# RECUPERACION.md · qué pasó el 6 de noviembre de 2026 y qué hay que reconstruir

## Qué pasó

Todo el proyecto se construyó en el espacio de trabajo en la nube de la sesión de Cowork. Ese
espacio se reinició y se borró. El único respaldo del código en el proyecto de claude.ai era
`EDUCATE_cuaderno_fuente.zip`, del **28 de octubre**, que solo trae la apertura y la Misión 1
de Matemáticas del piloto. No había copia en el computador de Nelson.

**Los entregables no se perdieron.** Todos los PDF, el .xlsx y los HTML que se entregaron
están adjuntos en la conversación de Cowork. **Descárgalos y guárdalos en esta carpeta**, en
`entregables/`: hoy esa conversación es el único lugar donde están.

## Lo que se recuperó y de dónde

| Qué | De dónde | Dónde quedó |
|---|---|---|
| Motor base: `base.py`, `lib.py`, `render.py`, `apertura*.py`, `mate_m1*.py`, `sellos.py` | zip del 28 oct | `libro/` |
| Planeadores, guías, revisión externa, visor y dos verificadores (11 archivos) | registro de la sesión del 3 al 6 nov, **reconstruidos re-ejecutando sus 56 cambios en orden, sin un fallo** | `libro/` |
| `TEXTOS_GUIA_DOCENTE.md` | documento del proyecto (idéntico byte por byte a la última versión) | `libro/` |
| Datos del tablero: avance, misiones, hallazgos (34), ICFES (65), pendientes, decisiones | archivos del tablero publicado en claude.ai | `tablero/` |
| Registro de los **196 instrumentos** (área, misión, pregunta, estrategia, título, contexto) | datos incrustados en el visor publicado | `tablero/instrumentos.csv` |
| Las **110 páginas construidas** como imagen (1100 px) | visor publicado | `referencia/hojas/` |
| Paquete aprobado de la Misión 1 del piloto y la propuesta | zip del 28 oct | `piloto/` |

`entregables.csv` se rehízo a mano con los conteos del último cierre.

## Lo que se perdió y hay que reconstruir

### 1. El motor de las hojas de taller — **prioridad 1**

- `taller_base.py` — la tarjeta de pregunta, `bloque()`, `set_bloque()`, `y_bloque2()`,
  `encajar()`, la cabecera de diario, el salvavidas. Está descrito con detalle en
  `CLAUDE.md` § 5. El modelo visual exacto está en `referencia/hojas/m1_t1.jpg` y
  siguientes, y el código más cercano que sobrevive es `libro/mate_m1.py`.
- `lib.py` del zip es **anterior** a dos correcciones que hay que volver a hacer:
  `chip()` debe medir su ancho con `tw()` (hoy cuenta caracteres), y hay que agregar `tw()`
  donde falte. Compara con `plan_piezas.py`, que ya usa `tw()`.

### 2. Los verificadores

- `verifica_cajas.py` — alto que se sale de la tarjeta, **borde derecho > 1370**, texto con
  `fill="#D8DEE6"` (LGRAY), chips más anchos que su texto.
- `verifica_pistas.py` — ningún instrumento resalta la opción correcta: ni por borde (grosor o
  color distinto en una sola opción) ni por tipografía (en un grupo de 3 a 6 líneas con el
  mismo tamaño, color y x, si todas menos una van en MAYÚSCULAS SOSTENIDAS, o al revés).
- `extrae_instrumentos.py` — lee los módulos y saca la lista de instrumentos para comprobar
  que no hay títulos repetidos. Mientras no exista, la referencia es
  `tablero/instrumentos.csv`.

### 3. Los módulos de las 14 misiones construidas

`m1`–`m6`, `lc1`–`lc6`, `soc1`, `soc2`, cada uno con su `_icfes`, más `build_mate.py`,
`build_libro.py`, `portada_lc.py`, `portada_soc.py`, `informe_errores.py`, `hoja_reunion.py`
y `matriz.py`.

**No hace falta reconstruirlos para avanzar.** Las páginas 1 a 110 ya están terminadas y
entregadas en PDF. Solo hay que rehacer una misión si Nelson pide corregir una hoja ya
construida; en ese caso se rehace esa hoja mirando su imagen en `referencia/hojas/` y su fila
en `tablero/instrumentos.csv`.

### 4. Dependencias rotas en lo que sí se recuperó

Estos archivos están completos pero importan módulos que se perdieron, así que **no corren
hasta que se reconstruyan sus fuentes**:

| Archivo | Necesita |
|---|---|
| `plan_lc.py`, `clase_viva_lc.py` | `extrae_instrumentos.py`, `lc1`–`lc6.py` (claves en el docstring), `lc1`–`lc6_icfes.py` (preguntas), `matriz.py` (SELLOS y TEXTOS) |
| `plan_mate.py` | `extrae_instrumentos.py` |
| `verifica_claves.py` | `m1`–`m6_icfes.py` |
| `visor_datos.py`, `visor_html.py` | los SVG de las hojas, `extrae_instrumentos.py` |

La salida más corta: escribir un `extrae_instrumentos.py` que lea `tablero/instrumentos.csv`
en vez de los módulos, con la misma función `filas()`. Con eso `plan_mate.py` vuelve a correr.
Para `plan_lc.py` y `clase_viva_lc.py` hacen falta además las claves del libro y las preguntas
ICFES de Lectura Crítica: lo más rápido es pasarlas a un `tablero/lc_datos.json` a partir de las
guías HTML ya entregadas, que las traen incrustadas.

## Para que no vuelva a pasar

- Esta carpeta es ahora la fuente. **Haz `git init` y un commit al final de cada sesión.**
- Al cerrar cada misión, sube un zip del código al proyecto de claude.ai, reemplazando
  `EDUCATE_cuaderno_fuente.zip`.

## Estado al 6 nov, tarde (sesión de Claude Code en la nube)

- Todo el proyecto está en GitHub: `nelsongonzalez1608-spec/educate-saber11`.
- **Reconstruido:** `taller_base.py` (prueba: `prueba_taller_base.py` rehace las páginas 106 y 107),
  `verifica_cajas.py`, `verifica_pistas.py`, `extrae_instrumentos.py` (lee el CSV) y
  `render.unir()` / `render.verifica()`, que tampoco venían en el zip. `lib.chip()` y
  `lib.panel()` miden con `tw()`. `plan_mate.py` vuelve a correr (24/24, todo en su caja).
- **Sigue roto:** `plan_lc.py` y `clase_viva_lc.py` (necesitan `matriz.py` y los datos de LC:
  la salida es `tablero/lc_datos.json` sacado de las guías HTML entregadas, que no están aquí),
  `verifica_claves.py` (necesita `m*_icfes.py`) y el visor.
- **`entregables/` sigue vacío.** Los PDF, el .xlsx y los HTML solo existen en la conversación de Cowork.
