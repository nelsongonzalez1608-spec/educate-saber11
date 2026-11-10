#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hojas 4-10: metas, qué te vas a encontrar, psicología, portada de Matemáticas."""
import math, random
from lib import *
from taller_base import salvavidas, SALV_D   # el salvavidas nuevo (flotador coral), igual en todas las áreas

random.seed(31)
OUT = "/home/claude/libro/"
CARRERAS = [  # referencia periodística 2026 (El Universal) — rango aproximado de puntaje global
    ("Medicina", 420, 469), ("Ingeniería civil", 370, 455), ("Biología", 311, 458), ("Derecho", 347, 448),
    ("Odontología", 360, 437), ("Ingeniería química", 358, 428), ("Enfermería", 331, 425),
    ("Ingeniería de sistemas", 371, 422), ("Administración de empresas", 331, 420), ("Matemáticas", 284, 415),
    ("Química farmacéutica", 328, 410), ("Lic. en educación", 297, 399), ("Lenguas extranjeras", 347, 398),
    ("Economía", 317, 394), ("Comunicación social", 320, 385), ("Trabajo social", 301, 382),
    ("Contaduría pública", 302, 378), ("Nutrición y dietética", 320, 360),
]


# ═════════════════════════════ 4 · METAS (1): la escala ═════════════════════════════
def metas_1():
    b = svg_open()
    y = frame(b, "Metas", EDU_ORO, 4, "¿para qué estoy entrenando?")
    y = titulo(b, y + 20, "Ponle un número a tu meta", EDU_ORO,
               sub="El Saber 11 se califica de 0 a 500 en el puntaje global y de 0 a 100 en cada área. "
                   "Una meta sin número no se puede entrenar.")
    top = y + 10

    # ── escalera a la izquierda ──
    LX, LW = M, 1000
    b.append(rect(LX, top, LW, 1250, SOFT, r=26))
    b.append(T(LX + 40, top + 56, ["La escala del puntaje global"], 32, EDU_AZUL, weight="700"))
    ax = LX + 130; y0 = top + 1160; y1 = top + 130      # eje: 0 abajo, 500 arriba
    b.append(line(ax, y0, ax, y1, EDU_AZUL, 6))
    def yv(v): return y0 - (y0 - y1) * v / 500
    for v in range(0, 501, 50):
        b.append(line(ax - 14, yv(v), ax + 14, yv(v), EDU_AZUL, 3))
        b.append(T(ax - 28, yv(v) + 9, [str(v)], 22, GRAY, anchor="end"))
    marcas = [(250, "Promedio nacional aproximado", "la mitad de los estudiantes queda por debajo", GRAY),
              (300, "Corte de admisión en universidades privadas", "p. ej. Universidad de los Andes 2026-2: 300 a 320", EDU_AZUL),
              (350, "Becas y oportunidades", "desde aquí se abren becas, créditos condonables y cupos que no dependen de pagar", EDU_VERDE),
              (420, "Carreras más exigidas", "Medicina, Ingeniería civil, Derecho en universidades top", EDU_ROJO)]
    for v, t, d, c in marcas:
        yy = yv(v)
        b.append(line(ax + 16, yy, ax + 70, yy, c, 3, "6,6"))
        b.append(f'<circle cx="{ax+78}" cy="{yy}" r="10" fill="{c}"/>')
        b.append(T(ax + 100, yy - 6, [f"{v}  ·  {t}"], 27, c, weight="700"))
        b.append(T(ax + 100, yy + 28, [d], 22, GRAY, style="italic"))
    # marcas del estudiante
    for lab, c, dy in [("HOY", EDU_ORO, 0), ("META", EDU_AZUL, 0)]:
        pass
    b.append(rect(LX + 560, top + 960, 400, 230, "white", r=18, stroke=EDU_ORO, sw=2.5, dash="8,6"))
    b.append(T(LX + 584, top + 1004, ["Marca con lápiz sobre la escala:"], 22, EDU_ORO, weight="700"))
    b.append(spath([(LX + 592, top + 1052), (LX + 640, top + 1052)], EDU_ORO, 5))
    b.append(T(LX + 660, top + 1060, ["HOY · tu primer simulacro"], 22, INK))
    b.append(spath([(LX + 592, top + 1108), (LX + 640, top + 1108)], EDU_AZUL, 5))
    b.append(T(LX + 660, top + 1116, ["META · el puntaje que necesitas"], 22, INK))
    b.append(T(LX + 584, top + 1162, ["Entre las dos rayas está tu trabajo."], 21, GRAY, style="italic"))

    # ── tabla a la derecha ──
    RX = LX + LW + 40; RW = W - M - RX
    b.append(rect(RX, top, RW, 1250, "white", r=26, stroke=EDU_ORO, sw=3))
    b.append(T(RX + 36, top + 56, ["Puntaje global de referencia"], 30, EDU_ORO, weight="700"))
    b.append(T(RX + 36, top + 90, ["por carrera · rango aproximado reportado en 2026"], 21, GRAY, style="italic"))
    yy = top + 140
    for i, (nm, lo, hi) in enumerate(CARRERAS):
        if i % 2: b.append(rect(RX + 20, yy - 28, RW - 40, 50, SOFT, r=8))
        b.append(T(RX + 36, yy + 8, [nm], 24, INK))
        # barra de rango
        bx0, bx1 = RX + 430, RX + RW - 110
        def px(v): return bx0 + (bx1 - bx0) * (v - 250) / 250
        b.append(line(px(250), yy, px(500), yy, "#E6EAF0", 8))
        b.append(line(px(lo), yy, px(hi), yy, EDU_ORO, 8))
        b.append(T(RX + RW - 36, yy + 8, [f"{lo}–{hi}"], 21, GRAY, anchor="end"))
        yy += 54
    b.append(T(RX + 36, top + 1190, ["Son referencias de prensa, no cortes oficiales. Cada universidad fija el suyo:"], 19, GRAY, style="italic"))
    b.append(T(RX + 36, top + 1218, ["confírmalo en la página de admisiones de la que tú quieres."], 19, GRAY, style="italic"))

    # ── mi cuenta ──
    y = top + 1250 + 60
    b.append(rect(M, y, CW, 560, CREMA, r=26))
    b.append(T(M + 40, y + 60, ["Mi cuenta"], 36, EDU_AZUL, weight="700"))
    b.append(T(M + 230, y + 60, ["— la escribes ahora y la vuelves a mirar después de cada simulacro"], 23, GRAY, style="italic"))
    campos = [("La carrera que quiero", 560), ("En la universidad", 560), ("Puntaje que necesito", 300)]
    xx = M + 40
    for lab, w_ in campos:
        b.append(T(xx, y + 130, [lab], 23, EDU_AZUL, weight="700"))
        b.append(line(xx, y + 190, xx + w_, y + 190, LGRAY, 2.6))
        xx += w_ + 60
    # operación
    oy = y + 300
    cajas = [("Puntaje que necesito", EDU_AZUL), ("−", None), ("Mi puntaje hoy", EDU_ORO), ("=", None),
             ("Lo que me falta", EDU_ROJO), ("÷", None), ("Semanas que faltan", GRAY), ("=", None), ("Puntos por semana", EDU_VERDE)]
    xx = M + 40; bw = 290
    for lab, c in cajas:
        if c is None:
            b.append(T(xx + 30, oy + 80, [lab], 54, EDU_AZUL, weight="700", anchor="middle")); xx += 60
        else:
            b.append(rect(xx, oy, bw, 120, "white", r=16, stroke=c, sw=3))
            b.append(T(xx + bw / 2, oy + 150, [lab], 20, c, weight="700", anchor="middle")); xx += bw + 10
    b.append(PT(M + 60, y + 520, ["Si el número de puntos por semana te asusta, bien: ya sabes cuánto vale cada sábado."], 30, EDU_AZUL, rot=-0.6))
    footer(b, 4, EDU_ORO)
    svg_close(b, OUT + "ap04_metas1.svg")


# ═════════════════════════════ 5 · METAS (2): tablero WOOP ═════════════════════════════
def metas_2():
    b = svg_open()
    y = frame(b, "Metas", EDU_ORO, 5, "mi tablero de metas")
    y = titulo(b, y + 20, "Mi tablero de metas", EDU_ORO,
               sub="Imaginar el resultado no basta: la investigación de Gabriele Oettingen muestra que la meta se mueve "
                   "cuando también nombras tu obstáculo y decides el plan. Cuatro casillas, en este orden.")
    top = y + 10
    pw = (CW - 40) / 2; ph = 700
    paneles = [
        ("1 · DESEO", EDU_AZUL, "Lo que quiero lograr con esta prueba, en una frase que me importe de verdad.",
         "lines", "happy"),
        ("2 · RESULTADO", EDU_VERDE, "El día que lo logro: ¿dónde estoy, con quién, qué siento? Dibújalo o escríbelo. Pega una foto si quieres.",
         "draw", "proud"),
        ("3 · OBSTÁCULO", EDU_ROJO, "Lo que está en MÍ que me lo puede impedir. No el profe, no el colegio, no el tiempo: yo.",
         "lines", "worried"),
        ("4 · PLAN", EDU_ORO, "Cuando aparezca el obstáculo, esto es lo que voy a hacer. Escríbelo como «si… entonces…».",
         "ifthen", "determined"),
    ]
    for i, (t, c, d, kind, mood) in enumerate(paneles):
        x = M + (i % 2) * (pw + 40); yy = top + (i // 2) * (ph + 60)
        panel(b, x, yy + 20, pw, ph, c, title=t, title_size=26)
        parrafo_j(b, x + 36, yy + 70, d, pw - 200, 25, color=GRAY, lh=34)
        b.append(face(x + pw - 70, yy + 90, 44, mood, c))
        iy = yy + 200
        if kind == "lines":
            b.append(wlines(x + 36, iy + 40, pw - 72, 9, c="#E3E8EF", step=52))
        elif kind == "draw":
            b.append(rect(x + 36, iy, pw - 72, 470, "white", r=14, stroke="#E3E8EF", sw=2))
            b.append(dots(x + 60, iy + 30, c, r=2.2, step=34, cols=int((pw - 120) // 34), rows=13, op=0.22))
            b.append(PT(x + pw - 60, iy + 450, ["dibuja aquí"], 26, c, rot=-2, anchor="end", op=0.7))
        else:
            for k in range(3):
                ky = iy + k * 150
                b.append(T(x + 36, ky + 30, ["Si"], 30, c, weight="700"))
                b.append(line(x + 90, ky + 36, x + pw - 40, ky + 36, "#CFD6E0", 2.4))
                b.append(T(x + 36, ky + 92, ["entonces yo"], 30, c, weight="700"))
                b.append(line(x + 230, ky + 98, x + pw - 40, ky + 98, "#CFD6E0", 2.4))
    y = top + 2 * (ph + 60) + 20

    # puntaje por área: hoy y meta
    b.append(rect(M, y, CW, 380, SOFT, r=26))
    b.append(T(M + 40, y + 56, ["Mi puntaje por área · hoy y meta"], 32, EDU_AZUL, weight="700"))
    b.append(T(M + 620, y + 56, ["(de 0 a 100 cada una; lo llenas con tu primer simulacro)"], 22, GRAY, style="italic"))
    n_ar = len(AREAS)
    gw = (CW - 80 - (n_ar - 1) * 20) / n_ar
    # En la prueba, Biología, Química y Física dan un solo puntaje: Ciencias Naturales.
    cien = [i for i, (nm, _) in enumerate(AREAS) if nm in ("Biología", "Química", "Física")]
    cx0 = M + 40 + cien[0] * (gw + 20); cx1 = M + 40 + cien[-1] * (gw + 20) + gw
    b.append(T((cx0 + cx1) / 2, y + 116, ["en la prueba son una sola: Ciencias Naturales, con un solo puntaje"],
               19, GRAY, style="italic", anchor="middle"))
    for i, (nm, c) in enumerate(AREAS):
        x = M + 40 + i * (gw + 20); yy = y + 150
        b.append(rect(x, yy, gw, 190, "white", r=16, stroke=c, sw=2.4))
        b.append(rect(x, yy, gw, 60, c, r=16)); b.append(rect(x, yy + 30, gw, 30, c, r=0))
        ls_ = wrap(nm, 14)
        for j, ln in enumerate(ls_):
            b.append(T(x + gw / 2, yy + (36 if len(ls_) == 1 else 26 + j * 24), [ln], 19, "white", weight="700", anchor="middle"))
        b.append(T(x + 24, yy + 96, ["hoy"], 21, GRAY)); b.append(line(x + 80, yy + 100, x + gw - 24, yy + 100, LGRAY, 2.4))
        b.append(T(x + 24, yy + 156, ["meta"], 21, c, weight="700")); b.append(line(x + 80, yy + 160, x + gw - 24, yy + 160, c, 2.4))
    footer(b, 5, EDU_ORO)
    svg_close(b, OUT + "ap05_metas2.svg")


# ═════════════════════════════ 6 · QUÉ VAS A ENCONTRAR (1): anatomía de la hoja ═════════════════════════════
def encontrar_1():
    b = svg_open()
    y = frame(b, "Qué te vas a encontrar", EDU_VERDE, 6, "así se lee una hoja de trabajo")
    y = titulo(b, y + 20, "Así se lee una hoja", EDU_VERDE,
               sub="Todas las hojas del cuaderno, en las siete áreas, tienen las mismas partes. Apréndetelas una vez.")
    top = y + 20
    # ── maqueta de hoja a la izquierda ──
    HX, HW, HH = M, 880, 1760
    b.append(rect(HX, top, HW, HH, "white", r=18, stroke="#C9D2DC", sw=3))
    pad = 36; c_area = "#1F4E8C"
    # encabezado
    b.append(rect(HX + pad, top + 30, HW - 2 * pad, 120, SOFT, r=12, stroke="#DDE3EA", sw=2))
    b.append(logo(HX + pad + 18, top + 58, 58))
    b.append(T(HX + pad + 210, top + 70, ["COMPETENCIAS"], 15, GRAY, weight="700", ls=1))
    for k, cc in enumerate([c_area, CORAL, AZ_M]):
        b.append(f'<circle cx="{HX+pad+226+k*46}" cy="{top+106}" r="12" fill="{cc}"/>')
    b.append(rect(HX + pad + 400, top + 54, 400, 72, "white", r=10, stroke=TEAL, sw=2))
    b.append(T(HX + pad + 420, top + 86, ["NUMÉRICO-VARIACIONAL"], 17, AZ_D, weight="700"))
    b.append(T(HX + pad + 420, top + 110, ["Misión 1 · Momento 1 · Estrategia 3"], 15, GRAY))
    # pregunta
    qy = top + 190
    b.append(rect(HX + pad, qy, 70, 70, c_area, r=12)); b.append(T(HX + pad + 35, qy + 48, ["7"], 34, "white", weight="700", anchor="middle"))
    b.append(T(HX + pad + 90, qy + 30, ["Pregunta 7 del libro · página 278"], 20, c_area, weight="700"))
    b.append(T(HX + pad + 90, qy + 58, ["Estrategia 3 · El crecimiento que se acumula"], 18, GRAY))
    # piensa en esto
    py = qy + 110
    b.append(rect(HX + pad, py, HW - 2 * pad, 210, AMBER_BG, r=12, stroke=AMBER_LN, sw=2))
    b.append(T(HX + pad + 20, py + 38, ["PIENSA EN ESTO"], 18, AMBER_D, weight="700", ls=1))
    for k, ln in enumerate(["¿La cantidad sube siempre lo mismo, o sube cada vez más?", "¿Qué número se repite en cada paso?", "Antes de calcular: ¿qué tipo de gráfica esperas?"]):
        b.append(f'<circle cx="{HX+pad+28}" cy="{py+78+k*44}" r="5" fill="{AMBER_D}"/>')
        b.append(T(HX + pad + 46, py + 84 + k * 44, [ln], 19, INK))
    # paso a paso + cuadrícula
    sy = py + 250
    SH = 520   # alto del paso a paso y la cuadrícula (cedió 80 px al salvavidas nuevo, que es más alto)
    b.append(rect(HX + pad, sy, 360, SH, "white", r=12, stroke=AZ_LN, sw=2))
    b.append(T(HX + pad + 20, sy + 38, ["PASO A PASO"], 18, AZ_D, weight="700", ls=1))
    pasos = ["Escribo el valor inicial.", "Calculo el cambio de un paso al siguiente.", "Reviso si el cambio es fijo o crece.", "Elijo la opción que lo muestre."]
    for k, ln in enumerate(pasos):
        yy = sy + 96 + k * 112
        b.append(checkbox(HX + pad + 20, yy - 20, s=11, c=AZ_D))
        for j, l2 in enumerate(wrap(ln, 22)):
            b.append(T(HX + pad + 56, yy + j * 24, [l2], 18, INK))
    b.append(grid_box(HX + pad + 380, sy, HW - 2 * pad - 380, SH, step=28))
    b.append(T(HX + pad + 400, sy + 36, ["CUADRÍCULA DE TRABAJO"], 16, AZ_M, weight="700", ls=1))
    b.append(PT(HX + pad + 420, sy + 120, ["4  6  8  10  12", "+2 +2 +2 +2", "sube siempre lo mismo", "→ es lineal"], 27, PENCIL, rot=-1, lh=44))
    # marca tu respuesta
    ry = sy + SH + 40
    b.append(T(HX + pad, ry + 30, ["MARCO AL FINAL:"], 18, AZ_D, weight="700", ls=1))
    for k, L in enumerate("ABCD"):
        cx = HX + pad + 260 + k * 90
        b.append(f'<circle cx="{cx}" cy="{ry+22}" r="24" fill="white" stroke="{AZ_D}" stroke-width="2.4"/>')
        b.append(T(cx, ry + 31, [L], 22, AZ_D, weight="700", anchor="middle"))
    b.append(ring(HX + pad + 260 + 2 * 90, ry + 22, r=27))
    # salvavidas: el mismo de todas las hojas (taller_base.salvavidas)
    vy = ry + 90; VH = 300
    salvavidas(b, HX + pad, vy, HW - 2 * pad, h=VH)
    # bitácora
    by = vy + VH + 40
    b.append(rect(HX + pad, by, HW - 2 * pad, 170, SOFT, r=12, stroke="#DDE3EA", sw=2))
    b.append(T(HX + pad + 20, by + 40, ["BITÁCORA DE LA CLASE"], 18, GRAY, weight="700", ls=1))
    b.append(T(HX + pad + 20, by + 82, ["Hoy entendí ________________   ·   Todavía no entiendo ________________"], 16, GRAY))
    b.append(T(HX + pad + 20, by + 118, ["La próxima vez voy a ________________"], 16, GRAY))

    # ── llamadas a la derecha (anclas separadas ≥ 150 px) ──
    CX = HX + HW + 70
    notas = [
        (top + 90, "El encabezado", "Qué competencia y qué componente del ICFES estás entrenando. Es lo que mide la prueba.", EDU_AZUL),
        (qy + 35, "La pregunta no está reimpresa", "La lees en tu libro. El cuaderno te dice la página y la estrategia con que se resuelve.", EDU_AZUL),
        (py + 105, "Piensa en esto", "Preguntas para mirar lo importante ANTES de calcular. Si las respondes en tu cabeza, medio camino está hecho.", AMBER_D),
        (sy + 170, "Paso a paso", "La ruta. Tachas cada paso cuando lo hagas. Si te saltas uno, ahí suele estar el error.", AZ_D),
        (sy + 400, "La cuadrícula", "Aquí va TODO lo que pienses: números, tablas, un dibujo, una flecha. Nada se hace «en la cabeza».", AZ_M),
        (ry + 22, "Marcas al final", "La letra es lo último que escribes. Sin cuadrícula, la hoja no está resuelta.", EDU_ROJO),
        (vy + 120, "Salvavidas", "Cuando te bloqueas: escribe lo poco que sí tenías claro, qué tenía que ser entonces y qué opción no podía ser. De ahí se sale.", SALV_D),
        (by + 85, "Bitácora", "Una vez por clase, siempre. Es lo que lee la coordinación para saber cómo vas.", GRAY),
    ]
    for (ay, t, d, c) in notas:
        b.append(hand_arrow(CX + 10, ay, HX + HW - 10, ay, c, sw=3.6, bend=0.12, head=20))
        b.append(T(CX + 40, ay - 14, [t], 27, c, weight="700"))
        yy = ay + 16
        for ln in wrap(d, 50):
            b.append(T(CX + 40, yy + 22, [ln], 21, INK)); yy += 28
    # cierre: lo que cambia y lo que no
    cy_ = top + HH + 60
    b.append(rect(M, cy_, CW, 250, CREMA, r=26))
    b.append(T(M + 40, cy_ + 60, ["En cada área cambia el color y el instrumento de pensamiento. Las ocho partes de la hoja, nunca."], 27, EDU_AZUL, weight="700"))
    n_ar = len(AREAS)
    gw = (CW - 80 - (n_ar - 1) * 20) / n_ar
    for i, (nm, c) in enumerate(AREAS):
        x = M + 40 + i * (gw + 20)
        b.append(rect(x, cy_ + 110, gw, 100, "white", r=16, stroke=c, sw=2.6))
        b.append(rect(x, cy_ + 110, 16, 100, c, r=8))
        ls_ = [" ".join(l) for l in wrap_px(nm, 21, gw - 56, "700")]
        for j, ln in enumerate(ls_):
            b.append(T(x + 36, cy_ + (168 if len(ls_) == 1 else 152 + j * 30), [ln], 21, c, weight="700"))
    footer(b, 6, EDU_VERDE)
    svg_close(b, OUT + "ap06_encontrar1.svg")


# ═════════════════════════════ 7 · QUÉ VAS A ENCONTRAR (2): momentos, clase y criticidad ═════════════════════════════
def encontrar_2():
    b = svg_open()
    y = frame(b, "Qué te vas a encontrar", EDU_VERDE, 7, "cómo está organizada cada área")
    y = titulo(b, y + 20, "Seis momentos, ocho clases, un nivel más", EDU_VERDE)
    top = y

    # momentos
    b.append(rect(M, top, CW, 430, SOFT, r=26))
    b.append(T(M + 40, top + 56, ["Cada área tiene 6 momentos"], 34, EDU_AZUL, weight="700"))
    parrafo_j(b, M + 40, top + 76, "Un momento es un taller de 10 preguntas de tu libro, más entrenamiento con preguntas tipo Saber 11 "
            "y un simulacro. Un momento no cabe en una clase: tu profesor lo reparte en el ritmo del grupo, en las 8 clases del área.",
            CW - 80, 24, color=GRAY, lh=34)
    gw = (CW - 80 - 5 * 26) / 6
    for i in range(6):
        x = M + 40 + i * (gw + 26); yy = top + 200
        b.append(rect(x, yy, gw, 180, "white", r=18, stroke=EDU_AZUL, sw=2.4))
        b.append(num_badge(x + 44, yy + 44, i + 1, EDU_AZUL, r=28, size=28))
        b.append(T(x + 86, yy + 54, ["Momento"], 22, EDU_AZUL, weight="700"))
        for k, (ic, lab) in enumerate([("📘", "10 preguntas del libro"), ("✔", "entrenamiento ICFES"), ("⏱", "simulacro")]):
            b.append(f'<circle cx="{x+30}" cy="{yy+98+k*30}" r="5" fill="{[EDU_ROJO, EDU_VERDE, EDU_ORO][k]}"/>')
            b.append(T(x + 46, yy + 104 + k * 30, [lab], 19, INK))
        if i < 5: b.append(hand_arrow(x + gw + 2, yy + 90, x + gw + 24, yy + 90, EDU_ORO, sw=3, bend=0, head=14))
    y = top + 470

    # una clase por dentro
    b.append(rect(M, y, CW, 560, "white", r=26, stroke=EDU_VERDE, sw=3))
    b.append(T(M + 40, y + 56, ["Una clase por dentro · 120 minutos"], 34, EDU_VERDE, weight="700"))
    b.append(T(M + 700, y + 56, ["siempre los mismos seis pasos, en cualquier área"], 23, GRAY, style="italic"))
    pasos = [("Activación", 15, "una tabla, una pregunta, cuaderno cerrado", EDU_AZUL),
             ("Pregunta problematizadora", 20, "el reto del momento: cada uno dice su hipótesis", EDU_ROJO),
             ("Desarrollo guiado", 35, "las preguntas del libro, con la estrategia", EDU_VERDE),
             ("Reto en equipo", 20, "una situación por equipo; registro individual", EDU_ORO),
             ("Evaluación individual", 20, "preguntas tipo Saber 11, en silencio", "#5B3E96"),
             ("Cierre", 10, "bitácora y salvavidas", TEAL)]
    bx = M + 40; bw_total = CW - 80; by = y + 110
    xx = bx
    for nm, mn, d, c in pasos:
        w_ = bw_total * mn / 120
        b.append(rect(xx, by, w_ - 6, 70, c, r=12))
        b.append(T(xx + (w_ - 6) / 2, by + 44, [f"{mn}'"], 24, "white", weight="700", anchor="middle"))
        xx += w_
    xx = bx
    for k, (nm, mn, d, c) in enumerate(pasos):
        w_ = bw_total * mn / 120
        yy = by + 110 + (k % 2) * 150
        b.append(line(xx + 14, by + 70, xx + 14, yy - 10, c, 2, "5,5"))
        b.append(f'<circle cx="{xx+14}" cy="{yy-10}" r="7" fill="{c}"/>')
        b.append(T(xx + 30, yy, [nm], 23, c, weight="700"))
        for j, ln in enumerate(wrap(d, 26)):
            b.append(T(xx + 30, yy + 30 + j * 26, [ln], 19, INK))
        xx += w_
    y += 600

    # criticidad
    b.append(rect(M, y, CW, 700, CREMA, r=26))
    b.append(T(M + 40, y + 56, ["Cómo subes de nivel · lo que el ICFES llama niveles de desempeño"], 34, EDU_ORO, weight="700"))
    niveles = [("1", "Insuficiente", "Marco sin leer todo. Adivino.", EDU_ROJO),
               ("2", "Mínimo", "Entiendo la pregunta, pero no sé qué hacer con los datos.", EDU_ORO),
               ("3", "Satisfactorio", "Sé el camino y lo ejecuto hasta la respuesta.", EDU_VERDE),
               ("4", "Avanzado", "Puedo explicar por qué las otras opciones están mal.", EDU_AZUL)]
    sx = M + 60; sw_ = 400; sh = 100
    for k, (n, nm, d, c) in enumerate(niveles):
        x = sx + k * (sw_ + 20); h = sh + k * 90; yy = y + 560 - h
        b.append(rect(x, yy, sw_, h, c, r=16))
        b.append(T(x + 24, yy + 46, [f"Nivel {n} · {nm}"], 24, "white", weight="700"))
        for j, ln in enumerate(wrap(d, 34)):
            b.append(T(x + 24, yy + 82 + j * 26, [ln], 19, "white", op=0.92))
    b.append(hand_arrow(sx + 60, y + 600, sx + 4 * (sw_ + 20) - 80, y + 600, EDU_ORO, sw=5, bend=0, head=26))
    b.append(PT(sx + 2 * (sw_ + 20), y + 650, ["cada hoja resuelta con andamiaje es un escalón"], 30, EDU_ORO, rot=-0.8, anchor="middle"))
    # membrete de las preguntas de entrenamiento (franja propia) · regla 7, Nelson 10 nov:
    # «Pregunta Saber 11», sin «oficial» ni «real» (varias vienen del ASED, no del ICFES)
    y += 740
    b.append(rect(M, y, CW, 190, "white", r=26, stroke=EDU_AZUL, sw=3))
    b.append(rect(M + 40, y + 50, 560, 90, SOFT, r=14, stroke=AZ_LN, sw=2))
    b.append(T(M + 70, y + 106, ["Pregunta Saber 11"], 26, AZ_D, weight="700"))
    b.append(T(M + 640, y + 80, ["Cuando veas este membrete, la pregunta tiene la forma y el nivel del Saber 11."], 24, INK))
    b.append(T(M + 640, y + 116, ["Es el formato de la prueba de verdad: lo entrenas aquí para que ese día nada te sorprenda."], 24, INK))
    b.append(hand_arrow(M + 620, y + 95, M + 605, y + 95, EDU_ORO, sw=3, bend=0, head=0))
    footer(b, 7, EDU_VERDE)
    svg_close(b, OUT + "ap07_encontrar2.svg")


if __name__ == "__main__":
    metas_1(); metas_2(); encontrar_1(); encontrar_2()
    print("ok 4-7")
