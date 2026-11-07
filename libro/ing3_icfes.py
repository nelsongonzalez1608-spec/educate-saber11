#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 3 · entrenamiento ICFES · páginas 285 y 289.

Las cuatro salen del cuadernillo oficial «Prueba Inglés · Cuadernillo de preguntas · Saber 11.º»
(Icfes, septiembre de 2024; fuente_icfes/16-octubre-cuadernillo-ingles-saber-11-2024.pdf), que
trae dos exámenes de 25 preguntas cada uno, ya aplicados. Verificadas contra la página del
cuadernillo y resueltas a mano; la tabla de respuestas del final del cuadernillo coincide.
Ninguna estaba en tablero/icfes.csv; reservadas en tablero/propuestas/ing_icfes_reservas.csv.
Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Los textos de la Parte 4 y la Parte 7 son largos y traen varios espacios: cada tarjeta imprime
el párrafo donde está su espacio (con los demás espacios numerados, como en el original). El
texto completo está en tablero/propuestas/ing3_textos.md para el profe.

Claves verificadas:

    QA · Examen 1 · 10 (Parte 4, «Coffee», p. 9)          · C since      estrategia 1
    QB · Examen 1 · 13 (Parte 4, «Coffee», p. 9)          · B described  estrategia 2
    QC · Examen 2 · 24 (Parte 7, «Valentine's Day», p. 22) · D out        estrategia 3
    QD · Examen 1 · 16 (Parte 4, «Coffee», p. 9)          · A While      estrategia 4

  10 · since: «has been well-known» (presente perfecto) une un punto de inicio (the beginning of
       the 14th century) con hoy. during pide un periodo, until un punto final.
  13 · described: «was first ___ by Ferdinand Runge» es voz pasiva: was + participio + by.
       describe (base) y describes (presente) no caben después de was.
  24 · out: «found out» = se enteró (descubrió las bodas secretas). found off / in / at no existen
       con ese sentido.
  16 · While: contraste dentro de la misma oración (mucha gente cree que es malo / los estudios
       muestran que es bueno). Because pone una causa ilógica; Except no introduce una oración.
"""
from ing3 import *   # noqa: F401,F403  (configura la misión y EST)
from ing3 import rot, caja, pista, renglon, texto, tinte, flecha, marca, frase_hueco

F = "Pregunta oficial ICFES · Saber 11"
INSTR = "Lea el texto de la parte inferior y seleccione la palabra correcta para cada espacio."


def fragmento(titulo, parrafos, espacio, nota="fragmento del texto; el profe tiene el texto completo"):
    """El texto del cuadernillo en un recuadro, en tinta, y el número del espacio que se responde."""
    def _d(b, x, y, w):
        yy = y + 6
        alto = []
        g = []
        g.append(T(x + 24, yy + 34, [titulo], 19, INK, weight="700"))
        yi = yy + 44
        for p in parrafos:
            svg, yi = TJ(x + 24, yi, p, w - 48, 19, INK, lh=27)
            g.append(svg)
            yi += 6
        g.append(T(x + w - 24, yi + 14, [f"({nota})"], 14, GRAY, style="italic", anchor="end"))
        h = yi + 26 - yy
        b.append(rect(x, yy, w, h, "#F7F8FA", r=12, stroke="#C9CED6", sw=1.6))
        b.extend(g)
        yy += h + 8
        b.append(T(x, yy + 22, [f"Espacio ({espacio}):"], 20, INK, weight="700"))
        return yy + 26
    return _d


COFFEE_2 = ("Coffee has been well-known (10) ________ the beginning of the 14th century, (11) ________ Sufi "
            "Yemenis started using coffee to stay alert during special activities. It became a popular medicine "
            "(12) ________ Europeans in the 1600s.")
COFFEE_3 = ("Caffeine was first (13) ________ in the 1800s by Ferdinand Runge, a doctor that found out some effects "
            "of coffee on people.")
COFFEE_4 = ("Some people say (14) ________ coffee isn't good, but doctors say you (15) ________ believe this. Thanks "
            "to caffeine you don't get hungry. Coffee can also reduce headaches and blood problems. (16) ________ "
            "many people believe coffee is bad, studies show it is good for your heart.")
VALENTINE_2 = ("One of the (23) ________ says that the original Valentine was a priest. It is said that the king, "
               "Claudius II, had forbidden marriage because he thought that only unmarried men made the best "
               "soldiers. However, Valentine continued to hold weddings for a lot of young couples in secret. When "
               "the King found (24) ________, he ordered soldiers to kill Valentine!")


# ───────── QA · Examen 1 · 10 · since ─────────
def ii1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Desde cuándo y hasta cuándo: el reloj del café", c,
                      "«Has been» no es un pasado cualquiera. Dibuja en la línea dónde empieza y hasta dónde llega lo "
                      "que dice la oración, y marca qué tiempo es.")
    x0, ww = x + 22, w - 44
    ly = yy + 44
    b.append(line(x0 + 10, ly, x0 + ww - 10, ly, c, 4))
    for k, lab in enumerate(("siglo XIV", "1600", "1800", "HOY")):
        px = x0 + 80 + k * (ww - 160) / 3
        b.append(line(px, ly - 14, px, ly + 14, c, 3))
        texto(b, px, ly - 22, lab, size=16, color=c, weight="700", anchor="middle")
    pista(b, x0 + 10, ly + 40, "Pinta la flecha de «has been well-known»: ¿dónde arranca? ¿hasta dónde llega?")
    yy = ly + 60
    for k, lab in enumerate(("es un periodo cerrado, con principio y fin en el pasado",
                             "llega hasta un punto final y ahí se detiene",
                             "arranca en un punto y sigue hasta hoy")):
        marca(b, x0 + 20, yy + k * 36, c, lab, size=16)
    yy += 3 * 36 + 8
    return alto_profe(b, x0, yy, ww,
                      "«Has been» es presente perfecto: has o have más la tercera cara del verbo. Pídele al profe que "
                      "lo dibuje en una línea de tiempo y lo compare con «was», que también es pasado.")


# ───────── QB · Examen 1 · 13 · described ─────────
def ii2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La oración al revés: Runge y la cafeína", c,
                      "La cafeína no hizo nada: alguien hizo algo con ella. Pon cada pieza de la oración en su bloque y "
                      "escribe debajo qué papel cumple. El bloque vacío pide una de las tres caras del verbo.")
    x0, ww = x + 22, w - 44
    piezas = (("Caffeine", 240), ("was first", 220), ("(13) ______", 260), ("by Ferdinand Runge", ww - 3 * 16 - 720))
    bx = x0
    for k, (p, pw) in enumerate(piezas):
        caja(b, bx, yy, pw, 58, c, sw=2.4, r=12, fill=("white" if k == 2 else tinte(c, 0.92)))
        texto(b, bx + pw / 2, yy + 37, p, size=19, weight="700", anchor="middle")
        renglon(b, bx + 14, yy + 104, bx + pw - 14)
        bx += pw + 16
    pista(b, x0, yy + 134, "papeles: lo que recibe la acción · el auxiliar · el verbo · quién la hizo")
    yy += 154
    return frase_hueco(b, x0, yy, ww, "Al derecho: Ferdinand Runge ______________ caffeine. Con «was» delante va la cara ___ .", c)


# ───────── QC · Examen 2 · 24 · found out ─────────
def ii3(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El verbo que cambia de sentido con su partícula", c,
                      "«Find» solo es encontrar. Con una partícula pegada cambia de sentido. Lee la historia: ¿qué le "
                      "pasó al rey? Escribe lo que hizo en español y después busca la pieza inglesa que dice eso.")
    x0, ww = x + 22, w - 44
    hw = (ww - 24) / 2
    caja(b, x0, yy, hw, 110, c, r=14)
    rot(b, x0 + 20, yy + 30, "EN LA HISTORIA, EL REY…", c, size=14)
    pista(b, x0 + 20, yy + 56, "con mis palabras, qué le pasó con las bodas secretas:")
    renglon(b, x0 + 20, yy + 94, x0 + hw - 20)
    bx = x0 + hw + 24
    caja(b, bx, yy, hw, 110, c, r=14)
    rot(b, bx + 20, yy + 30, "LA PIEZA COMPLETA", c, size=14)
    texto(b, bx + 20, yy + 80, "found", size=22, weight="700")
    b.append(rect(bx + 92, yy + 50, 110, 44, "white", r=8, stroke=c, sw=2.2))
    pista(b, bx + 222, yy + 80, "= en español:")
    renglon(b, bx + 330, yy + 82, bx + hw - 20)
    yy += 128
    rot(b, x0, yy + 18, "OTRAS PIEZAS QUE YA CONOZCO · ESCRIBO LA PARTÍCULA QUE LES FALTA", c, size=13)
    yy += 32
    pw = (ww - 2 * 20) / 3
    for k, (v, es) in enumerate((("wake", "despertarse"), ("sit", "sentarse"), ("look", "cuidar a alguien"))):
        px = x0 + k * (pw + 20)
        caja(b, px, yy, pw, 64, c, r=12)
        texto(b, px + 18, yy + 41, v, size=20, weight="700")
        b.append(rect(px + 30 + tw(v, 20, "700"), yy + 12, 90, 40, "white", r=8, stroke=c, sw=2))
        pista(b, px + 140 + tw(v, 20, "700"), yy + 39, "= " + es)
    return yy + 64


# ───────── QD · Examen 1 · 16 · While ─────────
def ii4(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La cuerda: ¿las dos ideas tiran juntas o en contra?", c,
                      "Cada idea agarra un extremo de la cuerda. Decide si las dos tiran hacia el mismo lado (una suma o explica "
                      "a la otra) o hacia lados contrarios. Esa respuesta escoge la familia del conector.")
    x0, ww = x + 22, w - 44
    ew = 440
    for k, (rt, en) in enumerate((("IDEA 1", "many people believe coffee is bad"),
                                  ("IDEA 2", "studies show it is good for your heart"))):
        bx = x0 if k == 0 else x0 + ww - ew
        caja(b, bx, yy, ew, 86, c, sw=2.4, r=14)
        rot(b, bx + 20, yy + 28, rt, c, size=14)
        texto(b, bx + 20, yy + 64, en, size=18, weight="700")
    rx0, rx1 = x0 + ew, x0 + ww - ew
    b.append(line(rx0, yy + 43, rx1, yy + 43, c, 7))
    b.append(line(rx0, yy + 43, rx1, yy + 43, "white", 2, dash="10,10"))
    mx = (rx0 + rx1) / 2
    b.append(f'<circle cx="{mx}" cy="{yy + 43}" r="12" fill="white" stroke="{c}" stroke-width="3"/>')
    pista(b, mx, yy + 24, "dibuja sobre la cuerda hacia dónde tira cada una", anchor="middle")
    yy += 104
    marca(b, x0 + 20, yy, c, "tiran hacia el mismo lado", size=16)
    marca(b, x0 + 360, yy, c, "tiran hacia lados contrarios", size=16)
    pista(b, x0 + 720, yy + 17, "la palabra de cada idea que más tira:")
    renglon(b, x0 + 990, yy + 19, x0 + ww - 20)
    return yy + 40


def comp(parte):
    return None      # el motor antepone «competencia ·»; la parte del examen va en ing3_icfes.csv


QA = dict(est=1, comp=comp(4), f=F, e=INSTR, inst=ii1,
          datos=fragmento("COFFEE", [COFFEE_2], 10),
          o=["during", "until", "since"])
QB = dict(est=2, comp=comp(4), f=F, e=INSTR, inst=ii2,
          datos=fragmento("COFFEE", [COFFEE_3], 13),
          o=["describe", "described", "describes"])
QC = dict(est=3, comp=comp(7), f=F, e=INSTR, inst=ii3,
          datos=fragmento("VALENTINE'S DAY", [VALENTINE_2], 24),
          o=["off", "in", "at", "out"])
QD = dict(est=4, comp=comp(4), f=F, e=INSTR, inst=ii4,
          datos=fragmento("COFFEE", [COFFEE_4], 16),
          o=["While", "Except", "Because"])


def build(pages=(285, 289)):
    return [hoja_icfes("ing3_i1", pages[0], QA, QB),
            hoja_icfes("ing3_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
