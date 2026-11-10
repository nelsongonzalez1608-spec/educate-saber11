#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PLANEADOR DEL DOCENTE · BIOLOGÍA · las ocho clases del área.

Mismo modelo aprobado en el piloto de Matemáticas y ya entregado en Lectura Crítica y Sociales
(plan_soc.py): seis momentos de 15·20·35·20·20·10, «tu aporte» acotado en cada uno y un banco de
dinámicas isomorfas a las estrategias. Usa el motor de plan_piezas.py sin cambiarlo; el dibujo de
las hojas sale de plan_soc.py, adaptado aquí (plan_soc no se toca).

Lo propio del área: donde Sociales tiene el mapa de actores, Biología tiene EL DATO Y SU
COMPARACIÓN de la portada del área (página 166 del cuaderno de 398): qué cambió, qué se midió y contra qué se compara.
Siete sellos «Alto · aquí entra el profe» (seis del taller y uno del entrenamiento) y cuatro claves
del libro que el profe tiene que saber defender o discutir (M4 P7 y P9, M6 P2 y P10).

Para las guías (clase_viva_bio.py), con los mismos nombres de plan_soc.py:
    FASES  CLASES  BASE  LIBRO  PAG_LIBRO  MISIONES  AVISOS  TALLER  INS_ICFES  BANCO  SELLOS
    SABERES  DINAMICAS  RETOS  CLAVES  ACTIVACION  PROBLEMATIZADORA  PREGUNTA_AREA
    NO_ES_TU_FUERTE  COLS_MIS  COMP_EST  COMP_NOM  COMP_ICFES
COMP_ICFES {misión: [competencia de P1…P4]} es la que el cuaderno le pone a cada pregunta de
entrenamiento (campo comp de bioN_icfes.py, leído sin importar el módulo). COMP_EST sale de ahí:
cada estrategia toma la competencia de su pregunta de entrenamiento.

Claves del libro: copiadas del docstring de bio1.py … bio6.py (resueltas a mano el 7 nov) y
comprobadas al construir con `verificar()`. Las del entrenamiento: tablero/icfes.csv, cruzadas
con el docstring de bioN_icfes.py y resueltas de nuevo el 10 nov (ver TEXTOS_BIO.md).

Membrete (Nelson, 10 nov): «Pregunta Saber 11», sin año ni «oficial». En este planeador las
preguntas de entrenamiento se llaman «preguntas tipo Saber 11».
"""
import ast, csv, re
from plan_piezas import *
import plan_piezas as PZ
import paginas as PG          # la numeración final del cuaderno (398 páginas, 10 nov): única fuente

BIO = "#30843C"; BIO_BG = "#EEF6EF"; BIO_LN = "#BFDDC4"
TOTAL = 24
configurar(BIO, BIO_BG, BIO_LN, "Biología", TOTAL)
AREA_CSV = "Biología"

AZUL = "#242478"; ROJO_E = "#A82424"; ORO_E = "#C9821B"
# El cierre no va en verde: el verde es el color del área (y de la activación).
PIZARRA = "#4A5A70"

# Los colores de las cuatro estrategias, tal como salen en los chips del cuaderno (EST de bioN.py).
COLS_MIS = {1: [AZUL, ROJO_E, ORO_E, MORADO], 2: [AZUL, ROJO_E, ORO_E, MORADO],
            3: [AZUL, MORADO, ROJO_E, ORO_E], 4: [AZUL, MORADO, ORO_E, ROJO_E],
            5: [AZUL, ROJO_E, MORADO, ORO_E], 6: [AZUL, MORADO, ROJO_E, ORO_E]}
COLS_EST = COLS_MIS[1]

# ─────────────────────────── los seis momentos ───────────────────────────
# El reparto es el aprobado: 15 · 20 · 35 · 20 · 20 · 10 = 120. No se cambia.
FASES = [
    ("Activación", 15, BIO,
     "Que el estudiante describa un fenómeno corto con tres preguntas —qué cambió, qué se midió y "
     "contra qué se compara— antes de explicarlo y antes de ver cualquier opción.",
     ["Proyecta o lee una observación de dos o tres renglones sin decir de dónde salió.",
      "Pide tres respuestas, en voz alta o en el tablero: qué cambió, qué se midió y contra qué se compara.",
      "Ejecuta la dinámica de apertura según la estrategia del encuentro."],
     "No explica el fenómeno ni acepta todavía explicaciones. Si alguien dice «es por las hormonas», "
     "le devuelve la pregunta: «¿qué dato te lo dice?». El cuaderno sigue cerrado.",
     "Proyector o tablero con la observación. Todavía no se abre el cuaderno."),
    ("Pregunta problematizadora", 20, "#1F4E8C",
     "Que el estudiante compruebe que en Biología la respuesta sale del dato —del texto, la tabla o "
     "la gráfica— y no de lo que suena científico, usando la pregunta modelo del libro.",
     ["Presenta la pregunta modelo del libro y la deja a la vista todo el momento.",
      "Pide respuestas a mano alzada ANTES de releer el texto o la gráfica, y las anota en el tablero.",
      "Hace la pregunta que gobierna el área: ¿qué dato, del texto, la tabla o la gráfica, respalda eso?",
      "Revela la clave solo al final y trabaja por qué cae cada una de las otras tres."],
     "Regla del momento: nadie justifica con «yo sé que» ni con lo que vio en internet. Toda "
     "intervención señala un renglón del texto, un número de la tabla o un punto de la gráfica.",
     "Libro abierto en la pregunta modelo. Cuaderno solo en «mi primera idea»."),
    ("Desarrollo guiado", 35, "#3B3BA6",
     "Que el estudiante escriba el instrumento —el dato, la comparación, el eslabón o el oficio— "
     "antes de mirar las opciones, y deje por escrito de dónde lo sacó.",
     ["Entrega las hojas del momento y trabaja por bloques: 1-2, 3-4, 5-6, 7-8 y 9-10.",
      "Antes de que marquen, verifica que el instrumento tenga escrito el dato o el eslabón que pide.",
      "Entre bloques, introduce la dinámica de la estrategia que viene: seis minutos, no más.",
      "Cuando aparece un sello «Alto · aquí entra el profe», explica el concepto en dos minutos y sigue."],
     "No explica el fenómeno antes que ellos ni dicta la respuesta. Si un estudiante se traba, le "
     "pregunta qué cambió y contra qué lo compara; si el instrumento está vacío, lo devuelve al texto "
     "o a la gráfica antes que a las opciones.",
     "Cuaderno, las cinco hojas de taller. Libro, en las preguntas 1 a 10."),
    ("Reto en equipo", 20, MORADO,
     "Que el estudiante defienda su explicación con el dato en la mano y acepte que otro equipo "
     "puede ver una variable o un eslabón que él no vio.",
     ["Arma equipos de tres y entrega el reto del corte de este momento.",
      "Exige que cada integrante llegue con su instrumento YA diligenciado individualmente.",
      "Da tres minutos de defensa por equipo: señalan el dato, la comparación o el eslabón que los respalda.",
      "Cierra mostrando qué variable o qué eslabón quedó por fuera en cada propuesta."],
     "El equipo discute, pero cada uno escribe en SU tarjeta del reto. No se acepta una defensa que "
     "diga «es que así funciona»: se nombra el dato, el grupo de comparación o el paso del proceso.",
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
     "Que el estudiante nombre la estrategia que usó y se lleve un concepto del día —un proceso, una "
     "estructura o una relación— escrito en sus propias palabras.",
     ["Socializa solo las preguntas que el grupo falló, pidiendo el dato o el eslabón que las resuelve.",
      "Pide que lean en voz alta su salvavidas: lo mínimo que sí tenían claro.",
      "Cada uno escribe el concepto del día en la franja «Palabras que me frenaron» de su hoja."],
     "No dicta la definición. El concepto se escribe como el estudiante lo entendió; si quedó mal "
     "entendido, eso se ve en la hoja y se corrige la próxima clase.",
     "Cuaderno: «Palabras que me frenaron», «lo que me llevo», carita de salida y portada del área."),
]

# Páginas del cuaderno. Los módulos de misión siguen en la numeración vieja (mapa de 347); lo
# impreso va en la de 398 (portada, seis misiones y, al final, las hojas de simulacro).
# paginas.nueva() traduce: si la numeración cambia, basta volver a construir.
BASE_VIEJA = {1: 140, 2: 147, 3: 154, 4: 161, 5: 168, 6: 175}
BASE = {m: PG.nueva(b) for m, b in BASE_VIEJA.items()}
PORTADA = PG.nueva(139)
AREA_PAGS = PG.rango_area("bio")
SIMULACRO_PAGS = PG.paginas_simulacro("bio")
SIM = f"{SIMULACRO_PAGS[0]} a {SIMULACRO_PAGS[-1]}"


def _pags(m):
    return f"{BASE[m]} a {BASE[m] + 6}"


CLASES = [
    (1, "Momento 1 · Biológico-celular", f"páginas {_pags(1)} del cuaderno"),
    (2, "Momento 2 · Biológico-organísmico", f"páginas {_pags(2)} del cuaderno"),
    (3, "Momento 3 · Biológico-ecosistémico", f"páginas {_pags(3)} del cuaderno"),
    (4, "Momento 4 · Ciencia, tecnología y sociedad", f"páginas {_pags(4)} del cuaderno"),
    (5, "Momento 5 · Entorno biológico · herencia", f"páginas {_pags(5)} del cuaderno"),
    (6, "Momento 6 · Entorno biológico · cierre del área", f"páginas {_pags(6)} del cuaderno"),
    (None, "Simulacro del área", "el simulacro que aplica EDUCATE, en condiciones de examen"),
    (None, "Socialización del simulacro", f"hojas de simulacro del cuaderno, páginas {SIM}"),
]

# Clases 7 y 8 (decisión de Nelson, 10 nov): el simulacro es una prueba que escoge EDUCATE y no está en
# el cuaderno; la clase 8 socializa sus preguntas en las hojas de simulacro. C7 y C8: plan_simulacro.py.
import plan_simulacro as PS
C7, C8 = PS.datos("bio", conteo="competencia (UC, EF, IN)", dinamica=dict(
    nombre="Lo que sí y lo que no", formato="en parejas",
    pasos=["Parejas con la segunda pregunta asignada. A dice en voz alta lo que cambia (la variable o el "
           "dato que manda) y en qué escala pasa.",
           "B propone a propósito una conclusión que dice más de lo que los datos permiten.",
           "A la corta: dice qué parte sí sostienen los datos y cuál no alcanza, y lo escribe en «lo que sí "
           "concluyo» y «lo que no alcanza».",
           "Cambian de papel para el tacho: cada opción descartada lleva la razón que dan los datos."],
    entrena="Separar lo que los datos permiten concluir de lo que se les agrega. Son las piezas «lo que "
            "cambia», «lo que sí concluyo» y «lo que no alcanza» del esquema."))

LIBRO = {1: (72, 75), 2: (83, 85), 3: (94, 97), 4: (104, 107), 5: (116, 119), 6: (127, 130)}
# Página del libro de cada pregunta: «la lees en tu libro, página N» (Q[n]["pag"] de bioN.py).
PAG_LIBRO = {
 1: [72, 73, 73, 73, 73, 74, 74, 74, 75, 75],
 2: [83, 83, 83, 84, 84, 84, 84, 85, 85, 85],
 3: [94, 95, 95, 95, 96, 96, 96, 97, 97, 97],
 4: [104, 105, 105, 105, 106, 106, 106, 107, 107, 107],
 5: [116, 117, 117, 117, 117, 118, 118, 118, 119, 119],
 6: [127, 128, 128, 128, 128, 129, 129, 130, 130, 130],
}

# Las tres competencias de Ciencias Naturales en el Saber 11.
COMP_NOM = {"UC": "Uso comprensivo del conocimiento científico", "EF": "Explicación de fenómenos",
            "IN": "Indagación"}
_COD = {"uso comprensivo": "UC", "explicación de fenómenos": "EF", "indagación": "IN"}

MISIONES = {
 1: dict(comp="Biológico-celular", pags=_pags(1),
   tema="La célula: una fábrica que trabaja en cadena",
   competencia="EF · explicación de fenómenos",
   estr=["Cada organelo, su oficio", "La ruta de la proteína, estación a estación",
         "Comparar contra el que no cambió", "Dónde hay más y hacia dónde va"],
   instala="Que la célula se lee como una fábrica en cadena: cada organelo tiene un oficio, la "
           "proteína recorre sus estaciones en orden y, si una falla, todo lo que viene después se "
           "detiene. Y que un efecto solo se afirma comparando contra el grupo que no cambió.",
   ojo="La figura de la pregunta 1 tacha con una X roja el lisosoma, que es justo la clave: se "
       "acierta sin razonar. Pide que prueben los cuatro organelos antes de mirar el dibujo. Las "
       "preguntas 4 y 10 preguntan casi lo mismo (el Golgi alterado), y la 6 y la 7 también.",
   cierre="La estrategia 4 —dónde hay más y hacia dónde va— tiene una sola pregunta en el taller (la "
          "2) y una en el entrenamiento. Dale en la dinámica el tiempo completo: es la base de la "
          "ósmosis y del transporte activo, que vuelven en las misiones 2 y 3."),
 2: dict(comp="Biológico-organísmico", pags=_pags(2),
   tema="El equilibrio de adentro: un cuerpo que se regula",
   competencia="UC · uso comprensivo",
   estr=["El circuito que vuelve al equilibrio", "La función sale del texto",
         "Dato contra dato, especie contra especie", "Lo que alcanza a explicar"],
   instala="Que el cuerpo se regula con circuitos: algo se desvía, un sensor lo detecta, un centro "
           "da una orden y un efector lo corrige. Y que la función de una estructura se saca de las "
           "palabras del texto, no de lo que uno ya cree saber.",
   ojo="La pregunta 10 trae una errata: dice que el páncreas artificial evita las «hipoglucemias», "
       "cuando liberar insulina al subir la glucosa evita las hiperglucemias. La pregunta 2 no tiene "
       "una opción que explique a las dos personas: la clave A es la única fisiológicamente cierta.",
   cierre="La pregunta 5 pide lo que cambia «primero» y el texto dice que la urea baja «gradualmente». "
          "No se contradicen: algo puede empezar primero y tardar en terminar. Vale la pena decirlo."),
 3: dict(comp="Biológico-ecosistémico", pags=_pags(3),
   tema="En el ecosistema nada cambia solo",
   competencia="UC y EF · datos, redes y límites",
   estr=["Los datos hablan primero", "Sigue la red: quién depende de quién",
         "Busca el factor que limita", "Del saber ecológico a la decisión"],
   instala="Que en un ecosistema nada cambia solo: los datos se leen contra el control, la red dice "
           "quién depende de quién, el factor que falta manda sobre los demás y una decisión ambiental "
           "se defiende con un dato que se pueda comprobar.",
   ojo="En las preguntas 2, 3, 4 y 5 la clave es la única opción razonable y las otras son disparates "
       "visibles: se aciertan por descarte. Exige el instrumento lleno antes de mirar las opciones; "
       "ahí está la ecología que esas preguntas no miden.",
   cierre="La tabla de la pregunta 1 no trae unidades y la de las preguntas 8 y 9 escribe los "
          "decimales con punto. Aprovéchalo: un dato sin unidades no se puede comparar con otro estudio."),
 4: dict(comp="Ciencia, tecnología y sociedad", pags=_pags(4),
   tema="Cada invento es una oportunidad y un riesgo",
   competencia="IN · indagación",
   estr=["¿Se puede poner a prueba?", "El mecanismo, eslabón por eslabón",
         "Para qué sirve cada pieza", "Lo que la evidencia respalda (y lo que no)"],
   instala="Que todo invento se mira con cuatro preguntas: ¿se puede poner a prueba?, ¿cuál es el "
           "mecanismo, eslabón por eslabón?, ¿para qué sirve cada pieza? y ¿qué respalda de verdad la "
           "evidencia, y qué no?",
   ojo="Las claves de las preguntas 7 y 9 son imprecisas: en la 7 el cambio de color es de los "
       "sensores y no de las nanopartículas; en la 9 el objetivo es personalizar contra el tumor, no "
       "disminuir efectos secundarios. Son las mejores de las cuatro. Si un estudiante lo nota, tiene razón.",
   cierre="Varias fuentes del libro (la cirugía fetal de 2025, la cifra de «hasta un 37 %» de memoria, "
          "el globo de Manizales) no se pudieron verificar. Trátalas como casos para razonar, no como "
          "datos para memorizar."),
 5: dict(comp="Entorno biológico", pags=_pags(5),
   tema="Lo que se hereda, lo que se edita y lo que se arriesga",
   competencia="IN y UC · herencia y pruebas",
   estr=["Seguir el alelo por la familia", "Del cambio en el ADN a lo que se ve",
         "La prueba que sí responde la pregunta", "Lo que gana, lo que arriesga, lo que exagera"],
   instala="Que un rasgo se sigue alelo por alelo de los padres a los hijos, que un cambio en el ADN "
           "se ve en el organismo paso por paso, que solo responde una pregunta la prueba que compara "
           "contra un control y que toda tecnología trae algo que gana y algo que arriesga.",
   ojo="La pregunta 6 habla de «la nueva información sobre la consanguinidad en la comunidad», pero "
       "ese texto no está en el libro: se cortó. Se responde con lo general. La opción D de la pregunta "
       "1 trae un dato falso: la portadora no transmite a todos sus hijos varones, sino a la mitad.",
   cierre="El texto del Pomsky culpa a los perros «híbridos»; cruzar dos razas distintas en principio "
          "reduce la homocigosis, y el problema aparece al cruzar parientes. Sepáralo en clase: mezclar "
          "razas no es lo mismo que cruzar hermanos."),
 6: dict(comp="Entorno biológico", pags=_pags(6),
   tema="La vida cambia: ambiente, selección y ecosistemas",
   competencia="UC, IN y EF · cierre del área",
   estr=["El ambiente o la herencia", "Lo que los datos sí dejan concluir",
         "Si se cae una pieza del ecosistema", "Para qué le sirve ese rasgo"],
   instala="Que la vida cambia con dos relojes: el de la vida de un individuo (el ambiente) y el de la "
           "historia de una población (la herencia y la selección). Es la misión que recoge las cinco "
           "anteriores: datos, comparaciones, redes y funciones.",
   ojo="La pregunta 10 tiene dos opciones defendibles: la B también es consistente con la tabla y el "
       "texto. La clave D es la que usa la comparación de los tres páramos que pide el enunciado. "
       "Acepta la discusión y no castigues a quien marque la B con argumentos.",
   cierre="En la pregunta 2 la clave dice que hubo respuesta en «autocontrol», pero en la tabla el "
          "autocontrol fue alto en los dos grupos: es la menos mala. La lección de cierre del área: una "
          "conclusión vale lo que valen los datos que de verdad usa."),
}

# Claves del libro: docstring de bio1.py … bio6.py (verificar() las compara al construir).
CLAVES = {
 1: dict(zip(range(1, 11), "ABBCDABBAC")),
 2: dict(zip(range(1, 11), "CACDACBAAD")),
 3: dict(zip(range(1, 11), "CABCBDCDBD")),
 4: dict(zip(range(1, 11), "BCCADAACAA")),
 5: dict(zip(range(1, 11), "BDCAADBDAC")),
 6: dict(zip(range(1, 11), "DAABBACABD")),
}

# ─────────── lo que el libro trae y hay que saber antes de entrar (de hallazgos.csv y
# tablero/propuestas/bioN_hallazgos.csv) ───────────
# Rótulo: «preg. N», «preg. N y M», «preg. N a M» (lo lee el motor de las guías), «ICFES k» para
# el entrenamiento, o un rótulo general. Severidad: alta · media · baja · atención.
AVISOS = {
 1: [("preg. 1", "media",
      "La figura del libro tacha con una X roja el lisosoma, que es la clave: se acierta sin razonar.",
      "Pide que prueben los cuatro organelos antes de mirar el dibujo. El cuaderno lo advierte."),
     ("preg. 9", "media",
      "El texto se contradice: dice que la línea B no expresa genes de proteínas de secreción y luego "
      "que la diferencia no se debe a la capacidad de síntesis.",
      "La clave A se sostiene con la conclusión de los investigadores. Si alguien duda, leyó bien."),
     ("preg. 4 y 10", "media",
      "Las dos evalúan lo mismo —el Golgi alterado deja proteínas sin empacar en el citoplasma— y las "
      "dos tienen clave C.",
      "Trabaja la 10 comparando las células A y B, como pide su instrumento."),
     ("preg. 6 y 7", "baja",
      "Usan el mismo estudio de gemelos y piden casi la misma conclusión.",
      "La 6 se trabaja leyendo el modelo y la 7 armando la ficha de variables."),
     ("preg. 5", "atención",
      "La opción C dice que el núcleo y el RER «solo reducen» la exportación; la gráfica muestra cero "
      "en los tres grupos tratados.",
      "Que lean el número de cada barra: reducir no es detener."),
     ("ICFES 4", "atención",
      "En la tabla, con los insecticidas 1, 2 y 3 sobreviven más cucarachas que sin insecticida.",
      "No cambia la clave. Úsalo: esos insecticidas no solo no sirven, parecen proteger.")],
 2: [("preg. 2", "media",
      "Ninguna opción explica la diferencia entre las dos personas: la A solo habla del corredor, la C "
      "contradice el enunciado y la D le pone sudor a quien está en la sala fría.",
      "La A se defiende como la única fisiológicamente cierta. Dilo abiertamente, como el cuaderno."),
     ("preg. 10", "media",
      "Errata: el texto dice que el páncreas artificial evita las «hipoglucemias»; liberar insulina "
      "cuando la glucosa sube evita las hiperglucemias.",
      "No cambia la clave D. Corrígelo en voz alta."),
     ("preg. 5", "atención",
      "Pide la variable que cambia «primero» y el texto dice que la urea baja «gradualmente».",
      "No se contradicen: algo puede empezar primero y tardar en terminar."),
     ("preg. 7", "atención",
      "La clave B (tasa metabólica más baja) no se lee en la tabla: se infiere de la glucosa más baja "
      "y del texto de la estivación.",
      "Que crucen tabla y texto, columna por columna."),
     ("preg. 1", "baja",
      "La figura dice «AUMENTO DE ORINA» junto al riñón: deja a un paso la clave.",
      "El instrumento obliga a seguir el agua hasta lo que queda en el cuerpo."),
     ("preg. 8", "atención",
      "La opción B dice que el camello baja su temperatura para sudar menos; en realidad la deja "
      "subir durante el día.",
      "No cambia la clave A. Puedes contar el dato real como ampliación.")],
 3: [("preg. 1 · tabla", "baja",
      "La tabla de biomasa no dice en qué unidades está ni qué se midió exactamente.",
      "Se resuelve por la tendencia. Un dato sin unidades no se compara con otro estudio: dilo."),
     ("preg. 1 · opción B", "atención",
      "La opción B dice que descomponer más «disminuye la producción primaria»: es un error "
      "conceptual, porque descomponer libera nutrientes.",
      "Dilo para que el distractor no se quede como dato."),
     ("preg. 2 a 5", "atención",
      "La clave es la única opción razonable; las otras son disparates visibles (sensores que «atraen» "
      "aves, el jaguar compitiendo por el pasto).",
      "Exige el instrumento lleno antes de las opciones: ahí está la ecología."),
     ("preg. 8 y 9", "baja",
      "La tabla escribe «2.8 millones» con punto decimal, y la opción D de la 8 habla de «diversidad "
      "funcional» con solo dos grupos.",
      "Escríbelo bien en el tablero: 2,8 millones."),
     ("ICFES 1", "atención",
      "El esquema de la pregunta dice «sustracción del oxígeno disuelto para tomar fosfatos y nitratos»: el "
      "oxígeno lo gasta la descomposición. La clave C sí lo dice bien.",
      "Corrige el esquema en voz alta al socializar."),
     ("ICFES 3", "atención",
      "La tabla pone «Gas natural · Propano»: el gas natural es sobre todo metano.",
      "No afecta la clave A.")],
 4: [("preg. 7", "media",
      "El cambio de color lo producen los sensores de pH, no las nanopartículas; la clave A se lo "
      "atribuye a las nanopartículas.",
      "Es la mejor de las cuatro. Si un estudiante lo nota, tiene razón: díselo."),
     ("preg. 9", "media",
      "La clave A dice adaptar la vacuna «al sistema inmune para disminuir efectos secundarios»; el "
      "texto la adapta al tumor y la menor toxicidad es un resultado.",
      "Se elige por descarte. Enseña a escoger la menos mala cuando ninguna es perfecta."),
     ("preg. 1", "atención",
      "La «primera cirugía fetal exitosa» (2025) no se verificó, y la opción B habla de vasos que el "
      "texto no menciona.",
      "Usa el sello: qué le pasa a un órgano apretado por un orificio."),
     ("preg. 2 a 5", "atención",
      "Las fuentes (2023 y 2025) y la cifra de «hasta un 37 %» de mejora de la memoria no se verificaron.",
      "Trátalas como caso, no como dato."),
     ("patrón de opciones", "atención",
      "En las preguntas 4, 6, 8 y 10 la correcta es la más técnica y las otras son absurdas a la "
      "vista: se aciertan por descarte.",
      "Exige el eslabón escrito antes de mirar las opciones."),
     ("reparto de claves", "baja",
      "A es clave 5 veces (4, 6, 7, 9 y 10) y D una sola vez.",
      "Reportado a la editorial. No lo digas en clase."),
     ("ICFES 1", "baja",
      "La barra «con pectinasa» de la gráfica A casi no se ve en la fotocopia: se redibujó.",
      "La clave B no depende de la A.")],
 5: [("preg. 6", "media",
      "La pregunta cita «la nueva información sobre la consanguinidad en la comunidad», pero ese "
      "texto no está en el libro: parece que se cortó.",
      "Se responde con lo general: entre parientes aumentan los homocigotos. El cuaderno lo dice."),
     ("preg. 6 · opción A", "atención",
      "La premisa de la opción A (la frecuencia del alelo no cambia) es cierta; lo falso es su conclusión.",
      "Distingue cuántos alelos hay de cuántos hijos salen con dos copias."),
     ("preg. 1", "atención",
      "La opción D dice que la portadora transmite la enfermedad ligada al X a todos sus hijos varones: "
      "es falso, en promedio a la mitad.",
      "No cambia la clave B. Que nadie se lleve el dato falso."),
     ("preg. 8 a 10", "media",
      "El texto culpa a los perros «híbridos»; cruzar dos razas distintas en principio reduce la "
      "homocigosis: el problema es cruzar parientes. El «30 %» de vida no trae fuente.",
      "Separa mezclar razas de cruzar hermanos, como el cuaderno en la 9."),
     ("preg. 5 y 7", "atención",
      "El distractor «transformar genes recesivos en dominantes» sale dos veces; en una bacteria no "
      "tiene sentido.",
      "Aprovecha la repetición en la 7."),
     ("patrón de opciones", "atención",
      "En las preguntas 2, 4, 9 y 10 la correcta es la más larga o la que integra; en la 10 las otras "
      "cierran con absolutos.",
      "No enseñes el truco. Instrumento antes de opciones.")],
 6: [("preg. 10", "alta",
      "Dos opciones defendibles: la B también es consistente con la tabla y el texto. La D es la que "
      "usa la comparación de los tres páramos que pide el enunciado.",
      "Clave tomada: D. Si alguien marca B con argumentos, reconócelo."),
     ("preg. 2", "media",
      "La clave A dice que hubo respuesta en «autocontrol», pero en la tabla el autocontrol fue alto "
      "en los dos grupos.",
      "Es la menos mala. Que comparen rasgo por rasgo."),
     ("preg. 1", "media",
      "Pide una «hipótesis evolutiva» sobre un experimento de seis meses: eso es ambiente, no "
      "evolución. La clave D sale de la frase introductoria.",
      "Separa los dos relojes, como el instrumento."),
     ("preg. 2 y 3", "atención",
      "Preguntan casi lo mismo y repiten los distractores.",
      "Úsalo para ver si el instrumento se llena igual las dos veces."),
     ("preg. 5", "baja",
      "El texto dice que la extinción se declaró en 2015; según información pública, el registro en "
      "la Lista Roja fue en 2016 y la declaración del gobierno australiano en 2019.",
      "No afecta la clave B. No des la fecha como dato."),
     ("preg. 8", "baja",
      "Pregunta por un «proceso» y las opciones describen rasgos.",
      "No cambia la clave A."),
     ("reparto de claves", "atención",
      "A 4 · B 3 · C 1 · D 2; en la 1, la 9 y la 10 la correcta es la más larga.",
      "Reportado a la editorial. No lo digas en clase.")],
}

# ─────────── los siete sellos «Alto · aquí entra el profe» del cuaderno ───────────
# Leídos de alto_profe() en bio1.py … bio5.py y bio2_icfes.py (la Misión 6 no tiene).
_S = [
 (1, 143, 6, "Gemelos monocigóticos y dicigóticos: cuánto ADN comparten unos y otros."),
 (2, 149, "ICFES 1", "Retroalimentación negativa: una hormona alta frena la orden que la produce."),
 (2, 150, 6, "Qué es una estrategia evolutiva: un rasgo que ayuda a sobrevivir y a dejar descendencia."),
 (3, 158, 7, "Qué lleva una pila por dentro y qué quiere decir que esté «descargada»."),
 (4, 161, 1, "La gastrosquisis y qué le pasa a un órgano apretado por un orificio estrecho."),
 (4, 165, 7, "Qué es un indicador de pH y por qué cambia de color cuando cambia la química."),
 (5, 171, 5, "Radiación ionizante: por qué rompe el ADN y en qué se diferencia de una quemadura."),
]
# _S trae la página vieja (leída del PDF entregado); SELLOS, la del cuaderno de 398.
SELLOS = [(AREA_CSV, m, PG.nueva(pag), preg, saber, "tarjeta de la pregunta", "En el cuaderno")
          for m, pag, preg, saber in _S]
TEXTOS = []        # los textos completos van en la guía (TEXTOS_BIO.md)

# Lo que el profe tiene que poder explicar en cada sello: título, qué es (sin jerga) y la pregunta
# que destraba. Mismo formato que SABERES de plan_soc.py. La del entrenamiento va con clave "I1".
SABERES = {
 (1, 6): ("Gemelos idénticos y mellizos",
          "Monocigóticos (idénticos): un solo óvulo fecundado que se parte en dos; tienen el mismo ADN. "
          "Dicigóticos (mellizos): dos óvulos y dos espermatozoides; comparten más o menos la mitad, "
          "como dos hermanos cualquiera.",
          "¿Estos dos tienen el mismo ADN o solo la mitad?"),
 (2, 6): ("Estrategia evolutiva",
          "Un rasgo que hace que quien lo tiene sobreviva más y deje más descendencia en su ambiente; "
          "por eso se mantiene de generación en generación. No es un plan: nadie lo decide.",
          "¿Le ayuda a sobrevivir? ¿Le ayuda a reproducirse?"),
 (2, "I1"): ("Retroalimentación negativa",
          "Cuando una hormona está alta en la sangre, el cuerpo frena la orden que la produce, como un "
          "termostato que apaga la calefacción. La pastilla mantiene altas dos hormonas y así frena el "
          "pico de la hormona que provoca la ovulación.",
          "Con esas hormonas altas, ¿llega la orden de ovular?"),
 (3, 7): ("Lo que lleva una pila por dentro",
          "Una pila produce electricidad con una reacción química entre metales y otras sustancias "
          "(zinc, manganeso y, en algunas, mercurio, cadmio o litio). «Descargada» quiere decir que la "
          "reacción se agotó, no que quedó vacía: los metales siguen adentro y salen si se rompe.",
          "¿Se le acabó la energía o se le acabó lo que tiene adentro?"),
 (4, 1): ("Gastrosquisis",
          "Un defecto de la pared abdominal del bebé: el intestino crece por fuera, por un orificio. Si "
          "la pared está tensa, el orificio aprieta al intestino y a los vasos que le llevan sangre; con "
          "menos sangre, el tejido puede morir. La toxina relaja el músculo y el orificio aprieta menos.",
          "¿Qué le pasa a un órgano que un orificio aprieta durante semanas?"),
 (4, 7): ("Indicador de pH",
          "Una sustancia que cambia de color según qué tan ácido o básico está el medio, como el agua de "
          "repollo morado. Cuando una fruta se daña cambian la acidez y los gases a su alrededor, y el "
          "indicador lo muestra.",
          "¿El color cambió porque cambió la química o porque cambió la luz?"),
 (5, 5): ("Radiación ionizante",
          "La que tiene energía para arrancarles electrones a los átomos: la de las bombas atómicas, los "
          "rayos X, los rayos gamma. Puede romper el ADN. En una célula del cuerpo puede dar cáncer; en un "
          "óvulo o un espermatozoide, el cambio pasa a los hijos. Una quemadura no reescribe el ADN.",
          "¿Esta célula es del cuerpo o es una célula sexual?"),
}

# ─────────── «Si Biología no es tu fuerte»: cuatro conceptos por clase ───────────
NO_ES_TU_FUERTE = {
 1: [("Los organelos y su oficio",
      "Núcleo: guarda el ADN, las instrucciones. Ribosomas: arman las proteínas. Retículo rugoso: las "
      "recibe y las pliega. Golgi: las modifica, empaca y despacha. Lisosomas: digieren lo que sobra. "
      "Mitocondrias: dan la energía."),
     ("La ruta de secreción",
      "Una proteína que sale de la célula, como la insulina, recorre en orden: núcleo (la instrucción), "
      "ribosoma del retículo rugoso, Golgi, vesícula y membrana. Si una estación se bloquea, todo lo de "
      "después se detiene."),
     ("Ósmosis y transporte activo",
      "El agua pasa por la membrana hacia donde hay más sales disueltas: por eso un suelo con mucho "
      "fertilizante le saca agua a la raíz. Llevar algo hacia donde ya hay más cuesta energía: es "
      "transporte activo."),
     ("Grupo control",
      "El grupo que no recibe el tratamiento y se mide igual. Sin él no se sabe si el cambio lo produjo "
      "el tratamiento. Un efecto se dice como diferencia: cuánto más o cuánto menos que el control.")],
 2: [("Homeostasis y retroalimentación",
      "El cuerpo mantiene estables la temperatura, el agua, la glucosa y el calcio. Funciona como un "
      "termostato: un sensor detecta el cambio, un centro da la orden y un efector lo corrige. Cuando "
      "lo corregido apaga la orden, es retroalimentación negativa."),
     ("La hormona antidiurética",
      "Le ordena al riñón que devuelva agua a la sangre. Sin ella, el riñón deja salir mucha agua: la "
      "persona orina mucho y se deshidrata. Por eso, después de sudar mucho, la orina sale poca y oscura."),
     ("Insulina y glucagón",
      "Después de comer sube la glucosa: el páncreas libera insulina y las células la guardan. En ayunas "
      "baja: el glucagón la saca de las reservas del hígado. Glucosa de más es hiperglucemia; de menos, "
      "hipoglucemia."),
     ("Estivación",
      "Es como hibernar, pero en la sequía y el calor: el animal se entierra, baja su metabolismo y "
      "gasta muy poca agua y energía. Las ranas del libro acumulan urea para no perder el agua del cuerpo.")],
 3: [("Factor limitante",
      "El recurso más escaso respecto a lo que el ser vivo necesita: manda sobre todos los demás. Si "
      "falta oxígeno en el agua, no importa cuánta comida haya: los peces sensibles no viven ahí."),
     ("Red trófica y descomponedores",
      "Quién se come a quién y quién depende de quién. Si sale un depredador, crecen sus presas y bajan "
      "las plantas que ellas comen. Los hongos y las bacterias devuelven al suelo la materia de todo lo "
      "que muere."),
     ("Eutrofización",
      "Cuando a un lago llegan demasiados nutrientes (abonos, aguas negras) crecen de más las algas; al "
      "morir, las bacterias que las descomponen gastan el oxígeno del agua y los peces mueren."),
     ("Fijación de nitrógeno y suelo vivo",
      "El aire tiene mucho nitrógeno, pero las plantas no lo pueden usar así: algunas bacterias del suelo "
      "lo convierten en compuestos que sí. Un suelo sano tiene muchos microorganismos distintos; esa "
      "diversidad es la que miden las preguntas 8 a 10.")],
 4: [("Hipótesis que se puede poner a prueba",
      "Dice qué se compara, qué se mide y qué resultado se espera: «los que usan X recuerdan más palabras "
      "que los que no». «X mejorará la vida en el futuro» no se puede poner a prueba así."),
     ("Fijación de nitrógeno",
      "Las bacterias fijadoras pasan el nitrógeno del aire a compuestos que la planta absorbe por la "
      "raíz. Por eso van en las «bombas de semillas»: abonan sin fertilizante químico."),
     ("Vacunas y linfocitos T",
      "Una vacuna le muestra al sistema inmune una señal del enemigo (un antígeno) para que aprenda a "
      "reconocerlo. Los linfocitos T atacan a las células que llevan esa señal. Contra el cáncer, la "
      "señal es un neoantígeno: una proteína que solo tiene el tumor."),
     ("Lo que respalda un estudio",
      "Un estudio respalda lo que midió, en quienes lo midió y en las condiciones en que lo hizo. Usar "
      "el resultado en otra población o para otro fin es ir más allá de la evidencia.")],
 5: [("Alelos, dominante y recesivo",
      "Cada persona tiene dos copias de cada gen, una de cada padre. Si una copia es dominante, basta "
      "ella para que el rasgo se vea; si es recesiva, se necesitan las dos. Dos padres sanos pueden "
      "tener un hijo enfermo si ambos llevan la copia recesiva."),
     ("Cómo leer un pedigrí",
      "Cuadrado es hombre, círculo es mujer, relleno es afectado. Si dos padres sanos tienen un hijo "
      "afectado, el rasgo es recesivo. Si una hija afectada tiene un padre sano, no es ligado al X recesivo."),
     ("Consanguinidad",
      "Los parientes comparten alelos. Si dos primos llevan el mismo alelo recesivo, sube la "
      "probabilidad de un hijo con las dos copias. El alelo no se vuelve más frecuente: lo que aumenta "
      "es la cantidad de hijos con dos copias iguales."),
     ("CRISPR y plásmidos",
      "CRISPR es una herramienta para cortar y cambiar un pedazo preciso de ADN. Los plásmidos son "
      "anillos pequeños de ADN que las bacterias se pasan entre ellas: así se riega la resistencia a un "
      "antibiótico, y el antibiótico selecciona a las que la tienen.")],
 6: [("Selección natural y artificial",
      "Natural: en un ambiente, los que tienen un rasgo útil sobreviven y dejan más hijos, y el rasgo se "
      "vuelve frecuente. Artificial: la persona escoge quién se reproduce, como con las razas de perros. "
      "Las dos toman generaciones."),
     ("Ambiente y herencia",
      "Lo que le pasa a un perro en su vida (lo estimulan, aprende) cambia su conducta, pero no su ADN, "
      "y no se hereda. La evolución se ve en una población a lo largo de generaciones."),
     ("Variabilidad y flujo génico",
      "Una población grande y conectada con otras tiene más variedad de alelos (heterocigosidad alta) y "
      "responde mejor a un cambio del ambiente. Una pequeña y aislada pierde variedad por azar: es la "
      "deriva genética."),
     ("Especie invasora y páramo",
      "Una especie que llega a donde no tiene depredadores crece sin control, como el pez león en el "
      "Caribe. El páramo y sus frailejones regulan el agua que baja a las ciudades: cuidarlo es cuidar "
      "el agua.")],
}

PREGUNTA_AREA = "¿Qué dato —del texto, la tabla o la gráfica— respalda eso?"
PROBLEMATIZADORA = {
 1: "¿Qué estación de la célula falló, y qué dato lo delata?",
 2: "¿Qué se desvió, quién lo detectó y qué lo devolvió al equilibrio?",
 3: "Si cambia esta pieza, ¿quién más en el ecosistema lo siente?",
 4: "¿Se puede poner a prueba lo que promete este invento?",
 5: "¿De dónde salió ese rasgo, y qué tan probable es que vuelva a salir?",
 6: "¿Esto cambió en la vida de un individuo o en la historia de la población?",
}

# Una observación corta y ORIGINAL para la activación: dos o tres renglones, sin nombres propios,
# con algo que cambió, algo que se midió y algo contra qué comparar. La pista es para el final.
ACTIVACION = {
 1: ("Una levadura en agua tibia con azúcar infla en una hora el globo puesto en la boca de la "
     "botella. La misma levadura en agua tibia sin azúcar, no.",
     "cambió el azúcar; se midió el globo; se compara contra la botella sin azúcar"),
 2: ("Después de un partido al mediodía, un jugador orina mucho menos que un día normal, y la orina "
     "sale más oscura.",
     "cambió el sudor; se midió la orina; se compara con un día normal: el cuerpo guardó agua"),
 3: ("Se sembró fríjol en dos materas iguales: una quedó en el patio y la otra en un clóset. A la "
     "semana, la del clóset estaba más alta, pero amarilla.",
     "cambió la luz; se midió la altura y el color; se compara la matera del patio con la del clóset"),
 4: ("Una aplicación promete que si duermes oyendo música suave, al otro día recuerdas el doble.",
     "¿qué se compara, qué se mide y contra quién? La frase no lo dice: así no se puede poner a prueba"),
 5: ("Dos papás con el color de piel de su familia tienen un hijo albino.",
     "nadie hizo trampa: cada papá guardaba una copia que no se veía, y al hijo le tocaron las dos"),
 6: ("Las palomas de la plaza ya no se asustan cuando la gente pasa; las del campo salen volando apenas "
     "alguien se acerca.",
     "cambió el lugar; ¿lo aprendieron en su vida o se heredó? Con este dato solo, no se sabe"),
}


# ─────────────────────── lo que ya está registrado ───────────────────────
def _instrumentos():
    """Las filas de Biología de tablero/instrumentos.csv. La pregunta del entrenamiento viene como
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


_META = re.compile(r"^(se omiten|figura|las cuatro|contexto|mismo contexto|tabla redibujada)", re.I)


def _banco():
    """Las filas «BIO Mn» de icfes.csv, en el orden del cuaderno (P1…P4 = QA…QD). El contexto se
    queda con lo que dice la pregunta: las notas de formato («figura redibujada…») no van."""
    with open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig") as f:
        r = list(csv.DictReader(f))
    out = {}
    for x in r:
        m = x["mision"].strip()
        if not m.startswith("BIO M"):
            continue
        x = dict(x)
        partes = [p for p in x["contexto"].split(" · ") if not _META.match(p.strip())]
        x["contexto"] = " · ".join(partes[:2]).strip()
        out.setdefault(int(m.replace("BIO M", "")), []).append(x)
    return out


def _comp_icfes():
    """La competencia de cada pregunta de entrenamiento: campo comp de QA…QD en bioN_icfes.py,
    leído con ast (sin importar el módulo, que reconfigura el motor del cuaderno)."""
    out = {}
    for m in range(1, 7):
        src = open(f"/home/claude/libro/bio{m}_icfes.py", encoding="utf-8").read()
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
    """Lo que tiene que cuadrar antes de dibujar: claves del libro contra el docstring de bioN.py,
    claves del entrenamiento contra el docstring de bioN_icfes.py, y la estrategia de cada pregunta
    contra las cuatro de la misión. Devuelve la lista de diferencias."""
    malas = []
    for m in range(1, 7):
        doc = open(f"/home/claude/libro/bio{m}.py", encoding="utf-8").read()[:3000]
        k = {int(n): c for n, c in re.findall(r"(\d+)·([A-D])", doc)}
        if k != CLAVES[m]:
            malas.append(f"M{m}: CLAVES {CLAVES[m]} · bio{m}.py {k}")
        doc = open(f"/home/claude/libro/bio{m}_icfes.py", encoding="utf-8").read()[:4000]
        ki = dict(re.findall(r"Q([A-D])\s*·[^·\n]*·\s*([A-D])\b", doc))
        for j, q in enumerate("ABCD"):
            if ki.get(q) != BANCO[m][j]["clave"].strip():
                malas.append(f"M{m} P{j+1}: icfes.csv {BANCO[m][j]['clave']} · bio{m}_icfes.py {ki.get(q)}")
        for p, e, _, _ in TALLER[m] + INS_ICFES[m]:
            if e not in MISIONES[m]["estr"]:
                malas.append(f"M{m} · {p}: estrategia «{e}» no está en la misión")
        if len(TALLER[m]) != 10 or len(INS_ICFES[m]) != 4 or len(BANCO[m]) != 4:
            malas.append(f"M{m}: {len(TALLER[m])} del taller, {len(INS_ICFES[m])} y {len(BANCO[m])} ICFES")
    return malas


# ─────────────────────────── banco de dinámicas ───────────────────────────
# Isomorfas a la estrategia: lo que hace el cuerpo es el mismo movimiento que después hará la mente
# frente al dato. En Biología el movimiento casi siempre es SEGUIR (el producto por sus estaciones,
# el alelo por la familia, el efecto por la red) o COMPARAR (contra el control, columna por
# columna). La E1 abre la clase (8'); las otras tres van entre bloques del desarrollo guiado (6').
# Ninguna usa el caso de una pregunta que viene después: se entrena el movimiento, no la respuesta.
DINAMICAS = {
 1: [("La fábrica sin un obrero", 8,
      ["Seis estudiantes al frente con un cartel: NÚCLEO, RIBOSOMA, RETÍCULO, GOLGI, LISOSOMA y "
       "MITOCONDRIA; cada uno dice su oficio en una frase.",
       "El docente anuncia un síntoma de la célula: «se llena de basura», «se queda sin energía», «las "
       "proteínas salen sin empacar».",
       "El grupo señala qué organelo dejó de trabajar, y ese estudiante se sienta.",
       "Para que se quede sentado, alguien dice qué oficio faltó y por qué produce ese síntoma; si no, "
       "vuelve a pararse."],
      "Ir del síntoma al oficio y del oficio al organelo, no del nombre que suena. Es el movimiento de "
      "las preguntas 1 y 8, y de la primera del entrenamiento (los lisosomas que se rompen).",
      "Seis carteles"),
     ("La cadena de montaje", 6,
      ["Cinco estudiantes en fila son estaciones: NÚCLEO, RIBOSOMA, RETÍCULO, GOLGI y MEMBRANA.",
       "Una hoja —la proteína— pasa de mano en mano; cada estación le hace su marca: un doblez, una "
       "firma, un sello.",
       "El docente le pide en secreto a una estación que no haga su marca o que no pase la hoja.",
       "Al final, el grupo mira la hoja: por la marca que falta dice qué estación falló y qué pasa con "
       "todas las que vienen después."],
      "Seguir el producto estación por estación y ubicar dónde se rompió la cadena: si una falla, todo "
      "lo de después falla. Es el movimiento de las preguntas 4, 5, 9 y 10, y de la tercera del "
      "entrenamiento (el error al copiar el ADN).",
      "Una hoja por ronda · cinco carteles"),
     ("El pulso de los que no se movieron", 6,
      ["El salón se parte en dos: una mitad hace veinte sentadillas y la otra se queda sentada.",
       "Todos se toman el pulso durante quince segundos y lo anotan en el tablero, en dos columnas.",
       "El docente lanza una conclusión: «con las sentadillas el pulso llega a 30 latidos».",
       "El grupo la corrige con la columna de los que no se movieron: cuánto subió respecto a ellos, no "
       "respecto a cero."],
      "Medir el efecto como diferencia contra el grupo que no recibió el cambio. Es el movimiento de "
      "las preguntas 3, 6 y 7, y de la cuarta del entrenamiento (la caja sin insecticida).",
      "Reloj con segundero · tablero"),
     ("Del lado lleno al lado vacío", 6,
      ["Una línea de cinta en el piso es la membrana: de un lado se paran doce estudiantes y del otro, tres.",
       "El docente dice quién se mueve: «uno pasa al lado donde hay menos», «uno pasa al lado donde hay más».",
       "Pasar hacia donde hay menos es gratis; hacia donde hay más cuesta una ficha de energía.",
       "Antes de cada paso, el grupo dice dónde hay más, dónde hay menos y si el paso cuesta."],
      "Contar dónde hay más y dónde hay menos antes de decir hacia dónde va algo y si gasta energía. Es "
      "el movimiento de la pregunta 2 (la sal del fertilizante y el agua de la raíz) y de la segunda "
      "del entrenamiento (sacar Na⁺ de la célula).",
      "Cinta · fichas de papel")],
 2: [("El termostato humano", 8,
      ["Cuatro estudiantes en círculo: VARIABLE, SENSOR, CONTROL y EFECTOR. La VARIABLE de pie es lo "
       "normal; en puntas, alta; agachada, baja.",
       "El docente dice: «después del almuerzo sube la glucosa», y la VARIABLE se pone en puntas.",
       "El SENSOR toca al CONTROL y dice qué detectó; el CONTROL da la orden en voz alta; el EFECTOR hace "
       "lo que corrige; solo entonces la VARIABLE vuelve a su altura.",
       "En la segunda ronda el docente saca a uno: el grupo dice qué le pasa a la variable sin él."],
      "Recorrer el circuito completo —qué se desvía, quién lo detecta, qué orden se da y qué la corrige— "
      "y ver qué pasa si falta un eslabón. Es el movimiento de las preguntas 1, 3 y 9, y de la primera "
      "del entrenamiento (la pastilla que frena la orden).",
      "Cuatro carteles"),
     ("Párate si dice para qué", 6,
      ["El docente lee despacio un párrafo corto sobre un animal que el grupo no conoce: el del pez "
       "pulmonado, que está en la guía.",
       "Todos sentados; se paran solo cuando oyen una frase que dice PARA QUÉ sirve algo.",
       "Quien se paró repite la frase con las palabras exactas del texto; si la cambia por lo que ya "
       "sabía, se sienta.",
       "El grupo escribe en el tablero cada función tal como la dice el texto, sin adornos."],
      "Sacar la función de las palabras del texto, no de lo que uno ya cree saber. Es el movimiento de "
      "las preguntas 4, 5 y 6 (las ranas en estivación) y de la tercera del entrenamiento (el "
      "monóxido y la hemoglobina).",
      "El párrafo del pez pulmonado"),
     ("Columna por columna", 6,
      ["En el piso, una tabla de cinta: tres filas (TRES ANIMALES INVENTADOS) y dos columnas (AGUA QUE "
       "PIERDE y TEMPERATURA).",
       "Seis estudiantes reciben una tarjeta con un número y se paran en su casilla.",
       "El docente pregunta «¿quién pierde menos agua?»: los de esa columna se ordenan de menor a mayor.",
       "Antes de concluir, el grupo revisa la otra columna: ¿el mismo animal es el menor también ahí, o "
       "la conclusión sirve para una sola columna?"],
      "Comparar columna por columna, con el mismo criterio para todas las especies, antes de sacar una "
      "conclusión. Es el movimiento de las preguntas 7 y 8, y de la cuarta del entrenamiento "
      "(sedentario contra deportista).",
      "Cinta · seis tarjetas con números"),
     ("¿Hasta dónde alcanza?", 6,
      ["Dos estudiantes al frente son dos casos: «en el páramo respira más rápido» y «en la costa suda más».",
       "Cada equipo recibe una tarjeta con una explicación posible.",
       "Un integrante lleva la tarjeta y pone la mano en el hombro de cada caso que la explicación de "
       "verdad explica.",
       "El grupo revisa: si la pregunta pide los dos y la tarjeta toca uno, se queda corta; si dice algo "
       "que el caso no dice, se pasó."],
      "Medir hasta dónde llega una explicación: si cubre todo lo que se pregunta y no agrega lo que el "
      "caso no dice. Es el movimiento de las preguntas 2 y 10, y de la segunda del entrenamiento (el "
      "oxígeno que no entra al capilar).",
      "Tarjetas con explicaciones")],
 3: [("Arriba o abajo del control", 8,
      ["Una línea de cinta en el piso es el control: el cero de la comparación.",
       "Tres estudiantes son tres cosas medidas en un cultivo: ORGANISMOS DEL SUELO, LOMBRICES y HONGOS.",
       "El docente lee dos datos inventados por variable —el tratamiento y el control—; cada uno da un "
       "paso adelante si el tratamiento quedó arriba, atrás si quedó abajo, y se queda si es igual.",
       "Solo después el grupo dice la conclusión, y tiene que nombrar a los tres, no solo al que más avanzó."],
      "Leer cada dato contra el control, fila por fila, antes de escoger una conclusión. Es el "
      "movimiento de las preguntas 8 y 9, y de la tercera del entrenamiento (la raya de los "
      "2.100 kcal/kg).",
      "Cinta · los datos en el tablero"),
     ("La red de lana", 6,
      ["Siete estudiantes son seres de un estanque: ALGA, PLANTA ACUÁTICA, RENACUAJO, LIBÉLULA, PEZ, "
       "GARZA y BACTERIA.",
       "Con un ovillo de lana, el docente une a cada uno con el que se lo come o del que depende.",
       "El docente saca al PEZ: suelta la lana y se sienta.",
       "Cada uno que siente que su hilo se aflojó dice qué le pasa y a quién le pasa algo después; la "
       "BACTERIA cierra diciendo qué recibe de todos los que mueren."],
      "Seguir una perturbación hilo por hilo hasta quien no estaba conectado directamente, y cerrar el "
      "ciclo con los descomponedores. Es el movimiento de las preguntas 2, 5 y 6, y de la segunda del "
      "entrenamiento (las moléculas de un ser vivo que muere).",
      "Un ovillo de lana · siete tarjetas"),
     ("La duela más corta", 6,
      ["Cinco estudiantes son lo que una planta necesita: LUZ, AGUA, NUTRIENTES, OXÍGENO y TEMPERATURA.",
       "El docente dice cuánto hay de cada uno, y cada factor levanta los brazos a esa altura.",
       "Un sexto estudiante, el CRECIMIENTO, solo puede subir los brazos hasta la altura del factor más bajo.",
       "El docente sube a tope todos menos uno: el grupo comprueba que el crecimiento no cambia y nombra "
       "el factor que limita."],
      "Buscar el único factor que falta y que manda sobre todo lo demás, aunque lo otro sobre. Es el "
      "movimiento de las preguntas 1 y 4, y de la primera del entrenamiento (el oxígeno de un lago).",
      "Ninguno"),
     ("Cuatro rincones, un dato", 6,
      ["Cuatro rincones son cuatro decisiones para el aceite usado de la cocina del colegio: SIFÓN CON "
       "JABÓN, CANECA DE BASURA, ENTERRARLO y BOTELLA AL PUNTO DE RECOLECCIÓN.",
       "El docente lee un dato: «una capa delgada de aceite sobre el agua no deja pasar el oxígeno del aire».",
       "Cada estudiante camina al rincón de la decisión que usa ese dato.",
       "Para quedarse, dice el «porque» de su rincón con el dato, y algo que se podría comprobar."],
      "Escoger la decisión que se apoya en un dato ecológico comprobable, no la que suena responsable. "
      "Es el movimiento de las preguntas 3, 7 y 10, y de la cuarta del entrenamiento (el tanque poco "
      "profundo).",
      "Cuatro letreros")],
 4: [("¿Cabe en el laboratorio?", 8,
      ["Dos zonas en el salón: SE PUEDE PONER A PRUEBA y ASÍ COMO ESTÁ, NO.",
       "El docente lee afirmaciones sobre un invento: «este casco te hará más inteligente», «quienes usan "
       "el casco recuerdan más palabras que quienes no lo usan».",
       "Cada estudiante camina a la zona que cree.",
       "Para quedarse en SE PUEDE, dice qué dos grupos compararía y qué mediría con un número; si no "
       "puede, se cambia de zona."],
      "Reconocer una hipótesis que se puede poner a prueba: dos grupos, una variable medible, un "
      "resultado esperado. Es el movimiento de las preguntas 2, 5 y 8, y de la primera del "
      "entrenamiento (la gráfica que espera el investigador).",
      "Dos letreros"),
     ("Eslabones del yogur", 6,
      ["Cada equipo recibe seis tarjetas desordenadas: calentar la leche, dejarla entibiar, agregar las "
       "bacterias, mantenerla tibia, las bacterias convierten el azúcar en ácido, la leche se espesa.",
       "Seis integrantes se ponen en fila con una tarjeta cada uno, en el orden que creen.",
       "El primero dice su paso y toca el hombro del siguiente solo si su paso es la causa del que sigue.",
       "Donde no se puede decir «y por eso…», la cadena se cae: el equipo reordena."],
      "Armar el mecanismo de modo que cada eslabón cause el siguiente y ninguno falte. Es el "
      "movimiento de las preguntas 1, 4 y 10, y de la tercera del entrenamiento (el orden para hacer "
      "vino de manzana).",
      "Seis tarjetas por equipo"),
     ("Las piezas de la semilla", 6,
      ["Tres estudiantes son las piezas de una semilla de fríjol: CUBIERTA, RESERVA DE ALIMENTO y "
       "EMBRIÓN, con su función escrita al respaldo de la tarjeta.",
       "El docente cuenta una situación: «pasa tres meses en suelo seco», «germina bajo la tierra, sin luz».",
       "El grupo dice qué pieza trabaja en esa situación; esa pieza voltea su tarjeta y lee su función.",
       "El docente saca una pieza y el grupo dice qué deja de poder hacer la semilla sin ella."],
      "Atribuir cada función a la pieza que la cumple, no a la que suena más importante. Es el "
      "movimiento de las preguntas 6 y 7, y de la cuarta del entrenamiento (para qué le sirve la "
      "fotosíntesis a la planta).",
      "Tres tarjetas · una semilla remojada, si hay"),
     ("El juez de la evidencia", 6,
      ["Tres marcas en el piso: LO RESPALDA, NO LO DICE y LO CONTRADICE.",
       "El docente lee un resultado: «en 40 tomates rociados con un aerosol nuevo salieron menos hongos "
       "que en 40 sin rociar, durante dos semanas».",
       "Lee afirmaciones una por una: «evita los hongos en todas las frutas», «redujo los hongos en esos "
       "tomates», «hace daño a quien se come el tomate».",
       "Cada estudiante camina a la marca que cree y, para quedarse, señala la palabra del resultado que "
       "lo decide."],
      "Separar lo que la evidencia respalda de lo que se le agrega: para quién se probó, cuánto y en qué "
      "condiciones. Es el movimiento de las preguntas 3 y 9, y de la segunda del entrenamiento (la "
      "hipótesis frente a los estudios).",
      "Tres letreros en el piso")],
 5: [("Las dos fichas de cada uno", 8,
      ["Cada estudiante recibe dos tarjetas, su par de alelos: casi todos tienen A y A; cuatro tienen A y "
       "a, sin que los demás sepan quiénes.",
       "Se forman parejas; cada uno pone boca abajo UNA de sus tarjetas, al azar: la que recibe el hijo.",
       "Se voltean: el hijo que sale a y a tiene la enfermedad, y el grupo cuenta cuántos salieron así.",
       "Se repite solo con los cuatro portadores emparejados entre sí, como parientes: el grupo compara "
       "cuántos a y a salen ahora."],
      "Seguir cada alelo de los padres al hijo y ver que dos portadores sanos pueden tener un hijo "
      "enfermo, y que entre parientes eso pasa más. Es el movimiento de las preguntas 1, 6 y 9, y de "
      "la primera del entrenamiento (de dónde sale la diversidad).",
      "Dos tarjetas por estudiante (A y a)"),
     ("La instrucción cambiada", 6,
      ["Un estudiante tiene una tarjeta con cinco pasos para dibujar una figura: es el ADN.",
       "Se la dicta en voz baja a un segundo, que la copia (el ARN) y se la lleva a un tercero, que "
       "dibuja en el tablero (lo que se ve).",
       "En la segunda ronda, el docente cambia en secreto una sola palabra de la tarjeta: «círculo» por "
       "«cuadrado».",
       "El grupo compara los dibujos: qué cambió en la instrucción y qué en lo que se ve."],
      "Ir del cambio en la instrucción al cambio en lo que se ve, paso por paso, sin saltarse el "
      "intermedio. Es el movimiento de las preguntas 2, 5 y 7, y de la tercera del entrenamiento "
      "(los mosquitos resistentes).",
      "Una tarjeta con la instrucción · tablero"),
     ("¿Con quién lo comparo?", 6,
      ["El docente pregunta: «¿repetir en voz alta ayuda a recordar?», y pide diez voluntarios.",
       "Los diez leen en voz alta diez palabras por treinta segundos y anotan las que recuerdan.",
       "El docente pregunta: «¿repetir en voz alta ayudó?». El grupo tiene que decir qué falta para saberlo.",
       "Se repite con dos grupos —en voz alta y en silencio— iguales en todo lo demás, y se comparan los "
       "promedios."],
      "Pedir el grupo de comparación y la variable que se mide antes de aceptar que una prueba responde "
      "la pregunta. Es el movimiento de las preguntas 3 y 8, y de la segunda del entrenamiento (los "
      "monos sin grupo control).",
      "Dos listas de diez palabras"),
     ("La balanza y la palabra que exagera", 6,
      ["Al frente, un estudiante con los brazos abiertos es una balanza: una mano es LO QUE GANA y la "
       "otra LO QUE ARRIESGA.",
       "El docente anuncia una tecnología: «un arroz editado para crecer con menos agua».",
       "Los equipos dictan una cosa para cada mano, y la balanza baja la mano que el grupo decide que pesa más.",
       "El docente lee tres frases de propaganda; el grupo se para cuando oye una palabra que exagera "
       "—«siempre», «garantiza», «por completo»— y dice qué dato faltaría."],
      "Valorar una tecnología con beneficio y riesgo a la vez, y desconfiar de la afirmación absoluta "
      "que ningún dato sostiene. Es el movimiento de las preguntas 4 y 10, y de la cuarta del "
      "entrenamiento (la cartelera que sí comunica el resultado).",
      "Tres frases de propaganda escritas por el docente")],
 6: [("Dos relojes", 8,
      ["Dos zonas en el salón: EN LA VIDA DE UNO (el ambiente) y EN MUCHAS GENERACIONES (la herencia).",
       "El docente lee cambios: «una persona se broncea en vacaciones», «los perros pequeños salieron de "
       "cruzar a los más pequeños por siglos», «un perro de finca corre más que uno de apartamento».",
       "Cada estudiante camina a la zona que cree.",
       "Para quedarse, responde: ¿eso pasa a los hijos? Si no puede decirlo, se cambia de zona."],
      "Separar lo que cambia en la vida de un individuo por el ambiente de lo que cambia en una "
      "población por herencia y selección. Es el movimiento de las preguntas 1, 2 y 3, y de la primera "
      "del entrenamiento (los ciclos de cuatro especies).",
      "Dos letreros"),
     ("Hasta donde llega la tabla", 6,
      ["El docente escribe una tabla: tres canchas del colegio con 2, 5 y 8 horas de sol, y pasto de 5, "
       "9 y 12 centímetros.",
       "Lee conclusiones: «la cancha con más sol tiene el pasto más alto», «el sol hace crecer el pasto en "
       "todas las ciudades», «el pasto de la cancha 2 es de otra especie».",
       "Cada estudiante se para a un lado de una línea: LO DEJA CONCLUIR o NO LO DICE.",
       "Para quedarse en el primer lado, dice qué filas y columnas usa; si usa otra, se cambia."],
      "Aceptar solo la conclusión que usa las filas y columnas que de verdad están en los datos, y todas "
      "las que pide el enunciado. Es el movimiento de las preguntas 7 y 10, y de la segunda del "
      "entrenamiento (el orden para vender las frutas).",
      "Tablero · cinta"),
     ("El dominó del cultivo", 6,
      ["Seis estudiantes en fila con un cartel: PLAGUICIDA, ABEJAS, FLORES POLINIZADAS, FRUTOS, AVES QUE "
       "LOS COMEN y SEMILLAS LLEVADAS LEJOS.",
       "El primero le toca el hombro al segundo, que dice qué le pasa con una frase: «las abejas mueren».",
       "Cada uno se agacha solo si puede decir por qué lo de atrás lo afecta; si no puede, se queda de "
       "pie y la cadena se corta ahí.",
       "El grupo nombra el último que se agachó: es el efecto más lejano que se puede afirmar."],
      "Seguir el efecto de quitar una pieza, eslabón por eslabón, hasta el último que de verdad se "
      "puede afirmar. Es el movimiento de las preguntas 5, 6 y 9, y de la tercera del entrenamiento "
      "(por qué el agua estancada importa).",
      "Seis carteles"),
     ("El rasgo y su problema", 6,
      ["Cuatro carteles en la pared son problemas de un ambiente: FRÍO DE NOCHE, SOL FUERTE, POCA AGUA y "
       "DEPREDADORES.",
       "Cada estudiante recibe un rasgo: «pelo grueso», «hojas pequeñas y cerosas», «espinas», «color "
       "del suelo», «raíces profundas».",
       "Camina al cartel del problema que ese rasgo resuelve.",
       "Para quedarse, dice cómo lo resuelve —qué evita o qué consigue— en una frase."],
      "Unir cada rasgo con el problema del ambiente que resuelve, y decir cómo. Es el movimiento de las "
      "preguntas 4 y 8, y de la cuarta del entrenamiento (para qué llevar azúcar a la raíz).",
      "Cuatro carteles · tarjetas de rasgos")],
}

# El párrafo de la dinámica «Párate si dice para qué» (Misión 2, E2). Original, para la guía.
PEZ_PULMONADO = (
    "El pez pulmonado africano vive en charcas que se secan. Cuando el agua baja, se entierra en el "
    "barro y fabrica a su alrededor un capullo de moco que se endurece. Ahí adentro respira aire por "
    "una abertura pequeña, y su corazón late mucho más despacio. El capullo sirve para que el cuerpo no "
    "pierda agua, y el latido lento le permite gastar muy poca energía durante meses. Cuando vuelven "
    "las lluvias, el barro se ablanda y el pez sale nadando.")

RETOS = {
 1: ("La fábrica que se detuvo", 20,
     "Cada equipo de tres recibe un caso: una célula que fabrica una hormona para exportarla ya no la "
     "saca; el laboratorio encontró la hormona sin empacar en el citoplasma, y la célula tiene energía "
     "normal. En doce minutos dibujan la ruta de la proteína, marcan con una X la estación que falló y "
     "escriben qué dato del caso la delata, descartan los organelos que el caso deja por fuera y dicen "
     "con qué célula la compararían para estar seguros. Exponen señalando el dato de cada parte."),
 2: ("El cuerpo después de la carrera", 20,
     "Cada equipo recibe un caso: una deportista corre una hora al mediodía; al final suda mucho, tiene "
     "sed, orina poco y oscuro, y media hora después su temperatura volvió a 37 °C. En doce minutos "
     "dibujan los dos circuitos que trabajaron —el de la temperatura y el del agua— con lo que se "
     "desvió, quién lo detectó, qué orden se dio y qué lo corrigió, y señalan el dato del caso que "
     "prueba cada eslabón. Cada integrante cierra escribiendo qué pasaría si la orden de guardar agua "
     "no llegara."),
 3: ("La quebrada del colegio", 20,
     "Cada equipo recibe la tabla de una quebrada en tres tramos: antes del pueblo (oxígeno disuelto "
     "8 mg/L, 14 especies de insectos acuáticos, pocas algas), junto al desagüe (3 mg/L, 4 especies, "
     "muchas algas) y dos kilómetros abajo (6 mg/L, 9 especies, algas moderadas). En doce minutos "
     "comparan cada tramo contra el de antes del pueblo, nombran el factor que limita la vida junto "
     "al desagüe, dibujan dos eslabones de quién depende de quién y proponen una decisión con el dato "
     "que la respalda. Cada integrante defiende una de las cuatro partes."),
 4: ("La pulsera que te hace mover", 20,
     "Cada equipo recibe un invento: una pulsera que vibra cuando el estudiante lleva cuarenta minutos "
     "sentado, para que se pare y camine. En doce minutos escriben una hipótesis que se pueda poner a "
     "prueba (qué dos grupos, qué se mide), arman el mecanismo eslabón por eslabón desde la vibración "
     "hasta el efecto que promete, dicen para qué sirve cada pieza y escriben una afirmación que su "
     "experimento respaldaría y otra que no. Cada integrante defiende una de las cuatro partes."),
 5: ("El criadero de la camada", 20,
     "Cada equipo recibe un caso: un criadero quiere fijar una raza nueva y cruza entre sí a los hermanos "
     "de una misma camada; los dos perros fundadores eran sanos, pero cada uno llevaba una copia recesiva "
     "de una enfermedad. En doce minutos dibujan el árbol de tres generaciones, hacen el cuadro de "
     "Punnett de un cruce entre hermanos portadores, proponen cómo comprobar si las enfermedades "
     "aumentan (contra qué grupo comparan) y escriben qué gana y qué arriesga el criadero. Cada uno "
     "cierra: «Mezclar razas no es lo mismo que ___, porque ___»."),
 6: ("Las mariposas del parque", 20,
     "Cada equipo trabaja la actividad de aula del libro: en un parque conviven mariposas de alas claras "
     "y de alas oscuras, y los muros se oscurecen por la contaminación. El docente da dos datos: de cada "
     "100 mariposas, 80 eran claras al principio y 30 veinte años después. En doce minutos separan qué "
     "cambió en la vida de cada mariposa y qué en la población, escriben solo la conclusión que esos "
     "datos permiten, encadenan qué le pasa a un pájaro que las come y dicen para qué le sirve el color. "
     "Cada uno cierra: «Las oscuras aumentaron porque ___, y eso no quiere decir que ___»."),
}


# ─────────────────────────────── hojas ───────────────────────────────
OUTP = OUT + "plan_bio_"


def _cajas_hilo(b, y):
    cajas = [("LIBRO", "tiene la pregunta", GRAY), ("CUADERNO", "tiene el andamiaje para resolverla", BIO),
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
    y = cabecera(b, "Biología", "Planeador del área · las ocho clases",
                 derecha="8", dsub="clases de 120 min", campos=True)
    y = seccion(b, y, "Para qué existe este documento")
    y = parrafo_j(b, M, y,
        "La calidad de la clase no puede depender de qué profesor llegue ese sábado. Por eso el "
        "método de EDUCATE no vive en el profesor: vive en el cuaderno del estudiante. Este "
        "planeador no te pide saber biología de memoria; te dice qué hacer con el libro y con el "
        "cuaderno en cada uno de los 120 minutos, y dónde termina lo fijo y empieza tu aporte.",
        CW, 26) + 24
    y = _cajas_hilo(b, y) + 30
    y = nota(b, M, y, CW,
        "Casi ninguna pregunta de Biología se resuelve recordando un nombre. Se resuelve preguntando "
        "qué cambió, qué se midió y contra qué se compara. Es el instrumento que el estudiante "
        f"encuentra en la portada del área, en la página {PORTADA}. Un estudiante que acierta con el "
        "instrumento vacío no aprendió la estrategia: adivinó, y en la prueba real no va a tener a "
        "quién preguntarle.",
        BIO, BIO_BG, BIO_LN, "El instrumento de pensamiento del área: el dato y su comparación", 25) + 30
    y = seccion(b, y, "El área en números")
    na = sum(len(v) for v in AVISOS.values())
    cif = [(str(AREA_PAGS[1] - AREA_PAGS[0] + 1), "páginas del cuaderno\\ncon portada y simulacro", BIO), ("60", "preguntas del libro\\ncon su instrumento", BIO),
           ("24", "preguntas tipo\\nSaber 11", "#1F4E8C"), (str(len(SELLOS)), "sellos «aquí entra\\nel profe»", ORO),
           (str(na), "avisos del libro\\nantes de entrar", ROJO)]
    an2 = (CW - 4 * 18) / 5
    for i, (v, l, c) in enumerate(cif):
        x = M + i * (an2 + 18)
        b.append(rect(x, y, an2, 140, "white", r=16, stroke=BIO_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, 112, c, r=3))
        b.append(T(x + 38, y + 64, [v], 50, c, weight="700"))
        for j, ln in enumerate(l.split("\\n")):
            b.append(T(x + 38, y + 98 + j * 26, [ln], 20, GRAY))
    y += 140 + 30
    y = seccion(b, y, "Las tres competencias que evalúa la prueba de Ciencias Naturales")
    comp = [("UC", "Uso comprensivo del conocimiento científico", "usar conceptos y modelos de la "
             "biología para entender una situación"),
            ("EF", "Explicación de fenómenos", "construir la explicación de lo que pasa, eslabón por "
             "eslabón, y juzgar si una explicación alcanza"),
            ("IN", "Indagación", "plantear preguntas que se puedan poner a prueba, comparar contra un "
             "control y sacar solo la conclusión que los datos permiten")]
    an3 = (CW - 2 * 18) / 3
    alt3 = 52 + max(len(wrap_px(t + ": " + d, 22, an3 - 70)) for _, t, d in comp) * 31 + 20
    for i, (cod, t, d) in enumerate(comp):
        x = M + i * (an3 + 18)
        b.append(rect(x, y, an3, alt3, BIO_BG, r=16, stroke=BIO_LN, sw=2))
        b.append(rect(x + 14, y + 14, 5, alt3 - 28, BIO, r=3))
        b.append(T(x + 40, y + 44, [cod], 26, BIO, weight="700"))
        parrafo_j(b, x + 40, y + 54, t + ": " + d, an3 - 70, 22, INK, lh=31)
    y += alt3 + 30
    y = nota(b, M, y, CW,
        "Dos preguntas del entrenamiento tratan del ciclo menstrual y de las pastillas anticonceptivas "
        "(misiones 2 y 6), y la misión 5 habla de enfermedades hereditarias en las familias. Se trabajan "
        "como biología: con el vocabulario correcto, sin bromas y sin pedir casos personales. Si un "
        "estudiante cuenta algo de su familia, se le agradece y no se discute en público. Y cuatro claves "
        "del libro son discutibles (misión 4, preguntas 7 y 9; misión 6, preguntas 2 y 10): están en la "
        "hoja de su clase.",
        ROJO, ROJO_BG, ROJO_LN, "Antes de empezar el área", 23) + 28
    y = nota(b, M, y, CW,
        "No necesitas ser biólogo. La segunda hoja de cada clase trae los cuatro conceptos que tienes "
        "que poder explicar en dos minutos, y el cuaderno marca con un sello «Alto · aquí entra el "
        "profe» las siete preguntas donde el estudiante no puede seguir sin ti. Lo demás lo resuelve el "
        "instrumento: qué cambió, qué se midió, contra qué se compara.",
        VERDE, VERDE_BG, VERDE_LN, "Si Biología no es tu fuerte", 23) + 28
    y = seccion(b, y, "Lo que la coordinación revisa, sin haber entrado a la clase",
        "Tres cuadernos al azar del grupo. No se mira si la respuesta está buena: se mira si el "
        "instrumento está lleno. Marca tú mismo esta lista al terminar el sábado.")
    rev = ["El instrumento de pensamiento está lleno en las diez preguntas, acertadas o no.",
           "«Mi primera idea, antes de hacer nada» tiene algo escrito en todas las preguntas.",
           "Los sellos «Alto · aquí entra el profe» tienen escrito «lo que explicó, en mis palabras».",
           "Las dos caritas de la clase están marcadas y la clase está anotada en la portada del área."]
    b.append(rect(M, y, CW, 34 + len(rev) * 50, "white", r=18, stroke=BIO_LN, sw=2))
    b.append(rect(M + 14, y + 16, 5, 2 + len(rev) * 50, BIO, r=3))
    yy = y + 34
    for r_ in rev:
        b.append(checkbox(M + 44, yy - 14, 13, BIO))
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
                                                "PARA EL PROFE", "ENTRENAMIENTO"])), 54)
    y += 2
    for n, (mis, tit, sub) in enumerate(CLASES, 1):
        alto = 96
        bg = "white" if mis else ORO_BG
        ln = BIO_LN if mis else ORO_LN
        c = BIO if mis else ORO
        b.append(rect(M, y, CW, alto, bg, r=14, stroke=ln, sw=2))
        b.append(rect(M + 12, y + 12, 5, alto - 24, c, r=3))
        b.append(T(colx[0] + 44, y + 62, [str(n)], 42, c, weight="700", anchor="middle"))
        b.append(T(colx[1] + 20, y + 44, [tit], 24, INK, weight="700"))
        b.append(T(colx[1] + 20, y + 74, [sub], 20, GRAY, style="italic"))
        if mis:
            d = MISIONES[mis]
            cod, de = d["competencia"].split(" · ")
            b.append(T(colx[2] + 20, y + 44, [cod], 23, BIO, weight="700"))
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
        b.append(rect(x, yy0, an, alto, BIO_BG, r=16, stroke=BIO_LN, sw=2))
        b.append(rect(x + 14, yy0 + 14, 5, alto - 28, BIO, r=3))
        b.append(T(x + 40, yy0 + 44, [f"Misión {m} · {d['comp']}"], 22, BIO, weight="700"))
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
        b.append(rect(x, y, an, alt, "white", r=16, stroke=BIO_LN, sw=2))
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
            "están en la hoja siguiente, en «Si Biología no es tu fuerte».",
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
        b.append(rect(M, y, CW, h, BIO_BG if p <= 2 else "white", r=10, stroke=BIO_LN, sw=1.6))
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
        f"Observación proyectada, sin contexto: «{caso}» Qué cambió, qué se midió, contra qué se "
        f"compara. Dinámica E1 «{din[0][0]}» ({din[0][1]}'). Pista para el cierre del momento: {pista}.",
        f"Pregunta modelo: la 1 del libro (página {PAG_LIBRO[mis][0]}), a la vista todo el momento. "
        f"Manos alzadas antes de releer. La pregunta del momento: {PROBLEMATIZADORA[mis]} Se abre la "
        f"página {t_pags[0]} solo en «mi primera idea».",
        f"1-2 en pantalla (página {t_pags[0]}, «{ins.get(1, '—')}» y «{ins.get(2, '—')}»); 3-4, 5-6, "
        f"7-8 y 9-10 en las páginas {t_pags[1]}, {t_pags[2]}, {t_pags[3]} y {t_pags[4]}. Entre "
        f"bloques, las dinámicas E2, E3 y E4."
        + (f" Sello en {'la pregunta' if ',' not in sel else 'las preguntas'} {sel}." if sel else ""),
        f"Reto del corte: «{RETOS[mis][0]}». Equipos de tres; cada uno registra en SU tarjeta. La "
        f"defensa nombra el dato, el grupo de comparación o el eslabón.",
        f"Entrenamiento, páginas {i_pags[0]} y {i_pags[1]}. Cuatro preguntas tipo Saber 11, en "
        f"silencio y con reloj.",
        f"Solo las falladas, con el dato o el eslabón que las resuelve. «Palabras que me frenaron», "
        f"«lo que me llevo», carita de salida y la clase {mis} en la portada del área.",
    ]
    y = seccion(b, y, "El sábado, minuto a minuto",
        "Las seis fases con el contenido de este momento puesto encima.")
    reloj = 0
    for (nom, mins, c, *_), txt in zip(FASES, concreto):
        lin = wrap_px(txt, 21, CW - 440)
        h = max(70, 24 + len(lin) * 29)
        b.append(rect(M, y, CW, h, "white", r=14, stroke=BIO_LN, sw=1.8))
        b.append(rect(M + 12, y + 12, 5, h - 24, c, r=3))
        b.append(T(M + 40, y + h / 2 - 2, [f"{reloj:02d}'–{reloj+mins:02d}'"], 22, c, weight="700"))
        b.append(T(M + 40, y + h / 2 + 26, [nom], 19, GRAY))
        parrafo_j(b, M + 400, y + (h - len(lin) * 29) / 2 - 5, txt, CW - 440, 21, INK, lh=29)
        reloj += mins
        y += h + 6
    y += 20
    y = seccion(b, y, "Si Biología no es tu fuerte",
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
        b.append(rect(M, y, CW, h, "white", r=12, stroke=BIO_LN, sw=1.8))
        b.append(rect(M + 10, y + 10, 4, h - 20, cc, r=2))
        b.append(T(M + 36, y + h / 2 - 3, [f"P{x4}"], 21, cc, weight="700"))
        b.append(T(M + 36, y + h / 2 + 20, [f"pág. {i_pags[0] if x4 <= 2 else i_pags[1]}"], 16, GRAY))
        b.append(T(M + 150, y + h / 2 + 8, [f"E{i_est+1} · {comp_icfes(mis, x4)}"], 18, cc, weight="700"))
        parrafo_j(b, M + 290, y + (h - len(l_c) * 28) / 2 - 4, ctx_, 620, 20, INK, weight="700", lh=28)
        parrafo_j(b, M + 940, y + (h - len(l_i) * 28) / 2 - 4, ins_, 640, 19, GRAY, style="italic", lh=28)
        cl = fila.get("clave", "").strip()
        b.append(rect(W - M - 96, y + h / 2 - 22, 64, 44, BIO_BG, r=10, stroke=BIO, sw=2))
        b.append(T(W - M - 64, y + h / 2 + 10, [cl or "—"], 26, BIO, weight="700", anchor="middle"))
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
    """Clases 7 y 8 · el simulacro de EDUCATE y su socialización en el cuaderno (C7 y C8)."""
    b = svg_open()
    y = cabecera(b, "Clases 7 y 8", "El simulacro de EDUCATE y su socialización en el cuaderno",
                 derecha=str(C8["preguntas_cuaderno"]), dsub="preguntas caben en el cuaderno")
    PS.hoja(b, y, C7, C8, BIO, BIO_BG, BIO_LN, seccion, nota)
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
           ("Las claves que el grupo discutió", "M4 P7 y P9, M6 P2 y P10: van a la editorial"),
           ("Los avisos nuevos que encuentres", "la lista se hizo resolviendo, y seguro falta alguno")]
    for t, s_ in dev:
        b.append(rect(M, y, CW, 64, "white", r=14, stroke=BIO_LN, sw=2))
        b.append(rect(M + 14, y + 12, 5, 40, ORO, r=3))
        b.append(checkbox(M + 42, y + 19, 13, BIO))
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


PDF = "/home/user/educate-saber11/entregables/EDUCATE_Planeador_Biologia.pdf"

if __name__ == "__main__":
    import sys
    import render
    malas = verificar()
    if malas:
        raise SystemExit("No cuadra:\n  " + "\n  ".join(malas))
    hojas = build()
    print(len(hojas), "hojas del planeador de Biología")
    if "--pdf" in sys.argv:
        render.unir(hojas, PDF)
        n, sin = render.verifica(PDF, "PLANEADOR")
        print(f"{PDF}: {n} páginas · sin pie: {sin or 'ninguna'}")
