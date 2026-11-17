"""La conceptualización de cada área, lista para la guía y el planeador (ver conceptos.py).

    import conceptos_area as CA
    D, colores = CA.de("soc", 3)        # None, None si el área todavía no tiene datos para esa misión

Los datos viven en conceptos_<área>.py (DATOS = {misión: dict(...)}); aquí se ordenan las estrategias
como las imprime el cuaderno (tablero/misiones.csv) y se pintan con el color que les da el planeador
(COLS_MIS, en el orden de MISIONES[mis]["estr"]). Matemáticas tiene su propio cargador (conceptos_mate.de).

Prueba visual de un área (dibuja todas las figuras en una hoja PNG por misión):
    python3 conceptos_area.py soc  [carpeta]
"""
import csv
import importlib
import os
import re
import sys

import conceptos

AQUI = os.path.dirname(os.path.abspath(__file__))
PREFIJO = {"lc": "LC", "soc": "SOC", "bio": "BIO", "qui": "QUI", "fis": "FIS", "ing": "ING"}
COLORES_LC = ["#A82424", "#242478", "#C9821B", "#5B3E96"]
_n = lambda s: re.sub(r"[^\w]", "", s.lower())


def orden_cuaderno(area, mis):
    """Nombres de las estrategias en el orden del cuaderno, escritos como en el planeador."""
    P = importlib.import_module("plan_" + area)
    plan = P.MISIONES[mis]["estr"]
    with open(os.path.join(AQUI, "..", "tablero", "misiones.csv"), encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if r["mision"].strip() == f"{PREFIJO[area]} Misión {mis}":
                csvl = [_n(x) for x in r["estrategias"].split(" · ")]
                por = {_n(x): x for x in plan}
                if sorted(csvl) == sorted(por):
                    return [por[x] for x in csvl]
    return list(plan)


def color_de(area, mis):
    P = importlib.import_module("plan_" + area)
    plan = P.MISIONES[mis]["estr"]
    cols = list(P.COLS_MIS[mis]) if hasattr(P, "COLS_MIS") else COLORES_LC
    return lambda nombre: cols[plan.index(nombre)]


def de(area, mis):
    try:
        M = importlib.import_module("conceptos_" + area)
    except ModuleNotFoundError:
        return None, None
    datos = M.DATOS.get(mis)
    if not datos:
        return None, None
    orden = orden_cuaderno(area, mis)
    cd = color_de(area, mis)
    D = conceptos.armar(datos, orden, cd)
    return D, [cd(n) for n in orden]


def prueba(area, carpeta):
    """Hoja PNG por misión con la idea central, las cuatro figuras y los textos, para revisarla a ojo."""
    import subprocess
    os.makedirs(carpeta, exist_ok=True)
    for mis in range(1, 7):
        D, cols = de(area, mis)
        if not D:
            print(f"misión {mis}: sin datos")
            continue
        piezas = [("centro", D["centro"][0], D["centro"][1], D["centro"][2])] + \
                 [(f"E{k+1}", i["t"], i["d"], i["svg"]) for k, i in enumerate(D["ideas"])]
        s = ['<svg xmlns="http://www.w3.org/2000/svg" width="1300" height="1650" viewBox="0 0 1300 1650">'
             '<rect width="1300" height="1650" fill="#fff"/>']
        for k, (rot, t, d, svg) in enumerate(piezas):
            y = 10 + k * 325
            fig = svg.replace("<svg ", f'<svg x="10" y="{y}" width="420" height="300" ', 1)
            s.append(fig)
            s.append(f'<rect x="10" y="{y}" width="420" height="300" fill="none" stroke="#eee"/>')
            s.append(f'<text x="450" y="{y+30}" font-family="Carlito" font-size="24" font-weight="700">{rot} · {t}</text>')
        s.append("</svg>")
        f = os.path.join(carpeta, f"{area}{mis}.svg")
        open(f, "w", encoding="utf-8").write("".join(s))
        subprocess.run(["rsvg-convert", "-w", "1000", f, "-o", f[:-4] + ".png"], check=True)
        print(f"misión {mis}: {D['titulo']} · {[i['t'] for i in D['ideas']]} → {f[:-4]}.png")


if __name__ == "__main__":
    prueba(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "/tmp/claude-0/prueba_conceptos")
