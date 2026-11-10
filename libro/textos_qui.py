#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lee TEXTOS_QUI.md y devuelve lo de Química que la guía de clase proyecta: las 24 preguntas de
entrenamiento (texto completo, enunciado, opciones, clave verificada, fuente y notas para el profe)
y, aparte, las figuras de esas preguntas redibujadas para la pantalla.

TEXTOS_QUI.md usa el mismo formato que TEXTOS_BIO.md, así que el lector es textos_soc.leer() con
area="QUÍMICA" (textos_soc no se toca). Sale de textos_bio.py.

    from textos_qui import leer, FIGURAS, FIG_OPCIONES
    icfes = leer()              # {(misión, k): dict(titulo, texto, enunciado, opciones, clave, notas…)}
    FIGURAS[(1, 2)]             # HTML de la tabla de los cuatro sólidos (va en el panel del texto)
    FIG_OPCIONES[(2, 3)]        # las cuatro gráficas de enfriamiento (van en la columna de opciones)

Donde el .md dice «[[figura]]», la guía pone FIGURAS[(misión, k)]. Cuando las opciones son gráficas
o figuras (M2 P3, M3 P4, M4 P2), FIG_OPCIONES[(misión, k)] va encima de las cuatro letras. Las figuras
repiten los datos de los módulos del cuaderno (quiN_icfes.py): tablas en HTML y esquemas en SVG en
línea, sin internet. Ninguna figura de opciones marca la correcta: las cuatro van en la misma tinta.

verificar() cruza, pregunta por pregunta, la clave del .md con el docstring de quiN_icfes.py y con
tablero/icfes.csv, las cuatro opciones con las del módulo (cuando el módulo las trae en texto) y que
cada figura esté donde el .md la pide.
"""
import ast, csv, html, math, re, unicodedata

import textos_soc

FUENTE = "/home/claude/libro/TEXTOS_QUI.md"
MARCA = "[[figura]]"
E = lambda t: html.escape(str(t), quote=False)


def leer(fuente=FUENTE):
    icfes, _, _ = textos_soc.leer(area="QUÍMICA", fuente=fuente)
    return icfes


# ─────────────────────────────── piezas de dibujo ───────────────────────────────
TINTA = "#1B1F27"; GRIS = "#5C6472"; LINEA = "#C9CFD8"; FONDO = "#F2F6F5"; BARRA = "#B9BEC8"
FUENTE_SVG = "font-family:'Source Sans 3','Segoe UI',system-ui,sans-serif"


def _svg(w, h, cuerpo, alt, ancho=None):
    tope = f";max-width:{ancho}px;margin:0 auto" if ancho else ""
    return (f'<figure class="fig"><svg viewBox="0 0 {w} {h}" role="img" aria-label="{E(alt)}" '
            f'style="{FUENTE_SVG}{tope}">{cuerpo}</svg></figure>')


def _t(x, y, txt, size=15, color=TINTA, anchor="start", bold=False, italic=False, rot=None):
    tr = f' transform="rotate({rot} {x:.0f} {y:.0f})"' if rot else ""
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-size="{size}" fill="{color}" text-anchor="{anchor}"'
            f'{" font-weight=\"700\"" if bold else ""}{" font-style=\"italic\"" if italic else ""}{tr}>'
            f'{E(txt)}</text>')


def _l(x1, y1, x2, y2, c=TINTA, sw=1.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{c}" stroke-width="{sw}"{d}/>'


def _tabla(cab, filas, titulo=None, nota=None, cab2=None):
    """Tabla HTML. cab2: fila de encabezado superior [(texto, colspan), …]."""
    sup = ("<tr>" + "".join(f'<th colspan="{n}">{E(t)}</th>' for t, n in cab2) + "</tr>") if cab2 else ""
    th = "<tr>" + "".join(f"<th>{E(c)}</th>" for c in cab) + "</tr>"
    tr = "".join("<tr>" + "".join(f"<td>{E(c)}</td>" for c in f) + "</tr>" for f in filas)
    cap = f"<caption>{E(titulo)}</caption>" if titulo else ""
    pie = f'<figcaption>{E(nota)}</figcaption>' if nota else ""
    return (f'<figure class="fig"><table class="tabla">{cap}<thead>{sup}{th}</thead><tbody>{tr}</tbody>'
            f'</table>{pie}</figure>')


# ─────────────────────────────── misión 1 ───────────────────────────────
def fig_solidos():
    return _tabla(["", "Densidad (g/cm³)", "Punto de fusión (°C)", "Solubilidad en agua",
                   "Solubilidad en etanol"],
                  [["Sólido 1", "1,0", "150", "Soluble", "Soluble"],
                   ["Sólido 2", "1,0", "150", "Insoluble", "Soluble"],
                   ["Sólido 3", "1,0", "80", "Soluble", "Insoluble"],
                   ["Sólido 4", "2,0", "80", "Insoluble", "Insoluble"]])


def fig_solubilidad():
    return _tabla(["Sustancia", "0 °C", "40 °C", "80 °C"],
                  [["AgNO₃ (s)", "1220", "3760", "6690"], ["KCl (s)", "276", "400", "511"],
                   ["NaCl (s)", "357", "366", "384"], ["O₂ (g)", "0,069", "0,031", "0,014"],
                   ["CO₂ (g)", "3,374", "0,97", "0"], ["He (g)", "0,00167", "0,00152", "0,00137"]],
                  titulo="Solubilidad a diferentes temperaturas (g de soluto/kg de agua)")


# ─────────────────────────────── misión 2 ───────────────────────────────
def fig_fusion():
    return _tabla(["Sustancia", "Tiempo", "Observación final"],
                  [["1", "50", "Pasa de estado sólido a líquido."],
                   ["2", "163", "Pasa de estado sólido a líquido."]])


def _temp_enfriamiento(forma, f):
    """Las cuatro formas de qui2_icfes._mini (temperatura en °C para f de 0 a 1)."""
    if forma == "A":
        return 20 + 80 * max(0.0, 1 - (f / 0.68) ** 2) if f < 0.68 else 20
    if forma == "B":
        return 20 + 80 * (1 / (1 + math.exp((f - 0.25) / 0.06))) / (1 / (1 + math.exp(-0.25 / 0.06)))
    if forma == "C":
        return 20 + 80 * math.exp(-f / 0.05)
    return 100 - 80 * f / 0.55 if f < 0.55 else 20


def fig_enfriamiento():
    c = ""
    for k, L in enumerate("ABCD"):
        ox = k * 210
        gx, gy, gw, gh = ox + 44, 34, 150, 150
        c += _t(ox + 6, 20, f"Gráfica {L}", 15, bold=True)
        for t in range(0, 121, 20):
            py = gy + gh - t / 120 * gh
            c += _l(gx, py, gx + gw, py, "#E3E8EF", 1)
            c += _t(gx - 5, py + 4, str(t), 10, anchor="end")
        c += _l(gx, gy + gh, gx + gw, gy + gh) + _l(gx, gy - 4, gx, gy + gh)
        c += _t(gx + gw / 2, gy + gh + 16, "tiempo", 11, GRIS, "middle", italic=True)
        c += _t(gx - 30, gy + gh / 2, "temperatura (°C)", 11, GRIS, "middle", italic=True, rot=-90)
        pts = " ".join(f"{gx + i / 100 * gw:.1f},{gy + gh - _temp_enfriamiento(L, i / 100) / 120 * gh:.1f}"
                       for i in range(101))
        c += f'<polyline points="{pts}" fill="none" stroke="{TINTA}" stroke-width="2.4"/>'
    return _svg(840, 214, c, "Cuatro gráficas de temperatura contra tiempo, A a D")


# ─────────────────────────────── misión 3 ───────────────────────────────
def fig_velocidad():
    filas = [("1", "10", "10", "100"), ("2", "20", "10", "200"), ("3", "30", "10", "?"),
             ("4", "40", "10", "400"), ("5", "10", "20", "400"), ("6", "10", "30", "?"),
             ("7", "10", "40", "1600")]
    grupos = [("Condiciones iniciales", 1), ("Modificando la concentración de X", 3),
              ("Modificando la concentración de W", 3)]
    cuerpo, k = "", 0
    for g, n in grupos:
        for j in range(n):
            primera = f'<td rowspan="{n}">{E(g)}</td>' if j == 0 else ""
            cuerpo += "<tr>" + primera + "".join(f"<td>{E(v)}</td>" for v in filas[k]) + "</tr>"
            k += 1
    th = "".join(f"<th>{E(t)}</th>" for t in ("", "Experimento", "Concentración de X (M)",
                                               "Concentración de W (M)", "Velocidad de reacción (M/s)"))
    return f'<figure class="fig"><table class="tabla"><thead><tr>{th}</tr></thead><tbody>{cuerpo}</tbody></table></figure>'


def fig_ph():
    return _tabla(["Sustancia", "pH", "Carácter"],
                  [["Leche", "6,8", "Neutro"], ["Jugo de naranja", "3,5", "Ácido"], ["Jabón", "9,0", "Básico"],
                   ["Agua", "7,0", "Neutro"], ["Crema de dientes", "10,5", "Básico"], ["Café", "5,0", "Ácido"],
                   ["Gel para el cabello", "7,2", "Neutro"]])


def fig_gas():
    gx, gy, gw, gh = 96, 18, 480, 240
    c = ""
    for v in range(0, 501, 100):
        py = gy + gh - v / 500 * gh
        c += _l(gx, py, gx + gw, py, "#DDE2E9", 1.2, "4,5") + _t(gx - 10, py + 5, str(v), 13, anchor="end")
    for t in range(0, 601, 100):
        px = gx + t / 600 * gw
        if t:
            c += _l(px, gy, px, gy + gh, "#DDE2E9", 1.2, "4,5")
        c += _t(px, gy + gh + 20, str(t), 13, anchor="middle")
    c += _l(gx, gy + gh, gx + gw + 10, gy + gh, TINTA, 2) + _l(gx, gy - 8, gx, gy + gh, TINTA, 2)
    for t, v in ((100, 100), (250, 250), (400, 400), (500, 500)):
        c += (f'<circle cx="{gx + t / 600 * gw:.1f}" cy="{gy + gh - v / 500 * gh:.1f}" r="7" fill="white" '
              f'stroke="{TINTA}" stroke-width="2.2"/>')
    c += _t(gx + gw / 2, gy + gh + 44, "Temperatura (K)", 14, bold=True, anchor="middle")
    c += _t(gx - 56, gy + gh / 2, "Volumen (mL)", 14, bold=True, anchor="middle", rot=-90)
    return _svg(600, 310, c, "Gráfica de volumen contra temperatura de un gas a presión constante: cuatro puntos",
                ancho=560)


def fig_barras_ph():
    graf = (("A", 8, 9.2), ("B", 7, 7), ("C", 0, 9.8), ("D", 6, 3))
    c = ""
    for k, (L, v1, v2) in enumerate(graf):
        ox = k * 210
        gx, gy, gw, gh = ox + 44, 30, 150, 140
        c += _t(ox + 6, 18, f"Gráfica {L}", 15, bold=True)
        for v in range(0, 11, 2):
            py = gy + gh - v / 10 * gh
            c += _l(gx, py, gx + gw, py, "#E3E8EF", 1) + _t(gx - 5, py + 4, str(v), 10, anchor="end")
        c += _l(gx, gy + gh, gx + gw, gy + gh) + _l(gx, gy - 4, gx, gy + gh)
        c += _t(gx - 28, gy + gh / 2, "pH", 12, bold=True, anchor="middle", rot=-90)
        for j, (v, n) in enumerate(((v1, "Mezcla 1"), (v2, "Mezcla 2"))):
            bx = gx + 18 + j * 70
            if v:
                c += (f'<rect x="{bx}" y="{gy + gh - v / 10 * gh:.1f}" width="44" height="{v / 10 * gh:.1f}" '
                      f'fill="{BARRA}" stroke="{TINTA}" stroke-width="1.4"/>')
            c += _t(bx + 22, gy + gh + 16, n, 11, anchor="middle")
    return _svg(840, 196, c, "Cuatro gráficas de barras con el pH de la mezcla 1 y la mezcla 2, A a D")


# ─────────────────────────────── misión 4 ───────────────────────────────
def fig_alcohol_eter():
    return _tabla(["Compuesto", "Peso molecular (g/mol)", "Tipo de fuerzas intermoleculares"],
                  [["Alcohol: CH₃-CH₂-OH", "46", "Fuertes"], ["Éter: CH₃-O-CH₃", "46", "Débiles"]])


def fig_liquidos():
    return _tabla(["Líquido", "Punto de ebullición (°C)", "Densidad (g/cm³)"],
                  [["Acetona", "56,3", "0,79"], ["Agua", "100,0", "1,00"], ["Cloroformo", "61,0", "1,48"]])


def fig_corchos():
    """Las cuatro figuras de opciones: en cada una, tres vasos (acetona, agua, cloroformo) con el
    corcho arriba (flota) o en el fondo (se hunde). Mismo dibujo que qui4_icfes.datos_104."""
    figs = (("A", (False, True, True)), ("B", (True, True, True)), ("C", (False, False, False)),
            ("D", (True, False, False)))
    c = ""
    for k, (L, fl) in enumerate(figs):
        ox = (k % 2) * 420
        oy = (k // 2) * 150
        c += _t(ox + 6, oy + 20, f"Figura {L}", 15, bold=True)
        for j, (n, f) in enumerate(zip(("Acetona", "Agua", "Cloroformo"), fl)):
            cx, by = ox + 110 + j * 115, oy + 112
            w, h = 64, 76
            x0 = cx - w / 2
            c += (f'<path d="M {x0} {by - h} L {x0 + 7} {by} L {x0 + w - 7} {by} L {x0 + w} {by - h}" '
                  f'fill="none" stroke="{TINTA}" stroke-width="1.8"/>')
            ly = by - h + 18
            c += _l(x0 + 3, ly, x0 + w - 3, ly, TINTA, 1.4)
            cy = ly - 2 if f else by - 11
            c += (f'<rect x="{cx - 12}" y="{cy - 7}" width="24" height="14" rx="3" fill="#E9D5B0" '
                  f'stroke="{TINTA}" stroke-width="1.4"/>')
            c += _t(cx, by + 20, n, 12, anchor="middle")
    return _svg(840, 300, c, "Cuatro figuras, A a D, con un corcho en tres vasos: acetona, agua y cloroformo")


def fig_columnas():
    return _tabla(["Sustancia", "?", "Volumen (mL)", "Densidad (g/mL)", "?"],
                  [["Agua", "1,8", "1,8", "1", "100"], ["Alcohol etílico", "1,2", "1,5", "0,8", "80"],
                   ["Ácido clorhídrico", "1,12", "1", "1,12", "48"], ["Ácido sulfúrico", "5,4", "2", "2,7", "337"]])


def fig_iman():
    c = ""
    for k, n in enumerate(("Borrador", "Tapa de esfero", "Pimpón", "Puntilla")):
        cx, cy = 90 + k * 170, 34
        if k == 0:
            c += f'<rect x="{cx - 34}" y="{cy - 16}" width="68" height="32" rx="4" fill="white" stroke="{TINTA}" stroke-width="1.8"/>'
        elif k == 1:
            c += (f'<rect x="{cx - 42}" y="{cy - 7}" width="84" height="14" rx="6" fill="{BARRA}" '
                  f'stroke="{TINTA}" stroke-width="1.6"/>' + _l(cx - 42, cy - 7, cx - 50, cy - 15))
        elif k == 2:
            c += f'<circle cx="{cx}" cy="{cy}" r="17" fill="white" stroke="{TINTA}" stroke-width="1.8"/>'
        else:
            c += _l(cx - 38, cy, cx + 32, cy, TINTA, 2.4) + _l(cx + 32, cy - 9, cx + 32, cy + 9, TINTA, 3)
        c += _t(cx, cy + 40, n, 14, anchor="middle")
    sx, ty = 170, 170
    c += f'<rect x="{sx - 40}" y="{ty}" width="460" height="12" fill="#C9CED6"/>'
    c += f'<rect x="{sx + 140}" y="{ty - 54}" width="120" height="40" rx="4" fill="white" stroke="{TINTA}" stroke-width="2"/>'
    c += f'<rect x="{sx + 236}" y="{ty - 46}" width="18" height="14" rx="2" fill="white" stroke="{TINTA}" stroke-width="1.6"/>'
    for wx in (sx + 166, sx + 234):
        c += f'<circle cx="{wx}" cy="{ty - 8}" r="8" fill="white" stroke="{TINTA}" stroke-width="2"/>'
    c += _t(sx + 245, ty - 60, "Objeto", 13, anchor="middle")
    c += f'<rect x="{sx + 180}" y="{ty + 20}" width="40" height="60" rx="3" fill="#C9CED6" stroke="{TINTA}" stroke-width="1.8"/>'
    for ay in (ty - 34, ty + 50):
        c += (f'<path d="M {sx + 60} {ay - 7} L {sx + 90} {ay - 7} L {sx + 90} {ay - 15} L {sx + 110} {ay} '
              f'L {sx + 90} {ay + 15} L {sx + 90} {ay + 7} L {sx + 60} {ay + 7} Z" fill="none" stroke="{TINTA}" '
              f'stroke-width="1.6" stroke-dasharray="4,3"/>')
    c += _t(sx + 280, ty - 28, "← Carro de plástico", 14)
    c += _t(sx + 230, ty + 56, "← Imán", 14)
    c += _t(sx - 40, ty + 30, "Mesa", 13, GRIS, italic=True)
    return _svg(700, 260, c, "Cuatro objetos (borrador, tapa de esfero, pimpón, puntilla) y el carro sobre la mesa "
                             "con el imán debajo", ancho=640)


# ─────────────────────────────── misión 5 ───────────────────────────────
def fig_organicos():
    return _tabla(["Compuesto", "Fórmula condensada", "PM (g/mol)", "μ (D)", "Pe (°C)"],
                  [["1 · n-pentano", "CH₃–CH₂–CH₂–CH₂–CH₃", "72", "0", "36"],
                   ["2 · cloruro de n-propilo", "CH₃–CH₂–CH₂–Cl", "78,5", "2,10", "47"],
                   ["3 · butiraldehído", "CH₃–CH₂–CH₂–CHO", "72", "2,72", "76"],
                   ["4 · alcohol n-butílico", "CH₃–CH₂–CH₂–CH₂–OH", "74", "1,63", "118"]],
                  nota="PM: peso molecular · μ: momento dipolar (polaridad) · Pe: punto de ebullición")


def fig_densidad():
    return _tabla(["", "Muestra 1", "Muestra 2", "Muestra 3", "Muestra 1", "Muestra 2", "Muestra 3"],
                  [["Masa (g)", "10", "20", "40", "10", "20", "30"],
                   ["Volumen (cm³)", "12", "24", "48", "16", "32", "48"]],
                  cab2=[("", 1), ("Material 1", 3), ("Material 2", 3)])


def fig_masas():
    return _tabla(["Elemento", "Número atómico", "Masa atómica (g/mol)"],
                  [["Hidrógeno · H", "1", "1"], ["Oxígeno · O", "8", "16"], ["Carbono · C", "6", "12"]])


def fig_palma():
    return _tabla(["Propiedad", "Aceite de palma", "Combustible fósil"],
                  [["Azufre (% de masa)*", "No detectado", "0,819"],
                   ["Punto de inflamación (°C)", "162,3", "62,3"],
                   ["Capacidad calorífica (MJ/kg)**", "39,5", "45,4"]],
                  titulo="Tabla 2",
                  nota="* Produce dióxido de azufre (SO₂), que contribuye a la contaminación ambiental. "
                       "** Así la llama la tabla: «energía necesaria para aumentar un grado centígrado la "
                       "temperatura del combustible».")


# ─────────────────────────────── misión 6 ───────────────────────────────
def fig_atomos():
    figs = (("A", 14, (2, 8, 2)), ("B", 12, (2, 8)), ("C", 12, (2, 8, 2)), ("D", 14, (2, 8)))
    c = (f'<rect x="4" y="4" width="330" height="32" rx="6" fill="white" stroke="{GRIS}" stroke-width="1.4"/>'
         + _t(16, 26, "Convenciones:  ○ = electrones   p⁺ = protones", 14))
    r0, dr = 20, 22
    for k, (L, p, capas) in enumerate(figs):
        cx, cy = 100 + k * 190, 170
        c += _t(cx, 66, L + ".", 17, bold=True, anchor="middle")
        c += f'<circle cx="{cx}" cy="{cy}" r="{r0}" fill="#EEF0F4" stroke="{TINTA}" stroke-width="1.6"/>'
        c += _t(cx, cy + 5, f"{p}p⁺", 13, bold=True, anchor="middle")
        for j in range(3):
            c += f'<circle cx="{cx}" cy="{cy}" r="{r0 + dr * (j + 1)}" fill="none" stroke="{TINTA}" stroke-width="1.4"/>'
        for j, n in enumerate(capas):
            r = r0 + dr * (j + 1)
            for i in range(n):
                a = 2 * math.pi * i / n - math.pi / 2 + 0.35 * j
                c += (f'<circle cx="{cx + r * math.cos(a):.1f}" cy="{cy + r * math.sin(a):.1f}" r="5" '
                      f'fill="white" stroke="{TINTA}" stroke-width="1.4"/>')
    return _svg(760, 266, c, "Cuatro modelos de capas, A a D, con sus protones en el núcleo y sus electrones")


def fig_azucares():
    return _tabla(["Azúcar", "Entalpía de combustión (kJ/mol)"],
                  [["Glucosa", "–2.816"], ["Sacarosa", "–5.648"], ["Fructosa", "–2.827"]])


def fig_metal():
    return _tabla(["", "Tubo 1", "Tubo 2", "Tubo 3"],
                  [["Exp. 1 · condición", "18 °C", "45 °C", "70 °C"],
                   ["Exp. 1 · reacción completa", "115 s", "75 s", "40 s"],
                   ["Exp. 2 · condición", "metal completo", "partido a la mitad", "en trozos pequeños"],
                   ["Exp. 2 · reacción completa", "115 s", "90 s", "50 s"]],
                  nota="Experimento 1: se modifica la temperatura, con el metal completo (sin partir). "
                       "Experimento 2: se modifica el tamaño del metal, a 18 °C.")


FIGURAS = {(1, 2): fig_solidos(), (1, 3): fig_solubilidad(),
           (2, 1): fig_fusion(),
           (3, 1): fig_velocidad(), (3, 2): fig_ph(), (3, 3): fig_gas(),
           (4, 1): fig_alcohol_eter(), (4, 2): fig_liquidos(), (4, 3): fig_columnas(), (4, 4): fig_iman(),
           (5, 1): fig_organicos(), (5, 2): fig_densidad(), (5, 3): fig_masas(), (5, 4): fig_palma(),
           (6, 1): fig_atomos(), (6, 2): fig_azucares(), (6, 3): fig_metal()}

# Preguntas cuyas opciones son gráficas o figuras: van en la columna de las opciones (no en el panel
# del texto, donde habría que desplazarse para ver las cuatro) y las letras quedan en una sola fila.
FIG_OPCIONES = {(2, 3): fig_enfriamiento(), (3, 4): fig_barras_ph(), (4, 2): fig_corchos()}
EN_OPCIONES = set(FIG_OPCIONES)

# Estilo de las figuras dentro del panel del texto (se agrega a la plantilla de la guía).
CSS = """.fig{margin:12px 0}.fig svg{display:block;width:100%;max-width:760px;height:auto}
.tabla{border-collapse:collapse;width:100%;table-layout:fixed;font-size:.86em;line-height:1.35}
.tabla th,.tabla td{border:1px solid var(--line);padding:5px 8px;vertical-align:top;overflow-wrap:anywhere}
.tabla th{background:#EEF4F2;text-align:left}.tabla caption{text-align:left;font-weight:700;padding:0 0 6px}
.fig figcaption,.figcap{font-size:.85em;font-style:italic;margin-top:6px}
.ops.cuatro{grid-template-columns:repeat(4,1fr)}.opsfig svg{max-width:760px}
"""


# ─────────────────────────────── verificación ───────────────────────────────
def _norm(t):
    t = unicodedata.normalize("NFKC", t).lower()
    t = re.sub(r"[₀-₉]", lambda m: str("₀₁₂₃₄₅₆₇₈₉".index(m.group(0))), t)
    return re.sub(r"[^\w%$]+", " ", t).strip()


def _modulo(mis):
    src = open(f"/home/claude/libro/qui{mis}_icfes.py", encoding="utf-8").read()
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
             if r["mision"].strip() == f"QUI M{mis}"]
    return {i + 1: r for i, r in enumerate(filas)}


def verificar(icfes=None):
    """Diferencias entre el .md, los módulos quiN_icfes.py y tablero/icfes.csv (lista vacía = todo bien)."""
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
            if not v["enunciado"]:
                malas.append(f"M{mis} P{k}: sin enunciado")
            if claves.get(q) != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · qui{mis}_icfes.py {claves.get(q)}")
            if tab.get(k, {}).get("clave", "").strip() != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · icfes.csv {tab.get(k, {}).get('clave')}")
            if "ASED" in tab.get(k, {}).get("fuente", "") and "ASED" not in v["fuente"]:
                malas.append(f"M{mis} P{k}: sale del ASED y el .md no lo dice")
            mo = ops.get(q)
            if mo and len(mo) == 4:
                for L, a, b in zip("ABCD", mo, v["opciones"]):
                    if _norm(a) != _norm(b):
                        malas.append(f"M{mis} P{k} {L}: el .md no copia la opción del cuaderno")
            elif (mis, k) not in FIG_OPCIONES:
                malas.append(f"M{mis} P{k}: el módulo no trae opciones en texto y no hay figura de opciones")
            if (MARCA in v["texto"]) != ((mis, k) in FIGURAS):
                malas.append(f"M{mis} P{k}: marca de figura y FIGURAS no coinciden")
            if not v["verificacion"]:
                malas.append(f"M{mis} P{k}: falta «Verificada resolviéndola»")
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
                  + (" · figura" if (m, k) in FIGURAS else "") + (" · figura de opciones" if (m, k) in FIG_OPCIONES else ""))
    malas = verificar(d)
    print("claves y opciones: todo coincide" if not malas else "\n".join(["DIFERENCIAS:"] + malas))
