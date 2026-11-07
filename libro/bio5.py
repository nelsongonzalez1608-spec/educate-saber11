#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 5 · componente entorno biológico · páginas 168–174.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 5» de Biología (fuente_libro/BIOLOGIA), páginas 116–119.
Contenido: el pedigrí de una enfermedad rara (1), maíz convencional y maíz editado con CRISPR
(2 a 4), la radiación de las bombas atómicas (5), consanguinidad y predicción (6), resistencia
a antibióticos por plásmidos (7) y los perros «de diseño» como el Pomsky (8 a 10).

Claves verificadas (resueltas a mano contra el texto y las figuras del libro, 7 nov 2026):

    1·B  2·D  3·C  4·A  5·A  6·D  7·B  8·D  9·A  10·C

  1 · Generación 1: padre y madre sanos; generación 2: una hija y un hijo afectados. Dos padres
      sanos con hijos afectados → no es dominante (A y C caen). La hija afectada tiene padre sano
      → no es ligada al X recesiva (D cae; además D afirma algo falso: la portadora no transmite
      a TODOS sus hijos varones, solo a la mitad en promedio). Queda autosómica recesiva (B).
      Además A es falsa en su razón: las generaciones 1 y 4 no tienen afectados.
  2 · D: el gen editado da resistencia → menos plaguicida → menos contaminación (la ilustración).
  3 · C: es la única que mide biodiversidad (especies de insectos) y compara las dos parcelas.
  4 · A: sin variabilidad, una plaga nueva encuentra a todas las plantas igual de vulnerables.
  5 · A: radiación ionizante → rompe el ADN → mutaciones (somáticas → cáncer; germinales →
      descendencia). B (calor), C (recesivo → dominante) y D (copias que «fortalecen») son falsas.
  6 · D: la consanguinidad aumenta la homocigosis (aa). Ojo: la premisa de A es cierta (la
      frecuencia del alelo no cambia), la conclusión no. El contexto que cita la pregunta no
      existe en el libro: hallazgo.
  7 · B: el plásmido se transfiere entre bacterias; el antibiótico selecciona a las que lo tienen.
  8 · D: es la única pregunta que relaciona la variable causa (consanguinidad) con el efecto
      (enfermedades hereditarias).
  9 · A: escasez → cruces entre parientes → más homocigotos recesivos.
 10 · C: la única que reconoce beneficio y riesgo; A, B y D cierran con absolutos.

Reparto: A 3 · B 2 · C 2 · D 3. Equilibrado. Patrón: en 2, 4, 9 y 10 la correcta es la más
larga o la que «integra»; en 10 las tres incorrectas cierran con absolutos. Registrado como
Atención en tablero/propuestas/bio5_hallazgos.csv.

Estrategias:
    1 · Seguir el alelo por la familia             (1, 6, 9  · ICFES N.º 66)   azul
    2 · Del cambio en el ADN a lo que se ve        (2, 5, 7  · ICFES N.º 55)   rojo
    3 · La prueba que sí responde la pregunta      (3, 8     · ICFES N.º 63)   morado
    4 · Lo que gana, lo que arriesga, lo que exagera (4, 10  · ICFES N.º 56)   oro

Hojas: 168 bio5_t1 (1-2) · 169 bio5_t2 (3-4) · 170 bio5_i1 · 171 bio5_t3 (5-6) ·
       172 bio5_t4 (7-8) · 173 bio5_t5 (9-10) · 174 bio5_i2.
"""
import math

from taller_base import *

configurar("Biología", 5, "entorno biológico",
           tema="Lo que se hereda, lo que se edita y lo que se arriesga",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Seguir el alelo por la familia", EDU_AZUL),
       2: ("Del cambio en el ADN a lo que se ve", EDU_ROJO),
       3: ("La prueba que sí responde la pregunta", MORADO),
       4: ("Lo que gana, lo que arriesga, lo que exagera", EDU_ORO)}
usar_estrategias(EST)
AZ, RO, MO, OR = (EST[k][1] for k in (1, 2, 3, 4))
GRIS_AF = "#B4BAC4"        # relleno de «afectado» en el pedigrí (dato de la figura, no pista)


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def texto(b, x, y, txt, size=17, color=INK, weight="400", anchor="start"):
    b.append(T(x, y, [txt], size, color, weight=weight, anchor=anchor))


def parrafo(b, x, y, w, txt, size=17, color=INK, style="normal", weight="400"):
    svg, yy = TJ(x, y, txt, w, size, color, style=style, weight=weight, lh=size + 8)
    b.append(svg)
    return yy


def sino(b, x, y, c, labels=("sí", "no"), gap=80):
    for j, lab in enumerate(labels):
        b.append(checkbox(x + j * gap, y, s=10, c=c))
        b.append(T(x + 28 + j * gap, y + 17, [lab], 16, GRAY))


def frase_hueco(b, x, y, w, txt, c, h=54, size=18):
    caja(b, x, y, w, h, c)
    b.append(T(x + 22, y + h / 2 + 7, [txt], size, INK, weight="700"))
    return y + h


def letra(b, cx, cy, L, c, r=17, size=16):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="2"/>')
    b.append(T(cx, cy + size * 0.38, [L], size, c, weight="700", anchor="middle"))


def tinte(c, k=0.9):
    from taller_base import _mezcla
    return _mezcla(c, k)


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12, bend=0.0):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


# ───────── P1 · pedigrí ─────────
def persona(b, cx, cy, sexo, afectado, s=46):
    fill = GRIS_AF if afectado else "white"
    if sexo == "h":
        b.append(rect(cx - s / 2, cy - s / 2, s, s, fill, r=2, stroke=INK, sw=2.4))
    else:
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{s / 2}" fill="{fill}" stroke="{INK}" stroke-width="2.4"/>')


def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El árbol de la familia, persona por persona", c,
                      "Copia del pedigrí del libro. Debajo de cada persona escribe su genotipo posible (AA, Aa, aa…). "
                      "Después pasa las tres pruebas: cada «sí» descarta patrones de herencia.")
    x0, ww = x + 22, w - 44
    # pedigrí a la izquierda
    pw = 490
    caja(b, x0, yy, pw, 560, c, r=16)
    gx = x0 + 20
    for k, g in enumerate(("Gen. 1", "Gen. 2", "Gen. 3", "Gen. 4")):
        pista(b, gx, yy + 64 + k * 132, g, size=14)
    cx = x0 + 262
    ys = [yy + 58 + k * 132 for k in range(4)]
    # generación 1
    b.append(line(cx - 90, ys[0], cx + 90, ys[0], INK, 2.2))
    persona(b, cx - 90, ys[0], "h", False)
    persona(b, cx + 90, ys[0], "m", False)
    b.append(line(cx, ys[0], cx, ys[0] + 52, INK, 2.2))
    xs2 = (cx - 120, cx, cx + 120)
    b.append(line(xs2[0], ys[0] + 52, xs2[2], ys[0] + 52, INK, 2.2))
    for xx, (sx, af) in zip(xs2, (("m", False), ("m", True), ("h", True))):
        b.append(line(xx, ys[0] + 52, xx, ys[1] - 23, INK, 2.2))
        persona(b, xx, ys[1], sx, af)
    # generación 3
    x3a, x3b = cx - 70, cx + 120
    b.append(line(xs2[1], ys[1] + 23, xs2[1], ys[1] + 60, INK, 2.2))
    b.append(line(xs2[1], ys[1] + 60, x3a, ys[1] + 60, INK, 2.2))
    b.append(line(x3a, ys[1] + 60, x3a, ys[2] - 23, INK, 2.2))
    persona(b, x3a, ys[2], "h", True)
    b.append(line(x3b, ys[1] + 23, x3b, ys[2] - 23, INK, 2.2))
    persona(b, x3b, ys[2], "m", False)
    b.append(line(x3a, ys[2] + 23, x3a, ys[3] - 23, INK, 2.2))
    persona(b, x3a, ys[3], "m", False)
    # casillas de genotipo
    # al lado de cada persona, sin pisar las líneas del árbol (la madre de la gen. 1, a la derecha)
    for (px, py, lado) in ((cx - 90, ys[0], -1), (cx + 90, ys[0], 1), (xs2[0], ys[1], 1), (xs2[1], ys[1], 1),
                           (xs2[2], ys[1], 1), (x3a, ys[2], -1), (x3b, ys[2], 1), (x3a, ys[3], -1)):
        bx_ = px + 31 if lado > 0 else px - 31 - 54
        b.append(rect(bx_, py - 16, 54, 32, "white", r=6, stroke=c, sw=1.6))
    pista(b, x0 + 20, yy + 548, "gris = afectado · □ hombre · ○ mujer", size=14)
    # tres pruebas a la derecha
    rx = x0 + pw + 30
    rw = ww - pw - 30
    pruebas = ("¿Hay un afectado cuyos dos padres están sanos?",
               "¿Hay una mujer afectada cuyo padre está sano?",
               "¿Hay alguna generación sin ningún afectado?")
    for k, p in enumerate(pruebas):
        py = yy + k * 134
        caja(b, rx, py, rw, 120, c, r=14)
        rot(b, rx + 18, py + 28, f"PRUEBA {k + 1}", c, size=14)
        texto(b, rx + 110, py + 28, p, size=17, weight="700")
        pista(b, rx + 18, py + 66, "en el árbol:", size=15)
        sino(b, rx + 110, py + 50, c)
        pista(b, rx + 290, py + 66, "dónde lo vi:", size=15)
        renglon(b, rx + 386, py + 68, rx + rw - 18)
        pista(b, rx + 18, py + 104, "entonces descarto:", size=15)
        renglon(b, rx + 160, py + 106, rx + rw - 18)
    yy2 = yy + 3 * 134
    return ojo(b, rx, yy2, rw, "DOS REGLAS PARA LEER UN PEDIGRÍ",
               "Si es dominante, todo afectado tiene al menos un padre o una madre afectados. Si es ligada al X "
               "recesiva, toda mujer afectada tiene un padre afectado. La regla que no se cumple en el árbol tumba "
               "su patrón.")


# ───────── P2 · dos parcelas ─────────
def i2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dos parcelas, fila por fila", c,
                      "Mira la ilustración del libro y llena la tabla. La edición genética cambia una sola fila; las "
                      "demás cambian por culpa de esa. Encierra la fila donde empieza todo.")
    x0, ww = x + 22, w - 44
    c1 = 330
    cw_ = (ww - c1) / 2
    filas = ("¿Qué tiene distinto en su ADN?", "¿Qué necesita contra el gusano?",
             "¿Qué le pasa al río cercano?", "¿Qué riesgo advierte la ilustración?")
    caja(b, x0, yy, ww, 56, c, fill=tinte(c), r=10)
    rot(b, x0 + c1 + 20, yy + 35, "MAÍZ CONVENCIONAL", c)
    rot(b, x0 + c1 + cw_ + 20, yy + 35, "MAÍZ EDITADO CON CRISPR", c)
    ry = yy + 56
    rh = 84
    for k, f in enumerate(filas):
        caja(b, x0, ry, ww, rh, c, r=0)
        b.append(f'<circle cx="{x0 + 24}" cy="{ry + rh / 2}" r="12" fill="white" stroke="{c}" stroke-width="2"/>')
        texto(b, x0 + 50, ry + rh / 2 + 6, f, size=17, weight="700")
        for j in range(2):
            renglon(b, x0 + c1 + 20 + j * cw_, ry + rh - 22, x0 + c1 + (j + 1) * cw_ - 20)
        ry += rh
    b.append(line(x0 + c1, yy, x0 + c1, ry, c, 2))
    b.append(line(x0 + c1 + cw_, yy, x0 + c1 + cw_, ry, c, 2))
    yy = ry + 18
    yy = frase_hueco(b, x0, yy, ww, "El gen editado cambió ________________ y por eso cambió ________________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una opción dice que la resistencia «surge» por usar plaguicidas:",
                  "¿puede un químico rociado sobre la planta escribirle un gen nuevo? En tu tabla, ¿cuál de las dos "
                  "parcelas tiene la resistencia en el ADN y cuál la tiene que comprar en un tanque?", c)


# ───────── P3 · qué mide cada propuesta ─────────
def i3(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "¿Qué mide cada propuesta?", c,
                      "Antes de elegir, escribe qué quieres saber: la pregunta es sobre el impacto en la "
                      "biodiversidad. Luego anota qué mide de verdad cada acción y si eso es biodiversidad.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 136, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE QUIERO SABER", c)
    pista(b, x0 + 20, yy + 72, "biodiversidad, en palabras mías, es…")
    renglon(b, x0 + 270, yy + 74, x0 + ww - 20)
    pista(b, x0 + 20, yy + 118, "y se mide contando…")
    renglon(b, x0 + 170, yy + 120, x0 + ww - 20)
    yy += 156
    cols = (90, 520, 300, ww - 910)
    heads = ("", "LO QUE MIDE ESA ACCIÓN", "¿ES BIODIVERSIDAD?", "¿COMPARA LAS DOS PARCELAS?")
    caja(b, x0, yy, ww, 50, c, fill=tinte(c), r=10)
    cx = x0
    for k, hd in enumerate(heads):
        if hd:
            rot(b, cx + 18, yy + 32, hd, c, size=14)
        cx += cols[k]
    ry = yy + 50
    for L in "ABCD":
        caja(b, x0, ry, ww, 66, c, r=0)
        letra(b, x0 + 45, ry + 33, L, c)
        renglon(b, x0 + cols[0] + 18, ry + 46, x0 + cols[0] + cols[1] - 18)
        sino(b, x0 + cols[0] + cols[1] + 40, ry + 22, c)
        sino(b, x0 + cols[0] + cols[1] + cols[2] + 40, ry + 22, c)
        ry += 66
    cx = x0
    for k in range(3):
        cx += cols[k]
        b.append(line(cx, yy, cx, ry, c, 2))
    yy = ry + 18
    return ojo(b, x0, yy, ww, "UNA MEDIDA BUENA, PERO DE OTRA COSA",
               "Un dato puede ser útil para el agricultor y aun así no responder esta pregunta. Vuelve a tu primera "
               "caja: la acción que sirve es la que mide lo que tú escribiste ahí, y lo mide en las dos parcelas.")


# ───────── P4 · plaga nueva en dos campos ─────────
def i4(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Dos campos frente a una plaga que nadie esperaba", c,
                      "Llega un hongo nuevo. Mata a toda planta que tenga la variante «a» y no puede con la variante "
                      "«b». Tacha las plantas que mueren en cada campo y cuenta las que quedan.")
    x0, ww = x + 22, w - 44
    half = (ww - 40) / 2
    campos = (("CAMPO 1 · TODAS IGUALES (como el cultivo CRISPR)", ["a"] * 24),
              ("CAMPO 2 · CON VARIACIÓN (como una población silvestre)",
               list("abaabaaabbaaabaabaababaa")))
    for k, (tit, gen) in enumerate(campos):
        bx = x0 + k * (half + 40)
        caja(b, bx, yy, half, 360, c, r=16)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        for i, g in enumerate(gen):
            col, fila = i % 6, i // 6
            px = bx + 52 + col * ((half - 104) / 5)
            py = yy + 86 + fila * 62
            # plantita: tallo y dos hojas
            b.append(line(px, py + 18, px, py - 10, EDU_VERDE, 3))
            b.append(f'<ellipse cx="{px - 9}" cy="{py}" rx="9" ry="5" fill="{EDU_VERDE}" '
                     f'transform="rotate(-30 {px - 9} {py})"/>')
            b.append(f'<ellipse cx="{px + 9}" cy="{py + 6}" rx="9" ry="5" fill="{EDU_VERDE}" '
                     f'transform="rotate(30 {px + 9} {py + 6})"/>')
            texto(b, px + 20, py + 22, g, size=17, color=INK, weight="700")
        pista(b, bx + 18, yy + 340, "sobreviven: ______ de 24")
    yy += 380
    yy = frase_hueco(b, x0, yy, ww, "Si llega una plaga que nadie conocía, el campo más expuesto es el ___ , porque ______________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una amenaza puede sonar grave y no ser la que te preguntan:",
                  "la pregunta es por lo que le pasa a un cultivo con baja variabilidad genética. Antes de marcar, "
                  "pregúntale a cada opción: ¿lo que describe depende de que las plantas sean todas iguales?", c)


# ───────── P5 · radiación ─────────
def i5(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dos caminos de un ADN roto", c,
                      "La misma radiación golpea dos tipos de células. Sigue cada camino y escribe qué pasa en cada "
                      "parada. El texto habla de dos efectos: cáncer y mutaciones en los descendientes.")
    x0, ww = x + 22, w - 44
    # origen
    caja(b, x0, yy, 260, 200, c, r=16, fill=tinte(c, 0.93))
    rot(b, x0 + 20, yy + 32, "LA RADIACIÓN", c)
    pista(b, x0 + 20, yy + 58, "¿de qué tipo? ¿qué le hace")
    pista(b, x0 + 20, yy + 80, "a la molécula de ADN?")
    renglon(b, x0 + 20, yy + 124, x0 + 240)
    renglon(b, x0 + 20, yy + 168, x0 + 240)
    caminos = (("UNA CÉLULA DEL CUERPO", ("el ADN queda…", "la célula empieza a…", "en la persona aparece…")),
               ("UNA CÉLULA SEXUAL", ("el ADN queda…", "el óvulo o el espermatozoide…", "en los hijos aparece…")))
    sx = x0 + 300
    sw_ = (ww - 300 - 2 * 24) / 3
    for k, (tit, pasos) in enumerate(caminos):
        py = yy + k * 230
        rot(b, sx, py + 10, tit, c, size=14)
        for j, ps in enumerate(pasos):
            bx = sx + j * (sw_ + 24)
            caja(b, bx, py + 24, sw_, 176, c, r=14)
            b.append(f'<circle cx="{bx + 26}" cy="{py + 52}" r="13" fill="white" stroke="{c}" stroke-width="2"/>')
            texto(b, bx + 26, py + 58, str(j + 1), size=15, color=c, weight="700", anchor="middle")
            pista(b, bx + 50, py + 58, ps)
            for r_ in range(3):
                renglon(b, bx + 18, py + 104 + r_ * 36, bx + sw_ - 18)
            if j < 2:
                flecha(b, bx + sw_ + 2, py + 112, bx + sw_ + 22, py + 112, c, head=9)
        flecha(b, x0 + 262, yy + 100, sx - 6, py + 112, c, bend=0.1 - 0.2 * k)
    yy += 460
    return alto_profe(b, x0, yy, ww,
                      "Radiación ionizante: la que tiene energía suficiente para arrancarles electrones a los átomos "
                      "de una molécula. Pídele al profe que explique qué le puede pasar a una molécula tan larga como el "
                      "ADN, y en qué se diferencia de una quemadura por calor.")


# ───────── P6 · consanguinidad · Punnett ─────────
def punnett(b, x, y, c, padre, madre, s=70):
    texto(b, x + s * 1.5, y - 14, f"padre {padre}", size=15, color=GRAY, anchor="middle")
    b.append(T(x - 16, y + s * 1.5, [f"madre {madre}"], 15, GRAY, anchor="middle", rot=-90))
    for i in range(3):
        for j in range(3):
            fill = tinte(c, 0.9) if (i == 0 or j == 0) and not (i == 0 and j == 0) else "white"
            if i == 0 and j == 0:
                continue
            b.append(rect(x + j * s, y + i * s, s, s, fill, r=0, stroke=c, sw=2))


def i6(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos cuadros de Punnett: extraños y parientes", c,
                      "El alelo «a» causa la enfermedad cuando va doble (aa). En una pareja de extraños es raro que los "
                      "dos lo carguen; entre primos que comparten abuelos, es mucho más fácil. Llena los dos cuadros.")
    x0, ww = x + 22, w - 44
    for k, (tit, p, m) in enumerate((("PAREJA DE EXTRAÑOS", "AA", "Aa"), ("PAREJA DE PRIMOS", "Aa", "Aa"))):
        bx = x0 + k * (ww / 2)
        caja(b, bx, yy, ww / 2 - 16, 330, c, r=16)
        rot(b, bx + 20, yy + 30, tit, c)
        punnett(b, bx + 60, yy + 72, c, p, m)
        px = bx + 300
        pista(b, px, yy + 100, "hijos aa:")
        texto(b, px + 74, yy + 100, "____ de 4", size=17)
        pista(b, px, yy + 150, "probabilidad:")
        texto(b, px + 104, yy + 150, "____ %", size=17)
        pista(b, px, yy + 200, "¿se ve la enfermedad?")
        sino(b, px, yy + 218, c)
    yy += 348
    yy = ojo(b, x0, yy, ww, "DOS NÚMEROS QUE NO SON EL MISMO",
             "La frecuencia del alelo es cuántos «a» hay en toda la población. La frecuencia de la enfermedad es "
             "cuántas personas son aa. Cruzar parientes no fabrica alelos nuevos, pero sí cambia cómo se juntan.")
    yy += 14
    return ojo(b, x0, yy, ww, "La «nueva información» que cita la pregunta no está en el libro:",
               "no hay una comunidad ni una predicción antes de la pregunta 6. Respóndela con tus dos cuadros: ¿qué le "
               "pasa a la probabilidad de aa cuando la pareja comparte abuelos?")


# ───────── P7 · plásmidos en cuatro viñetas ─────────
def bacteria(b, cx, cy, c, plasmido, w=74, h=36):
    b.append(rect(cx - w / 2, cy - h / 2, w, h, "white", r=h / 2, stroke=c, sw=2.2))
    if plasmido:
        b.append(f'<circle cx="{cx + 14}" cy="{cy}" r="7" fill="none" stroke="{c}" stroke-width="2.2"/>')


def i7(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La resistencia en cuatro viñetas", c,
                      "Las bacterias con un anillito llevan el plásmido con el gen de resistencia. Completa lo que pasa "
                      "en las viñetas 3 y 4 (dibuja o tacha) y escribe debajo de cada una qué está pasando.")
    x0, ww = x + 22, w - 44
    vw = (ww - 3 * 20) / 4
    vh = 280
    vin = (("1 · ANTES", [1, 0, 0, 1, 0, 0, 0, 0, 0]),
           ("2 · LLEGA EL ANTIBIÓTICO", [1, 0, 0, 1, 0, 0, 0, 0, 0]),
           ("3 · LO QUE QUEDA", None),
           ("4 · UNOS DÍAS DESPUÉS", None))
    for k, (tit, pl) in enumerate(vin):
        bx = x0 + k * (vw + 20)
        caja(b, bx, yy, vw, vh, c, r=14)
        rot(b, bx + 14, yy + 26, tit, c, size=13)
        if pl:
            for i, p in enumerate(pl):
                bacteria(b, bx + 50 + (i % 3) * ((vw - 100) / 2), yy + 70 + (i // 3) * 54, c, p)
        if k == 1:
            for i in range(7):
                b.append(f'<circle cx="{bx + 20 + i * (vw - 40) / 6:.1f}" cy="{yy + vh - 18}" r="4" fill="{c}"/>')
            pista(b, bx + 14, yy + vh - 30, "antibiótico", size=13)
        renglon(b, bx + 12, yy + vh + 34, bx + vw - 12)
        renglon(b, bx + 12, yy + vh + 70, bx + vw - 12)
        if k < 3:
            flecha(b, bx + vw + 2, yy + vh / 2, bx + vw + 18, yy + vh / 2, c, head=8)
    yy += vh + 92
    yy = frase_hueco(b, x0, yy, ww, "Esto complica al médico porque el gen de resistencia no se queda en ______________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "¡Otra vez «recesivos que se vuelven dominantes»!",
                  "esa frase ya apareció en la pregunta 5. Dominante y recesivo describen cómo se expresa un alelo en "
                  "un organismo con dos copias; una bacteria no funciona así. Mira tus viñetas: ¿qué viajó de una "
                  "bacteria a otra?", c)


# ───────── P8 · causa, efecto y comparación ─────────
def i8(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Causa, efecto y con qué comparo", c,
                      "Una pregunta de investigación tiene dos variables: la que sospecho que causa y la que veo como "
                      "efecto. Escríbelas y diseña con qué grupos las compararías.")
    x0, ww = x + 22, w - 44
    bw = (ww - 160) / 2
    for k, (tit, ps) in enumerate((("LO QUE SOSPECHO QUE CAUSA", "en la crianza de los Pomsky…"),
                                   ("LO QUE VEO COMO EFECTO", "en la salud de los perros…"))):
        bx = x0 + k * (bw + 160)
        caja(b, bx, yy, bw, 130, c, r=16, sw=2.6)
        rot(b, bx + 20, yy + 32, tit, c)
        pista(b, bx + 20, yy + 60, ps)
        renglon(b, bx + 20, yy + 104, bx + bw - 20)
    flecha(b, x0 + bw + 20, yy + 65, x0 + bw + 140, yy + 65, c, sw=3.4, head=16)
    texto(b, x0 + bw + 80, yy + 50, "¿se relaciona?", size=15, color=GRAY, anchor="middle")
    yy += 154
    caja(b, x0, yy, ww, 210, c, r=16)
    rot(b, x0 + 20, yy + 32, "MI COMPARACIÓN", c)
    gw = (ww - 60) / 2
    for k, tit in enumerate(("GRUPO 1 · perros nacidos de…", "GRUPO 2 · perros nacidos de…")):
        bx = x0 + 20 + k * (gw + 20)
        caja(b, bx, yy + 50, gw, 140, c, r=12, dash="7,5")
        texto(b, bx + 16, yy + 80, tit, size=16, weight="700", color=c)
        pista(b, bx + 16, yy + 112, "y en cada grupo cuento…")
        renglon(b, bx + 16, yy + 160, bx + gw - 16)
    yy += 228
    return ojo(b, x0, yy, ww, "UNA PREGUNTA PUEDE SER INTERESANTE Y NO SERVIR",
               "El reportaje toca muchos temas y todos dan para preguntar. Pero tu investigación busca una relación: "
               "la pregunta que sirve es la que se puede responder comparando tus dos grupos.")


# ───────── P9 · mezclar razas o cruzar hermanos ─────────
def alelos(b, cx, cy, c):
    for j in range(2):
        b.append(f'<circle cx="{cx - 16 + j * 32}" cy="{cy}" r="14" fill="white" stroke="{c}" stroke-width="2"/>')


def i9(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Mezclar razas o cruzar hermanos: no es lo mismo", c,
                      "Una enfermedad recesiva aparece cuando un cachorro recibe el mismo alelo dañino «d» de los dos "
                      "padres. Llena los alelos de los padres en cada caso y marca qué tan probable es que el cachorro "
                      "salga dd.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    casos = (("CASO 1 · POMERANIA × HUSKY", "dos razas distintas, sin parentesco", "Pomerania", "Husky"),
             ("CASO 2 · POMSKY × POMSKY HERMANOS", "escasean los ejemplares y se cruzan parientes", "hermano",
              "hermana"))
    for k, (tit, sub, p1, p2) in enumerate(casos):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 360, c, r=16)
        rot(b, bx + 20, yy + 30, tit, c, size=14)
        pista(b, bx + 20, yy + 54, sub)
        for j, nom in enumerate((p1, p2)):
            px = bx + half / 2 - 120 + j * 240
            texto(b, px, yy + 100, nom, size=16, color=GRAY, anchor="middle")
            alelos(b, px, yy + 130, c)
        b.append(line(bx + half / 2 - 80, yy + 130, bx + half / 2 + 80, yy + 130, c, 2))
        flecha(b, bx + half / 2, yy + 134, bx + half / 2, yy + 190, c, head=11)
        texto(b, bx + half / 2, yy + 214, "cachorro", size=16, color=GRAY, anchor="middle")
        alelos(b, bx + half / 2, yy + 240, c)
        pista(b, bx + 20, yy + 296, "¿qué tan probable es dd?")
        sino(b, bx + 20, yy + 312, c, labels=("baja", "alta"), gap=110)
    yy += 380
    yy = frase_hueco(b, x0, yy, ww, "El dd es más probable en el caso ___ , porque los dos padres ______________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una opción dice que mezclar razas «activa» mutaciones:",
                  "vuelve a la pregunta 5: ¿qué produce una mutación? Cruzar dos perros reparte alelos que ya "
                  "existían en los padres; no fabrica alelos nuevos.", c)


# ───────── P10 · balanza y detector de absolutos ─────────
def i10(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La balanza y el detector de «siempre»", c,
                      "Pon en cada plato lo que el texto dice de las pruebas genéticas y de la edición génica. Después "
                      "pasa cada opción por el detector: encierra las palabras que prometen sin dejar dudas.")
    x0, ww = x + 22, w - 44
    cx = x0 + ww / 2
    by = yy + 40
    b.append(f'<polygon points="{cx - 34},{by + 300} {cx + 34},{by + 300} {cx},{by + 230}" fill="{tinte(c, 0.8)}" '
             f'stroke="{c}" stroke-width="2.4"/>')
    b.append(line(cx, by + 230, cx, by + 30, c, 4))
    b.append(line(cx - 380, by + 30, cx + 380, by + 30, c, 4))
    for k, (tit, ps) in enumerate((("LO QUE PUEDE MEJORAR", "según los criadores"),
                                   ("LO QUE PUEDE ARRIESGAR", "según otros especialistas"))):
        px = cx + (-1 if k == 0 else 1) * 380
        b.append(line(px, by + 30, px - 150, by + 92, c, 2))
        b.append(line(px, by + 30, px + 150, by + 92, c, 2))
        bx = px - 200
        caja(b, bx, by + 92, 400, 150, c, r=16)
        rot(b, bx + 20, by + 122, tit, c)
        pista(b, bx + 20, by + 146, ps)
        renglon(b, bx + 20, by + 188, bx + 380)
        renglon(b, bx + 20, by + 226, bx + 380)
    yy = by + 330
    caja(b, x0, yy, ww, 120, c, r=16, dash="8,6")
    rot(b, x0 + 20, yy + 32, "DETECTOR DE «SIEMPRE»", c)
    pista(b, x0 + 20, yy + 58, "palabras que encerré en cada opción (siempre, todo, nunca, ningún…)")
    for k, L in enumerate("ABCD"):
        bx = x0 + 20 + k * ((ww - 40) / 4)
        letra(b, bx + 18, yy + 90, L, c)
        renglon(b, bx + 46, yy + 102, bx + (ww - 40) / 4 - 20)
    yy += 136
    return ojo(b, x0, yy, ww, "EN CIENCIA, UNA TÉCNICA NUEVA TIENE PLATOS EN LOS DOS LADOS",
               "Valorar es pesar con lo que dice el texto, no con lo que uno quisiera. Antes de marcar, comprueba que "
               "cada afirmación de la opción que elijas se pueda sostener con lo que escribiste en tu balanza.")


Q = {1: dict(n=1, est=1, pag=116, ctx="Pedigrí de una enfermedad rara · qué patrón de herencia",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=2, pag=117, ctx="Maíz convencional y maíz CRISPR · del gen al efecto",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=3, pag=117, ctx="Maíz CRISPR · cómo obtener evidencia sobre biodiversidad",
             comp="Indagación", inst=i3),
     4: dict(n=4, est=4, pag=117, ctx="Maíz CRISPR · el riesgo de un cultivo sin variabilidad",
             comp="Explicación de fenómenos", inst=i4),
     5: dict(n=5, est=2, pag=117, ctx="Radiación de las bombas atómicas · cáncer y mutaciones",
             comp="Explicación de fenómenos", inst=i5),
     6: dict(n=6, est=1, pag=118, ctx="Consanguinidad · cómo cambia la predicción",
             comp="Uso comprensivo del conocimiento científico", inst=i6),
     7: dict(n=7, est=2, pag=118, ctx="Bacterias resistentes · genes que viajan en plásmidos",
             comp="Explicación de fenómenos", inst=i7),
     8: dict(n=8, est=3, pag=118, ctx="Perros Pomsky · la pregunta de investigación adecuada",
             comp="Indagación", inst=i8),
     9: dict(n=9, est=1, pag=119, ctx="Perros Pomsky · por qué más enfermedades hereditarias",
             comp="Explicación de fenómenos", inst=i9),
     10: dict(n=10, est=4, pag=119, ctx="Perros Pomsky · valorar la biotecnología",
              comp="Uso comprensivo del conocimiento científico", inst=i10)}


def build(pages=(168, 169, 171, 172, 173)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"bio5_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
