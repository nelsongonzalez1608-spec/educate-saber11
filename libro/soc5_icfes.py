#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sociales y Ciudadanas · Misión 5 · entrenamiento ICFES · páginas 127 y 131.

Las cuatro preguntas salen del cuadernillo oficial Saber 11 «2016-1 · Examen de Estado ·
Segunda sesión», cuadernillo ABD (encabezado «Saber 11 - 116 - B10O - ABD · 2a. sesión»),
sección Sociales y Ciudadanas. Fotocopia en Drive: «1. CUADERNILLOS ICFES» /
«2016-2 SEGUNDA SESION.pdf» (el nombre del archivo dice 2016-2, la portada dice 2016-1).
Número de ítem leído en la página. Membrete (regla 7, Nelson 10 nov):
siempre «Pregunta Saber 11».

Descartados de la misma sección: 7 a 12 (el texto de Molano nombra a Juan Martín Caicedo,
político colombiano vivo) y 24 (la opción que parece correcta dice «No» y da una razón de «Sí»).

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · ítem 5  · D   (pobreza y zonas de riesgo · por qué allí)          estrategia 1
    QB · ítem 6  · D   (los caminos reales · qué está en conflicto)        estrategia 2
    QC · ítem 19 · C   (Genovia, el tratado y los subsidios)               estrategia 3
    QD · ítem 18 · B   (la Real Audiencia y la encomienda, 1557 y 1560)    estrategia 4
"""
from soc5 import *   # noqa: F401,F403  (configura la misión y EST)

F = "Pregunta Saber 11"


# ───────── QA · ítem 5 ─────────
def ii1(b, x, y, w, h):
    c = VE
    yy = titulo_instr(b, x, y, "La orilla, la ladera y el centro: quién llega a cada lugar", c,
                      "Para cada lugar marca qué tanto riesgo tiene y escribe qué necesitaría una familia para vivir "
                      "allí. La pregunta no pide qué tiene de bueno el lugar: pide por qué terminan ahí.")
    x0, ww = x + 22, w - 44
    zw = (ww - 40) / 3
    for k, rt in enumerate(("LA ORILLA DEL RÍO", "LA LADERA EMPINADA", "EL CENTRO PLANO Y FIRME")):
        bx = x0 + k * (zw + 20)
        caja(b, bx, yy, zw, 160, c, r=14)
        rot(b, bx + 18, yy + 30, rt, c, size=14)
        b.append(T(bx + 18, yy + 64, ["riesgo:"], 15, GRAY))
        for j, lab in enumerate(("alto", "bajo")):
            b.append(checkbox(bx + 84 + j * 100, yy + 48, s=10, c=c))
            b.append(T(bx + 110 + j * 100, yy + 64, [lab], 15, GRAY))
        pista(b, bx + 18, yy + 100, "para vivir aquí, una familia necesita…", size=14)
        renglon(b, bx + 18, yy + 138, bx + zw - 18)
    yy += 176
    return trampa(b, x0, yy, ww, "Una razón que querría cualquier familia no explica nada:",
                  "si lo que dice una opción le sirve igual a una familia rica, no explica por qué las familias "
                  "pobres son las que terminan en la orilla y en la ladera. Busca lo que sale de la definición de "
                  "pobreza que da el texto.", c)


# ───────── QB · ítem 6 ─────────
def ii2(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Un camino real con un dueño de cada lado", c,
                      "Un conflicto necesita dos lados que choquen. Escribe qué gana uno y qué pierde el otro, con las "
                      "palabras del texto.")
    x0, ww = x + 22, w - 44
    half = (ww - 150) / 2
    for k, (rt, ps) in enumerate((("LA GOBERNACIÓN", "con el proyecto, el departamento gana…"),
                                  ("ALGUNOS HABITANTES", "con el proyecto, ellos pierden…"))):
        bx = x0 + k * (half + 150)
        caja(b, bx, yy, half, 112, c, r=14)
        rot(b, bx + 20, yy + 30, rt, c)
        pista(b, bx + 20, yy + 56, ps)
        renglon(b, bx + 20, yy + 92, bx + half - 20)
    mx = x0 + half + 75
    b.append(f'<path d="M {mx - 50} {yy + 100} L {mx - 18} {yy + 56} L {mx + 18} {yy + 56} L {mx + 50} {yy + 100}" '
             f'fill="none" stroke="{c}" stroke-width="2.4" stroke-dasharray="6,6"/>')
    b.append(T(mx, yy + 40, ["el camino"], 14, GRAY, style="italic", anchor="middle"))
    yy += 128
    return frase_hueco(b, x0, yy, ww, "Chocan ______________________ y ______________________ .", c)


# ───────── QC · ítem 19 ─────────
def ii3(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Firmar y subsidiar: a quién le llega cada medida", c,
                      "Son dos medidas, una detrás de la otra. Para cada una escribe quién gana y quién pierde en "
                      "Genovia. La segunda medida existe por lo que dejó la primera.")
    x0, ww = x + 22, w - 44
    c0, c1 = x0, x0 + 300
    cw = (ww - 300 - 20) / 2
    rot(b, c1 + 16, yy + 18, "QUIÉN GANA EN GENOVIA", c)
    rot(b, c1 + cw + 36, yy + 18, "QUIÉN PIERDE O QUEDA EN RIESGO", c)
    yy += 30
    for k, rt in enumerate(("1 · FIRMAR EL TRATADO", "2 · DAR LOS SUBSIDIOS")):
        caja(b, c0, yy, 286, 64, c, r=12)
        rot(b, c0 + 16, yy + 38, rt, c, size=13)
        caja(b, c1, yy, cw, 64, c)
        caja(b, c1 + cw + 20, yy, cw, 64, c)
        if k == 0:
            b.append(hand_arrow(c0 + 140, yy + 66, c0 + 140, yy + 82, c, sw=2.4, bend=0, head=10))
        yy += 82
    yy += 4
    return frase_hueco(b, x0, yy, ww, "El subsidio sirve para que ______________________ no ______________________ .", c)


# ───────── QD · ítem 18 ─────────
def ii4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "1557 y 1560: qué cambió para el indígena y para el encomendero", c,
                      "Escribe cómo estaba cada uno con la encomienda y cómo quedó después de las dos órdenes de la "
                      "Real Audiencia. El propósito de una norma se lee en quién queda distinto.")
    x0, ww = x + 22, w - 44
    c1 = x0 + 230
    cw = (ww - 230 - 70) / 2
    rot(b, c1 + 16, yy + 18, "CON LA ENCOMIENDA", c)
    rot(b, c1 + cw + 86, yy + 18, "DESPUÉS DE 1557 Y 1560", c)
    yy += 30
    for rt in ("EL INDÍGENA", "EL ENCOMENDERO"):
        rot(b, x0, yy + 38, rt, c, size=14)
        caja(b, c1, yy, cw, 64, c)
        b.append(hand_arrow(c1 + cw + 10, yy + 32, c1 + cw + 60, yy + 32, c, sw=2.6, bend=0, head=12))
        caja(b, c1 + cw + 70, yy, cw, 64, c)
        yy += 80
    return ojo(b, x0, yy + 4, ww, "AYUDAR NO ES LO MISMO QUE IGUALAR",
               "Que una orden mejore algo para alguien no dice todavía para qué se dio. Mira tu tabla: ¿a quién "
               "le cambió más la situación, en qué sentido, y qué ganaba la Corona con ese cambio?")


def datos_pregunta(texto):
    def _d(b, x, y, w):
        svg, y2 = TJ(x, y + 4, texto, w, 20, INK, weight="700", lh=28)
        b.append(svg)
        return y2
    return _d


QA = dict(est=1, comp="Pensamiento reflexivo y sistémico", f=F,
          e="La pobreza puede entenderse como la privación de los recursos económicos para satisfacer las "
            "necesidades básicas como alimentación, salud, educación y vivienda dignas y está, generalmente, "
            "asociada con la carencia de capacidades para lograr una participación satisfactoria en los procesos "
            "sociales, políticos, cívicos y culturales. Distintas evidencias muestran que, debido a estas "
            "características, las poblaciones en condición de pobreza son más vulnerables ante los desastres "
            "naturales.",
          datos=datos_pregunta("¿Por cuál de las siguientes razones las poblaciones pobres tienden a instalarse "
                               "en áreas de mayor riesgo de desastre natural?"),
          o=["Porque les permite estar cerca de sus lugares de trabajo y de sus familias.",
             "Porque allí tienen facilidades de acceso a servicios de educación y salud.",
             "Porque en esas áreas pueden tener contacto permanente con la naturaleza.",
             "Porque el valor del suelo en estas áreas está acorde con su poder adquisitivo."],
          inst=ii1)
QB = dict(est=2, comp="Interpretación de perspectivas", f=F,
          e="La gobernación de un departamento tiene como proyecto recuperar los caminos reales de la época "
            "colonial que recorren varios municipios. Se propone que estos sean el eje de la promoción del "
            "departamento como destino turístico para caminantes y amantes de la naturaleza. Algunos habitantes de "
            "la zona dudan acerca de los beneficios de este proyecto, pues los caminos pasan por parte de sus "
            "tierras de cultivo y ganadería por tanto su recuperación y aprovechamiento implicaría expropiar estas "
            "tierras. Mencionan también que en los títulos de propiedad de sus tierras no hay nada que indique que "
            "una parte de sus terrenos sea pública. Adicionalmente, no ven que el turismo sea beneficioso para "
            "ellos.",
          datos=datos_pregunta("¿Qué aspectos de esta situación están en conflicto?"),
          o=["El interés de los gobernantes de desarrollar proyectos que beneficien a su región y el interés de "
             "los caminantes.",
             "La necesidad de proteger el medio ambiente y la naturaleza y la obligación de los gobernantes de "
             "proteger el patrimonio cultural.",
             "El desarrollo de la región como destino turístico y el incremento del poder político del gobernador.",
             "El desarrollo de una nueva fuente de ingresos para la región y una afectación en las tierras de los "
             "campesinos."],
          inst=ii2)
QC = dict(est=3, comp="Pensamiento reflexivo y sistémico", f=F,
          e="Genovia, un país productor de alimentos, discute un tratado de libre comercio con un país productor de "
            "zapatos y moda en general, Estasia. Esto haría que los zapatos y las prendas de vestir sean más baratos "
            "en Genovia y que este a su vez pueda exportar materias primas como algodón o lana. Los productores de "
            "materias primas en Genovia ven una posibilidad enorme de crecimiento; sin embargo, en el país hay "
            "gremios productores de bienes de cuero que están interesados en preservar su negocio que no podrían "
            "competir con los precios de los productos importados. En Genovia se ha hecho una propuesta para mediar "
            "esta situación: firmar el tratado y, al interior del país, otorgar subsidios para los productores "
            "nacionales. Esta propuesta de solución podría",
          o=["ayudar a los productores extranjeros a vender aún más barato.",
             "perjudicar a los compradores de productos de cuero.",
             "ajustarse a los intereses de los productores de bienes en cuero.",
             "incentivar la libre competencia entre los productores nacionales de bienes de cuero."],
          inst=ii3)
QD = dict(est=4, comp="Pensamiento social", f=F,
          e="Durante la Conquista de América, el «repartimiento» o «encomienda» consistió en el reparto de indígenas "
            "entre los conquistadores para su servicio personal, como recompensa avalada por la Corona por el éxito "
            "de sus campañas. Este sistema se convirtió en una vía segura para alcanzar la riqueza y la posición "
            "social que los conquistadores venían a buscar al Nuevo Mundo. Sin embargo, la Real Audiencia de Santa "
            "Fe de Bogotá, en 1557, estableció que «Cualquier indio que se asentase y se alquilare con cualquiera "
            "persona para le servir (…) que se le pague tres gramos de buen oro por jornal» y en 1560 prohibió el "
            "trabajo gratuito de los indígenas. Estas medidas de la Real Audiencia podrían obedecer al propósito de",
          o=["promover el ascenso social de los indígenas.",
             "disminuir el poder de los encomenderos.",
             "reconocer a los indígenas como iguales a los colonos.",
             "fortalecer a los encomenderos como administradores de los indígenas."],
          inst=ii4)


def build(pages=(127, 131)):
    return [hoja_icfes("soc5_i1", pages[0], QA, QB),
            hoja_icfes("soc5_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
