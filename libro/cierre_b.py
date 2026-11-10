#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cierre del cuaderno · estilo B · Bitácora · páginas 396, 397 y 398 (armado final, 10 nov 2026).

Decisiones de Nelson (tablero/decisiones.csv, 10 nov): el cierre post-prueba son 2 páginas, y la
última cara (398) no queda en blanco: «algo moderno y minimalista, que vaya de la mano con lo
psicológico; al final un mensaje o qué te dirías al terminar».

    396  «Ya lo presentaste»   cómo me fue · mi puntaje frente a mi meta (la de la página 3) · qué
                               funcionó del método y qué no
    397  «Lo que me llevo»     para la universidad o el trabajo · carta a quien empieza el cuaderno
                               el próximo año
    398  mensaje final         una frase, mucho aire, «Lo que me diría hoy, al terminar», la fecha en
                               que cerré el cuaderno y las caritas por última vez

Es para DESPUÉS del examen de verdad. Tono de la apertura: juvenil, algo filosófico, de frente,
sin sermón. No menciona Generación E. Sin líneas horizontales decorativas (regla 1): las únicas
líneas son renglones para escribir. Todo el texto es nuevo: va marcado con «# TEXTO NUEVO» para
que Nelson lo apruebe.

    python3 cierre_b.py      → libro/cierre_b_1.svg, cierre_b_2.svg, cierre_b_3.svg
"""
import os

from lib import *                    # noqa: F401,F403
import bitacora as BT
from bitacora import TX, twf, fit, SHA, MONO, HAND, FOSFO, FOSFO_2, TINTA_B, resaltador, wob_rect, estrellita
from apertura_b import pagina, cabecera, titulo, caja, h2, rot, num, mano, PSI, P_METAS
import paginas

LIBRO = os.path.dirname(os.path.realpath(__file__)) + "/"
P1, P2 = paginas.CIERRE
P3 = paginas.MENSAJE_FINAL
RENGLON = "#D3D9E2"            # renglón para escribir (no es texto)
FONDO = 2440                   # hasta aquí llega el contenido (el pie va debajo)

# Las cinco pruebas del examen de verdad (los resultados traen Ciencias Naturales en un solo puntaje)
PRUEBAS = [("Matemáticas", "#1F4E8C", None),
           ("Lectura Crítica", "#A82424", None),
           ("Sociales y Ciudadanas", "#C9821B", None),
           ("Ciencias Naturales", "#30843C", "un solo puntaje: Biología, Química y Física"),           # TEXTO NUEVO
           ("Inglés", "#1BA0A8", None)]


def renglones(b, x, y, w, y_fin, step=50):
    """Renglones de escribir desde y hasta y_fin (sin pasarse)."""
    n = int((y_fin - y) // step) + 1
    if n > 0:
        b.append(wlines(x, y, w, n, c=RENGLON, step=step))
    return y + (n - 1) * step


def pista(b, x, y, txt, w, size=21):
    """Una ayuda en cursiva gris, en tantos renglones como haga falta. Devuelve dónde terminó."""
    for j, ln in enumerate(wrap_px(txt, size, w, "400", "italic")):
        b.append(T(x, y + j * size * 1.38, [" ".join(ln)], size, GRAY, style="italic"))
    return y + (len(wrap_px(txt, size, w, "400", "italic")) - 1) * size * 1.38


def campo(b, x, y, rotulo, w_linea, c=INK, size=24, weight="400"):
    """«Rótulo ________» en un renglón. Devuelve el x donde termina."""
    b.append(T(x, y, [rotulo], size, c, weight=weight))
    x0 = x + tw(rotulo, size, weight) + 12
    b.append(line(x0, y + 4, x0 + w_linea, y + 4, RENGLON, 2.4))
    return x0 + w_linea


# ═════════════════════════════ 396 · YA LO PRESENTASTE ═════════════════════════════
SUB_1 = ("Esta página se llena después del examen de verdad: una parte en los días siguientes y otra cuando "   # TEXTO NUEVO
         "lleguen los resultados. No es para nadie más. Es para que lo que hiciste estos sábados no se quede "
         "solo en un número.")
METODO = [  # lo que el cuaderno le pidió hacer, en sus palabras                                    # TEXTO NUEVO
    "Escribir mi primera idea antes de hacer nada",
    "Llenar el instrumento antes de marcar",
    "El salvavidas, cuando me bloqueaba",
    "Tachar cada opción con una razón",
    "Las estrategias de cada misión",
    "El simulacro y su devolución",
    "Mirar cómo llego y cómo salgo",
]


def pagina_1():
    b = pagina()
    y = cabecera(b, "Cierre", "para después del examen de verdad", PSI)                              # TEXTO NUEVO
    y = titulo(b, y + 10, "Ya lo presentaste", marca="presentaste", size=68, sub=SUB_1, sub_size=24)  # TEXTO NUEVO
    # ── cómo me fue ──
    top = y + 6
    H1 = 560
    caja(b, M, top, CW, H1, c=PSI, sw=3, seed=901)
    wt = h2(b, M + 36, top + 56, "Cómo me fue", PSI, 34, marca=True, fill=FOSFO_2, seed=902)         # TEXTO NUEVO
    campo(b, M + 60 + wt, top + 54, "Presenté el Saber 11 el", 320, GRAY, 23)                         # TEXTO NUEVO
    # cómo salí del examen: encierra una
    fy = top + 150
    rot(b, M + 36, fy - 40, "Salí del examen así · encierra una", TINTA_B, 17)                        # TEXTO NUEVO
    moods = [("worried", "preocupado"), ("tired", "agotado"), ("calm", "tranquilo"), ("happy", "contento"),  # TEXTO NUEVO
             ("proud", "orgulloso"), ("surprised", "no sé todavía")]
    for i, (md, lab) in enumerate(moods):
        cx = M + 90 + i * 150
        b.append(face(cx, fy + 40, 38, md, TINTA_B, "white", sw=2.6))
        b.append(T(cx, fy + 112, [lab], 18, GRAY, anchor="middle"))
    # dos preguntas para escribir, a la derecha de las caritas
    qx = M + 36 + 6 * 150 + 10
    qw = W - M - 36 - qx
    pr = [("La pregunta que más me costó, y por qué", fy - 40),                                       # TEXTO NUEVO
          ("Un momento del examen en que usé algo de este cuaderno", fy + 120)]                       # TEXTO NUEVO
    for t, yy in pr:
        b.append(T(qx, yy, [t], 23, PSI, weight="700"))
        renglones(b, qx, yy + 52, qw, yy + 52 + 50)
    # lo que haría distinto ese día
    ly = fy + 190
    b.append(T(M + 36, ly + 40, ["Si pudiera volver a ese día, haría distinto"], 23, PSI, weight="700"))  # TEXTO NUEVO
    renglones(b, M + 36, ly + 96, CW - 72, top + H1 - 40)
    # ── mi puntaje frente a mi meta ──
    y = top + H1 + 26
    H2 = 610
    caja(b, M, y, CW, H2, c=EDU_AZUL, sw=3, seed=910)
    wt = h2(b, M + 36, y + 56, "Mi puntaje frente a mi meta", EDU_AZUL, 34, marca=True, fill=FOSFO, seed=911)  # TEXTO NUEVO
    b.append(T(M + 60 + wt, y + 54, [f"tu meta está en la página {P_METAS}: cópiala y ponle al lado lo que sacaste"],  # TEXTO NUEVO
               21, GRAY, style="italic"))
    # el global
    gx, gy, gw, gh = M + 36, y + 96, 360, 420
    b.append(wob_rect(gx, gy, gw, gh, EDU_AZUL, 2.6, fill="white", seed=912))
    b.append(rect(gx, gy, 10, gh, EDU_AZUL, r=0))                      # acento vertical (permitido)
    b.append(TX(gx + 30, gy + 50, "Puntaje global", 28, EDU_AZUL, SHA, "800"))                        # TEXTO NUEVO
    b.append(T(gx + 30, gy + 82, ["de 0 a 500"], 19, GRAY, style="italic"))
    filas = [("mi meta", 160), ("saqué", 265), ("diferencia", 370)]                                   # TEXTO NUEVO
    for lab, dy in filas:
        b.append(T(gx + 30, gy + dy, [lab], 22, INK if lab != "diferencia" else EDU_AZUL,
                   weight="700" if lab == "diferencia" else "400"))
        b.append(wob_rect(gx + 170, gy + dy - 44, gw - 200, 64, BT.CASILLA, 2, fill="white", seed=913 + dy, amp=0.8))
    # las cinco pruebas
    ax0 = gx + gw + 30
    aw = (W - M - 36 - ax0 - 4 * 18) / 5
    for i, (nm, c, sub) in enumerate(PRUEBAS):
        x = ax0 + i * (aw + 18)
        b.append(wob_rect(x, gy, aw, gh, c, 2.4, fill="white", seed=920 + i, amp=1))
        b.append(rect(x, gy, 10, gh, c, r=0))                         # acento vertical (permitido)
        ls = wrap_px(nm, 22, aw - 40, "700")
        for j, ln in enumerate(ls):
            b.append(T(x + 26, gy + 40 + j * 27, [" ".join(ln)], 22, c, weight="700"))
        if sub:
            for j, ln in enumerate(wrap_px(sub, 16, aw - 44, "400", "italic")):
                b.append(T(x + 26, gy + 40 + len(ls) * 27 + j * 21, [" ".join(ln)], 16, GRAY, style="italic"))
        for lab, dy in filas:
            b.append(T(x + 26, gy + dy, [lab], 19, INK if lab != "diferencia" else c,
                       weight="700" if lab == "diferencia" else "400"))
            b.append(line(x + 26, gy + dy + 38, x + aw - 22, gy + dy + 38, RENGLON, 2.4))
    yy = y + H2 - 36
    x1 = campo(b, M + 36, yy, "Donde más me acerqué:", 380, EDU_AZUL, 22, "700")                       # TEXTO NUEVO
    campo(b, x1 + 50, yy, "Lo que creo que explica la distancia:", W - M - 36 - (x1 + 50) - 400, EDU_AZUL, 22, "700")  # TEXTO NUEVO
    # ── qué funcionó del método y qué no ──
    y = y + H2 + 26
    H3 = FONDO - y
    caja(b, M, y, CW, H3, c=EDU_VERDE, sw=3, seed=930)
    wt = h2(b, M + 36, y + 56, "Qué funcionó del método y qué no", EDU_VERDE, 34, marca=True, fill=FOSFO_2,  # TEXTO NUEVO
            seed=931)
    b.append(T(M + 60 + wt, y + 54, ["marca una casilla por renglón; nadie te va a calificar esto"], 21, GRAY,  # TEXTO NUEVO
               style="italic"))
    TW = 1130
    cols = ["me sirvió", "a veces", "no me sirvió"]                                                    # TEXTO NUEVO
    cx = [M + 36 + 660 + k * 160 for k in range(3)]
    for k, t in enumerate(cols):
        rot(b, cx[k] + 13, y + 108, t, EDU_VERDE, 15, anchor="middle")
    ry = y + 160
    paso = (H3 - 200) / len(METODO)
    for i, it in enumerate(METODO):
        yy = ry + i * paso
        b.append(T(M + 36, yy, [it], 22, INK))
        for k in range(3):
            b.append(wob_rect(cx[k], yy - 24, 28, 28, EDU_VERDE, 2.2, fill="white", seed=940 + i * 3 + k, amp=0.6))
    # a la derecha: lo que cambiaría
    rx = M + 36 + TW + 30
    rw = W - M - 36 - rx
    b.append(BT.wob_vline(rx - 26, y + 90, y + H3 - 30, seed=950))
    b.append(T(rx, y + 108, ["Si empezara el cuaderno otra vez, cambiaría"], 22, EDU_VERDE, weight="700"))  # TEXTO NUEVO
    pista(b, rx, y + 140, "lo que no te sirvió no es un fracaso tuyo: también es un dato", rw, 19)    # TEXTO NUEVO
    renglones(b, rx, y + 210, rw, y + H3 - 36)
    BT.pie_b(b, P1, PSI, texto="Cuaderno de trabajo · Saber 11 · cierre")
    return b


# ═════════════════════════════ 397 · LO QUE ME LLEVO ═════════════════════════════
SUB_2 = ("El examen duró un día. Lo que aprendiste a hacer frente a una pregunta difícil te va a servir mucho "  # TEXTO NUEVO
         "más tiempo, y casi nunca va a venir con cuatro opciones.")
LLEVO = [  # (título, ayuda)                                                                          # TEXTO NUEVO
    ("Una forma de pensar que me llevo",
     "escribir antes de decidir, buscar el dato que manda, tachar con una razón… o la tuya"),
    ("Dónde la voy a necesitar",
     "una materia de primer semestre, un trabajo, una decisión que viene"),
    ("Lo que todavía me falta",
     "y a quién se lo voy a preguntar, o dónde lo voy a buscar"),
]
CARTA_AYUDA = ("Sin consejos de afiche. Cuéntale lo que de verdad te pasó: lo que te costó, lo que no esperabas, "  # TEXTO NUEVO
               "lo que te habría gustado saber el primer sábado.")


def pagina_2():
    b = pagina()
    y = cabecera(b, "Cierre", "lo que sigue después del cuaderno", PSI)                               # TEXTO NUEVO
    y = titulo(b, y + 10, "Lo que me llevo", marca="me llevo", size=68, sub=SUB_2, sub_size=24)       # TEXTO NUEVO
    # ── para la universidad o el trabajo ──
    top = y + 6
    H1 = 900
    caja(b, M, top, CW, H1, c=EDU_ORO, sw=3, seed=960)
    wt = h2(b, M + 36, top + 56, "Para la universidad o el trabajo", EDU_ORO, 34, marca=True, fill=FOSFO,  # TEXTO NUEVO
            seed=961)
    b.append(T(M + 60 + wt, top + 54, ["lo que este cuaderno te enseñó a hacer, no lo que te enseñó a responder"],  # TEXTO NUEVO
               21, GRAY, style="italic"))
    cw_ = (CW - 72 - 2 * 26) / 3
    ch = 560
    for i, (t, ay) in enumerate(LLEVO):
        x = M + 36 + i * (cw_ + 26)
        yy = top + 96
        b.append(wob_rect(x, yy, cw_, ch, EDU_ORO, 2.4, fill="white", seed=965 + i))
        num(b, x + 46, yy + 52, i + 1, EDU_ORO, r=26, size=22, seed=970 + i)
        for j, ln in enumerate(wrap_px(t, 25, cw_ - 110, "700")):
            b.append(T(x + 90, yy + 60 + j * 31, [" ".join(ln)], 25, EDU_ORO, weight="700"))
        pista(b, x + 30, yy + 128, ay, cw_ - 60, 19)
        renglones(b, x + 30, yy + 128 + 26 + 70, cw_ - 60, yy + ch - 30)    # mismos renglones en las tres
    yy = top + 96 + ch + 40
    b.append(T(M + 36, yy + 30, ["La próxima pregunta difícil de mi vida probablemente sea"], 24, EDU_ORO,  # TEXTO NUEVO
               weight="700"))
    renglones(b, M + 36, yy + 92, CW - 72, top + H1 - 40)
    # ── carta ──
    y = top + H1 + 26
    H2 = FONDO - y
    caja(b, M, y, CW, H2, c=PSI, sw=3, seed=980)
    wt = h2(b, M + 36, y + 56, "Carta a quien empieza este cuaderno el próximo año", PSI, 34, marca=True,  # TEXTO NUEVO
            fill=FOSFO_2, seed=981)
    fin = pista(b, M + 36, y + 102, CARTA_AYUDA, CW - 72, 21)
    mano(b, M + 36, fin + 74, "Hola,", PSI, 44, -1)                                                   # TEXTO NUEVO
    b.append(line(M + 36 + twf("Hola,", 44, HAND, "700") + 16, fin + 78, M + 640, fin + 78, RENGLON, 2.4))
    ult = renglones(b, M + 36, fin + 150, CW - 72, y + H2 - 120)
    # firma
    fy = y + H2 - 46
    mano(b, W - M - 900, fy, "—", PSI, 40, 0)
    x1 = campo(b, W - M - 860, fy, "", 380, GRAY, 22)
    b.append(T(W - M - 860 + 190, fy + 30, ["tu nombre o un apodo"], 16, GRAY, style="italic", anchor="middle"))  # TEXTO NUEVO
    campo(b, x1 + 30, fy, "promoción", 150, GRAY, 22)                                                 # TEXTO NUEVO
    BT.pie_b(b, P2, PSI, texto="Cuaderno de trabajo · Saber 11 · cierre")
    return b


# ═════════════════════════════ 398 · MENSAJE FINAL ═════════════════════════════
FRASE = ("Llegaste hasta aquí escribiendo cómo pensabas,",                                            # TEXTO NUEVO
         "no solo qué marcabas.")
REMATE = "Eso ya es tuyo. Ningún puntaje te lo quita."                                                # TEXTO NUEVO
PROMPT = "Lo que me diría hoy, al terminar"                                                           # TEXTO NUEVO
PROMPT_AYUDA = "a quien llegó el primer sábado, o a quien sale hoy por esa puerta"                   # TEXTO NUEVO


def pagina_3():
    """Moderna y minimalista: sin cabecera ni cuadrícula en toda la página; solo la frase, un
    espacio grande (con la cuadrícula de puntos adentro, para escribir) y, abajo y pequeño, la
    fecha y las caritas por última vez."""
    b = svg_open()
    # la frase
    s = fit(FRASE[0], 76, SHA, "800", CW - 80)
    y = 430
    b.append(estrellita(M + 30, y - 150, 22, PSI, 3.2))
    marca = "cómo pensabas"
    i = FRASE[0].index(marca)
    x2 = M + twf(FRASE[0][:i], s, SHA, "800")
    b.append(resaltador(x2, y - s * 0.78, twf(marca, s, SHA, "800"), s * 0.8, FOSFO, seed=991, rot=-1))
    b.append(TX(M, y, FRASE[0], s, TINTA_B, SHA, "800"))
    b.append(TX(M, y + s * 1.25, FRASE[1], s, TINTA_B, SHA, "800"))
    b.append(TX(M, y + s * 1.25 + 92, REMATE, 40, PSI, SHA, "400"))
    # el espacio grande
    by, bh = 840, 1220
    b.append(TX(M, by - 34, PROMPT, 44, TINTA_B, SHA, "800"))
    b.append(T(M + twf(PROMPT, 44, SHA, "800") + 24, by - 36, [PROMPT_AYUDA], 22, GRAY, style="italic"))
    b.append(BT.puntos(M + 40, by + 40, W - M - 40, by + bh - 40, 40))
    b.append(wob_rect(M, by, CW, bh, TINTA_B, 3, fill="none", seed=992, amp=1.6))
    # abajo, pequeño: la fecha y las caritas por última vez
    fy = by + bh + 120
    campo(b, M, fy, "Cerré este cuaderno el", 300, GRAY, 22)                                         # TEXTO NUEVO
    xs = W - M - 820
    for k, (lab, x0) in enumerate((("EL PRIMER SÁBADO LLEGUÉ", xs), ("HOY SALGO", xs + 500))):        # TEXTO NUEVO
        b.append(TX(x0, fy - 52, lab, 14, GRAY, MONO, "700"))
        for j, mood in enumerate(["worried", "calm", "happy"]):
            b.append(face(x0 + 26 + j * 70, fy - 4, 24, mood, TINTA_B, "white", sw=2.2))
    BT.pie_b(b, P3, PSI, texto="Cuaderno de trabajo · Saber 11")
    return b


PAGINAS = [pagina_1, pagina_2, pagina_3]


def construir():
    rutas = []
    for k, f in enumerate(PAGINAS, 1):
        r = LIBRO + f"cierre_b_{k}.svg"
        svg_close(f(), r)
        rutas.append(r)
    return rutas


if __name__ == "__main__":
    import render
    rutas = construir()
    os.makedirs("/tmp/claude-0/cierre_b", exist_ok=True)
    pdf = render.unir(rutas, "/tmp/claude-0/cierre_b/Cierre_B.pdf")
    print(pdf, render.verifica(pdf, "Aprende"))
