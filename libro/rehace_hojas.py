#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rehace las 84 hojas de misión ya entregadas (Matemáticas, Lectura Crítica y Sociales M1–M2)
con el motor actual, SIN volver a escribir sus instrumentos.

Por qué (6 nov 2026):
  · hallazgo 35: en las 30 hojas de taller de Matemáticas la franja de vocabulario tapaba la
    segunda tarjeta (tarjetas de 1090 con franja);
  · Matemáticas pasa a su azul #1F4E8C (decisión de Nelson: cada área, su color);
  · el salvavidas pasa a ser claro y único para todas las áreas, porque se escribe con lápiz.

Cómo: los módulos de cada misión se perdieron, pero el PDF entregado tiene cada instrumento en
vectores. Para cada página:
  1. pdftocairo → SVG de la página original, incrustado una sola vez en <defs>;
  2. pdftotext -bbox → número, página del libro, contexto, estrategia, competencia, membrete,
     rótulo de notas y subtítulo de la misión;
  3. taller_base.py arma la hoja nueva (marco, cabecera, columna derecha, salvavidas, franja) y
     en cada tarjeta muestra SOLO el recorte de la columna izquierda original. Si el recorte no
     cabe (tarjeta de 1090 → 1010), encajar() lo escala anclado arriba.

    python3 rehace_hojas.py                 # las 84
    python3 rehace_hojas.py 33 106          # esas páginas del cuaderno
    COLOR_MATE="#A82424" python3 rehace_hojas.py   # Matemáticas en el rojo con que se entregó
"""
import html as html_mod
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
K = 2000 / 612                    # el PDF entregado se rindió a ancho completo: 1 pt = K unidades
CLIP_X0, CLIP_X1 = M + 18, M + RX_OFF - 20   # sin el borde de la tarjeta ni la columna derecha

AREAS = {
    "m": ("Matemáticas", os.environ.get("COLOR_MATE", "#1F4E8C")),
    "lc": ("Lectura Crítica", EDU_ROJO),
    "soc": ("Sociales y Ciudadanas", EDU_ORO),
}


def _alto_original(area, tipo):
    """Así se entregaron (medido sobre las 110 páginas): Matemáticas usó 1090 en todo; en el
    taller con franja (el error), en el ICFES sin franja. LC y Sociales, 1010 con franja."""
    if area == "m":
        return 1090, tipo == "t"
    return 1010, True


# ───────── lectura del PDF entregado ─────────
def _palabras(pag):
    with tempfile.TemporaryDirectory() as tmp:
        out = os.path.join(tmp, "p.html")
        subprocess.run(["pdftotext", "-bbox", "-f", str(pag), "-l", str(pag), PDF, out], check=True)
        html = open(out, encoding="utf-8").read()
    ws = []
    for m in re.finditer(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',
                         html):
        x0, y0, x1, y1 = (float(v) * K for v in m.groups()[:4])
        t = html_mod.unescape(m.group(5))
        ws.append((x0, y0, x1, y1, t))
    return ws


def _lineas(ws, x0, x1, y0, y1):
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
    cuerpo = re.sub(r'id="([^"]+)"', lambda m: f'id="p{pag}-{m.group(1)}"', cuerpo)
    cuerpo = re.sub(r'(xlink:href|href)="#([^"]+)"', lambda m: f'{m.group(1)}="#p{pag}-{m.group(2)}"', cuerpo)
    cuerpo = re.sub(r'url\(#([^)]+)\)', lambda m: f'url(#p{pag}-{m.group(1)})', cuerpo)
    return f'<g id="orig{pag}" transform="scale({K:.6f})">{cuerpo}</g>'


def _color(png, xs, y):
    """Primer píxel saturado y oscuro en esa fila: el relleno del chip de estrategia."""
    im = Image.open(png).convert("RGB")
    k = im.width / 2000
    for x in xs:
        p = im.getpixel((int(x * k), int(y * k)))
        if max(p) - min(p) > 60 and sum(p) < 520:
            return "#%02X%02X%02X" % p
    return EDU_AZUL


def _fin_instrumento(ws, y_card, alto):
    """El rótulo del recuadro de notas («LO QUE SUBRAYÉ…», «LO QUE ANOTÉ…») marca el final."""
    for a, b, c, d, t in ws:
        if t in ("SUBRAYÉ", "ANOTÉ") and y_card + 130 < b < y_card + alto and a < M + 200:
            rot = " ".join(_lineas(ws, M + 20, M + 700, b - 2, d + 2))
            return d - 28 - 12, rot
    return y_card + alto - 40, None


def _chip_y_competencia(ws, x0, x1, y_card, inicio):
    """El chip y la línea «competencia · …» van muy juntos: se separan por renglón."""
    ls = _lineas(ws, x0, x1, y_card + 10, y_card + 104)
    chip_ = next((l for l in ls if l.startswith(inicio)), "")
    comp = next((l for l in ls if l.startswith("competencia")), "")
    return chip_, comp


def _taller(ws, png, y_card, alto):
    cab = _lineas(ws, M + 100, M + 740, y_card + 10, y_card + 104)
    m = re.match(r"Pregunta (\d+) · la lees en tu libro, página (\d+)", cab[0])
    chip_txt, comp = _chip_y_competencia(ws, M + 740, M + 1290, y_card, "Estrategia")
    m2 = re.match(r"Estrategia (\d+) · (.+)", chip_txt)
    fin, rot = _fin_instrumento(ws, y_card, alto)
    return dict(n=int(m.group(1)), pag=int(m.group(2)), ctx=cab[1] if len(cab) > 1 else "",
                est=int(m2.group(1)), est_nombre=m2.group(2).strip(),
                comp=comp.replace("competencia · ", "", 1) if comp.startswith("competencia") else None,
                color=_color(png, range(M + 770, M + 900), y_card + 52),
                y0=y_card + 118, y1=fin, nota=rot)


def _icfes(ws, png, y_card, alto):
    titulo_ = " ".join(_lineas(ws, M + 100, M + 700, y_card + 10, y_card + 58))
    memb = " ".join(_lineas(ws, M + 100, M + 700, y_card + 58, y_card + 104))
    chip_txt, comp = _chip_y_competencia(ws, M + 700, M + 1300, y_card, "entrena")
    m2 = re.match(r"entrena la estrategia (\d+) · (.+)", chip_txt)
    return dict(titulo=titulo_, membrete=memb, est=int(m2.group(1)), est_nombre=m2.group(2).strip(),
                comp=comp.replace("competencia · ", "", 1) if comp.startswith("competencia") else None,
                color=_color(png, range(M + 1268, M + 1100, -1), y_card + 52),
                y0=y_card + 108, y1=y_card + alto - 30)


def _recorte(pag, info, y_nueva, clave):
    """Función-instrumento que pega el recorte de la columna izquierda original."""
    dy = (y_nueva + (info["y0"] - info["y_card"])) - info["y0"]
    cid = f"c{pag}-{clave}"

    def inst(b, x, y, w, h):
        x0, x1, y0, y1 = CLIP_X0, CLIP_X1, info["y0"], info["y1"]
        b.append(f'<clipPath id="{cid}"><rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0:.1f}"/></clipPath>')
        b.append(f'<g transform="translate(0 {dy:.1f})"><g clip-path="url(#{cid})">'
                 f'<use xlink:href="#orig{pag}"/></g></g>')
        # caja invisible: para que medir()/encajar() y verifica_cajas.py sepan cuánto ocupa
        b.append(f'<rect x="{x0}" y="{y0 + dy:.1f}" width="{x1 - x0}" height="{y1 - y0:.1f}" fill="none"/>')
        return y1 + dy
    return inst


# ───────── tarjeta ICFES con el recorte original ─────────
def _tarjeta_icfes_recorte(b, y, info, inst, k):
    est = info["est"]
    c = tb._marco_tarjeta(b, y)
    b.append(rect(M + 28, y + 22, 60, 60, c, r=12))
    b.append(buoy(M + 58, y + 52, 15))
    b.append(T(M + 112, y + 44, [info["titulo"]], 24, c, weight="700"))
    membrete(b, M + 112, y + 58, info["membrete"])
    chip_estrategia(b, M + 1275, y + 30, est, prefijo="entrena la estrategia", derecha=True)
    if info["comp"]:
        b.append(T(M + 1275, y + 92, [f"competencia · {info['comp']}"], 15, GRAY, style="italic", anchor="end"))
    tb._primera_idea(b, y, M + 1460, "Mi primera idea:")
    tb._instrumento(b, f"icfes-{k}", inst, M + 30, y + 108, y + tb.BLK_H - 30)
    columna_derecha(b, y, est, cierre=("¿En qué se parece a lo del taller?",
                                       "(el libro y el ICFES preguntan lo mismo de otra forma)"))


# ───────── una página ─────────
def rehacer(pag, svg_nombre):
    area, mis, tipo, num = re.fullmatch(r"([a-z]+)(\d)_([ti])(\d)", svg_nombre).groups()
    mis = int(mis)
    nombre_area, color = AREAS[area]
    alto, _ = _alto_original(area, tipo)
    vocab = (tipo == "t") or area != "m"          # la franja se queda donde estaba
    ws = _palabras(pag)
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-f", str(pag), "-l", str(pag), "-r", "100", "-png", "-singlefile",
                        PDF, os.path.join(tmp, "p")], check=True)
        png = os.path.join(tmp, "p.png")
        ys = (210, 210 + alto + 40)
        lee = _taller if tipo == "t" else _icfes
        infos = [dict(lee(ws, png, y, alto), y_card=y) for y in ys]
    sub = _lineas(ws, M + 220, W - M - 660, 90, 125)
    tema, _, comp = (sub[0] if sub else "").partition(" · componente ")
    linea3 = " ".join(_lineas(ws, M + 220, W - M - 660, 125, 165))
    nota = next((i.get("nota") for i in infos if i.get("nota")), None)

    configurar(nombre_area, mis, comp, tema=tema, color=color, nota=nota)
    usar_estrategias({i["est"]: (i["est_nombre"], i["color"]) for i in infos})
    tb.set_bloque(vocab)
    y_nuevas = (Y0, y_bloque2())
    if tipo == "t":
        hoja = int(re.search(r"hoja (\d) de 5", linea3).group(1))
        qs = [dict(n=i["n"], est=i["est"], pag=i["pag"], ctx=i["ctx"], comp=i["comp"],
                   inst=_recorte(pag, i, yn, i["n"])) for i, yn in zip(infos, y_nuevas)]
        ruta = hoja_taller(svg_nombre, pag, hoja, qs[0], qs[1], vocab=vocab)
    else:
        b = svg_open()
        cabecera(b, linea3)
        for k, (i, yn) in enumerate(zip(infos, y_nuevas), 1):
            _tarjeta_icfes_recorte(b, yn, i, _recorte(pag, i, yn, f"i{k}"), k)
        if vocab:
            franja_vocab(b)
        footer(b, pag, color, texto=f"{nombre_area} · Misión {mis} · Entrenamiento ICFES")
        ruta = OUT + svg_nombre + ".svg"
        svg_close(b, ruta)
    s = open(ruta, encoding="utf-8").read()
    s = s.replace("<defs>", "<defs>" + _svg_original(pag), 1)
    open(ruta, "w", encoding="utf-8").write(s)
    return ruta, infos


def hojas():
    man = json.load(open(os.path.join(RAIZ, "tablero", "manifiesto_hojas.json"), encoding="utf-8"))
    n = int(re.search(r"^Pages:\s+(\d+)", subprocess.run(["pdfinfo", PDF], capture_output=True,
                                                         text=True).stdout, re.M).group(1))
    # solo las páginas que existen en el PDF entregado (1–110): las nuevas tienen su propio módulo
    return sorted((h["pagina"], h["svg"]) for h in man
                  if h["pagina"] <= n and re.fullmatch(r"(m|lc|soc)\d_[ti]\d", h["svg"]))


if __name__ == "__main__":
    pedidas = {int(a) for a in sys.argv[1:]}
    for pag, nombre in hojas():
        if pedidas and pag not in pedidas:
            continue
        ruta, infos = rehacer(pag, nombre)
        print(f"ok p.{pag:3d} {nombre:8s} " + " · ".join(
            (f"preg {i['n']}" if "n" in i else "icfes") + f" est {i['est']} ({i['y1'] - i['y0']:.0f} px)"
            for i in infos))
