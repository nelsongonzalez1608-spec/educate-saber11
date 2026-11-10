#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Estilo B · BITÁCORA (bullet journal), escogido por Nelson el 10 nov 2026.

Piezas del ENTORNO de la página (no del contenido): tipografías de títulos medidas con su
archivo real, cuadrícula de puntos, resaltador, recuadros y círculos a mano, chispas y sellos.
Las usan taller_base.py (hojas de misión), ing_diario.py, apertura3.py (portadas de área),
apertura_b.py (apertura nueva) y simulacro.py. Sale de libro/estilos_propuesta.py (dirección B),
con tres cambios pedidos al aplicarlo:

  · los recuadros a mano NO se pasan de las esquinas (Nelson podría leer esas puntas como
    «líneas»): el trazo es un solo camino cerrado que pasa exacto por las cuatro esquinas;
  · los círculos a mano cierran sobre sí mismos (sin colita);
  · los puntos de la cuadrícula son gris neutro claro (#D1D1D1 ≈ K 18 % en imprenta).

Nada de esto usa el azar global (`random`): los instrumentos de las misiones dibujan su trazo
de lápiz con random.uniform() y tienen que salir idénticos con el estilo nuevo. Todo lo que
tiembla aquí usa su propio random.Random(semilla).

Tipografías (SIL OFL 1.1, en fuentes/propuesta/; instalar en ~/.local/share/fonts y fc-cache):
Shantell Sans (títulos) y Space Mono (rótulos). El texto de lectura sigue en Carlito.
"""
import math
import os
import random

from lib import *   # noqa: F401,F403
from PIL import ImageFont

FUENTES = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "fuentes")

# ───────── paleta del estilo (los colores de área no cambian) ─────────
FOSFO = "#FFE94A"         # resaltador amarillo (en CMYK: amarillo limpio)
FOSFO_2 = "#B8F2D2"       # resaltador menta
TINTA_B = "#1E2230"       # tinta de los recuadros y títulos
DOT = "#D1D1D1"           # puntos de la cuadrícula: gris neutro ≈ K 18 %
LN_GRIS = "#9AA3B5"       # recuadro de notas (no es texto)
CASILLA = "#C9CFDA"       # borde de las casillas de escribir (no es texto)

SHA, MONO, HAND = "Shantell Sans", "Space Mono", "Caveat"
_ARCH = {(SHA, "400"): "propuesta/shantell-sans-400.ttf",
         (SHA, "700"): "propuesta/shantell-sans-700.ttf",
         (SHA, "800"): "propuesta/shantell-sans-800.ttf",
         (MONO, "400"): "propuesta/space-mono-400.ttf",
         (MONO, "700"): "propuesta/space-mono-700.ttf",
         (HAND, "400"): "Caveat-Regular.ttf", (HAND, "700"): "Caveat-Bold.ttf"}
_FC = {}


def twf(txt, size, fam, weight="400"):
    """Ancho real de txt en la fuente de títulos (Carlito si fam es None). Como tw()."""
    if fam is None:
        return tw(txt, size, weight)
    k = (fam, weight, size)
    if k not in _FC:
        _FC[k] = ImageFont.truetype(os.path.join(FUENTES, _ARCH[(fam, weight)]),
                                    int(round(size * 4)))
    return _FC[k].getlength(txt) / 4.0


def fit(txt, size, fam, weight, maxw, minimo=10):
    """Baja el tamaño hasta que txt quepa en maxw (medido con twf)."""
    while size > minimo and twf(txt, size, fam, weight) > maxw:
        size -= 0.5
    return size


def TX(x, y, txt, size, color, fam=None, weight="400", anchor="start", rot=0, ls=0,
       style="normal"):
    font = f"{fam}, Carlito, sans-serif" if fam else UI
    return T(x, y, [txt], size, color, weight=weight, anchor=anchor, font=font, rot=rot, ls=ls,
             style=style)


def _pts(p):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in p)


def _trazo(pts, c, sw, cerrado=False):
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + (" Z" if cerrado else "")
    return (f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round"/>')


# ───────── adornos (sin filtros, sin transparencias, sin azar global) ─────────
def puntos(x0, y0, x1, y1, paso=40, c=DOT, r=2.1):
    """Cuadrícula de puntos en un solo trazado (segmentos de largo cero con punta redonda)."""
    d = []
    yy = y0
    while yy <= y1:
        xx = x0
        while xx <= x1:
            d.append(f"M{xx} {yy}h0")
            xx += paso
        yy += paso
    return (f'<path d="{"".join(d)}" stroke="{c}" stroke-width="{2 * r}" '
            f'stroke-linecap="round" fill="none"/>')


def fondo_puntos(b):
    b.append(puntos(40, 40, W - 40, H_PAGE - 40, 40))


def resaltador(x, y, w, h, fill=FOSFO, seed=5, rot=-0.8):
    """Trazo de resaltador DETRÁS de una palabra: un relleno, nunca una raya debajo."""
    rnd = random.Random(seed)
    p = [(x - 6, y + rnd.uniform(0, 4)), (x + w + 8, y + rnd.uniform(-3, 3)),
         (x + w + 4 + rnd.uniform(0, 6), y + h * 0.5), (x + w + 10, y + h + rnd.uniform(-3, 2)),
         (x - 4, y + h + rnd.uniform(-2, 3)), (x - 10 + rnd.uniform(0, 4), y + h * 0.5)]
    return (f'<polygon points="{_pts(p)}" fill="{fill}" '
            f'transform="rotate({rot} {x + w / 2:.1f} {y + h / 2:.1f})"/>')


def wob_rect(x, y, w, h, c, sw=3, fill=None, seed=7, amp=1.4, r_fill=4):
    """Recuadro a pulso: UN camino cerrado que pasa exacto por las cuatro esquinas (no se pasa
    de ellas) y tiembla solo entre esquina y esquina."""
    rnd = random.Random(seed)
    esquinas = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    pts = []
    for i in range(4):
        (ax, ay), (bx, by) = esquinas[i], esquinas[(i + 1) % 4]
        n = max(2, int(math.hypot(bx - ax, by - ay) / 60))
        pts.append((ax, ay))
        for j in range(1, n):
            t = j / n
            px, py = ax + (bx - ax) * t, ay + (by - ay) * t
            if ax == bx:
                px += rnd.uniform(-amp, amp)
            else:
                py += rnd.uniform(-amp, amp)
            pts.append((px, py))
    g = [rect(x, y, w, h, fill, r=r_fill)] if fill else []
    g.append(_trazo(pts, c, sw, cerrado=True))
    return "".join(g)


def wob_circle(cx, cy, r, c, sw=2.6, seed=9, fill=None):
    """Círculo a pulso que cierra sobre sí mismo (sin colita)."""
    rnd = random.Random(seed)
    a0 = rnd.uniform(0, 6.28)
    fase = rnd.uniform(0, 6.28)
    n = 36
    pts = []
    for i in range(n):
        a = a0 + i / n * 2 * math.pi
        rr = r * (1 + 0.035 * math.sin(2 * a + fase))
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    g = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>' if fill else ""
    return g + _trazo(pts, c, sw, cerrado=True)


def wob_vline(x, y0, y1, c="#C3C9D4", sw=2, seed=1):
    """Divisor vertical a pulso (los acentos verticales sí se permiten)."""
    rnd = random.Random(seed)
    pts = [(x + rnd.uniform(-1.4, 1.4), yy) for yy in range(int(y0), int(y1), 40)] + [(x, y1)]
    return _trazo(pts, c, sw)


def estrellita(cx, cy, r, c, sw=2.4):
    """Chispa de cuatro puntas (garabato de margen)."""
    return (_trazo([(cx, cy - r), (cx, cy + r)], c, sw)
            + _trazo([(cx - r, cy), (cx + r, cy)], c, sw)
            + _trazo([(cx - r * .55, cy - r * .55), (cx + r * .55, cy + r * .55)], c, sw * .7)
            + _trazo([(cx - r * .55, cy + r * .55), (cx + r * .55, cy - r * .55)], c, sw * .7))


def flechita(x1, y1, x2, y2, c, sw=2.6, bend=0.25, head=11, seed=3):
    """Flecha curva de margen, con su propio azar (hand_arrow usa el global)."""
    rnd = random.Random(seed)
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    cx, cy = mx + nx * L * bend, my + ny * L * bend
    pts = []
    for i in range(21):
        t = i / 20
        px = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * cx + t ** 2 * x2
        py = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * cy + t ** 2 * y2
        pts.append((px + rnd.uniform(-.8, .8), py + rnd.uniform(-.8, .8)))
    g = [_trazo(pts, c, sw)]
    ang = math.atan2(y2 - cy, x2 - cx)
    for s in (-1, 1):
        a = ang + math.pi + s * 0.48
        g.append(_trazo([(x2, y2), (x2 + head * math.cos(a), y2 + head * math.sin(a))], c, sw))
    return "".join(g)


def rot_g(frag, ang, cx, cy):
    return f'<g transform="rotate({ang} {cx:.1f} {cy:.1f})">{frag}</g>'


def sello(b, x, y, txt, c, size=19, h=44, pad=18, ang=-1.6, derecha=False):
    """Sello de caucho: doble borde en la tinta `c`, texto en Carlito medido con tw().
    Va en <g class="chip"> (el primer rect es el que mide verifica_cajas.py). Devuelve
    (x de inicio, ancho)."""
    w = tw(txt, size, "700") + 2 * pad
    x0 = x - w if derecha else x
    g = (f'<g class="chip" data-pad="{pad}">'
         + rect(x0, y, w, h, "white", r=4, stroke=c, sw=3)
         + rect(x0 + 5, y + 5, w - 10, h - 10, "none", r=2, stroke=c, sw=1.4)
         + T(x0 + w / 2, y + h / 2 + size * 0.36, [txt], size, c, weight="700", anchor="middle")
         + "</g>")
    b.append(rot_g(g, ang, x0 + w / 2, y + h / 2) if ang else g)
    return x0, w


def sello_mono(b, x, y, txt, c, size=24, h=None, pad=18, ang=0):
    """Sello rectangular con texto en Space Mono (portadas y apertura). Devuelve el ancho."""
    h = h or size * 2.2
    w = twf(txt, size, MONO, "700") + 2 * pad
    g = (rect(x, y, w, h, "white", r=4, stroke=c, sw=3)
         + rect(x + 5, y + 5, w - 10, h - 10, "none", r=2, stroke=c, sw=1.4)
         + TX(x + w / 2, y + h / 2 + size * 0.36, txt, size, c, MONO, "700", anchor="middle"))
    b.append(rot_g(g, ang, x + w / 2, y + h / 2) if ang else g)
    return w


def sello_redondo(cx, cy, r, lineas, c, ang):
    """Sello redondo: doble aro y hasta cuatro líneas (MAYÚSCULAS en Space Mono, lo demás a mano)."""
    g = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="5"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r - 14}" fill="none" stroke="{c}" stroke-width="2"/>']
    tam = [30, 34, 26, 26]
    ys = [-46, 0, 44, 80]
    for t, s_, dy in zip(lineas, tam, ys):
        fam, wt = (MONO, "700") if t.isupper() else (HAND, "700")
        s_ = fit(t, s_ if t.isupper() else s_ + 8, fam, wt, 2 * r - 70)
        g.append(TX(cx, cy + dy, t, s_, c, fam, wt, anchor="middle"))
    g.append(estrellita(cx - r * .55, cy - r * .62, 8, c, 2))
    g.append(estrellita(cx + r * .55, cy - r * .62, 8, c, 2))
    return rot_g("".join(g), ang, cx, cy)


def fondo_blanco(b, x, y, txt, size, fam=None, weight="400", anchor="start", pad=6, h=None,
                 style="normal"):
    """Rectángulo blanco detrás de un texto suelto sobre la cuadrícula (que los puntos no lo
    atraviesen). Medido con twf/tw."""
    w = (twf(txt, size, fam, weight) if fam else tw(txt, size, weight, style)) + 2 * pad
    x0 = x - pad if anchor == "start" else (x - w + pad if anchor == "end" else x - w / 2)
    h = h or size * 1.45
    b.append(rect(x0, y - size * 1.05, w, h, "white", r=2))


def titulo_b(b, x, y, txt, size, c=TINTA_B, marca=None, fill=FOSFO, seed=11):
    """Título en Shantell Sans ExtraBold; `marca` = la parte del título que lleva resaltador
    detrás (debe estar dentro de txt). Devuelve el ancho del título."""
    if marca:
        i = txt.index(marca)
        x2 = x + twf(txt[:i], size, SHA, "800")
        b.append(resaltador(x2, y - size * 0.78, twf(marca, size, SHA, "800"), size * 0.8, fill,
                            seed=seed))
    b.append(TX(x, y, txt, size, c, SHA, "800"))
    return twf(txt, size, SHA, "800")


def pie_b(b, pag, c, texto="Cuaderno de trabajo · Saber 11"):
    """Pie de la bitácora: «Aprende → Practica → Avanza» (lo busca render.verifica), el texto en
    Space Mono y el número de página en un recuadro a mano. Sin línea horizontal: regla 1."""
    y = H_PAGE - 90
    b.append(rect(M - 8, y - 26, 380, 46, "white", r=2))
    b.append(T(M, y + 8, ["Aprende"], 21, c, weight="700"))
    b.append(T(M + 116, y + 8, ["→"], 21, EDU_ORO, weight="700"))
    b.append(T(M + 146, y + 8, ["Practica"], 21, c, weight="700"))
    b.append(T(M + 262, y + 8, ["→"], 21, EDU_ORO, weight="700"))
    b.append(T(M + 292, y + 8, ["Avanza"], 21, c, weight="700"))
    tt = texto.upper()
    s = fit(tt, 14, MONO, "400", 1000)
    wt = twf(tt, s, MONO)
    b.append(rect(W / 2 - wt / 2 - 8, y - 18, wt + 16, 32, "white", r=2))
    b.append(TX(W / 2, y + 4, tt, s, GRAY, MONO, anchor="middle"))
    t = f"p. {pag}"
    wt = twf(t, 24, MONO, "700")
    b.append(wob_rect(W - M - wt - 24, y - 30, wt + 24, 50, TINTA_B, 2.4, fill="white", seed=88))
    b.append(TX(W - M - 12, y + 6, t, 24, TINTA_B, MONO, "700", anchor="end"))
