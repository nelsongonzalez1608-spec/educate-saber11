#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 1 · componente léxico · lectura · páginas 269–275.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 1» de Inglés (fuente_libro/INGLÉS), páginas 414–415.
La misión del libro trae 21 ítems, no 10: Parte 1 (léxico: 14 descripciones que se emparejan
con un banco de palabras A–H, en dos grupos de 7: «People and What They do», 1–7, y «School
Life», 8–14) y Parte 2 (pragmático: 7 avisos, «¿dónde lo verías?», 3 opciones, 15–21). El
cuaderno trabaja 10 con su instrumento (las de más trampa o con la pista más enseñable) y la
tarjeta conserva el número del libro; las otras 11 se resuelven en el libro con las mismas
estrategias. Registrado en tablero/propuestas/ing1_hallazgos.csv (decisión para Nelson).

Claves verificadas (resueltas a mano contra el libro, 7 nov 2026). Las 21, para el profe:

    Parte 1 · 1·C  2·A  3·B  4·H  5·D  6·E  7·F  (sobra G Baker)
              8·B  9·A  10·C  11·D  12·E  13·F  14·G  (sobra H Bookshop)
    Parte 2 · 15·A  16·B  17·A  18·C  19·A  20·B  21·C

Las 10 del cuaderno:  1·C  5·D  7·F  11·D  13·F  16·B  18·C  19·A  20·B  21·C

  1 · C Technician: «a person who REPAIRS electrical machines in offices or houses». A (Factory)
      es un lugar; ninguna otra persona del banco repara máquinas.
  5 · D Volunteer: «works helping people WITHOUT being paid». A la enfermera, al artista, al
      conductor y al panadero les pagan; «without» deja solo al voluntario.
  7 · F Passenger: «travels in a bus, car, or plane BUT does NOT drive». Driver (H) viaja y
      maneja: «but does not drive» lo saca. Si se tachan las ya usadas (1–6), quedan F, G, H.
 11 · D Library: «a place where you can BORROW academic books». Bookshop (H) también tiene libros,
      pero ahí se compran (buy), no se piden prestados. «academic» no separa las dos.
 13 · F Seminar: «a group of students who DISCUSS a topic with a teacher». Lecture hall (B, la 8)
      es donde se escucha y se toman notas: uno habla, los demás escuchan.
 16 · B Delivery App: «Your package is ready. Pay ONLINE to SCHEDULE DELIVERY». Quien guarda
      el paquete y deja pagar por internet para programar la entrega es el servicio de envíos.
 18 · C Hospital reception: «Bring your ID. Payment is required before the MEDICAL APPOINTMENT».
      Documento y pago se piden en muchos lugares; «medical appointment» solo encaja en C.
 19 · A Airplane cabin: «Fasten your seat belt. TURBULENCE expected». Cinturón hay en carro, bus,
      avión; turbulencia solo en el avión. Las dos pistas a la vez: A.
 20 · B Streaming service email: «Your SUBSCRIPTION will be canceled if payment fails before July
      10». Quien cancela una suscripción es quien la vende. El banco (A) habla de pagos pero no
      «cancela tu suscripción»; el boletín escolar (C) no cobra.
 21 · C Airport security area: «Immigration control: keep PASSPORT and BOARDING PASS ready».
      Pasaporte + pase de abordar + control de inmigración: aeropuerto. Con reserva (hallazgo):
      inmigración y el filtro de seguridad son puntos distintos del aeropuerto; C es la mejor de
      las tres, no una descripción exacta.

Reparto de las 21: Parte 1 casi en orden alfabético (grupo 2: B A C D E F G, grupo 1: C A B H D E F):
quien marque «en orden» acierta casi todo. Parte 2: A 3 · B 2 · C 2. De las 10 del cuaderno:
A 1 · B 2 · C 3 · D 2 · F 2. Registrado en ing1_hallazgos.csv.

Estrategias:
    1 · El verbo delata la palabra        (1, 11, 13   · ICFES 2016-1 2.ª sesión · 87 watch)   azul
    2 · Cada pista tacha opciones         (5, 7        · ICFES Ex. 2 · 2 bus)        rojo
    3 · ¿Dónde estaría este aviso?        (19, 21      · ICFES Ex. 2 · 6 bookshelf)  morado
    4 · Quién me escribe y qué quiere     (16, 18, 20  · ICFES Ex. 2 · 5 shop)       oro

Hojas: 269 ing1_t1 (1-5) · 270 ing1_t2 (7-11) · 271 ing1_i1 · 272 ing1_t3 (13-16) ·
       273 ing1_t4 (18-19) · 274 ing1_t5 (20-21) · 275 ing1_i2.
"""
from taller_base import *

configurar("Inglés", 1, "léxico · lectura",
           tema="Las pistas que trae cada palabra",
           nota="LAS PALABRAS QUE SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("El verbo delata la palabra", EDU_AZUL),
       2: ("Cada pista tacha opciones", EDU_ROJO),
       3: ("¿Dónde estaría este aviso?", MORADO),
       4: ("Quién me escribe y qué quiere", EDU_ORO)}
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


def cita(b, x, y, w, txt, c, size=21, rotulo=None):
    """El fragmento en inglés tal como está en el libro: fondo tinte y acento vertical."""
    top = 34 if rotulo else 14
    lineas = wrap_px(txt, size, w - 56, "700")
    h = top + len(lineas) * (size + 9) + 14
    caja(b, x, y, w, h, tinte(c, 0.92), fill=tinte(c, 0.95), r=12)
    b.append(rect(x, y, 8, h, c, r=4))
    if rotulo:
        rot(b, x + 28, y + 24, rotulo, c, size=13)
    for k, ln in enumerate(lineas):
        texto(b, x + 28, y + top + size + k * (size + 9) - 4, " ".join(ln), size=size, weight="700")
    return y + h


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


# ───────── P1 · Technician · el verbo repairs ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Desarmo la descripción en cuatro piezas", c,
                      "Una descripción en inglés es una cadena de piezas. Debajo de cada pieza escribe lo que "
                      "entiendes, aunque sea a medias. La pieza que más dice casi siempre es el verbo: lo que esa "
                      "persona hace.")
    x0, ww = x + 22, w - 44
    piezas = (("¿PERSONA O LUGAR?", "a person who"), ("¿QUÉ HACE? · EL VERBO", "repairs"),
              ("¿QUÉ COSA?", "electrical machines"), ("¿DÓNDE?", "in offices or houses"))
    pw = (ww - 3 * 24) / 4
    for k, (tit, frag) in enumerate(piezas):
        bx = x0 + k * (pw + 24)
        caja(b, bx, yy, pw, 178, c, r=14)
        rot(b, bx + 16, yy + 28, tit, c, size=13)
        texto(b, bx + 16, yy + 70, frag, size=21, weight="700")
        pista(b, bx + 16, yy + 112, "lo que entiendo:")
        renglon(b, bx + 16, yy + 156, bx + pw - 16)
        if k < 3:
            flecha(b, bx + pw + 2, yy + 64, bx + pw + 22, yy + 64, c, head=8)
    yy += 200
    caja(b, x0, yy, ww, 196, c, r=14)
    rot(b, x0 + 20, yy + 30, "DEL VERBO A LA PERSONA", c)
    pista(b, x0 + 20, yy + 70, "En español, alguien que hace eso es un…")
    renglon(b, x0 + 330, yy + 72, x0 + ww / 2 + 40)
    pista(b, x0 + 20, yy + 116, "Las palabras de la columna que son LUGARES, no personas (no sirven):")
    renglon(b, x0 + 540, yy + 118, x0 + ww - 20)
    pista(b, x0 + 20, yy + 162, "La persona de la columna cuyo trabajo es ese verbo:")
    renglon(b, x0 + 400, yy + 164, x0 + ww / 2 + 120)
    pista(b, x0 + ww / 2 + 150, yy + 162, "¿la puse en otra pregunta?")
    sino(b, x0 + ww / 2 + 350, yy + 146, c)
    yy += 216
    return ojo(b, x0, yy, ww, "PALABRAS QUE SE PARECEN AL ESPAÑOL",
               "«Electrical» se parece a «eléctrico» y significa lo mismo: es un cognado. Los cognados ayudan "
               "muchísimo, pero hay falsos amigos: «actually» no es «actualmente», es «en realidad». Confirma "
               "siempre con el resto de la frase.")


# ───────── P5 · Volunteer · without ─────────
def i5(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La palabra que le da la vuelta a la frase", c,
                      "Hay palabras pequeñas que cambian todo el sentido. Encierra en la frase la que le da la "
                      "vuelta, y escribe cómo cambiaría la descripción si no estuviera.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "5.  This is a person who works helping people without being paid.", c,
              rotulo="LA DESCRIPCIÓN DEL LIBRO · ENCIERRA LA PALABRA QUE DA LA VUELTA")
    yy += 18
    half = (ww - 60) / 2
    for k, (tit, ps) in enumerate((("SI QUITO ESA PALABRA…", "la frase diría que es alguien que…"),
                                   ("CON ESA PALABRA…", "la frase dice que es alguien que…"))):
        bx = x0 + k * (half + 60)
        caja(b, bx, yy, half, 130, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c)
        pista(b, bx + 18, yy + 62, ps)
        renglon(b, bx + 18, yy + 108, bx + half - 18)
    flecha(b, x0 + half + 8, yy + 65, x0 + half + 52, yy + 65, c, head=9)
    yy += 150
    cols = (230, 330, ww - 560)
    yy = tabla_vacia(b, x0, yy, cols, ("LA PALABRA", "LO QUE SIGNIFICA", "UNA FRASE MÍA CON ELLA"),
                     ("without", "not / does not", "but"), c, rh=56, hh=42)
    yy += 20
    caja(b, x0, yy, ww, 120, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "LO QUE TACHO", c)
    pista(b, x0 + 20, yy + 66, "personas de la columna a las que SÍ les pagan por su trabajo:")
    for k in range(4):
        b.append(rect(x0 + 470 + k * 186, yy + 44, 170, 34, "white", r=8, stroke=c, sw=1.8))
    pista(b, x0 + 20, yy + 104, "y la persona que queda en pie:")
    renglon(b, x0 + 240, yy + 106, x0 + 640)
    return yy + 120


# ───────── P7 · Passenger · el banco se vacía ─────────
def i7(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El banco que se va vaciando", c,
                      "En la Parte 1 cada palabra sirve una sola vez y una sobra. Antes de resolver la 7, tacha "
                      "aquí las palabras que ya usaste en las preguntas 1 a 6 y anota en cuál. Lo que queda en pie "
                      "es tu banco nuevo.")
    x0, ww = x + 22, w - 44
    banco = ("Factory", "Nurse", "Technician", "Volunteer", "Artist", "Passenger", "Baker", "Driver")
    tw_ = (ww - 3 * 16) / 4
    for k, pal in enumerate(banco):
        bx = x0 + (k % 4) * (tw_ + 16)
        by = yy + (k // 4) * 100
        caja(b, bx, by, tw_, 86, c, r=12)
        b.append(f'<circle cx="{bx + 30}" cy="{by + 30}" r="16" fill="white" stroke="{c}" stroke-width="2"/>')
        texto(b, bx + 30, by + 36, "ABCDEFGH"[k], size=16, color=c, weight="700", anchor="middle")
        texto(b, bx + 58, by + 37, pal, size=20, weight="700")
        pista(b, bx + 16, by + 72, "la usé en la pregunta:")
        b.append(rect(bx + 172, by + 52, 56, 26, "white", r=6, stroke=GRAY, sw=1.4))
    yy += 216
    half = (ww - 40) / 2
    pistas = (("PISTA 1", "travels in a bus, car, or plane", "del banco que queda, ¿quiénes viajan así?"),
              ("PISTA 2", "but does not drive", "¿a quién saca esta pista? ¿quién queda?"))
    for k, (tit, frag, ps) in enumerate(pistas):
        bx = x0 + k * (half + 40)
        caja(b, bx, yy, half, 156, c, r=14)
        rot(b, bx + 18, yy + 28, tit, c, size=13)
        texto(b, bx + 18, yy + 64, frag, size=20, weight="700")
        pista(b, bx + 18, yy + 96, ps)
        renglon(b, bx + 18, yy + 138, bx + half - 18)
    flecha(b, x0 + half + 4, yy + 78, x0 + half + 36, yy + 78, c, head=9)
    yy += 176
    yy = trampa(b, x0, yy, ww, "Dos palabras del banco pueden ir en el mismo carro:",
                "una de las dos maneja y la otra no. El «but» de la descripción te dice cuál buscas. Al terminar "
                "el grupo, escribe en tu margen qué palabra sobró y por qué no encaja con ninguna descripción.", c)
    return yy


# ───────── P11 · Library · borrow ─────────
def i11(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Borrow, read, return: lo que le pasa al libro", c,
                      "Dos lugares de la columna tienen libros. Lo que los separa es un solo verbo de la descripción. "
                      "Sigue el camino del libro y usa como pista el aviso 15 de la página 415.")
    x0, ww = x + 22, w - 44
    pasos = ("borrow", "read", "return")
    pw = (ww - 2 * 60) / 3
    for k, v in enumerate(pasos):
        bx = x0 + k * (pw + 60)
        caja(b, bx, yy, pw, 120, c, r=14)
        b.append(f'<circle cx="{bx + 30}" cy="{yy + 32}" r="15" fill="white" stroke="{c}" stroke-width="2"/>')
        texto(b, bx + 30, yy + 38, str(k + 1), size=15, color=c, weight="700", anchor="middle")
        texto(b, bx + 58, yy + 40, v, size=23, weight="700")
        pista(b, bx + 18, yy + 76, "en español:")
        renglon(b, bx + 104, yy + 78, bx + pw - 18)
        if k < 2:
            flecha(b, bx + pw + 6, yy + 60, bx + pw + 54, yy + 60, c, head=10)
    yy += 140
    yy = cita(b, x0, yy, ww, "Please return books on time. Others are waiting for them.", c, size=20,
              rotulo="EL AVISO 15 DE LA PÁGINA 415")
    pista(b, x0, yy + 30, "¿Por qué habría otras personas esperando el mismo libro? Entonces, ¿el libro era mío?")
    renglon(b, x0 + 640, yy + 32, x0 + ww)
    yy += 54
    half = (ww - 30) / 2
    for k, (tit, v2) in enumerate((("UN LUGAR DONDE BORROW…", "…y después return"),
                                   ("UN LUGAR DONDE BUY…", "…y antes pay"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 128, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c)
        pista(b, bx + 250, yy + 30, v2)
        pista(b, bx + 18, yy + 70, "¿el libro vuelve al lugar?")
        sino(b, bx + 210, yy + 54, c)
        pista(b, bx + 18, yy + 110, "palabra de la columna:")
        renglon(b, bx + 180, yy + 112, bx + half - 18)
    yy += 146
    return ojo(b, x0, yy, ww, "UNA PISTA QUE COMPARTEN DOS OPCIONES NO DECIDE",
               "En los dos lugares puede haber libros académicos: la palabra «academic» no separa nada. Cuando "
               "dos opciones cumplen la misma pista, busca la pista que solo cumple una.")


# ───────── P13 · Seminar · discuss ─────────
def _salon(b, x, y, w, h, c, ronda):
    caja(b, x, y, w, h, c, r=14)
    cx, cy = x + w / 2, y + h / 2 + 10
    if ronda:
        import math as _m
        for k in range(8):
            a = 2 * _m.pi * k / 8 - _m.pi / 2
            px, py = cx + 120 * _m.cos(a), cy + 78 * _m.sin(a)
            prof = k == 0
            b.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{20 if prof else 16}" fill="white" '
                     f'stroke="{c}" stroke-width="2"/>')
            if prof:
                texto(b, px, py + 6, "T", size=16, color=c, weight="700", anchor="middle")
    else:
        b.append(f'<circle cx="{cx}" cy="{y + 50}" r="20" fill="white" stroke="{c}" stroke-width="2"/>')
        texto(b, cx, y + 56, "T", size=16, color=c, weight="700", anchor="middle")
        for f in range(3):
            for k in range(5):
                px = cx - 140 + k * 70
                py = y + 110 + f * 46
                b.append(f'<circle cx="{px}" cy="{py}" r="15" fill="white" stroke="{c}" stroke-width="2"/>')


def i13(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "¿Quién le habla a quién en el salón?", c,
                      "Las preguntas 8 y 13 describen dos maneras de tener clase. La diferencia está en quién habla. "
                      "Dibuja con flechas quién le habla a quién en cada salón (T es el profesor) y decide cuál "
                      "descripción va con cada dibujo.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, ronda in enumerate((False, True)):
        bx = x0 + k * (half + 30)
        _salon(b, bx, yy, half, 260, c, ronda)
        rot(b, bx + 18, yy + 28, f"SALÓN {k + 1}", c)
    yy += 276
    for k in range(2):
        bx = x0 + k * (half + 30)
        pista(b, bx, yy + 20, "va con la pregunta:")
        b.append(rect(bx + 150, yy, 60, 30, "white", r=6, stroke=c, sw=1.8))
        pista(b, bx + 230, yy + 20, "palabra de la columna:")
        renglon(b, bx + 400, yy + 22, bx + half)
    yy += 44
    cols = (260, 420, ww - 680)
    yy = tabla_vacia(b, x0, yy, cols, ("EL VERBO", "LO QUE SIGNIFICA", "¿HABLA UNO O HABLAN TODOS?"),
                     ("listen", "take notes", "discuss"), c, rh=54, hh=42)
    yy += 18
    return ojo(b, x0, yy, ww, "OJO CON LA PRIMERA PALABRA DE LA 13",
               "La descripción empieza con «a group of students», como si la respuesta fuera un grupo de personas. "
               "No te quedes en esa palabra: manda el verbo. Busca en la columna dónde o en qué tipo de clase pasa "
               "lo que ese verbo describe.")


# ───────── P16 · Delivery App · package ─────────
def i16(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Lo que el mensaje me cuenta y lo que me pide", c,
                      "Un aviso corto casi siempre le pide algo a quien lo lee. Separa lo que te cuenta de lo que te "
                      "pide, y después piensa quién podría mandarte ese mensaje.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "Your package is ready.  Pay online to schedule delivery.", c, size=22,
              rotulo="EL AVISO 16")
    yy += 16
    palabras = ("package", "online", "schedule", "delivery")
    pw = (ww - 3 * 16) / 4
    for k, p in enumerate(palabras):
        bx = x0 + k * (pw + 16)
        caja(b, bx, yy, pw, 110, c, r=12)
        texto(b, bx + 16, yy + 36, p, size=21, weight="700")
        pista(b, bx + 16, yy + 66, "creo que significa:")
        renglon(b, bx + 16, yy + 96, bx + pw - 16)
    pista(b, x0, yy + 136, "pista para «schedule»: es lo que tienes pegado en el cuaderno con las horas de cada clase")
    yy += 156
    half = (ww - 30) / 2
    for k, (tit, ps) in enumerate((("ME CUENTA…", "¿qué ya pasó con mi paquete?"),
                                   ("ME PIDE QUE…", "¿qué tengo que hacer yo, y por dónde?"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 112, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c)
        pista(b, bx + 160, yy + 30, ps)
        renglon(b, bx + 18, yy + 92, bx + half - 18)
    yy += 130
    caja(b, x0, yy, ww, 118, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "MI FILTRO PARA CADA OPCIÓN", c)
    pista(b, x0 + 20, yy + 66, "¿ese lugar me guarda un paquete para entregármelo?")
    pista(b, x0 + 20, yy + 100, "¿ahí puedo pagar por internet y escoger el día de la entrega?")
    for k, L in enumerate("ABC"):
        bx = x0 + 640 + k * 190
        texto(b, bx, yy + 66, L, size=17, color=c, weight="700")
        b.append(checkbox(bx + 26, yy + 50, s=10, c=c))
        texto(b, bx, yy + 100, L, size=17, color=c, weight="700")
        b.append(checkbox(bx + 26, yy + 84, s=10, c=c))
    return yy + 118


# ───────── P18 · Hospital reception · appointment ─────────
def i18(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La lista antes de salir para la cita", c,
                      "El aviso 18 da dos órdenes y una pista de tiempo. Conviértelo en la lista que harías antes de "
                      "salir de la casa, y después separa las palabras que sirven en cualquier parte de la que solo "
                      "sirve en un lugar.")
    x0, ww = x + 22, w - 44
    items = (("Bring your ID.", "¿qué tengo que llevar?"),
             ("Payment is required…", "¿qué tengo que hacer?"),
             ("…before the medical appointment.", "¿antes de qué?"))
    for k, (frag, ps) in enumerate(items):
        by = yy + k * 70
        caja(b, x0, by, ww, 60, c, r=12)
        b.append(checkbox(x0 + 18, by + 19, s=11, c=c))
        texto(b, x0 + 56, by + 38, frag, size=20, weight="700")
        pista(b, x0 + 420, by + 37, ps)
        renglon(b, x0 + 600, by + 40, x0 + ww - 20)
    yy += 226
    half = (ww - 30) / 2
    for k, (tit, ps) in enumerate((("PALABRAS QUE SIRVEN EN MUCHOS LUGARES", "documento y pago se piden en muchas partes"),
                                   ("LA PALABRA QUE SOLO ENCAJA EN UN LUGAR", "esta es la que decide"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 150, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        pista(b, bx + 18, yy + 58, ps)
        renglon(b, bx + 18, yy + 100, bx + half - 18)
        renglon(b, bx + 18, yy + 136, bx + half - 18)
    yy += 168
    yy = trampa(b, x0, yy, ww, "Pagar y mostrar un documento no te dice dónde estás:",
                "esas dos pistas sirven en muchas opciones a la vez. Antes de marcar, busca en el aviso la palabra que "
                "dice qué clase de cita es y escoge el único lugar donde esa cita ocurre.", c)
    return yy


# ───────── P19 · Airplane cabin · Venn ─────────
def i19(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Dos círculos, un solo lugar", c,
                      "Cada pista del aviso sirve para varios lugares. El lugar del aviso es el que está en las dos "
                      "pistas a la vez. Escribe dentro de cada círculo los lugares donde existe esa cosa; en el "
                      "centro, el que está en los dos.")
    x0, ww = x + 22, w - 44
    cy = yy + 222
    r = 176
    cxa, cxb = x0 + 330, x0 + 560
    for cxx in (cxa, cxb):
        b.append(f'<circle cx="{cxx}" cy="{cy}" r="{r}" fill="{tinte(c, 0.96)}" fill-opacity="0.6" '
                 f'stroke="{c}" stroke-width="2.4"/>')
    texto(b, cxa - 60, yy + 26, "seat belt", size=21, weight="700", anchor="middle")
    texto(b, cxb + 60, yy + 26, "turbulence", size=21, weight="700", anchor="middle")
    for k in range(3):
        renglon(b, cxa - 140, cy - 40 + k * 50, cxa - 40)
        renglon(b, cxb + 40, cy - 40 + k * 50, cxb + 140)
    pista(b, (cxa + cxb) / 2, cy - 30, "en los dos:", anchor="middle")
    renglon(b, (cxa + cxb) / 2 - 50, cy + 20, (cxa + cxb) / 2 + 50)
    rx = x0 + 790
    rw = ww - 790
    filas = (("seat belt", "es…"), ("turbulence", "es…"), ("fasten", "es lo que haces con…"),
             ("expected", "quiere decir…"))
    for k, (pal, ps) in enumerate(filas):
        by = yy + 30 + k * 94
        caja(b, rx, by, rw, 80, c, r=12)
        texto(b, rx + 16, by + 32, pal, size=19, weight="700")
        pista(b, rx + 150, by + 31, ps)
        renglon(b, rx + 16, by + 66, rx + rw - 16)
    yy += 420
    return ojo(b, x0, yy, ww, "LA PALABRA MÁS RARA ES LA QUE MÁS AYUDA",
               "«Turbulence» se parece a «turbulencia». Las palabras comunes (please, your, ready) aparecen en "
               "cualquier aviso; la palabra rara casi siempre pertenece a un solo lugar. Empieza por ella.")


# ───────── P20 · Streaming service email · if… will ─────────
def i20(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Si pasa esto, entonces pasa aquello", c,
                      "El aviso 20 es una advertencia con condición: if… will… Separa la condición de la consecuencia "
                      "y piensa quién tiene el poder de cumplir esa advertencia.")
    x0, ww = x + 22, w - 44
    half = (ww - 70) / 2
    partes = (("SI · if…", "payment fails before July 10", "lo que tendría que pasar:"),
              ("ENTONCES · will…", "your subscription will be canceled", "lo que me pasaría:"))
    for k, (tit, frag, ps) in enumerate(partes):
        bx = x0 + k * (half + 70)
        caja(b, bx, yy, half, 150, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c)
        texto(b, bx + 18, yy + 66, frag, size=20, weight="700")
        pista(b, bx + 18, yy + 100, ps)
        renglon(b, bx + 18, yy + 134, bx + half - 18)
    flecha(b, x0 + half + 10, yy + 75, x0 + half + 60, yy + 75, c, head=11)
    yy += 170
    caja(b, x0, yy, ww, 130, c, r=14)
    rot(b, x0 + 20, yy + 30, "¿QUÉ ES UNA SUBSCRIPTION?", c)
    pista(b, x0 + 20, yy + 62, "tres cosas a las que la gente se suscribe y paga cada mes:")
    for k in range(3):
        b.append(rect(x0 + 20 + k * 300, yy + 76, 280, 38, "white", r=8, stroke=c, sw=1.8))
    yy += 148
    caja(b, x0, yy, ww, 110, c, r=14)
    rot(b, x0 + 20, yy + 30, "QUIÉN PUEDE CUMPLIR LA ADVERTENCIA", c)
    pista(b, x0 + 20, yy + 64, "¿quién puede cancelarte una suscripción? escríbelo con tus palabras:")
    renglon(b, x0 + 20, yy + 96, x0 + ww - 20)
    yy += 128
    return ojo(b, x0, yy, ww, "WILL BE CANCELED: TODAVÍA NO HA PASADO",
               "«Will be» más el verbo habla del futuro: la suscripción aún no se ha cancelado. Por eso el aviso "
               "llega antes del 10 de julio, para que pagues a tiempo. La X del aviso marca la alerta.")


# ───────── P21 · Airport · passport ─────────
def i21(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Los papeles que te piden en cada viaje", c,
                      "Cada documento te lo piden en un lugar distinto. Llena la tabla y busca el lugar donde te "
                      "piden a la vez los dos documentos del aviso y además hay control de inmigración.")
    x0, ww = x + 22, w - 44
    cols = (240, 400, ww - 640)
    yy = tabla_vacia(b, x0, yy, cols, ("DOCUMENTO", "¿QUÉ ES?", "¿DÓNDE ME LO PIDEN?"),
                     ("passport", "boarding pass", "ID card", "ticket"), c, rh=56, hh=42)
    yy += 20
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "IMMIGRATION CONTROL", c)
    pista(b, x0 + 20, yy + 64, "se parece a la palabra en español:")
    renglon(b, x0 + 290, yy + 66, x0 + ww / 2)
    pista(b, x0 + 20, yy + 104, "¿quién pasa por un control de inmigración: alguien que se mueve en su ciudad o alguien que")
    pista(b, x0 + 20, yy + 130, "llega de otro país?  ¿en qué medio de transporte, casi siempre?")
    renglon(b, x0 + 470, yy + 132, x0 + ww - 20)
    yy += 168
    return ojo(b, x0, yy, ww, "LA OPCIÓN NO REPITE LAS PALABRAS DEL AVISO",
               "Ninguna opción dice «immigration». La que vale es el lugar donde, además del control, tendrías "
               "que tener listos los dos papeles. Si una opción encaja con una sola pista, todavía no es la "
               "respuesta.")


Q = {1: dict(n=1, est=1, pag=414, ctx="Parte 1 · People and What They do · repairs", inst=i1,
             comp="Léxico", letras="ABCDEFGH"),
     5: dict(n=5, est=2, pag=414, ctx="Parte 1 · People · helping people without being paid", inst=i5,
             comp="Léxico", letras="ABCDEFGH"),
     7: dict(n=7, est=2, pag=414, ctx="Parte 1 · People · travels but does not drive", inst=i7,
             comp="Léxico", letras="ABCDEFGH"),
     11: dict(n=11, est=1, pag=414, ctx="Parte 1 · School Life · borrow academic books", inst=i11,
              comp="Léxico", letras="ABCDEFGH"),
     13: dict(n=13, est=1, pag=414, ctx="Parte 1 · School Life · discuss a topic", inst=i13,
              comp="Léxico", letras="ABCDEFGH"),
     16: dict(n=16, est=4, pag=415, ctx="Parte 2 · aviso · Your package is ready", inst=i16,
              comp="Pragmático", letras="ABC"),
     18: dict(n=18, est=4, pag=415, ctx="Parte 2 · aviso · Bring your ID", inst=i18,
              comp="Pragmático", letras="ABC"),
     19: dict(n=19, est=3, pag=415, ctx="Parte 2 · aviso · Fasten your seat belt", inst=i19,
              comp="Pragmático", letras="ABC"),
     20: dict(n=20, est=4, pag=415, ctx="Parte 2 · aviso · Your subscription", inst=i20,
              comp="Pragmático", letras="ABC"),
     21: dict(n=21, est=3, pag=415, ctx="Parte 2 · aviso · Immigration control", inst=i21,
              comp="Pragmático", letras="ABC")}

PARES = ((1, 5), (7, 11), (13, 16), (18, 19), (20, 21))


def build(pages=(269, 270, 272, 273, 274)):
    out = []
    for k, (a, b_) in enumerate(PARES):
        out.append(hoja_taller(f"ing1_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
