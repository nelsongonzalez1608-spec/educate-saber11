#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figuras de Matemáticas para las guías de clase («clase viva»), en SVG dentro del HTML.

Redibujadas a partir del cuaderno (páginas 13–52) y del libro (pregunta 1 de cada misión), sin
nada del andamiaje del cuaderno: solo lo que trae la pregunta. Así se proyectan nítidas, no
llevan la marca de agua del libro y funcionan sin internet.

Los valores de la gráfica de ganancias (M2 · pregunta 1 del entrenamiento) salen de la
polilínea del cuaderno (página 20), medidos contra su cuadrícula: 4 · 4,5 · 5,8 · 5,8 · 6 ·
4,2 · 3,8 · 4 · 8,4 · 8,1 · 8 · 8 millones.
"""
import math

INK, MUT, LN = "#1B1F27", "#5C6472", "#C9D0DA"
AZ, ROJO, VERDE, ORO = "#1F4E8C", "#A82424", "#2E7A39", "#B0711A"


def svg(w, h, cuerpo, alto=300, rot=""):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{rot}" style="max-height:min({alto}px,34vh)" '
            f'xmlns="http://www.w3.org/2000/svg">{cuerpo}</svg>')


def t(x, y, s, size=15, c=INK, anchor="start", w="400", it=False):
    st = ' font-style="italic"' if it else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{c}" text-anchor="{anchor}" '
            f'font-weight="{w}"{st}>{s}</text>')


def ln(x1, y1, x2, y2, c=INK, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" '
            f'stroke-width="{sw}"{d} stroke-linecap="round"/>')


def poly(pts, fill="none", c=INK, sw=2, dash=None, close=True):
    p = " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    tag = "polygon" if close else "polyline"
    return f'<{tag} points="{p}" fill="{fill}" stroke="{c}" stroke-width="{sw}"{d} stroke-linejoin="round"/>'


def flecha(x1, y, x2, c=INK, sw=2.5):
    s = 1 if x2 > x1 else -1
    return ln(x1, y, x2, y, c, sw) + poly([(x2, y), (x2 - 10 * s, y - 6), (x2 - 10 * s, y + 6)], c, c, 1)


def recto(x, y, dx, dy, s=12):
    """Marca de ángulo recto en el vértice (x, y); dx, dy = hacia dónde abren los catetos (±1)."""
    return poly([(x + dx * s, y), (x + dx * s, y + dy * s), (x, y + dy * s)], c=INK, sw=1.5, close=False)


# ───────────────────────── ejes de una gráfica cartesiana ─────────────────────────
def ejes(x0, y0, x1, y1, xs, ys, xlab, ylab, xt=None, yt=None):
    """Cuadrícula y ejes. xs = (min, max, paso) en datos; ys igual. Devuelve (svg, X, Y)."""
    X = lambda v: x0 + (v - xs[0]) / (xs[1] - xs[0]) * (x1 - x0)
    Y = lambda v: y0 - (v - ys[0]) / (ys[1] - ys[0]) * (y0 - y1)
    o = []
    v = ys[0]
    while v <= ys[1] + 1e-9:
        o.append(ln(x0, Y(v), x1, Y(v), "#E6EAF0", 1))
        o.append(t(x0 - 8, Y(v) + 5, (yt or (lambda q: f"{q:g}"))(v), 13, MUT, "end"))
        v += ys[2]
    v = xs[0]
    while v <= xs[1] + 1e-9:
        o.append(t(X(v), y0 + 20, (xt or (lambda q: f"{q:g}"))(v), 13, MUT, "middle"))
        v += xs[2]
    o.append(ln(x0, y0, x1, y0, INK, 1.6) + ln(x0, y0, x0, y1, INK, 1.6))
    o.append(t((x0 + x1) / 2, y0 + 42, xlab, 14, MUT, "middle"))
    o.append(f'<text x="{x0-44}" y="{(y0+y1)/2}" font-size="14" fill="{MUT}" text-anchor="middle" '
             f'transform="rotate(-90 {x0-44} {(y0+y1)/2})">{ylab}</text>')
    return "".join(o), X, Y


# ═══════════════════════ pregunta modelo (pregunta 1 del libro) ═══════════════════════
def proyectil():
    g, X, Y = ejes(70, 250, 500, 20, (0, 6, 1), (0, 50, 10), "Tiempo (s)", "Altura (m)")
    pts = [(X(k / 20), Y(-5 * (k / 20) ** 2 + 30 * (k / 20))) for k in range(0, 121)]
    g += poly(pts, c=AZ, sw=3, close=False)
    g += f'<circle cx="{X(3)}" cy="{Y(45)}" r="5" fill="{AZ}"/>'
    return svg(530, 300, g, 280, "Gráfica de la altura del proyectil")


def tanque():
    # prisma de base cuadrada 4 × 4 × 3 con pirámide de 6 m encima (perspectiva oblicua)
    k, ox, oy = 34, 70, 330
    dx, dy = 0.5 * 4 * k * 0.8, -0.5 * 4 * k * 0.55
    a = (ox, oy); b = (ox + 4 * k, oy); c = (b[0] + dx, b[1] + dy); d = (a[0] + dx, a[1] + dy)
    h = 3 * k
    A, B, C, D = [(p[0], p[1] - h) for p in (a, b, c, d)]
    cen = ((A[0] + C[0]) / 2, (A[1] + C[1]) / 2 - 6 * k)
    g = poly([a, b, B, A], "#EEF3FA", AZ) + poly([b, c, C, B], "#E1E9F4", AZ)
    g += poly([A, B, cen], "#F4F7FB", AZ) + poly([B, C, cen], "#E9EFF7", AZ)
    g += ln(*a, *d, AZ, 1.5, "5,5") + ln(*d, *c, AZ, 1.5, "5,5") + ln(*d, *D, AZ, 1.5, "5,5")
    g += ln(*D, *cen, AZ, 1.5, "5,5") + ln(*A, *D, AZ, 1.5, "5,5") + ln(*D, *C, AZ, 1.5, "5,5")
    g += t((a[0] + b[0]) / 2, a[1] + 26, "4 m", 16, INK, "middle", "700")
    g += t((b[0] + c[0]) / 2 + 22, (b[1] + c[1]) / 2 + 14, "4 m", 16, INK, "start", "700")
    g += t(a[0] - 10, (a[1] + A[1]) / 2 + 5, "3 m", 16, INK, "end", "700")
    g += ln(cen[0], cen[1], cen[0], (A[1] + C[1]) / 2, ROJO, 1.5, "4,4")
    g += t(cen[0] + 16, cen[1] + 3 * k, "6 m", 16, ROJO, "start", "700")
    g += t(300, 60, "Volumen de la pirámide =", 15, MUT) + t(300, 82, "⅓ · área de la base · altura", 15, MUT)
    return svg(520, 360, g, 300, "Tanque: prisma de base cuadrada con cubierta piramidal")


def maqueta():
    cx, top, r, ry, h = 150, 60, 70, 20, 175
    g = (f'<rect x="{cx-r}" y="{top}" width="{2*r}" height="{h}" fill="#EEF3FA"/>'
         f'<ellipse cx="{cx}" cy="{top+h}" rx="{r}" ry="{ry}" fill="#E1E9F4" stroke="{AZ}" stroke-width="2"/>'
         f'<rect x="{cx-r}" y="{top}" width="{2*r}" height="{h}" fill="#EEF3FA"/>'
         f'<ellipse cx="{cx}" cy="{top}" rx="{r}" ry="{ry}" fill="#F7FAFD" stroke="{AZ}" stroke-width="2"/>')
    g += ln(cx - r, top, cx - r, top + h, AZ) + ln(cx + r, top, cx + r, top + h, AZ)
    g += f'<path d="M {cx-r} {top+h} A {r} {ry} 0 0 0 {cx+r} {top+h}" fill="none" stroke="{AZ}" stroke-width="2"/>'
    g += ln(cx, top, cx + r, top, ROJO, 2) + t(cx + r / 2, top - 6, "2 cm", 15, ROJO, "middle", "700")
    g += ln(cx + r + 22, top, cx + r + 22, top + h, ROJO, 1.5) + t(cx + r + 30, top + h / 2, "5 cm", 15, ROJO, "start", "700")
    g += t(330, 120, "Maqueta a escala 1:100", 17, INK, "start", "700")
    g += t(330, 148, "tanque cilíndrico", 15, MUT) + t(330, 172, "radio 2 cm · altura 5 cm", 15, MUT)
    return svg(560, 280, g, 260, "Tanque cilíndrico de la maqueta a escala 1:100")


# ═══════════════════════ entrenamiento ═══════════════════════
def carros():
    y = 90
    g = ln(40, y, 640, y, INK, 2)
    g += f'<circle cx="90" cy="{y}" r="7" fill="{ROJO}"/><circle cx="420" cy="{y}" r="7" fill="{ROJO}"/>'
    g += t(90, y + 30, "ciudad E", 15, INK, "middle", "700") + t(420, y + 30, "ciudad F", 15, INK, "middle", "700")
    g += ln(90, 40, 420, 40, MUT, 1.5) + ln(90, 32, 90, 48, MUT, 1.5) + ln(420, 32, 420, 48, MUT, 1.5)
    g += t(255, 32, "h", 17, INK, "middle", "700", True)
    g += flecha(100, y - 18, 190, AZ) + t(145, y - 26, "V₁", 15, AZ, "middle", "700")
    g += flecha(430, y - 18, 500, VERDE) + t(465, y - 26, "V₂", 15, VERDE, "middle", "700")
    g += t(560, 40, "V₂ &lt; V₁", 15, MUT, "middle", "400", True)
    g += t(330, 150, "los dos carros salen al mismo tiempo, en la misma dirección", 14, MUT, "middle", "400", True)
    return svg(680, 165, g, 200, "Las ciudades E y F y los dos carros")


GANANCIAS = [4, 4.5, 5.8, 5.8, 6, 4.2, 3.8, 4, 8.4, 8.1, 8, 8]
MESES = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]


def ganancias():
    g, X, Y = ejes(80, 230, 760, 20, (0, 11, 1), (0, 9, 1), "", "Ganancias (millones)",
                   xt=lambda v: MESES[int(round(v))])
    pts = [(X(i), Y(v)) for i, v in enumerate(GANANCIAS)]
    g += poly(pts, c=ROJO, sw=2.6, close=False)
    for x, y in pts:
        g += poly([(x, y - 6), (x + 6, y), (x, y + 6), (x - 6, y)], ROJO, ROJO, 1)
    return svg(780, 262, g, 220, "Ganancias mensuales de la empresa durante un año")


def arboles():
    g, base = "", 200
    for i, (hcm, lab) in enumerate([(120, "120 cm"), (140, "140 cm"), (160, "160 cm"), (None, "¿?")]):
        cx = 95 + i * 165
        hh = (hcm or 180) * 0.95
        top = base - hh
        if hcm:
            g += poly([(cx, top), (cx - 38, base - 14), (cx + 38, base - 14)], "#5EA868", VERDE, 1.5)
            g += f'<rect x="{cx-6}" y="{base-14}" width="12" height="14" fill="#7A5230"/>'
            g += t(cx, top - 10, lab, 16, INK, "middle", "700")
        else:
            g += poly([(cx, top), (cx - 38, base - 14), (cx + 38, base - 14)], "none", ORO, 2, "6,5")
            g += t(cx, top - 10, lab, 18, ORO, "middle", "700")
        g += t(cx, base + 24, f"Árbol {i+1}", 15, MUT, "middle")
    return svg(680, 235, g, 250, "Cuatro árboles en escalera: 120, 140, 160 cm y el cuarto sin medir")


def muro():
    k, ox, oy = 60, 50, 190
    w, hh, dx, dy = 3 * k, 2 * k, 0.5 * k * 1.1, -0.5 * k * 0.8
    a, b = (ox, oy), (ox + w, oy)
    A, B = (ox, oy - hh), (ox + w, oy - hh)
    g = poly([a, b, B, A], "#EEF3FA", ROJO) + poly([b, (b[0] + dx, b[1] + dy), (B[0] + dx, B[1] + dy), B], "#E1E9F4", ROJO)
    g += poly([A, B, (B[0] + dx, B[1] + dy), (A[0] + dx, A[1] + dy)], "#F4F7FB", ROJO)
    g += t((a[0] + b[0]) / 2, oy + 26, "3 m de largo", 15, INK, "middle", "700")
    g += t(ox - 10, oy - hh / 2, "2 m", 15, INK, "end", "700") + t(ox - 10, oy - hh / 2 + 18, "de alto", 13, MUT, "end")
    g += t(B[0] + dx + 8, B[1] + dy + 4, "0,5 m", 15, INK, "start", "700") + t(B[0] + dx + 8, B[1] + dy + 22, "de ancho", 13, MUT)
    return svg(330, 225, g, 230, "Muro de 3 m × 2 m × 0,5 m")


def postes():
    y = 150
    g = ln(30, y, 690, y, INK, 2)
    for x, hh, lab, ang, sl, col in [(150, 100, "10 m", "α = 30°", 150, ROJO), (470, 50, "5 m", "β = ¿?", 75, ORO)]:
        g += ln(x, y, x, y - hh, INK, 4) + f'<circle cx="{x}" cy="{y-hh}" r="7" fill="{INK}"/>'
        g += t(x - 12, y - hh / 2, lab, 15, INK, "end", "700")
        ex, ey = x + sl * math.cos(math.radians(22)), y + sl * math.sin(math.radians(22))
        g += ln(x, y, ex, ey, INK, 2)
        g += f'<path d="M {x+34} {y} A 34 34 0 0 1 {x+34*math.cos(math.radians(22)):.1f} {y+34*math.sin(math.radians(22)):.1f}" fill="none" stroke="{col}" stroke-width="2"/>'
        g += t(x + 30, y + 52, ang, 16, col, "start", "700")
    g += t(150, y - 112, "Poste 1", 15, INK, "middle", "700") + t(470, y - 62, "Poste 2", 15, INK, "middle", "700")
    g += t(690, y - 8, "acera", 13, MUT, "end", "400", True)
    return svg(720, 225, g, 230, "Dos postes de 10 m y 5 m y sus sombras")


def bancas():
    g = f'<rect x="20" y="10" width="330" height="280" rx="6" fill="#FAFBFD" stroke="{MUT}" stroke-width="1.5"/>'
    for lab, x, y in [("p", 70, 30), ("q", 230, 30), ("r", 70, 190), ("s", 230, 190)]:
        g += f'<rect x="{x}" y="{y}" width="80" height="80" rx="4" fill="#EEF3FA" stroke="{ROJO}" stroke-width="2"/>'
        g += t(x + 10, y + 22, lab, 17, ROJO, "start", "700", True)
    g += f'<circle cx="190" cy="150" r="24" fill="#D4D9E0" stroke="{MUT}" stroke-width="1.5"/>'
    g += t(190, 192, "fuente", 13, MUT, "middle", "400", True)
    g += ln(52, 110, 52, 190, VERDE, 2) + ln(44, 110, 60, 110, VERDE, 2) + ln(44, 190, 60, 190, VERDE, 2)
    g += f'<text x="36" y="150" font-size="15" font-weight="700" fill="{VERDE}" text-anchor="middle" transform="rotate(-90 36 150)">10 m</text>'
    g += t(370, 130, "entre los locales p y r", 14, MUT, "start", "400", True)
    g += t(370, 150, "hay 10 m", 14, MUT, "start", "400", True)
    return svg(540, 300, g, 260, "Plano: cuatro locales cuadrados alrededor de una fuente")


def _cubo(x, y, s, cinta=True):
    d, e = s * 0.42, s * 0.32
    g = poly([(x, y), (x + s, y), (x + s, y - s), (x, y - s)], "#F4F7FB", ROJO)
    g += poly([(x + s, y), (x + s + d, y - e), (x + s + d, y - s - e), (x + s, y - s)], "#E6ECF5", ROJO)
    g += poly([(x, y - s), (x + s, y - s), (x + s + d, y - s - e), (x + d, y - s - e)], "#FAFBFD", ROJO)
    if cinta:
        g += f'<rect x="{x}" y="{y-s*0.62}" width="{s}" height="{s*0.2}" fill="#E3B65A"/>'
        g += poly([(x + s, y - s * 0.62), (x + s + d, y - s * 0.62 - e), (x + s + d, y - s * 0.42 - e), (x + s, y - s * 0.42)], "#D6A748", "#D6A748", 1)
    return g


def vela():
    g = _cubo(60, 190, 70) + _cubo(340, 190, 140)
    g += t(95, 216, "lado 2 cm", 15, INK, "middle", "700") + t(410, 216, "lado 4 cm", 15, INK, "middle", "700")
    g += flecha(200, 130, 260, MUT, 2)
    g += t(20, 26, "la cinta rodea la vela por el contorno", 14, MUT, "start", "400", True)
    return svg(560, 230, g, 230, "Vela en cubo de lado 2 cm y de lado 4 cm, con la cinta alrededor")


def bermudas():
    M_, B_, S_ = (60, 150), (300, 40), (380, 190)
    g = poly([M_, B_, S_], "none", INK, 2)
    for (x, y) in (M_, B_, S_):
        g += f'<circle cx="{x}" cy="{y}" r="7" fill="{INK}"/>'
    g += t(48, 155, "Miami", 15, INK, "end", "700") + t(312, 38, "Bermuda", 15, INK, "start", "700")
    g += t(392, 196, "San Juan", 15, INK, "start", "700")
    g += t(165, 84, "1.035 mi", 15, MUT, "middle") + t(362, 112, "954 mi", 15, MUT, "start")
    g += t(222, 192, "1.033 mi", 15, MUT, "middle")
    g += t(20, 222, "distancias en millas", 13, MUT, "start", "400", True)
    return svg(480, 232, g, 230, "Triángulo Miami, Bermuda, San Juan, con distancias en millas")


def triangulos():
    datos = [("A", 12, 9, 15, "abajo"), ("B", 12, 16, 20, "abajo"), ("C", 28, 21, 35, "arriba"),
             ("D", 102, 172, 200, "arriba")]
    g = ""
    for i, (L, v, hz, hip, th) in enumerate(datos):
        ox = 50 + i * 200
        esc = min(125 / v, 150 / hz)
        x0, y0 = ox, 165
        top, rgt = (x0, y0 - v * esc), (x0 + hz * esc, y0)
        g += poly([(x0, y0), top, rgt], "#FAFBFD", INK, 2) + recto(x0, y0, 1, -1)
        g += t(x0 + hz * esc / 2, 22, L, 18, ROJO, "middle", "700")
        g += t(x0 - 8, y0 - v * esc / 2 + 5, str(v), 16, INK, "end")
        g += t(x0 + hz * esc / 2, y0 + 20, str(hz), 16, INK, "middle")
        g += t(x0 + hz * esc / 2 + 10, y0 - v * esc / 2 - 6, str(hip), 16, INK, "start")
        if th == "abajo":
            g += f'<path d="M {rgt[0]-26} {rgt[1]} A 26 26 0 0 1 {rgt[0]-26*math.cos(math.atan2(v,hz)):.1f} {rgt[1]-26*math.sin(math.atan2(v,hz)):.1f}" fill="none" stroke="{ORO}" stroke-width="2"/>'
            g += t(rgt[0] - 40, rgt[1] - 6, "θ", 15, ORO, "middle", "700")
        else:
            a = math.atan2(hz, v)
            g += f'<path d="M {top[0]} {top[1]+26} A 26 26 0 0 0 {top[0]+26*math.sin(a):.1f} {top[1]+26*math.cos(a):.1f}" fill="none" stroke="{ORO}" stroke-width="2"/>'
            g += t(top[0] + 9, top[1] + 40, "θ", 15, ORO, "middle", "700")
    g += t(10, 212, "las medidas están en unidades", 13, MUT, "start", "400", True)
    return svg(820, 220, g, 230, "Cuatro triángulos rectángulos A, B, C y D con el ángulo θ marcado")


def granjero():
    a, b, c = (40, 170), (290, 170), (200, 50)
    g = poly([a, b, c], "#EDF5EE", INK, 2)
    # marca del ángulo recto en c, entre ca y cb
    u = ((a[0] - c[0]) / 200, (a[1] - c[1]) / 200); v = ((b[0] - c[0]) / 150, (b[1] - c[1]) / 150)
    s = 14
    g += poly([(c[0] + u[0] * s, c[1] + u[1] * s), (c[0] + u[0] * s + v[0] * s, c[1] + u[1] * s + v[1] * s),
               (c[0] + v[0] * s, c[1] + v[1] * s)], c=INK, sw=1.5, close=False)
    g += t(122, 96, "cateto 4 m", 15, INK, "end", "700") + t(272, 100, "cateto 3 m", 15, INK, "start", "700")
    g += t(165, 196, "hipotenusa 5 m", 15, INK, "middle", "700")
    return svg(380, 210, g, 220, "Terreno triangular con catetos de 4 m y 3 m e hipotenusa de 5 m")


def regla():
    A, B, C = (70, 30), (70, 230), (220, 230)       # escuadra: 40 cm vertical, 30 cm horizontal
    nx, ny = 0.8, -0.6                               # normal hacia afuera de la hipotenusa
    o, w = 10, 20                                    # separación y ancho de la regla
    r1 = (A[0] + nx * o, A[1] + ny * o); r2 = (C[0] + nx * o, C[1] + ny * o)
    r3 = (r2[0] + nx * w, r2[1] + ny * w); r4 = (r1[0] + nx * w, r1[1] + ny * w)
    g = poly([A, B, C], "#DCE9C4", "#3E5A1E", 2) + poly([(92, 120), (92, 208), (158, 208)], "#FFFFFF", "#3E5A1E", 2)
    g += poly([r1, r2, r3, r4], "#DCE9C4", "#3E5A1E", 2)
    g += t(104, 196, "hueco", 13, MUT, "start", "400", True)
    g += t(60, 135, "40 cm", 15, INK, "end", "700") + t(145, 254, "30 cm", 15, INK, "middle", "700")
    g += t(220, 120, "50 cm", 15, INK, "start", "700")
    g += t(r3[0] + 8, r3[1] + 4, "x", 16, ROJO, "start", "700", True)
    return svg(320, 265, g, 260, "Una escuadra con un hueco triangular y una regla de 50 cm apoyada en su lado largo")


FIG = dict(proyectil=proyectil, tanque=tanque, maqueta=maqueta, carros=carros, ganancias=ganancias,
           arboles=arboles, muro=muro, postes=postes, bancas=bancas, vela=vela, bermudas=bermudas,
           triangulos=triangulos, granjero=granjero, regla=regla)
