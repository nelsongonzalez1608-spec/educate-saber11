#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 5 · Parte 6 del ICFES · componente lectura · páginas 321–330.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 5» de Inglés (fuente_libro/INGLÉS), páginas 456–459.
Comprensión inferencial: leer lo que el texto deja entender. Dos textos: «Why Photosynthesis
Matters» (Bloque 1, ocho preguntas) y «The Power of Street Music» (Bloque 2, ocho preguntas).

Decisión de Nelson (7 nov): el cuaderno trabaja TODAS las preguntas del libro, una tarjeta por
pregunta. El libro numera 1 a 8 en cada bloque; el cuaderno numera 1 a 16 y cada tarjeta dice
«Bloque k, n.º j del libro».

Estrategia de la Parte 6 (va en la cabecera): leer entre líneas, con la prueba en la mano. Lo que
se infiere tiene que poder señalarse en una frase del texto.

Claves verificadas (resueltas a mano contra el texto del libro, no copiadas; 7 nov 2026):

    cuaderno   libro       clave
     1         B1 n.º 1    C   el equilibrio de procesos biológicos («Without this process… could not survive»)
     2         B1 n.º 2    A   la energía viene del sol y pasa de un ser a otro («originally came from the sun»)
     3         B1 n.º 3    D   lo local altera lo global («directly affect… the stability of our climate»)
     4         B1 n.º 4    B   conservar = estrategia esencial para nuestra supervivencia («protecting our own future»)
     5         B1 n.º 5    C   «foundation»: soporte cuya ruptura arrastra al ecosistema
     6         B1 n.º 6    A   el contraste es con una atmósfera posible e invivible («would quickly become toxic»)
     7         B1 n.º 7    D   la amenaza está en la vida diaria, no solo lejos («In cities, air pollution…»)
     8         B1 n.º 8    B   los techos verdes meten procesos ecológicos en la ciudad construida
     9         B2 n.º 1    D   el andén roto se vuelve lugar de expresión
    10         B2 n.º 2    A   experiencias humanas compartidas y breves («For a brief instant»)
    11         B2 n.º 3    A   la cultura vive en lo cotidiano («art belongs only to theaters or museums»)
    12         B2 n.º 4    B   afirmarse contra el anonimato («visibility and dignity»)
    13         B2 n.º 5    D   vitalidad cultural desafiante frente a la indiferencia de la ciudad
    14         B2 n.º 6    C   conexión con historias culturales profundas («echoes of African heritage», «shared roots»)
    15         B2 n.º 7    B   la queja es un contraargumento que se supera («Others, however…»)
    16         B2 n.º 8    A   del anonimato caótico a la conexión con sentido

    En orden: 1·C 2·A 3·D 4·B 5·C 6·A 7·D 8·B 9·D 10·A 11·A 12·B 13·D 14·C 15·B 16·A

  4 · B (B1 n.º 4): «Protecting plants is not only about saving nature: it is about protecting our own
      future»: la conservación pasa de ser un favor a la naturaleza a ser algo que nos conviene para
      sobrevivir. A («exclusively… non-human species») es el marco viejo; C (opcional, recreativo) y D
      (una carga económica) no están en el texto.
  8 · B (B1 n.º 8): árboles, techos verdes y parques locales: los procesos de las plantas entran a la
      ciudad. A (lejos antes que lo local) lo contradice; C (políticas nacionales) no está; D (simbólico e
      ineficaz) lo niega «but together they can improve air quality».
 10 · A (B2 n.º 2): «For a brief instant», «Pedestrians slow down, a few smile, and someone even records the
      moment»: breve y compartido. B, C y D no salen del párrafo.
 11 · A (B2 n.º 3): «They challenge the idea that art belongs only to theaters or museums»: el arte vive
      también en la calle. B exagera (el autor no dice que los museos sobren); C y D no están.
 13 · D (B2 n.º 5): «resilient, creative, and unwilling to let silence define their cities»: resistir al
      silencio de la ciudad apurada del primer párrafo. A, B y C no son lo que dice esa frase.
 14 · C (B2 n.º 6): «echoes of African heritage», «salsa's heartbeat», «remind them of their shared roots».
      A (solo jóvenes), B (competencia) y D (rechazo del arte tradicional) no están.
  Las otras diez (1, 2, 3, 5, 6, 7, 9, 12, 15, 16) están explicadas en la versión anterior de este módulo
  (git) y se volvieron a verificar al rehacer cada tarjeta.

Reparto de las 16: A 5 · B 4 · C 3 · D 4. Bloque 1: C A D B C A D B (patrón que se repite cada cuatro).
Atención (hallazgo): en casi todas las preguntas los distractores cierran con absolutos («exclusively»,
«completely», «inherently», «all») y la correcta es la única que matiza. El cuaderno no lo enseña como truco:
la pregunta 14 enseña a tratar la palabra fuerte como una alarma que se comprueba en el texto, y la 11
muestra al autor peleando contra un «only» del propio texto.

Subestrategias (las cuatro de la Parte 6):
    1 · Lo que el texto deja entender          (1, 2, 3, 8, 10   · ICFES QA)   azul
    2 · Para qué lo pone el autor              (7, 9, 14, 15     · ICFES QB)   rojo
    3 · La frase que dice más de lo que dice   (5, 12, 13        · ICFES QC)   oro
    4 · Dos cosas frente a frente              (4, 6, 11, 16     · ICFES QD)   morado

Hojas: 321 t1 (1-2) · 322 t2 (3-4) · 323 t3 (5-6) · 324 t4 (7-8) · 325 ing5_i1 ·
       326 t5 (9-10) · 327 t6 (11-12) · 328 t7 (13-14) · 329 t8 (15-16) · 330 ing5_i2.
"""
from taller_base import *

configurar("Inglés", 5, "lectura",
           tema="Parte 6 · Leer entre líneas, con la prueba en la mano",
           nota="LO QUE SUBRAYÉ EN EL TEXTO", prefijo="Subestrategia", n_hojas=8)
MORADO = "#5B3E96"
EST = {1: ("Lo que el texto deja entender", EDU_AZUL),
       2: ("Para qué lo pone el autor", EDU_ROJO),
       3: ("La frase que dice más de lo que dice", EDU_ORO),
       4: ("Dos cosas frente a frente", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))


# ───────── piezas pequeñas (las usa también ing5_icfes.py) ─────────
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


def parrafo(b, x, y, w, txt, size=17, color=INK, style="normal", weight="400", lh=None):
    svg, yy = TJ(x, y, txt, w, size, color, weight=weight, style=style, lh=lh or size + 8)
    b.append(svg)
    return yy


def cita(b, x, y, w, txt, c, rotulo=None, size=18):
    """Fragmento en inglés tal como está en el libro: recuadro tinte con acento vertical."""
    yy0 = y + (34 if rotulo else 16)
    svg, yy = TJ(x + 26, yy0, txt, w - 50, size, INK, style="italic", lh=size + 8)
    h = yy - y + 14
    caja(b, x, y, w, h, tinte(c, 0.86), fill=tinte(c, 0.95), r=12)
    b.append(rect(x, y, 7, h, c, r=3))
    if rotulo:
        rot(b, x + 26, y + 24, rotulo, c, size=13)
    b.append(svg)
    return y + h


def renglones(b, x, y, w, n, step=46):
    for k in range(n):
        renglon(b, x, y + k * step, x + w)
    return y + (n - 1) * step


def tabla_vacia(b, x, y, cols, heads, filas, c, rh=58, hh=46, size=16, sin_renglon=()):
    """Tabla con encabezado tinte (la usan las hojas ICFES de esta misión; el taller ya no)."""
    ww = sum(cols)
    caja(b, x, y, ww, hh, c, fill=tinte(c), r=8)
    cx = x
    for k, hd in enumerate(heads):
        if hd:
            rot(b, cx + 14, y + hh / 2 + 6, hd, c, size=13)
        cx += cols[k]
    ry = y + hh
    for f in filas:
        caja(b, x, ry, ww, rh, c, r=0)
        lineas = f if isinstance(f, (list, tuple)) else [f]
        ty = ry + rh / 2 + 6 - (len(lineas) - 1) * 10
        for j, ln in enumerate(lineas):
            texto(b, x + 14, ty + j * 21, ln, size=size, weight="700" if j == 0 else "400",
                  style="normal" if j == 0 else "italic", color=INK if j == 0 else GRAY)
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


def casillas(b, x, y, labels, c, gap=None, size=15):
    """Casillas en fila con su rótulo. gap fijo o medido con tw()."""
    cx = x
    for lab in labels:
        b.append(checkbox(cx, y, s=10, c=c))
        texto(b, cx + 28, y + 17, lab, size=size, color=GRAY)
        cx += gap if gap else tw(lab, size) + 70


def hueco_ingles(b, x, y, w, c):
    """Recuadro de dos pisos: la palabra en inglés / lo que quiere decir."""
    caja(b, x, y, w, 96, c, r=10)
    pista(b, x + 12, y + 34, "en inglés:", size=14)
    renglon(b, x + 90, y + 38, x + w - 12)
    pista(b, x + 12, y + 80, "quiere decir:", size=14)
    renglon(b, x + 108, y + 84, x + w - 12)


def _mezcla_dos(c1, c2, k):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    d = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(p + (q - p) * k):02X}" for p, q in zip(a, d))


# ═════════════════════════ BLOQUE 1 · Why Photosynthesis Matters ═════════════════════════

# ───────── 1 · B1 n.º 1 · de qué depende la existencia humana ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Quita una pieza y mira qué se cae", c,
                      "Lo que el texto deja entender se prueba con una frase. El texto no dice «los humanos dependen "
                      "de…»: lo deja ver con oraciones del tipo «sin esto, pasa aquello». En cada ficha copia, en "
                      "inglés, lo que el texto dice que pasaría si esa pieza faltara.")
    x0, ww = x + 22, w - 44
    n, gap, baja = 4, 40, 26
    fw = (ww - gap * (n - 1)) / n
    fh = 270
    piezas = (("las plantas", "(no hay fotosíntesis)"), ("el oxígeno", "(el aire que respiramos)"),
              ("la energía del sol", "(la guardada en azúcares)"), ("los bosques", "(talados o enfermos)"))
    for k, (p, sub) in enumerate(piezas):
        fx, fy = x0 + k * (fw + gap), yy + k * baja
        caja(b, fx, fy, fw, fh, c, r=18, sw=2.4)
        b.append(rect(fx + 1.2, fy + 1.2, fw - 2.4, 92, tinte(c, 0.9), r=17))
        for dx in (-26, 0, 26):
            b.append(f'<circle cx="{fx + fw - 40 + dx / 2:.1f}" cy="{fy + 24 + (dx + 26) / 2.6:.1f}" r="5" '
                     f'fill="{c}"/>')
        rot(b, fx + 16, fy + 30, "SI FALTA…", c, size=13)
        texto(b, fx + 16, fy + 60, p, size=18, weight="700")
        pista(b, fx + 16, fy + 82, sub, size=14)
        pista(b, fx + 16, fy + 122, "lo que pasa, en inglés:", size=14)
        for j in range(3):
            renglon(b, fx + 16, fy + 160 + j * 36, fx + fw - 16)
        pista(b, fx + 16, fy + 256, "párrafo n.º ____", size=14)
        if k < n - 1:
            flecha(b, fx + fw + 4, fy + 150, fx + fw + gap - 4, fy + 150 + baja, c, head=9)
    yy += fh + baja * (n - 1) + 22
    caja(b, x0, yy, ww, 130, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE SOSTIENE TODO", c)
    pista(b, x0 + 20, yy + 60, "las cuatro fichas caen por la misma razón; escríbela en mis palabras, sin copiar ninguna opción:")
    renglones(b, x0 + 20, yy + 100, ww - 40, 1)
    yy += 148
    return trampa(b, x0, yy, ww, "Una opción puede ser cierta en el mundo y no estar en el texto:",
                  "«implies» quiere decir que el texto lo deja ver, no que tú lo sepas por otro lado. Antes de "
                  "marcar, busca la ficha que sostiene la opción. Si no hay ninguna, esa opción habla de otra "
                  "lectura.", c)


# ───────── 2 · B1 n.º 2 · de dónde viene la energía ─────────
def i2(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Sigue la energía de mano en mano", c,
                      "Inferir también es seguir un recorrido. El segundo párrafo cuenta un viaje: llena cada estación "
                      "con quién tiene la energía en ese momento y, debajo, marca si ese ser la fabrica o la recibe de "
                      "la estación anterior.")
    x0, ww = x + 22, w - 44
    n = 4
    gap = 46
    sw_ = (ww - gap * (n - 1)) / n
    pasos = ("PUNTO DE PARTIDA", "LA GUARDA PRIMERO", "LA RECIBE", "LA RECIBE DESPUÉS")
    for k, p in enumerate(pasos):
        bx = x0 + k * (sw_ + gap)
        caja(b, bx, yy, sw_, 200, c, r=16, sw=2.4)
        rot(b, bx + 18, yy + 30, p, c, size=13)
        pista(b, bx + 18, yy + 62, "¿quién o qué?")
        renglon(b, bx + 18, yy + 104, bx + sw_ - 18)
        for j, lab in enumerate(("la fabrica", "la recibe")):
            b.append(checkbox(bx + 18, yy + 128 + j * 34, s=10, c=c))
            texto(b, bx + 46, yy + 145 + j * 34, lab, size=15, color=GRAY)
        if k < n - 1:
            flecha(b, bx + sw_ + 6, yy + 100, bx + sw_ + gap - 6, yy + 100, c, head=10)
    yy += 226
    caja(b, x0, yy, ww, 228, c, r=14)
    rot(b, x0 + 20, yy + 30, "LAS PALABRAS QUE MUEVEN LA ENERGÍA", c)
    parrafo(b, x0 + 20, yy + 44, ww - 40,
            "En el párrafo 2 hay tres verbos o frases que dicen hacia dónde va la energía. Búscalos y cópialos "
            "en inglés, tal como están; al lado, escribe qué quiere decir cada uno.", size=16, color=GRAY,
            style="italic")
    tw3 = (ww - 80) / 3
    for k in range(3):
        bx = x0 + 20 + k * (tw3 + 20)
        hueco_ingles(b, bx, yy + 112, tw3, c)
    yy += 246
    return ojo(b, x0, yy, ww, "ORIGINALLY = AL PRINCIPIO, EN SU ORIGEN",
               "Cuando un texto dice que algo «originally came from» un lugar, te está contando dónde empezó, no "
               "dónde está ahora. Fíjate qué ser aparece como el primero de la cadena y cuál es el último.")


# ───────── 3 · B1 n.º 3 · lo local y lo global ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Del árbol talado al clima de todos", c,
                      "Lo que el texto deja entender a veces es una distancia. Cada daño del tercer párrafo empieza en "
                      "un lugar pequeño: traza una flecha desde cada efecto hasta el círculo más lejano al que llega, "
                      "según el texto.")
    x0, ww = x + 22, w - 44
    cx, cy = x0 + 250, yy + 236
    for r_, lab, k in ((228, "EL PLANETA", 0.96), (152, "LA CIUDAD", 0.92), (76, "EL LUGAR", 0.86)):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r_}" fill="{tinte(c, k)}" stroke="{c}" stroke-width="2"/>')
        rot(b, cx, cy - r_ + 26, lab, c, size=13, anchor="middle")
    pista(b, cx, cy + 6, "el bosque", anchor="middle")
    pista(b, cx, cy + 26, "que se tala", anchor="middle")
    rx = x0 + 600
    efectos = ("less oxygen", "fewer natural resources", "damaged leaves", "the quality of the air we breathe",
               "the stability of our climate")
    ey = yy + 14
    for e in efectos:
        ew = tw(e, 17, "700", "italic") + 44
        caja(b, rx, ey, ew, 52, c, r=26, fill=tinte(c, 0.95))
        texto(b, rx + 22, ey + 33, e, size=17, weight="700", style="italic")
        b.append(f'<circle cx="{rx - 14}" cy="{ey + 26}" r="6" fill="white" stroke="{c}" stroke-width="2"/>')
        ey += 74
    pista(b, rx, ey + 10, "la flecha sale del punto de cada efecto; si llega a varios círculos, al más grande")
    yy = max(cy + 228, ey + 20) + 22
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PALABRA «BUT» CORRIGE UNA IDEA", c)
    texto(b, x0 + 20, yy + 64, "These problems may seem distant, but they directly affect…", size=18, style="italic",
          weight="700")
    pista(b, x0 + 20, yy + 100, "lo que el lector podría creer (antes del «but»):")
    renglon(b, x0 + 360, yy + 102, x0 + ww - 20)
    pista(b, x0 + 20, yy + 136, "lo que el autor afirma (después del «but»):")
    renglon(b, x0 + 340, yy + 138, x0 + ww - 20)
    return yy + 150


# ───────── 4 · B1 n.º 4 · «protecting our own future» ─────────
def marco_cuadro(b, x, y, w, h, c):
    """Marco de cuadro: borde grueso, filo interior y cuatro esquinas."""
    b.append(rect(x, y, w, h, tinte(c, 0.88), r=6, stroke=c, sw=3))
    b.append(rect(x + 18, y + 18, w - 36, h - 36, "white", r=3, stroke=c, sw=1.6))
    for px, py in ((x, y), (x + w, y), (x, y + h), (x + w, y + h)):
        b.append(f'<circle cx="{px}" cy="{py}" r="7" fill="{c}"/>')


def i4(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Dos marcos para el mismo cuadro", c,
                      "Dos cosas frente a frente: la última oración pone la misma acción, proteger las plantas, en dos "
                      "marcos distintos, separados por los dos puntos. «Reframe» es cambiarle el marco. Llena cada "
                      "cuadro y mira qué cambió.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "Protecting plants is not only about saving nature: it is about protecting our own future.",
              c, rotulo="LA ÚLTIMA ORACIÓN DEL TEXTO", size=18)
    yy += 22
    fw, fh = (ww - 130) / 2, 300
    for k, (tit, frase) in enumerate((("EL MARCO DE ANTES", "«not only about saving nature»"),
                                      ("EL MARCO NUEVO", "«protecting our own future»"))):
        fx = x0 + k * (fw + 130)
        marco_cuadro(b, fx, yy, fw, fh, c)
        rot(b, fx + 40, yy + 52, tit, c, size=13)
        texto(b, fx + 40, yy + 82, frase, size=17, style="italic", weight="700")
        pista(b, fx + 40, yy + 122, "¿a quién se protege?")
        renglon(b, fx + 40, yy + 156, fx + fw - 40)
        pista(b, fx + 40, yy + 196, "¿quién gana si se hace?")
        renglon(b, fx + 40, yy + 230, fx + fw - 40)
        renglon(b, fx + 40, yy + 266, fx + fw - 40)
    mx = x0 + fw + 65
    flecha(b, mx - 44, yy + fh / 2, mx + 44, yy + fh / 2, c, sw=3, head=14, bend=-0.4)
    texto(b, mx, yy + fh / 2 + 52, "reframe", size=17, style="italic", weight="700", color=c, anchor="middle")
    yy += fh + 22
    caja(b, x0, yy, ww, 130, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "«FOR THIS REASON»: ¿CUÁL RAZÓN?", c)
    pista(b, x0 + 20, yy + 60, "el último párrafo empieza con «For this reason»; la razón está en el párrafo 3. En mis palabras:")
    renglon(b, x0 + 20, yy + 104, x0 + ww - 20)
    yy += 148
    return ojo(b, x0, yy, ww, "LA PREGUNTA PIDE EL MARCO NUEVO",
               "«Reframes… as» pregunta en qué se convierte la conservación después de los dos puntos. Una opción "
               "que describa solo el marco de antes se queda a mitad de la oración.")


# ───────── 5 · B1 n.º 5 · «foundation» ─────────
def i5(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "«Foundation» es una palabra de albañil", c,
                      "La frase que dice más de lo que dice se entiende llevándola a su mundo. En construcción, la "
                      "«foundation» es lo que va debajo de todo. Pon en cada piso quién vive del ecosistema y piensa "
                      "qué pasa si se cae la base.")
    x0, ww = x + 22, w - 44
    bx, bw = x0, 560
    pisos = ("PISO 3", "PISO 2", "PISO 1")
    py = yy + 4
    for k, p in enumerate(pisos):
        caja(b, bx + 40, py, bw - 80, 88, c, r=6)
        rot(b, bx + 56, py + 26, p, c, size=12)
        pista(b, bx + 56, py + 56, "¿quién está aquí?")
        renglon(b, bx + 200, py + 60, bx + bw - 56)
        py += 96
    b.append(rect(bx, py, bw, 96, tinte(c, 0.82), r=6, stroke=c, sw=2.6))
    rot(b, bx + 20, py + 30, "FOUNDATION", c, size=14)
    pista(b, bx + 20, py + 62, "¿qué proceso es la base?")
    renglon(b, bx + 210, py + 66, bx + bw - 20)
    py += 96
    rx, rw = x0 + bw + 40, ww - bw - 40
    preg = (("SI SE QUITA UN PISO DE ARRIBA…", "¿el edificio sigue en pie?"),
            ("SI SE DAÑA LA BASE…", "¿qué le pasa a todo lo de arriba?"),
            ("«ALMOST EVERY ECOSYSTEM»", "¿qué cambia la palabra «almost»?"))
    qy = yy + 4
    for t1, t2 in preg:
        caja(b, rx, qy, rw, 122, c, r=14)
        rot(b, rx + 18, qy + 28, t1, c, size=13)
        pista(b, rx + 18, qy + 56, t2)
        renglon(b, rx + 18, qy + 98, rx + rw - 18)
        qy += 134
    yy = max(py, qy) + 18
    caja(b, x0, yy, ww, 110, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "LA METÁFORA EN UNA LÍNEA", c)
    pista(b, x0 + 20, yy + 64, "llamar «foundation» a la fotosíntesis es decir que, si ella falla…")
    renglon(b, x0 + 20, yy + 96, x0 + ww - 20)
    return yy + 110


# ───────── 6 · B1 n.º 6 · la atmósfera de hoy frente a otra ─────────
def i6(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El termómetro del aire: respirable o tóxico", c,
                      "Dos cosas frente a frente: el texto no habla de dos planetas, habla de este aire y de otro que "
                      "podría existir. Ubica las dos situaciones en la barra y fíjate en el verbo que usa el autor para "
                      "la segunda.")
    x0, ww = x + 22, w - 44
    gx, gy, gw = x0 + 40, yy + 74, ww - 80
    n = 6
    for k in range(n):
        col = _mezcla_dos("#30843C", "#A82424", k / (n - 1))
        b.append(rect(gx + k * gw / n, gy, gw / n, 38, tinte(col, 0.55), r=0))
    caja(b, gx, gy, gw, 38, INK, fill="none", r=6, sw=2)
    texto(b, gx, gy - 14, "breathable", size=17, weight="700", style="italic", color="#30843C")
    texto(b, gx + gw, gy - 14, "toxic", size=17, weight="700", style="italic", color="#A82424", anchor="end")
    pista(b, gx + gw / 2, gy - 14, "dibuja una flecha para A (hoy) y otra para B (sin fotosíntesis)", anchor="middle")
    yy = gy + 66
    half = (ww - 30) / 2
    for k, (tit, ps) in enumerate((("A · EL AIRE DE HOY", "lo que lo mantiene así:"),
                                   ("B · EL AIRE SIN FOTOSÍNTESIS", "quién podría vivir en él:"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 190, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        pista(b, bx + 18, yy + 62, "copia la palabra del texto que lo describe:")
        renglon(b, bx + 18, yy + 98, bx + half - 18)
        pista(b, bx + 18, yy + 134, ps)
        renglon(b, bx + 18, yy + 172, bx + half - 18)
    yy += 210
    caja(b, x0, yy, ww, 170, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL VERBO DE LA SEGUNDA SITUACIÓN", c)
    texto(b, x0 + 20, yy + 66, "Without this process, the atmosphere would quickly become toxic…", size=18,
          style="italic", weight="700")
    pista(b, x0 + 20, yy + 102, "«would» en esta oración presenta algo que…")
    casillas(b, x0 + 20, yy + 120, ("ya pasó y está probado", "no pasa hoy, pero podría pasar",
                                    "pasa hoy en otro lugar"), c, gap=370)
    yy += 188
    return ojo(b, x0, yy, ww, "FRENTE A QUÉ SE COMPARA",
               "Cuando una pregunta dice «contrasts… with», busca el segundo término en el texto. Si una opción "
               "trae un lugar o un tiempo que el texto nunca nombra, el contraste no es ese.")


# ───────── 7 · B1 n.º 7 · la contaminación en las hojas de la ciudad ─────────
def pin(b, cx, cy, c, r=26):
    """Alfiler de mapa: círculo con punta hacia abajo."""
    b.append(f'<polygon points="{cx - r * 0.8:.1f},{cy + r * 0.5:.1f} {cx + r * 0.8:.1f},{cy + r * 0.5:.1f} '
             f'{cx},{cy + r * 2.1:.1f}" fill="{c}"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.42:.1f}" fill="white"/>')


def i7(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La cabeza del lector antes y después del ejemplo", c,
                      "Para qué lo pone el autor: un ejemplo se escoge para mover lo que piensa el lector. Escribe qué "
                      "pensaría quien leyera solo lo de los bosques talados, y qué piensa después de leer lo de los "
                      "árboles de la ciudad.")
    x0, ww = x + 22, w - 44
    half = (ww - 90) / 2
    for k, (tit, ps) in enumerate((("SOLO CON LOS BOSQUES", "«Forests cut down for farming or construction…»"),
                                   ("CON EL EJEMPLO DE LA CIUDAD", "«In cities, air pollution can damage the leaves…»"))):
        bx = x0 + k * (half + 90)
        b.append(f'<ellipse cx="{bx + half / 2}" cy="{yy + 150}" rx="{half / 2}" ry="140" fill="white" '
                 f'stroke="{c}" stroke-width="2.2"/>')
        for dx, dy, r_ in ((60, 300, 16), (34, 334, 10)):
            b.append(f'<circle cx="{bx + dx}" cy="{yy + dy}" r="{r_}" fill="white" stroke="{c}" stroke-width="2"/>')
        rot(b, bx + half / 2, yy + 52, tit, c, size=13, anchor="middle")
        pista(b, bx + half / 2, yy + 80, ps, size=14, anchor="middle")
        pista(b, bx + 70, yy + 120, "el lector piensa que el problema está…")
        renglon(b, bx + 70, yy + 160, bx + half - 70)
        renglon(b, bx + 70, yy + 200, bx + half - 70)
        renglon(b, bx + 110, yy + 240, bx + half - 110)
    flecha(b, x0 + half + 14, yy + 150, x0 + half + 76, yy + 150, c, head=12)
    yy += 360
    for k, (tit, q1) in enumerate((("EL BOSQUE TALADO", "¿dónde queda?"), ("EL ÁRBOL DE MI CALLE", "¿dónde queda?"))):
        bx = x0 + k * (half + 90)
        pin(b, bx + 30, yy + 30, tinte(c, 0.35) if k == 0 else c)
        rot(b, bx + 76, yy + 22, tit, c, size=13)
        pista(b, bx + 76, yy + 50, q1)
        renglon(b, bx + 190, yy + 54, bx + half)
        pista(b, bx + 76, yy + 88, "¿quién lo ve todos los días?")
        renglon(b, bx + 290, yy + 92, bx + half)
    yy += 118
    caja(b, x0, yy, ww, 104, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "PARA QUÉ LO PUSO", c)
    pista(b, x0 + 20, yy + 62, "el autor menciona las hojas de los árboles de la ciudad para que yo entienda que…")
    renglon(b, x0 + 20, yy + 92, x0 + ww - 20)
    return yy + 104


# ───────── 8 · B1 n.º 8 · «green roofs» ─────────
def arbolito(b, cx, by, s, c):
    b.append(rect(cx - s * 0.12, by - s * 0.45, s * 0.24, s * 0.45, "#8A6A4A", r=2))
    b.append(f'<polygon points="{cx - s * 0.5:.1f},{by - s * 0.4:.1f} {cx + s * 0.5:.1f},{by - s * 0.4:.1f} '
             f'{cx},{by - s * 1.3:.1f}" fill="{c}"/>')


def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dónde se siembra cada solución", c,
                      "Lo que el texto deja entender también está en dónde pone las cosas. El último párrafo propone "
                      "tres proyectos: escribe 1, 2 y 3 en el dibujo, en el lugar donde va cada uno, y después piensa "
                      "qué hace allí cada proyecto.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "…many schools and communities promote projects such as (1) planting trees, (2) creating "
                             "green roofs, or (3) protecting local parks.", c, rotulo="EL PÁRRAFO 4, CON NÚMEROS", size=17)
    yy += 18
    sh = 300
    caja(b, x0, yy, ww, sh, c, r=16, fill=tinte(c, 0.97))
    suelo = yy + sh - 60
    b.append(rect(x0 + 20, suelo, 760, 40, "#E6E9EF", r=4))
    pista(b, x0 + 400, suelo + 27, "la calle", anchor="middle")
    for k, (bx, bw_, bh) in enumerate(((x0 + 40, 150, 150), (x0 + 220, 130, 110), (x0 + 380, 170, 170))):
        b.append(rect(bx, suelo - bh, bw_, bh, "white", r=3, stroke=GRAY, sw=1.8))
        b.append(rect(bx - 6, suelo - bh - 16, bw_ + 12, 16, "white", r=3, stroke=c, sw=2, dash="6,4"))
        for wy in range(int(suelo - bh + 22), int(suelo - 20), 44):
            for wx in range(int(bx + 18), int(bx + bw_ - 30), 42):
                b.append(rect(wx, wy, 22, 24, "#EEF0F4", r=2))
    px = x0 + 590
    b.append(rect(px, suelo - 70, 180, 70, "white", r=10, stroke=GRAY, sw=1.8, dash="6,4"))
    pista(b, px + 90, suelo - 30, "un parque", anchor="middle")
    lx = x0 + 830
    b.append(line(lx, yy + 30, lx, yy + sh - 30, "#C9CED6", 2, dash="6,6"))
    for k in range(5):
        arbolito(b, lx + 90 + k * 64, suelo + 30 - (k % 2) * 16, 70, tinte(EDU_VERDE, 0.25))
    pista(b, lx + 220, yy + 40, "un bosque lejano", anchor="middle")
    pista(b, lx + 220, yy + 62, "(donde no vive nadie)", anchor="middle")
    pista(b, x0 + 400, yy + 32, "la ciudad: los techos punteados están vacíos", anchor="middle")
    yy += sh + 20
    half = (ww - 30) / 2
    caja(b, x0, yy, half, 170, c, r=14)
    rot(b, x0 + 18, yy + 30, "UN TECHO VERDE HACE EL TRABAJO DE…", c, size=13)
    pista(b, x0 + 18, yy + 62, "¿qué proceso del párrafo 1 pasa ahora encima de un edificio?")
    renglon(b, x0 + 18, yy + 104, x0 + half - 18)
    renglon(b, x0 + 18, yy + 146, x0 + half - 18)
    bx = x0 + half + 30
    caja(b, bx, yy, half, 170, c, r=14)
    rot(b, bx + 18, yy + 30, "LO PEQUEÑO QUE SUMA", c, size=13)
    texto(b, bx + 18, yy + 62, "These actions may look small, but together they…", size=16, style="italic", weight="700")
    pista(b, bx + 18, yy + 94, "copia lo que logran juntas:")
    renglon(b, bx + 18, yy + 132, bx + half - 18)
    return yy + 170


# ═════════════════════════ BLOQUE 2 · The Power of Street Music ═════════════════════════

# ───────── 9 · B2 n.º 1 · «a cracked sidewalk» ─────────
def i9(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La misma esquina, con y sin guitarra", c,
                      "Para qué lo pone el autor: el primer párrafo describe el mismo lugar dos veces, antes y después "
                      "de las primeras notas. Mira solo la esquina, no a la gente: qué hay en ella y en qué se "
                      "convierte. Después decide para qué sirve el detalle del andén roto.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (tit, marca, prom) in enumerate((
            ("ANTES DE LA MÚSICA", "At first…", ("lo que hay en la esquina:", "lo que NO hay:", "para qué sirve ese lugar:")),
            ("CUANDO SUENA EL BOLERO", "But when…", ("lo que hay en la esquina:", "lo que se le agregó:",
                                                    "en qué se convirtió el lugar:")))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 330, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        texto(b, bx + half - 18, yy + 30, marca, size=16, style="italic", weight="700", color=c, anchor="end")
        b.append(rect(bx + 18, yy + 276, half - 36, 34, "#EEF0F4", r=4, stroke=GRAY, sw=1.6))
        b.append(f'<polyline points="{bx + 90},{yy + 276} {bx + 104},{yy + 288} {bx + 96},{yy + 298} '
                 f'{bx + 112},{yy + 310}" fill="none" stroke="{GRAY}" stroke-width="1.8"/>')
        for j, ps in enumerate(prom):
            pista(b, bx + 18, yy + 70 + j * 64, ps)
            renglon(b, bx + 18 + tw(ps, 15, style="italic") + 12, yy + 74 + j * 64, bx + half - 18)
            renglon(b, bx + 18, yy + 102 + j * 64, bx + half - 18)
    yy += 350
    caja(b, x0, yy, ww, 170, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PALABRA «JUST»", c)
    texto(b, x0 + 20, yy + 64, "He doesn't have a stage, just a cracked sidewalk and the shade of a mango tree.",
          size=18, style="italic", weight="700")
    pista(b, x0 + 20, yy + 100, "aquí «just» quiere decir:")
    casillas(b, x0 + 240, yy + 84, ("solo, nada más", "justo, exacto", "con justicia"), c, gap=250)
    pista(b, x0 + 20, yy + 142, "con tan poco, ¿qué logra el músico en esa esquina?")
    renglon(b, x0 + 380, yy + 144, x0 + ww - 20)
    yy += 188
    return trampa(b, x0, yy, ww, "El detalle no siempre es una queja:",
                  "un andén roto podría servir para criticar la ciudad, pero pregúntate qué pasa en ese mismo "
                  "andén unas líneas después. Lo que el autor quiere mostrar está en el cambio, "
                  "no en la grieta.", c)


# ───────── 10 · B2 n.º 2 · de «hurrying past» a sonreír ─────────
def i10(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Cuadro por cuadro: los peatones", c,
                      "Lo que el texto deja entender se ve en lo que hace la gente. Ahora mira a los peatones, no la "
                      "esquina: el primer párrafo los cuenta como una película. En cada cuadro escribe qué hacen y si "
                      "van cada uno por su lado o juntos.")
    x0, ww = x + 22, w - 44
    fh = 300
    b.append(rect(x0, yy, ww, fh, "#3A3F4B", r=10))
    for k in range(int(ww // 46)):
        for sy in (yy + 12, yy + fh - 28):
            b.append(rect(x0 + 18 + k * 46, sy, 22, 16, "white", r=3))
    n = 4
    gap = 16
    cw = (ww - 40 - gap * (n - 1)) / n
    cuadros = ("At first…", "But when the first notes…", "Pedestrians slow down…", "…and someone even…")
    for k, t in enumerate(cuadros):
        cx = x0 + 20 + k * (cw + gap)
        b.append(rect(cx, yy + 42, cw, fh - 84, "white", r=6))
        texto(b, cx + 14, yy + 72, t, size=16, style="italic", weight="700", color=c)
        pista(b, cx + 14, yy + 104, "lo que hace la gente:", size=14)
        renglon(b, cx + 14, yy + 142, cx + cw - 14)
        renglon(b, cx + 14, yy + 176, cx + cw - 14)
        casillas(b, cx + 14, yy + 196, ("cada uno", "juntos"), c, gap=110, size=14)
    yy += fh + 22
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "CUÁNTO DURA Y ENTRE QUIÉNES", c)
    pista(b, x0 + 20, yy + 64, "copia la expresión del párrafo que dice cuánto dura el cambio:")
    renglon(b, x0 + 470, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 112, "lo que la música le hace a gente que no se conoce, en mis palabras:")
    renglon(b, x0 + 500, yy + 116, x0 + ww - 20)
    yy += 168
    return trampa(b, x0, yy, ww, "«Primary social function» pregunta por la gente:",
                  "qué hace la música con los que pasan por la esquina. La respuesta tiene que salir de tus cuatro "
                  "cuadros, no de lo que tú sabes de la música callejera.", c)


# ───────── 11 · B2 n.º 3 · «theaters or museums» ─────────
def i11(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El arte con boleta y el arte de andén", c,
                      "Dos cosas frente a frente: el autor pone la calle al lado del teatro y del museo. Llena las dos "
                      "fachadas con lo que dice el texto y después mira bien qué idea es la que el autor ataca.")
    x0, ww = x + 22, w - 44
    half = (ww - 60) / 2
    fy, fh = yy, 300
    # fachada del museo
    b.append(f'<polygon points="{x0},{fy + 70} {x0 + half / 2},{fy} {x0 + half},{fy + 70}" fill="{tinte(c, 0.9)}" '
             f'stroke="{c}" stroke-width="2"/>')
    caja(b, x0, fy + 70, half, fh - 70, c, r=4)
    for k in range(5):
        b.append(rect(x0 + 24 + k * (half - 64) / 4, fy + 84, 16, fh - 100, tinte(c, 0.92), r=2))
    rot(b, x0 + half / 2, fy + 52, "THEATERS OR MUSEUMS", c, size=12, anchor="middle")
    # esquina de la calle
    sx = x0 + half + 60
    caja(b, sx, fy + 70, half, fh - 70, c, r=4)
    b.append(rect(sx + 10, fy + fh - 40, half - 20, 26, "#EEF0F4", r=3, stroke=GRAY, sw=1.4))
    b.append(f'<polyline points="{sx + 140},{fy + fh - 40} {sx + 152},{fy + fh - 30} {sx + 146},{fy + fh - 22} '
             f'{sx + 160},{fy + fh - 14}" fill="none" stroke="{GRAY}" stroke-width="1.6"/>')
    rot(b, sx + half / 2, fy + 52, "THE STREET", c, size=12, anchor="middle")
    for k, bx in enumerate((x0, sx)):
        ix = bx + (60 if k == 0 else 24)
        iw = half - (120 if k == 0 else 48)
        b.append(rect(ix - 10, fy + 92, iw + 20, 160, "white", r=8))
        pista(b, ix, fy + 116, "¿se planea o pasa de repente?")
        renglon(b, ix, fy + 148, ix + iw)
        pista(b, ix, fy + 186, "¿quién puede llegar a verlo?")
        renglon(b, ix, fy + 218, ix + iw)
    texto(b, x0 + half + 30, fy + 190, "≠", size=40, color=c, weight="700", anchor="middle")
    yy = fy + fh + 22
    caja(b, x0, yy, ww, 230, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL AUTOR PELEA CONTRA UN «ONLY»", c)
    texto(b, x0 + 20, yy + 64, "They challenge the idea that art belongs only to theaters or museums.", size=18,
          style="italic", weight="700")
    pista(b, x0 + 20, yy + 100, "la idea que atacan, en mis palabras:")
    renglon(b, x0 + 290, yy + 104, x0 + ww - 20)
    pista(b, x0 + 20, yy + 142, "¿el autor dice que los teatros y museos ya no sirven?")
    casillas(b, x0 + 420, yy + 126, ("sí, lo dice", "no, dice otra cosa"), c, gap=170)
    pista(b, x0 + 20, yy + 186, "entonces, para el autor, la cultura vive…")
    renglon(b, x0 + 320, yy + 190, x0 + ww - 20)
    return yy + 230


# ───────── 12 · B2 n.º 4 · «I am here, my story matters» ─────────
def i12(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Parte la frase en dos y busca su pareja", c,
                      "La frase que dice más de lo que dice: la que va entre comillas tiene dos mitades, y la oración "
                      "de justo antes trae dos palabras que las explican. Une cada mitad con su palabra y escribe qué "
                      "le pasaría al músico si nadie lo oyera.")
    x0, ww = x + 22, w - 44
    cita(b, x0, yy, ww, "For many artists, playing in the street is not only about money. It is also about visibility "
                        "and dignity. A song on the corner can say: “I am here, my story matters.”", c,
         rotulo="EL PÁRRAFO 3, EN TU LIBRO", size=17)
    yy += 130
    lw = 420
    for k, mitad in enumerate(("“I am here”", "“my story matters”")):
        by = yy + k * 120
        caja(b, x0, by, lw, 92, c, r=46, sw=2.4, fill=tinte(c, 0.93))
        texto(b, x0 + lw / 2, by + 56, mitad, size=24, weight="700", style="italic", anchor="middle")
    rx = x0 + lw + 160
    for k, pal in enumerate(("money", "visibility", "dignity")):
        by = yy + k * 80 - 6
        caja(b, rx, by, 220, 60, c, r=10)
        texto(b, rx + 110, by + 38, pal, size=20, weight="700", style="italic", anchor="middle")
        texto(b, rx + 250, by + 38, "quiere decir:", size=15, color=GRAY, style="italic")
        renglon(b, rx + 350, by + 42, x0 + ww)
    pista(b, x0 + lw + 20, yy + 260, "traza una flecha de cada mitad a su palabra (una de las tres sobra)")
    yy += 286
    caja(b, x0, yy, ww, 250, c, r=14)
    rot(b, x0 + 20, yy + 30, "SI NADIE LO OYERA", c)
    pista(b, x0 + 20, yy + 66, "en una ciudad donde todos pasan de afán, el músico sería…")
    renglon(b, x0 + 420, yy + 70, x0 + ww - 20)
    renglon(b, x0 + 20, yy + 112, x0 + ww - 20)
    pista(b, x0 + 20, yy + 154, "entonces tocar en la calle es una manera de…")
    renglon(b, x0 + 360, yy + 158, x0 + ww - 20)
    renglon(b, x0 + 20, yy + 200, x0 + ww - 20)
    pista(b, x0 + 20, yy + 234, "(fíjate en quién habla en la frase: «I», el músico, hablando de sí mismo)", size=14)
    return yy + 250


# ───────── 13 · B2 n.º 5 · «unwilling to let silence define their cities» ─────────
def burbuja(b, x, y, w, h, c, cola="izq", fill="white"):
    """Globo de diálogo con su colita abajo."""
    caja(b, x, y, w, h, c, r=28, sw=2.4, fill=fill)
    tx = x + 70 if cola == "izq" else x + w - 70
    d = 1 if cola == "izq" else -1
    b.append(f'<polygon points="{tx - 18 * d},{y + h - 1} {tx + 18 * d},{y + h - 1} {tx - 30 * d},{y + h + 34}" '
             f'fill="{fill}" stroke="{c}" stroke-width="2.4"/>')
    b.append(rect(tx - 20 if d == 1 else tx - 20, y + h - 6, 40, 8, fill, r=0))


def i13(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El silencio como personaje", c,
                      "La frase que dice más de lo que dice: en la última oración el silencio es alguien que quiere "
                      "«definir» la ciudad, y los colombianos no lo dejan. Dale voz a cada uno y busca en el primer "
                      "párrafo dónde estaba ese silencio.")
    x0, ww = x + 22, w - 44
    yy = cita(b, x0, yy, ww, "…street music speaks of who Colombians are: resilient, creative, and unwilling to let "
                             "silence define their cities.", c, rotulo="LA ÚLTIMA ORACIÓN", size=17)
    yy += 22
    half = (ww - 40) / 2
    burbuja(b, x0, yy, half, 190, c, "izq", fill=tinte(GRAY, 0.92))
    rot(b, x0 + 24, yy + 32, "EL SILENCIO DIRÍA:", c, size=13)
    pista(b, x0 + 24, yy + 64, "«si yo definiera esta ciudad, la gente…»")
    renglon(b, x0 + 24, yy + 108, x0 + half - 24)
    renglon(b, x0 + 24, yy + 150, x0 + half - 24)
    bx = x0 + half + 40
    burbuja(b, bx, yy, half, 190, c, "der")
    rot(b, bx + 24, yy + 32, "LOS COLOMBIANOS RESPONDEN:", c, size=13)
    pista(b, bx + 24, yy + 64, "«no te dejamos, porque somos…» (las tres palabras del texto)")
    for k in range(3):
        caja(b, bx + 24 + k * (half - 48) / 3, yy + 90, (half - 48) / 3 - 14, 54, c, r=10)
    pista(b, bx + 24, yy + 170, "una de las tres no dice cómo son: dice lo que no están dispuestos a permitir")
    yy += 190 + 54
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "¿DÓNDE ESTABA EL SILENCIO EN EL PRIMER PÁRRAFO?", c)
    pista(b, x0 + 20, yy + 64, "antes de las primeras notas, la gente que pasaba por la esquina…")
    renglon(b, x0 + 470, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 110, "entonces el «silence» de la última oración no es solo falta de ruido: es…")
    renglon(b, x0 + 560, yy + 114, x0 + ww - 20)
    yy += 168
    return ojo(b, x0, yy, ww, "«UNWILLING TO LET» = NO ESTAR DISPUESTO A DEJAR",
               "Es una frase de resistencia: alguien quiere algo y otro no lo permite. Pregúntate quién quiere y quién "
               "no permite, y qué tipo de fuerza tiene la música en esa pelea.")


# ───────── 14 · B2 n.º 6 · bolero, rap y tambores ─────────
def medidor(b, cx, cy, r, c):
    """Medidor de media luna sin aguja: el estudiante la dibuja."""
    import math as _m
    pts = " ".join(f"{cx - r * _m.cos(_m.pi * i / 24):.1f},{cy - r * _m.sin(_m.pi * i / 24):.1f}" for i in range(25))
    b.append(f'<polygon points="{pts}" fill="{tinte(c, 0.94)}" stroke="{c}" stroke-width="2"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{c}"/>')
    texto(b, cx - r + 4, cy + 18, "suave", size=13, color=GRAY, style="italic")
    texto(b, cx + r - 4, cy + 18, "fuerte", size=13, color=GRAY, style="italic", anchor="end")


def i14(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Tres ciudades, un mismo árbol", c,
                      "Para qué lo pone el autor: nombra géneros de tres ciudades distintas. Escribe en cada rama lo "
                      "que suena allí y en las raíces lo que, según el párrafo 2, esa música trae de atrás.")
    x0, ww = x + 22, w - 44
    tx = x0 + 300
    b.append(rect(tx - 30, yy + 120, 60, 150, "#B08A66", r=8))
    b.append(f'<ellipse cx="{tx}" cy="{yy + 92}" rx="250" ry="88" fill="{tinte(EDU_VERDE, 0.86)}"/>')
    rot(b, tx, yy + 98, "STREET MUSIC", EDU_VERDE, size=14, anchor="middle")
    rx = x0 + 580
    rw = ww - 580
    for k, ciudad in enumerate(("BOGOTÁ", "CARTAGENA", "CALI")):
        ry = yy + k * 78
        caja(b, rx, ry, rw, 66, c, r=33)
        rot(b, rx + 24, ry + 40, ciudad, c, size=13)
        pista(b, rx + 150, ry + 40, "suena:")
        renglon(b, rx + 200, ry + 44, rx + rw - 30)
        flecha(b, tx + 200, yy + 70 + k * 20, rx - 6, ry + 33, c, sw=2, head=8)
    ry0 = yy + 270
    for k in range(5):
        b.append(f'<path d="M {tx} {ry0} Q {tx - 220 + k * 110} {ry0 + 30} {tx - 300 + k * 150} {ry0 + 60}" '
                 f'fill="none" stroke="#B08A66" stroke-width="3"/>')
    caja(b, rx, ry0 - 20, rw, 100, c, r=14, dash="8,6")
    rot(b, rx + 20, ry0 + 6, "LAS RAÍCES: LO QUE TRAE DE ATRÁS (EN INGLÉS)", c, size=13)
    renglon(b, rx + 20, ry0 + 60, rx + rw - 20)
    yy = ry0 + 100
    caja(b, x0, yy, ww, 196, c, r=14)
    rot(b, x0 + 20, yy + 30, "MEDIDOR DE PALABRAS FUERTES", c)
    pista(b, x0 + 20, yy + 56, "subraya en cada opción del libro su palabra más fuerte y dibuja la aguja; después, "
                               "¿el texto lo dice con esa fuerza?")
    gw = (ww - 40) / 4
    for k, L in enumerate("ABCD"):
        gx = x0 + 20 + k * gw + gw / 2
        medidor(b, gx - 40, yy + 136, 54, c)
        texto(b, gx - 104, yy + 100, L, size=20, color=c, weight="700", anchor="middle")
        for j, lab in enumerate(("sí", "no")):
            b.append(checkbox(gx + 34, yy + 92 + j * 38, s=10, c=c))
            texto(b, gx + 62, yy + 109 + j * 38, lab, size=15, color=GRAY)
    yy += 214
    return ojo(b, x0, yy, ww, "UNA PALABRA FUERTE ES UNA ALARMA, NO UNA RESPUESTA",
               "En esta misión muchas opciones traen palabras como always, never, completely, nothing u only. Una "
               "opción con palabra fuerte puede ser verdad si el texto lo dice así de fuerte, y la que suena moderada "
               "también necesita su frase en el texto. La alarma te dice dónde mirar, no qué marcar.")


# ───────── 15 · B2 n.º 7 · la queja del ruido ─────────
def i15(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dos voces en la balanza y quién gana", c,
                      "Para qué lo pone el autor: el último párrafo pone dos opiniones a pesar. Escribe cada una en su "
                      "plato, con la palabra en inglés que la anuncia, y mira hacia dónde se inclina el autor en la "
                      "última oración.")
    x0, ww = x + 22, w - 44
    cx = x0 + ww / 2
    by = yy + 70
    b.append(f'<polygon points="{cx - 46},{by + 150} {cx + 46},{by + 150} {cx},{by + 10}" fill="{tinte(c, 0.85)}" '
             f'stroke="{c}" stroke-width="2"/>')
    b.append(line(cx - 90, by + 150, cx + 90, by + 150, c, 3))
    b.append(line(cx - 470, by + 10, cx + 470, by + 10, c, 3))
    pw = 500
    for k, (lab, marca) in enumerate((("UNA VOZ", "Some people complain that…"),
                                      ("LA OTRA VOZ", "Others, however, argue that…"))):
        px = cx - 470 - pw / 2 + 40 if k == 0 else cx + 470 - pw / 2 - 40
        px = max(x0, min(px, x0 + ww - pw))
        b.append(line(px + pw / 2, by + 10, px + pw / 2, by + 44, c, 2))
        caja(b, px, by + 44, pw, 260, c, r=16)
        rot(b, px + 18, by + 72, lab, c, size=13)
        texto(b, px + 18, by + 104, marca, size=17, style="italic", weight="700")
        pista(b, px + 18, by + 136, "lo que dice, en mis palabras:")
        renglon(b, px + 18, by + 180, px + pw - 18)
        renglon(b, px + 18, by + 228, px + pw - 18)
        renglon(b, px + 18, by + 276, px + pw - 18)
    yy = by + 326
    cita(b, x0, yy, ww, "Whether it is a bolero, rap, or drums, the truth is that street music speaks of who "
                        "Colombians are: resilient, creative, and unwilling to let silence define their cities.", c,
         rotulo="LA ÚLTIMA ORACIÓN", size=17)
    yy += 104
    caja(b, x0, yy, ww, 120, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "MI VEREDICTO", c)
    pista(b, x0 + 20, yy + 64, "la balanza se inclina hacia:")
    casillas(b, x0 + 250, yy + 48, ("la primera voz", "la segunda voz", "queda en empate"), c, gap=230)
    pista(b, x0 + 20, yy + 102, "entonces la primera voz está en el texto para…")
    renglon(b, x0 + 360, yy + 104, x0 + ww - 20)
    return yy + 120


# ───────── 16 · B2 n.º 8 · el ruido de la ciudad y las notas del bolero ─────────
def i16(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Dos sonidos, dos maneras de estar en la calle", c,
                      "Dos cosas frente a frente: el autor opone dos sonidos, y cada uno trae una forma de estar con "
                      "los demás. Llena cada onda con lo que hace la gente en el primer párrafo y, al final, ponle un "
                      "nombre a cada lado.")
    x0, ww = x + 22, w - 44
    half = (ww - 40) / 2
    oh = 330
    for k, (tit, onda) in enumerate((("«THE NOISE OF THE CITY»", "rota"), ("«THE NOTES OF A BOLERO»", "suave"))):
        bx = x0 + k * (half + 40)
        caja(b, bx, yy, half, oh, c, r=16)
        rot(b, bx + 20, yy + 32, tit, c, size=13)
        wy = yy + 78
        if onda == "rota":
            pts = " ".join(f"{bx + 24 + i * (half - 48) / 22:.1f},{wy + (-22 if i % 2 else 18) * (0.5 + (i * 7 % 5) / 5):.1f}"
                           for i in range(23))
            b.append(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2.4"/>')
        else:
            seg = (half - 48) / 4
            d = f"M {bx + 24} {wy}"
            for i in range(4):
                x1 = bx + 24 + i * seg
                d += f" Q {x1 + seg / 4:.1f} {wy - 30} {x1 + seg / 2:.1f} {wy} Q {x1 + 3 * seg / 4:.1f} {wy + 30} {x1 + seg:.1f} {wy}"
            b.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="2.4"/>')
        pista(b, bx + 20, yy + 140, "¿qué hace la gente?")
        renglon(b, bx + 20, yy + 180, bx + half - 20)
        pista(b, bx + 20, yy + 220, "¿se miran unos a otros? ¿comparten algo?")
        renglon(b, bx + 20, yy + 260, bx + half - 20)
        renglon(b, bx + 20, yy + 300, bx + half - 20)
    yy += oh + 22
    pw = (ww - 90) / 2
    for k, tit in enumerate(("EL LADO DEL RUIDO SE LLAMA…", "EL LADO DEL BOLERO SE LLAMA…")):
        bx = x0 + k * (pw + 90)
        caja(b, bx, yy, pw, 110, c, r=55, sw=2.4)
        rot(b, bx + pw / 2, yy + 34, tit, c, size=13, anchor="middle")
        renglon(b, bx + 40, yy + 82, bx + pw - 40)
    texto(b, x0 + ww / 2, yy + 66, "vs.", size=22, weight="700", color=c, anchor="middle")
    yy += 130
    return ojo(b, x0, yy, ww, "UNA TENSIÓN TIENE DOS POLOS QUE SALEN DEL MISMO TEXTO",
               "Si una opción trae una pareja que no aparece en el primer párrafo, no es la tensión que el autor "
               "construye, aunque suene bonita. Los dos polos de la opción tienen que poder llenarse con lo que "
               "escribiste en las ondas.")


B1, B2 = "Bloque 1, n.º", "Bloque 2, n.º"
Q = {1: dict(n=1, est=1, pag=457, ctx=f"{B1} 1 del libro · de qué depende la vida humana",
             comp="Lectura · inferencia", inst=i1),
     2: dict(n=2, est=1, pag=457, ctx=f"{B1} 2 del libro · de dónde sale la energía",
             comp="Lectura · inferencia", inst=i2),
     3: dict(n=3, est=1, pag=457, ctx=f"{B1} 3 del libro · la tala: ¿un daño local?",
             comp="Lectura · inferencia", inst=i3),
     4: dict(n=4, est=4, pag=457, ctx=f"{B1} 4 del libro · «protecting our own future»",
             comp="Lectura · contraste implícito", inst=i4),
     5: dict(n=5, est=3, pag=457, ctx=f"{B1} 5 del libro · «the foundation of… every ecosystem»",
             comp="Lectura · sentido figurado", inst=i5),
     6: dict(n=6, est=4, pag=457, ctx=f"{B1} 6 del libro · la atmósfera de hoy frente a otra",
             comp="Lectura · contraste implícito", inst=i6),
     7: dict(n=7, est=2, pag=457, ctx=f"{B1} 7 del libro · las hojas de los árboles de la ciudad",
             comp="Lectura · propósito del autor", inst=i7),
     8: dict(n=8, est=1, pag=458, ctx=f"{B1} 8 del libro · «green roofs»",
             comp="Lectura · inferencia", inst=i8),
     9: dict(n=9, est=2, pag=458, ctx=f"{B2} 1 del libro · «a cracked sidewalk»",
             comp="Lectura · propósito del autor", inst=i9),
     10: dict(n=10, est=1, pag=458, ctx=f"{B2} 2 del libro · de «hurry past» a sonreír",
              comp="Lectura · inferencia", inst=i10),
     11: dict(n=11, est=4, pag=458, ctx=f"{B2} 3 del libro · la calle frente a «theaters or museums»",
              comp="Lectura · contraste implícito", inst=i11),
     12: dict(n=12, est=3, pag=459, ctx=f"{B2} 4 del libro · «I am here, my story matters»",
              comp="Lectura · sentido figurado", inst=i12),
     13: dict(n=13, est=3, pag=459, ctx=f"{B2} 5 del libro · «unwilling to let silence…»",
              comp="Lectura · sentido figurado", inst=i13),
     14: dict(n=14, est=2, pag=459, ctx=f"{B2} 6 del libro · bolero, rap y tambores",
              comp="Lectura · propósito del autor", inst=i14),
     15: dict(n=15, est=2, pag=459, ctx=f"{B2} 7 del libro · la queja por el ruido",
              comp="Lectura · propósito del autor", inst=i15),
     16: dict(n=16, est=4, pag=459, ctx=f"{B2} 8 del libro · el ruido de la ciudad y el bolero",
              comp="Lectura · contraste implícito", inst=i16)}


def build(pages=(321, 322, 323, 324, 326, 327, 328, 329)):
    out = []
    for k in range(8):
        out.append(hoja_taller(f"ing5_t{k + 1}", pages[k], k + 1, Q[2 * k + 1], Q[2 * k + 2]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
