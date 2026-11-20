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
    """Apuntes reales de un estudiante, en blanco tenue y trazo grueso: una ecuación resuelta paso a paso,
    un mapa conceptual, una gráfica con su tabla de datos y un triángulo con su razón. Sin tapar nada."""
    s = []
    M_ = lambda x, y, t, size=54, rot=0: _mano(x, y, t, size, rot, op=.34)
    L_ = lambda d, sw=5: _trazo(d, op=.32, sw=sw)
    # 1 · ecuación resuelta (arriba a la derecha, junto al título)
    ex, ey = 1250, 250
    s.append(M_(ex, ey, "2x + 5 = 17", 60))
    s.append(M_(ex, ey + 86, "2x = 12", 60))
    s.append(M_(ex, ey + 172, "x = 6", 64))
    s.append(L_(f"M{ex-14} {ey+122} h210 v68 h-210 z", 4.5))                     # resultado encerrado
    s.append(M_(ex + 420, ey + 40, "−5", 46))
    s.append(L_(f"M{ex+400} {ey+8} q46 30 0 70 l14 -4 m-14 4 l4 -14", 4))       # flechita del paso
    s.append(M_(ex + 360, ey + 128, "÷2", 46))
    s.append(L_(f"M{ex+340} {ey+96} q46 30 0 70 l14 -4 m-14 4 l4 -14", 4))
    # 2 · mapa conceptual (izquierda, entre el título y la escalera)
    cx, cy = 330, 820
    s.append(L_(f"M{cx-120} {cy} a120 52 0 1 0 240 0 a120 52 0 1 0 -240 0", 5))
    s.append(M_(cx - 82, cy + 18, "CÉLULA", 52))
    for (tx, ty, t) in [(70, 690, "núcleo"), (520, 690, "membrana"), (110, 985, "mitocondria")]:
        s.append(M_(tx, ty, t, 46))
    s.append(L_(f"M{cx-70} {cy-48} L170 704", 4))
    s.append(L_(f"M{cx+70} {cy-48} L560 704", 4))
    s.append(L_(f"M{cx-40} {cy+52} L230 950", 4))
    s.append(M_(560, 930, "→ energía", 44, -4))
    s.append(L_(f"M{cx+60} {cy+50} Q500 900 552 915", 4))
    # 3 · triángulo con su razón (centro, entre el mapa y el 500)
    tx0, ty0 = 860, 960
    s.append(L_(f"M{tx0} {ty0} L{tx0+300} {ty0} L{tx0+300} {ty0-200} Z", 5))
    s.append(L_(f"M{tx0+272} {ty0} v-28 h28", 3.5))
    s.append(L_(f"M{tx0+70} {ty0} a70 70 0 0 0 -8 -40", 4))
    s.append(M_(tx0 + 84, ty0 - 14, "θ", 44))
    s.append(M_(tx0 + 316, ty0 - 90, "op", 42))
    s.append(M_(tx0 + 100, ty0 - 128, "hip", 42, -30))
    s.append(M_(tx0 + 20, ty0 - 250, "sen θ = op / hip", 50, -3))
    # 4 · gráfica con su tabla de datos (abajo a la derecha, bajo la escalera)
    gx, gy = 1500, 2200
    s.append(L_(f"M{gx} {gy} V{gy-330} M{gx} {gy} H{gx+380}", 5))
    s.append(L_(f"M{gx-10} {gy-320} l10 -14 l10 14 M{gx+370} {gy-10} l14 10 l-14 10", 4))
    for k in range(4):                                  # los mismos datos de la tabla: d = 6t
        px, py = gx + 30 + k * 105, gy - 30 - k * 85
        s.append(f'<circle cx="{px}" cy="{py}" r="10" fill="#FFFFFF" fill-opacity=".36"/>')
    s.append(L_(f"M{gx+20} {gy-22} L{gx+370} {gy-305}", 3.5))
    s.append(M_(gx + 300, gy + 52, "t (s)", 42))
    s.append(M_(gx + 18, gy - 312, "d (m)", 42))
    tbx, tby = 1150, 1890
    s.append(L_(f"M{tbx} {tby} h220 M{tbx+90} {tby-60} v300", 4))
    s.append(M_(tbx + 24, tby - 16, "t", 44))
    s.append(M_(tbx + 120, tby - 16, "d", 44))
    for k, (a, d_) in enumerate([("0", "0"), ("1", "6"), ("2", "12"), ("3", "18")]):
        s.append(M_(tbx + 26, tby + 54 + k * 56, a, 44))
        s.append(M_(tbx + 118, tby + 54 + k * 56, d_, 44))
    s.append(M_(tbx - 10, tby + 300, "v = 6 m/s ✓", 46, -3))
    return s if False else "".join(s)


def portada_apuntes():
    b = portada("A")
    i = next(k for k, x in enumerate(b) if "M60 60h0" in x)        # justo encima de los puntos del fondo
    b.insert(i + 1, apuntes())
    return b
