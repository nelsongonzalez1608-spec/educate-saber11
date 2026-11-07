#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Motor de las hojas de Inglés POR PARTES DEL ICFES (formato nuevo, muestra: Misión 3).

Por qué existe: en Inglés el examen viene por partes y cada parte evalúa una cosa distinta. Nelson
decidió (7 nov) que cada misión de Inglés trabaje UNA estrategia por parte, con 4 subestrategias,
cubriendo TODOS los ítems del libro, con más vocabulario. El instrumento es por parte/subestrategia y
no por pregunta: excepción a la regla 4 solo para Inglés.

Una misión de Inglés en este formato son las mismas 7 páginas (taller, taller, ICFES, taller, taller,
taller, ICFES), pero las 5 de taller son:

    t1 · hoja_estrategia()   qué pide la parte, la estrategia con sus 4 pasos, las 4 subestrategias
                             con su mini-instrumento y un espacio resuelto pensando en voz alta
    t2 · hoja_trabajo()      uno o dos textos: «mi primera idea del texto», una fila por ítem
    t3 · hoja_trabajo()      (n.º · la pista que subrayé · subestrategia 1–4 · marco · seguridad),
    t4 · hoja_trabajo()      cierre del texto; reto en equipo; salvavidas y cierre de la misión
    t5 · hoja_diccionario()  mi diccionario de la parte

Este módulo NO modifica taller_base.py: reutiliza de allí configurar(), usar_estrategias(), la
cabecera de diario, el pie, el salvavidas y los colores. Las hojas ICFES siguen saliendo con
taller_base.hoja_icfes() desde el módulo *_icfes.py de la misión.

Todo lo que dibuja una pieza de trabajo va envuelto en <g class="instrumento" data-xmax data-ymax>
para que verifica_cajas.py revise que no se sale de su recuadro (cada pieza declara su propio borde,
no el 1370 de las tarjetas de taller).
"""
import os

from taller_base import *            # noqa: F401,F403  (lib, A, EST, cabecera, salvavidas, …)
from taller_base import _mezcla, _pie_texto
from PIL import ImageFont

LN = "#C9CED6"            # renglón para escribir a mano (se ve en papel; LGRAY es demasiado pálido)
FILA_BG = None            # fondo de las filas pares; se calcula con el color del área
_RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
_CAVEAT = os.path.join(_RAIZ, "fuentes", "Caveat-Regular.ttf")
_FM = {}


# ───────── piezas pequeñas (las mismas firmas que usaba ing3_v1: ing3_icfes las importa) ─────────
def tinte(c, k=0.9):
    return _mezcla(c, k)


def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2, c=LGRAY):
    b.append(line(x1, y, x2, y, c, 2))


def texto(b, x, y, txt, size=17, color=INK, weight="400", anchor="start", style="normal"):
    b.append(T(x, y, [txt], size, color, weight=weight, anchor=anchor, style=style))


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12, bend=0.0):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def marca(b, x, y, c, lab, size=16):
    """Casilla y su rótulo; devuelve el x donde termina."""
    b.append(checkbox(x, y, s=10, c=c))
    b.append(T(x + 28, y + 17, [lab], size, GRAY))
    return x + 28 + tw(lab, size) + 30


def frase_hueco(b, x, y, w, txt, c, h=54, size=18):
    caja(b, x, y, w, h, c)
    b.append(T(x + 22, y + h / 2 + 7, [txt], size, INK, weight="700"))
    return y + h


# ───────── letra de mano (Caveat) ─────────
def tw_mano(txt, size):
    """Ancho de un texto en Caveat, medido con la fuente real del repositorio (fuentes/)."""
    if size not in _FM:
        _FM[size] = ImageFont.truetype(_CAVEAT, int(round(size * 4)))
    return _FM[size].getlength(txt) / 4.0


def mano(b, x, y, txt, size=30, c=PENCIL, anchor="start"):
    b.append(T(x, y, [txt], size, c, font=WRITE, anchor=anchor))


def mano_lineas(txt, size, ancho):
    """Parte un texto a mano en renglones que caben en `ancho` (medido con Caveat)."""
    out, cur = [], []
    for p in txt.split(" "):
        if cur and tw_mano(" ".join(cur + [p]), size) > ancho:
            out.append(" ".join(cur))
            cur = [p]
        else:
            cur.append(p)
    if cur:
        out.append(" ".join(cur))
    return out


def envolver(b, n, frag, xmax, ymax):
    """Una pieza de trabajo, envuelta para que verifica_cajas/verifica_pistas la encuentren."""
    b.append(f'<g class="instrumento" data-n="{n}" data-ymax="{ymax:.0f}" data-xmax="{xmax:.0f}" '
             f'data-k="1.0000">' + "".join(frag) + "</g>")


# ───────── recuadros ─────────
def tarjeta_marco(b, x, y, w, h, band=88):
    """Tarjeta del cuaderno: borde del área y banda de color arriba (sin filetes horizontales)."""
    b.append(rect(x, y, w, h, "white", r=26, stroke=A["ln"], sw=2.4))
    if band:
        b.append(rect(x, y, w, band, A["bg"], r=26))
        b.append(rect(x, y + band - 30, w, 30, A["bg"], r=0))
        b.append(rect(x, y, w, h, "none", r=26, stroke=A["ln"], sw=2.4))


def banda(b, x, y, insignia, titulo, sub=None, c=None, size=26):
    """Insignia redonda + título + subtítulo en la banda de una tarjeta."""
    c = c or A["color"]
    if insignia is not None:
        s = str(insignia)
        b.append(f'<circle cx="{x + 52}" cy="{y + 44}" r="30" fill="{c}"/>')
        fs = 28 if len(s) <= 2 else 22
        b.append(T(x + 52, y + 44 + fs * 0.36, [s], fs, "white", weight="700", anchor="middle"))
        tx = x + 100
    else:
        tx = x + 34
    b.append(T(tx, y + 40, [titulo], size, c, weight="700"))
    if sub:
        b.append(T(tx, y + 70, [sub], 19, GRAY, style="italic"))
    return tx


def circulo_sub(b, cx, cy, n, r=17, size=19):
    """El circulito de color de una subestrategia, con su número."""
    c = EST[n][1]
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>')
    b.append(T(cx, cy + size * 0.36, [str(n)], size, "white", weight="700", anchor="middle"))


def casillas_sub(b, x, y, paso=66, s=13, size=18):
    """Las cuatro casillas de subestrategia, cada una con su color y su número a la derecha.
    Devuelve el x donde terminan."""
    for k, n in enumerate(sorted(EST)):
        c = EST[n][1]
        bx = x + k * paso
        b.append(rect(bx, y, s * 2, s * 2, "white", r=4, stroke=c, sw=2.6))
        b.append(T(bx + s * 2 + 8, y + s + size * 0.36, [str(n)], size, c, weight="700"))
    return x + len(EST) * paso


# ───────── hoja 1 · la parte y su estrategia ─────────
def hoja_estrategia(nombre, pag, hoja, parte, que_pide, muestra, estrategia, pasos, subs, modelo,
                    primera_idea):
    """parte: número de la parte del ICFES. que_pide: párrafo (se justifica). muestra(b, x, y, w, h):
    dibujo esquemático de cómo se ve la parte. estrategia: nombre. pasos: 4 tuplas (rótulo, texto).
    subs: {n: dict(cuando=…, pregunta=…, inst=fn(b, x, y, w, h))}. modelo: dict para modelo_voz_alta().
    primera_idea: la pregunta de «mi primera idea, antes de hacer nada»."""
    b = svg_open()
    cabecera(b, f"Prueba de Campo · hoja {hoja} de 5 · la Parte {parte} y su estrategia")
    c = A["color"]
    x, w = M, CW
    # A · qué pide la parte
    y = Y0
    hA = 372
    tarjeta_marco(b, x, y, w, hA)
    banda(b, x, y, f"P{parte}", f"Lo que pide la Parte {parte} del examen",
          "dicho de frente, antes de empezar")
    pw = 1080
    svg, yy = TJ(x + 34, y + 110, que_pide, pw, 21, INK, lh=30)
    b.append(svg)
    frag = []
    muestra(frag, x + pw + 80, y + 104, w - pw - 114, hA - 120)
    envolver(b, "muestra", frag, x + w - 20, y + hA - 10)
    iy = max(yy, y + hA - 92) + 6
    b.append(T(x + 34, iy + 4, ["Mi primera idea, antes de hacer nada:"], 19, c, weight="700"))
    b.append(T(x + 34, iy + 30, [primera_idea], 16, GRAY, style="italic"))
    renglon(b, x + 34 + tw("Mi primera idea, antes de hacer nada:", 19, "700") + 20, iy + 8,
            x + pw, LN)
    renglon(b, x + 34, iy + 66, x + pw, LN)
    # B · la estrategia y sus cuatro pasos
    y += hA + 20
    hB = 240
    tarjeta_marco(b, x, y, w, hB)
    banda(b, x, y, "E", f"La estrategia de la Parte {parte} · {estrategia}",
          "cuatro pasos, siempre en el mismo orden, para cada espacio")
    pasos_ruta(b, x + 30, y + 108, w - 60, pasos)
    # C · las cuatro subestrategias
    y += hB + 20
    hC = 440
    sw_ = (w - 24) / 2
    for k, n in enumerate(sorted(subs)):
        sx = x + (k % 2) * (sw_ + 24)
        sy = y + (k // 2) * (hC + 18)
        tarjeta_sub(b, sx, sy, sw_, hC, n, subs[n])
    y += 2 * hC + 18 + 20
    # D · un espacio resuelto pensando en voz alta
    modelo_voz_alta(b, x, y, w, H_PAGE - 140 - y, **modelo)
    footer(b, pag, c, texto=_pie_texto("Prueba de Campo"))
    ruta = OUT + nombre + ".svg"
    svg_close(b, ruta)
    return ruta


def pasos_ruta(b, x, y, w, pasos):
    """Los cuatro pasos de la estrategia en fila, unidos por flechas a mano."""
    c = A["color"]
    n = len(pasos)
    gap = 56
    pw = (w - gap * (n - 1)) / n
    for k, (rot_, txt) in enumerate(pasos):
        px = x + k * (pw + gap)
        b.append(rect(px, y, pw, 118, tinte(c, 0.95), r=16, stroke=A["ln"], sw=2))
        b.append(rect(px, y, 8, 118, c, r=4))
        rot(b, px + 26, y + 30, rot_, c, size=15)
        svg, _ = TJ(px + 26, y + 42, txt, pw - 50, 18, INK, lh=25)
        b.append(svg)
        if k < n - 1:
            flecha(b, px + pw + 8, y + 59, px + pw + gap - 8, y + 59, c, sw=3.2, head=12)


def tarjeta_sub(b, x, y, w, h, n, d):
    """Una subestrategia: su número y color, cuándo la llamo, su mini-instrumento y su pregunta."""
    nombre, c = EST[n]
    b.append(rect(x, y, w, h, "white", r=22, stroke=tinte(c, 0.7), sw=2.4))
    b.append(rect(x, y, 10, h, c, r=5))
    circulo_sub(b, x + 54, y + 44, n, r=24, size=26)
    b.append(T(x + 92, y + 42, [f"Subestrategia {n} · {nombre}"], 25, c, weight="700"))
    b.append(T(x + 92, y + 72, [f"La llamo cuando {d['cuando']}"], 17, GRAY, style="italic"))
    frag = []
    ix, iy, iw = x + 34, y + 96, w - 62
    ih = h - 96 - 64
    d["inst"](frag, ix, iy, iw, ih)
    envolver(b, f"sub{n}", frag, x + w - 14, y + h - 58)
    b.append(T(x + 34, y + h - 24, ["La pregunta que me hago:"], 18, c, weight="700"))
    b.append(T(x + 34 + tw("La pregunta que me hago:", 18, "700") + 12, y + h - 24, [d["pregunta"]], 18,
               INK, style="italic"))


def burbuja(b, x, y, w, lineas, size, c, sub=None, rotulo=None):
    """Globo de pensamiento con letra de mano. Devuelve el y donde termina."""
    lh = size * 1.05
    h = 22 + len(lineas) * lh + 8
    b.append(rect(x, y, w, h, "white", r=22, stroke=c, sw=2.2))
    # colita del globo, a la izquierda
    b.append(f'<circle cx="{x - 12}" cy="{y + h - 10}" r="6" fill="white" stroke="{c}" stroke-width="2"/>')
    b.append(f'<circle cx="{x - 26}" cy="{y + h + 2}" r="3.5" fill="white" stroke="{c}" stroke-width="2"/>')
    tx = x + 20
    if sub:
        circulo_sub(b, x + 34, y + 30, sub, r=15, size=17)
        tx = x + 60
    for i, ln in enumerate(lineas):
        mano(b, tx, y + 14 + size * 0.8 + i * lh, ln, size)
    return y + h


def modelo_voz_alta(b, x, y, w, h, frase, opciones, pensamientos, fila, nota=None, n_izq=2):
    """Un espacio resuelto pensando en voz alta. frase: el texto con el hueco. opciones: 3 strings.
    pensamientos: lista de (rótulo del paso, n.º de subestrategia o None, texto a mano); los n_izq
    primeros van debajo de la frase y el resto en la columna derecha (se leen como un periódico).
    fila: dict(n, pista, subs, letra, seguro) para mostrar cómo queda la fila llena."""
    c = A["color"]
    tarjeta_marco(b, x, y, w, h)
    banda(b, x, y, "0", "Así se piensa un espacio, en voz alta",
          nota or "un ejemplo inventado para ver la estrategia andando; los espacios del libro los "
                  "resuelves tú")
    yy = y + 104
    fw = 780
    # la frase y sus opciones
    svg, y2 = TJ(x + 58, yy + 40, frase, fw - 48, 22, INK, lh=31)
    hf = y2 - yy + 50
    caja(b, x + 34, yy, fw, hf, c, sw=2, fill=tinte(c, 0.95), r=14)
    rot(b, x + 58, yy + 28, "EL ESPACIO", c, size=14)
    b.append(svg)
    ox = x + 58
    for k, o in enumerate(opciones):
        b.append(T(ox, y2 + 32, [f"{'ABC'[k]}. {o}"], 21, INK, weight="700"))
        ox += tw(f"{'ABC'[k]}. {o}", 21, "700") + 54
    cols = [(x + 64, fw - 30, yy + hf + 14, pensamientos[:n_izq]),
            (x + 34 + fw + 70, x + w - 34 - (x + 34 + fw + 70), yy, pensamientos[n_izq:])]
    tinta = tinte(c, 0.45)
    for bx, bw, by, lista in cols:
        for paso, sub, txt in lista:
            lineas = mano_lineas(txt, 27, bw - (84 if sub else 44))
            rot(b, bx, by + 14, paso, c, size=13)
            by = burbuja(b, bx, by + 22, bw, lineas, 27, tinta, sub) + 12
    # así queda la fila llena
    fy = y + h - 172
    b.append(T(x + 34, fy + 4, ["Así queda la fila en mi hoja de trabajo:"], 19, c, weight="700"))
    frag = []
    yb = encabezado_tabla(frag, x + 30, fy + 18, w - 60)
    fila_espacio(frag, x + 30, yb, w - 60, fila["n"], "ABC", par=False)
    lapiz_fila(frag, x + 30, yb, w - 60, **fila)
    envolver(b, "modelo", frag, x + w - 20, y + h - 8)


# ───────── hojas de trabajo: una fila por ítem ─────────
RH = 62          # alto de fila (el renglón de la pista queda con 49 px libres encima)
HH = 62          # alto del encabezado de la tabla


def _cols(x, w):
    """Columnas de la tabla de espacios, medidas desde x en un ancho w (≥ 1700)."""
    seg_w = 330
    mar_w = 210
    sub_w = 4 * 66 + 20
    return dict(num=x + 44, pista0=x + 92, pista1=x + w - seg_w - mar_w - sub_w - 40,
                sub=x + w - seg_w - mar_w - sub_w + 6, marco=x + w - seg_w - mar_w + 30,
                seg=x + w - seg_w + 20, fin=x + w)


def encabezado_tabla(b, x, y, w):
    c = A["color"]
    k = _cols(x, w)
    b.append(rect(x, y, w, HH, tinte(c, 0.88), r=12))
    rot(b, k["num"], y + 26, "N.º", c, size=14, anchor="middle")
    rot(b, k["pista0"], y + 26, "LA PISTA QUE SUBRAYÉ · EN INGLÉS", c, size=14)
    pista(b, k["pista0"], y + 50, "las palabras vecinas del hueco que me dieron la respuesta", size=15)
    rot(b, k["sub"], y + 26, "SUBESTRATEGIA", c, size=14)
    pista(b, k["sub"], y + 50, "marco la que llamé", size=15)
    rot(b, k["marco"], y + 26, "MARCO", c, size=14)
    rot(b, k["seg"], y + 26, "¿QUÉ TAN SEGURO ESTOY?", c, size=14)
    for i, lab in enumerate(("adiviné", "casi", "seguro")):
        pista(b, k["seg"] + 22 + i * 106, y + 50, lab, size=15, anchor="middle")
    return y + HH


def fila_espacio(b, x, y, w, n, letras, par):
    c = A["color"]
    k = _cols(x, w)
    if par:
        b.append(rect(x, y, w, RH, tinte(c, 0.965), r=10))
    b.append(f'<circle cx="{k["num"]}" cy="{y + RH / 2}" r="21" fill="white" stroke="{c}" '
             f'stroke-width="2.4"/>')
    b.append(T(k["num"], y + RH / 2 + 7, [str(n)], 20, c, weight="700", anchor="middle"))
    renglon(b, k["pista0"], y + RH - 13, k["pista1"], LN)
    casillas_sub(b, k["sub"], y + RH / 2 - 13)
    for i, L in enumerate(letras):
        cx = k["marco"] + 20 + i * 60
        b.append(f'<circle cx="{cx}" cy="{y + RH / 2}" r="20" fill="white" stroke="{c}" '
                 f'stroke-width="2.4"/>')
        b.append(T(cx, y + RH / 2 + 7, [L], 20, c, weight="700", anchor="middle"))
    for i in range(3):
        b.append(checkbox(k["seg"] + 10 + i * 106, y + RH / 2 - 12, s=12, c=GRAY))
    return y + RH


def lapiz_fila(b, x, y, w, n, pista, subs, letra, seguro, letras="ABC"):
    """Las marcas a lápiz de una fila llena (solo en el modelo)."""
    k = _cols(x, w)
    mano(b, k["pista0"] + 6, y + RH - 20, pista, 30)
    for s in subs:
        bx = k["sub"] + (s - 1) * 66
        b.append(pcheck(bx + 3, y + RH / 2 - 6, 20))
    i = letras.index(letra)
    b.append(ring(k["marco"] + 20 + i * 60, y + RH / 2, r=25))
    b.append(pcheck(k["seg"] + 12 + seguro * 106, y + RH / 2 - 6, 20))


def nota_correccion(b, x, y, w, txt, rotulo="CORRECCIÓN EDUCATE"):
    """Nota corta bajo la fila de un espacio con error en el libro. Devuelve dónde termina."""
    lw = tw(rotulo + " ·", 14, "700") + 1.5 * len(rotulo + " ·") + 14
    x0 = x + 92
    svg, yy = TJ(x0 + 24 + lw, y + 10, txt, w - (x0 - x) - 48 - lw, 17, INK, lh=24)
    h = yy - y + 12
    b.append(rect(x0, y + 2, w - (x0 - x), h - 4, AMBER_BG, r=10))
    b.append(rect(x0, y + 2, 6, h - 4, EDU_ORO, r=3))
    rot(b, x0 + 22, y + 10 + 17 * 0.98, rotulo + " ·", AMBER_D, size=14)
    b.append(svg)
    return y + h + 6


def bloque_texto(b, y, t, ymax=None):
    """Un texto del libro: banda, «mi primera idea del texto», una fila por espacio, cierre.
    t = dict(n, titulo, pag, desde, hasta, letras='ABC', correcciones={n: txt}, antes={n: txt})."""
    c = A["color"]
    x, w = M, CW
    letras = t.get("letras", "ABC")
    corr, antes = t.get("correcciones", {}), t.get("antes", {})
    esp = list(range(t["desde"], t["hasta"] + 1))
    # el alto se calcula desde donde termina de verdad el contenido: se dibuja y luego el marco
    cuerpo = []
    ix, iw = x + 30, w - 60
    yy = y + 100 + 40
    rot(cuerpo, ix + 4, yy - 2, "MI PRIMERA IDEA DEL TEXTO", c, size=15)
    x0 = ix + 4 + tw("MI PRIMERA IDEA DEL TEXTO", 15, "700") + 25 * 1.5 + 30
    lab = "De qué trata, en una frase:"
    cuerpo.append(T(x0, yy, [lab], 19, INK))
    renglon(cuerpo, x0 + 10 + tw(lab, 19), yy + 4, ix + iw - 10, LN)
    yy += 54
    lab = "Va en:"
    cuerpo.append(T(x0, yy, [lab], 19, INK))
    xx = x0 + 10 + tw(lab, 19) + 10
    for o in ("pasado", "presente", "se mezclan"):
        cuerpo.append(checkbox(xx, yy - 19, s=12, c=c))
        cuerpo.append(T(xx + 34, yy, [o], 19, INK))
        xx += 34 + tw(o, 19) + 36
    lab = "La pista que me lo dijo:"
    cuerpo.append(T(xx + 30, yy, [lab], 19, INK))
    renglon(cuerpo, xx + 40 + tw(lab, 19), yy + 4, ix + iw - 10, LN)
    yy += 26
    tabla = []
    yy = encabezado_tabla(tabla, ix, yy, iw)
    for i, n in enumerate(esp):
        if n in antes:
            yy = nota_correccion(tabla, ix, yy + 4, iw, antes[n])
        yy = fila_espacio(tabla, ix, yy, iw, n, letras, par=(i % 2 == 1))
        if n in corr:
            yy = nota_correccion(tabla, ix, yy + 2, iw, corr[n])
    yy += 20
    # cierre del texto
    rot(tabla, ix + 4, yy + 18, "CIERRE DEL TEXTO", c, size=15)
    x0 = ix + 4 + tw("CIERRE DEL TEXTO", 15, "700") + 16 * 1.5 + 30
    lab = f"Marqué «seguro» en ____ de {len(esp)} espacios."
    tabla.append(T(x0, yy + 18, [lab], 19, INK))
    x2 = x0 + tw(lab, 19) + 60
    lab2 = "La subestrategia que más llamé:"
    tabla.append(T(x2, yy + 18, [lab2], 19, INK))
    xf = casillas_sub(tabla, x2 + tw(lab2, 19) + 22, yy - 3)
    pista(tabla, ix + iw - 10, yy + 18, f"las palabras que me frenaron → mi diccionario, página "
                                        f"{t.get('pag_dicc', '')}", size=16, anchor="end")
    yy += 64
    lab3 = "Lo que me llevo de este texto:"
    tabla.append(T(ix + 4, yy, [lab3], 19, c, weight="700"))
    renglon(tabla, ix + 14 + tw(lab3, 19, "700"), yy + 4, ix + iw - 10, LN)
    yy += 26
    h = yy - y
    tarjeta_marco(b, x, y, w, h)
    banda(b, x, y, t["n"], f"Texto {t['n']} · {t['titulo']}",
          f"espacios {t['desde']} a {t['hasta']} · lo lees en tu libro, página {t['pag']} · "
          f"{len(letras)} opciones por espacio: {', '.join(letras[:-1])} o {letras[-1]}")
    pista(b, x + w - 34, y + 54, "léelo entero, sin llenar nada, antes de la primera fila", size=17,
          anchor="end")
    b.extend(cuerpo)
    envolver(b, f"texto{t['n']}", tabla, x + w - 20, ymax or (y + h))
    return y + h


def hoja_trabajo(nombre, pag, hoja, textos, extra=None):
    """Hoja de trabajo: uno o dos textos y, si cabe, una pieza extra (reto, cierre de la misión).
    extra(b, y, alto_disponible)."""
    b = svg_open()
    ns = " y ".join(str(t["n"]) for t in textos)
    a, z = textos[0]["desde"], textos[-1]["hasta"]
    cabecera(b, f"Prueba de Campo · hoja {hoja} de 5 · texto{'s' if len(textos) > 1 else ''} {ns} · "
                f"espacios {a} a {z}")
    y = Y0
    for t in textos:
        y = bloque_texto(b, y, t) + 22
    if extra:
        extra(b, y, H_PAGE - 140 - y)
    footer(b, pag, A["color"], texto=_pie_texto("Prueba de Campo"))
    ruta = OUT + nombre + ".svg"
    svg_close(b, ruta)
    return ruta


# ───────── reto en equipo ─────────
def reto_equipo(b, y, h, titulo, minutos, consigna, reglas, filas, total):
    """Reto en equipo: comparar fila por fila y defender con la pista. Registro individual."""
    c = A["color"]
    x, w = M, CW
    tarjeta_marco(b, x, y, w, h)
    tx = banda(b, x, y, "R", f"Reto en equipo · {titulo}", f"{minutos} minutos · en parejas · cada uno "
                                                           f"llena su propio registro")
    chip(b, x + w - 40 - tw("se trabaja con un compañero", 18, "700") - 36, y + 24,
         "se trabaja con un compañero", c, size=18, h=40)
    svg, yy = TJ(x + 34, y + 104, consigna, w - 68, 21, INK, lh=30)
    b.append(svg)
    yy += 12
    rw = (w - 68 - 2 * 20) / 3
    alto = 0
    piezas = []
    for k, r_ in enumerate(reglas):
        rx = x + 34 + k * (rw + 20)
        s, y2 = TJ(rx + 64, yy + 18, r_, rw - 84, 18, INK, lh=25)
        piezas.append((rx, s))
        alto = max(alto, y2 - yy + 18)
    for k, (rx, s) in enumerate(piezas):
        b.append(rect(rx, yy, rw, alto, tinte(c, 0.95), r=14))
        b.append(f'<circle cx="{rx + 34}" cy="{yy + 34}" r="18" fill="{c}"/>')
        b.append(T(rx + 34, yy + 41, [str(k + 1)], 19, "white", weight="700", anchor="middle"))
        b.append(s)
    yy += alto + 22
    # tabla de desacuerdos
    frag = []
    ix, iw = x + 34, w - 68
    cols = [("ESPACIO", 150), ("YO MARQUÉ", 190), ("MI COMPAÑERO(A) MARCÓ", 290),
            ("LA PISTA QUE GANÓ · EN INGLÉS", iw - 150 - 190 - 290 - 420), ("¿QUIÉN CAMBIÓ?", 420)]
    frag.append(rect(ix, yy, iw, 50, tinte(c, 0.88), r=12))
    cx = ix
    for lab_, cw_ in cols:
        rot(frag, cx + 18, yy + 31, lab_, c, size=14)
        cx += cw_
    yy += 50
    disp = y + h - 84 - yy
    filas = max(3, min(filas, int(disp // 62)))
    fila_h = min(74, disp / filas)          # las filas se estiran para llenar la tarjeta
    for i in range(filas):
        if i % 2:
            frag.append(rect(ix, yy, iw, fila_h, tinte(c, 0.965), r=10))
        cx = ix
        for j, (lab_, cw_) in enumerate(cols):
            if j == 0:
                frag.append(T(cx + 18, yy + 42, ["n.º"], 17, GRAY, style="italic"))
                renglon(frag, cx + 52, yy + fila_h - 14, cx + cw_ - 24, LN)
            elif j in (1, 2):
                for q, L in enumerate("ABC"):
                    ccx = cx + 34 + q * 52
                    frag.append(f'<circle cx="{ccx}" cy="{yy + fila_h / 2}" r="18" fill="white" '
                                f'stroke="{c}" stroke-width="2.2"/>')
                    frag.append(T(ccx, yy + fila_h / 2 + 7, [L], 18, c, weight="700", anchor="middle"))
            elif j == 3:
                renglon(frag, cx + 18, yy + fila_h - 14, cx + cw_ - 24, LN)
            else:
                xx = cx + 18
                for o in ("yo", "mi compañero(a)", "nadie"):
                    frag.append(checkbox(xx, yy + fila_h / 2 - 11, s=11, c=GRAY))
                    frag.append(T(xx + 30, yy + fila_h / 2 + 7, [o], 17, INK))
                    xx += 30 + tw(o, 17) + 30
            cx += cw_
        yy += fila_h
    envolver(b, "reto", frag, x + w - 20, y + h - 70)
    yy = y + h - 64
    lab1 = "Mi compañero(a):"
    b.append(T(x + 34, yy + 22, [lab1], 19, INK))
    renglon(b, x + 44 + tw(lab1, 19), yy + 26, x + 600, LN)
    b.append(T(x + 650, yy + 22, [f"Coincidimos en ____ de {total} espacios."], 19, INK))
    b.append(T(x + w - 34, yy + 22, ["Mis duelos: gané ____ · perdí ____ · fueron al profe ____"], 19, c,
               weight="700", anchor="end"))
    return yy + 40


# ───────── cierre de la misión: salvavidas, mapa de errores, lo que me llevo ─────────
def cierre_mision(b, y, h, parte, textos):
    """Cierre de la parte: salvavidas del espacio que más costó, mapa de errores por subestrategia,
    termómetro de seguridad (seguro vs. acerté) y lo que me llevo. textos: [(n, cuántos espacios)]."""
    c = A["color"]
    x, w = M, CW
    tarjeta_marco(b, x, y, w, h)
    banda(b, x, y, f"P{parte}", f"Cierre de la Parte {parte}",
          "lo lleno al final del sábado, después de corregir con el profe")
    lw = 860
    yy = y + 110
    lab = "El espacio que más me costó fue el n.º"
    b.append(T(x + 34, yy + 20, [lab], 20, INK, weight="700"))
    renglon(b, x + 44 + tw(lab, 20, "700"), yy + 24, x + 34 + lw, LN)
    salvavidas(b, x + 34, yy + 46, lw, h=300)
    # mapa de errores
    rx = x + 34 + lw + 50
    rw = x + w - 34 - rx
    rot(b, rx, yy + 20, "MI MAPA DE ERRORES", c, size=15)
    pista(b, rx + tw("MI MAPA DE ERRORES", 15, "700") + 18 * 1.5 + 20, yy + 20,
          "con las claves del profe, cuento cuántos fallé con cada una", size=16)
    my = yy + 46
    for k, n in enumerate(sorted(EST)):
        nombre, ec = EST[n]
        ry = my + k * 62
        b.append(rect(rx, ry, rw, 52, tinte(ec, 0.93), r=12))
        circulo_sub(b, rx + 30, ry + 26, n, r=16, size=18)
        b.append(T(rx + 60, ry + 33, [nombre], 19, ec, weight="700"))
        b.append(T(rx + rw - 20, ry + 33, ["fallé ____"], 19, INK, anchor="end"))
    yy2 = my + 4 * 62 + 14
    b.append(T(rx, yy2 + 20, ["La que más tengo que practicar:"], 19, INK))
    casillas_sub(b, rx + tw("La que más tengo que practicar:", 19) + 20, yy2)
    # termómetro de seguridad
    ty = yy + 46 + 300 + 50
    rot(b, x + 34, ty, "MI TERMÓMETRO DE SEGURIDAD", c, size=15)
    svg, ty2 = TJ(x + 34, ty + 10, "Pinto una casilla por cada «seguro» que marqué. Cuando el profe dé las "
                  "claves, le pongo un punto a las que de verdad acerté.", lw, 17, GRAY, style="italic", lh=24)
    b.append(svg)
    frag = []
    ry = ty2 + 8
    for n, cuantos in textos:
        frag.append(T(x + 34, ry + 27, [f"Texto {n}"], 19, c, weight="700"))
        for q in range(cuantos):
            frag.append(rect(x + 150 + q * 56, ry, 46, 38, "white", r=8, stroke=tinte(c, 0.5), sw=2))
        ry += 50
    envolver(b, "termometro", frag, x + 34 + lw, y + h - 20)
    # lo que me llevo
    b.append(T(rx, ty, [f"Lo que me llevo de la Parte {parte}"], 22, c, weight="700"))
    b.append(T(rx, ty + 28, ["(una frase que me sirva el día del examen)"], 17, GRAY, style="italic"))
    ly = ty + 28
    for i in range(3):
        ly += 54
        renglon(b, rx, ly, x + w - 34, LN)
    fin = max(ry, ly) + 30
    if y + h - fin >= 110:
        lab = "Una pregunta que me quedó para el profe:"
        b.append(T(x + 34, fin + 24, [lab], 20, c, weight="700"))
        renglon(b, x + 44 + tw(lab, 20, "700"), fin + 28, x + w - 34, LN)
        k = fin + 28
        while k + 54 <= y + h - 30:
            k += 54
            renglon(b, x + 34, k, x + w - 34, LN)
    return y + h


# ───────── hoja 5 · mi diccionario ─────────
def hoja_diccionario(nombre, pag, hoja, parte, secciones, intro):
    """secciones: lista de funciones f(b, y) → y_final, en orden."""
    b = svg_open()
    cabecera(b, f"Prueba de Campo · hoja {hoja} de 5 · mi diccionario de la Parte {parte}")
    c = A["color"]
    y = Y0
    b.append(T(M, y + 44, [f"Mi diccionario de la Parte {parte}"], 40, c, weight="700"))
    svg, yy = TJ(M, y + 62, intro, CW, 21, GRAY, style="italic", lh=30)
    b.append(svg)
    y = yy + 18
    for f in secciones:
        y = f(b, y) + 22
    footer(b, pag, c, texto=_pie_texto("Prueba de Campo"))
    ruta = OUT + nombre + ".svg"
    svg_close(b, ruta)
    return ruta


def dicc_palabras(filas, rh=70):
    """Palabras que me frenaron: la palabra, dónde, la pista del contexto, lo que creo, una frase mía."""
    def _f(b, y):
        c = A["color"]
        x, w = M, CW
        cols = [("LA PALABRA", 280), ("TEXTO · ESPACIO", 170), ("LA PISTA DEL CONTEXTO", 420),
                ("LO QUE CREO QUE SIGNIFICA", 340), ("UNA FRASE MÍA, EN INGLÉS", w - 280 - 170 - 420 - 340 - 130),
                ("EN CLASE", 130)]
        h = 96 + 54 + filas * rh + 14
        tarjeta_marco(b, x, y, w, h)
        banda(b, x, y, None, "Palabras que me frenaron",
              "primero la adivino por el contexto; en clase la confirmo y marco la casilla")
        frag = []
        ix, iw = x + 20, w - 40
        yy = y + 96
        frag.append(rect(ix, yy, iw, 54, tinte(c, 0.88), r=12))
        cx = ix
        for lab, cw_ in cols:
            rot(frag, cx + 16, yy + 34, lab, c, size=14)
            cx += cw_
        yy += 54
        for i in range(filas):
            if i % 2:
                frag.append(rect(ix, yy, iw, rh, tinte(c, 0.965), r=10))
            cx = ix
            for j, (lab, cw_) in enumerate(cols):
                if j == len(cols) - 1:
                    frag.append(checkbox(cx + cw_ / 2 - 26, yy + rh / 2 - 12, s=12, c=GRAY))
                    frag.append(T(cx + cw_ / 2 + 4, yy + rh / 2 + 7, ["sí"], 17, GRAY))
                else:
                    renglon(frag, cx + 16, yy + rh - 14, cx + cw_ - 16, LN)
                cx += cw_
            yy += rh
        cx = ix
        for lab, cw_ in cols[:-1]:
            cx += cw_
            frag.append(line(cx, y + 96 + 54 + 8, cx, yy - 8, tinte(c, 0.75), 1.6))
        envolver(b, "dicc-palabras", frag, x + w - 10, y + h)
        return y + h
    return _f


def iman(b, x, y, c, h=40):
    """Imán de herradura acostado (⊏), con sus polos en gris: une la palabra con su pegada."""
    b.append(f'<polyline points="{x + 34},{y + 7} {x + 8},{y + 7} {x + 8},{y + h - 7} {x + 34},{y + h - 7}" '
             f'fill="none" stroke="{c}" stroke-width="11" stroke-linejoin="round"/>')
    b.append(rect(x + 30, y + 1, 12, 12, "#9AA1AC", r=2))
    b.append(rect(x + 30, y + h - 13, 12, 12, "#9AA1AC", r=2))


def dicc_parejas(titulo, consigna, n, sub, por_fila=3, rh=78):
    """Banco por llenar de palabras que van pegadas: [palabra] imán [pegada] = en español."""
    def _f(b, y):
        nombre, c = EST[sub]
        x, w = M, CW
        filas = (n + por_fila - 1) // por_fila
        svg, yy = TJ(x + 34, y + 100, consigna, w - 68, 19, INK, lh=27)
        y0 = yy + 14
        h = y0 - y + filas * rh + 10
        tarjeta_marco(b, x, y, w, h)
        banda(b, x, y, sub, titulo, f"subestrategia {sub} · {nombre}", c=c)
        b.append(svg)
        frag = []
        cw_ = (w - 68 - (por_fila - 1) * 30) / por_fila
        for k in range(n):
            px = x + 34 + (k % por_fila) * (cw_ + 30)
            py = y0 + (k // por_fila) * rh
            frag.append(rect(px, py, 190, 56, "white", r=10, stroke=c, sw=2.2))
            iman(frag, px + 196, py + 8, c)
            frag.append(rect(px + 246, py, 104, 56, tinte(c, 0.9), r=10, stroke=c, sw=2.2))
            frag.append(T(px + 366, py + 37, ["="], 22, c, weight="700"))
            renglon(frag, px + 392, py + 44, px + cw_ - 6, LN)
        envolver(b, "dicc-parejas", frag, x + w - 20, y + h)
        return y + h
    return _f


def _icono_relacion(b, cx, cy, tipo, c):
    """Dibujo de la relación: suma (+), oposición (→ ←), causa (← porque), resultado (→ entonces)."""
    if tipo == "suma":
        b.append(line(cx - 14, cy, cx + 14, cy, c, 5))
        b.append(line(cx, cy - 14, cx, cy + 14, c, 5))
    elif tipo == "contraste":
        b.append(hand_arrow(cx - 30, cy, cx - 5, cy, c, sw=3.4, bend=0, head=10))
        b.append(hand_arrow(cx + 30, cy, cx + 5, cy, c, sw=3.4, bend=0, head=10))
    elif tipo == "causa":
        b.append(hand_arrow(cx + 26, cy, cx - 26, cy, c, sw=3.4, bend=0, head=11))
    else:
        b.append(hand_arrow(cx - 26, cy, cx + 26, cy, c, sw=3.4, bend=0, head=11))


def dicc_familias(titulo, consigna, familias, sub, lineas=4, lh=54):
    """Banco por llenar de conectores por la relación que dicen. familias: [(tipo, nombre, pista)].
    Junto a cada conector, dos casillas: lo que sigue es oración (O) o solo un sustantivo (S)."""
    def _f(b, y):
        nombre, c = EST[sub]
        x, w = M, CW
        svg, yy = TJ(x + 34, y + 100, consigna, w - 68, 19, INK, lh=27)
        y0 = yy + 14
        h = y0 - y + 70 + lineas * lh + 16
        tarjeta_marco(b, x, y, w, h)
        banda(b, x, y, sub, titulo, f"subestrategia {sub} · {nombre}", c=c)
        b.append(svg)
        frag = []
        nf = len(familias)
        cw_ = (w - 68 - (nf - 1) * 24) / nf
        for k, (tipo, nom, ps) in enumerate(familias):
            px = x + 34 + k * (cw_ + 24)
            frag.append(rect(px, y0, cw_, 62, tinte(c, 0.9), r=12))
            _icono_relacion(frag, px + 46, y0 + 31, tipo, c)
            frag.append(T(px + 92, y0 + 27, [nom], 19, c, weight="700"))
            frag.append(T(px + 92, y0 + 50, [ps], 15, GRAY, style="italic"))
            for i in range(lineas):
                ly = y0 + 70 + (i + 1) * lh - 10
                renglon(frag, px + 10, ly, px + cw_ - 104, LN)
                for q, L in enumerate("OS"):
                    bx = px + cw_ - 92 + q * 46
                    frag.append(checkbox(bx, ly - 24, s=11, c=GRAY))
                    frag.append(T(bx + 27, ly - 6, [L], 15, GRAY, weight="700"))
        envolver(b, "dicc-familias", frag, x + w - 20, y + h)
        return y + h
    return _f


def dicc_verbos(titulo, consigna, cols, filas, sub, tablas=2, rh=58):
    """Tabla por llenar de las caras del verbo (las que me frenaron en los textos)."""
    def _f(b, y):
        nombre, c = EST[sub]
        x, w = M, CW
        svg, yy = TJ(x + 34, y + 100, consigna, w - 68, 19, INK, lh=27)
        y0 = yy + 14
        h = y0 - y + 48 + filas * rh + 16
        tarjeta_marco(b, x, y, w, h)
        banda(b, x, y, sub, titulo, f"subestrategia {sub} · {nombre}", c=c)
        b.append(svg)
        frag = []
        tw_ = (w - 68 - (tablas - 1) * 40) / tablas
        for t in range(tablas):
            tx = x + 34 + t * (tw_ + 40)
            frag.append(rect(tx, y0, tw_, 48, tinte(c, 0.88), r=10))
            cw_ = tw_ / len(cols)
            for j, lab in enumerate(cols):
                rot(frag, tx + j * cw_ + 14, y0 + 31, lab, c, size=14)
                if j:
                    frag.append(line(tx + j * cw_, y0 + 56, tx + j * cw_, y0 + 48 + filas * rh - 6,
                                     tinte(c, 0.75), 1.6))
            for i in range(filas):
                ry = y0 + 48 + i * rh
                if i % 2:
                    frag.append(rect(tx, ry, tw_, rh, tinte(c, 0.965), r=8))
                for j in range(len(cols)):
                    renglon(frag, tx + j * cw_ + 14, ry + rh - 12, tx + (j + 1) * cw_ - 14, LN)
        envolver(b, "dicc-verbos", frag, x + w - 20, y + h)
        return y + h
    return _f
