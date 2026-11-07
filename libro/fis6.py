#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 6 · componente físico · termodinámica · páginas 261–267. Cierre del área.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 6» de Física (fuente_libro/FÍSICA), páginas 259–262.
Contenido: la energía que se transforma, se reparte y se pierde. El calor de un centro de datos
(1), un motor eléctrico que mueve una banda (2 a 4), un molinillo de convección movido por
velas (5 a 7), agua caliente que se enfría en la sala (8), dos resistencias en paralelo (9) y la
eficiencia de un cargador de celular (10).

Claves verificadas (resueltas a mano, con cuentas y unidades, 7 nov 2026):

    1·B  2·C  3·A  4·D  5·C  6·C  7·B  8·D  9·C  10·D

  1 · B: la afirmación dice que lo aprovechado es «equivalente» al calor liberado. Los datos lo
      niegan los tres días: 6500/9000 = 72 % · 6100/8600 = 71 % · 6700/9200 = 73 %. A y C la dan
      por válida. Hallazgo (Media): la D también es defendible si «eficiencia del sistema» se lee
      como electricidad → calefacción (6500/12000 = 54 %); la B es la que usa directamente los
      datos contra la afirmación tal como está escrita.
  2 · C: 18 MJ − 13,5 MJ = 4,5 MJ que se van como calor (resistencia de los materiales) y
      vibraciones, como dice el texto. A niega las pérdidas; B (energía → masa) y D (energía
      potencial por el peso de la banda) no tienen sentido aquí.
  3 · A: 13,5 MJ / 18 MJ = 0,75 (sin unidades). C (0,65) y B (0,50) no salen de los datos; D (1,00)
      sería un motor sin pérdidas.
  4 · D: con una sola hora no se puede afirmar eficiencia total (hubo 4,5 MJ de pérdidas) ni
      generalizar a las condiciones reales de trabajo. Hallazgo (Media): la B también es cierta
      (los datos sí muestran pérdidas); la D la contiene y añade lo que pregunta el contexto (si los
      resultados bastan para caracterizar el motor). A y C generalizan.
  5 · C: la rapidez deja de aumentar cuando la energía que entrega el aire por segundo iguala la que
      se pierde por fricción en el eje y las aspas (y con el aire). A dice que se detiene (no se
      detiene); B, que la vela solo da luz; D, que la densidad no cambia (el aire caliente es menos
      denso: por eso sube).
  6 · C: 4 velas × 2,5 kJ/(vela·min) × 10 min = 100 kJ. A (25 kJ) es una vela; D (250 kJ) multiplica
      por 100; B (50 kJ) son dos velas. Atención: el montaje del texto tiene cinco velas y la
      pregunta usa cuatro («en una versión del experimento»).
  7 · B: mientras haya cera ardiendo, la energía química se sigue transformando en calor y mantiene
      la corriente de aire. A (la energía desaparece), C (sigue igual sin fuente) y D (solo la luz)
      contradicen la conservación o el texto.
  8 · D: el calor fluye del agua (más caliente) al aire de la sala hasta igualar temperaturas; la
      energía se conserva (pasa al aire). A (pierde TODA su energía térmica), B (el aire se calienta
      sin límite) y C (el calor desaparece) son falsas.
  9 · C: dos resistencias iguales en paralelo se reparten la corriente por mitades: 4 A / 2 = 2 A
      (cada una tiene 12 V: R = 12 V / 2 A = 6 Ω). A (6) es el valor de R en ohmios, no una
      corriente; D (4 A) es la total; B (1 A) no sale de ninguna cuenta. Atención: es un circuito
      eléctrico dentro de una misión de termodinámica.
 10 · D: la toma entrega 15 W × 3600 s = 54.000 J = 54 kJ; 45/54 = 0,83 → 83 %. Pero 45 + 6 = 51 kJ:
      faltan 3 kJ sin medir, así que «no existen otras pérdidas» no se sostiene. Atención: la B es
      parcialmente defendible (los 15 W son nominales; la energía de la toma no se midió); la D es la
      que se apoya en el dato «el resto no fue cuantificado». Además, la batería guarda energía
      química, no «energía eléctrica».

Reparto: A 1 (3) · B 2 (1, 7) · C 4 (2, 5, 6, 9) · D 3 (4, 8, 10). La A sale una sola vez.
Registrado como Atención en tablero/propuestas/fis6_hallazgos.csv.

Estrategias (las tres primeras recogen lo trabajado en el área: las cuentas con unidades de la
Misión 5, la conservación de la energía y el control de los datos en todas las misiones):
    1 · Multiplica, divide y lleva las unidades        (3, 6, 9   · ICFES 2016-1 1.ª ses. N.º 97)   azul
    2 · La energía no desaparece: cambia de forma      (2, 7      · ICFES 2016-1 2.ª ses. N.º 73)   rojo
    3 · ¿Alcanzan los datos para esa conclusión?       (1, 4, 10  · ICFES 2016-1 2.ª ses. N.º 77)   morado
    4 · Cuando algo deja de cambiar: el equilibrio     (5, 8      · ICFES cuadernillo 2025 N.º 35)  oro

Hojas: 261 fis6_t1 (1-2) · 262 fis6_t2 (3-4) · 263 fis6_i1 · 264 fis6_t3 (5-6) ·
       265 fis6_t4 (7-8) · 266 fis6_t5 (9-10) · 267 fis6_i2.
"""
from taller_base import *

configurar("Física", 6, "físico · termodinámica",
           tema="La energía que se transforma, se reparte y se pierde",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Multiplica, divide y lleva las unidades", EDU_AZUL),
       2: ("La energía no desaparece: cambia de forma", EDU_ROJO),
       3: ("¿Alcanzan los datos para esa conclusión?", MORADO),
       4: ("Cuando algo deja de cambiar: el equilibrio", EDU_ORO)}
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



def ecuacion(b, x, y, partes, c, size=19):
    """Fila de cuentas: texto fijo y huecos. partes = [("t", texto) | ("h", ancho)]."""
    cx = x
    for tipo, v in partes:
        if tipo == "t":
            texto(b, cx, y, v, size=size, weight="700")
            cx += tw(v, size, "700") + 12
        else:
            renglon(b, cx, y + 2, cx + v)
            cx += v + 12
    return cx


# ───────── P1 · centro de datos · ¿100 %? ─────────
def i1(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Tres días, dos porcentajes", c,
                      "Antes de juzgar la afirmación, saca de la tabla del libro dos porcentajes por día. Divide lo "
                      "aprovechado entre cada una de las otras dos columnas y multiplica por 100.")
    x0, ww = x + 22, w - 44
    cols = (140, (ww - 360) / 2, (ww - 360) / 2, 220)
    yy = tabla_vacia(b, x0, yy, cols, ("DÍA", "APROVECHADA ÷ TÉRMICA LIBERADA", "APROVECHADA ÷ CONSUMO ELÉCTRICO",
                                       "¿LLEGA A 100 %?"), ("Día 1", "Día 2", "Día 3"), c, rh=66,
                     sin_renglon=(3,))
    for k in range(3):
        sino(b, x0 + ww - 200, yy - 3 * 66 + k * 66 + 22, c)
    yy += 20
    caja(b, x0, yy, ww, 120, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE COMPARA LA AFIRMACIÓN", c)
    pista(b, x0 + 20, yy + 66, "dice que la energía")
    renglon(b, x0 + 170, yy + 68, x0 + 560)
    pista(b, x0 + 580, yy + 66, "es equivalente a la energía")
    renglon(b, x0 + 790, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 104, "¿lo confirman los tres días?")
    sino(b, x0 + 240, yy + 88, c)
    yy += 140
    return ojo(b, x0, yy, ww, "EFICIENCIA = LO ÚTIL ÷ LO QUE ENTRA",
               "Una eficiencia de 100 % querría decir que no se pierde nada en el camino. Para usar la fórmula hay que "
               "decidir primero qué es «lo que entra» en el sistema del que se habla. Lee otra vez la afirmación: "
               "¿de qué sistema habla y con qué dato lo mide?")


# ───────── P2 · motor · a dónde se va la energía ─────────
def i2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El libro de cuentas del motor", c,
                      "Lleva la energía como si fuera plata: todo lo que entra tiene que salir por algún lado. Llena la "
                      "cuenta con los datos del libro y escribe en qué formas sale lo que no llega al eje.")
    x0, ww = x + 22, w - 44
    cw = (ww - 2 * 60) / 3
    tits = (("ENTRA", "energía eléctrica"), ("SALE ÚTIL", "energía mecánica al eje"), ("SALE SIN USAR", "¿en qué formas?"))
    for k, (t1, t2) in enumerate(tits):
        bx = x0 + k * (cw + 60)
        caja(b, bx, yy, cw, 200, c, r=16, sw=2.4, fill=tinte(c, 0.95) if k == 0 else "white")
        rot(b, bx + 18, yy + 32, t1, c)
        pista(b, bx + 18, yy + 58, t2)
        renglon(b, bx + 18, yy + 120, bx + cw - 70)
        texto(b, bx + cw - 56, yy + 118, "MJ", size=18, weight="700")
        if k == 2:
            pista(b, bx + 18, yy + 160, "como:")
            renglon(b, bx + 70, yy + 162, bx + cw - 18)
        if k < 2:
            texto(b, bx + cw + 30, yy + 112, "=" if k == 0 else "+", size=34, color=c, weight="700",
                  anchor="middle")
    yy += 220
    caja(b, x0, yy, ww, 110, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "PREGUNTAS DE CONTADOR", c)
    pista(b, x0 + 20, yy + 64, "¿el motor sale más pesado después de una hora de trabajo?")
    sino(b, x0 + 480, yy + 48, c)
    pista(b, x0 + 20, yy + 96, "¿la banda gana altura al moverse?")
    sino(b, x0 + 480, yy + 80, c)
    pista(b, x0 + 660, yy + 64, "¿se siente tibio el motor? ¿por qué?")
    renglon(b, x0 + 660, yy + 98, x0 + ww - 20)
    yy += 130
    return ojo(b, x0, yy, ww, "«PERDER» ENERGÍA NO ES DESTRUIRLA",
               "En ingeniería, la energía «perdida» es la que terminó en una forma que no sirve para el trabajo que "
               "queríamos: calienta los cables y el aire, hace vibrar la estructura, suena. Sigue existiendo; solo "
               "que ya no mueve la banda.")


# ───────── P3 · eficiencia del motor ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La barra de las 18 casillas", c,
                      "Cada casilla es 1 MJ de energía eléctrica que entra al motor. Pinta las que llegan al eje como "
                      "energía mecánica (la mitad de una casilla también cuenta) y escribe la fracción.")
    x0, ww = x + 22, w - 44
    cw = (ww - 40) / 18
    for k in range(18):
        caja(b, x0 + 20 + k * cw, yy + 10, cw - 6, 70, c, r=6)
        texto(b, x0 + 20 + k * cw + (cw - 6) / 2, yy + 104, str(k + 1), size=14, color=GRAY, anchor="middle")
    pista(b, x0 + 20, yy + 134, "1 casilla = 1 MJ · total: 18 MJ consumidos")
    yy += 160
    caja(b, x0, yy, ww, 160, c, r=14, fill=tinte(c, 0.95))
    rot(b, x0 + 20, yy + 30, "LA FRACCIÓN ÚTIL", c)
    ecuacion(b, x0 + 20, yy + 76, [("t", "energía útil ÷ energía consumida  ="), ("h", 110), ("t", "MJ  ÷"),
                                   ("h", 110), ("t", "MJ  ="), ("h", 130)], c)
    pista(b, x0 + 20, yy + 128, "MJ ÷ MJ: ¿qué unidad queda?")
    renglon(b, x0 + 260, yy + 130, x0 + 520)
    pista(b, x0 + 560, yy + 128, "en porcentaje:")
    renglon(b, x0 + 680, yy + 130, x0 + 860)
    texto(b, x0 + 870, yy + 128, "%", size=18, weight="700")
    yy += 180
    return caja_preg(b, x0, yy, ww, 110, c, "¿PUEDE PASAR DE 1?",
                     "¿Qué querría decir una eficiencia de 1,00? ¿Y una mayor que 1? Escríbelo con tus palabras.")


# ───────── P4 · ¿una hora basta? ─────────
def i4(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Lo que muestra una hora y lo que no muestra", c,
                      "El contexto dice que los ingenieros querían saber si sus datos bastaban para describir el motor "
                      "en condiciones reales de trabajo. Separa lo que una sola hora de prueba sí deja decir de lo que "
                      "no alcanza a decir.")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    for k, (t1, t2) in enumerate((("LO QUE LOS DATOS SÍ MUESTRAN", "con números de la prueba"),
                                  ("LO QUE HARÍA FALTA PARA GENERALIZAR", "¿qué podría cambiar en el trabajo real?"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 250, c, r=16, sw=2.4)
        rot(b, bx + 18, yy + 32, t1, c)
        pista(b, bx + 18, yy + 58, t2)
        for j in range(4):
            renglon(b, bx + 18, yy + 108 + j * 42, bx + half - 18)
    yy += 270
    caja(b, x0, yy, ww, 74, c, r=14)
    pista(b, x0 + 20, yy + 30, "¿cuántas horas se midieron?")
    renglon(b, x0 + 230, yy + 32, x0 + 330)
    pista(b, x0 + 360, yy + 30, "¿con qué carga en la banda?")
    renglon(b, x0 + 570, yy + 32, x0 + 800)
    pista(b, x0 + 20, yy + 62, "¿hubo pérdidas?")
    sino(b, x0 + 150, yy + 46, c)
    pista(b, x0 + 360, yy + 62, "¿cuántos MJ?")
    renglon(b, x0 + 470, yy + 64, x0 + 600)
    yy += 94
    return trampa(b, x0, yy, ww, "Cuando dos opciones empiezan igual, la diferencia está en la razón:",
                  "lee cada razón completa y compárala con tus dos columnas. Una buena valoración responde todo lo que "
                  "se pregunta, no solo una parte.", c)


# ───────── P5 · el molinillo deja de acelerar ─────────
def i5(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La balanza del molinillo", c,
                      "En un platillo pon lo que el aire caliente le entrega a las aspas cada segundo; en el otro, lo "
                      "que las aspas pierden cada segundo por fricción. Según cómo quede la balanza, el giro acelera, "
                      "se mantiene o se frena.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 480, 290, c, r=16)
    cx_, top = x0 + 240, yy + 60
    b.append(f'<polygon points="{cx_ - 30},{yy + 250} {cx_ + 30},{yy + 250} {cx_},{top + 10}" fill="{tinte(c, 0.8)}" '
             f'stroke="{INK}" stroke-width="2"/>')
    b.append(line(cx_ - 180, top + 10, cx_ + 180, top + 10, INK, 3))
    for s in (-1, 1):
        px = cx_ + s * 150
        b.append(line(px, top + 10, px - 40, top + 90, INK, 1.6))
        b.append(line(px, top + 10, px + 40, top + 90, INK, 1.6))
        b.append(f'<path d="M {px - 60} {top + 90} Q {px} {top + 130} {px + 60} {top + 90} Z" fill="white" '
                 f'stroke="{INK}" stroke-width="2"/>')
    pista(b, cx_ - 150, top + 160, "entrega el aire", anchor="middle")
    pista(b, cx_ + 150, top + 160, "pierde por fricción", anchor="middle")
    pista(b, cx_ - 150, top + 182, "(cada segundo)", anchor="middle")
    pista(b, cx_ + 150, top + 182, "(cada segundo)", anchor="middle")
    tx = x0 + 500
    cols = (260, 210, ww - 500 - 470)
    tabla_vacia(b, tx, yy, cols, ("MOMENTO", "¿QUÉ LADO GANA?", "¿Y LA RAPIDEZ DEL GIRO?"),
                ("al encender", "a los pocos minutos", "si apago las velas"), c, rh=80, size=16)
    yy += 310
    caja_preg(b, x0, yy, ww, 104, c, "LA PALABRA DEL LIBRO",
              "«Se estabiliza» quiere decir que la rapidez ya no cambia. ¿Eso significa que no hay fuerzas, o que "
              "las que hay se compensan?")
    yy += 124
    return ojo(b, x0, yy, ww, "LA FRICCIÓN CRECE CON LA RAPIDEZ",
               "Mientras más rápido giran las aspas, más las frena el roce del eje y del aire. Piensa qué le pasa a tu "
               "balanza cuando el giro se acelera: ¿el platillo de la fricción se queda igual o se va llenando?")


# ───────── P6 · cuatro velas, diez minutos ─────────
def i6(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Velas por minutos por kilojulios", c,
                      "Escribe cada dato con su unidad completa y tacha las unidades que se cancelan. La que sobrevive "
                      "te dice si la cuenta está bien armada.")
    x0, ww = x + 22, w - 44
    fw = (ww - 3 * 70) / 4
    labs = (("CUÁNTAS VELAS", "velas"), ("CUÁNTO DA CADA UNA", "kJ / (vela · min)"),
            ("CUÁNTO TIEMPO", "min"), ("RESULTADO", "kJ"))
    for k, (t1, u) in enumerate(labs):
        bx = x0 + k * (fw + 70)
        caja(b, bx, yy, fw, 170, c, r=14, sw=2.4, fill=tinte(c, 0.95) if k == 3 else "white")
        rot(b, bx + 16, yy + 30, t1, c, size=14)
        renglon(b, bx + 16, yy + 100, bx + fw - 16)
        texto(b, bx + 16, yy + 140, u, size=18, color=c, weight="700")
        if k < 3:
            texto(b, bx + fw + 35, yy + 98, "×" if k < 2 else "=", size=36, color=c, weight="700", anchor="middle")
    yy += 190
    caja(b, x0, yy, ww, 120, c, r=14, dash="8,6")
    rot(b, x0 + 20, yy + 30, "COMPRUEBO CON OTRAS CANTIDADES", c)
    pista(b, x0 + 20, yy + 66, "con 1 vela y 10 min:")
    renglon(b, x0 + 190, yy + 68, x0 + 330)
    texto(b, x0 + 340, yy + 66, "kJ", size=17, weight="700")
    pista(b, x0 + 420, yy + 66, "con 5 velas y 10 min:")
    renglon(b, x0 + 600, yy + 68, x0 + 740)
    texto(b, x0 + 750, yy + 66, "kJ", size=17, weight="700")
    pista(b, x0 + 20, yy + 104, "¿mi resultado queda entre los dos?")
    sino(b, x0 + 290, yy + 88, c)
    yy += 140
    return trampa(b, x0, yy, ww, "El texto y la pregunta no usan el mismo número de velas:",
                  "el montaje del libro tiene cinco velas; esta versión del experimento usa otra cantidad. Subraya en "
                  "la pregunta cuántas velas y cuántos minutos, y usa esos.", c)


# ───────── P7 · de la cera al aspa ─────────
def i7(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Eslabón por eslabón, de la cera al aspa", c,
                      "El texto del libro cuenta una cadena de transformaciones. Escribe en cada eslabón la forma de "
                      "energía y dónde está. Después prueba qué pasa si cortas la cadena.")
    x0, ww = x + 22, w - 44
    ew = (ww - 3 * 40) / 4
    eslab = (("1 · EN LA CERA", "energía…"), ("2 · EN LA LLAMA", "energía… y…"),
             ("3 · EN EL AIRE QUE SUBE", "energía…"), ("4 · EN LAS ASPAS", "energía…"))
    for k, (t1, ps) in enumerate(eslab):
        bx = x0 + k * (ew + 40)
        caja(b, bx, yy, ew, 150, c, r=40, sw=2.6)
        rot(b, bx + 24, yy + 36, t1, c, size=14)
        pista(b, bx + 24, yy + 66, ps)
        renglon(b, bx + 24, yy + 112, bx + ew - 24)
        if k < 3:
            flecha(b, bx + ew + 4, yy + 75, bx + ew + 36, yy + 75, c, head=10)
    yy += 170
    half = (ww - 24) / 2
    caja_preg(b, x0, yy, half, 140, c, "SI APAGO LAS VELAS",
              "¿qué eslabón se corta primero? ¿qué le pasa al giro después de un rato?", 2)
    caja_preg(b, x0 + half + 24, yy, half, 140, c, "CUANDO LAS ASPAS SE DETIENEN",
              "su energía de movimiento terminó como…", 2)
    yy += 160
    return ojo(b, x0, yy, ww, "UNA PREDICCIÓN COHERENTE SIGUE LA CADENA",
               "Recorre la cadena dos veces: una con las velas encendidas y otra con las velas apagadas, y escribe qué "
               "le pasa a cada eslabón. Una predicción es coherente si no le pide a ningún eslabón entregar energía que "
               "no recibió.")


# ───────── P8 · equilibrio térmico ─────────
def i8(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Dos temperaturas que se encuentran", c,
                      "Dibuja en la gráfica cómo cambia la temperatura del agua y la del aire de la sala con el tiempo. "
                      "Usa un color para cada una. Marca el momento en que el calor deja de pasar.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 640, 380, c, r=16)
    gx, gy, gw, gh = x0 + 80, yy + 30, 520, 290
    b.append(line(gx, gy, gx, gy + gh, INK, 2.2))
    b.append(line(gx, gy + gh, gx + gw, gy + gh, INK, 2.2))
    for j, t in enumerate(("20", "40", "60", "80")):
        yv = gy + gh - (j + 1) * gh / 4.4
        b.append(line(gx - 6, yv, gx + 6, yv, INK, 2))
        texto(b, gx - 12, yv + 5, t, size=14, color=GRAY, anchor="end")
    b.append(T(x0 + 26, gy + gh / 2, ["temperatura (°C)"], 15, GRAY, style="italic", anchor="middle", rot=-90))
    pista(b, gx + gw / 2, gy + gh + 40, "tiempo", anchor="middle")
    b.append(f'<circle cx="{gx}" cy="{gy + gh - 4 * gh / 4.4}" r="7" fill="{EDU_ROJO}"/>')
    b.append(f'<circle cx="{gx}" cy="{gy + gh - 1 * gh / 4.4}" r="7" fill="{EDU_AZUL}"/>')
    pista(b, gx + 14, gy + gh - 4 * gh / 4.4 - 10, "agua al empezar")
    pista(b, gx + 14, gy + gh - 1 * gh / 4.4 - 10, "sala al empezar")
    rx, rw = x0 + 670, ww - 670
    qs = (("HACIA DÓNDE VA EL CALOR", "de ________ a ________"),
          ("CUÁNDO SE DETIENE", "cuando las dos temperaturas…"),
          ("¿Y LA SALA?", "¿se calienta mucho, poco o nada? ¿por qué?"))
    for k, (tit, ps) in enumerate(qs):
        caja_preg(b, rx, yy + k * 128, rw, 116, c, tit, ps)
    yy += 400
    return trampa(b, x0, yy, ww, "Dos preguntas para cada opción:",
                  "¿a dónde dice que se fue el calor del agua? ¿hasta cuándo dice que sigue pasando? Compara las dos "
                  "respuestas de cada opción con lo que escribiste a la derecha de la gráfica.", c)


# ───────── P9 · dos resistencias en paralelo ─────────
def i9(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El cruce donde se reparte la corriente", c,
                      "La corriente es como agua en tubos: lo que llega a un cruce es lo mismo que sale por las ramas. "
                      "Escribe en el dibujo cuánto pasa por cada camino y comprueba con la ley de Ohm.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 620, 330, c, r=16)
    lx, rx_, ty, by = x0 + 90, x0 + 560, yy + 60, yy + 280
    b.append(line(lx, ty, rx_, ty, INK, 2.4))
    b.append(line(lx, by, rx_, by, INK, 2.4))
    b.append(line(lx, ty, lx, ty + 80, INK, 2.4))
    b.append(line(lx, ty + 140, lx, by, INK, 2.4))
    b.append(line(lx - 24, ty + 80, lx + 24, ty + 80, INK, 3))
    b.append(line(lx - 13, ty + 96, lx + 13, ty + 96, INK, 3))
    b.append(line(lx - 24, ty + 112, lx + 24, ty + 112, INK, 3))
    b.append(line(lx - 13, ty + 128, lx + 13, ty + 128, INK, 3))
    b.append(line(lx, ty + 128, lx, ty + 140, INK, 2.4))
    texto(b, lx - 32, ty + 112, "12 V", size=16, weight="700", anchor="end")
    vector(b, lx + 40, ty - 18, lx + 120, ty - 18, INK, sw=2, head=9)
    texto(b, lx + 130, ty - 12, "4 A en total", size=16, weight="700")
    for k, rxx in enumerate((x0 + 270, x0 + 470)):
        b.append(line(rxx, ty, rxx, ty + 60, INK, 2.4))
        b.append(rect(rxx - 16, ty + 60, 32, 100, "white", r=2, stroke=INK, sw=2.2))
        b.append(line(rxx, ty + 160, rxx, by, INK, 2.4))
        b.append(f'<circle cx="{rxx}" cy="{ty}" r="6" fill="{INK}"/>')
        b.append(f'<circle cx="{rxx}" cy="{by}" r="6" fill="{INK}"/>')
        texto(b, rxx - 26, ty + 116, "R", size=17, weight="700", anchor="end")
        vector(b, rxx + 30, ty + 70, rxx + 30, ty + 130, INK, sw=2, head=8)
        caja(b, rxx + 44, ty + 84, 50, 34, c, r=6)
        texto(b, rxx + 100, ty + 108, "A", size=16, weight="700")
    yy2 = yy
    rx, rw = x0 + 650, ww - 650
    caja(b, rx, yy2, rw, 150, c, r=14)
    rot(b, rx + 16, yy2 + 28, "REGLA DEL CRUCE", c, size=14)
    ecuacion(b, rx + 16, yy2 + 76, [("t", "4 A ="), ("h", 80), ("t", "A +"), ("h", 80), ("t", "A")], c, size=18)
    pista(b, rx + 16, yy2 + 120, "si las dos ramas son iguales, ¿cómo se reparte?")
    caja(b, rx, yy2 + 170, rw, 160, c, r=14)
    rot(b, rx + 16, yy2 + 198, "COMPRUEBO CON OHM", c, size=14)
    ecuacion(b, rx + 16, yy2 + 246, [("t", "R = V ÷ I = 12 V ÷"), ("h", 70), ("t", "A ="), ("h", 70), ("t", "Ω")], c,
             size=18)
    pista(b, rx + 16, yy2 + 296, "cada resistencia recibe los 12 V completos")
    yy += 350
    return trampa(b, x0, yy, ww, "Revisa la unidad antes de marcar:",
                  "en esta pregunta salen números que son corrientes (amperios) y números que son resistencias "
                  "(ohmios). Una opción solo puede ser la corriente de una rama si está en amperios y si las dos "
                  "ramas, sumadas, dan la total.", c)


# ───────── P10 · eficiencia del cargador ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Lo que entra, lo que se guarda y lo que falta", c,
                      "15 W quiere decir 15 julios cada segundo. Calcula cuánta energía entregó la toma en una hora y "
                      "reparte esa energía entre lo que midieron. Después revisa la conclusión por partes.")
    x0, ww = x + 22, w - 44
    pasos = (("1 · LO QUE ENTREGA LA TOMA", [("t", "15 J/s  ×  3600 s  ="), ("h", 150), ("t", "J  ="), ("h", 90),
                                            ("t", "kJ")]),
             ("2 · LO QUE SE GUARDÓ", [("t", "45 kJ  ÷"), ("h", 90), ("t", "kJ  ="), ("h", 90), ("t", "→"),
                                       ("h", 80), ("t", "%")]),
             ("3 · LO QUE SE MIDIÓ EN TOTAL", [("t", "45 kJ  +  6 kJ  ="), ("h", 100), ("t", "kJ")]),
             ("4 · LO QUE NO SE MIDIÓ", [("t", "lo que entregó la toma  −  lo medido  ="), ("h", 100), ("t", "kJ")]))
    for k, (tit, partes) in enumerate(pasos):
        py = yy + k * 94
        caja(b, x0, py, ww, 82, c, r=14, fill=tinte(c, 0.96) if k % 2 == 0 else "white")
        rot(b, x0 + 20, py + 28, tit, c, size=14)
        ecuacion(b, x0 + 20, py + 64, partes, c, size=18)
    yy += 4 * 94 + 6
    half = (ww - 24) / 2
    for k, parte in enumerate(("«la eficiencia real es del 83 %»", "«no existen otras pérdidas»")):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 120, c, r=14, sw=2.4)
        rot(b, bx + 16, yy + 28, "PARTE " + str(k + 1) + " DE LA CONCLUSIÓN", c, size=14)
        texto(b, bx + 16, yy + 60, parte, size=17, weight="700")
        pista(b, bx + 16, yy + 98, "¿se sostiene con mis cuentas?")
        sino(b, bx + 250, yy + 82, c)
    yy += 140
    return alto_profe(b, x0, yy, ww,
                      "Potencia: es la energía por segundo. 1 vatio (W) = 1 julio cada segundo (J/s). Por eso energía = "
                      "potencia × tiempo, con el tiempo en segundos. Pídele al profe que lo muestre con el bombillo de "
                      "tu casa: ¿cuánta energía gasta uno de 10 W en una noche de 8 horas?")


Q = {1: dict(n=1, est=3, pag=259, ctx="Calor de un centro de datos · ¿la eficiencia es del 100 %?",
             comp="Indagación", inst=i1),
     2: dict(n=2, est=2, pag=260, ctx="Motor de una banda · por qué entrega menos de lo que consume",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=1, pag=260, ctx="Motor de una banda transportadora · la fracción de energía útil",
             comp="Uso comprensivo del conocimiento científico", inst=i3),
     4: dict(n=4, est=3, pag=260, ctx="Motor de una banda transportadora · ¿una hora basta para concluir?",
             comp="Indagación", inst=i4),
     5: dict(n=5, est=4, pag=261, ctx="Molinillo de convección · por qué el giro deja de acelerar",
             comp="Explicación de fenómenos", inst=i5),
     6: dict(n=6, est=1, pag=261, ctx="Molinillo de convección · energía química de cuatro velas",
             comp="Uso comprensivo del conocimiento científico", inst=i6),
     7: dict(n=7, est=2, pag=261, ctx="Molinillo de convección · qué predicción respeta la conservación",
             comp="Explicación de fenómenos", inst=i7),
     8: dict(n=8, est=4, pag=261, ctx="Agua caliente en la sala · qué pasa hasta el equilibrio",
             comp="Explicación de fenómenos", inst=i8),
     9: dict(n=9, est=1, pag=262, ctx="Dos resistencias iguales en paralelo · corriente por cada una",
             comp="Uso comprensivo del conocimiento científico", inst=i9),
     10: dict(n=10, est=3, pag=262, ctx="Cargador de celular de 15 W · ¿la conclusión es adecuada?",
              comp="Indagación", inst=i10)}


def build(pages=(261, 262, 264, 265, 266)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"fis6_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
