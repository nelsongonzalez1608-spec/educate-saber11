#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 3 · entrenamiento ICFES · páginas 242 y 246.

Fuentes, verificadas contra la página del cuadernillo:
  · «Cuadernillo de preguntas · Prueba Ciencias Naturales · Saber 11.°» del Icfes (noviembre de
    2025, reeditado en febrero de 2026 con las mismas 50 preguntas: fuente_icfes/22-diciembre-…
    y fuente_icfes/24-feb-…). Preguntas 31 (p. 23), 42 (p. 29) y 19 (p. 16).
  · Cuadernillo Saber 11 2016-1, 2.ª sesión, cuadernillo ABD (encabezado «Saber 11 - 083 - B10O -
    ABD · 2a. sesión»; Drive «1. CUADERNILLOS ICFES» / «2016-2 SEGUNDA SESION.pdf», que en la
    portada dice 2016-1 segunda sesión), Ciencias Naturales, ítem 72 (p. 23).
La pregunta 19 del cuadernillo 2025 es la misma 69 de 2016-1 2.ª sesión (no usar las dos).
Ninguna estaba en tablero/icfes.csv; las cuatro se reservaron en
tablero/propuestas/fis_icfes_reservas.csv. Ninguna nombra a un político. La gráfica de la 31, el
triángulo y las cuatro figuras de la 42, las cinco figuras de campo de la 72 (redibujadas con
líneas de campo calculadas para dos cargas de signo contrario) y las esferas de la 19 se
redibujaron con los mismos datos.

Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11» (el motor lo impone).

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · cuadernillo 2025 N.º 31 · B   (la menor corriente a 90 °C: la mayor R a 90 °C)  estrategia 1
    QB · cuadernillo 2025 N.º 42 · A   (fuerzas de 2 y 3 sobre 1)                        estrategia 2
    QC · 2016-1 2.ª ses. N.º 72  · A   (hacia dónde se mueve la carga −q)                estrategia 3
    QD · cuadernillo 2025 N.º 19 · A   (esferas +Q y neutra en contacto)                 estrategia 4

Cuentas:
  QA · Lecturas de la gráfica (Ω): R₁ 3 · 3,5 · 4 · 4,5 · 5 (sube recta); R₂ 2 · 2,2 · 2,8 · 3,8 · 5
       (sube cada vez más rápido); R₃ 5 · 4 · 2,8 · 2,2 · 2 (baja); R₄ 4 constante, de 0 a 80 °C.
       A 90 °C, siguiendo la tendencia: R₁ ≈ 5,25; R₂ ≈ 5,7 o más; R₃ ≈ 2; R₄ = 4. I = V/R: la menor
       corriente va con la mayor R a 90 °C → R₂ → B. A y C justifican con el rango 40–80 °C (no con
       90 °C); D da una razón cierta de R₄ que no responde la pregunta.
  QB · 1 y 2 positivas: se repelen → la fuerza de 2 sobre 1 apunta en la línea 2→1, alejándose de 2
       (arriba a la derecha). 1 positiva y 3 negativa: se atraen → la fuerza de 3 sobre 1 apunta hacia 3
       (abajo a la derecha) → A. B pone las dos al revés; C pone repulsión con 3; D atracción con 2.
  QC · El campo en el punto de −q es tangente a la línea, en el sentido de sus flechas (sale de + y va
       a −). Carga negativa: F = qE va en sentido CONTRARIO al campo → a lo largo de la línea, de
       regreso hacia la esfera positiva → A. B va a favor del campo (sería una carga positiva); C y D
       son perpendiculares a la línea.
  QD · En un metal solo se mueven los electrones. La esfera 2 era neutra y quedó + Q/2: perdió
       electrones; la 1 pasó de + Q a + Q/2: ganó electrones → los electrones pasaron de la 2 a la 1
       → A. B y D mueven protones; C da el sentido contrario.
"""
from fis3 import *   # noqa: F401,F403  (configura la misión y EST)
from fis3 import rot, caja, pista, renglon, frase_hueco, letra, casillas, flecha, carga, txt_izq


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 8, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · N.º 31 · resistencia contra temperatura ─────────
SERIES = (("R₁", ((0, 3), (20, 3.5), (40, 4), (60, 4.5), (80, 5)), "tri", "#7A7F8A", None),
          ("R₂", ((0, 2), (20, 2.2), (40, 2.8), (60, 3.8), (80, 5)), "rombo", INK, None),
          ("R₃", ((0, 5), (20, 4), (40, 2.8), (60, 2.2), (80, 2)), "equis", "#4A4F5A", "7,5"),
          ("R₄", ((0, 4), (20, 4), (40, 4), (60, 4), (80, 4)), "cuadro", "#9AA0AA", None))


def _marca(b, px, py, tipo, c):
    if tipo == "tri":
        b.append(f'<polygon points="{px},{py - 8} {px + 8},{py + 6} {px - 8},{py + 6}" fill="{c}"/>')
    elif tipo == "rombo":
        b.append(f'<polygon points="{px},{py - 8} {px + 8},{py} {px},{py + 8} {px - 8},{py}" fill="{c}"/>')
    elif tipo == "equis":
        b.append(line(px - 7, py - 7, px + 7, py + 7, c, 3))
        b.append(line(px - 7, py + 7, px + 7, py - 7, c, 3))
    else:
        b.append(rect(px - 7, py - 7, 14, 14, c, r=0))


def datos_31(b, x, y, w):
    gx, gy, gw, gh = x + 110, y + 14, 600, 150
    for v in range(0, 7):
        py = gy + gh - v / 6 * gh
        b.append(line(gx, py, gx + gw, py, LGRAY, 1.2, dash="4,6"))
        b.append(T(gx - 12, py + 5, [str(v)], 14, INK, anchor="end"))
    for t in range(0, 101, 10):
        px = gx + t / 100 * gw
        b.append(T(px, gy + gh + 22, [str(t)], 14, INK, anchor="middle"))
    b.append(line(gx, gy + gh, gx + gw + 10, gy + gh, INK, 2.2))
    b.append(line(gx, gy - 10, gx, gy + gh, INK, 2.2))
    for nom, pts, tipo, c, dash in SERIES:
        P = [(gx + t / 100 * gw, gy + gh - v / 6 * gh) for t, v in pts]
        b.append(f'<polyline points="{" ".join(f"{a:.1f},{c_:.1f}" for a, c_ in P)}" fill="none" stroke="{c}" '
                 f'stroke-width="3"' + (f' stroke-dasharray="{dash}"' if dash else "") + '/>')
        for px, py in P:
            _marca(b, px, py, tipo, c)
    b.append(T(gx + gw / 2, gy + gh + 48, ["Temperatura (°C)"], 15, INK, weight="700", anchor="middle"))
    b.append(T(gx - 52, gy + gh / 2, ["Resistencia (Ω)"], 15, INK, weight="700", anchor="middle", rot=-90))
    lx, ly = gx + gw + 60, gy + 0
    b.append(rect(lx, ly - 10, 150, 160, "white", r=0, stroke=INK, sw=1.6))
    for k, (nom, pts, tipo, c, dash) in enumerate(SERIES):
        yy = ly + 20 + k * 36
        b.append(line(lx + 16, yy, lx + 66, yy, c, 3, dash=dash))
        _marca(b, lx + 41, yy, tipo, c)
        b.append(T(lx + 84, yy + 7, [nom], 18, INK))
    return pregunta(b, x, gy + gh + 60, w,
                    "Un estudiante realiza actividades experimentales y encuentra que la corriente eléctrica en un "
                    "circuito es inversamente proporcional a la resistencia eléctrica. Se le solicita al estudiante "
                    "construir un circuito usando una de estas resistencias, de forma que pase la menor cantidad de "
                    "corriente eléctrica a 90 °C. Si las tendencias de resistencia como función de la temperatura se "
                    "mantienen, ¿cuál resistencia se debe utilizar?")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "El dato que decide está a 90 °C", c,
                      "La pregunta habla de 90 °C y la gráfica llega a 80 °C: lee cada resistencia en 80 °C, mira "
                      "hacia dónde va y estima su valor a 90 °C.")
    x0, ww = x + 22, w - 44
    cols = (("", 120), ("A 80 °C (Ω)", 200), ("¿HACIA DÓNDE VA?", 420), ("A 90 °C, MÁS O MENOS (Ω)", ww - 740))
    px = x0
    for t, cw in cols:
        caja(b, px, yy, cw, 36, c, r=0, fill=A["bg"])
        if t:
            rot(b, px + cw / 2, yy + 24, t, c, size=13, anchor="middle")
        px += cw
    for k, (nom, *_r) in enumerate(SERIES):
        ry = yy + 36 + k * 38
        px = x0
        for j, (t, cw) in enumerate(cols):
            caja(b, px, ry, cw, 38, c, r=0)
            if j == 0:
                b.append(T(px + cw / 2, ry + 27, [nom], 18, INK, weight="700", anchor="middle"))
            elif j == 2:
                casillas(b, px + 20, ry + 9, ("sube", "baja", "igual"), c, paso=130, size=15)
            px += cw
    yy += 36 + 4 * 38 + 12
    return frase_hueco(b, x0, yy, ww, "Menos corriente pide más __________ ; a 90 °C la más grande es ______ .", c)


# ───────── QB · N.º 42 · fuerzas de 2 y 3 sobre 1 ─────────
def _tri(b, cx, top, s, flechas=None, nombres=True):
    """Triángulo de cargas: 1 arriba (+), 2 abajo izquierda (+), 3 abajo derecha (−)."""
    p1, p2, p3 = (cx, top), (cx - 0.58 * s, top + s), (cx + 0.58 * s, top + s)
    if flechas is None:
        b.append(f'<polygon points="{p1[0]},{p1[1]} {p2[0]},{p2[1]} {p3[0]},{p3[1]}" fill="none" stroke="{INK}" '
                 f'stroke-width="2.4"/>')
    else:
        for q in (p2, p3):
            b.append(line(p1[0], p1[1], q[0], q[1], GRAY, 1.6, dash="6,5"))
    for (px, py), sg, n, dx in ((p1, "+", "1", 0), (p2, "+", "2", -30), (p3, "-", "3", 30)):
        carga(b, px, py, sg, r=13)
        if nombres:
            b.append(T(px + dx, py - 20 if n == "1" else py + 6, [n], 16, INK, weight="700", anchor="middle"))
    if flechas:
        L = 0.46 * s
        for (q, haciaq, lab) in flechas:
            ux, uy = q[0] - p1[0], q[1] - p1[1]
            d = math.hypot(ux, uy)
            ux, uy = ux / d, uy / d
            sg = 1 if haciaq else -1
            ex, ey = p1[0] + sg * ux * L, p1[1] + sg * uy * L
            flecha(b, p1[0] + sg * ux * 15, p1[1] + sg * uy * 15, ex, ey, INK, sw=2.6, head=10)
            b.append(T(ex + (24 if ex > p1[0] else -24), ey + (16 if ey > p1[1] else -10), lab, 14, INK,
                       weight="700", anchor="start" if ex > p1[0] else "end", lh=16))
    return p1, p2, p3


def datos_42(b, x, y, w):
    _tri(b, x + w / 2, y + 30, 105)
    yy = pregunta(b, x, y + 150, w, "¿Cuál de las siguientes figuras muestra la fuerza eléctrica que ejercen la carga 2 "
                                    "y la carga 3 sobre la carga 1?")
    c = A["color"]
    ow = (w - 30) / 4
    s = 112
    for k, L in enumerate("ABCD"):
        ox = x + k * (ow + 10)
        cx = ox + ow / 2 + 18
        top = yy + 84
        p1, p2, p3 = (cx, top), (cx - 0.58 * s, top + s), (cx + 0.58 * s, top + s)
        f2 = ["Fuerza de", "2 sobre 1"]
        f3 = ["Fuerza de", "3 sobre 1"]
        conf = {"A": ((p2, False, f2), (p3, True, f3)), "B": ((p2, True, f2), (p3, False, f3)),
                "C": ((p2, False, f2), (p3, False, f3)), "D": ((p2, True, f2), (p3, True, f3))}[L]
        letra(b, ox + 18, yy + 22, L, c)
        _tri(b, cx, top, s, flechas=conf, nombres=False)
    return yy + 84 + s + 22


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Una flecha por cada carga vecina", c,
                      "Lo de las dos cargas del avión: dibuja antes de elegir. Decide cada fuerza por separado: "
                      "primero los signos, después si se atraen o se repelen, y solo entonces hacia dónde apunta "
                      "la flecha que sale de la carga 1.")
    x0, ww = x + 22, w - 44
    pw = (ww - 24) / 2
    for k, (rt, otra) in enumerate((("LA CARGA 2 SOBRE LA 1", "2"), ("LA CARGA 3 SOBRE LA 1", "3"))):
        px = x0 + k * (pw + 24)
        caja(b, px, yy, pw, 150, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        b.append(T(px + 18, yy + 66, [f"Signos: 1 es ____ y {otra} es ____ →"], 17, INK))
        casillas(b, px + 330, yy + 50, ("se atraen", "se repelen"), c, paso=130, size=15)
        b.append(T(px + 18, yy + 116, [f"La flecha sobre 1 apunta"], 17, INK))
        casillas(b, px + 220, yy + 100, (f"hacia {otra}", f"lejos de {otra}"), c, paso=130, size=15)
    return yy + 166


# ───────── QC · N.º 72 · la carga −q en el campo ─────────
def _lineas_dipolo(d, n=10, paso=3.0, caja_=(-150, -130, 150, 130)):
    """Líneas de campo de +1 en (−d, 0) y −1 en (d, 0) (coordenadas con y hacia abajo)."""
    lineas = []
    for k in range(n):
        ang = math.pi * 2 * (k + 0.5) / n
        x, y = -d + 9 * math.cos(ang), 9 * math.sin(ang)
        pts = [(x, y)]
        for _ in range(900):
            r1 = math.hypot(x + d, y) or 1e-6
            r2 = math.hypot(x - d, y) or 1e-6
            ex = (x + d) / r1 ** 3 - (x - d) / r2 ** 3
            ey = y / r1 ** 3 - y / r2 ** 3
            m = math.hypot(ex, ey)
            x, y = x + paso * ex / m, y + paso * ey / m
            if not (caja_[0] <= x <= caja_[2] and caja_[1] <= y <= caja_[3]) or r2 < 9:
                break
            pts.append((x, y))
        lineas.append(pts)
    return lineas


LINEAS = _lineas_dipolo(55, n=12)
# La carga −q: sobre la línea que sale de + hacia arriba (la 7.ª), a unos pasos de la esfera.
_L = LINEAS[9]
QX, QY = _L[16]
_tx, _ty = _L[18][0] - _L[14][0], _L[18][1] - _L[14][1]
_tm = math.hypot(_tx, _ty)
TX, TY = _tx / _tm, _ty / _tm        # sentido del campo en el punto de −q


def _dipolo(b, cx, cy, s, flecha_q=None):
    for pts in LINEAS:
        P = [(cx + s * a, cy + s * c_) for a, c_ in pts]
        b.append(f'<polyline points="{" ".join(f"{a:.1f},{c_:.1f}" for a, c_ in P)}" fill="none" stroke="{GRAY}" '
                 f'stroke-width="1.6"/>')
        if len(P) > 30:
            i = len(P) // 2
            (ax, ay), (bx, by) = P[i - 3], P[i + 3]
            flecha(b, ax, ay, bx, by, GRAY, sw=1.6, head=7)
    carga(b, cx - 55 * s, cy, "+", r=12)
    carga(b, cx + 55 * s, cy, "-", r=12)
    qx, qy = cx + s * QX, cy + s * QY
    b.append(f'<circle cx="{qx:.1f}" cy="{qy:.1f}" r="7" fill="{INK}"/>')
    if flecha_q and flecha_q[0] < -0.3:       # la flecha va a la izquierda: el rótulo, a la derecha
        b.append(rect(qx + 12, qy - 30, 26, 20, "white", r=4))
        b.append(T(qx + 14, qy - 14, ["−q"], 15, INK, weight="700"))
    else:
        b.append(rect(qx - 38, qy - 30, 26, 20, "white", r=4))
        b.append(T(qx - 14, qy - 14, ["−q"], 15, INK, weight="700", anchor="end"))
    if flecha_q:
        ux, uy = flecha_q
        flecha(b, qx, qy, qx + 38 * ux, qy + 38 * uy, INK, sw=3.2, head=11)
    b.append(T(cx, cy + 130 * s + 8, ["E"], 16, INK, weight="700", style="italic", anchor="middle"))


def datos_72(b, x, y, w):
    _dipolo(b, x + w / 2, y + 110, 0.78)
    yy = pregunta(b, x, y + 222, w, "De acuerdo con la información anterior, ¿cuál de las siguientes figuras muestra la "
                                    "dirección en la que se moverá la carga −q al ser liberada desde el reposo?")
    c = A["color"]
    ow = (w - 30) / 4
    dirs = {"A": (-TX, -TY), "B": (TX, TY), "C": (-TY, TX), "D": (TY, -TX)}
    for k, L in enumerate("ABCD"):
        ox = x + k * (ow + 10)
        letra(b, ox + 18, yy + 22, L, c)
        _dipolo(b, ox + ow / 2 + 10, yy + 108, 0.74, flecha_q=dirs[L])
    return yy + 108 + 0.74 * 130 + 26


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "El campo empuja a lo positivo; a lo negativo, al revés", c,
                      "Lo de la carga de prueba en el ala: primero el sentido del campo en el punto, después el "
                      "signo de la carga. Dibuja con lápiz la flecha de E en el punto de −q, en la figura de arriba.")
    x0, ww = x + 22, w - 44
    pasos = (("1 · En el punto de −q, el campo apunta", ("hacia la esfera +", "alejándose de la esfera +")),
             ("2 · La carga es negativa: la fuerza va", ("a favor del campo", "contra el campo")),
             ("3 · Entonces −q se mueve", ("hacia la esfera +", "alejándose de la esfera +")))
    for k, (rt, ops) in enumerate(pasos):
        ry = yy + k * 50
        b.append(T(x0, ry + 24, [rt], 17, c, weight="700"))
        casillas(b, x0 + 400, ry + 8, ops, c, paso=280, size=16)
    return yy + 3 * 50


# ───────── QD · N.º 19 · esferas en contacto ─────────
def _esfera(b, cx, cy, n, signos):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="34" fill="#C9CED6" stroke="{INK}" stroke-width="2"/>')
    b.append(T(cx, cy + 7, [n], 18, INK, weight="700", anchor="middle"))
    for k in range(signos):
        a = 2 * math.pi * k / max(signos, 1) - math.pi / 2
        b.append(T(cx + 52 * math.cos(a), cy + 52 * math.sin(a) + 6, ["+"], 18, INK, weight="700", anchor="middle"))


def datos_19(b, x, y, w):
    yy = y + 8
    for k, (t, s1, s2, q1, q2) in enumerate((("Antes del contacto", 8, 0, "+ Q", ""),
                                             ("Después del contacto", 4, 4, "+ Q/2", "+ Q/2"))):
        bx = x + 110 + k * 600
        b.append(T(bx + 120, yy + 20, [t], 17, INK, weight="700", anchor="middle"))
        _esfera(b, bx + 50, yy + 110, "1", s1)
        _esfera(b, bx + 200, yy + 110, "2", s2)
        b.append(T(bx + 50, yy + 46, [q1], 17, INK, style="italic", anchor="middle"))
        if q2:
            b.append(T(bx + 200, yy + 46, [q2], 17, INK, style="italic", anchor="middle"))
    return pregunta(b, x, yy + 180, w, "Con base en la información anterior, ¿qué sucedió al poner las esferas en contacto?")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Quién se mueve en un metal", c,
                      "Lo de las agujas: del modelo al mecanismo. El texto del principio te da la regla; úsala para "
                      "decir qué le pasó a cada esfera por dentro, antes de mirar las opciones.")
    x0, ww = x + 22, w - 44
    b.append(T(x0, yy + 22, ["En un metal, las partículas que pueden pasar de un cuerpo a otro son los"], 17, INK))
    renglon(b, x0 + 590, yy + 26, x0 + 800)
    yy += 44
    for k, (rt, f) in enumerate((("ESFERA 2", "de neutra a + Q/2: ¿ganó o perdió electrones?"),
                                 ("ESFERA 1", "de + Q a + Q/2: ¿ganó o perdió electrones?"))):
        ry = yy + k * 44
        rot(b, x0, ry + 24, rt, c, size=14)
        b.append(T(x0 + 120, ry + 24, [f], 17, INK))
        casillas(b, x0 + 620, ry + 8, ("ganó", "perdió"), c, paso=120, size=16)
    return yy + 2 * 44


QA = dict(est=1, comp="Indagación",
          e="La siguiente gráfica muestra la relación entre la resistencia eléctrica y la temperatura para cuatro "
            "resistencias eléctricas (R₁, R₂, R₃ y R₄).",
          o=["R₁, porque tiene la mayor resistencia eléctrica desde los 40 °C hasta los 80 °C.",
             "R₂, porque su resistencia eléctrica será la mayor a 90 °C.",
             "R₃, porque tiene la menor resistencia desde los 40 °C hasta los 80 °C.",
             "R₄, porque su resistencia eléctrica no depende de la temperatura."],
          datos=datos_31, inst=ii1)
QB = dict(est=2, comp="Uso comprensivo del conocimiento científico",
          e="De la ley de Coulomb se sabe que la fuerza eléctrica debido a la interacción entre cargas de signos "
            "iguales es repulsiva y entre cargas de signos opuestos es atractiva. La siguiente figura muestra un "
            "sistema conformado por tres cargas eléctricas.",
          o=[], datos=datos_42, inst=ii2)
QC = dict(est=3, comp="Explicación de fenómenos",
          e="En la figura se muestra un campo eléctrico E, generado por dos esferas cargadas; en el interior del "
            "campo eléctrico se coloca una carga negativa −q, tal como se muestra en la figura.",
          o=[], datos=datos_72, inst=ii3)
QD = dict(est=4, comp="Explicación de fenómenos",
          e="En un metal que pierde electrones, la cantidad de protones es mayor que la de electrones y, por tanto, "
            "la carga total es positiva y se representa con signos +. Se tienen dos esferas metálicas idénticas: "
            "una esfera (1) inicialmente con carga + Q y otra esfera (2) inicialmente neutra. Al ponerlas en "
            "contacto y luego separarlas, se observa que las dos esferas quedan con cargas iguales + Q/2, como "
            "muestra la figura.",
          o=["De la esfera 2 pasaron electrones hacia la esfera 1.",
             "De la esfera 2 pasaron protones hacia la esfera 1.",
             "De la esfera 1 pasaron electrones hacia la esfera 2.",
             "De la esfera 1 pasaron protones hacia la esfera 2."],
          datos=datos_19, inst=ii4)


def build(pages=(242, 246)):
    return [hoja_icfes("fis3_i1", pages[0], QA, QB),
            hoja_icfes("fis3_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
