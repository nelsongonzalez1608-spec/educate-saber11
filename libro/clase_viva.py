#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUÍAS DE CLASE PROYECTABLES («clase viva») · el motor, para cualquier área.

Sale de clase_viva_lc.py (las 8 guías de Lectura Crítica entregadas) sin cambiarles nada:
las mismas escenas, la misma plantilla, el mismo JavaScript. Lo propio de cada área entra
por un objeto `Area`. Modelo aprobado: piloto/.../3_presentaciones/Clase_viva_estudiantes.html.

  · barra superior con el momento de la clase y un cronómetro que se reinicia solo cuando
    cambia el momento;
  · la guía del profe en un panel lateral (tecla G), con el objetivo, qué hacer y decir,
    lo que no hace y «Si [el área] no es tu fuerte»;
  · ← → / espacio / Inicio / Fin para moverse, T para el cronómetro, Esc cierra la guía;
  · ninguna clave aparece hasta que el profe la revela con un botón;
  · archivo único (logo incrustado en base64). Las fuentes de Google se piden con respaldo
    del sistema: sin internet la guía funciona igual, con la letra del sistema.

USO
───
    import clase_viva as CV
    import plan_soc as P                      # el planeador del área (ver CONTRATO abajo)
    from textos_soc import leer

    icfes, advert, taller = leer()
    A = CV.Area(
        nombre="Sociales y Ciudadanas", prefijo="SOC", fuerte="Si Sociales no es tu fuerte",
        color=CV.color_de("Sociales y Ciudadanas"),          # sale de lib.AREAS
        P=P,
        claves_libro=lambda mis: {...},        # {pregunta del libro: "A"…} verificadas
        preguntas_icfes=CV.preguntas_de_textos(icfes),       # o lambda mis: [QA, QB, QC, QD]
        textos=icfes, advertencias=advert, taller=taller,
        saberes={...}, activacion={...}, titulos={...}, leads={...},
        est_col=[...], textos_ui=dict(...),   # lo que en LC dice «subrayar el texto»
        out="/home/claude/libro/guias_soc/")
    CV.construir(A)                            # escribe las 8 y devuelve [(archivo, n)]

`Area` trae por defecto la redacción de Lectura Crítica (TEXTOS_UI); un área nueva cambia
las claves de TEXTOS_UI que hablan de «subrayar», «renglón», «texto» o de las competencias
CL/SG/RE (están marcadas «propio de LC» abajo). La prueba de que el motor no cambió nada de
LC es prueba_clase_viva_lc.py.

CONTRATO CON EL PLANEADOR (lo que el motor lee de `A.P`; son los nombres de plan_lc.py)
────────────────────────────────────────────────────────────────────────────────────
  P.FASES        lista de 6 tuplas (nombre, minutos, color, objetivo, [qué hace], cómo lo
                 hace / lo que no hace, material). Se usan nombre, minutos, objetivo, qué
                 hace (lista) y el 6.º campo («Lo que no haces» en la guía). Reparto
                 15·20·35·20·20·10.
  P.MISIONES     {mis: dict(comp, pags, competencia, estr=[4 nombres], cierre)}.
                 comp → «Componente …» de la portada; pags → «Páginas …» y el subtítulo;
                 competencia → tarjeta «Hoy»; estr → chip E1–E4 de cada pregunta, dinámica
                 y cierre; cierre → apoyo del cierre.
  P.TALLER       {mis: [(pregunta, estrategia, instrumento, contexto), …]} las 10 del libro.
                 `estrategia` tiene que ser uno de los nombres de MISIONES[mis]["estr"]
                 (si no, se pinta como E1).
  P.DINAMICAS    {mis: [4 × (nombre, minutos, [pasos], qué movimiento mental entrena,
                 material)]}, en el orden de las estrategias E1–E4.
  P.RETOS        {mis: (nombre, minutos, texto del reto)}.
  P.AVISOS       {mis: [(«preg. 4 y 5» | «preg. 10» | «texto 8 a 10», severidad
                 «alta|media|atención», qué pasa, qué hace el profe), …]} (puede ser {}).
  P.SELLOS       [(área, misión, página, pregunta, saber, …), …] — solo los del área; el
                 motor usa s[1], s[3] y s[4]. Puede ser [].
  P.BANCO        {mis: [4 dicts con "clave" y "contexto"]} = filas de tablero/icfes.csv del
                 área en el orden QA–QD. Si el área no lo tiene, `Area(banco=…)`.
  P.C7, P.C8     las clases 7 y 8 (decisión de Nelson, 10 nov): plan_simulacro.datos() en seis áreas y
                 plan_lc.C7/C8 en Lectura Crítica. Se usan C7: titulo, sub, donde, tiempos (3 × (nombre,
                 minutos, texto), 10·90·20), pasos, no_hace, cuaderno y, si están, que_es, registra,
                 al_final, conteo. C8: titulo, sub, paginas (o rango), esquema [(pieza, texto)],
                 reparto (escoge, asigna, regla), dinamica (forma de DINAMICAS), fases (6 textos),
                 no_hace y, si están, formato, revisa, alcance. La caja de herramientas y los «me piden»
                 salen de simulacro.V2[Area.sim].
  Si plan_soc no tiene alguno, se le pasa a Area un objeto con ese atributo
  (types.SimpleNamespace) en vez del módulo.

LAS CLASES 7 Y 8 (escenas_clase7, escenas_clase8)
─────────────────────────────────────────────────
  Clase 7 · 4 diapositivas: portada · condiciones de examen · el cronómetro grande de la prueba
            (aparte del de la barra: sigue corriendo al cambiar de diapositiva; T lo pausa) · cómo
            anotar en el cuaderno las tres preguntas para socializar. No proyecta preguntas ni claves.
  Clase 8 · 9 diapositivas con las seis fases (15·20·35·20·20·10): portada · el reparto «3 que escojo
            y 3 que asigna el profe» · activación con casillas donde el profe escribe las tres más
            falladas (se conservan mientras la página esté abierta y reaparecen en las siguientes) ·
            el profe modela la más fallada, pieza por pieza del esquema · la caja de herramientas del
            área dibujada como en el cuaderno · desarrollo · la dinámica del área · evaluación ·
            cierre. Sirve con cualquier simulacro. `escenas_clase8(A, antes=[…])` mete escenas al
            comienzo de la activación (Inglés: la ronda de claves de la tarea) y les descuenta el tiempo.
  Barra de las dos clases: subtitulos_simulacro(A).

LO QUE NO SALE DEL PLANEADOR (va en Area)
──────────────────────────────────────────
  claves_libro(mis)    → {1: "D", …, 10: "C"}. Sociales M3–M6: docstring de socN.py
                         («1·A  2·C …», `claves_docstring("soc3")`). M1–M2 no tienen módulo
                         (se perdieron el 6 nov): hay que sacarlas de plan_soc o verificarlas
                         en fuente_libro/ resolviendo.
  preguntas_icfes(mis) → [dict(e=enunciado, o=[4 opciones]) × 4]. Para Sociales,
                         `preguntas_de_textos(icfes)` usa las 24 de TEXTOS_GUIA_DOCENTE.md
                         (enunciado sin el caso, porque el caso va en el panel del texto).
  textos[(mis, k)]     → dict(titulo, texto, notas, verso=False): textos_soc.leer()[0].
  advertencias[mis]    → texto de la advertencia previa (portada).
  saberes[(mis, n)]    → (título, explicación simple, pregunta que destraba) para cada
                         sello: es el «Si … no es tu fuerte» de esa pregunta.
  activacion[mis]      → (frase corta inventada, pista).  titulos[mis], leads[mis].
  taller[(mis, n)]     → notas del taller (textos_soc.leer()[2]); se suman al apoyo del
                         bloque de esa pregunta.

PARA SOCIALES, ADEMÁS
─────────────────────
  · TEXTOS_UI: reescribir las claves «propio de LC» (subrayar el texto, renglón, CL/SG/RE).
    Las competencias de Sociales son tres: pensamiento social · interpretación y análisis
    de perspectivas · pensamiento reflexivo y sistémico (c7_competencias, c7_apoyo_conteo,
    c8_apoyo_elegir).
  · est_col: el oro del área (#C9821B) choca con var(--oro) de E3. Los colores de las
    estrategias del cuaderno de Sociales son azul, verde, rojo, morado:
    est_col=["var(--azul)", "var(--verde)", "var(--rojo)", "var(--morado)"],
    colores=dict(rojo="#A82424", m5=…) (m5 es oro también: conviene otro tono).
  · textos_soc.verificar() cruza las 24 claves del .md con socN_icfes.py y tablero/icfes.csv.

VERIFICAR
─────────
  python3 prueba_clase_viva_lc.py <carpeta>   → las 8 de LC; compara las clases 1–6 con
                                                 libro/fuente_guias_lc/ (copia de las entregadas)
  node verifica_guias.js <carpeta> [capturas]  → JS sin errores, ninguna clave visible antes
                                                 de revelar, nada fuera de ancho, la clave
                                                 revelada es la de data-k
"""
import base64, html, json, os, re, types

LOGO = "/home/claude/libro/logo_educate.png"
FICFES = "Pregunta Saber 11"      # membrete: siempre este, sin año ni «oficial» (regla 7, Nelson 10 nov)
E = lambda t: html.escape(str(t), quote=True)

# Colores fijos de la plantilla. --area y --m1 toman el color del área. Un área puede cambiar
# cualquiera (Area(colores=dict(m5=…))) o agregar otros (dict(rojo="#A82424") → var(--rojo)).
PALETA = dict(azul="#1F4E8C", oro="#B0711A", morado="#5B3E96", verde="#2E7A39",
              m2="#1F4E8C", m3="#3B3BA6", m4="#5B3E96", m5="#B0711A", m6="#2E7A39")


def color_de(nombre):
    from lib import AREAS
    return dict(AREAS)[nombre]


def claves_docstring(modulo, carpeta="/home/claude/libro/"):
    """«1·D  2·C  3·C …» del docstring de un módulo de misión → {1: "D", …}."""
    doc = open(f"{carpeta}{modulo}.py", encoding="utf-8").read()[:3000]
    return {int(n): k for n, k in re.findall(r"(\d+)·([A-D])", doc)}


def preguntas_de_textos(textos):
    return lambda mis: [dict(e=textos[(mis, k)]["enunciado"], o=textos[(mis, k)]["opciones"])
                        for k in range(1, 5)]


# ─────────── la redacción de pantalla y de la guía (por defecto, la de Lectura Crítica) ───────────
# Las marcadas «propio de LC» hablan de subrayar el texto o de CL/SG/RE: un área nueva las cambia.
TEXTOS_UI = dict(
    portada_decir=["«Libro abierto, cuaderno cerrado, lápiz. Esfero no: hoy vamos a "
                   "equivocarnos por escrito.»"],
    portada_libro="Las diez preguntas del momento {mis}",
    # propio de LC ↓
    regla_lead="Si la hoja está limpia, no leíste: pasaste los ojos.",
    regla_p=("Primero se marca el texto —el subrayado y la pregunta al margen—, después se marca "
             "la opción. Una respuesta correcta con el texto en blanco no cuenta como resuelta."),
    regla_decir=["«La respuesta correcta con la hoja limpia no cuenta. ¿Por qué? Porque en la "
                 "prueba nadie les va a decir si acertaron: tienen que saber de dónde lo sacaron.»"],
    regla_apoyo=["Si alguien pregunta para qué marcar, la respuesta corta es: porque el ICFES "
                 "pregunta tres o cuatro cosas distintas del mismo texto, y el que marcó la primera "
                 "vez no tiene que volver a leerlo entero."],
    act_h2="¿Qué palabra pesa más aquí?",
    act_lead="Subráyala en tu cabeza. Escríbele al lado una pregunta.",
    act_apoyo=("No expliques la frase. Si alguien pregunta de dónde salió, di: «eso es lo que vamos a "
               "averiguar». La frase es inventada para la clase: no sale del libro."),
    dina_decir=["«Esto no es recreo: es la misma operación que van a hacer con el texto en cinco "
                "minutos, pero con el cuerpo.»"],
    prob_lead="Antes de releer: ¿cuál creen que es? Levanten la mano.",
    prob_lead2="¿En qué renglón está eso que estás diciendo?",
    prob_sub=("Nadie justifica con «yo creo» ni con «se entiende que». Toda respuesta "
              "señala una palabra o un renglón del texto."),
    prob_apoyo=["Cuenta las manos tocando cada letra: el número queda en pantalla y sirve para el final "
                "del momento, cuando el grupo vea cuántos cambiaron de opinión al volver al texto.",
                "La clave de la pregunta modelo está en el libro mismo, en el análisis de distractores "
                "que viene después. Revélala solo al final de los 20 minutos."],
    bloque_h2="Preguntas {a} y {b}: primero el texto, después la opción",
    bloque_decir=["«Antes de marcar: ¿qué subrayaron? Léanme el renglón.»",
                  "Si alguien se traba, pregúntale qué subrayó. Si la hoja está limpia, vuelve al texto "
                  "antes que a la respuesta."],
    bloque_apoyo=("Las claves del libro son {a}·{ka} y {b}·{kb}. No las reveles hasta que todos tengan "
                  "el texto marcado: el botón es para el cierre del bloque."),
    reto_defensa=("<b>La defensa:</b> tres minutos por equipo, leyendo en voz alta el renglón que los "
                  "respalda. Citar de memoria no cuenta."),
    reto_apoyo=["El reto no tiene una sola respuesta correcta: gana el equipo que mejor sostiene la suya "
                "con el texto. Si dos lecturas están sostenidas, dilo: eso también es leer bien.",
                "Si un equipo entrega una sola hoja para los tres, el reto no cuenta. La discusión es "
                "compartida; el registro es individual."],
    icfes_decir=["Durante la evaluación no se proyecta nada: las preguntas están en el cuaderno. Esta "
                 "diapositiva es para el cierre, cuando se socializan las falladas.",
                 "«¿Qué subrayaste en el texto antes de mirar las opciones?»"],
    # Las clases 7 y 8 ya no usan TEXTOS_UI: todo sale de P.C7 y P.C8 (decisión de Nelson, 10 nov).
)


class Area:
    """Todo lo que cambia de un área a otra. Ver el docstring del módulo."""

    def __init__(self, nombre, prefijo, fuerte, color, P, claves_libro, preguntas_icfes,
                 textos, out, advertencias=None, taller=None, saberes=None, activacion=None,
                 titulos=None, leads=None, est_col=None, colores=None, textos_ui=None,
                 banco=None, apoyo_fuerte=None, sim=None):
        self.nombre, self.prefijo, self.fuerte, self.color = nombre, prefijo, fuerte, color
        self.P, self.claves_libro, self.preguntas_icfes = P, claves_libro, preguntas_icfes
        self.textos, self.out = textos, out
        self.advertencias = advertencias or {}
        self.taller = taller or {}
        self.saberes = saberes or {}
        self.activacion, self.titulos, self.leads = activacion, titulos, leads
        self.est_col = est_col or ["var(--area)", "var(--azul)", "var(--oro)", "var(--morado)"]
        self.colores = dict(PALETA, **(colores or {}))
        self.ui = dict(TEXTOS_UI, **(textos_ui or {}))
        self.banco = banco or (lambda mis: P.BANCO[mis])
        # «lo que necesitas saber si Lectura Crítica no es tu área» (portada)
        self.apoyo_fuerte = apoyo_fuerte or f"{nombre} no es tu área"
        # clave del área en simulacro.py (la caja de herramientas de la hoja de simulacro)
        self.sim = sim or SIM_CLAVE.get(nombre)


SIM_CLAVE = {"Matemáticas": "mate", "Lectura Crítica": "lc", "Sociales y Ciudadanas": "soc",
             "Biología": "bio", "Química": "qui", "Física": "fis", "Inglés": "ing"}


COL = {1: "var(--m1)", 2: "var(--m2)", 3: "var(--m3)", 4: "var(--m4)", 5: "var(--m5)", 6: "var(--m6)"}


# ───────────────────────────── datos ─────────────────────────────
def avisos_por_pregunta(A, mis):
    """«preg. 4 y 5», «preg. 10», «texto 8 a 10» → {pregunta: aviso}"""
    out = {}
    for preg, sev, que, hacer in getattr(A.P, "AVISOS", {}).get(mis, []):
        nums = [int(x) for x in re.findall(r"\d+", preg)]
        if " a " in preg and len(nums) == 2:
            nums = list(range(nums[0], nums[1] + 1))
        for n in nums:
            out.setdefault(n, []).append((sev, que, hacer))
    return out


def sello(A, mis, preg):
    for s in getattr(A.P, "SELLOS", []):
        if str(s[1]) == str(mis) and str(s[3]) == str(preg):
            return s
    return None


# ───────────────────────────── piezas de las escenas ─────────────────────────────
def guia(A, fase, decir=(), apoyo=()):
    nom, mins, c, obj, hace, como, material = A.P.FASES[fase]
    return dict(obj=obj, decir=list(decir) or list(hace), como=como, apoyo=list(apoyo))


def esc_portada(A, mis):
    d = A.P.MISIONES[mis]
    adv = A.advertencias.get(mis)
    apoyo = ["Abre esta guía con la tecla G en cada diapositiva: trae lo que dices y, debajo, "
             f"lo que necesitas saber si {A.apoyo_fuerte}.",
             "El cronómetro arranca con T y se reinicia solo cuando cambia el momento de la clase."]
    if adv:
        apoyo.insert(0, "⚑ Esta clase tiene advertencia previa. Léela antes del sábado: " +
                     re.sub(r"\s+", " ", adv)[:700])
    h = (f'<div class="logo-xl"><img src="__LOGO__" alt="EDUCATE · Para el Saber"></div>'
         f'<div class="eyebrow"><span class="tag">Clase {mis} de 8</span>'
         f'<span class="kicker">{E(A.nombre)} · Componente {E(d["comp"])}</span></div>'
         f'<h1>{E(A.titulos[mis])}</h1>')
    h += (f'<p class="lead">{E(A.leads[mis])}</p>'
          f'<div class="grid c3 mt">'
          f'<div class="card edge" style="--accent:var(--m1)"><h3>Tu libro</h3>'
          f'<p class="sub">{E(A.ui["portada_libro"].format(mis=mis))}</p></div>'
          f'<div class="card edge" style="--accent:var(--m4)"><h3>Tu cuaderno</h3>'
          f'<p class="sub">Páginas {E(d["pags"])}</p></div>'
          f'<div class="card edge" style="--accent:var(--m6)"><h3>Hoy</h3>'
          f'<p class="sub">120 minutos · 6 momentos · {E(d["competencia"])}</p></div></div>')
    return dict(m=None, html=h, guia=dict(obj="Que el grupo sepa desde el primer minuto qué va a "
                "pasar en estos 120 minutos y qué tiene que tener sobre la mesa.",
                decir=list(A.ui["portada_decir"]), apoyo=apoyo))


def esc_reglas(A, mis):
    filas = "".join(
        f'<div class="step" style="--accent:{COL[i+1]}"><div class="k">{i+1}</div>'
        f'<div><b>{E(f[0])}</b><span class="sub"> · {f[1]} min</span></div></div>'
        for i, f in enumerate(A.P.FASES))
    h = (f'<div class="eyebrow"><span class="kicker">Así vamos a trabajar</span></div>'
         f'<h2>Seis momentos, una sola regla</h2>'
         f'<div class="grid c2 mt"><div class="grid" style="gap:10px">{filas}</div>'
         f'<div class="card big edge" style="--accent:var(--area)"><h3>La regla del cuaderno</h3>'
         f'<p class="lead">{E(A.ui["regla_lead"])}</p>'
         f'<p>{E(A.ui["regla_p"])}</p>'
         f'</div></div>')
    return dict(m=None, html=h, guia=dict(
        obj="Que la regla quede dicha en voz alta antes de cualquier texto.",
        decir=list(A.ui["regla_decir"]), apoyo=list(A.ui["regla_apoyo"])))


def esc_activacion(A, mis):
    txt, pista = A.activacion[mis]
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m1)">Activación</span>'
         f'<span class="kicker">Cuaderno cerrado</span></div>'
         f'<h2>{E(A.ui["act_h2"])}</h2>'
         f'<blockquote class="cita xl">{E(txt)}</blockquote>'
         f'<p class="lead">{E(A.ui["act_lead"])}</p>'
         f'<div class="ctl"><button class="btn" data-show="pista{mis}">Mostrar la pista</button></div>'
         f'<div class="note" id="pista{mis}" hidden style="--accent:var(--m1)"><b>Pista:</b> {E(pista)}</div>')
    return dict(m=0, html=h, guia=guia(A, 0, apoyo=[
        A.ui["act_apoyo"],
        f"La pista existe para el cierre de los 15 minutos, no para el principio: {pista}."]))


def esc_dinamica(A, mis, i, fase):
    nom, mins, pasos, entrena, material = A.P.DINAMICAS[mis][i]
    est = A.P.MISIONES[mis]["estr"][i]
    lis = "".join(f'<li>{E(p)}</li>' for p in pasos)
    c = A.est_col[i]
    h = (f'<div class="eyebrow"><span class="min" style="--accent:{c}">Dinámica · {mins} min</span>'
         f'<span class="kicker">Entrena la estrategia {i+1} · {E(est)}</span></div>'
         f'<h2>{E(nom)}</h2>'
         f'<div class="grid c2 mt"><div class="card edge" style="--accent:{c}">'
         f'<h3>Cómo se hace</h3><ol class="pasos">{lis}</ol></div>'
         f'<div class="card"><h3>Qué vas a necesitar</h3><p>{E(material)}</p></div></div>')
    return dict(m=fase, min=mins, html=h, guia=guia(A, fase, decir=list(A.ui["dina_decir"]), apoyo=[
        "Qué movimiento mental entrena: " + entrena,
        "La regla para aprobar cualquier dinámica: si no puedes decir qué paso de la estrategia "
        "está ejercitando, es recreo, no clase."]))


def esc_problematizadora(A, mis):
    botones = "".join(
        f'<button class="btn tally" data-tally="h{mis}{L}">{L} <span class="n" id="h{mis}{L}">0</span></button>'
        for L in "ABCD")
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m2)">Pregunta problematizadora</span>'
         f'<span class="kicker">Libro abierto en la pregunta modelo</span></div>'
         f'<h2>Abran el libro en la pregunta modelo del momento {mis}</h2>'
         f'<p class="lead">{E(A.ui["prob_lead"])}</p>'
         f'<div class="ctl">{botones}<button class="btn" data-reset="h{mis}">↺</button></div>'
         f'<div class="card big edge mt" style="--accent:var(--m2)"><h3>La pregunta que gobierna el área</h3>'
         f'<p class="lead">{E(A.ui["prob_lead2"])}</p>'
         f'<p class="sub">{E(A.ui["prob_sub"])}</p></div>')
    return dict(m=1, html=h, guia=guia(A, 1, apoyo=list(A.ui["prob_apoyo"])))


def esc_bloque(A, mis, a, b_, claves, avisos):
    d = A.P.MISIONES[mis]
    taller = {p: (e, i, c) for p, e, i, c in A.P.TALLER[mis]}
    partes, apoyo = [], []
    for n in (a, b_):
        est, ins, ctx = taller[n]
        k = d["estr"].index(est) if est in d["estr"] else 0
        c = A.est_col[k]
        s = sello(A, mis, n)
        sel = ""
        if s:
            sab = A.saberes.get((mis, n))
            titulo_s = sab[0] if sab else s[4]
            sel = (f'<div class="sello"><b>Alto · aquí entra el profe</b>'
                   f'<span>{E(titulo_s)}</span></div>')
            if sab:
                apoyo.append(f"Pregunta {n} · {sab[0]}: {sab[1]} Para destrabar: «{sab[2]}»")
        for nota in A.taller.get((mis, n), []):
            apoyo.append(f"Pregunta {n} · {nota['titulo']}: " + re.sub(r"\s+", " ", nota["texto"]))
        av = ""
        for sev, que, hacer in avisos.get(n, []):
            av += (f'<div class="aviso sev-{E(sev[:4])}" hidden data-grupo="k{mis}{a}">'
                   f'<b>Ojo con esta clave:</b> {E(que)}</div>')
            apoyo.append(f"Pregunta {n} · aviso del libro ({sev}): {que} Qué haces: {hacer}")
        partes.append(
            f'<div class="card edge" style="--accent:{c}">'
            f'<div class="eyebrow"><span class="membrete">Libro · pregunta {n}</span>'
            f'<span class="min" style="--accent:{c}">E{k+1} · {E(est)}</span></div>'
            f'<p class="sub">{E(ctx)}</p>'
            f'<h3 style="color:{c}">{E(ins)}</h3>'
            f'<p>Llena el instrumento de tu cuaderno antes de mirar las opciones.</p>{sel}'
            f'<div class="clave" hidden data-grupo="k{mis}{a}"><span class="keychip" '
            f'style="background:{c}">{E(claves.get(n, "—"))}</span> es la clave del libro</div>'
            f'{av}</div>')
    ins_pantalla = (a == 1)
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m3)">Desarrollo guiado · '
         f'preguntas {a} y {b_}</span><span class="kicker">'
         f'{"En pantalla, casilla por casilla" if ins_pantalla else "En el cuaderno, cada uno el suyo"}'
         f'</span></div>'
         f'<h2>{E(A.ui["bloque_h2"].format(a=a, b=b_))}</h2>'
         f'<div class="grid c2 mt">{"".join(partes)}</div>'
         f'<div class="ctl"><button class="btn" data-showgrupo="k{mis}{a}">Revelar las claves</button></div>')
    apoyo.insert(0, A.ui["bloque_apoyo"].format(a=a, b=b_, ka=claves.get(a, '—'), kb=claves.get(b_, '—')))
    return dict(m=2, min=7, html=h, guia=guia(A, 2, decir=list(A.ui["bloque_decir"]), apoyo=apoyo))


def esc_reto(A, mis):
    nom, mins, txt = A.P.RETOS[mis]
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m4)">Reto en equipo · {mins} min</span>'
         f'<span class="kicker">Equipos de tres · cada uno responde en su cuaderno</span></div>'
         f'<h2>Reto del corte: {E(nom)}</h2>'
         f'<div class="card big edge mt" style="--accent:var(--m4)"><p class="lead">{E(txt)}</p></div>'
         f'<div class="note mt" style="--accent:var(--m4)">{A.ui["reto_defensa"]}</div>')
    return dict(m=3, html=h, guia=guia(A, 3, apoyo=list(A.ui["reto_apoyo"])))


def esc_icfes(A, mis, k, q, clave, txt):
    ops = "".join(
        f'<div class="op" data-op="{L}"><span class="L">{L}</span><span>{E(o)}</span></div>'
        for L, o in zip("ABCD", q["o"]))
    tit = txt.get("titulo") or "Texto de la pregunta"
    texto = txt.get("texto") or ""
    if txt.get("verso"):                     # poemas y canciones: verso por verso
        cuerpo = "".join("<p>" + "<br>".join(E(v) for v in p.split("\n")) + "</p>"
                         for p in texto.split("\n\n") if p.strip())
    else:
        cuerpo = "".join(f"<p>{E(p)}</p>" for p in texto.split("\n\n") if p.strip())
    ident = f"icf{mis}{k}"
    h = (f'<div class="eyebrow"><span class="membrete">{E(FICFES)}</span>'
         f'<span class="min" style="--accent:var(--m5)">Evaluación individual · pregunta {k}</span></div>'
         f'<div class="grid c2 icfes mt">'
         f'<div class="texto"><h3>{E(tit)}</h3>{cuerpo or "<p class=sub>El texto va completo en el cuaderno.</p>"}</div>'
         f'<div><p class="enun">{E(q["e"])}</p><div class="ops" id="{ident}">{ops}</div>'
         f'<div class="ctl"><button class="btn" data-clave="{ident}" data-k="{E(clave)}">Revelar la clave</button></div>'
         f'</div></div>')
    notas = txt.get("notas") or []
    return dict(m=4, html=h, guia=guia(A, 4, decir=list(A.ui["icfes_decir"]),
                                      apoyo=[f"La clave es la {clave}."] + notas))


def esc_cierre(A, mis):
    d = A.P.MISIONES[mis]
    ests = "".join(f'<div class="step" style="--accent:{A.est_col[i]}"><div class="k">{i+1}</div>'
                   f'<div><b>{E(e)}</b></div></div>' for i, e in enumerate(d["estr"]))
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m6)">Cierre</span>'
         f'<span class="kicker">La pregunta de siempre</span></div>'
         f'<h2>¿En qué se parecía la pregunta Saber 11 a la de tu libro?</h2>'
         f'<div class="grid c2 mt"><div class="grid" style="gap:10px">{ests}</div>'
         f'<div class="card big edge" style="--accent:var(--m6)"><h3>Antes de salir</h3>'
         f'<ol class="pasos"><li>La palabra nueva del día, en la franja de vocabulario, con tus '
         f'palabras.</li><li>«Lo que me llevo de esta pregunta».</li><li>Tu carita de salida.</li>'
         f'<li>La casilla {mis} de la portada del área.</li></ol></div></div>')
    return dict(m=5, html=h, guia=guia(A, 5, apoyo=[
        "La palabra nueva no se dicta. Si quedó mal entendida, eso se ve en la hoja y se corrige "
        "la próxima clase: es mejor que dictarla bien.",
        "Para el cierre del momento: " + d["cierre"]]))


# ─────────────────────────────── las dos clases del simulacro ───────────────────────────────
# Decisión de Nelson (10 nov): el simulacro ya no proyecta las 24 preguntas de entrenamiento.
#   Clase 7 · el estudiante presenta el simulacro de EDUCATE (cuadernillo o PTD, fuera del cuaderno).
#             La guía conduce la prueba: portada, condiciones de examen, un cronómetro grande y, al
#             final, cómo anotar en el cuaderno las preguntas que cada uno quiere socializar.
#   Clase 8 · la socialización en las hojas de simulacro del cuaderno, con las seis fases aprobadas.
# Todo sale de A.P.C7 y A.P.C8 (plan_simulacro.datos() o, en Lectura Crítica, plan_lc.C7/C8) y de la
# caja de herramientas de simulacro.py. No se proyecta ninguna pregunta ni ninguna clave: las preguntas
# más falladas no se conocen de antemano, y la clase 8 trae casillas para que el profe las escriba.
def _rango_sim(A):
    C8 = A.P.C8
    if C8.get("rango"):
        return C8["rango"]
    p = C8["paginas"]
    return f"{p[0]} a {p[-1]}"


def _sin_prefijo(t):
    """«Clase 7 · el simulacro de EDUCATE» → «El simulacro de EDUCATE»."""
    t = re.sub(r"^Clase \d\s*·\s*", "", t)
    return t[:1].upper() + t[1:]


def _primera_frase(t):
    return re.split(r"(?<=[.!?»])\s+(?=[A-ZÁÉÍÓÚÑ«])", t.strip(), maxsplit=1)[0]


def subtitulos_simulacro(A):
    """El subtítulo de la barra superior de las clases 7 y 8."""
    return ("Simulacro de EDUCATE · cuadernillo o PTD, fuera del cuaderno",
            f"Socialización del simulacro · hojas de simulacro, páginas {_rango_sim(A)}")


def caja_herramientas(A):
    """Las cuatro herramientas de la hoja de simulacro del área, con el mismo dibujito y el mismo
    rótulo que trae el cuaderno (simulacro.py, V2[área]["herr"]), y los cuatro «me piden»."""
    import simulacro as SIM
    SIM.colores(SIM.AREA[A.sim]["area"])
    v = SIM.V2[A.sim]
    cajas = "".join(
        f'<div class="herr"><span class="chk"></span>'
        f'<svg viewBox="-3 -3 40 42" width="60" height="63" aria-hidden="true">{ic(0, 0)}</svg>'
        f'<b>{E(lab)}</b></div>' for lab, ic in v["herr"])
    pide = "".join(f'<span class="pide"><span class="chk"></span>{E(p)}</span>' for p in v["pide"])
    return cajas, pide, [lab for lab, _ in v["herr"]], list(v["pide"])


def _asignadas_eco():
    return "".join(f'<span class="nums1">Asignada {k} · n.º <b data-eco="asig{k}">—</b></span>'
                   for k in (1, 2, 3))


def escenas_clase7(A):
    C7, C8 = A.P.C7, A.P.C8
    sim = _rango_sim(A)
    t_antes, t_prueba, t_anoto = C7["tiempos"]
    assert sum(t[1] for t in C7["tiempos"]) == 120, "la clase 7 tiene que sumar 120 minutos"
    reloj = "".join(f'<div class="step" style="--accent:{c}"><div class="k">{m}\'</div>'
                    f'<div><b>{E(n)}</b></div></div>'
                    for (n, m, _), c in zip(C7["tiempos"], ("var(--m2)", "var(--area)", "var(--m6)")))
    # 1 · portada
    sc = [dict(m=None, html=(
        '<div class="logo-xl"><img src="__LOGO__" alt="EDUCATE · Para el Saber"></div>'
        f'<div class="eyebrow"><span class="tag">Clase 7 de 8</span><span class="kicker">{E(A.nombre)} '
        f'· simulacro del área</span></div><h1>{E(_sin_prefijo(C7["titulo"]))}</h1>'
        f'<p class="lead">{E(C7["sub"])}.</p>'
        f'<div class="grid c3 mt">'
        f'<div class="card edge" style="--accent:var(--m1)"><h3>La prueba</h3><p class="sub">{E(C7["donde"])}</p></div>'
        f'<div class="card edge" style="--accent:var(--m4)"><h3>Tu cuaderno</h3>'
        f'<p class="sub">Cerrado durante la prueba. Al final se abre en las hojas de simulacro, páginas {E(sim)}.</p></div>'
        f'<div class="card edge" style="--accent:var(--m6)"><h3>Hoy</h3><div class="grid" style="gap:8px">{reloj}</div></div>'
        f'</div>'),
        guia=dict(obj="Que el simulacro se viva en condiciones de examen, y que cada uno salga con tres "
                      "preguntas anotadas para socializar en la clase 8.",
                  decir=[C7.get("que_es") or C7["donde"]],
                  como=C7["no_hace"],
                  apoyo=["Esta guía no trae preguntas ni claves: el simulacro lo escoge EDUCATE y sirve "
                         "cualquiera. Ten a la mano el cuadernillo (o el acceso a la PTD) y las hojas de "
                         "respuestas antes de que entren.",
                         "El cronómetro de la prueba está en la tercera diapositiva: es aparte del de la "
                         "barra y sigue corriendo aunque cambies de diapositiva."]))]
    # 2 · las condiciones de examen
    pasos = "".join(f"<li>{E(p)}</li>" for p in C7["pasos"])
    sc.append(dict(m=None, min=t_antes[1], html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--m2)">{E(t_antes[0])} · {t_antes[1]} min</span>'
        f'<span class="kicker">Condiciones de examen</span></div>'
        f'<h2>Como en la prueba de verdad</h2>'
        f'<div class="grid c2 mt"><div class="card edge" style="--accent:var(--m2)"><ol class="pasos">{pasos}</ol></div>'
        f'<div class="card big edge" style="--accent:var(--area)"><h3>Antes de empezar</h3>'
        f'<p>{E(t_antes[2])}</p></div></div>'),
        guia=dict(obj="Que las condiciones queden dichas una vez, antes de abrir el cuadernillo.",
                  decir=[t_antes[2], "«Durante la prueba no respondo dudas, ni de vocabulario. Si una "
                         "pregunta les parece mal hecha, márquenla al margen y sigan.»"],
                  como=C7["no_hace"],
                  apoyo=["Qué registras tú (esto no lo ve el estudiante):"] + list(C7.get("registra", [])))))
    # 3 · el cronómetro grande de la prueba (aparte del de la barra: no se reinicia al cambiar)
    sc.append(dict(m=None, html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--area)">{E(t_prueba[0])} · {t_prueba[1]} min</span>'
        f'<span class="kicker">En silencio y de corrido</span></div>'
        f'<div class="examen" data-examen="{t_prueba[1]}">'
        f'<div class="relojxl" data-exnum>{t_prueba[1]}:00</div>'
        f'<div class="exhoras"><span>Empieza <b data-exini>—</b></span><span>Termina <b data-exfin>—</b></span></div>'
        f'<div class="ctl" style="justify-content:center">'
        f'<button class="btn solid" data-ex="play">Iniciar la prueba</button>'
        f'<button class="btn" data-ex="reset" aria-label="Reiniciar la prueba">↺</button></div></div>'
        f'<p class="sub" style="text-align:center">{E(t_prueba[2])}</p>'),
        guia=dict(obj="Medir sin acompañamiento.",
                  decir=["Inicia el cronómetro cuando todos tengan el cuadernillo cerrado frente a ellos y "
                         "escribe en el tablero la hora de inicio y la de cierre que aparecen aquí.",
                         "No intervengas en los " + str(t_prueba[1]) + " minutos."],
                  como=C7["no_hace"],
                  apoyo=["Este cronómetro sigue corriendo aunque pases de diapositiva o abras la guía; "
                         "la tecla T lo pausa. ↺ lo vuelve a poner en " + str(t_prueba[1]) + " minutos.",
                         "Cuando llega a cero sigue contando en rojo, con un «+», el tiempo de más."] +
                        list(C7.get("registra", []))[:2])))
    # 4 · lo que anoto para socializar
    if C7.get("al_final"):
        lead_a, resto_a = C7["al_final"], t_anoto[2]
    else:                                   # Lectura Crítica no trae «al_final»
        lead_a = _primera_frase(t_anoto[2])
        resto_a = t_anoto[2][len(lead_a):].strip()
    sc.append(dict(m=None, min=t_anoto[1], html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--m6)">{E(t_anoto[0])} · {t_anoto[1]} min</span>'
        f'<span class="kicker">Cuaderno abierto en las páginas {E(sim)}</span></div>'
        f'<h2>Tres preguntas que quiero socializar</h2>'
        f'<div class="grid c2 mt"><div class="card big edge" style="--accent:var(--m6)">'
        f'<p class="lead">{E(lead_a)}</p>'
        f'<p>{E(resto_a)}</p></div>'
        f'<div class="card edge" style="--accent:var(--m4)"><h3>En el membrete de cada esquema</h3>'
        f'<ol class="pasos"><li>El <b>n.º</b> de la pregunta en el simulacro.</li>'
        f'<li>Marca <b>«la escogí yo»</b>.</li><li>En <b>«Marqué»</b>, la letra que marcaste.</li>'
        f'<li><b>«Era»</b> queda vacío hasta la clase 8.</li></ol></div></div>'),
        guia=dict(obj="Que cada uno llegue a la clase 8 con sus tres preguntas escogidas.",
                  decir=[t_anoto[2], "«No tienen que saber cuál era la respuesta: anoten la que dudaron, la "
                         "que creen que fallaron o la que acertaron sin saber por qué.»"],
                  como=C7["no_hace"],
                  apoyo=[C7["cuaderno"]] + [r for r in C7.get("registra", [])[2:]] +
                        ["En la semana, saca de las hojas de respuestas las tres preguntas más falladas: son "
                         "las que asignas en la clase 8."])))
    return sc


def escenas_clase8(A, antes=()):
    """La socialización en las hojas de simulacro del cuaderno, con las seis fases (A.P.FASES) y lo
    que trae A.P.C8. `antes`: escenas que van al comienzo de la activación (Inglés: la ronda de
    claves de la última tarea); su tiempo se descuenta de la activación."""
    C7, C8 = A.P.C7, A.P.C8
    F = A.P.FASES
    assert [f[1] for f in F] == [15, 20, 35, 20, 20, 10], "el reparto aprobado es 15·20·35·20·20·10"
    sim = _rango_sim(A)
    rep = C8["reparto"]
    fases = C8["fases"]
    cajas, pide, herr, pides = caja_herramientas(A)
    nom_d, min_d, pasos_d, entrena_d, material_d = C8["dinamica"]
    conteo = C7.get("conteo")

    def g(i, obj, apoyo=(), decir=None):
        return dict(obj=obj, decir=[fases[i]] + list(decir or []), como=C8["no_hace"] if i in (1, 2) else "",
                    apoyo=list(apoyo))

    filas = "".join(
        f'<div class="step" style="--accent:{COL[i+1]}"><div class="k">{i+1}</div>'
        f'<div><b>{E(f[0])}</b><span class="sub"> · {f[1]} min</span></div></div>' for i, f in enumerate(F))
    sc = [dict(m=None, html=(
        '<div class="logo-xl"><img src="__LOGO__" alt="EDUCATE · Para el Saber"></div>'
        f'<div class="eyebrow"><span class="tag">Clase 8 de 8</span><span class="kicker">{E(A.nombre)} '
        f'· socialización del simulacro</span></div><h1>{E(_sin_prefijo(C8["titulo"]))}</h1>'
        f'<p class="lead">{E(C8["sub"])}. Seis preguntas por estudiante: '
        f'{rep["escoge"]} que escoges tú y {rep["asigna"]} que asigna el profe.</p>'
        f'<div class="grid c3 mt">'
        f'<div class="card edge" style="--accent:var(--m1)"><h3>Tu cuaderno</h3>'
        f'<p class="sub">Hojas de simulacro, páginas {E(sim)}. Un esquema por pregunta.</p></div>'
        f'<div class="card edge" style="--accent:var(--m4)"><h3>Lo que traes</h3>'
        f'<p class="sub">Las {rep["escoge"]} preguntas que anotaste al final de la clase 7.</p></div>'
        f'<div class="card edge" style="--accent:var(--m6)"><h3>Hoy</h3>'
        f'<p class="sub">120 minutos · 6 momentos · la opción se marca al final</p></div></div>'),
        guia=dict(obj="Reparar, no repetir: socializar en el cuaderno las preguntas del simulacro que "
                      "cada uno escogió y las que más falló el grupo.",
                  decir=["«Cuaderno abierto en las hojas de simulacro, en los esquemas donde anotaron sus "
                         "tres preguntas.»"],
                  como=C8["no_hace"],
                  apoyo=["Antes de la clase: saca de las hojas de respuestas del simulacro las tres "
                         "preguntas más falladas. Esta guía sirve para cualquier simulacro: no trae las "
                         "preguntas; tú las escribes en la diapositiva de la activación.",
                         C8.get("alcance") or ""]))]
    sc[0]["guia"]["apoyo"] = [x for x in sc[0]["guia"]["apoyo"] if x]
    # 2 · seis momentos y el reparto
    sc.append(dict(m=None, html=(
        f'<div class="eyebrow"><span class="kicker">Así vamos a trabajar</span></div>'
        f'<h2>Seis preguntas: {rep["escoge"]} que escojo y {rep["asigna"]} que asigna el profe</h2>'
        f'<div class="grid c2 mt"><div class="grid" style="gap:10px">{filas}</div>'
        f'<div class="grid" style="gap:14px">'
        f'<div class="grid c2" style="gap:12px">'
        f'<div class="card edge" style="--accent:var(--m4)"><div class="nbig">{rep["escoge"]}</div>'
        f'<p><b>que escojo yo</b>: las que anoté al final de la clase 7.</p></div>'
        f'<div class="card edge" style="--accent:var(--area)"><div class="nbig">{rep["asigna"]}</div>'
        f'<p><b>que asigna el profe</b>: las que más falló el grupo.</p></div></div>'
        f'<div class="card big edge" style="--accent:var(--m3)"><h3>La regla</h3>'
        f'<p>{E(rep["regla"])}</p></div></div></div>'),
        guia=dict(obj="Que el reparto quede claro antes de abrir un solo esquema.",
                  decir=[rep["regla"]],
                  apoyo=[C8.get("revisa") or "Un esquema con la opción marcada y el resto en blanco no "
                         "cuenta como socializado."])))
    # 3 · activación: las más falladas (las escribe el profe) — más lo que el área haga antes
    mins_antes = sum(e.get("min") or 0 for e in antes)
    sc += [dict(e, m=0) for e in antes]
    filas_a = "".join(
        f'<div class="asig"><span class="k" style="background:{COL[k+1]}">{k}</span>'
        f'<label>n.º <input class="campo n" data-campo="asig{k}" inputmode="numeric" autocomplete="off" '
        f'aria-label="Número de la asignada {k}"></label>'
        f'<label class="w">qué pedía <input class="campo" data-campo="pide{k}" autocomplete="off" '
        f'aria-label="Qué pedía la asignada {k}"></label></div>' for k in (1, 2, 3))
    cont = (f'<div class="asig"><label class="w">Aciertos por {E(conteo)} '
            f'<input class="campo" data-campo="conteo" autocomplete="off" aria-label="Aciertos por {E(conteo)}">'
            f'</label></div>') if conteo else ""
    sc.append(dict(m=0, min=(15 - mins_antes) if antes else None, html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--m1)">Activación</span>'
        f'<span class="kicker">Las escribe el profe · el grupo las copia</span></div>'
        f'<h2>Las tres que más falló el grupo</h2>'
        f'<p class="lead">Escribe cada número en un esquema libre y marca <b>«me la asignaron»</b>.</p>'
        f'<div class="card edge mt" style="--accent:var(--m1)">{filas_a}{cont}</div>'
        f'<div class="note" style="--accent:var(--m1)"><b>Cómo proyectarlas:</b> si tienes el cuadernillo '
        f'o la PTD en pantalla, ábrelo en otra ventana con la pregunta y vuelve a esta guía (Alt+Tab). '
        f'Si no, basta con el número y lo que pedía: el enunciado lo tiene cada uno en su cuadernillo.</div>'),
        guia=g(0, "Que el resultado se devuelva sin notas y que cada uno sepa cuáles son sus tres asignadas.",
               apoyo=["Las casillas se llenan con el teclado y se quedan mientras la página esté abierta: los "
                      "números reaparecen en las diapositivas siguientes.",
                      "No escribas aquí la clave de ninguna: «Era» se llena después de razonar la pregunta."])))
    # 4 · problematizadora: el profe modela la más fallada, pieza por pieza
    piezas = "".join(
        f'<div class="step" style="--accent:var(--m2)"><div class="k">{k}</div>'
        f'<div><b>{E(p)}</b><span class="sub"> · {E(t)}</span></div></div>'
        for k, (p, t) in enumerate(C8["esquema"], 1))
    sc.append(dict(m=1, html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--m2)">Pregunta problematizadora</span>'
        f'<span class="kicker">El profe modela · todos llenan con él</span></div>'
        f'<h2>La más fallada, n.º <span data-eco="asig1">—</span>, pieza por pieza</h2>'
        f'<p class="lead">En voz alta y en el tablero. Cada uno la llena en su esquema al mismo tiempo.</p>'
        f'<div class="grid mt{" c2" if len(C8["esquema"]) > 6 else ""}" style="gap:8px">{piezas}</div>'),
        guia=g(1, "Que el grupo vea al profe llenar un esquema completo antes de hacerlo solo.",
               apoyo=["Piensa en voz alta, también cuando dudas: el estudiante necesita ver cómo se decide "
                      "qué le piden y qué herramienta se usa, no solo la respuesta.",
                      "La opción se marca al final, después del tacho con razón. Si alguien dice la letra "
                      "antes, pregúntale qué pieza del esquema la sostiene."])))
    # 5 · la caja de herramientas del área, dibujada como en el cuaderno
    sc.append(dict(m=1, html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--m2)">Pregunta problematizadora</span>'
        f'<span class="kicker">La caja de herramientas de {E(A.nombre)}</span></div>'
        f'<h2>Escoge la herramienta según lo que te piden</h2>'
        f'<div class="card edge mt" style="--accent:var(--m2)"><h3>Me piden…</h3>'
        f'<div class="pides">{pide}</div></div>'
        f'<div class="herrs mt">{cajas}</div>'
        f'<p class="sub mt">En el esquema, marca la que usaste y razona con ella en el espacio libre. '
        f'Ninguna es obligatoria: la que sirve depende de la pregunta.</p>'),
        guia=g(1, "Que el estudiante sepa que la caja tiene cuatro herramientas y que escoger una es parte "
                  "de resolver.",
               decir=[f"Muestra cada herramienta con la pregunta modelada: «¿cuál de estas me sirvió aquí, "
                      f"y por qué no las otras?»"],
               apoyo=["La caja de herramientas de la hoja de simulacro del área: " + ", ".join(herr) + ".",
                      "Los cuatro tipos de tarea de la fila «Me piden»: " + ", ".join(pides) + "."])))
    # 6 · desarrollo guiado: cada uno sus esquemas
    sc.append(dict(m=2, html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--m3)">Desarrollo guiado</span>'
        f'<span class="kicker">Cada uno en su cuaderno · páginas {E(sim)}</span></div>'
        f'<h2>Tus esquemas, uno por pregunta</h2>'
        f'<p class="lead">{E(_primera_frase(fases[2]))}</p>'
        f'<div class="grid c2 mt"><div class="card edge" style="--accent:var(--m3)"><h3>En cada esquema</h3>'
        f'<ol class="pasos"><li>Lo que me piden.</li><li>La herramienta que uso, y razono con ella.</li>'
        f'<li>Tacho con razón cada opción que descarto.</li><li>Solo al final, la opción.</li></ol></div>'
        f'<div class="card big edge" style="--accent:var(--area)"><p class="lead">Un esquema con la letra '
        f'marcada y el resto en blanco no cuenta como socializado.</p></div></div>'
        f'<div class="nums mt">{_asignadas_eco()}</div>'),
        guia=g(2, "Que cada uno llene sus esquemas con el andamiaje completo, no solo la letra.",
               apoyo=[C8.get("revisa") or "Lo que revisas: «me piden», la herramienta y el tacho con razón."])))
    # 7 · reto en equipo: la dinámica de socialización del área
    lis = "".join(f"<li>{E(p)}</li>" for p in pasos_d)
    sc.append(dict(m=3, min=min_d, html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--m4)">Reto en equipo · {min_d} min</span>'
        f'<span class="kicker">{E(C8.get("formato", "en equipos"))} · cada uno responde en su esquema</span></div>'
        f'<h2>{E(nom_d)}</h2>'
        f'<div class="grid c2 mt"><div class="card edge" style="--accent:var(--m4)"><h3>Cómo se hace</h3>'
        f'<ol class="pasos">{lis}</ol></div>'
        f'<div class="card"><h3>Qué vas a necesitar</h3><p>{E(material_d)}</p>'
        f'<h3 class="mt">Las asignadas</h3><div class="nums">{_asignadas_eco()}</div></div></div>'),
        guia=g(3, "Que la discusión sea compartida y el registro individual.",
               apoyo=["Qué pieza del esquema entrena: " + entrena_d,
                      "La regla para aprobar cualquier dinámica: si no puedes decir qué paso del esquema "
                      "está ejercitando, es recreo, no clase.",
                      "Si un equipo llena un solo esquema para todos, no cuenta: cada uno escribe en el suyo."])))
    # 8 · evaluación individual
    sc.append(dict(m=4, html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--m5)">Evaluación individual</span>'
        f'<span class="kicker">En silencio · sin ayuda</span></div>'
        f'<h2>Solo, como en la prueba</h2>'
        f'<div class="card big edge mt" style="--accent:var(--m5)"><p class="lead">{E(_primera_frase(fases[4]))}</p>'
        f'<p class="sub">El salvavidas: dónde me perdí y la pista que no vi.</p></div>'
        f'<div class="nums mt">{_asignadas_eco()}</div>'),
        guia=g(4, "Tener un dato individual de cómo quedó la estrategia, sin la ayuda del grupo.",
               apoyo=["No respondas dudas en estos 20 minutos: lo que no sepa, va al salvavidas."])))
    # 9 · cierre
    sc.append(dict(m=5, html=(
        f'<div class="eyebrow"><span class="min" style="--accent:var(--m6)">Cierre</span>'
        f'<span class="kicker">El cierre del área</span></div>'
        f'<h2>¿Qué pista no viste en el simulacro y hoy sí ves?</h2>'
        f'<div class="grid c2 mt"><div class="card big edge" style="--accent:var(--m6)"><h3>Antes de salir</h3>'
        f'<p class="lead">{E(fases[5])}</p></div>'
        f'<div class="card edge" style="--accent:var(--m4)"><h3>Lo que me llevo</h3>'
        f'<p>Una frase por esquema, que te sirva en el examen de verdad. No la copia de la respuesta: '
        f'lo que vas a hacer distinto la próxima vez.</p></div></div>'),
        guia=g(5, "Que el estudiante se lleve por escrito lo que va a hacer distinto en la prueba real.",
               apoyo=[C8.get("alcance") or "",
                      "Si nadie escribió algo distinto de la respuesta en «lo que me llevo», la estrategia no "
                      "se instaló todavía: anótalo en el registro para el reporte de los especialistas."])))
    sc[-1]["guia"]["apoyo"] = [x for x in sc[-1]["guia"]["apoyo"] if x]
    return sc


def escenas_clase(A, mis):
    claves = A.claves_libro(mis)
    avisos = avisos_por_pregunta(A, mis)
    qs = A.preguntas_icfes(mis)
    banco = A.banco(mis)
    sc = [esc_portada(A, mis), esc_reglas(A, mis), esc_activacion(A, mis),
          esc_dinamica(A, mis, 0, 0), esc_problematizadora(A, mis)]
    pares = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    for j, (a, b_) in enumerate(pares):
        sc.append(esc_bloque(A, mis, a, b_, claves, avisos))
        if j in (1, 2, 3):                       # cada 18 minutos, la dinámica del bloque
            sc.append(esc_dinamica(A, mis, j, 2))
    sc.append(esc_reto(A, mis))
    for k, q in enumerate(qs, 1):
        sc.append(esc_icfes(A, mis, k, q, banco[k - 1]["clave"], A.textos.get((mis, k), {})))
    sc.append(esc_cierre(A, mis))
    return sc


# ─────────────────────────────── la página ───────────────────────────────
def colores_css(A):
    c = A.colores
    return (f'--area:{A.color}; --azul:{c["azul"]}; --oro:{c["oro"]}; --morado:{c["morado"]}; '
            f'--verde:{c["verde"]};\n'
            f'  --m1:{A.color}; --m2:{c["m2"]}; --m3:{c["m3"]}; --m4:{c["m4"]}; --m5:{c["m5"]}; '
            f'--m6:{c["m6"]};' +
            "".join(f' --{k}:{v};' for k, v in c.items() if k not in PALETA))   # p. ej. rojo


def pagina(A, titulo, sub, escenas, nombre_mom):
    logo = "data:image/png;base64," + base64.b64encode(open(LOGO, "rb").read()).decode()
    datos = json.dumps(escenas, ensure_ascii=False).replace("__LOGO__", logo).replace("</", "<\\/")
    mom = json.dumps([dict(n=i + 1, nom=f[0], min=f[1], c=f"--m{i+1}") for i, f in enumerate(A.P.FASES)],
                     ensure_ascii=False)
    return (PLANTILLA.replace("__COLORES__", colores_css(A)).replace("__FUERTE__", E(A.fuerte))
            .replace("__TITULO__", E(titulo)).replace("__SUB__", E(sub))
            .replace("__NOMBRE__", E(nombre_mom)).replace("__LOGOSRC__", logo)
            .replace("__ESCENAS__", datos).replace("__MOM__", mom))


def construir(A, misiones=range(1, 7), simulacro=True):
    """Escribe las guías del área en A.out y devuelve [(archivo, n.º de diapositivas)]."""
    os.makedirs(A.out, exist_ok=True)
    hechos = []
    for mis in misiones:
        d = A.P.MISIONES[mis]
        sc = escenas_clase(A, mis)
        f = os.path.join(A.out, f"{A.prefijo}_Clase{mis}_Mision{mis}.html")
        open(f, "w", encoding="utf-8").write(
            pagina(A, f"{A.nombre} · Clase {mis}", f"Momento {mis} · {d['comp']} · páginas {d['pags']}",
                   sc, f"{A.nombre} · Clase {mis}"))
        hechos.append((f, len(sc)))
    if simulacro:
        sc7, sc8 = escenas_clase7(A), escenas_clase8(A)
        s7, s8 = subtitulos_simulacro(A)
        f7 = os.path.join(A.out, f"{A.prefijo}_Clase7_Simulacro.html")
        open(f7, "w", encoding="utf-8").write(pagina(A, f"{A.nombre} · Clase 7", s7, sc7,
                                                     f"{A.nombre} · Clase 7"))
        f8 = os.path.join(A.out, f"{A.prefijo}_Clase8_Devolucion.html")
        open(f8, "w", encoding="utf-8").write(pagina(A, f"{A.nombre} · Clase 8", s8, sc8,
                                                     f"{A.nombre} · Clase 8"))
        hechos += [(f7, len(sc7)), (f8, len(sc8))]
    for f, n in hechos:
        print(f"{os.path.basename(f):34s} {n:2d} diapositivas · {os.path.getsize(f)//1024} KB")
    return hechos


PLANTILLA = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>__TITULO__</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap">
<style>[hidden]{display:none!important}
:root{
  --display:"Archivo","Segoe UI",system-ui,sans-serif;
  --text:"Source Sans 3","Segoe UI",system-ui,sans-serif;
  __COLORES__
  --ink:#1B1F27; --muted:#5C6472; --faint:#A9B0BB; --line:#E3E7ED; --paper:#FFFFFF; --bg:#F6F4F1;
  color-scheme:light;
}
*{box-sizing:border-box}
html,body{height:100%;margin:0}
body{background:var(--bg);color:var(--ink);font-family:var(--text);font-size:clamp(16px,1.25vw,21px);line-height:1.5}
#app{display:grid;grid-template-rows:auto 1fr auto;height:100%}
#top{display:flex;align-items:center;gap:clamp(10px,1.4vw,22px);padding:10px clamp(14px,2vw,28px);background:var(--paper);flex-wrap:wrap}
.logo img{height:clamp(28px,2.6vw,40px);display:block}
#mom{display:flex;align-items:center;gap:12px;flex:1;min-width:200px}
#momdot{width:clamp(30px,2.4vw,40px);height:clamp(30px,2.4vw,40px);border-radius:50%;display:grid;place-items:center;color:#fff;font-family:var(--display);font-weight:800;background:var(--faint)}
#momnom{font-family:var(--display);font-weight:700;font-size:clamp(15px,1.2vw,20px)}
#momsub{color:var(--muted);font-size:.85em}
#clock{display:flex;align-items:center;gap:8px}
#tnum{font-family:var(--display);font-weight:800;font-size:clamp(20px,1.8vw,30px);font-variant-numeric:tabular-nums;min-width:4.2ch;text-align:right}
#tnum.over{color:var(--area)}
.btn{appearance:none;font:inherit;font-size:.86em;font-weight:600;border:1.5px solid var(--line);background:var(--paper);color:var(--ink);border-radius:10px;padding:7px 14px;cursor:pointer}
.btn:hover{border-color:var(--faint)}
.btn.solid{background:var(--area);border-color:var(--area);color:#fff}
.btn[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
#stage{overflow:auto;padding:clamp(18px,3vw,48px) clamp(16px,4vw,72px)}
#wrap{max-width:1500px;margin:0 auto}
#wrap.enter{animation:ent .28s ease-out}
@keyframes ent{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
#bot{display:flex;align-items:center;gap:12px;padding:10px clamp(14px,2vw,28px);background:var(--paper)}
#prog{flex:1;height:6px;border-radius:4px;background:var(--line);overflow:hidden}
#prog i{display:block;height:100%;background:var(--area);transition:width .25s}
#count{font-variant-numeric:tabular-nums;color:var(--muted);font-size:.85em}
#hint{color:var(--faint);font-size:.8em}
@media (max-width:760px){#hint{display:none}}
h1{font-family:var(--display);font-weight:800;font-size:clamp(34px,4.2vw,68px);line-height:1.05;margin:.2em 0 .25em;text-wrap:balance;letter-spacing:-.01em}
h2{font-family:var(--display);font-weight:800;font-size:clamp(26px,2.8vw,46px);line-height:1.1;margin:.25em 0 .3em;text-wrap:balance}
h3{font-family:var(--display);font-weight:700;font-size:clamp(18px,1.5vw,26px);margin:.1em 0 .4em;line-height:1.2}
p{margin:.35em 0 .6em}
.lead{font-size:1.2em;line-height:1.45;max-width:70ch}
.sub{color:var(--muted)}
.mt{margin-top:clamp(14px,1.8vw,26px)}
.logo-xl img{height:clamp(54px,6vw,96px);margin-bottom:12px}
.eyebrow{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center}
.tag,.min,.membrete{display:inline-block;border-radius:999px;padding:3px 12px;font-size:.78em;font-weight:700;letter-spacing:.02em}
.tag{background:var(--ink);color:#fff}
.min{background:var(--accent,var(--area));color:#fff}
.membrete{border:1.5px solid var(--line);color:var(--muted)}
.kicker{color:var(--muted);font-size:.85em;letter-spacing:.06em;text-transform:uppercase;font-weight:700}
.grid{display:grid;gap:clamp(12px,1.4vw,22px)}
.c2{grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr))}
.c3{grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr))}
.grid>*{min-width:0}
.card{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:clamp(14px,1.6vw,24px)}
.card.edge{border-left:6px solid var(--accent,var(--area))}
.card.big .lead{font-size:1.3em}
.step{display:flex;gap:14px;align-items:center;background:var(--paper);border:1px solid var(--line);border-left:5px solid var(--accent);border-radius:12px;padding:10px 14px}
.step .k{width:2em;height:2em;border-radius:50%;display:grid;place-items:center;background:var(--accent);color:#fff;font-family:var(--display);font-weight:800;flex:none}
.note{border-left:5px solid var(--accent,var(--area));background:var(--paper);border-radius:10px;padding:10px 16px;margin-top:12px}
.cita{font-family:var(--display);font-weight:600;line-height:1.35;background:var(--paper);border-left:6px solid var(--area);border-radius:12px;padding:clamp(16px,2vw,30px);margin:18px 0}
.cita.xl{font-size:clamp(24px,2.6vw,44px)}
.ctl{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.tally .n{display:inline-block;min-width:1.6em;margin-left:6px;padding:0 6px;border-radius:6px;background:var(--bg);font-variant-numeric:tabular-nums}
.pasos{margin:.2em 0 0;padding-left:1.3em}.pasos li{margin:.3em 0}
.sello{margin-top:12px;border:2px dashed var(--oro);border-radius:12px;padding:10px 14px;background:#FDF6EA}
.sello b{display:block;color:var(--oro);font-size:.8em;letter-spacing:.06em;text-transform:uppercase}
.clave{margin-top:12px;display:flex;align-items:center;gap:10px;font-weight:600}
.keychip{display:inline-grid;place-items:center;width:2.2em;height:2.2em;border-radius:10px;color:#fff;font-family:var(--display);font-weight:800;font-size:1.2em}
.aviso{margin-top:10px;border-radius:10px;padding:10px 14px;background:#FBEFEF;border-left:5px solid var(--area);font-size:.92em}
.aviso.sev-aten{background:#EDF5EE;border-left-color:var(--verde)}
.aviso.sev-medi{background:#FDF5E7;border-left-color:var(--oro)}
.icfes .texto{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:clamp(14px,1.6vw,24px);max-height:62vh;overflow:auto;font-size:.95em}
.enun{font-weight:600;font-size:1.08em}
.ops{display:grid;gap:8px;margin-top:10px}
.op{display:flex;gap:12px;align-items:flex-start;background:var(--paper);border:1.5px solid var(--line);border-radius:12px;padding:10px 14px}
.op .L{flex:none;width:1.8em;height:1.8em;border-radius:8px;display:grid;place-items:center;background:var(--bg);font-family:var(--display);font-weight:800}
.op.ok{border-color:var(--verde);background:#EDF5EE}.op.ok .L{background:var(--verde);color:#fff}
.picks{display:flex;flex-wrap:wrap;gap:8px}
.pick[aria-pressed="true"]{background:var(--area);border-color:var(--area);color:#fff}
#scrim{position:fixed;inset:0;background:rgba(15,18,24,.35);opacity:0;pointer-events:none;transition:opacity .2s}
#scrim.on{opacity:1;pointer-events:auto}
#guia{position:fixed;top:0;right:0;height:100%;width:min(520px,92vw);background:var(--paper);box-shadow:-12px 0 40px rgba(0,0,0,.18);transform:translateX(102%);transition:transform .25s;display:flex;flex-direction:column;z-index:10}
#guia.open{transform:none}
#guiahead{display:flex;align-items:center;gap:12px;padding:14px 18px;background:var(--bg)}
#guiabody{overflow:auto;padding:16px 20px 30px;font-size:.92em}
.gbox{border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin-bottom:12px}
.gbox h4{margin:0 0 6px;font-family:var(--display);font-size:.8em;letter-spacing:.07em;text-transform:uppercase;color:var(--area)}
.gbox ul{margin:0;padding-left:1.1em}.gbox li{margin:.35em 0}
.gbox.como{background:#F6F7F9}.gbox.como h4{color:var(--muted)}
.gbox.apoyo{background:#FDF6EA;border-color:#EAD9B4}.gbox.apoyo h4{color:var(--oro)}
.examen{background:var(--paper);border:1px solid var(--line);border-left:8px solid var(--area);border-radius:22px;padding:clamp(16px,2.4vw,40px);margin-top:clamp(12px,1.6vw,24px);text-align:center}
.relojxl{font-family:var(--display);font-weight:800;font-size:clamp(96px,17vw,280px);line-height:1;font-variant-numeric:tabular-nums;letter-spacing:-.02em}
.relojxl.over{color:var(--area)}
.exhoras{display:flex;justify-content:center;flex-wrap:wrap;gap:8px 36px;color:var(--muted);font-size:1.15em;margin-top:10px}
.exhoras b{color:var(--ink);font-variant-numeric:tabular-nums}
.nbig{font-family:var(--display);font-weight:800;font-size:clamp(40px,4vw,64px);line-height:1;color:var(--accent,var(--area))}
.asig{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;padding:8px 0}
.asig .k{width:2em;height:2em;border-radius:50%;display:grid;place-items:center;color:#fff;font-family:var(--display);font-weight:800;flex:none}
.asig label{display:flex;align-items:center;gap:8px;font-weight:600;color:var(--muted)}
.asig label.w{flex:1;min-width:min(100%,260px)}
.campo{font:inherit;font-size:1.1em;font-weight:700;color:var(--ink);border:none;border-bottom:2px dashed var(--faint);background:transparent;padding:4px 6px;min-width:0;flex:1;outline:none}
.campo.n{width:4.5em;flex:none;text-align:center}
.campo:focus{border-bottom-color:var(--area)}
.nums1{border:1.5px solid var(--line);border-radius:999px;padding:3px 14px;background:var(--paper);font-weight:600;color:var(--muted)}
.nums1 b{color:var(--ink)}
.pides{display:flex;flex-wrap:wrap;gap:10px 18px;font-size:1.08em}
.pide{display:inline-flex;align-items:center;gap:8px}
.chk{display:inline-block;width:20px;height:20px;border:2px solid var(--area);border-radius:4px;background:#fff;flex:none}
.herrs{display:grid;gap:clamp(12px,1.4vw,22px);grid-template-columns:repeat(auto-fit,minmax(min(100%,230px),1fr))}
.herr{display:flex;align-items:center;gap:14px;background:var(--paper);border:1px solid var(--line);border-left:6px solid var(--area);border-radius:16px;padding:14px 18px;font-size:1.12em}
.herr svg{flex:none}
</style>
</head>
<body>
<div id="app">
  <div id="top">
    <span class="logo"><img src="__LOGOSRC__" alt="EDUCATE · Para el Saber"></span>
    <div id="mom"><div id="momdot">·</div>
      <div style="min-width:0"><div id="momnom">__NOMBRE__</div><div id="momsub">__SUB__</div></div></div>
    <div id="clock"><span id="tnum">—</span>
      <button class="btn" id="play">Iniciar</button>
      <button class="btn" id="reset" aria-label="Reiniciar cronómetro">↺</button></div>
    <button class="btn" id="gbtn" aria-pressed="false">Guía del profe</button>
  </div>
  <div id="stage"><div id="wrap"></div></div>
  <div id="bot">
    <button class="btn" id="prev" aria-label="Anterior">←</button>
    <button class="btn" id="next" aria-label="Siguiente">→</button>
    <div id="prog"><i style="width:0%"></i></div>
    <span id="count">1 / 1</span>
    <span id="hint">← → avanzar · G guía · T cronómetro</span>
  </div>
</div>
<div id="scrim"></div>
<aside id="guia" aria-label="Guía del profe">
  <div id="guiahead"><b style="font-family:var(--display);flex:1">Guía del profe</b>
    <button class="btn" id="gclose" aria-label="Cerrar">✕</button></div>
  <div id="guiabody"></div>
</aside>
<script>
(function(){
"use strict";
var SC = __ESCENAS__;
var MOM = __MOM__;
var NOMBRE = document.getElementById("momnom").textContent, SUB = document.getElementById("momsub").textContent;
var $ = function(s){ return document.querySelector(s); };
var wrap = $("#wrap"), stage = $("#stage"), i = 0;
var tBase = 0, tLeft = 0, tOn = false, tick = null;
var elegidas = [];
function esc(t){ return String(t).replace(/[&<>"]/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c];}); }

function paintClock(){
  var n = $("#tnum");
  if(!tBase){ n.textContent = "—"; n.classList.remove("over"); return; }
  var s = Math.abs(tLeft), mm = Math.floor(s/60), ss = s%60;
  n.textContent = (tLeft<0?"+":"") + mm + ":" + (ss<10?"0":"") + ss;
  n.classList.toggle("over", tLeft<0);
}
function setTimer(min){
  tBase = min||0; tLeft = tBase*60; tOn = false;
  if(tick){ clearInterval(tick); tick = null; }
  $("#play").textContent = "Iniciar"; paintClock();
}
function toggleTimer(){
  if(!tBase) return;
  tOn = !tOn; $("#play").textContent = tOn ? "Pausar" : "Seguir";
  if(tick){ clearInterval(tick); tick = null; }
  if(tOn) tick = setInterval(function(){ tLeft--; paintClock(); }, 1000);
  paintClock();
}
// cronómetro de la prueba (clase 7): aparte del de la barra, no se reinicia al cambiar de diapositiva
var EX = {base:0, left:0, on:false, t:null, ini:null};
function hhmm(d){ return d.getHours() + ":" + (d.getMinutes()<10?"0":"") + d.getMinutes(); }
function exPaint(){
  var box = wrap.querySelector("[data-examen]"); if(!box) return;
  if(!EX.base){ EX.base = +box.dataset.examen; EX.left = EX.base*60; }
  var s = Math.abs(EX.left), mm = Math.floor(s/60), ss = s%60;
  var n = box.querySelector("[data-exnum]");
  n.textContent = (EX.left<0?"+":"") + mm + ":" + (ss<10?"0":"") + ss;
  n.classList.toggle("over", EX.left<0);
  box.querySelector("[data-exini]").textContent = EX.ini ? hhmm(EX.ini) : "—";
  box.querySelector("[data-exfin]").textContent = EX.on ? hhmm(new Date(Date.now() + EX.left*1000)) : (EX.ini ? "en pausa" : "—");
  var p = box.querySelector('[data-ex="play"]');
  p.textContent = EX.on ? "Pausar" : (EX.ini ? "Seguir" : "Iniciar la prueba");
}
function exToggle(){
  if(!EX.base) exPaint();
  EX.on = !EX.on;
  if(EX.t){ clearInterval(EX.t); EX.t = null; }
  if(EX.on){ if(!EX.ini) EX.ini = new Date(); EX.t = setInterval(function(){ EX.left--; exPaint(); }, 1000); }
  exPaint();
}
function exReset(){
  if(EX.ini && !window.confirm("¿Volver a poner el cronómetro de la prueba en cero?")) return;
  if(EX.t){ clearInterval(EX.t); EX.t = null; }
  EX.on = false; EX.ini = null; EX.left = EX.base*60; exPaint();
}
// casillas que llena el profe (clase 8): se guardan mientras la página esté abierta
var CAMPOS = {};
function pintaCampos(){
  [].forEach.call(wrap.querySelectorAll("[data-campo]"), function(x){ x.value = CAMPOS[x.dataset.campo] || ""; });
  [].forEach.call(wrap.querySelectorAll("[data-eco]"), function(x){ x.textContent = CAMPOS[x.dataset.eco] || "—"; });
}
function guiaHTML(g){
  if(!g) return '<p class="sub">Sin notas para esta diapositiva.</p>';
  var h = '<div class="gbox"><h4>Objetivo</h4><p>'+esc(g.obj)+'</p></div>';
  if(g.decir && g.decir.length) h += '<div class="gbox"><h4>Qué haces y qué dices</h4><ul>'+
     g.decir.map(function(d){ return '<li>'+esc(d)+'</li>'; }).join("")+'</ul></div>';
  if(g.como) h += '<div class="gbox como"><h4>Lo que no haces</h4><p>'+esc(g.como)+'</p></div>';
  if(g.apoyo && g.apoyo.length) h += '<div class="gbox apoyo"><h4>__FUERTE__</h4><ul>'+
     g.apoyo.map(function(d){ return '<li>'+esc(d)+'</li>'; }).join("")+'</ul></div>';
  return h;
}
function pintaElegidas(){
  var box = document.getElementById("elegidas"); if(!box) return;
  if(!elegidas.length){ box.innerHTML = '<p class="sub">Vuelve a la diapositiva anterior y escoge las cinco.</p>'; return; }
  box.innerHTML = elegidas.map(function(t,k){
    return '<div class="card edge" style="--accent:var(--m'+((k%6)+1)+')"><h3>'+(k+1)+'. '+esc(t)+'</h3>'+
      '<p class="sub">Busca esta pregunta en tu simulacro y en la hoja de taller de la misma estrategia.</p></div>';
  }).join("");
}
function go(n){
  var prev = SC[i];
  i = Math.max(0, Math.min(SC.length-1, n));
  var s = SC[i];
  wrap.innerHTML = s.html;
  wrap.classList.remove("enter"); void wrap.offsetWidth; wrap.classList.add("enter");
  stage.scrollTop = 0;
  var m = s.m!=null ? MOM[s.m] : null;
  $("#momdot").style.background = m ? "var("+m.c+")" : "var(--faint)";
  $("#momdot").textContent = m ? m.n : "·";
  $("#momnom").textContent = m ? m.nom : NOMBRE;
  $("#momsub").textContent = m ? (m.min+" minutos") : SUB;
  var want = s.min!=null ? s.min : (m ? m.min : 0);
  var cambio = !prev || prev===s || prev.m!==s.m || (prev.min||null)!==(s.min||null);
  if(cambio) setTimer(want);
  $("#count").textContent = (i+1)+" / "+SC.length;
  $("#prog i").style.width = (SC.length>1 ? i/(SC.length-1)*100 : 100)+"%";
  $("#guiabody").innerHTML = guiaHTML(s.guia);
  [].forEach.call(wrap.querySelectorAll("[data-pick]"), function(b){
    b.setAttribute("aria-pressed", elegidas.indexOf(b.textContent)>=0 ? "true" : "false"); });
  pintaElegidas();
  pintaCampos();
  exPaint();
  $("#clock").style.visibility = wrap.querySelector("[data-examen]") ? "hidden" : "";   // la prueba tiene su reloj
}
wrap.addEventListener("input", function(e){
  var x = e.target; if(!x.dataset || !x.dataset.campo) return;
  CAMPOS[x.dataset.campo] = x.value;
});
wrap.addEventListener("click", function(e){
  var b = e.target.closest("button"); if(!b) return;
  if(b.dataset.ex==="play") exToggle();
  if(b.dataset.ex==="reset") exReset();
  if(b.dataset.show){ var t = document.getElementById(b.dataset.show); if(t) t.hidden = !t.hidden; }
  if(b.dataset.showgrupo){
    var g = wrap.querySelectorAll('[data-grupo="'+b.dataset.showgrupo+'"]'), abrir = g.length && g[0].hidden;
    [].forEach.call(g, function(x){ x.hidden = !abrir; });
    b.textContent = abrir ? "Ocultar las claves" : "Revelar las claves";
  }
  if(b.dataset.clave){
    var box = document.getElementById(b.dataset.clave), ok = box.querySelector('[data-op="'+b.dataset.k+'"]');
    var on = ok && !ok.classList.contains("ok");
    [].forEach.call(box.querySelectorAll(".op"), function(o){ o.classList.remove("ok"); });
    if(on) ok.classList.add("ok");
    b.textContent = on ? "Ocultar la clave" : "Revelar la clave";
  }
  if(b.dataset.tally){ var n = document.getElementById(b.dataset.tally); n.textContent = (+n.textContent||0)+1; }
  if(b.dataset.reset){ [].forEach.call(wrap.querySelectorAll('[id^="'+b.dataset.reset+'"]'), function(x){
    if(x.classList.contains("n")) x.textContent = "0"; }); }
  if(b.dataset.pick!=null){
    var t = b.textContent, k = elegidas.indexOf(t);
    if(k>=0) elegidas.splice(k,1); else if(elegidas.length<5) elegidas.push(t);
    b.setAttribute("aria-pressed", elegidas.indexOf(t)>=0 ? "true" : "false");
  }
});
function setGuia(on){ $("#guia").classList.toggle("open", on); $("#scrim").classList.toggle("on", on);
  $("#gbtn").setAttribute("aria-pressed", on ? "true" : "false"); }
$("#next").addEventListener("click", function(){ go(i+1); });
$("#prev").addEventListener("click", function(){ go(i-1); });
$("#play").addEventListener("click", toggleTimer);
$("#reset").addEventListener("click", function(){ setTimer(tBase); });
$("#gbtn").addEventListener("click", function(){ setGuia(!$("#guia").classList.contains("open")); });
$("#gclose").addEventListener("click", function(){ setGuia(false); });
$("#scrim").addEventListener("click", function(){ setGuia(false); });
document.addEventListener("keydown", function(e){
  var t = e.target.tagName; if(t==="INPUT"||t==="TEXTAREA"||e.target.isContentEditable) return;
  if(e.key==="ArrowRight"||e.key==="PageDown"||e.key===" "){ go(i+1); e.preventDefault(); }
  else if(e.key==="ArrowLeft"||e.key==="PageUp"){ go(i-1); e.preventDefault(); }
  else if(e.key==="Home"){ go(0); e.preventDefault(); }
  else if(e.key==="End"){ go(SC.length-1); e.preventDefault(); }
  else if(e.key==="g"||e.key==="G"){ setGuia(!$("#guia").classList.contains("open")); }
  else if(e.key==="t"||e.key==="T"){ if(wrap.querySelector("[data-examen]")) exToggle(); else toggleTimer(); }
  else if(e.key==="Escape"){ setGuia(false); }
});
go(0);
})();
</script>
</body>
</html>
"""
