"""Piezas para dibujar las figuras de la conceptualización (ver conceptos.py y conceptos_mate.py).

Cada figura es un SVG de viewBox 420 × 300 (o 420 × h) con fondo transparente, trazo en tinta y
rellenos claros: va igual en la guía de pantalla y, escalada, en la hoja del planeador.
Reglas: fondo claro, el color del área o de la estrategia solo como acento, nada de texto en gris
claro (#C9D1DC es para líneas), letra Carlito, nada de líneas horizontales de adorno.

    from conceptos_figs import *
    def mi_figura(c):                       # c = color de la estrategia
        s = _caja(60, 120, 120, 100, 30) + _t(120, 270, "rótulo", 22, c, "middle")
        return _svg(s, "Descripción para lectores de pantalla", h=300)
"""
import math

TINTA, GRIS, LINEA = "#1E2230", "#6E7480", "#C9D1DC"
AZUL, ROJO, VERDE, ORO, MORADO = "#242478", "#A82424", "#30843C", "#C9821B", "#5B3E96"
F = 'font-family="Carlito, Calibri, Arial, sans-serif"'


def _svg(cuerpo, alt, w=420, h=300):
    """Envuelve el dibujo; agrega la sombra suave del piso (el «3D» liviano)."""
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{alt}">'
            f'<ellipse cx="{w/2}" cy="{h-14}" rx="{w*0.42}" ry="10" fill="{TINTA}" opacity=".07"/>{cuerpo}</svg>')


def _t(x, y, s, size=22, c=TINTA, anchor="start", w="700"):
    """Texto. s se escribe tal cual: no usar < ni & sin escapar."""
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" {F} font-size="{size}" fill="{c}" '
            f'font-weight="{w}">{s}</text>')


def _caja(x, y, w, h, d, cara="#fff", lado="#D3DCEA", tapa="#EEF2F8", sw=2.5):
    """Caja isométrica: frente (x, y, w, h) y fondo desplazado d hacia arriba a la derecha."""
    k = d * 0.6
    return (f'<polygon points="{x},{y} {x+w},{y} {x+w},{y+h} {x},{y+h}" fill="{cara}" stroke="{TINTA}" stroke-width="{sw}"/>'
            f'<polygon points="{x+w},{y} {x+w+d},{y-k} {x+w+d},{y+h-k} {x+w},{y+h}" fill="{lado}" stroke="{TINTA}" stroke-width="{sw}"/>'
            f'<polygon points="{x},{y} {x+d},{y-k} {x+w+d},{y-k} {x+w},{y}" fill="{tapa}" stroke="{TINTA}" stroke-width="{sw}"/>')


def _flecha(x1, y1, x2, y2, c, sw=4):
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 14 * math.cos(a - 0.45), y2 - 14 * math.sin(a - 0.45))
    p2 = (x2 - 14 * math.cos(a + 0.45), y2 - 14 * math.sin(a + 0.45))
    return (f'<path d="M{x1} {y1} L{x2} {y2} M{p1[0]:.1f} {p1[1]:.1f} L{x2} {y2} L{p2[0]:.1f} {p2[1]:.1f}" '
            f'fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')


def _tarjeta(x, y, w, h, texto, c, size=20, fondo="#fff"):
    """Rectángulo redondeado con un texto corto centrado (una línea)."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fondo}" stroke="{c}" stroke-width="3"/>'
            + _t(x + w / 2, y + h / 2 + size * 0.35, texto, size, TINTA, "middle", "600"))


def _bien(x, y, c=VERDE):
    return f'<path d="M{x} {y} l10 10 l18 -20" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'


def _mal(x, y, c=ROJO):
    return f'<path d="M{x} {y} l20 20 M{x+20} {y} l-20 20" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'


def _claro(c, k=0.82):
    """Versión clara de un color #RRGGBB (para rellenos)."""
    c = c.lstrip("#")
    r, g, b = (int(c[i:i + 2], 16) for i in (0, 2, 4))
    r, g, b = (round(v + (255 - v) * k) for v in (r, g, b))
    return f"#{r:02X}{g:02X}{b:02X}"


def lupa(c, lineas=("paso 1", "paso 2", "paso 3")):
    """Una lupa sobre una lista: revisar paso por paso."""
    s = ""
    for k, txt in enumerate(lineas):
        y = 50 + k * 64
        s += (f'<rect x="50" y="{y}" width="230" height="48" rx="10" fill="#fff" stroke="{LINEA}" stroke-width="2.5"/>'
              + _t(70, y + 32, txt, 20, TINTA, w="600"))
    s += (f'<circle cx="300" cy="170" r="52" fill="#fff" fill-opacity=".6" stroke="{c}" stroke-width="7"/>'
          f'<line x1="338" y1="208" x2="380" y2="252" stroke="{c}" stroke-width="12" stroke-linecap="round"/>')
    return _svg(s, "Una lupa revisa paso por paso", h=300)
