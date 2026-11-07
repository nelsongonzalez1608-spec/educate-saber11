#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 4 · entrenamiento ICFES · páginas 206 y 210.

Las cuatro preguntas salen de los cuadernillos oficiales Saber 11 2016-1 que están en Drive
(carpeta «1. CUADERNILLOS ICFES»), sección Ciencias Naturales, verificadas contra la página
escaneada:
  · «2016-1 PRIMERA SESION.pdf» — 1.ª sesión, cuadernillo AAM (encabezado «Saber 11 - 083 -
    B05R - AAM · 1a. sesión»), ítems 92 (p. 28) y 104 (p. 32).
  · «2016-2 SEGUNDA SESION.pdf» — en la portada dice 2016-1, 2.ª sesión, cuadernillo ABD
    (encabezado «Saber 11 - 083 - B10O - ABD · 2a. sesión»), ítems 54 (p. 17) y 71 (p. 23).
Ninguna estaba en tablero/icfes.csv; las cuatro se reservaron en
tablero/propuestas/qui_icfes_reservas.csv. Ninguna nombra a un político. Las tablas se
redibujaron con los mismos datos; las cuatro figuras de vasos del 104, los objetos y el esquema
del carro del 54 se redibujaron con lo mismo que muestra el escaneo.

Membrete: siempre «Pregunta oficial ICFES · Saber 11» (el motor lo impone).

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · 2.ª ses. N.º 71  · C   (alcohol y éter C2H6O: puntos de ebullición y fusión)   estrategia 1
    QB · 1.ª ses. N.º 104 · A   (corcho de 0,95 g/cm³ en tres líquidos)                 estrategia 2
    QC · 1.ª ses. N.º 92  · B   (títulos de las columnas 2 y 5)                          estrategia 3
    QD · 2.ª ses. N.º 54  · A   (qué objeto mueve el carro con el imán)                  estrategia 4

Cuentas y razones:
  QA · Mismo peso molecular (46 g/mol); lo único distinto son las fuerzas intermoleculares
       (fuertes en el alcohol). Más fuerza → más energía para cualquier cambio de estado → el
       alcohol tiene mayor punto de ebullición Y de fusión → C. (Datos reales: etanol −114 °C y
       78 °C; dimetiléter −141 °C y −24 °C.)
  QB · El corcho (0,95) flota donde el líquido es más denso: agua 1,00 y cloroformo 1,48 → flota;
       acetona 0,79 → se hunde → A (acetona al fondo, agua y cloroformo flotando).
  QC · Columna 2 = volumen × densidad: 1,8 × 1 = 1,8; 1,5 × 0,8 = 1,2; 1 × 1,12 = 1,12;
       2 × 2,7 = 5,4 → masa en gramos. Columna 5: el agua tiene 100 → punto de ebullición en °C
       → B. A y C las invierten; D les cambia las unidades.
  QD · El imán atrae materiales magnéticos (hierro); la puntilla es de hierro → A. B y C dan
       objetos que no son magnéticos «porque no lo son»; D le atribuye magnetismo al borrador.
"""
from qui4 import *   # noqa: F401,F403  (configura la misión y EST)
from qui4 import rot, caja, pista, renglon, frase_hueco, letra, casillas, tabla, si_no, hueco


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


def tabla_datos(b, x, y, cols, filas, hh=34, rh=30):
    px = x
    for t, cw in cols:
        celda(b, px, y, cw, hh, t, bold=True, fill=SOFT)
        px += cw
    y += hh
    for f in filas:
        px = x
        for (t, cw), v in zip(cols, f):
            celda(b, px, y, cw, rh, v)
            px += cw
        y += rh
    return y


def caja_num(b, x, y, c, w=90, h=38):
    caja(b, x, y, w, h, c, r=8)
    return x + w


# ───────── QA · N.º 71 · alcohol y éter ─────────
def datos_71(b, x, y, w):
    cols = (("Compuesto", 300), ("Peso molecular (g/mol)", 260), ("Tipo de fuerzas intermoleculares", 330))
    yy = tabla_datos(b, x + 30, y + 4, cols, (("Alcohol: CH₃-CH₂-OH", "46", "Fuertes"),
                                              ("Éter: CH₃-O-CH₃", "46", "Débiles")), rh=34)
    return pregunta(b, x, yy + 4, w, "Teniendo en cuenta la anterior información, ¿cómo debe ser el punto de "
                                     "ebullición y de fusión de estos dos compuestos?")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Mismo peso, distinta fuerza", c,
                      "Lo de los bloques de barro: busca lo único distinto. Escribe qué tienen igual y qué tienen "
                      "distinto las dos moléculas, y sigue la cadena hasta los dos cambios de estado.")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("LO QUE TIENEN IGUAL", "fórmula y peso molecular"),
                                  ("LO ÚNICO DISTINTO", "y quién lo tiene más fuerte"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 86, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        pista(b, px + 260, yy + 28, ps)
        renglon(b, px + 18, yy + 70, px + half - 18)
    yy += 102
    pasos = ("fuerzas más fuertes", "se necesita ______ energía", "para fundirse: temperatura más ______",
             "para hervir: temperatura más ______")
    bw = (ww - 3 * 40) / 4
    for k, t in enumerate(pasos):
        px = x0 + k * (bw + 40)
        caja(b, px, yy, bw, 60, c, r=30, fill=A["bg"] if k == 0 else "white")
        svg, _ = TJ(px + 16, yy + 24, t, bw - 32, 15, INK, lh=19)
        b.append(svg)
        if k < 3:
            b.append(hand_arrow(px + bw + 4, yy + 30, px + bw + 36, yy + 30, c, sw=2.4, bend=0.0, head=10))
    return yy + 76


# ───────── QB · N.º 104 · el corcho en tres líquidos ─────────
def _vaso_corcho(b, cx, by, flota):
    w, h = 74, 84
    x0 = cx - w / 2
    b.append(f'<path d="M {x0} {by - h} L {x0 + 8} {by} L {x0 + w - 8} {by} L {x0 + w} {by - h}" fill="none" '
             f'stroke="{INK}" stroke-width="2"/>')
    ly = by - h + 22
    b.append(line(x0 + 3, ly, x0 + w - 3, ly, INK, 1.6))
    cy = ly - 2 if flota else by - 12
    b.append(rect(cx - 13, cy - 8, 26, 16, "#E9D5B0", r=4, stroke=INK, sw=1.6))


def datos_104(b, x, y, w):
    c = A["color"]
    cols = (("Líquido", 220), ("Punto de ebullición (°C)", 260), ("Densidad (g/cm³)", 220))
    yy = tabla_datos(b, x + 30, y + 4, cols, (("Acetona", "56,3", "0,79"), ("Agua", "100,0", "1,00"),
                                              ("Cloroformo", "61,0", "1,48")), rh=28)
    yy = pregunta(b, x, yy + 2, w, "El estudiante introduce un corcho cuya densidad es 0,95 g/cm³ en cada uno de los "
                                   "líquidos. La figura que mejor representa la situación que observará el estudiante "
                                   "es")
    figs = (("A", (False, True, True)), ("B", (True, True, True)), ("C", (False, False, False)),
            ("D", (True, False, False)))
    gw = (w - 40) / 2
    for k, (L, fl) in enumerate(figs):
        fx = x + (k % 2) * (gw + 40)
        fy = yy + 14 + (k // 2) * 140
        letra(b, fx + 16, fy + 18, L, c)
        for j, (n, f) in enumerate(zip(("Acetona", "Agua", "Cloroformo"), fl)):
            cx = fx + 120 + j * 150
            _vaso_corcho(b, cx, fy + 100, f)
            b.append(T(cx, fy + 122, [n], 14, INK, anchor="middle"))
    return yy + 14 + 2 * 140


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "El corcho en la regla de densidades", c,
                      "Lo de los tres polvos: ¿se hunde, flota o se queda? Pon los tres líquidos y el corcho en la "
                      "regla (sus iniciales encima). Lo que queda a la derecha del corcho es más denso que él.")
    x0, ww = x + 22, w - 44
    ly = yy + 56
    L, R = x0 + 40, x0 + ww - 40
    b.append(line(L, ly, R, ly, INK, 2.6))
    for k in range(11):
        v = 0.6 + k * 0.1
        px = L + k / 10 * (R - L)
        b.append(line(px, ly - 9, px, ly + 9, INK, 2))
        b.append(T(px, ly + 30, [f"{v:.1f}".replace(".", ",")], 14, GRAY, anchor="middle"))
    pista(b, R, ly + 54, "g/cm³", anchor="end")
    yy = ly + 64
    return frase_hueco(b, x0, yy, ww, "El corcho se hunde en el líquido que es ______ denso que él; flota en "
                                      "______________ .", c)


# ───────── QC · N.º 92 · las columnas sin nombre ─────────
FILAS_92 = (("Agua", "1,8", "1,8", "1", "100"), ("Alcohol etílico", "1,2", "1,5", "0,8", "80"),
            ("Ácido clorhídrico", "1,12", "1", "1,12", "48"), ("Ácido sulfúrico", "5,4", "2", "2,7", "337"))


def datos_92(b, x, y, w):
    cols = (("Sustancia", 230), ("?", 110), ("Volumen (mL)", 170), ("Densidad (g/mL)", 190), ("?", 110))
    yy = tabla_datos(b, x + 30, y + 4, cols, FILAS_92, rh=28)
    return pregunta(b, x, yy + 4, w, "El estudiante olvida colocar el nombre de las columnas 2 y 5. Teniendo en "
                                     "cuenta los valores de los cuatro líquidos en estas columnas, ¿cuáles son los "
                                     "títulos correctos para las columnas?")


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Multiplica y compara: ¿qué columna es?", c,
                      "Lo de la pintura y los granos: ponle nombre a la propiedad. La densidad es masa dividida "
                      "entre volumen; entonces volumen × densidad te da otra propiedad. Haz la cuenta y busca en qué "
                      "columna aparece.")
    x0, ww = x + 22, w - 44
    nombres = ("Agua", "Alcohol", "Á. clorhídrico", "Á. sulfúrico")
    cw = (ww - 3 * 20) / 4
    for k, n in enumerate(nombres):
        px = x0 + k * (cw + 20)
        caja(b, px, yy, cw, 72, c, r=12)
        rot(b, px + 14, yy + 24, n.upper(), c, size=13)
        b.append(T(px + 14, yy + 56, ["volumen × densidad ="], 15, INK))
        caja(b, px + 14 + tw("volumen × densidad =", 15) + 8, yy + 34, cw - 28 - tw("volumen × densidad =", 15) - 8,
             30, c, r=6)
    yy += 88
    caja(b, x0, yy, ww, 52, c, r=12)
    b.append(T(x0 + 18, yy + 33, ["En la columna 5, el agua tiene 100. ¿Qué propiedad del agua vale 100, y en qué "
                                  "unidad?"], 16, INK))
    renglon(b, x0 + 760, yy + 38, x0 + ww - 18)
    yy += 66
    return frase_hueco(b, x0, yy, ww, "Columna 2: ______________ en ______ · Columna 5: ______________ en ______", c)


# ───────── QD · N.º 54 · el imán y el carro ─────────
def datos_54(b, x, y, w):
    c = INK
    yy = y + 6
    objs = ("Borrador", "Tapa de esfero", "Pimpón", "Puntilla")
    for k, n in enumerate(objs):
        cx = x + 90 + k * 200
        if k == 0:
            b.append(rect(cx - 36, yy + 6, 72, 34, "white", r=4, stroke=c, sw=1.8))
        elif k == 1:
            b.append(rect(cx - 44, yy + 16, 88, 14, "#B9BEC8", r=6, stroke=c, sw=1.6))
            b.append(line(cx - 44, yy + 16, cx - 52, yy + 8, c, 1.6))
        elif k == 2:
            b.append(f'<circle cx="{cx}" cy="{yy + 23}" r="18" fill="white" stroke="{c}" stroke-width="1.8"/>')
        else:
            b.append(line(cx - 40, yy + 23, cx + 34, yy + 23, c, 2.4))
            b.append(line(cx + 34, yy + 14, cx + 34, yy + 32, c, 3))
        b.append(T(cx, yy + 64, [n], 15, INK, anchor="middle"))
    yy += 80
    yy = pregunta(b, x, yy, w, "El estudiante quiere mover un carro de plástico colocando un imán, que atrae "
                               "elementos metálicos, por debajo de una mesa como se muestra en la figura.")
    # esquema
    sx = x + 300
    ty = yy + 70
    b.append(rect(sx - 40, ty, 460, 12, "#C9CED6", r=2))
    b.append(rect(sx + 140, ty - 54, 120, 40, "white", r=4, stroke=c, sw=2))
    b.append(rect(sx + 236, ty - 46, 18, 14, "white", r=2, stroke=c, sw=1.6))
    for wx in (sx + 166, sx + 234):
        b.append(f'<circle cx="{wx}" cy="{ty - 8}" r="8" fill="white" stroke="{c}" stroke-width="2"/>')
    b.append(T(sx + 200, ty - 64, ["Objeto"], 14, INK, anchor="middle"))
    b.append(rect(sx + 180, ty + 20, 40, 64, "#C9CED6", r=3, stroke=c, sw=1.8))
    for ay in (ty - 34, ty + 52):
        b.append(f'<path d="M {sx + 60} {ay - 8} L {sx + 90} {ay - 8} L {sx + 90} {ay - 16} L {sx + 110} {ay} '
                 f'L {sx + 90} {ay + 16} L {sx + 90} {ay + 8} L {sx + 60} {ay + 8} Z" fill="none" stroke="{c}" '
                 f'stroke-width="1.6" stroke-dasharray="4,3"/>')
    b.append(T(sx + 290, ty - 28, ["← Carro de plástico"], 14, INK))
    b.append(T(sx + 240, ty + 58, ["← Imán"], 14, INK))
    yy = ty + 96
    return pregunta(b, x, yy, w, "De acuerdo a lo anterior, ¿cuál de los objetos sirve para que el estudiante pueda "
                                 "mover el carro?")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Lo que atrae un imán", c,
                      "Lo de la minería: cada método le «pregunta» una propiedad a la partícula. El imán solo le "
                      "pregunta una. Escribe de qué material es cada objeto y si un imán lo atraería.")
    x0, ww = x + 22, w - 44
    cw = (ww - 3 * 20) / 4
    for k, n in enumerate(("borrador", "tapa de esfero", "pimpón", "puntilla")):
        px = x0 + k * (cw + 20)
        caja(b, px, yy, cw, 120, c, r=12)
        rot(b, px + 14, yy + 26, n.upper(), c, size=13)
        pista(b, px + 14, yy + 50, "hecho de:")
        renglon(b, px + 90, yy + 52, px + cw - 14)
        casillas(b, px + 14, yy + 76, ("lo atrae", "no"), c, paso=110, size=15)
    yy += 136
    return frase_hueco(b, x0, yy, ww, "El imán solo le pregunta a cada objeto: ¿estás hecho de ______________ ?", c)


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="El punto de ebullición y el punto de fusión de un compuesto dependen de diversos factores, como el peso "
            "molecular y las fuerzas moleculares que presentan las moléculas entre ellas. Cuanto más fuertes sean las "
            "fuerzas intermoleculares, más energía se necesitará para producir un cambio de estado. En la tabla se "
            "muestran dos moléculas con la misma fórmula molecular (C₂H₆O) pero con distintas estructuras moleculares "
            "y algunas de sus propiedades.",
          o=["El éter debe tener mayor punto de ebullición que el alcohol, pero menor punto de fusión.",
             "El alcohol debe tener mayor punto de ebullición que el éter, pero menor punto de fusión.",
             "El alcohol debe tener mayor punto de ebullición y de fusión que el éter.",
             "El éter debe tener mayor punto de ebullición y de fusión que el alcohol."],
          datos=datos_71, inst=ii1)
QB = dict(est=2, comp="Explicación de fenómenos",
          e="Un estudiante determinó las densidades y los puntos de ebullición de tres diferentes líquidos, como se "
            "muestra en la siguiente tabla.",
          o=[], datos=datos_104, inst=ii2)
QC = dict(est=3, comp="Indagación",
          e="Un estudiante desea caracterizar cuatro líquidos en el laboratorio. Para ello, toma las sustancias, mide "
            "su volumen, su masa, su punto de ebullición y calcula su densidad. El estudiante registró sus datos en la "
            "tabla.",
          o=["Columna 2: punto de ebullición (g); columna 5: masa (°C).",
             "Columna 2: masa (g); columna 5: punto de ebullición (°C).",
             "Columna 2: punto de ebullición (°C); columna 5: masa (g).",
             "Columna 2: masa (°C); columna 5: punto de ebullición (g)."],
          datos=datos_92, inst=ii3)
QD = dict(est=4, comp="Uso comprensivo del conocimiento científico",
          e="Un estudiante cuenta con los siguientes objetos:",
          o=["la puntilla, porque esta presenta propiedades magnéticas.",
             "la bola de pimpón, porque esta no presenta propiedades magnéticas.",
             "la tapa de esfero, porque esta no presenta propiedades magnéticas.",
             "el borrador, porque este presenta propiedades magnéticas."],
          datos=datos_54, inst=ii4)


def build(pages=(206, 210)):
    return [hoja_icfes("qui4_i1", pages[0], QA, QB),
            hoja_icfes("qui4_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
