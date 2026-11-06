#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sociales y Ciudadanas · Misión 5 · componente espacio y ambiente · páginas 125–131.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 5» de Ciencias Sociales, páginas 383–386.
Textos: los «territorios invisibles» del barrismo (1), la frontera con Venezuela (2), el este
de Ucrania (3), la mina en Boyacá (4), el asentamiento emberá en el Parque Nacional (5 a 7),
el agua de La Calera (8), el Tapón del Darién (9) y el informe de HRW sobre desplazamiento (10).

Claves verificadas (resueltas a mano contra el texto del libro, no copiadas, 6 nov 2026):

    1·A  2·A  3·B  4·C  5·B  6·A  7·D  8·B  9·C  10·D

Reparto: A 3 · B 3 · C 2 · D 2. Equilibrado. Pero en 1, 2, 4, 8, 9 y 10 la correcta es la que
«integra» a todos y las demás cierran con absolutos («ninguna función», «resuelve al mismo
tiempo», «elimina», «garantiza que no»): registrado en tablero/propuestas/soc5_hallazgos.csv.

Estrategias:
    1 · El lugar explica el problema          (3, 6, 9  · ICFES 5)    verde
    2 · Ninguna voz se queda afuera           (1, 10    · ICFES 6)    azul
    3 · Una medida, efectos en cadena         (2, 5, 8  · ICFES 19)   morado
    4 · Qué dice y qué busca quien habla      (4, 7     · ICFES 18)   rojo

Hojas: 125 soc5_t1 (1-2) · 126 soc5_t2 (3-4) · 127 soc5_i1 · 128 soc5_t3 (5-6) ·
       129 soc5_t4 (7-8) · 130 soc5_t5 (9-10) · 131 soc5_i2.
"""
from taller_base import *

configurar("Sociales y Ciudadanas", 5, "espacio y ambiente",
           tema="El territorio no es neutro: lugar, gente y poder",
           color=EDU_ORO, nota="LO QUE ANOTÉ DEL CASO")
MORADO = "#5B3E96"
EST = {1: ("El lugar explica el problema", EDU_VERDE),
       2: ("Ninguna voz se queda afuera", EDU_AZUL),
       3: ("Una medida, efectos en cadena", MORADO),
       4: ("Qué dice y qué busca quien habla", EDU_ROJO)}
usar_estrategias(EST)
VE, AZ, MO, RO = (EST[k][1] for k in (1, 2, 3, 4))


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def frase_hueco(b, x, y, w, texto, c, h=50):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [texto], 18, INK, weight="700"))
    return y + h


def letra(b, cx, cy, L, c, r=17, size=16):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="2"/>')
    b.append(T(cx, cy + size * 0.38, [L], size, c, weight="700", anchor="middle"))


def parrafo(b, x, y, w, texto, size=17, color=INK, style="normal"):
    svg, yy = TJ(x, y, texto, w, size, color, style=style, lh=size + 8)
    b.append(svg)
    return yy


# ───────── P1 · territorios invisibles · tres actores ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Tres ventanas que dan a la misma esquina", c,
                      "Barristas, vecinos y alcaldía miran el mismo lugar desde ventanas distintas. Escribe qué "
                      "es ese lugar para cada uno y qué quiere hacer con él. Después cuenta a cuántos les respeta "
                      "cada opción lo que de verdad dijeron.")
    x0, ww = x + 22, w - 44
    # el lugar, al centro; tres ventanas alrededor
    cx, cy = x0 + ww / 2, yy + 150
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="150" ry="56" fill="{SOFT}" stroke="{c}" '
             f'stroke-width="2.4" stroke-dasharray="8,6"/>')
    rot(b, cx, cy - 4, "EL «TERRITORIO", c, size=14, anchor="middle")
    rot(b, cx, cy + 20, "INVISIBLE»", c, size=14, anchor="middle")
    vw, vh = 360, 132
    ventanas = ((x0, yy, "LOS BARRISTAS"), (x0 + ww - vw, yy, "LOS VECINOS"),
                (cx - vw / 2, yy + 214, "LA ALCALDÍA"))
    for k, (vx, vy, quien) in enumerate(ventanas):
        caja(b, vx, vy, vw, vh, c, sw=2.2, r=14)
        rot(b, vx + 20, vy + 30, quien, c)
        pista(b, vx + 20, vy + 60, "para ellos, este lugar es…")
        renglon(b, vx + 20, vy + 84, vx + vw - 20)
        pista(b, vx + 20, vy + 110, "y quieren…")
        renglon(b, vx + 104, vy + 112, vx + vw - 20)
    b.append(hand_arrow(x0 + vw + 6, yy + 70, cx - 140, cy - 22, c, sw=2.6, bend=0.12, head=14))
    b.append(hand_arrow(x0 + ww - vw - 6, yy + 70, cx + 140, cy - 22, c, sw=2.6, bend=-0.12, head=14))
    b.append(hand_arrow(cx, yy + 212, cx, cy + 62, c, sw=2.6, bend=0.0, head=14))
    yy += 214 + vh + 24
    b.append(T(x0, yy + 20, ["¿A cuántos actores les respeta cada opción lo que dijeron? (0 a 3)"], 18, INK,
               weight="700"))
    yy += 36
    for k, L in enumerate("ABCD"):
        bx = x0 + k * 190
        letra(b, bx + 18, yy + 22, L, c)
        caja(b, bx + 48, yy, 70, 44, c)
    yy += 64
    return trampa(b, x0, yy, ww, "Una opción pone a los tres de acuerdo:",
                  "dice que barristas, vecinos y alcaldía «coinciden». Mira tus tres ventanas: ¿escribiste lo "
                  "mismo en las tres? Si el texto los muestra en desacuerdo, esa opción le borra la voz a alguien.",
                  c)


# ───────── P2 · frontera con Venezuela · efectos en cadena ─────────
def i2(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La medida baja como una cascada, salto por salto", c,
                      "Una medida que se toma en la frontera no se queda en la frontera. Escribe en cada salto lo "
                      "que pasa y en qué dimensión cae: así ves cómo se encadenan lo económico, lo social y lo "
                      "político.")
    x0, ww = x + 22, w - 44
    pasos = (("1 · LA MEDIDA", "qué se hizo y para qué, según el texto"),
             ("2 · LO QUE LE LLEGA AL BOLSILLO", "dos efectos: remesas, precios, abastecimiento…"),
             ("3 · LO QUE LE LLEGA A LA GENTE", "qué tensión aparece entre los vecinos de la frontera"),
             ("4 · LO QUE LE LLEGA AL PODER", "qué dice la oposición y a quién debilita eso"))
    bw = ww - 3 * 70
    for k, (rt, ps) in enumerate(pasos):
        bx = x0 + k * 70
        caja(b, bx, yy, bw, 92, c, r=14)
        rot(b, bx + 20, yy + 30, rt, c)
        pista(b, bx + 20 + tw(rt, 15, "700") + len(rt) * 1.5 + 16, yy + 30, ps)
        renglon(b, bx + 20, yy + 72, bx + bw - 180)
        b.append(T(bx + bw - 160, yy + 74, ["dimensión: ____"], 15, GRAY))
        if k < 3:
            b.append(hand_arrow(bx + 34, yy + 94, bx + 34 + 60, yy + 116, c, sw=2.6, bend=-0.3, head=12))
        yy += 112
    yy += 4
    yy = frase_hueco(b, x0, yy, ww, "El salto que más me costó llenar fue el ___ , porque el texto __________________ .", c)
    yy += 16
    yy = ojo(b, x0, yy, ww, "ANTES DE TOMAR EL CASO COMO HISTORIA",
             "El libro presenta el cierre de 2024 como un hecho. Pregúntale al profe qué pasó de verdad en la "
             "frontera ese año: para responder basta el texto, pero en Sociales un dato también se verifica.")
    return trampa(b, x0, yy + 14, ww, "Una opción promete que todo se arregla a la vez:",
                  "dice que la medida «resuelve al mismo tiempo» dos crisis. Revisa tu cascada: ¿algún salto "
                  "resolvió algo, o todos agravaron algo?", c)


# ───────── P3 · el este de Ucrania · mapa ─────────
def i3(b, x, y, w, h):
    c = VE
    yy = titulo_instr(b, x, y, "Pon en el mapa lo que hace valioso al este", c,
                      "El mapa está mudo a propósito. Escribe en él las tres características que el texto le da a la "
                      "región. Después sigue las dos flechas: una va hacia los que pelean, la otra hacia la gente.")
    x0, ww = x + 22, w - 44
    mw, mh = 760, 300
    # contorno esquemático: oeste a la izquierda, este a la derecha, Rusia más allá
    sy = 1.25
    base = [(20, 120), (120, 40), (330, 22), (520, 34), (640, 70), (mw - 40, 120), (mw - 30, 210), (600, 262),
            (420, 290), (220, 272), (60, 220), (20, 120)]
    pts = [(x0 + px, yy + 30 + (py - 20) * sy) for px, py in base]
    d = "M " + " L ".join(f"{px:.0f} {py:.0f}" for px, py in pts) + " Z"
    b.append(f'<path d="{d}" fill="{SOFT}" stroke="{c}" stroke-width="2.6"/>')
    b.append(f'<line x1="{x0 + 450}" y1="{yy + 40}" x2="{x0 + 450}" y2="{yy + 370}" stroke="{c}" '
             f'stroke-width="2" stroke-dasharray="6,6"/>')
    rot(b, x0 + 180, yy + 200, "OESTE", c, size=15)
    rot(b, x0 + 480, yy + 120, "EL ESTE", c, size=15)
    for k in range(3):
        cy_ = yy + 170 + k * 56
        b.append(f'<circle cx="{x0 + 490}" cy="{cy_}" r="14" fill="white" stroke="{c}" stroke-width="2.2"/>')
        b.append(T(x0 + 490, cy_ + 6, [str(k + 1)], 15, c, weight="700", anchor="middle"))
        renglon(b, x0 + 514, cy_ + 10, x0 + mw - 50)
    fx = x0 + mw + 20
    b.append(f'<line x1="{fx}" y1="{yy + 60}" x2="{fx}" y2="{yy + 380}" stroke="{GRAY}" '
             f'stroke-width="3" stroke-dasharray="3,7"/>')
    rot(b, fx, yy + 26, "FRONTERA", GRAY, size=13, anchor="middle")
    rot(b, fx, yy + 46, "CON RUSIA", GRAY, size=13, anchor="middle")
    pista(b, x0 + 20, yy + 420, "1, 2 y 3: las características que el texto le da a la región")
    # dos flechas de salida
    rx = x0 + mw + 70
    rw = ww - (mw + 70)
    for k, (rt, ps) in enumerate((("POR ESO LE INTERESA A…", "a quiénes y para qué"),
                                  ("POR ESO LA GENTE SUFRE…", "qué perdió la población"))):
        ry = yy + 70 + k * 170
        caja(b, rx, ry, rw, 146, c, r=14)
        rot(b, rx + 18, ry + 30, rt, c, size=14)
        pista(b, rx + 18, ry + 54, ps)
        renglon(b, rx + 18, ry + 94, rx + rw - 18)
        renglon(b, rx + 18, ry + 128, rx + rw - 18)
        b.append(hand_arrow(x0 + mw - 40, yy + 230, rx - 8, ry + 73, c, sw=2.6, bend=0.12 - 0.24 * k, head=13))
    mh = 410
    yy += mh + 34
    return ojo(b, x0, yy, ww, "LA CARACTERÍSTICA TIENE QUE ESTAR EN EL MAPA",
               "Cada opción nombra un rasgo del lugar. Antes de creerle, búscalo entre tus números 1, 2 y 3. Si el "
               "texto no se lo da a la región, esa opción explica otro lugar, no el este de Ucrania.")


# ───────── P4 · mina en Boyacá · prejuicio e intención ─────────
FRASES_4 = (("EL EMPRESARIO", "«quienes se oponen al proyecto son ignorantes que no entienden el progreso»"),
            ("LA LIDERESA AMBIENTAL", "«la minería solo enriquecerá a unos pocos y condenará a la comunidad a "
                                      "quedarse sin agua»"),
            ("EL ALCALDE", "«debemos escuchar todas las voces y garantizar que la decisión beneficie al "
                           "municipio»"))


def i4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La lupa sobre tres frases de la reunión", c,
                      "Lee cada frase con la lupa: ¿de quién habla, de las personas o del proyecto? Encierra la "
                      "palabra que más pesa. Después escribe qué busca quien la dijo.")
    x0, ww = x + 22, w - 44
    qw = 700
    for k, (quien, fr) in enumerate(FRASES_4):
        caja(b, x0, yy, ww, 150, c, r=14)
        b.append(rect(x0, yy, 8, 150, c, r=4))
        rot(b, x0 + 24, yy + 28, quien, c, size=14)
        parrafo(b, x0 + 24, yy + 38, qw - 40, fr, size=17, style="italic")
        bx = x0 + qw
        b.append(f'<line x1="{bx}" y1="{yy + 16}" x2="{bx}" y2="{yy + 134}" stroke="{c}" stroke-width="1.6" '
                 f'stroke-dasharray="4,6"/>')
        b.append(T(bx + 22, yy + 32, ["habla de:"], 15, GRAY))
        for j, lab in enumerate(("las personas", "el proyecto")):
            b.append(checkbox(bx + 106 + j * 160, yy + 16, s=10, c=c))
            b.append(T(bx + 134 + j * 160, yy + 32, [lab], 15, GRAY))
        b.append(T(bx + 22, yy + 76, ["busca:"], 15, GRAY))
        renglon(b, bx + 82, yy + 78, x0 + ww - 20)
        renglon(b, bx + 22, yy + 120, x0 + ww - 20)
        yy += 164
    yy += 2
    return ojo(b, x0, yy, ww, "DOS PALABRAS QUE NO SON LO MISMO",
               "Un prejuicio es un juicio sobre un grupo de personas sin haberlas oído. Una intención es lo que "
               "alguien quiere lograr con lo que dice. La pregunta te pide las dos cosas: revisa que la opción "
               "ponga cada una en la boca correcta.")


# ───────── P5 · Parque Nacional · lo social y lo político ─────────
def i5(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La madrugada en el parque, hora por hora", c,
                      "Ordena lo que pasó como si fuera una bitácora. En cada momento marca si lo que se movió fue "
                      "lo social (la gente, el espacio) o lo político (las decisiones de las instituciones).")
    x0, ww = x + 22, w - 44
    ly = yy + 30
    b.append(line(x0 + 40, ly, x0 + 40, ly + 4 * 104 - 30, c, 4))
    momentos = (("LA LLEGADA", "quiénes, cuántos, a dónde y para qué"),
                ("LO QUE SE VIO EN LA CIUDAD", "qué impacto menciona el texto"),
                ("LA RESPUESTA DE LAS AUTORIDADES", "qué recordaron y qué abrieron"),
                ("LO QUE HIZO LA COMUNIDAD", "qué exigió y a quién"))
    for k, (rt, ps) in enumerate(momentos):
        ry = ly + k * 104
        b.append(f'<circle cx="{x0 + 40}" cy="{ry + 10}" r="13" fill="white" stroke="{c}" stroke-width="3"/>')
        caja(b, x0 + 80, ry - 14, ww - 380, 86, c, r=12)
        rot(b, x0 + 100, ry + 14, rt, c, size=14)
        pista(b, x0 + 100 + tw(rt, 14, "700") + len(rt) * 1.5 + 16, ry + 14, ps)
        renglon(b, x0 + 100, ry + 54, x0 + ww - 320)
        for j, lab in enumerate(("social", "político")):
            b.append(checkbox(x0 + ww - 270, ry - 8 + j * 38, s=11, c=c))
            b.append(T(x0 + ww - 240, ry + 10 + j * 38, [lab], 16, GRAY))
    yy = ly + 4 * 104 - 4
    yy = frase_hueco(b, x0, yy, ww, "Lo social se volvió político en el momento en que ______________________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una opción promete una solución «inmediata»:",
                  "lee la última línea de tu bitácora. ¿El texto termina con algo resuelto o con exigencias "
                  "abiertas? Una opción que cierra lo que el texto deja abierto no explica la interacción: la "
                  "inventa.", c)


# ───────── P6 · Parque Nacional · el espacio ─────────
def i6(b, x, y, w, h):
    c = VE
    yy = titulo_instr(b, x, y, "La cédula del Parque Nacional", c,
                      "Todo lugar tiene su cédula: de quién es, dónde queda, para qué sirve. Llénala con lo que dice "
                      "el texto, no con lo que te imaginas del parque. La característica que buscas sale de aquí.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 380, c, sw=2.6, r=20)
    b.append(rect(x0, yy, ww, 56, _mezcla_local(c), r=20))
    b.append(rect(x0, yy + 30, ww, 26, _mezcla_local(c), r=0))
    rot(b, x0 + 28, yy + 36, "CÉDULA DEL LUGAR · PARQUE NACIONAL, BOGOTÁ", c, size=16)
    filas = (("¿DE QUIÉN ES?", ("público", "privado"), "la frase del texto que lo dice:"),
             ("¿DÓNDE QUEDA?", ("en la ciudad", "en el campo"), "qué parte de la ciudad:"),
             ("¿PARA QUÉ Y PARA QUIÉN?", ("para todos", "para unos pocos"), "qué se hace allí:"),
             ("¿QUÉ PERMITE LA NORMA?", ("asentarse", "no asentarse"), "quién lo recordó:"))
    lw = max(tw(f[0], 14, "700") + len(f[0]) * 1.5 for f in filas) + 40
    ry = yy + 76
    for rt, (o1, o2), ps in filas:
        rot(b, x0 + 28, ry + 26, rt, c, size=14)
        for j, lab in enumerate((o1, o2)):
            bx = x0 + 28 + lw + j * 190
            b.append(checkbox(bx, ry + 10, s=11, c=c))
            b.append(T(bx + 30, ry + 28, [lab], 16, GRAY))
        px = x0 + 28 + lw + 400
        pista(b, px, ry + 26, ps)
        renglon(b, px, ry + 58, x0 + ww - 28)
        ry += 74
    yy += 400
    return ojo(b, x0, yy, ww, "Palabras que encierran al lugar:",
               "una opción que le pone al parque una etiqueta cerrada («solo para esto», «solo de ellos») tiene "
               "que pasar por tu cédula antes de que le creas. Y fíjate en algo más: la pregunta pide una "
               "característica del espacio, no de la gente que llegó.")


def _mezcla_local(c):
    from taller_base import _mezcla
    return _mezcla(c, 0.90)


# ───────── P7 · Parque Nacional · las dos perspectivas ─────────
BANCO_7 = ("derecho", "ocupación", "diálogo", "desalojo", "reubicación", "vivienda", "no permitido",
           "retorno", "territorio indígena", "vida digna")


def i7(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "¿Quién diría cada palabra?", c,
                      "Cada actor nombra lo que pasa con sus propias palabras. Pon junto a cada palabra la letra "
                      "de quien la usaría según el texto: E (comunidad emberá), A (autoridades), las dos (EA) o "
                      "ninguna (X). Después busca la opción que respeta tu reparto.")
    x0, ww = x + 22, w - 44
    cols = 5
    cw = (ww - (cols - 1) * 18) / cols
    for k, pal in enumerate(BANCO_7):
        col, fila = k % cols, k // cols
        bx = x0 + col * (cw + 18)
        by = yy + fila * 82
        caja(b, bx, by, cw, 66, c, r=33)
        b.append(T(bx + 24, by + 40, [pal], 17, INK, weight="700"))
        b.append(rect(bx + cw - 66, by + 13, 52, 40, "white", r=8, stroke=c, sw=2))
    yy += 2 * 82 + 14
    half = (ww - 30) / 2
    for k, (quien, ps) in enumerate((("LA COMUNIDAD EMBERÁ", "con mis palabras, lo que ellos ven en el parque:"),
                                     ("LAS AUTORIDADES DISTRITALES", "con mis palabras, lo que ellas ven en el parque:"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 140, c, r=14)
        rot(b, bx + 20, yy + 30, quien, c)
        pista(b, bx + 20, yy + 56, ps)
        renglon(b, bx + 20, yy + 92, bx + half - 20)
        renglon(b, bx + 20, yy + 124, bx + half - 20)
    yy += 158
    return trampa(b, x0, yy, ww, "Las palabras que marcaste con X también enseñan:",
                  "si una opción pone en boca de alguien una palabra que nadie dice en el texto, o se la cambia "
                  "a otro actor, ya no cuenta su perspectiva: cuenta la de quien escribió la opción.", c)


# ───────── P8 · La Calera · ondas ─────────
def i8(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Las ondas que salen del pozo", c,
                      "Como una piedra en el agua: la extracción es el centro y cada onda llega más lejos. Escribe "
                      "en cada onda lo que pasa en esa dimensión según el texto. La respuesta tiene que tocar las "
                      "tres ondas sin contradecir ninguna.")
    x0, ww = x + 22, w - 44
    cx, cy = x0 + 300, yy + 236
    for k, r_ in enumerate((220, 156, 92)):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r_}" fill="{"white" if k else SOFT}" stroke="{c}" '
                 f'stroke-width="2.4" stroke-dasharray="{"" if k == 2 else "8,6"}"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="44" fill="{c}"/>')
    b.append(T(cx, cy - 2, ["el"], 15, "white", weight="700", anchor="middle"))
    b.append(T(cx, cy + 18, ["pozo"], 15, "white", weight="700", anchor="middle"))
    rot(b, cx, cy - 64, "1", c, size=16, anchor="middle")
    rot(b, cx, cy - 128, "2", c, size=16, anchor="middle")
    rot(b, cx, cy - 192, "3", c, size=16, anchor="middle")
    rx = x0 + 560
    rw = ww - 560
    ondas = (("ONDA 1 · LO AMBIENTAL", "qué le pasa al páramo y al agua"),
             ("ONDA 2 · LO SOCIAL", "qué teme la comunidad y qué ofrece la empresa"),
             ("ONDA 3 · LO POLÍTICO", "entre qué dos cosas tienen que decidir las autoridades"))
    for k, (rt, ps) in enumerate(ondas):
        ry = yy + 20 + k * 146
        caja(b, rx, ry, rw, 126, c, r=14)
        rot(b, rx + 20, ry + 30, rt, c)
        pista(b, rx + 20, ry + 56, ps)
        renglon(b, rx + 20, ry + 96, rx + rw - 20)
        r_, ang = (92, 156, 220)[k], math.radians((40, 8, -24)[k])
        b.append(hand_arrow(cx + r_ * math.cos(ang), cy - r_ * math.sin(ang), rx - 10, ry + 63, c, sw=2.4,
                            bend=0.06, head=12))
        b.append(f'<circle cx="{cx + r_ * math.cos(ang):.1f}" cy="{cy - r_ * math.sin(ang):.1f}" r="5" fill="{c}"/>')
    yy += 470
    return trampa(b, x0, yy, ww, "Una opción dice que la extracción «fortalece el ecosistema»:",
                  "ponla junto a tu onda 1. Si choca con lo que advierte la comunidad, no integra nada: borra una "
                  "onda. Pregúntale lo mismo a cada opción: ¿qué onda se queda en blanco?", c)


# ───────── P9 · Tapón del Darién · la ruta ─────────
def i9(b, x, y, w, h):
    c = VE
    yy = titulo_instr(b, x, y, "Camina el Darién parada por parada", c,
                      "La ruta va de Colombia a Panamá. En cada parada escribe qué pone el lugar en el camino y qué "
                      "le hace al migrante. Al final responde la otra mitad del texto: si es tan peligrosa, ¿por "
                      "qué la siguen usando?")
    x0, ww = x + 22, w - 44
    ly = yy + 64
    rot(b, x0, ly - 30, "COLOMBIA", c, size=14)
    rot(b, x0 + ww, ly - 30, "PANAMÁ", c, size=14, anchor="end")
    pts = []
    for i in range(41):
        t = i / 40
        pts.append((x0 + 20 + t * (ww - 40), ly + 18 * math.sin(t * math.pi * 3)))
    d = "M " + " L ".join(f"{px:.1f} {py:.1f}" for px, py in pts)
    b.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="3.4" stroke-dasharray="10,8"/>')
    n = 3
    pw = (ww - 2 * 30) / n
    for k in range(n):
        px = x0 + pw * k + pw / 2 + 30 * k
        b.append(f'<circle cx="{px}" cy="{ly}" r="20" fill="white" stroke="{c}" stroke-width="3"/>')
        b.append(T(px, ly + 7, [str(k + 1)], 18, c, weight="700", anchor="middle"))
        bx = x0 + k * (pw + 30)
        caja(b, bx, ly + 40, pw, 196, c, r=14)
        pista(b, bx + 18, ly + 70, "lo que pone el lugar:")
        renglon(b, bx + 18, ly + 110, bx + pw - 18)
        pista(b, bx + 18, ly + 150, "lo que le hace al migrante:")
        renglon(b, bx + 18, ly + 190, bx + pw - 18)
        renglon(b, bx + 18, ly + 222, bx + pw - 18)
    yy = ly + 256
    caja(b, x0, yy, ww, 96, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA OTRA MITAD", c)
    pista(b, x0 + 160, yy + 30, "aun así la siguen usando porque…")
    renglon(b, x0 + 20, yy + 74, x0 + ww - 20)
    yy += 112
    return ojo(b, x0, yy, ww, "Si no está en la ruta, no está en el texto:",
               "antes de aceptar una opción, busca en tus tres paradas lo que ella describe. Si lo que la "
               "opción pone en el camino no aparece en ninguna parada, está hablando de otra ruta.")


# ───────── P10 · HRW · cuatro actores ─────────
def i10(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Cuatro sillas en la misma mesa", c,
                      "Sintetizar es sentar a todos en la mesa sin cambiarle las palabras a nadie. Escribe en cada "
                      "silla lo que dice ese actor, en no más de seis palabras.")
    x0, ww = x + 22, w - 44
    cx, cy = x0 + ww / 2, yy + 200
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="190" ry="88" fill="{SOFT}" stroke="{c}" stroke-width="2.6"/>')
    rot(b, cx, cy - 4, "EL DESPLAZAMIENTO", c, size=14, anchor="middle")
    rot(b, cx, cy + 20, "EN CHOCÓ, CAUCA Y NARIÑO", c, size=13, anchor="middle")
    sw_, sh = 440, 112
    sillas = ((x0, yy, "LAS COMUNIDADES CAMPESINAS"), (x0 + ww - sw_, yy, "LAS AUTORIDADES LOCALES"),
              (x0, yy + 290, "EL GOBIERNO NACIONAL"), (x0 + ww - sw_, yy + 290, "LAS ORGANIZACIONES DE DD. HH."))
    for sx, sy, quien in sillas:
        caja(b, sx, sy, sw_, sh, c, r=18)
        rot(b, sx + 20, sy + 30, quien, c, size=14)
        renglon(b, sx + 20, sy + 70, sx + sw_ - 20)
        renglon(b, sx + 20, sy + 100, sx + sw_ - 20)
    yy += 290 + sh + 20
    b.append(T(x0, yy + 20, ["Sillas que la opción sienta sin cambiarle las palabras (0 a 4):"], 18, INK,
               weight="700"))
    yy += 34
    for k, L in enumerate("ABCD"):
        bx = x0 + k * 190
        letra(b, bx + 18, yy + 22, L, c)
        caja(b, bx + 48, yy, 70, 44, c)
    yy += 62
    return ojo(b, x0, yy, ww, "«COINCIDEN» ES UNA PALABRA QUE SE PRUEBA",
               "Si una opción dice que dos actores están de acuerdo, busca ese acuerdo en el texto. Y si dice "
               "que alguien «reconoce» o «exagera» algo, mira tu silla: ¿eso fue lo que escribiste?")


Q = {1: dict(n=1, est=2, pag=383, ctx="Barrismo · los «territorios invisibles» y tres actores",
             comp="Interpretación de perspectivas", inst=i1),
     2: dict(n=2, est=3, pag=383, ctx="Frontera con Venezuela · una medida y sus efectos",
             comp="Pensamiento reflexivo y sistémico", inst=i2),
     3: dict(n=3, est=1, pag=383, ctx="Guerra en Ucrania · por qué el este",
             comp="Pensamiento reflexivo y sistémico", inst=i3),
     4: dict(n=4, est=4, pag=384, ctx="Mina a cielo abierto en Boyacá · prejuicios e intenciones",
             comp="Interpretación de perspectivas", inst=i4),
     5: dict(n=5, est=3, pag=384, ctx="Emberá en el Parque Nacional · lo social y lo político",
             comp="Pensamiento reflexivo y sistémico", inst=i5),
     6: dict(n=6, est=1, pag=385, ctx="Emberá en el Parque Nacional · qué clase de espacio es",
             comp="Pensamiento social", inst=i6),
     7: dict(n=7, est=4, pag=385, ctx="Emberá en el Parque Nacional · cómo lo ve cada lado",
             comp="Interpretación de perspectivas", inst=i7),
     8: dict(n=8, est=3, pag=385, ctx="El agua de La Calera · ambiente, sociedad y política",
             comp="Pensamiento reflexivo y sistémico", inst=i8),
     9: dict(n=9, est=1, pag=385, ctx="Tapón del Darién · la geografía de una ruta",
             comp="Pensamiento reflexivo y sistémico", inst=i9),
     10: dict(n=10, est=2, pag=386, ctx="Informe de HRW · cuatro actores frente al desplazamiento",
              comp="Interpretación de perspectivas", inst=i10)}


def build(pages=(125, 126, 128, 129, 130)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"soc5_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
