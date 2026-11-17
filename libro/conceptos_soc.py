"""Conceptualización de Sociales y Ciudadanas (ver conceptos.py y el modelo aprobado conceptos_mate.py).

Seis misiones: para cada una, la idea central, una tarjeta por estrategia (en los nombres exactos de
plan_soc.MISIONES[mis]["estr"]) y nueve palabras de vocabulario. Lo justo para comprender, sin teoría.

Fuentes: plan_soc.py (MISIONES: componente, estrategias, «instala» y «ojo»; TALLER: el contexto de
cada pregunta; SABERES, NO_ES_TU_FUERTE y ACTIVACION; el banco ICFES de tablero/icfes.csv) y
clase_viva_soc.py (TITULOS y LEADS). Los artículos citados son de la Constitución de 1991 y se
revisaron uno por uno: 4 (norma de normas), 16 (libre desarrollo de la personalidad), 23 (derecho de
petición), 29 (debido proceso y presunción de inocencia), 86 (tutela). La televisión llegó a
Colombia el 13 de junio de 1954.

Los ejemplos son PROPIOS: no repiten casos, datos ni opciones de las 10 preguntas del libro ni de las
4 de entrenamiento, ni el caso de la activación. Sin nombres propios de la política colombiana.

Prueba: python3 conceptos_area.py soc /tmp/claude-0/pc_soc
"""
from conceptos_figs import *  # noqa: F401,F403  (TINTA, GRIS, LINEA, colores, F, math)
from conceptos_figs import _svg, _t, _caja, _flecha, _tarjeta, _bien, _mal, _claro


# ═══════════════════════════════ piezas propias ═══════════════════════════════
def _persona(x, y, c, r=18, raya=False):
    """Cabeza en (x, y) y hombros debajo. raya=True: silueta punteada (el que falta)."""
    d = ' stroke-dasharray="6 5"' if raya else ""
    fondo = "#fff" if raya else _claro(c)
    return (f'<path d="M{x-r*1.6} {y+r*3.6} Q{x-r*1.5} {y+r*1.2} {x} {y+r*1.2} Q{x+r*1.5} {y+r*1.2} '
            f'{x+r*1.6} {y+r*3.6} Z" fill="{fondo}" stroke="{TINTA}" stroke-width="2.5"{d}/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{TINTA}" stroke-width="2.5"{d}/>')


def _casa(x, y, w, c, fondo="#fff"):
    """Casa: frente de w × 0,7w con la esquina superior izquierda en (x, y) y techo encima."""
    h = w * 0.7
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fondo}" stroke="{TINTA}" stroke-width="2.5"/>'
            f'<polygon points="{x-8},{y} {x+w/2},{y-w*0.5} {x+w+8},{y}" fill="{_claro(c)}" stroke="{TINTA}" stroke-width="2.5"/>'
            f'<rect x="{x+w*0.4}" y="{y+h*0.45}" width="{w*0.2}" height="{h*0.55}" fill="{_claro(c, .6)}" stroke="{TINTA}" stroke-width="2"/>')


# ═══════════════════════════════ misión 1 ═══════════════════════════════
def fig_constitucion(c):
    s = (_caja(110, 72, 190, 176, 30, "#fff", _claro(c, .6), _claro(c, .85))
         + f'<rect x="124" y="86" width="12" height="148" fill="{_claro(c, .5)}"/>'
         + _t(212, 142, "Constitución", 24, TINTA, "middle")
         + _t(212, 196, "1991", 38, c, "middle")
         + _t(210, 286, "la norma de normas", 20, TINTA, "middle"))
    return _svg(s, "El libro de la Constitución de 1991")


def fig_actores(c):
    s = ""
    for x in (80, 210, 340):
        s += (f'<rect x="{x-54}" y="30" width="108" height="44" rx="14" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x, 59, "qué dice", 19, TINTA, "middle", "600")
              + f'<line x1="{x}" y1="76" x2="{x}" y2="96" stroke="{TINTA}" stroke-width="2.5"/>'
              + _persona(x, 116, c, 17)
              + _tarjeta(x - 54, 198, 108, 40, "por qué", c, 19))
    return _svg(s, "Tres actores: cada uno dice algo y lo dice por un interés")


def fig_principio(c):
    s = (f'<line x1="112" y1="120" x2="112" y2="150" stroke="{TINTA}" stroke-width="5"/>'
         f'<rect x="30" y="64" width="164" height="56" rx="10" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(112, 100, "¡queremos…!", 21, TINTA, "middle")
         + _persona(112, 168, c, 16)
         + f'<rect x="250" y="56" width="110" height="20" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="2.5"/>'
         + f'<rect x="266" y="76" width="78" height="150" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + "".join(f'<line x1="{x}" y1="80" x2="{x}" y2="222" stroke="{LINEA}" stroke-width="3"/>' for x in (286, 305, 324))
         + f'<rect x="250" y="226" width="110" height="20" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="2.5"/>'
         + _flecha(200, 92, 244, 120, c, 4)
         + _t(305, 280, "el principio", 20, c, "middle"))
    return _svg(s, "Detrás de lo que pide la gente hay un principio, como una columna")


def fig_dimensiones(c):
    s = (_caja(20, 128, 112, 62, 20, "#fff", _claro(c, .6), _claro(c, .85))
         + _t(76, 166, "causa", 22, TINTA, "middle"))
    for k, (lab, col) in enumerate([("económico", AZUL), ("social", c), ("ambiental", VERDE)]):
        y = 34 + k * 88
        s += (_flecha(158, 158, 222, y + 26, GRIS, 3.5)
              + _tarjeta(228, y, 168, 52, lab, col, 21))
    return _svg(s, "Una causa con efectos en tres dimensiones: económica, social y ambiental")


def fig_linea_tiempo(c):
    s = (_flecha(30, 170, 396, 170, TINTA, 4)
         + f'<path d="M232 140 Q290 70 346 140" fill="none" stroke="{c}" stroke-width="4" stroke-dasharray="8 6"/>'
         + f'<path d="M346 140 L332 134 M346 140 L344 125" stroke="{c}" stroke-width="4" stroke-linecap="round"/>'
         + _t(289, 84, "explica", 20, c, "middle"))
    for x, anio, lab in ((80, "1886", "antes"), (228, "1991", "cambio"), (350, "hoy", "ahora")):
        s += (f'<circle cx="{x}" cy="170" r="11" fill="{c if anio == "1991" else "#fff"}" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x, 214, anio, 24, TINTA, "middle") + _t(x, 244, lab, 19, GRIS, "middle", "600"))
    return _svg(s, "Línea de tiempo: 1886, 1991 y hoy; lo de antes explica lo de ahora")


# ═══════════════════════════════ misión 2 ═══════════════════════════════
def fig_capas(c):
    s = (_caja(60, 64, 260, 62, 34, "#fff", _claro(c, .6), _claro(c, .85))
         + _t(190, 103, "qué propone", 22, TINTA, "middle")
         + f'<line x1="190" y1="132" x2="190" y2="164" stroke="{GRIS}" stroke-width="3" stroke-dasharray="5 5"/>'
         + _caja(60, 176, 260, 62, 34, _claro(c, .85), _claro(c, .55), _claro(c, .92))
         + _t(190, 215, "por qué lo propone", 22, c, "middle"))
    return _svg(s, "Dos capas: lo que alguien propone y la razón por la que lo propone")


def fig_venn(c):
    s = (f'<circle cx="160" cy="152" r="100" fill="{_claro(c)}" fill-opacity=".75" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<circle cx="262" cy="152" r="100" fill="{_claro(ORO)}" fill-opacity=".6" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(108, 158, "solo A", 20, TINTA, "middle") + _t(211, 158, "los dos", 20, c, "middle")
         + _t(314, 158, "solo B", 20, TINTA, "middle")
         + _t(84, 40, "actor A", 19, GRIS, "middle", "600") + _t(338, 40, "actor B", 19, GRIS, "middle", "600"))
    return _svg(s, "Dos círculos que se cruzan: en qué coinciden y en qué no dos actores")


def _llave(x, y, c):
    return (f'<circle cx="{x}" cy="{y}" r="16" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
            f'<path d="M{x+16} {y} L{x+90} {y} M{x+72} {y} L{x+72} {y+14} M{x+84} {y} L{x+84} {y+12}" '
            f'stroke="{c}" stroke-width="6" stroke-linecap="round"/>')


def fig_llaves(c):
    s = ""
    for k, lab in enumerate(["tutela", "petición", "revocatoria"]):
        y = 74 + k * 76
        s += _llave(40, y, c) + _t(146, y + 7, lab, 20, TINTA)
    s += (f'<path d="M306 150 L306 118 A30 30 0 0 1 366 118 L366 150" fill="none" stroke="{TINTA}" stroke-width="7"/>'
          f'<rect x="288" y="148" width="96" height="86" rx="12" fill="{_claro(c)}" stroke="{TINTA}" stroke-width="3"/>'
          f'<circle cx="336" cy="182" r="9" fill="{TINTA}"/><rect x="332" y="186" width="8" height="24" fill="{TINTA}"/>'
          + _t(336, 270, "¿cuál abre?", 20, c, "middle"))
    return _svg(s, "Tres llaves con nombre y un candado: cada figura sirve para algo distinto")


def fig_moneda(c):
    s = ""
    for cx, signo, lab, col in ((120, "+", "a quién beneficia", VERDE), (300, "−", "a quién le cuesta", ROJO)):
        s += (f'<ellipse cx="{cx+8}" cy="122" rx="72" ry="72" fill="{_claro(ORO, .5)}" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<circle cx="{cx}" cy="118" r="72" fill="{_claro(ORO, .8)}" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<circle cx="{cx}" cy="118" r="56" fill="none" stroke="{ORO}" stroke-width="2"/>'
              + _t(cx, 140, signo, 64, col, "middle")
              + _t(cx, 226, lab, 19, TINTA, "middle", "600"))
    s += _t(210, 278, "hoy y mañana", 21, c, "middle")
    return _svg(s, "Las dos caras de una moneda: a quién beneficia y a quién le cuesta")


def fig_entredicho(c):
    s = (f'<rect x="50" y="36" width="210" height="226" rx="10" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(155, 76, "lo prometido", 22, TINTA, "middle"))
    for k in range(5):
        y = 108 + k * 28
        s += f'<line x1="72" y1="{y}" x2="{238 if k < 4 else 180}" y2="{y}" stroke="{LINEA}" stroke-width="6" stroke-linecap="round"/>'
    s += (f'<g transform="rotate(-12 310 170)"><circle cx="310" cy="170" r="62" fill="#fff" fill-opacity=".85" '
          f'stroke="{c}" stroke-width="6"/><circle cx="310" cy="170" r="50" fill="none" stroke="{c}" stroke-width="2"/>'
          + _t(310, 192, "?", 64, c, "middle") + '</g>')
    return _svg(s, "Un documento con lo prometido y un sello de duda encima")


# ═══════════════════════════════ misión 3 ═══════════════════════════════
def fig_decision(c):
    s = (_caja(140, 46, 140, 58, 26, "#fff", _claro(c, .6), _claro(c, .85))
         + _t(210, 83, "decisión", 22, TINTA, "middle"))
    for k in range(5):
        x = 50 + k * 80
        s += _flecha(210, 112, x, 168, GRIS, 3) + _persona(x, 190, c, 14)
    return _svg(s, "Una decisión que llega a muchas personas distintas")


def fig_preocupaciones(c):
    s = ""
    for k, lab in enumerate(["sustento", "tiempo", "orden"]):
        x = 80 + k * 130
        s += (f'<circle cx="{x}" cy="112" r="54" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x, 206, lab, 21, TINTA, "middle"))
    s += _t(80, 132, "$", 52, c, "middle")
    s += (f'<circle cx="210" cy="112" r="30" fill="#fff" stroke="{c}" stroke-width="4"/>'
          f'<path d="M210 112 L210 92 M210 112 L226 120" stroke="{TINTA}" stroke-width="4" stroke-linecap="round"/>')
    s += (f'<path d="M340 78 L370 90 Q370 132 340 146 Q310 132 310 90 Z" fill="#fff" stroke="{c}" stroke-width="4"/>')
    s += _t(210, 262, "cada quien mira desde lo suyo", 19, GRIS, "middle", "600")
    return _svg(s, "Tres preocupaciones: el sustento, el tiempo y el orden")


def fig_balanza(c):
    s = (f'<line x1="210" y1="64" x2="210" y2="240" stroke="{TINTA}" stroke-width="6"/>'
         f'<polygon points="160,252 260,252 236,238 184,238" fill="{_claro(c)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="80" y1="80" x2="340" y2="80" stroke="{TINTA}" stroke-width="6" stroke-linecap="round"/>'
         f'<circle cx="210" cy="80" r="9" fill="{c}"/>')
    for x, lab, col in ((80, "ganan", VERDE), (340, "pagan", ROJO)):
        s += (f'<line x1="{x}" y1="80" x2="{x-50}" y2="150" stroke="{TINTA}" stroke-width="2"/>'
              f'<line x1="{x}" y1="80" x2="{x+50}" y2="150" stroke="{TINTA}" stroke-width="2"/>'
              f'<path d="M{x-62} 150 L{x+62} 150 Q{x} 196 {x-62} 150 Z" fill="{_claro(col)}" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x, 222, lab, 22, col, "middle"))
    return _svg(s, "Una balanza: en un platillo los que ganan y en el otro los que pagan")


def fig_cuerda(c):
    s = (f'<path d="M40 150 Q80 140 120 150 T200 150 T280 150 T380 150" fill="none" stroke="{ORO}" stroke-width="9" stroke-linecap="round"/>'
         f'<circle cx="210" cy="150" r="14" fill="{c}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="210" y1="176" x2="210" y2="226" stroke="{GRIS}" stroke-width="3" stroke-dasharray="6 5"/>'
         + _flecha(70, 112, 24, 112, c, 5) + _flecha(350, 112, 396, 112, c, 5)
         + _tarjeta(30, 176, 130, 46, "derecho A", c, 20) + _tarjeta(260, 176, 130, 46, "derecho B", c, 20)
         + _t(210, 254, "ponderar", 22, TINTA, "middle"))
    return _svg(s, "Una cuerda tensada entre dos derechos; en el medio se pondera")


def fig_pueblos(c):
    s = (_casa(30, 120, 96, c) + _casa(196, 140, 70, c) + _casa(330, 160, 50, c)
         + _flecha(140, 180, 182, 180, c, 4) + _flecha(282, 186, 318, 186, c, 4)
         + _t(78, 222, "aquí", 21, TINTA, "middle") + _t(231, 222, "al lado", 21, TINTA, "middle")
         + _t(355, 222, "lejos", 21, TINTA, "middle")
         + _t(210, 270, "sigue la medida hasta donde llega", 19, GRIS, "middle", "600"))
    return _svg(s, "Tres casas, cada una más lejos: el efecto viaja")


# ═══════════════════════════════ misión 4 ═══════════════════════════════
def fig_hecho(c):
    s = (_caja(150, 112, 120, 70, 26, "#fff", _claro(c, .6), _claro(c, .85))
         + _t(210, 155, "hecho", 24, TINTA, "middle")
         + _flecha(30, 150, 140, 150, GRIS, 4) + _flecha(300, 150, 400, 150, c, 4)
         + _t(84, 136, "antes", 20, GRIS, "middle") + _t(350, 136, "después", 20, c, "middle")
         + _persona(176, 40, c, 12) + _persona(240, 40, ORO, 12)
         + _t(210, 240, "¿a quién le pasó?", 20, TINTA, "middle"))
    return _svg(s, "Un hecho con lo que venía de antes, lo que vino después y la gente que lo vivió")


def fig_prisma(c):
    s = (f'<line x1="20" y1="172" x2="182" y2="152" stroke="{TINTA}" stroke-width="6" stroke-linecap="round"/>'
         f'<polygon points="140,236 206,70 272,236" fill="#fff" fill-opacity=".9" stroke="{TINTA}" stroke-width="3"/>')
    for k, (lab, col) in enumerate([("político", c), ("económico", ORO), ("social", VERDE), ("cultural", ROJO)]):
        y = 56 + k * 58
        s += (f'<line x1="236" y1="150" x2="300" y2="{y}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>'
              + _t(306, y + 7, lab, 20, TINTA))
    s += _t(80, 260, "un hecho", 20, GRIS, "middle", "600")
    return _svg(s, "Un prisma abre un hecho en cuatro dimensiones")


def _ojo(x, y, c):
    return (f'<path d="M{x-30} {y} Q{x} {y-24} {x+30} {y} Q{x} {y+24} {x-30} {y} Z" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
            f'<circle cx="{x}" cy="{y}" r="10" fill="{c}"/>')


def fig_ojos(c):
    s = (f'<polygon points="96,74 180,128 180,186" fill="{_claro(c)}" opacity=".8"/>'
         f'<polygon points="324,226 256,176 256,128" fill="{_claro(ORO)}" opacity=".8"/>'
         + _caja(180, 128, 72, 58, 20, "#fff", _claro(c, .6), _claro(c, .85))
         + _ojo(66, 70, c) + _ojo(354, 230, ORO)
         + _t(66, 118, "un testigo", 19, TINTA, "middle", "600")
         + _t(354, 278, "otro testigo", 19, TINTA, "middle", "600")
         + _t(226, 228, "el hecho", 19, TINTA, "middle"))
    return _svg(s, "Dos testigos miran el mismo hecho desde lugares distintos")


def fig_antes_despues(c):
    s = (f'<rect x="24" y="44" width="176" height="166" rx="12" fill="#E3E7EF" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="220" y="44" width="176" height="166" rx="12" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + _casa(80, 130, 64, c, "#C8CEDA") + _casa(276, 130, 64, c, "#FFF7DD")
         + f'<circle cx="366" cy="84" r="14" fill="{ORO}"/>'
         + "".join(f'<line x1="{366 + 22*math.cos(a)}" y1="{84 + 22*math.sin(a)}" x2="{366 + 32*math.cos(a)}" '
                   f'y2="{84 + 32*math.sin(a)}" stroke="{ORO}" stroke-width="3" stroke-linecap="round"/>'
                   for a in [k * math.pi / 4 for k in range(8)])
         + _t(112, 248, "antes", 22, GRIS, "middle") + _t(308, 248, "después", 22, c, "middle"))
    return _svg(s, "La misma casa antes y después: algo cambió en la vida de la gente")


def fig_arbol(c):
    s = (f'<path d="M210 212 Q200 250 140 272 M210 212 L210 280 M210 212 Q222 250 282 272" fill="none" '
         f'stroke="{TINTA}" stroke-width="4" stroke-linecap="round"/>'
         f'<line x1="40" y1="212" x2="380" y2="212" stroke="{LINEA}" stroke-width="3"/>'
         f'<rect x="196" y="118" width="28" height="94" fill="#E9DCC6" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<ellipse cx="210" cy="86" rx="132" ry="56" fill="{_claro(VERDE)}" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(210, 94, "consecuencias", 22, TINTA, "middle")
         + _t(300, 256, "causas", 21, c))
    return _svg(s, "Un árbol: las raíces son las causas y la copa, las consecuencias")


# ═══════════════════════════════ misión 5 ═══════════════════════════════
def fig_territorio(c):
    s = (f'<polygon points="30,150 210,76 390,150 210,226" fill="{_claro(VERDE, .85)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="210,226 390,150 390,166 210,242 30,166 30,150" fill="{_claro(VERDE, .55)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="100,140 132,84 164,140" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="140,128 170,78 200,128" fill="#EEF2F8" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M232 84 Q250 130 210 150 T238 222" fill="none" stroke="{AZUL}" stroke-width="6" stroke-linecap="round"/>'
         + _casa(286, 138, 26, c) + _casa(320, 152, 22, c)
         + _t(210, 284, "gente · recursos · reglas", 20, TINTA, "middle"))
    return _svg(s, "Un pedazo de territorio con montañas, un río y casas")


def fig_mapa(c):
    s = (f'<rect x="30" y="30" width="360" height="226" rx="12" fill="#F5FAF6" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="50,130 86,66 122,130" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="96,130 130,76 164,130" fill="#EEF2F8" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M370 40 Q300 110 330 170 T290 250" fill="none" stroke="{AZUL}" stroke-width="7" stroke-linecap="round"/>'
         f'<path d="M40 200 L380 160" stroke="{GRIS}" stroke-width="7" stroke-dasharray="16 8"/>'
         f'<path d="M232 176 C212 150 212 124 232 120 C252 124 252 150 232 176 Z" fill="{c}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<circle cx="232" cy="138" r="7" fill="#fff"/>'
         + _t(106, 160, "relieve", 19, TINTA, "middle") + _t(326, 66, "río", 20, AZUL, "end")
         + _t(90, 236, "vía", 19, GRIS))
    return _svg(s, "Un mapa con montañas, río, vía y un punto marcado")


def fig_falta(c):
    s = ""
    for k in range(3):
        s += _persona(70 + k * 90, 104, c, 22)
    s += (_persona(340, 104, c, 22, raya=True) + _t(340, 112, "?", 26, c, "middle")
          + _t(210, 250, "¿quién falta?", 22, c, "middle"))
    return _svg(s, "Tres actores y un cuarto punteado: el que nadie nombra")


def fig_domino(c):
    s = f'<line x1="30" y1="232" x2="390" y2="232" stroke="{LINEA}" stroke-width="3"/>'
    for k, ang in enumerate([52, 38, 22, 8, 0]):
        x = 64 + k * 66
        s += (f'<g transform="rotate({ang} {x + 30} 232)"><rect x="{x}" y="122" width="30" height="110" rx="5" '
              f'fill="{_claro(c) if k == 0 else "#fff"}" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<line x1="{x+4}" y1="177" x2="{x+26}" y2="177" stroke="{TINTA}" stroke-width="2"/>'
              f'<circle cx="{x+15}" cy="150" r="4" fill="{TINTA}"/><circle cx="{x+15}" cy="204" r="4" fill="{TINTA}"/></g>')
    s += (_flecha(80, 60, 340, 60, c, 4)
          + _t(76, 270, "medida", 20, c, "middle") + _t(338, 270, "efecto 4", 20, TINTA, "middle"))
    return _svg(s, "Fichas de dominó que caen una tras otra: una medida y sus efectos")


def fig_discurso(c):
    s = (f'<rect x="40" y="26" width="340" height="84" rx="18" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="110,106 96,140 146,108" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="43" y="29" width="334" height="78" rx="16" fill="#fff"/>'
         + _t(210, 78, f'es puro <tspan fill="{c}">«progreso»</tspan>', 26, TINTA, "middle")
         + _flecha(218, 120, 218, 166, c, 4)
         + f'<rect x="110" y="172" width="216" height="68" rx="12" fill="#fff" stroke="{c}" stroke-width="3" stroke-dasharray="9 6"/>'
         + _t(218, 215, "¿qué busca?", 24, c, "middle"))
    return _svg(s, "Una frase con una palabra con carga y, debajo, lo que busca quien la dice")


# ═══════════════════════════════ misión 6 ═══════════════════════════════
def fig_pedestal(c):
    s = (f'<rect x="90" y="140" width="240" height="22" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="114" y="162" width="44" height="92" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="262" y="162" width="44" height="92" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="178" y="56" width="64" height="62" rx="6" fill="{_claro(ORO, .6)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="168" y="114" width="84" height="18" rx="4" fill="{_claro(ORO, .4)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="178" y1="132" x2="178" y2="140" stroke="{TINTA}" stroke-width="4"/>'
         f'<line x1="242" y1="132" x2="242" y2="140" stroke="{TINTA}" stroke-width="4"/>'
         + _t(136, 284, "ley", 21, c, "middle") + _t(284, 284, "derechos", 21, c, "middle")
         + _t(262, 92, "poder", 20, TINTA))
    return _svg(s, "La silla del poder apoyada en dos columnas: la ley y los derechos")


def fig_mayoria(c):
    s = ""
    for i in range(5):
        for j in range(4):
            s += f'<circle cx="{40 + i*28}" cy="{90 + j*28}" r="10" fill="{_claro(c, .5)}" stroke="{TINTA}" stroke-width="1.5"/>'
    for x, y in ((336, 118), (366, 118), (351, 146)):
        s += f'<circle cx="{x}" cy="{y}" r="10" fill="{_claro(ORO, .4)}" stroke="{TINTA}" stroke-width="1.5"/>'
    s += (f'<path d="M260 70 L296 84 Q296 150 260 176 Q224 150 224 84 Z" fill="#fff" stroke="{c}" stroke-width="5"/>'
          + _bien(248, 120, c)
          + _t(96, 236, "mayoría", 21, TINTA, "middle") + _t(351, 236, "minoría", 21, TINTA, "middle")
          + _t(260, 210, "derechos", 20, c, "middle"))
    return _svg(s, "Una mayoría grande, una minoría pequeña y un escudo de derechos en medio")


def fig_medidores(c):
    s = ""
    for cx, ang, lab, col in ((110, -25, "eficaz", VERDE), (310, -155, "legítimo", ROJO)):
        a = math.radians(ang)
        s += (f'<path d="M{cx-80} 180 A80 80 0 0 1 {cx+80} 180" fill="{_claro(c, .9)}" stroke="{TINTA}" stroke-width="3"/>'
              f'<line x1="{cx}" y1="180" x2="{cx + 64*math.cos(a):.1f}" y2="{180 + 64*math.sin(a):.1f}" '
              f'stroke="{col}" stroke-width="6" stroke-linecap="round"/>'
              f'<circle cx="{cx}" cy="180" r="8" fill="{TINTA}"/>'
              + _t(cx, 220, lab, 22, TINTA, "middle"))
    s += _t(210, 272, "no siempre van juntos", 20, c, "middle")
    return _svg(s, "Dos medidores: alto en eficaz, bajo en legítimo")


def fig_planos(c):
    s = ""
    for k, (lab, col) in enumerate([("político", c), ("social", ORO), ("ético", VERDE)]):
        y = 66 + k * 72
        s += (f'<polygon points="60,{y+30} 160,{y-14} 360,{y-14} 260,{y+30}" fill="{_claro(col, .78)}" '
              f'stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(210, y + 15, lab, 22, TINTA, "middle"))
    return _svg(s, "Tres planos apilados: político, social y ético")


def fig_medallas(c):
    """Cada voz levanta la bandera de su principio."""
    s = ""
    for x, lab in ((36, "legalidad"), (158, "igualdad"), (280, "libertad")):
        p = x + 30
        s += (f'<line x1="{p}" y1="36" x2="{p}" y2="196" stroke="{TINTA}" stroke-width="4"/>'
              f'<path d="M{p} 40 L{p+100} 40 Q{p+88} 62 {p+100} 84 L{p} 84 Z" fill="{_claro(c, .85)}" '
              f'stroke="{c}" stroke-width="3"/>'
              + _t(p + 45, 68, lab, 18, TINTA, "middle")
              + _persona(x, 150, c, 16))
    s += _t(210, 276, "cada voz, su principio", 20, TINTA, "middle")
    return _svg(s, "Tres personas, cada una con la bandera de su principio")


# ═══════════════════════════════ los datos ═══════════════════════════════
DATOS = {
 1: dict(
    titulo="Leer un caso, no opinar de él",
    centro=("La Constitución de 1991", "la norma de normas: dice cómo se organiza el Estado y qué derechos tenemos",
            fig_constitucion),
    centro_ej="si un colegio sanciona a un estudiante sin escucharlo, la pregunta no es si te parece justo: "
              "es qué dice la Constitución (el debido proceso, art. 29).",
    centro_ojo="opinar sobre el caso antes de leerlo con la Constitución en la mano.",
    centro_chequeo="¿Qué pesa más: el manual de convivencia o la Constitución? (la Constitución: es norma de normas, art. 4)",
    ideas={
        "Quién dice qué y por qué": dict(
            corto="actores, posturas e intereses",
            d="En todo caso hay actores: personas, grupos, instituciones. Cada uno dice algo (su postura) "
              "y lo dice por algo (su interés). Separar las tres cosas evita escoger la opción que más "
              "nos gusta.",
            f="actor → qué dice → por qué lo dice",
            ej="un barrio pide un semáforo: los padres quieren seguridad para los niños, los comerciantes "
               "temen perder parqueo y la alcaldía mira el presupuesto.",
            ojo="ponerle a un actor la frase de otro. Antes de marcar, pregunta: ¿de quién es esta "
                "frase en el caso?",
            chequeo="Un taxista se opone a una ciclorruta. ¿Cuál puede ser su interés? (no perder carriles ni tiempo)",
            svg=fig_actores),
        "El principio que hay detrás": dict(
            corto="el principio de la Constitución en juego",
            d="Detrás de lo que pide la gente casi siempre hay un principio de la Constitución: igualdad, "
              "participación, dignidad, libre desarrollo de la personalidad, debido proceso. Mira qué "
              "piden, no de qué tema es el caso.",
            f="lo que piden → el principio que lo respalda",
            ej="un estudiante pide ir al colegio con el pelo largo. No pide un favor: el principio "
               "detrás es el libre desarrollo de la personalidad (art. 16).",
            ojo="escoger el principio por el tema («es de salud, entonces es el derecho a la salud»). "
                "Mira qué se está pidiendo.",
            chequeo="Despiden a un trabajador sin dejarlo explicarse. ¿Qué principio se toca? (el debido proceso)",
            svg=fig_principio),
        "Si pasa esto, qué pasa después": dict(
            corto="consecuencias en varias dimensiones",
            d="Toda medida trae efectos, y no en un solo campo: económicos, sociales, ambientales, "
              "políticos. Un efecto bien dicho empieza en la causa que te dan y nombra a quién le llega.",
            f="causa → efecto económico + social + ambiental",
            ej="si sube el pasaje del bus: a las familias les queda menos plata (económico) y más gente "
               "camina o anda en bici (social y ambiental).",
            ojo="quedarse en una sola dimensión cuando la pregunta pide dos, o dar un efecto que no sale "
                "de la causa del caso.",
            chequeo="Cierra la única fábrica de un pueblo. Di un efecto económico y uno social. (desempleo; familias que se van)",
            svg=fig_dimensiones),
        "Lo de antes explica lo de ahora": dict(
            corto="el contexto histórico explica el presente",
            d="Un hecho de hoy se entiende mejor si se mira qué pasaba antes: qué crisis, qué norma, qué "
              "conflicto. Para comparar dos momentos se escribe el argumento de cada uno y se mira qué "
              "se repite.",
            f="antes (contexto) → hecho → ahora",
            ej="la tutela existe desde la Constitución de 1991 (art. 86). Antes no había un camino tan "
               "rápido para reclamar un derecho; por eso hoy la usa tanta gente.",
            ojo="creer que el pasado son solo fechas. Lo que importa es la razón de entonces y si se "
                "parece a la de ahora.",
            chequeo="¿Qué Constitución rigió en Colombia antes de la de 1991? (la de 1886)",
            svg=fig_linea_tiempo),
    },
    vocab=[("Constitución", "la norma más alta del país"),
           ("Estado social de derecho", "el poder sometido a la ley, para dar derechos"),
           ("Derecho fundamental", "derecho básico que se protege con tutela"),
           ("Tutela", "acción para proteger rápido un derecho"),
           ("Actor", "persona, grupo o entidad que participa"),
           ("Interés", "lo que alguien busca o quiere proteger"),
           ("Principio", "valor de la Constitución que guía una decisión"),
           ("Consecuencia", "lo que pasa por causa de algo"),
           ("Contexto", "lo que pasaba alrededor y antes del hecho")]),

 2: dict(
    titulo="Coincidir en qué, diferir en por qué",
    centro=("Postura y razón", "lo que alguien propone y por qué lo propone son dos cosas distintas", fig_capas),
    centro_ej="dos vecinos piden cerrar la calle los domingos: uno para que los niños jueguen, el otro "
              "para vender comida. Coinciden en la propuesta, no en la razón.",
    centro_ojo="creer que si dos actores proponen lo mismo, piensan igual.",
    centro_chequeo="Dos personas quieren menos carros en el centro: una por el aire, otra por los trancones. ¿En qué coinciden? (en la propuesta)",
    ideas={
        "En qué coinciden y en qué no": dict(
            corto="comparar propuesta y razón",
            d="Se comparan dos actores en dos niveles: qué proponen y por qué. Pueden coincidir en lo que "
              "proponen y diferir en la razón, o al revés. Un buen acuerdo le deja algo a cada lado.",
            f="propuesta: ¿igual o distinta? · razón: ¿igual o distinta?",
            ej="un grupo quiere prohibir la pólvora por los niños quemados; otro, solo regularla, por los "
               "que viven de venderla. Los dos ven el riesgo; difieren en la medida.",
            ojo="mirar solo el bando (a favor o en contra) y no la clase de razón: económica, ética, de "
                "salud o cultural.",
            chequeo="A favor del uniforme: uno dice «iguala», otro «sale barato». ¿Coinciden en la razón? (no: social vs. económica)",
            svg=fig_venn),
        "El nombre exacto de la figura": dict(
            corto="el mecanismo o la entidad exacta",
            d="Cada figura de la Constitución decide una cosa distinta. Tutela: protege ya un derecho "
              "fundamental. Derecho de petición: obliga a una entidad a responder. Consulta popular: el "
              "pueblo decide una pregunta. Revocatoria: retira a un alcalde o gobernador.",
            f="¿qué se decide? → un derecho · una respuesta · un mandato",
            ej="si una EPS no entrega un medicamento urgente, no se recogen firmas ni se pide una "
               "consulta popular: se pone una tutela.",
            ojo="confundir figuras que suenan parecido: referendo no es plebiscito, ni Procuraduría es "
                "Defensoría. Primero di qué se decide.",
            chequeo="Le escribes a la alcaldía para que te diga por qué no arreglan el parque. ¿Qué usas? (el derecho de petición)",
            svg=fig_llaves),
        "Las dos caras de la misma medida": dict(
            corto="beneficios y costos, hoy y mañana",
            d="Una medida pública casi nunca es solo buena o solo mala: beneficia a unos y le cuesta a "
              "otros, y puede cambiar de signo con el tiempo: ganar hoy y perder mañana, o al revés.",
            f="medida → beneficia a… / le cuesta a… · hoy / mañana",
            ej="volver peatonal una calle comercial: más gente camina y compra, pero los primeros meses "
               "los negocios que vivían del parqueo pierden clientes.",
            ojo="ver una sola cara, o creer que el efecto de hoy será el mismo dentro de cinco años.",
            chequeo="Talar un bosque para sembrar: ¿qué se gana hoy y qué se pierde mañana? (tierra y cosecha; agua y suelo)",
            svg=fig_moneda),
        "Qué queda en entredicho": dict(
            corto="el deber o la promesa que queda en duda",
            d="Cuando un hecho choca con lo que una institución dice o debe hacer, algo queda en duda: "
              "un deber del Estado, una promesa, la confianza. Se escribe primero el deber y después se "
              "mira si los hechos lo cumplen.",
            f="lo que debía pasar vs. lo que pasó = lo que queda en duda",
            ej="una alcaldía promete agua potable para todas las veredas y tres siguen con carrotanque: "
               "queda en duda que cumpla su deber de prestar ese servicio.",
            ojo="confundir lo que dice la institución con lo que hace. La frase bonita no prueba nada si "
                "los hechos la contradicen.",
            chequeo="Un colegio dice «aquí se escucha a todos» y no deja hablar al personero. ¿Qué queda en duda? (la participación)",
            svg=fig_entredicho),
    },
    vocab=[("Postura", "lo que alguien defiende o propone"),
           ("Consenso", "acuerdo entre todos o casi todos"),
           ("Disenso", "desacuerdo con una postura"),
           ("Tutela", "protege rápido un derecho fundamental"),
           ("Derecho de petición", "obliga a una entidad a responder"),
           ("Referendo", "el pueblo aprueba o deroga una norma"),
           ("Plebiscito", "el pueblo apoya o rechaza una decisión"),
           ("Revocatoria", "retira a un alcalde o gobernador"),
           ("Defensoría del Pueblo", "defiende los derechos humanos")]),

 3: dict(
    titulo="Cuatro preguntas a una decisión",
    centro=("Decisión pública", "una medida de una autoridad que le llega a mucha gente, para bien y para mal",
            fig_decision),
    centro_ej="un colegio pasa la jornada a la mañana: unos padres llegan a tiempo al trabajo, otros no "
              "tienen con quién dejar al hermano menor y el bus cambia de ruta.",
    centro_ojo="juzgar la medida por cómo te afecta a ti. El análisis mira a todos los afectados.",
    centro_chequeo="¿Cuántas preguntas le hacemos hoy a cada caso? (cuatro: voces, ganadores y perdedores, derecho, efecto lejano)",
    ideas={
        "Cada voz, su preocupación": dict(
            corto="qué le preocupa a cada actor",
            d="Cada actor mira el mismo caso desde su preocupación: el que vive de algo teme perderlo, el "
              "que decide mira el orden o el presupuesto, el que usa el servicio piensa en su acceso. "
              "«No quiere» no es lo mismo que «no puede».",
            f="actor → su preocupación → ¿no quiere o no puede?",
            ej="un parque va a cerrar a las 6 p. m.: los vecinos piensan en el ruido, los que trotan "
               "en su horario y la policía en la seguridad.",
            ojo="poner en boca de un actor la preocupación de otro. Cada frase tiene dueño.",
            chequeo="Una tienda deja de fiar. ¿No quiere o no puede? ¿Cómo lo sabes? (por la razón que da)",
            svg=fig_preocupaciones),
        "Quién gana y quién paga": dict(
            corto="beneficios y costos por actor",
            d="Toda decisión reparte: a unos les deja ganancias y a otros les cobra. El análisis completo "
              "pone cada efecto en su platillo y dice a quién le toca. La conclusión más completa nombra "
              "los dos lados.",
            f="decisión → ganan: ___ · pagan: ___",
            ej="un festival en el estadio: ganan hoteles, restaurantes y la ciudad que recauda; pagan "
               "los vecinos con ruido, calles cerradas y basura.",
            ojo="quedarse con un solo platillo: la opción que solo habla de beneficios, o solo de costos, "
                "se queda corta.",
            chequeo="Sube el parqueadero en el centro. ¿Quién gana y quién paga? (gana el transporte público; pagan los que van en carro)",
            svg=fig_balanza),
        "El derecho que se pone en tensión": dict(
            corto="dos derechos que chocan",
            d="A veces una decisión protege un derecho y toca otro: el espacio público frente al "
              "trabajo, la seguridad frente a la intimidad. Ninguno gana siempre: se busca la medida que "
              "proteja uno sacrificando lo menos posible del otro.",
            f="derecho A vs. derecho B → ponderar",
            ej="un concierto a medianoche: la recreación de los asistentes choca con la tranquilidad y "
               "el descanso de los vecinos.",
            ojo="decir que uno de los dos derechos «no aplica». Los dos son derechos; la pregunta es cómo "
                "se equilibran.",
            chequeo="Un colegio revisa los bolsos a la entrada. ¿Qué derechos chocan? (la seguridad y la intimidad)",
            svg=fig_cuerda),
        "El efecto que llega a otra parte": dict(
            corto="efectos que viajan lejos",
            d="Una decisión tomada en un lugar produce efectos en otros lugares y en actores que no "
              "estaban en la mesa: otro barrio, otro sector, otro país. Hay que seguir la medida hasta "
              "donde llega.",
            f="aquí → al lado → más lejos",
            ej="si una ciudad prohíbe las motos de noche, los repartidores pierden turnos, los "
               "restaurantes venden menos domicilios y las motos se van a los municipios vecinos.",
            ojo="quedarse en el efecto inmediato. Estas preguntas premian el efecto que nadie vio venir.",
            chequeo="Una fábrica bota residuos al río arriba del pueblo. ¿A quién le llega abajo? (pescadores, agricultores, acueductos)",
            svg=fig_pueblos),
    },
    vocab=[("Decisión pública", "medida de una autoridad para muchos"),
           ("Afectado", "a quien le llega una decisión"),
           ("Beneficio", "lo que alguien gana con una medida"),
           ("Costo", "lo que alguien pierde o paga"),
           ("Mínimo vital", "lo que se necesita hoy para vivir digno"),
           ("Espacio público", "calles, parques y plazas de todos"),
           ("Ponderar", "pesar dos derechos para equilibrarlos"),
           ("Efecto indirecto", "el que llega a quien no estaba en el caso"),
           ("Soberanía", "cada país decide sus propios asuntos")]),

 4: dict(
    titulo="El pasado tiene muchas voces",
    centro=("El hecho histórico", "algo que pasó: tiene causas, lo vivió gente distinta y dejó huellas",
            fig_hecho),
    centro_ej="la llegada del tren a un pueblo tuvo causas (sacar la cosecha), actores (comerciantes, "
              "arrieros) y consecuencias (nuevos negocios, menos trabajo para los arrieros).",
    centro_ojo="creer que la historia es una lista de fechas. La fecha ubica; lo que se pregunta es por "
               "qué pasó y a quién le pasó.",
    centro_chequeo="¿Qué tres cosas se le preguntan a un hecho histórico? (sus causas, sus actores y sus consecuencias)",
    ideas={
        "Un hecho, varias dimensiones": dict(
            corto="política, economía, sociedad y cultura",
            d="Un mismo hecho tiene varias capas: política (quién manda), económica (qué se gana o se "
              "pierde), social (qué le pasa a la gente) y cultural (qué cambia en las costumbres y la "
              "identidad). Responde la capa que te preguntan.",
            f="hecho → político · económico · social · cultural",
            ej="la televisión llegó a Colombia en 1954: el gobierno la usó para hablarle al país "
               "(político), nació una industria (económico) y las familias se juntaron frente a la "
               "pantalla (cultural).",
            ojo="quedarse con la dimensión más obvia. Si preguntan por lo social, la respuesta habla de la "
                "gente, no de la plata.",
            chequeo="Cierra la fábrica y el pueblo pierde su fiesta anual. ¿Qué dimensiones aparecen? (económica y cultural)",
            svg=fig_prisma),
        "Quién lo mira y desde dónde": dict(
            corto="perspectivas y fuentes",
            d="El mismo hecho se cuenta distinto según quién lo vivió y desde dónde: el que ganó, el que "
              "perdió, el que lo vio de lejos. Ninguna fuente lo dice todo: se contrastan y se pregunta "
              "qué pudo ver cada una.",
            f="fuente → quién es · dónde estaba · qué pudo ver",
            ej="una huelga contada por el dueño de la fábrica, por un obrero y por un periódico de otra "
               "ciudad da tres relatos distintos de los mismos días.",
            ojo="creer que si dos testimonios no coinciden, uno miente. Puede que cada uno haya visto "
                "una parte.",
            chequeo="¿Por qué un diario personal y un informe del gobierno cuentan distinto el mismo día? (quién escribe y para qué)",
            svg=fig_ojos),
        "Lo que el hecho le hizo a la gente": dict(
            corto="el impacto en la vida de las personas",
            d="Detrás de cada hecho hay vidas que cambian: familias que se van, oficios que se pierden, "
              "derechos que se ganan. La pregunta es qué se rompió o qué cambió en la gente, no solo qué "
              "pasó.",
            f="hecho → ¿qué ganó o perdió la gente? → ¿qué cambió en su vida?",
            ej="cuando llegó la luz eléctrica a una vereda, los niños pudieron estudiar de noche, abrió "
               "una tienda con nevera y la radio empezó a traer noticias.",
            ojo="contar el hecho y olvidar a las personas. Si preguntan por lo social, la respuesta "
                "habla de gente concreta.",
            chequeo="Deja de pasar el tren por un pueblo. Di un cambio en la vida de la gente. (se aíslan, pierden empleo o se van)",
            svg=fig_antes_despues),
        "De dónde viene y hasta dónde llega": dict(
            corto="causas de antes, efectos de después",
            d="Un hecho tiene raíces que vienen de antes (causas, a veces de años atrás) y ramas que "
              "llegan lejos (consecuencias, a veces en otros países). Casi nunca hay una sola causa: se "
              "buscan varias y se ordenan en el tiempo.",
            f="raíces (causas) → hecho → ramas (consecuencias)",
            ej="una cosecha enorme de café en otro país puede bajar el precio, y eso terminar en que los "
               "jóvenes de una vereda colombiana se vayan a la ciudad.",
            ojo="confundir coincidir con causar: que dos cosas pasen al tiempo no prueba que una produzca "
                "la otra.",
            chequeo="¿Un hecho de otro país puede cambiar algo en Colombia? Da un caso. (sí: una crisis o una guerra que sube precios)",
            svg=fig_arbol),
    },
    vocab=[("Hecho histórico", "algo que pasó y dejó huella"),
           ("Causa", "lo que hace que algo pase"),
           ("Consecuencia", "lo que resulta de un hecho"),
           ("Multicausalidad", "un hecho casi siempre tiene varias causas"),
           ("Perspectiva", "el lugar desde donde se mira"),
           ("Fuente", "de donde sale la información"),
           ("Testimonio", "lo que cuenta alguien que lo vivió"),
           ("Desplazamiento", "huir de donde se vive por la violencia"),
           ("Despojo", "que otro se quede con tu tierra")]),

 5: dict(
    titulo="El lugar también cuenta",
    centro=("Territorio", "un espacio con gente, recursos y reglas, que se disputa y se transforma",
            fig_territorio),
    centro_ej="un río no es solo agua: es ruta para lanchas, comida para pescadores, frontera entre dos "
              "municipios y desagüe de una ciudad.",
    centro_ojo="tratar el lugar como el fondo del problema. Pregunta qué tiene ese lugar que lo explica.",
    centro_chequeo="¿Por qué un puerto se vuelve un lugar disputado? (porque por ahí entran y salen mercancías)",
    ideas={
        "El lugar explica el problema": dict(
            corto="lo que el lugar tiene o le falta",
            d="Las características del lugar (relieve, clima, ríos, fronteras, recursos, vías) explican "
              "por qué algo pasa allí y no en otra parte: quién llega, qué se disputa, qué riesgo hay.",
            f="lugar → relieve · recursos · vías · frontera → problema",
            ej="un cruce de carreteras en la mitad del país se vuelve centro de comercio: todo el que "
               "viaja pasa por ahí.",
            ojo="explicarlo todo por las personas y olvidar el mapa, o al revés. El problema nace del "
                "cruce entre lugar y gente.",
            chequeo="¿Por qué hay tantos pueblos a la orilla de los ríos? (agua, pesca y transporte)",
            svg=fig_mapa),
        "Ninguna voz se queda afuera": dict(
            corto="todos los actores, también los ausentes",
            d="En un problema territorial hablan muchos: comunidades, empresas, Estado, organizaciones, "
              "grupos armados, migrantes. Un análisis completo nombra a todos, sobre todo a los que "
              "nadie escucha y a los que deciden desde lejos.",
            f="¿quién vive aquí? · ¿quién decide? · ¿quién gana? · ¿quién falta?",
            ej="en el arreglo de una playa turística hablan los hoteles y la alcaldía, pero también los "
               "pescadores, los vendedores y los que llegan a trabajar en temporada.",
            ojo="dejar por fuera al actor que no habla en el texto: muchas veces la respuesta correcta "
                "es la que lo incluye.",
            chequeo="Se planea una carretera por la selva. Nombra un actor que casi nadie menciona. (la comunidad que vive allí)",
            svg=fig_falta),
        "Una medida, efectos en cadena": dict(
            corto="una medida desata una cadena",
            d="Una medida sobre un territorio produce un efecto, que produce otro, y otro, como fichas de "
              "dominó. Seguir la cadena paso a paso muestra efectos sociales, económicos, políticos y "
              "ambientales que no se veían al principio.",
            f="medida → efecto 1 → efecto 2 → efecto 3",
            ej="un derrumbe cierra la vía → los camiones dan la vuelta → sube el costo del transporte → "
               "la papa llega más cara a la ciudad.",
            ojo="saltar del primer eslabón al último sin los del medio: cada salto tiene que salir del "
                "anterior.",
            chequeo="Se seca una laguna. Arma tres eslabones. (menos agua → menos cosecha → la gente se va)",
            svg=fig_domino),
        "Qué dice y qué busca quien habla": dict(
            corto="el interés detrás de las palabras",
            d="Lo que un actor dice sobre un territorio y su gente muestra lo que busca: proteger, "
              "explotar, ordenar, quedarse. Las palabras con carga («atrasados», «progreso», «tierra "
              "vacía») delatan prejuicios e intenciones.",
            f="lo que dice → la palabra con carga → lo que busca",
            ej="llamar «lote vacío» a un humedal prepara el terreno para construir: la palabra borra que "
               "allí viven aves y pasa el agua.",
            ojo="tomar las palabras de un actor como un dato neutral. Pregunta siempre qué gana él si le "
                "creen.",
            chequeo="Una empresa llama «modernización» a talar un parque para hacer parqueaderos. ¿Qué busca? (construir)",
            svg=fig_discurso),
    },
    vocab=[("Territorio", "espacio con gente, recursos y reglas"),
           ("Relieve", "las formas del terreno: montañas, valles"),
           ("Recurso natural", "lo que da la naturaleza: agua, suelo, minerales"),
           ("Frontera", "límite entre dos países o regiones"),
           ("Zona de riesgo", "lugar expuesto a inundación o derrumbe"),
           ("Migración", "moverse de un lugar a otro para vivir"),
           ("Conflicto ambiental", "disputa por el uso de la naturaleza"),
           ("Prejuicio", "juicio sobre alguien sin conocerlo"),
           ("Actor armado", "grupo que usa las armas para controlar")]),

 6: dict(
    titulo="Ganar no basta",
    centro=("Legitimidad", "un poder es legítimo si se obtiene y se ejerce con la ley y respetando derechos",
            fig_pedestal),
    centro_ej="un personero estudiantil que gana con votos comprados tiene el cargo, pero no la "
              "legitimidad.",
    centro_ojo="creer que legítimo es lo mismo que popular o que eficaz.",
    centro_chequeo="Un representante ganó por mayoría y luego cambió el manual sin consultar a nadie. ¿Fue legítima esa decisión? (no: se salió de las reglas)",
    ideas={
        "La mayoría y sus límites": dict(
            corto="la mayoría decide, pero no puede todo",
            d="En democracia decide la mayoría, pero hay cosas que ninguna votación puede quitar: los "
              "derechos fundamentales, también los de las minorías, la división de poderes y las reglas "
              "del juego. Una mayoría sin límites se vuelve tiranía.",
            f="mayoría + límites (derechos y reglas) = democracia",
            ej="un curso vota 30 contra 5 que esos cinco limpien el salón todo el año: ganó la mayoría, "
               "pero la decisión atropella la igualdad.",
            ojo="creer que si se votó, todo vale. Cambiar las reglas para que gane siempre el mismo "
                "tampoco es democrático.",
            chequeo="¿Puede una mayoría votar que un grupo no pueda opinar? (no: lo impiden el pluralismo y la libertad de expresión)",
            svg=fig_mayoria),
        "Eficaz no es lo mismo que legítimo": dict(
            corto="funcionar no justifica cualquier medio",
            d="Eficaz es lo que logra su objetivo; legítimo es lo que se hace dentro de la ley y "
              "respetando derechos. Un gobierno puede ser eficaz debilitando a los jueces o a la prensa: "
              "logra resultados, pero pierde legitimidad.",
            f="eficaz = logra el fin · legítimo = respeta los medios",
            ej="un rector acaba con la indisciplina revisando los celulares de todos sin permiso: "
               "funcionó, pero pasó por encima de la intimidad.",
            ojo="aceptar una medida porque «dio resultados». También se pregunta qué costó y qué "
                "derechos se perdieron en el camino.",
            chequeo="Una empresa entrega a tiempo porque no paga las horas extra. ¿Eficaz, legítima o las dos? (eficaz, no legítima)",
            svg=fig_medidores),
        "Lo político, lo social y lo ético": dict(
            corto="tres planos de una consecuencia",
            d="Una decisión de poder se mira en tres planos: político (qué pasa con las instituciones y "
              "con el poder), social (qué le pasa a la gente y a la convivencia) y ético (si es justa y "
              "respeta la dignidad).",
            f="político: instituciones · social: la gente · ético: lo justo",
            ej="un concejo aprueba una norma a medianoche y sin debate: se salta el control (político), "
               "la gente desconfía (social) y no fue transparente (ético).",
            ojo="mezclar los planos: «la gente protesta» es social, no ético; «es injusto» es ético, no "
                "político.",
            chequeo="«La decisión dejó al Congreso sin poder de control». ¿Qué plano es? (político)",
            svg=fig_planos),
        "Quién lo dice y desde qué principio": dict(
            corto="cada voz invoca un principio",
            d="En un debate ético-político cada actor se apoya en un principio: legalidad, igualdad, "
              "presunción de inocencia, libertad de prensa, separación de poderes. Se identifica quién "
              "habla, qué principio invoca y si los hechos lo confirman.",
            f="voz → principio que invoca → ¿los hechos lo confirman?",
            ej="en un debate sobre cámaras en los salones, el rector invoca la seguridad, los "
               "estudiantes la intimidad y los padres su derecho a saber cómo va la clase.",
            ojo="decir «culpable» de alguien que solo está investigado: toda persona se presume "
                "inocente mientras no la declaren culpable (art. 29).",
            chequeo="Alguien dice «nadie está por encima de la ley». ¿Qué principio invoca? (el Estado de derecho)",
            svg=fig_medallas),
    },
    vocab=[("Legitimidad", "poder ganado y usado según las reglas"),
           ("Legalidad", "actuar de acuerdo con la ley"),
           ("Eficacia", "lograr el objetivo propuesto"),
           ("Estado de derecho", "nadie está por encima de la ley"),
           ("División de poderes", "tres ramas que se controlan entre sí"),
           ("Pluralismo", "caben todas las voces, también las críticas"),
           ("Minoría", "el grupo con menos votos o menos poder"),
           ("Presunción de inocencia", "inocente hasta que una condena quede en firme"),
           ("Autoritarismo", "poder que se salta los límites")]),
}
