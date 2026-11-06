#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Piezas comunes del cuaderno completo (apertura, portadas de área, cierre)."""
import math, random
from base import *   # T, rect, line, logo, logo_w, wrap, PT, spath, jit, checkbox, grid_box, wlines, dots, esc

H_PAGE = 2588          # carta a W = 2000
M = 70                 # margen
CW = W - 2 * M         # ancho útil 1860

# paleta institucional (propuesta) + áreas
EDU_AZUL = "#242478"; EDU_ROJO = "#A82424"; EDU_VERDE = "#30843C"; EDU_ORO = "#C9821B"
CREMA = "#FFF8EC"; CREMA_LN = "#EAD9B4"; SOFT = "#F4F6FA"
AREAS = [("Matemáticas", "#1F4E8C"), ("Lectura Crítica", "#A82424"), ("Sociales y Ciudadanas", "#C9821B"),
         ("Ciencias Naturales", "#30843C"), ("Física", "#5B3E96"), ("Inglés", "#1BA0A8")]


def svg_open(h=H_PAGE):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="{W}" height="{h}" viewBox="0 0 {W} {h}">', "<defs>" + "".join(defs) + "</defs>",
            rect(0, 0, W, h, PAPER, r=0)]


def svg_close(body, path):
    body.append("</svg>")
    open(path, "w", encoding="utf-8").write("\n".join(body))


def frame(body, seccion, color, pag, sub=None):
    """Cabecera ligera: logo + nombre de sección. Devuelve y de inicio del contenido."""
    body.append(rect(0, 0, W, 150, SOFT, r=0))
    body.append(rect(0, 150, W, 6, color, r=0))
    body.append(logo(M, 40, 70))
    body.append(T(W - M, 78, [seccion.upper()], 26, color, weight="700", anchor="end", ls=3))
    if sub:
        body.append(T(W - M, 114, [sub], 20, GRAY, anchor="end"))
    return 156 + 60


def footer(body, pag, color, texto="Cuaderno de trabajo · Saber 11"):
    y = H_PAGE - 90
    body.append(line(M, y - 26, W - M, y - 26, LGRAY, 1.6))
    body.append(T(M, y + 8, ["Aprende"], 21, color, weight="700"))
    body.append(f'<circle cx="{M+120}" cy="{y}" r="5" fill="{EDU_ORO}"/>')
    body.append(T(M + 138, y + 8, ["Practica"], 21, color, weight="700"))
    body.append(f'<circle cx="{M+262}" cy="{y}" r="5" fill="{EDU_ORO}"/>')
    body.append(T(M + 280, y + 8, ["Avanza"], 21, color, weight="700"))
    body.append(T(W / 2, y + 8, [texto], 19, GRAY, anchor="middle"))
    body.append(T(W - M, y + 8, [str(pag)], 24, color, weight="700", anchor="end"))


def titulo(body, y, txt, color, size=72, sub=None, subcolor=GRAY):
    body.append(T(M, y + size * 0.8, [txt], size, color, weight="700"))
    y += size * 0.8 + 18
    if sub:
        svg, y = TJ(M, y, sub, CW, 28, subcolor, style="italic", lh=40)
        body.append(svg)
    return y + 16


def parrafo(body, x, y, txt, w_chars=100, size=30, color=INK, lh=None, font=UI, weight="400"):
    lh = lh or size * 1.42
    for ln in wrap(txt, w_chars):
        body.append(T(x, y + size, [ln], size, color, font=font, weight=weight))
        y += lh
    return y


def panel(body, x, y, w, h, color, title=None, fill="white", r=22, sw=3, dash=None, title_size=22):
    body.append(rect(x, y, w, h, fill, r=r, stroke=color, sw=sw, dash=dash))
    if title:
        tw = len(title) * title_size * 0.62 + 44
        body.append(rect(x + 26, y - title_size * 0.75, tw, title_size * 1.5, color, r=title_size * 0.75))
        body.append(T(x + 26 + tw / 2, y + title_size * 0.32, [title], title_size, "white", weight="700",
                      anchor="middle", ls=1))


# ───────── dibujo a mano: flechas y caritas ─────────
def hand_arrow(x1, y1, x2, y2, c, sw=4, bend=0.18, head=26, op=0.95):
    """Flecha curva con pulso de lápiz."""
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    nx, ny = -dy / L, dx / L
    cx, cy = mx + nx * L * bend, my + ny * L * bend
    pts = []
    for i in range(0, 21):
        t = i / 20
        px = (1 - t) ** 2 * x1 + 2 * (1 - t) * t * cx + t ** 2 * x2
        py = (1 - t) ** 2 * y1 + 2 * (1 - t) * t * cy + t ** 2 * y2
        pts.append((px + jit(0, 1.1), py + jit(0, 1.1)))
    g = [spath(pts, c, sw, op)]
    ang = math.atan2(y2 - cy, x2 - cx)
    for s in (-1, 1):
        a = ang + math.pi + s * 0.48
        g.append(spath([(x2, y2), (x2 + head * math.cos(a), y2 + head * math.sin(a))], c, sw, op))
    return "".join(g)


def face(cx, cy, r, mood="happy", c=INK, fill="#FFE9A8", sw=3.2):
    """Carita de trazo suave. mood: happy, calm, worried, determined, surprised, tired, proud."""
    g = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{c}" stroke-width="{sw}"/>']
    ex, ey = r * 0.36, r * 0.22
    er = max(2.2, r * 0.07)
    if mood == "determined":   # cejas rectas inclinadas hacia adentro, por encima del ojo
        g.append(spath([(cx - ex - r * .22, cy - ey - r * .40), (cx - ex + r * .16, cy - ey - r * .28)], c, sw))
        g.append(spath([(cx + ex + r * .22, cy - ey - r * .40), (cx + ex - r * .16, cy - ey - r * .28)], c, sw))
    elif mood == "worried":    # cejas hacia afuera
        g.append(spath([(cx - ex - r * .20, cy - ey - r * .26), (cx - ex + r * .16, cy - ey - r * .40)], c, sw))
        g.append(spath([(cx + ex + r * .20, cy - ey - r * .26), (cx + ex - r * .16, cy - ey - r * .40)], c, sw))
    if mood == "tired":
        g.append(spath([(cx - ex - r * .14, cy - ey), (cx - ex + r * .14, cy - ey)], c, sw))
        g.append(spath([(cx + ex - r * .14, cy - ey), (cx + ex + r * .14, cy - ey)], c, sw))
    else:
        g.append(f'<circle cx="{cx-ex}" cy="{cy-ey}" r="{er}" fill="{c}"/>')
        g.append(f'<circle cx="{cx+ex}" cy="{cy-ey}" r="{er}" fill="{c}"/>')
    mw = r * 0.5; my = cy + r * 0.28
    if mood in ("happy", "proud"):
        pts = [(cx - mw + i * (2 * mw / 10), my + math.sin(i / 10 * math.pi) * r * 0.22) for i in range(11)]
    elif mood == "calm":
        pts = [(cx - mw * .8 + i * (1.6 * mw / 10), my + math.sin(i / 10 * math.pi) * r * 0.08) for i in range(11)]
    elif mood == "worried" or mood == "tired":
        pts = [(cx - mw * .8 + i * (1.6 * mw / 10), my + r * .1 - math.sin(i / 10 * math.pi) * r * 0.14) for i in range(11)]
    elif mood == "determined":
        pts = [(cx - mw * .7, my + r * .02), (cx + mw * .7, my + r * .02)]
    elif mood == "surprised":
        g.append(f'<ellipse cx="{cx}" cy="{my+r*.05}" rx="{r*.16}" ry="{r*.22}" fill="none" stroke="{c}" stroke-width="{sw}"/>')
        pts = []
    else:
        pts = [(cx - mw, my), (cx + mw, my)]
    if pts: g.append(spath(pts, c, sw))
    if mood == "proud":
        g.append(f'<circle cx="{cx-r*.62}" cy="{cy+r*.12}" r="{r*.12}" fill="#F3A6A0" opacity="0.8"/>')
        g.append(f'<circle cx="{cx+r*.62}" cy="{cy+r*.12}" r="{r*.12}" fill="#F3A6A0" opacity="0.8"/>')
    return "".join(g)


def star(cx, cy, r, c):
    pts = []
    for i in range(10):
        rr = r if i % 2 == 0 else r * 0.45
        a = -math.pi / 2 + i * math.pi / 5
        pts.append(f"{cx + rr * math.cos(a):.1f},{cy + rr * math.sin(a):.1f}")
    return f'<polygon points="{" ".join(pts)}" fill="{c}"/>'


def num_badge(cx, cy, n, c, r=26, size=26):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>'
            + T(cx, cy + size * 0.36, [str(n)], size, "white", weight="700", anchor="middle"))


def write_box(body, x, y, w, h, c=LGRAY, lines=True, step=46, label=None, label_c=GRAY):
    body.append(rect(x, y, w, h, "white", r=14, stroke=c, sw=2))
    if lines:
        n = int((h - 30) // step)
        body.append(wlines(x + 18, y + 18 + step, w - 36, n, c="#E6EAF0", step=step))
    if label:
        body.append(T(x + 18, y + 30, [label], 19, label_c, style="italic"))


def chip(body, x, y, txt, c, size=20, pad=18, fill=None, txtc="white", h=None):
    h = h or size * 1.9
    w = len(txt) * size * 0.6 + pad * 2
    body.append(rect(x, y, w, h, fill or c, r=h / 2, stroke=c, sw=2))
    body.append(T(x + w / 2, y + h / 2 + size * 0.36, [txt], size, txtc, weight="700", anchor="middle"))
    return w


# ───────── texto justificado (medido con la fuente real: Carlito = Calibri métrico) ─────────
from PIL import ImageFont
_FC = {}
_FONTS = {("400", "normal"): "Carlito-Regular.ttf", ("700", "normal"): "Carlito-Bold.ttf",
          ("400", "italic"): "Carlito-Italic.ttf", ("700", "italic"): "Carlito-BoldItalic.ttf"}


def _font(size, weight="400", style="normal"):
    k = (size, weight, style)
    if k not in _FC:
        _FC[k] = ImageFont.truetype("/usr/share/fonts/truetype/crosextra/" + _FONTS[(weight, style)], int(round(size * 4))) 
    return _FC[k]


def tw(txt, size, weight="400", style="normal"):
    return _font(size, weight, style).getlength(txt) / 4.0


def wrap_px(txt, size, width, weight="400", style="normal"):
    words = txt.split(" "); lines = []; cur = []
    for w_ in words:
        cand = " ".join(cur + [w_])
        if tw(cand, size, weight, style) > width and cur:
            lines.append(cur); cur = [w_]
        else:
            cur.append(w_)
    if cur: lines.append(cur)
    return lines


def TJ(x, y, txt, width, size, color=INK, weight="400", style="normal", lh=None, op=1, last_align="start"):
    """Párrafo justificado. Devuelve (svg, y_final)."""
    lh = lh or size * 1.42
    lines = wrap_px(txt, size, width, weight, style)
    out = []; yy = y
    for i, words in enumerate(lines):
        last = (i == len(lines) - 1)
        if last or len(words) == 1:
            out.append(T(x, yy + size, [" ".join(words)], size, color, weight=weight, style=style, op=op))
        else:
            ws = [tw(w_, size, weight, style) for w_ in words]
            gap = (width - sum(ws)) / (len(words) - 1)
            xs = []; cx = x
            for w_, ww in zip(words, ws):
                xs.append(cx); cx += ww + gap
            tsp = "".join(f'<tspan x="{px:.1f}">{esc(w_)}</tspan>' for px, w_ in zip(xs, words))
            out.append(f'<text y="{yy + size}" font-family="{UI}" font-size="{size}" font-weight="{weight}" '
                       f'fill="{color}" font-style="{style}" opacity="{op}">{tsp}</text>')
        yy += lh
    return "".join(out), yy


def parrafo_j(body, x, y, txt, width, size=30, color=INK, lh=None, weight="400", style="normal"):
    svg, yy = TJ(x, y, txt, width, size, color, weight, style, lh)
    body.append(svg); return yy
