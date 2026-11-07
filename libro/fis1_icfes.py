#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 1 · entrenamiento ICFES · páginas 228 y 232.

Cuatro preguntas de Ciencias Naturales con contenido de mecánica clásica, de dos fuentes:
  · «Cuadernillo de preguntas · Prueba Ciencias Naturales · Saber 11.º» del Icfes (repo:
    fuente_icfes/22-diciembre-…-2025.pdf y 24-feb-…-2026.pdf; son las mismas 50 preguntas, con
    créditos distintos; el cuadernillo dice «utilizadas en aplicaciones anteriores»). Preguntas
    13, 17 y 43, verificadas contra el PDF.
  · ASED pre código 11 (Drive), capítulo 9 «Preguntas de Física», sección Mecánica clásica,
    ítem 13 (el ASED reinicia la numeración en cada sección). Solo se leyó el texto del PDF.
Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano, no copiadas del solucionario):

    QA · ASED Mecánica N.º 13 · C   (la fuerza que sostiene los paquetes es vertical y el
                                     desplazamiento horizontal: θ = 90°, W = F·d·cos 90° = 0)   estrategia 1
    QB · cuadernillo N.º 43 · D     (Ep alta al inicio, cero en t1 y t3, pico en t2, meseta en t4:
                                     caída, fondo, cima del rizo, fondo, tramo alto)            estrategia 2
    QC · cuadernillo N.º 13 · C     (tiempos distintos con la misma g → aceleraciones distintas →
                                     fuerzas netas distintas; altura, masa y forma no se variaron) estrategia 3
    QD · cuadernillo N.º 17 · D     (a los 20 m la banda de 30 m aún no se estira: solo hay caída
                                     libre, potencial gravitacional → cinética)                  estrategia 4

El solucionario del cuadernillo da 13·C, 17·D y 43·D: coincide.
Adaptaciones (registradas en fis1_icfes.csv): en el ASED N.º 13 «Kgf X m» se escribe «kgf × m»;
en la N.º 17 se omite la fotografía del puente (no hace falta para responder); en la N.º 43 la
gráfica y los cuatro modelos se redibujan con la misma forma.
"""
from fis1 import *   # noqa: F401,F403  (configura la misión y EST)
from fis1 import rot, caja, pista, texto, renglon, hueco, frase_hueco, flecha, marca, ejes, curva, punto


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · ASED Mecánica clásica N.º 13 · los paquetes ─────────
def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "La flecha de la mano y la flecha del camino", c,
                      "Como en la pregunta 9: una fuerza trabaja solo con la parte que va en la dirección del "
                      "movimiento. Dibuja las dos flechas y mide el ángulo entre ellas antes de hacer cuentas.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 420, 200, c, r=14)
    rot(b, x0 + 18, yy + 28, "DIBUJA AQUÍ", c, size=13)
    pista(b, x0 + 18, yy + 50, "la mano, el paquete y el camino", size=13)
    b.append(rect(x0 + 40, yy + 176, 340, 6, "#C9CED6", r=2))
    rx = x0 + 450
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 200, c, r=14)
    for j, (lab, w_) in enumerate((("la fuerza de la mano sobre el paquete apunta hacia", 170),
                                   ("el paquete se mueve hacia", 300),
                                   ("el ángulo entre las dos flechas es de", 120))):
        ry = yy + 44 + j * 50
        pista(b, rx + 18, ry, lab)
        renglon(b, rx + 18 + tw(lab, 15, style="italic") + 12, ry + 2, rx + rw - 18)
    texto(b, rx + 18, yy + 186, "la parte de la fuerza que va a lo largo del camino = ____ kgf  →  W = ____ × 200 m = ____", 16)
    return yy + 200


# ───────── QB · cuadernillo N.º 43 · la montaña rusa ─────────
def _carrito(b, cx, cy, lab, dx=0, dy=-26):
    b.append(rect(cx - 11, cy - 18, 22, 16, "white", r=3, stroke=INK, sw=2))
    b.append(T(cx + dx, cy + dy, [lab], 15, INK, style="italic", anchor="middle"))


def _modelo(b, x, y, k):
    """Los cuatro modelos de montaña rusa, cada uno en una caja de 280 × 150."""
    p = []
    if k == 0:      # A: baja a un valle y sube a una meseta
        for i in range(41):
            t = i / 40
            p.append((x + 20 + t * 240, y + 40 + 80 * math.exp(-((t - 0.45) / 0.18) ** 2) * (1 if t < 0.45 else 1)))
        p = [(px, py if px < x + 128 else max(py, y + 40)) for px, py in p]
        curva(b, p, INK, sw=2.6)
        for lab, t in (("t₁", 0.22), ("t₂", 0.45), ("t₃", 0.62), ("t₄", 0.85)):
            i = round(t * 40)
            _carrito(b, p[i][0], p[i][1], lab)
    elif k == 1:    # B: fondo plano y subida suave
        p = [(x + 20, y + 20), (x + 40, y + 120), (x + 150, y + 120)]
        for i in range(1, 21):
            t = i / 20
            p.append((x + 150 + t * 110, y + 120 - 50 * (1 - math.cos(math.pi * t)) / 2))
        curva(b, p, INK, sw=2.6)
        for lab, px in (("t₁", x + 70), ("t₂", x + 115)):
            _carrito(b, px, y + 120, lab)
        _carrito(b, p[10][0], p[10][1], "t₃")
        _carrito(b, p[19][0], p[19][1], "t₄")
    elif k == 2:    # C: colina
        for i in range(41):
            t = i / 40
            p.append((x + 20 + t * 240, y + 130 - 95 * math.exp(-((t - 0.35) / 0.2) ** 2) - (0 if t < 0.35 else -20 * (t - 0.35))))
        curva(b, p, INK, sw=2.6)
        for lab, t in (("t₁", 0.12), ("t₂", 0.35), ("t₃", 0.6), ("t₄", 0.85)):
            i = round(t * 40)
            _carrito(b, p[i][0], p[i][1], lab)
    else:           # D: caída, rizo y tramo alto
        p = [(x + 20, y + 10), (x + 40, y + 125), (x + 190, y + 125), (x + 215, y + 85), (x + 262, y + 85)]
        curva(b, p, INK, sw=2.6)
        b.append(f'<circle cx="{x + 120}" cy="{y + 92}" r="33" fill="none" stroke="{INK}" stroke-width="2.6"/>')
        _carrito(b, x + 68, y + 125, "t₁")
        b.append(rect(x + 109, y + 59, 22, 16, "white", r=3, stroke=INK, sw=2))
        b.append(T(x + 120, y + 50, ["t₂"], 15, INK, style="italic", anchor="middle"))
        _carrito(b, x + 170, y + 125, "t₃")
        _carrito(b, x + 245, y + 85, "t₄")


def datos_43(b, x, y, w):
    # la gráfica del estudiante
    gx, gy, gw, gh = x + 330, y + 30, 520, 150
    b.append(f'<line x1="{gx}" y1="{gy + gh}" x2="{gx + gw}" y2="{gy + gh}" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<line x1="{gx}" y1="{gy - 10}" x2="{gx}" y2="{gy + gh}" stroke="{INK}" stroke-width="2"/>')
    texto(b, gx - 12, gy + 4, "Energía potencial", 14, INK, weight="700", anchor="end")
    texto(b, gx + gw + 8, gy + gh + 5, "Tiempo", 14, INK, anchor="start")
    pts = []
    for i in range(121):
        t = i / 120
        if t < 0.2:
            e = 0.95 * (1 + math.cos(math.pi * t / 0.2)) / 2
        elif t < 0.65:
            e = 0.42 * math.exp(-((t - 0.45) / 0.05) ** 2)
        else:
            e = 0.38 * (1 - math.cos(math.pi * min(1, (t - 0.67) / 0.13))) / 2 if t > 0.67 else 0
        pts.append((gx + 6 + t * (gw - 20), gy + gh - e * gh))
    curva(b, pts, INK, sw=2.8)
    for lab, t in (("t₁", 0.2), ("t₂", 0.45), ("t₃", 0.67), ("t₄", 0.82)):
        xx = gx + 6 + t * (gw - 20)
        b.append(f'<line x1="{xx:.0f}" y1="{gy + 20}" x2="{xx:.0f}" y2="{gy + gh + 6}" stroke="{GRAY}" stroke-width="1.4" stroke-dasharray="5,4"/>')
        b.append(T(xx, gy + gh + 26, [lab], 15, INK, style="italic", anchor="middle"))
    yy = pregunta(b, x, gy + gh + 30, w, "De los siguientes modelos de montaña rusa, ¿cuál explica la gráfica obtenida por "
                                         "el estudiante?")
    for k in range(4):
        mx = x + k * 312
        texto(b, mx + 4, yy + 26, "ABCD"[k] + ".", 18, INK, weight="700")
        _modelo(b, mx + 24, yy + 14, k)
    return yy + 170


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Energía potencial alta, carrito arriba", c,
                      "La energía potencial gravitacional crece con la altura. Lee en la gráfica cómo está en cada "
                      "instante y tradúcelo a dónde tiene que estar el carrito. Después busca el modelo que cumple las "
                      "cuatro casillas.")
    x0, ww = x + 22, w - 44
    n, gap = 4, 16
    bw = (ww - gap * (n - 1)) / n
    for k, t in enumerate(("t₁", "t₂", "t₃", "t₄")):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 92, c, r=12)
        rot(b, bx + 16, yy + 24, f"EN {t}", c, size=13)
        pista(b, bx + 16, yy + 50, "energía: ______________", size=14)
        pista(b, bx + 16, yy + 78, "el carrito está: ________", size=14)
    return yy + 92


# ───────── QC · cuadernillo N.º 13 · tres objetos que caen ─────────
def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Lo que Juan movió y lo que dejó quieto", c,
                      "Como con el bailarín: una pregunta se puede contestar con un experimento solo si lo que ella "
                      "pregunta es justo lo que se cambió o lo que se midió. Llena la ficha y después pasa cada pregunta "
                      "por ella.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 18
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("LO QUE CAMBIÓ", "de un objeto a otro"), ("LO QUE SE MANTUVO", "igual para los tres"),
                                  ("LO QUE OBSERVÓ", "y lo que eso dice de la aceleración"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 128, c, r=12)
        rot(b, bx + 16, yy + 26, rt, c, size=13)
        pista(b, bx + 16, yy + 48, ps, size=13)
        renglon(b, bx + 16, yy + 84, bx + bw - 16)
        renglon(b, bx + 16, yy + 116, bx + bw - 16)
    return yy + 128


# ───────── QD · cuadernillo N.º 17 · el salto bungee ─────────
def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "La regla del puente: ¿ya se estiró la banda?", c,
                      "Igual que con el ciclista: la energía no se pierde, cambia de forma. Marca en la regla el punto "
                      "donde la banda empieza a estirarse y el punto donde va el deportista. Después escribe qué "
                      "energía baja y cuál sube en ese tramo.")
    x0, ww = x + 22, w - 44
    sx, sy, sh = x0 + 80, yy + 10, 230
    b.append(f'<line x1="{sx}" y1="{sy}" x2="{sx}" y2="{sy + sh}" stroke="{INK}" stroke-width="2.4"/>')
    for m in range(0, 66, 5):
        ty = sy + m / 65 * sh
        b.append(f'<line x1="{sx - (12 if m % 10 == 0 else 6)}" y1="{ty:.0f}" x2="{sx}" y2="{ty:.0f}" stroke="{INK}" stroke-width="1.6"/>')
        if m % 10 == 0:
            b.append(T(sx - 18, ty + 5, [f"{m} m"], 13, GRAY, anchor="end"))
    texto(b, sx + 14, sy + 6, "puente", 14, GRAY)
    texto(b, sx + 14, sy + sh + 4, "fondo (65 m abajo)", 14, GRAY)
    pista(b, sx + 14, sy + 110, "marca aquí los dos puntos", size=13)
    rx = x0 + 400
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 240, c, r=14)
    rot(b, rx + 18, yy + 30, "EN LOS PRIMEROS 20 m", c, size=14)
    for j, lab in enumerate(("la banda empieza a estirarse a los ____ m de caída; a los 20 m está",
                             "la energía que baja es la",
                             "la energía que sube es la",
                             "¿todavía falta otra transformación más abajo? ¿cuál?")):
        ry = yy + 74 + j * 44
        pista(b, rx + 18, ry, lab)
        renglon(b, rx + 18 + tw(lab, 15, style="italic") + 12, ry + 2, rx + rw - 18)
    return yy + 240


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="Una persona sale del supermercado con dos paquetes que pesan 5 kgf, uno en cada mano. Para llegar a su "
            "casa debe recorrer 2 cuadras de 100 metros cada una. El trayecto recorrido por la persona es "
            "completamente horizontal, lo hace sin detenerse y llega en 2 minutos a su casa. Sobre el trabajo "
            "mecánico en kgf × m realizado, podemos afirmar que",
          o=["tiene un valor de 2000 kgf × m ya que el trabajo es fuerza × distancia.",
             "es indeterminable porque el trabajo siempre se realiza contra la gravedad.",
             "es nulo porque la fuerza para sostener los paquetes no es en la dirección del movimiento.",
             "su valor numérico es de 500 kgf × m por cada paquete."],
          inst=ii1)
QB = dict(est=2, comp="Uso comprensivo del conocimiento científico",
          e="Un estudiante calculó la energía potencial de un vagón en una montaña rusa. La gráfica representa los "
            "datos obtenidos por el estudiante.",
          o=["El modelo A.", "El modelo B.", "El modelo C.", "El modelo D."],
          datos=datos_43, inst=ii2)
QC = dict(est=3, comp="Indagación",
          e="El profesor de Juan le entrega tres objetos de igual volumen y forma, pero de diferente material, y le "
            "pide que los deje caer desde la altura de sus hombros y observe el tiempo de caída al suelo, de cada uno "
            "de ellos. Juan observa que los tres tardan tiempos diferentes para llegar al suelo, a pesar de que los "
            "tres están sometidos a la misma aceleración gravitacional. Teniendo en cuenta la información anterior, "
            "¿cuál de las siguientes preguntas se puede contestar a partir de las observaciones que realizó Juan?",
          o=["¿El tiempo de caída de los objetos depende de la altura de lanzamiento?",
             "¿La fuerza gravitacional es proporcional a la masa de los objetos?",
             "¿La fuerza neta que actúa sobre cada uno de los objetos es diferente?",
             "¿La forma de los objetos está relacionada con diferencias en la fuerza de fricción?"],
          inst=ii3)
QD = dict(est=4, comp="Uso comprensivo del conocimiento científico",
          e="El salto bungee es un deporte que se practica generalmente en puentes. En uno de estos saltos, el "
            "deportista se lanzará desde un puente de 65 metros de altura, utilizando una banda elástica que tiene "
            "una longitud sin estirar de 30 metros y que puede estirarse 30 metros más. Cuando el deportista ha "
            "descendido apenas 20 metros de altura, ¿cuál de las siguientes transformaciones de energía se habrá "
            "dado?",
          o=["De energía cinética a potencial elástica.", "De energía cinética a potencial gravitacional.",
             "De energía potencial gravitacional a potencial elástica.",
             "De energía potencial gravitacional a cinética."],
          inst=ii4)


def build(pages=(228, 232)):
    return [hoja_icfes("fis1_i1", pages[0], QA, QB),
            hoja_icfes("fis1_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
