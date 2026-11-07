#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sociales y Ciudadanas · Misión 6 · componente ético-político · páginas 132–138.

Última misión del área. Libro fuente: «PRUEBA DE CAMPO MISIÓN 6» de Ciencias Sociales,
páginas 398–402. Textos: tres modelos para el debate del salario de los congresistas (1),
Constitución de 1991 y Bobbio (2 a 4), El Salvador y el «autoritarismo eficaz» (5 a 7), la
investigación al hijo del presidente (8) y la condena de primera instancia a un expresidente
en julio de 2025 (9 y 10).

Claves verificadas (resueltas a mano contra el texto del libro, no copiadas):

    1·C  2·C  3·B  4·B  5·C  6·B  7·D  8·B  9·C  10·D

Reparto: A 0 · B 4 · C 4 · D 2. La A no sale nunca. En la 6 la C también se puede defender
y en la 10 la B sigue de cerca el párrafo «sistémico» del texto: registrado, con todo lo
demás, en tablero/propuestas/soc6_hallazgos.csv.

Estrategias (la 3 y la 4 recogen lo trabajado en las misiones 1, 3 y 4 del área):
    1 · La mayoría y sus límites              (2, 3, 4  · ICFES 2016-1 2.ª sesión N.º 22)
    2 · Eficaz no es lo mismo que legítimo    (5, 6     · ICFES N.º 20)
    3 · Lo político, lo social y lo ético     (7, 10    · ICFES N.º 2)
    4 · Quién lo dice y desde qué principio   (1, 8, 9  · ICFES N.º 14)

Hojas: 132 soc6_t1 (1-2) · 133 soc6_t2 (3-4) · 134 soc6_i1 · 135 soc6_t3 (5-6) ·
       136 soc6_t4 (7-8) · 137 soc6_t5 (9-10) · 138 soc6_i2.

Nombres propios: el cuaderno no imprime los nombres de los políticos colombianos vivos que trae
el libro (preguntas 8 a 10); el estudiante los lee en su libro. Pendiente la decisión de la
Gerencia antes de imprimir.
"""
import math

from taller_base import *

configurar("Sociales y Ciudadanas", 6, "ético-político",
           tema="Lo que hace legítimo a un poder: la mayoría, los derechos y las cuentas",
           color=EDU_ORO, nota="LO QUE ANOTÉ DEL CASO")
MORADO = "#5B3E96"
EST = {1: ("La mayoría y sus límites", EDU_AZUL),
       2: ("Eficaz no es lo mismo que legítimo", EDU_ROJO),
       3: ("Lo político, lo social y lo ético", MORADO),
       4: ("Quién lo dice y desde qué principio", EDU_VERDE)}
usar_estrategias(EST)


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def frase_hueco(b, x, y, w, texto, c, h=48):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [texto], 18, INK, weight="700"))
    return y + h


def letra(b, cx, cy, L, c, r=17):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="2"/>')
    b.append(T(cx, cy + 7, [L], 16, c, weight="700", anchor="middle"))


def cita(b, x, y, w, rotulo, texto, c, size=17):
    """Fragmento del libro en fondo suave con acento vertical."""
    svg, y2 = TJ(x + 34, y + 38, texto, w - 60, size, INK, style="italic", lh=size + 8)
    hh = y2 - y + 12
    b.append(rect(x, y, w, hh, SOFT, r=10))
    b.append(rect(x, y, 8, hh, c, r=4))
    rot(b, x + 34, y + 24, rotulo, c, size=13)
    b.append(svg)
    return y + hh


# ───────── P1 · tres modelos para el salario de los congresistas ─────────
def i1(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Cada voz con su modelo: quién lo invocó y qué miraba", c,
                      "En el debate hablan tres voces y cada una se apoya en un modelo distinto. Antes de juzgar, "
                      "pon a cada voz al lado de su modelo y escribe qué mira ese modelo primero y qué le queda "
                      "por fuera en este caso.")
    x0, ww = x + 22, w - 44
    c1, c2, c3, c4 = x0, x0 + 260, x0 + 580, x0 + 900
    rot(b, c1, yy + 18, "MODELO", c)
    rot(b, c2, yy + 18, "QUIÉN LO INVOCÓ", c)
    rot(b, c3, yy + 18, "QUÉ MIRA PRIMERO", c)
    rot(b, c4, yy + 18, "QUÉ LE QUEDA POR FUERA", c)
    yy += 30
    for nom in ("utilitarista", "garantista", "desarrollo sostenible"):
        caja(b, c1, yy, 244, 66, c, fill=SOFT)
        b.append(T(c1 + 18, yy + 41, [nom], 18, c, weight="700"))
        for cx_, cw_ in ((c2, 304), (c3, 304), (c4, ww - 900)):
            caja(b, cx_, yy, cw_, 66, c)
        yy += 78
    yy += 4
    yy = frase_hueco(b, x0, yy, ww, "La medida que se discutía era ________________ y el problema de fondo era "
                                    "________________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "La pregunta pide el uso «más completo y coherente»:",
                  "pon cada opción al lado de tu última columna y pregúntate cuál se hace cargo de lo que a las "
                  "otras miradas les queda por fuera. Que una opción defienda un modelo con fuerza no la hace "
                  "más completa.", c)


# ───────── P2 · las tensiones de la democracia ─────────
def cuerda(b, x1, x2, y, c):
    """Cuerda tensa en zigzag entre dos cajas (trazo absoluto)."""
    n = 14
    pts = []
    for i in range(n + 1):
        px = x1 + (x2 - x1) * i / n
        py = y + (0 if i in (0, n) else (-9 if i % 2 else 9))
        pts.append(f"{px:.1f},{py:.1f}")
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{c}" stroke-width="3" '
             f'stroke-linejoin="round"/>')


def i2(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Las tres cuerdas que tensa Bobbio", c,
                      "Bobbio nombra tres pares de cosas que tiran en sentidos contrarios. Te damos un extremo de "
                      "cada cuerda: busca en el texto el otro. Después anota qué opciones sueltan uno de los dos "
                      "extremos.")
    x0, ww = x + 22, w - 44
    bw = 330
    for k, extremo in enumerate(("gobernabilidad", "eficacia", "la regla de la mayoría")):
        caja(b, x0, yy, bw, 60, c, fill=SOFT, r=30)
        b.append(T(x0 + bw / 2, yy + 38, [extremo], 19, c, weight="700", anchor="middle"))
        rx = x0 + bw + 230
        caja(b, rx, yy, bw, 60, c, r=30)
        pista(b, rx + 24, yy + 37, "el otro extremo:")
        cuerda(b, x0 + bw + 10, rx - 10, yy + 30, c)
        ox = rx + bw + 34
        pista(b, ox, yy + 24, "opciones que sueltan")
        pista(b, ox, yy + 44, "un extremo:")
        caja(b, ox + 160, yy + 6, ww - (ox - x0) - 160, 48, c)
        yy += 84
    yy += 4
    caja(b, x0, yy, ww, 108, c)
    rot(b, x0 + 24, yy + 30, "LA PREGUNTA CON LA QUE BOBBIO CIERRA EL TEXTO", c)
    pista(b, x0 + 24, yy + 54, "empieza con «¿cómo hacer que…?»: cópiala completa")
    renglon(b, x0 + 24, yy + 90, x0 + ww - 24)
    return yy + 108


# ───────── P3 · cómo se aplica el Estado Social de Derecho ─────────
def i3(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Cuatro fichas: la palabra clave de cada fuente", c,
                      "El texto junta tres artículos de la Constitución y un párrafo de Bobbio. Llena una ficha por "
                      "fuente: la palabra que mejor la resume y lo que le exige a una democracia.")
    x0, ww = x + 22, w - 44
    n, gap = 4, 24
    fw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("ARTÍCULO 1", "cómo es el Estado"), ("ARTÍCULO 40", "qué puede hacer el ciudadano"),
                                  ("ARTÍCULO 95", "qué le toca al ciudadano"), ("BOBBIO · 1984", "dónde está el dilema"))):
        bx = x0 + k * (fw + gap)
        caja(b, bx, yy, fw, 196, c, r=14)
        b.append(rect(bx, yy, fw, 44, _mezcla_azul(), r=14))
        b.append(rect(bx, yy + 30, fw, 14, _mezcla_azul(), r=0))
        rot(b, bx + 18, yy + 29, rt, c, size=14)
        pista(b, bx + 18, yy + 72, "palabra clave:", size=14)
        renglon(b, bx + 18, yy + 104, bx + fw - 18)
        pista(b, bx + 18, yy + 136, ps + ":", size=14)
        renglon(b, bx + 18, yy + 178, bx + fw - 18)
    yy += 214
    yy = frase_hueco(b, x0, yy, ww, "Con las cuatro fichas: un sistema es legítimo cuando ______________ "
                                    "y cuando ______________ .", c)
    yy += 16
    return ojo(b, x0, yy, ww, "CUENTA LAS FORMAS DE PARTICIPAR",
               "El artículo 40 nombra varias maneras de participar en el poder político. Cuéntalas y escribe el "
               "número en el margen. Si una opción las reduce a una sola, ya sabes qué hacer con ella.")


def _mezcla_azul():
    from taller_base import _mezcla
    return _mezcla(EST[1][1], 0.90)


# ───────── P4 · la mayoría sin límites ─────────
def i4(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "La regla sin freno: sigue el efecto en el tiempo", c,
                      "Imagina que desde mañana la mayoría puede decidir cualquier cosa, sin límites de la "
                      "Constitución. Usa lo que dice Bobbio para escribir qué pasaría en cada momento.")
    x0, ww = x + 22, w - 44
    ly = yy + 34
    b.append(line(x0 + 10, ly, x0 + ww - 40, ly, c, 4))
    b.append(f'<polygon points="{x0 + ww - 40},{ly - 12} {x0 + ww - 10},{ly} {x0 + ww - 40},{ly + 12}" '
             f'fill="{c}"/>')
    sw_ = (ww - 40) / 3
    for k, (rt, ps) in enumerate((("AL DÍA SIGUIENTE", "¿qué cambia en cómo se decide?"),
                                  ("CON LOS AÑOS", "¿qué le pasa a la confianza en las instituciones?"),
                                  ("PARA LAS MINORÍAS", "¿qué les puede hacer la mayoría?"))):
        cx = x0 + 10 + sw_ * k + sw_ / 2
        b.append(f'<circle cx="{cx:.1f}" cy="{ly}" r="14" fill="white" stroke="{c}" stroke-width="3"/>')
        bx = cx - sw_ / 2 + 10
        caja(b, bx, ly + 30, sw_ - 20, 170, c)
        rot(b, bx + 16, ly + 58, rt, c, size=14)
        svg, _ = TJ(bx + 16, ly + 84, ps, sw_ - 52, 14, GRAY, style="italic", lh=19)
        b.append(svg)
        renglon(b, bx + 16, ly + 144, bx + sw_ - 36)
        renglon(b, bx + 16, ly + 184, bx + sw_ - 36)
    yy = ly + 220
    return trampa(b, x0, yy, ww, "Dos opciones prometen que todo mejora:",
                  "si el texto dice que la democracia «se debilita cuando la mayoría, en nombre de su voluntad, "
                  "oprime a las minorías», ¿puede quitarle los límites a la mayoría y que todo salga ganando? "
                  "Pon cada opción al lado de tu línea de tiempo.", c)


# ───────── P5 · en qué se apoya el «autoritarismo eficaz» ─────────
def i5(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "El recibo del autoritarismo eficaz", c,
                      "Todo gobierno así pasa una cuenta: entrega algo y cobra algo. Llena el recibo con lo que dice "
                      "el texto. La pregunta no es si la cuenta es justa: es con qué se justifica el que la cobra.")
    x0, ww = x + 22, w - 44
    rw, rh = ww - 300, 262
    # recibo con borde de papel rasgado abajo (forma, no filete)
    pts = [f"{x0},{yy}", f"{x0 + rw},{yy}", f"{x0 + rw},{yy + rh}"]
    n = 24
    for i in range(1, n + 1):
        px = x0 + rw - rw * i / n
        py = yy + rh + (12 if i % 2 else 0)
        pts.append(f"{px:.1f},{py:.1f}")
    b.append(f'<polygon points="{" ".join(pts)}" fill="white" stroke="{c}" stroke-width="2.2"/>')
    rot(b, x0 + 24, yy + 32, "RECIBO · EL SALVADOR", c)
    half = (rw - 72) / 2
    for k, (rt, ps) in enumerate((("LO QUE ENTREGA", "lo que la gente recibe"),
                                  ("LO QUE COBRA", "el texto nombra varias cosas"))):
        bx = x0 + 24 + k * (half + 24)
        caja(b, bx, yy + 50, half, 192, c, r=8)
        rot(b, bx + 16, yy + 78, rt, c, size=14)
        pista(b, bx + 16, yy + 100, ps, size=14)
        for i in range(3):
            renglon(b, bx + 16, yy + 140 + i * 40, bx + half - 16)
    sx = x0 + rw + 30
    caja(b, sx, yy + 40, ww - rw - 30, 190, c, r=14, dash="8,6")
    rot(b, sx + 18, yy + 70, "CON QUÉ SE", c, size=14)
    rot(b, sx + 18, yy + 92, "JUSTIFICA", c, size=14)
    pista(b, sx + 18, yy + 118, "una palabra del texto", size=14)
    renglon(b, sx + 18, yy + 180, sx + ww - rw - 48)
    yy += rh + 30
    return trampa(b, x0, yy, ww, "Te piden en qué se apoya, no si está bien:",
                  "antes de elegir, pon cada opción frente a tu recibo. Lo que dice, ¿está en lo que entrega, "
                  "en lo que cobra o en ninguna de las dos columnas? Después vuelve a la casilla de la derecha.", c)


# ───────── P6 · los contrapesos ─────────
def i6(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Los contrapesos que se cayeron", c,
                      "Un Estado de Derecho se sostiene en varias columnas. Escribe en cada una lo que, según el "
                      "texto, le pasó cuando la seguridad dio resultados.")
    x0, ww = x + 22, w - 44
    bx0, bw = x0 + 40, ww - 80
    b.append(rect(bx0, yy, bw, 54, c, r=8))
    b.append(T(bx0 + bw / 2, yy + 35, ["EL PODER EJECUTIVO · ¿qué ganó?"], 18, "white", weight="700",
               anchor="middle"))
    cols = ("ASAMBLEA LEGISLATIVA", "CORTE SUPREMA", "PRENSA Y SOCIEDAD CIVIL")
    n, gap = 3, 60
    cw_ = (bw - gap * (n - 1)) / n
    for k, rt in enumerate(cols):
        cx = bx0 + k * (cw_ + gap)
        caja(b, cx, yy + 66, cw_, 196, c, r=6)
        b.append(rect(cx - 10, yy + 262, cw_ + 20, 18, c, r=4))
        rot(b, cx + cw_ / 2, yy + 96, rt, c, size=14, anchor="middle")
        pista(b, cx + cw_ / 2, yy + 120, "¿qué le pasó?", size=14, anchor="middle")
        renglon(b, cx + 18, yy + 170, cx + cw_ - 18)
        renglon(b, cx + 18, yy + 220, cx + cw_ - 18)
    yy += 300
    return alto_profe(b, x0, yy, ww,
                      "Aquí aparecen dos principios del Estado Social de Derecho: la división de poderes (que ninguna "
                      "rama mande sobre las otras y que se controlen entre sí) y el pluralismo (que quepan las voces "
                      "distintas, también las críticas). El profe explica qué quiere decir cada uno y cuál de los dos "
                      "nombra el texto cuando habla de «contrapesos».")


# ───────── P7 · consecuencias en varias dimensiones ─────────
def tri(b, cx, cy, r, c, sw=2.4, fill="white"):
    p = [(cx, cy - r), (cx + r * math.cos(math.radians(30)), cy + r / 2),
         (cx - r * math.cos(math.radians(30)), cy + r / 2)]
    b.append(f'<polygon points="{" ".join(f"{a:.1f},{bb:.1f}" for a, bb in p)}" fill="{fill}" '
             f'stroke="{c}" stroke-width="{sw}"/>')
    return p


def i7(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "El triángulo de las consecuencias", c,
                      "Lo que trabajaste en las misiones 3 y 4: un hecho tiene varias caras. Escribe en cada vértice "
                      "una consecuencia del «autoritarismo eficaz» que salga del texto. Después rellena, en el "
                      "triángulo pequeño de cada opción, los vértices que esa opción analiza de verdad.")
    x0, ww = x + 22, w - 44
    cx, cy, r = x0 + 390, yy + 200, 150
    p = tri(b, cx, cy, r, c, sw=3, fill=SOFT)
    for (px, py) in p:
        b.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="12" fill="{c}"/>')
    # una caja por vértice, unida al vértice con un trazo punteado
    cajas_v = (("LO POLÍTICO", x0 + 500, yy + 10, p[0]), ("LO SOCIAL", x0 + 560, yy + 296, p[1]),
               ("LO ÉTICO", x0, yy + 296, p[2]))
    for rt, bx, by, (px, py) in cajas_v:
        caja(b, bx, by, 226, 96, c)
        rot(b, bx + 16, by + 26, rt, c, size=14)
        renglon(b, bx + 16, by + 58, bx + 210)
        renglon(b, bx + 16, by + 86, bx + 210)
        ex = bx if bx > px else bx + 226
        b.append(line(px, py, ex, by + 48, c, 1.6, dash="4,5"))
    # triángulos pequeños por opción
    mx = x0 + 810
    rot(b, mx, yy + 24, "QUÉ VÉRTICES ANALIZA CADA OPCIÓN", c, size=14)
    pista(b, mx, yy + 46, "P político · S social · E ético", size=14)
    for k, L in enumerate("ABCD"):
        col, fila = k % 2, k // 2
        tx, ty = mx + 20 + col * 210, yy + 150 + fila * 160
        letra(b, tx, ty - 50, L, c)
        q = tri(b, tx + 100, ty + 6, 58, c, sw=2)
        for (qx, qy), et, (dx, dy) in zip(q, "PSE", ((0, -18), (24, 6), (-24, 6))):
            b.append(f'<circle cx="{qx:.1f}" cy="{qy:.1f}" r="11" fill="white" stroke="{c}" stroke-width="2"/>')
            b.append(T(qx + dx, qy + dy + 5, [et], 13, GRAY, weight="700", anchor="middle"))
    pista(b, mx, yy + 420, "rellena el círculo de cada vértice que la opción explica")
    yy += 440
    return frase_hueco(b, x0, yy, ww, "Una consecuencia que toca dos vértices a la vez: _______________________ .", c)


# ───────── P8 · perspectivas en tensión ─────────
def i8(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Mapa de voces: quién choca con quién", c,
                      "Lo de la Misión 1: quién dice qué y por qué. Escribe en cada globo lo que dice esa voz según "
                      "el texto. Después traza un rayo entre las dos voces que chocan de frente.")
    x0, ww = x + 22, w - 44
    cw_, chh = 380, 70
    ccx = x0 + ww / 2 - cw_ / 2
    cy0 = yy + 120
    caja(b, ccx, cy0, cw_, chh, c, fill=SOFT, r=35, sw=2.6)
    b.append(T(ccx + cw_ / 2, cy0 + 30, ["EL CASO"], 15, c, weight="700", ls=1.5, anchor="middle"))
    b.append(T(ccx + cw_ / 2, cy0 + 54, ["un familiar del presidente, investigado"], 16, INK, anchor="middle"))
    gw, gh = 380, 116
    voces = (("ALGUNOS SECTORES", x0, yy), ("OTROS SECTORES", x0 + ww - gw, yy),
             ("EL PRESIDENTE", x0, yy + 196), ("LA OPOSICIÓN", x0 + ww - gw, yy + 196))
    for rt, gx, gy in voces:
        caja(b, gx, gy, gw, gh, c, r=26)
        rot(b, gx + 22, gy + 30, rt, c, size=14)
        pista(b, gx + 22, gy + 52, "lo que dice:", size=14)
        renglon(b, gx + 22, gy + 96, gx + gw - 22)
        ex = gx + gw if gx == x0 else gx
        tx_ = ccx if gx == x0 else ccx + cw_
        b.append(line(ex, gy + gh / 2, tx_, cy0 + chh / 2, c, 1.8, dash="5,6"))
    yy += 196 + gh + 20
    return trampa(b, x0, yy, ww, "La pregunta dice «perspectivas en tensión», en plural:",
                  "cuenta cuántas voces mete cada opción y si esas voces se oponen entre sí o solo opina cada una "
                  "por su lado. Una sola voz, por sensata que suene, no es una tensión.", c)


# ───────── P9 · qué contradice el Estado de Derecho ─────────
def i9(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "La balanza del principio: ¿confirma o contradice?", c,
                      "Primero escribe el principio que está en juego, con palabras del texto. Después pon la letra "
                      "de cada opción en el platillo que le toca: lo que confirma el Estado de Derecho, o lo que lo "
                      "contradice.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 62, c)
    rot(b, x0 + 24, yy + 37, "EL PRINCIPIO EN JUEGO", c)
    renglon(b, x0 + 270, yy + 44, x0 + ww - 24)
    yy += 84
    mx = x0 + ww / 2
    b.append(f'<polygon points="{mx - 60},{yy + 230} {mx + 60},{yy + 230} {mx},{yy + 40}" fill="{SOFT}" '
             f'stroke="{c}" stroke-width="2.4"/>')
    b.append(line(mx - 420, yy + 40, mx + 420, yy + 40, c, 5))
    b.append(f'<circle cx="{mx}" cy="{yy + 40}" r="12" fill="{c}"/>')
    for k, (rt, sx) in enumerate((("CONFIRMA EL ESTADO DE DERECHO", -420), ("LO CONTRADICE", 420))):
        px = mx + sx
        b.append(line(px, yy + 40, px - 150, yy + 120, c, 1.8))
        b.append(line(px, yy + 40, px + 150, yy + 120, c, 1.8))
        caja(b, px - 200, yy + 120, 400, 110, c, r=40)
        rot(b, px, yy + 150, rt, c, size=14, anchor="middle")
        for j in range(4):
            caja(b, px - 150 + j * 80, yy + 166, 60, 50, c, r=8)
    yy += 250
    yy = ojo(b, x0, yy, ww, "OJO CON LA FECHA DEL TEXTO",
             "El libro cuenta el fallo de primera instancia de julio de 2025. Una decisión judicial puede "
             "cambiar cuando se apela. Responde con lo que dice el texto, y pregúntale al profe en qué va el caso.")
    yy += 14
    return frase_hueco(b, x0, yy, ww, "La pregunta pide una contradicción: busca la que va en contra de "
                                      "________________ .", c)


# ───────── P10 · las tres dimensiones de la sentencia ─────────
RECORTES = ("«fortalece la confianza ciudadana si se percibe justicia»",
            "«puede provocar reacciones de polarización»",
            "«crisis institucional si los poderes no respetan la sentencia»",
            "«debates éticos profundos sobre hasta dónde pueden llegar las sanciones»")


def i10(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Recorta el párrafo y ponle etiqueta a cada pedazo", c,
                      "El texto ya trae un párrafo «en el plano sistémico». Aquí está recortado en cuatro pedazos: "
                      "escribe en la etiqueta si cada uno es político, social o ético. Después haz lo mismo con "
                      "cada opción.")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    for k, t in enumerate(RECORTES):
        col, fila = k % 2, k // 2
        bx, by = x0 + col * (half + 24), yy + fila * 98
        caja(b, bx, by, half, 86, c, dash="8,6", r=6)
        svg, _ = TJ(bx + 18, by + 32, t, half - 180, 16, INK, style="italic", lh=22)
        b.append(svg)
        caja(b, bx + half - 140, by + 21, 124, 44, c, fill=SOFT, r=22)
        pista(b, bx + half - 78, by + 49, "etiqueta", size=13, anchor="middle")
    yy += 210
    rot(b, x0, yy + 16, "LO QUE DICE CADA OPCIÓN EN CADA DIMENSIÓN", c)
    pista(b, x0 + 500, yy + 16, "si la opción no dice nada en una dimensión, deja la raya")
    yy += 32
    cols = ("lo político", "lo social", "lo ético")
    cw_ = (ww - 70) / 3
    for k, L in enumerate("ABCD"):
        ry = yy + k * 56
        letra(b, x0 + 20, ry + 24, L, c)
        for j, lab in enumerate(cols):
            bx = x0 + 50 + j * (cw_ + 10)
            caja(b, bx, ry, cw_, 46, c, r=8)
            pista(b, bx + 14, ry + 29, lab + ":", size=14)
    return yy + 4 * 56


Q = {1: dict(n=1, est=4, pag=398, ctx="Salario de los congresistas · tres modelos para un mismo debate",
             comp="Pensamiento reflexivo y sistémico", inst=i1),
     2: dict(n=2, est=1, pag=399, ctx="Constitución de 1991 y Bobbio · las tensiones de la democracia",
             comp="Interpretación de perspectivas", inst=i2),
     3: dict(n=3, est=1, pag=399, ctx="Constitución de 1991 y Bobbio · cómo se aplica el Estado de Derecho",
             comp="Pensamiento social", inst=i3),
     4: dict(n=4, est=1, pag=399, ctx="Constitución de 1991 y Bobbio · la mayoría sin límites",
             comp="Pensamiento reflexivo y sistémico", inst=i4),
     5: dict(n=5, est=2, pag=400, ctx="El Salvador · en qué se apoya un «autoritarismo eficaz»",
             comp="Interpretación de perspectivas", inst=i5),
     6: dict(n=6, est=2, pag=400, ctx="El Salvador · la seguridad frente al Estado Social de Derecho",
             comp="Pensamiento social", inst=i6),
     7: dict(n=7, est=3, pag=401, ctx="El Salvador · las consecuencias del «autoritarismo eficaz»",
             comp="Pensamiento reflexivo y sistémico", inst=i7),
     8: dict(n=8, est=4, pag=401, ctx="El hijo del presidente, investigado (2023) · las voces del debate",
             comp="Interpretación de perspectivas", inst=i8),
     9: dict(n=9, est=4, pag=402, ctx="La condena a un expresidente (2025) · el Estado de Derecho",
             comp="Pensamiento social", inst=i9),
     10: dict(n=10, est=3, pag=402, ctx="La condena a un expresidente (2025) · política, sociedad y ética",
              comp="Pensamiento reflexivo y sistémico", inst=i10)}


def build(pages=(132, 133, 135, 136, 137)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"soc6_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
