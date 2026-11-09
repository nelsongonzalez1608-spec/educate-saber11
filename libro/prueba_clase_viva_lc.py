#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PRUEBA DEL MOTOR clase_viva.py · rehace las 8 guías de Lectura Crítica y las compara con
las entregadas (entregables/guias_lecturacritica/), diapositiva por diapositiva.

    python3 prueba_clase_viva_lc.py [carpeta de salida]      (por defecto /tmp/claude-0/guias_lc_prueba)

Nunca escribe en entregables/. Lo que el motor lee sale de lo que existe hoy:
  · el planeador real, plan_lc.py (FASES, MISIONES, DINAMICAS, RETOS, AVISOS, TALLER, BANCO);
  · los textos reales, textos_lc.py sobre TEXTOS_GUIA_DOCENTE.md;
  · SABERES, ACTIVACION, TITULOS y LEADS, leídos (sin importarlo) de clase_viva_lc.py.
Lo que se perdió el 6 nov (RECUPERACION.md) se repone desde las guías entregadas, que lo traen
incrustado: matriz.py (solo SELLOS, con un matriz.py provisional en la carpeta de salida),
las claves del libro (lcN.py), las preguntas ICFES (lcN_icfes.py) y el poema de M1 P4.
Si algún día vuelven esos módulos, esta prueba se puede pasar a leerlos directamente.

Compara cada diapositiva (html y guía del profe) y el resto de la página, con el único cambio
de nombre de la variable de color (--lc → --area), que no se ve.
"""
import ast, html, json, os, re, sys, types

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
ENTREGADAS = os.path.join(AQUI, "..", "entregables", "guias_lecturacritica")
NOMBRES = [f"LC_Clase{m}_Mision{m}.html" for m in range(1, 7)] + \
          ["LC_Clase7_Simulacro.html", "LC_Clase8_Devolucion.html"]


def escenas(ruta):
    s = open(ruta, encoding="utf-8").read()
    i = s.index("var SC = ") + len("var SC = ")
    j = s.index(";\nvar MOM = ", i)
    return s, json.loads(s[i:j].replace("<\\/", "</"))


def constantes_lc():
    """SABERES, ACTIVACION, TITULOS, LEADS de clase_viva_lc.py, sin importarlo (plan_lc no corre)."""
    src = open(os.path.join(AQUI, "clase_viva_lc.py"), encoding="utf-8").read()
    out = {}
    for n in ast.parse(src).body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") in ("SABERES", "ACTIVACION",
                                                                           "TITULOS", "LEADS"):
            out[n.targets[0].id] = ast.literal_eval(n.value)
    return out


def datos_de_entregadas():
    """Lo perdido, sacado de las guías entregadas: claves, preguntas ICFES, sellos y el poema."""
    claves, icfes, sellos, poema = {}, {}, [], ""
    un = lambda t: html.unescape(re.sub(r"<[^>]+>", "", t))
    for mis in range(1, 7):
        _, sc = escenas(os.path.join(ENTREGADAS, NOMBRES[mis - 1]))
        claves[mis], icfes[mis] = {}, []
        for e in sc:
            h = e["html"]
            for card in re.findall(r'<div class="card edge".*?es la clave del libro</div>', h):
                n = int(re.search(r"Libro · pregunta (\d+)", card).group(1))
                claves[mis][n] = re.search(r'class="keychip"[^>]*>([^<]*)<', card).group(1)
                m = re.search(r'<div class="sello"><b>[^<]*</b><span>([^<]*)</span>', card)
                if m:
                    sellos.append(("Lectura Crítica", mis, "", n, html.unescape(m.group(1))))
            if 'class="enun"' in h:
                e_ = un(re.search(r'<p class="enun">(.*?)</p>', h).group(1))
                ops = [un(o) for o in re.findall(r'<span class="L">[A-D]</span><span>(.*?)</span>', h)]
                icfes[mis].append(dict(e=e_, o=ops))
                if mis == 1 and len(icfes[mis]) == 4:
                    p = re.search(r'<div class="texto"><h3>.*?</h3><p>(.*?)</p>', h).group(1)
                    poema = "\n".join(html.unescape(v) for v in p.split("<br>"))
    return claves, icfes, sellos, poema


def area_lc(out):
    claves, icfes, sellos, poema = datos_de_entregadas()
    # matriz.py provisional (solo SELLOS) para que plan_lc importe
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "matriz.py"), "w", encoding="utf-8") as f:
        f.write("SELLOS = " + repr([tuple(s) for s in sellos]) + "\nTEXTOS = []\n")
    import plan_piezas
    plan_piezas.OUT = out.rstrip("/") + "/"
    import plan_lc as P
    import textos_lc
    import clase_viva as CV
    textos, advert = textos_lc.leer()
    t14 = textos.get((1, 4))
    if t14 is not None:
        t14["texto"] = t14["texto"] or poema
        t14["verso"] = True
    c = constantes_lc()
    return CV.Area(
        nombre="Lectura Crítica", prefijo="LC", fuerte="Si la lectura crítica no es tu fuerte",
        color=CV.color_de("Lectura Crítica"), P=P,
        claves_libro=lambda mis: claves[mis], preguntas_icfes=lambda mis: icfes[mis],
        textos=textos, advertencias=advert, saberes=c["SABERES"], activacion=c["ACTIVACION"],
        titulos=c["TITULOS"], leads=c["LEADS"], apoyo_fuerte="Lectura Crítica no es tu área",
        out=out), CV


def comparar(a, b):
    sa, sca = escenas(a)
    sb, scb = escenas(b)
    sb = sb.replace("--area", "--lc")
    scb = json.loads(json.dumps(scb).replace("--area", "--lc"))
    difs = []
    if len(sca) != len(scb):
        difs.append(f"n.º de diapositivas: entregada {len(sca)} · nueva {len(scb)}")
    for i, (x, y) in enumerate(zip(sca, scb), 1):
        for k in sorted(set(x) | set(y)):
            if x.get(k) != y.get(k):
                if k == "guia":
                    for g in sorted(set(x[k] or {}) | set(y[k] or {})):
                        if (x[k] or {}).get(g) != (y[k] or {}).get(g):
                            difs.append(f"diap. {i} · guía.{g}:\n      entregada: {str(x[k].get(g))[:300]}"
                                        f"\n      nueva:     {str(y[k].get(g))[:300]}")
                else:
                    difs.append(f"diap. {i} · {k}:\n      entregada: {str(x.get(k))[:300]}"
                                f"\n      nueva:     {str(y.get(k))[:300]}")
    cuerpo = lambda s: s[:s.index("var SC = ")] + s[s.index(";\nvar MOM = "):]
    if cuerpo(sa) != cuerpo(sb):
        difs.append("plantilla (CSS/JS/barra) distinta")
    return difs


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0/guias_lc_prueba/"
    A, CV = area_lc(out)
    CV.construir(A)
    total = 0
    for n in NOMBRES:
        d = comparar(os.path.join(ENTREGADAS, n), os.path.join(out, n))
        total += len(d)
        print(f"{n:30s} {'IGUAL' if not d else f'{len(d)} diferencias'}")
        for x in d:
            print("   ·", x)
    print("\nLas 8 guías salen iguales a las entregadas (salvo --lc → --area)." if not total
          else f"\n{total} diferencias en total.")


if __name__ == "__main__":
    main()
