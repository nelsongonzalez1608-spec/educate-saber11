#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 6 · entrenamiento ICFES · páginas 220 y 224.

Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · 2016-1, 2.ª ses. (ABD), CN, ítem 68 · B   (el ion Mg²⁺)                          estrategia 1
    QB · SIM. II 2023 química, N.º 274       · A   (entalpía de combustión de azúcares)   estrategia 2
    QC · SIM. II 2023 química, N.º 273       · D   (metal y ácido · temperatura y tamaño) estrategia 3
    QD · SIM. II 2023 química, N.º 335       · A   (plásticos desde grasas)               estrategia 4

  68 · B: el Mg tiene 12 protones; el ion Mg²⁺ perdió 2 electrones: 12 p⁺ y 10 electrones
       (2 + 8). Figuras: A = 14 p⁺, 12 e⁻; B = 12 p⁺, 10 e⁻; C = 12 p⁺, 12 e⁻ (átomo neutro);
       D = 14 p⁺, 10 e⁻. Verificada contra la página 22 del escaneo (Drive «1. CUADERNILLOS ICFES» /
       «2016-2 SEGUNDA SESION.pdf», cuya portada dice 2016-1 segunda sesión). Figuras redibujadas.
 274 · A: la sacarosa libera 5.648 kJ/mol, el doble que glucosa (2.816) y fructosa (2.827).
       Atención: D tiene la primera mitad cierta (la glucosa es la de menor contenido) y la razón
       ambigua según se lea el signo; A es la única enteramente correcta. Es una comparación POR
       MOL (por gramo los tres azúcares dan casi lo mismo, ≈ 16,5 kJ/g), igual que en el libro.
 273 · D: los dos cambios acortan el tiempo (temperatura: 115 → 75 → 40 s; tamaño: 115 → 90 →
       50 s). A («siempre… entre 40 y 75 s») extrapola; B es al revés (la temperatura ahorra 75 s,
       el tamaño 65 s); C («duración mínima de 50 s») no se sigue de tres tubos.
 335 · A: el texto dice que el petróleo no es renovable; las grasas se producen en cultivos y
       granjas. D es verdadera pero no es ventaja (el petróleo también lo originó la naturaleza);
       B no está en el texto; C es falsa.

Fuente de QB, QC y QD: «SIMULACRO II 2023-OFICIO-C.NATURALES - química.pdf» (Drive, id
1Y3haiTqbOoRuayZ3pDTD_CTWMGXwpntx), numeración continua del compilado, leídas en la versión de
texto del archivo (30 MB; el PDF no se puede descargar). Las tablas y opciones están completas en
el texto; la 274 se reconstruyó uniendo las dos columnas de la página (definición de ΔH y tabla de
azúcares); la 335 omite la tabla de polímeros comunes, que no hace falta para responder.
Reservadas en tablero/propuestas/qui_icfes_reservas.csv.
"""
from qui6 import *   # noqa: F401,F403  (configura la misión y EST)
from qui6 import rot, caja, pista, renglon, texto, tinte, tabla_vacia


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · ítem 68 · el ion Mg²⁺ ─────────
def atomo(b, cx, cy, protones, capas, r0=24, dr=26):
    """Modelo de capas: núcleo con «Np⁺» y electrones repartidos en cada capa."""
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r0}" fill="#EEF0F4" stroke="{INK}" stroke-width="1.8"/>')
    texto(b, cx, cy + 6, f"{protones}p⁺", size=15, anchor="middle", weight="700")
    for k in range(3):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r0 + dr * (k + 1)}" fill="none" stroke="{INK}" '
                 f'stroke-width="1.6"/>')
    for k, n in enumerate(capas):
        r = r0 + dr * (k + 1)
        for i in range(n):
            a = 2 * math.pi * i / n - math.pi / 2 + 0.35 * k
            ex, ey = cx + r * math.cos(a), cy + r * math.sin(a)
            b.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="6" fill="white" stroke="{INK}" stroke-width="1.6"/>')


def datos_68(b, x, y, w):
    caja(b, x, y + 4, 330, 40, GRAY, r=6)
    texto(b, x + 16, y + 30, "Convenciones:  ○ = electrones   p⁺ = protones", size=16)
    figs = (("A", 14, (2, 8, 2)), ("B", 12, (2, 8)), ("C", 12, (2, 8, 2)), ("D", 14, (2, 8)))
    fw = w / 4
    for k, (L, p, capas) in enumerate(figs):
        cx = x + fw * k + fw / 2
        texto(b, cx, y + 76, L + ".", size=19, weight="700", anchor="middle")
        atomo(b, cx, y + 196, p, capas)
    return y + 310


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Protones y electrones en cada dibujo", c,
                      "Como con las ecuaciones: aquí también se cuenta. Cuenta en cada modelo y calcula su carga. "
                      "Antes, escribe qué te dicen el «12» y el «2+» del enunciado.")
    x0, ww = x + 22, w - 44
    pista(b, x0, yy + 20, "número atómico 12 quiere decir…")
    renglon(b, x0 + 230, yy + 22, x0 + ww / 2 - 20)
    pista(b, x0 + ww / 2, yy + 20, "«2+» quiere decir que el átomo…")
    renglon(b, x0 + ww / 2 + 230, yy + 22, x0 + ww)
    yy += 38
    cols = (150, (ww - 150) / 4, (ww - 150) / 4, (ww - 150) / 4, (ww - 150) / 4)
    return tabla_vacia(b, x0, yy, cols, ("", "A", "B", "C", "D"),
                       ("protones", "electrones", "carga (p − e)"), c, rh=50, hh=40, size=16)


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="El magnesio metálico (Mg, número atómico = 12) forma iones Mg²⁺ y aumenta su número de oxidación. "
            "La figura que representa el ion Mg²⁺ es",
          o=["la figura A.", "la figura B.", "la figura C.", "la figura D."],
          datos=datos_68, inst=ii1)

# ───────── tabla de datos del cuadernillo ─────────
def tabla(b, x, y, cols, filas, c=GRAY, rh=34, head_h=38, size=16):
    W_ = sum(w for w, _ in cols)
    b.append(rect(x, y, W_, head_h, "#F1F3F6", r=0, stroke=c, sw=1.6))
    cx = x
    for w_, hd in cols:
        texto(b, cx + w_ / 2, y + head_h / 2 + 6, hd, size=size, weight="700", anchor="middle")
        cx += w_
    yy = y + head_h
    for f in filas:
        b.append(rect(x, yy, W_, rh, "white", r=0, stroke=c, sw=1.6))
        cx = x
        for (w_, _), v in zip(cols, f):
            texto(b, cx + w_ / 2, yy + rh / 2 + 6, v, size=size, anchor="middle")
            cx += w_
        yy += rh
    cx = x
    for w_, _ in cols[:-1]:
        cx += w_
        b.append(line(cx, y, cx, yy, c, 1.6))
    return yy


# ───────── QB · SIM. II N.º 274 · entalpía de combustión de azúcares ─────────
AZUCARES = ("La entalpía de una reacción (ΔH) mide el calor cedido o absorbido a presión constante, y se obtiene "
            "calculando la diferencia entre la energía de los productos y la energía de los reactivos: ΔH = H productos "
            "– H reactivos. La entalpía de combustión es un buen indicador del contenido energético de los azúcares; "
            "cuanto más calor se libere, mayor será su contenido energético. Las entalpías de combustión de algunos "
            "azúcares (azúcar + O₂ → CO₂ + H₂O) se presentan a continuación:")


def datos_274(b, x, y, w):
    yy = tabla(b, x, y + 4, ((260, "Azúcar"), (320, "Entalpía de combustión (kJ/mol)")),
               (("Glucosa", "–2.816"), ("Sacarosa", "–5.648"), ("Fructosa", "–2.827")))
    return pregunta(b, x, yy + 4, w, "Teniendo en cuenta la información anterior, puede afirmarse que de los tres "
                                     "azúcares")


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Ordena los azúcares por el calor que sueltan", c,
                      "Como con los tres combustibles del libro: primero lee el signo, después el tamaño. El signo dice "
                      "si el calor sale o entra; el número, cuánto.")
    x0, ww = x + 22, w - 44
    cols = (240, (ww - 240) / 3, (ww - 240) / 3, (ww - 240) / 3)
    return tabla_vacia(b, x0, yy, cols, ("", "GLUCOSA", "SACAROSA", "FRUCTOSA"),
                       ("¿el calor sale o entra?", "kJ que suelta por mol", "puesto (1.º = suelta más)"),
                       c, rh=40, hh=36, size=16)


# ───────── QC · SIM. II N.º 273 · velocidad de reacción ─────────
METAL = ("Un grupo de estudiantes quería conocer qué factores afectan la velocidad de reacción entre un ácido y un "
         "metal. Hicieron dos experimentos variando únicamente las condiciones especificadas en la tabla. En cada "
         "experimento tomaron 3 tubos de ensayo, a cada uno agregaron 1 mL de ácido y 1 g de metal, y registraron el "
         "tiempo de reacción.")


def datos_273(b, x, y, w):
    cols = ((300, ""), (210, "Tubo 1"), (210, "Tubo 2"), (210, "Tubo 3"))
    yy = tabla(b, x, y + 4, cols,
               (("Exp. 1 · condición", "18 °C", "45 °C", "70 °C"),
                ("Exp. 1 · reacción completa", "115 s", "75 s", "40 s"),
                ("Exp. 2 · condición", "metal completo", "partido a la mitad", "en trozos pequeños"),
                ("Exp. 2 · reacción completa", "115 s", "90 s", "50 s")))
    svg, yy = TJ(x, yy + 22, "Experimento 1: se modifica la temperatura, con el metal completo (sin partir). "
                             "Experimento 2: se modifica el tamaño del metal, a 18 °C.", w, 15, GRAY,
                 style="italic", lh=20)
    b.append(svg)
    return pregunta(b, x, yy, w, "De acuerdo con la información anterior, es posible concluir que")


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Lo que cambió el calor y lo que cambió el tamaño", c,
                      "Como con los quesos: calcula antes de opinar. Escribe cuántos segundos se ahorran en cada paso "
                      "y marca qué palabras de las opciones no se pueden comprobar con solo tres tubos.")
    x0, ww = x + 22, w - 44
    cols = (300, (ww - 300) / 3, (ww - 300) / 3, (ww - 300) / 3)
    return tabla_vacia(b, x0, yy, cols, ("", "DEL TUBO 1 AL 2", "DEL TUBO 2 AL 3", "DEL TUBO 1 AL 3"),
                       ("Exp. 1 (segundos menos)", "Exp. 2 (segundos menos)"), c, rh=42, hh=36, size=16)


# ───────── QD · SIM. II N.º 335 · plásticos desde grasas ─────────
PLASTICOS = ("Los plásticos son sustancias químicas sintéticas denominadas polímeros, cuya estructura es una cadena larga "
             "formada por unidades repetidas de moléculas más pequeñas que se conocen como monómeros. Actualmente, el "
             "99 % de los plásticos se sintetizan por polimerización de monómeros tipo alqueno (moléculas con dobles "
             "enlaces). Estos alquenos son obtenidos del petróleo, un recurso no renovable y en vías de agotarse. Para "
             "remplazar esta fuente de alquenos, algunos científicos proponen el uso de grasas animales y vegetales, "
             "que con luz ultravioleta se pueden transformar en alquenos.")


def datos_335(b, x, y, w):
    return pregunta(b, x, y, w, "Según el texto, el uso de materias primas como grasas animales y vegetales supone "
                                "una ventaja para la producción de plásticos, porque")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "De dónde salen las piezas del plástico", c,
                      "Como con el collar: las cuentas tienen que salir de alguna parte. Compara las dos fuentes de "
                      "monómeros y escribe qué pasa con cada una si la seguimos usando treinta años.")
    x0, ww = x + 22, w - 44
    cols = (300, (ww - 300) / 2, (ww - 300) / 2)
    return tabla_vacia(b, x0, yy, cols, ("", "PETRÓLEO", "GRASAS ANIMALES Y VEGETALES"),
                       ("¿se acaba?", "¿cómo se consigue más?", "en 30 años…"), c, rh=40, hh=36, size=16)


QB = dict(est=2, comp="Uso comprensivo del conocimiento científico", e=AZUCARES,
          o=["la sacarosa tiene mayor contenido energético, porque la reacción de combustión libera más energía.",
             "la glucosa tiene mayor contenido energético, porque la entalpía de combustión es mayor.",
             "la sacarosa tiene menor contenido energético, porque la reacción de combustión libera menos energía.",
             "la glucosa tiene menor contenido energético, porque la entalpía de combustión es menor."],
          datos=datos_274, inst=ii2)
QC = dict(est=3, comp="Indagación", e=METAL,
          o=["siempre que haya un incremento en la temperatura el tiempo de reacción se reducirá entre 40 y 75 "
             "segundos.",
             "la velocidad de reacción tiene una mayor variación cuando se modifica el tamaño del metal que cuando se "
             "modifica la temperatura.",
             "la reacción tiene una duración mínima de 50 segundos, si el metal se fracciona en trozos debido al "
             "aumento en la superficie de contacto.",
             "la velocidad de reacción se modifica al variar la temperatura y el tamaño del metal en el sistema."],
          datos=datos_273, inst=ii3)
QD = dict(est=4, comp="Uso comprensivo del conocimiento científico", e=PLASTICOS,
          o=["se puede lograr una producción renovable de estas materias primas mediante la implementación de "
             "cultivos y granjas.",
             "al usar grasas animales y vegetales se podría obtener un nuevo polímero que incorpore monómeros de "
             "distinta estructura en su cadena.",
             "al usar grasas animales y vegetales, se incrementaría la cantidad de petróleo en las reservas.",
             "las grasas animales y vegetales constituyen recursos que son originados por la naturaleza."],
          datos=datos_335, inst=ii4)


def build(pages=(220, 224)):
    return [hoja_icfes("qui6_i1", pages[0], QA, QB),
            hoja_icfes("qui6_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
