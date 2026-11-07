#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 3 · componente gramatical · léxico · páginas 283–289.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 3» de Inglés (fuente_libro/INGLÉS), páginas 435–437.
El libro trae CUATRO textos con espacios y 40 espacios (más el ejemplo 0), todos con tres
opciones (A–C): el concierto de Karol G en Medellín (0 a 10, tiempos simples), la película
Spider-Man: Across the Spider-Verse (11 a 20), la inteligencia artificial en el aula (21 a 30,
preposiciones) y la protesta social (31 a 40, conectores y preposiciones).

El cuaderno trabaja 10 de los 40 espacios (una pregunta por tarjeta, como en todas las áreas),
escogidos para que estén los cuatro movimientos de la misión y ninguno de los espacios con
problemas. El resto se resuelve en el libro. Equivalencia (pregunta del cuaderno → espacio):

    1 → 1    2 → 5    3 → 9    4 → 13    5 → 15    6 → 22    7 → 25    8 → 27    9 → 36    10 → 38

Claves verificadas (resueltas a mano contra el texto del libro, 7 nov 2026):

    1·C  2·B  3·A  4·C  5·A  6·B  7·B  8·A  9·C  10·A

  1 · C came: «Last month» y el ejemplo (0) gave ponen la historia en pasado; come (presente)
      concuerda con «fans» pero no con el tiempo; comes además es singular.
  2 · B were: «People» es plural en inglés (they) y el texto va en pasado. is: singular y
      presente; are: plural pero presente.
  3 · A thought: «Everyone» es singular (thinks concuerda), pero todo el párrafo va en pasado
      (came, began, sang, knew, were, presented, lasted, shared): thought. think no concuerda.
  4 · C went: gone es participio y necesitaría auxiliar (have gone); go es presente.
  5 · A used: «and» une dos verbos con el mismo sujeto (The movie introduced … and used …), y en
      la misma oración «critics admired» va en pasado. uses / use rompen el paralelo.
  6 · B for: search for (buscar algo). of y to no forman la colocación.
  7 · B because: la segunda mitad (it helps students understand) da la razón de la primera
      (AI can be useful). so pondría la ayuda como consecuencia; but, como contraste.
  8 · A with: combine X with Y. at y to no se usan con combine.
  9 · C Despite: el sentido es de contraste (oportunidades / riesgos) y lo que sigue es solo un
      sustantivo («these opportunities»), sin verbo: despite + sustantivo. Although pide una
      oración con verbo; However va solo, seguido de coma, y no rige un sustantivo.
 10 · A but also: correlativo «not only … but also». and y so no cierran la pareja.

Reparto: A 4 · B 3 · C 3. Equilibrado. Reparto de los 39 espacios del libro que tienen clave: A 12 · B 12 · C 15
(el 32 no tiene ninguna opción correcta). Los espacios con problemas (12, 18–20, 24, 32, 34, 35, 39, 40)
están en tablero/propuestas/ing3_hallazgos.csv.

Estrategias:
    1 · El reloj del texto            (1, 3, 5   · ICFES ex. 1 · 10)   azul
    2 · La forma que cabe             (2, 4      · ICFES ex. 1 · 13)   rojo
    3 · La preposición viene pegada   (6, 8      · ICFES ex. 2 · 24)   oro
    4 · El conector dice la relación  (7, 9, 10  · ICFES ex. 1 · 16)   morado

Hojas: 283 ing3_t1 (1-2) · 284 ing3_t2 (3-4) · 285 ing3_i1 · 286 ing3_t3 (5-6) ·
       287 ing3_t4 (7-8) · 288 ing3_t5 (9-10) · 289 ing3_i2.
"""
from taller_base import *

configurar("Inglés", 3, "gramatical · léxico",
           tema="Cada espacio pide su palabra: tiempo, forma y conector",
           nota="LO QUE ME DIJO LA ORACIÓN")
MORADO = "#5B3E96"
EST = {1: ("El reloj del texto", EDU_AZUL),
       2: ("La forma que cabe", EDU_ROJO),
       3: ("La preposición viene pegada", EDU_ORO),
       4: ("El conector dice la relación", MORADO)}
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


# ───────── P1 · espacio 1 · came ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La línea de tiempo del concierto de Medellín", c,
                      "Antes de mirar las opciones, decide cuándo pasa lo que cuenta el texto. La pista de tiempo "
                      "está escrita en la primera línea: encuéntrala, ponla en la línea y deja que ella escoja el verbo.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "Last month, Karol G (0) gave a massive concert in Medellín, her hometown. "
                             "Thousands of fans (1) ________ to the stadium early in the morning.", c)
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


# ───────── P2 · espacio 5 · were ─────────
def i2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La tabla del verbo to be, llenada por mí", c,
                      "Para escoger la forma de to be hay que pasar dos filtros: cuántos son y cuándo. Llena la tabla "
                      "con lo que sabes; después cruza la fila del sujeto con la columna del tiempo.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "People (5) ________ very excited because she also (6) ________ a new song for "
                             "the first time.", c)
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


# ───────── P3 · espacio 9 · thought ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El párrafo tiene un solo reloj: cuéntalo verbo por verbo", c,
                      "Un texto que cuenta una historia no cambia de tiempo a cada rato. Copia los verbos que ya "
                      "escogiste en los espacios 0 a 8 y marca en qué tiempo está cada uno. El conteo te dice la hora.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "…and at the end she (8) ________ a message of love and gratitude. Everyone "
                             "(9) ________ the night (10) ________ unforgettable.", c)
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


# ───────── P4 · espacio 13 · went ─────────
def i4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Las tres caras de cada verbo", c,
                      "Muchos verbos del inglés cambian de cara: una para hoy, otra para el pasado y otra que solo "
                      "sale acompañada de has, have, had o was. Llena las caras y mira qué hay justo antes del espacio.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "It (12) ________ in cinemas around the world and millions of people (13) ________ "
                             "to see it.", c)
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


# ───────── P5 · espacio 15 · used ─────────
def i5(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos vagones enganchados por and", c,
                      "Cuando and engancha dos verbos del mismo sujeto, los dos vagones viajan en el mismo tiempo. "
                      "Llena el vagón 14 primero y copia su tiempo en el 15. Busca también el otro verbo que ya trae la "
                      "oración.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "The movie (14) ________ new characters and (15) ________ a unique animation style "
                             "that many critics admired.", c)
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


# ───────── P6 · espacio 22 · for ─────────
def i6(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "En español no hace falta; en inglés, sí", c,
                      "Hay verbos que en español van directo a la cosa y en inglés piden una preposición pegada. "
                      "Escribe en cada fila la que agrega el inglés. No se traduce palabra por palabra: se aprende con "
                      "el verbo.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "Many students use them to practice English, do homework, or search (22) ________ "
                             "information.", c)
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


# ───────── P7 · espacio 25 · because ─────────
def i7(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La flecha entre las dos mitades", c,
                      "Un conector dice qué hace la segunda mitad con la primera. Antes de mirar las opciones, lee las "
                      "dos mitades por separado y decide hacia dónde apunta la flecha.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "On the other hand, AI can be useful (25) ________ it helps students understand "
                             "complex topics.", c)
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


# ───────── P8 · espacio 27 · with ─────────
def i8(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El puente entre technology y creativity", c,
                      "El verbo combine junta dos cosas. Dibuja qué queda a cada lado del puente y escribe en el puente "
                      "la palabra que las une. Esta vez pregúntale al español y después compruébalo en inglés.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "Some experts say that technology should be combined (27) ________ creativity and "
                             "human effort.", c)
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


# ───────── P9 · espacio 36 · Despite ─────────
def i9(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Lo que viene después del conector: ¿trae verbo o no?", c,
                      "Dos conectores pueden decir lo mismo y no caber en el mismo lugar. Primero decide la relación; "
                      "después mira qué viene entre el espacio y la coma. Esa mirada decide.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "(36) ________ these opportunities, online activism can also create new risks, such as "
                             "misinformation or polarization.", c)
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


# ───────── P10 · espacio 38 · but also ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Palabras que llegan en pareja", c,
                      "Algunos conectores vienen en dos partes: si aparece la primera, la segunda tiene que llegar "
                      "después. Encuentra en la oración la primera mitad y escribe la pareja completa.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "In addition, social movements remind us that democracy depends not only on elections "
                             "(38) ________ on constant participation and civic engagement.", c)
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


L3 = "ABC"
Q = {1: dict(n=1, est=1, pag=435, ctx="Karol G en Medellín · el espacio 1 del texto", inst=i1, letras=L3),
     2: dict(n=2, est=2, pag=435, ctx="Karol G en Medellín · el espacio 5 del texto", inst=i2, letras=L3),
     3: dict(n=3, est=1, pag=435, ctx="Karol G en Medellín · el espacio 9 del texto", inst=i3, letras=L3),
     4: dict(n=4, est=2, pag=436, ctx="Spider-Verse · el espacio 13 (texto en la p. 435)", inst=i4, letras=L3),
     5: dict(n=5, est=1, pag=436, ctx="Spider-Verse · el espacio 15 (texto en la p. 435)", inst=i5, letras=L3),
     6: dict(n=6, est=3, pag=436, ctx="AI in the Classroom · el espacio 22", inst=i6, letras=L3),
     7: dict(n=7, est=4, pag=436, ctx="AI in the Classroom · el espacio 25", inst=i7, letras=L3),
     8: dict(n=8, est=3, pag=436, ctx="AI in the Classroom · el espacio 27", inst=i8, letras=L3),
     9: dict(n=9, est=4, pag=437, ctx="Public Protest and Social Change · el espacio 36", inst=i9, letras=L3),
     10: dict(n=10, est=4, pag=437, ctx="Public Protest and Social Change · el espacio 38", inst=i10, letras=L3)}


def build(pages=(283, 284, 286, 287, 288)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"ing3_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
