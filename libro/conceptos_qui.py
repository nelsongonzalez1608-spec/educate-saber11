"""Conceptualización de Química (ver conceptos.py y conceptos_area.py): las seis misiones.

Al inicio de cada clase de contenido (3 de los 15 minutos de la Activación) el profe proyecta el
vocabulario de la misión y el «mapa de la misión»: una idea central y una tarjeta por estrategia, que se
abre como infografía (dibujo, definición corta, esquema, ejemplo propio, el «ojo» y la pregunta de
«comprueba», que va al planeador). Modelo aprobado: conceptos_mate.py.

Fuentes: plan_qui.py (MISIONES: estrategias, «instala» y «ojo»; TALLER, el banco ICFES y «Si Química
no es tu fuerte»), clase_viva_qui.py y TEXTOS_QUI.md. Los nombres de las estrategias son los de
plan_qui.MISIONES[mis]["estr"].

Los ejemplos son PROPIOS: no repiten los casos, datos ni opciones de las 10 preguntas del taller ni de
las 4 de entrenamiento (nada de nitrato de potasio, aspirina, hierro y azufre, sal y azúcar en la bodega,
parafina, propano, hielo seco, mercurio, tableta efervescente, cafetera de sifón, polvos en aceite,
minería artesanal, cafeína, PLA, biodiésel, clavo oxidado, gel con almidón ni quesos), para que la
conceptualización no resuelva el taller por adelantado.

Cuentas verificadas: H₂O = 18 g/mol, CO₂ = 44 g/mol, NaCl = 58,5 g/mol; 54 g de agua = 3 mol; 0,5 mol de
NaCl = 29,25 g; 100 g de agua de 20 a 100 °C = 100 · 4,18 · 80 = 33.440 J y evaporarla = 100 · 2.260 =
226.000 J; 10 · 4,18 · 5 = 209 J; 30 g en 20 cm³ = 1,5 g/cm³; C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O (O: 10 = 6 + 4);
2 H₂ + O₂ → 2 H₂O (4 g de H₂ = 2 mol → 36 g de agua); 12 g de C → 44 g de CO₂; de 4 a 1 mg/L es 75 % menos.
"""
import math
import random

from conceptos_figs import *                                         # noqa: F401,F403 (colores)
from conceptos_figs import _svg, _t, _caja, _flecha, _tarjeta, _bien, _mal, _claro

AGUA = "#E3EFF8"


def _vaso(x, y, w, h, nivel, fill, sw=3):
    """Vaso de laboratorio (boca arriba) con líquido hasta la fracción nivel."""
    ly = y + h * (1 - nivel)
    return (f'<rect x="{x+3}" y="{ly:.0f}" width="{w-6}" height="{y+h-ly-3:.0f}" fill="{fill}"/>'
            f'<path d="M{x-6} {y} L{x} {y+6} L{x} {y+h} L{x+w} {y+h} L{x+w} {y+6} L{x+w+6} {y}" '
            f'fill="none" stroke="{TINTA}" stroke-width="{sw}" stroke-linejoin="round"/>')


def _molecula(x, y, c, r=16):
    """Agua: un oxígeno y dos hidrógenos."""
    return (f'<circle cx="{x-r*0.95:.0f}" cy="{y+r*0.6:.0f}" r="{r*0.55:.0f}" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
            f'<circle cx="{x+r*0.95:.0f}" cy="{y+r*0.6:.0f}" r="{r*0.55:.0f}" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{TINTA}" stroke-width="2"/>')


def _particulas(r, n, x0, x1, y0, y1, rad, fill, sep=24):
    pts, k = [], 0
    while len(pts) < n and k < 5000:
        k += 1
        p = (r.uniform(x0, x1), r.uniform(y0, y1))
        if all((p[0] - a) ** 2 + (p[1] - b) ** 2 > sep ** 2 for a, b in pts):
            pts.append(p)
    return pts


# ═══════════════════════ Misión 1 · cuentas, propiedades y disoluciones ═══════════════════════
def mol(c):
    """Centro M1: un mol de agua es un montón fijo de moléculas que pesa 18 g."""
    s = (f'<path d="M40 110 Q40 90 60 90 L200 90 Q220 90 220 110 L220 236 Q220 252 204 252 L56 252 Q40 252 40 236 Z" '
         f'fill="{_claro(c, .9)}" stroke="{TINTA}" stroke-width="3"/>')
    for k in range(9):
        x, y = 78 + (k % 3) * 52 + (k // 3 % 2) * 12, 128 + (k // 3) * 46
        s += _molecula(x, y, _claro(ROJO, .55), 13)
    s += (_t(130, 70, "1 mol de agua", 20, TINTA, "middle")
          + _flecha(232, 170, 280, 170, c)
          + f'<polygon points="296,204 396,204 386,226 306,226" fill="#EEF2F8" stroke="{TINTA}" stroke-width="2.5"/>'
          f'<rect x="300" y="160" width="92" height="44" rx="8" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
          + _t(346, 191, "18 g", 24, c, "middle")
          + _t(210, 282, "6,02 × 10²³ moléculas", 20, TINTA, "middle"))
    return _svg(s, "Un mol de agua: un montón fijo de moléculas que en la balanza pesa 18 gramos")


def regla_tres(c):
    """E1 M1: la regla de tres con la unidad pegada a cada número."""
    s = ""
    filas = [("18 g", "1 mol"), ("54 g", "x")]
    for k, (a, b) in enumerate(filas):
        y = 40 + k * 76
        s += (_tarjeta(40, y, 130, 56, a, c, 24) + _flecha(180, y + 28, 236, y + 28, TINTA, 3.5)
              + _tarjeta(246, y, 130, 56, b, c, 24))
    s += (_t(210, 210, "x = 54 g · 1 mol ÷ 18 g", 22, TINTA, "middle")
          + _t(210, 254, "= 3 mol   (los gramos se cancelan)", 22, c, "middle"))
    return _svg(s, "Regla de tres: 18 g son 1 mol, 54 g son x; los gramos se cancelan y quedan 3 mol")


def filtrado(c):
    """E2 M1: arena y sal se separan porque solo la sal se disuelve."""
    s = (f'<polygon points="120,60 300,60 226,150 194,150" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
         f'<polygon points="140,66 280,66 222,140 198,140" fill="{_claro(c, .85)}" stroke="{c}" stroke-width="2"/>'
         f'<rect x="200" y="150" width="20" height="40" fill="#fff" stroke="{TINTA}" stroke-width="3"/>')
    r = random.Random(2)
    for x, y in _particulas(r, 10, 160, 260, 84, 118, 0, "", 13):
        if 140 + (y - 66) * 0.78 < x < 280 - (y - 66) * 0.78:
            s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="5" fill="#C9821B"/>'
    s += (_vaso(150, 196, 120, 74, .55, AGUA)
          + f'<line x1="210" y1="190" x2="210" y2="232" stroke="{AZUL}" stroke-width="3" stroke-dasharray="4 5"/>'
          + _t(316, 104, "arena", 20, ORO) + f'<line x1="268" y1="98" x2="310" y2="98" stroke="{TINTA}" stroke-width="1.8"/>'
          + _t(286, 246, "agua con sal", 20, TINTA)
          + _t(20, 40, "la sal se disuelve; la arena no", 18, c))
    return _svg(s, "Un embudo con filtro retiene la arena; abajo pasa el agua con la sal disuelta")


def solubilidad(c):
    """E3 M1: curvas de solubilidad: el sólido sube con la temperatura, el gas baja."""
    s = (f'<line x1="60" y1="240" x2="390" y2="240" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="60" y1="240" x2="60" y2="40" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M60 200 Q220 180 380 60" fill="none" stroke="{c}" stroke-width="6" stroke-linecap="round"/>'
         f'<path d="M60 110 Q200 190 380 220" fill="none" stroke="{TINTA}" stroke-width="5" stroke-linecap="round" stroke-dasharray="12 8"/>'
         + _t(300, 70, "sólido", 20, c) + _t(300, 196, "gas", 20, TINTA)
         + _t(72, 36, "g por 100 g de agua", 18, GRIS, w="600")
         + _t(390, 270, "temperatura →", 18, GRIS, "end", "600"))
    return _svg(s, "Curvas de solubilidad: la del sólido sube con la temperatura y la del gas baja")


def choques(c):
    """E4 M1: para reaccionar, las partículas chocan con energía."""
    s = ""
    for x, y, col in [(120, 120, _claro(c, .55)), (300, 120, "#FDF5E7")]:
        s += f'<circle cx="{x}" cy="{y}" r="34" fill="{col}" stroke="{TINTA}" stroke-width="2.5"/>'
    for k in range(3):
        s += (f'<line x1="{40 - k*4}" y1="{104 + k*16}" x2="{74 - k*4}" y2="{104 + k*16}" stroke="{GRIS}" stroke-width="3" stroke-linecap="round"/>'
              f'<line x1="{346 + k*4}" y1="{104 + k*16}" x2="{380 + k*4}" y2="{104 + k*16}" stroke="{GRIS}" stroke-width="3" stroke-linecap="round"/>')
    pts = " ".join(f"{210 + (26 if k % 2 == 0 else 12) * math.cos(k * math.pi / 6):.0f},"
                   f"{120 + (26 if k % 2 == 0 else 12) * math.sin(k * math.pi / 6):.0f}" for k in range(12))
    s += (f'<polygon points="{pts}" fill="{ORO}" opacity=".85"/>'
          + _flecha(160, 120, 180, 120, TINTA, 3) + _flecha(260, 120, 240, 120, TINTA, 3)
          + _t(210, 200, "chocan con energía", 20, TINTA, "middle")
          + _t(210, 240, "más calor · trozos pequeños · catalizador", 18, c, "middle"))
    return _svg(s, "Dos partículas que chocan con energía; el choque se acelera con calor, trozos pequeños o un catalizador")


# ═══════════════════════ Misión 2 · calor, estados y densidad ═══════════════════════
def piscina_taza(c):
    """Centro M2: la piscina tibia guarda más calor que la taza hirviendo."""
    s = (_caja(20, 170, 200, 60, 44, "#fff", "#D3DCEA", "#EEF2F8")
         + f'<polygon points="22,172 218,172 262,146 66,146" fill="{AGUA}"/>'
         + _t(120, 210, "piscina tibia", 20, TINTA, "middle")
         + f'<path d="M300 150 L300 220 Q300 236 316 236 L356 236 Q372 236 372 220 L372 150 Z" fill="#FDF5E7" stroke="{TINTA}" stroke-width="3"/>'
         f'<path d="M372 168 Q396 168 396 186 Q396 204 372 204" fill="none" stroke="{TINTA}" stroke-width="3"/>')
    for k in range(3):
        x = 314 + k * 22
        s += f'<path d="M{x} 136 q8 -12 0 -24 q-8 -12 0 -24" fill="none" stroke="{ROJO}" stroke-width="3" stroke-linecap="round"/>'
    s += (_t(336, 270, "taza hirviendo", 18, TINTA, "middle")
          + _t(120, 270, "más calor guardado", 18, c, "middle")
          + _t(30, 50, "calor ≠ temperatura", 22, c))
    return _svg(s, "Una piscina tibia guarda más calor que una taza hirviendo, aunque esté menos caliente")


def curva_calentamiento(c):
    """E1 M2: curva de calentamiento con dos mesetas."""
    s = (f'<line x1="50" y1="250" x2="395" y2="250" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="50" y1="250" x2="50" y2="30" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polyline points="50,230 100,180 180,180 230,110 340,110 390,50" fill="none" stroke="{c}" stroke-width="6" '
         f'stroke-linejoin="round" stroke-linecap="round"/>'
         f'<rect x="100" y="170" width="80" height="20" fill="{_claro(c, .8)}" opacity=".8"/>'
         f'<rect x="230" y="100" width="110" height="20" fill="{_claro(c, .8)}" opacity=".8"/>'
         + _t(140, 216, "fusión", 20, TINTA, "middle") + _t(285, 146, "ebullición", 20, TINTA, "middle")
         + _t(58, 40, "°C", 20, GRIS)
         + _t(390, 278, "tiempo (entra calor) →", 18, GRIS, "end", "600"))
    return _svg(s, "Curva de calentamiento: sube, se queda quieta en la fusión, sube y se queda quieta en la ebullición")


def tramos(c):
    """E2 M2: el calor total se arma por tramos."""
    s = ""
    datos = [(40, 100, "m·c·ΔT", "sube T", "#fff"), (140, 150, "m·L", "cambia estado", _claro(c, .75)),
             (290, 90, "m·c·ΔT", "sube T", "#fff")]
    for x, w, f, rot, fill in datos:
        s += (f'<rect x="{x}" y="100" width="{w}" height="70" fill="{fill}" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x + w / 2, 142, f, 22, TINTA, "middle") + _t(x + w / 2, 84, rot, 18, GRIS, "middle", "600"))
    s += (f'<path d="M40 190 Q40 204 60 204 L190 204 Q210 204 210 222 Q210 204 230 204 L360 204 Q380 204 380 190" '
          f'fill="none" stroke="{c}" stroke-width="3.5"/>'
          + _t(210, 256, "Q total = la suma de los tramos", 20, c, "middle"))
    return _svg(s, "Tres tramos de calor: dos donde sube la temperatura y uno de cambio de estado; se suman")


def particulas_temp(c):
    """E3 M2: partículas lentas en frío, rápidas y con más choques en caliente."""
    s = ""
    r = random.Random(11)
    for k, (x0, tit, larga) in enumerate([(30, "frío", 10), (230, "caliente", 34)]):
        s += f'<rect x="{x0}" y="40" width="160" height="170" rx="10" fill="{"#fff" if k == 0 else _claro(c, .9)}" stroke="{TINTA}" stroke-width="3"/>'
        for x, y in _particulas(r, 6, x0 + 30, x0 + 130, 70, 180, 0, "", 34):
            a = r.uniform(0, 2 * math.pi)
            s += (f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{x - larga*math.cos(a):.0f}" y2="{y - larga*math.sin(a):.0f}" '
                  f'stroke="{GRIS}" stroke-width="3" stroke-linecap="round"/>'
                  f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="{c if k else _claro(c, .5)}"/>')
        s += _t(x0 + 80, 244, tit, 20, TINTA, "middle")
    s += _t(210, 280, "más rápidas, más choques, más presión", 18, c, "middle")
    return _svg(s, "Dos cajas: en frío las partículas van lentas; en caliente van rápido y chocan más")


def capas_densidad(c):
    """E4 M2: lo más denso abajo, lo menos denso arriba."""
    s = (f'<rect x="120" y="80" width="110" height="60" fill="#FFF6D8"/>'
         f'<rect x="120" y="140" width="110" height="60" fill="{AGUA}"/>'
         f'<rect x="120" y="200" width="110" height="52" fill="#F1DDB8"/>'
         f'<path d="M112 40 L120 48 L120 252 L230 252 L230 48 L238 40" fill="none" stroke="{TINTA}" stroke-width="3"/>')
    for y, n, d in [(116, "aceite", "0,9"), (176, "agua", "1,0"), (232, "miel", "1,4")]:
        s += (f'<line x1="234" y1="{y-6}" x2="256" y2="{y-6}" stroke="{TINTA}" stroke-width="1.8"/>'
              + _t(262, y, n, 20, TINTA) + _t(400, y, d, 20, c, "end"))
    s += (_t(400, 60, "g/cm³", 18, GRIS, "end", "600")
          + _t(60, 100, "menos", 18, GRIS, "middle", "600") + _t(60, 122, "denso", 18, GRIS, "middle", "600")
          + _t(60, 214, "más", 18, GRIS, "middle", "600") + _t(60, 236, "denso", 18, GRIS, "middle", "600")
          + _flecha(60, 136, 60, 192, c, 3.5))
    return _svg(s, "Un vaso con miel abajo, agua en medio y aceite arriba, ordenados por densidad")


# ═══════════════════════ Misión 3 · mezclas, gases y evidencia ═══════════════════════
def mezcla_cambio(c):
    """Centro M3: en la mezcla las partículas siguen iguales; en el cambio químico se unen en otras."""
    s = ""
    for k, tit in enumerate(["mezcla", "cambio químico"]):
        x0 = 20 + k * 200
        s += (f'<rect x="{x0}" y="50" width="180" height="170" rx="14" fill="{"#fff" if k == 0 else _claro(c, .9)}" '
              f'stroke="{TINTA}" stroke-width="2.5"/>' + _t(x0 + 90, 36, tit, 20, TINTA, "middle"))
    for x, y in [(60, 90), (120, 100), (80, 160), (150, 170), (160, 90)]:
        s += f'<circle cx="{x}" cy="{y}" r="13" fill="{_claro(c, .5)}" stroke="{TINTA}" stroke-width="2"/>'
    for x, y in [(100, 128), (50, 196), (130, 200), (66, 128)]:
        s += f'<rect x="{x-11}" y="{y-11}" width="22" height="22" fill="#FDF5E7" stroke="{TINTA}" stroke-width="2"/>'
    for x, y in [(260, 100), (340, 110), (290, 180), (360, 186)]:
        s += (f'<circle cx="{x}" cy="{y}" r="13" fill="{_claro(c, .5)}" stroke="{TINTA}" stroke-width="2"/>'
              f'<rect x="{x+11}" y="{y-11}" width="22" height="22" fill="#FDF5E7" stroke="{TINTA}" stroke-width="2"/>')
    s += (_t(110, 252, "siguen iguales", 18, GRIS, "middle", "600")
          + _t(310, 252, "aparece algo nuevo", 18, c, "middle"))
    return _svg(s, "Mezcla: las partículas siguen separadas e iguales; cambio químico: se unen en una sustancia nueva")


def perillas(c):
    """E1 M3: una sola perilla se mueve; las demás quedan fijas."""
    s = ""
    for k, (n, pos, cambia) in enumerate([("temperatura", .4, False), ("cantidad", .6, False), ("luz", .75, True)]):
        y = 60 + k * 76
        col = c if cambia else GRIS
        s += (_t(20, y + 7, n, 20, TINTA)
              + f'<line x1="150" y1="{y}" x2="330" y2="{y}" stroke="#C9D1DC" stroke-width="8" stroke-linecap="round"/>'
              f'<circle cx="{150 + 180*pos:.0f}" cy="{y}" r="14" fill="{_claro(c, .5) if cambia else "#fff"}" stroke="{col}" stroke-width="3.5"/>')
        if cambia:
            s += _flecha(240, y + 26, 300, y + 26, c, 3) + _t(400, y + 7, "cambia", 18, c, "end")
        else:
            s += (f'<rect x="352" y="{y-6}" width="26" height="20" rx="3" fill="#fff" stroke="{GRIS}" stroke-width="2.5"/>'
                  f'<path d="M357 {y-6} L357 {y-13} A8 8 0 0 1 373 {y-13} L373 {y-6}" fill="none" stroke="{GRIS}" stroke-width="2.5"/>')
    s += _t(210, 280, "cambio una cosa; lo demás, igual", 18, TINTA, "middle", "600")
    return _svg(s, "Tres perillas: temperatura y cantidad con candado; solo la luz cambia")


def fases(c):
    """E2 M3: una fase (homogénea) o dos o más (heterogénea)."""
    s = (_vaso(60, 60, 110, 160, .8, _claro(c, .75))
         + _vaso(250, 60, 110, 160, .8, AGUA)
         + f'<rect x="253" y="190" width="104" height="27" fill="#F1DDB8"/>')
    r = random.Random(4)
    for x, y in _particulas(r, 7, 262, 348, 195, 212, 0, "", 12):
        s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="#8A6A3A"/>'
    s += (_t(115, 250, "1 fase", 20, TINTA, "middle") + _t(115, 276, "homogénea", 18, c, "middle")
          + _t(305, 250, "2 fases", 20, TINTA, "middle") + _t(305, 276, "heterogénea", 18, c, "middle"))
    return _svg(s, "Dos vasos: uno con una sola fase y otro con arena asentada en el fondo")


def jeringas(c):
    """E3 M3: el mismo gas en más o en menos espacio."""
    s = ""
    r = random.Random(8)
    for k, (largo, y) in enumerate([(200, 60), (110, 170)]):
        x0 = 40
        s += (f'<rect x="{x0}" y="{y}" width="230" height="56" rx="6" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
              f'<rect x="{x0+largo}" y="{y+4}" width="12" height="48" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2"/>'
              f'<line x1="{x0+largo+12}" y1="{y+28}" x2="{x0+largo+110}" y2="{y+28}" stroke="{TINTA}" stroke-width="5"/>'
              f'<rect x="{x0+largo+110}" y="{y+6}" width="10" height="44" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2"/>'
              f'<rect x="{x0-10}" y="{y+22}" width="10" height="12" fill="{TINTA}"/>')
        for x, yy in _particulas(r, 7, x0 + 14, x0 + largo - 12, y + 12, y + 44, 0, "", 15 if k else 24):
            s += f'<circle cx="{x:.0f}" cy="{yy:.0f}" r="6" fill="{c}"/>'
    s += (_t(40, 146, "más espacio: menos presión", 18, TINTA, w="600")
          + _t(40, 256, "menos espacio: más presión", 18, c))
    return _svg(s, "Dos jeringas tapadas: con el émbolo afuera el gas empuja poco; comprimido, empuja más")


def pistas(c):
    """E4 M3: las pistas de un cambio químico."""
    s = ""
    nombres = ["gas", "color", "calor", "sólido"]
    for k, n in enumerate(nombres):
        x = 22 + k * 100
        s += _vaso(x + 10, 80, 72, 110, .7, AGUA if k != 1 else _claro(c, .55))
        if k == 0:
            for j, (dx, dy) in enumerate([(22, 150), (44, 130), (30, 110), (52, 160)]):
                s += f'<circle cx="{x+dx}" cy="{dy}" r="{4 + j % 2 * 2}" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
        if k == 2:
            s += (f'<rect x="{x+42}" y="56" width="10" height="110" rx="5" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
                  f'<rect x="{x+44}" y="100" width="6" height="64" fill="{ROJO}"/>'
                  f'<circle cx="{x+47}" cy="170" r="9" fill="{ROJO}"/>')
        if k == 3:
            s += f'<path d="M{x+14} 186 Q{x+46} 168 {x+78} 186 Z" fill="#8A6A3A"/>'
        s += _t(x + 46, 226, n, 20, TINTA, "middle")
    s += _t(210, 272, "lo que se ve y no estaba en el testigo", 18, c, "middle")
    return _svg(s, "Cuatro vasos con pistas de un cambio químico: burbujas, color nuevo, calor y un sólido")


# ═══════════════════════ Misión 4 · propiedades que separan ═══════════════════════
def propiedades(c):
    """Centro M4: una sustancia, varias propiedades físicas."""
    s = (_caja(160, 120, 100, 90, 30, _claro(c, .85), _claro(c, .65), "#fff")
         + _t(210, 172, "sustancia", 18, TINTA, "middle"))
    for x, y, n in [(14, 30, "densidad"), (276, 30, "ebullición"), (14, 226, "conductividad"), (276, 226, "magnetismo")]:
        s += _tarjeta(x, y, 130, 42, n, c, 18)
    s += (f'<line x1="144" y1="60" x2="168" y2="96" stroke="{GRIS}" stroke-width="2"/>'
          f'<line x1="276" y1="60" x2="268" y2="96" stroke="{GRIS}" stroke-width="2"/>'
          f'<line x1="144" y1="236" x2="160" y2="212" stroke="{GRIS}" stroke-width="2"/>'
          f'<line x1="276" y1="236" x2="262" y2="212" stroke="{GRIS}" stroke-width="2"/>')
    return _svg(s, "Una sustancia con cuatro propiedades físicas alrededor")


def igualdad(c):
    """E1 M4: dos vasos con las mismas condiciones."""
    s = _vaso(70, 40, 100, 110, .6, AGUA) + _vaso(250, 40, 100, 110, .6, _claro(c, .75))
    for k, cond in enumerate(["100 mL", "20 °C", "5 min"]):
        y = 172 + k * 34
        s += (_tarjeta(70, y, 100, 28, cond, GRIS, 18) + _tarjeta(250, y, 100, 28, cond, GRIS, 18)
              + _bien(196, y + 12, VERDE))
    s += _t(120, 30, "A", 20, TINTA, "middle") + _t(300, 30, "B", 20, TINTA, "middle")
    return _svg(s, "Dos vasos A y B con la misma cantidad, la misma temperatura y el mismo tiempo")


def sedimenta(c):
    """E2 M4: grandes abajo rápido, finas suspendidas."""
    s = (f'<rect x="83" y="44" width="114" height="216" fill="{AGUA}"/>'
         f'<path d="M72 36 L80 44 L80 262 L200 262 L200 44 L208 36" fill="none" stroke="{TINTA}" stroke-width="3"/>')
    r = random.Random(6)
    for x, y in _particulas(r, 22, 92, 188, 60, 200, 0, "", 14):
        s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="2.8" fill="{GRIS}"/>'
    for k in range(4):
        s += f'<circle cx="{102 + k*26}" cy="244" r="12" fill="#8A6A3A"/>'
    for k in range(5):
        s += f'<circle cx="{98 + k*21}" cy="{222 - (k % 2) * 4}" r="7" fill="#C9A26A"/>'
    s += (f'<line x1="204" y1="100" x2="228" y2="100" stroke="{TINTA}" stroke-width="1.8"/>' + _t(234, 106, "finas: suspendidas", 18)
          + f'<line x1="204" y1="220" x2="228" y2="220" stroke="{TINTA}" stroke-width="1.8"/>' + _t(234, 226, "medianas", 18)
          + f'<line x1="204" y1="246" x2="228" y2="246" stroke="{TINTA}" stroke-width="1.8"/>' + _t(234, 252, "grandes: al fondo", 18, c))
    return _svg(s, "Una probeta con partículas grandes en el fondo, medianas encima y finas suspendidas")


def etiquetas(c):
    """E3 M4: cada propiedad con su nombre y su unidad."""
    s = ""
    for k, (n, u) in enumerate([("densidad", "g/cm³"), ("ebullición", "°C"), ("conductividad", "¿pasa corriente?")]):
        x = 10 + k * 136
        s += (f'<path d="M{x} 70 L{x+30} 40 L{x+100} 40 L{x+130} 70 L{x+130} 220 L{x} 220 Z" fill="{"#fff" if k != 2 else _claro(c, .88)}" '
              f'stroke="{c}" stroke-width="3"/>'
              f'<circle cx="{x+65}" cy="62" r="8" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x + 65, 120, n, 18, TINTA, "middle"))
        if k < 2:
            s += _t(x + 65, 170, u, 26, c, "middle")
        else:
            s += (f'<circle cx="{x+65}" cy="160" r="20" fill="#FFF6D8" stroke="{TINTA}" stroke-width="2.5"/>'
                  f'<rect x="{x+56}" y="180" width="18" height="16" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2"/>')
    s += _t(210, 268, "nómbrala bien: es media respuesta", 20, c, "middle")
    return _svg(s, "Tres etiquetas: densidad en g/cm³, ebullición en °C y conductividad con un bombillo")


def destilacion(c):
    """E4 M4: la destilación separa por punto de ebullición."""
    s = (f'<circle cx="90" cy="150" r="50" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
         f'<path d="M48 172 A50 50 0 0 0 132 172 Z" fill="{_claro(c, .75)}"/>'
         f'<rect x="80" y="70" width="20" height="40" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
         f'<line x1="100" y1="84" x2="300" y2="170" stroke="{TINTA}" stroke-width="12" stroke-linecap="round"/>'
         f'<line x1="100" y1="84" x2="300" y2="170" stroke="{AGUA}" stroke-width="6" stroke-linecap="round"/>'
         f'<path d="M80 214 Q90 194 100 214 Q96 232 90 232 Q84 232 80 214 Z" fill="{ORO}"/>'
         + _vaso(290, 186, 70, 70, .4, _claro(c, .85))
         + f'<circle cx="300" cy="178" r="4" fill="{c}"/>'
         + _t(90, 266, "agua: 100 °C", 18, TINTA, "middle", "600")
         + _t(326, 280, "alcohol: 78 °C", 18, c, "middle")
         + _t(210, 54, "hierve primero el alcohol", 18, TINTA, "middle", "600"))
    return _svg(s, "Destilación: el alcohol hierve primero, sube por el tubo y cae en otro vaso; el agua queda")


# ═══════════════════════ Misión 5 · el carbono ═══════════════════════
def ciclo_carbono(c):
    """Centro M5: el carbono pasa del combustible al aire y a la planta."""
    s = (_tarjeta(140, 24, 140, 46, "CO₂ del aire", c, 20, _claro(c, .9))
         + _tarjeta(16, 200, 140, 46, "combustible", TINTA, 20)
         + _tarjeta(264, 200, 140, 46, "planta", VERDE, 20, "#EAF4EC")
         + _flecha(100, 192, 168, 80, ORO) + _flecha(256, 80, 320, 190, VERDE) + _flecha(256, 223, 166, 223, GRIS)
         + _t(98, 128, "arde", 18, ORO, "middle") + _t(330, 128, "lo toma", 18, VERDE, "middle")
         + _t(210, 268, "con los años", 18, GRIS, "middle", "600"))
    return _svg(s, "El carbono pasa del combustible al CO₂ del aire, de ahí a la planta y vuelve")


def grupo_funcional(c):
    """E1 M5: una cadena de carbonos con un –OH al final."""
    pts = [(40, 170), (90, 140), (140, 170), (190, 140), (240, 170)]
    s = f'<polyline points="{" ".join(f"{x},{y}" for x, y in pts)} 290,140" fill="none" stroke="{TINTA}" stroke-width="5" stroke-linejoin="round"/>'
    for x, y in pts:
        s += f'<circle cx="{x}" cy="{y}" r="11" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
    s += (f'<circle cx="306" cy="130" r="30" fill="{_claro(c, .6)}" stroke="{c}" stroke-width="3.5"/>'
          + _t(306, 138, "OH", 22, TINTA, "middle")
          + _t(306, 62, "polar: se lleva", 18, c, "middle") + _t(306, 84, "con el agua", 18, c, "middle")
          + f'<path d="M370 168 Q382 186 370 196 Q358 186 370 168 Z" fill="{AGUA}" stroke="{AZUL}" stroke-width="2"/>'
          f'<path d="M390 196 Q402 214 390 224 Q378 214 390 196 Z" fill="{AGUA}" stroke="{AZUL}" stroke-width="2"/>'
          + _t(140, 222, "cadena C–H: no se mezcla", 18, TINTA, "middle", "600")
          + _t(210, 270, "el grupo decide cómo se comporta", 20, c, "middle"))
    return _svg(s, "Una cadena de carbonos que termina en un grupo OH, polar, que se lleva con el agua")


def conteo(c):
    """E2 M5: se cuentan los átomos a cada lado de la flecha."""
    s = _t(210, 40, "CH₄ + 2 O₂ → CO₂ + 2 H₂O", 24, TINTA, "middle")
    filas = [("C", 1, TINTA, "#fff"), ("H", 4, "#fff", TINTA), ("O", 4, _claro(ROJO, .5), TINTA)]
    for k, (el, n, fill, _) in enumerate(filas):
        y = 90 + k * 56
        for lado, x0 in enumerate((40, 250)):
            s += _t(x0, y + 7, el, 20, TINTA)
            for j in range(n):
                s += f'<circle cx="{x0 + 34 + j*26}" cy="{y}" r="10" fill="{fill}" stroke="{TINTA}" stroke-width="2"/>'
        s += _t(210, y + 9, "=", 26, c, "middle")
    s += _t(210, 270, "lo que entra = lo que sale", 20, c, "middle")
    return _svg(s, "Conteo de átomos: un carbono, cuatro hidrógenos y cuatro oxígenos a cada lado de la flecha")


def tablilla(c):
    """E3 M5: lo que la tabla deja afirmar y lo que no."""
    s = (f'<rect x="30" y="50" width="170" height="210" rx="12" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
         f'<rect x="80" y="38" width="70" height="24" rx="6" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(115, 100, "cloro (mg/L)", 18, GRIS, "middle", "600")
         + _t(50, 150, "antes", 20, TINTA) + _t(180, 150, "4", 22, TINTA, "end")
         + _t(50, 196, "después", 20, TINTA) + _t(180, 196, "1", 22, c, "end"))
    s += (_tarjeta(220, 76, 180, 50, "bajó un 75 %", VERDE, 20) + _bien(370, 154, VERDE)
          + _tarjeta(220, 186, 180, 50, "eliminó el cloro", ROJO, 20) + _mal(372, 250, ROJO))
    return _svg(s, "Una tabla con 4 y 1 mg/L: se puede decir que bajó un 75 %, no que eliminó el cloro")


def llamas(c):
    """E4 M5: con aire suficiente o sin él."""
    s = ""
    for k, (x, col, fondo, l1, l2) in enumerate([(110, AZUL, "#E6ECF8", "mucho aire", "CO₂ + H₂O"),
                                                  (310, ORO, "#FDF0D5", "poco aire", "CO + hollín")]):
        s += (f'<rect x="{x-50}" y="190" width="100" height="22" rx="6" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<path d="M{x} 70 Q{x+46} 140 {x+30} 176 Q{x} 196 {x-30} 176 Q{x-46} 140 {x} 70 Z" fill="{fondo}" stroke="{col}" stroke-width="4"/>'
              f'<path d="M{x} 120 Q{x+18} 156 {x} 180 Q{x-18} 156 {x} 120 Z" fill="{col}" opacity=".6"/>'
              + _t(x, 244, l1, 20, TINTA, "middle") + _t(x, 272, l2, 20, c if k else TINTA, "middle"))
    for k in range(3):
        s += f'<circle cx="{300 + k*12}" cy="{50 - k*10}" r="{8 + k*2}" fill="{GRIS}" opacity=".55"/>'
    return _svg(s, "Dos llamas: azul con mucho aire da CO₂ y agua; amarilla con poco aire da CO y hollín")


# ═══════════════════════ Misión 6 · reacciones y energía ═══════════════════════
def reaccion(c):
    """Centro M6: los átomos se reacomodan y la energía entra o sale."""
    def par(x, y, a, b):
        return (f'<circle cx="{x}" cy="{y}" r="18" fill="{a}" stroke="{TINTA}" stroke-width="2.5"/>'
                f'<circle cx="{x+30}" cy="{y}" r="18" fill="{b}" stroke="{TINTA}" stroke-width="2.5"/>')
    A, B = _claro(c, .55), "#FDF5E7"
    s = (par(40, 110, A, A) + par(40, 180, B, B)
         + _flecha(130, 145, 250, 145, TINTA, 4)
         + f'<path d="M150 120 q10 -14 20 0 t20 0 t20 0 t20 0" fill="none" stroke="{ORO}" stroke-width="3.5"/>'
         + _t(190, 96, "energía", 18, ORO, "middle")
         + par(290, 110, A, B) + par(290, 180, A, B)
         + _t(70, 248, "reactivos", 20, TINTA, "middle") + _t(320, 248, "productos", 20, c, "middle"))
    return _svg(s, "Reactivos que se reacomodan en productos, con energía que entra o sale")


def receta(c):
    """E1 M6: la ecuación es una receta en moles."""
    def h2(x, y):
        return (f'<circle cx="{x}" cy="{y}" r="9" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
                f'<circle cx="{x+16}" cy="{y}" r="9" fill="#fff" stroke="{TINTA}" stroke-width="2"/>')
    s = (f'<rect x="20" y="20" width="380" height="250" rx="16" fill="#fff" stroke="{c}" stroke-width="3"/>'
         + _t(210, 58, "2 H₂ + O₂ → 2 H₂O", 26, TINTA, "middle")
         + h2(60, 110) + h2(60, 140)
         + _t(116, 132, "+", 24, TINTA, "middle")
         + f'<circle cx="146" cy="125" r="14" fill="{_claro(ROJO, .5)}" stroke="{TINTA}" stroke-width="2"/>'
         f'<circle cx="172" cy="125" r="14" fill="{_claro(ROJO, .5)}" stroke="{TINTA}" stroke-width="2"/>'
         + _flecha(206, 125, 248, 125, TINTA, 3.5)
         + _molecula(290, 110, _claro(ROJO, .5), 14) + _molecula(350, 110, _claro(ROJO, .5), 14)
         + _t(210, 196, "en moles: 2 : 1 : 2", 22, c, "middle")
         + _t(210, 236, "gramos → moles → moles → gramos", 18, GRIS, "middle", "600"))
    return _svg(s, "Receta: dos moléculas de hidrógeno y una de oxígeno dan dos de agua")


def calor_sale_entra(c):
    """E2 M6: exotérmica (sale calor) y endotérmica (entra calor)."""
    s = ""
    for k, (x, col, tit, dh) in enumerate([(70, ROJO, "exotérmica", "ΔH negativo"), (270, AZUL, "endotérmica", "ΔH positivo")]):
        s += (_vaso(x, 90, 90, 100, .7, "#FBEFEF" if k == 0 else "#E6ECF8")
              + f'<rect x="{x+56}" y="50" width="10" height="120" rx="5" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
              f'<rect x="{x+58}" y="{70 if k == 0 else 130}" width="6" height="{100 if k == 0 else 40}" fill="{col}"/>'
              f'<circle cx="{x+61}" cy="174" r="8" fill="{col}"/>'
              + _t(x + 45, 236, tit, 20, TINTA, "middle") + _t(x + 45, 262, dh, 18, col, "middle"))
    for k in range(3):
        y = 110 + k * 26
        s += _flecha(166, y, 196, y, ROJO, 3.5) + _flecha(258, y, 230, y, AZUL, 3.5)
    s += _t(102, 34, "sale calor", 18, ROJO, "middle") + _t(316, 34, "entra calor", 18, AZUL, "middle")
    return _svg(s, "Dos vasos con termómetro: en la exotérmica sale calor y sube; en la endotérmica entra calor y baja")


def pilares(c):
    """E3 M6: la conclusión se sostiene en sus datos."""
    s = (f'<polygon points="40,96 380,96 210,30" fill="{_claro(c, .85)}" stroke="{TINTA}" stroke-width="3"/>'
         + _t(210, 84, "conclusión", 20, TINTA, "middle"))
    for k, ok in enumerate([True, True, False]):
        x = 70 + k * 110
        if ok:
            s += _caja(x, 100, 60, 150, 0, "#EEF2F8") + _t(x + 30, 180, "dato", 18, TINTA, "middle")
        else:
            s += (f'<rect x="{x}" y="100" width="60" height="150" fill="none" stroke="{ROJO}" stroke-width="3" stroke-dasharray="8 6"/>'
                  + _t(x + 30, 184, "?", 34, ROJO, "middle"))
    s += (f'<rect x="30" y="250" width="360" height="12" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2"/>'
          + _t(210, 282, "lo que no se midió no la sostiene", 18, c, "middle"))
    return _svg(s, "Un techo llamado conclusión sobre dos columnas de datos y un hueco donde falta un dato")


def polimero(c):
    """E4 M6: el monómero que se repite."""
    def hexa(cx, cy, r, fill, stroke, sw):
        pts = " ".join(f"{cx + r*math.cos(math.pi/6 + k*math.pi/3):.1f},{cy + r*math.sin(math.pi/6 + k*math.pi/3):.1f}"
                       for k in range(6))
        return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    s = ""
    for k in range(6):
        x = 50 + k * 64
        if k:
            s += f'<line x1="{x-64+26}" y1="140" x2="{x-26}" y2="140" stroke="{TINTA}" stroke-width="4"/>'
        on = k == 2
        s += hexa(x, 140, 26, _claro(c, .6) if on else "#fff", c if on else TINTA, 3.5 if on else 2.5)
    s += (f'<path d="M150 98 L150 88 L206 88 L206 98" fill="none" stroke="{c}" stroke-width="3"/>'
          + _t(178, 74, "monómero", 20, c, "middle")
          + _t(400, 205, "… y así miles de veces", 18, GRIS, "end", "600")
          + _t(210, 258, "polímero: la misma pieza repetida", 20, TINTA, "middle"))
    return _svg(s, "Una cadena de hexágonos iguales unidos: un polímero hecho de un monómero repetido")


# ═══════════════════════ los datos de las seis misiones ═══════════════════════
DATOS = {
    1: dict(
        titulo="Todo número trae su unidad",
        centro=("El mol", "una cantidad fija de partículas: 6,02 × 10²³, como una docena gigante", mol),
        centro_ej="un mol de agua (H₂O) pesa 2 · 1 + 16 = 18 g: cabe en poco más de una cucharada.",
        centro_ojo="mol no es lo mismo que gramo: para pasar de uno al otro se usa la masa molar.",
        centro_chequeo="¿Cuánto pesa un mol de CO₂ (C = 12, O = 16)? (44 g)",
        ideas={
            "La regla de tres con sus unidades": dict(
                corto="cada número con su unidad al lado",
                d="La regla de tres se arma con la unidad pegada a cada número: si arriba hay gramos, abajo "
                  "también. Al final las unidades repetidas se cancelan y queda la que pide la pregunta.",
                f="18 g → 1 mol;  54 g → x;  x = 54 · 1 ÷ 18 = 3 mol",
                ej="¿cuántos gramos son 0,5 mol de sal (NaCl, 58,5 g/mol)? 1 mol → 58,5 g; 0,5 mol → "
                   "0,5 · 58,5 = 29,25 g.",
                ojo="si la unidad del resultado no es la que piden (te piden gramos y te dio mol), la regla de "
                    "tres está montada al revés.",
                chequeo="Si 1 mol de O₂ pesa 32 g, ¿cuántos moles hay en 96 g? (3 mol)",
                svg=regla_tres),
            "La propiedad que la delata": dict(
                corto="lo que tiene ella y las otras no",
                d="Una sustancia se reconoce o se separa por una propiedad que las otras no tienen: el "
                  "magnetismo, la densidad, el punto de fusión, la solubilidad. El color o el tamaño del "
                  "pedazo casi nunca bastan.",
                f="propiedad que solo tiene una → la identifica o la separa",
                ej="arena y sal revueltas: el agua disuelve la sal y no la arena. Se filtra la arena y, al "
                   "evaporar el agua, vuelve la sal.",
                ojo="una propiedad que comparten todas no sirve para distinguir: si todas son blancas, el "
                    "color no delata a ninguna.",
                chequeo="El agua y el alcohol son incoloros. ¿Qué propiedad medirías para distinguirlos? (el punto de ebullición o la densidad)",
                svg=filtrado),
            "El tope de lo que se disuelve": dict(
                corto="solubilidad y disolución saturada",
                d="La solubilidad es lo máximo que se disuelve en una cantidad de agua a una temperatura. En el "
                  "tope la disolución está saturada y lo que sobra queda sólido. Casi todos los sólidos se "
                  "disuelven más en caliente; los gases, menos.",
                f="lo que sobra = lo que echo − el tope a esa temperatura",
                ej="a 20 °C, en 100 g de agua caben unos 36 g de sal de cocina: si echas 50 g, unos 14 g "
                   "se quedan en el fondo.",
                ojo="la solubilidad se da por cada 100 g de agua: si hay 200 g de agua, cabe el doble.",
                chequeo="Si en 100 g de agua caben 36 g de sal, ¿cuánto cabe en 50 g de agua? (18 g)",
                svg=solubilidad),
            "Lo que la reacción necesita": dict(
                corto="choques con energía suficiente",
                d="Para reaccionar, las partículas tienen que chocar con energía suficiente. Una reacción se "
                  "acelera con más temperatura, trozos más pequeños (más superficie), más concentración o un "
                  "catalizador.",
                f="más rápido: calor · trozos pequeños · concentración · catalizador",
                ej="el agua oxigenada se descompone despacio, pero sobre un pedazo de papa hace espuma de "
                   "inmediato: la papa trae catalasa, un catalizador.",
                ojo="el catalizador acelera la reacción, pero no se gasta ni cambia lo que se produce.",
                chequeo="¿Por qué la comida dura más en la nevera? (el frío hace más lentas las reacciones que la dañan)",
                svg=choques),
        },
        vocab=[("Mol", "6,02 × 10²³ partículas"),
               ("Masa molar", "lo que pesa un mol (g/mol)"),
               ("Soluto", "lo que se disuelve"),
               ("Solvente", "en lo que se disuelve, casi siempre agua"),
               ("Solubilidad", "lo máximo que se disuelve"),
               ("Saturada", "ya no admite más soluto"),
               ("Propiedad física", "se mide sin cambiar la sustancia"),
               ("Reactivo", "sustancia que entra a la reacción"),
               ("Catalizador", "acelera la reacción y no se gasta")]),
    2: dict(
        titulo="El calor hace dos trabajos",
        centro=("Calor y temperatura",
                "el calor es energía que pasa; la temperatura dice qué tan rápido se mueven las partículas",
                piscina_taza),
        centro_ej="una piscina tibia guarda mucho más calor que una taza de chocolate hirviendo, aunque la "
                  "taza esté más caliente: tiene muchísima más agua.",
        centro_ojo="calor y temperatura no son lo mismo: más cantidad de sustancia pide más calor para subir "
                   "los mismos grados.",
        centro_chequeo="Una olla con 2 L y otra con 1 L de agua, en el mismo fogón: ¿cuál tarda más en hervir? (la de 2 L)",
        ideas={
            "Donde la temperatura se queda quieta": dict(
                corto="la meseta: cambia el estado",
                d="En una curva de calentamiento, la meseta es el cambio de estado: entra calor, pero la "
                  "temperatura no sube, porque la energía se gasta en separar las partículas.",
                f="rampa: sube la temperatura   ·   meseta: cambia el estado",
                ej="al nivel del mar el agua hierve a 100 °C y se queda en 100 °C mientras hierve, aunque "
                   "subas el fogón.",
                ojo="la altura de la meseta dice a qué temperatura cambia el estado; el largo, cuánto calor "
                    "pide el cambio. Son dos datos distintos.",
                chequeo="En Bogotá el agua hierve cerca de 92 °C. Mientras hierve, ¿sigue subiendo la temperatura? (no: se queda quieta)",
                svg=curva_calentamiento),
            "El calor, tramo por tramo": dict(
                corto="calor sensible + calor latente",
                d="El calor de todo el proceso se parte en tramos: donde sube la temperatura, Q = m · c · ΔT "
                  "(calor sensible); en la meseta, Q = m · L (calor latente). Al final se suman los tramos.",
                f="Q = m · c · ΔT   ·   Q = m · L   ·   total = suma de tramos",
                ej="subir 100 g de agua de 20 a 100 °C pide 100 · 4,18 · 80 = 33.440 J; evaporarla toda, "
                   "100 · 2.260 = 226.000 J más.",
                ojo="en la meseta no se usa ΔT (vale cero): se usa el calor latente. Y revisa unidades: g "
                    "con J/g, kg con J/kg.",
                chequeo="¿Cuánto calor sube 10 g de agua 5 °C, con c = 4,18 J/g·°C? (209 J)",
                svg=tramos),
            "Lo explican los choques de partículas": dict(
                corto="más temperatura, más rapidez, más choques",
                d="La temperatura dice qué tan rápido se mueven las partículas. Si un gas encerrado se calienta, "
                  "sus partículas chocan más rápido y más seguido contra las paredes: sube la presión.",
                f="más temperatura → más rapidez → más choques → más presión",
                ej="una gota de colorante se riega más rápido en agua caliente que en agua fría: allá las "
                   "partículas se mueven y chocan más.",
                ojo="las partículas no se «dilatan» ni se «calientan» una por una: lo que cambia es qué tan "
                    "rápido se mueven y qué tan seguido chocan.",
                chequeo="Si un frasco cerrado con aire se enfría, ¿la presión adentro sube o baja? (baja: hay menos choques)",
                svg=particulas_temp),
            "Más denso abajo, menos denso arriba": dict(
                corto="densidad: masa ÷ volumen",
                d="Densidad es masa sobre volumen. Lo menos denso queda arriba y lo más denso se va al fondo. Lo "
                  "que sube un objeto en un líquido es el empuje: si es menos denso que el líquido, el empuje "
                  "le gana a su peso.",
                f="d = m ÷ V   (g/cm³)",
                ej="en un vaso con miel, agua y aceite, la miel (1,4 g/cm³) queda abajo, el agua (1,0) en "
                   "medio y el aceite (0,9) arriba.",
                ojo="lo pesado no siempre se hunde: un barco de acero flota porque, con el aire de adentro, su "
                    "densidad promedio es menor que la del agua.",
                chequeo="Un objeto de 30 g ocupa 20 cm³. ¿Flota en agua (1 g/cm³)? (no: su densidad es 1,5 g/cm³)",
                svg=capas_densidad),
        },
        vocab=[("Temperatura", "qué tan rápido se mueven las partículas"),
               ("Calor", "energía que pasa de lo caliente a lo frío"),
               ("Calor específico", "calor para subir 1 °C un gramo"),
               ("Calor latente", "calor para cambiar de estado"),
               ("Fusión", "de sólido a líquido"),
               ("Ebullición", "de líquido a gas, en todo el líquido"),
               ("Sublimación", "de sólido a gas, sin pasar por líquido"),
               ("Presión", "la fuerza de los choques sobre la pared"),
               ("Densidad", "masa ÷ volumen")]),
    3: dict(
        titulo="Mezclar no es transformar",
        centro=("Mezcla o cambio químico",
                "en una mezcla las sustancias siguen siendo las mismas; en un cambio químico aparece una nueva",
                mezcla_cambio),
        centro_ej="el agua con azúcar es una mezcla: si evaporas el agua, vuelve el azúcar. Un huevo frito "
                  "es un cambio químico: no vuelve a ser crudo.",
        centro_ojo="disolverse no es reaccionar: el azúcar desaparece de la vista, pero sigue ahí.",
        centro_chequeo="Quemar un papel, ¿es mezcla o cambio químico? (cambio químico: aparecen ceniza, humo y CO₂)",
        ideas={
            "Cambia una sola cosa a la vez": dict(
                corto="una variable cambia; lo demás, igual",
                d="Para saber qué causa un efecto se cambia una sola variable (la independiente), se mide el "
                  "resultado (la dependiente) y todo lo demás se deja igual. Un vaso testigo, sin el cambio, "
                  "sirve para comparar.",
                f="cambio 1 cosa → mido 1 cosa → lo demás, igual",
                ej="¿la luz daña la leche más rápido? Dos vasos iguales, la misma leche, la misma temperatura; "
                   "uno a la luz y otro en la oscuridad.",
                ojo="si cambias dos cosas a la vez y algo pasa, no sabes cuál de las dos lo causó.",
                chequeo="Alguien prueba un abono y además riega el doble. Si la planta crece más, ¿qué lo causó? (no se puede saber)",
                svg=perillas),
            "Clasifica por lo que se observa": dict(
                corto="homogénea o heterogénea",
                d="Una mezcla homogénea se ve como una sola fase, como el agua con sal. Una heterogénea deja "
                  "ver dos o más fases, como el agua con arena. Si en reposo se separa sola, es inestable.",
                f="1 fase: homogénea   ·   2 o más fases: heterogénea",
                ej="el granito, una ensalada o el agua con arena son heterogéneas; el aire limpio y el vinagre "
                   "son homogéneos.",
                ojo="se clasifica por lo que se ve, no por lo que dice la etiqueta. Si al reposar se asienta "
                    "algo, era heterogénea.",
                chequeo="Leche con chocolate en polvo que deja grumos en el fondo, ¿qué mezcla es? (heterogénea)",
                svg=fases),
            "Sigue al gas: presión y temperatura": dict(
                corto="más calor o menos espacio: más presión",
                d="Un gas encerrado empuja más si se calienta y menos si se enfría. Si se comprime, sube la "
                  "presión; si se le da espacio, baja. Si un vapor se enfría y vuelve líquido, ocupa mucho "
                  "menos y la presión cae.",
                f="P · V = constante (T fija)   ·   P ÷ T = constante (V fijo)",
                ej="tapa con el dedo una jeringa con aire y empuja el émbolo: el aire queda en menos espacio y "
                   "empuja más fuerte tu dedo.",
                ojo="en las cuentas de gases la temperatura va en kelvin (°C + 273): en grados Celsius las "
                    "proporciones salen mal.",
                chequeo="Si un gas a temperatura fija pasa a la mitad del volumen, ¿qué le pasa a su presión? (se duplica)",
                svg=jeringas),
            "Pide la evidencia antes de creer": dict(
                corto="lo que se vio y el testigo no mostró",
                d="Una conclusión necesita evidencia: algo que se observó o se midió y que no pasó en el "
                  "testigo. Las pistas de un cambio químico son un gas que no estaba, un color nuevo, calor o "
                  "un sólido que aparece.",
                f="afirmación ← dato observado ← comparación con el testigo",
                ej="el vinagre sobre una cáscara de huevo hace burbujas que no salen con agua sola: hay "
                   "evidencia de que reaccionaron.",
                ojo="lo que «suena lógico» no es evidencia. Y una sola pista, como un cambio de color, puede "
                    "venir de un cambio físico.",
                chequeo="Mezclas dos líquidos y el vaso se calienta solo. ¿Qué pista es esa? (calor: pista de un cambio químico)",
                svg=pistas),
        },
        vocab=[("Variable independiente", "la que yo cambio"),
               ("Variable dependiente", "la que mido"),
               ("Testigo", "el que no recibe el cambio"),
               ("Mezcla homogénea", "se ve una sola fase"),
               ("Mezcla heterogénea", "se ven dos o más fases"),
               ("Fase", "cada parte que se ve distinta"),
               ("Presión", "qué tan fuerte empuja el gas"),
               ("Cambio físico", "la sustancia sigue siendo la misma"),
               ("Cambio químico", "aparece una sustancia nueva")]),
    4: dict(
        titulo="Cada propiedad separa algo",
        centro=("Propiedad física", "lo que se mide de una sustancia sin convertirla en otra", propiedades),
        centro_ej="la densidad, el punto de ebullición, el tamaño de los granos, el magnetismo y la "
                  "conductividad son propiedades físicas; arder es una propiedad química.",
        centro_ojo="cada propiedad tiene su nombre y su unidad: no es lo mismo «pesa más» que «es más denso».",
        centro_chequeo="¿Medir el punto de ebullición del agua la convierte en otra sustancia? (no: es una propiedad física)",
        ideas={
            "Compara en igualdad de condiciones": dict(
                corto="misma cantidad, temperatura y tiempo",
                d="Dos resultados se comparan solo si todo lo demás fue igual: misma cantidad, misma "
                  "temperatura, mismo tiempo, mismo recipiente. Si una condición cambió, la diferencia puede "
                  "venir de ella.",
                f="misma cantidad · misma temperatura · mismo tiempo",
                ej="comparar qué jabón quita mejor una mancha solo vale si las telas, las manchas, el agua y el "
                   "tiempo de lavado son iguales.",
                ojo="una carrera dispareja da un ganador falso: antes de concluir, revisa fila por fila qué "
                    "condiciones cambiaron.",
                chequeo="Una pintura se secó al sol y otra a la sombra. ¿Puedes decir cuál seca más rápido? (no: cambió la condición)",
                svg=igualdad),
            "¿Se hunde, flota o queda suspendido?": dict(
                corto="densidad y tamaño de la partícula",
                d="En un líquido, una partícula más densa que él se hunde y una menos densa flota. Cuanto más "
                  "grande y densa, más rápido baja; las muy finas pueden quedar suspendidas mucho tiempo.",
                f="más densa y más grande → baja más rápido",
                ej="en agua con tierra, las piedritas caen primero, la arena después y el barro fino tarda "
                   "horas: el agua sigue turbia mucho rato.",
                ojo="suspendido no es disuelto: una suspensión se ve turbia y con el tiempo se asienta; una "
                    "disolución queda transparente.",
                chequeo="Una bolita de 0,8 g/cm³ en agua (1 g/cm³), ¿se hunde o flota? (flota)",
                svg=sedimenta),
            "Ponle nombre a la propiedad": dict(
                corto="el nombre exacto y su unidad",
                d="Cada propiedad tiene un nombre exacto: densidad (masa por volumen), solubilidad (cuánto se "
                  "disuelve), conductividad (si deja pasar la corriente o el calor), punto de ebullición, "
                  "magnetismo. Nombrarla bien es media respuesta.",
                f="densidad g/cm³ · solubilidad g/100 g · ebullición °C",
                ej="el cobre de los cables se usa por su conductividad eléctrica; el icopor de una nevera de "
                   "paseo, porque casi no conduce el calor.",
                ojo="conducir el calor y conducir la electricidad son dos propiedades distintas; y «pesado» no "
                    "es «denso».",
                chequeo="¿Qué propiedad hace que el aceite quede encima del vinagre? (su menor densidad)",
                svg=etiquetas),
            "Una propiedad, un método de separación": dict(
                corto="cada método usa una diferencia",
                d="Cada método aprovecha una propiedad: el imán, el magnetismo; el tamiz y el filtro, el "
                  "tamaño; la decantación, la densidad; la destilación, el punto de ebullición; la evaporación, "
                  "que el sólido no se evapora.",
                f="propiedad en que difieren → método que la usa",
                ej="para separar agua y alcohol se destila: el alcohol hierve a 78 °C y el agua a 100 °C, así "
                   "que el alcohol sale primero.",
                ojo="si los componentes no difieren en una propiedad, el método que la usa no los separa: un "
                    "tamiz no sirve si todos los granos miden lo mismo.",
                chequeo="¿Qué método separa el agua de la sal disuelta en ella? (la evaporación o la destilación)",
                svg=destilacion),
        },
        vocab=[("Densidad", "masa ÷ volumen"),
               ("Sedimentación", "las partículas se van al fondo"),
               ("Suspensión", "partículas que flotan y enturbian"),
               ("Disolución", "mezcla transparente de una fase"),
               ("Conductividad", "deja pasar la corriente o el calor"),
               ("Punto de ebullición", "temperatura a la que hierve"),
               ("Tamizado", "separar por tamaño con una malla"),
               ("Decantación", "dejar asentar y sacar lo de arriba"),
               ("Destilación", "separar por punto de ebullición")]),
    5: dict(
        titulo="El carbono cambia de casa",
        centro=("Química del carbono",
                "el carbono arma cadenas; lo que se le pega decide cómo se comporta", ciclo_carbono),
        centro_ej="el metano (CH₄) del gas de la estufa y el azúcar de la panela son compuestos de carbono: "
                  "los dos arden y dan CO₂ y agua.",
        centro_ojo="los átomos de carbono no aparecen ni desaparecen: pasan del combustible al CO₂ del aire.",
        centro_chequeo="¿Qué dos sustancias salen de quemar por completo un compuesto de C, H y O? (CO₂ y agua)",
        ideas={
            "Del grupo funcional a la propiedad": dict(
                corto="el grupo decide cómo se comporta",
                d="El grupo funcional es la parte de la molécula que decide cómo se comporta: –OH alcohol, "
                  "–COOH ácido, –COO– éster, –NH₂ amina. Un grupo polar se lleva bien con el agua; una cadena "
                  "larga de C e H, no.",
                f="grupo polar → se mezcla con agua   ·   cadena C–H → no",
                ej="el metanol (CH₃OH) se mezcla con el agua en cualquier proporción; el hexano (C₆H₁₄), "
                   "que es pura cadena, queda flotando encima.",
                ojo="dos moléculas del mismo tamaño se comportan muy distinto si cambia el grupo: mira el "
                    "grupo, no solo cuántos carbonos tiene.",
                chequeo="¿Qué grupo funcional tiene el ácido acético del vinagre? (–COOH: ácido carboxílico)",
                svg=grupo_funcional),
            "Los átomos no se pierden: se cuentan": dict(
                corto="los mismos átomos a cada lado",
                d="En una reacción los átomos no se crean ni se destruyen: se reacomodan. Se cuenta cada "
                  "elemento a cada lado de la flecha (coeficiente por subíndice); si cuadran, la ecuación está "
                  "balanceada y la masa se conserva.",
                f="CH₄ + 2 O₂ → CO₂ + 2 H₂O   (C 1 = 1 · H 4 = 4 · O 4 = 4)",
                ej="con el propano: C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O. Carbonos 3 = 3, hidrógenos 8 = 8 y "
                   "oxígenos 10 = 6 + 4.",
                ojo="el número de adelante multiplica a toda la molécula: 2 H₂O son 4 H y 2 O.",
                chequeo="En 2 H₂ + O₂ → 2 H₂O, ¿cuántos átomos de H hay a cada lado? (4 y 4)",
                svg=conteo),
            "Lo que la tabla sí deja afirmar": dict(
                corto="ni más ni menos de lo que mide",
                d="Una tabla solo deja afirmar lo que mide, en las condiciones y el tiempo en que se midió. "
                  "Bajar no es desaparecer, y lo que no se midió no se puede afirmar.",
                f="afirmación válida = lo que la tabla mide, ni más ni menos",
                ej="si un filtro baja el cloro del agua de 4 a 1 mg/L, se puede decir que lo reduce un 75 %; "
                   "no que «elimina el cloro».",
                ojo="«totalmente», «siempre» y «elimina» casi nunca los sostiene una tabla.",
                chequeo="Una tabla mide un jabón a 20 °C. ¿Sirve para afirmar cómo funciona a 60 °C? (no: eso no se midió)",
                svg=tablilla),
            "Qué sale del tubo de escape": dict(
                corto="combustión completa o incompleta",
                d="Con oxígeno suficiente, un combustible de carbono se quema completo y da CO₂ y agua. Si el "
                  "oxígeno no alcanza, la combustión queda incompleta: salen CO, hollín y otros compuestos a "
                  "medio quemar.",
                f="completa: CO₂ + H₂O   ·   incompleta: CO y hollín (C)",
                ej="una estufa de gas con llama azul quema completo; si la llama sale amarilla y tizna las "
                   "ollas, le falta aire y suelta hollín y CO.",
                ojo="CO no es CO₂: el monóxido sale cuando falta oxígeno y es venenoso aun en poca cantidad.",
                chequeo="Si un motor recibe menos aire del que necesita, ¿qué gas tóxico aumenta? (el monóxido de carbono, CO)",
                svg=llamas),
        },
        vocab=[("Hidrocarburo", "compuesto solo de carbono e hidrógeno"),
               ("Grupo funcional", "la parte que decide cómo se comporta"),
               ("Alcohol", "lleva el grupo –OH"),
               ("Éster", "lleva el grupo –COO–"),
               ("Polar", "con cargas parciales: se lleva con el agua"),
               ("Ecuación balanceada", "los mismos átomos a cada lado"),
               ("Combustión", "reacción con oxígeno que da calor"),
               ("Monóxido de carbono", "CO: gas venenoso, falta de oxígeno"),
               ("Biocombustible", "combustible hecho de plantas o grasas")]),
    6: dict(
        titulo="Una reacción es una receta con energía",
        centro=("Reacción química",
                "los reactivos se reacomodan en productos nuevos, en proporciones fijas, con energía que entra "
                "o sale", reaccion),
        centro_ej="al hornear un pan, el bicarbonato suelta CO₂ con el calor: la masa crece y lo que salió ya "
                  "no vuelve a ser polvo.",
        centro_ojo="una reacción no crea materia: reacomoda átomos, siempre en la misma proporción.",
        centro_chequeo="¿Qué dice una ecuación balanceada? (cuántos moles de cada sustancia reaccionan y se forman)",
        ideas={
            "La ecuación es una receta": dict(
                corto="los coeficientes son moles",
                d="Los coeficientes de una ecuación balanceada dicen cuántos moles reaccionan y se forman, como "
                  "una receta. Para trabajar en gramos: gramos a moles (÷ masa molar), la receta, y moles a "
                  "gramos (× masa molar).",
                f="gramos → moles → (receta) → moles → gramos",
                ej="2 H₂ + O₂ → 2 H₂O: 4 g de H₂ son 2 mol, dan 2 mol de agua, que son 2 · 18 = 36 g.",
                ojo="la receta se lee en moles, no en gramos: 2 H₂ + O₂ no quiere decir 2 g con 1 g.",
                chequeo="En C + O₂ → CO₂, ¿cuántos gramos de CO₂ salen de 12 g de carbono? (44 g)",
                svg=receta),
            "¿El calor sale o entra?": dict(
                corto="exotérmica o endotérmica",
                d="Si la reacción suelta calor es exotérmica: el termómetro sube y ΔH es negativo. Si lo "
                  "absorbe es endotérmica: el termómetro baja y ΔH es positivo. Toda combustión es exotérmica.",
                f="sale calor: ΔH negativo   ·   entra calor: ΔH positivo",
                ej="las compresas frías de los botiquines traen nitrato de amonio: al disolverse en agua "
                   "absorbe calor y la bolsa se enfría.",
                ojo="el signo se mira desde la reacción: si el vaso se calienta es porque la reacción PERDIÓ "
                    "calor, por eso ΔH es negativo.",
                chequeo="Al mezclar dos sustancias el vaso se enfría. ¿Exotérmica o endotérmica? (endotérmica)",
                svg=calor_sale_entra),
            "Una conclusión vale lo que valen sus datos": dict(
                corto="cuántos datos, de qué y en qué condiciones",
                d="Una conclusión es tan fuerte como los datos que la sostienen: cuántas mediciones, de qué y "
                  "en qué condiciones. Si solo se midió una propiedad, la conclusión no puede hablar de otras.",
                f="conclusión = lo medido + sus condiciones, sin agregar",
                ej="si un detergente limpió mejor en tres pruebas a 30 °C, se concluye eso; decir que «es el "
                   "mejor» exige compararlo también en precio y a otras temperaturas.",
                ojo="una sola medición o un solo criterio no alcanzan para «el mejor» ni para «siempre».",
                chequeo="Una pintura se probó solo en paredes de adentro. ¿Se puede concluir que aguanta la lluvia? (no: eso no se midió)",
                svg=pilares),
            "Piezas que se repiten: los polímeros": dict(
                corto="monómero repetido miles de veces",
                d="Un polímero es una molécula enorme hecha de una pieza pequeña (el monómero) que se repite "
                  "miles de veces, como los vagones de un tren. El almidón, la celulosa, las proteínas y los "
                  "plásticos son polímeros.",
                f="monómero + monómero + … → polímero   (–A–A–A–)",
                ej="el polietileno de las bolsas es etileno (C₂H₄) repetido miles de veces; el algodón es "
                   "celulosa: glucosa encadenada.",
                ojo="el monómero y el polímero no tienen las mismas propiedades: el etileno es un gas y el "
                    "polietileno, un sólido.",
                chequeo="¿Qué monómero se repite en el almidón? (la glucosa)",
                svg=polimero),
        },
        vocab=[("Reactivo", "lo que entra a la reacción"),
               ("Producto", "lo que sale de la reacción"),
               ("Coeficiente", "el número de adelante: cuántos moles"),
               ("Masa molar", "lo que pesa un mol (g/mol)"),
               ("Reactivo limitante", "el que se acaba primero y la frena"),
               ("Exotérmica", "suelta calor: ΔH negativo"),
               ("Endotérmica", "absorbe calor: ΔH positivo"),
               ("Monómero", "la pieza pequeña que se repite"),
               ("Polímero", "cadena enorme de monómeros")]),
}
