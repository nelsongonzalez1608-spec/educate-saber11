#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Apertura nueva del cuaderno · estilo B · Bitácora · 6 páginas (PROPUESTA, 10 nov 2026).

Nelson la aprobó en principio. NO está en el cuaderno ni en el manifiesto: cambia la numeración
(la apertura actual tiene 9 páginas) y eso se hace en un paso final aparte. Genera
libro/ap_b_1.svg … ap_b_6.svg:

    1  portada (la de la propuesta B, con el índice)
    2  «Antes de la primera pregunta» + «Cuatro reglas que no cambian»      (antes págs. 2 y 3)
    3  «Ponle un número a tu meta» + «Mi tablero de metas»                    (antes págs. 4 y 5)
    4  «Así se lee una hoja» + «Siete áreas, seis momentos, ocho clases»      (antes págs. 6 y 7)
    5  «Lo que pasa en tu cabeza»                                             (antes pág. 8)
    6  «Cómo leer este cuaderno» (para la coordinación)                       (antes pág. 9)

El contenido sale de apertura.py, apertura2.py y apertura3.py. Lo que cambió de texto (para que
Nelson lo apruebe) está marcado con «# TEXTO NUEVO» en este archivo:
  · las hojas de hoy ya no tienen «cuadrícula», «paso a paso» ni «piensa en esto»: donde la
    apertura vieja los nombraba, ahora dice «el instrumento»;
  · «la hoja 4 / la hoja 5» → «la página 3» (metas y tablero quedan en la misma página);
  · «Así se lee una hoja» explica la hoja de verdad (una miniatura de la página 178, antes 151);
  · un momento = una clase de contenido (CLAUDE.md § 1); antes decía que un momento no cabía en
    una clase.
El sello «Primero el andamiaje, después la respuesta» de la portada lo propuso Claude.

    python3 apertura_b.py        → libro/ap_b_1.svg … ap_b_6.svg y /tmp/claude-0/apertura_b/Apertura_B.pdf
"""
import math
import os
import random

from lib import *                    # noqa: F401,F403
import bitacora as BT
from bitacora import (TX, twf, fit, SHA, MONO, HAND, FOSFO, FOSFO_2, TINTA_B, resaltador,
                      wob_rect, wob_circle, estrellita, flechita, sello_redondo)
from apertura2 import CARRERAS

LIBRO = os.path.dirname(os.path.realpath(__file__)) + "/"
PSI = "#5B3E96"

# Numeración que tendrá el cuaderno cuando entre esta apertura (paso final aparte). Es el «mapa final
# de páginas (propuesto)» de tablero/decisiones.csv (10 nov): cada área con portada, 6 misiones y su
# simulacro al final; cierre de 2 páginas y la última cara con el mensaje final (398, Nelson 10 nov):
# 398 en total. Es el de libro/paginas.py; si el mapa cambia, se cambia allá y aquí.
N_AP = 6
P_METAS = 3
MAPA = [("Apertura", "1–6", None), ("Matemáticas", "7–59", 0), ("Lectura Crítica", "60–112", 1),
        ("Sociales y Ciudadanas", "113–165", 2), ("Biología", "166–214", 3), ("Química", "215–263", 4),
        ("Física", "264–312", 5), ("Inglés", "313–395", 6), ("Cierre", "396–398", None)]


def indice():
    return MAPA


# ───────── piezas ─────────
def pagina():
    b = svg_open()
    BT.fondo_puntos(b)
    return b


def cabecera(b, seccion, sub, c):
    b.append(rect(M - 10, 36, logo_w(70) + 20, 94, "white", r=4))
    b.append(logo(M, 48, 70))
    t = f"§ {seccion.upper()}"
    w = twf(t, 26, MONO, "700")
    b.append(resaltador(W - M - w, 54, w, 34, FOSFO_2, seed=303))
    b.append(TX(W - M, 82, t, 26, TINTA_B, MONO, "700", anchor="end"))
    st = sub.upper()
    b.append(rect(W - M - twf(st, 16, MONO) - 8, 100, twf(st, 16, MONO) + 8, 30, "white", r=2))
    b.append(TX(W - M, 120, st, 16, GRAY, MONO, anchor="end"))
    b.append(estrellita(W - M - w - 50, 70, 13, c))
    return 180


def titulo(b, y, txt, marca=None, sub=None, size=68, fill=FOSFO, seed=11, sub_size=25):
    BT.titulo_b(b, M, y + size * 0.8, txt, size, marca=marca, fill=fill, seed=seed)
    y += size * 0.8 + 22
    if sub:
        lines = wrap_px(sub, sub_size, CW, "400", "italic")
        lh = sub_size * 1.42
        b.append(rect(M - 8, y - 4, CW + 16, lh * len(lines) + 10, "white", r=2))
        svg, y = TJ(M, y, sub, CW, sub_size, GRAY, style="italic", lh=lh)
        b.append(svg)
    return y + 14


def caja(b, x, y, w, h, c=TINTA_B, sw=2.8, seed=0, fill="white"):
    b.append(wob_rect(x, y, w, h, c, sw, fill=fill, seed=seed))


def h2(b, x, y, txt, c=TINTA_B, size=32, marca=False, fill=FOSFO, seed=5):
    if marca:
        b.append(resaltador(x, y - size * 0.78, twf(txt, size, SHA, "800"), size * 0.8, fill, seed=seed))
    b.append(TX(x, y, txt, size, c, SHA, "800"))
    return twf(txt, size, SHA, "800")


def rot(b, x, y, txt, c, size=16, anchor="start"):
    b.append(TX(x, y, txt.upper(), size, c, MONO, "700", anchor=anchor))
    return twf(txt.upper(), size, MONO, "700")


def num(b, cx, cy, n, c, r=28, size=24, seed=1):
    b.append(wob_circle(cx, cy, r, c, 2.6, seed=seed, fill="white"))
    b.append(TX(cx, cy + size * 0.36, f"{n:02d}" if isinstance(n, int) else n, size, c, MONO, "700",
                anchor="middle"))


def vinetas(b, x, y, items, w, size, c, lh=None, gap=10, color=INK):
    lh = lh or size * 1.38
    for it in items:
        lns = wrap_px(it, size, w - 30)
        b.append(f'<circle cx="{x + 7}" cy="{y - size * 0.32:.1f}" r="6" fill="{c}"/>')
        for j, ln in enumerate(lns):
            b.append(T(x + 30, y + j * lh, [" ".join(ln)], size, color))
        y += len(lns) * lh + gap
    return y


def mano(b, x, y, txt, c, size=40, rot_=-0.8, anchor="start"):
    b.append(TX(x, y, txt, size, c, HAND, "700", rot=rot_, anchor=anchor))


# ═════════════════════════════ 1 · PORTADA ═════════════════════════════
FRASE = ("Este cuaderno no trae las respuestas.",
         "Trae la forma de pensarlas. Las respuestas las pones tú,",
         "con lápiz, después de escribir cómo llegaste a ellas.")


def portada():
    b = pagina()
    b.append(rect(M - 14, 70, logo_w(110) + 28, 136, "white", r=4))
    b.append(logo(M, 82, 110))
    t = "CUADERNO DE TRABAJO"
    b.append(rect(W - M - twf(t, 28, MONO, "700") - 20, 104, twf(t, 28, MONO, "700") + 20, 52, "white", r=2))
    b.append(TX(W - M - 10, 140, t, 28, TINTA_B, MONO, "700", anchor="end"))
    s1 = "Saber"
    b.append(TX(M - 8, 560, s1, 300, TINTA_B, SHA, "800"))
    x11 = M + twf(s1, 300, SHA, "800") + 30
    w11 = twf("11", 300, SHA, "800")
    b.append(resaltador(x11 - 10, 330, w11 + 20, 220, FOSFO, seed=201, rot=-2))
    b.append(TX(x11, 560, "11", 300, TINTA_B, SHA, "800"))
    b.append(estrellita(x11 + w11 + 70, 300, 34, EDU_ROJO, 4))
    b.append(estrellita(x11 + w11 + 130, 400, 18, EDU_AZUL, 3))
    sub = "las siete áreas de tu libro en un solo cuaderno"
    b.append(rect(M - 8, 610, twf(sub, 44, SHA, "400") + 16, 64, "white", r=2))
    b.append(TX(M, 656, sub, 44, TINTA_B, SHA))
    x = M
    for k, pal in enumerate(["Aprende", "Practica", "Avanza"]):
        w = BT.sello_mono(b, x, 720, pal.upper(), EDU_AZUL, size=26, h=60, pad=20, ang=(-2, 1.5, -1)[k])
        x += w + 20
        if k < 2:
            b.append(flechita(x - 8, 752, x + 46, 752, EDU_ORO, sw=3.5, bend=0.25, head=14, seed=k))
            x += 64
    # sello propuesto por Claude (decirlo en el informe)
    b.append(sello_redondo(1640, 520, 150, ("PRIMERO EL", "ANDAMIAJE", "después la", "respuesta"),
                           EDU_ROJO, -12))
    # de quién es y la meta (se escribe: recuadros blancos)
    lx, ly, lw = M, 900, 900
    caja(b, lx, ly, lw, 560, sw=3, seed=210)
    rot(b, lx + 40, ly + 66, "Esta bitácora es de", TINTA_B, 24)
    for i, lab in enumerate(["Nombre", "Colegio", "Grado y jornada"]):
        yy = ly + 170 + i * 120
        b.append(TX(lx + 40, yy, lab, 28, EDU_AZUL, SHA, "700"))
        b.append(line(lx + 40, yy + 52, lx + lw - 40, yy + 52, LGRAY, 2.6))
    mx, my = lx, ly + 610
    caja(b, mx, my, lw, 460, sw=3, seed=211)
    b.append(resaltador(mx + 36, my + 40, twf("MI META", 30, MONO, "700"), 34, FOSFO_2, seed=212))
    b.append(TX(mx + 36, my + 68, "MI META", 30, TINTA_B, MONO, "700"))
    b.append(wob_circle(mx + 300, my + 260, 150, EDU_ORO, 4, seed=213, fill="white"))
    b.append(TX(mx + 300, my + 270, "_____", 70, EDU_AZUL, SHA, "700", anchor="middle"))
    b.append(TX(mx + 300, my + 320, "puntaje global", 24, GRAY, anchor="middle"))
    mano(b, mx + 540, my + 190, "la defines en", EDU_ORO, 38, 0)
    mano(b, mx + 540, my + 234, f"la página {P_METAS}", EDU_ORO, 38, 0)              # TEXTO NUEVO (antes «hoja 4»)
    b.append(flechita(mx + 620, my + 262, mx + 470, my + 310, EDU_ORO, sw=3.5, bend=-0.35, head=16, seed=9))
    # índice
    rx, ry, rw = M + 960, 900, CW - 960
    caja(b, rx, ry, rw, 1070, sw=3, seed=220)
    b.append(resaltador(rx + 40, ry + 36, twf("ÍNDICE", 34, MONO, "700"), 38, FOSFO, seed=221))
    b.append(TX(rx + 40, ry + 68, "ÍNDICE", 34, TINTA_B, MONO, "700"))
    b.append(TX(rx + 260, ry + 66, "las siete áreas que vas a entrenar aquí", 22, GRAY, style="italic"))
    yy = ry + 150
    for nm, pags, ia in indice():
        c = AREAS[ia][1] if ia is not None else GRAY
        if ia is not None:
            b.append(rect(rx + 40, yy - 34, 44, 44, c, r=6))
            b.append(TX(rx + 62, yy - 2, str(ia + 1), 24, "white", MONO, "700", anchor="middle"))
        else:
            b.append(wob_rect(rx + 42, yy - 32, 40, 40, GRAY, 2, seed=int(yy), amp=.8))
        b.append(TX(rx + 110, yy, nm, 34, TINTA_B if ia is not None else GRAY, SHA, "700"))
        b.append(TX(rx + rw - 40, yy, f"p. {pags}", 24, c, MONO, "700", anchor="end"))
        yy += 96
    mano(b, rx + 40, ry + 1010, "En el Saber 11, Biología, Química y Física", GRAY, 30, 0)
    mano(b, rx + 40, ry + 1046, "se evalúan juntas en Ciencias Naturales.", GRAY, 30, 0)
    # la frase
    y3 = 2050
    caja(b, M, y3, CW, 400, sw=3, seed=230)
    w0 = twf(FRASE[0], 52, SHA, "800")
    b.append(resaltador(M + 50, y3 + 62, w0, 50, FOSFO, seed=231))
    b.append(TX(M + 50, y3 + 104, FRASE[0], 52, TINTA_B, SHA, "800"))
    b.append(TX(M + 50, y3 + 186, FRASE[1], 33, INK))
    b.append(TX(M + 50, y3 + 234, FRASE[2], 33, INK))
    b.append(face(W - M - 190, y3 + 210, 92, "determined", TINTA_B, "#FFE9A8"))
    b.append(flechita(W - M - 560, y3 + 330, W - M - 310, y3 + 262, EDU_ORO, sw=5, bend=-0.3, head=24, seed=4))
    mano(b, W - M - 760, y3 + 350, "ese eres tú", EDU_ORO, 48, -3)
    t = "EDUCATE · PARA EL SABER"
    b.append(rect(W / 2 - twf(t, 20, MONO) / 2 - 10, H_PAGE - 80, twf(t, 20, MONO) + 20, 40, "white", r=2))
    b.append(TX(W / 2, H_PAGE - 52, t, 20, GRAY, MONO, anchor="middle"))
    return b


# ═════════════════════════════ 2 · ANTES DE LA PRIMERA PREGUNTA + REGLAS ═════════════════════════════
CARTA = [
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
PIDE = [("Te va a pedir", EDU_AZUL, ["Escribir antes de marcar.", "Llenar la bitácora, siempre.",
                                     "Anotar en qué te equivocaste.", "Llegar con el libro."]),
        ("Te devuelve", EDU_VERDE, ["Una forma de pensar que sirve en las siete áreas.",
                                    "Saber exactamente en qué fallas.", "Tu puntaje subiendo con datos."]),
        ("No es", EDU_ROJO, ["Un cuaderno de respuestas.", "Un libro de teoría.",
                             "Algo que se llena por cumplir."])]
REGLAS = [
    ("Primero el andamiaje, después la respuesta",
     "La letra de la opción se marca al final. Si no escribiste cómo llegaste, la hoja está incompleta "
     "aunque la letra sea la correcta.", EDU_AZUL, "determined"),
    ("El error escrito vale más que el acierto callado",
     "Equivocarte y dejarlo anotado te muestra qué pensaste mal. Acertar sin escribir no te enseña nada "
     "que puedas repetir.", EDU_ROJO, "surprised"),
    ("Nadie resuelve por ti, nadie te deja solo",
     "Cada pregunta tiene un Salvavidas: la ruta mínima para desbloquearte. Pedirlo no resta; no pedirlo "
     "cuando lo necesitas sí.", EDU_VERDE, "calm"),
    ("La bitácora se llena siempre",
     "Al final de cada clase escribes qué entendiste, qué no, y qué vas a hacer distinto. Es la parte del "
     "cuaderno que lee la coordinación.", EDU_ORO, "proud"),
]


def intro():
    b = pagina()
    y = cabecera(b, "Introducción", "para ti, que vas a presentar el Saber 11", EDU_AZUL)
    y = titulo(b, y + 10, "Antes de la primera pregunta", marca="primera pregunta")
    # carta (izquierda) y lo que pide / devuelve / no es (derecha)
    top = y + 10
    LW = 1190
    yy = top + 46
    svgs = []
    for t in CARTA:
        svg, yy = TJ(M + 44, yy, t, LW - 88, 27, INK, lh=40)
        svgs.append(svg)
        yy += 14
    yy += 8
    h = yy - top + 150
    caja(b, M, top, LW, h, sw=3, seed=401)
    b.extend(svgs)
    mano(b, M + 44, yy + 50, "Bienvenido. Empecemos.", EDU_AZUL, 50, -1.2)
    b.append(T(M + 44, yy + 104, ["El equipo de EDUCATE · Para el Saber"], 24, GRAY, style="italic"))
    rx, rw = M + LW + 36, CW - LW - 36
    ry = top
    for k, (t, c, items) in enumerate(PIDE):
        n_l = sum(len(wrap_px(it, 25, rw - 90)) for it in items)
        ph = 80 + n_l * 34 + len(items) * 10 + 14
        caja(b, rx, ry, rw, ph, c=c, sw=2.6, seed=410 + k)
        h2(b, rx + 28, ry + 50, t, c, 30)
        vinetas(b, rx + 30, ry + 100, items, rw - 60, 25, c, lh=34, gap=10)
        ry += ph + 24
    # así vas a terminar cada sábado
    b.append(face(rx + 70, ry + 82, 58, "happy", EDU_AZUL))
    mano(b, rx + 150, ry + 66, "así vas a terminar cada sábado:", EDU_AZUL, 34, -1.5)
    for j, ln in enumerate(wrap_px("cansado, pero sabiendo exactamente qué aprendiste.", 34, rw - 160)):
        mano(b, rx + 150, ry + 112 + j * 40, " ".join(ln), EDU_AZUL, 34, -1.5)
    y = top + h + 50
    # reglas
    y = titulo(b, y, "Cuatro reglas que no cambian", marca="no cambian", size=54, fill=FOSFO_2, seed=12,
               sub="Son pocas a propósito. Si las cumples, el cuaderno funciona con cualquier profesor.",
               sub_size=24)
    gw = (CW - 30) / 2
    gh = 320
    for i, (t, d, c, mood) in enumerate(REGLAS):
        x = M + (i % 2) * (gw + 30)
        yy = y + 10 + (i // 2) * (gh + 26)
        caja(b, x, yy, gw, gh, c=c, sw=3, seed=420 + i)
        b.append(rect(x, yy, 14, gh, c, r=0))          # acento vertical (permitido)
        num(b, x + 76, yy + 66, i + 1, c, r=36, size=30, seed=i + 2)
        tt = wrap_px(t, 30, gw - 170)
        for j, ln in enumerate(tt):
            b.append(TX(x + 134, yy + 66 + j * 38, " ".join(ln), 30, c, SHA, "800"))
        ty = yy + 66 + (len(tt) - 1) * 38 + 26
        parrafo_j(b, x + 134, ty, d, gw - 320, 26, lh=37)
        b.append(face(x + gw - 96, yy + gh - 100, 66, mood, c))
    y += 10 + 2 * gh + 26 + 40
    # el hilo
    h2(b, M, y + 34, "El hilo que amarra todo", EDU_AZUL, 34)
    y += 64
    nodes = [("LIBRO", "tiene la pregunta", EDU_ROJO), ("CUADERNO", "tiene el camino para resolverla", EDU_AZUL),
             ("TÚ", "escribes el camino y marcas al final", EDU_VERDE)]
    nw = 500
    gap = (CW - 3 * nw) / 2
    for i, (n, d, c) in enumerate(nodes):
        x = M + i * (nw + gap)
        caja(b, x, y, nw, 170, c=c, sw=3.2, seed=430 + i)
        b.append(resaltador(x + nw / 2 - twf(n, 38, MONO, "700") / 2, y + 30, twf(n, 38, MONO, "700"), 34,
                            BT.FOSFO if i != 1 else FOSFO_2, seed=440 + i))
        b.append(TX(x + nw / 2, y + 60, n, 38, c, MONO, "700", anchor="middle"))
        b.append(T(x + nw / 2, y + 124, [d], 26, INK, anchor="middle"))
        if i < 2:
            b.append(flechita(x + nw + 16, y + 80, x + nw + gap - 16, y + 80, EDU_ORO, sw=5, bend=-0.25,
                              head=24, seed=450 + i))
    mano(b, M + nw + gap / 2, y + 36, "la pregunta", EDU_ORO, 30, -2, anchor="middle")
    mano(b, M + 2 * nw + 1.5 * gap, y + 36, "el método", EDU_ORO, 30, -2, anchor="middle")
    BT.pie_b(b, 2, EDU_AZUL)
    return b


# ═════════════════════════════ 3 · METAS ═════════════════════════════
WOOP = [
    ("1 · Deseo", EDU_AZUL, "Lo que quiero lograr con esta prueba, en una frase que me importe de verdad.",
     "lines", "happy"),
    ("2 · Resultado", EDU_VERDE, "El día que lo logro: ¿dónde estoy, con quién, qué siento? Dibújalo o "
     "escríbelo. Pega una foto si quieres.", "draw", "proud"),
    ("3 · Obstáculo", EDU_ROJO, "Lo que está en MÍ que me lo puede impedir. No el profe, no el colegio, no el "
     "tiempo: yo.", "lines", "worried"),
    ("4 · Plan", EDU_ORO, "Cuando aparezca el obstáculo, esto es lo que voy a hacer. Escríbelo como "
     "«si… entonces…».", "ifthen", "determined"),
]


def metas():
    random.seed(41)
    b = pagina()
    y = cabecera(b, "Metas", "¿para qué estoy entrenando?", EDU_ORO)
    y = titulo(b, y + 10, "Ponle un número a tu meta", marca="un número",
               sub="El Saber 11 se califica de 0 a 500 en el puntaje global y de 0 a 100 en cada área. "
                   "Una meta sin número no se puede entrenar.", sub_size=24)
    top = y + 6
    LH = 800
    # escala
    LX, LW = M, 900
    caja(b, LX, top, LW, LH, sw=2.8, seed=331)
    h2(b, LX + 36, top + 58, "La escala del puntaje global", EDU_AZUL, 28)
    ax, y0, y1 = LX + 110, top + 740, top + 110

    def yv(v):
        return y0 - (y0 - y1) * v / 500
    rnd = random.Random(7)
    b.append(BT._trazo([(ax + rnd.uniform(-1, 1), yy) for yy in range(int(y1), int(y0), 30)] + [(ax, y0)],
                       EDU_AZUL, 5))
    for v in range(0, 501, 50):
        b.append(line(ax - 12, yv(v), ax + 12, yv(v), EDU_AZUL, 3))
        b.append(TX(ax - 26, yv(v) + 8, str(v), 20, GRAY, MONO, anchor="end"))
    marcas = [(250, "Promedio nacional aproximado", "la mitad de los estudiantes queda por debajo", GRAY),
              (300, "Corte de admisión en universidades privadas", "p. ej. Universidad de los Andes 2026-2: 300 a 320", EDU_AZUL),
              (350, "Becas y oportunidades", "desde aquí se abren becas, créditos condonables y cupos que no dependen de pagar", EDU_VERDE),
              (420, "Carreras más exigidas", "Medicina, Ingeniería civil, Derecho en universidades top", EDU_ROJO)]
    for v, t, d, c in marcas:
        yy = yv(v)
        b.append(line(ax + 16, yy, ax + 60, yy, c, 3, "6,6"))
        b.append(wob_circle(ax + 70, yy, 10, c, 3, seed=v, fill="white"))
        b.append(T(ax + 92, yy - 4, [f"{v}  ·  {t}"], 24, c, weight="700"))
        b.append(T(ax + 92, yy + 24, [d], 19, GRAY, style="italic"))
    nx, ny, nw_, nh_ = LX + 470, top + 560, 400, 210
    caja(b, nx, ny, nw_, nh_, c=EDU_ORO, sw=2.4, seed=332)
    b.append(T(nx + 22, ny + 40, ["Marca con lápiz sobre la escala:"], 20, EDU_ORO, weight="700"))
    b.append(spath([(nx + 28, ny + 84), (nx + 72, ny + 84)], EDU_ORO, 6, 1))
    b.append(T(nx + 88, ny + 91, ["HOY · tu primer simulacro"], 20, INK))
    b.append(spath([(nx + 28, ny + 132), (nx + 72, ny + 132)], EDU_AZUL, 6, 1))
    b.append(T(nx + 88, ny + 139, ["META · el puntaje que necesitas"], 20, INK))
    b.append(T(nx + 22, ny + 184, ["Entre las dos rayas está tu trabajo."], 19, GRAY, style="italic"))
    # tabla de carreras
    RX = LX + LW + 30
    RW = W - M - RX
    caja(b, RX, top, RW, LH, sw=2.8, seed=333)
    h2(b, RX + 30, top + 58, "Puntaje global de referencia", EDU_ORO, 28)
    b.append(T(RX + 30, top + 90, ["por carrera · rango aproximado reportado en 2026"], 19, GRAY, style="italic"))
    yy = top + 132
    for i, (nm, lo, hi) in enumerate(CARRERAS):
        if i % 2:
            b.append(rect(RX + 16, yy - 22, RW - 32, 34, "#F4F6FA", r=6))
        b.append(T(RX + 30, yy + 4, [nm], 20, INK))
        bx0, bx1 = RX + 360, RX + RW - 130

        def px(v):
            return bx0 + (bx1 - bx0) * (v - 250) / 250
        b.append(line(px(250), yy - 3, px(500), yy - 3, "#E6EAF0", 7))
        b.append(resaltador(px(lo), yy - 11, px(hi) - px(lo), 16, "#F2C36B", seed=i, rot=0))
        b.append(TX(RX + RW - 26, yy + 4, f"{lo}–{hi}", 18, GRAY, MONO, anchor="end"))
        yy += 34.5
    b.append(T(RX + 30, top + LH - 46, ["Son referencias de prensa, no cortes oficiales. Cada universidad fija el suyo:"],
               17, GRAY, style="italic"))
    b.append(T(RX + 30, top + LH - 22, ["confírmalo en la página de admisiones de la que tú quieres."], 17, GRAY,
               style="italic"))
    # mi cuenta
    y = top + LH + 26
    CH = 330
    caja(b, M, y, CW, CH, sw=2.8, seed=334)
    wmc = h2(b, M + 36, y + 56, "Mi cuenta", EDU_AZUL, 32, marca=True, fill=FOSFO)
    b.append(T(M + 60 + wmc, y + 54, ["— la escribes ahora y la vuelves a mirar después de cada simulacro"],
               21, GRAY, style="italic"))
    xx = M + 36
    for lab, w_ in [("La carrera que quiero", 560), ("En la universidad", 560), ("Puntaje que necesito", 340)]:
        b.append(T(xx, y + 110, [lab], 21, EDU_AZUL, weight="700"))
        b.append(line(xx, y + 156, xx + w_, y + 156, LGRAY, 2.6))
        xx += w_ + 60
    oy = y + 186
    cajas_ = [("Puntaje que necesito", EDU_AZUL), ("−", None), ("Mi puntaje hoy", EDU_ORO), ("=", None),
              ("Lo que me falta", EDU_ROJO), ("÷", None), ("Semanas que faltan", GRAY), ("=", None),
              ("Puntos por semana", EDU_VERDE)]
    xx, bw = M + 36, 290
    for lab, c in cajas_:
        if c is None:
            b.append(T(xx + 30, oy + 60, [lab], 46, TINTA_B, weight="700", anchor="middle"))
            xx += 60
        else:
            b.append(wob_rect(xx, oy, bw, 86, c, 3, fill="white", seed=int(xx)))
            b.append(T(xx + bw / 2, oy + 114, [lab], 18, c, weight="700", anchor="middle"))
            xx += bw + 10
    y += CH + 16
    mano(b, M + 20, y + 36, "Si el número de puntos por semana te asusta, bien: ya sabes cuánto vale cada sábado.",
         EDU_AZUL, 32, -0.5)
    y += 84
    # tablero de metas (WOOP)
    y = titulo(b, y, "Mi tablero de metas", marca="tablero", size=48, fill=FOSFO_2, seed=13, sub_size=22,
               sub="Imaginar el resultado no basta: la investigación de Gabriele Oettingen muestra que la meta se "
                   "mueve cuando también nombras tu obstáculo y decides el plan. Cuatro casillas, en este orden.")
    pw = (CW - 3 * 22) / 4
    ph = 440
    for i, (t, c, d, kind, mood) in enumerate(WOOP):
        x = M + i * (pw + 22)
        caja(b, x, y, pw, ph, c=c, sw=3, seed=340 + i)
        h2(b, x + 24, y + 46, t, c, 28)
        b.append(face(x + pw - 46, y + 40, 26, mood, c))
        yy = parrafo_j(b, x + 24, y + 66, d, pw - 48, 19, color=GRAY, lh=26)
        iy = max(yy + 10, y + 200)
        if kind == "lines":
            b.append(wlines(x + 24, iy + 34, pw - 48, int((y + ph - 30 - iy) // 46), c="#E3E8EF", step=46))
        elif kind == "draw":
            b.append(rect(x + 24, iy, pw - 48, y + ph - 24 - iy, "white", r=6, stroke="#E3E8EF", sw=2))
            mano(b, x + pw - 40, y + ph - 40, "dibuja aquí", c, 26, -2, anchor="end")
        else:
            for k in range(2):
                ky = iy + k * 120
                b.append(T(x + 24, ky + 30, ["Si"], 24, c, weight="700"))
                b.append(line(x + 60, ky + 34, x + pw - 24, ky + 34, "#CFD6E0", 2.4))
                b.append(T(x + 24, ky + 84, ["entonces yo"], 24, c, weight="700"))
                b.append(line(x + 150, ky + 88, x + pw - 24, ky + 88, "#CFD6E0", 2.4))
    y += ph + 22
    # puntaje por área
    PH = 2440 - y
    caja(b, M, y, CW, PH, sw=2.6, seed=350)
    h2(b, M + 30, y + 44, "Mi puntaje por área · hoy y meta", EDU_AZUL, 26)
    b.append(T(M + 36 + twf("Mi puntaje por área · hoy y meta", 26, SHA, "800"), y + 44,
               ["(de 0 a 100; lo llenas con tu primer simulacro)"], 19, GRAY, style="italic"))
    n_ar = len(AREAS)
    gw = (CW - 60 - (n_ar - 1) * 16) / n_ar
    cien = [i for i, (nm, _) in enumerate(AREAS) if nm in ("Biología", "Química", "Física")]
    cx0 = M + 30 + cien[0] * (gw + 16)
    cx1 = M + 30 + cien[-1] * (gw + 16) + gw
    b.append(T(cx1, y + 44, ["en la prueba son una sola: Ciencias Naturales"], 17, GRAY, style="italic",
               anchor="end"))
    for i, (nm, c) in enumerate(AREAS):
        x = M + 30 + i * (gw + 16)
        yy = y + 66
        hh = PH - 86
        b.append(wob_rect(x, yy, gw, hh, c, 2.4, fill="white", seed=360 + i, amp=1))
        b.append(rect(x, yy, 10, hh, c, r=0))
        nm_s = fit(nm, 19, None, "700", gw - 30)
        b.append(T(x + 22, yy + 30, [nm], nm_s, c, weight="700"))
        b.append(T(x + 22, yy + hh - 50, ["hoy"], 18, GRAY))
        b.append(line(x + 68, yy + hh - 46, x + gw - 14, yy + hh - 46, LGRAY, 2.4))
        b.append(T(x + 22, yy + hh - 12, ["meta"], 18, c, weight="700"))
        b.append(line(x + 68, yy + hh - 8, x + gw - 14, yy + hh - 8, c, 2.4))
    BT.pie_b(b, 3, EDU_ORO)
    return b


# ═════════════════════════════ 4 · ASÍ SE LEE UNA HOJA + LA ORGANIZACIÓN ═════════════════════════════
HOJA_MUESTRA = "bio2_t4"        # página 178 (antes 151: la de la propuesta de estilos)


def _anidar(ruta, x, y, w):
    s = open(ruta, encoding="utf-8").read()
    ini = s.index(">", s.index("<svg")) + 1
    cuerpo = s[ini:s.rindex("</svg>")]
    h = w * H_PAGE / W
    return (wob_rect(x - 4, y - 4, w + 8, h + 8, TINTA_B, 2.6, seed=501)
            + f'<svg x="{x}" y="{y}" width="{w}" height="{h:.1f}" viewBox="0 0 {W} {H_PAGE}">{cuerpo}</svg>'), h


PARTES = [  # (x, y del marcador en la hoja de verdad: al borde de la parte, sin taparla), título, texto  # TEXTO NUEVO
    (1930, 100, "La fecha y cómo llegas", "Antes de empezar marcas cómo llegas; al salir, cómo sales."),
    (1190, 110, "El área y la misión", "Qué misión es, qué componente del ICFES entrenas y qué preguntas trae la hoja."),
    (750, 262, "La pregunta no está reimpresa", "La lees en tu libro: la tarjeta te dice la página."),
    (1080, 222, "La estrategia", "El sello dice con qué estrategia se resuelve. Es la misma del profe."),
    (1900, 262, "Mi primera idea", "Lo que piensas antes de hacer nada. Después la comparas."),
    (70, 560, "El instrumento de pensamiento", "Cada pregunta trae el suyo. Aquí va todo: datos, tablas, flechas, tachones. Nada «en la cabeza»."),
    (70, 990, "Lo que subrayé", "Lo que encontraste en el texto o en el caso, con tus palabras."),
    (1930, 420, "Marco al final", "La letra es lo último. Y dices qué tan seguro estás: adiviné, casi, seguro."),
    (1930, 660, "Salvavidas", "Cuando te bloqueas: lo mínimo que sí tenías claro, qué tenía que ser y qué no podía ser."),
    (1930, 915, "Lo que me llevo", "Una frase que te sirva en otra pregunta parecida."),
    (70, 2370, "Palabras que me frenaron", "No las busques todavía: adivínalas por el contexto y confírmalas en clase."),
]
FASES = [("Activación", 15, "una tabla, una pregunta, cuaderno cerrado", EDU_AZUL),
         ("Pregunta problematizadora", 20, "el reto del momento: cada uno dice su hipótesis", EDU_ROJO),
         ("Desarrollo guiado", 35, "las preguntas del libro, con la estrategia", EDU_VERDE),
         ("Reto en equipo", 20, "una situación por equipo; registro individual", EDU_ORO),
         ("Evaluación individual", 20, "preguntas tipo Saber 11, en silencio", PSI),
         ("Cierre", 10, "lo que me llevo y cómo salgo", TEAL)]                                # TEXTO NUEVO (antes «bitácora y salvavidas»)
NIVELES = [("1", "Insuficiente", "Marco sin leer todo. Adivino.", EDU_ROJO),
           ("2", "Mínimo", "Entiendo la pregunta, pero no sé qué hacer con los datos.", EDU_ORO),
           ("3", "Satisfactorio", "Sé el camino y lo ejecuto hasta la respuesta.", EDU_VERDE),
           ("4", "Avanzado", "Puedo explicar por qué las otras opciones están mal.", EDU_AZUL)]


def hoja_y_areas():
    b = pagina()
    y = cabecera(b, "Qué te vas a encontrar", "así se lee una hoja · cómo está organizada cada área", EDU_VERDE)
    y = titulo(b, y + 10, "Así se lee una hoja", marca="una hoja", size=60,
               sub="Todas las hojas del cuaderno, en las siete áreas, tienen las mismas partes. Apréndetelas una vez.",
               sub_size=23)
    top = y + 6
    HX, HW = M + 4, 760
    s = HW / W
    frag, HH = _anidar(LIBRO + HOJA_MUESTRA + ".svg", HX, top, HW)
    b.append(frag)
    # leyenda numerada
    CX = HX + HW + 50
    CWd = W - M - CX
    yy = top + 6
    for k, (px_, py_, t, d) in enumerate(PARTES, 1):
        ax, ay = HX + px_ * s, top + py_ * s
        b.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="17" fill="{EDU_VERDE}" stroke="white" stroke-width="3"/>')
        b.append(TX(ax, ay + 6, str(k), 17, "white", MONO, "700", anchor="middle"))
        b.append(wob_circle(CX + 20, yy + 18, 19, EDU_VERDE, 2.4, seed=k, fill="white"))
        b.append(TX(CX + 20, yy + 25, str(k), 18, EDU_VERDE, MONO, "700", anchor="middle"))
        b.append(TX(CX + 56, yy + 26, t, 25, TINTA_B, SHA, "800"))
        lns = wrap_px(d, 20, CWd - 60)
        for j, ln in enumerate(lns):
            b.append(T(CX + 56, yy + 56 + j * 26, [" ".join(ln)], 20, INK))
        yy += 56 + (len(lns) - 1) * 26 + 22
    assert yy <= top + HH + 10, f"la leyenda baja hasta {yy:.0f} (hoja hasta {top + HH:.0f})"
    y = top + HH + 34
    # ─── la organización ───
    y = titulo(b, y, "Siete áreas, seis momentos, ocho clases", marca="ocho clases", size=46, fill=FOSFO_2,
               seed=14)
    # siete áreas
    n_ar = len(AREAS)
    gw = (CW - (n_ar - 1) * 14) / n_ar
    for i, (nm, c) in enumerate(AREAS):
        x = M + i * (gw + 14)
        b.append(wob_rect(x, y, gw, 74, c, 2.6, fill="white", seed=520 + i, amp=1))
        b.append(rect(x, y, 10, 74, c, r=0))
        b.append(TX(x + 30, y + 46, str(i + 1), 26, c, MONO, "700"))
        lns = [" ".join(l) for l in wrap_px(nm, 19, gw - 74, "700")]
        for j, ln in enumerate(lns):
            b.append(T(x + 62, y + 44 + (j - (len(lns) - 1) / 2) * 23, [ln], 19, c, weight="700"))
    b.append(T(M, y + 104, ["En el Saber 11, Biología, Química y Física se evalúan juntas en Ciencias Naturales; "
                            "aquí van por separado, como en tu libro."], 19, GRAY, style="italic"))   # TEXTO NUEVO
    y += 128
    # momento: 7 páginas
    MW = 860
    caja(b, M, y, MW, 300, c=EDU_AZUL, sw=2.8, seed=530)
    h2(b, M + 26, y + 44, "Cada área: 6 momentos", EDU_AZUL, 26)
    parrafo_j(b, M + 26, y + 60, "Un momento son 7 páginas: 5 de taller con las 10 preguntas de tu libro y 2 de "   # TEXTO NUEVO
              "entrenamiento con 4 preguntas Saber 11. Inglés trabaja todas las preguntas de su libro.",
              MW - 52, 19, color=GRAY, lh=26)
    seq = ["taller", "taller", "Saber 11", "taller", "taller", "taller", "Saber 11"]
    pw_ = (MW - 52 - 6 * 12) / 7
    for i, t in enumerate(seq):
        x = M + 26 + i * (pw_ + 12)
        c = EDU_AZUL if t == "taller" else EDU_ORO
        b.append(wob_rect(x, y + 150, pw_, 104, c, 2.4, fill="white", seed=540 + i, amp=0.8))
        b.append(TX(x + pw_ / 2, y + 222, t, 16 if t == "taller" else 15, c, MONO, "700", anchor="middle"))
        b.append(TX(x + pw_ / 2, y + 278, f"p. {i + 1}", 15, GRAY, MONO, anchor="middle"))
    # membrete
    mx = M + MW + 30
    mw = W - M - mx
    caja(b, mx, y, mw, 300, c=EDU_ORO, sw=2.8, seed=531)
    h2(b, mx + 26, y + 44, "El membrete de las de entrenar", EDU_ORO, 26)
    t = "Pregunta Saber 11"
    wt = twf(t, 20, MONO, "700") + 40
    b.append(rect(mx + 26, y + 70, wt, 46, "white", r=4, stroke=EDU_ORO, sw=2.6))
    b.append(rect(mx + 31, y + 75, wt - 10, 36, "none", r=2, stroke=EDU_ORO, sw=1.2))
    b.append(TX(mx + 46, y + 100, t, 20, EDU_ORO, MONO, "700"))
    parrafo_j(b, mx + 26, y + 140, "Cuando veas este membrete, la pregunta tiene la forma y el nivel del Saber 11. "
              "Es el formato de la prueba de verdad: lo entrenas aquí para que ese día nada te sorprenda.",
              mw - 52, 20, lh=28)
    y += 326
    # una clase por dentro
    CH = 316
    caja(b, M, y, CW, CH, c=EDU_VERDE, sw=2.8, seed=532)
    wt = h2(b, M + 26, y + 44, "Ocho clases de 120 minutos", EDU_VERDE, 26)
    b.append(T(M + 46 + wt, y + 44, ["clases 1 a 6: un momento cada una · clase 7: simulacro del área · "   # TEXTO NUEVO
                                     "clase 8: devolución"], 20, GRAY, style="italic"))
    bx, bw_t, by = M + 26, CW - 52, y + 70
    xx = bx
    for nm, mn, d, c in FASES:
        w_ = bw_t * mn / 120
        b.append(rect(xx, by, w_ - 6, 46, c, r=6))
        b.append(TX(xx + (w_ - 6) / 2, by + 31, f"{mn}'", 20, "white", MONO, "700", anchor="middle"))
        xx += w_
    xx = bx
    for k, (nm, mn, d, c) in enumerate(FASES):
        w_ = bw_t * mn / 120
        yy = by + 86 + (k % 2) * 92
        b.append(line(xx + 12, by + 46, xx + 12, yy - 8, c, 2, "5,5"))          # vertical: permitido
        b.append(f'<circle cx="{xx + 12}" cy="{yy - 8}" r="6" fill="{c}"/>')
        ult = k == len(FASES) - 1        # la última fase es angosta: su texto va hacia la izquierda
        xt, an = (xx + w_ - 6, "end") if ult else (xx + 26, "start")
        ancho = (2 * w_ if ult else w_ * (2 if k % 2 else 1)) - 40
        b.append(T(xt, yy, [nm], 20, c, weight="700", anchor=an))
        for j, ln in enumerate(wrap_px(d, 16, ancho)):
            b.append(T(xt, yy + 22 + j * 19, [" ".join(ln)], 16, INK, anchor=an))
        xx += w_
    y += CH + 26
    # niveles
    NH = 2440 - y
    caja(b, M, y, CW, NH, c=EDU_ORO, sw=2.8, seed=533)
    h2(b, M + 26, y + 44, "Cómo subes de nivel", EDU_ORO, 26)
    b.append(T(M + 46 + twf("Cómo subes de nivel", 26, SHA, "800"), y + 44,
               ["lo que el ICFES llama niveles de desempeño · cada hoja con andamiaje es un escalón"], 20, GRAY,
               style="italic"))
    sw_ = (CW - 52 - 3 * 16) / 4
    base = y + NH - 20
    for k, (n, nm, d, c) in enumerate(NIVELES):
        x = M + 26 + k * (sw_ + 16)
        h = 96 + k * 30
        b.append(wob_rect(x, base - h, sw_, h, c, 2.6, fill=tb_mezcla(c, 0.88), seed=560 + k, amp=1))
        b.append(T(x + 18, base - h + 32, [f"Nivel {n} · {nm}"], 21, c, weight="700"))
        for j, ln in enumerate(wrap_px(d, 17, sw_ - 36)):
            b.append(T(x + 18, base - h + 58 + j * 22, [" ".join(ln)], 17, INK))
    BT.pie_b(b, 4, EDU_VERDE)
    return b


def tb_mezcla(c, k):
    from taller_base import _mezcla
    return _mezcla(c, k)


# ═════════════════════════════ 5 · LO QUE PASA EN TU CABEZA ═════════════════════════════
ESTADOS = [
    ("Bloqueo", "«No entiendo nada.»", "Lee la pregunta otra vez, despacio, y subraya el único dato que sí entiendes. "
     "Empieza por ahí.", "worried", EDU_AZUL),
    ("Prisa", "«Ya sé, es la B.»", "Puede ser. Escribe un solo paso en el instrumento antes de marcar. Si el paso "   # TEXTO NUEVO («cuadrícula» → «instrumento»)
     "aguanta, marca.", "determined", EDU_ROJO),
    ("Pánico", "«No me va a dar el tiempo.»", "Salta la pregunta, márcala con una bandera y sigue. Vuelves al final. "
     "Una pregunta no vale el examen.", "surprised", EDU_ORO),
    ("Cansancio", "«Ya no más.»", "Cierra con la bitácora, no con una pregunta a medias. Dejar escrito dónde "
     "quedaste también es avanzar.", "tired", EDU_VERDE),
]


def cabeza():
    b = pagina()
    y = cabecera(b, "La psicología de la meta", "lo que pasa en tu cabeza antes de una pregunta difícil", PSI)
    y = titulo(b, y + 10, "Lo que pasa en tu cabeza", marca="tu cabeza", size=68,
               sub="Todos sentimos esto frente a una pregunta difícil. La diferencia no es sentirlo o no: es saber "
                   "qué hacer cuando llega.")
    top = y + 10
    cw_ = (CW - 3 * 30) / 4
    for i, (nm, frase, que, mood, c) in enumerate(ESTADOS):
        x = M + i * (cw_ + 30)
        caja(b, x, top, cw_, 590, c=c, sw=3, seed=600 + i)
        b.append(face(x + cw_ / 2, top + 110, 76, mood, c))
        b.append(TX(x + cw_ / 2, top + 236, nm, 36, c, SHA, "800", anchor="middle"))
        mano(b, x + cw_ / 2, top + 290, frase, PENCIL, 34, -1.5, anchor="middle")
        b.append(resaltador(x + 40, top + 334, twf("QUÉ HACER", 17, MONO, "700"), 22, FOSFO, seed=610 + i))
        b.append(TX(x + 40, top + 351, "QUÉ HACER", 17, TINTA_B, MONO, "700"))
        parrafo_j(b, x + 36, top + 376, que, cw_ - 72, 24, lh=35)
    y = top + 630
    caja(b, M, y, CW, 500, sw=3, seed=620)
    h2(b, M + 40, y + 62, "El error no es una nota. Es un dato.", EDU_AZUL, 38, marca=True, fill=FOSFO_2)
    parrafo_j(b, M + 40, y + 90, "Cuando te equivoques — y te vas a equivocar, para eso es el cuaderno — no borres. "
              "Deja el error a la vista y responde estas tres preguntas al lado, con lápiz. Con eso, el mismo error no "
              "vuelve dos veces.", CW - 80, 25, color=GRAY, lh=36)
    qs = [("¿Qué entendí mal?", "de la pregunta, del dato, de la gráfica"),
          ("¿En qué paso me desvié?", "mira el instrumento: ¿qué parte llenaste sin pensarla?"),   # TEXTO NUEVO (antes «el paso a paso»)
          ("¿Qué hago distinto la próxima vez?", "una sola cosa, concreta, que puedas repetir")]
    qw = (CW - 80 - 2 * 30) / 3
    for i, (q, d) in enumerate(qs):
        x = M + 40 + i * (qw + 30)
        yy = y + 210
        b.append(wob_rect(x, yy, qw, 250, EDU_AZUL, 2.4, fill="white", seed=630 + i))
        num(b, x + 46, yy + 50, i + 1, EDU_AZUL, r=26, size=22, seed=i + 40)
        for j, ln in enumerate(wrap_px(q, 25, qw - 110, "700")):
            b.append(T(x + 90, yy + 58 + j * 30, [" ".join(ln)], 25, EDU_AZUL, weight="700"))
        for j, ln in enumerate(wrap_px(d, 23, qw - 60, "400", "italic")):
            b.append(T(x + 30, yy + 150 + j * 30, [" ".join(ln)], 23, GRAY, style="italic"))
    y += 550
    h2(b, M, y + 44, "Tres micro-hábitos del sábado", PSI, 38, marca=True, fill=FOSFO)
    y += 80
    hab = [("ANTES", "Desayuna. Trae el libro y dos lápices. Lee la bitácora del sábado pasado: ahí dejaste "
            "escrito por dónde seguir.", EDU_ORO),
           ("DURANTE", "Escribe antes de marcar. Pide el Salvavidas cuando lo necesites, no cuando ya se acabó el "
            "tiempo.", EDU_AZUL),
           ("DESPUÉS", "Cuéntale a alguien — en casa, en el bus — una cosa que aprendiste hoy. Si no la puedes "
            "explicar, no la aprendiste todavía.", EDU_VERDE)]
    hw = (CW - 2 * 30) / 3
    for i, (t, d, c) in enumerate(hab):
        x = M + i * (hw + 30)
        caja(b, x, y, hw, 330, c=c, sw=3, seed=640 + i)
        BT.sello_mono(b, x + 30, y + 30, t, c, size=24, h=54, pad=20, ang=(-2, 1.5, -1)[i])
        parrafo_j(b, x + 30, y + 120, d, hw - 60, 26, lh=37)
    # lo que me pasa a mí (se escribe)                                                      # TEXTO NUEVO
    y += 360
    caja(b, M, y, CW, 2440 - y, c=PSI, sw=3, seed=650)
    wt = h2(b, M + 36, y + 54, "Lo que me pasa a mí", PSI, 32, marca=True, fill=FOSFO_2, seed=651)
    b.append(T(M + 60 + wt, y + 52, ["marca el que más te llega y escribe qué vas a hacer la próxima vez"], 22,
               GRAY, style="italic"))
    xx = M + 36
    for i, (nm, _, _, _, c) in enumerate(ESTADOS):
        b.append(wob_rect(xx, y + 86, 26, 26, c, 2.4, fill="white", seed=660 + i, amp=0.7))
        b.append(T(xx + 40, y + 108, [nm], 25, c, weight="700"))
        xx += 40 + tw(nm, 25, "700") + 60
    b.append(T(M + 36, y + 168, ["La próxima vez que llegue, yo voy a"], 23, INK))
    b.append(line(M + 36 + tw("La próxima vez que llegue, yo voy a", 23) + 14, y + 172, W - M - 36, y + 172, LGRAY, 2.4))
    b.append(wlines(M + 36, y + 226, CW - 72, max(1, int((2440 - y - 236) // 54) + 1), c=LGRAY, step=54))
    BT.pie_b(b, 5, PSI)
    return b


# ═════════════════════════════ 6 · CÓMO LEER ESTE CUADERNO (coordinación) ═════════════════════════════
def coordinacion():
    b = pagina()
    y = cabecera(b, "Para la coordinación", "cómo leer este cuaderno sin entrar al salón", PSI)
    y = titulo(b, y + 10, "Cómo leer este cuaderno", marca="leer", size=68,
               sub="Esta hoja es para el coordinador. El cuaderno está hecho para que la calidad de la clase se "
                   "pueda auditar desde el papel: tres cuadernos al azar dicen más que una visita al salón.")
    top = y + 10
    caja(b, M, top, CW, 590, c=PSI, sw=3, seed=700)
    h2(b, M + 40, top + 60, "Qué mirar en tres cuadernos al azar", PSI, 34)
    checks = [("El instrumento está escrito antes de la letra marcada", "es la señal de que el método se está usando"),   # TEXTO NUEVO («la cuadrícula» → «el instrumento»)
              ("La bitácora de cada clase está llena", "es la única parte que el estudiante escribe sobre sí mismo"),
              ("Hay errores a la vista, sin borrar, con las tres preguntas al lado",
               "el cuaderno enseña por el error, no a pesar de él"),
              ("El Salvavidas se usó en algunas hojas", "usarlo es buena señal: pidió ayuda a tiempo"),
              (f"El tablero de metas (página {P_METAS}) tiene un obstáculo que depende del estudiante",       # TEXTO NUEVO (antes «hoja 5»)
               "si el obstáculo es «el profe», la meta está fuera de su control")]
    for i, (t, d) in enumerate(checks):
        yy = top + 126 + i * 90
        b.append(wob_rect(M + 44, yy - 26, 30, 30, PSI, 2.4, fill="white", seed=710 + i, amp=0.7))
        b.append(T(M + 96, yy, [t], 28, INK, weight="700"))
        b.append(T(M + 96, yy + 34, [d], 23, GRAY, style="italic"))
    y = top + 630
    h2(b, M, y + 44, "Señales y qué hacer con ellas", PSI, 34, marca=True, fill=FOSFO_2)
    y += 76
    cols = [("Señal", 600), ("Qué suele significar", 600), ("Qué hacer", CW - 1200)]
    rows = [("Respuesta correcta, instrumento vacío", "Copió o adivinó. El acierto no es suyo todavía.",       # TEXTO NUEVO («cuadrícula» → «instrumento»)
             "Conversación con el estudiante, no sanción. «Muéstrame cómo llegaste».", EDU_ROJO),
            ("Bitácora en blanco varias clases", "El cierre de la clase no se está haciendo.",
             "Hablar con el profesor, no con el estudiante: el cierre lo dirige él.", EDU_ORO),
            ("Muchas hojas con Salvavidas", "Pide ayuda a tiempo. No es alerta.",
             "Revisar en qué estrategia se repite: ahí está el refuerzo que necesita.", EDU_VERDE),
            ("Obstáculo del tablero = «el profe», «el colegio»", "La meta está puesta fuera de su alcance.",
             "Rehacer la casilla 3 con él: el obstáculo tiene que estar en lo que él controla.", PSI),
            (f"Puntaje «hoy» sin escribir en la página {P_METAS}", "No ha hecho el primer simulacro.",            # TEXTO NUEVO (antes «hoja 4»)
             "Agendar el simulacro. Sin número no hay meta que entrenar.", EDU_AZUL)]
    caja(b, M, y, CW, 64 + 5 * 150 + 10, sw=2.8, seed=720)
    x = M
    for t, w_ in cols:
        b.append(resaltador(x + 24, y + 20, twf(t.upper(), 18, MONO, "700"), 26, FOSFO, seed=int(x)))
        b.append(TX(x + 24, y + 40, t.upper(), 18, TINTA_B, MONO, "700"))
        x += w_
    y += 64
    for i, (s1, s2, s3, c) in enumerate(rows):
        rh = 150
        if i % 2:
            b.append(rect(M + 4, y, CW - 8, rh, "#F4F6FA", r=0))
        b.append(rect(M + 14, y + 14, 10, rh - 28, c, r=5))
        for k, (txt, w_) in enumerate(zip((s1, s2, s3), [cc[1] for cc in cols])):
            x = M + sum(cc[1] for cc in cols[:k])
            for j, ln in enumerate(wrap_px(txt, 25, w_ - 56, "700" if k == 0 else "400")):
                b.append(T(x + 40 if k == 0 else x + 24, y + 48 + j * 34, [" ".join(ln)], 25, c if k == 0 else INK,
                           weight="700" if k == 0 else "400"))
        y += rh
    y += 50
    hw = (CW - 40) / 2
    for k, (t, c, items) in enumerate([
            ("Cómo hablar de la meta con él", EDU_VERDE,
             ["No: «¿cuánto sacaste?»  Sí: «¿en qué paso te perdiste?»",
              "No: «¿por qué te fue mal?»  Sí: «¿qué dejaste escrito que sí servía?»",
              "No: «tienes que estudiar más.»  Sí: «¿qué vas a hacer distinto el sábado?»",
              "Pregunta por la bitácora, no por la nota. La nota ya la sabe."]),
            ("Lo que no se hace", EDU_ROJO,
             ["Castigar el error. El cuaderno lo necesita a la vista para enseñar.",
              "Comparar cuadernos en voz alta. Se comparan con el propio de hace un mes.",
              "Llenar la bitácora por él «para que quede completa». Vacía dice más que falsa.",
              "Mover la meta sin él. La meta se renegocia con el estudiante, no se le impone."])]):
        x = M + k * (hw + 40)
        ph = 2440 - y
        caja(b, x, y, hw, ph, c=c, sw=3, seed=730 + k)
        h2(b, x + 30, y + 58, t, c, 32)
        vinetas(b, x + 34, y + 124, items, hw - 70, 27, c, lh=38, gap=22)
    BT.pie_b(b, 6, PSI, texto="Cuaderno de trabajo · Saber 11 · hoja para la coordinación")
    return b


PAGINAS = [portada, intro, metas, hoja_y_areas, cabeza, coordinacion]


def construir():
    rutas = []
    for k, f in enumerate(PAGINAS, 1):
        b = f()
        r = LIBRO + f"ap_b_{k}.svg"
        svg_close(b, r)
        rutas.append(r)
    return rutas


if __name__ == "__main__":
    import render
    rutas = construir()
    os.makedirs("/tmp/claude-0/apertura_b", exist_ok=True)
    pdf = render.unir(rutas, "/tmp/claude-0/apertura_b/Apertura_B.pdf")
    print(pdf, render.verifica(pdf, "Aprende"))
