#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Verificador de pistas · ningún instrumento puede delatar la respuesta (CLAUDE.md § 2).

Dentro de cada <g class="instrumento"> busca dos clases de pista:

  BORDE       · un grupo de 3 a 6 recuadros del mismo tamaño (las opciones, las casillas)
                donde UNO SOLO tiene un grosor o un color de borde distinto a los demás.
  TIPOGRAFÍA  · un grupo de 3 a 6 líneas de texto con el mismo tamaño, color y x, donde
                todas menos una van en MAYÚSCULAS SOSTENIDAS, o al revés.

No revisa «la opción más larga»: eso se mira en el contenido, con la clave al lado.

    python3 verifica_pistas.py                  # todas las hojas de libro/
    python3 verifica_pistas.py soc3_t1.svg …

Sale con código 1 si encuentra una pista. Reconstruido el 6 nov 2026.
"""
import os
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict

from verifica_cajas import HOJAS, NS
import glob


def _mayus(s):
    letras = [c for c in s if c.isalpha()]
    return len(letras) >= 3 and all(c.isupper() for c in letras)


def _minus(s):
    letras = [c for c in s if c.isalpha()]
    return len(letras) >= 3 and not all(c.isupper() for c in letras)


def _solo_uno_distinto(valores):
    """Devuelve el índice del único elemento distinto, o None."""
    if not 3 <= len(valores) <= 6:
        return None
    cuenta = defaultdict(list)
    for i, v in enumerate(valores):
        cuenta[v].append(i)
    if len(cuenta) == 2:
        raros = [ix for ix in cuenta.values() if len(ix) == 1]
        if len(raros) == 1:
            return raros[0][0]
    return None


def revisar_instrumento(g):
    pistas = []
    # BORDE: recuadros hermanos del mismo tamaño
    grupos = defaultdict(list)
    for r in g.iter(NS + "rect"):
        if not r.get("stroke") or r.get("stroke") == "none":
            continue
        k = (round(float(r.get("width", 0))), round(float(r.get("height", 0))))
        if k[0] < 30 or k[1] < 20:
            continue
        grupos[k].append(r)
    for (w, h), rs in grupos.items():
        firmas = [(r.get("stroke", "").upper(), r.get("stroke-width", "")) for r in rs]
        i = _solo_uno_distinto(firmas)
        if i is not None:
            r = rs[i]
            pistas.append(f"BORDE · uno de {len(rs)} recuadros de {w}×{h} tiene borde "
                          f"{firmas[i][0]} {firmas[i][1]} y los demás no (x={r.get('x')}, y={r.get('y')})")
    # TIPOGRAFÍA: líneas hermanas (mismo tamaño, color y x)
    lineas = defaultdict(list)
    for t in g.iter(NS + "text"):
        txt = "".join(t.itertext()).strip()
        if not txt:
            continue
        x = t.get("x") or next((s.get("x") for s in t), None)
        k = (t.get("font-size"), (t.get("fill") or "").upper(), x)
        lineas[k].append(txt)
    for (size, fill, x), txts in lineas.items():
        if not 3 <= len(txts) <= 6:
            continue
        tipos = ["M" if _mayus(s) else "m" if _minus(s) else "-" for s in txts]
        if "-" in tipos:
            continue
        i = _solo_uno_distinto(tipos)
        if i is not None:
            pistas.append(f"TIPOGRAFÍA · en {len(txts)} líneas hermanas (tamaño {size}, x={x}) "
                          f"solo «{txts[i][:60]}» va {'en MAYÚSCULAS' if tipos[i] == 'M' else 'en minúsculas'}")
    return pistas


def revisar(ruta):
    raiz = ET.parse(ruta).getroot()
    out = []
    for g in raiz.iter(NS + "g"):
        if g.get("class") == "instrumento":
            for p in revisar_instrumento(g):
                out.append(f"pregunta {g.get('data-n')}: {p}")
    return out


def main(args):
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    rutas = args or sorted({f for p in HOJAS for f in glob.glob(p)})
    malas = 0
    for r in rutas:
        p = revisar(r)
        if p:
            malas += 1
            print(f"  ✘ {r}")
            for x in p:
                print(f"      · {x}")
        else:
            print(f"  ✔ {r}")
    print("NINGUNA PISTA" if not malas else f"{malas} HOJA(S) CON PISTAS")
    return 1 if malas else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
