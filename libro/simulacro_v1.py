#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hojas de SIMULACRO del cuaderno (PROPUESTA para Nelson, 10 nov; no está integrada al cuaderno).

Se usan en la clase 7 (el estudiante presenta el simulacro del área) y en la clase 8 (devolución):
el estudiante socializa en el cuaderno las preguntas que escoge o que le asignan. Cada esquema sirve
para CUALQUIER pregunta del área.

Formato (Nelson, 10 nov): 3 esquemas por página, 1 pregunta por esquema, hojas a doble cara.
Matemáticas, Lectura Crítica y Sociales: 5 hojas (10 páginas, 30 preguntas); Biología, Química,
Física e Inglés: 3 hojas (6 páginas, 18 preguntas). Ver HOJAS.

    hoja(clave, p, ruta, n_hojas=None)   dibuja la página p (1 … 2·n_hojas) del simulacro de un área
    python3 simulacro.py          genera libro/sim_muestra_<área>.svg (una por área) y el PDF de muestras

Categorías oficiales: Guía de orientación Saber 11.° 2026-2 (Icfes, 17 mar 2026) y documentos
«Niveles de desempeño» Saber 11.° 2022 (Matemáticas, Lectura Crítica, Ciencias Naturales). Ver el
informe de la propuesta: Sociales no tiene componentes desde 2013 y Lectura Crítica tampoco.
"""
import os
import sys

from lib import *            # noqa: F401,F403  (W, H_PAGE, M, CW, T, rect, line, tw, TJ, chip, face, …)
import taller_base as tb     # solo colores (_mezcla), flotador y la paleta del salvavidas

OUT = os.path.dirname(os.path.realpath(__file__)) + "/"
LN_W = "#DDE2EA"             # renglón para escribir (no es texto)
STEP = 46                    # alto de renglón: se escribe a mano

# ───────── categorías oficiales por área ─────────
CIENCIAS_COMP = ["Uso comprensivo del conocimiento científico", "Explicación de fenómenos", "Indagación"]
CIENCIAS_COMPO = ["biológico", "químico", "físico", "CTS"]
NIVEL_1_4 = ["1", "2", "3", "4"]

AREA = {
    "mate": dict(area="Matemáticas",
                 comp=["Interpretación y representación", "Formulación y ejecución", "Argumentación"],
                 rot_comp="Competencia", rot_compo="Contenido",
                 compo=["Estadística", "Geometría", "Álgebra y cálculo"],
                 nivel=NIVEL_1_4, titulo="Del dato a la comprobación"),
    "lc": dict(area="Lectura Crítica",
               comp=["Identificar y ubicar información local", "Relacionar e interpretar información",
                     "Evaluar y reflexionar sobre forma y contenido"],
               rot_comp="Proceso", rot_compo="Texto",
               compo=["continuo", "discontinuo", "·", "literario", "informativo filosófico",
                      "informativo no filosófico"],
               nivel=NIVEL_1_4, titulo="Del texto a la evidencia"),
    "soc": dict(area="Sociales y Ciudadanas",
                comp=["Pensamiento social", "Interpretación y análisis de perspectivas",
                      "Pensamiento reflexivo y sistémico"],
                rot_comp="Competencia", rot_compo="Dimensiones",
                compo=["política", "económica", "social", "cultural", "ambiental", "histórica",
                       "geográfica"],
                nivel=NIVEL_1_4, titulo="La mesa de las voces"),
    "bio": dict(area="Biología", comp=CIENCIAS_COMP, rot_comp="Competencia", rot_compo="Componente",
                compo=CIENCIAS_COMPO, nivel=NIVEL_1_4, titulo="De lo que veo a lo que concluyo"),
    "qui": dict(area="Química", comp=CIENCIAS_COMP, rot_comp="Competencia", rot_compo="Componente",
                compo=CIENCIAS_COMPO, nivel=NIVEL_1_4, titulo="La sustancia antes y después"),
    "fis": dict(area="Física", comp=CIENCIAS_COMP, rot_comp="Competencia", rot_compo="Componente",
                compo=CIENCIAS_COMPO, nivel=NIVEL_1_4, titulo="Primero dibujo el sistema"),
    "ing": dict(area="Inglés",
                comp=["1 · léxico", "2 · avisos", "3 · conversación", "4 · gramática",
                      "5 · lectura literal", "6 · lectura inferencial", "7 · gramática y léxico"],
                rot_comp="Parte", rot_compo=None, compo=None,
                nivel=["Pre A1", "A1", "A2", "B1"], titulo="La parte, la pista y la palabra"),
}

C = {}   # colores del área en curso


def colores(area):
    c = dict(AREAS)[area]
    C.update(c=c, bg=tb._mezcla(c, 0.93), ln=tb._mezcla(c, 0.78), soft=tb._mezcla(c, 0.88),
             dark=tb._mezcla(c, 0.30, "#000000"))
    return C


# ───────── piezas pequeñas ─────────
def rotulo(b, x, y, txt, c=None, size=15):
    b.append(T(x, y, [txt], size, c or C["c"], weight="700", ls=1.5))
    return tw(txt, size, "700") + 1.5 * len(txt)


def pista(b, x, y, txt, size=15):
    b.append(T(x, y, [txt], size, GRAY, style="italic"))
    return tw(txt, size, style="italic")


def renglones(b, x, y, w, n, step=STEP):
    for i in range(n):
        b.append(line(x, y + i * step, x + w, y + i * step, LN_W, 1.8))
    return y + (n - 1) * step


def caja(b, x, y, w, h, titulo, hint=None, n=None, fill="white", stroke=None, dash=None,
         acento=False, top=None):
    """Recuadro con rótulo y renglones que llenan lo que sobra. Devuelve y de la primera línea."""
    b.append(rect(x, y, w, h, fill, r=14, stroke=stroke or C["ln"], sw=2.2, dash=dash))
    if acento:
        b.append(rect(x, y, 8, h, C["c"], r=4))
    xi = x + (26 if acento else 18)
    wt = rotulo(b, xi, y + 28, titulo)
    assert xi + wt <= x + w - 10, f"rótulo se sale: {titulo}"
    yy = y + 28
    if hint:
        svg, yy = TJ(xi, y + 36, hint, w - (xi - x) - 18, 15, GRAY, style="italic", lh=20)
        b.append(svg)
        yy -= 4
    y1 = (top if top is not None else yy + STEP - 4)
    if n is None:
        n = int((y + h - 14 - y1) // STEP) + 1
    if n > 0:
        renglones(b, xi, y1, x + w - xi - 18, n)
    return y1


def check(b, x, y, txt, size=17, c=None):
    """Casilla + texto; devuelve el ancho ocupado."""
    b.append(rect(x, y - 17, 22, 22, "white", r=4, stroke=c or C["c"], sw=2.2))
    b.append(T(x + 32, y, [txt], size, INK))
    return 32 + tw(txt, size)


def circulo_op(b, cx, cy, txt, r=19, size=17):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{C["c"]}" stroke-width="2.4"/>')
    b.append(T(cx, cy + size * 0.35, [txt], size, C["c"], weight="700", anchor="middle"))


def flecha(b, x1, y1, x2, y2, sw=3):
    b.append(hand_arrow(x1, y1, x2, y2, C["c"], sw=sw, bend=0.0, head=16, op=0.8))


# ───────── cabecera de la página: diario + membrete del simulacro ─────────
def cabecera(b, a, p, n_hojas):
    """p = página dentro del simulacro del área (1 … 2·n_hojas); cada hoja tiene dos caras."""
    c = C["c"]
    b.append(rect(0, 0, W, 180, C["bg"], r=0))
    b.append(rect(0, 180, W, 6, c, r=0))
    b.append(logo(M, 44, 64))
    b.append(T(M + 230, 78, [f"{a['area'].upper()} · SIMULACRO"], 24, c, weight="700", ls=3))
    b.append(T(M + 230, 116, ["Clase 7: lo presento · Clase 8: socializo las preguntas que escojo "
                              "o que me asignan"], 22, GRAY))
    hoja_, cara = (p + 1) // 2, 2 - p % 2
    b.append(T(M + 230, 150, [f"Simulacro · hoja {hoja_} de {n_hojas} · cara {cara} de 2 · "
                              f"preguntas {3 * p - 2} a {3 * p} de {6 * n_hojas}"], 20, GRAY,
               style="italic"))
    b.append(T(W - M - 640, 78, ["Sábado ____ de ____________"], 24, INK))
    b.append(T(W - M - 640, 130, ["Llego:"], 22, GRAY))
    for i, mood in enumerate(["worried", "calm", "happy"]):
        b.append(face(W - M - 540 + i * 70, 122, 24, mood, GRAY, "white", sw=2.2))
    b.append(T(W - M - 300, 130, ["Salgo:"], 22, GRAY))
    for i, mood in enumerate(["worried", "calm", "happy"]):
        b.append(face(W - M - 200 + i * 70, 122, 24, mood, GRAY, "white", sw=2.2))
    # membrete del estudiante: nombre, cuál simulacro, sesión
    y = 206
    b.append(rect(M, y, CW, 78, "white", r=18, stroke=C["ln"], sw=2.2))
    b.append(rect(M, y, 8, 78, c, r=4))
    campos = [("Me llamo", 640), ("Simulacro", 470), ("Sesión", 230)]
    x = M + 34
    for txt, wl in campos:
        b.append(T(x, y + 50, [txt], 21, c, weight="700"))
        x += tw(txt, 21, "700") + 14
        b.append(line(x, y + 54, x + wl, y + 54, LN_W, 1.8))
        x += wl + 44
    b.append(T(W - M - 24, y + 50, ["¿cuál? · n.º o fecha"], 15, GRAY, style="italic", anchor="end"))
    return y + 78


# ───────── membrete de cada esquema ─────────
def opciones_fila(b, x, y, ops, x_max, size=17, gap=30):
    """Fila de casillas; «·» es un separador. Si no cabe, baja el tamaño."""
    while True:
        ancho = sum((tw(o, size) + 32 if o != "·" else 20) for o in ops) + gap * (len(ops) - 1)
        if x + ancho <= x_max or size <= 14:
            break
        size -= 0.5
    assert x + ancho <= x_max, f"no caben las opciones: {ops}"
    for o in ops:
        if o == "·":
            b.append(f'<circle cx="{x + 6}" cy="{y - 6}" r="4" fill="{C["ln"]}"/>')
            x += 20 + gap
        else:
            x += check(b, x, y, o, size) + gap
    return x


def membrete_esquema(b, a, y):
    """4 filas: pregunta n.º y nivel · competencia · componente · estrategia. Devuelve y final."""
    c = C["c"]
    x0 = M + 30
    filas = [a["rot_comp"]] + ([a["rot_compo"]] if a["rot_compo"] else []) + ["Estrategia"]
    lw = max(tw(f, 17, "700") for f in filas) + 28            # todas las filas, mismo ancho de rótulo
    x_max = W - M - 30
    # fila 1: n.º · la escogí / me la asignaron · marqué / era · nivel
    yy = y + 44
    b.append(f'<circle cx="{x0 + 22}" cy="{yy - 8}" r="24" fill="{c}"/>')
    b.append(T(x0 + 22, yy - 1, ["n.º"], 17, "white", weight="700", anchor="middle"))
    b.append(line(x0 + 56, yy + 4, x0 + 156, yy + 4, C["ln"], 2.2))
    x = x0 + 186
    x += check(b, x, yy, "la escogí yo") + 26
    x += check(b, x, yy, "me la asignaron") + 44
    b.append(T(x, yy, ["Marqué"], 17, GRAY)); x += tw("Marqué", 17) + 10
    b.append(rect(x, yy - 26, 44, 36, "white", r=8, stroke=C["ln"], sw=2)); x += 60
    b.append(T(x, yy, ["era"], 17, GRAY)); x += tw("era", 17) + 10
    b.append(rect(x, yy - 26, 44, 36, "white", r=8, stroke=C["ln"], sw=2)); x += 44
    # nivel, a la derecha
    niv = a["nivel"]
    rr = 19 if max(len(n) for n in niv) <= 2 else 0
    if rr:
        xr = x_max - 22 - (len(niv) - 1) * 50
        for i, n in enumerate(niv):
            circulo_op(b, xr + i * 50, yy - 7, n)
        xl = xr - 22
    else:      # Inglés: Pre A1 · A1 · A2 · B1 en pastillas medidas
        ws = [tw(n, 17, "700") + 28 for n in niv]
        xr = x_max - sum(ws) - 10 * (len(niv) - 1)
        xl = xr
        for n, wn in zip(niv, ws):
            b.append(rect(xr, yy - 25, wn, 36, "white", r=18, stroke=c, sw=2.2))
            b.append(T(xr + wn / 2, yy - 1, [n], 17, c, weight="700", anchor="middle"))
            xr += wn + 10
    rot = "Nivel que me exige"
    b.append(T(xl - 16, yy, [rot], 17, c, weight="700", anchor="end"))
    assert xl - 16 - tw(rot, 17, "700") > x + 20, "la fila 1 se monta"
    # fila 2 y 3
    yy += 46
    b.append(T(x0, yy, [a["rot_comp"]], 17, c, weight="700"))
    opciones_fila(b, x0 + lw, yy, a["comp"], x_max, gap=26 if len(a["comp"]) > 4 else 34)
    if a["rot_compo"]:
        yy += 44
        b.append(T(x0, yy, [a["rot_compo"]], 17, c, weight="700"))
        opciones_fila(b, x0 + lw, yy, a["compo"], x_max)
    # fila 4: estrategia = la misión (chip para encerrar) + la que usé, escrita
    yy += 48
    b.append(T(x0, yy, ["Estrategia"], 17, c, weight="700"))
    x = x0 + lw
    b.append(T(x, yy, ["de la misión"], 16, GRAY, style="italic"))
    x += tw("de la misión", 16, style="italic") + 14
    for m in range(1, 7):
        x += chip(b, x, yy - 27, f"M{m}", c, size=17, pad=14, fill="white", txtc=c, h=36) + 10
    x += 18
    t = "la que usé:"
    b.append(T(x, yy, [t], 17, GRAY))
    x += tw(t, 17) + 12
    b.append(line(x, yy + 4, x_max, yy + 4, LN_W, 1.8))
    return yy + 26


# ───────── columna derecha común: salvavidas (dónde me perdí) + lo que me llevo ─────────
def columna_cierre(b, x, y, w, h):
    sh = 236
    b.append(rect(x, y, w, sh, tb.SALV_BG, r=16, stroke=tb.SALV, sw=2.2))
    b.append(rect(x, y, 8, sh, tb.SALV, r=4))
    b.append(tb.flotador(x + 46, y + 34, r=16, sw=9))
    b.append(T(x + 76, y + 41, ["SALVAVIDAS"], 15, tb.SALV_D, weight="700", ls=2))
    b.append(T(x + 24, y + 86, ["Me perdí en:"], 17, tb.SALV_TX))
    b.append(line(x + 24 + tw("Me perdí en:", 17) + 12, y + 90, x + w - 20, y + 90, tb.SALV_LN, 1.8))
    b.append(line(x + 24, y + 136, x + w - 20, y + 136, tb.SALV_LN, 1.8))
    b.append(T(x + 24, y + 180, ["La pista que no vi:"], 17, tb.SALV_TX))
    b.append(line(x + 24 + tw("La pista que no vi:", 17) + 12, y + 184, x + w - 20, y + 184,
                  tb.SALV_LN, 1.8))
    b.append(line(x + 24, y + 222, x + w - 20, y + 222, tb.SALV_LN, 1.8))
    ly = y + sh + 36
    b.append(T(x, ly, ["Lo que me llevo de esta pregunta"], 19, C["c"], weight="700"))
    b.append(T(x, ly + 24, ["(una frase que me sirva en el examen de verdad)"], 15, GRAY, style="italic"))
    n = int((y + h - (ly + 70)) // STEP) + 1
    renglones(b, x, ly + 70, w, n)


# ═════════ los siete esquemas ═════════
def esq_mate(b, x, y, w, h):
    """Datos y lo que piden → el camino (cuadrícula numerada) → la comprobación."""
    c = C["c"]
    w1, w3, g = 360, 300, 36
    w2 = w - w1 - w3 - 2 * g
    hd = 196
    caja(b, x, y, w1, hd, "LOS DATOS QUE SÍ USO", "los copio con su unidad")
    caja(b, x, y + hd + 18, w1, h - hd - 18, "LO QUE ME PIDEN", "en mis palabras y en qué unidad")
    x2 = x + w1 + g
    b.append(grid_box(x2, y, w2, h, c=C["soft"], step=26))
    b.append(rect(x2, y, w2, 44, "white", r=10, op=0.94))
    rotulo(b, x2 + 18, y + 30, "EL CAMINO · MIS CUENTAS EN ORDEN")
    for i, yy in enumerate((y + 92, y + 92 + (h - 120) / 3, y + 92 + 2 * (h - 120) / 3)):
        b.append(f'<circle cx="{x2 + 30}" cy="{yy:.0f}" r="15" fill="white" stroke="{c}" stroke-width="2.2"/>')
        b.append(T(x2 + 30, yy + 6, [str(i + 1)], 16, c, weight="700", anchor="middle"))
    flecha(b, x + w1 + 4, y + hd / 2, x2 - 6, y + hd / 2)
    flecha(b, x + w1 + 4, y + hd + 18 + (h - hd - 18) / 2, x2 - 6, y + hd + 18 + (h - hd - 18) / 2)
    x3 = x2 + w2 + g
    flecha(b, x2 + w2 + 4, y + h / 2, x3 - 6, y + h / 2)
    b.append(rect(x3, y, w3, h, C["bg"], r=14, stroke=C["ln"], sw=2.2))
    rotulo(b, x3 + 18, y + 30, "LA COMPROBACIÓN")
    yy = y + 76
    for t in ("lo reemplacé en el enunciado", "la unidad cuadra", "el tamaño es creíble"):
        check(b, x3 + 18, yy, t, size=16)
        yy += 44
    svg, yy = TJ(x3 + 18, yy - 10, "Si algo no cuadra, vuelvo al paso", w3 - 36, 16, INK, lh=22)
    b.append(svg)
    b.append(T(x3 + 18, yy + 22, ["número"], 16, INK))
    b.append(line(x3 + 18 + tw("número", 16) + 10, yy + 26, x3 + 150, yy + 26, C["ln"], 2))
    b.append(T(x3 + 18, y + h - 20, ["y la respuesta tiene sentido."], 15, GRAY, style="italic"))


def esq_lc(b, x, y, w, h):
    """Qué dice → qué me pregunta → la evidencia (cita) → tacho con razón."""
    c = C["c"]
    g = 26
    wa = (w - g) / 2
    h3 = 64                                   # tacho con razón, abajo
    h2 = 112                                  # la cita
    h1 = h - h2 - h3 - 2 * 18
    caja(b, x, y, wa, h1, "QUÉ DICE EL TEXTO", "en una frase mía, sin copiar")
    caja(b, x + wa + g, y, wa, h1, "QUÉ ME PREGUNTA DE VERDAD",
         "¿lo que dice?, ¿cómo se arma?, ¿qué tan válido es?")
    # la cita
    y2 = y + h1 + 18
    b.append(rect(x, y2, w, h2, C["bg"], r=14))
    b.append(rect(x, y2, 8, h2, c, r=4))
    b.append(T(x + 30, y2 + 82, ["“"], 96, c, weight="700", op=0.55))
    rotulo(b, x + 84, y2 + 30, "LA EVIDENCIA · COPIO LAS PALABRAS EXACTAS")
    b.append(T(x + w - 20, y2 + 30, ["línea o párrafo n.º ______"], 15, GRAY, style="italic",
               anchor="end"))
    renglones(b, x + 84, y2 + 82, w - 104, 1)
    # tacho con razón: las cuatro en una fila
    y3 = y2 + h2 + 18
    rotulo(b, x, y3 + 16, "TACHO CON RAZÓN")
    pista(b, x + 170, y3 + 16, "la que sobrevive es la que la evidencia sostiene")
    wq = (w - 3 * 20) / 4
    for i, L in enumerate("ABCD"):
        cx = x + i * (wq + 20)
        cy = y3 + h3 - 12
        circulo_op(b, cx + 18, cy - 6, L, r=17, size=16)
        b.append(T(cx + 44, cy, ["no, porque"], 16, GRAY))
        b.append(line(cx + 44 + tw("no, porque", 16) + 8, cy + 4, cx + wq, cy + 4, LN_W, 1.8))


def esq_soc(b, x, y, w, h):
    """La situación en el centro; tres voces alrededor (quién, qué busca); desde dónde pregunta."""
    c = C["c"]
    wm = 800
    cx, cy = x + wm / 2, y + h / 2
    vw, vh = 250, 128
    voces = [(x, y, "VOZ 1"), (x + wm - vw, y, "VOZ 2"), (x, y + h - vh, "VOZ 3")]
    for vx, vy, tt in voces:      # los hilos van debajo de todo
        b.append(f'<line x1="{vx + vw / 2}" y1="{vy + vh / 2}" x2="{cx}" y2="{cy}" stroke="{C["ln"]}" '
                 f'stroke-width="2.4" stroke-dasharray="7,7"/>')
    for vx, vy, tt in voces:
        b.append(rect(vx, vy, vw, vh, "white", r=36, stroke=c, sw=2.2))
        rotulo(b, vx + 24, vy + 28, tt)
        b.append(T(vx + 24, vy + 70, ["quién:"], 16, GRAY))
        b.append(line(vx + 24 + tw("quién:", 16) + 8, vy + 74, vx + vw - 22, vy + 74, LN_W, 1.8))
        b.append(T(vx + 24, vy + 112, ["qué busca:"], 16, GRAY))
        b.append(line(vx + 24 + tw("qué busca:", 16) + 8, vy + 116, vx + vw - 22, vy + 116, LN_W, 1.8))
    # la situación, en el centro y encima de los hilos
    rx_, ry_ = 140, 78
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx_}" ry="{ry_}" fill="{C["bg"]}" stroke="{c}" '
             f'stroke-width="2.4"/>')
    b.append(T(cx, cy - 36, ["LA SITUACIÓN"], 15, c, weight="700", anchor="middle", ls=1.5))
    renglones(b, cx - 104, cy + 6, 208, 2, step=44)
    # cuarta esquina: ¿quién gana y quién paga?
    gx, gy = x + wm - vw, y + h - vh
    b.append(rect(gx, gy, vw, vh, C["bg"], r=14))
    rotulo(b, gx + 18, gy + 30, "EN QUÉ CHOCAN")
    renglones(b, gx + 18, gy + 76, vw - 36, 2, step=44)
    # derecha: la perspectiva que pide la pregunta
    xp = x + wm + 34
    wp = w - wm - 34
    hp = (h - 18) / 2
    caja(b, xp, y, wp, hp, "DESDE DÓNDE PREGUNTA", "¿desde qué voz, principio o derecho se mira?",
         acento=True)
    caja(b, xp, y + hp + 18, wp, hp, "LO QUE SE PONE EN TENSIÓN", "un derecho, un interés, una norma",
         acento=True)


def esq_bio(b, x, y, w, h):
    """¿En qué escala pasa? → lo que cambia → lo que muestran los datos → lo que sí puedo concluir."""
    c = C["c"]
    rotulo(b, x, y + 22, "¿EN QUÉ ESCALA PASA?")
    escalas = ["molécula", "célula", "organismo", "población", "ecosistema"]
    xs = x + 230
    for i, e in enumerate(escalas):
        wch = tw(e, 17) + 34
        b.append(rect(xs, y, wch, 36, "white", r=18, stroke=C["ln"], sw=2))
        b.append(T(xs + wch / 2, y + 24, [e], 17, INK, anchor="middle"))
        if i < len(escalas) - 1:
            b.append(T(xs + wch + 11, y + 25, ["›"], 22, C["c"], weight="700", anchor="middle"))
        xs += wch + 22
    pista(b, xs + 6, y + 24, "encierro una")
    y1 = y + 60
    hh = h - 60
    g = 40
    wc = (w - 2 * g) / 3
    tit = [("LO QUE CAMBIA", "la variable: qué se movió o qué se comparó"),
           ("LO QUE MUESTRAN LOS DATOS", "comparo contra el que no cambió (el control)"),
           ("LO QUE SÍ PUEDO CONCLUIR", "solo lo que los datos alcanzan a decir")]
    for i, (t, hnt) in enumerate(tit):
        xi = x + i * (wc + g)
        hi = hh if i < 2 else hh - 112
        caja(b, xi, y1, wc, hi, t, hnt, fill="white" if i != 1 else C["bg"],
             n=2 if i == 1 else None)
        if i < 2:
            flecha(b, xi + wc + 4, y1 + hh / 2, xi + wc + g - 6, y1 + hh / 2)
    # en la caja de los datos: unos ejes para dibujar la gráfica o la tabla en pequeño
    xd = x + wc + g
    ya = y1 + hh - 150
    b.append(line(xd + 40, ya, xd + 40, y1 + hh - 30, c, 2.2))
    b.append(line(xd + 40, y1 + hh - 30, xd + wc - 24, y1 + hh - 30, c, 2.2))
    b.append(T(xd + 50, ya + 4, ["si hay gráfica, la dibujo en pequeño"], 15, GRAY, style="italic"))
    xi = x + 2 * (wc + g)
    yb = y1 + hh - 96
    b.append(rect(xi, yb, wc, 96, "white", r=14, stroke=C["ln"], sw=2.2, dash="8,6"))
    rotulo(b, xi + 18, yb + 28, "Y LO QUE NO ALCANZA A DECIR")
    renglones(b, xi + 18, yb + 74, wc - 36, 1)


def beaker(x, y, w, h, c, fill):
    """Vaso de laboratorio con boca abierta (trazo absoluto)."""
    return (f'<path d="M {x},{y} L {x},{y + h - 18} Q {x},{y + h} {x + 18},{y + h} L {x + w - 18},{y + h} '
            f'Q {x + w},{y + h} {x + w},{y + h - 18} L {x + w},{y} L {x + w + 14},{y - 12}" '
            f'fill="{fill}" stroke="{c}" stroke-width="2.6" stroke-linejoin="round"/>'
            f'<path d="M {x},{y} L {x - 14},{y - 12}" fill="none" stroke="{c}" stroke-width="2.6"/>')


def esq_qui(b, x, y, w, h):
    """Antes → qué la transforma → después; abajo: lo que se conserva (balanza) y la propiedad que decide."""
    c = C["c"]
    hb = 200
    wb = 420
    for i, (t, hnt) in enumerate((("ANTES", "sustancias, estado, cantidad"),
                                  ("DESPUÉS", "qué quedó, en qué estado"))):
        bx = x + 14 + i * (w - wb - 28)
        b.append(beaker(bx, y + 22, wb, hb - 22, c, "white"))
        rotulo(b, bx + 22, y + 58, t)
        pista(b, bx + 22 + tw(t, 15, "700") + 1.5 * len(t) + 12, y + 58, hnt)
        renglones(b, bx + 22, y + 116, wb - 44, 2)
    # centro: qué la transforma
    mx = x + 14 + wb + 40
    mw = w - 2 * (wb + 14) - 80
    flecha(b, mx, y + 120, mx + mw, y + 120, sw=3.4)
    b.append(T(mx + mw / 2, y + 60, ["QUÉ LA TRANSFORMA"], 15, c, weight="700", anchor="middle", ls=1.5))
    pista_t = "calor · mezcla · reacción · presión"
    b.append(T(mx + mw / 2, y + 86, [pista_t], 15, GRAY, style="italic", anchor="middle"))
    b.append(line(mx + 10, y + 166, mx + mw - 10, y + 166, LN_W, 1.8))
    # abajo
    y2 = y + hb + 26
    h2 = h - hb - 26
    wl = (w - 30) * 0.55
    b.append(rect(x, y2, wl, h2, "white", r=14, stroke=C["ln"], sw=2.2))
    rotulo(b, x + 18, y2 + 28, "LO QUE SE CONSERVA")
    pista(b, x + 214, y2 + 28, "cuento átomos o masa a cada lado")
    # balanza: sobre cada platillo se escribe lo que se cuenta
    bx = x + wl / 2
    by = y2 + 48
    arm, pw = 190, 120
    b.append(line(bx, by, bx, y2 + h2 - 16, C["ln"], 3))
    b.append(line(bx - 60, y2 + h2 - 16, bx + 60, y2 + h2 - 16, C["ln"], 3))
    b.append(line(bx - arm, by, bx + arm, by, c, 3))
    b.append(f'<circle cx="{bx}" cy="{by}" r="6" fill="{c}"/>')
    py = by + 70
    for s_, lab in ((-1, "antes"), (1, "después")):
        px = bx + s_ * arm
        b.append(line(px, by, px, py - 40, C["ln"], 2))          # el gancho no cruza el renglón
        b.append(f'<path d="M {px - pw},{py} L {px + pw},{py} Q {px},{py + 34} {px - pw},{py} Z" '
                 f'fill="{C["bg"]}" stroke="{c}" stroke-width="2.2"/>')
        b.append(line(px - pw + 14, py - 8, px + pw - 14, py - 8, LN_W, 1.8))
        b.append(T(px, py + 42, [lab], 15, GRAY, style="italic", anchor="middle"))
    xr = x + wl + 30
    caja(b, xr, y2, w - wl - 30, h2, "LA PROPIEDAD QUE DECIDE", "densidad, solubilidad, punto de ebullición…",
         acento=True)


def esq_fis(b, x, y, w, h):
    """Dibujo el sistema (puntos) → magnitudes con unidad → la ley que manda → predigo antes de mirar."""
    c = C["c"]
    wd = 560
    b.append(rect(x, y, wd, h, "white", r=14, stroke=C["ln"], sw=2.2))
    for gx in range(int(x + 26), int(x + wd - 10), 28):
        for gy in range(int(y + 64), int(y + h - 10), 28):
            b.append(f'<circle cx="{gx}" cy="{gy}" r="1.8" fill="{C["ln"]}"/>')
    b.append(rect(x + 2, y + 2, wd - 4, 50, "white", r=12))
    rotulo(b, x + 18, y + 30, "DIBUJO EL SISTEMA")
    pista(b, x + 214, y + 30, "objetos, fuerzas o flujos, con flecha")
    xr = x + wd + 30
    wr = w - wd - 30
    # magnitudes
    hm = 150
    b.append(rect(xr, y, wr, hm, C["bg"], r=14))
    rotulo(b, xr + 18, y + 30, "LAS MAGNITUDES")
    pista(b, xr + 186, y + 30, "símbolo = valor y unidad")
    for i in range(2):
        yy = y + 80 + i * STEP
        for j in range(2):
            xx = xr + 18 + j * (wr - 36) / 2
            b.append(line(xx, yy, xx + 60, yy, C["ln"], 2))
            b.append(T(xx + 74, yy - 4, ["="], 20, c, weight="700"))
            b.append(line(xx + 100, yy, xx + (wr - 36) / 2 - 30, yy, C["ln"], 2))
    y2 = y + hm + 18
    hl = 96
    caja(b, xr, y2, wr, hl, "LA LEY O EL PRINCIPIO QUE MANDA", None, acento=True, n=1, top=y2 + 74)
    y3 = y2 + hl + 18
    h3 = h - (y3 - y)
    b.append(rect(xr, y3, wr, h3, "white", r=14, stroke=c, sw=2.2, dash="8,6"))
    rotulo(b, xr + 18, y3 + 30, "PREDIGO ANTES DE MIRAR LAS OPCIONES")
    yy = y3 + 64
    t1 = "Si"
    b.append(T(xr + 18, yy, [t1], 17, INK))
    xx = xr + 18 + tw(t1, 17) + 10
    b.append(line(xx, yy + 4, xx + 170, yy + 4, LN_W, 1.8)); xx += 186
    xx += check(b, xx, yy, "aumenta", 16) + 18
    xx += check(b, xx, yy, "disminuye", 16) + 18
    b.append(T(xx, yy, [","], 17, INK))
    yy += STEP
    t2 = "entonces"
    b.append(T(xr + 18, yy, [t2], 17, INK))
    xx = xr + 18 + tw(t2, 17) + 10
    b.append(line(xx, yy + 4, xr + wr - 18, yy + 4, LN_W, 1.8))


def esq_ing(b, x, y, w, h):
    """La frase (con el hueco) → la pista que manda → la palabra que elegí → las que descarté."""
    c = C["c"]
    h1 = 134
    b.append(rect(x, y, w, h1, C["bg"], r=14))
    b.append(rect(x, y, 8, h1, c, r=4))
    rotulo(b, x + 26, y + 30, "LA FRASE DONDE ESTÁ · LA COPIO Y DEJO EL HUECO")
    pista(b, x + 26, y + 54, "en las partes 2, 5 y 6: la línea del aviso o del texto que responde")
    renglones(b, x + 26, y + 112, w - 52, 1)
    y2 = y + h1 + 30
    h2 = h - h1 - 30 - 84
    g = 44
    # pista (lupa) → palabra → descarte
    wl = 400
    b.append(rect(x, y2, wl, h2, "white", r=14, stroke=C["ln"], sw=2.2))
    lx, ly = x + 40, y2 + 34
    b.append(f'<circle cx="{lx}" cy="{ly}" r="15" fill="white" stroke="{c}" stroke-width="3"/>')
    b.append(line(lx + 11, ly + 11, lx + 22, ly + 22, c, 4))
    rotulo(b, x + 72, y2 + 40, "LA PISTA QUE MANDA")
    svg, yy = TJ(x + 18, y2 + 60, "la palabra de al lado, el tiempo del verbo, el lugar o quién habla",
                 wl - 36, 15, GRAY, style="italic", lh=20)
    b.append(svg)
    renglones(b, x + 18, yy + 40, wl - 36, int((y2 + h2 - 14 - (yy + 40)) // STEP) + 1)
    xm = x + wl + g
    wm = 330
    flecha(b, x + wl + 4, y2 + h2 / 2, xm - 6, y2 + h2 / 2)
    b.append(rect(xm, y2, wm, h2, C["bg"], r=14, stroke=c, sw=2.6))
    rotulo(b, xm + 18, y2 + 30, "LA PALABRA QUE VA")
    b.append(rect(xm + 30, y2 + 62, wm - 60, 64, "white", r=12, stroke=C["ln"], sw=2))
    b.append(T(xm + 18, y2 + 160, ["opción"], 16, GRAY))
    b.append(rect(xm + 18 + tw("opción", 16) + 12, y2 + 134, 44, 36, "white", r=8, stroke=C["ln"], sw=2))
    xd = xm + wm + g
    flecha(b, xm + wm + 4, y2 + h2 / 2, xd - 6, y2 + h2 / 2)
    wd = x + w - xd
    caja(b, xd, y2, wd, h2, "LAS QUE DESCARTÉ Y POR QUÉ", "una razón por cada una, aunque sea corta",
         dash="8,6", stroke=c)
    # palabra nueva
    y3 = y + h - 64
    b.append(rect(x, y3, w, 64, "white", r=14, stroke=C["ln"], sw=2.2))
    rotulo(b, x + 18, y3 + 40, "PALABRA NUEVA")
    xx = x + 180
    for t, wl_ in (("en inglés", 330), ("= en español", 330)):
        b.append(T(xx, y3 + 40, [t], 17, GRAY))
        xx += tw(t, 17) + 12
        b.append(line(xx, y3 + 44, xx + wl_, y3 + 44, LN_W, 1.8))
        xx += wl_ + 30


# Hojas a doble cara por área (Nelson, 10 nov): 5 hojas = 10 páginas = 30 preguntas;
# 3 hojas = 6 páginas = 18 preguntas.
HOJAS = dict(mate=5, lc=5, soc=5, bio=3, qui=3, fis=3, ing=3)

ESQUEMA = dict(mate=esq_mate, lc=esq_lc, soc=esq_soc, bio=esq_bio, qui=esq_qui, fis=esq_fis, ing=esq_ing)


# ───────── un esquema completo y la página ─────────
def esquema(b, clave, a, y, h):
    c = C["c"]
    b.append(rect(M, y, CW, h, "white", r=26, stroke=C["ln"], sw=2.4))
    tmp = []
    y_m = membrete_esquema(tmp, a, y)
    hb = y_m - y + 6              # banda del membrete, debajo de lo que se marca
    b.append(rect(M, y, CW, hb, C["bg"], r=26) + rect(M, y + hb - 30, CW, 30, C["bg"], r=0))
    b.extend(tmp)
    # cuerpo
    yb = y + hb + 26
    hb2 = y + h - 26 - yb
    xe = M + 30
    we = 1270
    b.append(T(xe, yb + 6, [a["titulo"]], 24, c, weight="700"))
    frag = []
    ESQUEMA[clave](frag, xe, yb + 26, we, hb2 - 26)
    caja_ = tb.medir(frag)
    assert caja_[3] <= y + h - 20 and caja_[2] <= xe + we + 2 and caja_[0] >= xe - 2, \
        f"{clave}: el esquema se sale de su tarjeta {caja_} (tarjeta hasta y={y + h - 20:.0f})"
    b.extend(frag)
    b.append(line(xe + we + 22, yb, xe + we + 22, y + h - 30, "#E6EAF0", 2, "6,6"))
    xr = xe + we + 44
    columna_cierre(b, xr, yb - 12, W - M - 30 - xr, hb2 + 12)


def hoja(clave, p, ruta, n_hojas=None):
    """Página p (1 … 2·n_hojas) del simulacro del área. n_hojas: el del área (HOJAS) si no se pasa."""
    a = AREA[clave]
    n_hojas = n_hojas or HOJAS[clave]
    assert 1 <= p <= 2 * n_hojas, f"{clave}: la página {p} no existe (son {2 * n_hojas})"
    colores(a["area"])
    b = svg_open()
    y = cabecera(b, a, p, n_hojas) + 22
    fondo = H_PAGE - 90 - 26 - 24
    g = 22
    h = (fondo - y - 2 * g) / 3
    for i in range(3):
        esquema(b, clave, a, y + i * (h + g), h)
    footer(b, f"S{p}", C["c"], texto=f"{a['area']} · Simulacro · hoja {(p + 1) // 2} de {n_hojas}")
    svg_close(b, ruta)
    return ruta


ORDEN = ["mate", "lc", "soc", "bio", "qui", "fis", "ing"]

if __name__ == "__main__":
    import render
    claves = sys.argv[1:] or ORDEN
    rutas = [hoja(cl, 1, OUT + f"sim_v1_muestra_{cl}.svg") for cl in claves]
    os.makedirs("/tmp/claude-0/simulacro", exist_ok=True)
    pdf = "/tmp/claude-0/simulacro/Simulacro_muestras_v1.pdf"
    render.unir(rutas, pdf)
    print(pdf, render.verifica(pdf, marca="Aprende"))
