"""Conceptualización de Física (ver conceptos.py, conceptos_area.py y el modelo conceptos_mate.py).

Seis misiones, cada una con su idea central, una tarjeta por estrategia (los nombres son los de
plan_fis.MISIONES[mis]["estr"]) y nueve palabras de vocabulario.

Fuentes: plan_fis.py (MISIONES: instala, ojo y cierre; TALLER: el contexto de las diez preguntas;
BANCO: las cuatro de entrenamiento; NO_ES_TU_FUERTE y SABERES: lo que necesita el profe que no es
del área; ACTIVACION) y la física de grado 10 y 11 que piden esas preguntas.

Los ejemplos son propios: no repiten situaciones, datos ni opciones del taller ni del entrenamiento
(nada de rampas con bloques, bailarines, lavadoras, calorímetros, ollas a presión, trenes con freno
magnético, agujas imantadas, Wi-Fi, drones, sifones ni motores de banda), para que la
conceptualización no resuelva el taller por adelantado. Cada cuenta está resuelta y comprobada.
"""
import math

from conceptos_figs import *  # noqa: F401,F403  (colores y lupa)
from conceptos_figs import _svg, _t, _caja, _flecha, _tarjeta, _bien, _mal, _claro  # el * no trae los _


# ══════════════════════ figuras · Misión 1 ══════════════════════
def fig_c1(c):
    """Centro M1: una fuerza neta cambia la rapidez."""
    s = (f'<line x1="30" y1="240" x2="390" y2="240" stroke="{LINEA}" stroke-width="3"/>'
         + _caja(120, 150, 110, 90, 30, _claro(c, .88))
         + _flecha(30, 195, 112, 195, c, 6) + _t(30, 178, "fuerza", 20, c)
         + _t(290, 80, "la rapidez crece", 20, ORO))
    for k, L in enumerate((30, 60, 90)):
        y = 110 + 40 * k
        s += _flecha(290, y, 290 + L, y, ORO, 4)
    return _svg(s, "Una caja empujada: con fuerza neta, la rapidez crece")


def fig_fuerzas(c):
    """Diagrama de cuerpo libre de una caja jalada por el piso."""
    s = (f'<line x1="40" y1="200" x2="380" y2="200" stroke="{LINEA}" stroke-width="3"/>'
         + _caja(160, 120, 100, 80, 20, _claro(c, .9))
         + f'<circle cx="210" cy="160" r="6" fill="{TINTA}"/>'
         + _flecha(210, 160, 210, 272, ROJO, 5) + _t(222, 266, "P", 24, ROJO)
         + _flecha(210, 160, 210, 50, VERDE, 5) + _t(222, 62, "N", 24, VERDE)
         + _flecha(210, 160, 372, 160, c, 5) + _t(330, 148, "T", 24, c)
         + _flecha(210, 160, 70, 160, ORO, 5) + _t(74, 148, "Fr", 24, ORO))
    return _svg(s, "Caja jalada: peso, normal, tensión y rozamiento, cada uno con su flecha")


def fig_vt(c):
    """Gráfica v–t: pendiente = aceleración, área = distancia."""
    s = (f'<polygon points="60,250 300,250 300,90" fill="{_claro(c)}"/>'
         f'<line x1="60" y1="250" x2="390" y2="250" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="60" y1="250" x2="60" y2="35" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="60" y1="250" x2="300" y2="90" stroke="{c}" stroke-width="6" stroke-linecap="round"/>'
         + _t(38, 52, "v", 24) + _t(372, 280, "t", 24)
         + _t(80, 92, "pendiente", 20, c) + _t(80, 116, "= aceleración", 20, c)
         + _t(200, 236, "área = distancia", 20, TINTA, "middle"))
    return _svg(s, "Gráfica de rapidez contra tiempo: la pendiente es la aceleración y el área la distancia")


def fig_experimento(c):
    """Tres rampas: solo cambia la altura."""
    s = f'<line x1="30" y1="220" x2="390" y2="220" stroke="{LINEA}" stroke-width="3"/>'
    for k, h in enumerate((50, 80, 110)):
        x0 = 40 + 120 * k
        s += (f'<polygon points="{x0},220 {x0+100},220 {x0},{220-h}" fill="{_claro(c, .86)}" '
              f'stroke="{TINTA}" stroke-width="2.5"/>'
              f'<circle cx="{x0+14}" cy="{220-h+3}" r="11" fill="{ORO}" stroke="{TINTA}" stroke-width="2"/>')
    s += (_t(210, 256, "cambia solo la altura", 21, c, "middle")
          + _t(210, 284, "misma canica · mismo piso", 19, TINTA, "middle", "600"))
    return _svg(s, "Tres rampas de distinta altura con la misma canica")


def fig_energia(c):
    """Media caña con barras de energía arriba y abajo."""
    s = (f'<path d="M30 60 Q150 340 270 60" fill="none" stroke="{TINTA}" stroke-width="4"/>'
         f'<circle cx="44" cy="84" r="13" fill="{c}"/>'
         f'<circle cx="150" cy="186" r="13" fill="{ORO}"/>'
         + _t(62, 92, "arriba", 18, TINTA, w="600") + _t(150, 230, "abajo", 18, TINTA, "middle", "600"))
    base = 230
    for x, ep, ec in ((290, 120, 4), (350, 4, 120)):
        s += (f'<rect x="{x}" y="{base-ep}" width="18" height="{ep}" fill="{c}"/>'
              f'<rect x="{x+22}" y="{base-ec}" width="18" height="{ec}" fill="{ORO}"/>')
    s += (f'<line x1="282" y1="{base}" x2="398" y2="{base}" stroke="{TINTA}" stroke-width="2"/>'
          + _t(310, 254, "arriba", 17, TINTA, "middle", "600") + _t(370, 254, "abajo", 17, TINTA, "middle", "600")
          + f'<rect x="290" y="64" width="14" height="14" fill="{c}"/>' + _t(308, 78, "Ep", 18, c)
          + f'<rect x="346" y="64" width="14" height="14" fill="{ORO}"/>' + _t(364, 78, "Ec", 18, ORO)
          + _t(150, 282, "la suma no cambia", 20, TINTA, "middle"))
    return _svg(s, "Patineta en una media caña: arriba toda potencial, abajo toda cinética")


# ══════════════════════ figuras · Misión 2 ══════════════════════
def fig_c2(c):
    """Centro M2: partículas agitadas (caliente) y lentas (frío); el calor va de una a otra."""
    s = (f'<rect x="40" y="80" width="130" height="130" rx="12" fill="{_claro(ROJO, .88)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="250" y="80" width="130" height="130" rx="12" fill="{_claro(AZUL, .9)}" stroke="{TINTA}" stroke-width="2.5"/>')
    for x, y in ((70, 110), (130, 105), (95, 150), (145, 170), (65, 185), (120, 130)):
        s += (f'<circle cx="{x}" cy="{y}" r="7" fill="{ROJO}"/>'
              f'<path d="M{x-18} {y-6} l8 0 M{x-20} {y+4} l10 0" stroke="{ROJO}" stroke-width="2.5" stroke-linecap="round"/>')
    for x, y in ((280, 115), (340, 120), (300, 165), (355, 180), (315, 140)):
        s += f'<circle cx="{x}" cy="{y}" r="7" fill="{AZUL}"/>'
    s += (_flecha(180, 145, 242, 145, c, 6) + _t(211, 125, "calor", 20, c, "middle")
          + _t(105, 245, "caliente", 20, ROJO, "middle") + _t(315, 245, "frío", 20, AZUL, "middle"))
    return _svg(s, "Partículas rápidas en lo caliente y lentas en lo frío; el calor pasa de una a otra")


def fig_viajes(c):
    """Olla en la estufa: conducción por el mango, convección en la sopa, radiación de la llama."""
    s = (f'<rect x="140" y="130" width="140" height="80" rx="8" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="3"/>'
         f'<line x1="280" y1="142" x2="370" y2="142" stroke="{TINTA}" stroke-width="9" stroke-linecap="round"/>'
         f'<path d="M180 190 C160 170 170 150 200 150 C240 150 250 175 235 190" fill="none" stroke="{c}" stroke-width="3.5"/>'
         + _flecha(236, 188, 226, 194, c, 3.5)
         + f'<path d="M180 258 Q190 220 204 234 Q216 212 240 258 Z" fill="{ORO}" stroke="{ROJO}" stroke-width="2"/>'
         + _t(150, 112, "convección", 18, c) + _t(292, 124, "conducción", 18, ORO)
         + f'<path d="M168 236 q-8 -10 -16 0 t-16 0 t-16 0 t-16 0 t-16 0" fill="none" stroke="{ROJO}" stroke-width="3"/>'
         + _flecha(92, 236, 70, 236, ROJO, 3) + _t(30, 274, "radiación", 18, ROJO))
    return _svg(s, "Olla en la estufa: conducción por el mango, convección en la sopa y radiación de la llama")


def fig_cuenta(c):
    """Vaso con agua y termómetro: Q = m · c · ΔT."""
    s = (_t(165, 58, "Q = m · c · ΔT", 26, TINTA, "middle")
         + f'<rect x="90" y="130" width="150" height="110" fill="{_claro(c)}"/>'
         f'<path d="M90 90 L90 240 L240 240 L240 90" fill="none" stroke="{TINTA}" stroke-width="3.5"/>'
         + _t(165, 196, "m", 32, c, "middle")
         + f'<rect x="272" y="70" width="16" height="170" rx="8" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<circle cx="280" cy="248" r="15" fill="{ROJO}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="276" y="140" width="8" height="100" fill="{ROJO}"/>'
         + _flecha(312, 200, 312, 120, ROJO, 4) + _t(322, 168, "ΔT", 24, ROJO))
    return _svg(s, "Un vaso con agua y un termómetro: el calor depende de la masa, el material y los grados")


def fig_particulas(c):
    """Sólido, líquido y gas: las mismas partículas, distinto movimiento."""
    s = ""
    liq = [(18, 62), (36, 66), (54, 62), (72, 66), (90, 62), (27, 80), (45, 84), (63, 80), (81, 84),
           (18, 98), (36, 100), (54, 98), (72, 100), (90, 98)]
    gas = [(20, 20), (80, 30), (50, 55), (16, 88), (88, 80), (52, 96)]
    for k, nombre in enumerate(("sólido", "líquido", "gas")):
        x = 25 + 130 * k
        s += f'<rect x="{x}" y="70" width="110" height="110" rx="10" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
        if k == 0:
            pts = [(x + 22 + 22 * i, 92 + 22 * j) for i in range(4) for j in range(4)]
        elif k == 1:
            pts = [(x + 2 + a, 70 + b) for a, b in liq]
        else:
            pts = [(x + 2 + a, 70 + b) for a, b in gas]
        for px, py in pts:
            s += f'<circle cx="{px}" cy="{py}" r="7" fill="{c}" opacity=".85"/>'
        s += _t(x + 55, 210, nombre, 20, TINTA, "middle")
    s += _flecha(50, 262, 370, 262, ROJO, 4) + _t(210, 250, "más temperatura, más movimiento", 18, ROJO, "middle")
    return _svg(s, "Partículas en un sólido, un líquido y un gas")


def fig_fase(c):
    """La presión de afuera aprieta la superficie: decide a qué temperatura hierve."""
    s = (f'<rect x="120" y="165" width="180" height="85" fill="{_claro(c)}"/>'
         f'<path d="M120 140 L120 250 L300 250 L300 140" fill="none" stroke="{TINTA}" stroke-width="3.5"/>')
    for x in (160, 210, 260):
        s += _flecha(x, 62, x, 152, c, 4)
    for x, y, rr in ((150, 230, 7), (185, 205, 5), (230, 225, 8), (268, 200, 6), (205, 238, 4)):
        s += f'<circle cx="{x}" cy="{y}" r="{rr}" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
    s += (_t(210, 46, "presión de afuera", 20, c, "middle")
          + _t(210, 284, "menos presión: hierve a menos °C", 19, TINTA, "middle", "600"))
    return _svg(s, "La presión del aire empuja la superficie del agua y decide cuándo hierve")


# ══════════════════════ figuras · Misión 3 ══════════════════════
def _carga(x, y, signo, r=28):
    col = ROJO if signo == "+" else AZUL
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{_claro(col, .8)}" stroke="{TINTA}" stroke-width="2.5"/>'
            + _t(x, y + r * 0.36, signo, int(r * 1.1), TINTA, "middle"))


def fig_c3(c):
    """Centro M3: iguales se repelen, distintas se atraen."""
    s = (_t(210, 45, "iguales se repelen", 20, c, "middle")
         + _carga(140, 95, "+") + _carga(280, 95, "+")
         + _flecha(104, 95, 50, 95, TINTA, 4) + _flecha(316, 95, 370, 95, TINTA, 4)
         + _carga(110, 200, "+") + _carga(310, 200, "−")
         + _flecha(146, 200, 190, 200, TINTA, 4) + _flecha(274, 200, 230, 200, TINTA, 4)
         + _t(210, 262, "distintas se atraen", 20, c, "middle"))
    return _svg(s, "Cargas iguales se repelen; cargas distintas se atraen")


def fig_dato(c):
    """Tres datos: solo uno decide."""
    s = (_tarjeta(40, 46, 220, 50, "el color", LINEA)
         + _tarjeta(40, 116, 220, 50, "lo que costó", LINEA)
         + _tarjeta(40, 186, 220, 50, "el voltaje de la pila", c, 19)
         + f'<circle cx="318" cy="211" r="22" fill="#fff" stroke="{c}" stroke-width="6"/>'
         f'<path d="M340 211 L396 211 M380 211 L380 228 M392 211 L392 224" stroke="{c}" stroke-width="6" stroke-linecap="round"/>'
         + _t(330, 272, "el que decide", 20, c, "middle")
         + _t(330, 150, "¿cambia mi", 18, TINTA, "middle", "600") + _t(330, 172, "respuesta?", 18, TINTA, "middle", "600"))
    return _svg(s, "Tres datos sobre una linterna; solo el voltaje decide")


def fig_campo(c):
    """Líneas de campo que salen de una carga positiva."""
    s = ""
    for k in range(8):
        a = math.radians(45 * k)
        x1, y1 = 170 + 36 * math.cos(a), 150 + 36 * math.sin(a)
        x2, y2 = 170 + 108 * math.cos(a), 150 + 108 * math.sin(a)
        s += _flecha(round(x1, 1), round(y1, 1), round(x2, 1), round(y2, 1), c, 3.5)
    s += (_carga(170, 150, "+", 26)
          + f'<circle cx="330" cy="150" r="14" fill="{_claro(ROJO, .8)}" stroke="{TINTA}" stroke-width="2"/>'
          + _t(330, 157, "+", 18, TINTA, "middle") + _flecha(346, 150, 398, 150, ROJO, 4)
          + _t(370, 136, "F", 20, ROJO, "middle") + _t(300, 62, "sale de +", 20, c))
    return _svg(s, "Líneas de campo que salen de una carga positiva como rayos")


def fig_signo(c):
    """F = q · E: la positiva va a favor del campo, la negativa en contra."""
    s = (_t(40, 48, "campo E", 20, c)
         + _flecha(40, 70, 390, 70, c, 3) + _flecha(40, 236, 390, 236, c, 3)
         + _carga(90, 155, "+", 24) + _flecha(118, 155, 190, 155, ROJO, 5) + _t(154, 140, "F", 22, ROJO, "middle")
         + _carga(330, 155, "−", 24) + _flecha(302, 155, 240, 155, AZUL, 5) + _t(271, 140, "F", 22, AZUL, "middle")
         + _t(110, 206, "a favor", 18, TINTA, "middle", "600") + _t(305, 206, "en contra", 18, TINTA, "middle", "600")
         + _t(210, 278, "C × N/C = N", 22, TINTA, "middle"))
    return _svg(s, "En un campo hacia la derecha, la fuerza sobre la carga positiva va a favor y sobre la negativa en contra")


def fig_mecanismo(c):
    """Causa → lo que pasa por dentro → lo que se ve."""
    s = ""
    for k, (rot, l1, l2) in enumerate((("causa", "gira", "el imán"), ("por dentro", "cambia", "el campo"),
                                        ("lo que se ve", "prende", "el bombillo"))):
        x = 15 + 135 * k
        s += (_caja(x, 120, 100, 80, 18, "#fff", _claro(c, .7), _claro(c, .9))
              + _t(x + 50, 154, l1, 20, TINTA, "middle") + _t(x + 50, 180, l2, 18, TINTA, "middle", "600")
              + _t(x + 58, 88, rot, 18, c, "middle"))
        if k < 2:
            s += _flecha(x + 104, 220, x + 150, 220, c, 4)
    s += _t(210, 270, "explicar = contar la cadena", 20, TINTA, "middle")
    return _svg(s, "Una cadena de tres pasos: causa, lo que pasa por dentro y lo que se ve")


# ══════════════════════ figuras · Misión 4 ══════════════════════
def _onda(x0, x1, y, A, lam, fase=0.0, paso=4):
    pts = []
    x = x0
    while x <= x1:
        pts.append(f"{x:.0f},{y - A * math.sin(fase + 2 * math.pi * (x - x0) / lam):.1f}")
        x += paso
    return " ".join(pts)


def fig_c4(c):
    """Centro M4: una onda con su longitud de onda y su amplitud."""
    s = (f'<line x1="30" y1="150" x2="395" y2="150" stroke="{LINEA}" stroke-width="2"/>'
         f'<polyline points="{_onda(40, 384, 150, 60, 140)}" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
         f'<path d="M75 66 L215 66 M75 58 L75 74 M215 58 L215 74" stroke="{ORO}" stroke-width="3.5"/>'
         + _t(145, 54, "λ", 26, ORO, "middle")
         + f'<line x1="285" y1="150" x2="285" y2="210" stroke="{ROJO}" stroke-width="3.5"/>'
         + _t(290, 262, "amplitud", 19, ROJO, "middle"))
    return _svg(s, "Una onda con su longitud de onda entre dos crestas y su amplitud")


def fig_frecuencia(c):
    """La onda pasa a otro medio: misma frecuencia, otra longitud de onda."""
    izq = _onda(30, 220, 160, 48, 100)
    der = _onda(220, 392, 160, 48, 50, fase=2 * math.pi * 1.9)
    s = (f'<rect x="220" y="80" width="180" height="160" fill="{_claro(c, .86)}"/>'
         f'<polyline points="{izq} {der}" fill="none" stroke="{c}" stroke-width="5" stroke-linejoin="round"/>'
         + _t(40, 82, "medio 1", 18, TINTA, w="600") + _t(236, 102, "medio 2", 18, TINTA, w="600")
         + _t(210, 48, "la frecuencia no cambia", 20, ORO, "middle")
         + _t(110, 268, "λ larga", 20, TINTA, "middle") + _t(310, 268, "λ corta", 20, TINTA, "middle"))
    return _svg(s, "Una onda que pasa a un medio más lento: la misma frecuencia con una longitud de onda más corta")


def fig_lapiz(c):
    """Un lápiz en un vaso de agua se ve quebrado."""
    s = (f'<rect x="130" y="150" width="160" height="100" fill="{_claro(c)}"/>'
         f'<path d="M130 80 L130 250 L290 250 L290 80" fill="none" stroke="{TINTA}" stroke-width="3.5"/>'
         f'<line x1="210" y1="110" x2="210" y2="205" stroke="{GRIS}" stroke-width="2.5" stroke-dasharray="7 6"/>'
         f'<line x1="110" y1="40" x2="210" y2="150" stroke="{ORO}" stroke-width="10" stroke-linecap="round"/>'
         f'<line x1="210" y1="150" x2="250" y2="236" stroke="{ORO}" stroke-width="10" stroke-linecap="round"/>'
         + _t(218, 112, "normal", 18, GRIS) + _t(300, 126, "aire", 20, TINTA) + _t(300, 210, "agua", 20, c)
         + _t(210, 286, "se ve quebrado", 20, TINTA, "middle"))
    return _svg(s, "Un lápiz dentro de un vaso de agua se ve quebrado en la superficie")


def fig_observo(c):
    """Lo que vi frente a lo que supongo."""
    s = (_tarjeta(40, 56, 170, 60, "lo que vi", VERDE, 22)
         + _tarjeta(220, 56, 170, 60, "lo que supongo", ROJO, 21)
         + _t(125, 160, "el trueno llegó", 18, TINTA, "middle", "600")
         + _t(125, 186, "3 s después", 18, TINTA, "middle", "600")
         + _t(305, 160, "qué tan lejos,", 18, TINTA, "middle", "600")
         + _t(305, 186, "sin medir", 18, TINTA, "middle", "600")
         + _bien(110, 222) + _mal(295, 214))
    return _svg(s, "Dos columnas: lo que se observó sí se concluye; lo que se supone, no")


def fig_db(c):
    """Escalera de decibeles: cada 10 dB, diez veces la potencia."""
    s = ""
    for k, db in enumerate((60, 70, 80, 90)):
        x, h = 40 + 85 * k, 50 + 40 * k
        s += (_caja(x, 250 - h, 80, h, 20, "#fff", _claro(c, .7), _claro(c, .9))
              + _t(x + 40, 250 - h + 32, f"{db} dB", 20, TINTA, "middle"))
        if k:
            s += _t(x + 46, 250 - h - 20, "×10", 20, ORO, "middle")
    s += _t(210, 284, "de 60 a 90 dB: ×1.000", 20, TINTA, "middle")
    return _svg(s, "Escalones de 60, 70, 80 y 90 decibeles: cada escalón multiplica por diez")


# ══════════════════════ figuras · Misión 5 ══════════════════════
def fig_c5(c):
    """Centro M5: energía de altura y energía de movimiento."""
    s = (f'<path d="M30 92 C140 92 160 240 260 240 L395 240" fill="none" stroke="{TINTA}" stroke-width="4"/>'
         f'<circle cx="52" cy="76" r="16" fill="{c}"/>'
         f'<circle cx="320" cy="224" r="16" fill="{ORO}"/>'
         f'<path d="M282 216 l-26 0 M286 228 l-34 0" stroke="{ORO}" stroke-width="3.5" stroke-linecap="round"/>'
         + _t(76, 66, "Ep: altura", 20, c) + _t(320, 192, "Ec: rapidez", 20, ORO, "middle")
         + _t(210, 284, "Ep + Ec = energía mecánica", 20, TINTA, "middle"))
    return _svg(s, "Una pelota arriba de una loma tiene energía de altura; abajo, energía de movimiento")


def fig_unidades(c):
    """Cada magnitud con su unidad: etiquetas."""
    s = ""
    for k, (txt, fuerte) in enumerate((("m → kg", False), ("h → m", False), ("v → m/s", False), ("E → J", True))):
        x, y = 40 + 190 * (k % 2), 52 + 100 * (k // 2)
        col = c if fuerte else TINTA
        s += (f'<rect x="{x}" y="{y}" width="150" height="70" rx="14" fill="{_claro(c, .9) if fuerte else "#fff"}" '
              f'stroke="{col}" stroke-width="{4 if fuerte else 2.5}"/>'
              f'<circle cx="{x+18}" cy="{y+35}" r="7" fill="#fff" stroke="{col}" stroke-width="2.5"/>'
              + _t(x + 88, y + 44, txt, 24, col, "middle"))
    s += _t(210, 270, "sin unidad, no hay cuenta", 20, TINTA, "middle")
    return _svg(s, "Etiquetas: masa en kilogramos, altura en metros, rapidez en m/s y energía en julios")


def fig_trabajo(c):
    """Solo trabaja la parte de la fuerza que va a lo largo del camino."""
    s = (f'<line x1="40" y1="242" x2="390" y2="242" stroke="{LINEA}" stroke-width="3"/>'
         f'<rect x="110" y="170" width="120" height="50" rx="6" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<circle cx="135" cy="230" r="12" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<circle cx="205" cy="230" r="12" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + _flecha(230, 180, 330, 110, c, 5) + _t(338, 108, "F", 24, c)
         + f'<line x1="230" y1="180" x2="330" y2="180" stroke="{ORO}" stroke-width="4" stroke-dasharray="9 6"/>'
         + f'<path d="M270 180 A40 40 0 0 0 263 157" fill="none" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(278, 170, "θ", 20) + _t(240, 206, "la que trabaja", 18, ORO, w="600")
         + _flecha(110, 272, 300, 272, GRIS, 3.5) + _t(310, 279, "d", 22, GRIS))
    return _svg(s, "Un carrito jalado en diagonal: solo la parte de la fuerza a lo largo del camino hace trabajo")


def fig_pendulo(c):
    """Tres péndulos: cambia solo el largo; cada uno se mide cinco veces."""
    s = f'<rect x="50" y="40" width="320" height="12" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="2"/>'
    for k, L in enumerate((80, 130, 180)):
        x = 90 + 120 * k
        y = 52 + L
        s += (f'<line x1="{x}" y1="52" x2="{x}" y2="{y}" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<path d="M{x-30} {y-6} Q{x} {y+14} {x+30} {y-6}" fill="none" stroke="{GRIS}" stroke-width="2" stroke-dasharray="5 5"/>'
              f'<circle cx="{x}" cy="{y}" r="16" fill="{_claro(c, .8)}" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x + 34, y + 24, "×5", 18, ORO))
    s += _t(150, 280, "solo cambia el largo", 20, c, "middle")
    return _svg(s, "Tres péndulos de distinto largo, con la misma masa, medidos cinco veces cada uno")


def fig_globo(c):
    """Acción y reacción: el aire sale hacia atrás y el globo va hacia adelante."""
    s = (f'<ellipse cx="250" cy="160" rx="90" ry="62" fill="{_claro(c)}" stroke="{TINTA}" stroke-width="3"/>'
         f'<polygon points="162,160 146,149 146,171" fill="{_claro(c, .6)}" stroke="{TINTA}" stroke-width="2.5"/>'
         + _flecha(140, 146, 66, 136, GRIS, 3.5) + _flecha(140, 160, 56, 160, GRIS, 3.5)
         + _flecha(140, 174, 66, 184, GRIS, 3.5)
         + _t(60, 118, "acción", 20, TINTA)
         + _flecha(220, 70, 370, 70, c, 6) + _t(290, 52, "reacción", 20, c, "middle")
         + _t(100, 230, "el aire sale", 18, GRIS, "middle", "600"))
    return _svg(s, "Un globo suelta aire hacia atrás y sale disparado hacia adelante")


# ══════════════════════ figuras · Misión 6 ══════════════════════
def fig_c6(c):
    """Centro M6: lo que entra se reparte en útil y calor."""
    s = (f'<rect x="30" y="70" width="150" height="100" fill="{_claro(c, .8)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="180,70 320,70 320,56 372,90 320,124 320,110 180,110" fill="{_claro(c, .65)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M180 110 Q240 110 240 170 L240 215 L260 215 L210 262 L160 215 L180 215 Z" fill="{_claro(ROJO, .75)}" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(105, 114, "entra", 22, TINTA, "middle") + _t(105, 146, "100 J", 22, TINTA, "middle")
         + _t(250, 97, "útil 40 J", 20, TINTA, "middle") + _t(272, 250, "calor 60 J", 20, ROJO))
    return _svg(s, "Diagrama de flujo: entran 100 J, salen 40 J útiles y 60 J como calor")


def fig_watts(c):
    """W × s = J."""
    s = _t(210, 55, "1 W = 1 J cada segundo", 22, TINTA, "middle")
    for k, (sim, nom) in enumerate((("W", "vatios"), ("s", "segundos"), ("J", "julios"))):
        x = 25 + 135 * k
        s += (_caja(x, 110, 80, 90, 20, _claro(c, .9) if k == 2 else "#fff", _claro(c, .7), _claro(c, .92))
              + _t(x + 40, 170, sim, 40, c if k == 2 else TINTA, "middle")
              + _t(x + 40, 235, nom, 18, TINTA, "middle", "600"))
    s += _t(142, 168, "×", 34, TINTA, "middle") + _t(277, 168, "=", 34, TINTA, "middle")
    return _svg(s, "Vatios por segundos dan julios")


def fig_cadena(c):
    """Linterna: química → eléctrica → luz + calor."""
    s = (f'<rect x="30" y="115" width="80" height="50" rx="6" fill="{_claro(c, .85)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="110" y="131" width="8" height="18" fill="{TINTA}"/>'
         + _t(70, 148, "pila", 20, TINTA, "middle") + _t(70, 195, "química", 18, c, "middle")
         + _flecha(124, 140, 168, 140, c, 4) + _t(136, 112, "eléctrica", 18, c, "middle")
         + f'<circle cx="215" cy="140" r="40" fill="{_claro(ORO, .8)}" opacity=".7"/>'
         f'<circle cx="215" cy="140" r="30" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="203" y="170" width="24" height="20" fill="{_claro(TINTA, .7)}" stroke="{TINTA}" stroke-width="2"/>'
         + _flecha(262, 120, 330, 86, ORO, 4) + _t(338, 86, "luz", 20, ORO)
         + _flecha(262, 162, 330, 196, ROJO, 4) + _t(338, 206, "calor", 20, ROJO)
         + _t(210, 268, "entra = luz + calor", 20, TINTA, "middle"))
    return _svg(s, "La energía de una linterna pasa de química a eléctrica y sale como luz y calor")


def fig_puente(c):
    """El puente de los datos no alcanza a la conclusión."""
    s = (_caja(20, 160, 110, 100, 20, "#fff", _claro(c, .7), _claro(c, .9))
         + _t(75, 218, "datos", 20, TINTA, "middle")
         + _caja(280, 110, 100, 150, 20, "#fff", _claro(ROJO, .7), _claro(ROJO, .9))
         + _t(330, 194, "conclusión", 18, TINTA, "middle")
         + f'<rect x="150" y="146" width="80" height="12" fill="{c}"/>'
         f'<line x1="236" y1="152" x2="276" y2="152" stroke="{ROJO}" stroke-width="3" stroke-dasharray="6 5"/>'
         + _mal(242, 172) + _t(250, 78, "falta medir", 20, ROJO, "middle"))
    return _svg(s, "Un puente que sale de los datos y no alcanza a llegar a la conclusión")


def fig_tanque(c):
    """Entra tanto como sale: el nivel se queda quieto."""
    s = (f'<rect x="120" y="150" width="180" height="100" fill="{_claro(c)}"/>'
         f'<path d="M120 90 L120 250 L300 250 L300 90" fill="none" stroke="{TINTA}" stroke-width="3.5"/>'
         f'<path d="M50 50 L166 50 L166 70" fill="none" stroke="{TINTA}" stroke-width="10" stroke-linejoin="round"/>'
         f'<rect x="161" y="72" width="10" height="78" fill="{_claro(c, .5)}"/>'
         f'<path d="M300 236 Q340 236 352 282" fill="none" stroke="{_claro(c, .4)}" stroke-width="9" stroke-linecap="round"/>'
         f'<line x1="118" y1="150" x2="322" y2="150" stroke="{ORO}" stroke-width="3" stroke-dasharray="9 6"/>'
         + _t(180, 42, "entra", 20, c) + _t(322, 214, "sale", 20, c)
         + _t(20, 144, "nivel", 18, ORO) + _t(20, 166, "quieto", 18, ORO)
         + _t(210, 284, "entra = sale", 20, TINTA, "middle"))
    return _svg(s, "Un tanque con una llave arriba y un hueco abajo: cuando entra tanto como sale, el nivel no cambia")


# ══════════════════════ los datos de las seis misiones ══════════════════════
DATOS = {
    1: dict(
        titulo="Nada se mueve ni se detiene porque sí",
        centro=("Fuerza y movimiento", "una fuerza neta cambia la rapidez o la dirección; sin ella, todo sigue como iba",
                fig_c1),
        centro_ej="un disco de hockey sobre hielo sigue deslizando casi sin frenar: casi no hay rozamiento que lo detenga.",
        centro_ojo="moverse no necesita fuerza; cambiar el movimiento, sí.",
        centro_chequeo="Una nave en el espacio apaga los motores. ¿Se detiene? (no: sigue en línea recta con la misma rapidez)",
        ideas={
            "Las fuerzas, una por una": dict(
                corto="el diagrama de cuerpo libre",
                d="Se dibuja el objeto y cada fuerza como una flecha con nombre y con quién la hace: peso (la Tierra, "
                  "hacia abajo), normal (la superficie, perpendicular a ella), rozamiento (contra el deslizamiento) y "
                  "tensión (la cuerda).",
                f="fuerza neta = suma de flechas · si da 0, sigue como iba",
                ej="una lámpara colgada de un cable: peso hacia abajo y tensión hacia arriba, iguales. Fuerza neta 0: "
                   "la lámpara sigue quieta.",
                ojo="la normal es perpendicular a la superficie, no siempre vertical. Y cada flecha tiene un «quién»: "
                    "si no sabes quién la hace, sobra.",
                chequeo="Un libro quieto en una mesa, ¿qué dos fuerzas tiene y quién las hace? (peso, la Tierra; normal, la mesa)",
                svg=fig_fuerzas),
            "La gráfica cuenta el movimiento": dict(
                corto="pendiente = aceleración; área = distancia",
                d="En una gráfica de rapidez contra tiempo, la altura de la línea es la rapidez, su inclinación "
                  "(pendiente) es la aceleración y el área bajo la línea es la distancia recorrida.",
                f="a = Δv ÷ Δt   ·   distancia = área bajo la línea",
                ej="una moto pasa de 0 a 20 m/s en 4 s: a = 20 ÷ 4 = 5 m/s². Recorre el área del triángulo: "
                   "½ · 4 · 20 = 40 m.",
                ojo="en una gráfica v–t, una línea horizontal no es «quieto»: es rapidez constante. Quieto es la línea "
                    "pegada al cero.",
                chequeo="Va a 10 m/s constantes durante 6 s. ¿Qué distancia recorre? (60 m: el área del rectángulo)",
                svg=fig_vt),
            "El experimento justo": dict(
                corto="cambiar una sola cosa",
                d="Para saber si algo influye se cambia solo eso (la variable que cambio), se mide el efecto (la que "
                  "mido) y todo lo demás se deja igual (las controladas).",
                f="cambio 1 · mido 1 · el resto igual",
                ej="¿la altura de una rampa cambia qué tan lejos rueda una canica? Cambio la altura, mido la distancia "
                   "y dejo igual la canica, la rampa y el piso.",
                ojo="si cambias dos cosas a la vez, no sabrás cuál produjo el efecto.",
                chequeo="Pruebo si la suela cambia el agarre, pero un zapato va en baldosa y otro en cemento. ¿Qué falla? (cambié dos cosas)",
                svg=fig_experimento),
            "Lo que se conserva": dict(
                corto="la energía cambia de forma, no se pierde",
                d="La energía no se crea ni se destruye: cambia de forma. La de altura (potencial) se vuelve de "
                  "movimiento (cinética) y lo que roza se vuelve calor. La suma total queda igual.",
                f="Ep + Ec + calor = siempre lo mismo",
                ej="una patineta en una media caña: arriba casi quieta (toda potencial), abajo rapidísima (toda "
                   "cinética). Cada pasada sube un poco menos: lo que falta se volvió calor.",
                ojo="«se perdió energía» casi siempre quiere decir «se volvió calor o sonido»: no desapareció.",
                chequeo="Un columpio sube cada vez menos si nadie lo empuja. ¿A dónde se fue la energía? (calor y sonido por el roce)",
                svg=fig_energia),
        },
        vocab=[("Fuerza", "empujón o jalón que alguien le hace a algo"),
               ("Fuerza neta", "la suma de todas las fuerzas"),
               ("Peso", "la fuerza con que la Tierra jala hacia abajo"),
               ("Normal", "la fuerza de la superficie, perpendicular a ella"),
               ("Rozamiento", "la fuerza que se opone al deslizamiento"),
               ("Inercia", "seguir como iba si nada lo cambia"),
               ("Aceleración", "cuánto cambia la rapidez cada segundo"),
               ("Variable controlada", "lo que se deja igual en el experimento"),
               ("Energía cinética", "la energía del movimiento")]),
    2: dict(
        titulo="El calor siempre baja la cuesta",
        centro=("Calor y temperatura",
                "la temperatura es la agitación de las partículas; el calor, la energía que pasa del caliente al frío",
                fig_c2),
        centro_ej="una taza de chocolate en la mesa se enfría hasta quedar a la temperatura del cuarto, y ahí para.",
        centro_ojo="el frío no es algo que entra: es calor que sale.",
        centro_chequeo="Una baranda de metal se siente fría. ¿El metal le pasa frío a la mano? (no: la mano le pasa calor al metal)",
        ideas={
            "El calor va del caliente al frío": dict(
                corto="conducción, convección y radiación",
                d="Solo, el calor va siempre de lo caliente a lo frío. Viaja por contacto, de partícula en partícula "
                  "(conducción); con el fluido caliente que sube (convección), o sin medio, como la luz (radiación).",
                f="conducción · convección · radiación",
                ej="en una olla de sopa al fuego: el mango se calienta por conducción, la sopa da vueltas por "
                   "convección y la llama te calienta la cara por radiación.",
                ojo="el aire caliente sube porque es menos denso, no porque «el calor sube».",
                chequeo="¿Cómo llega a la Tierra el calor del Sol, si en el espacio no hay aire? (por radiación)",
                svg=fig_viajes),
            "La cuenta del calor": dict(
                corto="Q = m · c · ΔT",
                d="El calor que gana o pierde un cuerpo es su masa por su calor específico por el cambio de "
                  "temperatura. El calor específico dice cuánto calor cuesta subirle un grado a un gramo.",
                f="Q = m · c · ΔT",
                ej="calentar 200 g de agua (c = 1 cal/(g·°C)) de 20 °C a 70 °C: Q = 200 · 1 · 50 = 10.000 cal.",
                ojo="las unidades tienen que casar: gramos con cal/(g·°C), kilogramos con J/(kg·°C). Y ΔT es "
                    "final menos inicial.",
                chequeo="¿Cuántas calorías necesitan 50 g de agua para subir 4 °C? (200 cal)",
                svg=fig_cuenta),
            "Lo que hacen las partículas": dict(
                corto="temperatura = agitación",
                d="La temperatura mide qué tan rápido se mueven las partículas. En el sólido vibran en su puesto, en "
                  "el líquido se deslizan unas sobre otras y en el gas vuelan libres y separadas.",
                f="más temperatura = partículas más rápidas",
                ej="una gota de colorante se riega más rápido en agua caliente que en agua fría: allá las partículas "
                   "se mueven más.",
                ojo="al calentarse, las partículas no crecen: se mueven más rápido y se separan.",
                chequeo="¿En qué estado las partículas están más separadas y libres? (en el gas)",
                svg=fig_particulas),
            "El ambiente decide el cambio de fase": dict(
                corto="la presión decide cuándo hierve",
                d="Un líquido hierve cuando la presión de su vapor iguala la presión de afuera. Con menos presión "
                  "hierve a menos temperatura; con más presión, a más.",
                f="menos presión afuera → hierve a menos temperatura",
                ej="en una jeringa tapada con agua tibia, al jalar el émbolo baja la presión y el agua burbujea sin "
                   "estar cerca de 100 °C.",
                ojo="mientras hierve, el agua no sube de temperatura aunque la llama siga: el calor se gasta en "
                    "cambiar de fase.",
                chequeo="Si baja la presión de afuera, ¿el agua hierve a más o a menos de 100 °C? (a menos)",
                svg=fig_fase),
        },
        vocab=[("Temperatura", "qué tan agitadas están las partículas"),
               ("Calor", "energía que pasa del caliente al frío"),
               ("Conducción", "calor por contacto, partícula a partícula"),
               ("Convección", "calor que viaja con el fluido que sube"),
               ("Radiación", "calor que viaja sin medio, como la luz"),
               ("Calor específico", "calor para subir 1 °C a un gramo"),
               ("Equilibrio térmico", "cuando las temperaturas se igualan"),
               ("Presión", "fuerza que se reparte sobre un área"),
               ("Punto de ebullición", "la temperatura a la que hierve")]),
    3: dict(
        titulo="Lo que mueve a las cargas",
        centro=("Carga eléctrica", "iguales se repelen, distintas se atraen; en un metal se mueven los electrones",
                fig_c3),
        centro_ej="un globo frotado en el pelo se pega a la pared: quedó cargado y atrae las cargas de la pared.",
        centro_ojo="lo que se mueve casi siempre son los electrones; los protones se quedan en los núcleos.",
        centro_chequeo="Dos esferas con carga negativa se acercan. ¿Se atraen o se repelen? (se repelen)",
        ideas={
            "Busca el dato que decide": dict(
                corto="el dato que confirma o tumba",
                d="Para evaluar una explicación se pregunta: ¿qué dato, si lo midiera, me diría si es cierta o falsa? "
                  "Ese es el dato que decide. Los demás pueden ser verdad y no decidir nada.",
                f="explicación → ¿qué medida la confirma o la tumba?",
                ej="«la linterna no prende porque se acabaron las pilas»: decide el voltaje de las pilas, no el color "
                   "de la linterna ni lo que costó.",
                ojo="un dato interesante no es un dato que decide: pregúntate si cambiaría tu respuesta.",
                chequeo="«El bombillo se fundió». ¿Qué dato lo confirma? (el filamento roto, o que al cambiarlo prenda)",
                svg=fig_dato),
            "Dibuja el campo primero": dict(
                corto="las líneas salen de + y llegan a −",
                d="Las líneas de campo salen de las cargas positivas y llegan a las negativas, nunca se cruzan y se "
                  "aprietan donde el campo es más fuerte. Una carga positiva se empuja a favor de la línea.",
                f="sale de + · llega a − · nunca se cruzan",
                ej="alrededor de una sola carga positiva las líneas salen como los rayos de una rueda: juntas cerca "
                   "de la carga, separadas lejos.",
                ojo="la flecha dice hacia dónde iría una carga positiva; un electrón va al revés.",
                chequeo="En un punto las líneas están más apretadas. ¿Ahí el campo es más fuerte o más débil? (más fuerte)",
                svg=fig_campo),
            "Signo, sentido y unidad": dict(
                corto="F = q · E, completa",
                d="Una fuerza eléctrica se dice completa: cuánto (con su unidad), hacia dónde y con qué signo. La "
                  "fuerza sobre una carga es la carga por el campo, y da newtons.",
                f="F = q · E   ·   C × N/C = N",
                ej="una carga de 3 μC en un campo de 500 N/C: F = 0,000003 · 500 = 0,0015 N, en el sentido del campo.",
                ojo="μ es millonésima: 3 μC = 0,000003 C. Y si la carga es negativa, la fuerza va contra el campo.",
                chequeo="El campo apunta a la derecha. ¿Hacia dónde va la fuerza sobre un electrón? (a la izquierda)",
                svg=fig_signo),
            "Del modelo al mecanismo": dict(
                corto="contar la cadena por dentro",
                d="Un modelo explica qué pasa por dentro, paso por paso: electrones que se mueven, un campo que "
                  "cambia, dominios que se ordenan o se desordenan. Explicar es contar esa cadena, no nombrar el "
                  "resultado.",
                f="causa → lo que pasa por dentro → lo que se ve",
                ej="la dínamo de una bicicleta: la rueda hace girar un imán junto a una bobina, el campo cambia y "
                   "aparece corriente. El bombillo prende solo mientras pedaleas.",
                ojo="«porque es magnético» no explica nada: di qué se mueve, qué cambia y qué resulta.",
                chequeo="Si dejas de pedalear, ¿por qué se apaga la dínamo? (el imán deja de girar y el campo ya no cambia)",
                svg=fig_mecanismo),
        },
        vocab=[("Carga eléctrica", "positiva o negativa; iguales se repelen"),
               ("Electrón", "partícula negativa que se mueve en los metales"),
               ("Campo eléctrico", "la zona donde una carga siente fuerza"),
               ("Línea de campo", "sale de + y llega a −"),
               ("Coulomb (C)", "la unidad de carga"),
               ("N/C", "unidad del campo: newtons por coulomb"),
               ("Corriente", "cargas que se mueven por un conductor"),
               ("Inducción", "corriente que aparece cuando el campo cambia"),
               ("Dominio magnético", "zona diminuta que actúa como un imán")]),
    4: dict(
        titulo="La fuente marca el ritmo",
        centro=("Onda", "una perturbación que viaja y lleva energía, pero no lleva la materia", fig_c4),
        centro_ej="una boya en el mar sube y baja cuando pasa una ola, pero no viaja con ella hasta la playa.",
        centro_ojo="lo que viaja es la perturbación; el medio se queda en su sitio.",
        centro_chequeo="Un corcho sube y baja 3 veces en un segundo. ¿Cuál es la frecuencia de la onda? (3 Hz)",
        ideas={
            "La fuente pone la frecuencia": dict(
                corto="el ritmo, de la fuente; la rapidez, del medio",
                d="La frecuencia (cuántas ondas por segundo) la pone la fuente y no cambia al pasar a otro medio. La "
                  "rapidez la pone el medio. Si cambia la rapidez y la frecuencia no, cambia la longitud de onda.",
                f="v = λ · f   →   λ = v ÷ f",
                ej="un sonido de 340 Hz en el aire (340 m/s) tiene λ = 1 m; en el agua (unos 1.500 m/s) sigue en "
                   "340 Hz, pero λ ≈ 4,4 m.",
                ojo="al cambiar de medio no cambia la frecuencia: cambian la rapidez y la longitud de onda.",
                chequeo="Una onda de 5 Hz avanza a 20 m/s. ¿Cuál es su longitud de onda? (4 m)",
                svg=fig_frecuencia),
            "Dibújalo antes de elegir": dict(
                corto="el rayo, la normal y el medio",
                d="Antes de mirar las opciones se dibuja el rayo y la normal (la perpendicular a la superficie). Al "
                  "pasar a un medio donde va más lenta, la luz se acerca a la normal; donde va más rápida, se aleja.",
                f="más lenta → se acerca a la normal",
                ej="un lápiz dentro de un vaso con agua se ve quebrado: la luz que sale del agua se dobla y el ojo la "
                   "sigue en línea recta.",
                ojo="el ángulo se mide desde la normal, no desde la superficie.",
                chequeo="La luz pasa del agua al aire, donde va más rápido. ¿Se acerca o se aleja de la normal? (se aleja)",
                svg=fig_lapiz),
            "Concluye solo lo observado": dict(
                corto="lo que vi, no lo que supongo",
                d="Una conclusión no puede decir más que lo observado. Para afirmar algo nuevo (qué tan lejos, por "
                  "qué, siempre) hace falta medirlo o controlar lo que podría cambiar el resultado.",
                f="lo que vi ✓   ·   lo que supongo ✗",
                ej="si el trueno llega 3 s después del rayo, sé que el sonido tardó; para la distancia necesito su "
                   "rapidez: 340 · 3 ≈ 1.000 m.",
                ojo="«siempre», «todas» y «porque» suelen ir más allá de lo que se observó.",
                chequeo="Vi que una cuerda más tensa suena más agudo. ¿Vale para todas las cuerdas? (no sin probar otras)",
                svg=fig_observo),
            "Lee la tabla y su escala": dict(
                corto="decibeles: escala de veces",
                d="Antes de comparar los números de una tabla se mira la unidad y la escala. Los decibeles no se "
                  "suman: cada 10 dB más es 10 veces más potencia; 20 dB, 100 veces.",
                f="+10 dB = ×10   ·   +20 dB = ×100   ·   +30 dB = ×1.000",
                ej="una conversación (60 dB) y una licuadora (90 dB): 30 dB de diferencia. La licuadora lleva unas "
                   "1.000 veces más potencia de sonido.",
                ojo="una diferencia de 30 dB no es «un poco más»: es mil veces. Lee la escala antes que el número.",
                chequeo="Un parlante sube de 70 dB a 80 dB. ¿Cuántas veces más potencia? (10)",
                svg=fig_db),
        },
        vocab=[("Onda", "perturbación que viaja y lleva energía"),
               ("Frecuencia", "ondas por segundo, en hertz (Hz)"),
               ("Longitud de onda", "distancia entre dos crestas (λ)"),
               ("Amplitud", "qué tan alta es la cresta"),
               ("Medio", "por donde viaja la onda: aire, agua, sólido"),
               ("Refracción", "la onda se dobla al cambiar de medio"),
               ("Normal", "la línea perpendicular a la superficie"),
               ("Interferencia", "dos ondas que se suman o se anulan"),
               ("Decibel (dB)", "medida del sonido: +10 dB es ×10")]),
    5: dict(
        titulo="La energía que sube, corre y se escapa",
        centro=("Energía mecánica", "la suma de la energía de altura (potencial) y la de movimiento (cinética)",
                fig_c5),
        centro_ej="una manzana de 0,2 kg en una rama a 3 m tiene Ep = 0,2 · 10 · 3 = 6 J; justo antes de tocar el "
                  "suelo, esos 6 J son casi todos cinéticos.",
        centro_ojo="sin roce, la energía mecánica se conserva; con roce, una parte se vuelve calor.",
        centro_chequeo="Un balón quieto en una terraza, ¿tiene más energía potencial o cinética? (potencial)",
        ideas={
            "Cada magnitud con su fórmula y su unidad": dict(
                corto="Ep, Ec y W, en julios",
                d="Cada magnitud tiene su fórmula y su unidad: Ep = m · g · h y Ec = ½ · m · v², las dos en julios "
                  "(J), con la masa en kg, la altura en m y la rapidez en m/s. En la Tierra, g ≈ 10 m/s².",
                f="Ep = m · g · h   ·   Ec = ½ · m · v²",
                ej="una ciclista con su bicicleta (80 kg) a 5 m/s: Ec = ½ · 80 · 5² = 1.000 J.",
                ojo="la masa va en kg, no en gramos. Y el peso es una fuerza (en N), no una masa (en kg).",
                chequeo="Si la rapidez se duplica, ¿cuántas veces crece la energía cinética? (cuatro veces)",
                svg=fig_unidades),
            "¿Quién empuja y hacia dónde?": dict(
                corto="trabajo: fuerza a lo largo del camino",
                d="Una fuerza hace trabajo solo si el objeto se desplaza y ella empuja, al menos en parte, en esa "
                  "dirección. Si es perpendicular al movimiento o no hay desplazamiento, el trabajo es cero.",
                f="W = F · d · cos θ",
                ej="empujar un carrito de mercado 10 m con 30 N en la dirección del camino: W = 30 · 10 = 300 J.",
                ojo="cansarse no es hacer trabajo: empujar una pared que no se mueve da W = 0.",
                chequeo="Una fuerza forma 90° con el camino. ¿Cuánto trabajo hace? (cero: cos 90° = 0)",
                svg=fig_trabajo),
            "Una variable a la vez": dict(
                corto="una variable, lo demás fijo, repetir",
                d="Un procedimiento es confiable si cambia una sola variable, deja fijas las demás y repite cada "
                  "medida varias veces. Un solo ensayo puede salir así por casualidad.",
                f="1 variable · las demás fijas · varias repeticiones",
                ej="¿el largo de un péndulo cambia su periodo? Misma masa, mismo ángulo al soltar, solo cambia el "
                   "largo, y cada largo se mide cinco veces.",
                ojo="repetir no es cambiar otra cosa: se repite la misma prueba para ver si da lo mismo.",
                chequeo="Un solo ensayo dio que la canica pesada llegó primero. ¿Basta para concluir? (no: hay que repetir)",
                svg=fig_pendulo),
            "El principio que explica lo que se ve": dict(
                corto="nombrar el principio y mostrar cómo",
                d="Para explicar un fenómeno se nombra el principio que lo gobierna (conservación de la energía, "
                  "acción y reacción, inercia, presión del aire) y se muestra cómo produce lo que se ve.",
                f="fenómeno → ¿qué principio? → cómo lo produce",
                ej="un globo inflado que se suelta sale volando: empuja el aire hacia atrás y el aire lo empuja a él "
                   "hacia adelante (acción y reacción).",
                ojo="describir lo que pasa no es explicarlo: falta el nombre del principio y el porqué.",
                chequeo="¿Qué principio explica que un cohete avance en el espacio, sin aire en qué apoyarse? (acción y reacción)",
                svg=fig_globo),
        },
        vocab=[("Energía potencial", "energía por la altura: m · g · h"),
               ("Energía cinética", "energía por la rapidez: ½ · m · v²"),
               ("Energía mecánica", "potencial más cinética"),
               ("Julio (J)", "la unidad de energía y de trabajo"),
               ("Trabajo", "fuerza a lo largo de un desplazamiento"),
               ("Desplazamiento", "cuánto y hacia dónde se movió"),
               ("Momento", "masa por velocidad: p = m · v"),
               ("Presión atmosférica", "el empuje del aire sobre todo"),
               ("Principio", "regla de la física que explica fenómenos")]),
    6: dict(
        titulo="La energía que se transforma",
        centro=("Balance de energía", "la energía que entra es igual a la útil más la que se va como calor", fig_c6),
        centro_ej="un bombillo recibe 10 J cada segundo, da 4 J de luz y 6 J se van como calor: su eficiencia es "
                  "4 ÷ 10 = 40 %.",
        centro_ojo="ninguna máquina devuelve el 100 %: siempre algo se va como calor o ruido.",
        centro_chequeo="Entran 200 J y salen 150 J útiles. ¿Cuánto se fue como calor? (50 J)",
        ideas={
            "Multiplica, divide y lleva las unidades": dict(
                corto="E = P · t, con las unidades a la vista",
                d="Las cuentas de energía se hacen con las unidades a la vista: potencia por tiempo da energía "
                  "(W · s = J) y útil sobre entrada da eficiencia, sin unidades. Si las unidades no cuadran, la "
                  "cuenta está mal planteada.",
                f="E = P · t   ·   1 W = 1 J/s   ·   eficiencia = útil ÷ entrada",
                ej="una plancha de 1.000 W prendida 2 minutos: 2 min = 120 s, y 1.000 · 120 = 120.000 J.",
                ojo="los minutos y las horas se pasan a segundos antes de multiplicar por los vatios.",
                chequeo="Un bombillo de 60 W prendido 10 s, ¿cuánta energía usa? (600 J)",
                svg=fig_watts),
            "La energía no desaparece: cambia de forma": dict(
                corto="la cadena de transformaciones",
                d="En cada aparato la energía pasa de una forma a otra en cadena: química, eléctrica, de movimiento, "
                  "luz, calor. La que entra es igual a la suma de todas las que salen.",
                f="entrada = útil + calor + sonido",
                ej="una linterna: la energía química de la pila se vuelve eléctrica en el cable y sale del bombillo "
                   "como luz y como calor.",
                ojo="si en tu cuenta sobra o falta energía, te falta un eslabón: casi siempre, el calor.",
                chequeo="En un panel solar, ¿de qué forma a qué forma pasa la energía? (de luz a eléctrica, y una parte a calor)",
                svg=fig_cadena),
            "¿Alcanzan los datos para esa conclusión?": dict(
                corto="la conclusión no es más grande que los datos",
                d="Una conclusión no puede ser más grande que sus datos. Se pregunta: ¿cuántas medidas hay?, ¿en qué "
                  "condiciones?, ¿qué falta medir? Si falta algo, la conclusión queda abierta.",
                f="conclusión ≤ datos",
                ej="si una nevera nueva gastó menos que la vieja en una semana de diciembre, no sé si pasará todo el "
                   "año: falta medir con otro clima y otro uso.",
                ojo="«siempre», «nunca» y «el mejor» casi nunca caben en una sola medida.",
                chequeo="Con un solo día medido, ¿se sabe cuál panel rinde más en el año? (no: faltan días y estaciones)",
                svg=fig_puente),
            "Cuando algo deja de cambiar: el equilibrio": dict(
                corto="lo que entra iguala lo que sale",
                d="Un sistema llega al equilibrio cuando lo que entra iguala lo que sale: la temperatura, la rapidez "
                  "o el nivel dejan de cambiar. No es que todo se detenga: es que se compensa.",
                f="entra = sale   →   ya no cambia",
                ej="un tanque con la llave abierta y un hueco abajo sube hasta que sale tanta agua como entra; ahí el "
                   "nivel se queda quieto.",
                ojo="equilibrio no es quietud: el agua sigue entrando y saliendo, solo que se compensa.",
                chequeo="Un paracaidista cae a rapidez constante. ¿Qué fuerzas se compensan? (el peso y la resistencia del aire)",
                svg=fig_tanque),
        },
        vocab=[("Eficiencia", "útil ÷ entrada; nunca llega al 100 %"),
               ("Potencia", "energía por segundo"),
               ("Vatio (W)", "un julio cada segundo"),
               ("Energía útil", "la que sirve para lo que se quería"),
               ("Disipación", "energía que se va como calor o ruido"),
               ("Corriente", "carga que pasa por segundo, en amperios"),
               ("Resistencia", "lo que se opone al paso de la corriente"),
               ("Equilibrio", "lo que entra iguala lo que sale"),
               ("Curva de calentamiento", "temperatura contra tiempo al calentar")]),
}
