#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""LAS 8 GUÍAS DE LECTURA CRÍTICA con el motor clase_viva.py, y la comparación de las clases 1–6
con la copia fija de las guías entregadas (libro/fuente_guias_lc/), diapositiva por diapositiva.

    python3 prueba_clase_viva_lc.py [carpeta de salida]      (por defecto /tmp/claude-0/guias_lc_prueba)
    python3 prueba_clase_viva_lc.py ../entregables/guias_lecturacritica     ← las entregables

Lo que el motor lee sale de lo que existe hoy:
  · el planeador real, plan_lc.py (FASES, MISIONES, DINAMICAS, RETOS, AVISOS, TALLER, BANCO, C7, C8);
  · los SELLOS de libro/matriz.py (reconstrucción mínima del 10 nov);
  · los textos reales, textos_lc.py sobre TEXTOS_GUIA_DOCENTE.md;
  · SABERES, ACTIVACION, TITULOS y LEADS, leídos (sin importarlo) de clase_viva_lc.py.
Lo que se perdió el 6 nov (RECUPERACION.md) y no está en otra parte —las claves del libro (lcN.py),
las preguntas ICFES (lcN_icfes.py) y el poema de M1 P4— se repone desde libro/fuente_guias_lc/: la
copia de las seis guías de contenido tal como estaban entregadas el 10 nov, antes de regenerarlas.
Se lee de ahí y no de entregables/ porque la salida puede ser esa misma carpeta. No borrarla: si
algún día vuelven esos módulos, esta prueba se puede pasar a leerlos directamente.

Las clases 7 y 8 salen de plan_lc.C7 y C8 (decisión de Nelson, 10 nov) y no se comparan: son nuevas.
Antes de escribir revisa que no diga «oficial» ni «preguntas reales del ICFES».
"""
import ast, html, json, os, re, sys, types

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
FUENTE = os.path.join(AQUI, "fuente_guias_lc")      # copia fija de las entregadas (10 nov)
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
        _, sc = escenas(os.path.join(FUENTE, NOMBRES[mis - 1]))
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
    os.makedirs(out, exist_ok=True)
    import plan_lc as P                     # lee los SELLOS de libro/matriz.py
    assert sorted((int(s[1]), int(s[3])) for s in P.SELLOS) == sorted((s[1], s[3]) for s in sellos), \
        "los sellos de matriz.py no son los de las guías entregadas"
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


NO_EN_HTML = ["oficial", "preguntas reales del ICFES"]


def revisar(out):
    for n in NOMBRES:
        s = open(os.path.join(out, n), encoding="utf-8").read()
        malo = [t for t in NO_EN_HTML if re.search(re.escape(t), s, re.I)]
        if malo:
            raise SystemExit(f"{n}: dice {malo}; el membrete es «Pregunta Saber 11»")


def main():
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0/guias_lc_prueba/"
    if os.path.exists(os.path.join(out, "matriz.py")):     # lo dejaba la versión anterior de esta prueba
        os.remove(os.path.join(out, "matriz.py"))
    A, CV = area_lc(out)
    CV.construir(A)
    revisar(out)
    total = 0
    for n in NOMBRES[:6]:
        d = comparar(os.path.join(FUENTE, n), os.path.join(out, n))
        total += len(d)
        print(f"{n:30s} {'IGUAL' if not d else f'{len(d)} diferencias'}")
        for x in d:
            print("   ·", x)
    print("\nLas clases 1–6 salen iguales a las entregadas (salvo --lc → --area)." if not total
          else f"\n{total} diferencias en total (clases 1–6).")


if __name__ == "__main__":
    main()
