#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 6 · entrenamiento ICFES · páginas 337 y 344 (cierre del área).

Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11», sin año ni «oficial».

Claves verificadas (resueltas a mano, no copiadas de la tabla de respuestas):

    QA · SIMULACRO II 2023 Oficio · Inglés, Parte 4, N.º 253                · C  found   estrategia 1
    QB · cuadernillo Inglés Saber 11 (Icfes 2024), Examen 2, Parte 4, n.º 10 · B  said    estrategia 2
    QC · cuadernillo Inglés Saber 11 (Icfes 2024), Examen 1, Parte 4, n.º 12 · A  among   estrategia 3
    QD · SIMULACRO II 2023 Oficio · Inglés, Parte 4, N.º 222                · B  So      estrategia 4

 253 · C: «At the time» remite a un momento del pasado ya nombrado («Almost eight centuries later…
       began») y la oración sigue con «were already famous»: pasado simple, found. «find» es presente;
       «finding» necesita un auxiliar.
  10 · B: «Some scientists have ___» → have + participio: said (say · said · said). Tabla oficial: B.
  12 · A: «popular among Europeans»: popular entre un grupo de personas. «about» (sobre un tema) y «along»
       (a lo largo de) no van con «popular … Europeans». Tabla oficial: A.
 222 · B: las oraciones de antes dan las razones (vitaminas, minerales, limpia los dientes, ninguna fruta
       tiene tanto) y la del espacio dice el resultado: no sorprende que la llamen «the King». Conector de
       consecuencia: So. «But» es contraste; «Because» introduce una causa y no puede abrir una oración
       principal seguida de coma.

Las cuatro son de la Parte 4 (texto con espacios, tres opciones). Cada texto se imprime completo con
todos sus espacios numerados, como en el cuadernillo; solo se responde el espacio de la pregunta. El
texto del lobo etíope trae en el cuadernillo una errata de numeración («(4)» por «(14)»): se imprime
(14). Reservadas en tablero/propuestas/ing_icfes_reservas.csv (las 13, 16 y 24 del cuadernillo que se
pensaron primero ya las tenía la Misión 3).
"""
from ing6 import *   # noqa: F401,F403  (configura la misión y EST)
from ing6 import rot, caja, pista, renglon, texto, tinte, flecha, sino


def lectura(b, x, y, w, titulo, txt, size=18):
    svg, yy = TJ(x + 22, y + 46, txt, w - 44, size, INK, lh=size + 6)
    h = yy - y + 12
    b.append(rect(x, y, w, h, "white", r=12, stroke=GRAY, sw=1.6))
    b.append(T(x + w / 2, y + 30, [titulo], 17, INK, weight="700", anchor="middle"))
    b.append(svg)
    return y + h


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 14, txt, w, 20, INK, weight="700", lh=28)
    b.append(svg)
    return y2


INSTR = "Lea el texto y seleccione la palabra correcta para el espacio indicado."

# ───────── QA · SIM. II N.º 253 · History of paper ─────────
PAPER = ("Since the beginning of writing, people tried to think of something easy and cheap to write on, (246) ________ "
         "it took 3000 years until the Chinese people made paper. Only one thousand years afterwards, people were "
         "(247) ________ paper all over Europe and Asia. In the 8th century, the Arabs and the Chinese were enemies, "
         "and the Arabs captured (248) ________ Chinese men. Many of (249) ________ men knew how to make paper, and "
         "(250) ________ explained it to the Arabs as the price to be able to go home. Almost eight centuries (251) "
         "________ Europeans began to make (252) ________ own paper. At the time, people in the country of the Aztecs "
         "(253) ________ the way to make paper too, while the Chinese people were already famous for paper kites and "
         "toilet paper!")


def datos_253(b, x, y, w):
    yy = lectura(b, x, y, w, "HISTORY OF PAPER", PAPER)
    return pregunta(b, x, yy + 4, w, "Espacio (253):")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Los relojes del párrafo", c,
                      "Como con «Two years ago»: primero el marcador. Copia las marcas de tiempo del texto en orden y "
                      "escribe al lado si hablan del pasado o de hoy. El espacio 253 vive donde vive su marcador.")
    x0, ww = x + 22, w - 44
    n = 4
    gw = (ww - 30 * (n - 1)) / n
    for k, ps in enumerate(("primera marca:", "segunda marca:", "tercera marca:", "«At the time» = ")):
        bx = x0 + k * (gw + 30)
        caja(b, bx, yy, gw, 112, c, r=12)
        pista(b, bx + 14, yy + 30, ps)
        renglon(b, bx + 14, yy + 66, bx + gw - 14)
        for j, lab in enumerate(("pasado", "hoy")):
            b.append(checkbox(bx + 14 + j * 100, yy + 80, s=9, c=c))
            texto(b, bx + 38 + j * 100, yy + 96, lab, size=14, color=GRAY)
        if k < n - 1:
            flecha(b, bx + gw + 4, yy + 56, bx + gw + 26, yy + 56, c, head=8)
    yy += 130
    pista(b, x0, yy + 6, "el otro verbo de la misma oración («the Chinese people ___ already famous») está en:")
    renglon(b, x0 + 640, yy + 10, x0 + ww)
    return yy + 16


# ───────── QB · 2024 · Examen 2 · n.º 10 · The Ethiopian wolf ─────────
WOLF = ("It is an African animal, (0) which is called the Simien Jackal. Some scientists have (10) ________ it is not a "
        "real wolf. But studies show that (11) ________ close relationship to grey wolves and coyotes is evident. (12) "
        "________ Ethiopian wolves are more similar to grey wolves and coyotes than any other African canines. "
        "Scientists also believe there are about 450 of them living in wild conditions. The (13) ________ group of "
        "Ethiopian wolves lives (14) ________ the Bale Mountains National Park. The Ethiopian wolf has a special red "
        "coat with a white part in the front of the body. It is in size from 1,1 to 1,4 meters. By nature, the "
        "Ethiopian wolf looks for food by day, but it is sometimes nocturnal in areas where other animals may hunt it.")


def datos_10(b, x, y, w):
    yy = lectura(b, x, y, w, "THE ETHIOPIAN WOLF", WOLF)
    return pregunta(b, x, yy + 4, w, "Espacio (10):")


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Mira la palabra que va justo antes del espacio", c,
                      "Como con «I have already ___»: antes de leer las opciones, lee la palabra que manda. Escríbela, "
                      "di qué forma pide y llena las formas de «say».")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    caja(b, x0, yy, half, 120, c, r=14)
    pista(b, x0 + 18, yy + 34, "la palabra justo antes del espacio 10:")
    renglon(b, x0 + 300, yy + 38, x0 + half - 18)
    pista(b, x0 + 18, yy + 84, "la forma que pide:")
    renglon(b, x0 + 160, yy + 88, x0 + half - 18)
    bx = x0 + half + 30
    cw = (half - 40) / 3
    for k, lab in enumerate(("BASE", "PASADO", "PARTICIPIO")):
        cx = bx + k * (cw + 20)
        caja(b, cx, yy, cw, 120, c, r=12, fill=tinte(c, 0.95))
        rot(b, cx + cw / 2, yy + 28, lab, c, size=13, anchor="middle")
        renglon(b, cx + 16, yy + 90, cx + cw - 16)
    return yy + 120


# ───────── QC · 2024 · Examen 1 · n.º 12 · Coffee ─────────
COFFEE = ("Coffee is popular around the world. (0) Over the past centuries, few subjects have been as carefully studied "
          "as coffee. Its (9) ________ important component is caffeine and it has lots of benefits. Coffee has been "
          "well-known (10) ________ the beginning of the 14th century, (11) ________ Sufi Yemenis started using coffee "
          "to stay alert during special activities. It became a popular medicine (12) ________ Europeans in the 1600s. "
          "Caffeine was first (13) ________ in the 1800s by Ferdinand Runge, a doctor that found out some effects of "
          "coffee on people. Some people say (14) ________ coffee isn't good, but doctors say you (15) ________ "
          "believe this. Thanks to caffeine you don't get hungry. Coffee can also reduce headaches and blood problems. "
          "(16) ________ many people believe coffee is bad, studies show it is good for your heart.")


def datos_12(b, x, y, w):
    yy = lectura(b, x, y, w, "COFFEE", COFFEE)
    return pregunta(b, x, yy + 4, w, "Espacio (12):")


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Popular, ¿pero entre quiénes?", c,
                      "Como con «___ evidence»: hay palabras que casi siempre llegan acompañadas. Dibuja la medicina en "
                      "medio de la gente y escribe qué palabra pide «popular» cuando después viene un grupo de personas.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 420, 150, c, r=14)
    for k in range(9):
        cx = x0 + 60 + (k % 5) * 76 + (38 if k >= 5 else 0)
        cy = yy + 50 + (k // 5) * 60
        b.append(f'<circle cx="{cx}" cy="{cy}" r="13" fill="white" stroke="{c}" stroke-width="2"/>')
    pista(b, x0 + 210, yy + 140, "los europeos de 1600", anchor="middle")
    bx = x0 + 450
    caja(b, bx, yy, ww - 450, 150, c, r=14)
    pista(b, bx + 18, yy + 34, "«a popular medicine ___ Europeans» = una medicina popular ___ los europeos")
    pista(b, bx + 18, yy + 80, "en español diría:")
    renglon(b, bx + 160, yy + 84, bx + ww - 450 - 18)
    pista(b, bx + 18, yy + 126, "y en inglés esa palabra es:")
    renglon(b, bx + 220, yy + 130, bx + ww - 450 - 18)
    return yy + 150


# ───────── QD · SIM. II N.º 222 · The Apple ─────────
APPLE = ("An apple is good for one's health. It has important vitamins and minerals. Also, it helps to clean one's teeth "
         "after a meal. No other fruit has such good things for your body. (222) ______, it is not surprising that the "
         "apple is known (223) ______ the “King” of all fruits. The Romans helped greatly in (224) ______ the apple "
         "trees in European lands. Each time the Romans traveled around a country, they always (225) ______ apple seeds "
         "and planted (226) ______. They also carried the apple to England. The apple was brought to America (227) "
         "______ the first explorers from Europe. The Americans eat (228) ______ apples and apple cakes than any other "
         "people and (229) ______ two things have become American national foods.")


def datos_222(b, x, y, w):
    yy = lectura(b, x, y, w, "THE APPLE", APPLE)
    return pregunta(b, x, yy + 4, w, "Espacio (222):")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Lo que viene antes, el puente y lo que viene después", c,
                      "Como en el ejemplo con que abre la misión en el libro («The team trained hard; ___, they were "
                      "ready»): mira qué relación hay entre las dos ideas antes de escoger el conector.")
    x0, ww = x + 22, w - 44
    bw_ = (ww - 2 * 170) / 2
    caja(b, x0, yy, bw_, 150, c, r=14)
    rot(b, x0 + 18, yy + 28, "LO QUE DICEN LAS ORACIONES DE ANTES", c, size=12)
    renglon(b, x0 + 18, yy + 78, x0 + bw_ - 18)
    renglon(b, x0 + 18, yy + 122, x0 + bw_ - 18)
    mx = x0 + bw_ + 40
    caja(b, mx, yy + 30, 250, 90, c, r=45, sw=2.6, fill=tinte(c, 0.94))
    rot(b, mx + 125, yy + 62, "EL PUENTE", c, size=12, anchor="middle")
    renglon(b, mx + 40, yy + 102, mx + 210)
    flecha(b, x0 + bw_ + 6, yy + 75, mx - 6, yy + 75, c, head=9)
    flecha(b, mx + 256, yy + 75, mx + 294, yy + 75, c, head=9)
    rx = mx + 300
    caja(b, rx, yy, x0 + ww - rx, 150, c, r=14)
    rot(b, rx + 18, yy + 28, "LO QUE DICE LA ORACIÓN DEL ESPACIO", c, size=12)
    renglon(b, rx + 18, yy + 78, x0 + ww - 18)
    renglon(b, rx + 18, yy + 122, x0 + ww - 18)
    yy += 166
    pista(b, x0, yy + 8, "la segunda idea es, de la primera:")
    for j, lab in enumerate(("su causa", "su resultado", "su contrario")):
        b.append(checkbox(x0 + 270 + j * 170, yy - 8, s=10, c=c))
        texto(b, x0 + 298 + j * 170, yy + 9, lab, size=15, color=GRAY)
    return yy + 20


QA = dict(est=1, comp="Gramática · tiempos verbales", e=INSTR, o=["find", "finding", "found"],
          datos=datos_253, inst=ii1)
QB = dict(est=2, comp="Gramática · forma del verbo", e=INSTR, o=["saying", "said", "say"],
          datos=datos_10, inst=ii2)
QC = dict(est=3, comp="Léxico · colocación", e=INSTR, o=["among", "about", "along"],
          datos=datos_12, inst=ii3)
QD = dict(est=4, comp="Gramática · conectores y cohesión", e=INSTR, o=["Because", "So", "But"],
          datos=datos_222, inst=ii4)


def build(pages=(337, 344)):
    return [hoja_icfes("ing6_i1", pages[0], QA, QB),
            hoja_icfes("ing6_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
