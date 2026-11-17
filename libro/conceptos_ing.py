"""Conceptualización de Inglés (ver conceptos.py, conceptos_area.py y el modelo conceptos_mate.py).

En Inglés cada misión es una parte del examen Saber 11 (M1 Partes 1 y 2 · M2 Parte 3 · M3 Parte 4 ·
M4 Parte 5 · M5 Parte 6 · M6 Parte 7). Aquí el «concepto» es la estrategia de la parte y el saber
gramatical o léxico que pide: cómo se arma una descripción, la clase de pregunta, los tiempos y sus
marcadores, las preposiciones que van pegadas, los conectores, la palabra ancla, la paráfrasis,
la inferencia, el sentido figurado y las palabras que andan juntas. El vocabulario va en inglés
con su significado en español; las definiciones y el resto de la tarjeta, en español, con ejemplos
cortos en inglés.

Fuentes: plan_ing.py (MISIONES: parte, pasos, instala, ojo; TALLER_TODO: el contexto de las 127
tarjetas; BANCO: las preguntas de entrenamiento; NO_ES_TU_FUERTE: lo que necesita el profe que no
es del área) y los módulos ing1.py … ing6.py (bancos de palabras, avisos y textos del libro).

Los ejemplos son propios: no usan las palabras del banco de la Parte 1 (Technician, Factory, Nurse,
Driver, Volunteer, Artist, Passenger, Baker, Lecture hall, Laboratory, Student, Library, Exam,
Seminar, ID card, Bookshop), ni los avisos, diálogos, textos (Karol G, Spider-Verse, AI in the
Classroom, Public Protest, TWICE, Nairo, Photosynthesis, Street Music, An Unexpected Adventure,
Debating in Class, A Late Visitor) ni las opciones del taller y del entrenamiento.
"""
from conceptos_figs import *  # noqa: F401,F403  (colores y lupa)
from conceptos_figs import _svg, _t, _caja, _flecha, _tarjeta, _bien, _mal, _claro  # el * no trae los _


def _otro(c):
    """Un segundo acento que no se confunda con el color de la estrategia."""
    return MORADO if c.upper() == ORO else ORO


def _burbuja(x, y, w, h, texto, c, size=20, cola="izq", fondo="#fff", trazo=3, guion=""):
    """Burbuja de diálogo con su colita abajo (a la izquierda o a la derecha)."""
    cx = x + 30 if cola == "izq" else x + w - 30
    d = f' stroke-dasharray="{guion}"' if guion else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fondo}" stroke="{c}" stroke-width="{trazo}"{d}/>'
            f'<polygon points="{cx-8},{y+h-2} {cx+10},{y+h-2} {cx-4},{y+h+16}" fill="{fondo}" stroke="{c}" stroke-width="{trazo}" stroke-linejoin="round"/>'
            f'<rect x="{cx-10}" y="{y+h-6}" width="22" height="6" fill="{fondo}"/>'
            + _t(x + w / 2, y + h / 2 + size * 0.35, texto, size, TINTA, "middle", "600"))


def _persona(x, y, col, k=1.0):
    return (f'<circle cx="{x}" cy="{y}" r="{14*k}" fill="{_claro(col, .7)}" stroke="{TINTA}" stroke-width="2.5"/>'
            f'<path d="M{x-22*k} {y+52*k} Q{x-22*k} {y+18*k} {x} {y+18*k} Q{x+22*k} {y+18*k} {x+22*k} {y+52*k} Z" '
            f'fill="{_claro(col, .7)}" stroke="{TINTA}" stroke-width="2.5"/>')


# ══════════════════════ figuras · Misión 1 (Partes 1 y 2) ══════════════════════
def fig_c1(c):
    """Centro M1: la lupa sobre la pista que decide."""
    s = (f'<rect x="30" y="40" width="300" height="150" rx="14" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(50, 86, "a person who looks", 22, TINTA, w="600") + _t(50, 152, "after your", 22, TINTA, w="600")
         + _t(160, 152, "teeth", 22, c)
         + f'<circle cx="186" cy="145" r="33" fill="#fff" fill-opacity=".25" stroke="{c}" stroke-width="6"/>'
         f'<line x1="162" y1="169" x2="128" y2="206" stroke="{c}" stroke-width="10" stroke-linecap="round"/>'
         + _flecha(230, 226, 284, 226, c, 4)
         + _tarjeta(290, 200, 110, 50, "dentist", c, 22, _claro(c, .9)))
    return _svg(s, "Una lupa sobre la palabra teeth en la descripción: es un dentist")


def fig_oficio(c):
    """El verbo (o la cosa) más -er, -or, -ist, -ian da quien lo hace."""
    s = ""
    for k, (base, suf) in enumerate((("teach", "er"), ("sail", "or"), ("piano", "ist"), ("magic", "ian"))):
        y = 70 + 60 * k
        s += (_t(150, y, base, 24, TINTA, "end", "600") + _flecha(170, y - 8, 236, y - 8, GRIS, 3.5)
              + _t(256, y, f'{base}<tspan fill="{c}">{suf}</tspan>', 24, TINTA, w="700"))
    return _svg(s, "teach da teacher, sail da sailor, piano da pianist, magic da magician")


def fig_embudo(c):
    """Cada pista tacha opciones: el embudo."""
    s = f'<polygon points="60,90 360,90 240,200 240,250 180,250 180,200" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="2.5"/>'
    for x, w, pal, tachada in ((70, 46, "cook", True), (150, 64, "cinema", True),
                               (245, 74, "hospital", True), (345, 84, "pharmacy", False)):
        s += _t(x, 68, pal, 20, TINTA if not tachada else GRIS, "middle", "600")
        if tachada:
            s += f'<line x1="{x-w/2}" y1="62" x2="{x+w/2}" y2="62" stroke="{ROJO}" stroke-width="3"/>'
    s += (_t(210, 120, "1 · un lugar", 18, TINTA, "middle", "600")
          + _t(210, 158, "2 · buy medicine", 18, TINTA, "middle", "600")
          + _t(210, 284, "pharmacy", 22, c, "middle"))
    return _svg(s, "Un embudo: cada pista deja pasar menos palabras hasta que queda pharmacy")


def fig_aviso_lugar(c):
    """Un aviso y el lugar donde estaría: el andén."""
    s = (f'<rect x="60" y="40" width="300" height="80" rx="10" fill="{_claro(c, .9)}" stroke="{TINTA}" stroke-width="3"/>'
         + _t(210, 92, "Mind the gap", 32, TINTA, "middle")
         + f'<rect x="40" y="196" width="170" height="44" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="236" y="150" width="164" height="90" rx="10" fill="{_claro(c, .75)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="256" y="166" width="40" height="30" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
         f'<rect x="312" y="166" width="40" height="30" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
         + _flecha(223, 290, 223, 248, ORO, 4) + _t(236, 284, "the gap", 20, ORO)
         + _t(125, 226, "andén", 20, TINTA, "middle") + _t(320, 228, "tren", 20, TINTA, "middle"))
    return _svg(s, "El aviso Mind the gap junto al espacio entre el andén y el tren")


def fig_quien(c):
    """Quién escribe el aviso y qué quiere."""
    s = (f'<rect x="40" y="60" width="130" height="200" rx="6" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="3"/>'
         f'<circle cx="150" cy="170" r="7" fill="{TINTA}"/>'
         f'<rect x="50" y="96" width="110" height="44" rx="6" fill="#fff" stroke="{c}" stroke-width="3"/>'
         + _t(105, 117, "STAFF", 18, TINTA, "middle") + _t(105, 135, "ONLY", 18, TINTA, "middle")
         + _tarjeta(200, 80, 200, 56, "escribe: el dueño", c)
         + _tarjeta(200, 164, 200, 56, "quiere: prohibir", c))
    return _svg(s, "Una puerta con el aviso Staff only: lo escribe el dueño y quiere prohibir la entrada")


# ══════════════════════ figuras · Misión 2 (Parte 3) ══════════════════════
def fig_c2(c):
    """Centro M2: la respuesta que le contesta a la persona."""
    s = (_burbuja(20, 30, 300, 56, "Are you coming to the party?", TINTA, 20)
         + _burbuja(100, 120, 300, 56, "Sorry, I have to study.", c, 20, "der")
         + _burbuja(160, 210, 240, 50, "I love parties!", GRIS, 20, "der", guion="7 6")
         + _bien(58, 148) + _mal(118, 222))
    return _svg(s, "Una pregunta y dos respuestas: la que le contesta a la persona y la que solo repite la palabra")


def fig_tipo(c):
    """Auxiliar al comienzo: sí o no. Wh- al comienzo: un dato."""
    s = ""
    for k, (preg, resp) in enumerate((("Do you like rice?", "sí / no"), ("Where is the bank?", "un lugar"),
                                      ("What time is it?", "una hora"))):
        y = 40 + 78 * k
        col = c if k == 0 else ORO
        s += (_tarjeta(20, y, 230, 54, preg, TINTA, 20)
              + _flecha(258, y + 27, 298, y + 27, col, 4)
              + _tarjeta(304, y, 100, 54, resp, col, 20, _claro(col, .9)))
    return _svg(s, "Tres preguntas: la que empieza por Do pide sí o no; las que empiezan por Where y What piden un dato")


def fig_pedido(c):
    """Pedido, ofrecimiento y opinión: lo que en verdad me piden."""
    s = ""
    for k, (preg, que) in enumerate((("Could you…?", "un pedido"), ("Would you like…?", "una oferta"),
                                     ("Do you think…?", "tu opinión"))):
        y = 30 + 86 * k
        s += (_burbuja(20, y, 200, 52, preg, c, 21)
              + _flecha(232, y + 26, 268, y + 26, GRIS, 3.5)
              + _t(280, y + 34, que, 22, c))
    return _svg(s, "Could you pide un favor, Would you like ofrece algo y Do you think pide una opinión")


def fig_tiempo(c):
    """Did…? viaja al pasado; la respuesta se queda allá."""
    s = (f'<line x1="30" y1="170" x2="390" y2="170" stroke="{TINTA}" stroke-width="3"/>'
         f'<rect x="30" y="150" width="200" height="40" fill="{_claro(c, .88)}"/>'
         f'<line x1="30" y1="170" x2="390" y2="170" stroke="{TINTA}" stroke-width="3"/>'
         f'<circle cx="140" cy="170" r="10" fill="{c}"/><circle cx="320" cy="170" r="10" fill="{TINTA}"/>'
         + _t(140, 216, "yesterday", 20, c, "middle") + _t(320, 216, "ahora", 20, TINTA, "middle")
         + f'<path d="M318 140 Q230 50 150 140" fill="none" stroke="{c}" stroke-width="4"/>'
         + _flecha(158, 128, 148, 142, c, 4)
         + _t(232, 78, "Did you…?", 22, c, "middle")
         + _t(140, 262, "Yes, I did.", 22, TINTA, "middle"))
    return _svg(s, "Una línea de tiempo: Did you…? lleva la pregunta a ayer y la respuesta va en pasado")


def _cara(x, y, col, feliz):
    boca = (f'M{x-22} {y+10} Q{x} {y+32} {x+22} {y+10}' if feliz else f'M{x-22} {y+26} Q{x} {y+6} {x+22} {y+26}')
    return (f'<circle cx="{x}" cy="{y}" r="50" fill="{_claro(col, .8)}" stroke="{TINTA}" stroke-width="3"/>'
            f'<circle cx="{x-17}" cy="{y-12}" r="5" fill="{TINTA}"/><circle cx="{x+17}" cy="{y-12}" r="5" fill="{TINTA}"/>'
            f'<path d="{boca}" fill="none" stroke="{TINTA}" stroke-width="4" stroke-linecap="round"/>')


def fig_reaccion(c):
    """Una noticia buena y una mala: la reacción va con la noticia."""
    s = (_t(110, 58, "buena noticia", 18, GRIS, "middle", "600") + _t(310, 58, "mala noticia", 18, GRIS, "middle", "600")
         + _cara(110, 140, ORO, True) + _cara(310, 140, AZUL if c.upper() == ORO else c, False)
         + _t(110, 230, "That's great!", 22, TINTA, "middle") + _t(310, 230, "Oh no!", 22, TINTA, "middle"))
    return _svg(s, "Una cara feliz dice That's great y una triste dice Oh no")


# ══════════════════════ figuras · Misión 3 (Parte 4) ══════════════════════
def fig_c3(c):
    """Centro M3: las vecinas del espacio dan la pista."""
    s = (_tarjeta(30, 100, 70, 50, "She", c, 22, _claro(c, .9))
         + f'<rect x="114" y="100" width="110" height="50" rx="10" fill="#fff" stroke="{TINTA}" stroke-width="3" stroke-dasharray="8 6"/>'
         + _t(169, 133, "?", 26, TINTA, "middle")
         + _tarjeta(238, 100, 150, 50, "her bike", c, 22, _claro(c, .9))
         + _t(210, 196, "to school every day.", 22, TINTA, "middle", "600")
         + f'<path d="M65 96 Q100 50 150 94" fill="none" stroke="{ORO}" stroke-width="3.5"/>'
         + _flecha(140, 82, 152, 96, ORO, 3.5)
         + f'<path d="M300 96 Q250 50 192 94" fill="none" stroke="{ORO}" stroke-width="3.5"/>'
         + _flecha(204, 82, 192, 96, ORO, 3.5)
         + _t(210, 258, "falta un verbo, en presente, con she", 19, TINTA, "middle", "600"))
    return _svg(s, "Una oración con un espacio: las palabras vecinas dicen qué pieza falta")


def fig_reloj(c):
    """El reloj del texto: las marcas de pasado."""
    s = (f'<rect x="30" y="150" width="290" height="50" fill="{_claro(c, .86)}"/>'
         f'<line x1="30" y1="175" x2="390" y2="175" stroke="{TINTA}" stroke-width="3"/>'
         f'<line x1="330" y1="160" x2="330" y2="190" stroke="{TINTA}" stroke-width="4"/>'
         + _t(330, 225, "hoy", 20, TINTA, "middle")
         + _t(80, 136, "in 2019", 18, c, "middle") + _t(180, 136, "last year", 18, c, "middle")
         + _t(270, 136, "2 days ago", 18, c, "middle")
         + _t(160, 252, "won · took · wrote · ate", 20, TINTA, "middle")
         + f'<circle cx="360" cy="72" r="30" fill="#fff" stroke="{TINTA}" stroke-width="3"/>'
         f'<path d="M360 72 L360 52 M360 72 L374 80" stroke="{c}" stroke-width="4" stroke-linecap="round"/>')
    return _svg(s, "Una línea de tiempo con in 2019, last year y 2 days ago: todo eso es pasado")


def fig_forma(c):
    """Was con uno, were con varios."""
    s = (_t(100, 52, "una persona o cosa", 18, GRIS, "middle", "600") + _t(310, 52, "varias", 18, GRIS, "middle", "600")
         + _persona(100, 100, c)
         + _persona(270, 100, ORO) + _persona(310, 100, ORO) + _persona(350, 100, ORO)
         + _tarjeta(50, 190, 100, 54, "was", c, 26, _claro(c, .9))
         + _tarjeta(260, 190, 100, 54, "were", ORO, 26, _claro(ORO, .9)))
    return _svg(s, "Una persona va con was; varias personas van con were")


def fig_prep(c):
    """in, on, at: cómo es el lugar."""
    s = (
        # in: la pelota dentro de una caja transparente
        f'<circle cx="75" cy="175" r="16" fill="{ORO}"/>'
        + _caja(30, 140, 90, 70, 22, "#fff", _claro(c, .7), _claro(c, .9)).replace('fill="#fff"', 'fill="#fff" fill-opacity=".45"', 1)
        + _t(75, 252, "in", 28, c, "middle")
        # on: la pelota encima
        + _caja(160, 140, 90, 70, 22, "#fff", _claro(c, .7), _claro(c, .9))
        + f'<circle cx="214" cy="112" r="16" fill="{ORO}"/>'
        + _t(205, 252, "on", 28, c, "middle")
        # at: un punto en el mapa
        + f'<path d="M335 200 C305 160 305 118 335 118 C365 118 365 160 335 200 Z" fill="{_claro(c, .8)}" stroke="{TINTA}" stroke-width="2.5"/>'
        f'<circle cx="335" cy="146" r="10" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
        f'<ellipse cx="335" cy="206" rx="30" ry="7" fill="none" stroke="{TINTA}" stroke-width="2"/>'
        + _t(335, 252, "at", 28, c, "middle")
        + _t(210, 56, "espacio · superficie · punto", 20, TINTA, "middle"))
    return _svg(s, "In para algo dentro, on para algo encima, at para un punto")


def fig_conector(c):
    """El conector dice la relación entre dos ideas."""
    s = (_tarjeta(14, 60, 160, 56, "I was tired,", TINTA, 20)
         + _tarjeta(246, 60, 160, 56, "I went to bed.", TINTA, 20)
         + f'<line x1="174" y1="88" x2="246" y2="88" stroke="{c}" stroke-width="4"/>'
         + f'<circle cx="210" cy="88" r="26" fill="{_claro(c, .85)}" stroke="{c}" stroke-width="3"/>'
         + _t(210, 96, "so", 22, c, "middle"))
    for k, (con, rel) in enumerate((("because", "causa"), ("so", "consecuencia"), ("but", "contraste"))):
        x = 20 + 130 * k
        s += (f'<rect x="{x}" y="170" width="120" height="70" rx="12" fill="#fff" stroke="{c if k == 1 else LINEA}" stroke-width="3"/>'
              + _t(x + 60, 198, con, 21, c, "middle") + _t(x + 60, 226, rel, 18, TINTA, "middle", "600"))
    return _svg(s, "Dos ideas unidas por so; abajo, because da la causa, so la consecuencia y but el contraste")


# ══════════════════════ figuras · Misión 4 (Parte 5) ══════════════════════
def fig_c4(c):
    """Centro M4: la respuesta está escrita; se señala la frase."""
    s = f'<rect x="150" y="36" width="230" height="230" rx="10" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
    for k, w in enumerate((190, 170, 190, 150, 180, 120)):
        y = 60 + 32 * k
        if k == 3:
            s += f'<rect x="166" y="{y-4}" width="{w+16}" height="24" rx="5" fill="{_claro(c, .8)}" stroke="{c}" stroke-width="2.5"/>'
        s += f'<rect x="174" y="{y}" width="{w}" height="14" rx="5" fill="{LINEA}"/>'
    s += (_burbuja(20, 100, 96, 70, "?", c, 40)
          + _flecha(120, 166, 160, 162, c, 4)
          + _t(265, 290, "la frase que responde", 18, TINTA, "middle", "600"))
    return _svg(s, "Una pregunta y una página: se señala la frase que la responde")


def fig_ancla(c):
    """La palabra ancla: en la pregunta y en el texto."""
    s = (f'<circle cx="70" cy="70" r="14" fill="none" stroke="{c}" stroke-width="6"/>'
         f'<line x1="70" y1="84" x2="70" y2="200" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
         f'<line x1="44" y1="110" x2="96" y2="110" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
         f'<path d="M30 168 Q36 214 70 214 Q104 214 110 168" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
         f'<rect x="150" y="60" width="252" height="160" rx="12" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(165, 100, "Ana studied", 21, TINTA, w="600")
         + f'<rect x="282" y="78" width="70" height="30" rx="6" fill="{_claro(c, .8)}" stroke="{c}" stroke-width="2.5"/>'
         + _t(317, 100, "music", 21, TINTA, "middle")
         + _t(165, 140, "in Lima before", 21, TINTA, w="600") + _t(165, 180, "moving to Quito.", 21, TINTA, w="600")
         + f'<path d="M84 70 Q190 30 290 78" fill="none" stroke="{c}" stroke-width="3" stroke-dasharray="7 6"/>'
         + _t(210, 262, "Where did Ana study music?", 20, c, "middle"))
    return _svg(s, "Un ancla amarrada a la palabra music, que está en la pregunta y en el texto")


def fig_cifra(c):
    """Cada número con su dueño: etiquetas amarradas."""
    s = ""
    for k, (num, duen) in enumerate((("1998", "año en que se fundó"), ("300", "trabajadores"), ("15", "países"))):
        y = 50 + 76 * k
        s += (f'<polygon points="40,{y} 130,{y} 150,{y+24} 130,{y+48} 40,{y+48}" fill="{_claro(c, .88)}" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<circle cx="130" cy="{y+24}" r="5" fill="#fff" stroke="{TINTA}" stroke-width="2"/>'
              + _t(84, y + 33, num, 24, TINTA, "middle")
              + f'<path d="M135 {y+24} Q170 {y+44} 205 {y+24}" fill="none" stroke="{GRIS}" stroke-width="2.5"/>'
              + _t(214, y + 32, duen, 20, c))
    return _svg(s, "Tres etiquetas: 1998 con el año en que se fundó, 300 con trabajadores y 15 con países")


def fig_parafrasis(c):
    """La misma idea con otras palabras."""
    s = (f'<circle cx="150" cy="150" r="100" fill="{_claro(c, .9)}" stroke="{c}" stroke-width="3"/>'
         f'<circle cx="270" cy="150" r="100" fill="{_claro(_otro(c), .9)}" fill-opacity=".7" stroke="{_otro(c)}" stroke-width="3"/>'
         + _t(100, 40, "texto", 20, c, "middle") + _t(320, 40, "pregunta", 20, _otro(c), "middle")
         + _t(100, 158, "began", 24, TINTA, "middle") + _t(320, 158, "started", 24, TINTA, "middle")
         + _t(210, 142, "misma", 18, TINTA, "middle", "600") + _t(210, 166, "idea", 18, TINTA, "middle", "600"))
    return _svg(s, "Dos círculos que se cruzan: began en el texto y started en la pregunta dicen la misma idea")


def fig_filtro(c):
    """Dos preguntas a cada opción: ¿está en el texto? ¿responde?"""
    s = (f'<rect x="156" y="60" width="16" height="200" rx="6" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="2"/>'
         f'<rect x="286" y="60" width="16" height="200" rx="6" fill="{_claro(c, .7)}" stroke="{TINTA}" stroke-width="2"/>'
         + _t(164, 44, "¿está?", 20, c, "middle") + _t(294, 44, "¿responde?", 20, c, "middle"))
    for k, (hasta, ok) in enumerate(((148, False), (278, False), (360, True))):
        y = 100 + 70 * k
        s += (f'<circle cx="50" cy="{y}" r="18" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
              + _t(50, y + 7, str(k + 1), 20, TINTA, "middle")
              + _flecha(72, y, hasta, y, GRIS, 3.5))
        if not ok:
            s += _mal(hasta - 40, y - 34)
    s += _bien(368, 238)
    return _svg(s, "Tres opciones pasan por dos filtros: solo la que está en el texto y responde llega al final")


# ══════════════════════ figuras · Misión 5 (Parte 6) ══════════════════════
def _nube(x, y, col):
    return (f'<g fill="{col}" stroke="{TINTA}" stroke-width="2.5">'
            f'<circle cx="{x-30}" cy="{y+8}" r="24"/><circle cx="{x+30}" cy="{y+8}" r="24"/>'
            f'<circle cx="{x}" cy="{y-8}" r="32"/></g>'
            f'<rect x="{x-52}" y="{y+6}" width="104" height="26" fill="{col}"/>'
            f'<line x1="{x-54}" y1="{y+32}" x2="{x+54}" y2="{y+32}" stroke="{TINTA}" stroke-width="2.5"/>')


def fig_c5(c):
    """Centro M5: nubes + paraguas → va a llover."""
    s = (_nube(100, 90, "#E3E7EE")
         + _t(100, 160, "dark clouds", 20, TINTA, "middle")
         + _t(200, 104, "+", 34, TINTA, "middle")
         + f'<path d="M250 110 Q300 40 350 110 Z" fill="{_claro(c, .8)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M300 110 L300 150 Q300 162 288 160" fill="none" stroke="{TINTA}" stroke-width="3.5" stroke-linecap="round"/>'
         + _t(300, 196, "umbrella", 20, TINTA, "middle")
         + _flecha(210, 214, 210, 244, c, 4)
         + _t(210, 280, "deja entender: va a llover", 21, c, "middle"))
    return _svg(s, "Nubes oscuras más un paraguas dejan entender que va a llover")


def fig_inferir(c):
    """La calle mojada y los paraguas que se cierran: acaba de llover."""
    s = (f'<line x1="30" y1="220" x2="390" y2="220" stroke="{TINTA}" stroke-width="3"/>'
         f'<ellipse cx="110" cy="236" rx="60" ry="10" fill="{_claro(c, .7)}"/>'
         f'<ellipse cx="300" cy="238" rx="70" ry="11" fill="{_claro(c, .7)}"/>'
         f'<line x1="210" y1="80" x2="210" y2="206" stroke="{TINTA}" stroke-width="4" stroke-linecap="round"/>'
         f'<path d="M210 80 L192 170 L228 170 Z" fill="{_claro(c, .8)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M210 206 Q210 216 200 214" fill="none" stroke="{TINTA}" stroke-width="4" stroke-linecap="round"/>')
    for x, y in ((236, 184), (186, 192), (232, 204)):
        s += f'<path d="M{x} {y} q-5 9 0 12 q5 -3 0 -12 Z" fill="{c}"/>'
    s += (_t(70, 70, "lo que veo", 18, GRIS, w="600") + _t(70, 96, "wet streets", 20, TINTA)
          + _t(250, 70, "lo que se sigue", 18, GRIS, w="600") + _t(250, 96, "acaba de llover", 20, c)
          + _t(210, 280, "con prueba, no invento", 20, TINTA, "middle"))
    return _svg(s, "Un paraguas cerrado que gotea sobre una calle con charcos: se infiere que acaba de llover")


def fig_proposito(c):
    """Cada detalle apoya una idea: ¿para qué lo pone el autor?"""
    s = (f'<circle cx="210" cy="80" r="40" fill="{_claro(ORO, .8)}" stroke="{TINTA}" stroke-width="3"/>'
         f'<rect x="196" y="120" width="28" height="18" fill="{_claro(TINTA, .7)}" stroke="{TINTA}" stroke-width="2"/>'
         + _t(210, 88, "idea", 22, TINTA, "middle") + _t(262, 58, "¿para qué?", 20, c))
    for k, txt in enumerate(("un ejemplo", "un dato", "una cita")):
        x = 20 + 133 * k
        s += (_tarjeta(x, 200, 115, 50, txt, c, 19)
              + _flecha(x + 57, 196, 210 + (k - 1) * 10, 146, GRIS, 3))
    return _svg(s, "Un ejemplo, un dato y una cita apuntan a la idea que el autor quiere apoyar")


def fig_figurado(c):
    """My room is a jungle: literal no, figurado sí."""
    s = (_t(210, 44, "«My room is a jungle»", 22, TINTA, "middle")
         + f'<rect x="30" y="66" width="170" height="150" rx="12" fill="#fff" stroke="{LINEA}" stroke-width="3"/>'
         f'<rect x="220" y="66" width="170" height="150" rx="12" fill="#fff" stroke="{c}" stroke-width="3"/>')
    for x, h in ((70, 80), (115, 110), (160, 70)):
        s += (f'<polygon points="{x-26},200 {x+26},200 {x},{200-h}" fill="{_claro(VERDE, .7)}" stroke="{TINTA}" stroke-width="2"/>')
    for x, y, w, h, a in ((250, 170, 50, 22, -14), (300, 150, 40, 30, 10), (320, 190, 56, 16, -6),
                          (255, 110, 30, 30, 20), (340, 100, 34, 24, -18)):
        s += (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{_claro(c, .75)}" stroke="{TINTA}" '
              f'stroke-width="2" transform="rotate({a} {x + w/2} {y + h/2})"/>')
    s += (_mal(168, 76) + _bien(350, 80)
          + _t(115, 250, "literal", 20, GRIS, "middle") + _t(305, 250, "muy desordenado", 20, c, "middle"))
    return _svg(s, "My room is a jungle: no hay árboles, el cuarto está muy desordenado")


def fig_frente(c):
    """Dos cosas en la balanza: en qué se parecen, en qué no, a cuál favorece."""
    s = (f'<polygon points="210,96 196,250 224,250" fill="{_claro(TINTA, .75)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<line x1="80" y1="110" x2="340" y2="86" stroke="{TINTA}" stroke-width="5" stroke-linecap="round"/>'
         f'<circle cx="210" cy="98" r="7" fill="{TINTA}"/>'
         f'<line x1="80" y1="110" x2="60" y2="170" stroke="{TINTA}" stroke-width="2"/><line x1="80" y1="110" x2="100" y2="170" stroke="{TINTA}" stroke-width="2"/>'
         f'<line x1="340" y1="86" x2="320" y2="146" stroke="{TINTA}" stroke-width="2"/><line x1="340" y1="86" x2="360" y2="146" stroke="{TINTA}" stroke-width="2"/>'
         f'<path d="M44 170 Q80 194 116 170 Z" fill="{_claro(c, .8)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M304 146 Q340 170 376 146 Z" fill="{_claro(ORO, .8)}" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<rect x="62" y="146" width="36" height="24" fill="#fff" stroke="{c}" stroke-width="2.5"/>'
         f'<rect x="324" y="118" width="32" height="28" rx="4" fill="#fff" stroke="{ORO}" stroke-width="2.5"/>'
         + _t(80, 216, "papel", 20, c, "middle") + _t(340, 194, "digital", 20, ORO, "middle")
         + _t(210, 282, "but · while · unlike · however", 20, TINTA, "middle"))
    return _svg(s, "Una balanza compara un libro de papel y uno digital")


# ══════════════════════ figuras · Misión 6 (Parte 7) ══════════════════════
def fig_c6(c):
    """Centro M6: la pista está cerca o lejos del espacio."""
    s = (_tarjeta(40, 50, 130, 40, "Yesterday", ORO, 20, _claro(ORO, .85))
         + f'<rect x="182" y="62" width="200" height="16" rx="6" fill="{LINEA}"/>'
         f'<rect x="40" y="112" width="342" height="16" rx="6" fill="{LINEA}"/>'
         f'<rect x="40" y="162" width="230" height="16" rx="6" fill="{LINEA}"/>'
         + _tarjeta(282, 150, 60, 40, "I", c, 20, _claro(c, .85))
         + f'<rect x="40" y="206" width="110" height="40" rx="8" fill="#fff" stroke="{TINTA}" stroke-width="3" stroke-dasharray="8 6"/>'
         + _t(95, 233, "?", 22, TINTA, "middle")
         + f'<rect x="162" y="218" width="140" height="16" rx="6" fill="{LINEA}"/>'
         + f'<path d="M40 76 C6 110 6 190 36 222" fill="none" stroke="{ORO}" stroke-width="4"/>'
         + _flecha(24, 206, 38, 224, ORO, 4)
         + _flecha(300, 194, 156, 222, c, 4)
         + _t(330, 252, "cerca", 20, c, "middle") + _t(40, 282, "lejos: el párrafo", 20, ORO))
    return _svg(s, "Un párrafo con un espacio: la pista está en la palabra de al lado o al comienzo del párrafo")


def fig_linea(c):
    """Los tiempos del relato en la línea."""
    s = (f'<line x1="20" y1="170" x2="395" y2="170" stroke="{TINTA}" stroke-width="3"/>'
         f'<circle cx="50" cy="170" r="9" fill="{GRIS}"/>' + _t(50, 206, "had left", 18, GRIS, "middle")
         + f'<path d="M100 170 q8 -12 16 0 t16 0 t16 0 t16 0 t16 0" fill="none" stroke="{c}" stroke-width="5"/>'
         + _t(156, 140, "was cooking", 18, c, "middle")
         + f'<path d="M188 150 L176 172 L190 172 L180 196" fill="none" stroke="{ORO}" stroke-width="4" stroke-linejoin="round"/>'
         + _t(186, 222, "rang", 18, ORO, "middle")
         + _flecha(244, 120, 352, 120, VERDE, 4) + _t(296, 104, "have lived since…", 18, VERDE, "middle")
         + f'<line x1="360" y1="150" x2="360" y2="190" stroke="{TINTA}" stroke-width="4"/>'
         + _t(360, 222, "ahora", 18, TINTA, "middle"))
    return _svg(s, "Una línea de tiempo con had left, was cooking interrumpido por rang y have lived since hasta ahora")


def fig_al_lado(c):
    """La palabra de al lado manda la forma: eslabones."""
    s = ""
    for k, (izq, der) in enumerate((("has", "written"), ("to", "write"), ("she", "writes"))):
        y = 44 + 80 * k
        s += (_tarjeta(30, y, 100, 50, izq, c, 22, _claro(c, .85))
              + f'<ellipse cx="152" cy="{y+25}" rx="18" ry="11" fill="none" stroke="{TINTA}" stroke-width="3.5"/>'
              f'<ellipse cx="178" cy="{y+25}" rx="18" ry="11" fill="none" stroke="{TINTA}" stroke-width="3.5"/>'
              + _tarjeta(200, y, 160, 50, der, TINTA, 22))
    return _svg(s, "Tres cadenas: has con written, to con write, she con writes")


def fig_colocacion(c):
    """make y do: dos telarañas."""
    s = ""
    for cx, verbo, arriba, abajo, col in ((110, "make", "a mistake", "a decision", c),
                                          (310, "do", "homework", "exercise", _otro(c))):
        s += (f'<line x1="{cx}" y1="116" x2="{cx}" y2="66" stroke="{col}" stroke-width="3"/>'
              f'<line x1="{cx}" y1="184" x2="{cx}" y2="226" stroke="{col}" stroke-width="3"/>'
              f'<circle cx="{cx}" cy="150" r="36" fill="{_claro(col, .85)}" stroke="{col}" stroke-width="3"/>'
              + _t(cx, 158, verbo, 22, TINTA, "middle")
              + _t(cx, 56, arriba, 20, TINTA, "middle", "600") + _t(cx, 252, abajo, 20, TINTA, "middle", "600"))
    s += _t(210, 140, "hacer", 20, GRIS, "middle") + _flecha(190, 152, 152, 152, GRIS, 3) + _flecha(230, 152, 268, 152, GRIS, 3)
    return _svg(s, "Make va con a mistake y a decision; do va con homework y exercise")


def fig_parrafo(c):
    """Cada párrafo con su nota del tiempo."""
    s = ""
    for k in range(3):
        y = 40 + 80 * k
        for j, w in enumerate((250, 220)):
            s += f'<rect x="30" y="{y + 18*j}" width="{w}" height="12" rx="5" fill="{LINEA}"/>'
        if k == 2:
            s += (f'<rect x="120" y="{y+30}" width="80" height="30" rx="6" fill="#fff" stroke="{TINTA}" '
                  f'stroke-width="3" stroke-dasharray="7 5"/>' + _t(160, y + 52, "?", 20, TINTA, "middle"))
        else:
            s += f'<rect x="30" y="{y + 36}" width="180" height="12" rx="5" fill="{LINEA}"/>'
        col = c if k == 2 else ORO
        s += (f'<rect x="296" y="{y-4}" width="100" height="56" fill="{_claro(col, .7)}" stroke="{TINTA}" '
              f'stroke-width="2" transform="rotate({-4 + 4*k} 346 {y+24})"/>'
              + _t(346, y + 31, "presente", 19, TINTA, "middle"))
    return _svg(s, "Tres párrafos con una nota adhesiva que dice presente: el espacio del tercero también va en presente")


# ══════════════════════ los datos de las seis misiones ══════════════════════
DATOS = {
    1: dict(
        titulo="La pista que decide",
        centro=("Leer por piezas", "una descripción o un aviso se desarma: qué es, qué hace y dónde pasa", fig_c1),
        centro_ej="«a person who looks after your teeth»: es una persona, cuida los dientes (teeth). Es un dentist.",
        centro_ojo="escribe la palabra antes de marcar la letra: así no te dejas llevar por el orden del banco.",
        centro_chequeo="«A machine that keeps food cold». ¿Cuál es la pista que decide? (keeps food cold: es un fridge)",
        ideas={
            "El verbo delata la palabra": dict(
                corto="el verbo dice quién es",
                d="En la descripción, el verbo dice qué hace la persona o para qué sirve la cosa. Del verbo sale la "
                  "palabra: muchos oficios son el verbo (o la cosa) más -er, -or, -ist o -ian.",
                f="teach → teacher · sail → sailor · piano → pianist",
                ej="«a person who sings in a band» → sing → singer.",
                ojo="no todos siguen la regla: cook (cocinar) da cook (cocinero). «Cooker» es la estufa.",
                chequeo="«This person paints houses or pictures». ¿Qué palabra es? (painter)",
                svg=fig_oficio),
            "Cada pista tacha opciones": dict(
                corto="persona, lugar o cosa; después el verbo",
                d="Cada pedazo de la descripción tacha palabras del banco: primero si es persona, lugar o cosa; "
                  "después el verbo; al final la pista fina («but», «without», «not») que separa a dos parecidas.",
                f="persona / lugar / cosa → verbo → pista fina",
                ej="«a place where you can buy medicine» tacha a las personas y deja lugares; «buy medicine» deja "
                   "pharmacy y saca a hospital.",
                ojo="«but» y «without» le dan la vuelta a la frase: «like a sofa, but for one person» no es sofa, "
                    "es armchair.",
                chequeo="«A place where you watch films on a big screen». ¿Persona, lugar o cosa? ¿Qué palabra? (lugar; cinema)",
                svg=fig_embudo),
            "¿Dónde estaría este aviso?": dict(
                corto="la palabra clave dice el lugar",
                d="Un aviso corto se entiende imaginando dónde está pegado. Sus palabras clave (platform, aisle, "
                  "check-in) dicen el lugar: una estación, un supermercado, un aeropuerto.",
                f="palabra clave → lugar → ¿qué pasa ahí?",
                ej="«Mind the gap between the train and the platform» → en una estación de metro o de tren.",
                ojo="una palabra sola engaña: comprueba que todo el aviso tenga sentido en ese lugar.",
                chequeo="«Quiet, please: exam in progress». ¿Dónde estaría? (en la puerta de un salón de un colegio)",
                svg=fig_aviso_lugar),
            "Quién me escribe y qué quiere": dict(
                corto="quién escribe y qué quiere",
                d="Todo aviso o mensaje lo escribe alguien que quiere algo: informar, pedir, prohibir, ofrecer o "
                  "vender. Primero quién lo escribe; después, qué quiere que yo haga.",
                f="quién escribe · qué quiere: informar, pedir, prohibir, vender",
                ej="«Staff only» lo escribe el dueño del lugar y prohíbe: si no trabajas ahí, no entras.",
                ojo="«Please» no siempre es un pedido amable: «Please do not feed the animals» es una prohibición.",
                chequeo="«Sale! 2 for 1 on all shoes». ¿Quién escribe y qué quiere? (la tienda; vender)",
                svg=fig_quien),
        },
        vocab=[("No entry", "prohibido entrar"),
               ("Staff only", "solo personal autorizado"),
               ("Exit", "salida"),
               ("Out of order", "fuera de servicio, dañado"),
               ("Wet floor", "piso mojado"),
               ("Sold out", "agotado"),
               ("Opening hours", "horario de atención"),
               ("Keep off the grass", "no pisar el césped"),
               ("Lecture", "clase magistral (no es «lectura»)")]),
    2: dict(
        titulo="Contéstale a la persona, no a la palabra",
        centro=("La respuesta natural", "la que le contesta a quien habla, no la que repite su palabra", fig_c2),
        centro_ej="—Are you coming to the party? —Sorry, I have to study. No dice «party», pero contesta: no va.",
        centro_ojo="si una opción repite la palabra de la frase, sospecha: suele hablar del tema sin contestar.",
        centro_chequeo="—Can I borrow your pen? ¿Cuál contesta: «Sure, here you are» o «I like pens»? (Sure, here you are)",
        ideas={
            "¿Qué clase de pregunta me hacen?": dict(
                corto="sí o no, o un dato",
                d="Si la pregunta empieza por un auxiliar (Is, Are, Do, Does, Can, Did) pide sí o no. Si empieza "
                  "por What, Where, When, Who o How much, pide un dato.",
                f="Do / Is / Can…? → sí o no   ·   Wh-…? → un dato",
                ej="«Where do you live?» pide un lugar (In Cali). «Do you live in Cali?» pide sí o no (Yes, I do).",
                ojo="a una pregunta de dato no se le contesta «Yes»: «What time is it?» no se responde «Yes, it is».",
                chequeo="«When does the bus leave?» ¿Pide sí o no, o un dato? (un dato: una hora)",
                svg=fig_tipo),
            "¿Qué me están pidiendo?": dict(
                corto="pedido, oferta u opinión",
                d="Algunas preguntas no buscan información: piden algo. Could you…? es un pedido; Would you like…? "
                  "es un ofrecimiento; Do you think…? pide tu opinión.",
                f="Could you…? pedido · Would you like…? oferta · Do you think…? opinión",
                ej="—Would you like some juice? —Yes, please. / No, thanks.",
                ojo="a un pedido se le contesta aceptando o negándose (Sure / Sorry, I can't), no con información "
                    "sobre el tema.",
                chequeo="«Could you open the window?» ¿Qué contestas? (Sure / Of course / Sorry, I can't)",
                svg=fig_pedido),
            "El tiempo del verbo manda": dict(
                corto="la respuesta va en el tiempo de la pregunta",
                d="La respuesta va en el mismo tiempo que la pregunta. Did…? y las marcas yesterday, last week o ago "
                  "piden pasado; Are you going to…? pide futuro.",
                f="Did you…? → Yes, I did. / No, I didn't.",
                ej="—Did you watch the match yesterday? —Yes, I did. It was amazing!",
                ojo="was y were van según quién: I, he, she, it → was; you, we, they → were.",
                chequeo="«What did you do last weekend?» ¿En qué tiempo va la respuesta? (pasado: I visited my cousins)",
                svg=fig_tiempo),
            "Reacciono a lo que me cuentan": dict(
                corto="noticia buena o mala: reacciono",
                d="Cuando alguien cuenta una noticia, una queja o una opinión, se reacciona a eso: con alegría, con "
                  "pena, de acuerdo o en desacuerdo. No se responde con un dato que nadie pidió.",
                f="buena noticia → That's great! · mala → Oh no! I'm sorry.",
                ej="—I passed my driving test! —Congratulations! That's great!",
                ojo="«Me too» va con frases afirmativas (I like it. —Me too); «Me neither», con negativas "
                    "(I don't like it. —Me neither).",
                chequeo="—I lost my phone this morning. ¿Qué reacción encaja? (Oh no! / I'm sorry to hear that)",
                svg=fig_reaccion),
        },
        vocab=[("Could you…?", "¿podrías…? (un pedido)"),
               ("Would you like…?", "¿quieres…? (un ofrecimiento)"),
               ("Sure / Of course", "claro, con gusto"),
               ("No, thanks", "no, gracias"),
               ("That's great!", "¡qué bien!"),
               ("I'm sorry to hear that", "qué pena oír eso"),
               ("I agree", "estoy de acuerdo"),
               ("Never mind", "no importa, tranquilo"),
               ("Me neither", "yo tampoco")]),
    3: dict(
        titulo="Escucha a los vecinos del espacio",
        centro=("La pieza que falta", "antes de mirar las opciones, decide qué clase de palabra falta", fig_c3),
        centro_ej="«She ___ her bike to school every day»: falta un verbo en presente con she. Es rides.",
        centro_ojo="no llenes por cómo suena: busca la pista en las palabras de al lado.",
        centro_chequeo="«They arrived ___ the airport late». ¿Falta un verbo, una preposición o un conector? (una preposición: at)",
        ideas={
            "El reloj del texto": dict(
                corto="las marcas de tiempo ponen el pasado",
                d="Cada texto tiene un reloj: si cuenta algo que ya pasó, los verbos van en pasado. Las marcas "
                  "(yesterday, last year, in 2019, ago) lo ponen. Los regulares terminan en -ed; los irregulares se "
                  "aprenden.",
                f="last year / in 2019 / ago → won, took, wrote, ate",
                ej="«Last year my brother ___ (win) a chess tournament» → won.",
                ojo="un irregular no lleva -ed: es took, no «taked»; wrote, no «writed».",
                chequeo="«Two days ago we ___ (eat) at my aunt's house». (ate)",
                svg=fig_reloj),
            "La forma que cabe": dict(
                corto="el sujeto y las vecinas mandan la forma",
                d="El sujeto manda la forma: was con I, he, she, it o una sola cosa; were con you, we, they o varias. "
                  "Y entre un artículo y un sustantivo va un adjetivo.",
                f="the boy was · the boys were · a beautiful day",
                ej="«My grandparents ___ very happy at the party» → were: el sujeto son dos personas.",
                ojo="el sujeto puede estar lejos: «The keys of the car ___ on the table» → were, porque manda keys, "
                    "no car.",
                chequeo="«It was a ___ day»: ¿beauty, beautiful o beautifully? (beautiful: va entre artículo y sustantivo)",
                svg=fig_forma),
            "La preposición viene pegada": dict(
                corto="se aprenden en pareja",
                d="Muchas palabras llevan siempre la misma preposición y no se deducen del español: se aprenden en "
                  "pareja. Las de lugar dependen de cómo es el sitio: in un espacio, on una superficie, at un punto.",
                f="afraid of · good at · interested in · in / on / at",
                ej="«She is interested ___ photography» → in. «I'm good ___ math» → at.",
                ojo="traducir del español engaña: «casarse con» es get married to, no «with».",
                chequeo="«The keys are ___ the table» y «the milk is ___ the fridge». (on; in)",
                svg=fig_prep),
            "El conector dice la relación": dict(
                corto="causa, consecuencia o contraste",
                d="El conector une dos ideas y dice cómo se relacionan: because da la causa, so la consecuencia, "
                  "but y although el contraste, and suma. Se tapa el espacio y se pregunta qué relación hay.",
                f="because causa · so consecuencia · but / although contraste",
                ej="«I was tired, ___ I went to bed early» → so: lo segundo es consecuencia de lo primero.",
                ojo="but y although dicen casi lo mismo, pero van en sitios distintos: «It was cold, but we swam» / "
                    "«Although it was cold, we swam».",
                chequeo="«We stayed home ___ it was raining». ¿Causa, consecuencia o contraste? (causa: because)",
                svg=fig_conector),
        },
        vocab=[("Blank", "espacio en blanco"),
               ("Clue", "pista"),
               ("Past simple", "pasado simple: played, went"),
               ("Irregular verb", "verbo que no hace el pasado con -ed"),
               ("Subject", "sujeto: quién hace la acción"),
               ("Preposition", "preposición: in, on, at, for…"),
               ("Because", "porque (da la causa)"),
               ("So", "así que (da la consecuencia)"),
               ("Although", "aunque (da el contraste)")]),
    4: dict(
        titulo="Lo que el texto dice, dato por dato",
        centro=("Lectura literal", "la respuesta está escrita en el texto: hay que encontrarla y comprobarla", fig_c4),
        centro_ej="«The museum opens at 9 a.m. and closes at 6 p.m. on weekdays». ¿A qué hora cierra entre semana? "
                  "La frase lo dice: 6 p.m.",
        centro_ojo="no respondas de memoria ni por lo que sabes del tema: responde con la frase del texto.",
        centro_chequeo="El texto dice «The festival started in 1998» y la pregunta, «When did it begin?». ¿Qué palabra cambió? (started → begin)",
        ideas={
            "La palabra ancla": dict(
                corto="la palabra que comparten pregunta y texto",
                d="La palabra ancla es la que comparten la pregunta y el texto: un nombre, una fecha, un lugar. Se "
                  "busca en el texto y se lee la oración completa donde está, y la de al lado.",
                f="pregunta → ancla → oración completa del texto",
                ej="«Where did Ana study music?» Ancla: music. El texto: «Ana studied music in Lima before moving to "
                   "Quito». Respuesta: in Lima.",
                ojo="el ancla puede cambiar de forma: study, studied, student. Búscala en todas sus formas.",
                chequeo="En «How long did the trip last?», ¿cuál es la palabra ancla? (the trip)",
                svg=fig_ancla),
            "Cada cifra tiene dueño": dict(
                corto="cada número amarrado a lo suyo",
                d="En un texto con muchos números, cada uno va con algo: un año, una edad, un precio, una cantidad. "
                  "Antes de responder se amarra cada número a su dueño.",
                f="1998 → se fundó · 300 → trabajadores · 15 → países",
                ej="«The company was founded in 1998 and now has 300 workers in 15 countries». ¿Cuántos trabajadores? "
                   "300, no 15.",
                ojo="los números en letras también cuentan: «twelve» y «a dozen» son 12; «the nineties», los años 90.",
                chequeo="«She was 19 when she won her first race in 2010». ¿Cuántos años tenía en 2010? (19)",
                svg=fig_cifra),
            "Lo dice con otras palabras": dict(
                corto="la misma idea, otra forma",
                d="La pregunta casi nunca copia el texto: dice lo mismo con otras palabras (sinónimos u otra "
                  "estructura). Hay que reconocer la misma idea aunque cambie la forma.",
                f="texto: began = pregunta: started",
                ej="texto: «The shop is closed on Sundays». Pregunta: «When can't you buy there?». Respuesta: on Sundays.",
                ojo="si una opción copia palabras del texto, compruébala: copiar no es lo mismo que responder.",
                chequeo="«Big» y «large», «buy» y «purchase». ¿Qué son? (palabras que dicen lo mismo: sinónimos)",
                svg=fig_parafrasis),
            "Es verdad, pero no responde": dict(
                corto="¿está en el texto? ¿responde?",
                d="Un distractor puede traer un dato que sí está en el texto, pero que no contesta lo que preguntan. "
                  "Cada opción pasa dos pruebas: ¿está en el texto? y ¿responde esta pregunta?",
                f="¿está en el texto? ✓ + ¿responde? ✓ = la correcta",
                ej="texto: «Leo lives in Bogotá and works in Chía». Pregunta: «Where does Leo work?». «In Bogotá» es "
                   "verdad, pero no responde.",
                ojo="una opción verdadera no es la correcta si contesta otra pregunta.",
                chequeo="El texto dice que María canta y estudia Medicina. Si preguntan qué estudia, ¿sirve «she sings»? (no)",
                svg=fig_filtro),
        },
        vocab=[("According to", "según"),
               ("Founded", "fundado, creado"),
               ("Took place", "se llevó a cabo, ocurrió"),
               ("Approximately", "aproximadamente, más o menos"),
               ("Million", "millón: 1.5 million = un millón y medio"),
               ("Former", "anterior, ex-"),
               ("Since", "desde"),
               ("Until", "hasta"),
               ("Dozen", "docena (12)")]),
    5: dict(
        titulo="Leer entre líneas, con la prueba en la mano",
        centro=("Inferir", "sacar lo que el texto deja entender, con una frase que lo pruebe", fig_c5),
        centro_ej="«Carla looked at the dark clouds and went back for her umbrella». No dice que va a llover, pero "
                  "lo deja entender.",
        centro_ojo="inferir no es inventar: si no puedes señalar la frase que lo prueba, es invento.",
        centro_chequeo="«Tom ate three plates of rice». ¿Qué se infiere: que tenía hambre o que odia el arroz? (que tenía hambre)",
        ideas={
            "Lo que el texto deja entender": dict(
                corto="la idea que se apoya en una frase",
                d="Inferir es sacar una idea que el texto no dice con todas las letras, pero que se apoya en lo que "
                  "sí dice. La prueba es poder señalar la frase.",
                f="lo que dice + lo que se sigue = inferencia (con prueba)",
                ej="«The streets were wet and people were closing their umbrellas» → acaba de llover.",
                ojo="las palabras fuertes (always, never, completely, only) suelen pasarse de lo que el texto "
                    "prueba: compruébalas en el texto.",
                chequeo="«Luis yawned all through the class». ¿Qué se infiere? (que estaba cansado o con sueño)",
                svg=fig_inferir),
            "Para qué lo pone el autor": dict(
                corto="cada detalle apoya una idea",
                d="Cada ejemplo o detalle está para algo: ilustrar una idea, convencer, contrastar o acercar el tema "
                  "al lector. Se pregunta qué entendería el lector sin ese detalle.",
                f="detalle → ¿qué idea apoya?",
                ej="en un texto sobre reciclaje, el autor cuenta que su barrio llenó un camión de botellas en una "
                   "semana: muestra que el problema es cercano y grande.",
                ojo="el propósito no es el tema: «habla de reciclaje» no dice para qué puso ese ejemplo.",
                chequeo="Un texto sobre el sueño cita a una médica. ¿Para qué la pone? (para dar autoridad y convencer)",
                svg=fig_proposito),
            "La frase que dice más de lo que dice": dict(
                corto="el sentido figurado",
                d="Algunas frases no se leen al pie de la letra: tienen sentido figurado. Se piensa qué sería lo "
                  "literal y qué idea quiere transmitir el autor con esa imagen.",
                f="lo literal → la imagen → la idea",
                ej="«My room is a jungle»: no tiene árboles; está muy desordenado.",
                ojo="traducir palabra por palabra no sirve: «it's raining cats and dogs» es «está lloviendo a cántaros».",
                chequeo="«This bag weighs a ton». ¿Pesa mil kilos? (no: quiere decir que pesa mucho)",
                svg=fig_figurado),
            "Dos cosas frente a frente": dict(
                corto="comparar: igual, distinto y a cuál favorece",
                d="Muchos textos ponen dos cosas a comparar: antes y ahora, el campo y la ciudad, dos opiniones. Se "
                  "busca en qué se parecen, en qué se diferencian y a cuál favorece el autor.",
                f="A ↔ B: ¿igual? · ¿distinto? · ¿a cuál favorece?",
                ej="«Paper books are heavy, but you never need to charge them» compara libros de papel y digitales, y "
                   "destaca una ventaja del papel.",
                ojo="but, while, whereas, unlike y however avisan que viene una comparación.",
                chequeo="«Unlike cats, dogs need daily walks». ¿Qué compara y en qué? (perros y gatos; en los paseos diarios)",
                svg=fig_frente),
        },
        vocab=[("Infer", "inferir, sacar una conclusión"),
               ("Imply", "dar a entender sin decirlo"),
               ("Suggest", "sugerir, insinuar"),
               ("Purpose", "propósito, para qué"),
               ("Whereas", "mientras que (compara)"),
               ("Unlike", "a diferencia de"),
               ("However", "sin embargo"),
               ("Mainly", "principalmente"),
               ("Completely", "completamente · palabra absoluta: compruébala")]),
    6: dict(
        titulo="Leer todo el texto antes de llenar el espacio",
        centro=("El texto completo", "la pista está cerca (la palabra de al lado) o lejos (el párrafo entero)", fig_c6),
        centro_ej="«Yesterday was busy. In the morning I cleaned my room, and then I ___ (help) my dad» → helped: "
                  "el reloj lo pone yesterday, una oración antes.",
        centro_ojo="llenar el espacio leyendo solo la oración es apostar: lee el texto entero primero.",
        centro_chequeo="¿Qué se lee antes de llenar el primer espacio? (el texto completo)",
        ideas={
            "La línea de tiempo del verbo": dict(
                corto="cada tiempo, su lugar en la línea",
                d="Pasado simple: una acción terminada. Pasado continuo: una acción larga que otra interrumpe. "
                  "Presente perfecto: del pasado hasta hoy. Pasado perfecto: antes de otro pasado.",
                f="was cooking + when + rang · have lived since · had left",
                ej="«I was cooking when the phone rang»: cocinar es la acción larga; sonar, el golpe que la corta.",
                ojo="since y for, hasta hoy, piden presente perfecto: «I have lived here since 2020», no «I live here "
                    "since 2020».",
                chequeo="«When we arrived, the film ___ already ___ (start)». (had already started)",
                svg=fig_linea),
            "La palabra de al lado manda la forma": dict(
                corto="has, to, can o el sujeto deciden",
                d="La palabra pegada al espacio decide la forma: have o has piden participio (has written); to pide "
                  "el verbo base (to write); can, will y should, el verbo base sin to; he, she o it, -s en presente.",
                f="has written · to write · can write · she writes",
                ej="«She has ___ (write) three songs» → written. «She wants ___ (write) a book» → to write.",
                ojo="el sujeto manda aunque esté lejos: «The girl with the red shoes ___ (dance) very well» → dances.",
                chequeo="«We should ___ (call) her». ¿Calls, call o to call? (call)",
                svg=fig_al_lado),
            "Palabras que andan juntas": dict(
                corto="colocaciones: make, do, take, pay",
                d="Hay palabras que van juntas por costumbre (colocaciones). En inglés se dice make a mistake y do "
                  "homework, aunque en español las dos sean «hacer». Se aprenden en pareja.",
                f="make a mistake · do homework · take a photo · pay attention",
                ej="«I always ___ a photo of my food» → take, no make.",
                ojo="«hacer» no siempre es do: make a cake, make a decision; pero do exercise, do the dishes.",
                chequeo="«Please ___ attention»: ¿pay, put o give? (pay)",
                svg=fig_colocacion),
            "El párrafo entero decide": dict(
                corto="si la oración no basta, el párrafo",
                d="Cuando la oración sola no basta, decide el párrafo: si todo va en presente, el espacio también; si "
                  "es un relato en pasado, sigue ese reloj. También se mira quién es el sujeto en las oraciones de "
                  "antes.",
                f="la oración sola ✗ → el párrafo entero ✓",
                ej="«Every summer my uncle travels to the coast. He ___ (rent) a small boat and fishes» → rents: el "
                   "párrafo cuenta una costumbre en presente.",
                ojo="prueba la opción en la oración completa, en voz baja: si cambia el reloj del párrafo, no es.",
                chequeo="Un relato empieza «It was a cold night…». ¿En qué tiempo irán casi todos los verbos? (en pasado)",
                svg=fig_parrafo),
        },
        vocab=[("Already", "ya"),
               ("Just", "acabar de (I have just eaten)"),
               ("Since", "desde (un momento)"),
               ("For", "durante (un tiempo)"),
               ("Ago", "hace (two years ago)"),
               ("While", "mientras"),
               ("Yet", "todavía, aún (en negativas)"),
               ("Make a mistake", "cometer un error"),
               ("Pay attention", "prestar atención")]),
}
