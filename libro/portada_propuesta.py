#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PROPUESTA de portada del cuaderno (Nelson, 20 nov): minimalista y con la gamificación del libro, sin clichés.

El libro juega con «Misión Saber 11», la «prueba de campo» y «el siguiente nivel». La portada toma eso y lo
vuelve una herramienta en vez de un adorno:
  · el tablero de la ruta: 7 áreas × 6 misiones + el simulacro de cada área. El estudiante pinta una casilla por
    cada misión superada: la portada se va llenando durante el curso (es la única «barra de progreso»);
  · el nivel: una escala de 0 a 500 donde marca su punto de partida y su meta;
  · nada de trofeos, estrellas, controles ni medallas. Blanco, tinta, un acento por área.
No reemplaza la portada actual (apertura_b.portada): es un ejemplo para que Nelson decida.

    python3 portada_propuesta.py   → libro/portada_propuesta.svg y .png en la carpeta que se le pase
"""
import os
import sys

from lib import *                    # noqa: F401,F403
from bitacora import TX, twf, SHA, MONO, TINTA_B, FOSFO
import apertura_b as AP

LIBRO = os.path.dirname(os.path.realpath(__file__)) + "/"


def rombo(cx, cy, r, c, sw=4, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<polygon points="{cx},{cy-r} {cx+r},{cy} {cx},{cy+r} {cx-r},{cy}" fill="white" '
            f'stroke="{c}" stroke-width="{sw}" stroke-linejoin="round"{d}/>')


def portada():
    b = svg_open()
    b.append(rect(0, 0, W, H_PAGE, "white", r=0))
    # identidad
    b.append(logo(M + 10, 96, 96))
    t = "CUADERNO DE TRABAJO"
    b.append(TX(W - M - 10, 140, t, 24, GRAY, MONO, "700", anchor="end", ls=2))

    # título
    y = 560
    b.append(TX(M, y, "Saber", 250, TINTA_B, SHA, "800"))
    x11 = M + twf("Saber", 250, SHA, "800") + 40
    b.append(TX(x11, y, "11", 250, EDU_AZUL, SHA, "800"))
    b.append(TX(M + 6, y + 96, "42 misiones · 7 áreas · un solo número", 44, INK, SHA, "400"))

    # ── el tablero de la ruta
    y0 = 860
    b.append(TX(M + 10, y0, "TU RUTA", 26, TINTA_B, MONO, "700", ls=3))
    b.append(TX(M + 210, y0, "pinta una casilla por cada misión superada", 26, GRAY, SHA, "400"))
    lado, gap, fila = 84, 20, 128
    x_nom, x_cas = M + 10, M + 600
    x_sim = x_cas + 6 * (lado + gap) + 70
    b.append(TX(x_sim, y0 + 64, "simulacro", 20, GRAY, MONO, "700", anchor="middle"))
    yy = y0 + 92
    for nm, pags, ia in AP.indice():
        if ia is None:
            continue
        c = AREAS[ia][1]
        cy = yy + lado / 2
        b.append(rect(x_nom, yy + 14, 6, lado - 28, c, r=3))          # acento vertical
        b.append(TX(x_nom + 26, cy + 4, nm, 32, TINTA_B, SHA, "700"))
        b.append(TX(x_nom + 26, cy + 40, f"p. {pags}", 20, GRAY, MONO, "400"))
        for k in range(6):
            x = x_cas + k * (lado + gap)
            b.append(rect(x, yy, lado, lado, "white", r=14, stroke=c, sw=4))
            b.append(TX(x + lado / 2, yy + lado / 2 + 9, f"M{k+1}", 24, c, MONO, "700", anchor="middle"))
        b.append(rombo(x_sim, cy, lado * 0.56, c, 4, "10 8"))
        yy += fila

    # ── el nivel: de dónde arranco y a dónde voy
    gx, gy0, gy1 = W - M - 150, y0 + 92, y0 + 92 + 7 * fila - 44
    b.append(TX(gx, y0, "NIVEL", 26, TINTA_B, MONO, "700", anchor="middle", ls=3))
    b.append(rect(gx - 14, gy0, 28, gy1 - gy0, "#F2F4F8", r=14, stroke=LGRAY, sw=2))
    for v in range(0, 501, 100):
        ty = gy1 - (gy1 - gy0) * v / 500
        b.append(rect(gx - 30, ty - 2, 14, 4, GRAY, r=2))
        b.append(TX(gx - 44, ty + 8, str(v), 22, GRAY, MONO, "400", anchor="end"))
    for k, lab in enumerate(("hoy", "meta")):
        ly = gy1 + 90 + k * 64
        b.append(f'<polygon points="{gx-110},{ly-10} {gx-86},{ly-24} {gx-86},{ly+4}" fill="{EDU_ORO}"/>')
        b.append(TX(gx - 70, ly, lab, 26, EDU_ORO, SHA, "700"))
        b.append(line(gx + 10, ly + 4, gx + 130, ly + 4, LGRAY, 2.6))
    b.append(TX(gx, gy1 + 230, "dibuja tus dos flechas", 20, GRAY, SHA, "400", anchor="middle"))
    b.append(TX(gx, gy1 + 258, "en la escala", 20, GRAY, SHA, "400", anchor="middle"))

    # ── de quién es
    yb = 2120
    b.append(TX(M + 10, yb, "ESTA BITÁCORA ES DE", 22, GRAY, MONO, "700", ls=2))
    b.append(line(M + 10, yb + 92, M + 1100, yb + 92, LGRAY, 2.6))
    b.append(TX(M + 1180, yb, "COLEGIO Y GRADO", 22, GRAY, MONO, "700", ls=2))
    b.append(line(M + 1180, yb + 92, W - M - 10, yb + 92, LGRAY, 2.6))
    b.append(TX(M + 10, yb + 190, "Este cuaderno no trae respuestas. Trae el camino: las respuestas las pones tú.",
                28, INK, SHA, "400"))
    t = "EDUCATE · PARA EL SABER"
    b.append(TX(W / 2, H_PAGE - 70, t, 20, GRAY, MONO, anchor="middle", ls=2))
    return b


if __name__ == "__main__":
    import subprocess
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0"
    os.makedirs(out, exist_ok=True)
    f = LIBRO + "portada_propuesta.svg"
    svg_close(portada(), f)
    subprocess.run(["rsvg-convert", "-w", "1400", f, "-o", os.path.join(out, "portada_propuesta.png")], check=True)
    print(f, "→", os.path.join(out, "portada_propuesta.png"))
