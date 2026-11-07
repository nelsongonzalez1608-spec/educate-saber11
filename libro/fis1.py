#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 1 · componente físico · mecánica clásica · páginas 226–232.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 1» de Física (fuente_libro/FÍSICA), páginas 205–208.
Casos: dos bloques en planos de distinto ángulo y su gráfica v–t (1), ciclista que frena en la
arena (2), automóvil que se desliza al soltar el freno de mano (3), bailarín de ballet que gira
540° en el aire (4 a 6), tomate sobre una tabla que se retira de golpe (7), prenda en el tambor
de una lavadora (8), bloque de 5 kg en un plano de 30° unido a otro que cuelga (9), automóvil
que acelera, va constante y frena · qué gráfica v–t (10).

Claves verificadas (resueltas a mano contra el texto y las figuras, 7 nov 2026):

    1·A  2·C  3·B  4·A  5·C  6·B  7·B  8·A  9·D  10·B

Cuentas y razones:
  1 · En una gráfica v–t la pendiente es la aceleración: B pasa de 0 a ≈3,1 m/s en 3 s
      (a ≈ 1,0 m/s²) y A de 0 a ≈1,7 m/s en 3 s (a ≈ 0,57 m/s²). Comparar las pendientes (A) es
      lo único que usa la gráfica. C cambia otra variable (el material); B y D no comparan
      aceleraciones. Ver hallazgo: la gráfica no dice qué bloque va en el plano más inclinado.
  2 · La energía mecánica no se destruye: el rozamiento con la arena hace trabajo negativo y la
      convierte en energía térmica (y algo de sonido) (C). A, B y D invocan cosas que no pasan
      (el peso no cambia, la masa no cambia).
  3 · Con el freno, el rozamiento estático equilibra la componente paralela P·sen θ. Sin freno las
      ruedas giran y el rozamiento que queda es menor que P·sen θ: gana la componente (B). La
      normal (A) y la gravedad (D) no cambian; el rozamiento no «aumenta» (C).
  4 · Para saber si la superficie influye, se cambia solo la superficie y se mide lo que produce
      (el número de giros) (A). D cambia de salón: cambia también la luz, el espacio, el piso… a
      la vez. B y C cambian o miden otra cosa.
  5 · En el aire no hay torque externo apreciable: el momento angular L = I·ω se conserva. Abrir
      las piernas aumenta I y baja ω, lo que da control (C). Ver hallazgo: la pregunta llama
      «equilibrio» a algo que es conservación del momento angular.
  6 · Equilibrio al aterrizar = el centro de masa sobre la base de apoyo. Apoyar los dos pies
      agranda la base (B). C (flexionar más) reduce la fuerza sobre la rodilla al alargar el tiempo
      del choque (impulso): también es defendible si se lee «equilibrio» como «control». Ver
      hallazgo (Media): clave propuesta B; la editorial debe confirmar.
  7 · Al retirar la tabla desaparece la normal; ninguna fuerza horizontal actuó sobre el tomate:
      por inercia conserva su estado y solo cae por su peso (B).
  8 · F_c = m·v²/r. La variable que el experimentador puede mover y que más pesa (al cuadrado)
      es la rapidez de giro (A). B, C y D hablan de cambiar «la dirección» o «el sentido», que no
      es lo que mantiene la prenda pegada.
  9 · W_gravedad sobre A = (m·g·sen 30°) · d = 5 × 9,8 × 0,5 × d = 24,5·d J: la componente del peso
      paralela al plano por la distancia (D). La normal y P·cos 30° no hacen trabajo; la tensión no es la
      gravedad; sumar los pesos (B) mezcla el bloque que cuelga.
 10 · Acelera desde el reposo (recta que sube desde 0), va constante (recta horizontal) y frena
      uniforme hasta 0 (recta que baja hasta 0): solo B (0→2 m/s en 1 s, 2 m/s de 1 a 3 s, 2→0 de
      3 a 5 s).

Reparto: A 3 · B 4 · C 2 · D 1. B concentra 4 de 10 (no llega a la mitad); D una sola vez.
Hallazgos: tablero/propuestas/fis1_hallazgos.csv.

Estrategias:
    1 · Las fuerzas, una por una         (3, 6, 7, 9 · ICFES ASED Mecánica N.º 13)        azul
    2 · La gráfica cuenta el movimiento  (1, 10      · ICFES cuadernillo 2025-2026 N.º 43) rojo
    3 · El experimento justo             (4, 8       · ICFES cuadernillo 2025-2026 N.º 13) oro
    4 · Lo que se conserva               (2, 5       · ICFES cuadernillo 2025-2026 N.º 17) morado

Hojas: 226 fis1_t1 (1-2) · 227 fis1_t2 (3-4) · 228 fis1_i1 · 229 fis1_t3 (5-6) ·
       230 fis1_t4 (7-8) · 231 fis1_t5 (9-10) · 232 fis1_i2.
"""
import math
import re

from taller_base import *

configurar("Física", 1, "físico · mecánica clásica",
           tema="Fuerzas, movimiento y energía",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Las fuerzas, una por una", EDU_AZUL),
       2: ("La gráfica cuenta el movimiento", EDU_ROJO),
       3: ("El experimento justo", EDU_ORO),
       4: ("Lo que se conserva", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))
SUELO = "#7C8A99"          # rampas, mesas y suelo de los dibujos
RELLENO = "#EEF1F6"        # relleno de rampas y bloques


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
    """Casilla para escribir un número."""
    b.append(rect(x, y, w, h, "white", r=8, stroke=c, sw=1.8))
    return x + w


def frase_hueco(b, x, y, w, txt, c, h=56):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [_esp(txt)], 18, INK, weight="700"))
    return y + h


def flecha(b, x1, y1, x2, y2, c, sw=2.6, bend=0.0, head=13):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def marca(b, x, y, txt, c):
    """Casilla de marcar con su rótulo."""
    b.append(checkbox(x, y, s=11, c=c))
    b.append(T(x + 30, y + 18, [txt], 16, GRAY))


def punto(b, cx, cy, c, r=5):
    b.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" fill="{c}"/>')


def ejes(b, x, y, w, h, xlab, ylab, xt=(), yt=()):
    """Ejes de una gráfica con cuadrícula. xt / yt = [(fracción, rótulo)]."""
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


def poligono(b, pts, fill, c=SUELO, sw=2.4):
    b.append(f'<polygon points="{" ".join(f"{px:.0f},{py:.0f}" for px, py in pts)}" fill="{fill}" '
             f'stroke="{c}" stroke-width="{sw}" stroke-linejoin="round"/>')


def rampa(b, x, y, base, ang, c=SUELO, lab=None):
    """Triángulo rectángulo: ángulo `ang` (grados) abajo a la izquierda. Devuelve la punta alta."""
    alto = base * math.tan(math.radians(ang))
    poligono(b, [(x, y), (x + base, y), (x + base, y - alto)], RELLENO, c)
    b.append(f'<path d="M {x + 60} {y} A 60 60 0 0 0 {x + 60 * math.cos(math.radians(ang)):.1f} '
             f'{y - 60 * math.sin(math.radians(ang)):.1f}" fill="none" stroke="{c}" stroke-width="1.8"/>')
    texto(b, x + 72, y - 12, lab or f"{ang}°", 15, GRAY)
    return x + base, y - alto


def bloque_en(b, x, y, ang, s=70, fill="white", c=INK, txt=None):
    """Cuadrado de lado s apoyado sobre la recta de ángulo ang, con la esquina baja en (x, y)."""
    a = math.radians(ang)
    ux, uy = math.cos(a), -math.sin(a)          # a lo largo de la rampa
    nx, ny = -math.sin(a), -math.cos(a)         # perpendicular, hacia afuera
    p = [(x, y), (x + s * ux, y + s * uy), (x + s * ux + s * nx, y + s * uy + s * ny), (x + s * nx, y + s * ny)]
    poligono(b, p, fill, c, 2.4)
    cx = x + s / 2 * ux + s / 2 * nx
    cy = y + s / 2 * uy + s / 2 * ny
    if txt:
        texto(b, cx, cy + 6, txt, 16, INK, weight="700", anchor="middle")
    return cx, cy


# ───────── P1 · dos bloques en planos de distinto ángulo · gráfica v–t ─────────
def i1(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El escalón de cada recta", c,
                      "En una gráfica de velocidad contra tiempo, lo empinada que es la recta dice cuánto gana de "
                      "velocidad el bloque en cada segundo. Dibuja sobre cada recta un escalón: cuánto avanza el "
                      "tiempo y cuánto sube la velocidad. Lee los números en la gráfica de tu libro.")
    x0, ww = x + 22, w - 44
    gx, gy, gw, gh = x0 + 60, yy + 30, 460, 300
    ejes(b, gx, gy, gw, gh, "tiempo (s)", "velocidad (m/s)",
         xt=[(k / 3, str(k)) for k in range(4)], yt=[(k / 4, str(k)) for k in range(5)])
    curva(b, [(gx, gy + gh), (gx + gw, gy + gh - 3.1 / 4 * gh)], RO, sw=3)
    curva(b, [(gx, gy + gh), (gx + gw, gy + gh - 1.7 / 4 * gh)], "#7FA7CF", sw=3)
    texto(b, gx + gw + 10, gy + gh - 3.1 / 4 * gh + 6, "B", 17, RO, weight="700")
    texto(b, gx + gw + 10, gy + gh - 1.7 / 4 * gh + 6, "A", 17, "#4F7FAF", weight="700")
    pista(b, gx + 10, gy + 18, "dibuja aquí los dos escalones", size=13)
    rx = x0 + 600
    rw = x0 + ww - rx
    cols = ("", "Δt (s)", "Δv (m/s)", "Δv ÷ Δt")
    xs = (0, 110, 240, 380)
    for k, cl in enumerate(cols):
        rot(b, rx + xs[k] + (0 if k == 0 else 40), yy + 20, cl, c, size=13)
    for j, bl in enumerate(("Bloque A", "Bloque B")):
        ry = yy + 36 + j * 66
        caja(b, rx, ry, rw, 56, c, r=10)
        texto(b, rx + 16, ry + 35, bl, 17, INK, weight="700")
        for k in (1, 2, 3):
            hueco(b, rx + xs[k] + 10, ry + 9, 110, 38, c)
    pista(b, rx + 4, yy + 186, "la unidad de Δv ÷ Δt es ______ :  ¿qué magnitud es esa?  ______________", size=15)
    caja(b, rx, yy + 206, rw, 128, c, r=14)
    rot(b, rx + 18, yy + 234, "LO QUE LA GRÁFICA DICE Y LO QUE NO DICE", c, size=13)
    pista(b, rx + 18, yy + 268, "sí dice:")
    renglon(b, rx + 90, yy + 270, rx + rw - 18)
    pista(b, rx + 18, yy + 312, "no dice:")
    renglon(b, rx + 90, yy + 314, rx + rw - 18)
    yy = gy + gh + 60
    yy = frase_hueco(b, x0, yy, ww, "El número que me dice cuál bloque gana velocidad más rápido sale de _____________________ .", c)
    return trampa(b, x0, yy + 14, ww, "Un procedimiento puede ser cuidadoso y no responder la pregunta:",
                  "antes de aceptar uno, pregúntale qué número saca y si ese número es una aceleración. Si mide "
                  "otra cosa, o cambia algo distinto del ángulo, no compara lo que se pidió.", c)


# ───────── P2 · el ciclista en la arena · la energía no desaparece ─────────
def i2(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La caja de la energía del ciclista", c,
                      "Antes de la arena el ciclista lleva energía de movimiento. Pinta cada barra hasta donde creas "
                      "que llega, antes y después de detenerse. La regla del juego: la suma de las barras de cada "
                      "momento tiene que dar lo mismo.")
    x0, ww = x + 22, w - 44
    half = (ww - 40) / 2
    for k, (rt, ps) in enumerate((("ANTES · ENTRA A LA ARENA", "va rápido"),
                                  ("DESPUÉS · YA SE DETUVO", "quieto, sobre la arena"))):
        bx = x0 + k * (half + 40)
        caja(b, bx, yy, half, 330, c, r=16)
        rot(b, bx + 18, yy + 30, rt, c, size=14)
        pista(b, bx + 18, yy + 54, ps, size=14)
        base = yy + 270
        for j, lab in enumerate(("de movimiento", "de altura", "otra · ¿cuál?")):
            cx = bx + 60 + j * (half - 80) / 2.4
            b.append(rect(cx, base - 180, 70, 180, "white", r=4, stroke=c, sw=2))
            for t in range(1, 6):
                b.append(f'<line x1="{cx}" y1="{base - t * 30}" x2="{cx + 8}" y2="{base - t * 30}" stroke="{c}" stroke-width="1.4"/>')
            pista(b, cx + 35, base + 24, lab, size=14, anchor="middle")
        renglon(b, bx + 60 + 2 * (half - 80) / 2.4 - 20, base + 48, bx + half - 18)
    yy += 346
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA FUERZA QUE HIZO EL CAMBIO", c, size=14)
    pista(b, x0 + 20, yy + 70, "la fuerza que actuó entre la llanta y la arena se llama:")
    renglon(b, x0 + 430, yy + 72, x0 + ww - 20)
    pista(b, x0 + 20, yy + 118, "¿iba a favor o en contra del movimiento?")
    marca(b, x0 + 330, yy + 100, "a favor", c)
    marca(b, x0 + 460, yy + 100, "en contra", c)
    pista(b, x0 + 620, yy + 118, "¿qué se calienta cuando frenas así?")
    renglon(b, x0 + 900, yy + 120, x0 + ww - 20)
    yy += 166
    return ojo(b, x0, yy, ww, "ABSORBER NO ES BORRAR",
               "Si la barra «otra» te quedó vacía, la suma no te cuadra. Una explicación que deja la "
               "energía sin destino choca con la regla de tu caja, por científica que suene.")


# ───────── P3 · el automóvil que se desliza al soltar el freno ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El diagrama de cuerpo libre en la rampa", c,
                      "Dibuja sobre el carro las fuerzas, cada una con su nombre: el peso hacia el centro de la Tierra, "
                      "la normal perpendicular a la rampa y el rozamiento a lo largo de ella. Después parte el peso "
                      "en dos: una parte a lo largo de la rampa y otra contra la rampa.")
    x0, ww = x + 22, w - 44
    # la rampa con el carro (un bloque)
    rx0, ry0 = x0 + 20, yy + 330
    rampa(b, rx0, ry0, 560, 22, lab="θ")
    a = math.radians(22)
    bx, by = rx0 + 250 * math.cos(a), ry0 - 250 * math.sin(a)
    cx, cy = bloque_en(b, bx, by, 22, s=96)
    texto(b, cx, cy - 16, "carro", 15, INK, weight="700", anchor="middle")
    punto(b, cx, cy, INK, r=5)
    pista(b, rx0, yy + 16, "pon todas las flechas en el punto negro", size=13)
    # columna derecha: con freno y sin freno
    rx = x0 + 640
    rw = x0 + ww - rx
    for k, (rt, ps) in enumerate((("CON EL FRENO PUESTO", "el carro está quieto"),
                                  ("AL SOLTAR EL FRENO", "el carro empieza a bajar"))):
        ry = yy + k * 176
        caja(b, rx, ry, rw, 162, c, r=14)
        rot(b, rx + 18, ry + 28, rt, c, size=14)
        pista(b, rx + 18, ry + 50, ps, size=14)
        pista(b, rx + 18, ry + 90, "a lo largo de la rampa, hacia abajo:")
        renglon(b, rx + 280, ry + 92, rx + rw - 18)
        pista(b, rx + 18, ry + 136, "hacia arriba:")
        renglon(b, rx + 120, ry + 138, rx + rw / 2 + 20)
        pista(b, rx + rw / 2 + 40, ry + 136, "¿quién gana?")
        renglon(b, rx + rw / 2 + 140, ry + 138, rx + rw - 18)
    yy += 2 * 176 + 4
    caja(b, x0, yy, ww, 70, c, r=12)
    pista(b, x0 + 20, yy + 42, "Al soltar el freno, ¿cambiaron la masa, el ángulo o la gravedad?")
    marca(b, x0 + 560, yy + 24, "sí", c)
    marca(b, x0 + 640, yy + 24, "no", c)
    pista(b, x0 + 720, yy + 42, "entonces la fuerza que cambió fue:")
    renglon(b, x0 + 990, yy + 44, x0 + ww - 20)
    yy += 86
    return ojo(b, x0, yy, ww, "EL DIBUJO DE TU LIBRO PINTA LAS DOS PARTES DEL PESO HACIA ABAJO",
               "En la figura del libro las dos partes del peso salen verticales y la normal también. En tu "
               "diagrama, una parte va a lo largo de la rampa y la otra se mete contra ella; la normal sale "
               "perpendicular a la rampa, del mismo tamaño que la parte que se mete contra ella.")


# ───────── P4 · el bailarín · qué procedimiento investiga la superficie ─────────
def i4(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La ficha del experimento justo", c,
                      "Un experimento justo cambia una sola cosa a propósito, mide lo que pasa y deja quieto todo lo "
                      "demás. Llena la ficha para la pregunta del bailarín y después pasa cada procedimiento de las "
                      "opciones por los tres filtros.")
    x0, ww = x + 22, w - 44
    filas = (("LO QUE CAMBIO A PROPÓSITO", "lo que la pregunta quiere investigar"),
             ("LO QUE MIDO", "lo que el texto dice que mejora con más impulso"),
             ("LO QUE DEJO IGUAL", "escribe por lo menos tres cosas"))
    lw = max(tw(f[0], 14, "700") + 1.5 * len(f[0]) for f in filas) + 40
    for k, (rt, ps) in enumerate(filas):
        ry = yy + k * 74
        caja(b, x0, ry, ww, 64, c, r=12)
        b.append(rect(x0, ry, 8, 64, c, r=4))
        rot(b, x0 + 24, ry + 28, rt, c, size=14)
        pista(b, x0 + 24, ry + 52, ps, size=13)
        renglon(b, x0 + lw + 20, ry + 46, x0 + ww - 20)
    yy += 3 * 74 + 16
    cols = ("OPCIÓN", "¿CAMBIA SOLO LO QUE ESCRIBÍ ARRIBA?", "¿MIDE LO QUE ESCRIBÍ ARRIBA?", "¿DEJA LO DEMÁS IGUAL?")
    xs = (0, 140, 520, 860)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=13)
    yy += 26
    for j, L in enumerate("ABCD"):
        ry = yy + j * 56
        caja(b, x0, ry, ww, 46, c, r=10)
        b.append(f'<circle cx="{x0 + 40}" cy="{ry + 23}" r="15" fill="white" stroke="{c}" stroke-width="2"/>')
        texto(b, x0 + 40, ry + 29, L, 16, c, weight="700", anchor="middle")
        for xk in xs[1:]:
            marca(b, x0 + xk, ry + 12, "sí", c)
            marca(b, x0 + xk + 80, ry + 12, "no", c)
    yy += 4 * 56 + 8
    return trampa(b, x0, yy, ww, "Cambiar de lugar puede cambiar diez cosas a la vez:",
                  "si un procedimiento mueve lo que querías estudiar junto con otras condiciones, no sabrás cuál "
                  "de ellas produjo el resultado. Ese procedimiento no pasa el tercer filtro.", c)


# ───────── P5 · el bailarín en el aire · momento angular ─────────
def figura(b, cx, cy, abierta, c):
    """Silueta de palitos de un bailarín visto de frente: brazos y piernas abiertos o cerrados."""
    b.append(f'<circle cx="{cx}" cy="{cy - 92}" r="18" fill="white" stroke="{c}" stroke-width="3"/>')
    curva(b, [(cx, cy - 74), (cx, cy + 10)], c, sw=4)
    if abierta:
        curva(b, [(cx - 80, cy - 70), (cx, cy - 50), (cx + 80, cy - 70)], c, sw=4)
        curva(b, [(cx - 70, cy + 90), (cx, cy + 10), (cx + 70, cy + 90)], c, sw=4)
    else:
        curva(b, [(cx - 14, cy - 10), (cx, cy - 50), (cx + 14, cy - 10)], c, sw=4)
        curva(b, [(cx - 12, cy + 96), (cx, cy + 10), (cx + 12, cy + 96)], c, sw=4)
    b.append(f'<line x1="{cx}" y1="{cy - 130}" x2="{cx}" y2="{cy + 116}" stroke="{GRAY}" stroke-width="1.6" '
             f'stroke-dasharray="6,6"/>')


def i5(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La regla del giro en el aire", c,
                      "En el aire nadie empuja al bailarín, así que su cantidad de giro se mantiene. Lo que sí puede "
                      "hacer es acomodar el cuerpo: alejar o acercar la masa del eje. Mira las dos siluetas y completa "
                      "la regla antes de leer las opciones.")
    x0, ww = x + 22, w - 44
    yy = alto_profe(b, x0, yy, ww,
                    "Momento angular: L = I · ω. I mide qué tan lejos del eje está repartida la masa (inercia de "
                    "giro) y ω es qué tan rápido gira. Si ninguna fuerza externa lo hace girar, L se conserva: si I "
                    "sube, ω baja, y al revés. El profe lo muestra en una silla que gira con los brazos abiertos y "
                    "cerrados.") + 18
    for k, (ab, rt) in enumerate(((True, "BRAZOS Y PIERNAS ABIERTOS"), (False, "BRAZOS Y PIERNAS CERRADOS"))):
        fx = x0 + 120 + k * 300
        figura(b, fx, yy + 150, ab, c)
        rot(b, fx, yy + 300, rt, c, size=12, anchor="middle")
    pista(b, x0 + 60, yy + 16, "la raya punteada es el eje del giro", size=13)
    rx = x0 + 640
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 300, c, r=14)
    rot(b, rx + 18, yy + 30, "COMPLETA LA REGLA", c, size=14)
    for j, (lab, op) in enumerate((("abierto, la masa queda", "(cerca / lejos) del eje"),
                                   ("abierto, I es", "(grande / pequeño)"),
                                   ("abierto, gira", "(más rápido / más lento)"),
                                   ("en el aire, ¿alguien lo empuja?", "(sí / no)"))):
        ry = yy + 74 + j * 56
        pista(b, rx + 18, ry, lab)
        renglon(b, rx + 18 + tw(lab, 15, style="italic") + 12, ry + 2, rx + rw - 190)
        pista(b, rx + rw - 18, ry, op, size=13, anchor="end")
    yy += 318
    return frase_hueco(b, x0, yy, ww, "En el aire, lo que se mantiene igual de principio a fin es ______________________ .", c)


# ───────── P6 · el aterrizaje de pie · base de apoyo ─────────
def huella(b, cx, cy, c, ang=0):
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="22" ry="48" fill="white" stroke="{c}" stroke-width="2.4" '
             f'transform="rotate({ang} {cx} {cy})"/>')


def i6(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Los pies vistos desde arriba", c,
                      "Alguien se mantiene de pie si la vertical que baja de su centro de masa cae dentro de la zona "
                      "que encierran sus apoyos (la base). Encierra con una línea la base en cada caso y marca con un "
                      "punto dónde puede caer el centro de masa sin que se vaya al suelo.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (rt, dos) in enumerate((("UN SOLO PIE", False), ("LOS DOS PIES", True))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 250, c, r=16)
        rot(b, bx + 18, yy + 30, rt, c, size=14)
        mx = bx + half / 2
        if dos:
            huella(b, mx - 70, yy + 140, c, -10)
            huella(b, mx + 70, yy + 140, c, 10)
        else:
            huella(b, mx, yy + 140, c)
        pista(b, bx + 18, yy + 232, "la base es (grande / pequeña):", size=14)
        renglon(b, bx + 230, yy + 234, bx + half - 18)
    yy += 266
    caja(b, x0, yy, ww, 196, c, r=14)
    rot(b, x0 + 20, yy + 30, "PARA QUÉ SIRVE CADA ACCIÓN · ESCRÍBELO ANTES DE ELEGIR", c, size=14)
    for j, lab in enumerate(("agrandar la base de apoyo sirve para", "doblar más la rodilla sirve para",
                             "subir los brazos sirve para")):
        ry = yy + 74 + j * 44
        pista(b, x0 + 20, ry, lab)
        renglon(b, x0 + 20 + tw(lab, 15, style="italic") + 12, ry + 2, x0 + ww - 20)
    yy += 212
    return trampa(b, x0, yy, ww, "Una acción puede cuidar la rodilla y no el equilibrio:",
                  "la pregunta pide equilibrio al llegar al suelo. Si lo que escribiste para una acción no habla de "
                  "no caerse, anótalo y discútelo con el profe antes de marcar.", c)


# ───────── P7 · el tomate y la tabla · inercia ─────────
def i7(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Tres fotos del tomate", c,
                      "Dibuja en cada foto las fuerzas que actúan sobre el tomate, con su nombre. Una fuerza siempre "
                      "la hace algo que lo toca o la Tierra. Si en una foto nada lo toca, solo queda una.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 24
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("1 · QUIETO SOBRE LA TABLA", "antes del golpe"),
                                  ("2 · LA TABLA BAJA DE GOLPE", "la tabla se va"),
                                  ("3 · YA SIN TABLA", "cayendo al recipiente"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 300, c, r=16)
        rot(b, bx + 18, yy + 30, rt, c, size=13)
        pista(b, bx + 18, yy + 52, ps, size=13)
        mx = bx + bw / 2
        ty = yy + 150 if k < 2 else yy + 130
        b.append(f'<circle cx="{mx:.0f}" cy="{ty}" r="26" fill="#F7D9D4" stroke="{EDU_ROJO}" stroke-width="2.4"/>')
        if k == 0:
            b.append(rect(mx - 110, ty + 26, 220, 16, RELLENO, r=3, stroke=SUELO, sw=2))
        elif k == 1:
            b.append(rect(mx - 110, ty + 76, 220, 16, RELLENO, r=3, stroke=SUELO, sw=2))
            flecha(b, mx + 130, ty + 40, mx + 130, ty + 100, SUELO, sw=2.4)
        else:
            b.append(rect(mx - 70, yy + 210, 140, 60, "white", r=8, stroke=SUELO, sw=2))
            pista(b, mx, yy + 246, "recipiente", size=13, anchor="middle")
        pista(b, bx + 18, yy + 290, "fuerzas: __________________", size=14)
    yy += 316
    caja(b, x0, yy, ww, 110, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PRUEBA DE LA FUERZA HACIA ADELANTE", c, size=14)
    pista(b, x0 + 20, yy + 70, "¿en alguna foto dibujaste una fuerza horizontal sobre el tomate?")
    marca(b, x0 + 520, yy + 52, "sí", c)
    marca(b, x0 + 600, yy + 52, "no", c)
    pista(b, x0 + 680, yy + 70, "¿qué la haría?")
    renglon(b, x0 + 790, yy + 72, x0 + ww - 20)
    pista(b, x0 + 20, yy + 100, "si nada lo empujó de lado, el tomate conserva lo que hacía antes, que era:", size=14)
    renglon(b, x0 + 560, yy + 102, x0 + ww - 20)
    yy += 126
    return ojo(b, x0, yy, ww, "EL GOLPE LO RECIBE LA TABLA",
               "Lo que golpea la persona es el borde de la tabla. Para que el golpe moviera al tomate, algo tendría "
               "que tocarlo y empujarlo: búscalo en tus fotos antes de aceptar una explicación con empujones.")


# ───────── P8 · la prenda en la lavadora · qué variable modificar ─────────
def i8(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La fórmula escoge la variable", c,
                      "La fuerza que mantiene la prenda contra el tambor es la fuerza centrípeta. Mira de qué depende "
                      "en la fórmula y calcula qué pasa si duplicas cada cosa. La variable que conviene modificar es la "
                      "que puedes mover con un botón y que cambia mucho la fuerza.")
    x0, ww = x + 22, w - 44
    yy = alto_profe(b, x0, yy, ww,
                    "Fuerza centrípeta: F = m · v² ÷ r. Apunta siempre hacia el centro del giro. m es la masa de la "
                    "prenda, v su rapidez y r el radio del tambor. El profe muestra por qué la v va al cuadrado: "
                    "al doble de rapidez, cuatro veces la fuerza.") + 18
    cols = ("VARIABLE", "¿APARECE EN F?", "SI LA DUPLICO, F SE MULTIPLICA POR", "¿SE PUEDE MOVER CON UN BOTÓN?")
    xs = (0, 260, 500, 900)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=13)
    yy += 26
    for j, v in enumerate(("m · masa de la prenda", "v · rapidez de giro", "r · radio del tambor",
                           "el color o el tipo de tela")):
        ry = yy + j * 58
        caja(b, x0, ry, ww, 48, c, r=10)
        texto(b, x0 + 16, ry + 31, v, 17)
        marca(b, x0 + xs[1], ry + 13, "sí", c)
        marca(b, x0 + xs[1] + 80, ry + 13, "no", c)
        texto(b, x0 + xs[2] + 30, ry + 32, "× ______", 18)
        marca(b, x0 + xs[3], ry + 13, "sí", c)
        marca(b, x0 + xs[3] + 80, ry + 13, "no", c)
    yy += 4 * 58 + 10
    yy = frase_hueco(b, x0, yy, ww, "Para saber si la prenda queda más pegada, ¿mido el tamaño o la dirección de la fuerza? ____________", c)
    return ojo(b, x0, yy + 14, ww, "EN EL DIBUJO DE TU LIBRO LA FLECHA SALE DEL CENTRO",
               "La prenda aparece en el medio y la flecha de la fuerza centrípeta apunta hacia el borde. Es al revés: la "
               "prenda va pegada a la pared del tambor y la fuerza apunta hacia el centro.")


# ───────── P9 · el bloque de 5 kg en el plano de 30° · trabajo de la gravedad ─────────
def i9(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Solo trabaja lo que va a lo largo", c,
                      "Una fuerza hace trabajo con la parte de ella que va en la dirección en que se mueve el bloque. "
                      "Parte el peso del bloque en sus dos componentes, decide cuál va a lo largo del plano y haz la "
                      "cuenta con una distancia de prueba de 2 m.")
    x0, ww = x + 22, w - 44
    yy = alto_profe(b, x0, yy, ww,
                    "En una rampa de 30°, la parte del peso que va a lo largo del plano es P · sen 30° y la que se mete "
                    "contra el plano es P · cos 30°. sen 30° = 0,5 y cos 30° ≈ 0,87. El profe dibuja el triángulo del "
                    "peso para que se vea de dónde salen.") + 18
    rx0, ry0 = x0 + 20, yy + 260
    rampa(b, rx0, ry0, 430, 30)
    a = math.radians(30)
    cx, cy = bloque_en(b, rx0 + 170 * math.cos(a), ry0 - 170 * math.sin(a), 30, s=84)
    texto(b, cx, cy - 14, "5 kg", 15, INK, weight="700", anchor="middle")
    punto(b, cx, cy + 6, INK)
    pista(b, rx0, yy + 14, "dibuja P y sus dos partes desde el punto", size=13)
    rx = x0 + 520
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 250, c, r=14)
    rot(b, rx + 18, yy + 30, "LA CUENTA (g = 9,8 m/s²)", c, size=14)
    for j, t in enumerate(("el peso:  P = m · g = ______ × 9,8 = ________ N",
                           "a lo largo:  P × 0,5 = ______ N        contra el plano:  P × 0,87 = ______ N",
                           "el trabajo:  (la que va a lo largo) × d = ________ × 2 m = ________ J")):
        texto(b, rx + 18, yy + 80 + j * 52, t, 17)
    pista(b, rx + 18, yy + 232, "la unidad N · m tiene otro nombre: ______", size=14)
    yy += 266
    cols = ("FUERZA SOBRE EL BLOQUE", "¿ES DE LA GRAVEDAD?", "¿VA A LO LARGO DEL PLANO?")
    xs = (0, 420, 800)
    for k, cl in enumerate(cols):
        rot(b, x0 + xs[k], yy + 14, cl, c, size=13)
    yy += 24
    for j, f in enumerate(("parte del peso a lo largo del plano", "parte del peso contra el plano",
                           "normal · la hace el plano", "tensión · la hace la cuerda")):
        ry = yy + j * 50
        caja(b, x0, ry, ww, 42, c, r=10)
        texto(b, x0 + 16, ry + 28, f, 16)
        for xk in xs[1:]:
            marca(b, x0 + xk, ry + 10, "sí", c)
            marca(b, x0 + xk + 80, ry + 10, "no", c)
    return yy + 4 * 50


# ───────── P10 · acelera, va constante, frena · qué gráfica v–t ─────────
def i10(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dibujo la historia antes de mirar las gráficas", c,
                      "Parte la historia del automóvil en tres tramos y dibuja en cada cajita la forma que tiene la "
                      "velocidad en ese tramo. Después une los tres en la gráfica grande, en orden. Solo entonces "
                      "busca entre las cuatro la que se parece a la tuya.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 24
    bw = (ww - gap * (n - 1)) / n
    for k, (rt, ps) in enumerate((("TRAMO 1", "acelera desde el reposo"), ("TRAMO 2", "velocidad constante"),
                                  ("TRAMO 3", "frena parejo hasta detenerse"))):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 210, c, r=16)
        rot(b, bx + 18, yy + 30, rt, c, size=14)
        pista(b, bx + 100, yy + 30, ps, size=14)
        ejes(b, bx + 50, yy + 56, bw - 90, 100, "t", "v")
        pista(b, bx + 18, yy + 200, "empieza en v = ____   termina en v = ____", size=13)
    yy += 230
    gx, gy, gw, gh = x0 + 60, yy + 30, 560, 200
    ejes(b, gx, gy, gw, gh, "tiempo", "velocidad")
    pista(b, gx + 20, gy + 20, "la historia completa, en orden", size=13)
    rx = x0 + 680
    rw = x0 + ww - rx
    caja(b, rx, yy + 10, rw, 230, c, r=14)
    rot(b, rx + 18, yy + 40, "LO QUE TIENE QUE TENER LA GRÁFICA", c, size=13)
    for j, lab in enumerate(("cómo empieza:", "cuántos tramos rectos:", "cómo es el tramo del medio:",
                             "cómo termina:")):
        ry = yy + 84 + j * 44
        pista(b, rx + 18, ry, lab)
        renglon(b, rx + 18 + tw(lab, 15, style="italic") + 12, ry + 2, rx + rw - 18)
    yy += 290
    return ojo(b, x0, yy, ww, "UNA DE LAS GRÁFICAS DE TU LIBRO TRAE MAL EL EJE",
               "En la gráfica C el eje vertical dice 2,0 · 1,5 · 1,0 · 1,5 · 0,0: el cuarto número debería ser 0,5. "
               "No cambia lo que hay que buscar: la forma de la línea.")


Q = {1: dict(n=1, est=2, pag=205, ctx="Dos bloques en planos de distinto ángulo · gráfica v–t · qué procedimiento",
             comp="Indagación", inst=i1),
     2: dict(n=2, est=4, pag=205, ctx="Ciclista que se detiene en la arena · por qué la conclusión es incorrecta",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=1, pag=205, ctx="Automóvil en un plano inclinado · por qué se desliza sin el freno",
             comp="Explicación de fenómenos", inst=i3),
     4: dict(n=4, est=3, pag=206, ctx="Bailarín · cómo investigar si la superficie influye en el impulso",
             comp="Indagación", inst=i4),
     5: dict(n=5, est=4, pag=206, ctx="Bailarín que gira 540° en el aire · qué lo mantuvo estable",
             comp="Explicación de fenómenos", inst=i5),
     6: dict(n=6, est=1, pag=206, ctx="Bailarín que aterriza · qué acción ayuda al equilibrio",
             comp="Explicación de fenómenos", inst=i6),
     7: dict(n=7, est=1, pag=207, ctx="Tomate sobre una tabla que baja de golpe · inercia",
             comp="Explicación de fenómenos", inst=i7),
     8: dict(n=8, est=3, pag=207, ctx="Prenda en el tambor de una lavadora · qué variable modificar",
             comp="Indagación", inst=i8),
     9: dict(n=9, est=1, pag=207, ctx="Bloque de 5 kg en un plano de 30° · trabajo de la gravedad",
             comp="Uso comprensivo del conocimiento científico", inst=i9),
     10: dict(n=10, est=2, pag=208, ctx="Acelera, va constante y frena · qué gráfica v–t",
              comp="Uso comprensivo del conocimiento científico", inst=i10)}


def build(pages=(226, 227, 229, 230, 231)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"fis1_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
