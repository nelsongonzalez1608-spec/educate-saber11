#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUÍAS DE CLASE PROYECTABLES («clase viva») · SOCIALES Y CIUDADANAS · las 8 del área.

    python3 clase_viva_soc.py [carpeta]      (por defecto entregables/guias_sociales/)

Usa el motor clase_viva.py sin cambiarlo: las mismas escenas, la misma plantilla y el mismo
JavaScript que las de Lectura Crítica. Lo que entra de Sociales:

  · plan_soc.py: FASES, MISIONES, TALLER, DINAMICAS, RETOS, SELLOS, SABERES, ACTIVACION,
    PROBLEMATIZADORA, PREGUNTA_AREA, NO_ES_TU_FUERTE, COLS_MIS, COMP_EST, BANCO y CLAVES.
  · textos_soc.py: los 24 textos ICFES de TEXTOS_GUIA_DOCENTE.md y las notas del taller.
  · lo escrito aquí: TITULOS, LEADS, la redacción de pantalla (UI) y a qué aviso del libro se
    le da pantalla (PROYECTAR). Lo demás de AVISOS va solo a la guía del profe.

Lo que hace este módulo además de llenar el Area:

  1. Un Area por misión, porque los colores de las estrategias cambian de misión a misión en el
     cuaderno (COLS_MIS): la guía pinta cada estrategia con el color de su chip en el cuaderno.
     Los momentos llevan los colores del planeador de Sociales (m5 = rojo de la evaluación), así
     el oro del área (#C9821B, momento 1) no se repite en el momento 5.
  2. La portada de cada clase trae en la guía del profe lo de antes del sábado (el «ojo» de la
     misión y los avisos que no son de una pregunta) y los cuatro conceptos de «Si Sociales no
     es tu fuerte» (NO_ES_TU_FUERTE).
  3. La pregunta modelo de Sociales es la 1 del libro (el planeador abre la página de las
     preguntas 1 y 2 «solo en mi primera idea»): la diapositiva lo dice con su página.
  4. Sin nombres de políticos colombianos vivos en el HTML (ni en pantalla ni en la guía):
     `revisar_nombres()` falla si aparece alguno. Los casos del libro que los traen se nombran
     sin ellos y remiten al libro.
  5. Las ICFES de las misiones 1 y 2 salen del compilado ASED: su guía del profe dice
     «Pendiente: confirmar fuente (ASED)».
  6. `[hidden]{display:none!important}`: en la plantilla, `.clave{display:flex}` le gana al
     atributo hidden y la clave del libro se ve antes de revelarla (pasa en las guías de LC
     entregadas). Aquí se agrega la regla del piloto aprobado; clase_viva.py no se toca.

Comprueba antes de escribir que las claves coinciden: plan_soc.CLAVES con el docstring de
socN.py (M3–M6), y la clave ICFES de TEXTOS_GUIA_DOCENTE.md con socN_icfes.py y icfes.csv.
"""
import copy, os, re, sys, types

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import clase_viva as CV
import plan_soc as P
import textos_soc

OUT = os.path.join(AQUI, "..", "entregables", "guias_sociales")
ESCONDER = "[hidden]{display:none!important}\n"

# ─────────────────────────────── títulos de cada clase ───────────────────────────────
TITULOS = {
    1: "Quién dice qué, y desde qué principio",
    2: "Coincidir en qué, diferir en por qué",
    3: "Toda decisión tiene su cuenta",
    4: "Un hecho, muchas miradas",
    5: "El lugar también es causa",
    6: "Lo que hace legítimo a un poder",
}
LEADS = {
    1: "Hoy no vamos a opinar sobre las noticias. Vamos a leerlas con tres preguntas: quién dice "
       "qué y por qué, qué principio de la Constitución hay detrás y qué pasa después.",
    2: "Dos personas pueden querer lo mismo por razones distintas, y querer cosas distintas por la "
       "misma razón. Hoy no basta con saber quién dijo qué: hay que saber en qué coinciden y en qué no.",
    3: "Una decisión pública tiene voces, deja ganadores y perdedores, toca un derecho y produce "
       "efectos que llegan lejos de donde se tomó. Hoy le hacemos esas cuatro preguntas al mismo caso.",
    4: "El pasado no tiene una sola versión. Hoy miramos cada hecho desde donde lo vivió cada quien: "
       "qué le hizo a la gente, qué venía de antes y hasta dónde llegó.",
    5: "La orilla, la ladera, la frontera o la selva no son el fondo del problema: son parte de su "
       "causa. Hoy leemos el territorio como un actor más.",
    6: "La última clase de contenido del área. Hoy todo se junta: un poder no se vuelve legítimo "
       "solo por tener la mayoría, ni solo por dar resultados.",
}

# ─────────────── la redacción de pantalla y de la guía, para Sociales ───────────────
# Reemplaza las claves de clase_viva.TEXTOS_UI marcadas «propio de LC». Las que dependen de la
# misión se completan en ui(mis).
COMPETENCIAS = [("PS · pensamiento social", "conceptos, derechos y principios", "var(--m2)"),
                ("IP · interpretación y análisis de perspectivas", "quién dice qué y desde dónde",
                 "var(--m4)"),
                ("PRS · pensamiento reflexivo y sistémico", "dimensiones, efectos y contextos",
                 "var(--m6)")]

UI = dict(
    portada_decir=["«Libro abierto, cuaderno cerrado, lápiz. Hoy no les voy a preguntar qué "
                   "opinan: les voy a preguntar qué dice el caso.»"],
    regla_lead="Si el instrumento está vacío, no analizaste: opinaste.",
    regla_p=("Primero se escribe el instrumento —quién dice qué, qué principio, qué efecto—, después "
             "se marca la opción. Una respuesta correcta con el instrumento en blanco no cuenta como "
             "resuelta."),
    regla_decir=["«La respuesta correcta con el instrumento vacío no cuenta. ¿Por qué? Porque en "
                 "Sociales casi todas las opciones suenan justas: el que no escribió quién dice qué "
                 "escoge la que más le gusta, no la que dice el caso.»"],
    regla_apoyo=["Si alguien pregunta para qué escribir, la respuesta corta es: lo que separa la "
                 "opción correcta de las que suenan bien está en el caso, y el caso se olvida si no "
                 "se escribe.",
                 "Si alguien dice «eso está mal», devuélvele la pregunta: «¿mal para quién?». En "
                 "Sociales no se califica la opinión: se califica si sale del caso."],
    act_h2="¿Quién gana, quién pierde y quién decide?",
    act_lead="Tres nombres antes de cualquier opinión. Todavía no se abre el cuaderno.",
    act_apoyo=("No des tu opinión sobre el caso ni dejes que la clase arranque opinando. Si alguien "
               "dice «eso está mal», pregúntale «¿mal para quién?». El caso es inventado para la "
               "clase: no sale del libro ni de una noticia, y no tiene nombres propios."),
    dina_decir=["«Esto no es recreo: es la misma operación que van a hacer con el caso en cinco "
                "minutos —poner a cada actor, efecto o derecho en su lugar—, pero con el cuerpo.»"],
    prob_lead="Antes de releer el caso: ¿cuál creen que es? Levanten la mano.",
    prob_lead2=P.PREGUNTA_AREA,
    bloque_h2="Preguntas {a} y {b}: primero el instrumento, después la opción",
    bloque_decir=["«Antes de marcar: ¿quién dice qué en el caso? Léanme lo que escribieron en el "
                  "instrumento.»",
                  "Si alguien se traba, pregúntale a quién le pasa algo en el caso. Si el instrumento "
                  "está vacío, vuelve al caso antes que a las opciones."],
    bloque_apoyo=("Las claves del libro son {a}·{ka} y {b}·{kb}. No las reveles hasta que todos "
                  "tengan el instrumento escrito: el botón es para el cierre del bloque."),
    reto_defensa=("<b>La defensa:</b> tres minutos por equipo, señalando en el caso el actor, el "
                  "derecho o el renglón que los respalda. «Es que así es» no cuenta."),
    reto_apoyo=["El reto no tiene una sola respuesta correcta: gana el equipo que mejor sostiene la "
                "suya con el caso. Si dos análisis están sostenidos, dilo: eso también es pensar "
                "socialmente.",
                "Si un equipo entrega una sola hoja para los tres, el reto no cuenta. La discusión es "
                "compartida; el registro es individual.",
                "Cierra mostrando qué actor o qué dimensión quedó por fuera en cada propuesta."],
    icfes_decir=["Durante la evaluación no se proyecta nada: las preguntas están en el cuaderno. Esta "
                 "diapositiva es para el cierre, cuando se socializan las falladas.",
                 "«¿Qué escribiste en el instrumento antes de mirar las opciones? ¿Quién dice qué, y "
                 "desde dónde?»"],
    # clase 7
    c7_h1="Hoy nadie les va a decir si acertaron",
    c7_lead=("Veinticuatro preguntas, seguidas, como en la prueba. Lo único que llevan es lo que "
             "entrenaron: escribir quién, qué principio o qué efecto antes de mirar las opciones."),
    c7_decir=["«Pueden escribir en el cuaderno y al margen: en la prueba real también pueden rayar "
              "el cuadernillo, y es lo que entrenamos.»"],
    c7_reglas=["En silencio y en filas individuales.", "No se responde ninguna duda, ni de vocabulario.",
               "Las dudas se escriben en el margen.",
               "Primero el instrumento —actores, principio o efecto—, después la opción."],
    c7_apoyo_reglas=["Anota quién va directo a las opciones sin escribir nada en el instrumento: es "
                     "el dato más útil del simulacro, más que el puntaje."],
    c7_competencias=COMPETENCIAS,
    # clase 8
    c8_h1="Lo que escribiste esta vez",
    c8_lead=("Hoy no hay caso nuevo. Hoy vamos a poner tu instrumento de hace seis semanas al lado "
             "del de hoy."),
    c8_apoyo_elegir=["Si dudas entre dos, quédate con la de la competencia que más manos tuvo en el "
                     "conteo de la clase 7."],
    c8_h2="¿Qué actor, qué principio o qué efecto viste esta vez que antes no?",
    c8_decir=["«Pongan las dos hojas una al lado de la otra. ¿Qué escribieron distinto en el "
              "instrumento?»"],
    c8_apoyo=["Si nadie escribió distinto, la estrategia no se instaló todavía: anótalo en el "
              "registro para el reporte de los especialistas."],
)

# ───────────── los avisos del libro: cuáles salen en pantalla (al revelar) ─────────────
# Clave: (misión, rótulo del aviso en plan_soc.AVISOS). Valor: (rótulo que usa el motor,
# severidad en pantalla, texto para el estudiante), o una lista de esas si el aviso habla de dos
# preguntas que caen en bloques distintos. Lo que no está aquí va solo a la guía del
# profe: los avisos de nombres de la política, de marcas, de fuentes y de reparto de claves
# («no lo digas en clase») no se proyectan.
PROYECTAR = {
    (1, "preg. 4"): ("preg. 4", "atención",
        "El enunciado ya nombra el concepto —discriminación positiva o acción afirmativa—: lo que "
        "pregunta es para qué sirve, no cómo se llama."),
    (2, "preg. 6"): ("preg. 6", "media",
        "La opción D dice que la Conmoción Interior permite suspender los derechos humanos. Es "
        "falso: la Constitución permite limitar algunos, nunca suspenderlos (art. 214). Compruébalo "
        "en tu página 99."),
    (2, "preg. 7"): ("preg. 7", "atención",
        "La ley colombiana reconoce a los animales como seres sintientes (Ley 1774 de 2016), no "
        "como titulares de derechos. Si lo objetaste, tienes razón; la clave no cambia."),
    (3, "preg. 9"): ("preg. 9", "media",
        "La opción B define la legalidad como el derecho de cada país a difundir sus opiniones: "
        "eso es falso. Legalidad es actuar dentro de lo que la ley permite."),
    (3, "preg. 1"): ("preg. 1", "atención",
        "La clave A dice que el homenaje fortaleció la memoria y la legitimidad institucional; el "
        "texto no lo dice. Es la mejor de las cuatro, no una perfecta: si dudaste de esa mitad con "
        "el texto en la mano, leíste bien."),
    (4, "texto 4 a 7"): ("preg. 4", "media",
        "El texto dice que la violencia afectó «de manera especial a mujeres», pero la figura "
        "muestra 52,87 % hombres y 46,31 % mujeres. Comparar el texto con la figura es contrastar "
        "fuentes."),
    (4, "preg. 7"): ("preg. 7", "atención",
        "El texto solo dice que el desplazamiento «coincidió» con el banano y las rutas. La B se "
        "elige por descarte: coincidir no es causar."),
    (4, "preg. 10"): ("preg. 10", "atención",
        "El Plan Colombia empezó en 1999-2000. Después del 11 de septiembre de 2001 se fortaleció, "
        "pero no nació del 11-S."),
    (5, "preg. 2"): ("preg. 2", "media",
        "El texto da como hecho un cierre de la frontera con Venezuela en 2024 con sanciones "
        "comerciales, y no se encontró sustento: la frontera se reabrió en 2022. Para responder "
        "basta el texto: léelo como un caso."),
    (5, "preg. 6"): ("preg. 6", "media",
        "La clave A dice que el Parque Nacional «afecta la movilidad»: la afectaría el asentamiento, "
        "y el texto no habla de movilidad. Es la menos mala de las cuatro."),
    (6, "preg. 6"): ("preg. 6", "media",
        "Se pueden defender la B (división de poderes) y la C (pluralismo). La clave es B porque el "
        "texto habla de «contrapesos institucionales»."),
    (6, "preg. 1 y 10"): [
        ("preg. 1", "media",
         "La clave no concuerda del todo con la definición del texto: es la mejor de las cuatro. Si "
         "dudaste de ella con el texto en la mano, leíste bien."),
        ("preg. 10", "media",
         "La D gana porque nombra las tres dimensiones, aunque la B sigue más de cerca el texto. "
         "Nombrar lo político, lo social y lo ético no basta: cada parte tiene que estar en el texto.")],
}

# Casos del libro con nombres de la política (o que los señalan sin nombrarlos): en pantalla se
# nombran sin ellos y se remite al libro, donde el estudiante ya los lee.
CTX_NEUTRO = {
    (1, 1): "Una propuesta de Constituyente (2024) frente a la Constitución de 1991",
    (1, 5): "Una declaración de 1997 sobre los U'wa · qué entiende por progreso",
    (3, 1): "Un homenaje en la Plaza de Bolívar (2025) · lo social, lo político y lo económico",
    (3, 2): "Un homenaje en la Plaza de Bolívar (2025) · dos perspectivas",
    (6, 8): "Una investigación judicial en curso (2023) · las voces del debate",
    (6, 9): "Un fallo de primera instancia (2025) · el Estado de Derecho",
    (6, 10): "Un fallo de primera instancia (2025) · política, sociedad y ética",
}

FRANJA = ("El concepto del día —un derecho, un mecanismo o un principio—, en «Palabras que me "
          "frenaron», con tus palabras.")

# Nombres que no pueden salir en el HTML. Si aparece uno, la construcción se detiene.
PROHIBIDOS = ["Petro", "Uribe", "Plazas Vega", "Gustavo", "Álvaro", "Duque", "Santos", "Benedetti",
              "Turbay", "Pastrana", "Gaviria", "Samper", "Cepeda", "Vargas Lleras", "Fajardo",
              "Claudia López", "Nicolás"]

# Correcciones de redacción que se aplican a lo que viene de TEXTOS_GUIA_DOCENTE.md (sin tocar el
# .md: quedan en el informe). Pares (antes, después).
CORRIGE = [
    # el «no suspender» está en el art. 214, numeral 2 (el 213 define la Conmoción Interior)
    ("El artículo 213 dice limitar, más no suspender.",
     "El artículo 214 dice limitar, mas no suspender."),
    # nombre propio del oficial: la guía no lo repite (decisión pendiente de la Gerencia)
    ("El coronel Luis Alfonso Plazas Vega comandó la operación. Fue condenado y después absuelto.",
     "El oficial que comandó la retoma fue condenado y después absuelto (el libro lo nombra; la "
     "guía no lo repite)."),
    # meta-texto del .md que no se proyecta
    (" (el cuaderno lo imprime así)", ""),
]


def corrige(t):
    for a, b_ in CORRIGE:
        t = t.replace(a, b_)
    return t


def _tabla(m):
    """«| A | B | |---|---| | x | y |» (una tabla del .md aplanada) → «x: y.» por fila."""
    celdas = [c.strip() for c in m.group(0).split("|")]
    ncol = sum(1 for c in celdas if re.fullmatch(r"-{3,}", c))
    celdas = [c for c in celdas if c and not re.fullmatch(r"-{3,}", c)]
    filas = [celdas[i:i + ncol] for i in range(ncol, len(celdas), ncol)]
    return " ".join(f"{f[0]}: {f[1]}" + (f" ({', '.join(f[2:])})" if len(f) > 2 else "") + "."
                    for f in filas if len(f) == ncol)


def limpia_nota(t):
    """Las notas del .md llegan con viñetas y tablas aplanadas en una línea: se vuelven prosa."""
    t = corrige(t)
    t = re.sub(r"\|[^\n]*\|-{3,}\|[^\n]*\|", _tabla, t)
    t = re.sub(r"(?<=[.:])\s+-\s+", " ", t)
    t = re.sub(r"(^|\s)>\s+", " ", t).strip()          # citas «>» del .md
    return re.sub(r"\s*-{3,}\s*$", "", t)                 # separador «---» del .md


# ─────────────────────────────── datos ───────────────────────────────
def paginas(mis):
    """Páginas del cuaderno: taller [p1-2, p3-4, p5-6, p7-8, p9-10] e ICFES [P1-2, P3-4]."""
    b = P.BASE[mis]
    return [b, b + 1, b + 3, b + 4, b + 5], [b + 2, b + 6]


def clasifica_avisos():
    """Reparte plan_soc.AVISOS en: los que se proyectan (motor), los que van a la guía en su
    pregunta del taller, los de una pregunta ICFES y los generales de la misión (portada)."""
    proy, taller, icfes, general = {}, {}, {}, {}
    for mis, lista in P.AVISOS.items():
        proy[mis] = []
        for preg, sev, que, hacer in lista:
            if (mis, preg) in PROYECTAR:
                v = PROYECTAR[(mis, preg)]
                for rot, sev2, txt in (v if isinstance(v, list) else [v]):
                    proy[mis].append((rot, sev2, txt, hacer))
                continue
            nums = [int(x) for x in re.findall(r"\d+", preg)]
            if " a " in preg and len(nums) == 2:
                nums = list(range(nums[0], nums[1] + 1))
            if preg.startswith("ICFES") and nums:
                for k in nums:
                    icfes.setdefault((mis, k), []).append(
                        f"Aviso del libro ({sev}), solo para ti: {que} Qué haces: {hacer}")
            elif preg.startswith(("preg", "texto")) and nums:
                for n in nums:
                    taller.setdefault((mis, n), []).append(dict(
                        titulo=f"aviso del libro ({sev}), solo para ti, no se proyecta",
                        texto=f"{que} Qué haces: {hacer}"))
            else:
                general.setdefault(mis, []).append(f"{que} {hacer}")
    return proy, taller, icfes, general


def notas_taller(textos_taller, avisos_taller):
    """Notas del taller por pregunta, sin repetir la misma nota en las dos preguntas de un bloque
    (las de «preguntas 4, 5 y 6» saldrían dos veces en el bloque 5-6)."""
    junto = {}
    for d in (textos_taller, avisos_taller):
        for k, v in d.items():
            junto.setdefault(k, []).extend(v)
    out = {}
    for (mis, n), notas in sorted(junto.items()):
        par = n - 1 if n % 2 == 0 else n + 1
        ya = {x["titulo"] + x["texto"] for x in out.get((mis, par), [])}
        limpias = [dict(titulo=corrige(x["titulo"]), texto=limpia_nota(x["texto"])) for x in notas]
        out[(mis, n)] = [x for x in limpias if x["titulo"] + x["texto"] not in ya]
    return out


# Textos ICFES que son verso y el .md no marca con «**Formato:** verso»: la estrofa entre « »
# se parte en renglones donde empieza cada verso (mayúscula después de minúscula o puntuación).
VERSO = {(4, 2)}


def a_verso(texto):
    def parte(m):
        return re.sub(r"(?<=[a-záéíóúñ.,])\s+(?=[A-ZÁÉÍÓÚ])", "\n", m.group(0))
    t = re.sub(r"«[^»]+»", parte, texto)
    return re.sub(r":\s+«", ":\n\n«", t)


def textos_icfes(icfes, avisos_icfes):
    out = {}
    for (mis, k), v in icfes.items():
        v = copy.deepcopy(v)
        v["texto"] = corrige(v["texto"])
        if (mis, k) in VERSO and not v.get("verso"):
            v["texto"], v["verso"] = a_verso(v["texto"]), True
        v["notas"] = [limpia_nota(n) for n in v["notas"]] + avisos_icfes.get((mis, k), [])
        if "ASED" in v.get("fuente", ""):
            v["notas"].insert(0, "⚑ Pendiente: confirmar fuente (ASED). Esta pregunta sale del "
                                 "compilado ASED, que dice haber concebido sus preguntas: no es de "
                                 "un cuadernillo del ICFES. Nelson decide si se reemplaza; mientras "
                                 "tanto, no la presentes como «del ICFES».")
        out[(mis, k)] = v
    return out


def verificar_claves(icfes):
    """Las claves que se proyectan tienen que ser las verificadas. Falla si no coinciden."""
    malas = textos_soc.verificar(icfes)
    for mis in range(3, 7):
        doc = CV.claves_docstring(f"soc{mis}", AQUI + "/")
        if doc != P.CLAVES[mis]:
            malas.append(f"M{mis}: plan_soc.CLAVES {P.CLAVES[mis]} · soc{mis}.py {doc}")
    for mis in range(1, 7):
        for k in range(1, 5):
            if P.BANCO[mis][k - 1]["clave"].strip() != icfes[(mis, k)]["clave"]:
                malas.append(f"M{mis} P{k}: BANCO {P.BANCO[mis][k-1]['clave']} · .md "
                             f"{icfes[(mis, k)]['clave']}")
    if malas:
        raise SystemExit("Las claves no coinciden:\n  " + "\n  ".join(malas))


# ─────────────────────────────── el Area de cada misión ───────────────────────────────
def planeador(avisos_proy):
    """plan_soc con los avisos que se proyectan y el contexto de los casos sin nombres."""
    ns = types.SimpleNamespace(**{k: getattr(P, k) for k in dir(P) if k.isupper()})
    ns.AVISOS = avisos_proy
    ns.TALLER = {mis: [(p, e, i, CTX_NEUTRO.get((mis, p), c)) for p, e, i, c in filas]
                 for mis, filas in P.TALLER.items()}
    return ns


def colores_estrategia(mis):
    return list(P.COLS_MIS[mis])


def ui(mis):
    l0, l1 = P.LIBRO[mis]
    u = dict(UI)
    u["portada_libro"] = f"Las diez preguntas de la prueba de campo, páginas {l0} a {l1}"
    u["prob_sub"] = ("Nadie justifica con «yo pienso que» ni con lo que vio en las noticias: toda "
                     "respuesta nombra un actor del caso o un derecho, un artículo o un principio.")
    t_pags, _ = paginas(mis)
    apoyo = [f"La pregunta modelo es la 1 del libro (página {P.PAG_LIBRO[mis][0]}). El cuaderno se "
             f"abre en la página {t_pags[0]} solo en «mi primera idea».",
             "Cuenta las manos tocando cada letra: el número queda en pantalla y sirve para el final "
             "del momento, cuando el grupo vea cuántos cambiaron de opinión al volver al caso.",
             "No digas la clave en este momento: sale en el bloque de las preguntas 1 y 2, después de "
             "llenar el instrumento en pantalla, casilla por casilla. Ahí se trabaja por qué cae cada "
             "una de las otras tres."]
    if mis in (1, 3):
        apoyo.append("El caso de la pregunta 1 está en la conversación pendiente con la Gerencia "
                     "sobre la política viva. Se lee el argumento, no al personaje: si el salón se va "
                     "a opinar, devuélvelo al caso. En pantalla no sale ningún nombre: está en el libro.")
    u["prob_apoyo"] = apoyo
    return u


def area(mis, P_ns, textos, taller):
    return CV.Area(
        nombre="Sociales y Ciudadanas", prefijo="SOC", fuerte="Si Sociales no es tu fuerte",
        color=CV.color_de("Sociales y Ciudadanas"), P=P_ns,
        claves_libro=lambda m: P.CLAVES[m],
        preguntas_icfes=CV.preguntas_de_textos(textos),
        textos=textos, advertencias={}, taller=taller, saberes=P.SABERES,
        activacion=P.ACTIVACION, titulos=TITULOS, leads=LEADS,
        est_col=colores_estrategia(mis),
        colores=dict(m2="#1F4E8C", m3="#3B3BA6", m4=P.MORADO, m5=P.ROJO, m6=P.VERDE),
        textos_ui=ui(mis), apoyo_fuerte="Sociales no es tu área", out=OUT)


# ─────────────────────────── lo que se agrega a las escenas ───────────────────────────
def apoyo_portada(mis, general):
    """Guía del profe de la portada: antes del sábado y «Si Sociales no es tu fuerte»."""
    d = P.MISIONES[mis]
    out = ["⚑ Antes del sábado: " + P.limpia(d["ojo"])]
    for g in general.get(mis, []):
        out.append("Del libro, para ti: " + g)
    if mis == 1:
        out.append("Si el curso se desvía al debate político, la frase que lo devuelve es: «esa es tu "
                   "opinión y vale, pero no entra en esta pregunta».")
    out.append("Los cuatro conceptos que tienes que poder explicar hoy en dos minutos, sin jerga. Si "
               "un estudiante sabe más que tú de un tema, déjalo explicar y pide que señale en el caso "
               "de dónde lo saca:")
    out += [f"{t}: {x}" for t, x in P.NO_ES_TU_FUERTE[mis]]
    return out


def conteo_competencias():
    """Qué preguntas del simulacro son de cada competencia (clasificación del planeador)."""
    por = {"PS": [], "IP": [], "PRS": []}
    for mis in range(1, 7):
        for k in range(1, 5):
            por[P.comp_icfes(mis, k)].append(f"M{mis}·P{k}")
    return por


def escenas_contenido(A, mis, general):
    sc = CV.escenas_clase(A, mis)
    sc[0]["guia"]["apoyo"] = apoyo_portada(mis, general) + sc[0]["guia"]["apoyo"]
    l0 = P.PAG_LIBRO[mis][0]
    h = sc[4]["html"].replace(f"Abran el libro en la pregunta modelo del momento {mis}",
                              f"Abran el libro en la pregunta 1, página {l0}")
    # la pregunta problematizadora de este momento, en su propia tarjeta (plan_soc.PROBLEMATIZADORA)
    sc[4]["html"] = h + (f'<div class="card big edge mt" style="--accent:var(--m2)"><h3>La pregunta '
                         f'de este momento</h3><p class="lead">{CV.E(P.PROBLEMATIZADORA[mis])}</p></div>')
    # cierre: la franja del cuaderno se llama «Palabras que me frenaron» y en Sociales lo que se
    # escribe es el concepto del día (planeador, momento 6)
    viejo = "La palabra nueva del día, en la franja de vocabulario, con tus palabras."
    assert viejo in sc[-1]["html"]
    sc[-1]["html"] = sc[-1]["html"].replace(viejo, FRANJA)
    return sc


def rotulo(contexto, n=46):
    """Rótulo de la clase 8: el motor corta en 46 caracteres; aquí se corta por « · » o por
    palabra, para que ningún botón quede con media palabra."""
    partes = contexto.split(" · ")
    t = partes[0]
    if len(partes) > 1 and len(t) + 3 + len(partes[1]) <= n:
        t += " · " + partes[1]
    if len(t) > n:
        t = t[:n - 1].rsplit(" ", 1)[0].rstrip(" ,(") + "…"
    return t


def escenas_simulacro(A):
    sc7 = CV.escenas_clase7(A)
    sc7[0]["guia"]["apoyo"].append(
        "Ocho de las 24 (las de las misiones 1 y 2) salen del compilado ASED. ⚑ Pendiente: confirmar "
        "fuente (ASED). Nelson decide si se reemplazan antes de imprimir.")
    por = conteo_competencias()
    sc7[2]["guia"]["apoyo"] = [
        "La competencia de cada pregunta es la de la estrategia que entrena, según el planeador: es "
        "la clasificación de EDUCATE, no la oficial del ICFES.",
        *[f"{n} ({len(por[n.split(' · ')[0]])} preguntas): {', '.join(por[n.split(' · ')[0]])}."
          for n, _, _ in COMPETENCIAS],
        "Como no hay el mismo número de preguntas en cada competencia, compara proporciones, no "
        "manos sueltas.",
        "Anota los tres números: son el dato que la coordinación necesita para decidir el refuerzo."]
    todas = [(m, k, rotulo(fila["contexto"])) for m in range(1, 7) for k, fila in enumerate(P.BANCO[m], 1)]
    sc8 = CV.escenas_clase8(A, todas)
    sc8[-1]["guia"]["apoyo"] = [a.replace("la franja de vocabulario completa",
                                          "la franja «Palabras que me frenaron» completa")
                                for a in sc8[-1]["guia"]["apoyo"]]
    return sc7, sc8


# ─────────────────────────────── escribir ───────────────────────────────
def revisar_nombres(html, archivo):
    hay = [n for n in PROHIBIDOS if re.search(r"\b" + re.escape(n) + r"\b", html)]
    if hay:
        raise SystemExit(f"{archivo}: trae nombres que no pueden salir: {hay}")


def escribir(A, archivo, titulo, sub, sc):
    html = CV.pagina(A, titulo, sub, sc, titulo).replace("</style>", ESCONDER + "</style>", 1)
    revisar_nombres(html, archivo)
    f = os.path.join(A.out, archivo)
    with open(f, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"{archivo:34s} {len(sc):2d} diapositivas · {os.path.getsize(f)//1024} KB")
    return f, len(sc)


def construir(out=OUT):
    global OUT
    OUT = out
    os.makedirs(out, exist_ok=True)
    icfes, _, taller_md = textos_soc.leer()
    verificar_claves(icfes)
    proy, av_taller, av_icfes, general = clasifica_avisos()
    textos = textos_icfes(icfes, av_icfes)
    taller = notas_taller(taller_md, av_taller)
    P_ns = planeador(proy)
    hechos = []
    for mis in range(1, 7):
        A = area(mis, P_ns, textos, taller)
        A.out = out
        d = P.MISIONES[mis]
        sc = escenas_contenido(A, mis, general)
        hechos.append(escribir(A, f"SOC_Clase{mis}_Mision{mis}.html",
                               f"Sociales y Ciudadanas · Clase {mis}",
                               f"Momento {mis} · {d['comp']} · páginas {d['pags']}", sc))
    A = area(1, P_ns, textos, taller)
    A.out = out
    sc7, sc8 = escenas_simulacro(A)
    hechos.append(escribir(A, "SOC_Clase7_Simulacro.html", "Sociales y Ciudadanas · Clase 7",
                           "Simulacro del área · 24 preguntas", sc7))
    hechos.append(escribir(A, "SOC_Clase8_Devolucion.html", "Sociales y Ciudadanas · Clase 8",
                           "Devolución y cierre del área", sc8))
    return hechos


if __name__ == "__main__":
    construir(sys.argv[1] if len(sys.argv) > 1 else OUT)
