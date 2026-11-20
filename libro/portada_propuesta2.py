#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROPUESTA 2 de portada (Nelson, 20 nov: «se ve muy plana, es la portada de un cuaderno»).

La idea: cada área es un nivel. Siete bloques en 3D (isométricos, en el color de cada área y con su motivo)
forman una escalera que sube hacia la meta del estudiante. Es la gamificación del libro («Misión Saber 11»,
«el siguiente nivel») sin trofeos ni estrellas. Abajo, la etiqueta del cuaderno para escribir el nombre.
Dos variantes: A sobre azul institucional y B sobre papel claro.

    python3 portada_propuesta2.py <carpeta>   → portada_A.png y portada_B.png
"""
import os
import sys
import subprocess

from lib import *                    # noqa: F401,F403
from bitacora import TX, twf, SHA, MONO, TINTA_B, FOSFO
import motivos

LIBRO = os.path.dirname(os.path.realpath(__file__)) + "/"
NIVELES = [("mate", "MATEMÁTICAS"), ("lc", "LECTURA"), ("soc", "SOCIALES"), ("bio", "BIOLOGÍA"),
           ("qui", "QUÍMICA"), ("fis", "FÍSICA"), ("ing", "INGLÉS")]


def _mezcla(c, k, con="#FFFFFF"):
    c, o = c.lstrip("#"), con.lstrip("#")
    a = [int(c[i:i + 2], 16) for i in (0, 2, 4)]
    b = [int(o[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{round(x + (y - x) * k):02X}" for x, y in zip(a, b))


def bloque(x, y, w, h, d, c, area, n, nombre, tinta):
    """Bloque isométrico: frente (x, y, w, h) en el color del área, tapa clara, lado oscuro, motivo blanco."""
    k = d * 0.58
    tapa, lado = _mezcla(c, .45), _mezcla(c, .35, "#000000")
    s = (f'<polygon points="{x},{y} {x+d},{y-k} {x+w+d},{y-k} {x+w},{y}" fill="{tapa}" stroke="{tinta}" stroke-width="3" stroke-linejoin="round"/>'
         f'<polygon points="{x+w},{y} {x+w+d},{y-k} {x+w+d},{y+h-k} {x+w},{y+h}" fill="{lado}" stroke="{tinta}" stroke-width="3" stroke-linejoin="round"/>'
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" stroke="{tinta}" stroke-width="3"/>')
    m = motivos.motivo(area, "#FFFFFF").replace(
        "<svg ", f'<svg x="{x + w/2 - 62}" y="{y + 14}" width="124" height="124" opacity="0.9" ', 1)
    s += m
    s += TX(x + 16, y + h - 18, f"{n:02d}", 22, "#FFFFFF", MONO, "700")
    s += TX(x + w - 14, y + h - 18, nombre, 17, "#FFFFFF", MONO, "700", anchor="end")
    return s


def portada(variante):
    oscuro = variante == "A"
    fondo = EDU_AZUL if oscuro else "#FBF9F4"
    tinta = "#FFFFFF" if oscuro else TINTA_B
    suave = "#C9CDE8" if oscuro else GRAY
    borde = "#14144A" if oscuro else TINTA_B
    b = svg_open()
    b.append(rect(0, 0, W, H_PAGE, fondo, r=0))
    # puntos de cuaderno, muy tenues
    pts = "".join(f"M{x} {y}h0" for y in range(60, H_PAGE, 56) for x in range(60, W, 56))
    b.append(f'<path d="{pts}" stroke="{"#FFFFFF" if oscuro else "#1E2230"}" stroke-opacity="{.10 if oscuro else .07}" '
             f'stroke-width="5" stroke-linecap="round"/>')
    b.append(logo(M + 10, 96, 92, chip=oscuro, pad=16))
    b.append(TX(W - M - 10, 140, "CUADERNO DE TRABAJO", 24, suave, MONO, "700", anchor="end", ls=2))

    # título
    y = 520
    b.append(TX(M, y, "Saber", 250, tinta, SHA, "800"))
    x11 = M + twf("Saber", 250, SHA, "800") + 40
    w11 = twf("11", 250, SHA, "800")
    if oscuro:
        b.append(TX(x11, y, "11", 250, FOSFO, SHA, "800"))
    else:
        b.append(f'<rect x="{x11-14}" y="{y-178}" width="{w11+28}" height="150" rx="10" fill="{FOSFO}" transform="rotate(-2 {x11} {y})"/>')
        b.append(TX(x11, y, "11", 250, TINTA_B, SHA, "800"))
    b.append(TX(M + 6, y + 100, "42 misiones · 7 áreas · un solo número", 46, suave if oscuro else INK, SHA, "400"))

    # la escalera: cada área un nivel
    w, h, d = 210, 196, 92
    x0, y0 = 120, 2010
    for n, (area, nombre) in enumerate(NIVELES):
        x, yb = x0 + n * 228, y0 - n * 152
        b.append(bloque(x, yb, w, h, d, motivos.AREA_COLOR[area], area, n + 1, nombre, borde))
    # la meta, arriba de la escalera: se escribe
    mx, my = x0 + 6 * 228 + w / 2 + 40, y0 - 6 * 152 - 210
    b.append(f'<circle cx="{mx}" cy="{my}" r="104" fill="{"#FFFFFF" if oscuro else "#FFFFFF"}" stroke="{FOSFO if oscuro else EDU_ORO}" '
             f'stroke-width="6" stroke-dasharray="14 10"/>')
    b.append(TX(mx, my - 34, "MI META", 22, TINTA_B, MONO, "700", anchor="middle", ls=2))
    b.append(f'<line x1="{mx-62}" y1="{my+40}" x2="{mx+62}" y2="{my+40}" stroke="{LGRAY}" stroke-width="3"/>')
    b.append(TX(mx, my + 78, "de 500", 22, GRAY, SHA, "700", anchor="middle"))
    b.append(TX(x0 + 6, y0 - 6 * 152 - 30, "cada área es un nivel", 34, suave if oscuro else EDU_ORO, SHA, "700"))
    b.append(TX(x0 + 6, y0 - 6 * 152 + 14, "súbelos uno a uno", 34, suave if oscuro else EDU_ORO, SHA, "700"))

    # la etiqueta del cuaderno
    ly = 2290
    b.append(rect(M, ly, CW, 210, "#FFFFFF", r=22, stroke=borde, sw=3))
    b.append(f'<rect x="{M+8}" y="{ly+8}" width="{CW}" height="210" rx="22" fill="none" stroke="{borde}" stroke-opacity=".0"/>')
    for k, (lab, x1, x2) in enumerate([("NOMBRE", M + 40, M + 1080), ("COLEGIO", M + 1140, W - M - 40)]):
        b.append(TX(x1, ly + 70, lab, 22, GRAY, MONO, "700", ls=2))
        b.append(line(x1, ly + 150, x2, ly + 150, LGRAY, 2.6))
    b.append(TX(W / 2, H_PAGE - 40, "EDUCATE · PARA EL SABER", 20, suave, MONO, anchor="middle", ls=2))
    return b


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0"
    os.makedirs(out, exist_ok=True)
    for v in "AB":
        f = os.path.join(out, f"portada_{v}.svg")
        svg_close(portada(v), f)
        subprocess.run(["rsvg-convert", "-w", "1000", f, "-o", f[:-4] + ".png"], check=True)
    print("listo", out)
