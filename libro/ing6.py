#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 6 · Parte 7 del ICFES · componente gramatical · léxico · páginas 331–344.
Es la última misión del cuaderno: cierra el área de Inglés.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 6» de Inglés (fuente_libro/INGLÉS), páginas 468–470.
Textos con espacios, cuatro opciones cada uno: «An Unexpected Adventure» (Bloque 1, ocho espacios),
«Debating in Class» (Bloque 2, ocho) y «A Late Visitor», con Sherlock Holmes (Bloque 3, ocho).

Decisión de Nelson (7 nov): el cuaderno trabaja TODAS las preguntas del libro, una tarjeta por
pregunta. El libro numera 1 a 8 en cada bloque; el cuaderno numera 1 a 24 y cada tarjeta dice
«Bloque k, n.º j del libro». Dentro de la oración impresa se conserva el número del libro: (1)…(8).

Estrategia de la Parte 7 (cabecera): leer el texto entero antes de llenar el espacio. Recoge lo
trabajado en el área: el tiempo del verbo (M3, M6), la palabra que manda la forma (M3), las palabras
que van juntas (M1, M3) y el texto completo como prueba (M4, M5, y los conectores con que abre M6).

Claves verificadas (resueltas a mano, 7 nov 2026):

    cuaderno   libro       clave
     1         B1 n.º 1    B  went           pasado terminado: «Two years ago»
     2         B1 n.º 2    B  felt           (C «were feeling» también es correcta · Corrección EDUCATE)
     3         B1 n.º 3    C  were setting   acción larga interrumpida, sujeto «we» (falta «up» · Corrección EDUCATE)
     4         B1 n.º 4    A  began          «it suddenly ___ to snow», el relato va en pasado («surprised», «was»)
     5         B1 n.º 5    B  have been      «Since that day» llega hasta hoy
     6         B1 n.º 6    A  taken          have + participio
     7         B1 n.º 7    B  started        hecho puntual; sujeto «I» (lo natural sería «have started»: nota)
     8         B1 n.º 8    A  had            «had never imagined… would love»: antes del viaje
     9         B2 n.º 1    A  express        (D «explore» también es correcta · Corrección EDUCATE)
    10         B2 n.º 2    D  involve        el único verbo con sentido («involve subjects» es poco natural)
    11         B2 n.º 3    B  develop        «develop critical thinking»: meta positiva
    12         B2 n.º 4    A  check          lo contrario de «repeating information without analysis»
    13         B2 n.º 5    C  feel           «students» plural, presente habitual («Sometimes», «they become»)
    14         B2 n.º 6    B  use            el texto entero va en presente (C «used» es gramatical: Atención)
    15         B2 n.º 7    D  improves       sujeto «debating» = it
    16         B2 n.º 8    A  allow          allow + alguien + to + verbo (como «encourage students to», párrafo 1)
    17         B3 n.º 1    C  lit            (B «lighted» también es correcta · Corrección EDUCATE)
    18         B3 n.º 2    C  was broken     pasiva: el silencio lo rompen las ruedas («by»)
    19         B3 n.º 3    B  were           sujeto «my thoughts» (plural) + «wandering»
    20         B3 n.º 4    B  ran            hecho puntual en pasado («Suddenly») (los pasos no corren · Corrección EDUCATE)
    21         B3 n.º 5    C  took           «as»: al tiempo que «his hands trembled»
    22         B3 n.º 6    C  observing      la oración ya tiene su verbo («rose»), sin «and»
    23         B3 n.º 7    C  listened       ninguna queda bien: falta «to» (listened to) · Corrección EDUCATE
    24         B3 n.º 8    B  saw            el relato va en pasado

    En orden: 1·B 2·B 3·C 4·A 5·B 6·A 7·B 8·A 9·A 10·D 11·B 12·A 13·C 14·B 15·D 16·A
              17·C 18·C 19·B 20·B 21·C 22·C 23·C 24·B

Reparto de las 24: A 6 · B 9 · C 7 · D 2; el Bloque 3 no tiene ninguna A ni ninguna D (Atención en
tablero/propuestas/ing6_hallazgos.csv).

Subestrategias (las cuatro de la Parte 7):
    1 · La línea de tiempo del verbo          (1, 3, 4, 5, 8, 17, 20     · ICFES QA)   azul
    2 · La palabra de al lado manda la forma  (6, 13, 15, 18, 19         · ICFES QB)   rojo
    3 · Palabras que andan juntas             (9, 10, 11, 12, 16, 23     · ICFES QC)   oro
    4 · El párrafo entero decide              (2, 7, 14, 21, 22, 24      · ICFES QD)   morado

Hojas: 331–336 t1–t6 (1-12) · 337 ing6_i1 · 338–343 t7–t12 (13-24) · 344 ing6_i2.
"""
from taller_base import *

configurar("Inglés", 6, "gramatical · léxico",
           tema="Parte 7 · Leer todo el texto antes de llenar el espacio",
           nota="LO QUE SUBRAYÉ EN EL TEXTO", prefijo="Subestrategia", n_hojas=12)
MORADO = "#5B3E96"
EST = {1: ("La línea de tiempo del verbo", EDU_AZUL),
       2: ("La palabra de al lado manda la forma", EDU_ROJO),
       3: ("Palabras que andan juntas", EDU_ORO),
       4: ("El párrafo entero decide", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))


# ───────── piezas pequeñas (las usa también ing6_icfes.py) ─────────
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


def tinte(c, k=0.9):
    from taller_base import _mezcla
    return _mezcla(c, k)


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12, bend=0.0):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def sino(b, x, y, c, labels=("sí", "no"), gap=80):
    for j, lab in enumerate(labels):
        b.append(checkbox(x + j * gap, y, s=10, c=c))
        b.append(T(x + 28 + j * gap, y + 17, [lab], 16, GRAY))


def pista_linea(b, x, y, txt, x2, size=15):
    """Una pista y su renglón a continuación, medido con tw()."""
    pista(b, x, y, txt, size=size)
    renglon(b, x + tw(txt, size, style="italic") + 12, y + 4, x2)


def oracion(b, x, y, w, txt, c, rotulo="LA ORACIÓN DEL LIBRO", size=21):
    """La oración del libro con su espacio, en inglés, en un recuadro tinte con acento vertical."""
    svg, yy = TJ(x + 26, y + 38, txt, w - 52, size, INK, weight="700", style="italic", lh=size + 9)
    h = yy - y + 14
    caja(b, x, y, w, h, tinte(c, 0.86), fill=tinte(c, 0.95), r=12)
    b.append(rect(x, y, 7, h, c, r=3))
    rot(b, x + 26, y + 24, rotulo, c, size=13)
    b.append(svg)
    return y + h


def correccion(b, x, y, w, txt, escribe=None):
    """Recuadro «Corrección EDUCATE»: qué está mal en el libro y qué hacer, sin dar la clave.
    `escribe`: rótulo de un renglón para escribir la versión correcta."""
    c = A["color"]
    svg, yy = TJ(x + 30, y + 50, txt, w - 56, 18, INK, lh=26)
    if escribe:
        yy += 12
    h = yy - y + (58 if escribe else 14)
    b.append(rect(x, y, w, h, tinte(c, 0.93), r=14, stroke=c, sw=2.4))
    b.append(rect(x, y, 9, h, c, r=4))
    b.append(T(x + 30, y + 31, ["CORRECCIÓN EDUCATE"], 15, _mezcla_osc(c), weight="700", ls=1.5))
    b.append(svg)
    if escribe:
        pista_linea(b, x + 30, yy + 22, escribe, x + w - 24)
    return y + h


def _mezcla_osc(c):
    from taller_base import _mezcla
    return _mezcla(c, 0.35, "#000000")


def linea_tiempo(b, x, y, w, c, rotulos=("ANTES", "AHORA", "DESPUÉS"), xs=(0.12, 0.62, 0.92)):
    """Eje del tiempo con marcas. Devuelve la y del eje."""
    b.append(line(x, y, x + w, y, INK, 3))
    b.append(f'<polygon points="{x + w},{y} {x + w - 16},{y - 9} {x + w - 16},{y + 9}" fill="{INK}"/>')
    for r_, k in zip(rotulos, xs):
        px = x + w * k
        b.append(line(px, y - 12, px, y + 12, INK, 3))
        rot(b, px, y + 40, r_, c, size=13, anchor="middle")
    return y


def ficha(b, x, y, w, h, c, titulo_, lineas, fill="white", r=14):
    """Recuadro con rótulo y pistas con renglón (cada una: texto)."""
    caja(b, x, y, w, h, c, r=r, fill=fill)
    rot(b, x + 18, y + 30, titulo_, c, size=13)
    yy = y + 64
    for ps in lineas:
        pista_linea(b, x + 18, yy, ps, x + w - 18)
        yy += 44
    return y + h


# ═════════════════════════ BLOQUE 1 · An Unexpected Adventure ═════════════════════════

# ───────── 1 · B1 n.º 1 · «Two years ago» ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El marcador clava el verbo en el tiempo", c,
                      "Lee la oración entera antes de mirar las opciones: busca la palabra que dice cuándo pasó. "
                      "Clávala en la línea del tiempo y decide si esa acción ya terminó o sigue pasando.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "Two years ago, my family and I (1) ________ to the mountains for a weekend trip.", c)
    yy += 30
    ey = linea_tiempo(b, x0 + 20, yy + 40, ww - 40, c)
    pista(b, x0 + 20, ey - 22, "dibuja una X donde queda «two years ago»")
    yy = ey + 70
    half = (ww - 30) / 2
    caja(b, x0, yy, half, 200, c, r=14)
    rot(b, x0 + 18, yy + 30, "EL MARCADOR", c)
    pista(b, x0 + 18, yy + 64, "la palabra que dice cuándo:")
    renglon(b, x0 + 230, yy + 68, x0 + half - 18)
    pista(b, x0 + 18, yy + 108, "¿la acción ya terminó?")
    sino(b, x0 + 200, yy + 92, c)
    pista(b, x0 + 18, yy + 152, "¿llega hasta hoy?")
    sino(b, x0 + 200, yy + 136, c)
    bx = x0 + half + 30
    caja(b, bx, yy, half, 200, c, r=14)
    rot(b, bx + 18, yy + 30, "EL TIEMPO QUE VIVE AHÍ", c)
    pista(b, bx + 18, yy + 64, "nombre del tiempo verbal:")
    renglon(b, bx + 210, yy + 68, bx + half - 18)
    pista(b, bx + 18, yy + 108, "¿necesita auxiliar (am, have, did…)?")
    sino(b, bx + 290, yy + 92, c)
    pista(b, bx + 18, yy + 152, "un ejemplo mío con «last year»:")
    renglon(b, bx + 18, yy + 186, bx + half - 18)
    yy += 220
    return ojo(b, x0, yy, ww, "«AGO» CIERRA LA PUERTA",
               "«Ago» siempre mira hacia atrás desde hoy y deja la acción terminada allá. Con él no va el presente "
               "ni el presente perfecto: «I have gone two years ago» es un error que el ICFES conoce muy bien.")


# ───────── 2 · B1 n.º 2 · «we ___ tired when we finally arrived» ─────────
def i2(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El camino a la montaña, verbo por verbo", c,
                      "El párrafo entero decide: el primer párrafo cuenta un viaje y cada verbo es una parada del "
                      "camino. Escribe en cada señal el verbo que va ahí y su tiempo. El espacio 2 tiene que sonar "
                      "como las paradas que lo rodean.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "Two years ago, my family and I (1) ________ to the mountains for a weekend trip. The "
                                "road was long, and we (2) ________ tired when we finally arrived.", c,
                 rotulo="EL PRINCIPIO DEL RELATO", size=20)
    yy += 18
    rh = 250
    caja(b, x0, yy, ww, rh, c, r=16, fill=tinte(c, 0.97))
    mx = x0 + ww - 130
    for dx, s_ in ((0, 100), (-80, 70)):
        b.append(f'<polygon points="{mx + dx - s_},{yy + rh - 16} {mx + dx},{yy + rh - 16 - s_ * 1.5} '
                 f'{mx + dx + s_},{yy + rh - 16}" fill="{tinte(c, 0.8)}" stroke="{c}" stroke-width="2"/>')
    ry_ = yy + rh - 40
    d = (f"M {x0 + 20} {ry_} Q {x0 + 250} {ry_ - 30} {x0 + 480} {ry_} "
         f"Q {x0 + 710} {ry_ + 26} {mx - 150} {ry_ - 6}")
    b.append(f'<path d="{d}" fill="none" stroke="#C9CED6" stroke-width="22" stroke-linecap="round"/>')
    b.append(f'<path d="{d}" fill="none" stroke="white" stroke-width="3" stroke-dasharray="14,12"/>')
    paradas = ("Two years ago, my family and I…", "The road…", "and we (2)…", "when we finally…")
    pw = 214
    for k, t in enumerate(paradas):
        px, py = x0 + 20 + k * (pw + 18), yy + 18
        b.append(line(px + 40, py + 140, px + 40, ry_ - 4, "#8A6A4A", 4))
        caja(b, px, py, pw, 140, c, r=10, fill=tinte(c, 0.93) if k == 2 else "white")
        rot(b, px + 14, py + 26, f"PARADA {k + 1}", c, size=12)
        texto(b, px + 14, py + 52, t if tw(t, 15, "700", "italic") < pw - 24 else "Two years ago…", size=15,
              style="italic", weight="700")
        pista_linea(b, px + 14, py + 88, "verbo:", px + pw - 14, size=14)
        pista_linea(b, px + 14, py + 124, "tiempo:", px + pw - 14, size=14)
    pista(b, mx - 20, yy + 30, "la montaña", anchor="middle")
    yy += rh + 18
    caja(b, x0, yy, ww, 78, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "LO QUE DICEN LAS PARADAS", c)
    pista_linea(b, x0 + 20, yy + 60, "las que ya trae el libro («was», «arrived») van en este tiempo:", x0 + ww - 20)
    yy += 94
    return correccion(b, x0, yy, ww,
                      "En esta pregunta el libro espera una sola respuesta, pero en inglés hay dos opciones correctas. "
                      "Encuéntralas, márcalas las dos y escribe en qué cambia lo que cuenta cada una.",
                      escribe="la diferencia, en mis palabras:")


# ───────── 3 · B1 n.º 3 · «While we ___ our tent» ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Una acción larga, un golpe que la corta", c,
                      "En esta oración pasan dos cosas al tiempo. Dibuja la que dura como una barra y la que llega de "
                      "repente como un rayo. La palabra «while» te dice cuál es cuál.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "While we (3) ________ our tent, it suddenly (4) ________ to snow, which surprised everyone.", c)
    yy += 24
    gx, gw = x0 + 20, ww - 40
    caja(b, x0, yy, ww, 230, c, r=14)
    ey = yy + 150
    b.append(line(gx + 20, ey, gx + gw - 20, ey, INK, 2.4))
    b.append(rect(gx + 140, ey - 64, 560, 34, tinte(c, 0.85), r=6, stroke=c, sw=2, dash="7,5"))
    pista(b, gx + 150, ey - 76, "la acción que dura (escríbela adentro)")
    bx = gx + 470
    b.append(f'<polygon points="{bx},{ey - 120} {bx - 22},{ey - 40} {bx - 4},{ey - 44} {bx - 20},{ey + 6} '
             f'{bx + 22},{ey - 70} {bx + 4},{ey - 66} {bx + 18},{ey - 120}" fill="white" stroke="{RO}" '
             f'stroke-width="2.2"/>')
    pista(b, bx + 36, ey - 100, "la que llega de repente:")
    renglon(b, bx + 36, ey - 60, gx + gw - 20)
    rot(b, gx + 20, ey + 34, "ANTES", c, size=13)
    rot(b, gx + gw - 20, ey + 34, "DESPUÉS", c, size=13, anchor="end")
    pista(b, gx + 20, ey + 64, "marca en la línea el momento exacto en que empezó la nieve")
    yy += 250
    half = (ww - 30) / 2
    ficha(b, x0, yy, half, 120, c, "LA ACCIÓN LARGA", ("¿quién la hace?", "la fórmula (auxiliar + verbo):"))
    caja(b, x0 + half + 30, yy, half, 120, c, r=14)
    rot(b, x0 + half + 48, yy + 30, "EL AUXILIAR", c, size=13)
    pista(b, x0 + half + 48, yy + 64, "concuerda con el sujeto y va en el tiempo del relato:")
    sino(b, x0 + half + 48, yy + 82, c, labels=("lo comprobé", "todavía no"), gap=170)
    yy += 138
    return correccion(b, x0, yy, ww,
                      "Una carpa en inglés se arma con dos palabras: «set up a tent». Al libro le falta «up» después del "
                      "espacio. Escoge la forma de «set» que va y, cuando copies la oración, agrégale el «up».",
                      escribe="la oración completa, como debe ir:")


# ───────── 4 · B1 n.º 4 · «it suddenly ___ to snow» ─────────
def copo(b, cx, cy, r, c):
    import math as _m
    for k in range(3):
        a = _m.pi * k / 3
        b.append(line(cx - r * _m.cos(a), cy - r * _m.sin(a), cx + r * _m.cos(a), cy + r * _m.sin(a), c, 2.4))
    for k in range(6):
        a = _m.pi * k / 3
        px, py = cx + r * 0.62 * _m.cos(a), cy + r * 0.62 * _m.sin(a)
        b.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="3" fill="{c}"/>')


def i4(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Los verbos vecinos confirman la nieve", c,
                      "La línea de tiempo del verbo también se lee a los lados del espacio. Después del espacio 4 la "
                      "oración sigue y trae más verbos: cópialos en los copos, escribe su tiempo y decide si el espacio "
                      "va en el mismo.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "While we (3) ________ our tent, it suddenly (4) ________ to snow, which surprised "
                                "everyone because it was spring.", c)
    yy += 22
    n = 3
    cw = (ww - 40) / n
    for k, t in enumerate(("el verbo de «which…»", "el verbo de «because it…»", "el espacio 4")):
        bx = x0 + k * (cw + 20)
        caja(b, bx, yy, cw, 230, c, r=16, fill=tinte(c, 0.96) if k == 2 else "white")
        copo(b, bx + 56, yy + 62, 34, c)
        texto(b, bx + 108, yy + 56, t, size=16, style="italic", weight="700", color=c)
        pista_linea(b, bx + 18, yy + 136, "el verbo:", bx + cw - 18)
        pista_linea(b, bx + 18, yy + 186, "su tiempo:", bx + cw - 18)
    yy += 250
    caja(b, x0, yy, ww, 160, c, r=14)
    rot(b, x0 + 20, yy + 30, "«SUDDENLY» = DE REPENTE", c)
    pista(b, x0 + 20, yy + 64, "la nieve empezó…")
    sino(b, x0 + 160, yy + 48, c, labels=("en un instante", "poco a poco, durante un rato"), gap=200)
    pista(b, x0 + 20, yy + 106, "¿la forma que escogí puede ir sola después de «it», sin otro auxiliar?")
    sino(b, x0 + 560, yy + 90, c)
    pista(b, x0 + 20, yy + 144, "(prueba cada opción en voz baja: «it suddenly ___ to snow»)", size=14)
    yy += 178
    return ojo(b, x0, yy, ww, "«IT» + VERBO: EL CLIMA EN INGLÉS",
               "Para hablar del clima el inglés usa «it» como sujeto: «it rains», «it was cold». «It» es un sujeto de "
               "verdad: el verbo va conjugado, concuerda con él y lleva el tiempo del relato.")


# ───────── 5 · B1 n.º 5 · «Since that day» ─────────
def i5(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "«Since» tiende un puente hasta hoy", c,
                      "Hay marcadores que cierran la acción en el pasado y otros que la traen hasta el presente. "
                      "Dibuja el puente desde «that day» hasta hoy y contesta si el narrador todavía siente lo mismo.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "Since that day, I (5) ________ fascinated by nature and camping. I have already (6) "
                                "________ many photographs of our trips…", c)
    yy += 24
    caja(b, x0, yy, ww, 250, c, r=14)
    ax, aw = x0 + 40, ww - 80
    ey = yy + 190
    b.append(line(ax, ey, ax + aw, ey, INK, 2.6))
    p1, p2 = ax + aw * 0.18, ax + aw * 0.80
    for px, lab in ((p1, "THAT DAY (el viaje)"), (p2, "HOY (cuando escribe)")):
        b.append(line(px, ey - 12, px, ey + 12, INK, 3))
        rot(b, px, ey + 36, lab, c, size=13, anchor="middle")
    b.append(f'<path d="M {p1} {ey - 14} Q {(p1 + p2) / 2} {ey - 190} {p2} {ey - 14}" fill="none" '
             f'stroke="{c}" stroke-width="2.4" stroke-dasharray="10,7"/>')
    pista(b, (p1 + p2) / 2, ey - 112, "repasa el puente con lápiz si la fascinación sigue hasta hoy", anchor="middle")
    yy += 270
    half = (ww - 30) / 2
    for k, (tit, ej) in enumerate((("MARCADOR QUE CIERRA", "Two years ago…"), ("MARCADOR QUE LLEGA HASTA HOY", "Since that day…"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 190, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        texto(b, bx + 18, yy + 64, ej, size=18, style="italic", weight="700")
        pista(b, bx + 18, yy + 100, "tiempo verbal que pide:")
        renglon(b, bx + 200, yy + 104, bx + half - 18)
        pista(b, bx + 18, yy + 144, "otro marcador de la misma familia:")
        renglon(b, bx + 260, yy + 148, bx + half - 18)
    yy += 208
    return ojo(b, x0, yy, ww, "LA ORACIÓN DE AL LADO TE CONFIRMA",
               "Justo después el narrador escribe «I have already…». Cuando una oración vecina usa un tiempo, el "
               "texto te está mostrando desde qué momento cuenta. Úsala para comprobar, no para copiar.")


# ───────── 6 · B1 n.º 6 · «I have already ___» ─────────
def i6(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Cada auxiliar llega con su pareja", c,
                      "En inglés el auxiliar decide la forma del verbo que lo sigue. Completa la tabla de parejas, "
                      "busca el auxiliar que manda en el espacio 6 y escribe las tres formas de «take».")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "I have already (6) ________ many photographs of our trips, and I (7) ________ a blog "
                                "to share them with friends.", c)
    yy += 22
    parejas = (("I have / she has + …", "forma:", "ejemplo con «eat»:"),
               ("I am / we were + …", "forma:", "ejemplo con «eat»:"),
               ("I did not / will + …", "forma:", "ejemplo con «eat»:"))
    pw = (ww - 40) / 3
    for k, (aux, f1, f2) in enumerate(parejas):
        bx = x0 + k * (pw + 20)
        caja(b, bx, yy, pw, 160, c, r=14)
        texto(b, bx + 18, yy + 36, aux, size=18, weight="700", style="italic")
        pista(b, bx + 18, yy + 76, f1)
        renglon(b, bx + 80, yy + 80, bx + pw - 18)
        pista(b, bx + 18, yy + 124, f2)
        renglon(b, bx + 150, yy + 128, bx + pw - 18)
    yy += 180
    caja(b, x0, yy, ww, 130, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL AUXILIAR DEL ESPACIO 6", c)
    pista(b, x0 + 20, yy + 66, "la palabra que manda:")
    renglon(b, x0 + 200, yy + 70, x0 + ww / 2 - 20)
    pista(b, x0 + ww / 2, yy + 66, "¿«already» cambia la forma?")
    sino(b, x0 + ww / 2 + 220, yy + 50, c)
    pista(b, x0 + 20, yy + 110, "¿qué palabra quedó entre el auxiliar y el espacio?", size=14)
    renglon(b, x0 + 370, yy + 112, x0 + ww / 2 - 20)
    yy += 150
    cw = (ww - 60) / 4
    for k, lab in enumerate(("BASE", "PASADO", "PARTICIPIO", "-ING")):
        bx = x0 + k * (cw + 20)
        caja(b, bx, yy, cw, 96, c, r=12, fill=tinte(c, 0.95))
        rot(b, bx + cw / 2, yy + 28, lab, c, size=13, anchor="middle")
        renglon(b, bx + 20, yy + 76, bx + cw - 20)
    pista(b, x0, yy + 124, "las formas de «take», una en cada casilla; luego encierra la que pide el auxiliar")
    return yy + 130


# ───────── 7 · B1 n.º 7 · «and I ___ a blog» ─────────
def i7(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La fecha de nacimiento del blog", c,
                      "El párrafo entero decide: el segundo párrafo cuenta lo que el viaje dejó hasta hoy. Antes de "
                      "escoger, copia los verbos de las oraciones vecinas y piensa qué clase de hecho es abrir un blog.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "I have already (6) ________ many photographs of our trips, and I (7) ________ a blog to "
                                "share them with friends.", c, size=20)
    yy += 20
    # pantalla del blog
    pw, ph = 520, 330
    caja(b, x0, yy, pw, ph, INK, r=18, sw=2.4, fill="#F4F6FA")
    b.append(rect(x0 + 16, yy + 16, pw - 32, ph - 52, "white", r=8, stroke="#C9CED6", sw=1.6))
    b.append(rect(x0 + 16, yy + 16, pw - 32, 50, tinte(c, 0.88), r=8))
    texto(b, x0 + 36, yy + 48, "MY OUTDOOR BLOG", size=17, weight="700", color=c)
    pista_linea(b, x0 + 36, yy + 104, "lo abrí el día:", x0 + pw - 36)
    pista(b, x0 + 36, yy + 146, "abrir un blog es algo que…")
    for j, lab in enumerate(("pasa una vez y queda hecho", "pasa todos los días", "estaba pasando cuando…")):
        b.append(checkbox(x0 + 36, yy + 164 + j * 36, s=10, c=c))
        texto(b, x0 + 64, yy + 181 + j * 36, lab, size=15, color=GRAY)
    b.append(f'<circle cx="{x0 + pw / 2}" cy="{yy + ph - 18}" r="8" fill="none" stroke="{INK}" stroke-width="2"/>')
    rx = x0 + pw + 30
    rw = ww - pw - 30
    caja(b, rx, yy, rw, ph, c, r=14)
    rot(b, rx + 18, yy + 30, "LOS VECINOS DEL PÁRRAFO 2", c, size=13)
    for j, ps in enumerate(("Since that day, I (5)…", "I have already (6)…", "Honestly, I (8)…")):
        texto(b, rx + 18, yy + 72 + j * 72, ps, size=16, style="italic", weight="700")
        pista_linea(b, rx + 18, yy + 104 + j * 72, "tiempo:", rx + rw - 18, size=14)
    pista_linea(b, rx + 18, yy + 300, "el sujeto del espacio 7:", rx + rw - 18)
    yy += ph + 20
    return ojo(b, x0, yy, ww, "DOS MITADES, DOS CLASES DE HECHO",
               "La primera mitad va con «have + participio». La segunda puede ir en el mismo tiempo o en otro: lo "
               "decide la clase de hecho que cuenta, no la costumbre de repetir el tiempo de al lado. Revisa tus "
               "casillas del blog y el sujeto antes de marcar.")


# ───────── 8 · B1 n.º 8 · «Honestly, I ___ never imagined» ─────────
def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Antes del viaje, yo no lo sabía", c,
                      "La línea de tiempo del verbo: esta oración se mueve entre dos pasados y un futuro visto desde "
                      "atrás. Ubica en la línea cuándo no lo imaginaba y cuándo descubrió que le encantaba.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "Honestly, I (8) ________ never imagined how much I would love outdoor adventures.", c)
    yy += 30
    ey = linea_tiempo(b, x0 + 20, yy + 60, ww - 40, c, rotulos=("ANTES DEL VIAJE", "EL VIAJE (two years ago)", "HOY"),
                      xs=(0.14, 0.5, 0.9))
    for k, xs_ in enumerate((0.14, 0.5)):
        b.append(f'<circle cx="{x0 + 20 + (ww - 40) * xs_:.1f}" cy="{ey - 36}" r="16" fill="white" '
                 f'stroke="{c}" stroke-width="2" stroke-dasharray="5,4"/>')
    pista(b, x0 + 20, ey - 64, "escribe 1 donde «no lo imaginaba» y 2 donde empezó a amar la aventura")
    yy = ey + 74
    half = (ww - 30) / 2
    ficha(b, x0, yy, half, 160, c, "«NEVER IMAGINED»", ("¿cuándo no lo imaginaba?", "¿eso pasó antes de otro pasado?"))
    ficha(b, x0 + half + 30, yy, half, 160, c, "«WOULD LOVE»", ("mira hacia adelante desde:", "¿cuándo descubrió que le encanta?"))
    yy += 178
    caja(b, x0, yy, ww, 104, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "LA FORMA DE «IMAGINED»", c)
    pista(b, x0 + 20, yy + 64, "después del espacio viene «never imagined»: con un auxiliar delante, «imagined» es…")
    sino(b, x0 + 20, yy + 74, c, labels=("pasado simple", "participio"), gap=170)
    yy += 122
    return alto_profe(b, x0, yy, ww,
                      "«Would» después de un relato en pasado es el futuro visto desde el pasado. Y una acción que "
                      "ocurre antes de otra que ya pasó es «el pasado de un pasado». Pídele al profe dos ejemplos y "
                      "cómo se arma ese tiempo en inglés.")


# ═════════════════════════ BLOQUE 2 · Debating in Class ═════════════════════════

# ───────── 9 · B2 n.º 1 · «students ___ different points of view» ─────────
def i9(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La telaraña de «points of view»", c,
                      "Palabras que andan juntas: antes de mirar las opciones, escribe en cada hilo un verbo, en "
                      "español o en inglés, que se use con «un punto de vista». Después busca cuáles de las opciones "
                      "caben en tu telaraña.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "In these activities, students (1) ________ different points of view about a topic.", c)
    yy += 20
    cx, cy = x0 + ww / 2, yy + 140
    import math as _m
    for k in range(8):
        a = _m.pi * 2 * k / 8 + _m.pi / 8
        ex, ey = cx + 470 * _m.cos(a), cy + 112 * _m.sin(a)
        b.append(line(cx + 160 * _m.cos(a), cy + 56 * _m.sin(a), ex, ey, tinte(c, 0.5), 1.8))
        caja(b, ex - 90, ey - 22, 180, 44, c, r=22)
    for rr in (0.45, 0.75):
        pts = " ".join(f"{cx + 470 * rr * _m.cos(_m.pi * 2 * k / 8 + _m.pi / 8):.1f},"
                       f"{cy + 112 * rr * _m.sin(_m.pi * 2 * k / 8 + _m.pi / 8):.1f}" for k in range(9))
        b.append(f'<polyline points="{pts}" fill="none" stroke="{tinte(c, 0.7)}" stroke-width="1.4"/>')
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="160" ry="56" fill="{tinte(c, 0.9)}" stroke="{c}" stroke-width="2.4"/>')
    texto(b, cx, cy + 8, "points of view", size=21, weight="700", style="italic", anchor="middle")
    yy = cy + 150
    caja(b, x0, yy, ww, 106, c, r=14)
    rot(b, x0 + 20, yy + 30, "EN UN DEBATE", c)
    pista_linea(b, x0 + 20, yy + 66, "lo que hacen los estudiantes con un punto de vista, en mis palabras:", x0 + ww - 20)
    yy += 124
    return correccion(b, x0, yy, ww,
                      "El libro espera una sola respuesta, pero en esta oración dos opciones son correctas y naturales en "
                      "inglés. Encuéntralas, márcalas las dos y escribe qué hacen los estudiantes con cada una.",
                      escribe="con una… / con la otra…")


# ───────── 10 · B2 n.º 2 · «Some debates ___ subjects» ─────────
def i10(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Pon cada verbo en la oración y escucha si suena", c,
                      "Aquí las cuatro opciones tienen la misma forma: la gramática no decide, decide el sentido. "
                      "Escribe qué quiere decir cada verbo y lee la oración completa con él.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "In these activities, students (1) ________ different points of view about a topic. Some "
                                "debates (2) ________ subjects like climate change, technology, or social justice.", c)
    yy += 22
    cols = (110, 360, ww - 110 - 360 - 230, 230)
    caja(b, x0, yy, ww, 46, c, fill=tinte(c), r=8)
    for k, hd in enumerate(("", "QUÉ QUIERE DECIR EL VERBO", "«SOME DEBATES ___ SUBJECTS» QUIERE DECIR…", "¿TIENE SENTIDO?")):
        rot(b, x0 + sum(cols[:k]) + 14, yy + 29, hd, c, size=13)
    ry = yy + 46
    for L in "ABCD":
        caja(b, x0, ry, ww, 76, c, r=0)
        b.append(f'<circle cx="{x0 + 40}" cy="{ry + 38}" r="17" fill="white" stroke="{c}" stroke-width="2"/>')
        texto(b, x0 + 40, ry + 44, L, size=16, color=c, weight="700", anchor="middle")
        renglon(b, x0 + cols[0] + 14, ry + 58, x0 + cols[0] + cols[1] - 14)
        renglon(b, x0 + cols[0] + cols[1] + 14, ry + 58, x0 + ww - cols[3] - 14)
        sino(b, x0 + ww - cols[3] + 30, ry + 26, c)
        ry += 76
    cx = x0
    for k in range(3):
        cx += cols[k]
        b.append(line(cx, yy, cx, ry, c, 1.6))
    yy = ry + 20
    return ojo(b, x0, yy, ww, "LOS EJEMPLOS DEL TEXTO SON LA PRUEBA",
               "Después del espacio vienen «climate change, technology, or social justice». Pregúntate qué hace un "
               "debate con esos temas. El verbo correcto es el que convierte la oración en una descripción de lo que "
               "pasa en un debate de verdad.")


# ───────── 11 · B2 n.º 3 · «to ___ critical thinking» ─────────
def i11(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El ascensor de «critical thinking»", c,
                      "Palabras que andan juntas: «critical thinking» va con verbos que lo hacen crecer o lo hacen "
                      "pequeño. Escribe la letra de cada opción en el piso al que lleva el pensamiento crítico y mira "
                      "qué piso pide la palabra «goal».")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "The main goal is to (3) ________ critical thinking and help students learn how to defend "
                                "their opinions with respect.", c)
    yy += 22
    sw_, sh = 380, 390
    caja(b, x0, yy, sw_, sh, c, r=12, sw=2.6, fill=tinte(c, 0.97))
    pisos = ("CRECE", "SE QUEDA IGUAL", "SE ACHICA", "DESAPARECE")
    fh = (sh - 20) / 4
    for k, p in enumerate(pisos):
        fy = yy + 10 + k * fh
        b.append(rect(x0 + 12, fy, sw_ - 24, fh - 10, "white", r=8, stroke=tinte(c, 0.6), sw=1.6))
        rot(b, x0 + 30, fy + 30, p, c, size=13)
        for j in range(4):
            b.append(rect(x0 + 30 + j * 60, fy + 42, 44, 36, "white", r=6, stroke=c, sw=1.6, dash="4,3"))
    flecha(b, x0 + sw_ - 40, yy + sh - 40, x0 + sw_ - 40, yy + 40, c, sw=3, head=14)
    rx, rw = x0 + sw_ + 30, ww - sw_ - 30
    caja(b, rx, yy, rw, 180, c, r=14)
    rot(b, rx + 18, yy + 30, "LAS PALABRAS QUE DICEN EL PISO", c, size=13)
    pista(b, rx + 18, yy + 64, "«the main goal» y «help students» hablan de…")
    sino(b, rx + 18, yy + 80, c, labels=("algo bueno que se busca", "algo malo que se evita"), gap=230)
    pista_linea(b, rx + 18, yy + 150, "la meta de un debate, en mis palabras:", rx + rw - 18)
    caja(b, rx, yy + 200, rw, 190, c, r=14, dash="8,6")
    rot(b, rx + 18, yy + 230, "EN ESPAÑOL TAMBIÉN ANDAN JUNTAS", c, size=13)
    pista(b, rx + 18, yy + 264, "¿qué verbo usas tú con «el pensamiento crítico»?")
    texto(b, rx + 18, yy + 312, "«___________ el pensamiento crítico»", size=18, style="italic", weight="700")
    pista_linea(b, rx + 18, yy + 360, "¿cuál opción dice lo mismo?", rx + rw - 18)
    return yy + sh


# ───────── 12 · B2 n.º 4 · «___ evidence before speaking» ─────────
def i12(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "«Instead of» te da el contrario", c,
                      "La misma oración trae lo que NO deben hacer los estudiantes. Lo que va en el espacio es lo "
                      "opuesto. Llena los dos recuadros y luego busca qué verbos se juntan de verdad con «evidence».")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "A debate also teaches them to (4) ________ evidence before speaking, instead of "
                                "repeating information without analysis.", c)
    yy += 24
    half = (ww - 110) / 2
    for k, (tit, ps) in enumerate((("LO QUE NO DEBEN HACER", "copia en inglés lo que viene después de «instead of»:"),
                                   ("LO QUE SÍ DEBEN HACER", "su contrario, en mis palabras:"))):
        bx = x0 + k * (half + 110)
        caja(b, bx, yy, half, 190, c, r=14, sw=2.4, dash="8,6" if k == 0 else None)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        pista(b, bx + 18, yy + 64, ps)
        renglon(b, bx + 18, yy + 108, bx + half - 18)
        renglon(b, bx + 18, yy + 152, bx + half - 18)
    texto(b, x0 + half + 55, yy + 108, "≠", size=46, color=c, weight="700", anchor="middle")
    yy += 210
    caja(b, x0, yy, ww, 196, c, r=14)
    rot(b, x0 + 20, yy + 30, "VERBO + EVIDENCE: ¿QUÉ SE HACE CON UNA PRUEBA?", c)
    pista(b, x0 + 20, yy + 64, "escribe tres verbos (en inglés o en español) que sí se usan con «evidence» o «una prueba»:")
    tw3 = (ww - 80) / 3
    for k in range(3):
        bx = x0 + 20 + k * (tw3 + 20)
        caja(b, bx, yy + 84, tw3, 56, c, r=28)
        texto(b, bx + tw3 - 24, yy + 120, "+ evidence", size=16, color=GRAY, style="italic", anchor="end")
    pista(b, x0 + 20, yy + 176, "¿cuál de las opciones del libro está en tu lista o se parece a uno de tus verbos?")
    yy += 214
    return ojo(b, x0, yy, ww, "BEFORE SPEAKING = ANTES DE HABLAR",
               "El orden también ayuda: primero se hace algo con la evidencia y después se habla. Un buen debatiente "
               "no habla a ciegas.")


# ───────── 13 · B2 n.º 5 · «Sometimes, students ___ nervous» ─────────
def i13(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El espejo de la misma oración", c,
                      "La palabra de al lado manda la forma, y a veces la misma oración trae el modelo. La segunda "
                      "mitad repite la estructura de la primera: une con una línea cada pieza con la que hace su "
                      "mismo papel al otro lado del espejo.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "Sometimes, students (5) ________ nervous when they have to speak in front of others, "
                                "but with practice they become more confident.", c, size=20)
    yy += 42
    half = (ww - 80) / 2
    izq = ("Sometimes,", "students", "(5) ________", "nervous")
    der = ("they", "more confident", "with practice", "become")
    ph = 64
    for k, (a, d) in enumerate(zip(izq, der)):
        py = yy + k * (ph + 14)
        caja(b, x0, py, half - 40, ph, c, r=12, fill=tinte(c, 0.95) if "____" in a else "white")
        texto(b, x0 + (half - 40) / 2, py + 40, a, size=19, weight="700", style="italic", anchor="middle")
        b.append(f'<circle cx="{x0 + half - 22}" cy="{py + ph / 2}" r="6" fill="{c}"/>')
        caja(b, x0 + half + 120, py, half - 40, ph, c, r=12)
        texto(b, x0 + half + 120 + (half - 40) / 2, py + 40, d, size=19, weight="700", style="italic", anchor="middle")
        b.append(f'<circle cx="{x0 + half + 102}" cy="{py + ph / 2}" r="6" fill="{c}"/>')
    mx = x0 + half + 40
    b.append(line(mx, yy - 6, mx, yy + 4 * (ph + 14) - 8, tinte(c, 0.4), 4, dash="10,8"))
    rot(b, x0 + half / 2 - 20, yy - 10, "LA PRIMERA MITAD", c, size=12, anchor="middle")
    rot(b, x0 + half + 100 + half / 2, yy - 10, "LA SEGUNDA MITAD", c, size=12, anchor="middle")
    pista(b, x0, yy + 4 * (ph + 14) + 12, "(el orden no es el mismo a los dos lados: une por el papel que hace cada pieza)")
    yy += 4 * (ph + 14) + 26
    half2 = (ww - 30) / 2
    ficha(b, x0, yy, half2, 120, c, "EL SUJETO", ("«they» reemplaza a:", "¿uno o varios?"))
    ficha(b, x0 + half2 + 30, yy, half2, 120, c, "EL VERBO DEL ESPEJO", ("¿«become» lleva -s? ¿por qué?", "¿«sometimes» = una vez o muchas?"))
    yy += 138
    return ojo(b, x0, yy, ww, "VERBO + ADJETIVO: CÓMO SE SIENTE ALGUIEN",
               "Para decir cómo está alguien, el inglés pone un verbo y después el adjetivo: «they become confident», "
               "«you look tired». El adjetivo no cambia; el verbo concuerda con el sujeto y lleva el tiempo del texto.")


# ───────── 14 · B2 n.º 6 · «Teachers ___ debates» ─────────
def nota_adhesiva(b, x, y, w, h, c):
    b.append(f'<polygon points="{x},{y} {x + w},{y} {x + w},{y + h - 30} {x + w - 30},{y + h} {x},{y + h}" '
             f'fill="#FFF6C9" stroke="#E0C860" stroke-width="1.6"/>')
    b.append(f'<polygon points="{x + w},{y + h - 30} {x + w - 30},{y + h - 30} {x + w - 30},{y + h}" '
             f'fill="#F0DD8A" stroke="#E0C860" stroke-width="1.2"/>')


def i14(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Notas adhesivas: el tiempo de cada párrafo", c,
                      "El párrafo entero decide, y aquí el texto entero. Pega una nota en cada párrafo de «Debating in "
                      "Class»: copia un verbo conjugado que no esté en un espacio y escribe su tiempo. Después mira en "
                      "qué tiempo habla el texto.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "Teachers (6) ________ debates as a way to make classes more dynamic and interactive.", c)
    yy += 22
    n = 4
    gap = 22
    nw, nh = (ww - gap * (n - 1)) / n, 230
    for k, t in enumerate(("Many schools…", "The main goal is…", "…they become…", "In the end…")):
        nx = x0 + k * (nw + gap)
        nota_adhesiva(b, nx, yy, nw, nh, c)
        rot(b, nx + 16, yy + 30, f"PÁRRAFO {k + 1}", c, size=13)
        texto(b, nx + 16, yy + 58, t, size=16, style="italic", weight="700")
        pista(b, nx + 16, yy + 96, "el verbo:", size=14)
        b.append(line(nx + 16, yy + 132, nx + nw - 16, yy + 132, "#D9C77A", 2))
        pista(b, nx + 16, yy + 170, "su tiempo:", size=14)
        b.append(line(nx + 16, yy + 204, nx + nw - 46, yy + 204, "#D9C77A", 2))
    yy += nh + 22
    caja(b, x0, yy, ww, 140, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL TEXTO HABLA DE…", c)
    sino(b, x0 + 20, yy + 46, c, labels=("lo que pasa siempre en los colegios", "algo que pasó una vez"), gap=380)
    pista_linea(b, x0 + 20, yy + 114, "lo que hacen los profesores con los debates, en mis palabras:", x0 + ww - 20)
    yy += 158
    return ojo(b, x0, yy, ww, "UNA FORMA PUEDE SER CORRECTA Y NO SER DE ESTE TEXTO",
               "Suelta, más de una opción arma una oración gramatical. La que va es la que suena con el resto del "
               "texto: revisa tus notas antes de marcar y comprueba también que concuerde con «Teachers».")


# ───────── 15 · B2 n.º 7 · «debating ___ not only…» ─────────
def i15(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Encuentra el sujeto y cámbialo por «it» o «they»", c,
                      "El verbo concuerda con su sujeto, no con la palabra que tenga más cerca. Encierra el sujeto, "
                      "reemplázalo por el pronombre que le toca y lee la oración otra vez.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "In the end, debating (7) ________ not only academic skills, but also teamwork and empathy.", c)
    yy += 24
    piezas = (("In the end,", "¿qué es?"), ("debating", "¿qué es?"), ("(7) ____", "verbo"),
              ("not only academic skills, …", "¿qué es?"))
    anchos = (220, 210, 170, ww - 220 - 210 - 170 - 60)
    bx = x0
    for (p, q), aw in zip(piezas, anchos):
        caja(b, bx, yy, aw, 120, c, r=12, fill=tinte(c, 0.96) if "____" in p else "white")
        texto(b, bx + aw / 2, yy + 44, p, size=19, weight="700", style="italic", anchor="middle")
        pista(b, bx + 14, yy + 80, q)
        renglon(b, bx + 14, yy + 106, bx + aw - 14)
        bx += aw + 20
    yy += 144
    caja(b, x0, yy, ww, 170, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PRUEBA DEL PRONOMBRE", c)
    pista(b, x0 + 20, yy + 66, "«debating» nombra una actividad: ¿una cosa o varias? La cambio por:")
    for j, lab in enumerate(("it", "they")):
        b.append(checkbox(x0 + 470 + j * 110, yy + 50, s=10, c=c))
        texto(b, x0 + 498 + j * 110, yy + 67, lab, size=17, weight="700", style="italic")
    pista(b, x0 + 20, yy + 112, "la oración con el pronombre y el verbo «improve» bien conjugado:")
    renglon(b, x0 + 20, yy + 150, x0 + ww - 20)
    yy += 190
    return trampa(b, x0, yy, ww, "El plural de al lado no es el sujeto:",
                  "en la oración hay palabras en plural («skills», y antes «students») que jalan el oído hacia un verbo "
                  "sin -s. El sujeto es el que hace la acción de mejorar. Si al cambiarlo por el pronombre el verbo "
                  "suena raro, revisa la terminación.", c)


# ───────── 16 · B2 n.º 8 · «These experiences ___ students to become» ─────────
def pieza(b, x, y, w, h, c, txt, fill="white", diente=True):
    """Ficha de rompecabezas: rectángulo con un diente a la derecha."""
    caja(b, x, y, w, h, c, r=8, fill=fill, sw=2.2)
    if diente:
        b.append(f'<circle cx="{x + w + 2}" cy="{y + h / 2}" r="13" fill="{fill}" stroke="{c}" stroke-width="2.2"/>')
        b.append(rect(x + w - 14, y + h / 2 - 12, 16, 24, fill, r=0))
    texto(b, x + w / 2, y + h / 2 + 7, txt, size=19, weight="700", style="italic", anchor="middle")


def i16(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El molde «___ + alguien + to + verbo»", c,
                      "Palabras que andan juntas: algunos verbos llegan con un molde fijo. Mira el molde que trae el "
                      "espacio 8, prueba cada opción dentro y busca en el párrafo 1 otro verbo que use el mismo molde.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "These experiences (8) ________ students to become more active citizens in their communities.", c)
    yy += 26
    anchos = (300, 220, 200, ww - 300 - 220 - 200 - 72)
    tx_ = ("These experiences", "(8) ____", "students", "to become…")
    bx = x0
    for k, (aw, t) in enumerate(zip(anchos, tx_)):
        pieza(b, bx, yy, aw, 80, c, t, fill=tinte(c, 0.93) if k == 1 else "white", diente=k < 3)
        bx += aw + 24
    pista(b, x0 + 300 + 24 + 110, yy + 110, "el hueco", anchor="middle")
    pista(b, x0 + 300 + 24 + 220 + 24 + 100, yy + 110, "alguien", anchor="middle")
    yy += 136
    half = (ww - 30) / 2
    for k, (tit, molde, ej) in enumerate((
            ("LOS QUE ABREN EL CAMINO", "verbo + alguien + to + verbo", "help, ask, want…"),
            ("LOS QUE CIERRAN EL CAMINO", "verbo + alguien + from + -ing", "keep someone from…"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 200, c, r=14, dash="8,6" if k else None)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        texto(b, bx + 18, yy + 62, molde, size=17, weight="700", style="italic")
        pista(b, bx + 18, yy + 92, f"(como {ej})")
        pista_linea(b, bx + 18, yy + 136, "opciones del libro que van aquí:", bx + half - 18)
        renglon(b, bx + 18, yy + 178, bx + half - 18)
    yy += 220
    caja(b, x0, yy, ww, 110, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL MISMO MOLDE EN EL PÁRRAFO 1", c)
    pista_linea(b, x0 + 20, yy + 66, "Many schools ________ students to participate…  (cópialo del libro):", x0 + ww - 20)
    pista(b, x0 + 20, yy + 96, "y el sentido: ¿el último párrafo cuenta algo que ayuda o algo que estorba?", size=14)
    return yy + 110


# ═════════════════════════ BLOQUE 3 · A Late Visitor ═════════════════════════

# ───────── 17 · B3 n.º 1 · «when Sherlock Holmes ___ the fire» ─────────
def reloj(b, cx, cy, r, c):
    import math as _m
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="3"/>')
    for k in range(12):
        a = _m.pi * 2 * k / 12
        b.append(line(cx + r * 0.82 * _m.sin(a), cy - r * 0.82 * _m.cos(a),
                      cx + r * 0.94 * _m.sin(a), cy - r * 0.94 * _m.cos(a), c, 2.4))
    a1 = -_m.pi * 2 * 5 / 60
    b.append(line(cx, cy, cx + r * 0.72 * _m.sin(a1), cy - r * 0.72 * _m.cos(a1), INK, 3.4))
    a2 = -_m.pi * 2 * 0.2 / 12
    b.append(line(cx, cy, cx + r * 0.48 * _m.sin(a2), cy - r * 0.48 * _m.cos(a2), INK, 5))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="{INK}"/>')


def llama(b, cx, by, s, c):
    b.append(f'<path d="M {cx} {by - s * 1.6} Q {cx + s * 0.9} {by - s * 0.7} {cx + s * 0.5} {by} '
             f'L {cx - s * 0.5} {by} Q {cx - s * 0.9} {by - s * 0.7} {cx} {by - s * 1.6} Z" '
             f'fill="{tinte(EDU_ORO, 0.7)}" stroke="{EDU_ORO}" stroke-width="2"/>')


def i17(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Casi medianoche en Baker Street", c,
                      "La línea de tiempo del verbo: el cuento abre con una hora. «When» amarra esa hora con lo que "
                      "hizo Holmes. Ubica la escena en el reloj, contesta si pasan al mismo tiempo y escribe en las "
                      "llamas las formas que conoces de «light».")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "It was close to midnight when Sherlock Holmes (1) ________ the fire in our Baker Street rooms.", c)
    yy += 22
    reloj(b, x0 + 130, yy + 120, 110, c)
    pista(b, x0 + 130, yy + 262, "«close to midnight»", anchor="middle")
    rx = x0 + 290
    rw = ww - 290
    caja(b, rx, yy, rw, 250, c, r=14)
    rot(b, rx + 18, yy + 30, "LA HORA Y EL HECHO", c, size=13)
    pista_linea(b, rx + 18, yy + 70, "«It was close to midnight» está en:", rx + rw - 18)
    pista(b, rx + 18, yy + 116, "¿la hora y lo que hizo Holmes pasan en el mismo momento?")
    sino(b, rx + 470, yy + 100, c)
    pista_linea(b, rx + 18, yy + 160, "entonces el espacio 1 va en:", rx + rw - 18)
    pista(b, rx + 18, yy + 206, "¿«light» es regular o irregular?")
    sino(b, rx + 260, yy + 190, c, labels=("regular", "irregular", "las dos cosas"), gap=130)
    yy += 280
    caja(b, x0, yy, ww, 120, c, r=14, fill=tinte(EDU_ORO, 0.96))
    rot(b, x0 + 20, yy + 30, "LA FAMILIA DE «LIGHT»", c, size=13)
    pista(b, x0 + 260, yy + 30, "todas las formas que conozcas, en el orden que quieras; luego encierra las que cuentan lo que pasó a medianoche")
    lw = (ww - 40) / 4
    for k in range(4):
        lx = x0 + 20 + k * lw
        llama(b, lx + 26, yy + 100, 20, c)
        renglon(b, lx + 56, yy + 100, lx + lw - 20)
    yy += 140
    return correccion(b, x0, yy, ww,
                      "El libro espera una sola respuesta, pero el verbo «light» tiene dos formas de pasado aceptadas en "
                      "inglés, y las dos están entre las opciones. Encuéntralas y márcalas las dos.",
                      escribe="las dos formas que marqué:")


# ───────── 18 · B3 n.º 2 · «the silence ___ only by…» ─────────
def i18(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "¿Quién rompe a quién?", c,
                      "Antes de escoger, dibuja la acción: quién la hace y quién la recibe. Si el que la recibe es el "
                      "sujeto de la oración, la oración está en voz pasiva.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "Outside, the silence of London (2) ________ only by the distant wheels of a carriage.", c)
    yy += 26
    bw_ = 360
    for k, (lab, ps) in enumerate((("EL QUE HACE LA ACCIÓN", "¿quién o qué?"), ("EL QUE LA RECIBE", "¿quién o qué?"))):
        bx = x0 + (0 if k == 0 else ww - bw_)
        b.append(f'<ellipse cx="{bx + bw_ / 2}" cy="{yy + 80}" rx="{bw_ / 2}" ry="78" fill="white" stroke="{c}" '
                 f'stroke-width="2.4"/>')
        rot(b, bx + bw_ / 2, yy + 46, lab, c, size=13, anchor="middle")
        pista(b, bx + bw_ / 2, yy + 74, ps, anchor="middle")
        renglon(b, bx + 50, yy + 116, bx + bw_ - 50)
    flecha(b, x0 + bw_ + 20, yy + 80, x0 + ww - bw_ - 20, yy + 80, c, sw=3, head=16)
    texto(b, x0 + ww / 2, yy + 60, "to break (romper)", size=18, style="italic", weight="700", anchor="middle")
    yy += 186
    half = (ww - 30) / 2
    preg = ("¿cuál de los dos es el sujeto de la oración?", "¿qué me dice la palabra «by»?",
            "entonces la oración es…", "¿en qué tiempo va el relato?")
    for k, p in enumerate(preg):
        bx = x0 + (k % 2) * (half + 30)
        by = yy + (k // 2) * 112
        caja(b, bx, by, half, 96, c, r=30, fill=tinte(c, 0.97))
        pista(b, bx + 26, by + 34, p)
        if k == 2:
            sino(b, bx + 230, by + 18, c, labels=("activa", "pasiva"), gap=110)
        renglon(b, bx + 26, by + 74, bx + half - 26)
    yy += 2 * 112 + 4
    return ojo(b, x0, yy, ww, "PASIVA = BE + PARTICIPIO",
               "En la voz pasiva el verbo «be» lleva el tiempo (is, was, were…) y el verbo principal va en "
               "participio. Y la forma del «be» concuerda con el sujeto, como cualquier verbo.")


# ───────── 19 · B3 n.º 3 · «my thoughts ___ constantly wandering» ─────────
def i19(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La nube de pensamientos: ¿una o muchas?", c,
                      "La palabra de al lado manda la forma: el espacio está entre un sujeto y una palabra en -ing. "
                      "Dibuja en la nube cuántos pensamientos tiene Watson, encierra el sujeto verdadero y decide qué "
                      "verbo pide la -ing.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "I sat opposite him, a book open in my hands, though my thoughts (3) ________ constantly "
                                "wandering back to his sharp expression.", c, size=20)
    yy += 26
    cx, cy = x0 + 280, yy + 150
    for dx, dy, r_ in ((-150, 20, 80), (-60, -50, 95), (60, -40, 90), (150, 20, 80), (0, 60, 110)):
        b.append(f'<circle cx="{cx + dx}" cy="{cy + dy}" r="{r_}" fill="{tinte(c, 0.95)}" stroke="{c}" stroke-width="2"/>')
    for dx, dy, r_ in ((-150, 20, 78), (-60, -50, 93), (60, -40, 88), (150, 20, 78), (0, 60, 108)):
        b.append(f'<circle cx="{cx + dx}" cy="{cy + dy}" r="{r_}" fill="{tinte(c, 0.95)}"/>')
    pista(b, cx, cy - 10, "dibuja aquí sus pensamientos:", anchor="middle")
    pista(b, cx, cy + 14, "¿uno o varios?", anchor="middle")
    rx, rw = x0 + 560, ww - 560
    ficha(b, rx, yy, rw, 160, c, "EL SUJETO DE «WANDERING»", ("¿quién está «wandering»?", "¿termina en -s? ¿uno o varios?"))
    ficha(b, rx, yy + 176, rw, 116, c, "LO QUE PIDE LA -ING", ("antes de una -ing, para armar el tiempo, va:",))
    yy += 320
    return trampa(b, x0, yy, ww, "«I» y «my» están cerca, pero no mandan aquí:",
                  "en la oración hay un «I» y dos «my», todos en singular. Ninguno es el sujeto del espacio 3. El que "
                  "manda es el que está «wandering»: el verbo concuerda con él y va en el tiempo del relato, como «sat».",
                  c)


# ───────── 20 · B3 n.º 4 · «hurried footsteps ___ on the stairs» ─────────
def i20(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Pasos en la escalera: ¿cuándo suenan?", c,
                      "La línea de tiempo del verbo: «Suddenly» abre un hecho que interrumpe la calma. Sigue la escena "
                      "escribiendo qué pasa en cada escena y decide si los pasos sonaron mientras Watson leía o antes.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "Suddenly, hurried footsteps (4) ________ on the stairs, quick and uneven, disturbing the "
                                "stillness of the night.", c, size=20)
    yy += 22
    sx, sy = x0, yy
    pts = []
    for k in range(6):
        pts += [f"{sx + k * 56},{sy + 220 - k * 36}", f"{sx + (k + 1) * 56},{sy + 220 - k * 36}"]
    pts += [f"{sx + 6 * 56},{sy + 240}", f"{sx},{sy + 240}"]
    b.append(f'<polygon points="{" ".join(pts)}" fill="{tinte(c, 0.93)}" stroke="{c}" stroke-width="2"/>')
    for k in (1, 3, 5):
        b.append(f'<ellipse cx="{sx + k * 56 + 26}" cy="{sy + 220 - k * 36 - 10}" rx="12" ry="6" fill="{INK}" opacity="0.55"/>')
    pista(b, sx + 170, sy + 270, "los pasos en la escalera", anchor="middle")
    ex = x0 + 400
    ew = (ww - 400 - 60) / 3
    for k, (t, ps) in enumerate((("I sat opposite him…", "Watson está:"), ("Suddenly, footsteps (4)…", "los pasos:"),
                                 ("a tall figure appeared…", "el visitante:"))):
        bx = ex + k * (ew + 30)
        caja(b, bx, sy, ew, 250, c, r=14, fill=tinte(c, 0.96) if k == 1 else "white")
        rot(b, bx + 16, sy + 30, f"ESCENA {k + 1}", c, size=13)
        texto(b, bx + 16, sy + 62, t, size=15, style="italic", weight="700")
        pista(b, bx + 16, sy + 100, ps, size=14)
        renglon(b, bx + 16, sy + 136, bx + ew - 16)
        pista(b, bx + 16, sy + 176, "el verbo y su tiempo:", size=14)
        renglon(b, bx + 16, sy + 214, bx + ew - 16)
        if k < 2:
            flecha(b, bx + ew + 4, sy + 125, bx + ew + 26, sy + 125, c, head=8)
    yy = sy + 290
    caja(b, x0, yy, ww, 104, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "¿ANTES O MIENTRAS?", c)
    pista(b, x0 + 20, yy + 66, "los pasos sonaron…")
    sino(b, x0 + 160, yy + 50, c, labels=("mientras Watson estaba sentado", "antes de que se sentara"), gap=300)
    yy += 122
    return correccion(b, x0, yy, ww,
                      "En inglés los pasos no «corren»: suenan. Un hablante diría «footsteps sounded» o «footsteps "
                      "echoed on the stairs». El libro te pide una forma de «run»: escoge la que va con el relato.",
                      escribe="la oración con el verbo que usaría un hablante:")


# ───────── 21 · B3 n.º 5 · «his hands trembled as he ___ a letter» ─────────
def engranaje(b, cx, cy, r, c, dientes=10, fase=0.0):
    import math as _m
    pts = []
    for k in range(dientes * 2):
        a = fase + _m.pi * k / dientes
        rr = r if k % 2 == 0 else r * 0.8
        a1, a2 = a - _m.pi / dientes * 0.35, a + _m.pi / dientes * 0.35
        pts += [f"{cx + rr * _m.cos(a1):.1f},{cy + rr * _m.sin(a1):.1f}",
                f"{cx + rr * _m.cos(a2):.1f},{cy + rr * _m.sin(a2):.1f}"]
    b.append(f'<polygon points="{" ".join(pts)}" fill="{tinte(c, 0.9)}" stroke="{c}" stroke-width="2.2"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.62:.1f}" fill="white" stroke="{c}" stroke-width="1.8"/>')


def i21(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Los engranajes de «as»", c,
                      "El párrafo entero decide: «as» engrana dos acciones que giran al mismo tiempo. Escribe en cada "
                      "rueda su acción y su tiempo, y copia los verbos del resto del párrafo para ver en qué tiempo "
                      "gira toda la escena.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "The stranger's coat was dripping from the rain, and his hands trembled as he (5) ________ "
                                "a crumpled letter from his pocket.", c, size=20)
    yy += 24
    r = 120
    c1, c2 = (x0 + 140, yy + 140), (x0 + 140 + 2 * r * 0.92, yy + 140)
    engranaje(b, *c1, r, c, 10)
    engranaje(b, *c2, r, c, 10, fase=0.31)
    for (gx, gy), (t1, t2) in zip((c1, c2), (("his hands", "trembled"), ("he", "(5) ____"))):
        texto(b, gx, gy - 22, t1, size=16, style="italic", weight="700", anchor="middle")
        texto(b, gx, gy + 6, t2, size=16, style="italic", weight="700", anchor="middle", color=c)
        renglon(b, gx - 50, gy + 44, gx + 50)
    pista(b, (c1[0] + c2[0]) / 2, yy + 292, "el tiempo de cada rueda, en su renglón", anchor="middle")
    rx = x0 + 560
    rw = ww - 560
    caja(b, rx, yy, rw, 150, c, r=14)
    rot(b, rx + 18, yy + 30, "«AS» AQUÍ QUIERE DECIR", c, size=13)
    for j, lab in enumerate(("mientras, al tiempo que", "porque", "como (igual que)")):
        b.append(checkbox(rx + 18, yy + 50 + j * 32, s=10, c=c))
        texto(b, rx + 46, yy + 67 + j * 32, lab, size=15, color=GRAY)
    caja(b, rx, yy + 166, rw, 146, c, r=14, dash="8,6")
    rot(b, rx + 18, yy + 196, "LA ESCENA ENTERA", c, size=13)
    pista_linea(b, rx + 18, yy + 232, "«The stranger's coat ___ dripping»:", rx + rw - 18)
    pista_linea(b, rx + 18, yy + 270, "«Holmes ___ without haste»:", rx + rw - 18)
    pista(b, rx + 18, yy + 300, "(los dos, copiados del libro)", size=14)
    yy += 330
    return ojo(b, x0, yy, ww, "DOS RUEDAS QUE GIRAN JUNTAS VAN AL MISMO PASO",
               "Cuando «as» quiere decir «al tiempo que», las dos acciones se cuentan en el mismo tiempo. Si una "
               "rueda va en un tiempo y la otra en otro, el engranaje se traba.")


# ───────── 22 · B3 n.º 6 · «Holmes rose without haste, ___ the man» ─────────
def i22(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Una oración, un solo verbo que manda", c,
                      "Una oración en inglés tiene un verbo conjugado principal. Si ya está, y no hay «and» que una "
                      "otro, lo que sigue después de la coma describe cómo lo hace. Corta la oración en piezas.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "Holmes rose without haste, (6) ________ the man with that steady, piercing look that "
                                "seemed to strip away every secret.", c)
    yy += 24
    piezas = (("Holmes", "sujeto"), ("rose", "¿qué es?"), ("without haste,", "¿qué es?"), ("(6) ____ the man", "¿qué es?"),
              ("with that steady look…", "¿qué es?"))
    anchos = (170, 150, 230, 250, ww - 170 - 150 - 230 - 250 - 80)
    bx = x0
    for (p, q), aw in zip(piezas, anchos):
        caja(b, bx, yy, aw, 116, c, r=12, fill=tinte(c, 0.96) if "____" in p else "white")
        texto(b, bx + aw / 2, yy + 42, p, size=18, weight="700", style="italic", anchor="middle")
        pista(b, bx + 12, yy + 76, q)
        renglon(b, bx + 12, yy + 102, bx + aw - 12)
        bx += aw + 20
    yy += 140
    caja(b, x0, yy, ww, 210, c, r=14)
    rot(b, x0 + 20, yy + 30, "CUENTO Y DECIDO", c)
    pista(b, x0 + 20, yy + 66, "verbos conjugados que ya tiene la oración:")
    renglon(b, x0 + 330, yy + 70, x0 + ww / 2)
    pista(b, x0 + ww / 2 + 20, yy + 66, "¿hay «and» antes del espacio?")
    sino(b, x0 + ww / 2 + 250, yy + 50, c)
    pista(b, x0 + 20, yy + 112, "si tuviera «and», la oración diría: Holmes rose without haste and ________ the man…")
    pista(b, x0 + 20, yy + 152, "sin «and», el segundo verbo cuenta qué hacía Holmes mientras se levantaba; va en la forma:")
    renglon(b, x0 + 20, yy + 192, x0 + ww / 2)
    yy += 230
    return ojo(b, x0, yy, ww, "EL AUTOR YA LO HIZO ANTES",
               "Busca en el Bloque 3 otra oración que, después de la coma, sigue describiendo sin «and»: «…hurried "
               "footsteps (4) ____ on the stairs, quick and uneven, disturbing the stillness of the night». ¿En qué "
               "forma está ese verbo? Leer el texto entero te enseña cómo escribe este autor.")


# ───────── 23 · B3 n.º 7 · «while Holmes ___ each detail» ─────────
def i23(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Verbos que no viajan solos", c,
                      "Palabras que andan juntas: hay verbos que siempre llevan su preposición. Une cada verbo con la "
                      "suya y después mira qué le pasó a la oración del libro. El tiempo lo decide el relato, como en "
                      "«delivered».")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "He delivered his tale in broken sentences, while Holmes (7) ________ each detail with "
                                "unbroken attention.", c, size=20)
    yy += 24
    verbos = ("look", "wait", "listen", "depend")
    preps = ("on", "to", "at", "for")
    pw, ph = 200, 58
    for k, (v, p) in enumerate(zip(verbos, preps)):
        vy = yy + k * (ph + 14)
        pieza(b, x0 + 40, vy, pw, ph, c, v)
        caja(b, x0 + 560, vy, 140, ph, c, r=29, fill=tinte(c, 0.93))
        texto(b, x0 + 630, vy + 37, p, size=19, weight="700", style="italic", anchor="middle")
        pista_linea(b, x0 + 740, vy + 36, "el par, en español:", x0 + ww - 20)
    pista(b, x0 + 400, yy + 4 * (ph + 14) + 10, "une con una línea cada verbo con su preposición", anchor="middle")
    yy += 4 * (ph + 14) + 30
    caja(b, x0, yy, ww, 104, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "EL TIEMPO DEL ESPACIO 7", c)
    pista_linea(b, x0 + 20, yy + 66, "«He delivered» va en ______ y «while» une dos acciones del mismo momento; entonces:",
                x0 + ww - 20)
    yy += 122
    return correccion(b, x0, yy, ww,
                      "Al libro le falta «to»: en inglés se escucha «a» algo («listen to something»). Con cualquiera de "
                      "las opciones, la oración queda incompleta. Escoge la forma del verbo que va con el relato y escribe "
                      "la oración como debe ir, con el «to».",
                      escribe="while Holmes")


# ───────── 24 · B3 n.º 8 · «Holmes already ___ the outline» ─────────
def i24(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El censo de los verbos del relato", c,
                      "El tiempo de un relato lo decide el texto entero, no una sola oración. Copia en las cartas los "
                      "verbos conjugados del último párrafo, anota su tiempo y cuenta. El espacio 8 tiene que sonar como "
                      "el resto del cuento.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "To me the account sounded confusing, but Holmes already (8) ________ the outline of a "
                                "mystery forming with alarming clarity.", c)
    yy += 22
    n = 5
    gap = 18
    cw = (ww - gap * (n - 1)) / n
    for k in range(n):
        bx = x0 + k * (cw + gap)
        caja(b, bx + 6, yy + 6, cw, 210, tinte(c, 0.7), r=14, fill=tinte(c, 0.9))
        caja(b, bx, yy, cw, 210, c, r=14)
        b.append(f'<circle cx="{bx + 30}" cy="{yy + 30}" r="16" fill="{c}"/>')
        texto(b, bx + 30, yy + 36, str(k + 1), size=16, color="white", weight="700", anchor="middle")
        pista(b, bx + 16, yy + 80, "el verbo:", size=14)
        renglon(b, bx + 16, yy + 116, bx + cw - 16)
        pista(b, bx + 16, yy + 154, "su tiempo:", size=14)
        renglon(b, bx + 16, yy + 190, bx + cw - 16)
    yy += 236
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL CONTEO", c)
    for j, lab in enumerate(("en pasado:", "en presente:", "con auxiliar:")):
        pista(b, x0 + 20 + j * 330, yy + 70, lab)
        b.append(rect(x0 + 140 + j * 330, yy + 46, 70, 40, "white", r=8, stroke=c, sw=1.8))
    pista(b, x0 + 20, yy + 124, "entonces el verbo del espacio 8 va en:")
    renglon(b, x0 + 300, yy + 128, x0 + ww / 2)
    pista(b, x0 + ww / 2 + 20, yy + 124, "¿hay auxiliar antes del espacio?")
    sino(b, x0 + ww / 2 + 260, yy + 108, c)
    yy += 170
    return ojo(b, x0, yy, ww, "«ALREADY» NO OBLIGA AL PRESENTE PERFECTO",
               "«Already» se usa mucho con «have + participio», pero también en un relato en pasado: «He already knew "
               "the answer». Si el auxiliar no aparece en la oración, la forma que escojas tiene que poder ir sola.")


_P = {1: 468, 2: 469, 3: 470}
_CTX = {1: ("1", "«Two years ago, my family and I ___»", 1, "Gramática · tiempos verbales"),
        2: ("2", "«we ___ tired when we finally arrived»", 4, "Gramática · tiempo del relato"),
        3: ("3", "«While we ___ our tent»", 1, "Gramática · tiempos verbales"),
        4: ("4", "«it suddenly ___ to snow»", 1, "Gramática · tiempos verbales"),
        5: ("5", "«Since that day, I ___»", 1, "Gramática · tiempos verbales"),
        6: ("6", "«I have already ___»", 2, "Gramática · forma del verbo"),
        7: ("7", "«and I ___ a blog»", 4, "Gramática · tiempo del relato"),
        8: ("8", "«Honestly, I ___ never imagined»", 1, "Gramática · tiempos verbales"),
        9: ("1", "«students ___ different points of view»", 3, "Léxico · colocación"),
        10: ("2", "«Some debates ___ subjects»", 3, "Léxico · sentido y colocación"),
        11: ("3", "«to ___ critical thinking»", 3, "Léxico · colocación"),
        12: ("4", "«___ evidence before speaking»", 3, "Léxico · sentido y colocación"),
        13: ("5", "«Sometimes, students ___ nervous»", 2, "Gramática · concordancia"),
        14: ("6", "«Teachers ___ debates»", 4, "Gramática · tiempo del texto"),
        15: ("7", "«debating ___ not only academic skills»", 2, "Gramática · concordancia"),
        16: ("8", "«These experiences ___ students to…»", 3, "Léxico · régimen del verbo"),
        17: ("1", "«when Sherlock Holmes ___ the fire»", 1, "Gramática · tiempos verbales"),
        18: ("2", "«the silence of London ___»", 2, "Gramática · voz pasiva"),
        19: ("3", "«my thoughts ___ constantly wandering»", 2, "Gramática · concordancia"),
        20: ("4", "«hurried footsteps ___ on the stairs»", 1, "Gramática · tiempos verbales"),
        21: ("5", "«his hands trembled as he ___»", 4, "Gramática · tiempo del relato"),
        22: ("6", "«Holmes rose without haste, ___»", 4, "Gramática · cohesión de la oración"),
        23: ("7", "«while Holmes ___ each detail»", 3, "Léxico · verbo y preposición"),
        24: ("8", "«Holmes already ___ the outline»", 4, "Gramática · tiempo del relato")}
_INST = {k: globals()[f"i{k}"] for k in range(1, 25)}


def _q(n):
    nl, frase, est, comp = _CTX[n]
    bloque = (n - 1) // 8 + 1
    pag = _P[bloque]
    return dict(n=n, est=est, pag=pag, ctx=f"Bloque {bloque}, n.º {nl} del libro · {frase}", comp=comp,
                inst=_INST[n])


Q = {n: _q(n) for n in range(1, 25)}


def build(pages=(331, 332, 333, 334, 335, 336, 338, 339, 340, 341, 342, 343)):
    out = []
    for k in range(12):
        out.append(hoja_taller(f"ing6_t{k + 1}", pages[k], k + 1, Q[2 * k + 1], Q[2 * k + 2]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
