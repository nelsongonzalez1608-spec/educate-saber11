#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 2 · entrenamiento ICFES · páginas 284 y 288.

Fuente de las cuatro: «Cuadernillo de preguntas · Prueba Inglés · Saber 11.º» (Icfes, septiembre
de 2024; fuente_icfes/16-octubre-cuadernillo-ingles-saber-11-2024.pdf), Parte 3 («Complete las
conversaciones», A–C) de los dos exámenes, preguntas «utilizadas en aplicaciones anteriores».
Verificadas contra las páginas 8 y 16 del cuadernillo y su tabla de respuestas (páginas 23 y 24).
Ninguna estaba en tablero/icfes.csv; reservadas en tablero/propuestas/ing_icfes_reservas.csv.

OJO con la numeración del Examen 1: la página 8 dice «responde las preguntas 7 y 8», pero las
imprime como «6.» (Grandma) y «7.» (umbrella); la 6 real es un aviso de la Parte 2. La tabla de
respuestas va con la numeración correcta: 7 · C y 8 · B. Registrado como hallazgo.

Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano; coinciden con la tabla del cuadernillo):

    QA · Examen 1 · 8 · B   («How much is that umbrella?» → 50 dollars.)          estrategia 1
    QB · Examen 1 · 7 · C   («Grandma, shall I hold those bags for you?» → That's fine.)
                                                                                    estrategia 2
    QC · Examen 2 · 9 · C   («It rained a lot last night!» → Did you sleep?)        estrategia 3
    QD · Examen 2 · 7 · B   («I can't eat a cold sandwich. It is horrible!» → I agree.)
                                                                                    estrategia 4

  E1 · 8 · B: «How much…?» pide un precio. «Anything else?» lo dice el vendedor, no quien
       pregunta; «Cash only!» dice cómo pagar, no cuánto.
  E2 · 7 · C: «Shall I…?» es un OFRECIMIENTO de ayuda. La abuela contesta aceptando con
       amabilidad («That's fine», está bien). «I'm not afraid» y «Where are you?» no le
       contestan al ofrecimiento. Con reserva menor: «That's fine» también puede leerse como
       «no hace falta»; las dos lecturas responden al ofrecimiento.
  E3 · 9 · C: llovió mucho ANOCHE (pasado) → la pregunta natural es por esa noche: «Did you
       sleep?» (la lluvia hace ruido). «Did you accept?» y «Did you understand?» no tienen nada
       que ver con la lluvia.
  E4 · 7 · B: la persona da una opinión fuerte (un sándwich frío es horrible): se reacciona
       dándole la razón o no. «I agree». «I hope so» es para un deseo; «I am not» no responde a
       nada: nadie preguntó qué eres o cómo estás.
"""
from ing2 import *   # noqa: F401,F403  (configura la misión y EST)
from ing2 import rot, caja, pista, renglon, texto, tinte, flecha, sino

FUENTE = "Cuadernillo de preguntas · Prueba Inglés · Saber 11.º (Icfes, 2024)"


def conversa(frase):
    """El globo de quien habla, tal cual en el cuadernillo, y el globo vacío de la respuesta."""
    def datos(b, x, y, w):
        bw = tw(frase, 22, "700") + 60
        b.append(rect(x + 40, y + 8, bw, 60, "#F3F4F6", r=24, stroke="#9AA1AD", sw=1.8))
        texto(b, x + 70, y + 46, frase, size=22, weight="700")
        b.append(rect(x + w - 300, y + 80, 260, 50, "white", r=22, stroke="#9AA1AD", sw=1.8, dash="6,6"))
        texto(b, x + w - 170, y + 112, "?", size=22, color=GRAY, weight="700", anchor="middle")
        return y + 140
    return datos


# ───────── QA · How much is that umbrella? ─────────
def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "How + una palabra: qué dato me piden", c,
                      "Como con «Is this…?» y «Does this…?»: la primera palabra dice qué respuesta espera. Completa "
                      "la tabla y busca en las opciones el dato que pide «How much».")
    x0, ww = x + 22, w - 44
    cols = (250, 360, ww - 610)
    return tabla_vacia(b, x0, yy, cols, ("LA PREGUNTA", "PIDE…", "UN EJEMPLO DE RESPUESTA"),
                       ("How much…?", "How many…?", "How old…?", "How long…?"), c, rh=50, hh=40)


# ───────── QB · Grandma, shall I hold those bags…? ─────────
def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Me ofrecen ayuda: acepto o la rechazo con amabilidad", c,
                      "Como con «Could you print…?»: primero decide qué hace la frase. «Shall I…?» no pide un favor: "
                      "lo ofrece. Escribe cómo contestaría la abuela en cada caso.")
    x0, ww = x + 22, w - 44
    pista(b, x0, yy + 20, "Shall I hold those bags for you? quiere decir:")
    renglon(b, x0 + 320, yy + 22, x0 + ww)
    yy += 40
    half = (ww - 30) / 2
    for k, tit in enumerate(("SI LA ABUELA ACEPTA…", "SI LA RECHAZA CON AMABILIDAD…")):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 110, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c)
        pista(b, bx + 18, yy + 56, "en inglés:")
        renglon(b, bx + 18, yy + 92, bx + half - 18)
    return yy + 110


# ───────── QC · It rained a lot last night! ─────────
def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Anoche llovió: ¿qué preguntaría yo?", c,
                      "Como con «last night» en la pregunta 8: la marca de tiempo manda. Sigue la cadena desde lo que "
                      "pasó hasta la pregunta que tú harías.")
    x0, ww = x + 22, w - 44
    pasos = (("LO QUE PASÓ", "rained es el pasado de:"),
             ("A QUIEN ESTABA EN CASA…", "¿qué le pudo pasar esa noche?"),
             ("YO LE PREGUNTARÍA…", "en inglés: Did you ___ ?"))
    pw = (ww - 2 * 40) / 3
    for k, (tit, ps) in enumerate(pasos):
        bx = x0 + k * (pw + 40)
        caja(b, bx, yy, pw, 120, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c)
        pista(b, bx + 18, yy + 58, ps)
        renglon(b, bx + 18, yy + 100, bx + pw - 18)
        if k < 2:
            flecha(b, bx + pw + 4, yy + 60, bx + pw + 36, yy + 60, c, head=9)
    return yy + 120


# ───────── QD · I can't eat a cold sandwich ─────────
def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Una queja fuerte: ¿la comparto?", c,
                      "Como con el consejo del médico: aquí no te preguntan nada, te dan una opinión. Decide si la "
                      "compartes y escribe cómo lo dirías.")
    x0, ww = x + 22, w - 44
    pista(b, x0, yy + 20, "horrible significa:")
    renglon(b, x0 + 140, yy + 22, x0 + 460)
    pista(b, x0 + 490, yy + 20, "¿la persona pregunta algo?")
    sino(b, x0 + 690, yy + 4, c)
    yy += 40
    half = (ww - 30) / 2
    for k, tit in enumerate(("SI PIENSO IGUAL, DIGO…", "SI NO PIENSO IGUAL, DIGO…")):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 110, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c)
        pista(b, bx + 18, yy + 56, "en inglés:")
        renglon(b, bx + 18, yy + 92, bx + half - 18)
    return yy + 110


CONV = "Complete la conversación."

QA = dict(est=1, comp="Pragmático · Parte 3", e=CONV, o=["Anything else?", "50 dollars.", "Cash only!"],
          datos=conversa("How much is that umbrella?"), inst=ii1)
QB = dict(est=2, comp="Pragmático · Parte 3", e=CONV, o=["I'm not afraid!", "Where are you?", "That's fine."],
          datos=conversa("Grandma, shall I hold those bags for you?"), inst=ii2)
QC = dict(est=3, comp="Pragmático · Parte 3", e=CONV,
          o=["Did you accept?", "Did you understand?", "Did you sleep?"],
          datos=conversa("It rained a lot last night!"), inst=ii3)
QD = dict(est=4, comp="Pragmático · Parte 3", e=CONV, o=["I hope so.", "I agree.", "I am not."],
          datos=conversa("I can't eat a cold sandwich. It is horrible!"), inst=ii4)


def build(pages=(284, 288)):
    return [hoja_icfes("ing2_i1", pages[0], QA, QB),
            hoja_icfes("ing2_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
