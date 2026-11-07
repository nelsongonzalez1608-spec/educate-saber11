#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 3 · componente químico, aspectos analíticos de mezclas · páginas 197–203.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 3» de Química (fuente_libro/QUÍMICA), páginas 160–162.
Casos: tres estudiantes disuelven ácido cítrico (1), la tableta efervescente de vitamina C en
agua, bebida energizante con gas y bebida deportiva sin gas (2 a 4), el aceite de motor sobre
un charco (5), la llanta de la bicicleta (6), el protector solar en spray (7) y la cafetera
japonesa tipo sifón (8 a 10).

Claves verificadas (resueltas a mano contra el texto y la tabla del libro, no copiadas, 7 nov 2026):

    1·B  2·B  3·C  4·A  5·B  6·D  7·A  8·C  9·A  10·D

Cómo se resolvieron:
  1 · Meta doble: disolución completa (sin residuos) y menor tiempo. Ana: 10 min y quedan
      cristales (no cumple). Felipe: 6 min y turbidez (no cumple «sin residuos visibles»). Luis:
      4 min y solución transparente (cumple las dos) → B. D también elige a Luis, pero dice que
      la agitación «compensa la baja temperatura»: 35 °C no es la temperatura baja de la tabla
      (la de Ana es 20 °C). OJO: Luis cambió dos condiciones a la vez (temperatura y agitación);
      los datos no dejan saber cuál de las dos pesó más (hallazgo).
  2 · Lo único que el texto distingue del vaso 2 es el gas (los tres a temperatura ambiente,
      200 mL, vasos idénticos) → B: el burbujeo del gas agita y acelera la disolución. A (acidez)
      y D (catalizador que cambia la tableta) usan datos que el texto no da; C (el color) no
      cambia la velocidad. OJO: A es químicamente defendible (la tableta reacciona ácido +
      bicarbonato y una bebida ácida aporta), pero el texto no dice nada de acidez y la bebida
      deportiva también suele ser ácida: hallazgo Media.
  3 · Evidencia del efecto del gas: algo que pasa en el vaso con gas y no en sus testigos → C
      (más espuma y burbujas en el vaso 2). A pasa en los tres; B habla del vaso 3; D afirma algo
      del vaso de agua que no prueba nada sobre el gas.
  4 · Objetivo: ver la efervescencia sin espuma de más ni desorden → el agua (A): efervescencia
      moderada que se queda en el vaso. B tiene espuma de más; C justifica con que «tarda más»
      (no es la meta); D es falsa (ver la tableta no prueba que no reaccionó).
  5 · Dos fases visibles que no se mezclan (el aceite flota sobre el agua) → B. Los colores (A)
      son interferencia de la luz en la capa delgada, no una reacción.
  6 · El manómetro sigue en el rango adecuado: salió poco aire y la presión se mantiene → D.
  7 · Se separa en gotas al cabo de cinco minutos de reposo → inestable (A). C juzga por el
      primer instante.
  8 · Al calentar, el vapor de abajo aumenta la presión y empuja el agua hacia arriba; al
      apagar, el vapor se condensa, baja la presión (vacío parcial) y el líquido baja → C.
  9 · Clave propuesta A, con reserva (hallazgo Alta). El vacío parcial jala el líquido y, cuando
      el de arriba se acaba, jala aire por el filtro y el tubo: ese burbujeo hace la espuma. A
      dice bien el mecanismo (vacío que succiona aire) pero dice «a través de las juntas» (el
      aire entra por arriba, el recipiente superior está abierto). B dice que el aire atrapado
      «se libera al disminuir la temperatura»: al revés de la solubilidad de los gases (un
      líquido frío retiene MÁS gas). C (evaporación súbita) y D (fermentación) no tienen apoyo.
      Ninguna opción es limpia; hay que confirmar la clave con el solucionario de la editorial.
 10 · Todo lo que pasó se explica con presión, calor y filtración; no aparece ninguna sustancia
      nueva → D (separación física sin transformación). A llama al café «coloide que cambia de
      fase», B y C suponen una reacción o una descomposición sin evidencia.

Reparto: A 3 · B 3 · C 2 · D 2. Equilibrado.

Estrategias:
    1 · Cambia una sola cosa a la vez          (1, 3, 4     · ICFES 91)   azul
    2 · Clasifica por lo que se observa        (5, 7        · ICFES 65)   rojo
    3 · Sigue al gas: presión y temperatura    (6, 8, 9     · ICFES 95)   morado
    4 · Pide la evidencia antes de creer       (2, 10       · ICFES 113)  oro

Hojas: 197 qui3_t1 (1-2) · 198 qui3_t2 (3-4) · 199 qui3_i1 · 200 qui3_t3 (5-6) ·
       201 qui3_t4 (7-8) · 202 qui3_t5 (9-10) · 203 qui3_i2.
"""
from taller_base import *

configurar("Química", 3, "químico · aspectos analíticos de mezclas",
           tema="Mezclar no es transformar",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Cambia una sola cosa a la vez", EDU_AZUL),
       2: ("Clasifica por lo que se observa", EDU_ROJO),
       3: ("Sigue al gas: presión y temperatura", MORADO),
       4: ("Pide la evidencia antes de creer", EDU_ORO)}
usar_estrategias(EST)
AZ, RO, MO, OR = (EST[k][1] for k in (1, 2, 3, 4))
ESM = A["color"]
AGUA = "#DCEAF7"


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


def frase_hueco(b, x, y, w, texto, c, h=50, size=18):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [texto], size, INK, weight="700"))
    return y + h


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12):
    """Flecha recta (para esquemas)."""
    b.append(line(x1, y1, x2, y2, c, sw))
    ang = math.atan2(y2 - y1, x2 - x1)
    for s in (-1, 1):
        a = ang + math.pi + s * 0.45
        b.append(line(x2, y2, x2 + head * math.cos(a), y2 + head * math.sin(a), c, sw))


def vaso(b, x, y, w, h, c, nivel=None, liquido=None, sw=2.6):
    """Vaso de precipitados: boca abierta arriba, pico a la izquierda. nivel = fracción llena."""
    if nivel is not None:
        ly = y + h * (1 - nivel)
        b.append(rect(x + 3, ly, w - 6, y + h - ly - 3, liquido or AGUA, r=6))
        b.append(line(x + 3, ly, x + w - 3, ly, c, 1.6, dash="6,5"))
    b.append(f'<path d="M {x - 10} {y - 6} L {x} {y + 6} L {x} {y + h - 8} Q {x} {y + h} {x + 8} {y + h} '
             f'L {x + w - 8} {y + h} Q {x + w} {y + h} {x + w} {y + h - 8} L {x + w} {y - 4}" fill="none" '
             f'stroke="{c}" stroke-width="{sw}"/>')


def casillas(b, x, y, labels, c, paso=150, size=16):
    for k, lab in enumerate(labels):
        b.append(checkbox(x + k * paso, y, s=10, c=c))
        b.append(T(x + k * paso + 28, y + 16, [lab], size, GRAY))


# ───────── P1 · ácido cítrico · el procedimiento más exitoso ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos metas, tres procedimientos", c,
                      "El objetivo pide dos cosas a la vez: que no quede nada sin disolver y que se logre en el menor "
                      "tiempo. Ana es el punto de partida (20 °C, sin agitar). Compara a Luis y a Felipe con ella y "
                      "pásalos a los tres por las dos metas.")
    x0, ww = x + 22, w - 44
    cols = (("ESTUDIANTE", 190), ("¿CAMBIÓ LA TEMPERATURA?", 260), ("¿CAMBIÓ LA AGITACIÓN?", 250),
            ("META 1 · SIN RESIDUOS", 266), ("META 2 · MINUTOS", 260))
    hy = yy + 6
    px = x0
    for t, cw in cols:
        caja(b, px, hy, cw, 52, c, r=0, fill=A["bg"])
        rot(b, px + cw / 2, hy + 32, t, c, size=13, anchor="middle")
        px += cw
    for k, nom in enumerate(("Ana", "Luis", "Felipe")):
        ry = hy + 52 + k * 62
        px = x0
        for j, (t, cw) in enumerate(cols):
            caja(b, px, ry, cw, 62, c, r=0)
            if j == 0:
                b.append(T(px + 20, ry + 39, [nom], 19, INK, weight="700"))
            elif k == 0 and j in (1, 2):
                pista(b, px + cw / 2, ry + 38, "punto de partida", anchor="middle")
            elif j in (1, 2, 3):
                casillas(b, px + cw / 2 - 70, ry + 20, ("sí", "no"), c, paso=90)
            else:
                caja(b, px + cw / 2 - 50, ry + 12, 100, 38, c, r=8)
            px += cw
    yy = hy + 52 + 3 * 62 + 22
    yy = frase_hueco(b, x0, yy, ww, "Cumple las dos metas: ______________ , y cambió ______ condiciones respecto a "
                                    "Ana.", c)
    yy = ojo(b, x0, yy + 16, ww, "SI CAMBIAS DOS COSAS A LA VEZ",
             "sabes que la combinación funcionó, pero no cuál de las dos lo logró. Por eso la mejor opción es la que "
             "dice lo que los datos sí muestran. Y revisa los números que cita cada opción: si habla de una "
             "temperatura «baja», búscala en la tabla.")
    return yy


# ───────── P2 · tableta efervescente · por qué en la bebida con gas ─────────
def i2(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Lo que había en cada vaso antes de la tableta", c,
                      "Antes de explicar, haz el inventario. Escribe debajo de cada vaso lo que el texto dice que "
                      "tiene. Después separa lo que el texto sí dice de lo que tendrías que suponer para creerle a "
                      "cada explicación.")
    x0, ww = x + 22, w - 44
    nombres = (("VASO 1", "agua"), ("VASO 2", "bebida energizante con gas"), ("VASO 3", "bebida deportiva sin gas"))
    gw = (ww - 2 * 30) / 3
    for k, (v, d) in enumerate(nombres):
        gx = x0 + k * (gw + 30)
        vaso(b, gx + 30, yy + 34, 120, 130, c, nivel=0.7)
        rot(b, gx + 176, yy + 50, v, c, size=14)
        pista(b, gx + 176, yy + 74, d)
        pista(b, gx + 176, yy + 112, "el texto dice que tiene:")
        renglon(b, gx + 176, yy + 146, gx + gw - 4)
        renglon(b, gx + 176, yy + 178, gx + gw - 4)
    yy += 206
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("LO QUE EL TEXTO SÍ DICE", "de los tres vasos y del experimento"),
                                  ("LO QUE TENDRÍA QUE SUPONER", "datos que el texto no da"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 150, c, r=14, dash=None if k == 0 else "8,6")
        rot(b, px + 18, yy + 28, rt, c, size=14)
        pista(b, px + 18, yy + 52, ps)
        for j in range(2):
            renglon(b, px + 18, yy + 92 + j * 40, px + half - 18)
    yy += 166
    yy = frase_hueco(b, x0, yy, ww, "Lo único que el vaso 2 tiene y los otros dos no, según el texto: "
                                    "______________________ .", c)
    return ojo(b, x0, yy + 16, ww, "Una explicación química también necesita evidencia:",
               "si una opción explica con algo que el texto nunca midió ni mencionó, está suponiendo. Primero lo que "
               "el texto dice; después la química.")


# ───────── P3 · tableta efervescente · la evidencia del gas ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El vaso testigo", c,
                      "Para saber qué hace el gas, el vaso con gas se compara con un vaso igual en todo, menos en el "
                      "gas: ese es su testigo. Escribe qué cambia en cada pareja y encierra la que solo se diferencia "
                      "en el gas.")
    x0, ww = x + 22, w - 44
    parejas = (("1 y 2", ("agua", "energizante con gas")), ("2 y 3", ("energizante con gas", "deportiva sin gas")),
               ("1 y 3", ("agua", "deportiva sin gas")))
    pw = (ww - 2 * 26) / 3
    for k, (par, _) in enumerate(parejas):
        px = x0 + k * (pw + 26)
        caja(b, px, yy, pw, 236, c, r=16)
        rot(b, px + 18, yy + 30, f"VASOS {par}", c, size=15)
        a, bb = par.split(" y ")
        for j, n in enumerate((a, bb)):
            vx = px + 40 + j * 150
            vaso(b, vx, yy + 54, 80, 86, c, nivel=0.65, sw=2.2)
            b.append(T(vx + 40, yy + 112, [n], 22, c, weight="700", anchor="middle"))
        pista(b, px + 18, yy + 176, "lo que cambia entre los dos:")
        renglon(b, px + 18, yy + 214, px + pw - 18)
    yy += 256
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE SE VE EN EL VASO 2 Y NO SE VE EN SU TESTIGO", c, size=14)
    renglon(b, x0 + 20, yy + 82, x0 + ww - 20)
    yy += 120
    return ojo(b, x0, yy, ww, "UNA EVIDENCIA TIENE QUE MARCAR LA DIFERENCIA",
               "si algo pasa igual en los tres vasos, no dice nada sobre el gas. Y si una opción habla de un vaso que "
               "no es el que tiene gas, pregúntate qué prueba eso sobre el gas.")


# ───────── P4 · tableta efervescente · cuál líquido elegir ─────────
def i4(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La franja que pide el objetivo", c,
                      "La regla va de «no se ve nada» a «la espuma se sale del vaso». Sombrea con lápiz la franja que "
                      "pide el objetivo. Después ubica cada vaso en la regla, según el texto y la figura del libro: "
                      "escribe su número encima.")
    x0, ww = x + 22, w - 44
    ly = yy + 84
    L, R = x0 + 30, x0 + ww - 30
    seg = (R - L) / 5
    etiquetas = ("no se ve\nefervescencia", "pocas\nburbujas", "efervescencia\nque se ve bien", "mucha\nespuma",
                 "la espuma se\nsale del vaso")
    for k in range(5):
        caja(b, L + k * seg, ly - 30, seg, 60, c, r=0)
        for j, t in enumerate(etiquetas[k].split("\n")):
            pista(b, L + k * seg + seg / 2, ly + 58 + j * 20, t, anchor="middle")
    pista(b, L, ly - 46, "escribe dentro de la regla el número de cada vaso (1, 2, 3) donde creas que cae")
    yy = ly + 110
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("LA META, CON MIS PALABRAS", "¿qué quiero ver y qué no quiero que pase?"),
                                  ("LA RAZÓN TIENE QUE HABLAR DE LA META", "¿cuál razón de las opciones habla de otra cosa?"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 120, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        pista(b, px + 18, yy + 52, ps)
        renglon(b, px + 18, yy + 98, px + half - 18)
    yy += 136
    yy = frase_hueco(b, x0, yy, ww, "El vaso que cae dentro de la franja es el ______ .", c)
    return trampa(b, x0, yy + 16, ww, "Una opción dice que, si la tableta se sigue viendo, no hubo reacción:",
                  "¿qué te dicen las burbujas? Una tableta a medio disolver puede estar reaccionando todavía.", c)


# ───────── P5 · aceite sobre el charco ─────────
def i5(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Dos lupas sobre el charco", c,
                      "Dibuja el charco cortado de lado, como si lo partieras con un cuchillo: de abajo hacia arriba, "
                      "qué hay encima del asfalto. Después usa las dos lupas para nombrar lo que ves arriba y abajo.")
    x0, ww = x + 22, w - 44
    cw_ = 640
    caja(b, x0, yy, cw_, 290, c, r=14)
    rot(b, x0 + 18, yy + 28, "EL CHARCO, CORTADO DE LADO", c, size=14)
    b.append(rect(x0 + 20, yy + 236, cw_ - 40, 34, "#C9CED6", r=4))
    b.append(T(x0 + cw_ / 2, yy + 259, ["asfalto"], 15, INK, weight="700", anchor="middle"))
    pista(b, x0 + cw_ / 2, yy + 140, "dibuja aquí lo que hay encima del asfalto", anchor="middle")
    lx = x0 + cw_ + 40
    lw = x0 + ww - lx
    for k, (rt, ps) in enumerate((("LUPA ARRIBA", "¿qué sustancia veo?"), ("LUPA ABAJO", "¿qué sustancia veo?"))):
        ly = yy + k * 152
        b.append(f'<circle cx="{lx + 56}" cy="{ly + 64}" r="44" fill="white" stroke="{c}" stroke-width="3"/>')
        b.append(line(lx + 88, ly + 96, lx + 116, ly + 124, c, 6))
        rot(b, lx + 130, ly + 36, rt, c, size=14)
        pista(b, lx + 130, ly + 60, ps)
        renglon(b, lx + 130, ly + 100, lx + lw)
        pista(b, lx + 130, ly + 130, "¿se mezcla con la otra?   sí  /  no")
    yy += 310
    yy = frase_hueco(b, x0, yy, ww, "Cuento ______ fases que se distinguen a simple vista; por eso la mezcla es "
                                    "______________ .", c)
    return alto_profe(b, x0, yy + 16, ww,
                      "Pregúntale al profe por qué una capa muy delgada de aceite se ve de colores (violeta, verde) "
                      "sobre el agua: ¿es una sustancia nueva o es la luz que se refleja en la capa?")


# ───────── P6 · la llanta de la bicicleta ─────────
def _manometro(b, cx, cy, r, c):
    b.append(f'<path d="M {cx - r} {cy} A {r} {r} 0 0 1 {cx + r} {cy}" fill="white" stroke="{c}" '
             f'stroke-width="3"/>')
    b.append(line(cx - r, cy, cx + r, cy, c, 3))
    for k, (a0, a1, t) in enumerate(((180, 240, "baja"), (240, 300, "adecuada"), (300, 360, "alta"))):
        am = math.radians((a0 + a1) / 2)
        for a in (a0, a1):
            ar = math.radians(a)
            b.append(line(cx + (r - 22) * math.cos(ar), cy + (r - 22) * math.sin(ar), cx + r * math.cos(ar),
                          cy + r * math.sin(ar), c, 2.4))
        b.append(T(cx + (r - 46) * math.cos(am), cy + (r - 46) * math.sin(am) + 5, [t], 14, GRAY, anchor="middle"))
    b.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="{c}"/>')


def i6(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El ruido y la aguja", c,
                      "Dos instrumentos te hablan: el oído y el manómetro. Dibuja la aguja en cada momento según el "
                      "texto y escribe qué dice cada uno. Después decide cuál mide lo que quedó adentro de la llanta.")
    x0, ww = x + 22, w - 44
    r = 120
    for k, t in enumerate(("1 · ANTES DE DESCONECTAR", "2 · DESPUÉS DEL ESCAPE")):
        cx = x0 + 150 + k * 320
        rot(b, cx, yy + 22, t, c, size=13, anchor="middle")
        _manometro(b, cx, yy + 170, r, c)
    rx = x0 + 680
    rw = x0 + ww - rx
    for k, (rt, ps) in enumerate((("EL RUIDO ME DICE QUE…", "¿salió algo?"),
                                  ("LA AGUJA ME DICE QUE…", "¿cuánto quedó adentro?"))):
        ry = yy + k * 104
        caja(b, rx, ry, rw, 92, c, r=14)
        rot(b, rx + 18, ry + 28, rt, c, size=14)
        pista(b, rx + 260, ry + 28, ps)
        renglon(b, rx + 18, ry + 74, rx + rw - 18)
    yy += 214
    yy = frase_hueco(b, x0, yy, ww, "Salió __________ del aire, y la presión ______________ .", c)
    return ojo(b, x0, yy + 16, ww, "UNA PISTA NO PESA LO MISMO QUE UNA MEDIDA",
               "el escape se oyó, eso es cierto. Pero la presión que marca el manómetro es una medida de lo que hay "
               "adentro. Cuando parecen contradecirse, ¿a cuál le crees más? Compara cada opción con tu aguja.")


# ───────── P7 · protector solar en spray ─────────
def i7(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La película del protector en tres cuadros", c,
                      "Dibuja cómo se ve el producto sobre el vidrio en cada momento, como si fueran tres fotos "
                      "seguidas. Una mezcla se clasifica por lo que le pasa con el tiempo, no por cómo se ve al "
                      "primer instante.")
    x0, ww = x + 22, w - 44
    cuadros = ("1 · RECIÉN AGITADO", "2 · PRIMEROS SEGUNDOS", "3 · A LOS CINCO MINUTOS")
    gap = 30
    fw = (ww - 2 * gap) / 3
    for k, t in enumerate(cuadros):
        fx = x0 + k * (fw + gap)
        caja(b, fx, yy, fw, 250, c, r=14)
        rot(b, fx + 18, yy + 28, t, c, size=14)
        b.append(rect(fx + 18, yy + 44, fw - 36, 130, "#F5F7FA", r=8, stroke="#C9CED6", sw=1.6))
        pista(b, fx + fw / 2, yy + 114, "el vidrio: dibuja aquí", anchor="middle")
        casillas(b, fx + 22, yy + 196, ("uniforme", "en gotas"), c, paso=150)
        if k < 2:
            b.append(hand_arrow(fx + fw + 4, yy + 110, fx + fw + gap - 4, yy + 110, c, sw=2.4, bend=0.0, head=10))
    yy += 268
    half = (ww - 24) / 2
    for k, rt in enumerate(("UNA MEZCLA ESTABLE, CON EL TIEMPO…", "UNA MEZCLA INESTABLE, CON EL TIEMPO…")):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 96, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        renglon(b, px + 18, yy + 76, px + half - 18)
    yy += 112
    return trampa(b, x0, yy, ww, "Mira tus tres cuadros antes de leer las opciones:",
                  "si una opción clasifica el producto mirando solo el primer cuadro, no está usando la evidencia "
                  "de los cinco minutos. Y si explica con algo que nadie observó sobre el vidrio, tampoco.", c)


# ───────── P8 · cafetera de sifón · por qué sube y baja ─────────
def _sifon(b, cx, top, c, fuego):
    """Esquema de la cafetera de sifón: globo de arriba, tubo y globo de abajo."""
    b.append(rect(cx - 70, top, 140, 100, "white", r=30, stroke=c, sw=2.6))
    b.append(line(cx, top + 100, cx, top + 170, c, 4))
    b.append(f'<circle cx="{cx}" cy="{top + 220}" r="62" fill="white" stroke="{c}" stroke-width="2.6"/>')
    if fuego:
        for d in (-22, 0, 22):
            b.append(f'<path d="M {cx + d - 9} {top + 312} Q {cx + d} {top + 284} {cx + d + 9} {top + 312} Z" '
                     f'fill="{AMBER_BG}" stroke="{AMBER_D}" stroke-width="2"/>')
    pista(b, cx + 80, top + 30, "arriba", size=14)
    pista(b, cx + 72, top + 222, "abajo", size=14)


def i8(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El sifón en dos tiempos", c,
                      "Lo que mueve el agua es la diferencia de presión entre el recipiente de abajo y el de arriba. "
                      "En cada tiempo, dibuja con una flecha hacia dónde va el líquido y completa qué pasa con el "
                      "vapor y con la presión abajo.")
    x0, ww = x + 22, w - 44
    pw = (ww - 30) / 2
    for k, (t, fuego) in enumerate((("1 · CALENTANDO", True), ("2 · AL APAGAR LA FUENTE", False))):
        px = x0 + k * (pw + 30)
        caja(b, px, yy, pw, 376, c, r=16)
        rot(b, px + 18, yy + 28, t, c, size=14)
        _sifon(b, px + 120, yy + 46, c, fuego)
        tx = px + 260
        b.append(T(tx, yy + 76, ["Abajo, el vapor de agua…"], 16, INK))
        renglon(b, tx, yy + 110, px + pw - 18)
        b.append(T(tx, yy + 152, ["La presión abajo…"], 16, INK))
        casillas(b, tx, yy + 166, ("sube", "baja"), c, paso=110)
        b.append(T(tx, yy + 238, ["El líquido va hacia…"], 16, INK))
        casillas(b, tx, yy + 252, ("arriba", "abajo"), c, paso=110)
    yy += 392
    return alto_profe(b, x0, yy, ww,
                      "Pregúntale al profe qué le pasa al vapor de agua cuando se enfría dentro de un recipiente "
                      "cerrado y por qué eso deja un «vacío parcial» que jala el líquido.")


# ───────── P9 · cafetera de sifón · la espuma al bajar ─────────
def _botella(b, cx, by, c, frio):
    b.append(f'<path d="M {cx - 34} {by} L {cx - 34} {by - 130} Q {cx - 34} {by - 160} {cx - 12} {by - 176} '
             f'L {cx - 12} {by - 206} L {cx + 12} {by - 206} L {cx + 12} {by - 176} Q {cx + 34} {by - 160} '
             f'{cx + 34} {by - 130} L {cx + 34} {by} Z" fill="white" stroke="{c}" stroke-width="2.6"/>')
    for k in range(5):
        b.append(f'<circle cx="{cx - 14 + (k % 3) * 14}" cy="{by - 30 - k * 20}" r="4" fill="none" stroke="{c}" '
                 f'stroke-width="1.6"/>')
    if frio:
        for d in (-1, 1):
            sx = cx + d * 64
            for a in (90, 30, 150):
                ar = math.radians(a)
                b.append(line(sx - 18 * math.cos(ar), by - 90 - 18 * math.sin(ar), sx + 18 * math.cos(ar),
                              by - 90 + 18 * math.sin(ar), AZ, 2.2))
    else:
        for d in (-1, 1):
            sx = cx + d * 64
            b.append(f'<path d="M {sx} {by - 60} Q {sx - 10} {by - 80} {sx} {by - 100} Q {sx + 10} {by - 120} '
                     f'{sx} {by - 140}" fill="none" stroke="{RO}" stroke-width="2.2"/>')


def i9(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La gaseosa fría y la gaseosa caliente", c,
                      "Tú ya sabes algo de gases disueltos aunque no lo hayas estudiado: piensa en una gaseosa. Con "
                      "eso pon a prueba la explicación de la espuma. Después mira qué jala el vacío cuando ya no "
                      "queda líquido arriba.")
    x0, ww = x + 22, w - 44
    for k, (t, frio) in enumerate((("GASEOSA FRÍA", True), ("GASEOSA AL SOL", False))):
        cx = x0 + 110 + k * 230
        _botella(b, cx, yy + 236, c, frio)
        rot(b, cx, yy + 22, t, c, size=13, anchor="middle")
        b.append(checkbox(cx - 60, yy + 252, s=10, c=c))
        b.append(T(cx - 32, yy + 268, ["suelta más gas"], 15, GRAY))
    rx = x0 + 500
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 132, c, r=14)
    rot(b, rx + 18, yy + 28, "LA REGLA DE LA GASEOSA", c, size=14)
    b.append(T(rx + 18, yy + 66, ["Cuando un líquido se enfría, el gas disuelto en él…"], 16, INK))
    casillas(b, rx + 18, yy + 84, ("se escapa más", "se queda más disuelto"), c, paso=200)
    caja(b, rx, yy + 148, rw, 132, c, r=14)
    rot(b, rx + 18, yy + 176, "AL FINAL DE LA BAJADA", c, size=14)
    b.append(T(rx + 18, yy + 212, ["Cuando el líquido de arriba se acaba, el vacío de abajo jala…"], 16, INK))
    renglon(b, rx + 18, yy + 262, rx + rw - 18)
    yy += 300
    yy = trampa(b, x0, yy, ww, "Pon cada explicación al lado de tu regla de la gaseosa:",
                "si una opción dice que el aire «se libera» justo cuando el líquido se enfría, ¿cuadra con lo que pasa "
                "con una gaseosa fría? Y si otra habla del vacío, revisa por dónde dice que entra el aire.", c)
    return yy


# ───────── P10 · cafetera de sifón · la conclusión ─────────
PISTAS = ("aparece un gas que no estaba en los ingredientes", "un cambio de color que no se puede devolver",
          "se forma un sólido nuevo dentro del líquido", "sale o se absorbe calor sin que nadie caliente",
          "queda una sustancia que ningún método físico devuelve")


def i10(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Las pistas de un cambio químico, una por una", c,
                      "Un cambio químico deja pistas. Revisa cada pista contra lo que pasó en la cafetera y escribe "
                      "qué viste de verdad. Ojo: unas burbujas pueden ser un gas nuevo o aire que ya estaba; pregunta "
                      "de dónde vienen.")
    x0, ww = x + 22, w - 44
    cols = (("LA PISTA", 520), ("¿PASÓ EN LA CAFETERA?", 250), ("LO QUE DE VERDAD SE VIO", ww - 770))
    px = x0
    for t, cw in cols:
        caja(b, px, yy, cw, 46, c, r=0, fill=A["bg"])
        rot(b, px + 16, yy + 30, t, c, size=13)
        px += cw
    for k, p in enumerate(PISTAS):
        ry = yy + 46 + k * 58
        px = x0
        for j, (t, cw) in enumerate(cols):
            caja(b, px, ry, cw, 58, c, r=0)
            if j == 0:
                b.append(T(px + 16, ry + 36, [p], 16, INK))
            elif j == 1:
                casillas(b, px + 30, ry + 18, ("sí", "no"), c, paso=100)
            else:
                renglon(b, px + 16, ry + 44, px + cw - 16)
            px += cw
    yy += 46 + 5 * 58 + 20
    yy = frase_hueco(b, x0, yy, ww, "Al final, el café es ______________ sustancia; lo que hubo fue "
                                    "______________________ .", c)
    return ojo(b, x0, yy + 16, ww, "UNA REACCIÓN SE DEMUESTRA, NO SE SUPONE",
               "subir, bajar, filtrar y hacer espuma cambian dónde está la materia. ¿Cambian también qué es? Para "
               "afirmar una reacción o una descomposición, una opción necesita al menos una pista de la tabla con "
               "evidencia.")


Q = {1: dict(n=1, est=1, pag=160, ctx="Ácido cítrico en agua · el procedimiento más exitoso",
             comp="Indagación", inst=i1),
     2: dict(n=2, est=4, pag=160, ctx="Tableta efervescente · por qué en la bebida con gas",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=1, pag=161, ctx="Tableta efervescente · la evidencia del efecto del gas",
             comp="Indagación", inst=i3),
     4: dict(n=4, est=1, pag=161, ctx="Tableta efervescente · qué líquido elegir",
             comp="Indagación", inst=i4),
     5: dict(n=5, est=2, pag=161, ctx="Aceite de motor en el charco · por qué es heterogénea",
             comp="Uso comprensivo del conocimiento científico", inst=i5),
     6: dict(n=6, est=3, pag=161, ctx="La llanta de la bicicleta · el escape y el manómetro",
             comp="Explicación de fenómenos", inst=i6),
     7: dict(n=7, est=2, pag=161, ctx="Protector solar en spray · qué dice la inestabilidad",
             comp="Indagación", inst=i7),
     8: dict(n=8, est=3, pag=162, ctx="Cafetera de sifón · por qué el agua sube y baja",
             comp="Explicación de fenómenos", inst=i8),
     9: dict(n=9, est=3, pag=162, ctx="Cafetera de sifón · de dónde sale la espuma al bajar",
             comp="Explicación de fenómenos", inst=i9),
     10: dict(n=10, est=4, pag=162, ctx="Cafetera de sifón · la conclusión más precisa",
              comp="Uso comprensivo del conocimiento científico", inst=i10)}


def build(pages=(197, 198, 200, 201, 202)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"qui3_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
