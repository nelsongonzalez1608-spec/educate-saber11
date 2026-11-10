#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 1 · entrenamiento ICFES · páginas 185 y 189.

Cuatro preguntas de Ciencias Naturales con contenido de química, de dos fuentes en Drive:
  · «1. CUADERNILLOS ICFES» / «2016-1 PRIMERA SESION.pdf»: cuadernillo oficial Saber 11 2016-1,
    primera sesión, AAM; encabezado de Ciencias Naturales «Saber 11 - 083 - B05R - AAM · 1a. sesión».
    Ítems 115 y 105 (verificados contra la página escaneada).
  · «SIMULACRO II 2023-OFICIO-C.NATURALES - química.pdf» (simulacro de seguimiento, banco de
    química; CLAUDE.md § 10 lo lista entre las fuentes): ítems 46 y 252. NO se pudieron verificar
    contra un cuadernillo liberado del ICFES: el PDF pesa 30 MB y solo se leyó su texto. Las
    opciones se tomaron en el orden en que aparecen en ese texto. Se usan porque en los dos
    cuadernillos oficiales de Drive ya no quedaban preguntas de química sin usar o sin reservar
    (Biología y Química M3 a M6). Registrado en qui1_icfes.csv y en el informe.
Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11», sin año ni «oficial».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · 1.ª ses. N.º 115 · C   (1 N₂ + 3 H₂ → 2 NH₃: se producen 2 mol)            estrategia 1
    QB · Sim. II 2023 N.º 46 · C (punto de fusión y solubilidad en agua)          estrategia 2
    QC · Sim. II 2023 N.º 252 · D (la de los gases baja al subir la temperatura)  estrategia 3
    QD · 1.ª ses. N.º 105 · B   (ácido carboxílico de cadena larga + NaOH)          estrategia 4

  46 · Códigos con cada propuesta: solo punto de fusión → 150, 150, 80, 80 (se repiten); densidad
       y solubilidad en etanol → 1 y 2 quedan iguales (1,0 · soluble); punto de fusión y
       solubilidad en agua → 150-sí, 150-no, 80-sí, 80-no: los cuatro distintos (C); densidad y
       solubilidad en agua → 1 y 3 quedan iguales (1,0 · soluble).
  252 · AgNO₃, KCl y NaCl suben de 0 a 80 °C; O₂, CO₂ y He bajan. Solo D es cierta.
  105 · A es un éster (acetato de decilo) + NaOH; C una amida + HCl; D el mismo ácido de B
       pero con HCl, que no es base. B: CH₃(CH₂)₁₀COOH (ácido láurico) + NaOH.

Adaptaciones (registradas en qui1_icfes.csv): en la N.º 105 las cuatro parejas se escriben con
fórmula semidesarrollada en vez de la fórmula de esqueleto del cuadernillo (mismos átomos).
"""
from qui1 import *   # noqa: F401,F403  (configura la misión y EST)
from qui1 import rot, caja, pista, texto, renglon, hueco, frase_hueco, flecha, marca


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


def tabla(b, x, y, cols, filas, ws, c, h=32, size=15):
    """Tabla sencilla: encabezado con fondo de la misión y filas blancas."""
    for k, cl in enumerate(cols):
        b.append(rect(x + sum(ws[:k]), y, ws[k], h + 2, A["bg"], r=0, stroke=c, sw=1.4))
        b.append(T(x + sum(ws[:k]) + ws[k] / 2, y + h / 2 + 7, [cl], size, INK, weight="700", anchor="middle"))
    y += h + 2
    for fila in filas:
        for k, v in enumerate(fila):
            b.append(rect(x + sum(ws[:k]), y, ws[k], h, "white", r=0, stroke=c, sw=1.4))
            b.append(T(x + sum(ws[:k]) + ws[k] / 2, y + h / 2 + 6, [v], size, INK, anchor="middle"))
        y += h
    return y


# ───────── QA · 1.ª sesión N.º 115 · amoníaco ─────────
def datos_115(b, x, y, w):
    texto(b, x + w / 2 - 120, y + 34, "1 N₂  +  3 H₂   →   2 NH₃", 26, INK, weight="700", anchor="start")
    return pregunta(b, x, y + 48, w, "Teniendo en cuenta la información anterior, puede afirmarse que en la anterior "
                                     "reacción se produce(n)")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Los moles no se suman: los átomos se cuentan", c,
                      "Igual que en la pregunta 9: los números de la ecuación son la receta en moles. Cuenta los "
                      "átomos a cada lado de la flecha y lee la receta antes de mirar las opciones.")
    x0, ww = x + 22, w - 44
    cols = ("ÁTOMOS", "A LA IZQUIERDA (1 N₂ + 3 H₂)", "A LA DERECHA (2 NH₃)")
    xs = (0, 180, 640)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=13)
    for j, el in enumerate(("de nitrógeno (N)", "de hidrógeno (H)")):
        ry = yy + 28 + j * 54
        caja(b, x0, ry, ww, 46, c, r=10)
        texto(b, x0 + 16, ry + 30, el, 16)
        texto(b, x0 + xs[1] + 40, ry + 30, "____ × ____ = ____", 17)
        texto(b, x0 + xs[2] + 40, ry + 30, "____ × ____ = ____", 17)
    yy += 28 + 2 * 54 + 8
    return frase_hueco(b, x0, yy, ww, "La receta en moles:  1 de N₂  :  3 de H₂  :  ____ de NH₃     "
                                      "y con 2 mol de N₂ saldrían ____ mol de NH₃", c)


# ───────── QB · Sim. II 2023 N.º 46 · cuatro botellas ─────────
SOLIDOS = (("Sólido 1", "1,0", "150", "Soluble", "Soluble"), ("Sólido 2", "1,0", "150", "Insoluble", "Soluble"),
           ("Sólido 3", "1,0", "80", "Soluble", "Insoluble"), ("Sólido 4", "2,0", "80", "Insoluble", "Insoluble"))


def datos_46(b, x, y, w):
    c = A["color"]
    yy = tabla(b, x, y + 8, ("", "Densidad (g/cm³)", "Punto de fusión (°C)", "Solubilidad en agua",
                             "Solubilidad en etanol"), SOLIDOS, (150, 200, 220, 220, 220), c, h=30)
    return pregunta(b, x, yy + 2, w, "¿Qué propiedades deben medir los estudiantes en el laboratorio para saber qué "
                                     "sólido corresponde a cada botella?")


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Un código distinto para cada botella", c,
                      "Como con el hierro y el azufre: la propiedad sirve si deja a cada sólido con un código que "
                      "no se repite. Escoge dos propiedades, escribe el código de cada botella y mira si se repite. "
                      "Si se repite, prueba otra pareja.")
    x0, ww = x + 22, w - 44
    cols = ("", "MI PRUEBA 1: ______ + ______", "MI PRUEBA 2: ______ + ______")
    xs = (0, 160, 690)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=13)
    for j in range(4):
        ry = yy + 26 + j * 44
        caja(b, x0, ry, ww, 38, c, r=8)
        texto(b, x0 + 16, ry + 26, f"botella {j + 1}", 16)
        pista(b, x0 + xs[1], ry + 26, "código:", size=14)
        renglon(b, x0 + xs[1] + 60, ry + 28, x0 + xs[2] - 40)
        pista(b, x0 + xs[2], ry + 26, "código:", size=14)
        renglon(b, x0 + xs[2] + 60, ry + 28, x0 + ww - 20)
    yy += 26 + 4 * 44 + 4
    texto(b, x0 + xs[1], yy + 18, "¿se repite algún código?   sí  /  no", 15, GRAY)
    texto(b, x0 + xs[2], yy + 18, "¿se repite algún código?   sí  /  no", 15, GRAY)
    return yy + 26


# ───────── QC · Sim. II 2023 N.º 252 · solubilidad y temperatura ─────────
SOLUB = (("AgNO₃ (s)", "1220", "3760", "6690"), ("KCl (s)", "276", "400", "511"), ("NaCl (s)", "357", "366", "384"),
         ("O₂ (g)", "0,069", "0,031", "0,014"), ("CO₂ (g)", "3,374", "0,97", "0"),
         ("He (g)", "0,00167", "0,00152", "0,00137"))


def datos_252(b, x, y, w):
    c = A["color"]
    texto(b, x + 2, y + 22, "Solubilidad a diferentes temperaturas (g de soluto/kg de agua)", 15, INK, weight="700")
    yy = tabla(b, x, y + 32, ("Sustancia", "0 °C", "40 °C", "80 °C"), SOLUB, (220, 170, 170, 170), c, h=28)
    return pregunta(b, x, yy + 2, w, "De la información presentada en la tabla, es válido afirmar que la solubilidad "
                                     "de los tres")


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Sólidos de un lado, gases del otro", c,
                      "Lo de la pregunta 5, con seis sustancias. Pon una flecha (sube o baja) en cada fila y después "
                      "escribe lo que tienen en común los de cada grupo.")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    for k, (rt, sus) in enumerate((("LOS SÓLIDOS (s)", ("AgNO₃", "KCl", "NaCl")), ("LOS GASES (g)", ("O₂", "CO₂", "He")))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 190, c, r=14)
        rot(b, bx + 18, yy + 28, rt, c, size=14)
        pista(b, bx + 200, yy + 28, "de 0 °C a 80 °C la solubilidad", size=14)
        for j, s in enumerate(sus):
            ry = yy + 52 + j * 38
            texto(b, bx + 24, ry + 22, s, 17, INK, weight="700")
            marca(b, bx + 140, ry + 4, "sube", c)
            marca(b, bx + 260, ry + 4, "baja", c)
        pista(b, bx + 18, yy + 178, "los tres:", size=14)
        renglon(b, bx + 90, yy + 180, bx + half - 18)
    return yy + 190


# ───────── QD · 1.ª sesión N.º 105 · el jabón ─────────
def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "La ficha del jabón: tres requisitos", c,
                      "El texto da la receta completa. Escribe los tres requisitos y revisa cada pareja contra los "
                      "tres: la que falla en uno ya no hace jabón, por buena que se vea.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 20
    bw = (ww - gap * (n - 1)) / n
    for k, ps in enumerate(("el grupo que debe tener", "cómo debe ser la cadena", "con qué debe reaccionar")):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 74, c, r=12)
        rot(b, bx + 16, yy + 24, f"REQUISITO {k + 1}", c, size=13)
        pista(b, bx + 16, yy + 44, ps, size=14)
        renglon(b, bx + 16, yy + 66, bx + bw - 16)
    yy += 84
    texto(b, x0, yy + 22, "Para leer las fórmulas:   –COOH ácido carboxílico     –COO– entre dos carbonos: éster     "
                          "–CONH₂ amida", 15, GRAY)
    texto(b, x0, yy + 48, "¿NaOH es ácido o base? ________     ¿HCl es ácido o base? ________", 16, INK)
    return yy + 58


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="Cuando reacciona 1 mol de N₂ y 3 moles de H₂ se produce NH₃, como se muestra en la siguiente ecuación "
            "química.",
          o=["1 mol de NH₃.", "4 moles de NH₃.", "2 moles de NH₃.", "6 moles de NH₃."],
          datos=datos_115, inst=ii1)
QB = dict(est=2, comp="Indagación",
          e="Unos estudiantes tienen cuatro botellas sin marcar. Se sabe que en cada una de ellas se tiene un sólido "
            "diferente. Estos sólidos tienen las propiedades que se muestran en la tabla:",
          o=["Determinar el punto de fusión.", "Determinar la densidad y la solubilidad en etanol.",
             "Determinar el punto de fusión y la solubilidad en agua.",
             "Determinar la densidad y la solubilidad en agua."],
          datos=datos_46, inst=ii2)
QC = dict(est=3, comp="Uso comprensivo del conocimiento científico",
          e="A continuación, se muestra la solubilidad en agua de algunas sustancias a varias temperaturas y 1 atm "
            "de presión.",
          o=["sólidos disminuye cuando aumenta la temperatura.", "gases disminuye cuando disminuye la temperatura.",
             "sólidos es la única que se afecta con la variación de la temperatura.",
             "gases disminuye cuando aumenta la temperatura."],
          datos=datos_252, inst=ii3)
QD = dict(est=4, comp="Uso comprensivo del conocimiento científico",
          e="El proceso por el cual se obtienen los jabones consiste en la reacción entre un ácido carboxílico (-COOH), "
            "conformado por una cadena larga de átomos de carbono, y un hidróxido o base. A partir de esta "
            "información, ¿cuál de las siguientes parejas de moléculas puede usarse para la obtención de jabón?",
          o=["CH₃–(CH₂)₉–O–CO–CH₃   +   NaOH", "CH₃–(CH₂)₁₀–COOH   +   NaOH",
             "CH₃–(CH₂)₈–CONH₂   +   HCl", "CH₃–(CH₂)₁₀–COOH   +   HCl"],
          inst=ii4)


def build(pages=(185, 189)):
    return [hoja_icfes("qui1_i1", pages[0], QA, QB),
            hoja_icfes("qui1_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
