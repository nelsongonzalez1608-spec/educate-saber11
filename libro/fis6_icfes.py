#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 6 · entrenamiento ICFES · páginas 263 y 267. Cierre del área.

Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · 2016-1, 1.ª ses. (AAM), CN, ítem 97 · B   (fuente de 12 V y cinco resistencias iguales)   estrategia 1
    QB · 2016-1, 2.ª ses. (ABD), CN, ítem 73 · C   (bombillo que se enciende un rato y se apaga)    estrategia 2
    QC · 2016-1, 2.ª ses. (ABD), CN, ítem 77 · D   (dos pelotas que rebotan distinto)               estrategia 3
    QD · cuadernillo nov 2025 / feb 2026, N.º 35 · B (curva de calentamiento de un sólido)          estrategia 4

  97 · B: toda la corriente de la fuente pasa por R1 (I1) y por R5 de vuelta (I4 = I1). En el nudo
       se divide entre R2 (I3) y la rama R3–R4–R5 (I2): I1 = I2 + I3, así que I2 e I3 son menores
       que I1. (Con R iguales: la rama de tres resistencias tiene 3R, I3 = 3·I2.) A (todas iguales),
       C (I1 menor) y D (I3 = I1) contradicen la regla del nudo. Verificada contra la página 29 del
       escaneo «2016-1 PRIMERA SESION.pdf» (encabezado «Saber 11 - 083 - B05R - AAM · 1a. sesión»).
       Circuito redibujado con la misma conexión. Nota: el texto del cuadernillo dice «cinco (5)
       resistencias (R) de igual valor».
  73 · C: en la posición 1 la fuente carga el elemento P; en la posición 2 la fuente queda fuera y
       el bombillo se enciende con la energía que P había guardado, hasta que se agota: un
       condensador («almacenar energía eléctrica», dice la tabla). Una resistencia o un cable no
       guardan energía (con la fuente fuera, el bombillo no prendería); un interruptor solo abre o
       cierra. Verificada contra la página 24 del escaneo «2016-2 SEGUNDA SESION.pdf» (encabezado
       «Saber 11 - 083 - B10O - ABD · 2a. sesión»; la portada dice 2016-1 segunda sesión). Tabla y
       circuito redibujados.
  77 · D: la prueba se hizo en césped (tenis) y asfalto (baloncesto); en el salón el piso es otro,
       así que no se repitieron las mismas condiciones experimentales. A y B (peso, material) son
       propiedades de las pelotas, que no cambiaron; C («todos deben rebotar distinto») no explica
       por qué cambió el resultado. Verificada contra la página 25 del mismo escaneo. Figura
       redibujada con las mismas alturas (2,0 m; 1,0 m y 1,5 m).
  35 · B: la curva tiene dos tramos planos, a 0 °C (fusión) y a 100 °C (ebullición): agua. Benceno
       (6 y 80), acetonitrilo (−45 y 82) y 2-butanol (−115 y 100) no tienen esas dos temperaturas.
       Cuadernillo oficial «Prueba Ciencias Naturales, Cuadernillo de preguntas Saber 11.º» (Icfes,
       nov 2025; el de feb 2026 trae las mismas 50 preguntas), pregunta 35, p. 25. Gráfica redibujada.

Reservadas en tablero/propuestas/fis_icfes_reservas.csv.
"""
from fis6 import *   # noqa: F401,F403  (configura la misión y EST)
from fis6 import rot, caja, pista, renglon, texto, sino, tinte, tabla_vacia, vector, caja_preg


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


def resistencia(b, cx, cy, horizontal=True, lab=None):
    if horizontal:
        b.append(rect(cx - 40, cy - 12, 80, 24, "white", r=0, stroke=INK, sw=2))
        if lab:
            texto(b, cx, cy - 20, lab, size=15, weight="700", anchor="middle")
    else:
        b.append(rect(cx - 12, cy - 40, 24, 80, "white", r=0, stroke=INK, sw=2))
        if lab:
            texto(b, cx - 22, cy + 6, lab, size=15, weight="700", anchor="end")


# ───────── QA · ítem 97 · cinco resistencias ─────────
def datos_97(b, x, y, w):
    L, R, Mx, top, bot = x + 120, x + 600, x + 360, y + 40, y + 210
    b.append(line(L, top, R, top, INK, 2))
    b.append(line(L, bot, R, bot, INK, 2))
    b.append(line(Mx, top, Mx, bot, INK, 2))
    b.append(line(R, top, R, bot, INK, 2))
    b.append(line(L, top, L, top + 60, INK, 2))
    b.append(line(L, top + 110, L, bot, INK, 2))
    b.append(line(L - 22, top + 60, L + 22, top + 60, INK, 3))
    b.append(line(L - 12, top + 76, L + 12, top + 76, INK, 3))
    b.append(line(L, top + 76, L, top + 110, INK, 2))
    texto(b, L - 30, top + 70, "12 V", size=15, weight="700", anchor="end")
    texto(b, L + 16, top + 54, "+", size=15, weight="700")
    for cx, cy, hz, lab in (((L + Mx) / 2, top, True, "R1"), ((Mx + R) / 2, top, True, "R3"),
                            (Mx, (top + bot) / 2, False, "R2"), (R, (top + bot) / 2, False, "R4"),
                            ((Mx + R) / 2, bot, True, "R5")):
        b.append(rect(cx - 42, cy - 14, 84, 28, "white", r=0) if hz else rect(cx - 14, cy - 42, 28, 84, "white", r=0))
        resistencia(b, cx, cy, hz, lab)
    for x1, y1, x2, y2, lab, lx, ly in (((L + Mx) / 2 - 40, top + 26, (L + Mx) / 2 + 30, top + 26, "I1", (L + Mx) / 2 - 10, top + 52),
                                        ((Mx + R) / 2 - 40, top + 26, (Mx + R) / 2 + 30, top + 26, "I2", (Mx + R) / 2 - 10, top + 52),
                                        (Mx + 30, (top + bot) / 2 - 30, Mx + 30, (top + bot) / 2 + 30, "I3", Mx + 46, (top + bot) / 2 + 6),
                                        (L + 120, bot - 24, L + 50, bot - 24, "I4", L + 80, bot - 34)):
        vector(b, x1, y1, x2, y2, INK, sw=2, head=8)
        texto(b, lx, ly, lab, size=15, weight="700")
    return pregunta(b, x, bot + 16, w, "Según lo que se puede observar en la figura, sobre los valores de las "
                                       "corrientes (I) es correcto afirmar que")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Sigue la corriente desde la pila", c,
                      "Como en el cruce de la pregunta 9 del taller: lo que llega a un nudo sale repartido. Pon el signo "
                      "que corresponde (=, < o >) en cada relación.")
    x0, ww = x + 22, w - 44
    rel = ("I1  ___  I2 + I3", "I2  ___  I1", "I3  ___  I1", "I4  ___  I1")
    cw = (ww - 3 * 16) / 4
    for k, r_ in enumerate(rel):
        bx = x0 + k * (cw + 16)
        caja(b, bx, yy, cw, 84, c, r=12)
        texto(b, bx + cw / 2, yy + 50, r_, size=19, weight="700", anchor="middle")
    return yy + 84


# ───────── QB · ítem 73 · condensador ─────────
def datos_73(b, x, y, w):
    cols = ((170, "Nombre"), (420, "Función"))
    filas = (("Resistencia", "Generar una resistencia al paso de corriente"), ("Condensador", "Almacenar energía eléctrica"),
             ("Cable", "Conducir corriente eléctrica"), ("Interruptor", "Desviar o interrumpir el curso de la corriente"))
    yy = tabla(b, x, y + 4, cols, filas, rh=32, head_h=34, size=15)
    # circuito
    cx0 = x + 660
    L, R, top, bot = cx0, cx0 + 480, y + 40, y + 160
    b.append(line(L, top, L + 120, top, INK, 2))
    b.append(f'<circle cx="{L + 140}" cy="{top}" r="18" fill="#FFF4C8" stroke="{INK}" stroke-width="2"/>')
    texto(b, L + 140, top - 26, "bombillo", size=14, anchor="middle")
    b.append(line(L + 158, top, L + 240, top, INK, 2))
    b.append(rect(L + 240, top - 16, 120, 32, "white", r=0, stroke=INK, sw=2))
    texto(b, L + 300, top + 6, "P", size=17, weight="700", anchor="middle")
    b.append(line(L + 360, top, R, top, INK, 2))
    b.append(line(R, top, R, bot, INK, 2))
    b.append(line(R, bot, L + 120, bot, INK, 2))
    b.append(f'<circle cx="{L + 120}" cy="{bot}" r="6" fill="white" stroke="{INK}" stroke-width="2"/>')
    b.append(line(L + 120, bot, L + 72, bot + 22, INK, 2.6))
    b.append(f'<circle cx="{L + 64}" cy="{bot - 28}" r="6" fill="white" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<circle cx="{L + 64}" cy="{bot + 26}" r="6" fill="white" stroke="{INK}" stroke-width="2"/>')
    texto(b, L + 84, bot - 36, "2", size=15, weight="700")
    texto(b, L + 82, bot + 44, "1", size=15, weight="700")
    texto(b, L + 132, bot + 24, "interruptor", size=14)
    b.append(line(L, top, L, bot - 28, INK, 2))
    b.append(line(L, bot - 28, L + 58, bot - 28, INK, 2))
    b.append(line(L, bot - 28, L, bot + 60, INK, 2))
    b.append(line(L - 18, bot + 60, L + 18, bot + 60, INK, 3))
    b.append(line(L - 10, bot + 72, L + 10, bot + 72, INK, 3))
    b.append(line(L, bot + 72, L, bot + 90, INK, 2))
    b.append(line(L, bot + 90, L + 64, bot + 90, INK, 2))
    b.append(line(L + 64, bot + 90, L + 64, bot + 32, INK, 2))
    texto(b, L - 26, bot + 72, "fuente", size=14, anchor="end")
    yy = max(yy, bot + 96)
    return pregunta(b, x, yy + 4, w, "Al pasar el interruptor de la posición 1 a la posición 2, el bombillo se "
                                     "enciende durante un tiempo y luego se apaga. ¿Qué dispositivo debe colocarse "
                                     "en el punto P para que esto ocurra?")


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Posición 1, posición 2: ¿de dónde sale la luz?", c,
                      "Como en el molinillo: si algo sigue funcionando sin fuente, la energía tuvo que quedar guardada "
                      "en alguna parte. Sigue el camino de la corriente en cada posición.")
    x0, ww = x + 22, w - 44
    cols = (220, (ww - 220) / 2, (ww - 220) / 2)
    return tabla_vacia(b, x0, yy, cols, ("", "¿LA FUENTE ESTÁ EN EL CIRCUITO?", "¿DE DÓNDE SALE LA ENERGÍA?"),
                       ("Posición 1", "Posición 2"), c, rh=50, hh=34, size=16)


# ───────── QC · ítem 77 · rebotes ─────────
def datos_77(b, x, y, w):
    yy = pregunta(b, x, y, w - 470, "Cuando el estudiante va al salón de clases e intenta mostrarle el rebote de las "
                                    "pelotas a sus compañeros, no obtiene los mismos resultados. ¿Por qué el "
                                    "estudiante no obtuvo los mismos resultados?")
    fx = x + w - 440
    for k, (lab, hh_, piso, r_) in enumerate((("tenis", 1.0, "césped", 10), ("baloncesto", 1.5, "asfalto", 22))):
        bx = fx + k * 220
        base = y + 220
        b.append(rect(bx, base, 180, 16, "#C9D7B8" if k == 0 else "#B8BCC4", r=0, stroke=INK, sw=1.4))
        texto(b, bx + 90, base + 38, piso, size=14, anchor="middle")
        top = base - hh_ / 1.6 * 180
        b.append(line(bx + 120, base, bx + 120, top, INK, 1.8))
        b.append(line(bx + 112, top, bx + 128, top, INK, 1.8))
        texto(b, bx + 132, (base + top) / 2, f"{hh_:.1f} m".replace(".", ","), size=14)
        b.append(f'<circle cx="{bx + 60}" cy="{top - r_ - 4}" r="{r_}" fill="white" stroke="{INK}" stroke-width="2"/>')
        texto(b, bx + 60, top - 2 * r_ - 14, lab, size=14, anchor="middle")
    return max(yy, y + 270)


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Lo que cambió entre la cancha y el salón", c,
                      "Como con el motor de una sola hora: un resultado vale para las condiciones en que se obtuvo. "
                      "Escribe qué tenía cada prueba y qué tenía la del salón.")
    x0, ww = x + 22, w - 44
    cols = (230, (ww - 230) / 3, (ww - 230) / 3, (ww - 230) / 3)
    return tabla_vacia(b, x0, yy, cols, ("", "PISO", "ALTURA DE LANZAMIENTO", "¿LA MISMA PELOTA?"),
                       ("En la prueba", "En el salón"), c, rh=50, hh=34, size=16)


# ───────── QD · pregunta 35 · curva de calentamiento ─────────
def datos_35(b, x, y, w):
    gx, gy, gw, gh = x + 70, y + 10, 420, 220
    b.append(line(gx, gy, gx, gy + gh, INK, 2))
    b.append(line(gx, gy + gh, gx + gw, gy + gh, INK, 2))
    tmin, tmax = -40, 140
    Y = lambda t: gy + gh - (t - tmin) / (tmax - tmin) * gh
    for t in range(-40, 141, 20):
        b.append(line(gx - 5, Y(t), gx + 5, Y(t), INK, 1.6))
        texto(b, gx - 10, Y(t) + 5, str(t).replace("-", "−"), size=13, color=GRAY, anchor="end")
    for t in (0, 100):
        b.append(line(gx, Y(t), gx + gw, Y(t), GRAY, 1.4, "5,5"))
    pts = ((0, -40), (50, 0), (95, 0), (230, 100), (330, 100), (370, 140))
    b.append('<polyline points="' + " ".join(f"{gx + px:.1f},{Y(t):.1f}" for px, t in pts) +
             f'" fill="none" stroke="{INK}" stroke-width="3"/>')
    texto(b, gx + 60, Y(-30), "Sólido", size=14, weight="700")
    texto(b, gx + 170, Y(40), "Líquido", size=14, weight="700")
    texto(b, gx + 330, Y(125), "Gas", size=14, weight="700")
    b.append(T(x + 18, gy + gh / 2, ["Temperatura (°C)"], 14, GRAY, style="italic", anchor="middle", rot=-90))
    texto(b, gx + gw / 2, gy + gh + 26, "Tiempo", size=14, color=GRAY, anchor="middle")
    yy = pregunta(b, x + 540, y, w - 540, "Para identificar el sólido se cuenta con los datos de la tabla.")
    cols = ((180, "Sustancia"), (250, "Fusión (°C)"), (250, "Ebullición (°C)"))
    tabla(b, x + 540, yy + 8, cols, (("Benceno", "6", "80"), ("Agua", "0", "100"), ("Acetonitrilo", "−45", "82"),
                                     ("2-butanol", "−115", "100")), rh=32, head_h=34, size=15)
    return pregunta(b, x, gy + gh + 34, w, "Teniendo en cuenta la información anterior, ¿a qué sustancia corresponde "
                                           "el sólido inicial?")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Las dos mesetas de la curva", c,
                      "Como con el agua que se enfría hasta la temperatura de la sala: cuando la temperatura deja de "
                      "cambiar, la energía que entra se está usando en otra cosa. Lee las mesetas.")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    caja_preg(b, x0, yy, half, 110, c, "PRIMERA MESETA", "a ____ °C · ahí el sólido se…")
    caja_preg(b, x0 + half + 24, yy, half, 110, c, "SEGUNDA MESETA", "a ____ °C · ahí el líquido se…")
    return yy + 110


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="Un circuito se compone de una fuente de voltaje (12 V) y de cinco (5) resistencias (R) de igual valor, "
            "conectadas como se muestra en la siguiente figura.",
          o=["las corrientes I1, I2, I3 e I4 son iguales, porque estas corrientes se encuentran en el mismo circuito.",
             "las corrientes I2 e I3 son menores que I1, porque I1 se divide en I2 e I3.",
             "la corriente I1 es menor que I2 e I3, porque solo fluye a través de una resistencia.",
             "la corriente I3 es igual a la corriente I1, porque tanto I3 como I1 fluyen por una sola resistencia."],
          datos=datos_97, inst=ii1)
QB = dict(est=2, comp="Explicación de fenómenos",
          e="A continuación se presentan los nombres y las funciones de algunos dispositivos que pueden utilizarse en "
            "el circuito de la derecha.",
          o=["Una resistencia.", "Un cable.", "Un condensador.", "Un interruptor."], datos=datos_73, inst=ii2)
QC = dict(est=3, comp="Indagación",
          e="Un niño quiere ver qué pelota rebota más, una de tenis o una de baloncesto. Ambas se lanzan desde una "
            "altura de 2,0 m. La pelota de tenis lanzada sobre una cancha de césped rebotó 1,0 m; y la pelota de "
            "baloncesto, en una cancha de asfalto rebotó 1,5 m (ver figura).",
          o=["Porque no se tuvo en cuenta el peso de cada una de las pelotas.",
             "Porque no se tuvo en cuenta el material de cada una de las pelotas.",
             "Porque todos los objetos deben de rebotar de manera diferente.",
             "Porque no se tuvieron las mismas condiciones experimentales."],
          datos=datos_77, inst=ii3)
QD = dict(est=4, comp="Uso comprensivo del conocimiento científico",
          e="En un experimento, un sólido de identidad desconocida se calienta y se mide su temperatura hasta que se "
            "evapora, obteniendo la siguiente gráfica.",
          o=["Benceno.", "Agua.", "Acetonitrilo.", "2-butanol."], datos=datos_35, inst=ii4)


def build(pages=(263, 267)):
    return [hoja_icfes("fis6_i1", pages[0], QA, QB),
            hoja_icfes("fis6_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
