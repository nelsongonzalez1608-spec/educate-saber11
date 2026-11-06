#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""¿La clave que el planeador imprime al lado de cada pregunta ICFES es de ESA pregunta?

El planeador toma la clave del CSV del tablero por POSICIÓN, y el orden de las preguntas
en la hoja lo define el módulo m{n}_icfes.py. Si los dos órdenes no coinciden, el profesor
se para frente al salón con la clave equivocada. Esto compara membrete por membrete.
"""
import csv, re, sys

LIBRO = "/home/claude/libro/"


def del_modulo(n):
    """Membrete y enunciado en el orden en que el módulo monta las preguntas (QA…QD).
    En las misiones sin año verificado el membrete es el mismo para las cuatro, así que
    el cruce tiene que hacerse por el enunciado."""
    txt = open(f"{LIBRO}m{n}_icfes.py", encoding="utf-8").read()
    out = []
    for m in re.finditer(r'^Q([A-D])\s*=\s*dict\((.*?)\n\n', txt, re.M | re.S):
        cuerpo = m.group(2)
        f = re.search(r'\bf="([^"]+)"', cuerpo)
        enun = " ".join(re.findall(r'"([^"]{20,})"', cuerpo))
        out.append(((f.group(1) if f else ""), enun))
    return out


def del_csv(n):
    with open("/home/claude/tablero/icfes.csv", encoding="utf-8-sig") as f:
        r = list(csv.DictReader(f))
    return [(x["membrete"], x["clave"], x["contexto"]) for x in r
            if x["mision"].strip() == f"Misión {n}"]


def normaliza(s):
    """«Saber 11 · 2018-I · Cuadernillo 1 · N.º 59» y «2018-I · C1 · N.º 59» son lo mismo."""
    s = s.replace("Saber 11 · ", "").replace("Cuadernillo ", "C").replace("N.º", "N")
    s = re.sub(r"\s+", "", s).lower()
    return s


def main():
    malos = 0
    for n in range(1, 7):
        mod = del_modulo(n)
        csvf = del_csv(n)
        print(f"Misión {n}:")
        if len(mod) != len(csvf):
            print(f"  ✗ el módulo monta {len(mod)} preguntas y el CSV registra {len(csvf)}")
            malos += 1
            continue
        for i, ((fm, enun), (mb, cl, ctx)) in enumerate(zip(mod, csvf), 1):
            a, b = normaliza(fm), normaliza(mb)
            # Ojo: con a vacío (el módulo usa la constante FICFES, sin año), b.endswith("")
            # da True y la misión pasaba sin que se comparara nada.
            ok = bool(a) and bool(b) and (a == b or a.endswith(b) or b.endswith(a))
            via = "membrete"
            if not ok and ("sin año" in mb.lower() or "sinaño" in b):
                # Sin año verificado: el membrete es igual en las cuatro. Se cruza por las
                # palabras propias del contexto contra el enunciado real de la pregunta.
                claves = [p for p in re.split(r"[ ·,]+", ctx.lower())
                          if len(p) > 4 and p not in ("entre", "sobre", "donde", "entra")]
                hay = [p for p in claves if p.rstrip("s") in enun.lower()]
                ok = len(hay) >= max(1, len(claves) // 3)
                via = f"enunciado ({len(hay)}/{len(claves)} palabras)"
            marca = "✔" if ok else "✗"
            cl = cl or "—"
            print(f"  {marca} P{i} clave {cl} · vía {via} · {ctx}")
            if not ok:
                malos += 1
    print("LAS CLAVES ESTÁN EN SU PREGUNTA" if not malos
          else f"{malos} desalineaciones: NO ENTREGAR hasta arreglarlo")
    return malos


if __name__ == "__main__":
    sys.exit(1 if main() else 0)
