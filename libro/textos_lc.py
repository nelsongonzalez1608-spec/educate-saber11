#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lee TEXTOS_GUIA_DOCENTE.md y devuelve, por misión y pregunta ICFES de Lectura Crítica,
   el texto que se proyecta y lo que el profesor tiene que hacer notar.

   El archivo no es uniforme: las misiones 1 a 5 usan «## LECTURA CRÍTICA · MISIÓN n ·
   página p (pregunta k del entrenamiento)» y la 6 usa subtítulos «### Pregunta k (página p)».
   La misión 2 no repite el texto de Savater: lo remite a la misión 1.
"""
import os, re

FUENTE = "/home/claude/libro/TEXTOS_GUIA_DOCENTE.md"


def _numeros(cab):
    """«preguntas 1 y 2» → [1, 2] · «pregunta 3» → [3]"""
    m = re.search(r"[Pp]reguntas?\s+([\d\s,y]+)", cab)
    if not m:
        return []
    return [int(x) for x in re.findall(r"\d+", m.group(1))]


def leer():
    lineas = open(FUENTE, encoding="utf-8").read().split("\n")
    # bloques: (nivel, cabecera, cuerpo)
    bloques, cab, niv, cuerpo = [], None, 0, []
    for ln in lineas:
        m = re.match(r"^(#{1,3}) (.*)", ln)
        if m:
            if cab is not None:
                bloques.append((niv, cab, cuerpo))
            niv, cab, cuerpo = len(m.group(1)), m.group(2), []
        else:
            cuerpo.append(ln)
    if cab is not None:
        bloques.append((niv, cab, cuerpo))

    out = {}                  # (misión, pregunta) → dict(titulo, texto, notas, advertencia)
    advert = {}               # misión → texto de la advertencia previa
    mis, en_lc, titulo = None, False, ""
    pendientes = []           # bloques de pregunta cuyo texto viene en un ### posterior
    for niv, cab, cuerpo in bloques:
        up = cab.upper()
        if niv <= 2:
            if "LECTURA CRÍTICA" in up:
                en_lc = True
                m = re.search(r"MISIÓN\s+(\d)", up)
                mis = int(m.group(1)) if m else mis
            elif "SOCIALES" in up or "CIENCIAS" in up or "MATEMÁTICAS" in up:
                en_lc = False
            elif "ADVERTENCIA PREVIA" in up and "MISIÓN" in up:
                m = re.search(r"MISIÓN\s+(\d)", up)
                if m and en_lc is not None:
                    advert[int(m.group(1))] = _limpio(cuerpo)
        if not en_lc or mis is None:
            continue
        nums = _numeros(cab) if ("entrenamiento" in cab or niv == 3) else []
        if niv == 3 and not nums:
            # un ### sin números es el título del texto de la sección anterior
            titulo = cab
            for clave in pendientes:
                out[clave]["titulo"] = out[clave]["titulo"] or cab
                txt, notas = _partes(cuerpo)
                out[clave]["texto"] = out[clave]["texto"] or txt
                out[clave]["notas"] = out[clave]["notas"] or notas
            continue
        if nums:
            txt, notas = _partes(cuerpo)
            tit = ""
            if niv == 3:
                tit = cab.split("·", 1)[-1].strip() if "·" in cab else cab
                tit = re.sub(r"\s*·?\s*clave\s+\*\*[A-D]\*\*", "", tit)
            pendientes = []
            for k in nums:
                out[(mis, k)] = dict(titulo=tit, texto=txt, notas=notas, remite="")
                pendientes.append((mis, k))
            cuerpo_t = "\n".join(cuerpo)
            if not txt and re.search(r"Vuelve el texto de \*\*(\w+)\*\* de la Misión (\d)", cuerpo_t):
                m = re.search(r"Misión (\d)", cuerpo_t)
                for k in nums:
                    out[(mis, k)]["remite"] = f"M{m.group(1)}"
            elif not txt and re.match(r"\s*Mismo texto de", cuerpo_t):
                # «Mismo texto de Savater»: el de esta misma misión que ya se proyectó
                for k in nums:
                    out[(mis, k)]["remite"] = f"M{mis}"
                    out[(mis, k)]["notas"] = [_limpio(cuerpo).split("\n\n")[0].replace("\n", " ")]
    # resolver las remisiones (M2 P1-2 → el texto de Savater de M1 P1-2)
    for (m_, k), v in out.items():
        if v["remite"] and not v["texto"]:
            origen = int(v["remite"][1:])
            for (m2, k2), v2 in out.items():
                if m2 == origen and v2["texto"]:
                    v["texto"], v["titulo"] = v2["texto"], v["titulo"] or v2["titulo"]
                    break
    # El poema de Gómez Jattin va completo en el cuaderno y el .md no lo transcribe:
    # se toma de los versos que imprime la hoja (lc1_icfes.datos_poema).
    v = out.get((1, 4))
    # lc1_icfes.py se perdió el 6 nov (RECUPERACION.md): sin él, la entrada queda sin texto
    # y quien la use (clase_viva) puede reponer los versos desde otra fuente.
    if v is not None and not v["texto"] and os.path.exists("/home/claude/libro/lc1_icfes.py"):
        fuente_py = open("/home/claude/libro/lc1_icfes.py", encoding="utf-8").read()
        m = re.search(r"versos = \[(.*?)\]", fuente_py, re.S)
        if m:
            v["texto"] = "\n".join(re.findall(r'"([^"]+)"', m.group(1)))
    return out, advert


def _limpio(cuerpo):
    t = "\n".join(cuerpo).strip()
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"\*(.+?)\*", r"\1", t)
    return re.sub(r"\n-{3,}\s*$", "", t).strip()


def _partes(cuerpo):
    """Separa el texto citado (líneas «>») de las notas para el profesor (viñetas)."""
    texto, notas, cur = [], [], None
    for ln in cuerpo:
        s = ln.strip()
        if s.startswith(">"):
            texto.append(s.lstrip("> ").rstrip())
        elif s.startswith("- "):
            cur = s[2:]
            notas.append(cur)
        elif s and notas and ln.startswith("  "):
            notas[-1] += " " + s
    txt = "\n".join(texto).strip()
    txt = re.sub(r"\n{2,}", "\n\n", txt)
    limpia = lambda t: re.sub(r"\*\*(.+?)\*\*", r"\1", re.sub(r"\*([^*]+)\*", r"\1", t))
    return limpia(txt), [limpia(n) for n in notas]


if __name__ == "__main__":
    d, adv = leer()
    for m in range(1, 7):
        for k in range(1, 5):
            v = d.get((m, k))
            if not v:
                print(f"M{m} P{k}: — FALTA —")
                continue
            print(f"M{m} P{k}: «{v['titulo'][:48]}» · texto {len(v['texto'])} car. · "
                  f"{len(v['notas'])} notas{' · remite ' + v['remite'] if v['remite'] else ''}")
    print("advertencias previas:", sorted(adv))
