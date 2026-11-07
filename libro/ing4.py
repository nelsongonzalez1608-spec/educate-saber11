#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 4 · componente lectura · páginas 290–296.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 4» de Inglés (fuente_libro/INGLÉS), páginas 446–448.
Comprensión literal: la página 446 trae la tabla «Language Tools» (idea principal, ejemplo, dato,
contraste, repetición de palabras clave) y dos bloques con 8 preguntas cada uno, todas de tres
opciones (A–C). La numeración vuelve a empezar en 1 en el bloque 2.
  · Bloque 1 · la gira «This Is For» de TWICE en Australia (Rolling Stone Australia, 2025):
    texto en las páginas 446 y 447, preguntas en la 447.
  · Bloque 2 · Nairo Quintana y la Vuelta a España 2016: texto en la 447, preguntas en la 448.

El cuaderno trabaja 10 de las 16 (cinco por bloque). Equivalencia (cuaderno → libro):

    1 → B1·1   2 → B1·4   3 → B1·5   4 → B1·6   5 → B1·7
    6 → B2·1   7 → B2·2   8 → B2·4   9 → B2·6  10 → B2·7

Claves verificadas (resueltas a mano contra el texto del libro, 7 nov 2026):

    1·B  2·A  3·B  4·C  5·C  6·A  7·C  8·C  9·A  10·B

  1 · B Two: «two Sydney shows at Qudos Bank Arena». Four son los de toda Australia (2 + 2).
  2 · A August 8 at 11 AM: «general ticket sales opening on August 8 at 11 AM». August 7 at 10 AM
      es la preventa (pre-sale) para miembros de Live Nation; July 11 es el álbum.
  3 · B July 11: «released their fourth full album This Is For on July 11». August 8 es la venta
      general; November 1, el primer concierto.
  4 · C four full albums and 14 mini-albums: «released four full albums and 14 mini-albums».
  5 · C headline major stadiums: «the first female K-pop group to headline major US stadiums like
      SoFi and MetLife». Tokyo Dome no está en el texto (en Japón habla de Nissan Stadium) y
      Billboard tampoco.
  6 · A Spain's capital city: «ended in Madrid». B (Cataluña) no está; C (Boyacá) es donde se
      celebró, no donde terminó.
  7 · C The Colombian athlete riding for Movistar Team: Quintana, «riding for the Movistar Team,
      won the general classification». A es Herrera (1987); B, Froome (segundo).
  8 · C 1987: «after Luis Herrera's victory in 1987». A y B no cuadran con el año.
  9 · A The British cyclist associated with Team Sky: «Chris Froome, from Team Sky, who finished
      second». El texto no dice que Froome sea británico (dato de afuera; ver hallazgos).
 10 · B exactly two: «the first time two Colombians shared the final podium» (Quintana 1.º y
      Chaves 3.º). Herrera ganó en 1987, no estuvo en ese podio.

Reparto: A 3 · B 3 · C 4. Reparto de las 16 del libro: A 6 · B 4 · C 6. Equilibrado.

Estrategias:
    1 · La palabra ancla               (1, 5, 10  · ICFES ex. 1 · 18)   azul
    2 · Cada cifra tiene dueño         (2, 4, 8   · ICFES ex. 1 · 17)   rojo
    3 · Lo dice con otras palabras     (6, 7      · ICFES ex. 2 · 18)   oro
    4 · Es verdad, pero no responde    (3, 9      · ICFES ex. 1 · 20)   morado

Hojas: 290 ing4_t1 (1-2) · 291 ing4_t2 (3-4) · 292 ing4_i1 · 293 ing4_t3 (5-6) ·
       294 ing4_t4 (7-8) · 295 ing4_t5 (9-10) · 296 ing4_i2.
"""
from taller_base import *

configurar("Inglés", 4, "lectura",
           tema="Lo que el texto dice, dato por dato")
MORADO = "#5B3E96"
EST = {1: ("La palabra ancla", EDU_AZUL),
       2: ("Cada cifra tiene dueño", EDU_ROJO),
       3: ("Lo dice con otras palabras", EDU_ORO),
       4: ("Es verdad, pero no responde", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def texto(b, x, y, txt, size=17, color=INK, weight="400", anchor="start", style="normal"):
    b.append(T(x, y, [txt], size, color, weight=weight, anchor=anchor, style=style))


def tinte(c, k=0.9):
    from taller_base import _mezcla
    return _mezcla(c, k)


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12, bend=0.0):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def marca(b, x, y, c, lab, size=16):
    b.append(checkbox(x, y, s=10, c=c))
    b.append(T(x + 28, y + 17, [lab], size, GRAY))
    return x + 28 + tw(lab, size) + 30


def frase_hueco(b, x, y, w, txt, c, h=54, size=18):
    caja(b, x, y, w, h, c)
    b.append(T(x + 22, y + h / 2 + 7, [txt], size, INK, weight="700"))
    return y + h


def pregunta_en(b, x, y, w, txt, c, rotulo="LA PREGUNTA, EN TU LIBRO"):
    """La pregunta del libro en inglés, tal cual, para trabajar sobre ella."""
    svg, yy = TJ(x + 30, y + 40, txt, w - 60, 20, INK, weight="700", lh=29)
    h = yy - y + 8
    b.append(rect(x, y, w, h, tinte(c, 0.93), r=12))
    b.append(rect(x, y, 8, h, c, r=4))
    rot(b, x + 30, y + 28, rotulo, c, size=13)
    b.append(svg)
    return y + h


def encabezado(b, x, y, cols, heads, c, hh=46):
    caja(b, x, y, sum(cols), hh, c, fill=tinte(c), r=8)
    for k, hd in enumerate(heads):
        if hd:
            rot(b, x + sum(cols[:k]) + 14, y + hh / 2 + 6, hd, c, size=13)
    return y + hh


def rejilla(b, x, y, cols, n, c, rh=58, y_top=None):
    """Filas vacías con renglón en cada celda y líneas de columna desde y_top."""
    ry = y
    for _ in range(n):
        caja(b, x, ry, sum(cols), rh, c, r=0)
        for k in range(len(cols)):
            cx0 = x + sum(cols[:k])
            renglon(b, cx0 + 14, ry + rh - 14, cx0 + cols[k] - 14)
        ry += rh
    for k in range(1, len(cols)):
        cx0 = x + sum(cols[:k])
        b.append(line(cx0, y_top if y_top is not None else y, cx0, ry, c, 1.6))
    return ry


# ───────── P1 · B1·1 · shows en Sydney ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La palabra ancla y sus vecinas", c,
                      "La palabra ancla es la de la pregunta que seguro aparece igualita en el texto (un nombre, una "
                      "ciudad, una fecha). Encuéntrala, copia lo que tiene alrededor y responde solo con eso.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "1. How many shows will TWICE perform in Sydney?", c)
    yy += 22
    rot(b, x0, yy + 18, "PASO 1 · ENCIERRA EN LA PREGUNTA DE ARRIBA LA PALABRA ANCLA", c, size=14)
    yy += 40
    rot(b, x0, yy + 18, "PASO 2 · EN EL TEXTO, LAS DOS PALABRAS ANTES Y LAS DOS DESPUÉS DEL ANCLA", c, size=14)
    yy += 34
    n = 5
    gw = (ww - (n - 1) * 16) / n
    for k in range(n):
        bx = x0 + k * (gw + 16)
        ancla = k == 2
        caja(b, bx, yy, gw, 70, c, sw=2, r=12, fill=tinte(c, 0.9) if ancla else "white")
        if ancla:
            pista(b, bx + gw / 2, yy + 92, "el ancla", anchor="middle")
    yy += 112
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "PASO 3 · EL NÚMERO QUE ESTÁ PEGADO AL ANCLA", c, size=14)
    pista(b, x0 + 20, yy + 66, "el número:")
    b.append(rect(x0 + 110, yy + 42, 110, 40, "white", r=8, stroke=c, sw=2))
    pista(b, x0 + 260, yy + 66, "¿de qué es? ¿solo de esa ciudad o de todo el país?")
    for k, lab in enumerate(("de esa ciudad", "de todo el país")):
        marca(b, x0 + 620 + k * 220, yy + 50, c, lab)
    pista(b, x0 + 20, yy + 116, "otro número de conciertos que hay en el texto y de qué es:")
    renglon(b, x0 + 430, yy + 118, x0 + ww - 20)
    yy += 166
    return trampa(b, x0, yy, ww, "Un número puede ser verdadero y de otro sitio:",
                  "antes de marcar, revisa que el número que escogiste sea el que está pegado a tu ancla, y no el de "
                  "otra ciudad ni una cuenta que hiciste tú.", c)


# ───────── P2 · B1·4 · venta general ─────────
def i2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El calendario de TWICE: cada fecha con su evento", c,
                      "El texto trae muchas fechas y cada una es de un evento distinto. Ponlas todas en el calendario, "
                      "con su hora si la tiene, y escribe al lado de qué es. Después busca el evento que te preguntan.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "4. General ticket sales in Australia started on:", c)
    yy += 22
    meses = ("JULIO · JULY", "AGOSTO · AUGUST", "NOVIEMBRE · NOVEMBER")
    mw = (ww - 2 * 20) / 3
    for k, m in enumerate(meses):
        bx = x0 + k * (mw + 20)
        caja(b, bx, yy, mw, 250, c, sw=2.4, r=14)
        b.append(rect(bx, yy, mw, 44, tinte(c, 0.88), r=14))
        b.append(rect(bx, yy + 24, mw, 20, tinte(c, 0.88), r=0))
        rot(b, bx + 18, yy + 29, m, c, size=14)
        for j in range(2):
            ry = yy + 62 + j * 92
            caja(b, bx + 16, ry, 64, 52, c, r=8)
            pista(b, bx + 48, ry + 72, "día", anchor="middle", size=13)
            pista(b, bx + 96, ry + 20, "hora:", size=13)
            renglon(b, bx + 136, ry + 22, bx + mw - 16)
            pista(b, bx + 96, ry + 50, "qué pasa:", size=13)
            renglon(b, bx + 166, ry + 52, bx + mw - 16)
    yy += 270
    caja(b, x0, yy, ww, 96, c, r=14)
    rot(b, x0 + 20, yy + 30, "DOS PALABRAS QUE SE PARECEN", c, size=14)
    pista(b, x0 + 20, yy + 66, "«pre-sale» (pista: pre- como en prehistoria) creo que es:")
    renglon(b, x0 + 420, yy + 68, x0 + 760)
    pista(b, x0 + 790, yy + 66, "«general sale» creo que es:")
    renglon(b, x0 + 990, yy + 68, x0 + ww - 20)
    yy += 112
    return frase_hueco(b, x0, yy, ww, "La pregunta pide el evento ______________________ ; en mi calendario es el mes ____________ .", c)


# ───────── P3 · B1·5 · el álbum ─────────
def i3(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Dos preguntas a cada opción: ¿está en el texto? ¿responde?", c,
                      "Las tres fechas de las opciones aparecen en el texto: por eso las tres «suenan». Una opción "
                      "sirve solo si pasa las dos preguntas. Busca la palabra de la pregunta (released) y la fecha que "
                      "va con ella.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "5. The album This Is For was released on:", c)
    yy += 22
    cols = (110, 250, ww - 110 - 250 - 280, 280)
    yy0 = yy
    yy = encabezado(b, x0, yy, cols, ("OPCIÓN", "¿ESTÁ EN EL TEXTO?", "EN EL TEXTO, ESA FECHA ES DE…",
                                      "¿RESPONDE LA PREGUNTA?"), c)
    rh = 74
    for k, L in enumerate("ABC"):
        ry = yy + k * rh
        caja(b, x0, ry, sum(cols), rh, c, r=0)
        b.append(f'<circle cx="{x0 + 55}" cy="{ry + rh / 2}" r="18" fill="white" stroke="{c}" stroke-width="2.2"/>')
        texto(b, x0 + 55, ry + rh / 2 + 6, L, size=17, color=c, weight="700", anchor="middle")
        marca(b, x0 + cols[0] + 30, ry + 26, c, "sí")
        marca(b, x0 + cols[0] + 130, ry + 26, c, "no")
        cx2 = x0 + cols[0] + cols[1]
        renglon(b, cx2 + 14, ry + rh - 18, cx2 + cols[2] - 14)
        cx3 = cx2 + cols[2]
        marca(b, cx3 + 30, ry + 26, c, "sí")
        marca(b, cx3 + 130, ry + 26, c, "no")
    ry = yy + 3 * rh
    for k in range(1, 4):
        b.append(line(x0 + sum(cols[:k]), yy0, x0 + sum(cols[:k]), ry, c, 1.6))
    yy = ry + 22
    yy = frase_hueco(b, x0, yy, ww, "La palabra de la pregunta que me llevó a la fecha: ______________ (en la línea ____ del texto).", c)
    yy += 16
    return ojo(b, x0, yy, ww, "VERDADERO NO ES LO MISMO QUE CORRECTO",
               "Una fecha puede estar escrita en el texto y no ser la del álbum. La columna «¿está en el texto?» no "
               "decide nada: decide la última.")


# ───────── P4 · B1·6 · discos ─────────
def i4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Cada número del texto con su etiqueta", c,
                      "El texto está lleno de números. Cuélgale a cada uno su etiqueta: qué cuenta. La "
                      "respuesta pone cada número con su etiqueta, sin cambiarlas de dueño.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "6. TWICE has released a total of:", c)
    yy += 24
    nums = ("2015", "nine", "four", "14", "20 million", "24", "100 million", "1.5 million")
    cols_n = 4
    tw_ = (ww - (cols_n - 1) * 18) / cols_n
    for k, n_ in enumerate(nums):
        col, fila = k % cols_n, k // cols_n
        bx, by = x0 + col * (tw_ + 18), yy + fila * 150
        # etiqueta con su ojal
        b.append(f'<path d="M {bx + 30} {by} L {bx + tw_} {by} L {bx + tw_} {by + 130} L {bx + 30} {by + 130} '
                 f'L {bx} {by + 65} Z" fill="white" stroke="{c}" stroke-width="2.2"/>')
        b.append(f'<circle cx="{bx + 26}" cy="{by + 65}" r="7" fill="white" stroke="{c}" stroke-width="2"/>')
        texto(b, bx + 50, by + 40, n_, size=22, weight="700")
        pista(b, bx + 50, by + 70, "cuenta:", size=14)
        renglon(b, bx + 50, by + 98, bx + tw_ - 16)
        renglon(b, bx + 50, by + 122, bx + tw_ - 16)
    yy += 2 * 150 + 4
    yy = frase_hueco(b, x0, yy, ww, "La pregunta pide ______________ ; las etiquetas que la responden son: ______________________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "El número correcto con la etiqueta equivocada:",
                  "una opción puede usar un número que sí está en el texto y pegarle la etiqueta de otro. Lee cada "
                  "opción contra tus etiquetas, número por número.", c)


# ───────── P5 · B1·7 · Estados Unidos ─────────
def i5(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos «primeras veces», dos países", c,
                      "El texto cuenta dos récords de «la primera vez». La pregunta pide uno solo, el de un país. Busca "
                      "cómo escribe el texto el nombre de ese país (puede ser una abreviatura) y llena cada récord en su "
                      "país.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "7. In the United States, TWICE became the first female K-pop group to:", c)
    yy += 22
    caja(b, x0, yy, ww, 70, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL ANCLA DISFRAZADA", c, size=14)
    pista(b, x0 + 20, yy + 56, "la pregunta dice «United States»; el texto lo escribe así:")
    b.append(rect(x0 + 450, yy + 16, 160, 40, "white", r=8, stroke=c, sw=2))
    pista(b, x0 + 640, yy + 44, "y lo encontré en la línea:")
    renglon(b, x0 + 840, yy + 46, x0 + ww - 20)
    yy += 90
    hw = (ww - 30) / 2
    for k, pais in enumerate(("PRIMER PAÍS QUE NOMBRA", "SEGUNDO PAÍS QUE NOMBRA")):
        bx = x0 + k * (hw + 30)
        caja(b, bx, yy, hw, 236, c, sw=2.4, r=16)
        rot(b, bx + 20, yy + 30, pais, c, size=14)
        pista(b, bx + 20, yy + 62, "el país:")
        renglon(b, bx + 90, yy + 64, bx + hw - 20)
        pista(b, bx + 20, yy + 104, "«the first … to …» (lo que lograron):")
        renglon(b, bx + 20, yy + 142, bx + hw - 20)
        renglon(b, bx + 20, yy + 176, bx + hw - 20)
        pista(b, bx + 20, yy + 214, "los estadios que nombra:")
        renglon(b, bx + 200, yy + 216, bx + hw - 20)
    yy += 256
    return ojo(b, x0, yy, ww, "SI NO ESTÁ EN EL TEXTO, NO ES LITERAL",
               "Esta misión pide lo que el texto dice, no lo que sabes de TWICE. Si una opción nombra un lugar o un "
               "premio que no está en tus dos cajas, no lo saques de tu memoria: búscalo, y si no está, no cuenta.")


# ───────── P6 · B2·1 · Madrid ─────────
def i6(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Mismo lugar, otro nombre", c,
                      "Las opciones casi nunca copian el texto: lo dicen con otras palabras. Copia lo que dice el texto, "
                      "escribe cómo lo dice cada opción y decide si es el mismo lugar. A veces hace falta un dato que ya "
                      "sabes del mundo.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "1. According to the passage, where did the cycling event conclude in 2016?", c)
    yy += 22
    caja(b, x0, yy, ww, 96, c, sw=2.4, r=14)
    rot(b, x0 + 20, yy + 30, "EL TEXTO DICE (CÓPIALO DE LA PRIMERA LÍNEA)", c, size=14)
    texto(b, x0 + 20, yy + 72, "the Vuelta a España ended in", size=19, weight="700")
    renglon(b, x0 + 300, yy + 74, x0 + ww - 20)
    yy += 116
    cols = (110, 420, ww - 110 - 420 - 260, 260)
    yy0 = yy
    yy = encabezado(b, x0, yy, cols, ("OPCIÓN", "EL LUGAR QUE NOMBRA", "LO QUE TUVE QUE SABER PARA COMPARAR",
                                      "¿EL MISMO LUGAR?"), c)
    rh = 66
    for k, L in enumerate("ABC"):
        ry = yy + k * rh
        caja(b, x0, ry, sum(cols), rh, c, r=0)
        b.append(f'<circle cx="{x0 + 55}" cy="{ry + rh / 2}" r="17" fill="white" stroke="{c}" stroke-width="2.2"/>')
        texto(b, x0 + 55, ry + rh / 2 + 6, L, size=17, color=c, weight="700", anchor="middle")
        for j in (1, 2):
            cx0 = x0 + sum(cols[:j])
            renglon(b, cx0 + 14, ry + rh - 16, cx0 + cols[j] - 14)
        cx3 = x0 + sum(cols[:3])
        marca(b, cx3 + 30, ry + 22, c, "sí")
        marca(b, cx3 + 130, ry + 22, c, "no")
    ry = yy + 3 * rh
    for k in range(1, 4):
        b.append(line(x0 + sum(cols[:k]), yy0, x0 + sum(cols[:k]), ry, c, 1.6))
    yy = ry + 22
    caja(b, x0, yy, ww, 118, c, r=14)
    rot(b, x0 + 20, yy + 30, "PRACTICA CON COLOMBIA · ¿QUÉ CIUDAD ES?", c, size=14)
    for k, (en, _) in enumerate((("the capital of Colombia", ""), ("the main city of Antioquia", ""),
                                 ("the largest port on the Pacific", ""))):
        bx = x0 + 20 + k * ((ww - 40) / 3)
        texto(b, bx, yy + 68, en, size=17, weight="700")
        renglon(b, bx, yy + 100, bx + (ww - 40) / 3 - 30)
    return yy + 118


# ───────── P7 · B2·2 · el título general ─────────
def i7(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Las palabras de la pregunta, buscadas con otro nombre", c,
                      "La pregunta no usa las mismas palabras del texto. Para cada pedazo de la pregunta, escribe la "
                      "frase del texto que quiere decir lo mismo. Si no encuentras el pedazo, no encuentras la respuesta.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "2. Who managed to win the overall title in that year's competition?", c)
    yy += 22
    cols = (360, ww - 360 - 200, 200)
    yy0 = yy
    yy = encabezado(b, x0, yy, cols, ("EN LA PREGUNTA", "EN EL TEXTO SE DICE…", "¿EN QUÉ LÍNEA?"), c)
    rh = 66
    for k, p in enumerate(("managed to win", "the overall title", "that year's competition")):
        ry = yy + k * rh
        caja(b, x0, ry, sum(cols), rh, c, r=0)
        texto(b, x0 + 14, ry + 40, p, size=19, weight="700")
        for j in (1, 2):
            cx0 = x0 + sum(cols[:j])
            renglon(b, cx0 + 14, ry + rh - 16, cx0 + cols[j] - 14)
    ry = yy + 3 * rh
    for k in (1, 2):
        b.append(line(x0 + sum(cols[:k]), yy0, x0 + sum(cols[:k]), ry, c, 1.6))
    yy = ry + 22
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA FICHA DEL GANADOR, SEGÚN EL TEXTO", c, size=14)
    for k, lab in enumerate(("nombre:", "equipo:", "país:")):
        bx = x0 + 20 + k * ((ww - 40) / 3)
        pista(b, bx, yy + 74, lab)
        renglon(b, bx + 70, yy + 76, bx + (ww - 40) / 3 - 30)
    yy += 120
    return trampa(b, x0, yy, ww, "El texto nombra a más de un campeón:",
                  "antes de escoger, revisa de qué año es cada uno. La pregunta dice «that year»: el año del que habla "
                  "el texto desde la primera línea.", c)


# ───────── P8 · B2·4 · Luis Herrera ─────────
def i8(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dos colombianos en la línea de la Vuelta", c,
                      "El texto pone dos victorias colombianas en años distintos. Ubica las dos en la línea, mide la "
                      "distancia entre ellas y escribe cuál fue antes. Después compara cada opción con tu línea.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "4. In what year had Luis Herrera previously obtained the same trophy?", c)
    yy += 40
    ly = yy + 30
    b.append(line(x0 + 10, ly, x0 + ww - 30, ly, c, 4))
    b.append(f'<polygon points="{x0 + ww - 30},{ly - 12} {x0 + ww - 10},{ly} {x0 + ww - 30},{ly + 12}" fill="{c}"/>')
    anos = (1980, 1990, 2000, 2010, 2020)
    for k, a in enumerate(anos):
        px = x0 + 40 + k * (ww - 120) / 4
        b.append(line(px, ly - 14, px, ly + 14, c, 3))
        texto(b, px, ly + 40, str(a), size=16, color=c, weight="700", anchor="middle")
    pista(b, x0 + 10, ly - 28, "Marca con una flecha y un nombre dónde cae cada victoria:")
    yy = ly + 70
    hw = (ww - 30) / 2
    for k, rt in enumerate(("VICTORIA 1", "VICTORIA 2")):
        bx = x0 + k * (hw + 30)
        caja(b, bx, yy, hw, 112, c, r=14)
        rot(b, bx + 20, yy + 30, rt, c, size=14)
        pista(b, bx + 20, yy + 66, "quién:")
        renglon(b, bx + 80, yy + 68, bx + hw / 2 - 10)
        pista(b, bx + hw / 2 + 10, yy + 66, "año:")
        renglon(b, bx + hw / 2 + 56, yy + 68, bx + hw - 20)
        pista(b, bx + 20, yy + 98, "la palabra del texto que lo dice:")
        renglon(b, bx + 260, yy + 100, bx + hw - 20)
    yy += 130
    yy = frase_hueco(b, x0, yy, ww, "Herrera ganó ______ años ( antes / después ) de 2016; eso es más o menos ______ décadas.", c)
    yy += 16
    return ojo(b, x0, yy, ww, "«PREVIOUSLY» ES UNA PISTA DE TIEMPO",
               "«Previously» quiere decir «antes, en el pasado». Léela en la pregunta y ponla junto a tu línea: la "
               "misma pregunta te dice hacia qué lado de 2016 mirar.")


# ───────── P9 · B2·6 · el segundo ─────────
def i9(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El podio, escalón por escalón", c,
                      "Los tres del podio están en el texto, así que las tres opciones pueden describir a alguien real. "
                      "Sube a cada uno a su escalón con lo que el texto dice de él y mira cuál escalón te preguntan.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "6. Which competitor arrived second in the general standings?", c)
    yy += 30
    pw = 330
    alturas = {1: 220, 2: 170, 3: 130}
    orden = (2, 1, 3)
    base = yy + 330
    sx = x0 + (ww - 3 * pw) / 2
    for k, pos in enumerate(orden):
        bx = sx + k * pw
        ph = alturas[pos]
        caja(b, bx, base - ph, pw, ph, c, sw=2.6, r=6, fill=tinte(c, 0.9))
        texto(b, bx + pw / 2, base - ph + 50, f"{pos}.º", size=34, color=c, weight="700", anchor="middle")
        caja(b, bx + 14, base - ph - 104, pw - 28, 96, c, r=12)
        pista(b, bx + 30, base - ph - 76, "nombre:", size=14)
        renglon(b, bx + 100, base - ph - 74, bx + pw - 30)
        pista(b, bx + 30, base - ph - 42, "equipo / país:", size=14)
        renglon(b, bx + 140, base - ph - 40, bx + pw - 30)
        pista(b, bx + pw / 2, base - ph + 84, "lo dice el texto en:", size=13, anchor="middle")
        renglon(b, bx + 30, base - ph + 118, bx + pw - 30)
    yy = base + 22
    yy = frase_hueco(b, x0, yy, ww, "La pregunta pide el escalón ______ ; en el texto lo dice la frase «__________________».", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Que sea alguien del podio no basta:",
                  "una opción puede describir bien a un corredor que sí está en el texto, pero en otro escalón. "
                  "Antes de marcar, mira tu podio: ¿esa descripción es la del escalón que te preguntan?", c)


# ───────── P10 · B2·7 · los colombianos del podio ─────────
def i10(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Lista de todos los nombres del texto", c,
                      "Para contar bien, primero se hace la lista completa. Encuentra el ancla de la pregunta en el "
                      "texto; después escribe cada persona que nombra el texto y marca lo que el texto dice de ella.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "7. How many Colombian representatives stood on the last podium?", c)
    yy += 22
    caja(b, x0, yy, ww, 70, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL ANCLA", c, size=14)
    pista(b, x0 + 20, yy + 56, "la palabra de la pregunta que también está en el texto:")
    b.append(rect(x0 + 420, yy + 16, 180, 40, "white", r=8, stroke=c, sw=2))
    pista(b, x0 + 630, yy + 44, "la frase del texto donde está:")
    renglon(b, x0 + 850, yy + 46, x0 + ww - 20)
    yy += 90
    cols = (360, 300, 180, ww - 840)
    yy0 = yy
    yy = encabezado(b, x0, yy, cols, ("PERSONA QUE NOMBRA EL TEXTO", "DE DÓNDE ES, SEGÚN EL TEXTO",
                                      "¿DE QUÉ AÑO?", "¿EN EL ÚLTIMO PODIO?"), c)
    rh = 62
    for k in range(4):
        ry = yy + k * rh
        caja(b, x0, ry, sum(cols), rh, c, r=0)
        for j in range(3):
            cx0 = x0 + sum(cols[:j])
            renglon(b, cx0 + 14, ry + rh - 16, cx0 + cols[j] - 14)
        cx3 = x0 + sum(cols[:3])
        marca(b, cx3 + 30, ry + 20, c, "sí")
        marca(b, cx3 + 120, ry + 20, c, "no")
    ry = yy + 4 * rh
    for k in range(1, 4):
        b.append(line(x0 + sum(cols[:k]), yy0, x0 + sum(cols[:k]), ry, c, 1.6))
    yy = ry + 20
    yy = frase_hueco(b, x0, yy, ww, "Colombianos con «sí» en la última columna: ______ .", c)
    yy += 16
    return ojo(b, x0, yy, ww, "LA PREGUNTA DICE «THE LAST PODIUM»",
               "Antes de contar, revisa de qué año habla el texto en cada nombre: la pregunta es por el último "
               "podio, no por toda la historia del ciclismo colombiano.")


L3 = "ABC"
Q = {1: dict(n=1, est=1, pag=447, ctx="Bloque 1 · TWICE en Australia · pregunta 1 del bloque", inst=i1, letras=L3),
     2: dict(n=2, est=2, pag=447, ctx="Bloque 1 · TWICE en Australia · pregunta 4 del bloque", inst=i2, letras=L3),
     3: dict(n=3, est=4, pag=447, ctx="Bloque 1 · TWICE en Australia · pregunta 5 del bloque", inst=i3, letras=L3),
     4: dict(n=4, est=2, pag=447, ctx="Bloque 1 · TWICE en Australia · pregunta 6 del bloque", inst=i4, letras=L3),
     5: dict(n=5, est=1, pag=447, ctx="Bloque 1 · TWICE en Australia · pregunta 7 del bloque", inst=i5, letras=L3),
     6: dict(n=6, est=3, pag=448, ctx="Bloque 2 · Nairo y la Vuelta 2016 · pregunta 1 del bloque", inst=i6, letras=L3),
     7: dict(n=7, est=3, pag=448, ctx="Bloque 2 · Nairo y la Vuelta 2016 · pregunta 2 del bloque", inst=i7, letras=L3),
     8: dict(n=8, est=2, pag=448, ctx="Bloque 2 · Nairo y la Vuelta 2016 · pregunta 4 del bloque", inst=i8, letras=L3),
     9: dict(n=9, est=4, pag=448, ctx="Bloque 2 · Nairo y la Vuelta 2016 · pregunta 6 del bloque", inst=i9, letras=L3),
     10: dict(n=10, est=1, pag=448, ctx="Bloque 2 · Nairo y la Vuelta 2016 · pregunta 7 del bloque", inst=i10, letras=L3)}


def build(pages=(290, 291, 293, 294, 295)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"ing4_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
