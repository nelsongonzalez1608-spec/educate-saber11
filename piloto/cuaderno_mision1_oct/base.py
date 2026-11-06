#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EduCaTe · Cuaderno de trabajo — MATEMÁTICAS · MISIÓN 1 COMPLETA
Genera las hojas de MISIÓN (acompañan al libro) y de ENTRENAMIENTO ICFES.
Todo sale de los datos de abajo: el diseño es uno solo.
"""
import math, sys, random, base64, os

FILLED = "--lleno" in sys.argv
random.seed(17)
W = 2000

AZ     = "#1F4E8C"; AZ_D  = "#143761"; AZ_BG = "#EFF4FA"; AZ_LN = "#C3D7EA"
AZ_M   = "#5C90C4"; AZ_MD = "#3B6B99"; AZ_MBG = "#F3F7FC"; AZ_MLN = "#D2E2F1"
CORAL  = "#E4572E"; AMBER = "#F2A93B"; AMBER_D = "#9A6608"
AMBER_BG = "#FFF4E0"; AMBER_LN = "#F0CE85"
TEAL   = "#1BA0A8"; NAVY = "#12386B"
INK    = "#20242E"; GRAY = "#6E7480"; LGRAY = "#D8DEE6"; PAPER = "#FFFFFF"
UI     = "Segoe UI, Calibri, Arial, sans-serif"
WRITE  = "Caveat, Patrick Hand, cursive"
PENCIL = "#4E4E58"; PENCIL_L = "#6B6B76"; PENCIL_W = "#E4EEF6"

defs = ['<filter id="sh" x="-30%" y="-30%" width="160%" height="170%">'
        '<feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0E1630" flood-opacity="0.10"/></filter>']


def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def wrap(t, n):
    words, lines, cur = t.split(" "), [], ""
    for w in words:
        s = (cur + " " + w).strip()
        if len(s) > n and cur: lines.append(cur); cur = w
        else: cur = s
    if cur: lines.append(cur)
    return lines


def T(x, y, lines, size, color, weight="400", anchor="start", lh=None,
      font=UI, style="normal", ls=0, rot=0, op=1):
    lh = lh or size * 1.3
    ls_a = f' letter-spacing="{ls}"' if ls else ""
    tf = f' transform="rotate({rot} {x} {y})"' if rot else ""
    out = [f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
           f'fill="{color}" text-anchor="{anchor}" font-style="{style}" opacity="{op}"{ls_a}{tf}>']
    for i, ln in enumerate(lines):
        out.append(f'<tspan x="{x}" dy="{0 if i == 0 else lh}">{esc(ln)}</tspan>')
    out.append("</text>")
    return "".join(out)


def rect(x, y, w, h, fill, r=14, stroke=None, sw=0, dash=None, op=1):
    s = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" ry="{r}" fill="{fill}"{s}{d} opacity="{op}"/>')


def line(x1, y1, x2, y2, c, sw=2, dash=None, cap="round"):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{sw}" stroke-linecap="{cap}"{d}/>'


def img(path, x, y, w, h):
    b64 = base64.b64encode(open(path, "rb").read()).decode()
    return (f'<image x="{x}" y="{y}" width="{w}" height="{h}" xlink:href="data:image/png;base64,{b64}" '
            f'preserveAspectRatio="xMidYMid meet"/>')



# ───── logo EduCaTe ─────
LOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo_educate.png")
LOGO_AR = 296 / 134          # proporción real del archivo
_LOGO_B64 = None


def logo_w(h): return h * LOGO_AR


def logo(x, y, h=58, chip=False, pad=12, chip_fill="white", r=14):
    """Logo real de EduCaTe con esquina superior izquierda en (x, y).
    chip=True lo pone sobre una tarjeta blanca (para fondos oscuros)."""
    global _LOGO_B64
    if _LOGO_B64 is None:
        _LOGO_B64 = base64.b64encode(open(LOGO_PATH, "rb").read()).decode()
    w = logo_w(h); g = []
    if chip:
        g.append(rect(x - pad, y - pad, w + pad * 2, h + pad * 2, chip_fill, r=r))
    g.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" '
             f'xlink:href="data:image/png;base64,{_LOGO_B64}" preserveAspectRatio="xMidYMid meet"/>')
    return "".join(g)


def checkbox(x, y, s=11, c=NAVY): return rect(x, y, s * 2, s * 2, "white", r=3, stroke=c, sw=2.2)


def dots(x, y, c, r=3.2, step=13, cols=7, rows=4, op=0.5):
    return "".join(f'<circle cx="{x+i*step}" cy="{y+j*step}" r="{r}" fill="{c}" opacity="{op}"/>'
                   for i in range(cols) for j in range(rows))


def wlines(x, y, w, n, c=LGRAY, step=34):
    return "".join(line(x, y + i * step, x + w, y + i * step, c, 1.8) for i in range(n))


def grid_box(x, y, w, h, c="#D6E5F4", step=26):
    g = [rect(x, y, w, h, "white", r=10, stroke=c, sw=2)]
    gx = x + step
    while gx < x + w - 4: g.append(line(gx, y + 6, gx, y + h - 6, c, 0.9, cap="butt")); gx += step
    gy = y + step
    while gy < y + h - 4: g.append(line(x + 6, gy, x + w - 6, gy, c, 0.9, cap="butt")); gy += step
    return "".join(g)


def rocket(cx, cy, s, c, accent="#FFFFFF", flame=AMBER):
    return ("".join([
        f'<path d="M {cx},{cy-s} C {cx+0.52*s},{cy-0.34*s} {cx+0.52*s},{cy+0.34*s} {cx+0.28*s},{cy+0.60*s} '
        f'L {cx-0.28*s},{cy+0.60*s} C {cx-0.52*s},{cy+0.34*s} {cx-0.52*s},{cy-0.34*s} {cx},{cy-s} Z" fill="{c}"/>',
        f'<path d="M {cx-0.28*s},{cy+0.16*s} L {cx-0.74*s},{cy+0.68*s} L {cx-0.28*s},{cy+0.60*s} Z" fill="{c}" opacity="0.75"/>',
        f'<path d="M {cx+0.28*s},{cy+0.16*s} L {cx+0.74*s},{cy+0.68*s} L {cx+0.28*s},{cy+0.60*s} Z" fill="{c}" opacity="0.75"/>',
        f'<circle cx="{cx}" cy="{cy-0.16*s}" r="{0.21*s}" fill="{accent}"/>',
        f'<path d="M {cx-0.15*s},{cy+0.62*s} L {cx},{cy+1.02*s} L {cx+0.15*s},{cy+0.62*s} Z" fill="{flame}"/>']))


def diana(cx, cy, r, c):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="3"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.58}" fill="none" stroke="{c}" stroke-width="2.6"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*0.2}" fill="{c}"/>')


def buoy(cx, cy, r, c="white"):
    g = [f'<circle cx="{cx}" cy="{cy}" r="{r+5}" fill="white" opacity="0.20"/>',
         f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{c}" stroke-width="4.2"/>']
    for dx, dy in [(-1, 0), (1, 0)]:
        g.append(line(cx + dx * (r + 5), cy, cx + dx * (r - 5), cy, c, 4.2))
    for dy in (-1, 1):
        g.append(line(cx, cy + dy * (r + 5), cx, cy + dy * (r - 5), c, 4.2))
    return "".join(g)


# ───── lápiz ─────
def jit(v, a=1.3): return v + random.uniform(-a, a)


def PT(x, y, lines, size=26, color=PENCIL, rot=None, lh=None, anchor="start", op=0.92):
    rot = random.uniform(-1.0, 1.0) if rot is None else rot
    return T(x, y, lines, size, color, anchor=anchor, lh=lh or size * 1.12, font=WRITE, rot=rot, op=op)


def spath(pts, c=PENCIL, sw=2.6, op=0.9):
    return (f'<path d="M {" L ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)}" fill="none" stroke="{c}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" opacity="{op}"/>')


def ring(cx, cy, r=15, c=PENCIL, sw=2.6):
    g = []
    for k in range(2):
        pts = [(cx + r * (0.92 + 0.10 * math.sin(i / 25 * 2 * math.pi * 3 + k)) * math.cos(i / 25 * 2 * math.pi + k * 0.5) + jit(0, .8),
                cy + r * (0.92 + 0.10 * math.sin(i / 25 * 2 * math.pi * 3 + k)) * math.sin(i / 25 * 2 * math.pi + k * 0.5) + jit(0, .8))
               for i in range(26)]
        pts.append(pts[0]); g.append(spath(pts, c, sw, 0.85))
    return "".join(g)


def pfill(cx, cy, r=8, c=PENCIL):
    g, y = [], cy - r
    while y < cy + r:
        dx = math.sqrt(max(0.0, r * r - (y - cy) ** 2))
        g.append(spath([(cx - dx, jit(y, .4)), (cx + dx, jit(y, .4))], c, 1.6, 0.55)); y += 4.4
    return "".join(g)


def pcheck(x, y, s=20, c=PENCIL):
    return spath([(jit(x), jit(y + s * .45)), (jit(x + s * .36), jit(y + s * .85)), (jit(x + s * 1.02), jit(y - s * .18))], c, 3.0, .9)


# ═══════════════ PIEZAS COMUNES ═══════════════
def encabezado(body, subt):
    HY = 34
    body.append(rect(40, HY, 300, 168, "white", r=16, stroke="#C9D2DC", sw=2.4))
    body.append(logo(190 - logo_w(84) / 2, HY + 42, 84))
    CX, CW = 368, 900
    body.append(rect(CX, HY, CW, 168, "white", r=16, stroke=TEAL, sw=2.4))
    body.append(rect(CX + CW / 2 - 190, HY - 16, 380, 44, AZ, r=22))
    body.append(T(CX + CW / 2, HY + 14, ["COMPETENCIAS"], 24, "white", weight="700", anchor="middle", ls=1))
    for i, (l1, l2, c) in enumerate([("Interpretación", "y representación", AZ),
                                     ("Formulación", "y ejecución", CORAL),
                                     ("Argumentación", "", AZ_M)]):
        cw3 = (CW - 60) / 3; cx = CX + 30 + i * cw3
        body.append(rect(cx, HY + 44, cw3 - 14, 110, "#FBFCFD", r=12, stroke="#E3E8EE", sw=1.6))
        body.append(f'<circle cx="{cx+(cw3-14)/2}" cy="{HY+80}" r="23" fill="{c}"/>')
        body.append(T(cx + (cw3 - 14) / 2, HY + 126, [l1], 17, NAVY, weight="700", anchor="middle"))
        if l2: body.append(T(cx + (cw3 - 14) / 2, HY + 146, [l2], 17, NAVY, weight="700", anchor="middle"))
    KX, KW = 1300, W - 40 - 1300
    body.append(rect(KX, HY, KW, 168, "white", r=16, stroke=TEAL, sw=2.4))
    body.append(f'<circle cx="{KX+70}" cy="{HY+58}" r="34" fill="{TEAL}"/>')
    body.append(T(KX + 122, HY + 50, ["NUMÉRICO-"], 27, AZ_D, weight="700"))
    body.append(T(KX + 122, HY + 82, ["VARIACIONAL"], 27, AZ_D, weight="700"))
    body.append(line(KX + 24, HY + 104, KX + KW - 24, HY + 104, "#DDE5EC", 2))
    body.append(T(KX + 24, HY + 142, [subt], 19, GRAY))
    return HY + 168 + 26


def pie(body, y, texto):
    body.append(rect(40, y, W - 80, 74, NAVY, r=16))
    body.append(T(150, y + 47, ["Aprende"], 26, "white", weight="700"))
    body.append(f'<circle cx="300" cy="{y+39}" r="8" fill="{AZ_M}"/>')
    body.append(T(330, y + 47, ["Practica"], 26, "white", weight="700"))
    body.append(f'<circle cx="478" cy="{y+39}" r="8" fill="{AMBER}"/>')
    body.append(T(508, y + 47, ["Avanza"], 26, "white", weight="700"))
    body.append(T(W - 70, y + 47, [texto], 19, "#AFC4E0", anchor="end"))
    return y + 74 + 34


def salvavidas(g, X, PAD, CARD_W, sy, col_d, prompt, h=96, fill_txt=None):
    g.append(rect(X + PAD, sy, CARD_W - PAD * 2, h, col_d, r=14))
    g.append(buoy(X + PAD + 42, sy + 32, 13))
    g.append(T(X + PAD + 70, sy + 39, ["SALVAVIDAS"], 20, "white", weight="700", ls=1))
    g.append(T(X + PAD + 212, sy + 38, ["· ruta mínima — " + prompt], 18, "#BFD4F2", style="italic"))
    g.append(T(X + PAD + 34, sy + 74, ["Lo mínimo que sí tenía claro:"], 19, "white"))
    g.append(line(X + PAD + 304, sy + 78, X + PAD + 980, sy + 78, "white", 2, "6,6"))
    g.append(T(X + PAD + 1004, sy + 74, ["→  tenía que ser"], 19, "white"))
    g.append(line(X + PAD + 1178, sy + 78, X + PAD + 1270, sy + 78, "white", 2, "6,6"))
    g.append(T(X + PAD + 1292, sy + 74, ["porque"], 19, "white"))
    g.append(line(X + PAD + 1372, sy + 78, X + PAD + 1464, sy + 78, "white", 2, "6,6"))
    g.append(T(X + PAD + 1486, sy + 74, ["no podía ser."], 19, "white"))
    if FILLED and fill_txt:
        a, b, c = fill_txt
        g.append(PT(X + PAD + 318, sy + 74, [a], 25, PENCIL_W, rot=-0.4))
        g.append(PT(X + PAD + 1196, sy + 74, [b], 30, PENCIL_W, rot=-1.5))
        g.append(PT(X + PAD + 1388, sy + 74, [c], 25, PENCIL_W, rot=0.5))
    return sy + h
