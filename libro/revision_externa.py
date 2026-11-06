# -*- coding: utf-8 -*-
"""Hallazgos de los seis docentes que revisaron el libro fuente, normalizados
   contra nuestro propio registro.

   Fuente: seis archivos «Matriz de Hallazgos» entregados el 24 de octubre de 2026
   (Lectura Crítica fechada «oct-26»; Química trae «24 de noviembre de 2026», que
   es seguramente un lapsus de digitación y se anota tal cual).

   Una sola verdad: de aquí salen la pestaña del xlsx y la sección del tablero.

   TIPO: taxonomía compartida con nuestro registro, para poder cruzar.
     CLAVE       clave errada, doble o que no se deduce
     EVIDENTE    la respuesta se lee en el contexto o en la página
     FORMA       se adivina por la forma: extensión, palabra absoluta, letra fija
     DISTRACTOR  distractores de fácil descarte
     COMPETENCIA la pregunta no corresponde a la competencia o componente rotulado
     CONTEXTO    falta el texto base o un dato indispensable
     CONCEPTO    error conceptual en el contexto o en la opción correcta
     FUENTE      dato, cifra o fecha sin verificar
     GRAFICO     tabla, imagen o diagrama innecesario o mal construido
     NIVEL       nivel de desempeño 1 o 2: memoria o paráfrasis
     DUPLICADA   dos preguntas piden lo mismo, o una anticipa la respuesta de otra
     EDICION     ortografía, tipografía, contraste, numeración
     TEORIA      falta contenido teórico que la prueba sí evalúa
"""

REVISORES = [
    # area, grado, docente, fecha, rango de páginas, cuántos hallazgos
    ("Lectura Crítica",  "11", "Lic. Vanessa Hurtado",           "oct-26",      "16–70",   24),
    ("Ciencias Sociales", "11", "Gilberto Almanza Morales",       "24-oct-2026", "79–130",   9),
    ("Biología",         "11", "Rodolfo Mejía Meza",             "24-oct-2026", "78–136",  54),
    ("Matemáticas",      "10", "Alexander Castro Bowen",         "24-oct-2026", "9–72",    18),
    ("Química",          "10", "Haider Alfonso Jiménez Vargas",  "24-nov-2026", "148–208",  8),
    ("Inglés",           "10", "Diana Campo Martínez",           "24-oct-2026", "148–214",  7),
]

# (área, grado, pág. del revisor, ítem, qué reporta, tipo, cruce con nuestro registro)
FILAS = [
 # ───────────────────────── Lectura Crítica · grado 11 · Vanessa Hurtado
 ("Lectura Crítica","11","16","7 a 10","El texto para las preguntas 7 a 10 está incompleto","CONTEXTO","Nuevo · no lo vimos"),
 ("Lectura Crítica","11","16","—","«dudarlo» debe ser «dudar» y falta completar la penúltima línea del primer párrafo","EDICION","Nuevo"),
 ("Lectura Crítica","11","17","—","La franja SpaceGec escribe «quince» donde debería ir «15»","EDICION","Nuevo"),
 ("Lectura Crítica","11","24","—","Falta la tilde de «Cómo» en la instrucción 1 de Actividad en el aula","EDICION","Nuevo"),
 ("Lectura Crítica","11","27","—","La franja SpaceGec escribe «quince» donde debería ir «15»","EDICION","Nuevo"),
 ("Lectura Crítica","11","28","—","Al último párrafo del compendio de la misión le falta una «a»","EDICION","Nuevo"),
 ("Lectura Crítica","11","29","modelo","El título de la pregunta modelo debería nombrar el fragmento: John Stuart Mill sobre la libertad","EDICION","Nuevo"),
 ("Lectura Crítica","11","30","—","El recuadro Objetivo no dice qué se busca: debe hablar de seguir el hilo argumentativo","EDICION","Nuevo"),
 ("Lectura Crítica","11","33","—","En la definición de marcadores textuales falta una coma y «Funcionan» va en minúscula","EDICION","Nuevo"),
 ("Lectura Crítica","11","40","modelo","En las opciones B y C la cifra está separada del signo de porcentaje","EDICION","Nuevo"),
 ("Lectura Crítica","11","41","—","El recuadro de instrucción no dice qué hacer: «Lee el enunciado y completa las actividades»","EDICION","Nuevo"),
 ("Lectura Crítica","11","42","modelo","Comillas mal puestas en la opción B del recuadro de anatomía de la respuesta","EDICION","Nuevo"),
 ("Lectura Crítica","11","42","modelo","La opción A del análisis de distractores va en otro tamaño de fuente","EDICION","Nuevo"),
 ("Lectura Crítica","11","45","—","La instrucción rotulada «Responde» está en el punto equivocado de la actividad","EDICION","Nuevo"),
 ("Lectura Crítica","11","46","—","El segundo recuadro de la infografía de IA es poco legible por el contraste del color","EDICION","Reg. 28 · mismo defecto en nuestras hojas"),
 ("Lectura Crítica","11","48","—","La franja SpaceGec escribe «quince» donde debería ir «15»","EDICION","Nuevo"),
 ("Lectura Crítica","11","53","—","El recuadro que invita a revisar la bitácora va en la página siguiente","EDICION","Nuevo"),
 ("Lectura Crítica","11","56","—","«playlist» debe ir en cursiva por ser extranjerismo","EDICION","Nuevo"),
 ("Lectura Crítica","11","57","4 y 5","En la caricatura, el cartel amarillo corta las palabras: hay que rediseñarlo","EDICION","Reg. 23 · mismo defecto en nuestras hojas"),
 ("Lectura Crítica","11","59","—","La franja SpaceGec escribe «quince» donde debería ir «15»","EDICION","Nuevo"),
 ("Lectura Crítica","11","63","—","Las dos etiquetas «tu tarea» de la página no tienen el mismo tamaño de fuente","EDICION","Nuevo"),
 ("Lectura Crítica","11","67","—","No se entiende el subtítulo «preguntas para el libro» y las preguntas aluden a un texto que no está en el material","CONTEXTO","Nuevo · hallazgo de fondo"),
 ("Lectura Crítica","11","69","6 y 7","Sobra la tilde de «él» en la tercera línea del texto","EDICION","Nuevo"),
 ("Lectura Crítica","11","70","—","La franja SpaceGec escribe «quince» donde debería ir «15»","EDICION","Nuevo"),

 # ───────────────────────── Ciencias Sociales · grado 11 · Gilberto Almanza
 ("Ciencias Sociales","11","79","—","En los ejemplos del Pilar 2 falta el Referendo, que es el mecanismo de participación que más pregunta el ICFES","TEORIA","Nuevo"),
 ("Ciencias Sociales","11","81","—","La palabra «este» se repite dos veces en la formulación de la pregunta","EDICION","Nuevo"),
 ("Ciencias Sociales","11","85","modelo","El contexto de la pregunta modelo no corresponde al debate actual: es un debate de 2008","FUENTE","Nuevo"),
 ("Ciencias Sociales","11","92","7","La expresión «derechos de los animales» en el contexto de la pregunta 7 está mal planteada","CONCEPTO","Es nuestra pág. 348 · desfase +256 confirmado"),
 ("Ciencias Sociales","11","93","9","La pregunta 9 no obedece a la competencia de análisis de perspectivas que propone la misión 2","COMPETENCIA","Coincide con nuestra clasificación: la leímos como PS, no IP"),
 ("Ciencias Sociales","11","117","8","«La Tención» en la opción B debe ser «La discrepancia»","EDICION","Nuevo"),
 ("Ciencias Sociales","11","130","10","«Estados occidentales y suroccidentales» debe ser «los departamentos del Chocó, Cauca y Nariño»","CONCEPTO","Nuevo"),
 ("Ciencias Sociales","11","toda el área","—","Las respuestas correctas son por lo general las de mayor número de caracteres. El revisor lo anota como «(patrón IA)»","FORMA","Reg. 24 y Reg. 31 · converge con lo nuestro"),
 ("Ciencias Sociales","11","toda el área","—","Solo se evidencian niveles de dificultad 1 y 2: mera interpretación y paráfrasis entre el contexto y la opción","NIVEL","Nuevo · lo mismo dice el revisor de Biología"),

 # ───────────────────────── Biología · grado 11 · Rodolfo Mejía · M1 celular
 ("Biología","11","78","1","El modelo trae indicaciones muy evidentes; el diagrama debería mostrar estado inicial y final","EVIDENTE","Familia Reg. 11"),
 ("Biología","11","79","5","La sigla RER no se introduce desde el párrafo","CONTEXTO","Nuevo"),
 ("Biología","11","79","6","Información insuficiente para establecer la relación causa-efecto entre factores y actividad genética","CONTEXTO","Nuevo"),
 ("Biología","11","79","7","Competencia incorrecta: el enunciado corresponde a explicación de fenómenos","COMPETENCIA","Familia Reg. 34 · rótulos del banco"),
 ("Biología","11","79","8","La gráfica de glóbulos rojos es un estímulo innecesario, no aporta para responder","GRAFICO","Nuevo"),
 ("Biología","11","79","9","La opción correcta es la más extensa y los estudiantes se sesgan por el número de renglones","FORMA","Reg. 24 · converge"),
 ("Biología","11","79","10","«cisterna» es palabra poco común, la correcta es la más extensa y el contexto del bloque no se requiere","FORMA","Reg. 24 · converge"),
 # M2 organísmico
 ("Biología","11","89","1","El diagrama maneja simbología inadecuada para mostrar la disminución","GRAFICO","Nuevo"),
 ("Biología","11","89","2","Contexto insuficiente y la opción correcta no responde lo que pregunta el enunciado","CONTEXTO","Familia Reg. 14"),
 ("Biología","11","89","3","Contexto insuficiente y distractores de fácil descarte (B y D)","DISTRACTOR","Nuevo"),
 ("Biología","11","89","4","La opción correcta repite casi textualmente el contexto; distractores de fácil descarte","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Biología","11","90","5","Enunciado ambiguo: pide la variable que se modifica primero como señal, y la urea es respuesta, no señal","CONCEPTO","Familia Reg. 3"),
 ("Biología","11","90","6","Distractores de fácil descarte y la palabra «garantiza» en la opción correcta","FORMA","Reg. 33 · mismo defecto en nuestras hojas"),
 ("Biología","11","90","7","Datos poco plausibles en la tabla, la correcta no se deduce de ellos y la columna de glucosa no se usa","FUENTE","Familia Reg. 1"),
 ("Biología","11","91","8","Doble marcación de la clave (A y B) y la tabla no se requiere para responder","CLAVE","Reg. 2 · mismo defecto"),
 ("Biología","11","91","9","Pregunta de nivel 1: se responde de memoria","NIVEL","Nuevo"),
 ("Biología","11","91","10","Error conceptual en el contexto: la insulina evita la hiperglucemia, no la hipoglucemia","CONCEPTO","Nuevo"),
 # M3 ecosistémico
 ("Biología","11","100","1","Respuesta muy evidente, la tabla no se requiere y va sin unidades","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Biología","11","101","2","Distractor de fácil descarte: los sensores se repiten como distractor en las preguntas 2, 3 y 4","DISTRACTOR","Nuevo"),
 ("Biología","11","101","3","Pregunta similar a la 2 y enunciado poco preciso: las opciones son afirmaciones, no aplicaciones","DUPLICADA","Reg. 12, 25, 26 · mismo defecto"),
 ("Biología","11","101","4","Respuesta muy evidente y distractores de fácil descarte: el dato va en el enunciado","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Biología","11","102","5","Las flechas de la cadena trófica apuntan en la dirección equivocada (aplica también a la 6)","GRAFICO","Nuevo · hallazgo de fondo"),
 ("Biología","11","102","7","La pregunta no corresponde al componente biológico","COMPETENCIA","Familia Reg. 34"),
 ("Biología","11","103","8","Error de digitación en la opción D («nitrógeno..»)","EDICION","Familia Reg. 5"),
 ("Biología","11","103","9","La pregunta 8 brinda la respuesta de la pregunta 9","DUPLICADA","Reg. 25 · mismo defecto"),
 ("Biología","11","103","10","«diversidad» no corresponde a los datos: la tabla muestra abundancia y grupos funcionales","CONCEPTO","Nuevo"),
 # M4 CTS
 ("Biología","11","110","1","Respuesta muy evidente: la opción correcta repite palabras del contexto","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Biología","11","111","2","Respuesta evidente, nivel 1, y el enunciado admite más de una opción correcta (A y B también)","CLAVE","Reg. 2 · mismo defecto"),
 ("Biología","11","111","3","El enunciado se asocia más con ciencias sociales que con ciencias naturales","COMPETENCIA","Nuevo"),
 ("Biología","11","111","4","Distractores de fácil descarte: la médula espinal se descarta sin conocimiento biológico","DISTRACTOR","Nuevo"),
 ("Biología","11","112","5","Opción más extensa, respuesta explícita y un dato del contexto por verificar (cápsulas desde 30 km)","FORMA","Reg. 24 · converge"),
 ("Biología","11","112","6","Distractores de fácil descarte","DISTRACTOR","Nuevo"),
 ("Biología","11","112","7","No corresponde al componente biológico y la opción correcta no coincide con el contexto","COMPETENCIA","Familia Reg. 34"),
 ("Biología","11","113","8","Opción más extensa y error conceptual en la correcta: falta el grupo de comparación","CONCEPTO","Nuevo"),
 ("Biología","11","113","9","Nivel de desempeño 1 aunque el contexto use lenguaje científico; la correcta repite el contexto","NIVEL","Nuevo"),
 ("Biología","11","113","10","«linfocito» no se introduce y la pregunta 9 da la respuesta de la 10","DUPLICADA","Reg. 25 · mismo defecto"),
 # M5 genética
 ("Biología","11","122","1","Simbología inadecuada: el pedigrí va sin parejas en las generaciones 2 y 3","GRAFICO","Nuevo · hallazgo de fondo"),
 ("Biología","11","123","2","Respuesta muy evidente: la opción correcta repite palabras del contexto","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Biología","11","123","4","Doble marcación de la clave (A y C) y distractor de fácil descarte","CLAVE","Reg. 2 · mismo defecto"),
 ("Biología","11","123","5","Error conceptual: los estudios en hijos de sobrevivientes de Hiroshima no hallaron más mutaciones heredadas","CONCEPTO","Nuevo · hallazgo de fondo"),
 ("Biología","11","124","6","Falta el texto base: la pregunta menciona una información y una predicción que no aparecen en el libro","CONTEXTO","Igual que Lectura Crítica pág. 16 y 67"),
 ("Biología","11","124","7","Respuesta muy evidente: información repetida en el contexto","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Biología","11","124","8","Respuesta muy evidente y distractores de fácil descarte","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Biología","11","125","9","La correcta repite el contexto, «híbrido» está mal usado y la afirmación sobre enfermedades no tiene fuente","FUENTE","Reg. 31 · referencias sin verificar"),
 ("Biología","11","125","10","Los distractores se descartan por la forma: «asegura», «garantiza», «definitiva»","FORMA","Reg. 33 · mismo defecto en nuestras hojas"),
 # M6 evolución
 ("Biología","11","133","1","Error conceptual: el cambio es ambiental en seis meses, no evolutivo, y el contexto contradice el estudio citado","CONCEPTO","Nuevo · hallazgo de fondo"),
 ("Biología","11","134","2","La opción correcta no coincide con la tabla: el autocontrol es alto en ambos grupos","CLAVE","Reg. 1 · mismo defecto"),
 ("Biología","11","134","3","Pregunta similar a la 2 y «adaptación» mal usado para un cambio de seis meses","DUPLICADA","Reg. 12 · mismo defecto"),
 ("Biología","11","134","5","Respuesta muy evidente y fecha por verificar: la declaratoria de extinción se ubica en 2016 o 2019, no en 2015","FUENTE","Nuevo"),
 ("Biología","11","135","6","Respuesta muy evidente y distractores de fácil descarte","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Biología","11","135","7","La tabla no se requiere para responder: la conclusión va en el contexto","GRAFICO","Nuevo"),
 ("Biología","11","136","8","Distractores de fácil descarte y «proceso» por «característica»","DISTRACTOR","Nuevo"),
 ("Biología","11","136","9","Respuesta muy evidente: el enunciado ya trae la retención hídrica y el refugio","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Biología","11","136","10","Pregunta similar a la 7 y «demuestra» debería ser «es consistente con»","DUPLICADA","Reg. 12 · mismo defecto"),

 # ───────────────────────── Matemáticas · grado 10 · Alexander Castro
 ("Matemáticas","10","9","—","El vocabulario dice «fórmula para variación lineal»: debe ser «expresión algebraica de la función lineal», y la tasa de cambio ligarse a la pendiente","TEORIA","Nuevo"),
 ("Matemáticas","10","10","—","Hay que relacionar «acelera» y «desacelera» con la razón de cambio para no parecer física aislada","TEORIA","Nuevo"),
 ("Matemáticas","10","13","—","Sobran los paréntesis del ejemplo","EDICION","Nuevo"),
 ("Matemáticas","10","16","—","Falta identificar «misión 1» en la parte superior","EDICION","Nuevo"),
 ("Matemáticas","10","20","modelo","Falta apunte teórico a las desigualdades: la pregunta modelo también se resuelve con mayor que y menor que","TEORIA","Nuevo"),
 ("Matemáticas","10","28","8","Error en la respuesta marcada: la correcta es B. Además la C le falta inicio y su razón está mal planteada","CLAVE","Reg. 3 · mismo defecto, otro grado"),
 ("Matemáticas","10","29","—","«medidas métricas» es redundante y no todas las mediciones se obtienen aplicando fórmulas","CONCEPTO","Nuevo"),
 ("Matemáticas","10","39","4","Sobra una longitud de 120 cm debajo del módulo x","GRAFICO","Familia Reg. 1"),
 ("Matemáticas","10","41","8","La imagen dice «baños» y el contexto «baño»: le quita rigurosidad a la imagen que da la respuesta","EDICION","Reg. 4 · mismo defecto"),
 ("Matemáticas","10","41","8","La imagen no alude a los accesos directos que el estudiante debe deducir: falta una leyenda","GRAFICO","Nuevo"),
 ("Matemáticas","10","41","10","El área del salón de música es 48 − 32 = 16 m²: el cálculo del libro no da","CLAVE","Reg. 8 · mismo defecto"),
 ("Matemáticas","10","42","—","El glosario debería incluir congruencia","TEORIA","Nuevo"),
 ("Matemáticas","10","componente","—","En el componente geométrico-métrico faltan las razones trigonométricas y los teoremas del seno y coseno, que la prueba sí evalúa","TEORIA","Nuevo · hallazgo de fondo"),
 ("Matemáticas","10","56","—","La bitácora habla de «LA MEDIDA» de tendencia central y se lee como si fuera la única","EDICION","Nuevo"),
 ("Matemáticas","10","componente","—","En el componente aleatorio no hay referente teórico de combinatoria y sí hay preguntas del tema en la misión","TEORIA","Nuevo · hallazgo de fondo"),
 ("Matemáticas","10","70","2","La respuesta correcta es la A: es una combinación","CLAVE","Reg. 3 · mismo defecto, otro grado"),
 ("Matemáticas","10","70","3","La respuesta correcta es la D: hay que aplicar la definición de probabilidad","CLAVE","Reg. 3 · mismo defecto, otro grado"),
 ("Matemáticas","10","72","9","La respuesta correcta es la C: total de combinaciones del mismo color sobre el total de gatos","CLAVE","Reg. 3 · mismo defecto, otro grado"),

 # ───────────────────────── Química · grado 10 · Haider Jiménez
 ("Química","10","148","—","La tabla periódica no deja ver la masa atómica, aunque el libro afirma que la resalta","GRAFICO","Nuevo · el libro se contradice"),
 ("Química","10","152","—","En el párrafo final la palabra «MISIÓN» tiene las letras separadas","EDICION","Nuevo"),
 ("Química","10","154","1","No se dice que el aluminio se calienta en el crisol, aunque el análisis de distractores de la pág. 156 sí lo menciona","CONTEXTO","Nuevo"),
 ("Química","10","155","—","La actividad dice que «el color rojo es una representación didáctica» y el color impreso es amarillo","GRAFICO","Nuevo"),
 ("Química","10","156","—","Falta un dato por fila para poder resolver la tabla con la expresión de densidad","CONTEXTO","Familia Reg. 1"),
 ("Química","10","162","7","La respuesta a la pregunta 7 salta a la vista","EVIDENTE","Reg. 11 · mismo defecto"),
 ("Química","10","194","—","En el contexto aparece «elpersonalagrega» sin separar","EDICION","Nuevo"),
 ("Química","10","208","—","El contexto no define las condiciones del sistema A, solo las del B","CONTEXTO","Nuevo"),

 # ───────────────────────── Inglés · grado 10 · Diana Campo
 ("Inglés","10","148","—","Las respuestas vienen suministradas por el texto al pie de la página de actividades","EVIDENTE","Reg. 15 · mismo defecto en nuestras hojas"),
 ("Inglés","10","150","—","Todas las opciones correctas están en la A","FORMA","Reg. 24 · converge"),
 ("Inglés","10","180","—","La rejilla indica A pero ninguna opción es correcta: la respuesta es WAS TALKING, no «were talking»","CLAVE","Reg. 1 · mismo defecto, otro grado"),
 ("Inglés","10","181","—","Todos los textos usan el mismo tiempo gramatical: no se sale del pasado simple","TEORIA","Nuevo"),
 ("Inglés","10","208","4","La actividad pide escribir un texto en un solo tiempo gramatical: enseña una escritura plana","TEORIA","Nuevo"),
 ("Inglés","10","213","—","En el bloque 2 los números de pregunta del texto no coinciden con los de abajo","EDICION","Reg. 4 · mismo defecto"),
 ("Inglés","10","214","—","En el bloque 3 los números de pregunta del texto no coinciden con los de abajo","EDICION","Reg. 4 · mismo defecto"),
]

# ──────────────────────────────────────────────────────────────────────────────
# Lectura del cruce, tipo por tipo. «mios» cuenta nuestros registros del libro
# fuente (no los nuestros de producción, que son otra cosa).
NOMBRE_TIPO = {
 "CLAVE":"Clave errada, doble o que no se deduce",
 "EVIDENTE":"La respuesta se lee en el contexto",
 "FORMA":"Se adivina por la forma: extensión, palabra absoluta, letra fija",
 "DISTRACTOR":"Distractores de fácil descarte",
 "COMPETENCIA":"No corresponde a la competencia o componente rotulado",
 "CONTEXTO":"Falta el texto base o un dato indispensable",
 "CONCEPTO":"Error conceptual en el contexto o en la clave",
 "FUENTE":"Dato, cifra o fecha sin verificar",
 "GRAFICO":"Tabla, imagen o diagrama innecesario o mal construido",
 "NIVEL":"Nivel de desempeño 1 o 2: memoria o paráfrasis",
 "DUPLICADA":"Dos preguntas piden lo mismo, o una anticipa a otra",
 "EDICION":"Ortografía, tipografía, contraste, numeración",
 "TEORIA":"Falta contenido teórico que la prueba sí evalúa",
}

# tipo -> (nuestros registros de ese tipo, lectura del cruce)
CRUCE = {
 "CLAVE": ([1,2,3,4,8],
   "Los dos lados encontramos lo mismo en áreas distintas: nosotros cinco claves que no cierran "
   "en Matemáticas 11, los revisores cinco en Matemáticas 10, una en Inglés y cuatro en Biología "
   "(tres con doble marcación). Quince claves en total. No es el descuido de un autor: el libro "
   "salió sin una pasada de resolución pregunta por pregunta."),
 "EVIDENTE": ([11,27],
   "Nosotros lo vimos dos veces en Lectura Crítica. Biología lo reporta once veces y Química una. "
   "Es el defecto más repetido de todo el libro."),
 "FORMA": ([24],
   "Convergencia fuerte y por tres caminos independientes: nosotros, que la letra A concentra la "
   "mitad de las claves de Lectura Crítica; Inglés, que TODAS sus correctas son A; y Sociales y "
   "Biología, que la correcta es casi siempre la opción más larga. El revisor de Sociales lo "
   "escribe sin rodeos: «(patrón IA)»."),
 "DISTRACTOR": ([],
   "No lo registramos como categoría propia: lo leíamos dentro de «se puede defender otra». "
   "Biología lo reporta cinco veces, siempre en el mismo par de opciones. Hay que adoptar la categoría."),
 "COMPETENCIA": ([34],
   "Nosotros lo vimos en el rótulo de un ítem del banco ASED. Biología lo reporta cuatro veces y "
   "Sociales una, y en esa de Sociales habíamos clasificado la misma pregunta como pensamiento "
   "social cuando la misión la rotula como análisis de perspectivas. Dos lecturas independientes, "
   "la misma conclusión."),
 "CONTEXTO": ([14],
   "Tres revisores reportan preguntas que piden un texto o un dato que no está impreso: Lectura "
   "Crítica en las págs. 16 y 67, Biología en la 124 y Química en la 154, 156 y 208. Nosotros no "
   "lo vimos porque trabajamos sobre las preguntas ya montadas, no sobre el libro completo."),
 "CONCEPTO": ([],
   "Ocho casos de los revisores, varios serios: insulina e hipoglucemia al revés, mutaciones "
   "heredadas en Hiroshima, «diversidad» por «abundancia», un cambio ambiental presentado como "
   "evolutivo. Ninguno lo teníamos: se necesita ojo de especialista del área."),
 "FUENTE": ([31],
   "Nosotros encontramos las URL con «?utm_source=chatgpt.com» pegado. Los revisores encuentran "
   "cuatro datos sin respaldo: una fecha de extinción errada, cifras de orina poco plausibles, "
   "una afirmación sobre perros híbridos sin fuente y un dato de cápsulas lanzadas desde 30 km."),
 "GRAFICO": ([],
   "Nueve casos. Dos son de fondo: las flechas de la cadena trófica apuntan al revés y el pedigrí "
   "va sin parejas en dos generaciones. Y uno es el libro contradiciéndose: dice que su tabla "
   "periódica resalta la masa atómica, y la masa atómica no se ve."),
 "NIVEL": ([],
   "Dos revisores que no se conocen, en áreas distintas, dicen lo mismo: el libro se queda en "
   "niveles 1 y 2. Es el hallazgo más incómodo de todo el paquete, porque no se arregla "
   "corrigiendo preguntas una por una."),
 "DUPLICADA": ([12,17,25,26],
   "Nosotros cuatro pares en Lectura Crítica. Biología cinco, dos de ellos del tipo peor: la "
   "pregunta anterior le entrega la respuesta a la siguiente."),
 "EDICION": ([4,5],
   "Treinta y tres hallazgos, casi todos de Lectura Crítica. Nosotros no auditamos la tipografía "
   "del libro fuente: lo leímos para resolverlo. Este bloque es aporte limpio de los revisores."),
 "TEORIA": ([],
   "Ocho vacíos de contenido, siete de Matemáticas. Dos pesan: no hay teoría de combinatoria y sí "
   "hay preguntas de combinatoria; y falta trigonometría, que la prueba evalúa. Este es el "
   "hallazgo que más cuesta de arreglar y el que ningún corrector de estilo iba a ver."),
}

# Lo que vimos nosotros y ningún revisor mencionó.
SOLO_NOSOTROS = [
 ("Riesgo de lectura política", "Reg. 20, 21 y 32",
  "La columna sobre un expresidente vivo, los dos casos con el presidente actual y el coronel "
  "Plazas Vega con el Palacio de Justicia. Ningún revisor lo tocó. Sigue pendiente de la Gerencia."),
 ("Referencias generadas con IA sin limpiar", "Reg. 31",
  "Tres URL del libro traen «?utm_source=chatgpt.com» pegado. El revisor de Sociales llegó al "
  "mismo diagnóstico por otro camino, mirando la extensión de las respuestas."),
 ("El ASED reinicia la numeración por sección", "Reg. 34",
  "«Ítem 34» es una pregunta distinta en Lectura Crítica y en Sociales. Afecta a cómo citamos el banco."),
 ("Opciones que se niegan a sí mismas", "Reg. 18",
  "«Carece de parcialidad» usado para decir que algo es parcial. Es un error de lógica interna, "
  "no de redacción."),
 ("Defectos de nuestras propias hojas", "Reg. 13, 15, 16, 23, 28 y 33",
  "Seis, los seis corregidos y verificados. Tres de ellos son el mismo defecto que los revisores "
  "le encontraron al libro fuente: contraste ilegible, palabras cortadas por desborde y la pista "
  "que delata la respuesta."),
]
