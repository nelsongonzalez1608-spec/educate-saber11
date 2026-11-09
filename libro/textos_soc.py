#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lee TEXTOS_GUIA_DOCENTE.md y devuelve lo de Sociales y Ciudadanas que la guía de clase
   proyecta: las 24 preguntas ICFES (texto completo, enunciado, opciones, clave verificada,
   fuente y notas para el profe), las advertencias previas y las notas del taller.

   Formato que lee (el de las secciones de Sociales desde el 9 nov):

     ## SOCIALES · MISIÓN n · páginas p y q (entrenamiento ICFES)
     ### Pregunta k (página p) · Título · clave **X**
     **Fuente:** … **Competencia:** … **Estrategia del cuaderno:** e · nombre.
     **Formato:** verso                      (opcional: respeta los saltos de línea)
     > texto completo, en párrafos separados por «>» vacío
     **Pregunta:** enunciado
     **Opciones:**
     A. …   B. …   C. …   D. …
     **Verificada resolviéndola:** por qué es esa clave
     **Lo que el profesor debe hacer notar**
     - nota
     - nota

     ## Lo que hay que trabajar antes del taller · preguntas 4, 5 y 6     (o «en el taller»)
     ### Título del saber
     cuerpo                                                  → notas del taller por pregunta

     ## ADVERTENCIA PREVIA PARA EL PROFESOR                 → advertencia de la misión

   Uso:
       from textos_soc import leer
       icfes, advertencias, taller = leer()
       icfes[(3, 1)]["clave"]        → "A"
       icfes[(3, 1)]["texto"]        → el caso completo
       taller[(2, 4)]                → [dict(titulo=…, texto=…), …]

   `leer(area=…)` sirve para otra área que escriba sus secciones con el mismo formato.
   Las claves de aquí son las verificadas resolviendo la pregunta; `verificar()` las cruza con
   los módulos socN_icfes.py (M3 a M6) y con tablero/icfes.csv (las seis misiones).
"""
import csv, os, re

FUENTE = "/home/claude/libro/TEXTOS_GUIA_DOCENTE.md"
OTRAS = ("LECTURA CRÍTICA", "MATEMÁTICAS", "CIENCIAS", "BIOLOGÍA", "QUÍMICA", "FÍSICA", "INGLÉS",
         "SOCIALES")


def _md(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"\1", t)
    return re.sub(r"`([^`]+)`", r"\1", t).strip()


def _numeros(cab):
    m = re.search(r"[Pp]reguntas?\s+([\d\s,y]+)", cab)
    return [int(x) for x in re.findall(r"\d+", m.group(1))] if m else []


def _bloques(lineas):
    out, cab, niv, cuerpo = [], None, 0, []
    for ln in lineas:
        m = re.match(r"^(#{1,3}) (.*)", ln)
        if m:
            if cab is not None:
                out.append((niv, cab, cuerpo))
            niv, cab, cuerpo = len(m.group(1)), m.group(2), []
        else:
            cuerpo.append(ln)
    if cab is not None:
        out.append((niv, cab, cuerpo))
    return out


def _parrafos(lineas):
    """Agrupa líneas en párrafos separados por líneas vacías."""
    ps, cur = [], []
    for ln in lineas:
        if ln.strip():
            cur.append(ln)
        elif cur:
            ps.append(cur); cur = []
    if cur:
        ps.append(cur)
    return ps


def _pregunta(cab, cuerpo):
    m = re.match(r"Pregunta\s+(\d)\s*(?:\(página\s+(\d+)\))?\s*·\s*(.*?)\s*·\s*clave\s+\*\*([A-D])\*\*", cab)
    if not m:
        return None
    k, pag, tit, clave = int(m.group(1)), m.group(2), _md(m.group(3)), m.group(4)
    d = dict(titulo=tit, pagina=int(pag) if pag else None, clave=clave, texto="", enunciado="",
             opciones=[], notas=[], fuente="", competencia="", estrategia="", verificacion="",
             verso=False, remite="")
    # el texto citado: líneas «>», párrafos separados por «>» vacío
    citas, par = [], []
    for ln in cuerpo:
        s = ln.strip()
        if s.startswith(">"):
            t = s[1:].strip()
            if t:
                par.append(t)
            elif par:
                citas.append(par); par = []
    if par:
        citas.append(par)
    d["verso"] = any(re.match(r"\*\*Formato:\*\*\s*verso", ln.strip()) for ln in cuerpo)
    junta = "\n" if d["verso"] else " "
    d["texto"] = "\n\n".join(_md(junta.join(p)) for p in citas)

    resto = [ln for ln in cuerpo if not ln.strip().startswith(">")]
    modo = None
    for p in _parrafos(resto):
        primera = p[0].strip()
        if primera.startswith("**Fuente:**"):
            meta = _md(" ".join(x.strip() for x in p))
            meta = re.sub(r"Formato:\s*verso", "", meta).strip()
            f = re.search(r"Fuente:\s*(.*?)(?=\s*Competencia:|$)", meta)
            c = re.search(r"Competencia:\s*(.*?)(?=\s*Estrategia del cuaderno:|$)", meta)
            e = re.search(r"Estrategia del cuaderno:\s*(.*)$", meta)
            d["fuente"] = f.group(1).strip().rstrip(".") if f else ""
            d["competencia"] = c.group(1).strip().rstrip(".") if c else ""
            d["estrategia"] = e.group(1).strip().rstrip(".") if e else ""
            modo = None
        elif primera.startswith("**Pregunta:**"):
            d["enunciado"] = _md(" ".join(x.strip() for x in p).replace("**Pregunta:**", ""))
            modo = None
        elif primera.startswith("**Opciones:**"):
            modo = "op"
            for x in p[1:]:
                mo = re.match(r"\s*([A-D])\.\s+(.*)", x)
                if mo:
                    d["opciones"].append(_md(mo.group(2)))
        elif primera.startswith("**Verificada"):
            d["verificacion"] = _md(re.sub(r"^\*\*Verificada[^*]*\*\*", "", " ".join(x.strip() for x in p)))
            modo = None
        elif primera.startswith("**Lo que el profesor"):
            modo = "notas"
        elif modo == "notas":
            for x in p:
                if x.strip().startswith("- "):
                    d["notas"].append(x.strip()[2:])
                elif d["notas"]:
                    d["notas"][-1] += " " + x.strip()
        elif modo == "op":
            for x in p:
                mo = re.match(r"\s*([A-D])\.\s+(.*)", x)
                if mo:
                    d["opciones"].append(_md(mo.group(2)))
    d["notas"] = [_md(n) for n in d["notas"]]
    return k, d


def leer(area="SOCIALES", fuente=FUENTE):
    lineas = open(fuente, encoding="utf-8").read().split("\n")
    icfes, advert, taller = {}, {}, {}
    mis, dentro, seccion, nums_taller = None, False, None, []
    for niv, cab, cuerpo in _bloques(lineas):
        up = cab.upper()
        if niv <= 2:
            otra = any(o in up for o in OTRAS if o != area)
            if area in up:
                dentro = True
                m = re.search(r"MISIÓN\s+(\d)", up)
                if m:
                    mis = int(m.group(1))
                seccion = "icfes" if "ENTRENAMIENTO ICFES" in up and m else None
                nums_taller = []
                continue
            if otra:
                dentro, seccion = False, None
                continue
            if not dentro:
                continue
            if "ADVERTENCIA PREVIA" in up and mis:
                advert[mis] = _md("\n".join(cuerpo)).rstrip("-").strip()
                seccion = None
            elif "TALLER" in up and _numeros(cab):
                seccion, nums_taller = "taller", _numeros(cab)
            else:
                seccion = None
            continue
        if not dentro or mis is None:
            continue
        if seccion == "icfes" and cab.startswith("Pregunta"):
            r = _pregunta(cab, cuerpo)
            if r:
                icfes[(mis, r[0])] = r[1]
        elif seccion == "taller":
            txt = "\n\n".join(_md(" ".join(x.strip() for x in p))
                               for p in _parrafos([ln for ln in cuerpo if ln.strip() != "---"]))
            for n in nums_taller:
                taller.setdefault((mis, n), []).append(dict(titulo=_md(cab.replace("⚠", "")), texto=txt))
    return icfes, advert, taller


# ─────────────────────────────── verificación ───────────────────────────────
def _modulo_icfes(mis):
    """Las claves del docstring de socN_icfes.py (QA·A … o QA · N.º 87 · C) y los enunciados."""
    f = f"/home/claude/libro/soc{mis}_icfes.py"
    if not os.path.exists(f):
        return None
    doc = open(f, encoding="utf-8").read()[:4000]
    claves = {}
    for q, k in re.findall(r"Q([A-D])\s*(?:·[^·\n]*?)?·\s*([A-D])\b", doc):
        claves.setdefault("ABCD".index(q) + 1, k)
    return claves


def _csv(mis):
    f = "/home/claude/tablero/icfes.csv"
    filas = [r for r in csv.DictReader(open(f, encoding="utf-8-sig"))
             if r["mision"].strip() in (f"SOC M{mis}", f"SOC Misión {mis}")]
    return {i + 1: r["clave"].strip() for i, r in enumerate(filas)}


def verificar(icfes=None):
    """Lista de diferencias entre la clave del .md, la del módulo y la de tablero/icfes.csv."""
    icfes = icfes or leer()[0]
    malas = []
    for mis in range(1, 7):
        mod, tab = _modulo_icfes(mis), _csv(mis)
        for k in range(1, 5):
            v = icfes.get((mis, k))
            if not v:
                malas.append(f"M{mis} P{k}: falta en el .md")
                continue
            if len(v["opciones"]) != 4:
                malas.append(f"M{mis} P{k}: {len(v['opciones'])} opciones")
            if mod is not None and mod.get(k) != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · módulo {mod.get(k)}")
            if tab.get(k) != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · icfes.csv {tab.get(k)}")
    return malas


if __name__ == "__main__":
    d, adv, tal = leer()
    for m in range(1, 7):
        for k in range(1, 5):
            v = d.get((m, k))
            if not v:
                print(f"M{m} P{k}: — FALTA —")
                continue
            print(f"M{m} P{k} · p.{v['pagina']} · clave {v['clave']} · «{v['titulo'][:40]}» · "
                  f"texto {len(v['texto'])} car. · {len(v['opciones'])} opciones · {len(v['notas'])} notas")
    print("advertencias previas:", sorted(adv))
    print("notas del taller:", sorted(tal))
    malas = verificar(d)
    print("claves: todo coincide" if not malas else "\n".join(["DIFERENCIAS:"] + malas))
