#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUÍAS DE CLASE PROYECTABLES («clase viva») · FÍSICA · las 8 del área.

    python3 clase_viva_fis.py [carpeta]      (por defecto entregables/guias_fisica/)
    python3 clase_viva_fis.py --zip          (además arma entregables/EDUCATE_Guias_Fisica.zip)

Usa el motor clase_viva.py sin cambiarlo, igual que clase_viva_bio.py (el modelo que se copia aquí).
Lo que entra de Física:

  · plan_fis.py: FASES, MISIONES, TALLER, DINAMICAS, RETOS, SELLOS, SABERES, ACTIVACION,
    PROBLEMATIZADORA, PREGUNTA_AREA, NO_ES_TU_FUERTE, COLS_MIS, COMP_ICFES, BANCO, CLAVES, AVISOS y
    ASED (las dos preguntas de entrenamiento que salen del compilado ASED).
  · textos_fis.py: las 24 preguntas de entrenamiento de TEXTOS_FIS.md (texto completo, enunciado,
    opciones, clave verificada, por qué, notas) y sus figuras redibujadas: FIGURAS va en el panel
    del texto y FIG_OPCIONES, cuando las opciones son dibujos, en la columna de las opciones.
  · lo escrito aquí: TITULOS, LEADS, la redacción de pantalla (UI), qué aviso del libro se proyecta
    al revelar (PROYECTAR), las cuentas de cada reto para el profe (CUENTAS_RETO) y lo que pide
    cuidado en cada clase (CUIDADO: la seguridad de las dinámicas).

Lo que hace este módulo además de llenar el Area:

  1. Un Area por misión: cada estrategia se pinta con el color de su chip en el cuaderno (COLS_MIS).
     Los momentos: m1 = verde oliva del área (#5C7A1E, activación), m2 azul, m3 índigo, m4 morado,
     m5 rojo (la evaluación) y m6 pizarra (#4A5A70): el cierre no va en verde para no confundirse
     con el área ni con la opción correcta revelada, que el motor marca en verde (#2E7A39). El oliva
     no se usa en ninguna estrategia ni en otro momento.
  2. Membrete «Pregunta Saber 11» (Nelson, 10 nov): se fija en CV.FICFES antes de escribir, sin
     tocar clase_viva.py. En pantalla nunca dice «oficial» ni «reales»; `revisar_pantalla()` falla
     si aparece.
  3. Las figuras van en SVG o tabla en línea: el archivo sigue siendo único y funciona sin internet.
  4. La guía del profe de cada pregunta de entrenamiento trae por qué es la clave y por qué cae cada
     opción; las dos del compilado ASED (M1 P1 y M2 P1) llevan primero «Fuente: compilado ASED (no
     es del ICFES)».
  5. `[hidden]{display:none!important}`, como en Biología y Sociales: sin esa regla la clave del
     libro se ve antes de revelarla.

Comprueba antes de escribir: plan_fis.verificar() (claves del libro y del entrenamiento contra los
docstrings de fisN.py y fisN_icfes.py) y textos_fis.verificar() (el .md contra módulos e icfes.csv).
"""
import copy, os, re, sys, types, zipfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import clase_viva as CV
import plan_fis as P
import textos_fis

CV.FICFES = "Pregunta Saber 11"          # decisión de Nelson, 10 nov: sin año ni «oficial»

OUT = os.path.join(AQUI, "..", "entregables", "guias_fisica")
ZIP = os.path.join(AQUI, "..", "entregables", "EDUCATE_Guias_Fisica.zip")
CSS_EXTRA = ("[hidden]{display:none!important}\n" + textos_fis.CSS +
             ".aviso{border-left-color:var(--rojo)}"
             ".aviso.sev-baja{background:#EEF3FA;border-left-color:var(--azul)}\n")

# ─────────────────────────────── títulos de cada clase ───────────────────────────────
TITULOS = {
    1: "Nada se mueve porque sí",
    2: "El calor siempre va hacia lo frío",
    3: "Lo que mueve a las cargas",
    4: "La fuente marca el ritmo",
    5: "La energía que sube, corre y se escapa",
    6: "Ningún julio se pierde",
}
LEADS = {
    1: "Si algo arranca, frena o cambia de dirección, hay una fuerza con nombre detrás. Hoy dibujamos "
       "cada fuerza como una flecha, leemos el movimiento en una gráfica y seguimos la energía hasta "
       "donde se va.",
    2: "La sopa se enfría, el vidrio se empaña, el agua hierve. Hoy seguimos el calor de lo caliente a "
       "lo frío, lo contamos con su unidad y miramos qué hacen las partículas cuando se calientan.",
    3: "Un imán que entra a una bobina, una tormenta, una aguja que deja de ser imán. Hoy buscamos el "
       "dato que decide, dibujamos el campo antes de elegir y llevamos el signo de cada carga.",
    4: "Luz, sonido, Wi-Fi: todo son ondas. Hoy separamos lo que pone la fuente de lo que pone el medio, "
       "dibujamos antes de elegir y concluimos solo lo que se observó.",
    5: "Un dron, un sifón, un reloj en órbita. Hoy cada magnitud va con su fórmula y su unidad, y "
       "ninguna fuerza se queda sin decir quién la hace.",
    6: "La última clase de contenido del área. La energía entra, se transforma y una parte se va como "
       "calor, pero nunca desaparece. Hoy cerramos todas las cuentas.",
}

# ─────────────── la redacción de pantalla y de la guía, para Física ───────────────
COMPETENCIAS = [("UC · uso comprensivo del conocimiento científico", "conceptos y modelos de la física",
                 "var(--m2)"),
                ("EF · explicación de fenómenos", "por qué pasa, causa por causa", "var(--m4)"),
                ("IN · indagación", "preguntas, variables y conclusiones", "var(--m6)")]

UI = dict(
    portada_decir=["«Libro abierto, cuaderno cerrado, lápiz. Hoy nadie me va a decir la fórmula de "
                   "memoria: me van a mostrar la flecha o el julio que explica lo que pasa.»"],
    regla_lead="Si el instrumento está vacío, no lo resolviste: lo adivinaste.",
    regla_p=("Primero se hace el instrumento —el diagrama de fuerzas, la cuenta con unidades, la ficha "
             "del experimento—, después se marca la opción. Una respuesta correcta con el instrumento en "
             "blanco no cuenta como resuelta."),
    regla_decir=["«La respuesta correcta con el instrumento vacío no cuenta. ¿Por qué? Porque en Física "
                 "casi todas las opciones usan palabras técnicas: el que no dibujó la flecha ni hizo la "
                 "cuenta escoge la que suena mejor, no la que es.»"],
    regla_apoyo=["Si alguien pregunta para qué dibujar, la respuesta corta es: lo que separa la opción "
                 "correcta de las que suenan bien está en el sentido de una flecha, en un signo o en una "
                 "unidad, y eso se pierde si no se escribe.",
                 "Si alguien dice «es por la gravedad» o «es la energía», devuélvele la pregunta: "
                 "«¿quién empuja a quién, y hacia dónde?»."],
    act_h2="¿Qué cambió y qué lo causó?",
    act_lead="Dos respuestas antes de cualquier fórmula. Todavía no se abre el cuaderno.",
    act_apoyo=("No expliques el fenómeno ni aceptes todavía fórmulas: primero qué cambió y qué lo causó, "
               "dicho como una flecha con nombre. La observación es inventada para la clase: no sale del "
               "libro."),
    dina_decir=["«Esto no es recreo: es la misma operación que van a hacer con el dibujo o con la cuenta "
                "en cinco minutos —nombrar la flecha, llevar la cuenta, separar lo que cambia de lo que "
                "no—, pero con el cuerpo.»",
                "Nadie corre ni lanza nada. Si la dinámica pide moverse, se camina."],
    prob_lead="Antes de dibujar o calcular: ¿cuál creen que es? Levanten la mano.",
    prob_lead2=P.PREGUNTA_AREA,
    bloque_h2="Preguntas {a} y {b}: primero el instrumento, después la opción",
    bloque_decir=["«Antes de marcar: ¿qué flecha dibujaron, o qué cuenta hicieron? Léanmela con su unidad.»",
                  "Si alguien se traba, pregúntale qué cambió y quién lo causó. Si el instrumento está "
                  "vacío, vuelve al dibujo o al enunciado antes que a las opciones."],
    bloque_apoyo=("Las claves del libro son {a}·{ka} y {b}·{kb}. No las reveles hasta que todos tengan "
                  "el instrumento hecho: el botón es para el cierre del bloque."),
    reto_defensa=("<b>La defensa:</b> tres minutos por equipo, señalando la flecha, la cuenta con su unidad "
                  "o la variable que los respalda. «Porque sí» o «así dice la fórmula» no cuentan."),
    reto_apoyo=["El reto no tiene una sola respuesta correcta en todas sus partes: gana el equipo que mejor "
                "sostiene la suya con flechas y cuentas. Si dos explicaciones están sostenidas, dilo: eso "
                "también es hacer física.",
                "Si un equipo entrega una sola hoja para los tres, el reto no cuenta. La discusión es "
                "compartida; el registro es individual.",
                "Cierra mostrando qué fuerza, qué julio o qué variable quedó por fuera en cada propuesta."],
    icfes_decir=["Durante la evaluación no se proyecta nada: las preguntas están en el cuaderno. Esta "
                 "diapositiva es para el cierre, cuando se socializan las falladas.",
                 "«¿Qué dibujaste o qué calculaste antes de mirar las opciones? ¿Qué flecha o qué número "
                 "lo decide?»"],
    c7_h1="Hoy nadie les va a decir si acertaron",
    c7_lead=("Veinticuatro preguntas tipo Saber 11, seguidas, como en la prueba. Lo único que llevan es "
             "lo que entrenaron: la flecha con su nombre y la cuenta con su unidad antes de mirar las "
             "opciones."),
    c7_decir=["«Pueden dibujar y hacer cuentas al margen: en la prueba real también pueden rayar el "
              "cuadernillo, y es lo que entrenamos.»"],
    c7_reglas=["En silencio y en filas individuales.", "No se responde ninguna duda, ni de vocabulario.",
               "Las dudas se escriben en el margen.",
               "Primero la flecha o la cuenta, después la opción."],
    c7_apoyo_reglas=["Anota quién va directo a las opciones sin dibujar ni calcular nada: es el dato más "
                     "útil del simulacro, más que el puntaje."],
    c7_competencias=COMPETENCIAS,
    c8_h1="Lo que dibujaste esta vez",
    c8_lead=("Hoy no hay pregunta nueva. Hoy vamos a poner tu instrumento de hace seis semanas al lado "
             "del de hoy."),
    c8_apoyo_elegir=["Si dudas entre dos, quédate con la de la competencia que más manos tuvo en el "
                     "conteo de la clase 7."],
    c8_h2="¿Qué flecha, qué julio o qué unidad viste esta vez que antes no?",
    c8_decir=["«Pongan las dos hojas una al lado de la otra. ¿Qué dibujaron o calcularon distinto?»"],
    c8_apoyo=["Si nadie escribió distinto, la estrategia no se instaló todavía: anótalo en el registro "
              "para el reporte de los especialistas."],
)

# ───────────── los avisos del libro que salen en pantalla (al revelar las claves) ─────────────
# Clave: (misión, rótulo del aviso en plan_fis.AVISOS). Valor: (rótulo que usa el motor, severidad,
# texto para el estudiante). Lo que no está aquí va solo a la guía del profe: reparto de claves,
# fuentes, figuras sin consecuencia y supuestos de fondo no se proyectan.
PROYECTAR = {
    (1, "preg. 6"): ("preg. 6", "media",
        "Dos opciones se pueden defender: apoyar los dos pies (B) agranda la base de apoyo, y flexionar más "
        "la rodilla (C) alarga el choque y baja la fuerza. La clave tomada es B. Si defendiste C con el "
        "impulso, tienes un argumento."),
    (1, "preg. 3"): ("preg. 3", "media",
        "El diagrama del libro dibuja la normal vertical: es perpendicular a la rampa. Y la parte del peso "
        "que hace bajar el carro va a lo largo de la rampa, no hacia abajo."),
    (1, "preg. 8"): ("preg. 8", "media",
        "La flecha de la fuerza centrípeta del libro apunta hacia el borde: la fuerza centrípeta apunta "
        "hacia el centro del giro."),
    (2, "preg. 10"): ("preg. 10", "alta",
        "Dos opciones son correctas: la A y la D dan el mismo 0,25 cal/(g·°C), porque los dos signos menos "
        "de la A se cancelan. La clave tomada es D. Si marcaste A con la cuenta bien hecha, también tienes "
        "razón."),
    (2, "preg. 4"): ("preg. 4", "media",
        "El texto del libro lo dice al revés: con menos presión el agua hierve a menos temperatura y cocina "
        "más despacio. La olla a presión cocina rápido porque la presión es alta."),
    (3, "preg. 1"): ("preg. 1", "media",
        "La corriente aparece porque el campo magnético cambia mientras el imán entra o sale, no porque el "
        "campo «empuje» a los electrones. La clave tomada es D; la B también se puede defender."),
    (3, "preg. 6"): ("preg. 6", "media",
        "En la figura B las flechas apuntan al revés: con dos cargas positivas las líneas salen de cada "
        "carga. La forma de la B es la correcta: por eso es la mejor de las cuatro."),
    (4, "preg. 3"): ("preg. 3", "alta",
        "El esquema del libro tiene dos rayos con la letra A y el B está en el aire. La razón correcta es "
        "la de la opción B: al entrar al agua la luz va más lenta y se acerca a la normal."),
    (4, "preg. 9"): ("preg. 9", "alta",
        "Ninguna opción da la razón principal: en el caucho la onda va lenta porque el caucho es poco "
        "rígido. La absorción hace la onda más pequeña, no más lenta. La C es la única que dice algo cierto "
        "del caucho."),
    (4, "preg. 4"): ("preg. 4", "media",
        "La A y la D se pueden defender; la explicación principal es la A: el metal refleja casi toda la "
        "señal que le llega."),
    (4, "preg. 6"): ("preg. 6", "media",
        "Los dos vasos están casi a la misma distancia del dinosaurio: la diferencia se explica mejor por el "
        "vaso y el agua. La clave A concluye más de lo que se observa."),
    (5, "preg. 8"): ("preg. 8", "media",
        "La A y la D señalan algo que de verdad no se probó. La clave tomada es A, porque «cualquier "
        "líquido» es lo que más se aleja de un solo ensayo con agua."),
    (5, "preg. 1"): ("preg. 1", "baja",
        "El libro dice que el astronauta «pesa 80 kg». El kilogramo mide masa; el peso es una fuerza y se "
        "mide en newtons."),
    (6, "preg. 1"): ("preg. 1", "media",
        "La B usa los datos contra la afirmación (71 a 73 %). La D también se puede defender si se lee la "
        "eficiencia como electricidad que se vuelve calefacción. La clave tomada es B."),
    (6, "preg. 4"): ("preg. 4", "media",
        "La B y la D son ciertas; la D es más completa: además dice que una hora no basta para generalizar."),
}

# Las cuentas de cada reto, resueltas, para el profe que no es de Física (no se proyectan).
CUENTAS_RETO = {
    1: "Fuerzas en el tobogán: el peso (la Tierra, hacia abajo), la normal (el tobogán, perpendicular a él) "
       "y el rozamiento (el tobogán, contra el movimiento). La gráfica sube mientras baja por el tobogán y "
       "baja hasta cero en la arena. La prueba justa cambia solo la ropa: el mismo niño, el mismo tobogán, "
       "desde el mismo punto. La energía de la altura se volvió movimiento y, por el rozamiento, calor.",
    2: "Q = m · c · ΔT = 200 g · 1 cal/(g·°C) · (80 − 30) °C = 10 000 cal. El tinto se enfría hasta 20 °C, la "
       "temperatura del salón: ahí ya no hay diferencia que empuje el calor. Las partículas se mueven cada "
       "vez más despacio; las que se van como vapor son las más rápidas.",
    3: "F = q · E = 2 × 10⁻⁶ C · 10 000 N/C = 0,02 N. Si la carga es negativa, la fuerza va en contra del campo. "
       "Por el cable del pararrayos se mueven electrones. Un dato que pone a prueba la idea: contar los "
       "rayos que caen en edificios iguales con y sin pararrayos, en la misma zona.",
    4: "La nota (la frecuencia) la pone el parlante: no cambia al atravesar la pared. 84 − 64 = 20 dB: cien "
       "veces menos potencia detrás de la pared que delante, a la misma distancia. «La pared absorbe todo» "
       "no se puede concluir: detrás todavía se oyen 64 dB.",
    5: "Ep = 50 kg · 10 m/s² · 2 m = 1000 J. Ec = ½ · 50 kg · (6 m/s)² = 900 J. Faltan 100 J: se fueron como "
       "calor y sonido por el rozamiento. En el piso, el peso y la normal no hacen trabajo (son "
       "perpendiculares al camino); el rozamiento sí, en contra.",
    6: "E = 3000 W · 600 s = 1 800 000 J = 1,8 MJ. Fracción: 1,44 MJ ÷ 1,8 MJ = 0,8 (80 %). Una sola ducha, un "
       "día, no basta para hablar de «todas las duchas». El agua sale a temperatura constante porque entra "
       "tanta energía por segundo como la que se lleva el agua que sale: es un equilibrio.",
}

FRANJA = ("El concepto del día —una ley, una magnitud o una relación—, en «Palabras que me frenaron», "
          "con tus palabras.")

# Lo que pide cuidado en cada clase (portada de la guía del profe): la seguridad de las dinámicas.
CUIDADO = {
    1: "En «Las flechas de la mochila» la mochila es liviana y los cordones se halan suave. En «Camina la "
       "gráfica» se camina, no se corre: despeja el pasillo antes.",
    2: "En «El baile de las moléculas» los pupitres van a un lado y nadie corre, aunque las palmas vayan "
       "rápido.",
    3: "Ninguna dinámica usa pilas, cables ni enchufes de verdad: las cargas y los circuitos se hacen con "
       "personas y carteles.",
    4: "En «El ritmo y el piso» se camina, nunca se corre. En «Lo que oímos» el golpe a los pupitres es "
       "suave, siempre igual.",
    5: "La mochila de «¿Trabaja o no trabaja?» es liviana y se sube despacio. El carrito de la rampa rueda "
       "solo: no se lanza.",
    6: "Ninguna dinámica usa electricidad real: los ventiladores, el motor y la caja de fichas son de papel.",
}

# Nombres de la política colombiana que no pueden salir (regla del proyecto). Física no trae
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
    """Reparte plan_fis.AVISOS en: los que se proyectan (motor), los que van a la guía en su
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
        if (mis, k) in P.ASED or "ASED" in v.get("fuente", ""):
            notas.insert(0, "⚑ " + P.ASED_NOTA + ". Nelson decide si se reemplaza; mientras tanto, no la "
                            "presentes como «del ICFES».")
        v["notas"] = notas
        out[(mis, k)] = v
    return out


def verificar_claves(icfes):
    malas = P.verificar() + textos_fis.verificar(icfes)
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
    u["prob_sub"] = ("Nadie justifica con «así dice la fórmula» ni con «eso es obvio»: toda respuesta señala "
                     "una flecha del dibujo, un número con su unidad o un renglón del enunciado.")
    t_pags, _ = paginas(mis)
    u["prob_apoyo"] = [
        f"La pregunta modelo es la 1 del libro (página {P.PAG_LIBRO[mis][0]}). El cuaderno se abre en la "
        f"página {t_pags[0]} solo en «mi primera idea».",
        "Cuenta las manos tocando cada letra: el número queda en pantalla y sirve para el final del "
        "momento, cuando el grupo vea cuántos cambiaron de opinión al dibujar la flecha o hacer la cuenta.",
        "No digas la clave en este momento: sale en el bloque de las preguntas 1 y 2, después de llenar el "
        "instrumento en pantalla, casilla por casilla. Ahí se trabaja por qué cae cada una de las otras tres."]
    return u


def area(mis, P_ns, textos, taller):
    return CV.Area(
        nombre="Física", prefijo="FIS", fuerte="Si Física no es tu fuerte",
        color=P.FIS, P=P_ns,
        claves_libro=lambda m: P.CLAVES[m],
        preguntas_icfes=CV.preguntas_de_textos(textos),
        textos=textos, advertencias={}, taller=taller, saberes=P.SABERES,
        activacion=P.ACTIVACION, titulos=TITULOS, leads=LEADS,
        est_col=list(P.COLS_MIS[mis]),
        colores=dict(m2="#1F4E8C", m3="#3B3BA6", m4=P.MORADO, m5=P.ROJO, m6=P.PIZARRA, rojo=P.ROJO),
        textos_ui=ui(mis), apoyo_fuerte="Física no es tu área", out=OUT)


# ─────────────────────────── lo que se agrega a las escenas ───────────────────────────
def apoyo_portada(mis, general):
    d = P.MISIONES[mis]
    out = ["⚑ Antes del sábado: " + P.limpia(d["ojo"])]
    if mis in CUIDADO:
        out.append("Seguridad de las dinámicas: " + CUIDADO[mis])
    for g in general.get(mis, []):
        out.append("Del libro, para ti: " + g)
    out.append("Los cuatro conceptos que tienes que poder explicar hoy en dos minutos, sin jerga. Si un "
               "estudiante sabe más que tú de un tema, déjalo explicar y pide que lo muestre con una flecha "
               "o con una cuenta con unidades:")
    out += [f"{t}: {x}" for t, x in P.NO_ES_TU_FUERTE[mis]]
    return out


def con_figura(sc, mis, k):
    """Pone la figura de la pregunta en el panel del texto y, si las opciones son dibujos, los cuatro
    dibujos encima de las opciones (que quedan en una sola fila)."""
    marca = f"<p>{CV.E(textos_fis.MARCA)}</p>"
    fig = textos_fis.FIGURAS.get((mis, k))
    if fig:
        assert marca in sc["html"], f"M{mis} P{k}: falta la marca de la figura"
        sc["html"] = sc["html"].replace(marca, fig)
    assert marca not in sc["html"], f"M{mis} P{k}: la marca quedó sin figura"
    der = textos_fis.FIG_DERECHA.get((mis, k))
    if der:
        enun = '<p class="enun">'
        assert sc["html"].count(enun) == 1
        sc["html"] = sc["html"].replace(enun, f'<div class="derfig">{der}</div>{enun}')
    opc = textos_fis.FIG_OPCIONES.get((mis, k))
    if opc:
        ops = f'<div class="ops" id="icf{mis}{k}">'
        assert ops in sc["html"]
        sc["html"] = sc["html"].replace(ops, f'<div class="opsfig">{opc}</div>'
                                             f'<div class="ops cuatro" id="icf{mis}{k}">')
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
    # las cuentas del reto, resueltas, para el profe
    reto = [s for s in sc if "Reto del corte" in s["html"]]
    assert len(reto) == 1
    reto[0]["guia"]["apoyo"].insert(0, "Las cuentas del reto, para ti (no se proyectan): " + CUENTAS_RETO[mis])
    # las cuatro preguntas de entrenamiento: diapositivas 15 a 18
    for k in range(1, 5):
        con_figura(sc[13 + k], mis, k)
    viejo = "La palabra nueva del día, en la franja de vocabulario, con tus palabras."
    assert viejo in sc[-1]["html"]
    casilla = f"La casilla {mis} de la portada del área."
    assert casilla in sc[-1]["html"]
    sc[-1]["html"] = (sc[-1]["html"].replace(viejo, FRANJA)
                      .replace(casilla, f"La clase {mis} de la portada del área, con la causa que encontraste.")
                      .replace("¿En qué se parecía la pregunta Saber 11 a la de tu libro?",
                               "¿En qué se parecía la pregunta tipo Saber 11 a la de tu libro?"))
    sc[-1]["guia"]["apoyo"] = [a.replace("La palabra nueva no se dicta", "El concepto del día no se dicta")
                               for a in sc[-1]["guia"]["apoyo"]]
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
    ased = ", ".join(f"M{m}·P{k}" for m, k in sorted(P.ASED))
    sc7[0]["guia"]["apoyo"].append(
        f"Dos de las 24 salen del compilado ASED, que no es del ICFES ({ased}). En pantalla y en el "
        "cuaderno van con el membrete «Pregunta Saber 11», como las demás; no las presentes como «del "
        "ICFES». Nelson decide si se reemplazan.")
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
    # el rótulo de cada botón es el título de la pregunta en TEXTOS_FIS.md: corto y sin repetirse
    todas = [(m, k, rotulo(textos[(m, k)]["titulo"])) for m in range(1, 7) for k in range(1, 5)]
    sc8 = CV.escenas_clase8(A, todas)
    sc8[1]["guia"]["apoyo"].append(
        f"Cada pregunta escogida se repara en las hojas de simulacro del cuaderno (páginas {P.SIM}): un "
        "esquema por pregunta, la que el estudiante escoge o la que le asignas. Las hojas traen la "
        "competencia, la estrategia de la misión, las magnitudes con su unidad y «tacho con razón».")
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
    if "[[figura]]" in html:
        raise SystemExit(f"{archivo}: quedó una marca de figura sin dibujar")


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
    icfes = textos_fis.leer()
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
        hechos.append(escribir(A, f"FIS_Clase{mis}_Mision{mis}.html", f"Física · Clase {mis}",
                               f"Momento {mis} · {d['comp']} · páginas {d['pags']}", sc))
    A = area(1, P_ns, textos, taller)
    A.out = out
    sc7, sc8 = escenas_simulacro(A, textos)
    hechos.append(escribir(A, "FIS_Clase7_Simulacro.html", "Física · Clase 7",
                           "Simulacro del área · 24 preguntas", sc7))
    hechos.append(escribir(A, "FIS_Clase8_Devolucion.html", "Física · Clase 8",
                           "Devolución y cierre del área", sc8))
    return hechos


def empacar(hechos, destino=ZIP):
    """Las 8 en un .zip, en el orden de las clases (la clase 1 también va suelta en la carpeta)."""
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for f, _ in hechos:
            z.write(f, os.path.basename(f))
    print(f"{os.path.basename(destino)} · {len(hechos)} guías · {os.path.getsize(destino)//1024} KB")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    hechos = construir(args[0] if args else OUT)
    if "--zip" in sys.argv:
        empacar(hechos)
