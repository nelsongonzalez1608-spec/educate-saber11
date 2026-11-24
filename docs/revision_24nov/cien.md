# Revisión de Ciencias Naturales: Biología, Química y Física (p. 166–312)

Revisor: Ciencias Naturales · 24 nov 2026 · solo lectura (no se modificó ningún archivo del repositorio).
Material: `entregables/Cuaderno_Saber11_completo_398_paginas.pdf`, `fuente_libro/{BIOLOGIA,QUÍMICA,FÍSICA}`, `entregables/EDUCATE_Planeador_{Biologia,Quimica,Fisica}.pdf`, `entregables/guias_{biologia,quimica,fisica}/*Clase1–6*.html`, `tablero/icfes.csv` y `tablero/misiones.csv`.

## Método

- **Estructura:** saqué con `pdftotext` las 147 páginas (cabecera, «hoja n de 5 · preguntas a y b», pie y número de página) y lo comparé por programa.
- **Libro:** busqué en los 42 PDF del libro la página donde empieza cada una de las 180 preguntas del taller y la comparé con «la lees en tu libro, página N». Los casos que el programa no resolvió los revisé a mano; en Física M2 comparé también el contenido.
- **Entrenamiento:** rasterizé y miré las 36 páginas (72 preguntas). Resolví cada pregunta (cuentas, gráficas y figuras ampliadas) y comparé la clave en cuatro fuentes: cuaderno, planeador, guía (`data-k` y texto de la opción) y `icfes.csv`.
- **Estrategias:** comparé por programa los nombres de las estrategias en los chips del cuaderno, `misiones.csv`, las guías y los planeadores.
- **Portadas y simulacros:** revisé las tres portadas de área y la numeración de los tres simulacros.

## Resultado general

- **Claves:** las 72 claves de entrenamiento están bien. Las resolví y coinciden en las cuatro fuentes (cuaderno, planeador, guía y `icfes.csv`). Cada clave está al lado de su pregunta, en el mismo orden P1…P4. El planeador cita la página correcta del cuaderno.
- **Membrete:** las 72 tarjetas dicen exactamente «Pregunta Saber 11». En p. 166–312 no aparece «oficial» ni un año.
- **Libro:** las 180 citas «la lees en tu libro, página N» coinciden con la página real donde empieza la pregunta en el libro de esa misión.
- **Estructura:** las 18 misiones están completas. Las 7 páginas van en el orden taller, taller, ICFES, taller, taller, taller, ICFES. Las cabeceras traen el área y la misión correctas; «hoja n de 5 · preguntas a y b» va en secuencia; el pie lleva el número de página correcto.
- **Estrategias:** las 4 estrategias de cada misión son idénticas en cuaderno, planeador, guía y `misiones.csv`.
- **Portadas:** las de p. 166, 215 y 264 traen los 6 momentos y el rango de páginas correcto (166–214, 215–263 y 264–312).
- **Simulacros:** p. 209–214, 258–263 y 307–312 numeran las preguntas 1–18 de forma consecutiva, en 3 hojas de 2 caras.
- **Mayúsculas:** «EDUCATE» no aparece en minúsculas.

## Hallazgos

| página | severidad | qué está mal | evidencia | corrección propuesta |
|---|---|---|---|---|
| 180 (2.ª tarjeta, Bio M2 P4) · 190 (1.ª, Bio M4 P1) · 229 (1.ª, Qui M2 P3) · 236 (2.ª, Qui M3 P4) · 239 (2.ª, Qui M4 P2) · 281 (2.ª, Fís M3 P2) · 285 (1.ª, Fís M3 P3) · 292 (2.ª, Fís M4 P4) | **alta** | En 8 tarjetas de entrenamiento falta la fila de círculos A B C D bajo «MARCO AL FINAL». Bajo el rótulo no hay nada, así que el estudiante no tiene dónde marcar. Coinciden con las preguntas cuyas opciones son figuras o gráficas. | Lo vi en las imágenes de las 8 páginas. Además, `pdftotext -bbox` no encuentra las letras A–D junto a ese rótulo, y en las otras 64 tarjetas sí aparecen. | Revisar `taller_base.hoja_icfes()` o el recorte en `rehace_hojas.py` en las preguntas con opciones gráficas (`o=` con figuras), regenerar esas 8 páginas y volver a verlas. |
| 190 (Bio M4 P1) | media | El enunciado dice «Al leer la información del contexto…», pero el contexto de las pectinasas no está impreso en el cuaderno. La pregunta se puede resolver solo con la hipótesis, pero la referencia queda colgando. | Imagen p. 190. La p. 194 sí transcribe el contexto («Del contexto que comparte con otras preguntas: …»). | Agregar 1–2 líneas del contexto de las pectinasas, o cambiar a «Un investigador piensa que…». |
| 190, 225, 201, 208 y otras | atención | El texto de algunos chips de estrategia (rotados) roza o sobrepasa el borde de su recuadro, por ejemplo «Lo que la evidencia respalda (y lo que no)» en p. 190 y «Donde la temperatura se queda quieta» en p. 225. | Imágenes a 110 ppp. | Medir con `tw()` y ensanchar el chip; confirmarlo en la prueba impresa. |
| 222 (Qui M1 P3) | atención | La tabla de solubilidad da CO₂ = 0 g/kg a 80 °C. En la realidad es pequeña pero no cero. El dato viene de la fuente (SIM II 2023) y no cambia la clave D. | Tabla p. 222. | Dejarlo y anotarlo en `hallazgos.csv` («dato de la fuente»). |
| 243 (Qui M4 P3) | atención | La tabla de la fuente trae datos irreales: ácido sulfúrico con densidad 2,7 g/mL (la real es 1,83) y punto de ebullición del HCl a 48 °C. No cambia la clave B. | Tabla p. 243. | Registrar como «Atención»; opcional: avisar en la guía del profe. |
| 250 (Qui M5 P4) | media | La tabla del aceite de palma llama «Capacidad calorífica (MJ/kg)» a 39,5 y 45,4, y la nota la define como «energía necesaria para aumentar un grado la temperatura». Esos valores son el poder calorífico, no la capacidad calorífica. Es un error conceptual en un cuaderno de química, aunque no cambia la clave C. | Tabla y nota al pie de p. 250. | Cambiar a «Poder calorífico (MJ/kg)» y corregir la nota, o dejarlo como «Corrección EDUCATE». Registrar en `hallazgos.csv`. |
| 187 (Bio M3 P3) | atención | La tabla dice «Gas natural · Propano (C3H8)», cuando el gas natural es sobre todo metano. Además las fórmulas van sin subíndices (H2O, CO2, C3H8). | Imagen p. 187. El planeador ya lo menciona. | Poner subíndices (H₂O, CO₂, C₃H₈). El dato del propano queda como «Atención». |
| 267 (Fís M1 P1) y 274 (Fís M2 P1) | atención | Estas 2 preguntas vienen del compilado ASED, que no es del ICFES, y llevan el mismo membrete y la misma tarjeta que las demás. Las claves (C y C) están bien. | `icfes.csv`: «ASED pre código 11 … ítem 13 / ítem 10». | Decisión de Nelson (CLAUDE.md §9.3): reemplazarlas por preguntas de cuadernillos liberados. Mientras tanto, la guía debe decir «Fuente: compilado ASED (no es del ICFES)». |
| p. 169–306 (36 páginas de entrenamiento) | atención | La cabecera y el pie dicen «ENTRENAMIENTO ICFES», y cada tarjeta dice «(el libro y el ICFES preguntan lo mismo de otra forma)». La regla del 10 nov quitó «ICFES» del membrete y prohíbe decirle al estudiante que son «preguntas reales del ICFES». Esto no dice «reales», pero sí asocia al ICFES preguntas del ASED y del simulacro. | Texto de todas las páginas de entrenamiento. | Que Nelson decida si cambia a «ENTRENAMIENTO SABER 11» y «(el libro y el Saber 11 preguntan…)». |
| `tablero/icfes.csv` (QUI M1 y M2: 4 filas) | atención | El estado dice «Usada (por confirmar procedencia)» para preguntas del SIMULACRO II 2023, aunque CLAUDE.md §9.3 dice que Nelson confirmó que son reales del ICFES. El tablero quedó desactualizado. | Filas QUI M1 (botellas, solubilidad) y QUI M2 (sustancias fundidas, hielo). | Actualizar el estado a «Usada». |
| 201 y 208 (Bio M5 P3–P4 y Bio M6 P3) | atención | El mismo contexto del dengue se usa en 3 preguntas de dos misiones distintas. | Imágenes p. 201 y 208. | Aceptable. Si se quiere variedad, cambiar una en M6. |
| 183 (Bio M3) | atención | La primera página ICFES pone la pregunta 3 antes que la 2 (los círculos numerados quedan 3 y luego 2), aunque la cabecera dice «estrategias 2 y 3». | Imagen p. 183. | Opcional: intercambiar el orden de las tarjetas. |
| 225 (Qui M2 P1) | atención | La columna «Tiempo» de la tabla no tiene unidad, pero la opción A habla de «50 segundos». | Imagen p. 225. | Poner «Tiempo (s)» en la tabla, si la fuente lo permite. |

**Conteo:** alta 1 (8 tarjetas) · media 2 · atención 10.

## Verificado correcto, misión por misión

- **Bio M1 (167–173):** estructura y citas al libro (p. 72–75) correctas. Las claves de entrenamiento A, A, D, C están resueltas y coinciden en cuaderno, planeador, guía y csv.
- **Bio M2 (174–180):** estructura y citas al libro (p. 83–85) correctas. Claves B, D, A, A coinciden. Falta la fila A–D en P4 (ver tabla).
- **Bio M3 (181–187):** estructura y citas al libro (p. 94–97) correctas. Claves C, D, A, D coinciden.
- **Bio M4 (188–194):** estructura y citas al libro (p. 104–107) correctas. Claves B, A, C, D coinciden. Falta la fila A–D en P1 y falta el contexto de las pectinasas.
- **Bio M5 (195–201):** estructura y citas al libro (p. 116–119) correctas. Claves C, A, D, B coinciden.
- **Bio M6 (202–208):** estructura y citas al libro (p. 127–130) correctas. Claves A, D, B, A coinciden.
- **Qui M1 (216–222):** estructura y citas al libro (p. 140–142) correctas. Claves C, C, D, B coinciden (en la de las botellas comprobé las cuatro combinaciones de propiedades).
- **Qui M2 (223–229):** estructura y citas al libro (p. 150–152) correctas. Claves B, A, C, A coinciden. Falta la fila A–D en P3.
- **Qui M3 (230–236):** estructura y citas al libro (p. 160–162) correctas. Claves B, B, C, D coinciden. En la de cinética, X es de orden 1 y W de orden 2: el experimento 3 da 300 y el 6 da 900. Falta la fila A–D en P4.
- **Qui M4 (237–243):** estructura y citas al libro (p. 170–173) correctas. Claves C, A, B, A coinciden. Falta la fila A–D en P2.
- **Qui M5 (244–250):** estructura y citas al libro (p. 182–185) correctas. Claves B, C, C, C coinciden (H₂CO₃ = 62 g/mol; densidades 0,83 y 0,625).
- **Qui M6 (251–257):** estructura y citas al libro (p. 193–196) correctas. Claves B, A, D, A coinciden (en la figura B del Mg²⁺ conté 12 p⁺ y 2 + 8 electrones).
- **Fís M1 (265–271):** estructura y citas al libro (p. 205–208) correctas. Claves C, D, C, D coinciden. P1 es del ASED.
- **Fís M2 (272–278):** estructura y citas al libro (p. 216–218, también comparé el contenido) correctas. Claves C, C, B, A coinciden. P1 es del ASED.
- **Fís M3 (279–285):** estructura y citas al libro (p. 226–228) correctas. Claves B, A, A, A coinciden. Falta la fila A–D en P2 y P3.
- **Fís M4 (286–292):** estructura y citas al libro (p. 236–239) correctas. Claves D, C, C, B coinciden. Falta la fila A–D en P4.
- **Fís M5 (293–299):** estructura y citas al libro (p. 247–250) correctas. Claves A, D, A, D coinciden (comprobé que el momento se conserva en los 4 lanzamientos).
- **Fís M6 (300–306):** estructura y citas al libro (p. 259–262) correctas. Claves B, C, D, B coinciden.

## Lo que no alcancé a revisar

- **Libro, a fondo:** no comparé una por una las 180 preguntas del taller con el contenido del libro. Comparé la página y el número de cada pregunta (las 180 coinciden) y el contenido completo solo en Física M2.
- **Talleres:** no revisé uno por uno los 180 instrumentos del taller (que ninguno delate la respuesta ni se desborde). En las 72 tarjetas de entrenamiento no vi ninguna pista tipográfica de la clave.
- **Guías:** no abrí las guías en Playwright; solo extraje sus claves y sus textos.
- **Clases 7 y 8:** no revisé las guías de simulacro y devolución.
