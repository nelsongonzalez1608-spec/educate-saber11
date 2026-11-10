#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 3 · Parte 4 del ICFES · componente gramatical · léxico · páginas 289–310.

Decisión de Nelson (7 nov 2026): en Inglés el cuaderno trabaja TODAS las preguntas del libro, una
tarjeta por pregunta, cada una con su subestrategia y su propio instrumento. La v1 (10 tarjetas)
queda en ing3_v1.py como respaldo; la v2 en tablas se descartó («se ven como tablas»).

Libro fuente: «PRUEBA DE CAMPO MISIÓN 3» de Inglés (fuente_libro/INGLÉS), páginas 435–437. Cuatro
textos con 40 espacios (más el ejemplo 0), todos con tres opciones (A–C):
    texto 1 · Karol G en Medellín                    espacios  1–10   p. 435
    texto 2 · Spider-Man: Across the Spider-Verse    espacios 11–20   p. 435 (opciones en la 436)
    texto 3 · AI in the Classroom                    espacios 21–30   p. 436
    texto 4 · Public Protest and Social Change       espacios 31–40   p. 437
El libro numera los espacios del 1 al 40 sin reiniciar: pregunta n del cuaderno = espacio n.

Estrategia de la Parte 4: «Escucha a los vecinos del hueco», en cuatro pasos (la línea de contexto
de cada tarjeta dice cuál ejercita): 1 leo el texto entero (de qué trata, en qué tiempo va) ·
2 tapo las opciones y pregunto qué pieza falta · 3 busco la pista en las palabras vecinas ·
4 llamo a la subestrategia, marco y digo qué tan seguro estoy.

Claves verificadas (resueltas a mano contra el texto del libro, 7 nov 2026; coinciden con las 40 del
docstring de la v2):

    Texto 1 ·  1·C came   2·A began   3·B sang   4·C knew   5·B were   6·A presented   7·C lasted
               8·B shared   9·A thought   10·C was
    Texto 2 · 11·B was   12·A* was released (corregida)   13·C went   14·C introduced   15·A used
              16·C were   17·B combined*   18·A dealt*   19·C tried*   20·B left*
    Texto 3 · 21·A among   22·B for   23·C on   24·A by*   25·B because   26·C by   27·A with
              28·C for   29·B to   30·A for
    Texto 4 · 31·B in   32·— (ninguna; va «in»)   33·C across   34·C because*   35·A through*
              36·C Despite   37·B with   38·A but also   39·C since*   40·A undeniable

    * espacio con Corrección EDUCATE impresa (ver abajo); la letra es la que espera el libro.

  10 · was: «the night» es una sola cosa y la oración pequeña va en el reloj de «thought».
  12 · con la opción A corregida («was released»), es la voz pasiva: la película no estrena, la
       estrenan. B («It released in cinemas») es un uso informal; aceptarlo solo si se defiende.
  17 · combined es la esperada (reloj de 2023); combines se defiende: es lo que la historia sigue
       siendo hoy («the story, which combines…»). combine no concuerda con «the story».
  29 · to: después viene un verbo sin marca (succeed): essential to + verbo. El mismo texto trae el
       molde «use them to practice».
  40 · undeniable: entre un artículo y un sustantivo va un adjetivo. Atención: el «an» descarta solo
       la opción C (deny); es dato para el profe, no se imprime.

Reparto de las 39 con clave del libro (12 cuenta como A corregida): A 13 · B 11 · C 15. Equilibrado.

Correcciones EDUCATE impresas en la tarjeta (sin dar la clave):
    12      la opción A está mal escrita («was release» → «was released»): se corrige a lápiz.
    17      se defienden dos tiempos (pasado del relato / presente de lo que la historia es).
    18–20   valen pasado y presente narrativo: escoger un reloj en la 18 y sostenerlo hasta la 20.
    24      by, with y through se defienden las tres.
    32      ninguna opción sirve: no se marca letra; se escribe la palabra que va.
    34      as, since y because son correctas las tres.
    35      dos opciones correctas (through y on); el libro espera una.
    39      dos se defienden (since: la razón; but: una condición más).
    33 (through también se defiende, pero across es la natural) y 40 (el «an») quedan como
    «Atención» para el profe: no se imprimen.

Subestrategias (nombres y colores de la v1; las hojas ICFES 299 y 310 los usan):
    1 · El reloj del texto            azul    1 2 4 6 7 9 11 14 15 17 18 20          · ICFES ex. 1 · 10
    2 · La forma que cabe             rojo    3 5 8 10 12 13 16 19 29 40             · ICFES ex. 1 · 13
    3 · La preposición viene pegada   oro     21 22 23 24 26 27 28 30 31 32 33 35 37 · ICFES ex. 2 · 24
    4 · El conector dice la relación  morado  25 34 36 38 39                         · ICFES ex. 1 · 16

Hojas: 289–298 ing3_t1…t10 (preguntas 1–20) · 299 ing3_i1 · 300–309 ing3_t11…t20 (21–40) ·
       310 ing3_i2.
"""
from taller_base import *

configurar("Inglés", 3, "gramatical · léxico",
           tema="Parte 4 · Escucha a los vecinos del hueco",
           nota="LO QUE ME DIJO LA ORACIÓN", prefijo="Subestrategia", n_hojas=20)
MORADO = "#5B3E96"
EST = {1: ("El reloj del texto", EDU_AZUL),
       2: ("La forma que cabe", EDU_ROJO),
       3: ("La preposición viene pegada", EDU_ORO),
       4: ("El conector dice la relación", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))
CORR = "#2F3A4A"          # Corrección EDUCATE: pizarra, distinta de los cuatro colores
CORR_BG = "#EEF1F5"

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
    """Casilla y su rótulo; devuelve el x donde termina."""
    b.append(checkbox(x, y, s=10, c=c))
    b.append(T(x + 28, y + 17, [lab], size, GRAY))
    return x + 28 + tw(lab, size) + 30


def frase_hueco(b, x, y, w, txt, c, h=54, size=18):
    caja(b, x, y, w, h, c)
    b.append(T(x + 22, y + h / 2 + 7, [txt], size, INK, weight="700"))
    return y + h


def cita(b, x, y, w, txt, c, rotulo="ASÍ DICE TU LIBRO"):
    """El fragmento en inglés, tal como está en el libro, con el espacio numerado."""
    svg, yy = TJ(x + 30, y + 40, txt, w - 60, 20, INK, lh=30)
    h = yy - y + 8
    b.append(rect(x, y, w, h, tinte(c, 0.93), r=12))
    b.append(rect(x, y, 8, h, c, r=4))
    rot(b, x + 30, y + 28, rotulo, c, size=13)
    b.append(svg)
    return y + h


def tabla_vacia(b, x, y, cols, heads, filas, c, rh=58, hh=46, size=17, sin_renglon=()):
    """Encabezado con tinte, primera columna con rótulos y el resto con renglones."""
    ww = sum(cols)
    caja(b, x, y, ww, hh, c, fill=tinte(c), r=8)
    cx = x
    for k, hd in enumerate(heads):
        if hd:
            rot(b, cx + 14, y + hh / 2 + 6, hd, c, size=13)
        cx += cols[k]
    ry = y + hh
    for f in filas:
        caja(b, x, ry, ww, rh, c, r=0)
        texto(b, x + 14, ry + rh / 2 + 6, f, size=size, weight="700")
        cx = x + cols[0]
        for k in range(1, len(cols)):
            if k not in sin_renglon:
                renglon(b, cx + 14, ry + rh - 14, cx + cols[k] - 14)
            cx += cols[k]
        ry += rh
    cx = x
    for k in range(len(cols) - 1):
        cx += cols[k]
        b.append(line(cx, y, cx, ry, c, 1.6))
    return ry



# ───────── piezas de la misión 3 (versión de 40 tarjetas) ─────────
TEXTOS = {1: "TEXTO 1 · KAROL G EN MEDELLÍN",
          2: "TEXTO 2 · SPIDER-MAN: ACROSS THE SPIDER-VERSE",
          3: "TEXTO 3 · AI IN THE CLASSROOM",
          4: "TEXTO 4 · PUBLIC PROTEST AND SOCIAL CHANGE"}


def texto_de(n):
    return 1 + (n - 1) // 10


def rotulo_cita(n):
    t = texto_de(n)
    if t == 2:
        return TEXTOS[2] + " · LAS OPCIONES ESTÁN EN LA PÁGINA 436"
    return TEXTOS[t] + " · ASÍ DICE TU LIBRO"


def abre(b, x, y, w, c, n, titulo, sub, frag):
    """Título del instrumento y el fragmento del libro con el texto del que viene."""
    yy = titulo_instr(b, x, y, titulo, c, sub)
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, frag, c, rotulo=rotulo_cita(n))
    return x0, ww, yy


def idea_texto(b, x, y, w, c):
    """Primera tarjeta de cada texto: «mi primera idea del texto», antes de llenar nada."""
    h = 118
    caja(b, x, y, w, h, c, sw=2.2, fill=tinte(c, 0.95), r=14)
    rot(b, x + 20, y + 28, "MI PRIMERA IDEA DEL TEXTO", c, size=13)
    pista(b, x + 20 + tw("MI PRIMERA IDEA DEL TEXTO", 13, "700") + 1.5 * 25 + 16, y + 28,
          "léelo entero en tu libro antes de llenar un solo espacio")
    hw = (w - 60) / 2
    for k, lab in enumerate(("de qué trata, en una frase:", "en qué tiempo va y qué palabra me lo dijo:")):
        bx = x + 20 + k * (hw + 20)
        pista(b, bx, y + 62, lab)
        renglon(b, bx, y + 100, bx + hw)
    return y + h


def correccion(b, x, y, w, txt):
    """Corrección EDUCATE: qué está mal en el libro y qué hacer, sin dar la clave.
    Estilo B · Bitácora (10 nov): recuadro a mano y rótulo en Space Mono; mismo alto."""
    import bitacora as BT
    rotulo = "CORRECCIÓN EDUCATE"
    svg, yy = TJ(x + 30, y + 44, txt, w - 56, 17, INK, lh=25)
    h = yy - y + 14
    b.append(BT.wob_rect(x, y, w, h, CORR, 2.2, fill=CORR_BG, seed=int(y) + 5, amp=1.0))
    wr = BT.twf(rotulo, 14, BT.MONO, "700")
    b.append(BT.resaltador(x + 30, y + 12, wr, 20, BT.FOSFO, seed=int(y)))
    b.append(BT.TX(x + 30, y + 28, rotulo, 14, CORR, BT.MONO, "700"))
    pista(b, x + 30 + wr + 18, y + 28, "el libro tiene un problema en este espacio", size=14)
    b.append(svg)
    return y + h


def lab_linea(b, x, y, x2, lab, size=15):
    """Rótulo en cursiva y su renglón a continuación (medido con tw)."""
    pista(b, x, y, lab, size=size)
    renglon(b, x + tw(lab, size, style="italic") + 12, y + 2, x2)


def caja_rot(b, x, y, w, h, c, rotulo, sw=2, fill="white", r=14, size=13):
    caja(b, x, y, w, h, c, sw=sw, fill=fill, r=r)
    rot(b, x + 20, y + 28, rotulo, c, size=size)


def marcas(b, x, y, c, labs, size=16):
    """Varias casillas seguidas; devuelve el x donde termina la última."""
    for lab in labs:
        x = marca(b, x, y, c, lab, size=size)
    return x


def hueco_caja(b, x, y, w, c, h=40):
    b.append(rect(x, y, w, h, "white", r=8, stroke=c, sw=2))

# ───────── espacio 1 · came ─────────
def e1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La línea de tiempo del concierto de Medellín", c,
                      "Antes de mirar las opciones, decide cuándo pasa lo que cuenta el texto. La pista de tiempo "
                      "está escrita en la primera línea: encuéntrala, ponla en la línea y deja que ella escoja el verbo.")
    x0, ww = x + 22, w - 44
    yy = idea_texto(b, x0, yy, ww, c) + 16
    yy = cita(b, x0, yy, ww, "Last month, Karol G (0) gave a massive concert in Medellín, her hometown. "
                             "Thousands of fans (1) ________ to the stadium early in the morning.", c,
             rotulo=TEXTOS[1] + " · ASÍ DICE TU LIBRO")
    yy += 30
    # la línea de tiempo con tres zonas
    ly = yy + 40
    b.append(line(x0 + 10, ly, x0 + ww - 10, ly, c, 4))
    b.append(f'<polygon points="{x0 + ww - 10},{ly - 12} {x0 + ww + 8},{ly} {x0 + ww - 10},{ly + 12}" fill="{c}"/>')
    zw = (ww - 20) / 3
    zonas = (("ANTES · PASADO", "ya pasó"), ("AHORA · PRESENTE", "pasa siempre o hoy"),
             ("DESPUÉS · FUTURO", "todavía no pasa"))
    for k, (rt, ps) in enumerate(zonas):
        zx = x0 + 10 + k * zw
        if k:
            b.append(line(zx, ly - 22, zx, ly + 22, c, 3))
        rot(b, zx + zw / 2, ly - 18, rt, c, size=14, anchor="middle")
        pista(b, zx + zw / 2, ly + 40, ps, anchor="middle")
        caja(b, zx + 14, ly + 58, zw - 28, 126, c, r=12)
        pista(b, zx + 30, ly + 84, "pistas de tiempo que van aquí:", size=14)
        renglon(b, zx + 30, ly + 124, zx + zw - 30)
        renglon(b, zx + 30, ly + 164, zx + zw - 30)
    pista(b, x0 + 10, ly + 212, "Marca con una X en la línea dónde queda «Last month» y escribe la pista en su caja.")
    yy = ly + 234
    yy = frase_hueco(b, x0, yy, ww, "La pista de tiempo es ____________ ; el ejemplo (0) la confirma porque ____________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Que suene bien con «fans» no basta:",
                  "dos formas del verbo pueden concordar con un sujeto plural y aun así vivir en otro punto de la "
                  "línea. Pregúntale a cada opción en qué zona queda y quédate con la que cae donde marcaste la X.", c)


# ───────── espacio 5 · were ─────────
def e5(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La tabla del verbo to be, llenada por mí", c,
                      "Para escoger la forma de to be hay que pasar dos filtros: cuántos son y cuándo. Llena la tabla "
                      "con lo que sabes; después cruza la fila del sujeto con la columna del tiempo.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "People (5) ________ very excited because she also (6) ________ a new song for "
                             "the first time.", c,
             rotulo=TEXTOS[1] + " · ASÍ DICE TU LIBRO")
    yy += 22
    fw = (ww - 24) / 2
    for k, (rt, ps, ops) in enumerate((("FILTRO 1 · ¿CUÁNTOS SON?", "«People» cuenta como…", ("uno", "varios")),
                                       ("FILTRO 2 · ¿CUÁNDO?", "el texto va en…", ("pasado", "presente")))):
        bx = x0 + k * (fw + 24)
        caja(b, bx, yy, fw, 136, c, r=14)
        rot(b, bx + 20, yy + 30, rt, c, size=14)
        pista(b, bx + 20, yy + 60, ps)
        xx = bx + 20 + tw(ps, 15, style="italic") + 24
        for o in ops:
            xx = marca(b, xx, yy + 44, c, o)
        pista(b, bx + 20, yy + 98, "lo sé por:")
        renglon(b, bx + 100, yy + 100, bx + fw - 20)
    yy += 156
    cols = (300, (ww - 300) / 2, (ww - 300) / 2)
    yy = tabla_vacia(b, x0, yy, cols, ("QUIÉN", "PRESENTE · HOY", "PASADO · YA PASÓ"),
                     ("I", "he · she · it", "you · we · they"), c, rh=60)
    yy += 18
    yy = frase_hueco(b, x0, yy, ww, "Con los dos filtros me queda la fila __________ y la columna __________ .", c)
    yy += 16
    return ojo(b, x0, yy, ww, "OJO CON «PEOPLE»",
               "En español decimos «la gente estaba», en singular. En inglés «people» se usa como plural: piensa "
               "en «they». No te dejes llevar por cómo suena en español.")


# ───────── espacio 9 · thought ─────────
def e9(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El párrafo tiene un solo reloj: cuéntalo verbo por verbo", c,
                      "Un texto que cuenta una historia no cambia de tiempo a cada rato. Copia los verbos que ya "
                      "escogiste en los espacios 0 a 8 y marca en qué tiempo está cada uno. El conteo te dice la hora.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "…and at the end she (8) ________ a message of love and gratitude. Everyone "
                             "(9) ________ the night (10) ________ unforgettable.", c,
             rotulo=TEXTOS[1] + " · ASÍ DICE TU LIBRO")
    yy += 22
    cw = (ww - 2 * 18) / 3
    for k in range(9):
        col, fila = k % 3, k // 3
        bx, by = x0 + col * (cw + 18), yy + fila * 92
        caja(b, bx, by, cw, 78, c, r=12)
        b.append(f'<circle cx="{bx + 28}" cy="{by + 39}" r="16" fill="white" stroke="{c}" stroke-width="2.2"/>')
        texto(b, bx + 28, by + 45, str(k), size=16, color=c, weight="700", anchor="middle")
        renglon(b, bx + 58, by + 50, bx + cw - 150)
        b.append(checkbox(bx + cw - 132, by + 16, s=9, c=c))
        texto(b, bx + cw - 108, by + 31, "pasado", size=14, color=GRAY)
        b.append(checkbox(bx + cw - 132, by + 44, s=9, c=c))
        texto(b, bx + cw - 108, by + 59, "presente", size=14, color=GRAY)
    yy += 3 * 92 + 4
    yy = frase_hueco(b, x0, yy, ww, "De 9 verbos, ______ están en pasado. El reloj del párrafo marca: __________ .", c)
    yy += 16
    return ojo(b, x0, yy, ww, "«EVERYONE» ES UNA SOLA PERSONA",
               "«Everyone» quiere decir todos, pero en la gramática funciona como «he» o «she», igual que «todo el "
               "mundo» en español. Con eso descartas una forma; entre las que quedan decide el reloj, no el oído.")


# ───────── espacio 13 · went ─────────
def e13(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Las tres caras de cada verbo", c,
                      "Muchos verbos del inglés cambian de cara: una para hoy, otra para el pasado y otra que solo "
                      "sale acompañada de has, have, had o was. Llena las caras y mira qué hay justo antes del espacio.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "It (12) ________ in cinemas around the world and millions of people (13) ________ "
                             "to see it.", c,
             rotulo=rotulo_cita(13))
    yy += 20
    cols = (190, (ww - 190) / 3, (ww - 190) / 3, (ww - 190) / 3)
    yy = tabla_vacia(b, x0, yy, cols, ("VERBO", "1 · HOY", "2 · PASADO", "3 · CON HAS / HAVE / WAS"),
                     ("see", "go", "begin", "know"), c, rh=56)
    yy += 18
    caja(b, x0, yy, ww, 140, c, r=14)
    rot(b, x0 + 20, yy + 32, "JUSTO ANTES DEL ESPACIO 13", c, size=14)
    texto(b, x0 + 20, yy + 70, "¿Hay has, have, had o was?", size=17, color=INK)
    marca(b, x0 + 270, yy + 54, c, "sí")
    marca(b, x0 + 350, yy + 54, c, "no")
    texto(b, x0 + 470, yy + 70, "Entonces la cara 3 puede ir sola:", size=17, color=INK)
    marca(b, x0 + 760, yy + 54, c, "sí")
    marca(b, x0 + 840, yy + 54, c, "no")
    pista(b, x0 + 20, yy + 114, "Entre las dos caras que quedan, ¿cuál escoge el reloj del texto (In 2023…)?")
    renglon(b, x0 + 600, yy + 116, x0 + ww - 20)
    yy += 156
    return trampa(b, x0, yy, ww, "Hay una cara que nunca va sola:",
                  "la tercera cara (la del participio) necesita un auxiliar delante para funcionar como verbo. Si "
                  "en tu caja de arriba marcaste que no hay auxiliar, tacha esa cara antes de escoger.", c)


# ───────── espacio 15 · used ─────────
def e15(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos vagones enganchados por and", c,
                      "Cuando and engancha dos verbos del mismo sujeto, los dos vagones viajan en el mismo tiempo. "
                      "Llena el vagón 14 primero y copia su tiempo en el 15. Busca también el otro verbo que ya trae la "
                      "oración.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "The movie (14) ________ new characters and (15) ________ a unique animation style "
                             "that many critics admired.", c,
             rotulo=rotulo_cita(13))
    yy += 30
    # locomotora + dos vagones
    lw, vw, vh = 230, 400, 150
    caja(b, x0, yy, lw, vh, c, sw=2.6, r=18, fill=tinte(c, 0.88))
    rot(b, x0 + lw / 2, yy + 56, "EL SUJETO", c, size=14, anchor="middle")
    pista(b, x0 + lw / 2, yy + 84, "¿quién hace las", anchor="middle")
    pista(b, x0 + lw / 2, yy + 104, "dos acciones?", anchor="middle")
    renglon(b, x0 + 24, yy + 132, x0 + lw - 24)
    for k, n in enumerate(("14", "15")):
        vx = x0 + lw + 70 + k * (vw + 70)
        b.append(line(vx - 70, yy + vh / 2, vx, yy + vh / 2, c, 4))
        if k == 1:
            b.append(f'<circle cx="{vx - 35}" cy="{yy + vh / 2}" r="26" fill="white" stroke="{c}" stroke-width="2.6"/>')
            texto(b, vx - 35, yy + vh / 2 + 7, "and", size=17, color=c, weight="700", anchor="middle")
        caja(b, vx, yy, vw, vh, c, sw=2.6, r=18)
        rot(b, vx + 20, yy + 30, f"VAGÓN {n}", c, size=14)
        pista(b, vx + 20, yy + 64, "el verbo:")
        renglon(b, vx + 100, yy + 66, vx + vw - 20)
        pista(b, vx + 20, yy + 108, "su tiempo:")
        renglon(b, vx + 100, yy + 110, vx + vw - 20)
    ruedas = [x0 + 50, x0 + lw - 50]
    for k in range(2):
        vx = x0 + lw + 70 + k * (vw + 70)
        ruedas += [vx + 60, vx + vw - 60]
    for cxw in ruedas:
        b.append(f'<circle cx="{cxw:.0f}" cy="{yy + vh + 16}" r="15" fill="white" stroke="{c}" stroke-width="2.6"/>')
        b.append(f'<circle cx="{cxw:.0f}" cy="{yy + vh + 16}" r="4" fill="{c}"/>')
    yy += vh + 52
    caja(b, x0, yy, ww, 100, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL TERCER VERBO DE LA ORACIÓN, QUE YA ESTÁ ESCRITO", c, size=14)
    pista(b, x0 + 20, yy + 70, "lo copio:")
    renglon(b, x0 + 96, yy + 72, x0 + 520)
    pista(b, x0 + 560, yy + 70, "y está en el tiempo:")
    renglon(b, x0 + 710, yy + 72, x0 + ww - 20)
    yy += 116
    return ojo(b, x0, yy, ww, "Si los vagones no van al mismo tiempo, se descarrila la oración:",
               "revisa las tres opciones del espacio 15 con la pregunta «¿va en el mismo tiempo que el vagón 14?». "
               "Una forma puede ser correcta en otra oración y estar mal enganchada en esta.")


# ───────── espacio 22 · for ─────────
def e22(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "En español no hace falta; en inglés, sí", c,
                      "Hay verbos que en español van directo a la cosa y en inglés piden una preposición pegada. "
                      "Escribe en cada fila la que agrega el inglés. No se traduce palabra por palabra: se aprende con "
                      "el verbo.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "Many students use them to practice English, do homework, or search (22) ________ "
                             "information.", c,
             rotulo=TEXTOS[3] + " · ASÍ DICE TU LIBRO")
    yy += 22
    cols = (330, 380, ww - 710)
    filas = (("escuchar música", "listen ____ music"), ("mirar la pantalla", "look ____ the screen"),
             ("buscar información", "search ____ information"))
    caja(b, x0, yy, sum(cols), 46, c, fill=tinte(c), r=8)
    for k, hd in enumerate(("EN ESPAÑOL", "EN INGLÉS", "LA QUE AGREGA EL INGLÉS · DÓNDE LA HE VISTO")):
        rot(b, x0 + sum(cols[:k]) + 14, yy + 29, hd, c, size=13)
    ry = yy + 46
    for es, en in filas:
        caja(b, x0, ry, sum(cols), 66, c, r=0)
        texto(b, x0 + 14, ry + 40, es, size=18, color=GRAY, style="italic")
        texto(b, x0 + cols[0] + 14, ry + 40, en, size=19, weight="700")
        b.append(rect(x0 + cols[0] + cols[1] + 14, ry + 13, 90, 40, "white", r=8, stroke=c, sw=2))
        renglon(b, x0 + cols[0] + cols[1] + 124, ry + 50, x0 + sum(cols) - 14)
        ry += 66
    for k in (1, 2):
        b.append(line(x0 + sum(cols[:k]), yy, x0 + sum(cols[:k]), ry, c, 1.6))
    yy = ry + 22
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL VERBO Y SU PREPOSICIÓN, ESCRITOS COMO UNA SOLA PIEZA", c, size=14)
    texto(b, x0 + 20, yy + 76, "search", size=24, weight="700")
    b.append(rect(x0 + 104, yy + 46, 120, 44, "white", r=8, stroke=c, sw=2.2))
    pista(b, x0 + 250, yy + 76, "una frase mía en inglés con esta pieza:")
    renglon(b, x0 + 520, yy + 78, x0 + ww - 20)
    yy += 120
    return ojo(b, x0, yy, ww, "LA PREPOSICIÓN NO SE DEDUCE DEL ESPAÑOL",
               "«Buscar» no lleva nada en español, así que el español no te dice cuál poner. Pregúntate dónde has "
               "oído este verbo en inglés (un juego, una canción, una página web) y qué palabra venía pegada.")


# ───────── espacio 25 · because ─────────
def e25(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La flecha entre las dos mitades", c,
                      "Un conector dice qué hace la segunda mitad con la primera. Antes de mirar las opciones, lee las "
                      "dos mitades por separado y decide hacia dónde apunta la flecha.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "On the other hand, AI can be useful (25) ________ it helps students understand "
                             "complex topics.", c,
             rotulo=TEXTOS[3] + " · ASÍ DICE TU LIBRO")
    yy += 24
    mw = 430
    for k, (rt, en) in enumerate((("MITAD 1", "AI can be useful"),
                                  ("MITAD 2", "it helps students understand complex topics"))):
        bx = x0 if k == 0 else x0 + ww - mw
        caja(b, bx, yy, mw, 120, c, sw=2.4, r=16)
        rot(b, bx + 20, yy + 30, rt, c, size=14)
        svg, _ = TJ(bx + 20, yy + 44, en, mw - 40, 19, INK, weight="700", lh=26)
        b.append(svg)
    flecha(b, x0 + mw + 20, yy + 60, x0 + ww - mw - 20, yy + 60, c, sw=3, head=14)
    texto(b, x0 + ww / 2, yy + 44, "¿qué hace la 2 con la 1?", size=15, color=GRAY, anchor="middle", style="italic")
    yy += 140
    rels = ("la 2 dice POR QUÉ pasa la 1", "la 2 es lo que RESULTA de la 1", "la 2 va EN CONTRA de la 1")
    for k, r_ in enumerate(rels):
        marca(b, x0 + 20, yy + k * 40, c, r_, size=17)
    pista(b, x0 + 520, yy + 18, "la frase del texto que me lo dice:")
    renglon(b, x0 + 520, yy + 62, x0 + ww - 20)
    renglon(b, x0 + 520, yy + 104, x0 + ww - 20)
    yy += 132
    caja(b, x0, yy, ww, 96, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PRUEBA EN ESPAÑOL", c, size=14)
    texto(b, x0 + 20, yy + 70, "«La IA puede ser útil", size=18, style="italic")
    b.append(rect(x0 + 230, yy + 44, 150, 40, "white", r=8, stroke=c, sw=2))
    texto(b, x0 + 396, yy + 70, "ayuda a entender temas difíciles».", size=18, style="italic")
    pista(b, x0 + 700, yy + 70, "¿suena lógico? sí / no ·  ¿qué conector inglés dice eso?")
    yy += 112
    return trampa(b, x0, yy, ww, "Los tres conectores existen y son correctos en otra oración:",
                  "aquí no se pregunta si la palabra existe, sino si dice la relación que marcaste. Y el «On the other "
                  "hand» del comienzo responde al párrafo anterior, no a la segunda mitad de esta oración. Pon cada "
                  "opción en tu frase en español y quédate con la que no le cambia el sentido.", c)


# ───────── espacio 27 · with ─────────
def e27(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El puente entre technology y creativity", c,
                      "El verbo combine junta dos cosas. Dibuja qué queda a cada lado del puente y escribe en el puente "
                      "la palabra que las une. Esta vez pregúntale al español y después compruébalo en inglés.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "Some experts say that technology should be combined (27) ________ creativity and "
                             "human effort.", c,
             rotulo=TEXTOS[3] + " · ASÍ DICE TU LIBRO")
    yy += 26
    rr = 92
    cxl, cxr, cy = x0 + 150, x0 + ww - 150, yy + rr + 10
    for cx_, rt in ((cxl, "LADO 1"), (cxr, "LADO 2")):
        b.append(f'<circle cx="{cx_}" cy="{cy}" r="{rr}" fill="{tinte(c, 0.9)}" stroke="{c}" stroke-width="2.6"/>')
        rot(b, cx_, cy - 36, rt, c, size=14, anchor="middle")
        renglon(b, cx_ - 66, cy + 10, cx_ + 66)
        renglon(b, cx_ - 66, cy + 50, cx_ + 66)
    px0, px1 = cxl + rr + 10, cxr - rr - 10
    b.append(f'<path d="M {px0} {cy + 20} Q {(px0 + px1) / 2} {cy - 90} {px1} {cy + 20}" fill="none" '
             f'stroke="{c}" stroke-width="4"/>')
    b.append(line(px0, cy + 20, px1, cy + 20, c, 4))
    texto(b, (px0 + px1) / 2 - 90, cy - 4, "combined", size=22, weight="700", anchor="end")
    b.append(rect((px0 + px1) / 2 - 76, cy - 36, 152, 46, "white", r=8, stroke=c, sw=2.4))
    pista(b, (px0 + px1) / 2, cy + 50, "la palabra del puente", anchor="middle")
    yy = cy + rr + 24
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "PRIMERO EN ESPAÑOL, DESPUÉS EN INGLÉS", c, size=14)
    texto(b, x0 + 20, yy + 70, "En español diría: «combinar la tecnología", size=18, style="italic")
    b.append(rect(x0 + 380, yy + 44, 110, 40, "white", r=8, stroke=c, sw=2))
    texto(b, x0 + 506, yy + 70, "la creatividad».", size=18, style="italic")
    texto(b, x0 + 700, yy + 70, "¿Es la misma idea en inglés?", size=18)
    marca(b, x0 + 960, yy + 54, c, "sí")
    marca(b, x0 + 1040, yy + 54, c, "no")
    pista(b, x0 + 20, yy + 116, "Otra frase en inglés que conozco con combine y esa palabra:")
    renglon(b, x0 + 440, yy + 118, x0 + ww - 20)
    yy += 166
    return trampa(b, x0, yy, ww, "El español a veces ayuda y a veces engaña:",
                  "en el espacio 22 no te sirvió («buscar» no lleva nada). Aquí puede servir, pero no lo des por "
                  "hecho: la prueba es encontrar una frase en inglés que ya conozcas con ese verbo y esa palabra.", c)


# ───────── espacio 36 · Despite ─────────
def e36(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Lo que viene después del conector: ¿trae verbo o no?", c,
                      "Dos conectores pueden decir lo mismo y no caber en el mismo lugar. Primero decide la relación; "
                      "después mira qué viene entre el espacio y la coma. Esa mirada decide.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "(36) ________ these opportunities, online activism can also create new risks, such as "
                             "misinformation or polarization.", c,
             rotulo=TEXTOS[4] + " · ASÍ DICE TU LIBRO")
    yy += 22
    hw = (ww - 24) / 2
    caja(b, x0, yy, hw, 180, c, r=14)
    rot(b, x0 + 20, yy + 30, "PASO 1 · LA RELACIÓN", c, size=14)
    pista(b, x0 + 20, yy + 58, "«these opportunities» frente a «new risks»:")
    for k, lab in enumerate(("se oponen (contraste)", "una causa la otra", "se suman")):
        marca(b, x0 + 20, yy + 74 + k * 34, c, lab, size=16)
    bx = x0 + hw + 24
    caja(b, bx, yy, hw, 180, c, r=14)
    rot(b, bx + 20, yy + 30, "PASO 2 · ENTRE EL ESPACIO Y LA COMA", c, size=14)
    texto(b, bx + 20, yy + 66, "these opportunities", size=19, weight="700")
    pista(b, bx + 20, yy + 108, "¿tiene un verbo conjugado?")
    marca(b, bx + 230, yy + 92, c, "sí", size=16)
    marca(b, bx + 310, yy + 92, c, "no", size=16)
    pista(b, bx + 20, yy + 152, "entonces es:")
    marca(b, bx + 120, yy + 136, c, "una oración", size=16)
    marca(b, bx + 290, yy + 136, c, "solo un sustantivo", size=16)
    yy += 198
    cols = (ww / 3, ww / 3, ww - 2 * (ww / 3))
    heads = ("PIDE SUJETO + VERBO", "PIDE SOLO UN SUSTANTIVO", "VA SUELTO, CON COMA")
    caja(b, x0, yy, ww, 44, c, fill=tinte(c), r=8)
    for k, hd in enumerate(heads):
        rot(b, x0 + sum(cols[:k]) + 14, yy + 28, hd, c, size=13)
    caja(b, x0, yy + 44, ww, 110, c, r=0)
    for k in range(3):
        cx0 = x0 + sum(cols[:k])
        renglon(b, cx0 + 14, yy + 92, cx0 + cols[k] - 14)
        renglon(b, cx0 + 14, yy + 136, cx0 + cols[k] - 14)
        if k:
            b.append(line(cx0, yy, cx0, yy + 154, c, 1.6))
    pista(b, x0, yy + 178, "Clasifica aquí las tres opciones del libro y otros conectores de contraste que conozcas.")
    yy += 196
    return alto_profe(b, x0, yy, ww,
                      "Los conectores de contraste no se usan todos igual: unos van delante de una oración completa, "
                      "otros solo delante de un sustantivo y otros van sueltos con una coma. Pídele al profe que dé un "
                      "ejemplo de cada clase antes de que marques.")


# ───────── espacio 38 · but also ─────────
def e38(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Palabras que llegan en pareja", c,
                      "Algunos conectores vienen en dos partes: si aparece la primera, la segunda tiene que llegar "
                      "después. Encuentra en la oración la primera mitad y escribe la pareja completa.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "In addition, social movements remind us that democracy depends not only on elections "
                             "(38) ________ on constant participation and civic engagement.", c,
             rotulo=TEXTOS[4] + " · ASÍ DICE TU LIBRO")
    yy += 22
    caja(b, x0, yy, ww, 104, c, sw=2.4, r=14)
    rot(b, x0 + 20, yy + 30, "LA PRIMERA MITAD, ANTES DEL ESPACIO", c, size=14)
    b.append(rect(x0 + 20, yy + 46, 280, 44, "white", r=8, stroke=c, sw=2))
    texto(b, x0 + 330, yy + 76, "…", size=24, color=c, weight="700")
    rot(b, x0 + 380, yy + 76, "SU OTRA MITAD", c, size=14)
    b.append(rect(x0 + 540, yy + 46, 280, 44, "white", r=8, stroke=c, sw=2))
    pista(b, x0 + 850, yy + 76, "en español la pareja es: «no solo…")
    renglon(b, x0 + 1100, yy + 78, x0 + ww - 20)
    yy += 122
    rot(b, x0, yy + 20, "OTRAS PAREJAS QUE YA CONOZCO · ESCRIBO LA MITAD QUE FALTA Y LO QUE SIGNIFICA", c, size=14)
    yy += 36
    pw = (ww - 2 * 20) / 3
    for k, p in enumerate(("both …", "either …", "neither …")):
        bx = x0 + k * (pw + 20)
        caja(b, bx, yy, pw, 128, c, r=14)
        texto(b, bx + 20, yy + 40, p, size=21, weight="700")
        b.append(rect(bx + 20 + tw(p, 21, "700") + 14, yy + 14, 120, 40, "white", r=8, stroke=c, sw=2))
        pista(b, bx + 20, yy + 84, "significa:")
        renglon(b, bx + 100, yy + 86, bx + pw - 20)
        renglon(b, bx + 20, yy + 116, bx + pw - 20)
    yy += 146
    caja(b, x0, yy, ww, 92, c, r=14)
    rot(b, x0 + 20, yy + 30, "BÚSCALA EN EL MISMO TEXTO", c, size=14)
    pista(b, x0 + 20, yy + 66, "En el párrafo 3 hay otra pareja de estas. La copio:")
    renglon(b, x0 + 400, yy + 68, x0 + ww - 20)
    yy += 108
    return ojo(b, x0, yy, ww, "UNA MITAD SOLA SE QUEDA COJA",
               "Si la primera mitad ya está escrita, la opción correcta es la que la completa. Una palabra que "
               "une ideas, pero que no es la otra mitad de esa pareja, deja la oración sin terminar.")




# ═════════ TEXTO 1 · Karol G en Medellín · los espacios nuevos ═════════

# ───────── espacio 2 · began ─────────
def e2(b, x, y, w, h):
    c = AZ
    x0, ww, yy = abre(b, x, y, w, c, 2, "La noche contada en viñetas",
                      "Una historia se cuenta como una tira cómica: cada viñeta es un momento y todas viven en el "
                      "mismo tiempo. Llena las cuatro viñetas con lo que pasa (en español o con un dibujo) y después "
                      "decide en qué tiempo tiene que ir la viñeta del espacio 2.",
                      "Thousands of fans (1) ________ to the stadium early in the morning. The show (2) ________ "
                      "with colorful lights and fireworks. Karol G (3) ________ many of her greatest hits…")
    yy += 26
    vw = (ww - 3 * 34) / 4
    vh = 220
    rotulos = ("VIÑETA 1 · LOS FANS", "VIÑETA 2 · EL SHOW", "VIÑETA 3 · LAS CANCIONES", "VIÑETA 4 · AL FINAL")
    for k, rt in enumerate(rotulos):
        vx = x0 + k * (vw + 34)
        caja(b, vx, yy, vw, vh, c, sw=2, r=6, dash=None if k != 1 else "9,6")
        rot(b, vx + 16, yy + 28, rt, c, size=12)
        pista(b, vx + 16, yy + 56, "dibujo o palabra clave:", size=14)
        lab_linea(b, vx + 16, yy + 196, vx + vw - 16, "qué pasa:", size=14)
        if k < 3:
            flecha(b, vx + vw + 4, yy + vh / 2, vx + vw + 30, yy + vh / 2, c, sw=2.4, head=9)
    pista(b, x0, yy + vh + 26, "La viñeta 2 va punteada: es la del espacio. Las otras tres te dicen cómo se está "
                               "contando la noche.")
    yy += vh + 50
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA TIRA COMPLETA", c, size=14)
    texto(b, x0 + 20, yy + 70, "Las viñetas 1, 3 y 4", size=17)
    xx = marcas(b, x0 + 200, yy + 54, c, ("ya pasaron", "pasan siempre", "van a pasar"))
    lab_linea(b, xx + 10, yy + 70, x0 + ww - 20, "lo sé por:", size=15)
    yy += 122
    return ojo(b, x0, yy, ww, "UNA HISTORIA NO CAMBIA DE TIEMPO A MITAD DE CAMINO",
               "Si los fans llegaron y la cantante cantó, el show no puede estar empezando «hoy» en medio de la "
               "tira. Mira cómo cuenta el texto la viñeta de antes y la de después y escoge la forma que se queda "
               "en ese mismo tiempo.")


# ───────── espacio 3 · sang ─────────
def e3(b, x, y, w, h):
    c = RO
    x0, ww, yy = abre(b, x, y, w, c, 3, "Tres lecturas en voz alta: el oído y la regla",
                      "Lee la oración en voz alta (o en susurro) tres veces, una con cada opción de tu libro. Anota "
                      "cómo te suena y después pásala por la regla: quién canta y cuándo. Cuando el oído y la regla "
                      "no coinciden, gana la regla.",
                      "Karol G (3) ________ many of her greatest hits, and the audience (4) ________ every word.")
    yy += 22
    bh = 112
    for k, L in enumerate("ABC"):
        by = yy + k * (bh + 16)
        b.append(rect(x0 + 74, by, ww - 74, bh, "white", r=24, stroke=c, sw=2))
        b.append(f'<polygon points="{x0 + 76},{by + 40} {x0 + 54},{by + 56} {x0 + 76},{by + 70}" fill="white" '
                 f'stroke="{c}" stroke-width="2"/>')
        b.append(rect(x0 + 72, by + 42, 8, 26, "white", r=0))
        b.append(f'<circle cx="{x0 + 26}" cy="{by + 56}" r="24" fill="white" stroke="{c}" stroke-width="2.4"/>')
        texto(b, x0 + 26, by + 64, L, size=22, color=c, weight="700", anchor="middle")
        texto(b, x0 + 100, by + 38, "«Karol G", size=18, style="italic")
        hueco_caja(b, x0 + 186, by + 14, 150, c, h=36)
        texto(b, x0 + 348, by + 38, "many of her greatest hits»", size=18, style="italic")
        pista(b, x0 + 620, by + 38, "me suena:")
        marcas(b, x0 + 700, by + 22, c, ("bien", "raro"))
        pista(b, x0 + 100, by + 86, "la regla:")
        xx = marcas(b, x0 + 170, by + 70, c, ("una persona", "varias"))
        marcas(b, xx + 10, by + 70, c, ("ya pasó", "hoy o siempre"))
        pista(b, x0 + 920, by + 38, "¿pasa la regla?")
        marcas(b, x0 + 1040, by + 22, c, ("sí", "no"))
    yy += 3 * (bh + 16) + 6
    yy = frase_hueco(b, x0, yy, ww, "El oído me dijo __________ ; la regla me dijo __________ porque Karol G es __________ .", c)
    yy += 16
    return ojo(b, x0, yy, ww, "EL OÍDO SE ENTRENA CON LO QUE OYES",
               "Si en las canciones oyes mucho una forma del verbo, te va a sonar bien aunque aquí no quepa. El "
               "oído ayuda a descartar lo que suena roto; lo que decide es quién hace la acción y cuándo.")


# ───────── espacio 4 · knew ─────────
def e4(b, x, y, w, h):
    c = AZ
    x0, ww, yy = abre(b, x, y, w, c, 4, "El mismo verso con dos relojes",
                      "Cambia el reloj de la oración y mira qué le pasa al verbo. Escribe la forma del verbo «saber» "
                      "que pediría cada reloj; después vuelve al texto y decide cuál de los dos relojes trae.",
                      "Karol G (3) ________ many of her greatest hits, and the audience (4) ________ every word.")
    yy += 24
    for k, (rt, ini) in enumerate((("RELOJ 1 · LA COSTUMBRE", "Every concert,"),
                                   ("RELOJ 2 · UNA NOCHE QUE YA SE ACABÓ", "Last month,"))):
        by = yy + k * 138
        caja(b, x0, by, ww, 120, c, sw=2.2, r=16)
        b.append(f'<circle cx="{x0 + 52}" cy="{by + 60}" r="30" fill="white" stroke="{c}" stroke-width="2.6"/>')
        ang = (-60, 90) if k == 0 else (200, 300)
        import math as _m
        for a_, L_ in zip(ang, (22, 15)):
            ex = x0 + 52 + L_ * _m.cos(_m.radians(a_))
            ey = by + 60 + L_ * _m.sin(_m.radians(a_))
            b.append(line(x0 + 52, by + 60, ex, ey, c, 3))
        rot(b, x0 + 104, by + 32, rt, c, size=13)
        texto(b, x0 + 104, by + 82, f"«{ini} the audience", size=20, style="italic")
        bx = x0 + 104 + tw(f"«{ini} the audience", 20, style="italic") + 14
        hueco_caja(b, bx, by + 54, 170, c, h=40)
        texto(b, bx + 184, by + 82, "every word»", size=20, style="italic")
        lab_linea(b, bx + 330, by + 82, x0 + ww - 20, "en español:", size=15)
    yy += 2 * 138 + 4
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "VUELVO AL TEXTO", c, size=14)
    lab_linea(b, x0 + 20, yy + 74, x0 + 640, "la primera palabra del texto 1 es:")
    pista(b, x0 + 670, yy + 74, "entonces el texto usa el")
    marcas(b, x0 + 850, yy + 58, c, ("reloj 1", "reloj 2"))
    yy += 122
    return trampa(b, x0, yy, ww, "El sujeto no cambió y el verbo sí:",
                  "en los dos relojes la audiencia es la misma, y aun así el verbo cambia de cara. Por eso no basta "
                  "con mirar quién sabe la letra: hay que mirar cuándo la sabía.", c)


# ───────── espacio 6 · presented ─────────
def e6(b, x, y, w, h):
    c = AZ
    x0, ww, yy = abre(b, x, y, w, c, 6, "El contador de veces",
                      "Hay acciones que pasan una sola vez y otras que se repiten. El texto dice cuántas veces pasó "
                      "lo del espacio 6. Primero despeja el camino entre el sujeto y el espacio; después cuenta.",
                      "People (5) ________ very excited because she also (6) ________ a new song for the first time.")
    yy += 22
    caja_rot(b, x0, yy, ww, 112, c, "PASO 1 · QUITO LA PALABRA QUE SE METE EN EL MEDIO")
    texto(b, x0 + 20, yy + 74, "she", size=20, weight="700")
    b.append(rect(x0 + 62, yy + 52, 62, 30, c, r=4, op=0.30))
    texto(b, x0 + 70, yy + 74, "also", size=20)
    texto(b, x0 + 134, yy + 74, "(6) ________", size=20, weight="700")
    lab_linea(b, x0 + 300, yy + 74, x0 + ww - 20, "copio la oración sin esa palabra:")
    yy += 130
    caja_rot(b, x0, yy, ww, 220, c, "PASO 2 · ¿CUÁNTAS VECES PASÓ?")
    cw = (ww - 4 * 24) / 3
    for k, (lab, marcas_n) in enumerate((("una sola vez", 1), ("unas veces", 3), ("siempre, cada vez", 7))):
        cx0 = x0 + 24 + k * (cw + 24)
        caja(b, cx0, yy + 48, cw, 100, c, r=12)
        for j in range(marcas_n):
            tx = cx0 + 30 + j * 22
            b.append(line(tx, yy + 66, tx + 6, yy + 104, c, 3.4))
        b.append(checkbox(cx0 + cw - 44, yy + 64, s=11, c=c))
        pista(b, cx0 + 30, yy + 134, lab, size=16)
    lab_linea(b, x0 + 24, yy + 192, x0 + ww - 20, "las palabras del texto que me lo dicen:")
    yy += 238
    caja(b, x0, yy, ww, 96, c, r=14)
    rot(b, x0 + 20, yy + 30, "PASO 3 · DEL CONTADOR AL RELOJ", c, size=14)
    lab_linea(b, x0 + 20, yy + 70, x0 + ww - 20,
              "algo que pasó una vez, en una noche que ya terminó, va en el tiempo:")
    return yy + 96


# ───────── espacio 7 · lasted ─────────
def e7(b, x, y, w, h):
    c = AZ
    x0, ww, yy = abre(b, x, y, w, c, 7, "La barra de tres horas: ¿ya se cerró?",
                      "Una duración se dibuja como una barra: empieza, dura y termina. Dibuja la barra del concierto "
                      "en la línea y decide si se cerró antes de hoy o si sigue abierta.",
                      "The concert (7) ________ for almost three hours, and at the end she (8) ________ a message of "
                      "love and gratitude.")
    yy += 34
    ly = yy + 70
    caja(b, x0, yy, ww, 190, c, r=14)
    rot(b, x0 + 20, yy + 30, "DIBUJA AQUÍ LA BARRA DEL CONCIERTO", c, size=14)
    b.append(line(x0 + 40, ly + 40, x0 + ww - 80, ly + 40, c, 3.4))
    b.append(f'<polygon points="{x0 + ww - 80},{ly + 30} {x0 + ww - 62},{ly + 40} {x0 + ww - 80},{ly + 50}" '
             f'fill="{c}"/>')
    hx = x0 + ww - 170
    b.append(line(hx, ly + 22, hx, ly + 58, c, 4))
    rot(b, hx, ly + 88, "HOY", c, size=14, anchor="middle")
    for k in range(6):
        tx = x0 + 120 + k * 150
        b.append(line(tx, ly + 32, tx, ly + 48, c, 2))
    pista(b, x0 + 40, ly + 88, "antes")
    yy += 208
    hw = (ww - 24) / 2
    caja_rot(b, x0, yy, hw, 128, c, "«FOR ALMOST THREE HOURS»")
    lab_linea(b, x0 + 20, yy + 70, x0 + hw - 20, "en español:")
    pista(b, x0 + 20, yy + 106, "dice")
    marcas(b, x0 + 64, yy + 90, c, ("cuánto duró", "cuándo pasó"))
    bx = x0 + hw + 24
    caja_rot(b, bx, yy, hw, 128, c, "MI BARRA")
    pista(b, bx + 20, yy + 66, "termina")
    marcas(b, bx + 90, yy + 50, c, ("antes de hoy", "llega hasta hoy"))
    lab_linea(b, bx + 20, yy + 106, bx + hw - 20, "entonces el verbo va en:")
    yy += 146
    return ojo(b, x0, yy, ww, "«FOR» NO DICE EL TIEMPO DEL VERBO",
               "«for» dice cuánto duró algo, no cuándo pasó. Puede ir con cualquier tiempo: «I sleep for eight "
               "hours», «I slept for eight hours». El cuándo te lo dice el reloj del texto, no la duración.")


# ───────── espacio 8 · shared ─────────
def e8(b, x, y, w, h):
    c = RO
    x0, ww, yy = abre(b, x, y, w, c, 8, "Tres puertas y un solo sujeto",
                      "Cada forma del verbo es una puerta, y por cada puerta solo pasan ciertos sujetos en cierto "
                      "tiempo. Escribe arriba de cada puerta una opción de tu libro, anota quién puede pasar y "
                      "cuándo, y busca la puerta por donde entra el sujeto del espacio 8.",
                      "The concert (7) ________ for almost three hours, and at the end she (8) ________ a message of "
                      "love and gratitude.")
    yy += 24
    dw, dh, gap = 360, 330, (ww - 3 * 360) / 2
    for k, L in enumerate("ABC"):
        dx = x0 + k * (dw + gap)
        b.append(f'<path d="M {dx} {yy + dh} L {dx} {yy + 60} Q {dx} {yy} {dx + 60} {yy} L {dx + dw - 60} {yy} '
                 f'Q {dx + dw} {yy} {dx + dw} {yy + 60} L {dx + dw} {yy + dh} Z" fill="white" stroke="{c}" '
                 f'stroke-width="2.4"/>')
        b.append(f'<circle cx="{dx + dw - 34}" cy="{yy + dh / 2 + 30}" r="8" fill="{c}"/>')
        rot(b, dx + 24, yy + 40, f"PUERTA {L}", c, size=14)
        lab_linea(b, dx + 24, yy + 84, dx + dw - 24, "la opción:")
        pista(b, dx + 24, yy + 128, "¿quién pasa? (I, you, he, she, we, they)")
        renglon(b, dx + 24, yy + 166, dx + dw - 60)
        renglon(b, dx + 24, yy + 204, dx + dw - 60)
        pista(b, dx + 24, yy + 248, "¿cuándo?")
        marcas(b, dx + 24, yy + 262, c, ("hoy", "ya pasó"))
    yy += dh + 22
    yy = frase_hueco(b, x0, yy, ww, "El sujeto del 8 es __________ y la noche ya __________ → entra por la puerta ______ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una puerta puede dejar pasar a «she» y aun así estar cerrada:",
                  "concordar con el sujeto es solo la mitad. La otra mitad es el tiempo: ¿en qué tiempo se ha contado "
                  "la noche hasta llegar a «at the end»? Mira los espacios que ya llenaste.", c)


# ───────── espacio 10 · was ─────────
def e10(b, x, y, w, h):
    c = RO
    x0, ww, yy = abre(b, x, y, w, c, 10, "Una oración guardada dentro de otra",
                      "Después de «thought» empieza una oración pequeña que vive dentro de la grande y tiene su propio "
                      "sujeto. Sepárala, busca su sujeto y decide qué verbo necesita para unir «the night» con "
                      "«unforgettable».",
                      "Everyone (9) ________ the night (10) ________ unforgettable.")
    yy += 24
    caja(b, x0, yy, ww, 330, c, sw=2.6, r=18, fill=tinte(c, 0.95))
    rot(b, x0 + 22, yy + 32, "LA ORACIÓN GRANDE", c, size=14)
    texto(b, x0 + 22, yy + 76, "Everyone  (9) ________", size=21, weight="700")
    hueco_caja(b, x0 + 270, yy + 48, 96, c, h=40)
    pista(b, x0 + 380, yy + 76, "← aquí el inglés puede esconder una palabra que une; escríbela si la sabes")
    ix, iy, iw = x0 + 40, yy + 104, ww - 80
    caja(b, ix, iy, iw, 206, c, sw=2.2, r=14)
    rot(b, ix + 20, iy + 30, "LA ORACIÓN PEQUEÑA", c, size=14)
    texto(b, ix + 20, iy + 74, "the night  (10) ________  unforgettable", size=21, weight="700")
    lab_linea(b, ix + 20, iy + 122, ix + iw / 2 - 20, "su sujeto:")
    pista(b, ix + iw / 2, iy + 122, "es")
    marcas(b, ix + iw / 2 + 30, iy + 106, c, ("uno solo (it)", "varios (they)"))
    lab_linea(b, ix + 20, iy + 172, ix + iw - 20,
              "en español: «Todos pensaron que la noche __________ inolvidable» → la palabra que falta:")
    yy += 348
    caja(b, x0, yy, ww, 98, c, r=14)
    rot(b, x0 + 20, yy + 30, "LAS DOS ORACIONES, EN EL MISMO RELOJ", c, size=14)
    lab_linea(b, x0 + 20, yy + 72, x0 + ww / 2 - 20, "la grande va en:")
    lab_linea(b, x0 + ww / 2, yy + 72, x0 + ww - 20, "entonces la pequeña va en:")
    yy += 114
    return ojo(b, x0, yy, ww, "ENTRE UN SUSTANTIVO Y UN ADJETIVO",
               "Antes de escoger, mira qué clase de palabra es cada opción: entre «the night» y un adjetivo como "
               "«unforgettable» tiene que ir un verbo que una, como «es» o «fue» en español.")


# ═════════ TEXTO 2 · Spider-Verse ═════════

# ───────── espacio 11 · was ─────────
def e11(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El calendario: de 2023 a hoy", c,
                      "El texto 2 empieza con un año. Un año es la pista de tiempo más clara que existe: ponlo en el "
                      "calendario frente al año en que estás tú y mide la distancia.")
    x0, ww = x + 22, w - 44
    yy = idea_texto(b, x0, yy, ww, c) + 16
    yy = cita(b, x0, yy, ww, "In 2023, the movie Spider-Man: Across the Spider-Verse (11) ________ one of the most "
                             "popular films among teenagers.", c, rotulo=rotulo_cita(11))
    yy += 22
    caja_rot(b, x0, yy, ww, 160, c, "EL CALENDARIO")
    n = 7
    cw = (ww - 40 - (n - 1) * 12) / n
    for k in range(n):
        cx0 = x0 + 20 + k * (cw + 12)
        caja(b, cx0, yy + 46, cw, 66, c, r=8, fill=tinte(c, 0.93) if k == 0 else "white")
        if k == 0:
            texto(b, cx0 + cw / 2, yy + 88, "2023", size=22, weight="700", anchor="middle", color=c)
    pista(b, x0 + 20, yy + 140, "Escribe los años que siguen y encierra el año en que estás hoy. "
                                "Distancia: ______ años.")
    yy += 178
    hw = (ww - 24) / 2
    caja_rot(b, x0, yy, hw, 120, c, "EL SUJETO ES LARGO")
    pista(b, x0 + 20, yy + 62, "subraya en la cita desde «the movie» hasta el espacio.")
    pista(b, x0 + 20, yy + 98, "¿cuántas cosas son?")
    marcas(b, x0 + 170, yy + 82, c, ("una", "varias"))
    bx = x0 + hw + 24
    caja_rot(b, bx, yy, hw, 120, c, "LO QUE ME DICE EL CALENDARIO")
    pista(b, bx + 20, yy + 62, "2023 queda en la zona")
    marcas(b, bx + 190, yy + 46, c, ("ya pasó", "ahora", "todavía no"))
    lab_linea(b, bx + 20, yy + 98, bx + hw - 20, "el verbo «be» que pide:")
    return yy + 120


# ───────── espacio 12 · was released ─────────
def e12(b, x, y, w, h):
    c = RO
    x0, ww, yy = abre(b, x, y, w, c, 12, "La flecha de la acción: ¿quién estrena a quién?",
                      "Una película no se estrena sola: alguien la estrena. Dibuja la flecha de la acción y decide si "
                      "«It» (la película) hace la acción o la recibe. Eso decide la forma del verbo.",
                      "It (12) ________ in cinemas around the world and millions of people (13) ________ to see it.")
    yy += 16
    yy = correccion(b, x0, yy, ww,
                    "En tu libro la opción A dice «was release»: está mal escrita, le falta la -d del final "
                    "(«was released»). Corrígela con lápiz en el libro y después escoge entre las tres con tu "
                    "flecha y tu pista.") + 22
    bw = 330
    for k, (rt, ps) in enumerate((("QUIÉN HACE LA ACCIÓN", "en el texto no aparece; ¿quién sería?"),
                                  ("LA ACCIÓN", "estrenar · lanzar · sacar al público"),
                                  ("QUIÉN LA RECIBE", "¿qué cosa queda estrenada?"))):
        bx = x0 + k * (bw + (ww - 3 * bw) / 2)
        caja(b, bx, yy, bw, 150, c, sw=2.4, r=16, fill=tinte(c, 0.95) if k == 1 else "white")
        rot(b, bx + 20, yy + 30, rt, c, size=13)
        pista(b, bx + 20, yy + 60, ps, size=14)
        renglon(b, bx + 20, yy + 120, bx + bw - 20)
        if k < 2:
            flecha(b, bx + bw + 10, yy + 75, bx + bw + (ww - 3 * bw) / 2 - 10, yy + 75, c, sw=3, head=12)
    yy += 172
    caja(b, x0, yy, ww, 100, c, r=14)
    rot(b, x0 + 20, yy + 30, "EN LA ORACIÓN DEL LIBRO", c, size=14)
    pista(b, x0 + 20, yy + 70, "«It» es la película: en mi flecha")
    xx = marcas(b, x0 + 270, yy + 54, c, ("hace la acción", "recibe la acción"))
    lab_linea(b, xx + 10, yy + 70, x0 + ww - 20, "lo sé porque:")
    yy += 118
    return alto_profe(b, x0, yy, ww,
                      "Cuando el sujeto recibe la acción, el inglés arma el verbo de otra manera (la voz pasiva). "
                      "Pídele al profe que la muestre con un ejemplo que no sea del texto antes de que marques.")


# ───────── espacio 14 · introduced ─────────
def e14(b, x, y, w, h):
    c = AZ
    x0, ww, yy = abre(b, x, y, w, c, 14, "La pregunta de control: ¿did o does?",
                      "Una manera de oír el tiempo de un verbo es volver la oración pregunta. En inglés la pregunta "
                      "se hace con un ayudante que carga el tiempo: does (hoy, siempre) o did (ya pasó), y el verbo va "
                      "pelado, como en el diccionario. Escribe el verbo «introducir» en las dos preguntas, quédate con la que va con el texto y devuélvela a afirmación.",
                      "The movie (14) ________ new characters and (15) ________ a unique animation style that many "
                      "critics admired.")
    yy += 24
    hw = (ww - 24) / 2
    for k, (aux, rt) in enumerate((("Does", "PREGUNTA 1 · CON DOES"), ("Did", "PREGUNTA 2 · CON DID"))):
        bx = x0 + k * (hw + 24)
        caja(b, bx, yy, hw, 196, c, sw=2.4, r=16)
        b.append(f'<circle cx="{bx + 40}" cy="{yy + 44}" r="20" fill="white" stroke="{c}" stroke-width="2.4"/>')
        texto(b, bx + 40, yy + 53, "?", size=24, color=c, weight="700", anchor="middle")
        rot(b, bx + 74, yy + 50, rt, c, size=13)
        t0 = f"«{aux} the movie"
        texto(b, bx + 22, yy + 106, t0, size=19, style="italic")
        hx = bx + 22 + tw(t0, 19, style="italic") + 10
        hueco_caja(b, hx, yy + 78, 150, c)
        texto(b, hx + 162, yy + 106, "new characters?»", size=19, style="italic")
        pista(b, bx + 22, yy + 148, "¿cabe en un texto que empieza con «In 2023»?")
        marcas(b, bx + 22, yy + 160, c, ("sí", "no"))
    yy += 216
    caja(b, x0, yy, ww, 168, c, sw=2.6, r=16, fill=tinte(c, 0.95))
    rot(b, x0 + 20, yy + 30, "LA DEVUELVO A AFIRMACIÓN", c, size=14)
    pista(b, x0 + 20, yy + 66, "Cuando la pregunta se vuelve afirmación, el ayudante desaparece y su tiempo pasa al verbo:")
    texto(b, x0 + 20, yy + 114, "«The movie", size=20, style="italic")
    hueco_caja(b, x0 + 126, yy + 86, 200, c)
    texto(b, x0 + 340, yy + 114, "new characters.»", size=20, style="italic")
    lab_linea(b, x0 + 540, yy + 114, x0 + ww - 20, "el ayudante que escogí:")
    lab_linea(b, x0 + 20, yy + 150, x0 + ww - 20, "lo que le pasó al verbo cuando el ayudante se fue:")
    yy += 186
    return ojo(b, x0, yy, ww, "EL AYUDANTE SE LLEVA EL TIEMPO",
               "En la pregunta, el verbo va pelado y el ayudante dice el tiempo. En la afirmación no hay ayudante, "
               "así que el verbo tiene que cargar el tiempo él solo. Por eso la pregunta te deja oír cuál es.")


# ───────── espacio 16 · were ─────────
def e16(b, x, y, w, h):
    c = RO
    x0, ww, yy = abre(b, x, y, w, c, 16, "La lupa sobre la última letra del sujeto",
                      "En inglés el plural casi siempre se esconde en la última letra. Pon la lupa sobre el sujeto del "
                      "espacio 16, decide si esa letra lo vuelve plural y cámbialo por un pronombre.",
                      "Audiences (16) ________ very impressed by the story, which (17) ________ both exciting action "
                      "and emotional moments.")
    yy += 26
    cx, cy, r = x0 + 170, yy + 140, 120
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{tinte(c, 0.94)}" stroke="{c}" stroke-width="5"/>')
    b.append(line(cx + r * 0.72, cy + r * 0.72, cx + r * 1.2, cy + r * 1.2, c, 16))
    texto(b, cx - 8, cy + 14, "Audience", size=34, weight="700", anchor="middle")
    hueco_caja(b, cx + 86, cy - 26, 40, c, h=52)
    pista(b, cx, cy + 58, "la última letra va en la caja", anchor="middle", size=14)
    bx = x0 + 400
    bw = ww - 400
    caja_rot(b, bx, yy, bw, 300, c, "LO QUE VI CON LA LUPA")
    lab_linea(b, bx + 20, yy + 76, bx + bw - 20, "la palabra sin su última letra significa:")
    pista(b, bx + 20, yy + 130, "¿existe sin la última letra?")
    marcas(b, bx + 240, yy + 114, c, ("sí", "no"))
    pista(b, bx + 20, yy + 184, "entonces la última letra")
    marcas(b, bx + 200, yy + 168, c, ("la vuelve plural", "es parte de la palabra"))
    pista(b, bx + 20, yy + 238, "la cambio por el pronombre")
    marcas(b, bx + 220, yy + 222, c, ("it", "they"))
    lab_linea(b, bx + 20, yy + 280, bx + bw - 20, "y en el reloj del texto, ese pronombre con «very impressed»:")
    yy += 320
    return ojo(b, x0, yy, ww, "NO TODA -S DEL FINAL ES PLURAL",
               "«bus», «news», «is» también terminan en -s y no son plurales. La prueba es quitarla: si sin ella "
               "queda una palabra que existe y significa una sola cosa, la -s era la marca del plural.")


# ───────── espacio 17 · combined ─────────
def e17(b, x, y, w, h):
    c = AZ
    x0, ww, yy = abre(b, x, y, w, c, 17, "La flecha del «which»",
                      "«which» es una palabra que señala hacia atrás: reemplaza algo que ya se dijo. Dibuja a dónde "
                      "apunta, reescribe esa parte como una oración sola y decide de qué momento habla.",
                      "Audiences (16) ________ very impressed by the story, which (17) ________ both exciting action "
                      "and emotional moments.")
    yy += 30
    ry = yy + 70
    caja(b, x0, ry, 300, 64, c, sw=2.4, r=12)
    pista(b, x0 + 20, ry + 40, "a lo que señala:", size=15)
    caja(b, x0 + 560, ry, 200, 64, c, sw=2.4, r=12, fill=tinte(c, 0.9))
    texto(b, x0 + 660, ry + 41, "which", size=24, weight="700", anchor="middle")
    b.append(f'<path d="M {x0 + 600} {ry} Q {x0 + 450} {ry - 70} {x0 + 300} {ry + 10}" fill="none" stroke="{c}" '
             f'stroke-width="3.2" stroke-dasharray="9,6"/>')
    b.append(f'<polygon points="{x0 + 296},{ry - 6} {x0 + 304},{ry + 22} {x0 + 322},{ry + 2}" fill="{c}"/>')
    pista(b, x0 + 800, ry + 40, "which = «la cual», «que»")
    yy = ry + 90
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA REESCRIBO SIN «WHICH»", c, size=14)
    texto(b, x0 + 20, yy + 76, "«The story", size=20, style="italic")
    hueco_caja(b, x0 + 126, yy + 48, 180, c)
    texto(b, x0 + 320, yy + 76, "both exciting action and emotional moments.»", size=20, style="italic")
    yy += 122
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "¿DE QUÉ MOMENTO HABLO?", c, size=14)
    marcas(b, x0 + 20, yy + 56, c, ("de lo que pasó cuando la vieron en 2023",
                                    "de cómo es la historia, hoy y siempre"))
    yy += 122
    return correccion(b, x0, yy, ww,
                      "Aquí el libro espera un solo tiempo, pero se defienden dos: el del relato (todo el texto 2 "
                      "cuenta lo que pasó en 2023) y el de lo que la historia sigue siendo hoy. Marca el tuyo, "
                      "escribe tu pista en el salvavidas y defiéndela en clase.")


# ───────── espacio 18 · dealt ─────────
def e18(b, x, y, w, h):
    c = AZ
    x0, ww, yy = abre(b, x, y, w, c, 18, "El sujeto con dos nombres entre comas",
                      "Entre el sujeto y el espacio hay un nombre metido entre comas: es el mismo personaje dicho dos "
                      "veces. Tápalo para ver el sujeto pegado al verbo; después escoge tu reloj para los espacios "
                      "18, 19 y 20.",
                      "The main character, Miles Morales, (18) ________ with problems at school and at home, just like "
                      "many real teenagers.")
    yy += 16
    yy = correccion(b, x0, yy, ww,
                    "En los espacios 18, 19 y 20 el libro acepta un solo tiempo, pero en el resumen de una película "
                    "valen dos: el pasado (el texto arranca con «In 2023») y el presente con que se cuentan las "
                    "tramas. Escoge un reloj aquí y sostenlo en los tres.") + 22
    caja_rot(b, x0, yy, ww, 120, c, "TAPO LO QUE VA ENTRE COMAS")
    texto(b, x0 + 20, yy + 78, "The main character,", size=20, weight="700")
    b.append(rect(x0 + 206, yy + 52, 170, 36, c, r=6, op=0.30))
    texto(b, x0 + 214, yy + 78, "Miles Morales,", size=20)
    texto(b, x0 + 386, yy + 78, "(18) ________ with problems…", size=20, weight="700")
    pista(b, x0 + 700, yy + 78, "el sujeto es")
    marcas(b, x0 + 800, yy + 62, c, ("uno (he)", "varios (they)"))
    yy += 138
    caja(b, x0, yy, ww, 196, c, sw=2.6, r=16, fill=tinte(c, 0.95))
    rot(b, x0 + 20, yy + 32, "MI RELOJ PARA 18, 19 Y 20", c, size=14)
    marcas(b, x0 + 20, yy + 58, c, ("lo cuento como algo que ya pasó, como «In 2023»",))
    marcas(b, x0 + 20, yy + 98, c, ("lo cuento como el resumen de la trama, como en la contraportada",))
    lab_linea(b, x0 + 20, yy + 164, x0 + ww - 20, "la pista que me hizo escoger:")
    return yy + 196


# ───────── espacio 19 · tried ─────────
def e19(b, x, y, w, h):
    c = RO
    x0, ww, yy = abre(b, x, y, w, c, 19, "Los verbos que terminan en y",
                      "Los verbos que terminan en y a veces cambian la y cuando les pones -s o -ed. Llena la tabla, "
                      "descubre la regla por tu cuenta y aplícala al verbo del espacio 19 con el reloj que escogiste "
                      "en la pregunta 18.",
                      "He also (19) ________ to decide how to balance his life as a student and as Spider-Man.")
    yy += 22
    cols = (220, (ww - 220 - 330) / 2, (ww - 220 - 330) / 2, 330)
    yy = tabla_vacia(b, x0, yy, cols, ("VERBO", "HE · SHE · HOY", "YA PASÓ", "ANTES DE LA Y HAY…"),
                     ("study", "cry", "carry", "play", "enjoy"), c, rh=54)
    yy += 18
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA REGLA QUE DESCUBRÍ", c, size=14)
    lab_linea(b, x0 + 20, yy + 76, x0 + ww - 20,
              "si antes de la y hay una __________ , la y se vuelve ______ ; si hay una __________ , la y")
    yy += 122
    caja(b, x0, yy, ww, 100, c, sw=2.4, r=14, fill=tinte(c, 0.95))
    rot(b, x0 + 20, yy + 30, "EL ESPACIO 19, CON MI RELOJ DE LA PREGUNTA 18", c, size=14)
    lab_linea(b, x0 + 20, yy + 72, x0 + ww / 2 - 20, "mi reloj:")
    lab_linea(b, x0 + ww / 2, yy + 72, x0 + ww - 20, "«He also ______ to decide»:")
    return yy + 100


# ───────── espacio 20 · left ─────────
def e20(b, x, y, w, h):
    c = AZ
    x0, ww, yy = abre(b, x, y, w, c, 20, "Un hilo de tres cuentas",
                      "Los espacios 18, 19 y 20 cuentan la misma trama: son cuentas de un mismo collar y van en el "
                      "mismo tiempo. Escribe en cada cuenta el verbo que escogiste y revisa que el hilo no se rompa.",
                      "At the end, the movie (20) ________ viewers waiting for the next chapter in the series.")
    yy += 30
    hy = yy + 110
    b.append(f'<path d="M {x0 + 20} {hy - 40} Q {x0 + ww / 2} {hy + 90} {x0 + ww - 20} {hy - 40}" fill="none" '
             f'stroke="{c}" stroke-width="3"/>')
    for k, (n, px) in enumerate(((18, 0.2), (19, 0.5), (20, 0.8))):
        t = px
        bx_ = (1 - t) ** 2 * (x0 + 20) + 2 * (1 - t) * t * (x0 + ww / 2) + t ** 2 * (x0 + ww - 20)
        by_ = (1 - t) ** 2 * (hy - 40) + 2 * (1 - t) * t * (hy + 90) + t ** 2 * (hy - 40)
        b.append(f'<ellipse cx="{bx_:.0f}" cy="{by_:.0f}" rx="150" ry="74" fill="white" stroke="{c}" '
                 f'stroke-width="2.8"/>')
        rot(b, bx_, by_ - 30, f"CUENTA {n}", c, size=14, anchor="middle")
        renglon(b, bx_ - 100, by_ + 16, bx_ + 100)
        pista(b, bx_ - 100, by_ + 50, "hoy")
        b.append(checkbox(bx_ - 64, by_ + 34, s=9, c=c))
        pista(b, bx_ + 4, by_ + 50, "ya pasó")
        b.append(checkbox(bx_ + 64, by_ + 34, s=9, c=c))
    yy = hy + 120
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "¿SE ROMPIÓ EL HILO?", c, size=14)
    pista(b, x0 + 20, yy + 72, "las tres cuentas están en el mismo tiempo:")
    xx = marcas(b, x0 + 330, yy + 56, c, ("sí", "no"))
    lab_linea(b, xx + 10, yy + 72, x0 + ww - 20, "si no, cuál cambio y por qué:")
    yy += 122
    caja(b, x0, yy, ww, 100, c, r=14)
    rot(b, x0 + 20, yy + 30, "«THE MOVIE ___ VIEWERS WAITING»", c, size=14)
    lab_linea(b, x0 + 20, yy + 72, x0 + ww / 2 - 20, "en español:")
    lab_linea(b, x0 + ww / 2, yy + 72, x0 + ww - 20, "«dejar» en inglés, con mi reloj:")
    yy += 118
    return ojo(b, x0, yy, ww, "«AT THE END» NO CAMBIA EL RELOJ",
               "«At the end» dice en qué parte de la película pasa algo (al final), no cuándo pasa en la vida real. "
               "El reloj lo escogiste en la pregunta 18: sostenlo.")



# ═════════ TEXTO 3 · AI in the Classroom ═════════

def _gente(b, cx, cy, c, r=17):
    """Una persona vista desde arriba: cabeza y hombros."""
    b.append(f'<circle cx="{cx:.0f}" cy="{cy - 10:.0f}" r="{r * 0.55:.0f}" fill="white" stroke="{c}" stroke-width="2.4"/>')
    b.append(f'<path d="M {cx - r:.0f} {cy + r:.0f} Q {cx:.0f} {cy - 4:.0f} {cx + r:.0f} {cy + r:.0f}" fill="none" '
             f'stroke="{c}" stroke-width="2.4"/>')


def _cosa(b, cx, cy, c, s=26):
    b.append(rect(cx - s / 2, cy - s / 2, s, s, tinte(c, 0.6), r=5, stroke=c, sw=2.2))


# ───────── espacio 21 · among ─────────
def e21(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "¿Entre dos o en medio de muchos?", c,
                      "En español decimos «entre» para dos cosas y para una multitud. El inglés las separa. Mira los "
                      "dos dibujos, escribe la palabra inglesa que conozcas para cada uno y decide cuál dibuja a los "
                      "«teenagers» del texto.")
    x0, ww = x + 22, w - 44
    yy = idea_texto(b, x0, yy, ww, c) + 16
    yy = cita(b, x0, yy, ww, "Artificial Intelligence (AI) tools, like chatbots, have become very popular (21) ________ "
                             "teenagers.", c, rotulo=rotulo_cita(21))
    yy += 22
    hw = (ww - 24) / 2
    for k, rt in enumerate(("DIBUJO 1 · LA COSA QUEDA ENTRE DOS", "DIBUJO 2 · LA COSA QUEDA EN MEDIO DE MUCHOS")):
        bx = x0 + k * (hw + 24)
        caja_rot(b, bx, yy, hw, 256, c, rt)
        mx, my = bx + hw / 2, yy + 112
        if k == 0:
            _gente(b, mx - 120, my, c)
            _gente(b, mx + 120, my, c)
            _cosa(b, mx, my, c)
        else:
            import math as _m
            for j in range(9):
                a_ = 2 * _m.pi * j / 9
                _gente(b, mx + 150 * _m.cos(a_), my + 58 * _m.sin(a_), c, r=14)
            _cosa(b, mx, my, c)
        lab_linea(b, bx + 20, yy + 196, bx + hw - 20, "¿cuántos hay alrededor?")
        lab_linea(b, bx + 20, yy + 236, bx + hw - 20, "la palabra en inglés:")
    yy += 274
    caja(b, x0, yy, ww, 98, c, r=14)
    rot(b, x0 + 20, yy + 30, "LOS «TEENAGERS» DEL TEXTO", c, size=14)
    pista(b, x0 + 20, yy + 70, "son")
    xx = marcas(b, x0 + 56, yy + 54, c, ("dos", "muchos"))
    pista(b, xx + 10, yy + 70, "→ los chatbots quedan como en el")
    marcas(b, xx + 250, yy + 54, c, ("dibujo 1", "dibujo 2"))
    return yy + 98


# ───────── espacio 23 · on ─────────
def e23(b, x, y, w, h):
    c = OR
    x0, ww, yy = abre(b, x, y, w, c, 23, "El imán de «depend»",
                      "Algunos verbos traen pegada su palabra pequeña, como un imán, aunque otras palabras se metan en "
                      "el medio. Saca lo que estorba, junta el verbo con el espacio y escribe qué viene pegado.",
                      "However, teachers warn that depending too much (23) ________ these apps may reduce critical "
                      "thinking skills.")
    yy += 22
    caja_rot(b, x0, yy, ww, 112, c, "PASO 1 · SACO LO QUE SE METE EN EL MEDIO")
    texto(b, x0 + 20, yy + 76, "depending", size=20, weight="700")
    b.append(rect(x0 + 118, yy + 54, 92, 32, c, r=5, op=0.30))
    texto(b, x0 + 124, yy + 76, "too much", size=20)
    texto(b, x0 + 220, yy + 76, "(23) ____ these apps", size=20, weight="700")
    lab_linea(b, x0 + 460, yy + 76, x0 + ww - 20, "sin lo que estorba, ¿qué quiere decir?")
    yy += 130
    caja_rot(b, x0, yy, ww, 150, c, "PASO 2 · EL IMÁN")
    caja(b, x0 + 30, yy + 54, 210, 64, c, sw=2.4, r=12)
    texto(b, x0 + 135, yy + 95, "depend", size=24, weight="700", anchor="middle")
    b.append(f'<polyline points="{x0 + 300},{yy + 62} {x0 + 262},{yy + 62} {x0 + 262},{yy + 110} {x0 + 300},{yy + 110}" '
             f'fill="none" stroke="{c}" stroke-width="13" stroke-linejoin="round"/>')
    b.append(rect(x0 + 294, yy + 55, 14, 14, "#9AA1AC", r=2))
    b.append(rect(x0 + 294, yy + 103, 14, 14, "#9AA1AC", r=2))
    b.append(rect(x0 + 324, yy + 54, 110, 64, "white", r=12, stroke=c, sw=2.4, dash="8,6"))
    pista(b, x0 + 470, yy + 76, "la escribo cuando la confirme. Una frase mía en inglés con las dos:")
    renglon(b, x0 + 470, yy + 118, x0 + ww - 20)
    yy += 168
    caja_rot(b, x0, yy, ww, 104, c, "PASO 3 · ¿Y EL ESPAÑOL?")
    lab_linea(b, x0 + 20, yy + 72, x0 + 560, "en español se dice «depender ____»:")
    pista(b, x0 + 590, yy + 72, "¿esa palabra está entre las opciones?")
    marcas(b, x0 + 860, yy + 56, c, ("sí", "no"))
    yy += 122
    return trampa(b, x0, yy, ww, "Si el español no aparece entre las opciones, no te asustes:",
                  "quiere decir que el inglés usa otra palabra pegada. No escojas la que más se parece al español: "
                  "escoge la que hayas oído junto a este verbo en inglés.", c)


# ───────── espacio 24 · by ─────────
def e24(b, x, y, w, h):
    c = OR
    x0, ww, yy = abre(b, x, y, w, c, 24, "Tres maneras de decir quién revisa",
                      "La oración está dicha al revés: las tareas aparecen primero y quien las revisa va al final. "
                      "Ponla al derecho y después decide qué idea quieres decir con la palabra pequeña.",
                      "In some schools, assignments are checked carefully (24) ________ plagiarism detectors.")
    yy += 16
    yy = correccion(b, x0, yy, ww,
                    "Aquí se defienden las tres opciones: cada una dice una idea un poco distinta y las tres caben en "
                    "inglés. El libro espera una sola. Marca la tuya y escribe en tu salvavidas qué idea dice.") + 22
    caja_rot(b, x0, yy, ww, 112, c, "LA PONGO AL DERECHO, EMPEZANDO POR QUIEN REVISA")
    texto(b, x0 + 20, yy + 78, "«Plagiarism detectors", size=20, style="italic")
    hueco_caja(b, x0 + 230, yy + 50, 180, c)
    texto(b, x0 + 424, yy + 78, "the assignments.»", size=20, style="italic")
    pista(b, x0 + 640, yy + 78, "(revisar, en el tiempo de «are checked»)")
    yy += 130
    cw = (ww - 2 * 20) / 3
    for k, (rt, es) in enumerate((("IDEA 1 · QUIÉN LO HACE", "las tareas las revisa el detector"),
                                  ("IDEA 2 · CON QUÉ HERRAMIENTA", "las revisan con el detector"),
                                  ("IDEA 3 · POR MEDIO DE QUÉ", "pasan por el detector"))):
        bx = x0 + k * (cw + 20)
        caja_rot(b, bx, yy, cw, 168, c, rt)
        pista(b, bx + 20, yy + 64, f"«{es}»", size=15)
        lab_linea(b, bx + 20, yy + 112, bx + cw - 20, "en inglés:")
        b.append(checkbox(bx + 20, yy + 128, s=10, c=c))
        pista(b, bx + 50, yy + 145, "esta es la que quiero decir", size=14)
    return yy + 168


# ───────── espacio 26 · by ─────────
def e26(b, x, y, w, h):
    c = OR
    x0, ww, yy = abre(b, x, y, w, c, 26, "El espejo: la misma palabra a cada lado",
                      "Hay expresiones que repiten una palabra con una pequeña en el medio, como un espejo. No se "
                      "arman: se aprenden enteras. Completa las que conozcas y descubre si la del medio cambia.",
                      "For example, a chatbot can explain math exercises step (26) ________ step or translate short "
                      "texts.")
    yy += 26
    caja(b, x0, yy, ww, 120, c, sw=2.6, r=16, fill=tinte(c, 0.95))
    mx = x0 + ww / 2
    b.append(line(mx, yy + 14, mx, yy + 106, c, 2.4, dash="8,6"))
    texto(b, mx - 90, yy + 74, "step", size=30, weight="700", anchor="end")
    b.append(rect(mx - 70, yy + 38, 140, 52, "white", r=10, stroke=c, sw=2.4))
    texto(b, mx + 90, yy + 74, "step", size=30, weight="700")
    pista(b, x0 + 20, yy + 104, "en español: paso ___ paso")
    yy += 140
    filas = (("poco a poco", "little", "little"), ("uno por uno", "one", "one"),
             ("día a día", "day", "day"), ("lado a lado", "side", "side"))
    cw = (ww - 20) / 2
    for k, (es, a_, b2) in enumerate(filas):
        bx = x0 + (k % 2) * (cw + 20)
        by = yy + (k // 2) * 96
        caja(b, bx, by, cw, 80, c, r=12)
        pista(b, bx + 20, by + 48, es, size=16)
        texto(b, bx + 190, by + 49, a_, size=20, weight="700")
        hueco_caja(b, bx + 190 + tw(a_, 20, "700") + 12, by + 20, 90, c)
        texto(b, bx + 190 + tw(a_, 20, "700") + 114, by + 49, b2, size=20, weight="700")
    yy += 2 * 96 + 4
    caja(b, x0, yy, ww, 100, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE DESCUBRÍ", c, size=14)
    pista(b, x0 + 20, yy + 70, "en español usamos «a» y «por»; en inglés la del medio")
    xx = marcas(b, x0 + 400, yy + 54, c, ("cambia", "es siempre la misma"))
    lab_linea(b, xx + 10, yy + 70, x0 + ww - 20, "¿cuál?")
    yy += 118
    return ojo(b, x0, yy, ww, "SI CONOCES UNA, CONOCES LA FAMILIA",
               "Estas expresiones viajan juntas. Si no te sabes «step ___ step», busca entre las cuatro de arriba "
               "la que sí te sepas (de una canción, de un juego) y prueba si su palabra del medio sirve aquí.")


# ───────── espacio 28 · for ─────────
def e28(b, x, y, w, h):
    c = OR
    x0, ww, yy = abre(b, x, y, w, c, 28, "¿A quién se pega: a la de antes o a la de después?",
                      "El espacio tiene una vecina a cada lado. La palabra pequeña viene pegada a una de las dos. Para "
                      "saber a cuál, cambia la de después y mira si la pequeña se mueve.",
                      "Therefore, students are encouraged to use AI as a tool, not as a substitute (28) ________ "
                      "learning.")
    yy += 26
    cy_ = yy + 60
    caja(b, x0 + 60, cy_ - 34, 260, 68, c, sw=2.4, r=12)
    texto(b, x0 + 190, cy_ + 9, "substitute", size=24, weight="700", anchor="middle")
    hueco_caja(b, x0 + ww / 2 - 70, cy_ - 30, 140, c, h=60)
    caja(b, x0 + ww - 320, cy_ - 34, 260, 68, c, sw=2.4, r=12)
    texto(b, x0 + ww - 190, cy_ + 9, "learning", size=24, weight="700", anchor="middle")
    flecha(b, x0 + ww / 2 - 80, cy_, x0 + 330, cy_, c, sw=3, head=12)
    flecha(b, x0 + ww / 2 + 80, cy_, x0 + ww - 330, cy_, c, sw=3, head=12)
    pista(b, x0 + ww / 2, cy_ + 62, "¿hacia qué lado tira la palabra pequeña?", anchor="middle")
    yy = cy_ + 90
    caja_rot(b, x0, yy, ww, 180, c, "LA PRUEBA · CAMBIO LA PALABRA DE DESPUÉS")
    for k, fin in enumerate(("sugar", "a teacher", "real friends")):
        by = yy + 60 + k * 40
        texto(b, x0 + 20, by + 10, f"a substitute  ____  {fin}", size=19, style="italic")
    pista(b, x0 + 420, yy + 70, "¿la pequeña cambia cuando cambio lo de después?")
    marcas(b, x0 + 420, yy + 86, c, ("sí", "no"))
    lab_linea(b, x0 + 420, yy + 150, x0 + ww - 20, "entonces viene pegada a:")
    yy += 198
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "PRIMERO EL ESPAÑOL, DESPUÉS LA PRUEBA", c, size=14)
    lab_linea(b, x0 + 20, yy + 72, x0 + 520, "en español: «un sustituto ____ algo»")
    lab_linea(b, x0 + 550, yy + 72, x0 + ww - 20, "una frase en inglés que haya oído con substitute:")
    yy += 122
    return trampa(b, x0, yy, ww, "La pegada del español no siempre es la del inglés:",
                  "si la que te dicta el español está entre las opciones, no la marques por eso. Compruébala con una "
                  "frase en inglés que ya conozcas; si no tienes ninguna, marca «casi» en qué tan seguro estás.", c)


# ───────── espacio 29 · to ─────────
def e29(b, x, y, w, h):
    c = RO
    x0, ww, yy = abre(b, x, y, w, c, 29, "Un verbo sin nada encima",
                      "Esta vez la pista no está antes del espacio, sino después. Mira la palabra que sigue: si es un "
                      "verbo pelado, sin ninguna marca, la palabra pequeña que cabe antes de él es una sola.",
                      "In the future, digital literacy will be essential (29) ________ succeed in education and work, "
                      "and young people must be prepared (30) ________ new technological challenges.")
    yy += 24
    caja(b, x0, yy, 330, 250, c, sw=2.6, r=18, fill=tinte(c, 0.95))
    rot(b, x0 + 20, yy + 32, "LA PALABRA DE DESPUÉS", c, size=14)
    texto(b, x0 + 165, yy + 110, "succeed", size=36, weight="700", anchor="middle")
    lab_linea(b, x0 + 20, yy + 170, x0 + 310, "significa:")
    pista(b, x0 + 20, yy + 222, "es")
    marcas(b, x0 + 46, yy + 206, c, ("un verbo", "una cosa"))
    bx, bw = x0 + 354, ww - 354
    caja_rot(b, bx, yy, bw, 250, c, "¿QUÉ LLEVA ENCIMA?")
    for k, q in enumerate(("¿termina en -s?", "¿termina en -ed?", "¿termina en -ing?",
                           "¿tiene un sujeto pegado delante (I, he, they…)?")):
        by = yy + 70 + k * 42
        pista(b, bx + 20, by, q, size=16)
        marcas(b, bx + 420, by - 16, c, ("sí", "no"))
    lab_linea(b, bx + 20, yy + 236, bx + bw - 20, "si todo es «no», es un verbo pelado:")
    yy += 270
    caja(b, x0, yy, ww, 120, c, sw=2.2, r=14)
    rot(b, x0 + 20, yy + 30, "EL MISMO TEXTO YA LO HIZO", c, size=14)
    pista(b, x0 + 20, yy + 66, "En el primer párrafo del texto 3 hay un verbo pelado después de «use them». "
                               "Búscalo en tu libro y copia las tres palabras:")
    texto(b, x0 + 20, yy + 104, "use them", size=20, weight="700")
    hueco_caja(b, x0 + 120, yy + 78, 110, c)
    renglon(b, x0 + 244, yy + 104, x0 + 480)
    lab_linea(b, x0 + 520, yy + 104, x0 + ww - 20, "lo que hace esa palabra pequeña ahí:")
    yy += 138
    return ojo(b, x0, yy, ww, "LA VECINA DE DESPUÉS TAMBIÉN CUENTA",
               "No mires solo «essential». Antes de un verbo pelado no va cualquier palabra pequeña: va la que "
               "marca que viene un verbo. Antes de una cosa, en cambio, caben otras.")


# ───────── espacio 30 · for ─────────
def e30(b, x, y, w, h):
    c = OR
    x0, ww, yy = abre(b, x, y, w, c, 30, "¿Preparados para qué? La pregunta que contesta",
                      "Cada palabra pequeña contesta una pregunta distinta. Hazle una pregunta a «prepared», busca en "
                      "el texto la respuesta y mira qué viene después del espacio: ¿un verbo o una cosa?",
                      "…and young people must be prepared (30) ________ new technological challenges.")
    yy += 24
    caja(b, x0, yy, ww, 140, c, sw=2.4, r=16)
    rot(b, x0 + 20, yy + 30, "LE PREGUNTO A «PREPARED»", c, size=14)
    texto(b, x0 + 20, yy + 80, "«Young people must be prepared…", size=20, style="italic")
    b.append(rect(x0 + 340, yy + 50, 300, 46, tinte(c, 0.9), r=23, stroke=c, sw=2))
    pista(b, x0 + 360, yy + 80, "¿preparados ______ qué?", size=17)
    lab_linea(b, x0 + 20, yy + 122, x0 + ww - 20, "la respuesta que da el texto (después del espacio):")
    yy += 158
    hw = (ww - 24) / 2
    caja_rot(b, x0, yy, hw, 150, c, "LO QUE VIENE DESPUÉS DEL ESPACIO 30")
    texto(b, x0 + 20, yy + 76, "new technological challenges", size=19, weight="700")
    pista(b, x0 + 20, yy + 122, "es")
    marcas(b, x0 + 46, yy + 106, c, ("un verbo pelado", "una cosa (sustantivo)"))
    bx = x0 + hw + 24
    caja_rot(b, bx, yy, hw, 150, c, "COMPARO CON EL ESPACIO 29")
    pista(b, bx + 20, yy + 66, "allá venía", size=15)
    marcas(b, bx + 104, yy + 50, c, ("un verbo", "una cosa"))
    pista(b, bx + 20, yy + 110, "aquí viene", size=15)
    marcas(b, bx + 104, yy + 94, c, ("un verbo", "una cosa"))
    lab_linea(b, bx + 20, yy + 140, bx + hw - 20, "¿puede ir la misma pequeña?")
    yy += 168
    caja(b, x0, yy, ww, 100, c, r=14)
    rot(b, x0 + 20, yy + 30, "OTRA FRASE CON LA MISMA PREGUNTA", c, size=14)
    texto(b, x0 + 20, yy + 72, "«Are you ready", size=19, style="italic")
    hueco_caja(b, x0 + 152, yy + 44, 100, c)
    texto(b, x0 + 264, yy + 72, "the exam?»", size=19, style="italic")
    lab_linea(b, x0 + 400, yy + 72, x0 + ww - 20, "¿la conozco? ¿qué palabra pequeña lleva?")
    yy += 118
    return ojo(b, x0, yy, ww, "«PARA» SE DICE DE DOS MANERAS EN INGLÉS",
               "Antes de un verbo pelado va una (la del espacio 29); antes de una cosa, otra. El español usa la misma "
               "«para» en los dos casos: por eso aquí no basta con traducir, hay que mirar qué viene después.")


# ═════════ TEXTO 4 · Public Protest and Social Change ═════════

# ───────── espacio 31 · in ─────────
def e31(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Punto, superficie o recipiente: ¿cómo es el lugar?", c,
                      "Las palabras pequeñas de lugar dibujan la forma del sitio: un punto donde se está, una "
                      "superficie que se toca o un espacio con bordes donde se está adentro. Escribe la palabra inglesa "
                      "de cada dibujo y decide cómo es «cities».")
    x0, ww = x + 22, w - 44
    yy = idea_texto(b, x0, yy, ww, c) + 16
    yy = cita(b, x0, yy, ww, "In the last decade, massive demonstrations have erupted (31) ________ cities around the "
                             "world, demanding greater accountability and social justice.", c, rotulo=rotulo_cita(31))
    yy += 22
    cw = (ww - 2 * 20) / 3
    for k, rt in enumerate(("UN PUNTO", "UNA SUPERFICIE", "UN ESPACIO CON BORDES")):
        bx = x0 + k * (cw + 20)
        caja_rot(b, bx, yy, cw, 236, c, rt)
        mx, my = bx + cw / 2, yy + 100
        if k == 0:
            b.append(f'<circle cx="{mx}" cy="{my}" r="10" fill="{c}"/>')
            b.append(f'<circle cx="{mx}" cy="{my}" r="34" fill="none" stroke="{c}" stroke-width="2" '
                     f'stroke-dasharray="6,6"/>')
        elif k == 1:
            b.append(f'<polygon points="{mx - 130},{my + 30} {mx - 70},{my - 20} {mx + 130},{my - 20} '
                     f'{mx + 70},{my + 30}" fill="{tinte(c, 0.85)}" stroke="{c}" stroke-width="2.4"/>')
            _cosa(b, mx, my - 2, c, s=22)
        else:
            b.append(rect(mx - 90, my - 46, 180, 92, "white", r=10, stroke=c, sw=3))
            _cosa(b, mx, my, c, s=22)
        lab_linea(b, bx + 20, yy + 182, bx + cw - 20, "un ejemplo en español:", size=14)
        lab_linea(b, bx + 20, yy + 220, bx + cw - 20, "la palabra en inglés:", size=14)
    yy += 254
    caja(b, x0, yy, ww, 98, c, r=14)
    rot(b, x0 + 20, yy + 30, "«CITIES AROUND THE WORLD»", c, size=14)
    pista(b, x0 + 20, yy + 70, "las protestas pasan")
    xx = marcas(b, x0 + 164, yy + 54, c, ("en un punto", "sobre una superficie", "adentro de un espacio con bordes"))
    return yy + 98


# ───────── espacio 32 · ninguna (in) ─────────
def e32(b, x, y, w, h):
    c = OR
    x0, ww, yy = abre(b, x, y, w, c, 32, "Cuando ninguna opción sirve, escribo yo la palabra",
                      "Hay expresiones que se aprenden enteras, como un bloque. Lee la expresión completa, di en "
                      "español qué significa y escribe la palabra pequeña que la arma.",
                      "Citizens accuse leaders of acting (32) ________ the interests of political elites rather than "
                      "the wider population.")
    yy += 16
    yy = correccion(b, x0, yy, ww,
                    "En el libro ninguna de las tres opciones arma la expresión «acting ___ the interests of». No "
                    "marques letra en «marco al final»: tacha las tres y escribe "
                    "en la caja grande de abajo la palabra pequeña que sí va.") + 22
    caja_rot(b, x0, yy, ww, 110, c, "LA EXPRESIÓN, EN ESPAÑOL")
    lab_linea(b, x0 + 20, yy + 76, x0 + ww - 20,
              "«Los ciudadanos acusan a los líderes de actuar ______________________ de las élites políticas»:")
    yy += 128
    caja(b, x0, yy, ww, 190, c, sw=3, r=18, fill=tinte(c, 0.95))
    rot(b, x0 + 22, yy + 32, "LA PALABRA QUE VA · LA ESCRIBO YO", c, size=14)
    texto(b, x0 + 22, yy + 118, "acting", size=28, weight="700")
    b.append(rect(x0 + 130, yy + 72, 180, 70, "white", r=12, stroke=c, sw=3))
    texto(b, x0 + 326, yy + 118, "the interests of…", size=28, weight="700")
    lab_linea(b, x0 + 600, yy + 90, x0 + ww - 20, "por qué ninguna de las tres arma la expresión:")
    renglon(b, x0 + 600, yy + 140, x0 + ww - 20)
    yy += 208
    caja(b, x0, yy, ww, 100, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PRUEBA", c, size=14)
    lab_linea(b, x0 + 20, yy + 72, x0 + ww - 20,
              "otra expresión en inglés que conozca con «interest» o con la misma palabra pequeña:")
    return yy + 100


# ───────── espacio 33 · across ─────────
def e33(b, x, y, w, h):
    c = OR
    x0, ww, yy = abre(b, x, y, w, c, 33, "El dibujo del movimiento",
                      "Algunas palabras pequeñas dibujan cómo se mueve algo: siguiendo una línea, por dentro de un "
                      "túnel o de un lado a otro de una superficie. Escribe la palabra inglesa de cada dibujo y "
                      "decide cómo se mueve la inestabilidad por «entire regions».",
                      "…in many places they have escalated into violent clashes, leading to instability (33) ________ "
                      "entire regions.")
    yy += 24
    cw = (ww - 2 * 20) / 3
    for k, rt in enumerate(("SIGUE UNA LÍNEA", "PASA POR DENTRO", "VA DE UN LADO AL OTRO")):
        bx = x0 + k * (cw + 20)
        caja_rot(b, bx, yy, cw, 250, c, rt)
        mx, my = bx + cw / 2, yy + 104
        if k == 0:
            b.append(f'<path d="M {mx - 150} {my + 20} Q {mx - 50} {my - 40} {mx + 30} {my + 10} T {mx + 150} {my - 10}" '
                     f'fill="none" stroke="{tinte(c, 0.5)}" stroke-width="12"/>')
            flecha(b, mx - 140, my + 2, mx + 140, my - 26, c, sw=3, head=12, bend=0.1)
        elif k == 1:
            b.append(rect(mx - 90, my - 36, 180, 72, tinte(c, 0.85), r=36, stroke=c, sw=2.4))
            flecha(b, mx - 150, my, mx + 150, my, c, sw=3, head=12)
        else:
            b.append(f'<polygon points="{mx - 140},{my + 46} {mx - 90},{my - 40} {mx + 140},{my - 40} '
                     f'{mx + 90},{my + 46}" fill="{tinte(c, 0.85)}" stroke="{c}" stroke-width="2.4"/>')
            flecha(b, mx - 115, my + 4, mx + 115, my + 4, c, sw=3, head=12, bend=-0.15)
        lab_linea(b, bx + 20, yy + 196, bx + cw - 20, "en español:", size=14)
        lab_linea(b, bx + 20, yy + 234, bx + cw - 20, "en inglés:", size=14)
    yy += 268
    caja(b, x0, yy, ww, 144, c, r=14)
    rot(b, x0 + 20, yy + 30, "«ENTIRE REGIONS» = REGIONES ENTERAS", c, size=14)
    pista(b, x0 + 20, yy + 70, "la inestabilidad")
    marcas(b, x0 + 140, yy + 54, c, ("sigue una línea", "pasa por dentro de algo", "se extiende de un lado a otro"))
    lab_linea(b, x0 + 20, yy + 118, x0 + ww - 20, "la palabra del texto que me lo dice:")
    yy += 162
    return ojo(b, x0, yy, ww, "PIENSA EN UN MAPA",
               "Imagina cómo se vería en un mapa algo que afecta regiones enteras, y compara ese mapa con tus tres "
               "dibujos antes de marcar. Si dudas entre dos, escribe en el salvavidas por qué te quedas con uno.")


# ───────── espacio 34 · as / since / because ─────────
def e34(b, x, y, w, h):
    c = MO
    x0, ww, yy = abre(b, x, y, w, c, 34, "Quita el conector: ¿qué relación queda?",
                      "Una buena prueba para un conector es quitarlo. Parte la oración en dos con un punto, léelas "
                      "seguidas y fíjate qué relación pone tu cabeza entre ellas sin que nadie se la diga.",
                      "These mobilizations are powerful, (34) ________ they reveal deep frustration with inequality and "
                      "corruption.")
    yy += 16
    yy = correccion(b, x0, yy, ww,
                    "Las tres opciones de tu libro dicen la misma relación y las tres son correctas en este lugar. "
                    "Marca la que usarías tú y escribe en el salvavidas la pista que te dice cuál es la relación.") + 22
    caja_rot(b, x0, yy, ww, 160, c, "LA PARTO EN DOS, CON UN PUNTO Y SIN CONECTOR")
    texto(b, x0 + 20, yy + 74, "1.", size=20, color=c, weight="700")
    renglon(b, x0 + 50, yy + 76, x0 + ww - 20)
    texto(b, x0 + 20, yy + 126, "2.", size=20, color=c, weight="700")
    renglon(b, x0 + 50, yy + 128, x0 + ww - 20)
    yy += 178
    caja_rot(b, x0, yy, ww, 120, c, "LO QUE MI CABEZA PONE ENTRE LAS DOS, EN ESPAÑOL")
    texto(b, x0 + 20, yy + 84, "«Estas movilizaciones son poderosas,", size=19, style="italic")
    hueco_caja(b, x0 + 340, yy + 56, 150, c)
    texto(b, x0 + 504, yy + 84, "revelan una frustración profunda…»", size=19, style="italic")
    yy += 138
    rw = (ww - 3 * 14) / 4
    for k, (lab, tipo) in enumerate((("se suman", "suma"), ("se oponen", "contraste"),
                                     ("la 2 es la razón de la 1", "causa"), ("la 2 es el resultado", "resultado"))):
        bx = x0 + k * (rw + 14)
        caja(b, bx, yy, rw, 96, c, r=12)
        _icono(b, bx + 50, yy + 48, tipo, c)
        pista(b, bx + 94, yy + 54, lab, size=15)
        b.append(checkbox(bx + rw - 36, yy + 14, s=10, c=c))
    return yy + 96


def _icono(b, cx, cy, tipo, c):
    """Dibujo de la relación: suma (+), oposición (→ ←), causa (←), resultado (→)."""
    if tipo == "suma":
        b.append(line(cx - 14, cy, cx + 14, cy, c, 5))
        b.append(line(cx, cy - 14, cx, cy + 14, c, 5))
    elif tipo == "contraste":
        flecha(b, cx - 30, cy, cx - 5, cy, c, sw=3.4, head=10)
        flecha(b, cx + 30, cy, cx + 5, cy, c, sw=3.4, head=10)
    elif tipo == "causa":
        flecha(b, cx + 26, cy, cx - 26, cy, c, sw=3.4, head=11)
    else:
        flecha(b, cx - 26, cy, cx + 26, cy, c, sw=3.4, head=11)


# ───────── espacio 35 · through / on ─────────
def e35(b, x, y, w, h):
    c = OR
    x0, ww, yy = abre(b, x, y, w, c, 35, "El mensaje viaja: ¿por un canal o se queda en un lugar?",
                      "Una plataforma digital se puede imaginar de dos maneras: como un tubo por donde pasa el mensaje "
                      "o como una plaza donde queda puesto. Cada imagen tiene su palabra pequeña en inglés.",
                      "Protesters frequently communicate (35) ________ digital platforms, sharing videos and "
                      "coordinating marches in real time.")
    yy += 16
    yy = correccion(b, x0, yy, ww,
                    "Dos de las tres opciones de tu libro son correctas en inglés y el libro espera solo una. Marca la "
                    "tuya y escribe en el salvavidas cuál de los dos dibujos te la dio.") + 22
    hw = (ww - 24) / 2
    for k, rt in enumerate(("IMAGEN 1 · UN CANAL POR DONDE PASA", "IMAGEN 2 · UN LUGAR DONDE QUEDA PUESTO")):
        bx = x0 + k * (hw + 24)
        caja_rot(b, bx, yy, hw, 262, c, rt)
        mx, my = bx + hw / 2, yy + 110
        if k == 0:
            for sx in (mx - 220, mx + 190):
                b.append(rect(sx, my - 40, 30, 60, "white", r=6, stroke=c, sw=2.4))
            b.append(rect(mx - 170, my - 22, 340, 24, tinte(c, 0.85), r=12, stroke=c, sw=2))
            flecha(b, mx - 150, my - 10, mx + 150, my - 10, c, sw=3, head=11)
        else:
            b.append(rect(mx - 170, my - 50, 340, 90, tinte(c, 0.88), r=10, stroke=c, sw=2.4))
            for j in range(4):
                b.append(rect(mx - 150 + j * 80, my - 34, 60, 44, "white", r=4, stroke=c, sw=1.8))
        lab_linea(b, bx + 20, yy + 196, bx + hw - 20, "la plataforma es como:", size=14)
        lab_linea(b, bx + 20, yy + 238, bx + hw - 20, "la palabra pequeña en inglés:", size=14)
    yy += 280
    caja(b, x0, yy, ww, 100, c, r=14)
    rot(b, x0 + 20, yy + 30, "EN EL TEXTO", c, size=14)
    pista(b, x0 + 20, yy + 70, "«sharing videos and coordinating marches» me hace pensar en la")
    xx = marcas(b, x0 + 470, yy + 54, c, ("imagen 1", "imagen 2", "las dos"))
    lab_linea(b, xx + 10, yy + 70, x0 + ww - 20, "porque:")
    return yy + 100


# ───────── espacio 37 · with ─────────
def e37(b, x, y, w, h):
    c = OR
    x0, ww, yy = abre(b, x, y, w, c, 37, "La balanza de «instead of»",
                      "«instead of» (en lugar de) pone dos cosas en una balanza: lo que se espera y lo que no. Llena "
                      "los dos platillos y después piensa qué palabra une «respond» con lo que el gobierno entrega "
                      "como respuesta.",
                      "Governments are therefore expected to respond (37) ________ concrete reforms, instead of "
                      "symbolic promises.")
    yy += 30
    mx = x0 + ww / 2
    b.append(f'<polygon points="{mx - 40},{yy + 250} {mx + 40},{yy + 250} {mx},{yy + 40}" fill="{tinte(c, 0.85)}" '
             f'stroke="{c}" stroke-width="2.4"/>')
    b.append(line(mx - 400, yy + 40, mx + 400, yy + 40, c, 4))
    for k, (rt, ps) in enumerate((("LO QUE SÍ SE ESPERA", "lo que va antes de instead of"),
                                  ("LO QUE NO (INSTEAD OF)", "lo que va después de instead of"))):
        px = mx - 400 if k == 0 else mx + 400
        b.append(line(px, yy + 40, px - 120, yy + 120, c, 2))
        b.append(line(px, yy + 40, px + 120, yy + 120, c, 2))
        b.append(f'<path d="M {px - 170} {yy + 120} L {px + 170} {yy + 120} Q {px + 150} {yy + 190} {px} {yy + 190} '
                 f'Q {px - 150} {yy + 190} {px - 170} {yy + 120} Z" fill="white" stroke="{c}" stroke-width="2.4"/>')
        rot(b, px, yy + 146, rt, c, size=13, anchor="middle")
        renglon(b, px - 130, yy + 180, px + 130)
        pista(b, px, yy + 220, ps, size=14, anchor="middle")
    yy += 270
    caja(b, x0, yy, ww, 160, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA REESCRIBO SIN EL ESPACIO", c, size=14)
    texto(b, x0 + 20, yy + 76, "«Governments are expected to give", size=19, style="italic")
    renglon(b, x0 + 340, yy + 78, x0 + 700)
    texto(b, x0 + 712, yy + 76, ", not symbolic promises.»", size=19, style="italic")
    lab_linea(b, x0 + 20, yy + 130, x0 + ww - 20,
              "con «respond» hace falta una palabra pequeña delante de lo que se entrega como respuesta; la que yo diría:")
    yy += 178
    return trampa(b, x0, yy, ww, "Antes de marcar, mira qué viene después del espacio:",
                  "¿es la persona a quien se le responde, o es lo que se le entrega como respuesta? Cada idea lleva su "
                  "palabra pequeña en inglés, y no siempre es la que dictaría el español.", c)


# ───────── espacio 39 · since / but ─────────
def e39(b, x, y, w, h):
    c = MO
    x0, ww, yy = abre(b, x, y, w, c, 39, "¿Qué pregunta contesta la segunda idea?",
                      "Cuando una oración tiene dos ideas, la segunda casi siempre le contesta una pregunta a la "
                      "primera. Escribe las dos ideas en español y prueba qué pregunta contesta la segunda.",
                      "This participation requires both courage and organization, (39) ________ it cannot succeed "
                      "without broad alliances across society.")
    yy += 16
    yy = correccion(b, x0, yy, ww,
                    "Aquí se defienden dos opciones, según cómo leas la relación: la segunda idea como la razón de la "
                    "primera, o como un «pero» que agrega una condición más. El libro espera una. Escribe qué relación "
                    "lees tú y defiéndela en clase.") + 22
    hw = (ww - 90) / 2
    for k, rt in enumerate(("IDEA 1, EN ESPAÑOL", "IDEA 2, EN ESPAÑOL")):
        bx = x0 + k * (hw + 90)
        caja_rot(b, bx, yy, hw, 120, c, rt, sw=2.4)
        renglon(b, bx + 20, yy + 70, bx + hw - 20)
        renglon(b, bx + 20, yy + 106, bx + hw - 20)
    b.append(f'<circle cx="{x0 + hw + 45}" cy="{yy + 60}" r="28" fill="white" stroke="{c}" stroke-width="2.6"/>')
    texto(b, x0 + hw + 45, yy + 70, "?", size=26, color=c, weight="700", anchor="middle")
    yy += 140
    qw = (ww - 2 * 18) / 3
    for k, q in enumerate(("¿Por qué lo necesita?", "¿Y qué más hace falta?", "¿Qué pasa aunque lo tenga?")):
        bx = x0 + k * (qw + 18)
        b.append(rect(bx, yy, qw, 120, "white", r=24, stroke=c, sw=2))
        texto(b, bx + 22, yy + 40, q, size=18, weight="700", color=c)
        b.append(checkbox(bx + 22, yy + 62, s=10, c=c))
        pista(b, bx + 52, yy + 79, "la idea 2 la contesta", size=15)
        pista(b, bx + 22, yy + 108, "suena: bien / raro", size=14)
    yy += 138
    caja(b, x0, yy, ww, 96, c, r=14)
    rot(b, x0 + 20, yy + 30, "MI DEFENSA", c, size=14)
    lab_linea(b, x0 + 20, yy + 70, x0 + ww - 20, "la relación que leo y la palabra del texto que me la da:")
    return yy + 96


# ───────── espacio 40 · undeniable ─────────
def e40(b, x, y, w, h):
    c = RO
    x0, ww, yy = abre(b, x, y, w, c, 40, "El sándwich entre el artículo y el sustantivo",
                      "El espacio 40 está entre dos panes: una palabra que anuncia una cosa y la cosa. Lo que va en "
                      "medio de un sándwich así siempre es de la misma clase. Descubre cuál con una familia de palabras "
                      "que ya conoces del texto 3.",
                      "In conclusion, protests remain an (40) ________ reminder that freedom is preserved only when "
                      "citizens actively defend it.")
    yy += 24
    sw_, sx = 520, x0
    b.append(rect(sx, yy, sw_, 56, tinte(c, 0.85), r=28, stroke=c, sw=2.4))
    texto(b, sx + sw_ / 2, yy + 37, "an  ·  el artículo", size=19, weight="700", anchor="middle")
    b.append(rect(sx + 20, yy + 66, sw_ - 40, 70, "white", r=10, stroke=c, sw=2.4, dash="9,6"))
    pista(b, sx + sw_ / 2, yy + 108, "(40) ¿qué clase de palabra va aquí?", anchor="middle")
    b.append(rect(sx, yy + 146, sw_, 56, tinte(c, 0.85), r=28, stroke=c, sw=2.4))
    texto(b, sx + sw_ / 2, yy + 183, "reminder  ·  el sustantivo", size=19, weight="700", anchor="middle")
    bx, bw = x0 + sw_ + 30, ww - sw_ - 30
    caja_rot(b, bx, yy, bw, 202, c, "LA CLASE DEL RELLENO")
    pista(b, bx + 20, yy + 64, "entre un artículo y un sustantivo va")
    marcas(b, bx + 20, yy + 80, c, ("un verbo", "un adjetivo", "un adverbio"))
    lab_linea(b, bx + 20, yy + 150, bx + bw - 20, "un ejemplo en español: «un ______ recordatorio»:")
    pista(b, bx + 20, yy + 186, "(un recordatorio ¿cómo? → esa palabra dice cómo es la cosa)", size=14)
    yy += 222
    cols = (300, (ww - 300) / 2, (ww - 300) / 2)
    caja(b, x0, yy, ww, 44, c, fill=tinte(c), r=8)
    for k, hd in enumerate(("CLASE", "LA FAMILIA DE «SUCCESS» (TEXTO 3)", "LA FAMILIA DEL ESPACIO 40")):
        rot(b, x0 + sum(cols[:k]) + 14, yy + 28, hd, c, size=13)
    ry = yy + 44
    for f, (cl, ej) in enumerate((("verbo", "succeed"), ("adjetivo · termina en -ful / -able", ""),
                                  ("adverbio · termina en -ly", ""))):
        caja(b, x0, ry, ww, 56, c, r=0)
        texto(b, x0 + 14, ry + 35, cl, size=16, weight="700")
        if ej:
            texto(b, x0 + cols[0] + 14, ry + 36, ej, size=18, style="italic")
        else:
            renglon(b, x0 + cols[0] + 14, ry + 42, x0 + cols[0] + cols[1] - 14)
        renglon(b, x0 + cols[0] + cols[1] + 14, ry + 42, x0 + ww - 14)
        ry += 56
    for k in (1, 2):
        b.append(line(x0 + sum(cols[:k]), yy, x0 + sum(cols[:k]), ry, c, 1.6))
    pista(b, x0, ry + 26, "En la última columna, escribe cada opción de tu libro en la fila de su clase.")
    return ry + 34



# ═════════ las 40 tarjetas ═════════
PAG = {1: 435, 2: 435, 3: 436, 4: 437}
NOMBRE = {1: "Karol G en Medellín", 2: "Spider-Verse", 3: "AI in the Classroom", 4: "Public Protest"}
PASO = {1: "paso 1 · leo todo el texto", 2: "paso 2 · ¿qué pieza falta?", 3: "paso 3 · la pista vecina",
        4: "paso 4 · llamo a la subestrategia"}
#        espacio: (subestrategia, paso de la estrategia)
PLAN = {1: (1, 1), 2: (1, 3), 3: (2, 4), 4: (1, 3), 5: (2, 3), 6: (1, 3), 7: (1, 2), 8: (2, 4), 9: (1, 1),
        10: (2, 2), 11: (1, 1), 12: (2, 2), 13: (2, 3), 14: (1, 3), 15: (1, 3), 16: (2, 3), 17: (1, 2),
        18: (1, 3), 19: (2, 4), 20: (1, 1), 21: (3, 1), 22: (3, 3), 23: (3, 3), 24: (3, 2), 25: (4, 2),
        26: (3, 3), 27: (3, 3), 28: (3, 3), 29: (2, 3), 30: (3, 2), 31: (3, 1), 32: (3, 4), 33: (3, 3),
        34: (4, 2), 35: (3, 2), 36: (4, 3), 37: (3, 2), 38: (4, 3), 39: (4, 2), 40: (2, 3)}
L3 = "ABC"


def _q(n):
    t = texto_de(n)
    est, paso = PLAN[n]
    ctx = f"Texto {t} · {NOMBRE[t]} · {PASO[paso]}"
    return dict(n=n, est=est, pag=PAG[t], ctx=ctx, inst=globals()[f"e{n}"], letras=L3)


Q = {n: _q(n) for n in range(1, 41) if f"e{n}" in globals()}
PAGINAS = tuple(range(289, 299)) + tuple(range(300, 310))


def build(pages=PAGINAS):
    out = []
    for k in range(20):
        a, b_ = 2 * k + 1, 2 * k + 2
        if a in Q and b_ in Q:
            out.append(hoja_taller(f"ing3_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
