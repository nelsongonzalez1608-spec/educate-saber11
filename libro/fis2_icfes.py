#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 2 · entrenamiento ICFES · páginas 235 y 239.

Cuatro preguntas de Ciencias Naturales con contenido de termodinámica, de dos fuentes:
  · «Cuadernillo de preguntas · Prueba Ciencias Naturales · Saber 11.º» del Icfes (repo:
    fuente_icfes/22-diciembre-…-2025.pdf y 24-feb-…-2026.pdf; las mismas 50 preguntas).
    Preguntas 1, 22 y 27, verificadas contra el PDF.
  · ASED pre código 11 (Drive), capítulo 9 «Preguntas de Física», sección Mecánica clásica,
    ítem 10 (el ASED reinicia la numeración en cada sección; la pregunta está en Mecánica
    clásica aunque su contenido es el aire caliente). Solo se leyó el texto del PDF.
Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano, no copiadas del solucionario):

    QA · ASED Mecánica N.º 10 · C   (el aire caliente se expande, parte sale por la boca del globo,
                                     baja la densidad de adentro y el empuje supera al peso)     estrategia 1
    QB · cuadernillo N.º 22 · C     (misma estufa y mismo minuto → mismo calor Q; con el doble de
                                     masa, ΔT = Q/(2m·c) = 2 °C / 2 = 1 °C → 15 + 1 = 16 °C)    estrategia 2
    QC · cuadernillo N.º 1 · B      (al hervir, las moléculas de H₂O no se rompen: se separan y
                                     ocupan todo el recipiente)                                  estrategia 3
    QD · cuadernillo N.º 27 · A     (a 25 km hay menos partículas de aire: menos presión; la
                                     presión de vapor la iguala a menor temperatura)             estrategia 4

El solucionario del cuadernillo da 1·B, 22·C y 27·A: coincide.
Adaptaciones (registradas en fis2_icfes.csv): en la N.º 1 y la N.º 27 los modelos se redibujan
con la misma forma; en la N.º 1 las opciones, que son dibujos, se nombran «El modelo A» … «D».
Nota de la N.º 27: a 25 km la presión es ≈ 2,5 kPa y el agua herviría hacia 21 °C (dato para el
profe; la clave A no cambia).
"""
import random

from fis2 import *   # noqa: F401,F403  (configura la misión y EST)
from fis2 import rot, caja, pista, texto, renglon, hueco, frase_hueco, flecha, marca, linea_pista, particula


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · ASED Mecánica clásica N.º 10 · el globo ─────────
def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "La cadena del globo que sube", c,
                      "Como en la pregunta 8: el aire caliente sube porque es menos denso. Arma la cadena eslabón por "
                      "eslabón; cada uno tiene que salir del anterior.")
    x0, ww = x + 22, w - 44
    n, gap = 4, 34
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("1 · EL FUEGO", "le hace al aire de adentro:"), ("2 · LAS PARTÍCULAS", "se mueven más y se"),
                                  ("3 · ADENTRO QUEDA", "(más / menos) masa de aire"), ("4 · EL GLOBO", "sube porque el empuje es"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 120, c, r=12)
        rot(b, bx + 14, yy + 26, rt, c, size=13)
        pista(b, bx + 14, yy + 50, ps, size=13)
        renglon(b, bx + 14, yy + 92, bx + bw - 14)
        if k < n - 1:
            flecha(b, bx + bw + 4, yy + 60, bx + bw + gap - 4, yy + 60, c, sw=2.6, head=11)
    return yy + 120


# ───────── QB · cuadernillo N.º 22 · 1 L y 2 L en la misma estufa ─────────
def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "El mismo calor repartido en el doble de agua", c,
                      "Como en la pregunta 7: Q = m · c · ΔT. La estufa y el minuto son los mismos, así que el calor que "
                      "entra es el mismo. Escribe qué cambia y qué no antes de calcular.")
    x0, ww = x + 22, w - 44
    cols = ("", "CALOR QUE ENTRA", "MASA DE AGUA", "CUÁNTO SUBE (ΔT)", "TEMPERATURA FINAL")
    xs = (0, 160, 440, 680, 960)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=13)
    for j, (lab, q, m, dt, tf) in enumerate((("1 litro", "Q", "m", "2 °C", "17 °C"),
                                            ("2 litros", "______", "______", "______", "______"))):
        ry = yy + 26 + j * 56
        caja(b, x0, ry, ww, 46, c, r=10)
        texto(b, x0 + 16, ry + 30, lab, 17, INK, weight="700")
        for k, v in enumerate((q, m, dt, tf)):
            texto(b, x0 + xs[k + 1] + 10, ry + 30, v, 17)
    return yy + 26 + 2 * 56


# ───────── QC · cuadernillo N.º 1 · las moléculas de agua al hervir ─────────
def _h2o(b, cx, cy, s=1.0, ang=0):
    """Una molécula de agua: O (negro) con dos H (blancos)."""
    a = math.radians(ang)
    for da in (-52, 52):
        t = a + math.radians(da) + math.pi / 2
        hx, hy = cx + 7 * s * math.cos(t), cy + 7 * s * math.sin(t)
        b.append(f'<circle cx="{hx:.1f}" cy="{hy:.1f}" r="{3.2 * s:.1f}" fill="white" stroke="{INK}" stroke-width="1.3"/>')
    b.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{4.4 * s:.1f}" fill="{INK}"/>')


def _o(b, cx, cy):
    b.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="4.4" fill="{INK}"/>')


def _h(b, cx, cy):
    b.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="3.4" fill="white" stroke="{INK}" stroke-width="1.3"/>')


def _vaso(b, x, y, w=64, h=84):
    b.append(f'<path d="M {x} {y} L {x} {y + h - 6} Q {x} {y + h} {x + 6} {y + h} L {x + w - 6} {y + h} '
             f'Q {x + w} {y + h} {x + w} {y + h - 6} L {x + w} {y}" fill="white" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<ellipse cx="{x + w / 2}" cy="{y}" rx="{w / 2}" ry="6" fill="white" stroke="{INK}" stroke-width="2"/>')


def _liquido(b, x, y, w=64, h=84):
    for i in range(4):
        for j in range(2):
            _h2o(b, x + 10 + i * 15, y + h - 12 - j * 13, 0.85, (i * 47 + j * 90) % 360)


def datos_1(b, x, y, w):
    _vaso(b, x + w / 2 - 32, y + 12)
    _liquido(b, x + w / 2 - 32, y + 12)
    yy = pregunta(b, x, y + 104, w, "Cuando este recipiente se calienta manteniendo la presión constante, la distribución "
                                    "de las moléculas cambia, modificando el estado del agua. ¿Cuál de los siguientes "
                                    "modelos muestra correctamente la distribución de las moléculas de agua en estado "
                                    "líquido y gaseoso?")
    random.seed(7)
    for k in range(4):
        mx = x + 20 + k * 310
        texto(b, mx + 80, yy + 22, "ABCD"[k] + ".", 18, INK, weight="700", anchor="middle")
        texto(b, mx + 42, yy + 46, "Líquido", 14, INK, anchor="middle")
        texto(b, mx + 122, yy + 46, "Gas", 14, INK, anchor="middle")
        _vaso(b, mx + 10, yy + 60)
        _liquido(b, mx + 10, yy + 60)
        gx, gy = mx + 90, yy + 60
        _vaso(b, gx, gy)
        if k == 0:        # oxígenos arriba, hidrógenos abajo
            for i in range(8):
                _o(b, gx + 9 + (i % 4) * 15, gy + 14 + (i // 4) * 14)
            for i in range(10):
                _h(b, gx + 8 + (i % 5) * 12, gy + 62 + (i // 5) * 10)
        elif k == 1:      # moléculas enteras repartidas
            for i, (px, py) in enumerate(((12, 16), (40, 12), (26, 34), (52, 38), (12, 56), (38, 60), (54, 70), (22, 76))):
                _h2o(b, gx + px, gy + py, 0.85, i * 70)
        elif k == 2:      # moléculas apretadas arriba
            for i in range(4):
                for j in range(2):
                    _h2o(b, gx + 10 + i * 15, gy + 14 + j * 13, 0.85, (i * 47 + j * 90) % 360)
        else:             # átomos sueltos y revueltos
            for i, (px, py) in enumerate(((10, 14), (30, 22), (50, 12), (18, 40), (44, 44), (28, 62), (52, 70), (12, 74))):
                _o(b, gx + px, gy + py)
            for i, (px, py) in enumerate(((22, 12), (42, 28), (56, 30), (10, 28), (32, 46), (54, 56), (14, 58),
                                          (40, 64), (24, 80), (46, 80), (34, 34), (8, 64), (58, 44), (20, 50),
                                          (36, 76), (48, 18))):
                _h(b, gx + px, gy + py)
    return yy + 150


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "¿Se rompe la molécula al hervir?", c,
                      "Como en las preguntas 2 y 5: al calentar, las partículas se mueven más rápido. Decide qué cambia y "
                      "qué no cambia cuando el agua pasa de líquido a gas, y busca el modelo que cumple tus dos casillas.")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    for k, (rt, l1) in enumerate((("LO QUE CAMBIA AL HERVIR", "la distancia entre moléculas se vuelve"),
                                  ("LO QUE NO CAMBIA AL HERVIR", "cada molécula sigue siendo"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 96, c, r=12)
        rot(b, bx + 16, yy + 26, rt, c, size=13)
        linea_pista(b, bx + 16, yy + 70, bx + half - 16, l1)
    return yy + 96


# ───────── QD · cuadernillo N.º 27 · hervir a 25 km de altura ─────────
def datos_27(b, x, y, w):
    random.seed(27)
    bx, by, bw, bh = x + w / 2 - 70, y + 14, 140, 160
    b.append(rect(bx, by, bw, bh, "white", r=0, stroke=INK, sw=2))
    for _ in range(230):
        f = random.random() ** 3.4
        b.append(f'<circle cx="{bx + random.uniform(6, bw - 6):.1f}" cy="{by + bh - 4 - f * (bh - 10):.1f}" r="1.6" fill="{GRAY}"/>')
    for km in range(0, 31, 5):
        ty = by + bh - km / 30 * bh
        b.append(f'<line x1="{bx - 8}" y1="{ty:.0f}" x2="{bx}" y2="{ty:.0f}" stroke="{INK}" stroke-width="1.6"/>')
        b.append(T(bx - 12, ty + 5, [str(km)], 13, INK, anchor="end"))
    texto(b, bx - 12, by - 8, "Altura (km)", 14, INK, weight="700", anchor="end")
    return pregunta(b, x, by + bh + 6, w, "Una olla con agua hierve a una temperatura de 100 °C, cuando la altura es de 0 km. "
                                          "Teniendo en cuenta que el punto de ebullición corresponde a la temperatura a la "
                                          "cual la presión de vapor del líquido iguala a la presión atmosférica, si se pone "
                                          "a calentar la misma cantidad de agua a una altura de 25 km, ¿qué le sucede al "
                                          "agua?")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Menos aire encima, menos presión", c,
                      "Como en la pregunta 4 con la olla: cuenta en el modelo si hay más o menos partículas a 25 km que a "
                      "0 km. Después sigue la regla del enunciado hasta la temperatura.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 34
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("A 25 km HAY", "(más / menos) partículas de aire"), ("LA PRESIÓN ES", "(mayor / menor) que abajo"),
                                  ("EL VAPOR LA ALCANZA", "a una temperatura (mayor / menor)"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 106, c, r=12)
        rot(b, bx + 14, yy + 26, rt, c, size=13)
        pista(b, bx + 14, yy + 50, ps, size=13)
        renglon(b, bx + 14, yy + 88, bx + bw - 14)
        if k < n - 1:
            flecha(b, bx + bw + 4, yy + 54, bx + bw + gap - 4, yy + 54, c, sw=2.6, head=11)
    return yy + 106


QA = dict(est=1, comp="Explicación de fenómenos",
          e="Para elevar un globo se calienta con fuego el aire que está dentro de él. La explicación más acertada de "
            "por qué el globo se eleva, es que al calentar el aire",
          o=["la presión contra las paredes internas del globo es mayor que la presión externa.",
             "una parte del aire sale con velocidad hacia abajo, generando un impulso hacia arriba.",
             "una parte del aire sale del globo, disminuyendo la densidad y generando un empuje que lo eleva.",
             "el plástico del globo se tensa disminuyendo su peso específico y el globo se eleva."],
          inst=ii1)
QB = dict(est=2, comp="Uso comprensivo del conocimiento científico",
          e="Una estudiante calentó en una estufa, durante 1 minuto, un litro de agua que inicialmente estaba a 15 °C. "
            "La temperatura final del agua fue 17 °C. Si ahora calienta 2 litros de agua que inicialmente están a 15 °C, "
            "en la misma estufa durante un minuto, ¿cuál será la temperatura final de los 2 litros de agua?",
          o=["19 °C.", "17 °C.", "16 °C.", "15 °C."],
          inst=ii2)
QC = dict(est=3, comp="Uso comprensivo del conocimiento científico",
          e="A continuación, se muestra un modelo de la distribución de las moléculas de agua en estado líquido, en un "
            "recipiente cerrado.",
          o=["El modelo A.", "El modelo B.", "El modelo C.", "El modelo D."],
          datos=datos_1, inst=ii3)
QD = dict(est=4, comp="Explicación de fenómenos",
          e="El siguiente modelo representa la relación entre la altura y la cantidad de partículas de aire.",
          o=["Hierve a una temperatura menor que 100 °C, porque la presión es menor en esta altura.",
             "Hierve a una temperatura mayor que 100 °C, porque la presión es menor en esta altura.",
             "Nunca hierve, porque en esta altura hay muy poca cantidad de aire.",
             "Se congela, porque al no haber aire el agua pasará a estado sólido."],
          datos=datos_27, inst=ii4)


def build(pages=(235, 239)):
    return [hoja_icfes("fis2_i1", pages[0], QA, QB),
            hoja_icfes("fis2_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
