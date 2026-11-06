#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Manifiesto del visor: qué página es cada hoja, a qué misión pertenece y de qué área.
   De aquí salen el JSON del visor y los nombres de los JPEG. Una sola verdad con build_libro.
"""
import csv, json, os, subprocess, glob

OUT = "/home/claude/libro/"
IMG = "/home/claude/visor/img/"
TAB = "/home/claude/tablero/"

AREAS = [
    # clave, nombre, color, portada svg, primera pág., última pág., prefijos de misión
    ("mate", "Matemáticas",          "#1F4E8C", "ap10_mate", 10,  52,
     ["m1", "m2", "m3", "m4", "m5", "m6"]),
    ("lc",   "Lectura Crítica",      "#A82424", "ap53_lc",   53,  95,
     ["lc1", "lc2", "lc3", "lc4", "lc5", "lc6"]),
    ("soc",  "Sociales y Ciudadanas","#C9821B", "ap96_soc",  96,  138,
     ["soc1", "soc2"]),
    ("nat",  "Ciencias Naturales",   "#30843C", None,        139, 181, []),
    ("fis",  "Física",               "#5B3E96", None,        182, 224, []),
    ("ing",  "Inglés",               "#1BA0A8", None,        225, 267, []),
]

APERTURA = [("ap01_portada", 1, "Portada del cuaderno"),
            ("ap02_intro1", 2, "Esto no es un libro de respuestas"),
            ("ap03_intro2", 3, "Lo que sí es"),
            ("ap04_metas1", 4, "Dónde estoy hoy"),
            ("ap05_metas2", 5, "A dónde quiero llegar"),
            ("ap06_encontrar1", 6, "Cómo se lee este cuaderno"),
            ("ap07_encontrar2", 7, "Las seis áreas"),
            ("ap08_psico1", 8, "El día de la prueba"),
            ("ap09_psico2", 9, "Mi pacto conmigo")]

ORDEN_MIS = ["t1", "t2", "i1", "t3", "t4", "t5", "i2"]
ROL = {"t1": "Taller", "t2": "Taller", "t3": "Taller", "t4": "Taller", "t5": "Taller",
       "i1": "Entrenamiento ICFES", "i2": "Entrenamiento ICFES"}


def paginas_mision(pref):
    """Las siete páginas de una misión, en el orden en que se imprimen."""
    mod = __import__(pref if pref.startswith("lc") or pref.startswith("soc") else pref)
    return None  # no se usa: las páginas vienen del CSV de misiones


def leer_misiones():
    with open(TAB + "misiones.csv", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


# Primera página de cada misión. Es el mismo número que build_libro.py y build_mate.py
# le pasan a build(pages=...): la misión ocupa esa página y las seis siguientes.
BASE = {"m1": 11, "m2": 18, "m3": 25, "m4": 32, "m5": 39, "m6": 46,
        "lc1": 54, "lc2": 61, "lc3": 68, "lc4": 75, "lc5": 82, "lc6": 89,
        "soc1": 97, "soc2": 104}


def primera_pagina(pref):
    if not os.path.exists(OUT + pref + "_t1.svg"):
        return None
    return BASE.get(pref)


def manifiesto():
    mis_csv = {m["mision"]: m for m in leer_misiones()}
    hojas, areas = [], []

    for n, (svg, pag, titulo) in enumerate(APERTURA):
        hojas.append({"svg": svg, "pagina": pag, "area": "ap", "mision": None,
                      "rol": "Apertura", "titulo": titulo})

    for clave, nombre, color, portada, p0, p1, prefs in AREAS:
        mis = []
        if portada and os.path.exists(OUT + portada + ".svg"):
            hojas.append({"svg": portada, "pagina": p0, "area": clave, "mision": None,
                          "rol": "Portada de área", "titulo": "Portada · " + nombre})
        for i, pref in enumerate(prefs, 1):
            p1_ = primera_pagina(pref)
            if p1_ is None:
                mis.append({"n": i, "pref": pref, "estado": "pendiente", "hojas": []})
                continue
            base = p1_
            pags = [base, base + 1, base + 2, base + 3, base + 4, base + 5, base + 6]
            # orden impreso: t1 t2 i1 t3 t4 t5 i2  ->  páginas consecutivas
            lst = []
            for j, suf in enumerate(ORDEN_MIS):
                svg = f"{pref}_{suf}"
                if not os.path.exists(OUT + svg + ".svg"):
                    continue
                hojas.append({"svg": svg, "pagina": pags[j], "area": clave, "mision": i,
                              "rol": ROL[suf], "titulo": f"{nombre} · Misión {i} · {ROL[suf]}"})
                lst.append(svg)
            # busca la fila del CSV. Matemáticas va sin prefijo; las demás con el suyo.
            etiqueta = {"mate": "", "lc": "LC ", "soc": "SOC "}.get(clave, "") + f"Misión {i}"
            fila = mis_csv.get(etiqueta)
            mis.append({"n": i, "pref": pref, "estado": "listo", "hojas": lst,
                        "paginas": f"{pags[0]}–{pags[6]}",
                        "componente": (fila or {}).get("componente", ""),
                        "estrategias": (fila or {}).get("estrategias", ""),
                        "icfes": (fila or {}).get("icfes", "")})
        areas.append({"clave": clave, "nombre": nombre, "color": color,
                      "rango": f"{p0}–{p1}", "misiones": mis,
                      "total": 42 if clave != "ap" else 9})

    for n, (svg, pag, titulo) in enumerate(APERTURA):
        pass
    return {"hojas": hojas, "areas": areas}


def render(hojas, ancho=1100, calidad=74):
    os.makedirs(IMG, exist_ok=True)
    hechas = 0
    for h in hojas:
        dst = IMG + h["svg"] + ".jpg"
        src = OUT + h["svg"] + ".svg"
        if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src):
            continue
        png = "/tmp/claude-0/_v.png"
        subprocess.run(["rsvg-convert", "-w", str(ancho), "-o", png, src], check=True)
        subprocess.run(["convert", png, "-quality", str(calidad), "-strip", dst], check=True)
        hechas += 1
    return hechas


if __name__ == "__main__":
    m = manifiesto()
    print(len(m["hojas"]), "hojas en el manifiesto")
    for a in m["areas"]:
        listas = sum(len(x["hojas"]) for x in a["misiones"])
        print(f"  {a['nombre']:22s} {a['rango']:9s} {listas:3d} págs de misión")
    n = render(m["hojas"])
    print("imágenes nuevas:", n)
    os.makedirs("/home/claude/visor", exist_ok=True)
    json.dump(m, open("/home/claude/visor/manifiesto.json", "w"),
              ensure_ascii=False, indent=1)
    tot = sum(os.path.getsize(IMG + f) for f in os.listdir(IMG))
    print(f"peso de las imágenes: {tot/1e6:.1f} MB en {len(os.listdir(IMG))} archivos")
