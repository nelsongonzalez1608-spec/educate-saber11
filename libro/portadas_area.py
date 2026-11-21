#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portadas de área en la línea de la portada general (Nelson, 21 nov).

Arriba, una franja del color del área (hasta el borde, como la tapa): «NIVEL n DE 7», el nombre del área en grande,
sus competencias, apuntes reales de esa área en blanco tenue y SU bloque de la escalera en 3D, blanco, con su motivo,
sus 6 casillas de misión y sus páginas. Abajo, en papel claro, todo lo que se llena (es una página de trabajo y nunca
se escribe sobre fondo oscuro): el instrumento, los seis momentos con sus casillas, las ocho clases con fecha y caritas
y el puntaje del área. Los datos son los mismos de apertura3.py: este módulo reemplaza solo portada_area().

    python3 portadas_area.py      → ap10_mate.svg, ap53_lc.svg … ap268_ing.svg (las 7 portadas)
"""
import math

from lib import *                     # noqa: F401,F403
import apertura3 as A3
import bitacora as BT
import motivos
from portada_propuesta2 import _mezcla, PAGS

HERO = 860
CLAVE = {"Matemáticas": "mate", "Lectura Crítica": "lc", "Sociales": "soc", "Biología": "bio",
         "Química": "qui", "Física": "fis", "Inglés": "ing"}


def _mano(x, y, t, size=50, rot=0, op=.48):
    return (f'<text x="{x}" y="{y}" font-family="{BT.HAND}, Caveat, cursive" font-size="{size}" fill="#FFFFFF" '
            f'fill-opacity="{op}" transform="rotate({rot} {x} {y})">{t}</text>')


def _tr(d, sw=4.5, op=.45):
    return (f'<path d="{d}" fill="none" stroke="#FFFFFF" stroke-opacity="{op}" stroke-width="{sw}" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')


def apuntes(area):
    """Apuntes reales de cada área, en la franja, entre el título y el bloque (x 700–1250, y 470–720)."""
    x, y = 760, 600
    s = []
    if area == "mate":
        s += [_mano(x, y, "f(x) = 2x + 3"), _mano(x, y + 70, "f(4) = 11 ✓", 46),
              _tr(f"M{x+330} {y+150} V{y-40} M{x+330} {y+150} H{x+520}"),
              _tr(f"M{x+340} {y+130} L{x+500} {y-20}", 3.5)]
    elif area == "lc":
        s += [_mano(x, y, "tesis: «leer es dudar»", 46), _tr(f"M{x} {y+14} h420"),
              _mano(x, y + 72, "sin embargo → contraste", 44), _mano(x, y + 140, "¿quién lo dice y para qué?", 42, -2)]
    elif area == "soc":
        s += [_tr(f"M{x} {y+40} H{x+460}"), _tr(f"M{x+40} {y+20} v40 M{x+380} {y+20} v40", 4)]
        s += [_mano(x + 10, y, "1886", 42), _mano(x + 340, y, "1991", 42),
              _mano(x, y + 110, "Art. 86 → tutela", 46), _mano(x, y + 170, "causa → consecuencia", 42, -2)]
    elif area == "bio":
        s += [_mano(x, y, "Aa × Aa", 50)]
        gx, gy = x + 20, y + 30
        s += [_tr(f"M{gx} {gy} h200 v130 h-200 z M{gx+100} {gy} v130 M{gx} {gy+65} h200", 4)]
        s += [_mano(gx + 22, gy + 50, "AA", 40), _mano(gx + 122, gy + 50, "Aa", 40),
              _mano(gx + 22, gy + 115, "Aa", 40), _mano(gx + 128, gy + 115, "aa", 40),
              _mano(x + 260, y + 100, "3 : 1", 50)]
    elif area == "qui":
        s += [_mano(x, y, "2H₂ + O₂ → 2H₂O", 50), _mano(x, y + 76, "n = m / M", 48),
              _mano(x, y + 150, "18 g de H₂O = 1 mol", 42, -2)]
    elif area == "fis":
        bx, by = x + 340, y + 40
        s += [_mano(x, y, "F = m · a", 52), _mano(x, y + 76, "v = d / t", 48),
              _tr(f"M{bx} {by} h70 v70 h-70 z", 4), _tr(f"M{bx+35} {by+70} v70 m-10 -14 l10 14 l10 -14", 4),
              _tr(f"M{bx+70} {by+35} h80 m-14 -10 l14 10 l-14 10", 4), _mano(bx + 50, by + 170, "peso", 36)]
    elif area == "ing":
        s += [_mano(x, y, "I have been studying", 48), _mano(x, y + 72, "since 2020 · for 3 years", 42),
              _tr(f"M{x} {y+130} H{x+440} m-14 -10 l14 10 l-14 10"), _mano(x, y + 180, "past → now", 40)]
    return "".join(s)


def bloque_blanco(x, y, w, d, c, area, n, pags):
    """El nivel del área: un bloque blanco en 3D sobre el color del área."""
    h = w
    k = d * 0.58
    tinta = BT.TINTA_B
    s = (f'<polygon points="{x+16},{y+h+14} {x+w+d+16},{y+h-k+14} {x+w+d+16},{y-k+14}" fill="#000" fill-opacity=".14"/>'
         f'<polygon points="{x},{y} {x+d},{y-k} {x+w+d},{y-k} {x+w},{y}" fill="{_mezcla(c, .82)}" stroke="{tinta}" stroke-width="3.5" stroke-linejoin="round"/>'
         f'<polygon points="{x+w},{y} {x+w+d},{y-k} {x+w+d},{y+h-k} {x+w},{y+h}" fill="{_mezcla(c, .6)}" stroke="{tinta}" stroke-width="3.5" stroke-linejoin="round"/>'
         f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#FFFFFF" stroke="{tinta}" stroke-width="3.5"/>')
    s += motivos.motivo(area, c).replace("<svg ", f'<svg x="{x + w/2 - 110}" y="{y + 18}" width="220" height="220" ', 1)
    lado, gap = 40, 12
    x6 = x + (w - (6 * lado + 5 * gap)) / 2
    for i in range(6):
        s += (f'<rect x="{x6 + i*(lado+gap):.1f}" y="{y + h - 110}" width="{lado}" height="{lado}" rx="8" '
              f'fill="#FFFFFF" stroke="{c}" stroke-width="4"/>')
    s += BT.TX(x + 24, y + h - 26, f"NIVEL {n:02d}", 26, c, BT.MONO, "700")
    s += BT.TX(x + w - 22, y + h - 26, "6 misiones", 22, BT.TINTA_B, BT.MONO, "700", anchor="end")
    s += BT.TX(x + w / 2 + d / 2, y - k / 2 + 9, f"p. {pags}", 26, BT.TINTA_B, BT.MONO, "700", anchor="middle")
    return s


def portada_area_b(pag, n_area, nombre, c, titulo, comps, instr_titulo, instr_texto, dibujo,
                   momentos, clase_sub, clase_lab, archivo, sub_titulo=None, iw=300,
                   cajas=(EDU_ROJO, EDU_VERDE, EDU_ORO), borde_clase=None,
                   x_clase_sub=700, x_puntaje=520, paso_puntaje=330, claro=None,
                   nota_momentos="cada uno: 10 preguntas del libro + entrenamiento ICFES + simulacro"):
    area = CLAVE[nombre]
    tinte = A3._tinte(c, 0.42)
    b = svg_open()
    BT.fondo_puntos(b)
    # ── la franja del área
    b.append(rect(0, 0, W, HERO, c, r=0))
    pts = "".join(f"M{x} {y}h0" for y in range(40, HERO, 56) for x in range(60, W, 56))
    b.append(f'<path d="{pts}" stroke="#FFFFFF" stroke-opacity=".12" stroke-width="5" stroke-linecap="round"/>')
    b.append(BT.TX(M, 120, f"NIVEL {n_area:02d} DE {A3.N_AREAS:02d}", 28, "#FFFFFF", BT.MONO, "700", ls=4))
    b.append(BT.TX(W - M, 120, "CUADERNO DE TRABAJO · SABER 11", 22, "#FFFFFF", BT.MONO, "700", anchor="end", ls=2))
    tt = titulo[0] + titulo[1:].lower() if titulo.isupper() else titulo
    s_ = BT.fit(tt, 170, BT.SHA, "800", 1180)
    b.append(BT.TX(M - 6, 300, tt, s_, "#FFFFFF", BT.SHA, "800"))
    yy = 300
    if sub_titulo:
        st = sub_titulo if not sub_titulo.isupper() else sub_titulo.capitalize()
        b.append(BT.TX(M, 380, st, 66, "#FFFFFF", BT.SHA, "800"))
        yy = 380
    for k, ln in enumerate(comps):
        ss = 26
        while tw(ln, ss) > 1150 and ss > 17:
            ss -= 0.5
        b.append(T(M, yy + 70 + k * 44, [ln], ss, "#FFFFFF", weight="400"))
    b.append(apuntes(area))
    b.append(bloque_blanco(1330, 300, 400, 170, c, area, n_area, PAGS[n_area - 1]))

    # ── lo que se llena, en papel claro (misma información que antes)
    y0 = HERO + 50
    hb = 230
    b.append(BT.wob_rect(M, y0, CW, hb, BT.TINTA_B, 3, fill="white", seed=pag + 1))
    dibujo(b, M + 36, y0 + 20, iw, hb - 40)
    tx = M + 80 + iw
    b.append(BT.TX(tx, y0 + 60, instr_titulo, BT.fit(instr_titulo, 30, BT.SHA, "800", W - M - 40 - tx),
                   c, BT.SHA, "800"))
    parrafo_j(b, tx, y0 + 80, instr_texto, W - M - 40 - tx, 23, color=INK, lh=32)

    y = y0 + hb + 40
    wt = BT.twf("Tus seis momentos", 38, BT.SHA, "800")
    b.append(BT.resaltador(M, y + 14, wt, 34, BT.FOSFO, seed=pag + 2))
    b.append(BT.TX(M, y + 40, "Tus seis momentos", 38, BT.TINTA_B, BT.SHA, "800"))
    b.append(rect(M + wt + 24, y + 16, tw(nota_momentos, 23, style="italic") + 12, 34, "white", r=2))
    b.append(T(M + wt + 30, y + 40, [nota_momentos], 23, GRAY, style="italic"))
    mw = (CW - 40) / 2
    for i, (nm, comp) in enumerate(momentos):
        x = M + (i % 2) * (mw + 40); yy = y + 80 + (i // 2) * 122
        b.append(BT.wob_rect(x, yy, mw, 104, BT.TINTA_B, 2.4, fill="white", seed=pag * 10 + i))
        b.append(BT.wob_circle(x + 50, yy + 52, 30, c, 2.6, seed=i + 3))
        b.append(BT.TX(x + 50, yy + 62, f"{i + 1:02d}", 26, c, BT.MONO, "700", anchor="middle"))
        if nm:
            b.append(T(x + 104, yy + 46, [nm], 26, c, weight="700"))
            b.append(T(x + 104, yy + 80, [comp], 20, GRAY))
        else:
            b.append(line(x + 104, yy + 52, x + mw - 150, yy + 52, LGRAY, 2.4))
            b.append(T(x + 104, yy + 84, [comp or "Momento " + str(i + 1)], 20, GRAY))
        for k in range(3):
            b.append(BT.wob_rect(x + mw - 130 + k * 38, yy + 38, 22, 22, cajas[k], 2.2, fill="white",
                                 seed=i * 3 + k, amp=0.6))
    t = "CASILLAS: LIBRO · ICFES · SIMULACRO"
    b.append(rect(M - 6, y + 80 + 3 * 122 + 2, BT.twf(t, 16, BT.MONO) + 12, 26, "white", r=2))
    b.append(BT.TX(M, y + 80 + 3 * 122 + 20, t, 16, GRAY, BT.MONO))

    y = y + 80 + 3 * 122 + 50
    hc = 520
    b.append(BT.wob_rect(M, y, CW, hc, BT.TINTA_B, 3, fill="white", seed=pag + 3))
    t = f"Mis ocho clases de {nombre}"
    wt = BT.twf(t, 34, BT.SHA, "800")
    b.append(BT.resaltador(M + 40, y + 28, wt, 32, tinte, seed=pag + 4))
    b.append(BT.TX(M + 40, y + 54, t, 34, BT.TINTA_B, BT.SHA, "800"))
    xs = max(M + x_clase_sub, M + 40 + wt + 30)
    ss = 23
    while xs + tw(clase_sub, ss, style="italic") > W - M - 30 and ss > 17:
        ss -= 0.5
    b.append(T(xs, y + 54, [clase_sub], ss, GRAY, style="italic"))
    cw_ = (CW - 80 - 3 * 20) / 4
    for i in range(8):
        x = M + 40 + (i % 4) * (cw_ + 20); yy = y + 82 + (i // 4) * 210
        b.append(BT.wob_rect(x, yy, cw_, 192, A3._tinte(c, 0.55), 2.2, fill="white", seed=pag * 20 + i, amp=1))
        b.append(BT.wob_circle(x + 34, yy + 34, 22, c, 2.4, seed=i + 30))
        b.append(BT.TX(x + 34, yy + 41, str(i + 1), 20, c, BT.MONO, "700", anchor="middle"))
        b.append(T(x + 70, yy + 42, ["fecha ________"], 20, GRAY))
        for k, lab in enumerate(["llegué", "salí"]):
            fy = yy + 88 + k * 44
            b.append(T(x + 24, fy + 8, [lab], 19, GRAY))
            for m_, mood in enumerate(["worried", "calm", "happy"]):
                b.append(face(x + 110 + m_ * 54, fy, 18, mood, BT.TINTA_B, "white", sw=2))
        b.append(line(x + 24, yy + 176, x + cw_ - 24, yy + 176, LGRAY, 2))
        b.append(T(x + 24, yy + 168, [clase_lab], 16, GRAY, style="italic"))

    y += hc + 36
    b.append(BT.wob_rect(M, y, CW, 140, EDU_ORO, 3, fill="white", seed=pag + 5))
    t = f"Mi puntaje en {nombre}"
    b.append(BT.TX(M + 40, y + 58, t, BT.fit(t, 30, BT.SHA, "800", x_puntaje - 60), c if c != "#1F4E8C" else EDU_ORO,
                   BT.SHA, "800"))
    b.append(T(M + 40, y + 100, ["(de 0 a 100)"], 20, GRAY, style="italic"))
    for k, lab in enumerate(["simulacro 1", "simulacro 2", "simulacro 3", "META"]):
        x = M + x_puntaje + k * paso_puntaje
        if lab == "META":
            b.append(BT.resaltador(x, y + 38, BT.twf(lab, 22, BT.MONO, "700"), 26, BT.FOSFO, seed=pag + 6))
            b.append(BT.TX(x, y + 58, lab, 22, EDU_AZUL, BT.MONO, "700"))
        else:
            b.append(T(x, y + 58, [lab], 22, GRAY))
        b.append(line(x, y + 106, x + 260, y + 106, EDU_AZUL if lab == "META" else LGRAY, 2.6))
    assert y + 140 < H_PAGE - 130, f"{nombre}: el puntaje llega a {y + 140}"
    import paginas
    BT.pie_b(b, paginas.nueva(pag), c,
             texto=f"{nombre if not sub_titulo else nombre + ' y Ciudadanas'} · área {n_area} de {A3.N_AREAS}")
    svg_close(b, A3.OUT + archivo)


def construir():
    import random
    A3.portada_area = portada_area_b
    for f in (A3.portada_mate, A3.portada_lc, A3.portada_soc, A3.portada_bio, A3.portada_qui, A3.portada_fis):
        f()
    random.seed(41)
    A3.portada_ing()


if __name__ == "__main__":
    construir()
    print("ok · 7 portadas de área")
