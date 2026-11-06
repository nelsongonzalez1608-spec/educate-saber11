# Cuaderno de trabajo Saber 11 · EDUCATE — estado y reglas del proyecto

Documento de traspaso. Si estás empezando una sesión nueva, lee esto primero: tiene las
decisiones ya tomadas, lo que está construido y lo que falta. Todo el código fuente está
en el ZIP `EDUCATE_cuaderno_fuente.zip`, que debe subirse a los archivos del proyecto.

---

## 1. Qué es esto

EDUCATE · Para el Saber es un instituto que dicta preparación para el Saber 11 los sábados.
El problema que resuelve este proyecto: **la calidad de la clase no puede depender de qué
profesor llegue ese sábado.** Por eso el método no vive en el profesor: vive en el cuaderno
del estudiante.

El hilo que amarra todo el material:

```
LIBRO     → tiene la pregunta
CUADERNO  → tiene el andamiaje para resolverla
PLANEADOR → le dice al profe qué hacer con los dos
GUÍA      → pone ese plan en pantalla
```

Regla que gobierna el diseño de cada hoja: **primero se escribe el andamiaje, después se
marca la respuesta.** Una hoja con la respuesta correcta y el andamiaje vacío no cuenta como
resuelta. Esto convierte el cuaderno en el instrumento de auditoría: la coordinación revisa
tres cuadernos al azar sin haber entrado a la clase.

**Responsable:** Nelson González, asesor comercial y pedagógico.
**Aprueba:** Cristian Bueno, Gerente General.

---

## 2. Estado comercial

La propuesta ya fue **aprobada**. Términos cerrados:

| | |
|---|---|
| Valor | $ 4.500.000 COP (incluye la suscripción de IA de los dos meses, ≈ $660.000) |
| Anticipo | 30 % ($ 1.350.000) · luego 35 % y 35 % |
| Plazo | 8 semanas |
| Alcance | Cuaderno completo de las 6 áreas, ~270 hojas |
| Revisión | Especialista externo por área, salvo **Matemáticas y Física, que revisa Nelson** |

Archivo: `propuesta/Propuesta_EduCaTe_Cuadernos_por_Area.docx`

---

## 3. Arquitectura del cuaderno

**Un solo cuaderno físico**, tamaño carta, con las seis áreas adentro (como un cuaderno de
varias materias). No son seis cuadernos.

### Estructura de hojas

| Sección | Hojas | Se recorre |
|---|---|---|
| Portada general | 1 | una vez |
| Introducción | 2 | una vez |
| Metas | 2 | una vez |
| Qué te vas a encontrar | 2 | una vez |
| La psicología de la meta | 2 | una vez |
| Portada de cada área | 1 × 6 | por área |
| Hojas de trabajo | 7 × 6 momentos × 6 áreas = 252 | por área |
| Cierre post-prueba | 3 | una vez |
| **Total** | **≈ 270** | |

### Las tres unidades (no confundirlas)

- **Momento** = unidad de contenido. Cada área tiene **6 momentos**. Cada momento trae un
  taller de 10 preguntas del libro + entrenamiento ICFES + simulacro. Ocupa ≈ 7 hojas.
- **Clase** = sesión de 2 horas. Cada área tiene **8 clases**, número fijo, independiente de
  los momentos (incluye socialización de simulacro). Total: **48 clases**.
- **Los 6 momentos de clase** (Activación, Pregunta problematizadora, Desarrollo guiado,
  Reto en equipo, Evaluación individual, Cierre) son las fases *dentro* de una clase de
  120 minutos. No confundir con los 6 momentos de contenido.

### Entregables comprometidos

- 1 cuaderno combinado de las 6 áreas
- 6 planeadores del docente (uno por área, con la planeación de sus 8 clases)
- 48 guías de clase proyectables (una por clase)
- 1 documento maestro de metodología
- Reporte de observaciones de los especialistas

---

## 4. Reglas de diseño (no negociables)

Estas salieron de correcciones explícitas del cliente. Romperlas es retroceder.

1. **Nada de líneas horizontales decorativas.** Ni bajo los títulos, ni en el encabezado de
   página, ni en la portada. "Se nota muy de IA." Los acentos verticales en los recuadros sí
   se permiten.
2. **Texto justificado** en todos los párrafos corridos. Se mide con la fuente real (Carlito,
   métricamente igual a Calibri) usando `parrafo_j()` / `TJ()` en `lib.py`. No usar `wrap()`
   por número de caracteres para texto justificado.
3. **"EDUCATE" en mayúsculas sostenidas** en todo el texto. El logotipo es aparte.
4. **Cada pregunta tiene su propio instrumento de pensamiento.** No se repite la misma
   plantilla de flechitas y cuadritos. Si dos preguntas se ven iguales, está mal hecho.
   El cuaderno debe sentirse como un diario personal, no como un taller genérico.
5. **Formato diario:** cada hoja lleva fecha y caritas "llego / salgo"; cada pregunta lleva
   "mi primera idea, antes de hacer nada", "¿qué tan seguro estoy?" y "lo que me llevo".
6. **No referir demasiado al piloto de Matemáticas.** Ya fue aprobado; mencionarlo una vez
   como antecedente basta.
7. **Tono:** juvenil y algo filosófico en la apertura, sin ser infantil. Se habla de frente,
   no se sermonea.
8. **No mencionar Generación E** (el programa ya no existe). La marca de 350 puntos se rotula
   como "Becas y oportunidades".

---

## 5. Criterio de rotulación de preguntas ICFES  ⚠️ IMPORTANTE

El cuaderno le promete al estudiante, en la hoja 7, que *"cuando veas un membrete así, la
pregunta es real: salió en esa prueba, ese cuadernillo, con ese número. Puedes buscarla y
comprobarlo."* Esa promesa es el argumento de venta más fuerte del material y es verificable:
el ICFES publica los cuadernillos liberados.

**Por lo tanto:**

- ✅ **Con año**, solo si está confirmada una por una contra el cuadernillo liberado:
  `Saber 11 · 2019 · Cuadernillo 2 · N.º 46`
- ✅ **Sin año**, cuando sabemos que es real pero se perdió el origen:
  `Pregunta oficial ICFES · Saber 11`
- ✅ **Sello EDUCATE** (pastilla punteada en oro con diana), para preguntas construidas o
  adaptadas por el equipo: `Entrenamiento EDUCATE · tipo Saber 11`
- ❌ **Nunca** asignar un año o cuadernillo al azar. Se descartó explícitamente. Un año
  inventado lo desmiente cualquiera en un minuto, y el que responde es quien firma el material.

Hoja con el criterio dibujado: `EDUCATE_criterio_rotulacion.pdf` · código en `sellos.py`.

### Corrección factual ya aplicada
La pregunta del ICFES sobre los documentales P y Q (Saber 11 · 2019 · Cuadernillo 2 · N.º 18)
tenía la clave equivocada en la primera versión. En la gráfica **P va siempre 20 puntos por
encima de Q**, así que la conclusión del empleado es falsa y la respuesta correcta es la **D**,
no la C. Ya está corregido en todos los archivos.

---

## 6. Sistema visual

**Paleta institucional:** azul `#242478` · rojo `#A82424` · verde `#30843C` · oro `#C9821B`

**Colores por área:**

| Área | Color |
|---|---|
| Matemáticas | `#1F4E8C` |
| Lectura Crítica | `#A82424` |
| Sociales y Ciudadanas | `#C9821B` |
| Ciencias Naturales | `#30843C` |
| Física | `#5B3E96` |
| Inglés | `#1BA0A8` |

**Tipografías:** Carlito (= Calibri) para texto · Caveat para la letra a mano (lápiz del
estudiante, notas al margen).

**Formato de página:** SVG de ancho `W = 2000`, alto `H_PAGE = 2588` (proporción carta),
margen `M = 70`. Se convierte a PDF carta con `render.py` (rsvg-convert → pdftoppm para
revisar).

---

## 7. Qué está construido

### Entregado y aprobado
- **Piloto Misión 1 de Matemáticas** (versión anterior, en `cuaderno/`): cuaderno, planeador,
  guía docente, clase impresa, dos presentaciones HTML interactivas.
- **Propuesta comercial** (`propuesta/`): 8 páginas, .docx editable.

### Cuaderno nuevo — 19 hojas listas (`libro/`)
| Hojas | Contenido | Código |
|---|---|---|
| 1–3 | Portada, introducción (carta), las cuatro reglas | `apertura.py` |
| 4–7 | Metas (escala + tablero WOOP), qué te vas a encontrar | `apertura2.py` |
| 8–10 | Psicología del estudiante, hoja para coordinación, portada Matemáticas | `apertura3.py` |
| 11,13,15,16,18 | Taller Momento 1: las 10 preguntas, cada una con su instrumento | `mate_m1.py` |
| 12,14,17,19 | Entrenamiento ICFES por estrategia, 2 preguntas reales c/u | `mate_m1_icfes.py` |

PDF armado: `Cuaderno_Saber11_v3_1_justificado.pdf`

### Muestra hojeable para presentar
- `Cuaderno_EDUCATE_muestra.html` — archivo único autocontenido (4,4 MB). Se manda por
  WhatsApp o correo, abre en cualquier navegador sin internet. Pasa la hoja en 3D, tiene
  navegación por secciones y botón Ampliar para leer.
- Fuente: `flip/page.html` + `flip/build.py` (genera también la versión publicada en línea).
- Para regenerarlo tras cambiar el cuaderno: `pdftoppm` del PDF a `flip/pages/`, luego
  `python3 flip/build.py`.

---

## 8. Qué falta

| Prioridad | Tarea |
|---|---|
| 1 | **Momentos 2 a 6 de Matemáticas.** Falta recibir los PDF del libro. |
| 2 | **Hoja de simulacro del Momento 1** en el estilo nuevo (la del piloto es genérica). |
| 3 | **Banco de preguntas de Nelson.** Son reales pero se perdió el año. Hay que cruzarlas contra los cuadernillos liberados y rotular según §5. El ZIP original pesa 57 GB: hay que depurar antes (empezar solo por Matemáticas; mandar muestra de 10-20 primero para ver el formato). |
| 4 | Las otras cinco áreas, con su instrumento de pensamiento propio. |
| 5 | 6 planeadores y 48 guías de clase. |
| 6 | Cierre post-prueba (3 hojas, al final del cuaderno). |
| 7 | La pregunta del plan de vuelo (2019·C2·N.º 61) aparece dos veces, en estrategias 1 y 4. Reemplazar cuando haya más cuadernillos. |
| 8 | Puntajes de referencia de la hoja 4 son de prensa (El Universal, jun 2026), no cortes oficiales. Cambiar si EDUCATE tiene su propia tabla. |

**Acceso bloqueado:** `icfes.gov.co` está fuera del allowlist de la sesión. Para que Claude
descargue los cuadernillos oficiales directamente, habilitarlo en claude.ai →
Configuración → Capacidades → dominios permitidos. Si no, hay que subir los PDF a mano.

---

## 9. Cómo trabajar el código

```bash
cd libro
python3 apertura.py apertura2.py apertura3.py   # (cada uno por separado)
python3 mate_m1.py
python3 mate_m1_icfes.py
python3 render.py                                # SVG → PDF carta + JPG de revisión
```

- `lib.py` — piezas comunes: `frame()`, `titulo()`, `footer()`, `panel()`, `parrafo_j()`,
  `hand_arrow()`, `face()`, `num_badge()`, `write_box()`, `chip()`.
- `base.py` — primitivas SVG heredadas del piloto: `T()`, `rect()`, `line()`, `logo()`,
  `grid_box()`, `PT()` (lápiz), `spath()`, `ring()`, `salvavidas()`.
- **Siempre revisar visualmente** cada hoja renderizada antes de entregar. Los desbordes de
  texto no se ven en el código.

**Dependencias del entorno:** `rsvg-convert`, `pdftoppm`, `pdfunite`, Pillow, fuentes Carlito
y Caveat (en `/root/.fonts/`). El logo está en `cuaderno/logo_educate.png` y codificado en
`flip/logo.b64`.
