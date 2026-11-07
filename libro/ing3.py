#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 3 · Parte 4 del ICFES · componente gramatical · léxico · páginas 283–289.

FORMATO NUEVO (muestra para que Nelson lo apruebe, 7 nov 2026). La versión anterior, una tarjeta por
pregunta con 10 de los 40 espacios, está guardada en ing3_v1.py (OJO: su build() escribe los mismos
ing3_t1…t5; no correrla sin cambiarle los nombres).

En Inglés el examen viene por partes y cada parte evalúa una cosa distinta. La Misión 3 es la
Parte 4: un texto con espacios y tres opciones por espacio (gramática). Se trabaja con UNA estrategia
(«Escucha a los vecinos del hueco», 4 pasos) y 4 subestrategias, cada una con su mini-instrumento;
el instrumento es por subestrategia y no por pregunta (excepción a la regla 4, aprobada solo para
Inglés). Se cubren LOS 40 ESPACIOS del libro, una fila por espacio.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 3» de Inglés (fuente_libro/INGLÉS), páginas 435–437. Cuatro
textos: Karol G en Medellín (0 a 10), Spider-Man: Across the Spider-Verse (11 a 20), AI in the
Classroom (21 a 30) y Public Protest and Social Change (31 a 40). Opciones A–C.

Hojas:
    283 ing3_t1 · la Parte 4 y su estrategia (4 pasos, 4 subestrategias, un espacio en voz alta)
    284 ing3_t2 · textos 1 y 2 (espacios 1 a 20)
    285 ing3_i1 · entrenamiento ICFES (ing3_icfes.py, sin cambios)
    286 ing3_t3 · texto 3 (21 a 30) + reto en equipo «El duelo de las pistas»
    287 ing3_t4 · texto 4 (31 a 40) + cierre de la Parte 4 (salvavidas, mapa de errores, lo que me llevo)
    288 ing3_t5 · mi diccionario de la Parte 4
    289 ing3_i2 · entrenamiento ICFES (ing3_icfes.py, sin cambios)

Claves de los 40 espacios (resueltas a mano contra el texto del libro, 7 nov 2026; el cuaderno NO las
imprime, van al planeador):

    Texto 1 ·  1·C came   2·A began   3·B sang   4·C knew   5·B were   6·A presented   7·C lasted
               8·B shared   9·A thought   10·C was
    Texto 2 · 11·B was   12·— (ver corrección)   13·C went   14·C introduced   15·A used   16·C were
              17·B combined   18·A dealt*   19·C tried*   20·B left*
    Texto 3 · 21·A among   22·B for   23·C on   24·A by*   25·B because   26·C by   27·A with
              28·C for   29·B to   30·A for
    Texto 4 · 31·B in   32·— (ninguna; va «in»)   33·C across   34·C because*   35·A through*
              36·C Despite   37·B with   38·A but also   39·C since*   40·A undeniable

    * clave que espera el libro en un espacio con más de una respuesta defendible (ver correcciones).

Correcciones EDUCATE impresas en la fila (hallazgos de tablero/propuestas/ing3_hallazgos.csv):
    12      la opción A está mal escrita («was release» → «was released»): se corrige a lápiz.
    18–20   valen pasado y presente narrativo: escoger un tiempo y sostenerlo en los tres.
    24      by, with y through se defienden las tres.
    32      ninguna opción sirve: no marcar letra, escribir la palabra que va (in).
    34      as, since y because son correctas las tres.
    35      dos opciones correctas (through y on); el libro espera una.
    39      dos se defienden (since: la razón; but: una condición más).
    33 y 40 son «Atención» (through se defiende en 33; el «an» delata la 40): no se imprimen, van al
    planeador (tablero/propuestas/ing3_v2_notas.md).

Subestrategias (los nombres y colores no cambian: las hojas ICFES 285 y 289 los usan):
    1 · El reloj del texto            azul   línea de tiempo con tres zonas y el puente
    2 · La forma que cabe             rojo   las caras del verbo y tres filtros
    3 · La preposición viene pegada   oro    el imán de palabras pegadas y la trampa del español
    4 · El conector dice la relación  morado dos ideas, el hueco y cuatro relaciones dibujadas
"""
from ingles_base import *   # noqa: F401,F403  (taller_base, lib y las piezas de Inglés)
from ingles_base import _icono_relacion

configurar("Inglés", 3, "gramatical · léxico",
           tema="Parte 4 del ICFES · un texto con espacios: cada espacio pide su pieza",
           nota="LO QUE ME DIJO LA ORACIÓN")
MORADO = "#5B3E96"
EST = {1: ("El reloj del texto", EDU_AZUL),
       2: ("La forma que cabe", EDU_ROJO),
       3: ("La preposición viene pegada", EDU_ORO),
       4: ("El conector dice la relación", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))
PARTE = 4
PAG_DICC = 288


# ───────── hoja 1 · la muestra esquemática de la Parte 4 ─────────
def muestra_parte4(b, x, y, w, h):
    """Cómo se ve la Parte 4, sin contenido: renglones de texto, huecos numerados y A B C."""
    c = A["color"]
    gris = "#DCE2E9"
    b.append(rect(x, y, w, h - 40, "#F7F9FB", r=16, stroke="#C9CED6", sw=1.6))
    filas = [(0.30, 1, 0.42), (0.18, 2, 0.55), (0.52, 3, 0.20), (0.60, None, 0)]
    yy = y + 26
    for a, n, z in filas:
        x0 = x + 26
        x1 = x + w - 26
        ancho = x1 - x0
        b.append(rect(x0, yy, ancho * a, 18, gris, r=9))
        if n:
            hx = x0 + ancho * a + 12
            b.append(rect(hx, yy - 9, 96, 36, "white", r=8, stroke=c, sw=2.2))
            b.append(T(hx + 22, yy + 15, [f"({n})"], 18, c, weight="700"))
            b.append(line(hx + 52, yy + 18, hx + 84, yy + 18, c, 2))
            b.append(rect(hx + 108, yy, x1 - hx - 108, 18, gris, r=9))
        yy += 38
    yy += 2
    b.append(T(x + 26, yy + 18, ["(1)"], 18, c, weight="700"))
    ox = x + 74
    for L in "ABC":
        b.append(f'<circle cx="{ox + 14}" cy="{yy + 12}" r="14" fill="white" stroke="{c}" stroke-width="2"/>')
        b.append(T(ox + 14, yy + 18, [L], 15, c, weight="700", anchor="middle"))
        b.append(rect(ox + 36, yy + 4, 110, 16, gris, r=8))
        ox += 172
    pista(b, x + w / 2, y + h - 8, "un texto corto · espacios numerados · tres palabras por espacio",
          size=16, anchor="middle")


# ───────── hoja 1 · los mini-instrumentos de las subestrategias ─────────
def inst_reloj(b, x, y, w, h):
    """1 · línea de tiempo con tres zonas y el puente (desde antes hasta hoy)."""
    c = AZ
    ly = y + 46
    b.append(line(x + 6, ly, x + w - 22, ly, c, 4))
    b.append(f'<polygon points="{x + w - 24},{ly - 11} {x + w - 4},{ly} {x + w - 24},{ly + 11}" fill="{c}"/>')
    zw = (w - 30) / 3
    zonas = (("ANTES · YA PASÓ", "yesterday · ago · in 1990"),
             ("SIEMPRE · AHORA", "every day · usually · now"),
             ("DESPUÉS", "tomorrow · next week · soon"))
    for k, (rt, ej) in enumerate(zonas):
        zx = x + 6 + k * zw
        if k:
            b.append(line(zx, ly - 16, zx, ly + 16, c, 3))
        rot(b, zx + zw / 2, ly - 18, rt, c, size=13, anchor="middle")
        b.append(rect(zx + 8, ly + 26, zw - 16, 104, "white", r=12, stroke=tinte(c, 0.6), sw=2))
        pista(b, zx + zw / 2, ly + 52, ej, size=15, anchor="middle")
        b.append(T(zx + 22, ly + 84, ["las que encontré:"], 14, GRAY))
        renglon(b, zx + 22, ly + 118, zx + zw - 22, LN)
    py = ly + 146
    b.append(rect(x, py, w, 92, tinte(c, 0.93), r=12))
    rot(b, x + 20, py + 26, "EL PUENTE", c, size=13)
    flecha(b, x + 26, py + 70, x + 196, py + 70, c, sw=3, head=11, bend=-0.35)
    b.append(T(x + 220, py + 48, ["has / have + participio: empezó antes"], 18, INK))
    b.append(T(x + 220, py + 74, ["y llega hasta hoy (no es un pasado cerrado)"], 18, INK))
    return py + 92


def inst_forma(b, x, y, w, h):
    """2 · las caras del verbo (un ejemplo y dos filas mías) y tres filtros."""
    c = RO
    cols = ("BASE", "+ S (HE, SHE, IT)", "PASADO", "PARTICIPIO", "+ ING")
    cw_ = w / len(cols)
    b.append(rect(x, y, w, 40, tinte(c, 0.88), r=10))
    for j, lab in enumerate(cols):
        rot(b, x + j * cw_ + cw_ / 2, y + 26, lab, c, size=13, anchor="middle")
    for i, fila in enumerate((("write", "writes", "wrote", "written", "writing"), None, None)):
        ry = y + 40 + i * 50
        if i % 2 == 0:
            b.append(rect(x, ry, w, 50, tinte(c, 0.96), r=8))
        for j in range(len(cols)):
            if fila:
                b.append(T(x + j * cw_ + cw_ / 2, ry + 33, [fila[j]], 19, INK, anchor="middle"))
            else:
                renglon(b, x + j * cw_ + 16, ry + 38, x + (j + 1) * cw_ - 16, LN)
    pista(b, x, y + 40 + 150 + 22, "la primera fila es un ejemplo; en las otras dos, verbos que me "
                                   "frenaron en los textos", size=15)
    yy = y + 40 + 150 + 38
    filtros = ("¿uno o varios?", "¿qué hay justo antes? was · has · to · will",
               "¿va antes de un sustantivo?")
    xx = x
    for f in filtros:
        fw = tw(f, 16, "700") + 30
        b.append(rect(xx, yy, fw, 40, "white", r=20, stroke=c, sw=2))
        b.append(T(xx + 15, yy + 26, [f], 16, c, weight="700"))
        xx += fw + 12
    return yy + 40


def inst_pegada(b, x, y, w, h):
    """3 · el imán: la palabra y su pegada (tres ejemplos que no están en los textos y uno mío)."""
    c = OR
    pares = (("listen", "to", "escuchar"), ("afraid", "of", "tener miedo de"),
             ("good", "at", "ser bueno para"), (None, None, None))
    cw_ = (w - 24) / 2
    for k, (p, q, es) in enumerate(pares):
        px = x + (k % 2) * (cw_ + 24)
        py = y + (k // 2) * 66
        b.append(rect(px, py, 140, 54, "white", r=10, stroke=c, sw=2.2))
        iman(b, px + 146, py + 7, c)
        b.append(rect(px + 196, py, 70, 54, tinte(c, 0.88), r=10, stroke=c, sw=2.2))
        if p:
            b.append(T(px + 70, py + 35, [p], 20, INK, weight="700", anchor="middle"))
            b.append(T(px + 231, py + 35, [q], 20, INK, weight="700", anchor="middle"))
            pista(b, px + 282, py + 34, "= " + es, size=16)
        else:
            b.append(T(px + 282, py + 34, ["="], 18, c, weight="700"))
            renglon(b, px + 304, py + 40, px + cw_ - 4, LN)
    pista(b, x, y + 144, "la última pareja la lleno con una que encuentre en los textos", size=15)
    yy = y + 158
    return trampa(b, x, yy, w, "La trampa del español",
                  "En español se dice «soñar con»; en inglés, «dream of». La palabra pegada no se "
                  "traduce: se aprende junto con su compañera.", c)


def inst_conector(b, x, y, w, h):
    """4 · dos ideas, el hueco en medio, cuatro relaciones dibujadas y la revisión de lo que sigue."""
    c = MO
    iw = 300
    for k, lab in enumerate(("una idea", "la otra idea")):
        bx = x if k == 0 else x + w - iw
        b.append(rect(bx, y, iw, 62, tinte(c, 0.93), r=14, stroke=c, sw=2.2))
        rot(b, bx + 20, y + 26, f"IDEA {k + 1}", c, size=13)
        pista(b, bx + 20, y + 50, lab, size=15)
    mx = x + w / 2
    b.append(line(x + iw, y + 31, mx - 34, y + 31, c, 2.4, dash="7,6"))
    b.append(line(mx + 34, y + 31, x + w - iw, y + 31, c, 2.4, dash="7,6"))
    b.append(f'<circle cx="{mx}" cy="{y + 31}" r="30" fill="white" stroke="{c}" stroke-width="2.6"/>')
    b.append(T(mx, y + 41, ["?"], 28, c, weight="700", anchor="middle"))
    yy = y + 84
    rels = (("suma", "se suman"), ("contraste", "se oponen"), ("causa", "una es la razón"),
            ("resultado", "una es el resultado"))
    rw = (w - 3 * 12) / 4
    for k, (tipo, nom) in enumerate(rels):
        rx = x + k * (rw + 12)
        b.append(rect(rx, yy, rw, 92, "white", r=12, stroke=tinte(c, 0.6), sw=2))
        _icono_relacion(b, rx + rw / 2, yy + 30, tipo, c)
        b.append(T(rx + rw / 2, yy + 74, [nom], 16, INK, anchor="middle"))
    pista(b, x, yy + 118, "encierro la relación que hay entre las dos ideas: ella escoge la familia del conector",
          size=15)
    yy += 140
    lab = "Después del hueco viene:"
    b.append(T(x, yy + 18, [lab], 18, INK, weight="700"))
    xx = x + tw(lab, 18, "700") + 20
    for o in ("una oración con verbo", "solo un sustantivo"):
        xx = marca(b, xx, yy + 2, c, o, size=17)
    return yy + 26


SUBS = {1: dict(cuando="falta un verbo y hay que decidir cuándo pasa.",
                pregunta="¿esto pasó, pasa siempre o viene desde antes hasta hoy?", inst=inst_reloj),
        2: dict(cuando="ya sé el tiempo, pero la palabra tiene varias caras.",
                pregunta="¿quién hace la acción y qué hay justo antes del hueco?", inst=inst_forma),
        3: dict(cuando="falta una palabra pequeña: in, on, for, with…",
                pregunta="¿a cuál palabra de al lado va pegada?", inst=inst_pegada),
        4: dict(cuando="el hueco une dos ideas.",
                pregunta="¿las dos ideas se suman, se oponen, o una explica a la otra?", inst=inst_conector)}

PASOS = (("PRIMERO", "Leo el texto entero sin llenar nada: ¿de qué trata y en qué tiempo va?"),
         ("LUEGO", "Tapo las opciones y me pregunto qué pieza falta: ¿verbo, palabra pequeña o conector?"),
         ("DESPUÉS", "Busco la pista en las palabras vecinas, antes y después del hueco, y la subrayo."),
         ("AL FINAL", "Llamo a la subestrategia, marco la letra y digo qué tan seguro estoy."))

QUE_PIDE = ("En la Parte 4 te dan un texto corto con espacios numerados y, para cada espacio, tres "
            "palabras: A, B o C. Aquí nadie te pregunta qué opinas ni de qué trata el texto: te preguntan "
            "si sabes cómo se arma el inglés por dentro. Cada espacio es una pieza: un verbo en su tiempo, "
            "la forma exacta que encaja, una palabra pequeña que va pegada a otra o un conector que une "
            "dos ideas. La buena noticia es que la pista casi siempre está a dos o tres palabras del "
            "espacio. La trampa es traducir palabra por palabra: en español suena bien y te lleva a la "
            "opción equivocada.")

MODELO = dict(
    frase="Every Saturday, my cousin (0) ________ football with his friends in the park.",
    opciones=("play", "plays", "played"),
    pensamientos=(("PRIMERO · LEO TODO", None, "Habla de algo que mi primo hace cada sábado: una costumbre."),
                  ("LUEGO · TAPO LAS OPCIONES", None, "Después del hueco viene «football»: falta lo que él "
                                                      "hace. Es un verbo."),
                  ("DESPUÉS · LOS VECINOS", 1, "«Every Saturday»: pasa siempre. El reloj dice presente."),
                  ("DESPUÉS · LOS VECINOS", 2, "«my cousin» es uno solo, él: en presente el verbo lleva -s."),
                  ("AL FINAL · MARCO", None, "«play» no tiene -s y «played» vive en el pasado. Queda la B, "
                                             "y estoy seguro.")),
    fila=dict(n=0, pista="Every Saturday · my cousin", subs=(1, 2), letra="B", seguro=2))


# ───────── hojas 2 a 4 · los cuatro textos, una fila por espacio ─────────
TEXTOS = {
    1: dict(n=1, titulo="Karol G en Medellín", pag=435, desde=1, hasta=10, pag_dicc=PAG_DICC),
    2: dict(n=2, titulo="Spider-Man: Across the Spider-Verse", pag=435, desde=11, hasta=20, pag_dicc=PAG_DICC,
            correcciones={
                12: "la opción A está mal escrita en el libro: dice «was release» y debe decir «was released». "
                    "Corrígela con lápiz antes de decidir, y escoge entre las tres con tu pista."},
            antes={
                18: "en los espacios 18, 19 y 20 el libro acepta un solo tiempo, pero en el resumen de una "
                    "película valen dos: el pasado (el texto arranca con «In 2023») y el presente con que se "
                    "cuentan las tramas. Escoge un tiempo, sostenlo en los tres y escribe tu pista."}),
    3: dict(n=3, titulo="AI in the Classroom", pag=436, desde=21, hasta=30, pag_dicc=PAG_DICC,
            correcciones={
                24: "aquí se defienden las tres opciones: by (quién o qué revisa), with (con qué se revisa) y "
                    "through (por medio de qué). Marca una y escribe en tu pista qué idea dice."}),
    4: dict(n=4, titulo="Public Protest and Social Change", pag=437, desde=31, hasta=40, pag_dicc=PAG_DICC,
            correcciones={
                32: "ninguna de las tres opciones forma la expresión «acting ___ the interests of» (actuar en "
                    "favor de). No marques letra: en la línea escribe la palabra pequeña que sí va.",
                34: "las tres opciones dicen causa y las tres son correctas aquí. Marca la que usarías y escribe "
                    "la pista que te dice que lo que sigue es la razón.",
                35: "dos de las tres opciones son correctas en inglés y el libro espera solo una. Marca la tuya "
                    "y escribe por qué la otra que sirve también vale.",
                39: "dos opciones se defienden, según leas la relación: la razón de lo anterior o un «pero» que "
                    "agrega una condición. Escribe cuál relación lees y defiéndela en clase."}),
}

RETO = dict(
    titulo="El duelo de las pistas", minutos=20, total=30, filas=10,
    consigna=("Siéntate con un compañero y comparen sus filas de los textos 1, 2 y 3, espacio por "
              "espacio. Donde marcaron lo mismo, sigan. Donde no coincidan, no se vota ni se adivina: cada "
              "uno lee en voz alta, en inglés, la pista que subrayó, y gana la pista que explica mejor el "
              "espacio. Anota aquí cada desacuerdo y qué pasó."),
    reglas=("«Me suena» no es pista. La pista son palabras del texto, leídas en inglés.",
            "El que pierde el duelo no borra: tacha, marca de nuevo y copia la pista que ganó.",
            "Si los dos tienen buena pista, llaman al profe: puede ser un error del libro."))


def _reto(b, y, h):
    reto_equipo(b, y, h, **RETO)


def _cierre(b, y, h):
    cierre_mision(b, y, h, PARTE, [(n, t['hasta'] - t['desde'] + 1) for n, t in TEXTOS.items()])


# ───────── hoja 5 · mi diccionario ─────────
DICC_INTRO = ("Aquí guardas el inglés que te frenó en los cuatro textos. Una palabra que no entiendes no se "
              "busca de una: primero se adivina por lo que dice alrededor y después se confirma en clase. Así "
              "se aprende el vocabulario que pide el examen: dentro de su oración.")

SECCIONES = (
    dicc_palabras(8),
    dicc_parejas("Palabras que vienen pegadas",
                 "Cuando el profe dé las claves de los textos 3 y 4, copia aquí cada palabra con la pequeña que "
                 "va pegada a ella (en la caja de color) y cómo se dice todo en español. Fíjate cuántas veces la "
                 "pegada no es la que dirías traduciendo.", 9, sub=3),
    dicc_familias("Conectores por la relación que dicen",
                  "Copia cada conector de los textos y de sus opciones en la familia de la relación que dice. Al "
                  "lado, marca qué viene después de él: una oración con verbo (O) o solo un sustantivo (S).",
                  (("suma", "Se suman", "una idea más"), ("contraste", "Se oponen", "una dice lo contrario"),
                   ("causa", "Una es la razón", "porque…"), ("resultado", "Una es el resultado", "entonces…")),
                  sub=4),
    dicc_verbos("Verbos que cambian de cara en pasado",
                "Los verbos irregulares no llevan -ed: cambian de cara. Escribe aquí los de los textos 1 y 2 "
                "que te frenaron, con sus tres caras y lo que significan.",
                ("BASE", "PASADO", "PARTICIPIO", "EN ESPAÑOL"), 4, sub=2),
)


def build(pages=(283, 284, 286, 287, 288)):
    return [
        hoja_estrategia("ing3_t1", pages[0], 1, PARTE, QUE_PIDE, muestra_parte4,
                        "Escucha a los vecinos del hueco", PASOS, SUBS, MODELO,
                        "en un texto con espacios, lo que más me cuesta es…"),
        hoja_trabajo("ing3_t2", pages[1], 2, [TEXTOS[1], TEXTOS[2]]),
        hoja_trabajo("ing3_t3", pages[2], 3, [TEXTOS[3]], extra=_reto),
        hoja_trabajo("ing3_t4", pages[3], 4, [TEXTOS[4]], extra=_cierre),
        hoja_diccionario("ing3_t5", pages[4], 5, PARTE, SECCIONES, DICC_INTRO),
    ]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
