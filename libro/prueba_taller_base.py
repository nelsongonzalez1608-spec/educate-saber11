#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prueba del motor reconstruido: rehace con taller_base.py dos páginas ya entregadas,
para compararlas lado a lado con su imagen en referencia/hojas/.

    página 107 · soc2_t3 · Sociales M2, preguntas 5 y 6 (taller, con franja de vocabulario)
    página 106 · soc2_i1 · Sociales M2, entrenamiento ICFES 1 y 2

Los textos se transcribieron de las imágenes de referencia. No es el módulo soc2.py
(perdido): es la prueba de que el motor vuelve a producir la misma hoja.
"""
from taller_base import *

configurar("Sociales y Ciudadanas", 2, "competencias ciudadanas",
           tema="Contrastar posturas: en qué coinciden, en qué no",
           color=EDU_ORO, nota="LO QUE ANOTÉ DEL CASO")
EST = {1: ("En qué coinciden y en qué no", EDU_AZUL), 2: ("El nombre exacto de la figura", EDU_VERDE),
       3: ("Las dos caras de la misma medida", EDU_ORO), 4: ("Qué queda en entredicho", "#5B3E96")}
usar_estrategias(EST)
MORADO = EST[4][1]


def i5(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "Pon la frase encima de los hechos y mira si cuadran", MORADO,
                      "Arriba, lo que la frase anuncia. Abajo, lo que el texto cuenta que ocurrió. "
                      "Cuando no cuadran, la frase ya no informa: muestra algo.")
    x0, ww = x + 22, w - 44
    for rot, pista, dy in (("LO QUE LA FRASE ANUNCIA", "«defendiendo la democracia»", 0),
                           ("LO QUE EL TEXTO CUENTA QUE PASÓ", "cerca de 100 muertos, desapariciones", 80)):
        b.append(T(x0, yy + dy + 18, [rot], 15, MORADO, weight="700", ls=1.5))
        b.append(T(x0 + 600, yy + dy + 18, [pista], 15, GRAY, style="italic"))
        b.append(rect(x0, yy + dy + 26, ww, 42, "white", r=10, stroke=MORADO, sw=2))
    b.append(T(x0 + ww - 4, yy + 90, ["contra"], 15, MORADO, style="italic", anchor="end"))
    yy += 166
    b.append(rect(x0, yy, ww, 48, "white", r=10, stroke=MORADO, sw=2))
    b.append(T(x0 + 24, yy + 31, ["Entonces la frase sirve para ilustrar una ____________________ ."], 18,
               INK, weight="700"))
    yy += 64
    return trampa(b, x0, yy, ww, "Una opción dice que la frase «demuestra un consenso absoluto»:",
                  "el texto dice lo contrario, que la frase es controversial. Y otra la convierte en un "
                  "argumento legal para no investigar, que es una conclusión que el texto nunca saca.",
                  MORADO)


def i6(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "Escribe el deber del Estado y después mira cuál se rompió", MORADO,
                      "El Estado Social de Derecho existe para garantizar derechos. La pregunta es cuál de "
                      "sus deberes queda en entredicho cuando hay desapariciones y ejecuciones.")
    x0, ww = x + 22, w - 44
    b.append(rect(x0, yy, ww, 48, "white", r=10, stroke=MORADO, sw=2))
    b.append(T(x0 + 24, yy + 31, ["El Estado debe proteger los derechos de ______________ , incluso "
                                  "cuando se defiende."], 18, INK))
    yy += 64
    yy = ojo(b, x0, yy, ww, "OJO CON LA OPCIÓN D",
             "Dice que la conmoción interior «faculta al Estado para SUSPENDER» derechos.",
             fuerte="La Constitución dice LIMITAR, más no suspender. Compruébalo tú: está en la página 99.")
    yy += 14
    yy = trampa(b, x0, yy, ww, "Y otra opción no describe un deber sino su contrario:",
                "«la posibilidad de las Fuerzas Militares de actuar sin límites legales» no es un aspecto "
                "del Estado Social de Derecho: es justo lo que ese modelo prohíbe.", MORADO)
    yy += 14
    return alto_profe(b, x, yy, w - 4,
                      "El ESTADO SOCIAL DE DERECHO en una frase: el Estado existe para garantizar derechos, "
                      "y por eso ni siquiera defendiéndose puede desconocerlos. Ojo con la opción D: ver la "
                      "página 99.")


def datos_veg(b, x, y, w):
    c = EST[1][1]
    yy = y
    for k, (rot, txt) in enumerate((
            ("LAS DOS OPINIONES, LAS DOS A FAVOR DEL VEGETARIANISMO",
             "PRIMERA PERSONA: consumir carne es nocivo para los humanos, porque el animal sufre en el "
             "proceso y eso produce energías negativas que se transmiten al consumidor y perjudican su salud."),
            (None, "SEGUNDA PERSONA: el consumo de productos de origen animal es un acto amoral, en la "
                   "medida en que resulta del abuso e insensibilidad del ser humano ante los demás seres vivos."))):
        top = 26 if rot else 0
        svg, y2 = TJ(x + 34, yy + 14 + top, txt, w - 70, 17, INK, style="italic", lh=26)
        hh = y2 - yy + 12
        b.append(rect(x + 10, yy, w - 30, hh, SOFT, r=10))
        b.append(rect(x + 10, yy, 8, hh, c, r=4))
        if rot:
            b.append(T(x + 34, yy + 26, [rot], 13, c, weight="700", ls=1.5))
        b.append(svg)
        yy += hh + 12
    return yy


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Te piden la que NO es correcta: marca primero las tres que sí", c,
                      "Es la trampa más común de toda la prueba. Lee cada opción y pregúntate «¿esto es "
                      "cierto?». Marca las tres ciertas. La que queda sin marcar es la respuesta.")
    for k, t in enumerate(("«son similares, porque las dos van contra el consumo de carne»",
                           "«son complementarias, porque las dos argumentan proteger a los animales»",
                           "«son diferentes: una por la salud humana, otra por el bienestar animal»",
                           "«son disímiles: una mira del animal al humano, la otra del humano al animal»")):
        ry = yy + k * 46
        b.append(rect(x + 38, ry, 920, 38, "white", r=8, stroke=c, sw=1.8))
        b.append(T(x + 56, ry + 25, [t], 15, INK, style="italic"))
        for j, lab in enumerate(("cierta", "falsa")):
            b.append(checkbox(x + 990 + j * 120, ry + 8, s=10, c=c))
            b.append(T(x + 1020 + j * 120, ry + 25, [lab], 14, GRAY))
    yy += 4 * 46 + 10
    return trampa(b, x + 38, yy, w - 90, "Vuelve a la PRIMERA opinión antes de decidir:",
                  "¿habla de proteger a los animales o de la salud de quien come? Esa es la única afirmación "
                  "que le atribuye a alguien algo que no dijo, y por eso es la que NO es correcta.", c)


def datos_const(b, x, y, w):
    c = EST[2][1]
    svg, y2 = TJ(x + 34, y + 40, "Uno de los principios de nuestra Constitución es que los derechos de los "
                 "menores «prevalecen sobre los derechos de los demás». Ante unos altos índices de delincuencia "
                 "juvenil, el nuevo presidente decide reformar la Constitución para modificar ese principio.",
                 w - 70, 17, INK, style="italic", lh=26)
    hh = y2 - y + 12
    b.append(rect(x + 10, y, w - 30, hh, SOFT, r=10))
    b.append(rect(x + 10, y, 8, hh, c, r=4))
    b.append(T(x + 34, y + 24, ["EL CASO COMPLETO"], 13, c, weight="700", ls=1.5))
    b.append(svg)
    yy = y2 + 26
    b.append(f'<circle cx="{x + 22}" cy="{yy - 6}" r="5" fill="{c}"/>')
    b.append(T(x + 40, yy, ["Constitución Política de Colombia"], 15, c, weight="700"))
    b.append(T(x + 300, yy, ["· artículo 103 · mecanismos de participación"], 14, GRAY))
    return yy + 6


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Primero: ¿qué se quiere cambiar, una ley o la Constitución?", c,
                      "El mecanismo no se elige por quién lo propone: se elige por lo que se quiere cambiar. "
                      "Escríbelo y después mira cuál de los cuatro sirve para eso.")
    b.append(T(x + 24, yy + 18, ["LO QUE SE QUIERE CAMBIAR ES…"], 14, c, weight="700", ls=1.5))
    b.append(rect(x + 420, yy, 790, 38, "white", r=8, stroke=c, sw=2))
    yy += 56
    for k, (m, d) in enumerate((("referendo", "aprueba o deroga una norma, incluida una reforma constitucional"),
                                ("plebiscito", "apoya o rechaza una decisión del presidente"),
                                ("consulta popular", "responde una pregunta de interés nacional o local"),
                                ("cabildo abierto", "reúne a la comunidad para discutir asuntos del municipio"))):
        ry = yy + k * 48
        b.append(checkbox(x + 24, ry + 8, s=11, c=c))
        b.append(rect(x + 70, ry, 300, 40, "white", r=8, stroke=c, sw=1.8))
        b.append(T(x + 90, ry + 27, [m], 16, c, weight="700"))
        b.append(T(x + 400, ry + 27, [d], 16, INK))
    yy += 4 * 48 + 14
    return ojo(b, x, yy, w - 20, "Los otros tres existen y son válidos:",
               "solo que ninguno de ellos reforma la Constitución. Esa es toda la pregunta.")


Q = {5: dict(n=5, est=4, pag=348, ctx="Palacio de Justicia · qué función cumple la frase",
             comp="Interpretación de perspectivas", inst=i5),
     6: dict(n=6, est=4, pag=348, ctx="Estado Social de Derecho · qué deber se cuestiona",
             comp="Pensamiento reflexivo y sistémico", inst=i6)}
QA = dict(est=1, f="Pregunta oficial ICFES · Saber 11",
          e="Las dos personas están a favor del vegetarianismo. ¿Cuál de las siguientes afirmaciones sobre la "
            "relación entre las opiniones presentadas NO es correcta?",
          o=["Son similares, porque ambas van en contra del consumo de carne.",
             "Son complementarias, porque ambas promueven el vegetarianismo cuando argumentan la obligación de "
             "proteger a los animales.",
             "Son diferentes, porque la primera aboga por la salud del ser humano y la segunda, por el bienestar "
             "de los animales.",
             "Son disímiles, porque la primera se centra en cómo el animal afecta al ser humano y la segunda, en "
             "cómo el ser humano afecta al animal."],
          datos=datos_veg, inst=ii1)
QB = dict(est=2, f="Pregunta oficial ICFES · Saber 11",
          e="El presidente puede hacerlo a través de alguno de los mecanismos de participación ciudadana que "
            "contempla la misma Constitución; este mecanismo debe ser",
          o=["El referendo.", "El plebiscito.", "La consulta popular.", "El cabildo abierto."],
          datos=datos_const, inst=ii2)


def build():
    return [hoja_taller("prueba_soc2_t3", 107, 3, Q[5], Q[6]),
            hoja_icfes("prueba_soc2_i1", 106, QA, QB)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
