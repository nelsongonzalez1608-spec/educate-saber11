#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Inglés · Misión 5 · entrenamiento ICFES · páginas 325 y 330.

Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Claves verificadas (resueltas a mano contra el texto, no copiadas de la tabla de respuestas):

    QA · cuadernillo Inglés Saber 11 (Icfes 2024), Examen 1, Parte 6, n.º 25 · C   estrategia 1
    QB · cuadernillo Inglés Saber 11 (Icfes 2024), Examen 2, Parte 6, n.º 20 · A   estrategia 2
    QC · SIMULACRO II 2023 Oficio · Inglés, Parte 6, N.º 380                · B   estrategia 3
    QD · SIMULACRO II 2023 Oficio · Inglés, Parte 6, N.º 394                · A   estrategia 4

  25 · C: «One typical day I was too tired… to cook», «for whenever you don't feel like cooking
       yourself», «my usual take away restaurant»: Mark pide comida rápida algunas veces y le gusta.
       A exagera (no dice que no le guste cocinar, sino que a veces no tiene ganas); B («almost
       always») y D («tired of going to restaurants») no están en el texto. Tabla oficial: C.
  20 · A: el texto describe Colombia y la finca, y cierra con «Some of you reading this may feel
       inspired to do the same» (volver / viajar). B y C (comprar o manejar una finca) y D (escribir
       sobre los lugares) no son lo que busca. Tabla oficial: A.
 380 · B: «I wonder why people love gold and money so much nowadays, it's nothing special, just a
       metal. If you die, will you enjoy it?» y, después, lo que admira es la familia unida. A
       (aburrido cuando llueve), C (la comida) y D («the best places in the world») no son su actitud
       ante la vida; D además exagera lo que dice de los museos.
 394 · A: frente al espejo recuerda que llevó la misma ropa el día en que perdió el bolso y discutió
       con su pareja: «Not what you would call a successful day». Por eso deja de creer que la ropa da
       el éxito. B es falsa; C es cierta (casi todo es oscuro) pero no es lo que la hace cambiar; D
       toma al pie de la letra la broma de la ropa «deprimida».

Textos: el del cuadernillo 2024 (Examen 2, Jonathan) trae doce erratas impresas («Faador»,
«Cdombia», «caled Perera», «Cambia»…) y el de Swift Pizza dice «It left as if» por «It felt as if»;
los del SIMULACRO traen erratas de digitación («avaluable», «say with them»). El cuaderno imprime el
texto completo con la ortografía corregida y nada más cambiado; la lista exacta está en
tablero/propuestas/ing5_textos.md y en ing5_hallazgos.csv. Reservadas en
tablero/propuestas/ing_icfes_reservas.csv.
"""
from ing5 import *   # noqa: F401,F403  (configura la misión y EST)
from ing5 import rot, caja, pista, renglon, texto, tinte, tabla_vacia, parrafo


def lectura(b, x, y, w, titulo, parrafos, c=GRAY, size=18):
    """El texto de la pregunta, completo, en un recuadro con su título en inglés."""
    yy = y + 46
    partes = []
    for p in parrafos:
        svg, yy = TJ(x + 22, yy, p, w - 44, size, INK, lh=size + 5)
        partes.append(svg)
        yy += 6
    h = yy - y + 8
    b.append(rect(x, y, w, h, "white", r=12, stroke=c, sw=1.6))
    b.append(T(x + w / 2, y + 30, [titulo], 17, INK, weight="700", anchor="middle"))
    b.extend(partes)
    return y + h


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 14, txt, w, 20, INK, weight="700", lh=28)
    b.append(svg)
    return y2


# ───────── QA · 2024 · Examen 1 · n.º 25 · Swift Pizza ─────────
SWIFT = ("Today we have the pleasure of showing you the best letter written by our customer Mark. He wins £25 for "
         "writing about us this week. He is so happy with the orders at Swift Pizza and Sandwich House that he wants "
         "to declare a holiday to celebrate his experience here: “Happy burgerday and Merry Sandwichmas to everyone!” "
         "he wrote.",
         "Wednesday May 18, 2011. One typical day I was too tired after working all day long to cook for myself, and "
         "I was very hungry. I really wanted something to eat, so I decided to find a burger. I ordered a half-pound "
         "burger and a lamb and chicken sandwich. I also had some special requests about extra cheese and vegetables.",
         "Food arrived very fast (less than twenty minutes) and was hot and fresh. The burger was delicious, and left "
         "me wanting more – fortunately I had the sandwich left. It felt as if it was cut just a minute before I "
         "opened it – juicy, fresh, and great. Every single special request I made was completely satisfied, 100%! "
         "And the best thing was that all of the above and some drinks cost me ONLY 10 dollars! If that doesn't say "
         "value for money, I don't know what it does.",
         "It certainly feels great to find new excellent food delivery companies for whenever you don't feel like "
         "cooking yourself. I recently had a sad experience with my usual take away restaurant, so I decided to "
         "change to something else – and on my first try I got what I wanted! Order now from Swift Pizza and "
         "Sandwich House. Mark")


def datos_25(b, x, y, w):
    yy = lectura(b, x, y, w, "SWIFT PIZZA AND SANDWICH HOUSE", SWIFT)
    return pregunta(b, x, yy + 4, w, "It can be inferred from the text that Mark")


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "El reloj de Mark: ¿cada cuánto?", c,
                      "Como con la fotosíntesis: lo que el texto deja ver hay que poder señalarlo. Al lado de cada "
                      "frase, escribe qué deja ver de Mark y encierra con qué frecuencia pasa.")
    x0, ww = x + 22, w - 44
    cols = (470, ww - 470 - 280, 280)
    yy = tabla_vacia(b, x0, yy, cols, ("LA FRASE DEL TEXTO", "LO QUE DEJA VER DE MARK", "¿CADA CUÁNTO?"),
                     ("One typical day… too tired… to cook", "for whenever you don't feel like cooking",
                      "my usual take away restaurant"), c, rh=50, hh=38, size=15, sin_renglon=(2,))
    for k in range(3):
        texto(b, x0 + 470 + ww - 470 - 280 + 140, yy - 150 + k * 50 + 32, "siempre · a veces · nunca", size=15,
              color=GRAY, anchor="middle")
    return yy


# ───────── QB · 2024 · Examen 2 · n.º 20 · Jonathan ─────────
JONATHAN = ("I went to Colombia last summer. My journey began on the Caribbean coast and ended on the border with "
            "Ecuador. Colombia is a splendid country, extremely diverse and full of wonderful people. I will tell you "
            "why.",
            "In South Colombia there is a city called Pereira, just outside you can find an area where you will see "
            "the farm Villa Maria – a hidden paradise that takes a long time to get to. It is a working coffee farm "
            "located in the middle of a valley. Coffee and plantain grow as far as the eye can see. The farm is made "
            "up of the house and the processing plant. The family business has guests at the house for just $45.000 "
            "a night. This includes three home-cooked meals a day, a swimming pool, and as much coffee as you can "
            "drink. The scene is quite unbelievable. Bamboo chairs rest on the corners of the Villa, mangos hang from "
            "the trees and parrots and birds fly wild.",
            "A wonderful man named Hector who runs the farm is happy to show guests around the coffee processing "
            "plant. By day, the only sounds are of the horses coming down the valley side carrying food. By night, "
            "the wildlife comes alive, and depending on the time of the year thunderstorms offer a spectacular light "
            "show. For those who wish to escape, Villa Maria is the answer.",
            "This is just one attraction of many in Colombia. I could write pages on the country and not get bored. I "
            "graduate next year and I can't wait to return to this beautiful country. Some of you reading this may "
            "feel inspired to do the same.")


def datos_20(b, x, y, w):
    yy = lectura(b, x, y, w, "JONATHAN'S TRIP TO COLOMBIA", JONATHAN)
    return pregunta(b, x, yy + 4, w, "What is the writer trying to do in this article?")


def ii2(b, x, y, w, h):
    c = EST[2][1]
    yy = titulo_instr(b, x, y, "La última línea delata el propósito", c,
                      "Como con el andén roto: los detalles están al servicio de algo. Lee la última oración y "
                      "contesta, con el texto en la mano, a quién le habla Jonathan y qué espera que haga.")
    x0, ww = x + 22, w - 44
    cols = (420, ww - 420)
    return tabla_vacia(b, x0, yy, cols, ("LO QUE BUSCO", "LO QUE ENCONTRÉ EN EL TEXTO"),
                       ("«Some of you reading this» son…", "«to do the same» quiere decir…",
                        "lo de la finca le sirve para…"), c, rh=60, hh=38, size=15)


# ───────── QC · SIM. II 2023 · N.º 380 · My trip to Bogotá ─────────
BOGOTA = ("I arrived in Bogotá feeling excited and ready to explore a big city. Unfortunately, many hours of "
          "unstoppable rain didn't allow me to go out for a while. It rains a lot there, maybe more than in Wales, and "
          "I never thought that was possible.",
          "First: I decided to visit a museum. I think museums are now more interesting and enjoyable places than "
          "before. I visited the gold museum and saw the gold from all over Colombia. Ancient people used to stick "
          "little gold pieces to their clothes during religious activities. They never considered it as a valuable "
          "metal. I wonder why people love gold and money so much nowadays, it's nothing special, just a metal. If "
          "you die, will you enjoy it?",
          "After that, I went and stayed with a family I met at the museum. They invited me to stay with them in "
          "Chía. They live on the land that used to be their parents' farm. That's why they have divided it in "
          "smaller parts, which means that they all live close to, next to, opposite or near each other. That is one "
          "really close and warm family! The houses are old and badly arranged, built by themselves in different "
          "styles, but all beautiful and amazing. To have such a beautiful sense of family was something I had not "
          "seen in my whole life.",
          "Finally, we went to a restaurant called “EL PORTICO”. It's a huge place, with a fantastic view, and the "
          "food I ate was great. This was the part I like the most Colombian food is magnificent.")


def datos_380(b, x, y, w):
    yy = lectura(b, x, y, w, "MY TRIP TO BOGOTA AND OTHERS", BOGOTA)
    return pregunta(b, x, yy + 4, w, "What do we know about the writer's attitude towards life?")


def ii3(b, x, y, w, h):
    c = EST[3][1]
    yy = titulo_instr(b, x, y, "Una pregunta que no espera respuesta", c,
                      "Como con «I am here, my story matters»: la frase dice más de lo que dice. Contesta tú la "
                      "pregunta del autor y saca lo que cree.")
    x0, ww = x + 22, w - 44
    cols = (500, ww - 500)
    return tabla_vacia(b, x0, yy, cols, ("LO QUE SE PREGUNTA", "LO QUE YO CONTESTO"),
                       ("«If you die, will you enjoy it?» → la respuesta es…",
                        "entonces, para él, el oro y el dinero…",
                        "lo que sí le parece valioso (párrafo de Chía)…"), c, rh=60, hh=38, size=15)


# ───────── QD · SIM. II 2023 · N.º 394 · What to wear? ─────────
WEAR = ("Hello dear readers.",
        "It's February and London Fashion Week has just ended. Fashion shows have been happening around the city. "
        "Magazines are full of chats about who the model of the moment is. Superstars and journalists have announced "
        "what the best dressed will be wearing in the coming seasons. Honestly, clothes can make you happy. I have "
        "decided that tomorrow I will dress success.",
        "At 7.30 AM, I remember my promise. I decided that dressing for success means more than putting on my clothes "
        "the right way. I need to look good and feel good! The right clothing will make me feel confident and all my "
        "problems will disappear. Colleagues will be proud of me and I will get a better position.",
        "I open my closet and notice that most of my clothes are black, brown and grey. They hang down sadly on their "
        "hangers. Are they depressed? I decide that a bright color is needed for successful dressing, and choose a red "
        "sweater. Now, I also want to look cool and casual – I take the blue jean shorts. Finally, it's cold outside; "
        "black tights and long boots are a fashion rule. I look in the mirror. I realize that I wore exactly the same "
        "clothing two days ago. That was the day I lost my purse and had an argument with my partner. Not what you "
        "would call a successful day. I look in my closet. My black, grey and brown clothes seem to fall even further "
        "down. I shut the drawer of my closet and think that success is a state of mind and decide not to pay "
        "attention to London Fashion Week.")


def datos_394(b, x, y, w):
    yy = lectura(b, x, y, w, "WHAT TO WEAR?", WEAR)
    return pregunta(b, x, yy + 4, w, "The writer's opinion changed because")


def ii4(b, x, y, w, h):
    c = EST[4][1]
    yy = titulo_instr(b, x, y, "Antes y después del espejo", c,
                      "Como con el ruido y el bolero: pon frente a frente lo que ella creía y lo que piensa al final. "
                      "La causa del cambio es lo que pasó en el medio.")
    x0, ww = x + 22, w - 44
    cols = (230, (ww - 230) / 3, (ww - 230) / 3, (ww - 230) / 3)
    return tabla_vacia(b, x0, yy, cols, ("", "A LAS 7.30 CREÍA QUE…", "FRENTE AL ESPEJO RECORDÓ…",
                                         "AL CERRAR EL CLÓSET PIENSA…"),
                       ("con palabras del texto", "en mis palabras"), c, rh=62, hh=38, size=15)


QA = dict(est=1, comp="Lectura · inferencia",
          e="Lea el artículo y luego responda la pregunta.",
          o=["does not like cooking food for himself.", "almost always eats hamburgers.",
             "enjoys eating fast food sometimes.", "is tired of going to restaurants."],
          datos=datos_25, inst=ii1)
QB = dict(est=2, comp="Lectura · propósito del autor",
          e="Lea el artículo y luego responda la pregunta.",
          o=["encouraging tourists to visit Colombia.", "convincing people to buy a Colombian coffee farm.",
             "telling readers to run a coffee business in Colombia.",
             "inviting tourists to write about places they visit in Colombia."],
          datos=datos_20, inst=ii2)
QC = dict(est=3, comp="Lectura · sentido figurado",
          e="Lea el texto y responda la pregunta.",
          o=["A place is really boring when it rains.", "Other things are more important than money.",
             "Food must always be well prepared.", "Museums are the best places in the world."],
          datos=datos_380, inst=ii3)
QD = dict(est=4, comp="Lectura · contraste implícito",
          e="Lea el texto y responda la pregunta.",
          o=["nothing good happened when she wore the same.", "she realized that she couldn't feel or look better.",
             "she had only dark color clothing to wear.", "her clothes looked really miserable."],
          datos=datos_394, inst=ii4)


def build(pages=(325, 330)):
    return [hoja_icfes("ing5_i1", pages[0], QA, QB, vocab=False),
            hoja_icfes("ing5_i2", pages[1], QC, QD, vocab=False)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
