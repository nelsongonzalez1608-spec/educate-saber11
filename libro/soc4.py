#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sociales y Ciudadanas · Misión 4 · componente historia y cultura · páginas 118–124.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 4» de Ciencias Sociales, páginas 370–374.

Claves verificadas (resueltas a mano contra el texto del libro, no copiadas):

    1·B  2·A  3·B  4·B  5·D  6·A  7·B  8·B  9·A  10·A

Reparto: A 4 · B 5 · C 0 · D 1. La B concentra la mitad y la C no sale nunca: registrado
en tablero/propuestas/soc4_hallazgos.csv.

Estrategias:
    1 · Un hecho, varias dimensiones           (3, 6, 9  · ICFES 89)
    2 · Quién lo mira y desde dónde            (2, 5, 8  · ICFES 83)
    3 · Lo que el hecho le hizo a la gente     (1, 4     · ICFES 87)
    4 · De dónde viene y hasta dónde llega     (7, 10    · ICFES 81)

Hojas: 118 soc4_t1 (1-2) · 119 soc4_t2 (3-4) · 120 soc4_i1 · 121 soc4_t3 (5-6) ·
       122 soc4_t4 (7-8) · 123 soc4_t5 (9-10) · 124 soc4_i2.
"""
from taller_base import *

configurar("Sociales y Ciudadanas", 4, "historia y cultura",
           tema="Un hecho, muchas miradas: lo que el pasado le hizo a la gente",
           color=EDU_ORO, nota="LO QUE ANOTÉ DEL CASO")
MORADO = "#5B3E96"
EST = {1: ("Un hecho, varias dimensiones", EDU_AZUL),
       2: ("Quién lo mira y desde dónde", EDU_VERDE),
       3: ("Lo que el hecho le hizo a la gente", EDU_ROJO),
       4: ("De dónde viene y hasta dónde llega", MORADO)}
usar_estrategias(EST)


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw))


def pista(b, x, y, txt, size=15):
    b.append(T(x, y, [txt], size, GRAY, style="italic"))


def evidencia(b, x, y, w, rotulo, texto, c):
    """Cita del libro en fondo suave con acento vertical. Devuelve dónde termina."""
    svg, y2 = TJ(x + 34, y + 36, texto, w - 60, 17, INK, style="italic", lh=25)
    hh = y2 - y + 12
    b.append(rect(x, y, w, hh, SOFT, r=10))
    b.append(rect(x, y, 8, hh, c, r=4))
    rot(b, x + 34, y + 24, rotulo, c, size=13)
    b.append(svg)
    return y + hh


def frase_hueco(b, x, y, w, texto, c, bold=True):
    caja(b, x, y, w, 48, c)
    b.append(T(x + 24, y + 31, [texto], 18, INK, weight="700" if bold else "400"))
    return y + 48


# ───────── P1 · arte en La Violencia ─────────
def i1(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Del lienzo a la herida: qué denuncia cada obra", c,
                      "Un cuadro no es solo un estilo: es una forma de contar lo que le pasó a la gente. "
                      "Escribe, para cada artista, qué muestra y qué consecuencia del conflicto deja ver.")
    x0, ww = x + 22, w - 44
    c1, c2, c3 = x0, x0 + 330, x0 + 790
    rot(b, c1, yy + 18, "ARTISTA Y OBRA", c)
    rot(b, c2, yy + 18, "QUÉ MUESTRA", c)
    rot(b, c3, yy + 18, "QUÉ DENUNCIA DE LA SOCIEDAD", c)
    yy += 30
    for nom, sub in (("Débora Arango", "sus cuadros de las décadas de 1940 y 1950"),
                     ("Alejandro Obregón", "Violencia, 1962")):
        caja(b, c1, yy, 310, 64, c)
        b.append(T(c1 + 18, yy + 28, [nom], 17, c, weight="700"))
        b.append(T(c1 + 18, yy + 52, [sub], 14, GRAY, style="italic"))
        caja(b, c2, yy, 440, 64, c)
        caja(b, c3, yy, ww - 790, 64, c)
        yy += 78
    yy += 6
    yy = frase_hueco(b, x0, yy, ww, "Según la última frase del texto, el arte no era un ámbito ______________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una opción dice que la pintura «se limitó a reproducir estilos internacionales»:",
                  "antes de aceptarla, vuelve a tu tabla. Si pudiste escribir algo en la última columna, esa "
                  "opción ya no se sostiene. Haz lo mismo con las otras tres: ¿cuál deja la tabla en blanco?", c)


# ───────── P2 · Revolución Cultural ─────────
def i2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Dos lentes sobre la misma década", c,
                      "El hecho es uno solo: China, 1966 a 1976. Lo que cambia es quién lo mira. Escribe con las "
                      "palabras del texto qué vio cada lado, y después pregúntate si las opciones los ponen de "
                      "acuerdo o los separan.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (quien, pista_) in enumerate((("EL GOBIERNO Y EL PARTIDO", "el texto dice que estas medidas defendían…"),
                                         ("LOS CRÍTICOS, DE ADENTRO Y DE AFUERA", "el texto dice que se trataba de…"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 128, c)
        rot(b, bx + 20, yy + 30, quien, c)
        pista(b, bx + 20, yy + 56, pista_)
        b.append(line(bx + 20, yy + 102, bx + half - 20, yy + 102, LGRAY, 2))
    yy += 150
    b.append(T(x0, yy + 20, ["¿Cada opción los pone de acuerdo o los separa?"], 18, INK, weight="700"))
    yy += 40
    for k, L in enumerate("ABCD"):
        bx = x0 + k * (ww / 4)
        b.append(f'<circle cx="{bx + 22}" cy="{yy + 20}" r="18" fill="white" stroke="{c}" stroke-width="2"/>')
        b.append(T(bx + 22, yy + 27, [L], 17, c, weight="700", anchor="middle"))
        for j, lab in enumerate(("de acuerdo", "separados")):
            b.append(checkbox(bx + 56, yy + 2 + j * 32, s=10, c=c))
            b.append(T(bx + 84, yy + 18 + j * 32, [lab], 15, GRAY))
    yy += 82
    return ojo(b, x0, yy, ww, "¿De qué lado estaban los Guardias Rojos?",
               "Búscalos en el texto: qué hacían y para quién. Una opción los junta con los opositores; con lo "
               "que escribiste arriba puedes decidir si eso tiene sentido.")


# ───────── P3 · Nacional 1989 ─────────
def i3(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Las capas del mismo título", c,
                      "Un solo partido de fútbol trae varias capas encima. Escribe una frase por capa con lo que dice "
                      "el texto. Después tacha la opción que borra alguna capa: integrar es no dejar ninguna afuera.")
    x0, ww = x + 22, w - 44
    capas = (("LO DEPORTIVO", "qué ganó y por qué fue la primera vez"),
             ("LO QUE SINTIÓ EL PAÍS", "qué símbolo fue en medio de la crisis"),
             ("LO QUE HABÍA DETRÁS", "qué dinero y qué presiones menciona el texto"))
    for k, (rt, ps) in enumerate(capas):
        dx = k * 34
        caja(b, x0 + dx, yy, ww - dx, 70, c, sw=2)
        rot(b, x0 + dx + 20, yy + 28, rt, c)
        pista(b, x0 + dx + 20, yy + 54, ps)
        b.append(line(x0 + dx + 460, yy + 52, x0 + ww - 24, yy + 52, LGRAY, 2))
        yy += 82
    yy += 6
    b.append(T(x0, yy + 22, ["Capas que nombra cada opción (escribe cuántas, de 0 a 3):"], 18, INK, weight="700"))
    yy += 38
    for k, L in enumerate("ABCD"):
        bx = x0 + k * 160
        b.append(T(bx, yy + 30, [L], 20, c, weight="700"))
        caja(b, bx + 28, yy, 70, 44, c)
    yy += 64
    return trampa(b, x0, yy, ww, "Una opción usa el verbo «distraer»:",
                  "¿el texto dice que el fútbol tapó la crisis, o que la crisis se coló en el fútbol? No es lo mismo, "
                  "y la diferencia decide si esa opción borra una capa.", c)


# ───────── P4 · Turbo, dimensión social ─────────
def i4(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Más que un trasteo: lo que se rompió al irse", c,
                      "El texto insiste en que irse no fue solo «un cambio de residencia». Escribe en la maleta lo "
                      "que sí se pudieron llevar y en la vereda lo que se quedó roto.")
    x0, ww = x + 22, w - 44
    half = (ww - 110) / 2
    caja(b, x0, yy, half, 190, c)
    rot(b, x0 + 20, yy + 30, "LO QUE CABE EN LA MALETA", c)
    pista(b, x0 + 20, yy + 56, "lo que se movió de un lugar a otro")
    for i in range(2):
        b.append(line(x0 + 20, yy + 104 + i * 50, x0 + half - 20, yy + 104 + i * 50, LGRAY, 2))
    rx = x0 + half + 110
    caja(b, rx, yy, half, 190, c)
    rot(b, rx + 20, yy + 30, "LO QUE SE QUEDÓ ROTO EN LA VEREDA", c)
    pista(b, rx + 20, yy + 56, "el texto nombra al menos tres cosas")
    for i in range(3):
        b.append(line(rx + 20, yy + 92 + i * 40, rx + half - 20, yy + 92 + i * 40, LGRAY, 2))
    hand = hand_arrow(x0 + half + 18, yy + 95, rx - 18, yy + 95, c, sw=3.4, bend=0.25, head=18)
    b.append(hand)
    yy += 210
    yy = ojo(b, x0, yy, ww, "MIRA LA FUENTE ANTES DE CREERLE A UNA OPCIÓN",
             "El tablero del mapa no es un adorno: cuenta 802 registros asociados y pone el desplazamiento "
             "forzado como el hecho victimizante más frecuente. Léelo antes de decidir qué tan grande y qué tan "
             "conectado fue lo que pasó en Turbo, y después pon cada opción al lado de tu columna derecha.")
    return yy


# ───────── P5 · testimonios distintos ─────────
def i5(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Lo que cada familia pudo ver desde su vereda", c,
                      "Tres familias, tres respuestas distintas a la misma pregunta: ¿quién nos hizo esto? Imagina "
                      "desde dónde habla cada una y por qué podría responder así.")
    x0, ww = x + 22, w - 44
    cw = (ww - 40) / 3
    for k, (quien, ps) in enumerate((("NOMBRA A LA GUERRILLA", "¿qué pudo haber vivido?"),
                                     ("NOMBRA A LOS PARAMILITARES", "¿qué pudo haber vivido?"),
                                     ("NO NOMBRA A NADIE", "¿por qué callaría?"))):
        bx = x0 + k * (cw + 20)
        caja(b, bx, yy, cw, 170, c)
        b.append(face(bx + 40, yy + 42, 20, "calm" if k < 2 else "worried", c, "white", sw=2.2))
        rot(b, bx + 74, yy + 48, quien, c, size=14)
        pista(b, bx + 20, yy + 92, ps)
        b.append(line(bx + 20, yy + 140, bx + cw - 20, yy + 140, LGRAY, 2))
    yy += 192
    yy = frase_hueco(b, x0, yy, ww, "Lo que cambia entre las tres no es el hecho: es ______________________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una opción salta de los testimonios a un juicio:",
                  "habla de si se puede o no hacer una reconstrucción jurídica. Relee la pregunta: ¿pide qué hará un "
                  "juez, o qué muestran las diferencias entre las familias?", c)


# ───────── P6 · campo y ciudad ─────────
def i6(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Dos orillas del mismo desplazamiento", c,
                      "Un desplazamiento tiene dos orillas: el campo que se queda vacío y la ciudad que recibe. Primero "
                      "escribe lo que pasó en cada orilla. Después marca qué orilla nombra cada opción.")
    x0, ww = x + 22, w - 44
    half = (ww - 30) / 2
    for k, (rt, ps) in enumerate((("EN EL CAMPO QUE SE DEJA", "lo que perdieron las familias"),
                                  ("EN LA CIUDAD QUE RECIBE", "lo que tuvieron que enfrentar las urbes"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 120, c)
        rot(b, bx + 20, yy + 30, rt, c)
        pista(b, bx + 20, yy + 56, ps)
        b.append(line(bx + 20, yy + 96, bx + half - 20, yy + 96, LGRAY, 2))
    yy += 142
    rot(b, x0 + 120, yy + 18, "NOMBRA EL CAMPO", c, size=14)
    rot(b, x0 + 360, yy + 18, "NOMBRA LA CIUDAD", c, size=14)
    rot(b, x0 + 620, yy + 18, "NOMBRA MÁS DE UNA DIMENSIÓN", c, size=14)
    yy += 30
    for k, L in enumerate("ABCD"):
        ry = yy + k * 46
        b.append(f'<circle cx="{x0 + 40}" cy="{ry + 18}" r="17" fill="white" stroke="{c}" stroke-width="2"/>')
        b.append(T(x0 + 40, ry + 25, [L], 16, c, weight="700", anchor="middle"))
        for cx_ in (x0 + 190, x0 + 435, x0 + 735):
            b.append(checkbox(cx_, ry + 6, s=11, c=c))
    yy += 4 * 46 + 8
    return ojo(b, x0, yy, ww, "Palabras que cierran la puerta:",
               "«solo», «sin», «únicamente». Cuando una opción cierra una orilla o una dimensión con una de esas "
               "palabras, vuelve al texto y revisa si él también la cierra.")


# ───────── P7 · banano y rutas ─────────
def i7(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Sigue el banano y las rutas: qué se disputaba", c,
                      "La pregunta no pide quién disparó: pide para qué. Sigue la cadena con lo que dice el texto, "
                      "eslabón por eslabón, y la motivación sale al final.")
    x0, ww = x + 22, w - 44
    n, gap = 4, 44
    bw = (ww - gap * (n - 1)) / n
    eslabones = (("1 · LO QUE CRECÍA", "en la región, según el texto"),
                 ("2 · LO QUE HIZO LA VIOLENCIA", "con las familias de las veredas"),
                 ("3 · LO QUE QUEDÓ ATRÁS", "cuando las familias se fueron"),
                 ("4 · QUIÉN GANA CON ESO", "escríbelo con tus palabras"))
    for k, (rt, ps) in enumerate(eslabones):
        bx = x0 + k * (bw + gap)
        caja(b, bx, yy, bw, 150, c, r=24)
        rot(b, bx + 16, yy + 30, rt, c, size=13)
        pista(b, bx + 16, yy + 54, ps, size=14)
        b.append(line(bx + 16, yy + 118, bx + bw - 16, yy + 118, LGRAY, 2))
        if k < n - 1:
            b.append(hand_arrow(bx + bw + 4, yy + 75, bx + bw + gap - 4, yy + 75, c, sw=3, bend=0.0, head=14))
    yy += 170
    yy = frase_hueco(b, x0, yy, ww, "Entonces el motivo de fondo era ________________ , y no ________________ .", c)
    yy += 16
    return alto_profe(b, x0, yy, ww,
                      "Las cuatro opciones nombran una motivación: ideológica, territorial, religiosa, de urbanización. "
                      "Antes de elegir, el estudiante tiene que saber qué quiere decir cada una cuando se habla de un "
                      "conflicto armado, y qué es el despojo de tierras en la historia de Colombia.")


# ───────── P8 · María Antonieta en París 2024 ─────────
def i8(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Aplausos y reclamos: qué choca con qué", c,
                      "Dos públicos vieron la misma escena. Escribe qué valor defiende cada uno. El concepto que "
                      "buscas no es el de un lado: es el nombre del choque entre los dos.")
    x0, ww = x + 22, w - 44
    half = (ww - 120) / 2
    for k, (rt, ps) in enumerate((("LOS QUE APLAUDIERON", "«fue un homenaje artístico…»"),
                                  ("LOS QUE RECLAMARON", "«fue perturbador porque…»"))):
        bx = x0 + k * (half + 120)
        caja(b, bx, yy, half, 140, c, r=26)
        rot(b, bx + 22, yy + 32, rt, c)
        pista(b, bx + 22, yy + 58, ps)
        b.append(T(bx + 22, yy + 112, ["defienden:"], 16, GRAY))
        b.append(line(bx + 112, yy + 114, bx + half - 22, yy + 114, LGRAY, 2))
    cx = x0 + half + 60
    b.append(f'<circle cx="{cx}" cy="{yy + 70}" r="34" fill="white" stroke="{c}" stroke-width="2.4"/>')
    b.append(T(cx, yy + 78, ["vs."], 22, c, weight="700", anchor="middle"))
    yy += 160
    yy = frase_hueco(b, x0, yy, ww, "El choque entre ______________ y ______________ se llama ______________ .", c)
    yy += 16
    return trampa(b, x0, yy, ww, "Una opción habla de un «consenso absoluto»:",
                  "si el propio texto dice que unos lo vieron de una forma y otros de otra, ¿pudo haber consenso? "
                  "Otra habla de protocolos diplomáticos: búscalos en el texto antes de creerle.", c)


# ───────── P9 · voto femenino ─────────
def i9(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "La línea del voto: antes, durante y después", c,
                      "Un derecho no aparece en un día. Pon en la línea lo que el texto cuenta en cada momento y "
                      "marca qué dimensión se movió: si la línea solo tiene elecciones, te quedaste corto.")
    x0, ww = x + 22, w - 44
    ly = yy + 40
    b.append(line(x0 + 30, ly, x0 + ww - 30, ly, c, 4))
    hitos = (("ANTES DE 1954", "¿qué se reclamaba?"), ("1954", "¿qué se reconoció?"),
             ("1957", "¿qué pasó por primera vez?"), ("DÉCADAS SIGUIENTES", "¿qué debates se abrieron?"))
    sw_ = (ww - 60) / 4
    for k, (rt, ps) in enumerate(hitos):
        cx = x0 + 30 + sw_ * k + sw_ / 2
        b.append(f'<circle cx="{cx}" cy="{ly}" r="14" fill="white" stroke="{c}" stroke-width="3"/>')
        rot(b, cx, ly - 24, rt, c, size=14, anchor="middle")
        bx = cx - sw_ / 2 + 10
        caja(b, bx, ly + 28, sw_ - 20, 150, c)
        pista(b, bx + 14, ly + 56, ps, size=14)
        b.append(line(bx + 14, ly + 100, bx + sw_ - 34, ly + 100, LGRAY, 2))
        b.append(line(bx + 14, ly + 140, bx + sw_ - 34, ly + 140, LGRAY, 2))
    yy = ly + 196
    b.append(T(x0, yy + 20, ["Dimensiones que se movieron en la línea:"], 18, INK, weight="700"))
    for k, lab in enumerate(("política", "electoral", "cultural", "social", "educativa")):
        bx = x0 + 390 + k * 168
        b.append(checkbox(bx, yy + 2, s=11, c=c))
        b.append(T(bx + 30, yy + 20, [lab], 17, GRAY))
    yy += 48
    return trampa(b, x0, yy, ww, "Dos opciones dicen cosas ciertas:",
                  "las dos hablan de cambios políticos. Pero la pregunta pide la que refleja mejor la complejidad. "
                  "Cuenta cuántas de tus casillas marcadas caben en cada una.", c)


# ───────── P10 · 11-S y Colombia ─────────
def i10(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Del golpe en Nueva York al cambio en Colombia", c,
                      "Un hecho de afuera llega adentro por caminos concretos. Escribe qué cambió allá y por cuáles "
                      "tres caminos, según el texto, ese cambio llegó a Colombia.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, 360, 200, c, sw=2.6, r=24)
    rot(b, x0 + 20, yy + 32, "ESTADOS UNIDOS · 2001", c)
    pista(b, x0 + 20, yy + 58, "qué cambió en su política")
    for i in range(2):
        b.append(line(x0 + 20, yy + 110 + i * 50, x0 + 340, yy + 110 + i * 50, LGRAY, 2))
    rx = x0 + 480
    for k in range(3):
        ry = yy + k * 70
        b.append(hand_arrow(x0 + 370, yy + 100, rx - 10, ry + 30, c, sw=2.6, bend=0.12, head=14))
        caja(b, rx, ry, ww - 480, 58, c)
        b.append(T(rx + 20, ry + 36, [f"camino {k + 1} en Colombia:"], 16, GRAY, style="italic"))
    yy += 222
    yy = ojo(b, x0, yy, ww, "OJO CON LAS FECHAS",
             "El Plan Colombia empezó en 1999 y 2000, antes del 11-S. El texto no dice que el 11-S lo creó: dice "
             "que bajo ese plan se fortaleció la cooperación. Y «terrorismo» no es lo mismo que «terrorismo de "
             "Estado»: si una opción cambia la palabra, cambia el hecho.")
    return yy


Q = {1: dict(n=1, est=3, pag=370, ctx="La Violencia en la pintura · Débora Arango y Obregón",
             comp="Pensamiento social", inst=i1),
     2: dict(n=2, est=2, pag=371, ctx="Revolución Cultural en China · dos perspectivas",
             comp="Interpretación de perspectivas", inst=i2),
     3: dict(n=3, est=1, pag=371, ctx="Nacional, Copa Libertadores 1989 · un hecho con varias caras",
             comp="Pensamiento reflexivo y sistémico", inst=i3),
     4: dict(n=4, est=3, pag=372, ctx="Turbo 1980-1984 · la dimensión social del desplazamiento",
             comp="Pensamiento social", inst=i4),
     5: dict(n=5, est=2, pag=373, ctx="Turbo · testimonios que no coinciden",
             comp="Interpretación de perspectivas", inst=i5),
     6: dict(n=6, est=1, pag=373, ctx="Turbo · el campo que expulsa y la ciudad que recibe",
             comp="Pensamiento reflexivo y sistémico", inst=i6),
     7: dict(n=7, est=4, pag=373, ctx="Turbo · banano, rutas y la motivación del conflicto",
             comp="Pensamiento reflexivo y sistémico", inst=i7),
     8: dict(n=8, est=2, pag=373, ctx="París 2024 · María Antonieta y la controversia",
             comp="Interpretación de perspectivas", inst=i8),
     9: dict(n=9, est=1, pag=374, ctx="Voto femenino en Colombia · 1954 y 1957",
             comp="Pensamiento reflexivo y sistémico", inst=i9),
     10: dict(n=10, est=4, pag=374, ctx="11 de septiembre de 2001 · lo global en lo nacional",
              comp="Pensamiento reflexivo y sistémico", inst=i10)}


def build(pages=(118, 119, 121, 122, 123)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"soc4_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
