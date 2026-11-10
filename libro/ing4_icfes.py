#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 4 · entrenamiento ICFES · páginas 315 y 320.

Las cuatro salen del cuadernillo oficial «Prueba Inglés · Cuadernillo de preguntas · Saber 11.º»
(Icfes, septiembre de 2024; fuente_icfes/16-octubre-cuadernillo-ingles-saber-11-2024.pdf), Parte 5
(comprensión literal de un artículo, tres opciones). Verificadas contra la página del cuadernillo
y resueltas a mano; la tabla de respuestas del final coincide. Ninguna estaba en
tablero/icfes.csv; reservadas en tablero/propuestas/ing_icfes_reservas.csv.
Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11», sin año ni «oficial».

Cada tarjeta imprime los párrafos que necesita (el artículo completo está en
tablero/propuestas/ing4_textos.md, para que el profe lo proyecte).

Claves verificadas:

    QA · Examen 1 · 18 (Parte 5, «James Salter's Days in Film», pp. 10–11) · C a movie         estr. 1
    QB · Examen 2 · 18 (Parte 5, «My Artistic Adventure», pp. 18–19)       · B was too young   estr. 3
    QC · Examen 1 · 17 (Parte 5, «James Salter's Days in Film», pp. 10–11) · A from 1960 to 1979 estr. 2
    QD · Examen 1 · 20 (Parte 5, «James Salter's Days in Film», pp. 10–11) · C Nick Paumgarten  estr. 4

  18 (ex. 1) · «was adapted into a film called Passionate Falsehoods»: film = movie. No es un
       periódico (The New Yorker es donde salió el cuento) ni una obra de teatro.
  18 (ex. 2) · «I could not buy oil paints; I was only seven»: tenía siete años, era muy pequeña.
       El programa era español, pero eso no le impidió nada; ver televisión tampoco es la razón.
  17 (ex. 1) · «during the sixties and seventies, he worked in film making» = de 1960 a 1979.
       1957 es cuando dejó el ejército; 1997, cuando se publicó el cuento.
  20 (ex. 1) · «Nick Paumgarten in The Last Book, describes Salter's opinion»: el libro es de
       Paumgarten. Salter es de quien se habla; Treisman solo «ha hablado» de Salter.
"""
from ing4 import *   # noqa: F401,F403  (configura la misión y EST)
from ing4 import rot, caja, pista, renglon, texto, tinte, flecha, marca, frase_hueco, encabezado

F = "Pregunta Saber 11"
INSTR = "Lea el artículo y luego responda la pregunta."

SALTER_1 = ("James Salter was a pilot in the United States Air Force. He abandoned the military profession in 1957 "
            "after the publication of his first novel, The Hunters. He is best known as a novelist, but during the "
            "sixties and seventies, he worked in film making. Salter made documentaries, wrote scripts for films, "
            "and even was the director of a film called Three, starring Charlotte Rampling and Sam Waterston.")
SALTER_2 = ("Burning the Days, a short story published in The New Yorker in 1997, where Salter tells the story of his "
            "life, was adapted into a film called Passionate Falsehoods.")
SALTER_3 = ("Salter's time in the film world is both good and bad. In Rome, he met directors and stars. In New York, "
            "he explored the city with Robert Redford and enjoyed being famous. Deborah Treisman, and Michael Agger "
            "have talked about Salter. Nick Paumgarten in The Last Book, describes Salter's opinion about his film "
            "career:")
SALTER_4 = ("\"Of sixteen scripts for movies, only four were popular. There was money, attractive women, and entrance "
            "into rooms where there were stories more for the dinner table than for the page\". Salter thought he "
            "was wasting his time.")
ARTE_1 = ("When I was a child in Ireland, I went to bed late, and I could not sleep past six. One morning, I found a "
          "Spanish television show with a French man who was painting a beautiful countryside with oil paints.")
ARTE_3 = ("Every Sunday morning, I would try to paint what he was painting on the screen, but I needed oil paints to "
          "make my paintings as beautiful as his. I could not buy oil paints; I was only seven, and my parents would "
          "not buy them for me. Then I decided to use my mother's cosmetics and paper for my painting. I was ready to "
          "paint my first picture.")


def articulo(titulo, parrafos, tronco, nota="fragmento del artículo; el profe tiene el texto completo"):
    """Los párrafos del cuadernillo en un recuadro y, debajo, el comienzo de la pregunta."""
    def _d(b, x, y, w):
        yy = y + 6
        g = [T(x + w / 2, yy + 34, [titulo], 19, INK, weight="700", anchor="middle")]
        yi = yy + 46
        for p in parrafos:
            if p == "…":
                g.append(T(x + 24, yi + 18, ["[…]"], 18, GRAY))
                yi += 30
                continue
            svg, yi = TJ(x + 24, yi, p, w - 48, 18, INK, lh=25)
            g.append(svg)
            yi += 8
        g.append(T(x + w - 24, yi + 12, [f"({nota})"], 14, GRAY, style="italic", anchor="end"))
        h = yi + 24 - yy
        b.append(rect(x, yy, w, h, "#F7F8FA", r=12, stroke="#C9CED6", sw=1.6))
        b.extend(g)
        yy += h + 8
        svg, y2 = TJ(x, yy + 2, tronco, w, 20, INK, weight="700", lh=28)
        b.append(svg)
        return y2
    return _d


# ───────── QA · Examen 1 · 18 · Passionate Falsehoods ─────────
def ii1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Los títulos del texto y lo que es cada uno", c,
                      "El ancla es el título de la pregunta. Pero el texto trae varios títulos: novela, película, "
                      "cuento, revista… Escribe al lado de cada uno qué es y la palabra del texto que lo dice.")
    x0, ww = x + 22, w - 44
    cols = (330, 260, ww - 590)
    y0 = yy
    yy = encabezado(b, x0, yy, cols, ("TÍTULO DEL TEXTO", "¿QUÉ ES?", "LA PALABRA DEL TEXTO QUE LO DICE"), c, hh=40)
    rh = 48
    for k, t_ in enumerate(("The Hunters", "Three", "Burning the Days", "The New Yorker", "Passionate Falsehoods")):
        ry = yy + k * rh
        caja(b, x0, ry, sum(cols), rh, c, r=0)
        texto(b, x0 + 14, ry + 31, t_, size=17, weight="700", style="italic")
        for j in (1, 2):
            cx0 = x0 + sum(cols[:j])
            renglon(b, cx0 + 14, ry + rh - 12, cx0 + cols[j] - 14)
    ry = yy + 5 * rh
    for k in (1, 2):
        b.append(line(x0 + sum(cols[:k]), y0, x0 + sum(cols[:k]), ry, c, 1.6))
    return ry


# ───────── QB · Examen 2 · 18 · was too young ─────────
def ii2(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La razón dicha con otras palabras", c,
                      "La respuesta no copia el texto: lo dice de otra manera. Copia la frase que explica por qué no "
                      "tuvo pinturas y dila con tus palabras. Después busca la opción que diga lo mismo.")
    x0, ww = x + 22, w - 44
    hw = (ww - 70) / 2
    for k, (rt, ps) in enumerate((("EL TEXTO LO DICE ASÍ", "copio la frase (en inglés):"),
                                  ("YO LO DIGO ASÍ", "con mis palabras (en español):"))):
        bx = x0 + k * (hw + 70)
        caja(b, bx, yy, hw, 130, c, sw=2.4, r=14)
        rot(b, bx + 20, yy + 30, rt, c, size=14)
        pista(b, bx + 20, yy + 56, ps)
        renglon(b, bx + 20, yy + 90, bx + hw - 20)
        renglon(b, bx + 20, yy + 118, bx + hw - 20)
    flecha(b, x0 + hw + 10, yy + 65, x0 + hw + 60, yy + 65, c, head=11)
    return yy + 130


# ───────── QC · Examen 1 · 17 · from 1960 to 1979 ─────────
def ii3(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Tres fechas, tres dueños: la vida de Salter", c,
                      "Pon en la línea cada fecha del texto con lo que pasó. Una de ellas no está escrita con números: "
                      "tradúcela a años. La pregunta pide una sola.")
    x0, ww = x + 22, w - 44
    ly = yy + 30
    b.append(line(x0 + 10, ly, x0 + ww - 10, ly, c, 4))
    for k, a in enumerate(range(1950, 2001, 10)):
        px = x0 + 30 + k * (ww - 60) / 5
        b.append(line(px, ly - 12, px, ly + 12, c, 3))
        texto(b, px, ly + 34, str(a), size=15, color=c, weight="700", anchor="middle")
    yy = ly + 56
    fw = (ww - 2 * 18) / 3
    for k, f_ in enumerate(("1957", "the sixties and seventies", "1997")):
        bx = x0 + k * (fw + 18)
        caja(b, bx, yy, fw, 112, c, r=12)
        texto(b, bx + 16, yy + 30, f_, size=17, weight="700")
        pista(b, bx + 16, yy + 58, "en años:" if k == 1 else "lo que pasó:", size=14)
        renglon(b, bx + 100, yy + 60, bx + fw - 16)
        pista(b, bx + 16, yy + 94, "lo que pasó:" if k == 1 else "¿lo pregunta?", size=14)
        renglon(b, bx + 110, yy + 96, bx + fw - 16)
    return yy + 112


# ───────── QD · Examen 1 · 20 · Nick Paumgarten ─────────
def ii4(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Cuatro nombres y un libro: quién hizo qué", c,
                      "Los tres nombres de las opciones están en el texto: los tres son verdad. Escribe qué hace "
                      "cada persona en el texto: solo una hizo lo que se pregunta.")
    x0, ww = x + 22, w - 44
    nw = (ww - 3 * 14) / 4
    for k, n_ in enumerate(("James Salter", "Deborah Treisman", "Michael Agger", "Nick Paumgarten")):
        bx = x0 + k * (nw + 14)
        caja(b, bx, yy, nw, 104, c, r=12)
        texto(b, bx + 14, yy + 30, n_, size=17, weight="700")
        pista(b, bx + 14, yy + 56, "en el texto:", size=14)
        renglon(b, bx + 14, yy + 92, bx + nw - 14)
    return yy + 104


QA = dict(est=1, f=F, e=INSTR, inst=ii1,
          datos=articulo("JAMES SALTER'S DAYS IN FILM", [SALTER_1, SALTER_2, "…"], "18. Passionate Falsehoods is"),
          o=["a newspaper.", "a play.", "a movie."])
QB = dict(est=3, f=F, e=INSTR, inst=ii2,
          datos=articulo("MY ARTISTIC ADVENTURE", [ARTE_1, "…", ARTE_3, "…"],
                         "18. She could not get oil paints because she"),
          o=["didn't speak Spanish.", "was too young.", "always watched TV."])
QC = dict(est=2, f=F, e=INSTR, inst=ii3,
          datos=articulo("JAMES SALTER'S DAYS IN FILM", [SALTER_1, SALTER_2, "…"],
                         "17. James Salter played an important part in the making of movies"),
          o=["from 1960 to 1979.", "in 1957.", "after 1997."])
QD = dict(est=4, f=F, e=INSTR, inst=ii4,
          datos=articulo("JAMES SALTER'S DAYS IN FILM", ["…", SALTER_3, SALTER_4, "…"], "20. The Last Book was written by"),
          o=["James Salter.", "Deborah Treisman.", "Nick Paumgarten."])


def build(pages=(315, 320)):
    return [hoja_icfes("ing4_i1", pages[0], QA, QB),
            hoja_icfes("ing4_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
