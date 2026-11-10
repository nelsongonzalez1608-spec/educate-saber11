#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 3 · entrenamiento ICFES · páginas 199 y 203.

Las cuatro preguntas salen de los cuadernillos oficiales Saber 11 2016-1 que están en Drive
(carpeta «1. CUADERNILLOS ICFES»), sección Ciencias Naturales, verificadas contra la página
escaneada:
  · «2016-1 PRIMERA SESION.pdf» — 1.ª sesión, cuadernillo AAM (encabezado «Saber 11 - 083 -
    B05R - AAM · 1a. sesión»), ítems 91 (p. 28), 95 (p. 29) y 113 (p. 34).
  · «2016-2 SEGUNDA SESION.pdf» — en la portada dice 2016-1, 2.ª sesión, cuadernillo ABD
    (encabezado «Saber 11 - 083 - B10O - ABD · 2a. sesión»), ítem 65 (p. 21).
Ninguna estaba en tablero/icfes.csv; las cuatro se reservaron en
tablero/propuestas/qui_icfes_reservas.csv. Ninguna nombra a un político. La tabla del ítem 91,
la del 65, la gráfica del 95 y las cuatro gráficas de barras del 113 se redibujaron con los
mismos datos.

Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11» (el motor lo impone).

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · 1.ª ses. N.º 91  · B   (X + W → Z: experimento 3 o 6)               estrategia 1
    QB · 2.ª ses. N.º 65  · B   (qué pH tiene una sustancia neutra)           estrategia 2
    QC · 1.ª ses. N.º 95  · C   (gas a presión constante: doble temperatura)  estrategia 3
    QD · 1.ª ses. N.º 113 · D   (mezcla 2 con menor pH: qué gráfica)          estrategia 4

Cuentas:
  QA · Con X: 10 → 20 M duplica la velocidad (100 → 200) y 10 → 40 la cuadruplica (400): la
       velocidad va en proporción a [X]; experimento 3 (X = 30) → 300 M/s. Con W: 10 → 20
       multiplica por 4 (400) y 10 → 40 por 16 (1600): va con [W]²; experimento 6 (W = 30) →
       100 × 3² = 900 M/s. 900 > 300 → experimento 6, porque W mueve más la velocidad → B.
       C dice «únicamente cuando se varía W» (falso: X también la cambia).
  QB · En la tabla los «neutros» tienen pH 6,8 (leche), 7,0 (agua) y 7,2 (gel) → B. A y C dejan
       por fuera dos de los tres; D mete al jabón (9,0, básico).
  QC · Los puntos (100 K, 100 mL), (250 K, 250 mL), (400 K, 400 mL), (500 K, 500 mL) están sobre
       una recta que pasa por el origen: V/T = 1 mL/K. Doble T → doble V → C.
  QD · Menor pH en la mezcla 2: la barra de la mezcla 2 más baja que la de la mezcla 1. Solo D
       (6 y 3). A la pone más alta; B iguales; C deja la mezcla 1 sin barra.
"""
from qui3 import *   # noqa: F401,F403  (configura la misión y EST)
from qui3 import rot, caja, pista, renglon, frase_hueco, letra, casillas


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 8, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


def celda(b, x, y, w, h, txt, bold=False, fill="white", size=15):
    caja(b, x, y, w, h, GRAY, sw=1.4, r=0, fill=fill)
    lines = txt.split("\n")
    y0 = y + h / 2 - (len(lines) - 1) * (size + 3) / 2 + size * 0.35
    for k, ln in enumerate(lines):
        b.append(T(x + w / 2, y0 + k * (size + 3), [ln], size, INK, weight="700" if bold else "400",
                   anchor="middle"))


def caja_num(b, x, y, c, w=90, h=38):
    caja(b, x, y, w, h, c, r=8)
    return x + w


# ───────── QA · N.º 91 · velocidad de reacción ─────────
FILAS_91 = (("1", "10", "10", "100"), ("2", "20", "10", "200"), ("3", "30", "10", "?"), ("4", "40", "10", "400"),
            ("5", "10", "20", "400"), ("6", "10", "30", "?"), ("7", "10", "40", "1600"))


def datos_91(b, x, y, w):
    cols = (230, 140, 220, 220, 250)
    heads = ("", "Experimento", "Concentración\nde X (M)", "Concentración\nde W (M)", "Velocidad de\nreacción (M/s)")
    x0 = x + (w - sum(cols)) / 2
    yy = y + 4
    px = x0
    for cw, t in zip(cols, heads):
        if t:
            celda(b, px, yy, cw, 44, t, bold=True, fill=SOFT, size=14)
        px += cw
    yy += 44
    rh = 26
    grupos = (("Condiciones iniciales", 1), ("Modificando la\nconcentración de X", 3),
              ("Modificando la\nconcentración de W", 3))
    k = 0
    for g, n in grupos:
        celda(b, x0, yy, cols[0], rh * n, g, size=14)
        for j in range(n):
            px = x0 + cols[0]
            for cw, v in zip(cols[1:], FILAS_91[k]):
                celda(b, px, yy + j * rh, cw, rh, v, size=14)
                px += cw
            k += 1
        yy += rh * n
    return pregunta(b, x, yy + 4, w, "Teniendo en cuenta la información anterior y las tendencias observadas, al "
                                     "comparar los experimentos 3 y 6, ¿en cuál de los dos se obtendrá una mayor "
                                     "velocidad de reacción?")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Si duplico X… si duplico W…", c,
                      "Lo de los tres vasos: cambia una sola cosa a la vez. La tabla ya lo hizo; tú lee qué le pasa a "
                      "la velocidad cuando solo cambia X y cuando solo cambia W, y con eso predice los dos «?».")
    x0, ww = x + 22, w - 44
    for k, (r_, a, bb) in enumerate((("SOLO CAMBIA X", "de 10 a 20 (× 2): la velocidad queda ×", "de 10 a 40 (× 4): ×"),
                                     ("SOLO CAMBIA W", "de 10 a 20 (× 2): la velocidad queda ×", "de 10 a 40 (× 4): ×"))):
        ry = yy + k * 52
        rot(b, x0, ry + 26, r_, c, size=14)
        b.append(T(x0 + 170, ry + 26, [a], 16, INK))
        xa = x0 + 170 + tw(a, 16) + 10
        caja_num(b, xa, ry, c, w=70)
        b.append(T(xa + 110, ry + 26, [bb], 16, INK))
        caja_num(b, xa + 110 + tw(bb, 16) + 10, ry, c, w=70)
    yy += 110
    return frase_hueco(b, x0, yy, ww, "Predigo: experimento 3 ≈ ________ M/s · experimento 6 ≈ ________ M/s .", c)


# ───────── QB · N.º 65 · pH de una sustancia neutra ─────────
FILAS_65 = (("Leche", "6,8", "Neutro"), ("Jugo de naranja", "3,5", "Ácido"), ("Jabón", "9,0", "Básico"),
            ("Agua", "7,0", "Neutro"), ("Crema de dientes", "10,5", "Básico"), ("Café", "5,0", "Ácido"),
            ("Gel para el cabello", "7,2", "Neutro"))


def datos_65(b, x, y, w):
    cols = (300, 120, 200)
    x0 = x + 30
    yy = y + 4
    px = x0
    for cw, t in zip(cols, ("Sustancia", "pH", "Carácter")):
        celda(b, px, yy, cw, 30, t, bold=True, fill=SOFT)
        px += cw
    yy += 30
    for f in FILAS_65:
        px = x0
        for cw, v in zip(cols, f):
            celda(b, px, yy, cw, 28, v)
            px += cw
        yy += 28
    return pregunta(b, x, yy + 4, w, "De acuerdo con la información anterior, una sustancia neutra es aquella que "
                                     "presenta un pH")


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Siete sustancias en la regla del pH", c,
                      "Lo del charco: clasifica con lo que se ve, aquí con los datos. Escribe la inicial de cada "
                      "sustancia en su lugar de la regla y encierra con una llave las que la tabla llama «neutro».")
    x0, ww = x + 22, w - 44
    ly = yy + 56
    L, R = x0 + 30, x0 + ww - 30
    b.append(line(L, ly, R, ly, INK, 2.6))
    for v in range(0, 15):
        px = L + v / 14 * (R - L)
        b.append(line(px, ly - 9, px, ly + 9, INK, 2))
        b.append(T(px, ly + 32, [str(v)], 15, GRAY, anchor="middle"))
        if v < 14:
            b.append(line(px + (R - L) / 28, ly - 5, px + (R - L) / 28, ly + 5, INK, 1.4))
    pista(b, L, ly - 40, "← más ácido")
    pista(b, R, ly - 40, "→ más básico", anchor="end")
    yy = ly + 44
    yy = frase_hueco(b, x0, yy, ww, "Según ESTA tabla, lo neutro va desde pH ______ hasta pH ______ .", c)
    return ojo(b, x0, yy + 14, ww, "OJO CON LA PALABRA «NEUTRO»",
               "en química, neutro es exactamente pH 7 (a 25 °C); esta tabla llama «neutro» a lo que queda cerca. "
               "La pregunta pide lo que dice la tabla.")


# ───────── QC · N.º 95 · gas a presión constante ─────────
def datos_95(b, x, y, w):
    gx, gy, gw, gh = x + 120, y + 20, 520, 220
    for v in range(0, 501, 100):
        py = gy + gh - v / 500 * gh
        b.append(line(gx, py, gx + gw, py, LGRAY, 1.4, dash="4,6"))
        b.append(T(gx - 12, py + 5, [str(v)], 14, INK, anchor="end"))
    for t in range(0, 601, 100):
        px = gx + t / 600 * gw
        if t:
            b.append(line(px, gy, px, gy + gh, LGRAY, 1.4, dash="4,6"))
        b.append(T(px, gy + gh + 24, [str(t)], 14, INK, anchor="middle"))
    b.append(line(gx, gy + gh, gx + gw + 14, gy + gh, INK, 2.2))
    b.append(line(gx, gy - 10, gx, gy + gh, INK, 2.2))
    for t, v in ((100, 100), (250, 250), (400, 400), (500, 500)):
        b.append(f'<circle cx="{gx + t / 600 * gw:.1f}" cy="{gy + gh - v / 500 * gh:.1f}" r="8" fill="white" '
                 f'stroke="{INK}" stroke-width="2.4"/>')
    b.append(T(gx + gw / 2, gy + gh + 50, ["Temperatura (K)"], 15, INK, weight="700", anchor="middle"))
    b.append(T(gx - 64, gy + gh / 2, ["Volumen (mL)"], 15, INK, weight="700", anchor="middle", rot=-90))
    return pregunta(b, x, gy + gh + 62, w, "A partir de la información anterior, ¿qué sucederá con el volumen del gas "
                                           "si la temperatura aumenta al doble de la inicial, sin que se produzca un "
                                           "cambio de presión?")


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Escoge un punto y dobla su temperatura", c,
                      "Lo de la llanta y el sifón: sigue al gas. Escoge cualquier punto de la gráfica, dobla su "
                      "temperatura y lee el nuevo volumen. Si te da tiempo, hazlo con un segundo punto para "
                      "comprobar.")
    x0, ww = x + 22, w - 44
    pasos = ("Punto escogido:  T =", "K ·  V =", "mL   →   T doble =", "K ·  V leído =", "mL")
    for k in range(2):
        ry = yy + k * 56
        px = x0
        rot(b, px, ry + 26, f"PUNTO {k + 1}", c, size=14)
        px += 100
        for j, p in enumerate(pasos):
            b.append(T(px, ry + 26, [p], 16, INK))
            px += tw(p, 16) + 10
            if j < 4:
                px = caja_num(b, px, ry, c, w=78) + 10
    yy += 120
    return frase_hueco(b, x0, yy, ww, "V nuevo ÷ V inicial = ______ ; cuando la temperatura se dobla, el volumen "
                                      "______________ .", c)


# ───────── QD · N.º 113 · la mezcla con menor pH ─────────
def _barras(b, x, y, w, h, L, v1, v2, c):
    letra(b, x + 16, y + 16, L, c)
    gx, gy, gw, gh = x + 90, y + 6, w - 120, h - 36
    for v in range(0, 11, 2):
        py = gy + gh - v / 10 * gh
        b.append(line(gx, py, gx + gw, py, LGRAY, 1.2, dash="3,5"))
        b.append(T(gx - 8, py + 5, [str(v)], 13, INK, anchor="end"))
    b.append(line(gx, gy + gh, gx + gw, gy + gh, INK, 2))
    b.append(line(gx, gy - 4, gx, gy + gh, INK, 2))
    b.append(T(gx - 40, gy + gh / 2, ["pH"], 14, INK, weight="700", anchor="middle", rot=-90))
    for k, (v, n) in enumerate(((v1, "Mezcla 1"), (v2, "Mezcla 2"))):
        bx = gx + gw * (0.2 + 0.45 * k)
        if v:
            b.append(rect(bx, gy + gh - v / 10 * gh, gw * 0.25, v / 10 * gh, "#B9BEC8", r=0, stroke=INK, sw=1.6))
        b.append(T(bx + gw * 0.125, gy + gh + 22, [n], 14, INK, weight="700", anchor="middle"))


def datos_113(b, x, y, w):
    c = A["color"]
    gw, gh = (w - 40) / 2, 168
    graf = (("A", 8, 9.2), ("B", 7, 7), ("C", 0, 9.8), ("D", 6, 3))
    for k, (L, v1, v2) in enumerate(graf):
        _barras(b, x + (k % 2) * (gw + 40), y + 8 + (k // 2) * (gh + 14), gw, gh, L, v1, v2, c)
    return y + 8 + 2 * (gh + 14)


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Dibuja tu gráfica antes de ver las cuatro", c,
                      "Lo de la cafetera: primero la evidencia que tendría que aparecer. Dibuja tú las dos barras que "
                      "esperarías si la hipótesis es cierta; después busca entre A, B, C y D la que se parece a la "
                      "tuya.")
    x0, ww = x + 22, w - 44
    gx, gy, gw, gh = x0 + 70, yy + 10, 360, 190
    for v in range(0, 11, 2):
        py = gy + gh - v / 10 * gh
        b.append(line(gx, py, gx + gw, py, LGRAY, 1.2, dash="3,5"))
        b.append(T(gx - 8, py + 5, [str(v)], 13, GRAY, anchor="end"))
    b.append(line(gx, gy + gh, gx + gw, gy + gh, INK, 2.2))
    b.append(line(gx, gy - 4, gx, gy + gh, INK, 2.2))
    b.append(T(gx - 42, gy + gh / 2, ["pH"], 14, GRAY, weight="700", anchor="middle", rot=-90))
    for k, n in enumerate(("Mezcla 1", "Mezcla 2")):
        bx = gx + gw * (0.18 + 0.45 * k)
        b.append(rect(bx, gy + 6, gw * 0.26, gh - 6, "white", r=0, stroke=LGRAY, sw=1.6, dash="5,5"))
        b.append(T(bx + gw * 0.13, gy + gh + 22, [n], 14, GRAY, anchor="middle"))
    rx = gx + gw + 50
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 96, c, r=14)
    rot(b, rx + 18, yy + 28, "UN pH MÁS BAJO QUIERE DECIR…", c, size=14)
    casillas(b, rx + 18, yy + 50, ("más ácido", "más básico"), c, paso=180)
    caja(b, rx, yy + 110, rw, 96, c, r=14)
    rot(b, rx + 18, yy + 138, "LA HIPÓTESIS, EN BARRAS", c, size=14)
    b.append(T(rx + 18, yy + 178, ["La barra que tiene que quedar más baja es la de la mezcla ____ ."], 16, INK))
    return gy + gh + 30


QA = dict(est=1, comp="Indagación",
          e="Una estudiante analiza la velocidad de la reacción representada por la ecuación química X + W → Z. "
            "Primero, establece unas condiciones iniciales y mide la velocidad de reacción. Luego, modifica las "
            "concentraciones molares de los reactivos y mide una nueva velocidad.",
          o=["En el experimento 3, porque un cambio en la concentración de X produce un mayor cambio en la velocidad "
             "de reacción.",
             "En el experimento 6, porque un cambio en la concentración de W produce un mayor cambio en la velocidad "
             "de reacción.",
             "En el experimento 6, porque la velocidad de reacción cambia únicamente cuando se varía la concentración "
             "de W.",
             "En el experimento 3, porque la velocidad de reacción aumenta si la concentración de X aumenta."],
          datos=datos_91, inst=ii1)
QB = dict(est=2, comp="Uso comprensivo del conocimiento científico",
          e="Un grupo de estudiantes realizó un experimento para identificar sustancias ácidas y básicas y obtuvo los "
            "siguientes resultados.",
          o=["menor que 7,0.", "entre 6,8 y 7,2.", "mayor que 7,0.", "entre 6,5 y 9,0."],
          datos=datos_65, inst=ii2)
QC = dict(est=3, comp="Uso comprensivo del conocimiento científico",
          e="La siguiente gráfica presenta la relación entre la temperatura y el volumen para un gas a presión "
            "constante.",
          o=["No sufre variación.", "Se triplica.", "Se duplica.", "Se reduce a la mitad."],
          datos=datos_95, inst=ii3)
QD = dict(est=4, comp="Indagación",
          e="Un estudiante tiene la mezcla 1 y la mezcla 2 y tiene la hipótesis que la mezcla 2 tiene menor pH que la "
            "mezcla 1. Si la hipótesis del estudiante es cierta, ¿cuál de las siguientes gráficas muestra los "
            "resultados que se esperaría encontrar?",
          o=[], datos=datos_113, inst=ii4)


def build(pages=(199, 203)):
    return [hoja_icfes("qui3_i1", pages[0], QA, QB),
            hoja_icfes("qui3_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
