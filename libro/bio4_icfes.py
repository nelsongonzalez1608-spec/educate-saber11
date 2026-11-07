#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 4 · entrenamiento ICFES · páginas 163 y 167.

Las cuatro preguntas salen del cuadernillo oficial Saber 11 2016-1, 1.ª sesión, cuadernillo AAM
(encabezado «Saber 11 - 083 - B05R - AAM · 1a. sesión»), sección Ciencias Naturales, verificadas
contra la página escaneada en Drive («1. CUADERNILLOS ICFES» / «2016-1 PRIMERA SESION.pdf»,
páginas 30, 31 y 34). Los ítems 99 a 101 comparten el contexto del color del vino; el texto
completo está en tablero/propuestas/bio4_textos.md. Ninguna estaba en tablero/icfes.csv; las
cuatro se reservaron en tablero/propuestas/bio_icfes_reservas.csv. Ninguna nombra a un político.

Membrete: siempre «Pregunta oficial ICFES · Saber 11» (el motor lo impone).

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · N.º 99  · B   (pectinasas: qué gráfica espera el investigador)        estrategia 1
    QB · N.º 101 · A   (dos viñedos lejanos: mantener o cambiar la hipótesis)  estrategia 4
    QC · N.º 100 · C   (vino de manzana: el orden del proceso)                 estrategia 2
    QD · N.º 111 · D   (para qué le sirve la fotosíntesis a la planta)         estrategia 3

QA · la hipótesis compara dos vinos (con y sin pectinasa) en intensidad de color, sin hablar del
tiempo: la gráfica es de barras y la de «con pectinasa» va más alta → B. En A va más baja; C y D
ponen el tiempo en el eje x y en D la línea «sin pectinasa» queda por encima.
Las cuatro gráficas se redibujaron a partir del escaneo (la barra «con pectinasa» de la gráfica A
casi no se ve en la fotocopia): hallazgo registrado.
QC · la levadura tiene que estar antes de fermentar y las botellas lavadas antes de envasar:
prensado → levadura → fermentación → lavado de botellas → filtración y envasado → C. A agrega la
levadura al final; B no fermenta; D fermenta antes de agregar la levadura y no lava las botellas.
"""
from bio4 import *   # noqa: F401,F403  (configura la misión y EST)
from bio4 import rot, caja, pista, renglon, frase_hueco, letra


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 8, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


def cita(b, x, y, w, rotulo, texto, c, size=18):
    svg, yy = TJ(x + 26, y + 40, texto, w - 46, size, INK, lh=size + 8)
    h = yy - y + 12
    b.append(rect(x, y, w, h, SOFT, r=12))
    b.append(rect(x, y, 6, h, c, r=3))
    b.append(T(x + 26, y + 26, [rotulo], 14, GRAY, weight="700", ls=1.5))
    b.append(svg)
    return y + h


# ───────── QA · N.º 99 · pectinasas ─────────
def _mini(b, x, y, w, h, L, tipo, valores):
    """Una gráfica de opción. tipo: 'barras' (con, sin) o 'lineas' ([(t, con)], [(t, sin)])."""
    c = A["color"]
    letra(b, x + 16, y + 16, L, c)
    gx, gy, gw, gh = x + 70, y + 8, w - 300, h - 46
    b.append(line(gx, gy + gh, gx + gw, gy + gh, INK, 2))
    b.append(line(gx, gy, gx, gy + gh, INK, 2))
    b.append(T(gx - 10, gy + gh / 2, ["Intensidad del color"], 13, GRAY, anchor="middle", rot=-90))
    if tipo == "barras":
        b.append(T(gx + gw / 2, gy + gh + 22, ["Tipo de vino producido"], 13, GRAY, anchor="middle"))
        con, sin = valores
        bw = 46
        b.append(rect(gx + gw * 0.25, gy + gh - con * gh, bw, con * gh, "white", r=0, stroke=INK, sw=1.8,
                      dash="5,4"))
        b.append(rect(gx + gw * 0.62, gy + gh - sin * gh, bw, sin * gh, "#B9BEC8", r=0, stroke=INK, sw=1.8))
        lx = gx + gw + 26
        b.append(rect(lx, gy + 10, 22, 18, "white", r=0, stroke=INK, sw=1.6, dash="4,3"))
        b.append(T(lx + 32, gy + 24, ["con pectinasa"], 14, INK))
        b.append(rect(lx, gy + 42, 22, 18, "#B9BEC8", r=0, stroke=INK, sw=1.6))
        b.append(T(lx + 32, gy + 56, ["sin pectinasa"], 14, INK))
    else:
        b.append(T(gx + gw / 2, gy + gh + 22, ["Tiempo (días)"], 13, GRAY, anchor="middle"))
        con, sin = valores
        P = lambda t, v: f"{gx + t * gw:.0f} {gy + gh - v * gh:.0f}"
        b.append(f'<path d="M {" L ".join(P(t, v) for t, v in con)}" fill="none" stroke="{INK}" '
                 f'stroke-width="2.6"/>')
        b.append(f'<path d="M {" L ".join(P(t, v) for t, v in sin)}" fill="none" stroke="{INK}" '
                 f'stroke-width="2.6" stroke-dasharray="9,6"/>')
        lx = gx + gw + 26
        b.append(line(lx, gy + 19, lx + 26, gy + 19, INK, 2.6))
        b.append(T(lx + 36, gy + 24, ["con pectinasa"], 14, INK))
        b.append(line(lx, gy + 51, lx + 26, gy + 51, INK, 2.6, dash="7,5"))
        b.append(T(lx + 36, gy + 56, ["sin pectinasa"], 14, INK))


PREG_99 = ("Al leer la información del contexto, un investigador piensa que si se emplean pectinasas durante la "
           "producción de vino de uva, la intensidad del color de un vino es mayor que la de un vino producido sin "
           "pectinasas. Si la hipótesis del investigador es cierta, ¿cuál de las siguientes gráficas muestra los "
           "resultados esperados por el investigador?")


def datos_99(b, x, y, w):
    yy = y
    gw, gh = (w - 30) / 2, 132
    graf = (("A", "barras", (0.42, 0.62)), ("B", "barras", (0.88, 0.52)),
            ("C", "lineas", ([(0, 0.6), (0.5, 0.6), (0.5, 0.0)], [(0, 0.64), (0.5, 0.64), (0.85, 0.3)])),
            ("D", "lineas", ([(0, 0.15), (0.85, 0.5)], [(0, 0.42), (0.85, 0.78)])))
    for k, (L, tipo, val) in enumerate(graf):
        _mini(b, x + (k % 2) * (gw + 30), yy + 10 + (k // 2) * (gh + 10), gw, gh, L, tipo, val)
    return yy + 10 + 2 * (gh + 10)


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Diccionario de la hipótesis a la gráfica", c,
                      "Lo del banco de pruebas: una hipótesis dice qué se compara y qué se mide. Traduce cada pedazo "
                      "de la hipótesis a lo que tendría que verse en la gráfica. Solo después mira las cuatro.")
    x0, ww = x + 22, w - 44
    filas = (("«con pectinasas» y «sin pectinasas»", "¿qué son en la gráfica: dos barras, dos líneas, un eje?"),
             ("«la intensidad del color»", "¿en qué eje va?"),
             ("«es mayor que»", "¿qué se tiene que ver, y de cuál de las dos?"),
             ("¿la hipótesis dice algo del tiempo?", "entonces, ¿qué va en el eje horizontal?"))
    lw = 400
    for k, (dice, ps) in enumerate(filas):
        ry = yy + k * 84
        caja(b, x0, ry, lw, 72, c, r=36, fill=A["bg"])
        b.append(T(x0 + 24, ry + 43, [dice], 17, INK, style="italic"))
        b.append(hand_arrow(x0 + lw + 8, ry + 36, x0 + lw + 58, ry + 36, c, sw=2.4, bend=0.0, head=10))
        bx = x0 + lw + 70
        caja(b, bx, ry, ww - lw - 70, 72, c, r=10)
        pista(b, bx + 16, ry + 22, ps, size=14)
        renglon(b, bx + 16, ry + 62, x0 + ww - 16)
    return yy + 4 * 84


# ───────── QB · N.º 101 · dos viñedos ─────────
def ii2(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "La hipótesis frente a los estudios", c,
                      "Lo de la prótesis y las vacunas: una idea vale lo que la evidencia la respalde. Pon frente a "
                      "frente lo que supone el comerciante y lo que encontró en los estudios.")
    x0, ww = x + 22, w - 44
    half = (ww - 90) / 2
    for k, (rt, ps) in enumerate((("LO QUE SUPONE EL COMERCIANTE", "y por qué lo supone"),
                                  ("LO QUE DICEN LOS ESTUDIOS", "¿de qué depende cuántos pigmentos hay?"))):
        px = x0 + k * (half + 90)
        caja(b, px, yy, half, 132, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        pista(b, px + 18, yy + 52, ps)
        renglon(b, px + 18, yy + 88, px + half - 18)
        renglon(b, px + 18, yy + 118, px + half - 18)
    mx = x0 + half + 45
    b.append(T(mx, yy + 60, ["¿cuadran?"], 15, c, weight="700", anchor="middle"))
    for j, lab in enumerate(("sí", "no")):
        b.append(checkbox(mx - 40 + j * 50, yy + 76, s=10, c=c))
        b.append(T(mx - 30 + j * 50, yy + 122, [lab], 14, GRAY, anchor="middle"))
    yy += 150
    caja(b, x0, yy, ww, 90, c, r=14)
    rot(b, x0 + 18, yy + 28, "ENTRE DOS MUNICIPIOS LEJANOS PUEDE SER DISTINTO…", c, size=14)
    for k in range(3):
        b.append(T(x0 + 18 + k * (ww / 3), yy + 70, [f"{k + 1}."], 16, INK, weight="700"))
        renglon(b, x0 + 40 + k * (ww / 3), yy + 72, x0 + (k + 1) * (ww / 3) - 24)
    return yy + 104


# ───────── QC · N.º 100 · vino de manzana ─────────
ETAPAS = "selección de la fruta, prensado, fermentación-añejamiento, filtración y envasado"


def datos_100(b, x, y, w):
    yy = pregunta(b, x, y, w, "Si un investigador cuenta con los siguientes elementos para preparar una bebida "
                                   "alcohólica a base de manzana, ¿cuál es el modelo que indicaría correctamente un "
                                   "proceso de producción que le permitiría comercializar el vino de manzana "
                                   "empleando todos estos elementos?")
    els = ("manzana", "prensa", "colador", "levadura", "botella sin desinfectar")
    px = x
    for e in els:
        ew = tw(e, 17) + 34
        b.append(rect(px, yy + 6, ew, 36, "white", r=18, stroke=GRAY, sw=1.6))
        b.append(T(px + ew / 2, yy + 30, [e], 17, INK, anchor="middle"))
        px += ew + 14
    return yy + 46


def ii3(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Las tarjetas del proceso, en orden", c,
                      "Lo de la toxina y la vacuna: cada eslabón necesita que el anterior ya haya pasado. Escribe las "
                      "etapas en las tarjetas que necesites, en el orden en que tienen que ocurrir. Puede sobrar "
                      "alguna tarjeta.")
    x0, ww = x + 22, w - 44
    n, gap = 6, 26
    cw_ = (ww - (n - 1) * gap) / n
    for k in range(n):
        px = x0 + k * (cw_ + gap)
        caja(b, px, yy, cw_, 96, c, sw=2.2, r=12)
        letra(b, px + 22, yy + 24, str(k + 1), c, r=14, size=14)
        renglon(b, px + 14, yy + 66, px + cw_ - 14)
        if k < n - 1:
            b.append(hand_arrow(px + cw_ + 4, yy + 48, px + cw_ + gap - 4, yy + 48, c, sw=2.4, bend=0.0, head=10))
    yy += 112
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("PARA FERMENTAR HACE FALTA ANTES…", "¿quién convierte el azúcar en etanol?"),
                                  ("PARA ENVASAR HACE FALTA ANTES…", "¿cómo tiene que estar la botella?"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 88, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=13)
        pista(b, px + 18, yy + 50, ps)
        renglon(b, px + 18, yy + 76, px + half - 18)
    return yy + 100


# ───────── QD · N.º 111 · fotosíntesis ─────────
def ii4(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "La fábrica de la hoja: entra, sale, para qué", c,
                      "Lo de las bacterias y los envases: cada pieza hace algo. Escribe qué entra a la hoja, qué sale "
                      "de ella y, lo más importante, para qué usa la planta lo que fabrica.")
    x0, ww = x + 22, w - 44
    cx, cy = x0 + ww / 2 - 120, yy + 120
    b.append(f'<path d="M {cx - 150} {cy} Q {cx} {cy - 110} {cx + 150} {cy} Q {cx} {cy + 110} {cx - 150} {cy} Z" '
             f'fill="{A["bg"]}" stroke="{VERDE}" stroke-width="3"/>')
    b.append(line(cx - 150, cy, cx + 150, cy, VERDE, 2.4))
    rot(b, cx, cy - 16, "LA HOJA", VERDE, size=14, anchor="middle")
    for k in range(3):
        ey = cy - 70 + k * 70
        b.append(rect(x0, ey - 22, 190, 44, "white", r=8, stroke=c, sw=2, dash="5,5"))
        b.append(hand_arrow(x0 + 196, ey, cx - 140, cy + (k - 1) * 30, c, sw=2.4, bend=0.0, head=11))
    pista(b, x0, cy + 110, "lo que entra", size=14)
    for k in range(2):
        ey = cy - 40 + k * 80
        bx = cx + 300
        b.append(hand_arrow(cx + 152, cy + (k - 0.5) * 30, bx - 6, ey, c, sw=2.4, bend=0.0, head=11))
        b.append(rect(bx, ey - 22, 190, 44, "white", r=8, stroke=c, sw=2, dash="5,5"))
    pista(b, cx + 300, cy + 110, "lo que sale", size=14)
    yy = cy + 132
    return frase_hueco(b, x0, yy, ww, "La planta usa lo que fabrica para ______________________________ .", c)



QA = dict(est=1, comp="Indagación", e=PREG_99, o=[], datos=datos_99, inst=ii1)
QB = dict(est=4, comp="Indagación",
          e="Un comerciante compra dos viñedos en dos municipios lejanos entre sí, y tiene la hipótesis de que los "
            "vinos fabricados en estos dos municipios distantes van a tener la misma cantidad de pigmentos, porque se "
            "elaborarán con un mismo tipo de uva. Al buscar información, el comerciante encuentra que existen "
            "estudios en los que el número de pigmentos que producen los frutos de una misma planta varían, de "
            "acuerdo con la cantidad de agua con la que se riegan las plantas mientras se desarrollan. De acuerdo con "
            "lo anterior, ¿qué debería hacer el comerciante con su hipótesis?",
          o=["Cambiarla, porque condiciones ambientales como la cantidad de agua en el suelo, de luz o temperatura "
             "deben variar entre los municipios, lo cual produce que la cantidad de pigmentos generados en las uvas "
             "sea distinto.",
             "Mantenerla, porque la cantidad de pigmentos responsables del color depende únicamente de que el número "
             "de etapas y el tipo de fruta para la elaboración del vino sea el mismo, lo cual produce que la cantidad "
             "de pigmentos sea igual.",
             "Cambiarla, porque las uvas posiblemente no desarrollarán pigmentos si no se cultivan en un mismo viñedo.",
             "Mantenerla, porque todos los vinos deben tener una cantidad similar de pigmentos, siempre y cuando "
             "pasen por la etapa de fermentación."],
          inst=ii2)
QC = dict(est=2, comp="Uso comprensivo del conocimiento científico",
          e="Del contexto que comparte con otras preguntas: «En general, para comercializar cualquier vino "
            f"actualmente, el proceso debe cumplir las siguientes etapas: {ETAPAS}. La última etapa debe realizarse "
            "en recipientes lavados y desinfectados previamente».",
          o=["Prensado de manzanas → fermentación y añejamiento (azúcar → etanol + dióxido de carbono) → filtración "
             "y envasado → lavado y desinfección de botellas → adición de levadura.",
             "Prensado de manzanas → filtración y envasado → adición de levadura → lavado y desinfección de "
             "botellas.",
             "Prensado de manzanas → adición de levadura → fermentación y añejamiento (azúcar → etanol + dióxido de "
             "carbono) → lavado y desinfección de botellas → filtración y envasado.",
             "Prensado de manzanas → fermentación y añejamiento (azúcar → etanol + dióxido de carbono) → adición de "
             "levadura → filtración y envasado."],
          datos=datos_100, inst=ii3)
QD = dict(est=3, comp="Uso comprensivo del conocimiento científico",
          e="La fotosíntesis se lleva a cabo en los cloroplastos de las células vegetales y consiste en la "
            "transformación de la energía proveniente de la luz en azúcares. La fotosíntesis es importante para las "
            "plantas porque",
          o=["aporta sales al ecosistema.",
             "aporta cloroplastos nuevos a las células vegetales.",
             "elimina el exceso de agua almacenada en los ecosistemas.",
             "produce los nutrientes necesarios para su desarrollo y crecimiento."],
          inst=ii4)


def build(pages=(163, 167)):
    return [hoja_icfes("bio4_i1", pages[0], QA, QB),
            hoja_icfes("bio4_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
