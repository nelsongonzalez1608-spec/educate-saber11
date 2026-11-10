#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Piezas compartidas de las Misiones 1, 2 y 4 de Inglés (v3, 7 nov 2026).

No configura nada (no llama a configurar ni a usar_estrategias): se puede importar desde
cualquier módulo de misión sin pisar la misión de otro.

    correccion(b, x, y, w, texto)     recuadro «Corrección EDUCATE» (decisión de Nelson, 7 nov:
                                      los errores del libro se corrigen en el cuaderno, sin dar
                                      la clave). Devuelve dónde termina.
    cierre_mision(partes, ...)        devuelve la función cierre(b, y, h) que dibuja el cierre de
                                      la misión en el segundo bloque de una hoja de una pregunta.
    ctx_ok(texto)                     la línea de contexto de la tarjeta cabe antes del chip.
"""
from taller_base import *   # noqa: F401,F403
from taller_base import A, EST
import bitacora as BT       # estilo B · Bitácora (10 nov): misma geometría, otro entorno

CORR = "#242478"           # azul institucional: no se confunde con el salvavidas (coral)
CORR_BG = "#F2F3FA"
CORR_LN = "#9C9CC8"
CTX_MAX = 630              # px a 21 itálica: de M + 112 hasta antes del texto «competencia»


def ctx_ok(t):
    w = tw(t, 21, "400", "italic")
    if w > CTX_MAX:
        raise ValueError(f"contexto de {w:.0f} px (máx. {CTX_MAX}): «{t}»")
    return t


def correccion(b, x, y, w, texto, cierre_txt="Lo corregí en mi libro"):
    """Corrección EDUCATE: qué está mal en el libro y qué hacer. Nunca dice la clave.
    Bitácora: recuadro a mano en el azul institucional, fondo claro (se marca con lápiz),
    rótulo en Space Mono con resaltador. Mismo alto que antes."""
    svg, yy = TJ(x + 30, y + 52, texto, w - 60, 18, INK, lh=26)
    h = yy - y + 54
    b.append(BT.wob_rect(x, y, w, h, CORR, 2.4, fill=CORR_BG, seed=int(y) + 5, amp=1.2))
    rot_ = "CORRECCIÓN EDUCATE"
    wr = BT.twf(rot_, 15, BT.MONO, "700")
    b.append(BT.resaltador(x + 30, y + 16, wr, 22, BT.FOSFO, seed=int(y)))
    b.append(BT.TX(x + 30, y + 33, rot_, 15, CORR, BT.MONO, "700"))
    b.append(T(x + 30 + wr + 24, y + 32, ["el libro trae un error: así lo arreglamos"], 15, GRAY,
               style="italic"))
    b.append(svg)
    b.append(BT.wob_rect(x + 30, yy + 8, 20, 20, CORR, 2, fill="white", seed=int(yy), amp=0.6))
    b.append(T(x + 60, yy + 25, [cierre_txt], 16, GRAY, style="italic"))
    return y + h


def cierre_mision(titulo, partes, cuenta, pregunta_profe=True):
    """partes: [(rótulo, ayuda)] de lo que me llevo; cuenta: [(texto, total)] para «acerté ___ de N».
    Dibuja con el mismo marco de una tarjeta: es el bloque de cierre de la misión."""

    def cierre(b, y, h):
        c = A["color"]
        x0, w0 = M, CW
        b.append(BT.wob_rect(x0, y, w0, h, BT.TINTA_B, 3, fill="white", seed=50 + int(y), amp=1.6))
        b.append(BT.wob_circle(x0 + 62, y + 56, 38, c, 2.8, seed=7))
        b.append(BT.estrellita(x0 + 62, y + 56, 18, c, 3))
        wt = BT.twf(titulo, 32, BT.SHA, "800")
        b.append(BT.resaltador(x0 + 118, y + 24, wt, 32, BT.FOSFO, seed=int(y) + 9))
        b.append(BT.TX(x0 + 118, y + 52, titulo, 32, BT.TINTA_B, BT.SHA, "800"))
        b.append(T(x0 + 118, y + 88, ["Lo escribes al final de la clase, antes de marcar cómo sales."],
                   20, GRAY, style="italic"))

        def rot(x, y_, t):
            b.append(BT.TX(x, y_, t, 15, c, BT.MONO, "700"))

        # columna izquierda · lo que me llevo de cada parte
        lx, lw = x0 + 40, 1060
        yy = y + 150
        for rot_, ayuda in partes:
            rot(lx, yy, rot_.upper())
            b.append(T(lx, yy + 26, [ayuda], 16, GRAY, style="italic"))
            b.append(wlines(lx, yy + 76, lw, 3, c="#E3E8EF", step=48))
            yy += 76 + 2 * 48 + 50
        rot(lx, yy, "UNA PREGUNTA PARA EL PROFE")
        b.append(T(lx, yy + 26, ["lo que todavía no me cuadra, en una frase"], 16, GRAY, style="italic"))
        b.append(wlines(lx, yy + 76, lw, 2, c="#E3E8EF", step=48))
        # columna derecha · subestrategias y cuenta (divisor vertical: acento permitido)
        rx = x0 + 1160
        rw = x0 + w0 - 40 - rx
        b.append(BT.wob_vline(rx - 40, y + 130, y + h - 30, seed=int(y) + 1))
        ry = y + 150
        rot(rx, ry, "MIS SUBESTRATEGIAS")
        b.append(T(rx, ry + 26, ["marca una como la más fuerte y una como la más floja"], 16, GRAY,
                   style="italic"))
        b.append(T(rx + rw - 150, ry + 60, ["fuerte"], 15, GRAY, anchor="middle"))
        b.append(T(rx + rw - 60, ry + 60, ["floja"], 15, GRAY, anchor="middle"))
        for k in sorted(EST):
            nombre, ec = EST[k]
            yk = ry + 80 + (k - 1) * 70
            b.append(f'<circle cx="{rx + 22}" cy="{yk + 22}" r="20" fill="white" stroke="{ec}" stroke-width="2.6"/>')
            b.append(BT.TX(rx + 22, yk + 29, str(k), 18, ec, BT.MONO, "700", anchor="middle"))
            lns = wrap_px(nombre, 18, rw - 260, "700")[:2]
            for j, ln in enumerate(lns):
                b.append(T(rx + 56, yk + 20 + j * 22 + (11 if len(lns) == 1 else 0),
                           [" ".join(ln)], 18, INK, weight="700"))
            b.append(BT.wob_rect(rx + rw - 161, yk + 11, 22, 22, ec, 2, fill="white", seed=k + 80, amp=0.6))
            b.append(BT.wob_rect(rx + rw - 71, yk + 11, 22, 22, ec, 2, fill="white", seed=k + 90, amp=0.6))
        ry += 80 + 4 * 70 + 30
        rot(rx, ry, "MI CUENTA, CUANDO EL PROFE DÉ LAS CLAVES")
        for j, (txt, tot) in enumerate(cuenta):
            yj = ry + 56 + j * 58
            b.append(T(rx, yj, [txt], 18, INK))
            b.append(BT.wob_rect(rx + rw - 190, yj - 30, 80, 42, c, 2, fill="white", seed=j + 100, amp=0.8))
            b.append(T(rx + rw - 96, yj, [f"de {tot}"], 18, INK))
        ry += 56 + len(cuenta) * 58
        b.append(T(rx, ry, ["La que más me costó (número):"], 18, INK))
        b.append(BT.wob_rect(rx + rw - 190, ry - 30, 80, 42, c, 2, fill="white", seed=110, amp=0.8))
        ry += 60
        b.append(T(rx, ry, ["y por qué, en pocas palabras:"], 16, GRAY, style="italic"))
        b.append(wlines(rx, ry + 50, rw, 2, c="#E3E8EF", step=48))

    return cierre
