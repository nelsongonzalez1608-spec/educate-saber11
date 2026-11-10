#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hojas de SIMULACRO del cuaderno · versión 2 (PROPUESTA para Nelson, 10 nov; no está integrada).

Se usan en la clase 7 (el estudiante presenta el simulacro del área) y en la clase 8 (devolución):
el estudiante socializa en el cuaderno la pregunta que escoge o que le asignan. Cada esquema tiene
que servir para CUALQUIER pregunta del área (Nelson, 10 nov: «estaba un poco cerrado»).

Por qué cambió (ver tablero/propuestas/simulacro_analisis.md): la v1 dibujaba UN tipo de pregunta
por área (Química: reacciones; Sociales: voces en conflicto; Inglés: el hueco de una frase). Con
181 preguntas reales clasificadas, la v1 servía de verdad para 36 (20 %), a medias para 75 y no
servía para 70.

Forma de la v2 · un esquema base del área + su caja de herramientas (camino «a» del análisis):

    membrete (igual)        n.º · nivel · competencia · componente · estrategia
    fila A · ME PIDEN       el estudiante marca QUÉ TIPO de tarea es (4 tipos del área, sacados de
                            las preguntas reales) y la dice en sus palabras (o la escala, el nivel,
                            la predicción o la línea que manda, según el área)
    fila B · tres piezas    izquierda: LO QUE USO (datos, evidencia, situación, sustancias…)
                            centro: el espacio libre para razonar + la CAJA DE HERRAMIENTAS del
                            área (4 mini-formatos con su dibujito; el estudiante marca el que usó)
                            derecha: la pieza que cierra el razonamiento del área (comprobación,
                            trampas, idea clave, conclusión, ley, pista)
    fila C · TACHO          una razón por cada opción descartada
    columna derecha (igual) salvavidas + lo que me llevo

Formato (Nelson, 10 nov): 3 esquemas por página, 1 pregunta por esquema, hojas a doble cara.
Matemáticas, Lectura Crítica y Sociales: 5 hojas (10 páginas, 30 preguntas); Biología, Química,
Física e Inglés: 3 hojas (6 páginas, 18 preguntas). Ver HOJAS.

    hoja(clave, p, ruta, n_hojas=None)   dibuja la página p (1 … 2·n_hojas) del simulacro de un área
    python3 simulacro.py          genera libro/sim_muestra_<área>.svg (una por área) y el PDF de muestras

La versión 1 está en simulacro_v1.py (sus muestras: sim_v1_muestra_<área>.svg).

Categorías oficiales: Guía de orientación Saber 11.° 2026-2 (Icfes, 17 mar 2026) y documentos
«Niveles de desempeño» Saber 11.° 2022 (Matemáticas, Lectura Crítica, Ciencias Naturales).
"""
import os
import sys

from lib import *            # noqa: F401,F403  (W, H_PAGE, M, CW, T, rect, line, tw, TJ, chip, face, …)
import taller_base as tb     # colores (_mezcla), flotador, paleta del salvavidas y la cabecera
import bitacora as BT        # estilo B · Bitácora (10 nov): el entorno; los esquemas no cambian

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
                nivel=NIVEL_1_4, titulo="La situación y sus lentes"),
    "bio": dict(area="Biología", comp=CIENCIAS_COMP, rot_comp="Competencia", rot_compo="Componente",
                compo=CIENCIAS_COMPO, nivel=NIVEL_1_4, titulo="De lo que veo a lo que concluyo"),
    "qui": dict(area="Química", comp=CIENCIAS_COMP, rot_comp="Competencia", rot_compo="Componente",
                compo=CIENCIAS_COMPO, nivel=NIVEL_1_4, titulo="Lo que veo, las partículas y el número"),
    "fis": dict(area="Física", comp=CIENCIAS_COMP, rot_comp="Competencia", rot_compo="Componente",
                compo=CIENCIAS_COMPO, nivel=NIVEL_1_4, titulo="Primero dibujo el sistema"),
    "ing": dict(area="Inglés",
                comp=["1 · léxico", "2 · avisos", "3 · conversación", "4 · gramática",
                      "5 · lectura literal", "6 · lectura inferencial", "7 · gramática y léxico"],
                rot_comp="Parte", rot_compo=None, compo=None,
                nivel=["Pre A1", "A1", "A2", "B1"], titulo="La parte, la pista y la respuesta"),
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
    """p = página dentro del simulacro del área (1 … 2·n_hojas); cada hoja tiene dos caras.
    Bitácora: la misma cabecera de las hojas de misión (sin banda ni barra) y el recuadro a mano
    del estudiante."""
    c = C["c"]
    BT.fondo_puntos(b)
    b.append(rect(M - 10, 30, logo_w(62) + 20, 82, "white", r=4))
    b.append(logo(M, 40, 62))
    x0 = M + 200
    t = a["area"]
    s = 50
    while BT.twf(t, s, BT.SHA, "800") > 1240 - x0 - 220 and s > 30:
        s -= 0.5
    wt = BT.twf(t, s, BT.SHA, "800")
    b.append(BT.resaltador(x0, 92 - s * 0.8, wt, s * 0.8, BT.FOSFO, seed=2))
    b.append(BT.TX(x0, 88, t, s, BT.TINTA_B, BT.SHA, "800"))
    b.append(BT.TX(x0 + wt + 22, 86, "/ SIMULACRO", 24, c, BT.MONO, "700"))
    sub = "Clase 7: lo presento · Clase 8: socializo las preguntas que escojo o que me asignan"
    b.append(rect(x0 - 6, 104, tw(sub, 21) + 12, 30, "white", r=2))
    b.append(T(x0, 126, [sub], 21, GRAY))
    hoja_, cara = (p + 1) // 2, 2 - p % 2
    l3 = (f"Simulacro · hoja {hoja_} de {n_hojas} · cara {cara} de 2 · "
          f"preguntas {3 * p - 2} a {3 * p} de {6 * n_hojas}").upper()
    b.append(rect(x0 - 6, 140, BT.twf(l3, 15, BT.MONO) + 12, 26, "white", r=2))
    b.append(BT.TX(x0, 159, l3, 15, GRAY, BT.MONO))
    nx, ny, nw, nh = 1300, 24, W - M - 1300, 152
    b.append(BT.wob_rect(nx, ny, nw, nh, BT.TINTA_B, 2.6, fill="white", seed=41))
    b.append(T(nx + 28, ny + 52, ["Sábado ____ de ____________"], 24, INK))
    b.append(BT.TX(nx + 28, ny + 116, "LLEGO", 15, GRAY, BT.MONO, "700"))
    b.append(BT.TX(nx + 328, ny + 116, "SALGO", 15, GRAY, BT.MONO, "700"))
    for base in (nx + 120, nx + 420):
        for i, mood in enumerate(["worried", "calm", "happy"]):
            b.append(face(base + i * 62, ny + 108, 22, mood, BT.TINTA_B, "white", sw=2.2))
    b.append(BT.estrellita(nx - 34, ny + 30, 13, c))
    # membrete del estudiante: nombre, cuál simulacro, sesión
    y = 206
    b.append(BT.wob_rect(M, y, CW, 78, BT.TINTA_B, 2.6, fill="white", seed=43))
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
    b.append(BT.TX(x, ly, "Lo que me llevo de esta pregunta", 21, C["c"], BT.SHA, "700"))
    b.append(BT.estrellita(x + BT.twf("Lo que me llevo de esta pregunta", 21, BT.SHA, "700") + 20, ly - 7,
                           9, EDU_ORO, 2.2))
    b.append(T(x, ly + 24, ["(una frase que me sirva en el examen de verdad)"], 15, GRAY, style="italic"))
    n = int((y + h - (ly + 70)) // STEP) + 1
    renglones(b, x, ly + 70, w, n)



# ═════════ versión 2: un esquema base por área + su caja de herramientas ═════════
LN_C = "#C9CED6"             # contorno de los dibujitos de la caja de herramientas (no es texto)


def _p(*pts, c=None, sw=2.2, fill="none", close=False):
    """Trazo absoluto (verifica_cajas no mide trazos relativos)."""
    d = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + (" Z" if close else "")
    return f'<path d="{d}" fill="{fill}" stroke="{c or C["c"]}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"/>'


def _circ(cx, cy, r, c=None, fill="white", sw=2.2):
    return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{fill}" stroke="{c or C["c"]}" stroke-width="{sw}"/>'


def _flechita(x1, y, x2, c=None, sw=2.2):
    c = c or C["c"]
    return _p((x1, y), (x2, y), c=c, sw=sw) + _p((x2 - 6, y - 5), (x2, y), (x2 - 6, y + 5), c=c, sw=sw)


def beaker(x, y, w, h, c, fill):
    """Vaso de laboratorio con boca abierta (trazo absoluto)."""
    return (f'<path d="M {x},{y} L {x},{y + h - 18} Q {x},{y + h} {x + 18},{y + h} L {x + w - 18},{y + h} '
            f'Q {x + w},{y + h} {x + w},{y + h - 18} L {x + w},{y} L {x + w + 14},{y - 12}" '
            f'fill="{fill}" stroke="{c}" stroke-width="2.6" stroke-linejoin="round"/>'
            f'<path d="M {x},{y} L {x - 14},{y - 12}" fill="none" stroke="{c}" stroke-width="2.6"/>')


# ───────── los dibujitos de la caja de herramientas (caja de 34 × 34, esquina x, y) ─────────
def ic_cuentas(x, y):
    s = T(x + 2, y + 12, ["1"], 12, C["c"], weight="700") + T(x + 2, y + 32, ["2"], 12, C["c"], weight="700")
    return s + _p((x + 12, y + 8), (x + 34, y + 8), c=LN_C) + _p((x + 12, y + 28), (x + 30, y + 28), c=LN_C) \
        + T(x + 22, y + 21, ["="], 13, C["c"], weight="700", anchor="middle")


def ic_figura(x, y):
    return _p((x + 2, y + 32), (x + 32, y + 32), (x + 2, y + 4), close=True) \
        + _p((x + 2, y + 25), (x + 9, y + 25), (x + 9, y + 32), sw=1.6)


def ic_tabla(x, y):
    s = rect(x + 1, y + 3, 32, 28, "white", r=3, stroke=C["c"], sw=2)
    return s + _p((x + 12, y + 3), (x + 12, y + 31), sw=1.6) + _p((x + 1, y + 13), (x + 33, y + 13), sw=1.6) \
        + _p((x + 1, y + 22), (x + 33, y + 22), sw=1.6)


def ic_pruebo(x, y):
    return T(x + 17, y + 22, ["x=2"], 13, C["c"], weight="700", anchor="middle") \
        + _p((x + 5, y + 29), (x + 11, y + 33), (x + 29, y + 26), sw=2)


def ic_subrayo(x, y):
    s = rect(x + 1, y + 13, 33, 9, C["soft"], r=2)
    for yy in (8, 17, 27):
        s += _p((x + 3, y + yy), (x + 32, y + yy), c=LN_C if yy != 17 else C["c"], sw=2)
    return s


def ic_mapa(x, y):
    s = ""
    for i in range(3):
        s += rect(x + 6, y + 1 + i * 12, 22, 8, "white", r=2, stroke=C["c"], sw=1.8)
    return s + _p((x + 17, y + 9), (x + 17, y + 13), sw=1.6) + _p((x + 17, y + 21), (x + 17, y + 25), sw=1.6)


def ic_tesis(x, y):
    return rect(x + 8, y + 1, 18, 10, C["soft"], r=2, stroke=C["c"], sw=1.8) \
        + _p((x + 17, y + 11), (x + 6, y + 23), sw=1.8) + _p((x + 17, y + 11), (x + 28, y + 23), sw=1.8) \
        + rect(x + 1, y + 23, 12, 10, "white", r=2, stroke=C["c"], sw=1.8) \
        + rect(x + 21, y + 23, 12, 10, "white", r=2, stroke=C["c"], sw=1.8)


def ic_imagen(x, y):
    return rect(x + 1, y + 3, 32, 28, "white", r=3, stroke=C["c"], sw=2) \
        + _p((x + 17, y + 3), (x + 17, y + 31), sw=1.4) + _p((x + 1, y + 17), (x + 33, y + 17), sw=1.4) \
        + _circ(x + 9, y + 10, 3, fill=C["c"], sw=1)


def ic_voces(x, y):
    s = _p((x + 17, y + 17), (x + 6, y + 6), c=LN_C, sw=1.6) + _p((x + 17, y + 17), (x + 28, y + 6), c=LN_C, sw=1.6) \
        + _p((x + 17, y + 17), (x + 17, y + 31), c=LN_C, sw=1.6)
    return s + _circ(x + 6, y + 6, 5) + _circ(x + 28, y + 6, 5) + _circ(x + 17, y + 30, 5) \
        + _circ(x + 17, y + 17, 6, fill=C["soft"])


def ic_rueda(x, y):
    import math
    s = _circ(x + 17, y + 17, 15)
    for k in range(6):
        a = k * math.pi / 3
        s += _p((x + 17, y + 17), (x + 17 + 15 * math.cos(a), y + 17 + 15 * math.sin(a)), sw=1.4)
    return s


def ic_tiempo(x, y):
    s = _p((x + 1, y + 20), (x + 33, y + 20), sw=2)
    for xx in (5, 15, 27):
        s += _p((x + xx, y + 14), (x + xx, y + 26), sw=1.8)
    return s + _circ(x + 15, y + 20, 3.5, fill=C["c"], sw=1)


def ic_causa(x, y):
    return rect(x + 1, y + 11, 11, 12, "white", r=2, stroke=C["c"], sw=1.8) \
        + _flechita(x + 13, y + 17, x + 22) + rect(x + 23, y + 11, 11, 12, C["soft"], r=2, stroke=C["c"], sw=1.8)


def ic_cadena(x, y):
    return _circ(x + 5, y + 17, 4.5) + _flechita(x + 10, y + 17, x + 14, sw=1.6) + _circ(x + 19, y + 17, 4.5) \
        + _flechita(x + 24, y + 17, x + 27, sw=1.6) + _circ(x + 31, y + 17, 3.5, fill=C["c"], sw=1)


def ic_ejes(x, y):
    return _p((x + 3, y + 1), (x + 3, y + 31), (x + 33, y + 31), sw=2) \
        + f'<path d="M {x + 5},{y + 27} Q {x + 14},{y + 4} {x + 31},{y + 9}" fill="none" ' \
          f'stroke="{C["c"]}" stroke-width="2"/>'


def ic_control(x, y):
    s = ""
    for i, f in enumerate(("white", C["soft"])):
        xx = x + 5 + i * 15
        s += _p((xx, y + 2), (xx, y + 27), (xx + 5, y + 32), (xx + 10, y + 27), (xx + 10, y + 2), sw=1.8,
                fill=f)
    return s


def ic_punnett(x, y):
    return rect(x + 7, y + 7, 26, 26, "white", r=2, stroke=C["c"], sw=1.8) \
        + _p((x + 20, y + 7), (x + 20, y + 33), sw=1.4) + _p((x + 7, y + 20), (x + 33, y + 20), sw=1.4) \
        + T(x + 3, y + 18, ["A"], 9, C["c"], weight="700", anchor="middle") \
        + T(x + 13, y + 5, ["a"], 9, C["c"], weight="700", anchor="middle")


def ic_vasos(x, y):
    s = ""
    for xx in (x + 1, x + 22):
        s += _p((xx, y + 10), (xx, y + 30), (xx + 11, y + 30), (xx + 11, y + 10), sw=1.8)
    return s + _flechita(x + 14, y + 20, x + 21, sw=1.6)


def ic_particulas(x, y):
    s = _circ(x + 17, y + 17, 15)
    for dx, dy in ((-6, -6), (5, -7), (-7, 5), (6, 6), (0, 0)):
        s += f'<circle cx="{x + 17 + dx}" cy="{y + 17 + dy}" r="2.6" fill="{C["c"]}"/>'
    return s


def ic_unidades(x, y):
    return T(x + 17, y + 14, ["g"], 13, C["c"], weight="700", anchor="middle") \
        + _p((x + 17, y + 17), (x + 17, y + 24), sw=1.8) + _p((x + 13, y + 21), (x + 17, y + 25), (x + 21, y + 21), sw=1.8) \
        + T(x + 17, y + 36, ["mol"], 11, C["c"], weight="700", anchor="middle")


def ic_fuerzas(x, y):
    return rect(x + 11, y + 11, 12, 12, C["soft"], r=2, stroke=C["c"], sw=1.8) \
        + _flechita(x + 23, y + 17, x + 34, sw=1.8) + _p((x + 17, y + 23), (x + 17, y + 33), sw=1.8) \
        + _p((x + 13, y + 29), (x + 17, y + 33), (x + 21, y + 29), sw=1.8) + _p((x + 11, y + 17), (x + 1, y + 17), sw=1.8)


def ic_energia(x, y):
    return rect(x + 2, y + 6, 8, 26, C["soft"], r=1, stroke=C["c"], sw=1.6) \
        + rect(x + 14, y + 16, 8, 16, C["soft"], r=1, stroke=C["c"], sw=1.6) \
        + rect(x + 26, y + 24, 8, 8, C["soft"], r=1, stroke=C["c"], sw=1.6)


def ic_hueco(x, y):
    return _p((x + 1, y + 20), (x + 8, y + 20), c=LN_C) + rect(x + 11, y + 10, 13, 14, C["soft"], r=2, stroke=C["c"],
                                                               sw=1.8) + _p((x + 27, y + 20), (x + 34, y + 20), c=LN_C)


def ic_aviso(x, y):
    return rect(x + 3, y + 2, 28, 18, "white", r=3, stroke=C["c"], sw=2) + _p((x + 17, y + 20), (x + 17, y + 33), sw=2) \
        + _p((x + 8, y + 9), (x + 26, y + 9), c=LN_C, sw=1.6) + _p((x + 8, y + 14), (x + 22, y + 14), c=LN_C, sw=1.6)


def ic_charla(x, y):
    return rect(x + 1, y + 2, 20, 13, "white", r=5, stroke=C["c"], sw=1.8) \
        + rect(x + 13, y + 19, 20, 13, C["soft"], r=5, stroke=C["c"], sw=1.8)


def ic_linea(x, y):
    s = ""
    for yy in (6, 13, 20):
        s += _p((x + 2, y + yy), (x + 26, y + yy), c=LN_C, sw=1.8)
    return s + _circ(x + 23, y + 23, 6) + _p((x + 27, y + 27), (x + 33, y + 33), sw=2.6)


# ───────── qué ofrece cada área ─────────
# pide: los 4 tipos de tarea que salieron de las preguntas reales (ver el análisis).
# herr: la caja de herramientas: (rótulo, dibujito). linea2: qué va en la 2.ª línea de la fila A.
V2 = {
    "mate": dict(
        pide=["calcular un valor", "representar", "validar una afirmación", "ver si los datos alcanzan"],
        linea2=("texto", "En mis palabras y en qué unidad:"),
        izq=("LOS DATOS QUE SÍ USO", "con su unidad; tacho los que sobran"),
        centro="MI CAMINO", fondo="cuadricula",
        herr=[("cuentas en orden", ic_cuentas), ("figura con medidas", ic_figura),
              ("tabla o casos", ic_tabla), ("pruebo con un número", ic_pruebo)],
        der="comprobacion"),
    "lc": dict(
        pide=["qué dice", "cómo se arma", "qué supone o infiere", "qué tan válido es"],
        linea2=("texto", "Qué dice el texto (o la imagen), en una frase mía:"),
        izq="evidencia",
        centro="MI LECTURA", fondo="limpio",
        herr=[("subrayo y copio", ic_subrayo), ("mapa de párrafos", ic_mapa),
              ("tesis y razones", ic_tesis), ("la imagen por partes", ic_imagen)],
        der="trampas"),
    "soc": dict(
        pide=["qué concepto o norma", "qué busca cada actor", "qué efectos trae", "qué supone un argumento"],
        linea2=("texto", "Lo que está en juego (un derecho, un interés, una norma):"),
        izq="situacion",
        centro="MI MAPA", fondo="limpio",
        herr=[("la mesa de las voces", ic_voces), ("rueda de dimensiones", ic_rueda),
              ("línea de tiempo", ic_tiempo), ("causa y efecto", ic_causa)],
        der=("LA IDEA CLAVE", "concepto, norma o principio")),
    "bio": dict(
        pide=["explicar un proceso", "predecir qué pasa si…", "leer datos o un experimento",
              "valorar una conclusión"],
        linea2=("chips", "¿En qué escala pasa?", ["molécula", "célula", "organismo", "población", "ecosistema"]),
        izq=("LO QUE CAMBIA", "la variable o el dato que manda"),
        centro="MI ESQUEMA", fondo="limpio",
        herr=[("cadena de causas", ic_cadena), ("ejes y curva", ic_ejes),
              ("control y prueba", ic_control), ("cruce de genes", ic_punnett)],
        der="concluyo"),
    "qui": dict(
        pide=["explicar con partículas", "calcular una cantidad", "clasificar o identificar",
              "leer datos o un experimento"],
        linea2=("chips", "¿En qué nivel está la pregunta?", ["lo que se ve", "las partículas",
                                                               "el símbolo y el número"]),
        izq="vaso",
        centro="MI DIBUJO O MI CUENTA", fondo="limpio",
        herr=[("antes y después", ic_vasos), ("dibujo partículas", ic_particulas),
              ("cuenta con unidades", ic_unidades), ("control y prueba", ic_control)],
        der="propiedad"),
    "fis": dict(
        pide=["explicar o predecir", "calcular una magnitud", "escoger gráfica o diagrama",
              "evaluar un experimento"],
        linea2="predigo",
        izq="magnitudes",
        centro="DIBUJO EL SISTEMA", fondo="puntos",
        herr=[("fuerzas y vectores", ic_fuerzas), ("energía por tramos", ic_energia),
              ("ejes y curva", ic_ejes), ("control y prueba", ic_control)],
        der="ley"),
    "ing": dict(
        pide=["la palabra que va", "dónde o quién", "qué responder", "qué dice o deja entender"],
        linea2=("texto", "La línea que manda (la copio; si hay hueco, lo dejo):"),
        izq=("LO QUE DICE, EN ESPAÑOL", "la línea, el aviso o la pregunta"),
        centro="MI RAZONAMIENTO", fondo="renglones",
        herr=[("la palabra que falta", ic_hueco), ("dónde lo veo", ic_aviso),
              ("lo que me dicen", ic_charla), ("la línea que responde", ic_linea)],
        der="pista", pie="ing"),
}

# geometría del cuerpo del esquema (ancho 1270)
HA, GAP, HB, HC = 84, 14, 258, 54        # fila A · separación · fila B · fila C
WL, WR, GA = 268, 258, 34                # caja izquierda · caja derecha · hueco con flecha
WT = 176                                 # franja de la caja de herramientas


def _check_fila(b, x, y, ops, x_max, size=16, gap=22):
    """Fila de casillas medida con tw(); si no cabe, baja el tamaño hasta 14."""
    while True:
        ancho = sum(tw(o, size) + 30 for o in ops) + gap * (len(ops) - 1)
        if x + ancho <= x_max or size <= 14:
            break
        size -= 0.5
    assert x + ancho <= x_max, f"no caben: {ops}"
    for o in ops:
        x += check(b, x, y, o, size) + gap
    return x


def _chips_fila(b, x, y, ops, x_max, size=16):
    """Pastillas para encerrar (escala, nivel); ancho medido con tw()."""
    for i, o in enumerate(ops):
        wch = tw(o, size) + 30
        b.append(rect(x, y - 24, wch, 34, "white", r=17, stroke=C["ln"], sw=2))
        b.append(T(x + wch / 2, y - 1, [o], size, INK, anchor="middle"))
        x += wch + 12
    assert x <= x_max, f"no caben las pastillas: {ops}"
    return x


def fila_a(b, cfg, x, y, w):
    """ME PIDEN: el tipo de tarea (marco uno) y la 2.ª línea propia del área."""
    c = C["c"]
    y1 = y + 22
    rot = "ME PIDEN"
    rotulo(b, x, y1, rot)
    x0 = x + tw(rot, 15, "700") + 1.5 * len(rot) + 20
    xf = _check_fila(b, x0, y1 + 2, cfg["pide"], x + w - 120)
    b.append(T(x + w, y1, ["marco uno"], 15, GRAY, style="italic", anchor="end"))
    assert xf <= x + w - tw("marco uno", 15, style="italic") - 10, "la fila ME PIDEN se monta"
    y2 = y + 72
    l2 = cfg["linea2"]
    if l2 == "predigo":                                   # Física: la predicción, antes de mirar
        t1 = "Predigo antes de mirar: si"
        b.append(T(x, y2, [t1], 17, c, weight="700"))
        xx = x + tw(t1, 17, "700") + 10
        b.append(line(xx, y2 + 4, xx + 200, y2 + 4, LN_W, 1.8)); xx += 216
        xx += check(b, xx, y2, "aumenta", 16) + 16
        xx += check(b, xx, y2, "disminuye", 16) + 16
        t2 = "entonces"
        b.append(T(xx, y2, [t2], 17, INK)); xx += tw(t2, 17) + 10
        b.append(line(xx, y2 + 4, x + w, y2 + 4, LN_W, 1.8))
        return
    if l2[0] == "texto":
        b.append(T(x, y2, [l2[1]], 17, c, weight="700"))
        xx = x + tw(l2[1], 17, "700") + 12
        b.append(line(xx, y2 + 4, x + w, y2 + 4, LN_W, 1.8))
        return
    # pastillas para encerrar + lo demás en un renglón
    b.append(T(x, y2, [l2[1]], 17, c, weight="700"))
    xx = _chips_fila(b, x + tw(l2[1], 17, "700") + 16, y2, l2[2], x + w)
    pista(b, xx + 4, y2 - 2, "encierro uno")


def _caja_txt(b, x, y, w, h, titulo, hint, fill="white", stroke=None, dash=None, acento=False, n=None):
    return caja(b, x, y, w, h, titulo, hint, fill=fill, stroke=stroke, dash=dash, acento=acento, n=n)


def izquierda(b, cfg, x, y, w, h):
    c = C["c"]
    iz = cfg["izq"]
    if isinstance(iz, tuple):
        _caja_txt(b, x, y, w, h, iz[0], iz[1])
        return
    if iz == "evidencia":                                  # Lectura Crítica: la cita, con comillas
        b.append(rect(x, y, w, h, C["bg"], r=14))
        b.append(rect(x, y, 8, h, c, r=4))
        b.append(T(x + w - 18, y + 92, ["”"], 96, c, weight="700", op=0.35, anchor="end"))
        rotulo(b, x + 26, y + 30, "LA EVIDENCIA")
        svg, yy = TJ(x + 26, y + 38, "copio la frase exacta o señalo la parte de la imagen",
                     w - 96, 15, GRAY, style="italic", lh=20)
        b.append(svg)
        n = int((y + h - 54 - (yy + 40)) // STEP) + 1
        renglones(b, x + 26, yy + 40, w - 44, n)
        b.append(T(x + 26, y + h - 18, ["párrafo, línea o recuadro n.º"], 15, GRAY, style="italic"))
        b.append(line(x + 26 + tw("párrafo, línea o recuadro n.º", 15, style="italic") + 8, y + h - 14,
                      x + w - 18, y + h - 14, LN_W, 1.8))
        return
    if iz == "situacion":                                  # Sociales: la situación, en el centro de todo
        cx, cy, rx, ry = x + w / 2, y + h / 2, w / 2, h / 2
        b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{C["bg"]}" stroke="{c}" stroke-width="2.4"/>')
        b.append(T(cx, y + 50, ["LA SITUACIÓN"], 15, c, weight="700", anchor="middle", ls=1.5))
        b.append(T(cx, y + 74, ["quién, dónde, cuándo"], 15, GRAY, style="italic", anchor="middle"))
        for i, yy in enumerate((y + 120, y + 166, y + 208)):
            dy = abs(yy - cy) / ry
            half = rx * (1 - dy * dy) ** 0.5 - 26
            b.append(line(cx - half, yy, cx + half, yy, LN_W, 1.8))
        return
    if iz == "vaso":                                       # Química: lo que hay, dentro de un vaso
        b.append(beaker(x + 14, y + 12, w - 28, h - 12, c, "white"))
        rotulo(b, x + 34, y + 44, "LAS SUSTANCIAS")
        b.append(T(x + 34, y + 66, ["y los datos que uso, con unidad"], 15, GRAY, style="italic"))
        renglones(b, x + 34, y + 114, w - 68, 3)
        return
    if iz == "magnitudes":                                 # Física: símbolo = valor y unidad
        b.append(rect(x, y, w, h, C["bg"], r=14))
        rotulo(b, x + 18, y + 30, "LAS MAGNITUDES")
        pista(b, x + 18, y + 54, "símbolo = valor y unidad")
        for i in range(4):
            yy = y + 104 + i * STEP
            b.append(line(x + 18, yy, x + 70, yy, C["ln"], 2))
            b.append(T(x + 84, yy - 4, ["="], 20, c, weight="700"))
            b.append(line(x + 108, yy, x + w - 18, yy, C["ln"], 2))
        return
    raise ValueError(iz)


def centro(b, cfg, x, y, w, h):
    """El espacio libre para razonar, con la caja de herramientas del área a la izquierda."""
    c = C["c"]
    b.append(rect(x, y, w, h, "white", r=14, stroke=C["ln"], sw=2.2))
    # franja de herramientas
    b.append(rect(x, y, WT, h, C["bg"], r=14))
    b.append(rect(x + WT - 14, y, 14, h, C["bg"], r=0))
    rotulo(b, x + 14, y + 26, "HERRAMIENTA", size=14)
    yy = y + 40
    th = (h - 46) / 4
    for lab, ic in cfg["herr"]:
        b.append(rect(x + 12, yy + th / 2 - 10, 20, 20, "white", r=4, stroke=c, sw=2))
        b.append(ic(x + 40, yy + th / 2 - 17))
        lines = [" ".join(l) for l in wrap_px(lab, 14, WT - 90)]
        assert len(lines) <= 2, f"rótulo de herramienta muy largo: {lab}"
        y0 = yy + th / 2 + 5 - (len(lines) - 1) * 8
        b.append(T(x + 82, y0, lines, 14, INK, lh=16))
        for l in lines:
            assert x + 82 + tw(l, 14) <= x + WT - 4, f"herramienta se sale: {l}"
        yy += th
    # el lienzo
    xl, wl = x + WT, w - WT
    f = cfg["fondo"]
    if f == "cuadricula":
        gx = xl + 26
        while gx < xl + wl - 8:
            b.append(line(gx, y + 62, gx, y + h - 8, C["soft"], 0.9, cap="butt")); gx += 26
        gy = y + 66
        while gy < y + h - 8:
            b.append(line(xl + 8, gy, xl + wl - 8, gy, C["soft"], 0.9, cap="butt")); gy += 26
    elif f == "puntos":
        for gx in range(int(xl + 22), int(xl + wl - 8), 28):
            for gy in range(int(y + 72), int(y + h - 8), 28):
                b.append(f'<circle cx="{gx}" cy="{gy}" r="1.8" fill="{C["ln"]}"/>')
    elif f == "renglones":
        renglones(b, xl + 18, y + 92, wl - 36, int((h - 92 - 12) // STEP) + 1)
    rotulo(b, xl + 18, y + 26, cfg["centro"])
    b.append(T(xl + 18, y + 48, ["con la herramienta que marqué"], 15, GRAY, style="italic"))


def derecha(b, cfg, x, y, w, h):
    c = C["c"]
    d = cfg["der"]
    if isinstance(d, tuple):
        _caja_txt(b, x, y, w, h, d[0], d[1], fill="white", acento=True)
        return
    if d == "comprobacion":                                # Matemáticas
        b.append(rect(x, y, w, h, C["bg"], r=14, stroke=C["ln"], sw=2.2))
        rotulo(b, x + 18, y + 30, "LA COMPROBACIÓN")
        yy = y + 72
        for t in ("lo reemplacé en el enunciado", "unidad y tamaño creíbles",
                  "un caso que la tumba", "el paso con el error"):
            check(b, x + 18, yy, t, size=16)
            yy += 40
        pista(b, x + 18, y + h - 18, "marco lo que hice")
        return
    if d == "trampas":                                     # Lectura Crítica: el código de cada descarte
        b.append(rect(x, y, w, h, "white", r=14, stroke=C["ln"], sw=2.2))
        b.append(rect(x, y, 8, h, c, r=4))
        rotulo(b, x + 26, y + 30, "LAS TRAMPAS")
        pista(b, x + 26, y + 54, "pongo la letra en lo que tacho")
        yy = y + 92
        for k, t in (("N", "no lo dice"), ("O", "dice otra cosa"), ("E", "exagera o generaliza"),
                     ("R", "cierto, pero no responde")):
            b.append(_circ(x + 42, yy - 6, 14))
            b.append(T(x + 42, yy, [k], 16, c, weight="700", anchor="middle"))
            b.append(T(x + 66, yy, [t], 16, INK))
            assert x + 66 + tw(t, 16) <= x + w - 10, t
            yy += 38
        return
    if d == "concluyo":                                    # Biología
        hs = 94
        _caja_txt(b, x, y, w, h - hs - 12, "LO QUE SÍ CONCLUYO", "solo lo que los datos dicen",
                  fill=C["bg"])
        yb = y + h - hs
        b.append(rect(x, yb, w, hs, "white", r=14, stroke=C["ln"], sw=2.2, dash="8,6"))
        rotulo(b, x + 18, yb + 28, "LO QUE NO ALCANZA")
        renglones(b, x + 18, yb + 74, w - 36, 1)
        return
    if d == "propiedad":                                   # Química
        y1 = caja(b, x, y, w, h - 52, "LO QUE DECIDE", "la propiedad, el modelo o la ley", acento=True)
        check(b, x + 4, y + h - 12, "átomos y masa cuadran", size=16)
        return
    if d == "ley":                                         # Física
        caja(b, x, y, w, h - 52, "LA LEY QUE MANDA", "el principio y su fórmula", acento=True)
        check(b, x + 4, y + h - 12, "las unidades cuadran", size=16)
        return
    if d == "pista":                                       # Inglés
        b.append(rect(x, y, w, h, C["bg"], r=14, stroke=c, sw=2.4))
        lx, ly = x + 34, y + 30
        b.append(_circ(lx, ly, 13, sw=3))
        b.append(line(lx + 10, ly + 10, lx + 20, ly + 20, c, 4))
        rotulo(b, x + 60, y + 36, "LA PISTA QUE MANDA")
        yy = y + 84
        for t in ("la palabra de al lado", "el tiempo del verbo", "el lugar o quién habla",
                  "un conector o un número"):
            check(b, x + 18, yy, t, size=16)
            yy += 38
        b.append(T(x + 18, y + h - 16, ["otra:"], 16, GRAY))
        b.append(line(x + 18 + tw("otra:", 16) + 8, y + h - 12, x + w - 18, y + h - 12, LN_W, 1.8))
        return
    raise ValueError(d)


def fila_c(b, cfg, x, y, w):
    """TACHO CON RAZÓN: una razón por cada opción que descarto."""
    c = C["c"]
    yb = y + 36
    if cfg.get("pie") == "ing":
        rot = "DESCARTÉ"
        rotulo(b, x, yb, rot)
        xx = x + tw(rot, 15, "700") + 1.5 * len(rot) + 18
        mid = x + 760
        wq = (mid - 30 - xx) / 3
        for i, L in enumerate("ABC"):
            cx = xx + i * wq
            circulo_op(b, cx + 17, yb - 6, L, r=16, size=15)
            b.append(T(cx + 42, yb, ["porque"], 16, GRAY))
            b.append(line(cx + 42 + tw("porque", 16) + 8, yb + 4, cx + wq - 14, yb + 4, LN_W, 1.8))
        b.append(rect(mid, y, x + w - mid, HC, "white", r=14, stroke=C["ln"], sw=2.2))
        rotulo(b, mid + 18, yb, "PALABRA NUEVA")
        xx = mid + 18 + tw("PALABRA NUEVA", 15, "700") + 1.5 * 13 + 16
        b.append(line(xx, yb + 4, xx + 150, yb + 4, LN_W, 1.8))
        b.append(T(xx + 162, yb, ["="], 18, c, weight="700"))
        b.append(line(xx + 184, yb + 4, x + w - 18, yb + 4, LN_W, 1.8))
        return
    rot = "TACHO CON RAZÓN"
    rotulo(b, x, yb, rot)
    xx = x + tw(rot, 15, "700") + 1.5 * len(rot) + 18
    wq = (x + w - xx) / 4
    lc = cfg["der"] == "trampas"
    for i, L in enumerate("ABCD"):
        cx = xx + i * wq
        circulo_op(b, cx + 17, yb - 6, L, r=16, size=15)
        x1 = cx + 42
        if lc:      # casilla para la letra de la trampa
            b.append(rect(x1, yb - 25, 32, 34, "white", r=6, stroke=C["ln"], sw=2))
            x1 += 44
        t = "no:"
        b.append(T(x1, yb, [t], 16, GRAY))
        b.append(line(x1 + tw(t, 16) + 8, yb + 4, cx + wq - 16, yb + 4, LN_W, 1.8))


def esq_v2(b, clave, x, y, w, h):
    cfg = V2[clave]
    global HB
    HB = h - HA - 2 * GAP - HC            # la fila B se queda con el alto que sobra (Inglés tiene más)
    fila_a(b, cfg, x, y, w)
    yb = y + HA + GAP
    izquierda(b, cfg, x, yb, WL, HB)
    xc = x + WL + GA
    wc = w - WL - WR - 2 * GA
    flecha(b, x + WL + 4, yb + HB / 2, xc - 6, yb + HB / 2)
    centro(b, cfg, xc, yb, wc, HB)
    xr = xc + wc + GA
    flecha(b, xc + wc + 4, yb + HB / 2, xr - 6, yb + HB / 2)
    derecha(b, cfg, xr, yb, WR, HB)
    fila_c(b, cfg, x, yb + HB + GAP, w)


# Hojas a doble cara por área (Nelson, 10 nov): 5 hojas = 10 páginas = 30 preguntas;
# 3 hojas = 6 páginas = 18 preguntas.
HOJAS = dict(mate=5, lc=5, soc=5, bio=3, qui=3, fis=3, ing=3)


# ───────── un esquema completo y la página ─────────
def esquema(b, clave, a, y, h, n=1):
    c = C["c"]
    b.append(BT.wob_rect(M, y, CW, h, BT.TINTA_B, 3, fill="white", seed=50 + int(y), amp=1.6))
    tmp = []
    y_m = membrete_esquema(tmp, a, y)
    hb = y_m - y + 6              # el membrete; debajo, el divisor a mano (sin banda de color)
    b.extend(tmp)
    # cuerpo
    yb = y + hb + 22
    xe = M + 30
    we = 1270
    wt = BT.twf(a["titulo"], 26, BT.SHA, "800")
    b.append(BT.resaltador(xe, yb - 16, wt, 26, BT.FOSFO_2, seed=int(y)))
    b.append(BT.TX(xe, yb + 6, a["titulo"], 26, BT.TINTA_B, BT.SHA, "800"))
    frag = []
    esq_v2(frag, clave, xe + 2, yb + 24, we - 4, y + h - 20 - (yb + 24))
    caja_ = tb.medir(frag)
    ylim = y + h - 16
    assert caja_[3] <= ylim and caja_[2] <= xe + we + 1 and caja_[0] >= xe - 2, \
        f"{clave}: el esquema se sale de su tarjeta {caja_} (tarjeta hasta y={ylim:.0f})"
    # en <g class="instrumento"> para que verifica_cajas.py mida alto y borde derecho
    b.append(f'<g class="instrumento" data-n="{n}" data-ymax="{ylim:.0f}" data-xmax="{xe + we}">'
             + "".join(frag) + "</g>")
    b.append(BT.wob_vline(xe + we + 22, yb - 10, y + h - 30, seed=int(y)))
    xr = xe + we + 44
    columna_cierre(b, xr, yb - 12, W - M - 30 - xr, y + h - 26 - yb + 12)


def hoja(clave, p, ruta, n_hojas=None):
    """Página p (1 … 2·n_hojas) del simulacro del área. n_hojas: el del área (HOJAS) si no se pasa."""
    a = AREA[clave]
    n_hojas = n_hojas or HOJAS[clave]
    assert 1 <= p <= 2 * n_hojas, f"{clave}: la página {p} no existe (son {2 * n_hojas})"
    colores(a["area"])
    b = svg_open()
    y = cabecera(b, a, p, n_hojas) + 22      # la cabecera pone la cuadrícula de puntos
    fondo = H_PAGE - 90 - 26 - 24
    g = 22
    h = (fondo - y - 2 * g) / 3
    for i in range(3):
        esquema(b, clave, a, y + i * (h + g), h, n=3 * p - 2 + i)
    BT.pie_b(b, f"S{p}", C["c"], texto=f"{a['area']} · Simulacro · hoja {(p + 1) // 2} de {n_hojas}")
    svg_close(b, ruta)
    return ruta


ORDEN = ["mate", "lc", "soc", "bio", "qui", "fis", "ing"]

if __name__ == "__main__":
    import render
    claves = sys.argv[1:] or ORDEN
    rutas = [hoja(cl, 1, OUT + f"sim_muestra_{cl}.svg") for cl in claves]
    os.makedirs("/tmp/claude-0/simulacro", exist_ok=True)
    pdf = "/tmp/claude-0/simulacro/Simulacro_muestras_v2.pdf"
    render.unir(rutas, pdf)
    print(pdf, render.verifica(pdf, marca="Aprende"))
