#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sociales y Ciudadanas · Misión 3 · taller (páginas 111, 112, 114, 115, 116 del cuaderno).

Libro fuente: Prueba de Campo Misión 3, páginas 358 a 361 (componente competencias ciudadanas).
Textos: el homenaje en la Plaza de Bolívar (preguntas 1 a 3), la cafetería del colegio (4), el
teletrabajo (5), el centro de salud de la vereda (6), la hidroeléctrica (7) y los aranceles de
Estados Unidos (8 a 10).

Claves verificadas resolviendo cada pregunta contra el texto (6 nov 2026):

    1·A  2·C  3·D  4·A  5·A  6·A  7·C  8·D  9·A  10·C

Reparto: A cinco veces, C tres, D dos, B ninguna (registrado en soc3_hallazgos.csv).

Estrategias:
    1 · Cada voz, su preocupación         (2, 4, 8)   · azul
    2 · Quién gana y quién paga            (1, 7)      · verde
    3 · El derecho que se pone en tensión  (3, 6, 9)   · rojo
    4 · El efecto que llega a otra parte   (5, 10)     · morado
"""
from taller_base import *
from taller_base import _mezcla

configurar("Sociales y Ciudadanas", 3, "competencias ciudadanas",
           tema="Lo que mueve una decisión: voces, derechos y efectos",
           color=EDU_ORO, nota="LO QUE ANOTÉ DEL CASO")
EST = {1: ("Cada voz, su preocupación", EDU_AZUL),
       2: ("Quién gana y quién paga", EDU_VERDE),
       3: ("El derecho que se pone en tensión", EDU_ROJO),
       4: ("El efecto que llega a otra parte", "#5B3E96")}
usar_estrategias(EST)
AZ, VE, RO, MO = (EST[k][1] for k in (1, 2, 3, 4))


# ───────── piezas pequeñas ─────────
def rot(b, x, y, t, c, size=14):
    b.append(T(x, y, [t], size, c, weight="700", ls=1.5))


def pista(b, x, y, t, size=15, anchor="start"):
    b.append(T(x, y, [t], size, GRAY, style="italic", anchor=anchor))


def casilla(b, x, y, w, h, c, sw=2):
    b.append(rect(x, y, w, h, "white", r=10, stroke=c, sw=sw))


def frase(b, x, y, w, texto, c, h=48, size=18):
    """Frase para completar dentro de un recuadro."""
    casilla(b, x, y, w, h, c)
    b.append(T(x + 22, y + h / 2 + 6, [texto], size, INK))
    return y + h


def si_no(b, x, y, c, labs=("sí", "no")):
    for j, lab in enumerate(labs):
        b.append(checkbox(x + j * 96, y, s=10, c=c))
        b.append(T(x + 28 + j * 96, y + 17, [lab], 15, GRAY))


# ───────── 1 · el homenaje · lo político, lo social y lo económico ─────────
def i1(b, x, y, w, h):
    c = VE
    yy = titulo_instr(b, x, y, "El libro de cuentas del homenaje", c,
                      "Un hecho público mueve tres cosas a la vez. En cada dimensión anota lo que el "
                      "homenaje dio y lo que costó, según el texto. Si una casilla te queda vacía, vuelve "
                      "a leer antes de dejarla así.")
    x0 = x + 22
    c1, c2, c3 = x0, x0 + 250, x0 + 740
    wc = 470
    rot(b, c2 + 8, yy + 18, "LO QUE DIO", c)
    rot(b, c3 + 8, yy + 18, "LO QUE COSTÓ", c)
    yy += 30
    for dim, p1, p2 in (("lo político", "¿qué resaltaron y exigieron los líderes?", "¿hubo algo en contra?"),
                        ("lo social", "¿qué se honró en la plaza?", "¿qué voces no se oyeron?"),
                        ("lo económico", "¿alguien ganó algo?", "¿qué perdió quien vive del día?")):
        casilla(b, c1, yy, 230, 58, c)
        b.append(T(c1 + 20, yy + 36, [dim], 17, c, weight="700"))
        for cx, p in ((c2, p1), (c3, p2)):
            casilla(b, cx, yy, wc, 58, c)
            pista(b, cx + 16, yy + 22, p, size=14)
        yy += 70
    yy += 6
    yy = frase(b, x0, yy, w - 44, "Una buena interpretación sistémica deja algo en las dos columnas de "
                                   "____________ dimensión.", c)
    yy += 16
    return trampa(b, x0, yy, w - 44, "Hay opciones que cierran la cuenta antes de tiempo:",
                  "una dice que los cierres «únicamente» trajeron pérdidas; otra, que lo político y lo "
                  "social «nunca» pueden armonizarse. Revisa también si alguna da por resuelto lo que el "
                  "texto cuenta como una tensión. Una cuenta honesta no se cierra con una sola palabra.", c)


# ───────── 2 · el homenaje · las dos perspectivas ─────────
def globo(b, x, y, w, h, c, quien, pregunta):
    casilla(b, x, y, w, h, c, sw=2.2)
    b.append(f'<polygon points="{x + 40},{y + h - 1} {x + 70},{y + h - 1} {x + 44},{y + h + 26}" '
             f'fill="white" stroke="{c}" stroke-width="2.2"/>')
    b.append(rect(x + 38, y + h - 4, 34, 6, "white", r=0))
    rot(b, x + 20, y + 30, quien, c)
    pista(b, x + 20, y + 56, pregunta, size=14)


def i2(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Parte cada opción en dos y mira de quién es cada mitad", c,
                      "Cada opción tiene una mitad para los líderes políticos y otra para la vendedora. "
                      "Primero escribe lo que el texto le atribuye a cada uno. Después revisa las mitades: "
                      "una opción sirve solo si las dos dicen lo que el texto cuenta.")
    x0 = x + 22
    gw = (w - 44 - 30) // 2
    globo(b, x0, yy, gw, 130, c, "LOS LÍDERES POLÍTICOS…", "resaltaron ________ y exigieron ________")
    globo(b, x0 + gw + 30, yy, gw, 130, c, "LA VENDEDORA…", "cuestionó ________ porque ________")
    yy += 172
    rot(b, x0 + 120, yy, "MITAD DE LOS LÍDERES: ¿LA DICE EL TEXTO?", c, size=13)
    rot(b, x0 + 660, yy, "MITAD DE LA VENDEDORA: ¿LA DICE EL TEXTO?", c, size=13)
    yy += 16
    for k, L in enumerate("ABCD"):
        ry = yy + k * 46
        b.append(f'<circle cx="{x0 + 40}" cy="{ry + 18}" r="16" fill="white" stroke="{c}" stroke-width="2"/>')
        b.append(T(x0 + 40, ry + 24, [L], 16, c, weight="700", anchor="middle"))
        si_no(b, x0 + 120, ry + 6, c)
        si_no(b, x0 + 660, ry + 6, c)
    yy += 4 * 46 + 10
    return ojo(b, x0, yy, w - 44, "OJO CON LAS MITADES QUE SUENAN BIEN",
               "«La no repetición de hechos atroces» o «se muestran sorprendidos» suenan a texto de "
               "Sociales, pero antes de aceptar cualquier mitad, búscala en el texto con el dedo.",
               fuerte="Si no la encuentras, esa mitad no es del texto: es de quien escribió la opción.")


# ───────── 3 · el homenaje · qué derecho se pone en tensión ─────────
def i3(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "¿A quién se le tocó este derecho en la historia?", c,
                      "Un derecho está «en tensión» cuando a alguien de la historia le pasa algo con él. "
                      "Para cada derecho que nombran las opciones escribe a quién se le afectó y cómo. "
                      "Si a nadie, escribe «a nadie».")
    x0 = x + 22
    rot(b, x0 + 400, yy + 16, "¿A QUIÉN SE LE AFECTÓ, Y CÓMO?", c)
    yy += 28
    for d in ("la libre expresión política", "la diversidad cultural",
              "la participación democrática", "la dignidad y el mínimo vital"):
        casilla(b, x0, yy, 370, 50, c)
        b.append(T(x0 + 20, yy + 32, [d], 17, INK))
        casilla(b, x0 + 400, yy, w - 44 - 400, 50, c)
        yy += 62
    yy += 8
    return alto_profe(b, x, yy, w - 4,
                      "El MÍNIMO VITAL: la Corte Constitucional llama así a lo que una persona necesita "
                      "para vivir con dignidad hoy, como comer y pagar dónde dormir. No está escrito con "
                      "ese nombre en la Constitución: lo construyó la Corte a partir de la dignidad humana.")


# ───────── 4 · la cafetería · qué diferencia de perspectivas ─────────
def i4(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "No es lo mismo «no quiere» que «no puede»", c,
                      "Una diferencia de perspectivas está en las razones y también en los verbos. Copia lo "
                      "que dice cada lado con sus propias palabras y después compáralo con lo que cada "
                      "opción le atribuye.")
    x0 = x + 22
    cw_ = (w - 44 - 30) // 2
    for k, (quien, a, bb) in enumerate((("LOS ESTUDIANTES", "piden:", "porque:"),
                                        ("EL RECTOR", "responde:", "porque:"))):
        cx = x0 + k * (cw_ + 30)
        b.append(rect(cx, yy, cw_, 190, "white", r=14, stroke=c, sw=2))
        b.append(rect(cx, yy, 8, 190, c, r=4))
        rot(b, cx + 28, yy + 32, quien, c)
        for j, lab in enumerate((a, bb)):
            ly = yy + 80 + j * 62
            b.append(T(cx + 28, ly, [lab], 17, GRAY))
            b.append(line(cx + 130, ly + 4, cx + cw_ - 24, ly + 4, LGRAY, 2))
    yy += 210
    yy = frase(b, x0, yy, w - 44, "El rector no dijo que no quisiera: dijo que no ______________ "
                                   "modificar el menú de inmediato.", c)
    yy += 16
    return trampa(b, x0, yy, w - 44, "Dos opciones le cambian las palabras a alguien:",
                  "una dice que los estudiantes propusieron modificar el contrato con la cafetería, y otra "
                  "que el rector «no desea» que el menú cambie. Busca en el caso si eso se dijo. Lo que "
                  "nadie dijo no puede ser su perspectiva.", c)


# ───────── 5 · el teletrabajo · social, ambiental y tecnológico ─────────
def i5(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Sigue la política hasta el municipio sin señal", c,
                      "Una política nacional no cae igual en todas partes. Escribe qué le pasa en la ciudad "
                      "y qué le pasa en un municipio apartado, en cada una de las tres dimensiones que "
                      "pide la pregunta.")
    x0 = x + 22
    cA, cB = x0 + 250, x0 + 740
    wc = 470
    for cx, lugar in ((cA, "EN LA CIUDAD"), (cB, "EN EL MUNICIPIO APARTADO")):
        rot(b, cx + 8, yy + 18, lugar, c)
    yy += 30
    for dim, p1, p2 in (("lo social", "¿quién gana tiempo?", "¿quién se queda por fuera?"),
                        ("lo ambiental", "¿qué pasa con el tráfico y el aire?", "¿cambia algo allá?"),
                        ("lo tecnológico", "¿hay con qué conectarse?", "¿hay Internet suficiente?")):
        casilla(b, x0, yy, 230, 58, c)
        b.append(T(x0 + 20, yy + 36, [dim], 17, c, weight="700"))
        for cx, p in ((cA, p1), (cB, p2)):
            casilla(b, cx, yy, wc, 58, c)
            pista(b, cx + 16, yy + 22, p, size=14)
        yy += 70
    yy += 10
    return trampa(b, x0, yy, w - 44, "Hay opciones que hablan como si el país fuera una sola ciudad:",
                  "«asegura igualdad de oportunidades en todo el país», «garantiza de manera automática… en "
                  "todas las regiones». Pasa las cuatro opciones por tu columna de la derecha y mira cuáles "
                  "aguantan lo que escribiste ahí.", c)


# ───────── 6 · el centro de salud de la vereda · el argumento constitucional ─────────
def i6(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Si se cumpliera ese derecho, ¿volvería el médico?", c,
                      "Un argumento constitucional sirve si, cumpliéndolo, se resuelve el reclamo. Escribe "
                      "primero qué reclaman los habitantes. Después prueba cada idea de las opciones: "
                      "imagina que se cumple y mira qué pasa en la vereda.")
    x0 = x + 22
    rot(b, x0, yy + 18, "LO QUE RECLAMAN LOS HABITANTES, EN UNA FRASE", c)
    casilla(b, x0 + 520, yy, w - 44 - 520, 40, c)
    yy += 60
    rot(b, x0 + 900, yy + 4, "SI SE CUMPLE, ¿SE RESUELVE?", c, size=13)
    yy += 18
    for k, (L, idea) in enumerate((("A", "servicios de salud continuos y oportunos"),
                                   ("B", "libertad para viajar hasta un hospital"),
                                   ("C", "elegir al personal médico de la vereda"),
                                   ("D", "que el municipio decida si abre o cierra"))):
        ry = yy + k * 52
        b.append(f'<circle cx="{x0 + 18}" cy="{ry + 21}" r="16" fill="white" stroke="{c}" stroke-width="2"/>')
        b.append(T(x0 + 18, ry + 27, [L], 16, c, weight="700", anchor="middle"))
        casilla(b, x0 + 50, ry, 820, 42, c, sw=1.8)
        b.append(T(x0 + 70, ry + 28, [idea], 17, INK))
        si_no(b, x0 + 900, ry + 10, c, labs=("sí", "no", "a medias"))
    yy += 4 * 52 + 12
    return ojo(b, x0, yy, w - 44, "Que un derecho exista no basta:",
               "tiene que ser el que responde al reclamo. Si con él cumplido los niños y los adultos "
               "mayores siguen viajando horas para una urgencia, no es el argumento que sostiene lo que "
               "piden los habitantes.")


# ───────── 7 · la hidroeléctrica · la conclusión que integra ─────────
def i7(b, x, y, w, h):
    c = VE
    yy = titulo_instr(b, x, y, "Pon cada efecto en su platillo de la balanza", c,
                      "El texto trae efectos buenos y malos. Ponlos en su platillo y escribe al lado a quién "
                      "le toca cada uno: al millón de usuarios, a los campesinos, a la biodiversidad o a los "
                      "inversionistas.")
    x0 = x + 22
    cx = x + w / 2
    top = yy + 6
    # la balanza
    b.append(f'<polygon points="{cx - 60:.0f},{top + 150} {cx + 60:.0f},{top + 150} {cx:.0f},{top + 36}" '
             f'fill="white" stroke="{c}" stroke-width="2.4"/>')
    b.append(f'<circle cx="{cx:.0f}" cy="{top + 30}" r="10" fill="{c}"/>')
    b.append(line(cx - 420, top + 30, cx + 420, top + 30, c, 4))
    for s in (-1, 1):
        px = cx + s * 420
        b.append(line(px, top + 30, px - 118, top + 96, c, 2))
        b.append(line(px, top + 30, px + 118, top + 96, c, 2))
        b.append(f'<polygon points="{px - 120:.0f},{top + 96} {px + 120:.0f},{top + 96} '
                 f'{px + 92:.0f},{top + 120} {px - 92:.0f},{top + 120}" fill="white" stroke="{c}" '
                 f'stroke-width="2.4"/>')
    rot(b, cx - 420 - 60, top + 152, "LO QUE GANA", c)
    rot(b, cx + 420 - 70, top + 152, "LO QUE CUESTA", c)
    yy = top + 172
    colw = (w - 44 - 40) // 2
    for k in range(3):
        for s in (0, 1):
            bx = x0 + s * (colw + 40)
            casilla(b, bx, yy, colw - 220, 46, c)
            casilla(b, bx + colw - 206, yy, 206, 46, c)
            pista(b, bx + colw - 194, yy + 18, "¿a quién?", size=13)
        yy += 56
    yy += 10
    return trampa(b, x0, yy, w - 44, "Antes de elegir, revisa a quién le pone cada opción la ganancia:",
                  "¿el texto dice que los campesinos salen ganando? Compara con lo que escribiste en tus "
                  "casillas de «¿a quién?». La conclusión más completa deja peso en los dos platillos y no "
                  "le cambia el dueño a ningún efecto.", c)


# ───────── 8 · los aranceles · Trump y sus críticos ─────────
def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "¿Quién dijo cada frase? Únela con su dueño", c,
                      "Para comparar dos perspectivas hay que saber de quién es cada idea. Une con una línea "
                      "cada frase del texto con la persona que la dice. Después revisa si alguna opción le "
                      "presta a Trump palabras de otro.")
    x0 = x + 22
    frases = ("Estados Unidos es «la tienda más grande de la historia»",
              "los aranceles han encarecido los productos a los consumidores",
              "«se parecen más a sanciones: buscan castigar para forzar cambios políticos»",
              "seguirán comprando petróleo ruso pese a la presión")
    duenos = ("una investigadora del Centro Stimson", "Donald Trump",
              "funcionarios de la India", "los críticos")
    for k in range(4):
        ry = yy + k * 58
        casilla(b, x0, ry, 760, 46, c, sw=1.8)
        b.append(T(x0 + 18, ry + 30, [frases[k]], 16, INK, style="italic"))
        b.append(f'<circle cx="{x0 + 790}" cy="{ry + 23}" r="7" fill="{c}"/>')
        b.append(f'<circle cx="{x0 + 900}" cy="{ry + 23}" r="7" fill="{c}"/>')
        casilla(b, x0 + 924, ry, w - 44 - 924, 46, c, sw=1.8)
        b.append(T(x0 + 942, ry + 30, [duenos[k]], 16, INK))
    yy += 4 * 58 + 12
    return ojo(b, x0, yy, w - 44, "OJO CON LAS FRASES PRESTADAS",
               "Si una opción le atribuye a Trump una idea que en el texto dijo otra persona, esa mitad "
               "ya falla, aunque la idea sí aparezca en el artículo.",
               fuerte="La diferencia tiene que ser entre lo que Trump presenta y lo que le responden.")


# ───────── 9 · los aranceles · el principio del derecho internacional ─────────
def i9(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Define tú la palabra difícil antes de leer las opciones", c,
                      "El enunciado dice qué busca: el principio que «protege la autodeterminación». Si no "
                      "sabes qué es eso, ninguna opción te va a ayudar. Defínela primero y después compara "
                      "cada principio con tu definición.")
    x0 = x + 22
    yy = frase(b, x0, yy, w - 44, "auto = ____________   ·   determinación = ____________   ·   "
                                   "entonces autodeterminación es ____________________", c)
    yy += 16
    rot(b, x0 + 860, yy + 4, "¿PROTEGE LO MISMO QUE MI DEFINICIÓN?", c, size=13)
    yy += 16
    for k, (L, p) in enumerate((("A", "la soberanía de los Estados"), ("B", "la legalidad"),
                                ("C", "la igualdad"), ("D", "la solución pacífica de controversias"))):
        ry = yy + k * 50
        b.append(f'<circle cx="{x0 + 18}" cy="{ry + 20}" r="16" fill="white" stroke="{c}" stroke-width="2"/>')
        b.append(T(x0 + 18, ry + 26, [L], 16, c, weight="700", anchor="middle"))
        casilla(b, x0 + 50, ry, 780, 40, c, sw=1.8)
        b.append(T(x0 + 70, ry + 27, [p], 17, INK))
        si_no(b, x0 + 880, ry + 9, c)
    yy += 4 * 50 + 10
    yy = ojo(b, x0, yy, w - 44, "OJO CON LA OPCIÓN B",
             "El principio de legalidad existe, pero no es el derecho de un país a difundir sus opiniones: "
             "significa que las autoridades solo pueden hacer lo que la ley les permite. La opción usa un "
             "nombre real con una definición equivocada.")
    yy += 12
    return alto_profe(b, x, yy, w - 4,
                      "Dos principios de la Carta de la ONU que se parecen: la SOBERANÍA y no intervención "
                      "(cada Estado decide sus asuntos sin que otro lo obligue) y la SOLUCIÓN PACÍFICA de "
                      "controversias (los conflictos se arreglan negociando). El profe muestra en qué se "
                      "diferencian.")


# ───────── 10 · los aranceles · la conclusión que integra ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Tres anillos: dentro de casa, en el rival y en el aliado", c,
                      "Un arancel que dura mucho no se queda en la frontera: se riega. Escribe lo que el texto "
                      "dice que pasa en cada anillo. Después pasa cada opción por los tres.")
    x0 = x + 22
    cx, cy = x0 + 215, yy + 215
    for r_, fill in ((210, _mezcla(c, 0.90)), (140, _mezcla(c, 0.80)), (72, _mezcla(c, 0.66))):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r_}" fill="{fill}" stroke="{c}" stroke-width="2"/>')
    b.append(T(cx, cy + 6, ["EE. UU."], 16, c, weight="700", anchor="middle"))
    b.append(T(cx, cy - 98, ["países presionados"], 15, c, weight="700", anchor="middle"))
    b.append(T(cx, cy - 170, ["aliados"], 15, c, weight="700", anchor="middle"))
    bx = x0 + 470
    bw = w - 44 - 470
    for k, (lab, p) in enumerate((("Dentro de EE. UU. pasa…", "¿qué les pasa a los precios?"),
                                  ("En los países presionados pasa…", "¿cedieron? ¿qué dijeron?"),
                                  ("Con los aliados pasa…", "¿confían más o menos?"))):
        ry = yy + 10 + k * 140
        b.append(T(bx, ry + 22, [lab], 18, c, weight="700"))
        casilla(b, bx, ry + 36, bw, 80, c)
        pista(b, bx + 16, ry + 60, p, size=14)
    yy += 440
    return trampa(b, x0, yy, w - 44, "La conclusión más completa no deja un anillo vacío:",
                  "si una opción dice que en uno de ellos no pasa nada, o los llena todos solo de buenas "
                  "noticias, no integra lo que el texto cuenta. Compárala con lo que escribiste en cada "
                  "anillo antes de decidir.", c)


Q = {1: dict(n=1, est=2, pag=359, ctx="Homenaje en la Plaza de Bolívar · interacción sistémica",
             comp="Pensamiento reflexivo y sistémico", inst=i1),
     2: dict(n=2, est=1, pag=359, ctx="Homenaje en la Plaza de Bolívar · dos perspectivas",
             comp="Interpretación de perspectivas", inst=i2),
     3: dict(n=3, est=3, pag=359, ctx="Cierres en el centro · qué derecho entra en tensión",
             comp="Pensamiento social", inst=i3),
     4: dict(n=4, est=1, pag=359, ctx="Cafetería del colegio · estudiantes y rector",
             comp="Interpretación de perspectivas", inst=i4),
     5: dict(n=5, est=4, pag=359, ctx="Teletrabajo en entidades públicas · tres dimensiones",
             comp="Pensamiento reflexivo y sistémico", inst=i5),
     6: dict(n=6, est=3, pag=360, ctx="Centro de salud cerrado en el Cauca · el argumento",
             comp="Pensamiento social", inst=i6),
     7: dict(n=7, est=2, pag=360, ctx="Hidroeléctrica en el sur · la conclusión más completa",
             comp="Pensamiento reflexivo y sistémico", inst=i7),
     8: dict(n=8, est=1, pag=361, ctx="Aranceles de EE. UU. · Trump y sus críticos",
             comp="Interpretación de perspectivas", inst=i8),
     9: dict(n=9, est=3, pag=361, ctx="Aranceles de EE. UU. · qué principio se cuestiona",
             comp="Pensamiento social", inst=i9),
     10: dict(n=10, est=4, pag=361, ctx="Aranceles prolongados · efectos en varias dimensiones",
              comp="Pensamiento reflexivo y sistémico", inst=i10)}


def build(pages=(111, 112, 114, 115, 116)):
    out = []
    for hoja, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10)), start=1):
        out.append(hoja_taller(f"soc3_t{hoja}", pages[hoja - 1], hoja, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
