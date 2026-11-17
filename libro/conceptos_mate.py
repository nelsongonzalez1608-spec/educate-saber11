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


def datos(ESTR, EST_COL):
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


DATOS = None


def de(mis, ESTR, EST_COL):
    """ESTR y EST_COL vienen de clase_viva_mate (orden y color de las estrategias del cuaderno)."""
    global DATOS
    if DATOS is None:
        DATOS = datos(ESTR, EST_COL)
    return DATOS.get(mis)
