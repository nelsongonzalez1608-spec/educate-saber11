"""El toque personal de cada área (Nelson, 17 nov): un motivo sutil, en trazo fino y con poca opacidad,
que va en la esquina de la portada de la guía, de las dos diapositivas de conceptualización y de la hoja
de conceptualización del planeador. No tapa nada, no va detrás del texto y no es un fondo sólido.

    motivo("ing")  → SVG (viewBox 0 0 320 320)

Matemáticas: compás, transportador y π · Lectura Crítica: libro abierto y comillas · Sociales: rosa de
los vientos y columna · Biología: hoja, hélice de ADN y célula · Química: matraz y anillo de benceno ·
Física: átomo y péndulo · Inglés: Big Ben, Estatua de la Libertad y las banderas británica y estadounidense.
"""

AREA_COLOR = {"mate": "#1F4E8C", "lc": "#A82424", "soc": "#C9821B", "bio": "#30843C",
              "qui": "#0F7A68", "fis": "#5C7A1E", "ing": "#1BA0A8"}

CLAVE = {"Matemáticas": "mate", "Lectura Crítica": "lc", "Sociales y Ciudadanas": "soc", "Biología": "bio",
         "Química": "qui", "Física": "fis", "Inglés": "ing"}


def _g(c, cuerpo, sw=4):
    return (f'<g fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round">{cuerpo}</g>')


def _mate(c):
    return _g(c,
        # transportador
        '<path d="M40 250 A110 110 0 0 1 260 250 Z"/>'
        + "".join(f'<line x1="{150 + 100*__import__("math").cos(__import__("math").radians(a)):.0f}" '
                  f'y1="{250 - 100*__import__("math").sin(__import__("math").radians(a)):.0f}" '
                  f'x2="{150 + 88*__import__("math").cos(__import__("math").radians(a)):.0f}" '
                  f'y2="{250 - 88*__import__("math").sin(__import__("math").radians(a)):.0f}"/>'
                  for a in range(15, 180, 15))
        # compás
        + '<path d="M230 40 L190 170 M230 40 L270 170 M222 30 L238 30 L238 52 L222 52 Z M200 120 L260 120"/>'
        # π
        + '<path d="M40 70 L120 70 M62 70 L56 140 M98 70 L98 132 Q100 142 112 138"/>'
)


def _lc(c):
    return _g(c,
        '<path d="M40 230 Q100 200 160 230 Q220 200 280 230 L280 110 Q220 80 160 110 Q100 80 40 110 Z"/>'
        '<path d="M160 110 L160 230"/>'
        + "".join(f'<path d="M62 {128+i*20} Q100 {112+i*20} 140 {128+i*20}" stroke-width="2.5"/>' for i in range(4))
        + "".join(f'<path d="M180 {128+i*20} Q220 {112+i*20} 258 {128+i*20}" stroke-width="2.5"/>' for i in range(4))
        # comillas «»
        + '<path d="M120 40 L100 60 L120 80 M145 40 L125 60 L145 80 M175 40 L195 60 L175 80 M200 40 L220 60 L200 80"/>')


def _soc(c):
    rosa = ('<circle cx="100" cy="110" r="70"/><circle cx="100" cy="110" r="8"/>'
            '<path d="M100 30 L114 110 L100 190 L86 110 Z M20 110 L100 96 L180 110 L100 124 Z"/>'
            '')
    columna = ('<path d="M200 270 L290 270 M206 258 L284 258 M210 258 L210 140 M280 258 L280 140 '
               'M226 258 L226 140 M245 258 L245 140 M264 258 L264 140 M200 140 L290 140 M198 128 L245 100 L292 128 Z"/>')
    return _g(c, rosa + columna)


def _bio(c):
    hoja = '<path d="M40 260 Q40 140 160 120 Q160 240 40 260 Z M40 260 Q100 190 140 140"/>'
    adn = "".join(
        f'<line x1="{220 + 30*__import__("math").sin(y/22):.0f}" y1="{y}" x2="{220 - 30*__import__("math").sin(y/22):.0f}" y2="{y}" stroke-width="2.5"/>'
        for y in range(40, 290, 18))
    adn += ('<path d="' + "M" + " L".join(f'{220 + 30*__import__("math").sin(y/22):.1f} {y}' for y in range(30, 296, 6)) + '"/>'
            '<path d="' + "M" + " L".join(f'{220 - 30*__import__("math").sin(y/22):.1f} {y}' for y in range(30, 296, 6)) + '"/>')
    celula = '<ellipse cx="90" cy="70" rx="55" ry="38"/><circle cx="100" cy="72" r="13"/>'
    return _g(c, hoja + adn + celula)


def _qui(c):
    matraz = ('<path d="M70 60 L70 140 L20 250 Q16 262 30 262 L150 262 Q164 262 160 250 L110 140 L110 60 Z"/>'
              '<path d="M60 60 L120 60 M42 210 L138 210" stroke-width="3"/>'
              '<circle cx="80" cy="235" r="7"/><circle cx="108" cy="222" r="5"/>')
    import math
    hexa = "M" + " L".join(f'{230 + 55*math.cos(math.radians(a)):.1f} {110 + 55*math.sin(math.radians(a)):.1f}'
                           for a in range(30, 391, 60))
    benceno = f'<path d="{hexa}"/><circle cx="230" cy="110" r="30"/>'
    return _g(c, matraz + benceno)


def _fis(c):
    atomo = ('<ellipse cx="110" cy="110" rx="90" ry="32"/>'
             '<ellipse cx="110" cy="110" rx="90" ry="32" transform="rotate(60 110 110)"/>'
             '<ellipse cx="110" cy="110" rx="90" ry="32" transform="rotate(-60 110 110)"/>'
             '<circle cx="110" cy="110" r="10"/>')
    pendulo = ('<path d="M190 240 L300 240 M245 240 L245 236" stroke-width="3"/>'
               '<path d="M220 40 L290 40 M255 40 L215 200"/><circle cx="210" cy="215" r="16"/>'
               '<path d="M255 40 L255 190" stroke-dasharray="6 8" stroke-width="2"/>'
               '<path d="M222 192 Q255 210 288 192" stroke-dasharray="4 7" stroke-width="2"/>')
    return _g(c, atomo + pendulo)


def _ing(c):
    big_ben = ('<path d="M60 290 L60 120 L110 120 L110 290 M52 120 L118 120 M60 120 L85 60 L110 120 '
               'M85 60 L85 40"/><circle cx="85" cy="150" r="16"/><path d="M85 150 L85 140 M85 150 L93 154" stroke-width="2.5"/>'
               '<path d="M66 200 L104 200 M66 240 L104 240" stroke-width="2"/>')
    libertad = ('<path d="M190 290 L280 290 L270 250 L200 250 Z"/>'
                '<path d="M215 250 Q210 180 225 150 L245 150 Q262 180 255 250"/>'
                '<circle cx="235" cy="132" r="14"/>'
                '<path d="M222 124 L214 112 M230 119 L228 104 M240 119 L242 104 M248 124 L256 112"/>'
                '<path d="M248 150 L262 92"/><path d="M256 92 L268 92 L264 78 Q262 70 260 78 Z"/>')
    # banderas pequeñas, en sus colores (la única excepción al color del área)
    uk = ('<g transform="translate(150 30)"><rect width="66" height="40" fill="#012169"/>'
          '<path d="M0 0 L66 40 M66 0 L0 40" stroke="#fff" stroke-width="8"/>'
          '<path d="M0 0 L66 40 M66 0 L0 40" stroke="#C8102E" stroke-width="3"/>'
          '<path d="M33 0 V40 M0 20 H66" stroke="#fff" stroke-width="12"/>'
          '<path d="M33 0 V40 M0 20 H66" stroke="#C8102E" stroke-width="7"/></g>')
    us = ('<g transform="translate(230 30)"><rect width="66" height="40" fill="#fff"/>'
          + "".join(f'<rect y="{i*40/7:.2f}" width="66" height="{40/7:.2f}" fill="#B22234"/>' for i in range(0, 7, 2))
          + '<rect width="28" height="22" fill="#3C3B6E"/></g>')
    return _g(c, big_ben + libertad) + uk + us


DIBUJO = {"mate": _mate, "lc": _lc, "soc": _soc, "bio": _bio, "qui": _qui, "fis": _fis, "ing": _ing}


def motivo(area, color=None):
    """SVG completo del motivo del área (viewBox 0 0 320 320), sin opacidad: la pone quien lo usa."""
    area = CLAVE.get(area, area)
    c = color or AREA_COLOR[area]
    return f'<svg viewBox="0 0 320 320" aria-hidden="true">{DIBUJO[area](c)}</svg>'
