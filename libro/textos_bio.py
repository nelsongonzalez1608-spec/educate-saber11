#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lee TEXTOS_BIO.md y devuelve lo de Biología que la guía de clase proyecta: las 24 preguntas de
entrenamiento (texto completo, enunciado, opciones, clave verificada, fuente y notas para el profe)
y, aparte, las figuras de esas preguntas redibujadas para la pantalla (FIGURAS).

TEXTOS_BIO.md usa el mismo formato que las secciones de Sociales de TEXTOS_GUIA_DOCENTE.md, así que
el lector es textos_soc.leer() con area="BIOLOGÍA" (textos_soc no se toca).

    from textos_bio import leer, FIGURAS
    icfes = leer()                     # {(misión, k): dict(titulo, texto, enunciado, opciones, clave, notas…)}
    FIGURAS[(1, 2)]                    # HTML de la tabla de transporte y la célula con Na⁺ y K⁺

Donde el .md dice «[[figura]]», la guía pone FIGURAS[(misión, k)]. Las figuras repiten los datos de
los módulos del cuaderno (bioN_icfes.py): tablas en HTML y esquemas en SVG en línea, sin internet.

verificar() cruza, pregunta por pregunta, la clave del .md con el docstring de bioN_icfes.py y con
tablero/icfes.csv, y las cuatro opciones con las del módulo (cuando el módulo las trae en texto).
"""
import ast, csv, html, re, unicodedata

import textos_soc

FUENTE = "/home/claude/libro/TEXTOS_BIO.md"
MARCA = "[[figura]]"
E = lambda t: html.escape(str(t), quote=False)


def leer(fuente=FUENTE):
    icfes, _, _ = textos_soc.leer(area="BIOLOGÍA", fuente=fuente)
    return icfes


# ─────────────────────────────── figuras ───────────────────────────────
TINTA = "#1B1F27"; GRIS = "#5C6472"; LINEA = "#C9CFD8"; FONDO = "#F4F7F5"; ROJO = "#A82424"
FUENTE_SVG = "font-family:'Source Sans 3','Segoe UI',system-ui,sans-serif"


def _svg(w, h, cuerpo, alt):
    return (f'<figure class="fig"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{E(alt)}" '
            f'style="{FUENTE_SVG}">{cuerpo}</svg></figure>')


def _t(x, y, txt, size=15, color=TINTA, anchor="start", bold=False, italic=False):
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" fill="{color}" text-anchor="{anchor}"'
            f'{" font-weight=\"700\"" if bold else ""}{" font-style=\"italic\"" if italic else ""}>{E(txt)}</text>')


def _flecha(x1, y1, x2, y2, c=TINTA, sw=2):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 11 * math.cos(a - 0.4), y2 - 11 * math.sin(a - 0.4))
    p2 = (x2 - 11 * math.cos(a + 0.4), y2 - 11 * math.sin(a + 0.4))
    return (f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{c}" stroke-width="{sw}"/>'
            f'<polygon points="{x2:.0f},{y2:.0f} {p1[0]:.0f},{p1[1]:.0f} {p2[0]:.0f},{p2[1]:.0f}" fill="{c}"/>')


def _tabla(cab, filas, nota=None):
    th = "".join(f"<th>{E(c)}</th>" for c in cab)
    tr = "".join("<tr>" + "".join(f"<td>{E(c)}</td>" for c in f) + "</tr>" for f in filas)
    pie = f'<figcaption>{E(nota)}</figcaption>' if nota else ""
    return f'<figure class="fig"><table class="tabla"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table>{pie}</figure>'


def fig_transporte():
    tabla = _tabla(["", "Ósmosis", "Difusión simple", "Difusión facilitada", "Transporte activo"],
                   [["Moléculas transportadas", "Agua", "Gases", "Moléculas con carga eléctrica",
                     "Moléculas con carga eléctrica"],
                    ["Dirección del transporte", "De mayor a menor concentración",
                     "De mayor a menor concentración", "De mayor a menor concentración",
                     "De menor a mayor concentración"]])
    cx, cy = 230, 120
    c = (f'<ellipse cx="{cx}" cy="{cy}" rx="130" ry="80" fill="{FONDO}" stroke="#30843C" stroke-width="2.4"/>'
         f'<circle cx="{cx+48}" cy="{cy+18}" r="28" fill="white" stroke="#30843C" stroke-width="1.8"/>')
    for px, py in ((-62, -34), (-12, -48), (-76, 12), (-30, 2), (18, -26)):
        c += _t(cx + px, cy + py, "K⁺", 16, bold=True, anchor="middle")
    c += _t(cx - 50, cy + 52, "Na⁺", 16, bold=True, anchor="middle")
    for px, py in ((-170, -76), (120, -82), (168, -26), (172, 34), (128, 96), (-168, 84)):
        c += _t(cx + px, cy + py, "Na⁺", 16, bold=True, anchor="middle")
    c += _t(cx, 236, "Ejemplo de célula animal (esquema del cuadernillo)", 13, GRIS, "middle", italic=True)
    return tabla + _svg(460, 246, c, "Célula con cinco K⁺ y un Na⁺ adentro, y seis Na⁺ afuera")


def fig_sintesis():
    c = f'<rect x="10" y="10" width="700" height="250" rx="60" fill="{FONDO}" stroke="#30843C" stroke-width="2.4"/>'
    nx, ny = 170, 128
    c += f'<circle cx="{nx}" cy="{ny}" r="96" fill="white" stroke="#30843C" stroke-width="2"/>'
    pts = " ".join(f"{nx-64+i*13},{ny-46+(11 if i % 2 else -11)}" for i in range(11))
    c += f'<polyline points="{pts}" fill="none" stroke="{TINTA}" stroke-width="2.4"/>'
    c += _t(nx - 88, ny - 64, "ADN", 15, bold=True)
    c += _flecha(nx, ny - 26, nx, ny + 12)
    c += _t(nx + 10, ny - 4, "Transcripción", 14, bold=True)
    c += _t(nx - 60, ny + 44, "ARNm", 15, bold=True)
    c += _t(nx, ny + 116, "Núcleo", 13, GRIS, "middle", italic=True)
    import math
    rx, ry = 520, 150
    ondas = " ".join(f"{nx-20+t*9:.0f},{ny+26+7*math.sin(t*0.9):.0f}" for t in range(int((rx - 50 - nx + 20) / 9)))
    c += f'<polyline points="{ondas}" fill="none" stroke="{TINTA}" stroke-width="2.4"/>'
    c += (f'<ellipse cx="{rx}" cy="{ry-22}" rx="54" ry="32" fill="white" stroke="{TINTA}" stroke-width="2"/>'
          f'<ellipse cx="{rx}" cy="{ry+16}" rx="44" ry="20" fill="white" stroke="{TINTA}" stroke-width="2"/>')
    c += _t(rx + 62, ry - 46, "Ribosoma", 15, bold=True)
    for k in range(5):
        c += f'<circle cx="{rx-28-k*24}" cy="{ry-66-k*6}" r="9" fill="white" stroke="{TINTA}" stroke-width="1.8"/>'
    c += _t(rx - 180, ry - 104, "Proteína", 15, bold=True)
    ax, ay = rx + 120, ry + 24
    c += (f'<circle cx="{ax}" cy="{ay}" r="9" fill="white" stroke="{TINTA}" stroke-width="1.8"/>'
          f'<path d="M {ax-11} {ay+14} L {ax+11} {ay+14} L {ax} {ay+34} Z" fill="white" stroke="{TINTA}" stroke-width="1.8"/>')
    c += _t(ax + 18, ay + 5, "Aminoácido", 14, bold=True) + _t(ax + 18, ay + 32, "ARNt", 14, bold=True)
    c += _t(rx, ry + 60, "Traducción", 14, bold=True, anchor="middle")
    c += _t(380, 246, "Citoplasma", 13, GRIS, italic=True)
    return _svg(720, 270, c, "Modelo de síntesis de proteínas: transcripción en el núcleo y traducción en el ribosoma")


def fig_cucarachas():
    return _tabla(["Caja con las cucarachas", "Tratamiento", "% de cucarachas sobrevivientes"],
                  [["Caja 1", "Insecticida 1", "90 %"], ["Caja 2", "Insecticida 2", "80 %"],
                   ["Caja 3", "Insecticida 3", "70 %"], ["Caja 4", "Insecticida 4", "50 %"],
                   ["Caja 5", "Sin insecticida", "50 %"]])


def fig_lh():
    import math
    gx, gy, gw, gh = 60, 30, 520, 130
    c = (f'<line x1="{gx}" y1="{gy+gh}" x2="{gx+gw}" y2="{gy+gh}" stroke="{TINTA}" stroke-width="1.8"/>'
         f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy+gh}" stroke="{TINTA}" stroke-width="1.8"/>')
    pts = " ".join(f"{gx+d*gw/28:.0f},{gy+gh-(18+85*math.exp(-((d-14)**2)/1.6)):.0f}" for d in range(29))
    c += f'<polyline points="{pts}" fill="none" stroke="#30843C" stroke-width="2.8"/>'
    for d in (1, 14, 28):
        c += _t(gx + d * gw / 28, gy + gh + 22, str(d), 14, anchor="middle")
    c += _t(gx + gw / 2, gy + gh + 44, "días del ciclo menstrual", 14, GRIS, "middle", italic=True)
    c += _t(gx + 14 * gw / 28 + 14, gy + 10, "pico de hormona luteinizante (LH) → ovulación", 14, bold=True)
    c += _t(gx - 10, gy + gh / 2, "LH", 14, bold=True, anchor="end")
    return (_svg(600, 210, c, "Esquema: la hormona luteinizante tiene un pico hacia el día 14, que produce la ovulación")
            + '<p class="sub figcap">Esquema simplificado. El cuadernillo trae además las curvas de estrógeno y '
              'progesterona y las del ciclo estral.</p>')


def fig_alveolo():
    ax, ay = 300, 20
    c = (f'<path d="M {ax-200} {ay+20} Q {ax} {ay+230} {ax+200} {ay+20}" fill="#F4F6FA" stroke="{TINTA}" stroke-width="2.4"/>'
         + _t(ax + 210, ay + 34, "Alvéolo pulmonar", 15, bold=True))
    cy = ay + 170
    c += f'<path d="M {ax-290} {cy} Q {ax} {cy+70} {ax+290} {cy-10}" fill="none" stroke="{ROJO}" stroke-width="26" stroke-opacity="0.22"/>'
    for k in range(4):
        c += (f'<ellipse cx="{ax-150+k*100}" cy="{cy+26-abs(k-1.5)*8:.0f}" rx="22" ry="10" fill="white" '
              f'stroke="{ROJO}" stroke-width="1.8"/>')
    c += _t(ax + 200, cy + 56, "Capilar sanguíneo", 15, bold=True)
    c += _t(ax + 60, cy + 78, "Glóbulo rojo", 14)
    c += _t(ax - 290, cy + 56, "Sangre que entra al pulmón →", 14)
    c += _t(ax + 300, cy - 30, "→ sangre que sale", 14, anchor="start")
    c += _t(ax - 92, ay + 74, "O₂", 17, bold=True) + _flecha(ax - 60, ay + 80, ax - 60, cy + 6)
    c += _t(ax + 74, ay + 74, "CO₂", 17, bold=True) + _flecha(ax + 62, cy + 6, ax + 62, ay + 82)
    return _svg(740, 290, c, "Modelo del intercambio de oxígeno y dióxido de carbono entre el alvéolo y el capilar")


GRAF_FC = {"A": (((0, 85), (15, 135), (30, 143), (45, 148), (57, 152)),
                 ((0, 62), (15, 110), (30, 125), (45, 133), (57, 138))),
           "B": (((0, 65), (15, 90), (30, 115), (45, 140), (63, 165)),
                 ((0, 85), (15, 83), (30, 83), (45, 83), (60, 83))),
           "C": (((0, 113), (15, 116), (30, 122), (45, 135), (60, 150)),
                 ((0, 100), (15, 95), (30, 80), (45, 65), (60, 57))),
           "D": (((0, 62), (15, 108), (30, 128), (45, 135), (57, 138)),
                 ((0, 88), (15, 138), (30, 145), (45, 150), (57, 152)))}


def _mini_fc(ox, oy, L):
    pw, ph = 250, 150
    X = lambda t: ox + 50 + t / 80 * pw
    Y = lambda f: oy + 20 + ph - (f - 55) / 120 * ph
    c = _t(ox + 10, oy + 16, f"Gráfica {L}", 15, bold=True)
    for f in (55, 95, 135, 175):
        c += f'<line x1="{X(0):.0f}" y1="{Y(f):.0f}" x2="{X(80):.0f}" y2="{Y(f):.0f}" stroke="#E3E8EF"/>'
        c += _t(X(0) - 6, Y(f) + 4, str(f), 11, anchor="end")
    c += (f'<line x1="{X(0):.0f}" y1="{Y(55):.0f}" x2="{X(80):.0f}" y2="{Y(55):.0f}" stroke="{TINTA}" stroke-width="1.6"/>'
          f'<line x1="{X(0):.0f}" y1="{Y(55):.0f}" x2="{X(0):.0f}" y2="{Y(175)-6:.0f}" stroke="{TINTA}" stroke-width="1.6"/>')
    for t in (0, 20, 40, 60, 80):
        c += _t(X(t), Y(55) + 15, str(t), 11, anchor="middle")
    c += _t(X(40), Y(55) + 31, "Tiempo (minutos)", 11, anchor="middle")
    sed, dep = GRAF_FC[L]
    c += f'<polyline points="{" ".join(f"{X(t):.0f},{Y(f):.0f}" for t, f in sed)}" fill="none" stroke="{TINTA}" stroke-width="2.4"/>'
    for t, f in sed:
        c += (f'<polygon points="{X(t):.0f},{Y(f)-5:.0f} {X(t)+5:.0f},{Y(f):.0f} {X(t):.0f},{Y(f)+5:.0f} '
              f'{X(t)-5:.0f},{Y(f):.0f}" fill="white" stroke="{TINTA}" stroke-width="1.4"/>')
    c += (f'<polyline points="{" ".join(f"{X(t):.0f},{Y(f):.0f}" for t, f in dep)}" fill="none" '
          f'stroke="{TINTA}" stroke-width="1.6" stroke-dasharray="6,4"/>')
    for t, f in dep:
        c += f'<rect x="{X(t)-4:.0f}" y="{Y(f)-4:.0f}" width="8" height="8" fill="white" stroke="{TINTA}" stroke-width="1.4"/>'
    return c


def fig_frecuencia():
    c = (f'<line x1="10" y1="14" x2="50" y2="14" stroke="{TINTA}" stroke-width="2.4"/>'
         f'<polygon points="30,9 35,14 30,19 25,14" fill="white" stroke="{TINTA}" stroke-width="1.4"/>'
         + _t(58, 19, "Sedentario", 14) +
         f'<line x1="170" y1="14" x2="210" y2="14" stroke="{TINTA}" stroke-width="1.6" stroke-dasharray="6,4"/>'
         f'<rect x="186" y="10" width="8" height="8" fill="white" stroke="{TINTA}" stroke-width="1.4"/>'
         + _t(218, 19, "Deportista", 14) +
         _t(340, 19, "eje vertical: frecuencia cardiaca (latidos por minuto)", 13, GRIS, italic=True))
    for k, L in enumerate("ABCD"):
        c += _mini_fc((k % 2) * 330, 34 + (k // 2) * 225, L)
    return _svg(660, 490, c, "Cuatro gráficas de frecuencia cardiaca contra tiempo, A a D, sedentario y deportista")


def fig_eutrofizacion():
    def caja(x, y, w, h, txt, bold=False):
        lineas = txt.split("\n")
        s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="white" stroke="{GRIS}" stroke-width="1.6"/>'
        y0 = y + h / 2 - (len(lineas) - 1) * 9 + 5
        for j, l in enumerate(lineas):
            s += _t(x + w / 2, y0 + j * 18, l, 14, anchor="middle", bold=bold)
        return s
    cx = 360
    c = ""
    for t, px in (("Crecimiento de bacterias\nfotosintéticas", cx - 240), ("Toxicidad algal", cx),
                  ("Riesgos sanitarios", cx + 240)):
        c += caja(px - 105, 6, 210, 52, t)
        c += f'<line x1="{px}" y1="58" x2="{px}" y2="76" stroke="{GRIS}" stroke-width="1.6"/>'
    c += f'<line x1="{cx-240}" y1="76" x2="{cx+240}" y2="76" stroke="{GRIS}" stroke-width="1.6"/>'
    c += f'<line x1="{cx}" y1="76" x2="{cx}" y2="92" stroke="{GRIS}" stroke-width="1.6"/>'
    c += caja(cx - 110, 92, 220, 40, "Eutrofización", True)
    c += f'<line x1="{cx}" y1="132" x2="{cx}" y2="148" stroke="{GRIS}" stroke-width="1.6"/>'
    c += f'<line x1="{cx-180}" y1="148" x2="{cx+180}" y2="148" stroke="{GRIS}" stroke-width="1.6"/>'
    for t, px, t2 in (("Sustracción del oxígeno disuelto\npara tomar fosfatos y nitratos", cx - 180, "Mortalidad de peces"),
                      ("Pérdida de la calidad\ndel agua", cx + 180, "Olor y sabor desagradable")):
        c += f'<line x1="{px}" y1="148" x2="{px}" y2="162" stroke="{GRIS}" stroke-width="1.6"/>'
        c += caja(px - 140, 162, 280, 56, t)
        c += f'<line x1="{px}" y1="218" x2="{px}" y2="234" stroke="{GRIS}" stroke-width="1.6"/>'
        c += caja(px - 115, 234, 230, 40, t2)
    return _svg(720, 284, c, "Esquema de la eutrofización y sus consecuencias")


def fig_fuentes():
    return _tabla(["Fuente", "Tipo de energía", "Composición", "Poder calorífico (kcal/kg)"],
                  [["Agua de mar (agua salada)", "Osmótica", "Sales inorgánicas (NaCl, KCl…) y H₂O", "2.000"],
                   ["Aire", "Eólica", "N₂, O₂, Ar, CO₂, Ne, He, H₂O", "1.000"],
                   ["Materia orgánica en descomposición", "Química", "Materia orgánica y microorganismos", "2.500"],
                   ["Petróleo", "Química", "Combinación de hidrocarburos (alcanos, alquenos, alquinos…)", "10.000"],
                   ["Gas natural", "Química", "Propano (C₃H₈)", "9.300"]])


def _mini_vino(ox, oy, L, tipo, val):
    pw, ph = 220, 120
    x0, y0 = ox + 34, oy + 22
    c = _t(ox + 4, oy + 14, f"Gráfica {L}", 15, bold=True)
    c += (f'<line x1="{x0}" y1="{y0+ph}" x2="{x0+pw}" y2="{y0+ph}" stroke="{TINTA}" stroke-width="1.6"/>'
          f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+ph}" stroke="{TINTA}" stroke-width="1.6"/>')
    c += (f'<text transform="translate({x0-10},{y0+ph/2}) rotate(-90)" font-size="11" fill="{GRIS}" '
          f'text-anchor="middle">Intensidad del color</text>')
    if tipo == "barras":
        con, sin = val
        for k, (v, dash) in enumerate(((con, True), (sin, False))):
            bx = x0 + 40 + k * 100
            h = v * ph
            c += (f'<rect x="{bx}" y="{y0+ph-h:.0f}" width="44" height="{h:.0f}" '
                  + ('fill="white" stroke="{0}" stroke-width="1.6" stroke-dasharray="5,4"/>'.format(TINTA) if dash
                     else f'fill="#B8BEC8" stroke="{TINTA}" stroke-width="1.6"/>'))
        c += _t(x0 + pw / 2, y0 + ph + 16, "Tipo de vino producido", 11, anchor="middle")
        ley = (f'<rect x="{x0+pw+14}" y="{y0+4}" width="14" height="12" fill="white" stroke="{TINTA}" '
               f'stroke-dasharray="4,3"/>' + _t(x0 + pw + 34, y0 + 15, "con pectinasa", 12) +
               f'<rect x="{x0+pw+14}" y="{y0+26}" width="14" height="12" fill="#B8BEC8" stroke="{TINTA}"/>'
               + _t(x0 + pw + 34, y0 + 37, "sin pectinasa", 12))
    else:
        con, sin = val
        for pts, dash in ((con, False), (sin, True)):
            p = " ".join(f"{x0+a*pw:.0f},{y0+ph-b*ph:.0f}" for a, b in pts)
            c += (f'<polyline points="{p}" fill="none" stroke="{TINTA}" stroke-width="2"'
                  + (' stroke-dasharray="6,4"/>' if dash else "/>"))
        c += _t(x0 + pw / 2, y0 + ph + 16, "Tiempo (días)", 11, anchor="middle")
        ley = (f'<line x1="{x0+pw+14}" y1="{y0+10}" x2="{x0+pw+30}" y2="{y0+10}" stroke="{TINTA}" stroke-width="2"/>'
               + _t(x0 + pw + 34, y0 + 15, "con pectinasa", 12) +
               f'<line x1="{x0+pw+14}" y1="{y0+32}" x2="{x0+pw+30}" y2="{y0+32}" stroke="{TINTA}" '
               f'stroke-width="2" stroke-dasharray="5,3"/>' + _t(x0 + pw + 34, y0 + 37, "sin pectinasa", 12))
    return c + ley


def fig_vino():
    graf = (("A", "barras", (0.42, 0.62)), ("B", "barras", (0.88, 0.52)),
            ("C", "lineas", ([(0, 0.6), (0.5, 0.6), (0.5, 0.0)], [(0, 0.64), (0.5, 0.64), (0.85, 0.3)])),
            ("D", "lineas", ([(0, 0.15), (0.85, 0.5)], [(0, 0.42), (0.85, 0.78)])))
    c = "".join(_mini_vino((k % 2) * 360, (k // 2) * 175, L, t, v) for k, (L, t, v) in enumerate(graf))
    return (_svg(720, 345, c, "Cuatro gráficas de intensidad del color del vino con y sin pectinasa, A a D")
            + '<p class="sub figcap">Redibujadas desde una fotocopia: la barra «con pectinasa» de la gráfica A '
              'casi no se ve en el original.</p>')


def fig_ciclo():
    def nodo(x, y, txt, rx=118, ry=34):
        lineas = txt.split("\n")
        s = f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="white" stroke="{GRIS}" stroke-width="1.8"/>'
        y0 = y - (len(lineas) - 1) * 9 + 5
        for j, l in enumerate(lineas):
            s += _t(x, y0 + j * 18, l, 14, anchor="middle")
        return s
    L, R, top, bot = 150, 590, 60, 260
    c = nodo(L, top, "Células haploides (n)") + nodo(R, top, "Gametos: esperma (n)\ny óvulo (n)", ry=40)
    c += nodo(R, bot, "Cigoto diploide (2n)") + nodo((L + R) / 2 + 30, bot, "Organismo multicelular\ndiploide (2n)", 132, 40)
    c += nodo(L, bot, "Células (2n)\nlínea germinal", 108, 40)
    c += _flecha(L + 120, top, R - 122, top) + _t((L + R) / 2, top - 12, "Haploide (n)", 15, anchor="middle")
    c += _flecha(R, top + 42, R, bot - 36) + _t(R + 12, (top + bot) / 2 + 5, "Fertilización", 15, bold=True)
    c += _flecha(R - 120, bot, (L + R) / 2 + 164, bot) + _t((R - 120 + (L + R) / 2 + 164) / 2 + 2, bot - 46, "Mitosis", 15, anchor="middle", bold=True)
    c += _flecha((L + R) / 2 - 104, bot, L + 110, bot)
    c += _t(((L + R) / 2 - 104 + L + 110) / 2 + 4, bot - 64, "Formación de", 13, anchor="middle")
    c += _t(((L + R) / 2 - 104 + L + 110) / 2 + 4, bot - 48, "células germinales", 13, anchor="middle")
    c += _flecha(L, bot - 42, L, top + 36) + _t(L - 12, (top + bot) / 2 + 5, "Meiosis", 15, anchor="end", bold=True)
    c += _t((L + R) / 2, (top + bot) / 2 + 5, "Diploide (2n)", 15, anchor="middle")
    return _svg(760, 310, c, "Ciclo de alternancia entre células haploides y diploides: meiosis, fertilización y mitosis")


def fig_especies():
    return _tabla(["Especie", "Nombre científico", "Ciclo (días)", "Ciclos al año"],
                  [["1", "Ateles belzebuth", "24 - 27", "12"], ["2", "Bos primigenius taurus", "21 - 23", "6"],
                   ["3", "Equus ferus caballus", "23 - 26", "4"], ["4", "Papio hamadryas", "31 - 35", "11"]])


def fig_etileno():
    return _tabla(["Fruto", "Tiempo de exposición al etileno"],
                  [["Piña", "5 días y 2 horas"], ["Mango", "4 días y 24 minutos"], ["Banano", "2 días y 10 horas"],
                   ["Aguacate", "3 días y 21 horas"], ["Guayaba", "2 días y 3 horas"]])


FIGURAS = {(1, 2): fig_transporte(), (1, 3): fig_sintesis(), (1, 4): fig_cucarachas(),
           (2, 1): fig_lh(), (2, 2): fig_alveolo(), (2, 4): fig_frecuencia(),
           (3, 1): fig_eutrofizacion(), (3, 3): fig_fuentes(),
           (4, 1): fig_vino(), (5, 1): fig_ciclo(),
           (6, 1): fig_especies(), (6, 2): fig_etileno()}

# Estilo de las figuras dentro del panel del texto (se agrega a la plantilla de la guía).
CSS = """.fig{margin:12px 0}.fig svg{display:block;width:100%;max-width:760px;height:auto}
.tabla{border-collapse:collapse;width:100%;table-layout:fixed;font-size:.9em}
.tabla th,.tabla td{border:1px solid var(--line);padding:6px 8px;vertical-align:top;overflow-wrap:anywhere}
.tabla th{background:#F2F5F3;text-align:left}.figcap{font-size:.85em;font-style:italic}
"""


# ─────────────────────────────── verificación ───────────────────────────────
def _norm(t):
    t = unicodedata.normalize("NFKC", t).lower()
    t = re.sub(r"[₀-₉]", lambda m: str("₀₁₂₃₄₅₆₇₈₉".index(m.group(0))), t)
    return re.sub(r"[^\w%$]+", " ", t).strip()


def _modulo(mis):
    src = open(f"/home/claude/libro/bio{mis}_icfes.py", encoding="utf-8").read()
    claves = dict(re.findall(r"Q([A-D])\s*·[^·\n]*·\s*([A-D])\b", src[:4000]))
    ops = {}
    for n in ast.parse(src).body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") in ("QA", "QB", "QC", "QD"):
            kw = {k.arg: k.value for k in n.value.keywords}
            try:
                ops[n.targets[0].id[1]] = ast.literal_eval(kw["o"])
            except ValueError:
                ops[n.targets[0].id[1]] = None
    return claves, ops


def _csv(mis):
    filas = [r for r in csv.DictReader(open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig"))
             if r["mision"].strip() == f"BIO M{mis}"]
    return {i + 1: r for i, r in enumerate(filas)}


def verificar(icfes=None):
    """Diferencias entre el .md, los módulos bioN_icfes.py y tablero/icfes.csv (lista vacía = todo bien)."""
    icfes = icfes or leer()
    malas = []
    for mis in range(1, 7):
        claves, ops = _modulo(mis)
        tab = _csv(mis)
        for k in range(1, 5):
            q = "ABCD"[k - 1]
            v = icfes.get((mis, k))
            if not v:
                malas.append(f"M{mis} P{k}: falta en el .md")
                continue
            if len(v["opciones"]) != 4:
                malas.append(f"M{mis} P{k}: {len(v['opciones'])} opciones")
            if claves.get(q) != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · bio{mis}_icfes.py {claves.get(q)}")
            if tab.get(k, {}).get("clave", "").strip() != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · icfes.csv {tab.get(k, {}).get('clave')}")
            if "ASED" in tab.get(k, {}).get("fuente", "") and "ASED" not in v["fuente"]:
                malas.append(f"M{mis} P{k}: sale del ASED y el .md no lo dice")
            mo = ops.get(q)
            if mo and len(mo) == 4:
                for L, a, b in zip("ABCD", mo, v["opciones"]):
                    if _norm(a) != _norm(b):
                        malas.append(f"M{mis} P{k} {L}: el .md no copia la opción del cuaderno")
            if (MARCA in v["texto"]) != ((mis, k) in FIGURAS):
                malas.append(f"M{mis} P{k}: marca de figura y FIGURAS no coinciden")
    return malas


if __name__ == "__main__":
    d = leer()
    for m in range(1, 7):
        for k in range(1, 5):
            v = d.get((m, k))
            if not v:
                print(f"M{m} P{k}: — FALTA —")
                continue
            print(f"M{m} P{k} · p.{v['pagina']} · clave {v['clave']} · «{v['titulo'][:38]}» · texto "
                  f"{len(v['texto'])} car. · {len(v['opciones'])} opciones · {len(v['notas'])} notas"
                  + (" · figura" if (m, k) in FIGURAS else ""))
    malas = verificar(d)
    print("claves y opciones: todo coincide" if not malas else "\n".join(["DIFERENCIAS:"] + malas))
