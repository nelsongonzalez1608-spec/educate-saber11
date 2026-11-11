#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Las 12 hojas de entrenamiento Saber 11 de Lectura Crítica CON EL TEXTO COMPLETO (11 nov 2026).

Pedido de Nelson (textual): «No vi las preguntas Saber de lenguaje; en esas sí debes usar el texto
completo de la pregunta ICFES». Hasta ahora estas hojas imprimían solo el párrafo de la evidencia y
decían «el texto completo lo proyecta tu profe». En Lectura Crítica eso no sirve: la competencia es
leer el texto entero.

Cómo se arma cada hoja (sin agregar páginas: cada hoja conserva sus dos preguntas):
  · El texto se compone aquí, con la fuente real (Carlito), justificado con lib.TJ (medido con
    tw(), nunca contando caracteres), en DOS COLUMNAS para que el renglón se pueda leer:
      - si las dos preguntas comparten el texto, va una sola vez arriba, a lo ancho;
      - si son dos textos y uno es corto, cada tarjeta lleva el suyo (dentro de la tarjeta);
      - si el texto de la segunda pregunta es largo (Facebook, Kavafis), va a lo ancho justo
        antes de su tarjeta: el orden de lectura es siempre texto → pregunta.
    Letra del texto: 20 unidades (6,1 pt); si no cabe, 19 y luego 18 (5,5 pt), nunca menos.
  · De la tarjeta original (PDF entregado, en vectores) se recortan el enunciado, las opciones y el
    instrumento, igual que en rehace_hojas.py. Lo que se quita es el «párrafo donde está la
    evidencia», la referencia y el letrero «El texto completo lo proyecta tu profe» (modo `drop`);
    cuando el recuadro es parte de la pregunta («Lea el siguiente fragmento…», «Considere el
    siguiente fragmento…») el recuadro se queda y solo salen la referencia y el letrero (`caja`);
    si el recuadro ya era el texto completo (poema de Gómez Jattin, viñeta de «Checho», la frase
    del eufemismo) no se quita nada (`nada`). Si hace falta, los recortes de una tarjeta se escalan
    juntos (mismo k), anclados a la izquierda; nunca por debajo de K_MIN = 0,75.
  · La columna derecha (marco al final, ¿qué tan seguro?, salvavidas, ¿en qué se parece a lo del
    taller?) es la misma, un poco más compacta, para que las tarjetas puedan tener el alto que
    necesitan. La franja «palabras que me frenaron» va solo si cabe.
  · El sello «entrena la estrategia n · …» se mide con tw() y lleva más aire (pad 26): con pad 18
    el texto rozaba el borde y, rasterizado, parecía salirse (página 63).

Las fuentes de cada texto están en TEXTOS (campo `fuente` y `verificado`). Lo que no se pudo verificar
contra la fuente original se imprime como lo trae TEXTOS_GUIA_DOCENTE.md (lo mismo que ya proyecta la
guía) y queda dicho en el informe.

Lo llama rehace_hojas.py para las hojas lc*_i*; arma_pdf.py las compone como cualquier otra hoja
rehecha (marco nuevo + recortes del original).
"""
import os
import re

import taller_base as tb
from taller_base import *          # noqa: F401,F403
import bitacora as BT
import rehace_hojas as rh

RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
MD = os.path.join(RAIZ, "libro", "TEXTOS_GUIA_DOCENTE.md")

K_MIN = 0.75
RIGHT_MIN = 780          # alto mínimo de una tarjeta: lo pide la columna derecha compacta
Y_FIN = 2446             # hasta aquí puede bajar la última tarjeta (el pie está en 2498)
GAP_B = 22               # entre bloques
HEAD = 108               # encabezado de la tarjeta («Pregunta para entrenar», membrete, sello)


# ───────── los textos ─────────
def _md_texto(titulo):
    """Párrafos citados («>») bajo «### titulo» en TEXTOS_GUIA_DOCENTE.md, sin las negritas ni las
    cursivas que puso el documento para el profesor (no están en la fuente: serían una pista)."""
    lineas = open(MD, encoding="utf-8").read().split("\n")
    i = lineas.index("### " + titulo)
    pars, cur, autor = [], [], None
    for ln in lineas[i + 1:]:
        s = ln.strip()
        if s.startswith("**Lo que") or s.startswith("## ") or s.startswith("---"):
            break
        if autor is None and s.startswith("**") and not s.startswith("**Lo"):
            autor = s
            continue
        if s.startswith(">"):
            t = s.lstrip(">").strip()
            if t:
                cur.append(t)
            elif cur:
                pars.append(" ".join(cur)); cur = []
        elif cur and not s:
            pars.append(" ".join(cur)); cur = []
    if cur:
        pars.append(" ".join(cur))
    limpia = lambda t: re.sub(r"\*([^*]+)\*", r"\1", re.sub(r"\*\*(.+?)\*\*", r"\1", t))
    return [limpia(p) for p in pars], limpia(autor or "").strip("* ")


def _md(titulo, pie=None, titulo_impreso=None, nota=""):
    pars, autor = _md_texto(titulo)
    return dict(titulo=titulo_impreso if titulo_impreso is not None else titulo, parrafos=pars,
                pie=pie if pie is not None else autor, verificado=False,
                fuente="TEXTOS_GUIA_DOCENTE.md (lo que proyecta la guía); fuente original no "
                       "disponible en este entorno" + (" · " + nota if nota else ""))


TEXTOS = {}
TEXTOS_ = {
    # M1–M2 · Savater (compilación ff2: no está en este entorno ni en Drive)
    "savater": _md("Ética para Amador (fragmento)"),
    # M2 · Vargas Llosa (compilación ff2)
    "vargas": _md("Parábola de la solitaria"),
    # M3 · Rodríguez Monegal
    "monegal": _md("Cien años de soledad: el problema del anacronismo (fragmento)"),
    # M3 · Corrupción política · verificado contra LENGUAJE PTD30.pdf (Drive, preguntas 1 a 6)
    "corrupcion": dict(
        titulo="CORRUPCIÓN POLÍTICA",
        parrafos=[
            "Corrupción política, en términos generales, es el mal uso público (gubernamental) del poder "
            "para conseguir una ventaja ilegítima, generalmente secreta y privada. El término opuesto a "
            "corrupción política es transparencia. Por esta razón se puede hablar del nivel de corrupción o "
            "de transparencia de un Estado.",
            "Sayed y Bruce (1998) definen la corrupción como “el mal uso o el abuso del poder público para "
            "beneficio personal y privado”, entendiendo que este fenómeno no se limita a los funcionarios "
            "públicos. También se define como “el conjunto de actitudes y actividades mediante las cuales "
            "una persona transgrede compromisos adquiridos consigo mismo, utilizando los privilegios "
            "otorgados con el objetivo de obtener un beneficio ajeno al bien común”. Las formas de "
            "corrupción varían, pero las más comunes son el uso ilegítimo de información privilegiada, el "
            "tráfico de influencias, los sobornos, las extorsiones, los fraudes y el nepotismo.",
            "La corrupción no es específica de los países pobres, en desarrollo o en transición. En los "
            "países desarrollados hay casos frecuentes de corrupción en todos los campos posibles: "
            "desembolsos “debajo de la mesa” efectuados a cirujanos prestigiosos por pacientes con la "
            "intención de que se les adelante su posición en las listas de espera; contribuciones pagadas "
            "por personas ricas al “fondo social y cultural” de una universidad prestigiosa a cambio de la "
            "aceptación de sus hijos como alumnos; sobornos pagados para obtener diplomas, ventajas "
            "financieras y de otro tipo, etc.",
            "La corrupción también contribuye a la destrucción medioambiental. Los países corruptos pueden "
            "tener formalmente una legislación destinada a proteger el ambiente, pero no puede ser "
            "ejecutada si los encargados de que se cumpla son fácilmente sobornados. Lo mismo puede "
            "aplicarse para los derechos sociales, la protección laboral, la prevención del trabajo "
            "infantil, e incluso la seguridad alimentaria. Frente a la última, el economista y ganador del "
            "Premio Nobel Amartya Sen ha observado que “no existe nada que pueda llamarse problema "
            "apolítico de alimentos”. De acuerdo con este argumento, es la acción o inacción del gobierno "
            "lo que determina su severidad.",
            "Por ejemplo, en Bihar (India), más del 80% de la ayuda alimentaria subsidiaria a los pobres es "
            "robada por funcionarios públicos corruptos (Forbes, 2007).",
            "En suma, es posible afirmar que la corrupción política es una realidad mundial. Su nivel de "
            "tolerancia o de combate evidencia la madurez política de cada país. Por esta misma razón "
            "existen entidades nacionales e internacionales, oficiales y privadas con la misión de "
            "supervisar y controlar la corrupción política, como es el caso de la Organización de las "
            "Naciones Unidas, la Organización de los Estados Americanos y Transparencia Internacional.",
        ],
        pie="Tomado y adaptado de: Wikipedia, entrada “Corrupción Política”",
        verificado=True,
        fuente="LENGUAJE PTD30.pdf (Drive), texto de las preguntas 1 a 6 (la 1 y la 3 son las del cuaderno)"),
    # M4 · Cortázar (el .md trae un solo párrafo; la pregunta habla del «segundo párrafo»)
    "cortazar": _md("Del cuento breve y sus alrededores (fragmento)",
                    nota="INCOMPLETO: la pregunta dice «en el segundo párrafo» y el .md trae solo ese"),
    # M4 · Los fantasmas del Facebook · verificado contra LENGUAJE PTD34.pdf (Drive, preguntas 8 a 10)
    "facebook": dict(
        titulo="",
        parrafos=[
            "Jesica Migliavacca va con una amiga en el auto de su amigo Oscar Avendaño. Son casi las seis de "
            "la mañana cuando llegan a la esquina de Belgrano y Lamadrid [dos calles de Buenos Aires, "
            "Argentina] y por la ventana ven a un tipo con un BMW blanco hablando con el de un furgón de "
            "reparto de una panadería. Parecen intercambiar documentación después de haber chocado. El que "
            "maneja el BMW le dice algo a una de las chicas, quizás a Jesica, o tal vez a la amiga, no queda "
            "claro. Lo que se sabe es que Avendaño, probablemente molesto por el comentario, baja del auto, "
            "saca del baúl una escopeta 12.70 y forcejea con el conductor del BMW. Jesica espera en el auto. "
            "De la 12.70 sale un tiro. La bala entra en el ojo derecho de Jesica. Ese día los medios "
            "ilustraron la información con una foto de ella, tomada de su Facebook. En la imagen se la ve en "
            "una situación similar a la del momento de su muerte: Por la noche, dentro de un auto y con "
            "amigos.",
            "En su último cumpleaños, de sus 333 amigos en la red social, sólo once le desearon feliz "
            "cumpleaños.",
            "No sé si hago bien en escribirte por acá, porque soy de los que hablan solos o con ángeles. Uno "
            "sos vos. Quiero decirte que es muy fuerte ver tus fotos. No puedo imaginarme que sos vos. Y "
            "también es muy fuerte sentir que estás ahí mirando y riéndote de todo. Te quiero mucho.",
            "El internauta parece incómodo. Como si el dolor y la tristeza no encajaran en este espacio que "
            "todo el tiempo propone diversión y recreación. Uno de los grandes dilemas de la empresa "
            "Facebook: la imagen de perfil de los muertos permanece vital y fresca, aunque de manera "
            "ilusoria y muchas veces dolorosa para los seres queridos. En ocasiones esta estampa de la "
            "persona fallecida es descrita como “perturbadora”, “espeluznante” o “macabra”, tanto para "
            "dolientes como para otros usuarios que circunstancialmente se topan con esos perfiles cuando "
            "la plataforma sugiere amigos o recuerda cumpleaños.",
            "Para la red, morir no es necesariamente un problema. Las cuentas no se cierran por inactividad "
            "como ocurre con los mails. Los perfiles de los muertos permanecen abiertos y tan disponibles "
            "como su propietario haya determinado en vida. Solo aquel que tenga la contraseña, puede "
            "acceder, publicar o darlo de baja como si fuese el usuario original. En la mayoría de los "
            "casos, el perfil permanece tal como la persona lo dejó.",
            "La compañía creada por Mark Zuckerberg estima que en Argentina más de 500.000 usuarios de su "
            "red social (de un total de 20 millones en el país) tienen 65 años o más y la edad promedio "
            "ronda los 40 años. Si se tiene en cuenta la esperanza de vida nacional, en una década esos "
            "usuarios podrían estar muertos. Habría, en ese caso, medio millón de perfiles flotando en la "
            "web. Fantasmas virtuales, o como quieran llamarlos.",
        ],
        pie="Tomado de Moya, M. y Ennis, V. (2013, agosto). Los fantasmas del Facebook. Revista Anfibia. "
            "Recuperado de http://www.revistaanfibia.com/cronica/los-fantasmas-del-facebook/",
        verificado=True,
        fuente="LENGUAJE PTD34.pdf (Drive), texto de las preguntas 8 a 10 (la 10 es la del cuaderno)"),
    # M4 · Límites planetarios
    "tierra": _md("La Tierra sobrepasa sus límites planetarios (fragmento)"),
    # M5
    "schekman": _md("Por qué revistas como Nature, Science y Cell hacen daño a la ciencia (fragmento)"),
    "giraldo": _md("El llanto de un hombre (fragmento)"),
    "stornelli": _md("Los marginados digitales (fragmento)"),
    "paz": _md("El laberinto de la soledad (fragmento)"),
    # M1 · Gómez Jattin · ASED, preguntas 11 y 12. Las palabras, verificadas contra el texto del
    # compilado; los renglones, los del cuaderno entregado (la pregunta 11 del ASED habla de los
    # renglones que empiezan con «de», y coinciden).
    "jattin": dict(
        titulo="SI SE QUIERE LLEGAR A SER UNA BUENA VÍCTIMA",
        versos=[["Es necesario saber de toda la dulzura", "que entrelaza al verdugo con la muerte",
                 "de la paciencia con que afila su hacha", "de la soledad que ilumina su vida",
                 "y la de sus inocentes hijos", "del esfuerzo que implica portar y levantar el arma",
                 "de la sangre que pringa sus pantalones.", "Todas esas consideraciones deben estar presentes",
                 "en el momento de recoger nuestro pelo sobre la nuca", "y poner en sus manos el pescuezo."]],
        pie="Raúl Gómez Jattin, Antología poética, FICA. ed. Tiempo presente, Bogotá, 1991",
        verificado=True,
        fuente="ASED pre código 11 (Drive; texto del compilado), preguntas 11 y 12 · renglones del cuaderno "
               "entregado"),
    # M6 · ASED (verificado contra el texto del compilado: preguntas 35 a 38)
    "dresel": dict(
        titulo="",
        parrafos=["“Una de las razones para catalogar a algunas personas de inmaduras es que no son capaces de "
                  "afrontar una derrota, una tragedia, o cualquier otra desavenencia. Generalmente tales "
                  "personas no pueden soportar un desenlace fatal, ni siquiera un drama de experiencias "
                  "simbólicas. Por eso se han difundido tanto en la literatura popular los finales "
                  "agradables, de tal manera que un desenlace saturado de escenas desagradables, al final son "
                  "arreglados de tal modo que la acción varíe favorablemente. Las personas inmaduras "
                  "necesitan constantemente que se les demuestre que todas las cosas acabarán bien.”"],
        pie="El espejo del alma · Walter Dresel",
        verificado=True,
        fuente="ASED pre código 11 (Drive; texto del compilado), preguntas 35 a 38 de Lectura Crítica"),
    # M6 · Kavafis · ASED, preguntas 30 a 34. El texto extraído del compilado no conserva los saltos de
    # verso: se corta un renglón por pregunta y por respuesta, en el orden y con las palabras del ASED.
    "kavafis": dict(
        titulo="ESPERANDO A LOS BÁRBAROS",
        versos=[
            ["¿A qué esperamos, reunidos en el foro?", "A los bárbaros que deben llegar hoy."],
            ["¿Por qué no ocurre nada en el senado?", "¿Por qué los senadores están sentados sin legislar?",
             "Porque hoy llegan los bárbaros.", "¿Qué leyes van a dictar los senadores?",
             "Los bárbaros cuando lleguen, harán las leyes."],
            ["¿Por qué se ha levantado tan temprano nuestro emperador?",
             "¿Y por qué está sentado en el trono en la puerta de la ciudad, solemne y con corona?",
             "Porque hoy llegan los bárbaros y el emperador espera recibir a su jefe.",
             "Incluso tiene un pergamino que darle, repleto de títulos, con nombres imponentes."],
            ["¿Por qué salen nuestros dos cónsules y pretores vistiendo sus togas púrpuras, bordadas?",
             "¿Por qué se han puesto pulseras con tantas amatistas, y anillos con magníficas, brillantes "
             "esmeraldas?",
             "¿Por qué hoy salen con elegantes varas hermosamente trabajadas en oro y plata?",
             "Porque hoy llegan los bárbaros y las cosas como estas los deslumbran"],
            ["¿Por qué no vienen nuestros distinguidos oradores de costumbre a hacer discursos, a decir lo "
             "que tengan que decir?",
             "Porque hoy llegan los bárbaros y les aburre la retórica y las arengas"],
            ["¿Por qué esta repentina perplejidad, esta confusión? (qué serias se han vuelto las caras de la "
             "gente)",
             "¿Por qué rápidamente se vacían las calles y las plazas y todos regresan a sus casas absortos "
             "en meditación?",
             "Porque ha caído la noche y los bárbaros no han llegado y algunos de nuestros hombres vinieron "
             "desde la frontera a decir que ya no hay bárbaros."],
            ["¿Y ahora qué va a ser de nosotros sin los bárbaros?", "Aquellas gentes eran una especie de solución."],
        ],
        pie="Modificado de: Kostantin Kavafis, Obras escogidas, Edicomunicación, Barcelona, España, 1995",
        verificado=True,
        fuente="ASED pre código 11 (Drive; texto del compilado), preguntas 30 a 34 · los saltos de verso se "
               "reconstruyeron por oración (la extracción no los trae) · «magnificas» del ASED va con tilde"),
}


for _k, _v in TEXTOS_.items():
    _v["clave"] = _k
    TEXTOS[_k] = _v


# ───────── cada hoja: qué texto, dónde y qué se recorta ─────────
# texto: (clave, dónde) con dónde ∈ "arriba" (compartido, a lo ancho), "antes2" (a lo ancho, antes de
# la tarjeta 2), "t1"/"t2" (dentro de la tarjeta). corte: modo por tarjeta (drop / caja / nada).
HOJAS = {
    "lc1_i1": dict(textos=[("savater", "arriba")], corte=("drop", "drop"), preguntas="preguntas 1 y 2"),
    "lc1_i2": dict(textos=[("savater", "arriba"), ("jattin", "t2")], corte=("caja", "drop"),
                   preguntas="pregunta 3"),
    "lc2_i1": dict(textos=[("savater", "arriba")], corte=("caja", "caja"), preguntas="preguntas 1 y 2"),
    "lc2_i2": dict(textos=[("vargas", "arriba")], corte=("drop", "caja"), preguntas="preguntas 3 y 4"),
    "lc3_i1": dict(textos=[("monegal", "t1")], corte=("drop", "nada"), preguntas=""),
    "lc3_i2": dict(textos=[("corrupcion", "arriba")], corte=("drop", "drop"), preguntas="preguntas 3 y 4"),
    "lc4_i1": dict(textos=[("cortazar", "t1"), ("facebook", "antes2")], corte=("drop", "caja"),
                   preguntas="pregunta 2"),
    "lc4_i2": dict(textos=[("tierra", "arriba")], corte=("drop", "drop"), preguntas="preguntas 3 y 4"),
    "lc5_i1": dict(textos=[("schekman", "t1"), ("giraldo", "t2")], corte=("drop", "drop"), preguntas=""),
    "lc5_i2": dict(textos=[("stornelli", "t1"), ("paz", "t2")], corte=("drop", "drop"), preguntas=""),
    "lc6_i1": dict(textos=[("dresel", "arriba")], corte=("drop", "drop"), preguntas="preguntas 1 y 2"),
    "lc6_i2": dict(textos=[("kavafis", "antes2")], corte=("nada", "drop"), preguntas="pregunta 4"),
}


# ───────── composición del texto en dos columnas ─────────
def _renglones(txt, size, width):
    """[(palabras, último del párrafo)] medidos con la fuente real (lib.wrap_px)."""
    ls = wrap_px(txt, size, width)
    return [(w, i == len(ls) - 1) for i, w in enumerate(ls)]


def _linea_svg(x, y, palabras, ultimo, size, width, color=INK):
    if ultimo or len(palabras) == 1:
        return T(x, y + size, [" ".join(palabras)], size, color)
    ws = [tw(p, size) for p in palabras]
    gap = (width - sum(ws)) / (len(palabras) - 1)
    xs, cx = [], x
    for ww in ws:
        xs.append(cx); cx += ww + gap
    tsp = "".join(f'<tspan x="{px:.1f}">{esc(p)}</tspan>' for px, p in zip(xs, palabras))
    return (f'<text y="{y + size}" font-family="{UI}" font-size="{size}" font-weight="400" '
            f'fill="{color}" font-style="normal" opacity="1">{tsp}</text>')


def _items(tx, size, colw):
    """Lista de renglones del texto: ('l', palabras, último, sangría) o ('p',) = espacio de párrafo."""
    items = []
    if "versos" in tx:
        sang = 30
        for k, estrofa in enumerate(tx["versos"]):
            if k:
                items.append(("p",))
            for v in estrofa:
                for j, (w, ult) in enumerate(_renglones(v, size, colw - sang)):
                    items.append(("l", w, True, sang if j else 0))   # verso: sin justificar
    else:
        for k, p in enumerate(tx["parrafos"]):
            if k:
                items.append(("p",))
            for w, ult in _renglones(p, size, colw):
                items.append(("l", w, ult, 0))
    return items


def _columnas(items, ncol, lh, pgap, solo_estrofas=False):
    """Reparte los renglones en ncol columnas de alto parejo. Devuelve (columnas, alto). Un poema
    solo se corta entre estrofas."""
    alto = lambda its: sum(lh if i[0] == "l" else pgap for i in its)
    if ncol == 1:
        return [items], alto(items)
    total = alto(items)
    mejor = None
    for corte in range(1, len(items)):
        if solo_estrofas and items[corte][0] != "p":
            continue
        a, b = items[:corte], items[corte:]
        while a and a[-1][0] == "p":
            a = a[:-1]
        while b and b[0][0] == "p":
            b = b[1:]
        h = max(alto(a), alto(b))
        if mejor is None or h < mejor[0]:
            mejor = (h, a, b)
    if mejor is None:                       # un poema de una sola estrofa: una columna
        return [items], total
    return [mejor[1], mejor[2]], mejor[0]


def bloque_texto(tx, x, w, size, ncol=2, dibujar=None, etiqueta=""):
    """Mide (y, si se da `dibujar`=(b, y), dibuja) el texto completo. Devuelve el alto."""
    lh = round(size * 1.36, 1)
    pgap = round(size * 0.55, 1)
    pad = 26
    gut = 44
    colw = (w - 2 * pad - (ncol - 1) * gut) / ncol
    items = _items(tx, size, colw)
    cols, h_txt = _columnas(items, ncol, lh, pgap, solo_estrofas="versos" in tx)
    h_eti = 30 if etiqueta else 0
    h_tit = round(size * 1.25 + 12) if tx["titulo"] else 0
    pie_ls = wrap_px(tx["pie"], 16, w - 2 * pad, style="italic") if tx["pie"] else []
    h_pie = 12 + 22 * len(pie_ls) if pie_ls else 0
    alto = pad - 6 + h_eti + h_tit + h_txt + h_pie + pad - 8
    if dibujar is None:
        return alto
    b, y = dibujar
    c = A["color"]
    b.append(BT.wob_rect(x, y, w, alto, BT.LN_GRIS, 2.2, fill="white", seed=int(y) % 97 + 3, amp=1.0))
    b.append(rect(x + 6, y + 14, 7, alto - 28, c, r=3))            # acento vertical (regla 1)
    yy = y + pad - 6
    if etiqueta:
        b.append(BT.TX(x + pad, yy + 16, etiqueta, 14, c, BT.MONO, "700"))
        yy += h_eti
    if tx["titulo"]:
        b.append(T(x + pad, yy + size * 1.05, [tx["titulo"]], round(size * 1.1, 1), INK, weight="700"))
        yy += h_tit
    ZONAS.append(dict(clave=tx.get("clave"), titulo=(x + pad, yy - h_tit, w - 2 * pad, h_tit),
                      columnas=[(x + pad + k * (colw + gut) - 4, yy - 4, colw + 8, h_txt + 8)
                                for k in range(len(cols))]))
    for k, col in enumerate(cols):
        cx = x + pad + k * (colw + gut)
        cy = yy
        for it in col:
            if it[0] == "p":
                cy += pgap
                continue
            _, palabras, ult, sang = it
            b.append(_linea_svg(cx + sang, cy, palabras, ult, size, colw - sang))
            cy += lh
    yy += h_txt
    if pie_ls:
        yy += 12
        for ln in pie_ls:
            b.append(T(x + pad, yy + 16, [" ".join(ln)], 16, GRAY, style="italic"))
            yy += 22
    return alto


# ───────── lectura de la tarjeta original ─────────
def _lineas(ws, yc):
    from collections import defaultdict
    filas = defaultdict(list)
    for a, b_, c, d, t in ws:
        if rh.CLIP_X0 <= a < rh.CLIP_X1 and yc + 100 <= b_ < yc + 1000:
            filas[round(d / 6)].append((a, b_, d, t))
    out = []
    for _, v in sorted(filas.items()):
        v.sort()
        out.append((min(x[1] for x in v), max(x[2] for x in v), v[0][0], " ".join(t for *_, t in v)))
    return out


def segmentos(ws, yc, modo):
    """Tramos [y0, y1] (coordenadas del original) que se recortan de esa tarjeta."""
    L = _lineas(ws, yc)
    enun = [L[0]]
    for l in L[1:]:                                   # el enunciado puede tener dos renglones
        if l[2] < 120 and l[0] - enun[-1][1] < 12:
            enun.append(l)
        else:
            break
    op_a = next(l for l in L if l[3].startswith("A ") and l[2] < 120)
    notas = [l for l in L if re.match(r"(LO QUE SUBRAY|L O Q U E)", l[3])]
    ultimas = [l for l in L if not notas or l[0] < notas[0][0] - 5]
    fin = ultimas[-1][1] + 30
    medio = [l for l in L if enun[-1][1] < l[0] and l[1] <= op_a[0]]
    prov = [l for l in medio if "proyecta tu profe" in l[3]]
    refs = [l for l in medio if "·" in l[3] and l[2] >= 140 and l[3].count("·") >= 1
            and l is not medio[0]]
    ini = yc + 108
    if modo == "nada":
        return [(ini, fin)]
    corte_fin = (prov[-1][1] if prov else refs[-1][1]) + 8
    if modo == "drop":
        return [(ini, enun[-1][1] + 10), (corte_fin, fin)]
    # «caja»: el recuadro se queda; sale la referencia (y el letrero)
    ref = refs[-1] if not prov else max((l for l in refs if l[1] <= prov[-1][0]), key=lambda l: l[0])
    return [(ini, ref[0] - 6), (corte_fin, fin)]


# ───────── tarjeta ─────────
def _marco(b, y, h):
    b.append(BT.wob_rect(M, y, CW, h, BT.TINTA_B, 3, fill="white", seed=50 + int(y), amp=1.6))


def _encabezado(b, y, est, comp):
    """Como taller_base.encabezado_icfes(), con el sello medido y con más aire (pad 26)."""
    c = A["color"]
    b.append(BT.wob_circle(M + 62, y + 56, 38, c, 2.8, seed=int(y)))
    b.append(tb.boya(M + 62, y + 56, 15, c))
    t1 = "Pregunta para entrenar"
    w1 = BT.twf(t1, 30, BT.SHA, "800")
    b.append(BT.resaltador(M + 118, y + 20, w1, 30, BT.FOSFO_2, seed=int(y) + 3))
    b.append(BT.TX(M + 118, y + 46, t1, 30, BT.TINTA_B, BT.SHA, "800"))
    tb.membrete(b, M + 118, y + 62)
    nombre, ec = EST[est]
    BT.sello(b, M + 1275, y + 26, f"entrena la estrategia {est} · {nombre}", ec, size=19, h=44, pad=26,
             derecha=True)
    if comp:
        b.append(BT.TX(M + 1275, y + 100, f"COMPETENCIA · {comp.upper()}", 14, GRAY, BT.MONO,
                       anchor="end"))
    tb._primera_idea(b, y, M + 1460, "Mi primera idea:")


def _columna_derecha(b, y, h, est):
    """La columna derecha de siempre (taller_base.columna_derecha), más compacta."""
    c = A["color"]
    rx = M + RX_OFF
    rw = W - M - rx - 24
    ry = y + 122
    b.append(BT.wob_vline(rx - 18, ry, y + h - 30, seed=int(y)))
    b.append(BT.TX(rx, ry + 20, "MARCO AL FINAL", 16, BT.TINTA_B, BT.MONO, "700"))
    paso, r = 92, 30
    for k, L_ in enumerate("ABCD"):
        cx = rx + 36 + k * paso
        b.append(BT.wob_circle(cx, ry + 74, r, c, 2.4, seed=k + 60, fill="white"))
        b.append(BT.TX(cx, ry + 74 + 10, L_, 25, c, BT.SHA, "700", anchor="middle"))
    b.append(T(rx, ry + 136, ["¿Qué tan seguro estoy?"], 18, GRAY))
    for k, lab in enumerate(["adiviné", "casi", "seguro"]):
        b.append(BT.wob_rect(rx + k * 150, ry + 154, 22, 22, GRAY, 2, fill="white", seed=k + 70, amp=0.7))
        b.append(T(rx + 30 + k * 150, ry + 172, [lab], 18, GRAY))
    sy = ry + 204
    tb.salvavidas(b, rx, sy, rw, h=282)
    ly = sy + 282 + 46
    cierre = ("¿En qué se parece a lo del taller?", "(el libro y el ICFES preguntan lo mismo de otra forma)")
    b.append(BT.TX(rx, ly, cierre[0], 22, c, BT.SHA, "700"))
    b.append(BT.estrellita(rx + BT.twf(cierre[0], 22, BT.SHA, "700") + 22, ly - 8, 10, EDU_ORO, 2.2))
    b.append(T(rx, ly + 26, [cierre[1]], 16, GRAY, style="italic"))
    n = max(1, int((y + h - 84 - (ly + 70)) // 46) + 1)
    b.append(wlines(rx, ly + 70, rw - 70, n, c="#E3E8EF", step=46))
    tb.marca_est(b, W - M - 60, y + h - 50, est)


def _recorte_seg(b, pag, cid, y0, y1, y_dest, k, limite, n):
    """Un tramo del original, movido a y_dest y escalado k (anclado a la izquierda)."""
    x0, x1 = rh.CLIP_X0, rh.CLIP_X1
    dy = y_dest - y0                       # sin escala, el tramo empezaría en y_dest
    tx, ty = x0 * (1 - k), y_dest * (1 - k)
    b.append(f'<g class="instrumento" data-n="{n}" data-ymax="{limite:.0f}" data-xmax="{X_MAX}" '
             f'data-k="{k:.4f}"><g transform="translate({tx:.2f} {ty:.2f}) scale({k:.4f})">'
             f'<clipPath id="{cid}"><rect x="{x0}" y="{y0:.1f}" width="{x1 - x0}" height="{y1 - y0:.1f}"/>'
             f'</clipPath><g transform="translate(0 {dy:.1f})"><g clip-path="url(#{cid})">'
             f'<use xlink:href="#orig{pag}"/></g></g>'
             f'<rect x="{x0}" y="{y0 + dy:.1f}" width="{x1 - x0}" height="{y1 - y0:.1f}" fill="none"/>'
             f'</g></g>')
    return y_dest + k * (y1 - y0)


# ───────── la hoja ─────────
GAP_SEG = 12


def _plan(cfg, segs, size, kcap):
    """Alturas de cada bloque con letra `size` y escala máxima `kcap`. Devuelve (bloques, total)."""
    x_ancho, w_ancho = M, CW
    bloques = []
    def card(i):
        intx = [t for t, d in cfg["textos"] if d == f"t{i + 1}"]
        h_txt = bloque_texto(TEXTOS[intx[0]], M + 24, IW - 8, size) + 16 if intx else 0
        s_alto = sum(y1 - y0 for y0, y1 in segs[i]) + GAP_SEG * (len(segs[i]) - 1)
        fijo = HEAD + h_txt + 24
        k = 1.0
        if fijo + s_alto > RIGHT_MIN:
            k = max(kcap, min(1.0, (RIGHT_MIN - fijo) / s_alto))
        h = max(RIGHT_MIN, fijo + k * s_alto + 26)
        return ["tarjeta", i, h, k, intx[0] if intx else None]
    arriba = [t for t, d in cfg["textos"] if d == "arriba"]
    antes2 = [t for t, d in cfg["textos"] if d == "antes2"]
    eti = lambda: f"LEE PRIMERO EL TEXTO COMPLETO{' · ' + cfg['preguntas'] if cfg['preguntas'] else ''}"
    if arriba:
        bloques.append(("texto", arriba[0], bloque_texto(TEXTOS[arriba[0]], x_ancho, w_ancho, size,
                                                         etiqueta=eti()), eti()))
    bloques.append(card(0))
    if antes2:
        bloques.append(("texto", antes2[0], bloque_texto(TEXTOS[antes2[0]], x_ancho, w_ancho, size,
                                                         etiqueta=eti()), eti()))
    bloques.append(card(1))
    total = sum(bl[2] for bl in bloques) + GAP_B * (len(bloques) - 1)
    return bloques, total


PREFERENCIA = [(20, 1.0), (20, .95), (20, .9), (20, .85), (19, .9), (19, .85), (20, .8), (19, .8),
               (18, .85), (20, .75), (19, .75), (18, .8), (18, .75)]
INFORME = {}
ZONAS = []          # dónde quedó cada columna de texto (para comparar con pdftotext)


def rehacer_lc(pag, svg_nombre, pag_nueva):
    cfg = HOJAS[svg_nombre]
    mis = int(svg_nombre[2])
    nombre_area, color = rh.AREAS["lc"]
    ws = rh._palabras(pag)
    import subprocess, tempfile
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(["pdftoppm", "-f", str(pag), "-l", str(pag), "-r", "100", "-png", "-singlefile",
                        rh.PDF, os.path.join(tmp, "p")], check=True)
        png = os.path.join(tmp, "p.png")
        infos = [dict(rh._icfes(ws, png, y, 1010), y_card=y) for y in (210, 1260)]
    sub = rh._lineas(ws, M + 220, W - M - 660, 90, 125)
    tema, _, comp = (sub[0] if sub else "").partition(" · componente ")
    linea3 = " ".join(rh._lineas(ws, M + 220, W - M - 660, 125, 165))
    configurar(nombre_area, mis, comp, tema=tema, color=color)
    usar_estrategias({i["est"]: (i["est_nombre"], i["color"]) for i in infos})
    segs = [segmentos(ws, yc, modo) for yc, modo in zip((210, 1260), cfg["corte"])]

    del ZONAS[:]
    disponible = Y_FIN - Y0
    for size, kcap in PREFERENCIA:
        bloques, total = _plan(cfg, segs, size, kcap)
        if total <= disponible:
            break
    else:
        raise RuntimeError(f"{svg_nombre}: no cabe ni con letra 18 y escala {K_MIN} "
                           f"({total:.0f} de {disponible})")
    vocab = Y0 + total + 24 <= tb.VOCAB_Y
    # lo que sobra se reparte entre las tarjetas (más renglones para escribir), hasta 120 c/u
    sobra = (tb.VOCAB_Y - 24 if vocab else Y_FIN) - (Y0 + total)
    tarjetas = [bl for bl in bloques if bl[0] == "tarjeta"]
    extra = min(120, max(0, sobra) / len(tarjetas))
    for bl in tarjetas:
        bl[2] += extra
    b = tb.hoja_nueva()
    cabecera(b, rh.cabecera_icfes(linea3))
    y = Y0
    ks = []
    for bl in bloques:
        if bl[0] == "texto":
            bloque_texto(TEXTOS[bl[1]], M, CW, size, dibujar=(b, y), etiqueta=bl[3])
        else:
            _, i, h, k, intx = bl
            info = infos[i]
            _marco(b, y, h)
            _encabezado(b, y, info["est"], info["comp"])
            yy = y + HEAD
            if intx:
                yy += bloque_texto(TEXTOS[intx], M + 24, IW - 8, size, dibujar=(b, yy),
                                   etiqueta="LEE PRIMERO EL TEXTO COMPLETO") + 16
            for j, (y0, y1) in enumerate(segs[i]):
                yy = _recorte_seg(b, pag, f"c{pag}-i{i + 1}-{j}", y0, y1, yy, k, y + h - 8,
                                  f"icfes-{i + 1}") + GAP_SEG * k
            _columna_derecha(b, y, h, info["est"])
            ks.append(k)
        y += bl[2] + GAP_B
    if vocab:
        franja_vocab(b)
    tb.footer(b, pag_nueva, color, texto=f"{nombre_area} · Misión {mis} · Entrenamiento ICFES")
    ruta = OUT + svg_nombre + ".svg"
    svg_close(b, ruta)
    s = open(ruta, encoding="utf-8").read()
    s = s.replace("<defs>", "<defs>" + rh._svg_original(pag), 1)
    open(ruta, "w", encoding="utf-8").write(s)
    INFORME[svg_nombre] = dict(pagina=pag_nueva, letra=size, k=ks, franja=vocab,
                               alto=round(total), textos=[t for t, _ in cfg["textos"]],
                               zonas=[dict(z) for z in ZONAS])
    return ruta, infos


if __name__ == "__main__":
    import sys, json
    for pag, nueva, nombre in rh.hojas():
        if nombre in HOJAS and (len(sys.argv) == 1 or str(nueva) in sys.argv[1:]):
            rehacer_lc(pag, nombre, nueva)
            print(nombre, json.dumps(INFORME[nombre], ensure_ascii=False))
