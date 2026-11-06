---
name: educate-saber11
description: Procedimiento para construir el cuaderno Saber 11 de EDUCATE · Para el Saber — una misión del cuaderno, un planeador del docente o una guía de clase proyectable — con las reglas del proyecto, los verificadores y la revisión visual obligatoria.
---

# Cuaderno Saber 11 · EDUCATE · cómo se hace cada trabajo

Antes de usar esta skill, lee `CLAUDE.md` (reglas, arquitectura, lecciones) y
`RECUPERACION.md` (qué falta reconstruir). Esta skill es el procedimiento; las reglas
están allá y mandan sobre lo que diga aquí.

Responde a Nelson en español, directo y cálido. Si algo tiene riesgo real para él o para
EDUCATE, díselo de frente.

---

## A. Construir una misión del cuaderno (7 páginas)

**Entrada:** área, número de misión, páginas del libro fuente.
**Salida:** 7 SVG (5 de taller + 2 de ICFES), PDF carta, filas nuevas en el tablero.

1. **Leer las 10 preguntas del libro** en el PDF del libro fuente (`1. Grado.11.°.pdf`),
   renderizando las páginas con `pdftoppm -r 150 -jpeg`. Anotar enunciado, opciones y
   figura de cada una.
2. **Resolver las 10 a mano, contra el texto o la figura.** Nunca copiar la clave del libro.
   Escribir las claves verificadas en el docstring del módulo: `1·D  2·C  3·C …`.
   Todo lo que no cuadre —clave errada, dos opciones correctas, enunciado que no concuerda
   con la clave, figura que contradice el texto, errata— **se registra** en
   `tablero/hallazgos.csv`, con severidad Alta / Media / Baja / Atención.
3. **Revisar el reparto de claves** de la misión. Si una letra concentra la mitad, se registra.
4. **Definir las 4 estrategias** de la misión. Cada pregunta queda asignada a una.
5. **Diseñar un instrumento de pensamiento distinto para cada pregunta.** Antes de dibujarlo,
   revisar `tablero/instrumentos.csv`: ningún título puede repetirse en el cuaderno y ningún
   instrumento puede parecerse a otro. El instrumento obliga a hacer el razonamiento; nunca
   lo da hecho.
6. **Que ningún instrumento delate la respuesta**: la opción correcta no lleva borde distinto,
   ni las demás van en mayúsculas, ni la correcta es la única más larga.
7. Si la pregunta exige un concepto que el estudiante no trae (eufemismo, alegoría,
   combinatoria, razón trigonométrica…), poner el sello **«Alto · aquí entra el profe»** y
   registrarlo en la matriz: es una deuda con el planeador.
8. Si el texto de la pregunta es largo, el cuaderno trae **el párrafo con la evidencia** y la
   referencia; el texto completo va a `TEXTOS_GUIA_DOCENTE.md` con «lo que el profesor debe
   hacer notar». Criterio: con lo impreso, el estudiante tiene que poder responder solo.
9. **Elegir 4 preguntas oficiales del ICFES** para el entrenamiento, una por estrategia.
   Revisar `tablero/icfes.csv` para no repetir. Resolverlas a mano.
   **Membrete con año solo si se verificó contra el cuadernillo liberado**; si no,
   «Pregunta oficial ICFES · Saber 11». Con el ASED, anotar siempre la sección: su
   numeración se reinicia.
10. Construir los SVG con el motor (`taller_base.py`). Diario personal en cada hoja: fecha,
    caritas llego/salgo, «mi primera idea antes de hacer nada», «lo que me llevo».
11. **Verificadores** (deben pasar todos): `verifica_cajas.py`, `verifica_pistas.py`,
    `extrae_instrumentos.py` (sin títulos repetidos), `render.verifica(pdf, marca="Aprende")`.
12. **Revisión visual de las 7 hojas**: `rsvg-convert -w 1000` y mirar cada una. Buscar texto
    que se monta, que se sale, que queda cortado, rótulos que pisan la columna vecina, gris
    ilegible, glifos raros. Corregir y volver a mirar.
13. Actualizar el tablero: `misiones.csv`, `icfes.csv`, `hallazgos.csv`, `avance.csv`,
    `instrumentos.csv`, y decirle a Nelson qué se registró.

## B. Construir el planeador del docente de un área (24 hojas)

Modelo: `piloto/paquete_mision1_aprobado/2_docente/Mate_Mision1_PLANEADOR.pdf`.
Motor: `libro/plan_piezas.py`. Ejemplo completo: `libro/plan_lc.py`.

1. `plan_<área>.py` con `configurar(color, bg, línea, nombre, 24)`.
2. Los datos del área: `FASES` (reparto **15 · 20 · 35 · 20 · 20 · 10**, que no se cambia),
   `CLASES` (8), `MISIONES` (componente, páginas, competencia, las 4 estrategias, qué instalar,
   ojo con esto, cierre), `AVISOS` (los hallazgos del libro con qué hacer en clase).
3. **Las 24 dinámicas**, 4 por misión. Cada una debe ser **isomorfa a su estrategia**: lo que
   hace el cuerpo es el mismo movimiento que después hará la mente. Si no se puede decir qué
   paso de la estrategia ejercita, se descarta. Cómo se hace (4 pasos), qué movimiento mental
   entrena (con las preguntas que sirve) y material.
4. **6 retos del corte**, uno por misión, 20 minutos, discusión en equipo y registro individual.
5. Hojas: cómo se usa · las 8 clases + las 24 estrategias · los 120 minutos (2 hojas, con
   **«TU APORTE»** en cada momento) · por clase dos hojas (estrategias, sellos, las 10
   preguntas con su instrumento y avisos / minuto a minuto, textos a proyectar, las 4 ICFES
   con clave, registro del docente) · clases 7 y 8 · 6 hojas de dinámicas · cierre.
6. `verifica_plan.py` sin problemas, `verifica_claves.py` sin desalineaciones,
   `render.verifica(pdf, marca="PLANEADOR")` y revisión visual de las 24.

## C. Construir las 8 guías de clase de un área («clase viva»)

Modelo: `piloto/paquete_mision1_aprobado/3_presentaciones/Clase_viva_estudiantes.html`.
Ejemplo completo: `libro/clase_viva_lc.py`.

1. Una por clase. Las 6 de contenido: portada · reglas · activación (una frase corta inventada,
   y la guía lo dice) · dinámica E1 · pregunta modelo con conteo de manos · 5 bloques de 2
   preguntas con 3 dinámicas intercaladas · reto del corte · 4 ICFES con su texto · cierre.
   Clase 7: simulacro con reloj de 90 minutos y conteo por competencia. Clase 8: el profe
   escoge las 5 más falladas y se reparan.
2. Guía del profe (tecla G) en cada diapositiva: objetivo, qué haces y qué dices, lo que no
   haces, y **«Si [el área] no es tu fuerte»**: la explicación de cada sello en palabras
   simples, los avisos del libro y lo que el profesor debe hacer notar.
3. Las claves salen de los módulos verificados, nunca escritas a mano en la guía.
4. Prueba en Playwright, recorriendo todas las diapositivas: cero errores de JavaScript,
   **ninguna clave visible antes de revelarla**, nada que se salga de ancho, y que al revelar
   aparezca la clave correcta. Revisar capturas a 1600 × 900.
5. Nada de filetes horizontales de adorno en las barras.
6. Entregar en un .zip con las 8, más la clase 1 suelta para que Nelson la abra de una vez.

## D. Al terminar cualquier trabajo

- Corregir lo que encontraron los verificadores **antes** de mostrar nada.
- Decirle a Nelson en pocas líneas qué quedó, qué se registró como hallazgo y qué tiene que
  decidir él. Lo que escribiste tú y debería revisar un especialista, dilo.
- `git commit` con lo construido.
