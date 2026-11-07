#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 1 · entrenamiento ICFES · páginas 271 y 275.

Fuente de QB, QC y QD (QA: ver abajo, cambió el 7 nov): «Cuadernillo de preguntas · Prueba Inglés · Saber 11.º» (Icfes, septiembre
de 2024; fuente_icfes/16-octubre-cuadernillo-ingles-saber-11-2024.pdf): 50 preguntas «utilizadas
en aplicaciones anteriores de la prueba Saber 11.º», en dos exámenes de 25. Verificadas contra
las páginas 6, 14 y 15 del cuadernillo y su tabla de respuestas (páginas 23 y 24). Ninguna estaba
en tablero/icfes.csv; reservadas en tablero/propuestas/ing_icfes_reservas.csv.

En este cuadernillo la Parte 1 es el léxico (descripción → palabra, A–G con H de ejemplo) y la
Parte 2 los avisos («¿Dónde puede ver estos avisos?», A–C): las mismas dos tareas de la misión.

Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano; coinciden con la tabla del cuadernillo):

    QA · 2016-1 2.ª sesión · 87 · F  (time words · «You wear it to know what time it is»)  estrategia 1
    QB · Examen 2 · 2 · D   (Transportation · «People pay to take this public transport
                             by road»)                                              estrategia 2
    QC · Examen 2 · 6 · C   (aviso «Please, take the one you want to read»)          estrategia 3
    QD · Examen 2 · 5 · B   (aviso «New Toys: Green monsters, angry dolls…»)         estrategia 4

  E1 · 87 · F watch: el banco mezcla momentos del día (afternoon, evening, morning, yesterday,
       week, birthday) con dos cosas que dan la hora (clock, watch). Las dos dan la hora; el verbo
       «wear» (llevar puesto) deja solo el reloj de pulsera: el de pared (clock) no se lleva puesto.
       Las cinco del grupo (87-91): 87·F 88·E 89·D 90·H 91·G; A (afternoon) es el ejemplo y sobran
       B y C, como dice la instrucción («sobran tres de las ocho, una de las cuales se usa para el
       ejemplo»): el grupo es coherente. Resuelta a mano; el cuadernillo escaneado no trae tabla.

QA cambió el 7 nov (decisión de Nelson: «si una pregunta del ICFES tiene alguna falla, no la
uses»). Salió Examen 1 · 1 del cuadernillo 2024 (handbags): el cuadernillo titula el tema «Clothes
and accesories». Entró la N.º 87 del cuadernillo oficial Saber 11 2016-1, segunda sesión (ABD,
encabezado «Saber 11 - 051 - F2 - ABD»; en Drive, «2016-2 SEGUNDA SESION.pdf»), Inglés, Parte 2:
descripción → palabra, A–H, leída palabra por palabra en el escaneo, sin errata. El SIMULACRO II
2023 la repite como N.º 66 con errata («Dock» por «Clock»): se usa la del cuadernillo oficial.
Se descartaron, por errata: el grupo 86–90 del SIMULACRO (ejemplo sin punto final) y su grupo
81–85 (n.º 84 «have it lot»); y el cuadernillo 2024 Examen 2 · 1 y 3 (la instrucción dice
«Sobran dos palabras más» y con 3 preguntas y 7 palabras sobran cuatro; además repetiría el banco
de QB en la misma hoja).
  E2 · 2 · D bus: «pay to take» (se paga el pasaje) saca bike y motorbike (son tuyas) y la
       ambulancia; «public transport» se queda con bus, plane, train, boat; «by road» deja solo
       el bus (el tren va por rieles, el avión por aire, el barco por agua).
  E3 · 6 · C on a bookshelf: «take the one you want to READ» → lo que se toma son libros → el
       letrero está donde se guardan los libros. Un banquito (stool) no guarda libros; en un
       computador no se «toma» un libro con la mano.
  E4 · 5 · B in a shop: «New toys» + una lista de productos con sus colores = un anuncio que quiere
       vender. En una casa los juguetes no se anuncian «nuevos»; en un zoológico no hay muñecas.

Adaptaciones: en QB (Parte 1 del 2024) las opciones se imprimen A–G y la palabra H va en el
ejemplo, como en el original. En QA (2016-1) se imprimen las ocho, A–H, como en el original; la A
(afternoon) es la del ejemplo. La instrucción se reduce a una sola descripción. Los avisos se redibujan como un letrero con el
mismo texto.
"""
from ing1 import *   # noqa: F401,F403  (configura la misión y EST)
from ing1 import rot, caja, pista, renglon, texto, tinte, flecha

FUENTE = "Cuadernillo de preguntas · Prueba Inglés · Saber 11.º (Icfes, 2024)"


def pregunta(b, x, y, w, txt, size=20, weight="400"):
    svg, y2 = TJ(x, y + 22, txt, w, size, INK, weight=weight, lh=size + 8)
    b.append(svg)
    return y2


def vocab(tema, ejemplo, ej_resp, item):
    def datos(b, x, y, w):
        if tema:
            texto(b, x + w / 2, y + 26, tema, size=21, weight="700", anchor="middle")
            yy = y + 44
        else:
            yy = y + 6
        caja(b, x, yy, w, 52, "#D6DBE3", fill="#F5F6F8", r=10)
        texto(b, x + 18, yy + 33, "Ejemplo:", size=17, color=GRAY, weight="700")
        texto(b, x + 110, yy + 33, ejemplo, size=18)
        texto(b, x + w - 18, yy + 33, f"Respuesta: {ej_resp}", size=17, color=GRAY, anchor="end")
        yy += 66
        texto(b, x, yy + 22, item, size=21, weight="700")
        return yy + 30
    return datos


def aviso(lineas, titulo=None):
    def datos(b, x, y, w):
        aw = 560
        ax = x + (w - aw) / 2
        h = 34 + len(lineas) * 32
        b.append(rect(ax - 8, y + 6, aw + 16, h + 16, "white", r=6, stroke="#9AA1AD", sw=1.8))
        b.append(rect(ax, y + 14, aw, h, "#F3F4F6", r=4, stroke="#9AA1AD", sw=1.4))
        for k, ln in enumerate(lineas):
            texto(b, ax + aw / 2, y + 14 + 38 + k * 32, ln, size=22, weight="700", anchor="middle")
        yy = y + h + 30
        if titulo:
            yy = pregunta(b, x, yy, w, titulo)
        return yy
    return datos


# ───────── QA · 2016-1 2.ª sesión · 87 · watch ─────────
def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Primero la clase, después el verbo", c,
                      "Como con «repairs» en la pregunta 1: antes de leer la descripción, separa qué clase de "
                      "palabras trae la lista. Después, el verbo de la descripción escoge dentro de la clase.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (tit, ps) in enumerate((("MOMENTOS DEL TIEMPO", "partes del día, días, semanas…"),
                                   ("COSAS QUE SE PUEDEN TOCAR", "objetos"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 128, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        pista(b, bx + 18, yy + 54, ps)
        renglon(b, bx + 18, yy + 90, bx + half - 18)
        renglon(b, bx + 18, yy + 116, bx + half - 18)
    yy += 144
    pista(b, x0, yy + 20, "de las cosas, las que sirven para saber la hora:")
    renglon(b, x0 + 340, yy + 22, x0 + ww)
    yy += 40
    pista(b, x0, yy + 20, "el verbo de la descripción:")
    renglon(b, x0 + 200, yy + 22, x0 + 420)
    pista(b, x0 + 440, yy + 20, "¿a cuál de ellas se le puede hacer eso?")
    renglon(b, x0 + 730, yy + 22, x0 + ww)
    return yy + 30


# ───────── QB · Examen 2 · 2 · bus ─────────
def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Tres pistas, tres tachones", c,
                      "Como con «without» y «but» en las preguntas 5 y 7: cada pista de la descripción saca "
                      "palabras. Escribe debajo de cada pista las que tacha.")
    x0, ww = x + 22, w - 44
    pw = (ww - 2 * 40) / 3
    for k, frag in enumerate(("pay to take", "public transport", "by road")):
        bx = x0 + k * (pw + 40)
        caja(b, bx, yy, pw, 140, c, r=14)
        texto(b, bx + 18, yy + 36, frag, size=20, weight="700")
        pista(b, bx + 18, yy + 66, "tacha:")
        renglon(b, bx + 18, yy + 98, bx + pw - 18)
        renglon(b, bx + 18, yy + 128, bx + pw - 18)
        if k < 2:
            flecha(b, bx + pw + 4, yy + 70, bx + pw + 36, yy + 70, c, head=9)
    yy += 156
    pista(b, x0, yy + 20, "lo que queda en pie después de las tres pistas:")
    renglon(b, x0 + 330, yy + 22, x0 + ww)
    return yy + 30


# ───────── QC · Examen 2 · 6 · bookshelf ─────────
def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Lo que se toma y dónde se guarda", c,
                      "Como con el cinturón y la turbulencia: la cosa que nombra el aviso dice dónde está pegado. "
                      "Sigue la cadena de izquierda a derecha.")
    x0, ww = x + 22, w - 44
    pasos = (("«take the one you want to read»", "¿qué cosas se leen?"),
             ("esas cosas se guardan…", "¿dónde, en una casa o en un colegio?"),
             ("el letrero va pegado…", "¿cuál opción es ese sitio?"))
    pw = (ww - 2 * 40) / 3
    for k, (tit, ps) in enumerate(pasos):
        bx = x0 + k * (pw + 40)
        caja(b, bx, yy, pw, 130, c, r=14)
        texto(b, bx + 18, yy + 34, tit, size=17, weight="700")
        pista(b, bx + 18, yy + 62, ps)
        renglon(b, bx + 18, yy + 108, bx + pw - 18)
        if k < 2:
            flecha(b, bx + pw + 4, yy + 65, bx + pw + 36, yy + 65, c, head=9)
    return yy + 130


# ───────── QD · Examen 2 · 5 · shop ─────────
def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "¿Me informa, me prohíbe o me vende?", c,
                      "Como con el paquete y la cita médica: antes del lugar, mira qué quiere el aviso de quien lo "
                      "lee. Marca una sola intención y escribe la palabra que te lo mostró.")
    x0, ww = x + 22, w - 44
    ints = ("me informa algo", "me prohíbe algo", "me quiere vender algo", "me pide un favor")
    pw = (ww - 3 * 16) / 4
    for k, t in enumerate(ints):
        bx = x0 + k * (pw + 16)
        caja(b, bx, yy, pw, 60, c, r=12)
        b.append(checkbox(bx + 16, yy + 19, s=11, c=c))
        texto(b, bx + 50, yy + 37, t, size=17)
    yy += 76
    pista(b, x0, yy + 20, "la palabra del aviso que me lo mostró:")
    renglon(b, x0 + 280, yy + 22, x0 + ww / 2)
    pista(b, x0 + ww / 2 + 20, yy + 20, "¿dónde se anuncia eso?")
    renglon(b, x0 + ww / 2 + 200, yy + 22, x0 + ww)
    return yy + 30


INSTR_P1 = ("Lea la descripción de la izquierda. ¿Cuál palabra de la columna de la derecha (A - G) concuerda "
            "con la descripción? La opción H se usa para el ejemplo.")

INSTR_2016 = ("Lea la descripción de la izquierda. ¿Cuál palabra de la columna de la derecha (A - H) concuerda "
              "con la descripción? La opción A se usa para el ejemplo.")

QA = dict(est=1, comp="Léxico · descripción → palabra", e=INSTR_2016,
          o=["afternoon", "birthday", "clock", "evening", "morning", "watch", "week", "yesterday"],
          datos=vocab(None, "0.  This part of the day goes from twelve to six p.m.", "A · afternoon",
                      "87.  You wear it to know what time it is."), inst=ii1)
QB = dict(est=2, comp="Léxico · Parte 1", e=INSTR_P1,
          o=["ambulance", "boat", "bike", "bus", "motorbike", "plane", "train"],
          datos=vocab("Transportation", "0.  People drive it on a road and it carries big things.", "H · truck",
                      "2.  People pay to take this public transport by road."), inst=ii2)
QC = dict(est=3, comp="Pragmático · Parte 2", e="¿Dónde puede ver este aviso?",
          o=["on a stool", "on a computer", "on a bookshelf"],
          datos=aviso(["Please, take the one you", "want to read"]), inst=ii3)
QD = dict(est=4, comp="Pragmático · Parte 2", e="¿Dónde puede ver este aviso?",
          o=["in a house", "in a shop", "in a zoo"],
          datos=aviso(["New Toys: Green", "monsters, angry dolls,", "and black helicopters"]), inst=ii4)


def build(pages=(271, 275)):
    return [hoja_icfes("ing1_i1", pages[0], QA, QB),
            hoja_icfes("ing1_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
