#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 5 · componente entorno químico · páginas 211–217.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 5» de Química (fuente_libro/QUÍMICA), páginas 182–185.
Contenido: química orgánica en el entorno. El etanol como biocombustible (1), el plástico PLA y
la combustión de la glucosa (2), tres bolsas que se degradan en seis meses (3), cafeína y
teobromina en las bebidas energizantes (4 a 6) y el biodiésel frente al diésel fósil (7 a 10).

Claves verificadas (resueltas a mano contra el texto y las tablas del libro, 7 nov 2026):

    1·C  2·A  3·A  4·C  5·C  6·D  7·A  8·D  9·A  10·B

  1 · C: si el oxígeno no alcanza, el etanol (CH3–CH2–OH) se oxida a medias y queda en
      aldehído (CH3–CHO); eso explica el aumento de aldehídos. A dice algo cierto del grupo –OH
      (menos CO), pero no explica el impacto NEGATIVO que pide la pregunta. B y D son falsas.
  2 · A: las dos reacciones conservan la masa (se reorganizan átomos), con productos y energías
      distintos. Glucosa: C6H12O6 + 6 O2 → 6 CO2 + 6 H2O · C 6=6, H 12=12, O 18=18.
      Ácido láctico → unidad de PLA + agua: C3H6O3 → C3H4O2 + H2O · C 3=3, H 6=6, O 3=3.
      B, C y D hablan de átomos que se pierden o se destruyen.
  3 · A: el PLA pasó de 5,0 g a 3,8 g: perdió 1,2 g (24 %); el 76 % sigue ahí. Perder masa no
      prueba degradación total. B y D dicen «por completo / totalmente»; C contradice la tabla.
  4 · C: los grupos amida y amina son polares → interactúan con el agua → se distribuye en la
      sangre. A y B contradicen el texto; D inventa una unión a «enzimas musculares».
  5 · C: cafeína C8H10N4O2 y teobromina C7H8N4O2 difieren en un grupo metilo sobre un nitrógeno:
      cambia la disposición de los grupos nitrogenados y con ella el encaje en el receptor.
      A («idéntica») y B («no tienen grupos comunes») contradicen el enunciado; D, los azúcares.
  6 · D: los dos grupos tienen su pico a las 2 h (A 6,5 mg/L; B 5,9 mg/L). De 2 h a 6 h el grupo
      A baja 3,7 mg/L (6,5 → 2,8) y el B baja 4,8 mg/L (5,9 → 1,1): elimina más rápido.
  7 · A: el grupo –COO– tiene oxígenos que hacen polar la molécula: cambia viscosidad y
      biodegradabilidad. B (enlaces iónicos) y D (elimina los covalentes) son falsas: un éster es
      covalente; C dice «apolar», al revés.
  8 · D: 1 mol de biodiésel → 19 mol de CO2; 2 mol → 2 × 19 = 38 mol. (Ecuación balanceada:
      C 19=19 · H 36=36 · O 2+54 = 38+18 = 56.) B (27) es el O2; C (54) es 2 × 27.
  9 · A: SO2 1,8 → 0,0 g/km; partículas 180 → 120 mg/km; CO2 260 → 240 g/km (baja, no
      desaparece). B «elimina todos», C «idénticas», D «aumenta» contradicen la tabla.
 10 · B: une el resultado 2 (menos azufre y partículas, CO2 similar) con el 3 (subproductos
      oxigenados). A, C y D contradicen los resultados. Con reserva (hallazgo): la causa que da B
      está mal encadenada; el biodiésel tiene poco azufre porque los aceites vegetales casi no lo
      traen, no por los «subproductos oxigenados».

Reparto: A 4 · B 1 · C 3 · D 2. La B sale una sola vez; 4 y 5 son C seguidas. Registrado como
Atención en tablero/propuestas/qui5_hallazgos.csv.

Estrategias:
    1 · Del grupo funcional a la propiedad      (4, 5, 7   · ICFES pendiente)   azul
    2 · Los átomos no se pierden: se cuentan    (2, 8      · ICFES pendiente)   rojo
    3 · Lo que la tabla sí deja afirmar         (3, 6, 9   · ICFES pendiente)   morado
    4 · Qué sale del tubo de escape             (1, 10     · ICFES pendiente)   oro

Hojas: 211 qui5_t1 (1-2) · 212 qui5_t2 (3-4) · 213 qui5_i1 · 214 qui5_t3 (5-6) ·
       215 qui5_t4 (7-8) · 216 qui5_t5 (9-10) · 217 qui5_i2.
"""
from taller_base import *

configurar("Química", 5, "entorno químico",
           tema="El carbono en el tanque, en el vaso y en la bolsa",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Del grupo funcional a la propiedad", EDU_AZUL),
       2: ("Los átomos no se pierden: se cuentan", EDU_ROJO),
       3: ("Lo que la tabla sí deja afirmar", MORADO),
       4: ("Qué sale del tubo de escape", EDU_ORO)}
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


def hueco(b, x, y, w=70, h=40, c=GRAY):
    b.append(rect(x, y, w, h, "white", r=8, stroke=c, sw=1.8))


def tinte(c, k=0.9):
    from taller_base import _mezcla
    return _mezcla(c, k)


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12, bend=0.0):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


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


# ───────── P1 · etanol · aldehídos ─────────
def i1(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La escalera de oxidación del etanol", c,
                      "Quemar es oxidar. Con oxígeno de sobra, el etanol baja todos los escalones hasta CO₂ y "
                      "agua; si el oxígeno no alcanza, se queda a mitad de camino. Completa los escalones del "
                      "medio y marca dónde se detiene la combustión que deja aldehídos en el aire.")
    x0, ww = x + 22, w - 44
    pasos = (("ETANOL", "CH₃–CH₂–OH", "el alcohol que se mezcla con la gasolina"),
             ("ESCALÓN 2", None, "pierde 2 H: ¿qué grupo queda?"),
             ("ESCALÓN 3", None, "gana 1 O: ¿qué grupo queda?"),
             ("FINAL", "CO₂ + H₂O", "lo que sale con oxígeno de sobra"))
    sw_ = (ww - 3 * 40) / 4
    for k, (tit, form, ps) in enumerate(pasos):
        bx = x0 + k * (sw_ + 40)
        by = yy + 10 + k * 46
        caja(b, bx, by, sw_, 190, c, r=14, fill=tinte(c, 0.94) if form else "white")
        rot(b, bx + 16, by + 28, tit, c, size=14)
        if form:
            texto(b, bx + 16, by + 82, form, size=24, weight="700")
        else:
            pista(b, bx + 16, by + 60, "fórmula:")
            renglon(b, bx + 16, by + 104, bx + sw_ - 16)
        svg, _ = TJ(bx + 16, by + 132, ps, sw_ - 32, 15, GRAY, style="italic", lh=20)
        b.append(svg)
        b.append(checkbox(bx + sw_ - 40, by + 12, s=10, c=c))
        if k < 3:
            flecha(b, bx + sw_ + 4, by + 60, bx + sw_ + 36, by + 106, c, head=10)
    pista(b, x0, yy + 340, "marca con X la casilla del escalón donde se queda la combustión a medias")
    yy += 366
    caja(b, x0, yy, ww, 130, c, r=14)
    rot(b, x0 + 20, yy + 30, "DOS CAMINOS PARA EL MISMO ETANOL", c)
    half = (ww - 60) / 2
    for k, (t1, t2) in enumerate((("con oxígeno de sobra sale…", "y el aire recibe…"),
                                  ("con oxígeno escaso sale…", "y el aire recibe…"))):
        bx = x0 + 20 + k * (half + 20)
        pista(b, bx, yy + 64, t1)
        renglon(b, bx + 190, yy + 66, bx + half)
        pista(b, bx, yy + 108, t2)
        renglon(b, bx + 140, yy + 110, bx + half)
    yy += 150
    return trampa(b, x0, yy, ww, "Una opción puede decir algo cierto y no responder:",
                  "la pregunta pide explicar por qué AUMENTAN los aldehídos, el efecto negativo. Antes de marcar, "
                  "pregúntale a cada opción: ¿esto explica de dónde salen los aldehídos, o habla de otra cosa?", c)


# ───────── P2 · PLA y glucosa · conservar la masa ─────────
def i2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Cuento átomos a cada lado de la flecha", c,
                      "Una reacción no fabrica ni destruye átomos: los reacomoda. Cuenta cada elemento antes y "
                      "después en las dos reacciones. Si los números cuadran, la masa se conserva.")
    x0, ww = x + 22, w - 44
    reac = (("COMBUSTIÓN DE LA GLUCOSA", "C₆H₁₂O₆ + 6 O₂  →  6 CO₂ + 6 H₂O"),
            ("UNA UNIDAD DEL PLA", "C₃H₆O₃  →  C₃H₄O₂ (eslabón del PLA) + H₂O"))
    half = (ww - 30) / 2
    for k, (tit, ec) in enumerate(reac):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 400, c, r=16)
        rot(b, bx + 18, yy + 30, tit, c)
        texto(b, bx + 18, yy + 72, ec, size=19, weight="700")
        cols = (130, (half - 166) / 2, (half - 166) / 2)
        ty = yy + 96
        tabla_vacia(b, bx + 18, ty, cols, ("ÁTOMO", "ANTES", "DESPUÉS"), ("C", "H", "O"), c, rh=60)
        pista(b, bx + 18, yy + 380, "¿cuadran los tres?")
        sino(b, bx + 170, yy + 364, c)
    yy += 420
    yy = frase_hueco(b, x0, yy, ww, "En las dos reacciones la masa total se conserva porque los átomos ______________ .", c)
    yy += 16
    return ojo(b, x0, yy, ww, "SI LA BALANZA MARCA MENOS, MIRA QUÉ SE FUE AL AIRE",
               "El CO₂ y el vapor de agua son gases: si el recipiente está abierto, salen y la balanza baja. Esos "
               "átomos no dejaron de existir; están en el aire. Para comprobar la conservación se pesa todo, "
               "también lo que se escapa.")


# ───────── P3 · tres bolsas · seis meses ─────────
def i3(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Seis meses, tres bolsas, una balanza", c,
                      "Antes de juzgar la conclusión, saca de la tabla del libro cuánto perdió cada bolsa y qué "
                      "parte de ella sigue ahí. Haz las cuentas en el margen.")
    x0, ww = x + 22, w - 44
    cols = (230, 200, 200, 200, 210, ww - 1040)
    heads = ("MATERIAL", "INICIAL (g)", "FINAL (g)", "PERDIÓ (g)", "% PERDIDO", "% QUE SIGUE AHÍ")
    yy = tabla_vacia(b, x0, yy, cols, heads, ("Polietileno (PE)", "Ácido poliláctico (PLA)", "Papel"), c, rh=64)
    yy += 20
    caja(b, x0, yy, ww, 186, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PALABRA QUE USÓ EL ESTUDIANTE", c)
    texto(b, x0 + 20, yy + 66, "«totalmente biodegradable» significaría que, al final, la masa del PLA fuera…", size=17)
    renglon(b, x0 + 20, yy + 110, x0 + ww / 2 - 20)
    pista(b, x0 + ww / 2, yy + 108, "¿lo muestra la tabla?")
    sino(b, x0 + ww / 2 + 160, yy + 92, c)
    pista(b, x0 + 20, yy + 158, "y lo que sí muestra la tabla es que…")
    renglon(b, x0 + 290, yy + 160, x0 + ww - 20)
    yy += 204
    return ojo(b, x0, yy, ww, "UNA CONCLUSIÓN PUEDE IR MÁS LEJOS QUE SUS DATOS",
               "Que algo cambie no dice cuánto cambió ni cuándo termina. Fíjate en la palabra «totalmente» de la "
               "conclusión: para afirmarla, el dato tendría que mostrar el final del proceso, no un punto del camino.")


# ───────── P4 · cafeína · grupos polares ─────────
def i4(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Cadena: grupo polar, agua, sangre", c,
                      "La estructura explica el efecto si puedes encadenar los pasos sin saltarte ninguno. Clasifica "
                      "las partes de la cafeína y completa la cadena desde la molécula hasta el cerebro.")
    x0, ww = x + 22, w - 44
    partes = ("grupo amida (C=O unido a N)", "nitrógeno de amina en el anillo",
              "enlaces C–H de los grupos metilo", "el agua de la bebida (H–O–H)")
    cols = (520, 240, ww - 760)
    yy = tabla_vacia(b, x0, yy, cols, ("PARTE", "¿POLAR O APOLAR?", "¿SE ATRAE CON EL AGUA? ¿POR QUÉ?"),
                     partes, c, rh=60)
    yy += 24
    eslab = ("la cafeína tiene grupos…", "por eso se mezcla con…", "y viaja disuelta en…", "hasta llegar a…")
    ew = (ww - 3 * 30) / 4
    for k, e in enumerate(eslab):
        bx = x0 + k * (ew + 30)
        caja(b, bx, yy, ew, 120, c, r=60 if False else 14, sw=2.4)
        b.append(f'<circle cx="{bx + 26}" cy="{yy + 28}" r="13" fill="white" stroke="{c}" stroke-width="2"/>')
        texto(b, bx + 26, yy + 34, str(k + 1), size=15, color=c, weight="700", anchor="middle")
        pista(b, bx + 48, yy + 34, e)
        renglon(b, bx + 16, yy + 92, bx + ew - 16)
        if k < 3:
            flecha(b, bx + ew + 2, yy + 60, bx + ew + 28, yy + 60, c, head=9)
    yy += 140
    return alto_profe(b, x0, yy, ww,
                      "Polar: una parte de la molécula atrae más los electrones y queda con una carga parcial. Pídele "
                      "al profe que explique por qué lo polar se disuelve en lo polar (como el azúcar en el agua) y lo "
                      "apolar no (como el aceite).")


# ───────── P5 · cafeína y teobromina ─────────
def i5(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Gemelas que no son idénticas: cafeína y teobromina", c,
                      "Cuenta los átomos de cada una y encuentra la diferencia exacta. Después piensa qué le pasa a "
                      "una llave a la que le cambias un diente.")
    x0, ww = x + 22, w - 44
    cols = (300, 150, 150, 150, 150, ww - 900)
    heads = ("MOLÉCULA", "C", "H", "N", "O", "¿DE DÓNDE SALE?")
    yy = tabla_vacia(b, x0, yy, cols, heads, ("Cafeína · C₈H₁₀N₄O₂", "Teobromina · C₇H₈N₄O₂", "Diferencia"),
                     c, rh=58)
    pista(b, x0 + 900 + 14, yy - 150, "del libro")
    pista(b, x0 + 900 + 14, yy - 92, "dato del profe (no está en el libro)")
    yy += 20
    # llave y cerradura
    caja(b, x0, yy, ww, 250, c, r=16)
    rot(b, x0 + 20, yy + 30, "LA LLAVE Y LA CERRADURA", c)
    kx, ky = x0 + 40, yy + 70
    # cerradura (receptor)
    b.append(f'<path d="M {kx} {ky} L {kx + 260} {ky} L {kx + 260} {ky + 50} L {kx + 220} {ky + 50} '
             f'L {kx + 220} {ky + 90} L {kx + 170} {ky + 90} L {kx + 170} {ky + 50} L {kx + 110} {ky + 50} '
             f'L {kx + 110} {ky + 90} L {kx + 60} {ky + 90} L {kx + 60} {ky + 50} L {kx} {ky + 50} Z" '
             f'fill="{tinte(c, 0.85)}" stroke="{c}" stroke-width="2.2"/>')
    pista(b, kx, ky + 130, "el receptor del sistema nervioso")
    pista(b, kx, ky + 152, "tiene huecos en sitios fijos")
    bx2 = x0 + 360
    for k, (tit, ps) in enumerate((("LA CAFEÍNA ENCAJA…", "¿en cuántos huecos? dibújala debajo"),
                                   ("LA TEOBROMINA ENCAJA…", "le falta un grupo: ¿qué hueco queda vacío?"))):
        bxx = bx2 + k * ((ww - 380) / 2 + 10)
        bw_ = (ww - 380) / 2 - 10
        caja(b, bxx, yy + 50, bw_, 180, c, r=12, dash="7,5")
        texto(b, bxx + 16, yy + 78, tit, size=16, color=c, weight="700")
        pista(b, bxx + 16, yy + 102, ps)
    yy += 270
    return ojo(b, x0, yy, ww, "PARECIDAS NO ES LO MISMO QUE IGUALES",
               "Dos moléculas con los mismos grupos pueden actuar distinto si esos grupos están en otro sitio o "
               "falta uno. Lo que decide el efecto es cómo encaja la molécula en el receptor, no solo de qué está "
               "hecha.")


# ───────── P6 · dos curvas de cafeína ─────────
def i6(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Dos curvas de cafeína en la sangre", c,
                      "Pasa la tabla del libro a la gráfica: un color o un símbolo para cada grupo (● no fumadores, "
                      "× fumadores). Luego lee la gráfica, no la memoria.")
    x0, ww = x + 22, w - 44
    gx, gy, gw, gh = x0 + 70, yy + 20, 640, 380
    caja(b, x0, yy, 740, gh + 90, c, r=16)
    # rejilla
    for i in range(7):
        xx = gx + i * gw / 6
        b.append(line(xx, gy, xx, gy + gh, "#E6E1EE", 1.4))
        texto(b, xx, gy + gh + 26, str(i), size=15, color=GRAY, anchor="middle")
    for j in range(8):
        yv = gy + gh - j * gh / 7
        b.append(line(gx, yv, gx + gw, yv, "#E6E1EE", 1.4))
        texto(b, gx - 12, yv + 5, str(j), size=15, color=GRAY, anchor="end")
    b.append(line(gx, gy, gx, gy + gh, INK, 2))
    b.append(line(gx, gy + gh, gx + gw, gy + gh, INK, 2))
    pista(b, gx + gw / 2, gy + gh + 54, "tiempo (h)", anchor="middle")
    b.append(T(x0 + 22, gy + gh / 2, ["mg/L"], 15, GRAY, style="italic", anchor="middle", rot=-90))
    # preguntas a la derecha
    rx, rw = x0 + 770, ww - 770
    qs = (("EL PICO", "¿a qué hora llega cada grupo a su punto más alto?"),
          ("LA BAJADA", "de las 2 h a las 6 h baja: A ____ mg/L · B ____ mg/L"),
          ("LA COMPARACIÓN", "elimina más rápido el grupo ___, porque…"))
    for k, (tit, ps) in enumerate(qs):
        py = yy + k * 158
        caja(b, rx, py, rw, 142, c, r=14)
        rot(b, rx + 16, py + 28, tit, c, size=14)
        svg, _ = TJ(rx + 16, py + 54, ps, rw - 32, 16, INK, lh=22)
        b.append(svg)
        renglon(b, rx + 16, py + 122, rx + rw - 16)
    yy += gh + 110
    return ojo(b, x0, yy, ww, "LEE LA FORMA DE LA CURVA, NO SOLO UN PUNTO",
               "Dos grupos pueden parecerse en un dato y diferir en otro: no basta mirar el punto más alto. "
               "Un buen análisis dice en qué se parecen, en qué se diferencian y qué explica la diferencia.")


# ───────── P7 · alcano y éster ─────────
def i7(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Cara a cara: la cadena del diésel y el éster", c,
                      "Mira los dos pedazos de molécula. Lo único que cambia es el grupo –COO–. Llena la tabla con "
                      "el texto del libro y escribe qué propiedad cambia por culpa de ese grupo.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    mols = (("DIÉSEL FÓSIL · un alcano", "– CH₂ – CH₂ – CH₂ – CH₂ – CH₃"),
            ("BIODIÉSEL · un éster metílico", "– CH₂ – CH₂ – C(=O) – O – CH₃"))
    for k, (tit, f) in enumerate(mols):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 110, c, r=14, fill=tinte(c, 0.94))
        rot(b, bx + 18, yy + 30, tit, c)
        texto(b, bx + 18, yy + 80, f, size=23, weight="700")
    yy += 128
    cols = (380, (ww - 380) / 2, (ww - 380) / 2)
    filas = ("¿Tiene átomos de oxígeno?", "Tipo de enlaces (¿se comparten electrones?)",
             "¿Polar o apolar?", "¿Qué propiedad cambia por eso?")
    yy = tabla_vacia(b, x0, yy, cols, ("", "ALCANO DEL DIÉSEL", "ÉSTER DEL BIODIÉSEL"), filas, c, rh=62, size=16)
    yy += 20
    return alto_profe(b, x0, yy, ww,
                      "Enlace covalente polar y enlace iónico no son lo mismo. En el éster los átomos siguen "
                      "compartiendo electrones (covalente), solo que el oxígeno los jala más. Pídele al profe un ejemplo "
                      "de enlace iónico (la sal, Na⁺Cl⁻) para comparar.")


# ───────── P8 · receta duplicada ─────────
def i8(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Si la receta se duplica, todo se duplica", c,
                      "Los coeficientes de una ecuación balanceada son una receta en moles. Escribe cuánto entra y "
                      "cuánto sale de cada sustancia cuando cambias la cantidad de biodiésel.")
    x0, ww = x + 22, w - 44
    texto(b, x0, yy + 30, "C₁₉H₃₆O₂  +  27 O₂  →  19 CO₂  +  18 H₂O", size=26, weight="700")
    yy += 56
    cols = (250, (ww - 250) / 4, (ww - 250) / 4, (ww - 250) / 4, (ww - 250) / 4)
    heads = ("SI QUEMO…", "BIODIÉSEL (mol)", "O₂ QUE GASTA (mol)", "CO₂ QUE SALE (mol)", "H₂O QUE SALE (mol)")
    yy = tabla_vacia(b, x0, yy, cols, heads, ("la receta", "el doble", "el triple"), c, rh=64)
    yy += 20
    caja(b, x0, yy, ww, 120, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PREGUNTA PIDE…", c)
    pista(b, x0 + 20, yy + 66, "¿de qué sustancia?")
    renglon(b, x0 + 170, yy + 68, x0 + ww / 2 - 20)
    pista(b, x0 + ww / 2, yy + 66, "¿a partir de cuántos moles?")
    renglon(b, x0 + ww / 2 + 210, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 104, "entonces miro la columna:")
    renglon(b, x0 + 210, yy + 106, x0 + ww / 2 - 20)
    yy += 138
    return trampa(b, x0, yy, ww, "En la ecuación hay varios números y todos parecen respuestas:",
                  "27, 19 y 18 están escritos ahí mismo. Antes de marcar, comprueba que el número que elegiste "
                  "salga de la columna de la sustancia que te preguntan y de la fila de la cantidad correcta.", c)


# ───────── P9 · semáforo de emisiones ─────────
def i9(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El semáforo de las emisiones", c,
                      "Para cada contaminante, compara el diésel fósil con el biodiésel usando la tabla del libro. "
                      "Calcula el cambio y marca si bajó, quedó igual o subió.")
    x0, ww = x + 22, w - 44
    cols = (300, 190, 190, 200, ww - 880)
    heads = ("CONTAMINANTE", "DIÉSEL", "BIODIÉSEL", "CAMBIO", "")
    filas = ("CO₂ (g/km)", "SO₂ (g/km)", "Partículas (mg/km)")
    yy0 = yy
    yy = tabla_vacia(b, x0, yy, cols, heads, filas, c, rh=70, sin_renglon=(4,))
    bx = x0 + 880 + 40
    for j, lab in enumerate(("BAJÓ", "IGUAL", "SUBIÓ")):
        rot(b, bx + 20 + j * 100, yy0 + 30, lab, c, size=14, anchor="middle")
    for k in range(3):
        ry = yy0 + 48 + k * 70
        for j, col in enumerate(("#30843C", "#C9821B", "#A82424")):
            b.append(f'<circle cx="{bx + 20 + j * 100}" cy="{ry + 35}" r="18" fill="white" stroke="{col}" '
                     f'stroke-width="3"/>')
    yy += 24
    caja(b, x0, yy, ww, 160, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE LA TABLA NO DICE", c)
    pista(b, x0 + 20, yy + 66, "¿algún contaminante llegó a cero?")
    sino(b, x0 + 290, yy + 50, c)
    pista(b, x0 + 470, yy + 66, "¿cuál?")
    renglon(b, x0 + 530, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 108, "¿el biodiésel deja de emitir CO₂?")
    sino(b, x0 + 290, yy + 92, c)
    pista(b, x0 + 470, yy + 108, "¿cuánto emite todavía?")
    renglon(b, x0 + 640, yy + 110, x0 + ww - 20)
    pista(b, x0 + 20, yy + 146, "una opción vale solo si cada palabra suya se sostiene con mi semáforo")
    yy += 178
    return yy


# ───────── P10 · tres hallazgos ─────────
def i10(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Tres hallazgos, tres causas", c,
                      "El equipo encontró tres resultados. Al lado de cada uno escribe qué parte de la molécula lo "
                      "causa y a qué combustible le conviene. La explicación coherente es la que no contradice "
                      "ninguno de los tres.")
    x0, ww = x + 22, w - 44
    hall = ("Los alcanos dan más energía por mol.",
            "El biodiésel emite menos azufre y partículas, pero CO₂ parecido.",
            "Si la combustión es incompleta, salen aldehídos y peróxidos.")
    cols = (500, 380, ww - 880)
    yy = tabla_vacia(b, x0, yy, cols, ("HALLAZGO DEL LIBRO", "LO CAUSA…", "LE CONVIENE A…"), hall, c,
                     rh=78, size=16)
    yy += 20
    caja(b, x0, yy, ww, 120, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "MI FILTRO", c)
    pista(b, x0 + 20, yy + 64, "opción que contradice el hallazgo 1:")
    renglon(b, x0 + 280, yy + 66, x0 + ww / 2 - 10)
    pista(b, x0 + ww / 2 + 10, yy + 64, "y el hallazgo 2:")
    renglon(b, x0 + ww / 2 + 130, yy + 66, x0 + ww - 20)
    pista(b, x0 + 20, yy + 104, "opción que contradice el hallazgo 3:")
    renglon(b, x0 + 280, yy + 106, x0 + ww / 2 - 10)
    yy += 140
    return ojo(b, x0, yy, ww, "OJO CON LA PALABRA «ALQUENOS»",
               "El biodiésel es una mezcla de ésteres (con el grupo –COO–); algunas de sus cadenas tienen dobles "
               "enlaces, pero no es un alqueno puro. Y su bajo azufre viene sobre todo de la materia prima: los "
               "aceites vegetales casi no traen azufre. El profe lo aclara en clase.")


Q = {1: dict(n=1, est=4, pag=182, ctx="Etanol en la gasolina · por qué aumentan los aldehídos",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=2, pag=182, ctx="Plástico PLA y glucosa · la masa se conserva",
             comp="Uso comprensivo del conocimiento científico", inst=i2),
     3: dict(n=3, est=3, pag=182, ctx="Tres bolsas en seis meses · ¿el PLA desaparece?",
             comp="Indagación", inst=i3),
     4: dict(n=4, est=1, pag=183, ctx="Cafeína · de su estructura a su efecto",
             comp="Explicación de fenómenos", inst=i4),
     5: dict(n=5, est=1, pag=183, ctx="Cafeína y teobromina · por qué estimulan distinto",
             comp="Explicación de fenómenos", inst=i5),
     6: dict(n=6, est=3, pag=184, ctx="Cafeína en fumadores y no fumadores · qué dice la tabla",
             comp="Indagación", inst=i6),
     7: dict(n=7, est=1, pag=184, ctx="Biodiésel y diésel · qué cambia el grupo éster",
             comp="Explicación de fenómenos", inst=i7),
     8: dict(n=8, est=2, pag=185, ctx="Combustión del biodiésel · moles de CO₂",
             comp="Uso comprensivo del conocimiento científico", inst=i8),
     9: dict(n=9, est=3, pag=185, ctx="Emisiones de diésel y biodiésel · el análisis pertinente",
             comp="Indagación", inst=i9),
     10: dict(n=10, est=4, pag=185, ctx="Alcanos y biodiésel · explicar las diferencias",
              comp="Explicación de fenómenos", inst=i10)}


def build(pages=(211, 212, 214, 215, 216)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"qui5_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
