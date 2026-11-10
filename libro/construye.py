#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construye módulos de misión, CADA UNO EN SU PROPIO PROCESO.

taller_base guarda la configuración del área y la misión en memoria (configurar(),
usar_estrategias()) y cada módulo la fija al importarse. Si se importan dos módulos en el mismo
proceso, el último pisa al primero y las hojas salen con la misión equivocada (pasó el 7 nov).

    python3 construye.py soc3 soc3_icfes bio5 bio5_icfes

Numeración (armado final, 10 nov): los módulos guardan en `build(pages=(…))` la numeración VIEJA
(el mapa de 347 páginas) y no se editaron. Aquí se lee esa tupla y se traduce con
paginas.nueva() a la numeración de 398 antes de construir. taller_base comprueba que cada pie
coincida con tablero/manifiesto_hojas.json; por eso un módulo corrido solo (`python3 bio1.py`)
falla en vez de salir con el número viejo.
"""
import subprocess
import sys

CODIGO = """
import inspect, paginas, {m}
viejas = inspect.signature({m}.build).parameters["pages"].default
{m}.build(pages=tuple(paginas.nueva(p) for p in viejas))
"""

malos = []
for m in sys.argv[1:]:
    r = subprocess.run([sys.executable, "-c", CODIGO.format(m=m)], capture_output=True, text=True)
    print(("ok   " if r.returncode == 0 else "FALLA") + " " + m)
    if r.returncode:
        malos.append(m)
        print(r.stderr[-800:])
sys.exit(1 if malos else 0)
