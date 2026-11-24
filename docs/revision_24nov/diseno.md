# Revisión de diseño e imprenta · Cuaderno Saber 11 (398 páginas)

Revisado el 24 nov 2026. No se modificó ningún archivo del repositorio.

Material:
- Pantalla: `entregables/Cuaderno_Saber11_completo_398_paginas.pdf` (21 nov)
- Imprenta: `entregables/imprenta/Cuaderno_Saber11_imprenta_CMYK_398_paginas.pdf` (24 nov, PDF/X-4) y `libro/imprenta.py`

Cómo se revisó:
- Se rasterizaron las 398 páginas a 50 ppp y se miraron en hojas de contacto de 6 páginas. Las dudosas se ampliaron a 150–200 ppp (p. 4, 8, 14, 26, 169, 170, 236, 334, 343).
- La versión de imprenta se rasterizó a 30 ppp. Las 8 páginas con color a sangre y 6 páginas pares e impares se midieron a 72–144 ppp.
- Con pdfplumber se extrajeron, para cada página, el pie, el número impreso, los tamaños de letra, los colores del texto y las fuentes.
- Herramientas usadas también: pdffonts, pdfimages, pikepdf (cajas) y pdftotext (reglas de texto).

Aviso sobre el alcance: en las páginas 19–144 la revisión visual a 50 ppp se hizo una sola vez y las notas de ese tramo no quedaron por escrito; no se volvieron a abrir una por una. Sí pasaron por todos los controles automáticos (pie y número, tamaños, colores, fuentes y texto).

## Hallazgos

| página | severidad | qué está mal | evidencia | corrección propuesta |
|---|---|---|---|---|
| todas (397 de 398) | **alta** (decisión antes de imprimir) | La letra es muy pequeña en el PDF de imprenta. El cuaderno se reduce al 93 % para dejar el lomo de 2 cm. | Medido con la matriz real de cada glifo:<br>· el 36,6 % de los caracteres (466 130) queda por debajo de 5 pt, en las 398 páginas;<br>· el 21,6 % queda por debajo de 4,5 pt, en 397 páginas;<br>· el 8,1 % queda por debajo de 4 pt (102 687 caracteres), en 397 páginas.<br>Tamaños más usados en pantalla: 4,3 · 4,6 · 4,9 · 5,2 · 5,5 · 6,1 pt, que en imprenta quedan en 4,0 · 4,3 · 4,6 · 4,8 · 5,1 · 5,7 pt.<br>Por debajo de 3 pt solo hay 7 páginas: p. 4 (miniatura de la hoja, intencional) y p. 209–214 (íconos «a/A» de 2,6 pt en el simulacro de Biología). | No imprimir el tiraje sin la prueba física de 10 páginas (`Prueba_imprenta_10_paginas.pdf`). Si los rótulos de 4 pt se empastan, subir los rótulos (14–15 u) a ≥ 17 u y el texto corrido a ≥ 19 u. La otra salida es bajar la reducción a 0,95 con un lomo de 1,8 cm. |
| 103–112 (imprenta) | **alta** (preflight) | Errores de sintaxis en el contenido del PDF de imprenta. Solo aparecen en la versión CMYK; el PDF de pantalla de esas páginas está limpio. | Poppler dice 3 veces por página: «Syntax Error: No current point in closepath». Son 30 avisos en el simulacro de Lectura Crítica y vienen de un mismo objeto compartido. Es un trazado que Ghostscript escribió con `h` sin punto actual. | Correr el preflight (Acrobat o pdfToolbox) en esas 10 páginas antes de mandar a la litografía. Si falla, regenerar ese tramo o limpiar el trazado de origen en la plantilla del simulacro de LC. Comparar el render de p. 103 entre pantalla e imprenta. |
| 1, 7, 60, 113, 166, 215, 264, 313 (imprenta) | media | Se ve un filete claro en el color a sangre, justo donde termina la página escalada (al 93 %) sobre el fondo agregado por `imprenta._fondo()`. | En p. 7 a 144 ppp, en el borde de la página encajada, se ve un rectángulo de línea clara dentro de la franja: (68, 93, 157) contra (45, 74, 145) del azul. Lo mismo pasa en p. 60. Dentro de la franja hay una línea horizontal y dos verticales.<br>Puede ser solo el suavizado del visor, pero contradice la regla de «nada de líneas horizontales» si sale en la prueba. | Revisar este punto en la prueba física de p. 1, 7 y 313. Para eliminarlo de raíz: en las páginas de FONDOS, recortar la franja de la página original o sobreponer el fondo con un pequeño solape (trapping). Lo ideal es dibujar la franja del original en el tamaño final en vez de escalarla. |
| todas (imprenta) | atención | La cuadrícula de puntos de fondo (K18) queda a 4,6 mm del corte exterior. Bajo el límite pedido de unos 5 mm. | Medido en p. 2, 3, 100, 101, 396 y 397: la tinta oscura queda a 0,74 cm del exterior y a 2,12 cm del lomo. Con los puntos claros, queda a 0,46 cm del exterior y a 1,80 cm del lomo. | Es decorativo y un corte desviado no pierde nada. Si la litografía lo pide, recortar la cuadrícula a ≥ 5 mm (de 40–1960 u a 60–1940 u). |
| 1, 7, 60, 113, 215, 313 | atención | Las notas a mano de las portadas usan glifos que Caveat no tiene: → θ ✓ ₂. El respaldo los dibuja con Z003 (Zapf Chancery) e Inter, que no son fuentes del proyecto. | pdffonts muestra Z003-MediumItalic e Inter-Regular solo en esas páginas. Glifos afectados: p. 1 «→θθ✓», p. 7 «✓», p. 60 «→», p. 113 «→→», p. 215 «₂₂ →₂₂» (fórmulas de Química), p. 313 «→».<br>Todo está incrustado y no hay riesgo de imprenta, pero la letra no queda homogénea. | Para esos glifos, usar Shantell Sans o dibujar la flecha en SVG. En Química, escribir H2O con `baseline-shift` en vez del subíndice Unicode. |
| 8–49, 61–102, 114–127 | atención | Hay texto oculto duplicado bajo cada hoja rehecha: la página original queda debajo del recorte, como describe `arma_pdf.py`. | En la capa de texto aparecen flechas «→» en #BFD4F2 y una copia del texto original, por ejemplo en el salvavidas de p. 8. A 150 ppp no se ven: están tapadas.<br>Con la petición de sobreimprimir el negro, un objeto K100 oculto no aparece mientras lo tape un objeto no negro. | No hay que cambiar nada para imprimir. Sí conviene avisarle a la litografía que hay contenido tapado, por si su flujo aplana o aplica sobreimpresión a todo. |
| 14 | atención | La nota al pie del instrumento («Tres opciones dejan algo por fuera…») es un párrafo de 2 líneas en bandera, sin justificar. | Ampliación a 150 ppp. | Pasarla por `parrafo_j()` como el resto del texto corrido (regla 2). |
| 91 páginas de entrenamiento | atención | La cabecera dice «ENTRENAMIENTO ICFES», pero varias preguntas vienen del ASED, que no es del ICFES. | pdftotext: «ENTRENAMIENTO ICFES · ENTRENA LAS ESTRATEGIAS 1 Y 2 · 2 PREGUNTAS SABER 11» en 91 páginas. El membrete sí dice «Pregunta Saber 11», como pide la regla del 10 nov. | Decisión de Nelson: cambiar a «ENTRENAMIENTO SABER 11», en línea con la regla de no decir «del ICFES» donde lo ve el estudiante. |
| 396 | atención | «Mi puntaje frente a mi meta» tiene 6 columnas: Global, Mate, LC, Sociales, C. Naturales e Inglés. El cuaderno usa 7 áreas. | Hoja de contacto. Es coherente con las 5 pruebas reales del ICFES. | Ninguna, si es intencional. Se anota para que no parezca un error frente a las 7 portadas. |
| 1 | atención | El logo es una imagen raster. | pdfimages: 300 × 140 px a 326 ppi en imprenta. Es suficiente, pero la tilde de «Edú» no se ve sobre el azul, como ya se sabía. | Reemplazarlo por el logo en vector cuando llegue. |

## Lo que está bien

**Paginación y pies**
- Las 398 páginas están completas, en el orden del mapa de CLAUDE.md:
  - Apertura: 1–6
  - Matemáticas: 7–59 (simulacro 50–59)
  - Lectura Crítica: 60–112 (simulacro 103–112)
  - Sociales: 113–165 (simulacro 156–165)
  - Biología: 166–214 (simulacro 209–214)
  - Química: 215–263 (simulacro 258–263)
  - Física: 264–312 (simulacro 307–312)
  - Inglés: 313–395 (simulacro 390–395)
  - Cierre: 396–397
  - Mensaje final: 398
- No hay páginas en blanco ni duplicadas.
- El pie dice «Aprende · Practica · Avanza» en las 398 páginas.
- El número impreso coincide con la posición en el PDF en las 397 páginas numeradas. La portada no lleva número y su pie dice «EDUCATE · Aprende · Practica · Avanza».

**Cabeceras, colores y portadas**
- Las cabeceras son consistentes: área / misión, componente, fecha «Sábado __ de __», caritas llego/salgo y hoja n de 5.
- Cada área está en su color de CLAUDE.md, tanto en cabecera como en portada:
  - Matemáticas: azul
  - Lectura Crítica: rojo
  - Sociales: oro
  - Biología: verde hoja
  - Química: esmeralda
  - Física: oliva
  - Inglés: turquesa
- Las 7 portadas de área son coherentes entre sí: «NIVEL n DE 7», franja de color, bloque 3D con motivo y páginas, instrumento, seis momentos, ocho clases y puntaje. La portada general (p. 1) es la variante con escalera, 500 y apuntes.

**Elementos fijos de las hojas**
- El salvavidas es igual en todas las áreas: fondo claro, borde y flotador coral.
- No hay fondos oscuros donde el estudiante escribe.
- El reparto de la p. 4 es correcto: 15 / 20 / 35 / 20 / 20 / 10.
- Los chips de estrategia se ven bien al ampliarlos. A 50 ppp parecía que se salían, pero era efecto de la baja resolución.

**Reglas de texto**
- «EDUCATE» va en mayúsculas en todo el texto: no se encontró ninguna variante en minúscula.
- No aparece «Generación E», ni «Pregunta oficial», ni «preguntas reales del ICFES».
- No hay texto en LGRAY #D8DEE6 en ninguna página.

**No se vio en las hojas de contacto**
- Ninguna línea horizontal decorativa bajo títulos ni en las cabeceras.
- Ningún desborde de texto ni instrumento visible a 50 ppp en las páginas 1–18 y 145–398. Las 19–144 se miraron una vez sin dejar notas (ver el aviso de alcance arriba).

**Imprenta**
- 398 páginas con TrimBox (carta exacta), BleedBox (+3 mm) y MediaBox (+12 mm con marcas de corte en registro).
- Tiene OutputIntent y está marcado como PDF/X-4. Falta correr un validador.
- Todas las fuentes están incrustadas en subconjunto (4045 de 4045).
- Todas las imágenes están entre 326 y 1439 ppi; ninguna está por debajo de 300 ppi.
- El lomo queda bien:
  - impares: tinta a 2,12 cm del corte por la izquierda
  - pares: tinta a 2,12 cm del corte por la derecha
  - exterior: 0,74 cm de la tinta al corte
- El color a sangre de p. 1 y de las 7 franjas de portada llega hasta el borde del sangrado, sin filo blanco. Se comprobó en p. 1, 7, 60 y 313: 0 píxeles blancos en la fila del sangrado superior y en las columnas de los sangrados laterales.
- La franja termina a la misma altura en el sangrado y dentro de la página (≈ 280 pt bajo el corte).

## Conteo
- Alta: 2
- Media: 1
- Atención: 7
