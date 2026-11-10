#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLANEADOR DEL DOCENTE · INGLÉS · las ocho clases del área.

    python3 plan_ing.py --pdf      → entregables/EDUCATE_Planeador_Ingles.pdf (24 hojas)

Mismo modelo aprobado en el piloto de Matemáticas y ya entregado en Lectura Crítica, Sociales y
Biología (plan_bio.py, del que sale este archivo): seis momentos de 15·20·35·20·20·10, «tu aporte»
acotado en cada uno y un banco de dinámicas isomorfas a las subestrategias. Usa el motor
plan_piezas.py sin cambiarlo.

LO PROPIO DE INGLÉS. El cuaderno trabaja TODAS las preguntas del libro (decisión de Nelson, 7 nov):
127 tarjetas (M1 21 · M2 10 · M3 40 · M4 16 · M5 16 · M6 24). Cada misión es una parte del examen y su
estrategia va en el `tema=` del módulo; las tarjetas dicen «Subestrategia n». Con el reparto fijo de
la clase no caben 40 preguntas en 35 minutos, así que cada misión tiene un REPARTO (decisión de este
planeador, explicada en la hoja 1 y en la de cada clase):

  · CLASE: diez tarjetas representativas, en cinco bloques de dos, con las cuatro subestrategias y
    con las tarjetas que tienen sello «Alto · aquí entra el profe» (esas no pueden ir a la casa).
  · RETO: el reto del corte se hace con tarjetas del libro cuando quedan muchas (M1, M3, M4, M5, M6):
    un texto o un grupo completo en relevo por equipos; cada uno deja TODAS esas tarjetas llenas en su
    propio cuaderno (el cuaderno es el registro individual). La Misión 2 cabe entera en clase y su reto
    es original.
  · CASA: lo que queda, como tarea de la misión, y se revisa con una RONDA DE CLAVES de cinco minutos al
    comenzar la clase siguiente (dentro de los 15 de la activación). La tarea de la Misión 3 (22
    tarjetas) se reparte en tres entregas, un texto por semana, aprovechando que las misiones 4 y 5
    no dejan tarea.

Para las guías (clase_viva_ing.py), con los nombres del contrato de clase_viva.py:
    FASES  CLASES  MISIONES  TALLER (las 10 de clase)  TALLER_TODO  DINAMICAS  RETOS  AVISOS  SELLOS
    SABERES  ACTIVACION  PROBLEMATIZADORA  PREGUNTA_AREA  NO_ES_TU_FUERTE  PRONUNCIA  COLS_MIS  CLAVES
    REPARTO  BANCO  GRUPO_ICFES  pag_tarjeta()

Claves del libro: copiadas del docstring de ing1.py … ing6.py (resueltas a mano el 7 nov), vueltas a
resolver contra el libro el 10 nov y comprobadas al construir con `verificar()`. Las del entrenamiento:
TEXTOS_ING.md, cruzadas con el docstring de ingN_icfes.py y con tablero/icfes.csv (textos_ing.verificar).

Membrete (Nelson, 10 nov): «Pregunta Saber 11», sin año ni «oficial». Las páginas del cuaderno salen
de tablero/manifiesto_hojas.json: si el mapa de páginas cambia, el planeador lo sigue.
"""
import ast, csv, json, re
from plan_piezas import *
import plan_piezas as PZ
import paginas as PG          # la numeración final del cuaderno (398 páginas, 10 nov): única fuente

ING = "#1BA0A8"; ING_BG = "#E8F6F7"; ING_LN = "#B4DEE1"
ING_T = "#12808A"          # el turquesa, oscurecido, para texto pequeño sobre blanco
TOTAL = 24
configurar(ING, ING_BG, ING_LN, "Inglés", TOTAL)
AREA_CSV = "Inglés"

AZUL = "#242478"; ROJO_E = "#A82424"; ORO_E = "#C9821B"
PIZARRA = "#4A5A70"        # el cierre no va en turquesa: es el color del área (y de la activación)
CORR = "#242478"; CORR_BG = "#F2F3FA"; CORR_LN = "#C9CBE6"     # «Corrección EDUCATE» del cuaderno
SEV_ING = dict(SEV, **{"corrección": (CORR, CORR_BG, CORR_LN)})

# Los colores de las cuatro subestrategias, tal como salen en los chips del cuaderno (EST de ingN.py).
COLS_MIS = {1: [AZUL, ROJO_E, MORADO, ORO_E], 2: [AZUL, ROJO_E, MORADO, ORO_E],
            3: [AZUL, ROJO_E, ORO_E, MORADO], 4: [AZUL, ROJO_E, ORO_E, MORADO],
            5: [AZUL, ROJO_E, ORO_E, MORADO], 6: [AZUL, ROJO_E, ORO_E, MORADO]}

# ─────────────────────────── los seis momentos ───────────────────────────
# El reparto es el aprobado: 15 · 20 · 35 · 20 · 20 · 10 = 120. No se cambia.
FASES = [
    ("Activación", 15, ING,
     "Que el estudiante, antes de abrir el libro, busque en una frase corta en inglés la pista que "
     "decide —una palabra, un tiempo, una intención— y la nombre en voz alta.",
     ["Si hay tarea de la misión anterior, abre con la ronda de claves: cinco minutos, reloj a la vista.",
      "Proyecta la frase del día, inventada para la clase, y la lee despacio dos veces.",
      "Pide que el grupo señale la palabra que decide y diga qué decide: quién habla, cuándo pasa, qué falta.",
      "Ejecuta la dinámica de la subestrategia 1 (ocho minutos)."],
     "No traduce la frase ni explica gramática. Si alguien pregunta qué significa una palabra, le "
     "devuelve: «¿qué palabra de al lado te ayuda?». El cuaderno sigue cerrado, salvo en la ronda de claves.",
     "Frase proyectada. Cuaderno abierto solo en la ronda de claves."),
    ("Pregunta problematizadora", 20, "#1F4E8C",
     "Que el estudiante compruebe que en Inglés la respuesta sale de una pista del texto —la palabra "
     "vecina, el verbo, el marcador de tiempo, quién habla— y no de lo que suena bonito ni de traducir "
     "palabra por palabra.",
     ["Presenta la pregunta modelo (la primera de las diez de clase) y la deja a la vista todo el momento.",
      "Pide respuestas a mano alzada ANTES de buscar la pista, y las cuenta en pantalla.",
      "Hace la pregunta que gobierna el área: ¿qué palabra del texto te lo dice?",
      "Al final del momento llena con el grupo el instrumento de esa tarjeta y trabaja por qué cae cada opción."],
     "Regla del momento: nadie justifica con «me suena» ni con «en español se dice así». Toda "
     "intervención señala la palabra del texto que decide.",
     "Libro abierto en la parte del día. Cuaderno en la primera tarjeta de clase."),
    ("Desarrollo guiado", 35, "#3B3BA6",
     "Que el estudiante llene el instrumento de cada tarjeta —la pista, lo que tacha, el tiempo, la "
     "intención— antes de marcar la letra, en las diez tarjetas de clase de la misión.",
     ["Trabaja por bloques las diez tarjetas de clase (la hoja de la clase dice cuáles): unos cinco minutos por bloque.",
      "Antes de que marquen, verifica que el instrumento tenga escrita la pista.",
      "Entre bloques, la dinámica de la subestrategia que viene: tres minutos, no más.",
      "Cuando aparece una «Corrección EDUCATE» o un sello «Alto · aquí entra el profe», lo lee en voz alta "
      "y explica en dos minutos."],
     "No traduce el texto ni dicta la respuesta. Si un estudiante se traba, le pregunta qué palabra "
     "vecina mira; si el instrumento está vacío, lo devuelve al texto antes que a las opciones. Las "
     "tarjetas del reto y de la casa no se tocan en este momento.",
     "Cuaderno en las tarjetas de clase. Libro abierto en la parte del día."),
    ("Reto en equipo", 20, MORADO,
     "Que el estudiante defienda su respuesta con la pista en la mano y acepte que otro equipo puede "
     "ver una pista que él no vio.",
     ["Arma equipos de tres y anuncia el reto del corte de la misión.",
      "Cada integrante trabaja primero su parte, en SU cuaderno.",
      "Da tres minutos de defensa por equipo: leen en voz alta la palabra que decide.",
      "Cierra con las claves del reto (en la guía, con «Revelar»)."],
     "El equipo discute, pero cada uno escribe en su propio cuaderno. No se acepta «es que suena "
     "mejor»: se nombra la pista. Si el libro tiene una «Corrección EDUCATE» en el reto, se discute ahí.",
     "Cuaderno de cada uno, en las tarjetas del reto."),
    ("Evaluación individual", 20, ROJO,
     "Que el estudiante transfiera por sí solo la subestrategia a preguntas tipo Saber 11, con textos "
     "que no trabajó en clase.",
     ["Entrega las dos hojas de entrenamiento de la misión.",
      "Da el tiempo completo sin intervenir ni traducir.",
      "Registra quién llena el instrumento y quién va directo a las opciones."],
     "Este momento es silencioso y en filas individuales. Es el que produce el dato de seguimiento. Si "
     "un estudiante marca sin llenar el instrumento, se le anota, no se le corrige.",
     "Cuaderno, las dos hojas de entrenamiento. Reloj a la vista."),
    ("Cierre", 10, PIZARRA,
     "Que el estudiante nombre la subestrategia que usó, sepa qué tarjetas quedan para la casa y se "
     "lleve una palabra o una expresión nueva, escrita en sus palabras.",
     ["Socializa solo las preguntas que el grupo falló, pidiendo la pista que las resuelve.",
      "Dice en voz alta la tarea de la misión y cuándo se revisa (está en la última diapositiva).",
      "Cada uno escribe la palabra del día en la franja de vocabulario y marca su carita de salida."],
     "No dicta traducciones. La palabra se escribe como el estudiante la entendió; si quedó mal "
     "entendida, eso se ve en la hoja y se corrige la próxima clase.",
     "Cuaderno: franja de vocabulario, «lo que me llevo», carita de salida y portada del área."),
]

CLASES = [
    (1, "Misión 1 · Partes 1 y 2", "léxico y avisos · 21 preguntas"),
    (2, "Misión 2 · Parte 3", "conversaciones · 10 preguntas"),
    (3, "Misión 3 · Parte 4", "texto con espacios · 40 preguntas"),
    (4, "Misión 4 · Parte 5", "lectura literal · 16 preguntas"),
    (5, "Misión 5 · Parte 6", "lectura inferencial · 16 preguntas"),
    (6, "Misión 6 · Parte 7", "texto con espacios · 24 preguntas"),
    (None, "Simulacro del área", "la prueba que escoge EDUCATE"),
    (None, "Socialización del simulacro", "en las hojas de simulacro del cuaderno"),
]
AREA_PAGS = PG.rango_area("ing")                      # (313, 395): portada, seis misiones y simulacro
SIMULACRO_PAGS = PG.paginas_simulacro("ing")          # [390 … 395]
SIM = f"{SIMULACRO_PAGS[0]} a {SIMULACRO_PAGS[-1]}"

TOTAL_PREG = {1: 21, 2: 10, 3: 40, 4: 16, 5: 16, 6: 24}
LIBRO = {1: (414, 415), 2: (424, 425), 3: (435, 437), 4: (446, 448), 5: (456, 459), 6: (468, 470)}


def pag_libro(mis, n):
    """«La lees en tu libro, página N» de cada tarjeta (Q[n]["pag"] de ingN.py)."""
    if mis == 1:
        return 414 if n <= 14 else 415
    if mis == 2:
        return 424 if n <= 6 else 425
    if mis == 3:
        return {1: 435, 2: 435, 3: 436, 4: 437}[(n - 1) // 10 + 1]
    if mis == 4:
        return 447 if n <= 8 else 448
    if mis == 5:
        return 457 if n <= 7 else (458 if n <= 11 else 459)
    return {1: 468, 2: 469, 3: 470}[(n - 1) // 8 + 1]


def libro_num(mis, n):
    """Cómo se cita la tarjeta n en el libro: M4–M6 reinician la numeración en cada bloque."""
    if mis in (4, 5):
        return f"Bloque {1 if n <= 8 else 2}, n.º {(n - 1) % 8 + 1}"
    if mis == 6:
        return f"Bloque {(n - 1) // 8 + 1}, n.º {(n - 1) % 8 + 1}"
    if mis == 3:
        return f"texto {(n - 1) // 10 + 1}, espacio {n}"
    return f"n.º {n}"


# ─────────────────── las páginas del cuaderno, del manifiesto ───────────────────
def _manifiesto():
    d = json.load(open("/home/claude/tablero/manifiesto_hojas.json", encoding="utf-8"))
    return {x["svg"]: x["pagina"] for x in d if x.get("area") == "ing"}


PAG_SVG = _manifiesto()
# Qué tarjetas van en cada hoja de taller (build() de ingN.py): dos por hoja, en orden; en la Misión 1
# la hoja 11 lleva solo la 21 y el cierre de la misión.
N_HOJAS = {1: 11, 2: 5, 3: 20, 4: 8, 5: 8, 6: 12}


def pag_tarjeta(mis, n):
    return PAG_SVG[f"ing{mis}_t{(n - 1) // 2 + 1}"]


def pags_icfes(mis):
    return PAG_SVG[f"ing{mis}_i1"], PAG_SVG[f"ing{mis}_i2"]


def pags_mision(mis):
    ps = [p for s, p in PAG_SVG.items() if s.startswith(f"ing{mis}_")]
    return min(ps), max(ps)


def rango(ps):
    """Páginas: [269, 270, 271, 275] → «269 a 271 y 275» (lo mismo que nums())."""
    return nums(ps)


def nums(ns):
    """[8, 9, 10, 11] → «8 a 11»; [1, 2, 5, 6] → «1, 2, 5 y 6»: solo se juntan tramos de tres o más."""
    ns = sorted(set(ns))
    partes, i = [], 0
    while i < len(ns):
        j = i
        while j + 1 < len(ns) and ns[j + 1] == ns[j] + 1:
            j += 1
        if j - i >= 2:
            partes.append(f"{ns[i]} a {ns[j]}")
        else:
            partes += [str(x) for x in ns[i:j + 1]]
        i = j + 1
    return ", ".join(partes[:-1]) + (" y " if len(partes) > 1 else "") + partes[-1]


# ─────────────────────────────── las misiones ───────────────────────────────
MISIONES = {
 1: dict(comp="léxico · pragmático", parte="Partes 1 y 2",
   tema="La pista que decide",
   pasos=["¿persona, lugar o cosa?", "leo el verbo", "cada pista tacha", "tacho la que ya usé"],
   competencia="Partes 1 y 2 · palabras y avisos",
   estr=["El verbo delata la palabra", "Cada pista tacha opciones", "¿Dónde estaría este aviso?",
         "Quién me escribe y qué quiere"],
   instala="Que una descripción se lee por piezas: primero qué clase de cosa es (persona, lugar u "
           "objeto), después el verbo que la delata y por último las pistas que tachan opciones. Y que un "
           "aviso se entiende por quién lo escribe, qué quiere y dónde pasa eso.",
   ojo="Las claves de la Parte 1 salen casi en el orden alfabético del banco: quien marque «en orden» "
       "acierta sin leer. Cada tarjeta pide escribir la PALABRA antes de la letra: exígelo. El banco del "
       "grupo People muestra la I (Journalist) como opción; es la del ejemplo (Corrección EDUCATE, tarjeta 1).",
   cierre="La Parte 1 se trabaja como el examen: un grupo de siete descripciones con un banco que se va "
          "vaciando. Por eso en clase va el grupo People completo (1 a 7) y en el reto el grupo School Life "
          "(8 a 14)."),
 2: dict(comp="conversacional", parte="Parte 3",
   tema="Contéstale a la persona, no a la palabra",
   pasos=["¿qué clase de frase es?", "¿qué quiere quien habla?", "¿en qué tiempo está?",
          "la opción que le contesta a esa persona"],
   competencia="Parte 3 · conversaciones",
   estr=["¿Qué clase de pregunta me hacen?", "¿Qué me están pidiendo?", "El tiempo del verbo manda",
         "Reacciono a lo que me cuentan"],
   instala="Que en una conversación se contesta a la persona y no a la palabra: las opciones que repiten "
           "una palabra de la frase (printers, Internet, concerts) suenan bien y no contestan. Primero se "
           "decide qué clase de frase es y qué quiere quien habla.",
   ojo="En siete de las diez la correcta es la única que empieza por «Yes». No lo enseñes como truco: en "
       "el examen no siempre pasa. La pregunta 9 trae una opción con un error de concordancia («Mark and I "
       "was»): es la Corrección EDUCATE de la tarjeta.",
   cierre="La Misión 2 cabe entera en clase: diez tarjetas, cinco bloques. No deja tarea. Su reto es "
          "original: escribir la respuesta natural a seis frases que no están en el libro."),
 3: dict(comp="gramatical · léxico", parte="Parte 4",
   tema="Escucha a los vecinos del hueco",
   pasos=["leo el texto entero", "tapo las opciones: ¿qué pieza falta?", "busco la pista en las vecinas",
          "llamo a la subestrategia y marco"],
   competencia="Parte 4 · texto con espacios",
   estr=["El reloj del texto", "La forma que cabe", "La preposición viene pegada",
         "El conector dice la relación"],
   instala="Que el espacio no se llena con lo que suena: se tapan las opciones, se pregunta qué pieza falta "
           "(un verbo en su tiempo, una forma, una preposición, un conector) y se busca la pista en las "
           "palabras vecinas. El reloj del texto lo pone la primera oración.",
   ojo="Cuarenta espacios no caben en 35 minutos: en clase van diez de los cuatro textos (con los dos "
       "sellos), en el reto el texto 4 completo (el de las correcciones) y a la casa los demás, un texto por "
       "semana. El libro tiene ocho Corrección EDUCATE en esta misión: acéptalas como dicen las tarjetas.",
   cierre="La tarea de esta misión es la más larga del área (22 tarjetas cortas): un texto por semana, "
          "revisado con la ronda de claves de las clases 4, 5 y 6."),
 4: dict(comp="lectura", parte="Parte 5",
   tema="Lo que el texto dice, dato por dato",
   pasos=["el ancla de la pregunta", "cada dato con su dueño", "leo la frase vecina completa",
          "¿lo dice con otras palabras? ¿responde?"],
   competencia="Parte 5 · lectura literal",
   estr=["La palabra ancla", "Cada cifra tiene dueño", "Lo dice con otras palabras",
         "Es verdad, pero no responde"],
   instala="Que una pregunta literal se responde con el texto en la mano: se busca la palabra ancla, se "
           "lee la frase vecina completa y cada número se amarra a su dueño. Los distractores traen datos "
           "verdaderos del texto que no responden lo que preguntan.",
   ojo="El texto de la Vuelta dice que 2016 fue la primera vez que dos colombianos compartieron el podio: "
       "es falso (1989). Es la Corrección EDUCATE de la tarjeta 9. La tarjeta 14 tacha la nacionalidad que "
       "una opción le pone a Froome. El libro numera 1 a 8 en cada bloque; el cuaderno, 1 a 16.",
   cierre="La misión no deja tarea: diez tarjetas en clase y las otras seis en el reto, en relevo."),
 5: dict(comp="lectura", parte="Parte 6",
   tema="Leer entre líneas, con la prueba en la mano",
   pasos=["leo el texto entero", "¿qué deja entender?", "la frase que lo prueba",
          "descarto lo que el texto no sostiene"],
   competencia="Parte 6 · lectura inferencial",
   estr=["Lo que el texto deja entender", "Para qué lo pone el autor", "La frase que dice más de lo que dice",
         "Dos cosas frente a frente"],
   instala="Que inferir no es inventar: lo que el texto deja entender tiene que poder señalarse en una "
           "frase. Se pregunta para qué pone el autor cada ejemplo, qué dice de verdad una frase figurada y "
           "qué dos cosas pone frente a frente.",
   ojo="En casi todas las preguntas los distractores cierran con absolutos («exclusively», «completely», "
       "«all») y la correcta matiza. No lo enseñes como truco: la tarjeta 14 enseña a tratar la palabra "
       "fuerte como una alarma que se comprueba en el texto. Las cuatro del entrenamiento traen erratas "
       "corregidas por EDUCATE: la dirección de EDUCATE decide si se cambian.",
   cierre="La misión no deja tarea: diez tarjetas en clase y seis en el reto. Son preguntas largas: en el "
          "desarrollo guiado cada texto se lee una vez, entero, antes de su primer bloque de tarjetas."),
 6: dict(comp="gramatical · léxico", parte="Parte 7",
   tema="El texto entero decide el espacio",
   pasos=["leo el texto entero", "¿qué pieza falta?", "la pista: cerca o lejos",
          "pruebo la opción en la oración completa"],
   competencia="Parte 7 · texto con espacios",
   estr=["La línea de tiempo del verbo", "La palabra de al lado manda la forma", "Palabras que andan juntas",
         "El párrafo entero decide"],
   instala="Que la Parte 7 junta todo lo del área: el tiempo del verbo, la palabra que manda la forma, las "
           "palabras que andan juntas y el texto completo como prueba. El espacio se llena mirando cerca "
           "y, si no alcanza, el párrafo entero.",
   ojo="Seis Corrección EDUCATE en esta misión: dos con dos opciones correctas (2 y 9) en clase, una en la "
       "casa (3, falta «up») y tres en el reto (17, 20 y 23). La tarjeta 8 tiene el sello «Alto»: el pasado "
       "de un pasado. Es la última clase de contenido.",
   cierre="La tarea de la Misión 6 (seis tarjetas) se revisa al comenzar la clase 8, antes de la devolución "
          "del simulacro: la clase 7 es toda de prueba."),
}

# Claves del libro: docstring de ing1.py … ing6.py (verificar() las compara al construir).
# M3 · 32: ninguna opción sirve (Corrección EDUCATE): va «—».
_K = {1: "CABHDEFBACDEFGABACABC", 2: "CAABACABCB",
      3: "CABCBACBAC" "BACCACBACB" "ABCABCACBA" "B—CCACBACA",
      4: "BACABCCAACBCAABC", 5: "CADBCADBDAABDCBA", 6: "BBCABABAADBACBDACCBBCCCB"}
CLAVES = {m: dict(zip(range(1, len(k) + 1), k)) for m, k in _K.items()}

# ──────────── el reparto: qué se hace en clase, en el reto y en la casa (ver docstring) ────────────
# casa: [(tarjetas, clase en la que se revisa con la ronda de claves, rótulo de la entrega)]
REPARTO = {
 1: dict(clase=[1, 2, 3, 4, 5, 6, 7, 15, 16, 17], reto=[8, 9, 10, 11, 12, 13, 14],
         casa=[([18, 19, 20, 21], 2, "Parte 2, avisos")]),
 2: dict(clase=list(range(1, 11)), reto=[], casa=[]),
 3: dict(clase=[1, 3, 12, 14, 21, 23, 25, 29, 36, 38], reto=[31, 32, 33, 34, 35, 37, 39, 40],
         casa=[([2, 4, 5, 6, 7, 8, 9, 10], 4, "texto 1 · Karol G"),
               ([11, 13, 15, 16, 17, 18, 19, 20], 5, "texto 2 · Spider-Verse"),
               ([22, 24, 26, 27, 28, 30], 6, "texto 3 · AI in the Classroom")]),
 4: dict(clase=[1, 2, 3, 4, 7, 9, 11, 13, 14, 16], reto=[5, 6, 8, 10, 12, 15], casa=[]),
 5: dict(clase=[1, 3, 4, 5, 6, 7, 9, 12, 13, 15], reto=[2, 8, 10, 11, 14, 16], casa=[]),
 6: dict(clase=[1, 2, 5, 6, 8, 9, 12, 13, 14, 16], reto=[17, 18, 19, 20, 21, 22, 23, 24],
         casa=[([3, 4, 7, 10, 11, 15], 8, "bloques 1 y 2")]),
}


def ronda_de(clase):
    """La tarea que se revisa al comenzar esta clase: [(misión, tarjetas, rótulo)]."""
    return [(m, ns, rot) for m, r in REPARTO.items() for ns, c, rot in r["casa"] if c == clase]


# Clases 7 y 8 (decisión de Nelson, 10 nov): el simulacro es una prueba que escoge EDUCATE y no está en
# el cuaderno; la clase 8 socializa sus preguntas en las hojas de simulacro. C7 y C8: plan_simulacro.py.
# La clase 8 abre con la ronda de claves de la última tarea (la de la Misión 6).
import plan_simulacro as PS
_R8 = ronda_de(8)
C7, C8 = PS.datos("ing", conteo="familia de partes (palabras y avisos, gramática en el texto, lectura)", previo=(
    f"Abre con la ronda de claves de la tarea de la Misión {_R8[0][0]} (tarjetas {nums(_R8[0][1])}): cinco "
    f"minutos.") if _R8 else None, dinamica=dict(
    nombre="La línea que manda", formato="en parejas",
    pasos=["Parejas con la segunda pregunta asignada. B tapa las opciones con una hoja.",
           "A copia la línea que manda y dice en español lo que dice.",
           "B destapa una opción a la vez. A la acepta o la descarta diciendo la pista: la palabra de al "
           "lado, el tiempo del verbo, el lugar o quién habla, un conector o un número.",
           "Cambian de papel con la misma pregunta. Cada uno anota en su esquema lo que descartó y una "
           "palabra nueva."],
    entrena="Encontrar la pista antes de mirar las opciones, y descartar con una razón. Son «la línea que "
            "manda», «la pista que manda» y «descarté» del esquema."))


def destino(mis, n):
    r = REPARTO[mis]
    if n in r["clase"]:
        return "clase"
    if n in r["reto"]:
        return "reto"
    return "casa"


# ─────────── lo que el libro trae y hay que saber antes de entrar (de hallazgos.csv, de las
# Corrección EDUCATE impresas en el cuaderno y de tablero/propuestas/ingN_hallazgos.csv) ───────────
# Severidad: alta · media · baja · atención · corrección (la que el cuaderno ya corrige en la tarjeta).
AVISOS = {
 1: [("preg. 1 a 7", "corrección",
      "El banco del grupo People muestra la I (Journalist) con su círculo, como si fuera opción: es la del ejemplo.",
      "La tarjeta 1 lo dice: se tacha el círculo de la I y se escoge entre A y H."),
     ("preg. 21", "corrección",
      "Ninguna opción nombra con exactitud el lugar: inmigración y filtro de seguridad son puntos distintos del aeropuerto.",
      "Es de la casa: en la ronda de la clase 2, la C es la que más se acerca; vale el nombre exacto escrito al margen."),
     ("reparto de claves", "media",
      "Las claves de la Parte 1 salen casi en el orden alfabético del banco (C A B H D E F · B A C D E F G).",
      "No lo digas. Exige la palabra escrita antes de la letra. Va a la editorial."),
     ("preg. 2", "atención",
      "«This is a place» resuelve sola la pregunta: Factory es el único lugar del banco (y está en el grupo de personas).",
      "Úsala para el paso 1: ¿persona, lugar o cosa?"),
     ("preg. 8 y 13", "atención",
      "«Lecture» es un falso amigo (no es lectura) y «Seminar» está definido como «a group of students».",
      "Son del reto: dilo al revelar las claves. Las dos claves se sostienen.")],
 2: [("preg. 9", "corrección",
      "La opción B dice «Mark and I was»: error de concordancia (debe ser were). Corregida, B también respondería.",
      "La tarjeta pide encontrarla, tacharla y escribirla bien; la C se decide por lo que preguntan."),
     ("patrón «Yes»", "media",
      "En 7 de las 10 la correcta es la única que empieza por «Yes»; ninguna distractora empieza así.",
      "No lo enseñes como truco: exige el instrumento (qué quiere quien habla)."),
     ("preg. 10", "atención",
      "La C («I prefer drinking juice instead of water») es posible en una charla real; la B reacciona al consejo.",
      "Si alguien defiende la C, discútelo. La clave es B."),
     ("imágenes 2 y 8", "atención",
      "Las ilustraciones parecen generadas por IA y la de la 8 trae el logotipo de una red social.",
      "Nada en clase. Está en el informe del libro.")],
 3: [("preg. 12", "corrección",
      "La opción A está mal escrita («was release»). Corregida a lápiz («was released») es la clave.",
      "B («It released») es informal: acéptala solo si la defienden. Sello «Alto»: la voz pasiva."),
     ("preg. 32", "corrección",
      "Ninguna opción arma «acting ___ the interests of»: va «in».",
      "Reto: no se marca letra, se escribe in. «On behalf of» también es buena idea."),
     ("preg. 34, 35 y 39", "corrección",
      "34: as, since y because son correctas; 35: through y on; 39: since y but se defienden.",
      "Reto: es la discusión del equipo. Acepta las defendidas con la pista."),
     ("preg. 17 a 20 · 24", "corrección",
      "17 a 20: valen el pasado del relato (combined, dealt, tried, left) y el presente de la trama; 24: by, "
      "with y through son correctas.",
      "Son de la casa: en las rondas de las clases 5 y 6 acéptalas (en 18 a 20, el mismo reloj en las tres)."),
     ("preg. 29 · 33 · 40", "atención",
      "29: to no es preposición sino la marca del infinitivo; 33: through también se defiende; 40: el «an» descarta solo la C.",
      "Dilo al revelar. No cambian las claves.")],
 4: [("preg. 9", "corrección",
      "El texto dice que 2016 fue la primera vez que dos colombianos compartieron el podio: falso (1989, Parra y Vargas).",
      "Se corrige a lápiz: fue la primera vez que un colombiano ganó con otro colombiano en el podio. No cambia claves."),
     ("preg. 14", "corrección",
      "La opción A le pone a Froome una nacionalidad («British») que el texto no dice.",
      "Se tacha esa palabra y se decide con el equipo y el puesto. Clave A."),
     ("preg. 8", "corrección", "Falta «in»: «reflected in topping global charts».",
      "Es del reto. No cambia ninguna clave."),
     ("preg. 6", "baja", "La opción A («three full albums and two LP») no tiene sentido: un LP es un álbum.",
      "Va a la editorial. La clave C no cambia."),
     ("numeración", "atención", "El libro numera 1 a 8 en cada bloque; el cuaderno, 1 a 16.",
      "Al citar una pregunta del libro, di el bloque.")],
 5: [("absolutos", "media",
      "En casi todas, los distractores cierran con absolutos (exclusively, completely, all) y la correcta matiza.",
      "No lo enseñes como truco: la palabra fuerte es una alarma que se comprueba en el texto."),
     ("preg. 13", "atención",
      "«Urban indifference» no está en el texto: se infiere del primer párrafo (la gente que pasa de afán).",
      "La tarjeta lo arma: ¿dónde estaba el silencio en el primer párrafo?"),
     ("preg. 14", "atención",
      "La clave C se sostiene con los tambores y «shared roots», pero el rap del texto improvisa «about politics or love».",
      "Es del reto. Es la mejor de las cuatro."),
     ("claves del Bloque 1", "atención", "C A D B C A D B: un patrón que se repite cada cuatro.",
      "No lo digas en clase. Va a la editorial."),
     ("ICFES 1 a 4", "media",
      "Las cuatro de entrenamiento traen erratas que EDUCATE corrigió a mano: la dirección de EDUCATE decide si se cambian.",
      "Texto con erratas corregidas por EDUCATE; pendiente de decisión.")],
 6: [("preg. 2 y 9", "corrección",
      "Dos opciones correctas: felt y were feeling (2); express y explore (9). El libro espera una.",
      "La tarjeta pide encontrar y marcar las dos."),
     ("preg. 17, 20 y 23", "corrección",
      "17: lit y lighted son correctas; 20: los pasos no «corren» (sounded, echoed); 23: falta «to» (listened to).",
      "Reto: el equipo lo discute con la tarjeta."),
     ("preg. 3", "corrección", "Falta «up»: se dice «set up a tent».",
      "Casa: se revisa en la ronda de la clase 8."),
     ("preg. 7 · 10 · 14", "atención",
      "7: lo natural sería «have started»; 10: «involve subjects» es poco natural; 14: used también es gramatical.",
      "No cambian las claves: decide el tiempo del párrafo."),
     ("reparto de claves", "atención", "A 6 · B 9 · C 7 · D 2; el Bloque 3 no tiene ninguna A ni D.",
      "No lo digas. Va a la editorial.")],
}

# ─────────── los sellos «Alto · aquí entra el profe» del cuaderno (alto_profe() en ing3.py, ing6.py
# e ing3_icfes.py) ───────────
_S = [(3, 12, "La voz pasiva: cuando el sujeto recibe la acción, el verbo se arma con was o were más la tercera forma."),
      (3, 36, "Los conectores de contraste: unos van delante de una oración, otros delante de un sustantivo y "
              "otros sueltos, con coma."),
      (3, "ICFES 1", "El presente perfecto (has been): algo que empezó en el pasado y sigue hasta hoy."),
      (6, 8, "El pasado de un pasado (had + participio) y el futuro visto desde el pasado (would).")]


def _pag_sello(m, preg):
    return pag_tarjeta(m, preg) if isinstance(preg, int) else pags_icfes(m)[0]


SELLOS = [(AREA_CSV, m, _pag_sello(m, p), p, s, "tarjeta de la pregunta", "En el cuaderno") for m, p, s in _S]

# Lo que el profe tiene que poder explicar en cada sello: título, qué es (sin jerga) y la pregunta
# que destraba. La del entrenamiento va con clave "I1".
SABERES = {
 (3, 12): ("La voz pasiva",
           "Cuando el sujeto no hace la acción sino que la recibe, el inglés arma el verbo con was o were más la "
           "tercera forma: «The cake was made by my mother» (el pastel no hizo nada; lo hicieron). La película "
           "no estrena: la estrenan. Ejemplo que no es del texto: «The window was broken».",
           "¿«It» hace la acción o la recibe?"),
 (3, 36): ("Los conectores de contraste",
           "Los tres oponen dos ideas, pero no se usan igual: although va delante de una oración completa "
           "(although it rained, we played); despite, delante de un sustantivo (despite the rain, we played); "
           "however va suelto, con coma (It rained. However, we played).",
           "¿Lo que viene después del espacio trae verbo o es solo un sustantivo?"),
 (3, "I1"): ("El presente perfecto",
             "Has o have más la tercera forma del verbo (has been, have lived). Cuenta algo que empezó en el pasado "
             "y sigue hasta hoy: «I have lived here since 2015». Con «since» va el punto de inicio; con «for», "
             "cuánto tiempo.",
             "¿Eso empezó y terminó, o empezó y sigue?"),
 (6, 8): ("El pasado de un pasado y el futuro visto desde el pasado",
          "Had más la tercera forma cuenta algo que pasó antes de otro pasado: «When I arrived, the bus had "
          "left». Would, en un relato en pasado, mira hacia adelante desde ese pasado: «I never thought I "
          "would like it».",
          "¿Esto pasó antes de otra cosa que ya pasó?"),
}

# ─────────── «Si Inglés no es tu fuerte»: cuatro conceptos por clase ───────────
NO_ES_TU_FUERTE = {
 1: [("Descripción y palabra (Parte 1)",
      "El examen da descripciones cortas y un banco de palabras: hay que emparejarlas. Sobra una o dos. Se lee "
      "por piezas: «This is a person who…» (persona), «a place where…» (lugar), y el verbo dice qué hace."),
     ("Los oficios en inglés",
      "Muchos oficios terminan en -er, -or, -ist o -ian: driver (el que maneja), actor, artist, technician. Si "
      "conoces el verbo (drive, paint, repair), encuentras al que lo hace."),
     ("Falsos amigos",
      "Palabras que parecen español y no lo son: lecture es clase magistral (no lectura), library es "
      "biblioteca (librería es bookshop). Si un estudiante traduce por el parecido, pídele la pista."),
     ("Avisos (Parte 2)",
      "Un aviso corto se entiende por tres preguntas: quién lo escribe, qué quiere (informa, pide, prohíbe, "
      "vende) y dónde pasa eso. La palabra rara del aviso (turbulence, subscription) suele decir el lugar.")],
 2: [("Tipos de frase",
      "Si empieza por un verbo (Is, Does, Did, Can) pide sí o no; si empieza por What, Where o How much, pide "
      "un dato. Could you…? es un pedido; Shall I…? es un ofrecimiento; Do you think…? pide una opinión."),
     ("Contestar a la persona",
      "La respuesta natural contesta lo que la persona quiere. Las opciones que repiten una palabra de la frase "
      "(printers, Internet, TV) suelen ser trampas: hablan del tema, pero no le contestan."),
     ("El tiempo manda",
      "Did you…? pregunta por algo que ya pasó y se contesta en pasado (Yes, I did; it was great). Last night, "
      "yesterday y ago marcan el pasado."),
     ("Reaccionar",
      "Cuando alguien cuenta una noticia o da una opinión se reacciona: That's great!, Oh no!, I agree, That's "
      "true. No se contesta con un dato que nadie pidió.")],
 3: [("El pasado simple",
      "Los regulares terminan en -ed (lasted, shared). Los irregulares se aprenden: come → came, begin → "
      "began, sing → sang, know → knew, think → thought, go → went."),
     ("Was o were",
      "Was con I, he, she, it y una sola cosa; were con you, we, they y con varias cosas (the people were, "
      "audiences were). El sujeto puede estar lejos del verbo."),
     ("Preposiciones pegadas",
      "Muchas palabras llevan siempre la misma preposición: depend on, search for, popular among, prepared "
      "for, combined with. No se deducen del español: se aprenden en pareja."),
     ("Conectores",
      "Because da la causa; so, la consecuencia; but y although, el contraste; not only… but also suma dos "
      "cosas. Para escoger, se mira qué relación hay entre las dos ideas.")],
 4: [("La palabra ancla",
      "La palabra que comparten la pregunta y el texto: un nombre, una fecha, un lugar (Sydney, November 8th, "
      "Lagos de Covadonga). Se busca en el texto y se lee la oración completa donde está."),
     ("Números y fechas en inglés",
      "November 1st (primero), 8th (octavo); 1.5 million = un millón y medio (el inglés usa punto decimal); "
      "twenty-one = 21; the sixties = los años sesenta."),
     ("Decir lo mismo con otras palabras",
      "El examen rara vez copia el texto: Madrid es «Spain's capital city»; «finished second» es «arrived "
      "second». Hay que reconocer la misma idea dicha distinto."),
     ("El distractor verdadero",
      "Una opción puede traer un dato que sí está en el texto y no responder lo que preguntan (Sydney es "
      "verdad, pero los conciertos del 8 y el 9 son en Melbourne).")],
 5: [("Inferir",
      "Es sacar lo que el texto no dice con todas las letras pero deja entender. Siempre tiene que haber una "
      "frase que lo pruebe: si no se puede señalar, es invento."),
     ("Para qué lo pone el autor",
      "Un ejemplo o un detalle está para algo: ilustrar una idea, contrastar, convencer o mostrar que algo "
      "pasa cerca (los árboles de la ciudad, el andén roto)."),
     ("Sentido figurado",
      "«Foundation» es la base de una casa: si se cae, se cae todo. «I am here, my story matters» no es una "
      "letra de canción: es alguien que dice que existe y que vale."),
     ("Palabras absolutas",
      "Exclusively, completely, all, never: en las opciones casi siempre exageran. No es un truco: es una "
      "alarma que se comprueba en el texto.")],
 6: [("Los tiempos del relato",
      "Pasado simple (went, felt); pasado continuo, una acción larga (were setting); presente perfecto, desde "
      "el pasado hasta hoy (have been); pasado perfecto, antes de otro pasado (had imagined)."),
     ("La palabra de al lado",
      "Have o has piden la tercera forma (have taken); to pide el verbo sin cambios (to develop); un sujeto "
      "plural pide were o feel; uno solo, was o feels."),
     ("Palabras que andan juntas",
      "Express points of view, develop critical thinking, check evidence, allow someone to: son parejas fijas "
      "(colocaciones). Se reconocen porque «suenan» en inglés, y eso se entrena leyendo."),
     ("El párrafo entero",
      "Cuando la oración sola no decide, decide el párrafo: si todo va en presente, el espacio también; si es "
      "un relato en pasado, el espacio sigue ese reloj.")],
}

# Pronunciación aproximada de las palabras clave de cada clase, para un profe que no domina el
# inglés. Escrita a la española; la sílaba fuerte va con tilde. La revisa un especialista.
PRONUNCIA = {
 1: [("technician", "tek-NÍ-shan"), ("volunteer", "vo-lun-TÍR"), ("passenger", "PÁ-sen-yer"),
     ("driver", "DRÁI-ver"), ("library", "LÁI-bre-ri"), ("borrow", "BÓ-rou"),
     ("turbulence", "TÉR-biu-lens"), ("boarding pass", "BÓR-din pas")],
 2: [("could", "cud"), ("shall", "shal"), ("budget", "BÁ-yet"), ("enough", "i-NÁF"),
     ("episode", "É-pi-soud"), ("hydrated", "JÁI-drei-tid"), ("right away", "ráit a-UÉI"),
     ("I agree", "ái a-GRÍ")],
 3: [("began", "bi-GÁN"), ("knew", "niú"), ("thought", "zot"), ("released", "ri-LÍST"),
     ("among", "a-MÁNG"), ("because", "bi-KÓS"), ("despite", "dis-PÁIT"), ("undeniable", "an-di-NÁI-a-bol")],
 4: [("venue", "VÉ-niu"), ("stage", "STÉICH"), ("stadium", "STÉI-di-um"), ("debuted", "DÉI-biud"),
     ("jersey", "YÉR-si"), ("podium", "PÓU-di-um"), ("worldwide", "UÓRLD-uaid"), ("viewers", "VIÚ-ers")],
 5: [("photosynthesis", "fou-tou-SÍN-ze-sis"), ("breathable", "BRÍ-da-bol"), ("foundation", "faun-DÉI-shon"),
     ("deforestation", "di-fo-res-TÉI-shon"), ("sidewalk", "SÁID-uok"), ("pedestrians", "pe-DÉS-tri-ans"),
     ("heritage", "JÉ-ri-tich"), ("anonymity", "a-no-NÍ-mi-ti")],
 6: [("went", "uént"), ("taken", "TÉI-ken"), ("debate", "di-BÉIT"), ("thinking", "ZÍN-kin"),
     ("evidence", "É-vi-dens"), ("lit", "lit"), ("footsteps", "FÚT-steps"), ("wandering", "UÁN-de-rin")],
}

PREGUNTA_AREA = "¿Qué palabra del texto te lo dice?"
PROBLEMATIZADORA = {
 1: "¿Qué palabra de la descripción decide, y qué opciones tacha?",
 2: "¿Qué quiere de verdad la persona que me habla?",
 3: "¿Qué palabra vecina del espacio me dice qué pieza falta?",
 4: "¿En qué frase del texto está eso, dicho con estas o con otras palabras?",
 5: "¿Qué frase del texto me deja entender eso?",
 6: "¿Qué parte del texto entero decide el espacio?",
}

# Una frase corta y ORIGINAL en inglés para la activación, sin nombres propios, con una pista que
# decide. La pista es para el final del momento. Ninguna usa el caso de una pregunta del libro.
ACTIVACION = {
 1: ("This person brings letters to your house, but he does not write them.",
     "«brings» dice qué hace y el «but does not» tacha al que escribe: es el cartero (mail carrier)"),
 2: ("Sorry, could you say that again?",
     "empieza por «could», pero no pregunta si puedes: te pide un favor (que repitas). Se contesta repitiendo"),
 3: ("Yesterday my little sister ___ a cake for my birthday. (make)",
     "«yesterday» pone el reloj en pasado: made"),
 4: ("The bus leaves at 6:15, but on Sundays it leaves at 7:30. — When does the bus leave on Sundays?",
     "la palabra ancla es «Sundays»: 6:15 es verdad, pero no responde"),
 5: ("When I opened the door, everybody shouted «Surprise!» and the lights came on.",
     "nadie dice «fiesta» ni «cumpleaños», pero «Surprise!» y las luces lo dejan entender"),
 6: ("My grandmother is eighty, but she ___ to the gym three times a week. (go)",
     "«three times a week» es una costumbre y el sujeto es ella sola: goes"),
}

# Las competencias del simulacro (clase 7): en Inglés el examen se lee por partes; se agrupan en tres
# familias de ocho preguntas cada una.
GRUPO_ICFES = {1: "LP", 2: "LP", 3: "GT", 4: "LE", 5: "LE", 6: "GT"}
GRUPO_NOM = {"LP": ("Palabras, avisos y conversación", "Partes 1, 2 y 3 · misiones 1 y 2"),
             "GT": ("Gramática en el texto", "Partes 4 y 7 · misiones 3 y 6"),
             "LE": ("Lectura", "Partes 5 y 6 · misiones 4 y 5")}


# ─────────────────────── lo que ya está registrado ───────────────────────
def _instrumentos():
    """Las filas de Inglés de tablero/instrumentos.csv. La pregunta del entrenamiento viene como
    «A»…«D», «QA»…«QD» o «1»…«4»: se normaliza a 1…4."""
    from extrae_instrumentos import filas
    taller, icfes = {}, {}
    for a, mis, p, est, ins, ctx in filas():
        if a != AREA_CSV:
            continue
        es_icfes = "ICFES" in str(mis)
        k = int(str(mis).split()[0])
        p = str(p).replace("Q", "")
        n = "ABCD".index(p) + 1 if p in "ABCD" else int(p)
        (icfes if es_icfes else taller).setdefault(k, []).append((n, est, ins, ctx))
    for d in (taller, icfes):
        for k in d:
            d[k].sort()
    return taller, icfes


def _banco():
    """Las filas «ING Mn» de icfes.csv, en el orden del cuaderno (P1…P4 = QA…QD)."""
    with open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig") as f:
        r = list(csv.DictReader(f))
    out = {}
    for x in r:
        m = x["mision"].strip()
        if m.startswith("ING M"):
            out.setdefault(int(m.replace("ING M", "")), []).append(dict(x))
    return out


TALLER_TODO, INS_ICFES = _instrumentos()
# Para el motor de las guías: TALLER son solo las diez de clase de cada misión.
TALLER = {m: [t for t in TALLER_TODO[m] if t[0] in REPARTO[m]["clase"]] for m in TALLER_TODO}
BANCO = _banco()


def limpia(t):
    """Carlito no trae el glifo ⚠: la alerta se marca con color, no con el símbolo."""
    return t.replace("⚠ ", "").replace("⚠", "").strip()


def sellos_de(mis):
    return [s for s in SELLOS if str(s[1]) == str(mis)]


def _claves_docstring(mis):
    doc = ast.get_docstring(ast.parse(open(f"/home/claude/libro/ing{mis}.py", encoding="utf-8").read()))
    if mis in (5, 6):                       # traen la lista completa en una línea «En orden: …»
        doc = doc[doc.index("En orden:"):]
    k = {}
    for n, c in re.findall(r"(?<![\w·])(\d+)·([A-H])", doc):
        k.setdefault(int(n), c)
    return k


def verificar():
    """Lo que tiene que cuadrar antes de dibujar: claves del libro contra el docstring de ingN.py,
    claves del entrenamiento (.md · módulo · icfes.csv), el reparto (cada tarjeta en un solo lugar,
    diez en clase, los sellos en clase) y la subestrategia de cada pregunta. Devuelve las diferencias."""
    import textos_ing
    malas = textos_ing.verificar()
    for m in range(1, 7):
        k = _claves_docstring(m)
        for n, c in CLAVES[m].items():
            if c != "—" and k.get(n) != c:
                malas.append(f"M{m} · {n}: plan {c} · docstring de ing{m}.py {k.get(n)}")
        if len(CLAVES[m]) != TOTAL_PREG[m] or len(TALLER_TODO.get(m, [])) != TOTAL_PREG[m]:
            malas.append(f"M{m}: {len(CLAVES[m])} claves y {len(TALLER_TODO.get(m, []))} tarjetas")
        r = REPARTO[m]
        todas = r["clase"] + r["reto"] + [n for ns, _, _ in r["casa"] for n in ns]
        if sorted(todas) != list(range(1, TOTAL_PREG[m] + 1)):
            malas.append(f"M{m}: el reparto no cubre cada tarjeta una sola vez")
        if len(r["clase"]) != 10 or len(TALLER[m]) != 10:
            malas.append(f"M{m}: {len(r['clase'])} tarjetas de clase")
        for _, mm, _, p, *_ in SELLOS:
            if mm == m and isinstance(p, int) and p not in r["clase"]:
                malas.append(f"M{m}: la tarjeta {p} tiene sello y no está en clase")
        ests = {e for _, e, _, _ in TALLER[m]}
        if ests != set(MISIONES[m]["estr"]):
            malas.append(f"M{m}: las diez de clase no cubren las cuatro subestrategias ({ests})")
        for p, e, _, _ in TALLER_TODO[m] + INS_ICFES[m]:
            if e not in MISIONES[m]["estr"]:
                malas.append(f"M{m} · {p}: subestrategia «{e}» no está en la misión")
        if len(INS_ICFES[m]) != 4 or len(BANCO.get(m, [])) != 4:
            malas.append(f"M{m}: {len(INS_ICFES[m])} instrumentos ICFES y {len(BANCO.get(m, []))} en icfes.csv")
    return malas


# ─────────────────────────── banco de dinámicas ───────────────────────────
# Isomorfas a la subestrategia: lo que hace el cuerpo es el mismo movimiento que después hará la mente
# frente al texto en inglés. La E1 abre la clase (8'); las otras tres van entre bloques del desarrollo
# guiado (3'). Ninguna usa el caso de una pregunta del libro ni del entrenamiento: se entrena el
# movimiento, no la respuesta. Las frases en inglés son originales.
DINAMICAS = {
 1: [("El verbo que te delata", 8,
      ["Ocho estudiantes al frente con un cartel: MECHANIC, PILOT, WAITER, FIREFIGHTER, FARMER, DENTIST, "
       "CASHIER y KITCHEN. El resto los mira.",
       "El docente dice una descripción sin el nombre, despacio y marcando el verbo: «This person FIXES "
       "cars», «This person SERVES food».",
       "Antes de señalar, el grupo repite solo el verbo y dice en español qué hace esa persona; después señala "
       "el cartel, y ese estudiante se sienta: su palabra ya se usó.",
       "Última ronda: «This is a PLACE where you cook». El grupo dice primero si es persona o lugar."],
      "Ir del verbo de la descripción a la palabra, y separar personas de lugares antes de mirar el banco. "
      "Es el movimiento de las tarjetas 1, 4 y 6 (repairs, drives, creates) y de la primera del "
      "entrenamiento (wear).",
      "Ocho carteles"),
     ("La pista que te sienta", 3,
      ["Seis estudiantes de pie con una prenda escrita: JACKET, GLOVES, SCARF, SANDALS, CAP y BOOTS.",
       "El docente lee la descripción por pedazos: «You wear it…» (todos siguen de pie) «…on your feet…» "
       "(se sientan los que no van en los pies) «…when it is hot» (se sienta BOOTS).",
       "Antes de cada pedazo, el grupo dice quién se va a sentar y por qué.",
       "Gana la descripción en la que queda una sola palabra de pie. Se repite con otra lista."],
      "Leer la descripción pista por pista y tachar con cada una hasta que quede una sola. Es el movimiento "
      "de las tarjetas 3, 5 y 7 (but is not, without, but does not) y de la segunda del entrenamiento.",
      "Seis hojas con una palabra"),
     ("¿En qué rincón está el aviso?", 3,
      ["Cuatro rincones del salón con un cartel: SWIMMING POOL, BANK, BAKERY y HOSPITAL.",
       "El docente lee un aviso inventado: «Swimmers must take a shower first», «Take a number and wait», "
       "«Fresh bread every morning at six», «Visitors: two at a time».",
       "Cada uno camina al rincón donde vería ese aviso.",
       "Antes de volver, alguien de cada rincón dice la palabra del aviso que lo llevó allí."],
      "Buscar la palabra rara del aviso y preguntarse dónde pasa eso, antes de mirar las opciones. Es el "
      "movimiento de las tarjetas 15 y 17 y de la tercera del entrenamiento.",
      "Cuatro carteles"),
     ("El cartero de mensajes", 3,
      ["El docente reparte cuatro mensajes en tiras: «Your order is on its way», «Please do not run in the "
       "hall», «Big sale: everything at half price», «Can you bring a pencil tomorrow?».",
       "Quien tiene la tira la lee en voz alta como si la hubiera escrito él.",
       "El grupo contesta con un gesto: mano abierta, informa; mano extendida, pide; mano en alto, prohíbe; "
       "frotar los dedos, vende.",
       "Después dicen quién escribe ese mensaje y a quién."],
      "Decidir qué quiere el mensaje y quién lo escribe antes de buscar el lugar. Es el movimiento de las "
      "tarjetas 16, 18 y 20 y de la cuarta del entrenamiento (New toys).",
      "Cuatro tiras de papel")],
 2: [("La primera palabra manda", 8,
      ["El docente dice frases en inglés, una por una: «Is it cold outside?», «Where is the bathroom?», "
       "«Can you swim?», «What time is it?», «I love this song!».",
       "Si la frase empieza por un verbo (Is, Can, Do, Did) todos se ponen de pie: pide sí o no.",
       "Si empieza por What, Where, When o How, levantan la mano: pide un dato. Si no es pregunta, se quedan "
       "sentados.",
       "Alguien contesta en dos o tres palabras (Yes, it is. At six.) y el grupo dice si le contestó a la persona."],
      "Decidir qué clase de frase es antes de pensar la respuesta. Es el movimiento de las tarjetas 3 y 5 y "
      "de la primera del entrenamiento (How much…?).",
      "Ninguno"),
     ("Te pido, te ofrezco", 3,
      ["En parejas. Uno dice una frase de una tira: «Could you open the window?», «Shall I carry your "
       "bag?», «Do you think we should leave now?».",
       "El otro, antes de hablar, hace con el cuerpo lo que le piden u ofrecen: abre la ventana de mentiras, "
       "recibe o rechaza la bolsa, dice sí o no con la cabeza.",
       "Solo después dice la frase: «Sure!», «That's fine, thanks», «Yes, I think so».",
       "Cambian los papeles con otra tira."],
      "Saber qué me están pidiendo (un favor, una ayuda, una opinión) antes de contestar. Es el movimiento "
      "de las tarjetas 1, 2 y 4 y de la segunda del entrenamiento (Shall I…?).",
      "Tiras con seis frases"),
     ("Ayer, ahora, mañana", 3,
      ["Tres zonas en el piso con cinta: YESTERDAY, NOW y TOMORROW.",
       "El docente lee una pregunta: «Did you sleep well?», «Are you hungry?», «Will you come tomorrow?», "
       "«Did you see the game?».",
       "Un estudiante salta a la zona de esa pregunta y dice la palabra que lo decidió (did, are, will).",
       "Contesta en el mismo tiempo: «Yes, I did», «No, I'm not»."],
      "Que el tiempo del verbo de la pregunta mande el tiempo de la respuesta. Es el movimiento de las "
      "tarjetas 6, 8 y 9 y de la tercera del entrenamiento (rained last night).",
      "Cinta"),
     ("La cara antes de la frase", 3,
      ["El docente cuenta una noticia o da una opinión: «I lost my phone!», «This pizza is amazing!», "
       "«I passed the exam!», «I think homework is boring».",
       "El grupo reacciona primero con la cara: triste, feliz, de acuerdo, en desacuerdo.",
       "Después alguien dice la frase que va con esa cara: «Oh no!», «Congratulations!», «I agree», "
       "«Really? I don't think so».",
       "El docente pregunta: ¿le contestaste a la noticia o a una palabra suelta?"],
      "Reaccionar a lo que la persona cuenta, no a una palabra de la frase. Es el movimiento de las "
      "tarjetas 7 y 10 y de la cuarta del entrenamiento (a cold sandwich).",
      "Ninguno")],
 3: [("Los tres relojes de la pared", 8,
      ["Tres carteles en la pared: PASADO (yesterday, last…, ago), COSTUMBRE (every day, always) y AHORA "
       "(now, at the moment).",
       "El docente lee una oración inventada con un hueco y dice «blank»: «Last summer we blank to the "
       "beach (go)».",
       "Cada uno camina al reloj que marca la oración y dice la palabra que lo llevó allí.",
       "Desde el reloj dicen la forma del verbo (went). En la última ronda el marcador está una oración antes."],
      "Encontrar el marcador de tiempo, aunque esté lejos, y escoger el verbo de ese reloj. Es el "
      "movimiento de las tarjetas 1 y 14 y de la primera del entrenamiento (has been… since).",
      "Tres carteles"),
     ("Sujeto y verbo de la mano", 3,
      ["La mitad del grupo tiene un sujeto (I, She, They, The dog, My friends, The people) y la otra mitad un "
       "verbo (is, are, was, were, has, have).",
       "A la señal, cada sujeto busca un verbo que le quepa y se dan la mano.",
       "Cada pareja dice su oración corta en voz alta: «My friends were late».",
       "El grupo revisa: si una pareja no concuerda, se sueltan y buscan otra."],
      "Mirar el sujeto (uno o varios) antes de escoger la forma del verbo. Es el movimiento de las tarjetas "
      "3, 12 y 29 y de la segunda del entrenamiento (was described).",
      "Doce tarjetas"),
     ("Imanes", 3,
      ["Unos tienen una palabra (listen, wait, interested, good, afraid, look) y otros una preposición (to, "
       "for, in, at, of).",
       "A la señal, cada palabra busca su imán: la preposición que siempre la acompaña.",
       "Cada pareja dice una oración: «I'm afraid of dogs», «Wait for me».",
       "Si dos preposiciones quieren la misma palabra, el grupo decide cuál suena en inglés."],
      "Recordar que la preposición viene pegada a la palabra de antes y no se deduce del español. Es el "
      "movimiento de las tarjetas 21 y 23 y de la tercera del entrenamiento (found out).",
      "Once tarjetas"),
     ("La cuerda", 3,
      ["Dos estudiantes sostienen una cuerda, uno en cada punta.",
       "El docente dice dos ideas: «It was raining… we played football», «I was hungry… I made a sandwich».",
       "Si las ideas tiran juntas, los dos jalan hacia el mismo lado; si tiran en contra, cada uno hacia el suyo.",
       "El grupo escoge el conector: because, so, and; o but, although, despite."],
      "Ver qué relación hay entre dos ideas antes de escoger el conector. Es el movimiento de las tarjetas "
      "25, 36 y 38 y de la cuarta del entrenamiento (While).",
      "Una cuerda")],
 4: [("Cazadores de anclas", 8,
      ["El docente pega en cinco paredes cinco oraciones de un texto corto inventado sobre una feria del "
       "libro: fechas, lugar, precios, nombres.",
       "Lee una pregunta: «When does the fair open?», «How much is the ticket for students?».",
       "En equipos, dicen la palabra ancla (open, students) y caminan a la pared que la tiene.",
       "Leen en voz alta la oración completa y responden solo con lo que dice."],
      "Buscar en el texto la palabra que comparte con la pregunta y leer la oración entera donde está. Es el "
      "movimiento de las tarjetas 1 y 7 y de la primera del entrenamiento (Passionate Falsehoods).",
      "Cinco hojas en las paredes"),
     ("Cada número a su dueño", 3,
      ["El docente lee un párrafo corto con cuatro números: el año en que abrió el colegio, los estudiantes, "
       "las horas de clase y el precio del almuerzo.",
       "Cuatro estudiantes reciben un número y otros cuatro una etiqueta (year, students, hours, price).",
       "Cada número busca su etiqueta y los dos dicen la frase completa.",
       "El docente pregunta por uno de los números con otra palabra y el grupo lo encuentra."],
      "Amarrar cada cifra a su dueño antes de responder. Es el movimiento de las tarjetas 4, 11 y 16 y de "
      "la tercera del entrenamiento (from 1960 to 1979).",
      "Ocho tarjetas"),
     ("La misma idea con otro traje", 3,
      ["El docente lee una oración: «The shop opens at nine».",
       "Cinco estudiantes tienen una tarjeta con otra oración; se paran los que dicen lo mismo con otras "
       "palabras («The store starts working at 9 a.m.») y se quedan sentados los que dicen otra cosa.",
       "Cada uno que se paró dice qué palabra cambió por cuál.",
       "Se repite con dos oraciones más."],
      "Reconocer la misma idea dicha con otras palabras. Es el movimiento de las tarjetas 3, 9 y 13 y de la "
      "segunda del entrenamiento.",
      "Quince tarjetas"),
     ("¿Verdad o respuesta?", 3,
      ["El docente lee un texto de tres oraciones y hace una pregunta.",
       "Un voluntario dice un dato verdadero del texto que NO responde la pregunta; otro, el que sí responde.",
       "El grupo vota con el pulgar: de lado, es verdad pero no responde; arriba, responde.",
       "Se repite cambiando la pregunta sobre el mismo texto."],
      "Comparar cada opción con dos preguntas: ¿está en el texto?, ¿responde lo que preguntan? Es el "
      "movimiento de las tarjetas 2 y 14 y de la cuarta del entrenamiento (The Last Book).",
      "Ninguno")],
 5: [("Detectives de la mochila", 8,
      ["El docente muestra o lee lo que hay en una mochila inventada: a ticket, sunscreen, a map, a camera.",
       "En equipos escriben una inferencia: a dónde va la dueña y para qué.",
       "Cada equipo defiende la suya señalando el objeto que la prueba.",
       "Si una inferencia no se puede señalar en un objeto, se tacha: es invento."],
      "Inferir con la prueba en la mano: lo que se deja entender tiene que poder señalarse. Es el movimiento "
      "de las tarjetas 1 y 3 y de la primera del entrenamiento (Mark y la comida rápida).",
      "Cuatro objetos o una lista"),
     ("¿Para qué me lo cuentas?", 3,
      ["Cuatro rincones: PARA DAR UN EJEMPLO, PARA CONTRASTAR, PARA CONVENCER y PARA MOSTRAR QUE PASA CERCA.",
       "El docente lee un párrafo corto con un detalle: «Even in our school, the garden has fewer bees every year».",
       "Cada uno camina al rincón del para qué.",
       "Alguien de cada rincón dice qué idea del párrafo sostiene ese detalle."],
      "Preguntar para qué pone el autor un detalle o un ejemplo. Es el movimiento de las tarjetas 7, 9 y 15 "
      "y de la segunda del entrenamiento (Jonathan).",
      "Cuatro carteles"),
     ("Lo que dice y lo que quiere decir", 3,
      ["El docente lee una frase figurada: «My room is a jungle», «This homework is a mountain».",
       "El grupo la actúa primero al pie de la letra: monos y árboles; escalar una montaña.",
       "Después la actúa con lo que quiere decir: un cuarto desordenado, una tarea larga.",
       "Alguien dice en español lo que la frase dice de verdad."],
      "Separar lo que la frase dice de lo que quiere decir. Es el movimiento de las tarjetas 5, 12 y 13 y "
      "de la tercera del entrenamiento (If you die, will you enjoy it?).",
      "Ninguno"),
     ("Frente a frente", 3,
      ["Dos filas, una frente a la otra. Una tiene tarjetas de ANTES y la otra de DESPUÉS de un cambio "
       "inventado (un barrio antes y después del parque).",
       "Cada uno lee su tarjeta y busca en la otra fila la que le hace pareja.",
       "Cada pareja dice qué cambió y qué no.",
       "El docente pregunta: ¿qué causó el cambio?"],
      "Poner dos cosas frente a frente y decir qué las separa. Es el movimiento de las tarjetas 4 y 6 y de "
      "la cuarta del entrenamiento (antes y después del espejo).",
      "Diez tarjetas")],
 6: [("La línea de tiempo humana", 8,
      ["Cinco estudiantes al frente con una tarjeta de un relato inventado: llegué al pueblo · llovía · "
       "conocí a mi mejor amigo · desde entonces somos amigos · hoy.",
       "El grupo los ordena en una línea, del más viejo al de hoy.",
       "El docente lee una oración con hueco de ese relato («Since then, we ___ friends») y el que tiene "
       "esa tarjeta da un paso al frente.",
       "Desde su lugar en la línea, el grupo dice el tiempo del verbo y por qué."],
      "Ubicar cada acción en la línea de tiempo antes de escoger el verbo. Es el movimiento de las tarjetas "
      "1, 5 y 8 y de la primera del entrenamiento (At the time… found).",
      "Cinco tarjetas"),
     ("El jefe de al lado", 3,
      ["Unos tienen un jefe: HAVE, TO, CAN, WAS, SHE. Otros, una forma de un verbo: taken, take, taking, "
       "takes.",
       "El docente dice un jefe y los verbos que le sirven se paran junto a él.",
       "El grupo dice la regla en voz alta: «have pide la tercera forma».",
       "Se repite con otro verbo (write, written, writing, writes)."],
      "Mirar la palabra que va justo antes del espacio: ella manda la forma. Es el movimiento de las "
      "tarjetas 6 y 13 y de la segunda del entrenamiento (have said).",
      "Doce tarjetas"),
     ("Parejas de baile", 3,
      ["La mitad tiene un verbo (make, do, take, pay, catch, keep) y la otra un complemento (a mistake, "
       "homework, a photo, attention, a cold, a secret).",
       "A la señal, cada verbo busca su pareja de baile.",
       "Cada pareja dice una oración: «Pay attention, please».",
       "Las parejas raras («do a photo») se deshacen y el grupo las arregla."],
      "Reconocer las palabras que andan juntas en inglés. Es el movimiento de las tarjetas 9, 12 y 16 y de "
      "la tercera del entrenamiento (popular among).",
      "Doce tarjetas"),
     ("El jurado del párrafo", 3,
      ["El docente lee un párrafo inventado de cuatro oraciones con un hueco en la última.",
       "La pista que decide está en la primera oración, lejos del hueco.",
       "Los equipos buscan la oración que decide y la leen en voz alta.",
       "El jurado (tres estudiantes) dice si la pista está bien buscada antes de dar la palabra."],
      "Cuando la oración sola no alcanza, buscar la pista en el párrafo entero. Es el movimiento de las "
      "tarjetas 2 y 14 y de la cuarta del entrenamiento (So, it is not surprising).",
      "Ninguno")],
}

# Los retos del corte. Cuando quedan muchas tarjetas, el reto se hace con tarjetas del libro en relevo:
# el cuaderno de cada uno es el registro individual.
RETOS = {
 1: ("El banco compartido", 20,
     "Equipos de tres con el grupo School Life del libro (tarjetas 8 a 14). En siete minutos cada integrante "
     "llena dos o tres tarjetas en su cuaderno, con la palabra escrita antes de la letra, y tacha en el banco "
     "la palabra que usó. En los siete siguientes, cada dueño lee su descripción y la pista que decide; los "
     "otros dos llenan esa tarjeta en su propio cuaderno y tachan la palabra en su banco. Tres minutos de "
     "defensa por equipo y, al final, las claves. El banco tiene ocho palabras y siete descripciones: el "
     "equipo dice cuál sobró y por qué."),
 2: ("La respuesta que faltaba", 20,
     "Equipos de tres con seis frases que no están en el libro: «Can you lend me your pen for a minute?», "
     "«Would you like some help with that box?», «Is the library open on Saturdays?», «Did you finish the "
     "history homework?», «I think this movie is too long», «My brother broke his arm playing football». "
     "Cada integrante toma dos y escribe en su hoja qué clase de frase es, qué quiere quien habla, en qué "
     "tiempo está y la respuesta natural; además escribe una respuesta trampa que repita una palabra y no "
     "conteste. El equipo lee las seis en voz alta y los otros equipos adivinan cuál es la trampa."),
 3: ("El texto con trampas", 20,
     "Equipos de tres con el texto 4 del libro, «Public Protest and Social Change» (tarjetas 31 a 40, menos "
     "la 36 y la 38, que ya se hicieron en clase). Cinco minutos para leer el texto entero. Cada integrante "
     "se hace dueño de dos o tres espacios y los llena en su cuaderno: tapa las opciones, dice qué pieza "
     "falta y escribe la pista vecina. En el relevo, cada dueño lee su pista y los otros llenan esa tarjeta "
     "en su cuaderno. Cuatro tarjetas tienen Corrección EDUCATE (32, 34, 35 y 39): el equipo decide cuál "
     "defiende y por qué. Tres minutos de defensa por equipo."),
 4: ("El relevo de los datos", 20,
     "Equipos de tres con las seis tarjetas que no se hicieron en clase (5, 6, 8, 10, 12 y 15). Cada "
     "integrante se hace dueño de dos y las llena en su cuaderno con la frase del texto que responde. En el "
     "relevo, cada dueño lee la pregunta, la palabra ancla y la frase del texto; los otros dos llenan esa "
     "tarjeta en su cuaderno. Para cada distractor el equipo dice si no está en el texto o si es verdad y "
     "no responde. Tres minutos de defensa por equipo."),
 5: ("La prueba en la mano", 20,
     "Equipos de tres con las seis tarjetas que no se hicieron en clase (2, 8, 10, 11, 14 y 16). Cada "
     "integrante se hace dueño de dos y las llena en su cuaderno: lo que se infiere y la frase del texto "
     "que lo prueba, copiada. En el relevo, cada dueño lee su frase y los otros dos llenan esa tarjeta en "
     "su cuaderno. Gana la defensa que señale la frase exacta; si una respuesta no se puede señalar en el "
     "texto, el equipo la tacha."),
 6: ("El misterio de Baker Street", 20,
     "Equipos de tres con el Bloque 3 del libro, «A Late Visitor» (tarjetas 17 a 24). Cinco minutos para "
     "leer el texto entero y marcar su reloj: ¿en qué tiempo va el relato? Cada integrante se hace dueño de "
     "dos o tres espacios y los llena en su cuaderno; en el relevo, los otros llenan esas tarjetas en el "
     "suyo. Tres tarjetas tienen Corrección EDUCATE (17, 20 y 23): el equipo escribe cómo diría la oración "
     "un hablante. Tres minutos de defensa por equipo."),
}


# ─────────────────────────────── hojas ───────────────────────────────
OUTP = OUT + "plan_ing_"


def _cajas_hilo(b, y):
    cajas = [("LIBRO", "tiene la pregunta", GRAY), ("CUADERNO", "tiene el andamiaje para resolverla", ING),
             ("PLANEADOR", "te dice qué hacer con los dos", "#1F4E8C"),
             ("GUÍA", "pone ese plan en pantalla", PIZARRA)]
    an = (CW - 3 * 26) / 4
    for i, (t, s_, c) in enumerate(cajas):
        x = M + i * (an + 26)
        b.append(rect(x, y, an, 140, "white", r=18, stroke=c, sw=2.4))
        b.append(rect(x + 14, y + 16, 5, 108, c, r=3))
        b.append(T(x + an / 2 + 10, y + 58, [t], 26, c, weight="700", anchor="middle", ls=1.4))
        for j, ln in enumerate(wrap_px(s_, 21, an - 56)):
            b.append(T(x + an / 2 + 10, y + 94 + j * 28, [" ".join(ln)], 21, GRAY, anchor="middle"))
        if i < 3:
            b.append(T(x + an + 13, y + 82, ["›"], 34, "#A8B0BC", weight="700", anchor="middle"))
    return y + 140


def h1():
    b = svg_open()
    p0, p1 = pags_mision(1)[0] - 1, pags_mision(6)[1]
    y = cabecera(b, "Inglés", "Planeador del área · las ocho clases",
                 derecha="8", dsub="clases de 120 min", campos=True)
    y = seccion(b, y, "Para qué existe este documento")
    y = parrafo_j(b, M, y,
        "La calidad de la clase no puede depender de qué profesor llegue ese sábado. Por eso el método de "
        "EDUCATE no vive en el profesor: vive en el cuaderno del estudiante. Este planeador no te pide hablar "
        "inglés como un nativo; te dice qué hacer con el libro y con el cuaderno en cada uno de los 120 "
        "minutos, y dónde termina lo fijo y empieza tu aporte.", CW, 26) + 24
    y = _cajas_hilo(b, y) + 30
    y = nota(b, M, y, CW,
        "Casi ninguna pregunta de Inglés se resuelve traduciendo palabra por palabra. Se resuelve buscando la "
        "pista que decide: el verbo de la descripción, quién habla y qué quiere, el marcador de tiempo, la "
        "palabra vecina del espacio, la frase del texto que lo prueba. Cada tarjeta del cuaderno tiene su "
        "instrumento para escribir esa pista. Un estudiante que acierta con el instrumento vacío no aprendió "
        "la subestrategia: adivinó.",
        ING, ING_BG, ING_LN, "El instrumento de pensamiento del área: la pista que decide", 25) + 28
    y = seccion(b, y, "El área en números")
    nc = sum(len(r["clase"]) for r in REPARTO.values())
    nr = sum(len(r["reto"]) for r in REPARTO.values())
    nk = sum(len(ns) for r in REPARTO.values() for ns, _, _ in r["casa"])
    cif = [(str(AREA_PAGS[1] - AREA_PAGS[0] + 1), "páginas del cuaderno\\ncon portada y simulacro", ING),
           ("127", "preguntas del libro,\\nuna tarjeta cada una", ING),
           (str(nc), "en clase,\\ndiez por misión", "#1F4E8C"), (str(nr), "en el reto\\ndel corte", MORADO),
           (str(nk), "para la casa,\\ncon ronda de claves", ORO), ("24", "preguntas tipo\\nSaber 11", ROJO)]
    an2 = (CW - 5 * 16) / 6
    for i, (v, l, c) in enumerate(cif):
        x = M + i * (an2 + 16)
        b.append(rect(x, y, an2, 140, "white", r=16, stroke=ING_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, 112, c, r=3))
        b.append(T(x + 36, y + 64, [v], 50, c, weight="700"))
        for j, ln in enumerate(l.split("\\n")):
            b.append(T(x + 36, y + 98 + j * 26, [ln], 19, GRAY))
    y += 140 + 30
    y = nota(b, M, y, CW,
        "El cuaderno trabaja todas las preguntas del libro, y con el reparto fijo de la clase no caben: la "
        "Misión 3 trae 40. Por eso cada misión tiene tres destinos, y la hoja de cada clase dice cuáles "
        "tarjetas van a cada uno. EN CLASE, diez tarjetas representativas, con las cuatro subestrategias y "
        "con los sellos. EN EL RETO DEL CORTE, un texto o un grupo completo del libro, en relevo por equipos: "
        "cada uno deja esas tarjetas llenas en su propio cuaderno. EN LA CASA, lo que queda, y se revisa con "
        "una ronda de claves de cinco minutos al comenzar la clase siguiente: cada uno marca con otro color "
        "lo que falló y escribe al lado la pista que no vio. La Misión 2 cabe entera en clase.",
        ORO, ORO_BG, ORO_LN, "Las preguntas que no caben en clase", 23) + 28
    y = nota(b, M, y, CW,
        "No necesitas hablar inglés con fluidez. La segunda hoja de cada clase trae los cuatro conceptos que "
        "tienes que poder explicar en dos minutos y cómo se pronuncian las palabras clave. Si un estudiante "
        "pregunta algo que no sabes, no inventes: «No lo sé; vamos a ver qué dice el texto». La regla del área "
        "es que la respuesta sale de una pista del texto, no de la memoria de nadie. Anótalo en tu registro y "
        "tráelo resuelto la próxima clase. Si un estudiante sabe más inglés que tú, úsalo: que lea en voz alta "
        "y que señale la pista. Si dudas cómo se pronuncia una palabra, pídele a alguien que la lea.",
        VERDE, VERDE_BG, VERDE_LN, "Si Inglés no es tu fuerte", 23) + 28
    y = seccion(b, y, "Lo que la coordinación revisa, sin haber entrado a la clase",
        "Tres cuadernos al azar. No se mira si la respuesta está buena: se mira si el instrumento está lleno.")
    rev = ["El instrumento está lleno en las diez tarjetas de clase y en las del reto, acertadas o no.",
           "Las tarjetas de la casa están llenas y marcadas con otro color en la ronda de claves.",
           "Las «Corrección EDUCATE» y los sellos «Alto» tienen escrito lo que pide la tarjeta.",
           "Las dos caritas de la clase están marcadas y la clase está anotada en la portada del área."]
    b.append(rect(M, y, CW, 34 + len(rev) * 50, "white", r=18, stroke=ING_LN, sw=2))
    b.append(rect(M + 14, y + 16, 5, 2 + len(rev) * 50, ING, r=3))
    yy = y + 34
    for r_ in rev:
        b.append(checkbox(M + 44, yy - 14, 13, ING))
        parrafo_j(b, M + 100, yy - 22, r_, CW - 150, 23, INK)
        yy += 50
    y = yy + 40
    y = seccion(b, y, "La ronda de claves, paso a paso · cinco minutos",
        "Abre las clases 2, 4, 5, 6 y 8, dentro de los 15 minutos de la activación. La guía de clase trae las "
        "claves de la tarea en una diapositiva, ocultas hasta que presiones «Revelar».")
    pasos = [("1", "Cuaderno abierto en la tarea y un color distinto del lápiz en la mano."),
             ("2", "Revelas las claves; cada uno pone una chulita o una X junto al «marco al final» de cada tarjeta."),
             ("3", "Junto a cada X escribe la pista que no vio: la palabra del texto que decidía."),
             ("4", "Manos arriba por tarjeta: la más fallada se explica en un minuto; las demás, a tu registro.")]
    an = (CW - 3 * 16) / 4
    alto = max(70 + len(wrap_px(t, 20, an - 70)) * 28 for _, t in pasos)
    for i, (k, t) in enumerate(pasos):
        x = M + i * (an + 16)
        b.append(rect(x, y, an, alto, ORO_BG, r=14, stroke=ORO_LN, sw=1.8))
        b.append(f'<circle cx="{x+40}" cy="{y+40}" r="20" fill="{ORO}"/>')
        b.append(T(x + 40, y + 48, [k], 22, "white", weight="700", anchor="middle"))
        parrafo_j(b, x + 30, y + 66, t, an - 60, 20, INK, lh=28)
    y += alto
    pie(b, 1)
    svg_close(b, OUTP + "01.svg")
    return y


def h2():
    b = svg_open()
    p0, p1 = pags_mision(1)[0] - 1, pags_mision(6)[1]
    y = cabecera(b, "Las ocho clases", "Mapa del área de un vistazo",
                 derecha=str(AREA_PAGS[1] - AREA_PAGS[0] + 1), dsub=f"páginas · {AREA_PAGS[0]} a {AREA_PAGS[1]}")
    y = seccion(b, y, "Qué se ve en cada sábado y adónde va cada tarjeta",
        "Seis clases de contenido, una por misión, y dos para el simulacro del área. Cada misión es una parte "
        "del examen. El número de clases es fijo: no se recorta aunque una misión tenga 40 preguntas.")
    colx = [M, M + 104, M + 560, M + 900, M + 1180, M + 1560]
    y = encabezado_tabla(b, y, list(zip(colx, ["CLASE", "QUÉ SE TRABAJA", "EN CLASE", "EN EL RETO",
                                                "PARA LA CASA · RONDA", "ENTRENAMIENTO"])), 54)
    y += 2
    for n, (mis, tit, sub) in enumerate(CLASES, 1):
        alto = 100
        bg = "white" if mis else ORO_BG
        ln = ING_LN if mis else ORO_LN
        c = ING if mis else ORO
        b.append(rect(M, y, CW, alto, bg, r=14, stroke=ln, sw=2))
        b.append(rect(M + 12, y + 12, 5, alto - 24, c, r=3))
        b.append(T(colx[0] + 50, y + 64, [str(n)], 42, c, weight="700", anchor="middle"))
        b.append(T(colx[1] + 20, y + 44, [tit], 24, INK, weight="700"))
        b.append(T(colx[1] + 20, y + 76, [sub], 20, GRAY, style="italic"))
        if mis:
            r = REPARTO[mis]
            b.append(T(colx[2] + 20, y + 46, ["10 tarjetas"], 22, "#1F4E8C", weight="700"))
            cl = nums(r["clase"])
            b.append(T(colx[2] + 20, y + 76, [cl if tw(cl, 18) < 300 else "ver la hoja de la clase"], 18, GRAY))
            if r["reto"]:
                b.append(T(colx[3] + 20, y + 46, [f"{len(r['reto'])} tarjetas"], 22, MORADO, weight="700"))
                b.append(T(colx[3] + 20, y + 76, [nums(r["reto"]) if tw(nums(r["reto"]), 18) < 250
                                                  else "texto 4, menos 36 y 38"], 18, GRAY))
            else:
                b.append(T(colx[3] + 20, y + 46, ["reto original"], 22, MORADO, weight="700"))
                b.append(T(colx[3] + 20, y + 76, ["seis frases nuevas"], 18, GRAY))
            if r["casa"]:
                tot = sum(len(ns) for ns, _, _ in r["casa"])
                rev = " · ".join(str(c_) for _, c_, _ in r["casa"])
                b.append(T(colx[4] + 20, y + 46, [f"{tot} tarjetas"], 22, ORO, weight="700"))
                b.append(T(colx[4] + 20, y + 76, [f"ronda en la clase {rev}" if len(r["casa"]) == 1
                                                  else f"un texto por semana · clases {rev}"], 18, GRAY))
            else:
                b.append(T(colx[4] + 20, y + 58, ["sin tarea"], 22, GRAY))
            i1, i2 = pags_icfes(mis)
            b.append(T(colx[5] + 20, y + 46, ["4 tipo Saber 11"], 22, ROJO, weight="700"))
            b.append(T(colx[5] + 20, y + 76, [f"páginas {i1} y {i2}"], 18, GRAY))
        else:
            ron = ronda_de(8)
            b.append(T(colx[2] + 20, y + 60, ["condiciones de examen" if n == 7 else "6 por estudiante"],
                       21, GRAY))
            b.append(T(colx[4] + 20, y + 60, ["—" if n == 7 else f"ronda: tarea de la Misión {ron[0][0]}"], 21, GRAY))
            b.append(T(colx[5] + 20, y + 60, ["no está en el cuaderno" if n == 7 else f"páginas {SIM}"],
                       21, GRAY))
        y += alto + 10
    y += 24
    y = seccion(b, y, "Las 24 subestrategias del área, misión por misión",
        "Cada parte del examen tiene su estrategia y cuatro subestrategias. Son el vocabulario que el estudiante "
        "se lleva: si al final puede nombrarlas y decir para qué sirve cada una, el área cumplió.")
    an = (CW - 2 * 18) / 3
    alto = 0
    for m in range(1, 7):
        lins = sum(len(wrap_px(e, 21, an - 132)) for e in MISIONES[m]["estr"])
        alto = max(alto, 128 + lins * 29 + 4 * 12)
    for m in range(1, 7):
        x = M + ((m - 1) % 3) * (an + 18)
        yy0 = y + ((m - 1) // 3) * (alto + 18)
        d = MISIONES[m]
        b.append(rect(x, yy0, an, alto, ING_BG, r=16, stroke=ING_LN, sw=2))
        b.append(rect(x + 14, yy0 + 14, 5, alto - 28, ING, r=3))
        b.append(T(x + 40, yy0 + 44, [f"Misión {m} · {d['parte']}"], 22, ING_T, weight="700"))
        b.append(T(x + 40, yy0 + 72, [f"«{d['tema']}»"], 19, INK, style="italic"))
        a_, z_ = pags_mision(m)
        b.append(T(x + 40, yy0 + 100, [f"páginas {a_} a {z_}"], 18, GRAY))
        yy = yy0 + 122
        for j, e in enumerate(d["estr"]):
            c = COLS_MIS[m][j]
            b.append(T(x + 40, yy + 21, [f"S{j+1}"], 18, c, weight="700"))
            yy = parrafo_j(b, x + 92, yy - 1, e, an - 132, 21, INK, lh=29) + 12
    pie(b, 2)
    svg_close(b, OUTP + "02.svg")
    return y + 2 * alto + 18


def hoja_momentos(parte):
    desde, hasta = (0, 3) if parte == 1 else (3, 6)
    b = svg_open()
    y = cabecera(b, "Los 120 minutos", f"Momentos {desde+1} a {hasta} de los seis de una clase",
                 derecha="120", dsub="minutos por clase")
    y = seccion(b, y, "Distribución del tiempo · 120 minutos",
        "El núcleo de cada momento es fijo. Tu aporte tiene su propio espacio al final de cada bloque: va "
        "además de lo de arriba, no en vez de lo de arriba." if parte == 1 else
        "Viene de la hoja anterior. La misma estructura en las seis clases de contenido del área.")
    y = barra_tiempo(b, y, FASES)
    for i in range(desde, hasta):
        y = bloque_momento(b, y, i + 1, FASES[i])
    pie(b, 2 + parte)
    svg_close(b, OUTP + f"{2 + parte:02d}.svg")


def _rot_sello(preg):
    return f"tarjeta {preg}" if isinstance(preg, int) else str(preg)


def _chips_claves(b, y, mis):
    """Todas las claves de la misión, en tabla compacta: una casilla por tarjeta, con el color de su
    destino (clase, reto, casa). Devuelve dónde termina."""
    n = TOTAL_PREG[mis]
    porfila = 12 if n > 12 else n
    gap = 10
    w = (CW - (porfila - 1) * gap) / porfila
    h = 48
    colores = {"clase": ("white", ING, INK), "reto": (MORADO_BG, MORADO, MORADO), "casa": (ORO_BG, ORO, "#7A4A0C")}
    for i in range(n):
        k = i + 1
        x = M + (i % porfila) * (w + gap)
        yy = y + (i // porfila) * (h + 8)
        bg, ln, tc = colores[destino(mis, k)]
        b.append(rect(x, yy, w, h, bg, r=10, stroke=ln, sw=2))
        b.append(T(x + 16, yy + 32, [str(k)], 21, GRAY, weight="700"))
        cl = CLAVES[mis][k]
        b.append(T(x + w - 18, yy + 33, [cl], 25, tc, weight="700", anchor="end"))
    y += ((n - 1) // porfila + 1) * (h + 8) + 4
    x = M
    for t, key in (("en clase", "clase"), ("en el reto", "reto"), ("para la casa", "casa")):
        if key != "clase" and not any(destino(mis, k) == key for k in range(1, n + 1)):
            continue
        bg, ln, tc = colores[key]
        b.append(rect(x, y + 4, 34, 26, bg, r=6, stroke=ln, sw=2))
        b.append(T(x + 46, y + 25, [t], 19, GRAY))
        x += 46 + tw(t, 19) + 40
    extra = {3: "«—» en la 32: ninguna opción sirve; se escribe «in»."}.get(mis)
    if extra:
        b.append(T(x, y + 25, [extra], 19, GRAY, style="italic"))
    return y + 40


def _alto_avisos(mis):
    h = 46 + 52                    # el título de la sección y su subtítulo
    for preg, sev, que, hacer in AVISOS.get(mis, []):
        h += max(58, 18 + len(wrap_px(que + "  →  " + hacer, 19, CW - 380)) * 26) + 5
    return h + 16


AVISOS_EN_B = set()                # las misiones cuyos avisos no caben en la primera hoja de la clase


def _avisos(b, y, mis):
    av = AVISOS.get(mis, [])
    y = seccion(b, y, "Lo que tienes que saber del libro antes de entrar",
        "Salió de resolver las preguntas una por una. «Corrección» es lo que el cuaderno ya corrige en la tarjeta.")
    for preg, sev, que, hacer in av:
        c, bg, ln = SEV_ING[sev]
        texto = que + "  →  " + hacer
        lin = wrap_px(texto, 19, CW - 380)
        h = max(58, 18 + len(lin) * 26)
        b.append(rect(M, y, CW, h, bg, r=12, stroke=ln, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, h - 20, c, r=2))
        b.append(T(M + 34, y + h / 2 - 4, [preg.upper()], 16, c, weight="700", ls=1))
        chip(b, M + 34, y + h / 2 + 5, sev.upper(), c, size=12, pad=9, fill="white", txtc=c)
        parrafo_j(b, M + 340, y + (h - len(lin) * 26) / 2 - 5, texto, CW - 380, 19, INK, lh=26)
        y += h + 5
    y += 16
    return y


def hoja_clase(mis):
    d = MISIONES[mis]
    cols = COLS_MIS[mis]
    b = svg_open()
    l0, l1 = LIBRO[mis]
    a_, z_ = pags_mision(mis)
    y = cabecera(b, f"Clase {mis}", f"Misión {mis} · {d['parte']} · {d['comp']} · cuaderno {a_} a {z_} · "
                 f"libro {l0} a {l1}", derecha=f"{mis}", dsub="de 8 clases")
    y = seccion(b, y, f"La estrategia de {'las' if 'Partes' in d['parte'] else 'la'} {d['parte'].lower()}: «{d['tema']}»",
        "Sus cuatro pasos: " + " · ".join(f"{i+1} {p}" for i, p in enumerate(d["pasos"])) + ". Las cuatro "
        "subestrategias salen rotuladas en cada tarjeta, con este mismo color: nómbralas igual en voz alta.")
    an = (CW - 3 * 16) / 4
    r = REPARTO[mis]
    por = {e: [p for p, ee, _, _ in TALLER_TODO[mis] if ee == e] for e in d["estr"]}
    alt = max(84 + len(wrap_px(e, 23, an - 60, "700")) * 32 for e in d["estr"])
    for i, e in enumerate(d["estr"]):
        x = M + i * (an + 16)
        b.append(rect(x, y, an, alt, "white", r=16, stroke=ING_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt - 28, cols[i], r=3))
        b.append(T(x + 38, y + 40, [f"SUBESTRATEGIA {i+1}"], 16, cols[i], weight="700", ls=1.3))
        parrafo_j(b, x + 38, y + 50, e, an - 60, 23, INK, weight="700", lh=32)
        en_clase = [p for p in por[e] if p in r["clase"]]
        txt = f"{len(por[e])} tarjetas · en clase: {nums(en_clase)}"
        b.append(T(x + 38, y + alt - 22, [txt if tw(txt, 18) < an - 60 else f"{len(por[e])} tarjetas · "
                                          f"{len(en_clase)} en clase"], 18, GRAY))
    y += alt + 24
    y = nota(b, M, y, CW, d["instala"], ORO, ORO_BG, ORO_LN, "Lo que tienes que instalar antes del taller", 23) + 22
    ss = sellos_de(mis)
    if ss:
        y = seccion(b, y, f"{'El sello' if len(ss) == 1 else f'Los {len(ss)} sellos'} de esta clase",
            "En estas tarjetas el cuaderno le dice al estudiante «alto, aquí entra el profe». El concepto está "
            "explicado en la guía de clase; la del entrenamiento se explica al socializar.")
        for s in ss:
            _, _, pag, preg, saber, _, _ = s
            lin = wrap_px(saber, 21, CW - 330)
            h = max(56, 20 + len(lin) * 29)
            b.append(rect(M, y, CW, h, ORO_BG, r=12, stroke=ORO_LN, sw=1.8))
            b.append(rect(M + 10, y + 10, 4, h - 20, ORO, r=2))
            b.append(T(M + 36, y + h / 2 + 8, [f"pág. {pag} · {_rot_sello(preg)}"], 20, ORO, weight="700"))
            parrafo_j(b, M + 290, y + (h - len(lin) * 29) / 2 - 4, saber, CW - 330, 21, INK, lh=29)
            y += h + 6
        y += 16
    y = seccion(b, y, "Las diez tarjetas de clase, su instrumento y su clave",
        f"Van en el desarrollo guiado, en cinco bloques de dos: "
        f"{' · '.join(f'{a} y {b_}' for a, b_ in zip(r['clase'][::2], r['clase'][1::2]))}. La primera es la "
        "pregunta modelo del momento 2.")
    cx = [M, M + 80, M + 230, M + 560, M + 1230, W - M - 100]
    y = encabezado_tabla(b, y, list(zip(cx, ["N.º", "PÁGINAS", "SUBESTRATEGIA", "INSTRUMENTO DE PENSAMIENTO",
                                              "EN EL LIBRO", "CLAVE"])), 46)
    for p, est, ins, ctx in TALLER[mis]:
        i_est = d["estr"].index(est)
        c = cols[i_est]
        l_ins = wrap_px(ins, 20, 640)
        ctx_ = f"{libro_num(mis, p)} · " + ctx.split(" · ")[-1] if mis in (3, 4, 5, 6) else ctx
        ctx_ = re.sub(r"Bloque \d, n\.º \d del libro · |B\d n\.º \d · ", "", ctx_)
        l_ctx = wrap_px(ctx_, 18, 480)
        l_est = wrap_px(est, 17, 280)
        h = max(54, 16 + max(len(l_ins) * 28, len(l_ctx) * 26), 20 + len(l_est) * 23 + 4)
        b.append(rect(M, y, CW, h, ING_BG if p == r["clase"][0] else "white", r=10, stroke=ING_LN, sw=1.6))
        b.append(rect(M + 9, y + 9, 4, h - 18, c, r=2))
        b.append(T(cx[0] + 44, y + h / 2 + 9, [str(p)], 24, c, weight="700", anchor="middle"))
        b.append(T(cx[1] + 6, y + h / 2 - 3, [f"cuad. {pag_tarjeta(mis, p)}"], 17, INK, weight="700"))
        b.append(T(cx[1] + 6, y + h / 2 + 19, [f"libro {pag_libro(mis, p)}"], 17, GRAY))
        b.append(T(cx[2] + 4, y + (h - len(l_est) * 23) / 2 + 17, [f"S{i_est+1}"], 17, c, weight="700"))
        for j, ln in enumerate(l_est):
            b.append(T(cx[2] + 42, y + (h - len(l_est) * 23) / 2 + 17 + j * 23, [" ".join(ln)], 17, GRAY))
        parrafo_j(b, cx[3] + 14, y + (h - len(l_ins) * 28) / 2 - 4, ins, 640, 20, INK, lh=28)
        parrafo_j(b, cx[4] + 14, y + (h - len(l_ctx) * 26) / 2 - 4, ctx_, 480, 18, GRAY, lh=26)
        b.append(rect(cx[5] + 18, y + h / 2 - 21, 60, 42, "white", r=10, stroke=c, sw=2))
        b.append(T(cx[5] + 48, y + h / 2 + 9, [CLAVES[mis][p]], 24, c, weight="700", anchor="middle"))
        y += h + 5
    y += 20
    y = seccion(b, y, f"Las claves de las {TOTAL_PREG[mis]} tarjetas de la misión",
        "Resueltas a mano contra el libro. El color dice adónde va cada tarjeta. Las de la casa se revelan en "
        "la ronda de claves de la clase siguiente, en la guía.")
    y = _chips_claves(b, y, mis) + 14
    if y + _alto_avisos(mis) <= TOPE:
        y = _avisos(b, y, mis)
    else:
        AVISOS_EN_B.add(mis)
    pie(b, 3 + mis * 2)
    svg_close(b, OUTP + f"{3 + mis * 2:02d}.svg")
    return y


def hoja_clase_b(mis):
    d = MISIONES[mis]
    r = REPARTO[mis]
    b = svg_open()
    y = cabecera(b, f"Clase {mis} · minuto a minuto", "El sábado, lo que no cabe, lo que el libro trae y la evaluación",
                 derecha="120", dsub="minutos")
    i1, i2 = pags_icfes(mis)
    ins = {p: i for p, e, i, c in TALLER_TODO.get(mis, [])}
    din = DINAMICAS[mis]
    sel = [s[3] for s in sellos_de(mis) if isinstance(s[3], int)]
    caso, pista = ACTIVACION[mis]
    ronda = ronda_de(mis)
    corr = [a[0].replace("preg. ", "") for a in AVISOS[mis] if a[1] == "corrección"
            and any(int(x) in r["clase"] for x in re.findall(r"\d+", a[0]))]
    act = ""
    if ronda:
        m_, ns, rot_ = ronda[0]
        act = (f"Ronda de claves de la tarea de la Misión {m_} ({rot_}; tarjetas {nums(ns)}), 5'. Después, ")
    act += (f"{'frase' if ronda else 'Frase'} proyectada, sin contexto: «{caso}» ¿Qué palabra decide? Dinámica E1 «{din[0][0]}» "
            f"({din[0][1]}'). Pista para el final: {pista}.")
    pares = list(zip(r["clase"][::2], r["clase"][1::2]))
    bloques = "; ".join(f"{a} y {b_} (p. {pag_tarjeta(mis, a)}" +
                        (f" y {pag_tarjeta(mis, b_)})" if pag_tarjeta(mis, b_) != pag_tarjeta(mis, a) else ")")
                        for a, b_ in pares[1:])
    p1 = r["clase"][0]
    concreto = [
        act,
        f"Pregunta modelo: la tarjeta {p1} ({libro_num(mis, p1)}, libro página {pag_libro(mis, p1)}). Manos "
        f"alzadas antes de buscar la pista. La pregunta del momento: {PROBLEMATIZADORA[mis]} Al final se llena "
        f"con el grupo «{ins.get(p1, '—')}».",
        f"Bloques: {pares[0][0]} y {pares[0][1]} (el de la pregunta modelo, en pantalla); {bloques}. Unos cinco "
        f"minutos por bloque y, entre bloques, las dinámicas E2, E3 y E4 (3')."
        + (f" Sello «Alto» en {'la tarjeta' if len(sel) == 1 else 'las tarjetas'} {nums(sel)}." if sel else "")
        + (f" Corrección EDUCATE en {' y '.join(corr)}." if corr else ""),
        (f"Reto del corte «{RETOS[mis][0]}»: tarjetas {nums(r['reto'])} del libro, en relevo por equipos de tres "
         f"(páginas {rango([pag_tarjeta(mis, n) for n in r['reto']])}). Cada uno las deja llenas en su cuaderno."
         if r["reto"] else
         f"Reto del corte «{RETOS[mis][0]}»: seis frases nuevas; cada uno registra en su hoja."),
        f"Entrenamiento, páginas {i1} y {i2}. Cuatro preguntas tipo Saber 11, en silencio y con reloj."
        + (" Texto con erratas corregidas por EDUCATE; pendiente de decisión." if mis == 5 else ""),
        "Solo las falladas, con la pista que las resuelve. "
        + ((f"Tarea: tarjetas {nums(r['casa'][0][0])} (páginas "
            f"{rango([pag_tarjeta(mis, n) for n in r['casa'][0][0]])}); se revisan al comenzar la clase "
            f"{r['casa'][0][1]}." if len(r["casa"]) == 1 else
            "Tarea en tres entregas, un texto por semana: " +
            "; ".join(f"{nums(ns)} (clase {c_})" for ns, c_, _ in r["casa"]) + ".")
           if r["casa"] else "Esta misión no deja tarea.")
        + f" Vocabulario, «lo que me llevo», carita de salida y la clase {mis} en la portada del área.",
    ]
    y = seccion(b, y, "El sábado, minuto a minuto", "Las seis fases con el contenido de esta misión puesto encima.")
    reloj = 0
    for (nom, mins, c, *_), txt in zip(FASES, concreto):
        lin = wrap_px(txt, 20, CW - 420)
        h = max(68, 22 + len(lin) * 28)
        b.append(rect(M, y, CW, h, "white", r=14, stroke=ING_LN, sw=1.8))
        b.append(rect(M + 12, y + 12, 5, h - 24, c, r=3))
        b.append(T(M + 40, y + h / 2 - 2, [f"{reloj:02d}'–{reloj+mins:02d}'"], 22, c, weight="700"))
        b.append(T(M + 40, y + h / 2 + 26, [nom], 18, GRAY))
        parrafo_j(b, M + 380, y + (h - len(lin) * 28) / 2 - 5, txt, CW - 420, 20, INK, lh=28)
        reloj += mins
        y += h + 6
    y += 16
    if mis in AVISOS_EN_B:
        y = _avisos(b, y, mis)
    y = seccion(b, y, "Si Inglés no es tu fuerte",
        "Lo que tienes que poder explicar en dos minutos, y cómo se dicen las palabras clave (la sílaba fuerte "
        "lleva tilde). Si te preguntan algo que no sabes: «vamos a ver qué dice el texto».", color=VERDE)
    an = (CW - 18) / 2
    items = NO_ES_TU_FUERTE[mis]
    for fila in range(2):
        par = items[fila * 2: fila * 2 + 2]
        alto = max(62 + len(wrap_px(t, 19, an - 70)) * 26 for _, t in par) + 8
        for k, (tit, txt) in enumerate(par):
            x = M + k * (an + 18)
            b.append(rect(x, y, an, alto, VERDE_BG, r=14, stroke=VERDE_LN, sw=1.8))
            b.append(rect(x + 12, y + 12, 5, alto - 24, VERDE, r=3))
            b.append(T(x + 38, y + 38, [tit], 20, VERDE, weight="700"))
            parrafo_j(b, x + 38, y + 46, txt, an - 70, 19, INK, lh=26)
        y += alto + 10
    pr = PRONUNCIA[mis]
    pw = (CW - 3 * 12) / 4
    for i, (w_, p_) in enumerate(pr):
        x = M + (i % 4) * (pw + 12)
        yy = y + (i // 4) * 58
        b.append(rect(x, yy, pw, 50, "white", r=10, stroke=VERDE_LN, sw=1.6))
        b.append(T(x + 18, yy + 33, [w_], 20, INK, weight="700"))
        b.append(T(x + pw - 18, yy + 33, [p_], 20, VERDE, anchor="end"))
    y += ((len(pr) - 1) // 4 + 1) * 58 + 12
    banco = BANCO.get(mis, [])
    y = seccion(b, y, "Las cuatro preguntas de entrenamiento y su clave",
        "Membrete «Pregunta Saber 11», sin año. Claves verificadas resolviendo cada pregunta; el texto completo "
        "y por qué cae cada opción están en la guía de clase.")
    for k, (x4, est, ins_, ctx) in enumerate(INS_ICFES.get(mis, [])):
        fila = banco[k] if k < len(banco) else {}
        ctx_ = fila.get("contexto", "—").split(" · texto completo")[0]
        i_est = d["estr"].index(est)
        cc = COLS_MIS[mis][i_est]
        l_c = wrap_px(ctx_, 19, 640, "700")
        l_i = wrap_px(ins_, 18, 600, style="italic")
        h = max(56, 18 + max(len(l_c), len(l_i)) * 26)
        b.append(rect(M, y, CW, h, "white", r=12, stroke=ING_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, h - 20, cc, r=2))
        b.append(T(M + 34, y + h / 2 - 3, [f"P{x4}"], 20, cc, weight="700"))
        b.append(T(M + 34, y + h / 2 + 19, [f"pág. {i1 if x4 <= 2 else i2}"], 15, GRAY))
        b.append(T(M + 140, y + h / 2 + 8, [f"S{i_est+1}"], 18, cc, weight="700"))
        parrafo_j(b, M + 200, y + (h - len(l_c) * 26) / 2 - 4, ctx_, 640, 19, INK, weight="700", lh=26)
        parrafo_j(b, M + 880, y + (h - len(l_i) * 26) / 2 - 4, ins_, 600, 18, GRAY, style="italic", lh=26)
        cl = fila.get("clave", "").strip()
        b.append(rect(W - M - 96, y + h / 2 - 22, 64, 44, ING_BG, r=10, stroke=ING, sw=2))
        b.append(T(W - M - 64, y + h / 2 + 10, [cl or "—"], 26, ING_T, weight="700", anchor="middle"))
        y += h + 5
    y += 18
    y = seccion(b, y, "Después de la clase · tu registro",
                "Se llena el mismo sábado, antes de salir. Esto no lo ve el estudiante.")
    campos = [("¿Qué tarjeta hubo que explicar dos veces?", "y con qué ejemplo funcionó la segunda"),
              ("¿A quién hay que volver la próxima clase?", "nombres, no «algunos»"),
              ("¿Qué cuaderno quedó con el instrumento vacío?", "aunque haya acertado la respuesta"),
              ("¿Qué pregunta no supiste responder?", "tráela resuelta la próxima clase")]
    alto_reg = int(min(232, (2470 - y - 14) / 2))
    if alto_reg < 150:
        campos, alto_reg = [campos[0], campos[3]], int(min(232, 2470 - y - 4))
    if alto_reg < 150:
        raise SystemExit(f"Clase {mis}: el registro del docente queda de {alto_reg} px")
    registro_docente(b, y, alto=alto_reg, campos=campos)
    pie(b, 4 + mis * 2)
    svg_close(b, OUTP + f"{4 + mis * 2:02d}.svg")
    return y


def h17():
    """Clases 7 y 8 · el simulacro de EDUCATE y su socialización en el cuaderno (C7 y C8)."""
    b = svg_open()
    y = cabecera(b, "Clases 7 y 8", "El simulacro de EDUCATE y su socialización en el cuaderno",
                 derecha=str(C8["preguntas_cuaderno"]), dsub="preguntas caben en el cuaderno")
    y = PS.hoja(b, y, C7, C8, ING, ING_BG, ING_LN, seccion, nota)
    pie(b, 17)
    svg_close(b, OUTP + "17.svg")
    return y


def hoja_dinamicas(mis):
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Dinámicas · Misión {mis}",
                 "Movimiento con sentido: el cuerpo ensaya lo que después hará la mente",
                 derecha=f"{mis}", dsub="de 6 misiones")
    y = nota(b, M, y, CW,
        "La dinámica debe ser isomorfa a la subestrategia: lo que hace el cuerpo tiene que ser el mismo "
        "movimiento que después hará la mente frente al texto. Antes de usar una, responde: ¿qué paso de la "
        "subestrategia está ejercitando? Si no hay respuesta, es recreo, no clase. Las frases en inglés son "
        "inventadas para la clase: ninguna sale del libro.",
        ORO, ORO_BG, ORO_LN, "La regla para aprobar cualquier dinámica", 23) + 22
    for i, din in enumerate(DINAMICAS[mis]):
        y = bloque_dinamica(b, y, i, din, d["estr"][i], COLS_MIS[mis][i])
    y = bloque_reto(b, y + 4, mis, RETOS[mis])
    pie(b, 17 + mis)
    svg_close(b, OUTP + f"{17 + mis:02d}.svg")
    return y


def h24():
    b = svg_open()
    graves = [(m, a) for m in range(1, 7) for a in AVISOS.get(m, []) if a[1] not in ("atención",)]
    total = sum(len(v) for v in AVISOS.values())
    ncorr = sum(1 for m in AVISOS for a in AVISOS[m] if a[1] == "corrección")
    y = cabecera(b, "Cierre del área", "Las correcciones y los avisos del libro, juntos, y lo que hay que devolver",
                 derecha=str(total), dsub="avisos del libro")
    y = seccion(b, y, f"Los {len(graves)} avisos que tocan una clave, un dato o una tarjeta",
        f"Para repasarlos antes de empezar el área. {ncorr} son «Corrección EDUCATE»: el cuaderno ya corrige el "
        f"libro en la tarjeta, sin dar la clave. Los otros {total - len(graves)}, de «atención», están en la hoja "
        "de cada clase. Ninguno se le oculta al estudiante.")
    cx = [M, M + 330, M + 480]
    y = encabezado_tabla(b, y, list(zip(cx, ["DÓNDE", "SEVERIDAD", "QUÉ PASA"])), 46)
    for m, (preg, sev, que, hacer) in graves:
        c, bg, ln = SEV_ING[sev]
        lin = wrap_px(que, 18, CW - 520)
        h = max(46, 14 + len(lin) * 24)
        b.append(rect(M, y, CW, h, bg, r=10, stroke=ln, sw=1.6))
        b.append(rect(M + 9, y + 8, 4, h - 16, c, r=2))
        b.append(T(cx[0] + 30, y + h / 2 + 7, [f"M{m} · {preg}"], 18, INK, weight="700"))
        chip(b, cx[1] + 6, y + h / 2 - 13, sev.upper(), c, size=12, pad=10, fill="white", txtc=c)
        parrafo_j(b, cx[2] + 14, y + (h - len(lin) * 24) / 2 - 4, que, CW - 520, 18, INK, lh=24)
        y += h + 4
    y += 22
    y = seccion(b, y, "Qué tienes que devolver al terminar el área")
    dev = [("Los seis registros de clase", "con nombres, no «algunos»"),
           ("El conteo por familia de partes del simulacro", "el dato que decide el refuerzo"),
           ("Las preguntas que no supiste responder", "y cómo las resolviste: van al reporte"),
           ("Las correcciones que el grupo discutió", "M3 (32 a 39) y M6 (17 a 23): van a la editorial"),
           ("Los avisos nuevos que encuentres", "la lista se hizo resolviendo, y seguro falta alguno")]
    for t, s_ in dev:
        b.append(rect(M, y, CW, 64, "white", r=14, stroke=ING_LN, sw=2))
        b.append(rect(M + 14, y + 12, 5, 40, ORO, r=3))
        b.append(checkbox(M + 42, y + 19, 13, ING))
        b.append(T(M + 100, y + 41, [t], 23, INK, weight="700"))
        b.append(T(M + 860, y + 41, [s_], 21, GRAY))
        y += 72
    y += 20
    y = nota(b, M, y, CW,
        f"Las cuatro preguntas de entrenamiento de la Misión 5 (páginas {pags_icfes(5)[0]} y {pags_icfes(5)[1]}) traen erratas que EDUCATE "
        "corrigió a mano; la dirección está decidiendo si se cambian. Mientras tanto se usan como están en el "
        "cuaderno. La pronunciación aproximada de las hojas de clase y las frases en inglés de las dinámicas y "
        "de las activaciones las escribió EDUCATE para este planeador: si algo te suena raro, anótalo y "
        "devuélvelo con el registro.",
        ROJO, ROJO_BG, ROJO_LN, "Pendiente", 23)
    pie(b, 24)
    svg_close(b, OUTP + "24.svg")
    return y


TOPE = 2470          # donde empieza el pie (verifica_plan.py)


def build():
    """Dibuja las 24 hojas. Cada función devuelve hasta dónde llegó su contenido: verifica_plan.py no ve
    lo que empieza por debajo del pie (lo salta como si fuera el pie), así que aquí se mide aparte."""
    altos = {1: h1(), 2: h2()}
    hoja_momentos(1); hoja_momentos(2)
    for m in range(1, 7):
        altos[3 + 2 * m] = hoja_clase(m)
        altos[4 + 2 * m] = hoja_clase_b(m)
    altos[17] = h17()
    for m in range(1, 7):
        altos[17 + m] = hoja_dinamicas(m)
    altos[24] = h24()
    malas = {k: round(v) for k, v in altos.items() if v > TOPE}
    if malas:
        raise SystemExit(f"Se meten en el pie (hoja: hasta dónde llegan): {malas}")
    return [f"{OUTP}{i:02d}.svg" for i in range(1, TOTAL + 1)]


PDF = "/home/user/educate-saber11/entregables/EDUCATE_Planeador_Ingles.pdf"

if __name__ == "__main__":
    import sys
    import render
    malas = verificar()
    if malas:
        raise SystemExit("No cuadra:\n  " + "\n  ".join(malas))
    hojas = build()
    print(len(hojas), "hojas del planeador de Inglés")
    if "--pdf" in sys.argv:
        render.unir(hojas, PDF)
        n, sin = render.verifica(PDF, "PLANEADOR")
        print(f"{PDF}: {n} páginas · sin pie: {sin or 'ninguna'}")
