#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 1 · componente biológico-celular · páginas 140–146.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 1» de Biología, páginas 72–75 (componente biológico –
celular). Casos: desechos acumulados (1), fertilizante y marchitez (2), CO2 en células musculares
(3), Golgi en células tumorales (4), inhibidores de la ruta de secreción (5), gemelos y enzima
(6 y 7), glóbulos rojos sin núcleo (8), dos líneas que secretan insulina (9) y Golgi reducido (10).

Claves verificadas (resueltas a mano contra el texto y las gráficas del libro, 7 nov 2026):

    1·A  2·B  3·B  4·C  5·D  6·A  7·B  8·B  9·A  10·C

Cuentas: 3 → reposo 20 ppm, actividad 45 ppm; 45 − 20 = 25 ppm; 45 / 20 = 2,25 veces.
         5 → control 40; núcleo 0, RER 0, Golgi 0: cualquier etapa bloqueada deja la exportación en 0.
Reparto: A 3 · B 4 · C 2 · D 1. Sin concentración grave. Hallazgos (la figura de la 1 tacha el
lisosoma; 4 y 10, 6 y 7 preguntan casi lo mismo; el texto de la 9 se contradice): en
tablero/propuestas/bio1_hallazgos.csv.

Estrategias:
    1 · Cada organelo, su oficio                  (1, 8          · ICFES 2a-60)   azul
    2 · La ruta de la proteína, estación a estación (4, 5, 9, 10 · ICFES 2a-75)   rojo
    3 · Comparar contra el que no cambió          (3, 6, 7       · ICFES 2a-58)   oro
    4 · Dónde hay más y hacia dónde va            (2             · ICFES 1a-93)   morado

Hojas: 140 bio1_t1 (1-2) · 141 bio1_t2 (3-4) · 142 bio1_i1 · 143 bio1_t3 (5-6) ·
       144 bio1_t4 (7-8) · 145 bio1_t5 (9-10) · 146 bio1_i2.
"""
from taller_base import *

configurar("Biología", 1, "biológico · celular",
           tema="La célula: una fábrica que trabaja en cadena", nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Cada organelo, su oficio", EDU_AZUL),
       2: ("La ruta de la proteína, estación a estación", EDU_ROJO),
       3: ("Comparar contra el que no cambió", EDU_ORO),
       4: ("Dónde hay más y hacia dónde va", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))
VERDE_CEL = "#EEF7EF"      # citoplasma: tinte del verde de Biología


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def frase_hueco(b, x, y, w, texto, c, h=56):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [texto], 18, INK, weight="700"))
    return y + h


def ficha(b, cx, cy, txt, c, r=16, size=16):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="2.2"/>')
    b.append(T(cx, cy + size * 0.38, [txt], size, c, weight="700", anchor="middle"))


def flecha(b, x1, y1, x2, y2, c, sw=2.6, bend=0.0, head=13):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def parrafo(b, x, y, w, texto, size=17, color=INK, style="normal"):
    svg, yy = TJ(x, y, texto, w, size, color, style=style, lh=size + 8)
    b.append(svg)
    return yy


# ───────── P1 · desechos acumulados · los oficios ─────────
def _celula(b, cx, cy, rx, ry, c):
    """Célula animal esquemática: membrana, núcleo, mitocondria, lisosoma y desechos.
    Devuelve los puntos a los que apuntan las cuatro fichas (sin nombres: los pone el estudiante)."""
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{VERDE_CEL}" stroke="{c}" '
             f'stroke-width="3"/>')
    nx, ny = cx - 40, cy + 6
    b.append(f'<circle cx="{nx}" cy="{ny}" r="58" fill="white" stroke="{c}" stroke-width="2.4"/>')
    b.append(f'<circle cx="{nx + 8}" cy="{ny - 4}" r="18" fill="{c}" fill-opacity="0.25"/>')
    mx, my = cx + 112, cy - 78
    b.append(f'<ellipse cx="{mx}" cy="{my}" rx="52" ry="24" fill="white" stroke="{c}" stroke-width="2.2"/>')
    pts = " ".join(f"{mx - 40 + i * 10},{my + (12 if i % 2 else -12)}" for i in range(9))
    b.append(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="1.8"/>')
    lx, ly = cx + 118, cy + 86
    b.append(f'<circle cx="{lx}" cy="{ly}" r="22" fill="white" stroke="{c}" stroke-width="2.2"/>')
    for dx, dy in ((-7, -6), (6, -4), (-2, 7), (8, 8)):
        b.append(f'<circle cx="{lx + dx}" cy="{ly + dy}" r="3" fill="{c}"/>')
    # desechos: manchas grises sueltas en el citoplasma
    for dx, dy, s in ((-150, -60, 1.0), (-120, 92, 0.8), (40, -110, 0.9), (60, 104, 1.1), (-160, 30, 0.7),
                      (16, 140, 0.8), (170, 10, 0.8)):
        x0, y0 = cx + dx, cy + dy
        d = (f"M {x0 - 14 * s:.0f} {y0:.0f} L {x0 - 6 * s:.0f} {y0 - 11 * s:.0f} L {x0 + 9 * s:.0f} {y0 - 8 * s:.0f} "
             f"L {x0 + 14 * s:.0f} {y0 + 4 * s:.0f} L {x0 + 2 * s:.0f} {y0 + 11 * s:.0f} Z")
        b.append(f'<path d="{d}" fill="#9AA0AA" fill-opacity="0.55"/>')
    return {"1": (cx - rx * 0.72, cy + ry * 0.69), "2": (nx - 36, ny - 46), "3": (mx + 30, my - 18), "4": (lx + 16, ly + 16)}


def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Cuatro oficios y una basura que no sale", c,
                      "Ponle nombre a cada número del dibujo y escribe su oficio. Después pregúntale a cada uno: "
                      "si dejas de trabajar, ¿qué se queda sin hacer? La basura acumulada es la pista.")
    x0, ww = x + 22, w - 44
    cw_ = 470
    cx, cy = x0 + cw_ / 2 + 10, yy + 196
    p = _celula(b, cx, cy, 214, 172, c)
    fichas = {"1": (x0 + 14, yy + 380), "2": (x0 + 40, yy + 26), "3": (x0 + cw_ - 20, yy + 18),
              "4": (x0 + cw_ - 6, yy + 400)}
    for k, (fx, fy) in fichas.items():
        tx, ty = p[k]
        b.append(f'<line x1="{fx}" y1="{fy}" x2="{tx}" y2="{ty}" stroke="{c}" stroke-width="1.8"/>')
        ficha(b, fx, fy, k, c, r=17)
    pista(b, cx, yy + 440, "las manchas grises: el material de desecho acumulado", size=14, anchor="middle")
    rx = x0 + cw_ + 40
    rw = x0 + ww - rx
    for k in range(4):
        ry = yy + k * 124
        caja(b, rx, ry, rw, 112, c, r=12)
        ficha(b, rx + 30, ry + 36, str(k + 1), c, r=15, size=15)
        pista(b, rx + 58, ry + 42, "se llama:")
        renglon(b, rx + 128, ry + 44, rx + 340)
        pista(b, rx + 356, ry + 42, "su oficio:")
        renglon(b, rx + 430, ry + 44, rx + rw - 18)
        pista(b, rx + 58, ry + 92, "si se detiene, lo que queda sin hacer:")
        renglon(b, rx + 318, ry + 94, rx + rw - 18)
    yy += 4 * 124 + 10
    yy = frase_hueco(b, x0, yy, ww, "La basura se queda adentro cuando falla el número ___ , porque su oficio "
                                    "es ________________________ .", c)
    return ojo(b, x0, yy + 14, ww, "El dibujo de tu libro ya marca un organelo:",
               "no le creas al dibujo, créele al oficio. Si tu frase de arriba no explica por qué ese organelo y no "
               "los otros tres, la respuesta todavía no es tuya.")


# ───────── P2 · fertilizante · ósmosis ─────────
def i2(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Sal afuera, agua en camino", c,
                      "Dibuja puntos de soluto a cada lado de la membrana: pocos donde hay poco, muchos donde hay "
                      "mucho. Después dibuja la flecha del agua y síguela hasta la hoja.")
    x0, ww = x + 22, w - 44
    bw, bh = 330, 250
    cy_ = yy + 10
    # dos compartimentos y la membrana
    caja(b, x0, cy_, bw, bh, c, r=16, fill=VERDE_CEL)
    rot(b, x0 + 20, cy_ + 30, "ADENTRO · CÉLULA DE LA RAÍZ", c, size=13)
    caja(b, x0 + bw + 40, cy_, bw, bh, c, r=16, fill="#FBF4E8")
    rot(b, x0 + bw + 60, cy_ + 30, "AFUERA · SUELO CON FERTILIZANTE", c, size=13)
    mx = x0 + bw + 20
    for k in range(9):
        yk = cy_ + 16 + k * 26
        b.append(f'<line x1="{mx}" y1="{yk}" x2="{mx}" y2="{yk + 14}" stroke="{c}" stroke-width="4" '
                 f'stroke-linecap="round"/>')
    pista(b, mx, cy_ + bh + 26, "membrana", size=14, anchor="middle")
    pista(b, x0 + 20, cy_ + bh - 16, "dibuja aquí los puntos de soluto", size=14)
    pista(b, x0 + bw + 60, cy_ + bh - 16, "dibuja aquí los puntos de soluto", size=14)
    # la flecha del agua, para que la dibuje
    ax = x0 + 2 * bw + 80
    aw = x0 + ww - ax
    caja(b, ax, cy_, aw, bh, c, r=16)
    rot(b, ax + 20, cy_ + 30, "EL AGUA SE MUEVE", c, size=14)
    pista(b, ax + 20, cy_ + 56, "de donde hay ______ soluto")
    pista(b, ax + 20, cy_ + 92, "a donde hay ______ soluto")
    pista(b, ax + 20, cy_ + 140, "en este caso va de")
    renglon(b, ax + 160, cy_ + 142, ax + aw - 18)
    pista(b, ax + 20, cy_ + 180, "hacia")
    renglon(b, ax + 70, cy_ + 182, ax + aw - 18)
    pista(b, ax + 20, cy_ + 226, "dibuja la flecha sobre la membrana", size=14)
    yy = cy_ + bh + 50
    # la cadena hasta la hoja
    pasos = ("la célula pierde", "la planta pierde", "por eso la hoja")
    n, gap = 3, 46
    sw_ = (ww - gap * (n - 1)) / n
    for k, ps in enumerate(pasos):
        sx = x0 + k * (sw_ + gap)
        caja(b, sx, yy, sw_, 96, c, r=14)
        pista(b, sx + 18, yy + 32, ps)
        renglon(b, sx + 18, yy + 76, sx + sw_ - 18)
        if k < n - 1:
            flecha(b, sx + sw_ + 4, yy + 48, sx + sw_ + gap - 4, yy + 48, c)
    yy += 112
    return trampa(b, x0, yy, ww, "El suelo está húmedo y aun así la hoja se marchita:",
                  "que haya agua afuera no significa que el agua entre. Mira tus puntos: el agua no persigue al "
                  "agua. ¿Qué persigue? Escríbelo en el recuadro de la derecha antes de mirar las opciones.", c)


# ───────── P3 · CO2 en células musculares ─────────
def i3(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Reposo contra esfuerzo: la gráfica habla primero", c,
                      "Antes de leer las opciones, lee las barras. El grupo en reposo es tu punto de comparación: "
                      "todo lo que digas del grupo activo lo dices «comparado con el reposo».")
    x0, ww = x + 22, w - 44
    # lectura de la gráfica
    caja(b, x0, yy, ww, 186, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE MARCA CADA BARRA", c)
    for k, (lab, xx) in enumerate((("Grupo A · reposo", x0 + 20), ("Grupo B · actividad", x0 + 520))):
        pista(b, xx, yy + 78, lab)
        caja(b, xx + 160, yy + 50, 110, 46, c)
        b.append(T(xx + 282, yy + 80, ["ppm de CO₂"], 16, GRAY))
    for k, (lab, uni, xx) in enumerate((("B menos A:", "ppm", x0 + 20), ("B dividido entre A:", "veces", x0 + 520))):
        pista(b, xx, yy + 148, lab)
        caja(b, xx + 160, yy + 120, 110, 46, c)
        b.append(T(xx + 282, yy + 150, [uni], 16, GRAY))
    pista(b, x0 + ww - 20, yy + 148, "las cuentas, en el recuadro de abajo", size=14, anchor="end")
    yy += 204
    # de dónde sale el CO2
    caja(b, x0, yy, ww, 170, c, r=14)
    rot(b, x0 + 20, yy + 30, "DE DÓNDE SALE ESE CO₂", c)
    b.append(T(x0 + 20, yy + 80, ["glucosa  +  oxígeno   →   ________  +  agua  +  energía (ATP)"], 22, INK))
    pista(b, x0 + 20, yy + 122, "este proceso se llama")
    renglon(b, x0 + 180, yy + 124, x0 + 620)
    pista(b, x0 + 640, yy + 122, "y ocurre en el organelo")
    renglon(b, x0 + 812, yy + 124, x0 + ww - 20)
    pista(b, x0 + 20, yy + 156, "más CO₂ medido quiere decir que ese organelo trabajó ______ (más / menos)")
    yy += 188
    # lo que sí y no se midió
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("LO QUE LA GRÁFICA SÍ MIDIÓ", "una sola cosa, con su unidad"),
                                  ("LO QUE NO MIDIÓ", "algo que una opción podría afirmar sin datos"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 104, c, r=14, dash="8,6" if k else None)
        rot(b, bx + 18, yy + 28, rt, c, size=14)
        pista(b, bx + 18, yy + 52, ps, size=14)
        renglon(b, bx + 18, yy + 88, bx + half - 18)
    return yy + 104


# ───────── P4 · Golgi alterado · la línea de ensamblaje ─────────
def i4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La línea de ensamblaje con una estación dañada", c,
                      "Una proteína de exportación pasa por estas estaciones en orden. Escribe en cada una qué le "
                      "hacen. Después sigue a la proteína hasta la estación dañada: ¿hasta dónde llega y qué le "
                      "falta cuando se queda ahí?")
    x0, ww = x + 22, w - 44
    est = (("NÚCLEO", "la instrucción"), ("RIBOSOMA Y RER", "la cadena"), ("APARATO DE GOLGI", ""),
           ("VESÍCULA", "el viaje"), ("MEMBRANA", "la salida"))
    n, gap = 5, 26
    sw_ = (ww - gap * (n - 1)) / n
    by = yy + 20
    for k, (nom, ps) in enumerate(est):
        sx = x0 + k * (sw_ + gap)
        danada = k == 2
        caja(b, sx, by, sw_, 170, c, r=14, dash="7,6" if danada else None)
        rot(b, sx + sw_ / 2, by + 30, nom, c, size=13, anchor="middle")
        if ps:
            pista(b, sx + sw_ / 2, by + 54, ps, size=14, anchor="middle")
        pista(b, sx + 14, by + 84, "le hace:", size=14)
        renglon(b, sx + 14, by + 118, sx + sw_ - 14)
        renglon(b, sx + 14, by + 154, sx + sw_ - 14)
        if danada:
            # grieta: la estación está dañada (dato del enunciado)
            gx = sx + sw_ - 12
            b.append(f'<polyline points="{gx},{by - 8} {gx - 12},{by + 14} {gx + 4},{by + 26} {gx - 10},{by + 48}" '
                     f'fill="none" stroke="{c}" stroke-width="3"/>')
            pista(b, sx + sw_ / 2, by + 196, "dañada en estas células", size=14, anchor="middle")
        if k < n - 1:
            flecha(b, sx + sw_ + 2, by + 70, sx + sw_ + gap - 2, by + 70, c, sw=2.4, head=10)
    yy = by + 216
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "SIGUE A LA PROTEÍNA", c)
    pista(b, x0 + 20, yy + 70, "llega bien hasta la estación")
    renglon(b, x0 + 236, yy + 72, x0 + 620)
    pista(b, x0 + 640, yy + 70, "y allí se queda sin")
    renglon(b, x0 + 790, yy + 72, x0 + ww - 20)
    pista(b, x0 + 20, yy + 122, "por eso se acumula en")
    renglon(b, x0 + 190, yy + 124, x0 + 620)
    pista(b, x0 + 640, yy + 122, "y llega mal a")
    renglon(b, x0 + 750, yy + 124, x0 + ww - 20)
    yy += 166
    return trampa(b, x0, yy, ww, "Una opción le da al Golgi un oficio de otra estación:",
                  "revisa en tu línea dónde nace la instrucción y dónde se arma la cadena. Si una opción dice que "
                  "el daño está «antes» del Golgi, ya no habla de la alteración que vieron los científicos.", c)


# ───────── P5 · inhibidores · la ruta en serie ─────────
def i5(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Tres compuertas en la misma tubería", c,
                      "Copia de la gráfica lo que exportó cada grupo. Después imagina la ruta como una tubería con "
                      "tres compuertas en fila: cierra una sola por grupo y mira si algo sale al final.")
    x0, ww = x + 22, w - 44
    grupos = ("Control", "Grupo 1 · núcleo", "Grupo 2 · RER", "Grupo 3 · Golgi")
    gw = (ww - 3 * 20) / 4
    for k, g in enumerate(grupos):
        gx = x0 + k * (gw + 20)
        caja(b, gx, yy, gw, 92, c, r=12)
        rot(b, gx + 16, yy + 28, g.upper(), c, size=13)
        pista(b, gx + 16, yy + 70, "exportó:", size=15)
        caja(b, gx + 90, yy + 44, gw - 110, 38, c, r=8)
    yy += 116
    # la tubería
    ty = yy + 60
    b.append(rect(x0, ty - 22, ww - 160, 44, "#FDF0F0", r=22, stroke=c, sw=2.4))
    for k, nom in enumerate(("NÚCLEO", "RER", "GOLGI")):
        vx = x0 + 150 + k * 330
        b.append(rect(vx - 14, ty - 40, 28, 80, "white", r=6, stroke=c, sw=2.6))
        rot(b, vx, ty - 52, nom, c, size=13, anchor="middle")
    pista(b, x0 + 10, ty + 62, "entra la instrucción", size=14)
    flecha(b, x0 + ww - 156, ty, x0 + ww - 30, ty, c, sw=3, head=14)
    pista(b, x0 + ww - 20, ty + 62, "sale la proteína", size=14, anchor="end")
    yy = ty + 90
    caja(b, x0, yy, ww, 190, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE ME DICE LA TUBERÍA", c)
    pista(b, x0 + 20, yy + 72, "¿Cuántos grupos tratados llegaron a la misma cifra? ______   ¿Cuál cifra? ______")
    pista(b, x0 + 20, yy + 122, "Si cierro una compuerta del principio, lo que viene después")
    renglon(b, x0 + 470, yy + 124, x0 + ww - 20)
    pista(b, x0 + 20, yy + 170, "Entonces la ruta funciona")
    renglon(b, x0 + 210, yy + 172, x0 + ww - 20)
    yy += 206
    return ojo(b, x0, yy, ww, "«REDUCIR» Y «DETENER» NO SON LO MISMO",
               "Una barra baja no es una barra en cero. Antes de aceptar una palabra de las opciones, mira el número "
               "que copiaste en cada caja: la conclusión tiene que decir lo que pasó con los tres grupos, no con uno.")


# ───────── P6 · gemelos · el modelo de colores ─────────
def i6(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Gemelos: lo que cambia cuando cambia el ADN", c,
                      "Todos recibieron el mismo fármaco. Lee el modelo pareja por pareja: ¿comparten todo el ADN? "
                      "¿sus dos células se ven iguales? Lo que se mueve junto con el ADN es lo que lo explica.")
    x0, ww = x + 22, w - 44
    yy = alto_profe(b, x0, yy, ww,
                    "Monocigóticos: un solo óvulo fecundado que se divide en dos; los gemelos tienen el mismo ADN. "
                    "Dicigóticos: dos óvulos fecundados por dos espermatozoides; comparten más o menos la mitad, "
                    "como dos hermanos cualquiera.") + 18
    cols = ("PAREJA DEL MODELO", "¿COMPARTEN TODO EL ADN?", "¿LAS DOS CÉLULAS IGUALES?", "CÓMO ESTÁ LA ENZIMA EN CADA UNA")
    xs = (0, 300, 560, 820)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 20, cl, c, size=13)
    yy += 36
    for k, par in enumerate(("monocigóticos", "dicigóticos · pareja 1", "dicigóticos · pareja 2")):
        ry = yy + k * 70
        caja(b, x0, ry, ww, 60, c, r=10)
        b.append(T(x0 + 18, ry + 38, [par], 17, INK))
        for j, lab in enumerate(("sí", "no")):
            b.append(checkbox(x0 + xs[1] + j * 90, ry + 19, s=11, c=c))
            b.append(T(x0 + xs[1] + 30 + j * 90, ry + 38, [lab], 16, GRAY))
            b.append(checkbox(x0 + xs[2] + j * 90, ry + 19, s=11, c=c))
            b.append(T(x0 + xs[2] + 30 + j * 90, ry + 38, [lab], 16, GRAY))
        renglon(b, x0 + xs[3], ry + 44, x0 + ww - 18)
    yy += 3 * 70 + 10
    return frase_hueco(b, x0, yy, ww, "Cuando el ADN es el mismo, la enzima ____________ ; cuando cambia, "
                                      "la enzima ____________ .", c)


# ───────── P7 · gemelos · las variables del estudio ─────────
def i7(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La ficha del experimento: qué cambió, qué se midió, qué se dejó igual", c,
                      "Un fenómeno se explica con lo que el investigador hizo cambiar, no con lo que nadie midió. "
                      "Llena la ficha con el texto de la pregunta 7 y después decide qué explicación cabe en ella.")
    x0, ww = x + 22, w - 44
    filas = (("LO QUE CAMBIA ENTRE LOS GRUPOS", "entre monocigóticos y dicigóticos cambia cuánta…"),
             ("LO QUE SE MIDIÓ", "qué observaron en las células, con sus palabras"),
             ("LO QUE SE DEJÓ IGUAL", "lo que recibieron todos por igual"))
    lw = max(tw(f[0], 14, "700") + len(f[0]) * 1.5 for f in filas) + 44
    for k, (rt, ps) in enumerate(filas):
        ry = yy + k * 104
        caja(b, x0, ry, ww, 92, c, r=14)
        b.append(rect(x0, ry, 8, 92, c, r=4))
        rot(b, x0 + 26, ry + 36, rt, c, size=14)
        pista(b, x0 + 26, ry + 66, ps, size=14)
        renglon(b, x0 + lw + 30, ry + 64, x0 + ww - 20)
    yy += 3 * 104 + 6
    # la balanza de la variación
    caja(b, x0, yy, ww, 176, c, r=14)
    rot(b, x0 + 20, yy + 30, "PON LAS DOS COSAS UNA AL LADO DE LA OTRA", c)
    for k, (g, pct) in enumerate((("monocigóticos", "comparten ____ % del ADN"),
                                  ("dicigóticos", "comparten ____ % del ADN"))):
        gx = x0 + 20 + k * (ww / 2)
        b.append(T(gx, yy + 74, [g], 18, INK, weight="700"))
        pista(b, gx, yy + 106, pct)
        pista(b, gx, yy + 146, "variación de la enzima:")
        for j, lab in enumerate(("poca", "mucha")):
            b.append(checkbox(gx + 186 + j * 100, yy + 128, s=11, c=c))
            b.append(T(gx + 216 + j * 100, yy + 146, [lab], 16, GRAY))
    yy += 192
    return trampa(b, x0, yy, ww, "Una explicación que nadie midió:",
                  "si una opción habla de algo que no aparece en ninguna fila de tu ficha (una estructura que no se "
                  "observó, una sustancia que no se registró), no explica estos resultados: explica otro experimento.",
                  c)


# ───────── P8 · glóbulos rojos sin núcleo ─────────
def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Lo que se gana al vaciar la célula", c,
                      "Compara una célula típica con un glóbulo rojo maduro. Escribe qué ocupa el espacio en cada "
                      "una. Después pon en la balanza lo que el glóbulo rojo pierde y lo que gana para su oficio.")
    x0, ww = x + 22, w - 44
    # dos dibujos
    cx1, cx2, cy = x0 + 150, x0 + 470, yy + 104
    b.append(f'<circle cx="{cx1}" cy="{cy}" r="92" fill="{VERDE_CEL}" stroke="{c}" stroke-width="2.6"/>')
    b.append(f'<circle cx="{cx1 - 10}" cy="{cy}" r="40" fill="white" stroke="{c}" stroke-width="2.2"/>')
    b.append(f'<ellipse cx="{cx1 + 52}" cy="{cy - 52}" rx="24" ry="11" fill="white" stroke="{c}" stroke-width="1.8"/>')
    pista(b, cx1, cy + 124, "célula típica", size=15, anchor="middle")
    b.append(f'<ellipse cx="{cx2}" cy="{cy}" rx="104" ry="92" fill="#FBEDED" stroke="{RO}" stroke-width="2.6"/>')
    b.append(f'<ellipse cx="{cx2}" cy="{cy}" rx="46" ry="38" fill="none" stroke="{RO}" stroke-width="1.6" '
             f'stroke-dasharray="5,6"/>')
    pista(b, cx2, cy + 124, "glóbulo rojo maduro", size=15, anchor="middle")
    pista(b, cx2, cy + 146, "(visto de frente: el centro es más delgado)", size=13, anchor="middle")
    rx = x0 + 640
    rw = x0 + ww - rx
    for k, (rt, ps) in enumerate((("EN LA CÉLULA TÍPICA", "el espacio lo ocupan…"),
                                  ("EN EL GLÓBULO ROJO", "el espacio lo ocupa casi todo…"))):
        ry = yy + k * 116
        caja(b, rx, ry, rw, 102, c, r=14)
        rot(b, rx + 18, ry + 30, rt, c, size=14)
        pista(b, rx + 18, ry + 56, ps, size=14)
        renglon(b, rx + 18, ry + 88, rx + rw - 18)
    yy += 270
    # lo que pierde y lo que gana, en dos platillos
    half = (ww - 90) / 2
    for k, (lab, ps) in enumerate((("LO QUE PIERDE", "sin núcleo ya no puede…"),
                                   ("LO QUE GANA", "con ese espacio libre puede…"))):
        px = x0 + k * (half + 90)
        caja(b, px, yy, half, 168, c, r=16)
        rot(b, px + 20, yy + 30, lab, c, size=14)
        pista(b, px + 20, yy + 56, ps, size=15)
        renglon(b, px + 20, yy + 104, px + half - 20)
        renglon(b, px + 20, yy + 148, px + half - 20)
    mid = x0 + ww / 2
    b.append(f'<polygon points="{mid - 22},{yy + 120} {mid + 22},{yy + 120} {mid},{yy + 84}" fill="{c}"/>')
    b.append(T(mid, yy + 64, ["¿vale"], 15, c, weight="700", anchor="middle"))
    b.append(T(mid, yy + 150, ["la pena?"], 15, c, weight="700", anchor="middle"))
    yy += 184
    return frase_hueco(b, x0, yy, ww, "Su oficio es ______________ ; por eso le conviene más espacio para "
                                      "_______________ .", c)


# ───────── P9 · dos líneas celulares · la hipótesis ─────────
def i9(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La lista de sospechosos que el texto ya descartó", c,
                      "Los investigadores fueron tachando causas posibles. Para cada sospechoso, busca en el texto "
                      "si lo descartan, si lo dejan en pie o si ni lo mencionan, y copia la frase. Una hipótesis "
                      "coherente se apoya en lo que queda en pie, no en lo que nadie midió.")
    x0, ww = x + 22, w - 44
    sos = ("el estímulo químico", "la capacidad de síntesis", "un daño en la estructura", "la energía disponible",
           "el sistema intracelular de exportación")
    for k, s in enumerate(sos):
        ry = yy + k * 84
        caja(b, x0, ry, ww, 74, c, r=12)
        ficha(b, x0 + 30, ry + 37, str(k + 1), c, r=15, size=15)
        b.append(T(x0 + 58, ry + 30, [s], 17, INK))
        pista(b, x0 + 58, ry + 60, "la frase del texto:", size=14)
        renglon(b, x0 + 190, ry + 62, x0 + 700)
        for j, lab in enumerate(("lo descarta", "lo deja en pie", "no lo menciona")):
            bx = x0 + 730 + j * 168
            b.append(checkbox(bx, ry + 22, s=11, c=c))
            b.append(T(bx + 28, ry + 40, [lab], 15, GRAY))
    yy += 5 * 84 + 6
    yy = frase_hueco(b, x0, yy, ww, "Mi hipótesis: la línea A puede ____________ porque tiene ____________________ .", c)
    return ojo(b, x0, yy + 14, ww, "EL TEXTO DICE DOS COSAS QUE CHOCAN",
               "Al principio dice que la línea B no expresa los genes de las proteínas de secreción; al final, que la "
               "diferencia no se debe a la capacidad de síntesis. Quédate con la conclusión de los investigadores, "
               "que es lo que pregunta la 9, y coméntalo con el profe.")


# ───────── P10 · células A y B · Golgi reducido ─────────
def i10(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dos fábricas, una sola diferencia que importa", c,
                      "Compara las células A y B estación por estación. Marca dónde son iguales y dónde no. La "
                      "explicación tiene que estar en una fila donde B es distinta, no en una donde son iguales.")
    x0, ww = x + 22, w - 44
    filas = ("ribosomas y RER (arman la cadena)", "mitocondrias (dan la energía)", "aparato de Golgi",
             "lo que se encontró al final")
    c1, c2, c3 = x0 + 420, x0 + 700, x0 + 980
    rot(b, c1, yy + 20, "CÉLULAS A", c, size=13)
    rot(b, c2, yy + 20, "CÉLULAS B", c, size=13)
    rot(b, c3, yy + 20, "¿IGUALES?", c, size=13)
    yy += 36
    for k, f in enumerate(filas):
        ry = yy + k * 82
        caja(b, x0, ry, ww, 70, c, r=10)
        b.append(T(x0 + 18, ry + 42, [f], 17, INK))
        renglon(b, c1, ry + 50, c2 - 30)
        renglon(b, c2, ry + 50, c3 - 30)
        for j, lab in enumerate(("sí", "no")):
            b.append(checkbox(c3 + j * 90, ry + 24, s=11, c=c))
            b.append(T(c3 + 30 + j * 90, ry + 43, [lab], 16, GRAY))
    yy += 4 * 82 + 10
    caja(b, x0, yy, ww, 140, c, r=14)
    rot(b, x0 + 20, yy + 30, "CONECTA CON LA PREGUNTA 4", c)
    pista(b, x0 + 20, yy + 70, "la estación distinta, en mi línea de ensamblaje, le hace a la proteína:")
    renglon(b, x0 + 560, yy + 72, x0 + ww - 20)
    pista(b, x0 + 20, yy + 118, "sin eso, la insulina queda")
    renglon(b, x0 + 214, yy + 120, x0 + 640)
    pista(b, x0 + 656, yy + 118, "y no puede")
    renglon(b, x0 + 746, yy + 120, x0 + ww - 20)
    yy += 156
    return trampa(b, x0, yy, ww, "Una opción culpa a algo que B sí tiene:",
                  "antes de aceptarla, búscala en tu tabla. Si en esa fila marcaste «sí, son iguales», esa causa no "
                  "puede explicar por qué solo B falla.", c)


Q = {1: dict(n=1, est=1, pag=72, ctx="Célula animal con desechos acumulados · qué organelo falló",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=4, pag=73, ctx="Fertilizante concentrado · hojas marchitas en suelo húmedo",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=3, pag=73, ctx="CO₂ en células musculares · reposo y actividad intensa",
             comp="Indagación", inst=i3),
     4: dict(n=4, est=2, pag=73, ctx="Células tumorales · Golgi alterado y proteínas defectuosas",
             comp="Explicación de fenómenos", inst=i4),
     5: dict(n=5, est=2, pag=73, ctx="Ruta de secreción · grupo control y tres inhibidores",
             comp="Indagación", inst=i5),
     6: dict(n=6, est=3, pag=74, ctx="Gemelos y un fármaco · qué explica el modelo de colores",
             comp="Indagación", inst=i6),
     7: dict(n=7, est=3, pag=74, ctx="Gemelos y una enzima · qué fenómeno explica la diferencia",
             comp="Explicación de fenómenos", inst=i7),
     8: dict(n=8, est=1, pag=74, ctx="Glóbulos rojos sin núcleo · para qué lo pierden",
             comp="Uso comprensivo del conocimiento científico", inst=i8),
     9: dict(n=9, est=2, pag=75, ctx="Dos líneas celulares y la insulina · qué hipótesis",
             comp="Indagación", inst=i9),
     10: dict(n=10, est=2, pag=75, ctx="Insulina incompleta en el citoplasma · qué fenómeno",
              comp="Explicación de fenómenos", inst=i10)}


def build(pages=(140, 141, 143, 144, 145)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"bio1_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
