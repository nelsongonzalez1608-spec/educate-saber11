"""Registro de los instrumentos de pensamiento del cuaderno.

El original leía los módulos de misión (m1…m6, lc1…lc6, soc1, soc2) y se perdió el 6 nov
junto con ellos. Esta versión lee la fuente de verdad que sí sobrevivió:
`tablero/instrumentos.csv` (196 filas, una por pregunta).

    filas()          → [(area, mision, pregunta, estrategia, instrumento, contexto), …]
                       mismo contrato que la versión original (lo usan plan_mate.py,
                       plan_lc.py y visor_html.py).
    repetidos(extra) → títulos que aparecen más de una vez en el registro, contando
                       también los títulos nuevos que se pasen en `extra`.

Uso como verificador, antes de cerrar una misión:

    python3 extrae_instrumentos.py                   # revisa el registro completo
    python3 extrae_instrumentos.py "Título nuevo" …  # revisa además títulos candidatos

Sale con código 1 si hay títulos repetidos (regla 4: cada pregunta, su instrumento).
"""
import csv
import os
import sys
import unicodedata
from collections import defaultdict

CSV = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "tablero",
                   "instrumentos.csv")
CAMPOS = ("area", "mision", "pregunta", "estrategia", "instrumento", "contexto")


def filas(ruta=CSV):
    with open(ruta, encoding="utf-8-sig", newline="") as f:
        return [tuple(r[c].strip() for c in CAMPOS) for r in csv.DictReader(f)]


def _clave(t):
    """Compara títulos sin mayúsculas, tildes ni espacios de más."""
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(ch for ch in t if unicodedata.category(ch) != "Mn")
    return " ".join(t.split())


def repetidos(extra=(), ruta=CSV):
    donde = defaultdict(list)
    for a, mis, p, est, ins, ctx in filas(ruta):
        donde[_clave(ins)].append(f"{a} · misión {mis} · pregunta {p} · «{ins}»")
    for t in extra:
        donde[_clave(t)].append(f"NUEVO · «{t}»")
    return {k: v for k, v in donde.items() if len(v) > 1}


def main(argv):
    n = len(filas())
    rep = repetidos(argv)
    print(f"{n} instrumentos en el registro" + (f" + {len(argv)} nuevos" if argv else ""))
    if not rep:
        print("ok · ningún título repetido")
        return 0
    print(f"REPETIDOS · {len(rep)} título(s):")
    for lugares in rep.values():
        for l in lugares:
            print("   ", l)
        print()
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
