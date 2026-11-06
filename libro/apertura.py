#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hojas de apertura del cuaderno completo: portada, introducción, metas, qué vas a encontrar, psicología."""
import sys, math, random
from lib import *

random.seed(23)
OUT = "/home/claude/libro/"


# ═════════════════════════════ 1 · PORTADA ═════════════════════════════
def portada():
    b = svg_open()
    b.append(rect(0, 0, W, 920, EDU_AZUL, r=0))
    b.append(dots(80, 60, "white", r=3, step=38, cols=50, rows=21, op=0.10))
    b.append(logo(W / 2 - logo_w(180) / 2, 170, 180, chip=True, pad=36, r=32))
    b.append(T(W / 2, 540, ["CUADERNO DE TRABAJO"], 50, "white", weight="700", anchor="middle", ls=9))
    b.append(T(W / 2, 640, ["Saber 11 · las siete áreas de tu libro en un solo cuaderno"], 34, "#BFD4F2", anchor="middle"))
    b.append(T(W / 2, 790, ["Aprende  ·  Practica  ·  Avanza"], 38, EDU_ORO, weight="700", anchor="middle", ls=4))

    # tarjeta de identidad
    y = 1000
    b.append(rect(M, y, CW, 560, "white", r=30, stroke=EDU_AZUL, sw=3))
    b.append(T(M + 60, y + 76, ["Este cuaderno es de"], 30, GRAY, style="italic"))
    for i, (lab, w_) in enumerate([("Nombre", 1060), ("Colegio", 1060), ("Grado y jornada", 520)]):
        yy = y + 180 + i * 120
        b.append(T(M + 60, yy, [lab], 26, EDU_AZUL, weight="700"))
        b.append(line(M + 330, yy + 6, M + 330 + w_, yy + 6, LGRAY, 2.6))
    cx, cy = W - M - 310, y + 300
    b.append(f'<circle cx="{cx}" cy="{cy}" r="170" fill="{CREMA}" stroke="{EDU_ORO}" stroke-width="4"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="128" fill="none" stroke="{EDU_ORO}" stroke-width="2" stroke-dasharray="8,8"/>')
    b.append(T(cx, cy - 66, ["MI META"], 26, EDU_ORO, weight="700", anchor="middle", ls=2))
    b.append(T(cx, cy + 26, ["_____"], 60, EDU_AZUL, anchor="middle"))
    b.append(T(cx, cy + 78, ["puntaje global"], 22, GRAY, anchor="middle"))
    b.append(T(cx, cy + 108, ["(la defines en la hoja 4)"], 19, GRAY, anchor="middle", style="italic"))

    # siete áreas (como en el libro; en la prueba, Biología, Química y Física son Ciencias Naturales)
    y2 = 1640
    t_areas = "Las siete áreas que vas a entrenar aquí"
    b.append(T(M, y2 + 30, [t_areas], 30, EDU_AZUL, weight="700"))
    b.append(T(M + tw(t_areas, 30, "700") + 28, y2 + 30,
               ["(en el Saber 11, Biología, Química y Física se evalúan juntas en Ciencias Naturales)"],
               22, GRAY, style="italic"))
    n_ar = len(AREAS)
    gw = (CW - (n_ar - 1) * 24) / n_ar
    for i, (nm, c) in enumerate(AREAS):
        x = M + i * (gw + 24); yy = y2 + 76
        b.append(rect(x, yy, gw, 190, "white", r=22, stroke=c, sw=3))
        b.append(rect(x, yy, gw, 54, c, r=22))
        b.append(rect(x, yy + 30, gw, 24, c, r=0))
        b.append(T(x + gw / 2, yy + 38, [f"{i+1}"], 28, "white", weight="700", anchor="middle"))
        for j, ln in enumerate(wrap(nm, 13)):
            b.append(T(x + gw / 2, yy + 112 + j * 32, [ln], 25, c, weight="700", anchor="middle"))

    # frase de cierre
    y3 = 1990
    b.append(rect(M, y3, CW, 400, CREMA, r=30))
    b.append(T(M + 60, y3 + 96, ["Este cuaderno no trae las respuestas."], 44, EDU_AZUL, weight="700"))
    b.append(T(M + 60, y3 + 176, ["Trae la forma de pensarlas. Las respuestas las pones tú,"], 32, INK))
    b.append(T(M + 60, y3 + 226, ["con lápiz, después de escribir cómo llegaste a ellas."], 32, INK))
    b.append(face(W - M - 170, y3 + 200, 90, "determined", EDU_AZUL, "#FFE9A8"))
    b.append(hand_arrow(W - M - 520, y3 + 300, W - M - 290, y3 + 230, EDU_ORO, sw=5, bend=-0.3))
    b.append(PT(W - M - 700, y3 + 342, ["ese eres tú"], 36, EDU_ORO, rot=-3))

    b.append(T(W / 2, H_PAGE - 60, ["EDUCATE · Para el Saber"], 24, GRAY, anchor="middle"))
    svg_close(b, OUT + "ap01_portada.svg")


# ═════════════════════════════ 2 · INTRODUCCIÓN (carta) ═════════════════════════════
def intro_1():
    b = svg_open()
    y = frame(b, "Introducción", EDU_AZUL, 2, "para ti, que vas a presentar el Saber 11")
    y = titulo(b, y + 20, "Antes de la primera pregunta", EDU_AZUL)

    # carta a todo el ancho
    y0 = y + 10
    textos = [
        "Hay una pregunta que casi nadie te hace a los dieciséis: ¿quién decide lo que vas a poder elegir después? "
        "Suena grande. Pero se responde con algo pequeño: un número. El puntaje de esta prueba no dice quién eres; "
        "dice qué puertas se abren sin que tengas que pedir permiso. Y ese número no se negocia el día del examen: "
        "se construye los sábados, con lápiz, en hojas como estas.",
        "Este cuaderno existe por una razón simple: la clase del sábado no puede depender de quién la dicte. "
        "Cambian los profesores, cambian los colegios, cambia el ánimo. Lo que no puede cambiar es la forma de "
        "pensar que te lleva a la respuesta correcta. Por eso el método no vive en el profesor: vive aquí, en tus "
        "hojas, con tu letra. El libro trae la pregunta; el cuaderno trae el camino; tú traes la decisión de "
        "escribir lo que piensas antes de marcar.",
        "No te vamos a pedir que seas brillante. Te vamos a pedir que seas honesto con una hoja: que dejes el "
        "error a la vista en vez de borrarlo, que uses el Salvavidas cuando te bloquees, que llenes la bitácora "
        "aunque el día haya salido mal. Una respuesta correcta sin razonamiento escrito no cuenta. Una respuesta "
        "equivocada con el razonamiento escrito sí: ahí es donde se aprende, y ahí es donde el cuaderno deja de "
        "ser de EDUCATE y empieza a ser tuyo.",
        "Al final no vas a tener un cuaderno lleno de respuestas. Vas a tener un diario de cómo aprendiste a "
        "pensar bajo presión. Eso no se olvida después del examen. Eso se queda.",
    ]
    # medir altura
    nl = sum(len(wrap_px(t, 35, CW - 120)) for t in textos)
    bh = 60 + nl * 52 + (len(textos) - 1) * 24 + 160
    b.append(rect(M, y0, CW, bh, CREMA, r=28))
    yy = y0 + 50
    for t in textos:
        yy = parrafo_j(b, M + 60, yy, t, CW - 120, 35, lh=52) + 24
    b.append(PT(M + 60, yy + 30, ["Bienvenido. Empecemos."], 50, EDU_AZUL, rot=-1.2))
    b.append(T(M + 60, yy + 100, ["El equipo de EDUCATE · Para el Saber"], 26, GRAY, style="italic"))
    y = y0 + bh + 70

    # tres paneles
    items = [("Te va a pedir", EDU_AZUL, ["Escribir antes de marcar.", "Llenar la bitácora, siempre.",
                                           "Anotar en qué te equivocaste.", "Llegar con el libro."]),
             ("Te devuelve", EDU_VERDE, ["Una forma de pensar que sirve en las siete áreas.",
                                          "Saber exactamente en qué fallas.", "Tu puntaje subiendo con datos."]),
             ("No es", EDU_ROJO, ["Un cuaderno de respuestas.", "Un libro de teoría.",
                                   "Algo que se llena por cumplir."])]
    pw = (CW - 2 * 40) / 3; ph = 420
    for i, (t, c, ls) in enumerate(items):
        x = M + i * (pw + 40)
        panel(b, x, y + 20, pw, ph, c, title=t, title_size=26)
        yy = y + 20 + 90
        for ln in ls:
            for k, l2 in enumerate(wrap(ln, 27)):
                if k == 0: b.append(f'<circle cx="{x+40}" cy="{yy-11}" r="7" fill="{c}"/>')
                b.append(T(x + 66, yy, [l2], 31, INK))
                yy += 44
            yy += 12
    y += ph + 60

    # cierre emotivo
    b.append(face(M + 140, y + 130, 110, "happy", EDU_AZUL))
    b.append(hand_arrow(M + 300, y + 180, M + 560, y + 130, EDU_ORO, sw=6, bend=0.25))
    b.append(PT(M + 600, y + 110, ["así vas a terminar cada sábado:"], 46, EDU_AZUL, rot=-1.5))
    b.append(PT(M + 600, y + 180, ["cansado, pero sabiendo exactamente qué aprendiste."], 40, EDU_AZUL, rot=-1.5))
    footer(b, 2, EDU_AZUL)
    svg_close(b, OUT + "ap02_intro1.svg")


# ═════════════════════════════ 3 · INTRODUCCIÓN (reglas + hilo) ═════════════════════════════
def intro_2():
    b = svg_open()
    y = frame(b, "Introducción", EDU_AZUL, 3, "las reglas del juego")
    y = titulo(b, y + 20, "Cuatro reglas que no cambian", EDU_AZUL,
               sub="Son pocas a propósito. Si las cumples, el cuaderno funciona con cualquier profesor.")
    reglas = [
        ("Primero el andamiaje, después la respuesta",
         "La letra de la opción se marca al final. Si no escribiste cómo llegaste, la hoja está incompleta aunque la letra sea la correcta.",
         EDU_AZUL, "determined"),
        ("El error escrito vale más que el acierto callado",
         "Equivocarte y dejarlo anotado te muestra qué pensaste mal. Acertar sin escribir no te enseña nada que puedas repetir.",
         EDU_ROJO, "surprised"),
        ("Nadie resuelve por ti, nadie te deja solo",
         "Cada pregunta tiene un Salvavidas: la ruta mínima para desbloquearte. Pedirlo no resta; no pedirlo cuando lo necesitas sí.",
         EDU_VERDE, "calm"),
        ("La bitácora se llena siempre",
         "Al final de cada clase escribes qué entendiste, qué no, y qué vas a hacer distinto. Es la parte del cuaderno que lee la coordinación.",
         EDU_ORO, "proud"),
    ]
    RH = 372
    for i, (t, d, c, mood) in enumerate(reglas):
        yy = y + i * (RH + 34)
        b.append(rect(M, yy, CW, RH, "white", r=26, stroke=c, sw=3))
        b.append(rect(M, yy, 24, RH, c, r=12))
        b.append(num_badge(M + 100, yy + 84, i + 1, c, r=38, size=38))
        b.append(T(M + 170, yy + 98, [t], 42, c, weight="700"))
        parrafo_j(b, M + 170, yy + 138, d, 1440, 32, lh=46)
        b.append(face(W - M - 130, yy + RH / 2, 92, mood, c))
    y += 4 * (RH + 34) + 10

    b.append(T(M, y + 50, ["El hilo que amarra todo"], 42, EDU_AZUL, weight="700"))
    y += 100
    nodes = [("LIBRO", "tiene la pregunta", EDU_ROJO), ("CUADERNO", "tiene el camino para resolverla", EDU_AZUL),
             ("TÚ", "escribes el camino y marcas al final", EDU_VERDE)]
    nw = 520; gap = (CW - 3 * nw) / 2
    for i, (n, d, c) in enumerate(nodes):
        x = M + i * (nw + gap)
        b.append(rect(x, y, nw, 210, c, r=26))
        b.append(T(x + nw / 2, y + 84, [n], 46, "white", weight="700", anchor="middle", ls=3))
        for j, ln in enumerate(wrap(d, 26)):
            b.append(T(x + nw / 2, y + 138 + j * 32, [ln], 26, "#FFFFFF", anchor="middle", op=0.92))
        if i < 2:
            b.append(hand_arrow(x + nw + 16, y + 105, x + nw + gap - 16, y + 105, EDU_ORO, sw=6, bend=-0.25, head=30))
    b.append(PT(M + nw + gap / 2, y + 56, ["la pregunta"], 30, EDU_ORO, rot=-2, anchor="middle"))
    b.append(PT(M + 2 * nw + 1.5 * gap, y + 56, ["el método"], 30, EDU_ORO, rot=-2, anchor="middle"))
    footer(b, 3, EDU_AZUL)
    svg_close(b, OUT + "ap03_intro2.svg")


if __name__ == "__main__":
    portada(); intro_1(); intro_2()
    print("ok 1-3")
