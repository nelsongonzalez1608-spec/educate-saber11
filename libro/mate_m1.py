#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MATEMÁTICAS · Momento 1 · Patrones y relaciones de cambio — taller de 10 preguntas.
Cada pregunta tiene su propio instrumento de pensamiento. Formato diario: fecha, primera idea, marca, lo que me llevo."""
import math, random
from lib import *

random.seed(7)
OUT = "/home/claude/libro/"
AZm = "#1F4E8C"; AZm_L = "#C3D7EA"; AZm_BG = "#EFF4FA"
EST = {1: ("Leer el cambio", EDU_AZUL), 2: ("La razón constante", EDU_VERDE),
       3: ("El crecimiento que se acumula", EDU_ORO), 4: ("Juzgar la afirmación", EDU_ROJO)}
BLK_H = 1100
IW = 1270                 # ancho del instrumento
RX_OFF = IW + 40          # inicio de la columna derecha


def hoja_header(b, pag, hojas_txt):
    b.append(rect(0, 0, W, 180, AZm_BG, r=0)); b.append(rect(0, 180, W, 6, AZm, r=0))
    b.append(logo(M, 44, 64))
    b.append(T(M + 230, 78, ["MATEMÁTICAS · MOMENTO 1"], 24, AZm, weight="700", ls=3))
    b.append(T(M + 230, 116, ["Patrones y relaciones de cambio · componente numérico-variacional"], 22, GRAY))
    b.append(T(M + 230, 150, [hojas_txt], 20, GRAY, style="italic"))
    # diario: fecha y ánimo
    b.append(T(W - M - 640, 78, ["Sábado ____ de ____________"], 24, INK))
    b.append(T(W - M - 640, 130, ["Llego:"], 22, GRAY))
    for k, mood in enumerate(["worried", "calm", "happy"]):
        b.append(face(W - M - 540 + k * 70, 122, 24, mood, GRAY, "white", sw=2.2))
    b.append(T(W - M - 300, 130, ["Salgo:"], 22, GRAY))
    for k, mood in enumerate(["worried", "calm", "happy"]):
        b.append(face(W - M - 200 + k * 70, 122, 24, mood, GRAY, "white", sw=2.2))


def bloque(b, y, q, instrumento):
    """Marco común de una pregunta. instrumento(b, x, y, w, h) dibuja el mapa propio."""
    n, est = q["n"], q["est"]
    enm, ec = EST[est]
    b.append(rect(M, y, CW, BLK_H, "white", r=26, stroke=AZm_L, sw=2.4))
    # banda superior
    b.append(rect(M, y, CW, 104, AZm_BG, r=26)); b.append(rect(M, y + 60, CW, 44, AZm_BG, r=0))
    b.append(num_badge(M + 60, y + 52, n, AZm, r=34, size=34))
    b.append(T(M + 112, y + 44, [f"Pregunta {n} del taller · la lees en tu libro"], 24, AZm, weight="700"))
    b.append(T(M + 112, y + 78, [q["ctx"]], 21, GRAY, style="italic"))
    cw_ = chip(b, M + 720, y + 30, f"Estrategia {est} · {enm}", ec, size=19, h=44)
    b.append(T(M + 1280, y + 44, ["Mi primera idea, antes de hacer nada:"], 20, GRAY))
    b.append(line(M + 1280, y + 86, W - M - 30, y + 86, LGRAY, 2.2))
    # instrumento
    instrumento(b, M + 30, y + 130, IW, BLK_H - 160)
    # columna derecha
    rx = M + RX_OFF; rw = W - M - rx - 24; ry = y + 130
    b.append(line(rx - 18, ry, rx - 18, y + BLK_H - 30, "#E6EAF0", 2, "6,6"))
    b.append(T(rx, ry + 26, ["MARCO AL FINAL"], 18, AZm, weight="700", ls=2))
    for k, L in enumerate("ABCD"):
        cx = rx + 36 + k * 92
        b.append(f'<circle cx="{cx}" cy="{ry+80}" r="30" fill="white" stroke="{AZm}" stroke-width="2.6"/>')
        b.append(T(cx, ry + 90, [L], 26, AZm, weight="700", anchor="middle"))
    b.append(T(rx, ry + 150, ["¿Qué tan seguro estoy?"], 18, GRAY))
    for k, lab in enumerate(["adiviné", "casi", "seguro"]):
        b.append(checkbox(rx + k * 150, ry + 164, s=11, c=GRAY)); b.append(T(rx + 30 + k * 150, ry + 182, [lab], 18, GRAY))
    # salvavidas
    sy = ry + 230
    b.append(rect(rx, sy, rw, 300, AZ_D, r=18))
    b.append(buoy(rx + 36, sy + 36, 13))
    b.append(T(rx + 62, sy + 43, ["SALVAVIDAS"], 18, "white", weight="700", ls=2))
    b.append(T(rx + 24, sy + 90, ["Lo mínimo que sí tenía claro:"], 18, "#BFD4F2"))
    b.append(line(rx + 24, sy + 130, rx + rw - 24, sy + 130, "white", 1.6, "6,6"))
    b.append(T(rx + 24, sy + 176, ["→ entonces tenía que ser"], 18, "#BFD4F2"))
    b.append(line(rx + 24, sy + 216, rx + rw - 24, sy + 216, "white", 1.6, "6,6"))
    b.append(T(rx + 24, sy + 258, ["y no podía ser ____ porque"], 18, "#BFD4F2"))
    b.append(line(rx + 290, sy + 262, rx + rw - 24, sy + 262, "white", 1.6, "6,6"))
    # lo que me llevo
    ly = sy + 340
    b.append(T(rx, ly + 20, ["Lo que me llevo de esta pregunta"], 20, AZm, weight="700"))
    b.append(T(rx, ly + 48, ["(una frase que me sirva en otra pregunta parecida)"], 16, GRAY, style="italic"))
    b.append(wlines(rx, ly + 100, rw, 4, c="#E3E8EF", step=48))
    # mini-sello de estrategia (abajo derecha del bloque)
    b.append(f'<circle cx="{W-M-60}" cy="{y+BLK_H-50}" r="18" fill="{ec}"/>')
    b.append(T(W - M - 60, y + BLK_H - 43, [str(est)], 18, "white", weight="700", anchor="middle"))


def titulo_instr(b, x, y, t, c, sub=None):
    b.append(T(x, y + 30, [t], 30, c, weight="700"))
    if sub:
        svg, yy = TJ(x, y + 42, sub, IW - 20, 20, GRAY, style="italic", lh=26)
        b.append(svg)
        return yy + 14
    return y + 56


def cajas(b, x, y, n, w=92, h=64, gap=14, c=AZm_L, labels=None, fill="white"):
    for i in range(n):
        b.append(rect(x + i * (w + gap), y, w, h, fill, r=10, stroke=c, sw=2))
        if labels:
            b.append(T(x + i * (w + gap) + w / 2, y + h + 26, [labels[i]], 18, GRAY, anchor="middle"))


# ═══════════ instrumentos ═══════════
def cuenta(b, x, y, w, h, label="mis cuentas"):
    b.append(grid_box(x, y, w, h, step=28))
    b.append(T(x + 14, y + 26, [label.upper()], 15, AZ_M, weight="700", ls=1))


def ejes_mini(b, x, y, w, h, titulo, c):
    b.append(rect(x, y, w, h, "white", r=10, stroke=c, sw=2))
    b.append(T(x + w / 2, y + 26, [titulo], 17, c, weight="700", anchor="middle"))
    b.append(line(x + 30, y + h - 24, x + w - 16, y + h - 24, GRAY, 1.6))
    b.append(line(x + 30, y + 40, x + 30, y + h - 24, GRAY, 1.6))
    b.append(T(x + w - 16, y + h - 6, ["mes"], 13, GRAY, anchor="end"))
    b.append(T(x + 8, y + 50, ["$"], 13, GRAY))


def inst_q1(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "La silueta de la temperatura", EDU_AZUL,
                      "No calcules todavía. Primero copia las temperaturas, luego dibuja los puntos y únelos: la forma que salga es la que buscas entre las gráficas.")
    horas = ["6:00", "7:00", "8:00", "9:00", "10:00", "11:00", "12:00"]
    b.append(T(x, yy + 22, ["Temperaturas del libro, hora a hora:"], 20, INK))
    cajas(b, x + 400, yy, 7, w=96, h=60, gap=12, labels=horas)
    yy += 120
    # lienzo
    gx, gy, gw, gh = x, yy, 820, h - (yy - y) - 150
    b.append(rect(gx, gy, gw, gh, "white", r=12, stroke=AZm_L, sw=2))
    for i in range(7):
        px = gx + 70 + i * (gw - 110) / 6
        b.append(line(px, gy + 16, px, gy + gh - 40, "#E6EAF0", 1.4))
        b.append(T(px, gy + gh - 14, [horas[i]], 16, GRAY, anchor="middle"))
    for j in range(0, 13, 2):
        py = gy + gh - 50 - j * (gh - 80) / 12
        b.append(line(gx + 60, py, gx + gw - 20, py, "#E6EAF0", 1.4))
        b.append(T(gx + 50, py + 6, [f"{j}°"], 15, GRAY, anchor="end"))
    b.append(PT(gx + gw - 30, gy + 40, ["pon un punto por hora y únelos"], 22, EDU_AZUL, rot=-1.5, anchor="end", op=0.75))
    # a la derecha del lienzo: flechas por tramo y la pregunta clave
    rx = gx + gw + 40
    b.append(T(rx, gy + 30, ["Entre una hora y la siguiente:"], 20, INK))
    b.append(T(rx, gy + 56, ["dibuja ↑ si sube, ↓ si baja"], 18, GRAY, style="italic"))
    for i in range(6):
        b.append(rect(rx + i * 62, gy + 76, 50, 50, "white", r=8, stroke=AZm_L, sw=2))
    b.append(T(rx, gy + 190, ["¿A qué hora deja de subir?"], 20, INK))
    b.append(line(rx + 330, gy + 194, rx + 400, gy + 194, LGRAY, 2))
    b.append(T(rx, gy + 230, ["Ese es el pico. Márcalo con una"], 18, GRAY))
    b.append(T(rx, gy + 254, ["bandera en tu dibujo."], 18, GRAY))
    b.append(rect(rx, gy + 290, 400, 120, AMBER_BG, r=12, stroke=AMBER_LN, sw=2))
    b.append(T(rx + 16, gy + 322, ["La gráfica correcta es la que"], 19, AMBER_D, weight="700"))
    b.append(T(rx + 16, gy + 348, ["tiene ESA silueta: sube hasta"], 19, AMBER_D, weight="700"))
    b.append(T(rx + 16, gy + 374, ["el pico y después se devuelve."], 19, AMBER_D, weight="700"))
    b.append(T(x, gy + gh + 40, ["Opciones que NO tienen esa forma (táchalas):   A   B   C   D"], 20, INK))


def inst_q2(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "La cinta del tiempo", EDU_AZUL,
                      "Un deportista que avanza lo mismo cada segundo es una cinta con marcas iguales. Llénala y la fórmula aparece sola.")
    # cinta
    cy = yy + 90
    b.append(rect(x, cy - 10, w - 20, 20, AZm_L, r=10))
    for s_ in range(9):
        px = x + 30 + s_ * (w - 80) / 8
        b.append(line(px, cy - 22, px, cy + 22, AZm, 3))
        b.append(T(px, cy - 34, [f"{s_} s"], 17, GRAY, anchor="middle"))
        b.append(rect(px - 42, cy + 40, 84, 54, "white", r=8, stroke=AZm_L, sw=2))
        if s_ == 0: b.append(PT(px, cy + 78, ["0"], 26, PENCIL, rot=-2, anchor="middle"))
    b.append(T(x, cy + 130, ["metros recorridos"], 17, GRAY))
    # saltos
    for s_ in range(8):
        px0 = x + 30 + s_ * (w - 80) / 8; px1 = x + 30 + (s_ + 1) * (w - 80) / 8
        b.append(hand_arrow(px0 + 8, cy - 60, px1 - 8, cy - 60, EDU_ORO, sw=2.6, bend=-0.5, head=12))
    b.append(T(x + (w - 20) / 2, cy - 110, ["cada salto: + ____ m"], 22, EDU_ORO, weight="700", anchor="middle"))
    # regla
    ry = cy + 190
    b.append(rect(x, ry, 600, 170, "white", r=14, stroke=AZm_L, sw=2))
    b.append(T(x + 20, ry + 40, ["La regla en palabras:"], 20, AZm, weight="700"))
    b.append(T(x + 20, ry + 84, ["distancia  =  ________  ×  ________"], 24, INK))
    b.append(T(x + 20, ry + 128, ["(lo que avanza cada segundo) × (los segundos)"], 17, GRAY, style="italic"))
    b.append(rect(x + 640, ry, 600, 170, "white", r=14, stroke=AZm_L, sw=2))
    b.append(T(x + 660, ry + 40, ["A los 8 segundos:"], 20, AZm, weight="700"))
    b.append(T(x + 660, ry + 90, ["____ × ____ = ______ m"], 26, INK))
    b.append(T(x + 660, ry + 132, ["¿coincide con la casilla de 8 s de la cinta?"], 17, GRAY, style="italic"))
    b.append(T(x, ry + 220, ["Ahora lee las opciones: la correcta dice el número Y la razón (la velocidad no cambia). Las que dicen"], 19, INK))
    b.append(T(x, ry + 248, ["un número con una razón falsa, táchalas aunque el número esté bien."], 19, INK))
    py = ry + 290
    b.append(rect(x, py, w - 20, 150, SOFT, r=14))
    b.append(T(x + 20, py + 38, ["Para pensar: si en vez de 5 m cada segundo avanzara 5, luego 6, luego 7… ¿las marcas de la cinta serían iguales?"], 19, INK))
    b.append(T(x + 20, py + 68, ["Dibuja cómo se verían:"], 18, GRAY, style="italic"))
    b.append(rect(x + 20, py + 90, w - 60, 20, "white", r=10, stroke=AZm_L, sw=2))
    b.append(line(x + 40, py + 78, x + 40, py + 122, AZm, 3))


def inst_q3(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "El traductor", EDU_VERDE,
                      "Esta pregunta no pide calcular: pide traducir. A la izquierda, lo que dice el enunciado; a la derecha, cómo se escribe en símbolos.")
    rows = [("el 46,5 %", "como decimal"), ("de los hombres encuestados", "¿qué letra es ese total?"),
            ("cuántos hombres leyeron", "¿qué letra es el resultado?")]
    for i, (a, hint) in enumerate(rows):
        ry = yy + 10 + i * 96
        b.append(rect(x, ry, 520, 72, SOFT, r=10))
        b.append(T(x + 20, ry + 44, [a], 24, INK, weight="700"))
        b.append(hand_arrow(x + 540, ry + 36, x + 640, ry + 36, EDU_VERDE, sw=3, bend=0, head=16))
        b.append(rect(x + 660, ry, 300, 72, "white", r=10, stroke=EDU_VERDE, sw=2))
        b.append(T(x + 980, ry + 44, [hint], 18, GRAY, style="italic"))
    yy += 10 + 3 * 96 + 30
    # tres puertas
    b.append(T(x, yy + 24, ["¿Qué operación convierte un porcentaje en una cantidad de personas? Tacha las dos puertas falsas:"], 20, INK))
    for i, (op, lab) in enumerate([("+", "sumar"), ("×", "multiplicar"), ("÷", "dividir")]):
        px = x + 80 + i * 220
        b.append(rect(px, yy + 50, 160, 130, "white", r=14, stroke=EDU_VERDE, sw=2.4))
        b.append(rect(px + 56, yy + 50, 48, 130, EDU_VERDE, r=0, op=0.08))
        b.append(T(px + 80, yy + 128, [op], 54, EDU_VERDE, weight="700", anchor="middle"))
        b.append(T(px + 80, yy + 204, [lab], 18, GRAY, anchor="middle"))
    # expresión final
    ex = x + 780
    b.append(rect(ex, yy + 50, w - 780, 180, AMBER_BG, r=14, stroke=AMBER_LN, sw=2))
    b.append(T(ex + 20, yy + 90, ["Escribo la expresión completa:"], 19, AMBER_D, weight="700"))
    b.append(T(ex + 20, yy + 150, ["H  =  ______  ×  ______"], 34, INK))
    b.append(T(ex + 20, yy + 200, ["y busco la opción que diga exactamente eso"], 17, GRAY, style="italic"))
    b.append(T(x, yy + 270, ["Trampa frecuente: confundir «el porcentaje» (46,5) con «el número de personas» (H). Son cosas distintas."], 19, EDU_ROJO))
    b.append(rect(x, yy + 300, w - 20, 96, SOFT, r=14))
    b.append(T(x + 20, yy + 340, ["Para comprobar que lo entendiste: escribe la misma expresión para las mujeres (35,2 %):"], 19, INK))
    b.append(T(x + 20, yy + 380, ["M  =  ______  ×  ______"], 26, INK))


def inst_q4(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "Dos canastas", EDU_VERDE,
                      "Son 800 personas, pero no son un solo grupo: cada canasta tiene su propio porcentaje. Llena las dos y después júntalas.")
    cy = yy + 170
    for i, (nm, pct, c) in enumerate([("HOMBRES", "46,5 %", EDU_AZUL), ("MUJERES", "35,2 %", EDU_ROJO)]):
        cx = x + 330 + i * 560
        b.append(f'<circle cx="{cx}" cy="{cy}" r="140" fill="white" stroke="{c}" stroke-width="3"/>')
        b.append(T(cx, cy - 80, [nm], 20, c, weight="700", anchor="middle", ls=2))
        b.append(T(cx, cy - 42, ["400 personas"], 20, GRAY, anchor="middle"))
        b.append(T(cx, cy + 6, [f"400 × {pct}"], 24, INK, anchor="middle"))
        b.append(T(cx, cy + 44, ["= ________"], 30, INK, anchor="middle"))
        b.append(T(cx, cy + 88, ["leyeron"], 18, GRAY, anchor="middle"))
        b.append(hand_arrow(cx + (60 if i == 0 else -60), cy + 150, x + 610 + (-40 if i == 0 else 40), cy + 240, c, sw=3, bend=(0.15 if i == 0 else -0.15), head=16))
    by = cy + 250
    b.append(rect(x + 440, by, 340, 150, AMBER_BG, r=16, stroke=AMBER_LN, sw=2))
    b.append(T(x + 610, by + 36, ["TOTAL que leyó"], 20, AMBER_D, weight="700", anchor="middle"))
    b.append(T(x + 610, by + 78, ["____ + ____"], 24, INK, anchor="middle"))
    b.append(T(x + 610, by + 126, ["≈ ________ personas"], 26, INK, anchor="middle"))
    # trampa
    ty = by + 190
    b.append(rect(x, ty, w - 20, 110, "white", r=14, stroke=EDU_ROJO, sw=2, dash="8,6"))
    b.append(T(x + 24, ty + 40, ["La trampa: «800 × un solo porcentaje».  ¿Por qué no sirve?"], 21, EDU_ROJO, weight="700"))
    b.append(line(x + 24, ty + 86, x + w - 120, ty + 86, LGRAY, 2))
    b.append(spath([(x + w - 100, ty + 24), (x + w - 44, ty + 86)], EDU_ROJO, 4)); b.append(spath([(x + w - 44, ty + 24), (x + w - 100, ty + 86)], EDU_ROJO, 4))
    b.append(T(x, ty + 150, ["Redondea al final, no en cada canasta. La opción correcta es la más cercana a tu total, no la exacta."], 19, INK))


def inst_q5(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "La escalera de aumentos", EDU_ORO,
                      "Para saber si algo crece «parejo» o «cada vez más», no mires los saldos: mira cuánto sube de un mes al siguiente.")
    # tabla
    cols = ["Mes", "Saldo (del libro)", "Aumento = saldo − anterior", "¿Igual al anterior?"]
    cw_ = [100, 300, 380, 260]
    tx = x
    for i, c_ in enumerate(cols):
        b.append(rect(tx, yy, cw_[i] - 6, 44, EDU_ORO, r=8)); b.append(T(tx + 12, yy + 30, [c_], 17, "white", weight="700")); tx += cw_[i]
    for r in range(4):
        ry = yy + 52 + r * 60; tx = x
        for i in range(4):
            b.append(rect(tx, ry, cw_[i] - 6, 52, "white" if i else SOFT, r=8, stroke=AZm_L, sw=1.6))
            if i == 0: b.append(T(tx + cw_[i] / 2, ry + 34, [str(r + 1)], 22, INK, anchor="middle"))
            if i == 2 and r == 0: b.append(T(tx + 12, ry + 34, ["—"], 20, GRAY))
            if i == 3 and r > 0:
                b.append(T(tx + 20, ry + 34, ["igual"], 18, GRAY)); b.append(checkbox(tx + 90, ry + 14, s=10))
                b.append(T(tx + 140, ry + 34, ["más"], 18, GRAY)); b.append(checkbox(tx + 190, ry + 14, s=10))
            tx += cw_[i]
    # escalera dibujada
    sx = x + 1080; base = yy + 52 + 4 * 60
    for k in range(4):
        hh = 30 + k * 22
        b.append(rect(sx + k * 40, base - hh, 36, hh, EDU_ORO, r=4, op=0.35 + k * 0.15))
    b.append(T(sx - 10, base + 26, ["¿los escalones crecen?"], 16, GRAY))
    # veredicto
    vy = yy + 52 + 4 * 60 + 60
    b.append(T(x, vy + 24, ["Veredicto — encierra uno:"], 21, INK, weight="700"))
    b.append(rect(x + 330, vy - 6, 420, 56, "white", r=28, stroke=EDU_AZUL, sw=2.4))
    b.append(T(x + 540, vy + 30, ["aumentos iguales → LINEAL"], 20, EDU_AZUL, anchor="middle"))
    b.append(rect(x + 780, vy - 6, 460, 56, "white", r=28, stroke=EDU_ORO, sw=2.4))
    b.append(T(x + 1010, vy + 30, ["aumentos que crecen → EXPONENCIAL"], 20, EDU_ORO, anchor="middle"))
    b.append(T(x, vy + 100, ["¿Por qué crecen? Porque el 2 % se calcula cada mes sobre un saldo ________ que el anterior."], 20, INK))
    dy = vy + 140
    b.append(T(x, dy + 20, ["Dibuja la forma de cada crecimiento y encierra la que se parece al ahorro de Camilo:"], 19, INK))
    ejes_mini(b, x, dy + 36, 300, 190, "LINEAL (aumentos iguales)", EDU_AZUL)
    ejes_mini(b, x + 330, dy + 36, 300, 190, "EXPONENCIAL (crecen)", EDU_ORO)
    cuenta(b, x + 670, dy + 36, w - 690, 190)


def inst_q6(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "La máquina × 1,02", EDU_ORO,
                      "Cada mes el saldo entra a la máquina y sale multiplicado por 1,02. Para llegar al mes 6 hay que pasarlo tantas veces como meses falten.")
    cy = yy + 120
    meses = [3, 4, 5, 6]
    for i, m_ in enumerate(meses):
        bx = x + i * 320
        b.append(rect(bx, cy - 40, 200, 110, "white", r=12, stroke=AZm_L, sw=2))
        b.append(T(bx + 100, cy - 10, [f"mes {m_}"], 18, GRAY, anchor="middle"))
        b.append(T(bx + 100, cy + 44, ["________"], 26, INK, anchor="middle"))
        if i == 0: b.append(PT(bx + 100, cy + 46, ["1.061.208"], 26, PENCIL, rot=-1, anchor="middle"))
        if i < 3:
            gx = bx + 230
            b.append(f'<circle cx="{gx+30}" cy="{cy+15}" r="34" fill="{EDU_ORO}"/>')
            for k in range(8):
                a = k * math.pi / 4
                b.append(f'<rect x="{gx+30+40*math.cos(a)-7}" y="{cy+15+40*math.sin(a)-7}" width="14" height="14" fill="{EDU_ORO}" transform="rotate({k*45} {gx+30+40*math.cos(a)} {cy+15+40*math.sin(a)})"/>')
            b.append(T(gx + 30, cy + 22, ["×1,02"], 15, "white", weight="700", anchor="middle"))
    b.append(T(x, cy + 130, ["o de una vez:  1.061.208 × 1,02 × 1,02 × 1,02  =  1.061.208 × (1,02)³  ≈  ____________"], 22, INK))
    # trampa
    ty = cy + 190
    b.append(rect(x, ty, 760, 150, "white", r=14, stroke=EDU_ROJO, sw=2, dash="8,6"))
    b.append(T(x + 20, ty + 40, ["La trampa: sumar 20.000 tres veces."], 21, EDU_ROJO, weight="700"))
    b.append(T(x + 20, ty + 76, ["1.061.208 + 60.000 = 1.121.208.  ¿Se parece a la respuesta?"], 19, INK))
    b.append(T(x + 20, ty + 112, ["Sí, se parece. Por eso la opción cercana no es «la correcta»: la correcta es la que crece de verdad."], 17, GRAY, style="italic"))
    b.append(rect(x + 800, ty, w - 820, 150, AMBER_BG, r=14, stroke=AMBER_LN, sw=2))
    b.append(T(x + 820, ty + 44, ["Elijo la opción más cercana a mi número,"], 19, AMBER_D, weight="700"))
    b.append(T(x + 820, ty + 74, ["y escribo cuánto se aleja:"], 19, AMBER_D, weight="700"))
    b.append(T(x + 820, ty + 120, ["diferencia: ________"], 22, INK))
    cy2 = ty + 180
    b.append(rect(x, cy2, 480, 200, SOFT, r=14))
    b.append(T(x + 20, cy2 + 36, ["Comprobación del mes 4 por la otra ruta:"], 18, AZm, weight="700"))
    b.append(T(x + 20, cy2 + 78, ["2 % de 1.061.208 = ________"], 19, INK))
    b.append(T(x + 20, cy2 + 118, ["1.061.208 + ese 2 % = ________"], 19, INK))
    b.append(T(x + 20, cy2 + 160, ["¿da lo mismo que × 1,02?   sí / no"], 18, GRAY, style="italic"))
    cuenta(b, x + 510, cy2, w - 530, 200)


def inst_q7(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "La lupa sobre las diferencias", EDU_ORO,
                      "Ya sabes que el ahorro crece. Esta pregunta pide algo más fino: ¿cómo crece el crecimiento? Pon la lupa sobre los aumentos.")
    cy = yy + 110
    aum = ["20.000", "20.400", "20.808"]
    for i, a in enumerate(aum):
        bx = x + 60 + i * 400
        b.append(rect(bx, cy - 34, 220, 80, "white", r=12, stroke=EDU_ORO, sw=2.4))
        b.append(T(bx + 110, cy - 6, [f"aumento mes {i+1}→{i+2}"], 15, GRAY, anchor="middle"))
        b.append(PT(bx + 110, cy + 34, [a], 28, PENCIL, rot=-1, anchor="middle"))
        if i < 2:
            b.append(hand_arrow(bx + 236, cy + 6, bx + 384, cy + 6, EDU_ORO, sw=3, bend=-0.3, head=16))
            b.append(rect(bx + 260, cy + 40, 100, 44, "white", r=8, stroke=AZm_L, sw=2))
            b.append(T(bx + 310, cy + 110, ["+ ¿cuánto?"], 16, GRAY, anchor="middle"))
    # lupa
    lx, ly = x + 60, cy + 200
    b.append(f'<circle cx="{lx+70}" cy="{ly+50}" r="56" fill="{AMBER_BG}" stroke="{EDU_ORO}" stroke-width="5"/>')
    b.append(line(lx + 112, ly + 92, lx + 170, ly + 150, EDU_ORO, 12))
    b.append(T(lx + 200, ly + 30, ["Los aumentos:"], 20, INK, weight="700"))
    for k, lab in enumerate(["se mantienen", "crecen", "se achican"]):
        b.append(checkbox(lx + 200 + k * 230, ly + 46, s=11, c=EDU_ORO)); b.append(T(lx + 234 + k * 230, ly + 64, [lab], 19, INK))
    b.append(T(lx + 200, ly + 120, ["¿Y la diferencia entre los aumentos (los «+ ¿cuánto?»)?  también ________"], 19, INK))
    # por qué
    py = ly + 190
    b.append(rect(x, py, w - 20, 130, AMBER_BG, r=14, stroke=AMBER_LN, sw=2))
    b.append(T(x + 20, py + 40, ["La razón en una frase (la vas a necesitar para escoger la afirmación):"], 19, AMBER_D, weight="700"))
    b.append(T(x + 20, py + 90, ["la tasa es fija (2 %), pero se aplica sobre un saldo que cada mes es ______________, así que el aumento ______________."], 19, INK))
    cuenta(b, x, py + 160, w - 20, 170, "mis cuentas · las restas")


def inst_q8(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "El juicio de las fórmulas", EDU_ORO,
                      "Las cuatro opciones son fórmulas acusadas. Cada una pasa por tres preguntas. Solo la que responda bien a las tres queda absuelta.")
    cols = ["Opción", "¿Aplica el interés mes a mes\n(no una sola vez al final)?", "¿Multiplica por 1,02\n(no suma 2 % doce veces)?", "¿El exponente es 12\n(el número de meses)?", "Veredicto"]
    cw_ = [110, 330, 330, 300, 180]
    tx = x
    for i, c_ in enumerate(cols):
        b.append(rect(tx, yy, cw_[i] - 6, 70, EDU_ORO, r=8))
        for j, ln in enumerate(c_.split("\n")):
            b.append(T(tx + 12, yy + 30 + j * 22, [ln], 15, "white", weight="700"))
        tx += cw_[i]
    for r, L in enumerate("ABCD"):
        ry = yy + 78 + r * 62; tx = x
        for i in range(5):
            b.append(rect(tx, ry, cw_[i] - 6, 54, SOFT if i == 0 else "white", r=8, stroke=AZm_L, sw=1.6))
            if i == 0: b.append(T(tx + cw_[i] / 2, ry + 36, [L], 24, INK, weight="700", anchor="middle"))
            elif i < 4:
                b.append(T(tx + 30, ry + 36, ["sí"], 17, GRAY)); b.append(checkbox(tx + 66, ry + 16, s=10))
                b.append(T(tx + 130, ry + 36, ["no"], 17, GRAY)); b.append(checkbox(tx + 170, ry + 16, s=10))
            else:
                b.append(T(tx + 14, ry + 36, ["culpable / absuelta"], 14, GRAY))
            tx += cw_[i]
    fy = yy + 78 + 4 * 62 + 40
    b.append(rect(x, fy, w - 20, 120, AMBER_BG, r=14, stroke=AMBER_LN, sw=2))
    b.append(T(x + 20, fy + 42, ["Mi fórmula para 12 meses, escrita por mí antes de mirar la absuelta:"], 19, AMBER_D, weight="700"))
    b.append(T(x + 20, fy + 96, ["V  =  1.000.000  ×  ( ________ ) ^ ____"], 30, INK))
    b.append(T(x, fy + 160, ["Si tu fórmula y la absuelta no coinciden, una de las dos está mal. Averigua cuál antes de marcar."], 18, GRAY, style="italic"))
    ty2 = fy + 200
    b.append(rect(x, ty2, w - 20, 130, SOFT, r=14))
    b.append(T(x + 20, ty2 + 40, ["Transferencia — sin mirar las opciones:  ¿y para 24 meses?   V = 1.000.000 × ( ______ ) ^ ____"], 19, INK))
    b.append(T(x + 20, ty2 + 86, ["¿y si la tasa fuera 3 %?   V = 1.000.000 × ( ______ ) ^ 12        ¿qué cambia y qué no?"], 19, INK))


def inst_q9(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "El cazador de afirmaciones", EDU_ROJO,
                      "La gráfica no es una línea: sube, baja y vuelve a subir. Primero córtala en tramos; después pon a prueba cada afirmación contra tus tramos.")
    b.append(T(x, yy + 24, ["Mis tramos (del día ___ al día ___ , sube o baja):"], 20, INK))
    for i in range(4):
        bx = x + i * 310
        b.append(rect(bx, yy + 40, 290, 110, "white", r=12, stroke=EDU_ROJO, sw=2))
        b.append(T(bx + 16, yy + 72, ["del día ____ al ____"], 18, GRAY))
        b.append(T(bx + 16, yy + 118, ["↑ sube"], 19, INK)); b.append(checkbox(bx + 110, yy + 100, s=10))
        b.append(T(bx + 160, yy + 118, ["↓ baja"], 19, INK)); b.append(checkbox(bx + 250, yy + 100, s=10))
    yy += 190
    b.append(T(x, yy + 24, ["Cada afirmación pasa por dos filtros. Si cae en uno, táchala:"], 20, INK))
    hdr = ["", "¿Dice «siempre», «nunca», «todo el mes»?", "¿Contradice alguno de mis tramos?", "Queda"]
    cw_ = [90, 480, 460, 200]
    tx = x
    for i, c_ in enumerate(hdr):
        if c_:
            b.append(rect(tx, yy + 44, cw_[i] - 6, 44, EDU_ROJO, r=8)); b.append(T(tx + 12, yy + 73, [c_], 16, "white", weight="700"))
        tx += cw_[i]
    for r, L in enumerate("ABCD"):
        ry = yy + 96 + r * 58; tx = x
        for i in range(4):
            b.append(rect(tx, ry, cw_[i] - 6, 50, SOFT if i == 0 else "white", r=8, stroke=AZm_L, sw=1.6))
            if i == 0: b.append(T(tx + cw_[i] / 2, ry + 34, [L], 22, INK, weight="700", anchor="middle"))
            elif i < 3:
                b.append(T(tx + 24, ry + 34, ["sí → ✗"], 17, EDU_ROJO)); b.append(checkbox(tx + 110, ry + 14, s=10, c=EDU_ROJO))
                b.append(T(tx + 180, ry + 34, ["no"], 17, GRAY)); b.append(checkbox(tx + 220, ry + 14, s=10))
            else:
                b.append(checkbox(tx + 80, ry + 14, s=11, c=EDU_VERDE))
            tx += cw_[i]
    b.append(T(x, yy + 96 + 4 * 58 + 36, ["Si quedan dos, vuelve a los tramos: una de las dos exagera. La correcta dice exactamente lo que se ve, ni más ni menos."], 18, GRAY, style="italic"))
    ey = yy + 96 + 4 * 58 + 70
    b.append(rect(x, ey, w - 20, 170, SOFT, r=14))
    b.append(T(x + 20, ey + 38, ["Con mis palabras, en una frase: ¿qué hace el consumo de Valeria a lo largo del mes?"], 19, AZm, weight="700"))
    b.append(wlines(x + 20, ey + 90, w - 60, 2, c="#D8DEE6", step=46))
    b.append(T(x + 20, ey + 160, ["(si tu frase se parece a una opción, esa es la candidata)"], 16, GRAY, style="italic"))


def inst_q10(b, x, y, w, h):
    yy = titulo_instr(b, x, y, "Las dos mitades", EDU_ROJO,
                      "El consumo total de un tramo es el área bajo la curva en ese tramo. No hace falta calcularla: basta comparar dos rectángulos aproximados.")
    for i, (nm, dias, c) in enumerate([("PRIMERA MITAD", "días 5 a 15", EDU_AZUL), ("SEGUNDA MITAD", "días 15 a 25", EDU_ROJO)]):
        bx = x + i * 630
        b.append(rect(bx, yy + 10, 600, 300, "white", r=14, stroke=c, sw=2.4))
        b.append(T(bx + 20, yy + 48, [nm], 20, c, weight="700", ls=2)); b.append(T(bx + 260, yy + 48, [dias], 18, GRAY))
        # rectángulo sombreado
        rh = 110 if i == 0 else 200
        b.append(rect(bx + 30, yy + 290 - rh, 240, rh, c, r=4, op=0.15))
        b.append(rect(bx + 30, yy + 290 - rh, 240, rh, "none", r=4, stroke=c, sw=2, dash="6,5"))
        b.append(T(bx + 150, yy + 290 - rh - 10, ["altura típica"], 15, GRAY, anchor="middle"))
        b.append(T(bx + 300, yy + 110, ["altura típica (kWh/día):  ____"], 19, INK))
        b.append(T(bx + 300, yy + 160, ["× días del tramo:  ____"], 19, INK))
        b.append(line(bx + 300, yy + 184, bx + 580, yy + 184, INK, 1.6))
        b.append(T(bx + 300, yy + 226, ["≈ consumo del tramo:  ________"], 20, INK, weight="700"))
        b.append(T(bx + 300, yy + 270, ["(mira la gráfica: ¿la curva está alta o baja?)"], 15, GRAY, style="italic"))
    vy = yy + 350
    b.append(rect(x, vy, w - 20, 120, AMBER_BG, r=14, stroke=AMBER_LN, sw=2))
    b.append(T(x + 20, vy + 42, ["¿Cuál rectángulo es más grande?  ________________    Entonces el consumo total fue mayor en la ______________ mitad."], 19, AMBER_D, weight="700"))
    b.append(T(x + 20, vy + 90, ["Ahora sí: la afirmación correcta es la que diga eso. Las que hablen de un solo día o de «siempre», se tachan."], 18, INK))
    cuenta(b, x, vy + 150, w - 20, 180, "mis cuentas · o un dibujo de la gráfica con los dos rectángulos encima")


INST = {1: inst_q1, 2: inst_q2, 3: inst_q3, 4: inst_q4, 5: inst_q5, 6: inst_q6, 7: inst_q7, 8: inst_q8, 9: inst_q9, 10: inst_q10}


def build(qs, pages=(11, 13, 15, 16, 18)):
    pares = [(qs[i], qs[i + 1]) for i in range(0, 10, 2)]
    files = []
    for k, (qa, qb) in enumerate(pares):
        pag = pages[k]
        b = svg_open()
        hoja_header(b, pag, f"Taller · hoja {k+1} de 5 · preguntas {qa['n']} y {qb['n']}")
        bloque(b, 210, qa, INST[qa["n"]])
        bloque(b, 210 + BLK_H + 40, qb, INST[qb["n"]])
        footer(b, pag, AZm, texto="Matemáticas · Momento 1 · taller")
        f = OUT + f"m1_t{k+1}.svg"; svg_close(b, f); files.append(f)
    return files


if __name__ == "__main__":
    import json
    qs = json.load(open("/home/claude/cuaderno/libro_q.json"))
    for q in qs: q["n"] = int(q["n"]); q["est"] = int(q["est"])
    build(qs)
    print("ok taller M1")
