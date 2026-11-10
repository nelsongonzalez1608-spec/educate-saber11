#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador del planeador y de las guías: desborde vertical, desborde por la derecha
   y texto en el gris de las líneas. Los desbordes no se ven en el código.

   El pie del planeador ocupa de 2476 a 2552, así que el contenido tiene que quedar
   por encima de 2470.
"""
import glob, re, sys

TOPE_Y = 2470        # donde empieza el pie
TOPE_X = 1930 + 3    # M + CW = 1930, con 3 px de tolerancia


def bajo(svg):
    mx, quien = 0, ""
    for m in re.finditer(r'<rect[^>]*\by="([-\d.]+)"[^>]*\bheight="([-\d.]+)"', svg):
        y, h = float(m.group(1)), float(m.group(2))
        if y == 0 and h >= 2500:
            continue                      # el fondo de la página
        if abs(y - 2476) < 1 and abs(h - 76) < 1:
            continue                      # el pie (y solo el pie: un recuadro que EMPIEZA
                                          # debajo de 2470 también se sale; 10 nov)
        if y + h > mx:
            mx, quien = y + h, "rect"
    for m in re.finditer(r'<text[^>]*\by="([-\d.]+)"', svg):
        y = float(m.group(1))
        if y >= TOPE_Y:
            continue
        if y > mx:
            mx, quien = y, "text"
    for m in re.finditer(r'<tspan[^>]*\bdy="([-\d.]+)"', svg):
        pass
    return mx, quien


def derecha(svg):
    mx = 0
    for m in re.finditer(r'<rect[^>]*\bx="([-\d.]+)"[^>]*\bwidth="([-\d.]+)"', svg):
        x, w = float(m.group(1)), float(m.group(2))
        if x == 0 and w >= 2000:
            continue
        mx = max(mx, x + w)
    for m in re.finditer(r'<line[^>]*\bx2="([-\d.]+)"', svg):
        mx = max(mx, float(m.group(1)))
    return mx


def main(patron="/home/claude/libro/plan_mate_*.svg"):
    malos = 0
    for f in sorted(glob.glob(patron)):
        s = open(f, encoding="utf-8").read()
        y, quien = bajo(s)
        x = derecha(s)
        gris = len(re.findall(r'<text[^>]*fill="#D8DEE6"', s, re.I))
        prob = []
        if y > TOPE_Y:
            prob.append(f"se mete en el pie por {y - TOPE_Y:.0f} px ({quien})")
        if x > TOPE_X:
            prob.append(f"se sale por la derecha {x - TOPE_X:.0f} px")
        if gris:
            prob.append(f"{gris} textos en el gris de las líneas")
        nom = f.split("/")[-1]
        if prob:
            malos += 1
            print(f"  ✗ {nom}: " + " · ".join(prob))
        else:
            print(f"  ✔ {nom}: baja hasta {y:.0f}, borde derecho {x:.0f}")
    print(("TODO EN SU CAJA" if not malos else f"{malos} hojas con problema"))
    return malos


if __name__ == "__main__":
    sys.exit(1 if main(*sys.argv[1:]) else 0)
