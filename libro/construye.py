#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Construye módulos de misión, CADA UNO EN SU PROPIO PROCESO.

taller_base guarda la configuración del área y la misión en memoria (configurar(),
usar_estrategias()) y cada módulo la fija al importarse. Si se importan dos módulos en el mismo
proceso, el último pisa al primero y las hojas salen con la misión equivocada (pasó el 7 nov).

    python3 construye.py soc3 soc3_icfes bio5 bio5_icfes
"""
import subprocess
import sys

malos = []
for m in sys.argv[1:]:
    r = subprocess.run([sys.executable, "-c", f"import {m}; {m}.build()"], capture_output=True, text=True)
    print(("ok   " if r.returncode == 0 else "FALLA") + " " + m)
    if r.returncode:
        malos.append(m)
        print(r.stderr[-800:])
sys.exit(1 if malos else 0)
