#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma el PDF corregido del cuaderno (páginas 1 a 110) a partir del PDF entregado.

  · Las páginas que no son de misión (apertura, portadas) se copian tal cual.
  · Cada página de misión sale de dos capas:
      1. el MARCO nuevo: la hoja que dibujó rehace_hojas.py, sin el original incrustado;
      2. la página ORIGINAL del PDF entregado, puesta como Form XObject debajo de un recorte en
         cada tarjeta (la columna izquierda: el instrumento), movida y, si hizo falta, escalada
         igual que en el SVG.
    Así el instrumento conserva sus fuentes reales: el archivo pesa casi lo mismo que el
    original y el texto se puede buscar y copiar.

    python3 rehace_hojas.py && python3 arma_pdf.py
    → entregables/Cuaderno_Saber11_paginas_1_a_110_v2.pdf
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
DEST = os.path.join(RAIZ, "entregables", "Cuaderno_Saber11_paginas_1_a_110_v2.pdf")
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


def armar(dest=DEST):
    man = {h["pagina"]: h["svg"] for h in json.load(open(os.path.join(RAIZ, "tablero",
                                                                         "manifiesto_hojas.json")))}
    orig = pikepdf.open(PDF)
    nuevo = pikepdf.new()
    rehechas = 0
    with tempfile.TemporaryDirectory() as tmp:
        for p in range(1, len(orig.pages) + 1):
            svg = os.path.join(LIBRO, man[p] + ".svg")
            es_mision = re.fullmatch(r"(m|lc|soc)\d_[ti]\d", man[p]) is not None
            if not es_mision:
                nuevo.pages.append(orig.pages[p - 1])
                continue
            txt = open(svg, encoding="utf-8").read()
            marco_svg = os.path.join(tmp, f"{p}.svg")
            open(marco_svg, "w", encoding="utf-8").write(_sin_original(txt, p))
            marco_pdf = os.path.join(tmp, f"{p}.pdf")
            render.conv(marco_svg, marco_pdf)
            marco = pikepdf.open(marco_pdf)
            nuevo.pages.append(marco.pages[0])
            pg = pikepdf.Page(nuevo.pages[-1])
            fx = nuevo.copy_foreign(pikepdf.Page(orig.pages[p - 1]).as_form_xobject())
            nombre = pg.add_resource(fx, pikepdf.Name.XObject, prefix="Orig")
            ops = b"".join(_capa_original(*r, nombre=str(nombre)[1:]) for r in _recortes(txt))
            # cairo deja la matriz volteada al final del marco: se encierra entre q … Q para que
            # la página original entre con la matriz limpia (si no, sale de cabeza)
            pg.contents_add(pikepdf.Stream(nuevo, b"q\n"), prepend=True)
            pg.contents_add(pikepdf.Stream(nuevo, b"Q\n" + ops), prepend=False)
            rehechas += 1
        nuevo.save(dest, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
    return dest, rehechas


if __name__ == "__main__":
    d, n = armar()
    print(f"{d}: {n} páginas rehechas · {os.path.getsize(d) / 1e6:.1f} MB")
    print("pies:", render.verifica(d, "Aprende"))
