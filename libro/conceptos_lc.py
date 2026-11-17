"""Conceptualización de Lectura Crítica (ver conceptos.py y el modelo aprobado conceptos_mate.py).

Seis misiones: para cada una, la idea central, una tarjeta por estrategia (en los nombres exactos de
plan_lc.MISIONES[mis]["estr"]) y nueve palabras de vocabulario. Lo justo para comprender, sin teoría.

Fuentes: plan_lc.py (MISIONES: componente, estrategias, «instala» y «ojo»; TALLER: el contexto de
cada pregunta; AVISOS; el banco ICFES de tablero/icfes.csv) y clase_viva_lc.py (SABERES y la frase
de ACTIVACION de cada clase). Los ejemplos son PROPIOS: no repiten textos, casos ni opciones de las
10 preguntas del libro ni de las 4 de entrenamiento, ni la frase de la activación, para que la
conceptualización no resuelva nada por adelantado. Sin nombres de políticos.

Prueba: python3 conceptos_area.py lc /tmp/claude-0/pc_lc
"""
from conceptos_figs import *  # noqa: F401,F403  (TINTA, GRIS, LINEA, colores, F, math)
from conceptos_figs import _svg, _t, _caja, _flecha, _tarjeta, _bien, _mal, _claro


# ═══════════════════════════════ piezas propias ═══════════════════════════════
def _persona(x, y, c, r=18):
    """Cabeza en (x, y) y hombros debajo."""
    return (f'<path d="M{x-r*1.6} {y+r*3.6} Q{x-r*1.5} {y+r*1.2} {x} {y+r*1.2} Q{x+r*1.5} {y+r*1.2} '
            f'{x+r*1.6} {y+r*3.6} Z" fill="{_claro(c)}" stroke="{TINTA}" stroke-width="2.5"/>'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>')


def _renglones(x, y, w, n, paso=22, sw=6):
    """Renglones de un texto (pictograma): barras grises, no texto."""
    s = ""
    for k in range(n):
        ancho = w if k < n - 1 else w * 0.6
        s += (f'<line x1="{x}" y1="{y + k*paso}" x2="{x + ancho}" y2="{y + k*paso}" stroke="{LINEA}" '
              f'stroke-width="{sw}" stroke-linecap="round"/>')
    return s


# ═══════════════════════════════ misión 1 ═══════════════════════════════
def fig_contexto(c):
    s = (_tarjeta(135, 34, 150, 58, "pesado", c, 26)
         + _flecha(185, 96, 120, 148, c) + _flecha(235, 96, 300, 148, c)
         + _tarjeta(30, 152, 170, 52, "maleta pesada", TINTA, 20)
         + _tarjeta(220, 152, 170, 52, "amigo pesado", TINTA, 20)
         + _t(115, 244, "pesa mucho", 20, c, "middle") + _t(305, 244, "cae mal", 20, c, "middle"))
    return _svg(s, "La misma palabra cambia de sentido según la frase donde está")


def fig_palabra(c):
    s = (f'<rect x="30" y="40" width="360" height="62" rx="12" fill="{_claro(c, .9)}" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(210, 80, "Hoy está frío conmigo", 24, TINTA, "middle")
         + _flecha(150, 106, 115, 140, GRIS, 3) + _flecha(270, 106, 305, 140, GRIS, 3)
         + f'<rect x="40" y="146" width="150" height="54" rx="12" fill="#fff" stroke="{VERDE}" stroke-width="3"/>'
         + _t(56, 181, "distante", 21, TINTA, w="600") + _bien(148, 170)
         + f'<rect x="230" y="146" width="150" height="54" rx="12" fill="#fff" stroke="{ROJO}" stroke-width="3"/>'
         + _t(246, 181, "helado", 21, TINTA, w="600") + _mal(344, 163)
         + _t(210, 255, "¿la frase sigue diciendo lo mismo?", 19, TINTA, "middle", "600"))
    return _svg(s, "Una palabra se cambia por otra y se mira si la frase dice lo mismo")


def fig_funcion(c):
    s = _tarjeta(120, 36, 180, 60, "la idea", c, 24, _claro(c, .88))
    for k, txt in enumerate(["ejemplo", "explica", "contrasta"]):
        x = 20 + k * 135
        s += _tarjeta(x, 176, 120, 50, txt, TINTA, 19)
        s += _flecha(x + 60, 172, 210 + (k - 1) * 40, 102, c, 3.5)
    s += _t(210, 270, "¿qué hace en el texto?", 20, TINTA, "middle")
    return _svg(s, "Tres partes del texto trabajan para la idea")


def fig_iceberg(c):
    s = (f'<rect x="30" y="120" width="360" height="150" rx="10" fill="{_claro(c, .9)}"/>'
         f'<polygon points="150,120 270,120 320,196 262,258 160,252 110,190" fill="#fff" fill-opacity=".85" stroke="{TINTA}" stroke-width="2.5" stroke-dasharray="7 6"/>'
         f'<polygon points="160,120 190,66 210,80 234,56 262,120" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M30 120 Q60 110 90 120 T150 120 M270 120 Q300 110 330 120 T390 120" fill="none" stroke="{c}" stroke-width="3"/>'
         + _t(274, 74, "lo que dice", 20, TINTA) + _t(215, 196, "lo que se", 20, c, "middle")
         + _t(215, 220, "deduce", 20, c, "middle"))
    return _svg(s, "Un iceberg: arriba lo que el texto dice, abajo lo que se deduce")


def fig_columnas(c):
    s = (f'<polygon points="60,92 210,34 360,92" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="60" y="92" width="300" height="40" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(210, 120, "idea central", 22, c, "middle"))
    for x in (90, 190, 290):
        s += f'<rect x="{x}" y="132" width="40" height="112" fill="#EEF2F8" stroke="{TINTA}" stroke-width="2.5"/>'
    s += (f'<rect x="50" y="244" width="320" height="16" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2.5"/>'
          + _t(210, 290, "los detalles la sostienen", 18, TINTA, "middle", "600"))
    return _svg(s, "Un techo, la idea central, sostenido por columnas, los detalles")


# ═══════════════════════════════ misión 2 ═══════════════════════════════
def fig_decir_hacer(c):
    s = (f'<ellipse cx="100" cy="120" rx="78" ry="56" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="70,170 60,210 100,174" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<ellipse cx="100" cy="120" rx="76" ry="54" fill="#fff"/>'
         + _t(100, 130, "dice", 28, TINTA, "middle") + _t(210, 132, "+", 34, GRIS, "middle"))
    for k in range(8):
        s += (f'<rect x="300" y="64" width="22" height="24" rx="3" fill="{_claro(c)}" stroke="{TINTA}" '
              f'stroke-width="2.5" transform="rotate({45*k} 311 124)"/>')
    s += (f'<circle cx="311" cy="124" r="50" fill="{_claro(c)}" stroke="{TINTA}" stroke-width="2.5"/>'
          f'<circle cx="311" cy="124" r="38" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
          + _t(311, 133, "hace", 26, c, "middle")
          + _t(210, 262, "un párrafo hace las dos cosas", 20, TINTA, "middle"))
    return _svg(s, "Un globo de diálogo, lo que dice, y un engranaje, lo que hace")


def fig_verbos(c):
    s = ""
    for k, v in enumerate(["introduce", "ejemplifica", "matiza"]):
        y = 34 + k * 82
        s += (f'<rect x="30" y="{y}" width="200" height="64" rx="8" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
              + _renglones(48, y + 18, 160, 3, 14, 5)
              + _flecha(238, y + 32, 262, y + 32, c, 3.5)
              + _tarjeta(270, y + 10, 130, 44, v, c, 19))
    return _svg(s, "Tres párrafos, cada uno con el verbo de lo que hace")


def fig_diana(c):
    s = ""
    for r, f in ((92, "#fff"), (64, _claro(c)), (36, "#fff"), (12, c)):
        s += f'<circle cx="300" cy="140" r="{r}" fill="{f}" stroke="{TINTA}" stroke-width="2.5"/>'
    s += (_t(100, 96, "palabra con carga", 18, TINTA, "middle", "600")
          + _tarjeta(25, 110, 150, 56, "«progreso»", c, 22)
          + _flecha(178, 138, 284, 140, TINTA, 4)
          + _t(300, 270, "¿a quién apunta?", 20, TINTA, "middle"))
    return _svg(s, "Una palabra con carga apunta a un blanco: lo que se critica")


def fig_brujula(c):
    s = f'<circle cx="210" cy="150" r="92" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
    s += f'<circle cx="210" cy="150" r="80" fill="{_claro(c, .9)}" stroke="{LINEA}" stroke-width="2"/>'
    s += (f'<polygon points="210,138 292,150 210,162" fill="{c}" stroke="{TINTA}" stroke-width="2"/>'
          f'<polygon points="210,138 128,150 210,162" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
          f'<circle cx="210" cy="150" r="8" fill="{TINTA}"/>'
          + _t(210, 46, "informa", 20, TINTA, "middle") + _t(210, 270, "cuenta", 20, TINTA, "middle")
          + _t(308, 157, "convence", 20, c) + _t(112, 157, "critica", 20, TINTA, "end"))
    return _svg(s, "Una brújula cuya aguja apunta al propósito del texto")


def fig_puente(c):
    s = (_caja(25, 140, 115, 76, 24, "#fff", _claro(c, .7), _claro(c, .9))
         + _t(82, 186, "idea A", 22, TINTA, "middle")
         + _caja(265, 140, 115, 76, 24, "#fff", _claro(c, .7), _claro(c, .9))
         + _t(322, 186, "idea B", 22, TINTA, "middle")
         + f'<path d="M140 150 Q202 70 265 150" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
         + _tarjeta(140, 40, 130, 42, "conector", c, 20)
         + _t(205, 268, "pero · por eso · además", 20, TINTA, "middle"))
    return _svg(s, "Dos ideas unidas por un puente: el conector")


# ═══════════════════════════════ misión 3 ═══════════════════════════════
def fig_estructura(c):
    s = (f'<polyline points="40,226 150,226 150,104 270,104 270,204 380,204" fill="none" stroke="{TINTA}" '
         f'stroke-width="5" stroke-linejoin="round"/>'
         f'<circle cx="150" cy="226" r="12" fill="{c}"/><circle cx="270" cy="104" r="12" fill="{c}"/>'
         + _t(40, 260, "inicio", 20, TINTA) + _t(380, 238, "cierre", 20, TINTA, "end")
         + _t(160, 160, "giro", 20, c) + _t(290, 98, "giro", 20, c))
    return _svg(s, "El camino de un texto: inicio, dos giros y cierre")


def fig_bisagra(c):
    s = (f'<polygon points="50,70 200,86 200,236 50,252" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="200,86 340,56 340,226 200,236" fill="{_claro(c)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="192" y="104" width="16" height="28" rx="6" fill="{c}"/>'
         f'<rect x="192" y="192" width="16" height="28" rx="6" fill="{c}"/>'
         f'<path d="M290 40 Q340 20 372 56" fill="none" stroke="{c}" stroke-width="4"/>'
         f'<path d="M372 56 L357 51 M372 56 L370 41" stroke="{c}" stroke-width="4" stroke-linecap="round"/>'
         + _t(125, 168, "antes", 22, TINTA, "middle") + _t(270, 150, "después", 22, TINTA, "middle")
         + _t(210, 286, "ahora bien · pero · sin embargo", 18, TINTA, "middle", "600"))
    return _svg(s, "Una puerta con bisagra: el texto gira de un lado al otro")


def fig_termometro(c):
    s = (_tarjeta(110, 36, 200, 50, "lo que muestra", TINTA, 21)
         + _flecha(210, 90, 140, 150, c, 4)
         + f'<rect x="60" y="160" width="300" height="26" rx="13" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="2.5"/>'
         + f'<polygon points="128,154 152,154 140,174" fill="{c}" stroke="{TINTA}" stroke-width="2"/>'
         + _t(36, 184, "−", 34, ROJO, "middle") + _t(386, 186, "+", 34, VERDE, "middle")
         + _t(210, 240, "valora sin decirlo", 20, TINTA, "middle"))
    return _svg(s, "Una escala de valoración: lo que el autor muestra la mueve")


def fig_vuelta(c):
    s = f'<line x1="80" y1="170" x2="340" y2="170" stroke="{TINTA}" stroke-width="3"/>'
    for x, txt in ((80, "inicio"), (210, "medio"), (340, "cierre")):
        s += (f'<circle cx="{x}" cy="170" r="20" fill="{_claro(c) if x == 340 else "#fff"}" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x, 224, txt, 20, TINTA, "middle"))
    s += (f'<path d="M340 146 Q210 20 84 144" fill="none" stroke="{c}" stroke-width="4" stroke-dasharray="9 6"/>'
          f'<path d="M84 144 L84 128 M84 144 L99 138" stroke="{c}" stroke-width="4" stroke-linecap="round"/>'
          + _t(210, 52, "¿repite, niega o integra?", 19, c, "middle"))
    return _svg(s, "El cierre se lee contra el inicio")


def fig_reflector(c):
    s = (f'<polygon points="190,48 230,48 310,226 110,226" fill="{_claro(c, .85)}" opacity=".8"/>'
         f'<polygon points="184,20 236,20 230,50 190,50" fill="{TINTA}"/>'
         + "".join(f'<rect x="{x}" y="236" width="{w}" height="16" rx="8" fill="{LINEA}"/>'
                   for x, w in ((40, 60), (108, 76), (240, 54), (302, 80)))
         + f'<rect x="192" y="232" width="38" height="24" rx="6" fill="{c}" stroke="{TINTA}" stroke-width="2"/>'
         + _t(210, 286, "un detalle que dice mucho", 18, TINTA, "middle", "600"))
    return _svg(s, "Un reflector ilumina un detalle pequeño del renglón")


# ═══════════════════════════════ misión 4 ═══════════════════════════════
def fig_carretera(c):
    s = (f'<polygon points="140,276 280,276 232,62 188,62" fill="#EEF2F8" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="210" y1="80" x2="210" y2="262" stroke="#fff" stroke-width="5" stroke-dasharray="14 12"/>'
         f'<line x1="320" y1="130" x2="320" y2="262" stroke="{TINTA}" stroke-width="5"/>'
         f'<polygon points="320,70 362,112 320,154 278,112" fill="{_claro(c)}" stroke="{TINTA}" stroke-width="2.5"/>'
         + _flecha(300, 112, 340, 112, c, 5)
         + _t(30, 44, "el texto avisa lo que viene", 20, TINTA))
    return _svg(s, "Una carretera con una señal: el texto avisa lo que viene")


def fig_tres_senales(c):
    s = ""
    for k, lab in enumerate(["consecuencia", "contraste", "reformula"]):
        x = 70 + k * 140
        s += (f'<line x1="{x}" y1="130" x2="{x}" y2="220" stroke="{TINTA}" stroke-width="5"/>'
              f'<rect x="{x-42}" y="44" width="84" height="84" rx="14" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(x, 256, lab, 19, TINTA, "middle"))
    s += _flecha(48, 86, 92, 86, c, 5)                                  # sigue hacia adelante
    s += (f'<path d="M210 112 L210 88 L188 64 M210 88 L232 64" fill="none" stroke="{c}" stroke-width="5" '
          f'stroke-linecap="round" stroke-linejoin="round"/>')            # se abre en dos
    s += (f'<path d="M367 70 A20 20 0 1 1 352 64" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
          f'<path d="M352 64 L366 58 M352 64 L360 77" stroke="{c}" stroke-width="5" stroke-linecap="round"/>')
    return _svg(s, "Tres señales: seguir, abrirse en dos y dar la vuelta")


def fig_dedo(c):
    s = (f'<rect x="40" y="26" width="230" height="230" rx="10" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="52" y="146" width="206" height="28" rx="6" fill="{_claro(c, .7)}"/>'
         + _renglones(64, 56, 180, 8, 26, 6)
         + f'<rect x="236" y="151" width="84" height="18" rx="9" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + f'<rect x="300" y="138" width="86" height="58" rx="16" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + f'<rect x="236" y="151" width="70" height="15" rx="7" fill="#fff"/>'
         + "".join(f'<line x1="{x}" y1="172" x2="{x}" y2="194" stroke="{TINTA}" stroke-width="2"/>' for x in (324, 344, 364))
         + _t(210, 288, "¿lo dice tal cual?", 19, TINTA, "middle"))
    return _svg(s, "Un dedo señala el renglón donde está escrita la respuesta")


def fig_infografia(c):
    s = (f'<rect x="40" y="24" width="340" height="246" rx="12" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="56" y="40" width="308" height="42" rx="8" fill="{_claro(c)}" stroke="{TINTA}" stroke-width="2"/>'
         + _t(210, 69, "título", 21, TINTA, "middle")
         + f'<rect x="56" y="96" width="146" height="110" rx="8" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
         + _t(70, 122, "dato", 19, c))
    for k, h in enumerate([30, 52, 70]):
        s += f'<rect x="{126 + k*24}" y="{196 - h}" width="16" height="{h}" fill="{c}" opacity=".8"/>'
    s += (f'<rect x="218" y="96" width="146" height="110" rx="8" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
          + _t(232, 122, "lista", 19, c))
    for k in range(3):
        y = 146 + k * 22
        s += (f'<circle cx="238" cy="{y}" r="5" fill="{TINTA}"/>'
              f'<line x1="252" y1="{y}" x2="344" y2="{y}" stroke="{LINEA}" stroke-width="5" stroke-linecap="round"/>')
    s += (f'<rect x="56" y="218" width="308" height="38" rx="8" fill="#F7F9FC" stroke="{TINTA}" stroke-width="2"/>'
          + _t(210, 244, "fuente", 19, TINTA, "middle", "600"))
    return _svg(s, "Una infografía partida en bloques: título, dato, lista y fuente")


def fig_huellas(c):
    tiles = [(30, 30, "instructivo"), (220, 30, "narrativo"), (30, 148, "argumentativo"), (220, 148, "informativo")]
    s = ""
    for x, y, lab in tiles:
        s += (f'<rect x="{x}" y="{y}" width="170" height="104" rx="12" fill="#fff" stroke="{c}" stroke-width="3"/>'
              + _t(x + 85, y + 90, lab, 19, TINTA, "middle"))
    s += (_t(115, 70, "1. 2. 3.", 22, c, "middle") + _t(305, 70, "Había una vez", 19, c, "middle", "600")
          + _t(115, 188, "porque…", 22, c, "middle"))
    for k, h in enumerate([16, 30, 22, 38]):
        s += f'<rect x="{278 + k*16}" y="{196 - h}" width="11" height="{h}" fill="{c}" opacity=".8"/>'
    s += _t(210, 286, "huellas → tipo → propósito", 18, TINTA, "middle", "600")
    return _svg(s, "Cuatro tipos de texto con su huella")


# ═══════════════════════════════ misión 5 ═══════════════════════════════
def fig_intencion(c):
    s = (f'<rect x="40" y="70" width="110" height="140" rx="10" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + _renglones(58, 100, 74, 5, 22, 6)
         + _flecha(160, 140, 268, 140, c, 5)
         + _t(214, 118, "quiere algo", 20, c, "middle")
         + _persona(320, 110, c, 24)
         + _t(320, 236, "tú", 22, TINTA, "middle"))
    return _svg(s, "Un texto lanza una flecha hacia el lector: quiere algo de él")


def fig_tres_efectos(c):
    s = _persona(210, 190, c, 26)
    for x, y, txt in ((86, 82, "sé"), (210, 58, "pienso"), (334, 82, "hago")):
        s += (f'<circle cx="{x}" cy="{y}" r="44" fill="{_claro(c, .88)}" stroke="{c}" stroke-width="3"/>'
              + _t(x, y + 8, txt, 22, TINTA, "middle"))
    s += (f'<circle cx="150" cy="140" r="6" fill="{c}"/><circle cx="270" cy="140" r="6" fill="{c}"/>'
          f'<circle cx="210" cy="124" r="6" fill="{c}"/>')
    return _svg(s, "Si el texto funciona, el lector sabe, piensa distinto o hace algo")


def fig_atril(c):
    s = (_persona(210, 64, c, 22)
         + _caja(150, 122, 120, 120, 26, "#fff", _claro(c, .7), _claro(c, .9))
         + _t(210, 190, "desde", 20, TINTA, "middle") + _t(210, 214, "dónde", 20, TINTA, "middle")
         + f'<rect x="276" y="28" width="122" height="50" rx="14" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + f'<polygon points="282,70 262,86 296,76" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + f'<rect x="279" y="31" width="116" height="44" rx="12" fill="#fff"/>'
         + _t(337, 60, "dice…", 21, TINTA, "middle")
         + _tarjeta(20, 40, 116, 46, "interés", c, 20) + _flecha(138, 64, 178, 74, c, 3.5))
    return _svg(s, "Una persona habla desde un atril: su lugar y su interés pesan en lo que dice")


def fig_choque(c):
    s = (f'<rect x="20" y="34" width="180" height="70" rx="16" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<polygon points="70,100 60,132 100,102" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="23" y="37" width="174" height="64" rx="14" fill="#fff"/>'
         + _t(110, 78, "«¡rápido!»", 26, c, "middle"))
    for k in range(5):
        s += _persona(232 + k * 38, 150, c, 13)
    s += (f'<line x1="150" y1="170" x2="196" y2="170" stroke="{ROJO}" stroke-width="5"/>'
          f'<line x1="150" y1="188" x2="196" y2="188" stroke="{ROJO}" stroke-width="5"/>'
          f'<line x1="186" y1="154" x2="160" y2="204" stroke="{ROJO}" stroke-width="5"/>'
          + _t(80, 186, "dice", 22, TINTA, "middle") + _t(310, 232, "muestra", 22, TINTA, "middle")
          + _t(210, 280, "la ironía está en el choque", 19, TINTA, "middle", "600"))
    return _svg(s, "Un letrero dice rápido y la escena muestra una fila larga")


def _llave(x, y, c):
    return (f'<circle cx="{x}" cy="{y}" r="18" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
            f'<path d="M{x+18} {y} L{x+76} {y} M{x+58} {y} L{x+58} {y+14} M{x+70} {y} L{x+70} {y+12}" '
            f'stroke="{c}" stroke-width="6" stroke-linecap="round"/>')


def fig_equivalencia(c):
    s = (_llave(56, 92, c)
         + f'<rect x="44" y="164" width="56" height="86" rx="4" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="3"/>'
         + f'<circle cx="88" cy="210" r="5" fill="{TINTA}"/>'
         + _t(180, 104, "=", 38, GRIS, "middle") + _t(180, 222, "=", 38, GRIS, "middle")
         + _t(214, 102, "solución", 26, TINTA) + _t(214, 220, "oportunidad", 26, TINTA)
         + _t(210, 286, "pieza por pieza", 19, c, "middle"))
    return _svg(s, "Una llave equivale a solución y una puerta a oportunidad")


# ═══════════════════════════════ misión 6 ═══════════════════════════════
def fig_torre(c):
    s = (_caja(100, 204, 220, 50, 26, "#fff", _claro(c, .7), _claro(c, .9))
         + _t(210, 237, "evidencia", 21, TINTA, "middle")
         + _caja(125, 140, 170, 50, 26, "#fff", _claro(c, .7), _claro(c, .9))
         + _t(210, 173, "razones", 21, TINTA, "middle")
         + _caja(150, 76, 120, 50, 26, _claro(c, .85), _claro(c, .6), _claro(c, .92))
         + _t(210, 109, "tesis", 22, c, "middle"))
    return _svg(s, "Una torre: la tesis arriba, apoyada en razones y evidencia")


def fig_una_linea(c):
    s = (f'<rect x="30" y="70" width="320" height="130" rx="14" fill="#fff" stroke="{c}" stroke-width="3"/>'
         + _t(52, 118, "El autor defiende que…", 22, TINTA)
         + f'<line x1="52" y1="166" x2="320" y2="166" stroke="{LINEA}" stroke-width="3"/>'
         + f'<line x1="318" y1="196" x2="386" y2="128" stroke="{c}" stroke-width="16" stroke-linecap="butt"/>'
         + f'<polygon points="312,190 324,202 304,210" fill="{TINTA}"/>'
         + _t(190, 252, "una sola línea, con tus palabras", 19, TINTA, "middle", "600"))
    return _svg(s, "Una tarjeta para escribir la tesis en una sola línea")


def fig_jenga(c):
    s = ""
    for k in range(5):
        y = 222 - k * 34
        x = 110 + (120 if k == 2 else 0)
        cara = _claro(c, .75) if k == 2 else "#fff"
        s += _caja(x, y, 160, 30, 16, cara, "#D3DCEA", "#EEF2F8")
    s += (_flecha(286, 170, 386, 170, c, 4)
          + _t(200, 48, "¿sigue en pie?", 21, c, "middle"))
    return _svg(s, "Una torre de bloques a la que se le saca una pieza")


def fig_silencio(c):
    s = (f'<line x1="210" y1="170" x2="210" y2="252" stroke="{TINTA}" stroke-width="6"/>'
         f'<rect x="100" y="86" width="220" height="84" rx="12" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
         + _t(210, 140, "¡SILENCIO!", 32, c, "middle"))
    for r in (22, 42):
        s += (f'<path d="M{86} {128 - r} Q{86 - r} 128 {86} {128 + r}" fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round"/>'
              f'<path d="M{334} {128 - r} Q{334 + r} 128 {334} {128 + r}" fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round"/>')
    s += _t(210, 288, "lo pide a gritos", 20, TINTA, "middle")
    return _svg(s, "Un letrero que pide silencio mientras hace ruido")


def fig_camino(c):
    s = (f'<path d="M40 250 C140 250 100 160 200 160 S260 70 360 70" fill="none" stroke="{TINTA}" '
         f'stroke-width="5" stroke-dasharray="2 10" stroke-linecap="round"/>'
         f'<line x1="360" y1="70" x2="360" y2="20" stroke="{TINTA}" stroke-width="4"/>'
         f'<polygon points="360,20 396,32 360,44" fill="{c}"/>')
    for k, (x, y) in enumerate([(120, 205), (200, 160), (280, 115)]):
        s += (f'<circle cx="{x}" cy="{y}" r="17" fill="{c}" stroke="{TINTA}" stroke-width="2"/>'
              + _t(x, y + 7, str(k + 1), 20, "#fff", "middle"))
    s += (_t(348, 40, "conclusión", 20, TINTA, "end")
          + _t(310, 236, "paso a paso", 19, GRIS, "middle", "600"))
    return _svg(s, "Un camino con tres nudos que llega a la conclusión")


# ═══════════════════════════════ los datos ═══════════════════════════════
DATOS = {
 1: dict(
    titulo="Cada palabra trae su mundo",
    centro=("Leer en contexto", "el sentido de una palabra lo fija la frase donde está, no el diccionario",
            fig_contexto),
    centro_ej="«pesado» en «una maleta pesada» es que pesa mucho; en «un amigo pesado», que cae mal. "
              "Misma palabra, dos sentidos.",
    centro_ojo="marcar el primer significado que sale en el diccionario sin volver a leer la frase.",
    centro_chequeo="En «está frío con nosotros», ¿«frío» habla de temperatura? (no: quiere decir distante)",
    ideas={
        "La palabra exacta": dict(
            corto="el sentido de una palabra en su frase",
            d="Para saber qué significa una palabra en un texto, cámbiala por otra y mira si la frase "
              "sigue diciendo lo mismo. Ojo con las comillas: avisan que la palabra se usa con otro "
              "sentido, muchas veces irónico.",
            f="palabra → la cambio por otra → ¿la frase dice lo mismo?",
            ej="«Le "
               "“presté” mi cuaderno y nunca volvió»: las comillas dicen que no fue un préstamo, "
               "fue una pérdida.",
            ojo="escoger el significado más común. Casi siempre preguntan el sentido raro, el que solo "
                "funciona en esa frase.",
            chequeo="En «esa película es un ladrillo», ¿qué significa «ladrillo»? (aburrida, pesada)",
            svg=fig_palabra),
        "Para qué está ahí": dict(
            corto="la función de una parte del texto",
            d="Cada parte de un texto hace un trabajo: introduce, da un ejemplo, explica, contrasta o "
              "concluye. La pregunta no es qué dice la frase, sino qué hace en el texto.",
            f="lo que dice ≠ lo que hace: ejemplifica · explica · contrasta",
            ej="«Leer de noche me rinde más. Anoche terminé en una hora el capítulo que en la tarde no "
               "pude.» La segunda frase no trae otra idea: es el ejemplo que respalda la primera.",
            ojo="resumir lo que dice la frase cuando te piden su función. Las opciones con verbos "
                "(ejemplifica, contrasta) son las que responden.",
            chequeo="«Es caro; además, queda lejos». ¿Qué hace lo que viene después de «además»? (suma otra razón)",
            svg=fig_funcion),
        "Lo que no se dice": dict(
            corto="inferir: lo que el texto deja entender",
            d="Inferir es sacar algo que el texto no escribe pero que se deduce de lo que sí escribe. "
              "Toda inferencia tiene que poder señalarse en una pista del texto.",
            f="pista del texto + lo que ya sé = inferencia",
            ej="«Llegó empapado y dejó el paraguas cerrado en la entrada»: no lo dice, pero se deduce "
               "que llovía y que no alcanzó a abrirlo.",
            ojo="inventar más de lo que el texto permite. Si no puedes señalar la pista, es imaginación, "
                "no inferencia.",
            chequeo="«Volvió a mirar el reloj y suspiró». ¿Qué se infiere? (que está impaciente o esperando a alguien)",
            svg=fig_iceberg),
        "La idea que sostiene": dict(
            corto="la idea central de un fragmento",
            d="Es la idea a la que sirven todas las demás frases. Si el fragmento repite algo con "
              "distintas palabras, eso que se repite suele ser lo que lo sostiene.",
            f="frases del texto → ¿qué tienen en común? → idea central",
            ej="un texto cuenta que el abuelo arregla radios, guarda tornillos en frascos y nunca bota "
               "un cable: la idea que lo sostiene es que para él nada es basura.",
            ojo="escoger un detalle verdadero que no es la idea central: es cierto, pero no sostiene nada.",
            chequeo="Si quito una frase y el texto sigue en pie, ¿era la idea central? (no: era un detalle)",
            svg=fig_columnas),
    },
    vocab=[("Contexto", "lo que rodea a una palabra y le da sentido"),
           ("Sentido literal", "lo que la palabra dice al pie de la letra"),
           ("Sentido figurado", "lo que la palabra sugiere más allá de la letra"),
           ("Sinónimo", "palabra que significa lo mismo que otra"),
           ("Comillas", "marcan una cita o un sentido especial"),
           ("Inferencia", "lo que se deduce de las pistas del texto"),
           ("Idea central", "la idea a la que sirven las demás"),
           ("Metáfora", "nombrar una cosa con la imagen de otra"),
           ("Eufemismo", "palabra suave que reemplaza a una dura")]),

 2: dict(
    titulo="Lo que un párrafo hace",
    centro=("Decir y hacer", "un párrafo dice algo y, además, cumple una función en el texto",
            fig_decir_hacer),
    centro_ej="un párrafo cuenta que una abuela aprendió a leer a los 70 años. Eso dice; lo que hace es "
              "servir de ejemplo para la idea de que nunca es tarde.",
    centro_ojo="contestar qué dice el párrafo cuando la pregunta es qué hace.",
    centro_chequeo="Un párrafo empieza «Sin embargo, otros piensan…». ¿Qué hace? (presenta una objeción o un contraste)",
    ideas={
        "Qué hace este párrafo": dict(
            corto="el verbo que nombra su función",
            d="Lo que hace un párrafo se nombra con un verbo: introduce, ejemplifica, objeta, matiza, "
              "amplía o concluye. Su lugar ayuda: el primero suele presentar y el último, cerrar.",
            f="párrafo = un verbo: introduce · ejemplifica · objeta · concluye",
            ej="un texto sobre madrugar: el 1.º dice que rinde más, el 2.º cuenta el caso de una "
               "estudiante y el 3.º admite que no a todos les sirve. Introduce, ejemplifica, matiza.",
            ojo="dos verbos parecidos no son iguales: objetar es ir en contra; matizar es aceptar, pero "
                "con una condición.",
            chequeo="«Es cierto, aunque no siempre». ¿Objeta o matiza? (matiza)",
            svg=fig_verbos),
        "La crítica que no se ve": dict(
            corto="criticar sin decir «esto está mal»",
            d="A veces el autor critica sin decirlo: escoge palabras con carga, pone juntas dos cosas "
              "que chocan o usa la ironía. La crítica se encuentra en esas palabras, no en lo que tú "
              "piensas del tema.",
            f="palabras con carga + a quién apuntan = la crítica",
            ej="«El centro comercial trajo progreso: ya no queda ni un árbol en la cuadra.» No dice que "
               "esté mal, pero critica lo que algunos llaman progreso.",
            ojo="escoger la opción que critica lo que a ti te molesta del tema. La correcta critica lo "
                "que critica el texto.",
            chequeo="«Qué puntual: solo llegó una hora tarde». ¿Qué critica? (la impuntualidad, con ironía)",
            svg=fig_diana),
        "Para qué lo escribió": dict(
            corto="el propósito de todo el texto",
            d="Todo texto se escribe para algo: informar, explicar, convencer, criticar, contar o pedir. "
              "El propósito de todo el texto cabe en un verbo, y no siempre es el mismo de cada párrafo.",
            f="texto completo → un verbo: informa · convence · critica · cuenta",
            ej="una reseña que cuenta la trama de una película y termina con «no pierdan su plata» no "
               "informa: busca convencerte de no verla.",
            ojo="confundir el tema (de qué habla) con el propósito (para qué lo escribió).",
            chequeo="Un folleto dice «lávate las manos 20 segundos». ¿Informa o busca que hagas algo? (que lo hagas)",
            svg=fig_brujula),
        "Cómo se enlazan": dict(
            corto="la relación entre dos ideas",
            d="Dos ideas se enlazan por una relación: causa, consecuencia, contraste, adición o ejemplo. "
              "Casi siempre un conector la dice; si no lo hay, pon uno y mira cuál encaja.",
            f="idea A + conector + idea B   (porque · por eso · pero · además)",
            ej="«Entrené todo el mes; ___ perdí el partido.» Encaja «sin embargo», de contraste. «Por "
               "eso» diría que entrenar me hizo perder.",
            ojo="después de un «pero», el peso cae en lo que viene: eso es lo que el autor quiere "
                "que te quede.",
            chequeo="«Estudió poco, así que…». ¿Qué relación anuncia «así que»? (consecuencia)",
            svg=fig_puente),
    },
    vocab=[("Párrafo", "bloque de texto que desarrolla una idea"),
           ("Función", "el trabajo que hace una parte del texto"),
           ("Propósito", "para qué se escribió el texto"),
           ("Ejemplificar", "mostrar un caso que respalda una idea"),
           ("Objetar", "presentar una idea en contra"),
           ("Matizar", "aceptar una idea con una condición"),
           ("Ironía", "decir lo contrario de lo que se quiere decir"),
           ("Conector", "palabra que dice cómo se unen dos ideas"),
           ("Caricatura", "dibujo que critica con humor")]),

 3: dict(
    titulo="Dónde gira el texto",
    centro=("La estructura del texto", "cómo se arma un texto: dónde empieza, dónde gira y cómo cierra",
            fig_estructura),
    centro_ej="una crónica de un partido arranca en la tribuna, gira hacia el jugador lesionado y cierra "
              "con el estadio vacío. Tres partes, dos giros.",
    centro_ojo="leer cada párrafo suelto. La pregunta casi siempre es por la relación entre las partes.",
    centro_chequeo="¿Cuántas bisagras tiene un texto de tres párrafos? (dos: una entre cada par de párrafos)",
    ideas={
        "La bisagra del texto": dict(
            corto="el punto donde el texto gira",
            d="Una bisagra es el lugar donde el texto cambia de dirección: de un caso a una idea "
              "general, del antes al ahora, de lo que se cree a lo que es. Suele marcarla un conector o "
              "una pregunta.",
            f="parte 1 → bisagra (ahora bien · pero · sin embargo) → parte 2",
            ej="«Todos culpaban al árbitro. Ahora bien, el video muestra que el gol fue legal.» En "
               "«ahora bien» el texto deja la queja y pasa a la prueba.",
            ojo="creer que un párrafo solo sigue con lo mismo. Pregúntate: ¿de qué hablaba antes y de "
                "qué habla ahora?",
            chequeo="«Antes nadie leía en el bus; hoy todos van con el celular». ¿Dónde gira? (en «hoy»: del antes al ahora)",
            svg=fig_bisagra),
        "El juicio que no se dice": dict(
            corto="la valoración que el autor deja ver",
            d="El autor no escribe «esto es bueno» o «esto es malo», pero lo deja ver con lo que escoge "
              "mostrar, con lo que pone junto o con una palabra con carga. El juicio implícito se "
              "deduce: no se copia.",
            f="lo que muestra + cómo lo muestra = lo que piensa",
            ej="«La carta tiene cuarenta platos; el mesero tardó media hora en traer un vaso de agua.» "
               "No dice que el servicio sea malo: lo deja ver al poner juntas las dos cosas.",
            ojo="confundir describir con valorar: «llegó tarde» describe; «es irresponsable» valora.",
            chequeo="«Prometió llamar el lunes. Hoy es jueves.» ¿Qué juicio deja ver? (que no cumple su palabra)",
            svg=fig_termometro),
        "La pieza que remata": dict(
            corto="qué hace el cierre con lo anterior",
            d="El cierre de un texto, o el remate de una caricatura, no está por estar: puede repetir la "
              "idea del inicio, negarla, darle la vuelta o juntar todo lo anterior. Se lee siempre "
              "contra lo que vino antes.",
            f="inicio vs. cierre: repite · niega · da la vuelta · integra",
            ej="un cuento empieza «Nunca me gustó el mar» y termina con el narrador comprando una casa "
               "en la playa: el cierre le da la vuelta al inicio.",
            ojo="leer el final como un párrafo más. Compáralo con la primera línea: ahí está la relación.",
            chequeo="Si el último párrafo dice lo mismo que el primero con otras palabras, ¿qué hace? (repite y refuerza la idea)",
            svg=fig_vuelta),
        "El detalle que lo delata": dict(
            corto="el detalle pequeño que dice mucho",
            d="Un gesto, una palabra o un objeto que aparece un segundo y revela lo que el texto no dice "
              "directamente: lo que siente un personaje o lo que piensa el autor. Pregúntate por qué el "
              "autor puso justo eso.",
            f="detalle → ¿por qué está aquí? → lo que revela",
            ej="«Dijo que estaba tranquila mientras doblaba y desdoblaba la servilleta»: el gesto delata "
               "los nervios que sus palabras niegan.",
            ojo="pasar el detalle de largo porque «no es importante». En un texto corto, nada sobra.",
            chequeo="«Sonrió sin mostrar los dientes y miró hacia la puerta». ¿Qué delata? (incomodidad, ganas de irse)",
            svg=fig_reflector),
    },
    vocab=[("Estructura", "cómo están armadas las partes de un texto"),
           ("Bisagra", "el punto donde el texto cambia de rumbo"),
           ("Explícito", "lo que el texto dice abiertamente"),
           ("Implícito", "lo que el texto deja ver sin decirlo"),
           ("Valoración", "juicio de que algo es bueno o malo"),
           ("Remate", "el cierre que le da sentido a lo anterior"),
           ("Crónica", "relato de hechos reales con mirada de autor"),
           ("Paradoja", "dos ideas opuestas que resultan ciertas"),
           ("Connotación", "lo que una palabra sugiere además")]),

 4: dict(
    titulo="Las señales del texto",
    centro=("Leer la forma", "los conectores y el formato anuncian qué viene y para qué sirve el texto",
            fig_carretera),
    centro_ej="una receta trae pasos numerados y verbos como «mezcle» o «hornee»; una noticia, fecha y "
              "lugar en la primera línea. La forma ya dice qué clase de texto es.",
    centro_ojo="leer solo el contenido y saltarse la forma: títulos, viñetas, cifras y conectores "
               "también hablan.",
    centro_chequeo="Un texto con pasos numerados y verbos como «corte» y «pegue», ¿qué tipo es? (instructivo)",
    ideas={
        "La señal de tránsito": dict(
            corto="el conector anuncia lo que viene",
            d="Los conectores son señales: avisan qué viene antes de que llegue. Unos anuncian una "
              "consecuencia (así que, por eso), otros un contraste (en cambio, pero), otros la misma "
              "idea con otras palabras (es decir) o un caso (por ejemplo).",
            f="así que → consecuencia · en cambio → contraste · es decir → reformula",
            ej="«Mi hermano madruga todos los días; en cambio, yo…» Sin leer el resto, ya sabes que yo "
               "no madrugo.",
            ojo="cambiar un conector por otro de distinta clase cambia el sentido. Antes de escoger, di "
                "qué relación anuncia el original.",
            chequeo="«Por un lado, es barato; por otro…». ¿Qué anuncia «por otro»? (otro aspecto, muchas veces contrario)",
            svg=fig_tres_senales),
        "Lo que puedo señalar con el dedo": dict(
            corto="lo que está escrito, tal cual",
            d="Hay preguntas que no piden interpretar: piden encontrar. Cada opción se lleva al texto y "
              "se busca el renglón que la dice. Si no se puede señalar, no es la respuesta.",
            f="opción → busco el renglón → ¿lo dice tal cual?",
            ej="si el horario dice «abre de 8 a 12 los sábados», «abre los sábados en la mañana» se "
               "puede señalar; «abre todo el fin de semana», no.",
            ojo="las cifras se comparan completas: unidad, año y a qué se refieren. Un número igual "
                "en otro contexto no cuenta.",
            chequeo="El texto dice «7 de cada 10 encuestados». ¿Puedo afirmar «el 70 % del país»? (no: solo de los encuestados)",
            svg=fig_dedo),
        "Qué pieza es esta": dict(
            corto="el papel de cada bloque del texto",
            d="En un texto, y más en una infografía, cada bloque tiene su papel: título, dato, ejemplo, "
              "explicación, lista o fuente. Una lista puede ser de causas, de pasos, de requisitos o de "
              "resultados: hay que ver cuál.",
            f="bloque → ¿título, dato, ejemplo, lista o fuente?",
            ej="en el afiche de una feria, el recuadro «entrada libre, traer documento» no es "
               "publicidad: es una lista de requisitos.",
            ojo="leer una infografía de arriba abajo como si fuera un párrafo. Primero el título; después "
                "cada bloque y qué tiene que ver con el título.",
            chequeo="«Para inscribirte: tener 14 años, el carné y $5.000». ¿Causas, pasos o requisitos? (requisitos)",
            svg=fig_infografia),
        "La forma delata el propósito": dict(
            corto="el tipo de texto por sus huellas",
            d="Cada tipo de texto deja huellas: el informativo trae datos y fuentes; el argumentativo, "
              "una postura y razones; el narrativo, personajes y tiempo; el instructivo, pasos. "
              "Reconocer la forma dice para qué se escribió.",
            f="huellas → tipo de texto → propósito",
            ej="«Considero que la tarea debería ser opcional, porque…»: primera persona, una postura y "
               "un «porque». Es un texto argumentativo.",
            ojo="confundir el tema con el tipo: un texto sobre ciencia puede ser un cuento, y uno sobre "
                "fútbol, una argumentación.",
            chequeo="Un texto con titular, fecha, lugar y lo que pasó, ¿qué tipo es? (una noticia: informativo)",
            svg=fig_huellas),
    },
    vocab=[("Conector", "palabra que anuncia la relación entre ideas"),
           ("Consecuencia", "lo que resulta de algo"),
           ("Contraste", "poner frente a frente dos ideas distintas"),
           ("Reformular", "decir lo mismo con otras palabras"),
           ("Literal", "lo que está escrito tal cual"),
           ("Texto discontinuo", "se lee por bloques: gráficos, tablas, listas"),
           ("Infografía", "texto que mezcla datos, dibujos y bloques"),
           ("Enumeración", "lista de elementos de la misma clase"),
           ("Tipo de texto", "narrativo, informativo, argumentativo…")]),

 5: dict(
    titulo="Todo texto quiere algo",
    centro=("La intención", "lo que el texto busca en quien lo lee: que sepa, que crea o que haga algo",
            fig_intencion),
    centro_ej="en el grupo del curso, «mañana no hay clase» informa; «¡nadie falte a la feria!» quiere "
              "que vayas.",
    centro_ojo="la intención no se adivina en la cabeza del autor: se lee en lo que el texto construye y "
               "en lo que deja afuera.",
    centro_chequeo="Un aviso dice «Últimos cupos: inscríbete hoy». ¿Qué quiere? (que actúes ya: persuadir)",
    ideas={
        "Qué quiere que yo haga": dict(
            corto="informar, convencer o mover a actuar",
            d="Pregúntate qué cambia en ti si el texto funciona: ¿sabes algo nuevo, piensas distinto o "
              "haces algo? El título y el final suelen delatar la intención.",
            f="si funciona, yo… sé algo · pienso distinto · hago algo",
            ej="un afiche con la foto de un pulmón negro y la frase «tú decides» no informa sobre "
               "medicina: quiere que no fumes.",
            ojo="confundir el tema con la intención: un texto sobre deportes puede querer que compres "
                "unos tenis.",
            chequeo="«Cinco razones para dormir ocho horas». ¿Informar o convencer? (convencer: trae razones a favor)",
            svg=fig_tres_efectos),
        "Quién habla y desde dónde": dict(
            corto="la voz y el lugar desde donde habla",
            d="Todo texto tiene una voz: un periodista, una científica, un vecino afectado, una empresa. "
              "Desde dónde habla pesa en lo que dice y en lo que calla. Si cita a un experto, la cita "
              "respalda, pero no demuestra sola.",
            f="voz + lugar + interés = lo que dice y lo que calla",
            ej="la reseña de un celular escrita por la marca y la escrita por un usuario cuentan cosas "
               "distintas del mismo aparato.",
            ojo="pensar que hay una sola voz. En un texto hablan el autor y los que él cita: pregunta "
                "de quién es cada frase.",
            chequeo="Un estudio que dice que el azúcar es sano lo pagó una fábrica de dulces. ¿Qué hay que mirar? (su interés)",
            svg=fig_atril),
        "Lo que dice y lo que muestra": dict(
            corto="la palabra contra la imagen o el hecho",
            d="A veces lo que se dice choca con lo que se muestra: un letrero que dice una cosa sobre un "
              "dibujo que muestra otra, o una frase amable en una situación que la desmiente. En ese "
              "choque está la ironía, y casi siempre la crítica.",
            f="lo que dice vs. lo que muestra = ironía → crítica",
            ej="una tienda anuncia «atención rápida» y la foto muestra una fila de veinte personas.",
            ojo="quedarse con la palabra y no mirar la imagen, o al revés. El sentido está en la "
                "relación entre las dos.",
            chequeo="Ante un cuarto desordenado, la mamá dice «¡qué ordenado!». ¿Qué hace? (ironía: dice lo contrario)",
            svg=fig_choque),
        "La idea detrás de la imagen": dict(
            corto="lo concreto que representa una idea",
            d="Una imagen, una metáfora o una alegoría ponen algo concreto en lugar de una idea. Para "
              "leerlas se arma la equivalencia: esto del texto representa aquello. En una alegoría, cada "
              "pieza tiene su pareja.",
            f="imagen concreta = idea   (pieza por pieza)",
            ej="«Mi cuarto es un museo de las cosas que no termino»: el museo representa la pila de "
               "proyectos a medias.",
            ojo="leer la imagen al pie de la letra o quedarse con una sola pieza. Si una pieza queda sin "
                "pareja, la equivalencia está mal armada.",
            chequeo="En «el tiempo es un ladrón», ¿qué representa el ladrón? (que el tiempo se lleva cosas sin avisar)",
            svg=fig_equivalencia),
    },
    vocab=[("Intención", "lo que el texto busca en quien lo lee"),
           ("Persuadir", "llevar a alguien a creer o hacer algo"),
           ("Voz", "quién habla en el texto"),
           ("Autoridad", "experto que se cita para respaldar"),
           ("Sesgo", "inclinación hacia un lado"),
           ("Ironía", "decir lo contrario de lo que se piensa"),
           ("Sarcasmo", "ironía que busca herir a alguien"),
           ("Alegoría", "historia donde cada pieza representa algo"),
           ("Metáfora", "nombrar una idea con una imagen")]),

 6: dict(
    titulo="Lo que un texto defiende",
    centro=("Argumentar", "defender una idea, la tesis, con razones que la sostienen", fig_torre),
    centro_ej="«El colegio debería abrir la biblioteca los sábados» (tesis), «porque muchos no tienen "
              "dónde estudiar en la casa» (razón).",
    centro_ojo="una razón que no se conecta con la tesis no la sostiene, por cierta que sea.",
    centro_chequeo="«Llevemos termo: así no compramos botellas». ¿Tesis y razón? (tesis: llevar termo; razón: no comprar botellas)",
    ideas={
        "Una sola línea: qué defiende": dict(
            corto="la tesis en una sola frase",
            d="La tesis es la idea que el autor defiende en todo el texto. Escríbela en una sola línea "
              "con tus palabras y después busca dónde la dice o la deja ver el texto. Si varios casos "
              "apuntan a lo mismo, eso es la tesis.",
            f="«El autor defiende que…» + una sola línea",
            ej="un texto cuenta que una tía dejó el carro, que el barrio pintó ciclorrutas y que los "
               "niños van en bici al colegio: defiende que la ciudad cambia cuando cambian los hábitos.",
            ojo="confundir el tema («habla de la bicicleta») con la tesis («defiende que…»). La tesis "
                "siempre toma partido.",
            chequeo="«Este texto habla del celular». ¿Es una tesis? (no: es el tema; falta qué defiende)",
            svg=fig_una_linea),
        "Qué se cae si quito esto": dict(
            corto="la prueba de quitar una parte",
            d="Para saber para qué sirve un ejemplo, una cita o un párrafo, tápalo y mira qué le pasa al "
              "argumento: si la tesis queda sin apoyo, esa parte la sostenía. También sirve para "
              "encontrar las dos mitades de una paradoja.",
            f="quito la parte → ¿la tesis sigue en pie?",
            ej="en una charla sobre no dejar todo para última hora, la expositora cuenta la noche que no "
               "durmió por un trabajo. Sin esa historia, la idea pierde el caso que la vuelve creíble.",
            ojo="creer que todo lo que se puede quitar es relleno. Un ejemplo, si se cae, a veces se "
                "lleva el argumento.",
            chequeo="Si quitas una frase y el texto dice exactamente lo mismo, ¿qué función tenía? (poca: adornaba)",
            svg=fig_jenga),
        "Dice una cosa y hace la contraria": dict(
            corto="el choque entre lo dicho y lo hecho",
            d="Un texto, o alguien dentro de él, puede predicar una cosa y hacer la contraria: pedir "
              "silencio a gritos o celebrar la originalidad copiando. Detectar el choque es ver la "
              "ironía; ponerle nombre a lo criticado es entenderla.",
            f="dice A · hace lo contrario de A → ¿qué se critica?",
            ej="un profesor grita «¡aquí no se grita!». Lo que dice y lo que hace chocan: ahí está la "
               "ironía.",
            ojo="tomarlo como un error del autor. Casi siempre el choque está puesto a propósito para "
                "criticar algo.",
            chequeo="Una campaña contra el plástico reparte volantes plastificados. ¿Qué choca? (lo que pide contra lo que hace)",
            svg=fig_silencio),
        "Cómo llega el texto hasta ahí": dict(
            corto="el camino del texto hasta su conclusión",
            d="Un texto llega a su conclusión paso a paso: presenta un caso, descarta razones, agrega "
              "otra y cierra. Seguir el hilo es nombrar qué pasa en cada nudo. La conclusión correcta "
              "sale de ese camino.",
            f="nudo 1 → nudo 2 → nudo 3 → conclusión",
            ej="una carta cuenta que el equipo perdió, descarta que fuera mala suerte y termina en que "
               "faltó entrenar: cada paso empuja hacia la conclusión.",
            ojo="saltar a la conclusión que suena más bonita. Si no sale de los pasos del texto, es "
                "tuya, no del autor.",
            chequeo="Un texto va de «antes pensaba» a «hasta que» y a «ahora sé». ¿Dónde está la conclusión? (en «ahora sé»)",
            svg=fig_camino),
    },
    vocab=[("Tesis", "la idea que el autor defiende"),
           ("Argumento", "razón que sostiene una tesis"),
           ("Evidencia", "dato o caso que respalda una razón"),
           ("Conclusión", "a donde llega el texto"),
           ("Contraargumento", "razón en contra de la tesis"),
           ("Paradoja", "dos verdades que tiran para lados opuestos"),
           ("Ironía", "decir o mostrar lo contrario a propósito"),
           ("Contradicción", "afirmar dos cosas que no pueden ser a la vez"),
           ("Inferir", "sacar una conclusión de las pistas")]),
}
