#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 5 · entrenamiento ICFES · páginas 170 y 174.

Las cuatro preguntas salen del cuadernillo oficial Saber 11 2016-1, SEGUNDA sesión (cuadernillo
ABD; encabezado de la sección «Saber 11 - 083 - B10O - ABD · 2a. sesión»), sección Ciencias
Naturales, ítems 51 a 81. Verificadas contra la portada («ABD · 2016-1 · Examen de Estado ·
Segunda sesión») y las páginas escaneadas en Drive («1. CUADERNILLOS ICFES» / «2016-2 SEGUNDA
SESION.pdf»: el archivo se llama 2016-2 pero la portada dice 2016-1, segunda sesión).
Ninguna estaba en tablero/icfes.csv; reservadas en tablero/propuestas/bio_icfes_reservas.csv.

Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11», sin año ni «oficial».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · N.º 66 · C   (alternancia haploide-diploide · qué mecanismo genera diversidad)   estrategia 1
    QB · N.º 63 · A   (anticonceptivo en monos ardilla · el experimento no tiene control)  estrategia 3
    QC · N.º 55 · D   (dengue · aumentar la frecuencia del insecticida)                   estrategia 2
    QD · N.º 56 · B   (dengue · qué cartelera soporta el descubrimiento)                  estrategia 4

  66 · C: la fertilización junta gametos de dos individuos distintos. A (la mitosis da copias),
       B (la fase haploide no duplica cromosomas) y D (la célula haploide no sale de la unión de
       dos diploides) describen mal el modelo.
  63 · A: los dos grupos reciben el anticonceptivo; sin un grupo sin él no hay con qué comparar.
  55 · D: el texto dice que hay especies resistentes «sin importar su concentración».
  56 · B: es la única cartelera que muestra mosquitos frente a insecticidas (resistencia).

Adaptaciones de formato (registradas en bio5_icfes.csv): la figura de la N.º 66 se redibujó
con los mismos rótulos; las cuatro carteleras de la N.º 56 se transcriben como texto con sus
mismos datos, y su contexto del dengue se imprime una sola vez, en la N.º 55.
"""
from bio5 import *   # noqa: F401,F403  (configura la misión y EST)
from bio5 import rot, caja, pista, renglon, texto, sino, frase_hueco, tinte, flecha


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · N.º 66 · alternancia de generaciones ─────────
def nodo(b, cx, cy, lineas, c, rx=150, ry=40):
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="white" stroke="{c}" stroke-width="2"/>')
    for k, ln in enumerate(lineas):
        texto(b, cx, cy + 6 + (k - (len(lineas) - 1) / 2) * 20, ln, size=16, anchor="middle")


def etiqueta(b, x, y, txt, c):
    w = tw(txt, 16, "700") + 24
    b.append(rect(x - w / 2, y - 18, w, 34, tinte(c, 0.9), r=6, stroke=c, sw=1.6))
    texto(b, x, y + 5, txt, size=16, color=INK, weight="700", anchor="middle")


def datos_66(b, x, y, w):
    c = GRAY
    y0 = y + 10
    L, R = x + 200, x + w - 200
    top, bot = y0 + 50, y0 + 250
    nodo(b, L, top, ["Células haploides (n)"], c, rx=130)
    nodo(b, R, top, ["Gametos: esperma (n)", "y óvulo (n)"], c, rx=130, ry=44)
    nodo(b, R, bot, ["Cigoto diploide (2n)"], c, rx=130)
    nodo(b, (L + R) / 2 + 40, bot, ["Organismo multicelular", "diploide (2n)"], c, rx=150, ry=44)
    nodo(b, L, bot, ["Células (2n)", "línea germinal"], c, rx=120, ry=44)
    flecha(b, L + 134, top, R - 136, top, INK, sw=2.2, head=11)
    texto(b, (L + R) / 2, top - 12, "Haploide (n)", size=16, color=INK, anchor="middle")
    flecha(b, R, top + 46, R, bot - 42, INK, sw=2.2, head=11)
    etiqueta(b, R, (top + bot) / 2, "Fertilización", INK)
    flecha(b, R - 132, bot, (L + R) / 2 + 194, bot, INK, sw=2.2, head=11)
    texto(b, (R - 132 + (L + R) / 2 + 194) / 2, bot - 12, "Mitosis", size=16, color=INK, weight="700",
          anchor="middle")
    flecha(b, (L + R) / 2 - 114, bot, L + 124, bot, INK, sw=2.2, head=11)
    for k, t_ in enumerate(("Formación de", "células germinales")):
        texto(b, ((L + R) / 2 - 114 + L + 124) / 2, bot - 32 + k * 19, t_, size=15, color=INK, anchor="middle")
    flecha(b, L, bot - 46, L, top + 42, INK, sw=2.2, head=11)
    etiqueta(b, L, (top + bot) / 2, "Meiosis", INK)
    texto(b, (L + R) / 2, (top + bot) / 2 + 6, "Diploide (2n)", size=16, color=INK, anchor="middle")
    return pregunta(b, x, bot + 54, w, "El modelo incluye algunos de los mecanismos que generan diversidad dentro de "
                                       "una población. ¿Cuál mecanismo mostrado en el modelo genera diversidad?")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Pon el dedo en el ciclo: qué pasa en cada paso", c,
                      "Lo mismo que con el pedigrí: sigue el camino de los cromosomas. Escribe el nombre del paso que "
                      "responde cada pregunta.")
    x0, ww = x + 22, w - 44
    bw = (ww - 2 * 20) / 3
    for k, p in enumerate(("¿Dónde baja de 2n a n?", "¿Dónde se junta lo de dos individuos?",
                           "¿Dónde las células hijas salen iguales?")):
        bx = x0 + k * (bw + 20)
        caja(b, bx, yy, bw, 92, c, r=14)
        texto(b, bx + 18, yy + 32, p, size=16, weight="700", color=c)
        renglon(b, bx + 18, yy + 74, bx + bw - 18)
    return yy + 92


# ───────── QB · N.º 63 · monos ardilla ─────────
MONOS = ("En un zoológico necesitan regular la natalidad de las hembras de monos ardilla. Se ha diseñado el "
         "siguiente experimento para probar la efectividad de un nuevo método anticonceptivo: 1. Formación de dos "
         "grupos de hembras en edad reproductiva. 2. Suministro del anticonceptivo a todas las hembras de los dos "
         "grupos. 3. Reunión con machos de la especie. 4. Se repite cada mes el procedimiento y se contabiliza el "
         "número de embarazos por cada grupo.")


def datos_63(b, x, y, w):
    return pregunta(b, x, y, w, "Con base en la información anterior, ¿el experimento planteado permitirá reconocer "
                                "la efectividad del anticonceptivo en la población de monos ardilla?")


def ii2(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Dos grupos, ¿qué los hace distintos?", c,
                      "Como en la investigación de los Pomsky: sin comparación no hay prueba. Llena lo que recibe cada "
                      "grupo y escribe en qué se diferencian.")
    x0, ww = x + 22, w - 44
    gw = 360
    for k in range(2):
        bx = x0 + k * (gw + 20)
        caja(b, bx, yy, gw, 112, c, r=14)
        rot(b, bx + 18, yy + 28, f"GRUPO {k + 1}", c, size=14)
        pista(b, bx + 18, yy + 62, "¿recibe anticonceptivo?")
        sino(b, bx + 200, yy + 46, c, gap=70)
        pista(b, bx + 18, yy + 98, "¿se reúne con machos?")
        sino(b, bx + 200, yy + 82, c, gap=70)
    bx = x0 + 2 * (gw + 20)
    caja(b, bx, yy, ww - (bx - x0), 112, c, r=14, dash="8,6")
    rot(b, bx + 18, yy + 28, "LO ÚNICO DISTINTO ENTRE LOS DOS", c, size=14)
    renglon(b, bx + 18, yy + 66, x0 + ww - 18)
    renglon(b, bx + 18, yy + 100, x0 + ww - 18)
    return yy + 112


# ───────── QC · N.º 55 · dengue · frecuencia del insecticida ─────────
DENGUE = ("El dengue es una enfermedad tropical producida por la infección con el virus Flavivirus, que se transmite a "
          "través de las picaduras de algunos mosquitos hembra del género Aedes. Este tipo de mosquito se reproduce "
          "principalmente en aguas estancadas. Algunas de las medidas que recomiendan las entidades estatales para "
          "disminuir el caso de personas infectadas son: • Tapar los recipientes con agua al aire libre; eliminar "
          "llantas, botellas, barriles u otros recipientes que puedan retener agua. • Usar insecticidas para "
          "mosquitos. Investigaciones recientes han demostrado que algunas especies de adultos de mosquito del género "
          "Aedes son más resistentes que otras a algunos insecticidas, sin importar su concentración, de manera que "
          "el uso de estos no garantiza un 100% de protección frente al dengue.")


def datos_55(b, x, y, w):
    return pregunta(b, x, y, w, "Al observar la manera como se transmite el dengue, un estudiante afirma que para "
                                "garantizarse una protección del 100% frente al dengue con el uso de insecticidas, debe "
                                "aumentarse la frecuencia con la que estos se aplican. De acuerdo con la información "
                                "del contexto, ¿la hipótesis del estudiante debería mantenerse o cambiarse?")


def ii3(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Más dosis contra un mosquito que no responde", c,
                      "Como con los plásmidos: lo que decide está en el mosquito, no en el tanque. Escribe qué le pasa a "
                      "cada mosquito con cada dosis, según el texto.")
    x0, ww = x + 22, w - 44
    cols = (360, 250, 250, 250)
    caja(b, x0, yy, sum(cols), 44, c, fill=tinte(c), r=8)
    cx = x0 + cols[0]
    for k, hd in enumerate(("1 DOSIS", "2 DOSIS", "3 DOSIS")):
        rot(b, cx + 20, yy + 29, hd, c, size=14)
        cx += cols[k + 1]
    ry = yy + 44
    for f in ("Mosquito que no es resistente", "Mosquito resistente"):
        caja(b, x0, ry, sum(cols), 54, c, r=0)
        texto(b, x0 + 18, ry + 34, f, size=16, weight="700")
        cx = x0 + cols[0]
        for k in range(3):
            renglon(b, cx + 20, ry + 40, cx + cols[k + 1] - 20)
            cx += cols[k + 1]
        ry += 54
    cx = x0
    for k in range(3):
        cx += cols[k]
        b.append(line(cx, yy, cx, ry, c, 1.6))
    return ry


# ───────── QD · N.º 56 · carteleras ─────────
def datos_56(b, x, y, w):
    return pregunta(b, x, y, w, "Las cuatro carteleras llevan el mismo titular, «USAR INSECTICIDA NO TE PROTEGE 100% "
                                "DEL DENGUE», y debajo muestran lo que se describe en cada opción.")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "El titular y el dato que lo sostiene", c,
                      "Como en la balanza de los Pomsky: un titular vale lo que vale su dato. Antes de leer las "
                      "carteleras, escribe qué tendría que mostrar un dato para probar este titular.")
    x0, ww = x + 22, w - 44
    half = (ww - 20) / 2
    for k, (tit, ps) in enumerate((("EL DATO TENDRÍA QUE MOSTRAR…", "qué le pasa a quién, frente a qué"),
                                   ("NO ME BASTA UN DATO QUE…", "podría explicarse por otra causa"))):
        bx = x0 + k * (half + 20)
        caja(b, bx, yy, half, 104, c, r=14, dash="8,6" if k else None)
        rot(b, bx + 18, yy + 28, tit, c, size=14)
        pista(b, bx + 18, yy + 52, ps)
        renglon(b, bx + 18, yy + 90, bx + half - 18)
    return yy + 104


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="El modelo muestra la alternancia de generaciones entre células haploides y células diploides, en "
            "organismos con reproducción sexual.",
          o=["La mitosis, porque durante la fase diploide se lleva a cabo el proceso de división celular, y esto "
             "aumenta la variabilidad.",
             "La fase haploide, porque se duplica el número de cromosomas lo cual aumenta la variabilidad.",
             "La fertilización, porque se unen gametos de dos individuos diferentes y aumentan la variabilidad "
             "genética de la población.",
             "La formación de una célula haploide, porque a partir de la unión de dos células diploides genera gran "
             "variabilidad."],
          datos=datos_66, inst=ii1)
QB = dict(est=3, comp="Indagación", e=MONOS,
          o=["No, porque faltan grupos similares a los que no se les suministre el anticonceptivo para comparar los "
             "resultados.",
             "Sí, porque el experimento planteado es similar al que se realiza en humanos donde es más fácil reconocer "
             "el embarazo.",
             "No, porque al reunir los animales estos podrán estresarse por no estar en su ambiente natural.",
             "Sí, porque el anticonceptivo modifica los niveles hormonales de las hembras y esto las hace más "
             "agresivas."],
          datos=datos_63, inst=ii2)
QC = dict(est=2, comp="Explicación de fenómenos", e=DENGUE,
          o=["Debe mantenerse, porque los mosquitos resistentes pueden dejar de serlo si se disminuye la concentración "
             "de insecticida reduciendo la frecuencia de aplicación.",
             "Debe mantenerse, porque aunque haya algunos mosquitos resistentes, la cantidad de individuos resistentes "
             "es tan pequeña que la cantidad de picaduras será insignificante.",
             "Debe cambiarse, porque aunque al aumentar la frecuencia de aplicación se pueden eliminar todos los huevos "
             "de mosquitos, aún existirán larvas de otros insectos que probablemente se trasmitan la enfermedad.",
             "Debe cambiarse, porque al ser resistentes a los insecticidas sin importar su concentración, aunque se "
             "apliquen más dosis, estas probablemente no tendrán efecto sobre los mosquitos resistentes."],
          datos=datos_55, inst=ii3)
QD = dict(est=4, comp="Indagación",
          e="(El texto sobre el dengue está en la pregunta de arriba.) Los habitantes de un municipio quieren que "
            "todas las personas conozcan que el uso de insecticidas no garantiza la protección contra el dengue. ¿Cuál "
            "de las siguientes carteleras comunica apropiadamente resultados que soportan este descubrimiento?",
          o=["Un dibujo de dos mosquitos y la nota: «Los mosquitos Aedes aegypti y Aedes albopictus son similares, "
             "aunque pertenecen a especies diferentes».",
             "Una tabla: Aedes aegypti, resistente a las marcas 1, 2 y 3; Aedes albopictus, resistente a la 1 y "
             "susceptible a la 2 y la 3 (resistente: mortalidad < 80 %). Nota: «El mosquito de la especie Aedes "
             "aegypti es más resistente que el mosquito Aedes albopictus a la mayoría de los insecticidas».",
             "Una tabla de precios: Marca 1, $50.000; Marca 2, $25.000; Marca 3, $30.000. Nota: «Los costos de los "
             "insecticidas difieren según la marca».",
             "«Número de casos de personas infectadas entre 1993 y 1997»: 1993, 1500; 1994, 1800; 1995, 2000; 1996, "
             "1000; 1997, 2000. Nota: «Ha habido un aumento en el número de casos de personas infectadas al comparar "
             "los años 1993 y 1997»."],
          datos=datos_56, inst=ii4)


def build(pages=(170, 174)):
    return [hoja_icfes("bio5_i1", pages[0], QA, QB),
            hoja_icfes("bio5_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
