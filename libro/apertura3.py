#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hojas 8-10: la psicología de la meta (estudiante, coordinadores) y las portadas de área (10, 53, 96)."""
import math, random
from lib import *

random.seed(41)
OUT = "/home/claude/libro/"
PSI = "#5B3E96"   # violeta de la sección psicológica


# ═════════════════════════════ 8 · PSICOLOGÍA (estudiante) ═════════════════════════════
def psico_1():
    b = svg_open()
    y = frame(b, "La psicología de la meta", PSI, 8, "lo que pasa en tu cabeza antes de una pregunta difícil")
    y = titulo(b, y + 20, "Lo que pasa en tu cabeza", PSI,
               sub="Todos sentimos esto frente a una pregunta difícil. La diferencia no es sentirlo o no: es saber qué hacer cuando llega.")
    top = y + 10
    estados = [
        ("Bloqueo", "«No entiendo nada.»", "Lee la pregunta otra vez, despacio, y subraya el único dato que sí entiendes. Empieza por ahí.", "worried", EDU_AZUL),
        ("Prisa", "«Ya sé, es la B.»", "Puede ser. Escribe un solo paso en la cuadrícula antes de marcar. Si el paso aguanta, marca.", "determined", EDU_ROJO),
        ("Pánico", "«No me va a dar el tiempo.»", "Salta la pregunta, márcala con una bandera y sigue. Vuelves al final. Una pregunta no vale el examen.", "surprised", EDU_ORO),
        ("Cansancio", "«Ya no más.»", "Cierra con la bitácora, no con una pregunta a medias. Dejar escrito dónde quedaste también es avanzar.", "tired", EDU_VERDE),
    ]
    cw_ = (CW - 3 * 30) / 4
    for i, (nm, frase, que, mood, c) in enumerate(estados):
        x = M + i * (cw_ + 30)
        b.append(rect(x, top, cw_, 620, "white", r=26, stroke=c, sw=3))
        b.append(face(x + cw_ / 2, top + 110, 76, mood, c))
        b.append(T(x + cw_ / 2, top + 236, [nm], 32, c, weight="700", anchor="middle"))
        b.append(PT(x + cw_ / 2, top + 290, [frase], 30, PENCIL, rot=-1.5, anchor="middle"))
        b.append(line(x + 40, top + 320, x + cw_ - 40, top + 320, c, 2, "6,6"))
        b.append(T(x + 40, top + 356, ["QUÉ HACER"], 17, c, weight="700", ls=2))
        parrafo_j(b, x + 40, top + 372, que, cw_ - 80, 22, lh=32)
    y = top + 680

    # el error es un dato
    b.append(rect(M, y, CW, 470, CREMA, r=26))
    b.append(T(M + 40, y + 62, ["El error no es una nota. Es un dato."], 38, EDU_AZUL, weight="700"))
    parrafo_j(b, M + 40, y + 86, "Cuando te equivoques — y te vas a equivocar, para eso es el cuaderno — no borres. Deja el error "
            "a la vista y responde estas tres preguntas al lado, con lápiz. Con eso, el mismo error no vuelve dos veces.", CW - 80, 25, color=GRAY, lh=36)
    qs = [("¿Qué entendí mal?", "de la pregunta, del dato, de la gráfica"),
          ("¿En qué paso me desvié?", "mira el paso a paso: ¿cuál tachaste sin hacerlo?"),
          ("¿Qué hago distinto la próxima vez?", "una sola cosa, concreta, que puedas repetir")]
    qw = (CW - 80 - 2 * 30) / 3
    for i, (q, d) in enumerate(qs):
        x = M + 40 + i * (qw + 30); yy = y + 200
        b.append(rect(x, yy, qw, 220, "white", r=18, stroke=EDU_AZUL, sw=2.4))
        b.append(num_badge(x + 40, yy + 44, i + 1, EDU_AZUL, r=24, size=24))
        for j, ln in enumerate(wrap(q, 24)):
            b.append(T(x + 80, yy + 54 + j * 30, [ln], 25, EDU_AZUL, weight="700"))
        for j, ln in enumerate(wrap(d, 34)):
            b.append(T(x + 30, yy + 130 + j * 28, [ln], 21, GRAY, style="italic"))
    y += 520

    # micro-hábitos
    b.append(T(M, y + 44, ["Tres micro-hábitos del sábado"], 36, PSI, weight="700"))
    y += 80
    hab = [("ANTES", "Desayuna. Trae el libro y dos lápices. Lee la bitácora del sábado pasado: ahí dejaste escrito por dónde seguir.", EDU_ORO),
           ("DURANTE", "Escribe antes de marcar. Pide el Salvavidas cuando lo necesites, no cuando ya se acabó el tiempo.", EDU_AZUL),
           ("DESPUÉS", "Cuéntale a alguien — en casa, en el bus — una cosa que aprendiste hoy. Si no la puedes explicar, no la aprendiste todavía.", EDU_VERDE)]
    hw = (CW - 2 * 30) / 3
    for i, (t, d, c) in enumerate(hab):
        x = M + i * (hw + 30)
        b.append(rect(x, y, hw, 400, "white", r=22, stroke=c, sw=3))
        b.append(rect(x, y, hw, 64, c, r=22)); b.append(rect(x, y + 32, hw, 32, c, r=0))
        b.append(T(x + hw / 2, y + 44, [t], 24, "white", weight="700", anchor="middle", ls=3))
        parrafo_j(b, x + 30, y + 96, d, hw - 60, 25, lh=36)
    footer(b, 8, PSI)
    svg_close(b, OUT + "ap08_psico1.svg")


# ═════════════════════════════ 9 · PSICOLOGÍA (coordinadores) ═════════════════════════════
def psico_2():
    b = svg_open()
    y = frame(b, "Para la coordinación", PSI, 9, "cómo leer este cuaderno sin entrar al salón")
    y = titulo(b, y + 20, "Cómo leer este cuaderno", PSI,
               sub="Esta hoja es para el coordinador. El cuaderno está hecho para que la calidad de la clase se pueda auditar "
                   "desde el papel: tres cuadernos al azar dicen más que una visita al salón.")
    top = y + 10

    # qué mirar
    b.append(rect(M, top, CW, 520, "white", r=26, stroke=PSI, sw=3))
    b.append(T(M + 40, top + 60, ["Qué mirar en tres cuadernos al azar"], 34, PSI, weight="700"))
    checks = [("La cuadrícula está escrita antes de la letra marcada", "es la señal de que el método se está usando"),
              ("La bitácora de cada clase está llena", "es la única parte que el estudiante escribe sobre sí mismo"),
              ("Hay errores a la vista, sin borrar, con las tres preguntas al lado", "el cuaderno enseña por el error, no a pesar de él"),
              ("El Salvavidas se usó en algunas hojas", "usarlo es buena señal: pidió ayuda a tiempo"),
              ("El tablero de metas (hoja 5) tiene un obstáculo que depende del estudiante", "si el obstáculo es «el profe», la meta está fuera de su control")]
    for i, (t, d) in enumerate(checks):
        yy = top + 120 + i * 76
        b.append(checkbox(M + 44, yy - 22, s=13, c=PSI))
        b.append(T(M + 96, yy, [t], 26, INK, weight="700"))
        b.append(T(M + 96, yy + 32, [d], 21, GRAY, style="italic"))
    y = top + 560

    # señales
    b.append(T(M, y + 44, ["Señales y qué hacer con ellas"], 34, PSI, weight="700"))
    y += 76
    cols = [("Señal", 600), ("Qué suele significar", 600), ("Qué hacer", CW - 1200)]
    rows = [("Respuesta correcta, cuadrícula vacía", "Copió o adivinó. El acierto no es suyo todavía.", "Conversación con el estudiante, no sanción. «Muéstrame cómo llegaste».", EDU_ROJO),
            ("Bitácora en blanco varias clases", "El cierre de la clase no se está haciendo.", "Hablar con el profesor, no con el estudiante: el cierre lo dirige él.", EDU_ORO),
            ("Muchas hojas con Salvavidas", "Pide ayuda a tiempo. No es alerta.", "Revisar en qué estrategia se repite: ahí está el refuerzo que necesita.", EDU_VERDE),
            ("Obstáculo del tablero = «el profe», «el colegio»", "La meta está puesta fuera de su alcance.", "Rehacer la casilla 3 con él: el obstáculo tiene que estar en lo que él controla.", PSI),
            ("Puntaje «hoy» sin escribir en la hoja 4", "No ha hecho el primer simulacro.", "Agendar el simulacro. Sin número no hay meta que entrenar.", EDU_AZUL)]
    x = M
    for t, w_ in cols:
        b.append(rect(x, y, w_ - 6, 56, PSI, r=10)); b.append(T(x + 20, y + 37, [t], 22, "white", weight="700")); x += w_
    y += 64
    for i, (s1, s2, s3, c) in enumerate(rows):
        rh = 128
        if i % 2: b.append(rect(M, y, CW, rh, SOFT, r=10))
        b.append(rect(M, y + 10, 10, rh - 20, c, r=5))
        for k, (txt, w_) in enumerate(zip((s1, s2, s3), [c[1] for c in cols])):
            x = M + sum(cc[1] for cc in cols[:k])
            for j, ln in enumerate(wrap(txt, int(w_ / 13.5))):
                b.append(T(x + 26, y + 42 + j * 30, [ln], 23, INK if k else c, weight="700" if k == 0 else "400"))
        y += rh
    y += 40

    # cómo hablar + lo que no se hace
    hw = (CW - 40) / 2
    panel(b, M, y + 20, hw, 460, EDU_VERDE, title="Cómo hablar de la meta con él", title_size=24)
    pregs = ["No: «¿cuánto sacaste?»  Sí: «¿en qué paso te perdiste?»",
             "No: «¿por qué te fue mal?»  Sí: «¿qué dejaste escrito que sí servía?»",
             "No: «tienes que estudiar más.»  Sí: «¿qué vas a hacer distinto el sábado?»",
             "Pregunta por la bitácora, no por la nota. La nota ya la sabe."]
    yy = y + 90
    for p_ in pregs:
        for j, ln in enumerate(wrap(p_, 54)):
            if j == 0: b.append(f'<circle cx="{M+40}" cy="{yy-9}" r="6" fill="{EDU_VERDE}"/>')
            b.append(T(M + 62, yy, [ln], 24, INK)); yy += 33
        yy += 14
    panel(b, M + hw + 40, y + 20, hw, 460, EDU_ROJO, title="Lo que no se hace", title_size=24)
    nos = ["Castigar el error. El cuaderno lo necesita a la vista para enseñar.",
           "Comparar cuadernos en voz alta. Se comparan con el propio de hace un mes.",
           "Llenar la bitácora por él «para que quede completa». Vacía dice más que falsa.",
           "Mover la meta sin él. La meta se renegocia con el estudiante, no se le impone."]
    yy = y + 90
    for p_ in nos:
        for j, ln in enumerate(wrap(p_, 54)):
            if j == 0: b.append(f'<circle cx="{M+hw+80}" cy="{yy-9}" r="6" fill="{EDU_ROJO}"/>')
            b.append(T(M + hw + 102, yy, [ln], 24, INK)); yy += 33
        yy += 14
    footer(b, 9, PSI, texto="Cuaderno de trabajo · Saber 11 · hoja para la coordinación")
    svg_close(b, OUT + "ap09_psico2.svg")


# ═════════════════════════════ PORTADAS DE ÁREA (10 · 53 · 96) ═════════════════════════════
N_AREAS = len(AREAS)   # siete, como en el libro (Biología y Química por separado)


def _tinte(c, k=0.28):
    """El color del área mezclado con blanco: borde suave de las tarjetas de clase."""
    r, g, b_ = (int(c[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02X%02X%02X" % tuple(round(255 - (255 - v) * k) for v in (r, g, b_))


def portada_area(pag, n_area, nombre, c, titulo, comps, instr_titulo, instr_texto, dibujo,
                 momentos, clase_sub, clase_lab, archivo, sub_titulo=None, iw=300,
                 cajas=(EDU_ROJO, EDU_VERDE, EDU_ORO), borde_clase=None,
                 x_clase_sub=700, x_puntaje=520, paso_puntaje=330, claro=None):
    # claro: color de los textos secundarios sobre la banda (None → blanco translúcido)
    cl, op_cl = (claro, 1) if claro else ("white", 0.78)
    b = svg_open()
    b.append(rect(0, 0, W, 760, c, r=0))
    b.append(dots(60, 50, "white", r=3, step=38, cols=50, rows=18, op=0.10))
    b.append(logo(M, 60, 70, chip=True, pad=14))
    b.append(T(W - M, 110, [f"ÁREA {n_area} DE {N_AREAS}"], 26, cl, weight="700", anchor="end", ls=4, op=op_cl))
    b.append(T(M, 400, [titulo], 150, "white", weight="700", ls=6))
    if sub_titulo:
        b.append(T(M, 480, [sub_titulo], 56, "white", weight="700", ls=8, op=0.85))
    for k, ln in enumerate(comps):
        b.append(T(M, (540 if sub_titulo else 480) + k * 60, [ln], 28, cl, op=op_cl))
    # instrumento
    b.append(rect(M, 620, CW, 280, "white", r=26, stroke=c, sw=3))
    dibujo(b, M + 36, 650, iw, 220)
    tx = M + 80 + iw
    b.append(T(tx, 690, [instr_titulo], 34, c, weight="700"))
    parrafo_j(b, tx, 712, instr_texto, W - M - 40 - tx, 24, color=INK, lh=34)

    # seis momentos
    y = 960
    b.append(T(M, y + 40, ["Tus seis momentos"], 38, c, weight="700"))
    b.append(T(M + 380, y + 40, ["cada uno: 10 preguntas del libro + entrenamiento ICFES + simulacro"], 23, GRAY, style="italic"))
    mw = (CW - 40) / 2
    for i, (nm, comp) in enumerate(momentos):
        x = M + (i % 2) * (mw + 40); yy = y + 90 + (i // 2) * 130
        b.append(rect(x, yy, mw, 110, "white", r=18, stroke=c, sw=2.4))
        b.append(num_badge(x + 50, yy + 55, i + 1, c, r=30, size=30))
        if nm:
            b.append(T(x + 104, yy + 50, [nm], 26, c, weight="700"))
            b.append(T(x + 104, yy + 84, [comp], 20, GRAY))
        else:
            b.append(line(x + 104, yy + 56, x + mw - 150, yy + 56, LGRAY, 2.4))
            b.append(T(x + 104, yy + 88, [comp or "Momento " + str(i + 1)], 20, GRAY))
        for k in range(3):
            b.append(checkbox(x + mw - 130 + k * 38, yy + 40, s=11, c=cajas[k]))
    b.append(T(M, y + 90 + 3 * 130 + 20, ["casillas: libro · ICFES · simulacro"], 19, GRAY, style="italic"))

    # ocho clases
    y = y + 90 + 3 * 130 + 70
    b.append(rect(M, y, CW, 560, SOFT, r=26))
    b.append(T(M + 40, y + 56, [f"Mis ocho clases de {nombre}"], 36, c, weight="700"))
    b.append(T(M + x_clase_sub, y + 56, [clase_sub], 23, GRAY, style="italic"))
    cw_ = (CW - 80 - 3 * 20) / 4
    for i in range(8):
        x = M + 40 + (i % 4) * (cw_ + 20); yy = y + 90 + (i // 4) * 220
        b.append(rect(x, yy, cw_, 200, "white", r=18, stroke=borde_clase or _tinte(c), sw=2))
        b.append(num_badge(x + 34, yy + 34, i + 1, c, r=22, size=22))
        b.append(T(x + 70, yy + 42, ["fecha ________"], 20, GRAY))
        for k, lab in enumerate(["llegué", "salí"]):
            fy = yy + 90 + k * 46
            b.append(T(x + 24, fy + 8, [lab], 19, GRAY))
            for m_, mood in enumerate(["worried", "calm", "happy"]):
                b.append(face(x + 110 + m_ * 54, fy, 18, mood, GRAY, "white", sw=2))
        b.append(line(x + 24, yy + 184, x + cw_ - 24, yy + 184, LGRAY, 2))
        b.append(T(x + 24, yy + 176, [clase_lab], 16, GRAY, style="italic"))

    # puntaje del área
    y += 600
    b.append(rect(M, y, CW, 150, "white", r=26, stroke=EDU_ORO, sw=3))
    b.append(T(M + 40, y + 62, [f"Mi puntaje en {nombre}"], 30, c if c != "#1F4E8C" else EDU_ORO, weight="700"))
    b.append(T(M + 40, y + 106, ["(de 0 a 100)"], 20, GRAY, style="italic"))
    for k, lab in enumerate(["simulacro 1", "simulacro 2", "simulacro 3", "META"]):
        x = M + x_puntaje + k * paso_puntaje
        b.append(T(x, y + 62, [lab], 22, EDU_AZUL if lab == "META" else GRAY, weight="700" if lab == "META" else "400"))
        b.append(line(x, y + 112, x + 260, y + 112, EDU_AZUL if lab == "META" else LGRAY, 2.6))
    footer(b, pag, c, texto=f"{nombre if not sub_titulo else nombre + ' y Ciudadanas'} · área {n_area} de {N_AREAS}")
    svg_close(b, OUT + archivo)


def _dib_mate(b, x, y, w, h):
    b.append(grid_box(x, y, w, h, step=26))
    b.append(PT(x + 24, y + 50, ["4  6  8  10", "+2 +2 +2", "→ lineal"], 28, PENCIL, rot=-1.5, lh=44))


def _dib_lc(b, x, y, w, h):
    c = "#A82424"
    b.append(rect(x, y, w, h, SOFT, r=14, stroke="#E3E8EF", sw=2))
    b.append(rect(x + 4, y + 8, 8, h - 16, c, r=4))
    for k, (ln, sub) in enumerate([("el matiz suena", True), ("a traición; la duda,", False), ("a tibieza", True)]):
        yy = y + 50 + k * 44
        if sub:   # el subrayado va DEBAJO del texto, en el color del área
            b.append(f'<line x1="{x + 30}" y1="{yy + 11}" x2="{x + 34 + tw(ln, 23, style="italic")}" y2="{yy + 11}" '
                     f'stroke="{c}" stroke-width="4" stroke-linecap="round" opacity="0.6"/>')
        b.append(T(x + 32, yy, [ln], 23, INK, style="italic"))
    b.append(PT(x + 32, y + 196, ["¿traición a quién?"], 24, PENCIL, rot=-1.5))


def _dib_soc(b, x, y, w, h):
    c = "#C9821B"
    b.append(rect(x, y, w, h, SOFT, r=14, stroke="#E3E8EF", sw=2))
    b.append(rect(x + 4, y + 8, 8, h - 16, c, r=4))
    b.append(T(x + 32, y + 36, ["EL CASO"], 15, GRAY, weight="700", ls=2))
    for k, (lab, mano) in enumerate([("quién gana", "los pescadores"), ("quién pierde", "el turismo"),
                                     ("quién decide", "la alcaldía")]):
        yy = y + 66 + k * 48
        b.append(T(x + 32, yy, [lab], 20, c, weight="700"))
        b.append(line(x + 160, yy + 8, x + w - 14, yy + 8, LGRAY, 2))
        b.append(PT(x + 170, yy, [mano], 22, PENCIL, rot=-1))


def portada_mate():
    portada_area(10, 1, "Matemáticas", "#1F4E8C", "MATEMÁTICAS",
                 ["Interpretación y representación  ·  Formulación y ejecución  ·  Argumentación",
                  "Componentes: numérico-variacional  ·  geométrico-métrico  ·  aleatorio"],
                 "Tu instrumento de pensamiento: la cuadrícula de trabajo",
                 "En Matemáticas nada se resuelve «en la cabeza». La cuadrícula es donde pones la tabla, la "
                 "diferencia entre un valor y el siguiente, el dibujo de la gráfica, la cuenta. Si la cuadrícula está vacía, "
                 "la respuesta no es tuya todavía.", _dib_mate,
                 [("Patrones y relaciones de cambio", "Componente numérico-variacional")] + [("", "")] * 5,
                 "fecha · cómo llegué · cómo salí · una cosa que aprendí", "aprendí:", "ap10_mate.svg",
                 borde_clase=AZ_LN, claro="#BFD4F2")


def portada_lc():
    portada_area(53, 2, "Lectura Crítica", "#A82424", "LECTURA CRÍTICA",
                 ["Identificar contenidos locales  ·  Comprender el sentido global  ·  Reflexionar y evaluar",
                  "Textos continuos: literarios, filosóficos, informativos  ·  Textos discontinuos"],
                 "Tu instrumento de pensamiento: el texto marcado",
                 "En Lectura Crítica no hay cuentas que hacer: hay un texto que interrogar. Lo que aquí reemplaza a la "
                 "cuadrícula es el subrayado y la pregunta escrita al margen. Si la hoja está limpia, no leíste: "
                 "pasaste los ojos.", _dib_lc,
                 [("El sentido de las palabras", "Componente semántico"),
                  ("La arquitectura del texto", "Componente semántico")] + [("", "")] * 4,
                 "fecha · cómo llegué · cómo salí · una palabra nueva", "palabra nueva:", "ap53_lc.svg",
                 cajas=(EDU_AZUL, EDU_VERDE, EDU_ORO), x_clase_sub=760, x_puntaje=560, paso_puntaje=320)


def portada_soc():
    portada_area(96, 3, "Sociales", "#C9821B", "SOCIALES",
                 ["Pensamiento social  ·  Interpretación de perspectivas  ·  Pensamiento reflexivo y sistémico"],
                 "Tu instrumento de pensamiento: el mapa de actores",
                 "Casi ninguna pregunta de esta área se resuelve recordando una fecha. Se resuelve preguntando quién "
                 "gana, quién pierde y quién decide. Cuando tengas los tres nombres escritos, la mitad de las opciones "
                 "se cae sola.", _dib_soc,
                 [("Pensar socialmente", "Competencias ciudadanas"), ("", "Competencias ciudadanas"),
                  ("", "Competencias ciudadanas"), ("", "Historia y cultura"), ("", "Espacio y ambiente"),
                  ("", "Ético-político")],
                 "fecha · cómo llegué · cómo salí · un caso que me marcó", "el caso:", "ap96_soc.svg",
                 sub_titulo="Y CIUDADANAS", iw=330, cajas=(EDU_AZUL, EDU_VERDE, EDU_ORO),
                 x_clase_sub=760, x_puntaje=560, paso_puntaje=320)


def _dib_bio(b, x, y, w, h):
    c = "#30843C"
    b.append(rect(x, y, w, h, SOFT, r=14, stroke="#E3E8EF", sw=2))
    b.append(rect(x + 4, y + 8, 8, h - 16, c, r=4))
    b.append(T(x + 32, y + 36, ["EL DATO"], 15, GRAY, weight="700", ls=2))
    base = y + h - 46
    for k, (lab, alto) in enumerate((("reposo", 50), ("esfuerzo", 112))):
        bx = x + 44 + k * 96
        b.append(rect(bx, base - alto, 60, alto, c if k else "white", r=4, stroke=c, sw=2.4))
        b.append(T(bx + 30, base + 26, [lab], 17, GRAY, anchor="middle"))
    b.append(line(x + 34, base, x + 230, base, INK, 2))
    b.append(PT(x + 232, y + 90, ["¿contra", "qué lo", "comparo?"], 22, PENCIL, rot=-2, lh=28))


def portada_bio():
    portada_area(139, 4, "Biología", "#30843C", "BIOLOGÍA",
                 ["Uso comprensivo del conocimiento científico  ·  Explicación de fenómenos  ·  Indagación",
                  "Componentes: celular  ·  organísmico  ·  ecosistémico  ·  ciencia, tecnología y sociedad"],
                 "Tu instrumento de pensamiento: el dato y su comparación",
                 "Tu cuerpo regula su agua, su azúcar y su calcio sin pedirte permiso, y ninguna de tus células ha "
                 "leído un libro de biología. Aquí vas a mirarlas como las mira un científico: qué cambió, qué se "
                 "midió y contra qué se compara. Si no puedes señalar con el dedo de dónde sale tu respuesta, "
                 "todavía es una corazonada.", _dib_bio,
                 [("La célula, una fábrica en cadena", "Componente biológico · celular"),
                  ("El equilibrio de adentro", "Componente biológico · organísmico"),
                  ("En el ecosistema nada cambia solo", "Componente biológico · ecosistémico"),
                  ("Cada invento, una oportunidad y un riesgo", "Ciencia, tecnología y sociedad"),
                  ("Lo que se hereda y lo que se edita", "Entorno biológico"),
                  ("La vida cambia", "Entorno biológico")],
                 "fecha · cómo llegué · cómo salí · algo que observé", "observé:", "ap139_bio.svg",
                 iw=330, cajas=(EDU_AZUL, EDU_ROJO, EDU_ORO), x_clase_sub=760, x_puntaje=560, paso_puntaje=320)


def _dib_qui(b, x, y, w, h):
    c = "#0F7A68"
    b.append(rect(x, y, w, h, SOFT, r=14, stroke="#E3E8EF", sw=2))
    b.append(rect(x + 4, y + 8, 8, h - 16, c, r=4))
    b.append(T(x + 32, y + 36, ["LAS PARTÍCULAS"], 15, GRAY, weight="700", ls=2))
    # un vaso con agua y partículas disueltas
    vx, vy, vw, vh = x + 40, y + 60, 120, 130
    b.append(rect(vx, vy + 34, vw, vh - 34, "#EAF4FA", r=8))
    b.append(f'<path d="M {vx - 6} {vy} L {vx} {vy + 6} L {vx} {vy + vh - 10} Q {vx} {vy + vh} {vx + 10} {vy + vh} '
             f'L {vx + vw - 10} {vy + vh} Q {vx + vw} {vy + vh} {vx + vw} {vy + vh - 10} L {vx + vw} {vy + 6} '
             f'L {vx + vw + 6} {vy}" fill="none" stroke="#7C8A99" stroke-width="3" stroke-linejoin="round"/>')
    for px, py in ((24, 60), (58, 76), (92, 56), (40, 100), (78, 112), (100, 92), (20, 118)):
        b.append(f'<circle cx="{vx + px}" cy="{vy + py}" r="7" fill="white" stroke="{c}" stroke-width="2"/>')
    b.append(PT(x + 182, y + 96, ["40 → 0,40 g", "16 → ¿?"], 23, PENCIL, rot=-2, lh=34))


def portada_qui():
    portada_area(182, 5, "Química", "#0F7A68", "QUÍMICA",
                 ["Uso comprensivo del conocimiento científico  ·  Explicación de fenómenos  ·  Indagación",
                  "Componentes: aspectos analíticos y fisicoquímicos de sustancias y de mezclas  ·  entorno químico"],
                 "Tu instrumento de pensamiento: la partícula y su unidad",
                 "La sal que se pega en el salero, el gas que se escapa cuando destapas una gaseosa, el hielo que "
                 "flota en tu vaso: todo eso lo hacen partículas que nunca vas a ver. Aquí las vas a dibujar y a "
                 "contar, con la unidad al lado de cada número. Un número sin unidad no dice nada, y una partícula "
                 "que no sabes dibujar todavía es una palabra.", _dib_qui,
                 [("Disolver, separar y reaccionar", "Aspectos analíticos de sustancias"),
                  ("El calor, los cambios de estado y la densidad", "Aspectos fisicoquímicos de sustancias"),
                  ("Mezclar no es transformar", "Aspectos analíticos de mezclas"),
                  ("Cada propiedad física separa algo", "Aspectos fisicoquímicos de mezclas"),
                  ("El carbono en el tanque, el vaso y la bolsa", "Entorno químico"),
                  ("Reacciones que calientan y encadenan", "Entorno químico")],
                 "fecha · cómo llegué · cómo salí · algo que medí", "medí:", "ap182_qui.svg",
                 iw=330, cajas=(EDU_AZUL, EDU_ROJO, EDU_ORO), x_clase_sub=760, x_puntaje=560, paso_puntaje=320)


def _dib_fis(b, x, y, w, h):
    c = "#5C7A1E"
    b.append(rect(x, y, w, h, SOFT, r=14, stroke="#E3E8EF", sw=2))
    b.append(rect(x + 4, y + 8, 8, h - 16, c, r=4))
    b.append(T(x + 32, y + 36, ["LAS FLECHAS"], 15, GRAY, weight="700", ls=2))
    # una caja sobre el piso con sus cuatro fuerzas, dibujadas a lápiz
    piso = y + 160
    b.append(line(x + 30, piso, x + w - 24, piso, "#7C8A99", 3))
    bx, by = x + 130, piso - 60
    b.append(rect(bx, by, 76, 60, "white", r=4, stroke=INK, sw=2.4))
    cx, cy = bx + 38, by + 30
    b.append(hand_arrow(cx, cy, cx, cy - 78, PENCIL, sw=3, bend=0.0, head=13))
    b.append(hand_arrow(cx, cy, cx, cy + 74, PENCIL, sw=3, bend=0.0, head=13))
    b.append(hand_arrow(cx, cy, cx + 110, cy, PENCIL, sw=3, bend=0.0, head=13))
    b.append(hand_arrow(cx, cy, cx - 96, cy, PENCIL, sw=3, bend=0.0, head=13))
    b.append(PT(cx + 12, cy - 56, ["N"], 24, PENCIL, rot=-2))
    b.append(PT(cx + 12, cy + 70, ["P"], 24, PENCIL, rot=-2))
    b.append(PT(cx + 56, cy - 14, ["empujo"], 20, PENCIL, rot=-2))
    b.append(PT(cx - 96, cy - 14, ["roce"], 20, PENCIL, rot=-2))


def portada_fis():
    portada_area(225, 6, "Física", "#5C7A1E", "FÍSICA",
                 ["Uso comprensivo del conocimiento científico  ·  Explicación de fenómenos  ·  Indagación",
                  "Componentes: mecánica clásica  ·  termodinámica  ·  eventos ondulatorios  ·  electromagnetismo"],
                 "Tu instrumento de pensamiento: la flecha con su nombre",
                 "Nada cambia porque sí. Si el balón frena, algo lo frenó; si el café se enfría, el calor se fue a "
                 "alguna parte. La física es la terquedad de no aceptar un cambio sin su causa. Aquí cada fuerza se "
                 "dibuja como una flecha con su nombre y cada julio tiene que aparecer en la cuenta. Si te queda una "
                 "flecha que nadie empuja, o energía que no sabes a dónde fue, todavía no has terminado.", _dib_fis,
                 [("Fuerzas, movimiento y energía", "Componente físico · mecánica clásica"),
                  ("El calor, la temperatura y los cambios de fase", "Componente físico · termodinámica"),
                  ("", "Componente físico · electromagnetismo"),
                  ("", "Componente físico · eventos ondulatorios"),
                  ("", "Componente físico · mecánica clásica"),
                  ("", "Componente físico · termodinámica")],
                 "fecha · cómo llegué · cómo salí · una causa que encontré", "la causa:", "ap225_fis.svg",
                 iw=330, cajas=(EDU_AZUL, EDU_ROJO, EDU_ORO), x_clase_sub=740, x_puntaje=560, paso_puntaje=320)


if __name__ == "__main__":
    psico_1(); psico_2(); portada_mate(); portada_lc(); portada_soc(); portada_bio(); portada_qui(); portada_fis()
    print("ok 8-10, 53, 96, 139, 182, 225")
