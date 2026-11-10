# CLAUDE.md · Cuaderno Saber 11 · EDUCATE · Para el Saber

Este archivo lo lee Claude Code al abrir la carpeta. Es el contrato del proyecto: qué se
está construyendo, las reglas que no se negocian, cómo está armado el código y qué falta.
Léelo entero antes de tocar nada, y después lee `RECUPERACION.md`.

---

## 1. El proyecto

EDUCATE · Para el Saber es un instituto que prepara estudiantes para el Saber 11 los
sábados. El problema que resuelve el proyecto: **la calidad de la clase no puede depender
de qué profesor llegue ese sábado.** Por eso el método no vive en el profesor: vive en el
cuaderno del estudiante.

- **Nelson González** — asesor comercial y pedagógico. Es con quien trabajas.
- **Cristian Bueno** — Gerente General. Aprueba.
- Proyecto aprobado, 8 semanas.

El hilo que amarra todo el material:

```
LIBRO      → tiene la pregunta
CUADERNO   → tiene el andamiaje para resolverla
PLANEADOR  → le dice al profe qué hacer con los dos
GUÍA       → pone ese plan en pantalla
```

Regla que gobierna el diseño de cada hoja: **primero se escribe el andamiaje, después se
marca la respuesta.** Una hoja con la respuesta correcta y el andamiaje vacío no cuenta como
resuelta. Esto convierte el cuaderno en instrumento de auditoría: la coordinación revisa
tres cuadernos al azar sin haber entrado a la clase.

### Entregables comprometidos

| Entregable | Listo | Total |
|---|---|---|
| Cuaderno combinado de las siete áreas | 398 | **398 páginas** |
| Planeadores del docente (uno por área) | 7 | 7 |
| Guías de clase proyectables (una por clase) | 56 | 56 |
| Documento maestro de metodología | 0 | 1 |
| Reporte de los especialistas | 0 | 1 |
| Informe de hallazgos del libro | 1 | 1 |

**Son PÁGINAS, no hojas.** Nunca escribir «hojas» para el total.

**Cambio del 6 nov (decisión de Nelson):** el cuaderno sigue al libro tal cual. Como el libro trae
**Biología y Química por separado** (6 misiones cada una), Ciencias Naturales se parte en dos áreas:
son **7 áreas** y el cuaderno pasa de 270 a **313 páginas** (planeadores 7, clases 56). El proyecto
aprobado era de 270: **falta que Cristian apruebe la ampliación** (impresión y tiempo).

### Las tres unidades, que no se confunden

- **Momento** (o misión) = unidad de contenido. Cada área tiene **6**. Cada uno ocupa
  **7 páginas**: 5 de taller con las 10 preguntas del libro y 2 de entrenamiento con 4
  preguntas reales del ICFES. Orden impreso: taller, taller, ICFES, taller, taller, taller, ICFES.
- **Clase** = sesión de 2 horas. Cada área tiene **8**, número fijo: 6 de contenido + clase 7
  (simulacro del área) + clase 8 (devolución). Total 56 clases (7 áreas).
- **Las seis fases** de una clase de 120 minutos, con el reparto **aprobado en el piloto**:
  Activación **15** · Pregunta problematizadora **20** · Desarrollo guiado **35** ·
  Reto en equipo **20** · Evaluación individual **20** · Cierre **10**.
  No cambiar este reparto: ya se cambió una vez por error y hubo que rehacerlo.

### Mapa de páginas (exactamente 398, desde el 10 nov · estilo B «Bitácora»)

| Páginas | Sección |
|---|---|
| 1–6 | Apertura (`apertura_b.py`: `ap_b_1`…`ap_b_6`) |
| 7–59 | Matemáticas (portada + 6 misiones + simulacro de 10) |
| 60–112 | Lectura Crítica (43 + 10) |
| 113–165 | Sociales y Ciudadanas (43 + 10) |
| 166–214 | Biología (43 + 6) |
| 215–263 | Química (43 + 6) |
| 264–312 | Física (43 + 6) |
| 313–395 | Inglés (77 + 6) |
| 396–397 | Cierre post-prueba (`cierre_b.py`) |
| 398 | Mensaje final («Lo que me diría hoy, al terminar») |

**La numeración la manda `libro/paginas.py`** (escribe `tablero/mapa_paginas.json`, página vieja → nueva). Los
módulos de misión guardan su numeración vieja en `build(pages=…)`: **solo se construyen con `construye.py`**,
que traduce; `taller_base` falla si el pie no coincide con el manifiesto. `rehace_hojas.py` + `arma_pdf.py`
(`armar()` y `partir()`) dan `entregables/Cuaderno_Saber11_completo_398_paginas.pdf` y `Cuaderno_0N_<área>_pA-B.pdf`;
los PDF anteriores están en `entregables/anteriores/`. El simulacro se genera con `simulacro.py --cuaderno`.
El diseño original (antes del estilo B) está en la rama `diseno-original-10nov`.

Cada área son **43 páginas**: una portada y seis misiones de siete. **Excepto Inglés** (decisión de Nelson, 7 nov):
trabaja **todas** las preguntas del libro (127: M1 21, M2 10, M3 40, M4 16, M5 16, M6 24), una tarjeta por pregunta con
su instrumento propio; cada misión es una parte del examen (M1 Partes 1–2 … M6 Parte 7), la estrategia de la parte va en
`tema=` y las tarjetas dicen «Subestrategia n» (`configurar(..., prefijo="Subestrategia", n_hojas=K)`). Nelson rechazó
el formato de tablas («se ven como tablas»). Nelson acepta hasta 400 páginas en total; **la ampliación a 398 la aprueba Cristian.**

Colores de área: Matemáticas `#1F4E8C` · Lectura Crítica `#A82424` · Sociales `#C9821B` ·
Biología `#30843C` (verde hoja) · Química `#0F7A68` (verde esmeralda) · Física `#5C7A1E` (verde oliva) ·
Inglés `#1BA0A8`. Cada área tiene su color: es su personalidad (Nelson). Las tres ciencias van en verdes.

**El salvavidas es igual en todas las áreas** (Nelson, 6 nov): fondo claro `#FFF7F2`, borde y flotador coral
`#E4572E`, renglones grises. El estudiante lo llena con lápiz: nunca un fondo oscuro donde se escribe.
Paleta institucional: azul `#242478`, rojo `#A82424`, verde `#30843C`, oro `#C9821B`.

---

## 2. Reglas que no se negocian

Son de Nelson, textuales. Romper una es retroceder.

1. **Nada de líneas horizontales decorativas**: ni bajo los títulos, ni en el encabezado de
   página, ni en la portada. Se nota mucho que es generado por IA. Los acentos verticales en
   recuadros sí se permiten. *(Esto vale también para el HTML: nada de `border-bottom` de
   adorno en barras de encabezado.)*
2. **Texto justificado** en todos los párrafos corridos, medido con la fuente real usando
   `parrafo_j()` de `lib.py`. **Nunca justificar contando caracteres.**
3. **«EDUCATE» siempre en mayúsculas sostenidas** en el texto.
4. **Cada pregunta lleva su propio instrumento de pensamiento.** No repetir la misma plantilla
   de flechas y cuadritos. Si dos preguntas se ven iguales, está mal hecho.
5. El cuaderno debe sentirse como **un diario personal**, no como un taller genérico: fecha,
   caritas «llego / salgo», «mi primera idea antes de hacer nada», «lo que me llevo de esta
   pregunta».
6. **Tono juvenil y algo filosófico** en la apertura. Hablar de frente, sin sermonear.
   **No mencionar Generación E**: ese programa ya no existe.
7. **NUNCA inventar el año ni el cuadernillo de una pregunta del ICFES.** El membrete lleva
   año solo si está verificado contra el cuadernillo liberado. Si no se puede verificar, va
   **«Pregunta oficial ICFES · Saber 11»** sin año. Decidido; no se vuelve a discutir.
   **Desde el 6 nov el membrete es SIEMPRE genérico** («Pregunta oficial ICFES · Saber 11»), aunque el
   año esté verificado: Nelson no tiene certeza del año ni de la aplicación de cada pregunta del
   banco. El cuadernillo y el número verificados se guardan en `tablero/icfes.csv`, columna `fuente`.
   `taller_base.membrete()` ya no imprime otra cosa.
   **Desde el 10 nov (Nelson): el membrete es solo «Pregunta Saber 11»**, sin año, sin «oficial» y sin «ICFES»,
   en todo el material (cuaderno, planeadores y guías). La tarjeta dice «Pregunta para entrenar» (no «real»), y
   en ningún lugar que vea el estudiante se dice «preguntas reales del ICFES»: varias vienen del ASED, que no es del
   ICFES. La procedencia verificada sigue en `tablero/icfes.csv`, columna `fuente`; en la guía del profe, una pregunta
   del ASED dice «Fuente: compilado ASED (no es del ICFES)».

Y estas, que salieron del trabajo y también son reglas:

- **Todo hallazgo se registra**, aunque no sea un error. Lo que no requiere corrección va como
  «Atención». Va en `tablero/hallazgos.csv`.
- **Toda clave ICFES se verifica resolviendo la pregunta**, nunca copiándola de un
  solucionario. Y cuando un documento muestra la clave al lado de la pregunta, se verifica
  que esté al lado de **esa** pregunta (ver `verifica_claves.py`).
- **Ningún instrumento puede delatar la respuesta**: ni con un borde más grueso en la opción
  correcta, ni con mayúsculas en las incorrectas, ni con la opción más larga.
- **El ASED reinicia la numeración en cada sección**: «ítem 34» es una pregunta en Lectura
  Crítica y otra en Sociales. Anotar siempre la sección.
- **Nombres de políticos colombianos vivos**: pendiente de decisión de la Gerencia antes de
  imprimir. Mientras tanto no se agregan preguntas nuevas con nombres propios de la política.

### Cómo trabajar con Nelson

Responde en **español, directo y cálido**. Si algo que te pide tiene un riesgo real para él
o para EDUCATE, **díselo de frente aunque insista**. No le resumas cada paso; cuando
termines, dile qué quedó y qué tiene que decidir él.

---

## 3. Cómo se entrega

**Imprenta (Nelson, 9 nov):** carta, **pegado como un libro**, doble cara, sangrado estándar de 3 mm con marcas
de corte, CMYK y PDF/X al final. Los PDF actuales son vectoriales con fuentes incrustadas, pero tienen margen de
0,76 cm (M = 70 de 2000), sin sangrado y en RGB. La versión de imprenta se arma aparte, al final: margen del lomo
de unos 2 cm (izquierda en impares, derecha en pares), fondos que llegan al borde extendidos 3 mm. El logo de la
página 1 está a 175 ppi: hace falta el logo en vector (Nelson lo busca).

- Las hojas se generan en **SVG de 2000 × 2588** y se convierten a **PDF carta** con
  `render.py` (`rsvg-convert`).
- **Revisa visualmente cada hoja renderizada antes de entregarla.** Los desbordes de texto no
  se ven en el código. Rasteriza a PNG (`rsvg-convert -w 1000`) y míralo.
- Corre los verificadores antes de cualquier entrega (sección 6).

---

## 4. Instalación (Windows → WSL con Ubuntu)

El código usa rutas de Linux (`/home/claude/libro/`, `/tmp/claude-0/`). En Windows se trabaja
dentro de **WSL 2 con Ubuntu**, y `instalar.sh` deja todo listo en un solo paso: los programas,
la fuente Carlito, el enlace `/home/claude` → esta carpeta, Claude Code y la primera copia en git.

```powershell
# 1. En PowerShell como administrador, una sola vez, y reiniciar el computador
wsl --install -d Ubuntu
```

```bash
# 2. En la ventana de Ubuntu, una sola vez
bash /mnt/c/Users/ACER/Documents/EDUCATE_Saber11/instalar.sh

# 3. Cada vez que vayas a trabajar
cd /home/claude && claude
```

Claude Code se instala con el instalador oficial (`curl -fsSL https://claude.ai/install.sh | bash`)
y **se corre dentro de Ubuntu, no en PowerShell**. Pide una cuenta Pro, Max, Team o Enterprise;
el plan gratuito no lo incluye. El primer `claude` abre el navegador para iniciar sesión.
Si algo falla: `claude doctor`.

Fuentes: el texto se mide con **Carlito** (métrica idéntica a Calibri) en
`/usr/share/fonts/truetype/crosextra/`; sin ella `parrafo_j()` falla. Las tipografías de mano
(Caveat, Patrick Hand) están en `fuentes/`. Para probar las guías HTML hace falta Playwright,
que se instala cuando se necesite: `npm install -g playwright && npx playwright install chromium`.

### Trabajo en la nube (Claude Code en claude.ai)

El repositorio es `github.com/nelsongonzalez1608-spec/educate-saber11` (privado) y es la fuente.
En un contenedor nuevo: `apt-get install -y librsvg2-bin` y los enlaces
`/home/claude/libro`, `/home/claude/tablero` → las carpetas del repo y `/home/claude/cuaderno` →
`piloto/cuaderno_mision1_oct`; `mkdir -p /tmp/claude-0`. Las letras de mano (Caveat, Patrick Hand) se
instalan con `mkdir -p ~/.local/share/fonts && cp fuentes/*.ttf ~/.local/share/fonts/ && fc-cache -f`;
sin ellas la apertura sale con una letra de respaldo. **Estilo B (desde el 10 nov):** también `cp fuentes/propuesta/*.ttf ~/.local/share/fonts/ && fc-cache -f` (Shantell Sans y Space Mono, OFL); sin ellas los títulos salen con letra de respaldo. Las piezas del estilo están en `libro/bitacora.py`. Para el PDF final: `pip install pikepdf`. **Commit y push al final de cada sesión.**
Las pruebas de campo del libro (42 PDF, 6 misiones × 7 áreas) están en `fuente_libro/`.

## 5. Arquitectura

```
CLAUDE.md                 este archivo
RECUPERACION.md           qué se perdió el 6 nov y qué hay que reconstruir — LEER
libro/                    código
  base.py                 primitivas SVG: T, rect, line, logo, checkbox, wlines, esc
  lib.py                  W=2000, H_PAGE=2588, M=70, CW=1860 · tw(), wrap_px(), TJ(),
                          parrafo_j(), chip(), frame(), footer(), titulo(), panel()
  render.py               unir(svgs, pdf) · verifica(pdf, marca) → (n páginas, recortadas)
  apertura*.py            páginas 1–10
  mate_m1*.py             Misión 1 de Matemáticas, versión del piloto (modelo de una misión)
  plan_piezas.py          motor de los planeadores: cabecera, pie, nota, bloque_momento,
                          bloque_dinamica, bloque_reto, registro_docente, barra_tiempo
  plan_mate.py            planeador de Matemáticas (24 hojas) — motor propio, anterior a
                          plan_piezas; migrarlo cuando se toque
  plan_lc.py              planeador de Lectura Crítica (24 hojas) — usa plan_piezas
  clase_viva_lc.py        las 8 guías de clase proyectables de Lectura Crítica (HTML)
  textos_lc.py            lee TEXTOS_GUIA_DOCENTE.md → texto y notas por pregunta ICFES
  TEXTOS_GUIA_DOCENTE.md  textos completos que el cuaderno no imprime y el profe proyecta
  revision_externa.py     los 120 hallazgos de los 6 docentes revisores + cruce por tipo
  visor_*.py              el visor HTML del cuaderno (área → misión → hoja)
  verifica_plan.py        desbordes del planeador
  verifica_claves.py      que cada clave ICFES esté al lado de SU pregunta
tablero/                  la fuente de verdad de los datos
  avance.csv misiones.csv hallazgos.csv icfes.csv pendientes.csv decisiones.csv
  entregables.csv instrumentos.csv (196 instrumentos, uno por pregunta)
  manifiesto_hojas.json   qué SVG es cada página
referencia/hojas/         las 110 páginas construidas, en JPG de 1100 px (no imprimibles)
piloto/paquete_mision1_aprobado/   el paquete aprobado: cuaderno, planeador, clase impresa,
                          guía del encuentro y clase viva de la Misión 1 de Matemáticas
piloto/propuesta/         la propuesta comercial aprobada (.docx)
fuentes/                  tipografías de mano
docs/                     HANDOVER del 28 oct (desactualizado) y la muestra
```

### El motor de una hoja de taller (`taller_base.py` — reconstruido el 6 nov)

Reconstruido contra `referencia/hojas/`. La prueba es `prueba_taller_base.py`, que rehace las
páginas 106 y 107 ya entregadas. Al empezar una misión nueva, copiar su forma de uso (docstring de
`taller_base.py`): `configurar()`, `usar_estrategias()`, `hoja_taller()`, `hoja_icfes()`.
Así funciona:

- Cada hoja de taller trae **dos preguntas**, una por tarjeta. La tarjeta tiene: número,
  «la lees en tu libro, página N», chip de estrategia, «mi primera idea, antes de hacer nada»,
  el **instrumento de pensamiento** de esa pregunta (ancho `IW = 1270`), «marco al final»
  A B C D, «¿qué tan seguro estoy? adiviné / casi / seguro», el **salvavidas** (lo mínimo que
  sí tenía claro) y «lo que me llevo de esta pregunta».
- Alto de bloque variable: `set_bloque(con_vocab)` → **1010** con franja de vocabulario,
  **1090** sin ella. La segunda tarjeta se ubica con **`y_bloque2()`**, nunca con
  `210 + BLK_H + 40` (los módulos hacen `from taller_base import *` y congelan el valor).
- `encajar()` envuelve un instrumento que se pasa de alto en
  `<g transform="translate(...) scale(k)">`, anclado arriba y centrado. **Solo arregla el
  alto**; el ancho hay que respetarlo a mano: borde derecho máximo **M + 30 + IW = 1370**.
- Cabecera de cada hoja: fecha «Sábado ___ de ___», caritas llego/salgo, área · misión,
  componente y «hoja n de 5 · preguntas a y b».
- Un módulo por misión: `m3.py` (taller) + `m3_icfes.py` (entrenamiento). Cada módulo define
  `EST = {1: (nombre, color), …}`, los instrumentos `i1…i10`, `build(pages=(…))`, y en el
  docstring **las claves verificadas**: `1·D  2·C  3·C …`.
- Los módulos ICFES definen `QA…QD = dict(est, comp, f=membrete, e=enunciado, o=[4 opciones],
  datos=función que dibuja el texto)`.

### Rehacer una página ya entregada (sin sus módulos)

`rehace_hojas.py` toma la página del PDF entregado, lee su texto con `pdftotext -bbox` y la vuelve a
armar con `taller_base.py`; cada instrumento se recorta del original en vectores. `arma_pdf.py`
compone el PDF final poniendo la página original (fuentes reales) bajo el recorte. Si se cambia el
motor (marco, salvavidas, colores), basta `python3 rehace_hojas.py && python3 arma_pdf.py`.
El PDF entregado se rindió a página completa: 1 pt = 2000/612 unidades; `render.conv()` usa m=0.

### Visor de avance (página privada en claude.ai)

https://claude.ai/artifact/2wZ42PVyMpwpxbTz8BZ8Bw — tablero del proyecto con cuatro pestañas: cuaderno
(mapa de 313 páginas), material del docente (planeadores hoja por hoja y guías HTML), hallazgos (tabla con
filtros y descarga .csv) y descargas (PDF por área; capacidad `downloads`). No sirve .xlsx.
Se regenera con `python3 libro/visor_avance.py <carpeta>` (lee el manifiesto y el tablero; las imágenes
salen de los PDF de `entregables/` o, si no hay PDF, del SVG) y se vuelve a publicar en la misma URL.
Actualizarlo cada vez que se cierra un área.

### Lecciones que costaron caro (no repetirlas)

- **`LGRAY = #D8DEE6` es el gris de las LÍNEAS, nunca de texto.** En papel no se lee. Texto
  gris va en `GRAY = #6E7480` o más oscuro.
- **El ancho de un chip o de un rótulo se mide con `tw()`**, no contando caracteres. Contando
  caracteres los chips salían hasta 170 px más anchos y se montaban en la columna vecina.
- Si dos filas hermanas tienen rótulos, se mide el más largo y todas llevan ese ancho.
- **Carlito no trae el glifo ⚠**: el respaldo lo dibuja encima de la palabra siguiente. En
  SVG la alerta se marca con el color de la tarjeta, no con el símbolo.
- **El rayado de tachar va DEBAJO del texto** (opacidad 0.30), y el texto encima en tinta.
- `flecha_d(b, x1, y1, x2, c, sw)` es horizontal y dibuja en `b`; no devuelve nada.
- `line()` no tiene parámetro de opacidad: si hace falta, se escribe el `<line>` a mano.
- **Python: `"abc".endswith("")` es `True`.** Un verificador que compara membretes vacíos
  pasa sin comparar nada. Le pasó a `verifica_claves.py`; ya está arreglado.
- **Cada módulo de misión se construye en su propio proceso**: `python3 construye.py soc3 soc3_icfes …`.
  `configurar()` y `usar_estrategias()` guardan la misión en memoria al importar el módulo; si se
  importan dos en el mismo proceso, el último pisa al primero. El 7 nov las páginas 113 y 117 salieron
  «Misión 4» siendo de la 3. `verifica_cajas.py` ahora compara la misión de la cabecera con el archivo.
- **No reordenar un archivo cortándolo por la posición de una función**: así se perdió una vez
  todo el banco de dinámicas. Mover bloques con el editor, no con `s[:i] + nuevo`.
- El alto de una tarjeta se calcula **desde dónde termina de verdad el contenido**, no a ojo.
- `render.verifica(pdf, marca=...)`: las hojas del cuaderno llevan en el pie
  «Aprende · Practica · Avanza» (no «EDUCATE»); los planeadores, «PLANEADOR».

---

## 6. Verificadores — obligatorios antes de entregar

| Qué revisa | Archivo | Estado |
|---|---|---|
| Alto y borde derecho de cada instrumento; texto en LGRAY; ancho de chips | `verifica_cajas.py` | disponible (reconstruido 6 nov) |
| Que ningún instrumento delate la respuesta (borde y tipografía) | `verifica_pistas.py` | disponible (reconstruido 6 nov) |
| Que no haya dos instrumentos con el mismo título | `extrae_instrumentos.py "Título nuevo" …` | disponible (lee `tablero/instrumentos.csv`; al cerrar una misión, agregar sus filas) |
| Pie presente en todas las páginas del PDF (detecta PDF recortados) | `render.verifica()` | disponible (reconstruido 6 nov: el zip no lo traía) |
| Desbordes del planeador | `verifica_plan.py` | disponible |
| Claves ICFES al lado de su pregunta | `verifica_claves.py` | disponible (necesita los módulos `m*_icfes.py`) |

Para las guías HTML: abrirlas con Playwright, recorrer todas las diapositivas y comprobar
cero errores de JavaScript, **ninguna clave visible antes de que el profe la revele** y nada
que se salga de ancho.

---

## 7. Las guías de clase proyectables («clase viva»)

Modelo aprobado: `piloto/paquete_mision1_aprobado/3_presentaciones/Clase_viva_estudiantes.html`.
Lo replica `clase_viva_lc.py`.

- Barra superior: momento actual (círculo de color) y **cronómetro que se reinicia solo al
  cambiar de momento**.
- Teclas: `← →` avanzar · espacio · Inicio/Fin · **G** guía del profe · **T** cronómetro ·
  Esc cierra la guía.
- **Guía del profe** en panel lateral: objetivo, qué hace y qué dice, lo que no hace, y
  **«Si [el área] no es tu fuerte»** con lo que necesita saber un profesor que no es del área.
- Las claves solo aparecen al presionar «Revelar».
- Una clase de contenido = 19 diapositivas: portada · reglas · activación · dinámica E1 ·
  pregunta modelo con conteo de manos · 5 bloques de 2 preguntas (con 3 dinámicas
  intercaladas) · reto del corte · 4 preguntas ICFES con su texto completo · cierre.
- Archivo único, funciona con doble clic y sin internet.

## 8. El planeador del docente

Modelo aprobado: `piloto/paquete_mision1_aprobado/2_docente/Mate_Mision1_PLANEADOR.pdf` (4 hojas).
Por área son 24 hojas: cómo se usa · las 8 clases · los 120 minutos (2 hojas) · 2 hojas por
clase de contenido · clases 7 y 8 · banco de dinámicas (una hoja por misión) · cierre.

- En cada momento: objetivo específico, «qué hace el docente» / «cómo lo hace» y
  **«TU APORTE»**: el ejemplo o la variación del profe, declarado y acotado, *sin reemplazar
  lo de arriba*.
- **Regla para aprobar cualquier dinámica: debe ser isomorfa a la estrategia.** Lo que hace
  el cuerpo tiene que ser el mismo movimiento que después hará la mente frente a la pregunta.
  Si no puedes decir qué paso de la estrategia ejercita, es recreo, no clase.
- Cada misión trae 4 dinámicas (una por estrategia) y un **reto del corte** de 20 minutos con
  registro individual.

---

## 9. Lo que falta (en orden)

1. ~~Reconstruir el motor del cuaderno~~ — hecho el 6 nov. ~~Hallazgos 35 y 36~~ — corregidos: las
   98 páginas de misión entregadas se rehicieron con `rehace_hojas.py` (marco nuevo, salvavidas claro,
   Matemáticas en azul) y `arma_pdf.py` arma `entregables/Cuaderno_Saber11_paginas_1_a_110_v2.pdf`.
   La apertura y las portadas de área ya están a 7 áreas y con el salvavidas nuevo.
   **Pendiente:** el visor HTML (`EDUCATE_Visor_del_cuaderno.html`) muestra las páginas viejas.
2. ~~Sociales misiones 3 a 6~~ — hechas el 6 nov (`soc3.py` … `soc6_icfes.py`); Sociales completo en
   `entregables/Sociales_completo_paginas_96_a_138.pdf`. Los textos largos de M6 están en
   `tablero/propuestas/soc6_textos.md` (falta pasarlos a `TEXTOS_GUIA_DOCENTE.md`).
3. ~~Biología~~ — hecha el 7 nov (`bio1.py` … `bio6_icfes.py`, portada `ap139_bio`):
   `entregables/Biologia_completo_paginas_139_a_181.pdf`. ~~Química~~ — hecha el 7 nov (`qui1.py` …
   `qui6_icfes.py`, portada `ap182_qui`): `entregables/Quimica_completo_paginas_182_a_224.pdf`. 11 de sus 24
   preguntas ICFES salen del SIMULACRO II 2023 (Oficio): Nelson confirmó que son reales del ICFES.
   ~~Física~~ — hecha el 7 nov (`fis1.py` … `fis6_icfes.py`, portada `ap225_fis`):
   `entregables/Fisica_completo_paginas_225_a_267.pdf`. Los cuadernillos oficiales 2025 y 2026 de Ciencias
   Naturales son las mismas 50 preguntas. ~~Inglés~~ — hecho el 7 nov y rehecho (v3) con las 127 preguntas del libro (`ing1.py` … `ing6_icfes.py`,
   `ing_diario.py` con `correccion()` y `cierre_mision()`, portada `ap268_ing`): `entregables/Ingles_completo_paginas_268_a_344.pdf`.
   Los errores del libro se corrigen en la tarjeta («Corrección EDUCATE») y en la matriz quedan «Corregido en el cuaderno ·
   informar a la editorial». Las ICFES salen del cuadernillo oficial 2024, del 2016-1 y del SIM II 2023 Inglés
   (`fuente_icfes/SIM_II_2023_OFICIO_INGLES.pdf`; repite ítems del 2024: SIM 230–237 y 446–454). Regla de Nelson: **una
   pregunta ICFES con cualquier falla no se usa**; las 4 de M5 (Parte 6) tienen erratas y esperan su decisión.
   ~~El cierre~~ — hecho el 10 nov (396–398).
   **ASED:** su presentación dice que sus ~700 preguntas fueron «concebidas específicamente» por la Corporación ASED: no son
   del ICFES. 15 preguntas del cuaderno salen de él con el membrete oficial (4 Mate, 1 LC, 8 Sociales M1–M2, 2 Física): pendiente que Nelson
   decida reemplazarlas. No usar el ASED como fuente de preguntas ICFES.
4. ~~Las 8 guías de clase de Matemáticas~~ — hechas el 10 nov (`clase_viva_mate.py`, figuras en `figuras_mate.py`).
5. ~~Planeador y guías de Sociales~~ — hechos el 9 nov (`plan_soc.py`, `clase_viva_soc.py` con el motor general `clase_viva.py`). ~~Biología~~ hecha el 10 nov (`plan_bio.py`, `clase_viva_bio.py`, `TEXTOS_BIO.md`). Faltan Química, Física e Inglés. Las guías se prueban con `node libro/verifica_guias.js <carpeta> <capturas>` (mira lo que se pinta: el 9 nov encontró que las de LC mostraban las claves del taller).
6. **Decisión de Cristian** sobre los nombres de políticos vivos, antes de imprimir.
7. Subir a la matriz los sellos y textos de Matemáticas (hoy figuran en cero) y las 48
   dinámicas nuevas.
8. Que un especialista de Lenguaje revise las 18 explicaciones de los sellos en las guías de
   Lectura Crítica (las escribió Claude).
9. Revisar con la editorial el reparto de claves de Lectura Crítica (M6: seis A, ninguna B).
10. **Contar a la Gerencia los indicios de contenido generado por IA en el libro fuente**: un
    revisor externo escribió «(patrón IA)» sobre la extensión de las respuestas correctas, y
    tres URL del libro traen `?utm_source=chatgpt.com`.

## 10. Fuentes de preguntas ICFES

En el proyecto de claude.ai (no en esta carpeta, pesan mucho): los cuadernillos 2024 en cuatro
partes, el compilado **ASED pre código 11**, los simulacros **SIM. II 2023** de Inglés,
Lectura Crítica y Química, y los compilados `ff1`, `ff2`, `ff3` y `fenix 3`. Libro fuente:
`1. Grado.11.°.pdf` y `1. Grado.10.°.pdf`. Antes de elegir preguntas nuevas, revisar
`tablero/icfes.csv` para no repetir.

**Cuadernillos liberados oficiales** (bajados del sitio del ICFES el 7 nov, en `fuente_icfes/`): Ciencias
Naturales 2025 y 2026, Inglés 2024, Matemáticas 2026 y Lectura Crítica 2026 (dos). Vienen de la página
«Caja de herramientas Saber 11 · práctica». El entorno `educate-saber11` permite www.icfes.gov.co.
En Drive (carpeta con id 1kyvVqE2up3vOXl5LG3x-Z9BnVrjqx1LN): SIM. II 2023 de química, biología y física,
y el ASED (14 MB: se lee con `read_file_content`, la descarga se corta en 10 MB).
