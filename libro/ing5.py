#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 5 · componente lectura · páginas 297–303.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 5» de Inglés (fuente_libro/INGLÉS), páginas 456–459.
Comprensión inferencial: leer lo que el texto deja entender. Dos textos: «Why Photosynthesis
Matters» (Bloque 1, ocho preguntas) y «The Power of Street Music» (Bloque 2, ocho preguntas).

El libro trae 16 preguntas (dos bloques de 8, numerados 1 a 8 cada uno). El cuaderno trabaja 10:
Bloque 1 n.º 1, 2, 3, 5, 6, 7 y Bloque 2 n.º 1, 4, 7, 8. Quedan en el libro, para la clase o la
tarea, Bloque 1 n.º 4 (B) y 8 (B) y Bloque 2 n.º 2 (A), 3 (A), 5 (D) y 6 (C). Registrado como
Atención en tablero/propuestas/ing5_hallazgos.csv.

Claves verificadas (resueltas a mano contra el texto del libro, no copiadas, 7 nov 2026):

    1·C  2·A  3·D  4·C  5·A  6·D  7·D  8·B  9·B  10·A

  1 · C (B1 n.º 1): sin fotosíntesis «the atmosphere would quickly become toxic, and most species
      could not survive»; la energía de los azúcares «pass through the entire food chain». La vida
      humana depende del equilibrio de procesos biológicos del planeta. A, B y D no están en el texto
      (domesticación, tecnología, separar la ciudad de la naturaleza).
  2 · A (B1 n.º 2): «energy that originally came from the sun» y «pass through the entire food
      chain»: viene de afuera (el sol) y pasa de un organismo a otro. B y C dicen que la fabrican los
      animales u «any organism»; D invierte la cadena (de los depredadores a las presas).
  3 · D (B1 n.º 3): «These problems may seem distant, but they directly affect the quality of the air
      we breathe and the stability of our climate»: lo que se tala en un lugar cambia el aire y el
      clima de todos. A lo contradice («restricted»); B y C no están en el texto.
  4 · C (B1 n.º 5): «foundation» es la base de una construcción; si la base falla, se cae lo de
      arriba: un sistema de soporte cuya ruptura arrastra al ecosistema. A («easily replaceable»), B
      («far more than it benefits animal species») y D (solo estudios botánicos) lo contradicen.
  5 · A (B1 n.º 6): «Without this process, the atmosphere would quickly become toxic»: el contraste
      es con una atmósfera posible (would) en la que no se puede respirar. B (más oxígeno), C (otros
      planetas) y D (la tecnología) no están en el texto.
  6 · D (B1 n.º 7): la contaminación de la ciudad daña las hojas de los árboles de la calle: la
      amenaza no está solo en bosques lejanos, está donde vivimos. A, B y C contradicen el párrafo.
  7 · D (B2 n.º 1): «just a cracked sidewalk», sin escenario, y aun así la esquina se vuelve un lugar
      de música: el espacio se redefine por la expresión. A, B y C no se siguen del texto.
  8 · B (B2 n.º 4): la frase sigue a «It is also about visibility and dignity»: «I am here» es ser
      visto; «my story matters» es valer. Es afirmarse para no ser un anónimo más. A, C y D
      (negociar, protestar, ser descubierto) no están en el párrafo.
  9 · B (B2 n.º 7): «Some people complain… Others, however, argue that it is exactly this spontaneity
      that keeps culture alive… the truth is that street music speaks of who Colombians are»: la
      queja se presenta para responderla con una idea mayor. A y C van contra el cierre; D no está.
 10 · A (B2 n.º 8): el ruido es la gente que pasa de afán, cada uno en lo suyo; el bolero hace que se
      detengan, sonrían y graben: de la prisa anónima a un momento compartido. B (rural), C
      (tecnología) y D (pobreza) no son lo que opone el texto.

Reparto del cuaderno: A 3 · B 2 · C 2 · D 3. Reparto del libro (16): A 5 · B 4 · C 3 · D 4.
Atención (hallazgo): en casi todas las preguntas de los dos bloques los distractores cierran con
absolutos («exclusively», «completely», «inherently», «nearly eliminated», «all») y la correcta es la
única que matiza; el cuaderno no lo enseña como truco, pide la evidencia en el texto.

Estrategias:
    1 · Lo que el texto deja entender          (1, 2, 3   · ICFES QA)   azul
    2 · Para qué lo pone el autor              (6, 7, 9   · ICFES QB)   rojo
    3 · La frase que dice más de lo que dice   (4, 8      · ICFES QC)   oro
    4 · Dos cosas frente a frente              (5, 10     · ICFES QD)   morado

Hojas: 297 ing5_t1 (1-2) · 298 ing5_t2 (3-4) · 299 ing5_i1 · 300 ing5_t3 (5-6) ·
       301 ing5_t4 (7-8) · 302 ing5_t5 (9-10) · 303 ing5_i2.
"""
from taller_base import *

configurar("Inglés", 5, "lectura",
           tema="Lo que el texto dice sin decirlo",
           nota="LO QUE SUBRAYÉ EN EL TEXTO")
MORADO = "#5B3E96"
EST = {1: ("Lo que el texto deja entender", EDU_AZUL),
       2: ("Para qué lo pone el autor", EDU_ROJO),
       3: ("La frase que dice más de lo que dice", EDU_ORO),
       4: ("Dos cosas frente a frente", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))


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
    """Tabla con encabezado tinte y primera columna con rótulos; el resto, renglones."""
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


# ───────── P1 · B1 n.º 1 · de qué depende la existencia humana ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Quita una pieza y mira qué se cae", c,
                      "El texto no dice «los humanos dependen de…»: lo deja ver con oraciones del tipo «sin esto, "
                      "pasa aquello». Para cada pieza, copia en inglés lo que el texto dice que pasaría si faltara "
                      "y anota el párrafo donde lo encontraste.")
    x0, ww = x + 22, w - 44
    cols = (300, ww - 300 - 150, 150)
    yy = tabla_vacia(b, x0, yy, cols, ("SI FALTA…", "LO QUE PASA, CON LAS PALABRAS DEL TEXTO", "PÁRRAFO"),
                     (("las plantas", "(no hay fotosíntesis)"), ("el oxígeno", "(el aire que respiramos)"),
                      ("la energía del sol", "(la guardada en azúcares)"), ("los bosques", "(talados o enfermos)")),
                     c, rh=74)
    yy += 22
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE SOSTIENE TODO", c)
    pista(b, x0 + 20, yy + 62, "las cuatro filas apuntan a una sola idea; escríbela en mis palabras, sin copiar ninguna opción:")
    renglones(b, x0 + 20, yy + 104, ww - 40, 2, step=34)
    yy += 168
    return trampa(b, x0, yy, ww, "Una opción puede ser cierta en el mundo y no estar en el texto:",
                  "«implica» quiere decir que el texto lo deja ver, no que tú lo sepas por otro lado. Antes de "
                  "marcar, busca en tu tabla la fila que sostiene la opción. Si no hay ninguna, esa opción habla "
                  "de otra lectura.", c)


# ───────── P2 · B1 n.º 2 · de dónde viene la energía ─────────
def i2(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Sigue la energía de mano en mano", c,
                      "El segundo párrafo cuenta un viaje. Llena cada estación con quién tiene la energía en ese "
                      "momento y, debajo, marca si ese ser la fabrica o la recibe de la estación anterior.")
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


def hueco_ingles(b, x, y, w, c):
    """Recuadro de dos pisos: la palabra en inglés / lo que quiere decir."""
    caja(b, x, y, w, 96, c, r=10)
    pista(b, x + 12, y + 34, "en inglés:", size=14)
    renglon(b, x + 90, y + 38, x + w - 12)
    pista(b, x + 12, y + 80, "quiere decir:", size=14)
    renglon(b, x + 108, y + 84, x + w - 12)


# ───────── P3 · B1 n.º 3 · lo local y lo global ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Del árbol talado al clima de todos", c,
                      "Cada daño del tercer párrafo empieza en un lugar pequeño. Escribe en los círculos hasta "
                      "dónde llega cada efecto que nombra el texto: el lugar, la ciudad o el planeta entero.")
    x0, ww = x + 22, w - 44
    cx, cy = x0 + 250, yy + 250
    for r_, lab, k in ((240, "EL PLANETA", 0.96), (160, "LA CIUDAD", 0.92), (80, "EL LUGAR", 0.86)):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r_}" fill="{tinte(c, k)}" stroke="{c}" stroke-width="2"/>')
        rot(b, cx, cy - r_ + 26, lab, c, size=13, anchor="middle")
    pista(b, cx, cy + 6, "el bosque", anchor="middle")
    pista(b, cx, cy + 26, "que se tala", anchor="middle")
    rx, rw = x0 + 530, ww - 530
    efectos = ("less oxygen", "fewer natural resources", "damaged leaves", "the quality of the air we breathe",
               "the stability of our climate")
    cols = (290, (rw - 290) / 3, (rw - 290) / 3, (rw - 290) / 3)
    ty = yy + 6
    caja(b, rx, ty, rw, 44, c, fill=tinte(c), r=8)
    rot(b, rx + 14, ty + 28, "EFECTO (EN EL TEXTO)", c, size=13)
    for j, lab in enumerate(("LUGAR", "CIUDAD", "PLANETA")):
        rot(b, rx + 290 + cols[1] * (j + 0.5), ty + 28, lab, c, size=13, anchor="middle")
    ry = ty + 44
    for e in efectos:
        caja(b, rx, ry, rw, 62, c, r=0)
        texto(b, rx + 14, ry + 38, e, size=16, weight="700", style="italic")
        for j in range(3):
            b.append(checkbox(rx + 290 + cols[1] * (j + 0.5) - 11, ry + 20, s=11, c=c))
        ry += 62
    pista(b, rx, ry + 26, "marca hasta dónde llega cada uno (puede ser más de una casilla)")
    yy = max(cy + 250, ry + 40) + 18
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PALABRA «BUT» CORRIGE UNA IDEA", c)
    texto(b, x0 + 20, yy + 64, "These problems may seem distant, but they directly affect…", size=18, style="italic",
          weight="700")
    pista(b, x0 + 20, yy + 100, "lo que el lector podría creer (antes del «but»):")
    renglon(b, x0 + 360, yy + 102, x0 + ww - 20)
    pista(b, x0 + 20, yy + 136, "lo que el autor afirma (después del «but»):")
    renglon(b, x0 + 340, yy + 138, x0 + ww - 20)
    return yy + 150


# ───────── P4 · B1 n.º 5 · «foundation» ─────────
def i4(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "«Foundation» es una palabra de albañil", c,
                      "Una metáfora se entiende llevándola a su mundo. En construcción, la «foundation» es lo que va "
                      "debajo de todo. Pon en cada piso quién vive del ecosistema y piensa qué pasa si se cae la base.")
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


# ───────── P5 · B1 n.º 6 · la atmósfera de hoy frente a otra ─────────
def i5(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El termómetro del aire: respirable o tóxico", c,
                      "El texto no habla de dos planetas: habla de este aire y de otro que podría existir. Ubica "
                      "las dos situaciones en la barra y fíjate en el verbo que usa el autor para la segunda.")
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
    for j, lab in enumerate(("ya pasó y está probado", "no pasa hoy, pero podría pasar", "pasa hoy en otro lugar")):
        b.append(checkbox(x0 + 20 + j * 370, yy + 120, s=10, c=c))
        texto(b, x0 + 48 + j * 370, yy + 137, lab, size=15, color=GRAY)
    yy += 188
    return ojo(b, x0, yy, ww, "FRENTE A QUÉ SE COMPARA",
               "Cuando una pregunta dice «contrasts… with», busca el segundo término en el texto. Si una opción "
               "trae un lugar o un tiempo que el texto nunca nombra, el contraste no es ese.")


def _mezcla_dos(c1, c2, k):
    a = [int(c1[i:i + 2], 16) for i in (1, 3, 5)]
    d = [int(c2[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(p + (q - p) * k):02X}" for p, q in zip(a, d))


# ───────── P6 · B1 n.º 7 · la contaminación en las hojas de la ciudad ─────────
def i6(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La cabeza del lector antes y después del ejemplo", c,
                      "Un autor escoge sus ejemplos para mover lo que piensa el lector. Escribe qué pensaría quien "
                      "leyera solo lo de los bosques talados, y qué piensa después de leer lo de los árboles de la "
                      "ciudad.")
    x0, ww = x + 22, w - 44
    half = (ww - 90) / 2
    for k, (tit, ps) in enumerate((("SOLO CON LOS BOSQUES", "«Forests cut down for farming or construction…»"),
                                   ("CON EL EJEMPLO DE LA CIUDAD", "«In cities, air pollution can damage the leaves…»"))):
        bx = x0 + k * (half + 90)
        b.append(f'<ellipse cx="{bx + half / 2}" cy="{yy + 150}" rx="{half / 2}" ry="140" fill="white" '
                 f'stroke="{c}" stroke-width="2.2"/>')
        for j, (dx, dy, r_) in enumerate(((60, 300, 16), (34, 334, 10))):
            b.append(f'<circle cx="{bx + dx}" cy="{yy + dy}" r="{r_}" fill="white" stroke="{c}" stroke-width="2"/>')
        rot(b, bx + half / 2, yy + 52, tit, c, size=13, anchor="middle")
        pista(b, bx + half / 2, yy + 80, ps, size=14, anchor="middle")
        pista(b, bx + 70, yy + 120, "el lector piensa que el problema está…")
        renglon(b, bx + 70, yy + 160, bx + half - 70)
        renglon(b, bx + 70, yy + 200, bx + half - 70)
        renglon(b, bx + 110, yy + 240, bx + half - 110)
    flecha(b, x0 + half + 14, yy + 150, x0 + half + 76, yy + 150, c, head=12)
    yy += 356
    cols = (360, (ww - 360) / 2, (ww - 360) / 2)
    yy = tabla_vacia(b, x0, yy, cols, ("", "EL BOSQUE TALADO", "EL ÁRBOL DE MI CALLE"),
                     ("¿dónde queda?", "¿quién lo ve todos los días?"), c, rh=60)
    yy += 18
    caja(b, x0, yy, ww, 104, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "PARA QUÉ LO PUSO", c)
    pista(b, x0 + 20, yy + 62, "el autor menciona las hojas de los árboles de la ciudad para que yo entienda que…")
    renglon(b, x0 + 20, yy + 92, x0 + ww - 20)
    return yy + 104


# ───────── P7 · B2 n.º 1 · «a cracked sidewalk» ─────────
def i7(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La misma esquina, con y sin guitarra", c,
                      "El primer párrafo describe la esquina dos veces: antes y después de las primeras notas. "
                      "Anota lo que el texto dice de cada momento. Después decide para qué sirve el detalle del "
                      "andén roto.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (tit, marca) in enumerate((("ANTES DE LA MÚSICA", "At first…"), ("CUANDO SUENA EL BOLERO", "But when…"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 330, c, r=14)
        rot(b, bx + 18, yy + 30, tit, c, size=13)
        texto(b, bx + half - 18, yy + 30, marca, size=16, style="italic", weight="700", color=c, anchor="end")
        # andén con grieta
        b.append(rect(bx + 18, yy + 276, half - 36, 34, "#EEF0F4", r=4, stroke=GRAY, sw=1.6))
        b.append(f'<polyline points="{bx + 90},{yy + 276} {bx + 104},{yy + 288} {bx + 96},{yy + 298} '
                 f'{bx + 112},{yy + 310}" fill="none" stroke="{GRAY}" stroke-width="1.8"/>')
        for j, ps in enumerate(("el lugar:", "la gente que pasa:", "lo que hace la gente:")):
            pista(b, bx + 18, yy + 70 + j * 64, ps)
            renglon(b, bx + 170, yy + 74 + j * 64, bx + half - 18)
            renglon(b, bx + 18, yy + 102 + j * 64, bx + half - 18)
    yy += 350
    caja(b, x0, yy, ww, 170, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PALABRA «JUST»", c)
    texto(b, x0 + 20, yy + 64, "He doesn't have a stage, just a cracked sidewalk and the shade of a mango tree.",
          size=18, style="italic", weight="700")
    pista(b, x0 + 20, yy + 100, "aquí «just» quiere decir:")
    for j, lab in enumerate(("solo, nada más", "justo, exacto", "con justicia")):
        b.append(checkbox(x0 + 240 + j * 250, yy + 84, s=10, c=c))
        texto(b, x0 + 268 + j * 250, yy + 101, lab, size=15, color=GRAY)
    pista(b, x0 + 20, yy + 142, "con tan poco, ¿qué logra el músico en esa esquina?")
    renglon(b, x0 + 380, yy + 144, x0 + ww - 20)
    yy += 188
    return trampa(b, x0, yy, ww, "El detalle no siempre es una queja:",
                  "un andén roto podría servir para criticar la ciudad, pero pregúntate qué pasa en ese mismo "
                  "andén unas líneas después. Lo que el autor quiere mostrar está en el cambio, "
                  "no en la grieta.", c)


# ───────── P8 · B2 n.º 4 · «I am here, my story matters» ─────────
def i8(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Parte la frase en dos y busca su pareja", c,
                      "La frase entre comillas tiene dos mitades. La oración que va justo antes trae dos palabras "
                      "que las explican. Une cada mitad con su palabra y escribe qué le pasaría al músico si nadie "
                      "lo oyera.")
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


# ───────── P9 · B2 n.º 7 · la queja del ruido ─────────
def i9(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dos voces en la balanza y quién gana", c,
                      "El último párrafo pone dos opiniones a pesar. Escribe cada una en su plato, con la palabra en "
                      "inglés que la anuncia, y mira hacia dónde se inclina el autor en la última oración.")
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
    for j, lab in enumerate(("la primera voz", "la segunda voz", "queda en empate")):
        b.append(checkbox(x0 + 250 + j * 230, yy + 48, s=10, c=c))
        texto(b, x0 + 278 + j * 230, yy + 65, lab, size=15, color=GRAY)
    pista(b, x0 + 20, yy + 102, "entonces la primera voz está en el texto para…")
    renglon(b, x0 + 360, yy + 104, x0 + ww - 20)
    return yy + 120


# ───────── P10 · B2 n.º 8 · el ruido de la ciudad y las notas del bolero ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Dos sonidos, dos maneras de estar en la calle", c,
                      "El autor opone dos sonidos. Cada uno trae una forma de estar con los demás. Llena la tabla con "
                      "lo que hace la gente en el primer párrafo y, al final, ponle un nombre a cada lado.")
    x0, ww = x + 22, w - 44
    cols = (330, (ww - 330) / 2, (ww - 330) / 2)
    yy = tabla_vacia(b, x0, yy, cols, ("", "«THE NOISE OF THE CITY»", "«THE NOTES OF A BOLERO»"),
                     ("¿qué hace la gente?", "¿se miran unos a otros?", ("¿qué tienen en común?", "(algo que compartan)")),
                     c, rh=72)
    yy += 22
    half = (ww - 120) / 2
    for k, tit in enumerate(("EL LADO DEL RUIDO SE LLAMA…", "EL LADO DEL BOLERO SE LLAMA…")):
        bx = x0 + k * (half + 120)
        caja(b, bx, yy, half, 110, c, r=55, sw=2.4)
        rot(b, bx + half / 2, yy + 34, tit, c, size=13, anchor="middle")
        renglon(b, bx + 40, yy + 82, bx + half - 40)
    texto(b, x0 + ww / 2, yy + 66, "vs.", size=24, weight="700", color=c, anchor="middle")
    yy += 130
    return ojo(b, x0, yy, ww, "UNA TENSIÓN TIENE DOS POLOS QUE SALEN DEL MISMO TEXTO",
               "Si una opción trae una pareja que no aparece en el primer párrafo, no es la tensión que el autor "
               "construye, aunque suene bonita. Los dos polos de la opción tienen que poder llenarse con lo que "
               "escribiste en la tabla.")


Q = {1: dict(n=1, est=1, pag=457, ctx="Bloque 1, n.º 1 del libro · de qué depende la vida humana",
             comp="Lectura · inferencia", inst=i1),
     2: dict(n=2, est=1, pag=457, ctx="Bloque 1, n.º 2 del libro · de dónde sale la energía de un ecosistema",
             comp="Lectura · inferencia", inst=i2),
     3: dict(n=3, est=1, pag=457, ctx="Bloque 1, n.º 3 del libro · la tala: ¿un daño local?",
             comp="Lectura · inferencia", inst=i3),
     4: dict(n=4, est=3, pag=457, ctx="Bloque 1, n.º 5 del libro · «the foundation of almost every ecosystem»",
             comp="Lectura · sentido figurado", inst=i4),
     5: dict(n=5, est=4, pag=457, ctx="Bloque 1, n.º 6 del libro · la atmósfera de hoy frente a otra",
             comp="Lectura · contraste implícito", inst=i5),
     6: dict(n=6, est=2, pag=457, ctx="Bloque 1, n.º 7 del libro · la contaminación en las hojas de la ciudad",
             comp="Lectura · propósito del autor", inst=i6),
     7: dict(n=7, est=2, pag=458, ctx="Bloque 2, n.º 1 del libro · «a cracked sidewalk»",
             comp="Lectura · propósito del autor", inst=i7),
     8: dict(n=8, est=3, pag=459, ctx="Bloque 2, n.º 4 del libro · «I am here, my story matters»",
             comp="Lectura · sentido figurado", inst=i8),
     9: dict(n=9, est=2, pag=459, ctx="Bloque 2, n.º 7 del libro · la queja por el ruido",
             comp="Lectura · propósito del autor", inst=i9),
     10: dict(n=10, est=4, pag=459, ctx="Bloque 2, n.º 8 del libro · el ruido de la ciudad y el bolero",
              comp="Lectura · contraste implícito", inst=i10)}


def build(pages=(297, 298, 300, 301, 302)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"ing5_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
