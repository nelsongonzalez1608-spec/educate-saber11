#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLANEADOR DEL DOCENTE · SOCIALES Y CIUDADANAS · las ocho clases del área.

Mismo modelo aprobado en el piloto de Matemáticas y ya entregado en Lectura Crítica
(plan_lc.py): seis momentos de 15·20·35·20·20·10, «tu aporte» acotado en cada uno y un
banco de dinámicas isomorfas a las estrategias. Usa el motor de plan_piezas.py sin
cambiarlo.

Lo propio del área: donde Lectura Crítica tiene el texto marcado, Sociales tiene el MAPA
DE ACTORES de la portada del área (página 96): quién gana, quién pierde, quién decide. Y
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
     "Que el estudiante transfiera por sí solo la estrategia a preguntas reales del ICFES, con "
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

CLASES = [
    (1, "Momento 1 · Competencias ciudadanas", "páginas 97 a 103 del cuaderno"),
    (2, "Momento 2 · Competencias ciudadanas", "páginas 104 a 110 del cuaderno"),
    (3, "Momento 3 · Competencias ciudadanas", "páginas 111 a 117 del cuaderno"),
    (4, "Momento 4 · Historia y cultura", "páginas 118 a 124 del cuaderno"),
    (5, "Momento 5 · Espacio y ambiente", "páginas 125 a 131 del cuaderno"),
    (6, "Momento 6 · Ético-político · cierre del área", "páginas 132 a 138 del cuaderno"),
    (None, "Simulacro del área", "las 24 preguntas oficiales, en condiciones de prueba"),
    (None, "Socialización del simulacro", "devolución, reparación y cierre del área"),
]

BASE = {1: 97, 2: 104, 3: 111, 4: 118, 5: 125, 6: 132}
LIBRO = {1: (336, 339), 2: (347, 349), 3: (358, 361), 4: (370, 374), 5: (383, 386), 6: (398, 402)}

# PS pensamiento social · IP interpretación y análisis de perspectivas · PRS pensamiento
# reflexivo y sistémico. Clasificación NUESTRA por estrategia, no la oficial del ICFES.
COMP_NOM = {"PS": "Pensamiento social", "IP": "Interpretación y análisis de perspectivas",
            "PRS": "Pensamiento reflexivo y sistémico"}
COMP_EST = {1: ["IP", "PS", "PRS", "PS"], 2: ["IP", "PS", "PRS", "PS"],
            3: ["IP", "PRS", "PS", "PRS"], 4: ["PRS", "IP", "PRS", "PS"],
            5: ["PS", "IP", "PRS", "IP"], 6: ["PS", "PRS", "PRS", "IP"]}

MISIONES = {
 1: dict(comp="Competencias ciudadanas", pags="97 a 103",
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
   cierre="La estrategia 3 —si pasa esto, qué pasa después— no tiene pregunta oficial en el "
          "entrenamiento: se entrena solo en el taller, en las preguntas 3, 6 y 9. Dale ahí el "
          "tiempo que el ICFES no le da."),
 2: dict(comp="Competencias ciudadanas", pags="104 a 110",
   tema="Contrastar posturas: en qué coinciden, en qué no",
   competencia="IP · análisis de perspectivas",
   estr=["En qué coinciden y en qué no", "El nombre exacto de la figura",
         "Las dos caras de la misma medida", "Qué queda en entredicho"],
   instala="Que dos actores pueden coincidir en lo que proponen y diferir en por qué lo proponen, "
           "o al revés. Separar la propuesta de la razón es la operación que más evalúa el ICFES "
           "en esta competencia.",
   ojo="La opción D de la pregunta 6 dice que la Conmoción Interior permite «suspender» los "
       "derechos humanos. Es falso: la Constitución dice limitar, no suspender, y la página 99 "
       "del cuaderno enseña justo eso. Dilo en voz alta.",
   cierre="Los mecanismos de participación (pregunta 9 y la segunda del ICFES) se confunden entre "
          "sí. El criterio no es quién lo convoca sino qué se decide: un mandato, una ley o la "
          "Constitución."),
 3: dict(comp="Competencias ciudadanas", pags="111 a 117",
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
 4: dict(comp="Historia y cultura", pags="118 a 124",
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
 5: dict(comp="Espacio y ambiente", pags="125 a 131",
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
 6: dict(comp="Ético-político", pags="132 a 138",
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
      "El banco no trae una pregunta oficial limpia de efectos sobre dimensiones: la estrategia 3 "
      "no aparece en el entrenamiento ICFES.",
      "Dale tiempo completo a las preguntas 3, 6 y 9 del taller.")],
 2: [("preg. 6", "media",
      "La opción D dice que la Conmoción Interior permite suspender los derechos humanos. La "
      "Constitución dice limitar, no suspender (art. 214).",
      "No la dejes pasar como dato: el cuaderno la marca y la página 99 enseña lo contrario."),
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
      "La pregunta oficial trata de una niña wayú de 11 años, víctima de violación, que pide "
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
SELLOS = [(AREA_CSV, m, pag, preg, saber, "tarjeta de la pregunta", "En el cuaderno")
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
