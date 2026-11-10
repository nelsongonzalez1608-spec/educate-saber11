# -*- coding: utf-8 -*-
"""Datos del informe de hallazgos para la editorial (versión del 10 nov 2026).

Cada fila sale de tablero/hallazgos.csv (columna n) y se redactó de nuevo para la editorial:
tono formal, sin decisiones internas de EDUCATE. La genera libro/informe_editorial.py.

H(n, area, mision, preguntas, pagina, severidad, que_pasa, propuesta, cuaderno)
  severidad : Alta · Media · Baja · Atención · Considerar (contenido de actualidad, sin severidad)
  cuaderno  : "C" Corrección EDUCATE impresa en la tarjeta · "A" advertido en el cuaderno
              (recuadro, sello o instrumento) · "G" advertido al docente en el planeador y la guía
              · "" sin intervención
"""

H = []


def h(n, area, mision, preg, pag, sev, q, p, c=""):
    H.append(dict(n=n, area=area, mision=mision, preg=preg, pag=pag, sev=sev, q=q, p=p, c=c))


# ───────────────────────────── MATEMÁTICAS ─────────────────────────────
h(2, "MAT", 1, "Pregunta 5", "272", "Alta",
  "Las opciones A y B enuncian la misma justificación con otras palabras: la A da la cuenta "
  "(C(7) = 2.000 × 7 + 15.000 = 29.000) y la B la dice en palabras (costo fijo más siete pagos de "
  "2.000). Las dos son correctas.",
  "Reescribir una de las dos para que contenga un error de procedimiento, de modo que quede una sola "
  "respuesta correcta.", "A")
h(3, "MAT", 2, "Pregunta 1", "281", "Alta",
  "El enunciado pide la semana siguiente a la del máximo («programar un descanso justo después de la "
  "semana en la que se alcanza la mayor distancia»). Con D(t) = −5t² + 40t + 120 el máximo está en "
  "t = 4 (200 km) y la semana siguiente es la 5, con 195 km: ninguna opción lo dice. La clave A "
  "(«Semana 4, con 200 km») corresponde a la semana del máximo, y la B pone la semana 5 con 220 km, "
  "valor que no sale del modelo.",
  "Ajustar el enunciado para que pida la semana del máximo, o cambiar la opción correcta por "
  "«Semana 5, con 195 km».", "A")
h(1, "MAT", 3, "Pregunta 10", "295", "Alta",
  "La figura tiene 7 casillas vacías y la opción correcta afirma que hay 14. La conclusión («no es "
  "posible») sigue siendo cierta, pero la razón que da la clave no coincide con la figura.",
  "Corregir la cifra de la opción correcta (7 casillas) o ajustar la figura.", "A")
h(4, "MAT", 5, "Pregunta 9", "318", "Alta",
  "El enunciado dice 7 % de espectadores nuevos y la captura de pantalla dice 67 %. La clave sale de "
  "la captura (0,67 × 4.100 ≈ 2.747); con el 7 % del texto ninguna opción cuadra.",
  "Corregir el enunciado a 67 %.", "A")
h(8, "MAT", 6, "Pregunta 2", "325", "Alta",
  "La opción C trae la expresión correcta, (4 sobre 3)·(0,85)³·(0,15) + (0,85)⁴, pero el valor impreso "
  "es «≈ 0,833». La cuenta da ≈ 0,890 (0,368 + 0,522): el estudiante que calcula bien no encuentra su "
  "resultado entre las opciones.",
  "Corregir el valor de la opción C a ≈ 0,890.", "G")
h(7, "MAT", 4, "Pregunta 1", "303", "Media",
  "Dos opciones llegan al mismo número y las dos son matemáticamente correctas: la C también alcanza "
  "el resultado; la D es el procedimiento con menos pasos.",
  "Si la pregunta busca el procedimiento más eficiente, decirlo en el enunciado; si no, introducir un "
  "error en la C.", "G")
h(9, "MAT", 6, "Pregunta 10", "328", "Media",
  "Dos opciones son ciertas a la vez: una descarta al analista y la otra respalda al experto. La C "
  "gana porque valora las dos posturas, pero la B también es verdadera.",
  "Ajustar la B para que deje de ser verdadera, o precisar en el enunciado que se pide valorar las "
  "dos posturas.", "G")
h(5, "MAT", 3, "Pregunta 2", "293", "Media",
  "La cuarta opción está rotulada «A.» en lugar de «D.». Confunde al marcar la hoja de respuestas.",
  "Corregir el rótulo.", "G")
h(6, "MAT", 3, "Pregunta 8", "295", "Baja",
  "La opción correcta dice que «se multiplican los volúmenes de 32 cubos»; lo que se quiere decir es "
  "que el volumen de un cubo se multiplica por 32.",
  "Reescribir: «se multiplica por 32 el volumen de un cubo».", "G")
h(341, "MAT", 6, "Pregunta 3", "326", "Atención",
  "El primer investigador calcula (800 + 600) ÷ 2.000 = 0,7 para «al menos una vez por semana», y la "
  "cuenta es correcta. La clave D le da la razón y pide nombrar con precisión el evento; la A también "
  "le da la razón con un argumento válido.",
  "Precisar la A o el enunciado para que una sola opción sea la mejor.", "G")

# ───────────────────────────── LECTURA CRÍTICA ─────────────────────────────
h(11, "LC", 3, "Pregunta 10", "35", "Media",
  "La opción D parafrasea casi textualmente la frase final del texto y la A emite el juicio que el "
  "enunciado pide como implícito: hay dos opciones defendibles. Además, B y D empiezan en infinitivo "
  "y no concuerdan con el enunciado.",
  "Definir la respuesta esperada (lo implícito), reescribir la D para que no sea una paráfrasis de lo "
  "explícito y ajustar la concordancia de B y D.")
h(14, "LC", 4, "Pregunta 10", "44", "Media",
  "El enunciado pregunta por el efecto que tiene insistir en el cambio personal, pero las cuatro "
  "opciones describen lo que hace el texto. Leída al pie de la letra, ninguna opción responde lo que "
  "se pregunta.",
  "Reformular el enunciado («¿qué hace el texto al insistir…?») o las opciones, para que pregunta y "
  "respuestas hablen de lo mismo.")
h(17, "LC", 5, "Preguntas 4 y 5", "52 y 53", "Media",
  "Las dos preguntas tratan la misma contradicción de la caricatura y sus respuestas esperadas son "
  "casi intercambiables: una habla de la retórica del decreto y la otra del encierro que siguió. El "
  "estudiante puede marcar la de la otra pregunta y perder el punto por un matiz.",
  "Diferenciar el foco de las dos preguntas o reemplazar una de ellas.")
h(18, "LC", 5, "Pregunta 8", "54", "Media",
  "La opción A dice que la cita demuestra que el proceso «carece de parcialidad». Carecer de "
  "parcialidad es ser imparcial: lo contrario de lo que el texto sostiene. La opción invierte su "
  "propio sentido.",
  "Revisar la redacción (por ejemplo, «carece de imparcialidad», si es lo que se quiso decir).")
h(24, "LC", 0, "Reparto de claves del área", "—", "Media",
  "En la Misión 6 seis de las diez claves son A y ninguna es B; en la Misión 5 hay cinco A y ninguna "
  "D; en la Misión 3, cinco B. Un estudiante que lo note puede marcar la letra dominante y obtener la "
  "mitad del puntaje sin leer.",
  "Redistribuir la posición de las opciones correctas en las misiones 3, 5 y 6.")
h(27, "LC", 6, "Pregunta 10", "64", "Media",
  "Las cuatro opciones parafrasean la misma lección con distintos acentos: la A usa las palabras del "
  "texto («prisa», «accesorio»), pero la C también se sostiene. Además, el enunciado dice «el "
  "principio» donde quiere decir «el principito».",
  "Ajustar la C para que deje de ser defendible y corregir la errata del enunciado.")
h(10, "LC", 2, "Pregunta 5", "24", "Atención",
  "Dos opciones afirman que el gráfico contradice la escena; una de ellas agrega una mayoría que el "
  "dibujo no muestra.",
  "Verificar que solo una opción se sostenga con la imagen.")
h(12, "LC", 3, "Preguntas 4 y 5", "34", "Atención",
  "La 4 pregunta por la valoración sobre los que miran y la 5 por lo que sugiere «fascinación "
  "morbosa»: las respuestas esperadas dicen casi lo mismo.",
  "Diferenciar las dos preguntas.")
h(19, "LC", 5, "Pregunta 10", "54", "Atención",
  "La opción A atiende al título y la D al relato completo: las dos son valoraciones correctas del "
  "sesgo del texto.",
  "Precisar en el enunciado si se pregunta por el título o por el texto completo.")
h(25, "LC", 6, "Preguntas 1 y 3", "62", "Atención",
  "Las dos preguntan qué le hace la fotografía a la memoria; la respuesta de la 1 serviría para la 3.",
  "Diferenciar las dos preguntas.")
h(26, "LC", 6, "Preguntas 4 y 5", "62 y 63", "Atención",
  "Las dos trabajan la ironía del mismo post y la respuesta de una describe lo que la otra pide.",
  "Diferenciar las dos preguntas.")
h(20, "LC", 5, "Texto de las preguntas 8 a 10", "54", "Considerar",
  "El texto es una columna de opinión sobre un expresidente colombiano, y el libro la usa para "
  "entrenar la detección de sesgo. Pedagógicamente es pertinente.",
  "Dato para que la editorial lo considere: un texto de opinión sobre una figura política de la "
  "actualidad puede leerse como una toma de posición del material. Un texto equivalente sobre otro "
  "tema entrenaría la misma habilidad.")

# ───────────────────────────── SOCIALES Y CIUDADANAS ─────────────────────────────
h(30, "SOC", 2, "Pregunta 6, opción D", "348", "Media",
  "La opción D afirma que el Estado de Conmoción Interior «faculta al Estado para suspender "
  "temporalmente los derechos humanos». La Constitución (artículo 214, numeral 2) dice lo contrario: "
  "no podrán suspenderse los derechos humanos ni las libertades fundamentales. Aunque es un "
  "distractor, la afirmación puede quedarse como dato en el estudiante.",
  "Reformular el distractor para que su error no sea una afirmación constitucional falsa que se fije "
  "como dato, o aclararlo en la retroalimentación.")
h(31, "SOC", 2, "Fuentes de las preguntas 2, 4 y 5", "347 y 348", "Baja",
  "Las tres URL de las fuentes traen pegado el parámetro «?utm_source=chatgpt.com» (detalle en la "
  "sección «Indicios de contenido generado automáticamente»).",
  "Limpiar las URL y verificar cada fuente en el medio original.")
h(46, "SOC", 3, "Página de apertura", "358", "Media",
  "El recuadro «Artículo de opinión» aparece vacío: es un marco sin texto. Ninguna pregunta depende de "
  "él, pero el estudiante no encuentra el artículo que el título anuncia.",
  "Completar el recuadro o retirarlo.")
h(47, "SOC", 3, "Reparto de claves", "359 a 361", "Media",
  "Claves 1·A 2·C 3·D 4·A 5·A 6·A 7·C 8·D 9·A 10·C: la A concentra la mitad (5 de 10) y la B no "
  "aparece. Un estudiante que marque A en todas obtiene 5 de 10.",
  "Redistribuir la posición de las opciones correctas.")
h(51, "SOC", 3, "Pregunta 9, opción B", "361", "Media",
  "La opción B define el principio de legalidad como «el derecho de cada país a difundir sus opiniones "
  "políticas». Esa no es la definición de legalidad; un distractor con un nombre real y una definición "
  "equivocada puede quedarse como dato.",
  "Reformular el distractor con un error que no fije una definición falsa.", "A")
h(49, "SOC", 3, "Pregunta 1", "359", "Baja",
  "La opción correcta (A) afirma que el homenaje «fortaleció la memoria colectiva y la legitimidad "
  "institucional». El texto no lo dice: habla de tensiones y de un debate sobre qué voces se escuchan. "
  "Es la mejor de las cuatro, pero su primera mitad no se puede comprobar con el texto.",
  "Ajustar la opción para que se apoye en lo que el texto dice.")
h(52, "SOC", 3, "Pregunta 8, opción C", "361", "Baja",
  "Errata: «mientras Trump desista de aumentar aranceles» (debería ser «desiste» o «no desista»). "
  "Además, la opción dice «India y Brasil» y el texto solo dice que los funcionarios indios seguirán "
  "comprando petróleo ruso. No cambia la clave (D).",
  "Corregir la errata y ajustar la referencia a Brasil.")
h(54, "SOC", 3, "Texto de las preguntas 1 a 3", "358", "Baja",
  "Errata de léxico: «ciudadanos afines a las lindes políticas del partido». «Linde» es el límite de "
  "un terreno; lo que se quiso decir es «líneas» o «ideas».",
  "Corregir a «líneas políticas» o «ideas políticas».")
h(48, "SOC", 3, "Preguntas 1, 5, 7 y 10", "359 a 361", "Atención",
  "Las cuatro preguntas de «interacción entre dimensiones» se resuelven con el mismo recurso: la "
  "correcta es la única que dice «X pero también Y» y las otras tres traen una palabra absoluta "
  "(únicamente, garantiza, nunca, necesariamente, asegura).",
  "Variar la forma de las opciones para que la correcta no se reconozca por su estructura.", "A")
h(50, "SOC", 3, "Pregunta 9", "361", "Atención",
  "El enunciado ya define el principio que pide («que protege la autodeterminación») y la opción A "
  "repite casi la misma definición («protege la autonomía frente a presiones externas»). Se resuelve "
  "por coincidencia de palabras.",
  "Retirar la definición del enunciado.")
h(53, "SOC", 3, "Pregunta 8, opción A", "361", "Atención",
  "La segunda mitad de la opción A («los críticos dicen que estas medidas terminan afectando la "
  "economía interna») es literalmente cierta según el texto; lo que falla es la primera mitad: la "
  "idea de «sanción» la dice Emma Ashford, no Trump. Es un distractor fino.",
  "Sin cambio necesario; se registra para la retroalimentación.", "A")
h(55, "SOC", 3, "Texto de las preguntas 1 a 3", "358", "Atención",
  "La fecha del 15 de agosto de 2025 para las honras fúnebres coincide con la del artículo de Infobae "
  "que se cita.",
  "Confirmar la fecha del acto en el medio original.")
h(56, "SOC", 3, "Pregunta 3", "359", "Atención",
  "La clave D usa la expresión «mínimo vital», que viene de la jurisprudencia de la Corte "
  "Constitucional y no del texto ni de la letra de la Constitución.",
  "Introducir el concepto en el texto o en la teoría de la misión.", "A")
h(60, "SOC", 4, "Reparto de claves", "370 a 374", "Media",
  "Claves 1·B 2·A 3·B 4·B 5·D 6·A 7·B 8·B 9·A 10·A: la B concentra la mitad (5 de 10) y la C no sale "
  "nunca.",
  "Redistribuir la posición de las opciones correctas.")
h(61, "SOC", 4, "Preguntas 1, 4, 6, 8, 9 y 10", "370 a 374", "Media",
  "Las tres opciones incorrectas cierran con absolutos («únicamente», «solo», «sin relación», "
  "«aislado», «se limitó») y la correcta es la que «integra»; en la 6 y la 10 la correcta es además "
  "la más larga. Se puede responder sin leer el texto, buscando la opción sin absolutos.",
  "Variar la forma de los distractores y la extensión de las opciones.", "A")
h(63, "SOC", 4, "Preguntas 4 a 7, texto de Turbo", "372", "Media",
  "El texto dice que la violencia «afectó de manera especial a mujeres», pero el tablero que lo "
  "acompaña muestra Hombre 52,87 % y Mujer 46,31 %. Texto y figura no concuerdan.",
  "Ajustar la afirmación del texto o reemplazar la figura por una que la sustente.")
h(64, "SOC", 4, "Preguntas 4 a 7, figura", "372", "Baja",
  "El tablero se titula «Desplazamiento Forzado (1984)» y su fuente es el módulo «Eventos previos a "
  "1985», mientras el texto habla de 1980 a 1984; el mapa sombrea municipios de todo el país, no solo "
  "Urabá, y no está claro si los 802 registros son de Turbo. A la escala impresa los rótulos son "
  "ilegibles.",
  "Reemplazar la captura por una figura legible y acotada a lo que dice el texto.")
h(67, "SOC", 4, "Pregunta 8, opción A", "373 y 374", "Baja",
  "La opción A no lleva punto final.", "Corregir la errata.")
h(69, "SOC", 4, "Fuente de la pregunta 1", "370", "Baja",
  "Pie de figura: «the 1960s, and 1980s» (coma sobrante en el título del trabajo de Malagón Kurka).",
  "Corregir la referencia.")
h(62, "SOC", 4, "Preguntas 1 y 4", "370 y 372", "Atención",
  "Enunciado casi idéntico en las dos: «¿qué/cuál interpretación resulta más coherente con su "
  "dimensión social?».", "Variar el enunciado de una de las dos.")
h(65, "SOC", 4, "Pregunta 7", "373", "Atención",
  "La clave B («concentración de tierras y control de rutas») exige un dato que el texto no da: el "
  "texto solo dice que el desplazamiento «coincidió» con la expansión del banano y de las rutas "
  "ilegales, y coincidencia no es causa. Las opciones A, C y D son poco plausibles, de modo que se "
  "responde por descarte.",
  "Incluir en el texto el dato que sostiene la clave.", "A")
h(66, "SOC", 4, "Pregunta 10", "374", "Atención",
  "El texto dice que tras el 11-S «se fortaleció la cooperación militar bajo el Plan Colombia». Es "
  "correcto, pero un estudiante puede entender que el Plan Colombia nació del 11-S; empezó en 1999-2000.",
  "Agregar la fecha de inicio del Plan Colombia.", "A")
h(71, "SOC", 5, "Preguntas 1, 2, 4, 8, 9 y 10", "383 a 386", "Media",
  "Las opciones incorrectas cierran con absolutos o con imposibles («no cumplen ninguna función», "
  "«resuelve al mismo tiempo la crisis política y la migratoria», «garantiza que no se presenten "
  "conflictos», «elimina cualquier posibilidad», «zona desértica») y la correcta es la única que nombra "
  "a todos los actores o todas las dimensiones; en la 1, la 4 y la 10 es además la más larga.",
  "Variar la forma de los distractores y la extensión de las opciones.", "A")
h(73, "SOC", 5, "Pregunta 2", "383", "Media",
  "El texto presenta como hecho que «en 2024, el cierre parcial de la frontera entre Venezuela y "
  "Colombia» buscaba «presionar al gobierno venezolano mediante sanciones comerciales». No se encontró "
  "sustento: la frontera se reabrió en 2022 y Colombia no aplicó sanciones comerciales a Venezuela en "
  "2024.",
  "Verificar el dato; si el caso es hipotético, presentarlo como tal.", "A")
h(76, "SOC", 5, "Pregunta 6", "385", "Media",
  "La clave A dice que el Parque Nacional «afecta la movilidad»: lo que afectaría la movilidad es el "
  "asentamiento, no el parque, y el texto nunca habla de movilidad (solo de «impactos visibles» y de "
  "«uso colectivo»). La opción D de la pregunta 5 también habla de movilidad. La clave se defiende "
  "por descarte.",
  "Reescribir la clave con los términos del texto.")
h(74, "SOC", 5, "Preguntas 5 a 7, fuente", "384", "Baja",
  "La URL de la nota de El Tiempo termina en «?utm_source=chatgpt.com» (detalle en la sección "
  "«Indicios de contenido generado automáticamente»).",
  "Limpiar la URL y verificar la fuente en el medio original.")
h(75, "SOC", 5, "Preguntas 5 a 7, texto", "384", "Baja",
  "El crédito «Maria Paula Rodriguez Rozo» va sin tildes (María, Rodríguez) y no dice si es la autora "
  "de la nota o de la foto; la nota no tiene fecha.",
  "Completar la referencia.")
h(78, "SOC", 5, "Pregunta 10", "386", "Baja",
  "«En los estados occidentales y suroccidentales de Chocó, Cauca y Nariño»: calco del inglés "
  "«states»; en Colombia son departamentos. Además, el segundo párrafo (las cuatro perspectivas) no es "
  "de Human Rights Watch, aunque queda pegado a la cita.",
  "Corregir a «departamentos» y separar la cita del texto propio.")
h(72, "SOC", 5, "Enunciados", "383 a 386", "Atención",
  "Tres plantillas de enunciado se repiten tres veces cada una: «perspectivas de los actores» (1, 7, "
  "10), «si se analizan conjuntamente las dimensiones… ¿qué afirmación refleja su interacción?» (2, 5, "
  "8) y «cómo las características del espacio geográfico influyen en la problemática social» (3, 6, 9).",
  "Variar los enunciados.")
h(79, "SOC", 5, "Pregunta 3", "383", "Atención",
  "El texto dice que el este de Ucrania «se ubica muy cerca de la frontera rusa»: la región limita con "
  "Rusia. No cambia la clave.", "Precisar la redacción.")
h(85, "SOC", 6, "Reparto de claves", "398 a 402", "Media",
  "Claves 1·C 2·C 3·B 4·B 5·C 6·B 7·D 8·B 9·C 10·D: la A no sale nunca (B 4 · C 4 · D 2).",
  "Redistribuir la posición de las opciones correctas.")
h(86, "SOC", 6, "Pregunta 6", "400", "Media",
  "Dos opciones se pueden defender: la B (debilitar la Asamblea y la Corte contradice la división de "
  "poderes) y la C (perseguir periodistas y organizaciones críticas rompe el pluralismo, que el "
  "artículo 1 nombra). EDUCATE toma la B porque el texto dice que eso «ha reducido los contrapesos "
  "institucionales que caracterizan a un sistema democrático», pero la C también describe un hecho del "
  "texto y un principio de la Constitución.",
  "Ajustar la C para que deje de ser defendible, o precisar en el enunciado el principio por el que "
  "se pregunta.", "A")
h(87, "SOC", 6, "Pregunta 10", "402", "Media",
  "La clave D gana porque nombra las tres dimensiones («políticamente… socialmente… éticamente»), pero "
  "lo que afirma en cada una no sale del texto («cuestiona el ejercicio del poder absoluto»). La B "
  "sigue de cerca el párrafo «en el plano sistémico» (precedente, polarización, confrontaciones "
  "institucionales). Un estudiante que lea bien puede elegir la B.",
  "Reescribir la clave con lo que dice el texto o ajustar la B.")
h(88, "SOC", 6, "Pregunta 7", "401", "Media",
  "Las opciones A, B y C anuncian su propia falla dentro del texto de la opción («este análisis se "
  "concentra únicamente…», «la lectura resulta incompleta…», «no logra reconocer…»); la D es la única "
  "que no se autocritica y enumera «en lo político… en lo social… en lo ético». La pregunta se "
  "contesta sin leer el caso.",
  "Reescribir los distractores para que no declaren su propio error.")
h(90, "SOC", 6, "Pregunta 1", "398", "Media",
  "La opción C (clave) dice que el modelo de desarrollo sostenible integra «las dimensiones "
  "económicas, sociales y políticas», pero el texto lo define como el que equilibra «crecimiento "
  "económico, justicia social y protección ambiental». Además, el texto pone en boca del modelo "
  "garantista un argumento («una medida simbólica no resuelve la falta de control y sanción "
  "efectiva») que no corresponde a su definición (los derechos como límites intocables).",
  "Alinear la clave con la definición que da el propio texto y revisar el argumento atribuido al "
  "modelo garantista.")
h(93, "SOC", 6, "Preguntas 5 a 7, texto de El Salvador", "400", "Baja",
  "El texto se presenta con fecha en formato inglés («May 29th 2025 |») y titular traducido, sin "
  "fuente; califica de autoritario a un jefe de Estado extranjero en ejercicio. Es contenido de "
  "opinión presentado como información.",
  "Incluir la referencia completa e indicar que es un texto de opinión.")
h(94, "SOC", 6, "Pregunta 1, fuente", "398", "Baja",
  "Pie «(Adaptado de debates recientes en política pública):» con dos puntos al final y sin una "
  "referencia que se pueda consultar.", "Incluir una referencia verificable.")
h(95, "SOC", 6, "Preguntas guía", "398", "Baja",
  "Las preguntas guía hablan de «esta ley», de «los congresistas y el Gobierno» y de «la decisión», "
  "pero la misión no trae ninguna ley: parecen de otro texto.",
  "Reemplazar las preguntas guía por unas que correspondan a los textos de la misión.")
h(96, "SOC", 6, "Pregunta 8, opción A", "401", "Baja",
  "La opción A termina «…y no debería afectar la legitimidad del gobierno nacional como piensan "
  "algunos analistas»: no queda claro si los analistas piensan que afecta o que no afecta.",
  "Reescribir la frase final.")
h(89, "SOC", 6, "Preguntas 1, 2, 7 y 10", "398 a 402", "Atención",
  "Mismo molde de enunciado («¿cuál análisis/perspectiva integra de manera más completa…?») y la "
  "correcta es siempre la que «integra» o «equilibra»; en la 7 y la 10 nombra literalmente las "
  "dimensiones. Es el mismo patrón de las misiones 3 y 4.",
  "Variar los enunciados y la forma de la opción correcta.")
h(91, "SOC", 6, "Pregunta 5", "400", "Atención",
  "El enunciado pide «el análisis de los sectores que defienden el modelo», pero el texto no describe "
  "a ningún sector que lo defienda: quienes lo llaman «autoritarismo eficaz» son «algunos analistas» "
  "críticos. La clave C se deduce igual.", "Ajustar el enunciado al texto.")
h(92, "SOC", 6, "Preguntas 2 a 4, texto base", "399", "Atención",
  "El párrafo atribuido a Bobbio (El futuro de la democracia, 1984) es una paráfrasis presentada como "
  "texto del autor; los artículos 40 y 95 de la Constitución van entre comillas pero recortados (el 95 "
  "omite la mayoría de sus numerales).",
  "Indicar «adaptado de» en el párrafo de Bobbio y señalar con puntos suspensivos los recortes de los "
  "artículos.")
# contenido de actualidad (para considerar)
h(32, "SOC", 2, "Texto de las preguntas 4 a 6", "348", "Considerar",
  "El texto trata el caso del coronel Luis Alfonso Plazas Vega y la retoma del Palacio de Justicia de "
  "1985. El tratamiento es equilibrado.",
  "Dato para que la editorial lo considere dentro del conjunto de temas sensibles del libro.")
h(44, "SOC", 3, "Texto de las preguntas 1 a 3", "358", "Considerar",
  "El texto gira alrededor de las honras fúnebres del senador Miguel Uribe Turbay (asesinado en 2025) "
  "y cita a una vendedora que dice «A mí no me importa» sobre su muerte. Es un hecho reciente, con "
  "nombre propio y alusión a su partido.",
  "Dato para que la editorial lo considere: el caso puede resultar sensible para familias y "
  "estudiantes; la habilidad que se evalúa admite un caso menos polarizante.")
h(45, "SOC", 3, "Preguntas 8 a 10", "360 y 361", "Considerar",
  "El texto y las opciones nombran a Donald Trump, presidente en ejercicio de Estados Unidos.",
  "Dato para que la editorial lo considere dentro del conjunto de temas sensibles del libro.")
h(77, "SOC", 5, "Pregunta 8", "385", "Considerar",
  "El caso nombra a una empresa real (Coca-Cola) y le atribuye una práctica que «amenaza el "
  "abastecimiento de agua» en La Calera.",
  "Dato para que la editorial lo considere: atribuir una práctica a una marca concreta puede traer un "
  "riesgo reputacional o legal; el caso funciona igual con una empresa genérica.")
h(84, "SOC", 6, "Preguntas 8 a 10 y recuadro de cierre", "401 y 402", "Considerar",
  "El libro nombra a figuras políticas colombianas de la actualidad: el presidente de la República y "
  "su hijo (pregunta 8, investigación en curso por presunto enriquecimiento ilícito) y un "
  "expresidente (preguntas 9 y 10). El recuadro «Final de la Misión» los vuelve a nombrar.",
  "Dato para que la editorial lo considere dentro del conjunto de temas sensibles del libro.")
h(83, "SOC", 6, "Preguntas 9 y 10, texto sobre la condena a un expresidente", "401 y 402", "Considerar",
  "El texto presenta como firme la condena de primera instancia de julio de 2025 (12 años de prisión "
  "domiciliaria). Según información pública, en octubre de 2025 el Tribunal Superior de Bogotá revocó "
  "esa condena en segunda instancia. El texto dice además que el caso investigaba la manipulación de "
  "testigos «en procesos contra opositores políticos», una formulación imprecisa.",
  "Verificar el estado actual del proceso y actualizar o retirar el texto antes de una nueva "
  "impresión: un hecho judicial presentado como firme pudo cambiar.", "A")

# ───────────────────────────── BIOLOGÍA ─────────────────────────────
h(98, "BIO", 1, "Pregunta 1", "72", "Media",
  "La figura dibuja el lisosoma tachado con una X roja y una flecha, justo la estructura de la opción "
  "correcta (A). La figura delata la respuesta.",
  "Retirar la marca de la figura.", "A")
h(99, "BIO", 1, "Preguntas 4 y 10", "73 y 75", "Media",
  "Las dos preguntas evalúan lo mismo (alteración del aparato de Golgi → proteínas sin modificar ni "
  "empaquetar acumuladas en el citoplasma) y las dos tienen la clave C con casi la misma redacción.",
  "Reemplazar una de las dos por una pregunta sobre otro organelo o proceso.", "A")
h(101, "BIO", 1, "Pregunta 9", "75", "Media",
  "El texto se contradice: dice que la línea B «no expresa genes relacionados con proteínas de "
  "secreción» (eso es capacidad de síntesis) y luego que los investigadores concluyeron que la "
  "diferencia no se debía «a la capacidad de síntesis». Un estudiante atento puede dudar entre A y B; "
  "la clave A se sostiene con la conclusión de los investigadores.",
  "Eliminar la contradicción del texto.", "A")
h(100, "BIO", 1, "Preguntas 6 y 7", "74", "Baja",
  "Las dos preguntas usan el mismo estudio de gemelos y piden la misma conclusión (la actividad de la "
  "enzima depende de la información genética compartida); las claves A y B dicen casi lo mismo.",
  "Diferenciar las dos preguntas.", "A")
h(102, "BIO", 1, "Pregunta 5", "73", "Atención",
  "La opción C dice que núcleo y RER «solo reducen» la exportación, pero la gráfica muestra 0 en los "
  "tres grupos tratados. La gráfica decide (clave D), pero las barras en cero son pequeñas y el "
  "estudiante debe leer el número.", "Hacer más visible el valor cero en la gráfica.")
h(105, "BIO", 1, "Página 72", "72", "Atención",
  "La Prueba de Campo empieza con una tabla «Caso / Proceso afectado / Organelo clave / Consecuencia» "
  "sin encabezado, que viene de una página anterior del libro.",
  "Revisar la diagramación del inicio de la Prueba de Campo.")
h(106, "BIO", 2, "Pregunta 2", "83", "Media",
  "Ninguna opción explica la diferencia entre las dos personas: la A (correcta) solo habla del "
  "corredor; la C dice que la respiración aumenta «sin afectar la temperatura», lo que contradice el "
  "enunciado (ambas tienen variación de temperatura); la D atribuye sudor a la persona en la sala fría. "
  "La clave A se defiende como la única fisiológicamente cierta, no como la que explica la diferencia.",
  "Reescribir la clave para que compare a las dos personas.", "A")
h(107, "BIO", 2, "Pregunta 10", "85", "Media",
  "El texto dice que el páncreas artificial libera insulina cuando la glucosa supera ciertos umbrales, "
  "«lo que evita las hipoglucemias». Liberar insulina cuando la glucosa sube evita las "
  "hiperglucemias. No cambia la clave (D).",
  "Corregir a «hiperglucemias».", "A")
h(110, "BIO", 2, "Pregunta 1", "83", "Baja",
  "La figura dice «AUMENTO DE ORINA» junto al riñón, lo que deja a un paso la clave C y descarta la B.",
  "Retirar el rótulo de la figura.", "A")
h(108, "BIO", 2, "Pregunta 5", "84", "Atención",
  "La pregunta pide la variable que se modifica «primero», y el texto dice que los niveles de urea se "
  "reducen «gradualmente»; ninguna otra variable aparece como respuesta inmediata. La clave A se "
  "sostiene, pero la tensión puede confundir.", "Ajustar «primero» o «gradualmente».", "A")
h(109, "BIO", 2, "Pregunta 7", "84", "Atención",
  "La clave B (tasa metabólica más baja) no se lee en la tabla: se infiere de la glucosa más baja "
  "(80 mg/dL) y del texto de la estivación. La opción D afirma «alta temperatura», pero la rana "
  "(33 °C) no es la especie a mayor temperatura (camello, 42 °C).",
  "Sin cambio necesario; exige cruzar tabla y texto.", "A")
h(111, "BIO", 2, "Pregunta 8", "85", "Atención",
  "La opción B dice que el camello «reduce su temperatura corporal» para sudar menos; en realidad el "
  "camello deja subir su temperatura durante el día para sudar menos. La clave A es correcta.",
  "Sin cambio necesario; dato útil para la retroalimentación.")
h(113, "BIO", 3, "Pregunta 1, tabla", "94", "Baja",
  "La tabla de biomasa no dice en qué unidades está ni qué se midió exactamente (biomasa vegetal "
  "aérea, total…).", "Agregar unidades y descripción de la medida.")
h(117, "BIO", 3, "Preguntas 8 y 9, tabla", "97", "Baja",
  "«1.2 millones», «2.8 millones», «2.1 millones»: decimales con punto, cuando en Colombia se escribe "
  "coma (1,2 millones). La opción D de la 8 habla de «diversidad funcional» y la tabla solo trae dos "
  "grupos funcionales en porcentaje.",
  "Corregir la notación decimal.")
h(114, "BIO", 3, "Pregunta 1, opción B", "94", "Atención",
  "La opción B afirma que más descomposición «disminuye la producción primaria». Es un error "
  "conceptual (descomponer libera nutrientes); como distractor sirve, pero conviene explicarlo en la "
  "retroalimentación.", "Explicar el error en la retroalimentación.")
h(115, "BIO", 3, "Preguntas 2, 3, 4 y 5", "95 y 96", "Atención",
  "En las cuatro la clave es la única opción razonable y las otras tres son disparates visibles "
  "(sensores que «atraen» aves o dan «inmunidad», competencia jaguar–chigüiro por el pasto). Son "
  "preguntas muy fáciles para el nivel Saber 11.",
  "Fortalecer los distractores.")
h(116, "BIO", 3, "Pregunta 7", "96", "Atención",
  "La pregunta de las pilas no es del componente que anuncia la misión: es de ciencia, tecnología y "
  "sociedad (manejo de residuos).", "Revisar la clasificación por componente.")
h(122, "BIO", 4, "Pregunta 7, opción A", "106", "Media",
  "El texto dice que el envase tiene «nanopartículas antimicrobianas y sensores que detectan deterioro "
  "(pH, gases)»: el cambio de color lo producen los sensores. La clave A se lo atribuye a las "
  "nanopartículas. Es la mejor de las cuatro (las otras son disparates), pero es imprecisa.",
  "Corregir la clave para que atribuya el cambio de color a los sensores.")
h(123, "BIO", 4, "Pregunta 9, opción A", "107", "Media",
  "La clave A dice «adaptar vacunas al sistema inmune del paciente para disminuir efectos "
  "secundarios»; el texto adapta la vacuna al tumor de cada paciente (neoantígenos) y menciona la "
  "menor toxicidad como resultado, no como objetivo. Las otras tres contradicen el texto, así que A "
  "queda por descarte.",
  "Reescribir la clave: adaptar la vacuna al tumor de cada paciente.")
h(124, "BIO", 4, "Reparto de claves", "104 a 107", "Baja",
  "Claves 1·B 2·C 3·C 4·A 5·D 6·A 7·A 8·C 9·A 10·A: la A sale cinco veces (6 y 7 seguidas; 9 y 10 "
  "seguidas). Un estudiante que marque A en la duda obtiene 4 de 10.",
  "Redistribuir la posición de las opciones correctas.")
h(125, "BIO", 4, "Preguntas 4, 6, 8 y 10", "105 a 107", "Atención",
  "La correcta es la opción más técnica y las demás son absurdas a la vista («chip en la médula "
  "espinal», «impulsos aleatorios», «antígenos universales reconocidos por cualquier célula»).",
  "Fortalecer los distractores.")
h(126, "BIO", 4, "Pregunta 1", "104", "Atención",
  "El texto presenta como hecho la «primera cirugía fetal intrauterina exitosa» para gastrosquisis en "
  "Colombia (El Tiempo, 2025); no se pudo verificar. La opción B explica el efecto por presión sobre "
  "«vasos mesentéricos», algo que el texto no menciona.",
  "Verificar el dato y la fuente.", "A")
h(127, "BIO", 4, "Preguntas 2 a 5, fuentes", "105 y 106", "Atención",
  "Las fuentes citadas (Wired, 13 sep 2023; Infobae, 17 jun 2025, globo con «bombas de semillas» en "
  "Manizales) y la cifra de «hasta un 37 %» de mejora de la memoria no se pudieron verificar.",
  "Verificar fechas y cifras.")
h(132, "BIO", 5, "Pregunta 6", "118", "Media",
  "La pregunta dice «Con base en la nueva información sobre la consanguinidad en la comunidad, ¿cómo "
  "se debe ajustar la predicción…?», pero antes de ella no hay comunidad, ni predicción inicial, ni "
  "información sobre consanguinidad: el tema aparece después, en el texto del Pomsky (preguntas 8 a "
  "10). Parece que se cortó un texto de contexto.",
  "Restituir el texto de contexto de la pregunta.", "A")
h(138, "BIO", 5, "Preguntas 8 a 10, texto del Pomsky", "118 y 119", "Media",
  "El texto atribuye las enfermedades a los cruces entre parientes por escasez, pero lo presenta como "
  "problema de los perros «híbridos». Cruzar dos razas distintas (Pomerania × Husky) en principio "
  "reduce la homocigosis; el problema aparece después, si se cruzan parientes. El dato «la esperanza "
  "de vida puede reducirse hasta en un 30 %» no trae fuente.",
  "Separar en el texto el cruce entre razas del cruce entre parientes y citar la fuente del 30 %.", "A")
h(134, "BIO", 5, "Pregunta 1, pedigrí", "116", "Baja",
  "En el pedigrí, los individuos de las generaciones 3 y 4 cuelgan de un solo progenitor: no se dibujan "
  "las parejas de la mujer afectada de la generación 2 ni del hombre afectado de la generación 3. En "
  "un pedigrí estándar cada descendiente sale de una línea de pareja. No cambia la clave (B).",
  "Redibujar el pedigrí con las parejas.")
h(136, "BIO", 5, "Pregunta 7, enunciado", "118", "Baja",
  "El enunciado repite la misma idea dos veces: «la resistencia se transmite a través de plásmidos que "
  "contienen genes específicos, los cuales pueden transferirse entre bacterias» y, al final, «los genes "
  "responsables de este rasgo se encuentran en plásmidos que pueden transferirse de una bacteria a "
  "otra».", "Eliminar la redundancia.")
h(133, "BIO", 5, "Pregunta 6, opción A", "118", "Atención",
  "La premisa de la opción A («la frecuencia del alelo mutado no cambia con la consanguinidad») es "
  "verdadera; lo falso es la conclusión. Exige distinguir frecuencia alélica de frecuencia genotípica, "
  "que el libro no explica.", "Incluir la distinción en la teoría de la misión.", "A")
h(135, "BIO", 5, "Pregunta 1, opción D", "116", "Atención",
  "La opción D dice que en la herencia ligada al X recesiva «las mujeres portadoras transmiten la "
  "enfermedad a todos sus hijos varones». Es falso: la transmiten en promedio a la mitad. Es un "
  "distractor, pero imprime un dato falso que un estudiante puede memorizar.",
  "Reformular el distractor.")
h(137, "BIO", 5, "Preguntas 5 y 7, distractores", "117 y 118", "Atención",
  "El distractor «transformar genes recesivos en dominantes» aparece dos veces (5C y 7A). En la 7 no "
  "tiene sentido biológico: una bacteria no tiene pares de alelos.",
  "Reemplazar el distractor de la 7.")
h(140, "BIO", 5, "Componente", "116", "Atención",
  "Las cuatro páginas dicen «COMPONENTE: entorno biológico», pero las preguntas 1, 5, 6, 7 y 9 son de "
  "herencia y genética.", "Revisar el rótulo de componente.")
h(139, "BIO", 5, "Forma de las claves", "116 a 119", "Atención",
  "En la 2, la 4, la 9 y la 10 la correcta es la más larga o la única «integradora», y en la 10 las tres "
  "incorrectas cierran con absolutos («asegura», «garantiza», «definitiva», «sin ocasionar impactos»).",
  "Variar la extensión y la forma de las opciones.")
h(141, "BIO", 6, "Pregunta 10", "130", "Alta",
  "Dos opciones defendibles. La B («la estabilidad de Chingaza se explica porque su gran tamaño "
  "poblacional y alto flujo génico mantienen variabilidad suficiente para responder a cambios "
  "ambientales, reduciendo el riesgo de deriva genética») es consistente con la tabla y con el texto, "
  "igual que la D. La D es la que usa la comparación de los tres páramos que pide el enunciado, y por "
  "eso EDUCATE la toma como clave; pero dice «demuestra» con tres poblaciones de una tabla hipotética.",
  "Confirmar la clave y ajustar la B (o el enunciado) para que solo una opción sea correcta.", "A")
h(142, "BIO", 6, "Pregunta 2, opción A", "128", "Media",
  "La clave A dice que hubo «respuesta diferencial en actividad, autocontrol y sociabilidad», pero "
  "según la tabla del libro el autocontrol fue «Alto» en los dos grupos: no cambió. La D también habla "
  "de una «disminución en autocontrol» que no ocurrió. La correcta contiene un dato falso respecto a la "
  "tabla.", "Retirar «autocontrol» de la clave.", "A")
h(143, "BIO", 6, "Pregunta 1", "127", "Media",
  "Se pide una «hipótesis evolutiva» para un experimento que mide seis meses de vida de los mismos "
  "perros (efecto del ambiente, no evolución). La clave D (selección artificial) sale de la frase "
  "introductoria «muchos perros pequeños han sido seleccionados», no de los datos; y el mismo texto "
  "dice que la raza explica solo el 9 % de la conducta.",
  "Separar en el enunciado la escala evolutiva de la escala del experimento.", "A")
h(145, "BIO", 6, "Pregunta 5", "128", "Baja",
  "El texto dice que el Bramble Cay melomys «fue declarado extinto por la IUCN en 2015». Según "
  "información pública, el último avistamiento fue en 2009, la búsqueda sin hallazgos en 2014, la "
  "declaración del gobierno de Queensland y el registro en la Lista Roja de la UICN en 2016, y la "
  "oficialización del gobierno australiano en 2019.", "Verificar y corregir la fecha.")
h(146, "BIO", 6, "Pregunta 8", "130", "Baja",
  "El enunciado pregunta por el «proceso» que explica la supervivencia del frailejón, pero las cuatro "
  "opciones describen rasgos (estructuras), no procesos.", "Cambiar «proceso» por «rasgo».")
h(144, "BIO", 6, "Preguntas 2 y 3", "128", "Atención",
  "Las preguntas 2 y 3 preguntan casi lo mismo y sus claves dicen lo mismo con otras palabras (2A: el "
  "entorno modula la expresión de rasgos; 3A: la estimulación ambiental influye en la dinámica de los "
  "perros). Los distractores también se repiten.", "Diferenciar las dos preguntas.")
h(147, "BIO", 6, "Forma de las claves", "127 a 130", "Atención",
  "En la 1, la 9 y la 10 la correcta es la más larga o la más «integradora»; en la 3, la 6 y la 9 las "
  "incorrectas cierran con absolutos («solo», «exclusivamente», «exactamente»).",
  "Variar la extensión y la forma de las opciones.")
h(148, "BIO", 6, "Pregunta 4", "128", "Atención",
  "El texto dice «Cretácico (hace 120 millones de años)» para los fósiles de Sáchica. Los fósiles de "
  "Sáchica y Villa de Leyva son del Cretácico inferior (aprox. 125 a 113 millones de años): la cifra es "
  "razonable.", "Confirmación de un especialista.")
h(149, "BIO", 6, "Actividad en el aula", "127", "Atención",
  "La actividad (mariposas claras y oscuras en un parque contaminado) es el caso clásico del melanismo "
  "industrial (Biston betularia); el libro no lo nombra ni da la fuente.",
  "Nombrar el caso y su fuente.")

# ───────────────────────────── QUÍMICA ─────────────────────────────
h(150, "QUI", 1, "Preguntas 9 y 10, figura", "142", "Media",
  "El diagrama «Síntesis de ácido acetilsalicílico» dibuja mal las moléculas: el ácido salicílico y la "
  "aspirina aparecen sin el anillo de benceno, y la flecha de «subproducto» lleva a un recuadro que "
  "vuelve a decir «Aspirina (ácido acetilsalicílico) C₉H₈O₄». El subproducto real es el ácido acético "
  "(CH₃COOH). Las fórmulas moleculares sí están bien. No cambia las claves (B y C).",
  "Redibujar las estructuras y corregir el subproducto.", "A")
h(151, "QUI", 1, "Pregunta 4, figura", "140", "Baja",
  "El texto dice que en el recipiente a 5 °C hay 40 moléculas y a 25 °C hay 16; en el dibujo hay "
  "alrededor de 55 y de 13.", "Ajustar el dibujo a las cantidades del texto.", "A")
h(152, "QUI", 1, "Preguntas 6 a 8, tabla", "141", "Baja",
  "La relación se escribe «Higroscopicidad α 1/P(H₂O)» con una alfa en lugar del signo de "
  "proporcionalidad (∝), y la tabla no dice a qué temperatura se midió la presión de vapor; 3,8 kPa es "
  "más que la presión de vapor del agua pura a 25 °C (3,17 kPa).",
  "Usar el signo ∝ e indicar la temperatura de la medida.", "A")
h(153, "QUI", 1, "Preguntas 6 y 8", "141", "Baja",
  "Las dos preguntas piden la misma idea (la sal absorbe más agua del aire porque tiene menor presión "
  "de vapor); las claves A y D dicen casi lo mismo.", "Diferenciar las dos preguntas.", "A")
h(154, "QUI", 1, "Pregunta 10", "142", "Atención",
  "El enunciado ya dice que «la reacción requiere un catalizador ácido» y pregunta por qué fue lenta; "
  "la clave (C, falta de catalizador) se lee casi en el enunciado.", "Retirar el dato del enunciado.")
h(155, "QUI", 1, "Pregunta 2", "140", "Atención",
  "La clave A explica la ley de Henry diciendo que el CO₂ «se comprime y aumenta su interacción con el "
  "agua»: la idea es aceptable, pero la redacción es imprecisa.",
  "Precisar: a mayor presión parcial, más moléculas de CO₂ se disuelven.")
h(159, "QUI", 2, "Pregunta 1, figura", "150", "Media",
  "El texto dice que Y empieza a fundirse a 160 °C, pero en la gráfica la meseta de Y está en 200 °C. "
  "Además X arranca casi en su temperatura de fusión, Y arranca muy abajo y ninguna meseta termina: la "
  "gráfica no muestra cuándo se completa la fusión, que es lo que pregunta el enunciado. La clave B se "
  "sostiene.", "Ajustar la gráfica al texto y mostrar el final de las mesetas.", "A")
h(160, "QUI", 2, "Pregunta 3, figura", "150", "Media",
  "La curva de presión del tanque de propano sube de unas 1,5 atm a 20 °C a 8 atm a 70 °C (más de cinco "
  "veces). Con la ley de los gases a volumen constante (P ∝ T en kelvin) la presión subiría solo un "
  "17 %. La curva corresponde a un gas licuado que se evapora, no a un gas ideal. No cambia la clave (B).",
  "Aclarar en el texto que es un gas licuado, o ajustar la curva.", "A")
h(161, "QUI", 2, "Pregunta 10", "152", "Media",
  "La causa principal de que la esfera suba es el empuje (el mercurio es más denso que la esfera), y no "
  "aparece entre las opciones. La clave A (baja viscosidad) solo explica la rapidez; además la "
  "viscosidad del mercurio (≈ 1,5 mPa·s) es algo mayor que la del agua.",
  "Incluir el empuje en la clave o preguntar por la rapidez del ascenso.", "A")
h(162, "QUI", 2, "Pregunta 5", "151", "Baja",
  "La opción A dice «el aire caliente» para el método A, que según el texto y el esquema es una bandeja "
  "metálica. No cambia la clave (C).", "Ajustar el distractor al montaje.")
h(163, "QUI", 2, "Pregunta 8", "152", "Baja",
  "El matraz contiene «200 mL de un sólido orgánico»: un sólido no se mide en mililitros.",
  "Expresar la cantidad en gramos.")
h(165, "QUI", 2, "Preguntas 2 y 4; 5 y 6", "150 y 151", "Baja",
  "La 2 y la 4 evalúan lo mismo (calor sensible más calor latente); la 5 y la 6, lo mismo (el baño "
  "rodea el bloque a temperatura constante).", "Diferenciar cada par.", "A")
h(164, "QUI", 2, "Preguntas 9 y 10", "152", "Atención",
  "El contexto remite a un video («Conexión SpaceGec») que el estudiante no tiene en el material impreso "
  "y no dice de qué metal es la esfera.", "Indicar el material de la esfera en el texto.", "A")
h(169, "QUI", 3, "Pregunta 9", "162", "Alta",
  "Ninguna opción es limpia. El vacío parcial jala el líquido y, cuando el de arriba se acaba, jala "
  "aire por el filtro y el tubo (ese burbujeo hace la espuma). La A dice bien el mecanismo (vacío que "
  "succiona aire) pero dice que entra «a través de las juntas» (entra por el recipiente de arriba, que "
  "está abierto). La B dice que el aire atrapado «se libera al disminuir la temperatura», al revés de la "
  "solubilidad de los gases. La C (evaporación súbita) y la D (fermentación) no tienen apoyo. EDUCATE "
  "propone la A como clave.",
  "Confirmar la clave y corregir la A (el aire entra por el recipiente superior abierto).", "A")
h(170, "QUI", 3, "Pregunta 2", "160", "Media",
  "La A («la acidez de la bebida reacciona con la tableta, produciendo más gas») es químicamente "
  "defendible: la efervescencia de la tableta es una reacción ácido + bicarbonato, y una bebida ácida "
  "la alimenta. El texto no da ningún dato de acidez, y la bebida deportiva sin gas también suele ser "
  "ácida. Clave B.",
  "Agregar al texto el dato que descarta la acidez, o ajustar la A.")
h(171, "QUI", 3, "Pregunta 3", "161", "Media",
  "La «evidencia» de la clave C (más espuma y burbujas en el vaso con gas) está confundida: una bebida "
  "con gas suelta su propio CO₂ al echarle un sólido (nucleación), aunque la tableta no reaccione más "
  "rápido. La pregunta da por hecho lo que quiere probar.",
  "Revisar el diseño del experimento o la formulación de la evidencia.")
h(176, "QUI", 3, "Pregunta 4", "161", "Baja",
  "El texto no describe lo que pasó en cada vaso (espuma, burbujas); el estudiante tiene que sacarlo de "
  "la figura y de las opciones.", "Describir las observaciones en el texto.")
h(172, "QUI", 3, "Pregunta 1", "160", "Atención",
  "Luis cambió dos condiciones a la vez (temperatura y agitación), así que los datos no dicen cuál hizo "
  "la diferencia; la opción B dice «agitación constante» y la tabla solo dice «agitó con varilla», y la "
  "C atribuye la turbidez de Felipe a «exceso de soluto» cuando los tres usaron la misma cantidad.",
  "Ajustar el diseño para que cambie una sola variable.")
h(173, "QUI", 3, "Preguntas 1 a 4 y cierre", "160 a 162", "Atención",
  "El cierre dice que la misión observó las mezclas «sin recurrir a cambios químicos», pero las "
  "preguntas 2 a 4 giran alrededor de una tableta efervescente, que es una reacción química (ácido "
  "cítrico + bicarbonato → CO₂).", "Ajustar el texto del cierre.")
h(174, "QUI", 3, "Pregunta 5, opción A", "161", "Atención",
  "Los colores de una capa delgada de aceite sobre agua son interferencia de la luz, no una reacción.",
  "Explicarlo en la retroalimentación.", "A")
h(175, "QUI", 3, "Pregunta 6", "161", "Atención",
  "La pregunta de la llanta (presión de un gas) no es de análisis de mezclas, el componente que anuncia "
  "la misión.", "Revisar la clasificación por componente.")
h(181, "QUI", 4, "Pregunta 1", "170 y 171", "Media",
  "La afirmación que hay que justificar («el sulfato de cobre es la sustancia más soluble») es falsa: a "
  "20 °C se disuelven unos 200 g de azúcar en 100 g de agua, unos 36 g de sal y unos 32 g de sulfato de "
  "cobre pentahidratado. Además la tabla no dice cuánto sólido se echó, y la temperatura final (85, 95, "
  "90 °C) no se controló. La clave A es la mejor dentro del texto, pero enseña a concluir solubilidad "
  "con datos que no la miden.",
  "Rediseñar el experimento o cambiar la sustancia de la afirmación.", "A")
h(182, "QUI", 4, "Pregunta 8", "173", "Baja",
  "La pregunta parte de que «los métodos basados en magnetismo y tamaño de partícula no fueron "
  "eficientes», y el texto del contexto nunca lo dice.", "Incluir ese dato en el contexto.")
h(186, "QUI", 4, "Página 170, «Por ejemplo»", "170", "Baja",
  "El texto de teoría dice que «un colador de plástico no transfiere calor» (sí lo transfiere, mucho "
  "menos que el metal) y trae «rapidamente» sin tilde.",
  "Corregir a «transfiere mucho menos calor» y la tilde.")
h(183, "QUI", 4, "Pregunta 3", "171", "Atención",
  "El texto dice que una mezcla «formó una pasta espesa sin separación visible» y la clave C la llama "
  "«suspensión estable»; tampoco se dice qué frasco de la figura (M1, M2, M3) tiene cada polvo.",
  "Unificar el término e identificar los frascos.")
h(184, "QUI", 4, "Pregunta 9, opción D", "173", "Atención",
  "La clave dice que la densidad «condiciona su reacción frente al estímulo mecánico»: «reacción» no es "
  "la palabra (no hay reacción química). El texto tampoco dice qué fragmentos van al borde.",
  "Cambiar «reacción» por «respuesta» o «comportamiento».")
h(185, "QUI", 4, "Preguntas 6 y 7", "172", "Atención",
  "En la 6, el carbón vegetal conduce poco salvo que esté grafitizado o activado; la clave B "
  "simplifica. En la 7, en la aventadora decide la relación entre masa y área expuesta al aire, no solo "
  "la densidad.", "Precisar las claves.")
h(191, "QUI", 5, "Pregunta 10, opción B (clave)", "185", "Media",
  "La clave B dice que los dobles enlaces y grupos polares «favorecen la formación de subproductos "
  "oxigenados, lo que reduce azufre y partículas». La causa está mal encadenada: el biodiésel emite casi "
  "nada de azufre porque los aceites vegetales casi no traen azufre; los subproductos oxigenados son un "
  "efecto de la combustión incompleta. B sigue siendo la menos mala.",
  "Reescribir la opción con la relación causal correcta (revisión de un especialista).", "A")
h(192, "QUI", 5, "Pregunta 10, enunciado", "185", "Media",
  "Llama al biodiésel «alquenos insaturados derivados de aceites vegetales». El texto de las preguntas "
  "7 a 9 lo define, bien, como ésteres metílicos; no es un alqueno. Además dice que ambos combustibles "
  "producen «niveles similares de CO₂», mientras la tabla de la página 184 muestra 260 y 240 g/km.",
  "Corregir a «ésteres metílicos» y ajustar la comparación de CO₂.", "A")
h(193, "QUI", 5, "Texto «Bebidas energizantes» y pregunta 4", "183", "Media",
  "El texto atribuye a los grupos polares (amidas, aminas) tanto la solubilidad en agua como la "
  "capacidad de la cafeína de atravesar la barrera hematoencefálica. Lo segundo es impreciso: atravesar "
  "esa barrera se ve favorecido por moléculas pequeñas con algo de carácter apolar. También llama a la "
  "cafeína «amina heterocíclica», cuando sus grupos son sobre todo amidas. No cambia la clave (C).",
  "Revisión del texto por un especialista.", "A")
h(194, "QUI", 5, "Pregunta 5", "183", "Atención",
  "Dice que la teobromina es «muy similar a la cafeína en estructura y fórmula molecular», pero el "
  "libro no da su fórmula ni su estructura (C₇H₈N₄O₂ frente a C₈H₁₀N₄O₂). Sin ese dato la pregunta se "
  "responde descartando absolutos.", "Incluir las dos fórmulas.", "A")
h(195, "QUI", 5, "Pregunta 1, opción A", "182", "Atención",
  "La opción A («el grupo hidroxilo del etanol facilita su combustión completa…») es verdadera y está "
  "en el propio enunciado; solo falla porque no explica el impacto negativo que pide la pregunta.",
  "Sin cambio necesario; distractor válido.", "A")
h(196, "QUI", 5, "Pregunta 3", "182 y 183", "Atención",
  "Dice que los materiales estuvieron en condiciones «similares» (no iguales) de humedad y temperatura, "
  "y no aclara si la pérdida de masa puede ser también agua evaporada.", "Precisar las condiciones.")
h(197, "QUI", 5, "Pregunta 6, opción D (clave)", "184", "Atención",
  "La clave dice que la evidencia «confirma» la influencia de la actividad enzimática; con dos grupos y "
  "sin saber cuántas personas hubo en cada uno, «es coherente con» sería más preciso.",
  "Cambiar «confirma» por «es coherente con».")
h(198, "QUI", 5, "Forma de las claves", "182 a 185", "Atención",
  "En la 2, la 6 y la 10 la correcta es la más larga o la única que «integra» varios datos.",
  "Variar la extensión de las opciones.")
h(201, "QUI", 6, "Pregunta 5 y texto del polímero casero", "195", "Alta",
  "El texto dice que al mezclar gel (PVP) con harina de maíz (almidón) se forma «un nuevo polímero». "
  "Es químicamente incorrecto: la PVP y el almidón ya son polímeros; al amasarlos no hay "
  "polimerización, sus cadenas se enredan y se unen por atracciones entre moléculas (puentes de "
  "hidrógeno). La clave B («surge de la unión de moléculas que se repiten en cadenas») solo es correcta "
  "dentro del modelo del libro.",
  "Corregir el texto y la pregunta con un especialista.", "A")
h(202, "QUI", 6, "Pregunta 6, opciones B y D", "195", "Alta",
  "Por lo mismo, la opción D («el polímero es solo una mezcla física de gel y almidón, sin que ocurra un "
  "cambio real en la materia») tiene una parte defendible con la química real (no se forman enlaces "
  "nuevos entre átomos), aunque «sin cambio real» es falso porque cambian las propiedades. La clave del "
  "libro es B. Hay dos respuestas defendibles a medias.",
  "Revisar la pregunta junto con la corrección del texto (hallazgo anterior).", "A")
h(203, "QUI", 6, "Pregunta 7", "195", "Media",
  "El experimento dice que las tres muestras se prepararon con las mismas cantidades, el mismo tiempo "
  "de amasado y la misma temperatura, y no dice qué cambió entre ellas. Si nada cambió, las diferencias "
  "de 5, 12 y 15 cm serían error de medición. No cambia la clave (D).",
  "Indicar la variable que cambia entre muestras.", "A")
h(204, "QUI", 6, "Preguntas 2 a 4, energía por mol", "194", "Media",
  "Compara la energía liberada por mol de gasolina (−5470 kJ/mol), etanol (−1367) y metano (−890). "
  "Entre moléculas de tamaños tan distintos eso engaña: por gramo el metano da unos 55,6 kJ/g, más que "
  "la gasolina (≈ 48 kJ/g) y que el etanol (≈ 29,7 kJ/g). La clave C («el biogás libera menos energía "
  "que los otros») es cierta solo por mol.",
  "Precisar «por mol» en la clave o agregar la comparación por gramo.", "A")
h(208, "QUI", 6, "Pregunta 9", "196", "Media",
  "Para calcular la masa de Fe₂O₃ hacen falta las masas molares (Fe = 56 g/mol, O = 16 g/mol). El libro "
  "no las da; el 56 g del clavo sugiere la del hierro, pero la del oxígeno no aparece. Sin ese dato la "
  "pregunta no se puede resolver.", "Incluir las masas molares.", "A")
h(205, "QUI", 6, "Texto de los combustibles", "194", "Baja",
  "Escribe «libera −5470 kJ/mol»: el signo menos ya indica que el calor sale; «libera» más el signo "
  "negativo es una doble negación.", "Escribir «libera 5470 kJ/mol» o «ΔH = −5470 kJ/mol».", "A")
h(206, "QUI", 6, "Pregunta 1, gráfica", "193", "Baja",
  "El eje horizontal dice 0, 2, 3, 6, 8, 10, 12, 14: el «3» debería ser 4, porque las marcas están "
  "igual de separadas. No cambia la clave (B).", "Corregir el eje.", "A")
h(207, "QUI", 6, "Pregunta 1, enunciado", "193", "Atención",
  "El enunciado no dice que la cantidad de ácido sea la misma en todos los ensayos, y la clave B depende "
  "de eso («al agotarse el ácido»). Tampoco hace falta la «conservación de la materia y energía» que "
  "cita.", "Agregar el dato al enunciado.")
h(209, "QUI", 6, "Pregunta 10", "196", "Atención",
  "Hay una sola medición por temperatura, sin repeticiones, y la relación «pH baja = descomposición» la "
  "afirman los investigadores, no los datos.", "Sin cambio necesario; útil para discutir el diseño.")
h(210, "QUI", 6, "Página 193, actividad anterior", "193", "Atención",
  "La página empieza con «Preguntas: 1. ¿En cuál ensayo la reacción ocurre con mayor rapidez…? 2. ¿Qué "
  "variable explica la diferencia entre A y B?…» sobre unos ensayos cuyos datos no están en la Prueba de "
  "Campo (deben estar en la página 192). Esas preguntas también van numeradas 1 a 4.",
  "Diferenciar la numeración de la actividad y la de la Prueba de Campo.")

# ───────────────────────────── FÍSICA ─────────────────────────────
h(214, "FIS", 1, "Pregunta 6", "206", "Media",
  "Dos opciones defendibles. «Mantener el equilibrio al aterrizar» se cumple mejor apoyando los dos pies "
  "(B: agranda la base de apoyo), pero flexionar más la rodilla (C) alarga el tiempo del contacto y "
  "reduce la fuerza, que también se lee como «controlar» el aterrizaje. EDUCATE propone la B.",
  "Confirmar la clave y precisar en el enunciado qué cuenta como equilibrio.", "A")
h(215, "FIS", 1, "Pregunta 3, figura", "205", "Media",
  "El diagrama de fuerzas del carro en la rampa dibuja la normal vertical (debe ser perpendicular a la "
  "rampa) y las dos componentes del peso, P∥ y P⊥, ambas verticales hacia abajo (P∥ debe ir a lo largo "
  "de la rampa y P⊥ contra ella). El rozamiento aparece como rótulo sin flecha clara. No cambia la "
  "clave (B).", "Redibujar el diagrama.", "A")
h(216, "FIS", 1, "Pregunta 8, figura", "207", "Media",
  "La prenda aparece en el centro del tambor y la flecha de la «fuerza centrípeta» apunta hacia el "
  "borde: la fuerza centrípeta apunta hacia el centro del giro, con la prenda pegada a la pared. La "
  "flecha «Movimiento» va vertical hacia abajo sin explicar qué representa. No cambia la clave (A).",
  "Redibujar la figura.", "A")
h(217, "FIS", 1, "Pregunta 1, figura", "205", "Baja",
  "La gráfica v–t no dice qué bloque baja por el plano de mayor ángulo; la leyenda pone el bloque B "
  "primero; las dos rectas empiezan un poco por debajo de 0 m/s.", "Completar la leyenda y el origen.")
h(219, "FIS", 1, "Pregunta 9", "207", "Baja",
  "El enunciado pide el trabajo «sobre el bloque A», pero la figura no tiene letras; no se dice si el "
  "bloque sube o baja (el signo del trabajo cambia).", "Rotular el bloque e indicar el sentido.", "A")
h(220, "FIS", 1, "Pregunta 10, figura", "208", "Baja",
  "El eje vertical de la gráfica C dice 2,0 · 1,5 · 1,0 · 1,5 · 0,0: el cuarto valor debería ser 0,5 (y "
  "«0,0» usa coma mientras los demás usan punto).", "Corregir el eje.", "A")
h(218, "FIS", 1, "Pregunta 5", "206", "Atención",
  "Se pregunta qué «favoreció que mantuviera el equilibrio en el aire», pero lo que explica la opción "
  "correcta (C) es la conservación del momento angular (L = I·ω); «distribuyó mejor la masa» no es un "
  "término físico.", "Reformular con el principio de conservación.", "A")
h(221, "FIS", 1, "Preguntas 4 a 6", "206", "Atención",
  "El caso remite a un video («Conexión SpaceGec · Bailarín de Ballet slow motion (e-book)») que el "
  "estudiante del material impreso no tiene; «Bailarin» sin tilde. El texto alcanza para responder.",
  "Corregir la tilde.")
h(223, "FIS", 2, "Pregunta 10", "218", "Alta",
  "Dos opciones correctas. La D, c₂ = (500 × (30 − 25)) ÷ (200 × (80 − 30)) = 0,25, y la A, "
  "c₂ = (500 × (25 − 30)) ÷ (200 × (30 − 80)) = (−2500) ÷ (−10 000) = 0,25, son la misma expresión: "
  "los dos signos negativos se cancelan.",
  "Corregir la opción A, por ejemplo a (500 × (30 − 25)) ÷ (200 × (30 − 80)), que da negativo. Clave D.",
  "A")
h(224, "FIS", 2, "Pregunta 4", "217", "Media",
  "El enunciado dice que el cocinero libera vapor para reducir la presión «buscando disminuir el tiempo "
  "de cocción sin elevar demasiado la temperatura». Es al revés: a menor presión el agua hierve a menor "
  "temperatura y las verduras tardan más; la olla a presión cocina rápido por la presión alta. La figura "
  "(«Menor presión → menor temperatura de ebullición») sí es correcta. No cambia la clave (B).",
  "Corregir el propósito descrito en el enunciado.", "A")
h(225, "FIS", 2, "Pregunta 5, gráfica", "217", "Media",
  "La gráfica de temperatura contra energía extraída se aplana cerca de −273 °C, como si el gas "
  "necesitara cada vez más energía por grado; la tercera ley dice lo contrario (la capacidad calorífica "
  "tiende a cero), y un gas real se licúa mucho antes. La justificación de la C («la energía disponible "
  "para extraer es mínima») no explica la forma de la curva. El eje dice «-0» por 0.",
  "Revisión de la pregunta por un especialista.")
h(226, "FIS", 2, "Pregunta 7", "218", "Baja",
  "La clave C (el cobre, por su menor calor específico) supone que los dos bloques pierden calor al "
  "mismo ritmo. Con la misma masa, el bloque de aluminio es unas 3,3 veces más voluminoso y tiene más "
  "del doble de superficie; con la ley de enfriamiento de Newton tardarían casi lo mismo.",
  "Declarar el supuesto en el enunciado.", "A")
h(227, "FIS", 2, "Pregunta 1", "216", "Baja",
  "La ley de Fourier se escribe Q = k·A·(T₁ − T₂)/d: falta el tiempo (es el calor por unidad de tiempo, "
  "Q/t). La pared X de aluminio se describe y no se usa.", "Escribir Q/t.", "A")
h(228, "FIS", 2, "Preguntas 2 y 3", "216", "Atención",
  "El caso se titula «Efecto Mpemba», pero lanzar agua hirviendo al aire en un día bajo cero es otro "
  "fenómeno (gotas finas que se evaporan y se congelan). El efecto Mpemba es que, en ciertas "
  "condiciones, el agua caliente se congela antes que la fría en un recipiente.",
  "Cambiar el título del caso.")
h(231, "FIS", 3, "Pregunta 6", "227", "Media",
  "En la figura B (dos cargas positivas) las flechas apuntan hacia la línea que une las cargas, como si "
  "las líneas llegaran a ellas; con cargas positivas deben salir. Ninguna figura es del todo correcta; "
  "B es la única con la forma correcta. EDUCATE propone la B.",
  "Corregir el sentido de las flechas de la figura B.", "A")
h(232, "FIS", 3, "Pregunta 1", "226", "Media",
  "El estudiante del caso dice que el campo «interactúa directamente con los electrones del alambre y "
  "los empuja». La clave D dice que la afirmación «es correcta» por el cambio de flujo (Faraday), que "
  "es otra razón: un campo quieto no mueve electrones quietos. La B también la llama «correcta» y habla "
  "de un campo que varía. Dos opciones defendibles.",
  "Reformular para que la clave valore la explicación, no solo el veredicto.")
h(233, "FIS", 3, "Pregunta 7", "227", "Baja",
  "La carga de prueba se da como «2 × 10⁻⁶ (positivo)» sin unidad (coulomb) y las opciones dan «un "
  "vector de 8 × 10⁻⁴» sin unidad (newton).", "Agregar las unidades.", "A")
h(234, "FIS", 3, "Pregunta 4", "227", "Atención",
  "La opción A habla de «una carga negativa en movimiento», pero el texto no dice el signo de la carga.",
  "Indicar el signo en el texto.")
h(236, "FIS", 3, "Preguntas 8 y 9", "228", "Atención",
  "El texto dice que «el acero pierde el magnetismo a 770 °C»: es la temperatura de Curie del hierro "
  "puro; la de los aceros varía con la aleación. La 9 supone que las dos agujas se calientan igual con "
  "la misma fuente, lo que depende de su masa y su calor específico.", "Precisar el dato.")
h(237, "FIS", 4, "Pregunta 3", "237", "Alta",
  "En el esquema hay dos rayos rotulados «A» (uno en el aire y otro en el agua) y el rayo «B» está en el "
  "aire. El rayo que se acerca a la normal dentro del agua lleva la letra A, pero la opción con la razón "
  "correcta es «Trayectoria B, porque al disminuir su velocidad en el agua, la luz se desvía acercándose "
  "a la línea normal». La figura contradice la clave.",
  "Corregir los rótulos del esquema. EDUCATE propone la B como clave (por la razón).", "A")
h(238, "FIS", 4, "Pregunta 9", "239", "Alta",
  "Ninguna opción da la razón física principal: la rapidez de una onda en un sólido depende de su "
  "rigidez (módulo de elasticidad) y de su densidad. La absorción (C) reduce la amplitud y el alcance, "
  "no la rapidez; aun así el libro la sostiene en su repaso («en caucho llegaría mucho más tarde por su "
  "absorción», p. 236). La A es falsa: el caucho (≈ 1,1–1,5 g/cm³) es menos denso que el aluminio "
  "(2,7 g/cm³). EDUCATE propone la C, con reserva.",
  "Agregar la rigidez como razón en la opción correcta y corregir el repaso de la página 236.", "A")
h(239, "FIS", 4, "Pregunta 4", "238", "Media",
  "A («las paredes metálicas reflejan parte de la señal…») y D («interferencia destructiva por las "
  "múltiples reflexiones…») son defendibles. La explicación principal es A: el metal refleja casi toda "
  "la onda que llega y entra poca señal; la interferencia redistribuye la señal pero no baja su promedio. "
  "EDUCATE propone la A.", "Confirmar la clave.")
h(240, "FIS", 4, "Pregunta 6", "238", "Media",
  "Los dos vasos están en el mismo tablero, a casi la misma distancia de un dinosaurio lejano; que uno "
  "tenga ondas de mayor amplitud se explica mejor por la cantidad de agua o el vaso. La clave A («el "
  "vaso con mayor amplitud está más cerca del origen») no se puede establecer con esa observación. La "
  "escena es de una película.", "Replantear la observación o la clave.")
h(243, "FIS", 4, "Página 236, repaso", "236", "Media",
  "El repaso dice que «en caucho llegaría mucho más tarde por su absorción»: la causa es la baja "
  "rigidez, no la absorción (ver la pregunta 9).", "Corregir el repaso.")
h(241, "FIS", 4, "Pregunta 7", "238", "Atención",
  "B (tipo de líquido y forma de la superficie) y C (altura del agua) también son variables que hay que "
  "controlar; A es la más relevante. Clave A.", "Sin cambio necesario.")
h(242, "FIS", 4, "Preguntas 8 y 10", "239", "Atención",
  "La pregunta 8 se responde mejor con los radios que da después la pregunta 10 (12, 8 y 3 cm).",
  "Reordenar la información.", "A")
h(247, "FIS", 5, "Pregunta 8, opciones A y D", "250", "Media",
  "Dos valoraciones señalan algo que de verdad no se probó: la A (solo agua, no otros líquidos) y la D "
  "(solo vasos del mismo tamaño). La A es la mejor porque ataca la generalización «cualquier líquido», "
  "pero la D también es una crítica válida.", "Ajustar la D para que no sea defendible.")
h(244, "FIS", 5, "Pregunta 1, enunciado", "247", "Baja",
  "Dice que el astronauta «pesa 80 kg». El kilogramo mide masa; el peso es una fuerza (800 N con "
  "g = 10 m/s²). El dato, además, no interviene en la pregunta.", "Escribir «tiene una masa de 80 kg».",
  "A")
h(246, "FIS", 5, "Pregunta 4, datos", "248", "Baja",
  "Las rapideces (8 m/s y 5 m/s) son «promedio en los trayectos horizontales», no la rapidez en el "
  "momento de la entrega, y la pregunta las usa para la energía mecánica de la entrega. No cambia la "
  "clave (B).", "Precisar que se toma esa rapidez en la entrega.", "A")
h(249, "FIS", 5, "Texto del sifón", "249", "Baja",
  "Dice que el sifón funciona «siempre que la salida esté más baja que el nivel inicial del líquido». La "
  "condición es que la salida esté más baja que el nivel actual del líquido en el vaso de arriba (y que "
  "el pitillo esté lleno).", "Corregir la condición.")
h(250, "FIS", 5, "Pregunta 10, opción A (clave)", "250", "Baja",
  "Incluye «la resistencia del aire» entre las fuerzas que se oponen al movimiento del agua dentro del "
  "pitillo; dentro de un pitillo lleno de agua no hay aire: frena la fricción con las paredes "
  "(viscosidad).", "Cambiar «resistencia del aire» por «fricción con las paredes».")
h(245, "FIS", 5, "Pregunta 3", "248", "Atención",
  "El enunciado ya trae la causa (el reloj en órbita avanza más rápido porque el campo es más débil) y "
  "la clave A solo la repite. Además, en el GPS real la velocidad del satélite atrasa su reloj "
  "(relatividad especial, unos 7 μs por día) y la gravedad lo adelanta (unos 45 μs): la opción C dice "
  "lo contrario de lo que hace la velocidad.", "Retirar la causa del enunciado.", "A")
h(248, "FIS", 5, "Pregunta 9", "250", "Atención",
  "Pide «el modelo físico de la dinámica clásica» que explica el sifón. La clave D (presión atmosférica "
  "y gravedad) es la única sin error, pero no es un modelo de la dinámica; el modelo (conservación de la "
  "energía en el fluido) es el que la B nombra con una razón falsa.", "Revisar el enunciado.", "A")
h(252, "FIS", 6, "Pregunta 1, opciones B y D", "259", "Media",
  "La afirmación dice que lo aprovechado en calefacción es «equivalente» a la energía térmica liberada. "
  "La B la refuta con los datos (6500 < 9000; 71–73 %). La D también es defendible si «eficiencia del "
  "sistema» se lee como electricidad → calefacción (6500/12 000 = 54 %).",
  "Precisar en el enunciado qué eficiencia se evalúa.")
h(253, "FIS", 6, "Pregunta 4, opciones B y D", "260", "Media",
  "Las dos dicen que los datos no permiten afirmar eficiencia total y las dos son ciertas. La D añade "
  "que una hora no basta para generalizar, que es lo que pregunta el contexto. Clave D; la B es "
  "verdadera pero incompleta.", "Ajustar la B.", "A")
h(256, "FIS", 6, "Pregunta 10, opciones B y D y enunciado", "262", "Baja",
  "La D es la clave (54 kJ entregados; 45 + 6 = 51 kJ; faltan 3 kJ). La B es parcialmente defendible "
  "(los 15 W son nominales). Además, el enunciado dice que la batería «almacenó 45 kJ de energía "
  "eléctrica»: una batería guarda energía química.", "Corregir la redacción sobre la batería.")
h(254, "FIS", 6, "Pregunta 6, enunciado", "261", "Atención",
  "El montaje del texto tiene cinco velas y la pregunta usa cuatro («en una versión del experimento»). "
  "Es fácil multiplicar por cinco (125 kJ, que no es opción).", "Destacar el cambio en el enunciado.", "A")
h(255, "FIS", 6, "Pregunta 9", "262", "Atención",
  "Es un circuito eléctrico (corriente en dos resistencias en paralelo) dentro de una misión del "
  "componente termodinámica.", "Revisar la clasificación por componente.")
h(257, "FIS", 6, "Actividad en el aula", "259", "Atención",
  "La Prueba de Campo empieza con las opciones C y D de la actividad; las A y B están en una página "
  "anterior.", "Revisar la diagramación.")

# ───────────────────────────── INGLÉS ─────────────────────────────
h(260, "ING", 1, "Parte 1, reparto de claves", "414", "Media",
  "Las claves de la Parte 1 salen casi en el orden alfabético del banco: grupo 1 (preguntas 1–7) C A B "
  "H D E F; grupo 2 (8–14) B A C D E F G. Quien marque «en orden» acierta casi todo sin leer.",
  "Barajar el orden del banco de palabras.", "A")
h(261, "ING", 1, "Parte 1, instrucción y banco del grupo 1", "414", "Baja",
  "La instrucción dice «columna de la derecha (A - H)… la opción I se usa para el ejemplo», pero el "
  "banco del grupo 1 muestra la I (Journalist) en negrilla y con su círculo para rellenar, como una "
  "opción más; el grupo 2 no tiene I ni ejemplo. Además, el grupo «People and What They do» incluye "
  "«Factory», que es un lugar.",
  "Diferenciar visualmente la opción del ejemplo y revisar el título del grupo.", "C")
h(263, "ING", 1, "Pregunta 21", "415", "Baja",
  "«Immigration control: Keep passport and boarding pass ready» tiene como clave «Airport security "
  "area». En un aeropuerto, el control de inmigración y el filtro de seguridad son puntos distintos.",
  "Cambiar la opción por «Immigration area» o ajustar el aviso.", "C")
h(262, "ING", 1, "Pregunta 13", "414", "Atención",
  "«This is a group of students who discuss a topic with a teacher» define «Seminar» como un grupo de "
  "personas; un seminar es la clase o reunión donde se discute. La clave se sostiene.",
  "Precisar la definición.", "A")
h(264, "ING", 1, "Preguntas 10 y 12", "414", "Atención",
  "«A person who studies for a degree at a university» (Student) y «a test students take to enter a "
  "university» (Exam) son definiciones amplias: «student» no exige universidad y la 12 corresponde a "
  "«entrance exam». Las claves se sostienen.", "Ajustar las definiciones o las palabras.")
h(268, "ING", 1, "Pregunta 17", "415", "Atención",
  "El aviso «Don't share personal information in the comments. Report suspicious accounts» tiene como "
  "clave «Social media post»; es más un aviso de la plataforma (normas de la comunidad). La clave se "
  "sostiene.", "Sin cambio necesario.")
h(270, "ING", 1, "Pregunta 2", "414", "Atención",
  "«This is a place where…» (Factory) es la única descripción de lugar del grupo y «Factory» es el único "
  "lugar del banco: la primera palabra resuelve la pregunta.", "Incluir otro lugar en el banco.", "A")
h(259, "ING", 1, "Toda la misión", "414 y 415", "Atención",
  "La Prueba de Campo trae 21 ítems (Parte 1: 14 descripciones con banco de palabras; Parte 2: 7 "
  "avisos), no 10 como las demás misiones del libro.", "Dato de estructura; sin cambio necesario.")
h(271, "ING", 2, "Forma de las opciones", "424 y 425", "Media",
  "En 7 de las 10 preguntas (1, 2, 3, 4, 5, 6 y 8) la correcta es la única opción que empieza por "
  "«Yes», y ninguna distractora empieza por «Yes». Además, todas las distractoras repiten un sustantivo "
  "de la frase (printers, Internet, concerts, budgets, phones, jobs, doctors, TV, Mark, water). Un "
  "estudiante puede acertar 7 de 10 sin entender la conversación; en el ICFES las distractoras no siguen "
  "ese patrón.", "Variar el inicio de las opciones correctas y de las distractoras.", "A")
h(272, "ING", 2, "Pregunta 9", "425", "Media",
  "La opción B «Mark and I was just discussing the math project» tiene un error de concordancia (debe "
  "ser «were»). El cierre de la misión dice que el estudiante descartó «opciones gramaticalmente "
  "correctas que no respondían a la situación», y esta no es gramaticalmente correcta. Corregida, la B "
  "también contesta «What happened?»: el ítem solo discrimina por la gramática.",
  "Reemplazar la B por una opción gramatical que no responda a la situación.", "C")
h(273, "ING", 2, "Pregunta 10", "425", "Atención",
  "La opción C «I prefer drinking juice instead of water» es una respuesta posible en una charla real; la "
  "B (clave) es la más natural porque reacciona al consejo.", "Sin cambio necesario.")
h(274, "ING", 2, "Imágenes de las preguntas 2 y 8", "424 y 425", "Atención",
  "La imagen de la pregunta 2 repite el enunciado dentro del dibujo; la de la 8 muestra el logotipo de "
  "Facebook, una marca comercial. Las ilustraciones tienen apariencia de imágenes generadas "
  "automáticamente (mismo trazo, texto incrustado).",
  "Confirmar el origen y la licencia de las ilustraciones; retirar el logotipo.")
h(276, "ING", 3, "Espacio 32", "437", "Alta",
  "«Citizens accuse leaders of acting ___ the interests of political elites»: ninguna opción es "
  "correcta. La colocación es «acting in the interests of» (o «on behalf of»); therefore (A) es un "
  "conector, y by (B) y with (C) no forman la expresión. No hay clave posible.",
  "Incluir «in» entre las opciones.", "C")
h(277, "ING", 3, "Espacio 34", "437", "Alta",
  "«These mobilizations are powerful, ___ they reveal deep frustration…»: as (A), since (B) y because "
  "(C) son las tres conectores de causa, y las tres son gramaticales y lógicas en esa posición. Tres "
  "respuestas defendibles.", "Reemplazar dos opciones por conectores de otra relación.", "C")
h(278, "ING", 3, "Espacio 12", "436", "Media",
  "«It ___ in cinemas around the world»: la opción A está mal escrita («was release», debería ser «was "
  "released»), y la forma correcta en voz pasiva no está entre las opciones. La clave esperada B («It "
  "released in cinemas») es un uso informal, no el estándar de un examen.",
  "Corregir la A a «was released» y tomarla como clave.", "C")
h(279, "ING", 3, "Espacios 18 a 20", "436", "Media",
  "Miles Morales «___ with problems» (dealt / deals / deal), «He also ___ to decide» (try / tries / "
  "tried), «the movie ___ viewers waiting» (leaves / left / leave). En el resumen de una película el "
  "presente narrativo (deals, tries, leaves) es correcto; el pasado (dealt, tried, left) también, por el "
  "«In 2023» del comienzo. Claves esperadas: 18 A, 19 C, 20 B. Dos respuestas defendibles en cada uno.",
  "Dejar una sola forma verbal correcta en cada espacio.", "C")
h(280, "ING", 3, "Espacio 24", "436", "Media",
  "«assignments are checked carefully ___ plagiarism detectors»: by (A, el agente) y with (B, el "
  "instrumento) son correctas; through (C) también se acepta.",
  "Reemplazar dos opciones por preposiciones incorrectas.", "C")
h(281, "ING", 3, "Espacio 35", "437", "Media",
  "«Protesters frequently communicate ___ digital platforms»: through (A) y on (C) son correctas; by (B) "
  "no.", "Reemplazar la C.", "C")
h(287, "ING", 3, "Espacio 17", "435 y 436", "Media",
  "«Audiences were very impressed by the story, which ___ both exciting action and emotional moments»: "
  "la esperada es combined (B), pero combines (C) también es correcta: la oración de relativo describe "
  "lo que la historia es. combine (A) no concuerda.", "Reemplazar la C.", "C")
h(282, "ING", 3, "Espacio 39", "437", "Baja",
  "«This participation requires both courage and organization, ___ it cannot succeed without broad "
  "alliances»: la esperada es since (C), pero but (B) también se defiende (agrega una condición).",
  "Reemplazar la B.", "C")
h(286, "ING", 3, "Instrucción y cierre", "435 a 437", "Baja",
  "La instrucción mezcla tú y usted («Lee el texto… y seleccione la palabra»). El cierre habla de "
  "«competencia pragmática», pero el componente de la misión es gramatical y léxico.",
  "Unificar el trato y ajustar el cierre.")
h(283, "ING", 3, "Espacio 33", "437", "Atención",
  "«leading to instability ___ entire regions»: across (C) es la esperada y es correcta; through (B) "
  "también se defiende. Lo natural sería «throughout».", "Revisar la B.")
h(284, "ING", 3, "Espacio 40", "437", "Atención",
  "«protests remain an ___ reminder»: el artículo «an» descarta solo la opción deny (empieza por "
  "consonante). Entre undeniable y undeniably decide la clase de palabra. Clave A.",
  "Reemplazar «deny» por una opción que empiece por vocal.", "A")
h(288, "ING", 3, "Espacio 29", "436", "Atención",
  "«digital literacy will be essential ___ succeed»: el texto 3 se presenta como de preposiciones, pero "
  "aquí «to» es la marca del infinitivo, no una preposición. Clave B.", "Revisar la clasificación del ítem.")
h(289, "ING", 3, "Espacios 10 y 13", "435", "Atención",
  "Las opciones mezclan verbos de familias distintas en un mismo espacio (10: go / were / was; 13: go / "
  "gone / went). En el 10 la opción go no es del verbo be y se descarta sin leer.",
  "Usar formas del mismo verbo en cada espacio.")
h(290, "ING", 4, "Bloque 2, texto de la Vuelta", "447", "Media",
  "El texto dice que en 2016 fue «the first time two Colombians shared the final podium of the Vuelta». "
  "Es falso: en 1989 el podio fue Pedro Delgado, Fabio Parra (2.º) y Óscar de Jesús Vargas (3.º). Lo "
  "verdadero es que 2016 fue la primera vez que un colombiano ganó la Vuelta con otro colombiano en el "
  "podio (Quintana 1.º, Froome 2.º, Chaves 3.º). Las demás cifras (83 h 31 min 28 s, más de 3.200 km, "
  "300 millones de espectadores) no se pudieron verificar.",
  "Corregir la afirmación y verificar las cifras.", "C")
h(291, "ING", 4, "Bloque 2, preguntas 2 y 6", "448", "Baja",
  "Las opciones 2B y 6A llaman a Froome «The British cyclist». El texto solo dice «Chris Froome, from "
  "Team Sky»: la nacionalidad no está en el texto. En una prueba de lectura literal la clave de la 6 (A) "
  "depende de un dato externo.", "Agregar la nacionalidad al texto o retirarla de la opción.", "C")
h(292, "ING", 4, "Bloque 1, texto de TWICE", "447", "Baja",
  "«Their widespread fame is further reflected topping global charts»: falta la preposición "
  "(«reflected in topping global charts»).", "Corregir.", "C")
h(293, "ING", 4, "Bloque 1, pregunta 6", "447", "Baja",
  "La opción A dice «three full albums and two LP»: un LP es un álbum completo, así que la opción no "
  "tiene sentido (y «LP» va sin plural).", "Reescribir el distractor.")
h(294, "ING", 4, "Bloque 2, pregunta 4", "448", "Atención",
  "La opción A dice que Herrera ganó «three decades after 2016» (en el futuro): choca con «previously» "
  "de la misma pregunta y no distrae.", "Reescribir el distractor.")
h(299, "ING", 4, "Bloque 2, preguntas 5 y 8", "448", "Atención",
  "Las distractoras traen datos que no están en el texto (Mont Ventoux, Sierra Nevada; 150 y 200 "
  "millones). En la 8, la pregunta dice «Approximately» y la clave copia «More than three hundred "
  "million» del texto.", "Ajustar la redacción de la 8.")
h(300, "ING", 4, "Bloque 1, pregunta 8", "447", "Atención",
  "«TWICE debuted in the year» → 2015, copiado literal del texto; 2018 y 2019 no aparecen. Pregunta muy "
  "fácil.", "Sin cambio necesario.")
h(296, "ING", 4, "Numeración de los bloques", "446 a 448", "Atención",
  "La numeración vuelve a empezar en 1 en el bloque 2 («Responde las preguntas 1 a 8» dos veces). Lo "
  "mismo pasa en las misiones 5 (dos bloques) y 6 (tres bloques): «Bloque 1, pregunta 3» y «Bloque 2, "
  "pregunta 3» son preguntas distintas.", "Numerar las preguntas de forma continua en cada misión.")
h(302, "ING", 5, "Bloques 1 y 2, opciones", "457 a 459", "Atención",
  "En casi todas las preguntas los distractores cierran con absolutos («exclusively», «completely», "
  "«inherently», «nearly eliminated», «all», «far more») y la correcta es la única que matiza. Un "
  "estudiante puede acertar sin leer el texto.",
  "Variar la forma de las opciones.", "A")
h(304, "ING", 5, "Language Tools", "456", "Atención",
  "La tabla de herramientas (expresiones idiomáticas, marcadores culturales, registro formal e "
  "informal, connotación «home / house») no la evalúa ninguna de las 16 preguntas.",
  "Alinear el repaso con la prueba.")
h(314, "ING", 5, "Bloque 2, pregunta 6", "459", "Atención",
  "«By mentioning diverse genres like boleros, rap, and drums…»: la clave C («a connection to "
  "deep-seated cultural histories») se sostiene con los tambores y con «shared roots», pero el texto dice "
  "que el rap improvisa «about politics or love», no sobre la historia.", "Ajustar los ejemplos del enunciado.")
h(305, "ING", 5, "Bloque 2, crédito de la foto", "458", "Baja",
  "«This Photo by Unknown Author is licensed under CC BY-SA-NC»: autor desconocido y una licencia escrita "
  "en un orden que no existe (la de Creative Commons es BY-NC-SA).", "Verificar autor y licencia.")
h(316, "ING", 5, "Bloque 2, pregunta 2", "458", "Baja",
  "La pregunta cita «hurrying past»; el texto dice «people hurry past».", "Ajustar la cita.")
h(320, "ING", 6, "Bloque 1, pregunta 2", "468 y 469", "Media",
  "«The road was long, and we ___ tired when we finally arrived»: la clave es B (felt), pero C (were "
  "feeling) también es gramatical: «feel» admite la forma continua para un estado del momento.",
  "Reemplazar la C.", "C")
h(323, "ING", 6, "Bloque 2, pregunta 1", "469", "Media",
  "«students ___ different points of view about a topic»: A (express) es la clave, pero D (explore) "
  "también es correcta y natural.", "Reemplazar la D.", "C")
h(326, "ING", 6, "Bloque 3, pregunta 1", "470", "Media",
  "«when Sherlock Holmes ___ the fire»: la clave es C (lit), pero B (lighted) también es un pasado "
  "correcto de «light».", "Reemplazar la B por otra forma.", "C")
h(328, "ING", 6, "Bloque 3, pregunta 7", "470", "Media",
  "«while Holmes ___ each detail with unbroken attention»: con la clave C queda «listened each detail», "
  "que es un error: «listen» pide «to». Ninguna opción deja la oración correcta.",
  "Escribir «listened to each detail» o cambiar el verbo («followed»).", "C")
h(321, "ING", 6, "Bloque 1, pregunta 3", "468 y 469", "Baja",
  "«While we ___ our tent»: falta la partícula del verbo frasal («set up a tent» o «pitch a tent»).",
  "Agregar «up».", "C")
h(327, "ING", 6, "Bloque 3, pregunta 4", "470", "Baja",
  "«hurried footsteps ___ on the stairs»: la clave es B (ran), pero los pasos no «corren»: suenan "
  "(«sounded», «echoed», «came»).", "Cambiar el verbo.", "C")
h(329, "ING", 6, "Créditos de imagen", "469 y 470", "Baja",
  "«This Photo by Unknown Author is licensed under CC BY-SA-NC»: autor desconocido y licencia en un "
  "orden que no existe.", "Verificar autor y licencia.")
h(319, "ING", 6, "Language Tools y ejemplo", "468", "Atención",
  "La misión abre con conectores (however, therefore, because, in addition…), pero ninguna de las 24 "
  "preguntas evalúa un conector: todas son tiempos verbales, formas y vocabulario.",
  "Alinear el repaso con la prueba.")
h(322, "ING", 6, "Bloque 1, pregunta 7", "468 y 469", "Atención",
  "«I have already taken many photographs…, and I ___ a blog»: la clave es B (started), pero el párrafo "
  "va en presente perfecto y lo natural sería «have started», que no está entre las opciones.",
  "Revisar las opciones.", "A")
h(324, "ING", 6, "Bloque 2, pregunta 2", "469", "Atención",
  "«Some debates ___ subjects like…»: «involve subjects» es poco natural; lo común es «cover», «address» "
  "o «deal with». Es la clave (D) porque las demás no tienen sentido.", "Cambiar el verbo de la clave.")
h(325, "ING", 6, "Bloque 2, pregunta 6", "469", "Atención",
  "«Teachers ___ debates as a way to make classes more dynamic»: B (use) es la clave por el presente del "
  "texto; C (used) también es gramatical aunque cambia el tiempo.", "Sin cambio necesario.")
h(332, "ING", 6, "Bloque 1, pregunta 8", "469", "Atención",
  "«Honestly, I ___ never imagined how much I would love outdoor adventures»: la clave es A (had). C "
  "(«have») es gramatical, pero choca con «would love».", "Sin cambio necesario.", "A")


# ─────────── reparto de claves por misión (tabla de la sección de atención) ───────────
# (area, misión, reparto, observación, n del tablero)
REPARTO = [
    ("LC", "3", "cinco B", "una letra concentra la mitad", 24),
    ("LC", "5", "cinco A · ninguna D", "una letra concentra la mitad", 24),
    ("LC", "6", "seis A · ninguna B", "una letra concentra más de la mitad", 24),
    ("SOC", "3", "A 5 · B 0 · C 3 · D 2", "la A concentra la mitad; no hay B", 47),
    ("SOC", "4", "A 4 · B 5 · C 0 · D 1", "la B concentra la mitad; no hay C", 60),
    ("SOC", "5", "A 3 · B 3 · C 2 · D 2", "equilibrado", 70),
    ("SOC", "6", "A 0 · B 4 · C 4 · D 2", "no hay A", 85),
    ("BIO", "1", "A 3 · B 4 · C 2 · D 1", "la D sale una vez", 103),
    ("BIO", "2", "A 4 · B 1 · C 3 · D 2", "la B sale una vez", 112),
    ("BIO", "3", "A 1 · B 3 · C 3 · D 3", "la A sale una vez", 118),
    ("BIO", "4", "A 5 · B 1 · C 3 · D 1", "la A concentra la mitad", 124),
    ("BIO", "5", "A 3 · B 2 · C 2 · D 3", "equilibrado", 139),
    ("BIO", "6", "A 4 · B 3 · C 1 · D 2", "la C sale una vez", 147),
    ("QUI", "1", "A 3 · B 2 · C 3 · D 2", "equilibrado", 156),
    ("QUI", "2", "A 3 · B 4 · C 1 · D 2", "la C sale una vez", 166),
    ("QUI", "3", "A 3 · B 3 · C 2 · D 2", "equilibrado", 177),
    ("QUI", "4", "A 2 · B 2 · C 3 · D 3", "equilibrado", 187),
    ("QUI", "5", "A 4 · B 1 · C 3 · D 2", "la B sale una vez", 198),
    ("QUI", "6", "A 3 · B 3 · C 3 · D 1", "la D sale una vez", 211),
    ("FIS", "1", "A 3 · B 4 · C 2 · D 1", "la D sale una vez", 222),
    ("FIS", "2", "A 2 · B 2 · C 4 · D 2", "equilibrado", 230),
    ("FIS", "3", "A 3 · B 5 · C 1 · D 1", "la B concentra la mitad", 235),
    ("FIS", "5", "A 4 · B 3 · C 2 · D 1", "la D sale una vez", 251),
    ("FIS", "6", "A 1 · B 2 · C 4 · D 3", "la A sale una vez", 258),
    ("ING", "1", "Parte 1 en orden alfabético", "se acierta marcando «en orden»", 260),
    ("ING", "2", "A 4 · B 3 · C 3 (tres opciones)", "7 de 10 claves son la única que empieza por «Yes»", 271),
    ("ING", "3", "A 13 · B 11 · C 15 (39 espacios)", "equilibrado", 285),
    ("ING", "4", "A 6 · B 4 · C 6 (tres opciones)", "equilibrado", 296),
    ("ING", "5", "A 5 · B 4 · C 3 · D 4", "Bloque 1: C A D B C A D B, se repite cada cuatro", 303),
    ("ING", "6", "A 6 · B 9 · C 7 · D 2", "el Bloque 3 no tiene A ni D (cinco C y tres B)", 318),
]


# ─────────── fuentes ICFES (informativo) ───────────
# (fuente, ítem, qué pasa, efecto, n)
ICFES = [
    ("Cuadernillo Saber 11 2016-1, 1.ª sesión", "N.º 94 (Ciencias Naturales)",
     "El esquema dice «Sustracción del oxígeno disuelto para tomar fosfatos y nitratos», explicación "
     "química imprecisa (el oxígeno lo gasta la descomposición de la materia orgánica). La opción "
     "correcta es además la más larga.", "No cambia la clave (C).", 120),
    ("Cuadernillo Saber 11 2016-1, 1.ª sesión", "N.º 92 (Ciencias Naturales)",
     "La tabla le da al ácido sulfúrico una densidad de 2,7 g/mL (la real es 1,84; 2,7 es la del "
     "aluminio) y al ácido clorhídrico un punto de ebullición de 48 °C (corresponde a una solución "
     "concentrada, no al HCl puro).", "No cambia la clave (B).", 189),
    ("Cuadernillo Saber 11 2016-1, 1.ª sesión", "N.º 113 (Ciencias Naturales)",
     "En la gráfica C la mezcla 1 no tiene barra (pH 0 o dato faltante). El enunciado dice «tiene la "
     "hipótesis que» (falta «de»).", "No cambia la clave (D).", 180),
    ("Cuadernillo Saber 11 2016-1, 2.ª sesión", "N.º 58 (Ciencias Naturales)",
     "En la tabla, con los insecticidas 1, 2 y 3 sobreviven más cucarachas (90, 80 y 70 %) que sin "
     "insecticida (50 %).", "No cambia la clave (C); es un dato llamativo que conviene comentar.", 104),
    ("Cuadernillo Saber 11 2016-1, 2.ª sesión", "N.º 67 (Ciencias Naturales)",
     "La tabla pone «Gas natural · Propano (C3H8)»: el gas natural es sobre todo metano (CH4).",
     "No cambia la clave (A).", 121),
    ("Cuadernillo Saber 11 2016-1, 2.ª sesión", "N.º 65 (Ciencias Naturales)",
     "La tabla llama «neutro» a la leche (pH 6,8) y al gel (7,2), y la clave fija lo neutro «entre 6,8 y "
     "7,2». En química, neutro es pH 7 a 25 °C.", "No cambia la clave (B).", 179),
    ("Cuadernillo Saber 11 2016-1, 2.ª sesión", "N.º 54 (Ciencias Naturales)",
     "Dice que el imán «atrae elementos metálicos» (no todos: aluminio y cobre no) y escribe «metalicos» "
     "sin tilde.", "No cambia la clave (A).", 190),
    ("Cuadernillo Saber 11 2016-1, 2.ª sesión", "N.º 24 (Sociales y Ciudadanas)",
     "La opción D, que parece la correcta, empieza con «No» y da una razón de «Sí».",
     "Posible error de redacción.", 82),
    ("Cuadernillo Saber 11 2016-1, 2.ª sesión", "N.º 112 a 116 (Inglés, Parte 6, «Television»)",
     "«…since watching TV with them it is not real interaction» (sobra «it»); los apóstrofos van "
     "impresos como acento grave («Let`s», «Here`s»).", "Las cinco claves se sostienen.", 313),
    ("Cuadernillo de Inglés 2024", "Examen 2, Parte 6, pregunta 21",
     "La tabla oficial de respuestas da A («how to grow coffee on the farm»), pero el texto no dice cómo "
     "se cultiva el café; dice qué incluye el precio («This includes three home-cooked meals a day, a "
     "swimming pool…»): la respuesta es C.", "Clave oficial errada.", 307),
    ("Cuadernillo de Inglés 2024", "Examen 2, Parte 6, texto de la pregunta 20",
     "El texto «Jonathan's trip to Colombia» trae doce erratas: Faador (Ecuador), Cdombia y Cambia "
     "(Colombia), caled Perera (called Pereira), midde, valey, indudes, pod (pool), dork (drink), reston "
     "(rest on), arcund, wildife, Vila.", "Erratas de impresión.", 308),
    ("Cuadernillo de Inglés 2024", "Examen 1, Parte 6, texto de la pregunta 25",
     "«It left as if it was cut just a minute before I opened it»: debe ser «It felt as if».",
     "No cambia la clave (C).", 309),
    ("Cuadernillo de Inglés 2024", "Examen 1, Parte 1",
     "El tema se titula «Clothes and accesories» (errata: accessories).", "Errata.", 265),
    ("Cuadernillo de Inglés 2024", "Examen 2, Parte 1 (preguntas 1 a 3)",
     "La instrucción dice «Sobran dos palabras más», pero con 3 descripciones y 7 palabras sobran cuatro.",
     "Instrucción inexacta.", 266),
    ("Cuadernillo de Inglés 2024", "Examen 1, Parte 3",
     "Anuncia «preguntas 7 y 8», pero las imprime como «6.» y «7.». La tabla de respuestas usa la "
     "numeración correcta (7 · C, 8 · B).", "Quien coteje por el número impreso cruza las claves.", 275),
    ("Cuadernillo de Inglés 2024", "Examen 2, Parte 4, texto de la pregunta 10",
     "Numera «(4)» el último espacio, que es la pregunta 14.", "Errata de numeración.", 330),
    ("SIMULACRO II 2023 (Química)", "N.º 9, tabla 2",
     "Llama «capacidad calorífica» a un dato en MJ/kg y lo define como «energía necesaria para aumentar "
     "un grado centígrado la temperatura del combustible». Por unidades y valores (39,5 y 45,4 MJ/kg) es "
     "el poder calorífico.", "No cambia la clave (C).", 199),
    ("SIMULACRO II 2023 (Química)", "N.º 252",
     "La tabla da 0 g/kg de CO₂ a 80 °C; el valor real es pequeño pero no cero.",
     "No cambia la clave (D).", 158),
    ("SIMULACRO II 2023 (Química)", "N.º 67",
     "La tabla no trae la unidad del tiempo (la opción A habla de segundos); la clave B es la menos mala "
     "más que una conclusión fuerte.", "Ítem débil.", 168),
    ("SIMULACRO II 2023 (Química)", "N.º 274, opción D",
     "La D («la glucosa tiene menor contenido energético, porque la entalpía de combustión es menor») "
     "tiene la primera mitad cierta y la razón depende de cómo se lea el signo (−2.816 es mayor que "
     "−2.827, pero menor en tamaño). La comparación es por mol.", "Distractor ambiguo; clave A.", 212),
    ("SIMULACRO II 2023 (Inglés)", "Parte 2, grupos 61–65, 81–85, 86–90 y N.º 66",
     "Erratas: ejemplo sin punto final (86–90), «you cook this and have it lot» (84), instrucción «En las "
     "preguntas 41 - 45» y opción «chickern» (61–65), «Dock» por «Clock» (66).", "Erratas.", 267),
    ("SIMULACRO II 2023 (Inglés)", "Parte 6, N.º 379 a 454",
     "Todos los textos de la Parte 6 traen al menos una errata, por ejemplo «you.Spend», «ZCollect "
     "flags», «Sandra’s’», «Also, I if I won», «decription», «south Africa», «Jhons», «magnificient», "
     "«responsability». En el N.º 380: «avaluable metal», «to say with them»; en el N.º 394: «I will "
     "dress success» (falta «for»).", "Erratas de digitación.", 310),
    ("SIMULACRO II 2023 (Inglés)", "N.º 230 a 237, 446 a 449 y 450 a 454",
     "Repiten textos del cuadernillo de Inglés 2024 («Coffee», «Swift Pizza», «Jonathan»), con otras "
     "erratas.", "No son preguntas independientes.", 331),
    ("Cuadernillos de Lectura Crítica 2026", "16 feb y 9 sept 2026",
     "Los dos cuadernillos traen las mismas preguntas con cambios menores de redacción, como los de "
     "Ciencias Naturales 2025 y 2026.", "Cuentan como un solo banco.", 345),
]
