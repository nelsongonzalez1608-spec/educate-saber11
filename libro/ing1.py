#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 1 · Partes 1 y 2 del ICFES · componente léxico · pragmático · páginas 269–281.

Versión 3 (7 nov 2026, decisión de Nelson): el cuaderno trabaja LAS 21 PREGUNTAS del libro, una
tarjeta por pregunta, cada una con su subestrategia y su propio instrumento. La versión 2 (10 de
las 21) quedó en el historial de git.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 1» de Inglés (fuente_libro/INGLÉS), páginas 414–415.
  · Parte 1 (léxico, = Parte 1 del ICFES): 14 descripciones que se emparejan con un banco de
    palabras A–H, en dos grupos de 7: «People and What They do» (1–7; la I, Journalist, es la del
    ejemplo) y «School Life» (8–14). En cada grupo sobra una palabra.
  · Parte 2 (pragmático, = Parte 2 del ICFES): 7 avisos, «¿dónde lo verías?», A–C (15–21).

Estrategia de las dos partes (va en tema=): «La pista que decide».
    Parte 1 · 1 ¿persona, lugar o cosa? · 2 leo el verbo · 3 cada pista tacha · 4 tacho la usada
    Parte 2 · 1 la palabra rara del aviso · 2 qué me pide y quién lo escribe · 3 dónde pasa eso ·
              4 la opción que cumple todas las pistas
La línea de contexto de cada tarjeta nombra el paso que se ejercita.

Subestrategias (2 de la Parte 1 + 2 de la Parte 2; nombres y colores sin cambio: las hojas ICFES
274 y 281 los usan):
    1 · El verbo delata la palabra       azul    1, 4, 6, 8, 10, 11, 13       · ICFES QA (watch)
    2 · Cada pista tacha opciones        rojo    2, 3, 5, 7, 9, 12, 14        · ICFES QB (bus)
    3 · ¿Dónde estaría este aviso?       morado  15, 17, 19, 21               · ICFES QC (bookshelf)
    4 · Quién me escribe y qué quiere    oro     16, 18, 20                   · ICFES QD (shop)

Claves verificadas (resueltas otra vez a mano contra el libro, 7 nov 2026, al hacer cada tarjeta):

    Parte 1 · 1·C  2·A  3·B  4·H  5·D  6·E  7·F  (sobra G Baker; I Journalist es el ejemplo)
              8·B  9·A  10·C  11·D  12·E  13·F  14·G  (sobra H Bookshop)
    Parte 2 · 15·A  16·B  17·A  18·C  19·A  20·B  21·C

  1 · C Technician: «a person who REPAIRS electrical machines».
  2 · A Factory: «a PLACE where people work making cars or machines»: el único lugar del banco.
  3 · B Nurse: «helps PATIENTS BUT IS NOT A DOCTOR».
  4 · H Driver: «DRIVES people from one place to another FOR MONEY». Passenger viaja, no maneja.
  5 · D Volunteer: «WITHOUT being paid».
  6 · E Artist: «CREATES PAINTINGS OR SCULPTURES».
  7 · F Passenger: «travels… BUT DOES NOT DRIVE».
  8 · B Lecture hall: «a place where students LISTEN to a teacher and TAKE NOTES».
  9 · A Laboratory: «a ROOM where scientific EXPERIMENTS are done».
 10 · C Student: «a person who STUDIES for a degree at a university».
 11 · D Library: «BORROW academic books» (Bookshop vende: buy).
 12 · E Exam: «a TEST students take to enter a university».
 13 · F Seminar: «a group of students who DISCUSS a topic with a teacher».
 14 · G ID card: «an official CARD that PROVES you are a student».
 15 · A Library: «Please RETURN BOOKS on time. Others are waiting for them».
 16 · B Delivery App: «Your PACKAGE is ready. Pay ONLINE to schedule DELIVERY».
 17 · A Social media post: «Don't share personal information in the COMMENTS. Report suspicious
      ACCOUNTS»: comentarios y cuentas solo existen en una red social.
 18 · C Hospital reception: «… before the MEDICAL APPOINTMENT».
 19 · A Airplane cabin: «Fasten your SEAT BELT. TURBULENCE expected».
 20 · B Streaming service email: «Your SUBSCRIPTION will be canceled if payment fails».
 21 · C Airport security area: «IMMIGRATION control: keep PASSPORT and BOARDING PASS ready».

Reparto: Parte 1 casi en el orden alfabético del banco (C A B H D E F · B A C D E F G); Parte 2:
A 3 · B 2 · C 2. El cuaderno NO lo dice (decirlo regalaría las claves); para neutralizarlo, cada
instrumento de la Parte 1 pide escribir la PALABRA antes de marcar la letra. Hallazgo para la
editorial (ing1_hallazgos.csv).

Correcciones EDUCATE impresas:
  1 · el banco del grupo 1 muestra la I (Journalist) con su círculo, como si fuera opción: es la
      del ejemplo, no se marca en 1 a 7.
 21 · ninguna opción nombra con exactitud el lugar del aviso (inmigración y filtro de seguridad son
      puntos distintos del aeropuerto): escoger la que más se acerca y escribir el nombre exacto.
Hallazgos que NO se imprimen como corrección: «Factory» en el grupo de personas (la descripción 2
dice «a place», el título del grupo no manda: va como ojo en la tarjeta 2), «Seminar» definido
como «a group of students» (Atención; la tarjeta 13 pide mirar el verbo) y las definiciones
amplias de 10 y 12 (Atención).

Hojas (11 de taller + 2 ICFES):
  269 t1 (1-2) · 270 t2 (3-4) · 271 t3 (5-6) · 272 t4 (7-8) · 273 t5 (9-10) · 274 ing1_i1 ·
  275 t6 (11-12) · 276 t7 (13-14) · 277 t8 (15-16) · 278 t9 (17-18) · 279 t10 (19-20) ·
  280 t11 (21 + cierre de la misión) · 281 ing1_i2.
"""
from taller_base import *
from ing_diario import correccion, cierre_mision, ctx_ok

configurar("Inglés", 1, "léxico · pragmático",
           tema="Partes 1 y 2 · La pista que decide",
           nota="LAS PALABRAS QUE SUBRAYÉ", prefijo="Subestrategia", n_hojas=11)
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


def letrero(b, cx, y, lineas, c, w=620, size=22):
    """El aviso del libro redibujado como letrero, con su texto tal cual."""
    h = 30 + len(lineas) * (size + 12)
    x = cx - w / 2
    b.append(rect(x - 8, y, w + 16, h + 16, "white", r=8, stroke=c, sw=2))
    b.append(rect(x, y + 8, w, h, tinte(c, 0.94), r=6, stroke=tinte(c, 0.7), sw=1.4))
    for k, ln in enumerate(lineas):
        texto(b, cx, y + 8 + 22 + size + k * (size + 12) - 6, ln, size=size,
              weight="700" if k == 0 else "400", anchor="middle")
    return y + h + 16


def palabra_primero(b, x, y, c, x_fin):
    """La Parte 1: primero la palabra, después la letra (neutraliza el orden del banco)."""
    t = "la palabra del banco, escrita en inglés, antes de mirar la letra:"
    pista(b, x, y + 20, t)
    renglon(b, x + tw(t, 15, "400", "italic") + 14, y + 22, x_fin)
    return y + 34


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
    yy = ojo(b, x0, yy, ww, "PALABRAS QUE SE PARECEN AL ESPAÑOL",
             "«Electrical» se parece a «eléctrico» y significa lo mismo: es un cognado. Los cognados ayudan "
             "muchísimo, pero hay falsos amigos: «actually» no es «actualmente», es «en realidad». Confirma "
             "siempre con el resto de la frase.")
    return correccion(b, x0, yy + 16, ww,
                      "En tu libro, el banco del grupo People muestra la opción I (Journalist) con su círculo, como "
                      "si fuera una opción más. No lo es: la I es la del ejemplo (la 0). En las preguntas 1 a 7 "
                      "escoges solo entre A y H; tacha el círculo de la I.")


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
                      "Sigue el camino del libro y mira qué papel te dan en cada lugar.")
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
    half0 = (ww - 30) / 2
    for k, (tit, l1, l2) in enumerate((("PAPEL 1", "RECEIPT", "Total paid: $45.000"),
                                       ("PAPEL 2", "DUE DATE", "Return by: November 20"))):
        bx = x0 + k * (half0 + 30)
        b.append(rect(bx, yy, half0, 126, tinte(c, 0.96), r=6, stroke=c, sw=2, dash="3,4"))
        rot(b, bx + 18, yy + 26, tit, c, size=13)
        texto(b, bx + 18, yy + 60, l1, size=20, weight="700")
        texto(b, bx + 18 + tw(l1, 20, "700") + 24, yy + 60, l2, size=18)
        pista(b, bx + 18, yy + 98, "¿en cuál de los dos lugares me lo dan?")
        renglon(b, bx + 290, yy + 100, bx + half0 - 18)
    yy += 146
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
    yy += 50
    vw = (ww - 2 * 20) / 3
    for k, v in enumerate(("listen", "take notes", "discuss")):
        bx = x0 + k * (vw + 20)
        b.append(rect(bx, yy, vw, 140, tinte(c, 0.96), r=30, stroke=c, sw=2))
        texto(b, bx + 30, yy + 40, v, size=21, weight="700")
        pista(b, bx + 30, yy + 76, "en español:")
        renglon(b, bx + 120, yy + 78, bx + vw - 30)
        for j, lab in enumerate(("habla uno", "hablan todos")):
            b.append(checkbox(bx + 30 + j * 150, yy + 96, s=9, c=c))
            texto(b, bx + 54 + j * 150, yy + 112, lab, size=15, color=GRAY)
    yy += 158
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
    return correccion(b, x0, yy, ww,
                      "Ninguna de las tres opciones del libro nombra con exactitud el lugar de este aviso: en un "
                      "aeropuerto de verdad, el control de inmigración y el filtro de seguridad son dos puntos "
                      "distintos. Marca la opción que más se acerca a las tres pistas y escribe en el margen cómo "
                      "se llama, exacto, el lugar donde verías el aviso.")



# ═════════ instrumentos nuevos de la v3 (las 11 preguntas que antes no se trabajaban) ═════════

# ───────── P2 · Factory · a place ─────────
def i2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dos montones: personas y lugares", c,
                      "La primera pista de una descripción dice qué clase de cosa es: «a person who…» o «a place "
                      "where…». Antes de leer el resto, reparte las ocho palabras del banco en dos montones. "
                      "Escríbelas en inglés.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "2.  This is a place where people work making cars or machines.", c,
              rotulo="LA DESCRIPCIÓN · ENCIERRA LA PALABRA QUE DICE QUÉ CLASE DE COSA ES")
    yy += 20
    half = (ww - 40) / 2
    for k, (tit, ps, n) in enumerate((("MONTÓN 1 · PERSONAS", "a person who…", 8),
                                      ("MONTÓN 2 · LUGARES", "a place where…", 8))):
        bx = x0 + k * (half + 40)
        caja(b, bx, yy, half, 300, c, sw=2.4, r=16, fill=tinte(c, 0.97))
        rot(b, bx + 20, yy + 32, tit, c, size=14)
        pista(b, bx + 20 + tw(tit, 14, "700") + 40, yy + 32, ps)
        sw_ = (half - 60) / 2
        for j in range(n):
            sx = bx + 20 + (j % 2) * (sw_ + 20)
            sy = yy + 52 + (j // 2) * 60
            b.append(rect(sx, sy, sw_, 48, "white", r=10, stroke=tinte(c, 0.55), sw=1.8))
    yy += 320
    caja(b, x0, yy, ww, 160, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL RESTO DE LA DESCRIPCIÓN CONFIRMA", c, size=14)
    pista(b, x0 + 20, yy + 66, "«people work making cars or machines»: ¿qué se hace en ese lugar?")
    renglon(b, x0 + 520, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 104, "en español, ese lugar se llama:")
    renglon(b, x0 + 250, yy + 106, x0 + ww - 20)
    palabra_primero(b, x0 + 20, yy + 122, c, x0 + ww - 20)
    yy += 178
    return ojo(b, x0, yy, ww, "EL TÍTULO DEL GRUPO NO MANDA",
               "El grupo se llama «People and What They do», pero no todo el banco son personas. Lo que manda "
               "es la descripción que estás leyendo: si dice «a place», buscas en el montón de los lugares.")


# ───────── P3 · Nurse · helps patients but is not a doctor ─────────
def i3(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Se parece al doctor, pero no es el doctor", c,
                      "Primero piensa en todas las personas que ayudan a un paciente. Después deja que «but is "
                      "not a doctor» corte una. Llena la estrella antes de mirar el banco.")
    x0, ww = x + 22, w - 44
    cx, cy = x0 + ww / 2, yy + 200
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="170" ry="54" fill="{tinte(c, 0.92)}" stroke="{c}" '
             f'stroke-width="2.4"/>')
    texto(b, cx, cy - 4, "helps patients", size=22, weight="700", anchor="middle")
    pista(b, cx, cy + 24, "patients =  ¿cognado?", anchor="middle")
    puntas = ((x0 + 150, yy + 60), (x0 + ww - 150, yy + 60), (x0 + 150, yy + 340), (x0 + ww - 150, yy + 340))
    for k, (px, py) in enumerate(puntas):
        bw, bh = 300, 84
        caja(b, px - bw / 2, py - bh / 2, bw, bh, c, r=14)
        if k == 0:
            texto(b, px, py + 8, "a doctor", size=20, weight="700", anchor="middle")
        else:
            pista(b, px - bw / 2 + 16, py - 12, "otra persona que ayuda:", size=14)
            renglon(b, px - bw / 2 + 16, py + 26, px + bw / 2 - 16)
        ex = cx - 170 if px < cx else cx + 170
        flecha(b, ex + (-6 if px < cx else 6), cy + (-14 if py < cy else 14),
               px + (bw / 2 if px < cx else -bw / 2), py, c, sw=2.2, head=9, bend=0.1)
    yy += 410
    caja(b, x0, yy, ww, 170, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "LA TIJERA · BUT IS NOT A DOCTOR", c, size=14)
    pista(b, x0 + 20, yy + 66, "tacha en la estrella a quien corta esta pista. ¿Quiénes siguen en pie?")
    renglon(b, x0 + 560, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 108, "de los que siguen en pie, ¿cuál tiene su palabra en el banco?")
    renglon(b, x0 + 560, yy + 110, x0 + ww - 20)
    palabra_primero(b, x0 + 20, yy + 126, c, x0 + ww - 20)
    yy += 190
    return ojo(b, x0, yy, ww, "BUT ES UNA TIJERA",
               "Después de «but» viene lo que NO es. Las descripciones del ICFES lo usan mucho: primero te acercan "
               "(alguien que ayuda a pacientes) y después te cortan la opción más obvia.")


# ───────── P4 · Driver · drives people for money ─────────
def i4(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "De un lugar a otro: quién maneja y quién cobra", c,
                      "El verbo «drives» pone a alguien al volante. Dibuja el viaje de la descripción y escribe "
                      "en cada caja lo que pasa. La pista «for money» dice quién recibe la plata.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 250, c, r=16, fill=tinte(c, 0.97))
    ay, ax1, ax2 = yy + 150, x0 + 110, x0 + ww - 110
    for px, lab in ((ax1, "one place"), (ax2, "another place")):
        b.append(f'<circle cx="{px}" cy="{ay}" r="30" fill="white" stroke="{c}" stroke-width="2.6"/>')
        texto(b, px, ay + 62, lab, size=17, color=c, weight="700", anchor="middle")
    b.append(line(ax1 + 34, ay, ax2 - 34, ay, c, 2.4, dash="12,10"))
    kx = x0 + ww / 2 - 80
    b.append(rect(kx, ay - 66, 160, 52, "white", r=14, stroke=c, sw=2.4))
    b.append(rect(kx + 26, ay - 92, 100, 30, "white", r=10, stroke=c, sw=2.2))
    for wx in (kx + 36, kx + 124):
        b.append(f'<circle cx="{wx}" cy="{ay - 12}" r="13" fill="white" stroke="{c}" stroke-width="2.4"/>')
    texto(b, x0 + 20, yy + 34, "drives people from one place to another for money", size=21, weight="700")
    yy += 268
    pw = (ww - 2 * 24) / 3
    for k, (tit, ps) in enumerate((("DRIVES", "¿quién va al volante?"),
                                   ("PEOPLE", "¿quiénes van sentados atrás?"),
                                   ("FOR MONEY", "¿quién paga y quién cobra?"))):
        bx = x0 + k * (pw + 24)
        caja(b, bx, yy, pw, 140, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c, size=14)
        pista(b, bx + 18, yy + 60, ps)
        renglon(b, bx + 18, yy + 96, bx + pw - 18)
        renglon(b, bx + 18, yy + 126, bx + pw - 18)
    yy += 160
    caja(b, x0, yy, ww, 110, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PERSONA QUE MANEJA Y COBRA", c, size=14)
    pista(b, x0 + 20, yy + 64, "en español, su oficio es:")
    renglon(b, x0 + 200, yy + 66, x0 + ww - 20)
    palabra_primero(b, x0 + 20, yy + 72, c, x0 + ww - 20)
    yy += 128
    return trampa(b, x0, yy, ww, "En el mismo carro van dos palabras del banco:",
                  "una va al volante y otra va sentada. Las dos «viajan», pero solo una «drives… for money». Antes de "
                  "marcar, revisa que tu palabra haga lo que dice el verbo, no solo que vaya en el carro.", c)


# ───────── P6 · Artist · creates paintings or sculptures ─────────
def i6(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "De la obra a quien la hace: -er, -or, -ist, -ian", c,
                      "En inglés, la persona que hace algo casi siempre lleva una terminación pegada. Completa cada "
                      "escalera con lo que crees que va y escribe la palabra en español. Después usa lo aprendido en "
                      "la descripción 6.")
    x0, ww = x + 22, w - 44
    escaleras = (("a piano", "a pian", "quién lo toca"), ("to act", "an act", "quién lo hace"),
                 ("to teach", "a teach", "quién lo hace"), ("music", "a music", "quién la hace"))
    half = (ww - 30) / 2
    for k, (obra, raiz, ps) in enumerate(escaleras):
        bx = x0 + (k % 2) * (half + 30)
        by = yy + (k // 2) * 150
        caja(b, bx, by, half, 134, c, r=14)
        texto(b, bx + 20, by + 42, obra, size=21, weight="700")
        flecha(b, bx + 30 + tw(obra, 21, "700"), by + 36, bx + 60 + tw(obra, 21, "700") + 30, by + 36, c, head=9)
        rx = bx + 100 + tw(obra, 21, "700")
        texto(b, rx, by + 42, raiz, size=21, weight="700")
        b.append(rect(rx + tw(raiz, 21, "700") + 4, by + 14, 74, 38, "white", r=8, stroke=c, sw=2))
        pista(b, bx + 20, by + 84, f"en español ({ps}):")
        renglon(b, bx + 20, by + 118, bx + half - 20)
    yy += 2 * 150 + 4
    yy = cita(b, x0, yy, ww, "6.  This is a person who creates paintings or sculptures.", c,
              rotulo="LA DESCRIPCIÓN 6 · SUBRAYA LAS DOS OBRAS")
    yy += 18
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "DE LAS OBRAS A LA PERSONA", c, size=14)
    pista(b, x0 + 20, yy + 66, "paintings y sculptures, en español:")
    renglon(b, x0 + 280, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 106, "la palabra del banco con una de estas terminaciones que hace las dos cosas:")
    renglon(b, x0 + 560, yy + 108, x0 + ww - 20)
    pista(b, x0 + 20, yy + 138, "(la escribo en inglés y solo después busco su letra)")
    return yy + 150


# ───────── P8 · Lecture hall · listen and take notes ─────────
def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Palabras de dos piezas y un falso amigo", c,
                      "Tres palabras del banco de School Life están hechas de dos piezas. Sepáralas, escribe qué "
                      "crees que significa cada pieza y después las dos juntas. Una de las piezas se parece al "
                      "español y te engaña.")
    x0, ww = x + 22, w - 44
    for k, (p1, p2) in enumerate((("Lecture", "hall"), ("ID", "card"), ("Book", "shop"))):
        by = yy + k * 104
        for j, p in enumerate((p1, p2)):
            bx = x0 + j * 190
            b.append(rect(bx, by, 180, 84, tinte(c, 0.93), r=12, stroke=c, sw=2.2))
            texto(b, bx + 90, by + 34, p, size=22, weight="700", anchor="middle")
            renglon(b, bx + 16, by + 70, bx + 164)
        texto(b, x0 + 400, by + 50, "=", size=30, color=c, weight="700")
        caja(b, x0 + 440, by, ww - 440, 84, c, r=12)
        pista(b, x0 + 460, by + 30, "las dos piezas juntas:")
        renglon(b, x0 + 460, by + 68, x0 + ww - 20)
    yy += 3 * 104 + 8
    yy = cita(b, x0, yy, ww, "8.  This is a place where students listen to a teacher and take notes.", c,
              rotulo="LA DESCRIPCIÓN 8 · ENCIERRA LOS DOS VERBOS")
    yy += 18
    caja(b, x0, yy, ww, 118, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE PASA EN ESE LUGAR", c, size=14)
    pista(b, x0 + 20, yy + 66, "¿quién habla y quién escucha? ¿qué hacen las manos de los estudiantes?")
    renglon(b, x0 + 560, yy + 68, x0 + ww - 20)
    palabra_primero(b, x0 + 20, yy + 80, c, x0 + ww - 20)
    yy += 136
    return ojo(b, x0, yy, ww, "UN FALSO AMIGO EN EL BANCO",
               "«Lecture» se parece a «lectura», pero no quiere decir leer. Escribe arriba lo que crees que es y "
               "confírmalo en clase. Los falsos amigos son las trampas favoritas de la Parte 1.")


# ───────── P9 · Laboratory · a room where experiments are done ─────────
def i9(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El embudo: cada pista deja pasar menos palabras", c,
                      "Echa el banco de School Life por el embudo. En cada nivel escribe solo las palabras que pasan "
                      "esa pista. Abajo debe salir una sola.")
    x0, ww = x + 22, w - 44
    niveles = (("PISTA 1 · a room", "¿cuáles son salones o lugares? escríbelas", 1.00, 0),
               ("PISTA 2 · where experiments are done", "¿en cuáles de esas se hacen experimentos?", 0.74, 0),
               ("PISTA 3 · scientific", "¿cuál es de ciencias?", 0.48, 1))
    cx = x0 + ww / 2
    lh = 150
    for k, (tit, ps, f, n) in enumerate(niveles):
        top_w = ww * f
        bot_w = ww * (niveles[k + 1][2] if k < 2 else 0.30)
        ty, by_ = yy + k * (lh + 10), yy + k * (lh + 10) + lh
        pts = (f"{cx - top_w / 2:.1f},{ty} {cx + top_w / 2:.1f},{ty} "
               f"{cx + bot_w / 2:.1f},{by_} {cx - bot_w / 2:.1f},{by_}")
        b.append(f'<polygon points="{pts}" fill="{tinte(c, 0.95)}" stroke="{c}" stroke-width="2.4" '
                 f'stroke-linejoin="round"/>')
        texto(b, cx, ty + 34, tit, size=19, weight="700", anchor="middle")
        pista(b, cx, ty + 58, ps, anchor="middle")
        if k < 2:
            lw_ = bot_w - 60
            renglon(b, cx - lw_ / 2, ty + 100, cx + lw_ / 2)
            renglon(b, cx - lw_ / 2, ty + 136, cx + lw_ / 2)
        else:
            b.append(rect(cx - 110, ty + 76, 220, 50, "white", r=10, stroke=c, sw=2))
    yy += 3 * (lh + 10) + 10
    caja(b, x0, yy, ww, 130, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA QUE SALIÓ DEL EMBUDO", c, size=14)
    pista(b, x0 + 20, yy + 66, "se parece a esta palabra en español:")
    renglon(b, x0 + 290, yy + 68, x0 + 620)
    pista(b, x0 + 650, yy + 66, "«experiments» se parece a:")
    renglon(b, x0 + 850, yy + 68, x0 + ww - 20)
    palabra_primero(b, x0 + 20, yy + 88, c, x0 + ww - 20)
    return yy + 130


# ───────── P10 · Student · studies for a degree ─────────
def i10(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Degree: ¿temperatura o diploma?", c,
                      "Una palabra en inglés puede tener dos significados. La descripción 10 trae una así. Decide cuál "
                      "significado cabe en la frase y después busca a la persona que hace lo que dice el verbo.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "10.  This is a person who studies for a degree at a university.", c,
              rotulo="LA DESCRIPCIÓN 10")
    yy += 20
    half = (ww - 30) / 2
    # termómetro y diploma
    for k, (tit, ej) in enumerate((("DEGREE 1", "It is 30 degrees in Cali today."),
                                   ("DEGREE 2", "She has a degree in medicine."))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 250, c, r=16)
        rot(b, bx + 20, yy + 30, tit, c, size=14)
        texto(b, bx + 20, yy + 66, ej, size=19, weight="700")
        if k == 0:
            tx = bx + half - 70
            b.append(rect(tx, yy + 90, 26, 110, "white", r=13, stroke=c, sw=2.2))
            b.append(f'<circle cx="{tx + 13}" cy="{yy + 210}" r="20" fill="white" stroke="{c}" stroke-width="2.2"/>')
        else:
            dx = bx + half - 150
            b.append(rect(dx, yy + 96, 120, 84, "white", r=6, stroke=c, sw=2.2))
            b.append(f'<circle cx="{dx + 96}" cy="{yy + 172}" r="16" fill="white" stroke="{c}" stroke-width="2.2"/>')
        pista(b, bx + 20, yy + 112, "aquí «degree» quiere decir:")
        renglon(b, bx + 20, yy + 152, bx + half - 180)
        pista(b, bx + 20, yy + 196, "¿cabe en la descripción 10?")
        sino(b, bx + 20, yy + 210, c)
    yy += 270
    caja(b, x0, yy, ww, 176, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL VERBO Y LA PERSONA", c, size=14)
    pista(b, x0 + 20, yy + 66, "studies, en español:")
    renglon(b, x0 + 170, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 108, "¿quién estudia en una universidad para sacar un degree?")
    renglon(b, x0 + 420, yy + 110, x0 + ww - 20)
    pista(b, x0 + 20, yy + 150, "el verbo y la palabra del banco se parecen: escríbelas juntas y subraya lo que comparten:")
    renglon(b, x0 + 640, yy + 152, x0 + ww - 20)
    return yy + 176


# ───────── P12 · Exam · a test to enter a university ─────────
def i12(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La balanza: la descripción ya trae un sinónimo", c,
                      "A veces la descripción usa una palabra que pesa lo mismo que una del banco: un sinónimo. "
                      "Ponla en el plato izquierdo y busca en el banco la que equilibra la balanza.")
    x0, ww = x + 22, w - 44
    cx = x0 + ww / 2
    by = yy + 70
    b.append(f'<polygon points="{cx - 60},{yy + 330} {cx + 60},{yy + 330} {cx},{by + 6}" '
             f'fill="{tinte(c, 0.9)}" stroke="{c}" stroke-width="2.4" stroke-linejoin="round"/>')
    b.append(line(cx - 420, by, cx + 420, by, c, 4))
    b.append(f'<circle cx="{cx}" cy="{by}" r="10" fill="{c}"/>')
    for k, sx in enumerate((cx - 400, cx + 400)):
        b.append(line(sx, by, sx - 110, by + 120, c, 2))
        b.append(line(sx, by, sx + 110, by + 120, c, 2))
        b.append(f'<path d="M {sx - 150} {by + 120} L {sx + 150} {by + 120} L {sx + 110} {by + 170} '
                 f'L {sx - 110} {by + 170} Z" fill="white" stroke="{c}" stroke-width="2.4"/>')
        pista(b, sx, by + 200, "de la descripción:" if k == 0 else "del banco (en inglés):", anchor="middle")
        renglon(b, sx - 120, by + 156, sx + 120)
    yy += 360
    yy = cita(b, x0, yy, ww, "12.  This is a test students take to enter a university or a program.", c,
              rotulo="LA DESCRIPCIÓN 12")
    yy += 18
    caja(b, x0, yy, ww, 160, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PRUEBA QUE YO CONOZCO", c, size=14)
    pista(b, x0 + 20, yy + 66, "«to take a test», en español, se dice:")
    renglon(b, x0 + 290, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 106, "¿cómo se llama en Colombia la prueba que se presenta para entrar a la universidad?")
    renglon(b, x0 + 620, yy + 108, x0 + ww - 20)
    pista(b, x0 + 20, yy + 146, "y en inglés, esa clase de prueba se llama un…")
    renglon(b, x0 + 340, yy + 148, x0 + 700)
    return yy + 160


# ───────── P14 · ID card · proves you are a student ─────────
def i14(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El carné que me pide el portero", c,
                      "Llena el carné como si fuera tuyo. Después busca en la descripción 14 las tres pistas y mira "
                      "cuál palabra del banco cumple las tres. Al final, revisa qué palabra sobró en el grupo.")
    x0, ww = x + 22, w - 44
    kw, kh = 560, 300
    caja(b, x0, yy, kw, kh, c, sw=2.6, r=22, fill=tinte(c, 0.96))
    b.append(rect(x0, yy, kw, 56, c, r=22))
    b.append(rect(x0, yy + 30, kw, 26, c, r=0))
    texto(b, x0 + 24, yy + 38, "STUDENT CARD", size=19, color="white", weight="700")
    b.append(rect(x0 + 24, yy + 80, 150, 190, "white", r=10, stroke=c, sw=2))
    pista(b, x0 + 99, yy + 180, "foto", anchor="middle")
    for k, lab in enumerate(("name:", "school:", "number:", "valid until:")):
        ly = yy + 104 + k * 50
        pista(b, x0 + 196, ly, lab)
        renglon(b, x0 + 196 + tw(lab, 15, "400", "italic") + 10, ly + 2, x0 + kw - 24)
    rx, rw = x0 + kw + 30, ww - kw - 30
    for k, (pis, ps) in enumerate((("official", "¿quién lo entrega?"), ("card", "¿qué forma tiene?"),
                                   ("proves you are a student", "¿para qué sirve?"))):
        by = yy + k * 102
        caja(b, rx, by, rw, 90, c, r=12)
        texto(b, rx + 18, by + 34, pis, size=19, weight="700")
        pista(b, rx + 18 + tw(pis, 19, "700") + 16, by + 33, ps)
        renglon(b, rx + 18, by + 74, rx + rw - 18)
    yy += kh + 20
    palabra_primero(b, x0, yy, c, x0 + ww)
    yy += 44
    caja(b, x0, yy, ww, 170, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "SE CIERRA EL GRUPO SCHOOL LIFE · LA PALABRA QUE SOBRÓ", c, size=14)
    pista(b, x0 + 20, yy + 66, "la palabra del banco que no usé en 8 a 14:")
    renglon(b, x0 + 320, yy + 68, x0 + 640)
    pista(b, x0 + 20, yy + 106, "¿en qué se parece a la de la pregunta 11 y por qué no encaja en ninguna descripción?")
    renglon(b, x0 + 20, yy + 146, x0 + ww - 20)
    return yy + 170


# ───────── P15 · Library · return books… waiting for them ─────────
def i15(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "«Them» señala hacia atrás", c,
                      "Los avisos son cortos y se apoyan en palabras que señalan: «them», «others». Dibuja una flecha "
                      "desde cada una hasta lo que nombra. Con eso sabrás qué cosa espera la gente y dónde.")
    x0, ww = x + 22, w - 44
    y_sign = yy + 6
    yy = letrero(b, x0 + 340, y_sign, ["Please return books on time.", "Others are waiting for them."], c, w=640)
    rx = x0 + 720
    for k, (pal, ps) in enumerate((("them", "señala a:"), ("others", "son:"))):
        by = y_sign + k * 72
        caja(b, rx, by, ww - 720, 62, c, r=12)
        texto(b, rx + 16, by + 38, pal, size=20, weight="700")
        pista(b, rx + 100, by + 37, ps)
        renglon(b, rx + 170, by + 40, rx + ww - 720 - 16)
    yy = max(yy, y_sign + 140) + 34
    # la lista de espera
    lw = 470
    caja(b, x0, yy, lw, 300, c, sw=2.4, r=14, fill=tinte(c, 0.97))
    b.append(rect(x0 + lw / 2 - 60, yy - 12, 120, 28, tinte(c, 0.75), r=8, stroke=c, sw=2))
    texto(b, x0 + lw / 2, yy + 52, "WAITING LIST", size=20, color=c, weight="700", anchor="middle")
    for k in range(4):
        ly = yy + 104 + k * 50
        texto(b, x0 + 26, ly, f"{k + 1}.", size=18, color=c, weight="700")
        renglon(b, x0 + 56, ly + 2, x0 + lw - 26)
    pista(b, x0 + 26, yy + 286, "escribe nombres de tu salón: ¿qué estarían esperando?")
    rx2, rw2 = x0 + lw + 30, ww - lw - 30
    caja(b, rx2, yy, rw2, 300, c, r=14)
    rot(b, rx2 + 20, yy + 30, "¿DÓNDE PASA ESTO?", c, size=14)
    pista(b, rx2 + 20, yy + 66, "¿qué cosa tienes en tu casa que otra persona espera?")
    renglon(b, rx2 + 20, yy + 104, rx2 + rw2 - 20)
    pista(b, rx2 + 20, yy + 146, "¿y por qué la tienes tú, si no es tuya?")
    renglon(b, rx2 + 20, yy + 184, rx2 + rw2 - 20)
    pista(b, rx2 + 20, yy + 226, "el único lugar donde pasa eso (dilo antes de mirar):")
    renglon(b, rx2 + 20, yy + 266, rx2 + rw2 - 20)
    yy += 320
    return ojo(b, x0, yy, ww, "ON TIME",
               "«On time» es «a tiempo». Un aviso que te pide devolver algo a tiempo existe donde las cosas se "
               "prestan con fecha de entrega. Si en un lugar pagas y te llevas la cosa para siempre, nadie te la pide.")


# ───────── P17 · Social media post · comments and accounts ─────────
def i17(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "¿Esto pasa en la calle o en una pantalla?", c,
                      "Cada palabra del aviso vive en algún lugar. Une con una flecha cada palabra con el sitio donde "
                      "existe: la calle, la pantalla o los dos. El aviso está donde viven las palabras más raras.")
    x0, ww = x + 22, w - 44
    yy = letrero(b, x0 + ww / 2, yy, ["Don't share personal information in the comments.",
                                      "Report suspicious accounts."], c, w=820, size=21)
    yy += 16
    # calle (izquierda) · palabras (centro) · pantalla (derecha)
    zh = 330
    caja(b, x0, yy, 300, zh, c, sw=2.4, r=16, fill=tinte(c, 0.97))
    rot(b, x0 + 20, yy + 30, "LA CALLE", c, size=14)
    b.append(rect(x0 + 140, yy + 70, 16, 220, tinte(c, 0.6), r=4))
    b.append(rect(x0 + 70, yy + 74, 156, 70, "white", r=8, stroke=c, sw=2))
    px = x0 + ww - 300
    caja(b, px, yy, 300, zh, c, sw=2.4, r=16, fill=tinte(c, 0.97))
    rot(b, px + 20, yy + 30, "LA PANTALLA", c, size=14)
    b.append(rect(px + 90, yy + 56, 120, 230, "white", r=18, stroke=c, sw=2.4))
    b.append(rect(px + 132, yy + 266, 36, 8, tinte(c, 0.6), r=4))
    pals = ("personal information", "comments", "report", "suspicious", "accounts")
    cx = x0 + ww / 2
    for k, p in enumerate(pals):
        py = yy + 20 + k * 62
        pw = tw(p, 19, "700") + 40
        b.append(rect(cx - pw / 2, py, pw, 46, "white", r=23, stroke=c, sw=2))
        texto(b, cx, py + 30, p, size=19, weight="700", anchor="middle")
    yy += zh + 20
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "QUIÉN LO ESCRIBE Y PARA QUÉ", c, size=14)
    pista(b, x0 + 20, yy + 66, "¿de qué quiere proteger a quien lo lee?")
    renglon(b, x0 + 300, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 106, "las dos palabras que más me dijeron dónde estoy:")
    renglon(b, x0 + 380, yy + 108, x0 + ww - 20)
    pista(b, x0 + 20, yy + 140, "(las dos tienen que vivir en el mismo sitio de la opción que escojas)")
    return yy + 150


L8, L3 = "ABCDEFGH", "ABC"


def _q(n, est, ctx, inst, parte):
    if parte == 1:
        return dict(n=n, est=est, pag=414, ctx=ctx_ok(ctx), inst=inst, comp="Léxico", letras=L8)
    return dict(n=n, est=est, pag=415, ctx=ctx_ok(ctx), inst=inst, comp="Pragmático", letras=L3)


Q = {1: _q(1, 1, "Parte 1 · People · paso 2, leo el verbo: repairs", i1, 1),
     2: _q(2, 2, "Parte 1 · People · paso 1, ¿persona o lugar?: a place", i2, 1),
     3: _q(3, 2, "Parte 1 · People · paso 3, la pista tacha: but is not", i3, 1),
     4: _q(4, 1, "Parte 1 · People · paso 2, leo el verbo: drives", i4, 1),
     5: _q(5, 2, "Parte 1 · People · paso 3, la pista tacha: without", i5, 1),
     6: _q(6, 1, "Parte 1 · People · paso 2, leo el verbo: creates", i6, 1),
     7: _q(7, 2, "Parte 1 · People · paso 4, tacho las usadas: but does not", i7, 1),
     8: _q(8, 1, "Parte 1 · School Life · paso 2, los verbos: listen, take notes", i8, 1),
     9: _q(9, 2, "Parte 1 · School Life · paso 3, cada pista tacha: a room", i9, 1),
     10: _q(10, 1, "Parte 1 · School Life · paso 2, leo el verbo: studies", i10, 1),
     11: _q(11, 1, "Parte 1 · School Life · paso 2, leo el verbo: borrow", i11, 1),
     12: _q(12, 2, "Parte 1 · School Life · paso 3, la pista tacha: a test", i12, 1),
     13: _q(13, 1, "Parte 1 · School Life · paso 2, leo el verbo: discuss", i13, 1),
     14: _q(14, 2, "Parte 1 · School Life · pasos 3 y 4: card · la que sobra", i14, 1),
     15: _q(15, 3, "Parte 2 · aviso · paso 1, la palabra que señala: them", i15, 2),
     16: _q(16, 4, "Parte 2 · aviso · paso 2, qué me pide: Your package", i16, 2),
     17: _q(17, 3, "Parte 2 · aviso · paso 3, dónde pasa: comments, accounts", i17, 2),
     18: _q(18, 4, "Parte 2 · aviso · paso 2, qué me pide: Bring your ID", i18, 2),
     19: _q(19, 3, "Parte 2 · aviso · paso 1, la palabra rara: turbulence", i19, 2),
     20: _q(20, 4, "Parte 2 · aviso · paso 2, quién me escribe: subscription", i20, 2),
     21: _q(21, 3, "Parte 2 · aviso · paso 4, cumple todas: Immigration control", i21, 2)}

PARES = ((1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16), (17, 18), (19, 20))

CIERRE = cierre_mision(
    "Cierre de la Misión 1 · Partes 1 y 2",
    [("LO QUE ME LLEVO DE LA PARTE 1 · DESCRIPCIÓN → PALABRA",
      "la pista que más me sirvió para encontrar la palabra (el verbo, el «but», el lugar…)"),
     ("LO QUE ME LLEVO DE LA PARTE 2 · ¿DÓNDE VERÍAS ESTE AVISO?",
      "lo primero que voy a buscar en un aviso la próxima vez")],
    [("Parte 1 · descripciones (1 a 14)", 14), ("Parte 2 · avisos (15 a 21)", 7)])


def build(pages=(269, 270, 271, 272, 273, 275, 276, 277, 278, 279, 280)):
    out = []
    for k, (a, b_) in enumerate(PARES):
        out.append(hoja_taller(f"ing1_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    out.append(hoja_taller("ing1_t11", pages[10], 11, Q[21], None, cierre=CIERRE))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
