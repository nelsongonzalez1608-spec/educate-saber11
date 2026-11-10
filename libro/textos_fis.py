#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lee TEXTOS_FIS.md y devuelve lo de Física que la guía de clase proyecta: las 24 preguntas de
entrenamiento (texto completo, enunciado, opciones, clave verificada, fuente y notas para el profe)
y, aparte, las figuras de esas preguntas redibujadas para la pantalla.

TEXTOS_FIS.md usa el mismo formato que TEXTOS_BIO.md, así que el lector es textos_soc.leer() con
area="FÍSICA" (textos_soc no se toca).

    from textos_fis import leer, FIGURAS, FIG_OPCIONES
    icfes = leer()             # {(misión, k): dict(titulo, texto, enunciado, opciones, clave, notas…)}
    FIGURAS[(3, 1)]            # la gráfica de resistencia contra temperatura (va en el panel del texto)
    FIG_OPCIONES[(3, 2)]       # los cuatro triángulos de cargas (van en la columna de las opciones)

Donde el .md dice «[[figura]]», la guía pone FIGURAS[(misión, k)]. Cuando las opciones son dibujos
(el modelo A, la figura A, la gráfica A…), los cuatro van juntos en FIG_OPCIONES[(misión, k)], encima
de las opciones, para no tener que desplazarse en el panel del texto. Las figuras repiten los datos y
la geometría de los módulos del cuaderno (fisN_icfes.py): tablas en HTML y esquemas en SVG en
línea, sin internet. Ninguna figura marca la opción correcta: los cuatro dibujos de opciones llevan
el mismo trazo, el mismo grosor y el mismo tamaño de letra.

verificar() cruza, pregunta por pregunta, la clave del .md con el docstring de fisN_icfes.py y con
tablero/icfes.csv, las cuatro opciones con las del módulo (cuando el módulo las trae en texto), que
las del ASED lo digan en su fuente, y que cada marca [[figura]] tenga su figura.
"""
import ast, csv, html, math, random, re, unicodedata

import textos_soc

FUENTE = "/home/claude/libro/TEXTOS_FIS.md"
MARCA = "[[figura]]"
E = lambda t: html.escape(str(t), quote=False)


def leer(fuente=FUENTE):
    icfes, _, _ = textos_soc.leer(area="FÍSICA", fuente=fuente)
    return icfes


# ─────────────────────────────── piezas de dibujo ───────────────────────────────
TINTA = "#1B1F27"; GRIS = "#5C6472"; CLARO = "#C9CFD8"; FONDO = "#F4F6F1"
FUENTE_SVG = "font-family:'Source Sans 3','Segoe UI',system-ui,sans-serif"


def _svg(w, h, cuerpo, alt, ancho=None):
    tope = f";max-width:{ancho}px;margin:0 auto" if ancho else ""
    return (f'<figure class="fig"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{E(alt)}" '
            f'style="{FUENTE_SVG}{tope}">{cuerpo}</svg></figure>')


def _t(x, y, txt, size=15, color=TINTA, anchor="start", bold=False, italic=False, rot=None):
    tr = f' transform="rotate({rot} {x:.1f} {y:.1f})"' if rot is not None else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" text-anchor="{anchor}"'
            f'{" font-weight=\"700\"" if bold else ""}{" font-style=\"italic\"" if italic else ""}{tr}>'
            f'{E(txt)}</text>')


def _l(x1, y1, x2, y2, c=TINTA, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" '
            f'stroke-width="{sw}"{d}/>')


def _r(x, y, w, h, fill="white", stroke=TINTA, sw=2, rx=0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def _c(cx, cy, r, fill="white", stroke=TINTA, sw=2):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def _flecha(x1, y1, x2, y2, c=TINTA, sw=2, head=10):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - head * math.cos(a - 0.42), y2 - head * math.sin(a - 0.42))
    p2 = (x2 - head * math.cos(a + 0.42), y2 - head * math.sin(a + 0.42))
    bx, by = x2 - head * 0.7 * math.cos(a), y2 - head * 0.7 * math.sin(a)
    return (_l(x1, y1, bx, by, c, sw) +
            f'<polygon points="{x2:.1f},{y2:.1f} {p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}" fill="{c}"/>')


def _poly(pts, c=TINTA, sw=2.4, dash=None, fill="none"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="{fill}" '
            f'stroke="{c}" stroke-width="{sw}" stroke-linejoin="round"{d}/>')


def _carga(cx, cy, signo, r=13):
    s = _c(cx, cy, r, "white", TINTA, 2)
    s += _l(cx - r * 0.55, cy, cx + r * 0.55, cy, TINTA, 2.4)
    if signo == "+":
        s += _l(cx, cy - r * 0.55, cx, cy + r * 0.55, TINTA, 2.4)
    return s


def _letra(x, y, L):
    return _c(x, y, 13, "white", TINTA, 1.8) + _t(x, y + 5, L, 15, TINTA, "middle", bold=True)


def _tabla(cab, filas, nota=None, ancho=None):
    th = "".join(f"<th>{E(c)}</th>" for c in cab)
    tr = "".join("<tr>" + "".join(f"<td>{E(c)}</td>" for c in f) + "</tr>" for f in filas)
    pie = f'<figcaption>{E(nota)}</figcaption>' if nota else ""
    st = f' style="max-width:{ancho}px"' if ancho else ""
    return (f'<figure class="fig"><table class="tabla"{st}><thead><tr>{th}</tr></thead>'
            f'<tbody>{tr}</tbody></table>{pie}</figure>')


# ───────────────────── Misión 1 · P2 · la gráfica de energía potencial ─────────────────────
def fig_ep():
    gx, gy, gw, gh = 130, 24, 500, 150
    c = _l(gx, gy + gh, gx + gw, gy + gh) + _l(gx, gy - 12, gx, gy + gh)
    c += _t(gx - 10, gy + 4, "Energía", 14, anchor="end", bold=True)
    c += _t(gx - 10, gy + 22, "potencial", 14, anchor="end", bold=True)
    c += _t(gx + gw, gy + gh + 44, "Tiempo", 14, anchor="end", bold=True)
    pts = []
    for i in range(121):
        t = i / 120
        if t < 0.2:
            e = 0.95 * (1 + math.cos(math.pi * t / 0.2)) / 2
        elif t < 0.65:
            e = 0.42 * math.exp(-((t - 0.45) / 0.05) ** 2)
        else:
            e = 0.38 * (1 - math.cos(math.pi * min(1, (t - 0.67) / 0.13))) / 2 if t > 0.67 else 0
        pts.append((gx + 6 + t * (gw - 20), gy + gh - e * gh))
    c += _poly(pts, TINTA, 2.8)
    for lab, t in (("t₁", 0.2), ("t₂", 0.45), ("t₃", 0.67), ("t₄", 0.82)):
        xx = gx + 6 + t * (gw - 20)
        c += _l(xx, gy + 20, xx, gy + gh + 6, GRIS, 1.4, "5,4")
        c += _t(xx, gy + gh + 24, lab, 15, anchor="middle", italic=True)
    return _svg(660, 230, c, "Gráfica de la energía potencial del vagón contra el tiempo, con los instantes t1 a t4",
                ancho=640)


def _carrito(cx, cy, lab):
    return _r(cx - 11, cy - 18, 22, 16, "white", TINTA, 2, rx=3) + _t(cx, cy - 26, lab, 14, anchor="middle",
                                                                      italic=True)


def _montana(x, y, k):
    """Los cuatro modelos de montaña rusa (fis1_icfes._modelo), en una caja de 280 × 150."""
    c = ""
    if k == 0:
        p = [(x + 20 + (i / 40) * 240, y + 40 + 80 * math.exp(-(((i / 40) - 0.45) / 0.18) ** 2)) for i in range(41)]
        c += _poly(p, TINTA, 2.6)
        for lab, t in (("t₁", 0.22), ("t₂", 0.45), ("t₃", 0.62), ("t₄", 0.85)):
            px, py = p[round(t * 40)]
            c += _carrito(px, py, lab)
    elif k == 1:
        p = [(x + 20, y + 20), (x + 40, y + 120), (x + 150, y + 120)]
        for i in range(1, 21):
            t = i / 20
            p.append((x + 150 + t * 110, y + 120 - 50 * (1 - math.cos(math.pi * t)) / 2))
        c += _poly(p, TINTA, 2.6)
        c += _carrito(x + 70, y + 120, "t₁") + _carrito(x + 115, y + 120, "t₂")
        c += _carrito(p[10][0], p[10][1], "t₃") + _carrito(p[19][0], p[19][1], "t₄")
    elif k == 2:
        p = []
        for i in range(41):
            t = i / 40
            p.append((x + 20 + t * 240, y + 130 - 95 * math.exp(-((t - 0.35) / 0.2) ** 2)
                      - (0 if t < 0.35 else -20 * (t - 0.35))))
        c += _poly(p, TINTA, 2.6)
        for lab, t in (("t₁", 0.12), ("t₂", 0.35), ("t₃", 0.6), ("t₄", 0.85)):
            px, py = p[round(t * 40)]
            c += _carrito(px, py, lab)
    else:
        p = [(x + 20, y + 10), (x + 40, y + 125), (x + 190, y + 125), (x + 215, y + 85), (x + 262, y + 85)]
        c += _poly(p, TINTA, 2.6)
        c += _c(x + 120, y + 92, 33, "none", TINTA, 2.6)
        c += _carrito(x + 68, y + 125, "t₁")
        c += _r(x + 109, y + 59, 22, 16, "white", TINTA, 2, rx=3) + _t(x + 120, y + 50, "t₂", 14, anchor="middle",
                                                                       italic=True)
        c += _carrito(x + 170, y + 125, "t₃") + _carrito(x + 245, y + 85, "t₄")
    return c


def fig_montanas():
    c = ""
    for k, L in enumerate("ABCD"):
        ox, oy = (k % 2) * 310, (k // 2) * 175
        c += _letra(ox + 16, oy + 18, L) + _montana(ox + 10, oy + 14, k)
    return _svg(610, 340, c, "Cuatro modelos de montaña rusa, A a D, con los instantes t1 a t4", ancho=600)


# ───────────────────── Misión 2 · P3 · moléculas de agua ─────────────────────
def _h2o(cx, cy, s=1.0, ang=0):
    a = math.radians(ang)
    c = ""
    for da in (-52, 52):
        t = a + math.radians(da) + math.pi / 2
        c += _c(cx + 7 * s * math.cos(t), cy + 7 * s * math.sin(t), 3.2 * s, "white", TINTA, 1.3)
    return c + _c(cx, cy, 4.4 * s, TINTA, TINTA, 0)


def _o(cx, cy):
    return _c(cx, cy, 4.4, TINTA, TINTA, 0)


def _h(cx, cy):
    return _c(cx, cy, 3.4, "white", TINTA, 1.3)


def _vaso(x, y, w=64, h=84):
    return (f'<path d="M {x} {y} L {x} {y + h - 6} Q {x} {y + h} {x + 6} {y + h} L {x + w - 6} {y + h} '
            f'Q {x + w} {y + h} {x + w} {y + h - 6} L {x + w} {y}" fill="white" stroke="{TINTA}" stroke-width="2"/>'
            f'<ellipse cx="{x + w / 2}" cy="{y}" rx="{w / 2}" ry="6" fill="white" stroke="{TINTA}" stroke-width="2"/>')


def _liquido(x, y, w=64, h=84):
    return "".join(_h2o(x + 10 + i * 15, y + h - 12 - j * 13, 0.85, (i * 47 + j * 90) % 360)
                   for i in range(4) for j in range(2))


def fig_vaso():
    c = _vaso(28, 14) + _liquido(28, 14)
    return _svg(120, 110, c, "Recipiente cerrado con moléculas de agua líquida en el fondo", ancho=170)


def _modelo_gas(mx, my, k):
    c = _t(mx + 42, my + 4, "Líquido", 13, anchor="middle") + _t(mx + 122, my + 4, "Gas", 13, anchor="middle")
    c += _vaso(mx + 10, my + 18) + _liquido(mx + 10, my + 18)
    gx, gy = mx + 90, my + 18
    c += _vaso(gx, gy)
    if k == 0:
        c += "".join(_o(gx + 9 + (i % 4) * 15, gy + 14 + (i // 4) * 14) for i in range(8))
        c += "".join(_h(gx + 8 + (i % 5) * 12, gy + 62 + (i // 5) * 10) for i in range(10))
    elif k == 1:
        for i, (px, py) in enumerate(((12, 16), (40, 12), (26, 34), (52, 38), (12, 56), (38, 60), (54, 70), (22, 76))):
            c += _h2o(gx + px, gy + py, 0.85, i * 70)
    elif k == 2:
        c += "".join(_h2o(gx + 10 + i * 15, gy + 14 + j * 13, 0.85, (i * 47 + j * 90) % 360)
                     for i in range(4) for j in range(2))
    else:
        for px, py in ((10, 14), (30, 22), (50, 12), (18, 40), (44, 44), (28, 62), (52, 70), (12, 74)):
            c += _o(gx + px, gy + py)
        for px, py in ((22, 12), (42, 28), (56, 30), (10, 28), (32, 46), (54, 56), (14, 58), (40, 64), (24, 80),
                       (46, 80), (34, 34), (8, 64), (58, 44), (20, 50), (36, 76), (48, 18)):
            c += _h(gx + px, gy + py)
    return c


def fig_modelos_gas():
    c = ""
    for k, L in enumerate("ABCD"):
        ox, oy = (k % 2) * 215, (k // 2) * 140
        c += _letra(ox + 16, oy + 22, L) + _modelo_gas(ox + 34, oy + 16, k)
    leyenda = (_o(20, 300) + _t(32, 305, "oxígeno", 13, GRIS) + _h(110, 300) + _t(120, 305, "hidrógeno", 13, GRIS))
    return _svg(430, 316, c + leyenda, "Cuatro modelos, A a D, del agua líquida y en gas en un recipiente", ancho=520)


# ───────────────────── Misión 2 · P4 · altura y partículas de aire ─────────────────────
def fig_altura():
    rnd = random.Random(27)
    bx, by, bw, bh = 110, 22, 160, 200
    c = _r(bx, by, bw, bh, "white", TINTA, 2)
    for _ in range(260):
        f = rnd.random() ** 3.4
        c += f'<circle cx="{bx + rnd.uniform(6, bw - 6):.1f}" cy="{by + bh - 4 - f * (bh - 10):.1f}" r="1.8" fill="{GRIS}"/>'
    for km in range(0, 31, 5):
        ty = by + bh - km / 30 * bh
        c += _l(bx - 8, ty, bx, ty, TINTA, 1.6) + _t(bx - 12, ty + 5, str(km), 13, anchor="end")
    c += _t(bx - 50, by + bh / 2, "Altura (km)", 14, anchor="middle", bold=True, rot=-90)
    return _svg(300, 240, c, "Columna de aire: muchas partículas cerca del suelo y muy pocas a 25 y 30 km", ancho=300)


# ───────────────────── Misión 3 · P1 · resistencia contra temperatura ─────────────────────
SERIES = (("R₁", ((0, 3), (20, 3.5), (40, 4), (60, 4.5), (80, 5)), "tri", "#7A7F8A", None),
          ("R₂", ((0, 2), (20, 2.2), (40, 2.8), (60, 3.8), (80, 5)), "rombo", TINTA, None),
          ("R₃", ((0, 5), (20, 4), (40, 2.8), (60, 2.2), (80, 2)), "equis", "#4A4F5A", "7,5"),
          ("R₄", ((0, 4), (20, 4), (40, 4), (60, 4), (80, 4)), "cuadro", "#9AA0AA", None))


def _marca(px, py, tipo, col):
    if tipo == "tri":
        return f'<polygon points="{px:.1f},{py - 8:.1f} {px + 8:.1f},{py + 6:.1f} {px - 8:.1f},{py + 6:.1f}" fill="{col}"/>'
    if tipo == "rombo":
        return f'<polygon points="{px:.1f},{py - 8:.1f} {px + 8:.1f},{py:.1f} {px:.1f},{py + 8:.1f} {px - 8:.1f},{py:.1f}" fill="{col}"/>'
    if tipo == "equis":
        return _l(px - 7, py - 7, px + 7, py + 7, col, 3) + _l(px - 7, py + 7, px + 7, py - 7, col, 3)
    return _r(px - 7, py - 7, 14, 14, col, col, 0)


def fig_resistencias():
    gx, gy, gw, gh = 80, 20, 540, 170
    c = ""
    for v in range(7):
        py = gy + gh - v / 6 * gh
        c += _l(gx, py, gx + gw, py, "#E1E5EB", 1.2, "4,6") + _t(gx - 12, py + 5, str(v), 14, anchor="end")
    for t in range(0, 101, 10):
        c += _t(gx + t / 100 * gw, gy + gh + 22, str(t), 14, anchor="middle")
    c += _l(gx, gy + gh, gx + gw + 10, gy + gh, TINTA, 2.2) + _l(gx, gy - 10, gx, gy + gh, TINTA, 2.2)
    for nom, pts, tipo, col, dash in SERIES:
        P = [(gx + t / 100 * gw, gy + gh - v / 6 * gh) for t, v in pts]
        c += _poly(P, col, 3, dash)
        c += "".join(_marca(px, py, tipo, col) for px, py in P)
    c += _t(gx + gw / 2, gy + gh + 48, "Temperatura (°C)", 15, anchor="middle", bold=True)
    c += _t(gx - 44, gy + gh / 2, "Resistencia (Ω)", 15, anchor="middle", bold=True, rot=-90)
    lx, ly = gx + gw + 40, gy
    c += _r(lx, ly - 10, 120, 160, "white", TINTA, 1.6)
    for k, (nom, pts, tipo, col, dash) in enumerate(SERIES):
        yy = ly + 20 + k * 36
        c += _l(lx + 14, yy, lx + 60, yy, col, 3, dash) + _marca(lx + 37, yy, tipo, col)
        c += _t(lx + 74, yy + 7, nom, 18)
    return _svg(790, 260, c, "Resistencia contra temperatura de R1 a R4, de 0 a 80 grados", ancho=760)


# ───────────────────── Misión 3 · P2 · tres cargas en triángulo ─────────────────────
def _triangulo(cx, top, s, flechas=None, nombres=True):
    p1, p2, p3 = (cx, top), (cx - 0.58 * s, top + s), (cx + 0.58 * s, top + s)
    c = ""
    if flechas is None:
        c += (f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {p3[0]:.1f},{p3[1]:.1f}" '
              f'fill="none" stroke="{TINTA}" stroke-width="2.4"/>')
    else:
        c += _l(p1[0], p1[1], p2[0], p2[1], GRIS, 1.6, "6,5") + _l(p1[0], p1[1], p3[0], p3[1], GRIS, 1.6, "6,5")
    for (px, py), sg, n, dx in ((p1, "+", "1", 0), (p2, "+", "2", -30), (p3, "-", "3", 30)):
        c += _carga(px, py, sg)
        if nombres:
            c += _t(px + dx, py - 20 if n == "1" else py + 6, n, 16, anchor="middle", bold=True)
    if flechas:
        L = 0.46 * s
        for q, hacia, lab in flechas:
            ux, uy = q[0] - p1[0], q[1] - p1[1]
            d = math.hypot(ux, uy)
            ux, uy = ux / d, uy / d
            sg = 1 if hacia else -1
            ex, ey = p1[0] + sg * ux * L, p1[1] + sg * uy * L
            c += _flecha(p1[0] + sg * ux * 15, p1[1] + sg * uy * 15, ex, ey, TINTA, 2.6, 10)
            der = ex > p1[0]
            tx = ex + (10 if der else -10)
            ty = ey + (16 if ey > p1[1] else -18)
            for j, ln in enumerate(lab):
                c += _t(tx, ty + j * 15, ln, 12, anchor="start" if der else "end", bold=True)
    return c


def fig_triangulo():
    return _svg(260, 160, _triangulo(130, 32, 105), "Tres cargas en triángulo: 1 positiva arriba, 2 positiva "
                "abajo a la izquierda y 3 negativa abajo a la derecha", ancho=260)


def fig_triangulos():
    s = 100
    f2, f3 = ["Fuerza de", "2 sobre 1"], ["Fuerza de", "3 sobre 1"]
    conf = {"A": ((False, f2), (True, f3)), "B": ((True, f2), (False, f3)),
            "C": ((False, f2), (False, f3)), "D": ((True, f2), (True, f3))}
    c = ""
    for k, L in enumerate("ABCD"):
        ox, oy = (k % 2) * 300, (k // 2) * 200
        cx, top = ox + 150, oy + 66
        p2, p3 = (cx - 0.58 * s, top + s), (cx + 0.58 * s, top + s)
        (h2, l2), (h3, l3) = conf[L]
        c += _letra(ox + 18, oy + 20, L) + _triangulo(cx, top, s, flechas=((p2, h2, l2), (p3, h3, l3)), nombres=False)
    return _svg(600, 400, c, "Cuatro figuras, A a D, con las fuerzas de las cargas 2 y 3 sobre la carga 1", ancho=600)


# ───────────────────── Misión 3 · P3 · el campo de dos esferas y la carga −q ─────────────────────
def _lineas_dipolo(d=55, n=12, paso=3.0, caja=(-150, -130, 150, 130)):
    """Líneas de campo de +1 en (−d, 0) y −1 en (d, 0), como en fis3_icfes._lineas_dipolo."""
    lineas = []
    for k in range(n):
        ang = math.pi * 2 * (k + 0.5) / n
        x, y = -d + 9 * math.cos(ang), 9 * math.sin(ang)
        pts = [(x, y)]
        for _ in range(900):
            r1 = math.hypot(x + d, y) or 1e-6
            r2 = math.hypot(x - d, y) or 1e-6
            ex = (x + d) / r1 ** 3 - (x - d) / r2 ** 3
            ey = y / r1 ** 3 - y / r2 ** 3
            m = math.hypot(ex, ey)
            x, y = x + paso * ex / m, y + paso * ey / m
            if not (caja[0] <= x <= caja[2] and caja[1] <= y <= caja[3]) or r2 < 9:
                break
            pts.append((x, y))
        lineas.append(pts)
    return lineas


LINEAS = _lineas_dipolo()
_LQ = LINEAS[9]
QX, QY = _LQ[16]
_tx, _ty = _LQ[18][0] - _LQ[14][0], _LQ[18][1] - _LQ[14][1]
_tm = math.hypot(_tx, _ty)
TX, TY = _tx / _tm, _ty / _tm            # sentido del campo donde está −q


def _dipolo(cx, cy, s, flecha_q=None):
    c = ""
    for pts in LINEAS:
        P = [(cx + s * a, cy + s * b) for a, b in pts]
        c += _poly(P, GRIS, 1.5)
        if len(P) > 30:
            i = len(P) // 2
            (ax, ay), (bx, by) = P[i - 3], P[i + 3]
            c += _flecha(ax, ay, bx, by, GRIS, 1.5, 7)
    c += _carga(cx - 55 * s, cy, "+", 12) + _carga(cx + 55 * s, cy, "-", 12)
    qx, qy = cx + s * QX, cy + s * QY
    c += _c(qx, qy, 6.5, TINTA, TINTA, 0)
    if flecha_q and flecha_q[0] < -0.3:
        c += _r(qx + 10, qy - 28, 28, 19, "white", "white", 0, rx=4) + _t(qx + 12, qy - 13, "−q", 14, bold=True)
    else:
        c += _r(qx - 40, qy - 28, 28, 19, "white", "white", 0, rx=4) + _t(qx - 13, qy - 13, "−q", 14, bold=True,
                                                                          anchor="end")
    if flecha_q:
        ux, uy = flecha_q
        c += _flecha(qx, qy, qx + 38 * ux, qy + 38 * uy, TINTA, 3.2, 11)
    return c


def fig_dipolo():
    c = _dipolo(160, 112, 0.8) + _t(160, 222, "E", 16, anchor="middle", bold=True, italic=True)
    return _svg(320, 230, c, "Líneas de campo entre una esfera positiva y una negativa, con la carga −q sobre "
                "una de las líneas", ancho=380)


def fig_dipolos():
    dirs = {"A": (-TX, -TY), "B": (TX, TY), "C": (-TY, TX), "D": (TY, -TX)}
    c = ""
    for k, L in enumerate("ABCD"):
        ox, oy = (k % 2) * 270, (k // 2) * 215
        c += _letra(ox + 16, oy + 18, L) + _dipolo(ox + 140, oy + 112, 0.76, flecha_q=dirs[L])
    return _svg(540, 430, c, "Cuatro figuras, A a D, con la dirección en que se movería la carga −q", ancho=560)


# ───────────────────── Misión 3 · P4 · dos esferas metálicas ─────────────────────
def _esfera(cx, cy, n, signos):
    c = _c(cx, cy, 34, "#C9CED6", TINTA, 2) + _t(cx, cy + 7, n, 18, anchor="middle", bold=True)
    for k in range(signos):
        a = 2 * math.pi * k / max(signos, 1) - math.pi / 2
        c += _t(cx + 52 * math.cos(a), cy + 52 * math.sin(a) + 6, "+", 18, anchor="middle", bold=True)
    return c


def fig_esferas():
    c = ""
    for k, (tit, s1, s2, q1, q2) in enumerate((("Antes del contacto", 8, 0, "+ Q", ""),
                                               ("Después del contacto", 4, 4, "+ Q/2", "+ Q/2"))):
        bx = 20 + k * 330
        c += _t(bx + 125, 20, tit, 16, anchor="middle", bold=True)
        c += _esfera(bx + 55, 112, "1", s1) + _esfera(bx + 195, 112, "2", s2)
        c += _t(bx + 55, 192, q1, 16, anchor="middle", italic=True)
        if q2:
            c += _t(bx + 195, 192, q2, 16, anchor="middle", italic=True)
        else:
            c += _t(bx + 195, 192, "neutra", 14, GRIS, "middle", italic=True)
    return _svg(660, 205, c, "Dos esferas metálicas antes y después del contacto: + Q y neutra; luego + Q/2 y + Q/2",
                ancho=640)


# ───────────────────── Misión 4 · P2 · el farol y la piscina ─────────────────────
def _farol(x, y):
    c = _l(x, y, x, y + 58, TINTA, 4) + _c(x, y - 8, 9, "#FFF4E0", TINTA, 2)
    for a in range(0, 360, 45):
        r = math.radians(a)
        c += _l(x + 13 * math.cos(r), y - 8 + 13 * math.sin(r), x + 20 * math.cos(r), y - 8 + 20 * math.sin(r), TINTA, 1.6)
    return c


def _piscina(x, y, w, h, llena, titulo):
    c = _t(x, y + 14, titulo, 15, bold=True)
    bx = x + 70
    c += _r(x, y + 80, 70, h - 80, "#6E7480", "#6E7480", 0) + _farol(x + 35, y + 40) + _t(x + 2, y + 74, "Farol", 13)
    if llena:
        c += _r(bx, y + 82, w - 70, h - 82, "#D7E4EF", "#D7E4EF", 0)
        c += _t(bx + 14, y + 112, "Agua", 14, bold=True) + _t(x + w - 6, y + 70, "Aire", 14, anchor="end", bold=True)
    else:
        c += _t(bx + 30, y + 150, "Aire", 14, bold=True)
    c += _l(bx, y + 80, bx, y + h, TINTA, 3) + _l(bx, y + h, x + w, y + h, TINTA, 3) + _l(x + w, y + 80, x + w, y + h, TINTA, 3)
    ox, oy = x + w - 46, y + h - 40
    c += _c(ox, oy, 11, "white", TINTA, 2.2) + _t(ox, oy + 30, "Nadador", 13, anchor="middle")
    fx, fy = x + 35, y + 32
    if not llena:
        c += _flecha(fx + 10, fy + 6, ox - 10, oy - 6, TINTA, 2, 9)
        c += _t((fx + ox) / 2 + 16, (fy + oy) / 2 - 14, "Rayo de luz", 13)
    else:
        sx, sy = ox - 70, y + 82
        c += _flecha(fx + 10, fy + 6, sx, sy, TINTA, 2, 9) + _flecha(sx, sy, ox - 8, oy - 9, TINTA, 2, 9)
        c += _t((fx + sx) / 2 + 30, (fy + sy) / 2 - 12, "Rayo de luz", 13)
    return c


def fig_piscinas():
    c = _piscina(10, 6, 300, 200, False, "Figura 1. Piscina vacía") + \
        _piscina(350, 6, 300, 200, True, "Figura 2. Piscina llena de agua")
    return _svg(660, 220, c, "Figura 1: piscina vacía, el rayo del farol llega recto al nadador. Figura 2: piscina "
                "llena, el rayo se dobla al entrar al agua", ancho=660)


# ───────────────────── Misión 4 · P3 · dos parlantes ─────────────────────
PUNTOS_70 = ((0.24, 0.3, 0), (0.34, 0.24, 1), (0.44, 0.2, 0), (0.54, 0.24, 1), (0.64, 0.3, 0),
             (0.18, 0.55, 1), (0.29, 0.5, 0), (0.39, 0.46, 1), (0.49, 0.45, 0), (0.59, 0.46, 1), (0.69, 0.52, 0),
             (0.22, 0.8, 0), (0.33, 0.75, 1), (0.44, 0.72, 0), (0.55, 0.74, 1), (0.66, 0.8, 0))


def _parlante(x, y):
    return (_r(x, y, 44, 64, "white", TINTA, 2, rx=4) + _c(x + 22, y + 18, 9, "none", TINTA, 2) +
            _c(x + 22, y + 44, 14, "none", TINTA, 2))


def fig_parlantes():
    fw, fh, fx, y = 620, 196, 10, 6
    c = _r(fx, y, fw, fh, "white", TINTA, 2) + _r(fx + 2, y + 2, fw - 4, 60, "#EEF0F4", "#EEF0F4", 0)
    c += _t(fx + fw / 2, y + 38, "emisora del colegio", 14, anchor="middle")
    c += _parlante(fx + 24, y + 28) + _parlante(fx + fw - 68, y + 28)
    for px, py, negro in PUNTOS_70:
        cx, cy = fx + fw * px + 40, y + 70 + (fh - 70) * py
        c += (f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="11" ry="6" fill="{TINTA if negro else "white"}" '
              f'stroke="{TINTA}" stroke-width="1.8"/>')
    c += _c(fx + fw - 50, y + 148, 20, "white", TINTA, 2) + _t(fx + fw - 50, y + 156, "?", 22, anchor="middle", bold=True)
    c += _t(fx + fw - 50, y + 186, "estudiante", 12, anchor="middle")
    return _svg(640, 210, c, "Dos parlantes frente a la emisora y puntos negros y blancos marcados por el estudiante",
                ancho=640)


# ───────────────────── Misión 4 · P4 · tabla y gráficas del sonido ─────────────────────
FILAS_48 = (("0", "331,7"), ("1", "332,3"), ("2", "332,9"), ("3", "333,5"))


def fig_tabla_sonido():
    return _tabla(["Temperatura (°C)", "Velocidad del sonido (m/s)"], FILAS_48, ancho=460)


def fig_graficas_sonido():
    vel, tem = ("331,7", "332,3", "332,9", "333,5"), ("0", "1", "2", "3")
    graf = {"A": ("Temperatura (°C)", vel, "Velocidad del sonido (m/s)", tem),
            "B": ("Velocidad del sonido (m/s)", vel, "Temperatura (°C)", tem),
            "C": ("Temperatura (°C)", tem, "Velocidad del sonido (m/s)", vel[::-1]),
            "D": ("Velocidad del sonido (m/s)", tem, "Temperatura (°C)", vel[::-1])}
    c = ""
    for k, L in enumerate("ABCD"):
        ox, oy = (k % 2) * 290, (k // 2) * 215
        ylab, yt, xlab, xt = graf[L]
        c += _letra(ox + 16, oy + 18, L)
        gx, gy, gw, gh = ox + 110, oy + 30, 160, 120
        for i in range(4):
            py, px = gy + gh - i / 3 * gh, gx + i / 3 * gw
            c += _l(gx, py, gx + gw, py, "#E1E5EB", 1.2) + _l(px, gy, px, gy + gh, "#E1E5EB", 1.2)
            c += _t(gx - 6, py + 5, yt[i], 13, anchor="end") + _t(px, gy + gh + 18, xt[i], 13, anchor="middle")
        c += _l(gx, gy + gh, gx + gw + 8, gy + gh, TINTA, 2) + _l(gx, gy - 8, gx, gy + gh, TINTA, 2)
        c += _l(gx, gy + gh, gx + gw, gy, TINTA, 1.8)
        c += "".join(_c(gx + i / 3 * gw, gy + gh - i / 3 * gh, 4.5, TINTA, TINTA, 0) for i in range(4))
        c += _t(gx + gw / 2, gy + gh + 40, xlab, 13, anchor="middle", bold=True)
        partes = ylab.replace(" del sonido", " del|sonido").split("|")
        for j, p in enumerate(partes):
            c += _t(ox + 36 + j * 16 - (len(partes) - 1) * 8, gy + gh / 2, p, 13, anchor="middle", bold=True, rot=-90)
    return _svg(580, 425, c, "Cuatro gráficas, A a D, de velocidad del sonido y temperatura", ancho=580)


# ───────────────────── Misión 5 · P1 · rampa y tabla de momentos ─────────────────────
def fig_rampa():
    rx, ry = 70, 14
    c = _l(rx, ry + 10, rx, ry + 130, TINTA, 3)
    c += (f'<path d="M {rx} {ry + 20} Q {rx + 60} {ry + 120} {rx + 260} {ry + 128} L {rx + 420} {ry + 128}" '
          f'fill="none" stroke="{TINTA}" stroke-width="3"/>')
    c += _l(rx - 30, ry + 132, rx + 440, ry + 132, TINTA, 2)
    c += _c(rx + 14, ry + 6, 14, "white", TINTA, 2.2) + _c(rx + 404, ry + 116, 12, "white", TINTA, 2.2)
    c += _t(rx + 36, ry + 10, "Pelota 1 · masa = 5 kg", 15) + _t(rx + 330, ry + 96, "Pelota 2", 15)
    c += _t(rx - 12, ry + 80, "1,5 m", 15, anchor="end")
    svg = _svg(540, 160, c, "Rampa de 1,5 m: la pelota 1, de 5 kg, baja y choca con la pelota 2 en reposo", ancho=540)
    tabla = _tabla(["Lanzamiento", "Pelota 1 · antes", "Pelota 1 · después", "Masa pelota 2 (kg)",
                    "Pelota 2 · antes", "Pelota 2 · después"],
                   (("I", "27,10", "18,05", "1", "0", "9,00"), ("II", "27,10", "6,50", "3", "0", "20,60"),
                    ("III", "27,10", "0,00", "5", "0", "27,10"), ("IV", "27,10", "−4,50", "7", "0", "31,60")),
                   nota="Momentos en kg·m/s.")
    return svg + tabla


# ───────────────────── Misión 5 · P2 · la piñata ─────────────────────
def fig_pinata():
    px, py = 140, 20
    c = _l(px - 80, py, px + 80, py, TINTA, 3) + _l(px, py, px, py + 30, TINTA, 2)
    c += _c(px, py + 50, 22, "white", TINTA, 2.4)
    c += _l(px - 22, py + 50, px - 22, py + 150, TINTA, 2) + _l(px + 22, py + 50, px + 22, py + 110, TINTA, 2)
    c += (f'<polygon points="{px + 22},{py + 110} {px + 52},{py + 140} {px + 22},{py + 170} {px - 8},{py + 140}" '
          f'fill="#F1DDB8" stroke="{TINTA}" stroke-width="2"/>')
    c += _t(px + 60, py + 146, "piñata", 14) + _t(px + 30, py + 54, "polea", 14)
    c += _c(px - 22, py + 162, 9, "white", TINTA, 2) + _l(px - 22, py + 171, px - 22, py + 205, TINTA, 2.4)
    c += _t(px - 40, py + 196, "niño", 14, anchor="end")
    return _svg(280, 235, c, "Una cuerda pasa por una polea: de un lado cuelga la piñata y del otro la sostiene el niño",
                ancho=280)


# ───────────────────── Misión 5 · P4 · la pelota en el tubo ─────────────────────
def fig_tubo():
    tx, ty = 30, 8
    c = _r(tx, ty, 70, 200, "white", TINTA, 2.2, rx=8) + _c(tx + 35, ty + 80, 30, "#D8DCE2", TINTA, 2)
    c += _flecha(tx + 18, ty + 190, tx + 18, ty + 130, TINTA, 2.2, 9) + _flecha(tx + 52, ty + 190, tx + 52, ty + 130, TINTA, 2.2, 9)
    c += _t(tx + 100, ty + 40, "La pelota se mueve aceleradamente hacia arriba", 15, bold=True)
    c += _flecha(tx + 110, ty + 150, tx + 110, ty + 100, TINTA, 2.2, 9)
    c += _t(tx + 126, ty + 124, "dirección de movimiento", 15, bold=True)
    c += _t(tx + 126, ty + 143, "del aire soplado", 15, bold=True)
    return _svg(480, 220, c, "Tubo vertical con una pelota que sube acelerada; el aire soplado va hacia arriba", ancho=480)


# ───────────────────── Misión 6 · P1 · cinco resistencias ─────────────────────
def _resistencia(cx, cy, horizontal, lab):
    if horizontal:
        return _r(cx - 40, cy - 12, 80, 24, "white", TINTA, 2) + _t(cx, cy - 20, lab, 15, anchor="middle", bold=True)
    return _r(cx - 12, cy - 40, 24, 80, "white", TINTA, 2) + _t(cx - 22, cy + 6, lab, 15, anchor="end", bold=True)


def fig_circuito5():
    L, R, Mx, top, bot = 90, 570, 330, 34, 204
    c = _l(L, top, R, top) + _l(L, bot, R, bot) + _l(Mx, top, Mx, bot) + _l(R, top, R, bot)
    c += _l(L, top, L, top + 60) + _l(L, top + 110, L, bot)
    c += _l(L - 22, top + 60, L + 22, top + 60, TINTA, 3) + _l(L - 12, top + 76, L + 12, top + 76, TINTA, 3)
    c += _l(L, top + 76, L, top + 110)
    c += _t(L - 30, top + 72, "12 V", 15, anchor="end", bold=True) + _t(L + 18, top + 54, "+", 15, bold=True)
    for cx, cy, hz, lab in (((L + Mx) / 2, top, True, "R1"), ((Mx + R) / 2, top, True, "R3"),
                            (Mx, (top + bot) / 2, False, "R2"), (R, (top + bot) / 2, False, "R4"),
                            ((Mx + R) / 2, bot, True, "R5")):
        c += _resistencia(cx, cy, hz, lab)
    for x1, y1, x2, y2, lab, lx, ly in (((L + Mx) / 2 - 40, top + 26, (L + Mx) / 2 + 30, top + 26, "I1", (L + Mx) / 2 - 10, top + 52),
                                        ((Mx + R) / 2 - 40, top + 26, (Mx + R) / 2 + 30, top + 26, "I2", (Mx + R) / 2 - 10, top + 52),
                                        (Mx + 30, (top + bot) / 2 - 30, Mx + 30, (top + bot) / 2 + 30, "I3", Mx + 44, (top + bot) / 2 + 6),
                                        (L + 120, bot - 24, L + 50, bot - 24, "I4", L + 76, bot - 34)):
        c += _flecha(x1, y1, x2, y2, TINTA, 2, 8) + _t(lx, ly, lab, 15, bold=True)
    return _svg(620, 226, c, "Circuito: fuente de 12 V, R1 en serie, luego R2 en paralelo con la rama R3, R4 y R5; "
                "corrientes I1 a I4", ancho=620)


# ───────────────────── Misión 6 · P2 · tabla de dispositivos y circuito con P ─────────────────────
def fig_condensador():
    tabla = _tabla(["Nombre", "Función"],
                   (("Resistencia", "Generar una resistencia al paso de corriente"),
                    ("Condensador", "Almacenar energía eléctrica"), ("Cable", "Conducir corriente eléctrica"),
                    ("Interruptor", "Desviar o interrumpir el curso de la corriente")), ancho=560)
    L, R, top, bot = 70, 550, 40, 160
    c = _l(L, top, L + 120, top) + _c(L + 140, top, 18, "#FFF4C8", TINTA, 2)
    c += _t(L + 140, top - 26, "bombillo", 14, anchor="middle")
    c += _l(L + 158, top, L + 240, top) + _r(L + 240, top - 16, 120, 32, "white", TINTA, 2)
    c += _t(L + 300, top + 6, "P", 17, anchor="middle", bold=True)
    c += _l(L + 360, top, R, top) + _l(R, top, R, bot) + _l(R, bot, L + 120, bot)
    c += _c(L + 120, bot, 6, "white", TINTA, 2) + _l(L + 120, bot, L + 72, bot + 22, TINTA, 2.6)
    c += _c(L + 64, bot - 28, 6, "white", TINTA, 2) + _c(L + 64, bot + 26, 6, "white", TINTA, 2)
    c += _t(L + 84, bot - 36, "2", 15, bold=True) + _t(L + 82, bot + 44, "1", 15, bold=True)
    c += _t(L + 132, bot + 24, "interruptor", 14)
    c += _l(L, top, L, bot - 28) + _l(L, bot - 28, L + 58, bot - 28) + _l(L, bot - 28, L, bot + 60)
    c += _l(L - 18, bot + 60, L + 18, bot + 60, TINTA, 3) + _l(L - 10, bot + 72, L + 10, bot + 72, TINTA, 3)
    c += _l(L, bot + 72, L, bot + 90) + _l(L, bot + 90, L + 64, bot + 90) + _l(L + 64, bot + 90, L + 64, bot + 32)
    c += _t(L - 26, bot + 72, "fuente", 14, anchor="end")
    return tabla + _svg(600, 268, c, "Circuito con fuente, interruptor de dos posiciones, bombillo y el punto P",
                        ancho=560)


# ───────────────────── Misión 6 · P3 · pelotas que rebotan ─────────────────────
def fig_rebote():
    c = ""
    for k, (lab, alto, piso, r_) in enumerate((("tenis", 1.0, "césped", 10), ("baloncesto", 1.5, "asfalto", 22))):
        bx, base = 20 + k * 230, 236
        c += _r(bx, base, 180, 16, "#C9D7B8" if k == 0 else "#B8BCC4", TINTA, 1.4)
        c += _t(bx + 90, base + 38, piso, 14, anchor="middle")
        tope = base - alto / 1.6 * 180
        c += _l(bx + 120, base, bx + 120, tope, TINTA, 1.8) + _l(bx + 112, tope, bx + 128, tope, TINTA, 1.8)
        c += _t(bx + 132, (base + tope) / 2, f"{alto:.1f} m".replace(".", ","), 14)
        c += _c(bx + 60, tope - r_ - 4, r_, "white", TINTA, 2) + _t(bx + 60, tope - 2 * r_ - 14, lab, 14, anchor="middle")
    c += _t(20, 18, "Las dos se lanzan desde 2,0 m; la figura muestra la altura del rebote.", 13, GRIS, italic=True)
    return _svg(450, 290, c, "La pelota de tenis rebota 1,0 m sobre césped y la de baloncesto 1,5 m sobre asfalto",
                ancho=450)


# ───────────────────── Misión 6 · P4 · curva de calentamiento ─────────────────────
def fig_curva():
    gx, gy, gw, gh = 80, 14, 420, 220
    c = _l(gx, gy, gx, gy + gh) + _l(gx, gy + gh, gx + gw, gy + gh)
    Y = lambda t: gy + gh - (t + 40) / 180 * gh
    for t in range(-40, 141, 20):
        c += _l(gx - 5, Y(t), gx + 5, Y(t), TINTA, 1.6) + _t(gx - 10, Y(t) + 5, str(t).replace("-", "−"), 13, GRIS, "end")
    for t in (0, 100):
        c += _l(gx, Y(t), gx + gw, Y(t), GRIS, 1.4, "5,5")
    pts = ((0, -40), (50, 0), (95, 0), (230, 100), (330, 100), (370, 140))
    c += _poly([(gx + px, Y(t)) for px, t in pts], TINTA, 3)
    c += _t(gx + 60, Y(-30), "Sólido", 14, bold=True) + _t(gx + 170, Y(40), "Líquido", 14, bold=True)
    c += _t(gx + 330, Y(125), "Gas", 14, bold=True)
    c += _t(28, gy + gh / 2, "Temperatura (°C)", 14, GRIS, "middle", italic=True, rot=-90)
    c += _t(gx + gw / 2, gy + gh + 28, "Tiempo", 14, GRIS, "middle")
    svg = _svg(520, 270, c, "Curva de calentamiento con dos tramos planos, a 0 y a 100 grados", ancho=520)
    tabla = _tabla(["Sustancia", "Fusión (°C)", "Ebullición (°C)"],
                   (("Benceno", "6", "80"), ("Agua", "0", "100"), ("Acetonitrilo", "−45", "82"),
                    ("2-butanol", "−115", "100")), ancho=460)
    return svg + tabla


FIGURAS = {(1, 2): fig_ep(), (2, 3): fig_vaso(), (2, 4): fig_altura(),
           (3, 1): fig_resistencias(), (3, 2): fig_triangulo(), (3, 3): fig_dipolo(), (3, 4): fig_esferas(),
           (4, 2): fig_piscinas(), (4, 3): fig_parlantes(), (4, 4): fig_tabla_sonido(),
           (5, 1): fig_rampa(), (5, 2): fig_pinata(), (5, 4): fig_tubo(),
           (6, 1): fig_circuito5(), (6, 2): fig_condensador(), (6, 3): fig_rebote(), (6, 4): fig_curva()}

# Preguntas cuyas opciones son dibujos: los cuatro van en la columna de las opciones (no en el panel
# del texto, donde habría que desplazarse) y las opciones quedan en una sola fila.
FIG_OPCIONES = {(1, 2): fig_montanas(), (2, 3): fig_modelos_gas(), (3, 2): fig_triangulos(),
                (3, 3): fig_dipolos(), (4, 4): fig_graficas_sonido()}

# Estilo de las figuras dentro de la guía (se agrega a la plantilla).
CSS = """.fig{margin:12px 0}.fig svg{display:block;width:100%;max-width:760px;height:auto}
.tabla{border-collapse:collapse;width:100%;table-layout:fixed;font-size:.86em;line-height:1.35;margin:0 auto}
.tabla th,.tabla td{border:1px solid var(--line);padding:5px 8px;vertical-align:top;overflow-wrap:anywhere}
.tabla th{background:#F2F4EE;text-align:left}.fig figcaption{font-size:.85em;font-style:italic;color:var(--muted)}
.ops.cuatro{grid-template-columns:repeat(4,1fr)}.opsfig{background:var(--paper);border:1px solid var(--line);
border-radius:14px;padding:8px 10px;margin-top:10px}.opsfig .fig{margin:0}
"""


# ─────────────────────────────── verificación ───────────────────────────────
def _norm(t):
    t = unicodedata.normalize("NFKC", t).lower()
    t = re.sub(r"[₀-₉]", lambda m: str("₀₁₂₃₄₅₆₇₈₉".index(m.group(0))), t)
    return re.sub(r"[^\w%$]+", " ", t).strip()


def _modulo(mis):
    src = open(f"/home/claude/libro/fis{mis}_icfes.py", encoding="utf-8").read()
    claves = dict(re.findall(r"Q([A-D])\s*·[^·\n]*·\s*([A-D])\b", src[:4000]))
    ops = {}
    for n in ast.parse(src).body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") in ("QA", "QB", "QC", "QD"):
            kw = {k.arg: k.value for k in n.value.keywords}
            try:
                ops[n.targets[0].id[1]] = ast.literal_eval(kw["o"])
            except ValueError:
                ops[n.targets[0].id[1]] = None
    return claves, ops


def _csv(mis):
    filas = [r for r in csv.DictReader(open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig"))
             if r["mision"].strip() == f"FIS M{mis}"]
    return {i + 1: r for i, r in enumerate(filas)}


def verificar(icfes=None):
    """Diferencias entre el .md, los módulos fisN_icfes.py y tablero/icfes.csv (lista vacía = todo bien)."""
    icfes = icfes or leer()
    malas = []
    for mis in range(1, 7):
        claves, ops = _modulo(mis)
        tab = _csv(mis)
        for k in range(1, 5):
            q = "ABCD"[k - 1]
            v = icfes.get((mis, k))
            if not v:
                malas.append(f"M{mis} P{k}: falta en el .md")
                continue
            if len(v["opciones"]) != 4:
                malas.append(f"M{mis} P{k}: {len(v['opciones'])} opciones")
            if not v["enunciado"]:
                malas.append(f"M{mis} P{k}: sin enunciado")
            if claves.get(q) != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · fis{mis}_icfes.py {claves.get(q)}")
            if tab.get(k, {}).get("clave", "").strip() != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · icfes.csv {tab.get(k, {}).get('clave')}")
            if ("ASED" in tab.get(k, {}).get("fuente", "")) != ("ASED" in v["fuente"]):
                malas.append(f"M{mis} P{k}: el .md y icfes.csv no dicen lo mismo sobre el ASED")
            mo = ops.get(q)
            if mo and len(mo) == 4:
                for L, a, b in zip("ABCD", mo, v["opciones"]):
                    if _norm(a) != _norm(b):
                        malas.append(f"M{mis} P{k} {L}: el .md no copia la opción del cuaderno")
            if (MARCA in v["texto"]) != ((mis, k) in FIGURAS):
                malas.append(f"M{mis} P{k}: marca de figura y FIGURAS no coinciden")
            if (mis, k) in FIG_OPCIONES and not all(
                    re.search(r"\b" + L + r"\.?$", o) for L, o in zip("ABCD", v["opciones"])):
                malas.append(f"M{mis} P{k}: las opciones-dibujo deben nombrarse A…D")
    return malas


if __name__ == "__main__":
    d = leer()
    for m in range(1, 7):
        for k in range(1, 5):
            v = d.get((m, k))
            if not v:
                print(f"M{m} P{k}: — FALTA —")
                continue
            print(f"M{m} P{k} · p.{v['pagina']} · clave {v['clave']} · «{v['titulo'][:40]}» · texto "
                  f"{len(v['texto'])} car. · {len(v['opciones'])} opciones · {len(v['notas'])} notas"
                  + (" · figura" if (m, k) in FIGURAS else "") + (" · opciones-dibujo" if (m, k) in FIG_OPCIONES else "")
                  + (" · ASED" if "ASED" in v["fuente"] else ""))
    malas = verificar(d)
    print("claves y opciones: todo coincide" if not malas else "\n".join(["DIFERENCIAS:"] + malas))
