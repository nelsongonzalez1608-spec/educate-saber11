#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Física · Misión 3 · componente físico, electromagnetismo · páginas 240–246.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 3» de Física (fuente_libro/FÍSICA), páginas 226–228.
Casos: el imán que entra y sale de una bobina con galvanómetro (1), el freno electromagnético
del tren urbano (2 y 3), el sensor de campo eléctrico en la tormenta (4), los descargadores
estáticos del avión y la maqueta del ala (5 a 7) y la desmagnetización de agujas con una llama
(8 a 10).

Claves verificadas (resueltas a mano contra el texto y las figuras del libro, no copiadas, 7 nov 2026):

    1·D  2·C  3·B  4·A  5·B  6·B  7·A  8·B  9·B  10·A

Cómo se resolvieron:
  1 · Se induce corriente solo mientras cambia el flujo magnético dentro de la bobina (el imán
      entra o sale); con el imán quieto, aunque esté adentro, la aguja no se mueve → D (ley de
      Faraday). A es falsa (la inducción no exige material ferromagnético); C es falsa (el
      montaje no tiene batería y hay corriente). OJO: D dice que la afirmación «es correcta»,
      pero el estudiante dijo que el campo «interactúa directamente con los electrones y los
      empuja»; un campo quieto no mueve electrones quietos: lo que cuenta es que el campo
      CAMBIE. B también dice «correcta» y habla de que el campo varía (hallazgo Media).
  2 · La explicación es: imanes → corrientes inducidas en los rieles → campo opuesto → fuerza que
      frena. Las corrientes inducidas exigen un campo que varía: medir la variación del campo
      durante el frenado pone a prueba el eslabón central → C. A, B y D no tocan la cadena (masa
      y longitud, el peso en reposo, el voltaje al arrancar).
  3 · 90 km/h = 90 000 m / 3600 s = 25 m/s; 10 km/h = 10 000 m / 3600 s ≈ 2,78 m/s.
      Δv = 2,78 − 25 = −22,22 m/s; |a| = 22,22 m/s ÷ 6 s ≈ 3,70 m/s² → B. Si se divide sin
      convertir: 80 ÷ 6 ≈ 13,3 (km/h)/s, que no está en las opciones.
  4 · Las líneas de campo eléctrico salen de cargas positivas y llegan a negativas; si se curvan
      y se aprietan cerca del sensor es porque apareció o se movió una carga cerca → A. B (el
      vapor «cambia la polaridad») y C (el campo MAGNÉTICO) no explican un cambio del campo
      eléctrico; D contradice el modelo (las líneas no se vuelven aleatorias). OJO: el texto no
      dice el signo de la carga; A dice «negativa» (la base de las nubes de tormenta suele ser
      negativa): Atención.
  5 · La afirmación habla de la fuerza del campo sobre las cargas, en la punta del ala: el dato
      que la pone a prueba es esa fuerza, en ese lugar → B.
  6 · Dos cargas positivas idénticas: las líneas salen de cada carga y se apartan en el medio
      (repulsión, nunca van de una a la otra) → B. A muestra una sola carga; C, líneas paralelas
      que cruzan entre las dos; D, cargas negativas. OJO: en la figura B del libro las flechas
      apuntan HACIA la línea que une las cargas (como si llegaran a ellas); con cargas positivas
      deberían apuntar hacia afuera (hallazgo Media).
  7 · F = qE = (2 × 10⁻⁶ C)(400 N/C) = 8 × 10⁻⁴ N. Carga positiva: la fuerza va en el mismo
      sentido del campo, hacia la izquierda → A. El libro no escribe las unidades (ni C ni N):
      hallazgo Baja.
  8 · La idea dice que el calor desordena los dominios; el modelo dice que eso pasa al superar
      la temperatura de Curie. El dato que la prueba es la temperatura que alcanza la aguja y si
      supera esa temperatura → B.
  9 · Misma fuente, mismo tiempo: las dos agujas suben de temperatura parecido y el níquel llega
      antes a su temperatura de Curie (358 °C contra 770 °C) → B. C usa la conductividad, dato
      que el texto no da y que no es el umbral.
 10 · Al calentar, los átomos vibran más (energía cinética), se desordenan los dominios y al
      superar la temperatura de Curie el material deja de ser ferromagnético → A. B culpa al imán
      (lo que se calienta es la aguja), C a la dilatación y D a una ionización sin evidencia.

Reparto: A 3 · B 5 · C 1 · D 1. La B concentra la mitad (3, 5, 6, 8, 9; tres seguidas en
8-9 y 5-6): hallazgo Atención.

Estrategias:
    1 · Busca el dato que decide     (2, 5, 8      · ICFES 31 del cuadernillo 2025)  azul
    2 · Dibuja el campo primero      (4, 6         · ICFES 42 del cuadernillo 2025)  rojo
    3 · Signo, sentido y unidad      (3, 7         · ICFES 72 de 2016-1 2.ª ses.)    oro
    4 · Del modelo al mecanismo      (1, 9, 10     · ICFES 19 del cuadernillo 2025)  morado

Hojas: 240 fis3_t1 (1-2) · 241 fis3_t2 (3-4) · 242 fis3_i1 · 243 fis3_t3 (5-6) ·
       244 fis3_t4 (7-8) · 245 fis3_t5 (9-10) · 246 fis3_i2.
"""
from taller_base import *

configurar("Física", 3, "físico · electromagnetismo",
           tema="Lo que mueve a las cargas",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Busca el dato que decide", EDU_AZUL),
       2: ("Dibuja el campo primero", EDU_ROJO),
       3: ("Signo, sentido y unidad", EDU_ORO),
       4: ("Del modelo al mecanismo", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))
OLIVA = A["color"]


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


def casillas(b, x, y, labels, c, paso=150, size=16):
    for k, lab in enumerate(labels):
        b.append(checkbox(x + k * paso, y, s=10, c=c))
        b.append(T(x + k * paso + 28, y + 16, [lab], size, GRAY))


def txt_izq(b, x, y, txt, w, size=16, color=INK, lh=None):
    """Rótulo corto de varias líneas, alineado a la izquierda (no es párrafo corrido)."""
    lh = lh or size + 5
    lineas = [" ".join(p) for p in wrap_px(txt, size, w)]
    b.append(T(x, y + size, lineas, size, color, lh=lh))
    return y + size + (len(lineas) - 1) * lh


def carga(b, cx, cy, signo, c=INK, r=18):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#DCEAF7" stroke="{c}" stroke-width="2.4"/>')
    b.append(line(cx - 8, cy, cx + 8, cy, c, 2.6))
    if signo == "+":
        b.append(line(cx, cy - 8, cx, cy + 8, c, 2.6))


# ───────── P1 · imán y bobina · ¿es correcta la explicación? ─────────
def _bobina(b, x, y, c):
    for k in range(7):
        b.append(f'<ellipse cx="{x + 30 + k * 16}" cy="{y + 40}" rx="9" ry="34" fill="none" stroke="{c}" '
                 f'stroke-width="2.2"/>')


def i1(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "La aguja del galvanómetro en cuatro momentos", c,
                      "El estudiante dice que el campo del imán «empuja» a los electrones. Pon a prueba esa idea "
                      "con lo que pasa en el montaje. En cada momento marca si el campo dentro de la bobina está "
                      "cambiando y si la aguja se mueve.")
    x0, ww = x + 22, w - 44
    cols = (("MOMENTO", 430), ("¿HAY CAMPO DENTRO DE LA BOBINA?", 270), ("¿ESE CAMPO ESTÁ CAMBIANDO?", 262),
            ("¿SE MUEVE LA AGUJA?", ww - 962))
    hy = yy + 4
    px = x0
    for t, cw in cols:
        caja(b, px, hy, cw, 50, c, r=0, fill=A["bg"])
        rot(b, px + cw / 2, hy + 31, t, c, size=12, anchor="middle")
        px += cw
    momentos = ("1 · el imán quieto, lejos de la bobina", "2 · el imán entrando a la bobina",
                "3 · el imán quieto, dentro de la bobina", "4 · el imán saliendo de la bobina")
    for k, m in enumerate(momentos):
        ry = hy + 50 + k * 58
        px = x0
        for j, (t, cw) in enumerate(cols):
            caja(b, px, ry, cw, 58, c, r=0)
            if j == 0:
                b.append(T(px + 16, ry + 36, [m], 17, INK))
            else:
                casillas(b, px + cw / 2 - 65, ry + 19, ("sí", "no"), c, paso=90)
            px += cw
    yy = hy + 50 + 4 * 58 + 20
    yy = frase_hueco(b, x0, yy, ww, "La aguja se mueve solo cuando el campo dentro de la bobina ______________ .",
                     c)
    half = (ww - 24) / 2
    yy += 16
    for k, (rt, ps) in enumerate((("LO QUE DIJO EL ESTUDIANTE", "¿en qué momento de la tabla falla?"),
                                  ("LO QUE DICE EL MODELO (LEY DE FARADAY)", "con tus palabras"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 132, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        pista(b, px + 18, yy + 52, ps)
        renglon(b, px + 18, yy + 88, px + half - 18)
        renglon(b, px + 18, yy + 120, px + half - 18)
    yy += 148
    return ojo(b, x0, yy, ww, "LEE LA RAZÓN, NO SOLO EL VEREDICTO",
               "cada opción dice si la afirmación es correcta o incorrecta y da una razón. Quédate con la opción "
               "cuya razón coincide con lo que marcaste en la tabla, aunque el veredicto te sorprenda.")


# ───────── P2 · freno del tren · qué dato evalúa la explicación ─────────
def i2(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Los eslabones del freno sin contacto", c,
                      "La explicación del ingeniero es una cadena: si un eslabón falla, se cae todo. Completa el "
                      "eslabón que falta y después piensa qué dato habría que medir para saber si ese eslabón "
                      "de verdad ocurre.")
    x0, ww = x + 22, w - 44
    esl = ("Se activan los imanes del tren", "?", "Aparecen corrientes inducidas en los rieles",
           "Esas corrientes crean un campo opuesto", "Una fuerza frena al tren")
    n = len(esl)
    gap = 34
    ew = (ww - (n - 1) * gap) / n
    eh = 150
    for k, t in enumerate(esl):
        ex = x0 + k * (ew + gap)
        caja(b, ex, yy, ew, eh, c, r=40 if t != "?" else 14, dash="8,6" if t == "?" else None, sw=2.4)
        rot(b, ex + ew / 2, yy + 28, f"ESLABÓN {k + 1}", c, size=13, anchor="middle")
        if t == "?":
            pista(b, ex + ew / 2, yy + 56, "¿qué hace falta para", anchor="middle")
            pista(b, ex + ew / 2, yy + 76, "que haya corriente?", anchor="middle")
            renglon(b, ex + 14, yy + 112, ex + ew - 14)
            renglon(b, ex + 14, yy + 138, ex + ew - 14)
        else:
            txt_izq(b, ex + 16, yy + 44, t, ew - 32, 16)
        if k < n - 1:
            flecha(b, ex + ew + 4, yy + eh / 2, ex + ew + gap - 4, yy + eh / 2, c, sw=2.4, head=10)
    yy += eh + 24
    caja(b, x0, yy, ww, 196, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL DATO QUE DECIDE", c, size=14)
    pista(b, x0 + 230, yy + 30, "un dato sirve si, al salir distinto, tumba un eslabón")
    b.append(T(x0 + 20, yy + 74, ["Si mido ______________________________ y sale cero (no cambia),"], 17, INK))
    b.append(T(x0 + 20, yy + 112, ["se cae el eslabón ______ y la explicación del ingeniero ya no sirve."], 17, INK))
    b.append(T(x0 + 20, yy + 156, ["Un dato que no toca ningún eslabón (aunque sea del tren):"], 17, INK))
    renglon(b, x0 + 480, yy + 160, x0 + ww - 20)
    yy += 212
    return ojo(b, x0, yy, ww, "UN DATO DEL TREN NO ES UN DATO DE LA EXPLICACIÓN",
               "cuánto pesa el tren o qué voltaje usa al arrancar son datos ciertos, pero ¿cambian en algo la "
               "cadena del frenado? Pregúntale a cada opción en qué eslabón se mete.")


# ───────── P3 · freno del tren · la aceleración promedio ─────────
def _tache(b, x, y, w, c):
    """Raya inclinada para tachar una unidad (DEBAJO del texto se dibuja aparte)."""
    b.append(line(x, y + 4, x + w, y - 14, c, 2))


def i3(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La escalera de km/h a m/s", c,
                      "La aceleración se pide en m/s² y los datos vienen en km/h. Sube la escalera escribiendo la "
                      "unidad al lado de cada número y tachando las que se cancelan. Solo al final divides entre "
                      "el tiempo.")
    x0, ww = x + 22, w - 44
    for k, (rt, v) in enumerate((("RAPIDEZ ANTES DE FRENAR", "90"), ("RAPIDEZ AL TERMINAR", "10"))):
        ry = yy + k * 132
        caja(b, x0, ry, ww, 118, c, r=14)
        rot(b, x0 + 20, ry + 28, rt, c, size=14)
        bx = x0 + 20
        by = ry + 52
        partes = ((f"{v} km", "h"), ("1000 m", "1 km"), ("1 h", "3600 s"))
        for j, (num, den) in enumerate(partes):
            fx = bx + j * 250
            b.append(T(fx + 80, by + 20, [num], 20, INK, weight="700", anchor="middle"))
            b.append(line(fx + 10, by + 30, fx + 150, by + 30, INK, 2))
            b.append(T(fx + 80, by + 56, [den], 20, INK, weight="700", anchor="middle"))
            if j < 2:
                b.append(T(fx + 200, by + 40, ["×"], 26, INK, anchor="middle"))
        b.append(T(bx + 690, by + 40, ["="], 26, INK, anchor="middle"))
        caja(b, bx + 730, by + 6, 150, 48, c, r=8)
        b.append(T(bx + 900, by + 40, ["m/s"], 20, INK, weight="700"))
        pista(b, bx + 970, by + 24, "tacha con lápiz")
        pista(b, bx + 970, by + 46, "las unidades que se van")
    yy += 2 * 132 + 4
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 28, "LA ACELERACIÓN", c, size=14)
    b.append(T(x0 + 20, yy + 76, ["a  =  Δv ÷ Δt  =  ( ________  −  ________ ) m/s  ÷  ______ s  ="], 20, INK))
    caja(b, x0 + 760, yy + 44, 160, 48, c, r=8)
    b.append(T(x0 + 936, yy + 76, ["m/s²"], 20, INK, weight="700"))
    b.append(T(x0 + 20, yy + 126, ["El signo me dice que el tren __________ ; la pregunta pide el valor absoluto, sin signo."],
               17, INK))
    yy += 166
    return trampa(b, x0, yy, ww, "Haz la cuenta sin convertir, solo para ver qué pasa:",
                  "(90 − 10) ÷ 6 da un número en (km/h)/s. ¿Aparece entre las opciones? Un número sin su unidad "
                  "puede parecer bueno y estar en otra escala.", c)


# ───────── P4 · sensor en la tormenta · por qué se curvan las líneas ─────────
def i4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El campo del sensor, antes y durante la tormenta", c,
                      "Dibuja tú las líneas de campo alrededor del sensor en los dos momentos, como las describe "
                      "el texto. Después piensa qué tiene que aparecer en el cielo para que unas líneas rectas se "
                      "tuerzan y se amontonen.")
    x0, ww = x + 22, w - 44
    pw = (ww - 30) / 2
    ph = 330
    for k, t in enumerate(("1 · ANTES · LÍNEAS VERTICALES HACIA EL SUELO", "2 · DURANTE · SE CURVAN Y SE APRIETAN")):
        px = x0 + k * (pw + 30)
        caja(b, px, yy, pw, ph, c, r=16)
        rot(b, px + 18, yy + 28, t, c, size=13)
        b.append(rect(px + 16, yy + ph - 56, pw - 32, 40, "#E7DCC8", r=4))
        b.append(T(px + pw / 2, yy + ph - 30, ["suelo"], 15, INK, weight="700", anchor="middle"))
        sx = px + pw / 2
        b.append(rect(sx - 14, yy + ph - 96, 28, 40, "white", r=4, stroke=INK, sw=2))
        b.append(T(sx + 24, yy + ph - 70, ["sensor"], 14, INK))
        if k == 0:
            pista(b, px + 18, yy + 56, "dibuja cinco líneas con su flecha")
        else:
            b.append(f'<path d="M {px + 40} {yy + 92} q 30 -36 70 -8 q 34 -30 70 0 q 40 -10 44 30 q -10 30 -50 24 '
                     f'q -40 22 -90 0 q -48 4 -44 -46 Z" fill="#EEF0F4" stroke="{GRAY}" stroke-width="2"/>')
            pista(b, px + 260, yy + 74, "una nube de tormenta")
            pista(b, px + 260, yy + 96, "se acerca: ¿qué trae?")
    yy += ph + 18
    caja(b, x0, yy, ww, 162, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA REGLA DE LAS LÍNEAS DE CAMPO ELÉCTRICO", c, size=14)
    b.append(T(x0 + 20, yy + 76, ["Las líneas nacen en las cargas __________ y terminan en las cargas __________ ."],
               17, INK))
    b.append(T(x0 + 20, yy + 122, ["Si cambian de forma cerca del sensor, es porque cerca apareció o se movió"], 17, INK))
    renglon(b, x0 + 600, yy + 126, x0 + ww - 20)
    yy += 178
    return ojo(b, x0, yy, ww, "CAMPO ELÉCTRICO NO ES CAMPO MAGNÉTICO",
               "el sensor mide el campo eléctrico. Una opción que hable de otro campo, o que diga que las líneas se "
               "vuelven al azar, ¿está hablando del mismo modelo que usaste en tu dibujo?")


# ───────── P5 · descargadores del avión · qué información evalúa la propuesta ─────────
def _ala(b, x, y, w, c):
    b.append(f'<path d="M {x} {y + 30} L {x + w - 80} {y + 6} L {x + w} {y + 18} L {x + w - 70} {y + 56} '
             f'L {x} {y + 74} Z" fill="#F3F4F7" stroke="{c}" stroke-width="2.6"/>')
    for k in range(3):
        vx = x + w - 150 + k * 50
        b.append(line(vx, y + 56 - k * 4, vx + 34, y + 96 - k * 4, INK, 3))
    pista(b, x + w - 40, y + 130, "descargadores", anchor="end")


def i5(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Qué mide el dato y dónde lo mide", c,
                      "Una propuesta se pone a prueba con un dato de lo MISMO que afirma, en el MISMO lugar del que "
                      "habla. Subraya en tu libro las palabras de la propuesta del técnico y llena las dos fichas.")
    x0, ww = x + 22, w - 44
    aw = 560
    caja(b, x0, yy, aw, 250, c, r=16)
    rot(b, x0 + 18, yy + 28, "EL ALA, VISTA DESDE ARRIBA", c, size=13)
    _ala(b, x0 + 30, yy + 70, aw - 60, INK)
    pista(b, x0 + 18, yy + 232, "marca con una X el lugar del que habla la propuesta")
    fx = x0 + aw + 26
    fw = x0 + ww - fx
    for k, (rt, ps) in enumerate((("¿QUÉ AFIRMA QUE PASA?", "¿qué actúa sobre qué?"),
                                  ("¿DÓNDE PASA?", "¿en qué parte del avión?"))):
        fy = yy + k * 128
        caja(b, fx, fy, fw, 116, c, r=14)
        rot(b, fx + 18, fy + 28, rt, c, size=14)
        pista(b, fx + 290, fy + 28, ps)
        renglon(b, fx + 18, fy + 70, fx + fw - 18)
        renglon(b, fx + 18, fy + 102, fx + fw - 18)
    yy += 270
    caja(b, x0, yy, ww, 120, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL DATO QUE PONE A PRUEBA LA PROPUESTA", c, size=14)
    b.append(T(x0 + 20, yy + 80, ["Hay que medir ____________________________ , justo en ____________________ ."],
               18, INK))
    yy += 136
    return trampa(b, x0, yy, ww, "Una información puede ser del avión y no de la propuesta:",
                  "si un dato habla de otra parte del avión o de otro momento del vuelo (antes del despegue, el "
                  "aterrizaje), compáralo con tus dos fichas: ¿coinciden el qué y el dónde?", c)


# ───────── P6 · dos cargas positivas · qué diagrama del campo ─────────
def i6(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Tres reglas para revisar un dibujo de campo", c,
                      "Antes de mirar los cuatro diagramas, dibuja tú el campo de dos cargas positivas iguales. "
                      "Después pasa cada diagrama del libro por las tres reglas, una por una.")
    x0, ww = x + 22, w - 44
    dw = 470
    caja(b, x0, yy, dw, 300, c, r=16)
    rot(b, x0 + 18, yy + 28, "MI DIBUJO", c, size=13)
    carga(b, x0 + 140, yy + 170, "+")
    carga(b, x0 + dw - 140, yy + 170, "+")
    pista(b, x0 + dw / 2, yy + 276, "dibuja al menos seis líneas con flecha", anchor="middle")
    rx = x0 + dw + 24
    rw = x0 + ww - rx
    reglas = ("1 · Hay dos cargas y las dos son positivas.",
              "2 · En el medio, las líneas se apartan: no van de una carga a la otra.",
              "3 · Las flechas apuntan hacia afuera de cada carga positiva.")
    cols = (("", rw - 4 * 92),) + tuple((L, 92) for L in "ABCD")
    caja(b, rx, yy, cols[0][1], 46, c, r=0, fill=A["bg"])
    rot(b, rx + 14, yy + 30, "LA REGLA", c, size=13)
    px = rx + cols[0][1]
    for L, cw in cols[1:]:
        caja(b, px, yy, cw, 46, c, r=0, fill=A["bg"])
        letra(b, px + cw / 2, yy + 23, L, c, r=15, size=15)
        px += cw
    for k, rg in enumerate(reglas):
        ry = yy + 46 + k * 84
        caja(b, rx, ry, cols[0][1], 84, c, r=0)
        txt_izq(b, rx + 14, ry + 14, rg, cols[0][1] - 28, 16, lh=22)
        px = rx + cols[0][1]
        for L, cw in cols[1:]:
            caja(b, px, ry, cw, 84, c, r=0)
            casillas(b, px + 14, ry + 18, ("sí",), c, paso=0, size=15)
            casillas(b, px + 14, ry + 50, ("no",), c, paso=0, size=15)
            px += cw
    yy += 46 + 3 * 84 + 18
    yy = max(yy, yy)
    yy = frase_hueco(b, x0, yy, ww, "El diagrama que pasa más reglas es el ____ ; la regla que no cumple del todo: ____ .",
                     c)
    return alto_profe(b, x0, yy + 16, ww,
                      "Si ningún diagrama pasa las tres reglas, no es que estés mal: pregúntale al profe por las "
                      "flechas de los diagramas del libro y cuál escoger cuando una figura tiene un error.")


# ───────── P7 · carga de prueba · el vector fuerza ─────────
def i7(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "La flecha del campo y la flecha de la fuerza", c,
                      "Un vector tiene tamaño, unidad y sentido. Haz la cuenta con las unidades completas (el libro "
                      "no las escribe: ponlas tú) y dibuja la fuerza en el mismo punto donde está el campo.")
    x0, ww = x + 22, w - 44
    dw = 520
    caja(b, x0, yy, dw, 270, c, r=16)
    rot(b, x0 + 18, yy + 28, "EL PUNTO DONDE ESTÁ LA CARGA", c, size=13)
    cx, cy = x0 + dw / 2, yy + 120
    flecha(b, cx, cy, cx - 170, cy, INK, sw=3, head=14)
    b.append(T(cx - 150, cy - 16, ["E = 400 N/C"], 16, INK, weight="700"))
    carga(b, cx, cy, "+", r=16)
    pista(b, cx, cy + 60, "dibuja aquí la flecha de la fuerza F", anchor="middle")
    pista(b, cx, cy + 82, "(que salga de la carga)", anchor="middle")
    b.append(line(x0 + 30, yy + 236, x0 + dw - 30, yy + 236, GRAY, 1.6, dash="5,5"))
    b.append(T(x0 + 30, yy + 258, ["← izquierda"], 14, GRAY))
    b.append(T(x0 + dw - 30, yy + 258, ["derecha →"], 14, GRAY, anchor="end"))
    rx = x0 + dw + 24
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 270, c, r=16)
    rot(b, rx + 18, yy + 28, "LA CUENTA, CON UNIDADES", c, size=13)
    b.append(T(rx + 18, yy + 76, ["F  =  q · E"], 22, INK, weight="700"))
    b.append(T(rx + 18, yy + 124, ["F  =  ( ____________ C ) · ( ________ N/C )"], 19, INK))
    b.append(T(rx + 18, yy + 172, ["F  =  ____________  ·  ( C · N/C )  =  ____________ N"], 19, INK))
    pista(b, rx + 18, yy + 214, "C por N/C: ¿qué unidad queda cuando se cancelan los coulomb?")
    pista(b, rx + 18, yy + 240, "pista para la potencia: 2 × 4 = 8 y 10⁻⁶ × 10² = 10 elevado a ____")
    yy += 288
    caja(b, x0, yy, ww, 120, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL SENTIDO LO DECIDE EL SIGNO", c, size=14)
    b.append(T(x0 + 20, yy + 72, ["Carga positiva: la fuerza va __________________ que el campo."], 18, INK))
    b.append(T(x0 + 20, yy + 104, ["Si la carga fuera negativa, la fuerza iría __________________ ."], 18, INK))
    yy += 136
    return ojo(b, x0, yy, ww, "¿ES UN DATO O ES UN RESULTADO?",
               "si una opción trae un número que ya estaba en el enunciado, pregúntate qué es ese número: ¿la "
               "carga, el campo o la fuerza? La fuerza sale de tu cuenta.")


# ───────── P8 · desmagnetización · qué información comprueba la idea ─────────
def i8(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Si la idea es cierta, ¿qué tendría que pasar?", c,
                      "Una explicación se comprueba con una predicción: «si es cierta, entonces debería…». Completa "
                      "la idea del estudiante con lo que dice el modelo, escribe las dos predicciones y busca el "
                      "dato que te dice en cuál de las dos estás.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 106, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA IDEA", c, size=14)
    b.append(T(x0 + 20, yy + 72, ["El calor desordena los dominios magnéticos cuando la aguja pasa de una temperatura"],
               17, INK))
    b.append(T(x0 + 20, yy + 96, ["llamada ________________________ ."], 17, INK))
    yy += 124
    pw = (ww - 24) / 2
    for k, (rt, cond) in enumerate((("PREDICCIÓN 1", "Si la aguja NO llega a esa temperatura…"),
                                    ("PREDICCIÓN 2", "Si la aguja SÍ la supera…"))):
        px = x0 + k * (pw + 24)
        caja(b, px, yy, pw, 190, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        b.append(T(px + 18, yy + 66, [cond], 17, INK, weight="700"))
        pista(b, px + 18, yy + 94, "…entonces la aguja")
        renglon(b, px + 18, yy + 136, px + pw - 18)
        renglon(b, px + 18, yy + 172, px + pw - 18)
    yy += 208
    yy = frase_hueco(b, x0, yy, ww, "Para saber en cuál predicción estoy, necesito medir ______________________ .", c)
    return trampa(b, x0, yy + 16, ww, "Un dato del experimento no siempre sirve para esta idea:",
                  "la idea habla de temperatura y de dominios. Si un dato habla del imán o del tiempo que las agujas "
                  "estuvieron pegadas, ¿te dice en qué predicción estás?", c)


# ───────── P9 · acero y níquel · cuál pierde primero el magnetismo ─────────
def i9(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Dos metas en el mismo termómetro", c,
                      "Las dos agujas se calientan con la misma llama, al mismo tiempo: su temperatura sube parejo. "
                      "Marca en el termómetro la meta de cada metal (su temperatura de Curie) y piensa cuál llega "
                      "primero a la suya.")
    x0, ww = x + 22, w - 44
    tx, ty, th = x0 + 90, yy + 30, 360
    b.append(rect(tx, ty, 44, th, "white", r=22, stroke=INK, sw=2.6))
    b.append(f'<circle cx="{tx + 22}" cy="{ty + th + 26}" r="34" fill="#F3D6CF" stroke="{INK}" stroke-width="2.6"/>')
    for v in range(0, 801, 100):
        py = ty + th - 10 - v / 800 * (th - 30)
        b.append(line(tx + 44, py, tx + 62, py, INK, 2))
        b.append(T(tx + 70, py + 5, [f"{v} °C"], 14, GRAY))
    pista(b, tx + 140, ty + 120, "dibuja una raya")
    pista(b, tx + 140, ty + 142, "en cada meta y")
    pista(b, tx + 140, ty + 164, "escribe el metal")
    rx = x0 + 380
    rw = x0 + ww - rx
    caja(b, rx, yy, rw, 150, c, r=14)
    rot(b, rx + 18, yy + 28, "LA CARRERA", c, size=14)
    b.append(T(rx + 18, yy + 70, ["Meta del acero: ________ °C       Meta del níquel: ________ °C"], 17, INK))
    b.append(T(rx + 18, yy + 116, ["Como suben parejo, el que tiene la meta más ________ llega primero."], 17, INK))
    caja(b, rx, yy + 166, rw, 150, c, r=14)
    rot(b, rx + 18, yy + 194, "MODELO → MECANISMO", c, size=14)
    b.append(T(rx + 18, yy + 236, ["Al pasar su meta, los dominios de esa aguja se ____________ ,"], 17, INK))
    b.append(T(rx + 18, yy + 278, ["por eso deja de ser atraída y ____________ ."], 17, INK))
    yy += 460
    return trampa(b, x0, yy, ww, "Revisa de dónde sale la razón de cada opción:",
                  "el texto da dos temperaturas y dice que la fuente y el tiempo son iguales. Una razón que use una "
                  "propiedad que el texto no da, ¿la sacaste de los datos o la estás suponiendo?", c)


# ───────── P10 · agujas imantadas · la explicación según el modelo ─────────
def _aguja(b, x, y, w, c, flechas):
    b.append(f'<path d="M {x} {y} L {x + w - 40} {y - 22} L {x + w} {y} L {x + w - 40} {y + 22} Z" fill="white" '
             f'stroke="{INK}" stroke-width="2.4"/>')
    n = 6
    cw = (w - 60) / n
    for k in range(n):
        bx = x + 14 + k * cw
        b.append(rect(bx, y - 14, cw - 8, 28, "white", r=3, stroke=c, sw=1.6))
        if flechas:
            flecha(b, bx + 8, y, bx + cw - 16, y, c, sw=2, head=6)


def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Los dominios, antes y después de la llama", c,
                      "Cada cuadrito de la aguja es un dominio: una región donde los imanes atómicos apuntan igual. "
                      "Antes de la llama ya están dibujados. Dibuja tú cómo quedan después y explica qué les hizo el "
                      "calor a los átomos.")
    x0, ww = x + 22, w - 44
    pw = (ww - 30) / 2
    for k, (t, fl) in enumerate((("1 · ANTES · LA AGUJA SE PEGA AL IMÁN", True),
                                 ("2 · DESPUÉS DE CALENTAR LA PUNTA", False))):
        px = x0 + k * (pw + 30)
        caja(b, px, yy, pw, 190, c, r=16)
        rot(b, px + 18, yy + 28, t, c, size=13)
        _aguja(b, px + 40, yy + 104, pw - 80, c, fl)
        pista(b, px + 18, yy + 170, "los dominios apuntan igual" if fl else "dibuja una flecha en cada dominio")
    yy += 208
    caja(b, x0, yy, ww, 196, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA CADENA DEL MODELO", c, size=14)
    pasos = ("el calor le da a los átomos más…", "eso hace que los dominios…", "y al pasar de la temperatura de…")
    for k, p in enumerate(pasos):
        py = yy + 72 + k * 44
        b.append(T(x0 + 20, py, [p], 17, INK))
        renglon(b, x0 + 320, py + 4, x0 + ww - 20)
    yy += 212
    return trampa(b, x0, yy, ww, "La explicación tiene que hablar de lo que se calentó:",
                  "la llama tocó la punta de las agujas, no el imán. Si una opción explica con lo que le pasa al imán, "
                  "o con algo que nadie observó en la aguja, ¿cuadra con tu dibujo de los dominios?", c)


Q = {1: dict(n=1, est=4, pag=226, ctx="Imán y bobina con galvanómetro · ¿es correcta la explicación?",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=1, pag=226, ctx="Freno electromagnético del tren · qué dato evalúa la explicación",
             comp="Indagación", inst=i2),
     3: dict(n=3, est=3, pag=226, ctx="Freno electromagnético del tren · la aceleración promedio",
             comp="Uso comprensivo del conocimiento científico", inst=i3),
     4: dict(n=4, est=2, pag=227, ctx="Sensor de campo eléctrico en la tormenta · por qué se curvan las líneas",
             comp="Explicación de fenómenos", inst=i4),
     5: dict(n=5, est=1, pag=227, ctx="Descargadores estáticos del avión · qué información evalúa la propuesta",
             comp="Indagación", inst=i5),
     6: dict(n=6, est=2, pag=227, ctx="Dos cargas positivas idénticas · qué diagrama del campo",
             comp="Uso comprensivo del conocimiento científico", inst=i6),
     7: dict(n=7, est=3, pag=227, ctx="Carga de prueba en la maqueta del ala · el vector de la fuerza",
             comp="Uso comprensivo del conocimiento científico", inst=i7),
     8: dict(n=8, est=1, pag=228, ctx="Agujas imantadas y la llama · qué información comprueba la idea",
             comp="Indagación", inst=i8),
     9: dict(n=9, est=4, pag=228, ctx="Agujas de acero y de níquel · cuál pierde primero el magnetismo",
             comp="Explicación de fenómenos", inst=i9),
     10: dict(n=10, est=4, pag=228, ctx="Agujas imantadas · la explicación según el modelo del magnetismo",
              comp="Explicación de fenómenos", inst=i10)}


def build(pages=(240, 241, 243, 244, 245)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"fis3_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
