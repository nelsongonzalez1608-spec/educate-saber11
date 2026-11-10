#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GUÍAS DE CLASE PROYECTABLES («clase viva») · INGLÉS · las 8 del área.

    python3 clase_viva_ing.py [carpeta]      (por defecto entregables/guias_ingles/)

Usa el motor clase_viva.py sin cambiarlo (la plantilla, el JavaScript, la portada, las reglas, la
activación, las dinámicas, la pregunta problematizadora, el cierre y las clases 7 y 8). Lo que Inglés
necesita y el motor no trae se escribe aquí, como escenas propias con las mismas clases de CSS:

  1. BLOQUES CON LAS TARJETAS DE CLASE. El motor numera los bloques 1-2 … 9-10; en Inglés las diez de
     clase son otras (plan_ing.REPARTO: en la Misión 3 son la 1, 3, 12, 14…) y en las misiones 4 a 6 el
     libro reinicia la numeración en cada bloque. esc_bloque() muestra el número de la tarjeta, su
     ubicación en el libro y el texto en inglés EN GRANDE con sus opciones (ITEMS, transcritos del
     libro), el instrumento, la Corrección EDUCATE de la tarjeta (es la misma que el estudiante tiene
     impresa: no da la clave) y la clave oculta hasta «Revelar».
  2. RONDA DE CLAVES de la tarea (clases 2, 4, 5, 6 y 8) y RETO con tarjetas del libro: las claves en
     una caja .clave oculta que abre un botón; el profe ve en la guía qué aceptar.
  3. ENTRENAMIENTO CON OPCIONES A–H: la Parte 1 del examen trae un banco de ocho palabras (Misión 1).
     esc_icfes() es la del motor con las letras A–H.
  4. Membrete «Pregunta Saber 11» (CV.FICFES). En pantalla nunca dice «oficial» ni «reales»;
     revisar_pantalla() falla si aparece, o si aparece un nombre de la política colombiana.
  5. Las dinámicas E2–E4 van antes del primer bloque que trae su subestrategia (no en posiciones fijas).

Comprueba antes de escribir: plan_ing.verificar() (claves del libro, del entrenamiento y el reparto) y
que la clave de cada ITEM coincida con plan_ing.CLAVES.
"""
import copy, html, os, re, sys, types

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)

import clase_viva as CV
import plan_ing as P
import textos_ing

CV.FICFES = "Pregunta Saber 11"          # decisión de Nelson, 10 nov: sin año ni «oficial»
E = CV.E
OUT = os.path.join(AQUI, "..", "entregables", "guias_ingles")
LETRAS = "ABCDEFGH"

CSS_EXTRA = """[hidden]{display:none!important}
.en{font-family:var(--display);font-weight:600;font-size:1.32em;line-height:1.35;margin:.4em 0 .5em;color:var(--ink)}
.en.xl{font-size:1.6em}
.eops{list-style:none;margin:.3em 0 .6em;padding:0;display:grid;gap:4px}
.eops li{display:flex;gap:10px;align-items:baseline;font-size:1.12em;line-height:1.3}
.eops li b{flex:none;width:1.6em;height:1.6em;border-radius:7px;display:inline-grid;place-items:center;background:var(--bg);font-family:var(--display);font-size:.85em}
.eops.banco{grid-template-columns:repeat(auto-fit,minmax(min(100%,180px),1fr))}
.ins{font-size:.95em;color:var(--muted);margin:.2em 0}
.corr{margin-top:10px;border-left:5px solid #242478;background:#F2F3FA;border-radius:10px;padding:8px 14px;font-size:.92em}
.corr b{display:block;color:#242478;font-size:.78em;letter-spacing:.06em;text-transform:uppercase}
.kgrid{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}
.kg{display:inline-flex;gap:8px;align-items:center;border:1.5px solid var(--line);border-radius:10px;padding:6px 12px;background:var(--paper);font-weight:700}
.kg span{color:var(--muted);font-weight:600}
.nums{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.nums span{border:1.5px solid var(--line);border-radius:999px;padding:3px 12px;font-weight:700;background:var(--paper)}
.op .L{flex:none}
.icfes .texto{font-size:1.1em;line-height:1.5}
.icfes .texto .en{font-size:1.5em}
.icfes .op{font-size:1.08em}
.icfes .enun{font-size:1.18em}
"""

TITULOS = {
    1: "La pista que decide",
    2: "Contéstale a la persona, no a la palabra",
    3: "Escucha a los vecinos del hueco",
    4: "Lo que el texto dice, dato por dato",
    5: "Leer entre líneas, con la prueba en la mano",
    6: "Leer todo el texto antes de llenar el espacio",
}
LEADS = {
    1: "Hoy las palabras se encuentran por piezas: ¿es una persona, un lugar o una cosa? ¿Qué verbo la "
       "delata? ¿Qué pista tacha opciones? Y un aviso se entiende por quién lo escribe y qué quiere.",
    2: "En una conversación no se contesta a la palabra: se contesta a la persona. Hoy decidimos qué clase "
       "de frase nos dicen, qué quieren de nosotros y en qué tiempo hablan.",
    3: "Un espacio en blanco no se llena con lo que suena bonito. Tapamos las opciones, preguntamos qué "
       "pieza falta y escuchamos a los vecinos del hueco.",
    4: "Una gira de K-pop y una Vuelta a España. Hoy cada respuesta sale del texto, dato por dato: la "
       "palabra ancla, la cifra con su dueño y la misma idea dicha con otras palabras.",
    5: "La fotosíntesis y la música de la calle. Hoy leemos lo que el texto deja entender, pero solo lo que "
       "podemos señalar con el dedo en una frase.",
    6: "La última clase de contenido. Un viaje, un debate y un misterio en Baker Street: hoy el texto "
       "entero decide qué va en cada espacio.",
}


UI = dict(
    portada_decir=["«Libro abierto, cuaderno cerrado, lápiz. Hoy nadie traduce palabra por palabra: hoy "
                   "buscamos la pista que decide.»"],
    regla_lead="Si el instrumento está vacío, no lo resolviste: lo adivinaste.",
    regla_p=("Primero se escribe la pista en el instrumento —la palabra que decide, lo que tacha, el tiempo, "
             "la intención—, después se marca la letra. Una respuesta correcta con el instrumento en blanco "
             "no cuenta como resuelta."),
    regla_decir=["«La respuesta correcta con el instrumento vacío no cuenta. ¿Por qué? Porque en inglés casi "
                 "todas las opciones suenan bien: el que no escribió la pista escoge la que suena, no la que "
                 "dice el texto.»"],
    regla_apoyo=["Si alguien pregunta para qué escribir, la respuesta corta es: en el examen nadie traduce; "
                 "el que encuentra la pista responde en segundos.",
                 "Si alguien dice «es que suena mejor», devuélvele la pregunta: «¿qué palabra del texto te lo "
                 "dice?»."],
    act_h2="¿Qué palabra decide?",
    act_lead="Léela despacio. Señala la palabra que decide y di qué decide. Todavía no se abre el libro.",
    act_apoyo=("No traduzcas la frase ni expliques gramática: primero la palabra que decide. La frase es "
               "inventada para la clase: no sale del libro."),
    dina_decir=["«Esto no es recreo: es la misma operación que van a hacer con el texto en inglés en cinco "
                "minutos —buscar, tachar, ubicar en el tiempo—, pero con el cuerpo.»"],
    prob_lead="Antes de buscar la pista: ¿cuál creen que es? Levanten la mano.",
    prob_lead2=P.PREGUNTA_AREA,
    prob_sub=("Nadie justifica con «me suena» ni con «en español se dice así»: toda respuesta señala la "
              "palabra del texto que decide."),
    reto_defensa=("<b>La defensa:</b> tres minutos por equipo, leyendo en voz alta la palabra del texto que "
                  "decide. «Es que suena mejor» no cuenta."),
    reto_apoyo=[],
    icfes_decir=["Durante la evaluación no se proyecta nada: las preguntas están en el cuaderno. Esta "
                 "diapositiva es para el cierre, cuando se socializan las falladas.",
                 "«¿Qué pista escribiste en el instrumento antes de mirar las opciones?»"],
)

PROHIBIDOS = ["Petro", "Uribe", "Duque", "Santos", "Benedetti", "Pastrana", "Gaviria", "Samper",
              "Cepeda", "Vargas Lleras", "Fajardo", "Claudia López"]
NO_EN_PANTALLA = ["oficial", "reales del ICFES", "real del ICFES", "Pregunta real"]

# ─────────────── las diez tarjetas de clase de cada misión, como están en el libro ───────────────
# n: (texto en inglés, opciones, por qué es la clave). Transcritas de fuente_libro/INGLÉS (pruebas de
# campo, páginas 414 a 470). La clave sale de plan_ing.CLAVES; aquí solo se explica.
BANCO_PEOPLE = ["Factory", "Nurse", "Technician", "Volunteer", "Artist", "Passenger", "Baker", "Driver"]
AVISO = ["{0}"]
ITEMS = {
 1: {1: ("This is a person who repairs electrical machines in offices or houses.", BANCO_PEOPLE,
         "«repairs» (repara) deja solo a quien arregla máquinas: Technician. Driver maneja; Artist crea."),
     2: ("This is a place where people work making cars or machines.", BANCO_PEOPLE,
         "«a place»: el único lugar del banco es Factory; todas las demás son personas."),
     3: ("This is a person who helps patients but is not a doctor.", BANCO_PEOPLE,
         "«patients» lleva al hospital y «but is not a doctor» tacha al médico: Nurse."),
     4: ("This is a person who drives people from one place to another for money.", BANCO_PEOPLE,
         "«drives… for money»: Driver. Passenger también va de un lugar a otro, pero no maneja ni cobra."),
     5: ("This is a person who works helping people without being paid.", BANCO_PEOPLE,
         "«without being paid» (sin que le paguen) es lo que define a Volunteer."),
     6: ("This is a person who creates paintings or sculptures.", BANCO_PEOPLE,
         "«creates paintings»: Artist (el sufijo -ist, como en pianist)."),
     7: ("This is a person who travels in a bus, car, or plane but does not drive.", BANCO_PEOPLE,
         "«but does not drive» tacha a Driver: Passenger. Sobra G, Baker (y la I es la del ejemplo)."),
     15: ("Please return books on time. Others are waiting for them.", ["Library", "Coffee shop", "Gym"],
          "«return books» y «others are waiting for them»: libros prestados, que otros esperan. Library."),
     16: ("Your package is ready. Pay online to schedule delivery.",
          ["Supermarket", "Delivery App", "School noticeboard"],
          "«package», «pay online», «schedule delivery»: es el mensaje de una aplicación de domicilios."),
     17: ("Don't share personal information in the comments. Report suspicious accounts.",
          ["Social media post", "Public park sign", "Library rules board"],
          "«comments» y «accounts» solo existen en una red social: Social media post.")},
 2: {1: ("Could you print these documents before the meeting?",
         ["Printers are sometimes very slow.", "The meeting room is on the first floor.", "Yes, I'll do it right away."],
         "«Could you…?» es un pedido: se contesta aceptando o negándose. A y B repiten palabras del pedido sin decir si lo hará."),
     2: ("Good afternoon, I'm calling to confirm if you are still interested in our Internet service.",
         ["Yes, I need more information about the plans, please.", "The Internet is very fast in this city.",
          "I usually use the Internet every night."],
         "Quien llama quiere confirmar si sigues interesado: la A le contesta. B y C hablan de Internet en general."),
     3: ("Is this the line for the concert tickets?",
         ["Yes, it is. The ticket booth is right over there.", "I love going to concerts with my friends.",
          "The band is really famous in my country."],
         "«Is this…?» pide sí o no; «line» es fila. La A contesta y dice dónde está la taquilla."),
     4: ("Do you think we should add more details to the budget section?",
         ["I prefer to work in the morning, not at night.", "Yes, it will help explain the costs better.",
          "Budgets are important in every company."],
         "«Do you think…?» pide una opinión: la B da posición (yes) y razón. C es una verdad general que no opina."),
     5: ("Does this phone have enough memory for videos?",
         ["Yes, it has 128 GB, perfect for storing videos and photos.", "Phones are very popular this year.",
          "I like watching videos every day."],
         "Pide sí o no sobre ESTE teléfono: la A da el dato (128 GB). B y C hablan de teléfonos y videos en general."),
     6: ("Did you hear about Anna's new job?",
         ["I prefer working from home.", "Jobs are very important nowadays.",
          "Yes, she told me yesterday. It sounds great!"],
         "«Did you hear…?» pregunta por algo que ya pasó: la C contesta en pasado (told) y reacciona."),
     7: ("How are you feeling today?",
         ["Much better, thank you. The medicine is working.", "Doctors are very busy in this clinic.",
          "I don't like taking pills every day."],
         "El médico pregunta cómo te sientes HOY: la A contesta eso. B habla de la clínica; C, de una costumbre."),
     8: ("Did you watch the new episode last night?",
         ["I don't like watching TV during the week.", "Yes, it was amazing! I loved the ending.",
          "TV shows are very popular this year."],
         "«Did… last night?» se contesta en pasado: «Yes, it was amazing». A y C no dicen si lo vio."),
     9: ("I saw you talking to Mark yesterday. What happened?",
         ["Mark is very tall and plays basketball.", "Mark and I was just discussing the math project.",
          "Oh, nothing special. We were just talking about school."],
         "«What happened?» pide contar lo que pasó: la C. A describe a Mark. B tiene un error (Mark and I was → were)."),
     10: ("The doctor said I should drink more water.",
          ["Water is good for plants too.", "That's true, it's really important to stay hydrated.",
           "I prefer drinking juice instead of water."],
          "No es una pregunta: cuentan un consejo. La reacción natural le da la razón: la B.")},
 3: {1: ("Thousands of fans (1) ____ to the stadium early in the morning.", ["comes", "come", "came"],
         "El texto abre con «Last month»: el reloj está en pasado. came."),
     3: ("Karol G (3) ____ many of her greatest hits, and the audience (4) ____ every word.",
         ["sings", "sang", "sing"],
         "Mismo reloj del texto (pasado) y sujeto Karol G: sang. sing y sings son presente."),
     12: ("It (12) ____ in cinemas around the world and millions of people (13) ____ to see it.",
          ["was release", "released", "release"],
          "Con la A corregida a lápiz («was released») es la clave: la película no estrena, la estrenan (voz "
          "pasiva). B («It released») es informal: acéptala solo si la defienden."),
     14: ("The movie (14) ____ new characters and (15) ____ a unique animation style that many critics admired.",
          ["introduce", "introduces", "introduced"],
          "«In 2023» pone el reloj en pasado; la pregunta de control es ¿did o does? → did: introduced."),
     21: ("Artificial Intelligence (AI) tools, like chatbots, have become very popular (21) ____ teenagers.",
          ["among", "between", "inside"],
          "among = entre muchos (teenagers); between es entre dos; inside es dentro de algo."),
     23: ("However, teachers warn that depending too much (23) ____ these apps may reduce critical thinking skills.",
          ["at", "in", "on"], "depend on: la preposición viene pegada al verbo."),
     25: ("On the other hand, AI can be useful (25) ____ it helps students understand complex topics.",
          ["so", "because", "but"], "La segunda idea es la razón de la primera: because."),
     29: ("In the future, digital literacy will be essential (29) ____ succeed in education and work.",
          ["in", "to", "for"],
          "Después viene un verbo sin marca (succeed): essential to + verbo. Aquí to no es preposición: es la "
          "marca del infinitivo."),
     36: ("(36) ____ these opportunities, online activism can also create new risks, such as misinformation or polarization.",
          ["Although", "However", "Despite"],
          "Después del espacio viene solo un sustantivo (these opportunities), sin verbo: Despite. Although pide "
          "una oración; However va suelto, con coma."),
     38: ("Democracy depends not only on elections (38) ____ on constant participation and civic engagement.",
          ["but also", "and", "so"], "not only … but also: palabras que llegan en pareja.")},
 4: {1: ("How many shows will TWICE perform in Sydney?", ["One", "Two", "Four"],
         "«two Sydney shows». Four son los de toda Australia."),
     2: ("The concerts on November 8th and 9th will take place in:", ["Melbourne", "Sydney", "Brisbane"],
         "«two more shows at Melbourne's Rod Laver Arena on November 8th and 9th». Sydney es verdad, pero tiene "
         "el 1 y el 2; Brisbane no está en el texto."),
     3: ("The special stage design announced for the tour is:",
         ["a holographic screen", "a rotating stage", "a 360-degree stage"],
         "«a state-of-the-art 360-degree stage design»: se ve desde todos los ángulos; nada gira."),
     4: ("General ticket sales in Australia started on:",
         ["August 8 at 11 AM", "August 7 at 10 AM", "July 11 at 10 AM"],
         "«general ticket sales opening on August 8 at 11 AM». El 7 de agosto es la preventa; el 11 de julio, el álbum."),
     7: ("In the United States, TWICE became the first female K-pop group to:",
         ["perform at Tokyo Dome", "appear on Billboard", "headline major stadiums"],
         "«the first female K-pop group to headline major US stadiums like SoFi and MetLife»."),
     9: ("According to the passage, where did the cycling event conclude in 2016?",
         ["It came to an end in Spain's capital city.", "It finished in the main city of Catalonia.",
          "It concluded after celebrations in Boyacá."],
         "«ended in Madrid»: Madrid dicho con otras palabras (la capital de España, un dato de afuera del texto)."),
     11: ("How many stages were included in the edition held in 2016?",
          ["The race was shortened to only twenty stages.", "It had a total of twenty-one official stages.",
           "It was composed of exactly twenty-two stages."], "«across 21 stages» = twenty-one."),
     13: ("Which particular climb allowed Quintana to secure leadership?",
          ["The demanding ascent known as Lagos de Covadonga.", "The famous French mountain called Mont Ventoux.",
           "The long Spanish stage crossing Sierra Nevada."],
          "«the climb to Lagos de Covadonga, where he took the leader's red jersey»: la camiseta roja es el liderato."),
     14: ("Which competitor arrived second in the general standings?",
          ["The British cyclist associated with Team Sky.", "The Colombian rider who finally got third place.",
           "The Spanish champion recognized as Contador."],
          "«Chris Froome, from Team Sky, who finished second». «British» no está en el texto: es la Corrección "
          "EDUCATE de la tarjeta; se decide con el equipo y el puesto."),
     16: ("Approximately, how many spectators followed the event globally?",
          ["About one hundred and fifty million international fans.",
           "Close to two hundred million people from different nations.",
           "More than three hundred million viewers worldwide."], "«more than 300 million viewers worldwide».")},
 5: {1: ("The text implies that human existence is fundamentally dependent on which of the following principles?",
         ["The successful agricultural domestication of various animal and plant species.",
          "The ongoing advancement of humanity's technological and industrial innovations.",
          "The intricate and delicate balance of key planetary biological processes.",
          "The complete separation of urban environments from natural ecological systems."],
         "«Without this process… most species could not survive»: la vida humana depende de un proceso biológico."),
     3: ("From the third paragraph, it can be inferred that local human activities, such as deforestation:",
         ["have consequences that are primarily restricted to their immediate geographic areas.",
          "represent a necessary sacrifice for the continued economic development of societies.",
          "are generally less impactful to the planet than are most natural geological events.",
          "possess the significant capacity to alter large-scale global atmospheric systems."],
         "«directly affect the quality of the air we breathe and the stability of our climate»: lo local altera lo global."),
     4: ("The author's conclusion about \"protecting our own future\" reframes environmental conservation as:",
         ["a moral duty focused exclusively on the preservation of a variety of non-human species.",
          "an essential and pragmatic strategy for ensuring human survival and long-term well-being.",
          "an optional recreational activity for communities with sufficient economic and social resources.",
          "an economic burden that inevitably limits industrial progress and necessary societal expansion."],
         "«not only about saving nature: it is about protecting our own future»: cuidar las plantas nos conviene "
         "para sobrevivir. A es el marco viejo («exclusively»)."),
     5: ("By describing photosynthesis as the \"foundation of almost every ecosystem,\" the author implies that it is:",
         ["a biological process that is important but easily replaceable by other modern energy sources.",
          "a biological function that benefits the plant kingdom far more than it benefits animal species.",
          "a life-support system whose large-scale disruption would lead to systemic ecological collapse.",
          "a natural mechanism that is relevant mainly to the botanical studies of specialized plant life."],
         "«foundation» es la base de una casa: si se rompe, se cae todo. C."),
     6: ("The text implicitly contrasts the Earth's current, photosynthesis-maintained atmosphere with:",
         ["a previous or potential atmospheric state that is uninhabitable for complex aerobic life.",
          "a hypothetical atmosphere containing much higher levels of oxygen than are present today.",
          "a gaseous environment similar to those found on other non-inhabited planets in our solar system.",
          "a future atmosphere where advanced technology will fully replace all biological functions."],
         "«the atmosphere would quickly become toxic»: el contraste es con una atmósfera posible e invivible."),
     7: ("By mentioning the effects of urban pollution on tree leaves, the author primarily illustrates that:",
         ["the inherent resilience of plants allows them to adapt without issue to any environmental conditions.",
          "modern technology has nearly eliminated human dependence on the functions of urban plant life.",
          "natural environments and human-built ones operate in completely separate and unrelated spheres.",
          "threats to photosynthesis are not just distant problems but occur in our immediate daily lives."],
         "«In cities, air pollution…» y «may seem distant, but they directly affect…»: la amenaza está cerca. D."),
     9: ("The text's description of the musician's performance on a \"cracked sidewalk\" serves to highlight the "
         "idea that public spaces:",
         ["represent significant physical dangers for performers.", "require municipal funding for artistic development.",
          "are inherently unsuited for cultural gatherings.", "can be redefined and reclaimed by creative expression."],
         "Un andén roto se vuelve escenario: «transform public spaces into places of expression». D."),
     12: ("The phrase \"I am here, my story matters\" is used to imply that street performance is fundamentally an act of:",
          ["commercial negotiation with the passing audience.", "personal and cultural affirmation against anonymity.",
           "organized protest against government policies.", "professional ambition aimed at being discovered."],
          "«not only about money. It is also about visibility and dignity»: decir «existo y valgo». B."),
     13: ("The author's concluding statement that Colombians are \"unwilling to let silence define their cities\" "
          "frames street music as a form of:",
          ["historical preservation of nearly forgotten art forms.", "simple background entertainment for city dwellers.",
           "structured musical education for the population.", "defiant cultural vitality against urban indifference."],
          "«resilient, creative, and unwilling to let silence define their cities», frente a la gente que pasa de "
          "afán del primer párrafo. D."),
     15: ("The author introduces the complaint about noise and blocked sidewalks in the final paragraph primarily to:",
          ["suggest that street music should be more heavily regulated.",
           "create a counterargument that is then overcome by a greater ideal.",
           "conclude that the negative aspects ultimately outweigh the positive ones.",
           "admit that the central issue of the text is far too complex to resolve."],
          "«Some people complain… Others, however, argue…»: la queja se pone para superarla. B.")},
 6: {1: ("Two years ago, my family and I (1) ____ to the mountains for a weekend trip.",
         ["go", "went", "going", "gone"], "«Two years ago» clava el verbo en el pasado terminado: went."),
     2: ("The road was long, and we (2) ____ tired when we finally arrived.",
         ["feel", "felt", "were feeling", "feels"],
         "El relato va en pasado: felt es la del libro, y were feeling también es correcta (Corrección EDUCATE)."),
     5: ("Since that day, I (5) ____ fascinated by nature and camping.",
         ["became", "have been", "was becoming", "turn"],
         "«Since that day» tiende un puente desde el pasado hasta hoy: have been (presente perfecto)."),
     6: ("I have already (6) ____ many photographs of our trips, and I (7) ____ a blog to share them with friends.",
         ["taken", "took", "taking", "take"], "have + la tercera forma: taken."),
     8: ("Honestly, I (8) ____ never imagined how much I would love outdoor adventures.",
         ["had", "will", "have", "has"],
         "No lo imaginaba ANTES del viaje: el pasado de un pasado (had + imagined); «would love» mira hacia "
         "adelante desde ese pasado. Sello «Alto»."),
     9: ("In these activities, students (1) ____ different points of view about a topic.",
         ["express", "expand", "expect", "explore"],
         "express points of view es la del libro; explore también es correcta (Corrección EDUCATE)."),
     12: ("A debate also teaches them to (4) ____ evidence before speaking, instead of repeating information "
          "without analysis.", ["check", "ignore", "skip", "hide"],
          "«instead of repeating information without analysis» pide lo contrario: revisar la evidencia, check."),
     13: ("Sometimes, students (5) ____ nervous when they have to speak in front of others.",
          ["felt", "feels", "feel", "feeling"],
          "Sujeto plural (students) y presente habitual (Sometimes, they become): feel."),
     14: ("Teachers (6) ____ debates as a way to make classes more dynamic and interactive.",
          ["gives", "use", "used", "using"],
          "Todo el texto va en presente: use. used es gramatical, pero rompe el tiempo del párrafo."),
     16: ("These experiences (8) ____ students to become more active citizens in their communities.",
          ["allow", "stop", "cancel", "prevent"],
          "allow + alguien + to + verbo, el mismo molde de «encourage students to» del párrafo 1.")},
}

# La «Corrección EDUCATE» impresa en la tarjeta del cuaderno (ing1.py … ing6.py), resumida sin dar la clave.
CORR_TARJETA = {
 (1, 1): "En tu libro el banco muestra la opción I (Journalist) con su círculo. No es opción: es la del "
         "ejemplo. En las preguntas 1 a 7 escoges entre A y H; tacha el círculo de la I.",
 (2, 9): "Una de las tres opciones tiene un error de concordancia entre el sujeto y el verbo. Encuéntrala, "
         "márcala con una X y escribe cómo quedaría bien escrita.",
 (3, 12): "En tu libro la opción A dice «was release»: le falta la -d del final («was released»). Corrígela con "
          "lápiz y después escoge entre las tres.",
 (4, 9): "El texto dice que 2016 fue la primera vez que dos colombianos compartieron el podio de la Vuelta. No es "
         "cierto: ya había pasado en 1989. Lo que pasó por primera vez fue que un colombiano ganara con otro "
         "colombiano en el podio. Corrige esa frase a lápiz.",
 (4, 14): "Una de las opciones le pone a un corredor una nacionalidad que el texto no dice. Tacha esa palabra y "
          "decide con lo demás que dice la opción (el equipo, el puesto).",
 (6, 2): "El libro espera una sola respuesta, pero en inglés hay dos opciones correctas. Encuéntralas, márcalas "
         "las dos y escribe en qué cambia lo que cuenta cada una.",
 (6, 9): "El libro espera una sola respuesta, pero dos opciones son correctas y naturales en inglés. "
         "Encuéntralas y márcalas las dos.",
}


# ─────────────────────────────── datos ───────────────────────────────
def paginas_texto(mis):
    a, z = P.pags_mision(mis)
    return f"{a} a {z}"


def planeador():
    ns = types.SimpleNamespace(**{k: getattr(P, k) for k in dir(P) if k.isupper()})
    ns.MISIONES = {m: dict(d, pags=paginas_texto(m)) for m, d in P.MISIONES.items()}
    ns.AVISOS = {}                      # los avisos van en la guía del profe, no los proyecta el motor
    return ns


def ui(mis):
    l0, l1 = P.LIBRO[mis]
    u = dict(UI)
    u["portada_libro"] = (f"Las {P.TOTAL_PREG[mis]} preguntas de la prueba de campo, páginas {l0} a {l1}; "
                          f"hoy, diez en clase")
    p1 = P.REPARTO[mis]["clase"][0]
    u["prob_apoyo"] = [
        f"La pregunta modelo es la tarjeta {p1} ({P.libro_num(mis, p1)}, libro página {P.pag_libro(mis, p1)}). "
        f"El cuaderno se abre en la página {P.pag_tarjeta(mis, p1)} solo en «mi primera idea».",
        "Cuenta las manos tocando cada letra: el número queda en pantalla y sirve para el final del momento, "
        "cuando el grupo vea cuántos cambiaron de opinión al encontrar la pista.",
        "No digas la clave en este momento: sale en el primer bloque del desarrollo guiado, después de llenar el "
        "instrumento en pantalla, casilla por casilla."]
    return u


def area(mis, P_ns, textos):
    return CV.Area(
        nombre="Inglés", prefijo="ING", fuerte="Si Inglés no es tu fuerte",
        color=CV.color_de("Inglés"), P=P_ns,
        claves_libro=lambda m: P.CLAVES[m],
        preguntas_icfes=CV.preguntas_de_textos(textos),
        textos=textos, advertencias={}, taller={}, saberes=P.SABERES,
        activacion=P.ACTIVACION, titulos=TITULOS, leads=LEADS,
        est_col=list(P.COLS_MIS[mis]),
        colores=dict(m2="#1F4E8C", m3="#3B3BA6", m4=P.MORADO, m5=P.ROJO, m6=P.PIZARRA, rojo=P.ROJO),
        textos_ui=ui(mis), apoyo_fuerte="Inglés no es tu área", out=OUT)


def avisos_de(mis, n):
    """Los avisos del planeador que nombran la tarjeta n («preg. 17 a 20 · 24», «preg. 2 y 9»…)."""
    out = []
    for rot, sev, que, hacer in P.AVISOS.get(mis, []):
        if not rot.startswith("preg."):
            continue
        ns = set()
        for a, b in re.findall(r"(\d+) a (\d+)", rot):
            ns |= set(range(int(a), int(b) + 1))
        ns |= {int(x) for x in re.findall(r"\d+", rot)}
        if n in ns:
            out.append(f"Del libro ({sev}): {que} Qué haces: {hacer}")
    return out


def pron_de(mis, texto):
    t = texto.lower()
    return [f"{w} ({p})" for w, p in P.PRONUNCIA[mis] if w.lower() in t]


def kgrid(mis, ns):
    return "".join(f'<span class="kg"><span>{n}</span>{E(P.CLAVES[mis][n])}</span>' for n in ns)


# ─────────────────────────────── escenas propias ───────────────────────────────
def guia(A, fase, decir=(), apoyo=()):
    return CV.guia(A, fase, decir=decir, apoyo=apoyo)


def _tarjeta(A, mis, n, grupo):
    d = P.MISIONES[mis]
    est = next(e for p, e, i, c in P.TALLER_TODO[mis] if p == n)
    ins = next(i for p, e, i, c in P.TALLER_TODO[mis] if p == n)
    k = d["estr"].index(est)
    c = A.est_col[k]
    en, ops, _ = ITEMS[mis][n]
    banco = len(ops) > 4
    lis = "".join(f"<li><b>{L}</b><span>{E(o)}</span></li>" for L, o in zip(LETRAS, ops))
    sel = ""
    s = CV.sello(A, mis, n)
    if s:
        sab = P.SABERES.get((mis, n))
        sel = (f'<div class="sello"><b>Alto · aquí entra el profe</b><span>{E(sab[0] if sab else s[4])}</span></div>')
    corr = CORR_TARJETA.get((mis, n))
    corr_h = f'<div class="corr"><b>Corrección EDUCATE</b>{E(corr)}</div>' if corr else ""
    clave = P.CLAVES[mis][n]
    return (f'<div class="card edge" style="--accent:{c}">'
            f'<div class="eyebrow"><span class="membrete">Tarjeta {n} · libro p. {P.pag_libro(mis, n)} · '
            f'{E(P.libro_num(mis, n))}</span>'
            f'<span class="min" style="--accent:{c}">S{k+1} · {E(est)}</span></div>'
            f'<p class="en">{E(en)}</p>'
            f'<ul class="eops{" banco" if banco else ""}">{lis}</ul>'
            f'<p class="ins">Instrumento: <b style="color:{c}">{E(ins)}</b>. Llénalo antes de marcar.</p>'
            f'{corr_h}{sel}'
            f'<div class="clave" hidden data-grupo="{grupo}"><span class="keychip" style="background:{c}">'
            f'{E(clave)}</span> es la clave del libro</div></div>')


def esc_bloque(A, mis, a, b_):
    grupo = f"k{mis}{a}"
    partes = _tarjeta(A, mis, a, grupo) + _tarjeta(A, mis, b_, grupo)
    primero = a == P.REPARTO[mis]["clase"][0]
    apoyo = [f"Las claves del libro son {a}·{P.CLAVES[mis][a]} y {b_}·{P.CLAVES[mis][b_]}. No las reveles hasta "
             "que todos tengan la pista escrita: el botón es para el cierre del bloque."]
    for n in (a, b_):
        apoyo.append(f"Tarjeta {n} · por qué: {ITEMS[mis][n][2]}")
        sab = P.SABERES.get((mis, n))
        if sab:
            apoyo.append(f"Tarjeta {n} · sello «{sab[0]}»: {sab[1]} Para destrabar: «{sab[2]}»")
        if (mis, n) in CORR_TARJETA:
            apoyo.append(f"Tarjeta {n} · la Corrección EDUCATE de la tarjeta es la que está en pantalla: léela en "
                         "voz alta. No da la clave.")
        apoyo += [f"Tarjeta {n} · {x}" for x in avisos_de(mis, n)]
        pr = pron_de(mis, ITEMS[mis][n][0] + " " + " ".join(ITEMS[mis][n][1]))
        if pr:
            apoyo.append(f"Tarjeta {n} · cómo se dice: " + ", ".join(pr) + ".")
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m3)">Desarrollo guiado · tarjetas {a} y '
         f'{b_}</span><span class="kicker">{"En pantalla, casilla por casilla" if primero else "En el cuaderno, cada uno el suyo"}'
         f'</span></div>'
         f'<h2>Tarjetas {a} y {b_}: primero la pista, después la letra</h2>'
         f'<div class="grid c2 mt">{partes}</div>'
         f'<div class="ctl"><button class="btn" data-showgrupo="{grupo}">Revelar las claves</button></div>')
    return dict(m=2, min=5, html=h, guia=guia(A, 2, decir=[
        "«Antes de marcar: ¿qué pista escribieron? Léanmela.»",
        "Si alguien se traba, pregúntale qué palabra vecina mira. Si el instrumento está vacío, vuelve al texto "
        "antes que a las opciones."], apoyo=apoyo))


def esc_ronda(A, mis_clase):
    """La ronda de claves de la tarea, al comenzar la clase."""
    m, ns, rot = P.ronda_de(mis_clase)[0]
    ident = f"ronda{mis_clase}"
    pags = P.rango([P.pag_tarjeta(m, n) for n in ns])
    nums = "".join(f"<span>{n}</span>" for n in ns)
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m1)">Ronda de claves · 5 min</span>'
         f'<span class="kicker">Tarea de la Misión {m} · {E(rot)}</span></div>'
         f'<h2>Antes de empezar: la tarea de la Misión {m}</h2>'
         f'<p class="lead">Cuaderno abierto en las páginas {E(pags)} y un color distinto en la mano. Junto a cada '
         f'X escribe la pista que no viste.</p>'
         f'<div class="nums">{nums}</div>'
         f'<div class="ctl"><button class="btn" data-show="{ident}">Revelar las claves de la tarea</button></div>'
         f'<div class="clave kgrid" id="{ident}" hidden>{kgrid(m, ns)}</div>')
    apoyo = [f"Las claves: {', '.join(f'{n}·{P.CLAVES[m][n]}' for n in ns)}.",
             "Manos arriba por tarjeta: la más fallada se explica en un minuto, con la pista. Las demás van a tu "
             "registro. No se corrige la letra: se escribe la pista que faltó."]
    for n in ns:
        apoyo += [f"Tarjeta {n} · {x}" for x in avisos_de(m, n)]
    if m == 3 and 32 in ns:
        apoyo.append("La 32 no tiene letra: se escribe «in».")
    return dict(m=0, min=5, html=h, guia=dict(
        obj="Que la tarea se revise en cinco minutos y cada uno vea qué pista no vio.",
        decir=["«Cuaderno abierto en la tarea. Lápiz de otro color. Voy a revelar las claves: chulita o X, y "
               "junto a cada X la pista que no vieron.»"], apoyo=apoyo))


def esc_reto(A, mis):
    nom, mins, txt = P.RETOS[mis]
    r = P.REPARTO[mis]["reto"]
    extra, apoyo = "", ["Si un equipo entrega una sola hoja para los tres, el reto no cuenta. La discusión es "
                        "compartida; el registro es individual, en el cuaderno de cada uno."]
    if r:
        ident = f"reto{mis}"
        pags = P.rango([P.pag_tarjeta(mis, n) for n in r])
        extra = (f'<div class="nums">{"".join(f"<span>{n}</span>" for n in r)}</div>'
                 f'<p class="sub">Cuaderno, páginas {E(pags)}.</p>'
                 f'<div class="ctl"><button class="btn" data-show="{ident}">Revelar las claves del reto</button></div>'
                 f'<div class="clave kgrid" id="{ident}" hidden>{kgrid(mis, r)}</div>')
        apoyo.insert(0, f"Las claves del reto: {', '.join(f'{n}·{P.CLAVES[mis][n]}' for n in r)}. Revélalas al final, "
                        "después de las defensas.")
        for n in r:
            apoyo += [f"Tarjeta {n} · {x}" for x in avisos_de(mis, n)]
        if mis == 3:
            apoyo.append("La 32 no tiene letra: ninguna opción sirve y se escribe «in» («acting in the interests of»).")
    else:
        apoyo.insert(0, "Las seis frases son originales. Respuestas naturales posibles: «Sure, here you are» · "
                        "«Yes, please, thank you» · «Yes, it is. It opens at nine» · «Yes, I did. It was easy» · "
                        "«I agree, it was boring» o «Really? I liked it» · «Oh no! Is he OK?».")
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m4)">Reto en equipo · {mins} min</span>'
         f'<span class="kicker">Equipos de tres · cada uno responde en su cuaderno</span></div>'
         f'<h2>Reto del corte: {E(nom)}</h2>'
         f'<div class="card big edge mt" style="--accent:var(--m4)"><p class="lead">{E(txt)}</p>{extra}</div>'
         f'<div class="note mt" style="--accent:var(--m4)">{UI["reto_defensa"]}</div>')
    return dict(m=3, html=h, guia=guia(A, 3, apoyo=apoyo))


def esc_icfes(A, mis, k, q, clave, txt):
    """La del motor, con las letras A–H (la Parte 1 trae un banco de ocho palabras)."""
    ops = "".join(f'<div class="op" data-op="{L}"><span class="L">{L}</span><span>{E(o)}</span></div>'
                  for L, o in zip(LETRAS, q["o"]))
    texto = (txt.get("texto") or "")
    corto = len(texto) < 120                 # un aviso o la frase de una conversación: en grande
    cuerpo = "".join(f'<p{" class=\"en\"" if corto else ""} lang="en">{E(p)}</p>'
                     for p in texto.split("\n\n") if p.strip())
    ident = f"icf{mis}{k}"
    h = (f'<div class="eyebrow"><span class="membrete">{E(CV.FICFES)}</span>'
         f'<span class="min" style="--accent:var(--m5)">Evaluación individual · pregunta {k}</span></div>'
         f'<div class="grid c2 icfes mt">'
         f'<div class="texto"><h3>{E(txt.get("titulo") or "")}</h3>{cuerpo}</div>'
         f'<div><p class="enun">{E(q["e"])}</p><div class="ops" id="{ident}">{ops}</div>'
         f'<div class="ctl"><button class="btn" data-clave="{ident}" data-k="{E(clave)}">Revelar la clave</button></div>'
         f'</div></div>')
    notas = [f"La clave es la {clave}. Por qué: {txt.get('verificacion', '')}"] + list(txt.get("notas") or [])
    sab = P.SABERES.get((mis, f"I{k}"))
    if sab:
        notas.append(f"Sello del cuaderno · {sab[0]}: {sab[1]} Para destrabar: «{sab[2]}»")
    if mis == 5:
        notas.insert(0, "⚑ Texto con erratas corregidas por EDUCATE; pendiente de decisión.")
    return dict(m=4, html=h, guia=guia(A, 4, decir=list(UI["icfes_decir"]), apoyo=notas))


def orden_dinamicas(mis):
    """Antes de qué bloque (1…4, contando desde 0) va cada dinámica E2–E4: el primero, desde el segundo
    bloque, que trae una tarjeta de su subestrategia."""
    r = P.REPARTO[mis]["clase"]
    pares = list(zip(r[::2], r[1::2]))
    est = {p: e for p, e, _, _ in P.TALLER_TODO[mis]}
    nombres = P.MISIONES[mis]["estr"]
    pos = {}
    for k in (1, 2, 3):
        cand = [j for j in range(1, 5) if any(est[n] == nombres[k] for n in pares[j])]
        pos[k] = cand[0] if cand else k
    return pares, pos


def escenas_contenido(A, mis):
    d = P.MISIONES[mis]
    sc = [CV.esc_portada(A, mis), CV.esc_reglas(A, mis)]
    ronda = P.ronda_de(mis)
    if ronda:
        sc.append(esc_ronda(A, mis))
    act = CV.esc_activacion(A, mis)
    act["html"] = act["html"].replace('<blockquote class="cita xl">', '<blockquote class="cita xl" lang="en">')
    if ronda:
        act["min"] = 2
    sc += [act, CV.esc_dinamica(A, mis, 0, 0)]
    # la pregunta modelo: la primera de las diez de clase, en inglés y en grande
    p1 = P.REPARTO[mis]["clase"][0]
    pr = CV.esc_problematizadora(A, mis)
    pr["html"] = pr["html"].replace(f"Abran el libro en la pregunta modelo del momento {mis}",
                                    f"Abran el libro: tarjeta {p1}, página {P.pag_libro(mis, p1)}")
    en, ops, _ = ITEMS[mis][p1]
    lis = "".join(f"<li><b>{L}</b><span>{E(o)}</span></li>" for L, o in zip(LETRAS, ops))
    pr["html"] = pr["html"].replace(
        '<div class="ctl">',
        f'<p class="en xl" lang="en">{E(en)}</p><ul class="eops{" banco" if len(ops) > 4 else ""}">{lis}</ul>'
        '<div class="ctl">', 1)
    viejos = "".join(f'<button class="btn tally" data-tally="h{mis}{L}">{L} <span class="n" id="h{mis}{L}">0</span></button>'
                     for L in "ABCD")
    nuevos = "".join(f'<button class="btn tally" data-tally="h{mis}{L}">{L} <span class="n" id="h{mis}{L}">0</span></button>'
                     for L in LETRAS[:len(ops)])
    assert viejos in pr["html"]
    pr["html"] = pr["html"].replace(viejos, nuevos)
    pr["html"] += (f'<div class="card big edge mt" style="--accent:var(--m2)"><h3>La pregunta de este momento</h3>'
                   f'<p class="lead">{E(P.PROBLEMATIZADORA[mis])}</p></div>')
    sc.append(pr)
    pares, pos = orden_dinamicas(mis)
    for j, (a, b_) in enumerate(pares):
        for k in (1, 2, 3):
            if pos[k] == j:
                sc.append(CV.esc_dinamica(A, mis, k, 2))
        sc.append(esc_bloque(A, mis, a, b_))
    sc.append(esc_reto(A, mis))
    for k, q in enumerate(A.preguntas_icfes(mis), 1):
        sc.append(esc_icfes(A, mis, k, q, P.BANCO[mis][k - 1]["clave"].strip(), A.textos[(mis, k)]))
    cierre = CV.esc_cierre(A, mis)
    casa = P.REPARTO[mis]["casa"]
    if casa:
        filas = "".join(
            f'<li>Tarjetas <b>{E(P.nums(ns))}</b> ({E(rot)}, páginas '
            f'{E(P.rango([P.pag_tarjeta(mis, n) for n in ns]))}): se revisan al comenzar la clase {c_}.</li>'
            for ns, c_, rot in casa)
        tarea = (f'<div class="card edge mt" style="--accent:var(--oro)"><h3>Para la casa</h3>'
                 f'<ol class="pasos">{filas}</ol><p class="sub">Con el instrumento lleno, como en clase. La ronda de '
                 f'claves es de cinco minutos.</p></div>')
    else:
        tarea = ('<div class="card edge mt" style="--accent:var(--oro)"><h3>Para la casa</h3>'
                 '<p>Esta misión no deja tarea: todas sus tarjetas se hicieron en clase o en el reto.</p></div>')
    cierre["html"] += tarea
    viejo = "La palabra nueva del día, en la franja de vocabulario, con tus palabras."
    cierre["html"] = cierre["html"].replace(viejo, "La palabra o la expresión del día, en la franja de vocabulario, "
                                                   "con tus palabras.")
    cierre["guia"]["apoyo"].insert(0, "Di la tarea en voz alta y que la anoten: " + (
        "; ".join(f"tarjetas {P.nums(ns)}, ronda en la clase {c_}" for ns, c_, _ in casa) if casa else "no hay."))
    sc.append(cierre)
    # portada: lo que el profe tiene que saber antes del sábado
    apoyo = ["⚑ Antes del sábado: " + P.limpia(d["ojo"]),
             f"Lo que no cabe en clase: {d['cierre']}",
             "Los cuatro conceptos que tienes que poder explicar hoy en dos minutos, sin jerga:"]
    apoyo += [f"{t}: {x}" for t, x in P.NO_ES_TU_FUERTE[mis]]
    apoyo.append("Cómo se dicen las palabras clave (la sílaba fuerte lleva tilde): " +
                 ", ".join(f"{w} ({p})" for w, p in P.PRONUNCIA[mis]) + ".")
    apoyo.append("Si un estudiante pregunta algo que no sabes, no inventes: «No lo sé; vamos a ver qué dice el "
                 "texto». Anótalo en tu registro y tráelo resuelto. Si alguien sabe más inglés, que lea en voz alta.")
    sc[0]["guia"]["apoyo"] = apoyo + sc[0]["guia"]["apoyo"]
    return sc



def escenas_simulacro(A, textos):
    """Clases 7 y 8 (decisión de Nelson, 10 nov): salen del motor con plan_ing.C7 y C8. La clase 8
    abre con la ronda de claves de la tarea de la Misión 6 (plan_ing.ronda_de(8)), dentro de la
    activación: sus 5 minutos se descuentan de los 15."""
    antes = [esc_ronda(A, 8)] if P.ronda_de(8) else []
    return CV.escenas_clase7(A), CV.escenas_clase8(A, antes=antes)


# ─────────────────────────────── escribir ───────────────────────────────
def revisar_pantalla(html_, archivo):
    hay = [n for n in PROHIBIDOS if re.search(r"\b" + re.escape(n) + r"\b", html_)]
    if hay:
        raise SystemExit(f"{archivo}: trae nombres que no pueden salir: {hay}")
    malo = [t for t in NO_EN_PANTALLA if re.search(r"\b" + re.escape(t) + r"(es)?\b", html_, re.I)]
    if malo:
        raise SystemExit(f"{archivo}: dice {malo}; el membrete es «Pregunta Saber 11»")


def escribir(A, archivo, titulo, sub, sc):
    html_ = CV.pagina(A, titulo, sub, sc, titulo).replace("</style>", CSS_EXTRA + "</style>", 1)
    revisar_pantalla(html_, archivo)
    f = os.path.join(A.out, archivo)
    with open(f, "w", encoding="utf-8") as fh:
        fh.write(html_)
    print(f"{archivo:34s} {len(sc):2d} diapositivas · {os.path.getsize(f)//1024} KB")
    return f, len(sc)


def verificar_items():
    malas = []
    for m in range(1, 7):
        if sorted(ITEMS[m]) != sorted(P.REPARTO[m]["clase"]):
            malas.append(f"M{m}: ITEMS {sorted(ITEMS[m])} · clase {P.REPARTO[m]['clase']}")
        for n, (en, ops, _) in ITEMS[m].items():
            if LETRAS.index(P.CLAVES[m][n]) >= len(ops):
                malas.append(f"M{m}·{n}: la clave {P.CLAVES[m][n]} no está entre {len(ops)} opciones")
            if m in (3, 6) and not re.search(r"\(\d+\) ____", en):
                malas.append(f"M{m}·{n}: falta el espacio numerado")
    return malas


def construir(out=OUT):
    global OUT
    OUT = out
    os.makedirs(out, exist_ok=True)
    malas = P.verificar() + verificar_items()
    if malas:
        raise SystemExit("No cuadra:\n  " + "\n  ".join(malas))
    textos = textos_ing.leer()
    for (m, k), v in textos.items():
        assert v["clave"] == P.BANCO[m][k - 1]["clave"].strip(), (m, k)
    P_ns = planeador()
    hechos = []
    for mis in range(1, 7):
        A = area(mis, P_ns, textos)
        A.out = out
        d = P_ns.MISIONES[mis]
        sc = escenas_contenido(A, mis)
        hechos.append(escribir(A, f"ING_Clase{mis}_Mision{mis}.html", f"Inglés · Clase {mis}",
                               f"Misión {mis} · {d['parte']} · páginas {d['pags']}", sc))
    A = area(1, P_ns, textos)
    A.out = out
    sc7, sc8 = escenas_simulacro(A, textos)
    hechos.append(escribir(A, "ING_Clase7_Simulacro.html", "Inglés · Clase 7", CV.subtitulos_simulacro(A)[0], sc7))
    hechos.append(escribir(A, "ING_Clase8_Devolucion.html", "Inglés · Clase 8", CV.subtitulos_simulacro(A)[1], sc8))
    return hechos


if __name__ == "__main__":
    construir(sys.argv[1] if len(sys.argv) > 1 else OUT)
