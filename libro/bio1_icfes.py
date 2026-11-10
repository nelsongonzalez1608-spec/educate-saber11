#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 1 · entrenamiento ICFES · páginas 142 y 146.

Cuatro preguntas oficiales de Ciencias Naturales con contenido de biología celular, de dos
cuadernillos escaneados en Drive («1. CUADERNILLOS ICFES»):
  · «2016-1 PRIMERA SESION.pdf»: portada «2016-1 · Examen de Estado · Primera sesión», cuadernillo
    AAM; páginas de Ciencias Naturales con encabezado «Saber 11 - 083 - B05R - AAM · 1a. sesión».
  · «2016-2 SEGUNDA SESION.pdf»: portada «2016-1 · Segunda sesión», cuadernillo ABD; páginas de
    Ciencias Naturales con encabezado «Saber 11 - 083 - B10O - ABD · 2a. sesión».
Ninguna estaba en tablero/icfes.csv; reservadas en tablero/propuestas/bio_icfes_reservas.csv.
Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11», sin año ni «oficial».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · 2a sesión N.º 60 · A   (si se rompen los lisosomas)                     estrategia 1
    QB · 1a sesión N.º 93 · A   (sacar Na⁺ de la célula: contra el gradiente)     estrategia 4
    QC · 2a sesión N.º 75 · D   (error al copiar ADN → ARNm)                      estrategia 2
    QD · 2a sesión N.º 58 · C   (insecticida 4 = 50 % = caja sin insecticida)    estrategia 3

Cuentas de la QD: mueren 100 − sobrevivientes → 10, 20, 30, 50 y 50 %. El insecticida 4 mata lo
mismo que no echar nada. (Dato raro del ítem: con los insecticidas 1 a 3 mueren MENOS que sin
insecticida; registrado como «Atención».)
Las figuras de QB y QC están redibujadas en esquema a partir del cuadernillo.
"""
from bio1 import *   # noqa: F401,F403  (configura la misión y EST)
import math
from bio1 import rot, caja, pista, renglon, frase_hueco, ficha, flecha, VERDE_CEL


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · N.º 60 · lisosomas rotos ─────────
def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Si el saco de enzimas se revienta adentro", c,
                      "Lo mismo que en la pregunta 1: primero el oficio, después la falla. Sigue lo que estaba "
                      "guardado hasta el lugar donde queda suelto.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 56
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("LO QUE GUARDA EL LISOSOMA", "qué hay adentro y para qué sirve"),
                                  ("SI SE ROMPE, QUEDA SUELTO EN", "en qué parte de la célula"),
                                  ("LO PRIMERO QUE HACE AHÍ", "con lo que encuentra alrededor"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 128, c, r=16)
        rot(b, bx + 18, yy + 28, rt, c, size=13)
        pista(b, bx + 18, yy + 52, ps, size=14)
        renglon(b, bx + 18, yy + 88, bx + bw - 18)
        renglon(b, bx + 18, yy + 118, bx + bw - 18)
        if k < n - 1:
            flecha(b, bx + bw + 6, yy + 64, bx + bw + gap - 6, yy + 64, c, sw=3, head=14)
    yy += 144
    return ojo(b, x0, yy, ww, "LA PREGUNTA DICE «INICIALMENTE»",
               "Pide lo primero que pasaría, no lo que pasaría días después. Una opción puede ser cierta a la "
               "larga y aun así no ser lo inicial.")


# ───────── QB · N.º 93 · transporte de Na⁺ ─────────
def datos_93(b, x, y, w):
    c = A["color"]
    cols = ("Ósmosis", "Difusión simple", "Difusión facilitada", "Transporte activo")
    filas = (("Moléculas transportadas", ("Agua", "Gases", "Moléculas con carga eléctrica",
                                          "Moléculas con carga eléctrica")),
             ("Dirección del transporte", ("De mayor a menor concentración", "De mayor a menor concentración",
                                           "De mayor a menor concentración", "De menor a mayor concentración")))
    tx, lw, cw_ = x, 190, 165
    yy = y + 6
    b.append(rect(tx + lw, yy, 4 * cw_, 34, A["bg"], r=0, stroke=c, sw=1.4))
    b.append(T(tx + lw + 2 * cw_, yy + 24, ["Tipo de transporte"], 16, INK, weight="700", anchor="middle"))
    yy += 34
    for k, cl in enumerate(cols):
        b.append(rect(tx + lw + k * cw_, yy, cw_, 34, "white", r=0, stroke=c, sw=1.4))
        b.append(T(tx + lw + k * cw_ + cw_ / 2, yy + 23, [cl], 15, INK, anchor="middle"))
    yy += 34
    for nom, vals in filas:
        b.append(rect(tx, yy, lw, 62, "white", r=0, stroke=c, sw=1.4))
        svg, _ = TJ(tx + 10, yy + 6, nom, lw - 20, 15, INK, lh=20)
        b.append(svg)
        for k, v in enumerate(vals):
            b.append(rect(tx + lw + k * cw_, yy, cw_, 62, "white", r=0, stroke=c, sw=1.4))
            lns = [" ".join(p) for p in wrap_px(v, 15, cw_ - 16)]
            for j, ln in enumerate(lns):
                b.append(T(tx + lw + k * cw_ + cw_ / 2, yy + 22 + j * 19, [ln], 15, INK, anchor="middle"))
        yy += 62
    # la célula del ejemplo
    cx, cy = tx + lw + 4 * cw_ + 200, y + 100
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="130" ry="84" fill="{VERDE_CEL}" stroke="{c}" stroke-width="2.4"/>')
    b.append(f'<circle cx="{cx + 46}" cy="{cy + 20}" r="30" fill="white" stroke="{c}" stroke-width="1.8"/>')
    for px, py in ((-60, -36), (-10, -50), (-74, 10), (-30, 0), (20, -28)):
        b.append(T(cx + px, cy + py, ["K⁺"], 16, INK, weight="700", anchor="middle"))
    b.append(T(cx - 50, cy + 52, ["Na⁺"], 16, INK, weight="700", anchor="middle"))
    for px, py in ((-150, -80), (110, -84), (150, -30), (154, 30), (120, 92), (-150, 80)):
        b.append(T(cx + px, cy + py, ["Na⁺"], 16, INK, weight="700", anchor="middle"))
    pista(b, cx, cy + 116, "Ejemplo (esquema del cuadernillo)", size=14, anchor="middle")
    yy = max(yy, cy + 120)
    return pregunta(b, x, yy + 4, w, "Con base en la información anterior, si la célula del ejemplo necesitara "
                                     "transportar el ion Na⁺ del interior al exterior de la célula, ¿cuál tipo de "
                                     "transporte seguiría?")


def ii2(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Cuenta los iones antes de escoger la puerta", c,
                      "Igual que con la sal en el suelo: primero dónde hay más y dónde hay menos, después hacia "
                      "dónde tiene que ir. La tabla solo se mira al final.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 120, c, r=14)
    for k, (lab, xx) in enumerate((("Na⁺ adentro:", x0 + 20), ("Na⁺ afuera:", x0 + 300))):
        pista(b, xx, yy + 42, lab)
        caja(b, xx + 112, yy + 14, 80, 42, c)
    pista(b, x0 + 600, yy + 42, "¿el Na⁺ tiene carga eléctrica?")
    for j, lab in enumerate(("sí", "no")):
        b.append(checkbox(x0 + 840 + j * 90, yy + 25, s=11, c=c))
        b.append(T(x0 + 870 + j * 90, yy + 43, [lab], 16, GRAY))
    pista(b, x0 + 20, yy + 96, "Lo tienen que llevar de donde hay")
    renglon(b, x0 + 270, yy + 98, x0 + 520)
    pista(b, x0 + 536, yy + 96, "a donde hay")
    renglon(b, x0 + 630, yy + 98, x0 + 880)
    pista(b, x0 + 896, yy + 96, "(más / menos)")
    yy += 134
    return frase_hueco(b, x0, yy, ww, "La columna de la tabla que tiene mis dos datos (carga y dirección) es: "
                                      "____________________ .", c)


# ───────── QC · N.º 75 · síntesis de proteínas ─────────
def datos_75(b, x, y, w):
    c = A["color"]
    cx0, cy0, cw_, ch = x + 40, y + 6, 960, 250
    b.append(rect(cx0, cy0, cw_, ch, VERDE_CEL, r=60, stroke=c, sw=2.4))
    # núcleo con ADN y la transcripción
    nx, ny = cx0 + 190, cy0 + 122
    b.append(f'<circle cx="{nx}" cy="{ny}" r="104" fill="white" stroke="{c}" stroke-width="2.2"/>')
    pts = " ".join(f"{nx - 70 + i * 14},{ny - 50 + (12 if i % 2 else -12)}" for i in range(11))
    b.append(f'<polyline points="{pts}" fill="none" stroke="{INK}" stroke-width="2.4"/>')
    b.append(T(nx - 96, ny - 46, ["ADN"], 15, INK, weight="700", anchor="end"))
    b.append(f'<line x1="{nx}" y1="{ny - 30}" x2="{nx}" y2="{ny + 14}" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<polygon points="{nx - 7},{ny + 8} {nx + 7},{ny + 8} {nx},{ny + 20}" fill="{INK}"/>')
    b.append(T(nx + 12, ny - 2, ["Transcripción"], 15, INK, weight="700"))
    b.append(T(nx - 64, ny + 40, ["ARNm"], 15, INK, weight="700"))
    b.append(T(nx, ny + 124, ["Núcleo"], 14, GRAY, style="italic", anchor="middle"))
    # el ARNm sale del núcleo hasta el ribosoma (trazo ondulado)
    rx_, ry_ = cx0 + 640, cy0 + 142
    ondas = [(nx - 20 + t * 9, ny + 28 + 7 * math.sin(t * 0.9)) for t in range(int((rx_ - 40 - nx + 20) / 9))]
    b.append('<polyline points="' + " ".join(f"{a:.0f},{b_:.0f}" for a, b_ in ondas) +
             f'" fill="none" stroke="{INK}" stroke-width="2.6"/>')
    # ribosoma, cadena de proteína, aminoácido y ARNt
    b.append(f'<ellipse cx="{rx_}" cy="{ry_ - 22}" rx="58" ry="34" fill="white" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<ellipse cx="{rx_}" cy="{ry_ + 18}" rx="46" ry="22" fill="white" stroke="{INK}" stroke-width="2"/>')
    b.append(T(rx_ + 70, ry_ - 40, ["Ribosoma"], 15, INK, weight="700"))
    for k in range(5):
        b.append(f'<circle cx="{rx_ - 30 - k * 26}" cy="{ry_ - 70 - k * 6}" r="10" fill="white" stroke="{INK}" '
                 f'stroke-width="1.8"/>')
    b.append(T(rx_ - 200, ry_ - 112, ["Proteína"], 15, INK, weight="700"))
    ax, ay = rx_ + 150, ry_ + 20
    b.append(f'<circle cx="{ax}" cy="{ay}" r="10" fill="white" stroke="{INK}" stroke-width="1.8"/>')
    b.append(f'<path d="M {ax - 12} {ay + 16} L {ax + 12} {ay + 16} L {ax} {ay + 38} Z" fill="white" '
             f'stroke="{INK}" stroke-width="1.8"/>')
    b.append(T(ax + 24, ay + 6, ["Aminoácido"], 15, INK, weight="700"))
    b.append(T(ax + 24, ay + 36, ["ARNt"], 15, INK, weight="700"))
    b.append(T(rx_, ry_ + 66, ["Traducción"], 15, INK, weight="700", anchor="middle"))
    b.append(T(cx0 + 420, cy0 + 236, ["Citoplasma"], 14, GRAY, style="italic"))
    yy = cy0 + ch + 6
    return pregunta(b, x, yy, w, "De acuerdo con el modelo, si no se copia correctamente la información del ADN al "
                                 "ARNm en el proceso de transcripción, ¿qué puede sucederle al proceso de síntesis "
                                 "de proteínas?")


def ii3(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Una copia con error y quién la lee después", c,
                      "La misma ruta de la misión, con mensajes: escribe qué lee cada uno. Después mete el error "
                      "en la copia y síguelo.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 54
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("EL ADN · EL ORIGINAL", "dónde está y quién lo copia"),
                                  ("EL ARNm · LA COPIA", "aquí va el error: ¿a dónde viaja?"),
                                  ("EL RIBOSOMA · EL LECTOR", "qué lee y qué va uniendo"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 140, c, r=16, dash="8,6" if k == 1 else None)
        rot(b, bx + 18, yy + 28, rt, c, size=13)
        pista(b, bx + 18, yy + 52, ps, size=14)
        renglon(b, bx + 18, yy + 92, bx + bw - 18)
        renglon(b, bx + 18, yy + 128, bx + bw - 18)
        if k < n - 1:
            flecha(b, bx + bw + 6, yy + 70, bx + bw + gap - 6, yy + 70, c, sw=3, head=14)
    yy += 156
    return frase_hueco(b, x0, yy, ww, "Si la copia trae un error, el ribosoma une aminoácidos según ____________ "
                                      "y no según ____________ .", c)


# ───────── QD · N.º 58 · insecticidas ─────────
CUCAS = (("Caja 1", "Insecticida 1", "90 %"), ("Caja 2", "Insecticida 2", "80 %"),
         ("Caja 3", "Insecticida 3", "70 %"), ("Caja 4", "Insecticida 4", "50 %"),
         ("Caja 5", "Sin insecticida", "50 %"))


def datos_58(b, x, y, w):
    c = A["color"]
    ws = (230, 260, 300)
    tx = x
    yy = y + 6
    for k, cl in enumerate(("Caja con las cucarachas", "Tratamiento", "% de cucarachas sobrevivientes")):
        b.append(rect(tx + sum(ws[:k]), yy, ws[k], 34, A["bg"], r=0, stroke=c, sw=1.4))
        b.append(T(tx + sum(ws[:k]) + ws[k] / 2, yy + 23, [cl], 15, INK, weight="700", anchor="middle"))
    yy += 34
    for fila in CUCAS:
        for k, v in enumerate(fila):
            b.append(rect(tx + sum(ws[:k]), yy, ws[k], 30, "white", r=0, stroke=c, sw=1.4))
            b.append(T(tx + sum(ws[:k]) + ws[k] / 2, yy + 21, [v], 15, INK, anchor="middle"))
        yy += 30
    return pregunta(b, x, yy + 4, w, "Con estos resultados, los investigadores concluyeron: «El insecticida 4 es el "
                                     "más efectivo». Con base en la información anterior, ¿la conclusión de los "
                                     "investigadores es válida?")


def ii4(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Resta lo que pasa sin echar nada", c,
                      "Como en la pregunta 3: todo se compara con el grupo que no recibió tratamiento. Calcula "
                      "cuántas murieron en cada caja y compáralo con la caja 5.")
    x0, ww = x + 22, w - 44
    for k in range(5):
        bx = x0 + k * (ww / 5)
        caja(b, bx + 4, yy, ww / 5 - 8, 110, c, r=12)
        rot(b, bx + 20, yy + 26, f"CAJA {k + 1}", c, size=13)
        pista(b, bx + 20, yy + 56, "murieron:", size=14)
        caja(b, bx + 100, yy + 34, ww / 5 - 120, 34, c, r=6)
        pista(b, bx + 20, yy + 96, "¿más que la 5? ___" if k < 4 else "la referencia", size=14)
    yy += 124
    return frase_hueco(b, x0, yy, ww, "Caja 4 menos caja 5: ______ cucarachas muertas de diferencia. Entonces el "
                                      "insecticida 4 ______________ .", c)


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="En las células animales los lisosomas son los organelos encargados de digerir con enzimas los "
            "nutrientes que la célula consume. Si todos los lisosomas de una célula se rompieran, ¿qué le "
            "sucedería inicialmente a la célula?",
          o=["Se degradarían moléculas en su interior.",
             "Perdería todo el agua del citoplasma.",
             "No habría respiración celular.",
             "No se formarían proteínas."],
          inst=ii1)
QB = dict(est=4, comp="Explicación de fenómenos",
          e="La tabla muestra algunos tipos de transporte celular, sus características y un ejemplo de célula animal.",
          o=["Transporte activo.", "Difusión facilitada.", "Difusión simple.", "Ósmosis."],
          datos=datos_93, inst=ii2)
QC = dict(est=2, comp="Explicación de fenómenos",
          e="En el modelo se presenta el proceso de síntesis de proteínas en una célula.",
          o=["Se produciría una cadena de ARNm doble como la molécula de ADN.",
             "El ribosoma no podría entrar al núcleo a leer la información del ADN.",
             "Los aminoácidos no podrían unirse al ARNt en el citoplasma.",
             "Se unirían aminoácidos que no corresponden con la secuencia de ADN."],
          datos=datos_75, inst=ii3)
QD = dict(est=3, comp="Indagación",
          e="Un grupo de investigadores quería determinar la efectividad de cuatro insecticidas para controlar las "
            "plagas de cucarachas. Separaron a 500 cucarachas en grupos de 100. Cada grupo fue encerrado en una caja "
            "de vidrio con un insecticida diferente y a los tres días se determinó el porcentaje de cucarachas "
            "sobrevivientes. Los resultados se muestran en la tabla.",
          o=["No, porque con los otros tres insecticidas murieron más cucarachas.",
             "Sí, porque el insecticida mató más rápido a las cucarachas.",
             "No, porque un mismo porcentaje muere sin insecticida.",
             "Sí, porque el insecticida mata más cucarachas adultas."],
          datos=datos_58, inst=ii4)


def build(pages=(142, 146)):
    return [hoja_icfes("bio1_i1", pages[0], QA, QB),
            hoja_icfes("bio1_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
