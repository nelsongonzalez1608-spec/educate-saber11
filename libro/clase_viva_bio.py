#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUÍAS DE CLASE PROYECTABLES («clase viva») · BIOLOGÍA · las 8 del área.

    python3 clase_viva_bio.py [carpeta]      (por defecto entregables/guias_biologia/)

Usa el motor clase_viva.py sin cambiarlo, igual que clase_viva_soc.py (el modelo que se copia aquí).
Lo que entra de Biología:

  · plan_bio.py: FASES, MISIONES, TALLER, DINAMICAS, RETOS, SELLOS, SABERES, ACTIVACION,
    PROBLEMATIZADORA, PREGUNTA_AREA, NO_ES_TU_FUERTE, COLS_MIS, COMP_ICFES, BANCO, CLAVES y AVISOS.
  · textos_bio.py: las 24 preguntas de entrenamiento de TEXTOS_BIO.md (texto completo, enunciado,
    opciones, clave verificada, por qué, notas) y sus figuras redibujadas (FIGURAS).
  · lo escrito aquí: TITULOS, LEADS, la redacción de pantalla (UI) y qué aviso del libro se proyecta
    al revelar (PROYECTAR). Lo demás de AVISOS va solo a la guía del profe.

Lo que hace este módulo además de llenar el Area:

  1. Un Area por misión: cada estrategia se pinta con el color de su chip en el cuaderno (COLS_MIS).
     Los momentos: m1 = verde hoja del área (#30843C, activación), m2 azul, m3 índigo, m4 morado,
     m5 rojo (la evaluación) y m6 pizarra (#4A5A70): el cierre no va en verde para no confundirse
     con el área ni con la opción correcta revelada.
  2. Membrete «Pregunta Saber 11» (Nelson, 10 nov): se fija en CV.FICFES antes de escribir, sin
     tocar clase_viva.py. En pantalla nunca dice «oficial» ni «reales»; `revisar_pantalla()` falla
     si aparece.
  3. Las figuras de las preguntas (tablas, esquemas, las cuatro gráficas de opciones) van en el panel
     del texto, en SVG o tabla en línea: el archivo sigue siendo único y funciona sin internet.
  4. La guía del profe de cada pregunta de entrenamiento trae por qué es la clave y por qué cae cada
     opción; si la pregunta viene del compilado ASED, dice «Fuente: compilado ASED (no es del ICFES)»
     (en Biología ninguna: las 24 son de los cuadernillos 2016-1).
  5. `[hidden]{display:none!important}`, como en Sociales: sin esa regla la clave del libro se ve
     antes de revelarla.

Comprueba antes de escribir: plan_bio.verificar() (claves del libro y del entrenamiento contra los
docstrings de bioN.py y bioN_icfes.py) y textos_bio.verificar() (el .md contra módulos e icfes.csv).
"""
import copy, os, re, sys, types

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import clase_viva as CV
import plan_bio as P
import textos_bio

CV.FICFES = "Pregunta Saber 11"          # decisión de Nelson, 10 nov: sin año ni «oficial»

OUT = os.path.join(AQUI, "..", "entregables", "guias_biologia")
CSS_EXTRA = ("[hidden]{display:none!important}\n" + textos_bio.CSS +
             ".aviso{border-left-color:var(--rojo)}"
             ".aviso.sev-baja{background:#EEF3FA;border-left-color:var(--azul)}\n")

# ─────────────────────────────── títulos de cada clase ───────────────────────────────
TITULOS = {
    1: "La célula trabaja en cadena",
    2: "Un cuerpo que vuelve al equilibrio",
    3: "En el ecosistema nada cambia solo",
    4: "Cada invento, una oportunidad y un riesgo",
    5: "Lo que se hereda y lo que se edita",
    6: "La vida cambia con dos relojes",
}
LEADS = {
    1: "Hoy la célula es una fábrica: cada organelo tiene un oficio y la proteína recorre sus "
       "estaciones en orden. Si una falla, todo lo de después se detiene. Y un efecto solo se afirma "
       "comparando contra lo que no cambió.",
    2: "Tu cuerpo regula su agua, su azúcar y su calcio sin pedirte permiso. Hoy seguimos esos "
       "circuitos: qué se desvía, quién lo detecta, qué orden se da y qué lo corrige.",
    3: "Un lago, una sabana, un cultivo: si cambia una pieza, otras lo sienten. Hoy leemos los datos "
       "contra el control, seguimos la red y buscamos el factor que limita.",
    4: "Una prótesis de memoria, una vacuna diseñada con inteligencia artificial, un envase que avisa "
       "cuando la comida se daña. Hoy no basta con que suene bien: ¿se puede poner a prueba?",
    5: "Dos papás sanos pueden tener un hijo con una enfermedad hereditaria, y nadie hizo trampa. Hoy "
       "seguimos el alelo por la familia y miramos qué gana y qué arriesga editar el ADN.",
    6: "La última clase de contenido del área. Un perro cambia en su vida; una raza cambia en "
       "generaciones. Hoy separamos los dos relojes y juntamos todo lo que trabajamos.",
}

# ─────────────── la redacción de pantalla y de la guía, para Biología ───────────────
COMPETENCIAS = [("UC · uso comprensivo del conocimiento científico", "conceptos y modelos de la biología",
                 "var(--m2)"),
                ("EF · explicación de fenómenos", "por qué pasa, eslabón por eslabón", "var(--m4)"),
                ("IN · indagación", "preguntas, controles y conclusiones", "var(--m6)")]

UI = dict(
    portada_decir=["«Libro abierto, cuaderno cerrado, lápiz. Hoy no les voy a preguntar qué saben de "
                   "memoria: les voy a preguntar qué dato lo dice.»"],
    regla_lead="Si el instrumento está vacío, no lo resolviste: lo adivinaste.",
    regla_p=("Primero se escribe el instrumento —qué cambió, qué se midió, contra qué se compara—, "
             "después se marca la opción. Una respuesta correcta con el instrumento en blanco no cuenta "
             "como resuelta."),
    regla_decir=["«La respuesta correcta con el instrumento vacío no cuenta. ¿Por qué? Porque en "
                 "Biología casi todas las opciones suenan científicas: el que no escribió el dato escoge "
                 "la que suena mejor, no la que dice el texto o la gráfica.»"],
    regla_apoyo=["Si alguien pregunta para qué escribir, la respuesta corta es: lo que separa la opción "
                 "correcta de las que suenan bien está en un número, una flecha o una palabra del texto, "
                 "y eso se pierde si no se escribe.",
                 "Si alguien dice «eso es por las hormonas» o «eso es genético», devuélvele la pregunta: "
                 "«¿qué dato te lo dice?»."],
    act_h2="¿Qué cambió, qué se midió y contra qué se compara?",
    act_lead="Tres respuestas antes de cualquier explicación. Todavía no se abre el cuaderno.",
    act_apoyo=("No expliques el fenómeno ni aceptes todavía explicaciones: primero las tres respuestas. "
               "La observación es inventada para la clase: no sale del libro."),
    dina_decir=["«Esto no es recreo: es la misma operación que van a hacer con el texto o la gráfica en "
                "cinco minutos —seguir, comparar o ubicar—, pero con el cuerpo.»"],
    prob_lead="Antes de releer el texto o la gráfica: ¿cuál creen que es? Levanten la mano.",
    prob_lead2=P.PREGUNTA_AREA,
    bloque_h2="Preguntas {a} y {b}: primero el instrumento, después la opción",
    bloque_decir=["«Antes de marcar: ¿qué dato escribieron en el instrumento? Léanmelo.»",
                  "Si alguien se traba, pregúntale qué cambió y contra qué lo compara. Si el instrumento "
                  "está vacío, vuelve al texto o a la gráfica antes que a las opciones."],
    bloque_apoyo=("Las claves del libro son {a}·{ka} y {b}·{kb}. No las reveles hasta que todos tengan "
                  "el instrumento escrito: el botón es para el cierre del bloque."),
    reto_defensa=("<b>La defensa:</b> tres minutos por equipo, señalando el dato, el grupo de comparación "
                  "o el eslabón que los respalda. «Es que así funciona» no cuenta."),
    reto_apoyo=["El reto no tiene una sola respuesta correcta: gana el equipo que mejor sostiene la suya "
                "con datos. Si dos explicaciones están sostenidas, dilo: eso también es hacer ciencia.",
                "Si un equipo entrega una sola hoja para los tres, el reto no cuenta. La discusión es "
                "compartida; el registro es individual.",
                "Cierra mostrando qué variable o qué eslabón quedó por fuera en cada propuesta."],
    icfes_decir=["Durante la evaluación no se proyecta nada: las preguntas están en el cuaderno. Esta "
                 "diapositiva es para el cierre, cuando se socializan las falladas.",
                 "«¿Qué escribiste en el instrumento antes de mirar las opciones? ¿Qué dato lo decide?»"],
    c7_h1="Hoy nadie les va a decir si acertaron",
    c7_lead=("Veinticuatro preguntas tipo Saber 11, seguidas, como en la prueba. Lo único que llevan es "
             "lo que entrenaron: escribir el dato y su comparación antes de mirar las opciones."),
    c7_decir=["«Pueden escribir al margen: en la prueba real también pueden rayar el cuadernillo, y es "
              "lo que entrenamos.»"],
    c7_reglas=["En silencio y en filas individuales.", "No se responde ninguna duda, ni de vocabulario.",
               "Las dudas se escriben en el margen.",
               "Primero el dato y su comparación, después la opción."],
    c7_apoyo_reglas=["Anota quién va directo a las opciones sin escribir nada: es el dato más útil del "
                     "simulacro, más que el puntaje."],
    c7_competencias=COMPETENCIAS,
    c8_h1="Lo que escribiste esta vez",
    c8_lead=("Hoy no hay pregunta nueva. Hoy vamos a poner tu instrumento de hace seis semanas al lado "
             "del de hoy."),
    c8_apoyo_elegir=["Si dudas entre dos, quédate con la de la competencia que más manos tuvo en el "
                     "conteo de la clase 7."],
    c8_h2="¿Qué dato o qué comparación viste esta vez que antes no?",
    c8_decir=["«Pongan las dos hojas una al lado de la otra. ¿Qué escribieron distinto en el "
              "instrumento?»"],
    c8_apoyo=["Si nadie escribió distinto, la estrategia no se instaló todavía: anótalo en el registro "
              "para el reporte de los especialistas."],
)

# ───────────── los avisos del libro que salen en pantalla (al revelar las claves) ─────────────
# Clave: (misión, rótulo del aviso en plan_bio.AVISOS). Valor: (rótulo que usa el motor, severidad,
# texto para el estudiante). Lo que no está aquí va solo a la guía del profe: reparto de claves,
# patrones de opciones, fuentes sin verificar y figuras que delatan la clave no se proyectan.
PROYECTAR = {
    (1, "preg. 9"): ("preg. 9", "media",
        "El texto se contradice: primero dice que la línea B no expresa genes de proteínas de secreción "
        "y después que la diferencia no se debe a la capacidad de síntesis. La clave A se sostiene con la "
        "conclusión de los investigadores: si dudaste, leíste bien."),
    (1, "preg. 5"): ("preg. 5", "atención",
        "Reducir no es detener: la gráfica muestra cero en los tres grupos tratados, no una barra más baja."),
    (2, "preg. 2"): ("preg. 2", "media",
        "Ninguna opción explica a las dos personas a la vez. La A es la única fisiológicamente cierta: por "
        "eso es la clave, aunque no explique la diferencia."),
    (2, "preg. 10"): ("preg. 10", "media",
        "Errata del libro: liberar insulina cuando la glucosa sube evita las hiperglucemias, no las "
        "«hipoglucemias». La clave no cambia."),
    (2, "preg. 5"): ("preg. 5", "atención",
        "«Primero» y «gradualmente» no se contradicen: algo puede empezar primero y tardar en terminar."),
    (3, "preg. 1 · opción B"): ("preg. 1", "atención",
        "La opción B dice que descomponer más «disminuye la producción primaria». Es falso: descomponer "
        "libera nutrientes para las plantas."),
    (3, "preg. 8 y 9"): ("preg. 8", "baja",
        "En Colombia el decimal se escribe con coma: 2,8 millones, no «2.8 millones»."),
    (4, "preg. 7"): ("preg. 7", "media",
        "El texto separa dos piezas: las nanopartículas frenan bacterias y los sensores de pH detectan el "
        "deterioro. El cambio de color es de los sensores; la clave A se lo atribuye a las nanopartículas. "
        "Es la mejor de las cuatro, no una perfecta."),
    (4, "preg. 9"): ("preg. 9", "media",
        "El texto adapta la vacuna al tumor de cada paciente; la menor toxicidad es un resultado, no el "
        "objetivo. La A es la única que no contradice el texto: es la menos mala."),
    (5, "preg. 6"): ("preg. 6", "media",
        "La pregunta cita «la nueva información sobre la consanguinidad», pero ese texto no está en el "
        "libro. Se responde con lo general: entre parientes aumentan los hijos con dos copias iguales."),
    (5, "preg. 1"): ("preg. 1", "atención",
        "La opción D trae un dato falso: una portadora transmite una enfermedad ligada al X, en promedio, "
        "a la mitad de sus hijos varones, no a todos."),
    (5, "preg. 8 a 10"): ("preg. 9", "media",
        "Mezclar dos razas distintas no es lo que enferma: el problema aparece cuando se cruzan parientes. "
        "El texto del libro junta las dos cosas."),
    (6, "preg. 10"): ("preg. 10", "alta",
        "Dos opciones se pueden defender: la B también es consistente con la tabla. La clave D es la que "
        "usa la comparación de los tres páramos que pide el enunciado. Si marcaste B con argumentos, "
        "leíste bien."),
    (6, "preg. 2"): ("preg. 2", "media",
        "En la tabla el autocontrol fue alto en los dos grupos: no cambió. La clave A dice que sí; es la "
        "menos mala de las cuatro."),
}

FRANJA = ("El concepto del día —un proceso, una estructura o una relación—, en «Palabras que me "
          "frenaron», con tus palabras.")

# Temas que piden cuidado en clase (portada de la guía del profe).
CUIDADO = {
    2: "La primera pregunta del entrenamiento trata del ciclo menstrual y de las pastillas "
       "anticonceptivas. Es biología: vocabulario correcto, sin bromas y sin pedir casos personales.",
    5: "La clase habla de enfermedades hereditarias en las familias y del albinismo (la activación). Si "
       "un estudiante cuenta algo de su familia, se le agradece y no se discute en público.",
    6: "La primera pregunta del entrenamiento trata del ciclo menstrual. Vocabulario correcto, sin "
       "bromas y sin casos personales.",
}

# Nombres de la política colombiana que no pueden salir (regla del proyecto). Biología no trae
# ninguno; la revisión se deja por si alguien agrega un caso.
PROHIBIDOS = ["Petro", "Uribe", "Duque", "Santos", "Benedetti", "Pastrana", "Gaviria", "Samper",
              "Cepeda", "Vargas Lleras", "Fajardo", "Claudia López"]
# Lo que no puede decir la pantalla (membrete de Nelson, 10 nov).
NO_EN_PANTALLA = ["oficial", "reales del ICFES", "real del ICFES", "Pregunta real"]


# ─────────────────────────────── datos ───────────────────────────────
def paginas(mis):
    b = P.BASE[mis]
    return [b, b + 1, b + 3, b + 4, b + 5], [b + 2, b + 6]


def clasifica_avisos():
    """Reparte plan_bio.AVISOS en: los que se proyectan (motor), los que van a la guía en su
    pregunta del taller, los de una pregunta de entrenamiento y los generales de la misión."""
    proy, taller, icfes, general = {}, {}, {}, {}
    for mis, lista in P.AVISOS.items():
        proy[mis] = []
        for preg, sev, que, hacer in lista:
            if (mis, preg) in PROYECTAR:
                rot, sev2, txt = PROYECTAR[(mis, preg)]
                proy[mis].append((rot, sev2, txt, hacer))
                # el aviso completo, con lo que hace el profe, también va a la guía
            nums = [int(x) for x in re.findall(r"\d+", preg)]
            if " a " in preg and len(nums) == 2:
                nums = list(range(nums[0], nums[1] + 1))
            if preg.startswith("ICFES") and nums:
                for k in nums:
                    icfes.setdefault((mis, k), []).append(
                        f"Aviso ({sev}), solo para ti: {que} Qué haces: {hacer}")
            elif preg.startswith("preg") and nums:
                if (mis, preg) in PROYECTAR:
                    continue                     # el motor ya lo pone en el apoyo del bloque
                for n in nums:
                    taller.setdefault((mis, n), []).append(dict(
                        titulo=f"aviso del libro ({sev}), solo para ti, no se proyecta",
                        texto=f"{que} Qué haces: {hacer}"))
            else:
                general.setdefault(mis, []).append(f"{que} {hacer}")
    return proy, taller, icfes, general


def notas_taller(avisos_taller):
    """Una nota por pregunta, sin repetir la misma en las dos preguntas de un bloque."""
    out = {}
    for (mis, n), notas in sorted(avisos_taller.items()):
        par = n - 1 if n % 2 == 0 else n + 1
        ya = {x["titulo"] + x["texto"] for x in out.get((mis, par), [])}
        out[(mis, n)] = [x for x in notas if x["titulo"] + x["texto"] not in ya]
    return out


def textos_icfes(icfes, avisos_icfes):
    """Lo que el motor lee de cada pregunta de entrenamiento, con las notas del profe completas."""
    out = {}
    for (mis, k), v in icfes.items():
        v = copy.deepcopy(v)
        notas = [f"Por qué es la {v['clave']}: {v['verificacion']}"] if v.get("verificacion") else []
        sab = P.SABERES.get((mis, f"I{k}"))
        if sab:
            notas.append(f"Sello del cuaderno · {sab[0]}: {sab[1]} Para destrabar: «{sab[2]}»")
        notas += v["notas"] + avisos_icfes.get((mis, k), [])
        fuente = P.BANCO[mis][k - 1].get("fuente", "")
        if "ASED" in fuente or "ASED" in v.get("fuente", ""):
            notas.insert(0, "⚑ Fuente: compilado ASED (no es del ICFES). Nelson decide si se reemplaza; "
                            "mientras tanto, no la presentes como «del ICFES».")
        v["notas"] = notas
        out[(mis, k)] = v
    return out


def verificar_claves(icfes):
    malas = P.verificar() + textos_bio.verificar(icfes)
    for mis in range(1, 7):
        for k in range(1, 5):
            if P.BANCO[mis][k - 1]["clave"].strip() != icfes[(mis, k)]["clave"]:
                malas.append(f"M{mis} P{k}: BANCO {P.BANCO[mis][k-1]['clave']} · .md {icfes[(mis, k)]['clave']}")
    if malas:
        raise SystemExit("Las claves no coinciden:\n  " + "\n  ".join(malas))


# ─────────────────────────────── el Area de cada misión ───────────────────────────────
def planeador(avisos_proy):
    ns = types.SimpleNamespace(**{k: getattr(P, k) for k in dir(P) if k.isupper()})
    ns.AVISOS = avisos_proy
    ns.SELLOS = [s for s in P.SELLOS if isinstance(s[3], int)]     # el del entrenamiento va en su nota
    return ns


def ui(mis):
    l0, l1 = P.LIBRO[mis]
    u = dict(UI)
    u["portada_libro"] = f"Las diez preguntas de la prueba de campo, páginas {l0} a {l1}"
    u["prob_sub"] = ("Nadie justifica con «yo sé que» ni con lo que vio en internet: toda respuesta señala "
                     "un renglón del texto, un número de la tabla o un punto de la gráfica.")
    t_pags, _ = paginas(mis)
    u["prob_apoyo"] = [
        f"La pregunta modelo es la 1 del libro (página {P.PAG_LIBRO[mis][0]}). El cuaderno se abre en la "
        f"página {t_pags[0]} solo en «mi primera idea».",
        "Cuenta las manos tocando cada letra: el número queda en pantalla y sirve para el final del "
        "momento, cuando el grupo vea cuántos cambiaron de opinión al volver al texto o a la gráfica.",
        "No digas la clave en este momento: sale en el bloque de las preguntas 1 y 2, después de llenar el "
        "instrumento en pantalla, casilla por casilla. Ahí se trabaja por qué cae cada una de las otras tres."]
    return u


def area(mis, P_ns, textos, taller):
    return CV.Area(
        nombre="Biología", prefijo="BIO", fuerte="Si Biología no es tu fuerte",
        color=CV.color_de("Biología"), P=P_ns,
        claves_libro=lambda m: P.CLAVES[m],
        preguntas_icfes=CV.preguntas_de_textos(textos),
        textos=textos, advertencias={}, taller=taller, saberes=P.SABERES,
        activacion=P.ACTIVACION, titulos=TITULOS, leads=LEADS,
        est_col=list(P.COLS_MIS[mis]),
        colores=dict(m2="#1F4E8C", m3="#3B3BA6", m4=P.MORADO, m5=P.ROJO, m6=P.PIZARRA, rojo=P.ROJO),
        textos_ui=ui(mis), apoyo_fuerte="Biología no es tu área", out=OUT)


# ─────────────────────────── lo que se agrega a las escenas ───────────────────────────
def apoyo_portada(mis, general):
    d = P.MISIONES[mis]
    out = ["⚑ Antes del sábado: " + P.limpia(d["ojo"])]
    if mis in CUIDADO:
        out.append("Con cuidado: " + CUIDADO[mis])
    for g in general.get(mis, []):
        out.append("Del libro, para ti: " + g)
    out.append("Los cuatro conceptos que tienes que poder explicar hoy en dos minutos, sin jerga. Si un "
               "estudiante sabe más que tú de un tema, déjalo explicar y pide que señale en el texto o en "
               "la gráfica de dónde lo saca:")
    out += [f"{t}: {x}" for t, x in P.NO_ES_TU_FUERTE[mis]]
    return out


def con_figura(sc, mis, k):
    """Pone la figura de la pregunta (tabla, esquema o las cuatro gráficas) en el panel del texto."""
    fig = textos_bio.FIGURAS.get((mis, k))
    marca = f"<p>{CV.E(textos_bio.MARCA)}</p>"
    if fig:
        assert marca in sc["html"], f"M{mis} P{k}: falta la marca de la figura"
        if (mis, k) in textos_bio.EN_OPCIONES:
            ops = f'<div class="ops" id="icf{mis}{k}">'
            assert ops in sc["html"]
            sc["html"] = sc["html"].replace(marca, "").replace(
                ops, f'<div class="opsfig">{fig}</div><div class="ops cuatro" id="icf{mis}{k}">')
        else:
            sc["html"] = sc["html"].replace(marca, fig)
    return sc


def escenas_contenido(A, mis, general):
    sc = CV.escenas_clase(A, mis)
    assert len(sc) == 19, f"clase {mis}: {len(sc)} diapositivas"
    sc[0]["guia"]["apoyo"] = apoyo_portada(mis, general) + sc[0]["guia"]["apoyo"]
    l0 = P.PAG_LIBRO[mis][0]
    h = sc[4]["html"].replace(f"Abran el libro en la pregunta modelo del momento {mis}",
                              f"Abran el libro en la pregunta 1, página {l0}")
    sc[4]["html"] = h + (f'<div class="card big edge mt" style="--accent:var(--m2)"><h3>La pregunta '
                         f'de este momento</h3><p class="lead">{CV.E(P.PROBLEMATIZADORA[mis])}</p></div>')
    # el párrafo de la dinámica «Párate si dice para qué» (Misión 2, E2) va completo en la guía
    for s in sc:
        if "Párate si dice para qué" in s["html"]:
            s["guia"]["apoyo"].insert(0, "El párrafo para leer en voz alta: «" + P.PEZ_PULMONADO + "» "
                                      "Las funciones que el grupo debe encontrar: el capullo, para no "
                                      "perder agua; el latido lento, para gastar poca energía.")
    # las cuatro preguntas de entrenamiento: diapositivas 15 a 18
    for k in range(1, 5):
        con_figura(sc[13 + k], mis, k)
    viejo = "La palabra nueva del día, en la franja de vocabulario, con tus palabras."
    assert viejo in sc[-1]["html"]
    sc[-1]["html"] = sc[-1]["html"].replace(viejo, FRANJA).replace(
        "¿En qué se parecía la pregunta del ICFES a la de tu libro?",
        "¿En qué se parecía la pregunta tipo Saber 11 a la de tu libro?")
    return sc


def rotulo(contexto, n=46):
    partes = contexto.split(" · ")
    t = partes[0]
    if len(partes) > 1 and len(t) + 3 + len(partes[1]) <= n:
        t += " · " + partes[1]
    if len(t) > n:
        t = t[:n - 1].rsplit(" ", 1)[0].rstrip(" ,(") + "…"
    return t


def escenas_simulacro(A, textos):
    sc7 = CV.escenas_clase7(A)
    sc7[0]["guia"]["apoyo"].append(
        "Ninguna de las 24 sale del compilado ASED. En pantalla y en el cuaderno van con el membrete "
        "«Pregunta Saber 11»; la procedencia de cada una está en el tablero del proyecto.")
    por = {"UC": [], "EF": [], "IN": []}
    for m in range(1, 7):
        for k in range(1, 5):
            por[P.comp_icfes(m, k)].append(f"M{m}·P{k}")
    sc7[2]["guia"]["apoyo"] = [
        "La competencia de cada pregunta es la que le pone el cuaderno en su hoja de entrenamiento: es la "
        "clasificación de EDUCATE, sirve para decidir el refuerzo.",
        *[f"{n} ({len(por[n[:2]])} preguntas): {', '.join(por[n[:2]])}." for n, _, _ in COMPETENCIAS],
        "Como no hay el mismo número de preguntas en cada competencia, compara proporciones, no manos sueltas.",
        "En la prueba real Biología, Química y Física dan un solo puntaje de Ciencias Naturales.",
        "Anota los tres números: son el dato que la coordinación necesita para decidir el refuerzo."]
    # el rótulo de cada botón es el título de la pregunta en TEXTOS_BIO.md: corto y sin repetirse
    todas = [(m, k, rotulo(textos[(m, k)]["titulo"])) for m in range(1, 7) for k in range(1, 5)]
    sc8 = CV.escenas_clase8(A, todas)
    sc8[-1]["guia"]["apoyo"] = [a.replace("la franja de vocabulario completa",
                                          "la franja «Palabras que me frenaron» completa")
                                for a in sc8[-1]["guia"]["apoyo"]]
    return sc7, sc8


# ─────────────────────────────── escribir ───────────────────────────────
def revisar_pantalla(html, archivo):
    hay = [n for n in PROHIBIDOS if re.search(r"\b" + re.escape(n) + r"\b", html)]
    if hay:
        raise SystemExit(f"{archivo}: trae nombres que no pueden salir: {hay}")
    malo = [t for t in NO_EN_PANTALLA if re.search(r"\b" + re.escape(t) + r"(es)?\b", html, re.I)]
    if malo:
        raise SystemExit(f"{archivo}: dice {malo}; el membrete es «Pregunta Saber 11»")


def escribir(A, archivo, titulo, sub, sc):
    html = CV.pagina(A, titulo, sub, sc, titulo).replace("</style>", CSS_EXTRA + "</style>", 1)
    revisar_pantalla(html, archivo)
    f = os.path.join(A.out, archivo)
    with open(f, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"{archivo:34s} {len(sc):2d} diapositivas · {os.path.getsize(f)//1024} KB")
    return f, len(sc)


def construir(out=OUT):
    global OUT
    OUT = out
    os.makedirs(out, exist_ok=True)
    icfes = textos_bio.leer()
    verificar_claves(icfes)
    proy, av_taller, av_icfes, general = clasifica_avisos()
    textos = textos_icfes(icfes, av_icfes)
    taller = notas_taller(av_taller)
    P_ns = planeador(proy)
    hechos = []
    for mis in range(1, 7):
        A = area(mis, P_ns, textos, taller)
        A.out = out
        d = P.MISIONES[mis]
        sc = escenas_contenido(A, mis, general)
        hechos.append(escribir(A, f"BIO_Clase{mis}_Mision{mis}.html", f"Biología · Clase {mis}",
                               f"Momento {mis} · {d['comp']} · páginas {d['pags']}", sc))
    A = area(1, P_ns, textos, taller)
    A.out = out
    sc7, sc8 = escenas_simulacro(A, textos)
    hechos.append(escribir(A, "BIO_Clase7_Simulacro.html", "Biología · Clase 7",
                           "Simulacro del área · 24 preguntas", sc7))
    hechos.append(escribir(A, "BIO_Clase8_Devolucion.html", "Biología · Clase 8",
                           "Devolución y cierre del área", sc8))
    return hechos


if __name__ == "__main__":
    construir(sys.argv[1] if len(sys.argv) > 1 else OUT)
