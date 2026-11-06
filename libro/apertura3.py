#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hojas 8-10: la psicología de la meta (estudiante, coordinadores) y portada de Matemáticas."""
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


# ═════════════════════════════ 10 · PORTADA DE ÁREA · MATEMÁTICAS ═════════════════════════════
def portada_mate():
    AZm = "#1F4E8C"
    b = svg_open()
    b.append(rect(0, 0, W, 760, AZm, r=0))
    b.append(dots(60, 50, "white", r=3, step=38, cols=50, rows=18, op=0.10))
    b.append(logo(M, 60, 70, chip=True, pad=14))
    b.append(T(W - M, 110, ["ÁREA 1 DE 6"], 26, "#BFD4F2", weight="700", anchor="end", ls=4))
    b.append(T(M, 400, ["MATEMÁTICAS"], 150, "white", weight="700", ls=6))
    b.append(T(M, 480, ["Interpretación y representación  ·  Formulación y ejecución  ·  Argumentación"], 28, "#BFD4F2"))
    b.append(T(M, 540, ["Componentes: numérico-variacional  ·  geométrico-métrico  ·  aleatorio"], 28, "#BFD4F2"))
    # instrumento
    b.append(rect(M, 620, CW, 280, "white", r=26, stroke=AZm, sw=3))
    b.append(grid_box(M + 36, 650, 300, 220, step=26))
    b.append(PT(M + 60, 700, ["4  6  8  10", "+2 +2 +2", "→ lineal"], 28, PENCIL, rot=-1.5, lh=44))
    b.append(T(M + 380, 690, ["Tu instrumento de pensamiento: la cuadrícula de trabajo"], 34, AZm, weight="700"))
    parrafo_j(b, M + 380, 712, "En Matemáticas nada se resuelve «en la cabeza». La cuadrícula es donde pones la tabla, la "
            "diferencia entre un valor y el siguiente, el dibujo de la gráfica, la cuenta. Si la cuadrícula está vacía, "
            "la respuesta no es tuya todavía.", CW - 420, 24, color=INK, lh=34)

    # seis momentos
    y = 960
    b.append(T(M, y + 40, ["Tus seis momentos"], 38, AZm, weight="700"))
    b.append(T(M + 380, y + 40, ["cada uno: 10 preguntas del libro + entrenamiento ICFES + simulacro"], 23, GRAY, style="italic"))
    momentos = ["Patrones y relaciones de cambio", "", "", "", "", ""]
    mw = (CW - 40) / 2
    for i, nm in enumerate(momentos):
        x = M + (i % 2) * (mw + 40); yy = y + 90 + (i // 2) * 130
        b.append(rect(x, yy, mw, 110, "white", r=18, stroke=AZm, sw=2.4))
        b.append(num_badge(x + 50, yy + 55, i + 1, AZm, r=30, size=30))
        if nm:
            b.append(T(x + 104, yy + 50, [nm], 26, AZm, weight="700"))
            b.append(T(x + 104, yy + 84, ["Componente numérico-variacional"], 20, GRAY))
        else:
            b.append(line(x + 104, yy + 56, x + mw - 150, yy + 56, LGRAY, 2.4))
            b.append(T(x + 104, yy + 88, ["Momento " + str(i + 1)], 20, GRAY))
        for k in range(3):
            b.append(checkbox(x + mw - 130 + k * 38, yy + 40, s=11, c=[EDU_ROJO, EDU_VERDE, EDU_ORO][k]))
    b.append(T(M, y + 90 + 3 * 130 + 20, ["casillas: libro · ICFES · simulacro"], 19, GRAY, style="italic"))

    # ocho clases
    y = y + 90 + 3 * 130 + 70
    b.append(rect(M, y, CW, 560, SOFT, r=26))
    b.append(T(M + 40, y + 56, ["Mis ocho clases de Matemáticas"], 36, AZm, weight="700"))
    b.append(T(M + 700, y + 56, ["fecha · cómo llegué · cómo salí · una cosa que aprendí"], 23, GRAY, style="italic"))
    cw_ = (CW - 80 - 3 * 20) / 4
    for i in range(8):
        x = M + 40 + (i % 4) * (cw_ + 20); yy = y + 90 + (i // 4) * 220
        b.append(rect(x, yy, cw_, 200, "white", r=18, stroke=AZ_LN, sw=2))
        b.append(num_badge(x + 34, yy + 34, i + 1, AZm, r=22, size=22))
        b.append(T(x + 70, yy + 42, ["fecha ________"], 20, GRAY))
        for k, lab in enumerate(["llegué", "salí"]):
            fy = yy + 90 + k * 46
            b.append(T(x + 24, fy + 8, [lab], 19, GRAY))
            for m_, mood in enumerate(["worried", "calm", "happy"]):
                b.append(face(x + 110 + m_ * 54, fy, 18, mood, GRAY, "white", sw=2))
        b.append(line(x + 24, yy + 184, x + cw_ - 24, yy + 184, LGRAY, 2))
        b.append(T(x + 24, yy + 176, ["aprendí:"], 16, GRAY, style="italic"))

    # puntaje del área
    y += 600
    b.append(rect(M, y, CW, 150, "white", r=26, stroke=EDU_ORO, sw=3))
    b.append(T(M + 40, y + 62, ["Mi puntaje en Matemáticas"], 30, EDU_ORO, weight="700"))
    b.append(T(M + 40, y + 106, ["(de 0 a 100)"], 20, GRAY, style="italic"))
    for k, lab in enumerate(["simulacro 1", "simulacro 2", "simulacro 3", "META"]):
        x = M + 520 + k * 330
        b.append(T(x, y + 62, [lab], 22, EDU_AZUL if lab == "META" else GRAY, weight="700" if lab == "META" else "400"))
        b.append(line(x, y + 112, x + 260, y + 112, EDU_AZUL if lab == "META" else LGRAY, 2.6))
    footer(b, 10, AZm, texto="Matemáticas · área 1 de 6")
    svg_close(b, OUT + "ap10_mate.svg")


if __name__ == "__main__":
    psico_1(); psico_2(); portada_mate()
    print("ok 8-10")
