#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLANEADOR DEL DOCENTE · MATEMÁTICAS · las ocho clases del área.

El hilo:  LIBRO tiene la pregunta · CUADERNO tiene el andamiaje · PLANEADOR le dice al
profe qué hacer con los dos · GUÍA pone ese plan en pantalla.

Regla que gobierna todo: primero se escribe el andamiaje, después se marca la respuesta.
Una hoja con la respuesta correcta y el andamiaje vacío no cuenta como resuelta.

Mismo motor que el cuaderno (lib.py, SVG 2000 × 2588 → PDF carta). Sin líneas
horizontales decorativas: los acentos son verticales o bandas sólidas de cabecera.
"""
from lib import *

AZ = "#1F4E8C"            # Matemáticas
AZ_D = "#13325C"
AZ_BG = "#EEF3FA"
AZ_LN = "#C6D6EA"
ORO = "#C9821B"; ORO_BG = "#FDF5E7"; ORO_LN = "#E8CFA3"
ORO_CLARO = "#E8B65F"   # el oro institucional no contrasta sobre la banda oscura
ROJO = "#A82424"; ROJO_BG = "#FBEFEF"; ROJO_LN = "#E6C4C4"
VERDE = "#2E7A39"; VERDE_BG = "#EDF5EE"; VERDE_LN = "#C3DEC8"
PIZ = "#28313F"           # banda de cabecera
OUT = "/home/claude/libro/"
TOT = 24                  # 2 de entrada · 2 de momentos · 12 de clase · 1 de
                          # simulacro · 6 de dinámicas · 1 de cierre
PAGS = []                 # nombres de las hojas, en orden


# ═══════════════════════ piezas del documento ═══════════════════════
def cabecera(body, titulo_, sub, etiqueta, derecha=None, dsub=None, campos=False):
    """Banda sólida de cabecera. No es una línea: es el bloque de identificación."""
    h = 268 if campos else 200
    body.append(rect(M, 48, CW, h, PIZ, r=22))
    body.append(f'<circle cx="{W-200}" cy="90" r="150" fill="white" opacity="0.045"/>')
    body.append(logo(M + 42, 86, 62, chip=True, pad=12))
    lx = M + 42 + logo_w(62) + 40
    w = chip(body, lx, 80, etiqueta, ORO, size=19, pad=17, txtc="#3A2602")
    body.append(T(lx, 168, [titulo_], 46, "white", weight="700"))
    body.append(T(lx, 206, [sub], 23, "#A9B5C6"))
    if derecha:
        body.append(T(W - M - 42, 124, [derecha], 44, ORO_CLARO, weight="700", anchor="end"))
        body.append(T(W - M - 42, 156, [dsub or ""], 19, "#AEBACB", anchor="end"))
    if campos:
        cx = lx
        for lab, an in [("DOCENTE", 520), ("GRUPO", 240), ("FECHA", 250)]:
            body.append(T(cx, 250, [lab], 16, "#8D9BAE", ls=1))
            body.append(line(cx, 266, cx + an, 266, "#6E7C8E", 2, "7,7"))
            cx += an + 44
    return 48 + h + 44


def pie(body, pag, total):
    y = H_PAGE - 96
    body.append(rect(M, y - 16, CW, 76, AZ_BG, r=18))
    body.append(T(M + 30, y + 30, ["PLANEADOR DEL DOCENTE"], 19, AZ, weight="700", ls=1.6))
    body.append(f'<circle cx="{M+330}" cy="{y+23}" r="5" fill="{ORO}"/>')
    body.append(T(M + 352, y + 30, ["el cuaderno del estudiante es tu instrumento de seguimiento"],
                  19, GRAY))
    body.append(T(W - M - 30, y + 30, [f"Matemáticas · hoja {pag} de {total}"], 19, GRAY, anchor="end"))


def seccion(body, y, txt, sub=None, color=AZ):
    # El subtítulo va de segundo: antes estaba después del color y todas las
    # llamadas le pasaban la frase al parámetro `color`, que dibujaba el título
    # con fill="Lo que ya está construido…" en vez de azul.
    body.append(T(M, y + 30, [txt.upper()], 23, color, weight="700", ls=2.2))
    y += 46
    if sub:
        y = parrafo_j(body, M, y, sub, CW, 25, GRAY, style="italic") + 10
    return y + 8


def tarjeta(body, x, y, w, h, color, bg="white", ln=None, titulo_=None, sub=None, acento=True):
    """Tarjeta con acento VERTICAL a la izquierda (los verticales sí se permiten)."""
    body.append(rect(x, y, w, h, bg, r=18, stroke=ln or color, sw=2.2))
    if acento:
        body.append(rect(x, y + 14, 5, h - 28, color, r=3))
    yy = y + 20
    if titulo_:
        body.append(T(x + 26, yy + 26, [titulo_], 25, color, weight="700"))
        yy += 44
    if sub:
        body.append(T(x + 26, yy + 20, [sub], 20, GRAY, style="italic"))
        yy += 34
    return yy + 6


def nota(body, x, y, w, texto, color=AZ, bg=AZ_BG, ln=AZ_LN, rotulo=None, size=24):
    """Recuadro de aviso. Mide su propio alto con la fuente real."""
    pad = 24
    lineas = wrap_px(texto, size, w - pad * 2 - 14)
    h = pad * 2 + (34 if rotulo else 0) + len(lineas) * size * 1.42
    body.append(rect(x, y, w, h, bg, r=16, stroke=ln, sw=2))
    body.append(rect(x, y + 12, 5, h - 24, color, r=3))
    yy = y + pad
    if rotulo:
        body.append(T(x + pad + 14, yy + 20, [rotulo.upper()], 19, color, weight="700", ls=1.4))
        yy += 34
    parrafo_j(body, x + pad + 14, yy - 6, texto, w - pad * 2 - 14, size, INK)
    return y + h


# ═══════════════════════ contenido del área ═══════════════════════
# Los seis momentos de una CLASE de 120 minutos (fases, no contenidos).
FASES = [
    ("Activación", 15, AZ,
     "Que el estudiante active con el cuerpo la noción de cambio antes de ver cualquier "
     "fórmula, reconociendo en datos cotidianos qué magnitud varía y respecto a cuál.",
     ["Escribe en el tablero tres o cuatro datos en tabla, sin decir de qué son.",
      "Lanza una sola pregunta oral: ¿qué está cambiando aquí y respecto a qué?",
      "Ejecuta la dinámica de apertura según la estrategia del encuentro."],
     "No resuelve, no corrige y no adelanta vocabulario técnico. Si alguien dice «función» "
     "o «pendiente», lo deja pasar sin confirmar ni negar. El cuaderno permanece cerrado.",
     "Tablero y espacio despejado. Todavía no se abre el cuaderno."),
    ("Pregunta problematizadora", 20, ROJO,
     "Que el estudiante compruebe que una pregunta del ICFES no se resuelve calculando sino "
     "interpretando, usando la pregunta modelo del libro.",
     ["Presenta la pregunta modelo del libro y la deja a la vista todo el momento.",
      "Pide hipótesis a mano alzada ANTES de cualquier análisis y las anota en el tablero.",
      "Recorre en voz alta con el grupo el paso a paso que el libro propone.",
      "Revela la clave solo al final y trabaja el análisis de distractores."],
     "Regla del momento: nadie justifica diciendo «porque se ve así». Cada intervención debe "
     "nombrar un dato concreto de la gráfica o de la tabla.",
     "Libro abierto en la pregunta modelo. Cuaderno solo en «mi primera idea»."),
    ("Desarrollo guiado", 35, "#3B3BA6",
     "Que el estudiante resuelva las preguntas del taller dejando registro escrito de su "
     "razonamiento antes de marcar la respuesta.",
     ["Entrega las hojas del momento y trabaja por bloques: 1-2, 3-4, 5-6, 7-8 y 9-10.",
      "Antes de que marquen, verifica que el instrumento de pensamiento esté diligenciado.",
      "Cada 18 minutos corta e introduce la dinámica de la estrategia del bloque.",
      "Al cerrar cada bloque, nombra en voz alta la estrategia que acaban de usar."],
     "No da respuestas. Si un estudiante se traba, lo devuelve al paso a paso de su propia "
     "hoja y le pregunta en cuál de los pasos se quedó.",
     "Cuaderno, las cinco hojas de taller del momento. Libro, en las preguntas 1 a 10."),
    ("Reto en equipo", 20, "#6B4FBE",
     "Que el estudiante contraste su razonamiento con el de otros y defienda su elección con "
     "datos, sin que el equipo reemplace su registro individual.",
     ["Arma equipos de tres y entrega el reto del corte de este momento.",
      "Exige que cada integrante llegue con su cuaderno YA diligenciado individualmente.",
      "Da tres minutos de defensa por equipo: deben citar un dato, no una opinión.",
      "Cierra señalando en qué se parecían los razonamientos y en qué no."],
     "El equipo discute, pero cada uno responde en SU cuaderno. Si un equipo entrega una sola "
     "respuesta colectiva, el reto no cuenta: el producto es individual, la discusión es compartida.",
     "Cuaderno de cada estudiante y la tarjeta del reto del corte."),
    ("Evaluación individual", 20, ORO,
     "Que el estudiante transfiera por sí solo la estrategia aprendida a preguntas reales del "
     "ICFES, sin acompañamiento del docente ni de sus compañeros.",
     ["Entrega las dos hojas de entrenamiento ICFES del momento.",
      "Da el tiempo completo sin intervenir ni resolver dudas de contenido.",
      "Registra quién llena el instrumento y quién salta directo a marcar."],
     "Este momento es silencioso y en filas individuales. Es el que produce el dato de "
     "seguimiento del encuentro. Si un estudiante marca sin llenar la columna, se le anota, "
     "no se le corrige.",
     "Cuaderno, las dos hojas de entrenamiento ICFES. Reloj a la vista."),
    ("Cierre", 10, VERDE,
     "Que el estudiante verbalice qué tienen en común la pregunta del libro y la del ICFES, y "
     "nombre la estrategia que usó para resolverlas.",
     ["Socializa solo las preguntas que el grupo falló, con dos o tres respuestas del salón.",
      "Pide que lean en voz alta su salvavidas: la ruta mínima que los habría salvado.",
      "Cierra nombrando la estrategia y anunciando en qué momento vuelve a aparecer."],
     "No dicta la conclusión. Si nadie la escribe en sus palabras, la clase no cerró: vale más "
     "dejar una pregunta sin socializar que dictar el resumen.",
     "Cuaderno: «lo que me llevo de esta pregunta», carita de salida y casilla de la portada."),
]

# Las ocho clases del área. clase -> (misión de contenido o None, título, subtítulo)
CLASES = [
    (1, "Momento 1 · Numérico-variacional", "páginas 11 a 17 del cuaderno"),
    (2, "Momento 2 · Numérico-variacional", "páginas 18 a 24 del cuaderno"),
    (3, "Momento 3 · Espacial-métrico", "páginas 25 a 31 del cuaderno"),
    (4, "Momento 4 · Espacial-métrico", "páginas 32 a 38 del cuaderno"),
    (5, "Momento 5 · Aleatorio", "páginas 39 a 45 del cuaderno"),
    (6, "Momento 6 · Aleatorio avanzado", "páginas 46 a 52 del cuaderno"),
    (None, "Simulacro del área", "las 6 franjas de simulacro, en condiciones de prueba"),
    (None, "Socialización del simulacro", "devolución, reparación y cierre del área"),
]

# Por misión: componente, páginas, las cuatro estrategias y qué tiene que instalar el profe.
MISIONES = {
 1: dict(comp="Numérico-variacional", pags="11 a 17",
   estr=["Subir, llegar y volver", "Lo fijo y lo que crece",
         "Un modelo, tres preguntas", "El patrón que continúa"],
   instala="Qué es una razón de cambio y por qué es la misma cosa que la pendiente de una "
           "recta. Esa equivalencia no está dicha en el libro con esas palabras y es la que "
           "amarra todo el componente.",
   ojo="En el libro de grado 10 el revisor pidió justamente esto: que «tasa de cambio "
       "promedio» se relacione de inmediato con la pendiente. Aquí vale igual.",
   clave_est="La estrategia 1 cubre la parábola completa (subir, vértice, bajar). El banco "
             "ICFES verificado no tiene todavía una pregunta oficial de parábola completa, "
             "así que el entrenamiento de este momento refuerza las otras tres."),
 2: dict(comp="Numérico-variacional", pags="18 a 24",
   estr=["Encontrar el techo", "Refutar con el modelo",
         "El aumento constante", "Los datos mandan"],
   instala="La diferencia entre el máximo de una función y el punto donde se alcanza. Es el "
           "corazón de «encontrar el techo» y es exactamente lo que el libro confunde en la "
           "pregunta 1 de este momento.",
   ojo="Refutar es una operación matemática, no una opinión. Un solo contraejemplo numérico "
       "tumba la afirmación: hay que hacerlo en el tablero una vez para que lo crean.",
   clave_est="Las cuatro preguntas ICFES de este momento son oficiales y están verificadas "
             "una por una."),
 3: dict(comp="Espacial-métrico", pags="25 a 31",
   estr=["Partir el cuerpo en piezas", "La misma razón para los dos",
         "Cuántas veces cabe", "Antes de mover, mide"],
   instala="Semejanza: qué cambia y qué no cambia entre dos figuras semejantes. Y que "
           "«altura : sombra» y «sombra : altura» son razones distintas, aunque las dos sean "
           "ciertas. Lo que decide es el orden en que la pregunta las nombra.",
   ojo="La unidad primero, la cuenta después. La mitad de los errores de este momento son "
       "metros contra centímetros, no geometría.",
   clave_est="«Cuántas veces cabe» no es dividir volúmenes a ciegas: hay que medir el hueco "
             "y medir lo que se va a meter, y comprobar que encaje en las tres dimensiones."),
 4: dict(comp="Espacial-métrico", pags="32 a 38",
   estr=["Dimensión por dimensión", "Nombra los lados primero",
         "Cada cuerpo, su fórmula", "Juzgar lo que afirman"],
   instala="Las razones trigonométricas y, con ellas, qué par de lados forma la esquina "
           "recta. El cuaderno las usa en tres preguntas y el libro no las desarrolla: si el "
           "profe no las instala aquí, el estudiante adivina.",
   ojo="Esto no es una interpretación nuestra: el revisor de Matemáticas lo escribió en su "
       "matriz —faltan las razones trigonométricas y los teoremas del seno y del coseno, que "
       "la prueba sí evalúa.",
   clave_est="«Juzgar lo que afirman» es la estrategia que más aparece en el ICFES de este "
             "componente: hay que seguir el procedimiento paso por paso, no estimar a ojo."),
 5: dict(comp="Aleatorio", pags="39 a 45",
   estr=["Cuál medida responde", "De porcentaje a personas",
         "Afirmación por afirmación", "Probar los cuatro casos"],
   instala="Que media, mediana, moda y rango responden preguntas distintas, y que la "
           "pregunta decide cuál sirve. Decir «la medida de tendencia central» en singular, "
           "como si fuera una sola, es el error que el revisor marcó en la bitácora.",
   ojo="De porcentaje a personas: primero se junta el porcentaje, después se pasa a "
       "personas. Al revés se acumulan los redondeos y el número no cuadra.",
   clave_est="Las cuatro ICFES de este momento son de lectura de tablas y gráficos: el "
             "estudiante tiene que armar la tabla completa antes de dividir."),
 6: dict(comp="Aleatorio avanzado", pags="46 a 52",
   estr=["Juzgar el procedimiento", "Todos los casos que cuentan",
         "Hasta dónde llega el dato", "Lo que cambia el total"],
   instala="Conteo y combinatoria: cuándo importa el orden y cuándo no. Sin esto, «todos los "
           "casos que cuentan» es adivinar. Es el vacío teórico más grande del área.",
   ojo="El revisor de grado 10 lo dijo sin rodeos: en el componente aleatorio no hay "
       "referente teórico de combinatoria y sí hay preguntas de combinatoria. Lo mismo pasa "
       "en grado 11, y este momento es donde se tapa el hueco.",
   clave_est="«Hasta dónde llega el dato» es la estrategia de cierre del área: separar lo que "
             "la encuesta midió de lo que el analista afirmó. Riesgo no es lo mismo que "
             "pérdida, y probabilidad no es lo mismo que certeza."),
}

# Hallazgos del libro que el profe TIENE que saber antes de entrar.
AVISOS = {
 1: [("preg. 5", "alta", "Las opciones A y B dicen la misma justificación con otras palabras.",
      "Hay dos respuestas correctas. Acepta las dos y pide que escriban por qué son la misma.")],
 2: [("preg. 1", "alta", "El enunciado pide la semana SIGUIENTE al máximo y la clave da la del máximo.",
      "El enunciado y la clave no concuerdan. Resuelve lo que pide el enunciado y anótalo: es "
      "el ejemplo perfecto de «encontrar el techo» contra «dónde se alcanza el techo».")],
 3: [("preg. 10", "alta", "La figura tiene 7 casillas vacías y la opción correcta afirma que hay 14.",
      "Ninguna opción coincide con la figura. Que cuenten las casillas ellos mismos y escriban "
      "qué no les cuadró: el cuaderno les deja el renglón para eso."),
     ("preg. 2", "media", "La cuarta opción está rotulada «A.» en lugar de «D.».",
      "Avísalo antes de empezar, no después de que marquen."),
     ("preg. 8", "baja", "La opción correcta dice «se multiplican los volúmenes de 32 cubos».",
      "Redacción imprecisa: es un cubo y después los 32. Léela corrigiendo en voz alta.")],
 4: [("preg. 1", "atención", "Dos opciones llegan al mismo número y las dos son correctas.",
      "No es un error de fondo, pero si un estudiante defiende la otra, tiene razón.")],
 5: [("preg. 9", "alta", "El enunciado dice 7 % de espectadores nuevos y la captura de pantalla dice 67 %.",
      "El texto contradice la imagen. Decide cuál vas a usar ANTES de la clase y dilo de "
      "entrada; si no, el salón se parte en dos.")],
 6: [("preg. 2", "media", "La fórmula de la opción correcta está bien, pero el valor impreso es "
      "0,833 y el cálculo da 0,890.",
      "Que hagan la cuenta. El procedimiento es correcto; el número impreso no."),
     ("preg. 10", "atención", "Dos opciones son ciertas: una descarta al analista y la otra "
      "respalda al experto.",
      "Las dos se pueden defender. Úsala para cerrar el área discutiendo cuál afirma más de "
      "lo que el dato permite.")],
}


def _instrumentos():
    from extrae_instrumentos import filas
    taller, icfes = {}, {}
    for a, mis, p, est, ins, ctx in filas():
        if a != "Matemáticas":
            continue
        d = icfes if "ICFES" in str(mis) else taller
        k = int(str(mis).split()[0]) if str(mis).split()[0].isdigit() else int(str(mis)[0])
        d.setdefault(k, []).append((int(p), est, ins, ctx))
    for d in (taller, icfes):
        for k in d:
            d[k].sort()
    return taller, icfes


def _icfes_banco():
    import csv
    with open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig") as f:
        r = list(csv.DictReader(f))
    out = {}
    for x in r:
        m = str(x["mision"]).strip()
        if m.startswith("Misión") and m.split()[-1].isdigit():
            out.setdefault(int(m.split()[-1]), []).append(x)
    return out


TALLER, INS_ICFES = _instrumentos()
BANCO = _icfes_banco()
SEV = {"alta": (ROJO, ROJO_BG, ROJO_LN), "media": (ORO, ORO_BG, ORO_LN),
       "baja": (AZ, AZ_BG, AZ_LN), "atención": (VERDE, VERDE_BG, VERDE_LN)}


# ═══════════════════════ hoja 1 · cómo se usa ═══════════════════════
def h1():
    b = svg_open()
    y = cabecera(b, "Matemáticas", "Planeador del área · las ocho clases",
                 "PLANEADOR DEL DOCENTE", "8", "clases de 120 min", campos=True)

    y = seccion(b, y, "Para qué existe este documento")
    y = parrafo_j(b, M, y,
        "La calidad de la clase no puede depender de qué profesor llegue ese sábado. Por eso el "
        "método de EDUCATE no vive en el profesor: vive en el cuaderno del estudiante. Este "
        "planeador no te dice qué pensar; te dice qué hacer con el libro y con el cuaderno en "
        "cada uno de los 120 minutos, y dónde termina lo fijo y empieza tu aporte.", CW, 27) + 26

    # el hilo de los cuatro materiales
    cajas = [("LIBRO", "tiene la pregunta", GRAY),
             ("CUADERNO", "tiene el andamiaje para resolverla", AZ),
             ("PLANEADOR", "te dice qué hacer con los dos", ORO),
             ("GUÍA", "pone ese plan en pantalla", VERDE)]
    an = (CW - 3 * 26) / 4
    for i, (t, s, c) in enumerate(cajas):
        x = M + i * (an + 26)
        b.append(rect(x, y, an, 150, "white", r=18, stroke=c, sw=2.4))
        b.append(rect(x + 14, y + 16, 5, 118, c, r=3))
        b.append(T(x + an / 2 + 10, y + 62, [t], 26, c, weight="700", anchor="middle", ls=1.4))
        for j, ln in enumerate(wrap_px(s, 21, an - 56)):
            b.append(T(x + an / 2 + 10, y + 100 + j * 28, [" ".join(ln)], 21, GRAY, anchor="middle"))
        if i < 3:
            b.append(T(x + an + 13, y + 86, ["›"], 34, "#A8B0BC", weight="700", anchor="middle"))
    y += 150 + 36

    y = nota(b, M, y, CW,
        "Primero se escribe el andamiaje, después se marca la respuesta. Una hoja con la "
        "respuesta correcta y el andamiaje vacío no cuenta como resuelta. Esto es lo que "
        "convierte el cuaderno en instrumento de auditoría: la coordinación revisa tres "
        "cuadernos al azar sin haber entrado a la clase.",
        ORO, ORO_BG, ORO_LN, "La regla que gobierna cada hoja", 26) + 34

    y = seccion(b, y, "Las tres unidades, que no se confunden",
        "Son tres cosas distintas y en el material se llaman parecido. Vale la pena leerlas una vez.")
    tres = [("MOMENTO", "unidad de contenido. El área tiene 6. Cada uno ocupa 7 páginas: "
             "cinco de taller con las diez preguntas del libro y dos de entrenamiento ICFES.", AZ),
            ("CLASE", "sesión de 2 horas. El área tiene 8, número fijo. Seis son de contenido "
             "y dos son del simulacro del área.", ORO),
            ("LAS SEIS FASES", "Activación, pregunta problematizadora, desarrollo guiado, reto "
             "en equipo, evaluación individual y cierre. Son las fases DENTRO de una clase.", VERDE)]
    for t, d, c in tres:
        lineas = wrap_px(d, 24, CW - 290)
        h = max(92, 40 + len(lineas) * 34)
        b.append(rect(M, y, CW, h, "white", r=16, stroke=AZ_LN, sw=2))
        b.append(rect(M + 14, y + 14, 5, h - 28, c, r=3))
        b.append(T(M + 40, y + 48, [t], 23, c, weight="700", ls=1.6))
        parrafo_j(b, M + 250, y + 18, d, CW - 290, 24, INK)
        y += h + 12
    y += 22

    y = seccion(b, y, "El área en números",
        "Lo que ya está construido y verificado. Si algo de esto no te cuadra con lo que ves "
        "en el cuaderno, para la clase y escríbelo: el material se corrige, la clase no se repite.")
    cif = [("42", "páginas del cuaderno", AZ), ("6", "momentos de contenido", AZ),
           ("60", "preguntas del libro\ncon su andamiaje", ORO),
           ("24", "preguntas oficiales\ndel ICFES", VERDE),
           ("84", "instrumentos distintos\nninguno repetido", AZ)]
    an2 = (CW - 4 * 18) / 5
    for i, (v, l, c) in enumerate(cif):
        x = M + i * (an2 + 18)
        b.append(rect(x, y, an2, 148, "white", r=16, stroke=AZ_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, 120, c, r=3))
        b.append(T(x + 38, y + 68, [v], 52, c, weight="700"))
        for j, ln in enumerate(l.split("\n")):
            b.append(T(x + 38, y + 104 + j * 26, [ln], 20, GRAY))
    y += 148 + 34

    y = seccion(b, y, "Qué lleva el estudiante a cada sábado")
    lleva = [("El libro", "abierto en las páginas del momento. La pregunta vive ahí."),
             ("El cuaderno", "donde escribe el andamiaje. Nunca se devuelve a casa sin la "
              "carita de salida y «lo que me llevo de esta pregunta»."),
             ("Lápiz, no esfero", "porque la primera idea se escribe para corregirla, y una "
              "idea tachada con esfero deja de leerse.")]
    an3 = (CW - 2 * 18) / 3
    alt3 = max(34 + 40 + len(wrap_px(d, 22, an3 - 56)) * 31 for _, d in lleva)
    for i, (t, d) in enumerate(lleva):
        x = M + i * (an3 + 18)
        b.append(rect(x, y, an3, alt3, "white", r=16, stroke=AZ_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt3 - 28, ORO, r=3))
        b.append(T(x + 40, y + 42, [t], 23, INK, weight="700"))
        parrafo_j(b, x + 40, y + 56, d, an3 - 56, 22, GRAY, lh=31)
        y += 0
    y += alt3 + 26

    y = nota(b, M, y, CW,
        "Matemáticas se construyó antes de que existiera el registro de sellos «aquí entra el "
        "profe», así que en la matriz del proyecto esta área todavía figura con cero sellos y "
        "cero textos para proyectar. Lo que este planeador trae en «lo que tienes que instalar» "
        "sale de leer las 84 preguntas del área, no del registro: hay que subirlo a la matriz.",
        AZ, AZ_BG, AZ_LN, "Lo que este planeador todavía le debe a la matriz", 25) + 34

    y = seccion(b, y, "Lo que la coordinación revisa, sin haber entrado a la clase",
        "Tres cuadernos al azar del grupo. No se mira si la respuesta está buena: se mira si el "
        "andamiaje está escrito. Marca tú mismo esta lista al terminar el sábado.")
    rev = ["El instrumento de pensamiento está lleno en las diez preguntas del taller, acertadas o no.",
           "«Mi primera idea, antes de hacer nada» tiene algo escrito en todas las preguntas.",
           "El salvavidas está usado en las preguntas que el estudiante falló.",
           "«Lo que me llevo de esta pregunta» está en palabras del estudiante, no copiado del tablero.",
           "Las dos caritas de la clase están marcadas y la casilla de la portada también."]
    b.append(rect(M, y, CW, 50 + len(rev) * 54, "white", r=18, stroke=AZ_LN, sw=2))
    b.append(rect(M + 14, y + 16, 5, 18 + len(rev) * 54, AZ, r=3))
    yy = y + 36
    for r in rev:
        b.append(checkbox(M + 44, yy - 14, 13, AZ))
        parrafo_j(b, M + 100, yy - 22, r, CW - 150, 24, INK)
        yy += 54
    y += 50 + len(rev) * 54

    pie(b, 1, TOT)
    svg_close(b, OUT + "plan_mate_01.svg")
    PAGS.append("plan_mate_01")


# ═══════════════════════ hoja 2 · las ocho clases ═══════════════════════
def h2():
    b = svg_open()
    y = cabecera(b, "Las ocho clases", "Mapa del área de un vistazo", "PLANEADOR DEL DOCENTE",
                 "42", "páginas del cuaderno")
    y = seccion(b, y, "Qué se ve en cada sábado",
        "Seis clases de contenido, una por momento, y dos para el simulacro del área. "
        "El número de clases es fijo: no se recorta aunque un momento quede largo.")

    colx = [M, M + 120, M + 690, M + 1030, M + 1330]
    anchos = [110, 560, 330, 290, 460]
    enc = ["CLASE", "QUÉ SE TRABAJA", "PÁGINAS", "COMPONENTE", "ENTRENAMIENTO ICFES"]
    b.append(rect(M, y, CW, 54, PIZ, r=12))
    for x, e in zip(colx, enc):
        b.append(T(x + 20, y + 36, [e], 18, "white", weight="700", ls=1.3))
    y += 54 + 10

    for mis, tit, sub in CLASES:
        alto = 96
        bg = "white" if mis else ORO_BG
        ln = AZ_LN if mis else ORO_LN
        b.append(rect(M, y, CW, alto, bg, r=14, stroke=ln, sw=2))
        c = AZ if mis else ORO
        b.append(rect(M + 12, y + 12, 5, alto - 24, c, r=3))
        n = CLASES.index((mis, tit, sub)) + 1
        b.append(T(colx[0] + 44, y + 62, [str(n)], 42, c, weight="700", anchor="middle"))
        b.append(T(colx[1] + 20, y + 44, [tit], 24, INK, weight="700"))
        b.append(T(colx[1] + 20, y + 74, [sub], 20, GRAY, style="italic"))
        if mis:
            d = MISIONES[mis]
            b.append(T(colx[2] + 20, y + 58, ["páginas " + d["pags"]], 23, INK))
            b.append(T(colx[3] + 20, y + 58, [d["comp"]], 22, GRAY))
            banco = BANCO.get(mis, [])
            txt = f"{len(banco)} preguntas oficiales"
            b.append(T(colx[4] + 20, y + 46, [txt], 22, VERDE, weight="700"))
            b.append(T(colx[4] + 20, y + 76, ["verificadas una por una"], 19, GRAY))
        else:
            b.append(T(colx[2] + 20, y + 58, ["las 6 franjas"], 23, GRAY, style="italic"))
            b.append(T(colx[3] + 20, y + 58, ["todo el área"], 22, GRAY))
            b.append(T(colx[4] + 20, y + 58, ["24 preguntas ya resueltas"], 22, GRAY))
        y += alto + 10

    y += 24
    y = nota(b, M, y, CW,
        "Las clases 7 y 8 no traen contenido nuevo: trabajan las seis franjas de simulacro que "
        "el estudiante ya tiene en su cuaderno. La 7 es en condiciones de prueba, con reloj. La "
        "8 es la devolución: se reparan las preguntas falladas con el mismo instrumento con el "
        "que se trabajaron la primera vez, para que el estudiante vea su propio avance escrito.",
        ORO, ORO_BG, ORO_LN, "Por qué ocho clases y no seis", 25) + 34

    y = seccion(b, y, "Las 24 estrategias del área, agrupadas por componente",
        "Son el vocabulario que el estudiante se lleva. Si al final del área puede nombrar las "
        "veinticuatro y decir para qué sirve cada una, el área cumplió, aunque falle preguntas.")
    grupos = [("Numérico-variacional", "momentos 1 y 2", [1, 2], AZ, AZ_BG, AZ_LN),
              ("Espacial-métrico", "momentos 3 y 4", [3, 4], ORO, ORO_BG, ORO_LN),
              ("Aleatorio", "momentos 5 y 6", [5, 6], VERDE, VERDE_BG, VERDE_LN)]
    an = (CW - 2 * 18) / 3
    alto = 0
    for i, (nom, de, mm, c, bg, ln) in enumerate(grupos):
        ests = [(m, e) for m in mm for e in MISIONES[m]["estr"]]
        lins = sum(len(wrap_px(e, 21, an - 110)) for _, e in ests)
        alto = max(alto, 104 + lins * 29 + len(ests) * 14)
    for i, (nom, de, mm, c, bg, ln) in enumerate(grupos):
        x = M + i * (an + 18)
        b.append(rect(x, y, an, alto, bg, r=16, stroke=ln, sw=2))
        b.append(rect(x + 14, y + 14, 5, alto - 28, c, r=3))
        b.append(T(x + 40, y + 46, [nom], 23, c, weight="700"))
        b.append(T(x + 40, y + 74, [de], 19, GRAY, style="italic"))
        yy = y + 100
        for m in mm:
            for j, e in enumerate(MISIONES[m]["estr"]):
                b.append(T(x + 40, yy + 20, [f"M{m}·{j+1}"], 17, c, weight="700"))
                yy = parrafo_j(b, x + 112, yy - 2, e, an - 152, 21, INK, lh=29) + 14
    y += alto

    pie(b, 2, TOT)
    svg_close(b, OUT + "plan_mate_02.svg")
    PAGS.append("plan_mate_02")


# ═══════════ hojas 3 y 4 · los 120 minutos, momento por momento ═══════════
def _barra_tiempo(b, y):
    """El reparto de los 120 minutos. Es una banda de bloques sólidos, no una línea."""
    tot = sum(f[1] for f in FASES)
    x = M
    for i, (nom, mins, c, *_) in enumerate(FASES):
        an = CW * mins / tot
        b.append(rect(x + (0 if i == 0 else 2), y, an - 4, 42, c, r=10))
        b.append(T(x + an / 2, y + 29, [f"{mins}'"], 21, "white", weight="700", anchor="middle"))
        x += an
    return y + 42 + 26


def hoja_momentos(parte):
    """parte 1 = momentos 1 a 3 · parte 2 = momentos 4 a 6."""
    desde, hasta = (0, 3) if parte == 1 else (3, 6)
    b = svg_open()
    y = cabecera(b, "Los 120 minutos",
                 f"Momentos {desde+1} a {hasta} de los seis de una clase",
                 "PLANEADOR DEL DOCENTE", "120", "minutos por clase")

    if parte == 1:
        y = seccion(b, y, "Distribución del tiempo · 120 minutos",
            "El núcleo de cada momento es fijo. Tu aporte tiene su propio espacio al final de "
            "cada bloque: va además de lo de arriba, no en vez de lo de arriba.")
        y = _barra_tiempo(b, y)
    else:
        y = seccion(b, y, "Distribución del tiempo · 120 minutos",
            "Viene de la hoja anterior. La misma estructura en las ocho clases del área.")
        y = _barra_tiempo(b, y)

    for i in range(desde, hasta):
        nom, mins, c, obj, hace, como, material = FASES[i]
        l_obj = wrap_px(obj, 24, CW - 90)
        anc = (CW - 100) / 2
        l_como = wrap_px(como, 22, anc - 20)
        lin_hace = sum(len(wrap_px(h_, 22, anc - 60)) for h_ in hace)
        alto_cols = max(lin_hace * 31 + len(hace) * 16, len(l_como) * 31) + 44
        # 128 de cabecera del momento + 26 hasta el párrafo + el objetivo + 20 de aire
        # + las dos columnas + los 70 de TU APORTE + 20 de respiro al borde.
        h = 264 + len(l_obj) * 34.08 + alto_cols
        b.append(rect(M, y, CW, h, "white", r=20, stroke=AZ_LN, sw=2.2))
        b.append(rect(M + 16, y + 18, 5, h - 36, c, r=3))

        # identificación del momento
        b.append(f'<circle cx="{M+76}" cy="{y+52}" r="26" fill="{c}"/>')
        b.append(T(M + 76, y + 61, [str(i + 1)], 27, "white", weight="700", anchor="middle"))
        b.append(T(M + 124, y + 62, [nom], 29, INK, weight="700"))
        wch = chip(b, M + 124, y + 78, f"{mins} min", c, size=19, pad=16)
        b.append(T(M + 124 + wch + 20, y + 102, ["· " + material], 20, GRAY, style="italic"))

        yy = y + 128
        b.append(T(M + 44, yy + 18, ["OBJETIVO ESPECÍFICO"], 17, c, weight="700", ls=1.4))
        yy = parrafo_j(b, M + 44, yy + 26, obj, CW - 90, 24, INK) + 20

        # dos columnas: qué hace / cómo lo hace
        b.append(T(M + 44, yy + 18, ["QUÉ HACE EL DOCENTE"], 17, c, weight="700", ls=1.4))
        b.append(T(M + 60 + anc + 40, yy + 18, ["CÓMO LO HACE"], 17, c, weight="700", ls=1.4))
        b.append(line(M + 44 + anc + 20, yy + 34, M + 44 + anc + 20, yy + alto_cols - 4,
                      "#E6EAF0", 2))
        yh = yy + 30
        for h_ in hace:
            b.append(f'<circle cx="{M+56}" cy="{yh+18}" r="5.5" fill="{c}"/>')
            yh = parrafo_j(b, M + 80, yh, h_, anc - 60, 22, INK, lh=31) + 16
        parrafo_j(b, M + 60 + anc + 40, yy + 30, como, anc - 20, 22, GRAY, style="italic", lh=31)
        yy += alto_cols

        # TU APORTE: el espacio declarado y acotado del docente
        b.append(rect(M + 44, yy, CW - 88, 70, ORO_BG, r=14, stroke=ORO_LN, sw=2))
        b.append(T(M + 68, yy + 28, ["TU APORTE"], 18, ORO, weight="700", ls=1.4))
        b.append(T(M + 68, yy + 52, ["el ejemplo, la anécdota o la variación que agregas tú "
                                     "— sin reemplazar lo de arriba"], 19, GRAY, style="italic"))
        b.append(line(M + 980, yy + 52, M + CW - 80, yy + 52, "#C9A96B", 2, "8,8"))
        y += h + 16

    pie(b, 2 + parte, TOT)
    svg_close(b, OUT + f"plan_mate_{2 + parte:02d}.svg")


# ═══════════════════ hojas 4 a 9 · una por clase de contenido ═══════════════════
def hoja_clase(mis):
    """Clase de contenido: estrategias, mapa de las diez preguntas, entrenamiento
       ICFES, lo que el profe tiene que instalar y los avisos del libro."""
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Clase {mis}", f"Momento {mis} · {d['comp']} · páginas {d['pags']}",
                 "PLANEADOR DEL DOCENTE", f"{mis}", "de 8 clases")

    # ── las cuatro estrategias
    y = seccion(b, y, "Las cuatro estrategias del momento",
        "Son el vocabulario de la clase. El estudiante las ve rotuladas en cada pregunta de su "
        "cuaderno, así que conviene nombrarlas igual en voz alta.")
    an = (CW - 3 * 16) / 4
    cols = [AZ, VERDE, ORO, "#5B3E96"]
    alt = max(52 + len(wrap_px(e, 23, an - 60)) * 32 for e in d["estr"])
    for i, e in enumerate(d["estr"]):
        x = M + i * (an + 16)
        b.append(rect(x, y, an, alt, "white", r=16, stroke=AZ_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt - 28, cols[i], r=3))
        b.append(T(x + 38, y + 40, [f"ESTRATEGIA {i+1}"], 16, cols[i], weight="700", ls=1.3))
        parrafo_j(b, x + 38, y + 50, e, an - 60, 23, INK, weight="700", lh=32)
    y += alt + 32

    # ── lo que el profe tiene que instalar
    y = nota(b, M, y, CW, d["instala"], ORO, ORO_BG, ORO_LN,
             "Alto · aquí entra el profe: lo que tienes que instalar antes del taller", 26) + 16
    y = nota(b, M, y, CW, d["ojo"], AZ, AZ_BG, AZ_LN, "Ojo con esto", 24) + 32

    # ── mapa de las diez preguntas del taller
    y = seccion(b, y, "Las diez preguntas del libro y su instrumento",
        "Cada pregunta lleva su propio instrumento de pensamiento: ninguno se repite en el área. "
        "Las diez se trabajan en el desarrollo guiado, por bloques de a dos; las dos primeras van en "
        "pantalla y las demás en el cuaderno, con una dinámica entre bloque y bloque.")
    cx = [M, M + 96, M + 460, M + 1180]
    b.append(rect(M, y, CW, 50, PIZ, r=12))
    for x, e in zip(cx, ["N.º", "ESTRATEGIA", "INSTRUMENTO DE PENSAMIENTO", "CONTEXTO DE LA PREGUNTA"]):
        b.append(T(x + 18, y + 33, [e], 17, "white", weight="700", ls=1.2))
    y += 50 + 8
    for p, est, ins, ctx in TALLER.get(mis, []):
        i_est = d["estr"].index(est) if est in d["estr"] else 0
        c = cols[i_est]
        l_ins = wrap_px(ins, 22, 700)
        l_ctx = wrap_px(ctx, 21, 690)
        h = max(58, 22 + max(len(l_ins), len(l_ctx)) * 30)
        bg = "white" if p > 2 else AZ_BG
        b.append(rect(M, y, CW, h, bg, r=12, stroke=AZ_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, h - 20, c, r=2))
        b.append(T(cx[0] + 54, y + h / 2 + 9, [str(p)], 26, c, weight="700", anchor="middle"))
        b.append(T(cx[1] + 18, y + h / 2 + 7, [f"E{i_est+1}"], 20, c, weight="700"))
        b.append(T(cx[1] + 58, y + h / 2 + 7, [est], 20, GRAY))
        parrafo_j(b, cx[2] + 18, y + (h - len(l_ins) * 30) / 2 - 4, ins, 700, 22, INK, lh=30)
        parrafo_j(b, cx[3] + 18, y + (h - len(l_ctx) * 30) / 2 - 4, ctx, 690, 21, GRAY, lh=30)
        y += h + 6
    y += 20
    b.append(T(M, y + 20, ["Las dos primeras van sombreadas: son las que se resuelven en pantalla."],
               21, GRAY, style="italic"))
    y += 56

    # ── el sábado, minuto a minuto, con el contenido de ESTE momento
    base = 11 + (mis - 1) * 7          # primera página del momento en el cuaderno
    t_pags = [base, base + 1, base + 3, base + 4, base + 5]   # las cinco de taller
    i_pags = [base + 2, base + 6]                              # las dos de ICFES
    ins = {p: i for p, e, i, c in TALLER.get(mis, [])}
    din = DINAMICAS[mis]
    concreto = [
        f"Dato de apertura en el tablero. Cuaderno cerrado. Dinámica E1 «{din[0][0]}» "
        f"({din[0][1]}'). Las páginas {t_pags[0]} y {t_pags[1]} todavía sin abrir.",
        f"Pregunta modelo del libro, a la vista todo el momento. Hipótesis a mano alzada antes "
        f"de analizar. Se abre la página {t_pags[0]} solo en «mi primera idea, antes de hacer nada».",
        f"Las diez preguntas por bloques: 1-2 en pantalla (página {t_pags[0]}, instrumentos "
        f"«{ins.get(1,'—')}» y «{ins.get(2,'—')}»), después 3-4, 5-6, 7-8 y 9-10 en las páginas "
        f"{t_pags[1]}, {t_pags[2]}, {t_pags[3]} y {t_pags[4]}. Cada 18 minutos entra la dinámica "
        f"de la estrategia del bloque.",
        f"Reto del corte de la misión {mis}: «{RETOS[mis][0]}». Equipos de tres, pero cada uno "
        f"responde en SU cuaderno. Tres minutos de defensa por equipo, citando un dato.",
        f"Entrenamiento ICFES, páginas {i_pags[0]} y {i_pags[1]}. Cuatro preguntas oficiales, "
        f"en silencio y con reloj. Unos cinco minutos cada una.",
        f"Se socializan solo las falladas. Cada uno lee su salvavidas, escribe «lo que me llevo "
        f"de esta pregunta», marca su carita de salida y la casilla {mis} de la portada del área.",
    ]
    y = seccion(b, y, "El sábado, minuto a minuto",
        "Las seis fases con el contenido de este momento puesto encima. El reparto del tiempo "
        "es el mismo en las ocho clases.")
    reloj = 0
    for (nom, mins, c, *_), txt in zip(FASES, concreto):
        lin = wrap_px(txt, 23, CW - 480)
        h = max(76, 30 + len(lin) * 32)
        b.append(rect(M, y, CW, h, "white", r=14, stroke=AZ_LN, sw=1.8))
        b.append(rect(M + 12, y + 12, 5, h - 24, c, r=3))
        b.append(T(M + 40, y + h / 2 - 2, [f"{reloj:02d}'–{reloj+mins:02d}'"], 22, c,
                   weight="700"))
        b.append(T(M + 40, y + h / 2 + 26, [nom], 20, GRAY))
        parrafo_j(b, M + 440, y + (h - len(lin) * 32) / 2 - 5, txt, CW - 480, 23, INK, lh=32)
        reloj += mins
        y += h + 7

    pie(b, 3 + mis * 2, TOT)
    svg_close(b, OUT + f"plan_mate_{3 + mis * 2:02d}.svg")


def hoja_clase_b(mis):
    """Segunda cara de la clase: entrenamiento ICFES, avisos del libro y la bitácora."""
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Clase {mis} · evaluación", f"Entrenamiento ICFES y avisos del libro",
                 "PLANEADOR DEL DOCENTE", "25", "min de evaluación")

    banco = BANCO.get(mis, [])
    y = seccion(b, y, "Las cuatro preguntas oficiales del momento",
        "Van en las dos hojas de entrenamiento del cuaderno. Todas verificadas una por una: el "
        "membrete es siempre «Pregunta oficial ICFES · Saber 11».")
    for k, (x4, est, ins, ctx) in enumerate(INS_ICFES.get(mis, [])):
        fila = banco[k] if k < len(banco) else {}
        l_ins = wrap_px(ins, 23, CW - 700)
        h = max(118, 70 + len(l_ins) * 32)
        b.append(rect(M, y, CW, h, "white", r=16, stroke=VERDE_LN, sw=2))
        b.append(rect(M + 14, y + 14, 5, h - 28, VERDE, r=3))
        b.append(T(M + 40, y + 42, [f"PREGUNTA {x4}"], 17, VERDE, weight="700", ls=1.3))
        b.append(T(M + 40, y + 76, [fila.get("contexto", "—")[:40]], 23, INK, weight="700"))
        mb = fila.get("membrete", "Pregunta oficial ICFES · Saber 11")
        b.append(T(M + 40, y + 104, [mb], 20, GRAY, style="italic"))
        parrafo_j(b, M + 640, y + 32, ins, CW - 700, 23, INK, lh=32)
        cl = fila.get("clave", "").strip()
        if cl:
            b.append(rect(W - M - 110, y + h / 2 - 32, 64, 64, VERDE_BG, r=14, stroke=VERDE, sw=2))
            b.append(T(W - M - 78, y + h / 2 + 12, [cl], 34, VERDE, weight="700", anchor="middle"))
            b.append(T(W - M - 78, y + h / 2 + 44, ["clave"], 16, GRAY, anchor="middle"))
        y += h + 10
    y += 26

    # ── avisos del libro
    y = seccion(b, y, "Lo que tienes que saber del libro antes de entrar",
        "Salió de resolver las diez preguntas una por una. No se le esconde al estudiante: el "
        "cuaderno le deja un renglón para escribir qué no le cuadró.")
    for preg, sev, que, hacer in AVISOS.get(mis, []):
        c, bg, ln = SEV[sev]
        l_q = wrap_px(que, 24, CW - 420)
        l_h = wrap_px(hacer, 24, CW - 420)
        h = 44 + len(l_q) * 34 + 26 + len(l_h) * 34 + 22
        b.append(rect(M, y, CW, h, bg, r=16, stroke=ln, sw=2))
        b.append(rect(M + 14, y + 14, 5, h - 28, c, r=3))
        b.append(T(M + 40, y + 46, [preg.upper()], 21, c, weight="700", ls=1.2))
        w = chip(b, M + 40, y + 62, sev.upper(), c, size=16, pad=13, fill=bg, txtc=c)
        yy = parrafo_j(b, M + 390, y + 20, que, CW - 420, 24, INK, weight="700") + 8
        b.append(T(M + 390, yy + 18, ["QUÉ HACES EN CLASE"], 16, c, weight="700", ls=1.3))
        parrafo_j(b, M + 390, yy + 24, hacer, CW - 420, 24, INK)
        y += h + 12
    y += 26

    y = nota(b, M, y, CW, d["clave_est"], AZ, AZ_BG, AZ_LN, "Para el cierre del momento", 25) + 34

    # ── registro del docente después de la clase
    y = seccion(b, y, "Después de la clase · tu registro",
        "Esto no lo ve el estudiante. Se llena el mismo sábado, antes de salir: dentro de una "
        "semana ya no te acuerdas de quién se quedó atrás.")
    an = (CW - 16) / 2
    campos = [("¿Qué pregunta tuvo que volver a explicarse?",
               "y con qué palabras funcionó la segunda vez"),
              ("¿A quién hay que volver la próxima clase?",
               "nombres, no «algunos»"),
              ("¿Qué cuaderno quedó con el andamiaje vacío?",
               "aunque haya acertado la respuesta"),
              ("¿Qué cambiarías de esta clase?",
               "va al reporte de los especialistas")]
    for i, (t, sub_) in enumerate(campos):
        x = M + (i % 2) * (an + 16)
        yy = y + (i // 2) * 246
        b.append(rect(x, yy, an, 232, "white", r=16, stroke=AZ_LN, sw=2))
        b.append(rect(x + 14, yy + 14, 5, 204, AZ, r=3))
        b.append(T(x + 40, yy + 44, [t], 23, INK, weight="700"))
        b.append(T(x + 40, yy + 74, [sub_], 20, GRAY, style="italic"))
        b.append(wlines(x + 40, yy + 118, an - 80, 3, c="#E6EAF0", step=38))
    y += 246 * 2 - 14

    # ── puntaje del momento
    y = nota(b, M, y, CW,
        "Diez preguntas del libro y cuatro oficiales del ICFES. La nota del momento sale de las "
        "cuatro oficiales, no de las diez: las diez son para aprender, las cuatro son para medir. "
        "Un estudiante con el andamiaje completo y dos oficiales falladas no está mal; uno con "
        "cuatro oficiales buenas y el cuaderno en blanco sí, porque adivinó.",
        VERDE, VERDE_BG, VERDE_LN, "Cómo se califica este momento", 25)

    pie(b, 4 + mis * 2, TOT)
    svg_close(b, OUT + f"plan_mate_{4 + mis * 2:02d}.svg")


# ═══════════════════ hoja 16 · clases 7 y 8 · el simulacro ═══════════════════
def h16():
    b = svg_open()
    y = cabecera(b, "Clases 7 y 8", "El simulacro del área y su devolución",
                 "PLANEADOR DEL DOCENTE", "24", "preguntas del simulacro")

    y = seccion(b, y, "Qué son estas dos clases",
        "No traen contenido nuevo. Trabajan las seis franjas de simulacro que el estudiante ya "
        "tiene en su cuaderno, una por momento, y que hasta ahora resolvió de a poco.")

    dos = [("Clase 7 · el simulacro", ROJO, ROJO_BG, ROJO_LN,
            "Condiciones de prueba, 90 minutos de reloj, en silencio",
            ["Las 24 preguntas oficiales del área, seguidas, sin instrumento a la vista.",
             "El estudiante tapa la columna del andamiaje con una hoja. Eso es parte de la prueba.",
             "No se responde ninguna duda, ni de vocabulario. Las dudas se anotan en el margen.",
             "Los últimos 30 minutos: cada uno cuenta sus aciertos por componente y los escribe "
             "en la portada del área."]),
           ("Clase 8 · la devolución", VERDE, VERDE_BG, VERDE_LN,
            "Reparación con el mismo instrumento de la primera vez",
            ["Se eligen las cinco preguntas que más falló el grupo, no las que a ti te parecen "
             "más interesantes.",
             "Cada una se vuelve a trabajar con el instrumento con el que se trabajó la primera "
             "vez: el estudiante ve su letra de hace seis semanas al lado de la de hoy.",
             "Ese contraste es el cierre del área. No hay que explicarlo: hay que señalarlo.",
             "Al final, la página de cierre del cuaderno y el pacto para la siguiente área."])]
    an = (CW - 20) / 2
    for i, (tit, c, bg, ln, sub_, pasos) in enumerate(dos):
        x = M + i * (an + 20)
        lin_tot = sum(len(wrap_px(p_, 22, an - 110)) for p_ in pasos)
        h = 120 + lin_tot * 31 + len(pasos) * 22
        b.append(rect(x, y, an, h, bg, r=18, stroke=ln, sw=2.2))
        b.append(rect(x + 14, y + 16, 5, h - 32, c, r=3))
        b.append(T(x + 40, y + 52, [tit], 27, c, weight="700"))
        b.append(T(x + 40, y + 86, [sub_], 20, GRAY, style="italic"))
        yy = y + 112
        for p_ in pasos:
            b.append(f'<circle cx="{x+52}" cy="{yy+12}" r="6" fill="{c}"/>')
            yy = parrafo_j(b, x + 76, yy - 6, p_, an - 110, 22, INK, lh=31) + 22
    y += max(120 + sum(len(wrap_px(p_, 22, an - 110)) for p_ in d[5]) * 31 + len(d[5]) * 22
             for d in dos) + 34

    y = nota(b, M, y, CW,
        "El simulacro no se califica con nota. Se cuenta por componente: numérico-variacional, "
        "espacial-métrico y aleatorio. Lo que importa es que el estudiante vea en cuál de los "
        "tres se le va el puntaje, porque ahí es donde tiene que invertir las semanas que le "
        "quedan antes de la prueba real.",
        ORO, ORO_BG, ORO_LN, "Cómo se lee el resultado", 26) + 34

    y = seccion(b, y, "Conteo por componente",
        "Llénalo con el grupo en el tablero al final de la clase 7. Es el dato que la "
        "coordinación necesita para decidir el refuerzo.")
    comp = [("Numérico-variacional", "momentos 1 y 2", 8),
            ("Espacial-métrico", "momentos 3 y 4", 8),
            ("Aleatorio", "momentos 5 y 6", 8)]
    an2 = (CW - 2 * 18) / 3
    for i, (nom, de, n) in enumerate(comp):
        x = M + i * (an2 + 18)
        b.append(rect(x, y, an2, 212, "white", r=16, stroke=AZ_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, 184, AZ, r=3))
        b.append(T(x + 40, y + 46, [nom], 23, INK, weight="700"))
        b.append(T(x + 40, y + 76, [de + f" · {n} preguntas"], 20, GRAY, style="italic"))
        b.append(T(x + 40, y + 124, ["aciertos del grupo"], 19, GRAY))
        b.append(rect(x + 40, y + 136, an2 - 80, 56, AZ_BG, r=12, stroke=AZ_LN, sw=1.8))
        b.append(T(x + an2 / 2, y + 174, [f"de {n * 1}"], 22, GRAY, anchor="middle"))
    y += 212 + 34

    y = seccion(b, y, "Las cinco preguntas que se reparan en la clase 8",
        "Se eligen con el conteo de arriba, el mismo sábado de la clase 7. Anota aquí cuáles son "
        "y con qué instrumento se trabajaron la primera vez: el estudiante va a necesitar volver "
        "a esa página de su cuaderno.")
    cx = [M, M + 200, M + 560, M + 1160]
    b.append(rect(M, y, CW, 50, PIZ, r=12))
    for x, e in zip(cx, ["N.º", "MOMENTO Y PÁGINA", "CON QUÉ INSTRUMENTO SE TRABAJÓ",
                         "QUÉ FALLÓ EL GRUPO"]):
        b.append(T(x + 18, y + 33, [e], 17, "white", weight="700", ls=1.2))
    y += 50 + 8
    for k in range(1, 6):
        b.append(rect(M, y, CW, 84, "white", r=12, stroke=AZ_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, 64, VERDE, r=2))
        b.append(T(cx[0] + 54, y + 54, [str(k)], 26, VERDE, weight="700", anchor="middle"))
        for xi, xf in [(cx[1] + 18, cx[2] - 20), (cx[2] + 18, cx[3] - 20), (cx[3] + 18, W - M - 30)]:
            b.append(line(xi, y + 58, xf, y + 58, "#E6EAF0", 2))
        y += 84 + 7

    pie(b, 24, TOT)
    svg_close(b, OUT + "plan_mate_24.svg")


# ═══════════════════ hoja 17 · cierre del área ═══════════════════
def h17():
    b = svg_open()
    y = cabecera(b, "Cierre del área", "Los nueve avisos del libro, juntos, y lo que hay que devolver",
                 "PLANEADOR DEL DOCENTE", "9", "avisos del libro")

    y = seccion(b, y, "Los nueve avisos del libro, en una sola lista",
        "Para repasarlos antes de empezar el área, no cuando ya estás en la clase. Los de "
        "severidad alta impiden que un estudiante que razone bien llegue a la opción esperada.")
    cx = [M, M + 230, M + 400]
    b.append(rect(M, y, CW, 50, PIZ, r=12))
    for x, e in zip(cx, ["DÓNDE", "SEVERIDAD", "QUÉ PASA Y QUÉ HACES"]):
        b.append(T(x + 18, y + 33, [e], 17, "white", weight="700", ls=1.2))
    y += 50 + 8
    for m in range(1, 7):
        for preg, sev, que, hacer in AVISOS.get(m, []):
            c, bg, ln = SEV[sev]
            texto = que + "  →  " + hacer
            lin = wrap_px(texto, 22, CW - 450)
            h = max(72, 26 + len(lin) * 31)
            b.append(rect(M, y, CW, h, bg, r=12, stroke=ln, sw=1.8))
            b.append(rect(M + 10, y + 10, 4, h - 20, c, r=2))
            b.append(T(cx[0] + 40, y + h / 2 + 8, [f"M{m} · {preg}"], 22, INK, weight="700"))
            chip(b, cx[1] + 18, y + h / 2 - 16, sev.upper(), c, size=15, pad=12, fill="white", txtc=c)
            parrafo_j(b, cx[2] + 18, y + (h - len(lin) * 31) / 2 - 5, texto, CW - 450, 22, INK, lh=31)
            y += h + 7
    y += 28

    y = nota(b, M, y, CW,
        "Ninguno de estos avisos se le oculta al estudiante. En los casos de fondo el instrumento "
        "de la pregunta lo obliga a contar o calcular por su cuenta y le deja un renglón para "
        "escribir qué no le cuadró. Un estudiante que detecta un error del libro y lo escribe "
        "aprendió más que uno que marcó la opción esperada.",
        AZ, AZ_BG, AZ_LN, "Por qué el cuaderno no los esconde", 26) + 34

    y = seccion(b, y, "Qué tienes que devolver al terminar el área")
    dev = [("Los cuatro registros de clase", "uno por cada clase de contenido, con nombres"),
           ("El conteo por componente del simulacro", "el dato que decide el refuerzo"),
           ("Lo que cambiarías", "va al reporte de los especialistas, que es entregable del proyecto"),
           ("Los avisos nuevos que encuentres", "si hallas un error que no está en esta lista, "
            "escríbelo: la lista se construyó resolviendo, y seguro falta alguno")]
    for t, s_ in dev:
        lin = wrap_px(s_, 23, CW - 620)
        h = max(76, 30 + len(lin) * 32)
        b.append(rect(M, y, CW, h, "white", r=16, stroke=AZ_LN, sw=2))
        b.append(rect(M + 14, y + 12, 5, h - 24, ORO, r=3))
        b.append(checkbox(M + 42, y + h / 2 - 13, 13, AZ))
        b.append(T(M + 100, y + h / 2 + 8, [t], 24, INK, weight="700"))
        parrafo_j(b, M + 580, y + (h - len(lin) * 32) / 2 - 4, s_, CW - 620, 23, GRAY, lh=32)
        y += h + 12

    pie(b, 17, TOT)
    svg_close(b, OUT + "plan_mate_17.svg")


# ═══════════════════════ banco de dinámicas ═══════════════════════
# Regla de aprobación (del piloto, y vale para las seis áreas): la dinámica debe ser
# ISOMORFA a la estrategia. Lo que hace el cuerpo tiene que ser el mismo movimiento que
# después hará la mente frente a la pregunta. Si no se puede decir qué paso de la
# estrategia ejercita, es recreo, no clase.
# (nombre, minutos, cómo se hace, qué movimiento mental entrena, material)
DINAMICAS = {
 1: [("La gráfica humana", 8,
      ["Seis estudiantes se paran en fila sobre una cinta en el piso: cada uno es un segundo.",
       "El docente dice la altura de cada segundo; el estudiante se agacha, se para o estira "
       "los brazos según qué tan alto sea el valor.",
       "El resto del grupo, desde el frente, «lee» la figura: ¿sube, baja, hay un pico?",
       "Quien quedó más alto levanta la mano. Ahí se nombra el cambio de dirección."],
      "Ubicar el vértice y detectar en qué punto la curva deja de subir. Es exactamente el "
      "movimiento de las preguntas 1, 2 y 3.",
      "Espacio despejado · cinta en el piso como eje"),
     ("La cadena de a tantos", 8,
      ["El grupo se para en círculo. El docente da una base («arrancamos en 10.000») y una "
       "regla fija («cada uno suma 2.500»).",
       "Van diciendo su valor en voz alta, uno tras otro, sin calculadora.",
       "Quien se equivoca pasa al centro y debe decir cuál era el dato fijo que se repetía.",
       "Variante: a mitad de ronda el docente cambia la base pero deja la misma regla."],
      "Separar la base de partida del valor que se repite. Es la estructura de C(x) = mx + b "
      "que resuelven las preguntas 4, 5 y 6.",
      "Círculo de sillas · una tarjeta con la base"),
     ("La misma máquina, tres preguntas", 10,
      ["Se escribe un solo modelo en el tablero y no se borra en toda la dinámica.",
       "Tres estudiantes sacan una tarjeta al azar: «dame el valor», «dame la entrada», "
       "«¿se puede?».",
       "Cada uno dice qué operación necesita, SIN hacerla todavía.",
       "El grupo vota si la operación es la correcta; solo entonces se calcula."],
      "Ver que el mismo modelo responde preguntas distintas según de qué lado se despeje. Es "
      "el movimiento de las preguntas 7, 8 y 9.",
      "Tablero · tres tarjetas con los tipos de pregunta"),
     ("La fila de las diferencias", 8,
      ["Ocho estudiantes en fila, cada uno con un número de la sucesión en una hoja.",
       "Otros se paran entre dos y dicen en voz alta la diferencia que ven.",
       "Si las diferencias no son iguales, se forma una segunda fila: las diferencias de las "
       "diferencias.",
       "Nadie opera en papel. Si la segunda fila sale pareja, el patrón ya está encontrado."],
      "Mirar las diferencias antes que los números. Es el movimiento de la pregunta 10 y de la "
      "del ICFES sobre la sucesión 11, 17, 29, 53, 101.",
      "Ocho hojas con números · espacio para dos filas")],
 2: [("El techo del salón", 8,
      ["Se marcan cinco posiciones en el piso, una por periodo de la tabla.",
       "Cada estudiante se para en la suya y levanta los brazos a la altura de su valor.",
       "Antes de mirar, el grupo apuesta en voz alta cuál creen que es el más alto.",
       "Regla única: quien dice «el último» sin haber mirado los datos queda fuera de la ronda."],
      "No confundir el máximo con el final de la serie, que es el error que el libro mismo "
      "comete en la pregunta 1. Es el movimiento de las preguntas 1 y 3.",
      "Cinco marcas en el piso · la tabla en el tablero"),
     ("Un solo dato basta", 8,
      ["Queda una tabla a la vista en el tablero durante toda la dinámica.",
       "El docente lee una afirmación sobre esos datos. El grupo tiene 30 segundos.",
       "Quien encuentra UN dato que la contradiga lo dice en voz alta y se sienta.",
       "Si nadie lo encuentra, la afirmación queda en pie y se pasa a la siguiente."],
      "Refutar es señalar un contraejemplo, no opinar. Un solo número tumba la afirmación. Es "
      "el movimiento de las preguntas 2 y 4.",
      "Tablero con una tabla · reloj a la vista"),
     ("Dos filas que crecen", 10,
      ["Dos equipos arrancan con una persona de pie cada uno.",
       "El equipo A suma dos personas por ronda. El equipo B duplica las que tiene.",
       "Se juegan cuatro rondas en voz alta: el grupo ve con el cuerpo que B explota.",
       "Al final se pregunta: en la ronda 6, ¿cuántos habría en cada fila? Nadie opera, estiman."],
      "Distinguir con el cuerpo la suma constante del crecimiento que se multiplica. Es el "
      "movimiento de las preguntas 5, 6 y 7.",
      "Espacio al fondo del salón para dos filas"),
     ("Lo que entra y lo que sale", 8,
      ["Dos cajas en el piso rotuladas ENTRA y SALE.",
       "Cada estudiante recibe una tarjeta con un dato del problema.",
       "Antes de poner su tarjeta tiene que decir en voz alta en qué caja va y por qué.",
       "Al final se cuenta cada caja: ¿sobra, falta, o cuadra?"],
      "Ordenar los datos antes de concluir, en vez de operar con el primer número que aparece. "
      "Es el movimiento de las preguntas 8, 9 y 10.",
      "Dos cajas rotuladas · una tarjeta por dato")],
 3: [("El cuerpo por partes", 8,
      ["Con pupitres o cajas de cartón se arma en el salón un cuerpo compuesto.",
       "El grupo tiene que separarlo físicamente en las dos o tres piezas que sí sabe medir.",
       "Cada pieza se nombra en voz alta antes de tocar la calculadora.",
       "Si alguien propone una pieza cuya fórmula no puede escribir de memoria, no vale."],
      "Descomponer antes de calcular, y cobrar cada parte por separado. Es el movimiento de las "
      "preguntas 1, 8 y 9.",
      "Pupitres o cajas · espacio para armar y separar"),
     ("Dos sombras, un ángulo", 8,
      ["Con una linterna y dos objetos de alturas distintas se proyectan dos sombras.",
       "Se mide cada sombra y cada altura y se escriben las dos razones en el tablero.",
       "El grupo decide: ¿qué cambió entre los dos objetos y qué no cambió?",
       "Se mueve la linterna y se repite: la razón se mantiene, los tamaños no."],
      "Reconocer qué se conserva entre dos figuras semejantes, y que «altura : sombra» no es lo "
      "mismo que «sombra : altura». Es el movimiento de las preguntas 2 y 3.",
      "Una linterna · dos objetos de alturas distintas · metro"),
     ("Cabe o no cabe", 10,
      ["Se pone una caja al frente y un objeto que podría ir adentro.",
       "Antes de probar, cada equipo escribe su predicción: cuántos caben y en qué orden.",
       "Se prueba de verdad, metiéndolos uno por uno.",
       "Quien dividió volúmenes sin mirar las tres dimensiones explica por qué falló."],
      "Medir el hueco y medir lo que se va a meter, y comprobar que encaje en las tres "
      "dimensiones. Es el movimiento de las preguntas 4 y 5.",
      "Una caja y varios objetos iguales · metro"),
     ("La torre piso por piso", 8,
      ["Se arma una torre con vasos o cajas, de a un piso por turno.",
       "Antes de poner su piso, el estudiante dice en voz alta la medida que se acumula.",
       "Si pone el piso sin decir la medida, la torre se devuelve al piso anterior.",
       "Al llegar al tope se pregunta: ¿cuánto falta para el techo y de dónde puede salir?"],
      "Medir antes de mover, y acumular la medida piso por piso. Es el movimiento de las "
      "preguntas 6, 7 y 10.",
      "Vasos o cajas iguales · metro · espacio vertical")],
 4: [("Una, dos, tres dimensiones", 8,
      ["Tres zonas marcadas en el piso: LARGO, ÁREA y VOLUMEN.",
       "El docente dice una magnitud en palabras cotidianas: «los metros de cerca», «el pasto "
       "que cubre», «el agua que llena».",
       "Cada estudiante corre a la zona que cree.",
       "Quien se equivoca no sale: tiene que decir en qué unidad se mide la zona a la que fue."],
      "No confundir lo que mide con lo que cubre y lo que llena, que es donde se pierde el "
      "componente. Es el movimiento de las preguntas 1, 2 y 9.",
      "Tres zonas marcadas en el piso"),
     ("El triángulo con nombre", 8,
      ["Se dibuja un triángulo rectángulo grande en el tablero y se marca un ángulo.",
       "Por turnos, cada estudiante pasa y rotula UN lado respecto a ese ángulo: opuesto, "
       "adyacente o hipotenusa.",
       "Nadie puede escribir una razón hasta que los tres lados tengan nombre.",
       "Se cambia el ángulo marcado y se vuelven a rotular: dos lados cambian de nombre."],
      "Ponerle nombre a cada lado antes de escribir la razón, y ver cuáles dos forman la "
      "esquina recta. Es el movimiento de las preguntas 3 y 4, y de la del ICFES sobre "
      "cosecante y secante.",
      "Tablero · marcador de otro color para el ángulo"),
     ("La figura que sí sé medir", 10,
      ["Cada equipo recibe dibujada una figura compuesta distinta.",
       "Tienen que partirla con una sola línea y nombrar las dos figuras que les quedaron.",
       "Escriben de memoria la fórmula de cada una de las dos.",
       "Gana el equipo cuya partición use solo figuras cuya fórmula pudo escribir sin consultar."],
      "Partirla en dos figuras que sí sabes medir, en vez de buscar una fórmula para el "
      "contorno completo. Es el movimiento de las preguntas 6 y 7.",
      "Una hoja con la figura por equipo"),
     ("Sigue el procedimiento tal cual", 8,
      ["El docente lee en voz alta un procedimiento paso por paso.",
       "Lo ejecuta en el tablero exactamente como está escrito, incluso donde está mal.",
       "El grupo tiene que detener al docente en el paso donde se rompe.",
       "Quien lo detiene debe decir qué paso falló, no cuál es la respuesta correcta."],
      "Seguir el procedimiento paso por paso en vez de estimar a ojo. Es el movimiento de las "
      "preguntas 5, 8 y 10, y de la del ICFES sobre regla y escuadra.",
      "Tablero · el procedimiento escrito en una hoja")],
 5: [("Cuatro preguntas, cuatro medidas", 8,
      ["Se escriben en el tablero las edades reales del salón, todas.",
       "El docente hace cuatro preguntas seguidas: ¿cuál es la más común?, ¿quién está justo en "
       "la mitad?, ¿cuánto se reparte?, ¿cuánto separa al mayor del menor?",
       "Para cada una, el grupo grita QUÉ MEDIDA la responde, no el número.",
       "Solo al final se calculan las cuatro y se comprueba cuál servía para cuál."],
      "Que cada palabra se mide en una columna distinta, y que la pregunta decide cuál medida "
      "sirve. Es el movimiento de las preguntas 1 y 3.",
      "Tablero · las edades del propio salón"),
     ("El salón es el 100 %", 8,
      ["Se usa el propio salón como población y se cuenta en voz alta cuántos son.",
       "El docente pide un porcentaje: «que se pare el 25 %».",
       "Antes de pararse, el grupo tiene que decir cuántas personas son.",
       "Variante: salen cinco del salón y se repite el mismo porcentaje. El número cambia."],
      "Que el porcentaje depende del total sobre el que se calcula, y que primero se junta el "
      "porcentaje y después se pasa a personas. Es el movimiento de las preguntas 2, 7 y 9.",
      "El propio salón · nada más"),
     ("Una cuenta por afirmación", 10,
      ["Queda una tabla a la vista y se reparten cuatro afirmaciones en tarjetas.",
       "Cada equipo toma una y solo puede responder con UNA cuenta corta escrita.",
       "No se acepta un argumento sin cuenta, ni una cuenta sin la afirmación al lado.",
       "Se leen las cuatro cuentas y el grupo decide cuáles afirmaciones se sostienen."],
      "Una cuenta corta por cada afirmación, en vez de juzgarlas todas de una mirada. Es el "
      "movimiento de las preguntas 4, 5 y 6.",
      "Tablero con la tabla · cuatro tarjetas"),
     ("Los cuatro casos en el piso", 8,
      ["Cuatro zonas en el piso, una por opción de respuesta.",
       "Cada estudiante empieza parado en la zona que cree.",
       "El docente lee los casos uno por uno; quien ya no se sostiene en su zona se mueve.",
       "Regla para moverse: hay que decir en voz alta cuál caso lo sacó de ahí."],
      "Probar los cuatro casos en vez de quedarse con el que suena bien. Es el movimiento de "
      "las preguntas 8 y 10.",
      "Cuatro zonas marcadas en el piso")],
 6: [("Dos métodos, un resultado", 8,
      ["Se plantea un conteo y dos procedimientos distintos para resolverlo.",
       "Dos estudiantes los ejecutan en el tablero al mismo tiempo, uno cada uno.",
       "Cuando dan resultados distintos, el grupo no dice cuál está bien.",
       "Tiene que decir QUÉ SUPONE cada método: si cuenta el orden, si permite repetir."],
      "Juzgar qué supone cada método antes de decidir cuál sirve. Es el movimiento de las "
      "preguntas 1, 3 y 4.",
      "Tablero dividido en dos · dos marcadores"),
     ("La lista con los dedos", 10,
      ["Se plantea un conteo pequeño: tres dígitos, dos colores, algo que se pueda listar.",
       "El grupo escribe a mano la lista COMPLETA de casos que sirven. Nadie dice una fórmula.",
       "Se cuenta la lista en voz alta.",
       "Recién ahí se busca qué fórmula da ese número, y se comprueba contra la lista."],
      "Escribir la lista de los casos que sirven antes de buscar la fórmula, que es lo único "
      "que evita adivinar. Es el movimiento de las preguntas 2 y 9, y de la del candado.",
      "Hojas y lápiz · nada de calculadora"),
     ("Lo que midió y lo que dijo", 8,
      ["Se escribe en el tablero un dato real de encuesta y se deja a la vista.",
       "Dos zonas en el piso: LO DICE EL DATO y LO AGREGA EL ANALISTA.",
       "El docente lee cuatro afirmaciones; cada uno se para en una zona.",
       "Para quedarse hay que señalar la palabra exacta que lo hizo decidir."],
      "Separar lo que la encuesta midió de lo que el analista afirmó, y ver que riesgo no es "
      "pérdida. Es el movimiento de las preguntas 5, 7 y 10.",
      "Tablero con el dato · dos zonas marcadas"),
     ("La caja antes y después", 8,
      ["Una caja con fichas de dos colores, contadas a la vista de todos.",
       "Se pregunta la probabilidad de sacar un color. Cada uno la escribe.",
       "Se saca una ficha y NO se devuelve. Se vuelve a preguntar.",
       "Antes de dar la nueva probabilidad hay que escribir el nuevo total."],
      "Ver que el total cambia cuando quitas lo que te dieron, y que hay que redibujar la caja. "
      "Es el movimiento de las preguntas 6 y 8.",
      "Una caja opaca · fichas de dos colores")],
}

RETOS = {
 1: ("El modelo de otro equipo", 20,
     "Cada equipo de tres recibe una situación distinta con cuatro datos. En diez minutos deben: "
     "(1) escribir el modelo que la describe, (2) decir si es lineal o no y por qué, y (3) predecir "
     "el quinto dato. Después intercambian hojas: el otro equipo tiene que responder una pregunta "
     "nueva usando el modelo que recibió, sin rehacerlo. Gana el equipo cuyo modelo le sirvió al otro."),
 2: ("Techo, regla y contraejemplo", 20,
     "Cada equipo recibe una tabla y tres afirmaciones sobre ella. En doce minutos deben marcar el "
     "máximo y el periodo en que se alcanza, escribir la regla en una frase y tumbar al menos una de "
     "las tres afirmaciones con un dato. Exponen en tres minutos citando el dato, no la opinión. Gana "
     "el equipo que tumbe la afirmación con el dato más corto."),
 3: ("Cabe, no cabe y por qué", 20,
     "Cada equipo recibe un cuerpo compuesto dibujado y un espacio donde debería caber. En doce "
     "minutos deben partir el cuerpo en piezas medibles, calcular lo que ocupa y decidir si cabe. La "
     "decisión no basta: tienen que nombrar cuál de las tres dimensiones es la que decide. Gana el "
     "equipo que identifique la dimensión crítica, aunque el cálculo le quede largo."),
 4: ("El procedimiento ajeno", 20,
     "Cada equipo recibe el procedimiento escrito de otro equipo, con un error sembrado por el "
     "docente. En doce minutos deben ejecutarlo tal como está, encontrar el paso donde se rompe y "
     "escribir la corrección en una sola línea. Gana el equipo que encuentre el paso exacto; no gana "
     "el que llegue al número correcto por otro camino."),
 5: ("La misma tabla, cuatro preguntas", 20,
     "Todos los equipos reciben la MISMA tabla, pero cada uno una pregunta distinta. En doce minutos "
     "deben responderla con una cuenta corta y decir qué medida usaron. Al exponer, el grupo tiene "
     "que adivinar cuál era la pregunta de cada equipo oyendo solo su cuenta. Gana el equipo cuya "
     "cuenta deje ver la pregunta sin que la digan."),
 6: ("Hasta dónde llega el dato", 20,
     "Cada equipo recibe un titular de prensa y el dato de encuesta que lo respalda. En doce minutos "
     "deben subrayar en el titular lo que el dato sí sostiene y lo que el titular agregó. Después "
     "escriben un titular nuevo que diga exactamente lo que el dato permite. Gana el equipo cuyo "
     "titular nuevo sea el más corto sin dejar de ser cierto."),
}


def hoja_dinamicas(mis):
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Dinámicas · Misión {mis}",
                 "Movimiento con sentido: el cuerpo ensaya lo que después hará la mente",
                 "PLANEADOR DEL DOCENTE", f"{mis}", "de 6 misiones")

    y = nota(b, M, y, CW,
        "La dinámica debe ser isomorfa a la estrategia: lo que hace el cuerpo tiene que ser el "
        "mismo movimiento que después hará la mente frente a la pregunta. Antes de usar una, "
        "responde esto — ¿qué paso de la estrategia está ejercitando? Si no hay respuesta, es "
        "recreo, no clase.",
        ORO, ORO_BG, ORO_LN, "La regla para aprobar cualquier dinámica", 25) + 30

    cols = [AZ, VERDE, ORO, "#5B3E96"]
    for i, (nom, mins, pasos, entrena, material) in enumerate(DINAMICAS[mis]):
        c = cols[i]
        anc = (CW - 100) / 2
        lin_p = sum(len(wrap_px(p_, 22, anc - 60)) for p_ in pasos)
        l_ent = wrap_px(entrena, 22, anc - 20)
        alto_cols = max(lin_p * 31 + len(pasos) * 16, len(l_ent) * 31 + 34) + 30
        h = 128 + alto_cols
        b.append(rect(M, y, CW, h, "white", r=20, stroke=AZ_LN, sw=2.2))
        b.append(rect(M + 16, y + 18, 5, h - 36, c, r=3))
        w = chip(b, M + 44, y + 34, f"E{i+1}", c, size=19, pad=19)
        b.append(T(M + 44 + w + 26, y + 60, [nom], 27, INK, weight="700"))
        wm = chip(b, M + 44 + w + 26, y + 76, f"{mins} min", c, size=18, pad=15)
        b.append(T(M + 44 + w + 26 + wm + 18, y + 100,
                   [f"· entrena la estrategia «{d['estr'][i]}»"], 20, GRAY, style="italic"))
        b.append(T(W - M - 44, y + 48, [material], 19, GRAY, anchor="end"))

        yy = y + 120
        b.append(T(M + 44, yy + 18, ["CÓMO SE HACE"], 17, c, weight="700", ls=1.4))
        b.append(T(M + 60 + anc + 40, yy + 18, ["QUÉ MOVIMIENTO MENTAL ENTRENA"], 17, c,
                   weight="700", ls=1.4))
        b.append(line(M + 44 + anc + 20, yy + 34, M + 44 + anc + 20, y + h - 22, "#E6EAF0", 2))
        yp = yy + 30
        for p_ in pasos:
            b.append(f'<circle cx="{M+56}" cy="{yp+18}" r="5.5" fill="{c}"/>')
            yp = parrafo_j(b, M + 80, yp, p_, anc - 60, 22, INK, lh=31) + 16
        parrafo_j(b, M + 60 + anc + 40, yy + 30, entrena, anc - 20, 22, INK, lh=31)
        y += h + 14

    nom_r, min_r, txt_r = RETOS[mis]
    y += 8
    lin = wrap_px(txt_r, 23, CW - 90)
    h = 112 + len(lin) * 32
    b.append(rect(M, y, CW, h, "#F3F0FB", r=20, stroke="#D6CCEE", sw=2.2))
    b.append(rect(M + 16, y + 18, 5, h - 36, "#5B3E96", r=3))
    b.append(T(M + 44, y + 54, [f"Reto del corte · {nom_r}"], 26, "#5B3E96", weight="700"))
    b.append(T(M + 44, y + 86, [f"{min_r} min · trabajo en equipo, registro individual"], 20,
               GRAY, style="italic"))
    parrafo_j(b, M + 44, y + 98, txt_r, CW - 90, 23, INK, lh=32)

    pie(b, 17 + mis, TOT)
    svg_close(b, OUT + f"plan_mate_{17 + mis:02d}.svg")


def build():
    h1(); h2()
    hoja_momentos(1); hoja_momentos(2)
    for m in range(1, 7):
        hoja_clase(m); hoja_clase_b(m)
    h16()
    for m in range(1, 7):
        hoja_dinamicas(m)
    h17()
    return [f"plan_mate_{i:02d}" for i in range(1, TOT + 1)]


if __name__ == "__main__":
    hojas = build()
    print(len(hojas), "hojas del planeador de Matemáticas")
