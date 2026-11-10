#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 4 · entrenamiento ICFES · páginas 249 y 253.

Fuentes, verificadas contra la página del cuadernillo:
  · «Cuadernillo de preguntas · Prueba Ciencias Naturales · Saber 11.°» del Icfes (noviembre de
    2025, reeditado en febrero de 2026 con las mismas 50 preguntas: fuente_icfes/22-diciembre-…
    y fuente_icfes/24-feb-…). Preguntas 9 (p. 10), 32 (p. 23) y 48 (p. 33).
  · Cuadernillo Saber 11 2016-1, 2.ª sesión, cuadernillo ABD (encabezado «Saber 11 - 083 - B10O -
    ABD · 2a. sesión»; Drive «1. CUADERNILLOS ICFES» / «2016-2 SEGUNDA SESION.pdf», que en la
    portada dice 2016-1 segunda sesión), Ciencias Naturales, ítem 70 (p. 23).
Ninguna estaba en tablero/icfes.csv; las cuatro se reservaron en
tablero/propuestas/fis_icfes_reservas.csv. Ninguna nombra a un político. Las dos figuras de la
piscina (32), la figura de los parlantes (70) y la tabla y las cuatro gráficas de la 48 se
redibujaron con los mismos datos.

Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11» (el motor lo impone).

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · cuadernillo 2025 N.º 9  · D   (qué cambio asegura que el sonido va por el aire)  estrategia 1
    QB · cuadernillo 2025 N.º 32 · C   (cómo ve el nadador el farol con la piscina llena)  estrategia 2
    QC · 2016-1 2.ª ses. N.º 70  · C   (puntos negros y blancos frente a los parlantes)    estrategia 3
    QD · cuadernillo 2025 N.º 48 · B   (qué gráfica muestra la tabla del sonido)           estrategia 4

Cuentas:
  QA · La frecuencia la pone el animal (no cambia al cambiar de medio). La rapidez la pone el
       medio: ≈ 1500 m/s en agua, ≈ 340 m/s en aire. La longitud de onda también cambia (λ = v/f),
       pero depende de la fuente y del medio a la vez; la rapidez depende solo del medio → D. La
       forma de la onda (C) no identifica el medio.
  QB · La luz del farol entra al agua y se acerca a la normal (se dobla hacia abajo, más
       empinada). El ojo prolonga en línea recta el rayo que le llega: esa recta apunta más arriba
       que el farol de verdad → lo ve más alto → C.
  QC · Los dos parlantes emiten la misma nota. Donde las ondas llegan en fase (cresta con cresta)
       se suman: interferencia constructiva, sonido fuerte (puntos negros); donde llegan en
       oposición (cresta con valle) se anulan: destructiva, sonido débil (puntos blancos) → C.
       A y D meten reflexión o refracción; B dice que en todos los puntos pasan las dos cosas.
  QD · La variable que la estudiante cambió (temperatura) va en el eje horizontal y lo que midió
       (velocidad) en el vertical, con escalas que crecen: 0 a 3 °C y 331,7 a 333,5 m/s; cada grado
       sube 0,6 m/s (recta creciente) → B. A cambia los nombres de los ejes; C y D además ponen la
       escala de la velocidad al revés (de 333,5 a 331,7).
"""
from fis4 import *   # noqa: F401,F403  (configura la misión y EST)
from fis4 import rot, caja, pista, renglon, frase_hueco, letra, casillas, flecha, onda, AGUA


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 8, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · N.º 9 · el detector de sonido ─────────
def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Lo que pone el animal y lo que pone el agua", c,
                      "Lo de la cuerda y la cubeta: la fuente pone la frecuencia. Para cada magnitud decide quién la "
                      "pone; la que sirve para reconocer el medio es la que depende SOLO del medio.")
    x0, ww = x + 22, w - 44
    cols = (("MAGNITUD", 330), ("¿QUIÉN LA PONE?", ww - 330))
    px = x0
    for t, cw in cols:
        caja(b, px, yy, cw, 38, c, r=0, fill=A["bg"])
        rot(b, px + 16, yy + 25, t, c, size=13)
        px += cw
    for k, mag in enumerate(("longitud de onda", "frecuencia", "rapidez de la onda")):
        ry = yy + 38 + k * 44
        caja(b, x0, ry, cols[0][1], 44, c, r=0)
        b.append(T(x0 + 16, ry + 29, [mag], 17, INK))
        caja(b, x0 + cols[0][1], ry, cols[1][1], 44, c, r=0)
        casillas(b, x0 + cols[0][1] + 20, ry + 12, ("solo el animal", "solo el medio", "los dos"), c, paso=220,
                 size=15)
    return y + (yy - y) + 38 + 3 * 44


# ───────── QB · N.º 32 · el nadador y el farol ─────────
def _farol(b, x, y):
    b.append(line(x, y, x, y + 58, INK, 4))
    b.append(f'<circle cx="{x}" cy="{y - 8}" r="9" fill="{AMBER_BG}" stroke="{INK}" stroke-width="2"/>')
    for a in range(0, 360, 45):
        r = math.radians(a)
        b.append(line(x + 13 * math.cos(r), y - 8 + 13 * math.sin(r), x + 20 * math.cos(r),
                      y - 8 + 20 * math.sin(r), INK, 1.6))


def _piscina(b, x, y, w, h, llena, titulo):
    b.append(T(x + 120, y + 14, [titulo], 15, INK, weight="700"))
    bx = x + 70
    b.append(rect(x, y + 80, 70, h - 80, "#6E7480", r=0))
    _farol(b, x + 35, y + 22)
    b.append(T(x + 2, y + 76, ["Farol"], 13, INK))
    if llena:
        b.append(rect(bx, y + 82, w - 70, h - 82, "#C9CED6", r=0))
        b.append(T(bx + 30, y + 130, ["Agua"], 14, INK, weight="700"))
        b.append(T(x + w - 40, y + 72, ["Aire"], 14, INK, weight="700", anchor="end"))
    else:
        b.append(T(bx + 40, y + 150, ["Aire"], 14, INK, weight="700"))
    b.append(line(bx, y + 80, bx, y + h, INK, 3))
    b.append(line(bx, y + h, x + w, y + h, INK, 3))
    b.append(line(x + w, y + 80, x + w, y + h, INK, 3))
    ox, oy = x + w - 60, y + h - 40
    b.append(f'<circle cx="{ox}" cy="{oy}" r="11" fill="white" stroke="{INK}" stroke-width="2.2"/>')
    b.append(T(ox, oy + 30, ["Nadador"], 13, INK, anchor="middle"))
    fx, fy = x + 35, y + 14
    if not llena:
        flecha(b, fx + 10, fy + 6, ox - 10, oy - 6, INK, sw=2, head=9)
        b.append(T((fx + ox) / 2 + 10, (fy + oy) / 2 - 14, ["Rayo de luz"], 13, INK))
    else:
        sx = ox - 72
        sy = y + 82
        flecha(b, fx + 10, fy + 6, sx, sy, INK, sw=2, head=9)
        flecha(b, sx, sy, ox - 8, oy - 9, INK, sw=2, head=9)
        b.append(T((fx + sx) / 2 + 30, (fy + sy) / 2 - 12, ["Rayo de luz"], 13, INK))


def datos_32(b, x, y, w):
    pw = (w - 60) / 2
    _piscina(b, x + 20, y + 4, pw - 40, 190, False, "Figura 1. Piscina vacía")
    _piscina(b, x + 40 + pw, y + 4, pw - 40, 190, True, "Figura 2. Piscina llena de agua")
    return pregunta(b, x, y + 204, w, "Cuando una piscina está vacía, un nadador observa el farol que está en el borde, "
                                      "como se observa en la figura 1; luego, cuando se llena la piscina como se "
                                      "muestra en la figura 2, ¿cómo verá el nadador el farol?")


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "El ojo no sabe que el rayo se dobló", c,
                      "Lo de la cubeta: dibuja antes de elegir. El ojo cree que la luz siempre viene en línea recta. "
                      "En la figura 2, prolonga con regla y en punteado el último tramo del rayo, desde el nadador "
                      "hacia arriba, hasta la altura del farol.")
    x0, ww = x + 22, w - 44
    b.append(T(x0, yy + 24, ["Mi línea punteada pasa por"], 17, INK))
    casillas(b, x0 + 230, yy + 8, ("encima del farol", "el farol", "debajo del farol"), c, paso=210, size=16)
    b.append(T(x0, yy + 70, ["Al acercarse a la normal dentro del agua, el rayo que llega al ojo queda más"], 17, INK))
    renglon(b, x0 + 620, yy + 74, x0 + 820)
    return yy + 84


# ───────── QC · N.º 70 · los dos parlantes ─────────
def _parlante(b, x, y):
    b.append(rect(x, y, 44, 64, "white", r=4, stroke=INK, sw=2))
    for r, yy in ((9, y + 18), (14, y + 44)):
        b.append(f'<circle cx="{x + 22}" cy="{yy}" r="{r}" fill="none" stroke="{INK}" stroke-width="2"/>')


PUNTOS_70 = ((0.24, 0.3, 0), (0.34, 0.24, 1), (0.44, 0.2, 0), (0.54, 0.24, 1), (0.64, 0.3, 0),
             (0.18, 0.55, 1), (0.29, 0.5, 0), (0.39, 0.46, 1), (0.49, 0.45, 0), (0.59, 0.46, 1), (0.69, 0.52, 0),
             (0.22, 0.8, 0), (0.33, 0.75, 1), (0.44, 0.72, 0), (0.55, 0.74, 1), (0.66, 0.8, 0))


def datos_70(b, x, y, w):
    fw, fh = 620, 196
    fx = x + (w - fw) / 2
    b.append(rect(fx, y + 6, fw, fh, "white", r=0, stroke=INK, sw=2))
    b.append(rect(fx + 2, y + 8, fw - 4, 60, "#EEF0F4", r=0))
    b.append(T(fx + fw / 2, y + 44, ["emisora del colegio"], 14, INK, anchor="middle"))
    _parlante(b, fx + 24, y + 34)
    _parlante(b, fx + fw - 68, y + 34)
    for px, py, negro in PUNTOS_70:
        cx, cy = fx + fw * px + 40, y + 70 + (fh - 70) * py
        b.append(f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="11" ry="6" fill="{INK if negro else "white"}" '
                 f'stroke="{INK}" stroke-width="1.8"/>')
    b.append(f'<circle cx="{fx + fw - 50}" cy="{y + 154}" r="20" fill="white" stroke="{INK}" stroke-width="2"/>')
    b.append(T(fx + fw - 50, y + 162, ["?"], 22, INK, weight="700", anchor="middle"))
    b.append(T(fx + fw - 50, y + 194, ["estudiante"], 12, INK, anchor="middle"))
    return pregunta(b, x, y + fh + 16, w, "Si el estudiante le pregunta a la profesora la razón por la cual en los puntos "
                                          "negros el sonido se escucha más fuerte que en los blancos, ¿cuál de las "
                                          "siguientes argumentaciones debe darle la profesora al estudiante?")


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Suma dos ondas y escucha el resultado", c,
                      "Lo de los vasos: concluye solo con lo observado, que aquí es «más fuerte» y «más suave». "
                      "Dibuja la suma de cada pareja de ondas y di si suena más fuerte o más suave.")
    x0, ww = x + 22, w - 44
    pw = (ww - 24) / 2
    for k, (rt, fase) in enumerate((("CRESTA CON CRESTA", 0), ("CRESTA CON VALLE", math.pi))):
        px = x0 + k * (pw + 24)
        caja(b, px, yy, pw, 170, c, r=14)
        rot(b, px + 18, yy + 26, rt, c, size=13)
        for j, ph in enumerate((0, fase)):
            pts = []
            for i in range(61):
                xx = px + 30 + (pw * 0.5 - 40) * i / 60
                pts.append(f"{xx:.1f},{yy + 64 + j * 44 - 14 * math.sin(2 * math.pi * i / 30 + ph):.1f}")
            b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{INK}" stroke-width="2"/>')
        b.append(T(px + pw * 0.5, yy + 92, ["="], 26, INK, anchor="middle"))
        b.append(rect(px + pw * 0.5 + 24, yy + 44, pw * 0.5 - 44, 90, "white", r=8, stroke=LGRAY, sw=1.6, dash="5,5"))
        pista(b, px + pw * 0.75, yy + 154, "la suma, dibujada por mí", anchor="middle")
    yy += 186
    return frase_hueco(b, x0, yy, ww, "Puntos negros: ______________________ · puntos blancos: ______________________",
                       c)


# ───────── QD · N.º 48 · velocidad del sonido y temperatura ─────────
FILAS_48 = (("0", "331,7"), ("1", "332,3"), ("2", "332,9"), ("3", "333,5"))


def datos_48(b, x, y, w):
    cols = (300, 320)
    x0 = x + (w - sum(cols)) / 2
    yy = y + 4
    px = x0
    for cw, t in zip(cols, ("Temperatura (°C)", "Velocidad del sonido (m/s)")):
        b.append(rect(px, yy, cw, 32, SOFT, r=0, stroke=GRAY, sw=1.4))
        b.append(T(px + cw / 2, yy + 22, [t], 15, INK, weight="700", anchor="middle"))
        px += cw
    yy += 32
    for f in FILAS_48:
        px = x0
        for cw, v in zip(cols, f):
            b.append(rect(px, yy, cw, 28, "white", r=0, stroke=GRAY, sw=1.4))
            b.append(T(px + cw / 2, yy + 20, [v], 15, INK, anchor="middle"))
            px += cw
        yy += 28
    yy = pregunta(b, x, yy + 2, w, "¿Cuál de las siguientes gráficas muestra los resultados del experimento?")
    c = A["color"]
    gw = (w - 30) / 4
    vel = ("331,7", "332,3", "332,9", "333,5")
    tem = ("0", "1", "2", "3")
    graf = {"A": ("Temperatura (°C)", vel, "Velocidad del sonido (m/s)", tem),
            "B": ("Velocidad del sonido (m/s)", vel, "Temperatura (°C)", tem),
            "C": ("Temperatura (°C)", tem, "Velocidad del sonido (m/s)", vel[::-1]),
            "D": ("Velocidad del sonido (m/s)", tem, "Temperatura (°C)", vel[::-1])}
    for k, L in enumerate("ABCD"):
        ox = x + k * (gw + 10)
        ylab, yt, xlab, xt = graf[L]
        letra(b, ox + 16, yy + 20, L, c)
        gx, gy, ggw, ggh = ox + 96, yy + 46, gw - 116, 124
        for i in range(4):
            py = gy + ggh - i / 3 * ggh
            px = gx + i / 3 * ggw
            b.append(line(gx, py, gx + ggw, py, LGRAY, 1.2))
            b.append(line(px, gy, px, gy + ggh, LGRAY, 1.2))
            b.append(T(gx - 6, py + 5, [yt[i]], 13, INK, anchor="end"))
            b.append(T(px, gy + ggh + 18, [xt[i]], 13, INK, anchor="middle"))
        b.append(line(gx, gy + ggh, gx + ggw + 8, gy + ggh, INK, 2))
        b.append(line(gx, gy - 8, gx, gy + ggh, INK, 2))
        b.append(line(gx, gy + ggh, gx + ggw, gy, INK, 1.8))
        for i in range(4):
            b.append(f'<circle cx="{gx + i / 3 * ggw:.1f}" cy="{gy + ggh - i / 3 * ggh:.1f}" r="4.5" fill="{INK}"/>')
        b.append(T(gx + ggw / 2, gy + ggh + 40, [xlab], 13, INK, weight="700", anchor="middle"))
        yl = ylab.replace(" del sonido", " del|sonido").split("|")
        b.append(T(ox + 26 - (len(yl) - 1) * 8, gy + ggh / 2, yl, 13, INK, weight="700", anchor="middle",
                   rot=-90, lh=16))
    return yy + 46 + 124 + 50


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Cada eje con su variable y su escala", c,
                      "Lo del Wi-Fi: lee la tabla y su escala. La estudiante escogió las temperaturas y midió la "
                      "velocidad. Revisa en cada gráfica qué va en el eje horizontal y si sus números crecen.")
    x0, ww = x + 22, w - 44
    cols = (("", 470),) + tuple((L, (ww - 470) / 4) for L in "ABCD")
    caja(b, x0, yy, cols[0][1], 40, c, r=0, fill=A["bg"])
    rot(b, x0 + 14, yy + 26, "LO QUE REVISO", c, size=13)
    px = x0 + cols[0][1]
    for L, cw in cols[1:]:
        caja(b, px, yy, cw, 40, c, r=0, fill=A["bg"])
        letra(b, px + cw / 2, yy + 20, L, c, r=14, size=14)
        px += cw
    for k, rg in enumerate(("En el eje horizontal está la variable que ella escogió",
                            "Los números de los dos ejes crecen hacia afuera")):
        ry = yy + 40 + k * 46
        caja(b, x0, ry, cols[0][1], 46, c, r=0)
        b.append(T(x0 + 14, ry + 29, [rg], 15, INK))
        px = x0 + cols[0][1]
        for L, cw in cols[1:]:
            caja(b, px, ry, cw, 46, c, r=0)
            casillas(b, px + cw / 2 - 60, ry + 13, ("sí", "no"), c, paso=66, size=14)
            px += cw
    return yy + 40 + 2 * 46


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="Un investigador sumerge un detector de sonido en agua para grabar los sonidos emitidos por los animales. "
            "El detector muestra la longitud de onda, la frecuencia, la velocidad de propagación y la distancia a la "
            "que se produce el sonido emitido por los animales. El investigador saca el detector del agua y registra "
            "un sonido. ¿Cuál cambio de las variables mencionadas le permite asegurar al investigador que el sonido "
            "se trasmite por el aire y no por el agua?",
          o=["La longitud de onda.", "La frecuencia de la onda.", "La forma de la onda.", "La velocidad de la onda."],
          inst=ii1)
QB = dict(est=2, comp="Explicación de fenómenos",
          e="Los rayos de luz emitidos por objetos luminosos viajan en línea recta dentro de un mismo medio, como se "
            "muestra en la Figura 1. Si un rayo de luz pasa de aire a agua cambia su dirección, como se muestra en la "
            "Figura 2.",
          o=["Más bajo.", "De la misma altura.", "Más alto.", "Invertido."],
          datos=datos_32, inst=ii2)
QC = dict(est=3, comp="Explicación de fenómenos",
          e="Un estudiante camina por el frente de dos parlantes ubicados afuera de la emisora del colegio. Dentro de "
            "la emisora la profesora de física toca la nota «do», en un clarinete, para ayudar al profesor de música a "
            "afinar algunos instrumentos musicales. El estudiante nota que hay lugares en donde el sonido del "
            "clarinete se escucha más fuerte mientras que en otros no, y los marca como se muestra en la siguiente "
            "figura.",
          o=["Porque las ondas de sonido interfieren constructivamente en los puntos negros, y en los puntos blancos se "
             "reflejan.",
             "Porque las ondas de sonido interfieren constructivamente y destructivamente en todos los puntos, pero en "
             "los blancos las ondas se refractan.",
             "Porque las ondas de sonido interfieren constructivamente en los puntos negros, y destructivamente, en los "
             "puntos blancos.",
             "Porque las ondas de sonido interfieren destructivamente en los puntos blancos y negros, pero en los "
             "negros se reflejan y se refractan."],
          datos=datos_70, inst=ii3)
QD = dict(est=4, comp="Indagación",
          e="Una estudiante realizó un experimento para medir la velocidad de propagación del sonido en el aire a "
            "diferentes temperaturas. Los resultados que obtuvo se muestran en la siguiente tabla.",
          o=[], datos=datos_48, inst=ii4)


def build(pages=(249, 253)):
    return [hoja_icfes("fis4_i1", pages[0], QA, QB),
            hoja_icfes("fis4_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
