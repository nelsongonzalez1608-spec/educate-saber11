const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, HeadingLevel, Table, TableRow, TableCell,
  WidthType, BorderStyle, AlignmentType, ShadingType, ImageRun, PageBreak,
  LevelFormat, VerticalAlign, convertInchesToTwip, Header, Footer, PageNumber,
  TabStopType, TabStopPosition,
} = require("docx");

// ───────── paleta EduCaTe ─────────
const AZUL  = "242478";
const ROJO  = "A82424";
const VERDE = "30843C";
const ORO   = "C9821B";
const INK   = "20242E";
const GRAY  = "5B6479";
const LGRAY = "E9ECF3";
const LINE  = "D7DEEB";

const F_DISPLAY = "Arial";
const F_TEXT    = "Calibri";

// ───────── helpers ─────────
const inches = convertInchesToTwip;

function P(opts) { return new Paragraph(opts); }
function R(text, opts) { return new TextRun({ text, font: F_TEXT, size: 21, color: INK, ...opts }); }

function body(text, opts = {}) {
  return P({ alignment: AlignmentType.JUSTIFIED, spacing: { after: 160, line: 288 }, children: [R(text, opts)] });
}

function h1(text) {
  return P({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 420, after: 160 },
    children: [new TextRun({ text, font: F_DISPLAY, bold: true, size: 27, color: AZUL })],
  });
}

function h2(text, color = AZUL) {
  return P({
    spacing: { before: 260, after: 120 },
    children: [new TextRun({ text, font: F_DISPLAY, bold: true, size: 23, color })],
  });
}

function bullet(text, opts = {}) {
  return P({
    numbering: { reference: "bullets", level: 0 },
    spacing: { after: 100, line: 276 },
    children: [R(text, opts)],
  });
}

function note(text) {
  return P({
    alignment: AlignmentType.JUSTIFIED,
    spacing: { before: 80, after: 220, line: 276 },
    children: [new TextRun({ text, font: F_TEXT, size: 19, italics: true, color: GRAY })],
  });
}

function cell(children, { width, fill, vAlign = VerticalAlign.CENTER, borders = true } = {}) {
  return new TableCell({
    width: { size: width, type: WidthType.DXA },
    shading: fill ? { type: ShadingType.CLEAR, fill } : undefined,
    verticalAlign: vAlign,
    margins: { top: 90, bottom: 90, left: 110, right: 110 },
    borders: borders ? {
      top: { style: BorderStyle.SINGLE, size: 2, color: LINE },
      bottom: { style: BorderStyle.SINGLE, size: 2, color: LINE },
      left: { style: BorderStyle.SINGLE, size: 2, color: LINE },
      right: { style: BorderStyle.SINGLE, size: 2, color: LINE },
    } : undefined,
    children,
  });
}

function th(text, width) {
  return cell([P({ children: [new TextRun({ text, font: F_DISPLAY, bold: true, size: 18, color: "FFFFFF" })] })],
    { width, fill: AZUL });
}

function td(text, width, opts = {}) {
  return cell([P({ spacing: { line: 264 }, children: [new TextRun({ text, font: F_TEXT, size: 19, color: INK, ...opts })] })],
    { width, fill: opts.fill });
}

function mkTable(widths, rows) {
  return new Table({
    width: { size: widths.reduce((a, b) => a + b, 0), type: WidthType.DXA },
    columnWidths: widths,
    rows,
  });
}

const FULL = inches(6.5); // ancho útil de contenido

// ═══════════════════════════ PORTADA ═══════════════════════════
const logoBuf = fs.readFileSync("/home/claude/cuaderno/logo_educate.png");

const portada = [
  P({ alignment: AlignmentType.CENTER, spacing: { before: 600, after: 300 },
      children: [new ImageRun({ data: logoBuf, type: "png", transformation: { width: 210, height: 95 } })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 60 },
      children: [new TextRun({ text: "PROPUESTA DE TRABAJO", font: F_DISPLAY, bold: true, size: 20, color: ORO, characterSpacing: 24 })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: 80 },
      children: [new TextRun({ text: "Cuadernos de trabajo por área", font: F_DISPLAY, bold: true, size: 44, color: AZUL })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { before: 0, after: 260 },
      children: [new TextRun({ text: "y guías de clase para el docente", font: F_DISPLAY, bold: true, size: 44, color: AZUL })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { after: 500 },
      children: [new TextRun({
        text: "Seis áreas del Saber 11 · Matemáticas, Lectura Crítica, Sociales y Ciudadanas, Ciencias Naturales, Física e Inglés",
        font: F_TEXT, italics: true, size: 21, color: GRAY })] }),
  P({ alignment: AlignmentType.CENTER,
      spacing: { before: 440, after: 40 },
      children: [new TextRun({ text: "Presentada a", font: F_DISPLAY, bold: true, size: 17, color: ORO, characterSpacing: 16 })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { after: 220 },
      children: [new TextRun({ text: "Cristian Bueno — Gerente General, EDUCATE · Para el Saber", font: F_TEXT, size: 22, color: INK })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
      children: [new TextRun({ text: "Presentada por", font: F_DISPLAY, bold: true, size: 17, color: ORO, characterSpacing: 16 })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { after: 220 },
      children: [new TextRun({ text: "Nelson González — Asesor comercial y pedagógico", font: F_TEXT, size: 22, color: INK })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { after: 40 },
      children: [new TextRun({ text: "Fecha", font: F_DISPLAY, bold: true, size: 17, color: ORO, characterSpacing: 16 })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { after: 10 },
      children: [new TextRun({ text: "10 de octubre de 2026 · vigente por 15 días calendario", font: F_TEXT, size: 22, color: INK })] }),
  P({ children: [new PageBreak()] }),
];

// ═══════════════════════════ 1 · CONTEXTO ═══════════════════════════
const s1 = [
  h1("1 · Contexto y antecedente"),
  body("En EDUCATE dictamos clases de preparación para el Saber 11 los sábados, en un número creciente de colegios. "
    + "La calidad de la clase varía según qué profesor llegue ese sábado: algunos enseñan por competencias, otros "
    + "dictan cátedra, otros ignoran el libro. Auditar cada clase, con el número de colegios que atendemos hoy, no es viable."),
  body("La respuesta que construimos para Matemáticas — y que ya fue aprobada — fue sacar el método del profesor y "
    + "ponerlo en el cuaderno del estudiante: un cuaderno de trabajo que acompaña el libro sin reimprimir sus "
    + "preguntas, con una estrategia de pensamiento propia para cada una, entrenamiento con preguntas reales del "
    + "ICFES, un planeador del docente amarrado a los momentos de clase y a los documentos rectores del ICFES "
    + "(Marco de Referencia, Niveles de Desempeño, Guía de Orientación), y una guía de clase proyectable con la "
    + "metodología ya incorporada."),
  body("Esa primera misión de Matemáticas funciona como piloto probado. Esta propuesta lleva el mismo sistema a "
    + "las otras cinco áreas del Saber 11."),
];

// ═══════════════════════════ 2 · OBJETIVO ═══════════════════════════
const s2 = [
  h1("2 · Objetivo del proyecto"),
  body("Diseñar y construir, para cada una de las seis áreas del Saber 11, un sistema de acompañamiento "
    + "pedagógico — integrado en un único cuaderno de trabajo combinado, con un planeador del docente y una "
    + "guía de clase proyectable por área — de manera que la metodología de EDUCATE llegue al estudiante sin "
    + "depender del profesor que dicte la clase ese sábado."),
];

// ═══════════════════════════ ESTRUCTURA PEDAGÓGICA (momentos y clases) ═══════════════════════════
const AREAS = 6;
const MOMENTOS_POR_AREA = 6;           // seis momentos por área, cada uno con su taller de 10 preguntas del libro + ICFES
const HOJAS_POR_MOMENTO = 7;           // ≈ 6 a 8 hojas por momento, incluyendo el entrenamiento ICFES
const CLASES_POR_AREA = 8;             // fijo por área — distribuye los 6 momentos y la socialización del simulacro, independiente del número de momentos
const HOJAS_POR_AREA = MOMENTOS_POR_AREA * HOJAS_POR_MOMENTO;        // 42
const TOTAL_MOMENTOS = MOMENTOS_POR_AREA * AREAS;                    // 36
const TOTAL_CLASES = CLASES_POR_AREA * AREAS;                        // 48
const TOTAL_HOJAS_TRABAJO = HOJAS_POR_AREA * AREAS;                  // 252

// ═══════════════════════════ 3 · ALCANCE ═══════════════════════════
const s3 = [
  h1("3 · Alcance del proyecto"),
  body("El cuaderno es uno solo: un único libro físico, tamaño carta, que reúne las seis áreas del Saber 11 completas "
    + "— como los cuadernos de varias materias que un estudiante lleva en una sola carpeta. Dentro de ese cuaderno, "
    + "cada área tiene su propia portada, su propia identidad de color y su propio instrumento de pensamiento, "
    + "pero las secciones de apertura y cierre — portada general, introducción, metas, metodología, psicología y "
    + "cierre post-prueba — se recorren una sola vez, al principio y al final del libro (ver sección 4)."),
  body("Dentro de ese cuaderno único, cada una de las seis áreas — Matemáticas, Lectura Crítica, Sociales y "
    + "Ciudadanas, Ciencias Naturales, Física e Inglés — entrega su contenido completo, no una muestra:"),
  bullet(`Hojas de trabajo: el taller de 10 preguntas del libro de cada uno de los ${MOMENTOS_POR_AREA} momentos `
    + "por área, con el instrumento de pensamiento propio del área, entrenamiento con preguntas reales del ICFES "
    + "integrado a cada momento, y hojas de simulacro."),
  bullet(`Planeador del docente: las ${CLASES_POR_AREA} clases de cada área — que distribuyen los `
    + `${MOMENTOS_POR_AREA} momentos y la socialización del simulacro, independientemente de cómo se reparta cada `
    + "momento entre clases — cada una con su objetivo específico y su guion, los DBA y afirmaciones del Marco de "
    + "Referencia que se trabajan, el mapa de preguntas con su estrategia y competencia, los niveles de desempeño "
    + "oficiales, y un banco de dinámicas."),
  bullet("Guía de clase proyectable: una por cada una de esas clases, con la estrategia, las preguntas y los "
    + "tiempos de esa clase específica ya incorporados."),
  P({ alignment: AlignmentType.JUSTIFIED, spacing: { before: 160, after: 140 }, shading: { type: ShadingType.CLEAR, fill: "FFF6E6" },
      border: { left: { color: ORO, size: 24, style: BorderStyle.SINGLE, space: 10 } },
      indent: { left: 120 },
      children: [new TextRun({ text: "Alcance explícito de esta propuesta:  ", font: F_DISPLAY, bold: true, size: 20, color: "8A5A0B" }),
                 new TextRun({ text: `el cuaderno completo de las seis áreas, de principio a fin — ${MOMENTOS_POR_AREA} `
                   + `momentos por área y ${CLASES_POR_AREA} clases por área (${TOTAL_CLASES} clases en total, que `
                   + `distribuyen esos momentos y la socialización del simulacro) — con su planeador del docente y `
                   + `su guía de clase proyectable por clase (el desglose está en `
                   + "la sección 4). No es una muestra ni un piloto: es el libro completo que EDUCATE entrega a sus "
                   + "estudiantes, con la metodología y la identidad visual documentadas para que el sistema se "
                   + "pueda sostener y actualizar sin asesoría externa.", font: F_TEXT, size: 20, color: "5C4207" })] }),
];

// ═══════════════════════════ 4 · ESTRUCTURA DEL CUADERNO ═══════════════════════════
const estructura = [
  ["Portada general", "1", "EDUCATE, el nombre del estudiante y el año."],
  ["Introducción", "2", "La intención del cuaderno contada al estudiante: por qué existe, qué le va a pedir, qué le va a devolver. Un mensaje, no un reglamento."],
  ["Metas", "2", "Los puntajes de referencia de las carreras que más pregunta el estudiante, y un ejercicio de metas guiado — ver nota metodológica abajo — con espacio para que el estudiante lo complete a mano."],
  ["Qué te vas a encontrar", "2", "La metodología explicada con flechas: cómo se lee una hoja, qué es «Piensa en esto», el paso a paso, el Salvavidas y la Bitácora. Se entiende antes de llegar a la primera pregunta."],
  ["La psicología de la meta", "2", "Una página emotiva para el estudiante — con apoyo visual, poco texto — y una nota aparte dirigida a los coordinadores, sobre cómo leer el compromiso del estudiante con sus propias metas."],
  ["Portada de cada área", "1 × 6", "Una por área, con su color y su instrumento de pensamiento. Es el separador dentro del cuaderno único."],
  ["Hojas de trabajo", `${HOJAS_POR_MOMENTO} × ${MOMENTOS_POR_AREA} × ${AREAS}`,
    `El taller de 10 preguntas de cada uno de los ${MOMENTOS_POR_AREA} momentos por área (≈ ${HOJAS_POR_MOMENTO} hojas con el entrenamiento ICFES incluido). Se distribuye en las clases del área (sección 9).`],
  ["Cierre post-prueba", "3", "Una sola vez, al final del cuaderno: espacio de reflexión después del simulacro o de la prueba real, y bitácora general de las seis áreas."],
];
const wEst = [inches(1.7), inches(0.8), inches(4.0)];
const totalEstruct = 1+2+2+2+2+6+TOTAL_HOJAS_TRABAJO+3;
const s3b = [
  h1("4 · Estructura del cuaderno"),
  body("El cuaderno se abre y se cierra una sola vez; lo que se repite seis veces es solo la portada de cada "
    + "área y sus hojas de trabajo. Así se reparte el total:"),
  mkTable(wEst, [
    new TableRow({ tableHeader: true, children: [th("Sección", wEst[0]), th("Hojas", wEst[1]), th("Qué lleva", wEst[2])] }),
    ...estructura.map(([a, h, d], i) => new TableRow({ cantSplit: true, children: [
      td(a, wEst[0], { bold: true, fill: i % 2 ? LGRAY : "FFFFFF" }),
      cell([P({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: h, font: F_TEXT, bold: true, size: 19, color: ORO })] })],
        { width: wEst[1], fill: i % 2 ? LGRAY : "FFFFFF" }),
      td(d, wEst[2], { fill: i % 2 ? LGRAY : "FFFFFF" }),
    ] })),
    new TableRow({ cantSplit: true, children: [
      td("Total · cuaderno completo", wEst[0], { bold: true }),
      cell([P({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: `≈ ${totalEstruct}`, font: F_DISPLAY, bold: true, size: 19, color: AZUL })] })],
        { width: wEst[1] }),
      td("Esto es lo que cotiza la propuesta (sección 9), sin fases pendientes.", wEst[2], { italics: true, color: GRAY }),
    ] }),
  ]),
  h2("Nota metodológica · la sección de Metas"),
  body("Para que la sección de Metas sea algo más que una cartelera motivacional, la armamos sobre WOOP "
    + "(Wish–Outcome–Obstacle–Plan), la técnica de la psicóloga Gabriele Oettingen que combina visualizar la "
    + "meta con nombrar el obstáculo propio y planear la respuesta — es el hallazgo central de su investigación "
    + "sobre por qué la visualización sola no mueve a nadie a actuar. Se presenta con el lenguaje visual que "
    + "pediste — caritas, flechas, espacio para dibujar — pero cada estudiante termina con un obstáculo y un "
    + "plan propios escritos a mano, no solo una imagen pegada."),
];

// ═══════════════════════════ 4 · METODOLOGÍA ═══════════════════════════
const metPasos = [
  ["Documentos rectores", "Por cada área se parte del Marco de Referencia, los Niveles de Desempeño y la Guía de Orientación del ICFES vigentes. Todo lo que se construye debe poder rastrearse hasta uno de los tres."],
  ["Identidad del área", "Se define el instrumento de pensamiento propio de cada área — en Matemáticas es la cuadrícula de trabajo; en otras áreas será su equivalente — y su paleta de color dentro de la línea gráfica de EDUCATE."],
  ["Construcción del cuaderno", "Se desarrolla el contenido completo sobre el libro vigente de cada área, con el andamiaje de pensamiento y el banco de preguntas ICFES verificadas por año y cuadernillo."],
  ["Construcción del planeador", "Se planean las dos clases de cada momento por separado — cada una con su objetivo y su guion — cruzadas con el Marco de Referencia."],
  ["Construcción de la guía de clase", "Se traduce el planeador en una presentación proyectable, con la estrategia visible y las preguntas trabajadas."],
  ["Revisión especializada", "Cada área pasa por la revisión de un especialista antes de la entrega final (sección 6)."],
  ["Ajustes y entrega", "Se incorporan las observaciones de los especialistas y se entrega el paquete final de cada área."],
];
const s4 = [
  h1("5 · Metodología de trabajo"),
  ...metPasos.flatMap(([t, d], i) => [
    P({ spacing: { before: i ? 180 : 0, after: 60 },
        children: [new TextRun({ text: `${i + 1}.  `, font: F_DISPLAY, bold: true, size: 21, color: ORO }),
                   new TextRun({ text: t, font: F_DISPLAY, bold: true, size: 21, color: AZUL })] }),
    P({ spacing: { after: 60, line: 276 }, indent: { left: 260 },
        children: [R(d, { size: 20 })] }),
  ]),
];

// ═══════════════════════════ 5 · EQUIPO Y REVISIÓN ═══════════════════════════
const revRows = [
  ["Matemáticas", "Revisión directa de Nelson González, sin especialista externo adicional"],
  ["Lectura Crítica", "Especialista en Lectura Crítica (por confirmar)"],
  ["Sociales y Ciudadanas", "Especialista en Ciencias Sociales (por confirmar)"],
  ["Ciencias Naturales (Biología y Química)", "Especialista en Biología/Química (por confirmar)"],
  ["Física", "Revisión directa de Nelson González, sin especialista externo adicional"],
  ["Inglés", "Especialista en Inglés (por confirmar)"],
];
const wRev = [inches(2.3), inches(4.2)];
const s5 = [
  h1("6 · Equipo y revisión especializada"),
  body("Antes de la entrega final, cada área pasa por la revisión de un especialista. La vinculación de los "
    + "especialistas de Lectura Crítica, Sociales y Ciudadanas, Ciencias Naturales e Inglés corre por cuenta de "
    + "EDUCATE; Matemáticas y Física las reviso directamente yo."),
  mkTable(wRev, [
    new TableRow({ tableHeader: true, children: [th("Área", wRev[0]), th("Revisión especializada", wRev[1])] }),
    ...revRows.map(([a, r], i) => new TableRow({ cantSplit: true, children: [
      td(a, wRev[0], { bold: true, fill: i % 2 ? LGRAY : "FFFFFF" }),
      td(r, wRev[1], { fill: i % 2 ? LGRAY : "FFFFFF" }),
    ] })),
  ]),
  note("Los nombres de los especialistas se confirman al inicio del proyecto y no afectan el cronograma propuesto en la sección 7."),
];

// ═══════════════════════════ 6 · CRONOGRAMA ═══════════════════════════
const cronRows = [
  ["1", "Documentos rectores y mapeo curricular de las seis áreas · identidad visual y de instrumento de pensamiento por área."],
  ["2", "Cuaderno, planeador y guía de clase: Matemáticas y Lectura Crítica."],
  ["3", "Cuaderno, planeador y guía de clase: Sociales y Ciudadanas y Ciencias Naturales."],
  ["4", "Cuaderno, planeador y guía de clase: Física e Inglés. Cierre de la primera entrega parcial."],
  ["5", "Revisión especializada de las seis áreas y recolección de observaciones."],
  ["6", "Ajustes según especialistas. Validación final de preguntas y claves del ICFES."],
  ["7", "Documento maestro de metodología, para replicar el sistema a futuras misiones. Empaquetado final."],
  ["8", "Entrega final y cierre del proyecto."],
];
const wCron = [inches(0.9), inches(5.6)];
const s6 = [
  h1("7 · Cronograma — 8 semanas"),
  mkTable(wCron, [
    new TableRow({ tableHeader: true, children: [th("Semana", wCron[0]), th("Fase", wCron[1])] }),
    ...cronRows.map(([s, d], i) => new TableRow({ cantSplit: true, children: [
      cell([P({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: s, font: F_DISPLAY, bold: true, size: 20, color: AZUL })] })],
        { width: wCron[0], fill: i % 2 ? LGRAY : "FFFFFF" }),
      td(d, wCron[1], { fill: i % 2 ? LGRAY : "FFFFFF" }),
    ] })),
  ]),
];

// ═══════════════════════════ 7 · ENTREGABLES ═══════════════════════════
const s7 = [
  h1("8 · Entregables finales"),
  bullet("1 cuaderno de trabajo combinado para las seis áreas, completo: portada, introducción, metas, "
    + "metodología, psicología y cierre post-prueba, más el contenido completo de cada área "
    + "(detalle hoja por hoja en la sección 4)."),
  bullet(`6 planeadores del docente (uno por área), con la planeación completa de sus ${CLASES_POR_AREA} `
    + `clases — que distribuyen los ${MOMENTOS_POR_AREA} momentos del área y la socialización del simulacro — `
    + `no solo una muestra.`),
  bullet(`${TOTAL_CLASES} guías de clase proyectables en total, una por cada clase (detalle por área en la sección 9).`),
  bullet("1 documento maestro de metodología, para que el sistema se pueda mantener y actualizar sin "
    + "asesoría externa."),
  bullet("Reporte de observaciones y ajustes de la revisión especializada."),
];

// ═══════════════════════════ 8 · INVERSIÓN ═══════════════════════════
const RATE_HOJA = 2;   // horas por hoja de trabajo (andamiaje, ICFES, diagramación)
const RATE_CLASE = 10; // horas por clase (planeador + guía de clase proyectable de esa clase)
const horasAreaNueva = HOJAS_POR_AREA * RATE_HOJA + CLASES_POR_AREA * RATE_CLASE; // 42×2 + 8×10 = 164
// Matemáticas ya tiene 10 hojas y 1 clase construidas en el piloto entregado
const HOJAS_YA_CONSTRUIDAS_MATE = 10;
const CLASES_YA_CONSTRUIDAS_MATE = 1;
const creditoMatematicas = HOJAS_YA_CONSTRUIDAS_MATE * RATE_HOJA + CLASES_YA_CONSTRUIDAS_MATE * RATE_CLASE; // 10×2 + 1×10 = 30
const horasMatematicas = horasAreaNueva - creditoMatematicas + 10; // + ajuste al estándar final
const cargaRows = [
  ["Estructura del cuaderno (portada, introducción, metas, metodología, psicología, cierre)", "20", "una sola vez para las seis áreas"],
  ["Matemáticas", String(horasMatematicas),
    `${CLASES_POR_AREA} clases · la primera ya construida como piloto; se completa y ajusta al estándar final`],
  ["Lectura Crítica", String(horasAreaNueva), `${CLASES_POR_AREA} clases, cada una con su planeador y su guía de clase`],
  ["Sociales y Ciudadanas", String(horasAreaNueva), `${CLASES_POR_AREA} clases, cada una con su planeador y su guía de clase`],
  ["Ciencias Naturales", String(horasAreaNueva), `${CLASES_POR_AREA} clases, cada una con su planeador y su guía de clase`],
  ["Física", String(horasAreaNueva), `${CLASES_POR_AREA} clases, cada una con su planeador y su guía de clase`],
  ["Inglés", String(horasAreaNueva), `${CLASES_POR_AREA} clases, cada una con su planeador y su guía de clase`],
  ["Coordinación general, documentos rectores, identidad visual y documento maestro", "40", ""],
];
const totalHoras = cargaRows.reduce((acc, [, h]) => acc + Number(h), 0);
const wCar = [inches(2.6), inches(0.9), inches(3.0)];
const s8 = [
  h1("9 · Inversión"),
  body(`Esta es la carga de horas del cuaderno completo, con la estructura (sección 4) contada una sola vez `
    + `y el contenido completo de cada una de las seis áreas: ${MOMENTOS_POR_AREA} momentos por área y `
    + `${CLASES_POR_AREA} clases por área — ${TOTAL_CLASES} clases en total — cada una con su planeador y `
    + `su guía de clase proyectable — no una muestra por área.`),
  mkTable(wCar, [
    new TableRow({ tableHeader: true, children: [th("Área / frente de trabajo", wCar[0]), th("Horas", wCar[1]), th("Observación", wCar[2])] }),
    ...cargaRows.map(([a, h, o], i) => new TableRow({ cantSplit: true, children: [
      td(a, wCar[0], { bold: true, fill: i % 2 ? LGRAY : "FFFFFF" }),
      cell([P({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: h, font: F_TEXT, size: 19, color: INK })] })],
        { width: wCar[1], fill: i % 2 ? LGRAY : "FFFFFF" }),
      td(o, wCar[2], { italics: true, color: GRAY, fill: i % 2 ? LGRAY : "FFFFFF" }),
    ] })),
    new TableRow({ cantSplit: true, children: [
      td("Total", wCar[0], { bold: true }),
      cell([P({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: String(totalHoras), font: F_DISPLAY, bold: true, size: 19, color: AZUL })] })],
        { width: wCar[1], fill: "FFFFFF" }),
      td(`${TOTAL_MOMENTOS} momentos (contenido) y ${TOTAL_CLASES} clases (planeador y guía) entre las seis áreas.`, wCar[2], { italics: true, color: GRAY }),
    ] }),
  ]),
  note("La tarifa efectiva de este proyecto — valor total sobre horas — queda muy por debajo de una consultoría "
    + "de mercado para un sistema de seis áreas completas; se sostiene porque es un proyecto de volumen, con "
    + "una sola fase de entrega."),
  P({ alignment: AlignmentType.JUSTIFIED, spacing: { before: 100, after: 240 }, shading: { type: ShadingType.CLEAR, fill: "FFF6E6" },
      border: { left: { color: ORO, size: 24, style: BorderStyle.SINGLE, space: 10 } }, indent: { left: 120 },
      children: [new TextRun({ text: "Este valor ya incluye:  ", font: F_DISPLAY, bold: true, size: 20, color: "8A5A0B" }),
                 new TextRun({ text: "la suscripción ampliada de Claude durante los dos meses del proyecto "
                   + "(≈ $660.000 COP, detalle en la sección 10). La herramienta agiliza la trazabilidad entre los "
                   + "documentos de las seis áreas y la consistencia de formato y de estética a este ritmo — pero no "
                   + "reemplaza el trabajo: ejecuta sobre el Marco de Referencia ya trabajado, los bancos de preguntas "
                   + "ICFES ya clasificados y verificados, y el sistema de identidad de EDUCATE, construidos a lo largo "
                   + "de este proyecto. Esa base de conocimiento acumulado es lo que se cotiza; la herramienta solo lo "
                   + "ejecuta más rápido.", font: F_TEXT, size: 20, color: "5C4207" })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { before: 200, after: 80 },
      shading: { type: ShadingType.CLEAR, fill: AZUL },
      children: [new TextRun({ text: "VALOR TOTAL DE LA PROPUESTA", font: F_DISPLAY, bold: true, size: 18, color: "BFD4F2", characterSpacing: 16 })] }),
  P({ alignment: AlignmentType.CENTER, spacing: { after: 240 },
      shading: { type: ShadingType.CLEAR, fill: AZUL },
      children: [new TextRun({ text: "$ 4.500.000 COP", font: F_DISPLAY, bold: true, size: 44, color: "FFFFFF" })] }),
  h2("Forma de pago"),
];
const pagoRows = [
  ["Anticipo · al confirmar la propuesta", "30 %", "$ 1.350.000"],
  ["Segundo pago · semana 4, entrega parcial (3 áreas)", "35 %", "$ 1.575.000"],
  ["Pago final · semana 8, entrega y validación de especialistas", "35 %", "$ 1.575.000"],
];
const wPag = [inches(3.6), inches(0.9), inches(2.0)];
s8.push(
  mkTable(wPag, [
    new TableRow({ tableHeader: true, children: [th("Hito", wPag[0]), th("%", wPag[1]), th("Valor", wPag[2])] }),
    ...pagoRows.map(([h, p, v], i) => new TableRow({ cantSplit: true, children: [
      td(h, wPag[0], { fill: i % 2 ? LGRAY : "FFFFFF" }),
      cell([P({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: p, font: F_TEXT, bold: true, size: 19, color: ORO })] })],
        { width: wPag[1], fill: i % 2 ? LGRAY : "FFFFFF" }),
      cell([P({ alignment: AlignmentType.CENTER, children: [new TextRun({ text: v, font: F_DISPLAY, bold: true, size: 19, color: AZUL })] })],
        { width: wPag[2], fill: i % 2 ? LGRAY : "FFFFFF" }),
    ] })),
  ]),
  note("Los valores no incluyen impuestos aplicables, si los hubiera."),
);

// ═══════════════════════════ 9 · RECURSOS NECESARIOS ═══════════════════════════
const s9 = [
  h1("10 · Recursos necesarios para la ejecución"),
  h2("Herramienta de trabajo: Claude"),
  body("Los cuadernos, planeadores y guías de este proyecto se construyen con apoyo de Claude, la herramienta de "
    + "IA ya probada con Matemáticas. Sostener el ritmo de producción que exige este cronograma — seis áreas "
    + "completas en ocho semanas, con trazabilidad entre todos sus documentos — requiere la suscripción de uso "
    + "ampliado: USD $100 al mes (≈ $330.000 COP al mes, TRM aproximada de octubre de 2026), ≈ $660.000 COP "
    + "durante los dos meses del proyecto. Ese costo ya está incluido en el valor total de la sección 9; no es "
    + "un cobro adicional."),
  body("Vale la pena ser explícito sobre qué hace esta herramienta y qué no. Claude no reemplaza el trabajo "
    + "pedagógico ni la decisión editorial: ejecuta, más rápido y con más consistencia, sobre un conocimiento "
    + "que no se improvisa — el Marco de Referencia trabajado área por área, los bancos de preguntas ICFES ya "
    + "clasificados y verificados por año y cuadernillo, el sistema de identidad visual de EDUCATE, y el "
    + "historial completo de decisiones desde el piloto de Matemáticas. Esa base de conocimiento acumulado — "
    + "no la suscripción — es lo que hace posible este cuaderno, y es lo que no cualquiera puede reproducir "
    + "sin empezar de cero."),
  h2("Otros recursos"),
  bullet("Acceso a bancos de preguntas oficiales del ICFES adicionales a los ya entregados, si se requieren más años o cuadernillos."),
  bullet("Los documentos rectores vigentes de cada área — Marco de Referencia, Niveles de Desempeño y Guía de Orientación."),
  bullet("Los PDF de los libros de cada área, entregados con tiempo de antelación razonable frente al cronograma de la sección 7."),
];

// ═══════════════════════════ 10 · CONDICIONES ═══════════════════════════
const s10 = [
  h1("11 · Condiciones generales"),
  bullet("Esta propuesta tiene una vigencia de 15 días calendario desde la fecha de presentación."),
  bullet("Incluye una ronda de ajustes por entregable a partir de la retroalimentación de EDUCATE y de los especialistas."),
  bullet("Cambios de alcance — más misiones por área, más áreas, o rediseño de una identidad ya aprobada — se cotizan aparte."),
  bullet("El material entra en producción a partir de la confirmación del anticipo."),
  bullet("El material desarrollado queda en propiedad de EDUCATE · Para el Saber una vez cancelado en su totalidad."),
  bullet("La información y las preguntas suministradas por EDUCATE para este proyecto se manejan de forma confidencial y solo se usan para este fin."),
];

// ═══════════════════════════ 11 · ACEPTACIÓN ═══════════════════════════
function firma(rol) {
  return [
    P({ spacing: { before: 500, after: 10 },
        children: [new TextRun({ text: "_______________________________", font: F_TEXT, size: 21, color: LINE })] }),
    P({ spacing: { after: 4 }, children: [new TextRun({ text: "Nombre", font: F_DISPLAY, bold: true, size: 17, color: GRAY })] }),
    P({ spacing: { after: 160 }, children: [R(rol, { size: 19 })] }),
  ];
}
const s11 = [
  P({ children: [new PageBreak()] }),
  h1("12 · Aceptación de la propuesta"),
  body("La firma de esta propuesta, junto con la confirmación del anticipo, da inicio al proyecto en los términos descritos."),
  ...firma(""),
  P({ spacing: { after: 4 }, children: [new TextRun({ text: "Cargo", font: F_DISPLAY, bold: true, size: 17, color: GRAY })] }),
  P({ spacing: { after: 160 }, children: [R("Gerente General, EDUCATE · Para el Saber", { size: 19 })] }),
  P({ spacing: { after: 4 }, children: [new TextRun({ text: "Firma y fecha", font: F_DISPLAY, bold: true, size: 17, color: GRAY })] }),
  P({ spacing: { after: 400 }, children: [R("", { size: 19 })] }),
  P({ spacing: { before: 260, after: 40 },
      children: [new TextRun({ text: "Nelson González", font: F_DISPLAY, bold: true, size: 21, color: AZUL })] }),
  P({ spacing: { after: 0 },
      children: [new TextRun({ text: "Asesor comercial y pedagógico — EDUCATE · Para el Saber", font: F_TEXT, italics: true, size: 19, color: GRAY })] }),
];

// ═══════════════════════════ documento ═══════════════════════════
const doc = new Document({
  numbering: {
    config: [{
      reference: "bullets",
      levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
                 style: { paragraph: { indent: { left: 420, hanging: 260 } },
                          run: { color: ORO, font: F_DISPLAY } } }],
    }],
  },
  styles: {
    default: { document: { run: { font: F_TEXT, size: 21, color: INK } } },
  },
  sections: [{
    properties: {
      page: {
        size: { width: inches(8.5), height: inches(11) },
        margin: { top: inches(0.9), bottom: inches(0.9), left: inches(1), right: inches(1) },
      },
    },
    headers: {
      default: new Header({ children: [P({
        alignment: AlignmentType.RIGHT,
        children: [new TextRun({ text: "EDUCATE · Para el Saber — Propuesta de trabajo", font: F_TEXT, size: 15, color: GRAY })],
      })] }),
    },
    footers: {
      default: new Footer({ children: [P({
        alignment: AlignmentType.CENTER,
        children: [
          new TextRun({ text: "Página ", font: F_TEXT, size: 15, color: GRAY }),
          new TextRun({ children: [PageNumber.CURRENT], font: F_TEXT, size: 15, color: GRAY }),
          new TextRun({ text: " de ", font: F_TEXT, size: 15, color: GRAY }),
          new TextRun({ children: [PageNumber.TOTAL_PAGES], font: F_TEXT, size: 15, color: GRAY }),
        ],
      })] }),
    },
    children: [
      ...portada, ...s1, ...s2, ...s3, ...s3b, ...s4, ...s5, ...s6, ...s7, ...s8, ...s9, ...s10, ...s11,
    ],
  }],
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync("Propuesta_EduCaTe_Cuadernos_por_Area.docx", buf);
  console.log("listo:", buf.length, "bytes");
});
