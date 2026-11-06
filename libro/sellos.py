#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Criterio de rotulación: cómo se marca cada pregunta según lo que sabemos de ella."""
import math, random
from lib import *

random.seed(5)
OUT = "/home/claude/libro/"
AZm = "#1F4E8C"; AZm_L = "#C3D7EA"; AZm_BG = "#EFF4FA"
ORO_D = "#8A5A0B"


def sello_icfes(b, x, y, txt, size=19):
    """Membrete oficial. Mismo diseño con año o sin año: solo cambia lo que dice."""
    w = len(txt) * (size * 0.60) + 60
    b.append(rect(x, y, w, 44, "white", r=10, stroke=AZ_D, sw=2.2))
    b.append(rect(x, y, 14, 44, AZ_D, r=7))
    b.append(T(x + 30, y + 29, [txt], size, AZ_D, weight="700"))
    return w


def sello_educate(b, x, y, txt="Entrenamiento EDUCATE · tipo Saber 11", size=18):
    """Para preguntas construidas o adaptadas por el equipo, no tomadas de una prueba."""
    w = len(txt) * (size * 0.60) + 90
    b.append(rect(x, y, w, 42, AMBER_BG, r=21, stroke=EDU_ORO, sw=2.2, dash="7,5"))
    b.append(diana(x + 27, y + 21, 12, ORO_D))
    b.append(T(x + 52, y + 28, [txt], size, ORO_D, weight="700"))
    return w


def ficha(b, x, y, w, h, color, titulo_, sello_fn, lineas, pie):
    panel(b, x, y, w, h, color, title=titulo_, title_size=24)
    sello_fn(b, x + 34, y + 82)
    yy = y + 164
    for lab, txt in lineas:
        b.append(T(x + 34, yy + 22, [lab], 19, color, weight="700", ls=1))
        yy = parrafo_j(b, x + 34, yy + 32, txt, w - 68, 26, lh=38) + 24
    b.append(rect(x + 24, y + h - 92, w - 48, 66, color, r=14, op=0.10))
    b.append(T(x + 44, y + h - 52, [pie], 23, color, weight="700"))


def pagina():
    b = svg_open()
    y = frame(b, "Criterio de rotulación", AZm, 0, "qué puede decir el membrete de cada pregunta")
    y = titulo(b, y + 16, "El año es una afirmación, no un adorno", AZm,
               sub="Decir «pregunta del ICFES» es algo que sabemos y podemos sostener. Decir «2023 · Cuadernillo 1 · "
                   "N.º 45» es una dirección exacta que cualquiera puede ir a verificar. Por eso el año solo aparece "
                   "cuando lo tenemos confirmado, y su ausencia no le quita nada a la pregunta.")
    top = y + 26
    cw = (CW - 44) / 2
    PH = 780

    ficha(b, M, top, cw, PH, AZm, "Con año · verificada",
          lambda bb, xx, yy: sello_icfes(bb, xx, yy, "Saber 11 · 2019 · Cuadernillo 2 · N.º 46"),
          [("QUÉ AFIRMA", "Que la pregunta salió de esa prueba, ese cuadernillo y ese número. Es una dirección "
                          "exacta."),
           ("CUÁNDO SE USA", "Solo cuando está confirmada una por una contra el cuadernillo liberado del ICFES."),
           ("QUÉ PUEDE HACER EL ESTUDIANTE", "Ir a buscarla y comprobar que existe.")],
          "Lo que hace que el cuaderno se sienta serio.")

    x2 = M + cw + 44
    ficha(b, x2, top, cw, PH, AZ_M, "Sin año · origen ICFES",
          lambda bb, xx, yy: sello_icfes(bb, xx, yy, "Pregunta oficial ICFES · Saber 11"),
          [("QUÉ AFIRMA", "Que la pregunta viene de una prueba del ICFES. Nada más, y nada menos: eso es "
                          "exactamente lo que sabemos de tu banco."),
           ("CUÁNDO SE USA", "Preguntas reales cuyo año y cuadernillo se perdieron y todavía no hemos podido "
                             "recuperar."),
           ("QUÉ PUEDE HACER EL ESTUDIANTE", "Entrenar con una pregunta real. No se le promete una dirección "
                                             "que no tenemos, así que nada se puede desmentir.")],
          "Se ve sobrio, no incompleto.")

    # franja: el tercer caso
    y2 = top + PH + 46
    b.append(rect(M, y2, CW, 176, AMBER_BG, r=22, stroke=EDU_ORO, sw=2.4))
    sello_educate(b, M + 36, y2 + 34)
    parrafo_j(b, M + 36, y2 + 92, "Solo para preguntas que el equipo construyó o adaptó, no tomadas de una prueba. "
              "Si tu banco es todo del ICFES, este sello no aparece en el cuaderno.", CW - 72, 25, lh=36)

    # lo que no se hace
    y3 = y2 + 226
    b.append(rect(M, y3, CW, 330, "white", r=26, stroke=EDU_ROJO, sw=3))
    b.append(rect(M, y3, 24, 330, EDU_ROJO, r=12))
    b.append(T(M + 70, y3 + 58, ["Lo único que no se puede hacer"], 34, EDU_ROJO, weight="700"))
    sx, sy = M + 70, y3 + 90
    w_ = sello_icfes(b, sx, sy, "Saber 11 · 2023 · Cuadernillo 1 · N.º 45")
    b.append(rect(sx, sy, w_, 44, "#FFFFFF", r=10, op=0.55))
    b.append(spath([(sx + 10, sy + 6), (sx + w_ - 10, sy + 38)], EDU_ROJO, 5))
    b.append(spath([(sx + w_ - 10, sy + 6), (sx + 10, sy + 38)], EDU_ROJO, 5))
    b.append(PT(sx + w_ + 40, sy + 36, ["un año puesto al azar"], 30, EDU_ROJO, rot=-2))
    parrafo_j(b, M + 70, y3 + 156, "El ICFES publica los cuadernillos liberados. Si el año es inventado, un "
              "profesor, un colegio o un competidor lo comprueba en un minuto, y el que responde por el material "
              "es quien lo firma. Además, el cuaderno le promete al estudiante que ese membrete se puede "
              "verificar: inventarlo una vez quita el valor a todos los demás.", CW - 140, 26, lh=38)

    # qué sigue
    y4 = y3 + 386
    b.append(T(M, y4 + 40, ["Qué sigue con tu banco"], 34, AZm, weight="700"))
    y4 += 72
    pasos = [("Me lo pasas como esté", "Texto, PDF, Word o fotos. No hace falta ordenarlo antes.", AZm),
             ("Cruzo una por una", "Comparo cada enunciado contra los cuadernillos liberados y recupero el año "
                                   "real de las que aparezcan.", EDU_VERDE),
             ("Cada una con lo que sabemos", "Las recuperadas, con año. Las demás, «Pregunta oficial ICFES». "
                                             "Todas entran: ninguna se queda por fuera.", EDU_ORO)]
    pw = (CW - 2 * 30) / 3
    for i, (t, d, c) in enumerate(pasos):
        x = M + i * (pw + 30)
        b.append(rect(x, y4, pw, 330, "white", r=22, stroke=c, sw=2.6))
        b.append(num_badge(x + 44, y4 + 48, i + 1, c, r=27, size=27))
        b.append(T(x + 86, y4 + 58, [t], 24, c, weight="700"))
        parrafo_j(b, x + 30, y4 + 96, d, pw - 60, 26, lh=38)
        if i < 2:
            b.append(hand_arrow(x + pw + 4, y4 + 165, x + pw + 26, y4 + 165, EDU_ORO, sw=3, bend=0, head=14))
    b.append(PT(M, y4 + 420, ["Ninguna pregunta de tu banco se pierde. Lo único que cambia es cuánto nos atrevemos a afirmar de cada una."],
                34, AZm, rot=-0.6))
    footer(b, "", AZm, texto="Criterio de rotulación · uso interno EDUCATE")
    svg_close(b, OUT + "sellos.svg")


if __name__ == "__main__":
    pagina()
    print("ok sellos")
