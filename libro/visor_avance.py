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
# armado final (10 nov): un solo PDF con las 398 páginas; (archivo, primera, última, desplazamiento)
PDFS = [("Cuaderno_Saber11_completo_398_paginas.pdf", 1, 398, 0)]
# los PDF por sección (arma_pdf.PARTES): se copian tal cual a descargas/
CUADERNO = [("Cuaderno_01_Apertura_p1-6.pdf", "Apertura", 1, 6),
            ("Cuaderno_02_Matematicas_p7-59.pdf", "Matemáticas", 7, 59),
            ("Cuaderno_03_LecturaCritica_p60-112.pdf", "Lectura Crítica", 60, 112),
            ("Cuaderno_04_Sociales_p113-165.pdf", "Sociales y Ciudadanas", 113, 165),
            ("Cuaderno_05_Biologia_p166-214.pdf", "Biología", 166, 214),
            ("Cuaderno_06_Quimica_p215-263.pdf", "Química", 215, 263),
            ("Cuaderno_07_Fisica_p264-312.pdf", "Física", 264, 312),
            ("Cuaderno_08_Ingles_p313-395.pdf", "Inglés", 313, 395),
            ("Cuaderno_09_Cierre_p396-398.pdf", "Cierre", 396, 398)]


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


_AREA_VERIFICADA = None
_SIGLA = {"MAT": "Matemáticas", "LC": "Lectura Crítica", "SOC": "Sociales y Ciudadanas", "BIO": "Biología",
          "QUI": "Química", "FIS": "Física", "ING": "Inglés"}


def _area(x):
    """Área de un hallazgo. Primero la que verificó el informe para la editorial (informe_editorial_datos.py,
    10 nov); si no está, por cómo empieza la ubicación; si tampoco, por la página del libro."""
    import re
    global _AREA_VERIFICADA
    if _AREA_VERIFICADA is None:
        try:
            src = open(os.path.join(LIB, "informe_editorial_datos.py"), encoding="utf-8").read()
            _AREA_VERIFICADA = {int(n): _SIGLA.get(a, a) for n, a in re.findall(r'\bh\(\s*(\d+)\s*,\s*"([^"]+)"', src)}
        except OSError:
            _AREA_VERIFICADA = {}
    try:
        n = int(x["n"])
    except (KeyError, ValueError):
        n = None
    if n in _AREA_VERIFICADA:
        return _AREA_VERIFICADA[n]
    # filas sin área en la ubicación, revisadas a mano por su bloque en el tablero (10 nov)
    A_MANO = {81: "Sociales y Ciudadanas", 82: "Sociales y Ciudadanas", 199: "Química", 200: "Química",
              211: "Química", 212: "Química", 213: "Química", 251: "Física", 258: "Física"}
    if n in A_MANO:
        return A_MANO[n]
    u = x["ubicacion"]
    for k, a in (("Nuestro", "Nuestro (el cuaderno)"), ("Banco", "Banco ICFES"), ("Reservas", "Banco ICFES"),
                 ("Hojas de simulacro", "Nuestro (el cuaderno)"), ("Fuentes", "Fuentes y libro"),
                 ("Inglés", "Inglés"), ("Química", "Química"), ("Física", "Física"), ("Biolog", "Biología"),
                 ("Sociales", "Sociales y Ciudadanas"), ("SOC", "Sociales y Ciudadanas"),
                 ("Lectura", "Lectura Crítica"), ("LC ", "Lectura Crítica"), ("Matem", "Matemáticas")):
        if u.startswith(k) or (" " + k) in u:
            return a
    m = re.search(r"\d+", x["pagina_libro"] or "")
    p = int(m.group()) if m else None
    if p and 265 <= p <= 335: return "Matemáticas"
    if p and 60 <= p <= 135: return "Biología"
    if p and p < 60: return "Lectura Crítica"
    if p and 340 <= p <= 410: return "Sociales y Ciudadanas"
    return "Sin área"


def docente(out):
    """Planeadores (hojas como imagen) y guías de clase por área. Copia las guías a out/guias/."""
    import shutil, glob
    os.makedirs(os.path.join(out, "guias"), exist_ok=True)
    def hojas(pdf, carpeta):
        """Desde el 10 nov el planeador se ve como PDF dentro de la página (el tablero no admite más
        de 511 archivos): ya no se generan imágenes por hoja. Devuelve el número de hojas."""
        import pikepdf
        with pikepdf.open(os.path.join(ENT, pdf)) as p:
            return len(p.pages)
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
    guias_soc = []
    for f in sorted(glob.glob(os.path.join(ENT, "guias_sociales", "*.html"))):
        shutil.copy(f, os.path.join(out, "guias", os.path.basename(f)))
        n = os.path.basename(f)[:-5].replace("SOC_", "").replace("_", " · ").replace("Clase", "Clase ").replace("Mision", "Misión ").replace("Devolucion", "Devolución")
        guias_soc.append(dict(f="guias/" + os.path.basename(f), t=n))
    def guias_de(carpeta, prefijo):
        res = []
        for f in sorted(glob.glob(os.path.join(ENT, carpeta, "*.html"))):
            shutil.copy(f, os.path.join(out, "guias", os.path.basename(f)))
            n = os.path.basename(f)[:-5].replace(prefijo, "").replace("_", " · ").replace("Clase", "Clase ").replace("Mision", "Misión ").replace("Devolucion", "Devolución")
            res.append(dict(f="guias/" + os.path.basename(f), t=n))
        return res
    guias_mat, guias_bio = guias_de("guias_matematicas", "MAT_"), guias_de("guias_biologia", "BIO_")
    guias_qui, guias_fis, guias_ing = (guias_de("guias_quimica", "QUI_"), guias_de("guias_fisica", "FIS_"),
                                       guias_de("guias_ingles", "ING_"))
    pil = os.path.join(RAIZ, "piloto", "paquete_mision1_aprobado", "3_presentaciones")
    shutil.copy(os.path.join(pil, "Clase_viva_estudiantes.html"), os.path.join(out, "guias", "Piloto_Mate_M1_Clase_viva.html"))
    shutil.copy(os.path.join(pil, "Guia_del_encuentro_docente.html"), os.path.join(out, "guias", "Piloto_Guia_del_encuentro_docente.html"))
    return [
        dict(area="Matemáticas", planeador=dict(pdf="descargas/Planeador_Matematicas.pdf",
             hojas=hojas("EDUCATE_Planeador_Matematicas.pdf", "plan_mate")),
             guias=guias_mat + [dict(f="guias/Piloto_Mate_M1_Clase_viva.html", t="Piloto · Misión 1 (clase viva)"),
                    dict(f="guias/Piloto_Guia_del_encuentro_docente.html", t="Piloto · guía del encuentro docente")]),
        dict(area="Lectura Crítica", planeador=dict(pdf="descargas/Planeador_LecturaCritica.pdf",
             hojas=hojas("EDUCATE_Planeador_LecturaCritica.pdf", "plan_lc")), guias=guias_lc),
        dict(area="Sociales y Ciudadanas", planeador=dict(pdf="descargas/Planeador_Sociales.pdf",
             hojas=hojas("EDUCATE_Planeador_Sociales.pdf", "plan_soc")), guias=guias_soc),
        dict(area="Biología", planeador=dict(pdf="descargas/Planeador_Biologia.pdf",
             hojas=hojas("EDUCATE_Planeador_Biologia.pdf", "plan_bio")), guias=guias_bio),
        dict(area="Química", planeador=dict(pdf="descargas/Planeador_Quimica.pdf",
             hojas=hojas("EDUCATE_Planeador_Quimica.pdf", "plan_qui")), guias=guias_qui),
        dict(area="Física", planeador=dict(pdf="descargas/Planeador_Fisica.pdf",
             hojas=hojas("EDUCATE_Planeador_Fisica.pdf", "plan_fis")), guias=guias_fis),
        dict(area="Inglés", planeador=dict(pdf="descargas/Planeador_Ingles.pdf",
             hojas=hojas("EDUCATE_Planeador_Ingles.pdf", "plan_ing")), guias=guias_ing),
    ]


def descargas(out):
    """Archivos para descargar desde la página. El cuaderno, por área (pikepdf comparte las fuentes:
    partido con pdfseparate cada área pesaba 22 MB)."""
    import shutil
    d = os.path.join(out, "descargas")
    os.makedirs(d, exist_ok=True)
    copias = [(f, f) for f, *_ in CUADERNO] + [
              ("EDUCATE_Planeador_Matematicas.pdf", "Planeador_Matematicas.pdf"),
              ("EDUCATE_Planeador_LecturaCritica.pdf", "Planeador_LecturaCritica.pdf"),
              ("EDUCATE_Planeador_Sociales.pdf", "Planeador_Sociales.pdf"),
              ("EDUCATE_Planeador_Biologia.pdf", "Planeador_Biologia.pdf"),
              ("EDUCATE_Planeador_Quimica.pdf", "Planeador_Quimica.pdf"),
              ("EDUCATE_Planeador_Fisica.pdf", "Planeador_Fisica.pdf"),
              ("EDUCATE_Planeador_Ingles.pdf", "Planeador_Ingles.pdf"),
              ("EDUCATE_Informe_hallazgos_editorial_10nov.pdf", "Informe_hallazgos_editorial_10nov.pdf"),
              ("EDUCATE_Hallazgos_internos_10nov.pdf", "Hallazgos_internos_10nov.pdf"),
              ("EDUCATE_Documento_maestro_metodologia.pdf", "Documento_maestro_metodologia.pdf"),
              # la matriz .xlsx no se puede servir desde la página (solo PDF, imágenes, HTML…): queda en GitHub
              ("EDUCATE_Estado_del_proyecto.pdf", "Estado_del_proyecto_6nov.pdf"),
              ("EDUCATE_Muestra_reunion.pdf", "Muestra_reunion.pdf")]
    for a, b in copias:
        if os.path.exists(os.path.join(ENT, a)):
            shutil.copy(os.path.join(ENT, a), os.path.join(d, b))
    titulos = {f[:11]: f"Cuaderno · {n} (páginas {a}–{b})" for f, n, a, b in CUADERNO}
    titulos.update({"Planeador_Matematicas": "Planeador del docente · Matemáticas",
               "Planeador_LecturaCritica": "Planeador del docente · Lectura Crítica",
               "Planeador_Quimica": "Planeador del docente · Química",
               "Informe_hallazgos_editorial_10nov": "Informe de hallazgos para la editorial (10 nov)",
               "Hallazgos_internos_10nov": "Hallazgos internos de EDUCATE (10 nov)",
               "Documento_maestro_metodologia": "Documento maestro de metodología (borrador para aprobar)",
               "Planeador_Fisica": "Planeador del docente · Física",
               "Planeador_Ingles": "Planeador del docente · Inglés",
               "Planeador_Sociales": "Planeador del docente · Sociales y Ciudadanas",
               "Planeador_Biologia": "Planeador del docente · Biología",
               "Guias_LecturaCritica": "Las 8 presentaciones de Lectura Crítica (.zip)",
               "Guias_Sociales": "Las 8 presentaciones de Sociales y Ciudadanas (.zip)",
               "Informe_hallazgos_6nov": "Informe de hallazgos del libro (versión del 6 nov)",
               "Matriz_del_proyecto_6nov": "Matriz del proyecto (versión del 6 nov)",
               "Estado_del_proyecto_6nov": "Estado del proyecto (versión del 6 nov)", "Muestra_reunion": "Muestra para la reunión"})
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
