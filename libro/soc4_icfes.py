#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sociales y Ciudadanas · Misión 4 · entrenamiento ICFES · páginas 120 y 124.

Las cuatro preguntas salen del cuadernillo oficial Saber 11 2016-1, primera sesión
(cuadernillo AAM, código «Saber 11 - 116 - B05R - AAM»), sección Sociales y Ciudadanas,
segunda mitad. Año, sesión y número verificados contra la portada y la página del
cuadernillo escaneado en Drive («1. CUADERNILLOS ICFES» / «2016-1 PRIMERA SESION.pdf»).
El ítem 85 de la misma página se descartó: nombra a un político colombiano vivo.

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · N.º 87 · C      (desplazados y adaptación a la ciudad)        estrategia 3
    QB · N.º 89 · A      (Canción de los dinosaurios y la dictadura)  estrategia 1
    QC · N.º 83 · A      (autopista en la ciénaga · los opositores)   estrategia 2
    QD · N.º 81 · D      (origen de las guerrillas en los años 60)    estrategia 4
"""
from soc4 import *   # noqa: F401,F403  (configura la misión y EST)


def membrete_2016(n):
    """Verificada contra el cuadernillo 2016-1 (ítem n), pero el membrete es genérico por
    decisión de Nelson (6 nov). El dato queda en tablero/icfes.csv, columna fuente."""
    return "Pregunta oficial ICFES · Saber 11"


# ───────── QA · N.º 87 ─────────
def ii1(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Lo que sabía hacer en el campo, ¿sirve en la ciudad?", c,
                      "La ley dice por qué se van. La pregunta pide otra cosa: por qué les cuesta llegar. "
                      "Escribe dos saberes de la vida en la vereda y lo que la ciudad pide a cambio.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, rt in enumerate(("LO QUE SE APRENDE PARA VIVIR EN LA VEREDA", "LO QUE PIDE LA CIUDAD")):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 110, c)
        rot(b, bx + 20, yy + 30, rt, c)
        for i in range(2):
            b.append(line(bx + 20, yy + 62 + i * 32, bx + half - 20, yy + 62 + i * 32, LGRAY, 2))
    yy += 126
    return trampa(b, x0, yy, ww, "Te piden deducir, no suponer:",
                  "pregúntate de cada opción si sale de la definición de la ley o si es un dato sobre la ciudad que "
                  "la ley nunca da. Una afirmación puede sonar razonable y aun así no poder deducirse.", c)


def datos_87(b, x, y, w):
    yy = evidencia(b, x, y, w, "LEY 387 DE 1997",
                   "«Es desplazado toda persona que se ha visto forzada a migrar dentro del territorio nacional "
                   "abandonando su localidad de residencia o actividades económicas habituales, porque su vida, su "
                   "integridad física, su seguridad o libertad personales han sido vulneradas o se encuentran "
                   "directamente amenazadas».", EST[3][1])
    svg, y2 = TJ(x, yy + 6, "A partir de esta definición, puede deducirse que la población desplazada de las "
                 "zonas rurales tendría problemas para adaptarse a la vida urbana, porque", w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QB · N.º 89 ─────────
LETRA = ("Los amigos del barrio pueden desaparecer", "Los cantores de radio pueden desaparecer",
         "Los que están en los diarios pueden desaparecer", "La persona que amas puede desaparecer.",
         "Los que están en el aire pueden desaparecer, en el aire.",
         "Los que están en la calle pueden desaparecer, en la calle.",
         "Los amigos del barrio pueden desaparecer,", "Pero los dinosaurios van a desaparecer")


def datos_89(b, x, y, w):
    c = EST[1][1]
    hh = 4 * 26 + 50
    b.append(rect(x, y, w, hh, SOFT, r=10))
    b.append(rect(x, y, 8, hh, c, r=4))
    rot(b, x + 34, y + 24, "CANCIÓN DE LOS DINOSAURIOS · CHARLIE GARCÍA · 1985", c, size=13)
    for k, v in enumerate(LETRA):
        col, fila = divmod(k, 4)
        txt = ("“" if k == 0 else "") + v + ("”" if k == 7 else "")
        b.append(T(x + 34 + col * (w / 2), y + 54 + fila * 26, [txt], 16, INK, style="italic"))
    yy = y + hh + 8
    b.append(T(x, yy + 22, ["Puede afirmarse que la letra de esta canción"], 20, INK))
    return yy + 30


def ii2(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Pon la canción en su año y en su país", c,
                      "Una canción también es un documento de su época. Ubícala antes de juzgarla.")
    x0, ww = x + 22, w - 44
    for k, (rt, ps) in enumerate((("1985 · ARGENTINA", "¿qué gobierno acababa de terminar?"),
                                  ("LO QUE DESAPARECE EN LA LETRA", "¿personas o cosas? ¿cuántas veces?"))):
        bx = x0 + k * ((ww - 30) / 2 + 30)
        bw = (ww - 30) / 2
        caja(b, bx, yy, bw, 82, c)
        rot(b, bx + 20, yy + 28, rt, c)
        pista(b, bx + 20, yy + 52, ps)
        b.append(line(bx + 20, yy + 70, bx + bw - 20, yy + 70, LGRAY, 2))
    yy += 98
    return alto_profe(b, x0, yy, ww,
                      "La dictadura militar argentina (1976-1983) y los desaparecidos. Sin ese dato la canción parece "
                      "una lista; con él, cada verso dice algo. Fíjate también qué razón da cada opción, no solo si "
                      "dice «sí tiene relación».")


# ───────── QC · N.º 83 ─────────
CASO_83 = ("Con el propósito de fortalecer la economía nacional se discuten diferentes alternativas que "
           "faciliten la comunicación por tierra con los grandes puertos comerciales del norte del país. Con este "
           "fin, se consideró el transporte por el río Magdalena, la reorganización del sistema ferroviario y "
           "finalmente se decidió la construcción de una autopista a través de terrenos de ciénaga. El proyecto "
           "necesita una gran inversión para la infraestructura de la autopista, para la reubicación de los "
           "habitantes de los terrenos y para el dragado de grandes extensiones de la ciénaga. A pesar de los "
           "beneficios de esta propuesta, los opositores señalan que esta generaría problemas irreparables.")


def datos_83(b, x, y, w):
    b.append(T(x, y + 24, ["¿Cuál de las siguientes opciones podría apoyar mejor la posición de los opositores?"],
               20, INK))
    return y + 32


def ii3(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Ponte del lado de los opositores y busca su mejor argumento", c,
                      "El mejor argumento sale de lo que el proyecto hace, no de lo que uno sospecha que podría pasar.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 520, 86, c)
    pista(b, x0 + 18, yy + 28, "lo que el proyecto hace, según el texto:")
    b.append(line(x0 + 18, yy + 70, x0 + 502, yy + 70, LGRAY, 2))
    b.append(hand_arrow(x0 + 530, yy + 43, x0 + 600, yy + 43, c, sw=3, bend=0.0, head=14))
    caja(b, x0 + 610, yy, ww - 610, 86, c)
    pista(b, x0 + 628, yy + 28, "el daño irreparable que eso causaría:")
    b.append(line(x0 + 628, yy + 70, x0 + ww - 18, yy + 70, LGRAY, 2))
    yy += 104
    for k, L in enumerate("ABCD"):
        bx = x0 + k * (ww / 4)
        b.append(f'<circle cx="{bx + 20}" cy="{yy + 20}" r="17" fill="white" stroke="{c}" stroke-width="2"/>')
        b.append(T(bx + 20, yy + 27, [L], 16, c, weight="700", anchor="middle"))
        for j, lab in enumerate(("sale del texto", "es sospecha")):
            b.append(checkbox(bx + 52, yy + 2 + j * 30, s=10, c=c))
            b.append(T(bx + 80, yy + 18 + j * 30, [lab], 15, GRAY))
    return yy + 64


# ───────── QD · N.º 81 ─────────
FACT = ("1. el auge del negocio del narcotráfico en el sur del país.",
        "2. la difusión de las ideas que orientaron la Revolución cubana.",
        "3. el asesinato de integrantes de la Unión Patriótica.",
        "4. los problemas de distribución de la tierra en el sector rural.")


def datos_81(b, x, y, w):
    c = EST[4][1]
    hh = 2 * 28 + 30
    b.append(rect(x, y, w, hh, SOFT, r=10))
    b.append(rect(x, y, 8, hh, c, r=4))
    for k, f in enumerate(FACT):
        col, fila = divmod(k, 2)
        b.append(T(x + 30 + col * (w / 2), y + 36 + fila * 30, [f], 16, INK))
    return y + hh


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Ordena en el tiempo: qué ya existía en los años 60", c,
                      "Una causa tiene que estar antes que su efecto. Escribe el número de cada factor en la década "
                      "en que lo ubicas; lo que llegó después no pudo hacer nacer a las guerrillas.")
    x0, ww = x + 22, w - 44
    dec = ("1940", "1950", "1960", "1970", "1980", "1990")
    sw_ = ww / len(dec)
    ly = yy + 30
    b.append(line(x0 + 10, ly, x0 + ww - 10, ly, c, 4))
    for k, d in enumerate(dec):
        cx = x0 + sw_ * k + sw_ / 2
        b.append(f'<circle cx="{cx}" cy="{ly}" r="10" fill="white" stroke="{c}" stroke-width="3"/>')
        b.append(T(cx, ly - 18, [f"años {d[2:]}" if d != "1990" else "años 90"], 15, c, weight="700",
                   anchor="middle"))
        caja(b, cx - sw_ / 2 + 12, ly + 22, sw_ - 24, 60, c)
    b.append(T(x0 + sw_ * 2 + sw_ / 2, ly + 108, ["aquí nacen las guerrillas"], 15, GRAY,
               style="italic", anchor="middle"))
    return ly + 118


QA = dict(est=3, comp="Pensamiento social", f=membrete_2016(87),
          e="En la Ley 387 de 1997, donde se establecen disposiciones para prevenir el desplazamiento forzado, "
            "se indica:",
          o=["las jornadas de trabajo en la ciudad son más exigentes físicamente que las jornadas laborales en "
             "zonas rurales.",
             "la disponibilidad de alimentos es mucho menor en las zonas urbanas que en zonas rurales.",
             "los saberes culturales útiles para vivir en zonas rurales no son los mismos que se requieren para "
             "vivir en zonas urbanas.",
             "la seguridad en las zonas urbanas es más difícil de garantizar que en las zonas rurales."],
          datos=datos_87, inst=ii1)
QB = dict(est=1, comp="Pensamiento reflexivo y sistémico", f=membrete_2016(89),
          e="La siguiente es una estrofa de la Canción de los dinosaurios, compuesta e interpretada por el músico "
            "argentino Charlie García en 1985:",
          o=["tiene relación con la dictadura argentina, en tanto describe la persecución social y política "
             "característica de los regímenes dictatoriales.",
             "no tiene relación con la dictadura argentina, dado que el arte y la política son ámbitos "
             "independientes de la vida social.",
             "tiene relación con la época de la dictadura argentina, porque Charlie García tiene esa nacionalidad.",
             "no tiene relación con la dictadura, en tanto en este tipo de gobierno se respetan los derechos "
             "civiles y políticos."],
          datos=datos_89, inst=ii2)
QC = dict(est=2, comp="Interpretación de perspectivas", f=membrete_2016(83),
          e=CASO_83,
          o=["El proyecto perjudica el ecosistema de la región de la ciénaga así como las formas de vida de las "
             "comunidades de la zona.",
             "La construcción de la autopista inevitablemente será usada por políticos y contratistas corruptos "
             "para robar dinero del país.",
             "La autopista facilitará el transporte de mercancía de contrabando generando un impacto negativo en "
             "la economía del país.",
             "El tráfico de la autopista hará más insegura la región con accidentes de tránsito y robos a "
             "vehículos privados y/o comerciales."],
          datos=datos_83, inst=ii3)
QD = dict(est=4, comp="Pensamiento reflexivo y sistémico", f=membrete_2016(81),
          e="De los siguientes factores, ¿cuáles se relacionan, de manera directa, con el surgimiento de movimientos "
            "guerrilleros en Colombia en la década de los años 1960?",
          o=["2 y 3.", "1 y 4.", "1 y 3.", "2 y 4."],
          datos=datos_81, inst=ii4)


def build(pages=(120, 124)):
    return [hoja_icfes("soc4_i1", pages[0], QA, QB),
            hoja_icfes("soc4_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
