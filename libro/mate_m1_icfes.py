#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MATEMÁTICAS · Momento 1 · Entrenamiento ICFES — una hoja por estrategia, después del bloque del taller.
Preguntas Saber 11, cada una con su propio instrumento. Membrete (regla 7, Nelson 10 nov):
siempre «Pregunta Saber 11», sin año ni «oficial»."""
import math, random, sys
sys.path.insert(0, "/home/claude/cuaderno")
from lib import *
from mate_m1 import EST, BLK_H, IW, RX_OFF, AZm, AZm_L, AZm_BG, hoja_header, cuenta
import datos as D

random.seed(11)
OUT = "/home/claude/libro/"
IMG = "/home/claude/cuaderno/"


def membrete(b, x, y, txt):
    txt = "Pregunta Saber 11"          # regla 7 (10 nov): el dato de datos.py se ignora
    w = len(txt) * 11.4 + 60
    b.append(rect(x, y, w, 44, "white", r=10, stroke=AZ_D, sw=2.2))
    b.append(rect(x, y, 14, 44, AZ_D, r=7))
    b.append(T(x + 30, y + 29, [txt], 19, AZ_D, weight="700"))
    return w


def opciones(b, x, y, w, ops, size=19):
    yy = y
    for k, o in enumerate(ops):
        b.append(f'<circle cx="{x+16}" cy="{yy+8}" r="15" fill="white" stroke="{AZm}" stroke-width="2"/>')
        b.append(T(x + 16, yy + 14, ["ABCD"[k]], 16, AZm, weight="700", anchor="middle"))
        svg, y2 = TJ(x + 44, yy - 6, o, w - 50, size, INK, lh=size + 7)
        b.append(svg)
        yy = y2 + 14
    return yy


def bloque_icfes(b, y, est, q, idx, instrumento):
    enm, ec = EST[est]
    b.append(rect(M, y, CW, BLK_H, "white", r=26, stroke=AZm_L, sw=2.4))
    b.append(rect(M, y, CW, 104, AZm_BG, r=26)); b.append(rect(M, y + 60, CW, 44, AZm_BG, r=0))
    b.append(f'<rect x="{M+28}" y="{y+22}" width="60" height="60" rx="12" fill="{ec}"/>')
    b.append(T(M + 58, y + 62, ["✔"], 30, "white", weight="700", anchor="middle"))
    b.append(T(M + 112, y + 44, [f"Pregunta para entrenar · {idx} de 2"], 24, AZm, weight="700"))
    b.append(T(M + 112, y + 78, [f"entrena lo mismo que la estrategia {est}: {enm.lower()}"], 21, GRAY, style="italic"))
    membrete(b, M + 900, y + 30, q["f"])
    b.append(T(M + 1500, y + 44, ["Mi primera idea:"], 20, GRAY)); b.append(line(M + 1500, y + 86, W - M - 30, y + 86, LGRAY, 2.2))

    ix, iy = M + 30, y + 130
    has_img = bool(q.get("img")); has_tab = bool(q.get("tabla"))
    wide = has_img and q["img"] == "icfes_temp.png"
    tw = IW if (wide or not has_img) else 680
    svg, yy = TJ(ix, iy, q["e"], tw - 20, 20, INK, lh=28)
    b.append(svg); yy += 10
    if wide:
        iw_, ih = 940, 380
        b.append(rect(ix + (IW - iw_) / 2, yy, iw_, ih, "white", r=10, stroke="#E1E6EC", sw=1.6))
        b.append(img(IMG + q["img"], ix + (IW - iw_) / 2 + 10, yy + 10, iw_ - 20, ih - 20)); yy += ih + 14
    elif has_img:
        ih = q["h"]; iw_ = IW - tw - 30
        b.append(rect(ix + tw + 30, iy, iw_, ih, "white", r=10, stroke="#E1E6EC", sw=1.6))
        b.append(img(IMG + q["img"], ix + tw + 40, iy + 10, iw_ - 20, ih - 20))
    if has_tab:
        b.append(q["tabla"]["draw"](ix, yy, IW)); yy += q["tabla"]["h"] + 14
    yy = opciones(b, ix, yy, tw - 20, q["o"])
    yy = max(yy, iy + (q["h"] + 20 if (has_img and not wide) else 0)) + 14
    y_end = instrumento(b, ix, yy, IW, y + BLK_H - 30 - yy)
    rest = y + BLK_H - 30 - y_end
    if rest >= 150:
        cuenta(b, ix, y_end, IW, rest - 10, "mis cuentas")

    # columna derecha (igual que el taller)
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
    sy = ry + 230
    b.append(rect(rx, sy, rw, 300, AZ_D, r=18)); b.append(buoy(rx + 36, sy + 36, 13))
    b.append(T(rx + 62, sy + 43, ["SALVAVIDAS"], 18, "white", weight="700", ls=2))
    b.append(T(rx + 24, sy + 90, ["Lo mínimo que sí tenía claro:"], 18, "#BFD4F2")); b.append(line(rx + 24, sy + 130, rx + rw - 24, sy + 130, "white", 1.6, "6,6"))
    b.append(T(rx + 24, sy + 176, ["→ entonces tenía que ser"], 18, "#BFD4F2")); b.append(line(rx + 24, sy + 216, rx + rw - 24, sy + 216, "white", 1.6, "6,6"))
    b.append(T(rx + 24, sy + 258, ["y no podía ser ____ porque"], 18, "#BFD4F2")); b.append(line(rx + 290, sy + 262, rx + rw - 24, sy + 262, "white", 1.6, "6,6"))
    ly = sy + 340
    b.append(T(rx, ly + 20, ["¿En qué se parece a la del taller?"], 20, AZm, weight="700"))
    b.append(T(rx, ly + 48, ["(misma estrategia, otro disfraz: ¿cuál fue el disfraz?)"], 16, GRAY, style="italic"))
    b.append(wlines(rx, ly + 100, rw, 4, c="#E3E8EF", step=48))
    b.append(f'<circle cx="{W-M-60}" cy="{y+BLK_H-50}" r="18" fill="{ec}"/>')
    b.append(T(W - M - 60, y + BLK_H - 43, [str(est)], 18, "white", weight="700", anchor="middle"))


def tit(b, x, y, t, c):
    b.append(rect(x, y, IW, 4, c, r=2)); b.append(T(x, y + 40, [t], 24, c, weight="700")); return y + 60


# ═══════════ instrumentos ICFES ═══════════
def i_ciudades(b, x, y, w, h):
    yy = tit(b, x, y, "La tabla de récords — antes de leer las opciones, saca los datos que sí se ven", EDU_AZUL)
    cols = ["Ciudad", "Máxima (°C) y hora", "Mínima (°C) y hora", "¿Sube y baja, o solo sube?"]
    cw_ = [120, 320, 320, 420]
    tx = x
    for i, c_ in enumerate(cols):
        b.append(rect(tx, yy, cw_[i] - 6, 40, EDU_AZUL, r=8)); b.append(T(tx + 12, yy + 27, [c_], 16, "white", weight="700")); tx += cw_[i]
    for r in range(3):
        ry = yy + 46 + r * 46; tx = x
        for i in range(4):
            b.append(rect(tx, ry, cw_[i] - 6, 40, SOFT if i == 0 else "white", r=8, stroke=AZm_L, sw=1.4))
            if i == 0: b.append(T(tx + cw_[i] / 2, ry + 27, [f"Ciudad {r+1}"], 17, INK, anchor="middle"))
            tx += cw_[i]
    b.append(T(x, yy + 46 + 3 * 46 + 30, ["Ahora cada opción: «siempre» se cae con un solo momento en contra; «máxima menor que mínima» se mira en la tabla.  Táchalas:  A  B  C  D"], 17, INK))
    return yy + 46 + 3 * 46 + 50


def i_cruce(b, x, y, w, h):
    yy = tit(b, x, y, "El punto de cruce — ¿qué significa que dos líneas se toquen?", EDU_AZUL)
    b.append(T(x, yy + 22, ["Las dos líneas se cruzan en:  hora ______   distancia ______ km.   Antes del cruce iba adelante el avión ____; después, el ____."], 18, INK))
    b.append(T(x, yy + 60, ["Cruzarse significa que en ese instante los dos llevan ______________________.  ¿Eso es lo que afirma el empleado?   sí / no"], 18, INK))
    b.append(rect(x, yy + 90, w - 20, 120, AMBER_BG, r=12, stroke=AMBER_LN, sw=2))
    b.append(T(x + 16, yy + 124, ["Cuidado con la razón: dos opciones dicen «correcta». Una da la razón verdadera (se cruzan) y otra una razón"], 17, AMBER_D, weight="700"))
    b.append(T(x + 16, yy + 150, ["inventada (la mitad del viaje). Verifica en la gráfica: ¿600 km es la mitad del recorrido total?  ____"], 17, AMBER_D, weight="700"))
    b.append(T(x + 16, yy + 190, ["Si una opción tiene el veredicto bien y la razón mal, está mal."], 16, GRAY, style="italic"))
    return yy + 220


def i_salario(b, x, y, w, h):
    yy = tit(b, x, y, "Lo fijo y lo que crece — separa las dos partes antes de armar la fórmula", EDU_VERDE)
    b.append(rect(x, yy, 380, 110, "white", r=12, stroke=EDU_VERDE, sw=2)); b.append(T(x + 16, yy + 34, ["LO FIJO (lo tiene desde el día uno)"], 15, EDU_VERDE, weight="700")); b.append(T(x + 16, yy + 84, ["$ __________"], 24, INK))
    b.append(T(x + 400, yy + 70, ["+"], 40, EDU_VERDE, weight="700"))
    b.append(rect(x + 450, yy, 480, 110, "white", r=12, stroke=EDU_VERDE, sw=2)); b.append(T(x + 466, yy + 34, ["LO QUE CRECE (por cada año)"], 15, EDU_VERDE, weight="700")); b.append(T(x + 466, yy + 84, ["$ ________  ×  años"], 24, INK))
    b.append(T(x + 950, yy + 70, ["= salario"], 24, INK))
    b.append(T(x, yy + 150, ["Pruébala con alguien de 2 años de experiencia:  ________ + ________ × 2  =  ________.  ¿Suena a un salario razonable?"], 18, INK))
    b.append(T(x, yy + 186, ["Las opciones que multiplican el básico, o que suman los años como si fueran pesos, se tachan:   A  B  C  D"], 18, INK))
    return yy + 210


def i_tasa(b, x, y, w, h):
    yy = tit(b, x, y, "La tasa de cambio — una razón constante disfrazada de dinero", EDU_VERDE)
    b.append(T(x, yy + 22, ["1 dólar  →  ________ pesos          6 dólares  →  6 × ________  =  ________ pesos"], 20, INK))
    b.append(rect(x, yy + 54, w - 20, 100, AMBER_BG, r=12, stroke=AMBER_LN, sw=2))
    b.append(T(x + 16, yy + 88, ["Antes de calcular, estima: si UN dólar ya son 3.000 pesos, ¿seis dólares deben ser más o menos que 3.000?  ______"], 17, AMBER_D, weight="700"))
    b.append(T(x + 16, yy + 118, ["Con eso ya se caen dos opciones sin hacer una sola cuenta.  ¿Cuáles?  ____  ____"], 17, AMBER_D, weight="700"))
    b.append(T(x, yy + 190, ["¿Se parece a la cinta del deportista de la pregunta 2?  Cada ______ equivale a ______, igual que cada segundo eran 5 m."], 18, INK))
    return yy + 214


def i_monedas(b, x, y, w, h):
    yy = tit(b, x, y, "Caminar hacia atrás — si para avanzar se multiplica, para devolverse se…", EDU_ORO)
    dias = [("viernes", "512"), ("jueves", ""), ("miércoles", "")]
    for i, (d, v) in enumerate(dias):
        bx = x + i * 330
        b.append(rect(bx, yy + 10, 220, 90, "white", r=12, stroke=EDU_ORO, sw=2)); b.append(T(bx + 110, yy + 40, [d], 17, GRAY, anchor="middle"))
        if v: b.append(PT(bx + 110, yy + 84, [v], 28, PENCIL, rot=-1, anchor="middle"))
        else: b.append(T(bx + 110, yy + 82, ["______"], 26, INK, anchor="middle"))
        if i < 2:
            b.append(hand_arrow(bx + 236, yy + 55, bx + 316, yy + 55, EDU_ORO, sw=3, bend=-0.3, head=16))
            b.append(T(bx + 276, yy + 30, ["÷ 2"], 18, EDU_ORO, weight="700", anchor="middle"))
    b.append(rect(x + 1000, yy + 10, w - 1020, 90, "white", r=12, stroke=EDU_ROJO, sw=2, dash="7,5"))
    b.append(T(x + 1016, yy + 44, ["La trampa: 512 − 4 = 508."], 16, EDU_ROJO, weight="700")); b.append(T(x + 1016, yy + 72, ["¿por qué restar no sirve aquí?"], 15, GRAY, style="italic"))
    b.append(T(x, yy + 140, ["Compruébalo hacia adelante: ______ (mié) × 2 = ______ (jue) × 2 = 512 (vie).   ¿Cuadra?  sí / no"], 18, INK))
    b.append(T(x, yy + 176, ["¿Se parece a la máquina × 1,02 de Camilo? Allá el factor era 1,02; aquí es ______. Las dos son crecimiento que se acumula."], 17, GRAY, style="italic"))
    return yy + 200


def i_rosendo(b, x, y, w, h):
    yy = tit(b, x, y, "La tabla continúa — el interés no es fijo: es 10 % de lo que falta por pagar", EDU_ORO)
    b.append(T(x, yy + 22, ["Mes 3 →  saldo: ________    10 % de ese saldo: ________    + aporte 40.000  =  cuota: ________"], 19, INK))
    b.append(T(x, yy + 58, ["Mes 4 →  saldo: ________    10 % de ese saldo: ________    + aporte 40.000  =  cuota: ________   (para comprobar el patrón)"], 19, INK))
    b.append(rect(x, yy + 90, w - 20, 90, AMBER_BG, r=12, stroke=AMBER_LN, sw=2))
    b.append(T(x + 16, yy + 124, ["Mira las cuotas: 60.000 → 56.000 → ______.  ¿Bajan de a cuánto?  ______.  ¿Por qué de a eso y no de a otra cosa?"], 17, AMBER_D, weight="700"))
    b.append(T(x + 16, yy + 154, ["(pista: el saldo baja 40.000 y el 10 % de 40.000 es…)"], 16, GRAY, style="italic"))
    b.append(T(x, yy + 214, ["Trampa: la C (56.000) es la cuota del mes 2, que ya está en la tabla. La pregunta pide el mes 3."], 17, EDU_ROJO))
    return yy + 240


def i_documentales(b, x, y, w, h):
    yy = tit(b, x, y, "Un solo día basta — «todos los días» se derrumba con un contraejemplo", EDU_ROJO)
    b.append(T(x, yy + 22, ["Escoge un día cualquiera de la gráfica:  día ____  →  P marca ______   Q marca ______.   ¿Quién va arriba?  ____"], 19, INK))
    b.append(T(x, yy + 58, ["Prueba con otro día:  día ____  →  P ______   Q ______.   ¿Cambia quién va arriba, o es siempre el mismo?  ______"], 19, INK))
    b.append(T(x, yy + 94, ["¿A qué distancia va una línea de la otra?  ______ puntos.   Entonces: P(x) = Q(x) ____ 20   (escribe + o −)"], 19, INK))
    b.append(rect(x, yy + 126, w - 20, 100, AMBER_BG, r=12, stroke=AMBER_LN, sw=2))
    b.append(T(x + 16, yy + 160, ["La conclusión del empleado dice que Q fue mayor TODOS los días. Con lo que escribiste arriba: ¿es verdadera?  sí / no"], 17, AMBER_D, weight="700"))
    b.append(T(x + 16, yy + 190, ["Ahora las razones: dos opciones hablan de «dominio» y «rango» — palabras elegantes que no responden la pregunta. Tacha esas dos."], 16, AMBER_D, weight="700"))
    b.append(T(x, yy + 260, ["Es el mismo truco del cazador de afirmaciones (pregunta 9): las palabras «siempre», «todos», «nunca» se prueban con un solo caso."], 17, GRAY, style="italic"))
    return yy + 284


def i_veredicto(b, x, y, w, h):
    yy = tit(b, x, y, "Veredicto y razón — una opción solo es correcta si acierta en las dos columnas", EDU_ROJO)
    cols = ["Opción", "Veredicto que da", "¿El veredicto es verdadero?", "Razón que da", "¿La razón es verdadera?"]
    cw_ = [90, 220, 280, 360, 300]
    tx = x
    for i, c_ in enumerate(cols):
        b.append(rect(tx, yy, cw_[i] - 6, 40, EDU_ROJO, r=8)); b.append(T(tx + 10, yy + 27, [c_], 14, "white", weight="700")); tx += cw_[i]
    razones = ["solo al final", "se cruzan", "uno recorre más", "mitad del viaje"]
    for r, L in enumerate("ABCD"):
        ry = yy + 46 + r * 44; tx = x
        for i in range(5):
            b.append(rect(tx, ry, cw_[i] - 6, 38, SOFT if i == 0 else "white", r=8, stroke=AZm_L, sw=1.4))
            if i == 0: b.append(T(tx + cw_[i] / 2, ry + 26, [L], 18, INK, weight="700", anchor="middle"))
            elif i == 1: b.append(T(tx + 12, ry + 26, ["incorrecta" if r in (0, 2) else "correcta"], 16, GRAY))
            elif i == 3: b.append(T(tx + 12, ry + 26, [razones[r]], 16, GRAY))
            else:
                b.append(T(tx + 20, ry + 26, ["sí"], 15, GRAY)); b.append(checkbox(tx + 50, ry + 9, s=9)); b.append(T(tx + 110, ry + 26, ["no"], 15, GRAY)); b.append(checkbox(tx + 144, ry + 9, s=9))
            tx += cw_[i]
    b.append(T(x, yy + 46 + 4 * 44 + 28, ["La única con dos «sí» es la respuesta. Esta pregunta ya la viste en la hoja de la estrategia 1: ¿marcaste lo mismo? Si no, ¿qué cambió en tu cabeza?"], 16, GRAY, style="italic"))
    return yy + 46 + 4 * 44 + 50


INSTR = {1: [i_ciudades, i_cruce], 2: [i_salario, i_tasa], 3: [i_monedas, i_rosendo], 4: [i_documentales, i_veredicto]}


def build_icfes(est, pag):
    qs = D.ICFES[est]; enm, ec = EST[est]
    b = svg_open()
    hoja_header(b, pag, f"Entrenamiento ICFES · estrategia {est}: {enm}")
    for k, q in enumerate(qs):
        bloque_icfes(b, 210 + k * (BLK_H + 40), est, q, k + 1, INSTR[est][k])
    footer(b, pag, AZm, texto=f"Matemáticas · Momento 1 · entrenamiento ICFES · estrategia {est}")
    f = OUT + f"m1_e{est}.svg"; svg_close(b, f); return f


if __name__ == "__main__":
    for est, pag in [(1, 12), (2, 14), (3, 17), (4, 19)]:
        build_icfes(est, pag)
    print("ok icfes")
