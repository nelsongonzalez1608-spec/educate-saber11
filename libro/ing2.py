#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 2 · componente conversacional · páginas 276–282.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 2» de Inglés (fuente_libro/INGLÉS), páginas 424–425.
Diez diálogos cortos con dibujo: alguien dice una frase y hay que escoger la respuesta natural
entre tres (A–C). Es la tarea de la Parte 3 del ICFES («Complete las conversaciones»).

Claves verificadas (resueltas a mano contra el libro, 7 nov 2026):

    1·C  2·A  3·A  4·B  5·A  6·C  7·A  8·B  9·C  10·B

  1 · C: «Could you print…?» es un PEDIDO, no una pregunta por la capacidad. Se contesta
      aceptando o negándose: «Yes, I'll do it right away». A habla de impresoras y B de la sala:
      repiten palabras del pedido sin decir si se va a imprimir.
  2 · A: quien llama quiere CONFIRMAR si sigues interesado: «Yes, I need more information about
      the plans». B (el internet es rápido) y C (uso internet de noche) no le dicen nada.
  3 · A: «Is this…?» pide sí o no; «line» es FILA. A contesta y agrega dónde está la taquilla.
      B y C hablan de conciertos y de la banda.
  4 · B: «Do you think we should…?» pide una OPINIÓN sobre una propuesta: B da posición (yes) y
      razón (explicar mejor los costos). A habla de horarios; C es una verdad general.
  5 · A: «Does this phone have enough memory…?» pide sí o no sobre ESTE teléfono: A da el dato
      (128 GB). B y C hablan de teléfonos y videos en general.
  6 · C: «Did you hear about…?» pregunta por algo que ya pasó (enterarse de una noticia):
      «Yes, she told me yesterday. It sounds great!». A y B no dicen si te enteraste.
  7 · A: el médico pregunta cómo te sientes HOY: «Much better, thank you. The medicine is
      working». B habla de la clínica y C de una costumbre.
  8 · B: «Did you watch… last night?» → contesta en pasado: «Yes, it was amazing!». A (no me gusta
      ver TV entre semana) y C (los programas son populares) no dicen si lo vio.
  9 · C: «What happened?» pide contar lo que pasó: «Oh, nothing special. We were just talking
      about school». A describe a Mark. B tiene sentido pero un error de concordancia: «Mark and I
      WAS» (debe ser «were»). El libro la usa a propósito como distractora; registrado.
 10 · B: la frase no es una pregunta: es un consejo que alguien cuenta. La reacción natural le da
      la razón: «That's true, it's really important to stay hydrated». A es cierta pero no le
      responde; C es posible en una charla, pero no reacciona al consejo del médico (Atención).

Reparto: A 4 · B 3 · C 3. Equilibrado. Pero en 7 de las 10 la correcta es la única que empieza
por «Yes» (en 7 y 9 la correcta empieza por otra cosa, y en 10 por «That's true»), y ninguna
distractora empieza por «Yes»: se puede acertar sin leer. Registrado en ing2_hallazgos.csv.

Estrategias:
    1 · ¿Qué clase de pregunta me hacen?     (3, 5      · ICFES Ex. 1 · 8 umbrella)   azul
    2 · ¿Qué me están pidiendo?              (1, 2, 4   · ICFES Ex. 1 · 7 grandma)    rojo
    3 · El tiempo del verbo manda            (6, 8, 9   · ICFES Ex. 2 · 9 rained)     morado
    4 · Reacciono a lo que me cuentan        (7, 10     · ICFES Ex. 2 · 7 sandwich)   oro

Hojas: 276 ing2_t1 (1-2) · 277 ing2_t2 (3-4) · 278 ing2_i1 · 279 ing2_t3 (5-6) ·
       280 ing2_t4 (7-8) · 281 ing2_t5 (9-10) · 282 ing2_i2.
"""
from taller_base import *

configurar("Inglés", 2, "conversacional",
           tema="Contestarle a la persona, no a la palabra",
           nota="LO QUE SUBRAYÉ DE LA CONVERSACIÓN")
MORADO = "#5B3E96"
EST = {1: ("¿Qué clase de pregunta me hacen?", EDU_AZUL),
       2: ("¿Qué me están pidiendo?", EDU_ROJO),
       3: ("El tiempo del verbo manda", MORADO),
       4: ("Reacciono a lo que me cuentan", EDU_ORO)}
usar_estrategias(EST)
AZ, RO, MO, OR = (EST[k][1] for k in (1, 2, 3, 4))


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def texto(b, x, y, txt, size=17, color=INK, weight="400", anchor="start", style="normal"):
    b.append(T(x, y, [txt], size, color, weight=weight, anchor=anchor, style=style))


def sino(b, x, y, c, labels=("sí", "no"), gap=80):
    for j, lab in enumerate(labels):
        b.append(checkbox(x + j * gap, y, s=10, c=c))
        b.append(T(x + 28 + j * gap, y + 17, [lab], 16, GRAY))


def tinte(c, k=0.9):
    from taller_base import _mezcla
    return _mezcla(c, k)


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12, bend=0.0):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def burbuja(b, x, y, w, txt, c, size=21, rotulo=None, cola="izq"):
    """Globo de diálogo con la frase del libro, tal cual, en inglés."""
    top = 34 if rotulo else 16
    lineas = wrap_px(txt, size, w - 50, "700")
    h = top + len(lineas) * (size + 9) + 14
    b.append(rect(x, y, w, h, tinte(c, 0.95), r=22, stroke=c, sw=2.2))
    tx = x + 40 if cola == "izq" else x + w - 40
    d = -1 if cola == "izq" else 1
    b.append(f'<path d="M {tx - 14 * d} {y + h - 1} L {tx + 6 * d} {y + h + 22} L {tx + 14 * d} {y + h - 1}" '
             f'fill="{tinte(c, 0.95)}" stroke="{c}" stroke-width="2.2" stroke-linejoin="round"/>')
    b.append(rect(tx - 16, y + h - 6, 32, 8, tinte(c, 0.95), r=0))
    if rotulo:
        rot(b, x + 24, y + 24, rotulo, c, size=13)
    for k, ln in enumerate(lineas):
        texto(b, x + 24, y + top + size + k * (size + 9) - 4, " ".join(ln), size=size, weight="700")
    return y + h + 38


def tabla_vacia(b, x, y, cols, heads, filas, c, rh=58, hh=48, size=17, sin_renglon=()):
    """Tabla con encabezado tinte y primera columna con rótulos; el resto, renglones."""
    ww = sum(cols)
    caja(b, x, y, ww, hh, c, fill=tinte(c), r=8)
    cx = x
    for k, hd in enumerate(heads):
        if hd:
            rot(b, cx + 14, y + hh / 2 + 6, hd, c, size=14)
        cx += cols[k]
    ry = y + hh
    for f in filas:
        caja(b, x, ry, ww, rh, c, r=0)
        texto(b, x + 14, ry + rh / 2 + 6, f, size=size, weight="700")
        cx = x + cols[0]
        for k in range(1, len(cols)):
            if k not in sin_renglon:
                renglon(b, cx + 14, ry + rh - 16, cx + cols[k] - 14)
            cx += cols[k]
        ry += rh
    cx = x
    for k in range(len(cols) - 1):
        cx += cols[k]
        b.append(line(cx, y, cx, ry, c, 1.6))
    return ry


# ───────── P1 · Could you print…? · un pedido ─────────
def i1(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Pedido disfrazado de pregunta", c,
                      "Muchas preguntas en inglés no preguntan: piden. Antes de mirar las opciones, decide qué quiere "
                      "de verdad quien habla y cómo se le contesta a eso.")
    x0, ww = x + 22, w - 44
    yy = burbuja(b, x0, yy, 760, "Could you print these documents before the meeting?", c)
    half = (ww - 30) / 2
    caja(b, x0, yy, half, 190, c, r=14)
    rot(b, x0 + 18, yy + 30, "LO QUE DICEN LAS PALABRAS", c)
    pista(b, x0 + 18, yy + 64, "palabra por palabra, en español:")
    renglon(b, x0 + 18, yy + 104, x0 + half - 18)
    renglon(b, x0 + 18, yy + 150, x0 + half - 18)
    bx = x0 + half + 30
    caja(b, bx, yy, half, 190, c, r=14)
    rot(b, bx + 18, yy + 30, "LO QUE DE VERDAD QUIERE", c)
    for k, t in enumerate(("me pide un favor", "me ofrece ayuda", "me pide mi opinión", "me cuenta una noticia")):
        cx_ = bx + 18 + (k % 2) * (half / 2)
        cy_ = yy + 58 + (k // 2) * 60
        b.append(checkbox(cx_, cy_, s=11, c=c))
        texto(b, cx_ + 32, cy_ + 18, t, size=17)
    yy += 210
    cols = (330, ww - 330)
    yy = tabla_vacia(b, x0, yy, cols, ("SI ME PIDEN ALGO, PUEDO…", "LO DIRÍA ASÍ EN INGLÉS"),
                     ("aceptar", "negarme con una razón", "preguntar algo antes"), c, rh=56, hh=42)
    yy += 20
    return trampa(b, x0, yy, ww, "Una respuesta puede repetir una palabra del pedido y no contestarlo:",
                  "pregúntale a cada opción: después de oírla, ¿sé si esta persona va a imprimir los documentos o no? "
                  "Si todavía no lo sé, esa opción no contestó.", c)


# ───────── P2 · la llamada ─────────
def i2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La llamada: quién llama y para qué", c,
                      "En una llamada, quien llama tiene un motivo. Si encuentras el motivo, sabes qué necesita oír. "
                      "Llena las cuatro casillas antes de mirar las opciones.")
    x0, ww = x + 22, w - 44
    yy = burbuja(b, x0, yy, ww - 200,
                 "Good afternoon, I'm calling to confirm if you are still interested in our Internet service.", c)
    cw = (ww - 30) / 2
    cas = (("¿QUIÉN LLAMA?", "una persona, una empresa, un amigo…"),
           ("¿PARA QUÉ? · confirm =", "lo que quiere saber de mí"),
           ("still =", "pista: «¿todavía me quieres?»"),
           ("¿QUÉ NECESITA OÍR?", "en una frase corta"))
    for k, (tit, ps) in enumerate(cas):
        bx = x0 + (k % 2) * (cw + 30)
        by = yy + (k // 2) * 120
        caja(b, bx, by, cw, 104, c, r=14)
        rot(b, bx + 18, by + 30, tit, c)
        pista(b, bx + 18, by + 56, ps)
        renglon(b, bx + 18, by + 88, bx + cw - 18)
    yy += 250
    caja(b, x0, yy, ww, 130, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "DOS RESPUESTAS QUE LE SIRVEN A QUIEN LLAMA · EN INGLÉS", c)
    pista(b, x0 + 20, yy + 70, "una que diga que sí:")
    renglon(b, x0 + 180, yy + 72, x0 + ww - 20)
    pista(b, x0 + 20, yy + 112, "una que diga que no:")
    renglon(b, x0 + 180, yy + 114, x0 + ww - 20)
    yy += 150
    return ojo(b, x0, yy, ww, "UNA FRASE VERDADERA NO SIEMPRE RESPONDE",
               "Algo puede ser cierto sobre el internet y no decirle nada a quien llama. Quien llama quiere saber "
               "una sola cosa de ti: si la opción no se la dice, no sirve, por bien escrita que esté.")


# ───────── P3 · Is this the line…? ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La pregunta empieza por el verbo", c,
                      "La primera palabra de una pregunta en inglés te dice qué clase de respuesta espera. Desarma "
                      "la pregunta 3 y completa la tabla de las palabras que abren preguntas.")
    x0, ww = x + 22, w - 44
    piezas = ("Is", "this", "the line", "for the concert tickets?")
    anchos = (150, 150, 220, ww - 520 - 3 * 20)
    bx = x0
    for k, (p, aw) in enumerate(zip(piezas, anchos)):
        caja(b, bx, yy, aw, 112, c, r=12)
        texto(b, bx + 16, yy + 38, p, size=22, weight="700")
        pista(b, bx + 16, yy + 66, "abre la pregunta:" if k == 0 else "significa:")
        renglon(b, bx + 16, yy + 96, bx + aw - 16)
        bx += aw + 20
    yy += 130
    cols = (380, 380, ww - 760)
    yy = tabla_vacia(b, x0, yy, cols, ("SI LA PREGUNTA EMPIEZA CON…", "ESPERO OÍR…", "UN EJEMPLO EN INGLÉS"),
                     ("Is / Are / Do / Does / Can…", "What / Where / How much…"), c, rh=60, hh=42)
    yy += 20
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "«LINE» TIENE DOS SIGNIFICADOS", c)
    pista(b, x0 + 20, yy + 66, "significado 1:")
    renglon(b, x0 + 130, yy + 68, x0 + ww / 2 - 20)
    pista(b, x0 + ww / 2, yy + 66, "significado 2:")
    renglon(b, x0 + ww / 2 + 110, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 112, "¿cuál tiene sentido frente a una taquilla de boletas? ¿por qué?")
    renglon(b, x0 + 470, yy + 114, x0 + ww - 20)
    yy += 168
    pista(b, x0, yy + 20, "La respuesta que sirve me deja saber si estoy en el lugar correcto. Antes de marcar, compruébalo con cada opción.")
    return yy + 30


# ───────── P4 · Do you think we should…? · opinión ─────────
def i4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Me piden una opinión: posición y razón", c,
                      "«Do you think we should…?» propone algo y te pregunta qué opinas. Una opinión completa tiene "
                      "dos piezas: lo que piensas y por qué. Revisa si cada opción trae las dos.")
    x0, ww = x + 22, w - 44
    yy = burbuja(b, x0, yy, 900, "Do you think we should add more details to the budget section?", c)
    pista(b, x0, yy + 16, "budget significa…  (pista: en un proyecto, es la plata que hay para gastar)")
    renglon(b, x0 + 560, yy + 18, x0 + ww)
    yy += 40
    half = (ww - 30) / 2
    for k, (tit, ps) in enumerate((("PIEZA 1 · MI POSICIÓN", "¿agrego más detalles o no?"),
                                   ("PIEZA 2 · MI RAZÓN", "¿para qué servirían esos detalles?"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 110, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c)
        pista(b, bx + 18, yy + 58, ps)
        renglon(b, bx + 18, yy + 92, bx + half - 18)
    yy += 128
    rot(b, x0, yy + 20, "LAS TRES OPCIONES DEL LIBRO, PIEZA POR PIEZA", c)
    yy += 34
    cols = (150, (ww - 150) / 3, (ww - 150) / 3, (ww - 150) / 3)
    heads = ("OPCIÓN", "¿HABLA DE LOS DETALLES?", "¿DA UNA POSICIÓN?", "¿DA UNA RAZÓN?")
    caja(b, x0, yy, ww, 42, c, fill=tinte(c), r=8)
    cx = x0
    for k, hd in enumerate(heads):
        rot(b, cx + 14, yy + 27, hd, c, size=14)
        cx += cols[k]
    ry = yy + 42
    for L in "ABC":
        caja(b, x0, ry, ww, 52, c, r=0)
        texto(b, x0 + 60, ry + 33, L, size=19, color=c, weight="700")
        cx = x0 + cols[0]
        for k in range(1, 4):
            sino(b, cx + 30, ry + 16, c)
            cx += cols[k]
        ry += 52
    cx = x0
    for k in range(3):
        cx += cols[k]
        b.append(line(cx, yy, cx, ry, c, 1.6))
    return ry


# ───────── P5 · enough memory ─────────
def i5(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Enough: ¿alcanza o no alcanza?", c,
                      "«Does…?» pide un sí o un no sobre un hecho. Aquí el hecho es si una cantidad alcanza. Dibuja "
                      "las dos barras y piensa qué tendría que decir la respuesta para que tú pudieras decidir.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 220, c, r=14)
    rot(b, x0 + 20, yy + 30, "LAS DOS BARRAS · COLORÉALAS COMO TE IMAGINES", c)
    for k, lab in enumerate(("lo que le cabe al teléfono", "lo que ocupan los videos")):
        by = yy + 56 + k * 66
        pista(b, x0 + 20, by + 28, lab)
        b.append(rect(x0 + 230, by, ww - 280, 40, "white", r=8, stroke=c, sw=2))
        for t in range(1, 10):
            xx = x0 + 230 + t * (ww - 280) / 10
            b.append(line(xx, by + 30, xx, by + 40, c, 1.4))
    pista(b, x0 + 20, yy + 202, "si la barra de arriba es más larga que la de abajo, la respuesta es:")
    sino(b, x0 + 520, yy + 186, c, labels=("yes", "no"))
    pista(b, x0 + 720, yy + 202, "enough significa:")
    renglon(b, x0 + 850, yy + 204, x0 + ww - 20)
    yy += 240
    caja(b, x0, yy, ww, 120, c, r=14)
    rot(b, x0 + 20, yy + 30, "SI YO FUERA A COMPRAR ESE TELÉFONO…", c)
    pista(b, x0 + 20, yy + 66, "¿qué dato tendría que darme el vendedor para que yo decida?")
    renglon(b, x0 + 20, yy + 104, x0 + ww - 20)
    yy += 138
    return ojo(b, x0, yy, ww, "HABLAR DEL TEMA NO ES CONTESTAR LA PREGUNTA",
               "Una respuesta puede hablar de teléfonos o de videos y no decir nada de ESTE teléfono. La pregunta "
               "dice «this phone»: la respuesta que sirve dice algo de ese teléfono en particular.")


# ───────── P6 · Did you hear about…? · línea de tiempo ─────────
def i6(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Did pregunta por algo que ya pasó", c,
                      "«Did you hear about…?» pregunta si ya te enteraste de una noticia. Ubica en la línea del "
                      "tiempo la noticia, la pregunta y el verbo principal de cada opción (escribe su letra).")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 230, c, r=14)
    ly = yy + 120
    b.append(line(x0 + 40, ly, x0 + ww - 40, ly, INK, 2.4))
    b.append(hand_arrow(x0 + ww - 80, ly, x0 + ww - 36, ly, INK, sw=2.4, bend=0, head=12))
    for k, lab in enumerate(("ANTES (ya pasó)", "AHORA", "DESPUÉS")):
        xx = x0 + 160 + k * (ww - 320) / 2
        b.append(line(xx, ly - 12, xx, ly + 12, INK, 2.4))
        rot(b, xx, ly + 42, lab, c, size=14, anchor="middle")
    pista(b, x0 + 20, yy + 34, "escribe encima de la línea, en su sitio: N (la noticia de Anna), P (la pregunta) y A, B, C "
                               "(el verbo principal de cada opción)")
    pista(b, x0 + 20, yy + 210, "si dos caen en el mismo sitio, escríbelas una encima de la otra")
    yy += 250
    cols = (300, ww - 300)
    yy = tabla_vacia(b, x0, yy, cols, ("LA PIEZA", "LO QUE ENTIENDO"),
                     ("hear about", "Anna's new job", "¿qué quiere saber?"), c, rh=56, hh=42)
    yy += 20
    return ojo(b, x0, yy, ww, "DID… ? PIDE ALGO QUE YA PASÓ",
               "La respuesta natural dice si te enteraste o no, y puede agregar un detalle de cuándo o cómo. Si el "
               "verbo principal de una opción no tiene nada que ver con enterarse de la noticia, sospecha.")


# ───────── P7 · How are you feeling today? · termómetro ─────────
def i7(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El termómetro de cómo estoy", c,
                      "Mira el dibujo de la página 425: quién pregunta y a quién. «How are you feeling today?» pide que "
                      "hables de ti, hoy. Escribe en inglés cómo dirías cada grado del termómetro.")
    x0, ww = x + 22, w - 44
    tx, ty, th = x0 + 40, yy + 10, 360
    b.append(rect(tx, ty, 44, th, "white", r=22, stroke=c, sw=2.4))
    b.append(f'<circle cx="{tx + 22}" cy="{ty + th + 26}" r="34" fill="white" stroke="{c}" stroke-width="2.4"/>')
    niveles = ("muy bien", "mejor que antes", "más o menos", "no muy bien", "fatal")
    for k, nv in enumerate(niveles):
        yv = ty + 36 + k * 72
        b.append(line(tx + 44, yv, tx + 70, yv, c, 2))
        texto(b, tx + 86, yv + 6, nv, size=17, weight="700")
        pista(b, tx + 260, yv + 5, "en inglés:")
        renglon(b, tx + 340, yv + 8, x0 + 760)
    rx, rw = x0 + 800, ww - 800
    caja(b, rx, yy + 10, rw, 400, c, r=14)
    rot(b, rx + 18, yy + 40, "EL DIBUJO DE LA 7", c)
    for k, ps in enumerate(("¿quién pregunta?", "¿a quién le pregunta?", "¿dónde están?",
                            "entonces la respuesta tiene que hablar de…")):
        py = yy + 84 + k * 82
        pista(b, rx + 18, py, ps)
        renglon(b, rx + 18, py + 40, rx + rw - 18)
    yy += 440
    return ojo(b, x0, yy, ww, "TODAY MANDA",
               "La pregunta es por hoy y por la persona que contesta. Una opción que no te deja saber cómo está esa "
               "persona hoy no contestó, aunque use palabras que aparecen en el dibujo.")


# ───────── P8 · Did you watch…last night? ─────────
def i8(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Last night: la marca del tiempo", c,
                      "Las palabras de tiempo dicen en qué tiempo tiene que ir el verbo de la respuesta. Clasifica "
                      "estas marcas y después mira con cuál habla la pregunta 8.")
    x0, ww = x + 22, w - 44
    cols = (300, 330, ww - 630)
    yy = tabla_vacia(b, x0, yy, cols, ("LA MARCA DE TIEMPO", "¿PASADO, HÁBITO O FUTURO?", "UNA FRASE MÍA CON ELLA"),
                     ("last night", "yesterday", "usually", "every weekend", "tomorrow"), c, rh=54, hh=42)
    yy += 20
    caja(b, x0, yy, ww, 120, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PREGUNTA 8 EN ESPAÑOL", c)
    pista(b, x0 + 20, yy + 66, "Did you watch the new episode last night? =")
    renglon(b, x0 + 340, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 104, "¿se contesta con sí o no?")
    sino(b, x0 + 220, yy + 88, c)
    yy += 138
    half = (ww - 30) / 2
    for k, (tit, ps) in enumerate((("ALGUIEN QUE SÍ LO VIO DIRÍA…", "en inglés, en pasado"),
                                   ("ALGUIEN QUE NO LO VIO DIRÍA…", "en inglés, en pasado"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 110, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c)
        pista(b, bx + 18, yy + 56, ps)
        renglon(b, bx + 18, yy + 92, bx + half - 18)
    return yy + 110


# ───────── P9 · What happened? · was / were ─────────
def i9(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Was o were: quién estaba haciendo qué", c,
                      "Para contar lo que estabas haciendo ayer se usa was o were + el verbo con -ing. Completa la "
                      "tabla y úsala para revisar la gramática de cada opción, no solo su sentido.")
    x0, ww = x + 22, w - 44
    cols = (360, 200, ww - 560)
    yy = tabla_vacia(b, x0, yy, cols, ("QUIÉN", "¿WAS O WERE?", "COMPLETA: … just talking"),
                     ("I", "you", "he · she · Mark", "we · you and I", "they"), c, rh=52, hh=42)
    yy += 20
    half = (ww - 30) / 2
    for k, (tit, frag, ps) in enumerate((("LO QUE CUENTA", "I saw you talking to Mark yesterday.", "¿qué vio esta persona?"),
                                         ("LO QUE PREGUNTA", "What happened?", "¿se contesta con sí o no? ¿qué espera oír?"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 140, c, r=14)
        rot(b, bx + 18, yy + 28, tit, c, size=13)
        texto(b, bx + 18, yy + 62, frag, size=19, weight="700")
        pista(b, bx + 18, yy + 90, ps)
        renglon(b, bx + 18, yy + 124, bx + half - 18)
    yy += 160
    return ojo(b, x0, yy, ww, "REVISA LA GRAMÁTICA DE CADA OPCIÓN",
               "En el examen una opción puede tener sentido y estar mal escrita. El sujeto y el verbo tienen que "
               "concordar: compara el sujeto de cada opción con tu tabla antes de marcar.")


# ───────── P10 · un consejo del médico ─────────
def i10(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Me cuentan un consejo: ¿qué contesto?", c,
                      "La frase 10 no es una pregunta: alguien te cuenta lo que le dijo su médico. A eso no se contesta "
                      "con sí o no; se reacciona. Decide primero cómo reaccionarías tú.")
    x0, ww = x + 22, w - 44
    yy = burbuja(b, x0, yy, 760, "The doctor said I should drink more water.", c)
    pista(b, x0, yy + 16, "«said I should» quiere decir:")
    renglon(b, x0 + 210, yy + 18, x0 + 620)
    pista(b, x0 + 650, yy + 16, "¿termina en signo de pregunta?")
    sino(b, x0 + 880, yy, c)
    yy += 40
    cols = (360, ww - 360)
    yy = tabla_vacia(b, x0, yy, cols, ("PUEDO REACCIONAR…", "LO DIRÍA ASÍ EN INGLÉS"),
                     ("dándole la razón", "animándolo", "preguntándole algo", "llevándole la contraria"),
                     c, rh=56, hh=42)
    yy += 20
    return trampa(b, x0, yy, ww, "Algo puede ser cierto en el mundo y no responderle a esta persona:",
                  "¿la opción muestra que escuchaste lo que le dijo su médico? Si la podrías decir sin haber oído la "
                  "frase, no es una reacción a ella.", c)


Q = {1: dict(n=1, est=2, pag=424, ctx="Could you print these documents…?", inst=i1, comp="Pragmático",
             letras="ABC"),
     2: dict(n=2, est=2, pag=424, ctx="Una llamada · Internet service", inst=i2, comp="Pragmático",
             letras="ABC"),
     3: dict(n=3, est=1, pag=424, ctx="Is this the line for the concert tickets?", inst=i3, comp="Pragmático",
             letras="ABC"),
     4: dict(n=4, est=2, pag=424, ctx="Do you think we should add more details…?", inst=i4, comp="Pragmático",
             letras="ABC"),
     5: dict(n=5, est=1, pag=424, ctx="Does this phone have enough memory…?", inst=i5, comp="Pragmático",
             letras="ABC"),
     6: dict(n=6, est=3, pag=424, ctx="Did you hear about Anna's new job?", inst=i6, comp="Pragmático",
             letras="ABC"),
     7: dict(n=7, est=4, pag=425, ctx="How are you feeling today?", inst=i7, comp="Pragmático",
             letras="ABC"),
     8: dict(n=8, est=3, pag=425, ctx="Did you watch the new episode last night?", inst=i8, comp="Pragmático",
             letras="ABC"),
     9: dict(n=9, est=3, pag=425, ctx="I saw you talking to Mark… What happened?", inst=i9, comp="Pragmático",
             letras="ABC"),
     10: dict(n=10, est=4, pag=425, ctx="The doctor said I should drink more water.", inst=i10, comp="Pragmático",
              letras="ABC")}


def build(pages=(276, 277, 279, 280, 281)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"ing2_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
