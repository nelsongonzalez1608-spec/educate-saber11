#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 2 · componente biológico-organísmico · páginas 147–153.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 2» de Biología, páginas 83–85 (componente biológico –
organísmico). Casos: un paciente sin ADH (1), correr al sol y quedarse en una sala fría (2), el
calcio en sangre (3), las ranas Litoria y la estivación (4 a 6), la tabla de tres especies (7 y 8),
la glucosa después de comer (9) y el páncreas artificial (10).

Claves verificadas (resueltas a mano contra el texto y la tabla del libro, 7 nov 2026):

    1·C  2·A  3·C  4·D  5·A  6·C  7·B  8·A  9·A  10·D

Cuentas: 7 → agua eliminada: rana 5, camello 15, rata 50 mL/h; glucosa: rana 80, camello 95,
         rata 120 mg/dL. La rana es la menor en las dos columnas; en temperatura (33 °C) no es la
         mayor (camello 42 °C). 8 → rata 50 / camello 15 ≈ 3,3 veces más agua eliminada.
Reparto: A 4 · B 1 · C 3 · D 2. Hallazgos (la 2 no tiene una opción que explique los dos casos;
la 10 dice «hipoglucemias» donde va «hiperglucemias»; «primero» contra «gradualmente» en la 5;
la 7 se infiere, no se lee): en tablero/propuestas/bio2_hallazgos.csv.

Estrategias:
    1 · El circuito que vuelve al equilibrio     (1, 3, 9  · ICFES 2a-62)   azul
    2 · La función sale del texto                (4, 5, 6  · ICFES 1a-102)  rojo
    3 · Dato contra dato, especie contra especie (7, 8     · ICFES 1a-103)  oro
    4 · Lo que alcanza a explicar                (2, 10    · ICFES 1a-108)  morado

Hojas: 147 bio2_t1 (1-2) · 148 bio2_t2 (3-4) · 149 bio2_i1 · 150 bio2_t3 (5-6) ·
       151 bio2_t4 (7-8) · 152 bio2_t5 (9-10) · 153 bio2_i2.
"""
from taller_base import *

configurar("Biología", 2, "biológico · organísmico",
           tema="El equilibrio de adentro: un cuerpo que se regula", nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("El circuito que vuelve al equilibrio", EDU_AZUL),
       2: ("La función sale del texto", EDU_ROJO),
       3: ("Dato contra dato, especie contra especie", EDU_ORO),
       4: ("Lo que alcanza a explicar", MORADO)}
usar_estrategias(EST)
AZ, RO, OR, MO = (EST[k][1] for k in (1, 2, 3, 4))
TINTE = "#EEF7EF"


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def frase_hueco(b, x, y, w, texto, c, h=56):
    caja(b, x, y, w, h, c)
    b.append(T(x + 24, y + h / 2 + 7, [texto], 18, INK, weight="700"))
    return y + h


def ficha(b, cx, cy, txt, c, r=16, size=16):
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="white" stroke="{c}" stroke-width="2.2"/>')
    b.append(T(cx, cy + size * 0.38, [txt], size, c, weight="700", anchor="middle"))


def flecha(b, x1, y1, x2, y2, c, sw=2.6, bend=0.0, head=13):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def dos_casillas(b, x, y, labs, c, paso=110, size=16):
    for j, lab in enumerate(labs):
        b.append(checkbox(x + j * paso, y - 16, s=11, c=c))
        b.append(T(x + 30 + j * paso, y + 2, [lab], size, GRAY))


# ───────── P1 · sin ADH · el riñón ─────────
def _tubulo(b, x, y, w, c, bloqueado):
    """Túbulo renal esquemático: el agua sale hacia la sangre por tres flechitas (o no sale)."""
    b.append(rect(x, y + 34, w, 34, "#F6FBFF", r=17, stroke=c, sw=2.2))
    b.append(rect(x, y - 4, w, 22, "#FBEDED", r=11, stroke=EDU_ROJO, sw=1.8))
    b.append(T(x + w + 10, y + 12, ["sangre"], 14, GRAY, style="italic"))
    b.append(T(x + w + 10, y + 58, ["túbulo"], 14, GRAY, style="italic"))
    for k in range(3):
        ax = x + 60 + k * (w - 120) / 2
        b.append(f'<line x1="{ax}" y1="{y + 32}" x2="{ax}" y2="{y + 22}" stroke="{c}" stroke-width="2.4"/>')
        b.append(f'<polygon points="{ax - 6},{y + 24} {ax + 6},{y + 24} {ax},{y + 16}" fill="{c}"/>')
        if bloqueado:
            b.append(f'<line x1="{ax - 10}" y1="{y + 14}" x2="{ax + 10}" y2="{y + 34}" stroke="{INK}" stroke-width="2.4"/>')
            b.append(f'<line x1="{ax + 10}" y1="{y + 14}" x2="{ax - 10}" y2="{y + 34}" stroke="{INK}" stroke-width="2.4"/>')


def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El riñón sin la orden de guardar agua", c,
                      "La ADH es la orden que le dice al riñón: «devuelve agua a la sangre». Llena la fila de una "
                      "persona sana y la del paciente, y sigue el agua hasta el resto del cuerpo.")
    x0, ww = x + 22, w - 44
    tw_ = 300
    for k, (quien, bloq) in enumerate((("CON ADH · PERSONA SANA", False), ("SIN ADH · EL PACIENTE", True))):
        ry = yy + k * 196
        caja(b, x0, ry, ww, 180, c, r=16)
        rot(b, x0 + 20, ry + 30, quien, c, size=14)
        _tubulo(b, x0 + 20, ry + 64, tw_, c, bloq)
        cx = x0 + tw_ + 110
        pista(b, cx, ry + 44, "agua que vuelve a la sangre:")
        dos_casillas(b, cx + 214, ry + 44, ("mucha", "poca"), c, paso=100)
        pista(b, cx, ry + 92, "cantidad de orina:")
        dos_casillas(b, cx + 214, ry + 92, ("más", "menos"), c, paso=100)
        pista(b, cx, ry + 140, "líquido que queda en el cuerpo:")
        dos_casillas(b, cx + 214, ry + 140, ("más", "menos"), c, paso=100)
        pista(b, x0 + 20, ry + 162, "(cuadro del libro: la «X» = no hay reabsorción)" if bloq else "", size=13)
    yy += 2 * 196
    yy = frase_hueco(b, x0, yy, ww, "Efecto directo en el paciente: ________________________________ .", c)
    return trampa(b, x0, yy + 14, ww, "Una opción dice que el cuerpo «intentaría compensar»:",
                  "¿con qué? La hormona que guarda agua es justo la que falta. Compara esa opción con tu fila del "
                  "paciente antes de creerle.", c)


# ───────── P2 · al sol y al frío ─────────
def i2(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Al sol y al frío: lo que hace cada cuerpo", c,
                      "Una hipótesis que «explica la diferencia» tiene que poder hablar de las dos personas sin "
                      "contradecir el enunciado. Primero llena lo que le pasa a cada una; después pon a prueba "
                      "las cuatro opciones.")
    x0, ww = x + 22, w - 44
    lw = 300
    half = (ww - lw - 20) / 2
    for k, quien in enumerate(("CORRE 10 KM AL SOL", "SE QUEDA EN LA SALA FRÍA")):
        rot(b, x0 + lw + 20 + k * half + 14, yy + 20, quien, c, size=13)
    yy += 32
    filas = (("su temperatura tiende a", ("subir", "bajar")), ("el cuerpo responde con", None),
             ("lo que pierde o gasta", None))
    for k, (lab, ops) in enumerate(filas):
        ry = yy + k * 70
        caja(b, x0, ry, ww, 60, c, r=10)
        b.append(T(x0 + 18, ry + 38, [lab], 17, INK))
        for j in range(2):
            cx = x0 + lw + 20 + j * half + 14
            if ops:
                dos_casillas(b, cx, ry + 38, ops, c, paso=110)
            else:
                renglon(b, cx, ry + 46, cx + half - 30)
    yy += 3 * 70 + 16
    # la prueba de las cuatro opciones
    rot(b, x0, yy + 18, "LA PRUEBA DE CADA OPCIÓN", c, size=14)
    cols = ("habla del corredor", "habla de la sala fría", "contradice el enunciado o mi tabla")
    xs = (x0 + 330, x0 + 580, x0 + 830)
    for k, cl in enumerate(cols):
        pista(b, xs[k], yy + 18, cl, size=14)
    yy += 30
    for k, L in enumerate("ABCD"):
        ry = yy + k * 46
        ficha(b, x0 + 30, ry + 20, L, c, r=15, size=15)
        for xx in xs:
            b.append(checkbox(xx, ry + 9, s=11, c=c))
    yy += 4 * 46 + 6
    return ojo(b, x0, yy, ww, "NINGUNA OPCIÓN HABLA BIEN DE LAS DOS PERSONAS",
               "Es un problema de la pregunta, no tuyo. Cuando pase, quédate con la opción que es cierta en la "
               "fisiología y no contradice el enunciado, y anota en «lo que me llevo» qué le faltó.")


# ───────── P3 · calcio · el circuito ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La vuelta completa del calcio", c,
                      "Todo equilibrio es una vuelta: algo cambia, el cuerpo lo nota, responde y la variable vuelve "
                      "a su sitio. Llena la vuelta del calcio. La respuesta correcta es la que cierra el círculo.")
    x0, ww = x + 22, w - 44
    cx, cy = x0 + ww / 2, yy + 230
    b.append(f'<ellipse cx="{cx}" cy="{cy}" rx="250" ry="150" fill="none" stroke="{c}" stroke-width="2.4" '
             f'stroke-dasharray="10,8"/>')
    for (a1, a2) in ((200, 250), (290, 340), (20, 70), (110, 160)):
        ang = math.radians(a2)
        px, py = cx + 250 * math.cos(ang), cy + 150 * math.sin(ang)
        ang0 = math.radians(a2 - 8)
        qx, qy = cx + 250 * math.cos(ang0), cy + 150 * math.sin(ang0)
        b.append(hand_arrow(qx, qy, px, py, c, sw=3, bend=0.0, head=16))
    bw_, bh_ = 400, 128
    nodos = ((x0, yy, "1 · LO QUE CAMBIÓ", "el calcio en la sangre…", ("sube", "baja")),
             (x0 + ww - bw_, yy, "2 · DÓNDE HAY RESERVA", "el cuerpo guarda mucho calcio en…", None),
             (x0 + ww - bw_, yy + 332, "3 · QUÉ LO MUEVE", "un nervio, una hormona, el intestino…", None),
             (x0, yy + 332, "4 · CÓMO QUEDA AL FINAL", "el calcio en la sangre…", ("sube", "baja")))
    for nx, ny, rt, ps, ops in nodos:
        caja(b, nx, ny, bw_, bh_, c, r=16)
        rot(b, nx + 18, ny + 30, rt, c, size=14)
        pista(b, nx + 18, ny + 58, ps, size=15)
        if ops:
            dos_casillas(b, nx + 18, ny + 106, ops, c)
        else:
            renglon(b, nx + 18, ny + 106, nx + bw_ - 18)
    b.append(T(cx, cy + 6, ["EQUILIBRIO"], 18, c, weight="700", ls=2, anchor="middle"))
    yy += 332 + bh_ + 16
    return ojo(b, x0, yy, ww, "PRUEBA CADA OPCIÓN EN LA CASILLA 4",
               "Si con lo que dice la opción el calcio en la sangre baja todavía más, esa opción no regula nada: "
               "empeora lo que ya estaba mal.")


# ───────── P4 · urea · la función con las palabras del texto ─────────
def i4(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La función, con las palabras exactas del texto", c,
                      "La pregunta dice «según el texto»: la respuesta está escrita en el párrafo. Encuentra la "
                      "frase, cópiala y luego dila con tus palabras en seis palabras, una por casilla.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 150, c, r=14)
    rot(b, x0 + 20, yy + 30, "LA FRASE DEL TEXTO QUE DICE QUÉ HACE LA UREA", c, size=14)
    pista(b, x0 + 20, yy + 56, "cópiala completa, sin cambiarle nada", size=14)
    renglon(b, x0 + 20, yy + 96, x0 + ww - 20)
    renglon(b, x0 + 20, yy + 136, x0 + ww - 20)
    yy += 166
    rot(b, x0, yy + 20, "CON MIS PALABRAS, EN SEIS", c, size=14)
    yy += 34
    cw_ = (ww - 5 * 14) / 6
    for k in range(6):
        caja(b, x0 + k * (cw_ + 14), yy, cw_, 60, c, r=10)
    yy += 76
    yy = ojo(b, x0, yy, ww, "UNA PALABRA QUE YA CONOCES: «OSMÓTICO»",
             "Tiene que ver con el paso del agua a través de las membranas, como la sal y la raíz de la misión 1. "
             "Si la urea es un regulador osmótico, ¿qué hace con el agua de la rana: la deja salir o la retiene?")
    return trampa(b, x0, yy + 14, ww, "Encierra en cada opción las palabras que están en tu frase:",
                  "una opción que no comparte ninguna idea con la frase copiada no sale del texto, aunque suene a "
                  "biología.", c)


# ───────── P5 · la rana que despierta ─────────
def i5(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La rana que despierta, paso por paso", c,
                      "Cuando vuelven la humedad y el fresco, el texto cuenta lo que pasa en un orden. Copia cada "
                      "paso en su parada. La variable que «se modifica primero» tiene que estar en la primera.")
    x0, ww = x + 22, w - 44
    n, gap = 3, 50
    pw = (ww - gap * (n - 1)) / n
    paradas = (("1 · LO QUE EL TEXTO CUENTA PRIMERO", "qué cambia y cómo cambia"),
               ("2 · LO QUE VIENE DESPUÉS", "con las palabras del texto"),
               ("3 · LO QUE VIENE AL FINAL", "con las palabras del texto"))
    for k, (rt, ps) in enumerate(paradas):
        px = x0 + k * (pw + gap)
        caja(b, px, yy, pw, 190, c, r=16)
        rot(b, px + 18, yy + 30, rt, c, size=13)
        pista(b, px + 18, yy + 56, ps, size=14)
        renglon(b, px + 18, yy + 100, px + pw - 18)
        renglon(b, px + 18, yy + 140, px + pw - 18)
        renglon(b, px + 18, yy + 176, px + pw - 18)
        if k < n - 1:
            flecha(b, px + pw + 6, yy + 95, px + pw + gap - 6, yy + 95, c, sw=3, head=14)
    yy += 206
    caja(b, x0, yy, ww, 100, c, r=14)
    rot(b, x0 + 20, yy + 30, "¿LO DICE EL TEXTO?", c, size=14)
    pista(b, x0 + 20, yy + 66, "De las cuatro variables de las opciones, el texto conecta con la humedad solo")
    renglon(b, x0 + 600, yy + 68, x0 + ww - 20)
    pista(b, x0 + 20, yy + 90, "(escribe cuál o cuáles; las que no están en el texto, táchalas en el libro)", size=13)
    yy += 116
    return ojo(b, x0, yy, ww, "«PRIMERO» Y «GRADUALMENTE»",
               "El texto dice que ese cambio ocurre «gradualmente», y la pregunta pide lo que se modifica «primero». "
               "No se contradicen: algo puede empezar primero y tardar en terminar. Fíjate en cuál empieza.")


# ───────── P6 · estivación como estrategia evolutiva ─────────
def i6(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Las dos preguntas que le hace la evolución a la rana", c,
                      "Para la evolución, un rasgo es eficiente si responde bien a dos preguntas. Contesta las dos "
                      "con lo que dice el texto, no con lo que sabes de otras ranas.")
    x0, ww = x + 22, w - 44
    yy = alto_profe(b, x0, yy, ww,
                    "Estrategia evolutiva: un rasgo que hace que los individuos que lo tienen sobrevivan más y dejen "
                    "más descendencia en su ambiente. Por eso se mantiene de generación en generación.") + 18
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("¿LE AYUDA A SOBREVIVIR?", "cómo, según el texto"),
                                  ("¿LE AYUDA A REPRODUCIRSE?", "cómo, según el texto"))):
        bx = x0 + k * (half + 24)
        caja(b, bx, yy, half, 196, c, r=16)
        rot(b, bx + 20, yy + 30, rt, c, size=14)
        dos_casillas(b, bx + 20 + tw(rt, 14, "700") + len(rt) * 1.5 + 20, yy + 32, ("sí", "no"), c, paso=80)
        pista(b, bx + 20, yy + 64, ps, size=14)
        renglon(b, bx + 20, yy + 108, bx + half - 20)
        renglon(b, bx + 20, yy + 148, bx + half - 20)
        renglon(b, bx + 20, yy + 184, bx + half - 20)
    yy += 212
    return frase_hueco(b, x0, yy, ww, "Su ambiente cambia de ____________ a ____________ ; la estivación le sirve "
                                      "para ____________ .", c)


# ───────── P7 · la tabla de tres especies ─────────
ESPECIES = ("camello", "rata", "rana")


def i7(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Ordena la tabla columna por columna", c,
                      "No mires las opciones todavía. Ordena las tres especies de menor a mayor en cada columna de "
                      "la tabla. Después busca en qué columnas la rana queda en el mismo puesto que en el agua "
                      "eliminada.")
    x0, ww = x + 22, w - 44
    cols = ("TEMPERATURA AMBIENTE", "GLUCOSA EN SANGRE", "AGUA ELIMINADA")
    cw_ = (ww - 2 * 24) / 3
    for k, cl in enumerate(cols):
        cx = x0 + k * (cw_ + 24)
        caja(b, cx, yy, cw_, 250, c, r=16, dash="8,6" if k == 2 else None)
        rot(b, cx + 18, yy + 30, cl, c, size=13)
        for j, lab in enumerate(("menor", "en medio", "mayor")):
            ry = yy + 56 + j * 62
            pista(b, cx + 18, ry + 28, lab, size=14)
            caja(b, cx + 110, ry, cw_ - 128, 44, c, r=8)
    yy += 266
    caja(b, x0, yy, ww, 148, c, r=14)
    rot(b, x0 + 20, yy + 30, "LO QUE VA JUNTO CON EL AGUA ELIMINADA", c, size=14)
    pista(b, x0 + 20, yy + 68, "La rana queda en el mismo puesto en las columnas:")
    renglon(b, x0 + 380, yy + 70, x0 + ww - 20)
    pista(b, x0 + 20, yy + 112, "Poca glucosa en la sangre y poca orina pueden indicar que el cuerpo")
    renglon(b, x0 + 520, yy + 114, x0 + ww - 20)
    pista(b, x0 + 20, yy + 138, "(pista en el texto de las preguntas 4 a 6: ¿qué le pasa al metabolismo en la estivación?)",
          size=13)
    yy += 164
    return trampa(b, x0, yy, ww, "Una opción culpa a la temperatura:",
                  "mira tu primera columna. Si la rana no es la que está en el lugar más caliente, el calor no "
                  "puede explicar que ella sea la que menos agua elimina.", c)


# ───────── P8 · el camello ─────────
def i8(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Por dónde se le escapa el agua al camello", c,
                      "Un animal pierde agua por tres salidas. Para cada una, escribe qué tendría que hacer el camello "
                      "para cerrarla y si ese mecanismo existe de verdad en el cuerpo de un mamífero.")
    x0, ww = x + 22, w - 44
    caja(b, x0, yy, ww, 110, c, r=14)
    rot(b, x0 + 20, yy + 30, "PRIMERO, LOS DATOS", c, size=14)
    pista(b, x0 + 20, yy + 72, "camello:")
    caja(b, x0 + 90, yy + 46, 80, 40, c, r=8)
    pista(b, x0 + 180, yy + 72, "mL/h a 42 °C     rata:")
    caja(b, x0 + 350, yy + 46, 80, 40, c, r=8)
    pista(b, x0 + 440, yy + 72, "mL/h a 25 °C     la rata elimina")
    caja(b, x0 + 680, yy + 46, 80, 40, c, r=8)
    pista(b, x0 + 770, yy + 72, "veces lo del camello, con menos calor")
    yy += 126
    salidas = (("POR LA ORINA", "el riñón"), ("POR EL SUDOR", "la piel"), ("POR LA RESPIRACIÓN", "los pulmones"))
    sw_ = (ww - 2 * 24) / 3
    for k, (rt, org) in enumerate(salidas):
        sx = x0 + k * (sw_ + 24)
        caja(b, sx, yy, sw_, 250, c, r=16)
        # gota
        gx, gy = sx + sw_ - 40, yy + 30
        b.append(f'<path d="M {gx} {gy - 16} Q {gx + 14} {gy + 2} {gx} {gy + 14} Q {gx - 14} {gy + 2} {gx} {gy - 16} Z" '
                 f'fill="{c}" fill-opacity="0.35" stroke="{c}" stroke-width="1.6"/>')
        rot(b, sx + 18, yy + 30, rt, c, size=13)
        pista(b, sx + 18, yy + 54, f"órgano: {org}", size=14)
        pista(b, sx + 18, yy + 90, "para cerrarla tendría que…", size=14)
        renglon(b, sx + 18, yy + 128, sx + sw_ - 18)
        renglon(b, sx + 18, yy + 164, sx + sw_ - 18)
        pista(b, sx + 18, yy + 204, "¿eso existe y ahorra agua?", size=14)
        dos_casillas(b, sx + 18, yy + 236, ("sí", "no"), c, paso=80)
    yy += 266
    return ojo(b, x0, yy, ww, "UNA HIPÓTESIS FISIOLÓGICA SE PUEDE COMPROBAR",
               "Tiene que nombrar un órgano y un mecanismo que existan. Si una opción inventa una sustancia o un "
               "proceso que el cuerpo no tiene, no es hipótesis: es fantasía con palabras de biología.")


# ───────── P9 · glucosa después de comer ─────────
def i9(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El medidor de glucosa después del almuerzo", c,
                      "En el medidor está marcada la franja normal. Dibuja la flecha de lo que hace la glucosa al "
                      "comer y la flecha de vuelta. Después escribe quién da la orden de volver y a dónde se va la "
                      "glucosa que sobra en la sangre.")
    x0, ww = x + 22, w - 44
    mx, mw, mh = x0 + 40, 90, 400
    caja(b, mx, yy, mw, mh, c, r=40)
    b.append(rect(mx + 2, yy + 160, mw - 4, 80, "#E3EDF8", r=0))
    b.append(T(mx + mw + 16, yy + 206, ["franja normal"], 15, GRAY, style="italic"))
    b.append(T(mx + mw + 16, yy + 30, ["alto"], 15, GRAY, style="italic"))
    b.append(T(mx + mw + 16, yy + mh - 14, ["bajo"], 15, GRAY, style="italic"))
    rx = x0 + 300
    rw = x0 + ww - rx
    pasos = (("AL COMER CARBOHIDRATOS", "la glucosa en sangre…", ("sube", "baja")),
             ("LA ORDEN DE VOLVER", "la hormona y el órgano que la libera", None),
             ("A DÓNDE SE VA LA GLUCOSA QUE SOBRA", "sale de la sangre y entra en…", None))
    for k, (rt, ps, ops) in enumerate(pasos):
        ry = yy + k * 136
        caja(b, rx, ry, rw, 122, c, r=14)
        ficha(b, rx + 30, ry + 32, str(k + 1), c, r=15, size=15)
        rot(b, rx + 56, ry + 38, rt, c, size=14)
        pista(b, rx + 56, ry + 66, ps, size=14)
        if ops:
            dos_casillas(b, rx + 56, ry + 106, ops, c)
        else:
            renglon(b, rx + 56, ry + 104, rx + rw - 20)
    yy += 3 * 136 + 14
    return trampa(b, x0, yy, ww, "Una respuesta que regula baja lo que está alto:",
                  "si una opción mete más glucosa a la sangre cuando ya sobra, no regula: empeora. Revisa con tu "
                  "flecha de vuelta.", c)


# ───────── P10 · páncreas artificial ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Lo que hace el aparato y lo que no hace", c,
                      "El páncreas natural tiene varios oficios. Para cada uno, marca si el dispositivo lo hace "
                      "según el texto. La conclusión «adecuada» es la que no promete más de lo que marcaste.")
    x0, ww = x + 22, w - 44
    ofi = (("liberar insulina cuando la glucosa sube", "endocrino"), ("liberar glucagón", "endocrino"),
           ("liberar somatostatina", "endocrino"), ("enzimas para la digestión", "exocrino"))
    rot(b, x0 + 720, yy + 18, "¿EL DISPOSITIVO LO HACE?", c, size=13)
    yy += 30
    for k, (of, tipo) in enumerate(ofi):
        ry = yy + k * 72
        caja(b, x0, ry, ww, 62, c, r=10)
        b.append(T(x0 + 18, ry + 39, [of], 17, INK))
        pista(b, x0 + 470, ry + 39, f"oficio {tipo}", size=14)
        for j, lab in enumerate(("sí", "no", "el texto no lo dice")):
            b.append(checkbox(x0 + 720 + j * 110, ry + 20, s=11, c=c))
            b.append(T(x0 + 750 + j * 110, ry + 38, [lab], 15, GRAY))
    yy += 4 * 72 + 8
    yy = frase_hueco(b, x0, yy, ww, "El dispositivo hace ____ de los ____ oficios: reemplaza ______________ .", c)
    return ojo(b, x0, yy + 14, ww, "UNA PALABRA DEL TEXTO QUE NO CUADRA",
               "Dice que el dispositivo «evita las hipoglucemias» (azúcar bajo). Pero si libera insulina cuando la "
               "glucosa sube, lo que evita son las hiperglucemias (azúcar alto). Pregúntale al profe; para "
               "responder no cambia nada.")


Q = {1: dict(n=1, est=1, pag=83, ctx="Un paciente sin hormona antidiurética · qué efecto directo",
             comp="Uso comprensivo del conocimiento científico", inst=i1),
     2: dict(n=2, est=4, pag=83, ctx="Correr al sol y quedarse en una sala fría · qué hipótesis",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=1, pag=83, ctx="El calcio en la sangre baja · cómo se restablece",
             comp="Uso comprensivo del conocimiento científico", inst=i3),
     4: dict(n=4, est=2, pag=84, ctx="Ranas Litoria en estivación · para qué acumulan urea",
             comp="Uso comprensivo del conocimiento científico", inst=i4),
     5: dict(n=5, est=2, pag=84, ctx="Ranas estivadas en ambiente húmedo · qué cambia primero",
             comp="Indagación", inst=i5),
     6: dict(n=6, est=2, pag=84, ctx="La estivación · por qué es una estrategia evolutiva",
             comp="Explicación de fenómenos", inst=i6),
     7: dict(n=7, est=3, pag=84, ctx="Tabla de tres especies · por qué la rana elimina tan poca agua",
             comp="Indagación", inst=i7),
     8: dict(n=8, est=3, pag=85, ctx="El camello · qué hipótesis para conservar agua",
             comp="Indagación", inst=i8),
     9: dict(n=9, est=1, pag=85, ctx="Una comida rica en carbohidratos · cómo se regula la glucosa",
             comp="Uso comprensivo del conocimiento científico", inst=i9),
     10: dict(n=10, est=4, pag=85, ctx="El páncreas artificial · qué hace y qué no",
              comp="Explicación de fenómenos", inst=i10)}


def build(pages=(147, 148, 150, 151, 152)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"bio2_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
