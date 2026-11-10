#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sociales y Ciudadanas · Misión 6 · entrenamiento ICFES · páginas 134 y 138.

Las cuatro preguntas salen del cuadernillo oficial Saber 11 2016-1, SEGUNDA sesión
(cuadernillo ABD, código «Saber 11 - 116 - B10O - ABD» / «P4 - ABD»), sección Sociales y
Ciudadanas, ítems 1 a 24. Verificadas contra la portada («2016-1 · Examen de Estado · Segunda
sesión») y la página escaneada en Drive («1. CUADERNILLOS ICFES» / «2016-2 SEGUNDA SESION.pdf»:
el archivo se llama 2016-2 pero la portada dice 2016-1, segunda sesión). Ninguna estaba en
tablero/icfes.csv. La N.º 6 se cambió por la N.º 2 porque la Misión 5 usa los ítems 5, 6, 18 y 19; los 7 a 12
nombran a un exalcalde vivo y no se usan.

Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11».
Ninguna nombra a un político colombiano vivo.

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · N.º 22 · C   (la MANE y la reforma de 2011 · movimientos sociales y democracia)  estrategia 1
    QB · N.º 14 · D   (Ley de Caducidad de Uruguay · qué consenso hay entre las partes)  estrategia 4
    QC · N.º 20 · C   (Plan de Desarrollo de los 90 · eficiencia y equidad)              estrategia 2
    QD · N.º 2  · A   (toque de queda para menores · qué dimensión y por qué)          estrategia 3
"""
from soc6 import *   # noqa: F401,F403  (configura la misión y EST)
from soc6 import rot, caja, pista, renglon, frase_hueco, cita


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · N.º 22 · la MANE ─────────
MANE = ("En el año 2011 el movimiento estudiantil colombiano se organizó a través de la Mesa Amplia Nacional "
        "Estudiantil (MANE), con el fin de protestar en contra del proyecto de ley de Reforma a la Educación "
        "Superior propuesto por el Gobierno nacional. Los estudiantes exigían una discusión amplia y democrática "
        "del contenido de la reforma, la cual ya estaba siendo discutida en el Congreso de la República. Ante las "
        "protestas, algunos sectores sociales insistieron en que tales manifestaciones generaban inestabilidad y "
        "que las reclamaciones debían tramitarse por las vías institucionales de representación democrática, "
        "tales como el legislativo. Finalmente, y después de dos meses de movilizaciones, el Gobierno decidió "
        "retirar el proyecto de ley y generar un proceso de socialización con la sociedad civil, incluidos "
        "estudiantes, profesores y directivos universitarios, entre otros.")


def datos_22(b, x, y, w):
    return pregunta(b, x, y, w, "De acuerdo con la situación descrita, ¿cuál de las siguientes opciones describe "
                                "adecuadamente la relación entre los movimientos sociales y la democracia?")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Por dónde pasa una demanda: el Congreso o la calle", c,
                      "Lo mismo que con Bobbio: la democracia no es solo lo que decide la mayoría en el Congreso. "
                      "Sigue el camino de esta demanda de principio a fin.")
    x0, ww = x + 22, w - 44
    bw, gap = (ww - 2 * 60) / 3, 60
    for k, (rt, ps) in enumerate((("LO QUE PEDÍAN", "los estudiantes, según el texto"),
                                  ("LO QUE LES DIJERON", "algunos sectores sociales"),
                                  ("CÓMO TERMINÓ", "qué hizo el Gobierno a los dos meses"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 112, c, r=16)
        rot(b, bx + 18, yy + 28, rt, c, size=14)
        pista(b, bx + 18, yy + 50, ps, size=14)
        renglon(b, bx + 18, yy + 92, bx + bw - 18)
        if k < 2:
            b.append(hand_arrow(bx + bw + 6, yy + 56, bx + bw + gap - 6, yy + 56, c, sw=3, bend=0.0, head=14))
    yy += 128
    return trampa(b, x0, yy, ww, "Algunos dijeron que las protestas generaban inestabilidad:",
                  "¿el final del texto les da la razón? Mira qué pasó con la reforma y con quién se abrió la "
                  "discusión antes de decidir qué le hacen los movimientos sociales a la democracia.", c)


# ───────── QB · N.º 14 · Ley de Caducidad ─────────
URUGUAY = ("Después de la restitución de la democracia en Uruguay, se aprobó la Ley de Caducidad, ratificada en "
           "dos referendos populares en 1989 y 2009, en la que se deja a decisión del Gobierno cualquier "
           "investigación sobre crímenes cometidos en la dictadura. Hay tres posiciones respecto a esta ley. Según "
           "la primera, algunos ciudadanos que aprobaron el referendo consideran que es mejor no revivir los hechos "
           "dolorosos que se padecieron durante la dictadura. La segunda: algunos familiares de víctimas que sí "
           "desean investigar estos, pero consideran que esta ley, al otorgarle al Estado la facultad de investigar "
           "hechos cometidos por sí mismo, es obstáculo a su derecho a la justicia y a la verdad, y puede dejar "
           "impunes los hechos. Finalmente, la Corte Interamericana de Derechos Humanos (CIDH) considera que la ley "
           "puede ser un impedimento para la obligación que tiene el Estado ante las víctimas de investigar los "
           "hechos a solicitud de sus familiares, y que estos hechos pueden quedar en el olvido.")


def datos_14(b, x, y, w):
    return pregunta(b, x, y, w, "¿Qué punto de consenso habría entre las partes?")


def ii2(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Tres actores, una ley: lo que comparten dos", c,
                      "Escribe en cada círculo lo que piensa ese actor. Lo que comparten dos va donde sus círculos "
                      "se cruzan.")
    x0, ww = x + 22, w - 44
    r = 104
    cy = yy + r + 34
    for cx in (x0 + 300, x0 + 470, x0 + 640):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}" fill-opacity="0.06" stroke="{c}" '
                 f'stroke-width="2.2"/>')
    rot(b, x0 + 300 - 20, cy - r - 12, "LOS QUE REFRENDARON", c, size=13, anchor="middle")
    rot(b, x0 + 470, cy + r + 24, "LOS FAMILIARES", c, size=13, anchor="middle")
    rot(b, x0 + 640 + 20, cy - r - 12, "LA CIDH", c, size=13, anchor="middle")
    bx = x0 + 820
    caja(b, bx, yy + 10, ww - 820, 2 * r + 40, c)
    rot(b, bx + 18, yy + 38, "LO QUE COMPARTEN DOS", c, size=14)
    pista(b, bx + 18, yy + 66, "quiénes:", size=14)
    renglon(b, bx + 90, yy + 68, bx + ww - 838)
    pista(b, bx + 18, yy + 108, "en qué coinciden:", size=14)
    for i in range(3):
        renglon(b, bx + 18, yy + 150 + i * 36, bx + ww - 838)
    return cy + r + 34


# ───────── QC · N.º 20 · eficiencia y equidad ─────────
def datos_20(b, x, y, w):
    yy = cita(b, x, y, w, "PLAN NACIONAL DE DESARROLLO · AÑOS 1990",
              "«La eficiencia no puede ser antagónica con la equidad. Por tanto, en las determinaciones públicas "
              "primarán siempre consideraciones para que el juego del mercado no comprometa la equidad ni restrinja "
              "el acceso y la participación equitativa de los más pobres».", EST[2][1], size=18)
    return pregunta(b, x, yy + 4, w, "En este fragmento se adopta una postura crítica frente al modelo neoliberal, "
                                     "porque")


def ii3(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Eficiencia y equidad en la misma frase", c,
                      "Lo de la misión: que algo funcione no basta. Parte la cita en dos y fíjate quién le pone "
                      "límites al mercado.")
    x0, ww = x + 22, w - 44
    half = (ww - 330) / 2
    for k, rt in enumerate(("LO QUE DICE DE LA EFICIENCIA", "LO QUE DICE DE LA EQUIDAD")):
        bx = x0 + k * (half + 20)
        caja(b, bx, yy, half, 92, c)
        rot(b, bx + 18, yy + 28, rt, c, size=14)
        renglon(b, bx + 18, yy + 72, bx + half - 18)
    bx = x0 + 2 * half + 40
    caja(b, bx, yy, ww - (bx - x0), 92, c, dash="8,6")
    rot(b, bx + 18, yy + 28, "QUIÉN PONE EL FRENO", c, size=14)
    renglon(b, bx + 18, yy + 72, x0 + ww - 18)
    yy += 108
    return alto_profe(b, x0, yy, ww,
                      "Modelo neoliberal: dejar que el mercado reparta los bienes y reducir lo que hace el Estado en "
                      "la economía. Con esa idea clara, busca qué parte del fragmento va en contra de ella.")


# ───────── QD · N.º 2 · toque de queda ─────────
TOQUE = ("En una ciudad del norte de Colombia, son recurrentes las quejas de la ciudadanía por la presencia de "
         "niños, niñas y adolescentes circulando por las calles hasta avanzadas horas de la noche. Las quejas "
         "también se relacionan con su presencia en bares y discotecas y con su aparente venta y consumo de "
         "sustancias psicoactivas. Al respecto, las autoridades policiales deciden establecer un toque de queda "
         "que va desde las 9 de la noche hasta las 6 de la mañana, los viernes, sábados y domingos. Esta medida")


def ii4(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Del motivo de la queja al efecto de la medida", c,
                      "Cada opción le pone una etiqueta a la medida (social, política, económica, de seguridad) y "
                      "le agrega un «porque». Antes de mirar las etiquetas, sigue la cadena del caso.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 56
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("DE QUÉ SE QUEJAN", "lo que ven en las calles de noche"),
                                  ("QUÉ HACE LA MEDIDA", "a quién, cuándo y dónde"),
                                  ("QUÉ BUSCA CUIDAR", "y a quién, según el caso"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 104, c, r=16)
        rot(b, bx + 18, yy + 28, rt, c, size=14)
        pista(b, bx + 18, yy + 50, ps, size=14)
        renglon(b, bx + 18, yy + 88, bx + bw - 18)
        if k < n - 1:
            b.append(hand_arrow(bx + bw + 6, yy + 52, bx + bw + gap - 6, yy + 52, c, sw=3, bend=0.0, head=14))
    yy += 120
    return trampa(b, x0, yy, ww, "La etiqueta no decide: decide el «porque»:",
                  "revisa si lo que dice cada opción después de «porque» se sigue de tu cadena. Por ejemplo, "
                  "¿un toque de queda le quita trabajo a la policía en la noche, o le pone más?", c)


QA = dict(est=1, comp="Pensamiento reflexivo y sistémico", e=MANE,
          o=["Los movimientos sociales derivan en protestas que generan un ambiente de inestabilidad y debilitan "
             "la democracia.",
             "Los movimientos sociales solo son democráticos cuando hacen uso de las vías institucionales de "
             "representación.",
             "Los movimientos sociales permiten canalizar y expresar demandas sociales y, por tanto, fortalecen la "
             "democracia.",
             "Los movimientos sociales son los únicos mecanismos de representación y participación en una "
             "democracia como la colombiana."],
          datos=datos_22, inst=ii1)
QB = dict(est=4, comp="Interpretación de perspectivas", e=URUGUAY,
          o=["Los ciudadanos que refrendaron la ley coinciden con la CIDH en que es necesario que no se revivan los "
             "hechos dolorosos de la dictadura.",
             "Los familiares de las víctimas y los ciudadanos que refrendaron están de acuerdo en que es decisión "
             "de la ciudadanía investigar o no los hechos de la dictadura.",
             "La CIDH está de acuerdo con los familiares de las víctimas en que el Estado uruguayo puede decidir qué "
             "casos de violaciones a los DH se pueden investigar.",
             "Los familiares de víctimas y la CIDH coinciden en que esta ley se convierte en un instrumento de "
             "perpetuación de la impunidad y olvido de los hechos."],
          datos=datos_14, inst=ii2)
QC = dict(est=2, comp="Pensamiento reflexivo y sistémico",
          e="En el Plan Nacional de Desarrollo de Colombia de la década de los años 1990, se afirma lo siguiente:",
          o=["se reconoce el papel central del Estado en la buena gestión y administración de los recursos "
             "públicos.",
             "se define el mercado como el principal mecanismo para distribuir eficientemente los beneficios del "
             "crecimiento económico.",
             "se afirma que, sin la intervención del Estado, no es posible garantizarle buenas condiciones de vida a "
             "toda la población.",
             "se señala implícitamente que la privatización de las empresas del Estado es un mecanismo eficiente "
             "para garantizar la equidad."],
          datos=datos_20, inst=ii3)
QD = dict(est=3, comp="Pensamiento reflexivo y sistémico", e=TOQUE,
          o=["es positiva socialmente, porque disminuiría la exposición de los menores a diversos riesgos.",
             "es negativa políticamente, porque vulneraría los derechos fundamentales de los menores.",
             "es positiva económicamente, porque disminuiría la presencia policial a avanzadas horas de la noche.",
             "es negativa para la seguridad, porque incrementaría los índices de delincuencia común."],
          inst=ii4)


def build(pages=(134, 138)):
    return [hoja_icfes("soc6_i1", pages[0], QA, QB),
            hoja_icfes("soc6_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
