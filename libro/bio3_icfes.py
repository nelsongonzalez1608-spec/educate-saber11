#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Biología · Misión 3 · entrenamiento ICFES · páginas 156 y 160.

Las cuatro preguntas salen de los cuadernillos oficiales Saber 11 2016-1 que están en Drive
(carpeta «1. CUADERNILLOS ICFES»), sección Ciencias Naturales, verificadas contra la página
escaneada:
  · «2016-1 PRIMERA SESION.pdf» — 1.ª sesión, cuadernillo AAM (encabezado «Saber 11 - 083 -
    B05R - AAM · 1a. sesión»), ítems 94 y 116.
  · «2016-2 SEGUNDA SESION.pdf» — en la portada dice 2016-1, 2.ª sesión, cuadernillo ABD
    (encabezado «Saber 11 - 083 - B10O - ABD · 2a. sesión»), ítems 59 y 67.
Ninguna estaba en tablero/icfes.csv; las cuatro se reservaron en
tablero/propuestas/bio_icfes_reservas.csv. Ninguna nombra a un político.

Membrete (regla 7, Nelson 10 nov): siempre «Pregunta Saber 11» (el motor lo impone).

Claves verificadas (resueltas a mano, no copiadas de un solucionario):

    QA · 1.ª ses. N.º 94  · C   (eutrofización · qué le pasa al oxígeno)            estrategia 3
    QB · 1.ª ses. N.º 116 · D   (moléculas de un ser vivo que muere)                 estrategia 2
    QC · 2.ª ses. N.º 67  · A   (planta de energía en zona agrícola junto al mar)    estrategia 1
    QD · 2.ª ses. N.º 59  · D   (tanque poco profundo y luz ultravioleta)            estrategia 4

Cuentas: QC · la planta debe dar más de 2.100 kcal/kg y usar recursos de la zona. Agua de mar
2.000 (no pasa), aire 1.000 (no pasa), materia orgánica 2.500 (pasa y sale de los residuos
agrícolas), petróleo 10.000 y gas 9.300 (pasan, pero no son de la zona) → A.
"""
from bio3 import *   # noqa: F401,F403  (configura la misión y EST)
from bio3 import rot, caja, pista, renglon, frase_hueco, flecha, parrafo


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 8, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


def cuadro(b, x, y, w, h, txt, c, size=15, bold=False):
    caja(b, x, y, w, h, c, sw=2, r=6)
    lines = [" ".join(l) for l in wrap_px(txt, size, w - 16, "700" if bold else "400")]
    y0 = y + h / 2 - (len(lines) - 1) * (size + 3) / 2 + size * 0.35
    for k, ln in enumerate(lines):
        b.append(T(x + w / 2, y0 + k * (size + 3), [ln], size, INK, weight="700" if bold else "400",
                   anchor="middle"))


# ───────── QA · N.º 94 · eutrofización ─────────
def datos_94(b, x, y, w):
    c = INK
    cx = x + 420
    top = y + 6
    bw, bh = 230, 50
    # fila de arriba
    arriba = (("Crecimiento de bacterias fotosintéticas", cx - 300), ("Toxicidad algal", cx),
              ("Riesgos sanitarios", cx + 300))
    for t, px in arriba:
        cuadro(b, px - bw / 2, top, bw, bh, t, GRAY)
        b.append(line(px, top + bh, px, top + bh + 22, GRAY, 2))
    b.append(line(cx - 300, top + bh + 22, cx + 300, top + bh + 22, GRAY, 2))
    b.append(line(cx, top + bh + 22, cx, top + bh + 36, GRAY, 2))
    ey = top + bh + 36
    cuadro(b, cx - 130, ey, 260, 42, "Eutrofización", GRAY, size=17, bold=True)
    b.append(line(cx, ey + 42, cx, ey + 58, GRAY, 2))
    b.append(line(cx - 180, ey + 58, cx + 180, ey + 58, GRAY, 2))
    abajo = (("Sustracción del oxígeno disuelto para tomar fosfatos y nitratos", cx - 180,
              "Mortalidad de peces"),
             ("Pérdida de la calidad del agua", cx + 180, "Olor y sabor desagradable"))
    for t, px, t2 in abajo:
        b.append(line(px, ey + 58, px, ey + 72, GRAY, 2))
        cuadro(b, px - 150, ey + 72, 300, 62, t, GRAY)
        b.append(line(px, ey + 134, px, ey + 150, GRAY, 2))
        cuadro(b, px - 120, ey + 150, 240, 44, t2, GRAY)
    yy = ey + 200
    b.append(T(x + w, top + 20, ["Esquema de la eutrofización"], 14, GRAY, style="italic", anchor="end"))
    return pregunta(b, x, yy, w, "Con base en este esquema, se puede afirmar que una de las consecuencias de la "
                                 "eutrofización en un lago es")


def ii1(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "La cuenta del oxígeno en el lago", c,
                      "Lo del humedal: busca la condición que falta. Haz la cuenta del oxígeno del agua: qué lo pone y "
                      "qué lo gasta cuando sobran nutrientes.")
    x0, ww = x + 22, w - 44
    half = (ww - 24) / 2
    for k, (rt, ps) in enumerate((("LE PONE OXÍGENO AL AGUA", "¿quién lo produce o de dónde entra?"),
                                  ("LE GASTA OXÍGENO AL AGUA", "¿quién lo respira o lo usa al descomponer?"))):
        px = x0 + k * (half + 24)
        caja(b, px, yy, half, 120, c, r=14)
        rot(b, px + 18, yy + 28, rt, c, size=14)
        pista(b, px + 18, yy + 52, ps)
        renglon(b, px + 18, yy + 102, px + half - 18)
    yy += 136
    return frase_hueco(b, x0, yy, ww, "A los peces los limita el ____________ , porque se lo gastan "
                                      "______________________ .", c)


# ───────── QB · N.º 116 · moléculas de un ser vivo que muere ─────────
def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "La rueda de la materia después de la muerte", c,
                      "Lo de la sabana: los hongos también son parte de la red. Sigue lo que pasa con el cuerpo de "
                      "un ser vivo que nadie se comió, estación por estación, hasta que vuelve a empezar.")
    x0, ww = x + 22, w - 44
    cx, cy, R = x0 + ww / 2, yy + 190, 150
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{R}" fill="none" stroke="{c}" stroke-width="2.4" '
             f'stroke-dasharray="10,8"/>')
    rot(b, cx, cy + 6, "LA MATERIA", c, size=15, anchor="middle")
    est = (("1 · UN SER VIVO MUERE", "¿qué moléculas tenía su cuerpo?", -1, -1),
           ("2 · ¿QUIÉN LO APROVECHA?", "nadie se lo comió… ¿entonces quién?", 1, -1),
           ("3 · ¿EN QUÉ LO CONVIERTE?", "¿qué queda en el suelo?", 1, 1),
           ("4 · ¿QUIÉN LO VUELVE A USAR?", "¿y para qué?", -1, 1))
    bw, bh = 400, 112
    for rt, ps, sx, sy in est:
        bx = cx + sx * (R + 30) - (bw if sx < 0 else 0)
        by = cy + sy * 46 - (bh if sy < 0 else 0)
        caja(b, bx, by, bw, bh, c, r=14)
        rot(b, bx + 18, by + 28, rt, c, size=14)
        pista(b, bx + 18, by + 52, ps)
        renglon(b, bx + 18, by + 92, bx + bw - 18)
        ax = cx + sx * R * 0.72
        ay = cy + sy * R * 0.72
        b.append(f'<circle cx="{ax:.0f}" cy="{ay:.0f}" r="7" fill="{c}"/>')
    for k in range(4):
        a1 = math.radians(-135 + k * 90 + 18)
        a2 = math.radians(-135 + k * 90 + 72)
        b.append(hand_arrow(cx + R * math.cos(a1), cy + R * math.sin(a1), cx + R * math.cos(a2),
                            cy + R * math.sin(a2), c, sw=2.6, bend=-0.18, head=12))
    yy = cy + R + 20
    return frase_hueco(b, x0, yy, ww, "¿La materia se detiene en alguna estación de tu rueda? ¿En cuál? "
                                      "______________________", c)


# ───────── QC · N.º 67 · fuentes de energía ─────────
FUENTES = (("Agua de mar (agua salada)", "Osmótica", "Sales inorgánicas (NaCl, KCl...) y H2O", "2.000"),
           ("Aire", "Eólica", "N2, O2, Ar, CO2, Ne, He, H2O", "1.000"),
           ("Materia orgánica en descomposición", "Química", "Materia orgánica y microorganismos", "2.500"),
           ("Petróleo", "Química", "Combinación de hidrocarburos (alcanos, alquenos, alquinos...)", "10.000"),
           ("Gas natural", "Química", "Propano (C3H8)", "9.300"))


def datos_67(b, x, y, w):
    c = GRAY
    cols = (("Fuente", 330), ("Tipo de energía", 170), ("Composición", 560), ("Poder calorífico (kcal/kg)", 190))
    yy = y + 4
    px = x
    for t, cw in cols:
        caja(b, px, yy, cw, 40, c, sw=1.6, r=0, fill=SOFT)
        b.append(T(px + cw / 2, yy + 26, [t], 15, INK, weight="700", anchor="middle"))
        px += cw
    yy += 40
    for fila in FUENTES:
        px = x
        for (t, cw), v in zip(cols, fila):
            caja(b, px, yy, cw, 36, c, sw=1.6, r=0)
            b.append(T(px + cw / 2, yy + 24, [v], 15, INK, anchor="middle"))
            px += cw
        yy += 36
    return pregunta(b, x, yy + 6, w, "Si los habitantes de una zona agrícola cercana al mar desean instalar una "
                                     "planta de energía que produzca más de 2.100 kcal/kg y que aproveche los recursos "
                                     "de la zona, la mejor estrategia es")


def ii3(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "La raya de los 2.100 kcal/kg", c,
                      "Lo de las parcelas: los números deciden. Pon cada fuente como un punto en la regla y escribe "
                      "su nombre encima. Después encierra en un círculo las que sí hay en una zona agrícola junto al "
                      "mar.")
    x0, ww = x + 22, w - 44
    ly = yy + 70
    L, R_ = x0 + 30, x0 + ww - 30
    b.append(line(L, ly, R_, ly, INK, 2.6))
    for v in range(0, 10001, 1000):
        px = L + v / 10000 * (R_ - L)
        b.append(line(px, ly - 8, px, ly + 8, INK, 2))
        b.append(T(px, ly + 30, [f"{v // 1000}.000" if v else "0"], 14, GRAY, anchor="middle"))
    cut = L + 2100 / 10000 * (R_ - L)
    b.append(line(cut, ly - 54, cut, ly + 12, c, 3, dash="8,6"))
    b.append(T(cut + 8, ly - 40, ["2.100"], 15, c, weight="700"))
    pista(b, R_, ly + 54, "kcal/kg", anchor="end")
    yy = ly + 72
    return frase_hueco(b, x0, yy, ww, "Pasan la raya y además están en la zona: ______________________ .", c)


# ───────── QD · N.º 59 · purificación con luz ─────────
PROCESOS = (("I", "Un sistema de bombeo transporta el agua desde una quebrada cercana hasta un tanque de "
                  "recolección, donde se regula su caudal."),
            ("II", "El agua se dirige hacia una torre de aireación donde se oxigena."),
            ("III", "El agua se pasa a un tanque poco profundo donde la luz solar, particularmente la luz "
                    "ultravioleta, elimina una parte de las bacterias presentes."))


def datos_59(b, x, y, w):
    yy = y + 4
    for n, t in PROCESOS:
        b.append(T(x + 10, yy + 20, [n], 19, INK, weight="700"))
        svg, yy = TJ(x + 60, yy, t, w - 60, 19, INK, lh=26)
        b.append(svg)
        yy += 4
    return pregunta(b, x, yy, w, "¿Por qué el proceso III debe realizarse en un tanque poco profundo?")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Hasta dónde llega la luz", c,
                      "Lo de las pilas: la decisión sale de lo que le pasa al ser vivo. Dibuja con rayitas hasta "
                      "dónde baja la luz del sol en cada tanque y marca con puntos dónde quedan bacterias vivas.")
    x0, ww = x + 22, w - 44
    # sol
    sx, sy = x0 + 60, yy + 50
    b.append(f'<circle cx="{sx}" cy="{sy}" r="26" fill="{AMBER_BG}" stroke="{AMBER_D}" stroke-width="2.4"/>')
    for k in range(8):
        a = math.radians(k * 45)
        b.append(line(sx + 34 * math.cos(a), sy + 34 * math.sin(a), sx + 46 * math.cos(a), sy + 46 * math.sin(a),
                      AMBER_D, 2.4))
    tanques = (("TANQUE HONDO", 240, 250), ("TANQUE POCO PROFUNDO", 240, 90))
    tx = x0 + 130
    for k, (rt, tw_, th) in enumerate(tanques):
        px = tx + k * (tw_ + 50)
        top = yy + 70
        rot(b, px + tw_ / 2, top - 14, rt, c, size=13, anchor="middle")
        b.append(f'<path d="M {px} {top} L {px} {top + th} L {px + tw_} {top + th} L {px + tw_} {top}" '
                 f'fill="none" stroke="{c}" stroke-width="3"/>')
        b.append(line(px + 4, top + 14, px + tw_ - 4, top + 14, AZ, 2, dash="10,6"))
    rx = tx + 2 * 240 + 50 + 40
    rw = x0 + ww - rx
    caja(b, rx, yy + 40, rw, 150, c, r=14)
    rot(b, rx + 18, yy + 68, "EN EL FONDO DE CADA TANQUE", c, size=14)
    b.append(T(rx + 18, yy + 104, ["hondo: la luz"], 16, INK))
    b.append(T(rx + 18, yy + 150, ["poco profundo: la luz"], 16, INK))
    for j, yb in enumerate((yy + 88, yy + 134)):
        for i, lab in enumerate(("llega", "no llega")):
            bx_ = rx + 190 + i * 110
            b.append(checkbox(bx_, yb, s=10, c=c))
            b.append(T(bx_ + 26, yb + 16, [lab], 15, GRAY))
    yy += 340
    return frase_hueco(b, x0, yy, ww, "Si el tanque fuera hondo, las bacterias del fondo ______________________ .",
                       c)


QA = dict(est=3, comp="Uso comprensivo del conocimiento científico",
          e="Un ecosistema eutrofizado se caracteriza por una abundancia anormalmente alta de nutrientes. El "
            "esquema muestra la eutrofización de un cuerpo de agua.",
          o=["el aumento de la competencia por el alimento entre las especies del lago, porque desaparecen los "
             "productores.",
             "la reducción del espacio en el lago para el desplazamiento, porque los nutrientes ocupan todo el lago.",
             "la reducción del oxígeno disuelto para el metabolismo de los peces, porque este es consumido por "
             "microorganismos del lago.",
             "la reducción de la tasa fotosintética de las algas, porque hay menos peces herbívoros en el lago."],
          datos=datos_94, inst=ii1)
QB = dict(est=2, comp="Explicación de fenómenos",
          e="En la nutrición, los elementos biogeoquímicos se integran a los organismos y forman moléculas orgánicas "
            "necesarias para la supervivencia. ¿Qué sucede con las moléculas orgánicas de un ser vivo que muere por "
            "causas distintas de la depredación?",
          o=["Siguen como moléculas porque no pueden descomponerse.",
             "Salen del ecosistema porque deben ingresar nuevos elementos al medio.",
             "Se acumulan porque ya no pueden usarlas otros organismos.",
             "Se descomponen porque sirven de alimento a microorganismos."],
          inst=ii2)
QC = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="Actualmente está investigándose la manera de aprovechar materias primas renovables para producir "
            "energía, con el objetivo de sustituir las materias primas convencionales. En la siguiente tabla se "
            "comparan varias fuentes de energía.",
          o=["aprovechar la materia orgánica en descomposición que se produce de los residuos agrícolas.",
             "extraer petróleo de pozos petroleros alejados y transportarlo hasta la zona agrícola para producir "
             "grandes cantidades de energía.",
             "usar los distintos componentes del aire y transformarlos en energía mediante una reacción química.",
             "emplear un recurso renovable como el agua de mar para transformarlo en energía osmótica."],
          datos=datos_67, inst=ii3)
QD = dict(est=4, comp="Explicación de fenómenos",
          e="Una planta de purificación de agua para cultivos de hortalizas va a instalarse en una vereda. En la "
            "planta ocurren tres procesos:",
          o=["Porque permite que haya menor caudal de agua.",
             "Porque se forman menos grumos de material sólido.",
             "Porque el agua adquiere menor densidad.",
             "Porque hay mayor exposición del agua a la luz."],
          datos=datos_59, inst=ii4)


def build(pages=(156, 160)):
    return [hoja_icfes("bio3_i1", pages[0], QA, QB),
            hoja_icfes("bio3_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
