#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""El visor como UN SOLO archivo .html: las 110 hojas van incrustadas dentro.
   Se abre con doble clic, sin carpeta al lado y sin internet (salvo la tipografía,
   que tiene su respaldo del sistema).

   Las imágenes se rehacen a menor peso que las del visor publicado: un archivo de
   30 MB no lo abre nadie dos veces.
"""
import base64, json, os, subprocess, sys

OUT = "/home/claude/libro/"
VIS = "/home/claude/visor/"
MINI = "/home/claude/visor/img_suelto/"
SALIDA = "/home/claude/libro/EDUCATE_Visor_del_cuaderno.html"

ANCHO, CALIDAD = 1000, 70

SKEL_ABRE = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
  :root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);
        padding-bottom:env(safe-area-inset-bottom,0px)}
  body{margin:0;font:14px -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       background:#F7F8FA}
  img{max-width:100%}
  [hidden]{display:none!important}
</style>
</head>
<body>
"""
SKEL_CIERRA = "\n</body>\n</html>\n"


def rehacer():
    os.makedirs(MINI, exist_ok=True)
    man = json.load(open(VIS + "manifiesto.json"))
    n = 0
    for h in man["hojas"]:
        src, dst = OUT + h["svg"] + ".svg", MINI + h["svg"] + ".jpg"
        if os.path.exists(dst) and os.path.getmtime(dst) > os.path.getmtime(src):
            continue
        png = "/tmp/claude-0/_s.png"
        subprocess.run(["rsvg-convert", "-w", str(ANCHO), "-o", png, src], check=True)
        subprocess.run(["convert", png, "-quality", str(CALIDAD), "-strip",
                        "-interlace", "Plane", dst], check=True)
        n += 1
    return man, n


def main():
    man, nuevas = rehacer()
    peso = sum(os.path.getsize(MINI + f) for f in os.listdir(MINI))
    print(f"hojas rehechas: {nuevas} · peso en disco {peso/1e6:.1f} MB")

    inc = {}
    for h in man["hojas"]:
        b = open(MINI + h["svg"] + ".jpg", "rb").read()
        inc[h["svg"]] = "data:image/jpeg;base64," + base64.b64encode(b).decode()

    cuerpo = open(VIS + "index.html", encoding="utf-8").read()
    marca = '<script id="datos" type="application/json">'
    assert marca in cuerpo, "no encuentro el bloque de datos del visor"
    incrust = ("<script>window.__IMG__=" + json.dumps(inc) + ";</script>\n")
    cuerpo = cuerpo.replace(marca, incrust + marca, 1)

    html = SKEL_ABRE + cuerpo + SKEL_CIERRA
    open(SALIDA, "w", encoding="utf-8").write(html)
    print(f"archivo suelto: {SALIDA} · {os.path.getsize(SALIDA)/1e6:.1f} MB")


if __name__ == "__main__":
    main()
