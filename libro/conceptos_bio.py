"""Conceptualización de Biología (ver conceptos.py y conceptos_area.py): las seis misiones.

Al inicio de cada clase de contenido (3 de los 15 minutos de la Activación) el profe proyecta el
vocabulario de la misión y el «mapa de la misión»: una idea central y una tarjeta por estrategia, que se
abre como infografía (dibujo, definición corta, esquema, ejemplo propio, el «ojo» y la pregunta de
«comprueba», que va al planeador). Modelo aprobado: conceptos_mate.py.

Fuentes: plan_bio.py (MISIONES: estrategias, «instala» y «ojo»; TALLER, el banco ICFES, SABERES y
«Si Biología no es tu fuerte»), clase_viva_bio.py y TEXTOS_BIO.md. Los nombres de las estrategias son
los de plan_bio.MISIONES[mis]["estr"].

Los ejemplos son PROPIOS: no repiten los casos, datos ni opciones de las 10 preguntas del taller ni de
las 4 de entrenamiento de cada misión (nada de lisosomas rotos, insulina, gemelos, hormona antidiurética,
ranas, jaguares, fertilizantes del tomate, prótesis de hipocampo, maíz CRISPR, perros Pomsky, frailejones
ni pez león), para que la conceptualización no resuelva el taller por adelantado.

Datos que conviene que revise el profe de área: la frecuencia del colibrí (hasta unas 1.200 pulsaciones
por minuto) y del elefante (unas 30), y el ejemplo de los pinzones de Darwin tras la sequía de 1977.
"""
import math
import random

from conceptos_figs import *                                         # noqa: F401,F403 (colores)
from conceptos_figs import _svg, _t, _caja, _flecha, _tarjeta, _bien, _mal, _claro


# ═══════════════════════ piezas pequeñas ═══════════════════════
def _puntos(r, n, x0, x1, y0, y1, rad, fill, sep=18):
    """n puntos al azar (semilla fija) sin montarse unos sobre otros."""
    pts, s, k = [], "", 0
    while len(pts) < n and k < 4000:
        k += 1
        x, y = r.uniform(x0, x1), r.uniform(y0, y1)
        if all((x - a) ** 2 + (y - b) ** 2 > sep ** 2 for a, b in pts):
            pts.append((x, y))
            s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rad}" fill="{fill}"/>'
    return s


def _maceta(cx, top, alto_tallo, c):
    """Maceta con una planta de tallo alto_tallo; devuelve (svg, y de la punta)."""
    s = (f'<polygon points="{cx-42},{top} {cx+42},{top} {cx+32},{top+52} {cx-32},{top+52}" '
         f'fill="#F3E3C6" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="{cx-47}" y="{top-10}" width="94" height="14" rx="3" fill="#FBF3E4" stroke="{TINTA}" stroke-width="2.5"/>')
    yt = top - 10 - alto_tallo
    s += f'<line x1="{cx}" y1="{top-10}" x2="{cx}" y2="{yt}" stroke="#30843C" stroke-width="5" stroke-linecap="round"/>'
    for k in range(int(alto_tallo // 34)):
        y = top - 34 - k * 34
        lado = -1 if k % 2 else 1
        s += (f'<ellipse cx="{cx + lado*20}" cy="{y}" rx="20" ry="9" fill="#EAF4EC" stroke="#30843C" '
              f'stroke-width="2.5" transform="rotate({-25*lado} {cx + lado*20} {y})"/>')
    return s, yt


# ═══════════════════════ Misión 1 · la célula ═══════════════════════
def celula(c):
    """Centro M1: célula animal con sus partes nombradas."""
    s = (f'<ellipse cx="170" cy="145" rx="135" ry="102" fill="{_claro(c, .9)}" stroke="{TINTA}" stroke-width="3"/>'
         f'<circle cx="140" cy="140" r="44" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<circle cx="152" cy="130" r="11" fill="{_claro(c, .45)}"/>'
         + _t(140, 172, "núcleo", 18, TINTA, "middle")
         + f'<ellipse cx="240" cy="95" rx="34" ry="17" fill="#FBEFEF" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M214 95 q6 -10 12 0 t12 0 t12 0 t12 0" fill="none" stroke="#A82424" stroke-width="2.5"/>')
    for k in range(3):
        s += f'<path d="M{222+k*4} {178+k*12} q24 -14 48 0" fill="none" stroke="#C9821B" stroke-width="4"/>'
    for x, y in [(90, 90), (205, 205), (110, 205), (215, 140), (80, 175)]:
        s += f'<circle cx="{x}" cy="{y}" r="4" fill="{TINTA}"/>'
    s += (f'<line x1="276" y1="95" x2="318" y2="95" stroke="{TINTA}" stroke-width="1.8"/>'
          + _t(322, 101, "mitocondria", 18)
          + f'<line x1="276" y1="195" x2="318" y2="195" stroke="{TINTA}" stroke-width="1.8"/>'
          + _t(322, 201, "Golgi", 18)
          + f'<line x1="302" y1="150" x2="318" y2="150" stroke="{TINTA}" stroke-width="1.8"/>'
          + _t(322, 156, "membrana", 18)
          + _t(170, 274, "citoplasma: donde flota todo", 18, GRIS, "middle", "600"))
    return _svg(s, "Célula con núcleo, mitocondria, aparato de Golgi y membrana")


def organelos(c):
    """E1 M1: cuatro organelos, cuatro oficios."""
    def ico(k, x, y):
        if k == 0:
            return (f'<circle cx="{x}" cy="{y}" r="24" fill="{_claro(c, .75)}" stroke="{TINTA}" stroke-width="2.5"/>'
                    f'<circle cx="{x+5}" cy="{y-4}" r="7" fill="{_claro(c, .45)}"/>')
        if k == 1:
            return (f'<ellipse cx="{x}" cy="{y}" rx="34" ry="17" fill="#FBEFEF" stroke="{TINTA}" stroke-width="2.5"/>'
                    f'<path d="M{x-26} {y} q6 -10 12 0 t12 0 t12 0 t12 0" fill="none" stroke="#A82424" stroke-width="2.5"/>')
        if k == 2:
            return (f'<circle cx="{x}" cy="{y+7}" r="15" fill="#FDF5E7" stroke="{TINTA}" stroke-width="2.5"/>'
                    f'<circle cx="{x}" cy="{y-14}" r="10" fill="#FDF5E7" stroke="{TINTA}" stroke-width="2.5"/>')
        return (f'<circle cx="{x}" cy="{y}" r="24" fill="#F3EEF8" stroke="{TINTA}" stroke-width="2.5"/>'
                + "".join(f'<circle cx="{x+dx}" cy="{y+dy}" r="3.5" fill="{TINTA}"/>'
                          for dx, dy in [(-9, -6), (6, -10), (9, 5), (-4, 9), (0, -1)]))
    s = ""
    datos = [("núcleo", "guarda el ADN"), ("mitocondria", "da la energía"),
             ("ribosoma", "arma proteínas"), ("lisosoma", "digiere desechos")]
    for k, (n, o) in enumerate(datos):
        x, y = 25 + (k % 2) * 190, 18 + (k // 2) * 132
        s += (f'<rect x="{x}" y="{y}" width="180" height="122" rx="14" fill="#fff" stroke="{c}" stroke-width="2.5"/>'
              + ico(k, x + 90, y + 36) + _t(x + 90, y + 86, n, 20, TINTA, "middle")
              + _t(x + 90, y + 109, o, 18, GRIS, "middle", "600"))
    return _svg(s, "Cuatro organelos con su oficio: núcleo, mitocondria, ribosoma y lisosoma")


def ruta_proteina(c):
    """E2 M1: las estaciones de la proteína que sale de la célula."""
    s = (f'<circle cx="50" cy="128" r="30" fill="{_claro(c, .75)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M108 104 q10 -12 20 0 t20 0 M108 128 q10 -12 20 0 t20 0 M108 152 q10 -12 20 0 t20 0" '
         f'fill="none" stroke="{TINTA}" stroke-width="3"/>')
    for y in (98, 122, 146):
        for x in (112, 132, 152):
            s += f'<circle cx="{x}" cy="{y}" r="3" fill="{TINTA}"/>'
    for k in range(3):
        s += f'<path d="M{196+k*3} {112+k*14} q22 -12 44 0" fill="none" stroke="#C9821B" stroke-width="5" stroke-linecap="round"/>'
    s += (f'<circle cx="294" cy="128" r="15" fill="#FDF5E7" stroke="{TINTA}" stroke-width="2.5"/>'
          f'<circle cx="294" cy="128" r="5" fill="{c}"/>'
          f'<path d="M362 60 L362 112 M362 144 L362 196" stroke="{TINTA}" stroke-width="5"/>'
          f'<circle cx="392" cy="128" r="5" fill="{c}"/>')
    for x1, x2 in [(84, 104), (164, 192), (250, 274), (314, 352)]:
        s += _flecha(x1, 128, x2, 128, c, 3.5)
    for x, n in [(50, "núcleo"), (132, "retículo"), (218, "Golgi"), (294, "vesícula"), (386, "sale")]:
        s += _t(x, 222, n, 18, TINTA, "middle")
    s += _t(210, 270, "una estación detrás de otra", 20, c, "middle")
    return _svg(s, "Ruta de la proteína: núcleo, retículo, Golgi, vesícula y salida de la célula")


def grupo_control(c):
    """E3 M1: tratado contra control; el efecto es la diferencia."""
    s1, y1 = _maceta(120, 200, 70, c)
    s2, y2 = _maceta(280, 200, 130, c)
    s = (s1 + s2
         + f'<line x1="80" y1="{y1}" x2="326" y2="{y1}" stroke="{GRIS}" stroke-width="2.5" stroke-dasharray="8 6"/>'
         f'<path d="M332 {y2} L342 {y2} L342 {y1} L332 {y1}" fill="none" stroke="{c}" stroke-width="4"/>'
         + _t(350, (y1 + y2) / 2 + 7, "efecto", 20, c)
         + _t(120, 276, "control", 20, TINTA, "middle") + _t(280, 276, "tratado", 20, TINTA, "middle"))
    return _svg(s, "Dos plantas: la tratada crece más que la de control; el efecto es la diferencia")


def membrana(c):
    """E4 M1: difusión (gratis) y transporte activo (cuesta energía)."""
    r = random.Random(3)
    s = (_puntos(r, 16, 40, 180, 95, 205, 6, c)
         + _puntos(r, 4, 240, 380, 95, 205, 6, c, 40)
         + f'<rect x="198" y="80" width="24" height="140" fill="{_claro(c, .85)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="196" y="212" width="28" height="34" rx="8" fill="#FDF5E7" stroke="{TINTA}" stroke-width="2.5"/>'
         + _flecha(90, 64, 330, 64, "#30843C", 4)
         + _t(210, 40, "de donde hay más a donde hay menos: sola", 18, "#30843C", "middle")
         + _flecha(330, 232, 90, 232, "#A82424", 4)
         + _t(210, 276, "hacia donde ya hay más: cuesta energía", 18, "#A82424", "middle"))
    return _svg(s, "Membrana con muchas partículas a un lado y pocas al otro: difusión y transporte activo")


# ═══════════════════════ Misión 2 · el cuerpo se regula ═══════════════════════
def rango(c):
    """Centro M2: una variable que se sale del rango y vuelve."""
    s = (f'<rect x="40" y="110" width="350" height="60" fill="{_claro(c, .88)}"/>'
         f'<line x1="40" y1="140" x2="390" y2="140" stroke="{GRIS}" stroke-width="2" stroke-dasharray="7 6"/>'
         f'<path d="M40 140 C80 140 90 128 120 132 C150 136 160 60 190 62 C220 64 225 150 255 148 '
         f'C285 146 300 132 330 138 C360 144 370 140 390 140" fill="none" stroke="{c}" stroke-width="6" stroke-linecap="round"/>'
         + _t(48, 200, "rango normal", 20, TINTA)
         + _t(190, 46, "se desvía", 20, "#A82424", "middle")
         + _flecha(222, 80, 246, 128, "#30843C", 4)
         + _t(256, 104, "se corrige", 20, "#30843C")
         + _t(215, 262, "el cuerpo no evita el cambio: lo corrige", 18, TINTA, "middle", "600"))
    return _svg(s, "Una variable sale del rango normal y el cuerpo la devuelve")


def circuito(c):
    """E1 M2: desvío, sensor, centro y efector, en círculo."""
    cajas = [(150, 14, "desvío"), (288, 118, "sensor"), (150, 222, "centro"), (12, 118, "efector")]
    s = ""
    for x, y, n in cajas:
        s += _tarjeta(x, y, 120, 46, n, c, 20)
    s += (_flecha(272, 38, 330, 108, c) + _flecha(330, 172, 278, 236, c)
          + _flecha(144, 244, 86, 172, c) + _flecha(86, 110, 142, 44, c)
          + _t(210, 140, "vuelve al", 20, TINTA, "middle") + _t(210, 164, "equilibrio", 20, TINTA, "middle"))
    return _svg(s, "Circuito de regulación: desvío, sensor, centro de control y efector")


def texto_funcion(c):
    """E2 M2: la función se subraya en el texto."""
    s = (f'<rect x="36" y="30" width="200" height="232" rx="10" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="54" y="120" width="164" height="22" fill="{_claro(c, .65)}"/>')
    for k in range(8):
        y = 60 + k * 26
        w = 150 if k % 3 == 2 else 164
        s += f'<line x1="56" y1="{y}" x2="{56+w}" y2="{y}" stroke="#C9D1DC" stroke-width="5" stroke-linecap="round"/>'
    s += (f'<line x1="56" y1="131" x2="210" y2="131" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
          + _flecha(240, 131, 286, 131, c)
          + _tarjeta(292, 106, 112, 50, "función", c, 20)
          + _t(348, 190, "lo dice", 18, TINTA, "middle", "600")
          + _t(348, 212, "el texto", 18, TINTA, "middle", "600"))
    return _svg(s, "Un texto con una frase subrayada que dice la función")


def especies(c):
    """E3 M2: la misma columna, la misma unidad: ¿quién se sale?"""
    s = _t(210, 34, "misma variable, misma unidad", 20, TINTA, "middle")
    for k, (h, on) in enumerate([(150, False), (138, False), (52, True)]):
        x = 70 + k * 105
        s += _caja(x, 236 - h, 60, h, 16, _claro(c, .7) if on else "#EEF2F8",
                   _claro(c, .5) if on else "#D3DCEA", "#fff")
        s += _t(x + 30, 266, f"especie {'ABC'[k]}", 18, TINTA, "middle")
    s += _t(310, 164, "¿por qué?", 20, c, "middle")
    return _svg(s, "Tres especies en barras: una se sale del patrón")


def explicaciones(c):
    """E4 M2: se queda la explicación que da cuenta de todos los datos."""
    s = ""
    for k, (tit, marcas) in enumerate([("explicación 1", (1, 1, 1)), ("explicación 2", (1, 0, 0))]):
        x = 25 + k * 195
        s += (f'<rect x="{x}" y="22" width="180" height="210" rx="14" fill="#fff" '
              f'stroke="{c if k == 0 else GRIS}" stroke-width="{3.5 if k == 0 else 2.5}"/>'
              + _t(x + 90, 56, tit, 20, TINTA, "middle"))
        for j, ok in enumerate(marcas):
            y = 96 + j * 46
            s += _t(x + 26, y + 8, f"dato {j+1}", 20, TINTA, w="600")
            s += _bien(x + 124, y - 6) if ok else _mal(x + 128, y - 10)
    s += _t(210, 270, "se queda la que explica todo", 20, c, "middle")
    return _svg(s, "Dos explicaciones: la primera da cuenta de los tres datos y la segunda de uno solo")


# ═══════════════════════ Misión 3 · el ecosistema ═══════════════════════
def terrario(c):
    """Centro M3: seres vivos y ambiente en el mismo frasco."""
    s = (f'<circle cx="52" cy="54" r="24" fill="#C9821B" opacity=".85"/>'
         + _caja(110, 112, 220, 140, 46, "#F5FAF6", "#E2EFE4", "#FAFDFB")
         + f'<rect x="112" y="210" width="216" height="40" fill="#F3E3C6"/>')
    for x, h in [(150, 60), (200, 84), (262, 50)]:
        s += (f'<line x1="{x}" y1="210" x2="{x}" y2="{210-h}" stroke="{VERDE}" stroke-width="4"/>'
              f'<ellipse cx="{x-12}" cy="{210-h*0.6:.0f}" rx="13" ry="6" fill="#EAF4EC" stroke="{VERDE}" stroke-width="2"/>'
              f'<ellipse cx="{x+12}" cy="{210-h*0.8:.0f}" rx="13" ry="6" fill="#EAF4EC" stroke="{VERDE}" stroke-width="2"/>')
    s += (_t(52, 104, "luz", 20, "#C9821B", "middle")
          + _t(220, 236, "suelo y agua", 18, TINTA, "middle")
          + _t(220, 284, "lo vivo y lo no vivo, conectados", 18, TINTA, "middle", "600"))
    return _svg(s, "Un frasco con plantas, un animal pequeño, suelo, agua y luz")


def barras_control(c):
    """E1 M3: barras que suben o bajan respecto al control."""
    s = (f'<line x1="40" y1="150" x2="390" y2="150" stroke="{TINTA}" stroke-width="2.5" stroke-dasharray="9 6"/>'
         + _t(46, 140, "control = 0", 18, GRIS, w="600"))
    for k, (v, n) in enumerate([(50, "A"), (-70, "B"), (24, "C")]):
        x = 160 + k * 80
        y, h = (150 - v, v) if v > 0 else (150, -v)
        s += (f'<rect x="{x}" y="{y}" width="48" height="{h}" fill="{_claro(c, .7) if v > 0 else "#FBEFEF"}" '
              f'stroke="{c if v > 0 else "#A82424"}" stroke-width="2.5"/>')
        s += _t(x + 24, (y - 10) if v > 0 else (y + h + 24), f"{'+' if v > 0 else '−'}{abs(v)}", 18, TINTA, "middle")
        s += _t(x + 24, 270, f"grupo {n}", 18, TINTA, "middle", "600")
    return _svg(s, "Barras de tres grupos que suben o bajan respecto a la línea del control")


def red_trofica(c):
    """E2 M3: quién se come a quién; la flecha va hacia el que come."""
    nodos = {"pasto": (155, 226), "conejo": (40, 142), "grillo": (270, 142), "zorro": (40, 52), "ave": (270, 52)}
    s = _t(210, 30, "la flecha va hacia el que come", 18, TINTA, "middle", "600")
    for a, b in [("pasto", "conejo"), ("pasto", "grillo"), ("conejo", "zorro"), ("grillo", "ave"), ("ave", "zorro")]:
        (x1, y1), (x2, y2) = nodos[a], nodos[b]
        p1, p2 = (x1 + 55, y1 + 22), (x2 + 55, y2 + 22)
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        L = math.hypot(dx, dy)
        k1, k2 = (30 if dy else 60) / L, (30 if dy else 60) / L
        s += _flecha(p1[0] + dx * k1, p1[1] + dy * k1, p2[0] - dx * k2, p2[1] - dy * k2, c, 3.5)
    for n, (x, y) in nodos.items():
        s += _tarjeta(x, y, 110, 44, n, c if n == "pasto" else TINTA, 20, _claro(c, .85) if n == "pasto" else "#fff")
    return _svg(s, "Red trófica: el pasto alimenta al conejo y al grillo; el zorro y el ave están arriba")


def limitante(c):
    """E3 M3: tres recursos; el que más falta manda."""
    s = ""
    for k, (n, nivel) in enumerate([("luz", .85), ("agua", .8), ("nitrógeno", .22)]):
        x = 75 + k * 110
        alto = 170 * nivel
        on = nivel < .5
        s += (f'<rect x="{x}" y="50" width="60" height="170" rx="14" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<rect x="{x+5}" y="{215-alto:.0f}" width="50" height="{alto:.0f}" rx="10" '
              f'fill="{_claro(c, .45) if on else "#EEF2F8"}"/>'
              + _t(x + 30, 252, n, 18, c if on else TINTA, "middle"))
    s += _t(325, 36, "el que manda", 20, c, "middle")
    return _svg(s, "Tres recursos: luz y agua de sobra, nitrógeno escaso; el escaso es el que manda")


def decision(c):
    """E4 M3: de lo que se sabe a la decisión y a la medición."""
    s = ""
    for k, (n, h) in enumerate([("lo que sé", 60), ("decido", 100), ("lo mido", 140)]):
        x = 40 + k * 120
        s += _caja(x, 250 - h, 92, h, 22, "#fff" if k < 2 else _claro(c, .8), "#D3DCEA", "#EEF2F8")
        s += _t(x + 46, 250 - h + 34, n, 20, TINTA if k < 2 else c, "middle")
    s += _flecha(110, 160, 156, 118, c, 3.5) + _flecha(232, 116, 278, 78, c, 3.5)
    return _svg(s, "Tres escalones: lo que sé del ecosistema, la decisión y cómo la mido")


# ═══════════════════════ Misión 4 · ciencia, tecnología y sociedad ═══════════════════════
def matraz_preguntas(c):
    """Centro M4: un invento, tres preguntas."""
    s = (f'<path d="M190 60 L190 120 L130 230 Q124 246 142 246 L278 246 Q296 246 290 230 L230 120 L230 60 Z" '
         f'fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
         f'<path d="M150 200 L270 200 L290 236 Q292 244 280 244 L140 244 Q128 244 132 236 Z" fill="{_claro(c, .7)}"/>'
         f'<rect x="182" y="50" width="56" height="14" rx="4" fill="#EEF2F8" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(210, 190, "?", 44, c, "middle")
         + _t(20, 76, "¿qué promete?", 18, TINTA) + _t(20, 162, "¿cómo funciona?", 18, TINTA)
         + _t(400, 116, "¿qué se probó?", 18, TINTA, "end") + _t(400, 200, "¿en quiénes?", 18, TINTA, "end"))
    return _svg(s, "Un matraz con un signo de pregunta y cuatro preguntas alrededor")


def a_prueba(c):
    """E1 M4: con y sin el cambio, y algo que se mide."""
    s = ""
    for k, (n, nivel) in enumerate([("con X", 120), ("sin X", 70)]):
        x = 80 + k * 120
        s += (f'<path d="M{x} 50 L{x} 210 Q{x} 240 {x+30} 240 Q{x+60} 240 {x+60} 210 L{x+60} 50" '
              f'fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
              f'<path d="M{x+3} {240-nivel} L{x+57} {240-nivel} L{x+57} 210 Q{x+57} 237 {x+30} 237 Q{x+3} 237 {x+3} 210 Z" '
              f'fill="{_claro(c, .6) if k == 0 else "#EEF2F8"}"/>'
              + _t(x + 30, 272, n, 20, TINTA, "middle"))
    s += f'<rect x="330" y="50" width="34" height="190" rx="4" fill="#FDF5E7" stroke="{TINTA}" stroke-width="2.5"/>'
    for k in range(10):
        y = 60 + k * 18
        s += f'<line x1="330" y1="{y}" x2="{346 if k % 2 else 352}" y2="{y}" stroke="{TINTA}" stroke-width="2"/>'
    s += _t(347, 36, "mido", 18, c, "middle")
    return _svg(s, "Dos tubos, con y sin el cambio, y una regla para medir")


def cadena(c):
    """E2 M4: el mecanismo como cadena de eslabones."""
    s = ""
    nombres = ["causa", "paso", "paso", "efecto"]
    for k in range(4):
        x = 70 + k * 92
        s += (f'<ellipse cx="{x}" cy="130" rx="54" ry="30" fill="none" stroke="{c if k % 2 == 0 else TINTA}" '
              f'stroke-width="9"/>')
        s += _t(x, 200, nombres[k], 20, TINTA, "middle")
    s += _t(210, 262, "cada eslabón causa el siguiente", 20, c, "middle")
    return _svg(s, "Cuatro eslabones encadenados: causa, paso, paso y efecto")


def capas(c):
    """E3 M4: cada pieza del invento, su función (un tapabocas por capas)."""
    s = ""
    for k, (n, fill) in enumerate([("repele gotas", "#EEF2F8"), ("filtra", _claro(c, .65)), ("absorbe", "#FDF5E7")]):
        y = 80 + k * 72
        s += (f'<polygon points="40,{y} 220,{y} 270,{y-34} 90,{y-34}" fill="{fill}" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<line x1="262" y1="{y-16}" x2="296" y2="{y-16}" stroke="{TINTA}" stroke-width="1.8"/>'
              + _t(302, y - 9, n, 20, TINTA))
    s += _t(210, 266, "¿y si quito esta pieza?", 20, c, "middle")
    return _svg(s, "Tres capas separadas de un tapabocas, cada una con su función")


def alcance(c):
    """E4 M4: probado en unos, usado en otros."""
    s = ""
    for k, (tit, quien) in enumerate([("probado en", "adultos"), ("usado en", "niños")]):
        x = 30 + k * 200
        s += (f'<rect x="{x}" y="40" width="160" height="180" rx="14" fill="{"#fff" if k else _claro(c, .85)}" '
              f'stroke="{c if k == 0 else GRIS}" stroke-width="3"/>'
              + _t(x + 80, 74, tit, 20, TINTA, "middle") + _t(x + 80, 206, quien, 20, TINTA, "middle", "600"))
        for j in range(3):
            px = x + 40 + j * 40
            r = 14 if k == 0 else 10
            s += (f'<circle cx="{px}" cy="{120 if k == 0 else 126}" r="{r - 4}" fill="{TINTA}" opacity=".75"/>'
                  f'<path d="M{px-r} {170} Q{px} {130 if k == 0 else 140} {px+r} 170 Z" fill="{TINTA}" opacity=".75"/>')
    s += _bien(96, 252) + _t(310, 272, "?", 34, "#A82424", "middle") + _flecha(196, 130, 224, 130, GRIS, 3.5)
    return _svg(s, "Lo probado en adultos no está probado en niños")


# ═══════════════════════ Misión 5 · herencia ═══════════════════════
def adn(c):
    """Centro M5: la doble hélice con un gen marcado."""
    s = ""
    a = " ".join(f"{40+k*4},{140+45*math.sin(k*4/34):.1f}" for k in range(86))
    b = " ".join(f"{40+k*4},{140-45*math.sin(k*4/34):.1f}" for k in range(86))
    for k in range(4, 86, 6):
        x = 40 + k * 4
        y1, y2 = 140 + 45 * math.sin(k * 4 / 34), 140 - 45 * math.sin(k * 4 / 34)
        on = 150 <= x <= 262
        s += f'<line x1="{x}" y1="{y1:.0f}" x2="{x}" y2="{y2:.0f}" stroke="{c if on else "#C9D1DC"}" stroke-width="{4 if on else 3}"/>'
    s += (f'<polyline points="{a}" fill="none" stroke="{TINTA}" stroke-width="4"/>'
          f'<polyline points="{b}" fill="none" stroke="{TINTA}" stroke-width="4"/>'
          f'<path d="M150 72 L150 62 L262 62 L262 72" fill="none" stroke="{c}" stroke-width="3.5"/>'
          + _t(206, 50, "un gen", 20, c, "middle")
          + _t(210, 240, "alelos: versiones del mismo gen", 20, TINTA, "middle"))
    return _svg(s, "Doble hélice de ADN con un tramo marcado como un gen")


def punnett(c):
    """E1 M5: cuadro de Punnett Aa × Aa."""
    s = ""
    al = ["A", "a"]
    for i in range(2):
        s += _t(185 + i * 76, 60, al[i], 26, c, "middle") + _t(124, 112 + i * 76, al[i], 26, c, "middle")
        for j in range(2):
            g = "".join(sorted(al[j] + al[i]))
            on = g == "aa"
            s += (f'<rect x="{148 + i*76}" y="{72 + j*76}" width="76" height="76" '
                  f'fill="{_claro(c, .6) if on else "#fff"}" stroke="{TINTA}" stroke-width="2.5"/>'
                  + _t(186 + i * 76, 120 + j * 76, g, 24, TINTA, "middle"))
    s += (_t(224, 30, "papá", 18, GRIS, "middle", "600")
          + _t(70, 152, "mamá", 18, GRIS, "middle", "600")
          + _t(210, 268, "Aa × Aa: 1 de cada 4 es aa", 20, TINTA, "middle"))
    return _svg(s, "Cuadro de Punnett de dos padres Aa: una de cuatro casillas es aa")


def mutacion(c):
    """E2 M5: una letra cambia en el ADN y cambia la proteína."""
    s = _t(20, 66, "ADN", 18, TINTA)
    for k, L in enumerate("ATGCCA"):
        on = k == 3
        s += (f'<rect x="{98 + k*46}" y="38" width="40" height="40" rx="6" fill="{"#FBEFEF" if on else "#fff"}" '
              f'stroke="{"#A82424" if on else TINTA}" stroke-width="{3.5 if on else 2.5}"/>'
              + _t(118 + k * 46, 66, "T" if on else L, 22, "#A82424" if on else TINTA, "middle"))
    s += _flecha(232, 90, 232, 128, c, 3.5) + _t(20, 158, "proteína", 18, TINTA)
    for k in range(6):
        on = k == 3
        s += f'<circle cx="{118 + k*46}" cy="152" r="17" fill="{"#A82424" if on else _claro(c, .6)}" stroke="{TINTA}" stroke-width="2"/>'
        if k:
            s += f'<line x1="{118 + (k-1)*46 + 17}" y1="152" x2="{118 + k*46 - 17}" y2="152" stroke="{TINTA}" stroke-width="3"/>'
    s += (_flecha(232, 178, 232, 214, c, 3.5)
          + _tarjeta(142, 222, 180, 46, "rasgo distinto", c, 20))
    return _svg(s, "Una letra del ADN cambia, la proteína sale distinta y el rasgo cambia")


def diana(c):
    """E3 M5: la prueba que da en la pregunta."""
    s = ""
    for r, f in [(100, "#fff"), (70, _claro(c, .85)), (40, _claro(c, .6))]:
        s += f'<circle cx="250" cy="140" r="{r}" fill="{f}" stroke="{TINTA}" stroke-width="2.5"/>'
    s += (_flecha(60, 72, 244, 136, c, 5)
          + f'<line x1="40" y1="230" x2="160" y2="200" stroke="{GRIS}" stroke-width="4"/>'
          f'<line x1="330" y1="30" x2="370" y2="60" stroke="{GRIS}" stroke-width="4"/>'
          + _t(40, 36, "mide lo que preguntan", 20, c)
          + _t(210, 272, "las otras pruebas responden otra cosa", 18, TINTA, "middle", "600"))
    return _svg(s, "Una diana: una flecha da en el centro y otras se quedan afuera")


def balanza(c):
    """E4 M5: lo que gana contra lo que arriesga."""
    s = (f'<polygon points="210,90 186,244 234,244" fill="#EEF2F8" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="150" y="244" width="120" height="14" rx="4" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="70" y1="90" x2="350" y2="90" stroke="{TINTA}" stroke-width="6" stroke-linecap="round"/>'
         f'<circle cx="210" cy="90" r="8" fill="{c}"/>')
    for x, y, n, col in [(70, 90, "gana", "#30843C"), (350, 90, "arriesga", "#A82424")]:
        s += (f'<line x1="{x}" y1="{y}" x2="{x-34}" y2="{y+60}" stroke="{TINTA}" stroke-width="2"/>'
              f'<line x1="{x}" y1="{y}" x2="{x+34}" y2="{y+60}" stroke="{TINTA}" stroke-width="2"/>'
              f'<path d="M{x-50} {y+60} L{x+50} {y+60} Q{x} {y+96} {x-50} {y+60} Z" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x, y + 128, n, 20, col, "middle"))
    s += _t(210, 40, "«siempre» y «nunca»: exageran", 18, c, "middle")
    return _svg(s, "Una balanza que pesa lo que gana una tecnología contra lo que arriesga")


# ═══════════════════════ Misión 6 · la vida cambia ═══════════════════════
def generaciones(c):
    """Centro M6: un rasgo que se vuelve frecuente generación tras generación."""
    s = ""
    for g, n in enumerate([2, 4, 7]):
        y = 60 + g * 80
        s += _t(30, y + 7, f"gen. {g+1}", 18, TINTA, w="600")
        for k in range(8):
            on = k < n
            s += f'<circle cx="{120 + k*36}" cy="{y}" r="13" fill="{c if on else "#fff"}" stroke="{TINTA}" stroke-width="2"/>'
    s += (_flecha(400, 50, 400, 210, GRIS, 3.5)
          + _t(210, 280, "cambia la población, no el individuo", 18, TINTA, "middle", "600"))
    return _svg(s, "Tres generaciones: el rasgo útil pasa de 2 de 8 a 7 de 8 individuos")


def relojes(c):
    """E1 M6: el reloj de una vida y el de las generaciones."""
    s = ""
    for k, (cx, tit, sub) in enumerate([(110, "una vida", "ambiente"), (310, "generaciones", "herencia")]):
        s += (f'<circle cx="{cx}" cy="120" r="70" fill="{_claro(c, .85) if k else "#fff"}" stroke="{TINTA}" stroke-width="3"/>'
              f'<circle cx="{cx}" cy="120" r="6" fill="{TINTA}"/>')
        for j in range(12):
            a = j * math.pi / 6
            s += (f'<line x1="{cx + 58*math.cos(a):.1f}" y1="{120 + 58*math.sin(a):.1f}" '
                  f'x2="{cx + 66*math.cos(a):.1f}" y2="{120 + 66*math.sin(a):.1f}" stroke="{TINTA}" stroke-width="2.5"/>')
        s += (f'<line x1="{cx}" y1="120" x2="{cx}" y2="72" stroke="{TINTA}" stroke-width="4" stroke-linecap="round"/>'
              f'<line x1="{cx}" y1="120" x2="{cx + (30 if k == 0 else -34)}" y2="{120 + (14 if k == 0 else 22)}" '
              f'stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
              + _t(cx, 226, tit, 20, TINTA, "middle") + _t(cx, 252, sub, 20, c, "middle"))
    return _svg(s, "Dos relojes: el de una vida (ambiente) y el de las generaciones (herencia)")


def suben_juntas(c):
    """E2 M6: dos cosas que suben juntas por una tercera causa."""
    s = (f'<circle cx="210" cy="50" r="24" fill="#C9821B" opacity=".85"/>'
         + _t(250, 58, "sol", 20, "#C9821B")
         + f'<polyline points="40,200 100,180 160,150 220,130" fill="none" stroke="{c}" stroke-width="6" stroke-linecap="round"/>'
         f'<polyline points="230,215 290,199 350,171 400,151" fill="none" stroke="{TINTA}" stroke-width="6" stroke-linecap="round"/>'
         + _t(40, 230, "helados", 20, c) + _t(236, 244, "quemaduras", 20, TINTA)
         + _flecha(196, 72, 156, 136, "#C9821B", 3.5) + _flecha(224, 72, 306, 168, "#C9821B", 3.5)
         + _t(210, 280, "suben juntas, pero una no causa la otra", 18, TINTA, "middle", "600"))
    return _svg(s, "Helados y quemaduras suben juntos porque los dos dependen del sol")


def torre(c):
    """E3 M6: si sale una pieza, se mueven las de arriba."""
    s = (_caja(40, 196, 86, 52, 18, "#EEF2F8") + _caja(130, 196, 86, 52, 18, "#EEF2F8")
         + f'<rect x="238" y="196" width="80" height="52" fill="none" stroke="#A82424" stroke-width="3" stroke-dasharray="7 6"/>'
         + _caja(336, 214, 60, 42, 12, _claro(c, .75)) + _flecha(270, 236, 330, 236, c, 3.5)
         + '<g transform="rotate(7 175 175)">' + _caja(85, 140, 86, 52, 18, "#EEF2F8")
         + _caja(175, 140, 86, 52, 18, "#EEF2F8") + _caja(130, 84, 86, 52, 18, "#EEF2F8") + '</g>'
         + _t(362, 282, "una especie", 18, c, "middle")
         + _t(130, 40, "las de arriba se mueven", 18, TINTA, "middle", "600"))
    return _svg(s, "Torre de bloques: sale uno de abajo y los de arriba se inclinan")


def cactus(c):
    """E4 M6: cada rasgo contra un problema del ambiente."""
    s = (f'<line x1="30" y1="214" x2="300" y2="214" stroke="#C9D1DC" stroke-width="3"/>'
         f'<rect x="70" y="92" width="26" height="74" rx="13" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="3"/>'
         f'<rect x="80" y="140" width="50" height="26" rx="13" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="3"/>'
         f'<rect x="84" y="143" width="20" height="20" fill="{_claro(c, .7)}"/>'
         f'<path d="M80 216 Q60 236 34 238 M110 216 Q100 246 70 254 M190 216 Q214 240 250 244 M165 216 Q180 250 214 258" '
         f'fill="none" stroke="#8A6A3A" stroke-width="3.5" stroke-linecap="round"/>'
         f'<rect x="120" y="50" width="56" height="166" rx="28" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="3"/>')
    for x, y in [(126, 70), (170, 90), (126, 120), (170, 150), (126, 180)]:
        dx = -10 if x < 150 else 10
        s += f'<line x1="{x}" y1="{y}" x2="{x+dx}" y2="{y-6}" stroke="{TINTA}" stroke-width="2.5"/>'
    s += (f'<line x1="182" y1="86" x2="232" y2="70" stroke="{TINTA}" stroke-width="1.8"/>' + _t(236, 76, "espinas", 18)
          + f'<line x1="180" y1="140" x2="232" y2="136" stroke="{TINTA}" stroke-width="1.8"/>' + _t(236, 142, "tallo que guarda agua", 18)
          + f'<line x1="250" y1="242" x2="268" y2="242" stroke="{TINTA}" stroke-width="1.8"/>' + _t(272, 248, "raíces anchas", 18)
          + _t(236, 104, "pierde menos agua", 18, GRIS, w="600")
          + _t(236, 166, "para la sequía", 18, GRIS, w="600"))
    return _svg(s, "Un cactus con sus rasgos nombrados: espinas, tallo que guarda agua y raíces anchas")


# ═══════════════════════ los datos de las seis misiones ═══════════════════════
DATOS = {
    1: dict(
        titulo="La célula es una fábrica en cadena",
        centro=("La célula", "la unidad más pequeña que está viva: cada parte cumple un oficio", celula),
        centro_ej="como una panadería: la receta está en la oficina (el núcleo), los hornos son los ribosomas, "
                  "el Golgi empaca y las vesículas reparten.",
        centro_ojo="estructura y oficio van juntos: si una parte falta o falla, lo que ella hacía deja de hacerse.",
        centro_chequeo="¿Dónde guarda la célula las instrucciones para fabricar sus proteínas? (en el ADN del núcleo)",
        ideas={
            "Cada organelo, su oficio": dict(
                corto="un organelo, un trabajo",
                d="Cada organelo tiene su oficio: el núcleo guarda el ADN, la mitocondria saca energía de la "
                  "glucosa, el ribosoma arma proteínas, el lisosoma digiere lo que sobra y el cloroplasto (solo en "
                  "plantas) hace la fotosíntesis.",
                f="organelo → su oficio → qué deja de pasar si falla",
                ej="las células del músculo del corazón tienen miles de mitocondrias: trabajan sin parar y "
                   "necesitan mucha energía.",
                ojo="no confundas quién arma la proteína (ribosoma) con quién la empaca (Golgi), ni quién da "
                    "energía (mitocondria) con quién digiere (lisosoma).",
                chequeo="Una célula de la hoja tiene un organelo verde que la del músculo no tiene. ¿Cuál es? (el cloroplasto)",
                svg=organelos),
            "La ruta de la proteína, estación a estación": dict(
                corto="del núcleo hacia afuera, en orden",
                d="Una proteína que sale de la célula sigue una ruta fija: el núcleo manda la instrucción (ARN), "
                  "los ribosomas del retículo rugoso la arman, el Golgi la modifica y empaca, y una vesícula la "
                  "lleva hasta la membrana.",
                f="ADN → ARN → ribosoma y retículo → Golgi → vesícula → afuera",
                ej="la amilasa de la saliva se fabrica así en las glándulas salivales: recorre esas estaciones "
                   "y sale a la boca a partir el almidón.",
                ojo="si una estación falla, se detiene todo lo que viene DESPUÉS; lo de antes sigue trabajando "
                    "y se amontona justo antes del daño.",
                chequeo="¿Qué estación viene justo después del retículo rugoso? (el aparato de Golgi)",
                svg=ruta_proteina),
            "Comparar contra el que no cambió": dict(
                corto="el grupo control: igual, pero sin tratar",
                d="Un efecto solo se afirma comparando con un grupo control: igual en todo, pero sin el "
                  "tratamiento. El efecto es la diferencia entre los dos, no el número del grupo tratado.",
                f="efecto = tratado − control",
                ej="ratones que beben agua con una vitamina pesan 30 g; los de control, con agua sola, 26 g: "
                   "la vitamina sumó 4 g, no 30.",
                ojo="si el tratado y el control difieren en dos cosas (otra luz, otra edad), ya no sabes cuál "
                    "de las dos causó el efecto.",
                chequeo="Sin grupo control, ¿se puede saber si el cambio lo produjo el tratamiento? (no)",
                svg=grupo_control),
            "Dónde hay más y hacia dónde va": dict(
                corto="difusión, ósmosis y transporte activo",
                d="Las sustancias pasan solas de donde hay más a donde hay menos (difusión). El agua cruza la "
                  "membrana hacia el lado con más sustancias disueltas (ósmosis). Ir hacia donde ya hay más "
                  "cuesta energía: transporte activo.",
                f="de más a menos: gratis   ·   de menos a más: cuesta energía (ATP)",
                ej="una uva pasa metida en agua se hincha: adentro hay más azúcar disuelta que afuera, así que "
                   "el agua entra.",
                ojo="el agua no va hacia donde hay más agua: va hacia donde hay más sustancias disueltas.",
                chequeo="Si echas sal sobre unas rodajas de pepino, ¿el agua sale de sus células o entra? (sale)",
                svg=membrana),
        },
        vocab=[("Organelo", "una parte de la célula con un oficio"),
               ("Núcleo", "guarda el ADN: las instrucciones"),
               ("Mitocondria", "saca la energía de la glucosa"),
               ("Ribosoma", "arma las proteínas"),
               ("Aparato de Golgi", "modifica, empaca y despacha"),
               ("Lisosoma", "digiere lo que sobra"),
               ("Membrana", "el borde que decide qué entra y qué sale"),
               ("Ósmosis", "el agua va hacia donde hay más disuelto"),
               ("Grupo control", "igual en todo, pero sin el tratamiento")]),
    2: dict(
        titulo="Un cuerpo que se regula solo",
        centro=("Homeostasis", "mantener estable lo de adentro aunque cambie lo de afuera", rango),
        centro_ej="corras o duermas, el pH de tu sangre se mantiene cerca de 7,4: si se sale de ahí, el cuerpo "
                  "lo corrige en minutos.",
        centro_ojo="el cuerpo no evita los cambios: los corrige. Primero algo se desvía, después vuelve.",
        centro_chequeo="¿Qué hace el cuerpo cuando una variable se sale de su rango? (la detecta y la corrige)",
        ideas={
            "El circuito que vuelve al equilibrio": dict(
                corto="desvío, sensor, centro, efector",
                d="Algo se desvía, un sensor lo detecta, un centro de control da la orden y un efector corrige. "
                  "Cuando la corrección apaga la orden, es retroalimentación negativa: el circuito vuelve al "
                  "punto de partida.",
                f="desvío → sensor → centro → efector → equilibrio",
                ej="al subir escaleras aumenta el CO₂ en la sangre; un sensor del cerebro lo detecta y ordena "
                   "respirar más rápido. Cuando el CO₂ baja, la respiración se calma.",
                ojo="la respuesta va CONTRA el desvío: si algo sube, el circuito lo baja. Y cada pieza tiene su "
                    "papel: el sensor detecta, no corrige.",
                chequeo="Un termostato apaga el calentador cuando el cuarto llega a 22 °C. ¿Qué pieza del circuito es su termómetro? (el sensor)",
                svg=circuito),
            "La función sale del texto": dict(
                corto="con las palabras del texto",
                d="La función de una estructura se saca de las palabras del texto: qué hace, para qué y en qué "
                  "situación. No de lo que uno ya cree saber del tema.",
                f="estructura + lo que el texto dice que hace = función",
                ej="si el texto dice «los pelos de la raíz aumentan la superficie que absorbe agua», su función "
                   "es absorber más agua, no sostener la planta.",
                ojo="una opción puede ser cierta en biología y no ser lo que dice el texto: se marca la que el "
                    "texto respalda.",
                chequeo="El texto dice «la grasa del oso guarda energía para el invierno». ¿Qué función le da? (reserva de energía, no abrigo)",
                svg=texto_funcion),
            "Dato contra dato, especie contra especie": dict(
                corto="la misma variable, una al lado de otra",
                d="Para comparar especies se pone la misma variable una al lado de la otra, con la misma unidad, "
                  "y se busca la que se sale del patrón. Esa diferencia es la que hay que explicar.",
                f="misma columna · misma unidad · ¿quién se sale?",
                ej="el corazón de un colibrí llega a unas 1.200 pulsaciones por minuto y el de un elefante late "
                   "unas 30: el pequeño gasta energía mucho más rápido.",
                ojo="compara lo que la tabla mide de verdad: 10 litros de un elefante no son «más» que 1 litro "
                    "de un ratón si la tabla mide por kilo de peso.",
                chequeo="La especie A pierde el 5 % de su agua al día y la B el 20 %. ¿Cuál la conserva mejor? (la A)",
                svg=especies),
            "Lo que alcanza a explicar": dict(
                corto="que dé cuenta de todos los datos",
                d="Una explicación vale si da cuenta de TODOS los datos del caso, no solo de uno. Y un aparato o "
                  "un tratamiento se juzga por lo que hace, no por lo que promete.",
                f="dato 1, dato 2, dato 3: ¿los explica todos?",
                ej="una planta tiene las hojas amarillas y crece poco: «le falta nitrógeno» explica los dos "
                   "datos; «le dio mucho sol» no explica que crezca poco.",
                ojo="una explicación que solo sirve para una parte del caso está incompleta, aunque lo que diga "
                    "sea cierto.",
                chequeo="Una hipótesis explica 3 de los 4 datos del caso. ¿Basta? (no: tiene que dar cuenta de los cuatro)",
                svg=explicaciones),
        },
        vocab=[("Homeostasis", "mantener estable el medio interno"),
               ("Sensor", "detecta el cambio"),
               ("Centro de control", "recibe el aviso y da la orden"),
               ("Efector", "el órgano que corrige"),
               ("Retroalimentación negativa", "la corrección apaga la orden"),
               ("Hormona", "mensajero químico que viaja en la sangre"),
               ("Excreción", "sacar del cuerpo lo que sobra"),
               ("Adaptación", "rasgo que ayuda a vivir en un ambiente"),
               ("Hipótesis", "explicación que se puede poner a prueba")]),
    3: dict(
        titulo="En el ecosistema nada cambia solo",
        centro=("Ecosistema", "seres vivos y ambiente conectados: si cambia una pieza, cambian otras", terrario),
        centro_ej="si en una finca se acaban las abejas, hay menos flores polinizadas y después menos frutos: "
                  "nadie tocó los árboles, pero cambiaron.",
        centro_ojo="en un ecosistema casi nada tiene una sola causa: antes de responder, busca la cadena completa.",
        centro_chequeo="¿Qué une a los seres vivos de un ecosistema? (lo que comen y los recursos que comparten)",
        ideas={
            "Los datos hablan primero": dict(
                corto="primero el dato, después la teoría",
                d="Antes de explicar se lee la gráfica: qué mide cada eje, cuál es el grupo control y cuánto sube "
                  "o baja cada grupo respecto a él. Primero el dato, después la teoría.",
                f="cambio = grupo − control   (+ sube · − baja)",
                ej="en tres charcas: sin peces hay 40 renacuajos (control); con peces, 15 (−25); con peces y "
                   "plantas, 28 (−12). Las plantas les dan refugio.",
                ojo="una barra alta no es un buen resultado por sí sola: mira primero qué mide el eje (puede ser "
                    "plaga, no cosecha).",
                chequeo="El control tiene 50 plantas y el tratamiento 35. ¿Cuánto cambió y hacia dónde? (bajó 15)",
                svg=barras_control),
            "Sigue la red: quién depende de quién": dict(
                corto="red trófica: la flecha va al que come",
                d="Una red trófica dice quién se come a quién; la flecha va del que es comido al que come (sigue "
                  "la energía). Si una población cambia, se siguen las flechas hacia arriba y hacia abajo.",
                f="planta → herbívoro → carnívoro   (la flecha sigue la energía)",
                ej="si se cazan las garzas de una laguna, aumentan las ranas que ellas comían y bajan los "
                   "insectos de los que viven las ranas.",
                ojo="el efecto no se queda en el vecino: llega dos o tres eslabones más allá. Y la flecha apunta "
                    "al que come.",
                chequeo="En pasto → conejo → zorro, si desaparece el zorro, ¿qué le pasa al pasto? (baja, porque hay más conejos)",
                svg=red_trofica),
            "Busca el factor que limita": dict(
                corto="el recurso que más falta manda",
                d="El factor limitante es el recurso más escaso frente a lo que el ser vivo necesita. Manda sobre "
                  "los demás: dar más de lo que ya sobra no sirve; hay que dar lo que falta.",
                f="el crecimiento lo fija el recurso que más falta",
                ej="un cultivo en el desierto tiene sol y abono de sobra, pero poca agua: más abono no lo hace "
                   "crecer; más agua, sí.",
                ojo="el factor limitante cambia: cuando ya hay agua, puede faltar luz. Busca cuál falta en cada "
                    "lugar y en cada momento.",
                chequeo="Una planta tiene luz y agua de sobra, pero el suelo casi no tiene nitrógeno. ¿Qué la frena? (el nitrógeno)",
                svg=limitante),
            "Del saber ecológico a la decisión": dict(
                corto="decidir con un dato que se pueda medir",
                d="Una decisión ambiental se defiende con lo que se sabe del ecosistema y con un dato que se pueda "
                  "comprobar después. «Es bueno para el planeta» no es argumento; «baja el barro del río», sí.",
                f="lo que sé → decido → cómo lo compruebo",
                ej="sembrar árboles nativos en la orilla de una quebrada frena la erosión; se comprueba midiendo "
                   "el barro del agua antes y después.",
                ojo="una buena intención no basta: la decisión tiene que atacar la causa del problema, no solo "
                    "lo que se ve.",
                chequeo="¿Qué dato mostraría que cerrar una mina mejoró un río? (medir el mercurio del agua antes y después)",
                svg=decision),
        },
        vocab=[("Ecosistema", "seres vivos más su ambiente"),
               ("Población", "los de una misma especie en un lugar"),
               ("Comunidad", "todas las poblaciones de un lugar"),
               ("Red trófica", "quién se come a quién"),
               ("Productor", "fabrica su alimento con la luz"),
               ("Consumidor", "se alimenta de otros seres vivos"),
               ("Descomponedor", "devuelve al suelo la materia muerta"),
               ("Factor limitante", "el recurso que más falta y manda"),
               ("Biomasa", "la masa de los seres vivos de un lugar")]),
    4: dict(
        titulo="Un invento se mira con lupa",
        centro=("Indagar un invento",
                "preguntar qué promete, cómo funciona y qué se probó de verdad", matraz_preguntas),
        centro_ej="un filtro casero de arena y carbón promete agua limpia: ¿qué quita?, ¿cómo lo hace?, ¿se "
                  "probó con agua como la de mi vereda?",
        centro_ojo="una noticia sobre un invento mezcla lo que se probó con lo que se espera: sepáralos.",
        centro_chequeo="¿Qué se pregunta primero ante un invento nuevo? (qué promete, cómo funciona y qué se probó)",
        ideas={
            "¿Se puede poner a prueba?": dict(
                corto="qué comparo, qué mido, qué espero",
                d="Una hipótesis se puede poner a prueba si dice qué se compara, qué se mide y qué resultado se "
                  "espera. «Va a cambiar el mundo» no se puede medir; «cicatriza en menos días que sin crema», sí.",
                f="si cambio X, entonces cambia Y (comparado con un control)",
                ej="«las lechugas con riego por goteo dan más gramos por mata que las regadas con manguera»: dice "
                   "qué comparar y qué medir.",
                ojo="«mejor», «sano» o «revolucionario» no se miden: tradúcelos a un número (días, gramos, "
                    "porcentaje).",
                chequeo="«El casco nuevo protege mejor». ¿Qué le falta para ponerlo a prueba? (qué se mide, por ejemplo, la fuerza del golpe)",
                svg=a_prueba),
            "El mecanismo, eslabón por eslabón": dict(
                corto="cómo produce su efecto, paso a paso",
                d="Un mecanismo explica CÓMO algo produce su efecto: una cadena de pasos donde cada eslabón causa "
                  "el siguiente. Si falta un eslabón, la explicación queda cojeando.",
                f="causa → paso 1 → paso 2 → efecto",
                ej="el protector solar absorbe la luz ultravioleta → llega menos radiación a la piel → se daña "
                   "menos el ADN de sus células → menos quemaduras.",
                ojo="una opción puede nombrar bien la causa y el efecto y saltarse el paso del medio: esa no "
                    "explica el mecanismo.",
                chequeo="En «jabón → atrapa la grasa → ___ → manos limpias», ¿qué eslabón falta? (el agua arrastra la grasa)",
                svg=cadena),
            "Para qué sirve cada pieza": dict(
                corto="pieza por pieza: ¿y sin ella?",
                d="Un invento es un conjunto de piezas y cada una cumple una función. Para entenderlo se pregunta, "
                  "pieza por pieza: ¿qué hace esta parte?, ¿qué pasaría sin ella?",
                f="pieza → función → ¿qué pasa sin ella?",
                ej="en un tapabocas, la capa de afuera repele las gotas, la del medio filtra partículas y la de "
                   "adentro absorbe la humedad del aliento.",
                ojo="no le des a una pieza el oficio de otra: en una linterna la pila da la energía y el bombillo "
                    "la vuelve luz, no al revés.",
                chequeo="En una bicicleta, ¿qué pasa si quitas la cadena? (los pedales giran pero la rueda no: la cadena pasa la fuerza)",
                svg=capas),
            "Lo que la evidencia respalda (y lo que no)": dict(
                corto="en quiénes, para qué y en qué condiciones",
                d="Un estudio respalda lo que midió, en quiénes lo midió y en qué condiciones. Llevarlo a otras "
                  "personas, a otro uso o al futuro es una suposición que hay que poner a prueba.",
                f="probado en ___ y para ___ → solo vale para eso",
                ej="un medicamento probado en adultos sanos no está probado en niños: la dosis y el efecto pueden "
                   "cambiar.",
                ojo="«cura», «para todos» y «sin riesgos» casi nunca los sostiene un solo estudio.",
                chequeo="Una crema se probó en 30 ratones. ¿Ya se sabe que sirve en personas? (no: falta probarla en personas)",
                svg=alcance),
        },
        vocab=[("Hipótesis", "respuesta posible que se puede probar"),
               ("Variable", "lo que se cambia o se mide"),
               ("Grupo control", "el que no recibe el tratamiento"),
               ("Mecanismo", "cómo algo produce su efecto, paso a paso"),
               ("Evidencia", "lo que se observó o se midió"),
               ("Biotecnología", "usar seres vivos para hacer productos"),
               ("Nanotecnología", "materiales de tamaño casi molecular"),
               ("Antígeno", "la señal que reconoce el sistema inmune"),
               ("Ética", "pensar si algo está bien hacerlo")]),
    5: dict(
        titulo="Lo que se hereda y lo que se edita",
        centro=("Gen y alelo", "un gen es una instrucción del ADN; los alelos son sus versiones", adn),
        centro_ej="el gen del grupo sanguíneo tiene tres alelos: A, B y O. Cada persona lleva dos, uno de la "
                  "mamá y otro del papá.",
        centro_ojo="tener un alelo no siempre es mostrarlo: uno recesivo puede viajar escondido varias "
                   "generaciones.",
        centro_chequeo="¿Cuántas copias de cada gen tiene una persona y de dónde salen? (dos: una de cada padre)",
        ideas={
            "Seguir el alelo por la familia": dict(
                corto="cuadro de Punnett y pedigrí",
                d="Cada padre aporta un alelo. En el cuadro de Punnett se cruzan los alelos de los dos y se "
                  "cuentan las posibilidades. Si dos padres sanos tienen un hijo afectado, el rasgo es recesivo "
                  "y ambos lo portan.",
                f="Aa × Aa → AA : Aa : aa = 1 : 2 : 1",
                ej="en las arvejas, el verde (a) es recesivo frente al amarillo (A): dos plantas Aa dan, en "
                   "promedio, 1 de cada 4 semillas verde.",
                ojo="1 de cada 4 es una probabilidad para cada hijo, no un reparto fijo: una pareja puede tener "
                    "tres hijos aa seguidos.",
                chequeo="Aa × aa: ¿qué fracción de los hijos sale aa? (la mitad)",
                svg=punnett),
            "Del cambio en el ADN a lo que se ve": dict(
                corto="mutación → ARN → proteína → rasgo",
                d="Una mutación cambia la secuencia del ADN; el ARN copia ese cambio, la proteína sale distinta "
                  "o no sale, y eso se ve en el organismo. Se hereda solo si ocurre en óvulos o espermatozoides.",
                f="ADN cambiado → ARN → proteína distinta → rasgo",
                ej="en la anemia falciforme, una sola letra cambiada en el gen de la hemoglobina la deforma, y el "
                   "glóbulo rojo toma forma de hoz.",
                ojo="no todo lo que cambia el cuerpo cambia el ADN: un tatuaje o un músculo entrenado no pasan "
                    "a los hijos.",
                chequeo="Si cambia una letra del ADN, ¿qué es lo siguiente que sale distinto? (el ARN, y después la proteína)",
                svg=mutacion),
            "La prueba que sí responde la pregunta": dict(
                corto="mide justo lo que se pregunta",
                d="Primero se lee qué pregunta quiere responder el estudio. La prueba correcta mide justo esa "
                  "variable y la compara contra un control; las otras pueden ser útiles, pero responden otra cosa.",
                f="pregunta → qué mido → con qué lo comparo",
                ej="para saber si una vacuna protege a unas gallinas, se comparan vacunadas y no vacunadas y se "
                   "cuentan las enfermas; pesar los huevos responde otra cosa.",
                ojo="una prueba interesante que mide otra variable no responde la pregunta, por bien que suene.",
                chequeo="Pregunta: ¿la música calma a las vacas? ¿Qué mides? (algo de la calma, como el pulso, en vacas con y sin música)",
                svg=diana),
            "Lo que gana, lo que arriesga, lo que exagera": dict(
                corto="beneficio, riesgo y promesas de más",
                d="Una biotecnología se pesa en una balanza: lo que gana (el beneficio), lo que arriesga (los "
                  "efectos no deseados) y lo que exagera (promesas como «siempre» o «sin riesgo»).",
                f="beneficio frente a riesgo · alerta con «siempre» y «nunca»",
                ej="el arroz dorado trae un gen que le da provitamina A: gana nutrición, arriesga cruzarse con "
                   "arroces silvestres y exagera quien diga que acaba solo con el hambre.",
                ojo="ni todo es bueno ni todo es malo: la opción que solo ve un lado suele ser la incorrecta.",
                chequeo="«Esta semilla transgénica nunca tendrá plagas». ¿Qué palabra exagera? (nunca)",
                svg=balanza),
        },
        vocab=[("Gen", "un tramo de ADN con una instrucción"),
               ("Alelo", "una versión de un gen"),
               ("Dominante", "basta una copia para que se vea"),
               ("Recesivo", "se ve solo con las dos copias"),
               ("Genotipo", "los alelos que lleva: AA, Aa o aa"),
               ("Fenotipo", "el rasgo que se ve"),
               ("Mutación", "un cambio en la secuencia del ADN"),
               ("Portador", "lleva el alelo recesivo sin mostrarlo"),
               ("Transgénico", "organismo con un gen de otra especie")]),
    6: dict(
        titulo="La vida cambia con dos relojes",
        centro=("Evolución", "cambio de los rasgos de una población a lo largo de generaciones", generaciones),
        centro_ej="en una isla, después de una sequía sobrevivieron más los pinzones de pico grueso, que "
                  "rompían semillas duras, y sus crías nacieron con picos más gruesos.",
        centro_ojo="un individuo no evoluciona: cambia la población, porque unos dejan más hijos que otros.",
        centro_chequeo="¿Quién evoluciona: un individuo o una población? (la población)",
        ideas={
            "El ambiente o la herencia": dict(
                corto="lo que se vive no se hereda",
                d="Lo que un ser vivo vive o aprende cambia su cuerpo o su conducta, pero no su ADN, y no lo "
                  "hereda. Lo que se hereda cambia en la población, generación tras generación, por selección.",
                f="en una vida: ambiente   ·   en generaciones: herencia y selección",
                ej="un futbolista que entrena mucho gana músculo, pero sus hijos no nacen musculosos: ese cambio "
                   "no pasó al ADN.",
                ojo="«se acostumbró y lo heredó» es el error clásico: lo adquirido en vida no pasa a los hijos.",
                chequeo="Una planta crece alta y delgada a la sombra. ¿Sus semillas, sembradas al sol, darán plantas así? (no: fue el ambiente)",
                svg=relojes),
            "Lo que los datos sí dejan concluir": dict(
                corto="juntas no es causa; un caso no es regla",
                d="Una conclusión vale si los datos la sostienen: que dos cosas suban juntas no prueba que una "
                  "cause la otra, y lo que pasó en un lugar no vale para todos. La mejor usa todos los datos "
                  "que pide la pregunta.",
                f="suben juntas ≠ una causa la otra",
                ej="en vacaciones de mitad de año se venden más helados y hay más quemaduras de sol: suben "
                   "juntos, pero los helados no queman; los dos dependen del sol.",
                ojo="«demuestra», «siempre» o «todas» suelen pasarse de lo que los datos permiten.",
                chequeo="El río con más árboles en la orilla tiene más peces. ¿Ya está probado que los árboles causan los peces? (no: falta un experimento)",
                svg=suben_juntas),
            "Si se cae una pieza del ecosistema": dict(
                corto="el efecto viaja por la red",
                d="Cuando un ecosistema pierde o gana una pieza (una especie, el hábitat, el clima), el efecto "
                  "viaja por la red. Una especie invasora no tiene depredadores y crece sin control; una con un "
                  "solo hábitat desaparece si lo pierde.",
                f="cambio → quién lo sufre primero → quién después",
                ej="el caracol gigante africano llegó a Colombia sin depredadores: se riega rápido y se come "
                   "cultivos y plantas nativas.",
                ojo="no mires solo la especie que se va o que llega: busca también a las que dependían de ella.",
                chequeo="Si llega una especie sin depredadores a un lugar con comida de sobra, ¿qué pasa con su población? (crece rápido, sin control)",
                svg=torre),
            "Para qué le sirve ese rasgo": dict(
                corto="cada rasgo contra un problema del ambiente",
                d="Una adaptación es un rasgo que resuelve un problema del ambiente: frío, sequía, depredadores, "
                  "falta de comida. Para explicarla se pone cada rasgo frente al problema que resuelve.",
                f="rasgo → problema del ambiente que resuelve",
                ej="el cactus: espinas en vez de hojas (pierde menos agua), tallo grueso (guarda agua) y raíces "
                   "anchas y poco hondas (atrapan rápido la lluvia).",
                ojo="el rasgo no aparece porque el animal lo necesite: ya existía, y los que lo tenían "
                    "sobrevivieron más.",
                chequeo="El oso polar tiene una capa gruesa de grasa bajo la piel. ¿Contra qué problema le sirve? (el frío)",
                svg=cactus),
        },
        vocab=[("Evolución", "cambio de una población en generaciones"),
               ("Selección natural", "sobreviven y se reproducen los mejor adaptados"),
               ("Selección artificial", "la persona escoge quién se reproduce"),
               ("Adaptación", "rasgo que resuelve un problema del ambiente"),
               ("Variabilidad", "las diferencias entre individuos"),
               ("Especie invasora", "llega de afuera y crece sin control"),
               ("Hábitat", "el lugar donde vive una especie"),
               ("Extinción", "desaparece el último individuo"),
               ("Fósil", "resto o huella de un ser vivo antiguo")]),
}
