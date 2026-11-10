#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 5 · entrenamiento ICFES · páginas 256 y 260.

Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11», sin año ni «oficial».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · 2016-1, 2.ª ses. (ABD), CN, ítem 79  · A   (choque de dos pelotas · tabla de momentos)    estrategia 1
    QB · 2016-1, 2.ª ses. (ABD), CN, ítem 52  · D   (piñata colgada de una polea · equilibrio)    estrategia 2
    QC · 2016-1, 1.ª ses. (AAM), CN, ítem 106 · A   (resortes y masa de 500 g · qué controlar)    estrategia 3
    QD · cuadernillo nov 2025 / feb 2026, N.º 26 · D (pelota soplada que sube acelerada)          estrategia 4

  79 · A: la fuerza es proporcional a la variación del momento. Pelota 2: Δp = después − antes =
       9,00 · 20,60 · 27,10 · 31,60 kg·m/s en I, II, III y IV: la mayor, en el lanzamiento IV.
       (La pelota 1 pierde lo mismo: 27,10 − 18,05 = 9,05; 27,10 − 6,50 = 20,60; 27,10 − 0 = 27,10;
       27,10 − (−4,50) = 31,60: el momento total se conserva.) Pelota 1: 5 kg desde 1,5 m; con
       g = 9,8 m/s², v = √(2 g h) ≈ 5,42 m/s y p ≈ 27,1 kg·m/s, como dice la tabla.
       Verificada contra la página 26 del escaneo (Drive «2016-2 SEGUNDA SESION.pdf», encabezado
       «Saber 11 - 083 - P4 - ABD · 2a. sesión»; la portada dice 2016-1 segunda sesión). La rampa
       se redibujó; la tabla se copió con los mismos números.
  52 · D: la piñata está quieta: la tensión de la cuerda hacia arriba iguala su peso; una polea fija
       solo cambia la dirección de la cuerda, así que el niño tira con una fuerza igual al peso.
       A (el peso cambia con la altura), B (la posición del niño) y C (la polea sola) no explican el
       equilibrio. Verificada contra la página 17 del mismo escaneo. Figura redibujada.
 106 · A: para comparar la elasticidad de varios resortes se cambia el resorte y se deja fija la
       masa que se cuelga. B obliga al resultado; C (el tiempo) no influye; D cambiaría justo la
       variable que se compara. Verificada contra la página 33 del escaneo «2016-1 PRIMERA
       SESION.pdf» (encabezado «Saber 11 - 083 - B05R - AAM · 1a. sesión»).
  26 · D: si la pelota sube cada vez más rápido, la fuerza neta va hacia arriba: la fuerza del aire
       es mayor que el peso (segunda ley de Newton). A (el peso cambia), B (iguales: velocidad
       constante) y C (al revés) no lo explican. Cuadernillo oficial «Prueba Ciencias Naturales,
       Cuadernillo de preguntas Saber 11.º» (Icfes, nov 2025; el de feb 2026 trae las mismas 50
       preguntas), pregunta 26, p. 20. Es la misma pregunta del 2016-1, 2.ª sesión, ítem 53, con
       las opciones en otro orden: se usa el orden del cuadernillo 2025. Figura redibujada.

Reservadas en tablero/propuestas/fis_icfes_reservas.csv.
"""
from fis5 import *   # noqa: F401,F403  (configura la misión y EST)
from fis5 import rot, caja, pista, renglon, texto, sino, tinte, tabla_vacia, vector, caja_preg


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


def tabla(b, x, y, cols, filas, c=GRAY, rh=34, head_h=38, size=16):
    """Tabla de datos del cuadernillo, en tinta."""
    W_ = sum(w for w, _ in cols)
    b.append(rect(x, y, W_, head_h, "#F1F3F6", r=0, stroke=c, sw=1.6))
    cx = x
    for w_, hd in cols:
        texto(b, cx + w_ / 2, y + head_h / 2 + 6, hd, size=size, weight="700", anchor="middle")
        cx += w_
    yy = y + head_h
    for f in filas:
        b.append(rect(x, yy, W_, rh, "white", r=0, stroke=c, sw=1.6))
        cx = x
        for (w_, _), v in zip(cols, f):
            texto(b, cx + w_ / 2, yy + rh / 2 + 6, v, size=size, anchor="middle")
            cx += w_
        yy += rh
    cx = x
    for w_, _ in cols[:-1]:
        cx += w_
        b.append(line(cx, y, cx, yy, c, 1.6))
    return yy


# ───────── QA · ítem 79 · choque de dos pelotas ─────────
def datos_79(b, x, y, w):
    # rampa
    rx, ry = x + 60, y + 10
    b.append(line(rx, ry + 10, rx, ry + 130, INK, 3))
    b.append(f'<path d="M {rx} {ry + 20} Q {rx + 60} {ry + 120} {rx + 260} {ry + 128} L {rx + 420} {ry + 128}" '
             f'fill="none" stroke="{INK}" stroke-width="3"/>')
    b.append(line(rx - 30, ry + 132, rx + 440, ry + 132, INK, 2))
    b.append(f'<circle cx="{rx + 14}" cy="{ry + 6}" r="14" fill="white" stroke="{INK}" stroke-width="2.2"/>')
    b.append(f'<circle cx="{rx + 404}" cy="{ry + 116}" r="12" fill="white" stroke="{INK}" stroke-width="2.2"/>')
    texto(b, rx + 36, ry + 10, "Pelota 1 · masa = 5 kg", size=15)
    texto(b, rx + 330, ry + 96, "Pelota 2", size=15)
    texto(b, rx - 16, ry + 80, "1,5 m", size=15, anchor="end")
    yy = pregunta(b, x + 540, y - 6, w - 540,
                  "La estudiante registra en la tabla las variaciones del momento antes y después del choque de "
                  "cada pelota.")
    yy = max(yy, y + 138) + 4
    cols = ((150, "Lanzamiento"), (180, "Pelota 1 · antes"), (190, "Pelota 1 · después"),
            (200, "Masa pelota 2 (kg)"), (180, "Pelota 2 · antes"), (190, "Pelota 2 · después"))
    filas = (("I", "27,10", "18,05", "1", "0", "9,00"), ("II", "27,10", "6,50", "3", "0", "20,60"),
             ("III", "27,10", "0,00", "5", "0", "27,10"), ("IV", "27,10", "−4,50", "7", "0", "31,60"))
    yy = tabla(b, x, yy, cols, filas, rh=28, head_h=32, size=15)
    pista(b, x, yy + 20, "momentos en kg·m/s")
    return pregunta(b, x, yy + 24, w, "Si la estudiante sabe que la variación del momento es proporcional a la "
                                      "fuerza, ¿en cuál de los lanzamientos la pelota 1 se ejerció mayor fuerza "
                                      "para mover la pelota 2?")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Cuánto cambió el momento en cada choque", c,
                      "Como con los joules del dron: cada magnitud con su unidad. Δp = p después − p antes, en kg·m/s.")
    x0, ww = x + 22, w - 44
    cols = (190, (ww - 190) / 4, (ww - 190) / 4, (ww - 190) / 4, (ww - 190) / 4)
    yy = tabla_vacia(b, x0, yy, cols, ("LANZAMIENTO", "I", "II", "III", "IV"),
                     ("Δp pelota 2", "Δp pelota 1"), c, rh=46, hh=30, size=15)
    pista(b, x0, yy + 20, "¿se compensan los dos cambios en cada choque? ¿qué dice eso del momento total?")
    return yy + 24


# ───────── QB · ítem 52 · piñata y polea ─────────
def datos_52(b, x, y, w):
    yy = pregunta(b, x, y + 24, w - 300, "La piñata se mantiene en equilibrio y no se cae. Esto ocurre porque")
    px, py = x + w - 160, y - 30
    b.append(line(px - 80, py, px + 80, py, INK, 3))
    b.append(line(px, py, px, py + 30, INK, 2))
    b.append(f'<circle cx="{px}" cy="{py + 50}" r="22" fill="white" stroke="{INK}" stroke-width="2.4"/>')
    b.append(line(px - 22, py + 50, px - 22, py + 150, INK, 2))
    b.append(line(px + 22, py + 50, px + 22, py + 110, INK, 2))
    b.append(f'<polygon points="{px + 22},{py + 110} {px + 52},{py + 140} {px + 22},{py + 170} {px - 8},{py + 140}" '
             f'fill="{tinte(EDU_ORO, 0.7)}" stroke="{INK}" stroke-width="2"/>')
    texto(b, px + 60, py + 146, "piñata", size=14)
    b.append(f'<circle cx="{px - 22}" cy="{py + 162}" r="9" fill="white" stroke="{INK}" stroke-width="2"/>')
    b.append(line(px - 22, py + 171, px - 22, py + 205, INK, 2.4))
    texto(b, px - 40, py + 196, "niño", size=14, anchor="end")
    return max(yy, y + 210)


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Las fuerzas sobre la piñata quieta", c,
                      "Como con el agua del pitillo: cada fuerza con quién la hace. Dibuja las flechas sobre la "
                      "piñata y compara sus tamaños.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 230, 150, c, r=12)
    b.append(f'<circle cx="{x0 + 115}" cy="{yy + 80}" r="9" fill="{INK}"/>')
    pista(b, x0 + 14, yy + 24, "la piñata (un punto)")
    half = (ww - 270) / 2
    caja_preg(b, x0 + 250, yy, half, 150, c, "QUIÉN TIRA HACIA ARRIBA", "¿la cuerda, la polea o el niño? ¿y cuánto?", 2)
    caja_preg(b, x0 + 270 + half, yy, half, 150, c, "SI NO SE MUEVE…", "la fuerza hacia arriba es ____ que el peso", 2)
    return yy + 150


# ───────── QC · ítem 106 · resortes ─────────
def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Qué se repite igual en cada resorte", c,
                      "Como en el canal de la marea: una sola cosa cambia. Aquí se comparan resortes; escribe qué es lo "
                      "que cambia, qué tiene que quedar igual y qué se mide.")
    x0, ww = x + 22, w - 44
    cw = (ww - 40) / 3
    for k, t in enumerate(("LO QUE CAMBIA", "LO QUE QUEDA IGUAL", "LO QUE SE MIDE")):
        caja_preg(b, x0 + k * (cw + 20), yy, cw, 140, c, t, "", 2)
    yy += 160
    return caja_preg(b, x0, yy, ww, 104, c, "LA PRUEBA DEL COMPAÑERO",
                     "Si al repetir cambia algo más que el resorte, ¿podrá saber qué causó la diferencia? ¿Qué podría "
                     "cambiar sin darse cuenta?")


# ───────── QD · pregunta 26 · pelota en el tubo ─────────
def datos_26(b, x, y, w):
    tx, ty = x + 80, y + 4
    b.append(rect(tx, ty, 70, 200, "white", r=8, stroke=INK, sw=2.2))
    b.append(f'<circle cx="{tx + 35}" cy="{ty + 80}" r="30" fill="#D8DCE2" stroke="{INK}" stroke-width="2"/>')
    for dx_ in (18, 52):
        vector(b, tx + dx_, ty + 190, tx + dx_, ty + 130, INK, sw=2.2, head=9)
    texto(b, tx + 100, ty + 40, "La pelota se mueve aceleradamente hacia arriba", size=16, weight="700")
    vector(b, tx + 110, ty + 150, tx + 110, ty + 100, INK, sw=2.2, head=9)
    texto(b, tx + 130, ty + 130, "dirección de movimiento del aire soplado", size=16, weight="700")
    return pregunta(b, x, ty + 210, w, "Teniendo en cuenta lo anterior, ¿por qué ocurre esto?")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Flecha por flecha: la pelota del tubo", c,
                      "Como en el sifón: el principio explica lo que se ve. La segunda ley de Newton dice que la fuerza "
                      "neta va hacia donde se acelera el cuerpo.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 230, 150, c, r=12)
    b.append(f'<circle cx="{x0 + 115}" cy="{yy + 80}" r="22" fill="white" stroke="{INK}" stroke-width="2"/>')
    pista(b, x0 + 14, yy + 24, "dibuja sus dos fuerzas")
    half = (ww - 270) / 2
    caja_preg(b, x0 + 250, yy, half, 150, c, "LO QUE SE VE", "la pelota sube cada vez más rápido: acelera hacia…", 2)
    caja_preg(b, x0 + 270 + half, yy, half, 150, c, "LO QUE EXPLICA", "entonces la fuerza mayor es la de…", 2)
    return yy + 150


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="Una estudiante suelta varias veces una pelota de 5 kg de masa (pelota 1), desde la parte más alta de una "
            "rampa de 1,5 m de altura, para que choque elásticamente con una pelota de masa diferente (pelota 2), que "
            "inicialmente se encuentra en reposo, como se muestra en la figura.",
          o=["IV.", "III.", "II.", "I."], datos=datos_79, inst=ii1)
QB = dict(est=2, comp="Explicación de fenómenos",
          e="En una fiesta, un niño sostiene una piñata por medio de una cuerda que pasa por una polea, como muestra "
            "la figura.",
          o=["el peso de la piñata disminuye con la altura.", "el niño está ubicado debajo de la polea.",
             "la polea sostiene por sí sola el peso de la piñata.",
             "la fuerza que hace el niño es igual al peso de la piñata."],
          datos=datos_52, inst=ii2)
QC = dict(est=3, comp="Indagación",
          e="Un estudiante tenía algunos resortes y quería saber cuál de ellos era el más elástico. Para esto colgó una "
            "masa de 500 g a cada uno de los resortes y midió cuánto se estiraban. Un compañero de clase desea "
            "corroborar las medidas realizadas. Para esto, él vuelve a hacer mediciones asegurándose de",
          o=["usar la misma masa para probar todos los resortes.",
             "que todos los resortes terminen estirados la misma longitud.",
             "estirar todos los resortes al mismo tiempo.", "que todos los resortes tengan el mismo tamaño."],
          inst=ii3)
QD = dict(est=4, comp="Explicación de fenómenos",
          e="Un estudiante sopla una pelota por un tubo vertical y esta sube aceleradamente por el tubo, como se "
            "muestra en la siguiente figura:",
          o=["Porque el peso de la pelota cambia cuando el estudiante sopla aire por el tubo.",
             "Porque la fuerza que ejerce el aire que sopla el estudiante es igual que el peso de la pelota.",
             "Porque el peso de la pelota es mayor que la fuerza del aire que sopla el estudiante.",
             "Porque la fuerza que ejerce el aire que sopla el estudiante es mayor que el peso de la pelota."],
          datos=datos_26, inst=ii4)


def build(pages=(256, 260)):
    return [hoja_icfes("fis5_i1", pages[0], QA, QB),
            hoja_icfes("fis5_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
