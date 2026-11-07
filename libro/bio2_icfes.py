#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 2 · entrenamiento ICFES · páginas 149 y 153.

Cuatro preguntas oficiales de Ciencias Naturales con contenido de biología del organismo, de dos
cuadernillos escaneados en Drive («1. CUADERNILLOS ICFES»):
  · «2016-1 PRIMERA SESION.pdf»: portada «2016-1 · Primera sesión», cuadernillo AAM; Ciencias
    Naturales con encabezado «Saber 11 - 083 - B05R - AAM · 1a. sesión».
  · «2016-2 SEGUNDA SESION.pdf»: portada «2016-1 · Segunda sesión», cuadernillo ABD; Ciencias
    Naturales con encabezado «Saber 11 - 083 - B10O - ABD · 2a. sesión».
Ninguna estaba en tablero/icfes.csv; reservadas en tablero/propuestas/bio_icfes_reservas.csv.
Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · 2a sesión N.º 62  · B   (pastillas: hormonas altas todo el ciclo → no hay ovulación)  estrategia 1
    QB · 1a sesión N.º 108 · D   (si el O₂ no pasa al capilar, los tejidos se quedan sin O₂)  estrategia 4
    QC · 1a sesión N.º 102 · A   (el CO ocupa la hemoglobina → menos O₂ a las células)       estrategia 2
    QD · 1a sesión N.º 103 · A   (las dos frecuencias suben y se estabilizan; el deportista
                                  siempre más abajo; la D es la misma figura con la leyenda
                                  invertida)                                                  estrategia 3

La QA trae en el cuadernillo el texto de las preguntas 61 a 63 y dos gráficas de hormonas (ciclo
menstrual y ciclo estral). Aquí va el texto completo y un esquema simplificado de la hormona
luteinizante en el ciclo menstrual (pico hacia el día 14, ovulación). Las figuras de QB y QD están
redibujadas a partir del cuadernillo; los valores de QD se leyeron sobre la cuadrícula.
"""
from bio2 import *   # noqa: F401,F403  (configura la misión y EST)
from bio2 import rot, caja, pista, renglon, frase_hueco, ficha, flecha, dos_casillas, TINTE


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · N.º 62 · pastillas anticonceptivas ─────────
CICLOS = ("En el grupo de los mamíferos se presentan dos tipos de ciclos reproductivos: el menstrual (de 24 a 35 "
          "días), exclusivo de primates y humanos; y el ciclo estral (entre estaciones), en el resto de mamíferos. "
          "La diferencia entre estos dos tipos de ciclos radica en el periodo de receptividad sexual. En el ciclo "
          "estral, la hembra solo es sexualmente receptiva durante el estro u ovulación; en el ciclo menstrual, la "
          "hembra muestra receptividad sexual durante casi todo el ciclo.")


def datos_62(b, x, y, w):
    c = A["color"]
    # esquema simplificado: hormona luteinizante en el ciclo menstrual
    gx, gy, gw, gh = x + 60, y + 10, 520, 120
    b.append(f'<line x1="{gx}" y1="{gy + gh}" x2="{gx + gw}" y2="{gy + gh}" stroke="{INK}" stroke-width="1.8"/>')
    b.append(f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy + gh}" stroke="{INK}" stroke-width="1.8"/>')
    pts = []
    for d in range(0, 29):
        v = 18 + 80 * math.exp(-((d - 14) ** 2) / 1.6)
        pts.append(f"{gx + d * gw / 28:.0f},{gy + gh - v:.0f}")
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{c}" stroke-width="2.6"/>')
    for d in (1, 14, 28):
        b.append(T(gx + d * gw / 28, gy + gh + 22, [str(d)], 14, INK, anchor="middle"))
    b.append(T(gx + gw / 2, gy + gh + 42, ["días del ciclo menstrual"], 14, GRAY, style="italic", anchor="middle"))
    b.append(T(gx + 14 * gw / 28 + 14, gy + 12, ["pico de hormona luteinizante (LH) → ovulación"], 14, INK,
               weight="700"))
    b.append(T(gx - 10, gy + gh / 2, ["LH"], 14, INK, weight="700", anchor="end"))
    nota = ("Esquema simplificado de la figura del cuadernillo, que muestra además el estrógeno, la progesterona y "
            "el ciclo estral.")
    svg, yy = TJ(gx + gw + 40, gy + 30, nota, x + w - (gx + gw + 40), 14, GRAY, style="italic", lh=20)
    b.append(svg)
    yy = gy + gh + 52
    return pregunta(b, x, yy, w, "La mayoría de las pastillas anticonceptivas se basan en una mezcla de hormonas con "
                                 "una combinación estratégica de estrógeno y progesterona. Con base en la información "
                                 "anterior, ¿por qué una mujer que utiliza este método anticonceptivo tiene menor "
                                 "probabilidad de quedar embarazada?")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "La orden que nunca llega", c,
                      "Otro circuito, como el del calcio: una hormona alta frena la orden siguiente. Sigue la cadena "
                      "desde la pastilla hasta el óvulo.")
    x0, ww = x + 22, w - 44
    yy = alto_profe(b, x0, yy, ww,
                    "Retroalimentación negativa: cuando una hormona está alta en la sangre, el cuerpo frena la orden "
                    "que la produce, como un termostato que apaga la calefacción.") + 14
    n, gap = 3, 50
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("LA PASTILLA", "estrógeno y progesterona: ¿altos o bajos? ¿cuánto tiempo?"),
                                  ("EL PICO DE LH", "con esas hormonas altas, ¿aparece?"),
                                  ("LO QUE NO OCURRE", "sin pico de LH no hay…"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 120, c, r=14)
        rot(b, bx + 16, yy + 28, rt, c, size=13)
        svg, _ = TJ(bx + 16, yy + 38, ps, bw - 32, 14, GRAY, style="italic", lh=19)
        b.append(svg)
        renglon(b, bx + 16, yy + 104, bx + bw - 16)
        if k < n - 1:
            flecha(b, bx + bw + 6, yy + 60, bx + bw + gap - 6, yy + 60, c, sw=3, head=14)
    return yy + 120


# ───────── QB · N.º 108 · alvéolo y capilar ─────────
def datos_108(b, x, y, w):
    c = A["color"]
    ax, ay = x + 330, y + 20
    # alvéolo: media luna abierta arriba
    b.append(f'<path d="M {ax - 200} {ay + 20} Q {ax} {ay + 230} {ax + 200} {ay + 20}" fill="#F4F6FA" '
             f'stroke="{INK}" stroke-width="2.4"/>')
    b.append(T(ax + 215, ay + 30, ["Alvéolo pulmonar"], 15, INK, weight="700"))
    # capilar debajo
    cy = ay + 170
    b.append(f'<path d="M {ax - 300} {cy} Q {ax} {cy + 70} {ax + 300} {cy - 10}" fill="none" stroke="{EDU_ROJO}" '
             f'stroke-width="26" stroke-opacity="0.25"/>')
    for k in range(4):
        b.append(f'<ellipse cx="{ax - 160 + k * 100}" cy="{cy + 26 - abs(k - 1.5) * 8:.0f}" rx="24" ry="11" '
                 f'fill="white" stroke="{EDU_ROJO}" stroke-width="1.8"/>')
    b.append(T(ax + 230, cy + 46, ["Capilar sanguíneo"], 15, INK, weight="700"))
    b.append(T(ax + 130, cy + 70, ["Glóbulo rojo"], 14, INK))
    b.append(T(ax - 300, cy + 52, ["Sangre entrando al pulmón →"], 14, INK))
    b.append(T(ax + 320, cy - 34, ["→ Sangre saliendo del pulmón"], 14, INK))
    # intercambio
    b.append(T(ax - 70, ay + 70, ["O₂"], 17, INK, weight="700"))
    b.append(hand_arrow(ax - 58, ay + 80, ax - 58, cy + 10, INK, sw=2.2, bend=0.0, head=10))
    b.append(T(ax + 50, ay + 70, ["CO₂"], 17, INK, weight="700"))
    b.append(hand_arrow(ax + 64, cy + 6, ax + 64, ay + 82, INK, sw=2.2, bend=0.0, head=10))
    yy = cy + 90
    return pregunta(b, x, yy, w, "¿Qué efecto puede darse si el oxígeno no ingresa a través de la membrana del capilar "
                                 "sanguíneo?")


def ii2(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "El oxígeno, tramo por tramo", c,
                      "Como en la pregunta 2: una explicación tiene que alcanzar hasta el final de la cadena. Pon "
                      "la barrera donde dice la pregunta y marca hasta dónde llega el oxígeno.")
    x0, ww = x + 22, w - 44
    tramos = ("el aire", "el alvéolo", "la sangre del capilar", "los glóbulos rojos", "los demás tejidos")
    n, gap = 5, 30
    tw_ = (ww - gap * (n - 1)) / n
    for k, t in enumerate(tramos):
        tx = x0 + k * (tw_ + gap)
        caja(b, tx, yy, tw_, 104, c, r=14)
        b.append(T(tx + tw_ / 2, yy + 32, [t], 16, INK, weight="700", anchor="middle"))
        pista(b, tx + 16, yy + 64, "¿hay O₂ aquí?", size=14)
        dos_casillas(b, tx + 16, yy + 94, ("sí", "no"), c, paso=74, size=15)
        if k < n - 1:
            flecha(b, tx + tw_ + 4, yy + 52, tx + tw_ + gap - 4, yy + 52, c, sw=2.4, head=10)
    pista(b, x0 + 2 * (tw_ + gap) - gap / 2, yy + 128, "↑ aquí está la barrera de la pregunta", size=14,
          anchor="middle")
    yy += 140
    return trampa(b, x0, yy, ww, "¿El alvéolo fabrica oxígeno?",
                  "mira tu primer tramo: de dónde le llega el oxígeno al alvéolo. Una opción que le cambia el oficio "
                  "a una pieza ya no habla de este modelo.", c)


# ───────── QC · N.º 102 · monóxido de carbono ─────────
def ii3(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Cuatro asientos y un pasajero que no se baja", c,
                      "Lo que sale del texto, no de lo que suena: la hemoglobina es un bus de cuatro asientos. "
                      "Escribe quién ocupa cada asiento en aire limpio y con mucho monóxido de carbono.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, rt in enumerate(("AIRE LIMPIO", "MUCHO MONÓXIDO DE CARBONO (CO)")):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 130, c, r=16)
        rot(b, bx + 18, yy + 30, rt, c, size=13)
        for j in range(4):
            b.append(f'<circle cx="{bx + 70 + j * 120}" cy="{yy + 82}" r="30" fill="white" stroke="{c}" '
                     f'stroke-width="2.2"/>')
    yy += 146
    return frase_hueco(b, x0, yy, ww, "Con CO, la sangre lleva menos ____________ hacia ____________ .", c)


# ───────── QD · N.º 103 · frecuencia cardiaca ─────────
GRAF = {"A": (((0, 85), (15, 135), (30, 143), (45, 148), (57, 152)),
              ((0, 62), (15, 110), (30, 125), (45, 133), (57, 138))),
        "B": (((0, 65), (15, 90), (30, 115), (45, 140), (63, 165)),
              ((0, 85), (15, 83), (30, 83), (45, 83), (60, 83))),
        "C": (((0, 113), (15, 116), (30, 122), (45, 135), (60, 150)),
              ((0, 100), (15, 95), (30, 80), (45, 65), (60, 57))),
        "D": (((0, 62), (15, 108), (30, 128), (45, 135), (57, 138)),
              ((0, 88), (15, 138), (30, 145), (45, 150), (57, 152)))}


def _mini(b, x, y, gw, gh, L):
    c = A["color"]
    ficha(b, x + 14, y + 10, L, c, r=14, size=15)
    ox, oy = x + 70, y + gh - 30
    pw, ph = gw - 90, gh - 60
    X = lambda t: ox + t / 80 * pw
    Y = lambda f: oy - (f - 55) / 120 * ph
    for f in (55, 95, 135, 175):
        b.append(f'<line x1="{ox}" y1="{Y(f):.0f}" x2="{ox + pw}" y2="{Y(f):.0f}" stroke="#E3E8EF" stroke-width="1"/>')
        b.append(T(ox - 6, Y(f) + 5, [str(f)], 12, INK, anchor="end"))
    b.append(f'<line x1="{ox}" y1="{oy}" x2="{ox + pw}" y2="{oy}" stroke="{INK}" stroke-width="1.6"/>')
    b.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{Y(175) - 6:.0f}" stroke="{INK}" stroke-width="1.6"/>')
    for t in (0, 20, 40, 60, 80):
        b.append(T(X(t), oy + 16, [str(t)], 12, INK, anchor="middle"))
    b.append(T(ox + pw / 2, oy + 32, ["Tiempo (minutos)"], 12, INK, anchor="middle"))
    sed, dep = GRAF[L]
    b.append(f'<polyline points="{" ".join(f"{X(t):.0f},{Y(f):.0f}" for t, f in sed)}" fill="none" '
             f'stroke="{INK}" stroke-width="2.4"/>')
    for t, f in sed:
        b.append(f'<polygon points="{X(t):.0f},{Y(f) - 5:.0f} {X(t) + 5:.0f},{Y(f):.0f} {X(t):.0f},{Y(f) + 5:.0f} '
                 f'{X(t) - 5:.0f},{Y(f):.0f}" fill="white" stroke="{INK}" stroke-width="1.4"/>')
    b.append(f'<polyline points="{" ".join(f"{X(t):.0f},{Y(f):.0f}" for t, f in dep)}" fill="none" '
             f'stroke="{INK}" stroke-width="1.6" stroke-dasharray="6,4"/>')
    for t, f in dep:
        b.append(f'<rect x="{X(t) - 4:.0f}" y="{Y(f) - 4:.0f}" width="8" height="8" fill="white" stroke="{INK}" '
                 f'stroke-width="1.4"/>')


def datos_103(b, x, y, w):
    yy = y + 6
    # leyenda común (en el cuadernillo cada gráfica trae la misma leyenda)
    b.append(f'<line x1="{x}" y1="{yy + 8}" x2="{x + 40}" y2="{yy + 8}" stroke="{INK}" stroke-width="2.4"/>')
    b.append(f'<polygon points="{x + 20},{yy + 3} {x + 25},{yy + 8} {x + 20},{yy + 13} {x + 15},{yy + 8}" '
             f'fill="white" stroke="{INK}" stroke-width="1.4"/>')
    b.append(T(x + 50, yy + 14, ["Sedentario"], 15, INK))
    b.append(f'<line x1="{x + 180}" y1="{yy + 8}" x2="{x + 220}" y2="{yy + 8}" stroke="{INK}" stroke-width="1.6" '
             f'stroke-dasharray="6,4"/>')
    b.append(f'<rect x="{x + 196}" y="{yy + 4}" width="8" height="8" fill="white" stroke="{INK}" stroke-width="1.4"/>')
    b.append(T(x + 230, yy + 14, ["Deportista"], 15, INK))
    b.append(T(x + 400, yy + 14, ["eje vertical: frecuencia cardiaca (latidos por minuto)"], 14, GRAY,
               style="italic"))
    yy += 26
    gw, gh = (w - 30) / 4, 210
    for k, L in enumerate("ABCD"):
        _mini(b, x + k * (gw + 10), yy, gw, gh, L)
    return yy + gh + 4


def ii4(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Predice la curva antes de mirar las cuatro", c,
                      "Dato contra dato: primero lo que dice el texto, después las gráficas. Responde las tres "
                      "preguntas y busca la gráfica que cumple las tres.")
    x0, ww = x + 22, w - 44
    qs = (("Según el texto, al hacer ejercicio la frecuencia de cualquiera…", ("sube", "no cambia")),
          ("Entonces la curva del deportista…", ("sube", "baja o queda plana")),
          ("Quién queda más arriba todo el tiempo…", ("sedentario", "deportista")))
    for k, (q, ops) in enumerate(qs):
        ry = yy + k * 56
        caja(b, x0, ry, ww - 260, 48, c, r=10)
        pista(b, x0 + 18, ry + 31, q)
        dos_casillas(b, x0 + 470, ry + 31, ops, c, paso=170)
    caja(b, x0 + ww - 240, yy, 240, 160, c, r=14)
    rot(b, x0 + ww - 222, yy + 30, "LA QUE CUMPLE", c, size=13)
    rot(b, x0 + ww - 222, yy + 52, "LAS TRES", c, size=13)
    caja(b, x0 + ww - 160, yy + 76, 80, 64, c, r=10)
    yy += 3 * 56 + 8
    return ojo(b, x0, yy, ww, "DOS GRÁFICAS SE PARECEN MUCHO",
               "Tienen la misma forma con los nombres cambiados. Antes de escoger, mira en la leyenda cuál línea es "
               "la del deportista.")


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico", e=CICLOS,
          o=["Porque restringirá a unos días específicos su receptividad sexual, lo cual disminuye la posibilidad de "
             "quedar embarazada.",
             "Porque estas hormonas permanecerán en altas concentraciones durante todo el ciclo, lo cual impide la "
             "ovulación.",
             "Porque este método eliminará los espermatozoides durante su trayecto hacia el óvulo, lo cual impide la "
             "fecundación.",
             "Porque este método aumentará el número de días que dura el ciclo menstrual, lo cual altera los días "
             "fértiles."],
          datos=datos_62, inst=ii1)
QB = dict(est=4, comp="Explicación de fenómenos",
          e="El siguiente modelo representa el intercambio de oxígeno entre la membrana del alvéolo pulmonar y el "
            "capilar sanguíneo.",
          o=["Los alvéolos se desplazarán con el oxígeno por el sistema circulatorio.",
             "Los demás tejidos del cuerpo obtendrán el oxígeno a través del CO₂.",
             "Los alvéolos dejarán de producir oxígeno.",
             "Los demás tejidos del cuerpo se privarán de oxígeno."],
          datos=datos_108, inst=ii2)
QC = dict(est=2, comp="Uso comprensivo del conocimiento científico",
          e="La hemoglobina es la molécula encargada de realizar el intercambio de gases en los alvéolos pulmonares. "
            "La unión de la hemoglobina con el monóxido de carbono (CO) es más fuerte que con el oxígeno (O₂). Por "
            "esta razón, en presencia de CO se reduce la cantidad de moléculas de hemoglobina disponibles para unirse "
            "al O₂. Con base en la información anterior, una alta concentración de monóxido de carbono en el "
            "organismo puede generar problemas de salud, porque",
          o=["se disminuye el transporte de oxígeno hacia las células.",
             "se aumenta la cantidad de oxígeno libre en la sangre haciéndola efervescente.",
             "se disminuye el transporte de monóxido de carbono de los tejidos a los pulmones.",
             "el monóxido de carbono destruye las moléculas de hemoglobina en la sangre."],
          inst=ii3)
QD = dict(est=3, comp="Indagación",
          e="Cuando las personas hacen ejercicio el ritmo cardiaco se eleva. En personas deportistas el corazón se "
            "adapta y permite que un deportista pueda hacer ejercicio por más tiempo, sin aumentar demasiado su "
            "frecuencia cardiaca. En un experimento se somete una persona sedentaria y una que se ejercita "
            "regularmente, a una misma actividad física durante una hora. ¿Cuál gráfica representa mejor la "
            "frecuencia cardiaca en función del tiempo para ambas personas mientras hacen ejercicio?",
          o=[], datos=datos_103, inst=ii4)


def build(pages=(149, 153)):
    return [hoja_icfes("bio2_i1", pages[0], QA, QB, vocab=False),
            hoja_icfes("bio2_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
