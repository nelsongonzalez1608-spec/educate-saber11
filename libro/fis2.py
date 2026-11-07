#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 2 · componente físico · termodinámica · páginas 233–239.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 2» de Física (fuente_libro/FÍSICA), páginas 216–218.
Casos: pared de ladrillo de doble grosor · ley de Fourier (1), agua hirviendo lanzada al aire
en un día bajo cero, «efecto Mpemba» (2 y 3), olla a presión que libera vapor (4), gas que se
enfría hacia el cero absoluto (5), vidrio que se empaña y se aclara (6), bloques de cobre y de
aluminio que se enfrían de 120 °C a 10 °C (7), dos termómetros en un salón con calefacción (8),
calorímetro: cuerpo de 2 kg a 80 °C con 3 kg de agua a 20 °C (9), expresión del calor
específico de un cuerpo de 200 g (10).

Claves verificadas (resueltas a mano contra el texto y las figuras, 7 nov 2026):

    1·A  2·B  3·C  4·B  5·C  6·A  7·C  8·D  9·C  10·D

Cuentas y razones:
  1 · Flujo de calor por conducción: Q/t = k·A·(T₁ − T₂)/d. Mismo k, A y ΔT = 20 °C; d → 2d: el
      flujo se reduce a la mitad, más lento (A). Ver hallazgo: el libro escribe Q y no Q/t.
  2 · Las gotas finas tienen mucha superficie para su volumen: se evaporan muy rápido, y la
      evaporación se lleva las moléculas más energéticas y enfría lo que queda (B). (1 cubo de
      1 cm: 6 cm²; los mismos 1 cm³ en 1000 cubitos de 1 mm: 60 cm²).
  3 · Sin frío muy intenso las gotas no alcanzan a congelarse en el trayecto (C). A habla de
      temperatura «moderada»; B y D agregan condiciones que el fenómeno no necesita.
  4 · Hierve cuando la presión de vapor iguala la presión externa: con menos presión, hierve a
      menor temperatura (B). Ver hallazgo: el enunciado dice que se baja la presión para cocinar
      más rápido, y es al revés.
  5 · La curva cae cada vez menos por cada julio extraído y se aplana cerca de −273 °C: baja de
      manera progresivamente más lenta (C). Ver hallazgo (Media) sobre la física de la gráfica.
  6 · El aire húmedo de adentro toca el vidrio frío, se enfría y su vapor se condensa; cuando el
      vidrio se calienta, las gotas se evaporan (A).
  7 · Q = m·c·ΔT con ΔT = 110 °C: cobre 5 × 390 × 110 = 214 500 J; aluminio 5 × 900 × 110 =
      495 000 J. El cobre tiene que soltar menos de la mitad del calor: llega primero (C), si los
      dos pierden calor al mismo ritmo. Ver hallazgo sobre ese supuesto.
  8 · El aire caliente es menos denso, sube y se acumula arriba: convección (D).
  9 · 2000 g × 0,5 × (80 − T) = 3000 g × 1 × (T − 20) → 80 000 − 1000 T = 3000 T − 60 000 →
      T = 35 °C: entre 20 °C y 80 °C (C).
 10 · Calor que pierde el cuerpo = calor que gana el agua: 200 · c₂ · (80 − 30) = 500 · 1 · (30 − 25)
      → c₂ = 500·(30 − 25) ÷ (200·(80 − 30)) = 2500 ÷ 10 000 = 0,25 cal/(g·°C) (D). Ver hallazgo
      (Alta): la A, 500·(25 − 30) ÷ (200·(30 − 80)) = (−2500) ÷ (−10 000), da el mismo 0,25: hay
      dos expresiones correctas. Clave propuesta D (la forma con las dos diferencias positivas).

Reparto: A 2 · B 2 · C 4 · D 2. C concentra 4 de 10 (no llega a la mitad).
Hallazgos: tablero/propuestas/fis2_hallazgos.csv.

Estrategias:
    1 · El calor va del caliente al frío   (1, 6, 8  · ICFES ASED Mecánica N.º 10)          azul
    2 · La cuenta del calor                (7, 9, 10 · ICFES cuadernillo 2025-2026 N.º 22)  rojo
    3 · Lo que hacen las partículas        (2, 5     · ICFES cuadernillo 2025-2026 N.º 1)   oro
    4 · El ambiente decide el cambio de fase (3, 4   · ICFES cuadernillo 2025-2026 N.º 27)  morado

Hojas: 233 fis2_t1 (1-2) · 234 fis2_t2 (3-4) · 235 fis2_i1 · 236 fis2_t3 (5-6) ·
       237 fis2_t4 (7-8) · 238 fis2_t5 (9-10) · 239 fis2_i2.
"""
import math
import random
import re

from taller_base import *

configurar("Física", 2, "físico · termodinámica",
           tema="El calor, la temperatura y los cambios de fase",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("El calor va del caliente al frío", EDU_AZUL),
       2: ("La cuenta del calor", EDU_ROJO),
       3: ("Lo que hacen las partículas", EDU_ORO),
       4: ("El ambiente decide el cambio de fase", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))
FRIO = "#EAF4FA"          # relleno de lo frío
CALIENTE = "#FCE9DD"      # relleno de lo caliente
VIDRIO = "#7C8A99"


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def _esp(txt):
    """SVG junta los espacios repetidos: los que separan bloques se vuelven espacios duros."""
    return re.sub(r" {2,}", lambda m: " " * len(m.group()), txt)


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


def linea_pista(b, x, y, x2, lab, size=15):
    """Rótulo en cursiva y renglón que empieza donde termina el rótulo (medido con tw)."""
    pista(b, x, y, lab, size=size)
    renglon(b, x + tw(lab, size, style="italic") + 12, y + 2, x2)


def ejes(b, x, y, w, h, xlab, ylab, xt=(), yt=()):
    for f, lab in xt:
        xx = x + f * w
        b.append(f'<line x1="{xx:.0f}" y1="{y}" x2="{xx:.0f}" y2="{y + h}" stroke="#E6EAF0" stroke-width="1.4"/>')
        b.append(T(xx, y + h + 22, [lab], 14, GRAY, anchor="middle"))
    for f, lab in yt:
        yy = y + h - f * h
        b.append(f'<line x1="{x}" y1="{yy:.0f}" x2="{x + w}" y2="{yy:.0f}" stroke="#E6EAF0" stroke-width="1.4"/>')
        b.append(T(x - 8, yy + 5, [lab], 14, GRAY, anchor="end"))
    b.append(f'<line x1="{x}" y1="{y + h}" x2="{x + w}" y2="{y + h}" stroke="{INK}" stroke-width="2"/>')
    b.append(f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + h}" stroke="{INK}" stroke-width="2"/>')
    b.append(T(x + w, y + h + 44, [xlab], 14, GRAY, style="italic", anchor="end"))
    b.append(T(x, y - 10, [ylab], 14, GRAY, style="italic"))


def curva(b, pts, c, sw=3, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    b.append(f'<polyline points="{" ".join(f"{px:.0f},{py:.0f}" for px, py in pts)}" fill="none" '
             f'stroke="{c}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round"{d}/>')


def particula(b, cx, cy, c, r=7, fill="white"):
    b.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" fill="{fill}" stroke="{c}" stroke-width="2"/>')


# ───────── P1 · pared de doble grosor · ley de Fourier ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos paredes, una misma diferencia de temperatura", c,
                      "Dibuja una flecha de calor en cada pared: del lado caliente al frío, gruesa si pasa mucho calor "
                      "por segundo y delgada si pasa poco. Después mira qué letra de la fórmula cambió y qué le pasa "
                      "al resultado.")
    x0, ww = x + 22, w - 44
    yy = alto_profe(b, x0, yy, ww,
                    "La ley de Fourier dice cuánto calor pasa por una pared en cada segundo: Q ÷ t = k · A · (T₁ − T₂) ÷ d. "
                    "k depende del material, A es el área, T₁ − T₂ la diferencia de temperatura entre los dos lados y d "
                    "el grosor. El profe muestra que d está dividiendo.") + 18
    half = (ww - 30) / 2
    for k, (rt, gw) in enumerate((("PARED Y · GROSOR d", 50), ("PARED NUEVA · GROSOR 2d", 100))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 230, c, r=16)
        rot(b, bx + 18, yy + 28, rt, c, size=14)
        mx = bx + half / 2
        b.append(rect(bx + 14, yy + 44, mx - gw / 2 - bx - 14, 150, CALIENTE, r=8))
        b.append(rect(mx + gw / 2, yy + 44, bx + half - 14 - mx - gw / 2, 150, FRIO, r=8))
        b.append(rect(mx - gw / 2, yy + 40, gw, 158, "#E9DCCF", r=4, stroke="#A0705A", sw=2))
        texto(b, bx + 30, yy + 76, "adentro 25 °C", 15, INK)
        texto(b, bx + half - 30, yy + 76, "afuera 5 °C", 15, INK, anchor="end")
        pista(b, bx + 18, yy + 220, "el calor que pasa por segundo:", size=14)
        renglon(b, bx + 230, yy + 222, bx + half - 18)
    yy += 246
    cols = ("EN LA FÓRMULA", "k", "A", "T₁ − T₂", "d", "Q ÷ t")
    xs = (0, 260, 420, 580, 780, 960)
    caja(b, x0, yy, ww, 110, c, r=12)
    for k, cl in enumerate(cols):
        rot(b, x0 + 18 + xs[k], yy + 30, cl, c, size=13)
    texto(b, x0 + 18, yy + 80, "al pasar a la pared nueva:", 16, GRAY)
    for k in range(1, 6):
        pista(b, x0 + 18 + xs[k], yy + 64, "igual / doble / mitad", size=12)
        renglon(b, x0 + 18 + xs[k], yy + 92, x0 + xs[k] + 150)
    return yy + 110


# ───────── P2 · el agua hirviendo lanzada al aire · por qué se congela tan rápido ─────────
def i2(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Un balde de agua o mil gotitas", c,
                      "El agua pierde calor por su superficie. Haz la cuenta con un cubo de 1 cm de lado y con el mismo "
                      "volumen partido en cubitos de 1 mm. Después piensa qué moléculas son las que alcanzan a escaparse "
                      "por esa superficie.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (rt, l1, l2) in enumerate((
            ("UN CUBO DE 1 cm", "caras: 6   ·   área de una cara: 1 cm²", "superficie total = ______ cm²"),
            ("1000 CUBITOS DE 1 mm", "área de una cara: 0,01 cm²   ·   superficie de uno: ______ cm²",
             "superficie de los 1000 = ______ cm²"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 200, c, r=16)
        rot(b, bx + 18, yy + 28, rt, c, size=14)
        if k == 0:
            b.append(rect(bx + 30, yy + 52, 70, 70, FRIO, r=2, stroke=VIDRIO, sw=2))
        else:
            for i in range(5):
                for j in range(3):
                    b.append(rect(bx + 30 + i * 16, yy + 56 + j * 16, 11, 11, FRIO, r=1, stroke=VIDRIO, sw=1.4))
        texto(b, bx + 130, yy + 80, l1, 15 if k else 16)
        texto(b, bx + 130, yy + 116, l2, 16, INK, weight="700")
        pista(b, bx + 18, yy + 166, "mismo volumen: 1 cm³ de agua", size=14)
    yy += 216
    caja(b, x0, yy, ww, 236, c, r=14)
    rot(b, x0 + 20, yy + 30, "LAS MOLÉCULAS DE LA SUPERFICIE", c, size=14)
    pista(b, x0 + 20, yy + 54, "en una gota, unas moléculas van rápido y otras despacio: dibuja flechas largas y cortas", size=14)
    random.seed(4)
    gx, gy = x0 + 150, yy + 150
    b.append(f'<circle cx="{gx}" cy="{gy}" r="68" fill="{FRIO}" stroke="{VIDRIO}" stroke-width="2.4"/>')
    for _ in range(12):
        a = random.uniform(0, 2 * math.pi)
        rr = random.uniform(10, 56)
        particula(b, gx + rr * math.cos(a), gy + rr * math.sin(a), c, r=6)
    rx = x0 + 300
    linea_pista(b, rx, yy + 100, x0 + ww - 20, "las que alcanzan a escaparse del agua son las que van más")
    linea_pista(b, rx, yy + 148, x0 + ww - 20, "si se van las más rápidas, el promedio de las que quedan")
    linea_pista(b, rx, yy + 196, x0 + ww - 20, "y como la temperatura es ese promedio, la gota se")
    yy += 252
    return frase_hueco(b, x0, yy, ww, "Más superficie quiere decir que se escapan más moléculas cada segundo, así que la gota ___________ más rápido.", c)


# ───────── P3 · qué condición es indispensable ─────────
def i3(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La prueba de quitar una condición", c,
                      "Escribe las condiciones del fenómeno que trae el texto. Para cada una, imagina que la quitas: si "
                      "el fenómeno sigue ocurriendo, esa condición ayuda pero no es indispensable. Si deja de ocurrir, "
                      "encontraste la que se pide.")
    x0, ww = x + 22, w - 44
    cols = ("CONDICIÓN QUE TRAE EL TEXTO", "SI LA QUITO, ¿SE SIGUE CONGELANDO EN EL AIRE?", "ENTONCES ES")
    xs = (0, 470, 920)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=13)
    yy += 26
    for j in range(4):
        ry = yy + j * 66
        caja(b, x0, ry, ww, 56, c, r=10)
        b.append(T(x0 + 18, ry + 34, [f"{j + 1}"], 16, c, weight="700"))
        renglon(b, x0 + 44, ry + 40, x0 + xs[1] - 30)
        marca(b, x0 + xs[1], ry + 17, "sí", c)
        marca(b, x0 + xs[1] + 80, ry + 17, "no", c)
        pista(b, x0 + xs[2], ry + 34, "indispensable / ayuda", size=14)
    yy += 4 * 66 + 10
    caja(b, x0, yy, ww, 120, c, r=14)
    rot(b, x0 + 20, yy + 30, "EN QUÉ SE PARECE A LA PREGUNTA 2", c, size=14)
    linea_pista(b, x0 + 20, yy + 70, x0 + ww - 20, "¿qué tenía el aire de ese día que no tiene el aire de un día cualquiera?")
    linea_pista(b, x0 + 20, yy + 106, x0 + ww - 20, "si el aire estuviera a 15 °C, las gotas llegarían al suelo como")
    yy += 136
    return trampa(b, x0, yy, ww, "Una condición nueva no está en el texto:",
                  "si una opción pide algo que el texto nunca mencionó y sin lo cual el fenómeno igual ocurrió, "
                  "esa condición no puede ser la indispensable.", c)


# ───────── P4 · la olla a presión · temperatura de ebullición ─────────
PV = ((70, 31), (80, 47), (90, 70), (100, 101), (110, 143), (120, 199))


def i4(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La tabla de la presión de vapor", c,
                      "El agua hierve cuando la presión de su vapor alcanza la presión que la empuja desde afuera. Con "
                      "la tabla de valores reales, busca a qué temperatura hierve el agua con cada presión de afuera.")
    x0, ww = x + 22, w - 44
    # tabla de la presión de vapor del agua
    cw, hh = 110, 40
    texto(b, x0, yy + 16, "Presión de vapor del agua (valores medidos)", 15, INK, weight="700")
    yt = yy + 28
    b.append(rect(x0, yt, 200, hh, A["bg"], r=0, stroke=c, sw=1.4))
    texto(b, x0 + 100, yt + 26, "temperatura (°C)", 15, INK, weight="700", anchor="middle")
    b.append(rect(x0, yt + hh, 200, hh, A["bg"], r=0, stroke=c, sw=1.4))
    texto(b, x0 + 100, yt + hh + 26, "presión (kPa)", 15, INK, weight="700", anchor="middle")
    for k, (t, p) in enumerate(PV):
        cx = x0 + 200 + k * cw
        b.append(rect(cx, yt, cw, hh, "white", r=0, stroke=c, sw=1.4))
        b.append(rect(cx, yt + hh, cw, hh, "white", r=0, stroke=c, sw=1.4))
        texto(b, cx + cw / 2, yt + 26, str(t), 16, INK, anchor="middle")
        texto(b, cx + cw / 2, yt + hh + 26, str(p), 16, INK, anchor="middle")
    pista(b, x0, yt + 2 * hh + 26, "la presión del aire al nivel del mar es 101 kPa", size=14)
    yy = yt + 2 * hh + 44
    for j, (lab, p) in enumerate((("olla abierta al nivel del mar", "101"), ("olla a presión cerrada", "199"),
                                  ("olla al soltar vapor (ejemplo)", "143"))):
        ry = yy + j * 62
        caja(b, x0, ry, ww, 52, c, r=10)
        texto(b, x0 + 18, ry + 33, lab, 17)
        texto(b, x0 + 360, ry + 33, f"presión de afuera: {p} kPa", 16, GRAY)
        texto(b, x0 + 640, ry + 33, "hierve a ______ °C", 17, INK, weight="700")
    yy += 3 * 62 + 10
    yy = frase_hueco(b, x0, yy, ww, "Cuando la presión de afuera baja, la temperatura de ebullición ______________ .", c)
    return ojo(b, x0, yy + 14, ww, "OJO CON LO QUE BUSCA EL COCINERO",
               "El texto dice que suelta vapor para cocinar más rápido. Con tu tabla, revisa: ¿a menos temperatura "
               "las verduras se cocinan más rápido o más despacio? Anótalo en el margen: el enunciado del libro tiene "
               "ahí un problema, pero la pregunta es sobre la temperatura de ebullición.")


# ───────── P5 · hacia el cero absoluto · cómo baja la temperatura ─────────
def i5(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Lo que baja por cada 20 J", c,
                      "Lee en la gráfica de tu libro la temperatura cada 20 J de energía extraída y calcula cuántos grados "
                      "baja en cada tramo. Si los tramos bajan cada vez menos, la curva se está frenando.")
    x0, ww = x + 22, w - 44
    cols = ("ENERGÍA EXTRAÍDA (J)", "0", "20", "40", "60", "80", "100")
    cw = (ww - 230) / 6
    caja(b, x0, yy, ww, 186, c, r=12)
    for k, cl in enumerate(cols):
        xx = x0 + 18 if k == 0 else x0 + 230 + (k - 1) * cw + cw / 2
        rot(b, xx, yy + 32, cl, c, size=13, anchor="start" if k == 0 else "middle")
    texto(b, x0 + 18, yy + 86, "temperatura (°C)", 16)
    texto(b, x0 + 18, yy + 150, "cuánto bajó", 16)
    for k in range(6):
        hueco(b, x0 + 230 + k * cw + 14, yy + 58, cw - 28, 40, c)
        if k < 5:
            hueco(b, x0 + 230 + (k + 0.5) * cw + 18, yy + 122, cw - 36, 40, c)
    yy += 202
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "LAS PARTÍCULAS DEL GAS", c, size=14)
    linea_pista(b, x0 + 20, yy + 70, x0 + ww - 20, "la temperatura mide qué tan rápido se mueven las partículas; cerca de −273 °C se mueven")
    linea_pista(b, x0 + 20, yy + 112, x0 + ww - 20, "si ya casi no se mueven, la energía que todavía se les puede sacar es")
    yy += 166
    yy = frase_hueco(b, x0, yy, ww, "Por cada 20 J la temperatura baja cada vez ________ : la curva se ________ .", c)
    return ojo(b, x0, yy + 14, ww, "−273 °C ES EL PISO",
               "El cero absoluto (0 K = −273 °C) es la temperatura más baja posible. En la escala kelvin, "
               "K = °C + 273: 20 °C son 293 K. Escribe en kelvin la última temperatura de tu tabla.")


# ───────── P6 · el vidrio que se empaña y se aclara ─────────
def i6(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La ventana por dentro y por fuera", c,
                      "Dibuja las flechas del calor entre el aire de adentro, el vidrio y el aire de afuera. Después "
                      "arma la cadena de lo que pasa en dos momentos: cuando aparecen las gotas y cuando se van.")
    x0, ww = x + 22, w - 44
    vx = x0 + 300
    b.append(rect(x0, yy, 280, 260, CALIENTE, r=10))
    b.append(rect(vx + 40, yy, 280, 260, FRIO, r=10))
    b.append(rect(vx, yy - 6, 26, 272, "#DDE8F0", r=3, stroke=VIDRIO, sw=2.4))
    texto(b, x0 + 20, yy + 30, "aire de la habitación", 15, INK, weight="700")
    pista(b, x0 + 20, yy + 52, "tibio y húmedo", size=13)
    texto(b, vx + 60, yy + 30, "afuera, mañana fría", 15, INK, weight="700")
    texto(b, vx + 13, yy + 290, "vidrio", 14, GRAY, anchor="middle")
    pista(b, x0 + 20, yy + 240, "dibuja aquí las flechas", size=13)
    rx = x0 + 660
    rw = x0 + ww - rx
    for k, (rt, l1, l2) in enumerate((("1 · APARECEN LAS GOTAS", "el vapor toca el vidrio, que está", "el vapor pasa a"),
                                      ("2 · SE VAN LAS GOTAS", "con los minutos el vidrio se", "las gotas pasan a"))):
        ry = yy + k * 150
        caja(b, rx, ry, rw, 136, c, r=14)
        rot(b, rx + 18, ry + 28, rt, c, size=14)
        linea_pista(b, rx + 18, ry + 70, rx + rw - 18, l1)
        linea_pista(b, rx + 18, ry + 112, rx + rw - 18, l2)
    yy += 310
    caja(b, x0, yy, ww, 110, c, r=14)
    rot(b, x0 + 20, yy + 30, "NOMBRE DE LOS DOS CAMBIOS", c, size=14)
    linea_pista(b, x0 + 20, yy + 76, x0 + ww / 2 - 20, "de gas a líquido se llama")
    linea_pista(b, x0 + ww / 2 + 20, yy + 76, x0 + ww - 20, "de líquido a gas se llama")
    yy += 126
    return trampa(b, x0, yy, ww, "Un vidrio no es una esponja:",
                  "si una explicación pone al vidrio a chupar o a soltar agua, revisa tu cadena: el agua llegó por el "
                  "aire como vapor y se fue por el aire como vapor. Lo que cambió fue la temperatura del vidrio.", c)


# ───────── P7 · cobre y aluminio · cuál llega primero a 10 °C ─────────
def i7(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El calor que tiene que soltar cada bloque", c,
                      "Para bajar de 120 °C a 10 °C cada bloque tiene que soltar un calor Q = m · c · ΔT. Haz las dos "
                      "cuentas con sus unidades y compara: el que tiene que soltar menos calor termina antes, si los dos "
                      "lo sueltan al mismo ritmo.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (rt, cv, fill) in enumerate((("COBRE", "390", "#F3D9C4"), ("ALUMINIO", "900", "#E3E7EC"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 250, c, r=16)
        b.append(rect(bx + 20, yy + 50, 90, 90, fill, r=6, stroke=VIDRIO, sw=2))
        rot(b, bx + 65, yy + 36, rt, c, size=14, anchor="middle")
        texto(b, bx + 130, yy + 70, f"m = 5 kg    c = {cv} J/(kg · °C)", 16)
        texto(b, bx + 130, yy + 110, "ΔT = 120 °C − 10 °C = ______ °C", 16)
        texto(b, bx + 20, yy + 184, "Q = ____ × ______ × ______ = ____________ J", 17, INK, weight="700")
        pista(b, bx + 20, yy + 228, "para bajar 1 °C suelta: 5 × ______ = ______ J", size=14)
    yy += 266
    caja(b, x0, yy, ww, 106, c, r=14)
    rot(b, x0 + 20, yy + 30, "COMPARA", c, size=14)
    linea_pista(b, x0 + 20, yy + 70, x0 + ww / 2 - 10, "tiene que soltar menos calor el")
    linea_pista(b, x0 + ww / 2 + 10, yy + 70, x0 + ww - 20, "cuántas veces menos:")
    pista(b, x0 + 20, yy + 96, "un calor específico más bajo quiere decir (más / menos) julios por cada grado", size=14)
    yy += 122
    return ojo(b, x0, yy, ww, "EL SUPUESTO ESCONDIDO",
               "Tu comparación vale si los dos bloques pierden calor igual de rápido. Un bloque de aluminio de 5 kg es "
               "más grande que uno de cobre de 5 kg (tiene más superficie). Anótalo como pregunta para la clase; la "
               "pregunta del libro se responde con el calor específico.")


# ───────── P8 · dos termómetros en el salón · convección ─────────
def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El viaje del aire caliente por el salón", c,
                      "Dibuja con flechas el camino que hace el aire: sale caliente de la calefacción, sube, se enfría y "
                      "baja. Después completa la ficha de las tres formas de pasar el calor: cada una necesita algo "
                      "distinto.")
    x0, ww = x + 22, w - 44
    sx, sw_, sh = x0, 460, 300
    caja(b, sx, yy, sw_, sh, VIDRIO, r=8)
    b.append(rect(sx + 30, yy + sh - 50, 90, 40, CALIENTE, r=6, stroke="#C26A3A", sw=2))
    pista(b, sx + 75, yy + sh - 60, "calefacción", size=13, anchor="middle")
    for (tx, ty, lab) in ((sx + sw_ - 70, yy + 40, "termómetro de arriba"), (sx + sw_ - 70, yy + sh - 40, "termómetro de abajo")):
        b.append(rect(tx, ty - 22, 12, 44, "white", r=6, stroke=INK, sw=2))
        b.append(f'<circle cx="{tx + 6}" cy="{ty + 26}" r="9" fill="#E4572E"/>')
        pista(b, tx - 10, ty + 6, lab, size=13, anchor="end")
    rx = x0 + 490
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 140, c, r=14)
    rot(b, rx + 18, yy + 28, "EL AIRE CALIENTE", c, size=14)
    linea_pista(b, rx + 18, yy + 70, rx + rw - 18, "sus partículas están más (juntas / separadas):")
    linea_pista(b, rx + 18, yy + 112, rx + rw - 18, "entonces su densidad es (mayor / menor) y")
    yy2 = yy + 156
    cols = ("FORMA", "¿NECESITA CONTACTO?", "¿SE MUEVE EL MATERIAL?")
    xs = (0, 190, 430)
    for k, cl in enumerate(cols):
        rot(b, rx + 18 + xs[k], yy2 + 14, cl, c, size=12)
    for j, f in enumerate(("conducción", "convección", "radiación")):
        ry = yy2 + 26 + j * 42
        caja(b, rx, ry, rw, 36, c, r=8)
        texto(b, rx + 18, ry + 24, f, 16)
        for xk in xs[1:]:
            marca(b, rx + 18 + xk, ry + 7, "sí", c)
            marca(b, rx + 18 + xk + 70, ry + 7, "no", c)
    yy = max(yy + sh, yy2 + 26 + 3 * 42) + 16
    return frase_hueco(b, x0, yy, ww, "Lo que llevó el calor hasta el techo fue ________________ que se movió hacia arriba.", c)


# ───────── P9 · calorímetro · temperatura de equilibrio ─────────
def i9(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La balanza del calor", c,
                      "En un calorímetro aislado, todo el calor que suelta el cuerpo caliente lo recibe el agua. Primero "
                      "calcula cuántas calorías necesita cada uno por grado; después ubica en la recta dónde crees que "
                      "queda el equilibrio y comprueba con la cuenta.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (rt, m, cc, t0) in enumerate((("EL CUERPO", "2 kg = ______ g", "0,5", "80"),
                                         ("EL AGUA", "3 kg = ______ g", "1", "20"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 150, c, r=16)
        rot(b, bx + 18, yy + 28, f"{rt} · empieza a {t0} °C", c, size=14)
        texto(b, bx + 18, yy + 70, f"masa: {m}      c = {cc} cal/(g · °C)", 16)
        texto(b, bx + 18, yy + 120, "por cada grado: ______ × ______ = ______ cal/°C", 17, INK, weight="700")
    yy += 166
    # la recta de temperaturas
    lx0, lx1, ly = x0 + 60, x0 + ww - 60, yy + 70
    b.append(f'<line x1="{lx0}" y1="{ly}" x2="{lx1}" y2="{ly}" stroke="{INK}" stroke-width="2.4"/>')
    for t in range(0, 101, 10):
        xx = lx0 + t / 100 * (lx1 - lx0)
        b.append(f'<line x1="{xx:.0f}" y1="{ly - 10}" x2="{xx:.0f}" y2="{ly + 10}" stroke="{INK}" stroke-width="1.8"/>')
        b.append(T(xx, ly + 34, [f"{t} °C"], 14, GRAY, anchor="middle"))
    pista(b, x0, yy + 20, "marca con una flecha las dos temperaturas iniciales y con una X dónde crees que quedan los dos", size=14)
    yy += 126
    caja(b, x0, yy, ww, 170, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA CUENTA · LO QUE SUELTA EL CUERPO = LO QUE RECIBE EL AGUA", c, size=14)
    texto(b, x0 + 20, yy + 80, "______ cal/°C × (80 − T)  =  ______ cal/°C × (T − 20)", 18)
    texto(b, x0 + 20, yy + 130, "T = ________ °C", 18, INK, weight="700")
    pista(b, x0 + 260, yy + 130, "¿quedó cerca del que necesita más calorías por grado?  sí / no", size=15)
    yy += 186
    return ojo(b, x0, yy, ww, "OJO CON LAS UNIDADES", "El calor específico viene en cal/(g · °C) y las masas en kg. Pásalas a "
               "gramos antes de multiplicar: si no, las dos unidades no se cancelan.")


# ───────── P10 · la expresión del calor específico ─────────
def i10(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Quién pierde, quién gana y cuánto", c,
                      "Llena la ficha de cada sustancia. Escribe cada cambio de temperatura como «la mayor menos la "
                      "menor», para que salga positivo. Después arma la igualdad, despeja c₂ y calcula su valor.")
    x0, ww = x + 22, w - 44
    cols = ("", "MASA (g)", "c (cal/(g·°C))", "EMPIEZA (°C)", "TERMINA (°C)", "CAMBIO (°C)", "¿PIERDE O GANA?")
    xs = (0, 170, 330, 520, 680, 840, 1010)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=12)
    yy += 26
    for j, s in enumerate(("agua", "el cuerpo")):
        ry = yy + j * 60
        caja(b, x0, ry, ww, 50, c, r=10)
        texto(b, x0 + 16, ry + 32, s, 17, INK, weight="700")
        for k in range(1, 6):
            hueco(b, x0 + xs[k], ry + 6, 120 if k < 5 else 130, 38, c)
        pista(b, x0 + xs[6], ry + 32, "______", size=15)
    yy += 2 * 60 + 14
    caja(b, x0, yy, ww, 200, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA IGUALDAD Y EL DESPEJE", c, size=14)
    texto(b, x0 + 20, yy + 80, "______ × ______ × ______   =   ______ × c₂ × ______", 19)
    pista(b, x0 + 760, yy + 80, "(lo que gana = lo que pierde)", size=14)
    texto(b, x0 + 20, yy + 130, "c₂ = ( ______ × ______ ) ÷ ( ______ × ______ )", 19)
    texto(b, x0 + 20, yy + 180, "c₂ = ________ ÷ ________ = ________ cal/(g · °C)", 19, INK, weight="700")
    yy += 216
    return ojo(b, x0, yy, ww, "CALCULA EL NÚMERO DE CADA OPCIÓN",
               "Antes de marcar, haz la cuenta que propone cada opción y compárala con tu c₂. Si dos opciones te dan el "
               "mismo número, no estás equivocado: escribe por qué en el margen y coméntalo con el profe.")


Q = {1: dict(n=1, est=1, pag=216, ctx="Pared de ladrillo de doble grosor · qué pasa con el calor",
             comp="Uso comprensivo del conocimiento científico", inst=i1),
     2: dict(n=2, est=3, pag=216, ctx="Agua hirviendo lanzada al aire bajo cero · por qué se congela",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=4, pag=216, ctx="El mismo fenómeno en otro lugar · qué condición es indispensable",
             comp="Indagación", inst=i3),
     4: dict(n=4, est=4, pag=217, ctx="Olla a presión que suelta vapor · temperatura de ebullición",
             comp="Explicación de fenómenos", inst=i4),
     5: dict(n=5, est=3, pag=217, ctx="Gas que se enfría hacia el cero absoluto · qué dice la gráfica",
             comp="Indagación", inst=i5),
     6: dict(n=6, est=1, pag=217, ctx="Vidrio que se empaña y luego se aclara · qué proceso",
             comp="Explicación de fenómenos", inst=i6),
     7: dict(n=7, est=2, pag=217, ctx="Cobre y aluminio de 5 kg de 120 °C a 10 °C · cuál llega primero",
             comp="Uso comprensivo del conocimiento científico", inst=i7),
     8: dict(n=8, est=1, pag=218, ctx="Termómetros cerca del suelo y del techo · qué proceso",
             comp="Explicación de fenómenos", inst=i8),
     9: dict(n=9, est=2, pag=218, ctx="Calorímetro · 2 kg a 80 °C con 3 kg de agua a 20 °C",
             comp="Uso comprensivo del conocimiento científico", inst=i9),
     10: dict(n=10, est=2, pag=218, ctx="Calorímetro · expresión del calor específico c₂",
              comp="Uso comprensivo del conocimiento científico", inst=i10)}


def build(pages=(233, 234, 236, 237, 238)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"fis2_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
