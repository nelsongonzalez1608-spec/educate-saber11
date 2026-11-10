# Hojas de simulacro · ¿sirven los esquemas para cualquier pregunta del área?

Análisis y rediseño · 10 nov 2026 · para Nelson González

> «El diseño de las páginas en blanco me gustó, pero estaba un poco cerrado. […] la idea es que
> sirvan para socializar cualquier pregunta de esa área. No sé si está muy, muy limitada. Quiero
> que analicen eso.» — Nelson

## La respuesta corta

Sí, estaba cerrado. Clasificamos **181 preguntas reales** de las siete áreas (cuadernillos oficiales,
pruebas de campo del libro, preguntas ICFES ya usadas en el cuaderno y un PTD de Sociales) y pusimos
cada esquema de la versión 1 frente a cada una:

| | Sirve | A medias | No sirve | Muestra |
|---|---|---|---|---|
| Matemáticas | 2 | 13 | 15 | 30 |
| Lectura Crítica | 2 | 15 | 11 | 28 |
| Sociales y Ciudadanas | 5 | 8 | 13 | 26 |
| Biología | 8 | 13 | 3 | 24 |
| Química | 0 | 13 | 11 | 24 |
| Física | 12 | 6 | 6 | 24 |
| Inglés | 7 | 7 | 11 | 25 |
| **Total** | **36 (20 %)** | **75 (41 %)** | **70 (39 %)** | **181** |

El patrón es el mismo en las siete áreas: **cada esquema de la v1 dibujaba UN tipo de pregunta**, el
que salta a la vista cuando uno piensa en el área (Química → una reacción; Sociales → actores en
conflicto; Inglés → un hueco en una frase; Matemáticas → una cuenta). Pero el Saber 11 pregunta de
muchas formas, y las formas que la v1 no veía son justo las más frecuentes en los cuadernillos
oficiales: en Matemáticas, **validar una afirmación o un procedimiento** («¿es correcta?, sí,
porque…») es 1 de cada 4 preguntas; en Química, **clasificar o identificar** y **diseño
experimental** son casi la mitad y en ninguna «se transforma» nada; en Sociales, **reconocer el
concepto o la norma** (oferta y demanda, neoliberalismo, un mecanismo de participación) es la pregunta
más común del PTD 7 y no tiene voces.

La v2 deja de adivinar el tipo de pregunta: **le pide al estudiante que lo reconozca** (que es, además,
la primera habilidad que mide el examen) y le da una caja de herramientas del área para trabajarlo.

## Fuentes y cómo se armó la muestra

| Sigla | Fuente | Qué se usó |
|---|---|---|
| CM26 | `fuente_icfes/09-Marzo_Cuadernillo-de-Preguntas-Matematicas-Saber-11-2026.pdf` (50 preguntas) | 25 preguntas, escogidas para cubrir todos los tipos |
| CLC26 | `fuente_icfes/16-feb-cuadernillo-de-preguntas-lectura-critica-saber-11-2026.pdf` | 23 preguntas. **Atención:** el cuadernillo del 9 sept trae las mismas preguntas con retoques de redacción (igual que Ciencias 2025 = 2026) |
| CCN | `fuente_icfes/24-feb-cuadernillo-preguntas-ciencias-naturales-saber-11-2026.pdf` (= 2025) | 16 de Biología, 18 de Química y 16 de Física, clasificadas por su contenido |
| CI24 | `fuente_icfes/16-octubre-cuadernillo-ingles-saber-11-2024.pdf`, examen 1 | 15 preguntas de las 7 partes |
| SIM | `fuente_icfes/SIM_II_2023_OFICIO_INGLES.pdf` | 3 preguntas (partes de avisos, léxico y conversación) |
| PTD7 | «SOCIALES PTD7.pptx» (Drive de Nelson, solo lectura) | 8 de sus 15 preguntas |
| Libro | `fuente_libro/<ÁREA>/PRUEBA DE CAMPO MISIÓN n.pdf`, por su resumen en `tablero/instrumentos.csv` | 3 a 9 por área («M2-2» = misión 2, pregunta 2) |
| Cuaderno | preguntas ICFES ya puestas en el cuaderno (`tablero/instrumentos.csv`, `libro/*_icfes.py`) | 1 a 5 por área |

Cada pregunta se clasificó leyendo el enunciado completo, no el título. Donde una pregunta podía caer
en dos tipos se puso en el que manda la tarea (lo que se pide hacer), no el tema.

Escala de la tabla de cobertura: **sí** = el estudiante puede socializarla usando el esquema tal
como está; **a medias** = cabe, pero la mitad del esquema queda vacía o sobra y lo esencial se hace
fuera de él; **no** = el esquema empuja a pensar otra cosa que lo que la pregunta pide.

## Los caminos que se evaluaron

| Camino | A favor | En contra | Decisión |
|---|---|---|---|
| (a) esquema base del área + caja de herramientas | Sirve para cualquier pregunta; el estudiante decide el formato y eso es lo que se socializa; se conserva la personalidad del área en las piezas fijas | El lienzo libre puede quedar vacío en un estudiante flojo; hay que enseñar las herramientas | **Escogido** |
| (b) un esquema por tipo de pregunta, con selector | Muy guiado | Matemáticas tiene 9 tipos y Química 7: no caben en una página; el estudiante tendría que saber el tipo ANTES de escoger la página; vuelve el problema de hoy con más esquemas | Descartado |
| (c) espacio libre con guías mínimas | Máxima apertura | Se vuelve la «página en blanco» genérica; en la devolución no hay nada que auditar; pierde la personalidad del área | Descartado |

La v2 toma de (b) el selector («ME PIDEN», marco uno) y de (c) el lienzo libre, pero con la
estructura de (a) alrededor.

## Lo que cambió (y lo que no)

**Se conserva, tal cual:** el membrete de la página (nombre, simulacro, sesión, fecha, caritas), el
membrete de cada esquema (n.º, la escogí / me la asignaron, marqué / era, nivel, competencia,
componente, estrategia), el salvavidas, «lo que me llevo», el color de cada área, 3 esquemas por
página, las cantidades (5 hojas en Matemáticas, Lectura Crítica y Sociales; 3 en las demás).

**Lo nuevo, igual en las siete áreas (el esqueleto):**

1. **ME PIDEN · marco uno**: cuatro tipos de tarea del área, en palabras de estudiante, sacados de
   la clasificación de arriba. Marcar el tipo es ya la mitad del razonamiento y es lo primero que el
   profe pregunta en la devolución.
2. **Segunda línea propia del área**: la pregunta en mis palabras (Matemáticas, Lectura Crítica,
   Sociales, Inglés), la escala (Biología), el nivel de la química (Química) o la predicción antes
   de mirar (Física).
3. **Tres piezas en fila**: lo que uso → mi espacio para razonar con la herramienta que marqué → la
   pieza que cierra el razonamiento del área.
4. **La caja de herramientas**: cuatro mini-formatos con su dibujito, en la franja izquierda del
   lienzo. El estudiante marca el que usó y lo dibuja en el lienzo.
5. **Tacho con razón**: una razón por cada opción descartada (en Lectura Crítica, con la letra de la
   trampa).

**Lo que da la personalidad de cada área (lo que no se repite):**

| Área | Título | Lo que uso | Lienzo | Herramientas | La pieza que cierra |
|---|---|---|---|---|---|
| Matemáticas | Del dato a la comprobación | los datos que sí uso, con unidad | cuadrícula | cuentas en orden · figura con medidas · tabla o casos · pruebo con un número | **la comprobación**: lo reemplacé · unidad y tamaño creíbles · **un caso que la tumba** · **el paso con el error** |
| Lectura Crítica | Del texto a la evidencia | **la evidencia** con comillas: la frase exacta **o la parte de la imagen**; párrafo, línea o recuadro n.º | limpio | subrayo y copio · mapa de párrafos · tesis y razones · la imagen por partes | **las trampas**: N no lo dice · O dice otra cosa · E exagera o generaliza · R cierto, pero no responde (la letra va en cada opción tachada) |
| Sociales | La situación y sus lentes (antes: La mesa de las voces) | **la situación** en el óvalo: quién, dónde, cuándo | limpio | **la mesa de las voces** · rueda de dimensiones · línea de tiempo · causa y efecto | **la idea clave**: concepto, norma o principio |
| Biología | De lo que veo a lo que concluyo | lo que cambia | limpio | cadena de causas · ejes y curva · control y prueba · cruce de genes | **lo que sí concluyo** / lo que no alcanza a decir |
| Química | Lo que veo, las partículas y el número (antes: La sustancia antes y después) | las sustancias y los datos, **dentro del vaso** | limpio | antes y después · dibujo partículas · cuenta con unidades · control y prueba | **lo que decide**: la propiedad, el modelo o la ley · ☐ átomos y masa cuadran |
| Física | Primero dibujo el sistema | las magnitudes (símbolo = valor y unidad) | puntos | fuerzas y vectores · energía por tramos · ejes y curva · control y prueba | **la ley que manda** · ☐ las unidades cuadran |
| Inglés | La parte, la pista y la respuesta (antes: …y la palabra) | lo que dice, en español | renglones | la palabra que falta · dónde lo veo · lo que me dicen · la línea que responde | **la pista que manda** (lupa): la palabra de al lado · el tiempo del verbo · el lugar o quién habla · un conector o un número · y abajo: **palabra nueva** |

Química cambió de idea central: la v1 era «antes y después de una reacción»; la v2 usa los **tres
niveles de la química** (lo que se ve, las partículas, el símbolo y el número), que es el marco con
que se enseña la química en todas partes y abarca reacciones, mezclas, modelos, cuentas y tabla
periódica. El vaso y el antes/después siguen: el vaso guarda los datos y el antes/después es una de
las herramientas.

Sociales cambió de nombre porque la mesa de las voces pasó de ser todo el esquema a ser **una** de
sus cuatro herramientas: sigue ahí para las preguntas de perspectivas (que son 1 de cada 5).

## Reglas del proyecto (comprobadas en el código y en las muestras)

- Sin líneas horizontales decorativas: lo único horizontal son renglones para escribir y las líneas
  de la cuadrícula y de los dibujitos. *(La banda de color bajo la cabecera de página viene de
  `taller_base.cabecera`, el modelo aprobado de todo el cuaderno; no se tocó.)*
- Los textos de varias líneas (pistas en cursiva) van con `TJ`; ningún texto en LGRAY
  (`verifica_cajas.py`: «TODO EN SU CAJA» en las 7 muestras).
- Anchos medidos con `tw()`: casillas, pastillas y rótulos de herramienta (el código se detiene si
  algo no cabe).
- Renglones de 46 px; fondos claros donde se escribe (el fondo del área al 93 % de blanco).
- Cada esquema va en `<g class="instrumento">` con su límite: `verifica_cajas.py` mide alto y borde
  derecho (≤ 1370).


## Por área: la muestra, los tipos y la cobertura

### Matemáticas

**Esquema v1:** Del dato a la comprobación (datos y lo que piden → cuentas en orden → «lo reemplacé, la unidad cuadra, el tamaño es creíble»).

**Tipos encontrados y cobertura** (n = preguntas de la muestra de ese tipo):

| Tipo de pregunta | n | v1 | Por qué | v2 | Cómo la toma la v2 |
|---|---|---|---|---|---|
| Cálculo con datos de un texto o una tabla | 2 | **sí** | es el caso para el que se diseñó | **sí** | calcular un valor · cuentas en orden · lo reemplacé en el enunciado |
| Geometría con figura (ángulos, áreas, volúmenes, semejanza) | 4 | **a medias** | la cuadrícula deja dibujar, pero nada pide la figura con sus medidas y «la unidad cuadra» no dice nada de un ángulo | **sí** | figura con medidas en la cuadrícula · unidad y tamaño creíbles |
| Escoger la expresión, ecuación o función que modela | 3 | **a medias** | el camino lleva a UN número; no hay dónde probar las cuatro expresiones con un dato | **sí** | representar · pruebo con un número (meto un dato de la tabla en cada expresión) |
| Escoger la gráfica o la tabla que representa la situación | 3 | **no** | no hay cuentas en orden que hacer: el trabajo es leer un punto y buscarlo en cada gráfica | **sí** | representar · tabla o casos / pruebo con un número · tacho con razón |
| Validar una afirmación («¿es correcta?» · Sí/No, porque…) | 6 | **no** | no hay lugar para la afirmación ni para el contraejemplo; las opciones son razones y nadie las compara | **sí** | validar una afirmación · un caso que la tumba · tacho con razón |
| Hallar el procedimiento correcto o el paso con error | 4 | **no** | el esquema hace hacer las cuentas propias, no revisar las de otro | **sí** | validar · cuentas en orden (copio los pasos) · el paso con el error |
| Decidir qué se puede saber con los datos | 2 | **no** | no hay nada que calcular; hay que ver qué dato falta | **sí** | ver si los datos alcanzan · LOS DATOS QUE SÍ USO · tacho con razón |
| Conteo y probabilidad | 3 | **a medias** | las cuentas caben, pero no hay forma de listar los casos | **sí** | tabla o casos (o árbol) · un caso que la tumba |
| Leer gráficas o tablas estadísticas | 3 | **a medias** | sirve para el cálculo final, no para leer la gráfica | **sí** | LOS DATOS QUE SÍ USO (leídos de la gráfica) · tabla o casos |

**Cobertura sobre la muestra:** v1 — sí 2, a medias 13, no 15 de 30 (7 % sí). v2 — sí 30, a medias 0, no 0.

<details><summary>La muestra, pregunta por pregunta</summary>

| Fuente | N.º | Pregunta | Tipo | v1 | v2 |
|---|---|---|---|---|---|
| CM26 | 1 | Promedios de cuatro cursos · «hubo un aumento» | Validar una afirmación («¿es correcta?» · Sí/No, porque…) | no | sí |
| CM26 | 2 | Inversión en dólares · «en pesos también gana 3 %» | Validar una afirmación («¿es correcta?» · Sí/No, porque…) | no | sí |
| CM26 | 3 | Franjas del museo · ¿garantiza el menor precio? | Validar una afirmación («¿es correcta?» · Sí/No, porque…) | no | sí |
| CM26 | 4 | Capacitación · ¿cuántos empleados tiene «Insumos»? | Cálculo con datos de un texto o una tabla | sí | sí |
| CM26 | 5 | Capacitación · cuánto paga cada uno | Cálculo con datos de un texto o una tabla | sí | sí |
| CM26 | 8 | Temperatura y altitud · la expresión | Escoger la expresión, ecuación o función que modela | a medias | sí |
| CM26 | 12 | Costos por ciudad · ¿cuál gráfica? | Escoger la gráfica o la tabla que representa la situación | no | sí |
| CM26 | 13 | Comerciante · ¿qué se puede determinar? | Decidir qué se puede saber con los datos | no | sí |
| CM26 | 15 | Sombras de dos postes · el ángulo β | Geometría con figura (ángulos, áreas, volúmenes, semejanza) | a medias | sí |
| CM26 | 18 | Faros y barco · ley del seno | Geometría con figura (ángulos, áreas, volúmenes, semejanza) | a medias | sí |
| CM26 | 19 | Robots P y Q · la ecuación | Escoger la expresión, ecuación o función que modela | a medias | sí |
| CM26 | 24 | Área del cuadrado sombreado | Geometría con figura (ángulos, áreas, volúmenes, semejanza) | a medias | sí |
| CM26 | 25 | Extensiones de 4 dígitos distintos | Conteo y probabilidad | a medias | sí |
| CM26 | 26 | Parque automotor · afirmación verdadera | Leer gráficas o tablas estadísticas | a medias | sí |
| CM26 | 27 | Récord olímpico y mundial · ¿es posible? | Validar una afirmación («¿es correcta?» · Sí/No, porque…) | no | sí |
| CM26 | 31 | Tres estudiantes resuelven una ecuación | Hallar el procedimiento correcto o el paso con error | no | sí |
| CM26 | 33 | Porcentajes de un grupo · ¿cuál tabla? | Escoger la gráfica o la tabla que representa la situación | no | sí |
| CM26 | 35 | Descuento · ¿en qué paso está el error? | Hallar el procedimiento correcto o el paso con error | no | sí |
| CM26 | 38 | Pizza y bebidas · qué se puede calcular | Decidir qué se puede saber con los datos | no | sí |
| CM26 | 43 | Gráfica de A(x) = x·f(x) | Escoger la gráfica o la tabla que representa la situación | no | sí |
| CM26 | 45 | Grupos para el foro | Conteo y probabilidad | a medias | sí |
| CM26 | 46 | Procedimientos para la probabilidad de ganar | Hallar el procedimiento correcto o el paso con error | no | sí |
| CM26 | 48 | Rifa con tres balotas · por qué es más probable | Conteo y probabilidad | a medias | sí |
| CM26 | 49 | Valorización del 5 % anual · la expresión | Escoger la expresión, ecuación o función que modela | a medias | sí |
| CM26 | 50 | Volumen de tres empaques | Geometría con figura (ángulos, áreas, volúmenes, semejanza) | a medias | sí |
| Libro | M2-2 | Ciclistas · «el descanso debería ser en la semana 10» | Validar una afirmación («¿es correcta?» · Sí/No, porque…) | no | sí |
| Libro | M4-5 | «El cilindro no puede tener 9π m³» | Validar una afirmación («¿es correcta?» · Sí/No, porque…) | no | sí |
| Libro | M5-4 | Histograma de 200 estudiantes | Leer gráficas o tablas estadísticas | a medias | sí |
| Libro | M5-8 | Gira · qué países NO llegan al 50 % | Leer gráficas o tablas estadísticas | a medias | sí |
| Libro | M6-4 | Automatización · «0,30 × 0,30 = 0,09» | Hallar el procedimiento correcto o el paso con error | no | sí |

</details>

### Lectura Crítica

**Esquema v1:** Del texto a la evidencia (qué dice · qué me pregunta · la cita exacta · tacho con razón).

**Tipos encontrados y cobertura** (n = preguntas de la muestra de ese tipo):

| Tipo de pregunta | n | v1 | Por qué | v2 | Cómo la toma la v2 |
|---|---|---|---|---|---|
| Información local: qué dice el texto o quién lo narra | 2 | **sí** | la cita exacta es justo lo que pide | **sí** | qué dice · LA EVIDENCIA · subrayo y copio |
| Vocabulario en contexto (sinónimo, antónimo, reemplazo) | 2 | **a medias** | la cita sirve, pero no hay dónde probar cada palabra dentro de la frase | **sí** | subrayo y copio (la frase con la palabra) · trampas O y R en lo que tacho |
| Función de una parte (conector, párrafo, ejemplo, expresión) | 4 | **a medias** | una cita sola no muestra para qué está: hay que ver lo de antes y lo de después | **sí** | cómo se arma · mapa de párrafos |
| Tema, síntesis o título | 1 | **a medias** | el tema no cabe en una cita: es de todo el texto | **sí** | frase mía de la fila A · mapa de párrafos · trampa E (generaliza o se queda corto) |
| Inferencia, implicación, supuesto o prejuicio | 4 | **no** | pide «copio las palabras exactas» y el supuesto, por definición, no está escrito | **sí** | qué supone o infiere · tesis y razones · trampas N y E |
| Tesis y argumentos (razón a favor, cita que refuerza, contradice) | 4 | **a medias** | hay evidencia, pero no dónde poner la tesis frente a la razón | **sí** | tesis y razones · LA EVIDENCIA |
| Texto discontinuo: caricatura, historieta, infografía | 7 | **no** | no hay «palabras exactas» que copiar: la evidencia es un recuadro o un dibujo | **sí** | la imagen por partes · evidencia: «señalo la parte de la imagen» · recuadro n.º |
| Evaluar: propósito, contexto, juicio de valor, calidad de un resumen | 4 | **a medias** | «qué me pregunta de verdad» ayuda; nada ayuda a juzgar | **sí** | qué tan válido es · LAS TRAMPAS · tacho con la letra de la trampa |

**Cobertura sobre la muestra:** v1 — sí 2, a medias 15, no 11 de 28 (7 % sí). v2 — sí 28, a medias 0, no 0.

<details><summary>La muestra, pregunta por pregunta</summary>

| Fuente | N.º | Pregunta | Tipo | v1 | v2 |
|---|---|---|---|---|---|
| CLC26 | 1 | «famélico» · el antónimo | Vocabulario en contexto (sinónimo, antónimo, reemplazo) | a medias | sí |
| CLC26 | 2 | Quién narra el fragmento | Información local: qué dice el texto o quién lo narra | sí | sí |
| CLC26 | 3 | La palabra que describe a Johnny | Inferencia, implicación, supuesto o prejuicio | no | sí |
| CLC26 | 4 | La cita que refuerza la idea (avispa Sphex) | Tesis y argumentos (razón a favor, cita que refuerza, contradice) | a medias | sí |
| CLC26 | 5 | El tema principal | Tema, síntesis o título | a medias | sí |
| CLC26 | 6 | Infografía RCP · cuándo reanimar | Texto discontinuo: caricatura, historieta, infografía | no | sí |
| CLC26 | 8 | Para qué las imágenes en la infografía | Texto discontinuo: caricatura, historieta, infografía | no | sí |
| CLC26 | 9 | «pálido desierto de la mesa» · para qué | Función de una parte (conector, párrafo, ejemplo, expresión) | a medias | sí |
| CLC26 | 13 | Historieta de la limonada · a qué recurre | Texto discontinuo: caricatura, historieta, infografía | no | sí |
| CLC26 | 14 | Caricatura · qué la describe mejor | Texto discontinuo: caricatura, historieta, infografía | no | sí |
| CLC26 | 17 | «irrecusable» · sinónimo | Vocabulario en contexto (sinónimo, antónimo, reemplazo) | a medias | sí |
| CLC26 | 18 | Por qué el resumen es inadecuado | Evaluar: propósito, contexto, juicio de valor, calidad de un resumen | a medias | sí |
| CLC26 | 19 | La descripción de Aguado · a qué época corresponde | Evaluar: propósito, contexto, juicio de valor, calidad de un resumen | a medias | sí |
| CLC26 | 24 | Qué prejuicio cuestiona la autora | Inferencia, implicación, supuesto o prejuicio | no | sí |
| CLC26 | 25 | Qué contradice la tesis de la historieta | Tesis y argumentos (razón a favor, cita que refuerza, contradice) | a medias | sí |
| CLC26 | 27 | Cuál es un juicio de valor | Evaluar: propósito, contexto, juicio de valor, calidad de un resumen | a medias | sí |
| CLC26 | 30 | Supuesto subyacente a una afirmación | Inferencia, implicación, supuesto o prejuicio | no | sí |
| CLC26 | 31 | Razón a favor de la tesis (Giges) | Tesis y argumentos (razón a favor, cita que refuerza, contradice) | a medias | sí |
| CLC26 | 33 | Propósito del relato de Giges y cómo lo logra | Función de una parte (conector, párrafo, ejemplo, expresión) | a medias | sí |
| CLC26 | 35 | Función de «Sin embargo» | Función de una parte (conector, párrafo, ejemplo, expresión) | a medias | sí |
| CLC26 | 40 | Implicación sobre los fulbes | Inferencia, implicación, supuesto o prejuicio | no | sí |
| CLC26 | 45 | Infografía · qué inferir por región | Texto discontinuo: caricatura, historieta, infografía | no | sí |
| CLC26 | 48 | Propósito del autor de la infografía | Evaluar: propósito, contexto, juicio de valor, calidad de un resumen | a medias | sí |
| Libro | M1-4 | Caricatura de prensa · «servicio» entre comillas | Texto discontinuo: caricatura, historieta, infografía | no | sí |
| Libro | M2-6 | Caricatura · «la estadística a veces omite» | Texto discontinuo: caricatura, historieta, infografía | no | sí |
| Libro | M3-1 | Qué hace el segundo párrafo | Función de una parte (conector, párrafo, ejemplo, expresión) | a medias | sí |
| Libro | M4-7 | Qué afirmación es literal | Información local: qué dice el texto o quién lo narra | sí | sí |
| Libro | M6-7 | La tesis del ensayo sobre el dinero | Tesis y argumentos (razón a favor, cita que refuerza, contradice) | a medias | sí |

</details>

### Sociales y Ciudadanas

**Esquema v1:** La mesa de las voces (tres voces alrededor de la situación · en qué chocan · desde dónde pregunta · lo que se pone en tensión).

**Tipos encontrados y cobertura** (n = preguntas de la muestra de ese tipo):

| Tipo de pregunta | n | v1 | Por qué | v2 | Cómo la toma la v2 |
|---|---|---|---|---|---|
| Qué concepto, norma, derecho o mecanismo explica la situación | 8 | **no** | aquí no hay voces: hay que reconocer un concepto (oferta y demanda, tutela, ramas del poder) y la mesa obliga a inventar tres actores | **sí** | qué concepto o norma · LA IDEA CLAVE · causa y efecto |
| Perspectivas: qué piensa o busca cada actor | 5 | **sí** | es el caso para el que se diseñó | **sí** | qué busca cada actor · la mesa de las voces (ahora es una herramienta) |
| Efectos en varias dimensiones (pensamiento sistémico) | 4 | **a medias** | las dimensiones solo se marcan en el membrete; la mesa no tiene dónde poner efectos | **sí** | qué efectos trae · rueda de dimensiones o causa y efecto |
| Supuestos, intenciones y valor de un argumento o de una fuente | 4 | **a medias** | «desde dónde pregunta» ayuda, pero no hay dónde examinar el argumento | **sí** | qué supone un argumento · LA IDEA CLAVE · tacho con razón |
| Contexto histórico o geográfico (época, proceso, lugar) | 5 | **no** | no hay tiempo ni lugar en el esquema | **sí** | LA SITUACIÓN (quién, dónde, cuándo) · línea de tiempo |

**Cobertura sobre la muestra:** v1 — sí 5, a medias 8, no 13 de 26 (19 % sí). v2 — sí 26, a medias 0, no 0.

<details><summary>La muestra, pregunta por pregunta</summary>

| Fuente | N.º | Pregunta | Tipo | v1 | v2 |
|---|---|---|---|---|---|
| Cuaderno | M1 · ICFES 4 | Qué rama del poder puede ejercer cierta función | Qué concepto, norma, derecho o mecanismo explica la situación | no | sí |
| Cuaderno | M2 · ICFES 2 | El mecanismo de participación del presidente | Qué concepto, norma, derecho o mecanismo explica la situación | no | sí |
| Libro | M1-4 | Becas por puntaje Saber 11 · qué principio | Qué concepto, norma, derecho o mecanismo explica la situación | no | sí |
| Libro | M2-3 | Fotos publicadas sin permiso · qué principio | Qué concepto, norma, derecho o mecanismo explica la situación | no | sí |
| Libro | M2-9 | Firmas contra el alcalde · qué mecanismo | Qué concepto, norma, derecho o mecanismo explica la situación | no | sí |
| PTD7 | 3 | Ecopetrol y Oxy · qué concepto la explica | Qué concepto, norma, derecho o mecanismo explica la situación | no | sí |
| PTD7 | 4 | Verano y precio del café · qué conceptos | Qué concepto, norma, derecho o mecanismo explica la situación | no | sí |
| PTD7 | 13 | Discurso de 1990 · por qué es neoliberal | Qué concepto, norma, derecho o mecanismo explica la situación | no | sí |
| PTD7 | 1 | Plan Colombia · qué supuesto se reconoce | Supuestos, intenciones y valor de un argumento o de una fuente | a medias | sí |
| PTD7 | 8 | El CONPES 2465 apoya a Garay porque… | Supuestos, intenciones y valor de un argumento o de una fuente | a medias | sí |
| Libro | M5-4 | Mina en Boyacá · prejuicios e intenciones | Supuestos, intenciones y valor de un argumento o de una fuente | a medias | sí |
| Cuaderno | M4 · ICFES 3 | Autopista en la ciénaga · mejor argumento | Supuestos, intenciones y valor de un argumento o de una fuente | a medias | sí |
| PTD7 | 15 | Genovia · tratado y subsidios | Perspectivas: qué piensa o busca cada actor | sí | sí |
| Libro | M2-1 | Foro sobre celulares en clase · tres voces | Perspectivas: qué piensa o busca cada actor | sí | sí |
| Libro | M2-7 | Prohibición de las corridas · qué defiende cada lado | Perspectivas: qué piensa o busca cada actor | sí | sí |
| Libro | M3-8 | Aranceles · el gobierno y sus críticos | Perspectivas: qué piensa o busca cada actor | sí | sí |
| Libro | M4-5 | Turbo · testimonios que no coinciden | Perspectivas: qué piensa o busca cada actor | sí | sí |
| Libro | M1-9 | Cese al fuego · qué efecto integra dos dimensiones | Efectos en varias dimensiones (pensamiento sistémico) | a medias | sí |
| Libro | M3-10 | Aranceles prolongados · efectos en varias dimensiones | Efectos en varias dimensiones (pensamiento sistémico) | a medias | sí |
| Libro | M5-8 | El agua de La Calera · ambiente, sociedad y política | Efectos en varias dimensiones (pensamiento sistémico) | a medias | sí |
| Cuaderno | M3 · ICFES 2 | Mundial 2014 · efectos no esperados | Efectos en varias dimensiones (pensamiento sistémico) | a medias | sí |
| PTD7 | 2 | Lista de conceptos · ¿a qué proceso pertenecen? | Contexto histórico o geográfico (época, proceso, lugar) | no | sí |
| PTD7 | 6 | Separación de Panamá · qué puso en evidencia | Contexto histórico o geográfico (época, proceso, lugar) | no | sí |
| Libro | M4-9 | Voto femenino · 1954 y 1957 | Contexto histórico o geográfico (época, proceso, lugar) | no | sí |
| Libro | M5-9 | Tapón del Darién · la geografía de una ruta | Contexto histórico o geográfico (época, proceso, lugar) | no | sí |
| Cuaderno | M5 · ICFES 4 | Real Audiencia y encomienda · propósito | Contexto histórico o geográfico (época, proceso, lugar) | no | sí |

</details>

### Biología

**Esquema v1:** De lo que veo a lo que concluyo (escala · lo que cambia → lo que muestran los datos (con control) → lo que sí puedo concluir).

**Tipos encontrados y cobertura** (n = preguntas de la muestra de ese tipo):

| Tipo de pregunta | n | v1 | Por qué | v2 | Cómo la toma la v2 |
|---|---|---|---|---|---|
| Explicar un proceso o una estructura (célula, órganos, ciclos) | 4 | **a medias** | la escala ayuda, pero «los datos» y «el control» quedan vacíos cuando no hay experimento | **sí** | explicar un proceso · cadena de causas |
| Predecir qué pasa si algo cambia | 4 | **a medias** | «lo que cambia» sirve; no hay dónde seguir la cadena de efectos | **sí** | predecir qué pasa si… · cadena de causas |
| Leer datos, tablas o gráficas | 4 | **sí** | es el caso para el que se diseñó | **sí** | leer datos · ejes y curva · lo que sí concluyo |
| Indagación: hipótesis, control, pregunta investigable | 4 | **sí** | variable, control y conclusión están ahí | **sí** | leer datos o un experimento · control y prueba · lo que no alcanza |
| Genética y herencia (cruces, pedigrí, código) | 3 | **no** | no hay dónde hacer el cruce ni contar codones | **sí** | cruce de genes |
| Escoger el modelo o la gráfica que representa | 3 | **a medias** | los ejes pequeños ayudan; el resto del esquema sobra | **sí** | ejes y curva (dibujo lo que espero antes de mirar) · tacho con razón |
| Valorar un uso de la ciencia o una propuesta | 2 | **a medias** | la conclusión sirve; no hay dónde poner a favor y en contra | **a medias** | valorar una conclusión · lo que sí concluyo / lo que no alcanza; el a favor y en contra se hace en el lienzo libre (no hay herramienta propia) |

**Cobertura sobre la muestra:** v1 — sí 8, a medias 13, no 3 de 24 (33 % sí). v2 — sí 22, a medias 2, no 0.

<details><summary>La muestra, pregunta por pregunta</summary>

| Fuente | N.º | Pregunta | Tipo | v1 | v2 |
|---|---|---|---|---|---|
| CCN | 5 | Error al copiar ADN en ARNm · qué le pasa a la proteína | Predecir qué pasa si algo cambia | a medias | sí |
| CCN | 10 | Dengue · la cartelera que comunica los resultados | Indagación: hipótesis, control, pregunta investigable | sí | sí |
| CCN | 11 | Dengue · mantener o cambiar la hipótesis | Indagación: hipótesis, control, pregunta investigable | sí | sí |
| CCN | 12 | Por qué reducir el agua estancada | Explicar un proceso o una estructura (célula, órganos, ciclos) | a medias | sí |
| CCN | 16 | Secuencia de ARNm · cuántos aminoácidos | Genética y herencia (cruces, pedigrí, código) | no | sí |
| CCN | 20 | Antibióticos y supervivencia · qué hipótesis | Leer datos, tablas o gráficas | sí | sí |
| CCN | 21 | Red trófica sin atún | Predecir qué pasa si algo cambia | a medias | sí |
| CCN | 24 | Planta con y sin bacteria · qué gráfica | Escoger el modelo o la gráfica que representa | a medias | sí |
| CCN | 34 | Almidón y lugol · para qué el experimento 4 | Indagación: hipótesis, control, pregunta investigable | sí | sí |
| CCN | 36 | Lisosomas rotos | Predecir qué pasa si algo cambia | a medias | sí |
| CCN | 38 | Patos de cuello largo · genotipo de los padres | Genética y herencia (cruces, pedigrí, código) | no | sí |
| CCN | 39 | Proteínas por peso molecular · en qué tiempo | Leer datos, tablas o gráficas | sí | sí |
| CCN | 40 | Polilla de la cera · pregunta investigable | Indagación: hipótesis, control, pregunta investigable | sí | sí |
| CCN | 44 | Modelo de ecosistema abierto | Escoger el modelo o la gráfica que representa | a medias | sí |
| CCN | 47 | Ratones con y sin ejercicio en el laberinto | Leer datos, tablas o gráficas | sí | sí |
| CCN | 49 | Fotosíntesis y respiración · anabolismo | Explicar un proceso o una estructura (célula, órganos, ciclos) | a medias | sí |
| Libro | M1-1 | Célula con desechos · qué organelo falló | Explicar un proceso o una estructura (célula, órganos, ciclos) | a medias | sí |
| Libro | M2-9 | Comida rica en carbohidratos · regulación de la glucosa | Explicar un proceso o una estructura (célula, órganos, ciclos) | a medias | sí |
| Libro | M3-5 | Casanare · se van los jaguares | Predecir qué pasa si algo cambia | a medias | sí |
| Libro | M4-3 | Prótesis de hipocampo · uso responsable | Valorar un uso de la ciencia o una propuesta | a medias | a medias |
| Libro | M5-1 | Pedigrí de una enfermedad rara | Genética y herencia (cruces, pedigrí, código) | no | sí |
| Libro | M5-10 | Perros Pomsky · valorar la biotecnología | Valorar un uso de la ciencia o una propuesta | a medias | a medias |
| Libro | M6-2 | Perros de apartamento · lo que muestra la tabla | Leer datos, tablas o gráficas | sí | sí |
| Cuaderno | M2 · ICFES D | Frecuencia cardiaca · qué gráfica | Escoger el modelo o la gráfica que representa | a medias | sí |

</details>

### Química

**Esquema v1:** La sustancia antes y después (vaso ANTES → qué la transforma → vaso DESPUÉS · balanza de lo que se conserva · la propiedad que decide).

**Tipos encontrados y cobertura** (n = preguntas de la muestra de ese tipo):

| Tipo de pregunta | n | v1 | Por qué | v2 | Cómo la toma la v2 |
|---|---|---|---|---|---|
| Modelo de partículas y estados | 4 | **a medias** | el antes y el después sirven si hay cambio de estado; no hay dónde dibujar partículas | **sí** | explicar con partículas · dibujo partículas · nivel «las partículas» |
| Estequiometría y cantidades (moles, masa, reactivo límite) | 3 | **a medias** | la balanza cuenta átomos, pero no hay espacio para la cuenta con unidades | **sí** | calcular una cantidad · cuenta con unidades · átomos y masa cuadran |
| Soluciones, solubilidad y concentración | 3 | **a medias** | sirve el antes/después; la cuenta de concentración no cabe | **sí** | calcular · cuenta con unidades o antes y después |
| Clasificar o identificar (mezclas, configuración, grupos funcionales) | 6 | **no** | nada se transforma: los dos vasos y la balanza quedan vacíos | **sí** | clasificar o identificar · LO QUE DECIDE (la propiedad o el criterio) |
| Leer datos o gráficas (curvas de calentamiento, velocidad) | 3 | **a medias** | la propiedad que decide sirve; no hay dónde leer la gráfica | **sí** | leer datos · LAS SUSTANCIAS Y LOS DATOS · ejes en el lienzo |
| Diseño experimental (variable, control, procedimiento) | 3 | **no** | no hay variable ni control en el esquema | **sí** | leer datos o un experimento · control y prueba |
| Valorar una propuesta (pilas, combustibles, plásticos) | 2 | **no** | nada que ver con antes y después | **a medias** | LO QUE DECIDE (el criterio) · antes y después para comparar; no hay herramienta propia de a favor y en contra |

**Cobertura sobre la muestra:** v1 — sí 0, a medias 13, no 11 de 24 (0 % sí). v2 — sí 22, a medias 2, no 0.

<details><summary>La muestra, pregunta por pregunta</summary>

| Fuente | N.º | Pregunta | Tipo | v1 | v2 |
|---|---|---|---|---|---|
| CCN | 1 | Moléculas de agua en líquido y gas · qué modelo | Modelo de partículas y estados | a medias | sí |
| CCN | 2 | Formación del agua · los reactivos | Estequiometría y cantidades (moles, masa, reactivo límite) | a medias | sí |
| CCN | 3 | Sal de sodio a 83 °C · ¿la suposición es correcta? | Soluciones, solubilidad y concentración | a medias | sí |
| CCN | 4 | Hielo seco · por qué baja la densidad | Modelo de partículas y estados | a medias | sí |
| CCN | 7 | Contaminantes X y W · el procedimiento | Diseño experimental (variable, control, procedimiento) | no | sí |
| CCN | 8 | Dos sustancias · qué tipo de mezcla | Clasificar o identificar (mezclas, configuración, grupos funcionales) | no | sí |
| CCN | 15 | H₂SO₄ al 78 % o HNO₃ 112 mL/200 mL | Soluciones, solubilidad y concentración | a medias | sí |
| CCN | 18 | P₄ y Cl₂ · el reactivo límite | Estequiometría y cantidades (moles, masa, reactivo límite) | a medias | sí |
| CCN | 23 | Configuración del aluminio · por qué 3+ | Clasificar o identificar (mezclas, configuración, grupos funcionales) | no | sí |
| CCN | 27 | Agua que hierve a 25 km de altura | Modelo de partículas y estados | a medias | sí |
| CCN | 28 | El acero en el diagrama de clasificación | Clasificar o identificar (mezclas, configuración, grupos funcionales) | no | sí |
| CCN | 30 | Conductividad del MgSO₄ · qué se estudiaba | Diseño experimental (variable, control, procedimiento) | no | sí |
| CCN | 33 | Densidades a distintas temperaturas · mal planteado | Diseño experimental (variable, control, procedimiento) | no | sí |
| CCN | 35 | Curva de calentamiento · qué sustancia | Leer datos o gráficas (curvas de calentamiento, velocidad) | a medias | sí |
| CCN | 37 | Velocidad de formación de Z · qué concluir | Leer datos o gráficas (curvas de calentamiento, velocidad) | a medias | sí |
| CCN | 41 | Alcohol oxidado y pruebas de grupos funcionales | Clasificar o identificar (mezclas, configuración, grupos funcionales) | no | sí |
| CCN | 46 | Pilas en contenedores aislados · ¿apropiada? | Valorar una propuesta (pilas, combustibles, plásticos) | no | a medias |
| CCN | 50 | Cuatro alcoholes · el de menor acidez | Clasificar o identificar (mezclas, configuración, grupos funcionales) | no | sí |
| Libro | M1-1 | Nitrato de potasio · cuánto se cristaliza | Soluciones, solubilidad y concentración | a medias | sí |
| Libro | M2-3 | Tanque de propano al sol · por qué sube la presión | Modelo de partículas y estados | a medias | sí |
| Libro | M5-8 | Combustión del biodiésel · moles de CO₂ | Estequiometría y cantidades (moles, masa, reactivo límite) | a medias | sí |
| Libro | M6-10 | pH de un queso a tres temperaturas | Leer datos o gráficas (curvas de calentamiento, velocidad) | a medias | sí |
| Cuaderno | M5 · ICFES 4 | Aceite de palma frente al combustible fósil | Valorar una propuesta (pilas, combustibles, plásticos) | no | a medias |
| Cuaderno | M6 · ICFES 1 | El ion Mg²⁺ · qué modelo de capas | Clasificar o identificar (mezclas, configuración, grupos funcionales) | no | sí |

</details>

### Física

**Esquema v1:** Primero dibujo el sistema (dibujo con puntos · magnitudes · la ley que manda · predigo antes de mirar).

**Tipos encontrados y cobertura** (n = preguntas de la muestra de ese tipo):

| Tipo de pregunta | n | v1 | Por qué | v2 | Cómo la toma la v2 |
|---|---|---|---|---|---|
| Fuerzas y movimiento (diagramas, vectores, aceleración) | 3 | **sí** | es el caso para el que se diseñó | **sí** | fuerzas y vectores · la ley que manda |
| Energía, calor y sus transformaciones | 2 | **a medias** | se puede dibujar, pero no hay dónde poner la energía antes y después | **sí** | energía por tramos · predigo antes de mirar |
| Escoger o leer una gráfica | 4 | **a medias** | dibujar el sistema no ayuda a leer una curva | **sí** | escoger gráfica o diagrama · ejes y curva (dibujo la mía antes de mirar) |
| Ondas, luz, electricidad y magnetismo | 6 | **sí** | el dibujo con puntos sirve para rayos, campos y circuitos | **sí** | DIBUJO EL SISTEMA (el lienzo) · la ley que manda |
| Cálculo con fórmula y unidades | 3 | **sí** | magnitudes y ley están ahí | **sí** | LAS MAGNITUDES · la ley · las unidades cuadran |
| Indagación: pregunta investigable, variable, ¿basta un ensayo? | 6 | **no** | no hay variable, control ni conclusión: dibujar el sistema no responde «qué pregunta se puede contestar» | **sí** | evaluar un experimento · control y prueba |

**Cobertura sobre la muestra:** v1 — sí 12, a medias 6, no 6 de 24 (50 % sí). v2 — sí 24, a medias 0, no 0.

<details><summary>La muestra, pregunta por pregunta</summary>

| Fuente | N.º | Pregunta | Tipo | v1 | v2 |
|---|---|---|---|---|---|
| CCN | 6 | Olla que se enfría · qué gráfica | Escoger o leer una gráfica | a medias | sí |
| CCN | 9 | Detector fuera del agua · qué variable | Indagación: pregunta investigable, variable, ¿basta un ensayo? | no | sí |
| CCN | 13 | Tres objetos que caen · qué pregunta se puede contestar | Indagación: pregunta investigable, variable, ¿basta un ensayo? | no | sí |
| CCN | 14 | Lluvia vista desde el bus · vectores | Fuerzas y movimiento (diagramas, vectores, aceleración) | sí | sí |
| CCN | 17 | Salto bungee a los 20 m · transformación | Energía, calor y sus transformaciones | a medias | sí |
| CCN | 19 | Esferas en contacto · qué partículas pasaron | Ondas, luz, electricidad y magnetismo | sí | sí |
| CCN | 22 | 2 L de agua en la misma estufa | Energía, calor y sus transformaciones | a medias | sí |
| CCN | 25 | Piedra en el estanque · la aceleración | Fuerzas y movimiento (diagramas, vectores, aceleración) | sí | sí |
| CCN | 26 | Pelota soplada que sube acelerada | Fuerzas y movimiento (diagramas, vectores, aceleración) | sí | sí |
| CCN | 29 | Línea de tendencia · ¿es una predicción? | Indagación: pregunta investigable, variable, ¿basta un ensayo? | no | sí |
| CCN | 31 | Resistencias contra temperatura | Escoger o leer una gráfica | a medias | sí |
| CCN | 32 | El farol visto desde la piscina llena | Ondas, luz, electricidad y magnetismo | sí | sí |
| CCN | 42 | Fuerzas eléctricas sobre la carga 1 | Ondas, luz, electricidad y magnetismo | sí | sí |
| CCN | 43 | Energía potencial · qué montaña rusa | Escoger o leer una gráfica | a medias | sí |
| CCN | 45 | Onda longitudinal en la fila de personas | Ondas, luz, electricidad y magnetismo | sí | sí |
| CCN | 48 | Velocidad del sonido · qué gráfica | Escoger o leer una gráfica | a medias | sí |
| Libro | M1-1 | Dos bloques en planos · qué procedimiento | Indagación: pregunta investigable, variable, ¿basta un ensayo? | no | sí |
| Libro | M1-9 | Bloque en un plano de 30° · trabajo de la gravedad | Cálculo con fórmula y unidades | sí | sí |
| Libro | M2-9 | Calorímetro · 2 kg a 80 °C con 3 kg de agua | Cálculo con fórmula y unidades | sí | sí |
| Libro | M3-1 | Imán y bobina · ¿es correcta la explicación? | Ondas, luz, electricidad y magnetismo | sí | sí |
| Libro | M4-10 | Radios a un segundo · distancia en el aluminio | Cálculo con fórmula y unidades | sí | sí |
| Libro | M5-8 | Sifón · ¿vale la conclusión de un solo ensayo? | Indagación: pregunta investigable, variable, ¿basta un ensayo? | no | sí |
| Libro | M6-4 | Motor de la banda · ¿una hora basta? | Indagación: pregunta investigable, variable, ¿basta un ensayo? | no | sí |
| Libro | M6-9 | Dos resistencias iguales en paralelo | Ondas, luz, electricidad y magnetismo | sí | sí |

</details>

### Inglés

**Esquema v1:** La parte, la pista y la palabra (la frase con el hueco → la pista → la palabra que va → las que descarté · palabra nueva).

**Tipos encontrados y cobertura** (n = preguntas de la muestra de ese tipo):

| Tipo de pregunta | n | v1 | Por qué | v2 | Cómo la toma la v2 |
|---|---|---|---|---|---|
| Parte 1 · léxico: la palabra que corresponde a una descripción | 4 | **a medias** | no hay frase con hueco: hay una descripción y ocho palabras | **sí** | la palabra que va · LO QUE DICE en español · la palabra que falta |
| Parte 2 · avisos: dónde lo vería o qué significa | 3 | **no** | no hay hueco ni palabra: la respuesta es un lugar | **sí** | dónde o quién · dónde lo veo |
| Parte 3 · conversación: la respuesta que va | 3 | **a medias** | la «frase» sirve; la respuesta no es una palabra sino una réplica | **sí** | qué responder · lo que me dicen · la pista (quién habla) |
| Parte 4 · texto con espacios (gramática) | 5 | **sí** | es el caso para el que se diseñó | **sí** | la palabra que va · la palabra que falta · la pista |
| Parte 5 · comprensión literal | 4 | **no** | la respuesta es una frase del texto; ni hueco ni «palabra que va» | **sí** | qué dice · la línea que responde · LO QUE DICE en español |
| Parte 6 · comprensión inferencial | 4 | **no** | igual que la 5, y además hay que inferir | **sí** | qué dice o deja entender · la línea que responde · DESCARTÉ |
| Parte 7 · texto con espacios (léxico y gramática) | 2 | **sí** | es el caso para el que se diseñó | **sí** | la palabra que va · la pista (conector o tiempo) |

**Cobertura sobre la muestra:** v1 — sí 7, a medias 7, no 11 de 25 (28 % sí). v2 — sí 25, a medias 0, no 0.

<details><summary>La muestra, pregunta por pregunta</summary>

| Fuente | N.º | Pregunta | Tipo | v1 | v2 |
|---|---|---|---|---|---|
| CI24 | 1 | «A person can carry things in one of these» · handbags | Parte 1 · léxico: la palabra que corresponde a una descripción | a medias | sí |
| CI24 | 4 | «Some people need them to see well» · glasses | Parte 1 · léxico: la palabra que corresponde a una descripción | a medias | sí |
| SIM | 61 | «Rabbits like this long orange vegetable» | Parte 1 · léxico: la palabra que corresponde a una descripción | a medias | sí |
| CI24 | 6 | Aviso «Draw a line to complete the snake» | Parte 2 · avisos: dónde lo vería o qué significa | no | sí |
| SIM | 3 | Aviso «Do not eat here» | Parte 2 · avisos: dónde lo vería o qué significa | no | sí |
| CI24 | P3 | «How much is that umbrella?» | Parte 3 · conversación: la respuesta que va | a medias | sí |
| SIM | 121 | «She wasn't sent the invitation!» | Parte 3 · conversación: la respuesta que va | a medias | sí |
| CI24 | 9 | Coffee · «Its ___ important component» (most) | Parte 4 · texto con espacios (gramática) | sí | sí |
| CI24 | 13 | Coffee · «was first ___» (described) | Parte 4 · texto con espacios (gramática) | sí | sí |
| CI24 | 15 | Coffee · «you ___ believe this» (mustn't) | Parte 4 · texto con espacios (gramática) | sí | sí |
| CI24 | 16 | Coffee · «___ many people believe…» (While) | Parte 4 · texto con espacios (gramática) | sí | sí |
| CI24 | 17 | Salter · cuándo hizo cine | Parte 5 · comprensión literal | no | sí |
| CI24 | 20 | The Last Book · quién lo escribió | Parte 5 · comprensión literal | no | sí |
| CI24 | 21 | Salter · qué pensaba de su trabajo en el cine | Parte 5 · comprensión literal | no | sí |
| CI24 | 24 | Swift Pizza · según el texto, el cliente… | Parte 6 · comprensión inferencial | no | sí |
| CI24 | 25 | Swift Pizza · se puede inferir que Mark… | Parte 6 · comprensión inferencial | no | sí |
| Libro | M1-1 | Parte 1 · People · el verbo «repairs» | Parte 1 · léxico: la palabra que corresponde a una descripción | a medias | sí |
| Libro | M1-19 | Parte 2 · aviso · «turbulence» | Parte 2 · avisos: dónde lo vería o qué significa | no | sí |
| Libro | M2-3 | Parte 3 · «Is this the line…?» | Parte 3 · conversación: la respuesta que va | a medias | sí |
| Libro | M3-4 | Karol G en Medellín · espacio 4 (knew) | Parte 4 · texto con espacios (gramática) | sí | sí |
| Libro | M4-2 | TWICE · ¿responde? | Parte 5 · comprensión literal | no | sí |
| Libro | M5-3 | Fotosíntesis · la tala, ¿un daño local? | Parte 6 · comprensión inferencial | no | sí |
| Libro | M5-9 | Street Music · «a cracked sidewalk», para qué | Parte 6 · comprensión inferencial | no | sí |
| Libro | M6-10 | Debating in Class · «Some debates ___ subjects» | Parte 7 · texto con espacios (léxico y gramática) | sí | sí |
| Libro | M6-22 | A Late Visitor · «Holmes rose without haste, ___» | Parte 7 · texto con espacios (léxico y gramática) | sí | sí |

</details>


## Prueba de fuego · tres preguntas muy distintas por área

Para cada área se tomaron tres preguntas reales que se parecen lo menos posible entre sí, y se
describe lo que escribe el estudiante en cada pieza del esquema nuevo. Las claves se resolvieron, no
se copiaron (y coinciden con la tabla del cuadernillo).

### Matemáticas
1. **CM26-27 · Récord olímpico 10,50 s y mundial 10,49 s: ¿se puede romper uno sin el otro?**
   (validar). ME PIDEN ☑ validar una afirmación. Datos: 10,49 s y 10,50 s. Herramienta ☑ pruebo con
   un número: en la cuadrícula dibuja una recta numérica entre 10,49 y 10,50 y pone 10,497.
   Comprobación ☑ un caso que la tumba (aquí, un caso que la confirma: 10,497 < 10,50 y > 10,49).
   Tacha B, C y D con su razón. Clave A. *Con la v1 no había dónde poner la afirmación ni el
   ejemplo.* ✔
2. **CM26-15 · Postes de 10 m y 5 m, sombra del 1 a 30°: ¿ángulo del 2?** (geometría). ☑ calcular
   un valor. Datos: 10 m, 5 m, α = 30°. ☑ figura con medidas: dibuja los dos triángulos con el sol
   en la misma dirección. Comprobación ☑ unidad y tamaño creíbles: el ángulo no depende del tamaño
   del poste. Clave C (30°). Tacha A (5°) con su razón: el ángulo no se reparte según la altura del poste. ✔
3. **CM26-43 · ¿Cuál gráfica es A(x) = x·f(x) con f(x) = 5/x?** (representar). ☑ representar.
   Datos: f(x) = 5/x, x > 0. ☑ pruebo con un número: x = 1 → 5; x = 5 → 5; x = 10 → 5. En la
   cuadrícula: siempre 5, recta horizontal. Tacha las tres gráficas que no son constantes. Clave B.
   *En la v1 «mis cuentas en orden» llevaba a calcular un único número.* ✔

### Lectura Crítica
1. **CLC26-30 · Supuesto subyacente a «todo hombre piensa que la injusticia le brinda más
   ventajas…»** (inferencia). ☑ qué supone o infiere. La evidencia: copia la frase y el párrafo.
   ☑ tesis y razones: arriba la afirmación, abajo «lo que tiene que ser cierto para que esto sea
   verdad». Trampas: A = O (dice otra cosa), C = E… Clave B. *La v1 pedía copiar palabras exactas;
   el supuesto no está escrito.* ✔
2. **CLC26-14 · ¿Qué describe mejor la caricatura?** (discontinuo). ☑ qué dice. La evidencia: «señalo
   la parte de la imagen» (recuadro: el personaje con alas y la multitud). ☑ la imagen por partes:
   divide el dibujo en cuatro y escribe qué hay en cada parte. Frase mía: «la gente ataca a alguien
   que es bueno». Trampas: C = N (no lo dice), D = R. Clave B. ✔
3. **CLC26-35 · Función del conector «Sin embargo»** (cómo se arma). ☑ cómo se arma. La evidencia:
   copia las dos frases a cada lado del conector. ☑ mapa de párrafos, en pequeño: frase 1 → «sin
   embargo» → frase 2 (contraste). Trampas en A y B: O. Clave D. ✔

### Sociales y Ciudadanas
1. **PTD7-4 · Sequía, la producción de café cae a la mitad y el precio se duplica: ¿qué conceptos?**
   ☑ qué concepto o norma. La situación: verano, Colombia, un trimestre. ☑ causa y efecto: menos
   café (oferta ↓) + los mismos compradores (demanda =) → precio ↑. La idea clave: «oferta y
   demanda: si hay menos de algo y lo quieren igual, sube». Tacha «monopolio» (no hay un solo
   vendedor). Clave C. *En la v1 había que inventar tres voces que el texto no trae.* ✔
2. **Libro M2-1 · Foro sobre celulares en clase, tres voces** (perspectivas). ☑ qué busca cada actor.
   ☑ la mesa de las voces: dibuja tres círculos alrededor de la situación con quién y qué busca. Lo
   que está en juego: el derecho a la educación frente a la libertad. Es la pregunta de la v1, y
   sigue funcionando igual. ✔
3. **Cuaderno M5 · ICFES 4 · Real Audiencia y encomienda: el propósito de las medidas** (histórico).
   ☑ qué concepto o norma. La situación: siglo XVI, Santa Fe de Bogotá, la Real Audiencia. ☑ línea
   de tiempo: conquista → encomienda (indígenas como recompensa) → 1557 jornal de tres gramos de oro
   → 1560 se prohíbe el trabajo gratuito. La idea clave: «el propósito de una norma se lee en quién
   queda distinto: el encomendero pierde el trabajo gratis». Tacha D (fortalecer a los
   encomenderos: dice lo contrario). Clave B. ✔

### Biología
1. **CCN-38 · Dos patos de cuello largo tienen 3/4 hijos de cuello largo y 1/4 de corto: ¿genotipo
   de los padres?** (genética). ☑ explicar un proceso. Escala: organismo. ☑ cruce de genes: Aa × Aa
   en el cuadro de cuatro casillas → AA, Aa, Aa, aa = 3 : 1. Lo que sí concluyo: los dos son
   heterocigotos. Clave A. *La v1 no tenía dónde hacer el cruce.* ✔
2. **CCN-40 · Polilla de la cera: ¿qué pregunta puede resolverse con una investigación de Ciencias
   Naturales?** (indagación). ☑ leer datos o un experimento. Escala: población. ☑ control y prueba:
   «¿qué cambiaría, qué mediría?» para cada opción; la B (economía de los apicultores) no se mide
   con ciencias naturales. Lo que no alcanza: «la pérdida económica es otra ciencia». Clave A. ✔
3. **CCN-21 · Red trófica: ¿qué pasa si se extingue el atún?** (predecir). ☑ predecir qué pasa si…
   Escala: ecosistema. ☑ cadena de causas sobre la red: sin atún → aumenta el pez que el atún se
   comía → baja el pez loro, que es su presa. Lo que cambia: el atún. Clave A. ✔

### Química
1. **CCN-18 · 124 g de P₄ con 210 g de Cl₂: ¿reactivo límite?** (estequiometría). ☑ calcular una
   cantidad. Nivel: el símbolo y el número. En el vaso: P₄ 124 g/mol, Cl₂ 70 g/mol. ☑ cuenta con
   unidades: 124 g ÷ 124 = 1 mol de P₄ pide 6 mol de Cl₂; hay 210 ÷ 70 = 3 mol → el Cl₂ se acaba
   primero. ☑ átomos y masa cuadran. Clave A. ✔
2. **CCN-8 · Una sustancia de una fase que deja un sólido al calentarse y otra con dos fases: ¿qué
   mezclas son?** (clasificar). ☑ clasificar o identificar. Nivel: lo que se ve. ☑ antes y después
   (calentar la 1; mirar la 2). Lo que decide: «homogénea = uniforme; heterogénea = se ven fases».
   Clave A. *En la v1 los vasos de antes y después no tenían una reacción que mostrar.* ✔
3. **CCN-33 · Densidades del agua, etanol y aceite medidas a temperaturas distintas: ¿por qué está
   mal planteado?** (diseño experimental). ☑ leer datos o un experimento. Nivel: lo que se ve. ☑
   control y prueba: lo que cambio = el líquido; lo que mido = la densidad; lo que debía dejar igual
   = la temperatura (y no la dejó). Clave A. *La v1 no tenía variables.* ✔

### Física
1. **CCN-14 · La lluvia cae vertical para los de afuera: ¿qué vector ven los del bus?** (vectores).
   ☑ escoger gráfica o diagrama. Predigo: si el bus avanza, la lluvia se ve inclinada hacia atrás.
   ☑ fuerzas y vectores: suma la velocidad de la lluvia y la contraria a la del bus. Clave B. ✔
2. **CCN-13 · Tres objetos de igual volumen y forma, distinto material, caen en tiempos distintos:
   ¿qué pregunta se puede contestar?** (indagación). ☑ evaluar un experimento. ☑ control y prueba:
   lo que cambió = el material (y con él la masa); lo que se dejó igual = volumen, forma y altura;
   lo que se midió = el tiempo. Si la gravedad es la misma y los tiempos no, la fuerza neta no es la
   misma: eso sí se puede contestar. Tacha A (la altura no cambió) y D (la forma no cambió). Clave C. *La v1 hacía dibujar un
   sistema que no responde la pregunta.* ✔
3. **CCN-22 · 1 L de agua sube de 15 a 17 °C en 1 minuto: ¿y 2 L en la misma estufa?** (calor).
   ☑ explicar o predecir. Predigo: si la masa aumenta, la temperatura sube menos. Magnitudes:
   ΔT₁ = 2 °C, m₂ = 2 m₁. ☑ energía por tramos: la misma energía repartida en el doble de agua →
   ΔT = 1 °C → 16 °C. Ley: Q = m·c·ΔT. Clave C. ✔

### Inglés
1. **CI24-6 · Aviso «Draw a line to complete the snake and color it»: ¿dónde lo ve?** (Parte 2).
   ☑ dónde o quién. Lo que dice: «dibuja una línea para completar la culebra y coloréala». ☑ dónde lo
   veo. Pista ☑ quién habla (alguien que da instrucciones a un niño). Descarté A «on a rug» porque
   en un tapete no se escribe. Clave B. *En la v1 no había hueco ni palabra que poner.* ✔
2. **CI24-15 · «doctors say you ___ believe this» · mustn't / couldn't / wouldn't** (Parte 4).
   ☑ la palabra que va. La línea que manda: la copia con el hueco. ☑ la palabra que falta. Pista ☑
   la palabra de al lado (say: un consejo, una orden). Clave A. Es la pregunta de la v1. ✔
3. **CI24-25 · «It can be inferred from the text that Mark…»** (Parte 6). ☑ qué dice o deja
   entender. ☑ la línea que responde: «It certainly feels great to find new excellent food delivery
   companies for whenever you don't feel like cooking». Lo que dice: a veces no quiere cocinar y le
   gusta pedir comida rápida. Descarté A («does not like cooking»: exagera), B y D. Clave C. ✔

**Resultado:** las 21 preguntas caben. Las dos que quedan **a medias** en la tabla (valorar una
propuesta en Biología y en Química: CTS) también caben, pero el «a favor / en contra» se hace en el
lienzo libre porque ninguna herramienta lo dibuja; no se agregó una quinta herramienta porque no
cabe sin quitarle espacio al lienzo (ver decisiones).


## Lo que la v2 no resuelve sola (riesgos)

1. **Hay que enseñar la caja de herramientas.** Un dibujito con dos palabras no basta la primera
   vez. Propuesta: la clase 7 del planeador de cada área dedica 5 minutos a las cuatro herramientas,
   con una pregunta del simulacro ya resuelta en cada una. Sin esto, el lienzo libre se queda vacío.
2. **El lienzo libre es más difícil de auditar** que un formato cerrado. Lo compensa que todo lo
   demás sigue siendo marcable: tipo de tarea, herramienta, comprobación o trampas, tacho con
   razón. La coordinación puede revisar «marcó el tipo y la herramienta, y tachó con razón» sin
   leer el lienzo.
3. **Mismo esqueleto en las siete áreas.** Fue deliberado (el estudiante aprende UNA forma de
   socializar y la usa en todas), pero se arriesga a que Nelson lo vea como «la misma tabla de
   colores distintos». Lo que lo evita: las piezas propias de cada área (el óvalo de la situación,
   el vaso, las comillas, la lupa, la cuadrícula, los puntos) y los dibujitos. Hay que verlo impreso.
4. **La tabla de cobertura de la v2 es una evaluación de diseño**, hecha por quien diseñó. La prueba
   de fuego la respalda, pero la prueba real es la clase 8 con estudiantes.


## Lo que Nelson tiene que decidir

1. **¿La v2 o volver a la v1 con ajustes?** La v1 sirve bien para 1 de cada 5 preguntas.
2. **Los nombres nuevos**: Sociales «La situación y sus lentes», Química «Lo que veo, las partículas y
   el número», Inglés «La parte, la pista y la respuesta».
3. **¿Quién enseña la caja de herramientas?** Propuesta: 5 minutos al comienzo de la clase 7 (va en
   los planeadores que faltan).
4. **CTS en Biología y Química**: ¿se acepta hacer el «a favor / en contra» en el lienzo libre, o se
   cambia una herramienta? (por ejemplo, en Biología «cruce de genes» por «a favor y en contra» y el
   cruce se hace en el lienzo; genética es 3 de 24 preguntas en la muestra, CTS 2 de 24).
5. **Lectura Crítica**: el cuadernillo del 9 sept 2026 trae las mismas preguntas que el del 16 feb
   (como Ciencias 2025 y 2026). Queda registrado como «Atención»; no hay que hacer nada con el
   cuaderno.

Hallazgos registrados en `tablero/propuestas/simulacro_hallazgos.csv` (para pasar a `tablero/hallazgos.csv`).

Archivos: `libro/simulacro.py` (v2), `libro/simulacro_v1.py` (la anterior, intacta; sus muestras
salen como `sim_v1_muestra_<área>.svg`), `libro/sim_muestra_<área>.svg` (las 7 muestras nuevas) y
`/tmp/claude-0/simulacro/Simulacro_muestras_v2.pdf`.
