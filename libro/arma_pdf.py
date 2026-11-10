#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma el PDF corregido del cuaderno (páginas 1 a 110) a partir del PDF entregado.

  · Las páginas que no son de misión (apertura 1–9, portadas de área 10, 53, 96) salen de su SVG
    regenerado (apertura.py, apertura2.py, apertura3.py) si existe; si no, se copian tal cual
    del PDF entregado.
  · Cada página de misión sale de dos capas:
      1. el MARCO nuevo: la hoja que dibujó rehace_hojas.py, sin el original incrustado;
      2. la página ORIGINAL del PDF entregado, puesta como Form XObject debajo de un recorte en
         cada tarjeta (la columna izquierda: el instrumento), movida y, si hizo falta, escalada
         igual que en el SVG.
    Así el instrumento conserva sus fuentes reales: el archivo pesa casi lo mismo que el
    original y el texto se puede buscar y copiar.
  · Regla 7 (Nelson, 10 nov): antes de incrustar la página original se le BORRA todo el texto que
    queda fuera de los recortes (`_solo_texto_visible`). Ese texto no se veía, pero pdftotext lo
    leía: el título «Pregunta real para entrenar», el membrete viejo («Pregunta oficial ICFES»,
    con año en algunas de Matemáticas) y «· 2 preguntas reales» de la cabecera seguían debajo.
    Solo se quitan operadores de texto (Tj, TJ, ', "); los trazos y rellenos quedan como estaban.

Armado final (10 nov 2026 · 398 páginas): `armar()` ya no arma solo las 1–110: arma el cuaderno
COMPLETO en el orden de tablero/manifiesto_hojas.json y `partir()` saca un PDF por sección. Las
páginas de misión de las 1–110 entregadas se componen como arriba (leyendo su página vieja,
`pagina_anterior`); todas las demás salen de su SVG. Antes hay que haber regenerado todo:

    python3 paginas.py                     # tablero/mapa_paginas.json
    python3 construye.py soc3 soc3_icfes … # módulos (cada uno en su proceso; traduce la numeración)
    python3 rehace_hojas.py                # las 98 hojas de misión de las 1–110 (pie nuevo)
    python3 apertura3.py                   # portadas de área (pie nuevo)
    python3 simulacro.py --cuaderno        # las 54 hojas de simulacro
    python3 cierre_b.py                    # cierre (396–397) y mensaje final (398)
    python3 apertura_b.py                  # apertura (1–6; la página 4 anida bio2_t4)
    python3 arma_pdf.py
    → entregables/Cuaderno_Saber11_completo_398_paginas.pdf y Cuaderno_01_… a Cuaderno_09_…
"""
import json
import os
import re
import tempfile
import xml.etree.ElementTree as ET

import pikepdf

import render

RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
LIBRO = os.path.join(RAIZ, "libro")
PDF = os.path.join(RAIZ, "entregables", "Cuaderno_Saber11_paginas_1_a_110.pdf")
S = 612 / 2000                     # 1 unidad del SVG en puntos (página completa)
H_PT = 792
NS = "{http://www.w3.org/2000/svg}"


def _sin_original(svg_txt, pag):
    """El marco: la misma hoja sin la página original. rehace_hojas.py la incrusta justo
    después de <defs>, antes del filtro de sombra del motor (<filter id="sh">)."""
    i = svg_txt.index(f'<g id="orig{pag}"')
    j = svg_txt.index('<filter id="sh"', i)
    return (svg_txt[:i] + svg_txt[j:]).replace(f'<use xlink:href="#orig{pag}"/>', "")


def _recortes(svg_txt):
    """Por cada instrumento: (x0, y0, x1, y1) del recorte en la página ORIGINAL, dy, y el
    translate/scale que le puso encajar()."""
    raiz = ET.fromstring(svg_txt)
    out = []
    for g in raiz.iter(NS + "g"):
        if g.get("class") != "instrumento":
            continue
        k, tx, ty = 1.0, 0.0, 0.0
        hijo = next(iter(g), None)
        if hijo is not None and hijo.tag == NS + "g" and "scale" in (hijo.get("transform") or ""):
            n = [float(v) for v in re.findall(r"-?[\d.]+", hijo.get("transform"))]
            tx, ty, k = n[0], n[1], n[2]
        cp = next(e for e in g.iter(NS + "clipPath"))
        r = next(iter(cp))
        x0, y0 = float(r.get("x")), float(r.get("y"))
        x1, y1 = x0 + float(r.get("width")), y0 + float(r.get("height"))
        tr = next(e for e in g.iter(NS + "g") if (e.get("transform") or "").startswith("translate(0 "))
        dy = float(re.findall(r"-?[\d.]+", tr.get("transform"))[1])
        out.append((x0, y0, x1, y1, dy, k, tx, ty))
    return out


def _capa_original(x0, y0, x1, y1, dy, k, tx, ty, nombre):
    """Operadores PDF: mover la página original como en el SVG y recortar su instrumento."""
    e = S * tx
    f = H_PT * (1 - k) - S * ty - k * S * dy
    rx, ry = x0 * S, H_PT - y1 * S
    rw, rh = (x1 - x0) * S, (y1 - y0) * S
    return (f"q {k:.5f} 0 0 {k:.5f} {e:.3f} {f:.3f} cm "
            f"{rx:.3f} {ry:.3f} {rw:.3f} {rh:.3f} re W n /{nombre} Do Q\n").encode()


def _mult(a, b):
    """Producto de matrices PDF [a b c d e f]: primero a, después b."""
    return [a[0] * b[0] + a[1] * b[2], a[0] * b[1] + a[1] * b[3],
            a[2] * b[0] + a[3] * b[2], a[2] * b[1] + a[3] * b[3],
            a[4] * b[0] + a[5] * b[2] + b[4], a[4] * b[1] + a[5] * b[3] + b[5]]


MUESTRA = ("Tj", "TJ", "'", '"')
DEJADOS = []                           # textos invisibles que no se pudieron quitar
POSICION = ("BT", "Tm", "Td", "TD", "T*", "'", '"')


def _solo_texto_visible(pdf, page, recortes):
    """Reescribe el contenido de `page` (en memoria, nunca en el archivo entregado) sin los
    operadores de texto cuyo renglón cae fuera de todos los recortes. Un texto se queda si su
    origen está a la izquierda del borde derecho del recorte y su renglón (de la altura de la
    letra hacia arriba a un tercio hacia abajo) toca el recorte en vertical. Si un texto invisible
    va seguido, en el mismo BT, de otro que se dibuja a continuación sin reposicionarse, se deja
    (quitarlo correría al siguiente): ese queda en `DEJADOS` para revisarlo. Devuelve cuántos
    operadores quitó."""
    ops = pikepdf.parse_content_stream(page)
    ctm, pila = [1, 0, 0, 1, 0, 0], []
    tm = tlm = [1, 0, 0, 1, 0, 0]
    tfs, tl = 1.0, 0.0
    decision = {}                      # índice del operador → True si se borra
    invisibles = set()
    ultimo_show = None                 # índice del último texto en este BT sin reposicionar
    for i, (args, op) in enumerate(ops):
        o = str(op)
        a = [float(v) for v in args] if o in ("cm", "Tm", "Td", "TD", "TL") else None
        if o == "q":
            pila.append(ctm)
        elif o == "Q":
            ctm = pila.pop() if pila else ctm
        elif o == "cm":
            ctm = _mult(a, ctm)
        elif o == "BT":
            tm = tlm = [1, 0, 0, 1, 0, 0]
        elif o == "Tf":
            tfs = float(args[1])
        elif o == "TL":
            tl = a[0]
        elif o == "Tm":
            tm = tlm = a
        elif o in ("Td", "TD"):
            tlm = _mult([1, 0, 0, 1, a[0], a[1]], tlm); tm = tlm
            if o == "TD":
                tl = -a[1]
        elif o in ("T*", "'", '"'):
            tlm = _mult([1, 0, 0, 1, 0, -tl], tlm); tm = tlm
        if o in POSICION:
            ultimo_show = None
        if o in MUESTRA:
            if ultimo_show is not None and decision.get(ultimo_show):
                decision[ultimo_show] = False          # el anterior se queda: este depende de él
            mtx = _mult(tm, ctm)
            x, y = mtx[4] / S, (H_PT - mtx[5]) / S          # origen en unidades del SVG
            alto = abs(mtx[3]) * tfs / S
            visible = any(x < x1 and y - alto <= y1 and y + alto / 3 >= y0
                          for x0, y0, x1, y1, *_ in recortes)
            decision[i] = not visible
            if not visible:
                invisibles.add(i)
            ultimo_show = i
    borrar = {i for i, v in decision.items() if v}
    DEJADOS.extend((page.objgen, i) for i in invisibles - borrar)
    nuevos = [(args, op) for i, (args, op) in enumerate(ops) if i not in borrar]
    page.Contents = pdf.make_stream(pikepdf.unparse_content_stream(nuevos))
    return len(borrar)


def _pagina_mision(nuevo, orig, svg, p_vieja, tmp):
    """Agrega a `nuevo` una página de misión de las 1–110 entregadas: el marco nuevo (SVG de
    rehace_hojas.py sin el original) y, debajo de los recortes, la página vieja `p_vieja` del PDF
    entregado. Devuelve el PDF del marco (tiene que seguir abierto hasta save())."""
    txt = open(svg, encoding="utf-8").read()
    marco_svg = os.path.join(tmp, f"m{p_vieja}.svg")
    open(marco_svg, "w", encoding="utf-8").write(_sin_original(txt, p_vieja))
    marco_pdf = os.path.join(tmp, f"m{p_vieja}.pdf")
    render.conv(marco_svg, marco_pdf)
    marco = pikepdf.open(marco_pdf)
    nuevo.pages.append(marco.pages[0])
    pg = pikepdf.Page(nuevo.pages[-1])
    recs = _recortes(txt)
    _solo_texto_visible(orig, orig.pages[p_vieja - 1], recs)    # regla 7: nada viejo debajo
    fx = nuevo.copy_foreign(pikepdf.Page(orig.pages[p_vieja - 1]).as_form_xobject())
    nombre = pg.add_resource(fx, pikepdf.Name.XObject, prefix="Orig")
    ops = b"".join(_capa_original(*r, nombre=str(nombre)[1:]) for r in recs)
    # cairo deja la matriz volteada al final del marco: se encierra entre q … Q para que
    # la página original entre con la matriz limpia (si no, sale de cabeza)
    pg.contents_add(pikepdf.Stream(nuevo, b"q\n"), prepend=True)
    pg.contents_add(pikepdf.Stream(nuevo, b"Q\n" + ops), prepend=False)
    return marco


# ───────── armado final · 398 páginas (10 nov 2026) ─────────
ENT = os.path.join(RAIZ, "entregables")
COMPLETO = os.path.join(ENT, "Cuaderno_Saber11_completo_398_paginas.pdf")
PARTES = [("Cuaderno_01_Apertura_p1-6.pdf", 1, 6),
          ("Cuaderno_02_Matematicas_p7-59.pdf", 7, 59),
          ("Cuaderno_03_LecturaCritica_p60-112.pdf", 60, 112),
          ("Cuaderno_04_Sociales_p113-165.pdf", 113, 165),
          ("Cuaderno_05_Biologia_p166-214.pdf", 166, 214),
          ("Cuaderno_06_Quimica_p215-263.pdf", 215, 263),
          ("Cuaderno_07_Fisica_p264-312.pdf", 264, 312),
          ("Cuaderno_08_Ingles_p313-395.pdf", 313, 395),
          ("Cuaderno_09_Cierre_p396-398.pdf", 396, 398)]


def armar(dest=COMPLETO):
    """El cuaderno completo en el orden del manifiesto (398 páginas). Las páginas de misión de las
    1–110 entregadas salen del marco + el original (`_pagina_mision`); todas las demás, de su SVG."""
    man = sorted(json.load(open(os.path.join(RAIZ, "tablero", "manifiesto_hojas.json"), encoding="utf-8")),
                 key=lambda h: h["pagina"])
    assert [h["pagina"] for h in man] == list(range(1, len(man) + 1)), "el manifiesto tiene huecos"
    orig = pikepdf.open(PDF)
    nuevo = pikepdf.new()
    rehechas = de_svg = 0
    vivos = []          # los PDF de origen tienen que seguir abiertos hasta save()
    with tempfile.TemporaryDirectory() as tmp:
        for h in man:
            svg = os.path.join(LIBRO, h["svg"] + ".svg")
            if not os.path.exists(svg):
                raise FileNotFoundError(f"página {h['pagina']}: falta {svg}")
            pv = h.get("pagina_anterior")
            if pv and pv <= len(orig.pages) and re.fullmatch(r"(m|lc|soc)\d_[ti]\d", h["svg"]):
                vivos.append(_pagina_mision(nuevo, orig, svg, pv, tmp))
                rehechas += 1
                continue
            out = os.path.join(tmp, f"{h['pagina']}.pdf")
            render.conv(svg, out)
            hoja = pikepdf.open(out); vivos.append(hoja)
            nuevo.pages.append(hoja.pages[0])
            de_svg += 1
        nuevo.save(dest, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
    return dest, rehechas, de_svg


def partir(completo=COMPLETO):
    """Un PDF por sección (PARTES), copiando las páginas del completo (comparten fuentes)."""
    todo = pikepdf.open(completo)
    salidas = []
    for nom, a, b in PARTES:
        n = pikepdf.new()
        for i in range(a - 1, b):
            n.pages.append(todo.pages[i])
        n.remove_unreferenced_resources()
        d = os.path.join(ENT, nom)
        n.save(d, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
        salidas.append(d)
    return salidas


if __name__ == "__main__":
    d, n, r = armar()
    print(f"{d}: {n} páginas de misión rehechas sobre el original · {r} desde su SVG · "
          f"{os.path.getsize(d) / 1e6:.1f} MB")
    print("pies:", render.verifica(d, "Aprende"))
    print("textos invisibles que se dejaron (dependían de otro):", len(DEJADOS))
    for p in partir(d):
        print(os.path.basename(p), render.verifica(p, "Aprende"), f"{os.path.getsize(p) / 1e6:.1f} MB")
