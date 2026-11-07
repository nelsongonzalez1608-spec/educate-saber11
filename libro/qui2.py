#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 2 · componente químico · aspectos fisicoquímicos de sustancias · páginas 190–196.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 2» de Química (fuente_libro/QUÍMICA), páginas 150–152.
Casos: dos sólidos X y Y que se funden (1), parafina en un incendio (2), tanque de propano al sol
(3), grasa vegetal en bandeja metálica y en baño de agua (4 a 6), hielo seco (7), matraz con un
sólido orgánico y termómetro (8), esfera metálica sobre mercurio (9 y 10).

Claves verificadas (resueltas a mano contra el texto y las figuras del libro, 7 nov 2026):

    1·B  2·A  3·B  4·B  5·C  6·D  7·B  8·A  9·D  10·A

Cuentas y razones:
  1 · Y tiene que llegar a una temperatura de fusión mayor: más calor sensible antes de fundirse (B).
      A (menor calor específico → absorbe menos y tardaría menos) y D (menor calor latente → se
      fundiría antes) se contradicen solas; C no tiene dato. Ver hallazgo: la gráfica pone la
      meseta de Y en 200 °C y el texto dice 160 °C.
  2 · Q₁ = m·c·ΔT = 40 g × 2,1 J/(g·°C) × (60 − 30) °C = 2 520 J;  Q₂ = m·L = 40 g × 200 J/g = 8 000 J;
      total = 10 520 J (A).
  3 · Volumen fijo, más temperatura → más energía cinética → choques más frecuentes y más fuertes (B).
  4 · Primero calor sensible hasta 45 °C (100 × 2,0 × 20 = 4 000 J) y después calor latente
      (100 × 180 = 18 000 J) para separar las partículas: 22 000 J (B).
  5 · El agua rodea el bloque: el calor entra por todas las caras (C). D es falsa: el calor que
      necesita el bloque es el mismo con cualquier método.
  6 · El baño está a 80 °C, 35 °C por encima del punto de fusión, por todos lados y sin parar (D).
  7 · Sólido → gas sin pasar por líquido: sublimación (B).
  8 · Meseta de temperatura = cambio de fase: el calor que entra es calor latente (A).
  9 · Un metal como el acero (≈ 7,9 g/cm³) es menos denso que el mercurio (13,6 g/cm³): el empuje
      supera al peso (D). B (tensión superficial) no explica que flote una esfera entera.
 10 · De las cuatro, solo A nombra una propiedad real del mercurio que influya en la rapidez
      (poca resistencia al movimiento). Ver hallazgo: la causa de que suba es el empuje, que no
      está entre las opciones.

Reparto: A 3 · B 4 · C 1 · D 2. Sin concentración grave; C aparece una sola vez.
Hallazgos (la gráfica de la 1 contradice el texto; la curva de presión de la 3 sube mucho más de lo
que predice la ley de los gases; la 10 no ofrece la causa principal; «200 mL de un sólido»; la
opción A de la 5 habla de «aire caliente» en un método de bandeja; la 9 remite a un video):
tablero/propuestas/qui2_hallazgos.csv.

Estrategias:
    1 · Donde la temperatura se queda quieta   (1, 7, 8    · ICFES Sim. II 2023 N.º 67) azul
    2 · El calor, tramo por tramo              (2, 4       · ICFES 1.ª ses. N.º 112)   rojo
    3 · Lo explican los choques de partículas  (3, 5, 6    · ICFES 2.ª ses. N.º 76)    oro
    4 · Más denso abajo, menos denso arriba    (9, 10      · ICFES Sim. II 2023 N.º 64) morado

Hojas: 190 qui2_t1 (1-2) · 191 qui2_t2 (3-4) · 192 qui2_i1 · 193 qui2_t3 (5-6) ·
       194 qui2_t4 (7-8) · 195 qui2_t5 (9-10) · 196 qui2_i2.
"""
import random

import re

from taller_base import *

configurar("Química", 2, "químico · aspectos fisicoquímicos de sustancias",
           tema="El calor, los cambios de estado y la densidad",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Donde la temperatura se queda quieta", EDU_AZUL),
       2: ("El calor, tramo por tramo", EDU_ROJO),
       3: ("Lo explican los choques de partículas", EDU_ORO),
       4: ("Más denso abajo, menos denso arriba", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))
AGUA = "#EAF4FA"
CALIENTE = "#FCE9DD"       # relleno de lo que está caliente
VIDRIO = "#7C8A99"


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def _esp(txt):
    """SVG junta los espacios repetidos: los que separan bloques se vuelven espacios duros."""
    return re.sub(r" {2,}", lambda m: "\u00a0" * len(m.group()), txt)


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [_esp(txt)], size, GRAY, style="italic", anchor=anchor))


def texto(b, x, y, txt, size=17, color=INK, weight="400", anchor="start"):
    b.append(T(x, y, [_esp(txt)], size, color, weight=weight, anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def hueco(b, x, y, w=90, h=40, c=GRAY):
    b.append(rect(x, y, w, h, "white", r=8, stroke=c, sw=1.8))
    return x + w


def frase_hueco(b, x, y, w, txt, c, h=56):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [_esp(txt)], 18, INK, weight="700"))
    return y + h


def flecha(b, x1, y1, x2, y2, c, sw=2.6, bend=0.0, head=13):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def marca(b, x, y, txt, c):
    b.append(checkbox(x, y, s=11, c=c))
    b.append(T(x + 30, y + 18, [txt], 16, GRAY))


def particula(b, cx, cy, c, r=8):
    b.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" fill="white" stroke="{c}" stroke-width="2"/>')


def ejes(b, x, y, w, h, xlab, ylab, xt=(), yt=()):
    b.append(f'<line x1="{x}" y1="{y + h}" x2="{x + w}" y2="{y + h}" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + h}" stroke="{INK}" stroke-width="2"/>')
    for f, lab in xt:
        xx = x + f * w
        b.append(f'<line x1="{xx:.0f}" y1="{y}" x2="{xx:.0f}" y2="{y + h}" stroke="#E6EAF0" stroke-width="1.4"/>')
        b.append(T(xx, y + h + 22, [lab], 14, GRAY, anchor="middle"))
    for f, lab in yt:
        yy = y + h - f * h
        b.append(f'<line x1="{x}" y1="{yy:.0f}" x2="{x + w}" y2="{yy:.0f}" stroke="#E6EAF0" stroke-width="1.4"/>')
        b.append(T(x - 8, yy + 5, [lab], 14, GRAY, anchor="end"))
    b.append(T(x + w, y + h + 44, [xlab], 14, GRAY, style="italic", anchor="end"))
    b.append(T(x, y - 10, [ylab], 14, GRAY, style="italic"))


def curva(b, pts, c, sw=3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    b.append(f'<polyline points="{" ".join(f"{px:.0f},{py:.0f}" for px, py in pts)}" fill="none" '
             f'stroke="{c}" stroke-width="{sw}" stroke-linejoin="round"{d}/>')


def rejilla_particulas(b, x, y, n, m, paso, c, r=7):
    for i in range(n):
        for j in range(m):
            particula(b, x + i * paso, y + j * paso, c, r=r)


# ───────── P1 · dos curvas de calentamiento ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos curvas, dos mesetas, dos esperas", c,
                      "La gráfica está copiada de tu libro. Repasa con lápiz el tramo en que cada curva sube y "
                      "encierra el tramo en que se queda plana. Después llena la tabla con lo que leíste, no con "
                      "lo que esperabas leer.")
    x0, ww = x + 22, w - 44
    gx, gy, gw, gh = x0 + 60, yy + 30, 470, 250
    ejes(b, gx, gy, gw, gh, "tiempo (min)", "temperatura (°C)",
         xt=[(k / 5, str(k * 5)) for k in range(6)], yt=[(130 / 220, "130"), (160 / 220, "160"), (200 / 220, "200")])

    def P(t, temp):
        return gx + t / 25 * gw, gy + gh - temp / 220 * gh
    # X: empieza cerca de 120 °C y se aplana en 130 °C hacia el minuto 5
    curva(b, [P(t / 4, 120 + 10 * (1 - math.exp(-((t / 4) / 2.0) ** 2))) for t in range(0, 101)], "#C2185B")
    # Y: empieza abajo, sube en S y se aplana en 200 °C hacia el minuto 10
    curva(b, [P(t / 4, 10 + 190 / (1 + math.exp(-((t / 4) - 5.0) * 1.1))) for t in range(0, 101)], "#3A8C9A")
    texto(b, gx + gw + 8, P(25, 200)[1] + 6, "Y", 16, INK, weight="700")
    texto(b, gx + gw + 8, P(25, 130)[1] + 6, "X", 16, INK, weight="700")
    pista(b, gx, gy + gh + 64, "esquema de la gráfica de tu libro (página 150)", size=13)
    rx = gx + gw + 60
    rw = x0 + ww - rx
    cols = ("", "X", "Y")
    cxs = (rx, rx + 300, rx + 430)
    for k, cl in enumerate(cols):
        rot(b, cxs[k], yy + 22, cl, c, size=14)
    filas = ("empieza en (°C)", "se queda plana en (°C)", "llega a lo plano en el minuto", "el texto dice que funde a (°C)")
    for j, f in enumerate(filas):
        ry = yy + 36 + j * 60
        caja(b, rx, ry, rw, 50, c, r=10)
        texto(b, rx + 14, ry + 32, f, 16)
        hueco(b, cxs[1] - 10, ry + 7, 100, 36, c)
        hueco(b, cxs[2] - 10, ry + 7, 100, 36, c)
    yy = max(gy + gh + 80, yy + 36 + 4 * 60) + 10
    yy = frase_hueco(b, x0, yy, ww, "Y tarda más porque antes de fundirse tiene que subir ____ °C y X solo ____ °C.", c)
    return ojo(b, x0, yy + 14, ww, "LA GRÁFICA Y EL TEXTO NO DICEN LO MISMO",
               "El texto dice que Y empieza a fundirse a 160 °C, pero en la gráfica su tramo plano está en 200 °C. "
               "Y ninguna curva muestra cuándo termina la fusión. Escribe las dos lecturas en la tabla y coméntalo "
               "con el profe: la idea de la pregunta se sostiene con cualquiera de los dos números.")


# ───────── P2 · parafina · calor en dos tramos ─────────
def i2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La cuenta del calor en dos tramos", c,
                      "Fundir un sólido que está frío cuesta dos cuentas: una para llevarlo hasta su punto de fusión "
                      "y otra para fundirlo. Ubica los dos tramos en el dibujo, haz cada cuenta con sus unidades y "
                      "súmalas.")
    x0, ww = x + 22, w - 44
    # esquema de los dos tramos
    gx, gy, gw, gh = x0 + 50, yy + 30, 360, 200
    ejes(b, gx, gy, gw, gh, "calor que entra", "temperatura (°C)")
    p0, p1, p2 = (gx + 10, gy + gh - 40), (gx + 150, gy + 70), (gx + gw - 20, gy + 70)
    curva(b, [p0, p1, p2], c)
    b.append(f'<circle cx="{p0[0]}" cy="{p0[1]}" r="5" fill="{c}"/>')
    pista(b, p0[0] + 16, p0[1] + 26, "____ °C", size=14)
    pista(b, p1[0] - 24, p1[1] - 14, "____ °C", size=14)
    rot(b, gx + 110, gy + gh - 22, "TRAMO 1", c, size=13)
    rot(b, gx + 210, gy + 100, "TRAMO 2", c, size=13)
    rx = gx + gw + 50
    rw = x0 + ww - rx
    for k, (rt, f, l2) in enumerate((
            ("TRAMO 1 · SUBIR HASTA EL PUNTO DE FUSIÓN", "Q₁ = m × c × ΔT",
             "Q₁ = ____ g × ____ J/(g·°C) × ____ °C = ________ J"),
            ("TRAMO 2 · FUNDIR SIN CAMBIAR DE TEMPERATURA", "Q₂ = m × L",
             "Q₂ = ____ g × ____ J/g = ________ J"))):
        ry = yy + k * 130
        caja(b, rx, ry, rw, 116, c, r=14)
        rot(b, rx + 18, ry + 28, rt, c, size=13)
        texto(b, rx + 18, ry + 62, f, 18, INK, weight="700")
        texto(b, rx + 18, ry + 100, l2, 17)
    yy += 2 * 130 + 16
    yy = frase_hueco(b, x0, yy, ww, "Total = Q₁ + Q₂ = ________ J + ________ J = ________ J", c)
    yy += 14
    caja(b, x0, yy, ww, 90, c, r=12)
    rot(b, x0 + 20, yy + 28, "LAS UNIDADES TAMBIÉN SE CANCELAN", c, size=14)
    texto(b, x0 + 20, yy + 68, "g  ×  J/(g·°C)  ×  °C   →   queda solo: ______          g  ×  J/g   →   queda solo: ______", 18)
    yy += 106
    return ojo(b, x0, yy, ww, "ΔT ES UNA RESTA",
               "ΔT se lee «cambio de temperatura»: la de llegada menos la de salida. Si multiplicas por la "
               "temperatura final, la cuenta del tramo 1 sale más grande de lo que es.")


# ───────── P3 · tanque de propano al sol ─────────
def _tanque(b, x, y, w, h, c, fill="white"):
    b.append(rect(x, y, w, h, fill, r=h / 2, stroke=VIDRIO, sw=3))
    b.append(rect(x + w / 2 - 10, y - 22, 20, 22, "white", r=3, stroke=VIDRIO, sw=2.4))


def i3(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Partículas en un tanque que no puede agrandarse", c,
                      "Las partículas son las mismas en los dos dibujos. Ponle a cada una una flecha: corta si va "
                      "despacio, larga si va rápido. Marca después qué cambió al calentarse y qué no pudo cambiar.")
    x0, ww = x + 22, w - 44
    random.seed(3)
    pos = [(random.uniform(24, 226), random.uniform(22, 98)) for _ in range(9)]
    for k, (temp, fill) in enumerate((("20 °C", "white"), ("70 °C", CALIENTE))):
        tx = x0 + 10 + k * 300
        _tanque(b, tx, yy + 40, 250, 120, c, fill)
        for px, py in pos:
            particula(b, tx + px, yy + 40 + py, c, r=8)
        rot(b, tx + 125, yy + 190, temp, c, size=15, anchor="middle")
    rx = x0 + 620
    rw = x0 + ww - rx
    cols = ("AL CALENTARSE…", "aumenta", "igual", "disminuye")
    for k, cl in enumerate(cols):
        if k == 0:
            rot(b, rx, yy + 14, cl, c, size=13)
        else:
            pista(b, rx + 250 + (k - 1) * 110, yy + 14, cl, size=14)
    for j, f in enumerate(("número de partículas", "volumen del tanque", "rapidez de las partículas",
                           "choques contra la pared")):
        ry = yy + 26 + j * 46
        caja(b, rx, ry, rw, 40, c, r=8)
        texto(b, rx + 14, ry + 27, f, 16)
        for k in range(3):
            b.append(checkbox(rx + 262 + k * 110, ry + 9, s=11, c=c))
    yy += 26 + 4 * 46 + 18
    caja(b, x0, yy, ww, 156, c, r=14)
    rot(b, x0 + 20, yy + 30, "COMPRUEBA LA GRÁFICA CON LA LEY DE LOS GASES (TEMPERATURA EN KELVIN)", c, size=14)
    texto(b, x0 + 20, yy + 74, "T₁ = 20 + 273 = ______ K       T₂ = 70 + 273 = ______ K       "
                               "P₁ (gráfica, a 20 °C) ≈ ______ atm", 17)
    texto(b, x0 + 20, yy + 120, "P₂ = P₁ × T₂ ÷ T₁ = ______ × ______ ÷ ______ ≈ ______ atm      "
                                "la gráfica dice a 70 °C: ______ atm", 17)
    yy += 172
    return ojo(b, x0, yy, ww, "SI LA LEY Y LA GRÁFICA NO COINCIDEN, NO TE EQUIVOCASTE",
               "Con el gas solo, la presión debería subir poco. La curva del libro sube mucho más porque en un "
               "tanque de propano hay líquido que se evapora al calentarse. La idea de la pregunta (partículas más "
               "rápidas, más choques) se mantiene; el número, coméntalo con el profe.")


# ───────── P4 · grasa vegetal · por qué una cantidad específica ─────────
def i4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La misma energía, dos trabajos distintos", c,
                      "Dibuja las partículas de la grasa en tres momentos. Debajo escribe en qué se gasta la energía "
                      "en cada tramo y haz las dos cuentas: así ves de dónde sale una cantidad «específica».")
    x0, ww = x + 22, w - 44
    n, gap = 3, 56
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("A 25 °C · SÓLIDO", "dibujo ya hecho: ordenadas"),
                                  ("A 45 °C · FUNDIÉNDOSE", "dibújalas tú"),
                                  ("A 45 °C · LÍQUIDO", "dibújalas tú"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 196, c, r=14)
        rot(b, bx + 18, yy + 28, rt, c, size=13)
        pista(b, bx + 18, yy + 50, ps, size=13)
        if k == 0:
            rejilla_particulas(b, bx + bw / 2 - 60, yy + 80, 5, 4, 30, c)
        if k < n - 1:
            flecha(b, bx + bw + 8, yy + 100, bx + bw + gap - 8, yy + 100, c, sw=3, head=14)
            pista(b, bx + bw + gap / 2, yy + 140, f"tramo {k + 1}", size=13, anchor="middle")
    yy += 212
    half = (ww - 24) / 2
    for k, (rt, cu) in enumerate((("TRAMO 1 · LA ENERGÍA SE GASTA EN", "100 g × 2,0 J/(g·°C) × ____ °C = ______ J"),
                                  ("TRAMO 2 · LA ENERGÍA SE GASTA EN", "100 g × 180 J/g = ______ J"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 136, c, r=14)
        rot(b, bx + 18, yy + 28, rt, c, size=13)
        renglon(b, bx + 18, yy + 70, bx + half - 18)
        texto(b, bx + 18, yy + 116, cu, 17)
    yy += 152
    return frase_hueco(b, x0, yy, ww, "Esa cantidad depende de tres datos de la grasa: ________ , ________ y ________ .", c)


# ───────── P5 · bandeja contra baño · por dónde entra el calor ─────────
def _bloque(b, x, y, s, c):
    """Bloque en perspectiva sencilla: frente, techo y lado."""
    d = s * 0.35
    b.append(f'<polygon points="{x},{y} {x + s},{y} {x + s},{y + s} {x},{y + s}" fill="#F6D9B8" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<polygon points="{x},{y} {x + d},{y - d} {x + s + d},{y - d} {x + s},{y}" fill="#FBE8D2" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<polygon points="{x + s},{y} {x + s + d},{y - d} {x + s + d},{y + s - d} {x + s},{y + s}" fill="#EFC99E" stroke="{INK}" stroke-width="2"/>')


def i5(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Por cuántas caras le entra el calor", c,
                      "Pinta en cada bloque las caras que tocan algo caliente y cuéntalas. Después responde con tu "
                      "cuenta de la pregunta 4 si el método cambia la cantidad de calor que el bloque necesita o solo "
                      "la manera en que le llega.")
    x0, ww = x + 22, w - 44
    # método A: bandeja metálica
    ax = x0 + 60
    _bloque(b, ax + 60, yy + 80, 130, c)
    b.append(rect(ax, yy + 210, 300, 16, "#B9C2CC", r=3, stroke=INK, sw=1.8))
    for k in range(4):
        flecha(b, ax + 50 + k * 70, yy + 290, ax + 50 + k * 70, yy + 236, RO, sw=2.4, head=10)
    rot(b, ax + 150, yy + 30, "MÉTODO A · BANDEJA", c, size=13, anchor="middle")
    pista(b, ax + 150, yy + 316, "calor por debajo", size=13, anchor="middle")
    # método B: baño de agua a 80 °C
    bx = x0 + 440
    b.append(rect(bx, yy + 50, 300, 230, AGUA, r=10, stroke=VIDRIO, sw=3))
    _bloque(b, bx + 90, yy + 130, 110, c)
    rot(b, bx + 150, yy + 30, "MÉTODO B · BAÑO A 80 °C", c, size=13, anchor="middle")
    pista(b, bx + 150, yy + 316, "agua caliente alrededor", size=13, anchor="middle")
    rx = x0 + 800
    rw = x0 + ww - rx
    caja(b, rx, yy + 40, rw, 250, c, r=14)
    rot(b, rx + 18, yy + 70, "CARAS QUE TOCAN LO CALIENTE", c, size=13)
    pista(b, rx + 18, yy + 116, "método A:   ____ de 6")
    pista(b, rx + 18, yy + 156, "método B:   ____ de 6")
    pista(b, rx + 18, yy + 206, "¿el calor que necesita el bloque")
    pista(b, rx + 18, yy + 230, "cambia con el método?")
    marca(b, rx + 18, yy + 246, "sí", c)
    marca(b, rx + 110, yy + 246, "no", c)
    yy += 340
    yy = frase_hueco(b, x0, yy, ww, "Es más eficiente el método en que el calor ____________________________ .", c)
    return trampa(b, x0, yy + 14, ww, "Una razón puede describir otro montaje:",
                  "antes de aceptar una opción, mira el esquema: qué toca al bloque en cada método. Si la razón "
                  "habla de algo que no aparece en el dibujo, no está describiendo este experimento.", c)


# ───────── P6 · qué hace el agua caliente ─────────
def i6(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El termómetro del baño", c,
                      "Ubica en la escala las tres temperaturas del experimento y mide la distancia entre ellas. La "
                      "hipótesis tiene que hablar de algo que el agua sí puede hacer: el agua no le cambia a la grasa "
                      "lo que la grasa es.")
    x0, ww = x + 22, w - 44
    # escala vertical de 0 a 100 °C
    sx, sy, sh = x0 + 120, yy + 20, 340
    b.append(rect(sx - 14, sy, 28, sh, "white", r=14, stroke=VIDRIO, sw=2.6))
    b.append(f'<circle cx="{sx}" cy="{sy + sh + 18}" r="24" fill="#E8735A" stroke="{VIDRIO}" stroke-width="2.6"/>')
    for t in range(0, 101, 10):
        ty = sy + sh - t / 100 * (sh - 20) - 10
        b.append(f'<line x1="{sx + 16}" y1="{ty:.0f}" x2="{sx + 30}" y2="{ty:.0f}" stroke="{INK}" stroke-width="1.6"/>')
        texto(b, sx + 38, ty + 5, f"{t} °C", 13, GRAY)
    for k, lab in enumerate(("temperatura inicial del bloque", "punto de fusión de la grasa", "temperatura del baño")):
        ly = yy + 60 + k * 90
        pista(b, x0 + 280, ly, lab)
        hueco(b, x0 + 520, ly - 26, 90, 38, c)
        texto(b, x0 + 618, ly, "°C", 16, GRAY)
    pista(b, x0 + 280, yy + 330, "marca las tres con una raya en el termómetro", size=14)
    rx = x0 + 700
    rw = x0 + ww - rx
    caja(b, rx, yy + 20, rw, 330, c, r=14)
    rot(b, rx + 18, yy + 50, "LO QUE EL AGUA SÍ PUEDE HACER", c, size=13)
    pista(b, rx + 18, yy + 92, "el baño queda por encima del")
    pista(b, rx + 18, yy + 116, "punto de fusión:  ______ °C")
    pista(b, rx + 18, yy + 166, "¿esa temperatura la tiene")
    pista(b, rx + 18, yy + 190, "todo el tiempo?")
    marca(b, rx + 200, yy + 172, "sí", c)
    marca(b, rx + 280, yy + 172, "no", c)
    pista(b, rx + 18, yy + 240, "¿le llega al bloque por")
    pista(b, rx + 18, yy + 264, "todos lados?")
    marca(b, rx + 200, yy + 246, "sí", c)
    marca(b, rx + 280, yy + 246, "no", c)
    pista(b, rx + 18, yy + 316, "(mira tu dibujo de la pregunta 5)", size=13)
    yy += 400
    return trampa(b, x0, yy, ww, "El agua no puede cambiar lo que la grasa es:",
                  "su punto de fusión y su calor latente son de la grasa, como su color. Una hipótesis que dice que "
                  "el baño los cambia explica con algo que el agua no puede hacer.", c)


# ───────── P7 · hielo seco ─────────
def i7(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El triángulo de los estados y el atajo del hielo seco", c,
                      "Escribe el nombre de cada flecha del triángulo. Después repasa con color el camino que siguió "
                      "el hielo seco en la feria. La pista está en lo que no quedó en la mesa.")
    x0, ww = x + 22, w - 44
    cx, top = x0 + 360, yy + 30
    V = {"SÓLIDO": (cx - 260, top + 300), "LÍQUIDO": (cx + 260, top + 300), "GAS": (cx, top + 10)}
    for nom, (vx, vy) in V.items():
        b.append(rect(vx - 70, vy - 26, 140, 52, "white", r=26, stroke=c, sw=2.6))
        texto(b, vx, vy + 7, nom, 17, c, weight="700", anchor="middle")
    pares = (("SÓLIDO", "LÍQUIDO"), ("LÍQUIDO", "GAS"), ("SÓLIDO", "GAS"))
    for a_, z_ in pares:
        (ax_, ay_), (zx, zy) = V[a_], V[z_]
        dx, dy = zx - ax_, zy - ay_
        L = math.hypot(dx, dy)
        ux, uy = dx / L, dy / L
        nx, ny = -uy * 14, ux * 14
        s0, s1 = 80, L - 80
        flecha(b, ax_ + ux * s0 + nx, ay_ + uy * s0 + ny, ax_ + ux * s1 + nx, ay_ + uy * s1 + ny, c, sw=2.4, head=11)
        flecha(b, ax_ + ux * s1 - nx, ay_ + uy * s1 - ny, ax_ + ux * s0 - nx, ay_ + uy * s0 - ny, c, sw=2.4, head=11)
        # dos renglones (ida y vuelta) por fuera del triángulo, sin tocar las flechas
        mx, my = ax_ + dx / 2, ay_ + dy / 2
        if abs(dy) < 1:                     # base del triángulo: renglones debajo
            for k in (48, 80):
                renglon(b, mx - 90, my + k, mx + 90)
        else:
            x1, x2 = (mx - 230, mx - 60) if mx < cx else (mx + 60, mx + 230)
            for k in (-18, 18):
                renglon(b, x1, my + k, x2)
    rx = x0 + 760
    rw = x0 + ww - rx
    caja(b, rx, yy + 20, rw, 320, c, r=14)
    rot(b, rx + 18, yy + 50, "LA PISTA DE LA MESA", c, size=13)
    pista(b, rx + 18, yy + 92, "en la mesa no quedó:")
    renglon(b, rx + 18, yy + 126, rx + rw - 18)
    pista(b, rx + 18, yy + 172, "entonces nunca pasó por el")
    pista(b, rx + 18, yy + 196, "estado:")
    renglon(b, rx + 80, yy + 198, rx + rw - 18)
    pista(b, rx + 18, yy + 246, "el camino se llama:")
    renglon(b, rx + 18, yy + 286, rx + rw - 18)
    yy += 440
    return ojo(b, x0, yy, ww, "EL HUMO BLANCO NO ES EL CO₂",
               "El dióxido de carbono gaseoso es invisible. La nube blanca que se ve son gotitas de agua del aire que "
               "se condensan porque el hielo seco las enfría. El hielo seco no se disuelve en esas gotas: desaparece "
               "por otro camino.")


# ───────── P8 · el termómetro que se detiene ─────────
def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dibuja lo que cuenta el termómetro", c,
                      "Lee la historia del matraz y dibújala como gráfica: sube, se detiene unos minutos, vuelve a "
                      "subir. Después dibuja las partículas en cada tramo y escribe en qué se gasta el calor del "
                      "mechero cuando la temperatura no se mueve.")
    x0, ww = x + 22, w - 44
    gx, gy, gw, gh = x0 + 60, yy + 30, 520, 240
    ejes(b, gx, gy, gw, gh, "tiempo", "temperatura")
    pista(b, gx + 20, gy + 30, "dibuja aquí la curva", size=14)
    rx = gx + gw + 50
    rw = x0 + ww - rx
    for k, rt in enumerate(("TRAMO 1 · SUBE", "TRAMO 2 · SE DETIENE", "TRAMO 3 · VUELVE A SUBIR")):
        ry = yy + k * 98
        caja(b, rx, ry, rw, 88, c, r=12)
        rot(b, rx + 16, ry + 26, rt, c, size=13)
        caja(b, rx + rw - 120, ry + 10, 104, 68, c, r=8, dash="5,5")
        pista(b, rx + 16, ry + 50, "estado:", size=14)
        renglon(b, rx + 80, ry + 52, rx + rw - 140)
        pista(b, rx + 16, ry + 76, "partículas →", size=13)
    yy = max(yy + 3 * 98, gy + gh + 54) + 16
    yy = frase_hueco(b, x0, yy, ww, "En el tramo 2 el mechero sigue dando calor; ese calor se usa para ____________________ .", c)
    return ojo(b, x0, yy + 14, ww, "QUE LA TEMPERATURA NO SUBA NO QUIERE DECIR QUE NO ENTRE CALOR",
               "El mechero no se apagó. Pregúntate a dónde se va esa energía si no se nota en el termómetro: en la "
               "pregunta 2 ese tramo tuvo su propia cuenta.")


# ───────── P9 · la esfera que flota en mercurio ─────────
DENS = (("agua", 1.0), ("aluminio", 2.7), ("acero", 7.9), ("plomo", 11.3), ("mercurio", 13.6), ("oro", 19.3))


def i9(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La escalera de las densidades", c,
                      "Cada material está en su escalón según su densidad. Traza una raya horizontal a la altura del "
                      "mercurio y pinta de un color lo que flotaría en él y de otro lo que se hundiría. Tu libro no "
                      "dice de qué metal es la esfera: prueba con el acero.")
    x0, ww = x + 22, w - 44
    sx, sy, sh = x0 + 120, yy + 30, 380
    b.append(f'<line x1="{sx}" y1="{sy}" x2="{sx}" y2="{sy + sh}" stroke="{INK}" stroke-width="2.4"/>')
    for d in range(0, 21, 5):
        ty = sy + sh - d / 20 * sh
        b.append(f'<line x1="{sx - 10}" y1="{ty:.0f}" x2="{sx}" y2="{ty:.0f}" stroke="{INK}" stroke-width="1.8"/>')
        texto(b, sx - 16, ty + 5, str(d), 14, GRAY, anchor="end")
    pista(b, sx - 100, sy - 12, "densidad (g/cm³)", size=13)
    for k, (nom, d) in enumerate(DENS):
        ty = sy + sh - d / 20 * sh
        lx = sx + 40 + (k % 2) * 230
        b.append(f'<line x1="{sx}" y1="{ty:.0f}" x2="{lx - 6}" y2="{ty:.0f}" stroke="{GRAY}" stroke-width="1.4" '
                 f'stroke-dasharray="4,4"/>')
        texto(b, lx, ty + 6, f"{nom} · {str(d).replace('.', ',')}", 16, INK, weight="700")
    rx = x0 + 680
    rw = x0 + ww - rx
    caja(b, rx, yy + 20, rw, 250, c, r=14)
    rot(b, rx + 18, yy + 50, "DOS FUERZAS SOBRE LA ESFERA", c, size=13)
    ecx, ecy = rx + rw / 2, yy + 160
    # una esfera de acero queda hundida algo más de la mitad (7,9 ÷ 13,6 ≈ 0,58)
    b.append(f'<circle cx="{ecx}" cy="{ecy}" r="34" fill="white"/>')
    b.append(f'<rect x="{rx + 30}" y="{ecy - 5}" width="{rw - 60}" height="66" rx="6" fill="#C9D0D8" opacity="0.85"/>')
    b.append(f'<circle cx="{ecx}" cy="{ecy}" r="34" fill="none" stroke="{INK}" stroke-width="2.4"/>')
    pista(b, rx + 40, ecy + 50, "mercurio", size=13)
    pista(b, rx + 18, yy + 254, "dibuja el peso (↓) y el empuje (↑): ¿cuál más larga?", size=13)
    yy += 290
    caja(b, rx, yy, rw, 116, c, r=14)
    pista(b, rx + 18, yy + 40, "acero:  ______ g/cm³")
    pista(b, rx + 18, yy + 72, "mercurio:  ______ g/cm³")
    pista(b, rx + 18, yy + 104, "¿cuál es mayor?  ______________")
    yy = max(yy + 116, sy + sh + 20) + 14
    return frase_hueco(b, x0, yy, ww, "Un objeto flota en un líquido cuando su densidad es ________ que la del líquido.", c)


# ───────── P10 · por qué sube tan rápido ─────────
VISC = (("agua", "≈ 1"), ("mercurio", "≈ 1,5"), ("aceite de cocina", "≈ 60"), ("miel", "≈ 5 000"))


def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Lo que la empuja y lo que la frena", c,
                      "Cuando sueltas la esfera en el fondo pasan dos cosas: algo la empuja hacia arriba y algo se "
                      "opone a que se mueva. Dibuja las tres fuerzas y separa la pregunta en dos: por qué sube y por "
                      "qué sube rápido.")
    x0, ww = x + 22, w - 44
    # recipiente con la esfera en el fondo
    vx, vy, vw, vh = x0 + 40, yy + 20, 260, 320
    b.append(rect(vx, vy + 40, vw, vh - 40, "#DDE2E8", r=10, stroke=VIDRIO, sw=3))
    b.append(f'<circle cx="{vx + vw / 2}" cy="{vy + vh - 60}" r="34" fill="white" stroke="{INK}" stroke-width="2.4"/>')
    pista(b, vx + vw / 2, vy + 24, "mercurio", size=13, anchor="middle")
    pista(b, vx + vw / 2, vy + vh + 24, "dibuja 3 flechas sobre la esfera", size=13, anchor="middle")
    rx = x0 + 340
    rw = x0 + ww - rx
    for k, (rt, ps) in enumerate((("LO QUE LA EMPUJA HACIA ARRIBA", "la fuerza y la propiedad que la produce (pregunta 9)"),
                                  ("LO QUE LA FRENA MIENTRAS SUBE", "la fuerza y la propiedad del líquido que la produce"))):
        ry = yy + 20 + k * 120
        caja(b, rx, ry, rw, 106, c, r=14)
        rot(b, rx + 18, ry + 28, rt, c, size=13)
        pista(b, rx + 18, ry + 52, ps, size=14)
        renglon(b, rx + 18, ry + 90, rx + rw - 18)
    ty = yy + 270
    rot(b, rx, ty, "QUÉ TAN ESPESO ES CADA LÍQUIDO (VISCOSIDAD, EN mPa·s, CERCA DE 25 °C)", c, size=13)
    cw_ = rw / 4
    for k, (nom, v) in enumerate(VISC):
        bx = rx + k * cw_
        caja(b, bx + 4, ty + 14, cw_ - 8, 66, c, r=10)
        texto(b, bx + cw_ / 2, ty + 42, nom, 16, INK, weight="700", anchor="middle")
        texto(b, bx + cw_ / 2, ty + 68, v, 16, GRAY, anchor="middle")
    yy = max(ty + 96, vy + vh + 40)
    yy = frase_hueco(b, x0, yy, ww, "Sube porque ____________________ ; sube rápido porque ____________________ .", c)
    return ojo(b, x0, yy + 14, ww, "LA PREGUNTA PIDE LA RAPIDEZ, NO LA CAUSA",
               "Lo que hace subir a la esfera ya lo escribiste en la pregunta 9. Aquí preguntan otra cosa: por qué "
               "sube tan rápido. Con cada opción hazte dos preguntas: ¿el mercurio de verdad tiene esa propiedad? "
               "¿y esa propiedad cambia la rapidez de algo que se mueve dentro de él?")


Q = {1: dict(n=1, est=1, pag=150, ctx="Dos sólidos X y Y calentados igual · por qué Y tarda más en fundirse",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=2, pag=150, ctx="Bloques de parafina en un incendio · cuánta energía para fundirse",
             comp="Uso comprensivo del conocimiento científico", inst=i2),
     3: dict(n=3, est=3, pag=150, ctx="Tanque de propano al sol · por qué sube la presión",
             comp="Explicación de fenómenos", inst=i3),
     4: dict(n=4, est=2, pag=151, ctx="Grasa vegetal · por qué una cantidad específica de energía",
             comp="Explicación de fenómenos", inst=i4),
     5: dict(n=5, est=3, pag=151, ctx="Bandeja metálica o baño a 80 °C · qué método es más eficiente",
             comp="Indagación", inst=i5),
     6: dict(n=6, est=3, pag=151, ctx="El baño caliente y el tiempo de fusión · qué hipótesis",
             comp="Indagación", inst=i6),
     7: dict(n=7, est=1, pag=151, ctx="Hielo seco que se reduce sin dejar charco · qué propiedad",
             comp="Explicación de fenómenos", inst=i7),
     8: dict(n=8, est=1, pag=152, ctx="Matraz con un sólido orgánico · la temperatura que se estabiliza",
             comp="Explicación de fenómenos", inst=i8),
     9: dict(n=9, est=4, pag=152, ctx="Una esfera metálica que flota en mercurio · qué hipótesis",
             comp="Explicación de fenómenos", inst=i9),
     10: dict(n=10, est=4, pag=152, ctx="La esfera sube rápido desde el fondo · qué propiedad del mercurio",
              comp="Explicación de fenómenos", inst=i10)}


def build(pages=(190, 191, 193, 194, 195)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"qui2_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
