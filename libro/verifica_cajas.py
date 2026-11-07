#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador de cajas del cuaderno · obligatorio antes de entregar (CLAUDE.md § 6).

Revisa en cada SVG de hoja:
  1. ALTO      · ningún instrumento baja más que el límite de su tarjeta (data-ymax).
  2. ANCHO     · ningún instrumento pasa del borde derecho M + 30 + IW = 1370 (encajar()
                 solo arregla el alto: el ancho se respeta a mano).
  3. LGRAY     · ningún texto en #D8DEE6: es el gris de las líneas; en papel no se lee.
  4. CHIPS     · ningún chip más ancho que su texto medido con tw() + 2 × pad (+4 px).
                 Contando caracteres salían hasta 170 px de más.

    python3 verifica_cajas.py                     # todas las hojas m*/lc*/soc*/… de libro/
    python3 verifica_cajas.py soc3_t1.svg …       # esas

Sale con código 1 si algo falla. Reconstruido el 6 nov 2026 (el original se perdió).
"""
import glob
import os
import re
import sys
import xml.etree.ElementTree as ET

from lib import tw, LGRAY
from taller_base import _cajas, X_MAX

NS = "{http://www.w3.org/2000/svg}"
TOL = 1.0
HOJAS = ("m[0-9]*_[ti][0-9].svg", "lc[0-9]*_[ti][0-9].svg", "soc[0-9]*_[ti][0-9].svg",
         "bio[0-9]*_[ti][0-9].svg", "qui[0-9]*_[ti][0-9].svg", "fis[0-9]*_[ti][0-9].svg",
         "ing[0-9]*_[ti][0-9].svg", "ing[0-9]*_t[0-9][0-9].svg",
         "prueba_*.svg")


def _tag(e):
    return e.tag.replace(NS, "")


def revisar(ruta):
    raiz = ET.parse(ruta).getroot()
    fallas = []
    # 1 y 2 · instrumentos
    n_inst = 0
    for g in raiz.iter(NS + "g"):
        if g.get("class") != "instrumento":
            continue
        n_inst += 1
        cs = _cajas(g)
        if not cs:
            continue
        x1 = max(c[2] for c in cs)
        y1 = max(c[3] for c in cs)
        ymax, xmax = float(g.get("data-ymax")), float(g.get("data-xmax", X_MAX))
        n = g.get("data-n")
        if y1 > ymax + TOL:
            fallas.append(f"pregunta {n}: baja hasta {y1:.0f}, el límite es {ymax:.0f} "
                          f"({y1 - ymax:.0f} px de más)")
        if x1 > xmax + TOL:
            peor = max(cs, key=lambda c: c[2])
            fallas.append(f"pregunta {n}: borde derecho {x1:.0f} > {xmax:.0f} "
                          f"(lo que se sale empieza en x={peor[0]:.0f}, y={peor[1]:.0f})")
    # 0 · la misión de la cabecera y del pie es la del archivo (soc3_i1 → MISIÓN 3).
    #     El 7 nov dos hojas salieron con la misión de otro módulo construido en el mismo proceso.
    m_arch = re.match(r"(?:.*/)?[a-z]+(\d)_[ti]\d+\.svg$", ruta)
    if m_arch:
        textos = ["".join(t.itertext()) for t in raiz.iter(NS + "text")]
        vistas = {int(x) for t in textos for x in re.findall(r"MISI[ÓO]N (\d)\b", t.upper())}
        if vistas and vistas != {int(m_arch.group(1))}:
            fallas.append(f"la hoja dice misión {sorted(vistas)} y el archivo es de la misión "
                          f"{m_arch.group(1)}: se construyó con la configuración de otro módulo")
    # 3 · texto en LGRAY
    for t in raiz.iter(NS + "text"):
        if (t.get("fill") or "").upper() == LGRAY.upper():
            txt = "".join(t.itertext()).strip()[:50]
            fallas.append(f"texto en LGRAY {LGRAY}: «{txt}» — usa GRAY #6E7480 o más oscuro")
    # 4 · chips
    for g in raiz.iter(NS + "g"):
        if g.get("class") != "chip":
            continue
        r = next((e for e in g if _tag(e) == "rect"), None)
        t = next((e for e in g if _tag(e) == "text"), None)
        if r is None or t is None:
            continue
        txt = "".join(t.itertext())
        size = float(t.get("font-size"))
        peso = "700" if t.get("font-weight") in ("700", "bold") else "400"
        pad = float(g.get("data-pad", 18))
        debe = tw(txt, size, peso) + 2 * pad
        es = float(r.get("width"))
        if es > debe + 4:
            fallas.append(f"chip «{txt}»: mide {es:.0f}, su texto pide {debe:.0f} "
                          f"({es - debe:.0f} px de más)")
    return n_inst, fallas


def main(args):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    rutas = args or sorted({f for p in HOJAS for f in glob.glob(p)})
    if not rutas:
        print("no hay hojas para revisar")
        return 1
    malas = 0
    for r in rutas:
        n, fallas = revisar(r)
        if fallas:
            malas += 1
            print(f"  ✘ {r}  ({n} instrumentos)")
            for f in fallas:
                print(f"      · {f}")
        else:
            print(f"  ✔ {r}  ({n} instrumentos)")
    print("TODO EN SU CAJA" if not malas else f"{malas} HOJA(S) CON PROBLEMAS")
    return 1 if malas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
