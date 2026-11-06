#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MISIÓN 1 · MATEMÁTICAS — contenidos y armado de todas las hojas."""
from hojas import *
import hojas as HJ

PAG = "280"

# ══════════ LAS 10 PREGUNTAS DEL LIBRO ══════════
# (enunciado NO va: vive en el libro. Aquí solo el andamiaje.)
PREGUNTAS = [
 # ── Hoja A ──
 dict(n=1, grid=380, piensa=[
      "¿Los valores solo suben, o suben y en algún momento bajan?",
      "¿A qué hora está la temperatura más alta? ¿Qué pasa después?",
      "La gráfica correcta tiene que mostrar ese mismo cambio de dirección."],
      pasos=["Leo la fila de temperaturas y anoto cómo cambia.",
             "Marco la hora donde deja de subir: ahí está el pico.",
             "Busco la gráfica que suba hasta un pico y después baje."],
      rel=dict(grid=["4  6  8  10   9  7  5", "+2 +2 +2   −1 −2 −2",
                     "sube hasta las 9:00 (10°)", "y de ahí se devuelve"],
               resp="B", nota="(sube y luego baja)", mood=0,
               sv=("que no solo subía: a las 9 empezó a bajar", "B", "A y D"))),
 dict(n=2, grid=320, qr=True, piensa=[
      "¿La velocidad cambia en algún momento, o se mantiene igual?",
      "Si cada segundo avanza lo mismo, ¿qué operación los relaciona?"],
      pasos=["Identifico el dato constante: 5 metros cada segundo.",
             "Multiplico ese valor por los 8 segundos.",
             "Reviso que la justificación de la opción diga lo mismo."],
      rel=dict(grid=["5 m cada segundo", "1s = 5   2s = 10   4s = 20", "5 × 8 = 40 m"],
               resp="B", nota="= 40 metros", mood=1,
               sv=("que la velocidad no cambiaba nunca", "B", "la C"))),
 # ── Hoja B ──
 dict(n=3, grid=380, piensa=[
      "El 46,5 % es una parte de un total. ¿De cuál total?",
      "¿Qué operación convierte un porcentaje en cantidad de personas?",
      "Cuidado: una cosa es el porcentaje y otra el número de personas."],
      pasos=["Escribo el porcentaje como decimal: 46,5 % = 0,465.",
             "Lo multiplico por el total de hombres encuestados (Th).",
             "Verifico que la expresión escogida haga exactamente eso."],
      rel=dict(grid=["46,5 % → 0,465", "H = 0,465 × Th", "es multiplicar, no dividir"],
               resp="A", nota="", mood=0,
               sv=("que un % se multiplica, no se suma", "A", "la C"))),
 dict(n=4, grid=320, qr=True, piensa=[
      "Son 800 personas, pero divididas en dos grupos de 400.",
      "Cada grupo tiene su propio porcentaje. ¿Puedo usar uno solo?"],
      pasos=["Calculo el 46,5 % de los 400 hombres.",
             "Calculo el 35,2 % de las 400 mujeres.",
             "Sumo los dos resultados."],
      rel=dict(grid=["400 × 0,465 = 186", "400 × 0,352 = 140,8", "186 + 141 ≈ 327"],
               resp="B", nota="≈ 327", mood=1,
               sv=("que eran dos grupos distintos, no uno", "B", "la A"))),
 # ── Hoja C ──
 dict(n=5, grid=380, piensa=[
      "¿El aumento de cada mes es siempre la misma cantidad de pesos?",
      "De 1.000.000 a 1.020.000 subió 20.000. ¿Y del segundo al tercero?",
      "Si el aumento crece, el interés se calcula sobre un saldo mayor."],
      pasos=["Resto cada mes con el anterior y anoto los aumentos.",
             "Comparo esos aumentos entre sí: ¿iguales o crecientes?",
             "Elijo la opción que describa ese comportamiento."],
      rel=dict(grid=["1.020.000 − 1.000.000 = 20.000", "1.040.400 − 1.020.000 = 20.400",
                     "sube cada vez más → no es lineal"],
               resp="A", nota="(exponencial)", mood=0,
               sv=("que el aumento no era siempre igual", "A", "la B"))),
 dict(n=6, grid=320, qr=True, piensa=[
      "El 2 % se aplica cada mes sobre lo que haya acumulado.",
      "¿Puedo multiplicar 20.000 × 6, o el aumento va creciendo?"],
      pasos=["Reconozco que cada mes multiplico por 1,02.",
             "Avanzo del mes 3 al mes 6 aplicando ese factor.",
             "Comparo con las opciones y escojo la más cercana."],
      rel=dict(grid=["mes 3 = 1.061.208", "× 1,02 tres veces más", "≈ 1.126.000"],
               resp="C", nota="", mood=1,
               sv=("que crecía cada vez más, no de a 20.000", "C", "la A"))),
 # ── Hoja D ──
 dict(n=7, grid=380, piensa=[
      "Mira otra vez los aumentos: 20.000, luego 20.400, luego 20.808.",
      "¿Esa diferencia se mantiene, se achica o se agranda?",
      "La tasa es fija (2 %), pero el saldo sobre el que se aplica no lo es."],
      pasos=["Calculo las diferencias entre meses consecutivos.",
             "Observo si esas diferencias crecen.",
             "Escojo la afirmación que explique por qué crecen."],
      rel=dict(grid=["20.000 → 20.400 → 20.808", "cada vez un poquito más",
                     "porque el 2 % se aplica al total"],
               resp="D", nota="", mood=0,
               sv=("que el aumento se iba agrandando", "D", "la A"))),
 dict(n=8, grid=320, qr=True, piensa=[
      "¿El interés se suma una sola vez al final, o mes a mes?",
      "Multiplicar por 1,02 doce veces no es lo mismo que sumar 2 % × 12."],
      pasos=["Descarto las que suman el interés una sola vez.",
             "Busco la que multiplica repetidamente por 1,02.",
             "Confirmo que el exponente sea el número de meses."],
      rel=dict(grid=["12 meses seguidos", "× 1,02 doce veces", "V = 1.000.000 × (1,02)¹²"],
               resp="B", nota="", mood=1,
               sv=("que el interés se aplicaba cada mes", "B", "la A"))),
 # ── Hoja E ──
 dict(n=9, grid=380, piensa=[
      "La gráfica no es una línea: sube, baja y vuelve a subir.",
      "¿El consumo del final del mes es mayor o menor que el del inicio?",
      "Ojo con las opciones que hablan de 'siempre' o 'nunca'."],
      pasos=["Recorro la gráfica de izquierda a derecha por tramos.",
             "Comparo la primera mitad del mes con la segunda.",
             "Descarto las opciones que contradigan lo que veo."],
      rel=dict(grid=["empieza en 2, baja a 1", "y al final sube hasta 6",
                     "el final gasta más que el inicio"],
               resp="A", nota="", mood=1,
               sv=("que al final del mes el consumo se dispara", "A", "la C"))),
 dict(n=10, grid=320, qr=True, piensa=[
      "Si el eje horizontal es tiempo, el área bajo la curva es consumo total.",
      "¿En qué tramo la curva está más alta durante más tiempo?"],
      pasos=["Divido el mes en dos mitades: días 5-15 y días 15-25.",
             "Estimo en cuál la curva encierra más área.",
             "Escojo la afirmación coherente con esa comparación."],
      rel=dict(grid=["1ra mitad: valores bajos", "2da mitad: sube a 4, 5, 6",
                     "los últimos días pesan más"],
               resp="C", nota="", mood=1,
               sv=("que al final la curva estaba mucho más alta", "C", "la A"))),
]

# ══════════ LAS 4 ESTRATEGIAS ══════════
ESTRATEGIAS = {
 1: dict(nombre="Leer el cambio", sub="del dato a la forma: tabla ↔ gráfica ↔ enunciado",
         movs=[("Ubico los ejes", "qué magnitud va en cada uno y en qué unidades."),
               ("Sigo la línea", "¿sube, baja o cambia de dirección? ¿en qué punto?"),
               ("Leo el tramo exacto", "la afirmación habla de un intervalo: reviso ESE, no toda la gráfica.")],
         campos=[("Ejes", "¿qué va en el horizontal y qué en el vertical?"),
                 ("Forma de la línea", "¿sube, baja, cambia de dirección?"),
                 ("Tramo que revisé", "el intervalo exacto del que habla la opción"),
                 ("Descarto", "¿cuál opción se cae apenas miro la gráfica, y por qué?")],
         bitacora="¿en qué se parecieron estas dos preguntas del ICFES a la de tu misión?",
         bit_resp="en las tres tocaba mirar un tramo, no toda la gráfica"),
 2: dict(nombre="La razón constante", sub="cuando cada paso suma o multiplica siempre lo mismo",
         movs=[("Busco el dato fijo", "el valor que no cambia: por cada, cada vez, por unidad."),
               ("Separo base y aumento", "¿hay un punto de partida más algo que se repite?"),
               ("Escribo la operación", "primero multiplico lo que se repite, después sumo la base.")],
         campos=[("Dato fijo", "¿qué valor se repite siempre igual?"),
                 ("Base de partida", "¿hay algo que ya está desde el comienzo?"),
                 ("Mi operación", "cómo quedaría escrita"),
                 ("Descarto", "¿cuál opción invierte el orden de las operaciones?")],
         bitacora="¿cómo reconociste cuál era el dato que se repetía siempre igual?",
         bit_resp="porque decía 'por cada', ahí está el valor fijo"),
 3: dict(nombre="El crecimiento que se acumula", sub="distinguir lo que suma siempre igual de lo que se multiplica",
         movs=[("Comparo dos pasos seguidos", "¿la diferencia entre ellos se mantiene o crece?"),
               ("Decido el modelo", "diferencia fija → se suma. Diferencia creciente → se multiplica."),
               ("Verifico hacia atrás", "aplico el modelo a un dato que ya conozco y debe cuadrar.")],
         campos=[("Dos pasos seguidos", "¿cuánto cambió de uno al otro?"),
                 ("¿Suma o multiplica?", "la diferencia, ¿se mantiene o crece?"),
                 ("Mi comprobación", "lo aplico a un dato conocido"),
                 ("Descarto", "¿cuál opción trata un crecimiento compuesto como si fuera fijo?")],
         bitacora="¿qué pista te dijo que el crecimiento NO era de a la misma cantidad?",
         bit_resp="que la diferencia entre meses se iba agrandando"),
 4: dict(nombre="Juzgar la afirmación", sub="decidir si una conclusión se sostiene con los datos",
         movs=[("Aíslo lo que se afirma", "subrayo exactamente qué dice: ¿siempre? ¿todos? ¿mayor?"),
               ("Busco un contraejemplo", "me basta UN punto donde no se cumpla para tumbarla."),
               ("Reviso la razón, no solo el sí/no", "la opción correcta acierta en el veredicto Y en el porqué.")],
         campos=[("Qué se afirma", "la frase exacta, con sus palabras absolutas"),
                 ("Contraejemplo", "¿hay algún punto donde no se cumple?"),
                 ("Mi veredicto", "verdadera o falsa, y por qué"),
                 ("Descarto", "¿cuál opción acierta el sí/no pero da una razón equivocada?")],
         bitacora="¿por qué no basta con responder 'sí' o 'no' sin mirar la justificación?",
         bit_resp="porque dos opciones dicen lo mismo pero una explica mal"),
}

CAMPOS = {k: v["campos"] for k, v in ESTRATEGIAS.items()}


# ══════════ TABLA DE ROSENDO (pregunta ICFES sin imagen) ══════════
def tabla_rosendo(x, y, w):
    g = []; cols = [120, 240, 300, 240, 240]; th = 46
    filas = [("Mes", "Saldo a la fecha", "Interés (10 %)", "Aporte", "Valor de la cuota"),
             ("1", "$200.000", "$20.000", "$40.000", "$60.000"),
             ("2", "$160.000", "$16.000", "$40.000", "$56.000"),
             ("3", "$120.000", "", "$40.000", ""),
             ("4", "$80.000", "", "$40.000", ""),
             ("5", "$40.000", "", "$40.000", "")]
    tw = sum(cols)
    g.append(rect(x, y, tw, th * len(filas), "white", r=8, stroke="#C9D2DC", sw=1.8))
    for r, fila in enumerate(filas):
        yy = y + r * th
        if r == 0: g.append(rect(x, yy, tw, th, "#EDF3F8", r=8))
        elif r % 2 == 0: g.append(rect(x, yy, tw, th, "#FAFCFD", r=0))
        cx = x
        for c, val in enumerate(fila):
            if c: g.append(line(cx, y, cx, y + th * len(filas), "#DDE5EC", 1.3))
            g.append(T(cx + cols[c] / 2, yy + 30, [val], 17 if r else 15.5,
                       NAVY if r == 0 else INK, weight="700" if r == 0 else "400", anchor="middle"))
            cx += cols[c]
        if r: g.append(line(x, yy, x + tw, yy, "#DDE5EC", 1.3))
    return "".join(g)


# ══════════ LAS 8 PREGUNTAS ICFES ══════════
ICFES = {
 1: [dict(f="Saber 11 · 2019 · Cuadernillo 2 · N.º 46",
          e="Se determinó la temperatura entre las 12 m. y las 9 p.m. de un mismo día para tres ciudades. "
            "Los resultados se presentan en la gráfica. De acuerdo con la información de la gráfica, "
            "¿cuál de las siguientes afirmaciones es correcta?",
          img="icfes_temp.png", h=440,
          o=["La temperatura máxima de la ciudad 1 es menor que la temperatura mínima de la ciudad 3.",
             "La temperatura de la ciudad 2 siempre fue la más alta de las tres ciudades entre las 6 p.m. y las 9 p.m.",
             "La temperatura máxima de la ciudad 3 es menor que la temperatura máxima de la ciudad 2.",
             "La temperatura de la ciudad 3 siempre fue la más alta de las tres ciudades entre las 3 p.m. y las 6 p.m."],
          rel=dict(op=1, campos=["hora del día / temperatura °C", "la 3 sube y luego cae fuerte",
                                 "de 6 a 9 p.m. la 2 va por encima", "la C: la 3 llega a 30 y la 2 solo a 29"],
                   sv=("que la naranja llega más arriba que todas en un punto", "B", "la C"))),
     dict(f="Saber 11 · 2019 · Cuadernillo 2 · N.º 61",
          e="Dos aviones diferentes realizan el mismo viaje entre dos ciudades. Sin embargo, salen y llegan a "
            "horas diferentes. En la gráfica se muestra la distancia en relación con las horas de vuelo, para "
            "cada avión. Un empleado de la aerolínea ve el plan de vuelo y afirma que a las 11 a.m. ambos "
            "aviones habían recorrido la misma distancia. Esta afirmación es",
          img="icfes_vuelo.png", h=400,
          o=["incorrecta, pues solo al final ambos aviones recorren la misma distancia.",
             "correcta, pues en este punto se cruzan ambas líneas.",
             "incorrecta, pues uno de los aviones recorre una mayor distancia que el otro.",
             "correcta, pues este punto corresponde a la mitad de la distancia de viaje."],
          rel=dict(op=1, campos=["hora / km recorridos", "las dos suben, una más empinada",
                                 "a las 11 se cruzan en 600 km", "la A: no es solo al final"],
                   sv=("que las dos líneas se tocan en la mitad, no al final", "B", "la A")))],
 2: [dict(f="Saber 11 · 2019 · Cuadernillo 2 · N.º 28",
          e="Una empresa oferta una vacante de empleo en la que ofrece un salario básico de $950.000 y $75.000 "
            "adicionales por cada año de experiencia que tenga el aspirante. ¿Cuál de los siguientes "
            "procedimientos permite calcular el salario de un aspirante cualquiera?",
          img=None, h=0,
          o=["Multiplicar $950.000 por $75.000 y sumar los años de experiencia.",
             "Multiplicar $950.000 por los años de experiencia y adicionar $75.000.",
             "Sumar $950.000 al resultado de multiplicar $75.000 por los años de experiencia.",
             "Sumar $950.000 y $75.000, y multiplicar el resultado por los años de experiencia."],
          rel=dict(op=2, campos=["$75.000 por cada año", "$950.000 ya los tiene desde el día uno",
                                 "950.000 + (75.000 × años)", "la B: multiplica la base, no el aumento"],
                   sv=("que el básico no se multiplica por nada", "C", "la B"))),
     dict(f="Saber 11 · 2019 · Cuadernillo 2 · N.º 17",
          e="En un hotel se vende un cepillo de dientes por 6 dólares. A una persona que aún no ha cambiado sus "
            "pesos colombianos a dólares, el hotel le recibe el pago en pesos colombianos a una tasa de cambio "
            "de 3.000 pesos por cada dólar. ¿Cuánto debe pagar la persona por el cepillo?",
          img=None, h=0,
          o=["500 pesos colombianos.", "18.000 pesos colombianos.",
             "9.000 pesos colombianos.", "3.000 pesos colombianos."],
          rel=dict(op=1, campos=["3.000 pesos por cada dólar", "no hay base, arranca en cero",
                                 "6 × 3.000 = 18.000", "la A: eso sería dividir, no multiplicar"],
                   sv=("que cada dólar vale 3.000, y son 6", "B", "la A")))],
 3: [dict(f="Saber 11 · 2019 · Cuadernillo 2 · N.º 12",
          e="Por cada moneda que Miguel introduce en su alcancía en un día, al siguiente introduce el doble. "
            "El viernes, Miguel insertó 512 monedas. ¿Cuántas monedas introdujo en su alcancía el miércoles "
            "de esa misma semana?",
          img=None, h=0,
          o=["32", "64", "128", "508"],
          rel=dict(op=2, campos=["de un día al otro se duplica", "se multiplica, no se suma",
                                 "512 → 256 (jue) → 128 (mié)", "la D: eso sería restar 4"],
                   sv=("que para devolverme tocaba dividir en 2", "C", "la D"))),
     dict(f="Saber 11 · 2018-I · Cuadernillo 1 · N.º 86",
          e="Rosendo le solicitó al banco un préstamo de $200.000, para cancelarlo en 5 pagos mensuales. "
            "Cada mes abona $40.000 a la deuda y paga un interés del 10 % sobre el saldo a la fecha. "
            "La tabla muestra la cantidad de dinero que Rosendo debe pagar en las dos primeras cuotas. "
            "¿Cuál es el valor que debe pagar Rosendo en la cuota 3?",
          img=None, h=0, tabla=dict(h=46 * 6, draw=tabla_rosendo),
          o=["$40.000", "$52.000", "$56.000", "$116.000"],
          rel=dict(op=1, campos=["el saldo baja $40.000 cada mes", "el interés es 10 % del saldo, no fijo",
                                 "10 % de 120.000 = 12.000 → +40.000", "la C: ese es el valor de la cuota 2"],
                   sv=("que el interés bajaba junto con el saldo", "B", "la C")))],
 4: [dict(f="Saber 11 · 2019 · Cuadernillo 2 · N.º 18",
          e="Un canal de televisión presenta varios documentales en el horario de la noche. En la gráfica se "
            "muestra el nivel de audiencia de los documentales P y Q, durante su primer mes al aire. "
            "Basándose en la gráfica, un empleado del canal concluyó que el documental Q tuvo mayor nivel de "
            "audiencia que el documental P todos los días del mes. ¿Es verdadera la conclusión del empleado?",
          img="icfes_docu.png", h=430,
          o=["Sí, porque las funciones P(x) y Q(x) tienen rangos diferentes.",
             "No, porque las funciones P(x) y Q(x) tienen dominios iguales.",
             "Sí, porque P(x) = Q(x) − 20; por tanto, Q(x) es mayor.",
             "No, porque P(x) = Q(x) + 20; por tanto, P(x) es mayor."],
          rel=dict(op=3, campos=["que Q fue mayor que P TODOS los días del mes",
                                 "el día 5: P marca 50 y Q marca 30. Con uno basta.",
                                 "falsa — P va siempre 20 puntos por encima de Q",
                                 "la C: dice que Q es mayor, y la gráfica muestra lo contrario"],
                   sv=("que la línea de P iba siempre por encima de la de Q", "D", "la C"))),
     dict(f="Saber 11 · 2019 · Cuadernillo 2 · N.º 61",
          e="Dos aviones diferentes realizan el mismo viaje entre dos ciudades. Un empleado de la aerolínea "
            "afirma que a las 11 a.m. ambos aviones habían recorrido la misma distancia. Vuelve a mirar la "
            "gráfica del plan de vuelo: esta vez no te quedes con el sí o el no, revisa también la razón que "
            "da cada opción. ¿Cuál justifica correctamente el veredicto?",
          img="icfes_vuelo.png", h=400,
          o=["incorrecta, pues solo al final ambos aviones recorren la misma distancia.",
             "correcta, pues en este punto se cruzan ambas líneas.",
             "incorrecta, pues uno de los aviones recorre una mayor distancia que el otro.",
             "correcta, pues este punto corresponde a la mitad de la distancia de viaje."],
          rel=dict(op=1, campos=["que a las 11 llevaban lo mismo", "no hay: ahí sí se cruzan",
                                 "verdadera, porque las líneas se cortan",
                                 "la D: dice correcta pero por una razón falsa"],
                   sv=("que el cruce es el punto donde van iguales", "B", "la D")))],
}
