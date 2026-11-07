#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Química · Misión 6 · entrenamiento ICFES · páginas 220 y 224 · INCOMPLETO.

Estado al 7 nov 2026: solo hay UNA pregunta oficial verificada y libre para esta misión. Las
preguntas de química de los cuadernillos 2016-1 que hay en Drive («1. CUADERNILLOS ICFES»)
ya están reservadas por Química M1 a M4 (tablero/propuestas/qui_icfes_reservas.csv) o usadas
por Biología; el resto de la carpeta son simulacros de editoriales y pruebas propias (PTD,
MULTIPRUEBAS), que no son preguntas oficiales. Faltan tres preguntas (estrategias 2, 3 y 4):
no se inventan. build() se niega a construir hasta que estén.

Membrete siempre genérico (regla 7): «Pregunta oficial ICFES · Saber 11».

Pregunta verificada (resuelta a mano contra la figura del cuadernillo, no copiada):

    QA · 2016-1, 2.ª sesión (ABD), Ciencias Naturales, ítem 68 · B   estrategia 1

  68 · B: el Mg tiene 12 protones; el ion Mg²⁺ perdió 2 electrones: 12 p⁺ y 10 electrones
       (2 + 8, la capa externa vacía). Figuras del cuadernillo: A = 14 p⁺, 12 e⁻ (2-8-2);
       B = 12 p⁺, 10 e⁻ (2-8); C = 12 p⁺, 12 e⁻ (2-8-2, el átomo neutro); D = 14 p⁺, 10 e⁻ (2-8).
       Verificada contra la página 22 del escaneo (Drive «2016-2 SEGUNDA SESION.pdf», cuya
       portada dice 2016-1 segunda sesión). Reservada en qui_icfes_reservas.csv.

Adaptación de formato: las cuatro figuras se redibujan con los mismos números de protones y la
misma distribución de electrones por capa.
"""
from qui6 import *   # noqa: F401,F403  (configura la misión y EST)
from qui6 import rot, caja, pista, renglon, texto, tinte, tabla_vacia


def pregunta(b, x, y, w, txt):
    svg, y2 = TJ(x, y + 22, txt, w, 20, INK, lh=28)
    b.append(svg)
    return y2


# ───────── QA · ítem 68 · el ion Mg²⁺ ─────────
def atomo(b, cx, cy, protones, capas, r0=24, dr=26):
    """Modelo de capas: núcleo con «Np⁺» y electrones repartidos en cada capa."""
    b.append(f'<circle cx="{cx}" cy="{cy}" r="{r0}" fill="#EEF0F4" stroke="{INK}" stroke-width="1.8"/>')
    texto(b, cx, cy + 6, f"{protones}p⁺", size=15, anchor="middle", weight="700")
    for k in range(3):
        b.append(f'<circle cx="{cx}" cy="{cy}" r="{r0 + dr * (k + 1)}" fill="none" stroke="{INK}" '
                 f'stroke-width="1.6"/>')
    for k, n in enumerate(capas):
        r = r0 + dr * (k + 1)
        for i in range(n):
            a = 2 * math.pi * i / n - math.pi / 2 + 0.35 * k
            ex, ey = cx + r * math.cos(a), cy + r * math.sin(a)
            b.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="6" fill="white" stroke="{INK}" stroke-width="1.6"/>')


def datos_68(b, x, y, w):
    caja(b, x, y + 4, 330, 40, GRAY, r=6)
    texto(b, x + 16, y + 30, "Convenciones:  ○ = electrones   p⁺ = protones", size=16)
    figs = (("A", 14, (2, 8, 2)), ("B", 12, (2, 8)), ("C", 12, (2, 8, 2)), ("D", 14, (2, 8)))
    fw = w / 4
    for k, (L, p, capas) in enumerate(figs):
        cx = x + fw * k + fw / 2
        texto(b, cx, y + 76, L + ".", size=19, weight="700", anchor="middle")
        atomo(b, cx, y + 196, p, capas)
    return y + 310


def ii1(b, x, y, w, h):
    c = EST[1][1]
    yy = titulo_instr(b, x, y, "Protones y electrones en cada dibujo", c,
                      "Como con las ecuaciones: aquí también se cuenta. Cuenta en cada modelo y calcula su carga. "
                      "Antes, escribe qué te dicen el «12» y el «2+» del enunciado.")
    x0, ww = x + 22, w - 44
    pista(b, x0, yy + 20, "número atómico 12 quiere decir…")
    renglon(b, x0 + 230, yy + 22, x0 + ww / 2 - 20)
    pista(b, x0 + ww / 2, yy + 20, "«2+» quiere decir que el átomo…")
    renglon(b, x0 + ww / 2 + 230, yy + 22, x0 + ww)
    yy += 38
    cols = (150, (ww - 150) / 4, (ww - 150) / 4, (ww - 150) / 4, (ww - 150) / 4)
    return tabla_vacia(b, x0, yy, cols, ("", "A", "B", "C", "D"),
                       ("protones", "electrones", "carga (p − e)"), c, rh=50, hh=40, size=16)


QA = dict(est=1, comp="Uso comprensivo del conocimiento científico",
          e="El magnesio metálico (Mg, número atómico = 12) forma iones Mg²⁺ y aumenta su número de oxidación. "
            "La figura que representa el ion Mg²⁺ es",
          o=["la figura A.", "la figura B.", "la figura C.", "la figura D."],
          datos=datos_68, inst=ii1)

# Faltan: QB (estrategia 2 · ¿El calor sale o entra?), QC (estrategia 3 · Una conclusión vale lo
# que valen sus datos) y QD (estrategia 4 · Piezas que se repiten: los polímeros).
QB = QC = QD = None


def build(pages=(220, 224)):
    faltan = [n for n, q in (("QB", QB), ("QC", QC), ("QD", QD)) if q is None]
    if faltan:
        raise SystemExit("qui6_icfes: faltan preguntas oficiales verificadas: " + ", ".join(faltan) +
                         ". No se inventan (regla 7); ver el docstring.")
    return [hoja_icfes("qui6_i1", pages[0], QA, QB),
            hoja_icfes("qui6_i2", pages[1], QC, QD)]


if __name__ == "__main__":
    for f in build():
        print("ok", f)
