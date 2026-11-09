#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Visor de avance del cuaderno (página web privada en claude.ai).

    python3 visor_avance.py <carpeta_salida>

Escribe <carpeta_salida>/index.html (con los datos del tablero incrustados) y
<carpeta_salida>/pag/NNN.jpg (una imagen de 900 px por página hecha). Las imágenes salen de los
PDF de entregables/; las páginas que todavía no tienen PDF se toman de su SVG en libro/.
Después se publica la carpeta con la herramienta Artifact (mismo index.html → misma URL).
"""
import csv, json, os, subprocess, sys, datetime

RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
ENT, TAB, LIB = (os.path.join(RAIZ, d) for d in ("entregables", "tablero", "libro"))
PDFS = [("Cuaderno_Saber11_paginas_1_a_110_v2.pdf", 1, 110, 0),
        ("Sociales_completo_paginas_96_a_138.pdf", 111, 138, 95),
        ("Biologia_completo_paginas_139_a_181.pdf", 139, 181, 138),
        ("Quimica_completo_paginas_182_a_224.pdf", 182, 224, 181),
        ("Fisica_completo_paginas_225_a_267.pdf", 225, 267, 224),
        ("Ingles_completo_paginas_268_a_344.pdf", 268, 344, 267)]


def imagenes(out, pags):
    os.makedirs(os.path.join(out, "pag"), exist_ok=True)
    for h in pags:
        n = h["pagina"]
        dst = os.path.join(out, "pag", f"{n:03d}")
        if os.path.exists(dst + ".jpg"):
            continue
        fuente = next(((f, n - d) for f, a, b, d in PDFS if a <= n <= b), None)
        if fuente:
            subprocess.run(["pdftoppm", "-f", str(fuente[1]), "-l", str(fuente[1]), "-scale-to-x", "900",
                            "-scale-to-y", "-1", "-jpeg", "-jpegopt", "quality=72", "-singlefile",
                            os.path.join(ENT, fuente[0]), dst], check=True)
        else:
            png = dst + ".png"
            subprocess.run(["rsvg-convert", "-w", "900", os.path.join(LIB, h["svg"] + ".svg"), "-o", png], check=True)
            subprocess.run(["convert", png, "-quality", "72", dst + ".jpg"], check=True)
            os.remove(png)


def _area(x):
    """Área de un hallazgo: por cómo empieza su ubicación o, si no lo dice, por la página del libro."""
    import re
    u = x["ubicacion"]
    for k, a in (("Biolog", "Biología"), ("Sociales", "Sociales y Ciudadanas"), ("SOC", "Sociales y Ciudadanas"),
                 ("Lectura", "Lectura Crítica"), ("LC", "Lectura Crítica"), ("Matem", "Matemáticas"),
                 ("Nuestro", "Nuestro (el cuaderno)"), ("Banco", "Banco ICFES"), ("Reservas", "Banco ICFES")):
        if u.startswith(k) or (" " + k) in u:
            return a
    m = re.search(r"\d+", x["pagina_libro"] or "")
    p = int(m.group()) if m else None
    if p and 265 <= p <= 335: return "Matemáticas"
    if p and 60 <= p <= 135: return "Biología"
    if p and p < 60: return "Lectura Crítica"
    return "Sociales y Ciudadanas"   # 340–410 y las dos filas del ICFES de la M5, revisadas a mano


def docente(out):
    """Planeadores (hojas como imagen) y guías de clase por área. Copia las guías a out/guias/."""
    import shutil, glob
    os.makedirs(os.path.join(out, "guias"), exist_ok=True)
    def hojas(pdf, carpeta):
        d = os.path.join(out, "doc", carpeta)
        if not os.path.isdir(d):
            os.makedirs(d)
            subprocess.run(["pdftoppm", "-scale-to-x", "900", "-scale-to-y", "-1", "-jpeg", "-jpegopt", "quality=72",
                            os.path.join(ENT, pdf), os.path.join(d, "p")], check=True)
        return [f"doc/{carpeta}/{f}" for f in sorted(os.listdir(d))]
    guias_lc = []
    for f in sorted(glob.glob(os.path.join(ENT, "guias_lecturacritica", "*.html"))):
        shutil.copy(f, os.path.join(out, "guias", os.path.basename(f)))
        n = os.path.basename(f)[:-5].replace("LC_", "").replace("_", " · ").replace("Clase", "Clase ").replace("Mision", "Misión ").replace("Devolucion", "Devolución")
        guias_lc.append(dict(f="guias/" + os.path.basename(f), t=n))
    pil = os.path.join(RAIZ, "piloto", "paquete_mision1_aprobado", "3_presentaciones")
    shutil.copy(os.path.join(pil, "Clase_viva_estudiantes.html"), os.path.join(out, "guias", "Piloto_Mate_M1_Clase_viva.html"))
    shutil.copy(os.path.join(pil, "Guia_del_encuentro_docente.html"), os.path.join(out, "guias", "Piloto_Guia_del_encuentro_docente.html"))
    return [
        dict(area="Matemáticas", planeador=dict(pdf="descargas/Planeador_Matematicas.pdf",
             hojas=hojas("EDUCATE_Planeador_Matematicas.pdf", "plan_mate")),
             guias=[dict(f="guias/Piloto_Mate_M1_Clase_viva.html", t="Piloto · Misión 1 (clase viva)"),
                    dict(f="guias/Piloto_Guia_del_encuentro_docente.html", t="Piloto · guía del encuentro docente")],
             nota="Las 8 guías de clase del área están pendientes; abajo, las del piloto aprobado."),
        dict(area="Lectura Crítica", planeador=dict(pdf="descargas/Planeador_LecturaCritica.pdf",
             hojas=hojas("EDUCATE_Planeador_LecturaCritica.pdf", "plan_lc")), guias=guias_lc),
        dict(area="Sociales y Ciudadanas", planeador=None, guias=[], guias_nota="pendientes (el cuaderno ya está completo)"),
        dict(area="Biología", planeador=None, guias=[], guias_nota="pendientes (el cuaderno ya está completo)"),
        dict(area="Química", planeador=None, guias=[], guias_nota="pendientes (el cuaderno ya está completo)"),
        dict(area="Física", planeador=None, guias=[], guias_nota="pendientes (el cuaderno ya está completo)"),
        dict(area="Inglés", planeador=None, guias=[], guias_nota="después del cuaderno del área"),
    ]


def descargas(out):
    """Archivos para descargar desde la página. El cuaderno, por área (pikepdf comparte las fuentes:
    partido con pdfseparate cada área pesaba 22 MB)."""
    import shutil, pikepdf
    d = os.path.join(out, "descargas")
    os.makedirs(d, exist_ok=True)
    v2 = pikepdf.open(os.path.join(ENT, "Cuaderno_Saber11_paginas_1_a_110_v2.pdf"))
    for nom, a, b in (("Cuaderno_01_Apertura_p1-9.pdf", 1, 9), ("Cuaderno_02_Matematicas_p10-52.pdf", 10, 52),
                      ("Cuaderno_03_LecturaCritica_p53-95.pdf", 53, 95)):
        n = pikepdf.new()
        for i in range(a - 1, b):
            n.pages.append(v2.pages[i])
        n.remove_unreferenced_resources()
        n.save(os.path.join(d, nom), compress_streams=True, object_stream_mode=pikepdf.ObjectStreamMode.generate)
    copias = [("Sociales_completo_paginas_96_a_138.pdf", "Cuaderno_04_Sociales_p96-138.pdf"),
              ("Biologia_completo_paginas_139_a_181.pdf", "Cuaderno_05_Biologia_p139-181.pdf"),
              ("Quimica_completo_paginas_182_a_224.pdf", "Cuaderno_06_Quimica_p182-224.pdf"),
              ("Fisica_completo_paginas_225_a_267.pdf", "Cuaderno_07_Fisica_p225-267.pdf"),
              ("Ingles_completo_paginas_268_a_344.pdf", "Cuaderno_08_Ingles_p268-344.pdf"),
              ("EDUCATE_Planeador_Matematicas.pdf", "Planeador_Matematicas.pdf"),
              ("EDUCATE_Planeador_LecturaCritica.pdf", "Planeador_LecturaCritica.pdf"),
              ("EDUCATE_Informe_hallazgos.pdf", "Informe_hallazgos_6nov.pdf"),
              # la matriz .xlsx no se puede servir desde la página (solo PDF, imágenes, HTML…): queda en GitHub
              ("EDUCATE_Estado_del_proyecto.pdf", "Estado_del_proyecto_6nov.pdf"),
              ("EDUCATE_Muestra_reunion.pdf", "Muestra_reunion.pdf")]
    for a, b in copias:
        if os.path.exists(os.path.join(ENT, a)):
            shutil.copy(os.path.join(ENT, a), os.path.join(d, b))
    titulos = {"Cuaderno_01": "Cuaderno · Apertura (páginas 1–9)", "Cuaderno_02": "Cuaderno · Matemáticas (10–52)",
               "Cuaderno_03": "Cuaderno · Lectura Crítica (53–95)", "Cuaderno_04": "Cuaderno · Sociales y Ciudadanas (96–138)",
               "Cuaderno_05": "Cuaderno · Biología (139–181)", "Cuaderno_06": "Cuaderno · Química (182–224)", "Cuaderno_07": "Cuaderno · Física (225–267)", "Cuaderno_08": "Cuaderno · Inglés (268–344)", "Planeador_Matematicas": "Planeador del docente · Matemáticas",
               "Planeador_LecturaCritica": "Planeador del docente · Lectura Crítica",
               "Informe_hallazgos_6nov": "Informe de hallazgos del libro (versión del 6 nov)",
               "Matriz_del_proyecto_6nov": "Matriz del proyecto (versión del 6 nov)",
               "Estado_del_proyecto_6nov": "Estado del proyecto (versión del 6 nov)", "Muestra_reunion": "Muestra para la reunión"}
    out_l = []
    for f in sorted(os.listdir(d)):
        clave = next((k for k in titulos if f.startswith(k)), f)
        out_l.append(dict(f="descargas/" + f, t=titulos.get(clave, f), mb=round(os.path.getsize(os.path.join(d, f)) / 1e6, 1)))
    return out_l


def main(out):
    man = sorted(json.load(open(os.path.join(TAB, "manifiesto_hojas.json"), encoding="utf-8")),
                 key=lambda h: h["pagina"])
    imagenes(out, man)
    leer = lambda f: list(csv.DictReader(open(os.path.join(TAB, f), encoding="utf-8-sig")))
    h = leer("hallazgos.csv")
    datos = dict(pags=[dict(n=x["pagina"], svg=x["svg"], rol=x["rol"], tit=x["titulo"], m=x.get("mision"))
                       for x in man],
                 mis={r["mision"]: dict(comp=r["componente"], est=r["estrategias"]) for r in leer("misiones.csv")},
                 hallazgos=[dict(n=int(x["n"]), area=_area(x), ubic=x["ubicacion"], pag=x["pagina_libro"],
                                 que=x["que_pasa"], efecto=x["efecto"], sev=x["severidad"], estado=x["estado"])
                            for x in h],
                 instrumentos=len(leer("instrumentos.csv")), icfes=len(leer("icfes.csv")),
                 docente=docente(out), descargas=descargas(out))
    # de qué PDF de área sale cada página (para armar en la página PDF por misión, por página o completos)
    import re as _re
    datos["fuentes"] = [dict(f=d["f"], a=int(m.group(1)), b=int(m.group(2)))
                        for d in datos["descargas"]
                        for m in [_re.search(r"Cuaderno_\d\d_[A-Za-z]+_p(\d+)-(\d+)\.pdf$", d["f"])] if m]
    p = open(os.path.join(LIB, "visor_avance_plantilla.html"), encoding="utf-8").read()
    p = p.replace("__DATOS__", json.dumps(datos, ensure_ascii=False))
    p = p.replace("__FECHA__", datetime.date.today().strftime("%d/%m/%Y"))
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(p)
    print(len(man), "páginas en el visor")


if __name__ == "__main__":
    main(sys.argv[1])
