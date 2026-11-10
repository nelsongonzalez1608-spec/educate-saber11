#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Numeración final del cuaderno · 398 páginas (armado final, 10 nov 2026).

Es la única fuente de la numeración. Sale de las decisiones de Nelson del 10 nov
(tablero/decisiones.csv): apertura nueva de 6 páginas, cada área con su portada, sus 6 misiones y
su simulacro AL FINAL, cierre post-prueba de 2 páginas y una última cara con el mensaje final.

    1–6       Apertura (ap_b_1 … ap_b_6)
    7–59      Matemáticas            43 + simulacro 10
    60–112    Lectura Crítica        43 + 10
    113–165   Sociales y Ciudadanas  43 + 10
    166–214   Biología               43 + 6
    215–263   Química                43 + 6
    264–312   Física                 43 + 6
    313–395   Inglés                 77 + 6
    396–397   Cierre post-prueba (cierre_b_1, cierre_b_2)
    398       Mensaje final (cierre_b_3)

NUMERACIÓN VIEJA (la del mapa de 347): los módulos de misión (`build(pages=(…))`) y el PDF
entregado de las páginas 1–110 siguen en la numeración vieja. No se editaron: construye.py y
rehace_hojas.py traducen con `nueva()`. Un módulo NO se construye con `python3 bio1.py` (saldría
con el número viejo y taller_base lo detiene): se construye con `python3 construye.py bio1`.

    python3 paginas.py     → escribe tablero/mapa_paginas.json  {página_vieja: página_nueva}
"""
import json
import os

RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
MAPA_JSON = os.path.join(RAIZ, "tablero", "mapa_paginas.json")

TOTAL = 398
APERTURA = (1, 6)
CIERRE = (396, 397)
MENSAJE_FINAL = 398

# (clave del manifiesto, nombre, primera vieja, última vieja, primera nueva, páginas de simulacro)
AREAS = [
    ("mate", "Matemáticas", 10, 52, 7, 10),
    ("lc", "Lectura Crítica", 53, 95, 60, 10),
    ("soc", "Sociales y Ciudadanas", 96, 138, 113, 10),
    ("bio", "Biología", 139, 181, 166, 6),
    ("qui", "Química", 182, 224, 215, 6),
    ("fis", "Física", 225, 267, 264, 6),
    ("ing", "Inglés", 268, 344, 313, 6),
]


def _calcular():
    mapa, rangos, sims = {}, {}, {}
    sig = APERTURA[1] + 1
    for clave, _, a, b, ini, n_sim in AREAS:
        assert ini == sig, f"{clave}: empieza en {ini} y debería empezar en {sig}"
        for k, p in enumerate(range(a, b + 1)):
            mapa[p] = ini + k
        fin_mis = ini + (b - a)
        sims[clave] = list(range(fin_mis + 1, fin_mis + 1 + n_sim))
        rangos[clave] = (ini, fin_mis + n_sim)
        sig = fin_mis + n_sim + 1
    assert sig == CIERRE[0], f"las áreas terminan en {sig - 1} y el cierre empieza en {CIERRE[0]}"
    assert CIERRE[1] + 1 == MENSAJE_FINAL == TOTAL
    return mapa, rangos, sims


MAPA, RANGOS, SIMULACRO = _calcular()


def nueva(p_vieja):
    """Página vieja (mapa de 347) → página nueva (398). Las 9 de la apertura vieja no siguen."""
    if p_vieja not in MAPA:
        raise KeyError(f"la página vieja {p_vieja} no está en el cuaderno de 398 (apertura vieja 1–9 sale)")
    return MAPA[p_vieja]


def rango_area(clave):
    """(primera, última) del área en la numeración nueva, simulacro incluido."""
    return RANGOS[clave]


def paginas_simulacro(clave):
    return SIMULACRO[clave]


def escribir_json(ruta=MAPA_JSON):
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump({str(k): v for k, v in sorted(MAPA.items())}, f, ensure_ascii=False, indent=1)
    return ruta


if __name__ == "__main__":
    r = escribir_json()
    print(r, len(MAPA), "páginas que se conservan")
    for clave, nombre, *_ in AREAS:
        a, b = RANGOS[clave]
        s = SIMULACRO[clave]
        print(f"  {nombre:22s} {a:3d}–{b:3d}  ({b - a + 1})  simulacro {s[0]}–{s[-1]}")
    print(f"  Cierre {CIERRE[0]}–{CIERRE[1]} · mensaje final {MENSAJE_FINAL} · total {TOTAL}")
