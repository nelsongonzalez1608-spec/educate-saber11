#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parches de texto sobre el cuaderno armado (revisión del 24 nov, 6 revisores).

Las páginas de misión de Matemáticas, Lectura Crítica y Sociales M1–M2 traen el instrumento recortado del PDF entregado
(no hay módulo que regenerar). Para corregir una frase de esas páginas se tapa con el color del fondo que tiene alrededor y
se escribe la corrección encima, con la misma letra, tamaño y color (pdfplumber da los tres). También sirve para subrayar.

    python3 parches.py                  # aplica PARCHES a entregables/Cuaderno_Saber11_completo_398_paginas.pdf
arma_pdf.py lo llama al final, así que los parches sobreviven a un rearmado.

PARCHES: (página, texto viejo, texto nuevo, ocurrencia) · ocurrencia None = todas · texto nuevo None = solo subrayar.
El texto nuevo debe caber más o menos en el espacio del viejo (no empuja lo que sigue en la línea).
"""
import os
import subprocess
import tempfile

import pdfplumber
import pikepdf
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
COMPLETO = os.path.join(RAIZ, "entregables", "Cuaderno_Saber11_completo_398_paginas.pdf")

PARCHES = [
    # Matemáticas
    (14, "La cuarta opción es cierta pero no explica nada:", "La tercera opción (C) es cierta pero no explica nada:", None),
    (19, "página 282", "página 283", 1),                       # pregunta 8 de M2 (la 7 sí está en la 282)
    (25, "78,5 es el área en metros cuadrados", "78,5 es un cuarto del área total", None),
    # Lectura Crítica
    (70, "cuatro preguntas seguidas", "tres preguntas seguidas", None),
    (81, "transgrede", None, None),                            # el enunciado pide la «palabra subrayada»
    # Sociales
    (124, "página 99", "página 116", None),
    (124, "más no", "mas no", None),
]


def _hex(c):
    if c is None:
        return "#1E2230"
    if len(c) == 1:
        v = round(c[0] * 255)
        return f"#{v:02X}{v:02X}{v:02X}"
    if len(c) == 3:
        return "#" + "".join(f"{round(x * 255):02X}" for x in c)
    if len(c) == 4:   # CMYK
        cc, m, y, k = c
        return "#" + "".join(f"{round(255 * (1 - x) * (1 - k)):02X}" for x in (cc, m, y))
    return "#1E2230"


def _buscar(page, viejo):
    """Cajas (x0, top, x1, bottom, palabra0) de cada aparición de `viejo` en una sola línea, sin repetidas."""
    ws = page.extract_words(extra_attrs=["fontname", "size", "non_stroking_color"], keep_blank_chars=False)
    toks = viejo.split()
    vistos, out = set(), []
    for i in range(len(ws)):
        grupo = ws[i:i + len(toks)]
        if len(grupo) < len(toks):
            break
        ok = all(t == w["text"] or (k == len(toks) - 1 and w["text"].startswith(t)) or
                 (k == 0 and w["text"].endswith(t))
                 for k, (t, w) in enumerate(zip(toks, grupo)))
        if not ok or len({round(w["top"]) for w in grupo}) > 1:
            continue
        clave = (round(grupo[0]["x0"], 1), round(grupo[0]["top"], 1))
        if clave in vistos:
            continue
        vistos.add(clave)
        out.append((grupo[0]["x0"], grupo[0]["top"], grupo[-1]["x1"], grupo[-1]["bottom"], grupo[0]))
    return out


def _fondo(png, escala, x0, top, x1, bottom):
    """El color del papel alrededor de la frase: la mediana de una franja justo encima y debajo."""
    im = Image.open(png).convert("RGB")
    px = []
    for y in (top - 1.2, bottom + 1.0):
        for k in range(12):
            x = x0 + (x1 - x0) * k / 11
            px.append(im.getpixel((int(x * escala), int(y * escala))))
    px.sort(key=sum)
    r, g, b = px[len(px) // 2]
    return f"#{r:02X}{g:02X}{b:02X}"


def _visible(png, escala, x0, top, x1, bottom):
    """¿Hay tinta en la caja? Si la caja es del color del papel, la palabra está tapada."""
    im = Image.open(png).convert("L")
    caja = im.crop((int(x0 * escala), int(top * escala), int(x1 * escala), int(bottom * escala)))
    px = list(caja.getdata())
    if not px:
        return False
    fondo = sorted(px)[len(px) * 3 // 4]
    oscuros = sum(1 for v in px if v < fondo - 60)
    return oscuros / len(px) > 0.04


def aplicar(ruta=COMPLETO, parches=PARCHES):
    hechos = []
    pdf = pikepdf.open(ruta, allow_overwriting_input=True)
    vivos = []
    with pdfplumber.open(ruta) as plumb, tempfile.TemporaryDirectory() as tmp:
        for pag in sorted({p[0] for p in parches}):
            page = plumb.pages[pag - 1]
            W, H = float(page.width), float(page.height)
            png = os.path.join(tmp, f"{pag}")
            esc = 4
            subprocess.run(["pdftoppm", "-f", str(pag), "-l", str(pag), "-r", str(72 * esc), "-png",
                            "-singlefile", ruta, png], check=True)
            png += ".png"
            svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}pt" height="{H}pt" viewBox="0 0 {W} {H}">']
            for p, viejo, nuevo, n in [x for x in parches if x[0] == pag]:
                cajas = _buscar(page, viejo)
                if not cajas:
                    raise ValueError(f"p. {pag}: no encontré «{viejo}»")
                # solo las que se ven: el original incrustado deja copias tapadas en otras posiciones
                cajas = [c for c in cajas if _visible(png, esc, *c[:4])]
                if not cajas:
                    raise ValueError(f"p. {pag}: «{viejo}» no está a la vista")
                elegidas = cajas if n is None else [cajas[n]]
                for x0, top, x1, bottom, w0 in elegidas:
                    size = float(w0["size"])
                    color = _hex(w0.get("non_stroking_color"))
                    if nuevo is None:      # subrayar
                        svg.append(f'<line x1="{x0}" y1="{bottom + 0.6}" x2="{x1}" y2="{bottom + 0.6}" '
                                   f'stroke="{color}" stroke-width="{max(0.5, size * 0.07):.2f}"/>')
                    else:
                        bg = _fondo(png, esc, x0, top, x1, bottom)
                        bold = "Bold" in w0["fontname"]
                        italic = "Italic" in w0["fontname"]
                        svg.append(f'<rect x="{x0 - 0.6}" y="{top - 0.6}" width="{x1 - x0 + 1.2}" '
                                   f'height="{bottom - top + 1.4}" fill="{bg}"/>')
                        nuevo_esc = nuevo.replace("&", "&amp;").replace("<", "&lt;")
                        svg.append(f'<text x="{x0}" y="{bottom - size * 0.2:.2f}" font-family="Carlito" '
                                   f'font-size="{size:.2f}" font-weight="{"700" if bold else "400"}" '
                                   f'font-style="{"italic" if italic else "normal"}" fill="{color}">{nuevo_esc}</text>')
                    hechos.append((pag, viejo, nuevo))
            svg.append("</svg>")
            fs = os.path.join(tmp, f"o{pag}.svg")
            fp = os.path.join(tmp, f"o{pag}.pdf")
            open(fs, "w", encoding="utf-8").write("".join(svg))
            subprocess.run(["rsvg-convert", "-f", "pdf", "-o", fp, fs], check=True)
            o = pikepdf.open(fp)
            vivos.append(o)
            pdf.pages[pag - 1].add_overlay(o.pages[0])
        pdf.save(ruta, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
    return hechos


if __name__ == "__main__":
    for h in aplicar():
        print("parche", h)
