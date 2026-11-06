#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUÍAS DE CLASE PROYECTABLES · LECTURA CRÍTICA · «clase viva».

Una por clase: seis de contenido y las dos del simulacro. Mismo modelo del piloto
aprobado de Matemáticas (Clase_viva_estudiantes.html):
  · barra superior con el momento de la clase y un cronómetro que se reinicia solo
    cuando cambia el momento;
  · la guía del profe en un panel lateral (tecla G), con el objetivo, qué hacer y decir,
    y una sección «Si la lectura crítica no es tu fuerte»;
  · ← → para avanzar, T para el cronómetro, Esc para cerrar la guía.

Todo sale de lo que ya está construido y verificado: el planeador (plan_lc), las claves
del libro (docstrings de lcN.py), las preguntas ICFES (lcN_icfes.py), los textos completos
(TEXTOS_GUIA_DOCENTE.md) y los sellos (matriz.py). Ninguna clave aparece en pantalla
hasta que el profe la revela con un botón.
"""
import base64, html, json, os, re, importlib
import plan_lc as P
from textos_lc import leer as leer_textos

OUT = "/home/claude/libro/guias_lc/"
LOGO = "/home/claude/libro/logo_educate.png"
FICFES = "Pregunta oficial ICFES · Saber 11"      # sin año: ninguna se cruzó contra un cuadernillo
E = lambda t: html.escape(str(t), quote=True)

TEXTOS, ADVERTENCIAS = leer_textos()

# ─────────────── lo que el profe tiene que poder explicar en cada sello ───────────────
# Una definición corta, un ejemplo y la pregunta que lo destraba. Es para el profe que
# no viene de Lenguaje: lo que el cuaderno le pide que instale, dicho sin jerga.
SABERES = {
 (1, 6): ("Eufemismo", "Una palabra suave que reemplaza a una dura para que el hecho pese menos. "
          "«Ajuste de tarifas» por «alza»; «daños colaterales» por «civiles muertos». Las "
          "instituciones lo usan porque nombrar es decidir qué siente el que escucha.",
          "¿Qué palabra dura está escondida detrás de esta?"),
 (1, 7): ("Tipos de narrador", "En primera persona narra lo que vive («yo»). En tercera "
          "omnisciente sabe todo y entra en la cabeza de todos. En tercera testigo cuenta lo que "
          "ve, no lo que los demás piensan.",
          "¿Este narrador sabe lo que el personaje está pensando?"),
 (1, 9): ("Metáfora que adorna y metáfora que sostiene", "La que adorna se puede quitar y la "
          "idea queda en pie. La que sostiene, si la quitas, la idea se cae: el argumento estaba "
          "construido sobre ella.",
          "Reescribe la frase sin la metáfora. ¿Dice lo mismo?"),
 (1, 10): ("Monólogo interior", "El narrador deja hablar al personaje dentro de su cabeza, sin "
           "comillas y sin «dijo». Se nota porque cambia el tono o aparece un «yo» sin aviso.",
           "¿Quién está hablando en esta frase: el narrador o el personaje?"),
 (2, 3): ("Metáfora extendida", "Una comparación que no se usa una vez: organiza el texto "
          "entero. Cada parte del texto corresponde a una parte de la imagen.",
          "Si el texto fuera la imagen, ¿qué parte de la imagen es este párrafo?"),
 (2, 10): ("Conectores lógicos", "Dicen qué relación hay entre dos ideas. Causa: porque, ya que. "
           "Consecuencia: por eso, así que. Contraste: pero, sin embargo. Adición: además. "
           "Reformulación: es decir.",
           "Cambia el conector por otro de la lista. ¿Se rompe la frase?"),
 (3, 2): ("Paradoja", "Juntar dos cosas que parecen excluirse y que, pensadas, son las dos "
          "ciertas. «Vivimos más conectados y más solos.»",
          "¿Qué dos cosas pone el autor juntas que no deberían ir juntas?"),
 (3, 8): ("Ironía visual por inversión de papeles", "La caricatura pone a cada quien en el lugar "
          "del otro: el paciente atiende al médico. El chiste es el cambio; la crítica es lo que "
          "ese cambio deja ver.",
          "¿Quién está haciendo lo que normalmente hace el otro?"),
 (3, 9): ("El narrador que observa", "Una tercera persona que no sabe lo que el personaje piensa "
          "y conjetura: «parecía», «quizá», «como si». Lo que el narrador supone no es un hecho "
          "del texto.",
          "¿El narrador lo sabe o lo está suponiendo?"),
 (4, 1): ("La construcción consecutiva «tal… que», «tan… que»", "La primera parte da la "
          "intensidad y la segunda la consecuencia. Siempre apunta hacia adelante: lo que viene "
          "después del «que» es el resultado.",
          "¿Qué pasó por culpa de que fuera tan…?"),
 (4, 3): ("El texto discontinuo", "No se lee en línea, de izquierda a derecha: se lee por "
          "bloques. Título, gráfico, recuadro y fuente tienen cada uno su función.",
          "¿Qué bloque leíste primero y por qué ese?"),
 (4, 10): ("La carta al editor", "El texto de un lector que responde a algo publicado. Tiene "
           "destinatario, una posición y casi siempre pide algo. En redes es lo mismo, en corto "
           "y con etiquetas.",
           "¿A qué está respondiendo esta persona y qué pide?"),
 (5, 4): ("Ironía y sarcasmo", "Los dos dicen lo contrario de lo que quieren decir. El sarcasmo "
          "además quiere herir a alguien concreto. La ironía puede ser amable; el sarcasmo no.",
          "¿A quién le duele esta frase?"),
 (5, 6): ("Alegoría", "Un sistema de equivalencias: cada elemento de la historia representa algo. "
          "En la caverna de Platón, las sombras son las apariencias y el que sale es el que "
          "conoce. No es una metáfora suelta.",
          "¿Qué representa cada pieza de esta historia?"),
 (5, 8): ("Citar a una autoridad", "Explica y respalda una idea, pero no la demuestra. Que un "
          "experto lo diga no lo vuelve cierto: hay que mirar qué razones da.",
          "Si quitas al experto, ¿queda alguna razón en pie?"),
 (6, 1): ("El blog como tipo de texto", "Autor con nombre, tesis propia en primera persona, tono "
          "cercano y un público que puede responder en los comentarios.",
          "¿Quién escribe, qué defiende y a quién le habla?"),
 (6, 4): ("El meme como marca de tono", "No agrega información: agrega actitud, casi siempre "
          "burla o ironía. Si quitas la imagen, lo que se dice no cambia; cómo se dice, cambia "
          "todo.",
          "Sin la imagen, ¿qué se pierde?"),
 (6, 6): ("Paradoja", "Dos cosas ciertas al mismo tiempo que tiran en direcciones opuestas: lo "
          "invaluable también tiene precio. No es una contradicción ni un error del autor: es la "
          "forma del argumento.",
          "¿Cuáles son las dos mitades, y por qué las dos son verdad?"),
}

# Una frase corta y original para la activación de cada clase: dos o tres renglones,
# sin contexto, con una palabra que pesa más que las otras.
ACTIVACION = {
 1: ("El Gobierno anunció un «ajuste» en las tarifas del transporte. Desde el lunes, el "
     "pasaje cuesta cuatrocientos pesos más.", "«ajuste»: dice poco a propósito"),
 2: ("Muchos creen que leer rápido es leer bien. Pero quien lee rápido suele recordar el tema "
     "y olvidar el argumento.", "la segunda frase no explica: objeta"),
 3: ("Durante años la plaza estuvo vacía. Sin embargo, desde que pusieron la cancha, los "
     "vecinos bajan todas las tardes.", "«sin embargo»: ahí gira el texto"),
 4: ("La lluvia fue tan fuerte que el río se salió en tres barrios.",
     "«tan… que»: lo que viene después es la consecuencia"),
 5: ("Cada minuto que pasas en la fila del banco es un minuto que tu dinero no trabaja. Abre "
     "tu cuenta desde el celular.", "el texto no informa: quiere que hagas algo"),
 6: ("Tomamos mil fotos del concierto y no recordamos ninguna canción.",
     "dos cosas ciertas que tiran para lados opuestos"),
}


# ───────────────────────────── datos verificados ─────────────────────────────
def claves_libro(mis):
    doc = open(f"/home/claude/libro/lc{mis}.py", encoding="utf-8").read()[:3000]
    return {int(n): k for n, k in re.findall(r"(\d+)·([A-D])", doc)}


def preguntas_icfes(mis):
    mod = importlib.import_module(f"lc{mis}_icfes")
    return [getattr(mod, k) for k in ("QA", "QB", "QC", "QD")]


def avisos_por_pregunta(mis):
    """«preg. 4 y 5», «preg. 10», «texto 8 a 10» → {pregunta: aviso}"""
    out = {}
    for preg, sev, que, hacer in P.AVISOS.get(mis, []):
        nums = [int(x) for x in re.findall(r"\d+", preg)]
        if " a " in preg and len(nums) == 2:
            nums = list(range(nums[0], nums[1] + 1))
        for n in nums:
            out.setdefault(n, []).append((sev, que, hacer))
    return out


def sello(mis, preg):
    for s in P.SELLOS:
        if str(s[1]) == str(mis) and str(s[3]) == str(preg):
            return s
    return None


# ───────────────────────────── piezas de las escenas ─────────────────────────────
COL = {1: "var(--m1)", 2: "var(--m2)", 3: "var(--m3)", 4: "var(--m4)", 5: "var(--m5)", 6: "var(--m6)"}
EST_COL = ["var(--lc)", "var(--azul)", "var(--oro)", "var(--morado)"]


def guia(fase, decir=(), apoyo=()):
    nom, mins, c, obj, hace, como, material = P.FASES[fase]
    return dict(obj=obj, decir=list(decir) or list(hace), como=como, apoyo=list(apoyo))


def esc_portada(mis):
    d = P.MISIONES[mis]
    adv = ADVERTENCIAS.get(mis)
    apoyo = ["Abre esta guía con la tecla G en cada diapositiva: trae lo que dices y, debajo, "
             "lo que necesitas saber si Lectura Crítica no es tu área.",
             "El cronómetro arranca con T y se reinicia solo cuando cambia el momento de la clase."]
    if adv:
        apoyo.insert(0, "⚑ Esta clase tiene advertencia previa. Léela antes del sábado: " +
                     re.sub(r"\s+", " ", adv)[:700])
    h = (f'<div class="logo-xl"><img src="__LOGO__" alt="EDUCATE · Para el Saber"></div>'
         f'<div class="eyebrow"><span class="tag">Clase {mis} de 8</span>'
         f'<span class="kicker">Lectura Crítica · Componente {E(d["comp"])}</span></div>'
         f'<h1>{E(TITULOS[mis])}</h1>')
    h += (f'<p class="lead">{E(LEADS[mis])}</p>'
          f'<div class="grid c3 mt">'
          f'<div class="card edge" style="--accent:var(--m1)"><h3>Tu libro</h3>'
          f'<p class="sub">Las diez preguntas del momento {mis}</p></div>'
          f'<div class="card edge" style="--accent:var(--m4)"><h3>Tu cuaderno</h3>'
          f'<p class="sub">Páginas {E(d["pags"])}</p></div>'
          f'<div class="card edge" style="--accent:var(--m6)"><h3>Hoy</h3>'
          f'<p class="sub">120 minutos · 6 momentos · {E(d["competencia"])}</p></div></div>')
    return dict(m=None, html=h, guia=dict(obj="Que el grupo sepa desde el primer minuto qué va a "
                "pasar en estos 120 minutos y qué tiene que tener sobre la mesa.",
                decir=["«Libro abierto, cuaderno cerrado, lápiz. Esfero no: hoy vamos a "
                       "equivocarnos por escrito.»"], apoyo=apoyo))


TITULOS = {1: "Cada palabra pesa distinto", 2: "Un párrafo no dice: hace", 3: "Dónde gira el texto",
           4: "Las señales que el texto pone en el camino", 5: "Todo texto quiere algo",
           6: "Qué defiende, qué lo sostiene, qué lo traiciona"}
LEADS = {1: "Hoy no vamos a leer más rápido. Vamos a dejar de pasar los ojos: cada palabra pesa "
            "distinto, y la respuesta está en el renglón, no en lo que uno cree.",
         2: "Hoy la pregunta no es qué dice cada párrafo, sino qué está haciendo ahí: ejemplifica, "
            "objeta, matiza o cierra.",
         3: "Un texto de tres párrafos tiene dos bisagras. Hoy vamos a encontrarlas, y a leer lo "
            "que el autor juzga sin decirlo.",
         4: "Los conectores avisan lo que viene antes de que venga. Hoy aprendemos a leerlos como "
            "señales de tránsito.",
         5: "Nadie escribe por escribir. Hoy vamos a preguntarle a cada texto quién habla, desde "
            "dónde y qué quiere que hagamos.",
         6: "La última clase de contenido del área. Hoy todo se junta: la tesis en una línea, lo "
            "que se cae si quito un párrafo y la ironía que dice lo contrario."}


def esc_reglas(mis):
    filas = "".join(
        f'<div class="step" style="--accent:{COL[i+1]}"><div class="k">{i+1}</div>'
        f'<div><b>{E(f[0])}</b><span class="sub"> · {f[1]} min</span></div></div>'
        for i, f in enumerate(P.FASES))
    h = (f'<div class="eyebrow"><span class="kicker">Así vamos a trabajar</span></div>'
         f'<h2>Seis momentos, una sola regla</h2>'
         f'<div class="grid c2 mt"><div class="grid" style="gap:10px">{filas}</div>'
         f'<div class="card big edge" style="--accent:var(--lc)"><h3>La regla del cuaderno</h3>'
         f'<p class="lead">Si la hoja está limpia, no leíste: pasaste los ojos.</p>'
         f'<p>Primero se marca el texto —el subrayado y la pregunta al margen—, después se marca '
         f'la opción. Una respuesta correcta con el texto en blanco no cuenta como resuelta.</p>'
         f'</div></div>')
    return dict(m=None, html=h, guia=dict(
        obj="Que la regla quede dicha en voz alta antes de cualquier texto.",
        decir=["«La respuesta correcta con la hoja limpia no cuenta. ¿Por qué? Porque en la "
               "prueba nadie les va a decir si acertaron: tienen que saber de dónde lo sacaron.»"],
        apoyo=["Si alguien pregunta para qué marcar, la respuesta corta es: porque el ICFES "
               "pregunta tres o cuatro cosas distintas del mismo texto, y el que marcó la primera "
               "vez no tiene que volver a leerlo entero."]))


def esc_activacion(mis):
    txt, pista = ACTIVACION[mis]
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m1)">Activación</span>'
         f'<span class="kicker">Cuaderno cerrado</span></div>'
         f'<h2>¿Qué palabra pesa más aquí?</h2>'
         f'<blockquote class="cita xl">{E(txt)}</blockquote>'
         f'<p class="lead">Subráyala en tu cabeza. Escríbele al lado una pregunta.</p>'
         f'<div class="ctl"><button class="btn" data-show="pista{mis}">Mostrar la pista</button></div>'
         f'<div class="note" id="pista{mis}" hidden style="--accent:var(--m1)"><b>Pista:</b> {E(pista)}</div>')
    return dict(m=0, html=h, guia=guia(0, apoyo=[
        "No expliques la frase. Si alguien pregunta de dónde salió, di: «eso es lo que vamos a "
        "averiguar». La frase es inventada para la clase: no sale del libro.",
        f"La pista existe para el cierre de los 15 minutos, no para el principio: {pista}."]))


def esc_dinamica(mis, i, fase):
    nom, mins, pasos, entrena, material = P.DINAMICAS[mis][i]
    est = P.MISIONES[mis]["estr"][i]
    lis = "".join(f'<li>{E(p)}</li>' for p in pasos)
    h = (f'<div class="eyebrow"><span class="min" style="--accent:{EST_COL[i]}">Dinámica · {mins} min</span>'
         f'<span class="kicker">Entrena la estrategia {i+1} · {E(est)}</span></div>'
         f'<h2>{E(nom)}</h2>'
         f'<div class="grid c2 mt"><div class="card edge" style="--accent:{EST_COL[i]}">'
         f'<h3>Cómo se hace</h3><ol class="pasos">{lis}</ol></div>'
         f'<div class="card"><h3>Qué vas a necesitar</h3><p>{E(material)}</p></div></div>')
    return dict(m=fase, min=mins, html=h, guia=guia(fase, decir=[
        "«Esto no es recreo: es la misma operación que van a hacer con el texto en cinco "
        "minutos, pero con el cuerpo.»"], apoyo=[
        "Qué movimiento mental entrena: " + entrena,
        "La regla para aprobar cualquier dinámica: si no puedes decir qué paso de la estrategia "
        "está ejercitando, es recreo, no clase."]))


def esc_problematizadora(mis):
    botones = "".join(
        f'<button class="btn tally" data-tally="h{mis}{L}">{L} <span class="n" id="h{mis}{L}">0</span></button>'
        for L in "ABCD")
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m2)">Pregunta problematizadora</span>'
         f'<span class="kicker">Libro abierto en la pregunta modelo</span></div>'
         f'<h2>Abran el libro en la pregunta modelo del momento {mis}</h2>'
         f'<p class="lead">Antes de releer: ¿cuál creen que es? Levanten la mano.</p>'
         f'<div class="ctl">{botones}<button class="btn" data-reset="h{mis}">↺</button></div>'
         f'<div class="card big edge mt" style="--accent:var(--m2)"><h3>La pregunta que gobierna el área</h3>'
         f'<p class="lead">¿En qué renglón está eso que estás diciendo?</p>'
         f'<p class="sub">Nadie justifica con «yo creo» ni con «se entiende que». Toda respuesta '
         f'señala una palabra o un renglón del texto.</p></div>')
    return dict(m=1, html=h, guia=guia(1, apoyo=[
        "Cuenta las manos tocando cada letra: el número queda en pantalla y sirve para el final "
        "del momento, cuando el grupo vea cuántos cambiaron de opinión al volver al texto.",
        "La clave de la pregunta modelo está en el libro mismo, en el análisis de distractores "
        "que viene después. Revélala solo al final de los 20 minutos."]))


def esc_bloque(mis, a, b_, claves, avisos):
    d = P.MISIONES[mis]
    taller = {p: (e, i, c) for p, e, i, c in P.TALLER[mis]}
    partes, apoyo = [], []
    for n in (a, b_):
        est, ins, ctx = taller[n]
        k = d["estr"].index(est) if est in d["estr"] else 0
        s = sello(mis, n)
        sel = ""
        if s:
            sab = SABERES.get((mis, n))
            titulo_s = sab[0] if sab else s[4]
            sel = (f'<div class="sello"><b>Alto · aquí entra el profe</b>'
                   f'<span>{E(titulo_s)}</span></div>')
            if sab:
                apoyo.append(f"Pregunta {n} · {sab[0]}: {sab[1]} Para destrabar: «{sab[2]}»")
        av = ""
        for sev, que, hacer in avisos.get(n, []):
            av += (f'<div class="aviso sev-{E(sev[:4])}" hidden data-grupo="k{mis}{a}">'
                   f'<b>Ojo con esta clave:</b> {E(que)}</div>')
            apoyo.append(f"Pregunta {n} · aviso del libro ({sev}): {que} Qué haces: {hacer}")
        partes.append(
            f'<div class="card edge" style="--accent:{EST_COL[k]}">'
            f'<div class="eyebrow"><span class="membrete">Libro · pregunta {n}</span>'
            f'<span class="min" style="--accent:{EST_COL[k]}">E{k+1} · {E(est)}</span></div>'
            f'<p class="sub">{E(ctx)}</p>'
            f'<h3 style="color:{EST_COL[k]}">{E(ins)}</h3>'
            f'<p>Llena el instrumento de tu cuaderno antes de mirar las opciones.</p>{sel}'
            f'<div class="clave" hidden data-grupo="k{mis}{a}"><span class="keychip" '
            f'style="background:{EST_COL[k]}">{E(claves.get(n, "—"))}</span> es la clave del libro</div>'
            f'{av}</div>')
    ins_pantalla = (a == 1)
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m3)">Desarrollo guiado · '
         f'preguntas {a} y {b_}</span><span class="kicker">'
         f'{"En pantalla, casilla por casilla" if ins_pantalla else "En el cuaderno, cada uno el suyo"}'
         f'</span></div>'
         f'<h2>Preguntas {a} y {b_}: primero el texto, después la opción</h2>'
         f'<div class="grid c2 mt">{"".join(partes)}</div>'
         f'<div class="ctl"><button class="btn" data-showgrupo="k{mis}{a}">Revelar las claves</button></div>')
    apoyo.insert(0, f"Las claves del libro son {a}·{claves.get(a,'—')} y {b_}·{claves.get(b_,'—')}. "
                    "No las reveles hasta que todos tengan el texto marcado: el botón es para el "
                    "cierre del bloque.")
    return dict(m=2, min=7, html=h, guia=guia(2, decir=[
        "«Antes de marcar: ¿qué subrayaron? Léanme el renglón.»",
        "Si alguien se traba, pregúntale qué subrayó. Si la hoja está limpia, vuelve al texto "
        "antes que a la respuesta."], apoyo=apoyo))


def esc_reto(mis):
    nom, mins, txt = P.RETOS[mis]
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m4)">Reto en equipo · {mins} min</span>'
         f'<span class="kicker">Equipos de tres · cada uno responde en su cuaderno</span></div>'
         f'<h2>Reto del corte: {E(nom)}</h2>'
         f'<div class="card big edge mt" style="--accent:var(--m4)"><p class="lead">{E(txt)}</p></div>'
         f'<div class="note mt" style="--accent:var(--m4)"><b>La defensa:</b> tres minutos por equipo, '
         f'leyendo en voz alta el renglón que los respalda. Citar de memoria no cuenta.</div>')
    return dict(m=3, html=h, guia=guia(3, apoyo=[
        "El reto no tiene una sola respuesta correcta: gana el equipo que mejor sostiene la suya "
        "con el texto. Si dos lecturas están sostenidas, dilo: eso también es leer bien.",
        "Si un equipo entrega una sola hoja para los tres, el reto no cuenta. La discusión es "
        "compartida; el registro es individual."]))


def esc_icfes(mis, k, q, clave, txt):
    ops = "".join(
        f'<div class="op" data-op="{L}"><span class="L">{L}</span><span>{E(o)}</span></div>'
        for L, o in zip("ABCD", q["o"]))
    tit = txt.get("titulo") or "Texto de la pregunta"
    cuerpo = "".join(f"<p>{E(p)}</p>" for p in (txt.get("texto") or "").split("\n\n") if p.strip())
    if "\n" in (txt.get("texto") or "") and mis == 1 and k == 4:      # el poema, verso por verso
        cuerpo = "<p>" + "<br>".join(E(v) for v in txt["texto"].split("\n")) + "</p>"
    ident = f"icf{mis}{k}"
    h = (f'<div class="eyebrow"><span class="membrete">{E(FICFES)}</span>'
         f'<span class="min" style="--accent:var(--m5)">Evaluación individual · pregunta {k}</span></div>'
         f'<div class="grid c2 icfes mt">'
         f'<div class="texto"><h3>{E(tit)}</h3>{cuerpo or "<p class=sub>El texto va completo en el cuaderno.</p>"}</div>'
         f'<div><p class="enun">{E(q["e"])}</p><div class="ops" id="{ident}">{ops}</div>'
         f'<div class="ctl"><button class="btn" data-clave="{ident}" data-k="{E(clave)}">Revelar la clave</button></div>'
         f'</div></div>')
    notas = txt.get("notas") or []
    return dict(m=4, html=h, guia=guia(4, decir=[
        "Durante la evaluación no se proyecta nada: las preguntas están en el cuaderno. Esta "
        "diapositiva es para el cierre, cuando se socializan las falladas.",
        "«¿Qué subrayaste en el texto antes de mirar las opciones?»"],
        apoyo=[f"La clave es la {clave}."] + notas))


def esc_cierre(mis):
    d = P.MISIONES[mis]
    ests = "".join(f'<div class="step" style="--accent:{EST_COL[i]}"><div class="k">{i+1}</div>'
                   f'<div><b>{E(e)}</b></div></div>' for i, e in enumerate(d["estr"]))
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m6)">Cierre</span>'
         f'<span class="kicker">La pregunta de siempre</span></div>'
         f'<h2>¿En qué se parecía la pregunta del ICFES a la de tu libro?</h2>'
         f'<div class="grid c2 mt"><div class="grid" style="gap:10px">{ests}</div>'
         f'<div class="card big edge" style="--accent:var(--m6)"><h3>Antes de salir</h3>'
         f'<ol class="pasos"><li>La palabra nueva del día, en la franja de vocabulario, con tus '
         f'palabras.</li><li>«Lo que me llevo de esta pregunta».</li><li>Tu carita de salida.</li>'
         f'<li>La casilla {mis} de la portada del área.</li></ol></div></div>')
    return dict(m=5, html=h, guia=guia(5, apoyo=[
        "La palabra nueva no se dicta. Si quedó mal entendida, eso se ve en la hoja y se corrige "
        "la próxima clase: es mejor que dictarla bien.",
        "Para el cierre del momento: " + d["cierre"]]))


# ─────────────────────────────── las dos clases del simulacro ───────────────────────────────
def escenas_clase7():
    sc = [dict(m=None, html=(
        '<div class="logo-xl"><img src="__LOGO__" alt="EDUCATE · Para el Saber"></div>'
        '<div class="eyebrow"><span class="tag">Clase 7 de 8</span><span class="kicker">Lectura '
        'Crítica · simulacro del área</span></div><h1>Hoy nadie les va a decir si acertaron</h1>'
        '<p class="lead">Veinticuatro preguntas oficiales, seguidas, como en la prueba. Lo único '
        'que llevan es lo que entrenaron: marcar el texto antes de marcar la opción.</p>'),
        guia=dict(obj="Que el simulacro se viva en condiciones de prueba.", decir=[
            "«Pueden subrayar: en la prueba real también pueden, y es lo que entrenamos.»"],
            apoyo=["Las 24 preguntas son las de las seis franjas de entrenamiento del cuaderno. "
                   "No se proyectan: cada uno trabaja en su cuaderno."]))]
    sc.append(dict(m=None, min=90, html=(
        '<div class="eyebrow"><span class="min" style="--accent:var(--m5)">90 minutos</span>'
        '<span class="kicker">Inicia el cronómetro con T</span></div><h2>Las reglas del simulacro</h2>'
        '<div class="grid c2 mt"><div class="card edge" style="--accent:var(--m5)"><ol class="pasos">'
        '<li>En silencio y en filas individuales.</li><li>No se responde ninguna duda, ni de '
        'vocabulario.</li><li>Las dudas se escriben en el margen.</li><li>Se marca el texto, '
        'después la opción.</li></ol></div><div class="card big edge" style="--accent:var(--lc)">'
        '<p class="lead">Si la hoja está limpia, no leíste: pasaste los ojos.</p></div></div>'),
        guia=dict(obj="Medir sin acompañamiento.", decir=["No intervengas en los 90 minutos."],
                  apoyo=["Anota quién va directo a las opciones sin tocar el texto: es el dato "
                         "más útil del simulacro, más que el puntaje."])))
    tallas = "".join(
        f'<div class="card edge" style="--accent:{c}"><h3>{n}</h3><p class="sub">{d}</p>'
        f'<div class="ctl"><button class="btn tally" data-tally="c7{n[:2]}">+1 <span class="n" '
        f'id="c7{n[:2]}">0</span></button><button class="btn" data-reset="c7{n[:2]}">↺</button></div></div>'
        for n, d, c in [("CL · contenidos locales", "qué dice", "var(--m1)"),
                        ("SG · sentido global", "cómo se arma", "var(--m2)"),
                        ("RE · reflexionar y evaluar", "qué quiere y si se sostiene", "var(--m5)")])
    sc.append(dict(m=None, min=30, html=(
        '<div class="eyebrow"><span class="min" style="--accent:var(--m6)">Últimos 30 minutos</span>'
        '<span class="kicker">Conteo por competencia</span></div><h2>¿Dónde se nos fue el puntaje?</h2>'
        f'<div class="grid c3 mt">{tallas}</div><p class="sub mt">Cuenta las manos de quienes '
        'fallaron preguntas de cada competencia.</p>'),
        guia=dict(obj="Que el grupo vea en cuál de las tres competencias se le va el puntaje.",
                  decir=["«No es una nota: es un mapa de dónde hay que invertir las semanas que "
                         "quedan.»"], apoyo=["En Lectura Crítica casi siempre es RE, porque es la "
                         "única que no se responde buscando: hay que juzgar.",
                         "Anota los tres números: son el dato que la coordinación necesita para "
                         "decidir el refuerzo."])))
    return sc


def escenas_clase8(todas):
    """La devolución: el profe escoge las cinco más falladas de las 24 y se reparan."""
    lista = "".join(
        f'<button class="btn pick" data-pick="{i}">M{m}·P{k} · {E(t[:46])}</button>'
        for i, (m, k, t) in enumerate(todas))
    sc = [dict(m=None, html=(
        '<div class="logo-xl"><img src="__LOGO__" alt="EDUCATE · Para el Saber"></div>'
        '<div class="eyebrow"><span class="tag">Clase 8 de 8</span><span class="kicker">Lectura '
        'Crítica · devolución y cierre del área</span></div><h1>Lo que subrayaste esta vez</h1>'
        '<p class="lead">Hoy no hay texto nuevo. Hoy vamos a mirar tu letra de hace seis semanas '
        'al lado de la de hoy.</p>'),
        guia=dict(obj="Reparar, no repetir.", decir=["«Saquen el cuaderno abierto en el simulacro "
                  "y en la hoja de taller de la misma estrategia.»"], apoyo=[
                  "El contraste entre las dos hojas es el cierre del área. No hay que explicarlo: "
                  "hay que señalarlo."]))]
    sc.append(dict(m=None, html=(
        '<div class="eyebrow"><span class="kicker">Escoge las cinco más falladas</span></div>'
        '<h2>Las cinco preguntas que vamos a reparar</h2><div class="picks mt">' + lista + '</div>'
        '<p class="sub mt">Toca cinco. Se guardan mientras la página esté abierta.</p>'),
        guia=dict(obj="Elegir con el conteo de la clase 7, no con lo que a ti te parece interesante.",
                  decir=["Usa los tres números del conteo por competencia."], apoyo=[
                  "Si dudas entre dos, quédate con la de RE: es la que más puntaje cuesta."])))
    sc.append(dict(m=None, html=(
        '<div class="eyebrow"><span class="kicker">Una por una</span></div>'
        '<h2>¿Qué subrayaste esta vez que no subrayaste antes?</h2><div id="elegidas" class="grid c2 mt"></div>'),
        guia=dict(obj="Que cada estudiante vea su propio avance escrito.", decir=[
            "«Pongan las dos hojas una al lado de la otra. ¿Qué cambió en el subrayado?»"],
            apoyo=["Si nadie subrayó distinto, la estrategia no se instaló todavía: anótalo en el "
                   "registro para el reporte de los especialistas."])))
    ests = "".join(f'<div class="step" style="--accent:{COL[m]}"><div class="k">M{m}</div>'
                   f'<div><b>{E(" · ".join(P.MISIONES[m]["estr"]))}</b></div></div>' for m in range(1, 7))
    sc.append(dict(m=None, html=(
        '<div class="eyebrow"><span class="kicker">Cierre del área</span></div>'
        '<h2>Veinticuatro estrategias que ya son tuyas</h2>'
        f'<div class="grid" style="gap:10px;margin-top:16px">{ests}</div>'),
        guia=dict(obj="Que el estudiante nombre las estrategias que se lleva.", decir=[
            "«Si al final pueden nombrarlas y decir para qué sirve cada una, el área cumplió, "
            "aunque fallen preguntas.»"], apoyo=["Termina con la página de cierre del cuaderno y "
                                                 "la franja de vocabulario completa."])))
    return sc


def escenas_clase(mis):
    claves = claves_libro(mis)
    avisos = avisos_por_pregunta(mis)
    qs = preguntas_icfes(mis)
    banco = P.BANCO[mis]
    sc = [esc_portada(mis), esc_reglas(mis), esc_activacion(mis),
          esc_dinamica(mis, 0, 0), esc_problematizadora(mis)]
    pares = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
    for j, (a, b_) in enumerate(pares):
        sc.append(esc_bloque(mis, a, b_, claves, avisos))
        if j in (1, 2, 3):                       # cada 18 minutos, la dinámica del bloque
            sc.append(esc_dinamica(mis, j, 2))
    sc.append(esc_reto(mis))
    for k, q in enumerate(qs, 1):
        sc.append(esc_icfes(mis, k, q, banco[k - 1]["clave"], TEXTOS.get((mis, k), {})))
    sc.append(esc_cierre(mis))
    return sc


# ─────────────────────────────── la página ───────────────────────────────
def pagina(titulo, sub, escenas, nombre_mom):
    logo = "data:image/png;base64," + base64.b64encode(open(LOGO, "rb").read()).decode()
    datos = json.dumps(escenas, ensure_ascii=False).replace("__LOGO__", logo).replace("</", "<\\/")
    mom = json.dumps([dict(n=i + 1, nom=f[0], min=f[1], c=f"--m{i+1}") for i, f in enumerate(P.FASES)],
                     ensure_ascii=False)
    return (PLANTILLA.replace("__TITULO__", E(titulo)).replace("__SUB__", E(sub))
            .replace("__NOMBRE__", E(nombre_mom)).replace("__LOGOSRC__", logo)
            .replace("__ESCENAS__", datos).replace("__MOM__", mom))


PLANTILLA = r"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>__TITULO__</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700;800&family=Source+Sans+3:wght@400;600;700&display=swap">
<style>
:root{
  --display:"Archivo","Segoe UI",system-ui,sans-serif;
  --text:"Source Sans 3","Segoe UI",system-ui,sans-serif;
  --lc:#A82424; --azul:#1F4E8C; --oro:#B0711A; --morado:#5B3E96; --verde:#2E7A39;
  --m1:#A82424; --m2:#1F4E8C; --m3:#3B3BA6; --m4:#5B3E96; --m5:#B0711A; --m6:#2E7A39;
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
#tnum.over{color:var(--lc)}
.btn{appearance:none;font:inherit;font-size:.86em;font-weight:600;border:1.5px solid var(--line);background:var(--paper);color:var(--ink);border-radius:10px;padding:7px 14px;cursor:pointer}
.btn:hover{border-color:var(--faint)}
.btn.solid{background:var(--lc);border-color:var(--lc);color:#fff}
.btn[aria-pressed="true"]{background:var(--ink);border-color:var(--ink);color:#fff}
#stage{overflow:auto;padding:clamp(18px,3vw,48px) clamp(16px,4vw,72px)}
#wrap{max-width:1500px;margin:0 auto}
#wrap.enter{animation:ent .28s ease-out}
@keyframes ent{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}
#bot{display:flex;align-items:center;gap:12px;padding:10px clamp(14px,2vw,28px);background:var(--paper)}
#prog{flex:1;height:6px;border-radius:4px;background:var(--line);overflow:hidden}
#prog i{display:block;height:100%;background:var(--lc);transition:width .25s}
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
.min{background:var(--accent,var(--lc));color:#fff}
.membrete{border:1.5px solid var(--line);color:var(--muted)}
.kicker{color:var(--muted);font-size:.85em;letter-spacing:.06em;text-transform:uppercase;font-weight:700}
.grid{display:grid;gap:clamp(12px,1.4vw,22px)}
.c2{grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr))}
.c3{grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr))}
.grid>*{min-width:0}
.card{background:var(--paper);border:1px solid var(--line);border-radius:16px;padding:clamp(14px,1.6vw,24px)}
.card.edge{border-left:6px solid var(--accent,var(--lc))}
.card.big .lead{font-size:1.3em}
.step{display:flex;gap:14px;align-items:center;background:var(--paper);border:1px solid var(--line);border-left:5px solid var(--accent);border-radius:12px;padding:10px 14px}
.step .k{width:2em;height:2em;border-radius:50%;display:grid;place-items:center;background:var(--accent);color:#fff;font-family:var(--display);font-weight:800;flex:none}
.note{border-left:5px solid var(--accent,var(--lc));background:var(--paper);border-radius:10px;padding:10px 16px;margin-top:12px}
.cita{font-family:var(--display);font-weight:600;line-height:1.35;background:var(--paper);border-left:6px solid var(--lc);border-radius:12px;padding:clamp(16px,2vw,30px);margin:18px 0}
.cita.xl{font-size:clamp(24px,2.6vw,44px)}
.ctl{display:flex;flex-wrap:wrap;gap:8px;margin-top:14px}
.tally .n{display:inline-block;min-width:1.6em;margin-left:6px;padding:0 6px;border-radius:6px;background:var(--bg);font-variant-numeric:tabular-nums}
.pasos{margin:.2em 0 0;padding-left:1.3em}.pasos li{margin:.3em 0}
.sello{margin-top:12px;border:2px dashed var(--oro);border-radius:12px;padding:10px 14px;background:#FDF6EA}
.sello b{display:block;color:var(--oro);font-size:.8em;letter-spacing:.06em;text-transform:uppercase}
.clave{margin-top:12px;display:flex;align-items:center;gap:10px;font-weight:600}
.keychip{display:inline-grid;place-items:center;width:2.2em;height:2.2em;border-radius:10px;color:#fff;font-family:var(--display);font-weight:800;font-size:1.2em}
.aviso{margin-top:10px;border-radius:10px;padding:10px 14px;background:#FBEFEF;border-left:5px solid var(--lc);font-size:.92em}
.aviso.sev-aten{background:#EDF5EE;border-left-color:var(--verde)}
.aviso.sev-medi{background:#FDF5E7;border-left-color:var(--oro)}
.icfes .texto{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:clamp(14px,1.6vw,24px);max-height:62vh;overflow:auto;font-size:.95em}
.enun{font-weight:600;font-size:1.08em}
.ops{display:grid;gap:8px;margin-top:10px}
.op{display:flex;gap:12px;align-items:flex-start;background:var(--paper);border:1.5px solid var(--line);border-radius:12px;padding:10px 14px}
.op .L{flex:none;width:1.8em;height:1.8em;border-radius:8px;display:grid;place-items:center;background:var(--bg);font-family:var(--display);font-weight:800}
.op.ok{border-color:var(--verde);background:#EDF5EE}.op.ok .L{background:var(--verde);color:#fff}
.picks{display:flex;flex-wrap:wrap;gap:8px}
.pick[aria-pressed="true"]{background:var(--lc);border-color:var(--lc);color:#fff}
#scrim{position:fixed;inset:0;background:rgba(15,18,24,.35);opacity:0;pointer-events:none;transition:opacity .2s}
#scrim.on{opacity:1;pointer-events:auto}
#guia{position:fixed;top:0;right:0;height:100%;width:min(520px,92vw);background:var(--paper);box-shadow:-12px 0 40px rgba(0,0,0,.18);transform:translateX(102%);transition:transform .25s;display:flex;flex-direction:column;z-index:10}
#guia.open{transform:none}
#guiahead{display:flex;align-items:center;gap:12px;padding:14px 18px;background:var(--bg)}
#guiabody{overflow:auto;padding:16px 20px 30px;font-size:.92em}
.gbox{border:1px solid var(--line);border-radius:12px;padding:12px 14px;margin-bottom:12px}
.gbox h4{margin:0 0 6px;font-family:var(--display);font-size:.8em;letter-spacing:.07em;text-transform:uppercase;color:var(--lc)}
.gbox ul{margin:0;padding-left:1.1em}.gbox li{margin:.35em 0}
.gbox.como{background:#F6F7F9}.gbox.como h4{color:var(--muted)}
.gbox.apoyo{background:#FDF6EA;border-color:#EAD9B4}.gbox.apoyo h4{color:var(--oro)}
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
function guiaHTML(g){
  if(!g) return '<p class="sub">Sin notas para esta diapositiva.</p>';
  var h = '<div class="gbox"><h4>Objetivo</h4><p>'+esc(g.obj)+'</p></div>';
  if(g.decir && g.decir.length) h += '<div class="gbox"><h4>Qué haces y qué dices</h4><ul>'+
     g.decir.map(function(d){ return '<li>'+esc(d)+'</li>'; }).join("")+'</ul></div>';
  if(g.como) h += '<div class="gbox como"><h4>Lo que no haces</h4><p>'+esc(g.como)+'</p></div>';
  if(g.apoyo && g.apoyo.length) h += '<div class="gbox apoyo"><h4>Si la lectura crítica no es tu fuerte</h4><ul>'+
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
}
wrap.addEventListener("click", function(e){
  var b = e.target.closest("button"); if(!b) return;
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
  var t = e.target.tagName; if(t==="INPUT"||t==="TEXTAREA") return;
  if(e.key==="ArrowRight"||e.key==="PageDown"||e.key===" "){ go(i+1); e.preventDefault(); }
  else if(e.key==="ArrowLeft"||e.key==="PageUp"){ go(i-1); e.preventDefault(); }
  else if(e.key==="Home"){ go(0); e.preventDefault(); }
  else if(e.key==="End"){ go(SC.length-1); e.preventDefault(); }
  else if(e.key==="g"||e.key==="G"){ setGuia(!$("#guia").classList.contains("open")); }
  else if(e.key==="t"||e.key==="T"){ toggleTimer(); }
  else if(e.key==="Escape"){ setGuia(false); }
});
go(0);
})();
</script>
</body>
</html>
"""


def main():
    os.makedirs(OUT, exist_ok=True)
    hechos = []
    for mis in range(1, 7):
        d = P.MISIONES[mis]
        sc = escenas_clase(mis)
        f = f"{OUT}LC_Clase{mis}_Mision{mis}.html"
        open(f, "w", encoding="utf-8").write(
            pagina(f"Lectura Crítica · Clase {mis}", f"Momento {mis} · {d['comp']} · páginas {d['pags']}",
                   sc, f"Lectura Crítica · Clase {mis}"))
        hechos.append((f, len(sc)))
    todas = []
    for m in range(1, 7):
        for k, fila in enumerate(P.BANCO[m], 1):
            todas.append((m, k, fila["contexto"]))
    f7 = f"{OUT}LC_Clase7_Simulacro.html"
    open(f7, "w", encoding="utf-8").write(pagina("Lectura Crítica · Clase 7",
         "Simulacro del área · 24 preguntas", escenas_clase7(), "Lectura Crítica · Clase 7"))
    hechos.append((f7, len(escenas_clase7())))
    f8 = f"{OUT}LC_Clase8_Devolucion.html"
    open(f8, "w", encoding="utf-8").write(pagina("Lectura Crítica · Clase 8",
         "Devolución y cierre del área", escenas_clase8(todas), "Lectura Crítica · Clase 8"))
    hechos.append((f8, len(escenas_clase8(todas))))
    for f, n in hechos:
        print(f"{os.path.basename(f):34s} {n:2d} diapositivas · {os.path.getsize(f)//1024} KB")


if __name__ == "__main__":
    main()
