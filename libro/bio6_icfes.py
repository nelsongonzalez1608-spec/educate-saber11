#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 6 · entrenamiento ICFES · páginas 177 y 181.

Las cuatro preguntas salen del cuadernillo oficial Saber 11 2016-1, SEGUNDA sesión (cuadernillo
ABD; encabezado de la sección «Saber 11 - 083 - B10O - ABD · 2a. sesión»), sección Ciencias
Naturales. Verificadas contra la portada («ABD · 2016-1 · Examen de Estado · Segunda sesión») y
las páginas escaneadas en Drive («1. CUADERNILLOS ICFES» / «2016-2 SEGUNDA SESION.pdf»).
Ninguna estaba en tablero/icfes.csv; reservadas en tablero/propuestas/bio_icfes_reservas.csv.

Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11», sin año ni «oficial».

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · N.º 61 · A   (ciclo menstrual o estral en cuatro especies)                    estrategia 1
    QB · N.º 51 · D   (etileno · en qué orden vender las frutas)                       estrategia 2
    QC · N.º 57 · B   (dengue · por qué sirve reducir el agua estancada)               estrategia 3
    QD · N.º 64 · A   (floema · por qué llevar azúcar a raíces, tubérculos y frutos)   estrategia 4

  61 · A: el ciclo menstrual es exclusivo de primates y dura de 24 a 35 días; se repite casi cada
       mes. Especie 1 (Ateles, mono araña): 24-27 días, 12 ciclos al año; especie 4 (Papio,
       babuino): 31-35 días, 11 al año. Las especies 2 (vaca: 21-23 días, 6 al año) y 3 (caballo:
       23-26 días, 4 al año) son estrales: pocos ciclos, por temporadas. Ojo: la duración de la 3
       (23-26) se cruza con el rango menstrual; decide el número de ciclos al año y el grupo.
  51 · D: en horas: guayaba 51, banano 58, aguacate 93, mango 96,4 (4 días y 24 minutos), piña
       122. Primero se vende la que madura antes.
  57 · B: menos agua estancada → menos lugares donde se reproduce el mosquito → menos picaduras.
  64 · A: los órganos que no hacen fotosíntesis reciben el azúcar como fuente de energía.

Reparto de las cuatro: A 2 · B 1 · D 1. En la N.º 57 la correcta es la más larga (así viene en el
cuadernillo); registrado como Atención.

Adaptaciones de formato: de la N.º 61 se omiten las dos gráficas de hormonas del contexto (no se
necesitan para responder; se dice en la hoja); las tablas de la 61 y la 51 se redibujaron con los
mismos datos. El contexto del dengue de la N.º 57 es el mismo de la N.º 55 (Misión 5).
"""
from bio6 import *   # noqa: F401,F403  (configura la misión y EST)
from bio6 import rot, caja, pista, renglon, texto, sino, frase_hueco, tinte, flecha, letra


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


def tabla(b, x, y, cols, filas, c=GRAY, rh=36, head_h=40, size=16, italic_cols=()):
    """Tabla de datos del cuadernillo: cabecera y filas, en tinta."""
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
        for k, ((w_, _), v) in enumerate(zip(cols, f)):
            b.append(T(cx + w_ / 2, yy + rh / 2 + 6, [v], size, INK, anchor="middle",
                       style="italic" if k in italic_cols else "normal"))
            cx += w_
        yy += rh
    cx = x
    for w_, _ in cols[:-1]:
        cx += w_
        b.append(line(cx, y, cx, yy, c, 1.6))
    return yy


# ───────── QA · N.º 61 · ciclos ─────────
CICLOS = ("En el grupo de los mamíferos se presentan dos tipos de ciclos reproductivos: el menstrual (de 24 a 35 días), "
          "exclusivo de primates y humanos; y el ciclo estral (entre estaciones), en el resto de mamíferos. La "
          "diferencia entre estos dos tipos de ciclos radica en el periodo de receptividad sexual. En el ciclo estral, "
          "la hembra solo es sexualmente receptiva durante el estro u ovulación; en el ciclo menstrual, la hembra "
          "muestra receptividad sexual durante casi todo el ciclo. (El cuadernillo trae además dos gráficas de "
          "hormonas de cada ciclo; para esta pregunta no se necesitan.)")
ESPECIES = (("1", "Ateles belzebuth", "24 - 27", "12"), ("2", "Bos primigenius taurus", "21 - 23", "6"),
            ("3", "Equus ferus caballus", "23 - 26", "4"), ("4", "Papio hamadryas", "31 - 35", "11"))


def datos_61(b, x, y, w):
    yy = pregunta(b, x, y, w, "En la tabla se muestran la duración en días de algunos ciclos reproductivos de "
                              "especies de mamíferos.")
    yy = tabla(b, x + 120, yy + 12, ((110, "Especie"), (300, "Nombre científico"), (150, "Ciclo (días)"),
                                     (230, "Ciclos al año")), ESPECIES, rh=32, italic_cols=(1,))
    return pregunta(b, x, yy + 4, w, "Con base en la información anterior, ¿cuáles corresponden a ciclos menstruales?")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Todo el año o por temporadas", c,
                      "El texto da dos pistas de cada ciclo: cuánto dura y cada cuánto se repite. Revisa las dos en "
                      "cada especie; si solo una cuadra, todavía no decidas.")
    x0, ww = x + 22, w - 44
    cols = (130, 360, 360, ww - 850)
    heads = ("ESPECIE", "¿DURA ENTRE 24 Y 35 DÍAS?", "¿SE REPITE CASI CADA MES?", "ENTONCES ES")
    caja(b, x0, yy, ww, 40, c, fill=tinte(c), r=8)
    cx = x0
    for k, hd in enumerate(heads):
        rot(b, cx + 16, yy + 27, hd, c, size=13)
        cx += cols[k]
    ry = yy + 40
    for n in "1234":
        caja(b, x0, ry, ww, 44, c, r=0)
        texto(b, x0 + 60, ry + 29, n, size=17, weight="700", anchor="middle")
        sino(b, x0 + cols[0] + 30, ry + 12, c)
        sino(b, x0 + cols[0] + cols[1] + 30, ry + 12, c)
        renglon(b, x0 + sum(cols[:3]) + 16, ry + 34, x0 + ww - 16)
        ry += 44
    cx = x0
    for k in range(3):
        cx += cols[k]
        b.append(line(cx, yy, cx, ry, c, 1.6))
    return ry


# ───────── QB · N.º 51 · etileno ─────────
ETILENO = ("Algunos mercaderes de frutas utilizan el etileno, una hormona vegetal que promueve la maduración del fruto, "
           "para lograr frutos más jugosos en corto tiempo. Sin embargo, un tiempo prolongado de exposición a esta "
           "hormona disminuye la vida útil del fruto porque se pudre más rápido. Debido a esto, los mercaderes "
           "calcularon el tiempo de exposición necesario para la maduración del fruto sin que este se pudra. Sus "
           "resultados se muestran en la tabla.")


def datos_51(b, x, y, w):
    yy = tabla(b, x + 10, y + 10, ((270, "Fruto"), (180, "Piña"), (180, "Mango"), (180, "Banano"), (180, "Aguacate"),
                                   (180, "Guayaba")),
               (("Tiempo de exposición al etileno", "5 días y 2 horas", "4 días y 24 minutos", "2 días y 10 horas",
                 "3 días y 21 horas", "2 días y 3 horas"),), rh=40)
    return pregunta(b, x, yy + 4, w, "Si un mercader expone todos los frutos en bodega al etileno, ¿cuál debe ser el "
                                     "orden, del tiempo más cercano al más lejano, en que deben venderse las frutas "
                                     "para que no se pudran y no se pierdan en el negocio?")


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "Todo en horas antes de ordenar", c,
                      "Días, horas y minutos mezclados confunden. Pasa cada tiempo a horas (un día = 24 horas) y "
                      "después numera del que madura primero al último.")
    x0, ww = x + 22, w - 44
    n = 5
    bw = (ww - (n - 1) * 16) / n
    for k, f in enumerate(("Piña", "Mango", "Banano", "Aguacate", "Guayaba")):
        bx = x0 + k * (bw + 16)
        caja(b, bx, yy, bw, 120, c, r=14)
        texto(b, bx + 16, yy + 30, f, size=17, weight="700", color=c)
        texto(b, bx + 16, yy + 72, "= ______ horas", size=16, color=GRAY)
        texto(b, bx + 16, yy + 106, "orden:", size=16, color=GRAY)
        b.append(rect(bx + 76, yy + 84, 44, 30, "white", r=6, stroke=c, sw=1.8))
    return yy + 120


# ───────── QC · N.º 57 · agua estancada ─────────
DENGUE = ("El dengue es una enfermedad tropical producida por la infección con el virus Flavivirus, que se transmite a "
          "través de las picaduras de algunos mosquitos hembra del género Aedes. Este tipo de mosquito se reproduce "
          "principalmente en aguas estancadas. Algunas de las medidas que recomiendan las entidades estatales para "
          "disminuir el caso de personas infectadas son: • Tapar los recipientes con agua al aire libre; eliminar "
          "llantas, botellas, barriles u otros recipientes que puedan retener agua. • Usar insecticidas para "
          "mosquitos. Investigaciones recientes han demostrado que algunas especies de adultos de mosquito del género "
          "Aedes son más resistentes que otras a algunos insecticidas, sin importar su concentración, de manera que "
          "el uso de estos no garantiza un 100% de protección frente al dengue.")


def datos_57(b, x, y, w):
    return pregunta(b, x, y, w, "Teniendo en cuenta lo anterior, ¿por qué reducir el número de lugares donde el agua "
                                "se estanca es un buen método de prevención contra el dengue?")


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Dónde se corta el ciclo del dengue", c,
                      "Como con el frailejón: si cae una pieza, cae lo que depende de ella. Escribe en el ciclo quién "
                      "vive dónde y marca con una X el punto que corta tapar los recipientes.")
    x0, ww = x + 22, w - 44
    pasos = ("el agua quieta", "huevos y larvas", "mosquito adulto", "picadura", "persona")
    n = len(pasos)
    bw = (ww - (n - 1) * 46) / n
    for k, p in enumerate(pasos):
        bx = x0 + k * (bw + 46)
        caja(b, bx, yy, bw, 96, c, r=16)
        texto(b, bx + bw / 2, yy + 30, p, size=16, weight="700", anchor="middle")
        renglon(b, bx + 14, yy + 76, bx + bw - 14)
        if k < n - 1:
            flecha(b, bx + bw + 4, yy + 48, bx + bw + 42, yy + 48, c, sw=2.4, head=10)
    pista(b, x0, yy + 124, "en cada caja: quién está ahí (el mosquito, el virus o los dos)", size=15)
    return yy + 130


# ───────── QD · N.º 64 · floema ─────────
FLOEMA = ("Las plantas vasculares poseen un sistema de transporte de los productos fotosintéticos (azúcares) llamado "
          "floema. El floema transporta estos productos desde las hojas hasta los órganos subterráneos y de reserva, "
          "como las raíces, los tubérculos y los frutos.")


def datos_64(b, x, y, w):
    return pregunta(b, x, y, w, "Con base en la información anterior, ¿por qué es importante que se lleve a cabo el "
                                "transporte de azúcares a estos órganos de la planta?")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Quién fabrica el azúcar y quién lo gasta", c,
                      "Como con los rasgos del frailejón: cada órgano tiene su oficio. Marca cuál fabrica azúcar con "
                      "luz y cuál solo lo recibe, y escribe para qué lo usa el que lo recibe.")
    x0, ww = x + 22, w - 44
    org = ("hoja", "fruto", "tubérculo", "raíz")
    bw = (ww - 3 * 16) / 4
    for k, o in enumerate(org):
        bx = x0 + k * (bw + 16)
        caja(b, bx, yy, bw, 132, c, r=14)
        texto(b, bx + 16, yy + 30, o, size=17, weight="700", color=c)
        sino(b, bx + 16, yy + 44, c, labels=("fabrica", "recibe"), gap=120)
        pista(b, bx + 16, yy + 98, "lo usa para…", size=14)
        renglon(b, bx + 100, yy + 100, bx + bw - 14)
    return yy + 132


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico", e=CICLOS,
          o=["Los de las especies 1 y 4.", "Los de las especies 1 y 3.", "Los de las especies 2 y 3.",
             "Los de las especies 3 y 4."],
          datos=datos_61, inst=ii1)
QB = dict(est=2, comp="Indagación", e=ETILENO,
          o=["Piña, mango, aguacate, banano, guayaba.", "Aguacate, mango, piña, guayaba, banano.",
             "Banano, aguacate, guayaba, piña, mango.", "Guayaba, banano, aguacate, mango, piña."],
          datos=datos_51, inst=ii2)
QC = dict(est=3, comp="Explicación de fenómenos", e=DENGUE,
          o=["Porque al reducir el número de lugares donde el agua se estanca, disminuirán los casos de personas "
             "infectadas por beber este tipo de agua.",
             "Porque al reducir el número de lugares donde el agua se estanca, disminuirán los hábitats del mosquito "
             "y, por tanto, no habrá tantas picaduras de mosquito que transmitan el virus a las personas.",
             "Porque al reducir el número de lugares donde el agua se estanca, el agua no producirá mal olor y se "
             "favorecerá el crecimiento y reproducción de los mosquitos.",
             "Porque al reducir el número de lugares donde el agua se estanca, disminuirán los hábitats del virus y, "
             "por tanto, estos empezarán a infectar a las personas directamente sin necesitar de los mosquitos."],
          datos=datos_57, inst=ii3)
QD = dict(est=4, comp="Uso comprensivo del conocimiento científico", e=FLOEMA,
          o=["Porque permite que los azúcares se movilicen a los órganos no fotosintéticos y les provea energía.",
             "Porque aporta azúcares a las raíces y expulsa dióxido de carbono por los frutos en el momento de la "
             "fotosíntesis.",
             "Porque permite que las raíces, los tubérculos y los frutos conduzcan el azúcar hacia las hojas para que "
             "realicen la fotosíntesis.",
             "Porque aporta las sustancias necesarias para que las raíces, los tubérculos y los frutos realicen la "
             "fotosíntesis."],
          datos=datos_64, inst=ii4)


def build(pages=(177, 181)):
    return [hoja_icfes("bio6_i1", pages[0], QA, QB),
            hoja_icfes("bio6_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
