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
    """Corrección EDUCATE: qué está mal en el libro y qué hacer. Nunca dice la clave."""
    svg, yy = TJ(x + 30, y + 52, texto, w - 60, 18, INK, lh=26)
    h = yy - y + 54
    b.append(rect(x, y, w, h, CORR_BG, r=14, stroke=CORR_LN, sw=2))
    b.append(rect(x, y, 8, h, CORR, r=4))
    b.append(T(x + 30, y + 32, ["CORRECCIÓN EDUCATE"], 15, CORR, weight="700", ls=1.8))
    b.append(T(x + 30 + tw("CORRECCIÓN EDUCATE", 15, "700") + 18 * 1.8 + 24, y + 32,
               ["el libro trae un error: así lo arreglamos"], 15, GRAY, style="italic"))
    b.append(svg)
    b.append(checkbox(x + 30, yy + 8, s=10, c=CORR))
    b.append(T(x + 60, yy + 25, [cierre_txt], 16, GRAY, style="italic"))
    return y + h


def cierre_mision(titulo, partes, cuenta, pregunta_profe=True):
    """partes: [(rótulo, ayuda)] de lo que me llevo; cuenta: [(texto, total)] para «acerté ___ de N».
    Dibuja con el mismo marco de una tarjeta: es el bloque de cierre de la misión."""

    def cierre(b, y, h):
        c = A["color"]
        x0, w0 = M, CW
        b.append(rect(x0, y, w0, h, "white", r=26, stroke=A["ln"], sw=2.4))
        b.append(rect(x0, y, w0, 104, A["bg"], r=26))
        b.append(rect(x0, y + 60, w0, 44, A["bg"], r=0))
        b.append(f'<circle cx="{x0 + 60}" cy="{y + 52}" r="34" fill="{c}"/>')
        b.append(star(x0 + 60, y + 52, 18, "white"))
        b.append(T(x0 + 112, y + 46, [titulo], 26, c, weight="700"))
        b.append(T(x0 + 112, y + 82, ["Lo escribes al final de la clase, antes de marcar cómo sales."],
                   20, GRAY, style="italic"))
        # columna izquierda · lo que me llevo de cada parte
        lx, lw = x0 + 40, 1060
        yy = y + 150
        for rot_, ayuda in partes:
            b.append(T(lx, yy, [rot_], 16, c, weight="700", ls=1.6))
            b.append(T(lx, yy + 26, [ayuda], 16, GRAY, style="italic"))
            b.append(wlines(lx, yy + 76, lw, 3, c="#E3E8EF", step=48))
            yy += 76 + 2 * 48 + 50
        b.append(T(lx, yy, ["UNA PREGUNTA PARA EL PROFE"], 16, c, weight="700", ls=1.6))
        b.append(T(lx, yy + 26, ["lo que todavía no me cuadra, en una frase"], 16, GRAY, style="italic"))
        b.append(wlines(lx, yy + 76, lw, 2, c="#E3E8EF", step=48))
        # columna derecha · subestrategias y cuenta
        rx = x0 + 1160
        rw = x0 + w0 - 40 - rx
        ry = y + 150
        b.append(T(rx, ry, ["MIS SUBESTRATEGIAS"], 16, c, weight="700", ls=1.6))
        b.append(T(rx, ry + 26, ["marca una como la más fuerte y una como la más floja"], 16, GRAY,
                   style="italic"))
        b.append(T(rx + rw - 150, ry + 60, ["fuerte"], 15, GRAY, anchor="middle"))
        b.append(T(rx + rw - 60, ry + 60, ["floja"], 15, GRAY, anchor="middle"))
        for k in sorted(EST):
            nombre, ec = EST[k]
            yk = ry + 80 + (k - 1) * 70
            b.append(f'<circle cx="{rx + 22}" cy="{yk + 22}" r="20" fill="{ec}"/>')
            b.append(T(rx + 22, yk + 29, [str(k)], 18, "white", weight="700", anchor="middle"))
            for j, ln in enumerate(wrap_px(nombre, 18, rw - 260, "700")[:2]):
                b.append(T(rx + 56, yk + 20 + j * 22 + (11 if len(wrap_px(nombre, 18, rw - 260, "700")) == 1 else 0),
                           [" ".join(ln)], 18, INK, weight="700"))
            b.append(checkbox(rx + rw - 161, yk + 11, s=11, c=ec))
            b.append(checkbox(rx + rw - 71, yk + 11, s=11, c=ec))
        ry += 80 + 4 * 70 + 30
        b.append(T(rx, ry, ["MI CUENTA, CUANDO EL PROFE DÉ LAS CLAVES"], 16, c, weight="700", ls=1.6))
        for j, (txt, tot) in enumerate(cuenta):
            yj = ry + 56 + j * 58
            b.append(T(rx, yj, [txt], 18, INK))
            b.append(rect(rx + rw - 190, yj - 30, 80, 42, "white", r=8, stroke=c, sw=2))
            b.append(T(rx + rw - 96, yj, [f"de {tot}"], 18, INK))
        ry += 56 + len(cuenta) * 58
        b.append(T(rx, ry, ["La que más me costó (número):"], 18, INK))
        b.append(rect(rx + rw - 190, ry - 30, 80, 42, "white", r=8, stroke=c, sw=2))
        ry += 60
        b.append(T(rx, ry, ["y por qué, en pocas palabras:"], 16, GRAY, style="italic"))
        b.append(wlines(rx, ry + 50, rw, 2, c="#E3E8EF", step=48))

    return cierre
