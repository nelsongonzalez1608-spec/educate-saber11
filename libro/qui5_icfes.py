#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 5 · entrenamiento ICFES · páginas 213 y 217.

Fuente de las cuatro: «SIMULACRO II 2023-OFICIO-C.NATURALES - química.pdf» (Drive, id
1Y3haiTqbOoRuayZ3pDTD_CTWMGXwpntx), sección Ciencias Naturales · Química; numeración continua
del compilado. Leídas en la versión de texto del archivo (30 MB, no se puede descargar el PDF):
los enunciados, las tablas y las opciones salen completos en el texto; donde el original trae
una figura que no se pudo ver, se dice abajo. Ninguna estaba en tablero/icfes.csv; reservadas en
tablero/propuestas/qui_icfes_reservas.csv. Fuente del proyecto según CLAUDE.md § 10.

Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · N.º 347 · B   (cuatro compuestos · qué concluir del punto de ebullición)   estrategia 1
    QB · N.º 11  · C   (masa y volumen de dos materiales · ¿cuál es menos denso?)   estrategia 3
    QC · N.º 166 · C   (masa molecular del ácido carbónico)                         estrategia 2
    QD · N.º 9   · C   (combustible de aceite de palma · por qué es positivo)       estrategia 4

  347 · B: puntos de ebullición 36 (pentano), 47 (cloruro de propilo), 76 (butiraldehído) y
        118 °C (alcohol butílico): el mayor es el del alcohol. A cae (el pentano tiene 5 C y el
        menor punto); C cae (el menor es el pentano); D cae (pentano y butiraldehído pesan 72 y
        hierven a 36 y 76). La columna de estructuras del original se reemplaza por la fórmula
        condensada de cada compuesto.
   11 · C: material 1: 10/12 = 20/24 = 40/48 ≈ 0,83 g/cm³; material 2: 10/16 = 20/32 = 30/48 =
        0,625 g/cm³. Con 10 g, el material 2 ocupa 16 cm³ y el 1, 12 cm³. A da la razón
        equivocada; B y D dicen «incorrecta».
  166 · C: H₂CO₃ = 2 × 1 + 1 × 12 + 3 × 16 = 62 g/mol. B (32) sale de sumar números atómicos
        (2 × 1 + 6 + 3 × 8); A (29) olvida un H y dos O.
    9 · C: el combustible de palma no tiene azufre detectado (no produce SO₂) y se obtiene de un
        cultivo que se vuelve a sembrar. B: su «capacidad calorífica» es MENOR (39,5 frente a
        45,4 MJ/kg); A: los pozos son del petróleo; D: tener menos energía no es lo positivo.
        Hallazgo: la Tabla 2 llama «capacidad calorífica» a un dato en MJ/kg que es poder
        calorífico (energía liberada al quemarse), y la define como «energía para aumentar un
        grado la temperatura». La Tabla 1 (proceso del aceite) se resume en una línea.
"""
from qui5 import *   # noqa: F401,F403  (configura la misión y EST)
from qui5 import rot, caja, pista, renglon, texto, sino, tinte, tabla_vacia

FUENTE = "SIMULACRO II 2023-OFICIO-C.NATURALES - química.pdf"


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


# ───────── QA · N.º 347 · punto de ebullición ─────────
def datos_347(b, x, y, w):
    cols = ((300, "Nombre"), (330, "Fórmula condensada"), (150, "PM (g/mol)"), (130, "μ (D)"),
            (150, "Pe (°C)"))
    filas = (("1 · n-pentano", "CH₃–CH₂–CH₂–CH₂–CH₃", "72", "0", "36"),
             ("2 · cloruro de n-propilo", "CH₃–CH₂–CH₂–Cl", "78,5", "2,10", "47"),
             ("3 · butiraldehído", "CH₃–CH₂–CH₂–CHO", "72", "2,72", "76"),
             ("4 · alcohol n-butílico", "CH₃–CH₂–CH₂–CH₂–OH", "74", "1,63", "118"))
    yy = tabla(b, x, y + 4, cols, filas)
    pista(b, x, yy + 22, "PM: peso molecular · μ: momento dipolar (polaridad) · Pe: punto de ebullición")
    return pregunta(b, x, yy + 30, w, "De acuerdo con los datos de la tabla, se puede concluir que")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Qué grupo tiene cada molécula y a cuánto hierve", c,
                      "Como con el éster del biodiésel: el grupo funcional cambia la propiedad. Escribe el grupo de "
                      "cada compuesto y pon en orden los puntos de ebullición.")
    x0, ww = x + 22, w - 44
    cw = (ww - 3 * 14) / 4
    for k, n in enumerate(("1", "2", "3", "4")):
        bx = x0 + k * (cw + 14)
        caja(b, bx, yy, cw, 96, c, r=12)
        rot(b, bx + 14, yy + 26, f"COMPUESTO {n}", c, size=13)
        pista(b, bx + 14, yy + 52, "grupo:")
        renglon(b, bx + 66, yy + 54, bx + cw - 14)
        pista(b, bx + 14, yy + 84, "puesto (1.º = hierve más):")
        renglon(b, bx + 196, yy + 86, bx + cw - 14)
    return yy + 96


# ───────── QB · N.º 11 · densidad ─────────
def datos_11(b, x, y, w):
    cols = ((210, ""), (130, "Muestra 1"), (130, "Muestra 2"), (130, "Muestra 3"),
            (130, "Muestra 1"), (130, "Muestra 2"), (130, "Muestra 3"))
    texto(b, x + 210 + 195, y + 22, "Material 1", size=16, weight="700", anchor="middle")
    texto(b, x + 210 + 390 + 195, y + 22, "Material 2", size=16, weight="700", anchor="middle")
    filas = (("Masa (g)", "10", "20", "40", "10", "20", "30"),
             ("Volumen (cm³)", "12", "24", "48", "16", "32", "48"))
    yy = tabla(b, x, y + 32, cols, filas)
    return pregunta(b, x, yy + 6, w,
                    "Al consultar en un libro, el estudiante encontró que la densidad de un material es la razón "
                    "entre la masa del material y el volumen que ocupa este. Con esta información y los resultados "
                    "del estudio, él concluyó que «el material 2 es menos denso que el material 1». La conclusión del "
                    "estudiante es")


def ii2(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Divide masa entre volumen, muestra por muestra", c,
                      "Como con las bolsas del PLA: primero el dato, después la conclusión. Calcula las seis "
                      "densidades y mira si cada material da siempre lo mismo.")
    x0, ww = x + 22, w - 44
    cols = (230, (ww - 230) / 4, (ww - 230) / 4, (ww - 230) / 4, (ww - 230) / 4)
    return tabla_vacia(b, x0, yy, cols, ("", "MUESTRA 1", "MUESTRA 2", "MUESTRA 3", "¿SIEMPRE IGUAL?"),
                       ("Material 1 (g/cm³)", "Material 2 (g/cm³)"), c, rh=46, hh=38, size=16)


# ───────── QC · N.º 166 · masa molecular ─────────
def datos_166(b, x, y, w):
    yy = pregunta(b, x, y, w, "La siguiente tabla presenta las masas y números atómicos de diferentes elementos.")
    cols = ((240, "Elemento"), (220, "Número atómico"), (260, "Masa atómica (g/mol)"))
    yy = tabla(b, x, yy + 10, cols, (("Hidrógeno · H", "1", "1"), ("Oxígeno · O", "8", "16"),
                                     ("Carbono · C", "6", "12")))
    return pregunta(b, x, yy + 6, w, "A partir de la información anterior, ¿cuál es la masa molecular del ácido "
                                     "carbónico, H₂CO₃?")


def ii3(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Átomo por átomo: el ácido carbónico", c,
                      "Como en la receta del biodiésel: los subíndices dicen cuántos hay de cada uno. Llena cada "
                      "fila con la columna correcta de la tabla y suma.")
    x0, ww = x + 22, w - 44
    cols = (200, (ww - 200) / 4, (ww - 200) / 4, (ww - 200) / 4, (ww - 200) / 4)
    return tabla_vacia(b, x0, yy, cols, ("ÁTOMO", "¿CUÁNTOS HAY?", "× MASA (g/mol)", "= SUBTOTAL", "COLUMNA QUE USÉ"),
                       ("H", "C", "O", "total"), c, rh=40, hh=36, size=16)


# ───────── QD · N.º 9 · aceite de palma ─────────
PALMA = ("En una empresa se producen dos tipos de combustible: fósil y aceite de palma. Para producir el combustible "
         "fósil se extrae petróleo de pozos; para producir el de aceite de palma se extraen los frutos de la palma y "
         "se procesan (Tabla 1: esterilización, separación, extracción del aceite, clarificación y purificación, en "
         "la que se filtran las impurezas). Después se agregan otros compuestos al petróleo y al aceite para usarlos "
         "como combustible. En la Tabla 2 se muestran algunas de sus propiedades.")


def datos_9(b, x, y, w):
    cols = ((330, "Propiedad"), (300, "Aceite de palma"), (300, "Combustible fósil"))
    filas = (("Azufre (% de masa)*", "No detectado", "0,819"),
             ("Punto de inflamación (°C)", "162,3", "62,3"),
             ("Capacidad calorífica (MJ/kg)**", "39,5", "45,4"))
    yy = tabla(b, x, y + 4, cols, filas)
    svg, yy = TJ(x, yy + 22, "* Produce dióxido de azufre (SO₂), que contribuye a la contaminación ambiental. "
                             "** Así la llama la tabla: «energía necesaria para aumentar un grado centígrado la "
                             "temperatura del combustible».", w, 15, GRAY, style="italic", lh=20)
    b.append(svg)
    return pregunta(b, x, yy, w, "En una población que se dedica a plantar palma, se deja de utilizar combustible "
                                 "fósil para utilizar exclusivamente el combustible proveniente del aceite de palma. "
                                 "Teniendo en cuenta la información anterior, ¿por qué es positivo para la población "
                                 "utilizar combustible con aceite de palma?")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Lo que sale del tubo y lo que se vuelve a sembrar", c,
                      "Como con el biodiésel: mira qué sale al quemarlo y de dónde viene. Una razón vale si las dos "
                      "partes de la opción se sostienen con la tabla.")
    x0, ww = x + 22, w - 44
    cols = (380, (ww - 380) / 2, (ww - 380) / 2)
    return tabla_vacia(b, x0, yy, cols, ("", "ACEITE DE PALMA", "FÓSIL"),
                       ("¿Suelta SO₂ al quemarse?", "¿Se puede volver a producir?", "¿Cuál tiene más MJ/kg?"),
                       c, rh=40, hh=36, size=16)


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="La tabla indica algunas características de un grupo pequeño de compuestos orgánicos.",
          o=["a mayor cantidad de carbonos del compuesto, mayor será el punto de ebullición.",
             "el alcohol tiene el mayor punto de ebullición.",
             "el cloruro de propilo, al tener la mayor cantidad de hidrógenos, presenta el menor punto de ebullición.",
             "el peso molecular es directamente proporcional al punto de ebullición."],
          datos=datos_347, inst=ii1)
QB = dict(est=3, comp="Indagación",
          e="Un estudiante hizo un experimento para determinar la densidad de dos materiales diferentes. Los "
            "resultados se presentan en la siguiente tabla.",
          o=["correcta, porque el aumento de la masa para los dos materiales es aproximadamente constante.",
             "incorrecta, porque para el mismo volumen la masa del material 1 es mayor que la del material 2.",
             "correcta, porque para la misma masa el volumen del material 2 es mayor que el volumen del material 1.",
             "incorrecta, porque la densidad para los dos materiales es aproximadamente constante."],
          datos=datos_11, inst=ii2)
QC = dict(est=2, comp="Uso comprensivo del conocimiento científico",
          e="La masa molecular de un compuesto se determina mediante la sumatoria de las masas atómicas de cada uno "
            "de los elementos que lo conforman.",
          o=["29 g/mol.", "32 g/mol.", "62 g/mol.", "86 g/mol."],
          datos=datos_166, inst=ii3)
QD = dict(est=4, comp="Explicación de fenómenos", e=PALMA,
          o=["Porque el aceite del que se produce es transparente, y para su producción se perforan pozos en el suelo.",
             "Porque en el proceso de producción se separan todas las impurezas y su capacidad calorífica es alta.",
             "Porque no produce dióxido de azufre, y la población puede continuar plantando palmas.",
             "Porque tiene menos energía que el combustible fósil, y los frutos son fáciles de extraer."],
          datos=datos_9, inst=ii4)


def build(pages=(213, 217)):
    return [hoja_icfes("qui5_i1", pages[0], QA, QB),
            hoja_icfes("qui5_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
