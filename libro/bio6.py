#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 6 · componente entorno biológico · páginas 175–181.

Última misión del área. Libro fuente: «PRUEBA DE CAMPO MISIÓN 6» de Biología
(fuente_libro/BIOLOGIA), páginas 127–130. Contenido: perros de apartamento y estimulación
(1 a 3), fósiles marinos de Sáchica (4), la extinción del Bramble Cay melomys (5), el pez león
en el Caribe (6) y los frailejones de Guerrero, Chingaza y Sumapaz (7 a 10).

Claves verificadas (resueltas a mano contra el texto y las tablas del libro, 7 nov 2026):

    1·D  2·A  3·A  4·B  5·B  6·A  7·C  8·A  9·B  10·D

  1 · D: la única hipótesis evolutiva que usa lo que dice el texto («muchos perros pequeños han sido
      seleccionados»). A mezcla el efecto del ambiente con la supervivencia; B contradice la tabla
      (el autocontrol es alto en los dos grupos); C contradice el texto. Hallazgo: el experimento
      mide seis meses de vida, no evolución; la pregunta pide una hipótesis evolutiva sobre él.
  2 · A, la menos mala: dice que hubo respuesta diferencial «en actividad, autocontrol y
      sociabilidad», pero según la tabla el autocontrol no cambió (alto y alto). B, C y D son
      peores (mutaciones en seis meses, la raza que «determina casi por completo», el azar).
  3 · A: lo único distinto entre los grupos fue la estimulación.
  4 · B: la diversidad de formas sugiere nichos distintos. A, C y D no se siguen de la tabla.
  5 · B: el mar subió e inundó su único hábitat.
  6 · A: sin depredadores, el pez león reduce a los peces nativos.
  7 · C: Guerrero: 200 individuos, flujo nulo, heterocigosidad 0,15; Chingaza: 2.000, alto, 0,65;
      Sumapaz: 800, limitado, 0,40. Las tres columnas suben juntas.
  8 · A: hojas vellosas (lo dice el texto).
  9 · B: el texto dice que regulan el agua y dan refugio a otras especies.
 10 · D, con reserva: B («la estabilidad de Chingaza se explica porque su gran tamaño y alto flujo
      génico mantienen variabilidad…») también es consistente con la tabla y el texto. D es la que
      usa la comparación que pide el enunciado. Dos respuestas defendibles: hallazgo Alta.

Reparto: A 4 · B 3 · C 1 · D 2. La C sale una sola vez. Registrado como Atención.

Estrategias (la 1 y la 2 recogen lo trabajado en el área: la herencia de la Misión 5 y la
lectura de datos y comparaciones de todas las misiones):
    1 · El ambiente o la herencia                             (1, 2, 3 · ICFES N.º 61)   azul
    2 · Lo que los datos sí dejan concluir                    (7, 10   · ICFES N.º 51)   morado
    3 · Si se cae una pieza del ecosistema                    (5, 6, 9 · ICFES N.º 57)   rojo
    4 · Para qué le sirve ese rasgo                           (4, 8    · ICFES N.º 64)   oro

Hojas: 175 bio6_t1 (1-2) · 176 bio6_t2 (3-4) · 177 bio6_i1 · 178 bio6_t3 (5-6) ·
       179 bio6_t4 (7-8) · 180 bio6_t5 (9-10) · 181 bio6_i2.
"""
import math

from taller_base import *

configurar("Biología", 6, "entorno biológico",
           tema="La vida cambia: ambiente, selección y ecosistemas",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("El ambiente o la herencia", EDU_AZUL),
       2: ("Lo que los datos sí dejan concluir", MORADO),
       3: ("Si se cae una pieza del ecosistema", EDU_ROJO),
       4: ("Para qué le sirve ese rasgo", EDU_ORO)}
usar_estrategias(EST)
AZ, MO, RO, OR = (EST[k][1] for k in (1, 2, 3, 4))
VERDE_P = "#4E8A3A"     # dibujo de plantas


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


def parrafo(b, x, y, w, txt, size=17, color=INK, style="normal", weight="400"):
    svg, yy = TJ(x, y, txt, w, size, color, style=style, weight=weight, lh=size + 8)
    b.append(svg)
    return yy


# ───────── P1 · dos relojes ─────────
DATOS_1 = (("a", "«solo el 9 % de la variación conductual se explica por raza»"),
           ("b", "«muchos perros pequeños han sido seleccionados para adaptarse a espacios reducidos»"),
           ("c", "tras seis meses con pocas salidas: actividad baja y sociabilidad baja"),
           ("d", "«el entorno y la crianza tienen mayor impacto»"))


def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos relojes: la vida de un perro y la historia de la raza", c,
                      "Unos cambios pasan durante la vida de un mismo perro; otros, a lo largo de muchas generaciones "
                      "de perros. Escribe la letra de cada dato en el reloj que le corresponde.")
    x0, ww = x + 22, w - 44
    for k, (L, t_) in enumerate(DATOS_1):
        py = yy + k * 44
        letra(b, x0 + 18, py + 14, L, c, r=15, size=15)
        b.append(T(x0 + 46, py + 20, [t_], 17, INK, style="italic"))
    yy += 4 * 44 + 12
    half = (ww - 30) / 2
    for k, (tit, ps, marcas) in enumerate((("RELOJ 1 · LA VIDA DE UN PERRO", "se mide en meses", 6),
                                           ("RELOJ 2 · LA HISTORIA DE LA RAZA", "se mide en generaciones", 8))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 200, c, r=16)
        rot(b, bx + 20, yy + 30, tit, c, size=14)
        pista(b, bx + 20, yy + 54, ps)
        ly = yy + 92
        b.append(line(bx + 30, ly, bx + half - 30, ly, c, 3))
        for i in range(marcas + 1):
            px = bx + 30 + i * (half - 60) / marcas
            b.append(line(px, ly - 8, px, ly + 8, c, 2.4))
        pista(b, bx + 20, yy + 134, "datos que van aquí:")
        for j in range(3):
            b.append(rect(bx + 170 + j * 70, yy + 112, 52, 34, "white", r=6, stroke=c, sw=1.8))
        pista(b, bx + 20, yy + 180, "aquí cambia…")
        renglon(b, bx + 118, yy + 182, bx + half - 20)
    yy += 218
    return trampa(b, x0, yy, ww, "Una hipótesis evolutiva mira el reloj 2:",
                  "si una opción dice que el ambiente «produce» perros distintos y lo explica con la supervivencia, "
                  "revisa en cuál reloj está parada. Un perro que pasa seis meses con pocas salidas no les hereda eso "
                  "a sus cachorros.", c)


# ───────── P2 · rasgo por rasgo ─────────
def i2(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Rasgo por rasgo: qué cambió y qué no", c,
                      "Copia la tabla del libro y compara los dos grupos rasgo por rasgo. Lo que no cambió también es "
                      "un dato: una opción que diga que cambió se equivoca en esa parte.")
    x0, ww = x + 22, w - 44
    cols = (300, 300, 300, ww - 900)
    heads = ("RASGO", "ALTA ESTIMULACIÓN", "BAJA ESTIMULACIÓN", "¿CAMBIÓ?")
    caja(b, x0, yy, ww, 50, c, fill=tinte(c), r=10)
    cx = x0
    for k, hd in enumerate(heads):
        rot(b, cx + 18, yy + 32, hd, c, size=14)
        cx += cols[k]
    ry = yy + 50
    for f in ("Nivel de actividad", "Nivel de autocontrol", "Sociabilidad con humanos"):
        caja(b, x0, ry, ww, 70, c, r=0)
        texto(b, x0 + 18, ry + 42, f, size=17, weight="700")
        renglon(b, x0 + cols[0] + 20, ry + 50, x0 + cols[0] + cols[1] - 20)
        renglon(b, x0 + cols[0] + cols[1] + 20, ry + 50, x0 + cols[0] + cols[1] + cols[2] - 20)
        sino(b, x0 + cols[0] + cols[1] + cols[2] + 24, ry + 26, c, gap=74)
        ry += 70
    cx = x0
    for k in range(3):
        cx += cols[k]
        b.append(line(cx, yy, cx, ry, c, 2))
    yy = ry + 18
    yy = frase_hueco(b, x0, yy, ww, "Con menos estimulación se movió ______________ y no se movió ______________ .", c)
    yy += 16
    return ojo(b, x0, yy, ww, "SI NINGUNA OPCIÓN CUADRA PERFECTO CON TU TABLA",
               "A veces pasa. Anota en qué falla cada una y quédate con la que explica lo que sí cambió sin "
               "inventarse una causa que el experimento no midió.")


# ───────── P3 · el tablero del experimento ─────────
def perilla(b, cx, cy, c, r=34):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{tinte(c, 0.9)}" stroke="{c}" stroke-width="2.4"/>')
    b.append(f'<circle cx="{cx}" cy="{cy}" r="6" fill="{c}"/>')
    for i in range(7):
        a = math.radians(210 - i * 40)
        b.append(line(cx + (r + 6) * math.cos(a), cy - (r + 6) * math.sin(a),
                      cx + (r + 13) * math.cos(a), cy - (r + 13) * math.sin(a), c, 2))


def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El tablero del experimento: qué se movió y qué se dejó quieto", c,
                      "Un experimento es un tablero de perillas: el investigador mueve una, deja quietas las demás y "
                      "mira qué pasa. Llena el tablero del programa con los perros de apartamento.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 330, c, r=18, fill=tinte(c, 0.96))
    pw = (ww - 4 * 20) / 3
    for k, (tit, ps) in enumerate((("LA PERILLA QUE SE MOVIÓ", "qué fue distinto entre los dos grupos"),
                                   ("LAS PERILLAS QUIETAS", "qué fue igual para los dos grupos"),
                                   ("LO QUE SE MIDIÓ", "qué se anotó a los seis meses"))):
        bx = x0 + 20 + k * (pw + 20)
        caja(b, bx, yy + 20, pw, 290, c, r=14)
        perilla(b, bx + pw / 2, yy + 86, c)
        rot(b, bx + pw / 2, yy + 160, tit, c, size=14, anchor="middle")
        pista(b, bx + pw / 2, yy + 184, ps, size=14, anchor="middle")
        for j in range(3):
            renglon(b, bx + 18, yy + 224 + j * 34, bx + pw - 18)
    yy += 348
    yy = frase_hueco(b, x0, yy, ww, "Si solo se movió una perilla, lo que cambió en los perros se lo atribuyo a ____________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una opción habla de mutaciones que «surgieron durante el experimento»:",
                  "¿cuántas generaciones de perros caben en seis meses? Los perros medidos al final son los mismos "
                  "del principio.", c)


# ───────── P4 · tres oficios en el mismo mar ─────────
FOSILES = (("AMMONITES", "caparazón espiralado, gran diversidad de formas"),
           ("ICTIOSAURIOS", "cuerpo similar al de los delfines, nado veloz"),
           ("PLESIOSAURIOS", "cuello muy largo, aletas para impulsarse"))


def i4(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Tres fósiles, tres oficios en el mismo mar", c,
                      "La forma de un cuerpo cuenta cómo vivía. Para cada fósil, a partir del rasgo de la tabla, "
                      "escribe cómo crees que se movía o comía. Al final decide si los tres hacían lo mismo.")
    x0, ww = x + 22, w - 44
    fw = (ww - 2 * 20) / 3
    for k, (nom, rasgo) in enumerate(FOSILES):
        bx = x0 + k * (fw + 20)
        caja(b, bx, yy, fw, 300, c, r=16)
        rot(b, bx + 18, yy + 30, nom, c)
        b.append(T(bx + 18, yy + 58, [rasgo], 15, GRAY, style="italic"))
        pista(b, bx + 18, yy + 120, "ese rasgo le sirve para…")
        renglon(b, bx + 18, yy + 160, bx + fw - 18)
        renglon(b, bx + 18, yy + 194, bx + fw - 18)
        pista(b, bx + 18, yy + 236, "entonces vivía o comía…")
        renglon(b, bx + 18, yy + 276, bx + fw - 18)
    yy += 318
    caja(b, x0, yy, ww, 64, c, r=12)
    texto(b, x0 + 22, yy + 40, "¿Usaban el mar de la misma manera?", size=18, weight="700")
    sino(b, x0 + 380, yy + 23, c)
    pista(b, x0 + 560, yy + 40, "por eso podían…")
    renglon(b, x0 + 690, yy + 42, x0 + ww - 20)
    yy += 82
    return trampa(b, x0, yy, ww, "Una opción dice que los fósiles llegaron arrastrados desde lejos:",
                  "¿qué dice el texto sobre el lugar donde vivían? Un fósil marino en una montaña cuenta que la "
                  "montaña fue mar, no que alguien trajo los animales.", c)


# ───────── P5 · la isla ─────────
def i5(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Una isla, un solo hogar y el mar que sube", c,
                      "Así se ve Bramble Cay de lado. Completa el dibujo: escribe en cada recuadro lo que pide, según "
                      "el texto del libro.")
    x0, ww = x + 22, w - 44
    dh = 430
    caja(b, x0, yy, ww, dh, c, r=16)
    base = yy + dh - 34
    # la isla (corte)
    pts = [(x0 + 200, base), (x0 + 300, base - 90), (x0 + 420, base - 130), (x0 + 560, base - 138),
           (x0 + 700, base - 120), (x0 + 810, base - 70), (x0 + 900, base)]
    d = "M " + " L ".join(f"{px:.0f} {py:.0f}" for px, py in pts) + " Z"
    b.append(f'<path d="{d}" fill="#EFE3C8" stroke="#9C8150" stroke-width="2.4"/>')
    # dos niveles del mar
    for k, (lv, lab, dash) in enumerate(((base - 50, "nivel del mar antes", None),
                                         (base - 112, "nivel del mar después", "10,7"))):
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        b.append(f'<line x1="{x0 + 20}" y1="{lv}" x2="{x0 + ww - 20}" y2="{lv}" stroke="#2C6FA8" '
                 f'stroke-width="2.6"{dd}/>')
        pista(b, x0 + 30, lv - 8, lab, size=14)
    # el roedor: un punto en la cima
    b.append(f'<circle cx="{x0 + 560}" cy="{base - 150}" r="8" fill="{INK}"/>')
    texto(b, x0 + 576, base - 152, "el melomys", size=14, color=INK)
    # recuadros para escribir
    boxes = ((x0 + 20, yy + 20, 330, "1 · POR QUÉ SUBIÓ EL MAR"),
             (x0 + 400, yy + 20, 330, "2 · QUÉ LE PASÓ A SU HÁBITAT"),
             (x0 + ww - 350, yy + 20, 330, "3 · ¿A DÓNDE PODÍA IRSE?"))
    for bx, by, bw, tit in boxes:
        caja(b, bx, by, bw, 116, c, r=12)
        rot(b, bx + 16, by + 28, tit, c, size=13)
        renglon(b, bx + 16, by + 66, bx + bw - 16)
        renglon(b, bx + 16, by + 100, bx + bw - 16)
    yy += dh + 18
    return ojo(b, x0, yy, ww, "«ENDÉMICO» ES UNA PALABRA CLAVE",
               "Una especie endémica vive en un solo lugar del mundo y en ningún otro. Pregúntate qué significa eso "
               "para un animal pequeño cuando ese único lugar se inunda.")


# ───────── P6 · la red del arrecife ─────────
def nodo_red(b, cx, cy, txt, c, w=230, h=64, dash=None):
    b.append(rect(cx - w / 2, cy - h / 2, w, h, "white", r=32, stroke=c, sw=2.2, dash=dash))
    lineas = txt.split("|")
    for k, ln in enumerate(lineas):
        texto(b, cx, cy + 6 + (k - (len(lineas) - 1) / 2) * 20, ln, size=16, weight="700", anchor="middle")
    b.append(rect(cx + w / 2 - 18, cy - h / 2 - 16, 36, 32, "white", r=8, stroke=c, sw=1.8))


def i6(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La red del arrecife con un invitado sin enemigos", c,
                      "Dibuja flechas que vayan de la presa a quien se la come. En la casilla de cada uno escribe S si "
                      "su población sube con la llegada del pez león, B si baja o = si no cambia.")
    x0, ww = x + 22, w - 44
    dh = 400
    caja(b, x0, yy, ww, dh, c, r=16, fill=tinte(c, 0.96))
    cx = x0 + ww / 2
    nodo_red(b, cx, yy + 70, "Pez león|(invasor)", c)
    nodo_red(b, x0 + 230, yy + 210, "Peces pequeños|nativos", c)
    nodo_red(b, x0 + ww - 230, yy + 210, "Depredadores nativos|del arrecife", c)
    nodo_red(b, cx, yy + 340, "Arrecife de coral|y sus algas", c)
    nodo_red(b, x0 + ww - 160, yy + 70, "¿Quién se come|al pez león?", c, w=210, dash="7,5")
    pista(b, x0 + 30, yy + 380, "Dibuja tú las flechas: «va de la presa a quien la come».", size=14)
    yy += dh + 18
    yy = frase_hueco(b, x0, yy, ww, "La casilla del pez león tiene ___ porque en el Caribe colombiano ______________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una opción dice que el pez león no compite con nadie:",
                  "mira tu red: ¿come lo mismo que alguien más? Si dos especies se comen a las mismas presas, "
                  "compiten, aunque nunca se vean.", c)


# ───────── P7 · barras ─────────
PARAMOS = (("Guerrero", 200, 0.15), ("Sumapaz", 800, 0.40), ("Chingaza", 2000, 0.65))


def i7(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Tres páramos en barras: ¿suben juntas las columnas?", c,
                      "Dibuja las barras con los datos de la tabla del libro (en el orden en que van aquí). Marca "
                      "también el flujo génico. Después mira si las barras suben juntas o al revés.")
    x0, ww = x + 22, w - 44
    gw = (ww - 40) / 2
    graf = (("TAMAÑO POBLACIONAL (individuos)", (0, 500, 1000, 1500, 2000)),
            ("DIVERSIDAD GENÉTICA (índice)", (0, 0.2, 0.4, 0.6, 0.8)))
    gh = 300
    for k, (tit, marcas) in enumerate(graf):
        bx = x0 + k * (gw + 40)
        rot(b, bx, yy + 18, tit, c, size=14)
        ax, ay = bx + 70, yy + 40 + gh
        top = yy + 50
        b.append(line(ax, ay, ax, top, INK, 2.2))
        b.append(line(ax, ay, bx + gw - 10, ay, INK, 2.2))
        for i, m in enumerate(marcas):
            py = ay - i * (gh - 10) / (len(marcas) - 1)
            if i:
                b.append(f'<line x1="{ax}" y1="{py:.1f}" x2="{bx + gw - 10}" y2="{py:.1f}" stroke="#E6EAF0" '
                         f'stroke-width="1.6"/>')
            lab = f"{m:,}".replace(",", ".") if isinstance(m, int) else f"{m:.1f}".replace(".", ",")
            texto(b, ax - 10, py + 5, lab, size=14, color=GRAY, anchor="end")
        sw_ = (gw - 100) / 3
        for j, (nom, _, _) in enumerate(PARAMOS):
            texto(b, ax + 20 + sw_ * j + sw_ / 2, ay + 26, nom, size=15, color=INK, anchor="middle")
    yy += gh + 80
    caja(b, x0, yy, ww, 64, c, r=12)
    texto(b, x0 + 20, yy + 40, "Flujo génico:", size=17, weight="700")
    for j, (nom, _, _) in enumerate(PARAMOS):
        bx = x0 + 170 + j * 360
        texto(b, bx, yy + 40, nom, size=16, color=GRAY)
        renglon(b, bx + tw(nom, 16) + 12, yy + 44, bx + 330)
    yy += 82
    yy = frase_hueco(b, x0, yy, ww, "Cuando sube el tamaño, la diversidad ______________ ; y el flujo génico ______________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una opción dice que todas las poblaciones tienen una variabilidad parecida:",
                  "mira tus barras de diversidad. ¿Quedaron a la misma altura? Una conclusión tiene que poder "
                  "dibujarse con los datos.", c)


# ───────── P8 · el frailejón por partes ─────────
def frailejon(b, cx, base, c):
    """Tallo grueso, falda de hojas secas y roseta de hojas vellosas arriba."""
    b.append(rect(cx - 22, base - 250, 44, 250, "#B89A6A", r=10, stroke="#7E6338", sw=2))
    for i in range(6):
        yy = base - 230 + i * 34
        b.append(line(cx - 24, yy, cx + 24, yy + 14, "#7E6338", 1.6))
    for k in range(9):
        a = math.radians(20 + k * 17.5)
        x2 = cx + 120 * math.cos(a)
        y2 = base - 262 - 90 * math.sin(a)
        b.append(f'<path d="M {cx} {base - 252} Q {(cx + x2) / 2:.1f} {y2 - 18:.1f} {x2:.1f} {y2:.1f}" '
                 f'fill="none" stroke="#8FA88A" stroke-width="14" stroke-linecap="round"/>')
        b.append(f'<path d="M {cx} {base - 252} Q {(cx + x2) / 2:.1f} {y2 - 18:.1f} {x2:.1f} {y2:.1f}" '
                 f'fill="none" stroke="#DDE6D8" stroke-width="5" stroke-linecap="round" stroke-dasharray="2,5"/>')
    b.append(line(cx - 160, base, cx + 160, base, "#9C8150", 3))


def i8(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El frailejón por partes: cada rasgo contra un problema", c,
                      "A la izquierda, los rasgos que nombra el texto; a la derecha, los retos del páramo. Une cada "
                      "rasgo con el reto (o los retos) que enfrenta y escribe cómo lo hace.")
    x0, ww = x + 22, w - 44
    frailejon(b, x0 + 170, yy + 400, c)
    rasgos = ("hojas vellosas", "hojas en roseta", "tallo que acumula agua")
    probs = ("temperaturas extremas", "alta radiación solar", "guardar agua para los días secos")
    for k, r_ in enumerate(rasgos):
        ry = yy + 30 + k * 130
        caja(b, x0 + 330, ry, 260, 56, c, r=28)
        texto(b, x0 + 460, ry + 35, r_, size=17, weight="700", anchor="middle")
        b.append(f'<circle cx="{x0 + 602}" cy="{ry + 28}" r="7" fill="{c}"/>')
        pista(b, x0 + 330, ry + 92, "lo resuelve así:")
        renglon(b, x0 + 444, ry + 94, x0 + ww - 10)
    for k, p in enumerate(probs):
        ry = yy + 30 + k * 130
        caja(b, x0 + 820, ry, ww - 820, 56, c, r=12, dash="7,5")
        texto(b, x0 + 840, ry + 35, p, size=17)
        b.append(f'<circle cx="{x0 + 800}" cy="{ry + 28}" r="7" fill="white" stroke="{c}" stroke-width="2"/>')
    yy += 420
    return trampa(b, x0, yy, ww, "Una opción le da al tallo una función que mataría a la planta:",
                  "¿puede una planta vivir sin intercambiar gases con el aire? Antes de creerle a un rasgo, búscalo "
                  "en el texto y en tu dibujo.", c)


# ───────── P9 · el dominó del páramo ─────────
def i9(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El dominó del páramo después del fuego", c,
                      "Cuando cae la primera ficha, empuja a las demás. Escribe en cada ficha lo que se pierde y quién lo "
                      "sufre, según el texto, en el orden en que va cayendo.")
    x0, ww = x + 22, w - 44
    n = 5
    fw, fh = 196, 300
    gap = (ww - n * fw) / (n - 1)
    for k in range(n):
        bx = x0 + k * (fw + gap)
        top = yy + 20
        b.append(rect(bx, top, fw, fh, "white" if k else tinte(c, 0.9), r=16, stroke=c, sw=2.6))
        b.append(line(bx + 16, top + fh / 2, bx + fw - 16, top + fh / 2, c, 1.6))
        b.append(f'<circle cx="{bx + fw / 2}" cy="{top + 26}" r="7" fill="{c}"/>')
        if k == 0:
            rot(b, bx + fw / 2, top + 84, "EL INCENDIO", c, size=14, anchor="middle")
            pista(b, bx + fw / 2, top + 112, "reduce la cobertura", size=14, anchor="middle")
            pista(b, bx + fw / 2, top + 132, "de frailejones", size=14, anchor="middle")
            pista(b, bx + fw / 2, top + fh / 2 + 60, "la primera ficha", size=14, anchor="middle")
            pista(b, bx + fw / 2, top + fh / 2 + 80, "que cae", size=14, anchor="middle")
        else:
            texto(b, bx + 16, top + 62, "se pierde:", size=14, color=GRAY)
            renglon(b, bx + 16, top + 98, bx + fw - 16)
            renglon(b, bx + 16, top + 132, bx + fw - 16)
            texto(b, bx + 16, top + fh / 2 + 32, "quién lo sufre:", size=14, color=GRAY)
            renglon(b, bx + 16, top + fh / 2 + 70, bx + fw - 16)
            renglon(b, bx + 16, top + fh / 2 + 104, bx + fw - 16)
        if k < n - 1:
            flecha(b, bx + fw + 4, top + fh / 2, bx + fw + gap - 4, top + fh / 2, c, sw=2.4, head=9)
    yy += fh + 40
    return ojo(b, x0, yy, ww, "UNA PLANTA QUE TRABAJA PARA OTROS",
               "El texto dice dos cosas que hace el frailejón por el páramo. Si tus fichas solo hablan de la planta, te "
               "falta la mitad: un ecosistema es lo que pasa entre las especies.")


# ───────── P10 · cada conclusión con sus páramos ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Cada conclusión, con los páramos que de verdad usa", c,
                      "El enunciado pide una conclusión con base en los datos de los tres páramos. Para cada opción, "
                      "marca qué páramos usa, si la tabla la respalda y encierra su palabra más fuerte.")
    x0, ww = x + 22, w - 44
    cols = (80, 420, 290, ww - 790)
    heads = ("", "PÁRAMOS QUE USA", "¿LA TABLA LA RESPALDA?", "SU PALABRA MÁS FUERTE")
    caja(b, x0, yy, ww, 50, c, fill=tinte(c), r=10)
    cx = x0
    for k, hd in enumerate(heads):
        if hd:
            rot(b, cx + 18, yy + 32, hd, c, size=14)
        cx += cols[k]
    ry = yy + 50
    for L in "ABCD":
        caja(b, x0, ry, ww, 70, c, r=0)
        letra(b, x0 + 40, ry + 35, L, c)
        for j, p in enumerate(("Guerrero", "Chingaza", "Sumapaz")):
            bx = x0 + cols[0] + 18 + j * 132
            b.append(checkbox(bx, ry + 24, s=10, c=c))
            texto(b, bx + 26, ry + 41, p, size=15, color=GRAY)
        sino(b, x0 + cols[0] + cols[1] + 40, ry + 24, c)
        renglon(b, x0 + cols[0] + cols[1] + cols[2] + 18, ry + 50, x0 + ww - 18)
        ry += 70
    cx = x0
    for k in range(3):
        cx += cols[k]
        b.append(line(cx, yy, cx, ry, c, 2))
    yy = ry + 18
    return ojo(b, x0, yy, ww, "SI DOS OPCIONES TE PARECEN CIERTAS",
               "Puede pasar: una conclusión puede ser verdadera y aun así no responder lo que se pidió. Vuelve al "
               "enunciado, mira tu columna de páramos y anota tu duda para la clase: es una buena discusión.")


Q = {1: dict(n=1, est=1, pag=127, ctx="Perros de apartamento · una hipótesis evolutiva",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=1, pag=128, ctx="Perros de apartamento · lo que muestra la tabla",
             comp="Indagación", inst=i2),
     3: dict(n=3, est=1, pag=128, ctx="Perros de apartamento · la conclusión del experimento",
             comp="Indagación", inst=i3),
     4: dict(n=4, est=4, pag=128, ctx="Fósiles marinos de Sáchica · el ecosistema del Cretácico",
             comp="Explicación de fenómenos", inst=i4),
     5: dict(n=5, est=3, pag=128, ctx="Bramble Cay melomys · por qué se extinguió",
             comp="Explicación de fenómenos", inst=i5),
     6: dict(n=6, est=3, pag=129, ctx="Pez león en el Caribe · una especie invasora",
             comp="Explicación de fenómenos", inst=i6),
     7: dict(n=7, est=2, pag=129, ctx="Frailejones · tres páramos comparados",
             comp="Indagación", inst=i7),
     8: dict(n=8, est=4, pag=130, ctx="Frailejones · cómo sobreviven en el páramo",
             comp="Uso comprensivo del conocimiento científico", inst=i8),
     9: dict(n=9, est=3, pag=130, ctx="Frailejones · el efecto de los incendios",
             comp="Explicación de fenómenos", inst=i9),
     10: dict(n=10, est=2, pag=130, ctx="Frailejones · la conclusión más consistente",
              comp="Indagación", inst=i10)}


def build(pages=(175, 176, 178, 179, 180)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"bio6_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
