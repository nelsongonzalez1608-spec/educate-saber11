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
import base64

_REV = base64.b64encode(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "logo_educate_reverso.png"), "rb").read()).decode()


def logo_reverso(x, y, h):
    """Logo para fondo azul, sin recuadro blanco: «Para el Saber» en blanco (libro/logo_educate_reverso.png)."""
    w = logo_w(h)
    return (f'<image x="{x}" y="{y}" width="{w}" height="{h}" xlink:href="data:image/png;base64,{_REV}" '
            f'preserveAspectRatio="xMidYMid meet"/>')

LIBRO = os.path.dirname(os.path.realpath(__file__)) + "/"
PAGS = ["7–59", "60–112", "113–165", "166–214", "215–263", "264–312", "313–395"]   # = apertura_b.MAPA
NIVELES = [("mate", "MATEMÁTICAS"), ("lc", "LECTURA"), ("soc", "SOCIALES"), ("bio", "BIOLOGÍA"),
           ("qui", "QUÍMICA"), ("fis", "FÍSICA"), ("ing", "INGLÉS")]


def _mezcla(c, k, con="#FFFFFF"):
    c, o = c.lstrip("#"), con.lstrip("#")
    a = [int(c[i:i + 2], 16) for i in (0, 2, 4)]
    b = [int(o[i:i + 2], 16) for i in (0, 2, 4)]
    return "#" + "".join(f"{round(x + (y - x) * k):02X}" for x, y in zip(a, b))


def bloque(x, y, w, h, d, c, area, n, nombre, tinta, pags=""):
    """Bloque isométrico: frente (x, y, w, h) en el color del área, tapa clara, lado oscuro, motivo blanco."""
    k = d * 0.58
    tapa, lado = _mezcla(c, .45), _mezcla(c, .35, "#000000")
    s = (f'<polygon points="{x},{y} {x+d},{y-k} {x+w+d},{y-k} {x+w},{y}" fill="{tapa}" stroke="{tinta}" stroke-width="3" stroke-linejoin="round"/>'
         f'<polygon points="{x+w},{y} {x+w+d},{y-k} {x+w+d},{y+h-k} {x+w},{y+h}" fill="{lado}" stroke="{tinta}" stroke-width="3" stroke-linejoin="round"/>'
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" stroke="{tinta}" stroke-width="3"/>')
    m = motivos.motivo(area, "#FFFFFF").replace(
        "<svg ", f'<svg x="{x + w/2 - 56}" y="{y + 8}" width="112" height="112" opacity="0.9" ', 1)
    s += m
    # las seis misiones del área: se pintan cuando se superan
    lado, gap = 24, 7
    x6 = x + (w - (6 * lado + 5 * gap)) / 2
    for i in range(6):
        s += (f'<rect x="{x6 + i*(lado+gap):.1f}" y="{y + h - 84}" width="{lado}" height="{lado}" rx="5" '
              f'fill="none" stroke="#FFFFFF" stroke-width="2.5"/>')
    if pags:                                   # el índice va en la tapa de cada nivel
        s += TX(x + w / 2 + d * 0.5, y - k / 2 + 7, f"p. {pags}", 19, TINTA_B, MONO, "700", anchor="middle")
    s += TX(x + 16, y + h - 20, f"{n:02d}", 22, "#FFFFFF", MONO, "700")
    s += TX(x + w - 14, y + h - 20, nombre, 17, "#FFFFFF", MONO, "700", anchor="end")
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
    b.append(logo_reverso(M + 10, 90, 104) if oscuro else logo(M + 10, 96, 92))
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
    w, h, d = 210, 214, 92
    x0, y0 = 120, 2010
    for n, (area, nombre) in enumerate(NIVELES):
        x, yb = x0 + n * 228, y0 - n * 152
        b.append(bloque(x, yb, w, h, d, motivos.AREA_COLOR[area], area, n + 1, nombre, borde, PAGS[n]))
    # la meta, arriba de la escalera: un 500 grande
    tope_x, tope_y = x0 + 6 * 228 + d * 0.5, y0 - 6 * 152 - d * 0.58
    mx = tope_x + w / 2
    acento = FOSFO if oscuro else EDU_ORO
    b.append(TX(mx, tope_y - 120, "500", 190, acento if oscuro else TINTA_B, SHA, "800", anchor="middle"))
    if not oscuro:
        w5 = twf("500", 190, SHA, "800")
        b.insert(len(b) - 1, f'<rect x="{mx - w5/2 - 14}" y="{tope_y - 250}" width="{w5 + 28}" height="120" rx="10" '
                             f'fill="{FOSFO}" transform="rotate(-2 {mx} {tope_y - 190})"/>')
    b.append(TX(mx, tope_y - 330, "LA META", 26, suave, MONO, "700", anchor="middle", ls=4))
    b.append(TX(mx, tope_y - 50, "mi meta:", 30, suave if oscuro else GRAY, SHA, "700", anchor="end"))
    b.append(f'<line x1="{mx + 12}" y1="{tope_y - 44}" x2="{mx + 150}" y2="{tope_y - 44}" '
             f'stroke="{suave}" stroke-width="3" stroke-dasharray="2 8" stroke-linecap="round"/>')
    b.append(TX(x0 + 6, y0 - 6 * 152 - 30, "cada área es un nivel:", 34, suave if oscuro else EDU_ORO, SHA, "700"))
    b.append(TX(x0 + 6, y0 - 6 * 152 + 14, "pinta una casilla por misión", 34, suave if oscuro else EDU_ORO, SHA, "700"))

    # la etiqueta del cuaderno
    ly = 2290
    b.append(rect(M, ly, CW, 210, "#FFFFFF", r=22, stroke=borde, sw=3))
    b.append(f'<rect x="{M+8}" y="{ly+8}" width="{CW}" height="210" rx="22" fill="none" stroke="{borde}" stroke-opacity=".0"/>')
    for k, (lab, x1, x2) in enumerate([("NOMBRE", M + 40, M + 1080), ("COLEGIO", M + 1140, W - M - 40)]):
        b.append(TX(x1, ly + 70, lab, 22, GRAY, MONO, "700", ls=2))
        b.append(line(x1, ly + 150, x2, ly + 150, LGRAY, 2.6))
    b.append(TX(W / 2, H_PAGE - 40, "EDUCATE · Aprende · Practica · Avanza", 20, suave, MONO, anchor="middle", ls=2))
    return b


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/claude-0"
    os.makedirs(out, exist_ok=True)
    for v in "AB":
        f = os.path.join(out, f"portada_{v}.svg")
        svg_close(portada(v), f)
        subprocess.run(["rsvg-convert", "-w", "1000", f, "-o", f[:-4] + ".png"], check=True)
    print("listo", out)


# ── variante con apuntes de diario (Nelson, 20 nov): garabatos a mano en blanco tenue sobre el azul ──
def _mano(x, y, txt, size=46, rot=0, op=.27):
    from bitacora import HAND
    return (f'<text x="{x}" y="{y}" font-family="{HAND}, Caveat, cursive" font-size="{size}" fill="#FFFFFF" '
            f'fill-opacity="{op}" transform="rotate({rot} {x} {y})">{txt}</text>')


def _trazo(d, op=.25, sw=3.2):
    return (f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-opacity="{op}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def apuntes():
    """Notas de cuaderno, como las que deja un estudiante en los márgenes: una por área, sin tapar nada."""
    s = []
    # junto al título, arriba a la derecha
    s.append(_mano(1270, 300, "a² + b² = c²", 54, -6))
    s.append(_trazo("M1262 318 Q1420 332 1560 312"))                       # subrayado a mano
    s.append(_mano(1600, 420, "¿y si…?", 50, 4))
    s.append(_trazo("M1590 440 q-40 40 -10 90 l-12 -18 m12 18 l18 -12"))   # flechita curva
    s.append(_mano(1700, 230, "H₂O", 50, -3))
    # margen izquierdo, entre el título y la escalera
    s.append(_mano(120, 820, "v = d / t", 50, -4))
    s.append(_mano(160, 930, "«leer entre líneas»", 44, 3))
    s.append(_trazo("M150 950 q170 -30 330 4"))
    s.append(_mano(560, 760, "sin θ", 48, 8))
    s.append(_trazo("M548 712 a64 44 -8 1 0 120 6 a64 44 -8 1 0 -120 -6", sw=2.6))   # nota encerrada
    s.append(_mano(740, 900, "I have been…", 44, -5))
    # abajo a la derecha, bajo la escalera
    s.append(_mano(1250, 1900, "1991 · Constitución", 46, -3))
    s.append(_mano(1450, 2040, "Δ = cambio", 48, 4))
    s.append(_mano(1200, 2170, "ojo: primero el porqué", 44, -2))
    s.append(_trazo("M1190 2190 q260 -18 500 6"))
    s.append(_trazo("M1760 1960 l40 40 m0 -40 l-40 40", sw=3))               # una equis de «descartada»
    s.append(_trazo("M1660 1880 l18 20 l36 -42", sw=3.4))                     # chulito
    # espiral y estrellita de margen, sin cliché: un garabato de lápiz
    s.append(_trazo("M1180 760 q20 -20 40 0 q20 20 0 40 q-30 30 -60 0 q-40 -40 0 -80 q50 -50 100 0", sw=2.6))
    return "".join(s)


def portada_apuntes():
    b = portada("A")
    i = next(k for k, x in enumerate(b) if "M60 60h0" in x)        # justo encima de los puntos del fondo
    b.insert(i + 1, apuntes())
    return b
