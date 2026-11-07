#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Visor de avance del cuaderno (página web privada en claude.ai).

    python3 visor_avance.py <carpeta_salida>

Escribe <carpeta_salida>/index.html (con los datos del tablero incrustados) y
<carpeta_salida>/pag/NNN.jpg (una imagen de 900 px por página hecha). Las imágenes salen de los
PDF de entregables/; las páginas que todavía no tienen PDF se toman de su SVG en libro/.
Después se publica la carpeta con la herramienta Artifact (mismo index.html → misma URL).
"""
import csv, json, os, subprocess, sys, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ENT, TAB, LIB = (os.path.join(RAIZ, d) for d in ("entregables", "tablero", "libro"))
PDFS = [("Cuaderno_Saber11_paginas_1_a_110_v2.pdf", 1, 110, 0),
        ("Sociales_completo_paginas_96_a_138.pdf", 111, 138, 95),
        ("Biologia_completo_paginas_139_a_181.pdf", 139, 181, 138)]


def imagenes(out, pags):
    os.makedirs(os.path.join(out, "pag"), exist_ok=True)
    for h in pags:
        n = h["pagina"]
        dst = os.path.join(out, "pag", f"{n:03d}")
        if os.path.exists(dst + ".jpg"):
            continue
        fuente = next(((f, n - d) for f, a, b, d in PDFS if a <= n <= b), None)
        if fuente:
            subprocess.run(["pdftoppm", "-f", str(fuente[1]), "-l", str(fuente[1]), "-scale-to-x", "900",
                            "-scale-to-y", "-1", "-jpeg", "-jpegopt", "quality=72", "-singlefile",
                            os.path.join(ENT, fuente[0]), dst], check=True)
        else:
            png = dst + ".png"
            subprocess.run(["rsvg-convert", "-w", "900", os.path.join(LIB, h["svg"] + ".svg"), "-o", png], check=True)
            subprocess.run(["convert", png, "-quality", "72", dst + ".jpg"], check=True)
            os.remove(png)


def main(out):
    man = sorted(json.load(open(os.path.join(TAB, "manifiesto_hojas.json"), encoding="utf-8")),
                 key=lambda h: h["pagina"])
    imagenes(out, man)
    leer = lambda f: list(csv.DictReader(open(os.path.join(TAB, f), encoding="utf-8-sig")))
    h = leer("hallazgos.csv")
    sev = {}
    for x in h:
        sev[x["severidad"]] = sev.get(x["severidad"], 0) + 1
    datos = dict(pags=[dict(n=x["pagina"], svg=x["svg"], rol=x["rol"], tit=x["titulo"]) for x in man],
                 mis={r["mision"]: dict(comp=r["componente"], est=r["estrategias"]) for r in leer("misiones.csv")},
                 hallazgos=len(h), sev=sev, instrumentos=len(leer("instrumentos.csv")), icfes=len(leer("icfes.csv")))
    p = open(os.path.join(LIB, "visor_avance_plantilla.html"), encoding="utf-8").read()
    p = p.replace("__DATOS__", json.dumps(datos, ensure_ascii=False))
    p = p.replace("__FECHA__", datetime.date.today().strftime("%d/%m/%Y"))
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(p)
    print(len(man), "páginas en el visor")


if __name__ == "__main__":
    main(sys.argv[1])
