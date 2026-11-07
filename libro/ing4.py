#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 4 · Parte 5 del ICFES · componente lectura · páginas 311–320.

Versión 3 (7 nov 2026, decisión de Nelson): el cuaderno trabaja LAS 16 PREGUNTAS del libro, una
tarjeta por pregunta, cada una con su subestrategia y su propio instrumento.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 4» de Inglés (fuente_libro/INGLÉS), páginas 446–448.
Comprensión literal, dos bloques de 8 preguntas (A–C). La numeración del libro vuelve a empezar en
el bloque 2; el cuaderno numera 1–16 y la línea de contexto dice «Bloque b, n.º k del libro».
  · Bloque 1 · la gira «This Is For» de TWICE en Australia (texto en 446–447, preguntas en 447).
  · Bloque 2 · Nairo Quintana y la Vuelta a España 2016 (texto en 447, preguntas en 448).

Estrategia de la Parte 5 (tema=): «Lo que el texto dice, dato por dato», en cuatro pasos:
1 el ancla de la pregunta · 2 cada dato con su dueño · 3 leo la frase vecina completa ·
4 comparo cada opción: ¿lo dice con otras palabras? ¿responde lo que preguntan?

Subestrategias (nombres y colores sin cambio: las hojas ICFES 315 y 320 los usan):
    1 · La palabra ancla               azul    1, 7, 8, 15     · ICFES QA (Salter · 18)
    2 · Cada cifra tiene dueño         rojo    4, 6, 11, 12, 16 · ICFES QC (Salter · 17)
    3 · Lo dice con otras palabras     oro     3, 9, 10, 13    · ICFES QB (Artistic Adventure · 18)
    4 · Es verdad, pero no responde    morado  2, 5, 14        · ICFES QD (Salter · 20)

Claves verificadas (resueltas otra vez a mano contra el texto del libro, 7 nov 2026):

    cuaderno  1·B  2·A  3·C  4·A  5·B  6·C  7·C  8·A    (= Bloque 1, n.º 1 a 8)
    cuaderno  9·A 10·C 11·B 12·C 13·A 14·A 15·B 16·C    (= Bloque 2, n.º 1 a 8)

  1 · B1·1 · B Two: «two Sydney shows». Four son los de toda Australia.
  2 · B1·2 · A Melbourne: «two more shows at Melbourne's Rod Laver Arena on November 8th and 9th».
      Sydney es verdad pero tiene el 1 y el 2; Brisbane no está en el texto.
  3 · B1·3 · C a 360-degree stage: «a state-of-the-art 360-degree stage design». Nada gira ni hay
      pantalla holográfica.
  4 · B1·4 · A August 8 at 11 AM (venta general; August 7 es la preventa).
  5 · B1·5 · B July 11 (el álbum).
  6 · B1·6 · C four full albums and 14 mini-albums.
  7 · B1·7 · C headline major stadiums (SoFi y MetLife).
  8 · B1·8 · A 2015: «debuted in 2015». 2018 y 2019 no están en el texto.
  9 · B2·1 · A Spain's capital city (Madrid).
 10 · B2·2 · C The Colombian athlete riding for Movistar Team.
 11 · B2·3 · B twenty-one: «across 21 stages».
 12 · B2·4 · C 1987.
 13 · B2·5 · A Lagos de Covadonga: «the climb to Lagos de Covadonga, where he took the leader's red
      jersey». Mont Ventoux y Sierra Nevada no están en el texto.
 14 · B2·6 · A The British cyclist associated with Team Sky (Froome, «who finished second»; el
      texto no dice que sea británico: Corrección EDUCATE).
 15 · B2·7 · B exactly two (Quintana 1.º y Chaves 3.º).
 16 · B2·8 · C More than three hundred million viewers worldwide.

Reparto de las 16: A 6 · B 4 · C 6. Equilibrado.

Correcciones EDUCATE impresas:
  9 (primera del Bloque 2) · el texto dice que 2016 fue la primera vez que dos colombianos
      compartieron el podio de la Vuelta: falso (1989: Parra 2.º, Vargas 3.º). Lo verdadero
      (aprobado por Nelson): 2016 fue la primera vez que un colombiano ganó la Vuelta con otro
      colombiano en el podio. No cambia ninguna clave.
  8 · falta «in» en «reflected topping global charts» (último renglón del texto de TWICE).
 14 · una opción le pone a Froome una nacionalidad que el texto no dice: tacharla y decidir con el
      equipo y el puesto (sin decir cuál opción).
No se imprimen: «three full albums and two LP» (6, distractor mal construido, no engaña hacia una
respuesta errada; va a la editorial) y «Final de lA Misión» (es la capa de texto del PDF: impreso
se ve «FINAL DE LA MISIÓN» en versalitas; Atención).

Hojas (8 de taller + 2 ICFES):
  311 t1 (1-2) · 312 t2 (3-4) · 313 t3 (5-6) · 314 t4 (7-8) · 315 ing4_i1 ·
  316 t5 (9-10) · 317 t6 (11-12) · 318 t7 (13-14) · 319 t8 (15-16) · 320 ing4_i2.
"""
from taller_base import *
from ing_diario import correccion, ctx_ok

configurar("Inglés", 4, "lectura",
           tema="Parte 5 · Lo que el texto dice, dato por dato",
           prefijo="Subestrategia", n_hojas=8)
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
def o1(b, x, y, w, h):
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
def o4(b, x, y, w, h):
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
def o5(b, x, y, w, h):
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
def o6(b, x, y, w, h):
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
def o7(b, x, y, w, h):
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
def o9(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Mismo lugar, otro nombre", c,
                      "Las opciones casi nunca copian el texto: lo dicen con otras palabras. Copia lo que dice el texto, "
                      "escribe en cada postal cómo lo dice cada opción y decide si es el mismo lugar. A veces hace falta "
                      "un dato que ya sabes del mundo.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "1. According to the passage, where did the cycling event conclude in 2016?", c)
    yy += 22
    caja(b, x0, yy, ww, 96, c, sw=2.4, r=14)
    rot(b, x0 + 20, yy + 30, "EL TEXTO DICE (CÓPIALO DE LA PRIMERA LÍNEA)", c, size=14)
    texto(b, x0 + 20, yy + 72, "the Vuelta a España ended in", size=19, weight="700")
    renglon(b, x0 + 300, yy + 74, x0 + ww - 20)
    yy += 116
    pw = (ww - 2 * 20) / 3
    for k, L in enumerate("ABC"):
        bx = x0 + k * (pw + 20)
        b.append(rect(bx, yy, pw, 196, tinte(c, 0.97), r=6, stroke=c, sw=2))
        b.append(rect(bx + pw - 58, yy + 12, 44, 52, "white", r=4, stroke=c, sw=1.6, dash="4,3"))
        b.append(f'<circle cx="{bx + 30}" cy="{yy + 32}" r="17" fill="white" stroke="{c}" stroke-width="2.2"/>')
        texto(b, bx + 30, yy + 38, L, size=17, color=c, weight="700", anchor="middle")
        pista(b, bx + 58, yy + 38, "el lugar que nombra:")
        renglon(b, bx + 18, yy + 84, bx + pw - 70)
        pista(b, bx + 18, yy + 116, "lo que tuve que saber del mundo:")
        renglon(b, bx + 18, yy + 150, bx + pw - 18)
        pista(b, bx + 18, yy + 182, "¿el mismo lugar del texto?")
        marca(b, bx + pw - 150, yy + 166, c, "sí")
        marca(b, bx + pw - 80, yy + 166, c, "no")
    yy += 214
    return correccion(b, x0, yy, ww,
                      "Antes de leer el texto del Bloque 2: dice que 2016 fue «the first time two Colombians "
                      "shared the final podium». No es cierto: ya había pasado en 1989 (Fabio Parra fue 2.º y Óscar "
                      "de Jesús Vargas 3.º). Lo que sí pasó por primera vez en 2016 fue que un colombiano ganara la "
                      "Vuelta con otro colombiano en el podio. Corrige esa frase a lápiz en tu libro. Para responder, "
                      "usa lo que dice el texto: ninguna clave cambia.")


# ───────── P7 · B2·2 · el título general ─────────
def o10(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Las palabras de la pregunta, buscadas con otro nombre", c,
                      "La pregunta no usa las mismas palabras del texto. Tiende un puente desde cada pedazo de la pregunta "
                      "hasta la frase del texto que quiere decir lo mismo. Si no encuentras el pedazo, no encuentras la "
                      "respuesta.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "2. Who managed to win the overall title in that year's competition?", c)
    yy += 22
    lw_ = 330
    for k, p in enumerate(("managed to win", "the overall title", "that year's competition")):
        by = yy + k * 92
        b.append(rect(x0, by, lw_, 74, tinte(c, 0.93), r=12, stroke=c, sw=2.2))
        texto(b, x0 + 18, by + 44, p, size=19, weight="700")
        bx0, bx1 = x0 + lw_ + 8, x0 + lw_ + 120
        b.append(f'<path d="M {bx0} {by + 37} Q {(bx0 + bx1) / 2} {by + 6} {bx1} {by + 37}" fill="none" '
                 f'stroke="{c}" stroke-width="2.4"/>')
        b.append(line(bx0, by + 37, bx1, by + 37, c, 2.4))
        caja(b, bx1 + 8, by, ww - lw_ - 128, 74, c, r=12)
        pista(b, bx1 + 26, by + 26, "en el texto se dice… (y en qué línea)")
        renglon(b, bx1 + 26, by + 60, x0 + ww - 18)
    yy += 3 * 92 + 4
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
def o12(b, x, y, w, h):
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
def o14(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El podio, escalón por escalón", c,
                      "Los tres del podio están en el texto, así que las tres opciones pueden describir a alguien real. "
                      "Sube a cada uno a su escalón con lo que el texto dice de él y mira cuál escalón te preguntan.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "6. Which competitor arrived second in the general standings?", c)
    yy += 24
    pw = 330
    alturas = {1: 170, 2: 130, 3: 100}
    orden = (2, 1, 3)
    base = yy + 280
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
        pista(b, bx + pw / 2, base - ph + 78, "lo dice el texto en:", size=13, anchor="middle")
        renglon(b, bx + 30, base - 14, bx + pw - 30)
    yy = base + 22
    yy = trampa(b, x0, yy, ww, "Que sea alguien del podio no basta:",
                "una opción puede describir bien a un corredor que sí está en el texto, pero en otro escalón. "
                "Antes de marcar, mira tu podio: ¿cuál escalón te preguntan y qué frase del texto lo dice?", c)
    return correccion(b, x0, yy + 14, ww,
                      "Una de las opciones le pone a un corredor una nacionalidad que el texto no dice (el texto "
                      "solo dice de qué equipo es). En una pregunta de lectura literal solo cuenta lo que está en el "
                      "texto: tacha esa palabra en tu libro y decide con lo demás que dice la opción (el equipo, el "
                      "puesto).")


# ───────── P10 · B2·7 · los colombianos del podio ─────────
def o15(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Lista de todos los nombres del texto", c,
                      "Para contar bien, primero se hace la lista completa. Encuentra el ancla de la pregunta en el "
                      "texto; después llena una ficha por cada persona que nombra el texto (puede sobrar alguna).")
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
    fw = (ww - 4 * 16) / 5
    for k in range(5):
        bx = x0 + k * (fw + 16)
        b.append(rect(bx, yy, fw, 280, "white", r=14, stroke=c, sw=2.2))
        b.append(f'<circle cx="{bx + fw / 2}" cy="{yy + 40}" r="24" fill="{tinte(c, 0.9)}" stroke="{c}" stroke-width="2"/>')
        for j_, lab in enumerate(("nombre:", "de dónde es:", "¿de qué año?")):
            ly = yy + 92 + j_ * 46
            pista(b, bx + 14, ly, lab, size=14)
            renglon(b, bx + 14, ly + 30, bx + fw - 14)
        pista(b, bx + 14, yy + 236, "¿en el último podio?", size=14)
        marca(b, bx + 14, yy + 246, c, "sí", size=15)
        marca(b, bx + 90, yy + 246, c, "no", size=15)
    yy += 300
    yy = frase_hueco(b, x0, yy, ww, "Colombianos con «sí» en «¿en el último podio?»: ______ .", c)
    yy += 16
    return ojo(b, x0, yy, ww, "LA PREGUNTA DICE «THE LAST PODIUM»",
               "Antes de contar, revisa de qué año habla el texto en cada nombre: la pregunta es por el último "
               "podio, no por toda la historia del ciclismo colombiano.")



# ═════════ instrumentos nuevos de la v3 (las 6 preguntas que antes no se trabajaban) ═════════

# ───────── P2 · B1·2 · Melbourne ─────────
def n2(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Dos boletas, dos ciudades", c,
                      "El texto anuncia conciertos en dos ciudades. Llena una boleta por ciudad con lo que dice el texto: "
                      "el estadio y las dos noches. Después mira de quién son las fechas que te preguntan.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "2. The concerts on November 8th and 9th will take place in:", c)
    yy += 30
    bw = (ww - 30) / 2
    for k in range(2):
        bx = x0 + k * (bw + 30)
        b.append(rect(bx, yy, bw, 250, tinte(c, 0.96), r=14, stroke=c, sw=2.4))
        b.append(line(bx + bw - 120, yy + 14, bx + bw - 120, yy + 236, c, 2, dash="6,6"))
        rot(b, bx + 20, yy + 32, f"TICKET {k + 1} · TWICE · THIS IS FOR", c, size=14)
        for j, lab in enumerate(("city:", "arena:", "nights:")):
            ly = yy + 90 + j * 56
            pista(b, bx + 20, ly, lab)
            renglon(b, bx + 90, ly + 2, bx + bw - 140)
        texto(b, bx + bw - 60, yy + 110, "N.º", size=15, color=c, weight="700", anchor="middle")
        b.append(rect(bx + bw - 94, yy + 124, 68, 44, "white", r=8, stroke=c, sw=1.8))
        pista(b, bx + bw - 60, yy + 200, "en orden", anchor="middle", size=13)
    yy += 272
    yy = frase_hueco(b, x0, yy, ww, "Las fechas de la pregunta están en la boleta ____ ; la palabra que las une a su ciudad: __________ .", c, size=17)
    yy += 16
    return trampa(b, x0, yy, ww, "Una ciudad puede estar en el texto y no tener esas fechas:",
                  "la otra ciudad de la gira también es verdad, pero tiene sus propias noches. Y si una opción nombra "
                  "una ciudad que no aparece en ninguna boleta, el texto no la dice.", c)


# ───────── P3 · B1·3 · 360-degree stage ─────────
def n3(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Desde todos los ángulos: dibujo el escenario", c,
                      "El texto describe el escenario con una frase técnica y después la explica con otras palabras. "
                      "Dibuja lo que entiendes visto desde arriba y decide si el escenario se mueve o si lo que cambia es "
                      "dónde está el público.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "3. The special stage design announced for the tour is:", c)
    yy += 16
    yy = pregunta_en(b, x0, yy, ww, "… all venues featuring a state-of-the-art 360-degree stage design that allows fans "
                                    "to see the performance from every angle.", c,
                     rotulo="LO QUE DICE EL TEXTO · SUBRAYA LA PARTE QUE EXPLICA")
    yy += 20
    sw_ = 440
    b.append(rect(x0, yy, sw_, 300, "white", r=16, stroke=c, sw=2.2, dash="8,6"))
    rot(b, x0 + 20, yy + 30, "VISTO DESDE ARRIBA", c, size=14)
    b.append(f'<circle cx="{x0 + sw_ / 2}" cy="{yy + 160}" r="44" fill="{tinte(c, 0.85)}" stroke="{c}" stroke-width="2.4"/>')
    pista(b, x0 + sw_ / 2, yy + 166, "stage", anchor="middle")
    pista(b, x0 + sw_ / 2, yy + 284, "dibuja dónde se sientan los fans", anchor="middle")
    rx, rw = x0 + sw_ + 30, ww - sw_ - 30
    for k, (tit, ps) in enumerate((("360-DEGREE", "¿cuántos grados tiene una vuelta completa? ¿qué forma dibuja?"),
                                   ("FROM EVERY ANGLE", "¿desde dónde pueden ver los fans?"),
                                   ("¿SE MUEVE?", "¿el texto dice en alguna parte que el escenario gira?"))):
        by = yy + k * 102
        caja(b, rx, by, rw, 90, c, r=12)
        rot(b, rx + 18, by + 28, tit, c, size=13)
        pista(b, rx + 18, by + 52, ps)
        renglon(b, rx + 18, by + 78, rx + rw - 18)
    yy += 320
    return ojo(b, x0, yy, ww, "UNA OPCIÓN PUEDE SONAR A LO MISMO SIN SERLO",
               "360 grados hace pensar en algo que da vueltas. Pero lo literal es lo que el texto dice que pasa: "
               "léelo otra vez y comprueba si lo que gira es el escenario o la mirada del público.")


# ───────── P8 · B1·8 · debuted ─────────
def n8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Debut, debutar, debutó: el ancla cambia de forma", c,
                      "La palabra ancla puede aparecer en el texto con otra forma (otro tiempo, otra terminación). "
                      "Completa la escalera de la palabra, encuéntrala en el texto y copia lo que tiene pegado.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "8. TWICE debuted in the year", c)
    yy += 24
    pasos = (("a debut", "sustantivo"), ("to debut", "verbo"), ("debuted", "pasado"))
    pw = (ww - 2 * 50) / 3
    for k, (pal, ps) in enumerate(pasos):
        bx = x0 + k * (pw + 50)
        by = yy + (2 - k) * 34
        caja(b, bx, by, pw, 118, c, r=12, fill=tinte(c, 0.96))
        texto(b, bx + 18, by + 38, pal, size=21, weight="700")
        pista(b, bx + 18 + tw(pal, 21, "700") + 14, by + 37, ps)
        pista(b, bx + 18, by + 70, "en español:")
        renglon(b, bx + 18, by + 104, bx + pw - 18)
        if k < 2:
            flecha(b, bx + pw + 6, by + 40, bx + pw + 44, by + 6, c, head=9)
    yy += 190
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL ANCLA EN EL TEXTO", c, size=14)
    pista(b, x0 + 20, yy + 66, "¿en qué párrafo está? ¿con qué palabras empieza esa oración?")
    renglon(b, x0 + 470, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 108, "las palabras que tiene pegadas, copiadas tal cual:")
    renglon(b, x0 + 380, yy + 110, x0 + ww - 20)
    pista(b, x0 + 20, yy + 138, "(si un número de una opción no está escrito en el texto, no es literal)")
    yy += 168
    return correccion(b, x0, yy, ww,
                      "En la última oración de ese mismo párrafo («Their widespread fame is further reflected topping "
                      "global charts…») falta una palabra: debe decir «reflected in topping global charts». Escríbela a "
                      "lápiz en tu libro. No cambia ninguna respuesta.")


# ───────── P11 · B2·3 · twenty-one stages ─────────
def n11(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "21 = twenty-one: el número cambia de traje", c,
                      "El texto escribe los números con cifras y las opciones los escriben con letras. Antes de comparar, "
                      "vístelos igual: pasa a letras los números del texto y a cifras los de las opciones.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "3. How many stages were included in the edition held in 2016?", c)
    yy += 24
    half = (ww - 60) / 2
    rot(b, x0, yy + 16, "DEL TEXTO · EN CIFRAS → EN LETRAS", c, size=14)
    rot(b, x0 + half + 60, yy + 16, "DE LAS OPCIONES · EN LETRAS → EN CIFRAS", c, size=14)
    yy += 30
    for k, (n_, lab) in enumerate((("21", "stages"), ("3,200", "kilometers"), ("83", "hours"))):
        by = yy + k * 76
        b.append(rect(x0, by, 120, 60, tinte(c, 0.93), r=10, stroke=c, sw=2))
        texto(b, x0 + 60, by + 38, n_, size=22, weight="700", anchor="middle")
        pista(b, x0 + 136, by + 36, lab)
        renglon(b, x0 + 146 + tw(lab, 15, "400", "italic"), by + 40, x0 + half)
    for k, lab in enumerate(("twenty", "twenty-one", "twenty-two")):
        by = yy + k * 76
        bx = x0 + half + 60
        texto(b, bx, by + 38, lab, size=20, weight="700")
        flecha(b, bx + 120, by + 32, bx + 160, by + 32, c, head=9)
        b.append(rect(bx + 172, by + 8, 100, 50, "white", r=10, stroke=c, sw=2))
        pista(b, bx + 290, by + 30, "¿en el texto?", size=14)
        marca(b, bx + 290, by + 38, c, "sí", size=14)
        marca(b, bx + 358, by + 38, c, "no", size=14)
    yy += 3 * 76 + 10
    caja(b, x0, yy, ww, 120, c, r=14)
    rot(b, x0 + 20, yy + 30, "CADA CIFRA CON SU DUEÑO", c, size=14)
    pista(b, x0 + 20, yy + 66, "el número que el texto pega a «stages»:")
    b.append(rect(x0 + 300, yy + 42, 110, 40, "white", r=8, stroke=c, sw=2))
    pista(b, x0 + 440, yy + 66, "el de los kilómetros y el de las horas no son de etapas: ¿de qué son?")
    renglon(b, x0 + 20, yy + 104, x0 + ww - 20)
    yy += 138
    return ojo(b, x0, yy, ww, "CON GUION ENTRE LAS DECENAS Y LAS UNIDADES",
               "En inglés, del 21 al 99 los números compuestos llevan guion: thirty-five, forty-eight, ninety-nine. "
               "Si lees despacio el guion, no confundes dos números que empiezan igual.")


# ───────── P13 · B2·5 · Lagos de Covadonga ─────────
def n13(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La camiseta del líder: una frase que dice otra cosa", c,
                      "La pregunta habla de «secure leadership»; el texto no usa esa palabra. Dice lo mismo con una "
                      "imagen del ciclismo: una camiseta. Descifra la imagen y tiende el puente.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "5. Which particular climb allowed Quintana to secure leadership?", c)
    yy += 22
    jx, jy = x0 + 40, yy + 10
    pts = [(jx + 60, jy), (jx + 120, jy), (jx + 132, jy + 16), (jx + 180, jy + 30), (jx + 200, jy + 90),
           (jx + 160, jy + 100), (jx + 156, jy + 260), (jx + 24, jy + 260), (jx + 20, jy + 100),
           (jx - 20, jy + 90), (jx, jy + 30), (jx + 48, jy + 16)]
    b.append('<polygon points="' + " ".join(f"{a:.0f},{bb:.0f}" for a, bb in pts) +
             f'" fill="{tinte(EDU_ROJO, 0.82)}" stroke="{EDU_ROJO}" stroke-width="2.6" stroke-linejoin="round"/>')
    pista(b, jx + 90, jy + 296, "red jersey", anchor="middle")
    rx, rw = x0 + 290, ww - 290
    for k, (tit, ps) in enumerate((("EN EL TEXTO", "copia la frase donde aparece la camiseta roja:"),
                                   ("LA IMAGEN DESCIFRADA", "«took the leader's red jersey» quiere decir que…"),
                                   ("EL PUENTE", "«secure leadership» se parece a… (¿lo mismo?)"))):
        by = yy + k * 104
        caja(b, rx, by, rw, 92, c, r=12)
        rot(b, rx + 18, by + 28, tit, c, size=13)
        pista(b, rx + 18, by + 52, ps)
        renglon(b, rx + 18, by + 80, rx + rw - 18)
    yy += 3 * 104 + 6
    yy = frase_hueco(b, x0, yy, ww, "Donde tomó la camiseta, el texto nombra el lugar: ____________________ (línea ____ ).", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una montaña famosa no es una montaña del texto:",
                  "si una opción nombra una subida que no aparece en el texto, por real y famosa que sea, no sirve: la "
                  "pregunta es por lo que dice este texto. Busca el nombre en el texto antes de marcarla.", c)


# ───────── P16 · B2·8 · 300 million ─────────
def n16(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Aproximado no es inventado: la regla de los millones", c,
                      "«Approximately» pide un número cercano al del texto, no uno cualquiera. Ubica en la regla el número "
                      "del texto y el de cada opción. Después revisa si la opción dice lo mismo que el texto con otras "
                      "palabras.")
    x0, ww = x + 22, w - 44
    yy = pregunta_en(b, x0, yy, ww, "8. Approximately, how many spectators followed the event globally?", c)
    yy += 50
    ly = yy + 40
    rx0, rx1 = x0 + 60, x0 + ww - 60
    b.append(line(rx0, ly, rx1, ly, c, 4))
    for k in range(5):
        px = rx0 + k * (rx1 - rx0) / 4
        b.append(line(px, ly - 14, px, ly + 14, c, 3))
        texto(b, px, ly + 44, f"{k * 100} million" if k else "0", size=16, color=c, weight="700", anchor="middle")
    pista(b, x0, ly - 40, "marca con T el número del texto y con A, B y C el de cada opción:")
    yy = ly + 74
    bw = (ww - 40) / 3
    for k, t_ in enumerate(("spectators", "globally", "followed the event")):
        bx = x0 + k * (bw + 20)
        caja(b, bx, yy, bw, 110, c, r=12)
        texto(b, bx + 18, yy + 36, t_, size=19, weight="700")
        pista(b, bx + 18, yy + 64, "en el texto se dice:")
        renglon(b, bx + 18, yy + 96, bx + bw - 18)
    yy += 130
    caja(b, x0, yy, ww, 140, c, r=14)
    rot(b, x0 + 20, yy + 30, "«MORE THAN» Y «APPROXIMATELY»", c, size=14)
    pista(b, x0 + 20, yy + 66, "«more than» quiere decir:")
    renglon(b, x0 + 210, yy + 68, x0 + ww / 2 - 20)
    pista(b, x0 + ww / 2, yy + 66, "¿qué opción usa la misma expresión que el texto?")
    renglon(b, x0 + ww / 2 + 330, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 106, "los números de las otras opciones, ¿aparecen en algún lugar del texto?")
    renglon(b, x0 + 520, yy + 108, x0 + ww - 20)
    return yy + 140


L3 = "ABC"


def _q(n, est, bloque, k, tema_, paso, inst):
    ctx = ctx_ok(f"Bloque {bloque}, n.º {k} del libro · {tema_} · {paso}")
    return dict(n=n, est=est, pag=447 if bloque == 1 else 448, ctx=ctx, inst=inst, letras=L3)


Q = {1: _q(1, 1, 1, 1, "TWICE", "paso 1, el ancla", o1),
     2: _q(2, 4, 1, 2, "TWICE", "paso 4, ¿responde?", n2),
     3: _q(3, 3, 1, 3, "TWICE", "paso 3, la frase vecina", n3),
     4: _q(4, 2, 1, 4, "TWICE", "paso 2, cada fecha", o4),
     5: _q(5, 4, 1, 5, "TWICE", "paso 4, ¿responde?", o5),
     6: _q(6, 2, 1, 6, "TWICE", "paso 2, cada número", o6),
     7: _q(7, 1, 1, 7, "TWICE", "paso 1, el ancla disfrazada", o7),
     8: _q(8, 1, 1, 8, "TWICE", "paso 1, el ancla cambia de forma", n8),
     9: _q(9, 3, 2, 1, "Nairo", "paso 4, otras palabras", o9),
     10: _q(10, 3, 2, 2, "Nairo", "paso 4, otras palabras", o10),
     11: _q(11, 2, 2, 3, "Nairo", "paso 2, cifras y letras", n11),
     12: _q(12, 2, 2, 4, "Nairo", "paso 2, cada año", o12),
     13: _q(13, 3, 2, 5, "Nairo", "paso 3, la frase vecina", n13),
     14: _q(14, 4, 2, 6, "Nairo", "paso 4, ¿responde?", o14),
     15: _q(15, 1, 2, 7, "Nairo", "paso 1, el ancla y la lista", o15),
     16: _q(16, 2, 2, 8, "Nairo", "paso 2, aproximado", n16)}


def build(pages=(311, 312, 313, 314, 316, 317, 318, 319)):
    out = []
    for k in range(8):
        out.append(hoja_taller(f"ing4_t{k + 1}", pages[k], k + 1, Q[2 * k + 1], Q[2 * k + 2]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
