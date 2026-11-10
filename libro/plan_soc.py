#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLANEADOR DEL DOCENTE · SOCIALES Y CIUDADANAS · las ocho clases del área.

Mismo modelo aprobado en el piloto de Matemáticas y ya entregado en Lectura Crítica
(plan_lc.py): seis momentos de 15·20·35·20·20·10, «tu aporte» acotado en cada uno y un
banco de dinámicas isomorfas a las estrategias. Usa el motor de plan_piezas.py sin
cambiarlo.

Lo propio del área: donde Lectura Crítica tiene el texto marcado, Sociales tiene el MAPA
DE ACTORES de la portada del área (página 113 del cuaderno de 398): quién gana, quién pierde, quién decide. Y
tiene dos cosas que Lectura Crítica no tiene en esa medida: doce sellos «Alto · aquí entra
el profe» con conceptos que el estudiante no trae de casa (la Constituyente, el Estado
Social de Derecho, los mecanismos de participación…) y cinco preguntas del libro que tocan
la política colombiana viva, pendientes de la decisión de la Gerencia.

Para el agente de las guías (clase_viva_soc.py), con los mismos nombres de plan_lc.py:
    FASES  CLASES  BASE  MISIONES  AVISOS  TALLER  INS_ICFES  BANCO  SELLOS  DINAMICAS  RETOS
y, además, lo que en Lectura Crítica vivía dentro de clase_viva_lc.py o no existía:
    CLAVES            {misión: {pregunta: letra}}   claves del libro, resueltas a mano
    ACTIVACION        {misión: (caso corto, pista)}  el caso de los 15 minutos iniciales
    PROBLEMATIZADORA  {misión: pregunta del momento}  y PREGUNTA_AREA, la que gobierna el área
    SABERES           {(misión, pregunta): (título, qué es, pregunta que destraba)} · un sello
    NO_ES_TU_FUERTE   {misión: [(concepto, explicación)]}  «Si Sociales no es tu fuerte»
    COLS_MIS          {misión: [4 colores]}          los colores de estrategia del cuaderno
    COMP_EST          {misión: [4 competencias]}     PS · IP · PRS de cada estrategia
    LIBRO             {misión: (pág. desde, pág. hasta)} del libro del estudiante
TALLER ya sale sin nombres propios de la política colombiana (ver sin_nombres()).

Claves del libro de las misiones 1 y 2 (no tienen módulo): resueltas el 9 nov 2026 contra
«PRUEBA DE CAMPO MISIÓN 1 y 2» de fuente_libro/CIENCIAS SOCIALES, una por una:
    M1 · 1·A  2·D  3·B  4·B  5·A  6·C  7·C  8·A  9·B  10·C
    M2 · 1·A  2·C  3·D  4·B  5·A  6·B  7·D  8·C  9·A  10·D
Las de las misiones 3 a 6 se copian del docstring de soc3.py … soc6.py.
"""
import csv
from plan_piezas import *
import plan_piezas as PZ
import paginas as PG          # la numeración final del cuaderno (398 páginas, 10 nov): única fuente

SOC = "#C9821B"; SOC_BG = "#FDF5E7"; SOC_LN = "#E8CFA3"
TOTAL = 24
configurar(SOC, SOC_BG, SOC_LN, "Sociales y Ciudadanas", TOTAL)
AREA_CSV = "Sociales y Ciudadanas"

AZUL = "#242478"; VERDE_E = "#30843C"; ROJO_E = "#A82424"
# Los colores de las cuatro estrategias, tal como salen en los chips del cuaderno.
COLS_MIS = {1: [AZUL, VERDE_E, SOC, MORADO], 2: [AZUL, VERDE_E, SOC, MORADO],
            3: [AZUL, VERDE_E, ROJO_E, MORADO], 4: [AZUL, VERDE_E, ROJO_E, MORADO],
            5: [VERDE_E, AZUL, MORADO, ROJO_E], 6: [AZUL, ROJO_E, MORADO, VERDE_E]}
COLS_EST = COLS_MIS[1]          # el nombre de plan_lc, por si alguien lo busca

# ─────────────────────────── los seis momentos ───────────────────────────
# El reparto es el aprobado: 15 · 20 · 35 · 20 · 20 · 10 = 120. No se cambia.
FASES = [
    ("Activación", 15, SOC,
     "Que el estudiante arme un mapa de actores —quién gana, quién pierde, quién decide— sobre "
     "un caso corto, antes de ver cualquier opción y antes de opinar.",
     ["Proyecta o lee un caso de dos o tres renglones sin decir de dónde salió.",
      "Pide tres nombres, en voz alta o en el tablero: quién gana, quién pierde y quién decide.",
      "Ejecuta la dinámica de apertura según la estrategia del encuentro."],
     "No da su opinión sobre el caso ni deja que la clase arranque opinando. Si alguien dice "
     "«eso está mal», le devuelve la pregunta: «¿mal para quién?». El cuaderno sigue cerrado.",
     "Proyector o tablero con el caso corto. Todavía no se abre el cuaderno."),
    ("Pregunta problematizadora", 20, "#1F4E8C",
     "Que el estudiante compruebe que en Sociales la respuesta sale del caso y de la Constitución, "
     "no de su simpatía política, usando la pregunta modelo del libro.",
     ["Presenta la pregunta modelo del libro y la deja a la vista todo el momento.",
      "Pide respuestas a mano alzada ANTES de releer el caso, y las anota en el tablero.",
      "Hace la pregunta que gobierna el área: ¿quién dice eso en el caso, y desde dónde?",
      "Revela la clave solo al final y trabaja por qué cae cada una de las otras tres."],
     "Regla del momento: nadie justifica con «yo pienso que» ni con lo que vio en las noticias. "
     "Toda intervención nombra un actor del caso o un derecho, un artículo o un principio concreto.",
     "Libro abierto en la pregunta modelo. Cuaderno solo en «mi primera idea»."),
    ("Desarrollo guiado", 35, "#3B3BA6",
     "Que el estudiante escriba el instrumento —los actores, el derecho, las dimensiones o el "
     "antes y el después— antes de mirar las opciones, y deje por escrito de dónde lo sacó.",
     ["Entrega las hojas del momento y trabaja por bloques: 1-2, 3-4, 5-6, 7-8 y 9-10.",
      "Antes de que marquen, verifica que el instrumento tenga escritos los actores o las dimensiones.",
      "Entre bloques, introduce la dinámica de la estrategia que viene: seis minutos, no más.",
      "Cuando aparece un sello «Alto · aquí entra el profe», explica el concepto en dos minutos y sigue."],
     "No resume el caso ni da su lectura política. Si un estudiante se traba, le pregunta a quién "
     "le pasa algo en el caso; si el instrumento está vacío, lo devuelve al caso antes que a las "
     "opciones.",
     "Cuaderno, las cinco hojas de taller. Libro, en las preguntas 1 a 10."),
    ("Reto en equipo", 20, MORADO,
     "Que el estudiante defienda su análisis con el caso en la mano y acepte que otro equipo "
     "puede ver un actor o una dimensión que él no vio.",
     ["Arma equipos de tres y entrega el reto del corte de este momento.",
      "Exige que cada integrante llegue con su instrumento YA diligenciado individualmente.",
      "Da tres minutos de defensa por equipo: señalan el actor, el derecho o el renglón que los respalda.",
      "Cierra mostrando qué actor o qué dimensión quedó por fuera en cada propuesta."],
     "El equipo discute, pero cada uno escribe en SU tarjeta del reto. No se acepta una defensa "
     "que diga «es que así es»: se nombra quién, qué derecho o qué parte del caso.",
     "Cuaderno de cada estudiante y la tarjeta del reto del corte."),
    ("Evaluación individual", 20, ROJO,
     "Que el estudiante transfiera por sí solo la estrategia a preguntas tipo Saber 11, con "
     "casos que no trabajó en clase.",
     ["Entrega las dos hojas de entrenamiento ICFES del momento.",
      "Da el tiempo completo sin intervenir ni explicar conceptos.",
      "Registra quién llena el instrumento y quién va directo a las opciones."],
     "Este momento es silencioso y en filas individuales. Es el que produce el dato de "
     "seguimiento. Si un estudiante marca sin llenar el instrumento, se le anota, no se le corrige.",
     "Cuaderno, las dos hojas de entrenamiento ICFES. Reloj a la vista."),
    ("Cierre", 10, VERDE,
     "Que el estudiante nombre la estrategia que usó y se lleve un concepto del día —un derecho, "
     "un mecanismo o un principio— escrito en sus propias palabras.",
     ["Socializa solo las preguntas que el grupo falló, pidiendo el actor o el principio que las resuelve.",
      "Pide que lean en voz alta su salvavidas: lo mínimo que sí tenían claro.",
      "Cada uno escribe el concepto del día en la franja «Palabras que me frenaron» de su hoja."],
     "No dicta la definición. El concepto se escribe como el estudiante lo entendió; si quedó "
     "mal entendido, eso se ve en la hoja y se corrige la próxima clase.",
     "Cuaderno: «Palabras que me frenaron», «lo que me llevo», carita de salida y portada del área."),
]

# Páginas del cuaderno. Los módulos de misión siguen en la numeración vieja (mapa de 347); lo
# impreso va en la de 398 (portada, seis misiones y, al final, las hojas de simulacro).
# paginas.nueva() traduce: si la numeración cambia, basta volver a construir.
BASE_VIEJA = {1: 97, 2: 104, 3: 111, 4: 118, 5: 125, 6: 132}
BASE = {m: PG.nueva(b) for m, b in BASE_VIEJA.items()}
PORTADA = PG.nueva(96)
AREA_PAGS = PG.rango_area("soc")
SIMULACRO_PAGS = PG.paginas_simulacro("soc")
SIM = f"{SIMULACRO_PAGS[0]} a {SIMULACRO_PAGS[-1]}"


def _pags(m):
    return f"{BASE[m]} a {BASE[m] + 6}"


CLASES = [
    (1, "Momento 1 · Competencias ciudadanas", f"páginas {_pags(1)} del cuaderno"),
    (2, "Momento 2 · Competencias ciudadanas", f"páginas {_pags(2)} del cuaderno"),
    (3, "Momento 3 · Competencias ciudadanas", f"páginas {_pags(3)} del cuaderno"),
    (4, "Momento 4 · Historia y cultura", f"páginas {_pags(4)} del cuaderno"),
    (5, "Momento 5 · Espacio y ambiente", f"páginas {_pags(5)} del cuaderno"),
    (6, "Momento 6 · Ético-político · cierre del área", f"páginas {_pags(6)} del cuaderno"),
    (None, "Simulacro del área", "el simulacro que aplica EDUCATE, en condiciones de examen"),
    (None, "Socialización del simulacro", f"hojas de simulacro del cuaderno, páginas {SIM}"),
]

# Clases 7 y 8 (decisión de Nelson, 10 nov): el simulacro es una prueba que escoge EDUCATE y no está en
# el cuaderno; la clase 8 socializa sus preguntas en las hojas de simulacro. C7 y C8: plan_simulacro.py.
import plan_simulacro as PS
C7, C8 = PS.datos("soc", conteo="competencia (PS, IP, PRS)", dinamica=dict(
    nombre="La mesa de las voces", formato="en equipos de cuatro",
    pasos=["Equipos de cuatro con la segunda pregunta asignada. Antes de hablar, el equipo escribe la "
           "situación en el óvalo: quién, dónde, cuándo y qué está en juego.",
           "Cada integrante toma una opción (A, B, C o D) y la defiende un minuto como si fuera la correcta.",
           "Los otros tres solo pueden tumbarla con un concepto, una norma o un actor del caso, nunca con "
           "una opinión.",
           "Queda en pie la que nadie tumbó. Cada uno escribe en SU esquema la idea clave y tacha con razón "
           "las otras tres."],
    entrena="Leer la situación desde los actores y desde el principio que la decide antes de elegir. Son "
            "la situación, «la mesa de las voces» y la idea clave del esquema."))

LIBRO = {1: (336, 339), 2: (347, 349), 3: (358, 361), 4: (370, 374), 5: (383, 386), 6: (398, 402)}

# PS pensamiento social · IP interpretación y análisis de perspectivas · PRS pensamiento
# reflexivo y sistémico. Clasificación NUESTRA por estrategia, no la oficial del ICFES.
COMP_NOM = {"PS": "Pensamiento social", "IP": "Interpretación y análisis de perspectivas",
            "PRS": "Pensamiento reflexivo y sistémico"}
COMP_EST = {1: ["IP", "PS", "PRS", "PS"], 2: ["IP", "PS", "PRS", "PS"],
            3: ["IP", "PRS", "PS", "PRS"], 4: ["PRS", "IP", "PRS", "PS"],
            5: ["PS", "IP", "PRS", "IP"], 6: ["PS", "PRS", "PRS", "IP"]}

MISIONES = {
 1: dict(comp="Competencias ciudadanas", pags=_pags(1),
   tema="Pensar socialmente: hechos, principios y contextos",
   competencia="PS · pensamiento social",
   estr=["Quién dice qué y por qué", "El principio que hay detrás",
         "Si pasa esto, qué pasa después", "Lo de antes explica lo de ahora"],
   instala="Que un hecho de la noticia se lee con tres preguntas: quién dice qué y por qué, qué "
           "principio de la Constitución está detrás y qué pasa después. Es el mapa de actores de "
           "la portada del área puesto a trabajar por primera vez.",
   ojo="⚠ Dos textos de esta misión nombran al presidente en ejercicio (preguntas 1 y 5). Se "
       "trabajan como lectura del argumento, no como opinión sobre el personaje. No agregues "
       "ejemplos ni casos con nombres de la política.",
   cierre="La estrategia 3 —si pasa esto, qué pasa después— no tiene pregunta Saber 11 en el "
          "entrenamiento: se entrena solo en el taller, en las preguntas 3, 6 y 9. Dale ahí el "
          "tiempo que el ICFES no le da."),
 2: dict(comp="Competencias ciudadanas", pags=_pags(2),
   tema="Contrastar posturas: en qué coinciden, en qué no",
   competencia="IP · análisis de perspectivas",
   estr=["En qué coinciden y en qué no", "El nombre exacto de la figura",
         "Las dos caras de la misma medida", "Qué queda en entredicho"],
   instala="Que dos actores pueden coincidir en lo que proponen y diferir en por qué lo proponen, "
           "o al revés. Separar la propuesta de la razón es la operación que más evalúa el ICFES "
           "en esta competencia.",
   ojo="La opción D de la pregunta 6 dice que la Conmoción Interior permite «suspender» los "
       "derechos humanos. Es falso: la Constitución dice limitar, no suspender, y la página "
       f"{PG.nueva(99)} "
       "del cuaderno enseña justo eso. Dilo en voz alta.",
   cierre="Los mecanismos de participación (pregunta 9 y la segunda del ICFES) se confunden entre "
          "sí. El criterio no es quién lo convoca sino qué se decide: un mandato, una ley o la "
          "Constitución."),
 3: dict(comp="Competencias ciudadanas", pags=_pags(3),
   tema="Lo que mueve una decisión: voces, derechos y efectos",
   competencia="PRS · pensamiento sistémico",
   estr=["Cada voz, su preocupación", "Quién gana y quién paga",
         "El derecho que se pone en tensión", "El efecto que llega a otra parte"],
   instala="Que una decisión pública tiene voces, deja ganadores y perdedores, toca un derecho y "
           "produce efectos que llegan lejos de donde se tomó. Las cuatro estrategias son cuatro "
           "preguntas al mismo caso.",
   ojo="⚠ El texto de las preguntas 1 a 3 gira alrededor de las honras fúnebres de un senador "
       "asesinado en 2025 y cita a una vendedora que dice «a mí no me importa». Es reciente y "
       "polarizante: el encuadre es el duelo institucional frente al sustento de los informales.",
   cierre="En las preguntas 1, 5, 7 y 10 la correcta es la única que dice «X pero también Y» y "
          "las otras traen una palabra absoluta. No enseñes ese truco: el instrumento pide escribir "
          "las dimensiones antes de mirar las opciones, y eso es lo que se evalúa."),
 4: dict(comp="Historia y cultura", pags=_pags(4),
   tema="Un hecho, muchas miradas: lo que el pasado le hizo a la gente",
   competencia="PRS e IP · dimensiones y miradas",
   estr=["Un hecho, varias dimensiones", "Quién lo mira y desde dónde",
         "Lo que el hecho le hizo a la gente", "De dónde viene y hasta dónde llega"],
   instala="Que un hecho histórico no tiene una sola versión ni una sola dimensión: se mira desde "
           "dónde lo vivió cada quien, qué le hizo a la gente, qué venía de antes y hasta dónde "
           "llegó.",
   ojo="El texto de Turbo (preguntas 4 a 7) dice que la violencia afectó «de manera especial a "
       "mujeres», pero la figura muestra más hombres que mujeres. Si un estudiante lo nota, tiene "
       "razón: es la ocasión para contrastar fuentes.",
   cierre="Coincidir en el tiempo no es causar. La pregunta 7 pide una motivación que el texto "
          "solo sugiere: el sello de esa pregunta es para explicar qué es el despojo de tierras "
          "antes de que el grupo elija."),
 5: dict(comp="Espacio y ambiente", pags=_pags(5),
   tema="El territorio no es neutro: lugar, gente y poder",
   competencia="PRS e IP · lugar, efectos y voces",
   estr=["El lugar explica el problema", "Ninguna voz se queda afuera",
         "Una medida, efectos en cadena", "Qué dice y qué busca quien habla"],
   instala="Que el lugar no es el escenario del problema sino parte de su causa: la orilla, la "
           "ladera, la frontera o la selva deciden quién llega, qué se disputa y qué efectos se "
           "encadenan.",
   ojo="La pregunta 2 presenta como hecho un cierre de la frontera con Venezuela en 2024 con "
       "sanciones comerciales, y no se encontró sustento. Para responder basta el texto, pero "
       "en Sociales hay que saber cuándo un texto es un caso hipotético.",
   cierre="Tres plantillas de enunciado se repiten tres veces cada una. Avisa al grupo que el "
          "enunciado se parece pero el caso cambia: el que responde por inercia, falla."),
 6: dict(comp="Ético-político", pags=_pags(6),
   tema="Lo que hace legítimo a un poder: la mayoría, los derechos y las cuentas",
   competencia="PS, IP y PRS · cierre del área",
   estr=["La mayoría y sus límites", "Eficaz no es lo mismo que legítimo",
         "Lo político, lo social y lo ético", "Quién lo dice y desde qué principio"],
   instala="Que un poder no es legítimo solo por tener la mayoría ni solo por dar resultados: lo "
           "limitan los derechos, la división de poderes y el pluralismo. Es la misión que recoge "
           "las cinco anteriores.",
   ojo="⚠ Las preguntas 8 a 10 tratan de un familiar del presidente investigado y de la condena "
       "de primera instancia a un expresidente. El cuaderno no imprime nombres. Habla siempre de "
       "«investigado» y «presunto», y no afirmes en clase en qué va cada proceso.",
   cierre="En las preguntas 7 y 10 gana la opción que nombra lo político, lo social y lo ético. "
          "Nombrar las tres palabras no basta: cada pedazo tiene que estar en el texto. Esa es la "
          "lección de cierre del área."),
}

# Claves del libro. M1 y M2 resueltas el 9 nov contra el libro; M3 a M6, de soc3…soc6.py.
CLAVES = {
 1: dict(zip(range(1, 11), "ADBBACCABC")),
 2: dict(zip(range(1, 11), "ACDBABDCAD")),
 3: dict(zip(range(1, 11), "ACDAAACDAC")),
 4: dict(zip(range(1, 11), "BABBDABBAA")),
 5: dict(zip(range(1, 11), "AABCBADBCD")),
 6: dict(zip(range(1, 11), "CCBBCBDBCD")),
}

# ─────────── lo que el libro trae y hay que saber antes de entrar (de hallazgos.csv) ───────────
AVISOS = {
 1: [("preg. 1 y 5", "alta",
      "Las dos nombran al presidente en ejercicio: la 1 por su propuesta de Constituyente (2024) y "
      "la 5 por una declaración de 1997 sobre los U'wa. Está en la decisión pendiente de la Gerencia.",
      "Se lee el argumento, no al personaje. Si el salón se va a opinar, devuélvelo al renglón."),
     ("preg. 4", "atención",
      "El enunciado ya nombra el concepto —discriminación positiva o acción afirmativa—: pregunta "
      "por su propósito, no por su nombre.",
      "Usa el sello: la igualdad real y no solo formal es lo que separa la B de la D."),
     ("ICFES", "atención",
      "El banco no trae una pregunta Saber 11 limpia de efectos sobre dimensiones: la estrategia 3 "
      "no aparece en el entrenamiento ICFES.",
      "Dale tiempo completo a las preguntas 3, 6 y 9 del taller.")],
 2: [("preg. 6", "media",
      "La opción D dice que la Conmoción Interior permite suspender los derechos humanos. La "
      "Constitución dice limitar, no suspender (art. 214).",
      f"No la dejes pasar como dato: el cuaderno la marca y la página {PG.nueva(99)} enseña lo contrario."),
     ("preg. 4 a 6", "atención",
      "El texto del Palacio de Justicia (1985) nombra al oficial que dirigió la retoma. No es un "
      "político, pero entra en la conversación pendiente sobre nombres propios.",
      "El encuadre es la tensión entre la frase y los hechos. No se juzga a la persona en clase."),
     ("preg. 7", "atención",
      "Un revisor externo anotó que «derechos de los animales» está mal planteado: la ley los "
      "reconoce como seres sintientes (Ley 1774 de 2016), no como titulares de derechos.",
      "Si un estudiante lo objeta, tiene razón. La clave D no cambia."),
     ("fuentes 2, 4, 5", "atención",
      "Tres URL de las fuentes del libro traen pegado «?utm_source=chatgpt.com».",
      "No las proyectes. No afecta la respuesta.")],
 3: [("texto 1 a 3", "alta",
      "Las honras fúnebres de un senador asesinado en 2025 y una vendedora que dice «a mí no me "
      "importa». Hecho reciente y polarizante, en la conversación pendiente con la Gerencia.",
      "Duelo institucional frente a sustento de los informales. No pidas opiniones sobre el crimen."),
     ("preg. 9", "media",
      "La opción B define la legalidad como el derecho de cada país a difundir sus opiniones: es "
      "falso. Además, el enunciado ya define el principio que pide.",
      "Aclara qué es legalidad para que el error no se quede como dato. El instrumento lo advierte."),
     ("preg. 1", "baja",
      "La clave A afirma que el homenaje fortaleció la memoria y la legitimidad institucional; el "
      "texto no lo dice.",
      "Es la mejor de las cuatro. Quien dude de esa mitad con el texto en la mano, leyó bien."),
     ("ICFES 3", "atención",
      "La pregunta Saber 11 trata de una niña wayú de 11 años, víctima de violación, que pide "
      "interrumpir el embarazo.",
      "Encuádralo como conflicto de principios. No pidas opiniones personales sobre el aborto."),
     ("reparto de claves", "media",
      "Cinco de las diez claves son A y ninguna es B.",
      "Reportado a la editorial. No lo digas en clase: el que lo oye deja de leer.")],
 4: [("texto 4 a 7", "media",
      "El texto dice que la violencia afectó «de manera especial a mujeres»; la figura muestra "
      "52,87 % hombres y 46,31 % mujeres.",
      "Que comparen texto y figura: eso es contrastar fuentes. Léeles las dos cifras."),
     ("preg. 7", "atención",
      "La clave B pide un dato que el texto no da: solo dice que el desplazamiento «coincidió» "
      "con el banano y las rutas.",
      "Usa el sello. Se responde por descarte, y coincidir no es causar: dilo."),
     ("preg. 10", "atención",
      "El texto dice que tras el 11-S se fortaleció la cooperación del Plan Colombia, que había "
      "empezado en 1999-2000.",
      "El cuaderno trae «Ojo con las fechas». Que nadie salga creyendo que nació del 11-S."),
     ("patrón de opciones", "media",
      "En seis preguntas las incorrectas cierran con «únicamente», «solo» o «aislado». La B es "
      "clave cinco veces y la C ninguna.",
      "No enseñes el truco. Exige el instrumento lleno antes de mirar las opciones.")],
 5: [("preg. 2", "media",
      "El texto da como hecho un cierre de la frontera con Venezuela en 2024 con sanciones "
      "comerciales. No se encontró sustento: la frontera se reabrió en 2022.",
      "Para responder basta el texto; trátalo como caso. El cuaderno manda a preguntarte."),
     ("preg. 6", "media",
      "La clave A dice que el Parque Nacional «afecta la movilidad»: la afectaría el asentamiento, "
      "y el texto nunca habla de movilidad.",
      "Se defiende por descarte. Si alguien lo nota, dale la razón y pide la menos mala."),
     ("preg. 8", "atención",
      "El caso nombra a una empresa real y le atribuye una práctica que amenaza el agua de La Calera.",
      "Decisión pendiente de la Gerencia. En clase di «la embotelladora»: no repitas la marca."),
     ("patrón de opciones", "media",
      "En seis preguntas la correcta es la única que nombra a todos los actores; las demás "
      "cierran con absolutos. Tres enunciados se repiten tres veces cada uno.",
      "Avisa que el enunciado se parece y el caso cambia. Instrumento antes de opciones.")],
 6: [("preg. 9 y 10", "alta",
      "El texto da por firme la condena de primera instancia a un expresidente (julio de 2025); "
      "según información pública, la segunda instancia la revocó en octubre de 2025.",
      "No afirmes en qué va el proceso. Se pregunta el principio, no el caso."),
     ("preg. 8 a 10", "alta",
      "El libro nombra a un familiar del presidente investigado y a un expresidente. El cuaderno "
      "no imprime los nombres.",
      "Di «investigado» y «presunto». Si la Gerencia decide no usarlas, se reemplazan."),
     ("preg. 6", "media",
      "Se defienden la B (división de poderes) y la C (pluralismo). La clave es B porque el texto "
      "habla de «contrapesos institucionales».",
      "Acepta la discusión. El sello explica los dos principios."),
     ("preg. 1 y 10", "media",
      "En la 1 la clave no concuerda del todo con la definición del texto; en la 10 la D gana por "
      "nombrar las tres dimensiones y la B sigue mejor el texto.",
      "Quien dude con el texto en la mano, leyó bien: reconócelo."),
     ("preg. 7", "media",
      "Las opciones A, B y C anuncian su propia falla («se concentra únicamente…»): se contesta "
      "sin leer el caso.",
      "Pide qué consecuencia del texto le falta a cada opción."),
     ("reparto de claves", "media",
      "La A no es clave ninguna vez (B 4, C 4, D 2).",
      "Reportado a la editorial. No lo digas en clase.")],
}

# ─────────── los doce sellos «Alto · aquí entra el profe» del cuaderno ───────────
# Mismo formato que la matriz de Lectura Crítica: área, misión, página, pregunta, saber,
# dónde, estado. Leídos de las páginas 96 a 138 del PDF entregado.
_S = [
 (1, 97, 1, "Qué fue la Asamblea Nacional Constituyente de 1991: por qué se convocó, qué crisis "
            "venía antes y qué cambió."),
 (1, 98, 4, "La acción afirmativa: tratar distinto a quien partió de atrás, para que la igualdad "
            "sea real y no solo formal."),
 (1, 100, 6, "Servicios ecosistémicos y autonomía territorial indígena: dos términos que el "
             "enunciado usa sin explicar."),
 (1, 101, 8, "Qué es una EPS y cómo funciona el sistema de salud: quién recauda, quién administra "
             "y quién atiende."),
 (2, 105, 3, "Qué es la Personería Municipal y en qué se diferencia de la Defensoría del Pueblo y "
             "de la Procuraduría."),
 (2, 105, 4, "Qué fue la toma y la retoma del Palacio de Justicia, el 6 y 7 de noviembre de 1985."),
 (2, 107, 6, "El Estado Social de Derecho: el Estado existe para garantizar derechos, y ni "
             "defendiéndose puede desconocerlos."),
 (2, 109, 9, "Los mecanismos de participación del artículo 103 y qué decide cada uno."),
 (3, 112, 3, "El mínimo vital: lo que la Corte Constitucional protege para que alguien viva hoy "
             "con dignidad."),
 (3, 116, 9, "Soberanía y no intervención frente a solución pacífica de controversias: dos "
             "principios de la Carta de la ONU."),
 (4, 122, 7, "Qué quiere decir cada motivación de un conflicto armado y qué es el despojo de "
             "tierras en la historia de Colombia."),
 (6, 135, 6, "División de poderes y pluralismo: los dos principios detrás de la palabra "
             "«contrapesos»."),
]
# _S trae la página vieja (leída del PDF entregado); SELLOS, la del cuaderno de 398.
SELLOS = [(AREA_CSV, m, PG.nueva(pag), preg, saber, "tarjeta de la pregunta", "En el cuaderno")
          for m, pag, preg, saber in _S]
TEXTOS = []        # Sociales no tiene textos para proyectar en el planeador: van en la guía

# Lo que el profe tiene que poder explicar en cada sello: título, qué es (sin jerga) y la
# pregunta que destraba. Mismo formato que SABERES de clase_viva_lc.py.
SABERES = {
 (1, 1): ("La Constituyente de 1991",
          "Una asamblea elegida por voto popular que reemplazó la Constitución de 1886. Se convocó "
          "en 1990, con el país en plena violencia y desconfianza en las instituciones; la empujó "
          "un movimiento estudiantil, la «séptima papeleta».",
          "¿Qué crisis había antes de 1991, y quién dice hoy que hay una parecida?"),
 (1, 4): ("Acción afirmativa",
          "El artículo 13 pide que la igualdad sea «real y efectiva»: el Estado puede favorecer a "
          "grupos discriminados o marginados. No es un privilegio: compensa un punto de partida "
          "desigual.",
          "¿Este grupo partió del mismo lugar que los demás?"),
 (1, 6): ("Servicios ecosistémicos y autonomía territorial",
          "Lo que un ecosistema le da a la gente sin cobrar: agua, suelo fértil, clima. La "
          "autonomía territorial indígena es el derecho de un pueblo a gobernar su territorio según "
          "sus usos, dentro de la Constitución.",
          "Si se protege ese territorio, ¿qué gana la comunidad y qué gana el país?"),
 (1, 8): ("Cómo funciona el sistema de salud",
          "Desde la Ley 100 de 1993, el Estado recauda y gira la plata (hoy la ADRES), las EPS "
          "afilian y administran, y las IPS —hospitales y clínicas— atienden. La reforma discute "
          "quién administra esa plata.",
          "¿Quién manejaría la plata con la reforma, y quién la maneja hoy?"),
 (2, 3): ("Personería, Defensoría y Procuraduría",
          "La Procuraduría vigila la conducta de los servidores públicos; la Defensoría del Pueblo "
          "defiende los derechos humanos; la Personería hace las dos cosas en el municipio. Ninguna "
          "juzga: eso es de los jueces.",
          "¿Esta entidad juzga, vigila o defiende?"),
 (2, 4): ("El Palacio de Justicia, 1985",
          "El 6 de noviembre de 1985 el M-19 se tomó el Palacio y el Ejército lo retomó con una "
          "operación militar. Murieron cerca de cien personas, entre ellas magistrados, y hubo "
          "desaparecidos. En 2014 la Corte Interamericana condenó al Estado colombiano.",
          "¿Por qué una frase sobre defender la democracia se volvió polémica?"),
 (2, 6): ("Estado Social de Derecho",
          "Artículo 1: el poder se somete a la ley y existe para garantizar derechos. Ni en "
          "Conmoción Interior se pueden suspender los derechos humanos (art. 214): se pueden "
          "limitar, por un tiempo y con control.",
          "¿Puede el Estado quitar un derecho para defenderse?"),
 (2, 9): ("Mecanismos de participación",
          "Artículo 103: voto, plebiscito, referendo, consulta popular, cabildo abierto, iniciativa "
          "legislativa y revocatoria del mandato. La revocatoria saca a un alcalde o un gobernador "
          "antes de tiempo.",
          "¿Qué se decide aquí: un mandato, una ley o la Constitución?"),
 (3, 3): ("Mínimo vital",
          "La Corte Constitucional llama así a lo que una persona necesita hoy para vivir con "
          "dignidad: comer, pagar dónde dormir. No está escrito con ese nombre en la Constitución: "
          "la Corte lo sacó de la dignidad humana.",
          "¿Qué necesita esta persona hoy, no el año entrante?"),
 (3, 9): ("Soberanía y solución pacífica",
          "Soberanía y no intervención: cada Estado decide sus asuntos sin que otro lo obligue. "
          "Solución pacífica de controversias: los conflictos entre países se arreglan negociando. "
          "Las dos están en la Carta de la ONU.",
          "¿Este país está decidiendo lo suyo o presionando a otro?"),
 (4, 7): ("Motivaciones de un conflicto y despojo",
          "Ideológica es pelear por ideas; territorial o económica, por tierra, rutas o recursos. "
          "Despojo es cuando, además de expulsar a una familia, otro se queda con su tierra.",
          "¿Quién se quedó con la tierra cuando las familias se fueron?"),
 (6, 6): ("División de poderes y pluralismo",
          "División de poderes: ninguna rama manda sobre las otras y se controlan entre sí "
          "(art. 113). Pluralismo: caben las voces distintas, también las críticas (art. 1).",
          "¿Qué rama perdió poder, y qué voces se callaron?"),
}

# ─────────── «Si Sociales no es tu fuerte»: cuatro conceptos por clase ───────────
NO_ES_TU_FUERTE = {
 1: [("La Constitución de 1991",
      "Reemplazó la de 1886. Definió a Colombia como Estado social de derecho, democracia "
      "participativa y país pluriétnico, y creó la tutela. Para la pregunta 1 basta saber que se "
      "convocó por una crisis de las instituciones."),
     ("Acción afirmativa · art. 13",
      "La igualdad tiene que ser real, no solo de papel: el Estado puede dar más a quien partió "
      "de atrás. Una beca para colegios públicos no es un premio al mérito puro ni un regalo "
      "igual para todos."),
     ("El sistema de salud",
      "El Estado recauda y gira la plata (ADRES), las EPS afilian y administran, las IPS atienden. "
      "En la pregunta 8 la tensión es quién administra la plata, no si hay que atender."),
     ("Pueblos indígenas y territorio",
      "Los resguardos son de propiedad colectiva y no se venden (art. 63). Antes de explotar "
      "recursos en ellos hay que consultar a la comunidad: es la consulta previa.")],
 2: [("Mecanismos de participación · art. 103",
      "El referendo aprueba o deroga normas, también reformas a la Constitución. El plebiscito "
      "apoya o rechaza una decisión del presidente. La revocatoria retira a un alcalde o gobernador."),
     ("Personería, Defensoría y Procuraduría",
      "La Procuraduría vigila a los servidores públicos, la Defensoría defiende los derechos "
      "humanos y la Personería hace las dos cosas en el municipio. Ninguna de las tres juzga."),
     ("El Palacio de Justicia, 1985",
      "El M-19 se tomó el Palacio y el Ejército lo retomó. Murieron cerca de cien personas y hubo "
      "desaparecidos. La frase del texto choca con esos hechos: eso es lo que se pregunta."),
     ("Estado Social de Derecho · art. 1 y 214",
      "El Estado existe para garantizar derechos. En Conmoción Interior puede limitar algunos, "
      "por un tiempo; nunca suspender los derechos humanos.")],
 3: [("Mínimo vital",
      "Lo que alguien necesita hoy para vivir con dignidad. La Corte lo protege aunque la palabra "
      "no esté en la Constitución. Por eso un cierre que deja sin venta al informal toca un derecho."),
     ("Espacio público y trabajo informal",
      "La Constitución protege el espacio público (art. 82) y el trabajo (art. 25). Cuando una "
      "autoridad recupera una calle, la Corte ha pedido no dejar sin sustento a quien vive de ella."),
     ("Aranceles y principios de la ONU",
      "Un arancel es un impuesto a lo que se importa. Usarlo para presionar a otro país toca la "
      "soberanía y la solución pacífica de controversias, dos principios de la Carta de la ONU."),
     ("Autonomía indígena y niñez",
      "Los pueblos indígenas aplican su propia justicia dentro de la Constitución (art. 246); los "
      "derechos de los niños prevalecen (art. 44). Cuando chocan, no gana uno solo: se pondera.")],
 4: [("La Violencia y el Frente Nacional",
      "Hacia 1946-1958, guerra entre liberales y conservadores, sobre todo en el campo. El Frente "
      "Nacional (1958-1974) turnó el poder entre los dos y dejó por fuera a los demás: una raíz de "
      "las guerrillas de los 60."),
     ("El voto femenino",
      "Se aprobó en 1954 y las mujeres votaron por primera vez en el plebiscito del 1 de diciembre "
      "de 1957. Antes, la mitad del país no elegía ni podía ser elegida."),
     ("Desplazamiento y despojo",
      "Desplazado es quien huye de su tierra por la violencia (Ley 387 de 1997). Despojo es cuando "
      "otro se queda con esa tierra. Que dos cosas coincidan en el tiempo no prueba que una cause "
      "la otra."),
     ("El 11-S y el Plan Colombia",
      "El Plan Colombia empezó en 1999-2000, con apoyo de Estados Unidos contra el narcotráfico. "
      "Después del 11 de septiembre de 2001 ese apoyo se extendió a la lucha contra las guerrillas.")],
 5: [("Riesgo y pobreza",
      "Las laderas inestables y las orillas de los ríos son los suelos más baratos porque son los "
      "más peligrosos. Quien llega sin recursos termina ahí: el lugar es parte de la causa."),
     ("El Tapón del Darién",
      "Selva entre Colombia y Panamá donde la carretera Panamericana se interrumpe. Se volvió ruta "
      "de miles de migrantes hacia el norte, bajo control de grupos armados y redes de tráfico."),
     ("Los emberá en Bogotá",
      "Familias emberá desplazadas se asentaron durante meses en el Parque Nacional pidiendo "
      "garantías para volver. El caso cruza espacio público, desplazamiento y derechos de un "
      "pueblo indígena."),
     ("La encomienda colonial",
      "La Corona entregaba a un español un grupo de indígenas que le pagaban tributo, a cambio de "
      "protegerlos y evangelizarlos. En la práctica fue trabajo forzado; las audiencias intentaron "
      "limitarla.")],
 6: [("Estado de derecho y división de poderes",
      "Nadie, tampoco quien gobierna, está por encima de la ley. El poder se reparte en tres ramas "
      "que se controlan entre sí (art. 113); los órganos de control y la prensa libre completan "
      "los contrapesos."),
     ("La mayoría y sus límites",
      "La democracia decide por mayoría, pero la mayoría no puede quitarle los derechos a la "
      "minoría. Es la idea de Bobbio que trae el libro: las reglas del juego valen más que una "
      "votación."),
     ("Eficacia y legitimidad",
      "Eficaz es lo que logra su objetivo; legítimo es lo que se hace con respaldo en la ley y "
      "respetando derechos. Un gobierno puede bajar el crimen debilitando a jueces y prensa."),
     ("Presunción de inocencia y doble instancia",
      "Toda persona es inocente hasta que una condena quede en firme (art. 29). Una condena de "
      "primera instancia se apela y otra sala puede revocarla. En clase: «investigado», nunca "
      "«culpable».")],
}

PREGUNTA_AREA = "¿Quién dice eso en el caso, y desde dónde?"
PROBLEMATIZADORA = {
 1: "¿Qué principio de la Constitución está detrás de lo que pide la gente en este caso?",
 2: "¿En qué coinciden estos dos actores, y en qué no?",
 3: "¿Quién gana, quién paga y a quién más le llega esta decisión?",
 4: "¿Desde dónde mira el hecho cada quien, y qué le hizo a la gente?",
 5: "¿Qué tiene este lugar que explica el problema?",
 6: "¿Basta con que lo decida la mayoría, o basta con que funcione?",
}

# Un caso corto y ORIGINAL para la activación: dos o tres renglones, sin nombres propios,
# con un ganador, un perdedor y alguien que decide. La pista es para el final de los 15'.
ACTIVACION = {
 1: ("Desde el lunes, el bus del colegio ya no entra a la vereda: da la vuelta en la carretera "
     "principal. La rectoría dice que el camino está en mal estado.",
     "decide la rectoría, pierden los de la vereda, y lo que se toca es el acceso a la educación"),
 2: ("En la reunión de padres, unos piden prohibir el celular en el colegio y otros, permitirlo "
     "en el descanso. Los dos grupos dicen que lo hacen por el bien de los muchachos.",
     "coinciden en el fin, no en el medio"),
 3: ("La alcaldía cerró la plaza de mercado un mes para remodelarla. Los compradores celebran; "
     "los vendedores se fueron a vender a la calle.",
     "quién gana, quién paga, y el efecto que se fue a otra parte: la calle"),
 4: ("En 1970 llegó la carretera al pueblo. Los nietos de unos dicen que ese año empezó el "
     "progreso; los de otros, que ese año empezaron a irse los jóvenes.",
     "el mismo hecho, mirado desde dos lugares distintos"),
 5: ("Las casas más baratas del municipio están en la orilla del río. Cada invierno, el río crece.",
     "el lugar no es el fondo del problema: es parte de la causa"),
 6: ("Un gobierno logró bajar los robos a la mitad en un año. Para lograrlo, cerró el periódico que "
     "lo criticaba.",
     "funcionó, pero ¿con qué lo pagó?"),
}


# ─────────────────────── lo que ya está registrado ───────────────────────
NOMBRES = [("Petro y los U'wa (1997)", "Una declaración de 1997 sobre los U'wa"),
           ("El propio Petro ordena", "El propio autor ordena")]


def sin_nombres(t):
    """El cuaderno ya trae estos nombres; el planeador y la guía no los repiten (regla de
    políticos colombianos vivos, pendiente de la Gerencia)."""
    for a, b_ in NOMBRES:
        t = t.replace(a, b_)
    return t


def _instrumentos():
    from extrae_instrumentos import filas
    taller, icfes = {}, {}
    for a, mis, p, est, ins, ctx in filas():
        if a != AREA_CSV:
            continue
        d = icfes if "ICFES" in str(mis) else taller
        k = int(str(mis).split()[0])
        d.setdefault(k, []).append((int(p), est, sin_nombres(ins), sin_nombres(ctx)))
    for d in (taller, icfes):
        for k in d:
            d[k].sort()
    return taller, icfes


def _banco():
    """Las filas «SOC Mn» de icfes.csv, en el orden del cuaderno. El contexto se corta antes
    de « · cuadernillo»: la procedencia se queda en el tablero, no en el planeador."""
    with open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig") as f:
        r = list(csv.DictReader(f))
    out = {}
    for x in r:
        m = x["mision"].strip()
        if not m.startswith("SOC"):
            continue
        n = m.replace("SOC", "").replace("Misión", "").replace("M", "").strip()
        if n.isdigit():
            x = dict(x)
            x["contexto"] = x["contexto"].split(" · cuadernillo")[0].strip()
            out.setdefault(int(n), []).append(x)
    return out


TALLER, INS_ICFES = _instrumentos()
BANCO = _banco()


def limpia(t):
    """Carlito no trae el glifo ⚠ y el respaldo lo dibuja encima de la palabra siguiente.
    La alerta se marca con el color rojo de la tarjeta, no con el símbolo."""
    return t.replace("⚠ ", "").replace("⚠", "").strip()


def sellos_de(mis):
    return [s for s in SELLOS if str(s[1]) == str(mis)]


def comp_icfes(mis, k):
    """Competencia (PS, IP, PRS) de la pregunta ICFES k, por la estrategia que entrena."""
    est = INS_ICFES[mis][k - 1][1]
    i = MISIONES[mis]["estr"].index(est)
    return COMP_EST[mis][i]


# ─────────────────────────── banco de dinámicas ───────────────────────────
# Isomorfas a la estrategia: lo que hace el cuerpo es el mismo movimiento que después hará
# la mente frente al caso. En Sociales el movimiento casi siempre es UBICAR: poner a cada
# actor, efecto o derecho en su lugar. La E1 abre la clase (8'); las otras tres van entre
# bloques del desarrollo guiado y duran seis minutos.
DINAMICAS = {
 1: [("Tres sillas, tres razones", 8,
      ["Tres sillas al frente con un letrero cada una: VECINOS, ALCALDÍA y COMERCIANTES.",
       "El docente lee seis frases de un caso corto, sin decir quién dijo cada una.",
       "Un estudiante lleva cada frase a la silla de quien la dijo y la deja ahí.",
       "Para que se quede, otro dice el «porque» de ese actor con palabras del caso."],
      "Atribuir cada afirmación a su actor y a su razón antes de comparar. Es el movimiento de "
      "las preguntas 2, 5 y 8, y de la primera del ICFES (los motivos de la discriminación).",
      "Tres sillas · seis frases en tarjetas"),
     ("Del hecho al artículo", 6,
      ["Cinco carteles en la pared: IGUALDAD, PARTICIPACIÓN, DIGNIDAD, EXPRESIÓN y EDUCACIÓN.",
       "El docente lee un hecho corto del colegio o del barrio.",
       "Cada estudiante camina al cartel del principio que lo sostiene.",
       "Para quedarse, dice qué se está pidiendo en el hecho, no de qué tema es."],
      "Ir del hecho al principio por lo que se pide, no por el tema. Es el movimiento de las "
      "preguntas 4, 7 y 10, y de la segunda y la cuarta del ICFES.",
      "Cinco carteles · cinta"),
     ("Un pie en cada lado", 6,
      ["Una línea de cinta en el piso: a un lado SOCIAL y al otro ECONÓMICO.",
       "El docente anuncia una causa y lee efectos posibles, uno por uno.",
       "Si el efecto toca una dimensión, el estudiante se para en ese lado; si toca las dos, "
       "con un pie en cada lado.",
       "Solo cuenta si el efecto sale de la causa anunciada: el grupo lo comprueba en voz alta."],
      "Buscar el efecto que toca las dos dimensiones que pide el enunciado y que empieza en la "
      "causa dada. Es el movimiento de las preguntas 3, 6 y 9.",
      "Cinta en el piso"),
     ("Antes y ahora en el piso", 6,
      ["Una línea en el piso con dos marcas: HACE DIEZ AÑOS y HOY.",
       "Cada equipo recibe tarjetas con lo que se decía en cada momento para pedir un cambio en "
       "el colegio.",
       "Las ponen sobre su marca y unen con cinta las que usan el mismo argumento.",
       "Gana el equipo que dice en una frase qué argumento se repite."],
      "Comparar dos momentos por el argumento de cada uno, no por las fechas. Es el movimiento "
      "de la pregunta 1 y de la tercera del ICFES (los plebiscitos de 1886 y 1991).",
      "Cinta · tarjetas por equipo")],
 2: [("La cruz en el piso", 8,
      ["Una cruz de cinta en el piso: a lo ancho, QUÉ PROPONE; a lo largo, POR QUÉ.",
       "Cada estudiante recibe la tarjeta de un actor con su propuesta y su razón.",
       "Se para donde le corresponde en los dos ejes a la vez.",
       "El grupo lee: los de la misma columna coinciden en qué; los de la misma fila, en por qué."],
      "Separar lo que cada actor propone de por qué lo propone: se puede coincidir en una cosa y "
      "no en la otra. Es el movimiento de las preguntas 1, 4, 7 y 10, y de la primera del ICFES.",
      "Cinta · tarjetas de actores"),
     ("La ventanilla correcta", 6,
      ["Cinco pupitres son ventanillas: REVOCATORIA, REFERENDO, PLEBISCITO, CONSULTA y CABILDO.",
       "Cada equipo recibe una situación: qué se quiere decidir y quién lo pide.",
       "Va a la ventanilla que cree; quien la atiende lee en voz alta qué decide su mecanismo.",
       "Si no coincide con la situación, el equipo cambia de ventanilla."],
      "Elegir el nombre exacto de la figura por lo que se decide, no por quién la convoca. Es el "
      "movimiento de las preguntas 3 y 9, y de la segunda del ICFES.",
      "Cinco letreros · tarjetas de situaciones"),
     ("La moneda de dos caras", 6,
      ["Cada equipo recibe un círculo de cartón: una cara dice GANA y la otra CUESTA.",
       "El docente anuncia una medida: «se cierra el parque de noche».",
       "El equipo escribe un efecto en cada cara y al lado si pasa HOY o MAÑANA.",
       "Se voltean las monedas: ninguna puede tener una cara vacía."],
      "Ver que una medida no es solo buena o solo mala, y que el signo cambia con el tiempo. Es "
      "el movimiento de las preguntas 2 y 8, y de la tercera del ICFES.",
      "Un círculo de cartón por equipo"),
     ("La frase contra los hechos", 6,
      ["Se proyecta una frase oficial: «En este colegio todos participan en las decisiones».",
       "Cada equipo recibe cuatro tarjetas con hechos del año escolar.",
       "Pone cada hecho a un lado de la frase: CUADRA o NO CUADRA.",
       "Escribe qué deber queda en entredicho con los hechos que no cuadran."],
      "Poner un discurso encima de los hechos y nombrar lo que se rompe. Es el movimiento de las "
      "preguntas 5 y 6, y de la cuarta del ICFES (la reforma a la justicia de 2012).",
      "Proyector · cuatro tarjetas por equipo")],
 3: [("Media frase, dueño entero", 8,
      ["Se pegan en la pared tres actores de un caso corto que el docente lee.",
       "Cada equipo recibe una opción de respuesta cortada en dos mitades.",
       "Pega cada mitad bajo el actor que de verdad la dijo o la piensa en el caso.",
       "La mitad sin dueño en el caso se queda en la mesa: esa opción se cae."],
      "Partir cada opción en dos y comprobar de quién es cada mitad. Es el movimiento de las "
      "preguntas 2, 4 y 8, y de la primera del ICFES (el gerente y el voto).",
      "Tres letreros · opciones cortadas en dos"),
     ("La balanza humana", 6,
      ["Un lado del salón es GANA y el otro es PAGA.",
       "El docente lee una medida y reparte tarjetas con sus efectos.",
       "Cada estudiante camina con su tarjeta al lado que le toca y dice a quién afecta.",
       "Se cuenta al final: si un lado quedó vacío, el análisis está incompleto."],
      "Repartir los efectos de una decisión entre quien gana y quien paga; la conclusión completa "
      "tiene los dos platillos. Es el movimiento de las preguntas 1 y 7, y de la segunda del ICFES.",
      "Tarjetas con efectos"),
     ("¿A quién le tocaron este derecho?", 6,
      ["Cuatro estudiantes reciben un derecho: TRABAJO, EXPRESIÓN, SALUD y PARTICIPACIÓN.",
       "El docente narra un caso corto.",
       "Quien tiene un derecho se pone de pie solo si a alguien del caso le pasó algo con él.",
       "Para seguir de pie dice a quién y qué le pasó; si no puede, se sienta."],
      "Decidir que un derecho está en tensión porque a alguien concreto del caso le pasa algo con "
      "él. Es el movimiento de las preguntas 3, 6 y 9, y de la tercera del ICFES.",
      "Cuatro tarjetas de derechos"),
     ("Tres anillos", 6,
      ["Tres anillos de cuerda o cinta en el piso, uno dentro de otro.",
       "Un estudiante en el centro anuncia una medida: «sube el pasaje del bus».",
       "Otros entran a un anillo —cerca, lejos, muy lejos— con un efecto y a quién le llega.",
       "Para entrar al anillo de afuera, el efecto tiene que pasar por alguien del de adentro."],
      "Seguir un efecto más allá del blanco de la medida, eslabón por eslabón. Es el movimiento "
      "de las preguntas 5 y 10, y de la cuarta del ICFES (los consumidores que salen del barrio).",
      "Cuerda o cinta")],
 4: [("Cuatro lentes", 8,
      ["Cada estudiante recibe cuatro tarjetas de color: POLÍTICA, ECONOMÍA, SOCIEDAD y CULTURA.",
       "El docente narra un hecho histórico frase por frase.",
       "Después de cada frase, todos levantan la tarjeta de la dimensión que toca.",
       "Si hay dos colores arriba, quien levantó cada uno lee la palabra que lo hizo decidir."],
      "Descomponer un hecho en sus dimensiones antes de mirar opciones. Es el movimiento de las "
      "preguntas 3, 6 y 9, y de la segunda del ICFES (la canción y la dictadura).",
      "Cuatro tarjetas de color por estudiante"),
     ("Cada uno ve una cara", 6,
      ["Una caja en el centro del salón con un dibujo distinto en cada lado.",
       "Cuatro estudiantes, cada uno en un punto, describen solo lo que ven desde allí.",
       "El grupo compara: las cuatro descripciones son ciertas y ninguna es completa.",
       "Se leen dos testimonios de un mismo hecho: ¿desde dónde habla cada uno?"],
      "Ver que una versión depende del lugar desde donde se vivió el hecho. Es el movimiento de "
      "las preguntas 2, 5 y 8, y de la tercera del ICFES (el mejor argumento del otro lado).",
      "Una caja dibujada · dos testimonios cortos"),
     ("Lo que no cabe en la maleta", 6,
      ["Cada equipo recibe una lista de doce cosas: la casa, el oficio, los vecinos, la tierra, "
       "el colegio, la tumba de los abuelos…",
       "Tiene un minuto para escoger las cinco que caben en una maleta para irse esa noche.",
       "Escribe en el tablero lo que se quedó.",
       "El grupo dice qué le hizo el desplazamiento a esa familia mirando solo lo que se quedó."],
      "Pasar del hecho a lo que le hizo a la gente: lo que se rompe al irse. Es el movimiento de "
      "las preguntas 1 y 4, y de la primera del ICFES (el oficio que no sirve en la ciudad).",
      "Lista por equipo · nadie cuenta su propia historia"),
     ("Antes, durante, después", 6,
      ["Tres zonas en el piso: ANTES, DURANTE y DESPUÉS.",
       "Cada estudiante recibe una tarjeta con un hecho de una década.",
       "Se para en la zona que le toca respecto al hecho central que dice el docente.",
       "El grupo revisa ANTES: lo que ya existía puede explicar; lo que solo coincidió, no siempre."],
      "Ordenar en el tiempo para separar la causa de lo que solo coincidió. Es el movimiento de "
      "las preguntas 7 y 10, y de la cuarta del ICFES (qué ya existía en los años 60).",
      "Tres zonas en el piso · tarjetas")],
 5: [("El mapa del salón", 8,
      ["El salón es un municipio: la puerta es el río, la ventana la ladera y el tablero el centro.",
       "Cada estudiante recibe un papel: familia que llega sin plata, comerciante, empresa…",
       "Cada uno se ubica donde podría vivir o trabajar con lo que tiene.",
       "El grupo mira quién quedó junto al río y en la ladera, y dice por qué ahí."],
      "Leer las características del lugar como parte de la causa del problema. Es el movimiento "
      "de las preguntas 3, 6 y 9, y de la primera del ICFES (pobreza y zonas de riesgo).",
      "Tres letreros: RÍO, LADERA, CENTRO"),
     ("La silla vacía", 6,
      ["Una mesa al frente con cuatro sillas.",
       "El docente lee un caso del territorio; quien se sienta es un actor y dice su postura con "
       "palabras del caso.",
       "Se deja una silla vacía: el grupo dice quién falta en la mesa.",
       "Una opción que olvida a un actor, o que le cambia la postura, se cae."],
      "Comprobar que el análisis incluye a todos los actores y que cada uno dice lo que de verdad "
      "dijo. Es el movimiento de las preguntas 1 y 10, y de la segunda del ICFES.",
      "Una mesa · cuatro sillas"),
     ("La cadena de hombros", 6,
      ["El primer estudiante dice una medida: «se prohíbe la pesca en la ciénaga».",
       "El segundo le pone la mano en el hombro y dice un efecto de ese efecto, con su dimensión.",
       "Así hasta cinco eslabones.",
       "El grupo revisa cada eslabón: ¿alguno resolvió algo, o todos agravaron algo?"],
      "Encadenar efectos salto por salto y desconfiar de la opción que lo resuelve todo de una vez. "
      "Es el movimiento de las preguntas 2, 5 y 8, y de la tercera del ICFES.",
      "Ninguno"),
     ("Los cuatro rincones", 6,
      ["Cada rincón del salón es un actor: COMUNIDAD, EMPRESA, ALCALDÍA y AMBIENTALISTAS.",
       "El docente lee una palabra suelta: «progreso», «nuestro territorio», «invasores».",
       "Cada estudiante camina al rincón del actor que la diría.",
       "Para quedarse, dice qué busca ese actor cuando usa esa palabra."],
      "Separar lo que alguien dice de lo que busca al decirlo. Es el movimiento de las preguntas "
      "4 y 7, y de la cuarta del ICFES (el propósito de las medidas sobre la encomienda).",
      "Cuatro letreros")],
 6: [("La votación que no alcanza", 8,
      ["El docente propone cuatro decisiones para el salón: dos que la mayoría puede tomar y dos "
       "que tocan un derecho de alguien.",
       "Se vota cada una a mano alzada y se anota el resultado.",
       "Después de cada votación, el grupo decide si la mayoría PODÍA decidir eso.",
       "Las que tocan un derecho se tachan aunque hayan ganado."],
      "Separar lo que la mayoría puede decidir de lo que los derechos le ponen por límite. Es el "
      "movimiento de las preguntas 2, 3 y 4, y de la primera del ICFES (la MANE en 2011).",
      "Tablero"),
     ("Dos cajas: entrega y cobra", 6,
      ["Dos cajas al frente: LO QUE ENTREGA y LO QUE COBRA.",
       "El docente lee una medida de seguridad y reparte tarjetas con sus consecuencias.",
       "Cada estudiante echa su tarjeta en la caja que le toca y dice por qué.",
       "Se abren las cajas: una medida puede entregar mucho y cobrar lo que no se puede pagar."],
      "Evaluar por separado si una medida funciona y si es legítima. Es el movimiento de las "
      "preguntas 5 y 6, y de la tercera del ICFES (eficiencia y equidad).",
      "Dos cajas · tarjetas"),
     ("Tres carteles para un párrafo", 6,
      ["Tres carteles en la pared: POLÍTICO, SOCIAL y ÉTICO.",
       "Cada equipo recibe un párrafo corto impreso y lo recorta en frases.",
       "Pega cada frase bajo su cartel; la que no cabe en ninguno se queda en la mesa.",
       "Se revisa: ¿cada cartel tiene algo que de verdad está en el párrafo?"],
      "Clasificar cada afirmación por dimensión y comprobar que está en el texto: nombrar las tres "
      "palabras no basta. Es el movimiento de las preguntas 7 y 10, y de la cuarta del ICFES.",
      "Tres carteles · un párrafo y tijeras"),
     ("El banquillo del principio", 6,
      ["Tres estudiantes al frente con una tarjeta: LA MAYORÍA, LOS DERECHOS y EL EQUILIBRIO.",
       "El docente lee argumentos de un debate, uno por uno.",
       "El grupo dice de qué tarjeta sale cada argumento.",
       "El estudiante de esa tarjeta lo acepta o lo rechaza en voz alta, desde su principio."],
      "Ligar cada argumento con el principio desde el que se dice. Es el movimiento de las "
      "preguntas 1, 8 y 9, y de la segunda del ICFES (la Ley de Caducidad de Uruguay).",
      "Tres tarjetas grandes")],
}

RETOS = {
 1: ("El parque de la alcaldía", 20,
     "Cada equipo de tres trabaja el caso de la actividad de aula del libro: la alcaldía planea un "
     "parque; unos vecinos lo apoyan, otros temen perder parqueaderos y un grupo pide que se piense "
     "en niños y adultos mayores. En doce minutos arman el mapa de actores —quién gana, quién pierde, "
     "quién decide—, nombran el principio constitucional en juego y escriben un efecto en dos "
     "dimensiones. Exponen señalando el actor que respalda cada parte."),
 2: ("Dos ejes, cuatro voces", 20,
     "Cada equipo recibe un caso con cuatro actores: el colegio discute si el uniforme deja de ser "
     "obligatorio. Ubican a cada actor en dos ejes —qué propone y por qué— y escriben dos frases "
     "del tipo «X y Y coinciden en ___, pero no en ___». Después proponen un acuerdo que le deje "
     "algo a cada lado. Gana el equipo cuyo acuerdo nadie puede acusar de dejar a un actor sin nada."),
 3: ("El libro de cuentas de una decisión", 20,
     "Todos los equipos reciben el mismo caso: el municipio cierra la calle principal los domingos "
     "para una ciclovía. En doce minutos escriben las voces y su preocupación, quién gana y quién "
     "paga, el derecho que entra en tensión y un efecto que llega lejos de la calle. Cada integrante "
     "defiende una de las cuatro partes. Gana el efecto más lejano bien encadenado."),
 4: ("Dos testimonios, un mismo hecho", 20,
     "Cada equipo escribe dos testimonios de dos renglones sobre la llegada de la carretera a un "
     "pueblo en 1970: el de un comerciante del centro y el de una campesina de la vereda. Los pasa "
     "a otro equipo, que tiene que decir desde dónde habla cada uno, qué dimensiones toca el hecho y "
     "qué le hizo a la gente. Cada integrante cierra escribiendo el mejor argumento del testimonio "
     "con el que no está de acuerdo."),
 5: ("El barrio junto al río", 20,
     "Cada equipo dibuja en cinco minutos un barrio con un río, una ladera y un centro. El docente "
     "anuncia una medida: reubicar a las familias de la orilla. Ubican a los actores en el mapa, "
     "marcan qué rasgo del lugar explica el problema, encadenan tres efectos y escriben qué dice y "
     "qué busca uno de los actores. Exponen señalando en su propio mapa."),
 6: ("Tres filtros para una propuesta", 20,
     "El docente anuncia una propuesta: revisar maletas y celulares de todos al entrar, para acabar "
     "con los robos. Primero el salón vota. Después cada equipo la pasa por tres filtros: ¿la "
     "mayoría puede decidir esto?, ¿es eficaz y es legítima?, ¿qué pasa en lo político, lo social y "
     "lo ético? Cada integrante cierra con su frase: «Aunque la mayoría ___, la medida ___ porque ___»."),
}


# ─────────────────────────────── hojas ───────────────────────────────
OUTP = OUT + "plan_soc_"


def _cajas_hilo(b, y):
    cajas = [("LIBRO", "tiene la pregunta", GRAY), ("CUADERNO", "tiene el andamiaje para resolverla", SOC),
             ("PLANEADOR", "te dice qué hacer con los dos", "#1F4E8C"),
             ("GUÍA", "pone ese plan en pantalla", VERDE)]
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
    y = cabecera(b, "Sociales y Ciudadanas", "Planeador del área · las ocho clases",
                 derecha="8", dsub="clases de 120 min", campos=True)
    y = seccion(b, y, "Para qué existe este documento")
    y = parrafo_j(b, M, y,
        "La calidad de la clase no puede depender de qué profesor llegue ese sábado. Por eso el "
        "método de EDUCATE no vive en el profesor: vive en el cuaderno del estudiante. Este "
        "planeador no te pide saber historia de memoria; te dice qué hacer con el libro y con el "
        "cuaderno en cada uno de los 120 minutos, y dónde termina lo fijo y empieza tu aporte.",
        CW, 26) + 24
    y = _cajas_hilo(b, y) + 30
    y = nota(b, M, y, CW,
        "Casi ninguna pregunta de Sociales se resuelve recordando una fecha. Se resuelve "
        "preguntando quién gana, quién pierde y quién decide, y desde qué principio. Es el mapa de "
        "actores que el estudiante encuentra en la portada del área. Un estudiante que acierta con "
        "el instrumento vacío no aprendió la estrategia: adivinó, y en la prueba real no va a tener "
        "a quién preguntarle.",
        ORO, ORO_BG, ORO_LN, "El instrumento de pensamiento del área: el mapa de actores", 25) + 30
    y = seccion(b, y, "El área en números")
    na = sum(len(v) for v in AVISOS.values())
    cif = [(str(AREA_PAGS[1] - AREA_PAGS[0] + 1), "páginas del cuaderno\\ncon portada y simulacro", SOC), ("60", "preguntas del libro\\ncon su instrumento", SOC),
           ("24", "preguntas Saber 11\\npara entrenar", VERDE), (str(len(SELLOS)), "sellos «aquí entra\\nel profe»", ORO),
           (str(na), "avisos del libro\\nantes de entrar", ROJO)]
    an2 = (CW - 4 * 18) / 5
    for i, (v, l, c) in enumerate(cif):
        x = M + i * (an2 + 18)
        b.append(rect(x, y, an2, 140, "white", r=16, stroke=SOC_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, 112, c, r=3))
        b.append(T(x + 38, y + 64, [v], 50, c, weight="700"))
        for j, ln in enumerate(l.split("\\n")):
            b.append(T(x + 38, y + 98 + j * 26, [ln], 20, GRAY))
    y += 140 + 30
    y = seccion(b, y, "Las tres competencias que evalúa el ICFES en esta prueba")
    comp = [("PS", "Pensamiento social", "usar conceptos de las ciencias sociales y de la "
             "Constitución para entender un problema"),
            ("IP", "Interpretación de perspectivas", "reconocer quién dice qué, desde dónde y con "
             "qué intereses"),
            ("PRS", "Pensamiento reflexivo y sistémico", "ver las dimensiones de un problema y los "
             "efectos en cadena de una decisión")]
    an3 = (CW - 2 * 18) / 3
    alt3 = 52 + max(len(wrap_px(t + ": " + d, 22, an3 - 70)) for _, t, d in comp) * 31 + 20
    for i, (cod, t, d) in enumerate(comp):
        x = M + i * (an3 + 18)
        b.append(rect(x, y, an3, alt3, SOC_BG, r=16, stroke=SOC_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt3 - 28, SOC, r=3))
        b.append(T(x + 40, y + 44, [cod], 26, SOC, weight="700"))
        parrafo_j(b, x + 40, y + 54, t + ": " + d, an3 - 70, 22, INK, lh=31)
    y += alt3 + 30
    y = nota(b, M, y, CW,
        "Cinco preguntas del libro tocan la política colombiana viva: dos de la misión 1 nombran al "
        "presidente en ejercicio y tres de la misión 6 tratan de un familiar suyo investigado y de "
        "un expresidente condenado en primera instancia. La misión 3 abre con el homenaje a un "
        "senador asesinado en 2025. La decisión de la Gerencia está pendiente. Mientras tanto: no "
        "agregas casos con nombres propios, se lee el argumento y no al personaje, y si el salón se "
        "polariza, vuelves al renglón del texto.",
        ROJO, ROJO_BG, ROJO_LN, "Antes de empezar el área", 23) + 28
    y = nota(b, M, y, CW,
        "No necesitas ser de Sociales. La segunda hoja de cada clase trae los cuatro conceptos que "
        "tienes que poder explicar en dos minutos, y el cuaderno marca con un sello «Alto · aquí "
        "entra el profe» las doce preguntas donde el estudiante no puede seguir sin ti. Lo demás lo "
        "resuelve el mapa de actores: quién, qué derecho, qué efecto.",
        VERDE, VERDE_BG, VERDE_LN, "Si Sociales no es tu fuerte", 23) + 28
    y = seccion(b, y, "Lo que la coordinación revisa, sin haber entrado a la clase",
        "Tres cuadernos al azar del grupo. No se mira si la respuesta está buena: se mira si el "
        "instrumento está lleno. Marca tú mismo esta lista al terminar el sábado.")
    rev = ["El instrumento de pensamiento está lleno en las diez preguntas, acertadas o no.",
           "«Mi primera idea, antes de hacer nada» tiene algo escrito en todas las preguntas.",
           "Los sellos «Alto · aquí entra el profe» tienen escrito «lo que explicó, en mis palabras».",
           "Las dos caritas de la clase están marcadas y la clase está anotada en la portada del área."]
    b.append(rect(M, y, CW, 34 + len(rev) * 50, "white", r=18, stroke=SOC_LN, sw=2))
    b.append(rect(M + 14, y + 16, 5, 2 + len(rev) * 50, SOC, r=3))
    yy = y + 34
    for r_ in rev:
        b.append(checkbox(M + 44, yy - 14, 13, SOC))
        parrafo_j(b, M + 100, yy - 22, r_, CW - 150, 23, INK)
        yy += 50
    pie(b, 1)
    svg_close(b, OUTP + "01.svg")


def h2():
    b = svg_open()
    y = cabecera(b, "Las ocho clases", "Mapa del área de un vistazo",
                 derecha=str(AREA_PAGS[1] - AREA_PAGS[0] + 1), dsub=f"páginas · {AREA_PAGS[0]} a {AREA_PAGS[1]}")
    y = seccion(b, y, "Qué se ve en cada sábado",
        "Seis clases de contenido, una por momento, y dos para el simulacro del área. El número "
        "de clases es fijo: no se recorta aunque un momento quede largo.")
    colx = [M, M + 120, M + 700, M + 1110, M + 1450]
    y = encabezado_tabla(b, y, list(zip(colx, ["CLASE", "QUÉ SE TRABAJA", "ÉNFASIS",
                                                "PARA EL PROFE", "ENTRENAMIENTO ICFES"])), 54)
    y += 2
    for n, (mis, tit, sub) in enumerate(CLASES, 1):
        alto = 96
        bg = "white" if mis else ORO_BG
        ln = SOC_LN if mis else ORO_LN
        c = SOC if mis else ORO
        b.append(rect(M, y, CW, alto, bg, r=14, stroke=ln, sw=2))
        b.append(rect(M + 12, y + 12, 5, alto - 24, c, r=3))
        b.append(T(colx[0] + 44, y + 62, [str(n)], 42, c, weight="700", anchor="middle"))
        b.append(T(colx[1] + 20, y + 44, [tit], 24, INK, weight="700"))
        b.append(T(colx[1] + 20, y + 74, [sub], 20, GRAY, style="italic"))
        if mis:
            d = MISIONES[mis]
            cod, de = d["competencia"].split(" · ")
            b.append(T(colx[2] + 20, y + 44, [cod], 23, SOC, weight="700"))
            b.append(T(colx[2] + 20, y + 74, [de], 19, GRAY))
            ns, na = len(sellos_de(mis)), len(AVISOS.get(mis, []))
            tx = {0: "sin sellos", 1: "1 sello"}.get(ns, f"{ns} sellos")
            b.append(T(colx[3] + 20, y + 46, [f"{tx} · {na} avisos"], 22, INK, weight="700"))
            b.append(T(colx[3] + 20, y + 76, ["para preparar antes"], 19, GRAY))
            b.append(T(colx[4] + 20, y + 46, [f"{len(BANCO.get(mis, []))} preguntas Saber 11"],
                       22, VERDE, weight="700"))
            b.append(T(colx[4] + 20, y + 76, [f"páginas {BASE[mis]+2} y {BASE[mis]+6}"], 19, GRAY))
        else:
            b.append(T(colx[2] + 20, y + 58, ["PS · IP · PRS"], 23, GRAY))
            b.append(T(colx[3] + 20, y + 58, ["condiciones de examen" if n == 7 else "6 por estudiante"], 22, GRAY))
            b.append(T(colx[4] + 20, y + 58, ["no está en el cuaderno" if n == 7 else f"páginas {SIM}"], 22, GRAY))
        y += alto + 10
    y += 24
    y = seccion(b, y, "Las 24 estrategias del área, misión por misión",
        "Son el vocabulario que el estudiante se lleva. Si al final del área puede nombrarlas y decir "
        "para qué sirve cada una, el área cumplió, aunque falle preguntas.")
    an = (CW - 2 * 18) / 3
    alto = 0
    for m in range(1, 7):
        lins = sum(len(wrap_px(e, 21, an - 132)) for e in MISIONES[m]["estr"])
        alto = max(alto, 98 + lins * 29 + 4 * 12)
    for m in range(1, 7):
        x = M + ((m - 1) % 3) * (an + 18)
        yy0 = y + ((m - 1) // 3) * (alto + 18)
        d = MISIONES[m]
        b.append(rect(x, yy0, an, alto, SOC_BG, r=16, stroke=SOC_LN, sw=2))
        b.append(rect(x + 14, yy0 + 14, 5, alto - 28, SOC, r=3))
        b.append(T(x + 40, yy0 + 44, [f"Misión {m} · {d['comp']}"], 22, SOC, weight="700"))
        b.append(T(x + 40, yy0 + 72, [f"páginas {d['pags']}"], 19, GRAY, style="italic"))
        yy = yy0 + 92
        for j, e in enumerate(d["estr"]):
            c = COLS_MIS[m][j]
            b.append(T(x + 40, yy + 21, [f"E{j+1}"], 18, c, weight="700"))
            yy = parrafo_j(b, x + 92, yy - 1, e, an - 132, 21, INK, lh=29) + 12
    pie(b, 2)
    svg_close(b, OUTP + "02.svg")


def hoja_momentos(parte):
    desde, hasta = (0, 3) if parte == 1 else (3, 6)
    b = svg_open()
    y = cabecera(b, "Los 120 minutos", f"Momentos {desde+1} a {hasta} de los seis de una clase",
                 derecha="120", dsub="minutos por clase")
    y = seccion(b, y, "Distribución del tiempo · 120 minutos",
        "El núcleo de cada momento es fijo. Tu aporte tiene su propio espacio al final de cada "
        "bloque: va además de lo de arriba, no en vez de lo de arriba." if parte == 1 else
        "Viene de la hoja anterior. La misma estructura en las ocho clases del área.")
    y = barra_tiempo(b, y, FASES)
    for i in range(desde, hasta):
        y = bloque_momento(b, y, i + 1, FASES[i])
    pie(b, 2 + parte)
    svg_close(b, OUTP + f"{2 + parte:02d}.svg")


def _paginas(mis):
    base = BASE[mis]
    return [base, base + 1, base + 3, base + 4, base + 5], [base + 2, base + 6]


def hoja_clase(mis):
    d = MISIONES[mis]
    cols = COLS_MIS[mis]
    b = svg_open()
    l0, l1 = LIBRO[mis]
    y = cabecera(b, f"Clase {mis}", f"Momento {mis} · {d['comp']} · cuaderno {d['pags']} · "
                 f"libro {l0} a {l1}", derecha=f"{mis}", dsub="de 8 clases")
    y = seccion(b, y, "Las cuatro estrategias del momento",
        f"«{d['tema']}». El estudiante las ve rotuladas en cada pregunta de su cuaderno, con este "
        "mismo color: nómbralas igual en voz alta.")
    an = (CW - 3 * 16) / 4
    alt = max(52 + len(wrap_px(e, 23, an - 60)) * 32 for e in d["estr"])
    for i, e in enumerate(d["estr"]):
        x = M + i * (an + 16)
        b.append(rect(x, y, an, alt, "white", r=16, stroke=SOC_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt - 28, cols[i], r=3))
        b.append(T(x + 38, y + 40, [f"ESTRATEGIA {i+1} · {COMP_EST[mis][i]}"], 16, cols[i],
                   weight="700", ls=1.3))
        parrafo_j(b, x + 38, y + 50, e, an - 60, 23, INK, weight="700", lh=32)
    y += alt + 26
    y = nota(b, M, y, CW, d["instala"], ORO, ORO_BG, ORO_LN,
             "Lo que tienes que instalar antes del taller", 24) + 22
    # los sellos de esta misión
    ss = sellos_de(mis)
    if ss:
        y = seccion(b, y, f"{'El sello' if len(ss) == 1 else f'Los {len(ss)} sellos'} de esta clase",
            "En estas preguntas el cuaderno le dice al estudiante «alto, aquí entra el profe». El "
            "concepto está explicado en la hoja siguiente.")
        for s in ss:
            _, _, pag, preg, saber, _, _ = s
            lin = wrap_px(saber, 22, CW - 330)
            h = max(58, 22 + len(lin) * 30)
            b.append(rect(M, y, CW, h, ORO_BG, r=12, stroke=ORO_LN, sw=1.8))
            b.append(rect(M + 10, y + 10, 4, h - 20, ORO, r=2))
            b.append(T(M + 36, y + h / 2 + 8, [f"pág. {pag} · preg. {preg}"], 21, ORO, weight="700"))
            parrafo_j(b, M + 290, y + (h - len(lin) * 30) / 2 - 4, saber, CW - 330, 22, INK, lh=30)
            y += h + 6
        y += 18
    else:
        y = nota(b, M, y, CW,
            "Esta misión no tiene sellos «Alto · aquí entra el profe»: los conceptos que hacen falta "
            "están en la hoja siguiente, en «Si Sociales no es tu fuerte».",
            VERDE, VERDE_BG, VERDE_LN, "Sin sellos en esta clase", 22) + 24
    # las diez preguntas
    y = seccion(b, y, "Las diez preguntas del libro, su instrumento y su clave")
    cx = [M, M + 80, M + 210, M + 560, M + 1240, W - M - 100]
    y = encabezado_tabla(b, y, list(zip(cx, ["N.º", "PÁGINAS", "ESTRATEGIA", "INSTRUMENTO DE PENSAMIENTO",
                                              "CONTEXTO", "CLAVE"])), 46)
    t_pags, _ = _paginas(mis)
    claves = CLAVES[mis]
    for p, est, ins, ctx in TALLER.get(mis, []):
        i_est = d["estr"].index(est) if est in d["estr"] else 0
        c = cols[i_est]
        l_ins = wrap_px(ins, 20, 640)
        l_ctx = wrap_px(ctx, 19, 470)
        l_est = wrap_px(est, 18, 270)
        h = max(56, 18 + max(len(l_ins), len(l_ctx)) * 28, 22 + len(l_est) * 24 + 4)
        b.append(rect(M, y, CW, h, SOC_BG if p <= 2 else "white", r=10, stroke=SOC_LN, sw=1.6))
        b.append(rect(M + 9, y + 9, 4, h - 18, c, r=2))
        b.append(T(cx[0] + 44, y + h / 2 + 9, [str(p)], 24, c, weight="700", anchor="middle"))
        pc = t_pags[(p - 1) // 2]
        b.append(T(cx[1] + 6, y + h / 2 - 3, [f"cuad. {pc}"], 17, INK, weight="700"))
        b.append(T(cx[1] + 6, y + h / 2 + 19, [f"libro {_pag_libro(mis, p)}"], 17, GRAY))
        b.append(T(cx[2] + 4, y + (h - len(l_est) * 24) / 2 + 17, [f"E{i_est+1}"], 18, c, weight="700"))
        for j, ln in enumerate(l_est):
            b.append(T(cx[2] + 44, y + (h - len(l_est) * 24) / 2 + 17 + j * 24, [" ".join(ln)], 18, GRAY))
        parrafo_j(b, cx[3] + 14, y + (h - len(l_ins) * 28) / 2 - 4, ins, 640, 20, INK, lh=28)
        parrafo_j(b, cx[4] + 14, y + (h - len(l_ctx) * 28) / 2 - 4, ctx, 470, 19, GRAY, lh=28)
        b.append(rect(cx[5] + 18, y + h / 2 - 21, 60, 42, "white", r=10, stroke=c, sw=2))
        b.append(T(cx[5] + 48, y + h / 2 + 9, [claves[p]], 24, c, weight="700", anchor="middle"))
        y += h + 5
    y += 22
    av = AVISOS.get(mis, [])
    y = seccion(b, y, "Lo que tienes que saber del libro antes de entrar",
        "Salió de resolver las diez preguntas una por una. No se le esconde al estudiante.")
    for preg, sev, que, hacer in av:
        c, bg, ln = SEV[sev]
        texto = que + "  →  " + hacer
        lin = wrap_px(texto, 20, CW - 400)
        h = max(62, 20 + len(lin) * 28)
        b.append(rect(M, y, CW, h, bg, r=12, stroke=ln, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, h - 20, c, r=2))
        b.append(T(M + 36, y + h / 2 - 4, [preg.upper()], 17, c, weight="700", ls=1))
        chip(b, M + 36, y + h / 2 + 6, sev.upper(), c, size=13, pad=10, fill="white", txtc=c)
        parrafo_j(b, M + 360, y + (h - len(lin) * 28) / 2 - 5, texto, CW - 400, 20, INK, lh=28)
        y += h + 6
    pie(b, 3 + mis * 2)
    svg_close(b, OUTP + f"{3 + mis * 2:02d}.svg")


# Página del libro de cada pregunta, leída de «la lees en tu libro, página N» del cuaderno.
PAG_LIBRO = {
 1: [336, 337, 337, 337, 338, 338, 338, 338, 339, 339],
 2: [347, 347, 347, 348, 348, 348, 348, 349, 349, 349],
 3: [359, 359, 359, 359, 359, 360, 360, 361, 361, 361],
 4: [370, 371, 371, 372, 373, 373, 373, 373, 374, 374],
 5: [383, 383, 383, 384, 384, 385, 385, 385, 385, 386],
 6: [398, 399, 399, 399, 400, 400, 401, 401, 402, 402],
}


def _pag_libro(mis, p):
    return PAG_LIBRO[mis][p - 1]


def hoja_clase_b(mis):
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Clase {mis} · minuto a minuto", "El sábado, los conceptos y la evaluación",
                 derecha="120", dsub="minutos")
    t_pags, i_pags = _paginas(mis)
    ins = {p: i for p, e, i, c in TALLER.get(mis, [])}
    din = DINAMICAS[mis]
    sel = ", ".join(str(s[3]) for s in sellos_de(mis))
    caso, pista = ACTIVACION[mis]
    concreto = [
        f"Caso proyectado, sin contexto: «{caso}» Quién gana, quién pierde, quién decide. "
        f"Dinámica E1 «{din[0][0]}» ({din[0][1]}'). Pista para el cierre del momento: {pista}.",
        f"Pregunta modelo del libro, a la vista todo el momento. Manos alzadas antes de releer. "
        f"La pregunta del momento: {PROBLEMATIZADORA[mis]} Se abre la página {t_pags[0]} solo en "
        f"«mi primera idea».",
        f"1-2 en pantalla (página {t_pags[0]}, «{ins.get(1, '—')}» y «{ins.get(2, '—')}»); 3-4, 5-6, "
        f"7-8 y 9-10 en las páginas {t_pags[1]}, {t_pags[2]}, {t_pags[3]} y {t_pags[4]}. Entre "
        f"bloques, las dinámicas E2, E3 y E4."
        + (f" Sello en {'la pregunta' if ',' not in sel else 'las preguntas'} {sel}." if sel else ""),
        f"Reto del corte: «{RETOS[mis][0]}». Equipos de tres; cada uno registra en SU tarjeta. La "
        f"defensa nombra el actor, el derecho o el renglón.",
        f"Entrenamiento ICFES, páginas {i_pags[0]} y {i_pags[1]}. Cuatro preguntas Saber 11, en "
        f"silencio y con reloj.",
        f"Solo las falladas, con el actor o el principio que las resuelve. «Palabras que me "
        f"frenaron», «lo que me llevo», carita de salida y la clase {mis} en la portada del área.",
    ]
    y = seccion(b, y, "El sábado, minuto a minuto",
        "Las seis fases con el contenido de este momento puesto encima.")
    reloj = 0
    for (nom, mins, c, *_), txt in zip(FASES, concreto):
        lin = wrap_px(txt, 21, CW - 440)
        h = max(70, 24 + len(lin) * 29)
        b.append(rect(M, y, CW, h, "white", r=14, stroke=SOC_LN, sw=1.8))
        b.append(rect(M + 12, y + 12, 5, h - 24, c, r=3))
        b.append(T(M + 40, y + h / 2 - 2, [f"{reloj:02d}'–{reloj+mins:02d}'"], 22, c, weight="700"))
        b.append(T(M + 40, y + h / 2 + 26, [nom], 19, GRAY))
        parrafo_j(b, M + 400, y + (h - len(lin) * 29) / 2 - 5, txt, CW - 440, 21, INK, lh=29)
        reloj += mins
        y += h + 6
    y += 20
    # Si Sociales no es tu fuerte
    y = seccion(b, y, "Si Sociales no es tu fuerte",
        "Lo que tienes que poder explicar en dos minutos, sin jerga. Si un estudiante sabe más que "
        "tú de un tema, déjalo explicar y pide que señale en el caso de dónde lo saca.",
        color=VERDE)
    an = (CW - 18) / 2
    items = NO_ES_TU_FUERTE[mis]
    for fila in range(2):
        par = items[fila * 2: fila * 2 + 2]
        alto = max(66 + len(wrap_px(t, 20, an - 70)) * 28 for _, t in par) + 10
        for k, (tit, txt) in enumerate(par):
            x = M + k * (an + 18)
            b.append(rect(x, y, an, alto, VERDE_BG, r=14, stroke=VERDE_LN, sw=1.8))
            b.append(rect(x + 12, y + 12, 5, alto - 24, VERDE, r=3))
            b.append(T(x + 38, y + 40, [tit], 21, VERDE, weight="700"))
            parrafo_j(b, x + 38, y + 50, txt, an - 70, 20, INK, lh=28)
        y += alto + 12
    y += 16
    # ICFES
    banco = BANCO.get(mis, [])
    y = seccion(b, y, "Las cuatro preguntas Saber 11 y su clave",
        "Van con el membrete «Pregunta Saber 11», sin año. Claves verificadas "
        "resolviendo cada pregunta.")
    for k, (x4, est, ins_, ctx) in enumerate(INS_ICFES.get(mis, [])):
        fila = banco[k] if k < len(banco) else {}
        ctx_ = fila.get("contexto", "—")
        i_est = d["estr"].index(est) if est in d["estr"] else 0
        cc = COLS_MIS[mis][i_est]
        l_c = wrap_px(ctx_, 20, 620, "700")
        l_i = wrap_px(ins_, 19, 640)
        h = max(62, 20 + max(len(l_c), len(l_i)) * 28)
        b.append(rect(M, y, CW, h, "white", r=12, stroke=VERDE_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, h - 20, cc, r=2))
        b.append(T(M + 36, y + h / 2 - 3, [f"P{x4}"], 21, cc, weight="700"))
        b.append(T(M + 36, y + h / 2 + 20, [f"pág. {i_pags[0] if x4 <= 2 else i_pags[1]}"], 16, GRAY))
        b.append(T(M + 150, y + h / 2 + 8, [f"E{i_est+1} · {comp_icfes(mis, x4)}"], 18, cc, weight="700"))
        parrafo_j(b, M + 290, y + (h - len(l_c) * 28) / 2 - 4, ctx_, 620, 20, INK, weight="700", lh=28)
        parrafo_j(b, M + 940, y + (h - len(l_i) * 28) / 2 - 4, ins_, 640, 19, GRAY, style="italic", lh=28)
        cl = fila.get("clave", "").strip()
        b.append(rect(W - M - 96, y + h / 2 - 22, 64, 44, VERDE_BG, r=10, stroke=VERDE, sw=2))
        b.append(T(W - M - 64, y + h / 2 + 10, [cl or "—"], 26, VERDE, weight="700", anchor="middle"))
        y += h + 6
    y += 22
    y = seccion(b, y, "Después de la clase · tu registro",
        "Se llena el mismo sábado, antes de salir. Esto no lo ve el estudiante.")
    alto_reg = int(min(232, (2470 - y - 14) / 2))
    registro_docente(b, y, alto=alto_reg, campos=[
        ("¿Qué concepto hubo que explicar dos veces?", "y con qué ejemplo funcionó la segunda"),
        ("¿A quién hay que volver la próxima clase?", "nombres, no «algunos»"),
        ("¿Qué cuaderno quedó con el instrumento vacío?", "aunque haya acertado la respuesta"),
        ("¿Dónde se polarizó el salón?", "y cómo volviste al caso; va al reporte")])
    pie(b, 4 + mis * 2)
    svg_close(b, OUTP + f"{4 + mis * 2:02d}.svg")


def h17():
    """Clases 7 y 8 · el simulacro de EDUCATE y su socialización en el cuaderno (C7 y C8)."""
    b = svg_open()
    y = cabecera(b, "Clases 7 y 8", "El simulacro de EDUCATE y su socialización en el cuaderno",
                 derecha=str(C8["preguntas_cuaderno"]), dsub="preguntas caben en el cuaderno")
    PS.hoja(b, y, C7, C8, SOC, SOC_BG, SOC_LN, seccion, nota)
    pie(b, 17)
    svg_close(b, OUTP + "17.svg")


def hoja_dinamicas(mis):
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Dinámicas · Misión {mis}",
                 "Movimiento con sentido: el cuerpo ensaya lo que después hará la mente",
                 derecha=f"{mis}", dsub="de 6 misiones")
    y = nota(b, M, y, CW,
        "La dinámica debe ser isomorfa a la estrategia: lo que hace el cuerpo tiene que ser el "
        "mismo movimiento que después hará la mente frente al caso. Antes de usar una, responde "
        "esto: ¿qué paso de la estrategia está ejercitando? Si no hay respuesta, es recreo, no clase.",
        ORO, ORO_BG, ORO_LN, "La regla para aprobar cualquier dinámica", 24) + 26
    for i, din in enumerate(DINAMICAS[mis]):
        y = bloque_dinamica(b, y, i, din, d["estr"][i], COLS_MIS[mis][i])
    bloque_reto(b, y + 6, mis, RETOS[mis])
    pie(b, 17 + mis)
    svg_close(b, OUTP + f"{17 + mis:02d}.svg")


def h24():
    b = svg_open()
    total = sum(len(v) for v in AVISOS.values())
    y = cabecera(b, "Cierre del área", "Los avisos del libro, juntos, y lo que hay que devolver",
                 derecha=str(total), dsub="avisos del libro")
    y = seccion(b, y, f"Los {total} avisos del libro, en una sola lista",
        "Para repasarlos antes de empezar el área. Ninguno se le oculta al estudiante: si lo "
        "detecta y lo escribe, aprendió más que el que marcó la opción esperada.")
    cx = [M, M + 290, M + 430]
    y = encabezado_tabla(b, y, list(zip(cx, ["DÓNDE", "SEVERIDAD", "QUÉ PASA"])), 46)
    for m in range(1, 7):
        for preg, sev, que, hacer in AVISOS.get(m, []):
            c, bg, ln = SEV[sev]
            lin = wrap_px(que, 18, CW - 470)
            h = max(46, 14 + len(lin) * 24)
            b.append(rect(M, y, CW, h, bg, r=10, stroke=ln, sw=1.6))
            b.append(rect(M + 9, y + 8, 4, h - 16, c, r=2))
            b.append(T(cx[0] + 30, y + h / 2 + 7, [f"M{m} · {preg}"], 18, INK, weight="700"))
            chip(b, cx[1] + 6, y + h / 2 - 13, sev.upper(), c, size=12, pad=10, fill="white", txtc=c)
            parrafo_j(b, cx[2] + 14, y + (h - len(lin) * 24) / 2 - 4, que, CW - 470, 18, INK, lh=24)
            y += h + 4
    y += 22
    y = seccion(b, y, "Qué tienes que devolver al terminar el área")
    dev = [("Los seis registros de clase", "con nombres, no «algunos»"),
           ("El conteo por competencia del simulacro", "el dato que decide el refuerzo"),
           ("Dónde se polarizó el salón", "para la decisión pendiente de la Gerencia"),
           ("Los avisos nuevos que encuentres", "la lista se hizo resolviendo, y seguro falta alguno")]
    for t, s_ in dev:
        b.append(rect(M, y, CW, 64, "white", r=14, stroke=SOC_LN, sw=2))
        b.append(rect(M + 14, y + 12, 5, 40, ORO, r=3))
        b.append(checkbox(M + 42, y + 19, 13, SOC))
        b.append(T(M + 100, y + 41, [t], 23, INK, weight="700"))
        b.append(T(M + 760, y + 41, [s_], 21, GRAY))
        y += 72
    pie(b, 24)
    svg_close(b, OUTP + "24.svg")


def build():
    h1(); h2()
    hoja_momentos(1); hoja_momentos(2)
    for m in range(1, 7):
        hoja_clase(m); hoja_clase_b(m)
    h17()
    for m in range(1, 7):
        hoja_dinamicas(m)
    h24()
    return [f"{OUTP}{i:02d}.svg" for i in range(1, TOTAL + 1)]


PDF = "/home/user/educate-saber11/entregables/EDUCATE_Planeador_Sociales.pdf"

if __name__ == "__main__":
    import sys
    import render
    hojas = build()
    print(len(hojas), "hojas del planeador de Sociales y Ciudadanas")
    if "--pdf" in sys.argv:
        render.unir(hojas, PDF)
        n, sin = render.verifica(PDF, "PLANEADOR")
        print(f"{PDF}: {n} páginas · sin pie: {sin or 'ninguna'}")
