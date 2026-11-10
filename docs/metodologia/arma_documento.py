#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Arma el PDF del documento maestro de metodología desde su fuente en Markdown.

    python3 docs/metodologia/arma_documento.py

Fuente:  docs/metodologia/Documento_maestro_metodologia.md  (+ img/)
Salida:  entregables/EDUCATE_Documento_maestro_metodologia.pdf

Pasos: pandoc convierte el Markdown en HTML; este script le pone la portada, el índice y la
hoja de estilo (estilo B «Bitácora»: Shantell Sans y Space Mono en títulos, Carlito en el
texto, justificado con la fuente real por el navegador); Chromium (Playwright) lo imprime en
carta. Se imprime dos veces: la primera para saber en qué página cae cada sección y la segunda
con esos números en el índice.

Necesita: pandoc, node con playwright, pdftotext, y las fuentes Carlito, Shantell Sans y
Space Mono instaladas (CLAUDE.md § 4).
"""
import html
import os
import re
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.realpath(__file__))
RAIZ = os.path.normpath(os.path.join(AQUI, "..", ".."))
MD = os.path.join(AQUI, "Documento_maestro_metodologia.md")
PDF = os.path.join(RAIZ, "entregables", "EDUCATE_Documento_maestro_metodologia.pdf")
PLAYWRIGHT = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()

AREAS = [("Matemáticas", "#1F4E8C"), ("Lectura Crítica", "#A82424"), ("Sociales", "#C9821B"),
         ("Biología", "#30843C"), ("Química", "#0F7A68"), ("Física", "#5C7A1E"),
         ("Inglés", "#1BA0A8")]

CSS = r"""
@page { size: letter; margin: 19mm 21mm 20mm 21mm;
  @bottom-left { content: "EDUCATE · Documento maestro de metodología";
    font-family: "Space Mono"; font-size: 7.5pt; color: #6E7480; }
  @bottom-right { content: "p. " counter(page);
    font-family: "Space Mono"; font-size: 8pt; font-weight: 700; color: #242478; } }
@page :first { margin: 0; @bottom-left { content: none } @bottom-right { content: none } }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: Carlito, Calibri, sans-serif; font-size: 10.6pt; line-height: 1.38;
  color: #1E2230; background: #fff; margin: 0; hyphens: auto; -webkit-hyphens: auto; }
p, li, dd { text-align: justify; }
p { margin: 0 0 7pt 0; orphans: 3; widows: 3; }
b, strong { color: #14183A; }
code { font-family: "Space Mono"; font-size: 8.4pt; color: #242478; background: #EEF0F6;
  padding: 0 3px; border-radius: 3px; hyphens: none; }

/* ── títulos ── */
h1 { counter-increment: sec; break-before: auto; break-inside: avoid; margin-top: 30pt !important; break-after: avoid; font-family: "Shantell Sans"; font-weight: 800;
  font-size: 25pt; line-height: 1.18; color: #242478; margin: 0 0 14pt 0; hyphens: none;
  text-align: left; }
h1 .hl { background: linear-gradient(transparent 58%, #FFE94A 58%, #FFE94A 92%, transparent 92%);
  -webkit-box-decoration-break: clone; box-decoration-break: clone; padding: 0 4px; }
h1::before { content: "SECCIÓN " counter(sec); display: block; font-family: "Space Mono";
  font-weight: 700; font-size: 8.5pt; letter-spacing: .14em; color: #A82424; margin-bottom: 4pt; }
h1.sin-numero, h1.anexos { counter-increment: none; }
h1.sin-numero, h1.anexos, h1#el-problema-y-la-idea, h1#lo-socioemocional, h1#decisiones-abiertas { break-before: page; margin-top: 0 !important; }
h1.sin-numero::before { content: "PARA EMPEZAR"; }
h1.anexos::before { content: "AL FINAL"; }
h2 { hyphens: none; text-align: left; font-family: "Shantell Sans"; font-weight: 700; font-size: 14pt; line-height: 1.2;
  color: #242478; margin: 15pt 0 6pt 0; break-after: avoid; }
h3 { font-family: "Space Mono"; font-size: 9pt; letter-spacing: .08em; text-transform: uppercase;
  color: #A82424; margin: 12pt 0 4pt 0; break-after: avoid; }
ul, ol { margin: 0 0 8pt 0; padding-left: 18pt; }
li { margin-bottom: 3pt; orphans: 2; widows: 2; }

/* ── tablas: sin rayas; cabecera de color y filas alternas ── */
table { width: 100%; border-collapse: separate; border-spacing: 0; margin: 4pt 0 11pt 0;
  font-size: 9.6pt; line-height: 1.3; break-inside: auto; }
thead th { background: #242478; color: #fff; font-family: "Space Mono"; font-weight: 700;
  font-size: 7.6pt; letter-spacing: .05em; text-transform: uppercase; text-align: left;
  padding: 5pt 7pt; hyphens: none; }
thead th:first-child { border-radius: 5px 0 0 0; } thead th:last-child { border-radius: 0 5px 0 0; }
td { padding: 4.5pt 7pt; vertical-align: top; text-align: left; hyphens: manual; }
tbody tr:nth-child(odd) td { background: #F3F4F8; }
tr { break-inside: avoid; }
td code { font-size: 7.8pt; }

/* ── recuadros (acento vertical, nunca horizontal) ── */
.nota { border-left: 5px solid #242478; background: #F2F3FA; padding: 8pt 11pt 3pt 11pt;
  margin: 8pt 0 11pt 0; border-radius: 0 6px 6px 0; break-inside: avoid; font-size: 10.4pt; }
.nota.oro { border-color: #C9821B; background: #FBF4E7; }
.nota.rojo { border-color: #A82424; background: #FBEFEF; }
.nota.azul { border-color: #1F4E8C; background: #EEF3FA; }
.cita { border-left: 5px solid #E4572E; background: #FFF7F2; padding: 9pt 13pt 3pt 13pt;
  margin: 9pt 0 12pt 0; border-radius: 0 6px 6px 0; break-inside: avoid; }
.cita p { font-family: "Shantell Sans"; font-weight: 700; font-size: 12.5pt; line-height: 1.35;
  color: #242478; text-align: left; hyphens: none; }

/* ── el hilo y las fases ── */
.hilo { display: flex; gap: 7pt; margin: 6pt 0 12pt 0; break-inside: avoid; }
.hilo .pieza { flex: 1; border-radius: 7px; padding: 8pt 9pt; color: #fff; position: relative; }
.hilo .pieza b { display: block; font-family: "Space Mono"; font-size: 10pt; letter-spacing: .06em;
  color: #fff; margin-bottom: 3pt; }
.hilo .pieza span { font-size: 9.6pt; line-height: 1.25; display: block; }
.hilo .c1 { background: #242478; } .hilo .c2 { background: #A82424; }
.hilo .c3 { background: #30843C; } .hilo .c4 { background: #C9821B; }
.fases { display: flex; gap: 3pt; margin: 4pt 0 12pt 0; break-inside: avoid; }
.fase { color: #fff; border-radius: 5px; padding: 6pt 5pt; min-width: 0; }
.fase b { display: block; font-family: "Space Mono"; font-size: 11pt; color: #fff; }
.fase span { display: block; font-size: 8.2pt; line-height: 1.15; hyphens: none; }

/* ── figuras ── */
figure { margin: 6pt 0 12pt 0; break-inside: avoid; text-align: center; }
figure img { max-width: 100%; max-height: 92mm; }
figcaption { font-size: 8.8pt; font-style: italic; color: #4A5060; margin-top: 4pt;
  text-align: center; line-height: 1.3; hyphens: none; }
figure:has(img.media) img { width: auto; max-height: 150mm; }
figure:has(img.chica) img { max-height: 62mm; }
.dos { display: flex; gap: 12pt; align-items: flex-start; margin: 6pt 0 10pt 0; break-inside: avoid; }
.dos > figure { flex: 1; margin: 0; }
.dos > figure img { max-height: 118mm; }
.dos > .texto-lado { flex: 1.15; font-size: 10.2pt; }
.dos > .texto-lado ol { padding-left: 15pt; }

/* ── anatomía: tarjeta con números ── */
.anatomia { position: relative; margin: 4pt 0 6pt 0; break-inside: avoid; }
.anatomia figure { margin: 0; }
.anatomia > p { margin: 0; }
.anatomia > p:has(.m) { height: 0; line-height: 0; font-size: 0; }
.anatomia figcaption { display: none; }
.anatomia img { width: 100%; max-height: none; }
.anatomia .m { position: absolute; transform: translate(-50%,-50%); width: 17pt; height: 17pt; border-radius: 50%;
  background: #E4572E; color: #fff; font-family: "Space Mono"; font-weight: 700; font-size: 8.5pt;
  line-height: 17pt; text-align: center; box-shadow: 0 0 0 2px #fff; }
.leyenda ol { columns: 2; column-gap: 26pt; font-size: 9.8pt; margin-top: 2pt; }
.leyenda li { break-inside: avoid; text-align: left; }
.leyenda li::marker { font-family: "Space Mono"; font-weight: 700; color: #E4572E; }

/* ── portada ── */
.portada-pag { height: 279.4mm; width: 215.9mm; position: relative; overflow: hidden;
  background-color: #fff;
  background-image: radial-gradient(circle, #D1D1D1 1.1px, transparent 1.3px);
  background-size: 7mm 7mm; background-position: 3.5mm 3.5mm; padding: 26mm 24mm; }
.portada-pag .logo { height: 25mm; }
.portada-pag .kicker { font-family: "Space Mono"; font-weight: 700; font-size: 9.5pt;
  letter-spacing: .16em; color: #A82424; margin: 30mm 0 6mm 0; }
.portada-pag .titulo { hyphens: none; text-align: left; font-family: "Shantell Sans"; font-weight: 800; font-size: 40pt;
  line-height: 1.04; color: #242478; margin: 0; }
.portada-pag .titulo span { background: linear-gradient(transparent 55%, #FFE94A 55%, #FFE94A 92%, transparent 92%); }
.portada-pag .sub { font-size: 16pt; line-height: 1.3; color: #1E2230; margin: 9mm 0 0 0;
  max-width: 140mm; text-align: left; }
.portada-pag .areas { display: flex; flex-wrap: wrap; gap: 6pt 11pt; margin-top: 16mm; }
.portada-pag .areas div { font-family: "Space Mono"; font-size: 8.5pt; color: #1E2230;
  display: flex; align-items: center; gap: 5pt; }
.portada-pag .areas i { display: inline-block; width: 11pt; height: 11pt; border-radius: 50%; }
.portada-pag .pie { position: absolute; left: 24mm; right: 24mm; bottom: 24mm;
  background: #fff; border-left: 5px solid #242478; padding: 9pt 13pt; border-radius: 0 6px 6px 0;
  font-size: 10.5pt; line-height: 1.45; box-shadow: 0 0 0 1px #D8DEE6; }
.portada-pag .pie b { font-family: "Space Mono"; font-size: 8pt; letter-spacing: .1em;
  color: #A82424; display: block; }
.portada-pag .sello { position: absolute; right: 26mm; top: 30mm; transform: rotate(-8deg);
  border: 2.5px solid #A82424; border-radius: 50%; width: 36mm; height: 36mm; color: #A82424;
  font-family: "Shantell Sans"; font-weight: 800; font-size: 11pt; line-height: 1.1;
  display: flex; align-items: center; justify-content: center; text-align: center; padding: 4mm; }

/* ── índice ── */
.indice { break-before: page; }
.indice h1.toc { counter-increment: none; break-before: avoid; }
.indice h1.toc::before { content: "CONTENIDO"; }
.indice ol { list-style: none; padding: 0; margin: 4pt 0 0 0; }
.indice li { display: flex; align-items: baseline; gap: 10pt; padding: 3.2pt 8pt; margin: 0;
  border-radius: 4px; }
.indice li:nth-child(odd) { background: #F3F4F8; }
.indice .n { font-family: "Space Mono"; font-weight: 700; color: #A82424; width: 20pt; font-size: 9pt; }
.indice .t { flex: 1; font-family: "Shantell Sans"; font-weight: 700; font-size: 11pt; color: #242478; text-align: left; }
.indice .s { display: block; font-family: Carlito; font-weight: 400; font-size: 9pt; color: #4A5060; }
.indice .p { font-family: "Space Mono"; font-size: 9.5pt; color: #242478; }
"""

SUBS = {
    "Antes de leer": "Qué es este documento y qué está pendiente",
    "El problema y la idea": "Por qué un cuaderno y no un profesor estrella",
    "Las unidades del método": "Misión, clase y las seis fases",
    "La regla central: primero el andamiaje, después la respuesta": "El cuaderno como instrumento de auditoría",
    "Anatomía de una hoja": "Cada parte de la tarjeta y para qué está",
    "Estrategias y subestrategias": "Cómo se construyen y cómo se nombran; el caso de Inglés",
    "El entrenamiento Saber 11": "El membrete, la procedencia y las claves",
    "El simulacro y la devolución": "Clases 7 y 8 y las hojas de simulacro",
    "El planeador del docente": "«TU APORTE», las dinámicas y el reto del corte",
    "Las guías proyectables": "Teclas, cronómetro y claves con «Revelar»",
    "Lo socioemocional": "La apertura, el diario y el cierre",
    "Control de calidad": "Verificadores, revisión visual, hallazgos y especialistas",
    "Qué datos producirá el método": "Lo que se puede medir desde el primer sábado",
    "Decisiones abiertas": "Lo que tiene que decidir la Gerencia y Nelson",
    "Cómo se sostiene y se amplía el sistema": "Para mantenerlo sin asesoría externa",
    "Anexos": "Mapa de páginas, entregables, decisiones y glosario",
}


def portada():
    areas = "".join(f'<div><i style="background:{c}"></i>{n}</div>' for n, c in AREAS)
    return f"""<section class="portada-pag">
<img class="logo" src="img/logo_educate.png" alt="EDUCATE">
<div class="sello">primero el andamiaje, después la respuesta</div>
<div class="kicker">CUADERNO SABER 11 · EDUCATE · PARA EL SABER</div>
<p class="titulo">Documento maestro<br>de <span>metodología</span></p>
<p class="sub">Qué es el método, por qué funciona así y cómo se aplica, un sábado cualquiera y con cualquier profesor.</p>
<div class="areas">{areas}</div>
<div class="pie"><b>VERSIÓN PARA APROBACIÓN · 10 DE NOVIEMBRE DE 2026</b>
Para Cristian Bueno, Gerente General, y para los coordinadores y profesores de EDUCATE.<br>
Proyecto de Nelson González, asesor comercial y pedagógico.</div>
</section>"""


def indice(titulos, paginas):
    filas = []
    k = 0
    for i, t in enumerate(titulos):
        if t == "Antes de leer":
            n = ""
        elif t == "Anexos":
            n = "A–D"
        else:
            k += 1
            n = str(k)
        p = paginas.get(t, "")
        filas.append(f'<li><span class="n">{n}</span><span class="t">{html.escape(t)}'
                     f'<span class="s">{html.escape(SUBS.get(t, ""))}</span></span>'
                     f'<span class="p">{p}</span></li>')
    return ('<section class="indice"><h1 class="toc">Contenido</h1><ol>' + "".join(filas)
            + "</ol></section>")


def cuerpo():
    out = subprocess.run(["pandoc", MD, "-f", "markdown", "-t", "html5", "--wrap=none"],
                         capture_output=True, text=True, check=True).stdout
    out = re.sub(r'<div class="portada">\s*</div>', "", out)
    out = re.sub(r"(<h1[^>]*>)(.*?)(</h1>)", r'\1<span class="hl">\2</span>\3', out, flags=re.S)
    titulos = [html.unescape(re.sub(r"<[^>]+>", "", m))
               for m in re.findall(r"<h1[^>]*>(.*?)</h1>", out, flags=re.S)]
    return out, titulos


def html_completo(cuerpo_html, titulos, paginas):
    return f"""<!doctype html><html lang="es"><head><meta charset="utf-8">
<title>Documento maestro de metodología · EDUCATE</title><style>{CSS}</style></head>
<body>{portada()}{indice(titulos, paginas)}{cuerpo_html}</body></html>"""


def imprimir(html_path, pdf_path):
    js = f"""
const {{ chromium }} = require({os.path.join(PLAYWRIGHT, 'playwright')!r});
(async () => {{
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto("file://" + {html_path!r}, {{ waitUntil: "load" }});
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({{ path: {pdf_path!r}, format: "Letter", preferCSSPageSize: true,
                printBackground: true }});
  await b.close();
}})();"""
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(js)
    subprocess.run(["node", f.name], check=True)
    os.unlink(f.name)


def paginas_de(pdf, titulos):
    """Página donde empieza cada sección: se busca su rótulo («SECCIÓN n», «PARA EMPEZAR»,
    «AL FINAL») seguido de las primeras palabras del título."""
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", pdf], capture_output=True,
                                                         text=True).stdout).group(1))
    rotulos, k = {}, 0
    for t in titulos:
        if t == "Antes de leer":
            rotulos[t] = "PARA EMPEZAR"
        elif t == "Anexos":
            rotulos[t] = "AL FINAL"
        else:
            k += 1
            rotulos[t] = f"SECCIÓN {k}"
    res = {}
    for pg in range(3, n + 1):
        txt = " ".join(subprocess.run(["pdftotext", "-f", str(pg), "-l", str(pg), pdf, "-"],
                                      capture_output=True, text=True).stdout.split())
        for t in titulos:
            pat = re.escape(rotulos[t]) + r"\b\s+" + re.escape(" ".join(t.split()[:3]))
            if t not in res and re.search(pat, txt):
                res[t] = pg
    return res, n


def main():
    cuerpo_html, titulos = cuerpo()
    tmp = os.path.join(AQUI, "_arma.html")
    try:
        with open(tmp, "w") as f:
            f.write(html_completo(cuerpo_html, titulos, {}))
        imprimir(tmp, PDF)
        paginas, _ = paginas_de(PDF, titulos)
        with open(tmp, "w") as f:
            f.write(html_completo(cuerpo_html, titulos, paginas))
        imprimir(tmp, PDF)
        paginas2, n = paginas_de(PDF, titulos)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    faltan = [t for t in titulos if t not in paginas2]
    if paginas2 != paginas:
        print("Atención: el índice cambió la paginación; vuelve a correr el script.")
    print(f"{PDF}: {n} páginas")
    for t in titulos:
        print(f"  p. {paginas2.get(t, '?'):>3}  {t}")
    if faltan:
        print("No se encontró la página de:", faltan)
        sys.exit(1)


if __name__ == "__main__":
    main()
