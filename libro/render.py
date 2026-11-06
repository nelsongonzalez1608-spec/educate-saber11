#!/usr/bin/env python3
"""SVG (W=2000, carta) → PDF carta + JPG de revisión.

    conv(svg, pdf)              una hoja SVG → una página PDF carta, centrada, margen 10 pt
    unir(svgs, pdf)             varias hojas → un solo PDF (conv + pdfunite)
    verifica(pdf, marca)        → (n páginas, [páginas sin la marca del pie])
                                Una página sin pie casi siempre es una hoja recortada o
                                que no se terminó de dibujar. Marcas: «Aprende» para el
                                cuaderno (el pie dice «Aprende · Practica · Avanza»),
                                «PLANEADOR» para los planeadores.

Desde la terminal (comportamiento del original del 28 oct):

    python3 render.py               # ap*.svg → pdf_*.pdf + chk_*.jpg + Cuaderno_APERTURA.pdf
    python3 render.py a.svg b.svg   # esas hojas

`unir()` y `verifica()` se perdieron el 6 nov (el zip del 28 oct era anterior a ellas);
reconstruidos el 6 nov con el contrato descrito en CLAUDE.md § 5.
"""
import glob
import os
import re
import subprocess
import sys
import tempfile

LIBRO = os.path.dirname(os.path.realpath(__file__))


def conv(src, out):
    h = open(src, encoding="utf-8").read(400)
    Wd = float(re.search(r'width="(\d+)"', h).group(1))
    Hd = float(re.search(r'height="(\d+)"', h).group(1))
    pw, ph, m = 612, 792, 10          # carta
    s = min((ph - 2 * m) / Hd, (pw - 2 * m) / Wd)
    w, hh = Wd * s, Hd * s
    subprocess.run(["rsvg-convert", "-f", "pdf", "--page-width", f"{pw}pt",
                    "--page-height", f"{ph}pt", "--width", f"{w:.1f}pt",
                    "--height", f"{hh:.1f}pt", "--left", f"{(pw - w) / 2:.1f}pt",
                    "--top", f"{(ph - hh) / 2:.1f}pt", src, "-o", out], check=True)


def unir(svgs, pdf):
    svgs = list(svgs)
    if not svgs:
        raise ValueError("unir(): no hay hojas")
    with tempfile.TemporaryDirectory() as tmp:
        partes = []
        for i, s in enumerate(svgs):
            p = os.path.join(tmp, f"{i:04d}.pdf")
            conv(s, p)
            partes.append(p)
        if len(partes) == 1:
            subprocess.run(["cp", partes[0], pdf], check=True)
        else:
            subprocess.run(["pdfunite", *partes, pdf], check=True)
    return pdf


def _paginas(pdf):
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"^Pages:\s+(\d+)", info, re.M).group(1))


def verifica(pdf, marca="Aprende"):
    n = _paginas(pdf)
    sin_pie = []
    for i in range(1, n + 1):
        txt = subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), pdf, "-"],
                             capture_output=True, text=True, check=True).stdout
        if marca.lower() not in txt.lower():
            sin_pie.append(i)
    return n, sin_pie


def _main(names):
    os.chdir(LIBRO)
    names = names or sorted(glob.glob("ap*.svg"))
    outs = []
    for n in names:
        base = n[:-4]
        conv(n, f"pdf_{base}.pdf")
        outs.append(f"pdf_{base}.pdf")
        subprocess.run(["pdftoppm", "-jpeg", "-r", "70", "-singlefile", f"pdf_{base}.pdf",
                        f"chk_{base}"], check=True)
    if len(outs) > 1:
        subprocess.run(["pdfunite", *outs, "Cuaderno_APERTURA.pdf"], check=True)
    print("ok", len(outs))


if __name__ == "__main__":
    _main(sys.argv[1:])
