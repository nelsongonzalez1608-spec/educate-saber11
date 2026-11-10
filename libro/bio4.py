#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 4 · componente ciencia, tecnología y sociedad · páginas 161–167.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 4» de Biología, páginas 104–107.
Casos: la cirugía fetal para la gastrosquisis (1), la prótesis de hipocampo (2 a 4), las «bombas
de semillas» lanzadas desde un globo en Manizales (5 y 6), los envases comestibles con
nanotecnología (7) y las vacunas personalizadas contra el cáncer diseñadas con IA (8 a 10).

Claves verificadas (resueltas a mano contra el texto del libro, no copiadas, 7 nov 2026):

    1·B  2·C  3·C  4·A  5·D  6·A  7·A  8·C  9·A  10·A

Cómo se resolvieron:
  1 · El texto dice qué hizo la toxina: relajar la musculatura de la pared abdominal. La única
      opción que parte de ese efecto es B (menos tensión → menos presión sobre los vasos del
      intestino → menos necrosis). A, C y D parten de efectos que el texto no menciona.
  2 · Solo C compara dos grupos (con y sin prótesis) en una variable medible (memoria a corto
      plazo). A y D hablan del futuro sin decir cómo medir; B no tiene con quién comparar.
  3 · El implante se probó en pacientes; usarlo en estudiantes sin diagnóstico es aplicarlo a
      quien no lo necesita y en quien no se probó → C.
  4 · El texto: interpreta señales eléctricas y las transforma en patrones que fortalecen la
      codificación y la recuperación de recuerdos → A (estimulación dirigida). B pone el chip en
      la médula, C dice «aleatorios», D dice que bloquea la excitación.
  5 · Los sensores midieron temperatura, presión y humedad para evaluar la germinación → D.
  6 · Fijar nitrógeno: pasar el N2 del aire a compuestos que la planta puede usar → A.
  7 · El cambio de color responde a un cambio químico (pH) del medio → A. OJO: el texto atribuye
      la detección a «sensores» y la acción antimicrobiana a las nanopartículas; la opción A le
      pasa el cambio de color a las nanopartículas. Es la mejor de las cuatro, pero imprecisa:
      registrado como hallazgo.
  8 · Validar eficacia es relacionar la respuesta inmune (linfocitos T) con el resultado clínico
      (remisión) → C.
  9 · El objetivo es personalizar la vacuna para cada paciente → A. OJO: la opción A dice «adaptar
      al sistema inmune del paciente para disminuir efectos secundarios», cuando el texto adapta
      la vacuna al tumor (neoantígenos) y la menor toxicidad es un resultado, no el objetivo. Las
      otras tres contradicen el texto; A es la única defendible, pero mal redactada: hallazgo.
 10 · La IA identifica neoantígenos y con ellos se activan linfocitos T → A.

Reparto: A 5 · B 1 · C 3 · D 1 (la mitad en A: 4, 6, 7, 9 y 10). Registrado.

Estrategias:
    1 · ¿Se puede poner a prueba?                     (2, 5, 8     · ICFES 99)   azul
    2 · El mecanismo, eslabón por eslabón             (1, 4, 10    · ICFES 100)  morado
    3 · Para qué sirve cada pieza                     (6, 7        · ICFES 111)  oro
    4 · Lo que la evidencia respalda (y lo que no)    (3, 9        · ICFES 101)  rojo

Hojas: 161 bio4_t1 (1-2) · 162 bio4_t2 (3-4) · 163 bio4_i1 · 164 bio4_t3 (5-6) ·
       165 bio4_t4 (7-8) · 166 bio4_t5 (9-10) · 167 bio4_i2.
"""
from taller_base import *

configurar("Biología", 4, "ciencia, tecnología y sociedad",
           tema="Cada invento es una oportunidad y un riesgo",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("¿Se puede poner a prueba?", EDU_AZUL),
       2: ("El mecanismo, eslabón por eslabón", MORADO),
       3: ("Para qué sirve cada pieza", EDU_ORO),
       4: ("Lo que la evidencia respalda (y lo que no)", EDU_ROJO)}
usar_estrategias(EST)
AZ, MO, OR, RO = (EST[k][1] for k in (1, 2, 3, 4))
VERDE = A["color"]


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


# ───────── P1 · cirugía fetal · la toxina botulínica ─────────
def i1(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La cadena de la toxina, eslabón por eslabón", c,
                      "Una explicación rigurosa empieza por lo que el texto dice que hizo la toxina y avanza sin saltos. "
                      "Llena los eslabones de arriba abajo: cada uno tiene que salir del anterior.")
    x0, ww = x + 22, w - 44
    esl = (("1 · LO QUE HIZO LA TOXINA", "cópialo del texto, palabra por palabra"),
           ("2 · ENTONCES LA PARED DEL ABDOMEN…", "¿más tensa o menos tensa?"),
           ("3 · ENTONCES LO QUE PASA POR EL ORIFICIO…", "¿queda más apretado o más libre?"),
           ("4 · Y ESO PROTEGE AL INTESTINO DE…", "¿qué riesgo se evita?"))
    ew, eh = ww - 300, 92
    for k, (rt, ps) in enumerate(esl):
        ey = yy + k * (eh + 22)
        ex = x0 + k * 40
        caja(b, ex, ey, ew, eh, c, sw=2.2, r=46)
        rot(b, ex + 34, ey + 32, rt, c, size=14)
        pista(b, ex + 34 + tw(rt, 14, "700") + len(rt) * 1.5 + 14, ey + 32, ps)
        renglon(b, ex + 34, ey + 70, ex + ew - 34)
        if k < 3:
            b.append(hand_arrow(ex + ew - 60, ey + eh + 2, ex + ew - 20, ey + eh + 20, c, sw=2.4, bend=-0.3,
                                head=10))
    yy += 4 * (eh + 22) + 4
    yy = alto_profe(b, x0, yy, ww,
                    "Gastrosquisis: el intestino del bebé crece por fuera del abdomen, por un orificio en la pared. "
                    "Pregúntale al profe qué le pasa a un órgano vivo cuando lo aprieta un orificio estrecho durante "
                    "semanas.")
    return ojo(b, x0, yy + 14, ww, "SUBRAYA EL PRIMER ESLABÓN DE CADA OPCIÓN",
               "¿Empieza por lo mismo que tu eslabón 1? Una opción que arranca por un efecto que el texto no le "
               "atribuye a la toxina puede sonar muy científica y aun así no explicar este caso.")


# ───────── P2 · prótesis de hipocampo · hipótesis evaluable ─────────
def i2(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El banco de pruebas: ¿cabe en un experimento?", c,
                      "Una hipótesis se puede evaluar si cabe en un experimento: hay con quién comparar, hay algo que "
                      "medir y el resultado llega en un tiempo razonable. Trata de montar cada opción en el banco.")
    x0, ww = x + 22, w - 44
    filas = ("¿CON QUIÉN LO COMPARO?", "¿QUÉ NÚMERO MIDO?", "¿CUÁNDO TENGO EL RESULTADO?")
    lw = max(tw(f, 14, "700") + len(f) * 1.5 for f in filas) + 30
    cw_ = (ww - lw) / 4
    for k, L in enumerate("ABCD"):
        letra(b, x0 + lw + k * cw_ + cw_ / 2, yy + 22, L, c, r=19, size=17)
    for i, f in enumerate(filas):
        ry = yy + 54 + i * 96
        rot(b, x0, ry + 44, f, c, size=14)
        for k in range(4):
            caja(b, x0 + lw + k * cw_ + 6, ry, cw_ - 12, 82, c, r=10)
    yy += 54 + 3 * 96 + 6
    b.append(T(x0, yy + 20, ["Pon una X debajo de cada opción que no pudiste montar en el banco:"], 18, INK,
               weight="700"))
    yy += 36
    for k in range(4):
        cxx = x0 + lw + k * cw_ + cw_ / 2
        b.append(checkbox(cxx - 14, yy, s=14, c=c))
    yy += 48
    return ojo(b, x0, yy, ww, "SI QUEDÓ UNA CASILLA VACÍA, NO CABE",
               "Una hipótesis que se puede evaluar dice qué grupos se comparan y qué variable se mide. Si al montar "
               "una opción en el banco no supiste qué escribir en alguna fila, esa opción todavía no es un "
               "experimento.")


# ───────── P3 · prótesis de hipocampo · uso responsable ─────────
def i3(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "¿Para quién se probó y para quién se usa?", c,
                      "La evidencia de un estudio vale para las personas en las que se probó. Llena la ficha con lo "
                      "que dice el texto y después pon cada opción del lado que le corresponde: dentro de lo probado "
                      "o fuera de lo probado.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 170, c, sw=2.4, r=16, fill=A["bg"])
    rot(b, x0 + 24, yy + 32, "FICHA DE LA EVIDENCIA", c, size=15)
    campos = (("se probó en:", 0), ("para tratar:", 1), ("el resultado fue:", 2))
    for t, k in campos:
        b.append(T(x0 + 24, yy + 76 + k * 38, [t], 17, INK))
        renglon(b, x0 + 190, yy + 80 + k * 38, x0 + ww - 24)
    yy += 192
    half = (ww - 30) / 2
    for k, (rt, ps) in enumerate((("DENTRO DE LO PROBADO", "escribe aquí las letras"),
                                  ("FUERA DE LO PROBADO", "escribe aquí las letras"))):
        px = x0 + k * (half + 30)
        caja(b, px, yy, half, 140, c, sw=2.2, r=70 if k else 16, dash="8,6" if k else None)
        rot(b, px + half / 2, yy + 36, rt, c, size=15, anchor="middle")
        pista(b, px + half / 2, yy + 62, ps, anchor="middle")
    yy += 160
    caja(b, x0, yy, ww, 104, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA OPCIÓN DEL LADO DE AFUERA, ¿A QUIÉN PONE EN RIESGO?", c, size=14)
    renglon(b, x0 + 20, yy + 80, x0 + ww - 20)
    yy += 120
    return trampa(b, x0, yy, ww, "No toda novedad choca con el uso responsable:",
                  "la ciencia avanza discutiendo y mejorando. Lo que choca es usar algo donde la evidencia no lo "
                  "respalda. Revisa en qué lado de tu ficha quedó cada opción antes de decidir.", c)


# ───────── P4 · prótesis de hipocampo · el mecanismo ─────────
def i4(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "El recorrido de la señal hasta el recuerdo", c,
                      "Sigue la señal por el dibujo: de las neuronas al dispositivo y de vuelta. Escribe en cada "
                      "estación lo que el texto dice que pasa ahí. Después revisa si cada opción respeta el lugar "
                      "y el tipo de señal.")
    x0, ww = x + 22, w - 44
    # neurona de entrada · dispositivo · neurona de salida
    cy = yy + 130
    def neurona(cx, etiqueta):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="38" fill="{SOFT}" stroke="{c}" stroke-width="2.6"/>')
        for a in (200, 240, 120, 160):
            ra = math.radians(a)
            b.append(line(cx + 38 * math.cos(ra), cy + 38 * math.sin(ra), cx + 70 * math.cos(ra),
                          cy + 70 * math.sin(ra), c, 2.4))
        b.append(line(cx + 38, cy, cx + 110, cy, c, 3))
        rot(b, cx + 30, cy + 70, etiqueta, c, size=13, anchor="middle")
    neurona(x0 + 100, "LAS NEURONAS")
    dx = x0 + ww / 2 - 120
    caja(b, dx, cy - 56, 240, 112, c, sw=2.8, r=12, fill=A["bg"])
    for k in range(5):
        b.append(line(dx + 30 + k * 45, cy - 56, dx + 30 + k * 45, cy - 72, c, 2.4))
        b.append(line(dx + 30 + k * 45, cy + 56, dx + 30 + k * 45, cy + 72, c, 2.4))
    rot(b, dx + 120, cy + 6, "EL DISPOSITIVO", c, size=14, anchor="middle")
    neurona(x0 + ww - 230, "DE VUELTA AL CEREBRO")
    b.append(hand_arrow(x0 + 212, cy, dx - 8, cy, c, sw=2.6, bend=0.0, head=12))
    b.append(hand_arrow(dx + 248, cy, x0 + ww - 280, cy, c, sw=2.6, bend=0.0, head=12))
    yy = cy + 104
    est = (("1 · LO QUE ENTRA", "¿qué tipo de señal?"), ("2 · LO QUE HACE EL DISPOSITIVO", "¿qué la vuelve?"),
           ("3 · LO QUE SALE Y FORTALECE", "¿qué dos procesos de la memoria?"))
    gap = 24
    bw = (ww - 2 * gap) / 3
    for k, (rt, ps) in enumerate(est):
        px = x0 + k * (bw + gap)
        caja(b, px, yy, bw, 128, c, r=14)
        rot(b, px + 16, yy + 28, rt, c, size=13)
        pista(b, px + 16, yy + 52, ps)
        renglon(b, px + 16, yy + 88, px + bw - 16)
        renglon(b, px + 16, yy + 116, px + bw - 16)
    yy += 150
    b.append(T(x0, yy + 20, ["Revisa cada opción con dos preguntas: ¿dónde actúa? y ¿la señal es dirigida o al azar?"],
               18, INK, weight="700"))
    yy += 40
    for k, L in enumerate("ABCD"):
        px = x0 + k * (ww / 4)
        letra(b, px + 18, yy + 22, L, c)
        caja(b, px + 46, yy, ww / 4 - 64, 44, c)
        pista(b, px + 58, yy + 28, "dónde · cómo", size=13)
    return yy + 60


# ───────── P5 · bombas de semillas · uso de los datos ─────────
def i5(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Sensores conectados con la pregunta del proyecto", c,
                      "Unos datos sirven si responden la pregunta para la que se tomaron. Escribe junto a cada "
                      "sensor qué le podría pasar a una semilla viva si ese valor fuera extremo, y abajo la pregunta "
                      "del proyecto con las palabras del texto.")
    x0, ww = x + 22, w - 44
    sens = ("TEMPERATURA", "PRESIÓN", "HUMEDAD")
    sw_, sh = 300, 70
    for k, s_ in enumerate(sens):
        sy = yy + 10 + k * 96
        caja(b, x0, sy, sw_, sh, c, sw=2.4, r=35)
        rot(b, x0 + sw_ / 2, sy + 42, s_, c, size=15, anchor="middle")
        b.append(hand_arrow(x0 + sw_ + 8, sy + sh / 2, x0 + sw_ + 60, sy + sh / 2, c, sw=2.4, bend=0.0, head=10))
        pista(b, x0 + sw_ + 76, sy + 26, "si fuera extremo, a la semilla le podría pasar que…")
        renglon(b, x0 + sw_ + 76, sy + 62, x0 + ww)
    yy += 300
    caja(b, x0, yy, ww, 110, c, sw=2.4, r=14, fill=A["bg"])
    rot(b, x0 + 20, yy + 30, "LA PREGUNTA DEL PROYECTO, SEGÚN EL TEXTO", c, size=14)
    pista(b, x0 + 20, yy + 56, "«los datos servirán para evaluar…»")
    renglon(b, x0 + 20, yy + 92, x0 + ww - 20)
    yy += 128
    return ojo(b, x0, yy, ww, "UN BUEN USO DE LOS DATOS NO LES PIDE DE MÁS",
               "Fíjate qué midió la cápsula y para qué. Un análisis que concluye algo que ningún sensor registró, "
               "o que no tiene que ver con la pregunta del proyecto, le pide a los datos más de lo que pueden dar.")


# ───────── P6 · bombas de semillas · bacterias fijadoras ─────────
def i6(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El viaje del nitrógeno con casillas vacías", c,
                      "El nitrógeno viaja del aire al suelo, a las plantas y a los animales, y en cada lugar está en "
                      "una forma distinta. Escribe en cada casilla en qué forma está y, en el recuadro de cada flecha, "
                      "quién hace ese paso.")
    x0, ww = x + 22, w - 44
    est = ("1 · EN EL AIRE", "2 · EN EL SUELO", "3 · EN LA PLANTA", "4 · EN EL ANIMAL")
    gap = 76
    bw = (ww - 3 * gap) / 4
    by, bh = yy + 70, 150
    for k, rt in enumerate(est):
        bx = x0 + k * (bw + gap)
        caja(b, bx, by, bw, bh, c, sw=2.4, r=16)
        rot(b, bx + 16, by + 28, rt, c, size=13)
        pista(b, bx + 16, by + 54, "está como:")
        renglon(b, bx + 16, by + 96, bx + bw - 16)
        renglon(b, bx + 16, by + 132, bx + bw - 16)
        if k < 3:
            ax = bx + bw + 8
            b.append(hand_arrow(ax, by + bh / 2, ax + gap - 16, by + bh / 2, c, sw=2.8, bend=0.0, head=12))
            b.append(rect(ax - 40, by - 58, gap + 64, 40, "white", r=8, stroke=c, sw=1.8, dash="5,5"))
            pista(b, ax + gap / 2 - 4, by - 66, "¿quién?", size=13, anchor="middle")
    # regreso al suelo cuando mueren
    x4 = x0 + 3 * (bw + gap) + bw / 2
    x2 = x0 + (bw + gap) + bw / 2
    yb = by + bh + 8
    b.append(f'<path d="M {x4:.0f} {yb} Q {(x4 + x2) / 2:.0f} {yb + 150} {x2 + 10:.0f} {yb + 4}" fill="none" '
             f'stroke="{c}" stroke-width="2.6" stroke-dasharray="9,7"/>')
    b.append(hand_arrow(x2 + 40, yb + 34, x2 + 12, yb + 6, c, sw=2.6, bend=0.0, head=12))
    lx = (x4 + x2) / 2
    b.append(rect(lx - 170, yb + 52, 340, 44, "white", r=8, stroke=c, sw=1.8, dash="5,5"))
    pista(b, lx, yb + 118, "cuando mueren, ¿quién lo devuelve al suelo?", size=13, anchor="middle")
    yy = yb + 140
    return frase_hueco(b, x0, yy, ww, "Las bacterias de las cápsulas hacen el paso de la casilla ____ a la casilla "
                                      "____ .", c)


# ───────── P7 · envases con nanotecnología ─────────
def i7(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Las piezas del envase inteligente", c,
                      "El envase tiene varias piezas y cada una hace una cosa. Une cada pieza con lo que hace según "
                      "el texto. La pregunta es solo sobre una función: cambiar de color cuando cambia el pH.")
    x0, ww = x + 22, w - 44
    piezas = ("NANOPARTÍCULAS ANTIMICROBIANAS", "SENSORES DE ACIDEZ Y GASES", "NUTRIENTES ENCAPSULADOS")
    funciones = ("inhibir bacterias", "detectar el deterioro y cambiar de color", "mejorar el valor nutricional")
    pw = 420
    for k, p in enumerate(piezas):
        py = yy + 10 + k * 84
        caja(b, x0, py, pw, 64, c, sw=2.4, r=32)
        rot(b, x0 + pw / 2, py + 39, p, c, size=14, anchor="middle")
        b.append(f'<circle cx="{x0 + pw + 18}" cy="{py + 32}" r="7" fill="{c}"/>')
    fx = x0 + ww - 470
    orden = (2, 0, 1)
    for k, j in enumerate(orden):
        py = yy + 10 + k * 84
        b.append(f'<circle cx="{fx - 18}" cy="{py + 32}" r="7" fill="{c}"/>')
        caja(b, fx, py, 470, 64, c, r=12)
        b.append(T(fx + 20, py + 39, [funciones[j]], 17, INK))
    yy += 270
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("¿QUÉ CAMBIA EN LA FRUTA QUE SE DAÑA?", "lo que detecta el envase"),
                                  ("¿ESE CAMBIO ES QUÍMICO O FÍSICO?", "¿cambia una sustancia, o la luz o el calor?"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 116, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=13)
        pista(b, px + 18, yy + 52, ps)
        renglon(b, px + 18, yy + 92, px + half - 18)
    yy += 132
    return alto_profe(b, x0, yy, ww,
                      "Indicador de pH: una sustancia que cambia de color según qué tan ácido o básico está el medio "
                      "(como el agua del repollo morado). Pregúntale al profe por qué el color cambia cuando cambia "
                      "la química y no cuando cambia la luz.")


# ───────── P8 · vacunas personalizadas · validar la eficacia ─────────
def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos ejes para probar que la vacuna sirve", c,
                      "Validar la eficacia es mostrar que, cuando la vacuna hace su trabajo, el paciente mejora. Pon "
                      "en un eje lo que la vacuna provoca en el cuerpo y en el otro lo que significa mejorar. Dibuja "
                      "la tendencia que esperarías si funciona.")
    x0, ww = x + 22, w - 44
    gx, gy, gw, gh = x0 + 80, yy + 20, 470, 300
    b.append(line(gx, gy + gh, gx + gw, gy + gh, INK, 2.6))
    b.append(line(gx, gy, gx, gy + gh, INK, 2.6))
    b.append(f'<path d="M {gx + gw} {gy + gh} L {gx + gw - 14} {gy + gh - 7} L {gx + gw - 14} {gy + gh + 7} Z" '
             f'fill="{INK}"/>')
    b.append(f'<path d="M {gx} {gy} L {gx - 7} {gy + 14} L {gx + 7} {gy + 14} Z" fill="{INK}"/>')
    for k in range(1, 5):
        b.append(line(gx, gy + gh - k * gh / 5, gx + gw, gy + gh - k * gh / 5, LGRAY, 1.4, dash="3,6"))
    caja(b, gx + 20, gy + gh + 16, gw - 40, 44, c, r=8)
    pista(b, gx + gw / 2, gy + gh + 80, "eje x: lo que la vacuna provoca", anchor="middle")
    pista(b, gx + 18, gy + 20, "eje y (la caja de la izquierda): lo que significa mejorar")
    b.append(f'<g transform="rotate(-90 {x0 + 24} {gy + gh / 2})">'
             + rect(x0 + 24 - 120, gy + gh / 2 - 22, 240, 44, "white", r=8, stroke=c, sw=2) + "</g>")
    rx = gx + gw + 50
    rw = x0 + ww - rx
    caja(b, rx, gy, rw, 140, c, r=14)
    rot(b, rx + 18, gy + 28, "LA VARIABLE DE LA ENFERMEDAD", c, size=14)
    pista(b, rx + 18, gy + 52, "¿qué le pasa al cáncer si la vacuna sirve?")
    renglon(b, rx + 18, gy + 92, rx + rw - 18)
    renglon(b, rx + 18, gy + 124, rx + rw - 18)
    caja(b, rx, gy + 160, rw, 140, c, r=14)
    rot(b, rx + 18, gy + 188, "LA VARIABLE DEL SISTEMA INMUNE", c, size=14)
    pista(b, rx + 18, gy + 212, "¿qué células activa la vacuna, según el texto?")
    renglon(b, rx + 18, gy + 252, rx + rw - 18)
    renglon(b, rx + 18, gy + 284, rx + rw - 18)
    yy = gy + gh + 104
    return ojo(b, x0, yy, ww, "UNA RELACIÓN QUE VALIDA TIENE A LA ENFERMEDAD EN UN EJE",
               "Si ninguna de las dos variables de una opción dice si el paciente mejoró, esa relación describe "
               "algo, pero no prueba que la vacuna funciona. Busca la que tenga tus dos ejes.")


# ───────── P9 · vacunas personalizadas · el objetivo ─────────
def i9(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Personalizada, ¿para quién y contra qué?", c,
                      "El objetivo de una tecnología está en las palabras del texto, no en lo que uno se imagina de "
                      "ella. Contesta las tres preguntas con lo que dice el párrafo y después mide cada opción con "
                      "tus respuestas.")
    x0, ww = x + 22, w - 44
    preg = (("¿QUÉ HACE LA TECNOLOGÍA?", "un verbo del texto"), ("¿PARA QUIÉN?", "¿todos o cada uno?"),
            ("¿CONTRA QUÉ?", "¿qué enfermedad?"))
    gap = 24
    bw = (ww - 2 * gap) / 3
    for k, (rt, ps) in enumerate(preg):
        px = x0 + k * (bw + gap)
        caja(b, px, yy, bw, 130, c, sw=2.4, r=16)
        rot(b, px + 18, yy + 30, rt, c, size=14)
        pista(b, px + 18, yy + 56, ps)
        renglon(b, px + 18, yy + 96, px + bw - 18)
    yy += 154
    b.append(T(x0, yy + 20, ["¿Cuántas de tus tres respuestas respeta cada opción? (0 a 3)"], 18, INK, weight="700"))
    yy += 36
    for k, L in enumerate("ABCD"):
        bx = x0 + k * 190
        letra(b, bx + 18, yy + 22, L, c)
        caja(b, bx + 48, yy, 70, 44, c)
    yy += 66
    return ojo(b, x0, yy, ww, "PALABRAS QUE NO ADMITEN EXCEPCIÓN",
               "Encierra en cada opción las palabras absolutas, las que no dejan espacio a ninguna excepción. "
               "Después busca en el párrafo si el texto dice algo tan absoluto. Si no lo dice, la opción va más "
               "allá del texto.")


# ───────── P10 · vacunas personalizadas · la inmunidad adaptativa ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La carrera de relevos de la vacuna", c,
                      "Cuatro corredores se pasan el testigo hasta que el sistema inmune ataca al tumor. Escribe sobre "
                      "cada corredor qué hace y en la mano qué le entrega al siguiente.")
    x0, ww = x + 22, w - 44
    corredores = ("LA INTELIGENCIA ARTIFICIAL", "LA VACUNA DE ARNm", "LAS CÉLULAS DEL PACIENTE",
                  "EL SISTEMA INMUNE")
    n = 4
    gap = 36
    cw_ = (ww - (n - 1) * gap) / n
    pista_y = yy + 250
    b.append(line(x0, pista_y, x0 + ww, pista_y, c, 3))
    b.append(line(x0, pista_y + 16, x0 + ww, pista_y + 16, c, 1.6, dash="10,8"))
    for k, cr in enumerate(corredores):
        px = x0 + k * (cw_ + gap)
        caja(b, px, yy, cw_, 150, c, sw=2.2, r=14)
        rot(b, px + 14, yy + 28, cr, c, size=12)
        pista(b, px + 14, yy + 54, "lo que hace:")
        renglon(b, px + 14, yy + 92, px + cw_ - 14)
        renglon(b, px + 14, yy + 128, px + cw_ - 14)
        # corredor esquemático
        hx = px + cw_ / 2
        b.append(f'<circle cx="{hx}" cy="{yy + 172}" r="12" fill="white" stroke="{c}" stroke-width="2.4"/>')
        b.append(line(hx, yy + 184, hx - 8, yy + 214, c, 3))
        b.append(line(hx - 8, yy + 214, hx - 24, pista_y - 2, c, 3))
        b.append(line(hx - 8, yy + 214, hx + 14, pista_y - 2, c, 3))
        b.append(line(hx - 3, yy + 194, hx + 26, yy + 202, c, 3))
        if k < n - 1:
            tx = px + cw_ - 6
            caja(b, tx - 40, yy + 268, 120, 40, c, r=8, dash="5,5")
            pista(b, tx + 20, yy + 326, "le entrega", anchor="middle")
    yy = pista_y + 98
    yy = frase_hueco(b, x0, yy, ww, "Lo que el último corredor recibe y reconoce en el tumor se llama "
                                    "______________________ .", c)
    return trampa(b, x0, yy + 16, ww, "Adaptativo quiere decir dirigido:",
                  "el sistema inmune adaptativo ataca algo que reconoce, no todo lo que encuentra. Revisa si la opción "
                  "que elegiste tiene a alguien reconociendo algo concreto del tumor de ese paciente.", c)


Q = {1: dict(n=1, est=2, pag=104, ctx="Cirugía fetal · por qué sirve la toxina botulínica",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=1, pag=105, ctx="Prótesis de hipocampo · una hipótesis que se pueda evaluar",
             comp="Indagación", inst=i2),
     3: dict(n=3, est=4, pag=105, ctx="Prótesis de hipocampo · el uso responsable de la ciencia",
             comp="Uso comprensivo del conocimiento científico", inst=i3),
     4: dict(n=4, est=2, pag=105, ctx="Prótesis de hipocampo · cómo mejora la memoria",
             comp="Explicación de fenómenos", inst=i4),
     5: dict(n=5, est=1, pag=106, ctx="Bombas de semillas desde un globo · para qué sirven los datos",
             comp="Indagación", inst=i5),
     6: dict(n=6, est=3, pag=106, ctx="Bombas de semillas · qué hacen las bacterias fijadoras",
             comp="Uso comprensivo del conocimiento científico", inst=i6),
     7: dict(n=7, est=3, pag=106, ctx="Envases comestibles con nanotecnología · por qué cambian de color",
             comp="Explicación de fenómenos", inst=i7),
     8: dict(n=8, est=1, pag=107, ctx="Vacunas personalizadas con IA · cómo validar la eficacia",
             comp="Indagación", inst=i8),
     9: dict(n=9, est=4, pag=107, ctx="Vacunas personalizadas con IA · el objetivo, según el texto",
             comp="Uso comprensivo del conocimiento científico", inst=i9),
     10: dict(n=10, est=2, pag=107, ctx="Vacunas personalizadas con IA · cómo se activa la defensa",
              comp="Explicación de fenómenos", inst=i10)}


def build(pages=(161, 162, 164, 165, 166)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"bio4_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
