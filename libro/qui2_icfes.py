#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 2 · entrenamiento ICFES · páginas 192 y 196.

Cuatro preguntas de Ciencias Naturales con contenido fisicoquímico (calor, cambios de estado y
densidad), de tres fuentes en Drive:
  · «1. CUADERNILLOS ICFES» / «2016-1 PRIMERA SESION.pdf»: cuadernillo oficial Saber 11 2016-1,
    primera sesión, AAM; encabezado «Saber 11 - 083 - B05R - AAM · 1a. sesión». Ítem 112.
  · «1. CUADERNILLOS ICFES» / «2016-2 SEGUNDA SESION.pdf»: cuadernillo oficial 2016-1, segunda
    sesión, ABD; encabezado «Saber 11 - 083 - P4 - ABD · 2a. sesión» en esa página. Ítem 76.
  · «SIMULACRO II 2023-OFICIO-C.NATURALES - química.pdf» (simulacro de seguimiento; CLAUDE.md § 10
    lo lista entre las fuentes): ítems 67 y 64. NO verificados contra un cuadernillo liberado
    del ICFES (el PDF pesa 30 MB; solo se leyó su texto, donde estos dos ítems traen sus letras).
Ninguna estaba en tablero/icfes.csv; reservadas en tablero/propuestas/qui_icfes_reservas.csv.
Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · Sim. II 2023 N.º 67 · B (las observaciones son evidencia de que se funden con el calor)  est. 1
    QB · 1.ª ses. N.º 112 · A   (el calor convierte el agua en vapor)                          est. 2
    QC · 2.ª ses. N.º 76 · C    (enfría rápido al principio y cada vez más despacio)           est. 3
    QD · Sim. II 2023 N.º 64 · A (el hielo es menos denso: espacios vacíos entre moléculas)    est. 4

  67 · El alumno registró tiempo y estado final; nunca midió temperaturas. A y C afirman cosas
       sobre la temperatura o el momento del cambio que la tabla no trae; D habla de puntos de
       fusión que no se midieron. B solo dice lo que se observó.
  76 · Con 80 °C de diferencia al empezar, el flujo de calor es el mayor: la caída más empinada
       está al principio y se suaviza al acercarse a 20 °C. A y B empiezan suaves (al revés); D
       es una recta (rapidez constante). C. Las cuatro gráficas se redibujaron con la misma forma.
  64 · 1 g de hielo ocupa 1 ÷ 0,917 ≈ 1,09 mL; 1 g de agua líquida ≈ 1,00 mL. Menos densidad
       porque la red del hielo deja huecos (A). C acierta en «menor» pero da otra razón.
"""
from qui2 import *   # noqa: F401,F403  (configura la misión y EST)
from qui2 import rot, caja, pista, texto, renglon, hueco, frase_hueco, flecha, marca, ejes, curva, particula


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · Sim. II 2023 N.º 67 · dos sustancias fundidas ─────────
def datos_67(b, x, y, w):
    c = A["color"]
    ws = (180, 160, 420)
    yy = y + 8
    for k, cl in enumerate(("Sustancia", "Tiempo", "Observación final")):
        b.append(rect(x + sum(ws[:k]), yy, ws[k], 32, A["bg"], r=0, stroke=c, sw=1.4))
        b.append(T(x + sum(ws[:k]) + ws[k] / 2, yy + 22, [cl], 15, INK, weight="700", anchor="middle"))
    yy += 32
    for fila in (("1", "50", "Pasa de estado sólido a líquido."), ("2", "163", "Pasa de estado sólido a líquido.")):
        for k, v in enumerate(fila):
            b.append(rect(x + sum(ws[:k]), yy, ws[k], 30, "white", r=0, stroke=c, sw=1.4))
            b.append(T(x + sum(ws[:k]) + ws[k] / 2, yy + 21, [v], 15, INK, anchor="middle"))
        yy += 30
    return pregunta(b, x, yy + 2, w, "Las observaciones realizadas por el estudiante se pueden considerar")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Lo que el alumno anotó y lo que nunca midió", c,
                      "Como en la pregunta 1: antes de hablar de temperaturas, mira si alguien las midió. Una "
                      "evidencia es lo que se vio o se midió; una conclusión es lo que se afirma a partir de ella.")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("LO QUE ANOTÓ", "las dos columnas de su tabla"),
                                  ("LO QUE NO MIDIÓ", "y que una conclusión sobre fusión necesitaría"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 120, c, r=14, dash="8,6" if k else None)
        rot(b, bx + 18, yy + 28, rt, c, size=13)
        pista(b, bx + 18, yy + 52, ps, size=14)
        renglon(b, bx + 18, yy + 86, bx + half - 18)
        renglon(b, bx + 18, yy + 112, bx + half - 18)
    yy += 136
    return frase_hueco(b, x0, yy, ww, "Una opción que afirma algo de la columna derecha es ______________ ; "
                                      "una que solo dice lo de la izquierda es ______________ .", c)


# ───────── QB · 1.ª sesión N.º 112 · la plancha ─────────
def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "La energía de la plancha, eslabón por eslabón", c,
                      "Sigue la energía desde el enchufe hasta la tela, como seguiste el calor de la parafina por "
                      "tramos. Cada eslabón dice qué le pasa al agua del tanque.")
    x0, ww = x + 22, w - 44
    n, gap = 4, 40
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("1 · ENTRA", "energía eléctrica"), ("2 · SE VUELVE", "en la resistencia"),
                                  ("3 · EL AGUA DEL TANQUE", "sube su temperatura y…"),
                                  ("4 · SALE Y LLEGA A LA TELA", "¿en qué estado?"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 130, c, r=14)
        rot(b, bx + 16, yy + 26, rt, c, size=13)
        pista(b, bx + 16, yy + 50, ps, size=14)
        if k:
            renglon(b, bx + 16, yy + 88, bx + bw - 16)
            renglon(b, bx + 16, yy + 118, bx + bw - 16)
        if k < n - 1:
            flecha(b, bx + bw + 4, yy + 64, bx + bw + gap - 4, yy + 64, c, sw=3, head=12)
    yy += 146
    return frase_hueco(b, x0, yy, ww, "En la curva de la pregunta 2, el agua que sale como vapor ya pasó por el "
                                      "tramo ______ (el de la meseta).", c)


# ───────── QC · 2.ª sesión N.º 76 · enfriamiento de Newton ─────────
def _mini(b, x, y, w, h, L, forma):
    gx, gy, gw, gh = x + 44, y + 34, w - 58, h - 64
    b.append(T(x, y + 16, [L + "."], 18, INK, weight="700"))
    ejes(b, gx, gy, gw, gh, "tiempo", "",
         yt=[(t / 120, str(t)) for t in range(0, 121, 20)])
    b.append(T(gx + 10, y + 16, ["temperatura (°C)"], 13, GRAY, style="italic"))

    def P(f, temp):
        return gx + f * gw, gy + gh - temp / 120 * gh
    pts = []
    for i in range(101):
        f = i / 100
        if forma == "A":
            temp = 20 + 80 * max(0.0, 1 - (f / 0.68) ** 2) if f < 0.68 else 20
        elif forma == "B":
            temp = 20 + 80 * (1 / (1 + math.exp((f - 0.25) / 0.06))) / (1 / (1 + math.exp(-0.25 / 0.06)))
        elif forma == "C":
            temp = 20 + 80 * math.exp(-f / 0.05)
        else:
            temp = 100 - 80 * f / 0.55 if f < 0.55 else 20
        pts.append(P(f, temp))
    curva(b, pts, INK, sw=2.6)


def datos_76(b, x, y, w):
    gw, gh = (w - 30) / 4, 190
    for k, L in enumerate("ABCD"):
        _mini(b, x + k * (gw + 10), y + 8, gw, gh, L, L)
    return y + 8 + gh + 4


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "La diferencia de temperatura manda la rapidez", c,
                      "Lo mismo que el baño de la pregunta 6: mientras más diferencia, más flujo de calor. Calcula la "
                      "diferencia en tres momentos y decide cómo debe verse la curva en cada uno.")
    x0, ww = x + 22, w - 44
    cols = ("EL AGUA ESTÁ A", "DIFERENCIA CON EL AMBIENTE (20 °C)", "SE ENFRÍA")
    xs = (0, 260, 760)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=13)
    for j, t in enumerate(("100 °C (al empezar)", "60 °C (a mitad)", "25 °C (casi al final)")):
        ry = yy + 26 + j * 50
        caja(b, x0, ry, ww, 42, c, r=8)
        texto(b, x0 + 16, ry + 28, t, 16)
        texto(b, x0 + xs[1], ry + 28, "____ − 20 = ____ °C", 16)
        marca(b, x0 + xs[2], ry + 10, "rápido", c)
        marca(b, x0 + xs[2] + 130, ry + 10, "medio", c)
        marca(b, x0 + xs[2] + 250, ry + 10, "lento", c)
    yy += 26 + 3 * 50 + 6
    return frase_hueco(b, x0, yy, ww, "La curva debe empezar ____________ (empinada / suave) y terminar "
                                      "____________ .", c)


# ───────── QD · Sim. II 2023 N.º 64 · el hielo flota ─────────
def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Un kilo de hielo no cabe en un litro", c,
                      "La misma masa de agua, en dos estados. Calcula cuánto espacio ocupa cada una con V = m ÷ d y "
                      "piensa qué hay en el espacio que sobra.")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    for k, (rt, d) in enumerate((("AGUA LÍQUIDA · d = 1,00 g/mL", "1 000 g ÷ 1,00 g/mL = ________ mL"),
                                 ("HIELO · d = 0,917 g/mL", "1 000 g ÷ 0,917 g/mL = ________ mL"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 92, c, r=14)
        rot(b, bx + 18, yy + 28, rt, c, size=13)
        texto(b, bx + 18, yy + 70, d, 18)
    yy += 108
    return frase_hueco(b, x0, yy, ww, "Misma masa y más volumen: entre las moléculas del hielo queda ______________ .", c)


QA = dict(est=1, comp="Indagación",
          e="Un alumno fundió dos sustancias puras con la intención de saber cuál de ellas cambia de estado más "
            "rápidamente. Metió un trozo de cada sustancia en un recipiente de vidrio, los calentó con un mechero, y "
            "midió el tiempo que tardaron en cambiar de estado. Los resultados se muestran a continuación.",
          o=["una conclusión, porque las dos sustancias empiezan a cambiar de estado a los 50 segundos.",
             "una evidencia de que las sustancias se funden por efecto de la temperatura.",
             "una conclusión, porque los cambios de estado se dan a la misma temperatura.",
             "una evidencia de que las sustancias tienen puntos de fusión cercanos."],
          datos=datos_67, inst=ii1)
QB = dict(est=2, comp="Explicación de fenómenos",
          e="Algunas planchas almacenan agua en un tanque y transforman energía eléctrica en calor. Esta "
            "transformación de energía permite",
          o=["que se produzca vapor y este ayude en la eliminación de arrugas.",
             "que la plancha se haga más pesada y este peso elimine las arrugas.",
             "que el aire que circula entre la plancha y la ropa elimine las arrugas.",
             "que el agua del tanque permanezca líquida y elimine las arrugas."],
          inst=ii2)
QC = dict(est=3, comp="Uso comprensivo del conocimiento científico",
          e="Juan calienta una gran cantidad de agua en una olla. Al retirarla del fuego, la temperatura del agua se "
            "mide con un termómetro y este indica 100 °C. Juan mide la temperatura del ambiente obteniendo 20 °C. La "
            "ley de enfriamiento de Newton establece que cuanto mayor es la diferencia de temperatura entre un objeto "
            "y el ambiente, mayor es el flujo de calor y, por tanto, más rápido se enfría el objeto. Teniendo en "
            "cuenta la información anterior, ¿cuál de las siguientes gráficas describe mejor el proceso de "
            "enfriamiento del agua en la olla?",
          o=[], datos=datos_76, inst=ii3)
QD = dict(est=4, comp="Explicación de fenómenos",
          e="Cuando se congela el agua, flota sobre el agua líquida como ocurre en los casquetes glaciares; esto "
            "sucede porque el agua sólida presenta una densidad",
          o=["menor que en estado líquido, porque en estado sólido se generan espacios vacíos entre las moléculas.",
             "mayor que en estado líquido, porque en este estado líquido las moléculas de agua se encuentran más "
             "cercanas.",
             "menor que en estado líquido, porque en estado sólido las fuerzas de atracción entre las moléculas son "
             "mayores.",
             "mayor que en estado líquido, porque en estado sólido las moléculas de agua se atraen débilmente entre sí."],
          inst=ii4)


def build(pages=(192, 196)):
    return [hoja_icfes("qui2_i1", pages[0], QA, QB),
            hoja_icfes("qui2_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
