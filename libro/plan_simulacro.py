#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Clases 7 y 8 de los planeadores · el simulacro de EDUCATE y su socialización en el cuaderno.

Decisión de Nelson (10 nov): el simulacro deja de repetir las 24 preguntas de entrenamiento, que el
estudiante ya resolvió con instrumento.
    Clase 7 · el estudiante presenta el simulacro del área que aplique EDUCATE: una prueba que NO está
              en el cuaderno (el instituto escoge el cuadernillo o el PTD). Al final anota en su
              cuaderno qué preguntas quiere socializar.
    Clase 8 · se socializan preguntas de ese simulacro en las HOJAS DE SIMULACRO del cuaderno, al final
              de cada área (simulacro.py, v2): membrete, «me piden», caja de herramientas, cierre del
              área, «tacho con razón», salvavidas y «lo que me llevo». Las hojas alcanzan para 30
              preguntas en Matemáticas, Lectura Crítica y Sociales, y para 18 en las demás.

Un solo lugar para las seis áreas que lo usan (Matemáticas, Sociales, Biología, Química, Física e
Inglés; Lectura Crítica tiene su planeador aparte). Cada plan_<área>.py llama a

    C7, C8 = plan_simulacro.datos(clave, conteo=…, dinamica=…, previo=…)

y deja C7 y C8 como variables del módulo, para el agente de las guías (clase_viva_*.py). Las llaves
son las mismas que usa plan_lc.py (C7, C8 de Lectura Crítica), más algunas propias:

    C7 = dict(titulo, sub, donde,                        # qué es y dónde se presenta (fuera del cuaderno)
              tiempos=[(nombre, minutos, texto)],          # 10 · 90 · 20 = 120
              pasos=[…], no_hace, cuaderno,                # cómo se aplica · lo que no hace · qué se toca del cuaderno
              que_es, registra=[…], al_final, conteo)      # propias: qué cambió, qué registra el profe, qué anota
    C8 = dict(titulo, sub, paginas=[…], esquema=[(pieza, texto)],
              reparto=dict(escoge=3, asigna=3, regla),     # cómo se escogen las preguntas
              dinamica=(nombre, minutos, [pasos], entrena, material),   # la forma de DINAMICAS
              fases=[texto × 6],                           # las seis fases aprobadas, 15·20·35·20·20·10
              no_hace,
              rango, hojas, preguntas_cuaderno,            # propias: «a a b», hojas y preguntas del cuaderno
              por_simulacro=dict(hojas, paginas, preguntas, escogidas, asignadas),
              formato, revisa, alcance)                    # parejas o equipos · qué mira el profe · cuántas hojas

    hoja(b, y, C7, C8, col, bg, ln, seccion, nota)  dibuja el cuerpo de la hoja «Clases 7 y 8»
                                                   debajo de la cabecera; devuelve el y final.
Las piezas del esquema salen de simulacro.py (V2, AREA, HOJAS): si el esquema cambia, el planeador lo
sigue.
"""
from lib import *
import paginas as PG
import simulacro as SIM

ROJO = "#A82424"; ROJO_BG = "#FBEFEF"; ROJO_LN = "#E6C4C4"
VERDE = "#2E7A39"; VERDE_BG = "#EDF5EE"; VERDE_LN = "#C3DEC8"
MORADO = "#5B3E96"; MORADO_BG = "#F3F0FB"; MORADO_LN = "#D6CCEE"
ORO = "#C9821B"; ORO_BG = "#FDF5E7"; ORO_LN = "#E8CFA3"
COL_FASE = [None, ROJO, "#3B3BA6", MORADO, ORO, VERDE]   # el primero es el color del área
FASES_NOM = [("Activación", 15), ("Pregunta problematizadora", 20), ("Desarrollo guiado", 35),
             ("Reto en equipo", 20), ("Evaluación individual", 20), ("Cierre", 10)]   # aprobado: no se cambia

# La pieza de la izquierda y la que cierra el razonamiento, con el nombre que trae la hoja del cuaderno.
IZQ = {"evidencia": ("La evidencia", "copia la frase exacta (o señala la parte de la imagen) y dice dónde está"),
       "situacion": ("La situación", "quién, dónde y cuándo, en el óvalo"),
       "vaso": ("Las sustancias", "lo que hay en el vaso y los datos que usa, con unidad"),
       "magnitudes": ("Las magnitudes", "símbolo = valor y unidad")}
DER = {"comprobacion": ("La comprobación", "marca cómo comprobó: lo reemplazó en el enunciado, unidad y "
                        "tamaño creíbles, un caso que la tumba o el paso con el error"),
       "trampas": ("Las trampas", "pone la letra de la trampa en cada opción que tacha: N no lo dice, O dice "
                   "otra cosa, E exagera o generaliza, R es cierta pero no responde"),
       "concluyo": ("Lo que sí concluyo", "solo lo que los datos dicen; y debajo, «lo que no alcanza»"),
       "propiedad": ("Lo que decide", "la propiedad, el modelo o la ley; y marca si átomos y masa cuadran"),
       "ley": ("La ley que manda", "el principio y su fórmula; y marca si las unidades cuadran"),
       "pista": ("La pista que manda", "la palabra de al lado, el tiempo del verbo, el lugar o quién habla, "
                 "un conector o un número")}


def _y(lista, conj="y"):
    """['a', 'b', 'c'] → «a, b y c»."""
    lista = list(lista)
    return lista[0] if len(lista) == 1 else ", ".join(lista[:-1]) + f" {conj} " + lista[-1]


def _q(lista, conj="y"):
    return _y((f"«{x}»" for x in lista), conj)


def _rango(ps):
    return f"{ps[0]} a {ps[-1]}"


def esquema(clave):
    """[(pieza, qué hace el estudiante)] del esquema de la hoja de simulacro del área."""
    a, v = SIM.AREA[clave], SIM.V2[clave]
    filas_m = [a["rot_comp"].lower()] + ([a["rot_compo"].lower()] if a["rot_compo"] else [])
    memb = (f"El n.º de la pregunta; si la escogió o se la asignaron; qué marcó y cuál era; el nivel que le "
            f"exige; {_y(filas_m)}; y la estrategia: la misión donde la entrenó y la que usó.")
    l2 = v["linea2"]
    if l2 == "predigo":
        l2t = "y escribe su predicción antes de mirar: si aumenta o disminuye, entonces…"
    elif l2[0] == "texto":
        l2t = f"y escribe «{l2[1].rstrip(':')}»."
    else:
        l2t = f"y encierra {l2[1].replace('¿', '').rstrip('?').lower()}: {_q(l2[2], 'o')}."
    pide = f"marca qué tipo de tarea es ({_q(v['pide'], 'o')}) {l2t}"
    iz = v["izq"]
    iz_t, iz_d = (iz[0].capitalize(), iz[1]) if isinstance(iz, tuple) else IZQ[iz]
    herr = [h[0] for h in v["herr"]]
    centro = v["centro"].capitalize()
    usa = (f"«{iz_t[0].upper() + iz_t[1:].lower()}»: {iz_d}. Después marca una herramienta de la caja "
           f"({_q(herr, 'o')}) y razona con ella en «{centro.lower()}».")
    d = v["der"]
    der_t, der_d = ((d[0].capitalize(), d[1] + ": lo escribe en una línea; es lo que decide la pregunta")
                    if isinstance(d, tuple) else DER[d])
    der_t = der_t[0].upper() + der_t[1:].lower()
    if v.get("pie") == "ing":
        tacho = ("Descarté", "Una razón por cada opción que descarta, y una palabra nueva con su "
                 "significado.")
    elif d == "trampas":
        tacho = ("Tacho con razón", "Una razón por cada opción descartada, con la letra de su trampa.")
    else:
        tacho = ("Tacho con razón", "Una razón por cada opción descartada. La opción se marca al final.")
    return [("Membrete", memb),
            ("Me piden", pide[0].upper() + pide[1:]),
            (f"{iz_t[0].upper() + iz_t[1:].lower()} y la herramienta", usa),
            (der_t, der_d[0].upper() + der_d[1:] + "."),
            tacho,
            ("Salvavidas y lo que me llevo", "Dónde se perdió y la pista que no vio; y una frase que le "
             "sirva en el examen de verdad.")]


def datos(clave, conteo, dinamica, previo=None):
    """C7 y C8 del área. conteo: cómo se cuenta el resultado («competencia», «parte»…);
    dinamica: dict(nombre, formato, pasos, entrena); previo: lo que se hace antes en la activación
    de la clase 8 (Inglés: la ronda de claves de la última tarea)."""
    pags = PG.paginas_simulacro(clave)
    n_hojas = SIM.HOJAS[clave]
    assert len(pags) == 2 * n_hojas, f"{clave}: {len(pags)} páginas de simulacro y {n_hojas} hojas"
    n_preg = 3 * len(pags)
    sim = _rango(pags)
    herr = [h[0] for h in SIM.V2[clave]["herr"]]
    C7 = dict(
        titulo="Clase 7 · el simulacro de EDUCATE",
        sub="Condiciones de examen, en silencio y con reloj",
        donde=("Fuera del cuaderno: el simulacro del área que aplique EDUCATE, en cuadernillo o en PTD "
               "(lo escoge el instituto)."),
        que_es=("El estudiante presenta el simulacro del área que aplique EDUCATE: el instituto escoge el "
                "cuadernillo o el PTD. No está en el cuaderno y no repite las 24 preguntas de entrenamiento, "
                "que el estudiante ya resolvió con instrumento."),
        tiempos=[
            ("Antes de empezar", 10,
             "Puestos separados, celulares guardados, lápiz, borrador y la hoja de respuestas (o el ingreso a "
             "la PTD). Escribe en el tablero la hora de inicio y la de cierre. Cuaderno cerrado."),
            ("La prueba", 90,
             "En silencio y de corrido. El número de preguntas lo fija el simulacro que escogió EDUCATE; como "
             "referencia, unos dos minutos por pregunta. Las respuestas van solo en la hoja de respuestas; las "
             "cuentas y las marcas, en el cuadernillo, si EDUCATE lo deja rayar, o en hoja borrador."),
            ("Lo que anoto para socializar", 20,
             f"Se recogen las hojas de respuestas. Cada uno abre su cuaderno en la primera hoja de simulacro "
             f"libre (páginas {sim}), llena «Me llamo · Simulacro · Sesión» y, en el membrete de tres "
             f"esquemas, el n.º de cada pregunta que quiere socializar, «la escogí yo» y la letra que marcó."),
        ],
        pasos=["Condiciones de examen: puestos separados, sin celular, sin hablar.",
               "Hoja de respuestas aparte (o la PTD); el cuaderno del área no se abre durante la prueba.",
               "No se responde ninguna duda, ni de vocabulario, y no se dice ninguna clave.",
               f"Al final, en las hojas de simulacro (páginas {sim}), cada uno anota tres preguntas que "
               f"quiere socializar. «Era» queda vacío hasta la clase 8."],
        no_hace="No corrige, no adelanta claves y no comenta el simulacro: todo eso es la clase 8.",
        cuaderno=(f"Hojas de simulacro, páginas {sim}: solo el encabezado y el membrete de tres esquemas "
                  f"(n.º, «la escogí yo», «Marqué»)."),
        registra=[
            "Hora de inicio y de entrega de cada uno, y quién no terminó.",
            "Todo reclamo sobre una pregunta (un dato que no cuadra, dos opciones posibles): se anota y va "
            "a los hallazgos. No se discute durante la prueba.",
            "En la semana: cuántos fallaron cada pregunta. Las tres más falladas son las que asignas en la "
            "clase 8.",
            f"Los aciertos por {conteo}: el dato que decide el refuerzo. No es nota."],
        al_final=("Cada estudiante anota en su cuaderno el n.º de las tres preguntas que quiere socializar: "
                  "la que dudó, la que cree que falló o la que acertó sin saber por qué."),
        conteo=conteo,
    )
    assert sum(t[1] for t in C7["tiempos"]) == 120
    act = (f"Devuelve el resultado sin notas: los aciertos por {conteo} en el tablero y las tres preguntas "
           f"más falladas. Cada uno escribe sus números en tres esquemas, con «me la asignaron» marcado.")
    if previo:
        act = previo + " " + act
    textos = [
        act,
        f"Modelas en el tablero la más fallada, pieza por pieza del esquema y en voz alta, y el grupo la "
        f"llena contigo. Ahí presentas la caja de herramientas: {_q(herr)}, y cuándo sirve cada una.",
        "Cada uno llena los esquemas de las tres que escogió. Pasas por los puestos mirando «me piden» y "
        "la herramienta, no la respuesta: la opción se marca al final.",
        f"La dinámica «{dinamica['nombre']}» ({dinamica['formato']}) con la segunda asignada. Cada uno "
        f"responde en SU esquema.",
        "En silencio, cada uno llena solo el esquema de la tercera asignada. Es el dato de seguimiento de "
        "la clase.",
        "Cada uno lee en voz alta el salvavidas de una pregunta y escribe «lo que me llevo». Carita de "
        "salida y la portada del área con las ocho clases marcadas.",
    ]
    C8 = dict(
        titulo="Clase 8 · la socialización en el cuaderno",
        sub=f"En las hojas de simulacro, páginas {sim}",
        paginas=list(pags), rango=sim, hojas=n_hojas, preguntas_cuaderno=n_preg,
        esquema=esquema(clave),
        reparto=dict(escoge=3, asigna=3,
                     regla="El estudiante escoge tres: las que anotó al final de la clase 7. El profe asigna "
                           "tres: las más falladas por el grupo. Si una ya la escogió el estudiante, él "
                           "escoge otra."),
        por_simulacro=dict(hojas=1, paginas=2, preguntas=6, escogidas=3, asignadas=3),
        dinamica=(dinamica["nombre"], 20, dinamica["pasos"], dinamica["entrena"],
                  dinamica.get("material", "El cuaderno, en la hoja de simulacro")),
        formato=dinamica["formato"],
        fases=textos,
        no_hace=("No resuelve todas las preguntas del simulacro ni dicta las claves en lista: se socializa la "
                 "pregunta que tiene esquema."),
        revisa=("Lo que revisas en cada esquema: que «me piden», la herramienta y el tacho con razón estén "
                "llenos. Un esquema con la opción marcada y el resto en blanco no cuenta como socializado."),
        alcance=(f"Por simulacro se usa una hoja: dos páginas, seis preguntas (tres escogidas y tres "
                 f"asignadas). El cuaderno trae {n_hojas} hojas ({len(pags)} páginas, {n_preg} preguntas): "
                 f"alcanzan para este simulacro y {_num(n_hojas - 1)} más, o para las preguntas que el "
                 f"estudiante quiera reparar en casa."),
    )
    return C7, C8


def _num(n):
    return {1: "uno", 2: "dos", 3: "tres", 4: "cuatro"}.get(n, str(n))


# ─────────────────────────────── el dibujo ───────────────────────────────
def _caja(b, x, y, w, h, c, bg, ln):
    b.append(rect(x, y, w, h, bg, r=18, stroke=ln, sw=2.2))
    b.append(rect(x + 14, y + 16, 5, h - 32, c, r=3))


def hoja(b, y, C7, C8, col, bg, ln, seccion, nota):
    """Cuerpo de la hoja «Clases 7 y 8», debajo de la cabecera. Devuelve el y final (tope 2470)."""
    COL_FASE[0] = col
    y = nota(b, M, y, CW, C7["que_es"] + " En la clase 8 se socializan preguntas de ese simulacro en las "
             f"hojas de simulacro del cuaderno (páginas {C8['rango']}).", ORO, ORO_BG, ORO_LN,
             "Qué cambió: el simulacro ya no está en el cuaderno", 22) + 26

    # ── clase 7: los 120 minutos a la izquierda, lo que registra el profe a la derecha
    wl = 1130
    wr = CW - wl - 20
    x2 = M + wl + 20
    filas = []
    reloj = 0
    for nom, mins, txt in C7["tiempos"]:
        filas.append((reloj, reloj + mins, nom, wrap_px(txt, 20, wl - 300)))
        reloj += mins
    alto_l = 104 + sum(max(2, len(l)) * 28 + 22 for *_, l in filas)
    alto_r = 104 + sum(len(wrap_px(r_, 20, wr - 96)) * 28 + 16 for r_ in C7["registra"])
    alto = max(alto_l, alto_r) + 8
    _caja(b, M, y, wl, alto, ROJO, ROJO_BG, ROJO_LN)
    b.append(T(M + 40, y + 48, [C7["titulo"]], 26, ROJO, weight="700"))
    b.append(T(M + 40, y + 80, [C7["sub"]], 19, GRAY, style="italic"))
    yy = y + 104
    for a_, b_, nom, lin in filas:
        b.append(T(M + 40, yy + 22, [f"{a_:02d}'–{b_:02d}'"], 20, ROJO, weight="700"))
        b.append(T(M + 40, yy + 50, [nom], 17, GRAY))
        parrafo_j(b, M + 270, yy, " ".join(" ".join(l) for l in lin), wl - 300, 20, INK, lh=28)
        yy += max(2, len(lin)) * 28 + 22
    b.append(rect(x2, y, wr, alto, "white", r=18, stroke=ROJO_LN, sw=2.2))
    b.append(rect(x2 + 14, y + 16, 5, alto - 32, ROJO, r=3))
    b.append(T(x2 + 40, y + 48, ["Qué registras tú"], 24, ROJO, weight="700"))
    b.append(T(x2 + 40, y + 80, ["esto no lo ve el estudiante"], 19, GRAY, style="italic"))
    yy = y + 100
    for r_ in C7["registra"]:
        b.append(checkbox(x2 + 40, yy + 6, 12, ROJO))
        yy = parrafo_j(b, x2 + 76, yy, r_, wr - 96, 20, INK, lh=28) + 16
    y += alto + 24

    # ── clase 8: cómo se escogen y el reparto de los 120 minutos
    _caja_h = 0
    xt0 = M + 172 + max(tw(f[0], 19, "700") for f in FASES_NOM) + 30
    filas8 = [(nom, mins, wrap_px(txt, 20, M + CW - 30 - xt0)) for (nom, mins), txt in zip(FASES_NOM, C8["fases"])]
    esc = C8["reparto"]["regla"]
    l_esc = wrap_px(esc, 20, CW - 90)
    alto8 = 116 + len(l_esc) * 28 + 18 + sum(len(l) * 28 + 16 for *_, l in filas8) + 6
    _caja(b, M, y, CW, alto8, VERDE, VERDE_BG, VERDE_LN)
    b.append(T(M + 40, y + 48, [C8["titulo"]], 26, VERDE, weight="700"))
    b.append(T(M + 40, y + 80, [C8["sub"] + " · seis preguntas por estudiante: una hoja, las dos caras"],
               19, GRAY, style="italic"))
    yy = parrafo_j(b, M + 40, y + 96, esc, CW - 90, 20, INK, lh=28, weight="700") + 18
    reloj = 0
    xn = M + 172                                    # columna del nombre de la fase
    xt = xn + max(tw(f[0], 19, "700") for f in FASES_NOM) + 30
    for i, (nom, mins, lin) in enumerate(filas8):
        c = COL_FASE[i]
        h = len(lin) * 28
        b.append(rect(M + 40, yy - 2, 6, h + 4, c, r=3))
        b.append(T(M + 62, yy + 21, [f"{reloj:02d}'–{reloj + mins:03d}'" if reloj + mins >= 100
                                     else f"{reloj:02d}'–{reloj + mins:02d}'"], 19, c, weight="700"))
        b.append(T(xn, yy + 21, [nom], 19, INK, weight="700"))
        parrafo_j(b, xt, yy, " ".join(" ".join(l) for l in lin), M + CW - 30 - xt, 20, INK, lh=28)
        reloj += mins
        yy += h + 16
    y += alto8 + 24

    # ── el esquema, pieza por pieza
    y = seccion(b, y, "La hoja de simulacro del cuaderno, pieza por pieza")
    wp = 380
    for pieza, txt in C8["esquema"]:
        lin = wrap_px(txt, 20, CW - wp - 50)
        h = max(52, 18 + len(lin) * 27)
        b.append(rect(M, y, CW, h, "white", r=12, stroke=ln, sw=1.8))
        b.append(rect(M + 10, y + 9, 4, h - 18, col, r=2))
        b.append(T(M + 32, y + h / 2 + 7, [pieza], 20, col, weight="700"))
        assert tw(pieza, 20, "700") < wp - 40, f"la pieza no cabe: {pieza}"
        parrafo_j(b, M + wp, y + (h - len(lin) * 27) / 2 - 4, txt, CW - wp - 50, 20, INK, lh=27)
        y += h + 6
    lin = wrap_px(C8["revisa"], 19, CW - 40)
    y = parrafo_j(b, M + 20, y + 4, C8["revisa"], CW - 40, 19, GRAY, style="italic", lh=26) + 22

    # ── la dinámica de socialización
    nom_d, min_d, pasos_d, entrena_d, _ = C8["dinamica"]
    anc = (CW - 100) / 2
    lin_p = sum(len(wrap_px(p_, 20, anc - 60)) for p_ in pasos_d)
    l_ent = wrap_px(entrena_d, 20, anc - 20)
    h = 116 + max(lin_p * 28 + len(pasos_d) * 10, len(l_ent) * 28 + 30) + 14
    _caja(b, M, y, CW, h, MORADO, MORADO_BG, MORADO_LN)
    b.append(T(M + 44, y + 50, [f"Dinámica de socialización · {nom_d}"], 25, MORADO, weight="700"))
    b.append(T(M + 44, y + 82, [f"{min_d} min · {C8['formato']} · registro individual, cada uno en su esquema"],
               19, GRAY, style="italic"))
    xr = M + 60 + anc + 40
    b.append(T(xr, y + 82, ["QUÉ PIEZA DEL ESQUEMA ENTRENA"], 16, MORADO, weight="700", ls=1.3))
    yp = y + 100
    for p_ in pasos_d:
        b.append(f'<circle cx="{M+56}" cy="{yp+16}" r="5" fill="{MORADO}"/>')
        yp = parrafo_j(b, M + 78, yp, p_, anc - 60, 20, INK, lh=28) + 10
    parrafo_j(b, xr, y + 100, entrena_d, anc - 20, 20, INK, lh=28)
    y += h + 20

    y = nota(b, M, y, CW, C8["alcance"], col, bg, ln, "Cuántas hojas se usan", 21)
    return y
