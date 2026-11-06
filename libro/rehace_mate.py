#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corrige las 30 hojas de taller de Matemáticas (hallazgo 35) sin volver a escribir sus
instrumentos.

El problema: el motor perdido les dio tarjetas de 1090 aunque llevaban franja de vocabulario,
y la franja tapó el final de la segunda tarjeta. Los módulos m1…m6 se perdieron, pero el PDF
entregado tiene cada instrumento en vectores. Este script:

  1. toma la página del PDF entregado (pdftocairo → SVG) y la incrusta una vez en <defs>;
  2. lee de su texto (pdftotext -bbox) el número, la página del libro, el contexto, la
     estrategia y el subtítulo de la misión;
  3. arma la hoja con taller_base.py (tarjetas de 1010, franja, color del área) y en cada
     tarjeta muestra SOLO el recorte del instrumento original, en vectores; si el recorte no
     cabe en la tarjeta de 1010, encajar() lo escala anclado arriba.

Así no se transcribe nada a mano: lo que el estudiante lee es exactamente lo que se aprobó.

    python3 rehace_mate.py            # las 30 hojas
    python3 rehace_mate.py 33 34      # esas páginas del cuaderno
    COLOR_MATE="#A82424" python3 rehace_mate.py   # el marco en el rojo con que se entregaron
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from collections import defaultdict

from PIL import Image

import taller_base as tb
from taller_base import *

RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
PDF = os.path.join(RAIZ, "entregables", "Cuaderno_Saber11_paginas_1_a_110.pdf")
K = 2000 / 612                   # el PDF entregado se rindió a ancho completo: 1 pt = K unidades
AZUL_MATE = os.environ.get("COLOR_MATE", "#1F4E8C")   # COLOR_MATE=#A82424 para dejarlas en rojo
OLD_Y = (210, 210 + 1090 + 40)   # dónde estaban las dos tarjetas en el original
CLIP_X0, CLIP_X1 = M + 18, M + RX_OFF - 20   # sin el borde de la tarjeta ni la columna derecha


def _palabras(pag):
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "p.html")
        subprocess.run(["pdftotext", "-bbox", "-f", str(pag), "-l", str(pag), PDF, out], check=True)
        html = open(out, encoding="utf-8").read()
    ws = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',
                         html):
        x0, y0, x1, y1 = (float(v) * K for v in m.groups()[:4])
        t = m.group(5).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        ws.append((x0, y0, x1, y1, t))
    return ws


def _lineas(ws, x0, x1, y0, y1):
    """Texto de la zona, agrupado en renglones."""
    filas = defaultdict(list)
    for a, b, c, d, t in ws:
        if x0 <= a < x1 and y0 <= b < y1:
            filas[round(d / 6)].append((a, t))
    return [" ".join(t for _, t in sorted(v)) for _, v in sorted(filas.items())]


def _svg_original(pag):
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "p.svg")
        subprocess.run(["pdftocairo", "-svg", "-f", str(pag), "-l", str(pag), PDF, out], check=True)
        s = open(out, encoding="utf-8").read()
    s = re.sub(r"^<\?xml[^>]*>\s*", "", s)
    cuerpo = re.sub(r"^<svg[^>]*>", "", s.strip())
    cuerpo = re.sub(r"</svg>\s*$", "", cuerpo)
    # ids únicos por página, por si algún día se juntan dos en un mismo archivo
    cuerpo = re.sub(r'id="([^"]+)"', lambda m: f'id="p{pag}-{m.group(1)}"', cuerpo)
    cuerpo = re.sub(r'(xlink:href|href)="#([^"]+)"', lambda m: f'{m.group(1)}="#p{pag}-{m.group(2)}"', cuerpo)
    cuerpo = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#p{pag}-{m.group(1)})', cuerpo)
    return f'<g id="orig{pag}" transform="scale({K:.6f})">{cuerpo}</g>'


def _color_chip(png, y_card):
    """Color de la estrategia: el relleno del chip en la página original."""
    im = Image.open(png).convert("RGB")
    k = im.width / 2000
    for x in range(M + 770, M + 900):
        p = im.getpixel((int(x * k), int((y_card + 52) * k)))
        if max(p) - min(p) > 60 and sum(p) < 500:
            return "#%02X%02X%02X" % p
    return EDU_AZUL


def _tarjeta_original(ws, png, y_card):
    """Lo que dice la tarjeta original y dónde termina su instrumento."""
    cab = _lineas(ws, M + 100, M + 740, y_card + 10, y_card + 104)
    m = re.match(r"Pregunta (\d+) · la lees en tu libro, página (\d+)", cab[0])
    n, pag_libro = int(m.group(1)), int(m.group(2))
    ctx = cab[1] if len(cab) > 1 else ""
    chip_txt = " ".join(_lineas(ws, M + 740, M + 1290, y_card + 10, y_card + 80))
    m2 = re.match(r"Estrategia (\d+) · (.+)", chip_txt)
    est, est_nombre = int(m2.group(1)), m2.group(2).strip()
    # el recuadro «LO QUE SUBRAYÉ EN EL TEXTO» marca el final del instrumento
    fin = None
    for a, b, c, d, t in ws:
        if t == "SUBRAYÉ" and y_card < b < y_card + 1090 and a < M + 200:
            fin = d - 28 - 12          # renglón del rótulo − su alto − aire
    if fin is None:
        fin = y_card + 1090 - 40
    return dict(n=n, pag=pag_libro, ctx=ctx, est=est, est_nombre=est_nombre,
                color=_color_chip(png, y_card), y0=y_card + 118, y1=fin)


def _instrumento_recortado(pag, info, y_nueva):
    """Devuelve la función que pega el recorte del instrumento original en la tarjeta nueva."""
    dy = (y_nueva + 118) - info["y0"]
    cid = f"c{pag}-{info['n']}"

    def inst(b, x, y, w, h):
        x0, x1, y0, y1 = CLIP_X0, CLIP_X1, info["y0"], info["y1"]
        b.append(f'<clipPath id="{cid}"><rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}"/></clipPath>')
        b.append(f'<g transform="translate(0 {dy:.1f})"><g clip-path="url(#{cid})">'
                 f'<use xlink:href="#orig{pag}"/></g></g>')
        # caja invisible para que medir()/encajar() y verifica_cajas.py sepan cuánto ocupa
        b.append(f'<rect x="{x0}" y="{y0 + dy:.1f}" width="{x1 - x0}" height="{y1 - y0:.1f}" fill="none"/>')
        return y1 + dy
    return inst


def rehacer(pag, svg_nombre, mision):
    ws = _palabras(pag)
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-f", str(pag), "-l", str(pag), "-r", "100", "-png", "-singlefile",
                        PDF, os.path.join(tmp, "p")], check=True)
        png = os.path.join(tmp, "p.png")
        infos = [_tarjeta_original(ws, png, y) for y in OLD_Y]
    sub = _lineas(ws, M + 220, W - M - 660, 90, 125)
    tema, _, comp = (sub[0] if sub else "").partition(" · componente ")
    hoja = int(re.search(r"hoja (\d) de 5", " ".join(_lineas(ws, M + 220, W - M - 660, 125, 165))).group(1))

    configurar("Matemáticas", mision, comp, tema=tema, color=AZUL_MATE)
    usar_estrategias({i["est"]: (i["est_nombre"], i["color"]) for i in infos})
    tb.set_bloque(True)
    qs = []
    for info, y_n in zip(infos, (Y0, y_bloque2())):
        qs.append(dict(n=info["n"], est=info["est"], pag=info["pag"], ctx=info["ctx"],
                       inst=_instrumento_recortado(pag, info, y_n)))
    ruta = hoja_taller(svg_nombre, pag, hoja, qs[0], qs[1], vocab=True)
    # incrustar la página original una sola vez, en <defs>
    s = open(ruta, encoding="utf-8").read()
    s = s.replace("<defs>", "<defs>" + _svg_original(pag), 1)
    open(ruta, "w", encoding="utf-8").write(s)
    return ruta, infos


def hojas_mate():
    man = json.load(open(os.path.join(RAIZ, "tablero", "manifiesto_hojas.json"), encoding="utf-8"))
    out = []
    for h in man:
        m = re.fullmatch(r"m(\d)_t(\d)", h["svg"])
        if m:
            out.append((h["pagina"], h["svg"], int(m.group(1))))
    return sorted(out)


if __name__ == "__main__":
    pedidas = {int(a) for a in sys.argv[1:]}
    for pag, nombre, mis in hojas_mate():
        if pedidas and pag not in pedidas:
            continue
        ruta, infos = rehacer(pag, nombre, mis)
        print(f"ok p.{pag} {nombre}: " + " · ".join(
            f"preg {i['n']} (est {i['est']}, libro p.{i['pag']}, instrumento {i['y1'] - i['y0']:.0f} px)"
            for i in infos))
