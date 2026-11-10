#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLANEADOR DEL DOCENTE · QUÍMICA · las ocho clases del área.

Mismo modelo aprobado en el piloto de Matemáticas y ya entregado en Lectura Crítica, Sociales y
Biología (plan_bio.py, del que sale este archivo): seis momentos de 15·20·35·20·20·10, «tu aporte»
acotado en cada uno y un banco de dinámicas isomorfas a las estrategias. Usa el motor de
plan_piezas.py sin cambiarlo; el dibujo de las hojas es el de plan_bio.py (que no se toca).

Lo propio del área: donde Biología tiene el dato y su comparación, Química tiene LA PARTÍCULA Y SU
UNIDAD de la portada del área (página 182): qué se observó, qué se midió y con qué unidad, y qué
hacen las partículas. Once sellos «Alto · aquí entra el profe» (todos del taller; la Misión 2 no
tiene) y cuatro claves del libro que el profe tiene que saber defender o discutir (M3 P9, M5 P10,
M6 P5 y P6).

Seguridad (Nelson, 10 nov): ninguna dinámica usa sustancias reales, fuego, calor ni nada que un
salón no pueda hacer sin riesgo. Todo es con el cuerpo, tarjetas, cinta, clips y el tablero; los
retos que hablan de un experimento se diseñan en papel.

Para las guías (clase_viva_qui.py), con los mismos nombres de plan_bio.py:
    FASES  CLASES  BASE  LIBRO  PAG_LIBRO  MISIONES  AVISOS  TALLER  INS_ICFES  BANCO  SELLOS
    SABERES  DINAMICAS  RETOS  CLAVES  ACTIVACION  PROBLEMATIZADORA  PREGUNTA_AREA
    NO_ES_TU_FUERTE  COLS_MIS  COMP_EST  COMP_NOM  COMP_ICFES
COMP_ICFES {misión: [competencia de P1…P4]} es la que el cuaderno le pone a cada pregunta de
entrenamiento (campo comp de quiN_icfes.py, leído sin importar el módulo). COMP_EST sale de ahí:
cada estrategia toma la competencia de su pregunta de entrenamiento.

Claves del libro: copiadas del docstring de qui1.py … qui6.py (resueltas a mano el 7 nov) y
comprobadas al construir con `verificar()`. Las del entrenamiento: tablero/icfes.csv, cruzadas
con el docstring de quiN_icfes.py y resueltas de nuevo el 10 nov (ver TEXTOS_QUI.md).

Membrete (Nelson, 10 nov): «Pregunta Saber 11», sin año ni «oficial». En este planeador las
preguntas de entrenamiento se llaman «preguntas tipo Saber 11».
"""
import ast, csv, re
from plan_piezas import *
import plan_piezas as PZ

QUI = "#0F7A68"; QUI_BG = "#E9F4F1"; QUI_LN = "#B5DAD1"
TOTAL = 24
configurar(QUI, QUI_BG, QUI_LN, "Química", TOTAL)
AREA_CSV = "Química"

AZUL = "#242478"; ROJO_E = "#A82424"; ORO_E = "#C9821B"
# El cierre no va en verde: el verde esmeralda es el color del área (y de la activación).
PIZARRA = "#4A5A70"

# Los colores de las cuatro estrategias, tal como salen en los chips del cuaderno (EST de quiN.py).
COLS_MIS = {1: [AZUL, ROJO_E, ORO_E, MORADO], 2: [AZUL, ROJO_E, ORO_E, MORADO],
            3: [AZUL, ROJO_E, MORADO, ORO_E], 4: [AZUL, MORADO, ROJO_E, ORO_E],
            5: [AZUL, ROJO_E, MORADO, ORO_E], 6: [AZUL, ROJO_E, MORADO, ORO_E]}
COLS_EST = COLS_MIS[1]

# ─────────────────────────── los seis momentos ───────────────────────────
# El reparto es el aprobado: 15 · 20 · 35 · 20 · 20 · 10 = 120. No se cambia.
FASES = [
    ("Activación", 15, QUI,
     "Que el estudiante describa un fenómeno de todos los días con tres preguntas —qué se observó, "
     "qué se midió y con qué unidad, y qué hacen las partículas— antes de explicarlo y antes de ver "
     "cualquier opción.",
     ["Proyecta o lee una observación de dos o tres renglones sin decir de dónde salió.",
      "Pide tres respuestas, en voz alta o en el tablero: qué se observó, qué se midió y con qué "
      "unidad, y qué hacen las partículas.",
      "Ejecuta la dinámica de apertura según la estrategia del encuentro."],
     "No explica el fenómeno ni acepta todavía explicaciones. Si alguien dice «es una reacción "
     "química», le devuelve la pregunta: «¿qué viste o qué mediste que te lo dice?». El cuaderno "
     "sigue cerrado.",
     "Proyector o tablero con la observación. Todavía no se abre el cuaderno."),
    ("Pregunta problematizadora", 20, "#1F4E8C",
     "Que el estudiante compruebe que en Química la respuesta sale del dato con su unidad —del texto, "
     "la tabla o la gráfica— y de lo que hacen las partículas, no de la palabra que suena más técnica, "
     "usando la pregunta modelo del libro.",
     ["Presenta la pregunta modelo del libro y la deja a la vista todo el momento.",
      "Pide respuestas a mano alzada ANTES de releer el texto o la tabla, y las anota en el tablero.",
      "Hace la pregunta que gobierna el área: ¿qué número, con su unidad, o qué observación respalda eso?",
      "Revela la clave solo al final y trabaja por qué cae cada una de las otras tres."],
     "Regla del momento: nadie justifica con «yo sé que» ni con una palabra técnica suelta. Toda "
     "intervención señala un número con su unidad, una fila de la tabla o un punto de la gráfica.",
     "Libro abierto en la pregunta modelo. Cuaderno solo en «mi primera idea»."),
    ("Desarrollo guiado", 35, "#3B3BA6",
     "Que el estudiante escriba el instrumento —la cuenta con sus unidades, la propiedad, el dibujo "
     "de las partículas o la evidencia— antes de mirar las opciones, y deje por escrito de dónde lo sacó.",
     ["Entrega las hojas del momento y trabaja por bloques: 1-2, 3-4, 5-6, 7-8 y 9-10.",
      "Antes de que marquen, verifica que el instrumento tenga escrita la cuenta con sus unidades o el "
      "dato que pide.",
      "Entre bloques, introduce la dinámica de la estrategia que viene: seis minutos, no más.",
      "Cuando aparece un sello «Alto · aquí entra el profe», explica el concepto en dos minutos y sigue."],
     "No hace la cuenta antes que ellos ni dicta la respuesta. Si un estudiante se traba, le pregunta "
     "qué se midió y en qué unidad; si el instrumento está vacío, lo devuelve al texto o a la tabla "
     "antes que a las opciones.",
     "Cuaderno, las cinco hojas de taller. Libro, en las preguntas 1 a 10."),
    ("Reto en equipo", 20, MORADO,
     "Que el estudiante defienda su explicación con el dato y la unidad en la mano, y acepte que otro "
     "equipo puede ver una variable o una propiedad que él no vio.",
     ["Arma equipos de tres y entrega el reto del corte de este momento.",
      "Exige que cada integrante llegue con su instrumento YA diligenciado individualmente.",
      "Da tres minutos de defensa por equipo: señalan el dato, la cuenta o la propiedad que los respalda.",
      "Cierra mostrando qué variable, qué unidad o qué propiedad quedó por fuera en cada propuesta."],
     "El equipo discute, pero cada uno escribe en SU tarjeta del reto. No se acepta una defensa que "
     "diga «es que así reacciona»: se nombra el dato con su unidad, la cuenta o la propiedad.",
     "Cuaderno de cada estudiante y la tarjeta del reto del corte."),
    ("Evaluación individual", 20, ROJO,
     "Que el estudiante transfiera por sí solo la estrategia a preguntas tipo Saber 11, con "
     "situaciones que no trabajó en clase.",
     ["Entrega las dos hojas de entrenamiento del momento.",
      "Da el tiempo completo sin intervenir ni explicar conceptos.",
      "Registra quién llena el instrumento y quién va directo a las opciones."],
     "Este momento es silencioso y en filas individuales. Es el que produce el dato de "
     "seguimiento. Si un estudiante marca sin llenar el instrumento, se le anota, no se le corrige.",
     "Cuaderno, las dos hojas de entrenamiento. Reloj a la vista."),
    ("Cierre", 10, PIZARRA,
     "Que el estudiante nombre la estrategia que usó y se lleve un concepto del día —una propiedad, "
     "una ley o una relación entre cantidades— escrito en sus propias palabras.",
     ["Socializa solo las preguntas que el grupo falló, pidiendo el dato, la cuenta o la propiedad "
      "que las resuelve.",
      "Pide que lean en voz alta su salvavidas: lo mínimo que sí tenían claro.",
      "Cada uno escribe el concepto del día en la franja «Palabras que me frenaron» de su hoja."],
     "No dicta la definición. El concepto se escribe como el estudiante lo entendió; si quedó mal "
     "entendido, eso se ve en la hoja y se corrige la próxima clase.",
     "Cuaderno: «Palabras que me frenaron», «lo que me llevo», carita de salida y portada del área."),
]

CLASES = [
    (1, "Momento 1 · Aspectos analíticos de sustancias", "páginas 183 a 189 del cuaderno"),
    (2, "Momento 2 · Aspectos fisicoquímicos de sustancias", "páginas 190 a 196 del cuaderno"),
    (3, "Momento 3 · Aspectos analíticos de mezclas", "páginas 197 a 203 del cuaderno"),
    (4, "Momento 4 · Aspectos fisicoquímicos de mezclas", "páginas 204 a 210 del cuaderno"),
    (5, "Momento 5 · Entorno químico · el carbono", "páginas 211 a 217 del cuaderno"),
    (6, "Momento 6 · Entorno químico · cierre del área", "páginas 218 a 224 del cuaderno"),
    (None, "Simulacro del área", "las 24 preguntas tipo Saber 11, en condiciones de prueba"),
    (None, "Socialización del simulacro", "devolución, reparación y cierre del área"),
]

BASE = {1: 183, 2: 190, 3: 197, 4: 204, 5: 211, 6: 218}
LIBRO = {1: (140, 142), 2: (150, 152), 3: (160, 162), 4: (170, 173), 5: (182, 185), 6: (193, 196)}
# Página del libro de cada pregunta: «la lees en tu libro, página N» (Q[n]["pag"] de quiN.py).
PAG_LIBRO = {
 1: [140, 140, 140, 141, 141, 141, 141, 141, 142, 142],
 2: [150, 150, 150, 151, 151, 151, 151, 152, 152, 152],
 3: [160, 160, 161, 161, 161, 161, 161, 162, 162, 162],
 4: [170, 171, 171, 172, 172, 172, 172, 173, 173, 173],
 5: [182, 182, 182, 183, 183, 184, 184, 185, 185, 185],
 6: [193, 194, 194, 194, 195, 195, 195, 196, 196, 196],
}

# Las tres competencias de Ciencias Naturales en el Saber 11.
COMP_NOM = {"UC": "Uso comprensivo del conocimiento científico", "EF": "Explicación de fenómenos",
            "IN": "Indagación"}
_COD = {"uso comprensivo": "UC", "explicación de fenómenos": "EF", "indagación": "IN"}

MISIONES = {
 1: dict(comp="Aspectos analíticos de sustancias", pags="183 a 189",
   tema="Disolver, separar y reaccionar",
   competencia="UC · partículas, cuentas y propiedades",
   estr=["La regla de tres con sus unidades", "La propiedad que la delata",
         "El tope de lo que se disuelve", "Lo que la reacción necesita"],
   instala="Que en Química un número sin unidad no dice nada: la regla de tres se arma con la unidad "
           "al lado de cada número, una sustancia se reconoce por la propiedad que las otras no tienen, "
           "lo que se disuelve tiene un tope que cambia con la temperatura, y una reacción lenta se "
           "acelera con lo que le falta, no con más de lo que ya sobra.",
   ojo="La figura de la aspirina (preguntas 9 y 10) dibuja mal las moléculas: no la proyectes y trabaja "
       "con las fórmulas. En la pregunta 4 el dibujo no trae 40 y 16 bolitas: se cuenta con los números "
       "del texto. La 6 y la 8 piden la misma idea, y la 10 casi se responde con el enunciado.",
   cierre="La estrategia 4 —lo que la reacción necesita— tiene una sola pregunta en el taller (la 10) y "
          "una en el entrenamiento. Dale a la dinámica el tiempo completo: la colina de la energía de "
          "activación vuelve en la misión 6, con las reacciones que calientan."),
 2: dict(comp="Aspectos fisicoquímicos de sustancias", pags="190 a 196",
   tema="El calor, los cambios de estado y la densidad",
   competencia="EF · calor, estados y densidad",
   estr=["Donde la temperatura se queda quieta", "El calor, tramo por tramo",
         "Lo explican los choques de partículas", "Más denso abajo, menos denso arriba"],
   instala="Que el calor que entra a una sustancia hace dos trabajos distintos: subir la temperatura "
           "(calor sensible) y, en la meseta, cambiar el estado sin subirla (calor latente). Que todo "
           "eso se explica con partículas que se mueven y chocan, y que lo menos denso queda arriba.",
   ojo="La gráfica de la pregunta 1 pone la meseta de Y en 200 °C y el texto dice 160 °C: se responde "
       "con el texto. La curva del tanque de la 3 sube mucho más de lo que predice la ley de los gases. "
       "Y la 10 no ofrece la causa principal de que la esfera suba —el empuje—: la clave A solo explica "
       "la rapidez.",
   cierre="Las preguntas 2 y 4 hacen la misma cuenta de dos tramos (m · c · ΔT más m · L). Usa la "
          "segunda para que la hagan solos, con las unidades escritas en cada paso: J/(g·°C) por g por "
          "°C da julios."),
 3: dict(comp="Aspectos analíticos de mezclas", pags="197 a 203",
   tema="Mezclar no es transformar",
   competencia="IN · variables y evidencia",
   estr=["Cambia una sola cosa a la vez", "Clasifica por lo que se observa",
         "Sigue al gas: presión y temperatura", "Pide la evidencia antes de creer"],
   instala="Que para saber qué causó un efecto se cambia una sola cosa a la vez, que una mezcla se "
           "clasifica por lo que se ve (cuántas fases, si se separa en reposo), que un gas encerrado "
           "sube y baja con la presión y la temperatura, y que una conclusión pide evidencia: algo que "
           "pasó en un vaso y no en su testigo.",
   ojo="La clave A de la pregunta 9 es dudosa: ninguna opción explica limpio de dónde sale la espuma, y "
       "falta confirmarla con la editorial. En la 1, Luis cambió dos condiciones a la vez; en la 2, la "
       "opción A (la acidez de la bebida) es químicamente defendible aunque el texto no la sostiene.",
   cierre="El libro dice que la misión trabajó «sin recurrir a cambios químicos», pero la tableta "
          "efervescente de las preguntas 2 a 4 es una reacción (ácido cítrico más bicarbonato, que "
          "suelta CO₂). Dilo: mezclar no es transformar, pero en esos vasos sí hubo una transformación."),
 4: dict(comp="Aspectos fisicoquímicos de mezclas", pags="204 a 210",
   tema="Cada propiedad física separa algo",
   competencia="EF · propiedades que separan",
   estr=["Compara en igualdad de condiciones", "¿Se hunde, flota o queda suspendido?",
         "Ponle nombre a la propiedad", "Una propiedad, un método de separación"],
   instala="Que una comparación solo vale si todo lo demás fue igual; que en un líquido lo que se hunde, "
           "flota o queda suspendido depende de la densidad y del tamaño de las partículas; que cada "
           "propiedad tiene su nombre exacto y su unidad, y que cada una sirve para un método de "
           "separación distinto.",
   ojo="La pregunta 1 pide justificar algo que en la realidad es falso: el sulfato de cobre NO es el más "
       "soluble de los tres (a 20 °C el azúcar se disuelve mucho más). Se responde con la tabla, y el "
       "cuaderno pone un sello. La 8 da por hecho que magnetismo y tamaño «no fueron eficientes», cosa "
       "que el texto nunca dice.",
   cierre="Las preguntas 8 a 10 son de minería artesanal: separar sin agua ni químicos. Buen cierre para "
          "decir que cada propiedad física es una herramienta: el imán, el tamiz, la bandeja que vibra y "
          "el viento."),
 5: dict(comp="Entorno químico", pags="211 a 217",
   tema="El carbono en el tanque, en el vaso y en la bolsa",
   competencia="EF · estructura, átomos y emisiones",
   estr=["Del grupo funcional a la propiedad", "Los átomos no se pierden: se cuentan",
         "Lo que la tabla sí deja afirmar", "Qué sale del tubo de escape"],
   instala="Que el grupo funcional de una molécula decide sus propiedades (polar o apolar, se mezcla con "
           "el agua o no), que en una reacción los átomos no se pierden sino que se cuentan a cada lado "
           "de la flecha, que una tabla solo deja afirmar lo que mide y que lo que sale del tubo de "
           "escape depende de lo que entra al motor y del oxígeno que alcanza.",
   ojo="La clave B de la pregunta 10 encadena mal la causa: el biodiésel casi no emite azufre porque los "
       "aceites vegetales casi no lo traen, no por los «subproductos oxigenados»; y el enunciado lo "
       "llama «alquenos» cuando es un éster. El texto de la cafeína (pregunta 4) dice que su polaridad "
       "la ayuda a pasar al cerebro: es impreciso.",
   cierre="La B es clave una sola vez y en las preguntas 2, 6 y 10 la correcta es la más larga. No "
          "enseñes el truco: exige el instrumento —el grupo marcado, los átomos contados— antes de "
          "mirar las opciones."),
 6: dict(comp="Entorno químico", pags="218 a 224",
   tema="Reacciones que calientan y encadenan",
   competencia="EF · reacciones y energía",
   estr=["La ecuación es una receta", "¿El calor sale o entra?",
         "Una conclusión vale lo que valen sus datos", "Piezas que se repiten: los polímeros"],
   instala="Que una ecuación balanceada es una receta en moles (y, con las masas molares, en gramos), que "
           "en una reacción el calor sale o entra y el termómetro lo dice, que una conclusión vale lo "
           "que valen sus datos y que un polímero es una cadena de piezas que se repiten. Es la misión "
           "que recoge las cinco anteriores.",
   ojo="Las preguntas 5 y 6 enseñan un concepto equivocado: la PVP del gel y el almidón YA son "
       "polímeros, y al amasarlos no se forma «un nuevo polímero». Las claves B valen solo dentro del "
       "modelo del libro, y en la 6 un estudiante que sepa química puede defender la D. En la 9 faltan "
       "las masas molares: Fe = 56 g/mol y O = 16 g/mol.",
   cierre="La pregunta 2 compara combustibles por mol; por gramo, el metano suelta más energía que la "
          "gasolina. La lección de cierre del área: una conclusión depende de los datos que de verdad "
          "usa y de la unidad con que se compara."),
}

# Claves del libro: docstring de qui1.py … qui6.py (verificar() las compara al construir).
CLAVES = {
 1: dict(zip(range(1, 11), "CACBDAADBC")),
 2: dict(zip(range(1, 11), "BABBCDBADA")),
 3: dict(zip(range(1, 11), "BBCABDACAD")),
 4: dict(zip(range(1, 11), "ACCDABCDDB")),
 5: dict(zip(range(1, 11), "CAACCDADAB")),
 6: dict(zip(range(1, 11), "BCCABBDAAC")),
}

# ─────────── lo que el libro trae y hay que saber antes de entrar (de hallazgos.csv y
# tablero/propuestas/quiN_hallazgos.csv) ───────────
# Rótulo: «preg. N», «preg. N y M», «preg. N a M» (lo lee el motor de las guías), «ICFES k» para
# el entrenamiento, o un rótulo general. Severidad: alta · media · baja · atención.
AVISOS = {
 1: [("preg. 9 y 10", "media",
      "La figura de la síntesis de la aspirina dibuja mal las moléculas (sin el anillo de benceno) y su "
      "«subproducto» vuelve a ser aspirina.",
      "No la proyectes. La cuenta sale de las fórmulas C₇H₆O₃ y C₉H₈O₄ y de las masas molares."),
     ("preg. 4", "baja",
      "El texto dice 40 moléculas a 5 °C y 16 a 25 °C; en el dibujo hay unas 55 y unas 13 bolitas.",
      "Que trabajen con los números del texto. El cuaderno lo advierte."),
     ("preg. 7", "baja",
      "La tabla escribe «α» donde va el signo de proporcional (∝) y no dice a qué temperatura se midió "
      "la presión de vapor.",
      "Es el sello de la pregunta 7: explica la proporción inversa."),
     ("preg. 6 y 8", "baja",
      "Piden la misma idea: la sal absorbe más agua del aire porque tiene menor presión de vapor.",
      "La 6 se trabaja filtrando propiedades y la 8 armando la cadena dato, mecanismo, efecto."),
     ("preg. 10", "atención",
      "El enunciado ya dice que la reacción «requiere un catalizador ácido»: la clave C se lee casi en "
      "el enunciado.",
      "Úsala para dibujar la colina de la energía de activación, no para medir química."),
     ("preg. 2", "atención",
      "La clave A explica la ley de Henry diciendo que el CO₂ «se comprime»: la idea sirve, la redacción "
      "es imprecisa.",
      "Precisa: con más presión del gas encima, más moléculas entran al líquido."),
     ("ICFES 3", "atención",
      "La tabla da 0 g/kg de CO₂ a 80 °C; el valor real es pequeño, pero no cero.",
      "No cambia la clave D.")],
 2: [("preg. 1", "media",
      "El texto dice que Y empieza a fundirse a 160 °C; la gráfica pone su meseta en 200 °C, y ninguna "
      "meseta termina.",
      "Se responde con el texto. La clave B se sostiene: Y tiene que subir más antes de fundirse."),
     ("preg. 3", "media",
      "La curva del tanque sube de 1,5 a 8 atm entre 20 y 70 °C; con la ley de los gases a volumen fijo "
      "subiría apenas un 17 %.",
      "No cambia la clave B. Si alguien hace la cuenta, tiene razón: el propano del tanque es un líquido "
      "que se evapora."),
     ("preg. 10", "media",
      "La causa principal de que la esfera suba es el empuje (el mercurio es más denso) y no está entre "
      "las opciones. La clave A solo explica la rapidez.",
      "Separa «por qué sube» de «por qué sube rápido», como el cuaderno."),
     ("preg. 5", "baja",
      "La opción A habla de «aire caliente» en un método que es una bandeja metálica.",
      "No cambia la clave C."),
     ("preg. 8", "baja",
      "Dice «200 mL de un sólido»: un sólido no se mide en mililitros.",
      "Errata. No cambia la clave A."),
     ("preg. 9 y 10", "atención",
      "El contexto remite a un video que no está en el cuaderno y no dice de qué metal es la esfera.",
      "El cuaderno supone acero (7,9 g/cm³) y lo dice."),
     ("ICFES 1", "atención",
      "La tabla no trae la unidad del tiempo, y la clave B es la menos mala más que una conclusión fuerte.",
      "Úsalo: un tiempo sin unidad no se puede comparar.")],
 3: [("preg. 9", "alta",
      "Ninguna opción es limpia: el vacío parcial jala aire por el filtro y el tubo, y la clave A dice que "
      "entra «por las juntas». Falta confirmar la clave con la editorial.",
      "Clave tomada: A, la única con el mecanismo bien (el vacío que succiona aire). Si alguien la "
      "discute con argumentos, tiene razón."),
     ("preg. 2", "media",
      "La opción A (la acidez de la bebida alimenta la efervescencia) es químicamente defendible; el texto "
      "no da ningún dato de acidez.",
      "Se responde con lo que dice el texto: lo único distinto del vaso 2 es el gas."),
     ("preg. 3", "media",
      "La evidencia de la clave C (más espuma en el vaso con gas) está confundida: una bebida con gas "
      "suelta su propio CO₂ al echarle un sólido.",
      "No cambia la clave. Pregunta: ¿esa espuma prueba que la tableta reaccionó más rápido?"),
     ("preg. 1", "atención",
      "Luis cambió dos condiciones a la vez (temperatura y agitación): los datos no dicen cuál pesó más.",
      "Es la estrategia del día: cambia una sola cosa a la vez."),
     ("preg. 5", "atención",
      "Los colores del aceite sobre el agua son interferencia de la luz, no una reacción.",
      "Es el sello de la pregunta 5."),
     ("preg. 6", "atención",
      "La pregunta de la llanta es de gases, no de análisis de mezclas.",
      "No cambia la clave D."),
     ("cierre del libro", "atención",
      "Dice que la misión observó las mezclas «sin recurrir a cambios químicos», pero la tableta "
      "efervescente es una reacción.",
      "Dilo en el cierre."),
     ("ICFES 2", "atención",
      "La tabla llama «neutro» a la leche (6,8) y al gel (7,2); en química, neutro es pH 7 a 25 °C.",
      "La clave B sale de la tabla. El cuaderno lo aclara."),
     ("ICFES 4", "atención",
      "En la gráfica C la mezcla 1 no tiene barra (pH 0 o dato faltante).",
      "Se redibujó igual. No cambia la clave D.")],
 4: [("preg. 1", "media",
      "Hay que justificar que el sulfato de cobre es el más soluble, y en la realidad no lo es: a 20 °C "
      "el azúcar se disuelve mucho más. La tabla tampoco dice cuánto soluto se echó.",
      "Es el sello de la pregunta 1. La clave A es la mejor dentro de la tabla, no una verdad química."),
     ("preg. 8", "baja",
      "Parte de que magnetismo y tamaño «no fueron eficientes», y el texto nunca lo dice.",
      "No cambia la clave D."),
     ("preg. 3", "atención",
      "El texto describe «una pasta espesa sin separación visible» y la clave la llama «suspensión "
      "estable»; no se sabe qué frasco tiene cada polvo.",
      "No cambia la clave C."),
     ("preg. 9", "atención",
      "La clave D habla de la «reacción» frente a la vibración: no hay ninguna reacción química.",
      "Aclara la palabra: aquí «reacción» quiere decir respuesta."),
     ("preg. 6 y 7", "atención",
      "El carbón común conduce poco, salvo el grafito; en la aventadora decide la densidad y también la "
      "forma de lo que vuela.",
      "No cambia las claves B y C."),
     ("teoría del libro", "baja",
      "El texto de teoría dice que «un colador de plástico no transfiere calor» (sí transfiere, mucho "
      "menos que el metal).",
      "Corrígelo si sale en clase."),
     ("ICFES 3", "atención",
      "La tabla le da al ácido sulfúrico una densidad de 2,7 g/mL (la real es 1,84) y al ácido "
      "clorhídrico un punto de ebullición de 48 °C.",
      "No cambia la clave B. Úsalo: un dato raro se revisa antes de creerle."),
     ("ICFES 4", "atención",
      "El enunciado dice que el imán «atrae elementos metálicos»: no todos (el aluminio y el cobre no).",
      "No cambia la clave A.")],
 5: [("preg. 10", "media",
      "La clave B encadena mal la causa: el biodiésel casi no emite azufre porque el aceite vegetal casi "
      "no lo trae, no por los «subproductos oxigenados». Y el enunciado lo llama «alquenos»: es un éster.",
      "Es la menos mala de las cuatro. Corrige en voz alta la causa y la familia."),
     ("preg. 4", "media",
      "El texto dice que la polaridad ayuda a la cafeína a llegar al cerebro: en general lo polar lo "
      "dificulta. Y la llama «amina» cuando sus grupos son sobre todo amidas.",
      "No cambia la clave C. El instrumento trabaja solo la cadena grupo polar, agua, sangre."),
     ("preg. 5", "atención",
      "Dice que la teobromina es «muy similar» a la cafeína, pero no da su fórmula.",
      "El cuaderno da C₇H₈N₄O₂: un grupo metilo menos que la cafeína."),
     ("preg. 1", "atención",
      "La opción A es verdadera (el –OH ayuda a quemar mejor), pero no explica el impacto negativo que "
      "se pide.",
      "Lee con ellos qué pide la pregunta."),
     ("preg. 3", "atención",
      "Las bolsas estuvieron en condiciones «similares», no iguales, y parte de la masa perdida puede ser "
      "agua.",
      "No cambia la clave A. Buena discusión: qué más habría que controlar."),
     ("preg. 6", "atención",
      "La clave dice que la evidencia «confirma»; con dos grupos sin tamaño conocido, «es coherente con» "
      "sería más justo.",
      "No cambia la clave D."),
     ("reparto de claves", "atención",
      "A 4 · B 1 · C 3 · D 2; en las preguntas 2, 6 y 10 la correcta es la más larga.",
      "Reportado a la editorial. No lo digas en clase."),
     ("ICFES 4", "atención",
      "La tabla llama «capacidad calorífica» a un dato en MJ/kg que es el poder calorífico: la energía "
      "que suelta un kilo al quemarse.",
      "No cambia la clave C. Aclara la palabra.")],
 6: [("preg. 5 y 6", "alta",
      "El libro dice que al amasar gel y almidón se forma «un nuevo polímero»: los dos YA son polímeros "
      "y solo se enredan y se atraen. Las claves B valen dentro del modelo del libro; en la 6, la D es "
      "defendible a medias.",
      "Clave tomada: B en las dos. Es el sello de la pregunta 5. Si alguien defiende la D de la 6 con "
      "química, reconócelo."),
     ("preg. 2 a 4", "media",
      "Compara por mol; por gramo, el metano suelta más que la gasolina. Y «libera –5470»: el signo "
      "ya dice que sale.",
      "Sello de la pregunta 2. Se responde por mol."),
     ("preg. 7", "media",
      "Las tres muestras se prepararon igual: si nada cambió entre ellas, las diferencias son error.",
      "No cambia la clave D. Pregunta: ¿qué cambió?"),
     ("preg. 9", "media",
      "Faltan las masas molares: el libro no da la del oxígeno.",
      "Escríbelas en el tablero: Fe = 56 g/mol y O = 16 g/mol. El cuaderno las da."),
     ("preg. 1", "baja",
      "El eje de la gráfica dice 0, 2, 3, 6…: el «3» debe ser 4.",
      "No cambia la clave B. El cuaderno redibuja el eje."),
     ("preg. 10", "atención",
      "Una sola medición por temperatura, y la relación «pH baja = descomposición» la afirman los "
      "investigadores, no los datos.",
      "No cambia la clave C. Es la estrategia del día."),
     ("reparto de claves", "atención",
      "A 3 · B 3 · C 3 · D 1.",
      "Reportado a la editorial. No lo digas en clase."),
     ("ICFES 2", "atención",
      "La opción D tiene la primera mitad cierta y una razón ambigua según se lea el signo; la "
      "comparación es por mol.",
      "La A es la única enteramente correcta.")],
}

# ─────────── los once sellos «Alto · aquí entra el profe» del cuaderno ───────────
# Leídos de alto_profe() en qui1.py, qui3.py … qui6.py (la Misión 2 y los módulos ICFES no tienen).
_S = [
 (1, 187, 7, "El signo ∝ y la proporción inversa: si la presión de vapor baja, la higroscopicidad sube."),
 (1, 188, 10, "Energía de activación: la colina que las moléculas tienen que subir para reaccionar, y qué la baja."),
 (3, 200, 5, "Por qué una capa delgada de aceite se ve de colores sobre el agua: es la luz, no una sustancia nueva."),
 (3, 201, 8, "Qué le pasa al vapor que se enfría en un recipiente cerrado y por qué deja un vacío parcial."),
 (4, 204, 1, "Cómo se mide de verdad la solubilidad y qué es más soluble en la realidad."),
 (4, 207, 6, "Por qué conducen los metales y el grafito, y por qué la sal conduce disuelta y no sólida."),
 (5, 212, 4, "Polar y apolar: por qué lo polar se disuelve en lo polar."),
 (5, 215, 7, "Enlace covalente polar y enlace iónico no son lo mismo."),
 (6, 218, 2, "Comparar por mol o por gramo: el orden de los combustibles puede cambiar."),
 (6, 221, 5, "Qué es un polímero, y por qué amasar dos polímeros no forma uno nuevo."),
 (6, 222, 8, "Energía de enlace: romper enlaces cuesta y formarlos libera; formar agua calienta."),
]
SELLOS = [(AREA_CSV, m, pag, preg, saber, "tarjeta de la pregunta", "En el cuaderno")
          for m, pag, preg, saber in _S]
TEXTOS = []        # los textos completos van en la guía (TEXTOS_QUI.md)

# Lo que el profe tiene que poder explicar en cada sello: título, qué es (sin jerga) y la pregunta
# que destraba. Mismo formato que SABERES de plan_bio.py.
SABERES = {
 (1, 7): ("Proporción inversa",
          "El signo ∝ se lee «es proporcional a». Proporcional a 1 ÷ P quiere decir que van al revés: si "
          "la presión de vapor se duplica, la higroscopicidad se reduce a la mitad. La sustancia con "
          "menor presión de vapor es la que más agua le saca al aire.",
          "Si la presión de vapor baja a la mitad, ¿la higroscopicidad sube o baja, y cuánto?"),
 (1, 10): ("Energía de activación y catalizador",
          "Para reaccionar, las moléculas tienen que chocar con energía suficiente: es como subir una "
          "colina. Si pocas la suben, la reacción es lenta aunque sobre reactivo. Un catalizador abre un "
          "camino con la colina más baja; calentar le da a más moléculas la energía para subirla. Echar "
          "más del reactivo que ya sobra no la baja.",
          "¿Lo que falta es más reactivo o una colina más baja?"),
 (3, 5): ("Los colores del aceite sobre el agua",
          "Una capa de aceite muy delgada refleja la luz dos veces, arriba y abajo de la capa. Esos dos "
          "reflejos se refuerzan o se cancelan según el grosor, y por eso se ven franjas de colores, como "
          "en una pompa de jabón. Es la luz: no aparece ninguna sustancia nueva.",
          "Si fuera una sustancia nueva, ¿qué tendría que haber pasado con el aceite?"),
 (3, 8): ("El vapor que se enfría y el vacío parcial",
          "Al calentar, el agua de abajo se vuelve vapor y su presión empuja el líquido hacia arriba. Al "
          "apagar, el vapor se enfría y vuelve a ser agua líquida, que ocupa muchísimo menos espacio: "
          "abajo queda menos presión que afuera (un vacío parcial) y el líquido de arriba baja jalado.",
          "Cuando el vapor vuelve a ser agua, ¿ocupa más o menos espacio?"),
 (4, 1): ("Cómo se mide la solubilidad",
          "Se mide en gramos de soluto que caben en 100 g de agua, a una temperatura fija. A 20 °C caben "
          "unos 200 g de azúcar, unos 36 g de sal y unos 32 g de sulfato de cobre. Disolverse más rápido "
          "o a menos temperatura no es lo mismo que ser más soluble.",
          "¿La tabla dice cuánto se disolvió o a qué temperatura terminó de disolverse?"),
 (4, 6): ("Qué conduce la electricidad",
          "Para que pase corriente tiene que haber cargas que se puedan mover. En los metales y en el "
          "grafito se mueven electrones. La sal sólida tiene sus iones quietos: no conduce; disuelta en "
          "agua, los iones se sueltan y sí conduce. Conducir el calor es otra cosa.",
          "¿En este material hay algo con carga que se pueda mover?"),
 (5, 4): ("Polar y apolar",
          "Polar: una parte de la molécula jala más los electrones y queda con una carga parcial "
          "negativa, y otra parte con una positiva, como el agua. Lo polar se mezcla con lo polar (el "
          "azúcar en el agua) y lo apolar con lo apolar (la grasa en el aceite). Los grupos con oxígeno o "
          "nitrógeno suelen hacer polar una parte de la molécula.",
          "¿Esta molécula tiene oxígenos o nitrógenos que la hagan polar?"),
 (5, 7): ("Covalente polar e iónico",
          "En un enlace covalente los átomos comparten electrones; si uno los jala más (el oxígeno), es "
          "covalente polar: así es el éster del biodiésel. En un enlace iónico un átomo le entrega el "
          "electrón al otro y quedan dos iones, como en la sal (Na⁺Cl⁻).",
          "¿Los átomos comparten los electrones o uno se los quedó?"),
 (6, 2): ("Por mol o por gramo",
          "Un mol es una cantidad de moléculas, no una masa: un mol de gasolina pesa unos 114 g y uno de "
          "metano, 16 g. Por mol, la gasolina suelta más energía; por gramo, el metano suelta más "
          "(890 ÷ 16 ≈ 56 kJ/g frente a 5470 ÷ 114 ≈ 48 kJ/g). La pregunta del libro compara por mol.",
          "¿Comparamos la misma cantidad de moléculas o la misma masa?"),
 (6, 5): ("Polímero",
          "Una molécula larguísima hecha de una pieza pequeña (el monómero) que se repite, como un "
          "collar de cuentas. El almidón y la PVP del gel ya son polímeros. Al amasarlos no nace uno "
          "nuevo: sus cadenas se enredan y se atraen, y por eso la mezcla se estira.",
          "¿Se unieron piezas con enlaces nuevos o solo se enredaron cadenas que ya existían?"),
 (6, 8): ("Energía de enlace",
          "En una reacción unos enlaces se rompen (eso cuesta energía) y otros se forman (eso la libera). "
          "Si se libera más de lo que cuesta, sale calor y el termómetro sube: es exotérmica. En la "
          "neutralización, H⁺ + OH⁻ → H₂O: formar el agua libera energía.",
          "¿El termómetro subió o bajó? Entonces, ¿el calor salió o entró?"),
}

# ─────────── «Si Química no es tu fuerte»: cuatro conceptos por clase ───────────
NO_ES_TU_FUERTE = {
 1: [("Unidades y regla de tres",
      "Todo número de química trae unidad: g, mol, °C, atm, kPa. La regla de tres se arma con la unidad "
      "al lado de cada número; si arriba hay gramos, abajo también. Si la unidad no cuadra, la cuenta "
      "está mal aunque el número parezca bueno."),
     ("Mol y masa molar",
      "Un mol es una cantidad fija de partículas, como una docena pero enorme. La masa molar dice cuánto "
      "pesa un mol: se suman las masas de los átomos (C = 12, H = 1, O = 16). Para C₇H₆O₃: 7 · 12 + "
      "6 · 1 + 3 · 16 = 138 g/mol."),
     ("Solubilidad y saturación",
      "Cada sustancia tiene un tope de lo que se disuelve en cierta cantidad de agua a una temperatura. "
      "Lo que pasa del tope se queda sólido. Una disolución en el tope está saturada. Casi todos los "
      "sólidos se disuelven más en caliente; los gases, al revés."),
     ("La propiedad que identifica",
      "Una propiedad sirve para reconocer o separar una sustancia si las otras no la tienen: el imán "
      "atrae al hierro y no al azufre. La densidad, el punto de fusión, la solubilidad y el magnetismo "
      "son propiedades; el color o la forma del pedazo casi nunca bastan.")],
 2: [("Calor sensible y calor latente",
      "Calor sensible: sube la temperatura (Q = m · c · ΔT). Calor latente: cambia el estado sin subir "
      "la temperatura (Q = m · L). Por eso la gráfica tiene una meseta: mientras la sustancia se funde, "
      "el termómetro no se mueve."),
     ("Cambios de estado",
      "Fusión: de sólido a líquido. Ebullición: de líquido a gas. Sublimación: de sólido a gas sin pasar "
      "por líquido, como el hielo seco. Cada sustancia pura tiene su temperatura fija de fusión y de "
      "ebullición."),
     ("Partículas, temperatura y presión",
      "La temperatura dice qué tan rápido se mueven las partículas. Si un gas encerrado se calienta, sus "
      "partículas chocan más fuerte y más seguido contra las paredes: sube la presión. Un objeto muy "
      "caliente le pasa calor rápido al aire; cuando la diferencia es poca, despacio."),
     ("Densidad y flotación",
      "Densidad = masa ÷ volumen (g/cm³). Lo menos denso flota sobre lo más denso: el hielo (0,92) sobre "
      "el agua (1,00), el acero (7,9) sobre el mercurio (13,6). Lo que empuja hacia arriba es el empuje "
      "del líquido.")],
 3: [("Variable y testigo",
      "Para saber qué causó un efecto se cambia una sola cosa y lo demás se deja igual. El testigo es el "
      "vaso que no recibe el cambio. Si se cambian dos cosas a la vez, no se sabe cuál de las dos hizo "
      "la diferencia."),
     ("Mezcla homogénea y heterogénea",
      "Homogénea: se ve una sola fase, como el agua con sal. Heterogénea: se ven dos o más, como el aceite "
      "sobre el agua. Una mezcla inestable se separa sola en reposo, como el protector que forma gotas."),
     ("Gas, presión y temperatura",
      "Un gas encerrado empuja más si se calienta y menos si se enfría; si puede crecer, crece. Si el "
      "vapor se enfría tanto que vuelve a ser líquido, ocupa muchísimo menos y la presión cae: eso jala "
      "el líquido en la cafetera de sifón."),
     ("Cambio físico y cambio químico",
      "Físico: la sustancia sigue siendo la misma (disolver, filtrar, evaporar). Químico: aparece una "
      "sustancia nueva, y suele delatarse con un gas, un color, calor o un sólido que aparece. La tableta "
      "efervescente sí es un cambio químico: suelta CO₂.")],
 4: [("Comparación justa",
      "Dos resultados se comparan solo si todo lo demás fue igual: la misma agua, la misma temperatura, "
      "la misma cantidad. Si la carrera no fue pareja, la conclusión no vale."),
     ("Sedimentar, quedar suspendido, disolverse",
      "Las partículas grandes y densas se van rápido al fondo. Las muy finas se quedan flotando mucho "
      "tiempo: es una suspensión. Disolverse es otra cosa: la sustancia se separa en partículas tan "
      "pequeñas que no se ven."),
     ("Propiedades físicas que separan",
      "El imán separa lo magnético (el hierro). El tamiz separa por tamaño. El aire o la vibración "
      "separan por densidad: lo liviano para su tamaño se va. Ninguno de estos métodos cambia las "
      "sustancias."),
     ("Conducir la electricidad",
      "Conducen los materiales con cargas que se pueden mover: los metales y el grafito. Una sal sólida "
      "no conduce; disuelta en agua, sí. Conducir el calor y conducir la electricidad no son lo mismo.")],
 5: [("Grupo funcional",
      "La parte de la molécula que le da su manera de comportarse: –OH alcohol, –CHO aldehído, –COOH "
      "ácido, –COO– éster, –NH₂ amina, –CONH– amida. Dos moléculas con distinto grupo tienen propiedades "
      "distintas aunque pesen casi lo mismo."),
     ("Contar átomos en una ecuación",
      "En una reacción los átomos no se crean ni se destruyen: se reacomodan. Se cuenta cada elemento a "
      "cada lado de la flecha, multiplicando el número de adelante por el subíndice. Si cuadran, la "
      "ecuación está balanceada y la masa se conserva."),
     ("Combustión completa e incompleta",
      "Con oxígeno suficiente, un combustible de carbono se quema hasta CO₂ y agua. Si el oxígeno no "
      "alcanza, se queda a medias y salen CO, hollín o aldehídos. Lo que sale por el tubo depende de lo "
      "que entra y del oxígeno."),
     ("Lo que una tabla deja afirmar",
      "Perder masa no es desaparecer: el PLA pasó de 5,0 g a 3,8 g y el 76 % sigue ahí. Bajar no es "
      "eliminar. Palabras como «totalmente», «siempre» o «elimina» casi nunca las sostiene una tabla.")],
 6: [("La ecuación es una receta en moles",
      "En 4 Fe + 3 O₂ → 2 Fe₂O₃ los números de adelante dicen cuántos moles de cada uno. Para pasar a "
      "gramos se multiplica por la masa molar: Fe₂O₃ = 2 · 56 + 3 · 16 = 160 g/mol."),
     ("Exotérmica y endotérmica",
      "Exotérmica: la reacción suelta calor y el termómetro sube; se escribe con ΔH negativo. "
      "Endotérmica: absorbe calor y el termómetro baja; ΔH positivo. La combustión y la neutralización "
      "son exotérmicas."),
     ("Velocidad de reacción",
      "Una reacción va más rápido si se calienta, si los trozos son más pequeños (más superficie de "
      "contacto), si hay más concentración o si hay un catalizador. Cuando un reactivo se acaba, la "
      "reacción se detiene."),
     ("pH",
      "Escala de 0 a 14: menos de 7 es ácido, 7 es neutro y más de 7 es básico. Cuando un alimento se "
      "descompone, a menudo se vuelve más ácido y su pH baja.")],
}

PREGUNTA_AREA = "¿Qué número, con su unidad, o qué observación respalda eso?"
PROBLEMATIZADORA = {
 1: "¿Cuánto cabe, cuánto sobra, y qué número con su unidad lo dice?",
 2: "Si entra calor y el termómetro no se mueve, ¿en qué se gastó la energía?",
 3: "¿Qué cambió en este vaso que no cambió en el otro?",
 4: "¿Qué propiedad tiene una cosa que la otra no tiene, y qué herramienta la aprovecha?",
 5: "¿Qué parte de la molécula explica lo que hace, y qué átomos salen al otro lado?",
 6: "¿Qué dice la receta, salió o entró el calor, y alcanzan los datos para concluir?",
}

# Una observación corta y ORIGINAL para la activación: dos o tres renglones, sin nombres propios,
# algo que se observa, algo que se mide con su unidad y algo que hacen las partículas. Solo se lee
# o se proyecta: nada se hace con sustancias en el salón. La pista es para el final.
ACTIVACION = {
 1: ("En un vaso de agua fría se disuelven tres cucharadas de azúcar y la cuarta se queda en el fondo. "
     "Con la misma agua, pero caliente, se disuelven seis.",
     "se observó lo que se queda en el fondo; se midió en cucharadas; con agua caliente caben más "
     "partículas disueltas: hay un tope, y cambia con la temperatura"),
 2: ("Una olla de agua hierve en una ciudad de montaña. Se sube el fuego y el termómetro sigue marcando "
     "lo mismo: unos 92 °C.",
     "se observó que no subió; se midió en °C; el calor de más se gasta en volver vapor el agua, no en "
     "calentarla"),
 3: ("Dos vasos iguales con agua de la llave. En uno se echa una cucharada de sal y en el otro una de "
     "arena. Al rato, uno se ve transparente y el otro tiene el fondo lleno.",
     "se observó cuántas fases se ven; se mediría cuánto queda en el fondo, en gramos; la sal se "
     "separó en partículas que no se ven, la arena no"),
 4: ("Al barrer el salón, la arena se queda en el piso y el polvo fino flota en el aire un buen rato "
     "antes de caer.",
     "se observó qué cae y qué flota; se mediría el tamaño de cada grano y el tiempo que tarda en "
     "caer; lo grande y pesado cae rápido, lo finísimo se queda suspendido"),
 5: ("Una mancha de aceite en la camisa no sale con agua sola. Con un poco de jabón, sí.",
     "se observó qué sale y qué no; el aceite es apolar y el agua es polar: el jabón tiene una parte "
     "de cada uno y hace de puente"),
 6: ("En el botiquín hay dos bolsas que se activan al apretarlas: una se pone fría y la otra caliente. "
     "Las dos traen adentro dos sustancias que se mezclan.",
     "se observó frío o calor; se mediría en °C; en una el calor entra a la reacción (endotérmica) y en "
     "la otra sale (exotérmica)"),
}


# ─────────────────────── lo que ya está registrado ───────────────────────
def _instrumentos():
    """Las filas de Química de tablero/instrumentos.csv. La pregunta del entrenamiento viene como
    «A»…«D» (misiones 1 y 2) o «1»…«4» (3 a 6): se normaliza a 1…4."""
    from extrae_instrumentos import filas
    taller, icfes = {}, {}
    for a, mis, p, est, ins, ctx in filas():
        if a != AREA_CSV:
            continue
        es_icfes = "ICFES" in str(mis)
        k = int(str(mis).split()[0])
        n = "ABCD".index(p) + 1 if p in "ABCD" else int(p)
        (icfes if es_icfes else taller).setdefault(k, []).append((n, est, ins, ctx))
    for d in (taller, icfes):
        for k in d:
            d[k].sort()
    return taller, icfes


_META = re.compile(r"^(se omiten|se omite|figura|las cuatro|contexto|mismo contexto|tabla redibujada|"
                   r"estructuras del original|tabla 1)", re.I)


def _banco():
    """Las filas «QUI Mn» de icfes.csv, en el orden del cuaderno (P1…P4 = QA…QD). El contexto se
    queda con lo que dice la pregunta: las notas de formato («figura redibujada…») no van."""
    with open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig") as f:
        r = list(csv.DictReader(f))
    out = {}
    for x in r:
        m = x["mision"].strip()
        if not m.startswith("QUI M"):
            continue
        x = dict(x)
        partes = [p for p in x["contexto"].split(" · ") if not _META.match(p.strip())]
        x["contexto"] = re.sub(r"\s*\((tabla|gráfica|cuatro|objetos)[^)]*\)", "",
                               " · ".join(partes[:2])).strip()
        out.setdefault(int(m.replace("QUI M", "")), []).append(x)
    return out


def _comp_icfes():
    """La competencia de cada pregunta de entrenamiento: campo comp de QA…QD en quiN_icfes.py,
    leído con ast (sin importar el módulo, que reconfigura el motor del cuaderno)."""
    out = {}
    for m in range(1, 7):
        src = open(f"/home/claude/libro/qui{m}_icfes.py", encoding="utf-8").read()
        d = {}
        for n in ast.parse(src).body:
            if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") in ("QA", "QB", "QC", "QD"):
                kw = {k.arg: k.value for k in n.value.keywords}
                comp = ast.literal_eval(kw["comp"]).lower()
                d[n.targets[0].id] = next(c for t, c in _COD.items() if comp.startswith(t))
        out[m] = [d[q] for q in ("QA", "QB", "QC", "QD")]
    return out


TALLER, INS_ICFES = _instrumentos()
BANCO = _banco()
COMP_ICFES = _comp_icfes()


def _comp_est():
    """Cada estrategia toma la competencia de su pregunta de entrenamiento."""
    out = {}
    for m in range(1, 7):
        est = MISIONES[m]["estr"]
        out[m] = [None] * 4
        for (k, e, _, _), c in zip(INS_ICFES[m], COMP_ICFES[m]):
            out[m][est.index(e)] = c
    return out


COMP_EST = _comp_est()


def limpia(t):
    """Carlito no trae el glifo ⚠: la alerta se marca con color, no con el símbolo."""
    return t.replace("⚠ ", "").replace("⚠", "").strip()


def sellos_de(mis):
    return [s for s in SELLOS if str(s[1]) == str(mis)]


def comp_icfes(mis, k):
    """Competencia (UC, EF, IN) de la pregunta de entrenamiento k (1…4)."""
    return COMP_ICFES[mis][k - 1]


def verificar():
    """Lo que tiene que cuadrar antes de dibujar: claves del libro contra el docstring de quiN.py,
    claves del entrenamiento contra el docstring de quiN_icfes.py, la estrategia de cada pregunta
    contra las cuatro de la misión y las del EST de cada módulo, y la página de cada sello contra la
    hoja donde cae su pregunta. Devuelve la lista de diferencias."""
    malas = []
    for m in range(1, 7):
        src = open(f"/home/claude/libro/qui{m}.py", encoding="utf-8").read()
        ini = src.index('"""') + 3
        doc = src[ini:src.index('"""', ini)]
        lin = next(l for l in doc.split("\n") if re.match(r"\s+1·[A-D]\s", l))
        k = {int(n): c for n, c in re.findall(r"(\d+)·([A-D])", lin)}
        if k != CLAVES[m]:
            malas.append(f"M{m}: CLAVES {CLAVES[m]} · qui{m}.py {k}")
        est = re.findall(r'\d: \("([^"]+)", ', src[src.index("EST = {"):src.index("EST = {") + 400])
        if est != MISIONES[m]["estr"]:
            malas.append(f"M{m}: estrategias {MISIONES[m]['estr']} · qui{m}.py {est}")
        doc = open(f"/home/claude/libro/qui{m}_icfes.py", encoding="utf-8").read()[:4000]
        ki = dict(re.findall(r"Q([A-D])\s*·[^·\n]*·\s*([A-D])\b", doc))
        for j, q in enumerate("ABCD"):
            if ki.get(q) != BANCO[m][j]["clave"].strip():
                malas.append(f"M{m} P{j+1}: icfes.csv {BANCO[m][j]['clave']} · qui{m}_icfes.py {ki.get(q)}")
        for p, e, _, _ in TALLER[m] + INS_ICFES[m]:
            if e not in MISIONES[m]["estr"]:
                malas.append(f"M{m} · {p}: estrategia «{e}» no está en la misión")
        if len(TALLER[m]) != 10 or len(INS_ICFES[m]) != 4 or len(BANCO[m]) != 4:
            malas.append(f"M{m}: {len(TALLER[m])} del taller, {len(INS_ICFES[m])} y {len(BANCO[m])} ICFES")
        t_pags, _ = _paginas(m)
        for s in sellos_de(m):
            if t_pags[(s[3] - 1) // 2] != s[2]:
                malas.append(f"M{m}: el sello de la pregunta {s[3]} dice página {s[2]}")
    return malas


# ─────────────────────────── banco de dinámicas ───────────────────────────
# Isomorfas a la estrategia: lo que hace el cuerpo es el mismo movimiento que después hará la mente
# frente al dato. En Química el movimiento casi siempre es CONTAR (unidad frente a unidad, átomo por
# átomo), COMPARAR contra un tope o un testigo, o SEGUIR a las partículas. La E1 abre la clase (8');
# las otras tres van entre bloques del desarrollo guiado (6'). Ninguna usa el caso de una pregunta
# que viene después: se entrena el movimiento, no la respuesta.
# SEGURIDAD: ninguna usa sustancias reales, fuego ni calor. Solo el cuerpo, tarjetas, cinta, clips y
# el tablero; los objetos «calientes» o «densos» son tarjetas.
DINAMICAS = {
 1: [("La regla de tres de pie", 8,
      ["Dos columnas en el tablero, LO QUE SÉ y LO QUE BUSCO. El docente dicta: «12 pupitres pesan "
       "60 kg; ¿cuánto pesan 30?».",
       "Cuatro estudiantes pasan con una tarjeta cada uno: 12 pupitres, 60 kg, 30 pupitres y ¿? kg.",
       "Se paran pupitres frente a pupitres y kilos frente a kilos; si no, el grupo dice «no cuadra».",
       "Solo entonces se hace la cuenta, y el resultado se dice con su unidad: «150 kg», nunca «150»."],
      "Armar la regla de tres poniendo unidad frente a unidad antes de hacer la cuenta, y decir el "
      "resultado con su unidad. Es el movimiento de las preguntas 4, 7 y 9, y de la primera del "
      "entrenamiento (cuántos moles de amoníaco salen).",
      "Cuatro tarjetas por ronda · tablero"),
     ("El detective de la propiedad", 6,
      ["Cuatro estudiantes son sustancias; cada uno tiene en secreto tres datos: si el imán lo atrae, "
       "si flota y si se disuelve.",
       "El grupo solo hace preguntas de propiedad («¿te atrae el imán?») y anota las respuestas en una "
       "tabla.",
       "Tras cada pregunta dice si esa propiedad ya separa a alguno o si todos siguen iguales.",
       "Gana cuando cada sustancia tiene un código que no se repite, con el menor número de preguntas."],
      "Escoger la propiedad que deja a cada sustancia con un código distinto y descartar la que no "
      "separa nada. Es el movimiento de las preguntas 3, 6 y 8, y de la segunda del entrenamiento "
      "(las cuatro botellas sin marcar).",
      "Cuatro tarjetas de propiedades · tablero"),
     ("El vaso tiene tope", 6,
      ["Un cuadro de cinta en el piso es un vaso de agua: le caben seis estudiantes, que son el soluto "
       "disuelto.",
       "Entran de a uno; el séptimo no cabe y se queda al lado: es lo que queda en el fondo.",
       "«Calentamos»: el cuadro crece y caben nueve, como en casi todos los sólidos. Si los de adentro "
       "son un gas, el cuadro se achica y sobran.",
       "Antes de cada cambio, el grupo dice cuántos caben, cuántos hay, cuántos sobran y si quedó "
       "saturado."],
      "Comparar lo que hay contra el tope y ver que el tope cambia con la temperatura, al revés en "
      "sólidos y en gases. Es el movimiento de las preguntas 1, 2 y 5, y de la tercera del "
      "entrenamiento (la solubilidad de sólidos y gases a tres temperaturas).",
      "Cinta para el piso"),
     ("La colina de la reacción", 6,
      ["Una raya de cinta es la colina; ocho estudiantes en parejas, los reactivos, tienen que cruzarla.",
       "Para cruzar, una pareja choca las palmas y muestra una tarjeta de «empujón»; el docente reparte "
       "solo dos.",
       "Ronda uno: entran más parejas sin tarjeta. Ronda dos: todas tienen tarjeta (el catalizador).",
       "Se cuenta cuántas cruzan en treinta segundos, y el grupo dice qué faltaba y por qué agregar más "
       "de lo que sobraba no sirvió."],
      "Hacer la lista de lo que la reacción necesita y buscar lo que falta, en vez de agregar más de "
      "lo que ya sobra. Es el movimiento de la pregunta 10 (la aspirina lenta con reactivo sobrante) y "
      "de la cuarta del entrenamiento (la pareja de moléculas que sí hace jabón).",
      "Cinta · dos tarjetas de «empujón»")],
 2: [("El termómetro humano", 8,
      ["Cuatro estudiantes tomados de los brazos son un sólido; otro es el termómetro y sube el brazo "
       "con cada ficha de calor que entra.",
       "En el «punto de fusión», cada ficha suelta a una pareja y el brazo del termómetro NO sube.",
       "Cuando todos están sueltos (líquido), las fichas vuelven a subir el brazo.",
       "El grupo dibuja lo que hizo el brazo —subió, se quedó, subió— y dice en qué se gastaron las "
       "fichas del tramo plano."],
      "Leer la meseta: mientras cambia el estado, el calor entra y la temperatura no se mueve, porque "
      "se gasta en separar las partículas. Es el movimiento de las preguntas 1, 7 y 8, y de la primera "
      "del entrenamiento (lo que el alumno anotó y lo que nunca midió).",
      "Doce fichas de papel"),
     ("La factura en dos tramos", 6,
      ["Dos casillas en el tablero: TRAMO 1 · SUBIR LA TEMPERATURA y TRAMO 2 · CAMBIAR DE ESTADO.",
       "El docente cuenta: «un chocolate pasa de la nevera a la mano y se derrite»; los equipos ordenan "
       "los tramos.",
       "Un cajero pide para cada tramo los datos con su unidad —masa, grados, calor por gramo— y los "
       "escribe.",
       "La factura se suma solo si los dos tramos tienen sus unidades; si falta una, se devuelve."],
      "Partir el calor en tramos y sumarlos, con las unidades en cada uno: lo que sube la temperatura "
      "y lo que cambia el estado. Es el movimiento de las preguntas 2 y 4, y de la segunda del "
      "entrenamiento (la plancha que vuelve vapor el agua del tanque).",
      "Tablero"),
     ("Partículas en la cancha", 6,
      ["Diez estudiantes caminan dentro de un rectángulo de cinta; dos de afuera cuentan los toques a la "
       "cinta en veinte segundos.",
       "«Frío»: caminan despacio y tocan poco. «Caliente»: más rápido y tocan más: sube la presión.",
       "Cinco «calientes» entran entre cinco «fríos» y frenan un poco con cada toque: al principio "
       "mucho, al final casi nada.",
       "Cada cambio se explica con una frase de partículas, no con «porque sí»."],
      "Explicar lo que se mide afuera (la presión, lo rápido que algo se enfría) con lo que hacen las "
      "partículas adentro. Es el movimiento de las preguntas 3, 5 y 6, y de la tercera del "
      "entrenamiento (el agua que se enfría rápido al principio y despacio al final).",
      "Cinta · reloj con segundero"),
     ("La escalera de densidades", 6,
      ["Cinco tarjetas con densidades en g/cm³: aceite 0,92, agua 1,00, miel 1,40, hierro 7,9 y mercurio "
       "13,6.",
       "Quienes las tienen se ordenan como escalera: el más denso agachado, el menos denso en puntas.",
       "Otro recibe un objeto en tarjeta —corcho 0,24, canica 2,5, moneda 8,9— y se ubica donde "
       "quedaría.",
       "El grupo dice qué lo sostiene ahí (el empuje) y lo corrige si se pasó o se quedó corto."],
      "Comparar densidades, con su unidad, para decir qué queda arriba y qué abajo. Es el movimiento de "
      "las preguntas 9 y 10, y de la cuarta del entrenamiento (por qué el hielo flota en el agua).",
      "Ocho tarjetas con densidades")],
 3: [("Una perilla a la vez", 8,
      ["Tres estudiantes son perillas de un equipo de sonido: VOLUMEN, GRAVES y AGUDOS. El docente "
       "decidió en secreto cuál mejora la canción.",
       "Se mueven las tres al tiempo y el docente dice «mejor»: nadie puede saber cuál fue.",
       "Después se mueve una sola y las otras se quedan quietas, una ronda por perilla.",
       "El grupo arma una tabla —qué cambió, qué quedó igual, qué pasó— y nombra la perilla que manda."],
      "Cambiar una sola variable a la vez y dejar las demás quietas, para saber cuál produce el efecto. "
      "Es el movimiento de las preguntas 1, 3 y 4, y de la primera del entrenamiento (qué "
      "concentración mueve más la velocidad).",
      "Ninguno · tablero"),
     ("¿Cuántas fases ves?", 6,
      ["El docente dibuja seis frascos: agua con sal, agua con aceite, granola con leche, jugo con pulpa, "
       "café colado y agua con arena.",
       "Con los dedos, cada uno muestra cuántas fases se ven. Vale lo que se ve, no lo que se sabe.",
       "«Cinco minutos quietos»: el grupo dice cuáles se separan solas.",
       "Junto a cada frasco va un número inventado de «transparencia» (0 a 10): ¿entre qué números "
       "quedaron los de una fase?"],
      "Clasificar por lo que se observa —cuántas fases, si se separa en reposo— y leer el rango de "
      "números que le toca a cada grupo. Es el movimiento de las preguntas 5 y 7, y de la segunda del "
      "entrenamiento (el rango de pH de las sustancias neutras).",
      "Seis dibujos en el tablero"),
     ("El émbolo humano", 6,
      ["Diez estudiantes caminan dentro de un rectángulo de cinta; dos más sostienen una cuerda en un "
       "lado: es la tapa que se corre.",
       "«Calentamos»: caminan más rápido, empujan la cuerda y la tapa se corre. ¿Qué pasó con el volumen?",
       "«Tapa fija y calentamos»: la cuerda no se mueve y los que la sostienen sienten más empujones.",
       "Antes de cada orden, el grupo predice qué cambia, el volumen o la presión, y lo comprueba."],
      "Seguir al gas: si se calienta y puede crecer, crece; si no puede, empuja más. Es el movimiento de "
      "las preguntas 6, 8 y 9, y de la tercera del entrenamiento (el volumen del gas al doblar la "
      "temperatura).",
      "Cinta · una cuerda"),
     ("¿Dónde está la prueba?", 6,
      ["Caso inventado: «dos matas iguales; a una le pusimos música y creció más».",
       "Tres rincones: PASÓ SOLO EN LA DE MÚSICA, PASÓ EN LAS DOS y ESO NO PRUEBA NADA.",
       "El docente lee evidencias —«las dos recibieron agua», «la de música midió 3 cm más», «la de "
       "música estaba junto a la ventana»— y cada uno camina a un rincón.",
       "Solo es prueba lo que pasó en la mata con música y no en la otra, con todo lo demás igual."],
      "Pedir la evidencia antes de creer: algo que pasa donde está el cambio y no en el testigo. Es el "
      "movimiento de las preguntas 2 y 10, y de la cuarta del entrenamiento (la gráfica que esperaría "
      "la hipótesis).",
      "Tres letreros")],
 4: [("La carrera que no fue pareja", 8,
      ["Dos estudiantes hacen una carrera caminando; en secreto, uno sale dos pasos adelante y el otro "
       "carga dos maletas.",
       "El docente pregunta quién camina más rápido, y el grupo responde con el resultado.",
       "El docente revela las ventajas; el grupo lista lo que fue distinto además de quién caminaba.",
       "Se repite con todo igual, y el grupo dice por qué la primera carrera no servía para concluir."],
      "Antes de comparar dos resultados, revisar que todo lo demás haya sido igual; si no, la "
      "comparación no deja concluir. Es el movimiento de las preguntas 1 y 5, y de la primera del "
      "entrenamiento (dos moléculas del mismo peso con fuerzas distintas).",
      "Dos maletas · pasillo despejado"),
     ("Fondo, medio o superficie", 6,
      ["Tres letreros en la pared, de abajo arriba: FONDO, SUSPENDIDO y SUPERFICIE. El salón es un frasco.",
       "Cada uno recibe una tarjeta de partícula: más o menos densa que el líquido, y grande, mediana o "
       "finísima.",
       "Se para bajo el letrero donde quedaría al cabo de un minuto.",
       "El docente pregunta qué dato de la tarjeta lo mandó ahí: la densidad, el tamaño o los dos."],
      "Decidir si algo se hunde, flota o queda suspendido con dos datos: su densidad frente al líquido "
      "y el tamaño de la partícula. Es el movimiento de las preguntas 2, 3 y 4, y de la segunda del "
      "entrenamiento (el corcho en tres líquidos).",
      "Tarjetas de partícula · tres letreros"),
     ("El nombre exacto", 6,
      ["Cada equipo tiene cinco tarjetas: DENSIDAD (g/cm³), MASA (g), PUNTO DE EBULLICIÓN (°C), "
       "CONDUCTIVIDAD ELÉCTRICA y MAGNETISMO.",
       "El docente describe sin nombrar: «el aceite queda encima del vinagre», «el cable de cobre lleva "
       "la corriente».",
       "Cada equipo levanta la tarjeta de la propiedad que muestra la situación.",
       "Cuenta solo si dice la unidad o qué partícula lo explica; si no, baja la tarjeta."],
      "Ponerle a cada fenómeno el nombre exacto de la propiedad, con su unidad, y no uno que suena "
      "parecido. Es el movimiento de las preguntas 6, 7 y 9, y de la tercera del entrenamiento (los "
      "títulos de dos columnas de una tabla).",
      "Cinco tarjetas de propiedades por equipo"),
     ("Cada herramienta, su propiedad", 6,
      ["En la mesa, tarjetas con herramientas: IMÁN, COLADOR, VENTILADOR, EMBUDO DE DECANTACIÓN y "
       "FILTRO DE PAPEL.",
       "El docente dice una mezcla inventada: «clips con arroz», «piedritas en harina», «aceite con agua».",
       "Un estudiante escoge la herramienta y nombra la propiedad: «el imán, por el magnetismo».",
       "Si una herramienta ya falló con esa mezcla se tacha, y se pasa a otra propiedad."],
      "Unir cada método de separación con la propiedad física que aprovecha, y descartar lo que ya "
      "falló. Es el movimiento de las preguntas 8 y 10, y de la cuarta del entrenamiento (qué objeto "
      "mueve el carro con el imán).",
      "Cinco tarjetas de herramientas")],
 5: [("La pieza que cambia todo", 8,
      ["Cinco estudiantes tomados de los hombros son una cadena de carbonos que no cambia.",
       "El docente le pone al último una tarjeta: –OH, –CHO, –COOH o ninguna.",
       "Con cada tarjeta, el grupo dice si esa punta queda polar o apolar y si se llevaría bien con el "
       "agua: solo mira la tarjeta.",
       "Al final la cadena se alarga con tres más y el grupo discute qué pesa más: la cadena o la punta."],
      "Ir del grupo funcional a la propiedad: con la misma cadena, lo que cambia es la pieza de la "
      "punta. Es el movimiento de las preguntas 4, 5 y 7, y de la primera del entrenamiento (qué "
      "compuesto hierve a más temperatura).",
      "Cuatro tarjetas de grupos funcionales"),
     ("Las mismas fichas a cada lado", 6,
      ["Cada equipo recibe nueve fichas de papel: una negra (C), cuatro blancas (H) y cuatro rojas (O).",
       "Arman la izquierda de la ecuación que dicta el docente: CH₄ + 2 O₂ → CO₂ + 2 H₂O.",
       "Desarman y, con las MISMAS fichas, arman la derecha. No se pide ni se bota ninguna.",
       "Si falta o sobra una, la ecuación no estaba balanceada: cuentan elemento por elemento."],
      "Contar los átomos de cada elemento a cada lado de la flecha: se reacomodan, no se pierden. Es el "
      "movimiento de las preguntas 2 y 8, y de la tercera del entrenamiento (la masa del ácido "
      "carbónico, átomo por átomo).",
      "Nueve fichas de tres colores por equipo"),
     ("¿La tabla lo dice?", 6,
      ["En el tablero, tres jabones de 100 g y lo que queda tras un mes en la ducha: 70 g, 55 g y 90 g.",
       "El docente lee: «el 2 se gastó más», «el 2 desapareció», «el 3 nunca se gasta», «el 1 limpia "
       "mejor».",
       "Cada uno se para a un lado de una línea: LA TABLA LO DICE o LA TABLA NO LO DICE.",
       "Para quedarse en LO DICE, señala la fila y el número; «desapareció», «nunca» y «mejor» se "
       "discuten."],
      "Afirmar solo lo que los números permiten, sin palabras absolutas que la tabla no sostiene. Es el "
      "movimiento de las preguntas 3, 6 y 9, y de la segunda del entrenamiento (cuál de dos materiales "
      "es menos denso).",
      "Tablero · cinta"),
     ("Lo que entra y lo que sale", 6,
      ["La puerta es el motor. Los que entran llevan tarjetas: CARBONO, HIDRÓGENO, AZUFRE y OXÍGENO.",
       "Con oxígeno de sobra, cada CARBONO sale con dos OXÍGENO (CO₂) y el AZUFRE, con dos (SO₂).",
       "Con la mitad del oxígeno, algunos CARBONO salen con uno solo (CO) o solos (hollín).",
       "Si el AZUFRE no entra, el grupo dice qué deja de salir: lo que no entra no puede salir."],
      "Explicar lo que sale del tubo de escape con lo que entra al motor y con el oxígeno que alcanza. "
      "Es el movimiento de las preguntas 1 y 10, y de la cuarta del entrenamiento (por qué conviene un "
      "combustible sin azufre).",
      "Tarjetas de elementos")],
 6: [("La receta del sánduche", 8,
      ["En el tablero, una receta como ecuación: 2 panes + 1 queso + 1 jamón → 1 sánduche.",
       "Cada equipo recibe tarjetas —siete panes, cuatro quesos, dos jamones— y arma todos los "
       "sánduches que pueda.",
       "Dicen cuántos salieron, qué se acabó primero y qué sobró: lo que se acaba primero detiene todo.",
       "Con la receta doble, comprueban que todo se dobla en la misma proporción."],
      "Leer la ecuación como una receta: los números de adelante dicen cuánto de cada uno, lo que se "
      "acaba primero detiene la reacción y, si la receta se dobla, todo se dobla. Es el movimiento de "
      "las preguntas 1, 3 y 9, y de la primera del entrenamiento (protones y electrones del ion Mg²⁺).",
      "Tarjetas de panes, quesos y jamones"),
     ("Las manos del calor", 6,
      ["El docente lee: «la bolsa de calor del botiquín se calienta», «el hielo se derrite en la mano», "
       "«el sudor se evapora de la piel».",
       "Si el calor SALE de lo que cambia, manos hacia el frente; si ENTRA, manos al pecho.",
       "Un estudiante dice qué marcaría un termómetro al lado: sube o baja.",
       "En el tablero: sale calor, ΔH negativo; entra, positivo. Se compara cuánto sale por el tamaño "
       "del número."],
      "Decidir si el calor sale o entra mirando el termómetro y el signo, y comparar cuánto sale por el "
      "tamaño del número. Es el movimiento de las preguntas 2 y 8, y de la segunda del entrenamiento "
      "(qué azúcar suelta más energía al quemarse).",
      "Tablero"),
     ("¿Alcanza para concluir?", 6,
      ["En el tablero: «una estudiante durmió 8 horas y sacó 4,5; un compañero durmió 5 y sacó 3,8».",
       "El docente lee: «dormir más sube la nota», «siempre la sube un punto», «en estos dos casos, quien "
       "durmió más sacó más».",
       "Con los dedos, cada uno muestra cuántas mediciones usa cada conclusión; mano abierta si "
       "necesitaría muchas más.",
       "Se quedan con la que no pide más datos de los que hay, y nombran otra cosa que pudo cambiar."],
      "Pesar una conclusión contra los datos que la sostienen: cuántas mediciones, qué variable cambió "
      "y qué palabras se pasan («siempre», «suficiente»). Es el movimiento de las preguntas 4, 7 y 10, y "
      "de la tercera del entrenamiento (qué concluir de los tiempos de reacción).",
      "Tablero"),
     ("El collar de clips", 6,
      ["Cada equipo encadena veinte clips (o tiras de papel): cada clip es un monómero y el collar, el "
       "polímero.",
       "Dicen qué hace el collar que un clip suelto no hacía: se estira, se enreda, se puede jalar.",
       "Dos equipos enredan sus collares sin abrir ningún clip: ¿es un collar nuevo o dos enredados?",
       "El grupo escribe que unir piezas con enlaces nuevos no es lo mismo que enredar cadenas."],
      "Ver el polímero como una pieza que se repite, y separar unir piezas de enredar cadenas que ya "
      "existían. Es el movimiento de las preguntas 5 y 6, y de la cuarta del entrenamiento (de dónde "
      "salen las piezas del plástico).",
      "Veinte clips o tiras de papel por equipo")],
}

RETOS = {
 1: ("La sal de la cocina", 20,
     "A 20 °C caben 36 g de sal en 100 g de agua, y en la cocina echan 50 g. En doce minutos cada equipo "
     "calcula cuánta sal queda en el fondo, con la unidad en cada paso; dice si el agua quedó saturada y "
     "qué lo demuestra; nombra la propiedad que separa la sal del fondo, y escoge entre agregar agua, "
     "calentar o agitar para disolverla toda. Cada uno escribe su cuenta. (Docente: quedan 14 g; agitar "
     "solo apura y calentar casi no cambia el tope de la sal: sirve agregar unos 39 g de agua.)"),
 2: ("La paleta que se derrite", 20,
     "Una paleta de hielo de 100 g sale del congelador a −10 °C (hielo: 2,1 J/(g·°C); fundirlo: 334 J/g). "
     "En doce minutos cada equipo dibuja la gráfica de temperatura que espera y marca la meseta, calcula "
     "el calor de los dos tramos hasta tener agua a 0 °C, explica cada tramo con partículas y dice qué "
     "queda arriba si se echa un cubo de hielo en esa agua. Cada uno escribe su cuenta con unidades. "
     "(Docente: 2.100 J + 33.400 J = 35.500 J.)"),
 3: ("El jugo en polvo", 20,
     "Cada equipo diseña en papel —no se hace en el salón— un experimento para saber si el agua caliente "
     "disuelve más rápido el jugo en polvo que la fría: qué cambia y qué se deja igual, qué se mide y con "
     "qué unidad, cuál es el vaso testigo, cómo se clasifica la mezcla por lo que se ve y qué tendrían "
     "que observar para hablar de una reacción química. Cada uno escribe la única variable que cambia."),
 4: ("La mezcla del recreo", 20,
     "Cada equipo recibe en papel una mezcla para separar sin agua ni químicos: arena fina, clips, aserrín "
     "y piedritas. En doce minutos escriben la propiedad que distingue a cada componente, ordenan los "
     "métodos —imán, tamiz, soplar, bandeja que vibra—, dicen qué sale en cada paso y por qué dos métodos "
     "solo se comparan con la misma mezcla. Cada uno defiende un paso y escribe la propiedad que aprovecha."),
 5: ("El bus a gas", 20,
     "Una ciudad quiere cambiar buses de diésel por buses de gas natural (metano, CH₄). En doce minutos "
     "cada equipo cuenta los átomos de CH₄ + 2 O₂ → CO₂ + 2 H₂O a cada lado, dice qué saldría del tubo si "
     "el oxígeno no alcanza, inventa la tabla que medirían en los dos buses con una afirmación que permite "
     "y otra que no, y dice si el metano es polar. Cada uno cierra: «Los átomos no se pierden, porque ___»."),
 6: ("La bolsa de calor del botiquín", 20,
     "Una bolsa de calor trae hierro que se oxida con el aire (4 Fe + 3 O₂ → 2 Fe₂O₃). En doce minutos "
     "cada equipo calcula cuánto óxido sale de 28 g de hierro (Fe = 56 g/mol, O = 16 g/mol), dice si es "
     "exotérmica y qué dato lo prueba, escribe una conclusión que sostiene una sola bolsa y otra que "
     "pide muchas, y dice qué pieza se repite en el plástico de la bolsa. (Docente: 40 g; el plástico es "
     "polietileno y la pieza, el etileno.)"),
}


# ─────────────────────────────── hojas ───────────────────────────────
OUTP = OUT + "plan_qui_"


def _cajas_hilo(b, y):
    cajas = [("LIBRO", "tiene la pregunta", GRAY), ("CUADERNO", "tiene el andamiaje para resolverla", QUI),
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
    y = cabecera(b, "Química", "Planeador del área · las ocho clases",
                 derecha="8", dsub="clases de 120 min", campos=True)
    y = seccion(b, y, "Para qué existe este documento")
    y = parrafo_j(b, M, y,
        "La calidad de la clase no puede depender de qué profesor llegue ese sábado. Por eso el "
        "método de EDUCATE no vive en el profesor: vive en el cuaderno del estudiante. Este "
        "planeador no te pide saber química de memoria; te dice qué hacer con el libro y con el "
        "cuaderno en cada uno de los 120 minutos, y dónde termina lo fijo y empieza tu aporte.",
        CW, 26) + 24
    y = _cajas_hilo(b, y) + 30
    y = nota(b, M, y, CW,
        "Casi ninguna pregunta de Química se resuelve recordando una fórmula. Se resuelve preguntando "
        "qué se observó, qué se midió y con qué unidad, y qué hacen las partículas. Es el instrumento "
        "que el estudiante encuentra en la portada del área, en la página 182: un número sin unidad no "
        "dice nada, y una partícula que no sabe dibujar todavía es solo una palabra. Un estudiante que "
        "acierta con el instrumento vacío no aprendió la estrategia: adivinó, y en la prueba real no va "
        "a tener a quién preguntarle.",
        QUI, QUI_BG, QUI_LN, "El instrumento de pensamiento del área: la partícula y su unidad", 25) + 30
    y = seccion(b, y, "El área en números")
    na = sum(len(v) for v in AVISOS.values())
    cif = [("43", "páginas del cuaderno\\ncon la portada", QUI), ("60", "preguntas del libro\\ncon su instrumento", QUI),
           ("24", "preguntas tipo\\nSaber 11", "#1F4E8C"), (str(len(SELLOS)), "sellos «aquí entra\\nel profe»", ORO),
           (str(na), "avisos del libro\\nantes de entrar", ROJO)]
    an2 = (CW - 4 * 18) / 5
    for i, (v, l, c) in enumerate(cif):
        x = M + i * (an2 + 18)
        b.append(rect(x, y, an2, 140, "white", r=16, stroke=QUI_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, 112, c, r=3))
        b.append(T(x + 38, y + 64, [v], 50, c, weight="700"))
        for j, ln in enumerate(l.split("\\n")):
            b.append(T(x + 38, y + 98 + j * 26, [ln], 20, GRAY))
    y += 140 + 30
    y = seccion(b, y, "Las tres competencias que evalúa la prueba de Ciencias Naturales")
    comp = [("UC", "Uso comprensivo del conocimiento científico", "usar conceptos y modelos de la "
             "química (partículas, moles, propiedades) para entender una situación"),
            ("EF", "Explicación de fenómenos", "explicar lo que se observa con lo que hacen "
             "las partículas, y juzgar si una explicación alcanza"),
            ("IN", "Indagación", "cambiar una sola variable, comparar contra un "
             "testigo y sacar solo la conclusión que los datos permiten")]
    an3 = (CW - 2 * 18) / 3
    alt3 = 52 + max(len(wrap_px(t + ": " + d, 22, an3 - 70)) for _, t, d in comp) * 31 + 20
    for i, (cod, t, d) in enumerate(comp):
        x = M + i * (an3 + 18)
        b.append(rect(x, y, an3, alt3, QUI_BG, r=16, stroke=QUI_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt3 - 28, QUI, r=3))
        b.append(T(x + 40, y + 44, [cod], 26, QUI, weight="700"))
        parrafo_j(b, x + 40, y + 54, t + ": " + d, an3 - 70, 22, INK, lh=31)
    y += alt3 + 30
    y = nota(b, M, y, CW,
        "Ninguna dinámica de este planeador usa sustancias, fuego ni calor de verdad: todo se hace con el "
        "cuerpo, tarjetas, cinta, clips y el tablero, y los experimentos de los retos se diseñan en papel. "
        "Si un estudiante propone «hagámoslo de verdad», la respuesta en el salón es no. Y cuatro claves "
        "del libro son discutibles (misión 3, pregunta 9; misión 5, pregunta 10; misión 6, preguntas 5 y "
        "6): están en la hoja de su clase.",
        ROJO, ROJO_BG, ROJO_LN, "Antes de empezar el área", 23) + 28
    y = nota(b, M, y, CW,
        "No necesitas ser químico. La segunda hoja de cada clase trae los cuatro conceptos que tienes "
        "que poder explicar en dos minutos, y el cuaderno marca con un sello «Alto · aquí entra el "
        "profe» las once preguntas donde el estudiante no puede seguir sin ti. Lo demás lo resuelve el "
        "instrumento: qué se observó, qué se midió y con qué unidad, qué hacen las partículas.",
        VERDE, VERDE_BG, VERDE_LN, "Si Química no es tu fuerte", 23) + 28
    y = seccion(b, y, "Lo que la coordinación revisa, sin haber entrado a la clase",
        "Tres cuadernos al azar del grupo. No se mira si la respuesta está buena: se mira si el "
        "instrumento está lleno. Marca tú mismo esta lista al terminar el sábado.")
    rev = ["El instrumento de pensamiento está lleno en las diez preguntas, acertadas o no.",
           "«Mi primera idea, antes de hacer nada» tiene algo escrito en todas las preguntas.",
           "Los sellos «Alto · aquí entra el profe» tienen escrito «lo que explicó, en mis palabras».",
           "Las dos caritas de la clase están marcadas y la clase está anotada en la portada del área."]
    b.append(rect(M, y, CW, 34 + len(rev) * 50, "white", r=18, stroke=QUI_LN, sw=2))
    b.append(rect(M + 14, y + 16, 5, 2 + len(rev) * 50, QUI, r=3))
    yy = y + 34
    for r_ in rev:
        b.append(checkbox(M + 44, yy - 14, 13, QUI))
        parrafo_j(b, M + 100, yy - 22, r_, CW - 150, 23, INK)
        yy += 50
    pie(b, 1)
    svg_close(b, OUTP + "01.svg")


def h2():
    b = svg_open()
    y = cabecera(b, "Las ocho clases", "Mapa del área de un vistazo", derecha="43",
                 dsub="páginas del cuaderno")
    y = seccion(b, y, "Qué se ve en cada sábado",
        "Seis clases de contenido, una por momento, y dos para el simulacro del área. El número "
        "de clases es fijo: no se recorta aunque un momento quede largo.")
    colx = [M, M + 120, M + 700, M + 1110, M + 1450]
    y = encabezado_tabla(b, y, list(zip(colx, ["CLASE", "QUÉ SE TRABAJA", "ÉNFASIS",
                                                "PARA EL PROFE", "ENTRENAMIENTO"])), 54)
    y += 2
    for n, (mis, tit, sub) in enumerate(CLASES, 1):
        alto = 96
        bg = "white" if mis else ORO_BG
        ln = QUI_LN if mis else ORO_LN
        c = QUI if mis else ORO
        b.append(rect(M, y, CW, alto, bg, r=14, stroke=ln, sw=2))
        b.append(rect(M + 12, y + 12, 5, alto - 24, c, r=3))
        b.append(T(colx[0] + 44, y + 62, [str(n)], 42, c, weight="700", anchor="middle"))
        b.append(T(colx[1] + 20, y + 44, [tit], 24, INK, weight="700"))
        b.append(T(colx[1] + 20, y + 74, [sub], 20, GRAY, style="italic"))
        if mis:
            d = MISIONES[mis]
            cod, de = d["competencia"].split(" · ")
            b.append(T(colx[2] + 20, y + 44, [cod], 23, QUI, weight="700"))
            b.append(T(colx[2] + 20, y + 74, [de], 19, GRAY))
            ns, na = len(sellos_de(mis)), len(AVISOS.get(mis, []))
            tx = {0: "sin sellos", 1: "1 sello"}.get(ns, f"{ns} sellos")
            b.append(T(colx[3] + 20, y + 46, [f"{tx} · {na} avisos"], 22, INK, weight="700"))
            b.append(T(colx[3] + 20, y + 76, ["para preparar antes"], 19, GRAY))
            b.append(T(colx[4] + 20, y + 46, [f"{len(BANCO.get(mis, []))} tipo Saber 11"],
                       22, "#1F4E8C", weight="700"))
            b.append(T(colx[4] + 20, y + 76, [f"páginas {BASE[mis]+2} y {BASE[mis]+6}"], 19, GRAY))
        else:
            b.append(T(colx[2] + 20, y + 58, ["UC · EF · IN"], 23, GRAY))
            b.append(T(colx[3] + 20, y + 58, ["todo el área"], 22, GRAY))
            b.append(T(colx[4] + 20, y + 58, ["24 ya resueltas"], 22, GRAY))
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
        b.append(rect(x, yy0, an, alto, QUI_BG, r=16, stroke=QUI_LN, sw=2))
        b.append(rect(x + 14, yy0 + 14, 5, alto - 28, QUI, r=3))
        b.append(T(x + 40, yy0 + 44, [f"Misión {m} · {d['comp']}"], 22, QUI, weight="700"))
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


def _pag_libro(mis, p):
    return PAG_LIBRO[mis][p - 1]


def _rot_sello(preg):
    return f"preg. {preg}" if isinstance(preg, int) else str(preg)


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
    alt = max(52 + len(wrap_px(e, 23, an - 60, "700")) * 32 for e in d["estr"])
    for i, e in enumerate(d["estr"]):
        x = M + i * (an + 16)
        b.append(rect(x, y, an, alt, "white", r=16, stroke=QUI_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt - 28, cols[i], r=3))
        b.append(T(x + 38, y + 40, [f"ESTRATEGIA {i+1} · {COMP_EST[mis][i]}"], 16, cols[i],
                   weight="700", ls=1.3))
        # el nombre de la estrategia es un rótulo, no un párrafo corrido: va sin justificar
        for j, ln in enumerate(wrap_px(e, 23, an - 60, "700")):
            b.append(T(x + 38, y + 50 + 23 + j * 32, [" ".join(ln)], 23, INK, weight="700"))
    y += alt + 26
    y = nota(b, M, y, CW, d["instala"], ORO, ORO_BG, ORO_LN,
             "Lo que tienes que instalar antes del taller", 24) + 22
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
            b.append(T(M + 36, y + h / 2 + 8, [f"pág. {pag} · {_rot_sello(preg)}"], 21, ORO, weight="700"))
            parrafo_j(b, M + 290, y + (h - len(lin) * 30) / 2 - 4, saber, CW - 330, 22, INK, lh=30)
            y += h + 6
        y += 18
    else:
        y = nota(b, M, y, CW,
            "Esta misión no tiene sellos «Alto · aquí entra el profe»: los conceptos que hacen falta "
            "están en la hoja siguiente, en «Si Química no es tu fuerte».",
            VERDE, VERDE_BG, VERDE_LN, "Sin sellos en esta clase", 22) + 24
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
        b.append(rect(M, y, CW, h, QUI_BG if p <= 2 else "white", r=10, stroke=QUI_LN, sw=1.6))
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


def hoja_clase_b(mis):
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Clase {mis} · minuto a minuto", "El sábado, los conceptos y la evaluación",
                 derecha="120", dsub="minutos")
    t_pags, i_pags = _paginas(mis)
    ins = {p: i for p, e, i, c in TALLER.get(mis, [])}
    din = DINAMICAS[mis]
    sel = ", ".join(str(s[3]) for s in sellos_de(mis) if isinstance(s[3], int))
    caso, pista = ACTIVACION[mis]
    concreto = [
        f"Observación proyectada, sin contexto: «{caso}» Qué se observó, qué se midió y con qué "
        f"unidad, qué hacen las partículas. Dinámica E1 «{din[0][0]}» ({din[0][1]}'). Pista para el cierre del momento: {pista}.",
        f"Pregunta modelo: la 1 del libro (página {PAG_LIBRO[mis][0]}), a la vista todo el momento. "
        f"Manos alzadas antes de releer. La pregunta del momento: {PROBLEMATIZADORA[mis]} Se abre la "
        f"página {t_pags[0]} solo en «mi primera idea».",
        f"1-2 en pantalla (página {t_pags[0]}, «{ins.get(1, '—')}» y «{ins.get(2, '—')}»); 3-4, 5-6, "
        f"7-8 y 9-10 en las páginas {t_pags[1]}, {t_pags[2]}, {t_pags[3]} y {t_pags[4]}. Entre "
        f"bloques, las dinámicas E2, E3 y E4."
        + (f" Sello en {'la pregunta' if ',' not in sel else 'las preguntas'} {sel}." if sel else ""),
        f"Reto del corte: «{RETOS[mis][0]}». Equipos de tres; cada uno registra en SU tarjeta. La "
        f"defensa nombra el dato con su unidad, la cuenta o la propiedad.",
        f"Entrenamiento, páginas {i_pags[0]} y {i_pags[1]}. Cuatro preguntas tipo Saber 11, en "
        f"silencio y con reloj.",
        f"Solo las falladas, con el dato, la cuenta o la propiedad que las resuelve. «Palabras que me frenaron», "
        f"«lo que me llevo», carita de salida y la clase {mis} en la portada del área.",
    ]
    y = seccion(b, y, "El sábado, minuto a minuto",
        "Las seis fases con el contenido de este momento puesto encima.")
    reloj = 0
    for (nom, mins, c, *_), txt in zip(FASES, concreto):
        lin = wrap_px(txt, 21, CW - 440)
        h = max(70, 24 + len(lin) * 29)
        b.append(rect(M, y, CW, h, "white", r=14, stroke=QUI_LN, sw=1.8))
        b.append(rect(M + 12, y + 12, 5, h - 24, c, r=3))
        b.append(T(M + 40, y + h / 2 - 2, [f"{reloj:02d}'–{reloj+mins:02d}'"], 22, c, weight="700"))
        b.append(T(M + 40, y + h / 2 + 26, [nom], 19, GRAY))
        parrafo_j(b, M + 400, y + (h - len(lin) * 29) / 2 - 5, txt, CW - 440, 21, INK, lh=29)
        reloj += mins
        y += h + 6
    y += 20
    y = seccion(b, y, "Si Química no es tu fuerte",
        "Lo que tienes que poder explicar en dos minutos, sin jerga. Si un estudiante sabe más que "
        "tú de un tema, déjalo explicar y pide que señale en el texto o en la gráfica de dónde lo saca.",
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
    banco = BANCO.get(mis, [])
    y = seccion(b, y, "Las cuatro preguntas de entrenamiento y su clave",
        "Van con el membrete «Pregunta Saber 11», sin año. Claves verificadas resolviendo cada "
        "pregunta; el texto completo y por qué cae cada opción están en la guía de clase.")
    for k, (x4, est, ins_, ctx) in enumerate(INS_ICFES.get(mis, [])):
        fila = banco[k] if k < len(banco) else {}
        ctx_ = fila.get("contexto", "—")
        i_est = d["estr"].index(est) if est in d["estr"] else 0
        cc = COLS_MIS[mis][i_est]
        l_c = wrap_px(ctx_, 20, 620, "700")
        l_i = wrap_px(ins_, 19, 640, style="italic")
        h = max(62, 20 + max(len(l_c), len(l_i)) * 28)
        b.append(rect(M, y, CW, h, "white", r=12, stroke=QUI_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, h - 20, cc, r=2))
        b.append(T(M + 36, y + h / 2 - 3, [f"P{x4}"], 21, cc, weight="700"))
        b.append(T(M + 36, y + h / 2 + 20, [f"pág. {i_pags[0] if x4 <= 2 else i_pags[1]}"], 16, GRAY))
        b.append(T(M + 150, y + h / 2 + 8, [f"E{i_est+1} · {comp_icfes(mis, x4)}"], 18, cc, weight="700"))
        parrafo_j(b, M + 290, y + (h - len(l_c) * 28) / 2 - 4, ctx_, 620, 20, INK, weight="700", lh=28)
        parrafo_j(b, M + 940, y + (h - len(l_i) * 28) / 2 - 4, ins_, 640, 19, GRAY, style="italic", lh=28)
        cl = fila.get("clave", "").strip()
        b.append(rect(W - M - 96, y + h / 2 - 22, 64, 44, QUI_BG, r=10, stroke=QUI, sw=2))
        b.append(T(W - M - 64, y + h / 2 + 10, [cl or "—"], 26, QUI, weight="700", anchor="middle"))
        y += h + 6
    y += 22
    y = seccion(b, y, "Después de la clase · tu registro",
        "Se llena el mismo sábado, antes de salir. Esto no lo ve el estudiante.")
    alto_reg = int(min(232, (2470 - y - 14) / 2))
    registro_docente(b, y, alto=alto_reg, campos=[
        ("¿Qué cuenta o qué concepto hubo que explicar dos veces?", "y con qué ejemplo funcionó la segunda"),
        ("¿A quién hay que volver la próxima clase?", "nombres, no «algunos»"),
        ("¿Qué cuaderno quedó con el instrumento vacío?", "aunque haya acertado la respuesta"),
        ("¿Qué clave o qué dato del libro se discutió?", "y quién tenía razón; va al reporte")])
    pie(b, 4 + mis * 2)
    svg_close(b, OUTP + f"{4 + mis * 2:02d}.svg")


def h17():
    """Clases 7 y 8 · el simulacro del área y su devolución."""
    b = svg_open()
    y = cabecera(b, "Clases 7 y 8", "El simulacro del área y su devolución",
                 derecha="24", dsub="preguntas del simulacro")
    y = seccion(b, y, "Qué son estas dos clases",
        "No traen contenido nuevo. Trabajan las 24 preguntas tipo Saber 11 que el estudiante ya tiene "
        "en su cuaderno, cuatro por momento, y que hasta ahora resolvió de a poco y con instrumento.")
    dos = [("Clase 7 · el simulacro", ROJO, ROJO_BG, ROJO_LN,
            "Condiciones de prueba, 90 minutos de reloj, en silencio",
            ["Las 24 preguntas de entrenamiento del área, seguidas, en el orden del cuaderno.",
             "El estudiante SÍ puede escribir al margen la cuenta con sus unidades y dibujar las "
             "partículas: en la prueba real también puede, y es lo que entrenó.",
             "No se responde ninguna duda, ni de conceptos.",
             "Los últimos 30 minutos: cada uno cuenta sus aciertos por competencia (UC, EF, IN)."]),
           ("Clase 8 · la devolución", VERDE, VERDE_BG, VERDE_LN,
            "Reparación con el instrumento de la primera vez",
            ["Se eligen las cinco preguntas que más falló el grupo.",
             "Cada estudiante compara lo que escribió al margen en el simulacro con el instrumento "
             "de su hoja de entrenamiento.",
             "La pregunta que gobierna la clase: ¿qué dato, qué unidad o qué partícula viste esta vez "
             "que no viste antes?",
             "Al final, la portada del área: las ocho clases, las caritas y el puntaje."])]
    an = (CW - 20) / 2
    alto = 0
    for _, _, _, _, _, pasos in dos:
        alto = max(alto, 120 + sum(len(wrap_px(p_, 22, an - 110)) for p_ in pasos) * 31 + len(pasos) * 22)
    for i, (tit, c, bg, ln, sub_, pasos) in enumerate(dos):
        x = M + i * (an + 20)
        b.append(rect(x, y, an, alto, bg, r=18, stroke=ln, sw=2.2))
        b.append(rect(x + 14, y + 16, 5, alto - 32, c, r=3))
        b.append(T(x + 40, y + 52, [tit], 27, c, weight="700"))
        b.append(T(x + 40, y + 86, [sub_], 20, GRAY, style="italic"))
        yy = y + 112
        for p_ in pasos:
            b.append(f'<circle cx="{x+52}" cy="{yy+12}" r="6" fill="{c}"/>')
            yy = parrafo_j(b, x + 76, yy - 6, p_, an - 110, 22, INK, lh=31) + 22
    y += alto + 30
    y = nota(b, M, y, CW,
        "El simulacro no se califica con nota. Se cuenta por competencia, y lo que importa es que el "
        "estudiante vea en cuál se le va el puntaje. La competencia de cada pregunta es la que le pone "
        "el cuaderno en su hoja de entrenamiento; sirve para decidir el refuerzo, no para reportar. "
        "En la prueba real Biología, Química y Física dan un solo puntaje de Ciencias Naturales.",
        ORO, ORO_BG, ORO_LN, "Cómo se lee el resultado", 24) + 30
    y = seccion(b, y, "Conteo por competencia",
        "Llénalo con el grupo en el tablero al final de la clase 7. Debajo de cada una, las "
        "preguntas que le tocan: misión y número.")
    grupos = {"UC": [], "EF": [], "IN": []}
    for m in range(1, 7):
        for k in range(1, 5):
            grupos[comp_icfes(m, k)].append(f"M{m}·{k}")
    an2 = (CW - 2 * 18) / 3
    lineas = {c_: wrap_px("  ".join(v), 19, an2 - 80, "700") for c_, v in grupos.items()}
    alto2 = 168 + max(len(v) for v in lineas.values()) * 27
    for i, cod in enumerate(("UC", "EF", "IN")):
        x = M + i * (an2 + 18)
        b.append(rect(x, y, an2, alto2, "white", r=16, stroke=QUI_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alto2 - 28, QUI, r=3))
        b.append(T(x + 40, y + 46, [f"{cod} · {len(grupos[cod])} preguntas"], 23, INK, weight="700"))
        b.append(T(x + 40, y + 76, [COMP_NOM[cod].lower()], 19, GRAY, style="italic"))
        for j, ln in enumerate(lineas[cod]):
            b.append(T(x + 40, y + 108 + j * 27, [" ".join(ln)], 19, QUI, weight="700"))
        yb = y + 108 + len(lineas[cod]) * 27 - 6
        b.append(T(x + 40, yb + 20, ["aciertos del grupo"], 18, GRAY))
        b.append(rect(x + 230, yb - 6, an2 - 270, 40, QUI_BG, r=10, stroke=QUI_LN, sw=1.8))
    y += alto2 + 30
    y = seccion(b, y, "Las cinco preguntas que se reparan en la clase 8")
    cx = [M, M + 200, M + 560, M + 1160]
    y = encabezado_tabla(b, y, list(zip(cx, ["N.º", "MOMENTO Y PÁGINA", "QUÉ DATO HABÍA QUE VER",
                                              "QUÉ FALLÓ EL GRUPO"])))
    for k in range(1, 6):
        b.append(rect(M, y, CW, 76, "white", r=12, stroke=QUI_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, 56, VERDE, r=2))
        b.append(T(cx[0] + 54, y + 50, [str(k)], 26, VERDE, weight="700", anchor="middle"))
        for xi, xf in [(cx[1] + 18, cx[2] - 20), (cx[2] + 18, cx[3] - 20), (cx[3] + 18, W - M - 30)]:
            b.append(line(xi, y + 54, xf, y + 54, "#E6EAF0", 2))
        y += 82
    pie(b, 17)
    svg_close(b, OUTP + "17.svg")


def hoja_dinamicas(mis):
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Dinámicas · Misión {mis}",
                 "Movimiento con sentido: el cuerpo ensaya lo que después hará la mente",
                 derecha=f"{mis}", dsub="de 6 misiones")
    y = nota(b, M, y, CW,
        "La dinámica debe ser isomorfa a la estrategia: lo que hace el cuerpo tiene que ser el mismo "
        "movimiento que después hará la mente frente al dato. Antes de usar una, responde esto: ¿qué "
        "paso de la estrategia está ejercitando? Si no hay respuesta, es recreo, no clase.",
        ORO, ORO_BG, ORO_LN, "La regla para aprobar cualquier dinámica", 24) + 26
    for i, din in enumerate(DINAMICAS[mis]):
        y = bloque_dinamica(b, y, i, din, d["estr"][i], COLS_MIS[mis][i])
    bloque_reto(b, y + 6, mis, RETOS[mis])
    pie(b, 17 + mis)
    svg_close(b, OUTP + f"{17 + mis:02d}.svg")


def h24():
    b = svg_open()
    graves = [(m, a) for m in range(1, 7) for a in AVISOS.get(m, []) if a[1] != "atención"]
    total = sum(len(v) for v in AVISOS.values())
    y = cabecera(b, "Cierre del área", "Los avisos del libro, juntos, y lo que hay que devolver",
                 derecha=str(total), dsub="avisos del libro")
    y = seccion(b, y, f"Los {len(graves)} avisos que tocan una clave o un dato",
        f"Para repasarlos antes de empezar el área. Los otros {total - len(graves)}, de «atención», "
        "están en la hoja de cada clase. Ninguno se le oculta al estudiante: si lo detecta y lo "
        "escribe, aprendió más que el que marcó la opción esperada.")
    cx = [M, M + 330, M + 470]
    y = encabezado_tabla(b, y, list(zip(cx, ["DÓNDE", "SEVERIDAD", "QUÉ PASA"])), 46)
    for m, (preg, sev, que, hacer) in graves:
        c, bg, ln = SEV[sev]
        lin = wrap_px(que, 18, CW - 510)
        h = max(46, 14 + len(lin) * 24)
        b.append(rect(M, y, CW, h, bg, r=10, stroke=ln, sw=1.6))
        b.append(rect(M + 9, y + 8, 4, h - 16, c, r=2))
        b.append(T(cx[0] + 30, y + h / 2 + 7, [f"M{m} · {preg}"], 18, INK, weight="700"))
        chip(b, cx[1] + 6, y + h / 2 - 13, sev.upper(), c, size=12, pad=10, fill="white", txtc=c)
        parrafo_j(b, cx[2] + 14, y + (h - len(lin) * 24) / 2 - 4, que, CW - 510, 18, INK, lh=24)
        y += h + 4
    y += 22
    y = seccion(b, y, "Qué tienes que devolver al terminar el área")
    dev = [("Los seis registros de clase", "con nombres, no «algunos»"),
           ("El conteo por competencia del simulacro", "el dato que decide el refuerzo"),
           ("Las claves que el grupo discutió", "M3 P9, M5 P10, M6 P5 y P6: van a la editorial"),
           ("Los avisos nuevos que encuentres", "la lista se hizo resolviendo, y seguro falta alguno")]
    for t, s_ in dev:
        b.append(rect(M, y, CW, 64, "white", r=14, stroke=QUI_LN, sw=2))
        b.append(rect(M + 14, y + 12, 5, 40, ORO, r=3))
        b.append(checkbox(M + 42, y + 19, 13, QUI))
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


PDF = "/home/user/educate-saber11/entregables/EDUCATE_Planeador_Quimica.pdf"

if __name__ == "__main__":
    import sys
    import render
    malas = verificar()
    if malas:
        raise SystemExit("No cuadra:\n  " + "\n  ".join(malas))
    hojas = build()
    print(len(hojas), "hojas del planeador de Química")
    if "--pdf" in sys.argv:
        render.unir(hojas, PDF)
        n, sin = render.verifica(PDF, "PLANEADOR")
        print(f"{PDF}: {n} páginas · sin pie: {sin or 'ninguna'}")
