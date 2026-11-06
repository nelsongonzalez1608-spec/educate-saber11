#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Motor de las hojas del cuaderno: taller (2 preguntas del libro) y entrenamiento ICFES.

Reconstruido el 6 nov 2026 contra las 110 páginas de `referencia/hojas/` (geometría medida
sobre m1_t1, m2_t1, soc2_t3 y soc2_i1) y el contrato de CLAUDE.md § 5. El original se perdió
con el espacio de Cowork.

Cómo se usa desde un módulo de misión (p. ej. `soc3.py`):

    from taller_base import *
    configurar("Sociales y Ciudadanas", 3, "competencias ciudadanas",
               tema="Lo que dice la norma y lo que pasa", nota="LO QUE ANOTÉ DEL CASO")
    EST = {1: ("Nombre de la estrategia", EDU_AZUL), 2: (…, EDU_VERDE), …}
    usar_estrategias(EST)

    def i1(b, x, y, w, h):          # un instrumento: dibuja en b y devuelve dónde terminó
        yy = titulo_instr(b, x, y, "Título que no se repite", EST[1][1], "subtítulo…")
        …
        return yy

    Q = {1: dict(n=1, est=1, pag=346, ctx="Contexto · lo que pregunta", inst=i1), …}

    def build(pages=(111, 112, 114, 115, 116)):
        hoja_taller("soc3_t1", pages[0], 1, Q[1], Q[2])
        …

Reglas que el motor hace cumplir solo:
  · cada tarjeta mide su instrumento; si se pasa de alto lo encaja (`encajar`) — el ANCHO
    no lo arregla: borde derecho máximo M + 30 + IW = 1370, lo revisa verifica_cajas.py;
  · la segunda tarjeta se ubica con y_bloque2(), que lee BLK_H en el momento (no congelado);
  · cada instrumento queda envuelto en <g class="instrumento" …> para que los verificadores
    lo encuentren; cada chip, en <g class="chip">;
  · el pie del cuaderno dice «Aprende · Practica · Avanza» (lo busca render.verifica).
"""
import math
import os
import re
import xml.etree.ElementTree as ET

from lib import *   # noqa: F401,F403  (W, H_PAGE, M, CW, T, rect, line, tw, TJ, chip, …)
import lib as _lib

OUT = os.path.dirname(os.path.realpath(__file__)) + "/"

# ───────── geometría (medida sobre las hojas de referencia) ─────────
IW = 1270                      # ancho del instrumento
RX_OFF = IW + 40               # inicio de la columna derecha, desde M
X_MAX = M + 30 + IW            # 1370: borde derecho máximo de cualquier instrumento
Y0 = 210                       # arriba de la primera tarjeta
GAP = 40                       # entre tarjetas
BLK_CON_VOCAB, BLK_SIN_VOCAB = 1010, 1090
BLK_H = BLK_SIN_VOCAB
VOCAB_Y, VOCAB_H = 2290, 160
NOTA_MIN = 150                 # alto mínimo para que valga la pena el recuadro de notas

# ───────── configuración de la misión ─────────
A = dict(area="", mision=0, componente="", tema="", color=EDU_ROJO,
         nota="LO QUE SUBRAYÉ EN EL TEXTO")
EST = {}


def _mezcla(c, k, con="#FFFFFF"):
    """k = 0 → c; k = 1 → con."""
    a = [int(c[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(con[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * k):02X}" for x, y in zip(a, b))


def configurar(area, mision, componente, tema="", color=None, nota=None):
    """Color: el de las hojas de referencia de esa área. Las misiones de Matemáticas y de
    Lectura Crítica se imprimieron en el rojo #A82424; Sociales en el oro #C9821B. Para un área
    nueva, si no se pasa color, se toma el de lib.AREAS."""
    if color is None:
        color = dict(_lib.AREAS).get(area, EDU_ROJO)
    A.update(area=area, mision=mision, componente=componente, tema=tema, color=color)
    if nota:
        A["nota"] = nota
    A["bg"] = _mezcla(color, 0.93)        # banda de cabecera y de tarjeta  (#FBF1F0 en rojo)
    A["ln"] = _mezcla(color, 0.80)        # borde de tarjeta
    A["dark"] = _mezcla(color, 0.33, "#000000")   # salvavidas (#6F1716 en rojo)
    A["soft"] = _mezcla(color, 0.62)      # texto sobre el salvavidas
    return A


def usar_estrategias(est):
    EST.clear()
    EST.update(est)


def set_bloque(con_vocab):
    global BLK_H
    BLK_H = BLK_CON_VOCAB if con_vocab else BLK_SIN_VOCAB
    return BLK_H


def y_bloque2():
    """Arriba de la segunda tarjeta. Lee BLK_H ahora: los módulos que hacen
    `from taller_base import *` tienen una copia congelada de BLK_H y no deben usarla."""
    return Y0 + BLK_H + GAP


# ───────── medir lo que dibuja un instrumento ─────────
_NUM = re.compile(r"-?\d+(?:\.\d+)?(?:e-?\d+)?")
_SVGNS = "{http://www.w3.org/2000/svg}"


def _f(v, d=0.0):
    try:
        return float(v)
    except (TypeError, ValueError):
        return d


def _transform(s):
    """Devuelve (k, dx, dy) de translate(...) scale(...). La rotación se ignora."""
    k, dx, dy = 1.0, 0.0, 0.0
    if not s:
        return k, dx, dy
    for nombre, args in re.findall(r"(translate|scale)\(([^)]*)\)", s):
        n = [float(v) for v in _NUM.findall(args)]
        if nombre == "translate":
            dx += k * n[0]
            dy += k * (n[1] if len(n) > 1 else 0)
        else:
            k *= n[0]
    return k, dx, dy


def _texto_cajas(el, k, dx, dy):
    size = _f(el.get("font-size"), 20)
    weight = el.get("font-weight", "400")
    weight = "700" if weight in ("700", "bold") else "400"
    style = "italic" if el.get("font-style") == "italic" else "normal"
    anchor = el.get("text-anchor", "start")
    ls = _f(el.get("letter-spacing"))
    x0, y = _f(el.get("x")), _f(el.get("y"))
    partes = [(el.text or "", x0, y)] if (el.text or "").strip() else []
    for t in el:
        if t.tag.replace(_SVGNS, "") != "tspan":
            continue
        y += _f(t.get("dy"))
        partes.append((t.text or "", _f(t.get("x"), x0), y))
    out = []
    for txt, x, yy in partes:
        if not txt.strip():
            continue
        w = tw(txt, size, weight, style) + ls * len(txt)
        xa = x - w if anchor == "end" else x - w / 2 if anchor == "middle" else x
        out.append((dx + k * xa, dy + k * (yy - size * 0.78),
                    dx + k * (xa + w), dy + k * (yy + size * 0.24)))
    return out


def _cajas(el, k=1.0, dx=0.0, dy=0.0):
    """Cajas (x0, y0, x1, y1) de todo lo que dibuja el elemento, en coordenadas de página."""
    tag = el.tag.replace(_SVGNS, "")
    if tag in ("g", "svg", "a"):
        k2, dx2, dy2 = _transform(el.get("transform"))
        k, dx, dy = k * k2, dx + k * dx2, dy + k * dy2
        out = []
        for h in el:
            out += _cajas(h, k, dx, dy)
        return out
    P = lambda x, y: (dx + k * x, dy + k * y)
    sw = _f(el.get("stroke-width")) / 2 if el.get("stroke") not in (None, "none") else 0
    if tag in ("rect", "image"):
        x, y, w, h = (_f(el.get(a)) for a in ("x", "y", "width", "height"))
        a, b = P(x - sw, y - sw), P(x + w + sw, y + h + sw)
        return [(*a, *b)]
    if tag == "line":
        x1, y1, x2, y2 = (_f(el.get(a)) for a in ("x1", "y1", "x2", "y2"))
        a, b = P(min(x1, x2) - sw, min(y1, y2) - sw), P(max(x1, x2) + sw, max(y1, y2) + sw)
        return [(*a, *b)]
    if tag in ("circle", "ellipse"):
        cx, cy = _f(el.get("cx")), _f(el.get("cy"))
        rx = _f(el.get("r")) or _f(el.get("rx"))
        ry = _f(el.get("r")) or _f(el.get("ry"))
        a, b = P(cx - rx - sw, cy - ry - sw), P(cx + rx + sw, cy + ry + sw)
        return [(*a, *b)]
    if tag in ("path", "polygon", "polyline"):
        n = [float(v) for v in _NUM.findall(el.get("d") or el.get("points") or "")]
        if re.search(r"[a-z]", (el.get("d") or "").replace("e", "")):
            return []          # trazos relativos: no se miden (el motor no los produce)
        pts = list(zip(n[0::2], n[1::2]))
        if not pts:
            return []
        xs, ys = [p[0] for p in pts], [p[1] for p in pts]
        a, b = P(min(xs) - sw, min(ys) - sw), P(max(xs) + sw, max(ys) + sw)
        return [(*a, *b)]
    if tag == "text":
        return _texto_cajas(el, k, dx, dy)
    return []


def medir(frag):
    """Caja total de una lista de fragmentos SVG (o un string). None si no dibuja nada."""
    s = frag if isinstance(frag, str) else "".join(frag)
    raiz = ET.fromstring(f'<g xmlns="http://www.w3.org/2000/svg" '
                         f'xmlns:xlink="http://www.w3.org/1999/xlink">{s}</g>')
    cs = _cajas(raiz)
    if not cs:
        return None
    return (min(c[0] for c in cs), min(c[1] for c in cs),
            max(c[2] for c in cs), max(c[3] for c in cs))


def encajar(frag, x, y, w, h_max):
    """Si lo dibujado se pasa de h_max (medido desde y), lo escala anclado arriba y centrado.
    Solo arregla el ALTO. Devuelve (fragmento, y donde termina de verdad, k)."""
    s = frag if isinstance(frag, str) else "".join(frag)
    caja = medir(s)
    if caja is None:
        return s, y, 1.0
    alto = caja[3] - y
    if alto <= h_max:
        return s, caja[3], 1.0
    k = h_max / alto
    tx = x * (1 - k) + w * (1 - k) / 2
    ty = y * (1 - k)
    return (f'<g transform="translate({tx:.1f} {ty:.1f}) scale({k:.4f})">{s}</g>',
            y + h_max, k)


# ───────── piezas de la hoja ─────────
def cabecera(b, linea3):
    """Banda del diario: logo, área · misión, tema · componente, hoja; fecha y caritas."""
    c = A["color"]
    b.append(rect(0, 0, W, 180, A["bg"], r=0))
    b.append(rect(0, 180, W, 6, c, r=0))
    b.append(logo(M, 44, 64))
    b.append(T(M + 230, 78, [f"{A['area'].upper()} · MISIÓN {A['mision']}"], 24, c,
               weight="700", ls=3))
    sub = " · ".join(s for s in (A["tema"], f"componente {A['componente']}" if A["componente"]
                                  else "") if s)
    b.append(T(M + 230, 116, [sub], 22, GRAY))
    b.append(T(M + 230, 150, [linea3], 20, GRAY, style="italic"))
    b.append(T(W - M - 640, 78, ["Sábado ____ de ____________"], 24, INK))
    b.append(T(W - M - 640, 130, ["Llego:"], 22, GRAY))
    for k, mood in enumerate(["worried", "calm", "happy"]):
        b.append(face(W - M - 540 + k * 70, 122, 24, mood, GRAY, "white", sw=2.2))
    b.append(T(W - M - 300, 130, ["Salgo:"], 22, GRAY))
    for k, mood in enumerate(["worried", "calm", "happy"]):
        b.append(face(W - M - 200 + k * 70, 122, 24, mood, GRAY, "white", sw=2.2))


def _marco_tarjeta(b, y):
    c = A["color"]
    b.append(rect(M, y, CW, BLK_H, "white", r=26, stroke=A["ln"], sw=2.4))
    b.append(rect(M, y, CW, 104, A["bg"], r=26))
    b.append(rect(M, y + 60, CW, 44, A["bg"], r=0))
    return c


def _primera_idea(b, y, x, texto):
    b.append(T(x, y + 44, [texto], 20, GRAY))
    b.append(line(x, y + 86, W - M - 30, y + 86, LGRAY, 2.2))


def columna_derecha(b, y, est, cierre=("Lo que me llevo de esta pregunta",
                                        "(una frase que me sirva en otra pregunta parecida)")):
    """MARCO AL FINAL · ¿qué tan seguro estoy? · salvavidas · lo que me llevo · sello."""
    c = A["color"]
    rx = M + RX_OFF
    rw = W - M - rx - 24
    ry = y + 130
    b.append(line(rx - 18, ry, rx - 18, y + BLK_H - 30, "#E6EAF0", 2, "6,6"))
    b.append(T(rx, ry + 20, ["MARCO AL FINAL"], 18, c, weight="700", ls=2))
    for k, L in enumerate("ABCD"):
        cx = rx + 36 + k * 92
        b.append(f'<circle cx="{cx}" cy="{ry + 80}" r="30" fill="white" stroke="{c}" '
                 f'stroke-width="2.6"/>')
        b.append(T(cx, ry + 90, [L], 26, c, weight="700", anchor="middle"))
    b.append(T(rx, ry + 144, ["¿Qué tan seguro estoy?"], 18, GRAY))
    for k, lab in enumerate(["adiviné", "casi", "seguro"]):
        b.append(checkbox(rx + k * 150, ry + 164, s=11, c=GRAY))
        b.append(T(rx + 30 + k * 150, ry + 182, [lab], 18, GRAY))
    sy = ry + 231
    salvavidas(b, rx, sy, rw)
    ly = sy + 352
    b.append(T(rx, ly, [cierre[0]], 20, c, weight="700"))
    b.append(T(rx, ly + 28, [cierre[1]], 16, GRAY, style="italic"))
    b.append(wlines(rx, sy + 438, rw, 4, c="#E3E8EF", step=48))
    ec = EST[est][1]
    b.append(f'<circle cx="{W - M - 60}" cy="{y + BLK_H - 50}" r="18" fill="{ec}"/>')
    b.append(T(W - M - 60, y + BLK_H - 43, [str(est)], 18, "white", weight="700",
               anchor="middle"))


# El salvavidas es igual en todas las áreas: fondo claro para escribir con lápiz (Nelson, 6 nov).
SALV = "#E4572E"       # coral de flotador
SALV_D = "#B23A16"     # rótulo
SALV_BG = "#FFF7F2"    # fondo claro: el lápiz se lee
SALV_TX = "#3A3F4B"    # texto de las frases guía
SALV_LN = "#C9CED6"    # renglones


def flotador(cx, cy, r=20, sw=11):
    """Aro salvavidas: anillo blanco con cuatro franjas coral y su contorno."""
    import math as _m
    C = 2 * _m.pi * r
    return (f'<circle cx="{cx}" cy="{cy}" r="{r + sw / 2}" fill="none" stroke="{SALV}" stroke-width="1.6"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r - sw / 2}" fill="none" stroke="{SALV}" stroke-width="1.6"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="white" stroke-width="{sw - 1.6}"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{SALV}" stroke-width="{sw - 1.6}" '
            f'stroke-dasharray="{C / 8:.2f} {C / 8:.2f}" transform="rotate(-22.5 {cx} {cy})"/>')


def salvavidas(b, rx, sy, rw, h=300):
    """Lo mínimo que sí tenía claro → entonces tenía que ser → y no podía ser ___ porque.
    Mismo diseño en todas las áreas; se escribe encima con lápiz."""
    b.append(rect(rx, sy, rw, h, SALV_BG, r=18, stroke=SALV, sw=2.4))
    b.append(rect(rx, sy, 8, h, SALV, r=4))
    b.append(flotador(rx + 48, sy + 38))
    b.append(T(rx + 80, sy + 46, ["SALVAVIDAS"], 18, SALV_D, weight="700", ls=2))
    b.append(T(rx + 24, sy + 92, ["Lo mínimo que sí tenía claro:"], 18, SALV_TX))
    b.append(line(rx + 24, sy + 130, rx + rw - 24, sy + 130, SALV_LN, 1.8))
    b.append(T(rx + 24, sy + 174, ["→ entonces tenía que ser"], 18, SALV_TX))
    b.append(line(rx + 24, sy + 214, rx + rw - 24, sy + 214, SALV_LN, 1.8))
    b.append(T(rx + 24, sy + 256, ["y no podía ser ____ porque"], 18, SALV_TX))
    b.append(line(rx + 260, sy + 260, rx + rw - 24, sy + 260, SALV_LN, 1.8))


def chip_estrategia(b, x, y, est, prefijo="Estrategia", derecha=False):
    nombre, ec = EST[est]
    txt = f"{prefijo} {est} · {nombre}"
    w = tw(txt, 19, "700") + 36
    x0 = x - w if derecha else x
    chip(b, x0, y, txt, ec, size=19, h=44)
    return x0, w


def notas(b, x, y, w, h, rotulo=None):
    """Recuadro «lo que subrayé en el texto» / «lo que anoté del caso»: llena lo que sobra."""
    c = A["color"]
    b.append(rect(x, y, w, h, "white", r=14, stroke="#E6E1E4", sw=2))
    b.append(T(x + 16, y + 28, [rotulo or A["nota"]], 15, c, weight="700", ls=1.5))
    n = int((h - 70) // 48) + 1
    if n > 0:
        b.append(wlines(x + 18, y + 60, w - 36, n, c="#E6EAF0", step=48))


def _instrumento(b, n, inst, x, y, limite):
    """Dibuja el instrumento aparte, lo mide, lo encaja si se pasa y lo pega envuelto."""
    frag = []
    fin = inst(frag, x, y, IW, limite - y)
    s, y_fin, k = encajar(frag, x, y, IW, limite - y)
    if isinstance(fin, (int, float)) and k == 1.0:
        y_fin = max(y_fin, fin)
    b.append(f'<g class="instrumento" data-n="{n}" data-ymax="{limite:.0f}" '
             f'data-xmax="{X_MAX}" data-k="{k:.4f}">{s}</g>')
    return y_fin


def tarjeta(b, y, n, est, pag, ctx, inst, comp=None, **_):
    """Una pregunta del libro. inst(b, x, y, w, h) dibuja su instrumento y devuelve su final."""
    c = _marco_tarjeta(b, y)
    b.append(num_badge(M + 60, y + 52, n, c, r=34, size=34))
    b.append(T(M + 112, y + 44, [f"Pregunta {n} · la lees en tu libro, página {pag}"], 24, c,
               weight="700"))
    b.append(T(M + 112, y + 78, [ctx], 21, GRAY, style="italic"))
    cx, cw = chip_estrategia(b, M + 760, y + 30, est)
    if comp:
        b.append(T(cx + 4, y + 92, [f"competencia · {comp}"], 15, GRAY, style="italic"))
    _primera_idea(b, y, M + 1300, "Mi primera idea, antes de hacer nada:")
    ix, iy = M + 30, y + 130
    fondo = y + BLK_H - 40
    y_fin = _instrumento(b, n, inst, ix, iy, fondo)
    if fondo - (y_fin + 14) >= NOTA_MIN:
        notas(b, ix, y_fin + 14, IW - 4, fondo - y_fin - 14)
    columna_derecha(b, y, est)


# ───────── entrenamiento ICFES ─────────
def membrete(b, x, y, txt):
    """Regla 7: el año solo si está verificado contra el cuadernillo liberado. Si no:
    «Pregunta oficial ICFES · Saber 11»."""
    c = A["color"]
    w = tw(txt, 19, "700") + 48
    b.append(rect(x, y, w, 44, "white", r=10, stroke=c, sw=2.2))
    b.append(rect(x, y, 8, 44, c, r=4))
    b.append(T(x + 30, y + 29, [txt], 19, c, weight="700"))
    return w


def opciones(b, x, y, w, ops, size=19):
    c = A["color"]
    yy = y
    for k, o in enumerate(ops):
        b.append(f'<circle cx="{x + 15}" cy="{yy + 12}" r="15" fill="white" stroke="{c}" '
                 f'stroke-width="2"/>')
        b.append(T(x + 15, yy + 18, ["ABCD"[k]], 16, c, weight="700", anchor="middle"))
        svg, y2 = TJ(x + 47, yy, o, w - 50, size, INK, lh=size + 7)
        b.append(svg)
        yy = y2 + 8
    return yy


def tarjeta_icfes(b, y, q, n):
    """q = dict(est, comp, f=membrete, e=enunciado, o=[4 opciones], datos=fn, inst=fn).
    datos(b, x, y, w) dibuja el texto o la figura y devuelve dónde terminó."""
    est = q["est"]
    c = _marco_tarjeta(b, y)
    b.append(rect(M + 28, y + 22, 60, 60, c, r=12))
    b.append(buoy(M + 58, y + 52, 15))
    b.append(T(M + 112, y + 44, ["Pregunta real para entrenar"], 24, c, weight="700"))
    membrete(b, M + 112, y + 58, q.get("f") or "Pregunta oficial ICFES · Saber 11")
    chip_estrategia(b, M + 1275, y + 30, est, prefijo="entrena la estrategia", derecha=True)
    if q.get("comp"):
        b.append(T(M + 1275, y + 92, [f"competencia · {q['comp']}"], 15, GRAY, style="italic",
                   anchor="end"))
    _primera_idea(b, y, M + 1460, "Mi primera idea:")
    ix, iy = M + 30, y + 118
    svg, yy = TJ(ix, iy, q["e"], IW - 20, 20, INK, lh=28)
    b.append(svg)
    if q.get("datos"):
        yy = q["datos"](b, ix, yy + 10, IW - 20) or yy
    yy = opciones(b, ix, yy + 12, IW - 20, q["o"])
    fondo = y + BLK_H - 40
    y_fin = _instrumento(b, f"icfes-{n}", q["inst"], ix, yy + 14, fondo)
    if fondo - (y_fin + 14) >= NOTA_MIN:
        notas(b, ix, y_fin + 14, IW - 4, fondo - y_fin - 14, rotulo="MIS CUENTAS Y LO QUE SUBRAYÉ")
    columna_derecha(b, y, est, cierre=("¿En qué se parece a lo del taller?",
                                       "(el libro y el ICFES preguntan lo mismo de otra forma)"))


# ───────── franja de vocabulario ─────────
def franja_vocab(b):
    c = A["color"]
    y = VOCAB_Y
    b.append(rect(M, y, CW, VOCAB_H, "white", r=20, stroke=c, sw=2.4))
    b.append(rect(M, y, 8, VOCAB_H, c, r=4))
    b.append(T(M + 34, y + 30, ["PALABRAS QUE ME FRENARON"], 15, c, weight="700", ls=2))
    b.append(T(M + 361, y + 30, ["no la busques todavía: adivínala por el contexto y "
                                 "confírmala en clase"], 15, GRAY, style="italic"))
    b.append(T(M + 34, y + 90, ["la palabra"], 15, GRAY, style="italic"))
    b.append(T(M + 34, y + 140, ["lo que creo que significa"], 15, GRAY, style="italic"))
    for i in range(5):
        x = M + 239 + i * 320
        for yy in (y + 60, y + 112):
            b.append(rect(x, yy, 307, 42, "#F5F6FA", r=10, stroke="#E2E6EE", sw=1.6))


# ───────── hojas completas ─────────
def _pie_texto(tipo):
    return f"{A['area']} · Misión {A['mision']} · {tipo}"


def hoja_taller(nombre, pag, hoja, qa, qb, vocab=True):
    """Una hoja de taller: dos preguntas del libro. Devuelve la ruta del SVG."""
    set_bloque(vocab)
    b = svg_open()
    cabecera(b, f"Prueba de Campo · hoja {hoja} de 5 · preguntas {qa['n']} y {qb['n']}")
    tarjeta(b, Y0, **qa)
    tarjeta(b, y_bloque2(), **qb)
    if vocab:
        franja_vocab(b)
    footer(b, pag, A["color"], texto=_pie_texto("Prueba de Campo"))
    ruta = OUT + nombre + ".svg"
    svg_close(b, ruta)
    return ruta


def hoja_icfes(nombre, pag, qa, qb, vocab=True):
    """Una hoja de entrenamiento: dos preguntas reales del ICFES, cada una con su instrumento."""
    set_bloque(vocab)
    b = svg_open()
    e = sorted({qa["est"], qb["est"]})
    ests = " y ".join(str(x) for x in e)
    cabecera(b, f"Entrenamiento ICFES · entrena las estrategia{'s' if len(e) > 1 else ''} "
                f"{ests} · 2 preguntas reales")
    tarjeta_icfes(b, Y0, qa, 1)
    tarjeta_icfes(b, y_bloque2(), qb, 2)
    if vocab:
        franja_vocab(b)
    footer(b, pag, A["color"], texto=_pie_texto("Entrenamiento ICFES"))
    ruta = OUT + nombre + ".svg"
    svg_close(b, ruta)
    return ruta


# ───────── piezas que usan los instrumentos ─────────
def titulo_instr(b, x, y, t, c, sub=None):
    """Título del instrumento (en el color de la estrategia) y subtítulo justificado."""
    b.append(T(x, y + 30, [t], 30, c, weight="700"))
    if sub:
        svg, yy = TJ(x, y + 42, sub, IW - 20, 20, GRAY, style="italic", lh=26)
        b.append(svg)
        return yy + 14
    return y + 56


def cajas(b, x, y, n, w=92, h=64, gap=14, c=None, labels=None, fill="white"):
    c = c or A["ln"]
    for i in range(n):
        b.append(rect(x + i * (w + gap), y, w, h, fill, r=10, stroke=c, sw=2))
        if labels:
            b.append(T(x + i * (w + gap) + w / 2, y + h + 26, [labels[i]], 18, GRAY,
                       anchor="middle"))
    return y + h + (40 if labels else 0)


def trampa(b, x, y, w, titulo_, texto, c):
    """Recuadro punteado: «una opción dice que…». Texto justificado."""
    svg, yy = TJ(x + 24, y + 50, texto, w - 48, 19, INK, lh=27)
    h = yy - y + 16
    b.append(rect(x, y, w, h, "white", r=14, stroke=c, sw=2.2, dash="8,6"))
    b.append(T(x + 24, y + 34, [titulo_], 20, c, weight="700"))
    b.append(svg)
    return y + h


def ojo(b, x, y, w, titulo_, texto, fuerte=None):
    """Recuadro amarillo. Título en MAYÚSCULAS → rótulo pequeño; en frase → negrilla.
    `fuerte`: una línea en negrilla al final."""
    svg, yy = TJ(x + 24, y + 48, texto, w - 48, 18, INK, lh=26)
    g = [svg]
    if fuerte:
        svg2, yy = TJ(x + 24, yy, fuerte, w - 48, 18, INK, weight="700", lh=26)
        g.append(svg2)
    h = yy - y + 14
    b.append(rect(x, y, w, h, AMBER_BG, r=14, stroke=AMBER_LN, sw=2))
    if titulo_.isupper():      # «OJO CON LA OPCIÓN D»: rótulo pequeño espaciado
        b.append(T(x + 24, y + 30, [titulo_], 15, AMBER_D, weight="700", ls=1.5))
    else:                      # «Los otros tres existen…»: frase en negrilla
        b.append(T(x + 24, y + 32, [titulo_], 19, AMBER_D, weight="700"))
    b.extend(g)
    return y + h


def alto_profe(b, x, y, w, texto):
    """Sello «ALTO · aquí entra el profe»: el concepto que el estudiante no trae.
    Se registra en la matriz (SELLOS)."""
    c = EDU_ORO
    tw_ = w - 380
    svg, yy = TJ(x + 92, y + 52, texto, tw_ - 20, 17, INK, lh=25)
    h = max(yy - y + 18, 130)
    b.append(rect(x, y, w, h, "white", r=14, stroke=c, sw=2.2, dash="8,6"))
    b.append(rect(x, y, 8, h, c, r=4))
    b.append(f'<circle cx="{x + 46}" cy="{y + 44}" r="17" fill="{c}"/>')
    b.append(T(x + 46, y + 52, ["!"], 22, "white", weight="700", anchor="middle"))
    b.append(T(x + 92, y + 30, ["ALTO · AQUÍ ENTRA EL PROFE"], 15, AMBER_D, weight="700", ls=1.5))
    b.append(svg)
    bx = x + w - 300
    b.append(T(bx, y + 30, ["lo que explicó, en mis palabras:"], 15, GRAY, style="italic"))
    b.append(rect(bx, y + 44, 280, h - 62, "white", r=10, stroke=AMBER_LN, sw=2))
    return y + h
