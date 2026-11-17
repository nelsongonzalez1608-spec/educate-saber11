"""Conceptualización de Matemáticas (ver conceptos.py). Por ahora, Misión 1: la prueba que pidió Nelson
el 17 nov. Las ideas van en el orden de las estrategias del cuaderno (tablero/misiones.csv) y con su color.

Los ejemplos son propios: no repiten datos de las 10 preguntas del libro ni de las 4 de entrenamiento,
para que la conceptualización no resuelva el taller por adelantado.
"""

TINTA, GRIS, LINEA = "#1E2230", "#6E7480", "#C9D1DC"
F = 'font-family="Carlito, Calibri, Arial, sans-serif"'


def _svg(cuerpo, alt, w=420, h=300):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{alt}">'
            f'<ellipse cx="{w/2}" cy="{h-14}" rx="{w*0.42}" ry="10" fill="{TINTA}" opacity=".07"/>{cuerpo}</svg>')


def escalera(c):
    """Razón de cambio: escalones isométricos iguales (avanza 1, sube 2)."""
    s = ""
    for k in range(3):
        x, top = 70 + 90 * k, 230 - 60 * (k + 1)
        s += (f'<polygon points="{x},250 {x+90},250 {x+90},{top} {x},{top}" fill="#EEF2F8" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<polygon points="{x+90},250 {x+112},236 {x+112},{top-14} {x+90},{top}" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2.5"/>'
              f'<polygon points="{x},{top} {x+90},{top} {x+112},{top-14} {x+22},{top-14}" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>')
    s += (f'<line x1="92" y1="156" x2="182" y2="156" stroke="{c}" stroke-width="5" stroke-dasharray="10 7"/>'
          f'<line x1="182" y1="156" x2="182" y2="96" stroke="#E4572E" stroke-width="5"/>'
          f'<text x="120" y="146" {F} font-size="22" fill="{c}" font-weight="700">+1</text>'
          f'<text x="192" y="132" {F} font-size="22" fill="#E4572E" font-weight="700">+2</text>')
    return _svg(s, "Escalones iguales: cada uno avanza 1 y sube 2")


def parabola(c):
    s = (f'<line x1="40" y1="262" x2="380" y2="262" stroke="{LINEA}" stroke-width="2"/>'
         f'<path d="M60 262 Q210 -60 360 262" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
         f'<line x1="210" y1="101" x2="210" y2="262" stroke="{GRIS}" stroke-width="2" stroke-dasharray="7 6"/>'
         f'<circle cx="210" cy="101" r="12" fill="#C9821B" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<text x="228" y="92" {F} font-size="22" fill="{TINTA}" font-weight="700">vértice</text>'
         f'<path d="M98 210 L128 160" stroke="#30843C" stroke-width="5" stroke-linecap="round"/>'
         f'<path d="M128 160 L112 166 M128 160 L128 177" stroke="#30843C" stroke-width="5" stroke-linecap="round"/>'
         f'<path d="M292 160 L322 210" stroke="#A82424" stroke-width="5" stroke-linecap="round"/>'
         f'<path d="M322 210 L322 193 M322 210 L306 203" stroke="#A82424" stroke-width="5" stroke-linecap="round"/>'
         f'<text x="62" y="150" {F} font-size="20" fill="#30843C">sube</text>'
         f'<text x="318" y="150" {F} font-size="20" fill="#A82424">baja</text>')
    return _svg(s, "Parábola que sube, llega al vértice y baja")


def recta(c):
    s = (f'<line x1="60" y1="262" x2="390" y2="262" stroke="{LINEA}" stroke-width="2"/>'
         f'<line x1="60" y1="262" x2="60" y2="30" stroke="{LINEA}" stroke-width="2"/>'
         f'<rect x="60" y="182" width="16" height="80" fill="#30843C" opacity=".25"/>'
         f'<line x1="60" y1="182" x2="380" y2="62" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
         f'<circle cx="60" cy="182" r="10" fill="#fff" stroke="{c}" stroke-width="4"/>'
         f'<text x="84" y="214" {F} font-size="22" fill="{TINTA}" font-weight="700">lo fijo (b)</text>')
    for k in range(3):
        x, y = 140 + 80 * k, 152 - 30 * k
        s += (f'<path d="M{x} {y} L{x+80} {y} L{x+80} {y-30}" fill="none" stroke="#C9821B" stroke-width="3.5"/>')
    s += f'<text x="236" y="168" {F} font-size="22" fill="#C9821B" font-weight="700">lo que crece (m)</text>'
    return _svg(s, "Recta que arranca en un valor fijo y sube lo mismo en cada paso")


def modelo(c):
    caja = (f'<polygon points="150,110 270,110 270,200 150,200" fill="#fff" stroke="{TINTA}" stroke-width="2.5"/>'
            f'<polygon points="270,110 292,96 292,186 270,200" fill="#F3E3C6" stroke="{TINTA}" stroke-width="2.5"/>'
            f'<polygon points="150,110 270,110 292,96 172,96" fill="#FBF3E4" stroke="{TINTA}" stroke-width="2.5"/>'
            f'<text x="210" y="164" text-anchor="middle" {F} font-size="26" fill="{c}" font-weight="700">modelo</text>')
    s = (caja +
         f'<text x="50" y="162" {F} font-size="34" fill="{TINTA}" font-weight="700">x</text>'
         f'<text x="352" y="162" {F} font-size="34" fill="{TINTA}" font-weight="700">y</text>'
         f'<path d="M78 136 L140 136" stroke="#242478" stroke-width="4"/><path d="M140 136 L130 130 M140 136 L130 142" stroke="#242478" stroke-width="4"/>'
         f'<path d="M300 136 L342 136" stroke="#242478" stroke-width="4"/><path d="M342 136 L332 130 M342 136 L332 142" stroke="#242478" stroke-width="4"/>'
         f'<path d="M342 218 L80 218" stroke="#30843C" stroke-width="4" stroke-dasharray="8 6"/><path d="M80 218 L90 212 M80 218 L90 224" stroke="#30843C" stroke-width="4"/>'
         f'<text x="60" y="66" {F} font-size="20" fill="#242478" font-weight="700">1 evaluar →</text>'
         f'<text x="60" y="256" {F} font-size="20" fill="#30843C" font-weight="700">← 2 despejar</text>'
         f'<text x="250" y="256" {F} font-size="20" fill="#A82424" font-weight="700">3 ¿qué significa?</text>')
    return _svg(s, "Un modelo con tres preguntas: evaluar, despejar, interpretar")


def patron(c):
    vals = [5, 7, 11, 19, 35]
    s = f'<line x1="40" y1="262" x2="390" y2="262" stroke="{LINEA}" stroke-width="2"/>'
    for k, v in enumerate(vals):
        x, h = 60 + 66 * k, v * 6
        s += (f'<rect x="{x}" y="{262-h}" width="40" height="{h}" fill="#F7E3E3" stroke="{c}" stroke-width="2.5"/>'
              f'<polygon points="{x+40},{262} {x+50},{256} {x+50},{256-h} {x+40},{262-h}" fill="#E9C4C4" stroke="{c}" stroke-width="2"/>'
              f'<text x="{x+20}" y="{254-h}" text-anchor="middle" {F} font-size="20" fill="{TINTA}" font-weight="700">{v}</text>')
        if k:
            s += (f'<text x="{x-13}" y="290" text-anchor="middle" {F} font-size="18" fill="#C9821B" '
                  f'font-weight="700">+{v - vals[k-1]}</text>')
    return _svg(s, "Barras 5, 7, 11, 19, 35: las diferencias 2, 4, 8, 16 se duplican", h=300)


def _m1(ESTR, EST_COL):
    col = EST_COL[1]
    centro_svg = escalera("#242478")
    ideas = {
        "Subir, llegar y volver": dict(
            corto="la parábola y su punto más alto",
            d="Una cantidad que sube, llega a un punto donde deja de subir (el vértice) y vuelve a bajar. "
              "En el vértice está el máximo.",
            f="y = ax² + bx + c   (a negativa: abre hacia abajo)",
            ej="la altura de un balón pateado: sube, se detiene un instante arriba y cae.",
            ojo="estar subiendo no es lo mismo que estar arriba. Y la curva es simétrica: lo que pasa un "
                "segundo antes del vértice se repite un segundo después.",
            svg=parabola),
        "Lo fijo y lo que crece": dict(
            corto="la recta: arranque + ritmo",
            d="Lo fijo es lo que hay desde el principio, aunque no avances (el intercepto). Lo que crece es "
              "lo que se suma por cada unidad (la pendiente).",
            f="y = b + m·x",
            ej="un parqueadero cobra $3.000 por entrar y $1.500 por hora: y = 3.000 + 1.500x.",
            ojo="si la tabla sube siempre lo mismo, es una recta. Si dos planes se cruzan, en ese punto "
                "cuestan igual.",
            svg=recta),
        "Un modelo, tres preguntas": dict(
            corto="evaluar, despejar, interpretar",
            d="Un modelo es la fórmula que cuenta una situación. Siempre se le pueden hacer tres preguntas: "
              "me dan x y busco y; me dan y y busco x; o ¿qué significa este número?",
            f="evaluar → · ← despejar · ¿qué significa?",
            ej="con el parqueadero: ¿cuánto pago por 4 horas? (evaluar) · pagué $12.000, ¿cuántas horas? "
               "(despejar) · ¿qué es el 1.500? (interpretar).",
            ojo="antes de hacer cuentas, decide cuál de las tres te están preguntando. Y mira el dominio: "
                "no hay horas negativas.",
            svg=modelo),
        "El patrón que continúa": dict(
            corto="restar términos seguidos",
            d="Antes de buscar una fórmula, resta cada término con el anterior. Si la resta es siempre la "
              "misma, el patrón es lineal; si la resta se duplica, hay una potencia de 2.",
            f="5 · 7 · 11 · 19 · 35   →   restas 2 · 4 · 8 · 16",
            ej="aquí las restas se duplican: la regla es aₙ = 2ⁿ + 3. Compruébala con n = 1 y n = 2.",
            ojo="una fórmula del término general se prueba siempre con los primeros términos antes de marcar.",
            svg=patron),
    }
    lista = []
    for k, nombre in enumerate(ESTR[1]):
        i = dict(ideas[nombre], t=nombre)
        i["svg"] = i["svg"](col[k])
        lista.append(i)
    return {1: dict(
        titulo="Todo lo que cambia tiene un ritmo",
        centro=("Razón de cambio",
                "cuánto cambia una cantidad por cada unidad que avanza la otra", centro_svg),
        centro_ej="un taxi pasa de $9.000 a $15.000 entre el km 2 y el km 5: cambia $6.000 en 3 km, "
                  "$2.000 por km.",
        centro_ojo="dividir 15.000 entre 5 mezcla el arranque con el ritmo. La razón es cambio sobre cambio.",
        ideas=lista,
        vocab=[("Variable", "lo que cambia (x, y)"),
               ("Constante", "lo que no cambia"),
               ("Razón de cambio", "cuánto cambia por cada unidad"),
               ("Pendiente", "la razón de cambio de una recta"),
               ("Intercepto", "dónde arranca: el valor cuando x = 0"),
               ("Vértice", "el punto más alto o más bajo de la parábola"),
               ("Sucesión", "números en orden que siguen una regla"),
               ("Término general", "la regla que da el término de la posición n"),
               ("Dominio", "los valores de x que tienen sentido")],
        decir=["«Lo que acaban de descubrir tiene nombre». Toca la tarjeta del centro: razón de cambio.",
               "Abre solo la tarjeta de la estrategia 1: es la que vamos a entrenar ya en la dinámica. Las "
               "demás se abren cuando aparezcan en el taller: vuelve a esta diapositiva con ← cuando haga falta.",
               "Una frase por tarjeta, nada más. Si alguien pregunta algo largo: «lo vemos en la pregunta "
               "que toca»."],
        apoyo=["Las fórmulas están para reconocerlas, no para memorizarlas hoy.",
               "Los ejemplos son propios de la guía: no son los del libro, para que no resuelvan el taller "
               "por adelantado.",
               "La conceptualización se toma 3 de los 15 minutos de la Activación. Si la activación se "
               "alargó, pasa directo a la dinámica: el mapa sigue disponible para el cierre."])}
    return DATOS.get(mis)


# ══════════════════════ figuras de las misiones 2 a 6 ══════════════════════
def _t(x, y, s, size=22, c=TINTA, anchor="start", w="700"):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" {F} font-size="{size}" fill="{c}" font-weight="{w}">{s}</text>'


def _caja(x, y, w, h, d, cara="#fff", lado="#D3DCEA", tapa="#EEF2F8", sw=2.5):
    """Caja isométrica: frente (x, y, w, h) y fondo desplazado d hacia arriba a la derecha."""
    k = d * 0.6
    return (f'<polygon points="{x},{y} {x+w},{y} {x+w},{y+h} {x},{y+h}" fill="{cara}" stroke="{TINTA}" stroke-width="{sw}"/>'
            f'<polygon points="{x+w},{y} {x+w+d},{y-k} {x+w+d},{y+h-k} {x+w},{y+h}" fill="{lado}" stroke="{TINTA}" stroke-width="{sw}"/>'
            f'<polygon points="{x},{y} {x+d},{y-k} {x+w+d},{y-k} {x+w},{y}" fill="{tapa}" stroke="{TINTA}" stroke-width="{sw}"/>')


def _flecha(x1, y1, x2, y2, c, sw=4):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    p1 = (x2 - 14 * math.cos(a - 0.45), y2 - 14 * math.sin(a - 0.45))
    p2 = (x2 - 14 * math.cos(a + 0.45), y2 - 14 * math.sin(a + 0.45))
    return (f'<path d="M{x1} {y1} L{x2} {y2} M{p1[0]:.1f} {p1[1]:.1f} L{x2} {y2} L{p2[0]:.1f} {p2[1]:.1f}" '
            f'fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>')


def curva_puntos(c):
    """Centro M2: una tabla de datos que se vuelve curva."""
    pts = [(70, 230), (130, 150), (190, 110), (250, 110), (310, 150), (370, 230)]
    s = f'<line x1="40" y1="262" x2="390" y2="262" stroke="{LINEA}" stroke-width="2"/>'
    s += f'<path d="M70 230 Q220 -10 370 230" fill="none" stroke="{c}" stroke-width="5" stroke-dasharray="10 8"/>'
    for x, y in pts:
        s += f'<circle cx="{x}" cy="{y}" r="11" fill="#fff" stroke="{c}" stroke-width="4"/>'
    return _svg(s, "Datos de una tabla que dibujan una curva")


def techo(c):
    s = (f'<line x1="50" y1="262" x2="390" y2="262" stroke="{LINEA}" stroke-width="2"/>'
         f'<line x1="50" y1="262" x2="50" y2="30" stroke="{LINEA}" stroke-width="2"/>'
         f'<path d="M70 250 Q220 -40 370 250" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
         f'<line x1="50" y1="105" x2="220" y2="105" stroke="#C9821B" stroke-width="3" stroke-dasharray="8 6"/>'
         f'<line x1="220" y1="105" x2="220" y2="262" stroke="#30843C" stroke-width="3" stroke-dasharray="8 6"/>'
         f'<circle cx="220" cy="105" r="12" fill="#C9821B" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(62, 92, "cuánto vale", 20, "#C9821B") + _t(228, 290, "dónde (t)", 20, "#30843C"))
    return _svg(s, "Parábola con su techo: dónde se alcanza y cuánto vale", h=300)


def refutar(c):
    s = ""
    for k, (txt, ok) in enumerate([("t = 1 → sube", True), ("t = 2 → sube", True), ("t = 4 → baja", False)]):
        y = 40 + k * 76
        col = "#30843C" if ok else "#A82424"
        s += (f'<rect x="60" y="{y}" width="300" height="58" rx="12" fill="#fff" stroke="{col}" stroke-width="3"/>'
              + _t(84, y + 38, txt, 24, TINTA, w="600"))
        s += (f'<path d="M318 {y+30} l10 10 l18 -20" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round"/>'
              if ok else f'<path d="M318 {y+18} l22 22 M340 {y+18} l-22 22" stroke="{col}" stroke-width="5" stroke-linecap="round"/>')
    s += _t(210, 280, "un solo caso basta", 22, "#A82424", "middle")
    return _svg(s, "Tres casos revisados: uno solo contradice la afirmación", h=300)


def aumento(c):
    s = f'<line x1="40" y1="262" x2="390" y2="262" stroke="{LINEA}" stroke-width="2"/>'
    for k in range(5):
        x, h = 60 + 66 * k, 70 + 36 * k
        s += _caja(x, 262 - h, 38, h, 12, "#EAF4EC", "#C3DEC8", "#F5FAF6")
        if k:
            s += _t(x + 18, 262 - h - 18, "+36", 18, "#C9821B", "middle")
    return _svg(s, "Barras que suben siempre lo mismo en cada periodo", h=300)


def tabla_datos(c):
    filas = [("día", "hecho", "vendido"), ("1", "120", "118"), ("2", "160", "131"), ("3", "140", "139")]
    s = ""
    for i, f in enumerate(filas):
        y = 40 + i * 54
        fondo = "#F3EEF8" if i == 0 else ("#FBEFEF" if i == 2 else "#fff")
        for j, v in enumerate(f):
            x = 50 + j * 110
            s += f'<rect x="{x}" y="{y}" width="110" height="54" fill="{fondo}" stroke="{LINEA}" stroke-width="2"/>'
            s += _t(x + 55, y + 35, v, 22, TINTA if i else c, "middle", "700" if i == 0 else "500")
    s += f'<rect x="50" y="148" width="330" height="54" fill="none" stroke="#A82424" stroke-width="4" rx="4"/>'
    s += _t(215, 292, "hecho no es vendido", 22, "#A82424", "middle")
    return _svg(s, "Tabla de producción y ventas: una fila marcada donde se hizo más de lo que se vendió", h=300)


def medidas(c):
    s = (f'<line x1="40" y1="200" x2="120" y2="200" stroke="{c}" stroke-width="7" stroke-linecap="round"/>'
         + _t(80, 240, "1 D", 22, c, "middle")
         + f'<rect x="150" y="140" width="70" height="70" fill="#FDF5E7" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(185, 240, "2 D", 22, c, "middle")
         + _caja(270, 140, 70, 70, 34, "#FDF5E7", "#F1DDB8", "#FFFBF2")
         + _t(320, 240, "3 D", 22, c, "middle")
         + _t(210, 70, "m · m² · m³", 26, TINTA, "middle"))
    return _svg(s, "Longitud, área y volumen: una, dos y tres dimensiones", h=300)


def piezas(c):
    s = (_caja(110, 140, 180, 110, 50, "#EEF2F8", "#D3DCEA", "#F7F9FC")
         + f'<polygon points="110,140 290,140 340,110 160,110" fill="#F7F9FC" stroke="{TINTA}" stroke-width="2.5"/>'
         + f'<polygon points="110,140 225,40 290,140" fill="#FDF5E7" stroke="{TINTA}" stroke-width="2.5"/>'
         + f'<polygon points="290,140 225,40 340,110" fill="#F1DDB8" stroke="{TINTA}" stroke-width="2.5"/>'
         + _t(200, 210, "prisma", 22, c, "middle") + _t(232, 118, "pirámide", 18, "#C9821B", "middle"))
    return _svg(s, "Un cuerpo partido en un prisma y una pirámide encima", h=300)


def sombras(c):
    s = (f'<line x1="30" y1="250" x2="400" y2="250" stroke="{LINEA}" stroke-width="2"/>'
         f'<polygon points="80,250 80,190 160,250" fill="#EAF4EC" stroke="{c}" stroke-width="3"/>'
         f'<line x1="80" y1="250" x2="80" y2="190" stroke="{TINTA}" stroke-width="6"/>'
         f'<polygon points="200,250 200,100 400,250" fill="#EAF4EC" stroke="{c}" stroke-width="3"/>'
         f'<line x1="200" y1="250" x2="200" y2="100" stroke="{TINTA}" stroke-width="8"/>'
         f'<circle cx="40" cy="45" r="22" fill="#C9821B" opacity=".85"/>'
         + _t(120, 285, "sombra", 18, GRIS, "middle") + _t(300, 285, "sombra", 18, GRIS, "middle")
         + _t(192, 180, "altura", 18, TINTA, "end", "600") + _t(72, 225, "altura", 16, TINTA, "end", "600"))
    return _svg(s, "Dos objetos y sus sombras forman triángulos semejantes", h=300)


def baldosas(c):
    s = ""
    for i in range(6):
        for j in range(4):
            s += (f'<rect x="{80 + i*44}" y="{50 + j*44}" width="44" height="44" fill="{"#FBEFEF" if (i+j)%2 else "#fff"}" '
                  f'stroke="{c}" stroke-width="2"/>')
    s += (f'<rect x="80" y="50" width="264" height="176" fill="none" stroke="{TINTA}" stroke-width="3"/>'
          + _t(212, 262, "área total ÷ área de una baldosa", 20, TINTA, "middle", "600"))
    return _svg(s, "Un rectángulo cubierto con baldosas iguales", h=300)


def estante(c):
    s = (f'<rect x="40" y="90" width="340" height="12" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2"/>'
         f'<rect x="40" y="200" width="340" height="12" fill="#D3DCEA" stroke="{TINTA}" stroke-width="2"/>')
    for k in range(4):
        s += _caja(48 + k * 72, 128, 64, 72, 0, "#FDF5E7")
    s += (f'<rect x="336" y="128" width="40" height="72" fill="none" stroke="#A82424" stroke-width="3" stroke-dasharray="6 5"/>'
          + _t(210, 250, "mide antes de mover", 22, c, "middle"))
    return _svg(s, "Estante con cuatro cajas y un espacio libre medido", h=300)


def triangulo(c, rot=True):
    s = (f'<polygon points="40,250 320,250 320,70" fill="#F3EEF8" stroke="{TINTA}" stroke-width="3"/>'
         f'<rect x="296" y="226" width="24" height="24" fill="none" stroke="{TINTA}" stroke-width="2.5"/>'
         f'<path d="M90 250 A50 50 0 0 0 84 222" fill="none" stroke="#C9821B" stroke-width="4"/>'
         + _t(98, 240, "θ", 24, "#C9821B"))
    if rot:
        s += (_t(180, 285, "adyacente", 20, "#30843C", "middle") + _t(330, 170, "opuesto", 20, "#A82424")
              + _t(150, 140, "hipotenusa", 20, c, "middle"))
    return _svg(s, "Triángulo rectángulo con el ángulo θ y sus lados nombrados", h=300)


def escala(c):
    s = _caja(60, 190, 40, 40, 20, "#EEF2F8") + _t(80, 270, "×1", 22, c, "middle")
    for i in range(2):
        for j in range(2):
            s += _caja(200 + i * 70, 90 + j * 70, 70, 70, 36, "#EEF2F8")
    s += _t(270, 270, "lado ×2 · volumen ×8", 22, c, "middle")
    return _svg(s, "Un cubo pequeño y uno con el doble de lado", h=300)


def cilindro(c):
    s = (f'<path d="M120 80 L120 220 A90 26 0 0 0 300 220 L300 80" fill="#E6F4F1" stroke="{TINTA}" stroke-width="3"/>'
         f'<ellipse cx="210" cy="80" rx="90" ry="26" fill="#F5FBFA" stroke="{TINTA}" stroke-width="3"/>'
         f'<line x1="210" y1="80" x2="300" y2="80" stroke="{c}" stroke-width="4"/>'
         f'<line x1="330" y1="80" x2="330" y2="220" stroke="#C9821B" stroke-width="4"/>'
         + _t(255, 70, "r", 24, c, "middle") + _t(342, 160, "h", 24, "#C9821B"))
    return _svg(s, "Cilindro con su radio y su altura", h=300)


def lupa(c, lineas=("paso 1", "paso 2", "paso 3")):
    s = ""
    for k, txt in enumerate(lineas):
        y = 50 + k * 64
        s += (f'<rect x="50" y="{y}" width="230" height="48" rx="10" fill="#fff" stroke="{LINEA}" stroke-width="2.5"/>'
              + _t(70, y + 32, txt, 20, TINTA, w="600"))
    s += (f'<circle cx="300" cy="170" r="52" fill="#fff" fill-opacity=".6" stroke="{c}" stroke-width="7"/>'
          f'<line x1="338" y1="208" x2="380" y2="252" stroke="{c}" stroke-width="12" stroke-linecap="round"/>')
    return _svg(s, "Una lupa revisa paso por paso", h=300)


def histograma(c):
    s = f'<line x1="40" y1="250" x2="390" y2="250" stroke="{LINEA}" stroke-width="2"/>'
    for k, h in enumerate([60, 120, 180, 140, 80, 40]):
        s += _caja(60 + k * 54, 250 - h, 44, h, 10, "#E6F4F1", "#C2E3DC", "#F5FBFA")
    return _svg(s, "Histograma: muchos datos resumidos en barras")


def puntos_medidas(c):
    vals = [2, 3, 3, 4, 8]
    s = f'<line x1="40" y1="200" x2="390" y2="200" stroke="{LINEA}" stroke-width="3"/>'
    cuenta = {}
    for v in vals:
        cuenta[v] = cuenta.get(v, 0) + 1
        x = 40 + v * 40
        s += f'<circle cx="{x}" cy="{200 - cuenta[v]*30}" r="12" fill="{c}" opacity=".85"/>'
    for v in range(1, 9):
        s += _t(40 + v * 40, 230, str(v), 18, GRIS, "middle", "500")
    s += (f'<line x1="200" y1="60" x2="200" y2="200" stroke="#C9821B" stroke-width="3" stroke-dasharray="7 6"/>'
          + _t(206, 56, "media 4", 18, "#C9821B")
          + f'<line x1="160" y1="80" x2="160" y2="200" stroke="#30843C" stroke-width="3" stroke-dasharray="4 5"/>'
          + _t(152, 76, "mediana 3", 18, "#30843C", "end")
          + _t(215, 275, "un dato lejano (8) mueve la media", 18, TINTA, "middle", "600"))
    return _svg(s, "Cinco datos en una recta, con la media y la mediana marcadas", h=300)


def cuadricula(c):
    s = ""
    for k in range(100):
        i, j = k % 10, k // 10
        on = k < 25
        s += (f'<rect x="{110 + i*20}" y="{40 + j*20}" width="18" height="18" rx="3" '
              f'fill="{c if on else "#EEF2F8"}" opacity="{1 if on else 1}"/>')
    s += _t(210, 270, "25 de cada 100", 22, TINTA, "middle")
    return _svg(s, "Cien cuadritos con veinticinco coloreados: 25 por ciento", h=300)


def torta(c):
    import math
    s, a0 = "", -90
    for p, col in [(40, c), (25, "#C9821B"), (20, "#30843C"), (15, "#A82424")]:
        a1 = a0 + p * 3.6
        x0, y0 = 210 + 110 * math.cos(math.radians(a0)), 145 + 110 * math.sin(math.radians(a0))
        x1, y1 = 210 + 110 * math.cos(math.radians(a1)), 145 + 110 * math.sin(math.radians(a1))
        s += (f'<path d="M210 145 L{x0:.1f} {y0:.1f} A110 110 0 {1 if p > 50 else 0} 1 {x1:.1f} {y1:.1f} Z" '
              f'fill="{col}" opacity=".8" stroke="#fff" stroke-width="3"/>')
        a0 = a1
    return _svg(s, "Gráfico circular con cuatro sectores")


def cuatro_casos(c):
    s = ""
    for k, L in enumerate("ABCD"):
        x = 40 + k * 90
        s += (f'<rect x="{x}" y="80" width="74" height="90" rx="12" fill="#fff" stroke="{c}" stroke-width="3"/>'
              + _t(x + 37, 136, L, 34, c, "middle")
              + f'<rect x="{x+22}" y="190" width="30" height="30" rx="5" fill="#fff" stroke="{GRIS}" stroke-width="2.5"/>')
    s += _t(210, 270, "se prueban las cuatro", 22, TINTA, "middle")
    return _svg(s, "Cuatro opciones, cada una con su casilla para comprobar", h=300)


def dado(c):
    s = ""
    for k in range(6):
        x = 50 + (k % 3) * 110
        y = 50 + (k // 3) * 110
        on = (k + 1) % 2 == 0
        s += (f'<rect x="{x}" y="{y}" width="90" height="90" rx="16" fill="{"#F3EEF8" if on else "#fff"}" '
              f'stroke="{c if on else LINEA}" stroke-width="3"/>' + _t(x + 45, y + 60, str(k + 1), 36, c if on else GRIS, "middle"))
    return _svg(s, "Las seis caras de un dado con las tres pares resaltadas", h=300)


def casillas(c):
    s = ""
    for k, (n, lab) in enumerate([(6, "1.º"), (5, "2.º")]):
        x = 90 + k * 150
        s += (_caja(x, 90, 110, 110, 30, "#F3EEF8", "#DDD3EA", "#FAF7FD")
              + _t(x + 55, 162, str(n), 48, c, "middle") + _t(x + 55, 236, lab, 20, GRIS, "middle", "600"))
    s += _t(225, 160, "×", 36, TINTA, "middle") + _t(210, 280, "6 × 5 = 30", 24, TINTA, "middle")
    return _svg(s, "Dos casillas: seis opciones para la primera y cinco para la segunda", h=300)


def bolsa(c):
    s = (f'<path d="M90 90 Q80 250 170 250 Q260 250 250 90 Z" fill="#FAF7FD" stroke="{TINTA}" stroke-width="3"/>'
         f'<path d="M100 90 Q170 60 240 90" fill="none" stroke="{TINTA}" stroke-width="3"/>')
    for x, y, col in [(130, 160, "#30843C"), (175, 200, "#30843C"), (210, 150, "#30843C"),
                      (150, 215, "#C9821B"), (200, 115, "#C9821B")]:
        s += f'<circle cx="{x}" cy="{y}" r="18" fill="{col}" opacity=".85"/>'
    s += (_flecha(260, 140, 340, 100, c) + f'<circle cx="360" cy="90" r="18" fill="#30843C" opacity=".85"/>'
          + _t(350, 150, "no vuelve", 18, c, "middle"))
    return _svg(s, "Bolsa con cinco bolas; una sale y no vuelve", h=300)


def muestra(c):
    import random
    r = random.Random(7)
    s = f'<circle cx="210" cy="140" r="70" fill="#F3EEF8" stroke="{c}" stroke-width="3"/>'
    for _ in range(60):
        x, y = r.randint(40, 380), r.randint(30, 250)
        dentro = (x - 210) ** 2 + (y - 140) ** 2 < 66 ** 2
        s += f'<circle cx="{x}" cy="{y}" r="5" fill="{c if dentro else LINEA}"/>'
    s += _t(210, 285, "lo medido no es todo", 20, TINTA, "middle")
    return _svg(s, "Puntos de una población; solo los del círculo fueron medidos", h=300)


# ══════════════════════ los datos de las seis misiones ══════════════════════
# Cada idea: corto (rótulo del mapa), d (definición), f (fórmula o esquema), ej (ejemplo propio),
# ojo (el error típico), chequeo (la pregunta con la que el profe comprueba que quedó: va al planeador),
# svg (figura). Los ejemplos NO repiten datos del taller ni del entrenamiento.
CHEQUEO_M1 = {
    "Razón de cambio": "Un tanque tiene 20 litros a las 2 p. m. y 50 a las 5 p. m. ¿Cuántos litros entran por hora? (10)",
    "Subir, llegar y volver": "Un balón está a 12 m en el segundo 1 y a 12 m en el segundo 3. ¿En qué segundo llegó más alto? (en el 2: la curva es simétrica)",
    "Lo fijo y lo que crece": "En y = 8.000 + 1.200x, ¿cuál número es lo fijo y cuál lo que crece? (8.000 fijo; 1.200 por unidad)",
    "Un modelo, tres preguntas": "«¿Cuántas horas puedo parquear con $10.500?» ¿Evaluar, despejar o interpretar? (despejar)",
    "El patrón que continúa": "3, 6, 9, 12… ¿lineal o potencia? ¿Por qué? (lineal: la resta es siempre 3)",
}


def _m2a6():
    """{misión: dict(titulo, centro, centro_ej, centro_ojo, centro_chequeo, ideas{nombre: idea}, vocab)}"""
    return {
        2: dict(
            titulo="Lo que el modelo sí dice",
            centro=("Leer un modelo", "lo que una fórmula o una tabla dice de cómo cambia algo", curva_puntos),
            centro_ej="una tabla de alturas de un cohete de agua, segundo a segundo, dibuja una curva: sube, se "
                      "detiene y baja. La fórmula dice lo mismo con letras.",
            centro_ojo="las respuestas salen del modelo, no de lo que «parece lógico».",
            centro_chequeo="Si la tabla dice 10, 18, 22, 22, 18, ¿el valor más alto es el último? (no: está en el medio)",
            ideas={
                "Encontrar el techo": dict(
                    corto="dónde se alcanza y cuánto vale",
                    d="En una parábola que abre hacia abajo, el techo está en el vértice. Son dos datos "
                      "distintos: DÓNDE se alcanza (el valor de t) y CUÁNTO vale (lo que da la fórmula en ese t).",
                    f="t = −b ÷ (2a)",
                    ej="h(t) = −2t² + 12t: el techo está en t = −12 ÷ (2·(−2)) = 3, y vale −18 + 36 = 18.",
                    ojo="si preguntan cuándo, la respuesta es t; si preguntan cuánto, es la altura. Varias "
                        "opciones incorrectas son el otro dato.",
                    chequeo="En h(t) = −t² + 6t, ¿cuándo llega al techo y cuánto vale? (t = 3; vale 9)",
                    svg=techo),
                "Refutar con el modelo": dict(
                    corto="un solo dato que contradiga",
                    d="Para tumbar una afirmación basta un caso del propio modelo que la contradiga: un "
                      "contraejemplo. Refutar es hacer una cuenta, no dar una opinión.",
                    f="afirmación → busco un caso → ¿se cumple?",
                    ej="«con h(t) = −2t² + 12t la altura siempre sube»: en t = 3 vale 18 y en t = 4 vale 16. "
                       "Ya no siempre sube.",
                    ojo="«depende» o «no creo» no refutan nada: hay que mostrar el número.",
                    chequeo="«Todo número multiplicado por 2 da más que él mismo». ¿Qué número lo refuta? (0, o cualquier negativo)",
                    svg=refutar),
                "El aumento constante": dict(
                    corto="suma lo mismo cada periodo",
                    d="Si cada periodo se suma la misma cantidad, el crecimiento es lineal: el valor es lo "
                      "inicial más el aumento por el número de periodos.",
                    f="valor = inicial + aumento · n",
                    ej="una alcancía empieza con $40.000 y recibe $15.000 cada mes: a los 6 meses tiene "
                       "40.000 + 6 · 15.000 = $130.000.",
                    ojo="que un número sea grande no quiere decir que crezca más rápido: mira cuánto suma "
                        "cada periodo.",
                    chequeo="Una planta mide 4 cm y crece 3 cm por semana. ¿Cuánto mide en la semana 5? (19 cm)",
                    svg=aumento),
                "Los datos mandan": dict(
                    corto="la tabla decide, no la intuición",
                    d="Una decisión se justifica con los datos de la tabla, fila por fila. El ingreso neto es "
                      "lo que entra menos lo que costó.",
                    f="neto = ingreso − costo",
                    ej="se venden 50 empanadas a $2.000 ($100.000) y hacerlas costó $65.000: el neto es $35.000.",
                    ojo="producir más no es vender más: compara lo que se hizo con lo que se vendió en cada fila.",
                    chequeo="Si un día entraron $80.000 y se gastaron $95.000, ¿cuál fue el neto? (−$15.000: pérdida)",
                    svg=tabla_datos),
            },
            vocab=[("Modelo", "fórmula o tabla que describe una situación"),
                   ("Máximo", "el valor más alto que alcanza"),
                   ("Vértice", "el punto donde está el máximo de la parábola"),
                   ("Contraejemplo", "un caso que muestra que algo es falso"),
                   ("Refutar", "demostrar con datos que algo no es cierto"),
                   ("Crecimiento lineal", "suma lo mismo en cada periodo"),
                   ("Ingreso", "lo que entra por ventas"),
                   ("Costo", "lo que se gastó para producir"),
                   ("Ingreso neto", "ingreso menos costo")]),
        3: dict(
            titulo="Medir el espacio sin perderse",
            centro=("Medir el espacio", "longitud, área y volumen: una, dos y tres dimensiones", medidas),
            centro_ej="un cuadrado de 1 m de lado mide 100 cm de lado, pero 10.000 cm² de área; un cubo de 1 m "
                      "tiene 1.000.000 cm³.",
            centro_ojo="antes de cualquier cuenta, todas las medidas en la misma unidad. La mitad de los "
                       "errores de esta misión son metros contra centímetros.",
            centro_chequeo="¿Cuántos cm² tiene 1 m²? (10.000)",
            ideas={
                "Partir el cuerpo en piezas": dict(
                    corto="dividir en cuerpos conocidos",
                    d="Un cuerpo raro se parte en cuerpos conocidos; se calcula el volumen de cada pieza y se "
                      "suman. Prisma: área de la base por altura. Pirámide: un tercio de eso.",
                    f="prisma = base · h   ·   pirámide = ⅓ · base · h",
                    ej="una caja de 2 × 3 × 4 con techo de pirámide de altura 3: 24 + ⅓ · 6 · 3 = 24 + 6 = 30.",
                    ojo="la pirámide es un tercio del prisma con la misma base y altura, no el prisma entero.",
                    chequeo="Una pirámide de base 9 m² y altura 4 m, ¿qué volumen tiene? (12 m³)",
                    svg=piezas),
                "La misma razón para los dos": dict(
                    corto="semejanza: mismos ángulos, lados proporcionales",
                    d="Dos figuras semejantes tienen los mismos ángulos y sus lados están en la misma razón. "
                      "Con el sol, un objeto y su sombra forman triángulos semejantes con otro objeto y la suya.",
                    f="altura₁ ÷ sombra₁ = altura₂ ÷ sombra₂",
                    ej="un palo de 2 m da 3 m de sombra; a la misma hora un árbol da 12 m: mide 2 · 12 ÷ 3 = 8 m.",
                    ojo="altura : sombra y sombra : altura son razones distintas. Escríbela en el orden en que "
                        "la pregunta la nombra.",
                    chequeo="Si un poste de 4 m da 2 m de sombra, ¿cuánto vale la razón sombra : altura? (0,5)",
                    svg=sombras),
                "Cuántas veces cabe": dict(
                    corto="área total ÷ área de una pieza",
                    d="Para saber cuántas piezas cubren una superficie se divide el área total entre el área de "
                      "una pieza, con todo en la misma unidad. Un arco de circunferencia es una parte de 2πr.",
                    f="piezas = área total ÷ área de una   ·   circunferencia = 2πr",
                    ej="un patio de 3 m × 2 m con baldosas de 50 cm: 300 · 200 ÷ (50 · 50) = 24 baldosas.",
                    ojo="1 m = 100 cm, pero 1 m² = 10.000 cm². Pasa los lados a la misma unidad antes de "
                        "multiplicar.",
                    chequeo="¿Cuántas baldosas de 20 cm × 20 cm cubren 1 m²? (25)",
                    svg=baldosas),
                "Antes de mover, mide": dict(
                    corto="contar y medir antes de reorganizar",
                    d="Antes de reorganizar o encajar piezas se mide lo que hay: cuántas piezas, de qué "
                      "tamaño y cuánto espacio queda libre.",
                    f="espacio libre = espacio total − espacio ocupado",
                    ej="en un estante de 120 cm caben 4 cajas de 25 cm (100 cm) y sobran 20 cm, que no "
                       "alcanzan para una quinta.",
                    ojo="mover piezas en la cabeza sin medirlas es adivinar: primero los números, después el "
                        "movimiento.",
                    chequeo="En un estante de 90 cm, ¿cuántas cajas de 20 cm caben y cuánto sobra? (4; sobran 10 cm)",
                    svg=estante),
            },
            vocab=[("Área", "lo que cubre una superficie (m²)"),
                   ("Volumen", "el espacio que ocupa un cuerpo (m³)"),
                   ("Prisma", "cuerpo con dos bases iguales y paralelas"),
                   ("Pirámide", "cuerpo con una base y una punta"),
                   ("Semejanza", "misma forma, distinto tamaño"),
                   ("Razón", "la comparación de dos cantidades por división"),
                   ("Proporción", "dos razones iguales"),
                   ("Circunferencia", "el borde del círculo: mide 2πr"),
                   ("Unidad de medida", "en qué se mide: cm, m, cm², m³")]),
        4: dict(
            titulo="Medir lo que no se alcanza",
            centro=("Medir lo que no se alcanza",
                    "cuando no se puede medir directo, se mide con una escala o con un triángulo",
                    lambda c: triangulo(c, rot=False)),
            centro_ej="la altura de un edificio se calcula desde el piso con un ángulo y una distancia; la "
                      "distancia entre dos ciudades, con un mapa y su escala.",
            centro_ojo="siempre hay una figura detrás: dibújala y rotula lo que sabes antes de calcular.",
            centro_chequeo="¿Qué dos herramientas sirven para medir sin llegar? (la escala y el triángulo rectángulo)",
            ideas={
                "Dimensión por dimensión": dict(
                    corto="escala: longitud ×k, área ×k², volumen ×k³",
                    d="En una escala 1:k las longitudes se multiplican por k, las áreas por k² y los "
                      "volúmenes por k³: cada dimensión se escala una vez.",
                    f="longitud ×k   ·   área ×k²   ·   volumen ×k³",
                    ej="en un plano 1:200, un cuarto de 2 cm × 3 cm mide 4 m × 6 m: 24 m² de verdad.",
                    ojo="si multiplicas el área solo por k, te quedas corto: el área crece por k dos veces.",
                    chequeo="Si un cubo duplica su lado, ¿por cuánto se multiplica su volumen? (por 8)",
                    svg=escala),
                "Nombra los lados primero": dict(
                    corto="opuesto, adyacente, hipotenusa",
                    d="Mirando un ángulo del triángulo rectángulo: el opuesto está enfrente, el adyacente lo "
                      "toca y no es la hipotenusa, y la hipotenusa es el lado más largo, frente al ángulo recto.",
                    f="sen = op ÷ hip   ·   cos = ady ÷ hip   ·   tan = op ÷ ady",
                    ej="una escalera de 5 m forma 60° con el piso: su pie queda a 5 · cos 60° = 2,5 m de la pared.",
                    ojo="los nombres cambian si cambias de ángulo: el opuesto de un ángulo es el adyacente del "
                        "otro. Rotula antes de escoger la razón.",
                    chequeo="Si conozco el opuesto y el adyacente, ¿qué razón uso? (la tangente)",
                    svg=triangulo),
                "Cada cuerpo, su fórmula": dict(
                    corto="círculo, cilindro, triángulo",
                    d="Cada figura tiene su fórmula. Una figura compuesta se parte en figuras conocidas y se "
                      "suman sus áreas o sus volúmenes.",
                    f="círculo π·r²   ·   cilindro π·r²·h   ·   triángulo b·h ÷ 2",
                    ej="un tanque de radio 1 m y altura 2 m guarda π · 1² · 2 ≈ 6,28 m³: unos 6.280 litros.",
                    ojo="1 m³ son 1.000 litros. Y el radio es la mitad del diámetro: revisa cuál te dieron.",
                    chequeo="Un círculo de diámetro 6 cm, ¿qué radio tiene y cuál es su área? (3 cm; 9π cm²)",
                    svg=cilindro),
                "Juzgar lo que afirman": dict(
                    corto="rehacer la cuenta y comparar",
                    d="Para juzgar una afirmación se rehace el cálculo con los datos y se compara: se acepta "
                      "solo si los números la sostienen. También se revisa la fórmula que usaron.",
                    f="afirmación → rehago → ¿coincide?",
                    ej="«la diagonal de un cuadrado de lado 3 mide 6»: con Pitágoras, √(9 + 9) ≈ 4,24. Es falsa.",
                    ojo="una cuenta bien hecha con la fórmula equivocada también es un error: mira qué razón "
                        "o qué fórmula escogieron.",
                    chequeo="«El área de un círculo de radio 2 es 4π». ¿Es cierto? (sí: π · 2² = 4π)",
                    svg=lambda c: lupa(c, ("dato", "fórmula", "cuenta"))),
            },
            vocab=[("Escala", "cuántas veces se reduce la realidad"),
                   ("Hipotenusa", "el lado más largo, frente al ángulo recto"),
                   ("Cateto opuesto", "el lado de enfrente del ángulo"),
                   ("Cateto adyacente", "el lado que toca el ángulo"),
                   ("Seno", "opuesto ÷ hipotenusa"),
                   ("Coseno", "adyacente ÷ hipotenusa"),
                   ("Tangente", "opuesto ÷ adyacente"),
                   ("Radio", "del centro al borde: la mitad del diámetro"),
                   ("Cilindro", "cuerpo de dos bases circulares: π·r²·h")]),
        5: dict(
            titulo="Muchos datos, pocas palabras",
            centro=("Leer datos", "resumir muchos datos en pocos números y gráficos sin cambiar lo que dicen",
                    histograma),
            centro_ej="las notas de un curso de 40 estudiantes caben en un número (la media) o en un gráfico "
                      "de barras, pero cada resumen cuenta una parte distinta.",
            centro_ojo="antes de las barras se leen el título, los ejes y las unidades.",
            centro_chequeo="¿Qué se lee primero en un gráfico? (el título, los ejes y las unidades)",
            ideas={
                "Cuál medida responde": dict(
                    corto="media, mediana, moda, rango",
                    d="Media: el reparto parejo. Mediana: el dato del medio con los datos ordenados. Moda: el "
                      "que más se repite. Rango: el mayor menos el menor. La pregunta decide cuál sirve.",
                    f="media = suma ÷ n   ·   rango = mayor − menor",
                    ej="con 2, 3, 3, 4 y 8: media 4, mediana 3, moda 3 y rango 6.",
                    ojo="«homogéneo» quiere decir poca dispersión (rango pequeño), no media baja.",
                    chequeo="Con 1, 1, 5, 9, ¿cuáles son la moda y la mediana? (moda 1; mediana 3)",
                    svg=puntos_medidas),
                "De porcentaje a personas": dict(
                    corto="total × % ÷ 100",
                    d="Un porcentaje se pasa a personas multiplicando el total por el porcentaje y dividiendo "
                      "entre 100. Si hay que juntar grupos, primero se suman los porcentajes.",
                    f="personas = total · % ÷ 100",
                    ej="de 800 estudiantes, 15 % y 10 % prefieren dos frutas: juntas son 25 %, y "
                       "800 · 25 ÷ 100 = 200.",
                    ojo="convertir cada grupo y redondear antes de sumar acumula error: suma porcentajes, "
                        "después convierte.",
                    chequeo="¿Cuántas personas son el 30 % de 1.200? (360)",
                    svg=cuadricula),
                "Afirmación por afirmación": dict(
                    corto="cada frase contra el gráfico",
                    d="Ante varias afirmaciones sobre un gráfico, se revisa cada una contra el gráfico, por "
                      "separado, y se marca si el dato la sostiene o no.",
                    f="afirmación → dato del gráfico → ✓ o ✗",
                    ej="en un gráfico circular, «la mitad prefiere mango» exige que mango ocupe el 50 %; ser "
                       "la tajada más grande no basta.",
                    ojo="frecuencia no es lo mismo que porcentaje: mira qué mide el eje antes de comparar.",
                    chequeo="Si una tajada es del 40 %, ¿se puede decir que es «la mayoría»? (no: la mayoría pasa del 50 %)",
                    svg=torta),
                "Probar los cuatro casos": dict(
                    corto="opción por opción, sin saltarse",
                    d="Cuando la pregunta pide la opción que cumple, o la que NO cumple, se prueba cada opción "
                      "con los datos, una por una, sin saltarse ninguna.",
                    f="opción → calculo → comparo → marco",
                    ej="¿qué par de grupos NO llega al 50 %? 20 % + 25 % = 45 %: ese par no llega, aunque "
                       "parezca mucho.",
                    ojo="para comparar con el 50 %, suma primero y compara después.",
                    chequeo="¿Llegan al 50 % juntos un grupo de 28 % y otro de 21 %? (no: suman 49 %)",
                    svg=cuatro_casos),
            },
            vocab=[("Media", "suma de los datos ÷ cuántos son"),
                   ("Mediana", "el dato del medio, con los datos ordenados"),
                   ("Moda", "el dato que más se repite"),
                   ("Rango", "el mayor menos el menor"),
                   ("Dispersión", "qué tan separados están los datos"),
                   ("Frecuencia", "cuántas veces aparece un dato"),
                   ("Porcentaje", "cuántos de cada 100"),
                   ("Histograma", "barras pegadas que agrupan datos"),
                   ("Gráfico circular", "un círculo partido según los porcentajes")]),
        6: dict(
            titulo="Contar bien antes de apostar",
            centro=("Probabilidad", "casos que interesan ÷ casos posibles", dado),
            centro_ej="al lanzar un dado, sacar par son 3 casos de 6: la probabilidad es 3 ÷ 6 = 0,5.",
            centro_ojo="una probabilidad va de 0 a 1 (de 0 % a 100 %): si da más, algo se contó mal.",
            centro_chequeo="¿Cuál es la probabilidad de sacar un número mayor que 4 en un dado? (2 ÷ 6 = ⅓)",
            ideas={
                "Todos los casos que cuentan": dict(
                    corto="contar con orden o sin orden",
                    d="Antes de calcular se cuentan todos los casos. Si importa el orden y no se repite, se "
                      "multiplican las opciones de cada puesto. Si se puede repetir, opciones elevado a "
                      "puestos. «Al menos 3 de 4» son dos casos: exactamente 3, o los 4.",
                    f="sin repetir: 6 · 5   ·   con repetición: 5³",
                    ej="un presidente y un tesorero entre 6 personas: 6 · 5 = 30 formas.",
                    ojo="si el orden no importa (un comité de dos), cada pareja se contó dos veces: 30 ÷ 2 = 15.",
                    chequeo="¿Cuántas claves de 3 dígitos se arman con 1, 2 y 3 si se pueden repetir? (3³ = 27)",
                    svg=casillas),
                "Lo que cambia el total": dict(
                    corto="complemento y sin reemplazo",
                    d="La probabilidad de que NO pase es 1 menos la de que pase. Sin reemplazo, lo que sale no "
                      "vuelve: en la segunda extracción el total tiene uno menos.",
                    f="P(no A) = 1 − P(A)   ·   sin reemplazo: n, luego n − 1",
                    ej="en una bolsa con 3 verdes y 2 amarillas, sacar dos verdes sin devolver: "
                       "3/5 · 2/4 = 6/20 = 0,3.",
                    ojo="multiplicar 3/5 · 3/5 supone que la primera bola volvió a la bolsa.",
                    chequeo="Si la probabilidad de lluvia es 0,35, ¿cuál es la de que no llueva? (0,65)",
                    svg=bolsa),
                "Juzgar el procedimiento": dict(
                    corto="revisar paso por paso",
                    d="No basta con que el resultado parezca razonable: se revisa cada paso y se busca dónde "
                      "se usó un dato o una operación que no corresponde.",
                    f="paso 1 → paso 2 → paso 3: ¿cuál falla?",
                    ej="«la probabilidad de dos caras con dos monedas es 1/2 + 1/2 = 1»: el paso falla, porque "
                       "los dos sucesos juntos se multiplican: 1/2 · 1/2 = 1/4.",
                    ojo="«y» entre dos sucesos independientes multiplica; «o» entre sucesos que no pueden "
                        "pasar a la vez suma.",
                    chequeo="¿Una probabilidad puede dar 1,2? ¿Qué te dice eso del procedimiento? (no; hay un paso malo)",
                    svg=lupa),
                "Hasta dónde llega el dato": dict(
                    corto="lo que el dato permite decir",
                    d="Un dato describe a quienes se midió y cuándo se midió. Usarlo para el futuro o para "
                      "otros grupos es una suposición, y hay que decirla.",
                    f="dato de hoy ≠ certeza de mañana",
                    ej="si el 30 % de un curso lee a diario, no se sabe si el año entrante será igual, ni si pasa "
                       "lo mismo en otro colegio.",
                    ojo="«siempre», «seguro» y «todos» suelen pasarse de lo que el dato permite.",
                    chequeo="Una encuesta a 50 estudiantes de un colegio, ¿sirve para hablar de todo el país? (no sin decir la suposición)",
                    svg=muestra),
            },
            vocab=[("Probabilidad", "casos favorables ÷ casos posibles"),
                   ("Caso posible", "cualquier resultado que puede salir"),
                   ("Caso favorable", "un resultado que sí cuenta"),
                   ("Complemento", "lo contrario: 1 menos la probabilidad"),
                   ("Sin reemplazo", "lo que sale no vuelve"),
                   ("Permutación", "conteo donde el orden importa"),
                   ("Combinación", "conteo donde el orden no importa"),
                   ("Muestra", "el grupo al que de verdad se le preguntó"),
                   ("Proyección", "usar el dato para el futuro: es una suposición")]),
    }


DECIR = ["«Lo que acaban de descubrir tiene nombre». Toca la tarjeta del centro y dila en una frase.",
         "Abre solo la tarjeta de la estrategia 1: es la que se entrena ya en la dinámica. Las demás se "
         "abren cuando aparezcan en el taller: vuelve a esta diapositiva con ← cuando haga falta.",
         "Una frase por tarjeta, nada más. Si alguien pregunta algo largo: «lo vemos en la pregunta que toca»."]
APOYO = ["Las fórmulas están para reconocerlas, no para memorizarlas hoy.",
         "Los ejemplos son propios de la guía: no son los del libro, para que no resuelvan el taller por "
         "adelantado.",
         "La conceptualización se toma 3 de los 15 minutos de la Activación. Si la activación se alargó, pasa "
         "directo a la dinámica: el mapa sigue disponible para el cierre."]


def datos(ESTR, EST_COL):
    out = {}
    m1 = _m1(ESTR, EST_COL)[1]
    for i in m1["ideas"]:
        i["chequeo"] = CHEQUEO_M1[i["t"]]
    m1["centro_chequeo"] = CHEQUEO_M1["Razón de cambio"]
    out[1] = m1
    for mis, D in _m2a6().items():
        col = EST_COL[mis]
        ct, cd, cfig = D["centro"]
        ideas = []
        for k, nombre in enumerate(ESTR[mis]):
            i = dict(D["ideas"][nombre], t=nombre)
            i["svg"] = i["svg"](col[k])
            ideas.append(i)
        out[mis] = dict(D, centro=(ct, cd, cfig("#242478")), ideas=ideas, decir=DECIR, apoyo=APOYO)
    for mis, D in out.items():                      # que no falte nada (el planeador lo imprime todo)
        for i in D["ideas"]:
            faltan = [k for k in ("t", "corto", "d", "f", "ej", "ojo", "chequeo", "svg") if not i.get(k)]
            assert not faltan, (mis, i.get("t"), faltan)
    return out


DATOS = None


def de(mis, ESTR, EST_COL):
    """ESTR y EST_COL vienen de clase_viva_mate (orden y color de las estrategias del cuaderno)."""
    global DATOS
    if DATOS is None:
        DATOS = datos(ESTR, EST_COL)
    return DATOS.get(mis)
