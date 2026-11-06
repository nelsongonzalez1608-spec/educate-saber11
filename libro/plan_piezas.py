#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Piezas comunes de los planeadores del docente, una por área.

Salió de plan_mate.py: la primera versión tenía el motor y los datos en el mismo
archivo, y copiarlo seis veces habría dejado seis motores que se van separando.
Aquí vive solo el dibujo; los datos de cada área van en su propio plan_<área>.py.

Reglas que respeta: ninguna línea horizontal decorativa (la cabecera es una banda
sólida y los acentos de los recuadros son verticales), texto justificado medido con
la fuente real y EDUCATE siempre en mayúsculas sostenidas.
"""
from lib import *

OUT = "/home/claude/libro/"

# El oro institucional no contrasta sobre la banda oscura de la cabecera.
ORO = "#C9821B"; ORO_BG = "#FDF5E7"; ORO_LN = "#E8CFA3"; ORO_CLARO = "#E8B65F"
ROJO = "#A82424"; ROJO_BG = "#FBEFEF"; ROJO_LN = "#E6C4C4"
VERDE = "#2E7A39"; VERDE_BG = "#EDF5EE"; VERDE_LN = "#C3DEC8"
MORADO = "#5B3E96"; MORADO_BG = "#F3F0FB"; MORADO_LN = "#D6CCEE"
PIZ = "#28313F"

SEV = {"alta": (ROJO, ROJO_BG, ROJO_LN), "media": (ORO, ORO_BG, ORO_LN),
       "baja": ("#1F4E8C", "#EEF3FA", "#C6D6EA"), "atención": (VERDE, VERDE_BG, VERDE_LN)}

# Lo pone cada área con configurar(). Arranca en el azul de Matemáticas.
A = "#1F4E8C"; A_BG = "#EEF3FA"; A_LN = "#C6D6EA"
AREA = "Matemáticas"; TOT = 24


def configurar(color, bg, ln, nombre_area, total_hojas):
    """Fija el color del área y su nombre para toda la construcción."""
    global A, A_BG, A_LN, AREA, TOT
    A, A_BG, A_LN, AREA, TOT = color, bg, ln, nombre_area, total_hojas


def cabecera(body, titulo_, sub, etiqueta="PLANEADOR DEL DOCENTE",
             derecha=None, dsub=None, campos=False):
    """Banda sólida de identificación. No es una línea: es un bloque."""
    h = 268 if campos else 200
    body.append(rect(M, 48, CW, h, PIZ, r=22))
    body.append(f'<circle cx="{W-200}" cy="90" r="150" fill="white" opacity="0.045"/>')
    body.append(logo(M + 42, 86, 62, chip=True, pad=12))
    lx = M + 42 + logo_w(62) + 40
    chip(body, lx, 80, etiqueta, ORO, size=19, pad=17, txtc="#3A2602")
    body.append(T(lx, 168, [titulo_], 46, "white", weight="700"))
    body.append(T(lx, 206, [sub], 23, "#A9B5C6"))
    if derecha:
        body.append(T(W - M - 42, 124, [derecha], 44, ORO_CLARO, weight="700", anchor="end"))
        body.append(T(W - M - 42, 156, [dsub or ""], 19, "#AEBACB", anchor="end"))
    if campos:
        cx = lx
        for lab, an in [("DOCENTE", 520), ("GRUPO", 240), ("FECHA", 250)]:
            body.append(T(cx, 250, [lab], 16, "#8D9BAE", ls=1))
            body.append(line(cx, 266, cx + an, 266, "#6E7C8E", 2, "7,7"))
            cx += an + 44
    return 48 + h + 44


def pie(body, pag):
    y = H_PAGE - 96
    body.append(rect(M, y - 16, CW, 76, A_BG, r=18))
    body.append(T(M + 30, y + 30, ["PLANEADOR DEL DOCENTE"], 19, A, weight="700", ls=1.6))
    body.append(f'<circle cx="{M+330}" cy="{y+23}" r="5" fill="{ORO}"/>')
    body.append(T(M + 352, y + 30,
                  ["el cuaderno del estudiante es tu instrumento de seguimiento"], 19, GRAY))
    body.append(T(W - M - 30, y + 30, [f"{AREA} · hoja {pag} de {TOT}"], 19, GRAY, anchor="end"))


def seccion(body, y, txt, sub=None, color=None):
    body.append(T(M, y + 30, [txt.upper()], 23, color or A, weight="700", ls=2.2))
    y += 46
    if sub:
        y = parrafo_j(body, M, y, sub, CW, 25, GRAY, style="italic") + 10
    return y + 8


def nota(body, x, y, w, texto, color=None, bg=None, ln=None, rotulo=None, size=24):
    """Recuadro de aviso. Mide su propio alto con la fuente real."""
    color = color or A; bg = bg or A_BG; ln = ln or A_LN
    pad = 24
    lineas = wrap_px(texto, size, w - pad * 2 - 14)
    h = pad * 2 + (34 if rotulo else 0) + len(lineas) * size * 1.42
    body.append(rect(x, y, w, h, bg, r=16, stroke=ln, sw=2))
    body.append(rect(x + 12, y + 12, 5, h - 24, color, r=3))
    yy = y + pad
    if rotulo:
        body.append(T(x + pad + 14, yy + 20, [rotulo.upper()], 19, color, weight="700", ls=1.4))
        yy += 34
    parrafo_j(body, x + pad + 14, yy - 6, texto, w - pad * 2 - 14, size, INK)
    return y + h


def encabezado_tabla(body, y, columnas, alto=50):
    """columnas: lista de (x, rótulo). Devuelve el y de la primera fila."""
    body.append(rect(M, y, CW, alto, PIZ, r=12))
    for x, e in columnas:
        body.append(T(x + 18, y + alto * 0.66, [e], 17, "white", weight="700", ls=1.2))
    return y + alto + 8


def barra_tiempo(body, y, fases):
    """El reparto de los 120 minutos, en bloques sólidos."""
    tot = sum(f[1] for f in fases)
    x = M
    for i, f in enumerate(fases):
        mins, c = f[1], f[2]
        an = CW * mins / tot
        body.append(rect(x + (0 if i == 0 else 2), y, an - 4, 42, c, r=10))
        body.append(T(x + an / 2, y + 29, [f"{mins}'"], 21, "white", weight="700",
                      anchor="middle"))
        x += an
    return y + 42 + 26


def bloque_momento(body, y, n, fase):
    """Un momento de la clase, con su objetivo, las dos columnas y TU APORTE.
       fase = (nombre, minutos, color, objetivo, [qué hace], cómo lo hace, material)"""
    nom, mins, c, obj, hace, como, material = fase
    l_obj = wrap_px(obj, 24, CW - 90)
    anc = (CW - 100) / 2
    l_como = wrap_px(como, 22, anc - 20)
    lin_hace = sum(len(wrap_px(h_, 22, anc - 60)) for h_ in hace)
    alto_cols = max(lin_hace * 31 + len(hace) * 16, len(l_como) * 31) + 44
    # 128 de cabecera del momento + 26 hasta el párrafo + objetivo + 20 de aire
    # + las dos columnas + 70 de TU APORTE + 20 de respiro al borde.
    h = 264 + len(l_obj) * 34.08 + alto_cols

    body.append(rect(M, y, CW, h, "white", r=20, stroke=A_LN, sw=2.2))
    body.append(rect(M + 16, y + 18, 5, h - 36, c, r=3))
    body.append(f'<circle cx="{M+76}" cy="{y+52}" r="26" fill="{c}"/>')
    body.append(T(M + 76, y + 61, [str(n)], 27, "white", weight="700", anchor="middle"))
    body.append(T(M + 124, y + 62, [nom], 29, INK, weight="700"))
    wch = chip(body, M + 124, y + 78, f"{mins} min", c, size=19, pad=16)
    body.append(T(M + 124 + wch + 20, y + 102, ["· " + material], 20, GRAY, style="italic"))

    yy = y + 128
    body.append(T(M + 44, yy + 18, ["OBJETIVO ESPECÍFICO"], 17, c, weight="700", ls=1.4))
    yy = parrafo_j(body, M + 44, yy + 26, obj, CW - 90, 24, INK) + 20

    body.append(T(M + 44, yy + 18, ["QUÉ HACE EL DOCENTE"], 17, c, weight="700", ls=1.4))
    body.append(T(M + 60 + anc + 40, yy + 18, ["CÓMO LO HACE"], 17, c, weight="700", ls=1.4))
    body.append(line(M + 44 + anc + 20, yy + 34, M + 44 + anc + 20, yy + alto_cols - 4,
                     "#E6EAF0", 2))
    yh = yy + 30
    for h_ in hace:
        body.append(f'<circle cx="{M+56}" cy="{yh+18}" r="5.5" fill="{c}"/>')
        yh = parrafo_j(body, M + 80, yh, h_, anc - 60, 22, INK, lh=31) + 16
    parrafo_j(body, M + 60 + anc + 40, yy + 30, como, anc - 20, 22, GRAY, style="italic", lh=31)
    yy += alto_cols

    # TU APORTE: el espacio declarado y acotado del docente.
    body.append(rect(M + 44, yy, CW - 88, 70, ORO_BG, r=14, stroke=ORO_LN, sw=2))
    body.append(T(M + 68, yy + 28, ["TU APORTE"], 18, ORO, weight="700", ls=1.4))
    body.append(T(M + 68, yy + 52, ["el ejemplo, la anécdota o la variación que agregas tú "
                                    "— sin reemplazar lo de arriba"], 19, GRAY, style="italic"))
    body.append(line(M + 980, yy + 52, M + CW - 80, yy + 52, "#C9A96B", 2, "8,8"))
    return y + h + 16


def bloque_dinamica(body, y, i, din, estrategia, color):
    """din = (nombre, minutos, [pasos], qué entrena, material)"""
    nom, mins, pasos, entrena, material = din
    anc = (CW - 100) / 2
    lin_p = sum(len(wrap_px(p_, 22, anc - 60)) for p_ in pasos)
    l_ent = wrap_px(entrena, 22, anc - 20)
    alto_cols = max(lin_p * 31 + len(pasos) * 16, len(l_ent) * 31 + 34) + 30
    h = 128 + alto_cols

    body.append(rect(M, y, CW, h, "white", r=20, stroke=A_LN, sw=2.2))
    body.append(rect(M + 16, y + 18, 5, h - 36, color, r=3))
    w = chip(body, M + 44, y + 34, f"E{i+1}", color, size=19, pad=19)
    body.append(T(M + 44 + w + 26, y + 60, [nom], 27, INK, weight="700"))
    wm = chip(body, M + 44 + w + 26, y + 76, f"{mins} min", color, size=18, pad=15)
    body.append(T(M + 44 + w + 26 + wm + 18, y + 100,
                  [f"· entrena la estrategia «{estrategia}»"], 20, GRAY, style="italic"))
    body.append(T(W - M - 44, y + 48, [material], 19, GRAY, anchor="end"))

    yy = y + 120
    body.append(T(M + 44, yy + 18, ["CÓMO SE HACE"], 17, color, weight="700", ls=1.4))
    body.append(T(M + 60 + anc + 40, yy + 18, ["QUÉ MOVIMIENTO MENTAL ENTRENA"], 17, color,
                  weight="700", ls=1.4))
    body.append(line(M + 44 + anc + 20, yy + 34, M + 44 + anc + 20, y + h - 22, "#E6EAF0", 2))
    yp = yy + 30
    for p_ in pasos:
        body.append(f'<circle cx="{M+56}" cy="{yp+18}" r="5.5" fill="{color}"/>')
        yp = parrafo_j(body, M + 80, yp, p_, anc - 60, 22, INK, lh=31) + 16
    parrafo_j(body, M + 60 + anc + 40, yy + 30, entrena, anc - 20, 22, INK, lh=31)
    return y + h + 14


def bloque_reto(body, y, mis, reto):
    nom_r, min_r, txt_r = reto
    lin = wrap_px(txt_r, 23, CW - 90)
    h = 112 + len(lin) * 32
    body.append(rect(M, y, CW, h, MORADO_BG, r=20, stroke=MORADO_LN, sw=2.2))
    body.append(rect(M + 16, y + 18, 5, h - 36, MORADO, r=3))
    body.append(T(M + 44, y + 54, [f"Reto del corte · {nom_r}"], 26, MORADO, weight="700"))
    body.append(T(M + 44, y + 86, [f"{min_r} min · trabajo en equipo, registro individual"],
                  20, GRAY, style="italic"))
    parrafo_j(body, M + 44, y + 98, txt_r, CW - 90, 23, INK, lh=32)
    return y + h


def registro_docente(body, y, campos=None, alto=232):
    """Las cuatro casillas que el docente llena el mismo sábado, antes de salir."""
    campos = campos or [
        ("¿Qué pregunta tuvo que volver a explicarse?", "y con qué palabras funcionó la segunda vez"),
        ("¿A quién hay que volver la próxima clase?", "nombres, no «algunos»"),
        ("¿Qué cuaderno quedó con el andamiaje vacío?", "aunque haya acertado la respuesta"),
        ("¿Qué cambiarías de esta clase?", "va al reporte de los especialistas")]
    an = (CW - 16) / 2
    for i, (t, sub_) in enumerate(campos):
        x = M + (i % 2) * (an + 16)
        yy = y + (i // 2) * (alto + 14)
        body.append(rect(x, yy, an, alto, "white", r=16, stroke=A_LN, sw=2))
        body.append(rect(x + 14, yy + 14, 5, alto - 28, A, r=3))
        body.append(T(x + 40, yy + 44, [t], 23, INK, weight="700"))
        body.append(T(x + 40, yy + 74, [sub_], 20, GRAY, style="italic"))
        body.append(wlines(x + 40, yy + 118, an - 80, max(1, int((alto - 118) // 38)),
                           c="#E6EAF0", step=38))
    return y + (alto + 14) * ((len(campos) + 1) // 2) - 14
