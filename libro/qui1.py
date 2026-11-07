#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 1 · componente químico · aspectos analíticos de sustancias · páginas 183–189.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 1» de Química (fuente_libro/QUÍMICA), páginas 140–142.
Casos: recristalización del nitrato de potasio (1), CO₂ y presión · ley de Henry (2), hierro y
azufre frente al imán (3), CO₂ disuelto a 5 °C y a 25 °C (4 y 5), sal y azúcar en una bodega
húmeda · higroscopicidad y presión de vapor (6 a 8), síntesis de la aspirina (9 y 10).

Claves verificadas (resueltas a mano contra el texto, las tablas y las figuras, 7 nov 2026):

    1·C  2·A  3·C  4·B  5·D  6·A  7·A  8·D  9·B  10·C

Cuentas:
  1 · A 80 °C caben 250 g en 1 kg de agua: se disuelven los 250 g. A 20 °C caben 180 g:
      250 − 180 = 70 g se cristalizan; el líquido que queda tiene disueltos justo 180 g, el tope
      a 20 °C → saturado. (A dice 75 g e insaturada; B y D contradicen la cuenta.)
  2 · CO₂/P = 0,15/1 = 0,45/3 = 0,75/5 = 0,15 g por atm: proporcional a la presión, T constante.
      A es la única que relaciona más presión con más gas disuelto (B y D niegan la presión;
      C dice lo contrario de la tabla).
  3 · El imán atrae al hierro (ferromagnético) y no al azufre → propiedades magnéticas (C).
  4 · 0,40 g / 40 moléculas = 0,010 g por molécula; × 16 = 0,16 g. O bien 16/40 = 0,40 → 0,40 × 0,40 g.
  5 · A menor temperatura, menor energía cinética: el gas se queda disuelto (D). A invoca la
      presión, que se mantuvo constante.
  6 · Higroscopicidad ∝ 1/P(H₂O): la sal tiene la menor presión de vapor (2,1 kPa) → mayor
      higroscopicidad → absorbe agua y se compacta (A). D lo dice al revés.
  7 · (1/2,1) ÷ (1/3,8) = 3,8/2,1 = 1,81 ≈ 1,8 veces (A).
  8 · La sal reduce más la presión de vapor → favorece la absorción de agua del aire (D).
  9 · M(C₇H₆O₃) = 7·12 + 6·1 + 3·16 = 138 g/mol; M(C₉H₈O₄) = 9·12 + 8·1 + 4·16 = 180 g/mol.
      138 g = 1 mol → 1 mol de aspirina = 180 g teóricos; 80 % → 0,80 × 180 = 144 g (B).
 10 · El enunciado dice que la reacción requiere catalizador ácido y fue muy lenta → C.

Reparto: A 3 · B 2 · C 3 · D 2. Equilibrado.
Hallazgos (figura de la aspirina con estructuras erradas y un «subproducto» que vuelve a ser
aspirina; las bolitas del dibujo no son 40 y 16; 3,8 kPa sin temperatura; «α» por «∝»; 6 y 8
preguntan casi lo mismo; la 10 se responde con el enunciado): tablero/propuestas/qui1_hallazgos.csv.

Estrategias:
    1 · La regla de tres con sus unidades     (4, 7, 9    · ICFES 1.ª ses. N.º 115)   azul
    2 · La propiedad que la delata            (3, 6, 8    · ICFES Sim. II 2023 N.º 46) rojo
    3 · El tope de lo que se disuelve         (1, 2, 5    · ICFES Sim. II 2023 N.º 252) oro
    4 · Lo que la reacción necesita           (10         · ICFES 1.ª ses. N.º 105)   morado

Hojas: 183 qui1_t1 (1-2) · 184 qui1_t2 (3-4) · 185 qui1_i1 · 186 qui1_t3 (5-6) ·
       187 qui1_t4 (7-8) · 188 qui1_t5 (9-10) · 189 qui1_i2.
"""
import re

from taller_base import *

configurar("Química", 1, "químico · aspectos analíticos de sustancias",
           tema="Disolver, separar y reaccionar",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("La regla de tres con sus unidades", EDU_AZUL),
       2: ("La propiedad que la delata", EDU_ROJO),
       3: ("El tope de lo que se disuelve", EDU_ORO),
       4: ("Lo que la reacción necesita", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))
AGUA = "#EAF4FA"           # relleno del agua en los dibujos
VIDRIO = "#7C8A99"         # contorno de vasos y matraces


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def _esp(txt):
    """SVG junta los espacios repetidos: los que separan bloques se vuelven espacios duros."""
    return re.sub(r" {2,}", lambda m: "\u00a0" * len(m.group()), txt)


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [_esp(txt)], size, GRAY, style="italic", anchor=anchor))


def texto(b, x, y, txt, size=17, color=INK, weight="400", anchor="start"):
    b.append(T(x, y, [_esp(txt)], size, color, weight=weight, anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def hueco(b, x, y, w=90, h=40, c=GRAY):
    """Casilla para escribir un número."""
    b.append(rect(x, y, w, h, "white", r=8, stroke=c, sw=1.8))
    return x + w


def frase_hueco(b, x, y, w, txt, c, h=56):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [_esp(txt)], 18, INK, weight="700"))
    return y + h


def flecha(b, x1, y1, x2, y2, c, sw=2.6, bend=0.0, head=13):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def marca(b, x, y, txt, c):
    """Casilla de marcar con su rótulo."""
    b.append(checkbox(x, y, s=11, c=c))
    b.append(T(x + 30, y + 18, [txt], 16, GRAY))


def vaso(b, x, y, w, h, nivel=0.78, fill=AGUA):
    """Vaso de laboratorio: paredes, agua hasta `nivel` (fracción del alto)."""
    ya = y + h * (1 - nivel)
    b.append(f'<path d="M {x} {ya} L {x} {y + h - 12} Q {x} {y + h} {x + 12} {y + h} L {x + w - 12} {y + h} '
             f'Q {x + w} {y + h} {x + w} {y + h - 12} L {x + w} {ya} Z" fill="{fill}"/>')
    b.append(f'<path d="M {x - 6} {y} L {x} {y + 6} L {x} {y + h - 12} Q {x} {y + h} {x + 12} {y + h} '
             f'L {x + w - 12} {y + h} Q {x + w} {y + h} {x + w} {y + h - 12} L {x + w} {y + 6} L {x + w + 6} {y}" '
             f'fill="none" stroke="{VIDRIO}" stroke-width="3" stroke-linejoin="round"/>')
    return ya


def particula(b, cx, cy, c, r=7):
    b.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" fill="white" stroke="{c}" stroke-width="2"/>')


def ejes(b, x, y, w, h, c, xlab, ylab, xt=(), yt=()):
    """Ejes de una gráfica con marcas. xt / yt = [(fracción, rótulo)]."""
    b.append(f'<line x1="{x}" y1="{y + h}" x2="{x + w}" y2="{y + h}" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + h}" stroke="{INK}" stroke-width="2"/>')
    for f, lab in xt:
        xx = x + f * w
        b.append(f'<line x1="{xx:.0f}" y1="{y}" x2="{xx:.0f}" y2="{y + h}" stroke="#E6EAF0" stroke-width="1.4"/>')
        b.append(T(xx, y + h + 22, [lab], 14, GRAY, anchor="middle"))
    for f, lab in yt:
        yy = y + h - f * h
        b.append(f'<line x1="{x}" y1="{yy:.0f}" x2="{x + w}" y2="{yy:.0f}" stroke="#E6EAF0" stroke-width="1.4"/>')
        b.append(T(x - 8, yy + 5, [lab], 14, GRAY, anchor="end"))
    b.append(T(x + w, y + h + 44, [xlab], 14, GRAY, style="italic", anchor="end"))
    b.append(T(x, y - 10, [ylab], 14, GRAY, style="italic"))


# ───────── P1 · recristalización del nitrato de potasio ─────────
def i1(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Lo que cabe caliente y lo que cabe frío", c,
                      "Cada vaso es 1 kg de agua con una regla de gramos al lado. Marca con una raya el tope de sal "
                      "que cabe a esa temperatura y pinta hasta donde llega la sal que echó el ingeniero. Lo que "
                      "quede por encima de la raya no cabe disuelto.")
    x0, ww = x + 22, w - 44
    vw, vh = 150, 300
    for k, (temp, lab) in enumerate((("80 °C", "al principio"), ("20 °C", "al final"))):
        vx = x0 + 70 + k * 280
        vaso(b, vx, yy + 20, vw, vh, nivel=0.92)
        for g in range(0, 301, 50):          # regla de gramos: 0 abajo, 300 arriba
            ty = yy + 20 + vh - g / 300 * (vh - 24)
            b.append(f'<line x1="{vx - 16}" y1="{ty:.0f}" x2="{vx - 4}" y2="{ty:.0f}" stroke="{INK}" stroke-width="1.6"/>')
            b.append(T(vx - 20, ty + 5, [str(g)], 13, GRAY, anchor="end"))
        rot(b, vx + vw / 2, yy + vh + 50, temp, c, size=16, anchor="middle")
        pista(b, vx + vw / 2, yy + vh + 70, lab, size=14, anchor="middle")
    pista(b, x0 + 4, yy + 12, "gramos", size=13)
    ybase = yy + vh + 90
    rx = x0 + 640
    rw = x0 + ww - rx
    for k, (rt, filas) in enumerate((("A 80 °C", (("caben", "g"), ("echó", "g"))),
                                     ("A 20 °C", (("caben", "g"), ("tiene", "g"))))):
        ry = yy + k * 170
        caja(b, rx, ry, rw, 156, c, r=14)
        rot(b, rx + 18, ry + 28, rt, c)
        for j, (lab, uni) in enumerate(filas):
            pista(b, rx + 18, ry + 70 + j * 50, lab)
            hueco(b, rx + 80, ry + 44 + j * 50, 96, 38)
            texto(b, rx + 186, ry + 70 + j * 50, uni, 16, GRAY)
        if k == 0:
            pista(b, rx + 250, ry + 70, "¿se disolvió todo?")
            marca(b, rx + 250, ry + 92, "sí", c)
            marca(b, rx + 330, ry + 92, "no", c)
        else:
            pista(b, rx + 250, ry + 70, "no cabe y se vuelve cristal:")
            pista(b, rx + 250, ry + 120, "____ − ____ = ____ g")
    yy = max(yy + 2 * 170, ybase) + 26
    # la regla de las tres palabras
    rot(b, x0, yy + 4, "EL LÍQUIDO QUE QUEDA ENCIMA DE LOS CRISTALES, A 20 °C, ES", c)
    yy += 18
    defs = (("insaturado", "todavía le cabe más soluto"), ("saturado", "tiene disuelto justo el tope"),
            ("sobresaturado", "tiene disuelto más que el tope"))
    n, gap = 3, 22
    bw = (ww - gap * (n - 1)) / n
    for k, (nom, df) in enumerate(defs):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 84, c, r=12)
        b.append(checkbox(bx + 16, yy + 18, s=11, c=c))
        texto(b, bx + 46, yy + 36, nom, 18, INK, weight="700")
        pista(b, bx + 16, yy + 70, df, size=15)
    yy += 100
    return ojo(b, x0, yy, ww, "COMPARA DOS NÚMEROS, NO DOS MOMENTOS",
               "Para clasificar el líquido no mires lo que había al principio: compara lo que todavía tiene "
               "disuelto a 20 °C con lo que cabe a 20 °C. Esos dos números ya los escribiste arriba.")


# ───────── P2 · CO₂ y presión · ley de Henry ─────────
def i2(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Tres presiones, una misma razón", c,
                      "Copia la tabla y divide el gas disuelto entre la presión en cada fila. Si la división da lo "
                      "mismo tres veces, encontraste la regla. Después ubica los puntos y mira si la recta sale del cero.")
    x0, ww = x + 22, w - 44
    cols = ("PRESIÓN (atm)", "CO₂ DISUELTO (g/100 g)", "CO₂ ÷ PRESIÓN")
    cx = (x0, x0 + 170, x0 + 410)
    cwid = (150, 220, 200)
    for k, cl in enumerate(cols):
        rot(b, cx[k], yy + 18, cl, c, size=13)
    for j, p in enumerate((1, 3, 5)):
        ry = yy + 34 + j * 62
        caja(b, cx[0], ry, cwid[0], 50, c, r=8)
        texto(b, cx[0] + cwid[0] / 2, ry + 33, str(p), 20, INK, weight="700", anchor="middle")
        hueco(b, cx[1], ry, cwid[1], 50, c)
        hueco(b, cx[2], ry, cwid[2], 50, c)
    # gráfica para ubicar los puntos
    gx, gy, gw, gh = x0 + 720, yy + 26, 440, 190
    ejes(b, gx, gy, gw, gh, c, "presión (atm)", "CO₂ disuelto (g/100 g)",
         xt=[(k / 6, str(k)) for k in range(7)], yt=[(k / 4, f"{k * 0.2:.1f}".replace(".", ",")) for k in range(5)])
    yy += 34 + 3 * 62 + 46
    # la ficha del experimento
    filas = (("LO QUE SE CAMBIÓ A PROPÓSITO", "la variable que movieron los estudiantes"),
             ("LO QUE SE MIDIÓ", "lo que cambió como respuesta"),
             ("LO QUE SE DEJÓ IGUAL", "la condición que el texto dice que no se movió"))
    lw = max(tw(f[0], 14, "700") + 1.5 * len(f[0]) for f in filas) + 40
    for k, (rt, ps) in enumerate(filas):
        ry = yy + k * 74
        caja(b, x0, ry, ww, 64, c, r=12)
        b.append(rect(x0, ry, 8, 64, c, r=4))
        rot(b, x0 + 24, ry + 28, rt, c, size=14)
        pista(b, x0 + 24, ry + 52, ps, size=13)
        renglon(b, x0 + lw + 20, ry + 46, x0 + ww - 20)
    yy += 3 * 74 + 6
    yy = frase_hueco(b, x0, yy, ww, "Si la presión se duplica, el gas disuelto ____________________ .", c)
    return trampa(b, x0, yy + 14, ww, "Una hipótesis que explica con algo que nadie midió:",
                  "no explica estos datos, explica otro experimento. Antes de aceptar una, busca su causa en tu "
                  "ficha: si no aparece en «lo que se cambió», no puede ser la causa de lo que se midió.", c)


# ───────── P3 · hierro y azufre frente al imán ─────────
def i3(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Hierro y azufre: la diferencia que sirve para separar", c,
                      "Llena la ficha de cada sustancia con lo que sabes de ellas. Después marca en qué filas son "
                      "distintas. Separar no es lo mismo que distinguir: la propiedad que separa es la que el "
                      "procedimiento usa con las manos.")
    x0, ww = x + 22, w - 44
    props = ("color", "cómo se ve (polvo, limadura, trozo)", "¿lo atrae un imán?", "¿se disuelve en agua?",
             "¿conduce la electricidad?")
    c1, c2, c3 = x0 + 380, x0 + 660, x0 + 960
    rot(b, c1, yy + 18, "HIERRO", c, size=13)
    rot(b, c2, yy + 18, "AZUFRE", c, size=13)
    rot(b, c3, yy + 18, "¿SON DISTINTOS?", c, size=13)
    yy += 32
    for k, p in enumerate(props):
        ry = yy + k * 64
        caja(b, x0, ry, ww, 54, c, r=10)
        texto(b, x0 + 18, ry + 34, p, 17)
        renglon(b, c1, ry + 40, c2 - 30)
        renglon(b, c2, ry + 40, c3 - 30)
        marca(b, c3, ry + 16, "sí", c)
        marca(b, c3 + 90, ry + 16, "no", c)
    yy += 5 * 64 + 16
    caja(b, x0, yy, ww, 136, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE HIZO EL PROCEDIMIENTO", c)
    pista(b, x0 + 20, yy + 72, "pasó por encima de la mezcla:")
    renglon(b, x0 + 236, yy + 74, x0 + 560)
    pista(b, x0 + 580, yy + 72, "y lo que se fue con él fue:")
    renglon(b, x0 + 780, yy + 74, x0 + ww - 20)
    pista(b, x0 + 20, yy + 118, "entonces la fila de mi ficha que explica la separación es:")
    renglon(b, x0 + 440, yy + 120, x0 + ww - 20)
    yy += 152
    return ojo(b, x0, yy, ww, "DISTINTOS EN VARIAS COSAS, SEPARADOS POR UNA",
               "El hierro y el azufre también se ven de distinto color, pero nadie separa a mano un polvo fino "
               "grano por grano. Quédate con la fila que coincide con lo que hizo el procedimiento.")


# ───────── P4 · CO₂ a 5 °C y a 25 °C · moléculas y gramos ─────────
def i4(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Lo que pesa cada bolita del dibujo", c,
                      "Si 40 bolitas representan cierta masa, cada bolita representa una parte igual. Haz la cuenta "
                      "por dos caminos distintos: si los dos dan lo mismo, la respuesta es tuya. Escribe siempre la "
                      "unidad al lado del número.")
    x0, ww = x + 22, w - 44
    # dos vasos con su dato
    for k, (temp, lab) in enumerate((("5 °C", "moléculas"), ("25 °C", "moléculas"))):
        vx = x0 + 20 + k * 230
        ya = vaso(b, vx, yy + 10, 150, 190, nivel=0.86)
        import random as _r
        _r.seed(11 + k)
        for _ in range(14 if k == 0 else 6):
            particula(b, vx + _r.uniform(20, 130), _r.uniform(ya + 18, yy + 186), c, r=7)
        rot(b, vx + 75, yy + 228, temp, c, size=15, anchor="middle")
        hueco(b, vx + 10, yy + 240, 70, 36, c)
        pista(b, vx + 88, yy + 264, lab, size=13)
        hueco(b, vx + 10, yy + 284, 70, 36, c)
        pista(b, vx + 88, yy + 308, "gramos", size=13)
    # camino 1 y camino 2
    rx = x0 + 500
    rw = x0 + ww - rx
    for k, (rt, l1, l2) in enumerate((
            ("CAMINO 1 · CUÁNTO PESA UNA BOLITA", "____ g ÷ ____ moléculas = ________ g por molécula",
             "____ g por molécula × ____ moléculas = ________ g"),
            ("CAMINO 2 · QUÉ FRACCIÓN QUEDA", "____ moléculas ÷ ____ moléculas = ________ (fracción)",
             "________ × ____ g = ________ g"))):
        ry = yy + k * 166
        caja(b, rx, ry, rw, 150, c, r=14)
        rot(b, rx + 18, ry + 30, rt, c, size=14)
        texto(b, rx + 18, ry + 78, l1, 18)
        texto(b, rx + 18, ry + 126, l2, 18)
    yy += 2 * 166 + 10
    yy = frase_hueco(b, x0, yy, ww, "¿Los dos caminos dieron lo mismo?  ____    ¿Tiene sentido que a 25 °C haya "
                                    "menos gramos?  ____", c)
    return ojo(b, x0, yy + 14, ww, "EL DIBUJO DE TU LIBRO NO TRAE 40 Y 16 BOLITAS",
               "Si las cuentas una por una no te dan esos números. Trabaja con los datos del texto (40 y 16); el "
               "dibujo solo muestra la idea: menos bolitas, menos gas disuelto.")


# ───────── P5 · temperatura y gas disuelto · la hipótesis ─────────
def i5(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Moléculas inquietas: el gas que se escapa del agua", c,
                      "Dibuja una flecha en cada molécula: corta si se mueve despacio, larga si se mueve rápido. "
                      "Dibuja también las que alcanzan a salir del agua. Después revisa qué cambió en el "
                      "experimento y qué se dejó quieto.")
    x0, ww = x + 22, w - 44
    import random as _r
    for k, temp in enumerate(("5 °C", "25 °C")):
        vx = x0 + 40 + k * 300
        ya = vaso(b, vx, yy + 40, 200, 240, nivel=0.78)
        _r.seed(5 + k)
        for _ in range(9):
            particula(b, vx + _r.uniform(24, 176), _r.uniform(ya + 20, yy + 262), c, r=9)
        b.append(f'<line x1="{vx}" y1="{ya:.0f}" x2="{vx + 200}" y2="{ya:.0f}" stroke="{VIDRIO}" stroke-width="1.6" '
                 f'stroke-dasharray="6,5"/>')
        pista(b, vx + 100, yy + 26, "aire", size=13, anchor="middle")
        rot(b, vx + 100, yy + 310, temp, c, size=16, anchor="middle")
    rx = x0 + 640
    rw = x0 + ww - rx
    caja(b, rx, yy + 10, rw, 290, c, r=14)
    rot(b, rx + 18, yy + 40, "LO QUE DICE MI DIBUJO", c, size=14)
    for j, (lab, op) in enumerate((("a 5 °C las moléculas se mueven", "(más / menos) rápido"),
                                   ("a 25 °C las moléculas se mueven", "(más / menos) rápido"),
                                   ("las que escapan son más a", "(5 °C / 25 °C)"))):
        ry = yy + 84 + j * 70
        pista(b, rx + 18, ry, lab)
        renglon(b, rx + 18, ry + 34, rx + 260)
        pista(b, rx + 276, ry + 32, op, size=14)
    yy += 320
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("LO QUE CAMBIÓ EN EL EXPERIMENTO", "una sola variable"),
                                  ("LO QUE SE MANTUVO CONSTANTE", "el texto lo dice en la primera frase"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 96, c, r=14)
        rot(b, bx + 18, yy + 28, rt, c, size=14)
        pista(b, bx + 18, yy + 50, ps, size=14)
        renglon(b, bx + 18, yy + 82, bx + half - 18)
    yy += 112
    return trampa(b, x0, yy, ww, "Una hipótesis puede culpar a una variable que no se movió:",
                  "si su causa aparece en tu casilla de «lo que se mantuvo constante», esa hipótesis no explica la "
                  "diferencia entre los dos recipientes, por bien que suene.", c)


# ───────── P6 · sal y azúcar en la bodega · qué propiedad ─────────
def i6(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La bodega húmeda: qué vimos y qué lo explica", c,
                      "Primero lo que pasó, sin explicarlo. Después pasa cada propiedad que nombran las opciones por "
                      "dos filtros: ¿la relaciona el texto con el agua del aire? ¿y los datos dicen que la sal la tiene "
                      "más que el azúcar?")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    for k, (sus, ps) in enumerate((("SAL (NaCl) · después de 48 h", "cómo quedó"),
                                   ("AZÚCAR (sacarosa) · después de 48 h", "cómo quedó"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 90, c, r=14)
        rot(b, bx + 18, yy + 28, sus, c, size=14)
        pista(b, bx + 18, yy + 52, ps, size=14)
        renglon(b, bx + 18, yy + 78, bx + half - 18)
    yy += 106
    yy = frase_hueco(b, x0, yy, ww, "Un polvo se pega en bloques cuando ____________________ del aire.", c)
    yy += 24
    cols = ("PROPIEDAD", "¿EL TEXTO LA RELACIONA CON LA HUMEDAD?", "¿LOS DATOS DICEN QUIÉN TIENE MÁS?")
    xs = (0, 330, 800)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=13)
    yy += 28
    props = ("higroscopicidad", "densidad", "solubilidad en agua", "estructura molecular")
    for k, p in enumerate(props):
        ry = yy + k * 62
        caja(b, x0, ry, ww, 52, c, r=10)
        texto(b, x0 + 18, ry + 33, p, 17)
        marca(b, x0 + xs[1], ry + 15, "sí", c)
        marca(b, x0 + xs[1] + 90, ry + 15, "no", c)
        pista(b, x0 + xs[2], ry + 33, "tiene más:", size=15)
        renglon(b, x0 + xs[2] + 80, ry + 36, x0 + ww - 20)
    yy += 4 * 62 + 6
    return ojo(b, x0, yy + 8, ww, "UNA PROPIEDAD QUE NADIE MIDIÓ NO SIRVE DE PRUEBA",
               "Si la fila quedó en «no» o sin dato de quién tiene más, esa propiedad puede ser cierta en la vida "
               "real y aun así no ser la explicación que esta pregunta pide.")


# ───────── P7 · cuántas veces más higroscópica ─────────
def i7(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Al revés: cuando la presión baja, la sed de agua sube", c,
                      "La relación del libro es inversa: la higroscopicidad va con 1 ÷ presión de vapor. Calcula el "
                      "1 ÷ P de cada sustancia, divide los dos resultados y comprueba con el atajo.")
    x0, ww = x + 22, w - 44
    yy = alto_profe(b, x0, yy, ww,
                    "En la tabla de tu libro, el símbolo que parece una «α» es el signo de «es proporcional a». "
                    "Proporcional a 1 ÷ P quiere decir proporción inversa: si la presión de vapor se duplica, la "
                    "higroscopicidad se reduce a la mitad; si la presión baja, la higroscopicidad sube.") + 18
    half = (ww - 24) / 2
    for k, sus in enumerate(("SAL (NaCl)", "AZÚCAR")):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 126, c, r=14)
        rot(b, bx + 18, yy + 28, sus, c, size=14)
        pista(b, bx + 18, yy + 66, "presión de vapor:")
        hueco(b, bx + 150, yy + 40, 90, 38, c)
        texto(b, bx + 250, yy + 66, "kPa", 16, GRAY)
        texto(b, bx + 18, yy + 110, "1 ÷ ______ = ________", 18)
    yy += 142
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "CUÁNTAS VECES", c)
    texto(b, x0 + 20, yy + 76, "higroscopicidad de la sal ÷ higroscopicidad del azúcar  =  ________ ÷ ________  =  ________ veces", 18)
    texto(b, x0 + 20, yy + 124, "atajo, volteando la fracción:   P del azúcar ÷ P de la sal  =  ______ ÷ ______  =  ______", 18)
    yy += 166
    return frase_hueco(b, x0, yy, ww, "La más higroscópica es la de presión de vapor más ________ , y lo es ____ veces.", c)


# ───────── P8 · la hipótesis de la bodega ─────────
def i8(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dato, mecanismo, efecto: la hipótesis en tres eslabones", c,
                      "Una hipótesis buena es una cadena que no se rompe: empieza en un dato que sí está en la tabla, "
                      "dice qué hace ese dato y termina en lo que se vio en la bodega. Arma tu cadena antes de leer "
                      "las opciones.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 54
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("1 · EL DATO MEDIDO", "qué sustancia y qué número"),
                                  ("2 · LO QUE HACE ESE DATO", "con el agua del aire"),
                                  ("3 · LO QUE SE VIO", "en la bodega, a las 48 h"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 196, c, r=16)
        rot(b, bx + 18, yy + 30, rt, c, size=14)
        pista(b, bx + 18, yy + 56, ps, size=14)
        for j in range(3):
            renglon(b, bx + 18, yy + 100 + j * 40, bx + bw - 18)
        if k < n - 1:
            flecha(b, bx + bw + 8, yy + 98, bx + bw + gap - 8, yy + 98, c, sw=3, head=14)
    yy += 214
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "¿LA CADENA HABLA DE LA MISMA SUSTANCIA DE PUNTA A PUNTA?", c, size=14)
    pista(b, x0 + 20, yy + 76, "menor presión de vapor la tiene:")
    renglon(b, x0 + 250, yy + 78, x0 + 560)
    pista(b, x0 + 600, yy + 76, "se compactó:")
    renglon(b, x0 + 700, yy + 78, x0 + ww - 20)
    pista(b, x0 + 20, yy + 124, "¿coinciden?")
    marca(b, x0 + 120, yy + 106, "sí", c)
    marca(b, x0 + 210, yy + 106, "no", c)
    pista(b, x0 + 320, yy + 124, "una opción que nombra la otra sustancia se cae porque")
    renglon(b, x0 + 700, yy + 126, x0 + ww - 20)
    yy += 166
    return trampa(b, x0, yy, ww, "Un dato que suena científico no siempre es el de la tabla:",
                  "si el primer eslabón de una hipótesis es una propiedad que la tabla no trae, la cadena empieza en "
                  "el aire. Revisa tu eslabón 1 antes de aceptarla.", c)


# ───────── P9 · rendimiento de la aspirina ─────────
def i9(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Lo que podía salir y lo que salió", c,
                      "Primero comprueba con las masas atómicas que 138 g y 180 g son la misma cantidad de "
                      "moléculas (1 mol). Después pinta en la barra el porcentaje que de verdad salió y conviértelo "
                      "en gramos.")
    x0, ww = x + 22, w - 44
    pista(b, x0, yy + 14, "masas atómicas:  C = 12   H = 1   O = 16   (en g/mol)", size=15)
    yy += 30
    half = (ww - 24) / 2
    for k, (fm, rt) in enumerate((("C₇H₆O₃", "ÁCIDO SALICÍLICO"), ("C₉H₈O₄", "ASPIRINA"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 120, c, r=14)
        rot(b, bx + 18, yy + 28, f"{rt} · {fm}", c, size=14)
        n = (7, 6, 3) if k == 0 else (9, 8, 4)
        texto(b, bx + 18, yy + 72, f"{n[0]} × 12 + {n[1]} × 1 + {n[2]} × 16 = ________ g/mol", 18)
        texto(b, bx + 18, yy + 106, "en 1 mol hay ______ g", 16, GRAY)
    yy += 136
    yy = frase_hueco(b, x0, yy, ww, "138 g de ácido salicílico son ____ mol  →  dan ____ mol de aspirina  =  ______ g "
                                    "si todo saliera bien (100 %)", c)
    yy += 22
    # la barra del rendimiento
    rot(b, x0, yy + 14, "LA BARRA DEL 100 %: PINTA LO QUE SALIÓ", c, size=14)
    yy += 28
    bw = ww - 40
    for k in range(10):
        b.append(rect(x0 + 20 + k * bw / 10, yy, bw / 10, 56, "white", r=0, stroke=c, sw=1.8))
        b.append(T(x0 + 20 + (k + 1) * bw / 10, yy + 80, [f"{(k + 1) * 10} %"], 13, GRAY, anchor="middle"))
    b.append(T(x0 + 20, yy + 80, ["0 %"], 13, GRAY, anchor="middle"))
    yy += 104
    caja(b, x0, yy, ww, 70, c, r=12)
    texto(b, x0 + 20, yy + 44, "lo que salió  =  ______ g  ×  ______ ÷ 100  =  ________ g", 19)
    yy += 86
    return ojo(b, x0, yy, ww, "EL PORCENTAJE SE LE SACA AL PRODUCTO",
               "El rendimiento compara lo que salió de aspirina con lo que podía salir de aspirina. El número "
               "del reactivo sirve para saber cuánto podía salir, no para multiplicarlo por el porcentaje.")


# ───────── P10 · catalizador · la reacción lenta ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La colina que tienen que subir los reactivos", c,
                      "Haz la lista de lo que el diagrama dice que la reacción necesita. Después lee el síntoma "
                      "(muy lenta y sobró reactivo) y busca en tu lista lo que tiene que ver con la rapidez, no con "
                      "la cantidad.")
    x0, ww = x + 22, w - 44
    yy = alto_profe(b, x0, yy, ww,
                    "Para reaccionar, las moléculas tienen que chocar con suficiente energía: es como subir una colina "
                    "(energía de activación). Si pocas logran subirla, la reacción es lenta. El profe dibuja la colina "
                    "en el tablero y explica qué cosas cambian su altura y cuáles no.") + 18
    # la lista de lo que pide la reacción
    rot(b, x0, yy + 14, "LO QUE EL DIAGRAMA DICE QUE NECESITA", c, size=14)
    yy += 28
    n, gap = 4, 18
    bw = (ww - gap * (n - 1)) / n
    for k in range(n):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 96, c, r=12)
        b.append(T(bx + 16, yy + 26, [str(k + 1)], 16, c, weight="700"))
        renglon(b, bx + 16, yy + 60, bx + bw - 16)
        pista(b, bx + 16, yy + 84, "¿afecta la rapidez?  sí / no", size=13)
    yy += 112
    # la colina
    gx, gy, gw, gh = x0 + 60, yy + 24, 560, 200
    ejes(b, gx, gy, gw, gh, c, "avance de la reacción", "energía")
    pts = []
    for i in range(41):
        t = i / 40
        e = 0.35 * (1 - t) + 0.15 * t + 0.55 * math.exp(-((t - 0.5) / 0.16) ** 2)
        pts.append(f"{gx + 20 + t * (gw - 40):.0f},{gy + gh - e * gh:.0f}")
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{c}" stroke-width="3"/>')
    pista(b, gx + 30, gy + gh - 0.35 * gh - 12, "reactivos", size=13)
    pista(b, gx + gw - 30, gy + gh - 0.15 * gh - 12, "aspirina", size=13, anchor="end")
    rx = gx + gw + 40
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 230, c, r=14)
    rot(b, rx + 18, yy + 30, "EN LA COLINA", c, size=14)
    pista(b, rx + 18, yy + 70, "la reacción fue lenta porque pocas moléculas")
    renglon(b, rx + 18, yy + 108, rx + rw - 18)
    pista(b, rx + 18, yy + 150, "lo que faltó, de mi lista, es el número:")
    hueco(b, rx + 300, yy + 124, 60, 38, c)
    pista(b, rx + 18, yy + 200, "dibuja en la gráfica cómo sería la colina con eso", size=14)
    yy += 246
    return trampa(b, x0, yy, ww, "Una explicación que no aparece en el diagrama:",
                  "si una opción culpa a algo que el diagrama no muestra y que el texto no reporta, compárala con la "
                  "que sí sale en tu lista. Lo que se observó fue lentitud, no un accidente.", c)


Q = {1: dict(n=1, est=3, pag=140, ctx="Nitrato de potasio · de 80 °C a 20 °C · cuánto se cristaliza",
             comp="Uso comprensivo del conocimiento científico", inst=i1),
     2: dict(n=2, est=3, pag=140, ctx="CO₂ disuelto a 1, 3 y 5 atm · qué hipótesis explica la tabla",
             comp="Indagación", inst=i2),
     3: dict(n=3, est=2, pag=140, ctx="Azufre en polvo y limaduras de hierro · el imán",
             comp="Uso comprensivo del conocimiento científico", inst=i3),
     4: dict(n=4, est=1, pag=141, ctx="40 moléculas a 5 °C y 16 a 25 °C · cuántos gramos quedan",
             comp="Uso comprensivo del conocimiento científico", inst=i4),
     5: dict(n=5, est=3, pag=141, ctx="CO₂ disuelto y temperatura · qué hipótesis",
             comp="Explicación de fenómenos", inst=i5),
     6: dict(n=6, est=2, pag=141, ctx="Sal y azúcar en una bodega húmeda · qué propiedad",
             comp="Explicación de fenómenos", inst=i6),
     7: dict(n=7, est=1, pag=141, ctx="Presión de vapor 2,1 y 3,8 kPa · cuántas veces más higroscópica",
             comp="Uso comprensivo del conocimiento científico", inst=i7),
     8: dict(n=8, est=2, pag=141, ctx="Sal y azúcar en la bodega · qué hipótesis",
             comp="Indagación", inst=i8),
     9: dict(n=9, est=1, pag=142, ctx="Síntesis de la aspirina · 138 g de reactivo al 80 %",
             comp="Uso comprensivo del conocimiento científico", inst=i9),
     10: dict(n=10, est=4, pag=142, ctx="Aspirina · reacción lenta con reactivo sobrante · por qué",
              comp="Explicación de fenómenos", inst=i10)}


def build(pages=(183, 184, 186, 187, 188)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"qui1_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
