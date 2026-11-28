#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Simulacro · VERSIÓN 2 del cuaderno: UNA página por área (Nelson, 28 nov: «que quede una sola, y que la guía la
hagan los estudiantes después en otra parte»).

Qué hay en la página (una sola cara, en papel claro, todo se llena con lápiz):
  1 · Hoja de respuestas      el número de la pregunta, las opciones A–D y una casilla «acerté»
  2 · Mis resultados          aciertos por competencia (o por parte, en Inglés), puntaje y nivel de desempeño
  3 · Mis tres errores        qué pregunta, por qué fallé (casillas) y qué hago distinto
El análisis pregunta por pregunta (las 54 hojas de la versión 1: esquemas de 3 preguntas por página) sale del
cuaderno y queda como «Guía del simulacro», un cuadernillo aparte (simulacro.py --cuaderno las sigue generando).

    python3 simulacro_1p.py            → libro/sim1_<área>.svg (las 7) y /tmp/.../Simulacro_1p.pdf
    python3 simulacro_1p.py mate       → una sola
"""
import os
import sys

from lib import *            # noqa: F401,F403
import bitacora as BT
import simulacro as S

OUT = os.path.dirname(os.path.realpath(__file__)) + "/"
N_PREG = dict(mate=30, lc=30, soc=30, bio=18, qui=18, fis=18, ing=18)
ERRORES = ["no leí bien", "no sabía el concepto", "me confundí entre dos opciones", "me faltó tiempo", "adiviné"]


def seccion(b, y, txt, c, sub=None):
    wt = BT.twf(txt, 38, BT.SHA, "800")
    b.append(BT.resaltador(M, y + 14, wt, 34, BT.FOSFO, seed=int(y)))
    b.append(BT.TX(M, y + 40, txt, 38, BT.TINTA_B, BT.SHA, "800"))
    if sub:
        b.append(rect(M + wt + 22, y + 14, tw(sub, 22, style="italic") + 12, 32, "white", r=2))
        b.append(T(M + wt + 28, y + 38, [sub], 22, GRAY, style="italic"))
    return y + 74


def cabecera(b, a, c):
    """Misma cabecera de las hojas del cuaderno (logo, área, fecha, caritas), sin los campos de «hoja n de m»."""
    BT.fondo_puntos(b)
    b.append(rect(M - 10, 30, logo_w(62) + 20, 82, "white", r=4))
    b.append(logo(M, 40, 62))
    x0 = M + 200
    t = a["area"]
    s = 50
    while BT.twf(t, s, BT.SHA, "800") > 1240 - x0 - 260 and s > 30:
        s -= 0.5
    wt = BT.twf(t, s, BT.SHA, "800")
    b.append(BT.resaltador(x0, 92 - s * 0.8, wt, s * 0.8, BT.FOSFO, seed=2))
    b.append(BT.TX(x0, 88, t, s, BT.TINTA_B, BT.SHA, "800"))
    b.append(BT.TX(x0 + wt + 22, 86, "/ MI SIMULACRO", 24, c, BT.MONO, "700"))
    sub = "Clase 7: lo presento · Clase 8: reviso mis errores"
    b.append(rect(x0 - 6, 104, tw(sub, 21) + 12, 30, "white", r=2))
    b.append(T(x0, 126, [sub], 21, GRAY))
    nx, ny, nw, nh = 1300, 24, W - M - 1300, 152
    b.append(BT.wob_rect(nx, ny, nw, nh, BT.TINTA_B, 2.6, fill="white", seed=41))
    b.append(T(nx + 28, ny + 52, ["Sábado ____ de ____________"], 24, INK))
    b.append(BT.TX(nx + 28, ny + 116, "LLEGO", 15, GRAY, BT.MONO, "700"))
    b.append(BT.TX(nx + 328, ny + 116, "SALGO", 15, GRAY, BT.MONO, "700"))
    for base in (nx + 120, nx + 420):
        for i, mood in enumerate(["worried", "calm", "happy"]):
            b.append(face(base + i * 62, ny + 108, 22, mood, BT.TINTA_B, "white", sw=2.2))
    y = 206
    b.append(BT.wob_rect(M, y, CW, 78, BT.TINTA_B, 2.6, fill="white", seed=43))
    x = M + 34
    for txt, wl in [("Me llamo", 700), ("Fecha", 250)]:
        b.append(T(x, y + 50, [txt], 21, c, weight="700"))
        x += tw(txt, 21, "700") + 14
        b.append(line(x, y + 54, x + wl, y + 54, S.LN_W, 1.8))
        x += wl + 40
    # el intento: el mismo simulacro se puede presentar más de una vez (puntajes 1, 2 y 3 de la portada del área)
    b.append(T(x, y + 50, ["Intento"], 21, c, weight="700"))
    x += tw("Intento", 21, "700") + 22
    for lab in ("1.º", "2.º", "3.º"):
        b.append(rect(x, y + 28, 30, 30, "white", r=5, stroke=c, sw=2.4))
        b.append(T(x + 40, y + 52, [lab], 22, INK, weight="700"))
        x += 40 + tw(lab, 22, "700") + 34
    return y + 78


def hoja_respuestas(b, y, n, c):
    cols = 3
    filas = n // cols
    cw = CW / cols
    for k in range(n):
        col, fila = k // filas, k % filas
        x0 = M + col * cw
        yy = y + fila * 64
        b.append(BT.TX(x0 + 20, yy + 38, f"{k + 1:02d}", 24, BT.TINTA_B, BT.MONO, "700"))
        for i, L in enumerate("ABCD"):
            cx = x0 + 120 + i * 62
            b.append(f'<circle cx="{cx}" cy="{yy + 28}" r="22" fill="white" stroke="{c}" stroke-width="2.4"/>')
            b.append(T(cx, yy + 28 + 8, [L], 22, c, weight="700", anchor="middle"))
        b.append(rect(x0 + 392, yy + 12, 32, 32, "white", r=5, stroke=GRAY, sw=2.2))
        b.append(T(x0 + 436, yy + 36, ["acerté"], 19, GRAY))
        if col < cols - 1:
            b.append(BT.wob_vline(x0 + cw - 8, yy + 4, yy + 56, seed=k))
    return y + filas * 64 + 16


def resultados(b, y, a, c, n):
    comp = a["comp"]
    # tabla: una fila por competencia / parte
    ancho_nom = 980
    b.append(BT.wob_rect(M, y, CW, 70 + len(comp) * 62 + 20, BT.TINTA_B, 2.6, fill="white", seed=int(y) + 3))
    b.append(BT.TX(M + 34, y + 44, a["rot_comp"].upper(), 18, GRAY, BT.MONO, "700"))
    b.append(BT.TX(M + ancho_nom + 60, y + 44, "ACIERTOS", 18, GRAY, BT.MONO, "700"))
    b.append(BT.TX(M + ancho_nom + 330, y + 44, "DE", 18, GRAY, BT.MONO, "700"))
    for k, nom in enumerate(comp):
        yy = y + 70 + k * 62
        b.append(T(M + 34, yy + 30, [nom], 24, INK))
        b.append(line(M + ancho_nom + 60, yy + 38, M + ancho_nom + 230, yy + 38, S.LN_W, 2))
        b.append(T(M + ancho_nom + 330, yy + 34, ["____"], 24, GRAY))
    yb = y + 70 + len(comp) * 62 + 20
    # puntaje y nivel
    bw = (CW - 2 * 24) / 3
    cajas = [("Mi puntaje", "(de 0 a 100)"), ("Mi nivel", "1 · 2 · 3 · 4"), ("Mi meta", "(la de la portada del área)")]
    for k, (t, sub) in enumerate(cajas):
        x = M + k * (bw + 24)
        b.append(BT.wob_rect(x, yb + 14, bw, 132, c if k == 2 else BT.TINTA_B, 2.6, fill="white", seed=int(yb) + k))
        b.append(BT.TX(x + 28, yb + 62, t, 30, c, BT.SHA, "800"))
        b.append(T(x + 28, yb + 92, [sub], 19, GRAY, style="italic"))
        b.append(line(x + 28, yb + 126, x + bw - 28, yb + 126, S.LN_W, 2.2))
    return yb + 14 + 132 + 10


def errores(b, y, c):
    ancho = (CW - 2 * 24) / 3
    for k in range(3):
        x = M + k * (ancho + 24)
        b.append(BT.wob_rect(x, y, ancho, 560, BT.TINTA_B, 2.6, fill="white", seed=int(y) + 20 + k))
        b.append(BT.wob_circle(x + 44, y + 50, 26, c, 2.6, seed=k + 5))
        b.append(BT.TX(x + 44, y + 59, str(k + 1), 24, c, BT.MONO, "700", anchor="middle"))
        b.append(T(x + 90, y + 58, ["Pregunta n.º"], 24, c, weight="700"))
        b.append(line(x + 90 + tw("Pregunta n.º", 24, "700") + 14, y + 62, x + ancho - 30, y + 62, S.LN_W, 2.2))
        b.append(BT.TX(x + 28, y + 112, "POR QUÉ FALLÉ", 16, GRAY, BT.MONO, "700"))
        for j, e in enumerate(ERRORES):
            yy = y + 150 + j * 46
            b.append(rect(x + 28, yy - 14, 22, 22, "white", r=4, stroke=c, sw=2.2))
            b.append(T(x + 62, yy + 4, [e], 20, INK))
        b.append(BT.TX(x + 28, y + 410, "LO QUE HAGO DISTINTO", 16, GRAY, BT.MONO, "700"))
        for j in range(3):
            b.append(line(x + 28, y + 454 + j * 40, x + ancho - 28, y + 454 + j * 40, S.LN_W, 2.2))
    return y + 560


def hoja(clave, ruta, pag=None):
    a = S.AREA[clave]
    S.colores(a["area"])
    c = S.C["c"]
    n = N_PREG[clave]
    b = svg_open()
    y = cabecera(b, a, c) + 26
    y = seccion(b, y, "Mi hoja de respuestas", c, f"{n} preguntas · marco aquí lo que respondí en el simulacro")
    y = hoja_respuestas(b, y, n, c)
    y = seccion(b, y + 10, "Mis resultados", c, "los lleno en la clase 8, con las claves a la vista")
    y = resultados(b, y, a, c, n)
    y = seccion(b, y + 14, "Mis tres errores más caros", c, "uno por tarjeta: lo que pasó y lo que cambio")
    y = errores(b, y, c)
    assert y < H_PAGE - 150, f"{clave}: el contenido llega a {y:.0f}"
    BT.pie_b(b, pag if pag is not None else "S1", c, texto=f"{a['area']} · Mi simulacro")
    svg_close(b, ruta)
    return ruta


ORDEN = ["mate", "lc", "soc", "bio", "qui", "fis", "ing"]

if __name__ == "__main__":
    import render
    claves = sys.argv[1:] or ORDEN
    rutas = [hoja(cl, OUT + f"sim1_{cl}.svg") for cl in claves]
    os.makedirs("/tmp/claude-0/simulacro", exist_ok=True)
    pdf = "/tmp/claude-0/simulacro/Simulacro_1p.pdf"
    render.unir(rutas, pdf)
    print(pdf, render.verifica(pdf, marca="Aprende"))
