#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sociales y Ciudadanas · Misión 3 · entrenamiento ICFES (páginas 113 y 117 del cuaderno).

Las cuatro preguntas salen del cuadernillo «Saber 11 · 2016-1 · Examen de Estado · primera sesión»
(Drive de Nelson, carpeta «1. CUADERNILLOS ICFES», archivo «2016-1 PRIMERA SESION.pdf», sección
Sociales y Ciudadanas, encabezado «Saber 11 - 116 - B05R - AAM»). Es una fotocopia del cuadernillo
con su portada; como no se cotejó contra la publicación liberada del ICFES, el membrete va sin año
(regla 7; desde el 10 nov, siempre «Pregunta Saber 11»).

Claves verificadas resolviendo cada pregunta (6 nov 2026):

    QA·A  (ítem 74 · el gerente y el voto de los empleados)       estrategia 1
    QB·B  (ítem 80 · la Ley Seca del Mundial 2014)                  estrategia 2
    QC·B  (ítem 70 · la niña wayú y la autonomía indígena)          estrategia 3
    QD·D  (ítem 90 · retirar a los consumidores del barrio)         estrategia 4
"""
from taller_base import *
from taller_base import _mezcla
import soc3  # noqa: F401  (configura el área, la misión y las estrategias)
from soc3 import AZ, VE, RO, MO, rot, pista, casilla, si_no

F = "Pregunta Saber 11"


def caja_texto(b, x, y, w, rotulo, txt, c):
    svg, y2 = TJ(x + 34, y + 38, txt, w - 70, 17, INK, style="italic", lh=25)
    hh = y2 - y + 10
    b.append(rect(x + 10, y, w - 30, hh, SOFT, r=10))
    b.append(rect(x + 10, y, 8, hh, c, r=4))
    b.append(T(x + 34, y + 24, [rotulo], 13, c, weight="700", ls=1.5))
    b.append(svg)
    return y2 + 6


# ───────── QA · el gerente y el voto ─────────
def iia(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La frase tiene que hablar de lo que pasó, no de la política en general", c,
                      "Escribe qué hizo el gerente y qué le molesta al empleado. La frase que lo apoya tiene "
                      "que hablar de eso mismo.")
    x0 = x + 22
    for k, lab in enumerate(("Lo que hizo el gerente:", "Lo que le molesta al empleado:")):
        cx = x0 + k * 620
        b.append(T(cx, yy + 20, [lab], 17, c, weight="700"))
        casilla(b, cx, yy + 32, 590, 44, c)
    yy += 100
    rot(b, x0 + 70, yy, "¿HABLA DE LO QUE HIZO EL GERENTE?", c, size=13)
    rot(b, x0 + 620, yy, "¿DICE LO MISMO QUE EL EMPLEADO?", c, size=13)
    yy += 14
    for k, L in enumerate("ABCD"):
        ry = yy + k * 44
        b.append(f'<circle cx="{x0 + 18}" cy="{ry + 16}" r="15" fill="white" stroke="{c}" stroke-width="2"/>')
        b.append(T(x0 + 18, ry + 22, [L], 15, c, weight="700", anchor="middle"))
        si_no(b, x0 + 70, ry + 5, c)
        si_no(b, x0 + 620, ry + 5, c)
    return yy + 4 * 44


# ───────── QB · la Ley Seca ─────────
def iib(b, x, y, w, h):
    c = VE
    yy = titulo_instr(b, x, y, "La medida apunta a un blanco: mira a quién más le cae", c,
                      "Toda medida tiene un efecto que se buscaba y otros que le caen a alguien sin que nadie los "
                      "buscara. Escribe primero el que se buscaba; después, a quién más le toca la Ley Seca ese día.")
    x0 = x + 22
    bw = 260
    b.append(rect(x0, yy + 40, bw, 70, _mezcla(c, 0.88), r=14, stroke=c, sw=2.2))
    b.append(T(x0 + bw / 2, yy + 84, ["la Ley Seca"], 19, c, weight="700", anchor="middle"))
    rx = x0 + bw + 120
    rw = w - 44 - (bw + 120)
    for k, (lab, p) in enumerate((("LO QUE SE BUSCABA", "¿qué se quería que dejara de pasar?"),
                                  ("LO QUE LE CAE A ALGUIEN MÁS", "¿a quién? ¿qué pierde o qué gana?"))):
        ry = yy + k * 92
        rot(b, rx, ry + 14, lab, c)
        casilla(b, rx, ry + 24, rw, 50, c)
        pista(b, rx + 16, ry + 44, p, size=13)
        b.append(hand_arrow(x0 + bw + 8, yy + 75, rx - 12, ry + 49, c, sw=2.6, bend=0.0, head=14))
    yy += 196
    return ojo(b, x0, yy, w - 44, "Un efecto no esperado no es cualquier cosa:",
               "tiene que poder salir de prohibir el licor ese día en la ciudad. Antes de marcar, pregúntale "
               "a cada opción si eso de verdad podría pasar por la Ley Seca.")


# ───────── QC · la niña wayú ─────────
def iic(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Cada lado del conflicto tiene su propio respaldo en la Constitución", c,
                      "Un conflicto tiene dos lados. Escribe qué defiende cada uno y en qué se apoya. La opción "
                      "correcta pone uno de cada lado, sin contradecir lo que dijo la Corte.")
    x0 = x + 22
    cw_ = (w - 44 - 30) // 2
    for k, (quien, p) in enumerate((("LA NIÑA", "pide ________ y se apoya en ________"),
                                    ("LA COMUNIDAD WAYÚ", "se opone porque ________ y se apoya en ________"))):
        cx = x0 + k * (cw_ + 30)
        casilla(b, cx, yy, cw_, 76, c, sw=2.2)
        rot(b, cx + 18, yy + 26, quien, c)
        pista(b, cx + 18, yy + 54, p, size=14)
    yy += 96
    return ojo(b, x0, yy, w - 44, "OJO CON LO QUE DIJO LA CORTE",
               "Antes de aceptar una opción, compárala con el texto: ¿la Corte Constitucional permitió o "
               "prohibió la interrupción del embarazo en un caso como este? Una opción que lo cambie ya no "
               "describe este conflicto.")


# ───────── QD · el barrio ─────────
def datos_d(b, x, y, w):
    return caja_texto(b, x, y, w, "EL CASO",
                      "En Bogotá existe un barrio en el que han venido concentrándose consumidores y vendedores de "
                      "drogas ilegales. Para mejorar la situación de este barrio, y de los consumidores de drogas que "
                      "a él acuden, la Alcaldía Mayor propuso retirar del barrio a todos los traficantes de drogas, y "
                      "a todos los consumidores. En segundo lugar, se han propuesto controles médicos para los "
                      "consumidores, los cuales incluirían programas de sustitución de sustancias.", MO)


def iid(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Sigue a los consumidores después de que salen del barrio", c,
                      "La pregunta deja solo la primera solución: retirar. Los controles médicos no cuentan aquí. "
                      "Sigue a las personas un paso más allá del barrio.")
    x0 = x + 22
    cw_ = (w - 44 - 80) // 3
    for k, lab in enumerate(("los retiran del barrio", "¿a dónde van?", "¿qué pasa con su adicción?")):
        cx = x0 + k * (cw_ + 40)
        b.append(T(cx, yy + 20, [lab], 17, c, weight="700"))
        casilla(b, cx, yy + 32, cw_, 44, c)
        if k < 2:
            b.append(f'<polygon points="{cx + cw_ + 10},{yy + 44} {cx + cw_ + 30},{yy + 54} '
                     f'{cx + cw_ + 10},{yy + 64}" fill="{c}"/>')
    return yy + 80


QA = dict(est=1, comp="Interpretación de perspectivas", f=F,
          e="Durante la época electoral, el gerente de una empresa les dice a sus subalternos que deben votar por "
            "el candidato de un determinado partido político, y que si no lo hacen, perderán su trabajo. Un "
            "empleado afirma que esto es inapropiado. ¿Cuál es la frase que mejor apoya lo que dice el empleado?",
          o=["Amenazar a la gente para que vote por un determinado partido es un abuso.",
             "Hablar de política siempre lleva a conflictos porque nadie se pone de acuerdo.",
             "La obligación de los superiores es ilustrar a los empleados en política.",
             "Los gerentes de las empresas no deberían interesarse en temas políticos."],
          inst=iia)
QB = dict(est=2, comp="Pensamiento reflexivo y sistémico", f=F,
          e="Durante el primer partido de Colombia en el Mundial de Fútbol 2014 y después de este, se presentaron "
            "en la ciudad de Bogotá episodios de violencia y alteración del orden público. Por esto, para el "
            "momento del segundo partido, la Administración Distrital tomó la decisión de decretar la Ley Seca. "
            "¿Qué efectos NO esperados podría tener la solución dada por la Administración Distrital?",
          o=["El ahorro de los hogares bogotanos en gastos como el licor, los parqueaderos y la alimentación.",
             "Las pérdidas económicas de los comerciantes de la ciudad en una ocasión que generalmente trae "
             "ganancias.",
             "El aumento de episodios de violencia urbana, accidentes de tránsito y alteración del orden público.",
             "Aceptación de la medida por toda la ciudadanía para evitar que se presenten hechos de violencia en "
             "la ciudad."],
          inst=iib)
QC = dict(est=3, comp="Pensamiento social", f=F,
          e="En el 2012, una niña de once años perteneciente a la comunidad indígena wayú declaró que estaba "
            "embarazada y solicitó al Estado colombiano que se le practicara un aborto con el argumento de que su "
            "padre la había violado y, por dictamen de la Corte Constitucional, en esa situación es legítima la "
            "interrupción voluntaria del embarazo. La comunidad wayú se opuso radicalmente a la solicitud de la "
            "niña porque el aborto es una práctica prohibida en la legislación de este grupo indígena. En esta "
            "situación, ¿qué aspectos entran en conflicto?",
          o=["El principio constitucional de la prohibición a cualquier tipo de discriminación étnica y la "
             "solicitud de la niña por igualdad de condiciones ante la ley.",
             "El principio constitucional del respeto por la autonomía de los grupos indígenas y la legitimidad "
             "de la solicitud de la niña wayú como ciudadana colombiana.",
             "El principio constitucional de la legitimidad del aborto en caso de abuso sexual y el respeto de "
             "la cultura wayú hacia los derechos de los niños.",
             "El principio constitucional que prohíbe la tortura y el dictamen de la Corte Constitucional que "
             "prohíbe la interrupción voluntaria del embarazo."],
          inst=iic)
QD = dict(est=4, comp="Pensamiento reflexivo y sistémico", f=F,
          e="Si se decidiera implementar únicamente la primera solución, ¿qué impacto tendría en las personas que "
            "consumen drogas?",
          o=["Positivo, pues ya no podrían comprar drogas a los traficantes y esta abstinencia forzosa los curaría.",
             "Negativo, pues se acabaría con la principal actividad económica del barrio y tendrían que "
             "trasladarse a otro.",
             "Positivo, pues gracias al apoyo médico podrían superar su problema de adicción a las drogas.",
             "Negativo, ya que encontrarían otros expendedores y su adicción continuaría sin ser tratada."],
          datos=datos_d, inst=iid)


def build(pages=(113, 117)):
    return [hoja_icfes("soc3_i1", pages[0], QA, QB),
            hoja_icfes("soc3_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
