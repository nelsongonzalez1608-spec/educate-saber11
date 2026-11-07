#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 5 · componente físico · mecánica clásica · páginas 254–260.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 5» de Física (fuente_libro/FÍSICA), páginas 247–250.
Contenido: energía mecánica en sistemas reales. Una herramienta en la Tierra y en Marte (1),
una central mareomotriz en el laboratorio (2), los relojes del GPS (3), un dron que reparte
paquetes en Bogotá (4 a 7) y un sifón hecho con dos vasos y un pitillo (8 a 10).

Claves verificadas (resueltas a mano, con cuentas y unidades, 7 nov 2026):

    1·C  2·B  3·A  4·B  5·C  6·A  7·B  8·A  9·D  10·A

  1 · C: la herramienta (10 kg) está a 2 m. Tierra: Ep = 10 kg · 10 m/s² · 2 m = 200 J.
      Marte: Ep = 10 kg · 4 m/s² · 2 m = 80 J. Diferencia = 120 J. (Con 9,8 y 3,7 daría
      196 − 74 = 122 J: la misma opción.) D (196 J) es la Ep en la Tierra con g = 9,8; B (98 J) y
      A (49 J) son la mitad y la cuarta parte. Los 80 kg del astronauta no intervienen.
      Hallazgo (Baja): el libro dice que el astronauta «pesa 80 kg» (el peso se mide en newtons).
  2 · B: para saber cómo influye la altura del agua hay que cambiar solo la altura y dejar fija la
      velocidad del flujo (y la posición de la turbina). A cambia dos variables a la vez; C cambia
      otra variable; D no controla nada y escoge los datos.
  3 · A: el enunciado ya da la causa (el reloj en órbita está donde el campo gravitacional es más
      débil): en la superficie el campo es más intenso y el tiempo transcurre más despacio. B, C y D
      ponen otra causa (presión, velocidad que «acelera» el reloj, fuerza eléctrica). Atención: el
      principio (relatividad general) no se nombra; además, en el GPS real la velocidad del satélite
      ATRASA su reloj (relatividad especial, unos 7 μs por día) y la gravedad lo adelanta (unos
      45 μs): la C dice lo contrario de lo que hace la velocidad.
  4 · B: g = 10 m/s². Piso 20: Ep = 3 · 10 · 60 = 1800 J; Ec = ½ · 3 · 8² = 96 J; Em = 1896 J.
      Piso 5: Ep = 3 · 10 · 15 = 450 J; Ec = ½ · 3 · 5² = 37,5 J; Em = 487,5 J.
      Diferencia = 1408,5 J > 1000 J (con g = 9,8: 1860 − 478,5 = 1381,5 J). A, C y D se caen con
      la cuenta. Hallazgo (Baja): las rapideces son «promedio en los trayectos horizontales», no en
      el momento de la entrega; solo con la Ep la diferencia ya es 1350 J, la clave no cambia.
  5 · C: proporción directa: 90.000 J / 30 m = 3000 J/m → 3000 J/m · 75 m = 225.000 J (o bien
      75/30 = 2,5 veces → 90.000 · 2,5). A, B y D no salen de la proporción.
  6 · A: W = F · d · cos θ. Al acelerar, la fuerza del dron empuja en la dirección del movimiento y
      el paquete gana ΔEc = ½ · 3 kg · (8² − 5²) m²/s² = 58,5 J. Sostenido quieto, d = 0 → W = 0.
      B, C y D confunden esfuerzo (gasto de batería) con trabajo sobre el paquete.
  7 · B: la energía de la batería que no quedó como Ep o Ec del paquete se disipó como calor y
      sonido (aire, fricción interna de los motores, también el calor de la propia batería). A, C y
      D contradicen la conservación.
  8 · A: con un solo ensayo, con agua, no se puede afirmar «cualquier líquido, en cualquier
      condición». Hallazgo (Media): la D («parcial», solo vasos del mismo tamaño) también señala
      algo que no se probó; la A es la mejor porque ataca la generalización a «cualquier líquido»
      (un líquido muy viscoso no fluye igual), pero las dos son críticas válidas.
  9 · D: la presión atmosférica empuja el agua por el brazo corto y la gravedad sobre la columna
      más larga la hace bajar. A dice «solo de la masa y no de la altura»; B dice que la energía
      potencial «desaparece»; C usa la tercera ley con el vaso de abajo. Atención: el modelo que se
      enseña en física (Bernoulli, conservación de la energía en el fluido) es el que la B nombra
      mal; ninguna opción lo dice bien, la D es la única sin error.
 10 · A: gravedad hacia abajo, presión atmosférica sobre la superficie del vaso de arriba y rozamiento
      (viscosidad) en el pitillo. B, C y D traen fuerzas que no existen aquí (centrífuga, flotación
      que «equilibra») o direcciones al revés. Atención: «resistencia del aire» dentro de un pitillo
      lleno de agua no aplica; lo que frena es la fricción del agua con las paredes.

Reparto: A 4 (3, 6, 8, 10) · B 3 (2, 4, 7) · C 2 (1, 5) · D 1 (9). La D sale una sola vez.
Registrado como Atención en tablero/propuestas/fis5_hallazgos.csv.

Estrategias:
    1 · Cada magnitud con su fórmula y su unidad   (1, 4, 5  · ICFES 2016-1 2.ª ses. N.º 79)   azul
    2 · ¿Quién empuja y hacia dónde?               (6, 10    · ICFES 2016-1 2.ª ses. N.º 52)   rojo
    3 · Una variable a la vez                      (2, 8     · ICFES 2016-1 1.ª ses. N.º 106)  morado
    4 · El principio que explica lo que se ve      (3, 7, 9  · ICFES cuadernillo 2025 N.º 26)  oro

Hojas: 254 fis5_t1 (1-2) · 255 fis5_t2 (3-4) · 256 fis5_i1 · 257 fis5_t3 (5-6) ·
       258 fis5_t4 (7-8) · 259 fis5_t5 (9-10) · 260 fis5_i2.
"""
from taller_base import *

configurar("Física", 5, "físico · mecánica clásica",
           tema="La energía que sube, que corre y que se escapa",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Cada magnitud con su fórmula y su unidad", EDU_AZUL),
       2: ("¿Quién empuja y hacia dónde?", EDU_ROJO),
       3: ("Una variable a la vez", MORADO),
       4: ("El principio que explica lo que se ve", EDU_ORO)}
usar_estrategias(EST)
AZ, RO, MO, OR = (EST[k][1] for k in (1, 2, 3, 4))


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def texto(b, x, y, txt, size=17, color=INK, weight="400", anchor="start"):
    b.append(T(x, y, [txt], size, color, weight=weight, anchor=anchor))


def sino(b, x, y, c, labels=("sí", "no"), gap=80):
    for j, lab in enumerate(labels):
        b.append(checkbox(x + j * gap, y, s=10, c=c))
        b.append(T(x + 28 + j * gap, y + 17, [lab], 16, GRAY))


def tinte(c, k=0.9):
    from taller_base import _mezcla
    return _mezcla(c, k)


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12, bend=0.0):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def vector(b, x1, y1, x2, y2, c, sw=3.2, head=14):
    """Flecha recta (vector de fuerza o velocidad)."""
    import math as _m
    a = _m.atan2(y2 - y1, x2 - x1)
    b.append(line(x1, y1, x2, y2, c, sw))
    for s in (-1, 1):
        aa = a + _m.pi + s * 0.45
        b.append(line(x2, y2, x2 + head * _m.cos(aa), y2 + head * _m.sin(aa), c, sw))


def tabla_vacia(b, x, y, cols, heads, filas, c, rh=58, hh=48, size=17, sin_renglon=()):
    """Tabla con encabezado tinte y primera columna con rótulos; el resto, renglones."""
    ww = sum(cols)
    caja(b, x, y, ww, hh, c, fill=tinte(c), r=8)
    cx = x
    for k, hd in enumerate(heads):
        if hd:
            rot(b, cx + 14, y + hh / 2 + 6, hd, c, size=14)
        cx += cols[k]
    ry = y + hh
    for f in filas:
        caja(b, x, ry, ww, rh, c, r=0)
        texto(b, x + 14, ry + rh / 2 + 6, f, size=size, weight="700")
        cx = x + cols[0]
        for k in range(1, len(cols)):
            if k not in sin_renglon:
                renglon(b, cx + 14, ry + rh - 16, cx + cols[k] - 14)
            cx += cols[k]
        ry += rh
    cx = x
    for k in range(len(cols) - 1):
        cx += cols[k]
        b.append(line(cx, y, cx, ry, c, 1.6))
    return ry


def caja_preg(b, x, y, w, h, c, tit, ps, lineas=1):
    """Recuadro con rótulo, una pregunta corta y renglones para responder."""
    caja(b, x, y, w, h, c, r=14)
    rot(b, x + 16, y + 28, tit, c, size=14)
    svg, yy = TJ(x + 16, y + 40, ps, w - 32, 16, INK, lh=22)
    b.append(svg)
    for k in range(lineas):
        renglon(b, x + 16, y + h - 18 - k * 40, x + w - 16)
    return y + h


# ───────── P1 · Tierra y Marte · energía potencial ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos planetas, la misma herramienta", c,
                      "La energía potencial gravitatoria se calcula con Ep = m · g · h. Antes de multiplicar, decide "
                      "qué masa usar: el enunciado trae dos. Usa los valores redondeados que pide el libro.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 96, c, r=14)
    pista(b, x0 + 20, yy + 36, "¿Qué objeto está a 2 m de altura?")
    renglon(b, x0 + 280, yy + 38, x0 + ww / 2 - 20)
    pista(b, x0 + ww / 2, yy + 36, "entonces su masa es")
    renglon(b, x0 + ww / 2 + 160, yy + 38, x0 + ww - 120)
    texto(b, x0 + ww - 100, yy + 36, "kg", size=17, weight="700")
    pista(b, x0 + 20, yy + 78, "el otro dato de masa, ¿para qué sirve aquí?")
    renglon(b, x0 + 340, yy + 80, x0 + ww - 20)
    yy += 116
    cols = (230, 170, 200, 170, ww - 770)
    yy = tabla_vacia(b, x0, yy, cols, ("LUGAR", "m (kg)", "g (m/s²)", "h (m)", "Ep = m · g · h (J)"),
                     ("Tierra", "Marte", "Diferencia"), c, rh=66)
    yy += 20
    caja(b, x0, yy, ww, 74, c, r=14, fill=tinte(c, 0.94))
    rot(b, x0 + 20, yy + 30, "LA UNIDAD TAMBIÉN SE MULTIPLICA", c)
    texto(b, x0 + 20, yy + 60, "kg  ·  m/s²  ·  m  =", size=19, weight="700")
    renglon(b, x0 + 240, yy + 62, x0 + 520)
    texto(b, x0 + 540, yy + 60, "=  joule (J)", size=19, weight="700")
    pista(b, x0 + 700, yy + 60, "¿qué unidades quedan antes de llamarlo joule?")
    yy += 94
    return ojo(b, x0, yy, ww, "EL PESO NO SE MIDE EN KILOGRAMOS",
               "El libro dice que el astronauta «pesa 80 kg». Los kilogramos miden la masa; el peso es una fuerza y "
               "se mide en newtons: en la Tierra, 80 kg × 10 m/s² = 800 N. En Marte la masa sigue siendo 80 kg, "
               "pero el peso cambia.")


# ───────── P2 · central mareomotriz · control de variables ─────────
def i2(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El tablero de control del canal", c,
                      "Un experimento confiable mueve una sola perilla a la vez. Escribe cada variable del canal en su "
                      "columna: la que cambio a propósito, las que dejo quietas y la que mido al final.")
    x0, ww = x + 22, w - 44
    vars_ = ("altura del agua", "velocidad del flujo", "posición de la turbina", "energía que genera",
             "tamaño del canal")
    cx = x0
    for v in vars_:
        wv = tw(v, 16, "700") + 34
        caja(b, cx, yy, wv, 40, c, r=20, fill=tinte(c, 0.92))
        texto(b, cx + 17, yy + 26, v, size=16, weight="700")
        cx += wv + 14
    yy += 60
    cw = (ww - 2 * 24) / 3
    cols = (("LA QUE CAMBIO", "variable independiente"), ("LAS QUE DEJO FIJAS", "variables controladas"),
            ("LA QUE MIDO", "variable dependiente"))
    for k, (t1, t2) in enumerate(cols):
        bx = x0 + k * (cw + 24)
        caja(b, bx, yy, cw, 220, c, r=14, sw=2.4)
        # perilla
        b.append(f'<circle cx="{bx + cw - 40}" cy="{yy + 36}" r="18" fill="white" stroke="{c}" stroke-width="2.4"/>')
        b.append(line(bx + cw - 40, yy + 36, bx + cw - 40 + 12 * (k - 1), yy + 22, c, 3))
        rot(b, bx + 16, yy + 30, t1, c)
        pista(b, bx + 16, yy + 54, t2)
        for j in range(3):
            renglon(b, bx + 16, yy + 104 + j * 44, bx + cw - 16)
    yy += 240
    caja(b, x0, yy, ww, 110, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA PRUEBA DEL CRÉDITO", c)
    pista(b, x0 + 20, yy + 62, "Si cambio dos perillas a la vez y la energía sube, ¿a cuál de las dos le doy el crédito?")
    renglon(b, x0 + 20, yy + 96, x0 + ww - 20)
    yy += 128
    return trampa(b, x0, yy, ww, "Muchos datos no es lo mismo que datos confiables:",
                  "si en cada medición cambian varias cosas, o si se anotan solo los números que convienen, ya no se "
                  "puede saber qué causó la diferencia. Antes de marcar, revisa en cada procedimiento cuántas perillas "
                  "se mueven.", c)


# ───────── P3 · relojes del GPS ─────────
def i3(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Dos relojes a distinta distancia de la Tierra", c,
                      "Subraya en el enunciado la causa que da el libro. Después ubica cada reloj en el dibujo y "
                      "completa la cadena: dónde es más intenso el campo, dónde corre más despacio el tiempo.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 270, c, r=16)
    ex, ey, er = x0 + 150, yy + 140, 90
    for k in range(12):
        import math as _m
        a = k * _m.pi / 6
        b.append(line(ex + (er + 8) * _m.cos(a), ey + (er + 8) * _m.sin(a),
                      ex + (er + 50) * _m.cos(a), ey + (er + 50) * _m.sin(a), tinte(c, 0.55), 2, "6,6"))
    b.append(f'<circle cx="{ex}" cy="{ey}" r="{er}" fill="{tinte(EDU_AZUL, 0.8)}" stroke="{EDU_AZUL}" stroke-width="2.4"/>')
    texto(b, ex, ey + 6, "Tierra", size=18, color=EDU_AZUL, weight="700", anchor="middle")
    # reloj en superficie
    def reloj(cx, cy):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="20" fill="white" stroke="{INK}" stroke-width="2.4"/>')
        b.append(line(cx, cy, cx, cy - 13, INK, 2.4))
        b.append(line(cx, cy, cx + 10, cy, INK, 2.4))
    reloj(ex + er + 4, ey - 30)
    sx = x0 + 640
    b.append(rect(sx - 40, ey - 18, 80, 36, "#EEF0F4", r=6, stroke=INK, sw=2))
    b.append(rect(sx - 100, ey - 10, 50, 20, tinte(EDU_AZUL, 0.6), r=2, stroke=INK, sw=1.6))
    b.append(rect(sx + 50, ey - 10, 50, 20, tinte(EDU_AZUL, 0.6), r=2, stroke=INK, sw=1.6))
    reloj(sx, ey - 48)
    pista(b, sx, ey + 44, "satélite del GPS", anchor="middle")
    pista(b, ex + er + 30, ey - 30, "reloj en la superficie")
    rx, rw = x0 + 790, ww - 810
    for k, (tit, ps) in enumerate((("CAMPO MÁS INTENSO", "¿cerca o lejos de la Tierra?"),
                                    ("TIEMPO MÁS LENTO", "¿en cuál de los dos relojes?"),
                                    ("EL GPS CORRIGE", "¿qué reloj se adelanta?"))):
        py = yy + 14 + k * 84
        rot(b, rx, py + 22, tit, c, size=14)
        pista(b, rx, py + 44, ps)
        renglon(b, rx, py + 74, rx + rw)
    yy += 290
    caja(b, x0, yy, ww, 104, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "MI FILTRO", c)
    pista(b, x0 + 20, yy + 62, "la causa que da el enunciado es:")
    renglon(b, x0 + 260, yy + 64, x0 + ww - 20)
    pista(b, x0 + 20, yy + 92, "una opción sirve si explica con esa causa, no con otra que el enunciado no menciona")
    yy += 122
    return alto_profe(b, x0, yy, ww,
                      "Relatividad general: la gravedad cambia el ritmo del tiempo. Cerca de una masa grande, como la "
                      "Tierra, el tiempo transcurre un poquito más despacio. Pídele al profe que explique por qué una "
                      "diferencia de millonésimas de segundo basta para que el GPS se equivoque kilómetros en un día.")


# ───────── P4 · el dron · energía mecánica ─────────
def i4(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La cuenta de joules en dos entregas", c,
                      "Energía mecánica = energía potencial + energía cinética. Calcula las dos partes en cada entrega, "
                      "con g = 10 m/s², y después compara los totales.")
    x0, ww = x + 22, w - 44
    cols = (170, 110, 110, 120, 240, 240, ww - 990)
    yy = tabla_vacia(b, x0, yy, cols, ("ENTREGA", "m (kg)", "h (m)", "v (m/s)", "Ep = m·g·h (J)",
                                       "Ec = ½·m·v² (J)", "Em (J)"),
                     ("Piso 20", "Piso 5", "Diferencia"), c, rh=70)
    yy += 20
    half = (ww - 24) / 2
    caja_preg(b, x0, yy, half, 120, c, "¿PASA DE 1.000 J?",
              "la diferencia de energía mecánica es mayor que 1.000 J:")
    sino(b, x0 + 16, yy + 70, c)
    caja_preg(b, x0 + half + 24, yy, half, 120, c, "¿QUÉ PESA MÁS?",
              "en la diferencia aporta más la altura (Ep) o la rapidez (Ec)? ¿cuánto cada una?")
    yy += 140
    return ojo(b, x0, yy, ww, "¿Y LA RAPIDEZ EN EL MOMENTO DE LA ENTREGA?",
               "El libro da la rapidez promedio de los trayectos horizontales, no la del instante en que entrega. "
               "Úsala como pide la pregunta, pero mira cuánto aporta la Ec al total: ¿cambiaría la comparación si "
               "el dron llegara casi quieto?")


# ───────── P5 · consumo proporcional a la altura ─────────
def i5(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Cada metro de altura cuesta lo mismo", c,
                      "«Proporción directa» quiere decir que si la altura se multiplica por un número, el consumo se "
                      "multiplica por el mismo número. Resuélvelo por dos caminos y comprueba que llegan al mismo valor.")
    x0, ww = x + 22, w - 44
    # edificio
    bx, by, bw, bh = x0 + 20, yy + 10, 150, 400
    caja(b, bx, by, bw, bh, c, r=6, fill=tinte(c, 0.94))
    for j in range(1, 10):
        b.append(line(bx, by + j * bh / 10, bx + bw, by + j * bh / 10, tinte(c, 0.7), 1.4))
    for hm, lab in ((30, "30 m · piso 10"), (75, "75 m · piso 25")):
        py = by + bh - hm / 80 * bh
        b.append(line(bx - 10, py, bx + bw + 20, py, c, 2.6, "7,5"))
        texto(b, bx + bw + 26, py + 6, lab, size=16, color=c, weight="700")
    texto(b, bx + bw + 26, by + bh - 30 / 80 * bh + 30, "90.000 J", size=16, weight="700")
    texto(b, bx + bw + 26, by + bh - 75 / 80 * bh + 30, "? J", size=16, weight="700")
    texto(b, bx + bw / 2, by + bh + 26, "0 m", size=15, color=GRAY, anchor="middle")
    rx, rw = x0 + 380, ww - 380
    caja(b, rx, yy, rw, 190, c, r=14)
    rot(b, rx + 20, yy + 30, "CAMINO 1 · CUÁNTO CUESTA UN METRO", c)
    texto(b, rx + 20, yy + 76, "90.000 J  ÷  30 m  =", size=19, weight="700")
    renglon(b, rx + 250, yy + 78, rx + 420)
    texto(b, rx + 430, yy + 76, "J/m", size=19, weight="700")
    texto(b, rx + 20, yy + 130, "J/m  ×  75 m  =", size=19, weight="700")
    renglon(b, rx + 190, yy + 132, rx + 400)
    texto(b, rx + 410, yy + 130, "J", size=19, weight="700")
    pista(b, rx + 20, yy + 172, "fíjate: J/m × m deja solo J")
    caja(b, rx, yy + 210, rw, 190, c, r=14)
    rot(b, rx + 20, yy + 240, "CAMINO 2 · CUÁNTAS VECES MÁS ALTO", c)
    texto(b, rx + 20, yy + 286, "75 m  ÷  30 m  =", size=19, weight="700")
    renglon(b, rx + 200, yy + 288, rx + 340)
    texto(b, rx + 350, yy + 286, "veces", size=19, weight="700")
    texto(b, rx + 20, yy + 340, "90.000 J  ×", size=19, weight="700")
    renglon(b, rx + 140, yy + 342, rx + 240)
    texto(b, rx + 250, yy + 340, "=", size=19, weight="700")
    renglon(b, rx + 280, yy + 342, rx + 480)
    texto(b, rx + 490, yy + 340, "J", size=19, weight="700")
    pista(b, rx + 20, yy + 382, "m ÷ m no deja unidad: es un número de veces")
    yy += 440
    caja(b, x0, yy, ww, 80, c, r=14, dash="8,6")
    pista(b, x0 + 20, yy + 32, "¿Alcanza la batería de 1.080.000 J para esa entrega?")
    sino(b, x0 + 420, yy + 16, c)
    pista(b, x0 + 20, yy + 66, "¿qué parte de la batería gasta? (consumo ÷ capacidad)")
    renglon(b, x0 + 420, yy + 68, x0 + ww - 20)
    return yy + 80


# ───────── P6 · trabajo mecánico ─────────
def i6(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Fuerza y camino: ¿van juntos o no?", c,
                      "Hay trabajo sobre el paquete cuando la fuerza lo mueve en su misma dirección: W = F · d. En cada "
                      "escena dibuja la fuerza que hace el dron y el desplazamiento del paquete, y decide si cambia su "
                      "energía.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (tit, sub) in enumerate((("ESCENA 1 · ACELERA DE 5 A 8 m/s", "trayecto horizontal"),
                                    ("ESCENA 2 · LO SOSTIENE QUIETO", "a 60 m de altura"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 330, c, r=16)
        rot(b, bx + 18, yy + 30, tit, c)
        pista(b, bx + 18, yy + 52, sub)
        # dron y paquete
        dx, dy = bx + 150, yy + 110
        b.append(rect(dx - 40, dy - 12, 80, 20, "#EEF0F4", r=6, stroke=INK, sw=2))
        for s in (-1, 1):
            b.append(line(dx + s * 40, dy - 6, dx + s * 64, dy - 18, INK, 2))
            b.append(line(dx + s * 80, dy - 22, dx + s * 48, dy - 22, INK, 2.4))
        b.append(line(dx, dy + 8, dx, dy + 30, INK, 2))
        b.append(rect(dx - 26, dy + 30, 52, 44, tinte(EDU_ORO, 0.75), r=4, stroke=INK, sw=2))
        texto(b, dx, dy + 58, "3 kg", size=14, weight="700", anchor="middle")
        pista(b, dx + 90, dy + 52, "dibuja aquí las flechas")
        fy = yy + 210
        pista(b, bx + 18, fy, "desplazamiento del paquete:")
        renglon(b, bx + 230, fy + 2, bx + half - 60)
        texto(b, bx + half - 50, fy, "m", size=16, weight="700")
        pista(b, bx + 18, fy + 40, "¿la fuerza y el camino van en la misma dirección?")
        sino(b, bx + 18, fy + 52, c)
        pista(b, bx + 18, fy + 106, "¿cambia la energía del paquete?")
        sino(b, bx + 270, fy + 90, c)
    yy += 350
    caja(b, x0, yy, ww, 92, c, r=14, fill=tinte(c, 0.95))
    rot(b, x0 + 20, yy + 30, "LO QUE GANA EL PAQUETE EN LA ESCENA 1", c)
    texto(b, x0 + 20, yy + 70, "ΔEc = ½ · 3 kg · (8² − 5²) m²/s²  =", size=19, weight="700")
    renglon(b, x0 + 400, yy + 72, x0 + 600)
    texto(b, x0 + 610, yy + 70, "J", size=19, weight="700")
    pista(b, x0 + 660, yy + 70, "ese es el trabajo que hizo el dron sobre el paquete")
    yy += 110
    return ojo(b, x0, yy, ww, "CANSARSE NO ES HACER TRABAJO",
               "Sostener el paquete gasta batería: los motores empujan aire hacia abajo y se calientan. Pero en física "
               "hay trabajo SOBRE EL PAQUETE solo si la fuerza lo desplaza. El gasto de la batería y el trabajo sobre "
               "el paquete son dos cuentas distintas.")


# ───────── P7 · la energía que no llegó al paquete ─────────
def i7(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El río de energía que sale de la batería", c,
                      "Dibuja el ancho de cada brazo del río según cuánta energía lleva. La energía no se crea ni se "
                      "destruye: todo lo que sale de la batería tiene que terminar en alguna parte que puedas nombrar.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 330, c, r=16)
    sx, sy = x0 + 30, yy + 70
    caja(b, sx, sy, 180, 190, c, r=12, fill=tinte(c, 0.85), sw=2.4)
    rot(b, sx + 16, sy + 34, "BATERÍA", c)
    pista(b, sx + 16, sy + 60, "energía química")
    pista(b, sx + 16, sy + 84, "100 %")
    # tronco y brazos (contornos para que el estudiante los pinte)
    tx = sx + 180
    b.append(f'<path d="M {tx} {sy} L {tx + 260} {sy} C {tx + 360} {sy} {tx + 380} {sy - 30} {tx + 480} {sy - 30} '
             f'L {tx + 560} {sy - 30} L {tx + 560} {sy + 70} L {tx + 480} {sy + 70} C {tx + 400} {sy + 70} '
             f'{tx + 380} {sy + 95} {tx + 330} {sy + 95} C {tx + 380} {sy + 95} {tx + 400} {sy + 140} '
             f'{tx + 480} {sy + 140} L {tx + 560} {sy + 140} L {tx + 560} {sy + 240} L {tx + 480} {sy + 240} '
             f'C {tx + 380} {sy + 240} {tx + 360} {sy + 190} {tx + 260} {sy + 190} L {tx} {sy + 190} Z" '
             f'fill="none" stroke="{c}" stroke-width="2.4" stroke-dasharray="9,6"/>')
    pista(b, tx + 40, sy + 100, "lo que sale de la batería")
    ex = tx + 580
    caja(b, ex, sy - 40, ww - (ex - x0) - 20, 120, c, r=12)
    rot(b, ex + 16, sy - 12, "LLEGA AL PAQUETE", c, size=14)
    pista(b, ex + 16, sy + 14, "como energía…")
    renglon(b, ex + 16, sy + 60, x0 + ww - 36)
    caja(b, ex, sy + 130, ww - (ex - x0) - 20, 120, c, r=12)
    rot(b, ex + 16, sy + 158, "NO LLEGA AL PAQUETE", c, size=14)
    pista(b, ex + 16, sy + 184, "se fue como… (dos formas)")
    renglon(b, ex + 16, sy + 230, x0 + ww - 36)
    pista(b, sx, yy + 312, "¿Cuál brazo es más ancho según los ingenieros? Píntalo más grueso.")
    yy += 350
    caja(b, x0, yy, ww, 76, c, r=14, fill=tinte(c, 0.94))
    texto(b, x0 + 20, yy + 46, "energía de la batería  =", size=19, weight="700")
    renglon(b, x0 + 260, yy + 48, x0 + 600)
    texto(b, x0 + 610, yy + 46, "+", size=19, weight="700")
    renglon(b, x0 + 640, yy + 48, x0 + ww - 20)
    yy += 96
    return trampa(b, x0, yy, ww, "Pregúntale a cada opción: ¿a dónde se fue la energía que falta?",
                  "Una explicación consistente con el modelo físico tiene que nombrar el destino de la energía. Si una "
                  "opción no lo dice, o dice que la energía dejó de existir, no está usando la conservación de la "
                  "energía.", c)


# ───────── P8 · sifón · ¿la conclusión se sostiene? ─────────
def i8(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Las tres palabras grandes de la conclusión", c,
                      "«Cualquier líquido», «en cualquier condición», «siempre»: la conclusión promete mucho. Una "
                      "conclusión vale hasta donde llegan sus ensayos. Escribe qué se probó de verdad y qué faltaría.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 70, c, r=14)
    pista(b, x0 + 20, yy + 42, "¿cuántos ensayos hubo?")
    renglon(b, x0 + 200, yy + 44, x0 + 300)
    pista(b, x0 + 330, yy + 42, "¿con cuántos líquidos?")
    renglon(b, x0 + 510, yy + 44, x0 + 610)
    pista(b, x0 + 640, yy + 42, "¿con cuántos tipos de vaso?")
    renglon(b, x0 + 850, yy + 44, x0 + 950)
    yy += 90
    cols = (330, (ww - 330) / 2, (ww - 330) / 2)
    yy = tabla_vacia(b, x0, yy, cols, ("LA PALABRA", "LO QUE SE PROBÓ", "LO QUE FALTARÍA PROBAR"),
                     ("«cualquier líquido»", "«en cualquier condición»", "«siempre»"), c, rh=82)
    yy += 20
    caja(b, x0, yy, ww, 110, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "UN EXPERIMENTO EN MI CABEZA", c)
    pista(b, x0 + 20, yy + 62, "si cambio el agua por miel, ¿el sifón funcionaría igual? ¿y si cambio el vaso por uno ancho?")
    renglon(b, x0 + 20, yy + 96, x0 + ww - 20)
    yy += 128
    return ojo(b, x0, yy, ww, "MÁS DE UNA OPCIÓN PUEDE SEÑALAR ALGO QUE FALTÓ",
               "Para escoger no basta con que la crítica sea cierta: tiene que apuntar a lo que la conclusión "
               "generalizó sin probar y que de verdad cambiaría el resultado del sifón. Compara las críticas con tu "
               "experimento en la cabeza.")


# ───────── P9 · sifón · el modelo ─────────
def i9(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El sifón por dentro: dos columnas de agua", c,
                      "Mira el pitillo como dos columnas de agua unidas por arriba. Rotula las alturas, dibuja quién "
                      "empuja sobre la superficie de cada vaso y decide qué columna pesa más.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 700, 420, c, r=16)
    # mesa, taza, vasos
    my = yy + 390
    b.append(line(x0 + 30, my, x0 + 670, my, INK, 3))
    tzx = x0 + 90
    b.append(rect(tzx, my - 110, 140, 110, "#EEF0F4", r=8, stroke=INK, sw=2))
    pista(b, tzx + 70, my - 50, "taza", anchor="middle")
    v1x, v1y = tzx + 10, my - 110 - 160
    b.append(rect(v1x, v1y, 120, 160, "white", r=4, stroke=INK, sw=2.2))
    b.append(rect(v1x + 3, v1y + 40, 114, 117, tinte(EDU_AZUL, 0.78), r=2))
    v2x, v2y = x0 + 470, my - 160
    b.append(rect(v2x, v2y, 120, 160, "white", r=4, stroke=INK, sw=2.2))
    b.append(rect(v2x + 3, v2y + 130, 114, 27, tinte(EDU_AZUL, 0.78), r=2))
    # pitillo
    px1, px2, top = v1x + 70, v2x + 50, v1y - 50
    b.append(f'<path d="M {px1} {v1y + 140} L {px1} {top + 20} Q {px1} {top} {px1 + 20} {top} L {px2 - 20} {top} '
             f'Q {px2} {top} {px2} {top + 20} L {px2} {v2y + 150}" fill="none" stroke="{tinte(EDU_AZUL, 0.4)}" '
             f'stroke-width="10" stroke-linecap="round"/>')
    # cotas
    for xx, y1, y2, lab in ((px1 - 40, top, v1y + 40, "brazo corto"), (px2 + 34, top, v2y + 130, "brazo largo")):
        b.append(line(xx, y1, xx, y2, c, 2, "5,4"))
        b.append(line(xx - 8, y1, xx + 8, y1, c, 2))
        b.append(line(xx - 8, y2, xx + 8, y2, c, 2))
    for k, lab in enumerate(("altura del brazo corto:", "altura del brazo largo:")):
        pista(b, px1 + 70, top + 70 + k * 64, lab)
        renglon(b, px1 + 70, top + 100 + k * 64, px2 - 40)
    pista(b, x0 + 30, yy + 34, "dibuja con flechas el empuje del aire sobre el agua de cada vaso")
    rx, rw = x0 + 730, ww - 730
    qs = (("QUÉ COLUMNA PESA MÁS", "la del brazo… ¿por qué?"),
          ("QUÉ LA HACE SUBIR", "¿qué empuja el agua hacia arriba por el brazo corto?"),
          ("QUÉ LA HACE BAJAR", "¿qué fuerza tira del agua por el brazo largo?"))
    for k, (tit, ps) in enumerate(qs):
        caja_preg(b, rx, yy + k * 142, rw, 128, c, tit, ps)
    yy += 440
    return alto_profe(b, x0, yy, ww,
                      "Presión atmosférica: el aire tiene peso y empuja sobre todo lo que toca, también sobre la "
                      "superficie del agua de cada vaso (unos 10 N por cada centímetro cuadrado). Pídele al profe que "
                      "muestre por qué el agua no se cae de un pitillo tapado arriba con el dedo.")


# ───────── P10 · fuerzas sobre el agua del pitillo ─────────
def i10(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Diagrama de cuerpo libre de un poco de agua del pitillo", c,
                      "Imagina un trocito de agua dentro del brazo largo como un punto. Para cada fuerza candidata "
                      "decide si de verdad actúa, quién la hace y hacia dónde va. Después dibuja solo las que pasan.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 300, 400, c, r=16)
    b.append(rect(x0 + 120, yy + 40, 60, 330, tinte(EDU_AZUL, 0.85), r=10, stroke=INK, sw=2))
    b.append(f'<circle cx="{x0 + 150}" cy="{yy + 205}" r="10" fill="{INK}"/>')
    pista(b, x0 + 150, yy + 392, "brazo largo del pitillo", anchor="middle")
    pista(b, x0 + 16, yy + 28, "dibuja las flechas aquí")
    cols = (300, 160, 220, ww - 300 - 700)
    tx = x0 + 320
    filas = ("peso (gravedad)", "empuje del aire (presión)", "rozamiento con el pitillo", "fuerza centrífuga",
             "flotación", "fuerza magnética")
    hh, rh = 48, 58
    caja(b, tx, yy, sum(cols), hh, c, fill=tinte(c), r=8)
    for k, hd in enumerate(("FUERZA CANDIDATA", "¿ACTÚA AQUÍ?", "¿QUIÉN LA HACE?", "¿HACIA DÓNDE?")):
        rot(b, tx + sum(cols[:k]) + 14, yy + 30, hd, c, size=14)
    ry = yy + hh
    for f in filas:
        caja(b, tx, ry, sum(cols), rh, c, r=0)
        texto(b, tx + 14, ry + rh / 2 + 6, f, size=16, weight="700")
        sino(b, tx + cols[0] + 14, ry + 18, c, gap=70)
        renglon(b, tx + cols[0] + cols[1] + 14, ry + rh - 16, tx + cols[0] + cols[1] + cols[2] - 14)
        renglon(b, tx + cols[0] + cols[1] + cols[2] + 14, ry + rh - 16, tx + sum(cols) - 14)
        ry += rh
    cx = tx
    for k in range(3):
        cx += cols[k]
        b.append(line(cx, yy, cx, ry, c, 1.6))
    yy = max(ry, yy + 400) + 20
    return trampa(b, x0, yy, ww, "Una fuerza necesita alguien que la haga:",
                  "si no puedes decir quién empuja o tira (la Tierra, el aire, la pared del pitillo…), esa fuerza no "
                  "va en el diagrama. Una opción es correcta solo si todas las fuerzas que nombra pasan esta prueba y "
                  "van en la dirección correcta.", c)


Q = {1: dict(n=1, est=1, pag=247, ctx="Una herramienta en la Tierra y en Marte · diferencia de energía potencial",
             comp="Uso comprensivo del conocimiento científico", inst=i1),
     2: dict(n=2, est=3, pag=248, ctx="Central mareomotriz en el laboratorio · qué procedimiento es confiable",
             comp="Indagación", inst=i2),
     3: dict(n=3, est=4, pag=248, ctx="Relojes en la Tierra y en un satélite · qué principio explica el GPS",
             comp="Explicación de fenómenos", inst=i3),
     4: dict(n=4, est=1, pag=248, ctx="Dron en Bogotá · energía mecánica del paquete en el piso 20 y en el 5",
             comp="Uso comprensivo del conocimiento científico", inst=i4),
     5: dict(n=5, est=1, pag=249, ctx="Dron en Bogotá · consumo de batería proporcional a la altura",
             comp="Uso comprensivo del conocimiento científico", inst=i5),
     6: dict(n=6, est=2, pag=249, ctx="Dron en Bogotá · cuándo hace trabajo sobre el paquete",
             comp="Explicación de fenómenos", inst=i6),
     7: dict(n=7, est=4, pag=249, ctx="Dron en Bogotá · la energía que no llegó al paquete",
             comp="Explicación de fenómenos", inst=i7),
     8: dict(n=8, est=3, pag=250, ctx="Sifón con dos vasos · ¿vale la conclusión de un solo ensayo?",
             comp="Indagación", inst=i8),
     9: dict(n=9, est=4, pag=250, ctx="Sifón con dos vasos · qué modelo explica el flujo",
             comp="Explicación de fenómenos", inst=i9),
     10: dict(n=10, est=2, pag=250, ctx="Sifón con dos vasos · qué fuerzas mueven el agua",
              comp="Explicación de fenómenos", inst=i10)}


def build(pages=(254, 255, 257, 258, 259)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"fis5_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
