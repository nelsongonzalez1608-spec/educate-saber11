#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 6 · componente entorno químico · páginas 218–224. Cierre del área.

Libro fuente: «PRUEBA DE CAMPO MISIÓN 6» de Química (fuente_libro/QUÍMICA), páginas 193–196.
Contenido: reacciones químicas y energía. Metal en ácido clorhídrico (1), gasolina, etanol y
biogás como combustibles (2 a 4), un polímero casero de gel y almidón (5 a 7), neutralización
(8), oxidación de un clavo (9) y el pH de un queso a tres temperaturas (10).

Claves verificadas (resueltas a mano contra el texto, la gráfica y las ecuaciones del libro,
7 nov 2026):

    1·B  2·C  3·C  4·A  5·B  6·B  7·D  8·A  9·A  10·C

  1 · B: la curva sube 3 °C por cada 2 g hasta unos 8 g y se aplana cerca de 12–13 °C: el ácido
      se agota y ya no hay reacción que libere calor. A y D aceptan el «indefinidamente»; C niega
      que haya reacción (el metal reacciona con el HCl). Errata de la figura: el eje x dice
      0, 2, 3, 6, 8… (el «3» debe ser 4: las marcas están igual de separadas). No cambia la clave.
  2 · C: el biogás libera menos energía POR MOL (–890 frente a –1367 y –5470 kJ/mol) y es
      renovable. A dice «siempre» y «sin desventajas» (el texto le pone CO2 alto); B, que el
      etanol no necesita oxígeno (la combustión siempre lo necesita); D, «equivalentes».
      Hallazgo (Media): comparar por mol moléculas de tamaños tan distintos engaña; por gramo el
      metano da 890/16 ≈ 55,6 kJ/g, más que la gasolina (≈ 5470/114 ≈ 48 kJ/g) y el etanol
      (1367/46 ≈ 29,7 kJ/g).
  3 · C: 1 C2H5OH → 2 CO2; 2 mol → 4 mol de CO2. (Balance: C 2=2 · H 6=6 · O 1+6 = 4+3 = 7.)
      D (6) es el agua de 2 mol (2 × 3).
  4 · A: la segunda postura suma criterios (energía por mol, carácter renovable) que la primera
      dejó por fuera. B («basta»), C («equivalentes») y D (la ley de conservación no decide
      cuál combustible conviene) no se sostienen.
  5 · B, dentro del modelo que usa el libro. Hallazgo (Alta): la PVP del gel y el almidón YA
      son polímeros; al amasarlos no ocurre una polimerización, se forma una red de cadenas unidas
      por atracciones entre ellas (puentes de hidrógeno). La «baba» no es «un nuevo polímero».
  6 · B, dentro del mismo modelo. Con la química real, la D («mezcla física… sin cambio real»)
      tiene una parte defendible (no hay enlaces nuevos entre átomos), aunque «sin cambio real» es
      falso (cambian las propiedades). Registrado con la 5.
  7 · D: «se estira más» es elongación; «resistente» es la fuerza que aguanta antes de romperse.
      La conclusión usa una sola propiedad. A («siempre»), B (las variables sí se controlaron)
      y C («suficiente»). Hallazgo (Media): el texto dice que las tres muestras se prepararon
      igual y no dice qué cambió entre ellas; si nada cambió, las diferencias serían error.
  8 · A: la temperatura subió → se liberó energía → exotérmica. Formar el enlace H–O del agua
      libera energía. B dice endotérmica con temperatura que sube; C y D niegan el cambio.
  9 · A: 56 g de Fe = 1 mol (masa molar 56 g/mol). 4 Fe → 2 Fe2O3, o sea 1 mol Fe → 0,5 mol
      Fe2O3. Masa molar de Fe2O3 = 2 × 56 + 3 × 16 = 160 g/mol → 0,5 × 160 = 80 g.
      D (160) es 1 mol de óxido; B y C no salen de ninguna cuenta con la ecuación.
 10 · C: 4 °C → 6,0 · 20 °C → 5,2 · 35 °C → 4,8: a más temperatura, menor pH; los
      investigadores usan la bajada del pH como indicador de descomposición. A (no se puede
      concluir nada), B (error experimental) y D (solo depende de la leche) no se sostienen.
      Atención: una sola medición por temperatura, sin repeticiones.

Reparto: A 3 · B 3 · C 3 · D 1. La D sale una sola vez. Registrado como Atención.

Estrategias (la 1 y la 3 recogen lo trabajado en el área: contar átomos y moles en la Misión 5
y leer tablas y conclusiones en todas las misiones):
    1 · La ecuación es una receta                       (1, 3, 9  · ICFES 2.ª ses. N.º 68)   azul
    2 · ¿El calor sale o entra?                         (2, 8     · ICFES pendiente)         rojo
    3 · Una conclusión vale lo que valen sus datos      (4, 7, 10 · ICFES pendiente)         morado
    4 · Piezas que se repiten: los polímeros            (5, 6     · ICFES pendiente)         oro

Hojas: 218 qui6_t1 (1-2) · 219 qui6_t2 (3-4) · 220 qui6_i1 · 221 qui6_t3 (5-6) ·
       222 qui6_t4 (7-8) · 223 qui6_t5 (9-10) · 224 qui6_i2.
"""
from taller_base import *

configurar("Química", 6, "entorno químico",
           tema="Reacciones que calientan, que oxidan y que encadenan",
           nota="LO QUE OBSERVÉ Y SUBRAYÉ")
MORADO = "#5B3E96"
EST = {1: ("La ecuación es una receta", EDU_AZUL),
       2: ("¿El calor sale o entra?", EDU_ROJO),
       3: ("Una conclusión vale lo que valen sus datos", MORADO),
       4: ("Piezas que se repiten: los polímeros", EDU_ORO)}
usar_estrategias(EST)
AZ, RO, MO, OR = (EST[k][1] for k in (1, 2, 3, 4))


# ───────── piezas pequeñas ─────────
def rot(b, x, y, txt, c, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, c, weight="700", ls=1.5, anchor=anchor))


def caja(b, x, y, w, h, c, sw=2, fill="white", r=10, dash=None):
    b.append(rect(x, y, w, h, fill, r=r, stroke=c, sw=sw, dash=dash))


def pista(b, x, y, txt, size=15, anchor="start"):
    b.append(T(x, y, [txt], size, GRAY, style="italic", anchor=anchor))


def renglon(b, x1, y, x2):
    b.append(line(x1, y, x2, y, LGRAY, 2))


def texto(b, x, y, txt, size=17, color=INK, weight="400", anchor="start"):
    b.append(T(x, y, [txt], size, color, weight=weight, anchor=anchor))


def sino(b, x, y, c, labels=("sí", "no"), gap=80):
    for j, lab in enumerate(labels):
        b.append(checkbox(x + j * gap, y, s=10, c=c))
        b.append(T(x + 28 + j * gap, y + 17, [lab], 16, GRAY))


def frase_hueco(b, x, y, w, txt, c, h=54, size=18):
    caja(b, x, y, w, h, c)
    b.append(T(x + 22, y + h / 2 + 7, [txt], size, INK, weight="700"))
    return y + h


def tinte(c, k=0.9):
    from taller_base import _mezcla
    return _mezcla(c, k)


def flecha(b, x1, y1, x2, y2, c, sw=2.6, head=12, bend=0.0):
    b.append(hand_arrow(x1, y1, x2, y2, c, sw=sw, bend=bend, head=head))


def tabla_vacia(b, x, y, cols, heads, filas, c, rh=58, hh=48, size=17, sin_renglon=()):
    ww = sum(cols)
    caja(b, x, y, ww, hh, c, fill=tinte(c), r=8)
    cx = x
    for k, hd in enumerate(heads):
        if hd:
            rot(b, cx + 14, y + hh / 2 + 6, hd, c, size=14)
        cx += cols[k]
    ry = y + hh
    for f in filas:
        caja(b, x, ry, ww, rh, c, r=0)
        texto(b, x + 14, ry + rh / 2 + 6, f, size=size, weight="700")
        cx = x + cols[0]
        for k in range(1, len(cols)):
            if k not in sin_renglon:
                renglon(b, cx + 14, ry + rh - 16, cx + cols[k] - 14)
            cx += cols[k]
        ry += rh
    cx = x
    for k in range(len(cols) - 1):
        cx += cols[k]
        b.append(line(cx, y, cx, ry, c, 1.6))
    return ry


def ejes(b, gx, gy, gw, gh, xs, ys, xlab, ylab, c_grid="#E3E8EF"):
    """Rejilla con marcas igual de separadas; xs, ys = rótulos de las marcas."""
    for i, v in enumerate(xs):
        xx = gx + i * gw / (len(xs) - 1)
        b.append(line(xx, gy, xx, gy + gh, c_grid, 1.4))
        texto(b, xx, gy + gh + 24, v, size=15, color=GRAY, anchor="middle")
    for j, v in enumerate(ys):
        yv = gy + gh - j * gh / (len(ys) - 1)
        b.append(line(gx, yv, gx + gw, yv, c_grid, 1.4))
        texto(b, gx - 10, yv + 5, v, size=15, color=GRAY, anchor="end")
    b.append(line(gx, gy, gx, gy + gh, INK, 2))
    b.append(line(gx, gy + gh, gx + gw, gy + gh, INK, 2))
    pista(b, gx + gw / 2, gy + gh + 50, xlab, anchor="middle")
    b.append(T(gx - 52, gy + gh / 2, [ylab], 15, GRAY, style="italic", anchor="middle", rot=-90))


# ───────── P1 · metal en ácido · dónde se aplana ─────────
def i1(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Dónde se aplana la curva", c,
                      "La gráfica del libro, con el eje bien numerado. Lee cuánto sube la temperatura en el tramo "
                      "recto y dónde deja de subir. Después piensa en el metal y el ácido como los ingredientes de "
                      "una receta.")
    x0, ww = x + 22, w - 44
    gx, gy, gw, gh = x0 + 70, yy + 16, 560, 330
    caja(b, x0, yy, 670, gh + 96, c, r=16)
    ejes(b, gx, gy, gw, gh, [str(v) for v in range(0, 15, 2)], [str(v) for v in range(0, 15, 2)],
         "masa de metal (g)", "aumento de temperatura (°C)")
    pts = ((0, 0), (2, 3), (4, 6), (6, 9), (8, 11), (10, 12), (12, 12.5), (14, 12.7))
    P = lambda m, t: (gx + m / 14 * gw, gy + gh - t / 14 * gh)
    b.append('<polyline points="' + " ".join(f"{P(m, t)[0]:.1f},{P(m, t)[1]:.1f}" for m, t in pts) +
             f'" fill="none" stroke="{EDU_ORO}" stroke-width="3"/>')
    for m, t in pts:
        px, py = P(m, t)
        b.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="{EDU_ORO}"/>')
    rx, rw = x0 + 700, ww - 700
    qs = (("TRAMO RECTO", "cada 2 g de metal, la temperatura sube ____ °C"),
          ("DONDE SE APLANA", "desde unos ____ g casi no sube; ¿por qué?"),
          ("SI AGREGO 30 GRAMOS", "la temperatura subiría a… ¿y por qué no más?"))
    for k, (tit, ps) in enumerate(qs):
        py = yy + k * 142
        caja(b, rx, py, rw, 128, c, r=14)
        rot(b, rx + 16, py + 28, tit, c, size=14)
        svg, _ = TJ(rx + 16, py + 54, ps, rw - 32, 16, INK, lh=22)
        b.append(svg)
        renglon(b, rx + 16, py + 110, rx + rw - 16)
    yy += gh + 116
    return ojo(b, x0, yy, ww, "LA FIGURA DEL LIBRO TIENE UNA ERRATA EN EL EJE",
               "En el libro el eje de la masa dice 0, 2, 3, 6, 8… Las marcas están igual de separadas, así que ese "
               "«3» es un 4. Aquí está corregido. La forma de la curva no cambia.")


# ───────── P2 · ficha técnica de tres combustibles ─────────
def i2(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "La ficha técnica de tres combustibles", c,
                      "Llena la ficha solo con lo que dice el texto del libro. Una afirmación «explica mejor las "
                      "diferencias» si cada parte suya coincide con una casilla de tu ficha.")
    x0, ww = x + 22, w - 44
    cols = (330, (ww - 330) / 3, (ww - 330) / 3, (ww - 330) / 3)
    filas = ("Energía por mol (kJ/mol)", "¿Cuál libera más? (1.º, 2.º, 3.º)", "Emisiones de CO₂",
             "Almacenamiento", "¿Es renovable?")
    yy = tabla_vacia(b, x0, yy, cols, ("", "GASOLINA", "ETANOL", "BIOGÁS (METANO)"), filas, c, rh=60, size=16)
    yy += 20
    yy = frase_hueco(b, x0, yy, ww, "El signo menos en «–890 kJ/mol» quiere decir que el calor ______________ .", c)
    yy += 16
    return alto_profe(b, x0, yy, ww,
                      "Comparar por mol o por gramo. Un mol de gasolina pesa unos 114 gramos y un mol de metano, apenas "
                      "16. Pídele al profe que divida la energía entre la masa de un mol: el orden de los combustibles "
                      "puede cambiar. La pregunta se responde con lo que dice el texto, por mol.")


# ───────── P3 · seguir a los carbonos ─────────
def i3(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "Sigue a los carbonos del etanol", c,
                      "Cada átomo de carbono del etanol termina dentro de una molécula de CO₂. Dibuja dos "
                      "moléculas de etanol como bolitas (● carbono) y une cada carbono con su CO₂. Luego confirma "
                      "con la receta.")
    x0, ww = x + 22, w - 44
    texto(b, x0, yy + 28, "C₂H₅OH  +  3 O₂  →  2 CO₂  +  3 H₂O", size=26, weight="700")
    yy += 52
    half = (ww - 80) / 2
    for k, (tit, ps) in enumerate((("ANTES · 2 MOLÉCULAS DE ETANOL", "dibuja los carbonos de cada una"),
                                   ("DESPUÉS · LAS MOLÉCULAS DE CO₂", "dibuja un CO₂ por cada carbono"))):
        bx = x0 + k * (half + 80)
        caja(b, bx, yy, half, 300, c, r=16, dash="8,6" if k else None)
        rot(b, bx + 18, yy + 30, tit, c, size=14)
        pista(b, bx + 18, yy + 54, ps)
    flecha(b, x0 + half + 10, yy + 150, x0 + half + 70, yy + 150, c, sw=3.4, head=14)
    yy += 320
    cols = (300, (ww - 300) / 4, (ww - 300) / 4, (ww - 300) / 4, (ww - 300) / 4)
    yy = tabla_vacia(b, x0, yy, cols, ("RECETA EN MOLES", "C₂H₅OH", "O₂", "CO₂", "H₂O"),
                     ("1 vez la receta", "2 veces la receta"), c, rh=58)
    yy += 18
    return trampa(b, x0, yy, ww, "Un número bien multiplicado puede ser de la sustancia equivocada:",
                  "en la fila de «2 veces la receta» salen varios números. Antes de marcar, mira el encabezado de la "
                  "columna: la pregunta es por el CO₂.", c)


# ───────── P4 · criterios del foro ─────────
def i4(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "¿Con cuántos criterios se decidió?", c,
                      "La pregunta del foro pedía tres cosas: eficiencia, impacto ambiental y viabilidad. Revisa qué "
                      "criterios usó cada grupo y qué dicen los datos del libro sobre ellos.")
    x0, ww = x + 22, w - 44
    cols = (330, 190, 190, ww - 710)
    filas = ("Emisiones de CO₂", "Energía por mol", "¿Es renovable?", "Almacenamiento")
    yy0 = yy
    yy = tabla_vacia(b, x0, yy, cols, ("CRITERIO", "GRUPO 1", "GRUPO 2", "LO QUE DICE EL DATO DEL ETANOL"),
                     filas, c, rh=62, sin_renglon=(1, 2))
    for k in range(4):
        ry = yy0 + 48 + k * 62
        for j in range(2):
            bx = x0 + 330 + j * 190 + 30
            sino(b, bx, ry + 20, c, labels=("lo usó", "no"), gap=90)
    yy += 20
    caja(b, x0, yy, ww, 136, c, r=14)
    rot(b, x0 + 20, yy + 30, "EL VEREDICTO", c)
    pista(b, x0 + 20, yy + 66, "de los tres que pedía el foro, el grupo 1 usó ___ y el grupo 2 usó ___")
    pista(b, x0 + 20, yy + 108, "una conclusión es suficiente cuando…")
    renglon(b, x0 + 280, yy + 110, x0 + ww - 20)
    yy += 154
    return ojo(b, x0, yy, ww, "UNA LEY CIERTA NO SIEMPRE ES EL CRITERIO QUE SE PIDE",
               "Todos los combustibles conservan la masa y la energía, como toda reacción. Por eso esa ley no sirve "
               "para elegir entre ellos: lo que los distingue está en tu tabla.")


# ───────── P5 · del polvo y el gel a la baba ─────────
def i5(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Del polvo y el gel a la baba que se estira", c,
                      "Describe cada material con lo que verías y tocarías en la cocina. Si la baba tiene propiedades "
                      "que no tenía ningún ingrediente, pregúntate qué pudo pasar entre las moléculas al amasar.")
    x0, ww = x + 22, w - 44
    cols = (300, (ww - 300) / 3, (ww - 300) / 3, (ww - 300) / 3)
    filas = ("¿Cómo se ve?", "¿Fluye o se sostiene?", "¿Se estira?", "¿Se evapora algo?")
    yy = tabla_vacia(b, x0, yy, cols, ("", "GEL (PVP)", "HARINA DE MAÍZ", "LA BABA"), filas, c, rh=58)
    yy += 20
    caja(b, x0, yy, ww, 170, c, r=14)
    rot(b, x0 + 20, yy + 30, "DIBUJA LAS MOLÉCULAS", c)
    pw = (ww - 80) / 3
    for k, t_ in enumerate(("en el gel", "en la harina", "en la baba")):
        bx = x0 + 20 + k * (pw + 20)
        caja(b, bx, yy + 46, pw, 108, c, r=10, dash="6,5")
        pista(b, bx + 12, yy + 70, t_)
    yy += 188
    return alto_profe(b, x0, yy, ww,
                      "Polímero: una molécula larguísima hecha de una pieza que se repite. Ojo: la PVP del gel y el "
                      "almidón ya son polímeros. Pídele al profe que explique qué pasa entre esas cadenas cuando se "
                      "amasan juntas, y si eso es formar un polímero nuevo.")


# ───────── P6 · una cuenta no es un collar ─────────
def i6(b, x, y, w, h):
    c = OR
    yy = titulo_instr(b, x, y, "Una cuenta no es un collar", c,
                      "Un collar está hecho de cuentas, pero se dobla, se enreda y cuelga: eso no lo hace una cuenta "
                      "sola. Compara una pieza suelta con la cadena que forma.")
    x0, ww = x + 22, w - 44
    # cuenta suelta y collar
    caja(b, x0, yy, ww, 170, c, r=16)
    rot(b, x0 + 20, yy + 30, "UNA PIEZA", c, size=14)
    b.append(f'<circle cx="{x0 + 90}" cy="{yy + 100}" r="22" fill="{tinte(c, 0.7)}" stroke="{c}" stroke-width="2.4"/>')
    rot(b, x0 + 260, yy + 30, "LA CADENA", c, size=14)
    for i in range(16):
        cx = x0 + 280 + i * 54
        cy = yy + 100 + 26 * math.sin(i / 2.2)
        if i:
            b.append(line(cx - 54, yy + 100 + 26 * math.sin((i - 1) / 2.2), cx, cy, c, 2))
    for i in range(16):
        cx = x0 + 280 + i * 54
        cy = yy + 100 + 26 * math.sin(i / 2.2)
        b.append(f'<circle cx="{cx}" cy="{cy:.1f}" r="16" fill="{tinte(c, 0.7)}" stroke="{c}" stroke-width="2"/>')
    yy += 190
    cols = (380, (ww - 380) / 2, (ww - 380) / 2)
    filas = ("¿De qué átomos está hecha?", "¿Cómo están organizadas?", "¿Puede estirarse o enredarse?",
             "¿Tiene las mismas propiedades?")
    yy = tabla_vacia(b, x0, yy, cols, ("", "UNA PIEZA SUELTA", "LA CADENA LARGA"), filas, c, rh=58, size=16)
    yy += 20
    return frase_hueco(b, x0, yy, ww, "Los mismos átomos pueden dar propiedades distintas si cambia ______________ .", c)


# ───────── P7 · estirarse no es resistir ─────────
def i7(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Estirarse no es lo mismo que resistir", c,
                      "Ordena el experimento en tres columnas. Después separa dos propiedades que la conclusión "
                      "mezcla: cuánto se estira un material y cuánta fuerza aguanta antes de romperse.")
    x0, ww = x + 22, w - 44
    cw_ = (ww - 40) / 3
    cols_ = (("LO QUE SE MANTUVO IGUAL", "variables controladas", 3),
             ("LO QUE CAMBIÓ ENTRE MUESTRAS", "¿lo dice el texto?", 2),
             ("LO QUE SE MIDIÓ", "con qué unidad", 2))
    for k, (tit, ps, n) in enumerate(cols_):
        bx = x0 + k * (cw_ + 20)
        caja(b, bx, yy, cw_, 220, c, r=14, dash="8,6" if k == 1 else None)
        rot(b, bx + 16, yy + 30, tit, c, size=14)
        pista(b, bx + 16, yy + 56, ps)
        for r_ in range(n):
            renglon(b, bx + 16, yy + 104 + r_ * 44, bx + cw_ - 16)
    yy += 240
    half = (ww - 30) / 2
    for k, (tit, ps) in enumerate((("ELONGACIÓN", "cuánto se alarga antes de romperse · se mide en cm"),
                                   ("RESISTENCIA", "cuánta fuerza aguanta antes de romperse · se mide con un peso"))):
        bx = x0 + k * (half + 30)
        caja(b, bx, yy, half, 150, c, r=14)
        rot(b, bx + 16, yy + 30, tit, c, size=14)
        pista(b, bx + 16, yy + 56, ps)
        pista(b, bx + 16, yy + 100, "¿la midió el estudiante?")
        sino(b, bx + 200, yy + 84, c)
        pista(b, bx + 16, yy + 136, "ejemplo de la vida diaria:")
        renglon(b, bx + 200, yy + 138, bx + half - 16)
    yy += 168
    return ojo(b, x0, yy, ww, "UN CHICLE SE ESTIRA MUCHO Y AGUANTA POCO",
               "Una cuerda de acero casi no se estira y aguanta muchísimo. Antes de marcar, compara la palabra que usó "
               "el estudiante con lo que de verdad midió.")


# ───────── P8 · escalón de energía ─────────
def i8(b, x, y, w, h):
    c = RO
    yy = titulo_instr(b, x, y, "El escalón de energía de la neutralización", c,
                      "En el diagrama, la altura es la energía guardada en las sustancias. Los reactivos ya están "
                      "dibujados. Dibuja el escalón de los productos (más arriba o más abajo) según lo que marcó el "
                      "termómetro, y la flecha del calor.")
    x0, ww = x + 22, w - 44
    dw = 660
    caja(b, x0, yy, dw, 380, c, r=16)
    ax, ay = x0 + 60, yy + 30
    b.append(line(ax, ay, ax, ay + 300, INK, 2))
    b.append(line(ax, ay + 300, ax + dw - 100, ay + 300, INK, 2))
    b.append(T(ax - 26, ay + 150, ["energía guardada"], 15, GRAY, style="italic", anchor="middle", rot=-90))
    pista(b, ax + 250, ay + 326, "avance de la reacción", anchor="middle")
    b.append(line(ax + 30, ay + 140, ax + 210, ay + 140, INK, 4))
    texto(b, ax + 120, ay + 128, "HCl + NaOH", size=17, weight="700", anchor="middle")
    b.append(line(ax + 260, ay + 40, ax + 260, ay + 280, "#E3E8EF", 2, "6,6"))
    pista(b, ax + 280, ay + 60, "productos: NaCl + H₂O")
    pista(b, ax + 280, ay + 82, "dibuja aquí su escalón")
    rx, rw = x0 + dw + 30, ww - dw - 30
    qs = (("EL TERMÓMETRO", "la temperatura de la solución…"),
          ("EL CALOR VA…", "de las sustancias hacia el agua, o del agua hacia ellas"),
          ("SE LLAMA…", "exotérmica / endotérmica, porque…"))
    for k, (tit, ps) in enumerate(qs):
        py = yy + k * 124
        caja(b, rx, py, rw, 110, c, r=14)
        rot(b, rx + 16, py + 28, tit, c, size=14)
        svg, _ = TJ(rx + 16, py + 52, ps, rw - 32, 15, GRAY, style="italic", lh=20)
        b.append(svg)
        renglon(b, rx + 16, py + 94, rx + rw - 16)
    yy += 400
    return alto_profe(b, x0, yy, ww,
                      "Energía de enlace: en una reacción unos enlaces se rompen y otros se forman, y en cada paso la "
                      "energía entra o sale. Pídele al profe que lo explique con la formación del agua (H⁺ + OH⁻ → "
                      "H₂O) y que lo relacione con lo que marcó el termómetro.")


# ───────── P9 · puente gramos → moles → gramos ─────────
def i9(b, x, y, w, h):
    c = AZ
    yy = titulo_instr(b, x, y, "El puente gramos, moles, gramos", c,
                      "La ecuación cuenta en moles, pero la balanza pesa en gramos. Cruza el puente paso a paso: "
                      "de gramos de hierro a moles, de moles de hierro a moles de óxido, y de vuelta a gramos.")
    x0, ww = x + 22, w - 44
    texto(b, x0, yy + 28, "4 Fe  +  3 O₂  →  2 Fe₂O₃", size=26, weight="700")
    pista(b, x0 + 420, yy + 26, "masas molares: Fe = 56 g/mol · O = 16 g/mol")
    yy += 50
    pasos = (("1 · GRAMOS DE Fe", "56 g", "dato del libro"),
             ("2 · MOLES DE Fe", None, "56 g ÷ 56 g/mol"),
             ("3 · MOLES DE Fe₂O₃", None, "por cada 4 Fe salen ___ Fe₂O₃"),
             ("4 · GRAMOS DE Fe₂O₃", None, "moles × masa molar"))
    pw = (ww - 3 * 34) / 4
    for k, (tit, val, ps) in enumerate(pasos):
        bx = x0 + k * (pw + 34)
        caja(b, bx, yy, pw, 170, c, r=14, fill=tinte(c, 0.94) if val else "white")
        rot(b, bx + 14, yy + 28, tit, c, size=13)
        if val:
            texto(b, bx + 14, yy + 92, val, size=30, weight="700")
        else:
            renglon(b, bx + 14, yy + 104, bx + pw - 14)
        svg, _ = TJ(bx + 14, yy + 134, ps, pw - 28, 15, GRAY, style="italic", lh=20)
        b.append(svg)
        if k < 3:
            flecha(b, bx + pw + 3, yy + 85, bx + pw + 31, yy + 85, c, head=10)
    yy += 190
    caja(b, x0, yy, ww, 110, c, r=14)
    rot(b, x0 + 20, yy + 30, "MASA MOLAR DEL Fe₂O₃", c)
    texto(b, x0 + 20, yy + 80, "2 × ____ g  +  3 × ____ g  =  ______ g/mol", size=22, weight="700")
    yy += 128
    return trampa(b, x0, yy, ww, "La masa molar del óxido no es la respuesta:",
                  "es lo que pesa UN mol de Fe₂O₃. Mira tu paso 3: ¿cuántos moles de óxido salen de verdad con 56 g "
                  "de hierro?", c)


# ───────── P10 · tres quesos ─────────
def i10(b, x, y, w, h):
    c = MO
    yy = titulo_instr(b, x, y, "Tres quesos, tres temperaturas, una tendencia", c,
                      "Ubica los tres datos del libro en la gráfica y únelos. Luego separa lo que se midió de lo que "
                      "los investigadores interpretan con esa medida.")
    x0, ww = x + 22, w - 44
    gx, gy, gw, gh = x0 + 80, yy + 16, 500, 300
    caja(b, x0, yy, 620, gh + 96, c, r=16)
    ejes(b, gx, gy, gw, gh, ["0", "10", "20", "30", "40"], ["4,5", "5,0", "5,5", "6,0", "6,5"],
         "temperatura (°C)", "pH final")
    rx, rw = x0 + 650, ww - 650
    qs = (("LO QUE SE MIDIÓ", "una variable que cambia y otra que se mide"),
          ("LA TENDENCIA", "cuando la temperatura sube, el pH…"),
          ("LO QUE SE INTERPRETA", "¿qué significa, según el texto, que el pH baje?"))
    for k, (tit, ps) in enumerate(qs):
        py = yy + k * 134
        caja(b, rx, py, rw, 120, c, r=14)
        rot(b, rx + 16, py + 28, tit, c, size=14)
        svg, _ = TJ(rx + 16, py + 52, ps, rw - 32, 15, GRAY, style="italic", lh=20)
        b.append(svg)
        renglon(b, rx + 16, py + 102, rx + rw - 16)
    yy += gh + 116
    return ojo(b, x0, yy, ww, "LO QUE RECOGE TODA EL ÁREA",
               "Ante cualquier conclusión, pregunta: ¿qué se midió?, ¿qué tendencia muestran los datos?, ¿cuántas "
               "mediciones hay?, ¿la interpretación la dicen los datos o la dicen los investigadores? Anota tus "
               "respuestas antes de leer las opciones.")


Q = {1: dict(n=1, est=1, pag=193, ctx="Metal en ácido clorhídrico · por qué deja de calentar",
             comp="Explicación de fenómenos", inst=i1),
     2: dict(n=2, est=2, pag=194, ctx="Gasolina, etanol y biogás · diferencias entre combustibles",
             comp="Explicación de fenómenos", inst=i2),
     3: dict(n=3, est=1, pag=194, ctx="Combustión del etanol · moles de CO₂",
             comp="Uso comprensivo del conocimiento científico", inst=i3),
     4: dict(n=4, est=3, pag=194, ctx="El foro de los combustibles · qué conclusión basta",
             comp="Indagación", inst=i4),
     5: dict(n=5, est=4, pag=195, ctx="Polímero casero de gel y almidón · qué explica el cambio",
             comp="Explicación de fenómenos", inst=i5),
     6: dict(n=6, est=4, pag=195, ctx="Polímero y sus componentes · qué relación hay",
             comp="Uso comprensivo del conocimiento científico", inst=i6),
     7: dict(n=7, est=3, pag=195, ctx="Tres muestras que se estiran · ¿la más resistente?",
             comp="Indagación", inst=i7),
     8: dict(n=8, est=2, pag=196, ctx="Ácido clorhídrico e hidróxido de sodio · por qué se calienta",
             comp="Explicación de fenómenos", inst=i8),
     9: dict(n=9, est=1, pag=196, ctx="Un clavo que se oxida · masa de óxido de hierro",
             comp="Uso comprensivo del conocimiento científico", inst=i9),
     10: dict(n=10, est=3, pag=196, ctx="pH de un queso a tres temperaturas · el análisis pertinente",
              comp="Indagación", inst=i10)}


def build(pages=(218, 219, 221, 222, 223)):
    out = []
    for k, (a, b_) in enumerate(((1, 2), (3, 4), (5, 6), (7, 8), (9, 10))):
        out.append(hoja_taller(f"qui6_t{k + 1}", pages[k], k + 1, Q[a], Q[b_]))
    return out


if __name__ == "__main__":
    for f in build():
        print("ok", f)
