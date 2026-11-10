#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLANEADOR DEL DOCENTE · LECTURA CRÍTICA · las ocho clases del área.

Mismo modelo aprobado en el piloto de Matemáticas: seis momentos de 15·20·35·20·20·10,
«tu aporte» acotado en cada uno y un banco de dinámicas isomorfas a las estrategias.

Lo propio del área: donde Matemáticas tiene la cuadrícula, Lectura Crítica tiene el
TEXTO MARCADO — el subrayado y la pregunta escrita al margen. Y tiene dos deudas que
Matemáticas no tiene registradas: 18 sellos «aquí entra el profe» y 21 textos que el
cuaderno no imprime completos y el docente tiene que proyectar.
"""
import csv
from plan_piezas import *
import plan_piezas as PZ

LC = "#A82424"; LC_BG = "#FBEFEF"; LC_LN = "#E6C4C4"
TOTAL = 24
configurar(LC, LC_BG, LC_LN, "Lectura Crítica", TOTAL)

COLS_EST = [LC, "#1F4E8C", ORO, MORADO]      # un color por estrategia


# ─────────────────────────── los seis momentos ───────────────────────────
# El reparto es el aprobado: 15 · 20 · 35 · 20 · 20 · 10 = 120.
FASES = [
    ("Activación", 15, LC,
     "Que el estudiante note que leer no es pasar los ojos, trabajando sobre un texto corto "
     "antes de que aparezca cualquier pregunta de opción múltiple.",
     ["Proyecta dos o tres renglones sin decir de dónde salieron ni de qué tratan.",
      "Pide una sola cosa: subrayar la palabra que más pesa y escribirle una pregunta al lado.",
      "Ejecuta la dinámica de apertura según la estrategia del encuentro."],
     "No explica el texto, no da el contexto y no corrige el subrayado. Si alguien pregunta "
     "«¿de qué es esto?», lo devuelve: «eso es lo que vamos a averiguar». El cuaderno sigue cerrado.",
     "Proyector o tablero con dos o tres renglones. Todavía no se abre el cuaderno."),
    ("Pregunta problematizadora", 20, "#1F4E8C",
     "Que el estudiante compruebe que la respuesta está en el texto y no en su opinión, usando "
     "la pregunta modelo del libro.",
     ["Presenta la pregunta modelo del libro y la deja a la vista todo el momento.",
      "Pide respuestas a mano alzada ANTES de releer, y las anota en el tablero.",
      "Hace la pregunta que gobierna el área: ¿en qué renglón está eso que estás diciendo?",
      "Revela la clave solo al final y trabaja el análisis de distractores."],
     "Regla del momento: nadie justifica con «yo creo» ni con «se entiende que». Toda "
     "intervención tiene que señalar una palabra o un renglón concreto del texto.",
     "Libro abierto en la pregunta modelo. Cuaderno solo en «mi primera idea»."),
    ("Desarrollo guiado", 35, "#3B3BA6",
     "Que el estudiante marque el texto antes de mirar las opciones, y deje por escrito de "
     "dónde sacó lo que va a responder.",
     ["Entrega las hojas del momento y trabaja por bloques: 1-2, 3-4, 5-6, 7-8 y 9-10.",
      "Antes de que marquen, verifica que el texto esté subrayado y el instrumento diligenciado.",
      "Cada 18 minutos corta e introduce la dinámica de la estrategia del bloque.",
      "Al cerrar cada bloque, nombra en voz alta la estrategia que acaban de usar."],
     "No parafrasea el texto ni lo resume. Si un estudiante se traba, le pregunta qué subrayó; "
     "si la hoja está limpia, lo devuelve a leer antes que a responder.",
     "Cuaderno, las cinco hojas de taller. Libro, en las preguntas 1 a 10."),
    ("Reto en equipo", 20, MORADO,
     "Que el estudiante defienda su lectura con el texto en la mano y acepte que otra lectura "
     "también puede estar sostenida.",
     ["Arma equipos de tres y entrega el reto del corte de este momento.",
      "Exige que cada integrante llegue con su cuaderno YA diligenciado individualmente.",
      "Da tres minutos de defensa por equipo: deben leer en voz alta el renglón que los respalda.",
      "Cierra señalando dónde el texto permite las dos lecturas y dónde no."],
     "El equipo discute, pero cada uno responde en SU cuaderno. No se acepta una defensa sin "
     "lectura en voz alta del fragmento: citar de memoria no cuenta.",
     "Cuaderno de cada estudiante y la tarjeta del reto del corte."),
    ("Evaluación individual", 20, ORO,
     "Que el estudiante transfiera por sí solo la estrategia a preguntas tipo Saber 11, con "
     "textos que no trabajó en clase.",
     ["Entrega las dos hojas de entrenamiento ICFES del momento.",
      "Da el tiempo completo sin intervenir ni aclarar vocabulario.",
      "Registra quién subraya el texto y quién va directo a las opciones."],
     "Este momento es silencioso y en filas individuales. Es el que produce el dato de "
     "seguimiento. Si un estudiante marca sin subrayar, se le anota, no se le corrige.",
     "Cuaderno, las dos hojas de entrenamiento ICFES. Reloj a la vista."),
    ("Cierre", 10, VERDE,
     "Que el estudiante nombre la estrategia que usó y se lleve una palabra nueva del día, "
     "escrita en sus propios términos.",
     ["Socializa solo las preguntas que el grupo falló, pidiendo el renglón que las sostiene.",
      "Pide que lean en voz alta su salvavidas: la ruta mínima que los habría salvado.",
      "Cada uno escribe la palabra nueva del día en la franja de vocabulario de su hoja."],
     "No dicta la definición. La palabra nueva se escribe como el estudiante la entendió; si "
     "quedó mal entendida, eso se ve en la hoja y se corrige la próxima clase.",
     "Cuaderno: franja de vocabulario, «lo que me llevo», carita de salida y casilla de la portada."),
]

CLASES = [
    (1, "Momento 1 · Componente semántico", "páginas 54 a 60 del cuaderno"),
    (2, "Momento 2 · Componente semántico", "páginas 61 a 67 del cuaderno"),
    (3, "Momento 3 · Componente sintáctico", "páginas 68 a 74 del cuaderno"),
    (4, "Momento 4 · Componente sintáctico", "páginas 75 a 81 del cuaderno"),
    (5, "Momento 5 · Componente pragmático", "páginas 82 a 88 del cuaderno"),
    (6, "Momento 6 · Pragmático · cierre del área", "páginas 89 a 95 del cuaderno"),
    (None, "Simulacro del área", "las 6 franjas de simulacro, en condiciones de prueba"),
    (None, "Socialización del simulacro", "devolución, reparación y cierre del área"),
]

BASE = {1: 54, 2: 61, 3: 68, 4: 75, 5: 82, 6: 89}

MISIONES = {
 1: dict(comp="Semántico", pags="54 a 60", competencia="CL · identificar contenidos locales",
   estr=["La palabra exacta", "Para qué está ahí", "Lo que no se dice", "La idea que sostiene"],
   instala="Que el significado de una palabra lo fija la frase donde está, no el diccionario. "
           "Es la operación que el ICFES evalúa una y otra vez y la que el estudiante cree que "
           "ya sabe hacer.",
   ojo="La franja de vocabulario de esta misión es la primera del cuaderno. Si arranca vacía, "
       "las cinco siguientes arrancan vacías: vale la pena pararse en ella el primer sábado.",
   cierre="El entrenamiento ICFES de este momento usa el mismo fragmento de Savater que la "
          "misión 2, a propósito: el estudiante tiene que ver que un texto aguanta preguntas "
          "de distinto tipo."),
 2: dict(comp="Semántico", pags="61 a 67", competencia="SG · comprender el sentido global",
   estr=["Qué hace este párrafo", "La crítica que no se ve", "Para qué lo escribió",
         "Cómo se enlazan"],
   instala="La diferencia entre lo que un párrafo DICE y lo que un párrafo HACE. Un párrafo "
           "puede ejemplificar, objetar, matizar o concluir, y casi siempre hay un verbo que "
           "lo delata.",
   ojo="Cuando el texto trae un «pero», el peso cae del lado derecho. Conviene hacerlo en el "
       "tablero una vez, con una frase del propio salón, antes de la pregunta 8.",
   cierre="Esta misión introduce la caricatura como texto discontinuo. Se lee por planos, del "
          "frente al fondo, y eso hay que mostrarlo señalando con el dedo en la proyección."),
 3: dict(comp="Sintáctico", pags="68 a 74", competencia="SG · comprender el sentido global",
   estr=["La bisagra del texto", "El juicio que no se dice", "La pieza que remata",
         "El detalle que lo delata"],
   instala="Qué es una bisagra: el punto donde el texto gira. Un texto de tres párrafos tiene "
           "dos, y casi siempre están marcadas por un conector que el estudiante lee sin ver.",
   ojo="Aquí aparece el juicio implícito: el cronista no califica a nadie, deja que lo veas. "
       "Es la operación más difícil del área y la que más se evalúa en el componente.",
   cierre="Dos preguntas de esta misión, la 4 y la 5, preguntan casi lo mismo. Está anotado "
          "como hallazgo: si el grupo lo nota, dales la razón y pide que escriban la diferencia."),
 4: dict(comp="Sintáctico", pags="75 a 81", competencia="SG y CL · estructura y datos locales",
   estr=["La señal de tránsito", "Lo que puedo señalar con el dedo", "Qué pieza es esta",
         "La forma delata el propósito"],
   instala="Los conectores como señales de tránsito: «es tal… que» apunta hacia adelante, «en "
           "cambio» anuncia contraste, «dicho de otro modo» reformula. El conector dice qué "
           "viene antes de que venga.",
   ojo="Esta misión trae textos discontinuos: infografía, enumeración con cifras. Se leen por "
       "pisos, no en línea. Hay que proyectarlos: en el cuaderno van recortados.",
   cierre="«Lo que puedo señalar con el dedo» es la estrategia que más rinde en la prueba: "
          "cuando cada opción trae una cifra, la respuesta está impresa en el texto."),
 5: dict(comp="Pragmático", pags="82 a 88", competencia="RE · reflexionar y evaluar",
   estr=["Qué quiere que yo haga", "Quién habla y desde dónde", "Lo que dice y lo que muestra",
         "La idea detrás de la imagen"],
   instala="Que todo texto viene de alguien que quiere algo. Identificar la intención no es "
           "adivinar la psicología del autor: es mirar qué construye el texto y qué deja afuera.",
   ojo="⚠ El texto de las preguntas 8 a 10 es una columna de opinión sobre un expresidente "
       "colombiano vivo. Lee la advertencia previa de la guía ANTES del sábado: el encuadre de "
       "la clase es sobre el procedimiento argumentativo, no sobre el personaje.",
   cierre="Citar a una autoridad explica y respalda, pero no demuestra. Esa distinción es el "
          "corazón de la pregunta 8 y vale para todo lo que el estudiante lea después."),
 6: dict(comp="Pragmático · cierre del área", pags="89 a 95",
   competencia="RE · reflexionar y evaluar",
   estr=["Una sola línea: qué defiende", "Qué se cae si quito esto",
         "Dice una cosa y hace la contraria", "Cómo llega el texto hasta ahí"],
   instala="Qué es una paradoja: dos cosas ciertas al mismo tiempo que tiran en direcciones "
           "opuestas. No es una contradicción ni un error del autor: es la forma del argumento.",
   ojo="En esta misión seis de las diez claves son A y ninguna es B. Está reportado a la "
       "editorial. Mientras tanto, no digas la distribución en voz alta: el estudiante que la "
       "oye deja de leer.",
   cierre="El poema de Kavafis del cierre hay que proyectarlo completo: el efecto está en la "
          "repetición, y el cuaderno solo trae tres preguntas y el final."),
}

AVISOS = {
 1: [],
 2: [("preg. 5", "atención",
      "Dos opciones afirman que el gráfico contradice la escena; una agrega una mayoría que el "
      "dibujo no muestra.",
      "No es un error de fondo, pero si un estudiante defiende la otra, pídele que señale la "
      "mayoría en el dibujo. Ahí se cae sola.")],
 3: [("preg. 10", "media",
      "La opción D parafrasea casi textual la frase final y la A emite el juicio que el "
      "enunciado pide como implícito.",
      "Las dos se pueden defender. Úsala para enseñar la diferencia entre repetir el texto y "
      "sacarle una conclusión."),
     ("preg. 4 y 5", "atención",
      "La 4 pregunta por la valoración sobre los que miran y la 5 por lo que sugiere "
      "«fascinación morbosa»: las respuestas son casi permutables.",
      "Trabájalas juntas y pide que escriban en una línea qué le pregunta cada una.")],
 4: [("preg. 10", "media",
      "El enunciado pregunta por el EFECTO de insistir en el cambio personal, pero las cuatro "
      "opciones describen lo que el texto HACE.",
      "Ninguna responde lo que se pide. Que marquen la que más se acerque y escriban al lado "
      "qué pregunta sí responderían las opciones.")],
 5: [("texto 8 a 10", "alta",
      "Es una columna de opinión sobre un expresidente colombiano vivo, usada para entrenar la "
      "detección de sesgo.",
      "Lee la advertencia previa de la guía antes del sábado. El encuadre es el procedimiento "
      "argumentativo; si el salón se va al personaje, devuélvelo al texto."),
     ("preg. 8", "media",
      "La opción A dice que la cita demuestra que el proceso «carece de parcialidad», y carecer "
      "de parcialidad es ser imparcial: la opción niega su propio sentido.",
      "Léela en voz alta y pregunta qué quiso decir. Es un buen ejemplo de que la forma de una "
      "opción puede delatarla."),
     ("preg. 4 y 5", "media",
      "Las dos preguntan por la misma contradicción de la caricatura y sus respuestas son casi "
      "permutables.",
      "Resuelve una con el grupo y deja la otra para el reto en equipo."),
     ("preg. 10", "atención",
      "La A atiende al título y la D al relato completo: las dos son valoraciones correctas del "
      "sesgo del texto.",
      "Acepta las dos si el estudiante señala de dónde sacó la suya.")],
 6: [("preg. 1 y 3", "atención",
      "Las dos preguntan qué le hace la fotografía a la memoria y la respuesta de la 1 serviría "
      "para la 3.",
      "Hazlas seguidas y pide que escriban qué agrega la 3 que la 1 no pedía."),
     ("preg. 4 y 5", "atención",
      "Las dos trabajan la ironía del mismo post y la respuesta de una describe lo que la otra "
      "pide.",
      "Una en pantalla y la otra en el reto en equipo."),
     ("preg. 10", "media",
      "Las cuatro opciones parafrasean la misma lección con distintos acentos: la A usa las "
      "palabras del texto.",
      "Esta es la pregunta para enseñar el criterio de cierre del área: cuando cuatro opciones "
      "dicen casi lo mismo, gana la que usa las palabras del texto."),
     ("reparto de claves", "media",
      "Seis de las diez claves de esta misión son A y ninguna es B.",
      "Reportado a la editorial. No lo menciones en clase: el estudiante que lo oye deja de leer.")],
}


# ─────────────────────── lo que ya está registrado ───────────────────────
def _instrumentos():
    from extrae_instrumentos import filas
    taller, icfes = {}, {}
    for a, mis, p, est, ins, ctx in filas():
        if a != "Lectura Crítica":
            continue
        d = icfes if "ICFES" in str(mis) else taller
        k = int(str(mis).split()[0])
        d.setdefault(k, []).append((int(p), est, ins, ctx))
    for d in (taller, icfes):
        for k in d:
            d[k].sort()
    return taller, icfes


def _banco():
    """El CSV rotula las misiones de dos formas: «LC Misión 1» y «LC M3»."""
    with open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig") as f:
        r = list(csv.DictReader(f))
    out = {}
    for x in r:
        m = x["mision"].strip()
        if not m.startswith("LC"):
            continue
        n = m.replace("LC", "").replace("Misión", "").replace("M", "").strip()
        if n.isdigit():
            out.setdefault(int(n), []).append(x)
    return out


def _de_matriz(nombre):
    """SELLOS y TEXTOS viven en matriz.py y los lee el planeador sin copiarlos."""
    import ast
    tree = ast.parse(open(OUT + "matriz.py").read())
    for n in tree.body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == nombre:
            fuera = []
            for e in n.value.elts:
                v = [x.value if isinstance(x, ast.Constant) else "?" for x in e.elts]
                if v[0] == "Lectura Crítica":
                    fuera.append(v)
            return fuera
    return []


TALLER, INS_ICFES = _instrumentos()
BANCO = _banco()
SELLOS = _de_matriz("SELLOS")      # área, misión, página, pregunta, saber, dónde, estado
TEXTOS = _de_matriz("TEXTOS")      # área, misión, páginas, texto, fuente, tipo, completo, nota


def limpia(t):
    """Carlito no trae el glifo ⚠ y el respaldo lo dibuja encima de la palabra siguiente.
    La alerta se marca con el color rojo de la tarjeta, no con el símbolo."""
    return t.replace("⚠ ", "").replace("⚠", "").strip()


def sellos_de(mis):
    return [s for s in SELLOS if str(s[1]) == str(mis)]


def textos_de(mis):
    return [t for t in TEXTOS if str(t[1]) == str(mis)]


# ─────────────────────────── banco de dinámicas ───────────────────────────
# Isomorfas a la estrategia: lo que hace el cuerpo es el mismo movimiento que después
# hará la mente frente al texto. En Lectura Crítica el movimiento casi siempre es señalar.
DINAMICAS = {
 1: [("Cambia la palabra", 8,
      ["Se proyecta una frase del texto con una palabra tapada.",
       "El grupo propone cuatro palabras para el hueco.",
       "Cada propuesta se lee en voz alta DENTRO de la frase, no suelta.",
       "El grupo vota cuáles cambian el sentido y cuáles no, y dice por qué."],
      "Probar cada opción dentro de la frase y escuchar cuál desentona. Es el movimiento de "
      "las preguntas 1, 4 y 10, y de la del ICFES sobre «deslumbrar».",
      "Proyector o tablero · una frase con un hueco"),
     ("El párrafo que falta", 8,
      ["Se reparte un texto corto cortado en tarjetas, una por párrafo.",
       "El docente retira una tarjeta sin decir cuál.",
       "Cada equipo lee lo que queda y dice qué perdió el texto: ¿un ejemplo, una razón, el cierre?",
       "Se muestra la tarjeta retirada y se comprueba."],
      "Ver para qué está cada parte del texto mirando qué se cae cuando falta. Es el movimiento "
      "de las preguntas 2 y 9.",
      "Un texto cortado en tarjetas por equipo"),
     ("Lo dicho y lo que se entiende", 8,
      ["Dos columnas en el tablero: LO DICE y LO DEJA ENTENDER.",
       "El docente lee frases de un texto corto, una por una.",
       "Un estudiante pasa y la pone en una columna.",
       "Para quedarse tiene que señalar la palabra que lo hizo decidir."],
      "Separar lo que el texto afirma de lo que deja entender, y anclar la inferencia a una "
      "palabra. Es el movimiento de las preguntas 3, 5 y 6.",
      "Tablero en dos columnas"),
     ("Tres veces la misma idea", 10,
      ["Se proyecta un texto donde la idea central aparece tres veces con otras palabras.",
       "El salón se divide en tres grupos; cada grupo busca UNA aparición.",
       "Cada grupo lee la suya en voz alta.",
       "Juntos escriben en el tablero la idea en una sola línea."],
      "Reconocer la idea que sostiene el texto por su repetición, no por la primera frase. Es "
      "el movimiento de las preguntas 7 y 8.",
      "Proyector · un texto de tres párrafos")],
 2: [("El verbo del párrafo", 8,
      ["Cada estudiante recibe cuatro tarjetas: EJEMPLIFICA, OBJETA, MATIZA, CONCLUYE.",
       "El docente lee un párrafo en voz alta.",
       "A la cuenta de tres, todos levantan la tarjeta que creen.",
       "Quien levantó una distinta a la mayoría tiene que leer la frase que lo hizo decidir."],
      "Ver qué hace un párrafo, no qué dice. Es el movimiento de las preguntas 1, 2 y 7.",
      "Cuatro tarjetas por estudiante"),
     ("Miente u omite", 8,
      ["Tres zonas en el piso: MIENTE, OMITE y NI LO UNO NI LO OTRO.",
       "El docente lee afirmaciones sobre un texto que todos tienen a la vista.",
       "Cada estudiante se para en una zona.",
       "Para quedarse tiene que señalar en el texto lo que dice o lo que calla."],
      "Distinguir las formas en que un texto critica sin decirlo: no es lo mismo mentir que "
      "omitir. Es el movimiento de las preguntas 4, 6 y 8.",
      "Tres zonas marcadas · el texto proyectado"),
     ("Un verbo para todo el texto", 10,
      ["Cada equipo lee el mismo texto y escribe UN verbo que diga para qué fue escrito.",
       "Los verbos se escriben en el tablero, uno al lado del otro.",
       "Cada equipo tiene que mostrar en el texto lo que respalda su verbo.",
       "Se tachan los verbos que no aguantan la prueba."],
      "Ver que todo texto tiene un verbo que lo resume y que la intención se demuestra con el "
      "texto, no con la opinión. Es el movimiento de las preguntas 3 y 9.",
      "Tablero · el mismo texto para todos"),
     ("Cambia el conector", 8,
      ["Se proyecta una frase con un conector subrayado.",
       "El grupo propone otros conectores para reemplazarlo.",
       "Cada uno se lee en voz alta dentro de la frase.",
       "Se decide cuáles mantienen la relación entre las dos ideas y cuáles la rompen."],
      "Ver que la relación entre dos ideas está escrita en el conector. Es el movimiento de las "
      "preguntas 5 y 10, y de la del ICFES sobre la función del «Pero».",
      "Proyector · una frase con conector")],
 3: [("Las dos bisagras", 8,
      ["Se pega en la pared un texto de tres párrafos impreso en grande.",
       "Dos estudiantes se paran en los puntos donde creen que el texto gira.",
       "El grupo discute si están bien puestos.",
       "Se tapa el conector de cada bisagra y se leen las dos partes solas."],
      "Encontrar el punto donde el texto cambia de rumbo. Es el movimiento de las preguntas 1 y "
      "6, y de la del ICFES sobre el conector en Cien años de soledad.",
      "Un texto impreso en grande · cinta"),
     ("Sin adjetivos", 10,
      ["El docente describe una escena en voz alta sin calificar a nadie.",
       "Cada estudiante escribe en una línea qué juicio le queda de la escena.",
       "Se leen tres o cuatro juicios en voz alta.",
       "El grupo busca qué palabras de la descripción produjeron ese juicio."],
      "Ver que un texto puede juzgar sin adjetivos, solo con lo que pone al lado de qué. Es el "
      "movimiento de las preguntas 2, 4, 7 y 10.",
      "Una escena descrita · hojas sueltas"),
     ("Repite, niega o integra", 8,
      ["Se proyecta un texto sin su cierre.",
       "Se muestran tres cierres posibles, uno por uno.",
       "El grupo dice si cada uno repite lo dicho, lo niega o lo integra.",
       "Se revela el cierre real y se ve de cuál de los tres tipos es."],
      "Reconocer qué hace la pieza que remata un texto. Es el movimiento de las preguntas 3 y 8.",
      "Proyector · tres cierres en tarjetas"),
     ("Un segundo distinto", 8,
      ["Se lee en voz alta un párrafo que describe a un personaje.",
       "Los estudiantes levantan la mano en el momento exacto en que el personaje es distinto.",
       "Se relee esa frase y se subraya.",
       "El grupo dice qué revela ese segundo que el resto del párrafo oculta."],
      "Encontrar el detalle que delata lo que el texto no dice en voz alta. Es el movimiento de "
      "las preguntas 5 y 9.",
      "Un párrafo para leer en voz alta")],
 4: [("Las señales de tránsito", 8,
      ["Tres flechas dibujadas en el tablero: SIGUE IGUAL, GIRA y EXPLICA.",
       "Cada estudiante recibe una tarjeta con un conector.",
       "Por turnos pegan su tarjeta bajo la flecha que creen.",
       "Quien la puso mal tiene que inventar una frase con su conector."],
      "Leer el conector como una señal que anuncia lo que viene. Es el movimiento de las "
      "preguntas 1 y 6, y de la del ICFES sobre Cortázar.",
      "Tablero con tres flechas · tarjetas con conectores"),
     ("Con el dedo", 8,
      ["Se proyecta un texto con cifras y se leen las cuatro opciones de una pregunta.",
       "Para cada opción, un estudiante pasa y señala con el dedo la línea que la respalda.",
       "Si nadie puede señalarla, la opción sale.",
       "Gana la que queda con el dedo puesto."],
      "Comprobar cada opción contra una línea concreta del texto. Es el movimiento de las "
      "preguntas 5, 7 y 9.",
      "Proyector · un texto con cifras"),
     ("La infografía por pisos", 10,
      ["Cada equipo recibe una infografía cortada en franjas horizontales.",
       "Tienen que armarla en el orden en que se lee.",
       "Rotulan cada franja: título, dato, causa, consecuencia o fuente.",
       "Se comparan los órdenes entre equipos."],
      "Leer un texto discontinuo por pisos y saber qué pieza es cada uno. Es el movimiento de "
      "las preguntas 2, 4 y 8.",
      "Una infografía cortada por equipo"),
     ("Adivina el tipo", 8,
      ["Se proyectan cuatro fragmentos cortos: noticia, opinión, instructivo y carta.",
       "Se tapa el contenido y se deja solo la forma: títulos, fechas, saludos, viñetas.",
       "El grupo adivina qué tipo es cada uno.",
       "Se destapa y se comprueba."],
      "Ver que la forma del texto delata su propósito antes de leer el contenido. Es el "
      "movimiento de las preguntas 3 y 10.",
      "Proyector · cuatro fragmentos")],
 5: [("Lo que me pide el texto", 8,
      ["Se leen tres textos muy cortos: un aviso, un fragmento filosófico y un trino.",
       "Después de cada uno, el grupo dice en voz alta qué quiere el texto que el lector haga "
       "o crea.",
       "No se acepta «informar» como respuesta: hay que decir qué se busca con la información.",
       "Se escribe en el tablero un verbo por texto."],
      "Identificar la intención mirando lo que el texto construye. Es el movimiento de las "
      "preguntas 3, 7 y 9.",
      "Tres textos cortos · tablero"),
     ("La silla del autor", 8,
      ["Una silla al frente del salón.",
       "El docente lee una cita del texto.",
       "Un estudiante se sienta y dice, en primera persona, quién es y desde dónde habla.",
       "El grupo decide si la silla está bien ocupada señalando el texto."],
      "Ubicar quién habla y desde qué posición. Es el movimiento de las preguntas 8 y 10, y de "
      "la del ICFES sobre la voz de «El llanto de un hombre».",
      "Una silla · las citas en tarjetas"),
     ("Letra contra dibujo", 8,
      ["Se divide el salón en dos mitades frente a la misma caricatura.",
       "Una mitad lee solo la letra; la otra mira solo el dibujo.",
       "Cada mitad dice qué entendió.",
       "Se juntan las dos lecturas: la caricatura está en la diferencia."],
      "Ver que lo que el texto dice y lo que muestra pueden no coincidir, y que ahí está la "
      "crítica. Es el movimiento de las preguntas 4 y 5.",
      "Una caricatura proyectada"),
     ("Las equivalencias", 10,
      ["Se reparten dos juegos de tarjetas: piezas de la imagen y las ideas que representan.",
       "Cada pareja tiene que unir cada pieza con su idea.",
       "Se comparan las uniones entre parejas.",
       "La alegoría queda armada cuando todas las piezas tienen su equivalente."],
      "Leer una alegoría como un sistema de equivalencias y no como una metáfora suelta. Es el "
      "movimiento de las preguntas 1, 2 y 6.",
      "Dos juegos de tarjetas por pareja")],
 6: [("En una línea", 8,
      ["Cada estudiante escribe en una sola línea qué defiende el texto.",
       "Después tiene que encontrar esa idea en el texto y subrayarla.",
       "Si no la encuentra, reescribe su línea.",
       "Se leen tres líneas en voz alta con el subrayado al lado."],
      "Escribir la tesis con las propias palabras y comprobarla en el texto. Es el movimiento "
      "de las preguntas 1, 3 y 7.",
      "Hojas sueltas · el texto proyectado"),
     ("Tapa y mira", 8,
      ["Se proyecta el texto completo.",
       "El docente tapa un párrafo con una hoja sobre la proyección.",
       "El grupo lee lo que queda y dice qué se cayó del argumento.",
       "Se destapa y se comprueba."],
      "Ver qué función cumple una parte mirando qué se cae cuando se quita. Es el movimiento de "
      "las preguntas 2, 6 y 9.",
      "Proyector · una hoja para tapar"),
     ("Partido por la mitad", 8,
      ["Se imprime un post con meme y se corta en dos mitades.",
       "La mitad del salón lee la primera parte; la otra mitad, la segunda.",
       "Cada mitad dice qué entendió.",
       "Al juntarlas, el grupo nombra qué se está criticando."],
      "Ver que la ironía dice una cosa y hace la contraria, y que critica algo con nombre. Es el "
      "movimiento de las preguntas 4 y 5.",
      "Un post impreso y cortado en dos"),
     ("Los nudos del hilo", 10,
      ["Se tiende un hilo de lado a lado del salón con cinco nudos.",
       "Cada nudo es un momento del fragmento.",
       "Los estudiantes cuelgan en cada nudo una tarjeta con lo que pasa ahí.",
       "Se recorre el hilo leyendo las tarjetas en orden."],
      "Seguir cómo llega el texto hasta su conclusión, paso por paso. Es el movimiento de las "
      "preguntas 8 y 10.",
      "Un hilo · ganchos · tarjetas")],
}

RETOS = {
 1: ("Una palabra, cuatro frases", 20,
     "Cada equipo de tres recibe una palabra usada en cuatro frases distintas. En doce minutos "
     "deben escribir qué significa en cada frase y subrayar la palabra vecina que se lo fija. "
     "Exponen leyendo la frase en voz alta. Gana el equipo que encuentre la diferencia más fina "
     "entre dos de los cuatro usos."),
 2: ("El verbo de cada párrafo", 20,
     "Cada equipo recibe un texto de cuatro párrafos desordenados. Deben asignar a cada párrafo "
     "un verbo —ejemplifica, objeta, matiza, concluye— y pasarle SOLO la lista de verbos a otro "
     "equipo. El otro equipo tiene que reconstruir el orden del texto con esa lista. Gana el "
     "equipo cuyos verbos permitieron reconstruirlo."),
 3: ("Dónde gira", 20,
     "Cada equipo recibe un texto sin separación de párrafos. En doce minutos deben marcar las "
     "bisagras, poner las barras donde iría cada párrafo y escribir en una línea qué hace cada "
     "tramo. Se comparan las barras entre equipos: donde no coinciden, cada equipo defiende la "
     "suya leyendo el conector."),
 4: ("Pruébalo con el dedo", 20,
     "Todos los equipos reciben la misma infografía y cuatro afirmaciones sobre ella. Cada "
     "afirmación se acepta solo si el equipo puede señalar con el dedo dónde está; si no, se "
     "rechaza por escrito diciendo qué le falta. Gana el equipo con menos afirmaciones aceptadas "
     "sin respaldo."),
 5: ("Quién lo dice y para qué", 20,
     "Cada equipo recibe un texto de opinión distinto. En doce minutos deben escribir quién "
     "habla, desde dónde, qué quiere que el lector crea y qué deja por fuera. Lo último es lo "
     "que más cuenta. Exponen leyendo el renglón que respalda cada respuesta."),
 6: ("La tesis en una línea", 20,
     "Cada equipo recibe tres textos cortos. Para cada uno escribe la tesis en una sola línea y "
     "le pasa SOLO las tres líneas a otro equipo, que tiene que encontrar en cada texto el "
     "renglón que la sostiene. Gana el equipo cuyas tres líneas el otro pudo comprobar."),
}


# ─────────────────────────────── hojas ───────────────────────────────
def h1():
    b = svg_open()
    y = cabecera(b, "Lectura Crítica", "Planeador del área · las ocho clases",
                 derecha="8", dsub="clases de 120 min", campos=True)
    y = seccion(b, y, "Para qué existe este documento")
    y = parrafo_j(b, M, y,
        "La calidad de la clase no puede depender de qué profesor llegue ese sábado. Por eso el "
        "método de EDUCATE no vive en el profesor: vive en el cuaderno del estudiante. Este "
        "planeador no te dice cómo leer un texto; te dice qué hacer con el libro y con el "
        "cuaderno en cada uno de los 120 minutos, y dónde termina lo fijo y empieza tu aporte.",
        CW, 27) + 26

    cajas = [("LIBRO", "tiene la pregunta", GRAY), ("CUADERNO", "tiene el andamiaje para resolverla", LC),
             ("PLANEADOR", "te dice qué hacer con los dos", ORO), ("GUÍA", "pone ese plan en pantalla", VERDE)]
    an = (CW - 3 * 26) / 4
    for i, (t, s_, c) in enumerate(cajas):
        x = M + i * (an + 26)
        b.append(rect(x, y, an, 150, "white", r=18, stroke=c, sw=2.4))
        b.append(rect(x + 14, y + 16, 5, 118, c, r=3))
        b.append(T(x + an / 2 + 10, y + 62, [t], 26, c, weight="700", anchor="middle", ls=1.4))
        for j, ln in enumerate(wrap_px(s_, 21, an - 56)):
            b.append(T(x + an / 2 + 10, y + 100 + j * 28, [" ".join(ln)], 21, GRAY, anchor="middle"))
        if i < 3:
            b.append(T(x + an + 13, y + 86, ["›"], 34, "#A8B0BC", weight="700", anchor="middle"))
    y += 150 + 36

    y = nota(b, M, y, CW,
        "Si la hoja está limpia, no leíste: pasaste los ojos. En Lectura Crítica el andamiaje es "
        "el texto marcado — el subrayado y la pregunta escrita al margen. Un estudiante que acierta "
        "con el texto en blanco no aprendió la estrategia: adivinó, y en la prueba real no va a "
        "tener a quién preguntarle.",
        ORO, ORO_BG, ORO_LN, "El instrumento de pensamiento del área", 26) + 34

    y = seccion(b, y, "El área en números",
        "Lo que ya está construido y verificado. Lectura Crítica es el área con más material "
        "registrado para el profe: por eso este planeador trae, clase por clase, lo que hay que "
        "instalar y lo que hay que proyectar.")
    cif = [("43", "páginas del cuaderno\\ncon la portada", LC), ("60", "preguntas del libro\\ncon su andamiaje", LC),
           ("24", "preguntas Saber 11\\npara entrenar", VERDE), ("18", "sellos «aquí entra\\nel profe»", ORO),
           ("21", "textos para\\nproyectar completos", "#1F4E8C")]
    an2 = (CW - 4 * 18) / 5
    for i, (v, l, c) in enumerate(cif):
        x = M + i * (an2 + 18)
        b.append(rect(x, y, an2, 148, "white", r=16, stroke=LC_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, 120, c, r=3))
        b.append(T(x + 38, y + 68, [v], 52, c, weight="700"))
        for j, ln in enumerate(l.split("\\n")):
            b.append(T(x + 38, y + 104 + j * 26, [ln], 20, GRAY))
    y += 148 + 34

    y = seccion(b, y, "Las tres competencias que evalúa el ICFES en esta prueba")
    comp = [("CL", "Identificar y entender los contenidos locales", "qué significa una palabra, una "
             "frase, una cifra en su contexto"),
            ("SG", "Comprender cómo se articulan las partes", "qué hace cada párrafo y cómo se amarra "
             "con el siguiente"),
            ("RE", "Reflexionar y evaluar el contenido", "quién habla, qué quiere, qué deja afuera y "
             "si su argumento se sostiene")]
    an3 = (CW - 2 * 18) / 3
    alt3 = 52 + max(len(wrap_px(t + ": " + d, 22, an3 - 70)) for _, t, d in comp) * 31 + 20
    for i, (cod, t, d) in enumerate(comp):
        x = M + i * (an3 + 18)
        b.append(rect(x, y, an3, alt3, LC_BG, r=16, stroke=LC_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt3 - 28, LC, r=3))
        b.append(T(x + 40, y + 44, [cod], 26, LC, weight="700"))
        parrafo_j(b, x + 40, y + 54, t + ": " + d, an3 - 70, 22, INK, lh=31)
    y += alt3 + 34

    y = nota(b, M, y, CW,
        "Dos textos de esta área tocan figuras políticas colombianas vivas: la columna de la "
        "misión 5 y, por extensión, los casos de Sociales. La decisión de la Gerencia sobre cómo "
        "tratarlos está pendiente. Mientras tanto, este planeador trae la advertencia en la clase "
        "donde aplica y el encuadre que hay que darle: se lee el procedimiento, no el personaje.",
        ROJO, ROJO_BG, ROJO_LN, "Antes de empezar el área", 24) + 34

    y = seccion(b, y, "Lo que la coordinación revisa, sin haber entrado a la clase",
        "Tres cuadernos al azar del grupo. No se mira si la respuesta está buena: se mira si el "
        "texto está marcado. Marca tú mismo esta lista al terminar el sábado.")
    rev = ["Los textos del taller tienen subrayado y al menos una pregunta escrita al margen.",
           "«Mi primera idea, antes de hacer nada» tiene algo escrito en todas las preguntas.",
           "El instrumento de pensamiento está lleno en las diez, acertadas o no.",
           "La franja de vocabulario tiene la palabra nueva del día, en palabras del estudiante.",
           "Las dos caritas de la clase están marcadas y la casilla de la portada también."]
    b.append(rect(M, y, CW, 50 + len(rev) * 54, "white", r=18, stroke=LC_LN, sw=2))
    b.append(rect(M + 14, y + 16, 5, 18 + len(rev) * 54, LC, r=3))
    yy = y + 36
    for r_ in rev:
        b.append(checkbox(M + 44, yy - 14, 13, LC))
        parrafo_j(b, M + 100, yy - 22, r_, CW - 150, 24, INK)
        yy += 54
    pie(b, 1)
    svg_close(b, OUT + "plan_lc_01.svg")


def h2():
    b = svg_open()
    y = cabecera(b, "Las ocho clases", "Mapa del área de un vistazo", derecha="43",
                 dsub="páginas del cuaderno")
    y = seccion(b, y, "Qué se ve en cada sábado",
        "Seis clases de contenido, una por momento, y dos para el simulacro del área. El número "
        "de clases es fijo: no se recorta aunque un momento quede largo.")
    colx = [M, M + 120, M + 690, M + 1000, M + 1420]
    y = encabezado_tabla(b, y, list(zip(colx, ["CLASE", "QUÉ SE TRABAJA", "COMPETENCIA",
                                                "PARA EL PROFE", "ENTRENAMIENTO ICFES"])), 54)
    y += 2
    for n, (mis, tit, sub) in enumerate(CLASES, 1):
        alto = 96
        bg = "white" if mis else ORO_BG
        ln = LC_LN if mis else ORO_LN
        c = LC if mis else ORO
        b.append(rect(M, y, CW, alto, bg, r=14, stroke=ln, sw=2))
        b.append(rect(M + 12, y + 12, 5, alto - 24, c, r=3))
        b.append(T(colx[0] + 44, y + 62, [str(n)], 42, c, weight="700", anchor="middle"))
        b.append(T(colx[1] + 20, y + 44, [tit], 24, INK, weight="700"))
        b.append(T(colx[1] + 20, y + 74, [sub], 20, GRAY, style="italic"))
        if mis:
            d = MISIONES[mis]
            b.append(T(colx[2] + 20, y + 58, [d["competencia"].split(" · ")[0]], 23, LC, weight="700"))
            ns, nt = len(sellos_de(mis)), len(textos_de(mis))
            b.append(T(colx[3] + 20, y + 46, [f"{ns} sellos · {nt} textos"], 22, INK, weight="700"))
            b.append(T(colx[3] + 20, y + 76, ["para instalar y proyectar"], 19, GRAY))
            b.append(T(colx[4] + 20, y + 46, [f"{len(BANCO.get(mis, []))} preguntas Saber 11"],
                       22, VERDE, weight="700"))
            b.append(T(colx[4] + 20, y + 76, ["sin año verificado"], 19, GRAY))
        else:
            b.append(T(colx[2] + 20, y + 58, ["CL · SG · RE"], 23, GRAY))
            b.append(T(colx[3] + 20, y + 58, ["todo el área"], 22, GRAY))
            b.append(T(colx[4] + 20, y + 58, ["24 preguntas ya resueltas"], 22, GRAY))
        y += alto + 10
    y += 24

    y = seccion(b, y, "Las 24 estrategias del área, agrupadas por componente",
        "Son el vocabulario que el estudiante se lleva. Si al final del área puede nombrar las "
        "veinticuatro y decir para qué sirve cada una, el área cumplió, aunque falle preguntas.")
    grupos = [("Semántico", "momentos 1 y 2", [1, 2], LC, LC_BG, LC_LN),
              ("Sintáctico", "momentos 3 y 4", [3, 4], "#1F4E8C", "#EEF3FA", "#C6D6EA"),
              ("Pragmático", "momentos 5 y 6", [5, 6], ORO, ORO_BG, ORO_LN)]
    an = (CW - 2 * 18) / 3
    alto = 0
    for nom, de, mm, c, bg, ln in grupos:
        lins = sum(len(wrap_px(e, 21, an - 152)) for m in mm for e in MISIONES[m]["estr"])
        alto = max(alto, 104 + lins * 29 + 8 * 14)
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
    pie(b, 2)
    svg_close(b, OUT + "plan_lc_02.svg")


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
    svg_close(b, OUT + f"plan_lc_{2 + parte:02d}.svg")


def hoja_clase(mis):
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Clase {mis}", f"Momento {mis} · {d['comp']} · páginas {d['pags']}",
                 derecha=f"{mis}", dsub="de 8 clases")

    y = seccion(b, y, "Las cuatro estrategias del momento",
        "Son el vocabulario de la clase. El estudiante las ve rotuladas en cada pregunta de su "
        "cuaderno, así que conviene nombrarlas igual en voz alta.")
    an = (CW - 3 * 16) / 4
    alt = max(52 + len(wrap_px(e, 23, an - 60)) * 32 for e in d["estr"])
    for i, e in enumerate(d["estr"]):
        x = M + i * (an + 16)
        b.append(rect(x, y, an, alt, "white", r=16, stroke=LC_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt - 28, COLS_EST[i], r=3))
        b.append(T(x + 38, y + 40, [f"ESTRATEGIA {i+1}"], 16, COLS_EST[i], weight="700", ls=1.3))
        parrafo_j(b, x + 38, y + 50, e, an - 60, 23, INK, weight="700", lh=32)
    y += alt + 28

    y = nota(b, M, y, CW, d["instala"], ORO, ORO_BG, ORO_LN,
             "Alto · aquí entra el profe: lo que tienes que instalar antes del taller", 25) + 14
    y = nota(b, M, y, CW, limpia(d["ojo"]), ROJO if "⚠" in d["ojo"] else LC,
             ROJO_BG if "⚠" in d["ojo"] else LC_BG, ROJO_LN if "⚠" in d["ojo"] else LC_LN,
             "Ojo con esto", 23) + 28

    # los sellos registrados de esta misión
    ss = sellos_de(mis)
    if ss:
        y = seccion(b, y, f"Los {len(ss)} sellos de esta clase",
            "En estas preguntas el cuaderno le dice al estudiante «alto, aquí entra el profe». "
            "Si llegas sin el concepto preparado, el sello se vuelve un hueco.")
        for s in ss:
            _, _, pag, preg, saber, _, _ = s
            lin = wrap_px(saber, 23, CW - 330)
            h = max(64, 24 + len(lin) * 32)
            b.append(rect(M, y, CW, h, ORO_BG, r=12, stroke=ORO_LN, sw=1.8))
            b.append(rect(M + 10, y + 10, 4, h - 20, ORO, r=2))
            b.append(T(M + 36, y + h / 2 + 8, [f"pág. {pag} · preg. {preg}"], 21, ORO, weight="700"))
            parrafo_j(b, M + 290, y + (h - len(lin) * 32) / 2 - 4, saber, CW - 330, 23, INK, lh=32)
            y += h + 6
        y += 20

    # las diez preguntas
    y = seccion(b, y, "Las diez preguntas del libro y su instrumento")
    cx = [M, M + 96, M + 560, M + 1240]
    y = encabezado_tabla(b, y, list(zip(cx, ["N.º", "ESTRATEGIA", "INSTRUMENTO DE PENSAMIENTO",
                                              "CONTEXTO"])), 46)
    for p, est, ins, ctx in TALLER.get(mis, []):
        i_est = d["estr"].index(est) if est in d["estr"] else 0
        c = COLS_EST[i_est]
        l_ins = wrap_px(ins, 21, 650)
        l_ctx = wrap_px(ctx, 20, 620)
        h = max(52, 18 + max(len(l_ins), len(l_ctx)) * 28)
        b.append(rect(M, y, CW, h, LC_BG if p <= 2 else "white", r=10, stroke=LC_LN, sw=1.6))
        b.append(rect(M + 9, y + 9, 4, h - 18, c, r=2))
        b.append(T(cx[0] + 54, y + h / 2 + 9, [str(p)], 24, c, weight="700", anchor="middle"))
        b.append(T(cx[1] + 18, y + h / 2 + 7, [f"E{i_est+1}"], 19, c, weight="700"))
        b.append(T(cx[1] + 56, y + h / 2 + 7, [est], 19, GRAY))
        parrafo_j(b, cx[2] + 18, y + (h - len(l_ins) * 28) / 2 - 4, ins, 650, 21, INK, lh=28)
        parrafo_j(b, cx[3] + 18, y + (h - len(l_ctx) * 28) / 2 - 4, ctx, 620, 20, GRAY, lh=28)
        y += h + 5
    y += 26
    av = AVISOS.get(mis, [])
    if av:
        y = seccion(b, y, "Lo que tienes que saber del libro antes de entrar",
            "Salió de resolver las diez preguntas una por una. No se le esconde al estudiante.")
        for preg, sev, que, hacer in av:
            c, bg, ln = SEV[sev]
            texto = que + "  →  " + hacer
            lin = wrap_px(texto, 21, CW - 440)
            h = max(64, 22 + len(lin) * 29)
            b.append(rect(M, y, CW, h, bg, r=12, stroke=ln, sw=1.8))
            b.append(rect(M + 10, y + 10, 4, h - 20, c, r=2))
            b.append(T(M + 36, y + h / 2 - 4, [preg.upper()], 18, c, weight="700", ls=1))
            chip(b, M + 36, y + h / 2 + 6, sev.upper(), c, size=13, pad=10, fill="white", txtc=c)
            parrafo_j(b, M + 400, y + (h - len(lin) * 29) / 2 - 5, texto, CW - 440, 21, INK, lh=29)
            y += h + 6
    else:
        y = nota(b, M, y, CW,
            "Las diez preguntas de este momento se resolvieron una por una y ninguna dejó aviso. "
            "Es la única misión del área así: si encuentras algo, anótalo en el registro.",
            VERDE, VERDE_BG, VERDE_LN, "Lo que tienes que saber del libro", 23)
    pie(b, 3 + mis * 2)
    svg_close(b, OUT + f"plan_lc_{3 + mis * 2:02d}.svg")


def hoja_clase_b(mis):
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Clase {mis} · minuto a minuto", "El sábado, los textos y la evaluación",
                 derecha="120", dsub="minutos")

    base = BASE[mis]
    t_pags = [base, base + 1, base + 3, base + 4, base + 5]
    i_pags = [base + 2, base + 6]
    ins = {p: i for p, e, i, c in TALLER.get(mis, [])}
    din = DINAMICAS[mis]
    concreto = [
        f"Dos o tres renglones proyectados, sin contexto. Cada uno subraya la palabra que más pesa. "
        f"Dinámica E1 «{din[0][0]}» ({din[0][1]}').",
        f"Pregunta modelo del libro, a la vista todo el momento. Respuestas a mano alzada antes de "
        f"releer. Se abre la página {t_pags[0]} solo en «mi primera idea».",
        f"Las diez preguntas por bloques: 1-2 en pantalla (página {t_pags[0]}, «{ins.get(1,'—')}» "
        f"y «{ins.get(2,'—')}»), después 3-4, 5-6, 7-8 y 9-10 en las páginas {t_pags[1]}, "
        f"{t_pags[2]}, {t_pags[3]} y {t_pags[4]}. Cada 18 minutos, la dinámica del bloque.",
        f"Reto del corte: «{RETOS[mis][0]}». Equipos de tres, cada uno responde en SU cuaderno. "
        f"La defensa se hace leyendo el renglón en voz alta.",
        f"Entrenamiento ICFES, páginas {i_pags[0]} y {i_pags[1]}. Cuatro preguntas Saber 11, en "
        f"silencio y con reloj.",
        f"Solo las falladas, con el renglón que las sostiene. Cada uno escribe la palabra nueva del "
        f"día, «lo que me llevo», su carita de salida y la casilla {mis} de la portada.",
    ]
    y = seccion(b, y, "El sábado, minuto a minuto",
        "Las seis fases con el contenido de este momento puesto encima.")
    reloj = 0
    for (nom, mins, c, *_), txt in zip(FASES, concreto):
        lin = wrap_px(txt, 22, CW - 480)
        h = max(72, 26 + len(lin) * 30)
        b.append(rect(M, y, CW, h, "white", r=14, stroke=LC_LN, sw=1.8))
        b.append(rect(M + 12, y + 12, 5, h - 24, c, r=3))
        b.append(T(M + 40, y + h / 2 - 2, [f"{reloj:02d}'–{reloj+mins:02d}'"], 22, c, weight="700"))
        b.append(T(M + 40, y + h / 2 + 26, [nom], 19, GRAY))
        parrafo_j(b, M + 440, y + (h - len(lin) * 30) / 2 - 5, txt, CW - 480, 22, INK, lh=30)
        reloj += mins
        y += h + 6
    y += 22

    # textos que hay que proyectar
    tt = textos_de(mis)
    if tt:
        y = seccion(b, y, f"Los {len(tt)} textos que tienes que proyectar",
            "El cuaderno trae el párrafo con la evidencia; el texto completo lo proyectas tú. "
            "Los íntegros están en TEXTOS_GUIA_DOCENTE.md.")
        for t in tt:
            _, _, pags, texto, fuente, tipo, completo, nota_ = t
            alerta = "⚠" in nota_
            c, bg, ln = (ROJO, ROJO_BG, ROJO_LN) if alerta else (LC, "white", LC_LN)
            linea2 = f"{fuente} · {tipo}"
            l2 = wrap_px(linea2, 19, CW - 520)
            l3 = wrap_px(limpia(nota_), 20, 400)
            h = max(74, 46 + len(l2) * 26, 30 + len(l3) * 27)
            b.append(rect(M, y, CW, h, bg, r=12, stroke=ln, sw=1.8))
            b.append(rect(M + 10, y + 10, 4, h - 20, c, r=2))
            b.append(T(M + 36, y + 34, [f"pág. {pags}"], 19, c, weight="700"))
            b.append(T(M + 190, y + 34, [texto], 22, INK, weight="700"))
            parrafo_j(b, M + 190, y + 40, linea2, CW - 620, 19, GRAY, lh=26)
            parrafo_j(b, W - M - 430, y + (h - len(l3) * 27) / 2 - 4, limpia(nota_), 400, 20,
                      c if alerta else GRAY, lh=27)
            y += h + 6
        y += 20

    # ICFES
    banco = BANCO.get(mis, [])
    y = seccion(b, y, "Las cuatro preguntas Saber 11",
        "Van sin año y sin «oficial»: el membrete dice «Pregunta Saber 11» y nada más (regla 7, "
        "Nelson 10 nov).")
    for k, (x4, est, ins_, ctx) in enumerate(INS_ICFES.get(mis, [])):
        fila = banco[k] if k < len(banco) else {}
        ctx_ = fila.get("contexto", "—")
        l_c = wrap_px(ctx_, 21, 740)
        l_i = wrap_px(ins_, 20, 720)
        h = max(64, 22 + max(len(l_c), len(l_i)) * 29)
        b.append(rect(M, y, CW, h, "white", r=12, stroke=VERDE_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, h - 20, VERDE, r=2))
        b.append(T(M + 36, y + h / 2 + 8, [f"P{x4}"], 21, VERDE, weight="700"))
        parrafo_j(b, M + 100, y + (h - len(l_c) * 29) / 2 - 4, ctx_, 740, 21, INK, weight="700", lh=29)
        parrafo_j(b, M + 870, y + (h - len(l_i) * 29) / 2 - 4, ins_, 720, 20, GRAY, style="italic", lh=29)
        cl = fila.get("clave", "").strip()
        b.append(rect(W - M - 96, y + h / 2 - 22, 64, 44, VERDE_BG, r=10, stroke=VERDE, sw=2))
        b.append(T(W - M - 64, y + h / 2 + 10, [cl or "—"], 26, VERDE, weight="700", anchor="middle"))
        y += h + 6
    y += 26
    y = seccion(b, y, "Después de la clase · tu registro",
        "Se llena el mismo sábado, antes de salir. Esto no lo ve el estudiante.")
    # El alto de cada casilla sale del espacio que queda antes del pie (2470),
    # no de un número fijo: la clase 6 trae cinco textos y no le cabía el de 232.
    alto_reg = int(min(232, (2470 - y - 14) / 2))
    registro_docente(b, y, alto=alto_reg, campos=[
        ("¿Qué texto hubo que releer en voz alta?", "y en qué renglón se destrabó el grupo"),
        ("¿A quién hay que volver la próxima clase?", "nombres, no «algunos»"),
        ("¿Qué cuaderno quedó con el texto sin marcar?", "aunque haya acertado la respuesta"),
        ("¿Qué cambiarías de esta clase?", "va al reporte de los especialistas")])
    pie(b, 4 + mis * 2)
    svg_close(b, OUT + f"plan_lc_{4 + mis * 2:02d}.svg")


def h17():
    """Clases 7 y 8 · el simulacro del área y su devolución."""
    b = svg_open()
    y = cabecera(b, "Clases 7 y 8", "El simulacro del área y su devolución",
                 derecha="24", dsub="preguntas del simulacro")
    y = seccion(b, y, "Qué son estas dos clases",
        "No traen contenido nuevo. Trabajan las seis franjas de simulacro que el estudiante ya "
        "tiene en su cuaderno, una por momento, y que hasta ahora resolvió de a poco.")
    dos = [("Clase 7 · el simulacro", ROJO, ROJO_BG, ROJO_LN,
            "Condiciones de prueba, 90 minutos de reloj, en silencio",
            ["Las 24 preguntas Saber 11 del área, seguidas, con los textos completos.",
             "El estudiante SÍ puede subrayar: en la prueba real también puede, y es lo que entrenó.",
             "No se responde ninguna duda, ni de vocabulario.",
             "Los últimos 30 minutos: cada uno cuenta sus aciertos por competencia (CL, SG, RE)."]),
           ("Clase 8 · la devolución", VERDE, VERDE_BG, VERDE_LN,
            "Reparación con el texto marcado de la primera vez",
            ["Se eligen las cinco preguntas que más falló el grupo.",
             "Cada estudiante compara el subrayado del simulacro con el de su hoja de taller.",
             "La pregunta que gobierna la clase: ¿qué subrayaste esta vez que no subrayaste antes?",
             "Al final, la página de cierre del cuaderno y la franja de vocabulario completa."])]
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
    y += alto + 34

    y = nota(b, M, y, CW,
        "El simulacro no se califica con nota. Se cuenta por competencia: contenidos locales, "
        "sentido global y reflexión. Lo que importa es que el estudiante vea en cuál de las tres "
        "se le va el puntaje. En Lectura Crítica casi siempre es la tercera, porque es la única "
        "que no se responde buscando: hay que juzgar.",
        ORO, ORO_BG, ORO_LN, "Cómo se lee el resultado", 25) + 34

    y = seccion(b, y, "Conteo por competencia",
        "Llénalo con el grupo en el tablero al final de la clase 7.")
    comp = [("CL · contenidos locales", "qué dice"), ("SG · sentido global", "cómo se arma"),
            ("RE · reflexionar y evaluar", "qué quiere y si se sostiene")]
    an2 = (CW - 2 * 18) / 3
    for i, (nom, de) in enumerate(comp):
        x = M + i * (an2 + 18)
        b.append(rect(x, y, an2, 200, "white", r=16, stroke=LC_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, 172, LC, r=3))
        b.append(T(x + 40, y + 46, [nom], 23, INK, weight="700"))
        b.append(T(x + 40, y + 76, [de], 20, GRAY, style="italic"))
        b.append(T(x + 40, y + 120, ["aciertos del grupo"], 19, GRAY))
        b.append(rect(x + 40, y + 132, an2 - 80, 50, LC_BG, r=12, stroke=LC_LN, sw=1.8))
    y += 200 + 34

    y = seccion(b, y, "Las cinco preguntas que se reparan en la clase 8")
    cx = [M, M + 200, M + 560, M + 1160]
    y = encabezado_tabla(b, y, list(zip(cx, ["N.º", "MOMENTO Y PÁGINA", "QUÉ HABÍA QUE SUBRAYAR",
                                              "QUÉ FALLÓ EL GRUPO"])))
    for k in range(1, 6):
        b.append(rect(M, y, CW, 80, "white", r=12, stroke=LC_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, 60, VERDE, r=2))
        b.append(T(cx[0] + 54, y + 52, [str(k)], 26, VERDE, weight="700", anchor="middle"))
        for xi, xf in [(cx[1] + 18, cx[2] - 20), (cx[2] + 18, cx[3] - 20), (cx[3] + 18, W - M - 30)]:
            b.append(line(xi, y + 56, xf, y + 56, "#E6EAF0", 2))
        y += 86
    pie(b, 17)
    svg_close(b, OUT + "plan_lc_17.svg")


def hoja_dinamicas(mis):
    d = MISIONES[mis]
    b = svg_open()
    y = cabecera(b, f"Dinámicas · Misión {mis}",
                 "Movimiento con sentido: el cuerpo ensaya lo que después hará la mente",
                 derecha=f"{mis}", dsub="de 6 misiones")
    y = nota(b, M, y, CW,
        "La dinámica debe ser isomorfa a la estrategia: lo que hace el cuerpo tiene que ser el "
        "mismo movimiento que después hará la mente frente al texto. Antes de usar una, responde "
        "esto — ¿qué paso de la estrategia está ejercitando? Si no hay respuesta, es recreo, no clase.",
        ORO, ORO_BG, ORO_LN, "La regla para aprobar cualquier dinámica", 25) + 30
    for i, din in enumerate(DINAMICAS[mis]):
        y = bloque_dinamica(b, y, i, din, d["estr"][i], COLS_EST[i])
    bloque_reto(b, y + 8, mis, RETOS[mis])
    pie(b, 17 + mis)
    svg_close(b, OUT + f"plan_lc_{17 + mis:02d}.svg")


def h24():
    b = svg_open()
    total = sum(len(v) for v in AVISOS.values())
    y = cabecera(b, "Cierre del área", "Los avisos del libro, juntos, y lo que hay que devolver",
                 derecha=str(total), dsub="avisos del libro")
    y = seccion(b, y, f"Los {total} avisos del libro, en una sola lista",
        "Para repasarlos antes de empezar el área. Ninguno se le oculta al estudiante: si lo "
        "detecta y lo escribe, aprendió más que el que marcó la opción esperada.")
    cx = [M, M + 290, M + 450]
    y = encabezado_tabla(b, y, list(zip(cx, ["DÓNDE", "SEVERIDAD", "QUÉ PASA Y QUÉ HACES"])))
    for m in range(1, 7):
        for preg, sev, que, hacer in AVISOS.get(m, []):
            c, bg, ln = SEV[sev]
            texto = que + "  →  " + hacer
            lin = wrap_px(texto, 21, CW - 500)
            h = max(64, 22 + len(lin) * 29)
            b.append(rect(M, y, CW, h, bg, r=12, stroke=ln, sw=1.8))
            b.append(rect(M + 10, y + 10, 4, h - 20, c, r=2))
            b.append(T(cx[0] + 36, y + h / 2 + 8, [f"M{m} · {preg}"], 20, INK, weight="700"))
            chip(b, cx[1] + 10, y + h / 2 - 15, sev.upper(), c, size=14, pad=11, fill="white", txtc=c)
            parrafo_j(b, cx[2] + 18, y + (h - len(lin) * 29) / 2 - 5, texto, CW - 500, 21, INK, lh=29)
            y += h + 6
    y += 26
    y = seccion(b, y, "Qué tienes que devolver al terminar el área")
    dev = [("Los seis registros de clase", "con nombres, no «algunos»"),
           ("El conteo por competencia del simulacro", "el dato que decide el refuerzo"),
           ("Las franjas de vocabulario", "tres cuadernos al azar, fotografiados"),
           ("Los avisos nuevos que encuentres", "la lista se construyó resolviendo, y seguro falta alguno")]
    for t, s_ in dev:
        b.append(rect(M, y, CW, 70, "white", r=14, stroke=LC_LN, sw=2))
        b.append(rect(M + 14, y + 12, 5, 46, ORO, r=3))
        b.append(checkbox(M + 42, y + 22, 13, LC))
        b.append(T(M + 100, y + 44, [t], 23, INK, weight="700"))
        b.append(T(M + 700, y + 44, [s_], 21, GRAY))
        y += 80
    pie(b, 24)
    svg_close(b, OUT + "plan_lc_24.svg")


def build():
    h1(); h2()
    hoja_momentos(1); hoja_momentos(2)
    for m in range(1, 7):
        hoja_clase(m); hoja_clase_b(m)
    h17()
    for m in range(1, 7):
        hoja_dinamicas(m)
    h24()
    return [f"plan_lc_{i:02d}" for i in range(1, TOTAL + 1)]


if __name__ == "__main__":
    print(len(build()), "hojas del planeador de Lectura Crítica")
