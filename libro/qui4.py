#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 4 · componente químico, aspectos fisicoquímicos de mezclas · páginas 204–210.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 4» de Química (fuente_libro/QUÍMICA), páginas 170–173.
Casos: sulfato de cobre, cloruro de sodio y azúcar calentados en agua (1), arena fina, harina
de maíz y talco en aceite de cocina (2 a 4), los bloques de barro del taller artesanal (5), la
pintura ecológica que conduce (6), la ventilación que limpia granos (7) y la minería artesanal
con métodos físicos (8 a 10).

Claves verificadas (resueltas a mano contra el texto y la tabla del libro, no copiadas, 7 nov 2026):

    1·A  2·C  3·C  4·D  5·A  6·B  7·C  8·D  9·D  10·B

Cómo se resolvieron:
  1 · Las tres se calentaron 10 minutos con la misma agua. Sulfato de cobre: totalmente disuelta
      a 85 °C; azúcar: totalmente disuelta a 90 °C; cloruro de sodio: parcialmente a 95 °C. La
      única opción que usa los datos a favor del sulfato es A (se disolvió por completo a la
      temperatura más baja). B contradice la tabla (la sal quedó parcial); C dice que el azúcar
      se disolvió «a mayor temperatura» y por eso es más soluble (al revés); D confunde calentarse
      más con interactuar más. OJO, hallazgo Media: la afirmación del estudiante es falsa en la
      realidad (a 20 °C se disuelven unos 200 g de azúcar en 100 g de agua, unos 36 g de sal y
      unos 32 g de sulfato de cobre pentahidratado), la tabla no dice cuánto soluto se echó y la
      temperatura final no se controló. A es la mejor de las cuatro dentro del texto, no una
      conclusión química sólida.
  2 · La que sedimenta rápido tiene partículas más grandes y pesadas → C (hipótesis sobre el
      polvo, que es lo que cambia entre frascos). A, B y D hablan del aceite o de una reacción
      que nadie observó.
  3 · Partícula muy fina: se queda suspendida, no se va al fondo → C. A dice que se disuelve en
      el aceite (el talco es mineral insoluble); B, reacción; D, que «desaparece».
  4 · D: el tamaño de partícula influye en la estabilidad y las finas se quedan suspendidas más
      tiempo. A y B lo dicen al revés; C llama «homogénea» a la arena.
  5 · Mismo molde, mismo sol, mismos tres días; lo único distinto es el polvo → A (partículas más
      gruesas, menos cohesión). B y C suponen diferencias que el texto descarta; D usa el color.
  6 · Conducir corriente necesita cargas que se muevan; el carbón (grafito) tiene electrones
      que se mueven → B. A inventa una «reacción conductora»; C confunde aislante térmico con
      conducción eléctrica; D dice que «todas» conducen, contra el dato.
  7 · El aire arrastra lo liviano para su tamaño (menos denso) y deja lo denso → C.
  8 · Si magnetismo y tamaño no sirvieron, el siguiente paso lógico es otra propiedad física
      disponible sin agua ni químicos: la densidad (decantación seca, vibración) → D. A repite lo
      que falló; B («hacerse magnéticas por fricción») es falsa; C cambia el estado con calor.
  9 · En la bandeja seca que vibra no hay imán ni se habla de carga: la vibración separa por
      densidad → D. A necesita un imán; B, cargas; C, el color no cambia el movimiento.
 10 · El tamiz separa por tamaño: pasa lo que cabe por la malla → B. A (color y calor), C
      («siempre» magnéticos: el oro y el cobre brillan y no lo son) y D (triturar por la masa).

Reparto: A 2 · B 2 · C 3 · D 3. Equilibrado (8 y 9 seguidas en D).

Estrategias:
    1 · Compara en igualdad de condiciones         (1, 5        · ICFES 71)   azul
    2 · ¿Se hunde, flota o queda suspendido?       (2, 3, 4     · ICFES 104)  morado
    3 · Ponle nombre a la propiedad                (6, 7, 9     · ICFES 92)   rojo
    4 · Una propiedad, un método de separación     (8, 10       · ICFES 54)   oro

Hojas: 204 qui4_t1 (1-2) · 205 qui4_t2 (3-4) · 206 qui4_i1 · 207 qui4_t3 (5-6) ·
       208 qui4_t4 (7-8) · 209 qui4_t5 (9-10) · 210 qui4_i2.
"""
from taller_base import *

configurar("Química", 4, "químico · aspectos fisicoquímicos de mezclas",
           tema="Cada propiedad física separa algo",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("Compara en igualdad de condiciones", EDU_AZUL),
       2: ("¿Se hunde, flota o queda suspendido?", MORADO),
       3: ("Ponle nombre a la propiedad", EDU_ROJO),
       4: ("Una propiedad, un método de separación", EDU_ORO)}
usar_estrategias(EST)
AZ, MO, RO, OR = (EST[k][1] for k in (1, 2, 3, 4))
ACEITE = "#FBF0C8"


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


def casillas(b, x, y, labels, c, paso=150, size=16):
    for k, lab in enumerate(labels):
        b.append(checkbox(x + k * paso, y, s=10, c=c))
        b.append(T(x + k * paso + 28, y + 16, [lab], size, GRAY))


def frasco(b, x, y, w, h, c, nivel=0.75, fill=ACEITE):
    """Frasco con tapa, lleno de aceite hasta `nivel`."""
    b.append(rect(x + w * 0.12, y, w * 0.76, 22, "white", r=5, stroke=c, sw=2.2))
    ly = y + 30 + (h - 30) * (1 - nivel)
    b.append(rect(x + 3, ly, w - 6, y + h - ly - 3, fill, r=10))
    b.append(rect(x, y + 26, w, h - 26, "none", r=18, stroke=c, sw=2.6))


def tabla(b, x, y, cols, filas, c, rh=56, hh=46, head_size=13):
    """cols = ((rótulo, ancho), …); filas = lista de funciones f(b, x, y, w, h, j) o textos."""
    px = x
    for t, cw in cols:
        caja(b, px, y, cw, hh, c, r=0, fill=A["bg"])
        rot(b, px + 14, y + hh / 2 + 5, t, c, size=head_size)
        px += cw
    for k, fila in enumerate(filas):
        ry = y + hh + k * rh
        px = x
        for j, (t, cw) in enumerate(cols):
            caja(b, px, ry, cw, rh, c, r=0)
            celda = fila[j]
            if callable(celda):
                celda(b, px, ry, cw, rh)
            elif celda:
                b.append(T(px + 14, ry + rh / 2 + 6, [celda], 16, INK))
            px += cw
    return y + hh + len(filas) * rh


def si_no(c, a="sí", bb="no", paso=80):
    return lambda b, x, y, w, h: casillas(b, x + 16, y + h / 2 - 10, (a, bb), c, paso=paso)


def hueco(c, ancho=None):
    return lambda b, x, y, w, h: renglon(b, x + 14, y + h - 14, x + (ancho or w) - 14)


# ───────── P1 · tres sustancias calentadas · cuál es más soluble ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "La carrera que no fue pareja", c,
                      "Solubilidad es cuánto soluto se disuelve en cierta cantidad de agua a una temperatura dada. "
                      "Antes de creerle a la tabla, revisa si las tres sustancias corrieron en las mismas "
                      "condiciones. Después ordénalas con los datos que sí hay.")
    x0, ww = x + 22, w - 44
    cols = (("SUSTANCIA", 300), ("TEMPERATURA FINAL", 230), ("¿TOTALMENTE DISUELTA?", 260),
            ("PUESTO: LA QUE MENOS CALOR NECESITÓ", ww - 790))
    caja_puesto = lambda b, x, y, w, h: caja(b, x + w / 2 - 40, y + 9, 80, h - 18, c, r=8)
    filas = [(n, hueco(c), si_no(c), caja_puesto) for n in ("Sulfato de cobre", "Cloruro de sodio", "Azúcar")]
    yy = tabla(b, x0, yy, cols, filas, c, rh=52, hh=44) + 18
    rot(b, x0, yy + 16, "¿LA CARRERA FUE PAREJA?", c, size=14)
    pista(b, x0 + 240, yy + 16, "marca si el texto lo dice")
    conds = ("la misma cantidad de agua", "la misma cantidad de cada sólido", "el mismo tiempo de calentamiento",
             "la misma temperatura al final")
    for k, t in enumerate(conds):
        cx_ = x0 + (k % 2) * (ww / 2)
        cy_ = yy + 36 + (k // 2) * 40
        b.append(T(cx_, cy_ + 16, [t], 16, INK))
        casillas(b, cx_ + 300, cy_, ("lo dice", "no lo dice"), c, paso=110, size=15)
    yy += 124
    return alto_profe(b, x0, yy, ww,
                      "Pregúntale al profe cómo se mide la solubilidad de verdad (gramos en 100 g de agua, a una "
                      "temperatura fija) y qué es más soluble en la realidad, el azúcar o el sulfato de cobre. La "
                      "pregunta, eso sí, te pide justificar con los datos de ESTA tabla.")


# ───────── P2 · tres polvos en aceite · el que sedimenta más rápido ─────────
def i2(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Tres polvos en la regla del tamaño", c,
                      "Dibuja dentro de cada frasco cómo quedó a los diez minutos: partículas en el fondo, flotando "
                      "o repartidas. Después pon los tres polvos en la regla, del grano más grueso al más fino.")
    x0, ww = x + 22, w - 44
    gap = 30
    fw = 150
    for k, n in enumerate(("arena fina", "harina de maíz", "talco")):
        fx = x0 + 20 + k * (fw + 70)
        frasco(b, fx, yy + 6, fw, 200, c)
        b.append(T(fx + fw / 2, yy + 236, [n], 16, INK, weight="700", anchor="middle"))
    rx = x0 + 680
    rw = x0 + ww - rx
    caja(b, rx, yy + 6, rw, 220, c, r=14)
    rot(b, rx + 18, yy + 34, "LO QUE CAMBIA DE UN FRASCO A OTRO", c, size=14)
    casillas(b, rx + 18, yy + 54, ("el aceite", "el polvo", "el tiempo"), c, paso=150)
    rot(b, rx + 18, yy + 122, "LO QUE ES IGUAL EN LOS TRES", c, size=14)
    renglon(b, rx + 18, yy + 170, rx + rw - 18)
    renglon(b, rx + 18, yy + 206, rx + rw - 18)
    yy += 262
    L, R = x0 + 40, x0 + ww - 40
    b.append(hand_arrow(L, yy + 40, R, yy + 40, c, sw=2.6, bend=0.0, head=14))
    pista(b, L, yy + 74, "la partícula más grande")
    pista(b, R, yy + 74, "la partícula más pequeña", anchor="end")
    for k in range(3):
        caja(b, L + 160 + k * 300, yy, 220, 30, c, r=8, dash="6,5")
    yy += 96
    yy = frase_hueco(b, x0, yy, ww, "El que se fue al fondo primero tenía partículas ______________ .", c)
    return ojo(b, x0, yy + 16, ww, "LA HIPÓTESIS HABLA DE LO QUE CAMBIÓ",
               "si en los tres frascos el aceite es el mismo, una explicación que culpa al aceite no explica por qué "
               "un frasco se portó distinto de los otros dos.")


# ───────── P3 · el talco que no se separa ─────────
CRIT_3 = ("con el tiempo, ¿se va al fondo?", "¿se puede separar con un filtro de papel?",
          "¿el sólido se volvió parte del líquido?", "¿se ve turbio?")


def i3(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Disuelto no es lo mismo que suspendido", c,
                      "Compara con dos mezclas que ya conoces: sal en agua y arena en agua. Responde cada criterio "
                      "para las tres mezclas y mira a cuál de las dos se parece el talco en aceite.")
    x0, ww = x + 22, w - 44
    cols = (("CRITERIO", 470), ("SAL EN AGUA", 250), ("ARENA EN AGUA", 250), ("TALCO EN ACEITE", ww - 970))
    filas = [(t, si_no(c), si_no(c), si_no(c)) for t in CRIT_3]
    yy = tabla(b, x0, yy, cols, filas, c, rh=50, hh=42) + 18
    rot(b, x0, yy + 16, "EL TALCO EN ACEITE SE PARECE MÁS A…", c, size=14)
    casillas(b, x0 + 360, yy, ("la sal en agua", "la arena en agua", "ninguna de las dos"), c, paso=200)
    yy += 44
    yy = frase_hueco(b, x0, yy, ww, "Lo que hace que el talco no se vaya al fondo es ______________________ .", c)
    return trampa(b, x0, yy + 16, ww, "Que no lo veas no quiere decir que se disolvió:",
                  "el talco es un mineral que no se disuelve en aceite. Si una opción dice que se disolvió o que "
                  "desapareció, compárala con tu tabla.", c)


# ───────── P4 · la afirmación válida sobre las mezclas ─────────
def i4(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Cuatro reglas contra tres frascos", c,
                      "Cada opción es una regla general. Una regla general se cae con un solo frasco que la "
                      "contradiga. Escribe qué dice cada opción de las partículas y pásala por los tres frascos.")
    x0, ww = x + 22, w - 44

    def L_(L):
        return lambda b, x, y, w, h: letra(b, x + w / 2, y + h / 2, L, c)

    caja_f = lambda b, x, y, w, h: caja(b, x + 16, y + 9, w - 32, h - 18, c, r=8)
    cols = (("", 70), ("QUÉ DICE DE LAS PARTÍCULAS", 520), ("¿LO CONFIRMAN LOS FRASCOS?", 300),
            ("EL FRASCO QUE LA PRUEBA O LA TUMBA", ww - 890))
    filas = [(L_(L), hueco(c), si_no(c), caja_f) for L in "ABCD"]
    yy = tabla(b, x0, yy, cols, filas, c, rh=58, hh=44) + 18
    return ojo(b, x0, yy, ww, "«HOMOGÉNEA» Y «HETEROGÉNEA» SE VEN",
               "si una opción llama homogénea a una mezcla en la que se ve un sólido en el fondo, ya tienes el frasco "
               "que la tumba.")


# ───────── P5 · los bloques de barro ─────────
CONDS_5 = ("el molde", "los días al sol", "el sol que recibió cada bloque", "el barro seco", "el polvo fino agregado",
           "el tiempo antes de desmoldar")


def i5(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dos bloques, una sola diferencia", c,
                      "Una buena hipótesis apunta a lo que fue distinto entre los dos bloques, no a lo que fue igual. "
                      "Pasa cada condición por el texto: ¿fue igual, fue distinta o el texto no lo dice?")
    x0, ww = x + 22, w - 44
    # los dos bloques
    bw = 170
    b.append(rect(x0 + 20, yy + 20, bw, 110, "#EFE3D0", r=6, stroke=c, sw=2.4))
    b.append(T(x0 + 20 + bw / 2, yy + 160, ["bloque que se mantuvo"], 15, INK, anchor="middle"))
    bx = x0 + 240
    b.append(rect(bx, yy + 20, bw, 110, "#EFE3D0", r=6, stroke=c, sw=2.4))
    b.append(f'<path d="M {bx + 40} {yy + 20} L {bx + 70} {yy + 60} L {bx + 52} {yy + 88} L {bx + 90} {yy + 130}" '
             f'fill="none" stroke="{INK}" stroke-width="2.4"/>')
    b.append(f'<path d="M {bx + 130} {yy + 20} L {bx + 116} {yy + 54} L {bx + 150} {yy + 80}" fill="none" '
             f'stroke="{INK}" stroke-width="2.2"/>')
    b.append(T(bx + bw / 2, yy + 160, ["bloque que se fragmentó"], 15, INK, anchor="middle"))
    tx = x0 + 470
    cols = (("CONDICIÓN", 300), ("IGUAL", 120), ("DISTINTA", 140), ("NO LO DICE", ww - 470 - 560))

    def chk(b, x, y, w, h):
        b.append(checkbox(x + w / 2 - 10, y + h / 2 - 10, s=10, c=c))

    filas = [(t, chk, chk, chk) for t in CONDS_5]
    yy2 = tabla(b, tx, yy, cols, filas, c, rh=44, hh=40)
    yy = max(yy2, yy + 180) + 18
    yy = frase_hueco(b, x0, yy, ww, "La hipótesis tiene que hablar de ______________________ , porque es lo único "
                                    "distinto.", c)
    return ojo(b, x0, yy + 16, ww, "UNA HIPÓTESIS NO CONTRADICE EL TEXTO",
               "si el texto dice que los dos bloques estuvieron igual de tiempo y en el mismo sol, una explicación que "
               "suponga lo contrario no es coherente, por razonable que suene.")


# ───────── P6 · la pintura que conduce ─────────
def i6(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El bombillo de prueba", c,
                      "Así se prueba en el laboratorio si algo conduce: se pone en el hueco del circuito y se mira el "
                      "bombillo. Completa qué pasó con cada pintura según el texto y escribe qué tiene que tener "
                      "por dentro un material para que el bombillo prenda.")
    x0, ww = x + 22, w - 44
    # circuito
    cx0, cy0 = x0 + 30, yy + 30
    b.append(rect(cx0, cy0 + 60, 70, 110, "white", r=8, stroke=INK, sw=2.4))
    b.append(rect(cx0 + 22, cy0 + 50, 26, 12, INK, r=2))
    b.append(T(cx0 + 35, cy0 + 125, ["pila"], 15, INK, anchor="middle"))
    b.append(line(cx0 + 35, cy0 + 50, cx0 + 35, cy0, INK, 2.4))
    b.append(line(cx0 + 35, cy0, cx0 + 300, cy0, INK, 2.4))
    b.append(f'<circle cx="{cx0 + 300}" cy="{cy0 + 34}" r="30" fill="white" stroke="{INK}" stroke-width="2.4"/>')
    b.append(f'<path d="M {cx0 + 288} {cy0 + 44} Q {cx0 + 300} {cy0 + 18} {cx0 + 312} {cy0 + 44}" fill="none" '
             f'stroke="{INK}" stroke-width="2"/>')
    b.append(T(cx0 + 344, cy0 + 40, ["bombillo"], 15, INK))
    b.append(line(cx0 + 300, cy0 + 64, cx0 + 300, cy0 + 120, INK, 2.4))
    b.append(rect(cx0 + 230, cy0 + 120, 140, 70, "white", r=8, stroke=c, sw=2.4, dash="7,5"))
    b.append(T(cx0 + 300, cy0 + 160, ["la pintura"], 15, c, weight="700", anchor="middle"))
    b.append(line(cx0 + 300, cy0 + 190, cx0 + 300, cy0 + 220, INK, 2.4))
    b.append(line(cx0 + 300, cy0 + 220, cx0 + 35, cy0 + 220, INK, 2.4))
    b.append(line(cx0 + 35, cy0 + 220, cx0 + 35, cy0 + 170, INK, 2.4))
    rx = x0 + 520
    cols = (("PINTURA CON MÁS…", 260), ("¿PRENDE?", ww - 520 - 260))
    filas = [(t, si_no(c)) for t in ("carbón vegetal", "cal", "almidón")]
    yy2 = tabla(b, rx, yy + 10, cols, filas, c, rh=50, hh=40)
    yy = max(yy2, yy + 260) + 16
    caja(b, x0, yy, ww, 92, c, r=14)
    rot(b, x0 + 18, yy + 28, "PARA QUE PASE CORRIENTE, POR DENTRO EL MATERIAL TIENE QUE TENER…", c, size=14)
    renglon(b, x0 + 18, yy + 74, x0 + ww - 18)
    yy += 108
    return alto_profe(b, x0, yy, ww,
                      "Pregúntale al profe por qué conducen los metales y el grafito (que es carbón) y por qué una "
                      "sal sólida no conduce pero disuelta en agua sí. Y qué diferencia hay entre conducir el calor "
                      "y conducir la electricidad.")


# ───────── P7 · ventilación de granos ─────────
def i7(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Lo que se lleva el aire y lo que se queda", c,
                      "Reparte las cosas del texto entre el compartimento y la cinta. Después compara una cáscara y "
                      "un grano del mismo tamaño: ¿en qué se diferencian para que el aire trate distinto a cada uno?")
    x0, ww = x + 22, w - 44
    # ventilador y cinta
    fx, fy = x0 + 40, yy + 90
    for k in range(3):
        a = math.radians(90 + k * 120)
        b.append(f'<ellipse cx="{fx + 22 * math.cos(a):.1f}" cy="{fy + 22 * math.sin(a):.1f}" rx="22" ry="10" '
                 f'fill="white" stroke="{c}" stroke-width="2.2" transform="rotate({90 + k * 120} '
                 f'{fx + 22 * math.cos(a):.1f} {fy + 22 * math.sin(a):.1f})"/>')
    b.append(f'<circle cx="{fx}" cy="{fy}" r="6" fill="{c}"/>')
    pista(b, fx, fy + 64, "aire", anchor="middle")
    for k in range(3):
        b.append(hand_arrow(fx + 60, fy - 20 + k * 20, fx + 230, fy - 30 + k * 16, c, sw=2.2, bend=0.0, head=10))
    b.append(rect(x0 + 100, yy + 200, 520, 26, "#E6E9EE", r=13, stroke=INK, sw=2))
    for px in (x0 + 113, x0 + 607):
        b.append(f'<circle cx="{px}" cy="{yy + 213}" r="9" fill="white" stroke="{INK}" stroke-width="2"/>')
    pista(b, x0 + 360, yy + 254, "cinta transportadora", anchor="middle")
    b.append(rect(x0 + 300, yy + 10, 320, 120, "white", r=10, stroke=c, sw=2.2, dash="7,5"))
    rot(b, x0 + 316, yy + 36, "COMPARTIMENTO", c, size=13)
    renglon(b, x0 + 316, yy + 80, x0 + 604)
    renglon(b, x0 + 316, yy + 114, x0 + 604)
    rot(b, x0 + 120, yy + 184, "SE QUEDA EN LA CINTA:", c, size=13)
    renglon(b, x0 + 330, yy + 186, x0 + 610)
    rx = x0 + 680
    rw = x0 + ww - rx
    caja(b, rx, yy + 10, rw, 250, c, r=14)
    rot(b, rx + 18, yy + 38, "UNA CÁSCARA Y UN GRANO DEL MISMO TAMAÑO", c, size=13)
    b.append(T(rx + 18, yy + 76, ["¿Cuál pesa más?"], 16, INK))
    renglon(b, rx + 170, yy + 78, rx + rw - 18)
    b.append(T(rx + 18, yy + 124, ["Entonces, para su tamaño, el que tiene"], 16, INK))
    b.append(T(rx + 18, yy + 150, ["más masa es el que…"], 16, INK))
    renglon(b, rx + 170, yy + 152, rx + rw - 18)
    b.append(T(rx + 18, yy + 200, ["El aire se lleva lo que…"], 16, INK))
    renglon(b, rx + 18, yy + 238, rx + rw - 18)
    yy += 280
    return ojo(b, x0, yy, ww, "PREGÚNTALE A CADA OPCIÓN: ¿ESO LO NOTA EL VIENTO?",
               "la propiedad que buscas tiene que cambiar lo que el aire hace con la partícula mientras pasa por la "
               "cinta. Si el viento no la «siente», no puede ser la que hace funcionar el sistema.")


# ───────── P8 · minería artesanal · el siguiente paso ─────────
METODOS = (("con un imán", None), ("con un tamiz (una malla)", None), ("con vibración en bandeja seca", None),
           ("echándolo en agua", None), ("calentándolo hasta fundir", None))


def i8(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Tachar lo que ya falló", c,
                      "Cada método de separación aprovecha una propiedad física. Escribe cuál aprovecha cada uno, "
                      "marca si ya se probó y falló, y si las reglas del lote lo permiten: solo propiedades físicas, "
                      "sin agua ni sustancias químicas.")
    x0, ww = x + 22, w - 44
    cols = (("MÉTODO", 330), ("PROPIEDAD QUE APROVECHA", 360), ("¿YA FALLÓ?", 240), ("¿LO PERMITE EL LOTE?", ww - 930))
    filas = [(t, hueco(c), si_no(c), si_no(c)) for t, _ in METODOS]
    yy = tabla(b, x0, yy, cols, filas, c, rh=54, hh=42) + 18
    yy = frase_hueco(b, x0, yy, ww, "Si fallaron los que usan ______________ y ______________ , pruebo con "
                                    "______________ .", c)
    return ojo(b, x0, yy + 16, ww, "UN SIGUIENTE PASO LÓGICO NO REPITE NI INVENTA",
               "repetir lo que falló con más fuerza no es un paso nuevo. Y un método que supone que una partícula se "
               "vuelve magnética o cambia de estado tiene que poder explicarse con una propiedad física real.")


# ───────── P9 · minería · la bandeja que vibra ─────────
def i9(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "Centro o borde de la bandeja", c,
                      "Mira la bandeja desde arriba. Dibuja con puntos gruesos los fragmentos que se van a los bordes "
                      "y con puntos finos los que se quedan quietos en el centro. Después revisa qué hay de verdad "
                      "en la bandeja para que algo se mueva.")
    x0, ww = x + 22, w - 44
    tw_ = 420
    b.append(rect(x0 + 20, yy + 10, tw_, 250, "white", r=14, stroke=c, sw=2.6))
    b.append(rect(x0 + 120, yy + 70, tw_ - 200, 130, "none", r=10, stroke=c, sw=1.8, dash="6,6"))
    pista(b, x0 + 20 + tw_ / 2, yy + 140, "centro", anchor="middle")
    pista(b, x0 + 30, yy + 36, "borde")
    for k in range(3):
        b.append(line(x0 + 470, yy + 90 + k * 30, x0 + 500, yy + 80 + k * 30, c, 2.2))
        b.append(line(x0 + 500, yy + 80 + k * 30, x0 + 530, yy + 100 + k * 30, c, 2.2))
    pista(b, x0 + 500, yy + 200, "vibra", anchor="middle")
    rx = x0 + 580
    rw = x0 + ww - rx
    caja(b, rx, yy + 10, rw, 120, c, r=14)
    rot(b, rx + 18, yy + 38, "EN LA BANDEJA HAY…", c, size=14)
    casillas(b, rx + 18, yy + 58, ("un imán", "agua"), c, paso=150)
    casillas(b, rx + 18, yy + 92, ("cargas eléctricas", "solo vibración"), c, paso=190)
    caja(b, rx, yy + 146, rw, 114, c, r=14)
    rot(b, rx + 18, yy + 174, "LOS DEL BORDE Y LOS DEL CENTRO SE DIFERENCIAN EN…", c, size=13)
    renglon(b, rx + 18, yy + 236, rx + rw - 18)
    yy += 282
    return ojo(b, x0, yy, ww, "UNA PROPIEDAD SOLO EXPLICA SI ESTÁ EN JUEGO",
               "si no hay imán en la bandeja, el magnetismo no puede empujar a nadie; si nadie frotó ni cargó los "
               "fragmentos, la carga tampoco. Busca la propiedad que sí actúa cuando solo hay vibración y gravedad.")


# ───────── P10 · minería · la afirmación válida ─────────
def i10(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "El tamiz por dentro", c,
                      "Así se ve una malla de cerca. Encierra con un círculo las partículas que pasan por los huecos y "
                      "tacha las que se quedan arriba. Después escribe la única pregunta que el tamiz le hace a cada "
                      "partícula.")
    x0, ww = x + 22, w - 44
    gx, gy, gs, n = x0 + 30, yy + 10, 56, 5
    for k in range(n + 1):
        b.append(line(gx + k * gs, gy, gx + k * gs, gy + n * gs, c, 4))
        b.append(line(gx, gy + k * gs, gx + n * gs, gy + k * gs, c, 4))
    parts = ((gx + 30, gy + 26, 16), (gx + 140, gy + 80, 40), (gx + 200, gy + 140, 12), (gx + 90, gy + 200, 30),
             (gx + 250, gy + 230, 14), (gx + 30, gy + 150, 46), (gx + 240, gy + 40, 26))
    for px, py, r in parts:
        b.append(f'<circle cx="{px}" cy="{py}" r="{r / 2 + 3}" fill="#EFE3D0" stroke="{INK}" stroke-width="2"/>')
    rx = x0 + 380
    rw = x0 + ww - rx
    caja(b, rx, yy + 10, rw, 120, c, r=14)
    rot(b, rx + 18, yy + 38, "LA ÚNICA PREGUNTA QUE HACE EL TAMIZ", c, size=14)
    renglon(b, rx + 18, yy + 100, rx + rw - 18)
    caja(b, rx, yy + 146, rw, 134, c, r=14)
    rot(b, rx + 18, yy + 174, "BUSCA UN CONTRAEJEMPLO", c, size=14)
    b.append(T(rx + 18, yy + 210, ["Un material que brilla como metal y que un imán NO atrae:"], 16, INK))
    renglon(b, rx + 18, yy + 256, rx + rw - 18)
    yy += 300
    return trampa(b, x0, yy, ww, "Las palabras «siempre» y «todos» piden mucho:",
                  "a una afirmación con «siempre» la tumba un solo caso en contra. Y una afirmación válida tiene que "
                  "decir qué propiedad usa el método y por qué funciona.", c)


Q = {1: dict(n=1, est=1, pag=170, ctx="Sulfato de cobre, sal y azúcar · cuál es más soluble",
             comp="Indagación", inst=i1),
     2: dict(n=2, est=2, pag=171, ctx="Tres polvos en aceite · por qué uno sedimentó más rápido",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=2, pag=171, ctx="Tres polvos en aceite · el talco que no se separa",
             comp="Explicación de fenómenos", inst=i3),
     4: dict(n=4, est=2, pag=172, ctx="Tres polvos en aceite · la afirmación válida",
             comp="Uso comprensivo del conocimiento científico", inst=i4),
     5: dict(n=5, est=1, pag=172, ctx="Bloques de barro · por qué uno se fragmentó",
             comp="Indagación", inst=i5),
     6: dict(n=6, est=3, pag=172, ctx="Pintura ecológica · cuál conduce la corriente",
             comp="Explicación de fenómenos", inst=i6),
     7: dict(n=7, est=3, pag=172, ctx="Ventilación de granos · qué propiedad hace funcionar el sistema",
             comp="Uso comprensivo del conocimiento científico", inst=i7),
     8: dict(n=8, est=4, pag=173, ctx="Minería artesanal · el siguiente paso para separar",
             comp="Indagación", inst=i8),
     9: dict(n=9, est=3, pag=173, ctx="Minería artesanal · la bandeja que vibra",
             comp="Explicación de fenómenos", inst=i9),
     10: dict(n=10, est=4, pag=173, ctx="Minería artesanal · la afirmación válida sobre los métodos",
              comp="Uso comprensivo del conocimiento científico", inst=i10)}


def build(pages=(204, 205, 207, 208, 209)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"qui4_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
