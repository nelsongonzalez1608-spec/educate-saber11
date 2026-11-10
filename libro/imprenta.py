#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Versión de IMPRENTA del cuaderno (aparte: no toca el cuaderno ni sus PDF de revisión).

Especificaciones de la litografía (Nelson, 9 nov · tablero/decisiones.csv): carta, pegado como un
libro (lomo encolado), doble cara, sangrado de 3 mm con marcas de corte, CMYK y PDF/X.

Qué hace, a partir de entregables/Cuaderno_Saber11_completo_398_paginas.pdf (solo lo lee):

  1. LOMO. Cada página entra como Form XObject (vectores y fuentes intactos), escalada a ESCALA y
     corrida hacia afuera para que entre la tinta y el corte del lado del lomo queden LOMO_CM:
     a la izquierda en las impares y a la derecha en las pares (la paridad es la del cuaderno,
     así que una prueba solo puede llevar páginas cuya paridad coincida con su lugar en la prueba).
     Correr el marco sin escalar no alcanza: el borde exterior tiene 0,60 cm de blanco y el lomo
     pide 1,40 cm más.
  2. SANGRADO Y MARCAS. Página final = carta + 3 mm por lado (BleedBox) + 12 mm de zona de marcas
     (MediaBox); TrimBox = carta exacta. Marcas de corte en registro (C100 M100 Y100 K100), fuera
     del sangrado. En el estilo B ningún fondo llega al borde: todo termina a ≥ 0,6 cm del corte
     (el fondo es blanco y la cuadrícula de puntos va de 40 a 1960), así que el sangrado es papel.
  3. NEGRO. Antes de pasar a CMYK, los colores neutros se reescriben en K solo: la tinta
     #1E2230 y todo neutro con canal máximo ≤ 0,25 → K100; los grises neutros → K = 1 − gris
     (el #6E7480 de los rótulos queda en K54; el #D1D1D1 de la cuadrícula, en K18). Los tintes
     claros con color (#FFF7F2 del salvavidas, #D8DEE6 de las líneas) se dejan a la conversión. Así la
     letra pequeña no depende del registro de cuatro tintas.
  4. CMYK. Ghostscript (pdfwrite, ColorConversionStrategy=CMYK, perfil de salida PERFIL).
     Los colores ya en DeviceCMYK (el negro del paso 3 y las marcas) pasan intactos.
  5. PDF/X-4 (preparado, no validado): OutputIntent con el perfil, GTS_PDFXVersion, TrimBox y
     BleedBox en cada página y XMP con pdfxid. Ghostscript 10.02 solo escribe PDF/X-3, que no
     admite transparencias (las sombras de las tarjetas): las aplanaría volviendo imagen la
     página entera. X-4 sí las admite. La litografía debe correr su preflight.

Uso:
    python3 imprenta.py                      # la prueba de 10 páginas → entregables/imprenta/
    python3 imprenta.py --medir 1-20         # arma esas páginas en /tmp y mide tiempo y peso
    python3 imprenta.py --completo           # el cuaderno entero (solo cuando Nelson apruebe)
Opciones: --lomo-cm 2.0  --escala 0.93
"""
import argparse
import os
import shutil
import subprocess
import sys
import tempfile
import time

import pikepdf

RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
FUENTE = os.path.join(RAIZ, "entregables", "Cuaderno_Saber11_completo_398_paginas.pdf")
SALIDA = os.path.join(RAIZ, "entregables", "imprenta")
PERFIL = "/usr/share/color/icc/ghostscript/default_cmyk.icc"   # Artifex CMYK SWOP (estucado)
PERFIL_NOMBRE = "Artifex CMYK SWOP (Ghostscript) · reemplazar por el de la litografía"

MM = 72 / 25.4
W, H = 612.0, 792.0                  # carta en puntos
SANGRADO = 3 * MM
ZONA = 12 * MM                       # del corte al borde del MediaBox (marcas)
MARCA_DESDE, MARCA_LARGO = 3.5 * MM, 6 * MM
U = W / 2000                         # 1 unidad del SVG en puntos
TINTA_IZQ, TINTA_DER = 56 * U, 1944 * U   # dónde empieza y termina la tinta (medido en las 398)
TINTA_ARR, TINTA_ABJ = 14 * U, 65 * U      # blanco arriba y abajo de la tinta (cabecera y pie)

# Las 10 páginas de la prueba: (página del cuaderno, qué prueba). La posición en la prueba tiene
# la misma paridad que la página real, para que el lomo quede del lado que quedará en el libro.
PRUEBA = [
    (1, "Portada del cuaderno · logo raster"),
    (178, "Taller de Biología con letra pequeña (la que más texto ≤ 14 unidades tiene)"),
    (3, "Apertura · tablero de metas"),
    (30, "Matemáticas con figura (triángulo y tabla) · Misión 4"),
    (7, "Portada de área · Matemáticas"),
    (370, "Entrenamiento ICFES de Inglés · el texto más largo del cuaderno"),
    (103, "Simulacro de Lectura Crítica"),
    (396, "Cierre · después del examen"),
    (359, "Inglés con «Corrección EDUCATE»"),
    (398, "Mensaje final"),
]


# ───────────────────────── 1 · 2  imposición: lomo, sangrado, marcas ─────────────────────────
def _marcas():
    """Marcas de corte en las cuatro esquinas, en registro (CMYK 100/100/100/100)."""
    x0, y0 = ZONA, ZONA
    x1, y1 = ZONA + W, ZONA + H
    a, b = MARCA_DESDE, MARCA_DESDE + MARCA_LARGO
    s = ["q 1 1 1 1 K 0.25 w 0 J"]
    for x, sx in ((x0, -1), (x1, 1)):
        for y, sy in ((y0, -1), (y1, 1)):
            s.append(f"{x + sx * a:.3f} {y:.3f} m {x + sx * b:.3f} {y:.3f} l S")   # horizontal
            s.append(f"{x:.3f} {y + sy * a:.3f} m {x:.3f} {y + sy * b:.3f} l S")   # vertical
    s.append("Q")
    return ("\n".join(s) + "\n").encode()


def geometria(pagina, lomo_cm, escala):
    """(e, f) del cm que pone la página original escalada: lomo a la izquierda si es impar."""
    lomo = lomo_cm * 10 * MM
    if pagina % 2:                                       # impar: lomo a la izquierda
        e = lomo - TINTA_IZQ * escala
    else:                                                # par: lomo a la derecha
        e = W - lomo - TINTA_DER * escala
    f = (H - H * escala) / 2 - (TINTA_ABJ - TINTA_ARR) / 2 * escala   # mismo blanco arriba y abajo
    return e, f


def margenes(lomo_cm, escala):
    """Distancias del corte a la tinta, en cm: (lomo, exterior, arriba, abajo)."""
    lomo = lomo_cm * 10 * MM
    ext = W - lomo - (TINTA_DER - TINTA_IZQ) * escala
    f = (H - H * escala) / 2 + (TINTA_ARR + TINTA_ABJ) / 2 * escala
    return lomo / MM / 10, ext / MM / 10, f / MM / 10, f / MM / 10


def imponer(paginas, dest, lomo_cm=2.0, escala=0.93, fuente=FUENTE):
    """Arma el PDF RGB de imprenta con las páginas pedidas (números del cuaderno, en orden).
    Comprueba que cada una caiga en su paridad real."""
    for pos, p in enumerate(paginas, 1):
        if pos % 2 != p % 2:
            raise ValueError(f"la página {p} quedaría en la posición {pos}: el lomo saldría del lado "
                             "equivocado. Escoge páginas que alternen impar/par.")
    src = pikepdf.open(fuente)
    out = pikepdf.new()
    marcas = _marcas()
    mw, mh = W + 2 * ZONA, H + 2 * ZONA
    for p in paginas:
        fx = out.copy_foreign(pikepdf.Page(src.pages[p - 1]).as_form_xobject())
        e, f = geometria(p, lomo_cm, escala)
        pg = pikepdf.Dictionary(
            Type=pikepdf.Name.Page,
            MediaBox=[0, 0, mw, mh],
            TrimBox=[ZONA, ZONA, ZONA + W, ZONA + H],
            BleedBox=[ZONA - SANGRADO, ZONA - SANGRADO, ZONA + W + SANGRADO, ZONA + H + SANGRADO],
            Resources=pikepdf.Dictionary(XObject=pikepdf.Dictionary(P0=fx)),
        )
        cuerpo = (f"q {escala:.5f} 0 0 {escala:.5f} {ZONA + e:.3f} {ZONA + f:.3f} cm /P0 Do Q\n").encode()
        pg.Contents = out.make_stream(cuerpo + marcas)
        out.pages.append(pikepdf.Page(pg))
    out.docinfo["/Title"] = "EDUCATE · Cuaderno Saber 11 · imprenta"
    out.save(dest, compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
    return dest


# ───────────────────────────── 3 · negro y grises en K solo ─────────────────────────────
OSCURO = 0.25          # neutro con todos los canales ≤ esto → K100
NEUTRO = 0.08          # diferencia entre canales que aún es gris en tonos oscuros y medios (≤ 0,6)
NEUTRO_CLARO = 0.02    # en tonos claros solo el gris puro: #FFF7F2 (salvavidas) o #F5E5E5 son tintes


def _a_k(r, g, b):
    d, hi = max(r, g, b) - min(r, g, b), max(r, g, b)
    if d > (NEUTRO if hi <= 0.6 else NEUTRO_CLARO):
        return None
    if hi <= OSCURO:
        return 1.0
    return round(1 - (r + g + b) / 3, 4)


def negro_en_k(pdf_path, dest):
    """Reescribe rg/RG/g/G neutros en k/K (solo negro) en las páginas y en todas sus formas.
    Devuelve un resumen {color original: K}."""
    pdf = pikepdf.open(pdf_path)
    vistos, resumen = set(), {}

    def reescribir(obj):
        ops = pikepdf.parse_content_stream(obj)
        nuevos, cambio = [], False
        for args, op in ops:
            o = str(op)
            if o in ("rg", "RG", "g", "G"):
                v = [float(a) for a in args]
                rgb = v if len(v) == 3 else v * 3
                k = _a_k(*rgb)
                if k is not None:
                    hexa = "#" + "".join(f"{round(c * 255):02X}" for c in rgb)
                    resumen[hexa] = k
                    nuevos.append(([0, 0, 0, k], pikepdf.Operator("k" if o in ("rg", "g") else "K")))
                    cambio = True
                    continue
            nuevos.append((args, op))
        if cambio:
            data = pikepdf.unparse_content_stream(nuevos)
            if isinstance(obj, pikepdf.Stream):
                obj.write(data)
            else:
                obj.Contents = pdf.make_stream(data)

    def recorrer(res):
        if res is None:
            return
        for _, x in (res.get("/XObject") or {}).items():
            if x.objgen in vistos or x.get("/Subtype") != "/Form":
                continue
            vistos.add(x.objgen)
            reescribir(x)
            recorrer(x.get("/Resources"))
        for _, g in (res.get("/ExtGState") or {}).items():
            sm = g.get("/SMask")
            if isinstance(sm, pikepdf.Dictionary) and "/G" in sm and sm.G.objgen not in vistos:
                vistos.add(sm.G.objgen)        # las máscaras se dejan en su espacio (luminosidad)
        for _, pat in (res.get("/Pattern") or {}).items():
            if isinstance(pat, pikepdf.Stream) and pat.objgen not in vistos:
                vistos.add(pat.objgen)
                reescribir(pat)
                recorrer(pat.get("/Resources"))

    for page in pdf.pages:
        reescribir(page)
        recorrer(page.Resources)
    pdf.save(dest)
    return resumen


# ───────────────────────────── 4 · 5  CMYK y PDF/X-4 ─────────────────────────────
def a_cmyk(src, dest):
    subprocess.run([
        "gs", "-q", "-dBATCH", "-dNOPAUSE", "-dSAFER", "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.6", "-sColorConversionStrategy=CMYK",
        "-sProcessColorModel=DeviceCMYK", f"-sOutputICCProfile={PERFIL}",
        "-dRenderIntent=1",                      # colorimétrico relativo
        "-dAutoRotatePages=/None", "-dEmbedAllFonts=true", "-dSubsetFonts=true",
        "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
        "-dAutoFilterColorImages=false", "-sColorImageFilter=FlateEncode",
        "-o", dest, src], check=True)


def marcar_pdfx4(path, cajas, titulo):
    """OutputIntent + cajas + metadatos PDF/X-4. `cajas`: [(MediaBox, TrimBox, BleedBox)]."""
    pdf = pikepdf.open(path, allow_overwriting_input=True)
    icc = pdf.make_stream(open(PERFIL, "rb").read())
    icc.N = 4
    pdf.Root.OutputIntents = pikepdf.Array([pikepdf.Dictionary(
        Type=pikepdf.Name.OutputIntent, S=pikepdf.Name.GTS_PDFX,
        OutputConditionIdentifier="Custom", OutputCondition=PERFIL_NOMBRE,
        Info=PERFIL_NOMBRE, RegistryName="http://www.color.org", DestOutputProfile=icc)])
    for page, (mb, tb, bb) in zip(pdf.pages, cajas):
        page.MediaBox, page.TrimBox, page.BleedBox = mb, tb, bb
        for k in ("/CropBox", "/ArtBox"):
            if k in page:
                del page[k]
    # cairo marca cada grupo de transparencia (y la página entera, que entra como forma) con
    # /CS /DeviceRGB: el RIP mezclaría en RGB y el negro K100 volvería a salir en cuatro tintas.
    grupos = 0
    for o in pdf.objects:
        if isinstance(o, (pikepdf.Dictionary, pikepdf.Stream)) and "/Group" in o:
            g = o.Group
            if g.get("/CS") == pikepdf.Name.DeviceRGB:
                g.CS = pikepdf.Name.DeviceCMYK
                grupos += 1
    pdf.docinfo["/Title"] = titulo
    pdf.docinfo["/Trapped"] = pikepdf.Name.False_
    pdf.docinfo["/GTS_PDFXVersion"] = "PDF/X-4"
    with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
        meta["dc:title"] = titulo
        meta["pdfxid:GTS_PDFXVersion"] = "PDF/X-4"
        meta["pdfx:GTS_PDFXVersion"] = "PDF/X-4"
        meta["xmp:CreatorTool"] = "EDUCATE imprenta.py"
    pdf.save(path)


def armar(paginas, dest_cmyk, dest_rgb=None, lomo_cm=2.0, escala=0.93, titulo=None):
    titulo = titulo or "EDUCATE · Cuaderno Saber 11 · imprenta"
    with tempfile.TemporaryDirectory() as tmp:
        rgb = dest_rgb or os.path.join(tmp, "rgb.pdf")
        imponer(paginas, rgb, lomo_cm, escala)
        k = os.path.join(tmp, "k.pdf")
        resumen = negro_en_k(rgb, k)
        a_cmyk(k, dest_cmyk)
    mw, mh = W + 2 * ZONA, H + 2 * ZONA
    cajas = [([0, 0, mw, mh], [ZONA, ZONA, ZONA + W, ZONA + H],
              [ZONA - SANGRADO, ZONA - SANGRADO, ZONA + W + SANGRADO, ZONA + H + SANGRADO])
             for _ in paginas]
    marcar_pdfx4(dest_cmyk, cajas, titulo)
    return resumen


def _rango(s):
    a, _, b = s.partition("-")
    return list(range(int(a), int(b or a) + 1))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--lomo-cm", type=float, default=2.0)
    ap.add_argument("--escala", type=float, default=0.93)
    ap.add_argument("--medir", help="rango de páginas para medir tiempo y peso, p. ej. 1-20")
    ap.add_argument("--completo", action="store_true")
    a = ap.parse_args()
    lo, ex, ar, ab = margenes(a.lomo_cm, a.escala)
    print(f"escala {a.escala:.3f} · tinta a {lo:.2f} cm del corte en el lomo, {ex:.2f} cm afuera, "
          f"{ar:.2f} cm arriba, {ab:.2f} cm abajo")
    print(f"letra: 14 u → {14 * U * a.escala:.2f} pt · 15 u → {15 * U * a.escala:.2f} pt · "
          f"20 u → {20 * U * a.escala:.2f} pt")
    t = time.time()
    if a.medir:
        d = tempfile.mkdtemp()
        pags = _rango(a.medir)
        r = armar(pags, os.path.join(d, "cmyk.pdf"), os.path.join(d, "rgb.pdf"), a.lomo_cm, a.escala)
        n = len(pags)
        for f in ("rgb.pdf", "cmyk.pdf"):
            mb = os.path.getsize(os.path.join(d, f)) / 1e6
            print(f"{f}: {mb:.1f} MB · {mb / n:.2f} MB por página → 398 páginas ≈ {mb / n * 398:.0f} MB")
        print(f"{n} páginas en {time.time() - t:.0f} s → 398 ≈ {(time.time() - t) / n * 398 / 60:.0f} min")
        shutil.rmtree(d)
        sys.exit()
    os.makedirs(SALIDA, exist_ok=True)
    if a.completo:
        n = len(pikepdf.open(FUENTE).pages)
        r = armar(list(range(1, n + 1)), os.path.join(SALIDA, f"Cuaderno_Saber11_imprenta_CMYK_{n}_paginas.pdf"),
                  None, a.lomo_cm, a.escala, "EDUCATE · Cuaderno Saber 11 · imprenta")
    else:
        r = armar([p for p, _ in PRUEBA], os.path.join(SALIDA, "Prueba_imprenta_10_paginas.pdf"),
                  os.path.join(SALIDA, "Prueba_imprenta_10_paginas_RGB.pdf"), a.lomo_cm, a.escala,
                  "EDUCATE · Cuaderno Saber 11 · prueba de imprenta (10 páginas)")
    print("neutros pasados a K solo:", ", ".join(f"{c}→K{k * 100:.0f}" for c, k in sorted(r.items())))
    print(f"listo en {time.time() - t:.0f} s")
