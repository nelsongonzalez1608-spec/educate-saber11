#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUÍAS DE CLASE PROYECTABLES («clase viva») · QUÍMICA · las 8 del área.

    python3 clase_viva_qui.py [carpeta]      (por defecto entregables/guias_quimica/)

Usa el motor clase_viva.py sin cambiarlo, igual que clase_viva_bio.py (el modelo que se copia aquí).
Lo que entra de Química:

  · plan_qui.py: FASES, MISIONES, TALLER, DINAMICAS, RETOS, SELLOS, SABERES, ACTIVACION,
    PROBLEMATIZADORA, PREGUNTA_AREA, NO_ES_TU_FUERTE, COLS_MIS, COMP_ICFES, BANCO, CLAVES y AVISOS.
  · textos_qui.py: las 24 preguntas de entrenamiento de TEXTOS_QUI.md (texto completo, enunciado,
    opciones, clave verificada, por qué, notas) y sus figuras redibujadas: FIGURAS (en el panel del
    texto) y FIG_OPCIONES (las gráficas o figuras que son las opciones).
  · lo escrito aquí: TITULOS, LEADS, la redacción de pantalla (UI), qué aviso del libro se proyecta
    al revelar (PROYECTAR) y la nota de seguridad de cada clase (CUIDADO). Lo demás de AVISOS va solo
    a la guía del profe.

Lo que hace este módulo además de llenar el Area:

  1. Un Area por misión: cada estrategia se pinta con el color de su chip en el cuaderno (COLS_MIS:
     azul, rojo, oro y morado, ninguno verde). Los momentos: m1 = verde esmeralda del área (#0F7A68,
     activación), m2 azul, m3 índigo, m4 morado, m5 rojo (la evaluación) y m6 pizarra (#4A5A70): el
     cierre no va en verde para no confundirse con el área ni con la opción correcta revelada (verde
     hoja #2E7A39, del motor).
  2. Membrete «Pregunta Saber 11» (Nelson, 10 nov): se fija en CV.FICFES antes de escribir, sin
     tocar clase_viva.py. En pantalla nunca dice «oficial» ni «reales»; `revisar_pantalla()` falla
     si aparece.
  3. Las figuras de las preguntas van en el panel del texto, en SVG o tabla en línea; cuando las
     opciones son gráficas, van encima de las cuatro letras. El archivo sigue siendo único y funciona
     sin internet.
  4. La guía del profe de cada pregunta de entrenamiento trae por qué es la clave y por qué cae cada
     opción; si la pregunta viene del compilado ASED, dice «Fuente: compilado ASED (no es del ICFES)»
     (en Química ninguna: once son del SIMULACRO II 2023 de química y trece de los cuadernillos 2016-1).
  5. `[hidden]{display:none!important}`, como en Biología: sin esa regla la clave del libro se ve
     antes de revelarla.

Comprueba antes de escribir: plan_qui.verificar() (claves del libro y del entrenamiento contra los
docstrings de quiN.py y quiN_icfes.py) y textos_qui.verificar() (el .md contra módulos e icfes.csv).
"""
import copy, os, re, sys, types

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import clase_viva as CV
import plan_qui as P
import textos_qui

CV.FICFES = "Pregunta Saber 11"          # decisión de Nelson, 10 nov: sin año ni «oficial»

OUT = os.path.join(AQUI, "..", "entregables", "guias_quimica")
CSS_EXTRA = ("[hidden]{display:none!important}\n" + textos_qui.CSS +
             ".aviso{border-left-color:var(--rojo)}"
             ".aviso.sev-baja{background:#EEF3FA;border-left-color:var(--azul)}\n")

# ─────────────────────────────── títulos de cada clase ───────────────────────────────
TITULOS = {
    1: "Disolver, separar y reaccionar",
    2: "El calor, los cambios de estado y la densidad",
    3: "Mezclar no es transformar",
    4: "Cada propiedad física separa algo",
    5: "El carbono en el tanque, en el vaso y en la bolsa",
    6: "Reacciones que calientan y encadenan",
}
LEADS = {
    1: "La sal que se queda en el fondo, el gas que se escapa de la gaseosa, la pastilla que se demora en "
       "salir. Hoy todo número va con su unidad, y cada sustancia se reconoce por lo que las otras no tienen.",
    2: "El agua hierve y el termómetro no se mueve. ¿Adónde se fue el calor? Hoy seguimos la energía tramo "
       "por tramo y la explicamos con partículas que se mueven y chocan.",
    3: "Dos vasos, una tableta, un charco con aceite, una cafetera que sube y baja. Hoy cambiamos una sola "
       "cosa a la vez y pedimos la evidencia antes de creer.",
    4: "El imán, el colador, el viento, la bandeja que vibra: cada uno separa por una propiedad distinta. "
       "Hoy la comparación tiene que ser pareja y cada propiedad tiene su nombre.",
    5: "La gasolina, el café y la bolsa del supermercado tienen carbono. Hoy miramos la pieza de la molécula "
       "que decide lo que hace, y contamos los átomos que entran y salen.",
    6: "La última clase de contenido del área. Una ecuación es una receta, el termómetro dice si el calor "
       "sale o entra, y una conclusión vale lo que valen sus datos.",
}

# ─────────────── la redacción de pantalla y de la guía, para Química ───────────────

UI = dict(
    portada_decir=["«Libro abierto, cuaderno cerrado, lápiz. Hoy no les voy a preguntar fórmulas de "
                   "memoria: les voy a preguntar qué número, con qué unidad, lo dice.»"],
    regla_lead="Si el instrumento está vacío, no lo resolviste: lo adivinaste.",
    regla_p=("Primero se escribe el instrumento —la cuenta con sus unidades, la propiedad, el dibujo de "
             "las partículas—, después se marca la opción. Una respuesta correcta con el instrumento en "
             "blanco no cuenta como resuelta."),
    regla_decir=["«La respuesta correcta con el instrumento vacío no cuenta. ¿Por qué? Porque en Química "
                 "casi todas las opciones suenan técnicas: el que no escribió la cuenta escoge la que suena "
                 "mejor, no la que dicen los números.»"],
    regla_apoyo=["Si alguien pregunta para qué escribir, la respuesta corta es: lo que separa la opción "
                 "correcta de las que suenan bien está en un número, una unidad o una fila de la tabla, y "
                 "eso se pierde si no se escribe.",
                 "Si alguien dice «es una reacción química» o «es por la presión», devuélvele la pregunta: "
                 "«¿qué viste o qué mediste que te lo dice?»."],
    act_h2="¿Qué se observó, qué se midió y con qué unidad, y qué hacen las partículas?",
    act_lead="Tres respuestas antes de cualquier explicación. Todavía no se abre el cuaderno.",
    act_apoyo=("No expliques el fenómeno ni aceptes todavía explicaciones: primero las tres respuestas. "
               "La observación es inventada para la clase: no sale del libro, y nada de ella se hace en el "
               "salón."),
    dina_decir=["«Esto no es recreo: es la misma operación que van a hacer con la tabla o la ecuación en "
                "cinco minutos —contar, comparar o seguir a las partículas—, pero con el cuerpo.»"],
    prob_lead="Antes de releer el texto o la tabla: ¿cuál creen que es? Levanten la mano.",
    prob_lead2=P.PREGUNTA_AREA,
    bloque_h2="Preguntas {a} y {b}: primero el instrumento, después la opción",
    bloque_decir=["«Antes de marcar: ¿qué cuenta o qué dato escribieron en el instrumento? Léanmelo con "
                  "su unidad.»",
                  "Si alguien se traba, pregúntale qué se midió y en qué unidad. Si el instrumento está "
                  "vacío, vuelve al texto o a la tabla antes que a las opciones."],
    bloque_apoyo=("Las claves del libro son {a}·{ka} y {b}·{kb}. No las reveles hasta que todos tengan "
                  "el instrumento escrito: el botón es para el cierre del bloque."),
    reto_defensa=("<b>La defensa:</b> tres minutos por equipo, señalando el dato con su unidad, la cuenta o "
                  "la propiedad que los respalda. «Es que así reacciona» no cuenta."),
    reto_apoyo=["El reto no tiene una sola respuesta correcta: gana el equipo que mejor sostiene la suya "
                "con datos. Si dos explicaciones están sostenidas, dilo: eso también es hacer ciencia.",
                "Si un equipo entrega una sola hoja para los tres, el reto no cuenta. La discusión es "
                "compartida; el registro es individual.",
                "Los retos se resuelven en papel: ninguno se hace con sustancias en el salón.",
                "Cierra mostrando qué variable, qué unidad o qué propiedad quedó por fuera en cada propuesta."],
    icfes_decir=["Durante la evaluación no se proyecta nada: las preguntas están en el cuaderno. Esta "
                 "diapositiva es para el cierre, cuando se socializan las falladas.",
                 "«¿Qué escribiste en el instrumento antes de mirar las opciones? ¿Qué número lo decide?»"],
)

# ───────────── los avisos del libro que salen en pantalla (al revelar las claves) ─────────────
# Clave: (misión, rótulo del aviso en plan_qui.AVISOS). Valor: (rótulo que usa el motor, severidad,
# texto para el estudiante). Lo que no está aquí va solo a la guía del profe: reparto de claves,
# patrones de opciones, fuentes sin verificar y figuras que no se proyectan.
PROYECTAR = {
    (1, "preg. 4"): ("preg. 4", "baja",
        "El dibujo del libro no trae 40 y 16 bolitas: la cuenta se hace con los números del texto."),
    (1, "preg. 2"): ("preg. 2", "atención",
        "La clave dice que el CO₂ «se comprime». Más preciso: con más presión del gas encima, más "
        "moléculas entran al líquido."),
    (2, "preg. 1"): ("preg. 1", "media",
        "Errata del libro: el texto dice que Y se funde a 160 °C y la gráfica pone la meseta en 200 °C. "
        "Se responde con el texto; la clave no cambia."),
    (2, "preg. 10"): ("preg. 10", "media",
        "Lo que hace subir la esfera es el empuje: el mercurio es más denso que ella. La clave A solo "
        "explica por qué sube rápido; la causa principal no estaba entre las opciones."),
    (2, "preg. 8"): ("preg. 8", "baja",
        "Errata del libro: un sólido no se mide en mililitros. La clave no cambia."),
    (3, "preg. 9"): ("preg. 9", "alta",
        "Ninguna opción es limpia: el aire entra por el filtro y el tubo, no «por las juntas». La A es la "
        "que tiene bien el mecanismo, el vacío que succiona aire. Si la discutiste con argumentos, leíste "
        "bien."),
    (3, "preg. 2"): ("preg. 2", "media",
        "La opción A también tiene química: una bebida ácida alimenta la efervescencia. Pero el texto no "
        "dice nada de acidez: lo único distinto del vaso 2 es el gas."),
    (3, "preg. 1"): ("preg. 1", "atención",
        "Luis cambió dos cosas a la vez, la temperatura y la agitación: con estos datos no se sabe cuál "
        "de las dos hizo la diferencia."),
    (4, "preg. 1"): ("preg. 1", "media",
        "Ojo: en la realidad el azúcar se disuelve mucho más que el sulfato de cobre. La clave A es la "
        "mejor con ESTA tabla, no una verdad química."),
    (4, "preg. 9"): ("preg. 9", "atención",
        "En la clave, «reacción» quiere decir respuesta a la vibración: no hay ninguna reacción química."),
    (5, "preg. 10"): ("preg. 10", "media",
        "La clave encadena mal la causa: el biodiésel casi no suelta azufre porque el aceite vegetal casi "
        "no lo trae. Y el biodiésel es un éster, no un alqueno. La B es la menos mala de las cuatro."),
    (5, "preg. 4"): ("preg. 4", "media",
        "El texto dice que lo polar ayuda a la cafeína a llegar al cerebro: en general es al revés. Lo "
        "polar sí la ayuda a disolverse en la sangre, que es lo que pide la pregunta."),
    (6, "preg. 5 y 6"): ("preg. 5", "alta",
        "El gel y el almidón ya son polímeros: al amasarlos no nace un polímero nuevo, sus cadenas se "
        "enredan y se atraen. Las claves B valen dentro del modelo del libro; en la 6, quien defienda la D "
        "con química tiene parte de razón."),
    (6, "preg. 9"): ("preg. 9", "media",
        "El libro no da las masas molares: Fe = 56 g/mol y O = 16 g/mol."),
    (6, "preg. 2 a 4"): ("preg. 2", "media",
        "Por mol, el biogás suelta menos energía; por gramo, el metano suelta más que la gasolina. La "
        "pregunta se responde por mol, como dice el texto."),
    (6, "preg. 1"): ("preg. 1", "baja",
        "Errata de la gráfica del libro: en el eje, el «3» debe ser 4."),
}

FRANJA = ("El concepto del día —una propiedad, una ley o una relación entre cantidades—, en «Palabras "
          "que me frenaron», con tus palabras.")

# Seguridad (Nelson): la clase de Química no maneja sustancias. Va en la portada de cada guía del profe.
SEGURIDAD = ("Seguridad: las dinámicas son con el cuerpo, tarjetas, cinta y clips; ninguna usa sustancias, "
             "fuego ni calor de verdad, y los retos se resuelven en papel. Si alguien propone hacer en el "
             "salón el experimento del libro, la respuesta es no.")
CUIDADO = {
    3: "La activación y las preguntas 2 a 4 hablan de vasos con sustancias y de una tableta efervescente: "
       "se leen y se dibujan, no se hacen.",
    6: "Las preguntas hablan de ácido clorhídrico, hidróxido de sodio y combustibles: son casos para razonar "
       "en papel. Nada de eso entra al salón.",
}

# Nombres de la política colombiana que no pueden salir (regla del proyecto). Química no trae ninguno;
# la revisión se deja por si alguien agrega un caso.
PROHIBIDOS = ["Petro", "Uribe", "Duque", "Santos", "Benedetti", "Pastrana", "Gaviria", "Samper",
              "Cepeda", "Vargas Lleras", "Fajardo", "Claudia López"]
# Lo que no puede decir la pantalla (membrete de Nelson, 10 nov).
NO_EN_PANTALLA = ["oficial", "reales del ICFES", "real del ICFES", "Pregunta real", "del ICFES"]


# ─────────────────────────────── datos ───────────────────────────────
def paginas(mis):
    b = P.BASE[mis]
    return [b, b + 1, b + 3, b + 4, b + 5], [b + 2, b + 6]


def clasifica_avisos():
    """Reparte plan_qui.AVISOS en: los que se proyectan (motor), los que van a la guía en su
    pregunta del taller, los de una pregunta de entrenamiento y los generales de la misión."""
    proy, taller, icfes, general = {}, {}, {}, {}
    for mis, lista in P.AVISOS.items():
        proy[mis] = []
        for preg, sev, que, hacer in lista:
            if (mis, preg) in PROYECTAR:
                rot, sev2, txt = PROYECTAR[(mis, preg)]
                proy[mis].append((rot, sev2, txt, hacer))
            nums = [int(x) for x in re.findall(r"\d+", preg)]
            if " a " in preg and len(nums) == 2:
                nums = list(range(nums[0], nums[1] + 1))
            if preg.startswith("ICFES") and nums:
                for k in nums:
                    icfes.setdefault((mis, k), []).append(
                        f"Aviso ({sev}), solo para ti: {que} Qué haces: {hacer}")
            elif preg.startswith("preg") and nums:
                if (mis, preg) in PROYECTAR:
                    # el motor pone en el bloque el texto proyectado y lo que hace el profe; el aviso
                    # completo, con lo que dice el libro, va también a las otras preguntas que toca
                    rot_n = int(re.findall(r"\d+", PROYECTAR[(mis, preg)][0])[0])
                    nums = [n for n in nums if n != rot_n and (n - 1) // 2 != (rot_n - 1) // 2]
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
    malas = P.verificar() + textos_qui.verificar(icfes)
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
    ns.SELLOS = [s for s in P.SELLOS if isinstance(s[3], int)]
    return ns


def ui(mis):
    l0, l1 = P.LIBRO[mis]
    u = dict(UI)
    u["portada_libro"] = f"Las diez preguntas de la prueba de campo, páginas {l0} a {l1}"
    u["prob_sub"] = ("Nadie justifica con «yo sé que» ni con una palabra técnica suelta: toda respuesta "
                     "señala un número con su unidad, una fila de la tabla o un punto de la gráfica.")
    t_pags, _ = paginas(mis)
    u["prob_apoyo"] = [
        f"La pregunta modelo es la 1 del libro (página {P.PAG_LIBRO[mis][0]}). El cuaderno se abre en la "
        f"página {t_pags[0]} solo en «mi primera idea».",
        "Cuenta las manos tocando cada letra: el número queda en pantalla y sirve para el final del "
        "momento, cuando el grupo vea cuántos cambiaron de opinión al volver al texto o a la tabla.",
        "No digas la clave en este momento: sale en el bloque de las preguntas 1 y 2, después de llenar el "
        "instrumento en pantalla, casilla por casilla. Ahí se trabaja por qué cae cada una de las otras tres."]
    return u


def area(mis, P_ns, textos, taller):
    return CV.Area(
        nombre="Química", prefijo="QUI", fuerte="Si Química no es tu fuerte",
        color=CV.color_de("Química"), P=P_ns,
        claves_libro=lambda m: P.CLAVES[m],
        preguntas_icfes=CV.preguntas_de_textos(textos),
        textos=textos, advertencias={}, taller=taller, saberes=P.SABERES,
        activacion=P.ACTIVACION, titulos=TITULOS, leads=LEADS,
        est_col=list(P.COLS_MIS[mis]),
        colores=dict(m2="#1F4E8C", m3="#3B3BA6", m4=P.MORADO, m5=P.ROJO, m6=P.PIZARRA, rojo=P.ROJO),
        textos_ui=ui(mis), apoyo_fuerte="Química no es tu área", out=OUT)


# ─────────────────────────── lo que se agrega a las escenas ───────────────────────────
def apoyo_portada(mis, general):
    d = P.MISIONES[mis]
    out = ["⚑ Antes del sábado: " + P.limpia(d["ojo"]), SEGURIDAD]
    if mis in CUIDADO:
        out.append("Con cuidado: " + CUIDADO[mis])
    for g in general.get(mis, []):
        out.append("Del libro, para ti: " + g)
    out.append("Los cuatro conceptos que tienes que poder explicar hoy en dos minutos, sin jerga. Si un "
               "estudiante sabe más que tú de un tema, déjalo explicar y pide que señale en el texto o en "
               "la tabla de dónde lo saca:")
    out += [f"{t}: {x}" for t, x in P.NO_ES_TU_FUERTE[mis]]
    return out


def con_figura(sc, mis, k):
    """Pone la figura de la pregunta en el panel del texto y, si las opciones son gráficas o figuras,
    las pone encima de las cuatro letras (que quedan en una sola fila)."""
    marca = f"<p>{CV.E(textos_qui.MARCA)}</p>"
    fig = textos_qui.FIGURAS.get((mis, k))
    if fig:
        assert marca in sc["html"], f"M{mis} P{k}: falta la marca de la figura"
        sc["html"] = sc["html"].replace(marca, fig)
    assert marca not in sc["html"], f"M{mis} P{k}: la marca quedó sin figura"
    fop = textos_qui.FIG_OPCIONES.get((mis, k))
    if fop:
        ops = f'<div class="ops" id="icf{mis}{k}">'
        assert ops in sc["html"]
        sc["html"] = sc["html"].replace(ops, f'<div class="opsfig">{fop}</div><div class="ops cuatro" id="icf{mis}{k}">')
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
    # las cuatro preguntas de entrenamiento: diapositivas 15 a 18
    for k in range(1, 5):
        con_figura(sc[13 + k], mis, k)
    viejo = "La palabra nueva del día, en la franja de vocabulario, con tus palabras."
    assert viejo in sc[-1]["html"]
    sc[-1]["html"] = sc[-1]["html"].replace(viejo, FRANJA).replace(
        "¿En qué se parecía la pregunta del ICFES a la de tu libro?",
        "¿En qué se parecía la pregunta tipo Saber 11 a la de tu libro?")
    return sc



def escenas_simulacro(A, textos):
    """Clases 7 y 8 (decisión de Nelson, 10 nov): salen del motor con plan_qui.C7 y C8."""
    return CV.escenas_clase7(A), CV.escenas_clase8(A)


# ─────────────────────────────── escribir ───────────────────────────────
def revisar_pantalla(html, archivo):
    hay = [n for n in PROHIBIDOS if re.search(r"\b" + re.escape(n) + r"\b", html)]
    if hay:
        raise SystemExit(f"{archivo}: trae nombres que no pueden salir: {hay}")
    sin_ased = html.replace("compilado ASED (no es del ICFES)", "").replace("como «del ICFES»", "")
    malo = [t for t in NO_EN_PANTALLA if re.search(r"\b" + re.escape(t) + r"(es)?\b", sin_ased, re.I)]
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
    icfes = textos_qui.leer()
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
        hechos.append(escribir(A, f"QUI_Clase{mis}_Mision{mis}.html", f"Química · Clase {mis}",
                               f"Momento {mis} · {d['comp']} · páginas {d['pags']}", sc))
    A = area(1, P_ns, textos, taller)
    A.out = out
    sc7, sc8 = escenas_simulacro(A, textos)
    hechos.append(escribir(A, "QUI_Clase7_Simulacro.html", "Química · Clase 7",
                           CV.subtitulos_simulacro(A)[0], sc7))
    hechos.append(escribir(A, "QUI_Clase8_Devolucion.html", "Química · Clase 8",
                           CV.subtitulos_simulacro(A)[1], sc8))
    return hechos


if __name__ == "__main__":
    construir(sys.argv[1] if len(sys.argv) > 1 else OUT)
