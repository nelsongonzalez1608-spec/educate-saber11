#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 1 · entrenamiento ICFES · páginas 271 y 275.

Fuente de las cuatro: «Cuadernillo de preguntas · Prueba Inglés · Saber 11.º» (Icfes, septiembre
de 2024; fuente_icfes/16-octubre-cuadernillo-ingles-saber-11-2024.pdf): 50 preguntas «utilizadas
en aplicaciones anteriores de la prueba Saber 11.º», en dos exámenes de 25. Verificadas contra
las páginas 6, 14 y 15 del cuadernillo y su tabla de respuestas (páginas 23 y 24). Ninguna estaba
en tablero/icfes.csv; reservadas en tablero/propuestas/ing_icfes_reservas.csv.

En este cuadernillo la Parte 1 es el léxico (descripción → palabra, A–G con H de ejemplo) y la
Parte 2 los avisos («¿Dónde puede ver estos avisos?», A–C): las mismas dos tareas de la misión.

Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano; coinciden con la tabla del cuadernillo):

    QA · Examen 1 · 1 · B   (Clothes · «A person can carry things in one of these»)  estrategia 1
    QB · Examen 2 · 2 · D   (Transportation · «People pay to take this public transport
                             by road»)                                              estrategia 2
    QC · Examen 2 · 6 · C   (aviso «Please, take the one you want to read»)          estrategia 3
    QD · Examen 2 · 5 · B   (aviso «New Toys: Green monsters, angry dolls…»)         estrategia 4

  E1 · 1 · B handbags: el verbo es «carry» (cargar, llevar cosas). Gafas, sombrero, pijama,
       bufanda, falda y medias se llevan PUESTAS (wear); en un bolso se cargan cosas.
  E2 · 2 · D bus: «pay to take» (se paga el pasaje) saca bike y motorbike (son tuyas) y la
       ambulancia; «public transport» se queda con bus, plane, train, boat; «by road» deja solo
       el bus (el tren va por rieles, el avión por aire, el barco por agua).
  E3 · 6 · C on a bookshelf: «take the one you want to READ» → lo que se toma son libros → el
       letrero está donde se guardan los libros. Un banquito (stool) no guarda libros; en un
       computador no se «toma» un libro con la mano.
  E4 · 5 · B in a shop: «New toys» + una lista de productos con sus colores = un anuncio que quiere
       vender. En una casa los juguetes no se anuncian «nuevos»; en un zoológico no hay muñecas.

Adaptaciones: el título del tema «Clothes and accesories» del original se corrige a «Clothes and
accessories» (errata del cuadernillo, registrada). Las opciones de la Parte 1 se imprimen A–G y la
palabra H va en el ejemplo, como en el original. Los avisos se redibujan como un letrero con el
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
        texto(b, x + w / 2, y + 26, tema, size=21, weight="700", anchor="middle")
        yy = y + 44
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


# ───────── QA · Examen 1 · 1 · handbags ─────────
def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Wear o carry: dos cajones", c,
                      "Como con «repairs» en la pregunta 1: el verbo de la descripción decide. Reparte las siete "
                      "palabras en dos cajones y busca la que va con el verbo que dice la descripción.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (tit, ps) in enumerate((("WEAR · LO LLEVO PUESTO", "en el cuerpo"),
                                   ("CARRY · LO CARGO, LLEVO COSAS EN ÉL", "en la mano o al hombro"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 150, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        pista(b, bx + 18, yy + 54, ps)
        renglon(b, bx + 18, yy + 96, bx + half - 18)
        renglon(b, bx + 18, yy + 134, bx + half - 18)
    yy += 166
    pista(b, x0, yy + 20, "el verbo de la descripción 1:")
    renglon(b, x0 + 210, yy + 22, x0 + 500)
    pista(b, x0 + 530, yy + 20, "entonces miro el cajón:")
    renglon(b, x0 + 700, yy + 22, x0 + ww)
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

QA = dict(est=1, comp="Léxico · Parte 1", e=INSTR_P1,
          o=["glasses", "handbags", "hat", "pajamas", "scarf", "skirt", "socks"],
          datos=vocab("Clothes and accessories", "0.  You wear this to know the time.", "H · watch",
                      "1.  A person can carry things in one of these."), inst=ii1)
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
