#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLANEADOR DEL DOCENTE · FÍSICA · las ocho clases del área.

    python3 plan_fis.py [--pdf]        (el PDF va a entregables/EDUCATE_Planeador_Fisica.pdf)

Mismo modelo aprobado en el piloto de Matemáticas y ya entregado en Lectura Crítica, Sociales y
Biología (plan_bio.py, que es el que se copia aquí): seis momentos de 15·20·35·20·20·10, «tu
aporte» acotado en cada uno y un banco de dinámicas isomorfas a las estrategias. Usa el motor de
plan_piezas.py sin cambiarlo; el dibujo de las hojas sale de plan_bio.py, adaptado aquí.

Lo propio del área: donde Biología tiene el dato y su comparación, Física tiene LA FLECHA CON SU
NOMBRE de la portada del área (página 225): nada cambia porque sí; cada fuerza se dibuja como una
flecha con su nombre y cada julio tiene que aparecer en la cuenta. Doce sellos «Alto · aquí entra
el profe» (todos del taller), tres claves del libro de reserva alta (M2 P10, M4 P3 y M4 P9) y
siete de reserva media que el profe tiene que saber defender o discutir.

Seguridad de las dinámicas (encargo del 10 nov): ninguna usa electricidad real ni lanza objetos.
Las cargas, los circuitos y las ondas se hacen con personas, cuerdas, cinta y fichas; se camina,
nunca se corre; las cuerdas se halan suave y lo que se carga es una mochila liviana.

Para las guías (clase_viva_fis.py), con los mismos nombres de plan_bio.py:
    FASES  CLASES  BASE  LIBRO  PAG_LIBRO  MISIONES  AVISOS  TALLER  INS_ICFES  BANCO  SELLOS
    SABERES  DINAMICAS  RETOS  CLAVES  ACTIVACION  PROBLEMATIZADORA  PREGUNTA_AREA
    NO_ES_TU_FUERTE  COLS_MIS  COMP_EST  COMP_NOM  COMP_ICFES  ASED
COMP_ICFES {misión: [competencia de P1…P4]} es la que el cuaderno le pone a cada pregunta de
entrenamiento (campo comp de fisN_icfes.py, leído sin importar el módulo). COMP_EST sale de ahí.
ASED {(misión, k)} son las preguntas de entrenamiento que salen del compilado ASED (columna fuente
de tablero/icfes.csv): M1 P1 y M2 P1. No son del ICFES; Nelson decide si se reemplazan.

Claves del libro: copiadas del docstring de fis1.py … fis6.py (resueltas a mano el 7 nov) y
comprobadas al construir con `verificar()`. Las del entrenamiento: tablero/icfes.csv, cruzadas con
el docstring de fisN_icfes.py y resueltas otra vez el 10 nov, con cuentas y unidades (TEXTOS_FIS.md).
Las 24 coinciden.

Membrete (Nelson, 10 nov): «Pregunta Saber 11», sin año ni «oficial». En este planeador las
preguntas de entrenamiento se llaman «preguntas tipo Saber 11».
"""
import ast, csv, re
from plan_piezas import *
import plan_piezas as PZ

FIS = "#5C7A1E"; FIS_BG = "#F2F5EA"; FIS_LN = "#CBD8B0"
TOTAL = 24
configurar(FIS, FIS_BG, FIS_LN, "Física", TOTAL)
AREA_CSV = "Física"

AZUL = "#242478"; ROJO_E = "#A82424"; ORO_E = "#C9821B"
# El cierre va en pizarra: el verde oliva es el color del área (y de la activación).
PIZARRA = "#4A5A70"

# Los colores de las cuatro estrategias, tal como salen en los chips del cuaderno (EST de fisN.py).
COLS_MIS = {1: [AZUL, ROJO_E, ORO_E, MORADO], 2: [AZUL, ROJO_E, ORO_E, MORADO],
            3: [AZUL, ROJO_E, ORO_E, MORADO], 4: [AZUL, ROJO_E, MORADO, ORO_E],
            5: [AZUL, ROJO_E, MORADO, ORO_E], 6: [AZUL, ROJO_E, MORADO, ORO_E]}
COLS_EST = COLS_MIS[1]

# ─────────────────────────── los seis momentos ───────────────────────────
# El reparto es el aprobado: 15 · 20 · 35 · 20 · 20 · 10 = 120. No se cambia.
FASES = [
    ("Activación", 15, FIS,
     "Que el estudiante describa un fenómeno corto diciendo qué cambió y qué lo causó —qué fuerza, "
     "qué calor, qué carga— antes de explicarlo con fórmulas y antes de ver cualquier opción.",
     ["Proyecta o lee una observación de dos o tres renglones sin decir de dónde salió.",
      "Pide dos respuestas, en voz alta o en el tablero: qué cambió y qué lo causó, dicho como una "
      "flecha con nombre («el piso frena…», «el calor va de… a…»).",
      "Ejecuta la dinámica de apertura según la estrategia del encuentro."],
     "No explica el fenómeno ni acepta todavía fórmulas. Si alguien dice «es por la gravedad» o «es "
     "la energía», le devuelve la pregunta: «¿quién empuja a quién, y hacia dónde?». El cuaderno "
     "sigue cerrado.",
     "Proyector o tablero con la observación. Todavía no se abre el cuaderno."),
    ("Pregunta problematizadora", 20, "#1F4E8C",
     "Que el estudiante compruebe que en Física la respuesta sale de la causa dibujada o de la cuenta "
     "con unidades, y no de la opción que suena más técnica, usando la pregunta modelo del libro.",
     ["Presenta la pregunta modelo del libro y la deja a la vista todo el momento.",
      "Pide respuestas a mano alzada ANTES de dibujar o calcular nada, y las anota en el tablero.",
      "Hace la pregunta que gobierna el área: ¿qué lo causó? Muéstrame la flecha o el julio que lo "
      "explica.",
      "Revela la clave solo al final y trabaja por qué cae cada una de las otras tres."],
     "Regla del momento: nadie justifica con «así dice la fórmula» ni con «eso es obvio». Toda "
     "intervención señala una flecha del dibujo, un número con su unidad o un renglón del enunciado.",
     "Libro abierto en la pregunta modelo. Cuaderno solo en «mi primera idea»."),
    ("Desarrollo guiado", 35, "#3B3BA6",
     "Que el estudiante haga el instrumento —el diagrama de fuerzas, la cuenta con unidades, la "
     "ficha del experimento o la cadena de la energía— antes de mirar las opciones, y deje por "
     "escrito de dónde lo sacó.",
     ["Entrega las hojas del momento y trabaja por bloques: 1-2, 3-4, 5-6, 7-8 y 9-10.",
      "Antes de que marquen, verifica que el instrumento tenga la flecha dibujada o la cuenta escrita "
      "con su unidad.",
      "Entre bloques, introduce la dinámica de la estrategia que viene: seis minutos, no más.",
      "Cuando aparece un sello «Alto · aquí entra el profe», explica el concepto en dos minutos y sigue."],
     "No resuelve la cuenta en el tablero antes que ellos ni dicta la respuesta. Si un estudiante se "
     "traba, le pregunta qué cambió y quién lo causó; si la cuenta no tiene unidades, la devuelve "
     "antes de mirar el número.",
     "Cuaderno, las cinco hojas de taller. Libro, en las preguntas 1 a 10."),
    ("Reto en equipo", 20, MORADO,
     "Que el estudiante defienda su explicación con el dibujo o la cuenta en la mano y acepte que "
     "otro equipo puede ver una fuerza, una pérdida o una variable que él no vio.",
     ["Arma equipos de tres y entrega el reto del corte de este momento.",
      "Exige que cada integrante llegue con su instrumento YA diligenciado individualmente.",
      "Da tres minutos de defensa por equipo: muestran la flecha, la cuenta o la variable que los respalda.",
      "Cierra mostrando qué fuerza, qué julio o qué variable quedó por fuera en cada propuesta."],
     "El equipo discute, pero cada uno escribe en SU tarjeta del reto. No se acepta una defensa que "
     "diga «porque sí» o «eso dice la fórmula»: se señala la flecha, el número con su unidad o la "
     "variable que se controló.",
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
     "Que el estudiante nombre la estrategia que usó y se lleve un concepto del día —una ley, una "
     "magnitud o una relación— escrito en sus propias palabras.",
     ["Socializa solo las preguntas que el grupo falló, pidiendo la flecha o la cuenta que las resuelve.",
      "Pide que lean en voz alta su salvavidas: lo mínimo que sí tenían claro.",
      "Cada uno escribe el concepto del día en «Palabras que me frenaron» y la causa que encontró en "
      "la portada del área."],
     "No dicta la definición ni la fórmula. El concepto se escribe como el estudiante lo entendió; si "
     "quedó mal entendido, eso se ve en la hoja y se corrige la próxima clase.",
     "Cuaderno: «Palabras que me frenaron», «lo que me llevo», carita de salida y portada del área."),
]

CLASES = [
    (1, "Momento 1 · Mecánica clásica", "páginas 226 a 232 del cuaderno"),
    (2, "Momento 2 · Termodinámica", "páginas 233 a 239 del cuaderno"),
    (3, "Momento 3 · Electromagnetismo", "páginas 240 a 246 del cuaderno"),
    (4, "Momento 4 · Eventos ondulatorios", "páginas 247 a 253 del cuaderno"),
    (5, "Momento 5 · Mecánica clásica · la energía", "páginas 254 a 260 del cuaderno"),
    (6, "Momento 6 · Termodinámica · cierre del área", "páginas 261 a 267 del cuaderno"),
    (None, "Simulacro del área", "las 24 preguntas tipo Saber 11, en condiciones de prueba"),
    (None, "Socialización del simulacro", "devolución, reparación y cierre del área"),
]

BASE = {1: 226, 2: 233, 3: 240, 4: 247, 5: 254, 6: 261}
LIBRO = {1: (205, 208), 2: (216, 218), 3: (226, 228), 4: (236, 239), 5: (247, 250), 6: (259, 262)}


def _pag_libro():
    """Página del libro de cada pregunta: Q[n]["pag"] de fisN.py («la lees en tu libro, página N»)."""
    out = {}
    for m in range(1, 7):
        src = open(f"/home/claude/libro/fis{m}.py", encoding="utf-8").read()
        q = {int(n): int(p) for n, p in re.findall(r"(\d+): dict\(n=\d+, est=\d, pag=(\d+)", src)}
        out[m] = [q[n] for n in range(1, 11)]
    return out


PAG_LIBRO = _pag_libro()

# Las tres competencias de Ciencias Naturales en el Saber 11.
COMP_NOM = {"UC": "Uso comprensivo del conocimiento científico", "EF": "Explicación de fenómenos",
            "IN": "Indagación"}
_COD = {"uso comprensivo": "UC", "explicación de fenómenos": "EF", "indagación": "IN"}

MISIONES = {
 1: dict(comp="Mecánica clásica", pags="226 a 232",
   tema="Fuerzas, movimiento y energía",
   competencia="UC e IN · fuerzas, gráficas y energía",
   estr=["Las fuerzas, una por una", "La gráfica cuenta el movimiento",
         "El experimento justo", "Lo que se conserva"],
   instala="Que nada se mueve ni se detiene porque sí: cada cambio de movimiento tiene una fuerza con "
           "nombre, dirección y alguien que la hace. Que una gráfica de rapidez se lee tramo por tramo, "
           "que un experimento justo cambia una sola cosa y que la energía no se pierde: cambia de forma.",
   ojo="La figura de la pregunta 3 dibuja mal el diagrama de fuerzas (la normal vertical y las dos "
       "componentes del peso hacia abajo) y la de la 8 pone la flecha centrípeta hacia afuera. Que "
       "dibujen el suyo antes de mirar el del libro. La pregunta 6 tiene dos opciones defendibles.",
   cierre="La pregunta 5 dice «equilibrio» donde la física dice «conservación del momento angular». "
          "Vale la pena separar las dos palabras: el bailarín no está quieto, está girando con el giro "
          "total constante."),
 2: dict(comp="Termodinámica", pags="233 a 239",
   tema="El calor, la temperatura y los cambios de fase",
   competencia="EF y UC · calor, cuentas y partículas",
   estr=["El calor va del caliente al frío", "La cuenta del calor",
         "Lo que hacen las partículas", "El ambiente decide el cambio de fase"],
   instala="Que el calor siempre va del cuerpo más caliente al más frío, que se cuenta con "
           "Q = m · c · ΔT llevando las unidades, que la temperatura es la agitación de las partículas "
           "y que el ambiente —la presión, el frío— decide cuándo cambia de fase una sustancia.",
   ojo="La pregunta 10 tiene dos opciones correctas (la A y la D dan el mismo 0,25) y la 4 explica al "
       "revés cómo funciona la olla a presión. Las dos están en la hoja de esta clase, con qué hacer.",
   cierre="La pregunta 9 mezcla kilogramos con cal/(g·°C). Cierra con eso: un número sin su unidad no "
          "se puede multiplicar con otro."),
 3: dict(comp="Electromagnetismo", pags="240 a 246",
   tema="Lo que mueve a las cargas",
   competencia="EF, UC e IN · cargas, campos y datos",
   estr=["Busca el dato que decide", "Dibuja el campo primero",
         "Signo, sentido y unidad", "Del modelo al mecanismo"],
   instala="Que antes de opinar se busca el dato que decide, que el campo se dibuja antes de elegir "
           "una figura, que toda fuerza eléctrica lleva signo, sentido y unidad, y que el modelo "
           "—electrones que se mueven, campos que cambian, dominios que se desordenan— explica el "
           "mecanismo paso por paso.",
   ojo="La B es clave en cinco de las diez preguntas y en la 6 las flechas de la figura que es clave "
       "están al revés. En la 1 hay dos opciones defendibles. Exige el instrumento lleno antes de "
       "mirar las opciones.",
   cierre="La pregunta 7 trae la carga y la fuerza sin unidades. Cierra pidiéndolas: 2 × 10⁻⁶ C por "
          "400 N/C da 8 × 10⁻⁴ N."),
 4: dict(comp="Eventos ondulatorios", pags="247 a 253",
   tema="La fuente marca el ritmo",
   competencia="EF, UC e IN · ondas, luz y sonido",
   estr=["La fuente pone la frecuencia", "Dibújalo antes de elegir",
         "Concluye solo lo observado", "Lee la tabla y su escala"],
   instala="Que la frecuencia la pone la fuente y la rapidez la pone el medio, que antes de elegir se "
           "dibuja la onda o el rayo, que solo se concluye lo que se observó y que una tabla se lee con "
           "su escala: en decibeles, cada 10 es un factor 10.",
   ojo="Dos claves de reserva alta: en la 3 el esquema tiene dos rayos con la letra A, y en la 9 "
       "ninguna opción da la razón física. Otras dos de reserva media (4 y 6). Es la misión que más "
       "le pide al profe: prepara los cuatro sellos.",
   cierre="El repaso del libro (página 236) dice que en el caucho la onda llega tarde «por su "
          "absorción». Cierra corrigiéndolo: llega tarde porque el caucho es blando, poco rígido."),
 5: dict(comp="Mecánica clásica", pags="254 a 260",
   tema="La energía que sube, corre y se escapa",
   competencia="UC, EF e IN · energía, fuerzas y control",
   estr=["Cada magnitud con su fórmula y su unidad", "¿Quién empuja y hacia dónde?",
         "Una variable a la vez", "El principio que explica lo que se ve"],
   instala="Que cada magnitud tiene su fórmula y su unidad (Ep = m · g · h, Ec = ½ · m · v², "
           "W = F · d · cos θ), que antes de hablar de trabajo se pregunta quién empuja y hacia dónde, "
           "que un experimento cambia una variable a la vez y que un fenómeno se explica con el nombre "
           "de su principio.",
   ojo="La pregunta 8 tiene dos valoraciones defendibles (A y D) y la 1 dice que el astronauta «pesa "
       "80 kg». La 3 pide un concepto que el estudiante no trae, la relatividad general: es un sello.",
   cierre="La pregunta 6 es la más contraria a la intuición: sostener un paquete quieto cansa, pero no "
          "hace trabajo sobre él. Ciérrala con la fórmula: sin desplazamiento, W = 0."),
 6: dict(comp="Termodinámica", pags="261 a 267",
   tema="La energía que se transforma",
   competencia="UC, EF e IN · cierre del área",
   estr=["Multiplica, divide y lleva las unidades", "La energía no desaparece: cambia de forma",
         "¿Alcanzan los datos para esa conclusión?", "Cuando algo deja de cambiar: el equilibrio"],
   instala="Que la energía que entra es igual a la útil más la que se va como calor, que la eficiencia "
           "es una fracción sin unidades, que una conclusión no puede ser más grande que sus datos y "
           "que el equilibrio llega cuando lo que entra iguala lo que sale. Recoge las cinco misiones.",
   ojo="Tres preguntas de la estrategia de los datos (1, 4 y 10) tienen una segunda opción "
       "defendible. No castigues a quien defienda la otra con números: pídele la cuenta.",
   cierre="Es el cierre del área. La frase de la portada —«si te queda energía que no sabes a dónde "
          "fue, todavía no has terminado»— vale para las seis misiones."),
}

# Claves del libro: docstring de fis1.py … fis6.py (verificar() las compara al construir).
CLAVES = {
 1: dict(zip(range(1, 11), "ACBACBBADB")),
 2: dict(zip(range(1, 11), "ABCBCACDCD")),
 3: dict(zip(range(1, 11), "DCBABBABBA")),
 4: dict(zip(range(1, 11), "DBBABAAACD")),
 5: dict(zip(range(1, 11), "CBABCABADA")),
 6: dict(zip(range(1, 11), "BCADCCBDCD")),
}

# ─────────── lo que el libro trae y hay que saber antes de entrar (tablero/hallazgos.csv,
# filas de Física, y tablero/propuestas/fisN_hallazgos.csv) ───────────
# Rótulo: «preg. N», «preg. N y M», «preg. N a M» (lo lee el motor de las guías), «ICFES k» para
# el entrenamiento, o un rótulo general. Severidad: alta · media · baja · atención.
AVISOS = {
 1: [("preg. 6", "media",
      "Dos opciones defendibles: apoyar los dos pies (B) agranda la base de apoyo; flexionar más la "
      "rodilla (C) alarga el choque y baja la fuerza. La pregunta no dice qué cuenta como equilibrio.",
      "Clave tomada: B. Si alguien defiende la C con el impulso, tiene un argumento: reconócelo."),
     ("preg. 3", "media",
      "El diagrama del libro dibuja la normal vertical y las dos componentes del peso hacia abajo: la "
      "normal es perpendicular a la rampa y la parte del peso que lo hace bajar va a lo largo de ella.",
      "No cambia la clave B. Que dibujen su diagrama antes de mirar el del libro."),
     ("preg. 8", "media",
      "La figura pone la prenda en el centro del tambor y la flecha centrípeta hacia el borde: la "
      "fuerza centrípeta apunta al centro, y la prenda va pegada a la pared.",
      "No cambia la clave A. Corrige la flecha en el tablero."),
     ("preg. 5", "atención",
      "Pregunta por el «equilibrio en el aire», pero lo que explica la clave C es la conservación del "
      "momento angular (L = I · ω).",
      "Usa el sello: abrir las piernas sube I y baja ω; el giro total no cambia."),
     ("preg. 1", "baja",
      "La gráfica no dice qué bloque baja por el plano más inclinado, y las dos rectas arrancan un poco "
      "por debajo de cero.",
      "Se responde comparando pendientes. No cambia la clave A."),
     ("preg. 9 y 10", "baja",
      "En la 9 la figura no marca cuál es el bloque A (es el de 5 kg); en la 10 el eje de la gráfica C "
      "dice 1,5 donde va 0,5.",
      "Dilo antes del bloque. No cambian las claves D y B."),
     ("reparto de claves", "atención",
      "A 3 · B 4 · C 2 · D 1: la D sale una sola vez.",
      "Reportado a la editorial. No lo digas en clase.")],
 2: [("preg. 10", "alta",
      "Dos opciones correctas: la A, 500·(25 − 30) ÷ (200·(30 − 80)), y la D, 500·(30 − 25) ÷ "
      "(200·(80 − 30)), dan el mismo 0,25 cal/(g·°C): los dos signos menos se cancelan.",
      "Clave tomada: D. Quien marque A con la cuenta bien hecha también tiene razón: dilo."),
     ("preg. 4", "media",
      "El texto dice que se baja la presión de la olla para cocinar más rápido: es al revés. Con menos "
      "presión el agua hierve a menos temperatura y cocina más despacio.",
      "No cambia la clave B. Corrígelo en voz alta: la olla a presión cocina rápido por la presión alta."),
     ("preg. 5", "media",
      "La gráfica se aplana cerca de −273 °C como si costara cada vez más energía bajar un grado; la "
      "física dice otra cosa, y un gas real se vuelve líquido mucho antes.",
      "Se responde leyendo la forma de la curva (C). No entres en la física de fondo: va al especialista."),
     ("preg. 7", "baja",
      "La clave C supone que los dos bloques pierden calor al mismo ritmo; con la misma masa, el de "
      "aluminio es más grande y tiene más superficie.",
      "La C se sostiene con Q = m · c · ΔT. Nombra el supuesto."),
     ("preg. 1", "baja",
      "El libro escribe la ley de Fourier sin el tiempo: es el calor por segundo (Q ÷ t).",
      "El sello del cuaderno ya la trae bien escrita."),
     ("preg. 2 y 3", "atención",
      "El caso se llama «efecto Mpemba», pero lanzar agua hirviendo al aire bajo cero es otro "
      "fenómeno: gotas finas que se evaporan y se congelan.",
      "No cambia las claves B y C. No enseñes ese nombre para este fenómeno."),
     ("preg. 9", "atención",
      "Las masas vienen en kilogramos y el calor específico en cal/(g·°C): hay que pasar a gramos. La "
      "temperatura final es 35 °C.",
      "Que escriban la unidad de cada número antes de multiplicar.")],
 3: [("preg. 1", "media",
      "La clave D dice que la afirmación «es correcta» por el cambio de flujo, pero el estudiante del "
      "caso dijo otra cosa: que el campo empuja directamente a los electrones. La B también es defendible.",
      "Clave tomada: D. Aclara que lo que produce la corriente es que el campo cambie."),
     ("preg. 6", "media",
      "En la figura B las flechas apuntan hacia la línea entre las cargas, como si llegaran a ellas; "
      "con dos cargas positivas tienen que salir.",
      "Ninguna figura es perfecta: la B tiene la forma correcta. Usa el sello del cuaderno."),
     ("preg. 7", "baja",
      "La carga y la fuerza vienen sin unidades: faltan los coulombs y los newtons.",
      "Que las escriban: 2 × 10⁻⁶ C · 400 N/C = 8 × 10⁻⁴ N. No cambia la clave A."),
     ("preg. 4", "atención",
      "La opción A dice que la carga es negativa, pero el texto no da el signo.",
      "Es plausible: la base de las nubes de tormenta suele ser negativa. No cambia la clave."),
     ("preg. 8 y 9", "atención",
      "770 °C es la temperatura de Curie del hierro puro, no la de cualquier acero; y la 9 supone que "
      "las dos agujas se calientan igual.",
      "No cambia las claves."),
     ("reparto de claves", "atención",
      "La B es clave en cinco de diez preguntas (3, 5, 6, 8 y 9).",
      "Reportado a la editorial. No lo digas en clase.")],
 4: [("preg. 3", "alta",
      "En el esquema hay dos rayos con la letra A (uno en el aire y otro en el agua) y el B está en el "
      "aire. La opción con la razón correcta es «Trayectoria B»: la figura contradice la clave.",
      "Clave tomada: B, por la razón. Con el sello, que cada uno le ponga su letra a cada rayo."),
     ("preg. 9", "alta",
      "Ninguna opción da la razón principal: en el caucho la onda va lenta porque es poco rígido. La "
      "absorción (C) achica la onda, no la frena; y el caucho es menos denso que el aluminio.",
      "Clave tomada: C, la única que dice algo cierto del caucho. Dilo de frente, con el sello."),
     ("preg. 4", "media",
      "La A (el metal refleja la señal) y la D (interferencia por las reflexiones adentro) son "
      "defendibles; la explicación principal es la A.",
      "Clave tomada: A. La editorial podría tener la D: si alguien la defiende, escúchalo."),
     ("preg. 6", "media",
      "Los dos vasos están casi a la misma distancia del dinosaurio: la diferencia se explica mejor por "
      "el vaso y el agua. La clave A concluye más de lo que se observa.",
      "Clave tomada: A. Úsala para discutir justo la estrategia: concluye solo lo observado."),
     ("preg. 7", "atención",
      "La B y la C también son variables que hay que controlar; la A es la que más pesa sobre lo que se mide.",
      "Buena ocasión para hablar de variables de control."),
     ("preg. 8", "atención",
      "Se responde mejor con los radios que da después la pregunta 10 (12, 8 y 3 cm).",
      "El sello del cuaderno trae la idea: más rígido, más rápido."),
     ("página 236", "media",
      "El repaso del libro dice que en el caucho la onda llega tarde «por su absorción»: la causa es la "
      "poca rigidez.",
      "Si alguien lo cita, corrígelo con el sello de la pregunta 8.")],
 5: [("preg. 8", "media",
      "Dos valoraciones señalan algo que de verdad no se probó: la A (solo se usó agua) y la D (solo "
      "vasos del mismo tamaño).",
      "Clave tomada: A, porque ataca «cualquier líquido». Quien marque D tiene un argumento."),
     ("preg. 1", "baja",
      "Dice que el astronauta «pesa 80 kg»: el kilogramo mide masa; el peso se mide en newtons. El dato "
      "no se usa.",
      "No cambia la clave C. Dilo: el peso es una fuerza."),
     ("preg. 3", "atención",
      "El enunciado ya trae la causa y la clave la repite; además, en el GPS real la velocidad del "
      "satélite atrasa su reloj, al revés de lo que dice la C.",
      "Usa el sello sobre la relatividad general. No entres en la otra relatividad."),
     ("preg. 4", "baja",
      "Las rapideces son promedios en los trayectos horizontales, no la rapidez en el momento de la entrega.",
      "No cambia la clave B: solo con la energía potencial la diferencia ya pasa de 1000 J."),
     ("preg. 9 y 10", "atención",
      "La 9 pide un «modelo» y la clave D nombra fuerzas. En la 10, dentro del pitillo lleno no hay "
      "«resistencia del aire»: frena la fricción del agua con las paredes.",
      "No cambian las claves D y A."),
     ("texto del sifón", "baja",
      "Dice que el sifón funciona si la salida está más baja que el nivel inicial; es el nivel que "
      "tenga el agua de arriba en cada momento.",
      "No afecta ninguna clave."),
     ("reparto de claves", "atención",
      "La D sale una sola vez (pregunta 9).",
      "Reportado a la editorial. No lo digas en clase.")],
 6: [("preg. 1", "media",
      "La B refuta la afirmación con los datos (71 a 73 %); la D también se defiende si «eficiencia» se "
      "lee como electricidad que se vuelve calefacción (54 %).",
      "Clave tomada: B. Si alguien marca D con la cuenta, tiene un argumento."),
     ("preg. 4", "media",
      "La B y la D dicen que los datos no permiten afirmar eficiencia total, y las dos son ciertas; la D "
      "agrega que una hora no basta para generalizar.",
      "Clave tomada: D, la que responde el contexto completo."),
     ("preg. 10", "baja",
      "La D se apoya en que faltan 3 kJ sin medir (45 + 6 = 51 de 54 kJ). La B es en parte defendible, y "
      "la batería guarda energía química, no «eléctrica».",
      "Clave tomada: D. Corrige la palabra de la batería."),
     ("preg. 6", "atención",
      "El montaje tiene cinco velas y la pregunta usa cuatro: es fácil multiplicar por cinco (125 kJ, "
      "que no es opción).",
      "Que subrayen el «cuatro» antes de multiplicar."),
     ("preg. 9", "atención",
      "Es un circuito eléctrico dentro de una misión de termodinámica.",
      "Se trabaja con la estrategia de las cuentas con unidades."),
     ("actividad de aula", "atención",
      "La prueba de campo empieza con las opciones C y D de la actividad de aula; la A y la B no vienen.",
      "No afecta las preguntas."),
     ("reparto de claves", "atención",
      "La A sale una sola vez (pregunta 3).",
      "Reportado a la editorial. No lo digas en clase.")],
}

# ─────────── los doce sellos «Alto · aquí entra el profe» del cuaderno ───────────
# Leídos de alto_profe() en fis1.py … fis6.py; la página es la hoja de taller de esa pregunta
# (comprobada en el PDF entregado). Ninguno está en el entrenamiento.
_S = [
 (1, 5, "Momento angular: L = I · ω. Si nada externo lo hace girar, el giro total se conserva."),
 (1, 8, "Fuerza centrípeta: F = m · v² ÷ r, y siempre apunta hacia el centro del giro."),
 (1, 9, "El peso en una rampa: P · sen θ a lo largo del plano y P · cos θ contra el plano."),
 (2, 1, "Ley de Fourier: el calor que cruza una pared cada segundo baja si la pared es más gruesa."),
 (3, 6, "Cómo se revisa un dibujo de campo eléctrico y qué hacer si la figura del libro trae un error."),
 (4, 2, "Por qué una onda va más despacio en una cuerda gruesa que en una delgada."),
 (4, 3, "El esquema del libro tiene dos rayos con la letra A: cómo leer las opciones."),
 (4, 8, "Por qué una onda va más rápido en un material rígido que en uno blando."),
 (4, 9, "Ninguna opción habla de la rigidez: cuál marcar cuando la razón física no está."),
 (5, 3, "Relatividad general: cerca de una masa grande el tiempo pasa un poco más despacio."),
 (5, 9, "Presión atmosférica: el aire empuja sobre la superficie del agua de cada vaso."),
 (6, 10, "Potencia: 1 W es 1 J cada segundo; energía = potencia × tiempo en segundos."),
]


def _pag_taller(m, n):
    b = BASE[m]
    return [b, b + 1, b + 3, b + 4, b + 5][(n - 1) // 2]


SELLOS = [(AREA_CSV, m, _pag_taller(m, n), n, saber, "tarjeta de la pregunta", "En el cuaderno")
          for m, n, saber in _S]
TEXTOS = []        # los textos completos van en la guía (TEXTOS_FIS.md)

# Lo que el profe tiene que poder explicar en cada sello: título, qué es (sin jerga) y la pregunta
# que destraba. Mismo formato que SABERES de plan_bio.py.
SABERES = {
 (1, 5): ("Momento angular",
          "Mide cuánto «giro» lleva un cuerpo: L = I · ω. I depende de qué tan lejos del eje está la "
          "masa (brazos o piernas abiertas, I grande) y ω de qué tan rápido gira. En el aire nada de "
          "afuera lo cambia: si el bailarín abre las piernas, I sube y gira más despacio.",
          "¿Cambió el giro total, o solo cómo está repartida la masa?"),
 (1, 8): ("Fuerza centrípeta",
          "La fuerza que mantiene algo dando vueltas apunta siempre hacia el centro: F = m · v² ÷ r. "
          "Crece con la masa, mucho con la rapidez (al cuadrado) y baja con el radio. En la lavadora la "
          "pared del tambor empuja la ropa hacia el centro; el agua sale por los huecos.",
          "Si duplico la rapidez, ¿cuántas veces más fuerza hace falta? (cuatro)"),
 (1, 9): ("El peso en una rampa",
          "En una rampa el peso se parte en dos flechas: una a lo largo del plano (P · sen θ), que hace "
          "bajar el bloque, y otra contra el plano (P · cos θ), que la normal equilibra. Con 30°, "
          "sen 30° = 0,5: la mitad del peso empuja rampa abajo.",
          "¿Cuál de las dos flechas va en la dirección en que se mueve el bloque?"),
 (2, 1): ("Ley de Fourier",
          "El calor que cruza una pared cada segundo es Q ÷ t = k · A · (T₁ − T₂) ÷ d: crece con el área "
          "y con la diferencia de temperatura, y baja con el grosor d, que está dividiendo. Doble grosor, "
          "la mitad del calor por segundo.",
          "¿El grosor está multiplicando o dividiendo?"),
 (3, 6): ("Las reglas de un dibujo de campo",
          "Las líneas salen de las cargas positivas y llegan a las negativas, nunca se cruzan, y entre "
          "dos cargas iguales se apartan: nunca van de una a la otra. En la figura B del libro la forma "
          "es la correcta, pero las flechas apuntan al revés. Es la mejor de las cuatro.",
          "¿De dónde salen y hacia dónde van las flechas?"),
 (4, 2): ("Rapidez de una onda en una cuerda",
          "La onda va más rápido si la cuerda está más tensa y más despacio si pesa más por cada metro. "
          "La frecuencia la pone la mano y no cambia al pasar a la parte gruesa; como allá va más "
          "lenta, la longitud de onda se acorta: λ = v ÷ f.",
          "¿Quién pone el ritmo: la mano o la cuerda?"),
 (4, 3): ("Refracción, y un esquema con dos letras A",
          "La luz que entra al agua va más lenta y se dobla acercándose a la normal (la línea "
          "perpendicular a la superficie). En el esquema del libro dos rayos llevan la letra A y el B "
          "está en el aire: la opción con la razón correcta es la B. Que cada uno marque sus rayos.",
          "¿Este rayo se quedó en el aire o entró al agua?"),
 (4, 8): ("Rigidez y rapidez",
          "Un material rígido recupera su forma enseguida y por eso pasa la perturbación rápido: en el "
          "aluminio una onda va mucho más rápido que en el caucho, que es blando. No es por el peso: el "
          "caucho es menos denso que el aluminio.",
          "¿Este material vuelve rápido a su forma o se queda deformado?"),
 (4, 9): ("Cuando la razón física no está en las opciones",
          "La rapidez depende de la rigidez y de la densidad. La absorción hace que la onda pierda "
          "tamaño y no llegue lejos, pero no la hace más lenta. La C es la única opción que dice algo "
          "cierto del caucho: se marca, y se dice en voz alta que no es la razón principal.",
          "¿Eso explica que vaya más lento, o que llegue más pequeña?"),
 (5, 3): ("Relatividad general",
          "La gravedad cambia el ritmo del tiempo: en la superficie de la Tierra un reloj va un poquito "
          "más despacio que en un satélite, donde la gravedad es más débil. Son millonésimas de segundo "
          "al día, pero el GPS mide distancias con la rapidez de la luz: sin corregir, se equivocaría "
          "kilómetros en un día.",
          "¿Dónde es más fuerte la gravedad: en el suelo o en la órbita?"),
 (5, 9): ("Presión atmosférica",
          "El aire pesa y empuja sobre todo lo que toca: unos 10 N por centímetro cuadrado al nivel del "
          "mar (en Bogotá, unos 7,5). Un pitillo lleno y tapado arriba con el dedo no se vacía porque el "
          "aire empuja el agua desde abajo. En el sifón, ese empuje sube el agua por el tramo corto.",
          "¿Quién empuja el agua hacia arriba, si nadie la chupa?"),
 (6, 10): ("Potencia",
          "Un vatio es un julio cada segundo (1 W = 1 J/s). La energía es la potencia por el tiempo en "
          "segundos: un bombillo de 10 W durante una noche de 8 horas gasta 10 × 8 × 3600 = 288 000 J, "
          "unos 288 kJ.",
          "¿El tiempo de tu cuenta está en segundos?"),
}

# ─────────── «Si Física no es tu fuerte»: cuatro conceptos por clase ───────────
NO_ES_TU_FUERTE = {
 1: [("Fuerza y diagrama de cuerpo libre",
      "Una fuerza es un empujón o un jalón que alguien le hace a algo. Se dibuja como flecha desde el "
      "objeto, con nombre: peso (la Tierra, hacia abajo), normal (la superficie, perpendicular a ella), "
      "rozamiento (la superficie, contra el deslizamiento) y tensión (la cuerda, a lo largo de ella)."),
     ("Inercia",
      "Si sobre un cuerpo no hay fuerza neta, sigue como iba: quieto, o en línea recta con la misma "
      "rapidez. Por eso, si la tabla se retira de golpe, el tomate no se va con ella: solo cae."),
     ("Gráfica de rapidez contra tiempo",
      "La altura de la línea es la rapidez y su inclinación es la aceleración. Recta que sube: acelera "
      "parejo; horizontal: rapidez constante; que baja: frena. Más inclinada, más aceleración."),
     ("Trabajo y energía",
      "Una fuerza trabaja solo con la parte que va a lo largo del movimiento: W = F · d · cos θ. Si es "
      "perpendicular al camino, no trabaja. La energía que «se pierde» con el rozamiento se vuelve "
      "calor: no desaparece.")],
 2: [("Calor y temperatura",
      "La temperatura mide qué tan agitadas están las partículas; el calor es la energía que pasa de lo "
      "más caliente a lo más frío. Solo, el calor nunca va del frío al caliente."),
     ("Conducción, convección y radiación",
      "Conducción: el calor pasa de partícula en partícula por un sólido (la pared, la cuchara). "
      "Convección: el aire o el agua caliente, menos densos, suben y se llevan el calor. Radiación: "
      "viaja sin medio, como el calor del sol."),
     ("Q = m · c · ΔT",
      "El calor que gana o pierde algo es su masa por su calor específico por el cambio de temperatura. "
      "El agua tiene c = 1 cal/(g·°C): un gramo sube un grado con una caloría. Doble masa con el mismo "
      "calor: la mitad de grados."),
     ("Ebullición y presión",
      "El agua hierve cuando la presión de su vapor iguala la presión de afuera. Con menos presión, como "
      "en una montaña, hierve a menos de 100 °C; en la olla a presión, a más, y por eso cocina rápido.")],
 3: [("Carga eléctrica",
      "Hay positiva y negativa: iguales se repelen, distintas se atraen. En un metal se mueven los "
      "electrones, que son negativos; los protones se quedan en los núcleos."),
     ("Campo eléctrico y sus líneas",
      "Las líneas salen de las cargas positivas y llegan a las negativas, nunca se cruzan y se aprietan "
      "donde el campo es más fuerte. Una carga positiva se empuja a favor de la línea; una negativa, en "
      "contra."),
     ("F = q · E y las unidades",
      "La fuerza sobre una carga es la carga (en coulombs, C) por el campo (en newtons por coulomb, N/C) "
      "y da newtons. 1 μC = 0,000001 C. Para pasar de km/h a m/s se divide por 3,6."),
     ("Inducción y temperatura de Curie",
      "Un imán quieto dentro de una bobina no produce corriente: aparece solo mientras el campo cambia, "
      "cuando el imán entra o sale. Y un imán calentado por encima de su temperatura de Curie deja de "
      "ser imán: sus dominios se desordenan.")],
 4: [("Frecuencia, longitud de onda y rapidez",
      "Frecuencia: cuántas ondas pasan por segundo; la pone la fuente. Rapidez: qué tan rápido avanza; "
      "la pone el medio. Longitud de onda: la distancia entre dos crestas, λ = v ÷ f."),
     ("Refracción",
      "Cuando la luz pasa a un medio donde va más lenta, como del aire al agua, se dobla acercándose a "
      "la normal. El ojo cree que la luz llegó en línea recta: por eso las cosas se ven donde no están."),
     ("Interferencia",
      "Dos ondas que se encuentran se suman. Cresta con cresta: más fuerte (constructiva). Cresta con "
      "valle: se anulan (destructiva). Por eso frente a dos parlantes hay puntos de sonido fuerte y "
      "otros donde casi no se oye."),
     ("Decibeles",
      "Es una escala de veces, no de sumas: 10 dB más es 10 veces más potencia; 20 dB, 100 veces; "
      "30 dB, 1000 veces. Por eso 33 dB de diferencia son unas 2000 veces.")],
 5: [("Energía potencial y cinética",
      "Ep = m · g · h, con la masa en kg, g ≈ 10 m/s² en la Tierra y la altura en m: da julios (J). "
      "Ec = ½ · m · v²: con el doble de rapidez, cuatro veces la energía. La mecánica es la suma de las dos."),
     ("Trabajo",
      "W = F · d · cos θ. Sostener algo quieto cansa, pero no hace trabajo sobre el objeto: no hay "
      "desplazamiento. Una fuerza trabaja si empuja, al menos en parte, en la dirección del movimiento."),
     ("Momento y fuerza",
      "El momento es p = m · v, en kg·m/s. El cambio del momento en un choque es la fuerza por el "
      "tiempo que dura el empujón: si los choques duran lo mismo, cambia más el momento donde la fuerza "
      "fue mayor."),
     ("Presión atmosférica y sifón",
      "El aire empuja sobre todo lo que toca, unos 10 N por cm² al nivel del mar. En el sifón, ese "
      "empuje sube el agua por el tramo corto y el peso de la columna larga la hace bajar.")],
 6: [("Eficiencia",
      "Fracción de la energía que entra que sale como útil: útil ÷ entrada. No tiene unidades y nunca "
      "llega a 1 (100 %): siempre algo se va como calor o ruido."),
     ("Potencia",
      "Energía por segundo: 1 W = 1 J/s. Energía = potencia × tiempo, con el tiempo en segundos: 15 W "
      "durante una hora son 15 × 3600 = 54 000 J."),
     ("Corriente en un circuito",
      "La corriente es la carga que pasa por segundo, en amperios (A). En un cruce se reparte, y lo que "
      "entra es lo que sale. Dos resistencias iguales en paralelo se reparten la corriente por mitades."),
     ("Equilibrio térmico y cambios de fase",
      "El calor pasa del caliente al frío hasta que las temperaturas se igualan; ahí deja de cambiar. "
      "Mientras una sustancia se funde o hierve, recibe calor y su temperatura no sube: son los tramos "
      "planos de una curva de calentamiento.")],
}

PREGUNTA_AREA = "¿Qué lo causó? Muéstrame la flecha o el julio que lo explica."
PROBLEMATIZADORA = {
 1: "¿Qué fuerza —con su nombre y su dirección— explica ese movimiento?",
 2: "¿De dónde a dónde va el calor, y cuánto hace falta para ese cambio?",
 3: "¿Qué carga se movió, hacia dónde, y qué dato lo prueba?",
 4: "¿Qué pone la fuente, qué pone el medio y qué se puede concluir de lo que se ve?",
 5: "¿Cuántos julios hay, quién los puso y a dónde se fueron?",
 6: "Si la energía no desaparece, ¿en qué se convirtió la que falta?",
}

# Una observación corta y ORIGINAL para la activación: dos o tres renglones, sin nombres propios,
# con algo que cambió y una causa que hay que encontrar. La pista es para el final del momento.
ACTIVACION = {
 1: ("Un bus frena de golpe y los pasajeros que iban de pie se van hacia adelante, aunque nadie los "
     "empujó.",
     "cambió la rapidez del bus, no la de ellos: siguieron como iban (inercia). La flecha que los "
     "frena es la del piso en los zapatos o la de la mano en el tubo"),
 2: ("Al soplar sobre una cucharada de sopa caliente, se enfría más rápido que si se deja quieta.",
     "el calor va de la sopa al aire más frío; el soplo se lleva el aire caliente y húmedo de encima, "
     "y las partículas más rápidas se evaporan y se llevan su energía"),
 3: ("Al quitarse un saco de lana en un cuarto oscuro se ven chispitas y se oye un chasquido.",
     "al frotar, unos electrones pasaron de un material al otro; las cargas separadas se juntan de "
     "golpe a través del aire: eso es la chispa"),
 4: ("En el estadio, cuando el público hace «la ola», nadie avanza por la tribuna: cada uno se para y "
     "se sienta en su puesto, y aun así la ola le da la vuelta a la cancha.",
     "lo que viaja es la perturbación, no las personas; el ritmo lo pone quien se para primero, y qué "
     "tan rápido avanza depende de qué tan rápido reacciona la tribuna"),
 5: ("Para subir una loma en bicicleta hay que pedalear duro y uno suda; para bajarla, sin pedalear, "
     "la bicicleta acelera sola.",
     "subiendo, la energía de la comida se vuelve altura (y calor del cuerpo); bajando, la altura se "
     "vuelve rapidez. Ningún julio aparece ni desaparece"),
 6: ("Un carrito de cuerda arranca rápido, va cada vez más despacio y se detiene, aunque la mesa es lisa.",
     "la energía guardada en el resorte se volvió movimiento y, por el roce, calor; cuando se acaba lo "
     "guardado, se detiene"),
}

# Las preguntas de entrenamiento que salen del compilado ASED (columna fuente de icfes.csv).
ASED_NOTA = "Fuente: compilado ASED (no es del ICFES)"


# ─────────────────────── lo que ya está registrado ───────────────────────
def _instrumentos():
    """Las filas de Física de tablero/instrumentos.csv. La pregunta del entrenamiento viene como
    «A»…«D» (misiones 1 y 2), «1»…«4» (3 y 4) o «QA»…«QD» (5 y 6): se normaliza a 1…4."""
    from extrae_instrumentos import filas
    taller, icfes = {}, {}
    for a, mis, p, est, ins, ctx in filas():
        if a != AREA_CSV:
            continue
        es_icfes = "ICFES" in str(mis)
        k = int(str(mis).split()[0])
        q = p[-1] if p.startswith("Q") else p
        n = "ABCD".index(q) + 1 if q in ("A", "B", "C", "D") else int(q)
        (icfes if es_icfes else taller).setdefault(k, []).append((n, est, ins, ctx))
    for d in (taller, icfes):
        for k in d:
            d[k].sort()
    return taller, icfes


_META = re.compile(r"^(se omiten|figura|las cuatro|contexto|mismo contexto|tabla redibujada|"
                   r"rampa redibujada|circuito redibujado)", re.I)


def _banco():
    """Las filas «FIS Mn» de icfes.csv, en el orden del cuaderno (P1…P4 = QA…QD). El contexto se
    queda con lo que dice la pregunta: las notas de formato («figura redibujada…») no van."""
    with open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig") as f:
        r = list(csv.DictReader(f))
    out = {}
    for x in r:
        m = x["mision"].strip()
        if not m.startswith("FIS M"):
            continue
        x = dict(x)
        ctx = re.sub(r"\s*\((?:[^)]*redibujad[^)]*|condensador)\)", "", x["contexto"])
        partes = [p for p in ctx.split(" · ") if not _META.match(p.strip())]
        x["contexto"] = " · ".join(partes[:2]).strip()
        out.setdefault(int(m.replace("FIS M", "")), []).append(x)
    return out


def _comp_icfes():
    """La competencia de cada pregunta de entrenamiento: campo comp de QA…QD en fisN_icfes.py,
    leído con ast (sin importar el módulo, que reconfigura el motor del cuaderno)."""
    out = {}
    for m in range(1, 7):
        src = open(f"/home/claude/libro/fis{m}_icfes.py", encoding="utf-8").read()
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
ASED = {(m, k + 1) for m, filas_ in BANCO.items() for k, x in enumerate(filas_) if "ASED" in x["fuente"]}


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
    """Lo que tiene que cuadrar antes de dibujar: claves del libro contra el docstring de fisN.py,
    claves del entrenamiento contra el docstring de fisN_icfes.py, la estrategia de cada pregunta
    contra las cuatro de la misión, y que la pregunta de entrenamiento k entrene la estrategia k.
    Devuelve la lista de diferencias."""
    malas = []
    for m in range(1, 7):
        doc = open(f"/home/claude/libro/fis{m}.py", encoding="utf-8").read()
        a = doc.index('"""') + 3
        doc = doc[a:doc.index('"""', a)]
        k = {int(n): c for n, c in re.findall(r"\b(\d+)·([A-D])\b", doc)}
        if k != CLAVES[m]:
            malas.append(f"M{m}: CLAVES {CLAVES[m]} · fis{m}.py {k}")
        doc = open(f"/home/claude/libro/fis{m}_icfes.py", encoding="utf-8").read()[:4000]
        ki = dict(re.findall(r"Q([A-D])\s*·[^·\n]*·\s*([A-D])\b", doc))
        for j, q in enumerate("ABCD"):
            if ki.get(q) != BANCO[m][j]["clave"].strip():
                malas.append(f"M{m} P{j+1}: icfes.csv {BANCO[m][j]['clave']} · fis{m}_icfes.py {ki.get(q)}")
        for p, e, _, _ in TALLER[m] + INS_ICFES[m]:
            if e not in MISIONES[m]["estr"]:
                malas.append(f"M{m} · {p}: estrategia «{e}» no está en la misión")
        for p, e, _, _ in INS_ICFES[m]:
            if MISIONES[m]["estr"].index(e) != p - 1:
                malas.append(f"M{m} · ICFES {p}: entrena «{e}», no la estrategia {p}")
        if len(TALLER[m]) != 10 or len(INS_ICFES[m]) != 4 or len(BANCO[m]) != 4:
            malas.append(f"M{m}: {len(TALLER[m])} del taller, {len(INS_ICFES[m])} y {len(BANCO[m])} ICFES")
    if ASED != {(1, 1), (2, 1)}:
        malas.append(f"ASED: se esperaban M1 P1 y M2 P1 y el tablero dice {sorted(ASED)}")
    return malas


# ─────────────────────────── banco de dinámicas ───────────────────────────
# Isomorfas a la estrategia: lo que hace el cuerpo es el mismo movimiento que después hará la mente
# frente al dibujo o la cuenta. En Física el movimiento casi siempre es NOMBRAR LA FLECHA (quién
# empuja y hacia dónde), LLEVAR LA CUENTA (de la energía, del calor, de las unidades) o SEPARAR
# (lo que pone la fuente y lo que pone el medio, lo que se cambió y lo que se dejó quieto). La E1
# abre la clase (8'); las otras tres van entre bloques del desarrollo guiado (6'). Ninguna usa el
# caso de una pregunta que viene después: se entrena el movimiento, no la respuesta.
# Seguridad: nada de electricidad real ni de lanzar objetos; se camina, nunca se corre.
DINAMICAS = {
 1: [("Las flechas de la mochila", 8,
      ["Una mochila liviana en el pupitre del frente, con tres cordones amarrados; tres estudiantes "
       "toman uno cada uno, sin halar.",
       "El grupo nombra en voz alta todas las fuerzas sobre la mochila: quién la hace y hacia dónde.",
       "El docente dice cómo van a halar («dos a la derecha, uno a la izquierda») y el grupo predice "
       "si se mueve y hacia dónde.",
       "Halan suave. Si la predicción falla, buscan la flecha olvidada: casi siempre, el rozamiento."],
      "Nombrar cada fuerza —quién la hace y hacia dónde apunta— antes de decir qué pasa con el "
      "movimiento. Es el movimiento de las preguntas 3, 6, 7 y 9, y de la primera del entrenamiento "
      "(la fuerza que sostiene los paquetes).",
      "Una mochila liviana · tres cordones de un metro"),
     ("Camina la gráfica", 6,
      ["El docente dibuja una gráfica de rapidez contra tiempo: parte de cero, sube, se queda plana y "
       "vuelve a subir, más inclinada.",
       "Un voluntario la camina por el pasillo mientras otro cuenta segundos: si sube, va cada vez más "
       "rápido; si es plana, mantiene el paso. Sin correr.",
       "El grupo lo corrige en el momento: «¡ahí estaba plana, no aceleres!».",
       "Al revés: otro camina una historia que el docente le dice al oído y el grupo la dibuja."],
      "Leer cada tramo de una gráfica como un pedazo de movimiento —sube, plano o baja— y traducir en "
      "las dos direcciones. Es el movimiento de las preguntas 1 y 10, y de la segunda del "
      "entrenamiento (la gráfica de la energía del vagón).",
      "Tablero · pasillo despejado"),
     ("Una sola perilla", 6,
      ["Un borrador amarrado a un cordón es un péndulo: un estudiante cuenta cuánto tarda en hacer "
       "diez idas y vueltas.",
       "«¿De qué depende ese tiempo?». Las ideas van al tablero: el largo, el peso, qué tan lejos se "
       "suelta.",
       "Cada equipo escoge una y llena: LO QUE CAMBIO, LO QUE DEJO QUIETO, LO QUE MIDO.",
       "Dos equipos prueban al frente. Si uno cambió dos cosas, el grupo dice por qué no se sabe cuál fue."],
      "Separar lo que se cambia de lo que se deja quieto, y aceptar que un experimento solo responde "
      "por la variable que movió. Es el movimiento de las preguntas 4 y 8, y de la tercera del "
      "entrenamiento (qué pregunta se puede contestar con lo observado).",
      "Un borrador · un cordón de un metro · un reloj"),
     ("Los tres bolsillos de la energía", 6,
      ["Tres estudiantes son tres bolsillos: ALTURA, MOVIMIENTO y CALOR. El de ALTURA tiene diez fichas.",
       "El docente narra despacio: «un carrito está arriba de una rampa… baja… rueda… frena hasta "
       "quedarse quieto».",
       "En cada frase el grupo dice cuántas fichas pasan y de qué bolsillo a cuál; se las pasan de mano "
       "en mano.",
       "Al final se cuentan: tienen que ser diez. Ninguna desaparece ni aparece de la nada."],
      "Seguir lo que se conserva: lo que sale de una forma aparece en otra y el total no cambia. Es el "
      "movimiento de las preguntas 2 y 5 —en la 5 lo que se conserva es el giro— y de la cuarta del "
      "entrenamiento (el salto bungee).",
      "Diez fichas de papel · tres letreros")],
 2: [("La fila del calor", 8,
      ["Ocho estudiantes en fila son las partículas de una varilla. Los dos de un extremo están "
       "«calientes»: se frotan las manos rápido.",
       "Solo se le pasa agitación al vecino más quieto, tocándole el hombro: él se frota más rápido y "
       "el que la dio, más despacio.",
       "El grupo mira hacia dónde viaja la agitación y cuándo se detiene: cuando todos se frotan igual.",
       "«¿Puedes pasarle agitación al que está más caliente que tú?». El grupo dice por qué no."],
      "Ubicar quién está más caliente y quién más frío antes de decir hacia dónde va el calor, y ver "
      "que el paso se detiene cuando las temperaturas se igualan. Es el movimiento de las preguntas 1, "
      "6 y 8, y de la primera del entrenamiento (el aire caliente del globo).",
      "Ninguno"),
     ("El mismo calor para más agua", 6,
      ["Dos equipos: uno de dos estudiantes y otro de cuatro. Cada uno es una porción igual de agua y "
       "empieza agachado: 20 grados.",
       "Cada equipo recibe ocho fichas de calor; cada ficha sube un grado a quien la recibe, y por cada "
       "grado se estira un poco.",
       "Reparten por igual y el grupo compara: ¿qué equipo subió más grados por persona?",
       "Segunda ronda: un equipo es de un material «terco», de dos fichas por grado. El grupo predice "
       "antes de repartir."],
      "Llevar la cuenta del calor: el mismo calor en más masa sube menos la temperatura, y un calor "
      "específico mayor pide más calor por grado (Q = m · c · ΔT). Es el movimiento de las preguntas "
      "7, 9 y 10, y de la segunda del entrenamiento (dos litros en la misma estufa).",
      "Dieciséis fichas de papel"),
     ("El baile de las moléculas", 6,
      ["Doce estudiantes forman cuatro moléculas de agua: tríos de la mano, el oxígeno en el medio. "
       "Pupitres a un lado.",
       "Palmas lentas: se mueven despacio y juntas. Palmas rápidas: más rápido y repartidas por el "
       "salón. Caminando, nunca corriendo.",
       "Regla que nadie rompe: cambian la rapidez y la distancia, pero ningún trío se suelta.",
       "El ritmo baja hasta casi parar: el grupo dice qué cambió y qué no cambió."],
      "Explicar la temperatura y los cambios de fase con lo que hacen las partículas: más rápidas y "
      "más separadas, pero enteras. Es el movimiento de las preguntas 2 y 5, y de la tercera del "
      "entrenamiento (el modelo del agua líquida y en gas).",
      "Cinta para el piso"),
     ("La puerta de la olla", 6,
      ["Cinco estudiantes son el agua de una olla. Junto a una «puerta» de cinta, cuatro más son el "
       "aire de afuera.",
       "Cada palmada es más calor: las moléculas dan un paso hacia la puerta.",
       "Una molécula sale —el agua hierve— cuando sus pasos igualan las personas de la puerta.",
       "La puerta cambia: dos personas (menos aire empujando) o seis (olla tapada). El grupo predice "
       "antes de aplaudir."],
      "Antes de decir a qué temperatura cambia de fase, mirar qué pone el ambiente: con menos presión "
      "afuera hierve antes; con más, después. Es el movimiento de las preguntas 3 y 4, y de la cuarta "
      "del entrenamiento (hervir agua a 25 km de altura).",
      "Cinta · un letrero «puerta»")],
 3: [("El dato que tumba la idea", 8,
      ["Cuatro carteles en las esquinas: VOLTAJE DE LA PILA, LARGO DEL CABLE, COLOR DEL BOMBILLO y "
       "TEMPERATURA DEL BOMBILLO.",
       "El docente lee una idea: «la linterna alumbra menos porque la pila ya se gastó».",
       "Cada estudiante camina al cartel del dato que pondría a prueba ESA idea.",
       "Para quedarse, dice qué valor le daría la razón a la idea y cuál se la quitaría. Si no puede, "
       "cambia de esquina."],
      "Antes de mirar las opciones, leer qué dice exactamente la idea y buscar la medida —en qué lugar "
      "y en qué condición— que la confirma o la tumba. Es el movimiento de las preguntas 2, 5 y 8, y "
      "de la primera del entrenamiento (la resistencia a 90 °C).",
      "Cuatro carteles · sin pilas ni cables de verdad"),
     ("El salón es un campo", 6,
      ["El docente es una carga positiva en un extremo del salón; un estudiante con un cartel «−», "
       "una negativa en el otro.",
       "Seis estudiantes son cargas positivas pequeñas: cada uno apunta con el brazo hacia donde lo "
       "empujan las dos cargas.",
       "El grupo revisa: cerca de la + los brazos se alejan; cerca de la −, apuntan hacia ella.",
       "Con lana unen los brazos en líneas de la + a la −, y comprueban que nunca se cruzan."],
      "Dibujar el campo antes de elegir una figura: de dónde salen las líneas, a dónde llegan y hacia "
      "dónde empujan en cada punto. Es el movimiento de las preguntas 4 y 6, y de la segunda del "
      "entrenamiento (las fuerzas de dos cargas sobre una tercera).",
      "Dos carteles (+ y −) · un ovillo de lana"),
     ("Pasos con signo", 6,
      ["Una cinta en el piso con una flecha es el campo eléctrico: apunta hacia la ventana.",
       "Cada estudiante tiene una tarjeta con una carga: «+2 μC», «−1 μC», «+1 μC», «−3 μC».",
       "Antes de moverse dice su cuenta: «menos tres microcoulombs: tres pasos contra el campo». "
       "Positiva, hacia la ventana; negativa, hacia la puerta.",
       "Segunda ronda: la carga viene en otra unidad («0,000002 C») y hay que pasarla a μC antes."],
      "Llevar el signo, el sentido y la unidad en cada cuenta: una carga negativa se empuja en contra "
      "del campo, y un número sin unidad no se puede usar. Es el movimiento de las preguntas 3 y 7, y "
      "de la tercera del entrenamiento (hacia dónde se mueve la carga −q).",
      "Cinta · tarjetas con cargas"),
     ("Quién se puede mover", 6,
      ["Diez estudiantes son un pelo: cinco sentados son protones y cinco de pie, electrones. Otros "
       "diez son un globo, igual.",
       "El docente «frota» el globo con el pelo: tres electrones caminan del pelo al globo. Los "
       "protones no se levantan.",
       "El grupo cuenta la carga de cada uno: pelo +3, globo −3. Nada se creó ni se destruyó.",
       "«El globo quedó negativo: ¿qué se movió?». Quien diga «protones» muestra cuál se levantó."],
      "Usar el modelo para decir, paso a paso, qué partícula se mueve, hacia dónde y por qué, sin "
      "mover lo que el modelo no deja mover. Es el movimiento de las preguntas 1, 9 y 10, y de la "
      "cuarta del entrenamiento (las dos esferas metálicas que se tocan).",
      "Ninguno")],
 4: [("El ritmo y el piso", 8,
      ["El docente marca un ritmo con palmas: es la fuente. Seis estudiantes salen uno por palmada y "
       "dan un paso largo por palmada.",
       "En una zona marcada con cinta, el medio «lento», dan pasos cortos, pero siempre uno por palmada.",
       "El grupo mira: ¿cambió el ritmo?, ¿la distancia entre compañeros?, ¿qué tan rápido avanza la fila?",
       "Al salir de la zona: ¿qué vuelve a cambiar, qué no cambió nunca y quién lo puso?"],
      "Separar lo que pone la fuente (la frecuencia, que no cambia de un medio a otro) de lo que pone "
      "el medio (la rapidez y, con ella, la longitud de onda). Es el movimiento de las preguntas 2, 3 "
      "y 9, y de la primera del entrenamiento (el detector de sonido fuera del agua).",
      "Cinta · pasillo despejado · sin correr"),
     ("La moneda que sube", 6,
      ["Una cinta en el piso es la superficie del agua. Un estudiante agachado bajo ella tiene una "
       "moneda en el «fondo».",
       "Con un cordón arman el camino de la luz hasta el ojo de otro, de pie: recto en el agua, se "
       "dobla en la cinta alejándose de la normal, recto en el aire.",
       "«Mi ojo no sabe que la luz se dobló»: con otro cordón prolongan hacia atrás el último tramo.",
       "El grupo marca dónde se «ve» la moneda y lo compara con dónde está."],
      "Dibujar los rayos antes de elegir y prolongar en línea recta lo que le llega al ojo. Es el "
      "movimiento de las preguntas 1 y 8, y de la segunda del entrenamiento (cómo ve el nadador el "
      "farol).",
      "Cinta · dos cordones · una moneda"),
     ("Lo que oímos y lo que decimos", 6,
      ["El docente golpea suave, siempre igual, la punta de una fila de pupitres; tres estudiantes con "
       "la oreja en la madera dicen si oyen fuerte, medio o débil.",
       "El docente lee conclusiones: «el sonido se debilita al alejarse», «la madera transmite mejor que el aire».",
       "Cada uno camina a una zona: LO OBSERVAMOS, NO LO OBSERVAMOS o NECESITO OTRA PRUEBA.",
       "Para quedarse, dice qué dato lo respalda o qué cambiaría en la otra prueba."],
      "Concluir solo lo que la observación permite y nombrar qué habría que controlar para decir más. "
      "Es el movimiento de las preguntas 6 y 7, y de la tercera del entrenamiento (los puntos donde se "
      "oye fuerte y donde casi no).",
      "Una fila de pupitres · tres letreros"),
     ("La gráfica humana", 6,
      ["Con cinta, dos ejes en el piso; un equipo escribe los rótulos y las marcas de cada escala.",
       "El docente dicta una tabla: a los 0, 5, 10 y 15 minutos, una taza de agua está a 80, 65, 55 y "
       "50 °C. Cuatro estudiantes se ubican como puntos.",
       "El grupo revisa que cada uno esté en su minuto y en su temperatura.",
       "El docente voltea en secreto una escala o cambia los rótulos de eje: ¿la gráfica cuenta la misma historia?"],
      "Antes de leer la forma, leer qué variable va en cada eje y hacia dónde crece su escala. Es el "
      "movimiento de las preguntas 4, 5 y 10, y de la cuarta del entrenamiento (qué gráfica muestra la "
      "tabla del sonido).",
      "Cinta · hojas para rótulos y marcas")],
 5: [("La fórmula llama a sus datos", 8,
      ["Cada estudiante tiene una tarjeta: «m = 2 kg», «h = 3 m», «v = 4 m/s», «g = 10 m/s²», «t = 5 s»; "
       "tres más tienen Ep = m · g · h, Ec = ½ · m · v² y p = m · v.",
       "Cada fórmula llama al frente solo los datos que necesita; los que sobran se quedan sentados.",
       "La cuenta va con números y unidades a la vez: 2 kg · 10 m/s² · 3 m = 60 J.",
       "Cambia una tarjeta («h = 6 m», «v = 8 m/s»): ¿el resultado se duplica, se cuadruplica o no cambia?"],
      "Escoger la fórmula por la magnitud que se pide, llamar solo los datos que usa y arrastrar la "
      "unidad hasta el final. Es el movimiento de las preguntas 1, 4 y 5, y de la primera del "
      "entrenamiento (cuánto cambió el momento en cada choque).",
      "Tarjetas con datos y fórmulas"),
     ("¿Trabaja o no trabaja?", 6,
      ["Un estudiante con una mochila liviana; cada uno del grupo tiene dos tarjetas: SÍ TRABAJA y NO TRABAJA.",
       "Despacio, el estudiante sube la mochila al pupitre, la sostiene quieta, camina con ella a la "
       "misma altura y la baja.",
       "Antes de cada acción, el grupo dibuja en el aire dos flechas: hacia dónde empuja la mano y hacia "
       "dónde va la mochila.",
       "Levantan la tarjeta: trabaja si las dos flechas van, al menos en parte, en la misma línea."],
      "Nombrar quién empuja y hacia dónde, y compararlo con hacia dónde se mueve el objeto, antes de "
      "hablar de trabajo o de equilibrio. Es el movimiento de las preguntas 6 y 10, y de la segunda "
      "del entrenamiento (las fuerzas sobre la piñata quieta).",
      "Una mochila liviana · dos tarjetas por estudiante"),
     ("Las perillas de la rampa", 6,
      ["Cuatro estudiantes son las perillas de una rampa de cuadernos: ALTURA, CARRITO, SUPERFICIE y LARGO.",
       "Pregunta: «¿la altura cambia qué tan lejos llega el carrito?». Solo esa perilla cambia; las "
       "demás se cruzan de brazos.",
       "Se prueba dos veces con un carrito de juguete o una tapa, cambiando solo la altura.",
       "El docente mueve dos perillas a escondidas: ¿se sabe cuál fue?, ¿vale para cualquier rampa?"],
      "Cambiar una variable a la vez, dejar fijas las demás y no estirar la conclusión más allá de lo "
      "que se probó. Es el movimiento de las preguntas 2 y 8, y de la tercera del entrenamiento (qué "
      "asegurar al repetir la medida de los resortes).",
      "Cuadernos · un carrito de juguete o una tapa"),
     ("El rincón del principio", 6,
      ["Tres rincones: LA ENERGÍA NO DESAPARECE, SI HAY FUERZA NETA HAY ACELERACIÓN y EL AIRE EMPUJA.",
       "El docente muestra un fenómeno: una pelota que rebota cada vez más bajo, un carrito que arranca "
       "con un empujón, una ventosa pegada a la baldosa.",
       "Cada estudiante camina al rincón del principio que lo explica.",
       "Para quedarse, lo dice con las palabras del principio. Si solo describe lo que ve, cambia de rincón."],
      "Explicar un fenómeno nombrando el principio y usándolo, no describiéndolo otra vez. Es el "
      "movimiento de las preguntas 3, 7 y 9, y de la cuarta del entrenamiento (la pelota que sube "
      "acelerada por el tubo).",
      "Tres carteles · una pelota · una ventosa")],
 6: [("Unidades que se tachan", 8,
      ["Cinco tarjetas: «2 ventiladores», «50 W por ventilador», «2 h», «3600 s por hora», «1 kJ por "
       "cada 1000 J».",
       "«¿Cuánta energía gastan en la tarde?». Se ordenan para que cada unidad de abajo se tache con "
       "una de arriba; al tacharse, chocan las manos.",
       "La que queda tiene que ser de energía: 2 × 50 × 2 × 3600 = 720 000 J = 720 kJ.",
       "Segunda ronda: se reparten entre los dos ventiladores. 720 kJ ÷ 2 = 360 kJ cada uno."],
      "Llevar las unidades en la cuenta como si fueran números: se multiplican, se dividen y se "
      "tachan, y la que queda dice si la cuenta tiene sentido. Es el movimiento de las preguntas 3, 6 "
      "y 9, y de la primera del entrenamiento (cómo se reparte la corriente I1).",
      "Cinco tarjetas"),
     ("La tira que se reparte", 6,
      ["Una tira de papel de un metro es la energía que entra a un carrito de juguete con motor. "
       "Cuatro en fila: ELÉCTRICA, MOTOR, RUEDAS, MOVIMIENTO.",
       "En cada paso, quien recibe la tira arranca un pedazo y lo pega bajo CALOR Y RUIDO.",
       "El grupo mide con regla lo que llegó al carrito y lo que quedó en el tablero.",
       "Juntan los pedazos: tienen que sumar un metro. ¿Qué fracción llegó útil?"],
      "Seguir la energía forma por forma y cerrar la cuenta: lo que entra es lo útil más lo que se va "
      "como calor; nada aparece de la nada. Es el movimiento de las preguntas 2 y 7, y de la segunda "
      "del entrenamiento (el bombillo que se prende sin la fuente).",
      "Una tira de papel de un metro · cinta · una regla"),
     ("Hasta dónde llega la conclusión", 6,
      ["Una cinta en el piso con cinco marcas: ESTAS BOTELLAS · ESTE DÍA · CUALQUIER DÍA DE SOL · "
       "CUALQUIER RECIPIENTE · SIEMPRE.",
       "Datos: tres botellas iguales con agua, una hora al sol, subieron de 18 °C a 31, 30 y 32 °C.",
       "El docente lee una conclusión y un voluntario se para en la marca hasta donde ella llega.",
       "El grupo lo devuelve a la última marca que los datos cubren y dice qué faltaría medir."],
      "Medir el tamaño de una conclusión contra el de los datos: cuántos ensayos, en qué condiciones, "
      "con qué. Es el movimiento de las preguntas 1, 4 y 10, y de la tercera del entrenamiento (por qué "
      "no se repitió el rebote en el salón).",
      "Cinta · cinco hojas con las marcas"),
     ("La caja que se llena y se vacía", 6,
      ["En cada palmada, uno saca de una caja una ficha por cada cuatro que haya (las pérdidas) y otro "
       "echa dos (lo que entra).",
       "Un tercero anota en el tablero cuántas quedan: 2, 4, 5, 6, 7, 8, 8, 8…",
       "La cuenta sube cada vez más despacio y se queda en 8: ahí sale lo mismo que entra.",
       "¿Y si entran tres por palmada? El grupo predice antes de probar: 12."],
      "Reconocer el equilibrio como el momento en que lo que entra iguala lo que sale, no como el "
      "momento en que todo se detiene. Es el movimiento de las preguntas 5 y 8 y, con otra razón, de la "
      "cuarta del entrenamiento (los tramos planos de la curva de calentamiento).",
      "Una caja · treinta fichas")],
}

RETOS = {
 1: ("El tobogán del parque", 20,
     "Cada equipo de tres recibe un caso: un niño baja por un tobogán y, al llegar abajo, frena en la "
     "arena hasta quedarse quieto. En doce minutos dibujan las fuerzas sobre el niño en el tobogán, "
     "cada una con su nombre y quién la hace; esbozan la gráfica de su rapidez contra el tiempo, de "
     "arriba hasta que se detiene; diseñan una prueba justa para saber si la ropa (jean o sudadera) "
     "cambia la rapidez al llegar; y escriben a dónde se fue la energía de la altura. Cada integrante "
     "defiende una de las cuatro partes."),
 2: ("El tinto de las seis", 20,
     "Cada equipo recibe un caso: una taza con 200 g de tinto a 80 °C se deja en un salón a 20 °C. En "
     "doce minutos dibujan con flechas por dónde se va el calor (la taza, el aire que sube, el vapor); "
     "calculan cuánto calor suelta el tinto hasta llegar a 30 °C, con c = 1 cal/(g·°C), llevando las "
     "unidades; explican qué les pasa a las partículas mientras se enfría; y dicen hasta qué "
     "temperatura baja y por qué ahí se detiene. Cada uno cierra: «El tinto dejó de enfriarse porque "
     "___, y eso no quiere decir que ___»."),
 3: ("La tormenta y el pararrayos", 20,
     "Cada equipo recibe una idea que circula en el barrio: «el pararrayos atrae los rayos». En doce "
     "minutos escriben qué dato pondría a prueba esa idea; dibujan el campo entre la base de una nube, "
     "con carga negativa, y el suelo; calculan la fuerza sobre una carga de 2 μC en un campo de "
     "10 000 N/C, con su unidad, y dicen hacia dónde va si la carga es negativa; y explican qué "
     "partículas se mueven por el cable del pararrayos hasta la tierra. Cada integrante defiende una "
     "de las cuatro partes."),
 4: ("El parlante de la fiesta", 20,
     "Cada equipo recibe una tabla: un parlante suena a 90 dB a 2 m, a 84 dB a 4 m y, detrás de una "
     "pared, a 4 m, a 64 dB. En doce minutos dicen qué pone el parlante y qué pone la pared (¿cambia "
     "la nota al atravesarla?); dibujan los frentes de onda que salen del parlante y llegan a la "
     "pared; escriben una conclusión que los datos permiten y otra que no («la pared absorbe todo el "
     "sonido»); y calculan cuántas veces más débil se oye detrás de la pared que delante, a la misma "
     "distancia. Cada integrante defiende una de las cuatro partes."),
 5: ("La patineta en la rampa", 20,
     "Cada equipo recibe un caso: una patinadora de 50 kg baja desde el borde de una rampa de 2 m de "
     "altura y llega abajo a 6 m/s. En doce minutos calculan su energía potencial arriba y su energía "
     "cinética abajo, con g = 10 m/s² y con unidades; dibujan las fuerzas sobre ella cuando rueda en "
     "el piso y dicen cuáles hacen trabajo; diseñan una prueba para saber si la masa de quien patina "
     "cambia la rapidez al llegar abajo; y explican con un principio a dónde se fueron los julios "
     "que faltan. Cada integrante defiende una de las cuatro partes."),
 6: ("La ducha eléctrica", 20,
     "Cada equipo recibe un caso: una ducha eléctrica de 3000 W funciona 10 minutos y el agua recibe "
     "1,44 MJ. En doce minutos calculan la energía que entró, con las unidades hasta el final, y la "
     "fracción que llegó al agua; dibujan la cadena de la energía, desde la red hasta el agua, con lo "
     "que se pierde en cada paso; deciden si con esa sola ducha se puede afirmar que «todas las duchas "
     "eléctricas aprovechan el 80 %»; y explican por qué el agua sale a temperatura constante mientras "
     "la ducha está prendida. Cada uno cierra: «La energía que no calentó el agua se fue a ___, y eso "
     "no quiere decir que ___»."),
}
# ─────────────────────────────── hojas ───────────────────────────────
OUTP = OUT + "plan_fis_"


def _cajas_hilo(b, y):
    cajas = [("LIBRO", "tiene la pregunta", GRAY), ("CUADERNO", "tiene el andamiaje para resolverla", FIS),
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
    y = cabecera(b, "Física", "Planeador del área · las ocho clases",
                 derecha="8", dsub="clases de 120 min", campos=True)
    y = seccion(b, y, "Para qué existe este documento")
    y = parrafo_j(b, M, y,
        "La calidad de la clase no puede depender de qué profesor llegue ese sábado. Por eso el "
        "método de EDUCATE no vive en el profesor: vive en el cuaderno del estudiante. Este "
        "planeador no te pide saber física de memoria; te dice qué hacer con el libro y con el "
        "cuaderno en cada uno de los 120 minutos, y dónde termina lo fijo y empieza tu aporte.",
        CW, 26) + 24
    y = _cajas_hilo(b, y) + 30
    y = nota(b, M, y, CW,
        "Casi ninguna pregunta de Física se resuelve recordando una fórmula. Se resuelve preguntando "
        "qué cambió y qué lo causó: cada fuerza se dibuja como una flecha con su nombre y cada julio "
        "tiene que aparecer en la cuenta. Es el instrumento que el estudiante encuentra en la portada "
        "del área, en la página 225. Un estudiante que acierta con el instrumento vacío no aprendió la "
        "estrategia: adivinó, y en la prueba real no va a tener a quién preguntarle.",
        FIS, FIS_BG, FIS_LN, "El instrumento de pensamiento del área: la flecha con su nombre", 25) + 30
    y = seccion(b, y, "El área en números")
    na = sum(len(v) for v in AVISOS.values())
    cif = [("43", "páginas del cuaderno\\ncon la portada", FIS), ("60", "preguntas del libro\\ncon su instrumento", FIS),
           ("24", "preguntas tipo\\nSaber 11", "#1F4E8C"), (str(len(SELLOS)), "sellos «aquí entra\\nel profe»", ORO),
           (str(na), "avisos del libro\\nantes de entrar", ROJO)]
    an2 = (CW - 4 * 18) / 5
    for i, (v, l, c) in enumerate(cif):
        x = M + i * (an2 + 18)
        b.append(rect(x, y, an2, 140, "white", r=16, stroke=FIS_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, 112, c, r=3))
        b.append(T(x + 38, y + 64, [v], 50, c, weight="700"))
        for j, ln in enumerate(l.split("\\n")):
            b.append(T(x + 38, y + 98 + j * 26, [ln], 20, GRAY))
    y += 140 + 30
    y = seccion(b, y, "Las tres competencias que evalúa la prueba de Ciencias Naturales")
    comp = [("UC", "Uso comprensivo del conocimiento científico", "usar conceptos y modelos de la "
             "física —fuerza, energía, calor, carga, onda— para entender una situación"),
            ("EF", "Explicación de fenómenos", "construir la explicación de lo que pasa, eslabón por "
             "causa, y juzgar si una explicación alcanza"),
            ("IN", "Indagación", "plantear preguntas que se puedan poner a prueba, comparar contra un "
             "control y sacar solo la conclusión que los datos permiten")]
    an3 = (CW - 2 * 18) / 3
    alt3 = 52 + max(len(wrap_px(t + ": " + d, 22, an3 - 70)) for _, t, d in comp) * 31 + 20
    for i, (cod, t, d) in enumerate(comp):
        x = M + i * (an3 + 18)
        b.append(rect(x, y, an3, alt3, FIS_BG, r=16, stroke=FIS_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt3 - 28, FIS, r=3))
        b.append(T(x + 40, y + 44, [cod], 26, FIS, weight="700"))
        parrafo_j(b, x + 40, y + 54, t + ": " + d, an3 - 70, 22, INK, lh=31)
    y += alt3 + 30
    y = nota(b, M, y, CW,
        "Dos de las 24 preguntas de entrenamiento (la primera de las misiones 1 y 2) salen del "
        "compilado ASED, no de un cuadernillo del ICFES: no las presentes como «del ICFES». Tres claves "
        "del libro tienen reserva alta (misión 2, pregunta 10; misión 4, preguntas 3 y 9) y siete más, "
        "reserva media: están en la hoja de su clase. Y ninguna dinámica usa electricidad real ni lanza "
        "objetos: se camina, nunca se corre, y las cuerdas se halan suave.",
        ROJO, ROJO_BG, ROJO_LN, "Antes de empezar el área", 23) + 28
    y = nota(b, M, y, CW,
        "No necesitas ser físico. La segunda hoja de cada clase trae los cuatro conceptos que tienes "
        "que poder explicar en dos minutos, y el cuaderno marca con un sello «Alto · aquí entra el "
        "profe» las doce preguntas donde el estudiante no puede seguir sin ti. Lo demás lo resuelve el "
        "instrumento: qué cambió, qué lo causó, y la flecha o la cuenta que lo muestra.",
        VERDE, VERDE_BG, VERDE_LN, "Si Física no es tu fuerte", 23) + 28
    y = seccion(b, y, "Lo que la coordinación revisa, sin haber entrado a la clase",
        "Tres cuadernos al azar del grupo. No se mira si la respuesta está buena: se mira si el "
        "instrumento está lleno. Marca tú mismo esta lista al terminar el sábado.")
    rev = ["El instrumento de pensamiento está lleno en las diez preguntas, acertadas o no.",
           "«Mi primera idea, antes de hacer nada» tiene algo escrito en todas las preguntas.",
           "Los sellos «Alto · aquí entra el profe» tienen escrito «lo que explicó, en mis palabras».",
           "Las dos caritas de la clase están marcadas y la clase está anotada en la portada del área."]
    b.append(rect(M, y, CW, 34 + len(rev) * 50, "white", r=18, stroke=FIS_LN, sw=2))
    b.append(rect(M + 14, y + 16, 5, 2 + len(rev) * 50, FIS, r=3))
    yy = y + 34
    for r_ in rev:
        b.append(checkbox(M + 44, yy - 14, 13, FIS))
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
        ln = FIS_LN if mis else ORO_LN
        c = FIS if mis else ORO
        b.append(rect(M, y, CW, alto, bg, r=14, stroke=ln, sw=2))
        b.append(rect(M + 12, y + 12, 5, alto - 24, c, r=3))
        b.append(T(colx[0] + 44, y + 62, [str(n)], 42, c, weight="700", anchor="middle"))
        b.append(T(colx[1] + 20, y + 44, [tit], 24, INK, weight="700"))
        b.append(T(colx[1] + 20, y + 74, [sub], 20, GRAY, style="italic"))
        if mis:
            d = MISIONES[mis]
            cod, de = d["competencia"].split(" · ")
            b.append(T(colx[2] + 20, y + 44, [cod], 23, FIS, weight="700"))
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
        b.append(rect(x, yy0, an, alto, FIS_BG, r=16, stroke=FIS_LN, sw=2))
        b.append(rect(x + 14, yy0 + 14, 5, alto - 28, FIS, r=3))
        b.append(T(x + 40, yy0 + 44, [f"Misión {m} · {d['comp']}"], 22, FIS, weight="700"))
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
        b.append(rect(x, y, an, alt, "white", r=16, stroke=FIS_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt - 28, cols[i], r=3))
        b.append(T(x + 38, y + 40, [f"ESTRATEGIA {i+1} · {COMP_EST[mis][i]}"], 16, cols[i],
                   weight="700", ls=1.3))
        parrafo_j(b, x + 38, y + 50, e, an - 60, 23, INK, weight="700", lh=32)
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
            "están en la hoja siguiente, en «Si Física no es tu fuerte».",
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
        b.append(rect(M, y, CW, h, FIS_BG if p <= 2 else "white", r=10, stroke=FIS_LN, sw=1.6))
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
        f"Observación proyectada, sin contexto: «{caso}» Qué cambió y qué lo causó. Dinámica E1 «{din[0][0]}» ({din[0][1]}'). Pista para el cierre del momento: {pista}.",
        f"Pregunta modelo: la 1 del libro (página {PAG_LIBRO[mis][0]}), a la vista todo el momento. "
        f"Manos alzadas antes de dibujar o calcular. La pregunta del momento: {PROBLEMATIZADORA[mis]} Se abre la "
        f"página {t_pags[0]} solo en «mi primera idea».",
        f"1-2 en pantalla (página {t_pags[0]}, «{ins.get(1, '—')}» y «{ins.get(2, '—')}»); 3-4, 5-6, "
        f"7-8 y 9-10 en las páginas {t_pags[1]}, {t_pags[2]}, {t_pags[3]} y {t_pags[4]}. Entre "
        f"bloques, las dinámicas E2, E3 y E4."
        + (f" Sello en {'la pregunta' if ',' not in sel else 'las preguntas'} {sel}." if sel else ""),
        f"Reto del corte: «{RETOS[mis][0]}». Equipos de tres; cada uno registra en SU tarjeta. La "
        f"defensa señala la flecha, la cuenta con su unidad o la variable que se controló.",
        f"Entrenamiento, páginas {i_pags[0]} y {i_pags[1]}. Cuatro preguntas tipo Saber 11, en "
        f"silencio y con reloj.",
        f"Solo las falladas, con la flecha o la cuenta que las resuelve. «Palabras que me frenaron», "
        f"«lo que me llevo», carita de salida y la causa del día en la clase {mis} de la portada.",
    ]
    y = seccion(b, y, "El sábado, minuto a minuto",
        "Las seis fases con el contenido de este momento puesto encima.")
    reloj = 0
    for (nom, mins, c, *_), txt in zip(FASES, concreto):
        lin = wrap_px(txt, 21, CW - 440)
        h = max(70, 24 + len(lin) * 29)
        b.append(rect(M, y, CW, h, "white", r=14, stroke=FIS_LN, sw=1.8))
        b.append(rect(M + 12, y + 12, 5, h - 24, c, r=3))
        b.append(T(M + 40, y + h / 2 - 2, [f"{reloj:02d}'–{reloj+mins:02d}'"], 22, c, weight="700"))
        b.append(T(M + 40, y + h / 2 + 26, [nom], 19, GRAY))
        parrafo_j(b, M + 400, y + (h - len(lin) * 29) / 2 - 5, txt, CW - 440, 21, INK, lh=29)
        reloj += mins
        y += h + 6
    y += 20
    y = seccion(b, y, "Si Física no es tu fuerte",
        "Lo que tienes que poder explicar en dos minutos, sin jerga. Si un estudiante sabe más que "
        "tú de un tema, déjalo explicar y pide que lo muestre con una flecha o con una cuenta con unidades.",
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
        "pregunta, con cuentas y unidades; el texto completo, las figuras y por qué cae cada opción "
        "están en la guía de clase.")
    for k, (x4, est, ins_, ctx) in enumerate(INS_ICFES.get(mis, [])):
        fila = banco[k] if k < len(banco) else {}
        ctx_ = fila.get("contexto", "—")
        if (mis, x4) in ASED:
            ctx_ += " · " + ASED_NOTA
        i_est = d["estr"].index(est) if est in d["estr"] else 0
        cc = COLS_MIS[mis][i_est]
        l_c = wrap_px(ctx_, 20, 620, "700")
        l_i = wrap_px(ins_, 19, 640, style="italic")
        h = max(62, 20 + max(len(l_c), len(l_i)) * 28)
        b.append(rect(M, y, CW, h, "white", r=12, stroke=FIS_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, h - 20, cc, r=2))
        b.append(T(M + 36, y + h / 2 - 3, [f"P{x4}"], 21, cc, weight="700"))
        b.append(T(M + 36, y + h / 2 + 20, [f"pág. {i_pags[0] if x4 <= 2 else i_pags[1]}"], 16, GRAY))
        b.append(T(M + 150, y + h / 2 + 8, [f"E{i_est+1} · {comp_icfes(mis, x4)}"], 18, cc, weight="700"))
        parrafo_j(b, M + 290, y + (h - len(l_c) * 28) / 2 - 4, ctx_, 620, 20, INK, weight="700", lh=28)
        parrafo_j(b, M + 940, y + (h - len(l_i) * 28) / 2 - 4, ins_, 640, 19, GRAY, style="italic", lh=28)
        cl = fila.get("clave", "").strip()
        b.append(rect(W - M - 96, y + h / 2 - 22, 64, 44, FIS_BG, r=10, stroke=FIS, sw=2))
        b.append(T(W - M - 64, y + h / 2 + 10, [cl or "—"], 26, FIS, weight="700", anchor="middle"))
        y += h + 6
    y += 22
    y = seccion(b, y, "Después de la clase · tu registro",
        "Se llena el mismo sábado, antes de salir. Esto no lo ve el estudiante.")
    alto_reg = int(min(232, (2470 - y - 14) / 2))
    registro_docente(b, y, alto=alto_reg, campos=[
        ("¿Qué concepto hubo que explicar dos veces?", "y con qué ejemplo funcionó la segunda"),
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
             "El estudiante SÍ puede dibujar al margen las flechas y hacer las cuentas con unidades: "
             "en la prueba real también puede, y es lo que entrenó.",
             "No se responde ninguna duda, ni de conceptos.",
             "Los últimos 30 minutos: cada uno cuenta sus aciertos por competencia (UC, EF, IN)."]),
           ("Clase 8 · la devolución", VERDE, VERDE_BG, VERDE_LN,
            "Reparación con el instrumento de la primera vez",
            ["Se eligen las cinco preguntas que más falló el grupo.",
             "Cada estudiante compara lo que escribió al margen en el simulacro con el instrumento "
             "de su hoja de entrenamiento.",
             "La pregunta que gobierna la clase: ¿qué flecha, qué julio o qué unidad viste esta vez "
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
        b.append(rect(x, y, an2, alto2, "white", r=16, stroke=FIS_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alto2 - 28, FIS, r=3))
        b.append(T(x + 40, y + 46, [f"{cod} · {len(grupos[cod])} preguntas"], 23, INK, weight="700"))
        b.append(T(x + 40, y + 76, [COMP_NOM[cod].lower()], 19, GRAY, style="italic"))
        for j, ln in enumerate(lineas[cod]):
            b.append(T(x + 40, y + 108 + j * 27, [" ".join(ln)], 19, FIS, weight="700"))
        yb = y + 108 + len(lineas[cod]) * 27 - 6
        b.append(T(x + 40, yb + 20, ["aciertos del grupo"], 18, GRAY))
        b.append(rect(x + 230, yb - 6, an2 - 270, 40, FIS_BG, r=10, stroke=FIS_LN, sw=1.8))
    y += alto2 + 30
    y = seccion(b, y, "Las cinco preguntas que se reparan en la clase 8")
    cx = [M, M + 200, M + 560, M + 1160]
    y = encabezado_tabla(b, y, list(zip(cx, ["N.º", "MOMENTO Y PÁGINA", "QUÉ FLECHA O CUENTA HABÍA QUE VER",
                                              "QUÉ FALLÓ EL GRUPO"])))
    for k in range(1, 6):
        b.append(rect(M, y, CW, 76, "white", r=12, stroke=FIS_LN, sw=1.8))
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
        "movimiento que después hará la mente frente al dibujo o la cuenta. Antes de usar una, responde "
        "esto: ¿qué paso de la estrategia está ejercitando? Si no hay respuesta, es recreo, no clase.",
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
           ("Las claves que el grupo discutió", "M2 P10, M4 P3 y P9 y las de reserva media: a la editorial"),
           ("Los avisos nuevos que encuentres", "la lista se hizo resolviendo, y seguro falta alguno")]
    for t, s_ in dev:
        b.append(rect(M, y, CW, 64, "white", r=14, stroke=FIS_LN, sw=2))
        b.append(rect(M + 14, y + 12, 5, 40, ORO, r=3))
        b.append(checkbox(M + 42, y + 19, 13, FIS))
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


PDF = "/home/user/educate-saber11/entregables/EDUCATE_Planeador_Fisica.pdf"


def revisa_pie(svg):
    """Lo que verifica_plan.py no ve: un recuadro que EMPIEZA debajo de 2470 (lo toma por el pie y
    no lo cuenta). El pie del planeador es el recuadro de y = 2476 y sus textos de y = 2522; nada más
    puede quedar de 2470 para abajo. Devuelve la lista de lo que se mete en el pie."""
    s = open(svg, encoding="utf-8").read()
    malos = []
    for m in re.finditer(r'<rect[^>]*\by="([-\d.]+)"[^>]*\bheight="([-\d.]+)"', s):
        y, h = float(m.group(1)), float(m.group(2))
        if h >= 2500 or abs(y - 2476) < 1:
            continue
        if y + h > 2470:
            malos.append(f"recuadro de y = {y:.0f} a {y + h:.0f}")
    for m in re.finditer(r'<text[^>]*\by="([-\d.]+)"', s):
        y = float(m.group(1))
        if y > 2470 and abs(y - 2522) > 1:
            malos.append(f"texto en y = {y:.0f}")
    return malos

if __name__ == "__main__":
    import sys
    import render
    malas = verificar()
    if malas:
        raise SystemExit("No cuadra:\n  " + "\n  ".join(malas))
    hojas = build()
    print(len(hojas), "hojas del planeador de Física")
    pisan = {h.rsplit("_", 1)[1]: revisa_pie(h) for h in hojas}
    pisan = {k: v for k, v in pisan.items() if v}
    if pisan:
        raise SystemExit("Se meten en el pie:\n  " + "\n  ".join(f"{k}: {v[:3]}" for k, v in pisan.items()))
    if "--pdf" in sys.argv:
        render.unir(hojas, PDF)
        n, sin = render.verifica(PDF, "PLANEADOR")
        print(f"{PDF}: {n} páginas · sin pie: {sin or 'ninguna'}")
