#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Propuesta de tres direcciones de estilo para el cuaderno Saber 11 (10 nov 2026).

Nelson: «Quiero creatividad en el diseño, es para jóvenes de 16 años … sin dejar lo esencial,
me refiero a los entornos». Aquí solo cambia el ENTORNO de la página (cabecera, marco de la
tarjeta, fondos, rótulos, adornos, títulos, íconos). El contenido es el real: la portada y la
hoja de metas toman sus textos de apertura.py / apertura2.py, y la hoja de taller usa las
preguntas 7 y 8 de Biología · Misión 2 (bio2.py, página 151) con SUS instrumentos sin tocar.

    A · RECORTES  — scrapbook / diario de collage
    B · BITÁCORA  — bullet journal / zine
    C · BLOQUE    — neo-brutalismo / tarjetas grandes de color

    python3 estilos_propuesta.py      → libro/estilo_{A,B,C}_{1,2,3}.svg + estilo_resumen.svg
                                         y /tmp/claude-0/estilos/Propuesta_estilos.pdf

No modifica taller_base.py, lib.py, apertura*.py ni bio2.py: los importa y redibuja aparte.
Tipografías de títulos (todas SIL OFL 1.1, en fuentes/propuesta/): DM Serif Display (A),
Shantell Sans + Space Mono (B), Bricolage Grotesque (C). El texto de lectura sigue en Carlito.
Se mide con twf(), la misma idea de tw() pero con el archivo de la fuente de títulos.
El entorno no usa filtros ni transparencias: color plano y vectorial. Lo que queda con opacidad
(caritas al 90 %, rayados de algunos instrumentos) viene del motor actual. El único raster es el logo.
"""
import math
import os
import random
import sys

LIBRO = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, LIBRO)

import bio2                      # noqa: E402  configura Biología · Misión 2 (un solo módulo)
import taller_base as tb         # noqa: E402
from taller_base import *        # noqa: E402,F401,F403
from apertura2 import CARRERAS   # noqa: E402
from PIL import ImageFont        # noqa: E402

OUTD = LIBRO + "/"
PDF_DIR = "/tmp/claude-0/estilos"
FUENTES = os.path.join(LIBRO, "..", "fuentes")

# ───────── tipografías de títulos (medidas con su archivo real) ─────────
DMS, SHA, MONO, BRI, HAND = ("DM Serif Display", "Shantell Sans", "Space Mono",
                             "Bricolage Grotesque", "Caveat")
_ARCH = {(DMS, "400"): "propuesta/dm-serif-display-400.ttf",
         (SHA, "400"): "propuesta/shantell-sans-400.ttf",
         (SHA, "700"): "propuesta/shantell-sans-700.ttf",
         (SHA, "800"): "propuesta/shantell-sans-800.ttf",
         (MONO, "400"): "propuesta/space-mono-400.ttf",
         (MONO, "700"): "propuesta/space-mono-700.ttf",
         (BRI, "400"): "propuesta/bricolage-grotesque-400.ttf",
         (BRI, "700"): "propuesta/bricolage-grotesque-700.ttf",
         (BRI, "800"): "propuesta/bricolage-grotesque-800.ttf",
         (HAND, "400"): "Caveat-Regular.ttf", (HAND, "700"): "Caveat-Bold.ttf"}
_FC = {}


def twf(txt, size, fam, weight="400"):
    """Ancho real de txt en la fuente de títulos (Carlito si fam es None)."""
    if fam is None:
        return tw(txt, size, weight)
    k = (fam, weight, size)
    if k not in _FC:
        _FC[k] = ImageFont.truetype(os.path.join(FUENTES, _ARCH[(fam, weight)]),
                                    int(round(size * 4)))
    return _FC[k].getlength(txt) / 4.0


def fit(txt, size, fam, weight, maxw, minimo=10):
    while size > minimo and twf(txt, size, fam, weight) > maxw:
        size -= 1
    return size


def TX(x, y, txt, size, color, fam=None, weight="400", anchor="start", rot=0, ls=0,
       style="normal"):
    font = f"{fam}, Carlito, sans-serif" if fam else UI
    return T(x, y, [txt], size, color, weight=weight, anchor=anchor, font=font, rot=rot, ls=ls,
             style=style)


# ───────── adornos vectoriales (sin filtros, sin transparencias) ─────────
def _pts(p):
    return " ".join(f"{x:.1f},{y:.1f}" for x, y in p)


def torn(x0, y0, x1, y1, fill, bordes="b", amp=9, paso=22, seed=1, fibra="#FFFFFF"):
    """Papel rasgado: rectángulo con los bordes de `bordes` (t, r, b, l) dentados.
    El trazo blanco hace de fibra del papel: es el canto del recorte, no una línea."""
    rnd = random.Random(seed)

    def borde(ax, ay, bx, by, roto):
        L = math.hypot(bx - ax, by - ay)
        n = max(1, int(L / paso))
        out = []
        for i in range(n):
            t = i / n
            px, py = ax + (bx - ax) * t, ay + (by - ay) * t
            if roto and i:
                d = rnd.uniform(-amp, amp)
                if ax == bx:
                    px += d
                else:
                    py += d
            out.append((px, py))
        return out
    p = (borde(x0, y0, x1, y0, "t" in bordes) + borde(x1, y0, x1, y1, "r" in bordes)
         + borde(x1, y1, x0, y1, "b" in bordes) + borde(x0, y1, x0, y0, "l" in bordes))
    st = f' stroke="{fibra}" stroke-width="4" stroke-linejoin="round"' if fibra else ""
    return f'<polygon points="{_pts(p)}" fill="{fill}"{st}/>'


def tape(cx, cy, w, h, ang, fill, motivo="#FFFFFF", seed=3):
    """Cinta washi opaca con extremos rasgados y un motivo de puntos."""
    rnd = random.Random(seed)
    izq = [(-w / 2 + rnd.uniform(-5, 5), -h / 2 + h * i / 5) for i in range(6)]
    der = [(w / 2 + rnd.uniform(-5, 5), h / 2 - h * i / 5) for i in range(6)]
    g = [f'<g transform="translate({cx:.1f} {cy:.1f}) rotate({ang})">',
         f'<polygon points="{_pts(izq + der)}" fill="{fill}"/>']
    if motivo:
        for i in range(int(w / 26)):
            for j in (-1, 1):
                g.append(f'<circle cx="{-w / 2 + 16 + i * 26 + (13 if j > 0 else 0):.1f}" '
                         f'cy="{j * h / 4:.1f}" r="3.4" fill="{motivo}"/>')
    g.append("</g>")
    return "".join(g)


def resaltador(x, y, w, h, fill, seed=5, rot=-0.8):
    """Trazo de resaltador detrás de una palabra: es un relleno, no un subrayado."""
    rnd = random.Random(seed)
    p = [(x - 6, y + rnd.uniform(0, 4)), (x + w + 8, y + rnd.uniform(-3, 3)),
         (x + w + 4 + rnd.uniform(0, 6), y + h * 0.5), (x + w + 10, y + h + rnd.uniform(-3, 2)),
         (x - 4, y + h + rnd.uniform(-2, 3)), (x - 10 + rnd.uniform(0, 4), y + h * 0.5)]
    return (f'<polygon points="{_pts(p)}" fill="{fill}" '
            f'transform="rotate({rot} {x + w / 2:.1f} {y + h / 2:.1f})"/>')


def wob_rect(x, y, w, h, c, sw=3, fill=None, seed=7, amp=1.4, sobre=5):
    """Recuadro a mano: cuatro trazos que se pasan un poco en las esquinas (pluma de bujo)."""
    rnd = random.Random(seed)
    g = [rect(x, y, w, h, fill, r=4)] if fill else []
    lados = [((x - sobre, y), (x + w + sobre * .6, y)), ((x + w, y - sobre), (x + w, y + h + sobre * .5)),
             ((x + w + sobre * .4, y + h), (x - sobre, y + h)), ((x, y + h + sobre * .4), (x, y - sobre))]
    for (ax, ay), (bx, by) in lados:
        n = max(2, int(math.hypot(bx - ax, by - ay) / 60))
        pts = []
        for i in range(n + 1):
            t = i / n
            pts.append((ax + (bx - ax) * t + rnd.uniform(-amp, amp),
                        ay + (by - ay) * t + rnd.uniform(-amp, amp)))
        g.append(spath(pts, c, sw, 1))
    return "".join(g)


def wob_circle(cx, cy, r, c, sw=2.6, seed=9, vueltas=1.08, fill=None):
    rnd = random.Random(seed)
    a0 = rnd.uniform(0, 6.28)
    n = 34
    pts = []
    for i in range(int(n * vueltas) + 1):
        a = a0 + i / n * 2 * math.pi
        rr = r * (1 + 0.035 * math.sin(i * 0.9 + a0)) + (i / n) * 2.5
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    g = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}"/>' if fill else ""
    return g + spath(pts, c, sw, 1)


def puntos(x0, y0, x1, y1, paso=40, c="#CBD1DB", r=2.1):
    """Cuadrícula de puntos en un solo trazado (segmentos de largo cero con punta redonda)."""
    d = []
    yy = y0
    while yy <= y1:
        xx = x0
        while xx <= x1:
            d.append(f"M{xx} {yy}h0")
            xx += paso
        yy += paso
    return (f'<path d="{"".join(d)}" stroke="{c}" stroke-width="{2 * r}" '
            f'stroke-linecap="round" fill="none"/>')


def estrellita(cx, cy, r, c, sw=2.4):
    """Chispa de cuatro puntas a mano (garabato de margen)."""
    return (spath([(cx, cy - r), (cx, cy + r)], c, sw, 1)
            + spath([(cx - r, cy), (cx + r, cy)], c, sw, 1)
            + spath([(cx - r * .55, cy - r * .55), (cx + r * .55, cy + r * .55)], c, sw * .7, 1)
            + spath([(cx - r * .55, cy + r * .55), (cx + r * .55, cy - r * .55)], c, sw * .7, 1))


def clip(x, y, c="#8A93A3"):
    """Clip de papel."""
    return (f'<path d="M {x + 10} {y + 70} L {x + 10} {y + 12} C {x + 10} {y - 4} {x + 34} {y - 4} '
            f'{x + 34} {y + 12} L {x + 34} {y + 82} C {x + 34} {y + 98} {x + 2} {y + 98} {x + 2} {y + 82} '
            f'L {x + 2} {y + 24}" fill="none" stroke="{c}" stroke-width="4" stroke-linecap="round"/>')


def rot_g(frag, ang, cx, cy):
    return f'<g transform="rotate({ang} {cx:.1f} {cy:.1f})">{frag}</g>'


def chip_medido(b, x, y, txt, fill, txtc="white", size=19, h=44, pad=18, r=None, stroke=None,
                sw=2, extra="", ang=0):
    """Chip con el ancho medido con tw() (Carlito): lo revisa verifica_cajas.py."""
    w = tw(txt, size, "700") + 2 * pad
    r = h / 2 if r is None else r
    g = (f'<g class="chip" data-pad="{pad}">'
         + rect(x, y, w, h, fill, r=r, stroke=stroke or fill, sw=sw)
         + (extra(x, y, w, h) if extra else "")
         + T(x + w / 2, y + h / 2 + size * 0.36, [txt], size, txtc, weight="700", anchor="middle")
         + "</g>")
    b.append(rot_g(g, ang, x + w / 2, y + h / 2) if ang else g)
    return w


def pagina(fondo):
    b = svg_open()
    if fondo and fondo.upper() != "#FFFFFF":
        b.append(rect(0, 0, W, H_PAGE, fondo, r=0))
    return b


# ════════════════════════════ los tres estilos ════════════════════════════
class Estilo:
    """Lo común de una hoja de taller. Cada dirección redefine el entorno."""
    key = "X"
    papel = "#FFFFFF"

    def fondo(self, b):
        pass

    # columna derecha: misma geometría que taller_base.columna_derecha
    def columna(self, b, y, est, letras="ABCD"):
        c = A["color"]
        rx = M + RX_OFF
        rw = W - M - rx - 24
        ry = y + 130
        self.divisor(b, rx - 18, ry, y + tb.BLK_H - 30)
        self.rotulo(b, rx, ry + 20, "Marco al final")
        paso = min(92, (rw - 72) / max(len(letras) - 1, 1))
        r = min(30, paso / 2 - 4)
        for k, L in enumerate(letras):
            self.burbuja(b, rx + 36 + k * paso, ry + 80, r, L, c, k)
        b.append(T(rx, ry + 144, ["¿Qué tan seguro estoy?"], 18, GRAY))
        for k, lab in enumerate(["adiviné", "casi", "seguro"]):
            self.casilla(b, rx + k * 150, ry + 164)
            b.append(T(rx + 30 + k * 150, ry + 182, [lab], 18, GRAY))
        sy = ry + 231
        self.salv(b, rx, sy, rw)
        ly = sy + 352
        self.cierre(b, rx, ly, "Lo que me llevo de esta pregunta",
                    "(una frase que me sirva en otra pregunta parecida)")
        b.append(wlines(rx, sy + 438, rw, 4, c="#E3E8EF", step=48))
        self.marca_est(b, W - M - 60, y + tb.BLK_H - 50, est)

    def divisor(self, b, x, y0, y1):
        b.append(line(x, y0, x, y1, "#E6EAF0", 2, "6,6"))      # vertical: permitido

    def casilla(self, b, x, y):
        b.append(checkbox(x, y, s=11, c=GRAY))

    def salv(self, b, rx, sy, rw):
        tb.salvavidas(b, rx, sy, rw)

    def tarjeta(self, b, y, n, est, pag, ctx, inst, comp=None, letras="ABCD", **_):
        self.marco(b, y, n)
        self.encabezado(b, y, n, pag, ctx, est, comp)
        ix, iy = M + 30, y + 130
        fondo = y + tb.BLK_H - 40
        y_fin = tb._instrumento(b, n, inst, ix, iy, fondo)
        if fondo - (y_fin + 14) >= tb.NOTA_MIN:
            self.notas(b, ix, y_fin + 14, IW - 4, fondo - y_fin - 14)
        self.columna(b, y, est, letras)

    def hoja_taller(self, nombre, pag, hoja, qa, qb):
        tb.set_bloque(True)
        b = pagina(self.papel)
        self.fondo(b)
        nh = A.get("n_hojas", 5)
        self.cabecera(b, f"Prueba de Campo · hoja {hoja} de {nh} · preguntas {qa['n']} y {qb['n']}")
        self.tarjeta(b, tb.Y0, **qa)
        self.tarjeta(b, tb.y_bloque2(), **qb)
        self.vocab(b)
        self.pie(b, pag, A["color"], f"{A['area']} · Misión {A['mision']} · Prueba de Campo")
        ruta = OUTD + nombre + ".svg"
        svg_close(b, ruta)
        return ruta


# ─────────────────────────── A · RECORTES ───────────────────────────
KRAFT, KRAFT_D, KRAFT_LN = "#E8DCC4", "#6B5532", "#D6C6A6"
NOTA, NOTA_D, NOTA_LN = "#FFF1A6", "#EBD77A", "#E2D27E"
CINTAS = ["#BFE3D6", "#F6C9C4", "#F3D98B", "#C9D7F2"]
TINTA_A = "#2B2724"
PAPEL_A = "#FBF7EF"


class Recortes(Estilo):
    key = "A"
    papel = PAPEL_A

    def cabecera(self, b, linea3):
        c = A["color"]
        b.append(torn(26, -20, 1262, 172, KRAFT, bordes="br", seed=11, fibra=None))
        b.append(torn(14, -20, 1250, 160, A["bg"], bordes="br", seed=12))
        b.append(tape(1236, 34, 150, 42, 52, CINTAS[3], seed=4))
        b.append(logo(M, 46, 62))
        x0 = M + 210
        b.append(TX(x0, 88, A["area"], 54, c, DMS))
        x1 = x0 + twf(A["area"], 54, DMS) + 18
        b.append(TX(x1, 86, f"misión {A['mision']}", 44, TINTA_A, HAND, "700"))
        sub = " · ".join(s for s in (A["tema"], f"componente {A['componente']}") if s)
        b.append(TX(x0, 124, sub, 20, GRAY))
        b.append(TX(x0, 152, linea3, 19, GRAY, style="italic"))
        # nota adhesiva con la fecha y las caritas (aquí se escribe: fondo claro)
        nx, ny, nw, nh = 1296, 20, 634, 156
        g = [rect(nx, ny, nw, nh, NOTA, r=2),
             f'<polygon points="{_pts([(nx + nw - 44, ny + nh), (nx + nw, ny + nh - 44), (nx + nw - 44, ny + nh - 44)])}" fill="{NOTA_D}"/>',
             f'<polygon points="{_pts([(nx + nw - 44, ny + nh), (nx + nw, ny + nh - 44), (nx + nw, ny + nh)])}" fill="{PAPEL_A}"/>',
             T(nx + 30, ny + 56, ["Sábado ____ de ____________"], 24, INK),
             T(nx + 30, ny + 116, ["Llego:"], 22, TINTA_A)]
        for k, mood in enumerate(["worried", "calm", "happy"]):
            g.append(face(nx + 130 + k * 62, ny + 108, 22, mood, TINTA_A, "white", sw=2.2))
        g.append(T(nx + 330, ny + 116, ["Salgo:"], 22, TINTA_A))
        for k, mood in enumerate(["worried", "calm", "happy"]):
            g.append(face(nx + 432 + k * 62, ny + 108, 22, mood, TINTA_A, "white", sw=2.2))
        b.append(rot_g("".join(g), 0.9, nx + nw / 2, ny + nh / 2))
        b.append(tape(nx + nw / 2, ny + 2, 160, 40, -3, CINTAS[0], seed=8))

    def marco(self, b, y, n):
        h = tb.BLK_H
        b.append(rot_g(rect(M + 8, y + 10, CW, h, KRAFT, r=4), -0.45, M + CW / 2, y + h / 2))
        b.append(rect(M, y, CW, h, "white", r=6, stroke="#E6DDCC", sw=2))
        b.append(tape(W - M - 34, y + 10, 170, 44, 38, CINTAS[n % 4], seed=n))

    def encabezado(self, b, y, n, pag, ctx, est, comp):
        c = A["color"]
        cx, cy = M + 62, y + 58
        b.append(f'<circle cx="{cx + 3}" cy="{cy + 4}" r="41" fill="{KRAFT_LN}"/>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="41" fill="white"/>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="{c}"/>')
        b.append(TX(cx, cy + 15, str(n), 42, "white", DMS, anchor="middle"))
        t1 = f"Pregunta {n}"
        b.append(TX(M + 118, y + 54, t1, 40, TINTA_A, DMS))
        x2 = M + 118 + twf(t1, 40, DMS) + 14
        t2 = f"la lees en tu libro, página {pag}"
        s2 = fit(t2, 30, HAND, "700", M + 735 - x2)
        b.append(TX(x2, y + 52, t2, s2, c, HAND, "700"))
        b.append(TX(M + 118, y + 90, ctx, 20, GRAY, style="italic"))
        nombre, ec = EST[est]
        txt = f"{A.get('prefijo', 'Estrategia')} {est} · {nombre}"
        # cinta rotuladora (Dymo): el chip sigue midiéndose con tw()
        chip_medido(b, M + 760, y + 26, txt, ec, r=5, ang=-1.2)
        if comp:
            b.append(TX(M + 764, y + 96, f"competencia · {comp}", 15, GRAY, style="italic"))
        # primera idea: en una notica amarilla clara
        px, pw = M + 1290, W - M - 30 - (M + 1290)
        g = [rect(px, y + 16, pw, 92, "#FFF7CF", r=2),
             TX(px + 18, y + 48, "Mi primera idea, antes de hacer nada:", 25, TINTA_A, HAND, "700"),
             line(px + 18, y + 90, px + pw - 18, y + 90, NOTA_LN, 2)]
        b.append(rot_g("".join(g), 0.5, px + pw / 2, y + 60))

    def notas(self, b, x, y, w, h):
        c = A["color"]
        b.append(rect(x, y, w, h, "white", r=4, stroke="#E6DDCC", sw=2))
        b.append(clip(x + 22, y - 18))
        b.append(TX(x + 70, y + 34, A["nota"].capitalize(), 26, c, HAND, "700"))
        n = int((h - 70) // 48) + 1
        if n > 0:
            b.append(wlines(x + 18, y + 60, w - 36, n, c="#E6EAF0", step=48))

    def divisor(self, b, x, y0, y1):
        b.append(line(x, y0, x, y1, "#E6DDCC", 2, "4,8"))

    def rotulo(self, b, x, y, txt):
        b.append(TX(x, y + 6, txt, 30, A["color"], HAND, "700"))

    def burbuja(self, b, cx, cy, r, L, c, k):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="white" stroke="{c}" stroke-width="2.6"/>')
        b.append(TX(cx, cy + r / 2.6, L, round(28 * r / 30), c, DMS, anchor="middle"))

    def salv(self, b, rx, sy, rw):
        tb.salvavidas(b, rx, sy, rw)
        b.append(tape(rx + rw - 44, sy + 6, 120, 38, 30, CINTAS[1], seed=21))

    def cierre(self, b, x, y, t1, t2):
        b.append(TX(x, y + 2, t1, 30, A["color"], HAND, "700"))
        b.append(TX(x, y + 28, t2, 16, GRAY, style="italic"))

    def marca_est(self, b, cx, cy, est):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="white" stroke="{KRAFT_LN}" stroke-width="2"/>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="17" fill="{EST[est][1]}"/>')
        b.append(T(cx, cy + 7, [str(est)], 18, "white", weight="700", anchor="middle"))

    def vocab(self, b):
        y, h = tb.VOCAB_Y, tb.VOCAB_H
        b.append(torn(M - 6, y, W - M + 6, y + h, KRAFT, bordes="lr", amp=7, seed=31))
        b.append(tape(M + 8, y + 14, 120, 38, -34, CINTAS[2], seed=32))
        b.append(tape(W - M - 10, y + h - 12, 120, 38, -30, CINTAS[0], seed=33))
        b.append(TX(M + 60, y + 38, "Palabras que me frenaron", 30, KRAFT_D, HAND, "700"))
        x2 = M + 60 + twf("Palabras que me frenaron", 30, HAND, "700") + 20
        b.append(TX(x2, y + 36, "no la busques todavía: adivínala por el contexto y confírmala en clase",
                    15, KRAFT_D, style="italic"))
        b.append(TX(M + 34, y + 90, "la palabra", 15, KRAFT_D, style="italic"))
        b.append(TX(M + 34, y + 140, "lo que creo que significa", 15, KRAFT_D, style="italic"))
        for i in range(5):
            x = M + 239 + i * 320
            for yy in (y + 60, y + 112):
                b.append(rect(x, yy, 307, 42, "white", r=4, stroke=KRAFT_LN, sw=1.6))

    def pie(self, b, pag, c, texto):
        y = H_PAGE - 90
        b.append(T(M, y + 8, ["Aprende"], 21, c, weight="700"))
        b.append(f'<circle cx="{M + 120}" cy="{y}" r="5" fill="{EDU_ORO}"/>')
        b.append(T(M + 138, y + 8, ["Practica"], 21, c, weight="700"))
        b.append(f'<circle cx="{M + 262}" cy="{y}" r="5" fill="{EDU_ORO}"/>')
        b.append(T(M + 280, y + 8, ["Avanza"], 21, c, weight="700"))
        b.append(T(W / 2, y + 8, [texto], 19, GRAY, anchor="middle"))
        b.append(f'<circle cx="{W - M - 30}" cy="{y - 2}" r="34" fill="{KRAFT}"/>')
        b.append(TX(W - M - 30, y + 10, str(pag), 30, TINTA_A, DMS, anchor="middle"))


# ─────────────────────────── B · BITÁCORA ───────────────────────────
FOSFO = "#FFE94A"         # amarillo resaltador (en CMYK: amarillo limpio, sin brillo fluorescente)
FOSFO_2 = "#B8F2D2"       # menta resaltador
TINTA_B = "#1E2230"
DOT = "#CBD1DB"


class Bitacora(Estilo):
    key = "B"

    def fondo(self, b):
        b.append(puntos(40, 40, W - 40, H_PAGE - 40, 40, DOT, 2.1))

    def cabecera(self, b, linea3):
        c = A["color"]
        b.append(rect(M - 10, 30, logo_w(62) + 20, 82, "white", r=4))
        b.append(logo(M, 40, 62))
        x0 = M + 200
        t = A["area"]
        s = 50
        wt = twf(t, s, SHA, "800")
        b.append(resaltador(x0, 52, wt, 40, FOSFO, seed=2))
        b.append(TX(x0, 88, t, s, TINTA_B, SHA, "800"))
        b.append(TX(x0 + wt + 22, 86, f"/ MISIÓN {A['mision']:02d}", 24, c, MONO, "700"))
        sub = " · ".join(s for s in (A["tema"], f"componente {A['componente']}") if s)
        b.append(rect(x0 - 6, 104, tw(sub, 21) + 12, 30, "white", r=2))
        b.append(TX(x0, 126, sub, 21, GRAY))
        l3 = linea3.upper()
        b.append(rect(x0 - 6, 140, twf(l3, 15, MONO) + 12, 26, "white", r=2))
        b.append(TX(x0, 159, l3, 15, GRAY, MONO))
        # fecha y registro de ánimo (aquí se escribe: recuadro blanco)
        nx, ny, nw, nh = 1300, 24, 630, 152
        b.append(wob_rect(nx, ny, nw, nh, TINTA_B, 2.6, fill="white", seed=41))
        b.append(T(nx + 28, ny + 52, ["Sábado ____ de ____________"], 24, INK))
        b.append(TX(nx + 28, ny + 116, "LLEGO", 15, GRAY, MONO, "700"))
        b.append(TX(nx + 328, ny + 116, "SALGO", 15, GRAY, MONO, "700"))
        for base in (nx + 120, nx + 420):
            for k, mood in enumerate(["worried", "calm", "happy"]):
                b.append(face(base + k * 62, ny + 108, 22, mood, TINTA_B, "white", sw=2.2))
        b.append(estrellita(nx - 34, ny + 30, 13, c))

    def marco(self, b, y, n):
        b.append(wob_rect(M, y, CW, tb.BLK_H, TINTA_B, 3, fill="white", seed=50 + n, amp=1.6))

    def encabezado(self, b, y, n, pag, ctx, est, comp):
        c = A["color"]
        cx, cy = M + 62, y + 56
        b.append(wob_circle(cx, cy, 38, c, 2.8, seed=n, vueltas=1.15))
        b.append(TX(cx, cy + 12, f"{n:02d}", 32, c, MONO, "700", anchor="middle"))
        t1 = f"Pregunta {n}"
        w1 = twf(t1, 34, SHA, "800")
        b.append(resaltador(M + 118, y + 22, w1, 34, FOSFO, seed=n + 3))
        b.append(TX(M + 118, y + 52, t1, 34, TINTA_B, SHA, "800"))
        b.append(TX(M + 118 + w1 + 16, y + 50, f"la lees en tu libro, página {pag}", 21, c, weight="700"))
        b.append(TX(M + 118, y + 88, ctx, 20, GRAY, style="italic"))
        nombre, ec = EST[est]
        txt = f"{A.get('prefijo', 'Estrategia')} {est} · {nombre}"
        # sello de caucho: doble borde, tinta del color de la estrategia
        chip_medido(b, M + 760, y + 26, txt, "white", txtc=ec, r=4, stroke=ec, sw=3, ang=-1.6,
                    extra=lambda x, y, w, h: rect(x + 5, y + 5, w - 10, h - 10, "none", r=2,
                                                  stroke=ec, sw=1.4))
        if comp:
            b.append(TX(M + 764, y + 98, f"COMPETENCIA · {comp.upper()}", 12, GRAY, MONO))
        b.append(hand_arrow(M + 1262, y + 54, M + 1296, y + 40, c, sw=2.6, bend=0.25, head=11))
        b.append(T(M + 1300, y + 44, ["Mi primera idea, antes de hacer nada:"], 20, GRAY))
        b.append(line(M + 1300, y + 86, W - M - 30, y + 86, LGRAY, 2.2))

    def notas(self, b, x, y, w, h):
        c = A["color"]
        b.append(wob_rect(x, y, w, h, "#9AA3B5", 2, fill="white", seed=int(y), amp=1.2, sobre=5))
        b.append(TX(x + 18, y + 30, A["nota"], 14, c, MONO, "700"))
        n = int((h - 70) // 48) + 1
        if n > 0:
            b.append(wlines(x + 18, y + 60, w - 36, n, c="#E6EAF0", step=48))

    def divisor(self, b, x, y0, y1):
        pts = [(x + random.Random(int(y0)).uniform(-1.4, 1.4), yy) for yy in range(int(y0), int(y1), 40)]
        b.append(spath(pts, "#C3C9D4", 2, 1))

    def rotulo(self, b, x, y, txt):
        b.append(TX(x, y, txt.upper(), 16, TINTA_B, MONO, "700"))

    def burbuja(self, b, cx, cy, r, L, c, k):
        b.append(wob_circle(cx, cy, r, c, 2.4, seed=k + 60, fill="white"))
        b.append(TX(cx, cy + r / 3, L, round(25 * r / 30), c, SHA, "700", anchor="middle"))

    def casilla(self, b, x, y):
        b.append(wob_rect(x, y, 22, 22, GRAY, 2, fill="white", seed=x, amp=0.7, sobre=3))

    def salv(self, b, rx, sy, rw):
        tb.salvavidas(b, rx, sy, rw)

    def cierre(self, b, x, y, t1, t2):
        b.append(TX(x, y + 2, t1, 22, A["color"], SHA, "700"))
        b.append(estrellita(x + twf(t1, 22, SHA, "700") + 22, y - 6, 10, EDU_ORO, 2.2))
        b.append(TX(x, y + 28, t2, 16, GRAY, style="italic"))

    def marca_est(self, b, cx, cy, est):
        ec = EST[est][1]
        b.append(f'<circle cx="{cx}" cy="{cy}" r="22" fill="white" stroke="{ec}" stroke-width="2.6"/>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="16" fill="none" stroke="{ec}" stroke-width="1.2"/>')
        b.append(TX(cx, cy + 7, str(est), 18, ec, MONO, "700", anchor="middle"))

    def vocab(self, b):
        y, h = tb.VOCAB_Y, tb.VOCAB_H
        c = A["color"]
        b.append(wob_rect(M, y, CW, h, TINTA_B, 2.6, fill="white", seed=77))
        t = "PALABRAS QUE ME FRENARON"
        wt = twf(t, 15, MONO, "700")
        b.append(resaltador(M + 34, y + 16, wt, 22, FOSFO_2, seed=78))
        b.append(TX(M + 34, y + 33, t, 15, TINTA_B, MONO, "700"))
        b.append(TX(M + 34 + wt + 26, y + 33, "no la busques todavía: adivínala por el contexto "
                    "y confírmala en clase", 15, GRAY, style="italic"))
        b.append(TX(M + 34, y + 90, "la palabra", 15, GRAY, style="italic"))
        b.append(TX(M + 34, y + 140, "lo que creo que significa", 15, GRAY, style="italic"))
        for i in range(5):
            x = M + 239 + i * 320
            for yy in (y + 60, y + 112):
                b.append(rect(x, yy, 307, 42, "white", r=4, stroke="#C9CFDA", sw=1.6))
        b.append(estrellita(W - M - 40, y + 30, 11, c))

    def pie(self, b, pag, c, texto):
        y = H_PAGE - 90
        b.append(rect(M - 8, y - 26, 380, 46, "white", r=2))
        b.append(T(M, y + 8, ["Aprende"], 21, c, weight="700"))
        b.append(T(M + 116, y + 8, ["→"], 21, EDU_ORO, weight="700"))
        b.append(T(M + 146, y + 8, ["Practica"], 21, c, weight="700"))
        b.append(T(M + 262, y + 8, ["→"], 21, EDU_ORO, weight="700"))
        b.append(T(M + 292, y + 8, ["Avanza"], 21, c, weight="700"))
        tt = texto.upper()
        b.append(rect(W / 2 - twf(tt, 14, MONO) / 2 - 8, y - 18, twf(tt, 14, MONO) + 16, 32, "white", r=2))
        b.append(TX(W / 2, y + 4, tt, 14, GRAY, MONO, anchor="middle"))
        t = f"p. {pag}"
        wt = twf(t, 24, MONO, "700")
        b.append(wob_rect(W - M - wt - 24, y - 30, wt + 24, 50, TINTA_B, 2.4, fill="white", seed=88))
        b.append(TX(W - M - 12, y + 6, t, 24, TINTA_B, MONO, "700", anchor="end"))


# ─────────────────────────── C · BLOQUE ───────────────────────────
TINTA_C = "#16181D"
AMARILLO = "#FFD84D"
LILA = "#C9B8FF"


def bloque(x, y, w, h, fill, sombra=TINTA_C, d=10, sw=4, r=12, stroke=TINTA_C):
    """Bloque neo-brutalista: borde grueso y sombra desplazada sólida (sin filtros)."""
    g = []
    if sombra:
        g.append(rect(x + d, y + d, w, h, sombra, r=r))
    g.append(rect(x, y, w, h, fill, r=r, stroke=stroke, sw=sw))
    return "".join(g)


class Bloque(Estilo):
    key = "C"

    def cabecera(self, b, linea3):
        c = A["color"]
        b.append(bloque(M, 26, 186, 132, "white", d=8))
        b.append(logo(M + 93 - logo_w(66) / 2, 58, 66))
        x0, x1 = M + 214, 1150
        b.append(bloque(x0, 26, x1 - x0, 132, c, d=8))
        b.append(TX(x0 + 28, 82, A["area"].upper(), fit(A["area"].upper(), 46, BRI, "800", 640),
                    "white", BRI, "800"))
        sub = " · ".join(s for s in (A["tema"], f"componente {A['componente']}") if s)
        s = fit(sub, 19, None, "400", x1 - x0 - 56)
        b.append(TX(x0 + 28, 114, sub, s, "white"))
        b.append(TX(x0 + 28, 142, linea3, 17, tb._mezcla(c, 0.78), style="italic"))
        # número de misión en bloque amarillo
        b.append(bloque(1174, 26, 112, 132, AMARILLO, d=8))
        b.append(TX(1230, 56, "MISIÓN", 15, TINTA_C, weight="700", anchor="middle", ls=1))
        b.append(TX(1230, 136, f"{A['mision']:02d}", 66, TINTA_C, BRI, "800", anchor="middle"))
        # fecha y caritas en bloque blanco (se escribe)
        nx, nw = 1312, W - M - 1312
        b.append(bloque(nx, 26, nw, 132, "white", sombra=c, d=8))
        b.append(T(nx + 24, 72, ["Sábado ____ de __________"], 24, INK))
        b.append(TX(nx + 24, 132, "Llego", 19, TINTA_C, weight="700"))
        b.append(TX(nx + 312, 132, "Salgo", 19, TINTA_C, weight="700"))
        for base in (nx + 112, nx + 400):
            for k, mood in enumerate(["worried", "calm", "happy"]):
                b.append(face(base + k * 58, 124, 21, mood, TINTA_C, "white", sw=2.4))

    def marco(self, b, y, n):
        b.append(bloque(M, y, CW, tb.BLK_H, "white", sombra=A["color"], d=12, sw=4.5, r=14))

    def encabezado(self, b, y, n, pag, ctx, est, comp):
        c = A["color"]
        b.append(bloque(M + 26, y + 22, 70, 70, c, d=5, sw=3.5, r=8))
        b.append(TX(M + 61, y + 72, str(n), 40, "white", BRI, "800", anchor="middle"))
        t1 = f"Pregunta {n}"
        b.append(TX(M + 118, y + 54, t1, 36, TINTA_C, BRI, "800"))
        x2 = M + 118 + twf(t1, 36, BRI, "800") + 14
        b.append(TX(x2, y + 52, f"la lees en tu libro, página {pag}", 21, GRAY))
        b.append(TX(M + 118, y + 88, ctx, 20, GRAY, style="italic"))
        nombre, ec = EST[est]
        txt = f"{A.get('prefijo', 'Estrategia')} {est} · {nombre}"
        w = tw(txt, 19, "700") + 36
        b.append(rect(M + 764, y + 30, w, 44, TINTA_C, r=22))
        chip_medido(b, M + 760, y + 26, txt, ec, stroke=TINTA_C, sw=3)
        if comp:
            b.append(TX(M + 764, y + 98, f"competencia · {comp}", 15, GRAY, style="italic"))
        b.append(TX(M + 1300, y + 38, "Mi primera idea, antes de hacer nada:", 19, TINTA_C, BRI, "700"))
        b.append(rect(M + 1300, y + 52, W - M - 30 - (M + 1300), 50, "white", r=8, stroke=TINTA_C, sw=2.5))

    def notas(self, b, x, y, w, h):
        y, h = y + 18, h - 18          # la pestaña amarilla no toca el instrumento de arriba
        b.append(rect(x, y, w, h, "white", r=10, stroke=TINTA_C, sw=2.5))
        t = A["nota"]
        wt = tw(t, 15, "700") + 1.5 * len(t) + 28
        b.append(rect(x + 16, y - 16, wt, 32, AMARILLO, r=6, stroke=TINTA_C, sw=2.5))
        b.append(T(x + 30, y + 6, [t], 15, TINTA_C, weight="700", ls=1.5))
        n = int((h - 70) // 48) + 1
        if n > 0:
            b.append(wlines(x + 18, y + 60, w - 36, n, c="#E6EAF0", step=48))

    def divisor(self, b, x, y0, y1):
        b.append(line(x, y0, x, y1, "#D5D9E0", 2.5, "2,10"))

    def rotulo(self, b, x, y, txt):
        b.append(TX(x, y + 2, txt.upper(), 20, TINTA_C, BRI, "800", ls=1))

    def burbuja(self, b, cx, cy, r, L, c, k):
        b.append(f'<circle cx="{cx + 4}" cy="{cy + 4}" r="{r:.1f}" fill="{c}"/>')
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r:.1f}" fill="white" stroke="{TINTA_C}" stroke-width="3"/>')
        b.append(TX(cx, cy + r / 2.8, L, round(26 * r / 30), TINTA_C, BRI, "800", anchor="middle"))

    def casilla(self, b, x, y):
        b.append(rect(x, y, 22, 22, "white", r=3, stroke=TINTA_C, sw=2.5))

    def salv(self, b, rx, sy, rw):
        b.append(rect(rx + 8, sy + 8, rw, 300, tb.SALV, r=18))     # sombra en el coral del salvavidas
        tb.salvavidas(b, rx, sy, rw)

    def cierre(self, b, x, y, t1, t2):
        b.append(TX(x, y + 2, t1, 21, TINTA_C, BRI, "800"))
        b.append(TX(x, y + 28, t2, 16, GRAY, style="italic"))

    def marca_est(self, b, cx, cy, est):
        b.append(bloque(cx - 20, cy - 20, 40, 40, EST[est][1], d=4, sw=2.5, r=6))
        b.append(TX(cx, cy + 8, str(est), 20, "white", BRI, "800", anchor="middle"))

    def vocab(self, b):
        y, h = tb.VOCAB_Y + 8, tb.VOCAB_H - 8
        b.append(bloque(M, y, CW - 10, h, "white", sombra=AMARILLO, d=10, sw=4, r=14))
        b.append(TX(M + 34, y + 34, "PALABRAS QUE ME FRENARON", 18, TINTA_C, BRI, "800", ls=1))
        x2 = M + 34 + twf("PALABRAS QUE ME FRENARON", 18, BRI, "800") + 24 + 24
        b.append(TX(x2, y + 33, "no la busques todavía: adivínala por el contexto y confírmala en clase",
                    15, GRAY, style="italic"))
        b.append(TX(M + 34, y + 86, "la palabra", 15, GRAY, style="italic"))
        b.append(TX(M + 34, y + 132, "lo que creo que significa", 15, GRAY, style="italic"))
        for i in range(5):
            x = M + 239 + i * 318
            for yy in (y + 56, y + 104):
                b.append(rect(x, yy, 300, 40, "white", r=6, stroke=TINTA_C, sw=2))

    def pie(self, b, pag, c, texto):
        y = H_PAGE - 84
        b.append(T(M, y + 8, ["Aprende"], 21, c, weight="700"))
        b.append(rect(M + 115, y - 5, 10, 10, TINTA_C, r=1))
        b.append(T(M + 138, y + 8, ["Practica"], 21, c, weight="700"))
        b.append(rect(M + 257, y - 5, 10, 10, TINTA_C, r=1))
        b.append(T(M + 280, y + 8, ["Avanza"], 21, c, weight="700"))
        b.append(T(W / 2, y + 8, [texto], 19, GRAY, anchor="middle"))
        b.append(rect(W - M - 76, y - 32, 76, 56, TINTA_C, r=8))
        b.append(TX(W - M - 38, y + 10, str(pag), 28, "white", BRI, "800", anchor="middle"))


ESTILOS = {"A": Recortes(), "B": Bitacora(), "C": Bloque()}


# ════════════════════════════ íconos simples de área (trazo) ════════════════════════════
def icono(kind, cx, cy, s, c, sw=None):
    """Íconos de una línea, del mismo grueso, para las siete áreas."""
    sw = sw or s * 0.10
    P = lambda pts: spath([(cx + a * s, cy + b_ * s) for a, b_ in pts], c, sw, 1)
    if kind == "mate":
        return P([(-.55, .02), (-.36, .02), (-.14, .46), (.1, -.46), (.56, -.46)]) + \
            P([(.2, -.12), (.5, .3)]) + P([(.5, -.12), (.2, .3)])
    if kind == "lc":
        g = []
        for dx in (-.26, .26):
            g.append(f'<circle cx="{cx + dx * s:.1f}" cy="{cy - .08 * s:.1f}" r="{.17 * s:.1f}" fill="{c}"/>')
            g.append(P([(dx + .15, -.06), (dx + .04, .38)]))
        return "".join(g)
    if kind == "soc":
        g = [P([(-.55, -.18), (0, -.52), (.55, -.18), (-.55, -.18)]), P([(-.55, .48), (.55, .48)])]
        for dx in (-.36, 0, .36):
            g.append(P([(dx, -.08), (dx, .38)]))
        return "".join(g)
    if kind == "bio":
        ts = [i / 14 for i in range(15)]
        lado = lambda sg: [(-.45 + .9 * t + sg * .26 * math.sin(math.pi * t),
                            .45 - .9 * t + sg * .26 * math.sin(math.pi * t)) for t in ts]
        return P(lado(1) + lado(-1)[::-1]) + P([(-.58, .58), (.22, -.22)])
    if kind == "qui":
        return P([(-.16, -.52), (-.16, -.14), (-.48, .46), (.48, .46), (.16, -.14), (.16, -.52)]) + \
            P([(-.26, -.52), (.26, -.52)]) + P([(-.32, .2), (.32, .2)])
    if kind == "fis":
        g = [f'<circle cx="{cx}" cy="{cy}" r="{.1 * s:.1f}" fill="{c}"/>']
        for a in (0, 60, 120):
            g.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{.56 * s:.1f}" ry="{.2 * s:.1f}" fill="none" '
                     f'stroke="{c}" stroke-width="{sw:.1f}" transform="rotate({a} {cx} {cy})"/>')
        return "".join(g)
    if kind == "ing":
        return (P([(-.5, -.42), (.5, -.42), (.5, .2), (-.05, .2), (-.3, .46), (-.26, .2), (-.5, .2), (-.5, -.42)])
                + TX(cx, cy + .06 * s, "Hi", round(.36 * s), c, BRI, "800", anchor="middle"))
    return ""


ICON = ["mate", "lc", "soc", "bio", "qui", "fis", "ing"]
INDICE = [("Apertura", "1–9", None), ("Matemáticas", "10–52", 0), ("Lectura Crítica", "53–95", 1),
          ("Sociales y Ciudadanas", "96–138", 2), ("Biología", "139–181", 3), ("Química", "182–224", 4),
          ("Física", "225–267", 5), ("Inglés", "268–344", 6), ("Cierre", "345–347", None)]
FRASE = ("Este cuaderno no trae las respuestas.",
         "Trae la forma de pensarlas. Las respuestas las pones tú,",
         "con lápiz, después de escribir cómo llegaste a ellas.")


# ════════════════════════════ 1 · PORTADAS ════════════════════════════
def portada_A():
    random.seed(5)
    b = pagina(PAPEL_A)
    # recortes de fondo
    b.append(torn(-30, -30, W + 30, 1000, KRAFT, bordes="b", amp=12, seed=101, fibra=None))
    b.append(torn(-30, -30, W + 30, 975, EDU_AZUL, bordes="b", amp=12, seed=102))
    b.append(rot_g(torn(1130, 70, 1470, 300, EDU_ORO, bordes="tblr", amp=8, seed=103), -7, 1300, 185))
    b.append(rot_g(torn(560, 330, 900, 560, EDU_ROJO, bordes="tblr", amp=8, seed=104), 8, 730, 445))
    b.append(rot_g(torn(1250, 400, 1420, 520, AREAS[6][1], bordes="tblr", amp=6, seed=108), 12, 1335, 460))
    # polaroid con el logo
    pw, ph = 560, 410
    g = [rect(W / 2 - pw / 2 + 8, 110 + 10, pw, ph, "#1A1A5A", r=4),
         rect(W / 2 - pw / 2, 110, pw, ph, "white", r=4),
         logo(W / 2 - logo_w(170) / 2, 150, 170),
         TX(W / 2, 470, "mi cuaderno · Saber 11", 44, TINTA_A, HAND, "700", anchor="middle")]
    b.append(rot_g("".join(g), -3, W / 2, 315))
    b.append(tape(W / 2 - 230, 112, 170, 46, -28, CINTAS[2], seed=105))
    b.append(tape(W / 2 + 236, 118, 170, 46, 30, CINTAS[0], seed=106))
    b.append(TX(W / 2, 680, "Cuaderno de trabajo", 120, "white", DMS, anchor="middle"))
    b.append(TX(W / 2, 760, "Saber 11 · las siete áreas de tu libro en un solo cuaderno", 36, "#C9D3F2",
                anchor="middle"))
    b.append(TX(W / 2, 870, "Aprende · Practica · Avanza", 60, "#F7C873", HAND, "700", anchor="middle"))
    # ficha de identidad (se escribe: blanca)
    fx, fy, fw, fh = M + 10, 1080, 1180, 500
    g = [rect(fx + 10, fy + 12, fw, fh, KRAFT, r=4), rect(fx, fy, fw, fh, "white", r=4),
         TX(fx + 50, fy + 80, "Este cuaderno es de", 46, TINTA_A, HAND, "700")]
    for i, (lab, w_) in enumerate([("Nombre", 780), ("Colegio", 780), ("Grado y jornada", 520)]):
        yy = fy + 190 + i * 110
        g.append(TX(fx + 50, yy, lab, 32, EDU_AZUL, DMS))
        g.append(line(fx + 330, yy + 6, fx + 330 + w_, yy + 6, LGRAY, 2.6))
    b.append(rot_g("".join(g), -1.2, fx + fw / 2, fy + fh / 2))
    b.append(tape(fx + 60, fy + 4, 180, 48, -36, CINTAS[1], seed=107))
    # sticker de la meta
    cx, cy = W - M - 330, 1330
    g = [f'<circle cx="{cx + 8}" cy="{cy + 10}" r="230" fill="{KRAFT}"/>',
         f'<circle cx="{cx}" cy="{cy}" r="230" fill="white"/>',
         f'<circle cx="{cx}" cy="{cy}" r="212" fill="{NOTA}"/>',
         TX(cx, cy - 92, "MI META", 34, EDU_ORO, weight="700", anchor="middle", ls=4),
         TX(cx, cy + 30, "_____", 80, EDU_AZUL, DMS, anchor="middle"),
         TX(cx, cy + 92, "puntaje global", 28, TINTA_A, anchor="middle"),
         TX(cx, cy + 132, "(la defines en la hoja 4)", 24, GRAY, style="italic", anchor="middle")]
    b.append(rot_g("".join(g), 6, cx, cy))
    # las siete áreas: etiquetas de papel
    y2 = 1700
    b.append(TX(M, y2, "Las siete áreas que vas a entrenar aquí", 50, EDU_AZUL, DMS))
    b.append(TX(M, y2 + 46, "(en el Saber 11, Biología, Química y Física se evalúan juntas en Ciencias Naturales)",
                24, GRAY, style="italic"))
    gw = (CW - 6 * 22) / 7
    for i, (nm, c) in enumerate(AREAS):
        x = M + i * (gw + 22)
        yy = y2 + 90
        g = [torn(x, yy, x + gw, yy + 200, c, bordes="tblr", amp=5, paso=18, seed=120 + i),
             TX(x + 22, yy + 72, f"{i + 1}", 64, "white", HAND, "700")]
        lines = wrap_px(nm, 29, gw - 40, "700")
        for j, ln in enumerate(lines):
            g.append(TX(x + 22, yy + 140 + j * 34 - 17 * (len(lines) - 1), " ".join(ln), 29, "white", weight="700"))
        b.append(rot_g("".join(g), (-2.2, 1.6, -1, 2.4, -1.8, 1.2, -2.6)[i], x + gw / 2, yy + 100))
        if i % 2 == 0:
            b.append(tape(x + gw / 2, yy + 2, 110, 34, (-8, 6, -4, 9)[i // 2], CINTAS[(i // 2) % 4], seed=130 + i))
    # la frase: hoja de cuaderno con margen vertical
    y3 = 2090
    g = [rect(M + 10, y3 + 12, CW - 10, 360, KRAFT, r=4), rect(M, y3, CW - 10, 360, "white", r=4),
         line(M + 90, y3 + 10, M + 90, y3 + 350, "#F2B8B0", 2.5),
         TX(M + 130, y3 + 100, FRASE[0], 60, EDU_AZUL, DMS),
         TX(M + 130, y3 + 180, FRASE[1], 33, INK), TX(M + 130, y3 + 228, FRASE[2], 33, INK)]
    b.append(rot_g("".join(g), 0.6, W / 2, y3 + 180))
    b.append(face(W - M - 180, y3 + 200, 92, "determined", EDU_AZUL, "#FFE9A8"))
    b.append(hand_arrow(W - M - 560, y3 + 316, W - M - 300, y3 + 250, EDU_ORO, sw=5, bend=-0.3))
    b.append(TX(W - M - 760, y3 + 330, "ese eres tú", 48, EDU_ORO, HAND, "700", rot=-3))
    b.append(TX(W / 2, H_PAGE - 50, "EDUCATE · Para el Saber", 24, GRAY, anchor="middle"))
    return b


def sello_redondo(cx, cy, r, lineas, c, ang):
    """Sello de caucho redondo: doble aro y cuatro líneas de texto."""
    g = [f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="5"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r - 14}" fill="none" stroke="{c}" stroke-width="2"/>']
    tam = [30, 34, 26, 26]
    ys = [-46, 0, 44, 80]
    for t, s_, dy in zip(lineas, tam, ys):
        fam, wt = (MONO, "700") if t.isupper() else (HAND, "700")
        s_ = fit(t, s_ if t.isupper() else s_ + 8, fam, wt, 2 * r - 70)
        g.append(TX(cx, cy + dy, t, s_, c, fam, wt, anchor="middle"))
    g.append(estrellita(cx - r * .55, cy - r * .62, 8, c, 2))
    g.append(estrellita(cx + r * .55, cy - r * .62, 8, c, 2))
    return rot_g("".join(g), ang, cx, cy)


def portada_B():
    random.seed(6)
    S = ESTILOS["B"]
    b = pagina("#FFFFFF")
    S.fondo(b)
    b.append(rect(M - 14, 70, logo_w(110) + 28, 136, "white", r=4))
    b.append(logo(M, 82, 110))
    t = "CUADERNO DE TRABAJO"
    b.append(rect(W - M - twf(t, 28, MONO, "700") - 20, 104, twf(t, 28, MONO, "700") + 20, 52, "white", r=2))
    b.append(TX(W - M - 10, 140, t, 28, TINTA_B, MONO, "700", anchor="end"))
    # título gigante
    s1 = "Saber"
    b.append(TX(M - 8, 560, s1, 300, TINTA_B, SHA, "800"))
    x11 = M + twf(s1, 300, SHA, "800") + 30
    w11 = twf("11", 300, SHA, "800")
    b.append(resaltador(x11 - 10, 330, w11 + 20, 220, FOSFO, seed=201, rot=-2))
    b.append(TX(x11, 560, "11", 300, TINTA_B, SHA, "800"))
    b.append(estrellita(x11 + w11 + 70, 300, 34, EDU_ROJO, 4))
    b.append(estrellita(x11 + w11 + 130, 400, 18, EDU_AZUL, 3))
    sub = "las siete áreas de tu libro en un solo cuaderno"
    b.append(rect(M - 8, 610, twf(sub, 44, SHA, "400") + 16, 64, "white", r=2))
    b.append(TX(M, 656, sub, 44, TINTA_B, SHA))
    # Aprende → Practica → Avanza como sellos
    x = M
    for k, pal in enumerate(["Aprende", "Practica", "Avanza"]):
        w = twf(pal.upper(), 26, MONO, "700") + 40
        b.append(rot_g(rect(x, 720, w, 60, "white", r=4, stroke=EDU_AZUL, sw=3)
                       + rect(x + 5, 725, w - 10, 50, "none", r=2, stroke=EDU_AZUL, sw=1.4)
                       + TX(x + w / 2, 760, pal.upper(), 26, EDU_AZUL, MONO, "700", anchor="middle"),
                       (-2, 1.5, -1)[k], x + w / 2, 750))
        x += w + 20
        if k < 2:
            b.append(hand_arrow(x - 8, 752, x + 46, 752, EDU_ORO, sw=3.5, bend=0.25, head=14))
            x += 64
    b.append(sello_redondo(1640, 520, 150, ("PRIMERO EL", "ANDAMIAJE", "después la", "respuesta"), EDU_ROJO, -12))
    # columna izquierda: de quién es y la meta
    lx, ly, lw = M, 900, 900
    b.append(wob_rect(lx, ly, lw, 560, TINTA_B, 3, fill="white", seed=210))
    b.append(TX(lx + 40, ly + 66, "ESTA BITÁCORA ES DE", 24, TINTA_B, MONO, "700"))
    for i, lab in enumerate(["Nombre", "Colegio", "Grado y jornada"]):
        yy = ly + 170 + i * 120
        b.append(TX(lx + 40, yy, lab, 28, EDU_AZUL, SHA, "700"))
        b.append(line(lx + 40, yy + 52, lx + lw - 40, yy + 52, LGRAY, 2.6))
    mx, my = lx, ly + 610
    b.append(wob_rect(mx, my, lw, 460, TINTA_B, 3, fill="white", seed=211))
    b.append(resaltador(mx + 36, my + 40, twf("MI META", 30, MONO, "700"), 34, FOSFO_2, seed=212))
    b.append(TX(mx + 36, my + 68, "MI META", 30, TINTA_B, MONO, "700"))
    b.append(wob_circle(mx + 300, my + 260, 150, EDU_ORO, 4, seed=213, vueltas=1.2, fill="white"))
    b.append(TX(mx + 300, my + 270, "_____", 70, EDU_AZUL, SHA, "700", anchor="middle"))
    b.append(TX(mx + 300, my + 320, "puntaje global", 24, GRAY, anchor="middle"))
    b.append(TX(mx + 540, my + 190, "la defines en", 38, EDU_ORO, HAND, "700"))
    b.append(TX(mx + 540, my + 234, "la hoja 4", 38, EDU_ORO, HAND, "700"))
    b.append(hand_arrow(mx + 620, my + 262, mx + 470, my + 310, EDU_ORO, sw=3.5, bend=-0.35, head=16))
    # columna derecha: índice
    rx, ry, rw = M + 960, 900, CW - 960
    b.append(wob_rect(rx, ry, rw, 1070, TINTA_B, 3, fill="white", seed=220))
    b.append(resaltador(rx + 40, ry + 36, twf("ÍNDICE", 34, MONO, "700"), 38, FOSFO, seed=221))
    b.append(TX(rx + 40, ry + 68, "ÍNDICE", 34, TINTA_B, MONO, "700"))
    b.append(TX(rx + 260, ry + 66, "las siete áreas que vas a entrenar aquí", 22, GRAY, style="italic"))
    yy = ry + 150
    for nm, pags, ia in INDICE:
        c = AREAS[ia][1] if ia is not None else GRAY
        if ia is not None:
            b.append(rect(rx + 40, yy - 34, 44, 44, c, r=6))
            b.append(TX(rx + 62, yy - 2, str(ia + 1), 24, "white", MONO, "700", anchor="middle"))
        else:
            b.append(wob_rect(rx + 42, yy - 32, 40, 40, GRAY, 2, seed=int(yy), amp=.8, sobre=3))
        b.append(TX(rx + 110, yy, nm, 34, TINTA_B if ia is not None else GRAY, SHA, "700"))
        b.append(TX(rx + rw - 40, yy, f"p. {pags}", 24, c, MONO, "700", anchor="end"))
        yy += 96
    b.append(TX(rx + 40, ry + 1010, "En el Saber 11, Biología, Química y Física", 30, GRAY, HAND, "700"))
    b.append(TX(rx + 40, ry + 1046, "se evalúan juntas en Ciencias Naturales.", 30, GRAY, HAND, "700"))
    # la frase
    y3 = 2050
    b.append(wob_rect(M, y3, CW, 400, TINTA_B, 3, fill="white", seed=230))
    w0 = twf(FRASE[0], 52, SHA, "800")
    b.append(resaltador(M + 50, y3 + 62, w0, 50, FOSFO, seed=231))
    b.append(TX(M + 50, y3 + 104, FRASE[0], 52, TINTA_B, SHA, "800"))
    b.append(TX(M + 50, y3 + 186, FRASE[1], 33, INK))
    b.append(TX(M + 50, y3 + 234, FRASE[2], 33, INK))
    b.append(face(W - M - 190, y3 + 210, 92, "determined", TINTA_B, "#FFE9A8"))
    b.append(hand_arrow(W - M - 560, y3 + 330, W - M - 310, y3 + 262, EDU_ORO, sw=5, bend=-0.3))
    b.append(TX(W - M - 760, y3 + 350, "ese eres tú", 48, EDU_ORO, HAND, "700", rot=-3))
    t = "EDUCATE · PARA EL SABER"
    b.append(rect(W / 2 - twf(t, 20, MONO) / 2 - 10, H_PAGE - 80, twf(t, 20, MONO) + 20, 40, "white", r=2))
    b.append(TX(W / 2, H_PAGE - 52, t, 20, GRAY, MONO, anchor="middle"))
    return b


def estallido(cx, cy, r, fill, lineas, ang):
    """Sticker en estrella de 16 puntas con borde grueso y sombra sólida."""
    def poly(dx, dy):
        p = []
        for i in range(32):
            rr = r if i % 2 == 0 else r * 0.84
            a = i * math.pi / 16
            p.append((cx + dx + rr * math.cos(a), cy + dy + rr * math.sin(a)))
        return _pts(p)
    g = [f'<polygon points="{poly(8, 8)}" fill="{TINTA_C}"/>',
         f'<polygon points="{poly(0, 0)}" fill="{fill}" stroke="{TINTA_C}" stroke-width="4" stroke-linejoin="round"/>']
    for k, t in enumerate(lineas):
        g.append(TX(cx, cy - 6 + k * 46, t, fit(t, 36, BRI, "800", 2 * r * .72), TINTA_C, BRI, "800", anchor="middle"))
    return rot_g("".join(g), ang, cx, cy)


def portada_C():
    b = pagina("#FFFFFF")
    # bloque grande
    b.append(bloque(M, 60, CW - 16, 900, EDU_AZUL, sombra=EDU_ORO, d=16, sw=5, r=18))
    b.append(bloque(M + 50, 110, logo_w(110) + 60, 150, "white", d=8))
    b.append(logo(M + 80, 130, 110))
    b.append(TX(W - M - 70, 190, "CUADERNO DE TRABAJO", 40, "white", BRI, "800", anchor="end", ls=3))
    s = fit("SABER 11", 360, BRI, "800", CW - 120)
    b.append(TX(M + 50, 640, "SABER 11", s, AMARILLO, BRI, "800"))
    b.append(TX(M + 56, 730, "las siete áreas de tu libro en un solo cuaderno", 40, "white", BRI, "700"))
    x = M + 56
    for k, pal in enumerate(["Aprende", "Practica", "Avanza"]):
        w = twf(pal, 34, BRI, "800") + 56
        b.append(bloque(x, 790, w, 76, (AMARILLO, "white", AMARILLO)[k], d=6, sw=3.5, r=38))
        b.append(TX(x + w / 2, 840, pal, 34, TINTA_C, BRI, "800", anchor="middle"))
        x += w + 26
    b.append(estallido(W - M - 250, 820, 140, "white", ("PRIMERO EL", "ANDAMIAJE"), -10))
    # identidad y meta
    y = 1040
    b.append(bloque(M, y, 1200, 520, "white", sombra=EDU_AZUL, d=12, sw=4.5, r=16))
    b.append(TX(M + 50, y + 80, "ESTE CUADERNO ES DE", 30, TINTA_C, BRI, "800", ls=2))
    for i, (lab, w_) in enumerate([("Nombre", 760), ("Colegio", 760), ("Grado y jornada", 500)]):
        yy = y + 200 + i * 110
        b.append(TX(M + 50, yy, lab, 28, EDU_AZUL, weight="700"))
        b.append(rect(M + 330, yy - 42, w_, 60, "white", r=8, stroke=TINTA_C, sw=2.5))
    mx = M + 1250
    mw = W - M - 16 - mx
    b.append(bloque(mx, y, mw, 520, AMARILLO, d=12, sw=4.5, r=16))
    b.append(TX(mx + mw / 2, y + 84, "MI META", 44, TINTA_C, BRI, "800", anchor="middle", ls=3))
    b.append(rect(mx + 60, y + 130, mw - 120, 170, "white", r=12, stroke=TINTA_C, sw=3.5))
    b.append(TX(mx + mw / 2, y + 360, "puntaje global", 30, TINTA_C, weight="700", anchor="middle"))
    b.append(TX(mx + mw / 2, y + 404, "(la defines en la hoja 4)", 24, TINTA_C, style="italic", anchor="middle"))
    # siete áreas
    y2 = 1650
    b.append(TX(M, y2, "Las siete áreas que vas a entrenar aquí", 50, TINTA_C, BRI, "800"))
    b.append(TX(M, y2 + 44, "(en el Saber 11, Biología, Química y Física se evalúan juntas en Ciencias Naturales)",
                24, GRAY, style="italic"))
    gw = (CW - 16 - 6 * 24) / 7
    for i, (nm, c) in enumerate(AREAS):
        x = M + i * (gw + 24)
        yy = y2 + 90
        b.append(bloque(x, yy, gw, 290, c, d=8, sw=4, r=14))
        b.append(TX(x + 20, yy + 56, f"{i + 1:02d}", 40, "white", BRI, "800"))
        b.append(icono(ICON[i], x + gw - 54, yy + 50, 62, "white", sw=5))
        lns = wrap_px(nm, 28, gw - 36, "700")
        for j, ln in enumerate(lns):
            b.append(TX(x + 20, yy + 236 + j * 34 - 34 * (len(lns) - 1), " ".join(ln), 28, "white", BRI, "800"))
    # frase
    y3 = 2120
    b.append(bloque(M, y3, CW - 16, 320, "white", sombra=EDU_ROJO, d=12, sw=4.5, r=16))
    b.append(TX(M + 50, y3 + 96, FRASE[0], fit(FRASE[0], 56, BRI, "800", 1300), TINTA_C, BRI, "800"))
    b.append(TX(M + 50, y3 + 176, FRASE[1], 32, INK))
    b.append(TX(M + 50, y3 + 222, FRASE[2], 32, INK))
    b.append(face(W - M - 200, y3 + 160, 96, "determined", TINTA_C, AMARILLO, sw=4.5))
    t = "ese eres tú"
    w = twf(t, 30, BRI, "800") + 50
    b.append(bloque(W - M - 600, y3 + 220, w, 60, LILA, d=5, sw=3, r=30))
    b.append(TX(W - M - 600 + w / 2, y3 + 261, t, 30, TINTA_C, BRI, "800", anchor="middle"))
    x1, y1_, x2, y2_ = W - M - 600 + w + 14, y3 + 240, W - M - 300, y3 + 184
    a = math.atan2(y2_ - y1_, x2 - x1)
    b.append(line(x1, y1_, x2 - 14 * math.cos(a), y2_ - 14 * math.sin(a), TINTA_C, 5))
    hd = [(x2, y2_), (x2 - 26 * math.cos(a - .45), y2_ - 26 * math.sin(a - .45)),
          (x2 - 26 * math.cos(a + .45), y2_ - 26 * math.sin(a + .45))]
    b.append(f'<polygon points="{_pts(hd)}" fill="{TINTA_C}"/>')
    b.append(TX(W / 2, H_PAGE - 50, "EDUCATE · Para el Saber", 24, GRAY, anchor="middle"))
    return b


# ════════════════════════════ 2 · METAS («Ponle un número a tu meta») ════════════════════════════
class Ap:
    """Ganchos de estilo para una hoja de apertura."""

    def __init__(self, k):
        self.k = k

    def cabecera(self, b, seccion, sub, c):
        k = self.k
        if k == "A":
            b.append(torn(-20, -20, W + 20, 150, CREMA, bordes="b", amp=8, seed=301))
            b.append(logo(M, 40, 70))
            b.append(TX(W - M, 82, seccion.lower(), 54, c, HAND, "700", anchor="end"))
            b.append(TX(W - M, 120, sub, 21, GRAY, anchor="end", style="italic"))
            b.append(tape(W - M - 60, 150, 150, 40, -6, CINTAS[2], seed=302))
            return 216
        if k == "B":
            b.append(rect(M - 10, 36, logo_w(70) + 20, 94, "white", r=4))
            b.append(logo(M, 48, 70))
            t = f"§ {seccion.upper()}"
            w = twf(t, 26, MONO, "700")
            b.append(resaltador(W - M - w, 54, w, 34, FOSFO_2, seed=303))
            b.append(TX(W - M, 82, t, 26, TINTA_B, MONO, "700", anchor="end"))
            st = sub.upper()
            b.append(rect(W - M - twf(st, 16, MONO) - 8, 100, twf(st, 16, MONO) + 8, 30, "white", r=2))
            b.append(TX(W - M, 120, st, 16, GRAY, MONO, anchor="end"))
            b.append(estrellita(W - M - w - 50, 70, 13, c))
            return 216
        b.append(bloque(M, 30, 210, 120, "white", d=8))
        b.append(logo(M + 105 - logo_w(66) / 2, 57, 66))
        t = seccion.upper()
        w = twf(t, 34, BRI, "800") + 60
        b.append(bloque(W - M - w - 8, 30, w, 70, c, d=8, r=10))
        b.append(TX(W - M - 8 - w / 2, 78, t, 34, "white", BRI, "800", anchor="middle", ls=2))
        b.append(TX(W - M - 8, 138, sub, 21, GRAY, anchor="end", style="italic"))
        return 216

    def titulo(self, b, y, txt, sub, c):
        k = self.k
        if k == "A":
            b.append(TX(M, y + 78, txt, 92, c, DMS))
            yy = y + 112
        elif k == "B":
            # resaltador detrás de «un número»
            a, m_ = "Ponle ", "un número"
            x2 = M + twf(a, 80, SHA, "800")
            b.append(resaltador(x2, y + 20, twf(m_, 80, SHA, "800"), 64, FOSFO, seed=311))
            b.append(TX(M, y + 78, txt, 80, TINTA_B, SHA, "800"))
            yy = y + 112
        else:
            a, m_, z = "Ponle", "un número", "a tu meta"       # = txt, con el bloque amarillo en medio
            x2 = M + twf(a, 86, BRI, "800") + 30
            w2 = twf(m_, 86, BRI, "800")
            b.append(bloque(x2 - 18, y + 4, w2 + 36, 100, AMARILLO, d=7, sw=4, r=10))
            b.append(TX(M, y + 80, a, 86, TINTA_C, BRI, "800"))
            b.append(TX(x2, y + 80, m_, 86, TINTA_C, BRI, "800"))
            b.append(TX(x2 + w2 + 48, y + 80, z, 86, TINTA_C, BRI, "800"))
            yy = y + 124
        if k == "B":
            lines = wrap_px(sub, 28, CW, "400", "italic")
            b.append(rect(M - 8, yy - 6, CW + 16, 40 * len(lines) + 12, "white", r=2))
        svg, yy = TJ(M, yy, sub, CW, 28, GRAY, style="italic", lh=40)
        b.append(svg)
        return yy + 16

    def panel(self, b, x, y, w, h, tipo, c, seed=0):
        k = self.k
        if k == "A":
            if tipo == "escala":
                b.append(torn(x, y, x + w, y + h, "#F3EBDB", bordes="tblr", amp=5, seed=320 + seed, fibra=None))
                b.append(tape(x + w / 2, y + 4, 180, 44, -3, CINTAS[3], seed=321))
            elif tipo == "nota":
                b.append(rect(x, y, w, h, NOTA, r=2))
            else:
                b.append(rect(x + 8, y + 10, w, h, KRAFT, r=4))
                b.append(rect(x, y, w, h, "white", r=4))
                b.append(clip(x + w - 70, y - 22))
        elif k == "B":
            b.append(wob_rect(x, y, w, h, TINTA_B if tipo != "nota" else c, 2.8, fill="white", seed=330 + seed))
        else:
            if tipo == "escala":
                b.append(bloque(x, y, w - 10, h, "#F1F2FB", sombra=EDU_AZUL, d=10, sw=4, r=16))
            elif tipo == "nota":
                b.append(rect(x, y, w, h, "white", r=12, stroke=TINTA_C, sw=3))
            else:
                b.append(bloque(x, y, w - 10, h, "white", sombra=c, d=10, sw=4, r=16))

    def h2(self, b, x, y, txt, c, size=32):
        k = self.k
        if k == "A":
            b.append(TX(x, y, txt, size + 4, c, DMS))
        elif k == "B":
            b.append(TX(x, y, txt, size - 2, c, SHA, "800"))
        else:
            b.append(TX(x, y, txt, size - 2, c, BRI, "800"))

    def caja(self, b, x, y, w, h, c):
        k = self.k
        if k == "A":
            b.append(rect(x, y, w, h, "white", r=4, stroke=c, sw=3))
        elif k == "B":
            b.append(wob_rect(x, y, w, h, c, 3, fill="white", seed=int(x)))
        else:
            b.append(rect(x + 6, y + 6, w, h, c, r=10))
            b.append(rect(x, y, w, h, "white", r=10, stroke=TINTA_C, sw=3.5))

    def mano(self, b, x, y, txt, c, size=40):
        b.append(TX(x, y, txt, size, c, HAND, "700", rot=-0.6))


def metas(k):
    random.seed(41)
    S = ESTILOS[k]
    ap = Ap(k)
    c0 = EDU_ORO
    b = pagina(S.papel)
    S.fondo(b)
    y = ap.cabecera(b, "Metas", "¿para qué estoy entrenando?", c0)
    y = ap.titulo(b, y + 10, "Ponle un número a tu meta",
                  "El Saber 11 se califica de 0 a 500 en el puntaje global y de 0 a 100 en cada área. "
                  "Una meta sin número no se puede entrenar.", c0)
    top = y + 14
    ink = {"A": TINTA_A, "B": TINTA_B, "C": TINTA_C}[k]
    eje = EDU_AZUL if k != "C" else TINTA_C
    # ── escala ──
    LX, LW, LH = M, 1000, 1250
    ap.panel(b, LX, top, LW, LH, "escala", c0, 1)
    ap.h2(b, LX + 40, top + 70, "La escala del puntaje global", EDU_AZUL if k != "C" else TINTA_C)
    ax, y0, y1 = LX + 130, top + 1160, top + 140

    def yv(v):
        return y0 - (y0 - y1) * v / 500
    if k == "C":      # columna de bloques: 10 tramos de 50
        for i in range(10):
            v = i * 50
            zona = (EDU_ROJO if v >= 400 else EDU_VERDE if v >= 350 else EDU_AZUL if v >= 300
                    else GRAY if v >= 250 else None)
            b.append(rect(ax - 16, yv((i + 1) * 50), 32, yv(i * 50) - yv((i + 1) * 50),
                          tb._mezcla(zona, 0.55) if zona else "white", r=0, stroke=TINTA_C, sw=3))
    elif k == "B":
        b.append(spath([(ax + random.uniform(-1, 1), yy) for yy in range(int(y1), int(y0) + 1, 40)], eje, 5, 1))
    else:
        b.append(line(ax, y0, ax, y1, eje, 6))
    for v in range(0, 501, 50):
        if k != "C":
            b.append(line(ax - 14, yv(v), ax + 14, yv(v), eje, 3))
        fam = MONO if k == "B" else (BRI if k == "C" else None)
        b.append(TX(ax - 30, yv(v) + 9, str(v), 22, GRAY, fam, "700" if k == "C" else "400", anchor="end"))
    marcas = [(250, "Promedio nacional aproximado", "la mitad de los estudiantes queda por debajo", GRAY),
              (300, "Corte de admisión en universidades privadas", "p. ej. Universidad de los Andes 2026-2: 300 a 320", EDU_AZUL),
              (350, "Becas y oportunidades", "desde aquí se abren becas, créditos condonables y cupos que no dependen de pagar", EDU_VERDE),
              (420, "Carreras más exigidas", "Medicina, Ingeniería civil, Derecho en universidades top", EDU_ROJO)]
    for v, t, d, c in marcas:
        yy = yv(v)
        b.append(line(ax + 20, yy, ax + 70, yy, c, 3, "6,6"))
        if k == "C":
            b.append(rect(ax + 68, yy - 11, 22, 22, c, r=3, stroke=TINTA_C, sw=2.5))
        elif k == "B":
            b.append(wob_circle(ax + 78, yy, 11, c, 3, seed=v, fill="white"))
        else:
            b.append(f'<circle cx="{ax + 78}" cy="{yy}" r="10" fill="{c}"/>')
        b.append(TX(ax + 102, yy - 6, f"{v}  ·  {t}", 27, c, weight="700"))
        for j, ln in enumerate(wrap_px(d, 22, LW - 250, "400", "italic")):
            b.append(TX(ax + 102, yy + 28 + j * 28, " ".join(ln), 22, GRAY, style="italic"))
    nx, ny = LX + 560, top + 950
    ap.panel(b, nx, ny, 400, 240, "nota", c0, 2)
    b.append(TX(nx + 24, ny + 46, "Marca con lápiz sobre la escala:", 22, c0 if k != "C" else TINTA_C, weight="700"))
    b.append(spath([(nx + 32, ny + 94), (nx + 80, ny + 94)], EDU_ORO, 6))
    b.append(TX(nx + 100, ny + 102, "HOY · tu primer simulacro", 22, INK))
    b.append(spath([(nx + 32, ny + 150), (nx + 80, ny + 150)], EDU_AZUL, 6))
    b.append(TX(nx + 100, ny + 158, "META · el puntaje que necesitas", 22, INK))
    b.append(TX(nx + 24, ny + 206, "Entre las dos rayas está tu trabajo.", 21, GRAY, style="italic"))
    # ── tabla de carreras ──
    RX = LX + LW + 40
    RW = W - M - RX
    ap.panel(b, RX, top, RW, LH, "tabla", c0, 3)
    ap.h2(b, RX + 36, top + 70, "Puntaje global de referencia", c0 if k != "C" else TINTA_C, 30)
    b.append(TX(RX + 36, top + 106, "por carrera · rango aproximado reportado en 2026", 21, GRAY, style="italic"))
    yy = top + 160
    bar = {"A": EDU_ORO, "B": EDU_ORO, "C": EDU_ORO}[k]
    for i, (nm, lo, hi) in enumerate(CARRERAS):
        if i % 2:
            b.append(rect(RX + 20, yy - 28, RW - 50, 50, {"A": "#F7F1E4", "B": "#F4F6FA", "C": "#F3F4F7"}[k], r=8))
        b.append(TX(RX + 36, yy + 8, nm, 24, INK))
        bx0, bx1 = RX + 430, RX + RW - 150

        def px(v):
            return bx0 + (bx1 - bx0) * (v - 250) / 250
        b.append(line(px(250), yy, px(500), yy, "#E6EAF0", 8))
        if k == "B":
            b.append(resaltador(px(lo), yy - 9, px(hi) - px(lo), 18, "#F2C36B", seed=i, rot=0))
        elif k == "C":
            b.append(rect(px(lo), yy - 9, px(hi) - px(lo), 18, bar, r=2, stroke=TINTA_C, sw=2))
        else:
            b.append(line(px(lo), yy, px(hi), yy, bar, 8))
        b.append(TX(RX + RW - 44, yy + 8, f"{lo}–{hi}", 21, GRAY, MONO if k == "B" else None, anchor="end"))
        yy += 54
    b.append(TX(RX + 36, top + 1186, "Son referencias de prensa, no cortes oficiales. Cada universidad fija el suyo:",
                19, GRAY, style="italic"))
    b.append(TX(RX + 36, top + 1214, "confírmalo en la página de admisiones de la que tú quieres.", 19, GRAY,
                style="italic"))
    # ── mi cuenta ──
    y = top + LH + 60
    ap.panel(b, M, y, CW, 560, "cuenta", c0, 4)
    ap.h2(b, M + 40, y + 70, "Mi cuenta", EDU_AZUL if k != "C" else TINTA_C, 38)
    wmc = twf("Mi cuenta", {"A": 42, "B": 36, "C": 36}[k], {"A": DMS, "B": SHA, "C": BRI}[k],
              {"A": "400", "B": "800", "C": "800"}[k])
    b.append(TX(M + 60 + wmc, y + 68, "— la escribes ahora y la vuelves a mirar después de cada simulacro",
                23, GRAY, style="italic"))
    xx = M + 40
    for lab, w_ in [("La carrera que quiero", 560), ("En la universidad", 560), ("Puntaje que necesito", 300)]:
        b.append(TX(xx, y + 140, lab, 23, EDU_AZUL if k != "C" else TINTA_C, weight="700"))
        b.append(line(xx, y + 200, xx + w_, y + 200, LGRAY, 2.6))
        xx += w_ + 60
    oy = y + 290
    cajas_ = [("Puntaje que necesito", EDU_AZUL), ("−", None), ("Mi puntaje hoy", EDU_ORO), ("=", None),
              ("Lo que me falta", EDU_ROJO), ("÷", None), ("Semanas que faltan", GRAY), ("=", None),
              ("Puntos por semana", EDU_VERDE)]
    xx, bw = M + 40, 286
    for lab, c in cajas_:
        if c is None:
            b.append(TX(xx + 30, oy + 80, lab, 54, ink, weight="700", anchor="middle"))
            xx += 60
        else:
            ap.caja(b, xx, oy, bw, 120, c)
            b.append(TX(xx + bw / 2, oy + 156, lab, 20, c, weight="700", anchor="middle"))
            xx += bw + 10
    ap.mano(b, M + 60, y + 520, "Si el número de puntos por semana te asusta, bien: ya sabes cuánto vale cada sábado.",
            EDU_AZUL if k != "C" else TINTA_C, 36)
    S.pie(b, 4, c0, "Cuaderno de trabajo · Saber 11")
    return b


PORTADAS = {"A": portada_A, "B": portada_B, "C": portada_C}

# ════════════════════════════ lámina resumen ════════════════════════════
FICHAS = {
    "A": dict(nombre="Recortes", tipo="scrapbook · diario de collage",
              palabras="hecho a mano · cálido · íntimo · de colección", fam=DMS, peso="400",
              tipo_txt="DM Serif Display (títulos) + Caveat (rótulos a mano)",
              acentos=[(PAPEL_A, "papel"), (KRAFT, "kraft"), (NOTA, "nota"), (CINTAS[0], "cinta"),
                       (CINTAS[1], "cinta"), (CINTAS[3], "cinta")]),
    "B": dict(nombre="Bitácora", tipo="bullet journal · zine",
              palabras="ordenado · ingenioso · de estudio · con garabatos", fam=SHA, peso="800",
              tipo_txt="Shantell Sans (títulos) + Space Mono (rótulos)",
              acentos=[(FOSFO, "resaltador"), (FOSFO_2, "menta"), (DOT, "puntos"), (TINTA_B, "tinta")]),
    "C": dict(nombre="Bloque", tipo="neo-brutalismo · tarjetas de color",
              palabras="directo · gráfico · seguro · con energía", fam=BRI, peso="800",
              tipo_txt="Bricolage Grotesque ExtraBold (títulos)",
              acentos=[(TINTA_C, "tinta"), (AMARILLO, "amarillo"), (LILA, "lila")]),
}


def _anidar(ruta, x, y, w):
    """Mete una hoja SVG entera, en vectores, como miniatura."""
    s = open(ruta, encoding="utf-8").read()
    ini = s.index(">", s.index("<svg")) + 1
    cuerpo = s[ini:s.rindex("</svg>")]
    h = w * H_PAGE / W
    return (rect(x - 3, y - 3, w + 6, h + 6, "#C9CED6", r=4)
            + f'<svg x="{x}" y="{y}" width="{w}" height="{h:.1f}" viewBox="0 0 {W} {H_PAGE}">{cuerpo}</svg>')


def resumen():
    b = pagina("#FFFFFF")
    b.append(logo(M, 46, 64))
    b.append(TX(M + 210, 92, "Tres direcciones para el entorno del cuaderno", 44, EDU_AZUL, weight="700"))
    b.append(TX(M + 210, 132, "Mismo contenido, mismo instrumento, mismo salvavidas. Cambia la cabecera, el marco, "
                "los rótulos, los títulos y los adornos.", 22, GRAY, style="italic"))
    y = 200
    for k in "ABC":
        f = FICHAS[k]
        b.append(rect(M, y, CW, 740, "#F6F7FA", r=24))
        b.append(rect(M, y, 10, 740, EDU_AZUL, r=5))
        b.append(TX(M + 50, y + 92, k, 72, EDU_AZUL, f["fam"], f["peso"]))
        b.append(TX(M + 130, y + 88, f["nombre"], fit(f["nombre"], 64, f["fam"], f["peso"], 560),
                    TINTA_C, f["fam"], f["peso"]))
        b.append(TX(M + 50, y + 140, f["tipo"], 24, GRAY, style="italic"))
        b.append(TX(M + 50, y + 210, "Cómo se siente", 18, EDU_AZUL, weight="700", ls=1.5))
        b.append(TX(M + 50, y + 246, f["palabras"], 25, INK))
        b.append(TX(M + 50, y + 316, "Acentos que se suman", 18, EDU_AZUL, weight="700", ls=1.5))
        for i, (hx, nm) in enumerate(f["acentos"]):
            cx = M + 82 + i * 112
            b.append(f'<circle cx="{cx}" cy="{y + 370}" r="32" fill="{hx}" stroke="#C9CED6" stroke-width="2"/>')
            b.append(TX(cx, y + 428, nm, 16, GRAY, anchor="middle"))
            b.append(TX(cx, y + 450, hx.upper(), 14, GRAY, anchor="middle"))
        b.append(TX(M + 50, y + 512, "Títulos", 18, EDU_AZUL, weight="700", ls=1.5))
        b.append(TX(M + 50, y + 590, "Aa · Pregunta 7", 60, TINTA_C, f["fam"], f["peso"]))
        b.append(TX(M + 50, y + 632, f["tipo_txt"], 20, INK))
        b.append(TX(M + 50, y + 662, "licencia SIL Open Font License 1.1 · texto de lectura sigue en Carlito",
                    17, GRAY, style="italic"))
        for n in (1, 2, 3):
            b.append(_anidar(OUTD + f"estilo_{k}_{n}.svg", M + 790 + (n - 1) * 350, y + 52, 322))
            b.append(TX(M + 790 + (n - 1) * 350 + 161, y + 52 + 417 + 40,
                        ("portada", "metas · página 4", "taller · Biología, página 151")[n - 1], 19, GRAY,
                        anchor="middle"))
        y += 770
    b.append(TX(M, H_PAGE - 62, "Los siete colores de área no cambian. El salvavidas conserva #FFF7F2 y #E4572E en las tres. "
                "Todo es vectorial y sin filtros; el único raster es el logo.", 20, GRAY, style="italic"))
    return b


def construir():
    rutas = []
    for k, S in ESTILOS.items():
        b = PORTADAS[k]()
        r1 = OUTD + f"estilo_{k}_1.svg"
        svg_close(b, r1)
        r2 = OUTD + f"estilo_{k}_2.svg"
        svg_close(metas(k), r2)
        random.seed(17)
        r3 = S.hoja_taller(f"estilo_{k}_3", 151, 4, bio2.Q[7], bio2.Q[8])
        rutas += [r1, r2, r3]
    b = resumen()
    r = OUTD + "estilo_resumen.svg"
    svg_close(b, r)
    rutas.append(r)
    return rutas


if __name__ == "__main__":
    import render
    rutas = construir()
    os.makedirs(PDF_DIR, exist_ok=True)
    pdf = render.unir(rutas, os.path.join(PDF_DIR, "Propuesta_estilos.pdf"))
    for r in rutas:
        print(r)
    print(pdf)
