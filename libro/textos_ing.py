#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lee TEXTOS_ING.md y devuelve lo de Inglés que la guía de clase proyecta: las 24 preguntas de
entrenamiento (texto completo, enunciado, opciones, clave verificada, fuente y notas para el profe).

Es el mismo formato de TEXTOS_BIO.md y de las secciones de Sociales de TEXTOS_GUIA_DOCENTE.md, pero
textos_soc.leer() solo acepta claves y opciones de la A a la D, y en Inglés la Parte 1 del examen trae un
banco de palabras (A–H): la Misión 1 tiene una pregunta de ocho opciones con clave F y otra de siete.
Por eso este lector es propio (textos_soc no se toca); el resto del formato es idéntico.

    from textos_ing import leer, verificar
    icfes = leer()           # {(misión, k): dict(titulo, texto, enunciado, opciones, clave, notas…)}
    verificar(icfes)         # [] si todo cuadra

verificar() cruza, pregunta por pregunta, la clave del .md con el docstring de ingN_icfes.py y con
tablero/icfes.csv, y las opciones con las listas `o=[…]` de QA…QD del módulo (leídas con ast, sin
importar el módulo: importarlo reconfigura el motor del cuaderno).
"""
import ast, csv, re

FUENTE = "/home/claude/libro/TEXTOS_ING.md"
LETRAS = "ABCDEFGH"


def _md(t):
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"\1", t)
    return re.sub(r"`([^`]+)`", r"\1", t).strip()


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
    m = re.match(r"Pregunta\s+(\d)\s*(?:\(página\s+(\d+)\))?\s*·\s*(.*?)\s*·\s*clave\s+\*\*([A-H])\*\*", cab)
    if not m:
        return None
    k, pag, tit, clave = int(m.group(1)), m.group(2), _md(m.group(3)), m.group(4)
    d = dict(titulo=tit, pagina=int(pag) if pag else None, clave=clave, texto="", enunciado="",
             opciones=[], notas=[], fuente="", competencia="", estrategia="", verificacion="", verso=False)
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
    d["texto"] = "\n\n".join(_md(" ".join(p)) for p in citas)
    resto = [ln for ln in cuerpo if not ln.strip().startswith(">")]
    modo = None
    for p in _parrafos(resto):
        primera = p[0].strip()
        if primera.startswith("**Fuente:**"):
            meta = _md(" ".join(x.strip() for x in p))
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
                mo = re.match(r"\s*([A-H])\.\s+(.*)", x)
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
    d["notas"] = [_md(n) for n in d["notas"]]
    return k, d


def leer(fuente=FUENTE):
    """{(misión, k): pregunta} de las secciones «## INGLÉS · MISIÓN n … (entrenamiento ICFES)»."""
    lineas = open(fuente, encoding="utf-8").read().split("\n")
    icfes, mis = {}, None
    for niv, cab, cuerpo in _bloques(lineas):
        if niv <= 2:
            m = re.search(r"INGLÉS\s*·\s*MISIÓN\s+(\d)", cab.upper())
            mis = int(m.group(1)) if m and "ENTRENAMIENTO ICFES" in cab.upper() else None
            continue
        if mis and cab.startswith("Pregunta"):
            r = _pregunta(cab, cuerpo)
            if r:
                icfes[(mis, r[0])] = r[1]
    return icfes


# ─────────────────────────────── verificación ───────────────────────────────
def _modulo(mis, carpeta="/home/claude/libro/"):
    """Claves del docstring de ingN_icfes.py y opciones de QA…QD (ast, sin importar el módulo)."""
    src = open(f"{carpeta}ing{mis}_icfes.py", encoding="utf-8").read()
    arbol = ast.parse(src)
    doc = ast.get_docstring(arbol) or ""
    claves = {}
    for ln in doc.split("\n"):
        m = re.match(r"\s*Q([A-D])\s*·", ln)
        if m and m.group(1) not in claves:
            letras = re.findall(r"·\s+([A-H])(?=\s|$)", ln)
            if letras:
                claves[m.group(1)] = letras[-1]
    ops = {}
    for n in arbol.body:
        if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") in ("QA", "QB", "QC", "QD"):
            for kw in n.value.keywords:
                if kw.arg == "o":
                    ops[n.targets[0].id[1]] = ast.literal_eval(kw.value)
    return claves, ops


def _csv(mis, f="/home/claude/tablero/icfes.csv"):
    filas = [r for r in csv.DictReader(open(f, encoding="utf-8-sig")) if r["mision"].strip() == f"ING M{mis}"]
    return {i + 1: r["clave"].strip() for i, r in enumerate(filas)}


def verificar(icfes=None):
    """Diferencias entre la clave del .md, la del docstring del módulo y la de icfes.csv, y entre las
    opciones del .md y las del módulo. Devuelve [] si todo cuadra."""
    icfes = icfes or leer()
    malas = []
    for mis in range(1, 7):
        claves, ops = _modulo(mis)
        tab = _csv(mis)
        for k, q in enumerate("ABCD", 1):
            v = icfes.get((mis, k))
            if not v:
                malas.append(f"M{mis} P{k}: falta en el .md")
                continue
            if claves.get(q) != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · docstring de ing{mis}_icfes.py {claves.get(q)}")
            if tab.get(k) != v["clave"]:
                malas.append(f"M{mis} P{k}: .md {v['clave']} · icfes.csv {tab.get(k)}")
            if [o.rstrip(".") for o in ops.get(q, [])] != [o.rstrip(".") for o in v["opciones"]]:
                malas.append(f"M{mis} P{k}: opciones del .md {v['opciones']} · módulo {ops.get(q)}")
            if LETRAS.index(v["clave"]) >= len(v["opciones"]):
                malas.append(f"M{mis} P{k}: la clave {v['clave']} no está entre {len(v['opciones'])} opciones")
            if not v["texto"] or not v["enunciado"] or not v["verificacion"]:
                malas.append(f"M{mis} P{k}: le falta texto, enunciado o verificación")
    return malas


if __name__ == "__main__":
    d = leer()
    for m in range(1, 7):
        for k in range(1, 5):
            v = d.get((m, k))
            if not v:
                print(f"M{m} P{k}: — FALTA —")
                continue
            print(f"M{m} P{k} · p.{v['pagina']} · clave {v['clave']} · «{v['titulo'][:44]}» · texto "
                  f"{len(v['texto'])} car. · {len(v['opciones'])} opciones · {len(v['notas'])} notas")
    malas = verificar(d)
    print("claves y opciones: todo coincide" if not malas else "\n".join(["DIFERENCIAS:"] + malas))
