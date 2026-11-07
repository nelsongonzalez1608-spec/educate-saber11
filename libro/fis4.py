#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 4 · componente físico, eventos ondulatorios · páginas 247–253.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 4» de Física (fuente_libro/FÍSICA), páginas 236–239.
Casos: el láser y la doble rendija (1), la onda que pasa de una cuerda delgada a una gruesa (2),
el láser rojo que entra al agua de una cubeta (3), el Wi-Fi del apartamento medido en tres puntos
(4 y 5), los dos vasos de agua de la escena de Jurassic Park (6 y 7) y las ondas en placas de
aluminio, plástico y caucho (8 a 10).

Claves verificadas (resueltas a mano contra el texto, la tabla y las figuras del libro, no copiadas,
7 nov 2026):

    1·D  2·B  3·B  4·A  5·B  6·A  7·A  8·A  9·C  10·D

Cómo se resolvieron:
  1 · Separación entre franjas Δy ≈ λ·L/d. Los ángulos de los máximos dependen de λ y d, no de L;
      al acercar la pantalla (L menor) esos mismos ángulos caen más juntos → D. A (la luz «pierde
      energía»), B (menos intensidad, menos franjas) y C (reflexión) no explican la geometría.
  2 · La frecuencia la fija la fuente (constante). En la parte gruesa hay más masa por metro y la
      onda va más lenta; λ = v/f → λ también disminuye → B. A y D cambian la frecuencia; C dice
      que la velocidad no cambia y que λ aumenta.
  3 · Al pasar del aire al agua la luz va más lenta y se acerca a la normal → B, por la razón.
      OJO (hallazgo Alta): en el esquema del libro el rayo que se acerca a la normal DENTRO del agua
      está rotulado «A» (hay dos rayos con la letra A, uno en el aire y otro en el agua) y el rayo
      «B» está en el aire. La razón de B es la correcta, pero la letra del dibujo no coincide.
  4 · El punto C está a la misma distancia que A (descarta B) y la diferencia es la habitación de
      paredes metálicas. El metal refleja la mayor parte de la onda de radio que llega a la pared
      (efecto de jaula): entra poca señal → A. D (interferencia destructiva por múltiples
      reflexiones adentro) es defendible a medias: la interferencia crea zonas de más y de menos
      señal, pero no baja el promedio de la energía que entró; además el router está afuera.
      C es falsa (el metal no «amplifica» ni cambia la frecuencia). Clave propuesta A, con reserva
      (hallazgo Media: la editorial podría tener D).
  5 · −45 − (−78) = 33 dB. Cada 10 dB es un factor 10 en potencia: 10^3,3 ≈ 2000 → la señal en C es
      unas dos mil veces más débil que en A → B. A trata los dB como lineales; C y D confunden
      decibeles con vatios y con hercios.
  6 · Mayor amplitud ↔ el vaso recibe más energía de la vibración; la conclusión que el texto
      busca es que ese vaso está más cerca del origen → A. B mezcla frecuencia y energía; C habla
      de sonido (el texto dice que no se escucha); D culpa al agua del vaso de absorber según la
      distancia. OJO (hallazgo Media): los dos vasos están en el mismo tablero, a casi la misma
      distancia de un dinosaurio lejano; lo que distingue a los vasos (amplitud distinta y
      frecuencia distinta) se explica mejor por la cantidad de agua o el vaso (su frecuencia propia).
      La observación no permite establecer A con seguridad.
  7 · Para que la distancia sea la única variable que afecta la intensidad, lo primero es que la
      fuente vibre igual en cada ensayo → A. B y C también son variables a controlar (Atención),
      pero la amplitud de la fuente es la que más pesa sobre lo que se mide; D (la luz) no influye.
  8 · En un material más rígido la onda va más rápido: en el mismo segundo llega más lejos.
      Aluminio > plástico > caucho en radio → A (coincide con los radios de la pregunta 10:
      12, 8 y 3 cm). B, C y D desordenan los materiales.
  9 · Clave propuesta C, con reserva (hallazgo Alta). La rapidez de una onda en un sólido depende
      de su rigidez (módulo de elasticidad) y de su densidad: el caucho es muy poco rígido. La
      absorción (C) reduce la amplitud y el alcance, no la rapidez; aun así es la única opción que
      dice algo cierto del caucho y la que sostiene el propio texto del libro («en caucho llegaría
      mucho más tarde por su absorción»). A es falsa (el caucho, ≈1,1–1,5 g/cm³, es menos denso que
      el aluminio, 2,7 g/cm³); B y D no tienen apoyo. Ninguna opción da la razón física principal.
 10 · Mismo tiempo t = 1 s: el caucho recorre 3 cm (v = 3 cm/s) y el aluminio 12 cm (v = 12 cm/s);
      en el tiempo en que el caucho recorre 3 cm, el aluminio recorre 12 cm → D.

Reparto: A 4 · B 3 · C 1 · D 2. Sin una letra dominante (6, 7 y 8 seguidas en A: Atención).

Estrategias:
    1 · La fuente pone la frecuencia   (2, 3, 9      · ICFES 9 del cuadernillo 2025)     azul
    2 · Dibújalo antes de elegir       (1, 8         · ICFES 32 del cuadernillo 2025)    rojo
    3 · Concluye solo lo observado     (6, 7         · ICFES 70 de 2016-1 2.ª ses.)      morado
    4 · Lee la tabla y su escala       (4, 5, 10     · ICFES 48 del cuadernillo 2025)    oro

Hojas: 247 fis4_t1 (1-2) · 248 fis4_t2 (3-4) · 249 fis4_i1 · 250 fis4_t3 (5-6) ·
       251 fis4_t4 (7-8) · 252 fis4_t5 (9-10) · 253 fis4_i2.
"""
from taller_base import *

configurar("Física", 4, "físico · eventos ondulatorios",
           tema="La fuente marca el ritmo, el medio la rapidez",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("La fuente pone la frecuencia", EDU_AZUL),
       2: ("Dibújalo antes de elegir", EDU_ROJO),
       3: ("Concluye solo lo observado", MORADO),
       4: ("Lee la tabla y su escala", EDU_ORO)}
usar_estrategias(EST)
AZ, RO, MO, OR = (EST[k][1] for k in (1, 2, 3, 4))
AGUA = "#DCEAF7"


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def letra(b, cx, cy, L, c, r=17, size=16):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="2"/>')
    b.append(T(cx, cy + size * 0.38, [L], size, c, weight="700", anchor="middle"))


def frase_hueco(b, x, y, w, texto, c, h=50, size=18):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [texto], size, INK, weight="700"))
    return y + h


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12):
    b.append(line(x1, y1, x2, y2, c, sw))
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (-1, 1):
        a = ang + math.pi + s * 0.45
        b.append(line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), c, sw))


def casillas(b, x, y, labels, c, paso=150, size=16):
    for k, lab in enumerate(labels):
        b.append(checkbox(x + k * paso, y, s=10, c=c))
        b.append(T(x + k * paso + 28, y + 16, [lab], size, GRAY))


def onda(b, x, y, w, amp, lam, c, sw=2.4):
    """Onda senoidal como polilínea (medible)."""
    pts = []
    n = max(int(w / 4), 2)
    for i in range(n + 1):
        px = x + w * i / n
        pts.append(f"{px:.1f},{y - amp * math.sin(2 * math.pi * (px - x) / lam):.1f}")
    b.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{c}" stroke-width="{sw}"/>')


# ───────── P1 · doble rendija · la pantalla más cerca ─────────
def i1(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Los mismos ángulos sobre dos pantallas", c,
                      "Desde la rendija salen las direcciones de las franjas claras; esas direcciones (los ángulos) "
                      "no cambian si se mueve la pantalla. Marca dónde cae cada dirección en la pantalla lejana y "
                      "en la cercana, y mide con tu regla la separación.")
    x0, ww = x + 22, w - 44
    dh = 330
    caja(b, x0, yy, ww, dh, c, r=16)
    rx, ry = x0 + 90, yy + dh / 2
    b.append(rect(rx - 8, yy + 30, 16, dh - 60, "#C9CED6", r=3))
    b.append(rect(rx - 8, ry - 22, 16, 12, "white", r=0))
    b.append(rect(rx - 8, ry + 10, 16, 12, "white", r=0))
    rot(b, rx, yy + 24, "RENDIJA", c, size=12, anchor="middle")
    p_cerca, p_lejos = x0 + 520, x0 + 980
    for px, t in ((p_cerca, "PANTALLA CERCA"), (p_lejos, "PANTALLA LEJOS")):
        b.append(line(px, yy + 40, px, yy + dh - 30, INK, 3))
        rot(b, px, yy + 30, t, c, size=12, anchor="middle")
    for k in (-2, -1, 0, 1, 2):
        ang = k * 0.065
        x2 = p_lejos + 30
        b.append(line(rx + 8, ry, x2, ry + (x2 - rx) * math.tan(ang), GRAY, 1.6, dash="6,6"))
    pista(b, rx + 40, yy + dh - 40, "marca con un punto dónde cruza cada línea")
    pista(b, rx + 40, yy + dh - 18, "las dos pantallas, y mide entre dos marcas vecinas")
    yy += dh + 16
    half = (ww - 24) / 2
    for k, rt in enumerate(("SEPARACIÓN ENTRE DOS MARCAS, PANTALLA LEJOS", "SEPARACIÓN ENTRE DOS MARCAS, PANTALLA CERCA")):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 90, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=13)
        b.append(T(px + 18, yy + 70, ["medí: ________ mm"], 18, INK))
    yy += 106
    yy = frase_hueco(b, x0, yy, ww, "Los ángulos ______________ ; las franjas quedan más juntas porque la distancia "
                                    "______________ .", c)
    return ojo(b, x0, yy + 16, ww, "LA ENERGÍA NO DIBUJA FRANJAS",
               "que la luz llegue con más o menos intensidad cambia qué tan brillantes se ven, no dónde caen. Para "
               "explicar dónde caen las franjas, la razón tiene que hablar de direcciones y distancias.")


# ───────── P2 · cuerda delgada y gruesa ─────────
def i2(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La mano marca el ritmo; la cuerda, la rapidez", c,
                      "En una onda hay algo que pone la fuente (la mano que agita) y algo que pone el medio (la "
                      "cuerda). Decide quién manda en cada magnitud y llena la tabla con ↑ (aumenta), ↓ (disminuye) "
                      "o = (igual) al pasar al tramo grueso.")
    x0, ww = x + 22, w - 44
    dh = 150
    caja(b, x0, yy, ww, dh, c, r=16)
    mid = x0 + ww / 2
    onda(b, x0 + 40, yy + 80, mid - x0 - 40, 40, 150, INK, sw=2)
    b.append(line(mid, yy + 80, x0 + ww - 40, yy + 80, INK, 7))
    b.append(line(mid, yy + 20, mid, yy + 140, GRAY, 1.6, dash="5,5"))
    pista(b, x0 + 40, yy + 140, "tramo delgado")
    pista(b, x0 + ww - 40, yy + 140, "tramo grueso: dibuja tú la onda que esperas", anchor="end")
    yy += dh + 16
    cols = (("MAGNITUD", 330), ("¿QUIÉN LA PONE?", 400), ("AL ENTRAR AL TRAMO GRUESO", ww - 730))
    px = x0
    for t, cw in cols:
        caja(b, px, yy, cw, 44, c, r=0, fill=A["bg"])
        rot(b, px + 16, yy + 28, t, c, size=13)
        px += cw
    for k, mag in enumerate(("frecuencia  f", "rapidez  v", "longitud de onda  λ")):
        ry = yy + 44 + k * 54
        px = x0
        for j, (t, cw) in enumerate(cols):
            caja(b, px, ry, cw, 54, c, r=0)
            if j == 0:
                b.append(T(px + 16, ry + 34, [mag], 18, INK))
            elif j == 1:
                casillas(b, px + 20, ry + 16, ("la fuente", "la cuerda", "las dos"), c, paso=125, size=15)
            else:
                casillas(b, px + 20, ry + 16, ("↑", "↓", "="), c, paso=110, size=18)
            px += cw
    yy += 44 + 3 * 54 + 16
    yy = frase_hueco(b, x0, yy, ww, "Si  v = λ · f  y  f  no cambia,  v  y  λ  cambian en sentido ______________ (el mismo / contrario).", c)
    return alto_profe(b, x0, yy + 16, ww,
                      "Pregúntale al profe por qué una onda viaja más despacio en una cuerda gruesa (más masa por "
                      "cada metro) que en una delgada con la misma tensión.")


# ───────── P3 · láser en la cubeta · qué trayectoria ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La normal manda: ángulo de entrada y de salida", c,
                      "La frecuencia de la luz la pone el láser; el agua solo cambia su rapidez. Dibuja la normal, "
                      "mide con transportador el ángulo del rayo que llega y dibuja tú el rayo dentro del agua "
                      "según la regla.")
    x0, ww = x + 22, w - 44
    dw, dh = 520, 380
    caja(b, x0, yy, dw, dh, c, r=16)
    sx, sy = x0 + dw / 2, yy + 170
    b.append(rect(x0 + 2, sy, dw - 4, dh - 172, AGUA, r=0))
    b.append(line(x0 + 2, sy, x0 + dw - 2, sy, INK, 2.4))
    b.append(T(x0 + 22, sy - 14, ["AIRE"], 15, INK, weight="700"))
    b.append(T(x0 + 22, sy + 30, ["AGUA"], 15, INK, weight="700"))
    flecha(b, sx - 125, sy - 125, sx - 3, sy - 3, "#C0392B", sw=3.2, head=12)
    b.append(T(sx - 132, sy - 128, ["láser"], 15, INK, weight="700", anchor="end"))
    pista(b, sx + 14, sy - 130, "dibuja la normal")
    pista(b, sx + 14, sy + 120, "dibuja el rayo en el agua")
    rx = x0 + dw + 24
    rw = x0 + ww - rx
    cols = (("", 140), ("RAPIDEZ DE LA LUZ", (rw - 140) / 2), ("ÁNGULO CON LA NORMAL", (rw - 140) / 2))
    px = rx
    for t, cw in cols:
        caja(b, px, yy, cw, 44, c, r=0, fill=A["bg"])
        if t:
            rot(b, px + cw / 2, yy + 28, t, c, size=12, anchor="middle")
        px += cw
    for k, med in enumerate(("aire", "agua")):
        ry = yy + 44 + k * 70
        px = rx
        for j, (t, cw) in enumerate(cols):
            caja(b, px, ry, cw, 70, c, r=0)
            if j == 0:
                b.append(T(px + 18, ry + 42, [med], 18, INK, weight="700"))
            elif j == 1:
                casillas(b, px + 16, ry + 24, ("mayor", "menor"), c, paso=100, size=15)
            else:
                b.append(T(px + 16, ry + 44, ["______ °"], 18, INK))
            px += cw
    ry = yy + 44 + 2 * 70 + 16
    caja(b, rx, ry, rw, dh - (ry - yy), c, r=14)
    rot(b, rx + 18, ry + 28, "LA REGLA, EN MIS PALABRAS", c, size=13)
    b.append(T(rx + 18, ry + 66, ["Si la luz entra a un medio donde va más lenta,"], 16, INK))
    b.append(T(rx + 18, ry + 94, ["el rayo se __________ de la normal."], 16, INK))
    pista(b, rx + 18, ry + 132, "¿y la frecuencia, cambia?   sí  /  no")
    yy += dh + 16
    return alto_profe(b, x0, yy, ww,
                      "En el esquema del libro hay DOS rayos con la letra A, uno en el aire y otro en el agua, y el "
                      "rayo B está en el aire. Ponle tu propia letra a cada rayo y pregúntale al profe cómo leer las "
                      "opciones: un rayo que se queda en el aire no pasó al agua.")


# ───────── P4 · Wi-Fi · por qué baja la descarga en C ─────────
def i4(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El plano de la casa con sus tres medidas", c,
                      "Pasa la tabla al plano: debajo de cada punto escribe su distancia, lo que hay entre el router "
                      "y él, y sus dos medidas. Después compara C con el punto que está a su misma distancia.")
    x0, ww = x + 22, w - 44
    ph = 260
    caja(b, x0, yy, ww, ph, c, r=16)
    rx_, ry_ = x0 + 110, yy + 120
    b.append(rect(rx_ - 30, ry_ - 20, 60, 40, "white", r=6, stroke=INK, sw=2.4))
    b.append(T(rx_, ry_ + 6, ["router"], 13, INK, weight="700", anchor="middle"))
    pts = (("A", x0 + 420, None), ("B", x0 + 740, "concreto"), ("C", x0 + 1060, "metal"))
    for L, px, pared in pts:
        if pared == "concreto":
            b.append(rect(px - 80, yy + 40, 16, 120, "#C9CED6", r=2))
            pista(b, px - 72, yy + 34, "pared de concreto", anchor="middle")
        elif pared == "metal":
            b.append(rect(px - 110, yy + 30, 220, 120, "none", r=4, stroke=INK, sw=5))
            pista(b, px, yy + 50, "paredes metálicas", anchor="middle")
        letra(b, px, ry_, L, c, r=20, size=18)
        for j, t in enumerate(("distancia: ________", "en medio: ________", "dBm: ______  Mbps: ______")):
            b.append(T(px - 100, yy + 180 + j * 26, [t], 15, INK))
    yy += ph + 16
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "C CONTRA EL PUNTO QUE ESTÁ A SU MISMA DISTANCIA", c, size=14)
    b.append(T(x0 + 20, yy + 72, ["Se parecen en ______________________ ; lo único distinto es ______________________ ."],
               17, INK))
    b.append(T(x0 + 20, yy + 116, ["Cuando una onda de radio llega a una pared de metal, casi toda"], 17, INK))
    casillas(b, x0 + 540, yy + 100, ("la atraviesa", "se refleja", "se vuelve sonido"), c, paso=160, size=15)
    yy += 166
    return trampa(b, x0, yy, ww, "Una hipótesis tiene que cuadrar con TODO el plano:",
                  "si una opción culpa a la distancia, revisa a qué distancia está C. Y si explica con lo que pasa "
                  "dentro de la habitación, pregúntate primero cuánta señal alcanzó a entrar.", c)


# ───────── P5 · Wi-Fi · 33 dB de diferencia ─────────
def i5(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La escalera de los decibeles", c,
                      "En una escala logarítmica no se resta: se multiplica. La regla es esta: cada 10 dB menos, la "
                      "potencia se divide entre 10; y 3 dB menos, se divide más o menos entre 2. Baja la escalera "
                      "desde A hasta C.")
    x0, ww = x + 22, w - 44
    pasos = ("A · −45", "−55", "−65", "−75", "C · −78")
    n = len(pasos)
    sw_, sh = (ww - 40) / n, 64
    for k, p in enumerate(pasos):
        px = x0 + 20 + k * sw_
        py = yy + 20 + k * 52
        caja(b, px, py, sw_ - 16, sh, c, r=10, fill=A["bg"] if k in (0, n - 1) else "white")
        b.append(T(px + (sw_ - 16) / 2, py + 26, [f"{p} dBm"], 16, INK, weight="700", anchor="middle"))
        pista(b, px + (sw_ - 16) / 2, py + 50, "potencia ÷ ______" if k else "potencia de A", anchor="middle")
        if k < n - 1:
            flecha(b, px + sw_ - 20, py + sh / 2, px + sw_ + 4, py + 52 + sh / 2, c, sw=2.2, head=9)
    yy += 20 + (n - 1) * 52 + sh + 20
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA CUENTA DE LA ESCALERA", c, size=14)
    b.append(T(x0 + 20, yy + 76, ["De A a C la potencia se divide entre  ____ × ____ × ____ × ____  ≈  ____________ ."],
               18, INK))
    b.append(T(x0 + 20, yy + 122, ["Entonces la señal en C es más débil que en A unas ____________ veces."], 18, INK))
    yy += 166
    return ojo(b, x0, yy, ww, "UN DECIBEL NO ES UN VATIO NI UN HERCIO",
               "el dB compara dos potencias; no es la potencia misma ni la frecuencia. Si una opción convierte los 33 "
               "dB en vatios o en hercios, está cambiando de magnitud.")


# ───────── P6 · los vasos de Jurassic Park · qué conclusión ─────────
def _vaso(b, cx, by, c, ondas):
    b.append(f'<path d="M {cx - 40} {by - 110} L {cx - 30} {by} L {cx + 30} {by} L {cx + 40} {by - 110}" '
             f'fill="none" stroke="{INK}" stroke-width="2.6"/>')
    b.append(f'<ellipse cx="{cx}" cy="{by - 70}" rx="36" ry="10" fill="{AGUA}" stroke="{INK}" stroke-width="1.6"/>')
    for r in range(1, ondas + 1):
        b.append(f'<ellipse cx="{cx}" cy="{by - 70}" rx="{r * 32 / ondas:.1f}" ry="{r * 8 / ondas:.1f}" fill="none" '
                 f'stroke="{c}" stroke-width="1.4"/>')


def i6(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Dos vasos en el mismo tablero", c,
                      "Antes de concluir, separa lo que el texto dice que se vio de lo que habría que suponer. Mira "
                      "dónde están los vasos y dónde está el origen de la vibración: ¿qué tan distintas son sus "
                      "distancias?")
    x0, ww = x + 22, w - 44
    dh = 230
    caja(b, x0, yy, ww, dh, c, r=16)
    b.append(rect(x0 + 40, yy + 168, 420, 18, "#C9CED6", r=4))
    pista(b, x0 + 250, yy + 210, "el tablero del carro", anchor="middle")
    _vaso(b, x0 + 160, yy + 168, c, 2)
    _vaso(b, x0 + 340, yy + 168, c, 5)
    b.append(T(x0 + 160, yy + 40, ["vaso 1"], 15, INK, weight="700", anchor="middle"))
    b.append(T(x0 + 340, yy + 40, ["vaso 2"], 15, INK, weight="700", anchor="middle"))
    gx = x0 + ww - 120
    b.append(f'<path d="M {gx - 60} {yy + 186} L {gx - 50} {yy + 120} Q {gx - 20} {yy + 80} {gx + 20} {yy + 96} '
             f'L {gx + 50} {yy + 70} L {gx + 60} {yy + 90} L {gx + 30} {yy + 120} L {gx + 40} {yy + 186} Z" '
             f'fill="#EEF0F4" stroke="{GRAY}" stroke-width="2"/>')
    pista(b, gx, yy + 210, "el dinosaurio, lejos", anchor="middle")
    b.append(line(x0 + 500, yy + 120, gx - 90, yy + 120, GRAY, 1.6, dash="8,6"))
    pista(b, (x0 + 500 + gx - 90) / 2, yy + 108, "distancia: ¿parecida o muy distinta para los dos vasos?",
          anchor="middle")
    yy += dh + 16
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("LO QUE EL TEXTO DICE QUE SE VIO", "en cada vaso y en el carro"),
                                  ("LO QUE HABRÍA QUE SUPONER", "datos que el texto no da"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 160, c, r=14, dash=None if k == 0 else "8,6")
        rot(b, px + 18, yy + 28, rt, c, size=14)
        pista(b, px + 18, yy + 52, ps)
        for j in range(3):
            renglon(b, px + 18, yy + 88 + j * 30, px + half - 18)
    yy += 176
    return ojo(b, x0, yy, ww, "EL TEXTO DICE QUE NO SE ESCUCHA NINGÚN SONIDO",
               "una conclusión tiene que salir de lo que se vio en los vasos. Si habla de algo que nadie oyó o nadie "
               "midió, ponla en la columna de lo que habría que suponer.")


# ───────── P7 · vasos alineados · qué controlar ─────────
def i7(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Lo que muevo, lo que mido y lo que dejo quieto", c,
                      "En un buen experimento solo cambia una cosa. Llena los tres cajones y después ordena lo que "
                      "dejaste quieto: ¿cuál cambiaría más lo que mides si se te olvida controlarlo?")
    x0, ww = x + 22, w - 44
    cw = (ww - 2 * 24) / 3
    cajones = (("LO QUE MUEVO A PROPÓSITO", "una sola cosa", 1), ("LO QUE MIDO", "lo que observo en cada vaso", 1),
               ("LO QUE DEJO QUIETO", "escribe al menos cuatro", 4))
    for k, (rt, ps, n) in enumerate(cajones):
        px = x0 + k * (cw + 24)
        caja(b, px, yy, cw, 250, c, r=14, sw=2.4)
        rot(b, px + 18, yy + 30, rt, c, size=14)
        pista(b, px + 18, yy + 56, ps)
        for j in range(n if n > 1 else 2):
            renglon(b, px + 18, yy + 100 + j * 40, px + cw - 18)
    yy += 266
    caja(b, x0, yy, ww, 170, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL ORDEN DE LO QUE DEJO QUIETO", c, size=14)
    pista(b, x0 + 380, yy + 30, "1 = lo que más cambiaría la intensidad de las ondas")
    for k in range(4):
        px = x0 + 20 + k * ((ww - 40) / 4)
        b.append(T(px, yy + 82, [f"{k + 1} ·"], 18, INK, weight="700"))
        renglon(b, px + 34, yy + 86, px + (ww - 40) / 4 - 24)
    b.append(T(x0 + 20, yy + 140, ["El 1 lo puse primero porque si cambia,"], 17, INK))
    renglon(b, x0 + 330, yy + 144, x0 + ww - 20)
    yy += 186
    return trampa(b, x0, yy, ww, "Pregúntale a cada opción si toca lo que mides:",
                  "algo que no puede mover el agua de un vaso no hace falta controlarlo. Y entre dos cosas que sí "
                  "influyen, ¿cuál cambia directamente la intensidad de las ondas que mides?", c)


# ───────── P8 · ondas en tres placas · qué figura ─────────
def i8(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Tres placas, un segundo: dibuja tú los anillos", c,
                      "En el mismo segundo, la onda llega más lejos donde viaja más rápido. Ordena los materiales "
                      "de más rígido a más blando, decide en cuál va más rápido y dibuja el anillo de afuera en cada "
                      "placa, del tamaño que esperas.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "DE MÁS RÍGIDO A MÁS BLANDO", c, size=14)
    for k in range(3):
        px = x0 + 20 + k * 330
        b.append(T(px, yy + 80, [f"{k + 1} ·"], 18, INK, weight="700"))
        renglon(b, px + 34, yy + 84, px + 280)
    yy += 120
    pw = (ww - 2 * 24) / 3
    for k, m in enumerate(("aluminio", "plástico", "caucho")):
        px = x0 + k * (pw + 24)
        caja(b, px, yy, pw, 300, c, r=16)
        b.append(T(px + pw / 2, yy + 32, [m], 18, INK, weight="700", anchor="middle"))
        cx_, cy_ = px + pw / 2, yy + 170
        b.append(f'<circle cx="{cx_}" cy="{cy_}" r="7" fill="{INK}"/>')
        b.append(f'<circle cx="{cx_}" cy="{cy_}" r="120" fill="none" stroke="{LGRAY}" stroke-width="1.6" '
                 f'stroke-dasharray="4,6"/>')
        pista(b, cx_, yy + 290, "el golpe, en el centro", anchor="middle")
    yy += 316
    yy = frase_hueco(b, x0, yy, ww, "Más rápida en el ______________ → anillo más grande en el ______________ .", c)
    return alto_profe(b, x0, yy + 16, ww,
                      "Pregúntale al profe por qué una onda viaja más rápido en un material rígido (que recupera su "
                      "forma enseguida) que en uno blando como el caucho.")


# ───────── P9 · el caucho es más lento · la razón ─────────
def i9(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "¿Cambia la rapidez o cambia el tamaño?", c,
                      "No es lo mismo qué tan rápido viaja una onda que qué tan grande llega o cuánto dura. Clasifica "
                      "cada propiedad: ¿qué le cambia a la onda? Usa los datos de densidad para poner a prueba la "
                      "razón de la densidad.")
    x0, ww = x + 22, w - 44
    props = ("la rigidez del material", "la densidad del material", "la energía que el material absorbe",
             "la fuerza del golpe", "el tamaño de la placa")
    cols = (("LA PROPIEDAD", 440), ("¿QUÉ LE CAMBIA A LA ONDA?", ww - 440))
    px = x0
    for t, cw in cols:
        caja(b, px, yy, cw, 44, c, r=0, fill=A["bg"])
        rot(b, px + 16, yy + 28, t, c, size=13)
        px += cw
    for k, p in enumerate(props):
        ry = yy + 44 + k * 52
        caja(b, x0, ry, cols[0][1], 52, c, r=0)
        b.append(T(x0 + 16, ry + 33, [p], 17, INK))
        caja(b, x0 + cols[0][1], ry, cols[1][1], 52, c, r=0)
        casillas(b, x0 + cols[0][1] + 20, ry + 16, ("su rapidez", "su tamaño o cuánto dura", "nada de eso"),
                 c, paso=230, size=15)
    yy += 44 + 5 * 52 + 16
    caja(b, x0, yy, ww, 100, c, r=14)
    rot(b, x0 + 20, yy + 30, "DATOS PARA PONER A PRUEBA LA DENSIDAD", c, size=14)
    b.append(T(x0 + 20, yy + 72, ["aluminio ≈ 2,7 g/cm³    ·    caucho ≈ 1,1 a 1,5 g/cm³    →   ¿el caucho es más "
                                  "denso?   sí  /  no"], 17, INK))
    yy += 116
    return alto_profe(b, x0, yy, ww,
                      "Ninguna opción habla de la rigidez. Pregúntale al profe cuál opción dice algo cierto del "
                      "caucho, si eso explica la rapidez o solo el tamaño de la onda, y cuál marcar en ese caso.")


# ───────── P10 · radios a un segundo · cuánto recorre en el aluminio ─────────
def i10(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Mismo reloj, tres reglas", c,
                      "Los radios se midieron en el mismo instante, un segundo después del golpe: con eso sacas la "
                      "rapidez de cada placa. Después usa el reloj del caucho para el aluminio.")
    x0, ww = x + 22, w - 44
    cols = (("PLACA", 260), ("RADIO A 1 s", 280), ("RAPIDEZ = RADIO ÷ TIEMPO", ww - 540))
    px = x0
    for t, cw in cols:
        caja(b, px, yy, cw, 44, c, r=0, fill=A["bg"])
        rot(b, px + 16, yy + 28, t, c, size=13)
        px += cw
    for k, (m, r_) in enumerate((("aluminio", "12 cm"), ("plástico", "8 cm"), ("caucho", "3 cm"))):
        ry = yy + 44 + k * 56
        px = x0
        for j, (t, cw) in enumerate(cols):
            caja(b, px, ry, cw, 56, c, r=0)
            if j == 0:
                b.append(T(px + 16, ry + 36, [m], 18, INK, weight="700"))
            elif j == 1:
                b.append(T(px + 16, ry + 36, [r_], 18, INK))
            else:
                b.append(T(px + 16, ry + 36, ["______ cm ÷ ______ s  =  ______ cm/s"], 18, INK))
            px += cw
    yy += 44 + 3 * 56 + 16
    caja(b, x0, yy, ww, 160, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL RELOJ DEL CAUCHO", c, size=14)
    b.append(T(x0 + 20, yy + 76, ["El caucho recorre 3 cm en  t = ______ s ."], 18, INK))
    b.append(T(x0 + 20, yy + 124, ["En ese mismo t, el aluminio recorre  ______ cm/s × ______ s  =  ______ cm ."], 18, INK))
    yy += 176
    return ojo(b, x0, yy, ww, "LA REGLA NO SE COPIA, SE APLICA",
               "repetir los 3 cm del caucho sería pensar que las dos ondas van igual de rápido. ¿Lo dicen tus "
               "rapideces de la tabla?")


Q = {1: dict(n=1, est=2, pag=236, ctx="Láser y doble rendija · la pantalla más cerca",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=1, pag=237, ctx="Onda de una cuerda delgada a una gruesa · qué cambia",
             comp="Uso comprensivo del conocimiento científico", inst=i2),
     3: dict(n=3, est=1, pag=237, ctx="Láser rojo que entra al agua · qué trayectoria",
             comp="Uso comprensivo del conocimiento científico", inst=i3),
     4: dict(n=4, est=4, pag=238, ctx="Wi-Fi en tres puntos · por qué baja la descarga en C",
             comp="Indagación", inst=i4),
     5: dict(n=5, est=4, pag=238, ctx="Wi-Fi en A y en C · qué indican 33 dB de diferencia",
             comp="Uso comprensivo del conocimiento científico", inst=i5),
     6: dict(n=6, est=3, pag=238, ctx="Los vasos de Jurassic Park · qué conclusión permite la observación",
             comp="Indagación", inst=i6),
     7: dict(n=7, est=3, pag=238, ctx="Vasos alineados a distintas distancias · qué controlar",
             comp="Indagación", inst=i7),
     8: dict(n=8, est=2, pag=239, ctx="Ondas en aluminio, plástico y caucho · qué figura",
             comp="Explicación de fenómenos", inst=i8),
     9: dict(n=9, est=1, pag=239, ctx="Ondas en la placa de caucho · por qué van más lento",
             comp="Explicación de fenómenos", inst=i9),
     10: dict(n=10, est=4, pag=239, ctx="Radios a un segundo · cuánto recorre la onda en el aluminio",
              comp="Uso comprensivo del conocimiento científico", inst=i10)}


def build(pages=(247, 248, 250, 251, 252)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"fis4_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
