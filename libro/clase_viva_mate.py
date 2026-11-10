#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUÍAS DE CLASE PROYECTABLES («clase viva») · MATEMÁTICAS · las 8 del área.

    python3 clase_viva_mate.py [carpeta]      (por defecto entregables/guias_matematicas/)

Escribe MAT_Clase1_Mision1.html … MAT_Clase6_Mision6.html, MAT_Clase7_Simulacro.html,
MAT_Clase8_Devolucion.html y entregables/EDUCATE_Guias_Matematicas.zip.

Usa el motor clase_viva.py sin cambiarlo (la plantilla, el JavaScript, la portada, las reglas, el
reto, el cierre y las clases 7 y 8). Lo propio de Matemáticas va en escenas escritas aquí, con las
mismas clases CSS y los mismos atributos data-* que el motor, para que el JavaScript y
verifica_guias.js las manejen igual:

  · ACTIVACIÓN: una tabla de datos inventados que se destapa, la pregunta del planeador («¿qué
    está cambiando aquí, y respecto a qué?») y la pista escondida.
  · PREGUNTA PROBLEMATIZADORA: la pregunta 1 del libro en pantalla, completa, con su figura
    redibujada (figuras_mate.py), el conteo de manos y la clave detrás de «Revelar», que el
    planeador manda revelar al final del momento.
  · BLOQUES: cada pregunta del libro con su página, su estrategia (número y color del chip del
    cuaderno), su instrumento y la instrucción del instrumento tal como está impresa en el
    cuaderno. La clave y el aviso del libro salen solo con «Revelar las claves».
  · ENTRENAMIENTO: las 4 preguntas con enunciado, datos y figura (SVG o tabla HTML), rotuladas
    «Pregunta Saber 11» (decisión de Nelson, 10 nov), con la estrategia que entrenan.

De dónde sale cada cosa:
  · plan_mate.py (sin tocarlo): FASES, MISIONES, TALLER, INS_ICFES, BANCO, AVISOS, DINAMICAS y
    RETOS. Las dinámicas y los retos son los del planeador, en su orden.
  · tablero/misiones.csv: el número de cada estrategia en el cuaderno. En la Misión 6 el
    planeador numera distinto (E1 = «Juzgar el procedimiento») que el cuaderno (E1 = «Todos los
    casos que cuentan»): la guía usa el número del cuaderno, que es lo que ve el estudiante.
  · el cuaderno (páginas 11–52): página del libro de cada pregunta y la instrucción de cada
    instrumento (LEAD, copiada del PDF entregado).
  · lo escrito aquí: las claves del taller (CLAVE) y el camino a cada una (SOL), resueltas una por
    una contra fuente_libro/MATEMATICAS; los enunciados de entrenamiento (ICFES) con su clave y su
    camino; títulos, activaciones, «Si Matemáticas no es tu fuerte» (FUERTE) y los avisos para el
    estudiante (PROYECTAR). Todo eso lo debe revisar un especialista de Matemáticas.

Antes de escribir comprueba que las claves de entrenamiento coinciden con tablero/icfes.csv, que
las 60 preguntas del libro tienen clave y camino, y que no aparece ningún nombre de la lista
PROHIBIDOS.
"""
import csv, os, re, sys, types, zipfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import clase_viva as CV
import plan_mate as P
import figuras_mate as F

E = CV.E
OUT = os.path.join(AQUI, "..", "entregables", "guias_matematicas")
ZIP = os.path.join(AQUI, "..", "entregables", "EDUCATE_Guias_Matematicas.zip")
MEMBRETE = "Pregunta Saber 11"          # decisión de Nelson, 10 nov: sin año y sin «oficial»
NOMBRE = "Matemáticas"
FUERTE = "Si Matemáticas no es tu fuerte"

# ─────────────────────────────── colores ───────────────────────────────
# Momentos: --m1 es el azul del área (lo fija el motor). Los otros cinco no repiten ninguno de los
# cuatro colores de estrategia del cuaderno (azul #242478, rojo #A82424, verde #30843C, oro
# #C9821B), para que en una misma diapositiva el momento y la estrategia no se confundan.
COLORES = dict(m2="#A23B72", m3="#5B3E96", m4="#0E7C86", m5="#3E4A5C", m6="#8C5A2B",
               azul="#242478", oro="#B0711A", verde="#2E7A39", rojo="#A82424")
AZUL, ROJO, VERDE, ORO = "#242478", "#A82424", "#30843C", "#C9821B"
# Color del chip de cada estrategia en el cuaderno (muestreado de las páginas 11–52).
EST_COL = {1: [AZUL, VERDE, ORO, ROJO]}
for _m in range(2, 7):
    EST_COL[_m] = [AZUL, ROJO, VERDE, ORO]


def estr_cuaderno():
    """{misión: [E1, E2, E3, E4]} con el orden del cuaderno (tablero/misiones.csv)."""
    out = {}
    with open(os.path.join(AQUI, "..", "tablero", "misiones.csv"), encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            m = re.fullmatch(r"Misión (\d)", r["mision"].strip())
            if m:
                out[int(m.group(1))] = [x.strip() for x in r["estrategias"].split(" · ")]
    # el csv quita las comas de los nombres: se recuperan los del planeador
    for mis, lista in out.items():
        nombres = {re.sub(r"[^\w]", "", n): n for n in P.MISIONES[mis]["estr"]}
        out[mis] = [nombres[re.sub(r"[^\w]", "", n)] for n in lista]
    return out


ESTR = estr_cuaderno()


def num_est(mis, nombre):
    return ESTR[mis].index(nombre) + 1


def col_est(mis, nombre):
    return EST_COL[mis][num_est(mis, nombre) - 1]


# ─────────────────────────────── portada de cada clase ───────────────────────────────
TITULOS = {
    1: "Lo que sube, lo que crece y lo que se repite",
    2: "El techo no siempre está al final",
    3: "Partir, comparar y medir antes de mover",
    4: "Cada medida se estira a su manera",
    5: "Cada pregunta tiene su medida",
    6: "Hasta dónde llega un dato",
}
LEADS = {
    1: "Hoy no vamos a calcular más rápido. Vamos a leer lo que cambia: qué sube y hasta dónde, qué "
       "se queda fijo y qué se suma cada vez.",
    2: "El valor más alto no es el último porque sí. Hoy buscamos el techo con el modelo en la mano, "
       "y tumbamos afirmaciones con un solo número.",
    3: "Ninguna figura difícil se mide de un golpe. Hoy la partimos en piezas que sí sabemos medir, "
       "comparamos con la misma razón y medimos antes de mover.",
    4: "Una escala no multiplica todo por el mismo número, y un triángulo no se resuelve sin nombrar "
       "sus lados. Hoy cada medida va en su dimensión.",
    5: "Media, mediana, moda y rango responden preguntas distintas. Hoy primero leemos qué pregunta "
       "el enunciado y después escogemos la medida.",
    6: "La última clase de contenido del área. Hoy separamos lo que el dato mide de lo que alguien "
       "afirma con él, y contamos todos los casos antes de dar una probabilidad.",
}
LIBRO = {1: (271, 273), 2: (281, 283), 3: (293, 295), 4: (303, 306), 5: (315, 318), 6: (325, 328)}

# «Si Matemáticas no es tu fuerte» de la portada: lo que el profe tiene que poder explicar hoy.
FUERTE_MIS = {
    1: ["Razón de cambio: cuánto cambia una cantidad por cada unidad que avanza la otra. En una recta "
        "es la pendiente, y es la misma en todos los tramos.",
        "Modelo lineal y = mx + b: b es lo que hay desde el principio (lo fijo) y m lo que se suma por "
        "cada unidad (lo que crece). C(x) = 2.500x + 10.000: 10.000 de entrada y 2.500 por artículo.",
        "Parábola: sube, llega a un punto máximo (el vértice) y vuelve a bajar. Es simétrica: lo que "
        "pasa un segundo antes del vértice se repite un segundo después.",
        "Patrones: antes de buscar una fórmula se restan términos seguidos. Si la resta es siempre la "
        "misma, el patrón es lineal; si la resta se duplica, hay una potencia de 2."],
    2: ["El máximo de y = at² + bt + c (con a negativa) está en t = −b ÷ (2a). Son dos datos distintos: "
        "DÓNDE se alcanza (el valor de t) y CUÁNTO vale (lo que da la fórmula en ese t).",
        "Refutar no es opinar: basta un solo dato del propio modelo que contradiga la afirmación.",
        "Aumento constante: si cada periodo suma lo mismo, el crecimiento es lineal. Que algo sea grande "
        "no quiere decir que crezca más rápido.",
        "Ingreso neto = lo que entra menos lo que costó."],
    3: ["Volumen de un prisma = área de la base × altura. Volumen de una pirámide = ⅓ × área de la base "
        "× altura.",
        "Semejanza: si dos triángulos tienen los mismos ángulos, sus lados son proporcionales. Los rayos "
        "del sol llegan paralelos, así que un objeto y su sombra forman triángulos semejantes con otro "
        "objeto y la suya.",
        "Unidades: 1 m = 100 cm, pero 1 m² = 10.000 cm² y 1 m³ = 1.000.000 cm³. Antes de dividir, todo "
        "en la misma unidad.",
        "Longitud de una circunferencia = 2πr; un cuarto de vuelta es la cuarta parte."],
    4: ["Escala 1:k: las longitudes se multiplican por k, las áreas por k² y los volúmenes por k³.",
        "En un triángulo rectángulo, mirando un ángulo: el opuesto es el lado de enfrente, el adyacente "
        "es el que lo toca y no es la hipotenusa, y la hipotenusa es el lado más largo. sen = opuesto ÷ "
        "hipotenusa; cos = adyacente ÷ hipotenusa; tan = opuesto ÷ adyacente.",
        "Volumen de un cilindro = π · r² · h. Un metro cúbico son 1.000 litros.",
        "Área de un círculo = π · r²; la de medio círculo, la mitad. Área de un triángulo rectángulo = "
        "cateto × cateto ÷ 2."],
    5: ["Media: el reparto parejo (suma ÷ cantidad de datos). Mediana: el dato del medio, con los datos "
        "ordenados. Moda: el que más se repite. Rango: el mayor menos el menor.",
        "Dispersión (rango, desviación estándar): qué tan separados están los datos. «Homogéneo» quiere "
        "decir poca dispersión, no media baja.",
        "Probabilidad = casos que interesan ÷ casos posibles. Un porcentaje de un total = total × "
        "porcentaje ÷ 100.",
        "Para decidir si algo pasa del 50 %, primero se suman los porcentajes y después se compara."],
    6: ["Complemento: la probabilidad de que NO pase es 1 menos la de que pase.",
        "Sin reemplazo: lo que se saca no vuelve, así que en la segunda extracción el total tiene uno "
        "menos.",
        "Contar con orden y sin repetir: de 10 dígitos se arman 10 × 9 = 90 parejas distintas (eso es "
        "10! ÷ 8!). Con repetición: 5 dígitos en 4 posiciones son 5⁴.",
        "«Al menos 3 de 4» son dos casos: exactamente 3 o los 4. Cada caso se calcula y después se suman.",
        "Una encuesta describe el presente; usarla para el futuro es una suposición que hay que decir."],
}

# ─────────────────────────────── activación ───────────────────────────────
# (filas de la tabla, pregunta de más, pista). Los datos son inventados para la clase.
ACTIVACION = {
    1: ([("segundo", "0", "1", "2", "3", "4"), ("metros", "0", "15", "20", "15", "0")],
        "Y una más: ¿en qué momento deja de pasar lo que venía pasando?",
        "Es la altura de un balón pateado hacia arriba, segundo a segundo: sube, llega y vuelve. El "
        "proyectil de la pregunta 1 hace lo mismo."),
    2: ([("semana", "1", "2", "3", "4", "5", "6"), ("ventas", "30", "45", "55", "60", "55", "45")],
        "Y una más: ¿dónde está el valor más alto? ¿Es el último?",
        "Son las arepas que vendió la tienda del colegio cada semana. El techo está en la semana 4, no "
        "en la última: es el error que comete el libro en la pregunta 1 de hoy."),
    3: ([("lado (cm)", "1", "2", "3", "4"), ("cubitos que caben", "1", "8", "27", "64")],
        "Y una más: ¿el segundo número crece igual que el primero?",
        "Son cubos armados con cubitos de 1 cm. Si el lado se duplica, caben 8 veces más cubitos: lo que "
        "mide no crece igual que lo que llena."),
    4: ([("lado en el plano (cm)", "1", "2", "3"), ("área en la realidad (m²)", "25", "100", "225")],
        "Y una más: cuando el primero se duplica, ¿por cuánto se multiplica el segundo?",
        "Es un plano a escala 1:500: 1 cm del papel son 5 m de verdad, y un cuadrado de 1 cm de lado "
        "cubre 25 m². Si el lado se duplica, el área se multiplica por 4."),
    5: ([("estudiante", "A", "B", "C", "D", "E"), ("minutos", "10", "12", "12", "15", "46")],
        "Y una más: ¿qué número representa mejor a este grupo?",
        "Son los minutos que tardan cinco estudiantes en llegar al colegio. El promedio da 19, pero "
        "cuatro de los cinco tardan 15 o menos: un solo dato alejado arrastra la media; la mediana (12) "
        "no se mueve."),
    6: ([("", "rojas", "azules", "verdes", "total"), ("antes", "5", "3", "2", "10"),
         ("después de sacar una roja", "4", "3", "2", "9")],
        "Y una más: ¿qué cambió y qué se quedó igual?",
        "Es una caja con bolas. Al sacar una roja sin devolverla cambia el total: la probabilidad de "
        "sacar azul pasa de 3/10 a 3/9 aunque las azules siguen siendo 3."),
}

# ─────────────────────────────── las 60 preguntas del libro ───────────────────────────────
# Claves verificadas resolviendo cada pregunta contra fuente_libro/MATEMATICAS (10 nov).
# «A · B»: dos opciones correctas (hallazgos 2, 7 y 9); la que va primero es la que defiende el
# cuaderno cuando el libro pide una sola.
CLAVE = {
    1: ["A", "B", "C", "A", "A · B", "D", "A", "C", "A", "B"],
    2: ["A", "C", "B", "C", "A", "B", "C", "D", "C", "D"],
    3: ["B", "B", "A", "C", "A", "C", "A", "B", "D", "C"],
    4: ["D · C", "B", "A", "A", "C", "D", "C", "A", "B", "B"],
    5: ["B", "B", "D", "A", "A", "C", "A", "D", "B", "A"],
    6: ["D", "C", "D", "A", "B", "A", "B", "A", "A", "C · B"],
}
CLAVE = {m: dict(enumerate(v, 1)) for m, v in CLAVE.items()}

# El camino a cada clave (va a la guía del profe, en «Si Matemáticas no es tu fuerte»).
SOL = {
 (1, 1): "La gráfica sube de t = 0 a t = 3 (llega a 45 m) y baja de 3 a 6. Sube solo de 0 a 3 s. La C "
         "confunde «estar arriba del suelo» con «estar subiendo».",
 (1, 2): "−5t² + 30t = 40 → t² − 6t + 8 = 0 → (t − 2)(t − 4) = 0. Pasa por 40 m en t = 2 (subiendo) y "
         "en t = 4 (bajando): después del máximo, 4 s. Por simetría: el pico está en 3; el 2 está 1 s "
         "antes, así que el otro cruce está 1 s después.",
 (1, 3): "Tres controles: sale de (0, 0), llega a 45 m en t = 3 y vuelve a 0 en t = 6. Solo la C los "
         "pasa. La A es una recta, la B se queda plana en 40 y la D arranca en 10 y no pasa de 40.",
 (1, 4): "C(25) − C(20) = 72.500 − 60.000 = 12.500, en 5 artículos: 2.500 por artículo. La B (12.500) es "
         "el cambio total, no la tasa. En un modelo lineal la tasa es siempre el número que acompaña a x.",
 (1, 5): "C(7) = 2.000 × 7 + 15.000 = 29.000: el cliente tiene razón. La A dice la cuenta y la B dice "
         "la misma cuenta en palabras (costo fijo más 7 pagos de 2.000): las dos son correctas.",
 (1, 6): "1.450.000 − 200.000 = 1.250.000; 1.250.000 ÷ 50.000 = 25 personas. Se comprueba: 50.000 × 25 "
         "+ 200.000 = 1.450.000.",
 (1, 7): "C(1) = 60.000, C(2) = 68.500, C(3) = 77.000, C(4) = 85.500: cada kilo suma 8.500. Aumenta "
         "siempre lo mismo.",
 (1, 8): "102.000 − 60.000 = 42.000; 42.000 ÷ 8.500 ≈ 4,94 kilos adicionales al primero, así que p ≈ "
         "5,94 ≈ 6 kg. C(6) = 102.500 es el valor más cercano a lo que pagó.",
 (1, 9): "La fórmula tiene un solo número por kilo (8.500) y ninguna condición de «después de tantos "
         "kilos». Las otras tres opciones inventan esa condición.",
 (1, 10): "Las barras van 120, 140, 160, 180: suben 20 cada semana. La semana 5 es 200 mil: 200.000.",
 (2, 1): "El vértice de D(t) = −5t² + 40t + 120 está en t = −40 ÷ (2 × −5) = 4, y D(4) = 200 km. El "
         "enunciado pide la semana SIGUIENTE (la 5), y D(5) = 195 km: ninguna opción lo dice. La B pone "
         "semana 5 con 220 km, que no sale del modelo. La clave del libro es la A, la del máximo.",
 (2, 2): "D(4) = 200 y D(10) = −500 + 400 + 120 = 20: la distancia sube hasta la semana 4 y después "
         "baja. En la 10 está muy lejos del máximo. Dos números del modelo bastan para refutarlo.",
 (2, 3): "Vértice en t = −180 ÷ (2 × −15) = 6; A(6) = −540 + 1.080 + 900 = 1.440 visitantes. Es la "
         "pregunta 1 con otros números.",
 (2, 4): "Cada visitante deja 42.000 (30.000 de entrada y 12.000 de gasto): el ingreso sube y baja con los "
         "visitantes. El máximo es el día 6, así que el mayor ingreso es antes del día 7. Los días 9 y 10 "
         "tienen menos (A(9) = 1.305 y A(10) = 1.200).",
 (2, 5): "72.500 − 60.000 = 12.500 por 5 bloques más: 2.500 por bloque. La B es el aumento total.",
 (2, 6): "Cada semana creció 2,5 cm: el aumento es el mismo. La planta es más alta (el tamaño cambió), "
         "pero la velocidad no: no crece «cada vez más rápido».",
 (2, 7): "Sube 20 por mes: junio 150, julio 170, agosto 190. Quien para un mes antes marca 170 (B).",
 (2, 8): "Del día 6 en adelante se venden 140, 120, 100…; si se hornean 160, sobran 20, 40, 60… y cada pan "
         "que sobra ya costó 3.000. La propuesta no es adecuada: D.",
 (2, 9): "La frase tiene dos partes: «la venta creció» (cierto en la primera semana) y «seguirá creciendo "
         "al mismo ritmo» (falso: desde el día 6 baja 20 por día). Basta con que una parte falle.",
 (2, 10): "Día 4: 140 panes. Ingreso 140 × 4.500 = 630.000; costo 140 × 3.000 = 420.000; neto 210.000. Por "
          "el otro camino: cada pan deja 1.500, y 140 × 1.500 = 210.000.",
 (3, 1): "Prisma: 4 × 4 × 3 = 48 m³. Pirámide: ⅓ × 16 × 6 = 32 m³. Total: 80 m³. La C (96 m³) sale de "
         "olvidar el ⅓ y quitar el prisma; las otras, de usar mal la fórmula de la pirámide.",
 (3, 2): "Rayos paralelos, triángulos semejantes: 10 ÷ 12 = 26 ÷ x → x = 26 × 12 ÷ 10 = 31,2 m. En el "
         "libro la cuarta opción viene rotulada «A.»: es la D.",
 (3, 3): "altura ÷ sombra: farola 10 ÷ 12 ≈ 0,83; estatua 26 ÷ 31,2 ≈ 0,83. La B (1,2 = 1,2) también es "
         "una igualdad cierta, pero es sombra ÷ altura: no es la razón altura : sombra que piden.",
 (3, 4): "Todo en metros: la baldosa mide 0,4 m y cubre 0,16 m². El piso: 12 × 8 = 96 m². 96 ÷ 0,16 = "
         "600. Por filas: 12 ÷ 0,4 = 30 y 8 ÷ 0,4 = 20; 30 × 20 = 600.",
 (3, 5): "Circunferencia: 2π × 10 ≈ 62,8 m; un cuarto ≈ 15,7 m. La C es la vuelta entera y la B, media.",
 (3, 6): "Base: dos capas de cubos de 20 cm = 40 cm; nivel 2: 20 cm; nivel 3: 20 cm. Total: 80 cm.",
 (3, 7): "La vitrina mide 100 cm y la muñeca 40: tiene que empezar a 60 cm o menos. Sin los prismas del "
         "nivel 3, la cima queda a 60 cm y la muñeca llega justo a 100. Las otras opciones suben la "
         "pirámide o desarman la base.",
 (3, 8): "Un cubo: 0,2 × 0,2 × 0,2 = 0,008 m³; 32 cubos: 0,256 m³. La opción dice «se multiplican los "
         "volúmenes de 32 cubos»: se entiende el volumen de un cubo multiplicado por 32.",
 (3, 9): "Prisma: 40 × 20 × 20 = 16.000 cm³; cubo: 20 × 20 × 20 = 8.000 cm³. El prisma son 2 cubos: se ve "
         "partiendo su largo de 40 en dos de 20.",
 (3, 10): "Las tres piezas cubren 4 + 4 + 4 = 12 casillas. En la figura del libro hay 7 casillas vacías, "
          "no 14 como dice la C. «No es posible» es cierto (12 no es 7), pero la razón de la C usa un "
          "número que la figura no muestra. La clave del libro es la C.",
 (4, 1): "Real: r = 200 cm = 2 m, h = 500 cm = 5 m; V = π × 2² × 5 = 20π ≈ 62,8 m³. Por el otro camino: "
         "en la maqueta V = 20π cm³, × 100³ = 20π m³. C y D llegan al mismo número; la pregunta pide el "
         "más directo y seguro, la D, porque no hay que acordarse de elevar al cubo.",
 (4, 2): "12 cm × 2.000 = 24.000 cm = 240 m. El paso que más se olvida es el último: pasar a metros.",
 (4, 3): "La base (4 m) es el cateto adyacente a θ y la longitud de la rampa es la hipotenusa: adyacente ÷ "
         "hipotenusa es el coseno, cos θ = 4 ÷ hipotenusa, como propone el grupo A.",
 (4, 4): "cos 30° = 4 ÷ L → L = 4 ÷ cos 30° = 4 ÷ 0,866 ≈ 4,62 m. Quien multiplica (4 × 0,866 ≈ 3,46) "
         "obtiene algo menor que la base: imposible para una hipotenusa.",
 (4, 5): "π × 1,5² × 4 = 9π ≈ 28,3 m³, que es más que 24 m³. El folleto está bien; el asistente leyó 9π "
         "como si fuera 9.",
 (4, 6): "9π ≈ 28,27 m³; 28,27 ÷ 0,001 = 28.274 litros, unos 28.000.",
 (4, 7): "Rectángulo: 12 × 8 = 96 m². Semicírculo sobre el lado de 8 m: r = 4, π × 16 ÷ 2 ≈ 25,1 m². "
         "Total ≈ 121 m².",
 (4, 8): "El ángulo de tiro va de un poste al otro. tan θ = 7/18 da solo el ángulo hacia un poste, no la "
         "apertura entre los dos.",
 (4, 9): "3,6 cm × 500 = 1.800 cm = 18 m, que coincide con los 18 m del enunciado.",
 (4, 10): "En el punto de la barrera el balón va a 2,4 m y la barrera mide 2 m: pasa 0,4 m por encima.",
 (5, 1): "«Homogéneos» se mide con la dispersión (desviación estándar), no con la media. Beta tiene la "
         "desviación más alta (20): es el barrio menos homogéneo.",
 (5, 2): "Tarde + noche = 80 + 50 = 130; 130 ÷ 260 = 0,5 = 50 %.",
 (5, 3): "Datos 4, 6, 10, 5, 5: media 30 ÷ 5 = 6; mediana 5; moda 5; rango 6. «En promedio» es la media, "
         "6, que no supera 7. La B también dice «incorrecta», pero con la mediana, que no es el promedio.",
 (5, 4): "Barras 20, 40, 60, 50, 30 (suman 200). El 40–59 tiene 60, el mayor. Menos de 60 puntos: 120, "
         "que es el 60 % exacto, no «más del 60 %» (B). Desde 60: 80, no 100 (C). Extremos: 50, no la "
         "mitad (D).",
 (5, 5): "Manzana 30 % + banano 25 % = 55 %, más de la mitad.",
 (5, 6): "Chile 26,08 + Argentina 14,70 = 40,78 %, más del 40 %. A: 4,33 %; B: 12,40 frente a 20,55; D: "
         "Perú 6,90 frente a 6,84.",
 (5, 7): "40,78 % de 500.000 = 203.900 ≈ 204.000.",
 (5, 8): "Chile + Argentina = 40,78. Con EE. UU.: 50,33; con México: 51,78; con Guatemala: 53,18; con "
         "Perú: 47,68, que no llega al 50.",
 (5, 9): "En la captura: nuevos 67 % y recurrentes 33 %. 0,67 × 4.100 ≈ 2.747 y 0,33 × 4.100 ≈ 1.353. Con "
         "el 7 % que dice el texto ninguna opción cuadra.",
 (5, 10): "Nuevos: 2.747 × 0,42 ≈ 1.154 mujeres. Las otras: B, recurrentes mujeres ≈ 568; C, hombres en "
          "total ≈ 2.378; D, recurrentes hombres ≈ 785.",
 (6, 1): "A usa la frecuencia observada (0,6) como probabilidad empírica: razonable. B la mete en un modelo "
         "binomial: razonable. C tira los datos y supone ⅓ para cada caso sin razón: inválido. La D es la "
         "única que valora los tres.",
 (6, 2): "Al menos 3 de 4: exactamente 3 → 4 × 0,85³ × 0,15 ≈ 0,368; los 4 → 0,85⁴ ≈ 0,522. Suma ≈ 0,890. "
         "La fórmula de la C está bien; el número impreso (0,833) no.",
 (6, 3): "(800 + 600) ÷ 2.000 = 0,7 es correcto: «al menos una vez por semana» incluye a quienes leen a "
         "diario, así que el segundo investigador se equivoca. La D dice que el número está bien y pide "
         "nombrar con precisión el evento. La A también le da la razón al primero: si alguien la defiende "
         "con la cuenta, tiene argumento.",
 (6, 4): "De 100 empleos, 30 están en riesgo; de esos, no se reconvierte el 30 % (100 % − 70 %): 30 × 0,30 "
         "= 9 de cada 100. El cálculo es coherente.",
 (6, 5): "El 65 % es riesgo, no pérdida, y el 40 % de esos puede reconvertirse: se perderían unos 65 × "
         "0,6 = 39 de cada 100. El investigador matiza bien.",
 (6, 6): "Complemento: 1 − 0,45 = 0,55. La tasa de desempleo (8 %) es un dato que sobra.",
 (6, 7): "Menor riesgo no es cero riesgo: 3 de cada 10 empleos están en riesgo. «No tendrá problemas» es un "
         "absoluto que el dato no sostiene.",
 (6, 8): "5/10 la roja; queda una bola menos, así que 3/9 la azul. P = 5/10 × 3/9 = 1/6. El segundo cálculo "
         "(× 3/10) sería con reemplazo.",
 (6, 9): "Dos órdenes: literatura y después ciencia (40/100 × 35/99) o ciencia y después literatura "
         "(35/100 × 40/99). Suma = 2 × 1.400 ÷ 9.900 ≈ 0,283.",
 (6, 10): "La encuesta mide el presente; el 40 % no se puede proyectar al futuro sin más información. La B y "
          "la C son ciertas: la B descarta al analista y la C además valora la postura del experto, que es "
          "lo que se preguntó. El cuaderno lleva a la C.",
}

# La instrucción de cada instrumento, tal como está impresa en el cuaderno (páginas 11–52).
LEAD = {
 (1, 1): "No respondas desde la fórmula todavía. Recorre la gráfica de tu libro de izquierda a derecha y anota, en cada tramo de un segundo, si la altura sube o baja. El intervalo que te piden es el que tenga puras flechas hacia arriba.",
 (1, 2): "Una parábola es simétrica: lo que pasa antes del punto más alto se repite después, a la misma distancia. Hay dos caminos para esta pregunta. Haz el que te resulte más claro y comprueba con el otro.",
 (1, 3): "No busques «la que se parece». Pásale a cada gráfica tres controles que salen del enunciado. La correcta es la única que los pasa los tres; las demás fallan por lo menos en uno.",
 (1, 4): "La tasa de cambio promedio responde a: cuando avanzo de un punto al otro, ¿cuánto sube el costo por cada unidad que avanzo? Es un escalón: lo que sube dividido entre lo que avanza.",
 (1, 5): "El cliente hizo una afirmación. No la creas ni la descartes: compruébala. Reemplaza el dato que él dice y mira si la cuenta cierra.",
 (1, 6): "La fórmula es una máquina: entran personas y sale dinero. Aquí te dan la salida y te piden la entrada, así que hay que recorrerla al revés, deshaciendo cada paso en orden contrario.",
 (1, 7): "La pregunta es sobre el comportamiento, no sobre un valor. Calcula cuatro costos seguidos y resta cada uno con el anterior: esa resta es la que responde.",
 (1, 8): "Antes de hacer cuentas, encierra la respuesta entre dos valores con la tabla que ya hiciste. Así, cuando despejes, ya sabes si el resultado tiene sentido.",
 (1, 9): "Tres de las cuatro opciones inventan una condición: que algo cambia después de cierto peso. Una condición así tendría que estar escrita en la fórmula. Ve a buscarla.",
 (1, 10): "La barra de la semana 5 está marcada con un signo de interrogación. Para saber su altura no hace falta adivinar: mide los escalones entre las barras que sí están.",
 (2, 1): "Cada opción trae dos datos: una semana y unos kilómetros. Para que una opción sirva, los dos tienen que ser ciertos a la vez. Primero halla dónde está el techo; después comprueba cada pareja.",
 (2, 2): "Él dice que la semana 10 es la de mayor distancia. Para refutarlo no necesitas un discurso: necesitas dos números del propio modelo puestos uno al lado del otro.",
 (2, 3): "Esta pregunta es la número 1 vestida de otra forma: cambian los números y el contexto, pero el camino es idéntico. Compara las dos fórmulas antes de calcular y vas a ver que te sabes el camino.",
 (2, 4): "El empleado habla de ingresos, pero el modelo que tienes es de visitantes. Antes de responder, averigua si una cosa arrastra a la otra: eso decide toda la pregunta.",
 (2, 5): "Con dos filas de una tabla puedes reconstruir toda la regla. Halla primero cuánto sube por bloque, arma la fórmula, y compruébala volviendo a las dos filas que te dieron.",
 (2, 6): "El estudiante mira lo alta que quedó la planta y concluye que creció cada vez más rápido. Son dos cosas distintas: llena las dos columnas y verás cuál de las dos está cambiando.",
 (2, 7): "La tabla llega hasta junio y a ti te preguntan por agosto. Escribe los meses que faltan, uno por uno, marcando el salto entre cada par. El error más común es parar un mes antes.",
 (2, 8): "La propuesta es hornear 160 todos los días. Para saber si conviene, completa cuánto se vende cada día y mira qué pasa con lo que no se vendió: cada pan que sobra ya costó 3.000 pesos.",
 (2, 9): "Las afirmaciones largas suelen tener una parte verdadera y otra falsa, y por eso convencen. Pártela, juzga cada mitad por separado, y recuerda: basta con que una mitad falle.",
 (2, 10): "«Neto» quiere decir lo que queda después de descontar lo que costó. Hay dos caminos y los dos llegan al mismo número: haz uno y comprueba con el otro.",
 (3, 1): "Nadie tiene una fórmula para «prisma con sombrero». Lo que sí hay es una fórmula para la caja y otra para la punta. Separa las dos piezas, calcula cada una y después súmalas.",
 (3, 2): "El sol está tan lejos que sus rayos llegan paralelos: la farola y la estatua hacen el mismo triángulo, uno pequeño y otro grande. Dibuja los dos y pon en cada uno lo que sabes.",
 (3, 3): "Con dos alturas y dos sombras se pueden armar cuatro divisiones distintas, y cada una da un número diferente. Hazlas todas: después solo tienes que ver cuál es la que te piden.",
 (3, 4): "El piso viene en metros y la baldosa en centímetros. Mientras no estén en la misma unidad, cualquier división da un número sin sentido. Pásalo todo a metros y escoge tu camino.",
 (3, 5): "Te piden caminar por el borde, no cubrir el terreno. Antes de calcular, decide qué te están pidiendo: eso cambia la fórmula y la respuesta.",
 (3, 6): "La altura no se adivina mirando el dibujo: se suma. Escribe lo que mide cada nivel, súmalos hacia arriba y compara el total con el techo de la vitrina.",
 (3, 7): "Primero el número: cuánto espacio necesitas y cuánto tienes. Con esa diferencia en la mano, cada propuesta se juzga sola — y además hay tres reglas que ninguna puede romper.",
 (3, 8): "Las opciones vienen con explicación, y tres de ellas explican mal. Haz tu propia cuenta en dos pasos y después busca cuál opción coincide con lo que a ti te dio.",
 (3, 9): "Las dos piezas tienen 20 cm en dos de sus lados; solo cambia la tercera. Dibuja la raya que parte el prisma en cubos y después confirma con números que no te engañó el ojo.",
 (3, 10): "Antes de imaginar giros y encajes, cuenta. Si las casillas que tienes no son las mismas que los huecos que hay, ninguna manera de girar las piezas va a servir.",
 (4, 1): "Una escala 1:100 no multiplica todo por 100. Cada tipo de medida se estira a su manera. Llena la tabla primero y después haz los dos caminos: tienen que darte el mismo número.",
 (4, 2): "La escala te dice cuántas veces agrandar, pero el resultado te queda en la unidad del papel. El paso que más se olvida es el último: pasar de centímetros a metros.",
 (4, 3): "Antes de juzgar a los grupos, ponle nombre a cada lado respecto a θ: el opuesto, el adyacente y la hipotenusa. Aquí te dan la base (4 m) y te piden la hipotenusa: busca la razón que junta esos dos.",
 (4, 4): "La fórmula ya te la dieron bien. Lo que falta es despejar: la longitud está en el denominador, y eso cambia si multiplicas o divides. Equivocarte aquí no es un error de trigonometría.",
 (4, 5): "El asistente mira «9π» y lo lee como un número pequeño. Mientras π siga ahí como letra, no puedes comparar. Ponle su valor y la discusión se acaba en un renglón.",
 (4, 6): "Te dan el dato al revés de como lo necesitas: te dicen cuánto ocupa un litro, y tú quieres saber cuántos litros caben. Es una división, y conviene verla antes de hacerla.",
 (4, 7): "No hay fórmula para «rectángulo con una punta redonda». Hay una para el rectángulo y otra para el medio círculo. Marca por dónde se parten y mide cada pieza aparte.",
 (4, 8): "El enunciado dice que el ángulo de tiro va de un poste al otro. La cuenta del entrenador usa un solo poste. Dibuja los dos ángulos sobre el esquema y vas a ver que no son el mismo.",
 (4, 9): "Es la misma cuenta de la pregunta 2 con otros números. Llena la fila que falta y de paso comprueba las dos de arriba: si el método te sirve en las tres, ya lo tienes.",
 (4, 10): "Toda la pregunta cabe en una resta, pero hay que ver el corte de lado para saber cuáles dos números restar. Dibuja la barrera, marca por dónde pasó el balón y mide la diferencia.",
 (5, 1): "La conclusión usa la palabra «homogéneos». Esa palabra no se mide con el promedio: tiene su propia columna en la tabla. Une cada palabra con la medida que de verdad la responde.",
 (5, 2): "Una probabilidad es el pedazo que te interesa dividido por todo. Aquí el «todo» son las 260 visitas. Marca las franjas que entran y verás el resultado antes de dividir.",
 (5, 3): "Con cinco números se pueden sacar cuatro medidas distintas, y las opciones usan las cuatro. Sácalas todas primero; después vuelve al enunciado y fíjate en qué palabra usó el supervisor.",
 (5, 4): "Las cuatro afirmaciones hablan de cantidades y de porcentajes acumulados. Leer eso en las barras es adivinar; escrito en una tabla, se comprueba en segundos.",
 (5, 5): "La afirmación habla de dos frutas y de «más de la mitad». Son dos cosas que comprobar: cuánto suman esas dos, y si ese número pasa de 50. No basta con que una de las dos sea grande.",
 (5, 6): "Ninguna de las cuatro se decide mirando la gráfica: todas piden sumar o comparar dos o tres porcentajes. Escribe la cuenta antes de hacerla y no te enredas.",
 (5, 7): "Dos pasos: cuánto suman los dos países en porcentaje, y cuánto es ese porcentaje de 500.000. Si haces los dos de un tirón es fácil perder un cero por el camino.",
 (5, 8): "Chile y Argentina están en los cuatro conjuntos, así que esa parte la calculas una sola vez. Después solo sumas el tercer país y comparas con 50.",
 (5, 9): "La captura trae dos barras parecidas. Una parte a los espectadores en nuevos y recurrentes; la otra los parte en seguidores y no seguidores. Mira cuál de las dos responde la pregunta.",
 (5, 10): "Primero se parte en nuevos y recurrentes; después cada pedazo se vuelve a partir en hombres y mujeres. Arma el árbol completo y las cuatro afirmaciones se responden solas.",
 (6, 1): "No te piden hacer ninguna cuenta: te piden valorar tres maneras de pensar. Escribe qué supone cada una y si usa o descarta los datos de los 60 días.",
 (6, 2): "«Al menos 3» no es un solo caso: son varios. Marca en la tabla cuáles combinaciones mantienen el sistema en línea y verás cuántos términos tiene que sumar tu cuenta.",
 (6, 3): "Los dos investigadores discuten, pero no sobre lo mismo. Uno habla del resultado y el otro de cómo se nombra. Revisa las dos cosas por separado antes de darle la razón a alguno.",
 (6, 4): "De cada cien empleos, primero se apartan los que están en riesgo; de esos, se vuelven a apartar los que no logran reconvertirse. Sigue los cien hasta el final y el 9 % aparece solo.",
 (6, 5): "El periodista cambió una palabra y con eso cambió el dato. Parte los cien empleos de manufactura en sus tres grupos y cuenta cuántos se perderían de verdad.",
 (6, 6): "Te dan la probabilidad de estar en riesgo y te piden la de NO estarlo. Juntas tienen que dar el total, así que es una resta. Lo difícil no es la cuenta: es no meter datos que sobran.",
 (6, 7): "Ser el sector con menos riesgo no es lo mismo que no tener riesgo. Dibuja a cuántos de cada diez trabajadores afecta ese 30 % y vuelve a leer la afirmación.",
 (6, 8): "Sin reemplazo, la bola que sacaste ya no está. Pinta las dos cajas, cuenta cuántas quedan y el denominador de la segunda fracción se cae de maduro.",
 (6, 9): "Puede salir primero el de literatura o primero el de ciencia, y las dos cosas cumplen lo que piden. Dibuja los dos caminos, calcula cada uno y súmalos.",
 (6, 10): "Una encuesta mide lo que pasa hoy. Para hablar del futuro hace falta algo más. Separa las dos cosas y después juzga cada valoración por dos criterios, no por uno.",
}
# Página del libro de cada pregunta (la de «la lees en tu libro, página N» del cuaderno).
PAG = {1: "271 272 272 272 272 272 273 273 273 273", 2: "281 281 281 282 282 282 282 282 283 283",
       3: "293 293 293 294 294 294 294 295 295 295", 4: "303 304 304 304 305 305 305 306 306 306",
       5: "315 316 316 316 317 317 317 317 318 318", 6: "325 325 326 326 327 327 327 327 328 328"}
PAG = {m: dict(enumerate(map(int, s.split()), 1)) for m, s in PAG.items()}

# Avisos del libro que salen en pantalla al revelar la clave (redactados para el estudiante). Lo
# que dice el planeador para el profe va además a su guía. (severidad, texto)
PROYECTAR = {
    (1, 5): ("alta", "La A y la B dicen lo mismo con otras palabras: las dos son correctas."),
    (2, 1): ("alta", "El enunciado pide la semana siguiente al máximo (la 5, con 195 km) y ninguna opción lo "
                     "dice. La clave del libro, la A, es la semana del máximo."),
    (3, 2): ("media", "En el libro la cuarta opción viene rotulada «A.»: es la D."),
    (3, 8): ("baja", "La B dice «se multiplican los volúmenes de 32 cubos»: se entiende el volumen de un "
                     "cubo multiplicado por 32."),
    (3, 10): ("alta", "En la figura hay 7 casillas vacías, no 14. «No es posible» sigue siendo cierto, pero "
                      "la razón que da la C no coincide con la figura."),
    (4, 1): ("atención", "La C llega al mismo número: si la defendiste con la cuenta, tienes razón. La D es "
                         "el camino con menos pasos donde equivocarse."),
    (5, 9): ("alta", "El texto dice 7 % de espectadores nuevos y la captura dice 67 %. La clave sale de la "
                     "captura."),
    (6, 2): ("media", "La fórmula de la C está bien, pero el número impreso no: la cuenta da ≈ 0,890, no "
                      "0,833."),
    (6, 3): ("atención", "La A también le da la razón al primer investigador, y su cuenta es correcta. La D "
                         "gana porque además pide nombrar bien qué incluye el evento."),
    (6, 10): ("atención", "La B también es cierta. La C gana porque valora las dos posturas, que es lo que "
                          "se preguntó."),
}
# Lo que no está en plan_mate.AVISOS y salió de resolver de nuevo (10 nov): solo para el profe.
AVISO_NUEVO = {
    (6, 3): "Aviso nuevo (no está en el planeador ni en hallazgos.csv): la A también se puede defender. El "
            "0,7 es correcto y el primer investigador tiene razón; la D gana solo porque además pide nombrar "
            "con precisión el evento. Acepta la discusión.",
}

# ─────────────────────────────── la pregunta modelo (pregunta 1 del libro) ───────────────────────────────
MODELO = {
    1: dict(info="La función f(t) = −5t² + 30t representa la altura en metros de un proyectil lanzado "
                 "verticalmente durante los primeros 6 segundos.",
            fig="proyectil",
            e="Según la gráfica, ¿en qué intervalo de tiempo la altura del proyectil aumenta?",
            o=["De 0 a 3 segundos, porque la pendiente es positiva en ese tramo.",
               "De 3 a 6 segundos, porque el proyectil sigue en movimiento.",
               "En todo el intervalo, porque siempre está por encima del suelo.",
               "Nunca, porque la función es decreciente en todo el recorrido."]),
    2: dict(info="Un grupo de ciclistas registra la distancia total recorrida en kilómetros durante sus "
                 "entrenamientos semanales. El comportamiento se modela con la función D(t) = −5t² + 40t + "
                 "120, donde D(t) es la distancia total en la semana t y 0 ≤ t ≤ 10.",
            fig=None,
            e="El entrenador quiere programar un descanso justo después de la semana en la que se alcanza "
              "la mayor distancia recorrida. ¿En qué semana deberían tomar el descanso y cuántos kilómetros "
              "habrán recorrido en ese momento?",
            o=["Semana 4, con 200 km.", "Semana 5, con 220 km.", "Semana 6, con 240 km.",
               "Semana 7, con 210 km."]),
    3: dict(info="En un parque se construye un tanque de agua formado por un prisma rectangular de base "
                 "cuadrada, sobre el que se instala una cubierta piramidal. El lado de la base cuadrada es de "
                 "4 m, la altura del prisma es de 3 m y la altura de la pirámide es de 6 m.",
            fig="tanque",
            e="Según el esquema, ¿cuál es el volumen total de la estructura?",
            o=["64 m³", "80 m³", "96 m³", "112 m³"]),
    4: dict(info="En el plano de una maqueta arquitectónica a escala 1:100 se representa un tanque cilíndrico "
                 "con radio de 2 cm y altura de 5 cm. Un grupo de personas discute cómo calcular el volumen "
                 "real del tanque: algunos proponen multiplicar el volumen obtenido en el plano por 100, otros "
                 "por 100², otros por 100³, y algunos aseguran que lo correcto es primero hallar las "
                 "dimensiones reales y luego calcular con ellas.",
            fig="maqueta",
            e="¿Cuál de los siguientes procedimientos es el más directo y seguro para evitar errores de "
              "cálculo?",
            o=["El volumen debe multiplicarse por 100, porque la escala aumenta linealmente.",
               "El volumen debe multiplicarse por 100², ya que el área de la base crece de manera cuadrática.",
               "El volumen debe multiplicarse por 100³, pues las tres dimensiones se amplían según la escala.",
               "El volumen real se obtiene multiplicando radio y altura por 100, y calculando con esas "
               "medidas."]),
    5: dict(info="En un estudio sobre movilidad urbana se encuestaron tres barrios para estimar el tiempo (en "
                 "minutos) que tardan los habitantes en llegar a su trabajo. Un investigador concluyó: «Con "
                 "respecto al barrio Beta se puede afirmar que los tiempos de desplazamiento son los más "
                 "homogéneos, porque tienen la media más baja».",
            tabla=[("Barrio", "Media", "Mediana", "Desviación estándar"), ("Alfa", "42", "40", "6"),
                   ("Beta", "38", "30", "20"), ("Gamma", "44", "43", "8")],
            e="Con base en la información de la tabla, ¿qué valoración es correcta sobre esa conclusión?",
            o=["Es correcta, porque la media más baja implica que los tiempos de Beta son menores y, por "
               "tanto, más homogéneos.",
               "Es incorrecta, porque la dispersión en Beta es muy alta, lo que muestra desigualdad en los "
               "tiempos de desplazamiento.",
               "Es correcta, porque la mediana de Beta confirma que la mayoría tarda 30 minutos, más bajo "
               "que en los otros barrios.",
               "Es incorrecta porque, para saber qué tan homogéneos son los datos, se debe comparar la "
               "mediana y no la media."]),
    6: dict(info="De 60 días de negociación del dólar, en 36 cerró al alza, en 18 a la baja y en 6 estable. "
                 "Método A: usar la frecuencia relativa de subidas (36/60 = 0,6) como probabilidad de que "
                 "suba. Método B: un modelo binomial con n = 20 días y p = 0,6 para estimar la probabilidad "
                 "de que al menos 12 días cierren al alza. Método C: asumir que los datos pasados no sirven "
                 "y que cada día el dólar tiene probabilidad ⅓ de subir, bajar o quedarse igual.",
            fig=None,
            e="Con base en esta situación, ¿qué valoración es más adecuada?",
            o=["El método A es pertinente, porque usar la frecuencia observada como probabilidad empírica "
               "permite proyectar tendencias, aunque con limitaciones.",
               "El método B es el más adecuado, pues convierte la frecuencia observada en un modelo "
               "probabilístico que ayuda a estimar escenarios concretos.",
               "El método C es el más válido, ya que sin información adicional no se pueden usar los datos "
               "pasados para hacer inferencias.",
               "Tanto el método A como el B son razonables, pero el C es inválido porque descarta de manera "
               "arbitraria la información empírica."]),
}
PASO_MODELO = {
    1: "Recorran la gráfica de izquierda a derecha: ¿dónde sube, dónde baja? El intervalo es el tramo que "
       "solo sube.",
    2: "Antes de calcular: ¿la pregunta pide la semana del máximo o la de después? Leer qué preguntan es "
       "el primer paso.",
    3: "¿Hay una fórmula para la figura entera? No: hay una para la caja y otra para la punta.",
    4: "No pregunta qué número da, sino qué procedimiento es más seguro: hay que hacer los dos caminos.",
    5: "¿Qué palabra usa la conclusión? «Homogéneos». ¿Qué columna de la tabla mide eso?",
    6: "No hay que calcular nada: hay que decir qué supone cada método y si usa o tira los datos.",
}

# ─────────────────────────────── entrenamiento (4 por misión) ───────────────────────────────
def tabla(filas, cab=True):
    h = '<table class="dat">'
    for i, f in enumerate(filas):
        tag = "th" if (cab and i == 0) else "td"
        h += "<tr>" + "".join(f"<{tag}>{E(c)}</{tag}>" for c in f) + "</tr>"
    return h + "</table>"


def cajas(items):
    return ('<div class="cajas">' + "".join(
        f'<div class="caja"><b>{E(a)}</b>{"".join(f"<span>{E(x)}</span>" for x in b)}</div>'
        for a, b in items) + "</div>")


ICFES = {
 (1, 1): dict(e="Una empresa alquila automóviles a sus clientes de acuerdo con dos planes. Si durante una "
                "semana Juan obtuvo mayor rentabilidad con el primer plan, fue probablemente porque",
              datos=cajas([("Plan 1", ["$ 320.000 por semana", "kilometraje ilimitado"]),
                           ("Plan 2", ["$ 100.000 por semana", "más $ 2.000 por cada kilómetro"])]),
              o=["su recorrido fue menor de 110 km.", "su recorrido fue de 110 km.",
                 "su recorrido fue de 150 km.", "su recorrido fue de 100 km."], k="C",
              sol="El plan 2 cuesta 100.000 + 2.000k. Empatan cuando 320.000 = 100.000 + 2.000k → k = 110 km. "
                  "Por encima de 110 km el plan 2 sale más caro y conviene el 1: 150 km. A 100 km conviene el "
                  "plan 2 (180.000) y a 110 empatan."),
 (1, 2): dict(e="Dos ciudades E y F están separadas por una distancia h. Desde E sale un carro con velocidad "
                "constante V₁ hacia F, sin detenerse en ella; al mismo tiempo sale un segundo carro desde F "
                "con velocidad constante V₂, menor que V₁, en la misma dirección. ¿Qué información es "
                "necesaria para determinar el tiempo que transcurre entre la salida de los dos carros y el "
                "momento en que están a la misma distancia de la ciudad E?",
              fig="carros", o=["V₁ − V₂ y V₁", "h y V₁ + V₂", "V₁ + V₂ y V₁", "h y V₁ − V₂"], k="D",
              sol="A la misma distancia de E: V₁t = V₂t + h → t(V₁ − V₂) = h → t = h ÷ (V₁ − V₂). Hacen falta h "
                  "y V₁ − V₂. La suma V₁ + V₂ sirve cuando van uno contra el otro."),
 (1, 3): dict(e="Observe la siguiente secuencia numérica. El décimo término de la sucesión es 3.077 porque",
              datos='<div class="suc">' + "".join(f"<span>{x}</span>" for x in ["11", "17", "29", "53", "101", "…"]) + "</div>",
              o=["cada término se obtiene multiplicando 6 por un número primo y restando 1.",
                 "el término n-ésimo de la sucesión es de la forma 6n + 5.",
                 "al restar un término con cualquiera de los anteriores se obtiene un múltiplo de 6.",
                 "el término n-ésimo de la sucesión es de la forma 2ⁿ × 3 + 5."], k="D",
              sol="Las diferencias son 6, 12, 24, 48: se duplican. 2ⁿ × 3 + 5 da 11, 17, 29, 53, 101, y en n = 10: "
                  "1.024 × 3 + 5 = 3.077. La C es cierta pero no explica el décimo término; la B (6n + 5) falla "
                  "desde el término 3."),
 (1, 4): dict(e="La empresa de Acueducto y Alcantarillado de una ciudad liquida las cuentas de sus usuarios "
                "del estrato X con el siguiente cuadro. Si una persona necesita calcular el costo total de su "
                "recibo, debe",
              datos=tabla([("Consumo (m³)", "Acueducto", "Alcantarillado", "Aseo"),
                           ("0 a 40", "263,33", "131,66", "5.305"), ("41 a 80", "689,30", "344,65", "5.305"),
                           ("más de 80", "883,57", "441,78", "5.305"), ("Cargo fijo", "5.912", "1.401", "1.336")])
                    + '<p class="sub nota">Tarifas en pesos por metro cúbico. La de aseo y los cargos fijos son '
                      'valores fijos del mes.</p>',
              o=["sumar el cargo fijo al consumo y al alcantarillado.",
                 "multiplicar los m³ consumidos por las tarifas de acueducto y de alcantarillado, y sumar la "
                 "tarifa de aseo y los cargos fijos.",
                 "multiplicar los m³ consumidos por el costo de consumo y por el costo de alcantarillado.",
                 "multiplicar los m³ consumidos por las tarifas y sumar los cargos fijos de aseo y "
                 "alcantarillado."], k="B",
              sol="Acueducto y alcantarillado dependen de los m³ (se multiplican); aseo y cargos fijos se cobran "
                  "siempre (se suman). Solo la B incluye todo: la D olvida el cargo fijo del acueducto."),
 (2, 1): dict(e="La gráfica muestra las ganancias mensuales de una empresa durante un año. Para analizar la "
                "variabilidad de sus ganancias, la empresa compara los cuatro trimestres del año (enero-marzo; "
                "abril-junio; julio-septiembre; octubre-diciembre) por separado, y establece el rango "
                "estadístico para cada uno, que es la diferencia entre el mayor y menor valor de un grupo de "
                "datos numéricos. El menor rango estadístico se dio en el trimestre octubre-diciembre, porque",
              fig="ganancias", ancho=True,
              o=["se registraron las mayores ganancias.",
                 "las ganancias mensuales en este trimestre fueron menores que las de septiembre.",
                 "la suma de las ganancias de estos tres meses es menor que la suma de las ganancias anteriores.",
                 "se obtuvieron ganancias casi iguales en los tres meses."], k="D",
              sol="Rango de cada trimestre (mayor − menor, en millones, leído en la gráfica): ene–mar ≈ 1,8; "
                  "abr–jun ≈ 1,8; jul–sep ≈ 4,6; oct–dic ≈ 0,1. El rango es pequeño porque los tres meses "
                  "ganaron casi lo mismo, no porque hayan ganado más."),
 (2, 2): dict(e="La tabla muestra algunos datos que evidencian la relación entre dos unidades de medida de la "
                "temperatura. Una persona afirma que los datos de la columna K siempre serán mayores que los de "
                "la columna °C. ¿Es verdadera esta afirmación?",
              datos=tabla([("°C", "K"), ("−273", "0"), ("−3", "270"), ("0", "273"), ("10", "283")]),
              o=["No, porque, en la primera fila, el valor de °C es mayor que el de K.",
                 "Sí, porque la columna K es 273 unidades mayor que la columna °C.",
                 "No, porque la columna K aumenta independientemente de la columna °C.",
                 "Sí, porque, en la última fila, el valor de °C y de K son positivos."], k="B",
              sol="K − °C = 273 en las cuatro filas: K = °C + 273. Sumar un número positivo siempre da más. La A "
                  "cae en la trampa de los negativos: −273 es menor que 0."),
 (2, 3): dict(e="La figura muestra un arreglo de árboles en forma de escalera en la entrada de un vivero. El "
                "dueño del vivero afirma que los árboles son cortados de tal manera que las alturas siguen una "
                "secuencia de forma creciente, a partir de un patrón. Para poder hallar la altura a la que se "
                "debe cortar el árbol 4, ¿cuál de los siguientes valores se debe calcular primero?",
              fig="arboles", ancho=True,
              o=["La división entre las alturas de los árboles 1 y 3.",
                 "La multiplicación de la altura del primer árbol por 4.",
                 "La resta entre las alturas de dos árboles consecutivos.",
                 "La suma de las alturas de los tres primeros árboles."], k="C",
              sol="140 − 120 = 20 y 160 − 140 = 20: lo que se repite es la diferencia entre árboles seguidos. "
                  "Con ella, el árbol 4 mide 180 cm."),
 (2, 4): dict(e="En la tabla se muestra la cantidad de fotocopias y almuerzos comprados por 5 estudiantes. "
                "Para solicitar un subsidio de fotocopias, un estudiante debe comprar fotocopias por encima del "
                "promedio de fotocopias. Para solicitar el subsidio de almuerzos, debe comprar almuerzos en una "
                "cantidad mayor que el doble del promedio de almuerzos. Una persona afirma que el estudiante 2 "
                "cumple los requisitos para solicitar los dos subsidios. ¿Es verdadera esta afirmación?",
              datos=tabla([("Estudiante", "1", "2", "3", "4", "5", "Promedio"),
                           ("Fotocopias", "12", "50", "25", "25", "13", "25"),
                           ("Almuerzos", "15", "20", "10", "3", "12", "12")]),
              o=["Sí, porque los promedios de fotocopias y almuerzos son menores que las compras que realizó "
                 "el estudiante 2.",
                 "No, porque el estudiante 2 solamente puede beneficiarse del subsidio de almuerzos.",
                 "No, porque el estudiante 2 solamente puede beneficiarse del subsidio de fotocopias.",
                 "Sí, porque las compras de fotocopias y almuerzos del estudiante 2 son iguales que el "
                 "promedio de compras."], k="C",
              sol="Fotocopias: 50 > 25, cumple. Almuerzos: necesita más de 2 × 12 = 24 y compró 20, no cumple. "
                  "Solo puede pedir el de fotocopias."),
 (3, 1): dict(e="Para preparar una mezcla de cemento y arena, se debe calcular el volumen de la zona por "
                "construir (alto × largo × ancho), y posteriormente calcular la cantidad de cemento y arena por "
                "utilizar. La tabla muestra la cantidad necesaria para preparar un metro cúbico de mezcla, "
                "según su aplicación. De acuerdo con la información anterior, ¿qué cantidad de mezcla se "
                "requiere para construir un muro de dimensiones 3 m × 2 m × 0,5 m?",
              fig="muro", lado=True,
              datos=tabla([("Aplicación", "Cemento (kg)", "Arena (kg)"), ("Pisos", "35", "70"),
                           ("Techos", "30", "90"), ("Muros", "25", "75"), ("Revestimientos", "20", "100")])
                    + '<p class="sub nota">Cantidad necesaria para preparar un metro cúbico de mezcla.</p>',
              o=["105 kg de cemento y 210 kg de arena.", "90 kg de cemento y 270 kg de arena.",
                 "75 kg de cemento y 225 kg de arena.", "60 kg de cemento y 300 kg de arena."], k="C",
              sol="Volumen: 3 × 2 × 0,5 = 3 m³. Fila «Muros»: 25 kg de cemento y 75 de arena por m³ → 75 kg y "
                  "225 kg. Las otras son la misma cuenta con la fila de pisos, techos o revestimientos."),
 (3, 2): dict(e="Las sombras proyectadas por dos postes paralelos de 10 metros y 5 metros se muestran en la "
                "figura. El ángulo entre la acera horizontal y la sombra del poste 1 es α = 30°. De acuerdo con "
                "esto, se puede afirmar que el ángulo entre la acera horizontal y la sombra del poste 2 es",
              fig="postes", o=["β = 5°", "β = 15°", "β = 30°", "β = 60°"], k="C",
              sol="Los rayos del sol llegan paralelos: el ángulo de la sombra con la acera es el mismo para los "
                  "dos postes, 30°. La altura cambia el tamaño de la sombra, no su dirección."),
 (3, 3): dict(e="Cuatro locales cuadrados p, q, r y s, con medidas iguales, se instalaron alrededor de una "
                "fuente circular. Por comodidad para los turistas, se planea situar cinco bancas de forma que: "
                "cada una tenga 2 m de longitud; quedarán una seguida de la otra, entre los locales p y r; "
                "formarán una línea paralela al borde izquierdo del terreno; y mantendrán un espacio libre para "
                "paso entre las bancas y los locales. Este plan",
              fig="bancas",
              o=["es posible implementarlo, porque la longitud del lado del terreno es mayor que la medida "
                 "total de las bancas.",
                 "es posible implementarlo, porque el espacio entre los locales es suficiente para ubicar las "
                 "cinco bancas.",
                 "no es posible implementarlo, porque se debería tener la información sobre la distancia "
                 "entre las bancas y los locales.",
                 "no es posible implementarlo, porque la medida total de las cinco bancas es igual a la "
                 "distancia entre los locales."], k="D",
              sol="Cinco bancas de 2 m = 10 m, lo mismo que hay entre p y r. Caben justas, pero no queda espacio "
                  "libre para pasar, que es una de las condiciones del plan."),
 (3, 4): dict(e="Una persona elabora una vela en forma de cubo, de lado 2 cm, y coloca una cinta, que le cuesta "
                "$ x, alrededor de la vela. Cuando le encargan una vela en forma de cubo de lado 4 cm, él calcula "
                "correctamente que necesita multiplicar por 8 la cantidad de cera que debe usar, pero calcula "
                "incorrectamente que el precio de la cinta será $ 8x. ¿Cuál es el precio correcto de la cinta y "
                "por qué?",
              fig="vela",
              o=["$ 2x; porque hay exactamente dos caras que la cinta no abarca.",
                 "$ 4x; porque son cuatro caras que la cinta cubre y todas aumentan.",
                 "$ 2x; porque la cinta solo aumenta su longitud y en la nueva vela dicha longitud se duplica.",
                 "$ 4x; porque la cantidad de cera aumenta 8 veces y el lado 2 veces, y por tanto la cinta "
                 "aumenta 8 ÷ 2 = 4 veces."], k="C",
              sol="La cinta rodea el contorno: es una longitud. Si el lado pasa de 2 a 4 cm, el contorno se "
                  "duplica y la cinta cuesta 2x. La cera es un volumen: esa sí se multiplica por 8."),
 (4, 1): dict(e="El triángulo de las Bermudas está formado entre Miami, Bermuda y San Juan de Puerto Rico, con "
                "las distancias mostradas en la figura. Si una milla son 1,6 kilómetros, ¿cuál es la distancia "
                "en kilómetros que separa Miami de Bermuda en el triángulo?",
              fig="bermudas", o=["625 km.", "646,9 km.", "1.036,6 km.", "1.656 km."], k="D",
              sol="Miami–Bermuda: 1.035 millas × 1,6 = 1.656 km. La milla es más larga que el kilómetro, así que "
                  "el número en kilómetros tiene que ser mayor: eso descarta A, B y C sin calcular."),
 (4, 2): dict(e="La cosecante de un ángulo en un triángulo rectángulo se define como la razón entre la "
                "hipotenusa y el cateto opuesto al ángulo; la secante del mismo ángulo corresponde a la razón "
                "entre la hipotenusa y el cateto adyacente. ¿En cuál de los siguientes triángulos se cumple que "
                "csc θ = 1,25 y sec θ = 1,66?",
              fig="triangulos", ancho=True,
              o=["El triángulo A.", "El triángulo B.", "El triángulo C.", "El triángulo D."], k="A",
              sol="csc = hipotenusa ÷ opuesto y sec = hipotenusa ÷ adyacente. En A, θ está abajo: opuesto 12, "
                  "adyacente 9 → 15 ÷ 12 = 1,25 y 15 ÷ 9 ≈ 1,67. En B salen al revés (1,67 y 1,25); en C, "
                  "35 ÷ 21 ≈ 1,67; en D, 200 ÷ 172 ≈ 1,16."),
 (4, 3): dict(e="Un granjero quiere cultivar un terreno triangular, como se muestra en la figura. Para calcular "
                "el área del terreno, el granjero multiplica las longitudes de los catetos, y este resultado se "
                "divide entre 2. Siguiendo este procedimiento, el área del terreno es",
              fig="granjero", o=["7 m²", "6 m²", "12 m²", "10 m²"], k="B",
              sol="Los catetos (4 m y 3 m) forman la esquina recta: 4 × 3 ÷ 2 = 6 m². La hipotenusa no entra: si "
                  "se usa el 5, salen los distractores."),
 (4, 4): dict(e="Se apila una regla y una escuadra para formar el área sombreada de la figura. El área del "
                "triángulo interior es 150 cm² y el área cubierta por la regla y la escuadra, incluido el "
                "triángulo interior, es 850 cm². Una persona calcula el ancho x de la regla así: Paso 1, halla "
                "el área de la región sombreada: 850 − 150 = 700 cm². Paso 2, calcula el área del triángulo "
                "grande: (30 × 40) ÷ 2 = 600 cm². Paso 3, plantea 700 − 600 = 100 cm² = 50x. Paso 4, concluye "
                "que x = 100 ÷ 50 = 2 cm. Este procedimiento es incorrecto porque",
              fig="regla",
              o=["el área del triángulo grande se debe calcular efectuando la multiplicación 30 × 40 cm².",
                 "al despejar la ecuación planteada, el valor de x corresponde a 100 − 50 cm.",
                 "el área del triángulo grande ya incluye el área del triángulo interior, por tanto el área de "
                 "la regla es 850 − 600 = 250 cm².",
                 "la ecuación que se debe plantear con el área de la regla está incompleta; debería ser "
                 "150 cm² = 50x ÷ 2."], k="C",
              sol="Los 850 cm² ya incluyen el hueco, y el triángulo grande (600 cm²) también. El paso 1 quita el "
                  "hueco y el paso 3 lo vuelve a quitar. La regla mide 850 − 600 = 250 cm² y x = 250 ÷ 50 = 5 cm."),
 (5, 1): dict(e="La tabla muestra el promedio y el rango de ventas de algunos productos de una cafetería los "
                "fines de semana. Según la información de la tabla, ¿cuál es el producto que, en promedio, se "
                "vende menos en un fin de semana en la cafetería?",
              datos=tabla([("Producto", "Promedio de ventas", "Rango de ventas"), ("Café", "30", "18"),
                           ("Buñuelo", "24", "20"), ("Pandebono", "20", "26"), ("Pandeyuca", "32", "22")]),
              o=["Buñuelo.", "Pandebono.", "Café.", "Pandeyuca."], k="B",
              sol="«En promedio» manda a la columna del promedio: el menor es pandebono (20). El rango no dice "
                  "cuánto se vende sino qué tan disparejas son las ventas."),
 (5, 2): dict(e="En un barrio donde hay 1.000 casas de estratos 1 y 2, se realizó una encuesta para conocer las "
                "casas que tienen conexión a internet. De las 350 casas de estrato 1, solamente 20 tienen "
                "conexión a internet, y 550 de las casas de estrato 2 tienen conexión a internet. ¿Cuál es la "
                "probabilidad de que al elegir una casa al azar, esta NO tenga conexión a internet?",
              o=["100 / 1.000", "330 / 1.000", "430 / 1.000", "570 / 1.000"], k="C",
              sol="Sin conexión: estrato 1, 350 − 20 = 330; estrato 2, 650 − 550 = 100; total 430. La "
                  "probabilidad es 430/1.000. La B solo cuenta el estrato 1; la D cuenta las que sí tienen."),
 (5, 3): dict(e="Los resultados de una encuesta sobre sexo y edad de cada uno de los estudiantes de un curso se "
                "muestran en la tabla. El profesor afirma que la probabilidad de seleccionar un estudiante de 15 "
                "años de edad entre el grupo de los hombres es igual a 2/5, porque hay 2 hombres de 15 años de "
                "edad en el curso de 5 estudiantes. La interpretación del profesor es errada, porque",
              datos=tabla([("Estudiante", "1", "2", "3", "4", "5"), ("Sexo", "H", "M", "H", "H", "M"),
                           ("Edad", "15 años", "17 años", "17 años", "15 años", "15 años")]),
              o=["le falta considerar una persona en el cálculo realizado.",
                 "todos los estudiantes de 15 años de edad son hombres.",
                 "considera más personas de las que requiere para el cálculo.",
                 "solo debe tener en cuenta la población de 15 años de edad."], k="C",
              sol="Entre los hombres (3: estudiantes 1, 3 y 4) los de 15 años son 2: la probabilidad es 2/3. El "
                  "profesor dividió entre los 5 del curso, es decir, metió a las mujeres en el total."),
 (5, 4): dict(e="Los valores dominantes en un conjunto de datos son aquellos que aparecen con mayor frecuencia, "
                "siempre y cuando dicha frecuencia sea mayor o igual que dos. Para hallarlos se cuenta cuántas "
                "veces aparece cada dato y se seleccionan los que más se repiten, con al menos dos apariciones. "
                "¿Para cuál o cuáles de los datos de la tabla es posible determinar los valores dominantes con "
                "ese procedimiento?",
              datos=tabla([("Peso (kg)", "22", "26", "29", "35", "41"),
                           ("Estatura (m)", "1,25", "1,28", "1,28", "1,34", "1,42"),
                           ("Edad (años)", "9", "10", "11", "11", "12")], cab=False)
                    + '<p class="sub nota">Datos de un curso de 5 estudiantes.</p>',
              o=["Únicamente para edad.", "Únicamente para peso.", "Para edad y para estatura.",
                 "Para peso y para estatura."], k="C",
              sol="Peso: ningún dato se repite. Estatura: 1,28 aparece dos veces. Edad: 11 aparece dos veces. El "
                  "método sirve para edad y estatura."),
 (6, 1): dict(e="Pedro tiene un candado que se abre al colocar una contraseña de dos números diferentes del 0 "
                "al 9. Pedro quiere saber cuántas contraseñas posibles se pueden ensayar en el candado, y para "
                "ello propone tres procedimientos. ¿Cuál o cuáles procedimientos permiten determinar "
                "correctamente el total de combinaciones posibles?",
              datos=cajas([("Procedimiento 1", ["10! ÷ 8!"]), ("Procedimiento 2", ["10² + 9²"]),
                           ("Procedimiento 3", ["10 × 9"])]),
              o=["1 y 3 solamente.", "2 y 3 solamente.", "1 solamente.", "2 solamente."], k="A",
              sol="Importa el orden y no se repite: 10 opciones para el primero y 9 para el segundo, 10 × 9 = 90. "
                  "10! ÷ 8! = 10 × 9 = 90 también. 10² + 9² = 181 no cuenta nada."),
 (6, 2): dict(e="Para saber la cantidad de códigos de 4 cifras, donde los dígitos se pueden repetir, que pueden "
                "usarse para identificar a los estudiantes de un colegio, se propone el siguiente procedimiento. "
                "¿Cuántos dígitos se pueden obtener con este conjunto usando el procedimiento anterior?",
              datos=cajas([("Paso 1", ["contar cuántos números tiene el conjunto de dígitos elegido"]),
                           ("Paso 2", ["elevar a la 4 el resultado del paso 1"])])
                    + '<p class="enun2">Colegio de 600 estudiantes · conjunto elegido: { 1, 2, 3, 4, 5 }</p>',
              o=["5", "75", "625", "3.125"], k="C",
              sol="El conjunto {1, 2, 3, 4, 5} tiene 5 dígitos; 5⁴ = 625 códigos. El dato de 600 estudiantes "
                  "solo sirve para ver que alcanzan. La pregunta dice «dígitos» pero el procedimiento cuenta "
                  "códigos: se responde lo que el procedimiento calcula."),
 (6, 3): dict(e="Se presentan para la gobernación de un departamento varios candidatos; los de mayor opción son "
                "Pérez y Gómez. Las gráficas muestran los últimos sondeos entre los electores habilitados. Si "
                "solo votan los que dijeron que sí votarían, y la predicción de la encuesta se cumple, la "
                "gobernación la ganará el candidato Pérez con un total de",
              datos=cajas([("El departamento", ["Población: 1.200.000", "Electores habilitados: 250.000"]),
                           ("¿Piensa usted votar?", ["Sí: 50 %", "No: 40 %", "Ns/Nr: 10 %"]),
                           ("¿Por quién votará?", ["Pérez: 42 %", "Gómez: 41 %", "Otros: 17 %"])]),
              o=["52.500 votos; con 2.500 votos por encima del otro candidato.",
                 "102.500 votos; con una diferencia de 2.000 votos.",
                 "52.500 votos; 1.250 votos más que el otro candidato.",
                 "102.500 votos; 1.500 votos por encima del otro candidato."], k="C",
              sol="Votan los que dijeron sí: 50 % de 250.000 = 125.000. Pérez: 42 % de 125.000 = 52.500; Gómez: "
                  "41 % = 51.250. Diferencia: 1.250. Las opciones de 102.500 toman los 250.000 como total."),
 (6, 4): dict(e="El administrador de una librería debe registrar en una tabla la cantidad de libros que vende "
                "cada mes, pero olvidó registrar las ventas del segundo mes. Con la información de la tabla, "
                "¿cuál de los siguientes datos se puede determinar?",
              datos=tabla([("Mes", "1", "2", "3", "4", "5", "6"), ("Libros", "124", "?", "124", "368", "124", "231")]),
              o=["El promedio mensual de libros vendidos durante los últimos 6 meses.",
                 "El rango de la cantidad de libros vendidos durante los últimos 6 meses.",
                 "La moda de la cantidad de libros vendidos durante los últimos 6 meses.",
                 "La mediana de la cantidad de libros vendidos durante los últimos 6 meses."], k="C",
              sol="La moda es 124 pase lo que pase en el mes 2: ya aparece tres veces y cualquier otro valor "
                  "aparecería a lo sumo dos. El promedio y el rango cambian con el dato que falta, y la mediana "
                  "también (124 si el mes 2 es pequeño; 177,5 si es grande)."),
}


# ─────────────────────────────── el planeador, adaptado ───────────────────────────────
def planeador():
    """plan_mate con los nombres que espera clase_viva.py. Las estrategias, en el orden del cuaderno."""
    ns = types.SimpleNamespace()
    ns.FASES = P.FASES
    ns.MISIONES = {m: dict(comp=d["comp"], pags=d["pags"], estr=ESTR[m],
                           competencia="4 estrategias · 10 preguntas del libro · 4 de entrenamiento",
                           cierre=d["clave_est"]) for m, d in P.MISIONES.items()}
    ns.TALLER = P.TALLER
    ns.DINAMICAS = P.DINAMICAS
    ns.RETOS = P.RETOS
    ns.AVISOS = {}
    ns.SELLOS = []
    ns.BANCO = P.BANCO
    return ns


COMPONENTES = [("Numérico-variacional", "momentos 1 y 2 · 8 preguntas", "var(--m2)"),
               ("Espacial-métrico", "momentos 3 y 4 · 8 preguntas", "var(--m4)"),
               ("Aleatorio", "momentos 5 y 6 · 8 preguntas", "var(--m6)")]

UI = dict(
    portada_decir=["«Libro abierto, cuaderno cerrado, lápiz. Esfero no: hoy vamos a equivocarnos por "
                   "escrito, y eso se corrige con borrador.»"],
    regla_lead="Si el instrumento está vacío, no resolviste: adivinaste.",
    regla_p=("Primero se escribe el instrumento —la tabla, la cuenta, el dibujo—, después se marca la "
             "opción. Una respuesta correcta con el instrumento en blanco no cuenta como resuelta."),
    regla_decir=["«Si marcas sin llenar, para mí esa pregunta está en blanco, aunque esté bien.»",
                 "Pasa por los puestos mirando el instrumento, no la respuesta."],
    regla_apoyo=["Si alguien pregunta para qué escribir si ya sabe la respuesta: porque en la prueba nadie "
                 "le va a decir si acertó, y la única manera de saberlo es tener la cuenta en el papel.",
                 "Tú no tienes que resolver nada en este momento: tu trabajo es verificar que estén "
                 "escribiendo. Ese registro es lo que la coordinación revisa después."],
    dina_decir=["«Esto no es recreo: es el mismo movimiento que van a hacer con la pregunta en cinco "
                "minutos, pero con el cuerpo.»"],
    bloque_decir=["«Antes de marcar: ¿qué escribieron en el instrumento? Léanme la cuenta.»",
                  "Si alguien se traba, pregúntale en qué casilla del instrumento se quedó. No le des la "
                  "respuesta: devuélvelo a su hoja."],
    reto_defensa=("<b>La defensa:</b> tres minutos por equipo, citando un dato o una cuenta. «Porque se ve "
                  "así» no cuenta."),
    reto_apoyo=["El reto se gana con el dato que sostiene la decisión, no con llegar primero. Si dos equipos "
                "llegan a respuestas distintas bien sostenidas, dilo: también es hacer matemáticas.",
                "Si un equipo entrega una sola hoja para los tres, el reto no cuenta. La discusión es "
                "compartida; el registro es individual.",
                "Cierra señalando en qué se parecían los razonamientos y en qué no."],
    c7_h1="Hoy nadie les va a decir si acertaron",
    c7_lead=("Veinticuatro preguntas tipo Saber 11, seguidas, como en la prueba: las de las seis franjas de "
             "entrenamiento. Lo único que llevan es lo que entrenaron: la cuenta en el papel antes de "
             "marcar."),
    c7_decir=["«Tapen con una hoja la columna del instrumento: hoy trabajan sin andamiaje, como en la prueba "
              "real. Pueden hacer cuentas en el margen.»"],
    c7_reglas=["En silencio y en filas individuales.", "No se responde ninguna duda, ni de vocabulario.",
               "Las dudas se escriben en el margen.", "La columna del instrumento queda tapada.",
               "Cada cuenta se escribe al margen antes de marcar."],
    c7_apoyo_reglas=["Anota quién marca sin escribir ninguna cuenta: es el dato más útil del simulacro, más "
                     "que el puntaje."],
    c7_competencias=COMPONENTES,
    c8_h1="Lo que escribiste esta vez",
    c8_lead=("Hoy no hay pregunta nueva. Hoy vamos a poner tu instrumento de hace seis semanas al lado de lo "
             "que escribiste en el simulacro."),
    c8_apoyo_elegir=["Si dudas entre dos, quédate con la del componente que más manos tuvo en el conteo de la "
                     "clase 7."],
    c8_h2="¿Qué cuenta hiciste esta vez que antes no hiciste?",
    c8_decir=["«Pongan las dos hojas una al lado de la otra. ¿Qué escribieron distinto?»"],
    c8_apoyo=["Si nadie escribió distinto, la estrategia no se instaló todavía: anótalo en el registro para el "
              "reporte de los especialistas."],
)


def area(mis):
    A = CV.Area(nombre=NOMBRE, prefijo="MAT", fuerte=FUERTE, color=CV.color_de(NOMBRE), P=planeador(),
                claves_libro=lambda m: CLAVE[m], preguntas_icfes=lambda m: [ICFES[(m, k)] for k in range(1, 5)],
                textos={}, out=OUT, titulos=TITULOS, leads=LEADS, est_col=EST_COL[mis],
                colores=COLORES, textos_ui=dict(UI, portada_libro=(
                    f"Las diez preguntas de la prueba de campo, páginas {LIBRO[mis][0]} a {LIBRO[mis][1]}")),
                apoyo_fuerte="Matemáticas no es tu área")
    return A


# ─────────────────────────────── escenas propias de Matemáticas ───────────────────────────────
def figura(nombre):
    return f'<div class="fig">{F.FIG[nombre]()}</div>' if nombre else ""


def guia_fase(A, fase, decir=(), apoyo=()):
    return CV.guia(A, fase, decir=decir, apoyo=apoyo)


def avisos_planeador(mis):
    """plan_mate.AVISOS → {pregunta: [(severidad, qué pasa, qué hace el profe)]}"""
    out = {}
    for preg, sev, que, hacer in P.AVISOS.get(mis, []):
        for n in map(int, re.findall(r"\d+", preg)):
            out.setdefault(n, []).append((sev, que, hacer))
    return out


def apoyo_portada(mis):
    d = P.MISIONES[mis]
    out = ["⚑ Antes del sábado, lo que tienes que instalar: " + d["instala"],
           "Ojo con esto: " + d["ojo"]]
    for preg, sev, que, hacer in P.AVISOS.get(mis, []):
        out.append(f"Aviso del libro, {preg} ({sev}): {que} Qué haces: {hacer}")
    if mis == 6:
        out.append("Ojo con la numeración: el planeador impreso llama E1 a «Juzgar el procedimiento»; en el "
                   "cuaderno del estudiante es la estrategia 3. Esta guía usa siempre el número del cuaderno, "
                   "que es el que ven ellos.")
    out.append("Lo que tienes que poder explicar hoy en dos minutos, sin jerga. Si un estudiante lo sabe "
               "mejor que tú, déjalo explicar y pide que lo muestre con un número:")
    out += FUERTE_MIS[mis]
    return out


def esc_activacion(A, mis):
    filas, mas, pista = ACTIVACION[mis]
    cab = "".join(f"<th>{E(c)}</th>" for c in filas[0])
    cuerpo = "".join("<tr><th>" + E(f[0]) + "</th>" + "".join(f"<td>{E(c)}</td>" for c in f[1:]) + "</tr>"
                     for f in filas[1:])
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m1)">Activación</span>'
         f'<span class="kicker">Cuaderno cerrado</span></div>'
         f'<h2>¿Qué está cambiando aquí, y respecto a qué?</h2>'
         f'<p class="lead">Unos números en una tabla. Nadie dice todavía de qué son.</p>'
         f'<table class="dat act"><thead><tr>{cab}</tr></thead><tbody id="datos{mis}" hidden>{cuerpo}</tbody></table>'
         f'<p class="lead mt">{E(mas)}</p>'
         f'<div class="ctl"><button class="btn" data-show="datos{mis}">Destapar los datos</button>'
         f'<button class="btn" data-show="pista{mis}">Mostrar la pista</button></div>'
         f'<div class="note" id="pista{mis}" hidden style="--accent:var(--m1)"><b>De dónde salen:</b> {E(pista)}</div>')
    return dict(m=0, html=h, guia=guia_fase(A, 0, decir=[
        "Destapa los datos y haz una sola pregunta: «¿qué está cambiando aquí, y respecto a qué?». Anota en el "
        "tablero tres respuestas distintas sin calificar ninguna.",
        "Después, la segunda pregunta de la pantalla."], apoyo=[
        "No tienes que explicar nada en este momento. Si alguien dice «función», «pendiente» o «variable», no "
        "lo confirmes ni lo niegues: «anótalo, volvemos a eso».",
        "Los datos son inventados para la clase: no salen del libro. Dilo si te lo preguntan.",
        "La pista es para el cierre de los 15 minutos, no para el principio: " + pista]))


def esc_dinamica(A, mis, i, fase):
    """Dinámica i del planeador (en su orden), con el número y el color de su estrategia en el cuaderno."""
    nom, mins, pasos, entrena, material = P.DINAMICAS[mis][i]
    est = P.MISIONES[mis]["estr"][i]
    n, c = num_est(mis, est), col_est(mis, est)
    lis = "".join(f'<li>{E(p)}</li>' for p in pasos)
    h = (f'<div class="eyebrow"><span class="min" style="--accent:{c}">Dinámica · {mins} min</span>'
         f'<span class="kicker">Entrena la estrategia {n} · {E(est)}</span></div>'
         f'<h2>{E(nom)}</h2>'
         f'<div class="grid c2 mt"><div class="card edge" style="--accent:{c}">'
         f'<h3>Cómo se hace</h3><ol class="pasos">{lis}</ol></div>'
         f'<div class="card"><h3>Qué vas a necesitar</h3><p>{E(material)}</p>'
         f'<h3 class="mt">Qué entrena</h3><p>{E(entrena)}</p></div></div>')
    return dict(m=fase, min=mins, html=h, guia=guia_fase(A, fase, decir=list(UI["dina_decir"]), apoyo=[
        "Qué movimiento mental entrena: " + entrena,
        "La regla para aprobar cualquier dinámica: si no puedes decir qué paso de la estrategia está "
        "ejercitando, es recreo, no clase.",
        f"Es la dinámica de la estrategia {n} del cuaderno, «{est}». Al terminar, di el nombre en voz alta: "
        "es el mismo que el estudiante ve en el chip de su hoja."]))


def opciones(ident, o, cols2=False):
    ops = "".join(f'<div class="op" data-op="{L}"><span class="L">{L}</span><span>{E(x)}</span></div>'
                  for L, x in zip("ABCD", o))
    return f'<div class="ops{" c2" if cols2 else ""}" id="{ident}">{ops}</div>'


def esc_problematizadora(A, mis):
    q = MODELO[mis]
    pag = PAG[mis][1]
    clave = CLAVE[mis][1].split(" · ")[0]
    botones = "".join(f'<button class="btn tally" data-tally="h{mis}{L}">{L} <span class="n" id="h{mis}{L}">0</span></button>'
                      for L in "ABCD")
    datos = figura(q.get("fig")) + (tabla(q["tabla"]) if q.get("tabla") else "")
    corta = all(len(x) < 30 for x in q["o"])
    ident = f"mod{mis}"
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m2)">Pregunta problematizadora</span>'
         f'<span class="membrete">Libro · pregunta 1 · página {pag}</span></div>'
         f'<h2>Abran el libro en la página {pag}</h2>'
         f'<div class="grid c2 mt modelo"><div class="card">'
         f'<p>{E(q["info"])}</p>{datos}</div>'
         f'<div><p class="enun">{E(q["e"])}</p>{opciones(ident, q["o"], corta)}'
         f'<div class="ctl"><span class="sub manos">Antes de analizar, manos:</span>{botones}<button class="btn" data-reset="h{mis}">↺</button>'
         f'<button class="btn" data-clave="{ident}" data-k="{clave}">Revelar la clave</button></div>'
         f'<div class="note" style="--accent:var(--m2)"><b>La regla de este momento:</b> nadie justifica '
         f'diciendo «porque se ve así». Cada intervención nombra un dato: un valor, un punto de la gráfica, '
         f'una cuenta.</div></div></div>')
    av = [f"Aviso del libro ({s}): {que} Qué haces: {hacer}" for s, que, hacer in avisos_planeador(mis).get(1, [])]
    return dict(m=1, html=h, guia=guia_fase(A, 1, apoyo=[
        "Cuenta las manos con los botones antes de cualquier análisis. El número queda en pantalla: al final "
        "del momento vuelves a él y el grupo ve cuántos cambiaron de opinión al hacer la cuenta.",
        "Primer paso en voz alta: " + PASO_MODELO[mis],
        f"La clave es la {CLAVE[mis][1]}. Cómo se llega: {SOL[(mis, 1)]}",
        "Revélala solo al final de los 20 minutos, después del análisis de distractores: el botón es para "
        "ese momento. En el bloque de las preguntas 1 y 2 la vuelven a trabajar en su instrumento."] + av))


def esc_bloque(A, mis, a, b_):
    taller = {p: (e, i, c) for p, e, i, c in P.TALLER[mis]}
    avp = avisos_planeador(mis)
    partes, apoyo = [], []
    for n in (a, b_):
        est, ins, ctx = taller[n]
        k, c = num_est(mis, est), col_est(mis, est)
        clave = CLAVE[mis][n]
        av = ""
        if (mis, n) in PROYECTAR:
            sev, txt = PROYECTAR[(mis, n)]
            av = (f'<div class="aviso sev-{E(sev[:4])}" hidden data-grupo="k{mis}{a}">'
                  f'<b>Ojo con esta clave:</b> {E(txt)}</div>')
        doble = " doble" if "·" in clave else ""
        partes.append(
            f'<div class="card edge" style="--accent:{c}">'
            f'<div class="eyebrow"><span class="membrete">Libro · pregunta {n} · página {PAG[mis][n]}</span>'
            f'<span class="min" style="--accent:{c}">E{k} · {E(est)}</span></div>'
            f'<p class="sub">{E(ctx)}</p>'
            f'<h3 style="color:{c}">{E(ins)}</h3>'
            f'<p class="inst">{E(LEAD[(mis, n)])}</p>'
            f'<div class="clave" hidden data-grupo="k{mis}{a}"><span class="keychip{doble}" '
            f'style="background:{c}">{E(clave)}</span> {"son las claves" if doble else "es la clave"} del libro</div>'
            f'{av}</div>')
        apoyo.append(f"Pregunta {n} · clave {clave}. Cómo se llega: {SOL[(mis, n)]}")
        for sev, que, hacer in avp.get(n, []):
            apoyo.append(f"Pregunta {n} · aviso del libro ({sev}): {que} Qué haces: {hacer}")
        if (mis, n) in AVISO_NUEVO:
            apoyo.append(f"Pregunta {n} · {AVISO_NUEVO[(mis, n)]}")
    en_pantalla = (a == 1)
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m3)">Desarrollo guiado · '
         f'preguntas {a} y {b_}</span><span class="kicker">'
         f'{"En pantalla, casilla por casilla" if en_pantalla else "En el cuaderno, cada uno el suyo"}</span></div>'
         f'<h2>Preguntas {a} y {b_}: primero el instrumento, después la opción</h2>'
         f'<div class="grid c2 mt">{"".join(partes)}</div>'
         f'<div class="ctl"><button class="btn" data-showgrupo="k{mis}{a}">Revelar las claves</button></div>')
    apoyo.insert(0, f"Las claves del libro son {a}·{CLAVE[mis][a]} y {b_}·{CLAVE[mis][b_]}. No las reveles "
                    "hasta que todos tengan el instrumento escrito: el botón es para el cierre del bloque.")
    if en_pantalla:
        apoyo.insert(1, "Este bloque se hace en el tablero, casilla por casilla del instrumento, con todo el "
                        "grupo: es el modelo de cómo se llenan las demás hojas.")
    return dict(m=2, min=7, html=h, guia=guia_fase(A, 2, decir=list(UI["bloque_decir"]), apoyo=apoyo))


def esc_icfes(A, mis, k):
    q = ICFES[(mis, k)]
    fila = P.BANCO[mis][k - 1]
    _, est, ins, _ = P.INS_ICFES[mis][k - 1]
    n, c = num_est(mis, est), col_est(mis, est)
    ident = f"icf{mis}{k}"
    datos = figura(q.get("fig")) + q.get("datos", "")
    if q.get("lado"):
        datos = f'<div class="lado">{datos}</div>'
    corta = all(len(x) < 34 for x in q["o"])
    pie = (f'<div class="ctl"><button class="btn" data-clave="{ident}" data-k="{q["k"]}">Revelar la clave</button></div>')
    cab = (f'<div class="eyebrow"><span class="membrete">{E(MEMBRETE)}</span>'
           f'<span class="min" style="--accent:var(--m5)">Evaluación individual · pregunta {k}</span>'
           f'<span class="min" style="--accent:{c}">E{n} · {E(est)}</span></div>')
    if q.get("ancho"):
        h = (cab + f'<p class="enun mt">{E(q["e"])}</p>{datos}'
             f'{opciones(ident, q["o"], True)}{pie}')
    else:
        h = (cab + f'<div class="grid c2 icfes mt"><div><p class="enun">{E(q["e"])}</p>{datos}</div>'
             f'<div>{opciones(ident, q["o"], corta)}{pie}</div></div>')
    apoyo = [f"La clave es la {q['k']}. Cómo se llega: {q['sol']}",
             f"En el cuaderno la trabajan con el instrumento «{ins}» (estrategia {n} · {est})."]
    if "ASED" in fila.get("fuente", ""):
        apoyo.insert(0, "⚑ Fuente: compilado ASED (no es del ICFES). No la presentes como pregunta del ICFES; "
                        "Nelson decide si se reemplaza.")
    return dict(m=4, html=h, guia=guia_fase(A, 4, decir=[
        "Durante la evaluación no se proyecta nada: las preguntas están en el cuaderno. Esta diapositiva es "
        "para el cierre, cuando se socializan las falladas.",
        "«¿Qué cuenta escribiste antes de mirar las opciones?»"], apoyo=apoyo))


def escenas_contenido(mis):
    A = area(mis)
    sc = [CV.esc_portada(A, mis), CV.esc_reglas(A, mis), esc_activacion(A, mis),
          esc_dinamica(A, mis, 0, 0), esc_problematizadora(A, mis)]
    sc[0]["guia"]["apoyo"] = apoyo_portada(mis) + sc[0]["guia"]["apoyo"]
    for j, (a, b_) in enumerate([(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]):
        sc.append(esc_bloque(A, mis, a, b_))
        if j in (1, 2, 3):                       # cada 18 minutos, la dinámica del bloque (como el motor)
            sc.append(esc_dinamica(A, mis, j, 2))
    sc.append(CV.esc_reto(A, mis))
    sc[-1]["guia"]["apoyo"].insert(0, "El reto es el del planeador (banco de dinámicas, hoja de la misión "
                                      f"{mis}): {P.RETOS[mis][2]}")
    for k in range(1, 5):
        sc.append(esc_icfes(A, mis, k))
    cierre = CV.esc_cierre(A, mis)
    viejo = "La palabra nueva del día, en la franja de vocabulario, con tus palabras."
    assert viejo in cierre["html"]
    cierre["html"] = cierre["html"].replace(
        viejo, "La palabra que te frenó hoy, en «Palabras que me frenaron», con tus palabras.")
    cierre["guia"]["apoyo"].insert(0, "Pide que dos o tres lean en voz alta su salvavidas: la ruta mínima que "
                                      "los habría salvado en la pregunta que fallaron.")
    sc.append(cierre)
    return A, sc


def escenas_simulacro():
    A = area(2)
    sc7 = CV.escenas_clase7(A)
    ased = [f"M{m}·P{k}" for m in range(1, 7) for k, f in enumerate(P.BANCO[m], 1) if "ASED" in f.get("fuente", "")]
    sc7[0]["guia"]["apoyo"].append(
        f"⚑ {len(ased)} de las 24 ({', '.join(ased)}) salen del compilado ASED, no del ICFES. Nelson decide si "
        "se reemplazan antes de imprimir.")
    sc7[2]["html"] = (sc7[2]["html"].replace("Conteo por competencia", "Conteo por componente")
                      .replace("preguntas de cada competencia", "preguntas de cada componente"))
    sc7[2]["guia"]["obj"] = "Que el grupo vea en cuál de los tres componentes se le va el puntaje."
    sc7[2]["guia"]["apoyo"] = [
        "Se cuenta por componente, como dice el planeador: numérico-variacional (franjas de los momentos 1 y "
        "2), espacial-métrico (3 y 4) y aleatorio (5 y 6). Ocho preguntas en cada uno.",
        "Cada estudiante cuenta sus aciertos por componente y los escribe en la portada del área; tú cuentas "
        "las manos de quienes fallaron más de la mitad en cada uno.",
        "Anota los tres números: son el dato que la coordinación necesita para decidir el refuerzo."]
    todas = [(m, k, re.split(r" · ", f["contexto"])[0][:46]) for m in range(1, 7) for k, f in enumerate(P.BANCO[m], 1)]
    sc8 = CV.escenas_clase8(A, todas)
    sc8[1]["guia"]["decir"] = ["Usa los tres números del conteo por componente de la clase 7."]
    sc8[1]["guia"]["apoyo"].append("Cada pregunta se repara con el instrumento con el que se trabajó la primera "
                                   "vez: el estudiante tiene que volver a esa página de su cuaderno (franjas de "
                                   "entrenamiento: páginas 13, 17, 20, 24, 27, 31, 34, 38, 41, 45, 48 y 52).")
    sc8[-1]["guia"]["apoyo"] = [a.replace("la franja de vocabulario completa",
                                          "la franja «Palabras que me frenaron» completa") for a in sc8[-1]["guia"]["apoyo"]]
    return A, sc7, sc8


# ─────────────────────────────── escribir ───────────────────────────────
CSS = """
.dat{border-collapse:collapse;margin-top:10px;font-size:.95em;background:var(--paper)}
.dat th,.dat td{border:1px solid var(--line);padding:6px 14px;text-align:center}
.dat th{background:#EEF3FA;font-weight:700}
.dat.act{font-size:1.15em;margin-top:0}.dat.act td,.dat.act th{min-width:4.2em;padding:8px 16px}
.dat td.q{color:var(--faint);font-weight:700}
.fig{background:var(--paper);border:1px solid var(--line);border-radius:14px;padding:10px 14px;margin-top:10px}
.fig svg{display:block;width:100%;height:auto;margin:0 auto}
.fig text{font-family:var(--text)}
.ops.c2{grid-template-columns:1fr 1fr}
.modelo{font-size:.9em}.manos{align-self:center}.modelo .card p{margin-top:0}
.lado{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-start}.lado .fig{flex:1 1 260px}.lado .dat{flex:0 0 auto}
.inst{font-style:italic;color:var(--muted)}
.nota{font-size:.85em;margin-top:4px}
.enun2{font-weight:600;margin-top:10px}
.cajas{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}
.caja{flex:1 1 200px;background:var(--paper);border:1px solid var(--line);border-left:5px solid var(--m5);border-radius:10px;padding:8px 14px}
.caja b{display:block;font-family:var(--display)}.caja span{display:block}
.suc{display:flex;flex-wrap:wrap;gap:10px;margin-top:10px}
.suc span{min-width:3.6em;text-align:center;font-family:var(--display);font-weight:800;font-size:1.4em;background:var(--paper);border:1.5px solid var(--line);border-radius:10px;padding:8px 12px}
.keychip.doble{width:auto;padding:0 .45em}
"""

PROHIBIDOS = ["Petro", "Uribe", "Duque", "Santos", "Pastrana", "Gaviria", "Samper", "Benedetti",
              "Vargas Lleras", "Fajardo", "Claudia López", "Cepeda", "Turbay", "Galán", "Bolívar Moreno"]


def revisar(html, archivo):
    hay = [n for n in PROHIBIDOS if re.search(r"\b" + re.escape(n) + r"\b", html)]
    if hay:
        raise SystemExit(f"{archivo}: trae nombres que no pueden salir: {hay}")
    if re.search(r"oficial", html, re.I):
        raise SystemExit(f"{archivo}: dice «oficial»: " + re.search(r".{60}oficial.{60}", html, re.I | re.S).group(0))


# Texto del planeador y del motor que nombra al ICFES donde ahora va «Saber 11» o «de entrenamiento»
# (decisión de Nelson, 10 nov). plan_mate.py no se toca: el cambio se hace al escribir la guía.
MEMBRETE_TXT = [
    ("¿En qué se parecía la pregunta del ICFES a la de tu libro?",
     "¿En qué se parecía la pregunta Saber 11 a la de tu libro?"),
    ("la pregunta del libro y la del ICFES", "la pregunta del libro y la de entrenamiento"),
    ("una pregunta del ICFES no se resuelve", "una pregunta tipo Saber 11 no se resuelve"),
    ("preguntas reales del ICFES", "preguntas tipo Saber 11"),
    ("y de la del ICFES sobre", "y de la de entrenamiento sobre"),
    ("Las cuatro ICFES de este momento", "Las cuatro preguntas de entrenamiento de este momento"),
    ("más aparece en el ICFES de este componente", "más aparece en Saber 11 en este componente"),
    ("hojas de entrenamiento ICFES", "hojas de entrenamiento"),
    ("Entrenamiento ICFES", "Entrenamiento"),
]


def escribir(A, archivo, titulo, sub, sc, out):
    html = CV.pagina(A, titulo, sub, sc, titulo).replace("</style>", CSS + "</style>", 1)
    for a, b_ in MEMBRETE_TXT:
        html = html.replace(a, b_)
    revisar(html, archivo)
    f = os.path.join(out, archivo)
    with open(f, "w", encoding="utf-8") as fh:
        fh.write(html)
    print(f"{archivo:30s} {len(sc):2d} diapositivas · {os.path.getsize(f)//1024} KB")
    return f


def verificar():
    """Las claves que se proyectan tienen que ser las verificadas."""
    malas = []
    for m in range(1, 7):
        if len(CLAVE[m]) != 10:
            malas.append(f"M{m}: {len(CLAVE[m])} claves del libro")
        for n in range(1, 11):
            if (m, n) not in SOL or (m, n) not in LEAD:
                malas.append(f"M{m} P{n}: falta camino o instrucción")
        for k in range(1, 5):
            fila = P.BANCO[m][k - 1]
            if fila["clave"].strip() != ICFES[(m, k)]["k"]:
                malas.append(f"M{m} ICFES {k}: icfes.csv {fila['clave']} · guía {ICFES[(m, k)]['k']}")
            if P.INS_ICFES[m][k - 1][3][:30] != ICFES[(m, k)]["e"][:30]:
                malas.append(f"M{m} ICFES {k}: el enunciado no es el de instrumentos.csv")
        for p, e, i, c in P.TALLER[m]:
            if e not in ESTR[m]:
                malas.append(f"M{m} P{p}: estrategia {e} no está en el cuaderno")
    if malas:
        raise SystemExit("No coincide:\n  " + "\n  ".join(malas))


def construir(out=OUT):
    os.makedirs(out, exist_ok=True)
    verificar()
    hechos = []
    for mis in range(1, 7):
        A, sc = escenas_contenido(mis)
        d = P.MISIONES[mis]
        hechos.append(escribir(A, f"MAT_Clase{mis}_Mision{mis}.html", f"{NOMBRE} · Clase {mis}",
                               f"Momento {mis} · {d['comp']} · páginas {d['pags']}", sc, out))
    A, sc7, sc8 = escenas_simulacro()
    hechos.append(escribir(A, "MAT_Clase7_Simulacro.html", f"{NOMBRE} · Clase 7",
                           "Simulacro del área · 24 preguntas", sc7, out))
    hechos.append(escribir(A, "MAT_Clase8_Devolucion.html", f"{NOMBRE} · Clase 8",
                           "Devolución y cierre del área", sc8, out))
    with zipfile.ZipFile(ZIP, "w", zipfile.ZIP_DEFLATED) as z:
        for f in hechos:
            z.write(f, os.path.basename(f))
    print("zip:", os.path.relpath(ZIP, AQUI), f"{os.path.getsize(ZIP)//1024} KB")
    return hechos


if __name__ == "__main__":
    construir(sys.argv[1] if len(sys.argv) > 1 else OUT)
