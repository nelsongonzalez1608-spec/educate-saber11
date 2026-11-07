#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 6 · componente gramatical · léxico · páginas 304–310 (cierre del área).

Libro fuente: «PRUEBA DE CAMPO MISIÓN 6» de Inglés (fuente_libro/INGLÉS), páginas 468–470.
Textos con espacios, cuatro opciones cada uno: «An Unexpected Adventure» (Bloque 1, ocho espacios),
«Debating in Class» (Bloque 2, ocho) y «A Late Visitor», con Sherlock Holmes (Bloque 3, ocho).

El libro trae 24 preguntas (tres bloques numerados 1 a 8 cada uno). El cuaderno trabaja 10:
Bloque 1 n.º 1, 3, 5, 6 · Bloque 2 n.º 2, 4, 7 · Bloque 3 n.º 2, 6, 8. Las otras 14 quedan en el libro.
Claves de las 24 (resueltas a mano, 7 nov 2026):

    Bloque 1:  1·B went  2·B felt  3·C were setting  4·A began  5·B have been  6·A taken
               7·B started  8·A had
    Bloque 2:  1·A express  2·D involve  3·B develop  4·A check  5·C feel  6·B use  7·D improves
               8·A allow
    Bloque 3:  1·C lit  2·C was broken  3·B were  4·B ran  5·C took  6·C observing  7·C listened
               8·B saw

Claves del cuaderno (verificadas):

    1·B  2·C  3·B  4·A  5·D  6·A  7·D  8·C  9·C  10·B

  1 · B (B1 n.º 1): «Two years ago» marca un pasado terminado → pasado simple: went. «go» es presente,
      «going» y «gone» necesitan un auxiliar (am / have) que no está.
  2 · C (B1 n.º 3): «While we ___ our tent, it suddenly began to snow»: una acción larga en curso que
      otra interrumpe → pasado continuo; sujeto «we» → were setting. «are setting» es presente; «set» y
      «sets» no muestran la acción en curso. (Errata: falta «up»: «set up a tent».)
  3 · B (B1 n.º 5): «Since that day» une un punto del pasado con hoy (sigue fascinado) → presente
      perfecto: have been. «became» y «was becoming» cierran la acción en el pasado; «turn» no concuerda.
  4 · A (B1 n.º 6): «I have already ___» → have + participio: taken (take · took · taken).
  5 · D (B2 n.º 2): un debate trata temas, los incluye: involve. Con «avoid», «replace» o «imagine» la
      oración no dice lo que hace un debate con «subjects like climate change».
  6 · A (B2 n.º 4): «___ evidence before speaking, instead of repeating information without analysis»:
      lo contrario de repetir sin analizar es revisar: check. «ignore», «skip» y «hide» van en la
      dirección de «without analysis».
  7 · D (B2 n.º 7): el sujeto es «debating» (una actividad: it) → tercera persona: improves.
  8 · C (B3 n.º 2): el silencio no rompe nada; lo rompen las ruedas («by the distant wheels») → voz
      pasiva en pasado: was broken.
  9 · C (B3 n.º 6): «Holmes rose without haste, ___ the man…»: la oración ya tiene su verbo («rose») y
      no hay «and» → cláusula de participio: observing.
 10 · B (B3 n.º 8): el relato va en pasado («began», «delivered», «sounded») → saw. «sees» rompe el
      tiempo; «seeing» y «seen» necesitan auxiliar.

Reparto del cuaderno: A 2 · B 3 · C 3 · D 2. Reparto del libro (24): A 6 · B 9 · C 7 · D 2; el Bloque 3
no tiene ninguna A ni ninguna D (Atención en tablero/propuestas/ing6_hallazgos.csv).

Estrategias (la 4 recoge el área: leer todo el texto antes de llenar el espacio, como en las misiones de
lectura, y la función de los conectores con que abre esta misión en el libro):
    1 · La línea de tiempo del verbo          (1, 2, 3   · ICFES QA)   azul
    2 · La palabra de al lado manda la forma  (4, 7, 8   · ICFES QB)   rojo
    3 · Palabras que andan juntas             (5, 6      · ICFES QC)   oro
    4 · El párrafo entero decide              (9, 10     · ICFES QD)   morado

Hojas: 304 ing6_t1 (1-2) · 305 ing6_t2 (3-4) · 306 ing6_i1 · 307 ing6_t3 (5-6) ·
       308 ing6_t4 (7-8) · 309 ing6_t5 (9-10) · 310 ing6_i2.
"""
from taller_base import *

configurar("Inglés", 6, "gramatical · léxico",
           tema="Cada palabra en su tiempo y en su lugar",
           nota="LO QUE SUBRAYÉ EN EL TEXTO")
MORADO = "#5B3E96"
EST = {1: ("La línea de tiempo del verbo", EDU_AZUL),
       2: ("La palabra de al lado manda la forma", EDU_ROJO),
       3: ("Palabras que andan juntas", EDU_ORO),
       4: ("El párrafo entero decide", MORADO)}
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


def sino(b, x, y, c, labels=("sí", "no"), gap=80):
    for j, lab in enumerate(labels):
        b.append(checkbox(x + j * gap, y, s=10, c=c))
        b.append(T(x + 28 + j * gap, y + 17, [lab], 16, GRAY))


def oracion(b, x, y, w, txt, c, rotulo="LA ORACIÓN DEL LIBRO", size=21):
    """La oración del libro con su espacio, en inglés, en un recuadro tinte con acento vertical."""
    svg, yy = TJ(x + 26, y + 38, txt, w - 52, size, INK, weight="700", style="italic", lh=size + 9)
    h = yy - y + 14
    caja(b, x, y, w, h, tinte(c, 0.86), fill=tinte(c, 0.95), r=12)
    b.append(rect(x, y, 7, h, c, r=3))
    rot(b, x + 26, y + 24, rotulo, c, size=13)
    b.append(svg)
    return y + h


def linea_tiempo(b, x, y, w, c, rotulos=("ANTES", "AHORA", "DESPUÉS"), xs=(0.12, 0.62, 0.92)):
    """Eje del tiempo con tres marcas. Devuelve la y del eje."""
    b.append(line(x, y, x + w, y, INK, 3))
    b.append(f'<polygon points="{x + w},{y} {x + w - 16},{y - 9} {x + w - 16},{y + 9}" fill="{INK}"/>')
    for r_, k in zip(rotulos, xs):
        px = x + w * k
        b.append(line(px, y - 12, px, y + 12, INK, 3))
        rot(b, px, y + 40, r_, c, size=13, anchor="middle")
    return y


def tabla_vacia(b, x, y, cols, heads, filas, c, rh=58, hh=46, size=16, sin_renglon=()):
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


# ───────── P1 · B1 n.º 1 · «Two years ago» ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El marcador clava el verbo en el tiempo", c,
                      "Antes de mirar las opciones, busca en la oración la palabra que dice cuándo pasó. Clávala en la "
                      "línea del tiempo y decide si esa acción ya terminó o sigue pasando.")
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


# ───────── P2 · B1 n.º 3 · «While we ___ our tent» ─────────
def i2(b, x, y, w, h):
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
    cols = (380, (ww - 380) / 2, (ww - 380) / 2)
    yy = tabla_vacia(b, x0, yy, cols, ("", "LA ACCIÓN LARGA", "EL GOLPE"),
                     ("¿quién la hace?", "¿con qué palabra empieza?", "forma del verbo (fórmula)"), c, rh=58)
    yy += 18
    return trampa(b, x0, yy, ww, "Mira también quién es el sujeto:",
                  "la forma que pide la acción larga se arma con un auxiliar que concuerda con el sujeto. Escribe "
                  "el sujeto de la acción larga y comprueba que el auxiliar que eliges sea el suyo y que esté en "
                  "pasado, como el resto del relato.", c)


# ───────── P3 · B1 n.º 5 · «Since that day» ─────────
def i3(b, x, y, w, h):
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


# ───────── P4 · B1 n.º 6 · «I have already ___» ─────────
def i4(b, x, y, w, h):
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


# ───────── P5 · B2 n.º 2 · «Some debates ___ subjects» ─────────
def i5(b, x, y, w, h):
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


# ───────── P6 · B2 n.º 4 · «___ evidence before speaking» ─────────
def i6(b, x, y, w, h):
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


# ───────── P7 · B2 n.º 7 · «debating ___ not only…» ─────────
def i7(b, x, y, w, h):
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


# ───────── P8 · B3 n.º 2 · «the silence ___ only by…» ─────────
def i8(b, x, y, w, h):
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
    cols = (520, ww - 520)
    yy = tabla_vacia(b, x0, yy, cols, ("PREGUNTA", "MI RESPUESTA"),
                     ("¿cuál de los dos es el sujeto de la oración?", "¿qué me dice la palabra «by»?",
                      "¿activa o pasiva?", "¿en qué tiempo va el relato?"), c, rh=60)
    yy += 18
    return ojo(b, x0, yy, ww, "PASIVA = BE + PARTICIPIO",
               "En la voz pasiva el verbo «be» lleva el tiempo (is, was, were…) y el verbo principal va en "
               "participio. Y la forma del «be» concuerda con el sujeto, como cualquier verbo.")


# ───────── P9 · B3 n.º 6 · «Holmes rose without haste, ___ the man» ─────────
def i9(b, x, y, w, h):
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


# ───────── P10 · B3 n.º 8 · «Holmes already ___ the outline» ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El censo de los verbos del relato", c,
                      "El tiempo de un relato lo decide el texto entero, no una sola oración. Copia los verbos "
                      "conjugados del último párrafo, anota su tiempo y cuenta. El espacio 8 tiene que sonar como el "
                      "resto del cuento.")
    x0, ww = x + 22, w - 44
    yy = oracion(b, x0, yy, ww, "To me the account sounded confusing, but Holmes already (8) ________ the outline of a "
                                "mystery forming with alarming clarity.", c)
    yy += 22
    cols = (90, 330, 330, ww - 750)
    caja(b, x0, yy, ww, 44, c, fill=tinte(c), r=8)
    for k, hd in enumerate(("", "VERBO DEL PÁRRAFO", "TIEMPO", "¿QUIÉN LO HACE?")):
        rot(b, x0 + sum(cols[:k]) + 14, yy + 28, hd, c, size=13)
    ry = yy + 44
    for k in range(5):
        caja(b, x0, ry, ww, 52, c, r=0)
        texto(b, x0 + 45, ry + 33, str(k + 1), size=16, color=c, weight="700", anchor="middle")
        for j in range(1, 4):
            renglon(b, x0 + sum(cols[:j]) + 14, ry + 40, x0 + sum(cols[:j + 1]) - 14)
        ry += 52
    cx = x0
    for k in range(3):
        cx += cols[k]
        b.append(line(cx, yy, cx, ry, c, 1.6))
    yy = ry + 20
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


Q = {1: dict(n=1, est=1, pag=468, ctx="Bloque 1, n.º 1 del libro · «Two years ago, my family and I ___»",
             comp="Gramática · tiempos verbales", inst=i1),
     2: dict(n=2, est=1, pag=468, ctx="Bloque 1, n.º 3 del libro · «While we ___ our tent»",
             comp="Gramática · tiempos verbales", inst=i2),
     3: dict(n=3, est=1, pag=468, ctx="Bloque 1, n.º 5 del libro · «Since that day, I ___»",
             comp="Gramática · tiempos verbales", inst=i3),
     4: dict(n=4, est=2, pag=468, ctx="Bloque 1, n.º 6 del libro · «I have already ___»",
             comp="Gramática · forma del verbo", inst=i4),
     5: dict(n=5, est=3, pag=469, ctx="Bloque 2, n.º 2 del libro · «Some debates ___ subjects»",
             comp="Léxico · sentido y colocación", inst=i5),
     6: dict(n=6, est=3, pag=469, ctx="Bloque 2, n.º 4 del libro · «___ evidence before speaking»",
             comp="Léxico · sentido y colocación", inst=i6),
     7: dict(n=7, est=2, pag=469, ctx="Bloque 2, n.º 7 del libro · «debating ___ not only academic skills»",
             comp="Gramática · concordancia", inst=i7),
     8: dict(n=8, est=2, pag=470, ctx="Bloque 3, n.º 2 del libro · «the silence of London ___»",
             comp="Gramática · voz pasiva", inst=i8),
     9: dict(n=9, est=4, pag=470, ctx="Bloque 3, n.º 6 del libro · «Holmes rose without haste, ___»",
             comp="Gramática · cohesión de la oración", inst=i9),
     10: dict(n=10, est=4, pag=470, ctx="Bloque 3, n.º 8 del libro · «Holmes already ___ the outline»",
              comp="Gramática · tiempo del relato", inst=i10)}


def build(pages=(304, 305, 307, 308, 309)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"ing6_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
