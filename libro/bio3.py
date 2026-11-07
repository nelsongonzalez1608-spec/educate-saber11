#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 3 · componente biológico-ecosistémico · páginas 154–160.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 3» de Biología, páginas 94–97.
Casos: calefacción del suelo y biomasa (1), restauración de un humedal (2 a 4), la cadena de la
sabana del Casanare con el jaguar (5 y 6), las pilas usadas (7) y los fertilizantes en un cultivo
de tomate (8 a 10).

Claves verificadas (resueltas a mano contra los datos del libro, no copiadas, 7 nov 2026):

    1·C  2·A  3·B  4·C  5·B  6·D  7·C  8·D  9·B  10·D

Cómo se resolvieron:
  1 · La zona A sube de 670 a 730 (+60); la B baja de 665 a 405 (−260, un 39 %). Lo único que el
      experimento cambió fue la temperatura del suelo y lo que midió fue la biomasa vegetal: la
      hipótesis que usa solo eso es C (el calor bajó la eficiencia fotosintética). A necesita
      herbívoros que nadie midió; B dice que descomponer más «disminuye la producción primaria»
      (descomponer libera nutrientes, no frena a la planta); D habla de la zona A y de especies
      invasoras que el texto no menciona.
  2 · Las aves vuelven cuando hay comida y refugio: insectos y flora nativa → A. B, C y D unen
      algo que sí pasó con un efecto que el texto no dice (competencia, atracción, inmunidad).
  3 · La flora nativa restablece interacciones planta–animal (polinización, dispersión) → B.
  4 · Lo único distinto de esa zona es el oxígeno disuelto bajo; las especies sensibles no
      pueden vivir ahí → C (factor limitante).
  5 · Sin depredador, nada controla a los herbívoros → B. A es falsa: el jaguar no come pasto.
  6 · Los chigüiros que se acumularon mientras no estaba el jaguar siguen comiendo pasto → D.
  7 · Las pilas llevan metales pesados que contaminan agua y suelo si no se aíslan → C.
  8 · Parcela B frente al control C: 2,8 contra 2,1 millones (+0,7), 41 % contra 38 % de
      descomponedoras (+3), 19 % contra 15 % de fijadoras (+4): sube en todo → D. A dice que
      redujo (falso), B habla de la parcela sin fertilizante, C de la química.
  9 · B gana las tres filas y es la que cuida la biodiversidad microbiana → B. A y D son falsas
      contra la tabla (A tiene menos organismos y menos fijadoras); C afirma una productividad
      que la tabla no midió.
 10 · «A largo plazo» pide varios ciclos y «salud del suelo» se midió con la diversidad
      microbiana → D.

Reparto: A 1 · B 3 · C 3 · D 3. Equilibrado. En 2, 3, 4 y 5 la correcta es la única «razonable»
y las otras tres son disparates visibles: registrado en tablero/propuestas/bio3_hallazgos.csv.

Estrategias:
    1 · Los datos hablan primero                 (8, 9        · ICFES 67)   azul
    2 · Sigue la red: quién depende de quién     (2, 5, 6     · ICFES 116)  morado
    3 · Busca el factor que limita               (1, 4        · ICFES 94)   rojo
    4 · Del saber ecológico a la decisión        (3, 7, 10    · ICFES 59)   oro

Hojas: 154 bio3_t1 (1-2) · 155 bio3_t2 (3-4) · 156 bio3_i1 · 157 bio3_t3 (5-6) ·
       158 bio3_t4 (7-8) · 159 bio3_t5 (9-10) · 160 bio3_i2.
"""
from taller_base import *

configurar("Biología", 3, "biológico-ecosistémico",
           tema="En el ecosistema nada cambia solo",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Los datos hablan primero", EDU_AZUL),
       2: ("Sigue la red: quién depende de quién", MORADO),
       3: ("Busca el factor que limita", EDU_ROJO),
       4: ("Del saber ecológico a la decisión", EDU_ORO)}
usar_estrategias(EST)
AZ, MO, RO, OR = (EST[k][1] for k in (1, 2, 3, 4))
VERDE = A["color"]


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def letra(b, cx, cy, L, c, r=17, size=16):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="2"/>')
    b.append(T(cx, cy + size * 0.38, [L], size, c, weight="700", anchor="middle"))


def parrafo(b, x, y, w, texto, size=17, color=INK, style="normal"):
    svg, yy = TJ(x, y, texto, w, size, color, style=style, lh=size + 8)
    b.append(svg)
    return yy


def frase_hueco(b, x, y, w, texto, c, h=50, size=18):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [texto], size, INK, weight="700"))
    return y + h


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12):
    """Flecha recta sin pulso (para esquemas)."""
    b.append(line(x1, y1, x2, y2, c, sw))
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (-1, 1):
        a = ang + math.pi + s * 0.45
        b.append(line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), c, sw))


def fila_letras(b, x, y, c, rotulo, ancho=70, paso=190):
    """A B C D con una casilla al lado para escribir (un número, una letra, una palabra)."""
    b.append(T(x, y + 20, [rotulo], 18, INK, weight="700"))
    y += 36
    for k, L in enumerate("ABCD"):
        bx = x + k * paso
        letra(b, bx + 18, y + 22, L, c)
        caja(b, bx + 48, y, ancho, 44, c)
    return y + 60


# ───────── P1 · calefacción del suelo · biomasa ─────────
def i1(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dos zonas en la misma gráfica", c,
                      "Pasa la tabla del libro a la gráfica: un punto por mes para cada zona (un círculo para la "
                      "zona A, una cruz para la zona B) y únelos. Una tabla se lee número por número; una gráfica te muestra de una vez hacia dónde "
                      "va cada zona.")
    x0, ww = x + 22, w - 44
    # ejes
    gx, gy, gw, gh = x0 + 66, yy + 40, 560, 290
    vmin, vmax = 400, 750
    for k, v in enumerate(range(vmin, vmax + 1, 50)):
        py = gy + gh - (v - vmin) / (vmax - vmin) * gh
        b.append(line(gx, py, gx + gw, py, LGRAY, 1.6))
        b.append(T(gx - 12, py + 6, [str(v)], 15, GRAY, anchor="end"))
    for m in range(1, 9):
        px = gx + (m - 0.5) / 8 * gw
        b.append(line(px, gy, px, gy + gh, LGRAY, 1.2, dash="3,6"))
        b.append(T(px, gy + gh + 26, [str(m)], 15, GRAY, anchor="middle"))
    b.append(line(gx, gy + gh, gx + gw, gy + gh, INK, 2.4))
    b.append(line(gx, gy - 6, gx, gy + gh, INK, 2.4))
    b.append(T(gx + gw / 2, gy + gh + 52, ["mes"], 15, GRAY, style="italic", anchor="middle"))
    b.append(T(gx - 12, gy - 24, ["biomasa"], 15, GRAY, style="italic", anchor="end"))
    # columna de cuentas
    rx = gx + gw + 40
    rw = x0 + ww - rx
    caja(b, rx, gy - 4, rw, 92, c, r=14)
    rot(b, rx + 18, gy + 24, "LO ÚNICO QUE EL EXPERIMENTO CAMBIÓ", c, size=14)
    renglon(b, rx + 18, gy + 68, rx + rw - 18)
    caja(b, rx, gy + 104, rw, 122, c, r=14)
    rot(b, rx + 18, gy + 132, "DEL MES 1 AL MES 8", c, size=14)
    pista(b, rx + 200, gy + 132, "+ si subió, − si bajó")
    b.append(T(rx + 18, gy + 172, ["la zona A cambió:"], 17, INK))
    b.append(T(rx + 18, gy + 210, ["la zona B cambió:"], 17, INK))
    for k in range(2):
        caja(b, rx + 170, gy + 146 + k * 38, 110, 34, c, r=8)
    caja(b, rx, gy + 238, rw, 82, c, r=14)
    rot(b, rx + 18, gy + 264, "LO QUE MIDIERON (Y NADA MÁS)", c, size=14)
    renglon(b, rx + 18, gy + 304, rx + rw - 18)
    yy = gy + gh + 72
    yy = fila_letras(b, x0, yy, c, "¿Cuántas cosas que nadie midió necesita cada hipótesis para funcionar?")
    return ojo(b, x0, yy + 4, ww, "UNA HIPÓTESIS COHERENTE NO INVENTA PERSONAJES",
               "La mejor explicación usa lo que el experimento cambió y lo que midió, con el menor número de "
               "supuestos extra. Fíjate también de qué zona habla cada opción: la pregunta es sobre la zona B.")


# ───────── P2 · el humedal · por qué vuelven las aves ─────────
def i2(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Lo que un ave necesita para volver", c,
                      "Ponte en el lugar del ave. Para volver a un humedal necesita cuatro cosas. Escribe qué le "
                      "ofrece hoy el humedal en cada una, según el texto, y marca si el texto lo dice o si tú lo "
                      "supones.")
    x0, ww = x + 22, w - 44
    cx, cy = x0 + ww / 2, yy + 150
    # el ave, al centro (silueta sencilla)
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="96" ry="58" fill="{SOFT}" stroke="{c}" stroke-width="2.6"/>')
    b.append(f'<path d="M {cx - 40} {cy - 6} Q {cx - 4} {cy - 70} {cx + 44} {cy - 14}" fill="none" '
             f'stroke="{c}" stroke-width="2.4"/>')
    b.append(f'<circle cx="{cx + 70}" cy="{cy - 34}" r="5" fill="{c}"/>')
    b.append(f'<path d="M {cx + 92} {cy - 30} L {cx + 118} {cy - 22} L {cx + 92} {cy - 16} Z" fill="{c}"/>')
    rot(b, cx, cy + 34, "EL AVE QUE VOLVIÓ", c, size=13, anchor="middle")
    cw_, ch_ = 450, 124
    necesidades = (("ALIMENTO", x0, yy), ("REFUGIO", x0 + ww - cw_, yy),
                   ("AGUA PARA VIVIR", x0, yy + 176), ("DÓNDE ANIDAR", x0 + ww - cw_, yy + 176))
    for k, (rt, bx, by) in enumerate(necesidades):
        caja(b, bx, by, cw_, ch_, c, r=14)
        rot(b, bx + 18, by + 28, rt, c, size=14)
        pista(b, bx + 18, by + 54, "lo que hoy le ofrece el humedal:")
        renglon(b, bx + 18, by + 84, bx + cw_ - 18)
        for j, lab in enumerate(("el texto lo dice", "lo supongo")):
            b.append(checkbox(bx + 18 + j * 190, by + 94, s=9, c=c))
            b.append(T(bx + 44 + j * 190, by + 110, [lab], 15, GRAY))
        ex = bx + cw_ + 6 if bx == x0 else bx - 6
        b.append(hand_arrow(ex, by + ch_ / 2, cx + (-100 if bx == x0 else 100), cy, c, sw=2.2, bend=0.0, head=11))
    yy += 176 + ch_ + 26
    # regla de lo lejano a lo directo
    b.append(T(x0, yy + 20, ["Ubica las letras A, B, C y D en la regla: ¿qué tan cerca toca cada opción lo que el ave "
                             "necesita?"], 18, INK, weight="700"))
    ly = yy + 66
    b.append(line(x0 + 30, ly, x0 + ww - 30, ly, c, 3))
    for k in range(9):
        px = x0 + 30 + k * (ww - 60) / 8
        b.append(line(px, ly - 10, px, ly + 10, c, 2.4))
    pista(b, x0 + 30, ly + 34, "no tiene que ver")
    pista(b, x0 + ww / 2, ly + 34, "causa lejana", anchor="middle")
    pista(b, x0 + ww - 30, ly + 34, "causa directa", anchor="end")
    return trampa(b, x0, ly + 52, ww, "Que algo haya pasado no lo vuelve la causa:",
                  "una opción puede nombrar algo que sí se hizo en el humedal y pegarle un efecto que el texto no "
                  "cuenta. Pregúntale a cada opción: ¿el texto dice que eso produjo aquello?", c)


# ───────── P3 · el humedal · aplicar la ecología ─────────
def _planta(b, cx, by, c):
    """Planta esquemática: tallo, hojas, una flor y un fruto. by = suelo."""
    b.append(line(cx, by, cx, by - 210, VERDE, 4))
    for k, (dx, dy, s) in enumerate(((-1, 60, 1), (1, 100, 1), (-1, 140, 1))):
        ex = cx + dx * 46
        b.append(f'<ellipse cx="{ex}" cy="{by - dy}" rx="44" ry="16" fill="{SOFT}" stroke="{VERDE}" '
                 f'stroke-width="2.2" transform="rotate({-dx * 24} {ex} {by - dy})"/>')
    for a in range(0, 360, 60):
        px = cx + 22 * math.cos(math.radians(a))
        py = by - 232 + 22 * math.sin(math.radians(a))
        b.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="14" fill="white" stroke="{c}" stroke-width="2"/>')
    b.append(f'<circle cx="{cx}" cy="{by - 232}" r="11" fill="{c}"/>')
    b.append(f'<circle cx="{cx + 56}" cy="{by - 176}" r="15" fill="{RO}" opacity="0.85"/>')
    b.append(line(cx + 10, by - 176, cx + 44, by - 176, VERDE, 2.4))
    b.append(line(cx - 70, by, cx + 70, by, GRAY, 2.4))


def i3(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Ida y vuelta entre la planta y el animal", c,
                      "Aplicar la ecología es explicar cómo un ser vivo depende de otro. Llena las dos flechas de "
                      "cada lado: lo que la planta nativa le da al animal y lo que el animal le devuelve a la "
                      "planta.")
    x0, ww = x + 22, w - 44
    cx = x0 + ww / 2
    _planta(b, cx, yy + 290, c)
    rot(b, cx, yy + 318, "LA PLANTA NATIVA", c, size=13, anchor="middle")
    bw_ = 400
    for k, quien in enumerate(("EL INSECTO", "EL AVE")):
        bx = x0 if k == 0 else x0 + ww - bw_
        caja(b, bx, yy + 10, bw_, 290, c, r=16)
        rot(b, bx + 20, yy + 40, quien, c, size=15)
        pista(b, bx + 20, yy + 76, "la planta le da:")
        renglon(b, bx + 20, yy + 114, bx + bw_ - 20)
        renglon(b, bx + 20, yy + 152, bx + bw_ - 20)
        pista(b, bx + 20, yy + 196, "y el animal le devuelve:")
        renglon(b, bx + 20, yy + 234, bx + bw_ - 20)
        renglon(b, bx + 20, yy + 272, bx + bw_ - 20)
        inner = bx + bw_ + 8 if k == 0 else bx - 8
        px = cx - 90 if k == 0 else cx + 90
        b.append(hand_arrow(px, yy + 100, inner, yy + 100, c, sw=2.4, bend=0.0, head=12))
        b.append(hand_arrow(inner, yy + 220, px, yy + 220, c, sw=2.4, bend=0.0, head=12))
    yy += 346
    yy = frase_hueco(b, x0, yy, ww, "Una relación que volvió con la flora nativa:  el ____________ le ____________ "
                                    "a la ____________ .", c)
    return ojo(b, x0, yy + 16, ww, "Aplicar es conectar dos seres vivos:",
               "si una opción no nombra ninguna relación entre seres vivos, no está aplicando la ecología, está "
               "hablando de otra cosa. Y si nombra una, verifica que el texto la respalde antes de creerle.")


# ───────── P4 · el humedal · la zona con poco oxígeno ─────────
def i4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El barril del humedal: la duela más corta manda", c,
                      "Un barril hecho de duelas (las tablas de los lados) solo se llena hasta la duela más corta. Así funciona un ecosistema: "
                      "basta que falte una condición para que muchas especies no lleguen, aunque las demás estén "
                      "bien. Escribe en cada duela una condición de esa zona.")
    x0, ww = x + 22, w - 44
    # barril
    bx, by, bw = x0 + 20, yy + 20, 400
    alturas = (300, 290, 300, 150, 296, 286)
    sw_ = bw / len(alturas)
    base = by + 320
    for k, hh in enumerate(alturas):
        px = bx + k * sw_
        caja(b, px + 3, base - hh, sw_ - 6, hh, c, sw=2.2, r=6)
        b.append(T(px + sw_ / 2, base - hh - 10, [str(k + 1)], 15, c, weight="700", anchor="middle"))
    b.append(rect(bx + 3, base - 140, bw - 6, 140, "#DCEAF7", r=4, op=0.75))
    b.append(line(bx - 8, base - 140, bx + bw + 8, base - 140, AZ, 2.4, dash="8,6"))
    pista(b, bx + bw / 2, base + 26, "hasta aquí se llena", anchor="middle")
    # tabla de condiciones
    tx = bx + bw + 46
    tw_ = x0 + ww - tx
    rot(b, tx, by + 10, "DUELA · LA CONDICIÓN QUE REPRESENTA", c, size=14)
    for k in range(6):
        ry = by + 30 + k * 50
        letra(b, tx + 16, ry + 20, str(k + 1), c, r=14, size=14)
        renglon(b, tx + 44, ry + 34, tx + tw_)
    yy = base + 50
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("LO QUE ESTA ZONA TIENE IGUAL", "a las otras zonas del humedal"),
                                  ("LO ÚNICO QUE TIENE DISTINTO", "según los registros"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 118, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        pista(b, px + 18, yy + 52, ps)
        renglon(b, px + 18, yy + 86, px + half - 18)
    yy += 134
    return frase_hueco(b, x0, yy, ww, "La duela corta de esta zona es ____________ , y por eso no llegan las "
                                      "especies que ______________________ .", c)


# ───────── P5 · sabana del Casanare · sin jaguar ─────────
def i5(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Saca al jaguar y mira qué se mueve", c,
                      "Dibuja tú las flechas de la cadena: la flecha va del que es comido al que come. Después tacha "
                      "al jaguar y marca, debajo de cada ser vivo, si su población sube, baja o se queda igual.")
    x0, ww = x + 22, w - 44
    nodos = (("GRAMÍNEAS", "productor"), ("CHIGÜIROS", "herbívoro"), ("JAGUARES", "carnívoro"))
    nw, nh, gap = 290, 96, (ww - 3 * 290) / 2
    ny = yy + 20
    for k, (n, rol) in enumerate(nodos):
        px = x0 + k * (nw + gap)
        caja(b, px, ny, nw, nh, c, sw=2.4, r=48)
        rot(b, px + nw / 2, ny + 44, n, c, size=17, anchor="middle")
        pista(b, px + nw / 2, ny + 70, rol, anchor="middle")
        for j, sim in enumerate(("sube", "baja", "igual")):
            qx = px + 30 + j * 90
            b.append(checkbox(qx, ny + nh + 22, s=11, c=c))
            b.append(T(qx + 28, ny + nh + 40, [sim], 16, GRAY))
    # hongos abajo
    hy = ny + nh + 110
    hw = 420
    caja(b, x0 + ww / 2 - hw / 2, hy, hw, 80, c, sw=2.4, r=40, dash="8,6")
    rot(b, x0 + ww / 2, hy + 36, "HONGOS DESCOMPONEDORES", c, size=15, anchor="middle")
    pista(b, x0 + ww / 2, hy + 60, "¿de quiénes reciben materia?", anchor="middle")
    yy = hy + 104
    yy = frase_hueco(b, x0, yy, ww, "Mientras estaba, el jaguar le hacía a la población de chigüiros de "
                                    "______________________ .", c)
    return trampa(b, x0, yy + 16, ww, "Una opción dice que jaguar y chigüiro competían por alimento:",
                  "mira tus flechas. ¿Comen lo mismo? Si no comparten alimento, no pueden competir por él, y esa "
                  "explicación se cae sola.", c)


# ───────── P6 · sabana del Casanare · vuelve el jaguar ─────────
def i6(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Tres fotos de la sabana: antes, sin jaguar y al volver", c,
                      "Colorea con lápiz la altura de cada barra según cuántos hay en cada momento (pocos abajo, "
                      "muchos arriba). La pregunta está en la tercera foto: ¿con qué se encuentra el jaguar cuando "
                      "vuelve?")
    x0, ww = x + 22, w - 44
    fotos = ("1 · ANTES", "2 · SIN JAGUAR", "3 · CUANDO VUELVE")
    gap = 30
    fw = (ww - 2 * gap) / 3
    fh = 300
    for k, ft in enumerate(fotos):
        fx = x0 + k * (fw + gap)
        caja(b, fx, yy, fw, fh, c, sw=2.2, r=14)
        rot(b, fx + 18, yy + 28, ft, c, size=14)
        base = yy + fh - 50
        b.append(line(fx + 20, base, fx + fw - 20, base, INK, 2))
        pista(b, fx + 14, yy + 62, "muchos", size=13)
        pista(b, fx + 14, base - 6, "pocos", size=13)
        for j, quien in enumerate(("gramíneas", "chigüiros", "jaguares")):
            bxx = fx + 80 + j * (fw - 110) / 3
            bw_ = (fw - 110) / 3 - 18
            b.append(rect(bxx, yy + 46, bw_, base - yy - 46, "white", r=4, stroke=LGRAY, sw=2, dash="5,5"))
            b.append(T(bxx + bw_ / 2, base + 24, [quien], 14, GRAY, anchor="middle"))
        if k < 2:
            b.append(hand_arrow(fx + fw + 2, yy + fh / 2, fx + fw + gap - 2, yy + fh / 2, c, sw=2.4, bend=0.0,
                                head=10))
    yy += fh + 22
    caja(b, x0, yy, ww, 120, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE ENCUENTRA EL JAGUAR AL VOLVER", c, size=14)
    pista(b, x0 + 20, yy + 58, "¿cuántos chigüiros hay en la foto 3, los de la foto 1 o los de la foto 2? ¿y qué "
                               "están haciendo con las gramíneas?")
    renglon(b, x0 + 20, yy + 98, x0 + ww - 20)
    yy += 136
    return trampa(b, x0, yy, ww, "Una opción dice que la recuperación depende «exclusivamente» de dos niveles:",
                  "busca en tus tres fotos a los chigüiros. Si en alguna foto ellos pesan sobre las gramíneas, "
                  "ninguna explicación que los deje por fuera puede ser coherente con la cadena.", c)


# ───────── P7 · pilas usadas ─────────
def i7(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El viaje de una pila después de la caneca", c,
                      "Sigue a una pila que se bota mal. En cada parada escribe qué le pasa a ella y qué le pasa a lo "
                      "que lleva adentro. Un criterio científico sale de lo que ocurre en este viaje.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 86, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE LLEVA ADENTRO UNA PILA", c, size=14)
    pista(b, x0 + 340, yy + 30, "aunque esté «descargada»")
    renglon(b, x0 + 20, yy + 70, x0 + ww - 20)
    yy += 110
    paradas = ("1 · la caneca", "2 · el botadero", "3 · la lluvia", "4 · el suelo y el agua", "5 · los seres vivos")
    n = len(paradas)
    pw = (ww - (n - 1) * 22) / n
    ly = yy + 24
    pts = " L ".join(f"{x0 + pw / 2 + k * (pw + 22):.0f} {ly + (14 if k % 2 else -6)}" for k in range(n))
    b.append(f'<path d="M {pts}" fill="none" stroke="{c}" stroke-width="3" stroke-dasharray="10,8"/>')
    for k, p in enumerate(paradas):
        px = x0 + k * (pw + 22)
        cyy = ly + (14 if k % 2 else -6)
        b.append(f'<circle cx="{px + pw / 2:.0f}" cy="{cyy}" r="16" fill="white" stroke="{c}" stroke-width="3"/>')
        b.append(T(px + pw / 2, cyy + 6, [str(k + 1)], 15, c, weight="700", anchor="middle"))
        caja(b, px, ly + 40, pw, 170, c, r=14)
        rot(b, px + 14, ly + 66, p.split(" · ")[1].upper(), c, size=13)
        for j in range(3):
            renglon(b, px + 14, ly + 106 + j * 36, px + pw - 14)
    yy = ly + 232
    yy = alto_profe(b, x0, yy, ww,
                    "Pregúntale al profe qué materiales lleva una pila por dentro y qué quiere decir que esté "
                    "«descargada»: ¿se le acabó la energía o se le acabó lo que tiene adentro?")
    return ojo(b, x0, yy + 14, ww, "UN CRITERIO CIENTÍFICO SE PUEDE COMPROBAR",
               "Busca en cada opción su «porque» y pregúntale dos cosas: ¿se podría comprobar en un laboratorio? "
               "¿Explica lo que le pasa al ambiente en tu viaje de cinco paradas?")


# ───────── P8 · fertilizantes · parcela B ─────────
FILAS_8 = ("microorganismos", "descomponedoras", "fijadoras")


def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El control es el cero: barras hacia arriba o hacia abajo", c,
                      "La parcela C no recibió fertilizante: es el control, y en esta gráfica es la raya del cero. "
                      "Para cada fila de la tabla, dibuja una barra para B y otra para A: hacia arriba si quedó por "
                      "encima del control, hacia abajo si quedó por debajo. Escribe en la punta cuánto.")
    x0, ww = x + 22, w - 44
    gx, gw = x0 + 70, ww - 70
    top, alto = yy + 20, 300
    cero = top + alto / 2
    b.append(line(gx, top, gx, top + alto, INK, 2.2))
    b.append(line(gx, cero, gx + gw, cero, INK, 3))
    b.append(T(gx - 12, cero + 6, ["C = 0"], 15, INK, weight="700", anchor="end"))
    pista(b, gx - 12, top + 14, "más", anchor="end")
    pista(b, gx - 12, top + alto - 4, "menos", anchor="end")
    for k in (1, 2, 3):
        for sgn in (-1, 1):
            b.append(line(gx, cero + sgn * k * alto / 8, gx + gw, cero + sgn * k * alto / 8, LGRAY, 1.4, "3,6"))
    gw3 = gw / 3
    for i, f in enumerate(FILAS_8):
        fx = gx + i * gw3
        rot(b, fx + gw3 / 2, top + alto + 30, f.upper(), c, size=13, anchor="middle")
        for j, par in enumerate(("B", "A")):
            bx = fx + gw3 / 2 - 90 + j * 110
            b.append(rect(bx, top + 6, 70, alto - 12, "white", r=4, stroke=LGRAY, sw=1.6, dash="5,5"))
            b.append(T(bx + 35, top + alto + 56, [f"parcela {par}"], 14, GRAY,
                       anchor="middle"))
    yy = top + alto + 76
    yy = frase_hueco(b, x0, yy, ww, "Las barras de la parcela B van hacia ________ ; las de la parcela A, hacia "
                                    "________ .", c)
    yy += 16
    yy = fila_letras(b, x0, yy, c, "¿De qué parcela habla cada opción? Escribe la parcela (A, B o C) antes de leer "
                                   "el «porque».")
    return ojo(b, x0, yy + 4, ww, "LA PREGUNTA ES SOBRE LA PARCELA B",
               "Una opción puede describir bien lo que pasó en otra parcela y aun así no responder. Primero, de "
               "quién habla; después, si lo que dice coincide con tus barras.")


# ───────── P9 · fertilizantes · agricultura sostenible ─────────
def i9(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El podio de las parcelas", c,
                      "Arma un podio por cada fila de la tabla: escribe la letra de la parcela que queda de primera, "
                      "de segunda y de tercera. Sostenible quiere decir fértil por mucho tiempo sin acabar con la "
                      "vida del suelo.")
    x0, ww = x + 22, w - 44
    criterios = ("MICROORGANISMOS POR GRAMO", "DESCOMPONEDORAS", "FIJADORAS DE NITRÓGENO")
    gap = 30
    pw = (ww - 2 * gap) / 3
    for k, cr in enumerate(criterios):
        px = x0 + k * (pw + gap)
        rot(b, px + pw / 2, yy + 22, cr, c, size=13, anchor="middle")
        base = yy + 290
        sw_ = (pw - 20) / 3
        for j, (puesto, hh) in enumerate(((2, 120), (1, 170), (3, 80))):
            bx_ = px + 10 + j * sw_
            caja(b, bx_, base - hh, sw_, hh, c, sw=2.2, r=4, fill=A["bg"] if puesto == 1 else "white")
            b.append(T(bx_ + sw_ / 2, base - hh + 36, [f"{puesto}.º"], 20, c, weight="700", anchor="middle"))
            b.append(f'<circle cx="{bx_ + sw_ / 2:.1f}" cy="{base - hh - 40}" r="28" fill="white" stroke="{c}" '
                     f'stroke-width="2.2"/>')
    yy += 312
    yy = frase_hueco(b, x0, yy, ww, "La parcela que sube a los tres podios es la ____ , y lo que la pone ahí "
                                    "es ______________________ .", c)
    yy += 16
    yy = ojo(b, x0, yy, ww, "¿LA TABLA MIDIÓ ESO?",
             "La tabla cuenta microorganismos. No cuenta tomates, ni la altura de las plantas, ni el precio. Si una "
             "opción concluye algo que la tabla no midió, no se alinea con los datos aunque suene bien.")
    return trampa(b, x0, yy + 14, ww, "Compara cada opción con tus podios:",
                  "si una opción dice que una parcela «tiene la mayor cantidad» de algo, busca esa parcela en el "
                  "podio de esa fila. Los números de la tabla deciden, no la palabra «equilibrada».", c)


# ───────── P10 · fertilizantes · cómo seguir la investigación ─────────
def i10(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La pregunta del estudio, palabra por palabra", c,
                      "Un buen criterio para seguir investigando responde exactamente la pregunta que se hicieron. "
                      "Desarma la pregunta en sus dos partes y pídele a cada opción que cumpla las dos.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 86, c, sw=2.4, r=16, fill=A["bg"])
    b.append(T(x0 + 24, yy + 36, ["«¿Cuál práctica es más beneficiosa"], 21, INK, style="italic"))
    t1 = "«¿Cuál práctica es más beneficiosa "
    w1 = tw(t1, 21, style="italic")
    b.append(T(x0 + 24 + w1, yy + 36, ["a largo plazo"], 21, c, weight="700", style="italic"))
    w2 = tw("a largo plazo", 21, "700", "italic")
    b.append(T(x0 + 24 + w1 + w2 + 6, yy + 36, ["para la"], 21, INK, style="italic"))
    w3 = tw("para la ", 21, style="italic")
    b.append(T(x0 + 24 + w1 + w2 + 6 + w3, yy + 36, ["salud del suelo"], 21, c, weight="700", style="italic"))
    b.append(T(x0 + 24 + w1 + w2 + 6 + w3 + tw("salud del suelo", 21, "700", "italic") + 1, yy + 36, ["?»"], 21,
               INK, style="italic"))
    letra(b, x0 + 24 + w1 + w2 / 2, yy + 66, "1", c, r=13, size=13)
    letra(b, x0 + 24 + w1 + w2 + 6 + w3 + tw("salud del suelo", 21, "700", "italic") / 2, yy + 66, "2", c, r=13,
          size=13)
    yy += 104
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("1 · «A LARGO PLAZO» ME EXIGE…", "¿un mes o varios ciclos de cultivo?"),
                                  ("2 · «LA SALUD DEL SUELO» SE MIDIÓ CON…", "mira qué contaron en la tabla"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 118, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        pista(b, px + 18, yy + 54, ps)
        renglon(b, px + 18, yy + 92, px + half - 18)
    yy += 140
    # tabla A–D × dos filtros (la única de la misión)
    b.append(T(x0, yy + 20, ["Pásale los dos filtros a cada opción:"], 18, INK, weight="700"))
    yy += 40
    colx = (x0 + 320, x0 + 640)
    rot(b, colx[0], yy + 18, "¿MIDE EL SUELO?", c, size=14, anchor="middle")
    rot(b, colx[1], yy + 18, "¿MIRA VARIOS CICLOS?", c, size=14, anchor="middle")
    for k, L in enumerate("ABCD"):
        ry = yy + 40 + k * 50
        letra(b, x0 + 40, ry + 18, L, c)
        for cxx in colx:
            for j, lab in enumerate(("sí", "no")):
                b.append(checkbox(cxx - 70 + j * 90, ry + 6, s=11, c=c))
                b.append(T(cxx - 42 + j * 90, ry + 24, [lab], 16, GRAY))
    rx = x0 + 820
    caja(b, rx, yy + 30, x0 + ww - rx, 200, c, r=14, dash="8,6")
    rot(b, rx + 18, yy + 58, "LA QUE PASA LOS DOS", c, size=14)
    pista(b, rx + 18, yy + 84, "y lo que mediría:")
    for j in range(3):
        renglon(b, rx + 18, yy + 126 + j * 36, x0 + ww - 18)
    return yy + 250


Q = {1: dict(n=1, est=3, pag=94, ctx="Calefacción del suelo · por qué baja la biomasa de la zona B",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=2, pag=95, ctx="Restauración del humedal · por qué volvieron las aves",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=4, pag=95, ctx="Restauración del humedal · aplicar el conocimiento ecológico",
             comp="Uso comprensivo del conocimiento científico", inst=i3),
     4: dict(n=4, est=3, pag=95, ctx="Restauración del humedal · la zona con poco oxígeno",
             comp="Explicación de fenómenos", inst=i4),
     5: dict(n=5, est=2, pag=96, ctx="Sabana del Casanare · se van los jaguares",
             comp="Explicación de fenómenos", inst=i5),
     6: dict(n=6, est=2, pag=96, ctx="Sabana del Casanare · vuelven los jaguares, el pasto no",
             comp="Explicación de fenómenos", inst=i6),
     7: dict(n=7, est=4, pag=96, ctx="Jornada de reciclaje · qué hacer con las pilas usadas",
             comp="Uso comprensivo del conocimiento científico", inst=i7),
     8: dict(n=8, est=1, pag=97, ctx="Fertilizantes en el tomate · lo que pasó en la parcela B",
             comp="Indagación", inst=i8),
     9: dict(n=9, est=1, pag=97, ctx="Fertilizantes en el tomate · cuál es sostenible",
             comp="Indagación", inst=i9),
     10: dict(n=10, est=4, pag=97, ctx="Fertilizantes en el tomate · cómo seguir el estudio",
              comp="Indagación", inst=i10)}


def build(pages=(154, 155, 157, 158, 159)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"bio3_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
