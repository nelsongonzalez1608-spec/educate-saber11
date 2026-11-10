#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Informe de hallazgos del libro para la editorial y hallazgos internos (10 nov 2026).

   python3 libro/informe_editorial.py

Salidas:
  entregables/EDUCATE_Informe_hallazgos_editorial_10nov.pdf
  entregables/EDUCATE_Hallazgos_internos_10nov.pdf
  tablero/hallazgos_editorial.csv

Los textos para la editorial están en informe_editorial_datos.py (redactados a partir de
tablero/hallazgos.csv). Este archivo arma HTML (Carlito) y lo pasa a PDF con Playwright.
Al final comprueba que las 346 filas del tablero queden en algún lugar (informe, interno o
lista de no enviadas) y que ninguna quede dos veces como hallazgo.
"""
import base64
import csv
import html
import os
import subprocess
import sys
from collections import Counter, OrderedDict

AQUI = os.path.dirname(os.path.realpath(__file__))
RAIZ = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)
from informe_editorial_datos import H, REPARTO, ICFES  # noqa: E402

TMP = os.environ.get("INFORME_TMP", "/tmp/claude-0/informe_editorial")
os.makedirs(TMP, exist_ok=True)

AREAS = OrderedDict([
    ("MAT", ("Matemáticas", "#1F4E8C")),
    ("LC", ("Lectura Crítica", "#A82424")),
    ("SOC", ("Sociales y Ciudadanas", "#C9821B")),
    ("BIO", ("Biología", "#30843C")),
    ("QUI", ("Química", "#0F7A68")),
    ("FIS", ("Física", "#5C7A1E")),
    ("ING", ("Inglés", "#1BA0A8")),
])
SEV = ["Alta", "Media", "Baja"]
SEV_COLOR = {"Alta": "#A82424", "Media": "#B8730F", "Baja": "#242478",
             "Atención": "#30843C", "Considerar": "#6E7480"}
PREGUNTAS = {"MAT": 60, "LC": 60, "SOC": 60, "BIO": 60, "QUI": 60, "FIS": 60, "ING": 127}

# ─────────── lo que no va al informe de la editorial ───────────
NUESTRO = [13, 15, 16, 21, 23, 28, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 97, 335, 339, 340]
PROPIOS = [336, 337, 338, 344, 346]           # material de EDUCATE sin el rótulo «Nuestro»
GESTION = [22, 29, 34, 57, 58, 59, 81, 129, 130, 131, 157, 167, 200, 213, 312, 334]
MARCA_AGUA = [119, 128, 178, 188]               # van a la sección de indicios
NO_ENVIADAS = {
    68: "«Final de lA Misión»: la «A» mayúscula solo existe en la capa de texto del PDF; impreso, el "
        "título va en versalitas y no se ve (comprobado en la p. 374 de Sociales; lo confirma la fila 297)",
    80: "Igual que la 68 (p. 386 de Sociales)",
    297: "Igual que la 68 (Inglés M4); la propia fila dice que no requiere corrección",
    229: "Nota didáctica: la propia fila dice «sin error»",
    269: "Nota didáctica: «no es error» (falso amigo «lecture»)",
    295: "Nota didáctica: la fila dice «bien construida»",
    298: "Nota didáctica: «buen distractor»",
    315: "Nota didáctica: «inferencia legítima»",
    333: "Nota didáctica: «sin efecto en la clave»",
    342: "Consolida las filas 2, 7 y 9 (Matemáticas); se informan allí",
    343: "Consolida las filas 1, 3, 4 y 8 (Matemáticas); se informan allí",
    311: "Se informa junto con la 310 (erratas del SIMULACRO II, Inglés Parte 6)",
    301: "Se informa junto con la 296 (numeración que se reinicia en cada bloque)",
    317: "Se informa junto con la 296 (numeración que se reinicia en cada bloque)",
    306: "Igual que la 68 (Inglés M5): «lA» no se ve impreso",
}
REPARTO_SOLO = [70, 103, 112, 118, 156, 166, 177, 187, 211, 222, 230, 235, 251, 258, 285, 303, 318]

ACCION = {
    13: "Se recalculó el alto de los instrumentos de las 23 hojas; verifica_cajas.py mide ahora cada "
        "instrumento contra el alto disponible.",
    15: "Instrumentos rehechos sin borde en la opción correcta; verifica_pistas.py lo vigila.",
    16: "chip() mide el ancho con tw() y la fuente real.",
    21: "Se consultó a la Gerencia. La decisión sobre nombres de políticos vivos sigue pendiente "
        "antes de imprimir (CLAUDE.md § 9, punto 6).",
    23: "La línea de tiempo se ajustó al ancho de la tarjeta.",
    28: "Las pistas pasaron a GRAY; verifica_cajas.py detecta texto en LGRAY.",
    33: "Se quitaron las mayúsculas de los distractores; verifica_pistas.py revisa también la tipografía.",
    35: "Las 30 hojas se rehicieron con rehace_hojas.py (alto 1010 con franja).",
    36: "Decisión de Nelson (6 nov): las 42 páginas de misión pasaron al azul #1F4E8C.",
    37: "unir() y verifica() reconstruidos el 6 nov.",
    38: "Salvavidas claro y único en todas las áreas; 98 páginas de misión rehechas.",
    39: "Apertura rehecha a 7 áreas, colores nuevos y salvavidas claro (y después en estilo B).",
    40: "No se tocó. Se resuelve con la fila 339 al aplicar el estilo B. Verificar en la apertura y "
        "las hojas nuevas.",
    41: "Pendiente. La apertura se rehízo en estilo B (6 páginas): verificar si el ejemplo de membrete "
        "con año sigue y agregar la explicación del membrete genérico.",
    42: "Se agregó la frase «en la prueba son una sola: Ciencias Naturales, con un solo puntaje».",
    43: "Pendiente. Verificar si sigue en la portada del estilo B.",
    97: "construye.py arma cada módulo en su propio proceso; verifica_cajas.py compara la misión de la "
        "cabecera con la del archivo.",
    335: "Corregido el 9 nov en las 8 guías, en clase_viva.py y en verifica_guias.js (mira lo que se "
         "pinta). Las guías se volvieron a entregar.",
    339: "Se corrige al aplicar el estilo B (las tres propuestas ya no tienen esas líneas).",
    340: "Pendiente según el tablero. El commit c9bcad2 dice «Misión 6 de Mate en el orden del "
         "cuaderno»: verificar si ya quedó resuelto y cerrar la fila.",
    336: "Corregido en la guía proyectable; falta corregir TEXTOS_GUIA_DOCENTE.md (sigue diciendo "
         "artículo 213 en las líneas 681, 684 y 1094).",
    337: "Pendiente: cotejar con el cuadernillo 2016-1. soc4_icfes.py y TEXTOS_GUIA_DOCENTE.md siguen "
         "con «Charlie».",
    338: "Pendiente: un especialista decide la competencia de las 8 preguntas.",
    344: "Resuelto con la versión 2 de las hojas de simulacro, aprobada por Nelson el 10 nov.",
    346: "Igual que la 339: se decide junto con la cabecera del cuaderno.",
}
GESTION_NOTA = {
    22: "Falta una pregunta oficial de la estrategia 3 de Sociales M1.",
    29: "Ítem del ASED descartado por una opción mal nombrada.",
    34: "El ASED reinicia la numeración por sección.",
    57: "Pregunta oficial con tema delicado (Sociales M3); alternativa: ítem 75.",
    58: "Criterio de membrete con año: resuelto por la decisión del 6 nov (membrete siempre genérico).",
    59: "Cruce de ítems entre Sociales M3 y M4: corregido.",
    81: "Nombre de archivo de Drive («2016-2») distinto de la portada («2016-1»).",
    129: "Fotocopia poco legible del ítem 99; se redibujó: cotejar con un cuadernillo limpio.",
    130: "Adaptación de las opciones dibujadas del ítem 100 a texto.",
    131: "Reservas duplicadas de ítems de Biología; línea «RETIRADA».",
    157: "Preguntas del SIMULACRO II en Química M1. El tablero dice «Pendiente de decisión», pero la "
         "decisión del 7 nov ya acepta el SIMULACRO II como oficial: cerrar la fila.",
    167: "Igual que la 157 (Química M2): cerrar la fila.",
    200: "Preguntas del SIMULACRO II leídas en versión de texto: cotejar con el PDF.",
    213: "Igual que la 200.",
    312: "Inglés M5: las cuatro ICFES tienen erratas; decisión de Nelson pendiente (a, b o c).",
    334: "Sello «Alto» de Inglés M6: deuda con el planeador de Inglés.",
}

# ─────────── utilidades ───────────
e = html.escape


def leer_tablero():
    with open(os.path.join(RAIZ, "tablero", "hallazgos.csv"), encoding="utf-8") as f:
        return {int(r["n"]): r for r in csv.DictReader(f)}


def logo_data():
    with open(os.path.join(AQUI, "logo_educate.png"), "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()


def pag_txt(p):
    if not p or p == "—":
        return "—"
    return ("pp. " if (" " in p or "–" in p) else "p. ") + p.replace(" a ", "–")


def mision_txt(m):
    return "Toda el área" if m == 0 else f"Misión {m}"


CSS = """
@page { size: Letter; margin: 17mm 19mm 19mm 19mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: Carlito, Calibri, sans-serif; font-size: 10.6pt; line-height: 1.36;
       color: #1E2230; margin: 0; background: #fff; }
p { text-align: justify; hyphens: auto; -webkit-hyphens: auto; margin: 0 0 7pt 0; }
h1, h2, h3, h4 { font-weight: 700; margin: 0; line-height: 1.15; }
.salto { break-before: page; }
.mono { font-family: 'Space Mono', monospace; letter-spacing: .02em; }
.rot { font-size: 7.6pt; text-transform: uppercase; letter-spacing: .09em; color: #5B6170;
       font-weight: 700; }
/* portada */
.portada { height: 240mm; position: relative; }
.portada .logo { width: 46mm; }
.portada .bloque { position: absolute; top: 62mm; left: 0; right: 0; border-left: 7px solid #242478;
                   padding: 2mm 0 2mm 9mm; }
.portada h1 { font-size: 31pt; color: #242478; }
.portada .sub { font-size: 15pt; color: #1E2230; margin-top: 5mm; }
.portada .fecha { font-size: 11.5pt; color: #5B6170; margin-top: 3mm; }
.portada .cifras { position: absolute; top: 140mm; left: 0; right: 0; display: flex; gap: 5mm; }
.cifra { flex: 1; background: #F3F4F8; border-left: 4px solid #242478; padding: 4mm 4mm 3.5mm 5mm; }
.cifra b { display: block; font-size: 22pt; line-height: 1; color: #242478; }
.cifra span { font-size: 9.2pt; color: #3A4050; }
.portada .pie { position: absolute; bottom: 0; left: 0; right: 0; font-size: 9.6pt; color: #3A4050; }
.portada .pie p { text-align: left; margin: 0 0 2pt 0; }
/* títulos */
.cap { border-left: 7px solid var(--c); padding: 1mm 0 1mm 6mm; margin: 0 0 5mm 0; }
.cap .num { font-size: 9pt; color: var(--c); text-transform: uppercase; letter-spacing: .12em;
            font-weight: 700; }
.cap h2 { font-size: 22pt; color: var(--c); margin-top: 1mm; }
.cap .bajada { font-size: 10pt; color: #3A4050; margin-top: 1.5mm; }
h3.sec { font-size: 13.5pt; color: #242478; margin: 5mm 0 2.5mm 0; break-after: avoid; }
h3.mis { font-size: 12.5pt; color: var(--c); margin: 5mm 0 2.5mm 0; break-after: avoid; }
h4 { font-size: 11pt; color: #1E2230; margin: 3.5mm 0 1.5mm 0; break-after: avoid; }
/* tablas sin reglas: filas alternas */
table { border-collapse: collapse; width: 100%; font-size: 9.6pt; }
th { text-align: left; font-size: 8pt; text-transform: uppercase; letter-spacing: .06em;
     color: #3A4050; padding: 2.2mm 2mm; background: #E6E8EF; }
td { padding: 1.9mm 2mm; vertical-align: top; text-align: left; }
tr { break-inside: avoid; }
tbody tr:nth-child(odd) td { background: #F6F7FA; }
td.n, th.n { text-align: right; font-variant-numeric: tabular-nums; width: 13mm; }
tr.total td { font-weight: 700; background: #E6E8EF !important; }
.punto { display: inline-block; width: 3mm; height: 3mm; border-radius: 50%; margin-right: 2mm;
         vertical-align: -0.2mm; }
/* tarjetas de hallazgo */
.h { border-left: 4px solid var(--s); background: #F7F8FA; padding: 2.6mm 4mm 1.4mm 4.2mm;
     margin: 0 0 3mm 0; break-inside: avoid; }
.h .cab { display: flex; flex-wrap: wrap; align-items: baseline; gap: 2.5mm; margin-bottom: 1.6mm; }
.h .donde { font-weight: 700; font-size: 10.6pt; }
.h .pag { color: #3A4050; font-size: 9.6pt; }
.h .reg { margin-left: auto; color: #6E7480; font-size: 8.4pt; }
.chip { display: inline-block; font-size: 7.6pt; font-weight: 700; text-transform: uppercase;
        letter-spacing: .07em; padding: .5mm 2.2mm .4mm 2.2mm; border-radius: 3mm; color: #fff;
        background: var(--s); }
.chip.c { background: #fff; color: #1F6B2E; box-shadow: inset 0 0 0 1.2px #1F6B2E; }
.chip.a { background: #fff; color: #4A5060; box-shadow: inset 0 0 0 1.1px #8A90A0; }
.h .lab { font-weight: 700; color: #3A4050; }
.h p { margin-bottom: 1.6mm; }
/* atención: lista breve */
.at { padding: 1.3mm 0 1.3mm 3.4mm; border-left: 2.5px solid var(--c); margin: 0 0 1.7mm 0;
      break-inside: avoid; font-size: 9.4pt; line-height: 1.32; }
.at .donde { font-weight: 700; }
.at p { margin: 0; }
.at .prop { color: #3A4050; }
.nota { background: #F3F4F8; border-left: 4px solid #242478; padding: 3mm 4.5mm 1mm 4.5mm;
        margin: 3mm 0 4mm 0; break-inside: avoid; }
.nota.oro { border-left-color: #C9821B; background: #FBF6EC; }
ol.pide { margin: 0 0 3mm 0; padding-left: 6mm; }
ol.pide li { margin-bottom: 1.6mm; text-align: justify; }
.url { font-family: 'Space Mono', monospace; font-size: 7.9pt; word-break: break-all; color: #1E2230; }
.leyenda { display: flex; flex-wrap: wrap; gap: 3mm 6mm; font-size: 9.4pt; margin: 2mm 0 3mm 0; }
.leyenda div { flex: 1 1 45%; }
.dos { display: flex; gap: 6mm; }
.dos > div { flex: 1; }
"""


def chip_sev(s):
    nombre = {"Considerar": "Para considerar"}.get(s, s)
    return f'<span class="chip" style="--s:{SEV_COLOR[s]}">{e(nombre)}</span>'


def chip_cuad(c):
    if c == "C":
        return '<span class="chip c">Corrección EDUCATE en el cuaderno</span>'
    if c == "A":
        return '<span class="chip a">Advertido en el cuaderno</span>'
    if c == "G":
        return '<span class="chip a">Advertido en el planeador y la guía</span>'
    return ""


def tarjeta(x):
    s = x["sev"]
    return (f'<div class="h" style="--s:{SEV_COLOR[s]}"><div class="cab">'
            f'<span class="donde">{e(x["preg"])}</span>'
            + (f'<span class="pag">{e(pag_txt(x["pag"]))} del libro</span>' if x["pag"] not in ("", "—") else "")
            + f'{chip_sev(s)}{chip_cuad(x["c"])}<span class="reg">Reg. {x["n"]}</span></div>'
            f'<p><span class="lab">Qué pasa.</span> {e(x["q"])}</p>'
            f'<p><span class="lab">Propuesta de EDUCATE.</span> {e(x["p"])}</p></div>')


def linea_at(x, color):
    m = mision_txt(x["mision"])
    c = {"C": " · corrección EDUCATE en el cuaderno", "A": " · advertido en el cuaderno",
         "G": " · advertido en el planeador y la guía"}.get(x["c"], "")
    return (f'<div class="at" style="--c:{color}"><p><span class="donde">{e(m)} · {e(x["preg"])}</span> '
            f'· {e(pag_txt(x["pag"]))}{c} · <span style="color:#6E7480">Reg. {x["n"]}</span></p>'
            f'<p>{e(x["q"])} <span class="prop"><b>Propuesta:</b> {e(x["p"])}</span></p></div>')


def html_doc(titulo, cuerpo):
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{e(titulo)}</title>'
            f'<style>{CSS}</style></head><body>{cuerpo}</body></html>')


PIE = ('<div style="width:100%;font-family:Carlito,sans-serif;font-size:7.6pt;color:#5B6170;'
       'padding:0 19mm;display:flex;justify-content:space-between;">'
       '<span>EDUCATE · Para el Saber</span><span>{titulo}</span>'
       '<span><span class="pageNumber"></span> de <span class="totalPages"></span></span></div>')


def a_pdf(html_txt, pdf, titulo, portada_sin_pie=True):
    hp = os.path.join(TMP, os.path.basename(pdf).replace(".pdf", ".html"))
    with open(hp, "w", encoding="utf-8") as f:
        f.write(html_txt)
    js = os.path.join(TMP, "a_pdf.js")
    with open(js, "w") as f:
        f.write("""
const { chromium } = require('playwright');
(async () => {
  const [,, src, out, pie] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto('file://' + src, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: out, format: 'Letter', printBackground: true, preferCSSPageSize: true,
                displayHeaderFooter: true, headerTemplate: '<div></div>', footerTemplate: pie });
  await b.close();
})();
""")
    env = dict(os.environ, NODE_PATH="/opt/node22/lib/node_modules")
    tmp_pdf = pdf + ".tmp.pdf"
    subprocess.run(["node", js, hp, tmp_pdf, PIE.format(titulo=e(titulo))], check=True, env=env)
    # la portada va sin pie: se reemplaza la página 1 por la misma página sin pie
    if portada_sin_pie:
        import pikepdf
        js2 = js.replace(".js", "_sinpie.js")
        with open(js2, "w") as f:
            f.write(open(js).read().replace("displayHeaderFooter: true", "displayHeaderFooter: false"))
        tmp2 = pdf + ".tmp2.pdf"
        subprocess.run(["node", js2, hp, tmp2, ""], check=True, env=env)
        con, sin = pikepdf.open(tmp_pdf), pikepdf.open(tmp2)
        out = pikepdf.new()
        out.pages.append(sin.pages[0])
        for pg in con.pages[1:]:
            out.pages.append(pg)
        out.docinfo["/Title"] = titulo
        out.docinfo["/Author"] = "EDUCATE · Para el Saber"
        out.save(pdf)
        con.close(); sin.close()
        os.remove(tmp2)
        os.remove(tmp_pdf)
    else:
        os.replace(tmp_pdf, pdf)
    return hp


# ─────────── informe para la editorial ───────────
def informe(tab):
    logo = logo_data()
    principales = [x for x in H if x["sev"] in SEV]
    atencion = [x for x in H if x["sev"] == "Atención"]
    considerar = [x for x in H if x["sev"] == "Considerar"]
    cnt = Counter((x["area"], x["sev"]) for x in H)
    n_corr = sum(1 for x in H if x["c"] == "C")
    n_adv = sum(1 for x in H if x["c"] == "A")
    altas = [x for x in H if x["sev"] == "Alta"]
    preg_total = sum(PREGUNTAS.values())
    filas_rep = len(set(n for x in H for n in [x["n"]]) | set(r[4] for r in REPARTO)
                    | set(i[4] for i in ICFES) | set(MARCA_AGUA))

    o = []
    # portada
    o.append(f'''<section class="portada">
<img class="logo" src="{logo}" alt="EDUCATE">
<div class="bloque"><h1>Informe de hallazgos<br>del libro Misión Saber 11</h1>
<div class="sub">Para la editorial · revisión pregunta por pregunta de las siete áreas</div>
<div class="fecha">Versión del 10 de noviembre de 2026 · reemplaza el informe del 6 de noviembre</div></div>
<div class="cifras">
<div class="cifra"><b>{preg_total}</b><span>preguntas de las Pruebas de Campo resueltas una por una</span></div>
<div class="cifra"><b>{len(principales)}</b><span>hallazgos que piden revisión ({len(altas)} de severidad alta)</span></div>
<div class="cifra"><b>{len(atencion)}</b><span>puntos de atención y {len(considerar)} temas para considerar</span></div>
<div class="cifra"><b>{len(ICFES)}</b><span>observaciones sobre las fuentes ICFES (informativas)</span></div>
</div>
<div class="pie"><p><b>EDUCATE · Para el Saber</b></p>
<p>Preparado por Nelson González, asesor comercial y pedagógico.</p>
<p>Documento de trabajo para la conversación con la editorial. Acompaña al archivo hallazgos_editorial.csv, con la misma información en tabla.</p></div>
</section>''')

    # presentación y resumen
    o.append('<section class="salto">')
    o.append('<div class="cap" style="--c:#242478"><div class="num">Presentación</div><h2>Por qué existe este informe</h2></div>')
    o.append(
        f'<p>EDUCATE construye sobre el libro Misión Saber 11 un cuaderno de trabajo para el estudiante, de '
        f'398 páginas, con sus planeadores para el docente y sus guías de clase. Cada pregunta del cuaderno '
        f'lleva un instrumento de pensamiento que se diseña a partir de cómo se llega a la respuesta, y por eso '
        f'no bastó con transcribir: fue necesario resolver las {preg_total} preguntas de las Pruebas de Campo '
        f'de las siete áreas (seis misiones por área), contrastar cada opción con el enunciado y, donde hay '
        f'figuras o tablas, medirlas.</p>')
    o.append(
        '<p>En ese trabajo aparecieron claves discutibles, erratas, figuras que no coinciden con el texto, '
        'datos por verificar y algunos patrones en la forma de las opciones. Todo quedó registrado. Este '
        'informe recoge lo que concierne al libro, con la página, lo que se observó (con la cita literal '
        'cuando la hay), lo que EDUCATE propone y si el cuaderno ya lo corrige o lo advierte. Lo compartimos '
        'como aliados: el propósito común es que el estudiante tenga en las manos un material sin tropiezos, '
        'y la editorial es quien puede llevar estas mejoras a la próxima edición.</p>')
    o.append(
        '<p>Las claves que aquí se mencionan son las que EDUCATE obtuvo resolviendo cada pregunta; no se '
        'contrastaron con un solucionario de la editorial. Donde decimos «EDUCATE propone» es porque hay más '
        'de una lectura posible y nos gustaría conocer la clave que la editorial tiene prevista.</p>')

    # tabla resumen
    o.append('<h3 class="sec">Resumen por área y severidad</h3>')
    o.append('<table><thead><tr><th>Área</th><th class="n">Preguntas</th><th class="n">Alta</th>'
             '<th class="n">Media</th><th class="n">Baja</th><th class="n">Subtotal</th>'
             '<th class="n">Atención</th><th class="n">Para considerar</th>'
             '<th class="n">Corrección EDUCATE</th></tr></thead><tbody>')
    tot = Counter()
    for k, (nom, col) in AREAS.items():
        a, m, b = cnt[(k, "Alta")], cnt[(k, "Media")], cnt[(k, "Baja")]
        at, co = cnt[(k, "Atención")], cnt[(k, "Considerar")]
        cc = sum(1 for x in H if x["area"] == k and x["c"] == "C")
        for kk, v in (("p", PREGUNTAS[k]), ("a", a), ("m", m), ("b", b), ("s", a + m + b), ("at", at),
                      ("co", co), ("cc", cc)):
            tot[kk] += v
        o.append(f'<tr><td><span class="punto" style="background:{col}"></span>{e(nom)}</td>'
                 f'<td class="n">{PREGUNTAS[k]}</td><td class="n">{a}</td><td class="n">{m}</td>'
                 f'<td class="n">{b}</td><td class="n"><b>{a + m + b}</b></td><td class="n">{at}</td>'
                 f'<td class="n">{co or "—"}</td><td class="n">{cc or "—"}</td></tr>')
    o.append(f'<tr class="total"><td>Total</td><td class="n">{tot["p"]}</td><td class="n">{tot["a"]}</td>'
             f'<td class="n">{tot["m"]}</td><td class="n">{tot["b"]}</td><td class="n">{tot["s"]}</td>'
             f'<td class="n">{tot["at"]}</td><td class="n">{tot["co"]}</td><td class="n">{tot["cc"]}</td></tr>')
    o.append('</tbody></table>')
    o.append(
        f'<p style="margin-top:3mm">De los {len(principales)} hallazgos que piden revisión, {n_corr} ya van '
        f'resueltos en el cuaderno con una «Corrección EDUCATE» impresa en la tarjeta de la pregunta (todos de '
        f'Inglés), y en {sum(1 for x in principales if x["c"] == "A")} más el cuaderno advierte el problema al '
        f'estudiante o al docente con un recuadro o un sello, sin cambiar el libro. Aparte, el informe trae '
        f'{len(ICFES)} observaciones sobre las fuentes ICFES y una sección sobre indicios de contenido generado '
        f'automáticamente. En total, el informe recoge {filas_rep} registros del tablero de EDUCATE; cada '
        f'hallazgo lleva su número de registro («Reg.») para facilitar la conversación.</p>')
    o.append('</section>')

    # escala y lo que se pide
    o.append('<section class="salto">')
    o.append('<div class="cap" style="--c:#242478"><div class="num">Cómo leer el informe</div><h2>Severidades y lo que se le pide a la editorial</h2></div>')
    o.append('<div class="leyenda">'
             f'<div>{chip_sev("Alta")} Ninguna opción es correcta, hay dos correctas o la clave contradice el enunciado o la figura. El estudiante que razona bien no llega a la respuesta esperada.</div>'
             f'<div>{chip_sev("Media")} Dos opciones defendibles, una clave imprecisa, una figura o un dato que contradice el texto, o un patrón que permite acertar sin leer.</div>'
             f'<div>{chip_sev("Baja")} Erratas, redacciones imprecisas o referencias incompletas que no cambian la clave.</div>'
             f'<div>{chip_sev("Atención")} Observaciones que no exigen corrección pero conviene conocer: patrones de claves, preguntas repetidas, redacciones mejorables. Van en una sección aparte.</div>'
             f'<div>{chip_sev("Considerar")} Contenido de actualidad política o con marcas reales. No es un error: es un dato para que la editorial lo valore.</div>'
             f'<div>{chip_cuad("C")} El cuaderno imprime la corrección en la tarjeta. {chip_cuad("A")} El cuaderno avisa con un recuadro, un sello o el propio instrumento. {chip_cuad("G")} El aviso va al docente.</div>'
             '</div>')
    o.append('<h3 class="sec">Lo que EDUCATE le pide a la editorial</h3><ol class="pide">')
    lista_altas = "; ".join(f'{AREAS[x["area"]][0]} {mision_txt(x["mision"])}, {x["preg"][0].lower() + x["preg"][1:]} ({pag_txt(x["pag"])})'
                            for x in sorted(altas, key=lambda y: (list(AREAS).index(y["area"]), y["mision"])))
    o.append(f'<li><b>Revisar las {len(altas)} preguntas de severidad alta</b> y confirmar o corregir su clave: {e(lista_altas)}.</li>')
    o.append('<li><b>Confirmar la clave</b> donde EDUCATE tuvo que escoger entre dos lecturas (las tarjetas que dicen «EDUCATE propone»), para que el cuaderno, el planeador y las guías coincidan con el solucionario de la editorial.</li>')
    o.append('<li><b>Corregir en la próxima impresión</b> las erratas, figuras y datos señalados como media o baja, en especial las figuras de Física y Química que muestran fuerzas, rayos o moléculas mal dibujados.</li>')
    o.append('<li><b>Revisar el reparto y la forma de las opciones</b> en las misiones donde una letra concentra la mitad de las claves o donde la correcta se reconoce por su forma (la más larga, la única sin absolutos, la única que empieza por «Yes»).</li>')
    o.append('<li><b>Verificar datos, fechas y fuentes</b> que el informe marca como no comprobados, y limpiar las cuatro URL que traen el parámetro «utm_source=chatgpt.com».</li>')
    o.append('<li><b>Confirmar si los archivos que tiene EDUCATE son la versión final del libro.</b> Todas las páginas recibidas llevan la marca de agua «MATERIAL PARA REVISIÓN». Si existe una versión posterior, agradecemos recibirla para cotejar este informe.</li>')
    o.append('<li><b>Valorar</b> los textos de actualidad política y con marcas reales que se listan en la sección «Para considerar».</li></ol>')
    o.append('<div class="nota"><p><b>Una aclaración sobre el cuaderno.</b> El cuaderno no esconde estas preguntas. En los casos de fondo, el instrumento lleva al estudiante a calcular o a comprobar por su cuenta, y el docente recibe en el planeador y en la guía el aviso correspondiente. Así el error queda a la vista en la clase, en lugar de que el estudiante marque al azar y arrastre la duda hasta el examen. Solo en Inglés, donde el error impedía resolver la pregunta o enseñaba una forma incorrecta, el cuaderno imprime una «Corrección EDUCATE».</p></div>')
    o.append('</section>')

    # capítulos por área
    for i, (k, (nom, col)) in enumerate(AREAS.items(), 1):
        xs = [x for x in principales if x["area"] == k]
        a, m, b = (sum(1 for x in xs if x["sev"] == s) for s in SEV)
        nat = cnt[(k, "Atención")]
        nco = cnt[(k, "Considerar")]
        partes = []
        if nat:
            partes.append(f'{nat} punto de atención va en la sección aparte' if nat == 1 else
                          f'{nat} puntos de atención van en la sección aparte')
        if nco:
            partes.append(f'{nco} tema va en «Para considerar»' if nco == 1 else
                          f'{nco} temas van en «Para considerar»')
        extra = (" " + " y ".join(partes) + ".") if partes else ""
        o.append(f'<section class="salto" style="--c:{col}"><div class="cap" style="--c:{col}">'
                 f'<div class="num">Capítulo {i}</div><h2>{e(nom)}</h2>'
                 f'<div class="bajada">{len(xs)} hallazgos: {a} de severidad alta, {m} media y {b} baja.{e(extra)}</div></div>')
        por_m = OrderedDict()
        for x in sorted(xs, key=lambda y: (y["mision"], SEV.index(y["sev"]))):
            por_m.setdefault(x["mision"], []).append(x)
        for mi, ys in por_m.items():
            o.append(f'<h3 class="mis" style="--c:{col}">{e(mision_txt(mi))}</h3>')
            o.extend(tarjeta(y) for y in ys)
        o.append('</section>')

    # atención
    o.append('<section class="salto"><div class="cap" style="--c:#30843C"><div class="num">Sección aparte</div>'
             '<h2>Puntos de atención</h2><div class="bajada">Observaciones que no exigen corrección, en forma breve, '
             'y el reparto de claves de cada misión.</div></div>')
    o.append('<h3 class="sec">Reparto de claves por misión</h3>')
    o.append('<p>El reparto se contó con las claves que EDUCATE obtuvo al resolver. Se marca cuando una letra '
             'concentra la mitad de las claves, cuando una letra no aparece o cuando las claves siguen un orden '
             'reconocible. Matemáticas no presentó concentraciones dignas de nota y en Física Misión 4 no se '
             'registró el reparto.</p>')
    o.append('<table><thead><tr><th style="width:27%">Área</th><th style="width:9%">Misión</th><th style="width:27%">Reparto</th><th>Observación</th><th class="n">Reg.</th></tr></thead><tbody>')
    for (k, mi, rep, obs, n) in REPARTO:
        o.append(f'<tr><td><span class="punto" style="background:{AREAS[k][1]}"></span>{e(AREAS[k][0])}</td>'
                 f'<td>{e(mi)}</td><td>{e(rep)}</td><td>{e(obs)}</td><td class="n">{n}</td></tr>')
    o.append('</tbody></table>')
    for k, (nom, col) in AREAS.items():
        ys = sorted([x for x in atencion if x["area"] == k], key=lambda y: (y["mision"], y["n"]))
        if not ys:
            continue
        o.append(f'<h3 class="mis" style="--c:{col}">{e(nom)}</h3>')
        o.extend(linea_at(y, col) for y in ys)
    o.append('</section>')

    # para considerar
    o.append('<section class="salto"><div class="cap" style="--c:#6E7480"><div class="num">Para considerar</div>'
             '<h2>Contenido de actualidad política y marcas reales</h2></div>')
    o.append('<p>Los textos que siguen no tienen un error de contenido, salvo el de la condena que se cita al '
             'final, cuyo estado judicial pudo cambiar. Se listan porque nombran a figuras políticas de la '
             'actualidad, tratan hechos recientes y polarizantes o atribuyen prácticas a una empresa real. Son un '
             'dato para que la editorial valore, con su propio criterio, si conviene mantenerlos en una nueva '
             'edición de un material escolar.</p>')
    previo = None
    for x in sorted(considerar, key=lambda y: (list(AREAS).index(y["area"]), y["mision"])):
        cab = f'{AREAS[x["area"]][0]} · {mision_txt(x["mision"])}'
        if cab != previo:
            o.append(f'<h4>{e(cab)}</h4>')
            previo = cab
        o.append(tarjeta(x))
    o.append('</section>')

    # fuentes ICFES
    o.append('<section class="salto"><div class="cap" style="--c:#242478"><div class="num">Informativo</div>'
             '<h2>Las fuentes ICFES</h2><div class="bajada">Erratas y claves dudosas en los cuadernillos oficiales y en el SIMULACRO II 2023.</div></div>')
    o.append('<p>Las páginas de entrenamiento del cuaderno usan preguntas reales del ICFES, tomadas de los '
             'cuadernillos liberados y del SIMULACRO II 2023. Al resolverlas también aparecieron erratas y algunas '
             'claves dudosas. Esta sección es solo informativa: no son responsabilidad de la editorial, pero le '
             'pueden servir si el libro usa los mismos cuadernillos. La observación de mayor peso es la clave '
             'oficial errada de la pregunta 21 del Examen 2 de Inglés 2024.</p>')
    o.append('<table><thead><tr><th style="width:30%">Fuente e ítem</th><th>Qué pasa</th><th style="width:19%">Efecto</th><th class="n">Reg.</th></tr></thead><tbody>')
    for (fu, it, q, ef, n) in ICFES:
        o.append(f'<tr><td><b>{e(fu)}</b><br>{e(it)}</td><td>{e(q)}</td>'
                 f'<td>{e(ef)}</td><td class="n">{n}</td></tr>')
    o.append('</tbody></table></section>')

    # indicios
    o.append(seccion_indicios(tab))

    # cierre
    o.append('<section style="margin-top:6mm"><div class="nota oro"><p><b>Para seguir.</b> EDUCATE queda atento a '
             'la respuesta de la editorial sobre las claves y sobre la versión del libro. Si la editorial lo '
             'prefiere, podemos revisar juntos las preguntas de severidad alta en una sesión de trabajo, con el '
             'cuaderno y el libro a la vista. Agradecemos de antemano la disposición: el objetivo es común.</p></div></section>')
    return html_doc("Informe de hallazgos del libro Misión Saber 11", "".join(o))


URLS = [
    ("Sociales y Ciudadanas", "Misión 2", "347", "Texto de la pregunta 2 (reforma fiscal)",
     "https://www.lanacion.com.ar/agencias/colombia-contempla-presentar-a-congreso-reforma-fiscal-por-26-billones-de-pesos-para-financiar-nid16072025/?utm_source=chatgpt.com"),
    ("Sociales y Ciudadanas", "Misión 2", "348", "Fuente 1 del texto de las preguntas 4 a 6",
     "https://www.bluradio.com/nacion/aqui-defendiendo-la-democracia-maestro-la-frase-que-marco-al-coronel-plazas?utm_source=chatgpt.com"),
    ("Sociales y Ciudadanas", "Misión 2", "348", "Fuente 2 del texto de las preguntas 4 a 6",
     "https://www.elespectador.com/judicial/las-pruebas-contra-el-coronel-article-4533/?utm_source=chatgpt.com"),
    ("Sociales y Ciudadanas", "Misión 5", "384", "Texto de las preguntas 5 a 7",
     "https://www.eltiempo.com/bogota/indigenas-intentan-asentarse-otra-vez-en-el-parque-nacional-esto-es-lo-que-se-sabe-3455105?utm_source=chatgpt.com"),
]


def seccion_indicios(tab):
    o = ['<section class="salto"><div class="cap" style="--c:#242478"><div class="num">Sección delicada</div>'
         '<h2>Indicios de contenido generado automáticamente</h2></div>']
    o.append('<p>Esta sección reúne hechos observados en los archivos que recibió EDUCATE. Ninguno, por sí solo, '
             'permite concluir cómo se elaboró el libro, y no es nuestra intención afirmarlo. Los compartimos '
             'porque, vistos juntos, sugieren que algunas partes pudieron redactarse o ilustrarse con ayuda de '
             'herramientas de inteligencia artificial y no pasaron por una revisión final. La editorial está en la '
             'mejor posición para valorarlos.</p>')
    o.append('<h3 class="sec">1. Enlaces con el parámetro «utm_source=chatgpt.com»</h3>')
    o.append('<p>Cuatro URL de las fuentes citadas en el libro terminan en «?utm_source=chatgpt.com», el '
             'parámetro que la herramienta ChatGPT añade a los enlaces que muestra en sus respuestas. Se '
             'localizaron extrayendo el texto de los 42 archivos de Prueba de Campo con pdftotext. Las URL se '
             'transcriben tal como aparecen impresas, uniendo los cortes de línea. (En registros anteriores de '
             'EDUCATE se hablaba de tres; la búsqueda completa encontró cuatro.)</p>')
    o.append('<table><thead><tr><th style="width:17%">Área y misión</th><th class="n" style="width:9%">Página</th><th style="width:22%">Ubicación</th><th>URL impresa</th></tr></thead><tbody>')
    for (a, m, p, u, url) in URLS:
        o.append(f'<tr><td>{e(a)}<br>{e(m)}</td><td class="n">{p}</td><td>{e(u)}</td><td class="url">{e(url)}</td></tr>')
    o.append('</tbody></table>')
    o.append('<h3 class="sec">2. La observación de un revisor externo</h3>')
    o.append('<p>Seis docentes revisaron el libro por encargo de EDUCATE, cada uno en su área. El revisor de '
             'Ciencias Sociales de grado 11 anotó que las respuestas correctas son, por lo general, las de mayor '
             'número de caracteres, y lo marcó textualmente como «(patrón IA)». Al resolver las preguntas, EDUCATE '
             'encontró el mismo rasgo de forma independiente, y no solo en Sociales.</p>')
    o.append('<h3 class="sec">3. Patrones en el reparto y la forma de las claves</h3>')
    o.append('<p>Los siguientes patrones permiten acertar sin leer el texto. Son frecuentes en material generado '
             'de manera automática, aunque también pueden deberse a una plantilla de redacción:</p><ol class="pide">')
    o.append('<li><b>Claves en orden alfabético.</b> Inglés, Misión 1, Parte 1 (p. 414): grupo 1, C A B H D E F; grupo 2, B A C D E F G (Reg. 260).</li>')
    o.append('<li><b>La correcta es la única que empieza por «Yes».</b> Inglés, Misión 2 (pp. 424–425): en 7 de 10 preguntas, y ninguna distractora empieza así (Reg. 271).</li>')
    o.append('<li><b>La correcta es la única que matiza.</b> Inglés, Misión 5 (pp. 457–459): los distractores cierran con absolutos («exclusively», «completely», «all») (Reg. 302); el Bloque 1 repite la secuencia C A D B (Reg. 303). Sociales, misiones 3 a 6 (pp. 359–402): la correcta es la que «integra» o dice «X pero también Y» y las demás traen «únicamente», «garantiza», «nunca» (Reg. 48, 61, 71, 89).</li>')
    o.append('<li><b>La correcta es la más larga.</b> Sociales M4 y M5, Biología M5 y M6, Química M5 (Reg. 61, 71, 139, 147, 198).</li>')
    o.append('<li><b>Una letra concentra la mitad de las claves.</b> Lectura Crítica M3, M5 y M6; Sociales M3 y M4; Biología M4; Física M3 (ver la tabla de reparto en «Puntos de atención»).</li></ol>')
    o.append('<h3 class="sec">4. Ilustraciones con apariencia de imagen generada</h3>')
    o.append('<p>En Inglés, Misión 2 (pp. 424–425), las ilustraciones de las conversaciones comparten el mismo '
             'trazo y llevan texto incrustado dentro del dibujo: la de la pregunta 2 repite el enunciado dentro de '
             'la imagen y la de la pregunta 8 muestra el logotipo de Facebook (Reg. 274). Los créditos de imagen de '
             'las misiones 5 y 6 dicen «This Photo by Unknown Author is licensed under CC BY-SA-NC», con una '
             'licencia escrita en un orden que no existe (Reg. 305 y 329). Conviene confirmar el origen y la '
             'licencia de las ilustraciones.</p>')
    o.append('<h3 class="sec">5. La marca de agua «MATERIAL PARA REVISIÓN»</h3>')
    o.append('<p>Todas las páginas de los 42 archivos de Prueba de Campo que recibió EDUCATE (seis misiones de '
             'siete áreas) llevan atravesada la marca de agua «MATERIAL PARA REVISIÓN» (Reg. 119, 128, 178 y 188 '
             'la anotan en Biología y Química; se comprobó en las siete áreas). Varias pruebas empiezan con restos '
             'de la página anterior del libro (Biología p. 72, Química p. 193, Física p. 259), y en Biología M5 la '
             'pregunta 6 se refiere a un texto que no está antes de ella.</p>')
    o.append('<div class="nota oro"><p><b>Lo que pedimos.</b> Que la editorial confirme si la versión que tiene '
             'EDUCATE es la versión final del libro. Si hay una versión posterior, agradecemos recibirla: varios '
             'de los hallazgos de este informe podrían estar ya corregidos, y EDUCATE ajustaría el cuaderno antes '
             'de imprimir.</p></div>')
    o.append('</section>')
    return "".join(o)


# ─────────── documento interno ───────────
def interno(tab):
    o = []
    o.append(f'<section><img src="{logo_data()}" style="width:32mm" alt="EDUCATE">'
             '<div class="cap" style="--c:#A82424;margin-top:6mm"><div class="num">Documento interno · para Nelson y Cristian</div>'
             '<h2>Hallazgos internos de EDUCATE</h2><div class="bajada">Versión del 10 de noviembre de 2026 · '
             'errores del propio material y filas que no van a la editorial</div></div>')
    estados = Counter()
    for n in NUESTRO + PROPIOS:
        r = tab[n]
        abierto = n in (21, 40, 41, 43, 336, 337, 338, 339, 340, 346)
        estados["abiertos" if abierto else "cerrados"] += 1
    o.append(f'<p>El tablero tiene {len(tab)} registros. {len(NUESTRO)} llevan el rótulo «Nuestro…»: son errores '
             f'del cuaderno, de las guías o del motor, y no se envían a la editorial. Se suman aquí {len(PROPIOS)} '
             f'filas que también son del material de EDUCATE aunque no lleven el rótulo. De las '
             f'{len(NUESTRO) + len(PROPIOS)}, {estados["cerrados"]} están corregidas y {estados["abiertos"]} siguen '
             f'abiertas o por verificar.</p>')
    o.append('<h3 class="sec">Lo que sigue abierto</h3><ol class="pide">')
    o.append('<li><b>Nombres de políticos (Reg. 21).</b> Decisión de Cristian antes de imprimir. El informe para la editorial presenta esos textos solo como dato para que la editorial los considere.</li>')
    o.append('<li><b>Líneas horizontales de la cabecera y el pie (Reg. 40, 339, 346).</b> Se quitan con el estilo B; falta verificar las páginas finales.</li>')
    o.append('<li><b>Apertura (Reg. 41, 43).</b> Verificar en la apertura del estilo B el ejemplo de membrete con año y el texto montado sobre el círculo.</li>')
    o.append('<li><b>Planeador y guías (Reg. 336, 337, 338, 340).</b> Artículo 214 en TEXTOS_GUIA_DOCENTE.md, «Charly García», competencia de 8 ICFES de Sociales y numeración de estrategias de Matemáticas M6.</li></ol>')
    o.append('<table><thead><tr><th class="n">Reg.</th><th style="width:47%">Dónde y qué pasó</th><th>Qué se hizo</th><th style="width:14%">Estado</th></tr></thead><tbody>')
    for n in NUESTRO + PROPIOS:
        r = tab[n]
        o.append(f'<tr><td class="n">{n}</td><td><b>{e(r["ubicacion"])}</b><br>{e(r["que_pasa"])}</td>'
                 f'<td>{e(ACCION.get(n, r["efecto"]))}</td><td>{e(r["estado"])} · {e(r["severidad"])}</td></tr>')
    o.append('</tbody></table></section>')

    o.append('<section class="salto"><h3 class="sec">Filas de gestión interna (fuentes ICFES, ASED, reservas)</h3>')
    o.append('<p>No son errores del libro ni del cuaderno: son decisiones y controles de EDUCATE sobre las preguntas '
             'del entrenamiento. No van a la editorial. Las del ASED, en particular, no se mencionan en el informe '
             'externo.</p>')
    o.append('<table><thead><tr><th class="n">Reg.</th><th style="width:28%">Dónde</th><th>Nota</th><th style="width:16%">Estado</th></tr></thead><tbody>')
    for n in GESTION:
        r = tab[n]
        o.append(f'<tr><td class="n">{n}</td><td>{e(r["ubicacion"])}</td><td>{e(GESTION_NOTA[n])}</td><td>{e(r["estado"])}</td></tr>')
    o.append('</tbody></table>')
    o.append('<h3 class="sec">Filas del libro que no se enviaron a la editorial</h3>')
    o.append('<table><thead><tr><th class="n">Reg.</th><th style="width:30%">Dónde</th><th>Razón</th></tr></thead><tbody>')
    for n, why in NO_ENVIADAS.items():
        o.append(f'<tr><td class="n">{n}</td><td>{e(tab[n]["ubicacion"])}</td><td>{e(why)}</td></tr>')
    o.append('</tbody></table>')
    o.append('<h3 class="sec">Diferencias entre el tablero y el informe</h3><ol class="pide">')
    o.append('<li><b>Matemáticas M6 pregunta 2 (Reg. 8):</b> el tablero dice Media y la fila 343 la cuenta como Alta. El informe usa Alta: el valor impreso de la clave no coincide con la cuenta, así que ninguna opción trae el resultado correcto.</li>')
    o.append('<li><b>Matemáticas M4·1 y M6·10 (Reg. 7 y 9):</b> el tablero dice Atención y la fila 342 dice Media. El informe usa Media.</li>')
    o.append('<li><b>Reg. 341</b> dice «Misión 6 · ICFES P3», pero es la pregunta 3 del taller (libro p. 326), no una pregunta ICFES. En el informe va como Matemáticas M6, pregunta 3.</li>')
    o.append('<li><b>URL con «utm_source=chatgpt.com» (Reg. 31 y 74):</b> CLAUDE.md habla de tres; son cuatro (tres en Sociales M2 y una en Sociales M5). El tablero las tenía con severidades distintas (Atención y Media); en el informe las dos van como Baja.</li>')
    o.append('<li><b>«Final de lA Misión» (Reg. 68, 80, 286, 306, 329):</b> la mayúscula solo existe en la capa de texto; impreso no se ve. Se retiró del informe.</li>')
    o.append('<li><b>Reg. 157 y 167:</b> siguen «Pendiente de decisión», pero la decisión del 7 nov ya acepta el SIMULACRO II como oficial. Conviene cerrarlas.</li>')
    o.append('<li><b>Política en el tablero:</b> las filas 20, 44, 83 y 84 tienen severidad Alta por el riesgo político, no por un error de contenido. En el informe van en «Para considerar», sin severidad, igual que 32, 45 y 77.</li>')
    o.append('</ol></section>')
    return html_doc("Hallazgos internos de EDUCATE", "".join(o))


# ─────────── CSV para la editorial ───────────
def csv_editorial(path):
    cols = ["reg_tablero", "seccion", "area", "mision", "preguntas", "pagina_libro", "severidad",
            "que_pasa", "propuesta_educate", "estado_en_el_cuaderno"]
    est = {"C": "Corrección EDUCATE en el cuaderno", "A": "Advertido en el cuaderno",
           "G": "Advertido en el planeador y la guía del docente", "": "Sin intervención"}
    filas = []
    orden = {k: i for i, k in enumerate(AREAS)}
    sev_o = {"Alta": 0, "Media": 1, "Baja": 2, "Atención": 3, "Considerar": 4}
    for x in sorted(H, key=lambda y: (sev_o[y["sev"]] >= 3, sev_o[y["sev"]] == 4, orden[y["area"]],
                                      y["mision"], sev_o[y["sev"]])):
        sec = {"Atención": "Punto de atención", "Considerar": "Para considerar"}.get(x["sev"], "Hallazgo")
        filas.append([x["n"], sec, AREAS[x["area"]][0], mision_txt(x["mision"]), x["preg"], x["pag"],
                      "Para considerar" if x["sev"] == "Considerar" else x["sev"], x["q"], x["p"], est[x["c"]]])
    for (k, mi, rep, obs, n) in REPARTO:
        filas.append([n, "Reparto de claves", AREAS[k][0], f"Misión {mi}", "Todas", "", "Atención",
                      f"Reparto: {rep}. {obs[0].upper() + obs[1:]}.", "Redistribuir si una letra concentra la mitad o falta.", ""])
    for (fu, it, q, ef, n) in ICFES:
        filas.append([n, "Fuente ICFES (informativo)", fu, "", it, "", "Informativo", q, ef, ""])
    for (a, m, p, u, url) in URLS:
        filas.append(["31" if m == "Misión 2" else "74", "Indicio", a, m, u, p, "Indicio",
                      f"URL con el parámetro utm_source=chatgpt.com: {url}", "Limpiar la URL y verificar la fuente.", ""])
    filas.append(["119 128 178 188", "Indicio", "Todas", "Todas", "Todas", "", "Indicio",
                  "Todas las páginas de los 42 archivos de Prueba de Campo llevan la marca de agua «MATERIAL PARA REVISIÓN».",
                  "Confirmar si la versión que tiene EDUCATE es la final.", ""])
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(cols)
        w.writerows(filas)
    return len(filas)


def contabilidad(tab):
    en_h = [x["n"] for x in H]
    rep = Counter(en_h)
    dobles = [n for n, c in rep.items() if c > 1]
    cubiertas = set(en_h) | set(r[4] for r in REPARTO) | set(i[4] for i in ICFES) | set(MARCA_AGUA) \
        | set(NUESTRO) | set(PROPIOS) | set(GESTION) | set(NO_ENVIADAS) | set(REPARTO_SOLO)
    faltan = sorted(set(tab) - cubiertas)
    nuestro_tab = sorted(n for n, r in tab.items() if r["ubicacion"].startswith("Nuestro"))
    assert nuestro_tab == sorted(NUESTRO), (nuestro_tab, NUESTRO)
    assert not (set(en_h) & (set(NUESTRO) | set(PROPIOS) | set(GESTION))), "fila interna en el informe"
    return dobles, faltan


def main():
    tab = leer_tablero()
    dobles, faltan = contabilidad(tab)
    print("filas dobles en H:", dobles, "· filas sin destino:", faltan)
    ent = os.path.join(RAIZ, "entregables")
    a_pdf(informe(tab), os.path.join(ent, "EDUCATE_Informe_hallazgos_editorial_10nov.pdf"),
          "Informe de hallazgos del libro Misión Saber 11 · 10 nov 2026")
    a_pdf(interno(tab), os.path.join(ent, "EDUCATE_Hallazgos_internos_10nov.pdf"),
          "Hallazgos internos · 10 nov 2026 · documento interno", portada_sin_pie=False)
    n = csv_editorial(os.path.join(RAIZ, "tablero", "hallazgos_editorial.csv"))
    c = Counter(x["sev"] for x in H)
    print("informe:", len(H), dict(c), "· filas csv:", n,
          "· corrección EDUCATE:", sum(1 for x in H if x["c"] == "C"))


if __name__ == "__main__":
    main()
