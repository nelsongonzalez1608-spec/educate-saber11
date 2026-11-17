"""Conceptualización dentro de la guía de clase («clase viva»). Decisión de Nelson, 17 nov.

No es una presentación aparte: son DOS diapositivas que entran en la guía de cada clase de contenido,
entre la activación y la dinámica de la estrategia 1, dentro de los 15 minutos de la Activación
(el reparto 15·20·35·20·20·10 no cambia):

  1. «Las palabras de hoy»: el vocabulario de la misión, palabra y definición de una línea.
  2. «El mapa de la misión»: una idea central y una tarjeta por estrategia. Cada tarjeta se abre
     con un clic y muestra su infografía: dibujo, definición corta, fórmula, ejemplo y el «ojo».

Primero descubren (activación), después se nombra (conceptualización), después se entrena (dinámica).

Estilo (Nelson): limpio, fondo claro, colores institucionales solo como acento, nada de fondos
sólidos detrás del texto, «3D» liviano (sombra corrida y figuras isométricas), sin recargar.

Uso desde un módulo de guía:
    import conceptos
    sc[pos:pos] = conceptos.escenas(A, mis, DATOS[mis], color_est)
y añadir conceptos.CSS a la hoja de estilos de la página.

DATOS[mis] = dict(
    centro=(titulo, definicion, figura_svg),
    ideas=[dict(t=titulo, d=definicion, f=formula, ej=ejemplo, ojo=advertencia, svg=figura), …],
    vocab=[(palabra, definicion), …],
    decir=[…], apoyo=[…])        # para la guía del profe
"""
from html import escape as E

MIN = 3          # minutos que se toma la conceptualización dentro de la Activación

CSS = """
.cv-voc{display:grid;gap:clamp(10px,1.2vw,18px);grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));margin-top:clamp(14px,1.8vw,26px)}
.cv-voc div{background:#fff;border:1.5px solid var(--line);border-top:5px solid var(--acc,var(--area));border-radius:14px;padding:12px 16px;box-shadow:4px 4px 0 rgba(30,34,48,.08)}
.cv-voc b{display:block;font-family:var(--display);font-size:1.18em;color:var(--ink)}
.cv-voc span{color:var(--muted)}
.cv-voc.tapar span{visibility:hidden}
.cv-mapa{position:relative;display:grid;gap:clamp(14px,2vw,34px);grid-template-columns:1fr 1.1fr 1fr;grid-template-areas:"a . b" ". c ." "d . e";margin-top:clamp(12px,1.6vw,22px)}
.cv-mapa>svg{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.cv-nodo{font:inherit;text-align:left;cursor:pointer;background:#fff;border:2px solid var(--acc);border-radius:16px;padding:12px 16px;box-shadow:6px 6px 0 var(--acc);transition:transform .15s, box-shadow .15s;position:relative}
.cv-nodo:hover{transform:translate(-2px,-2px);box-shadow:8px 8px 0 var(--acc)}
.cv-nodo .n{display:inline-grid;place-items:center;width:1.7em;height:1.7em;border-radius:50%;background:var(--acc);color:#fff;font-family:var(--display);font-weight:800;margin-right:8px}
.cv-nodo b{font-family:var(--display);font-size:1.12em}
.cv-nodo small{display:block;color:var(--muted);font-size:.9em;margin-top:4px}
.cv-centro{grid-area:c;text-align:center;border-width:3px}
.cv-centro b{font-size:1.35em;color:var(--acc)}
.cv-det{margin-top:clamp(14px,1.8vw,26px);display:grid;gap:clamp(14px,2vw,30px);grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);align-items:center;background:#fff;border:1.5px solid var(--line);border-left:6px solid var(--acc);border-radius:18px;padding:clamp(14px,1.8vw,28px)}
.cv-det svg{width:100%;height:auto;max-height:52vh}
.cv-mapa[hidden],.cv-det[hidden]{display:none}
.cv-det h3{color:var(--acc)}
.cv-f{display:inline-block;font-family:ui-monospace,Menlo,Consolas,monospace;font-weight:700;font-size:1.12em;border:2px dashed var(--acc);border-radius:10px;padding:4px 12px;margin:4px 0 8px}
.cv-ej{color:var(--muted)}
.cv-ojo{margin-top:8px;padding-left:12px;border-left:4px solid var(--oro)}
.cv-ojo b{color:var(--oro)}
#wrap{position:relative}
.cv-motivo{position:absolute;top:-6px;right:0;width:clamp(110px,13vw,220px);opacity:.22;pointer-events:none;z-index:0}
.cv-motivo svg{width:100%;height:auto;display:block}
.cv-motivo~*{position:relative;z-index:1}
@media (max-width:760px){.cv-motivo{display:none}}
@media (max-width:760px){.cv-mapa{grid-template-columns:1fr;grid-template-areas:"c" "a" "b" "d" "e"}.cv-mapa>svg{display:none}.cv-det{grid-template-columns:1fr}}
"""

# El JavaScript del motor ya abre y cierra con data-show; aquí hace falta «una sola a la vez».
JS = """
wrap.addEventListener("click", function(e){
  var b = e.target.closest("[data-cv]"), v = e.target.closest("[data-cvback]");
  if(b){ var d = document.getElementById(b.dataset.cv), m = document.getElementById(b.dataset.cvg);
    if(d && m){ m.hidden = true; d.hidden = false; } }
  if(v){ var d2 = document.getElementById(v.dataset.cvback), m2 = document.getElementById(v.dataset.cvg);
    if(d2 && m2){ d2.hidden = true; m2.hidden = false; } }
  var t = e.target.closest("[data-tapar]");
  if(t){ var x = document.getElementById(t.dataset.tapar); x.classList.toggle("tapar");
    t.textContent = x.classList.contains("tapar") ? "Destapar las definiciones" : "Tapar las definiciones"; }
});
"""

AREAS_GRID = ["a", "b", "d", "e"]


def motivo_html(A):
    """El toque del área (motivos.py), en la esquina de la diapositiva. Vacío si el área no lo tiene."""
    import motivos
    clave = motivos.CLAVE.get(getattr(A, "nombre", ""), None)
    return f'<div class="cv-motivo">{motivos.motivo(clave)}</div>' if clave else ""


def _guia(obj, decir, apoyo):
    return dict(obj=obj, decir=list(decir), como="", apoyo=list(apoyo))


def esc_vocabulario(A, mis, D, colores):
    tarjetas = "".join(
        f'<div style="--acc:{colores[k % len(colores)]}"><b>{E(p)}</b><span>{E(d)}</span></div>'
        for k, (p, d) in enumerate(D["vocab"]))
    h = (motivo_html(A) + f'<div class="eyebrow"><span class="min" style="--accent:var(--m1)">Conceptualización · {MIN} min</span>'
         f'<span class="kicker">Las palabras de hoy</span></div>'
         f'<h2>{len(D["vocab"])} palabras para esta clase</h2>'
         f'<div class="cv-voc" id="voc{mis}">{tarjetas}</div>'
         f'<div class="ctl"><button class="btn" data-tapar="voc{mis}">Tapar las definiciones</button></div>')
    return dict(m=0, min=MIN, html=h, guia=_guia(
        "Que el grupo tenga a la vista, desde el principio, las palabras con las que se va a hablar hoy.",
        ["Lee las palabras en voz alta, una vez, sin explicar ninguna: «estas son las palabras de hoy».",
         "Juego de un minuto: tapa las definiciones, di una definición y que el grupo responda la palabra."],
        ["No es una clase de vocabulario: son treinta segundos de lectura y un minuto de juego. "
         "Las palabras se aprenden usándolas en el taller.",
         "Si una palabra ya salió en la activación, señálala: «esta es la que dijo …»."]))


def esc_mapa(A, mis, D, colores):
    ct, cd, csvg = D["centro"]
    g = f"cv{mis}"
    nodos = [f'<button class="cv-nodo cv-centro" style="--acc:var(--area)" data-cv="{g}c" data-cvg="{g}"><b>{E(ct)}</b><small>{E(cd)}</small></button>']
    dets = [_detalle(f"{g}c", g, "var(--area)", ct, cd, None, D.get("centro_ej"), D.get("centro_ojo"), csvg)]
    for k, idea in enumerate(D["ideas"]):
        c = colores[k % len(colores)]
        nodos.append(f'<button class="cv-nodo" style="--acc:{c};grid-area:{AREAS_GRID[k]}" data-cv="{g}{k}" '
                     f'data-cvg="{g}"><span class="n">{k+1}</span><b>{E(idea["t"])}</b>'
                     f'<small>{E(idea["corto"])}</small></button>')
        dets.append(_detalle(f"{g}{k}", g, c, idea["t"], idea["d"], idea.get("f"), idea.get("ej"),
                             idea.get("ojo"), idea["svg"]))
    lineas = ('<svg aria-hidden="true" viewBox="0 0 100 100" preserveAspectRatio="none">'
              + "".join(f'<line x1="50" y1="50" x2="{x}" y2="{y}" stroke="#9AA3B2" stroke-width="2" '
                        f'stroke-dasharray="6 6" vector-effect="non-scaling-stroke"/>'
                        for x, y in ((18, 16), (82, 16), (18, 84), (82, 84))) + '</svg>')
    h = (motivo_html(A) + f'<div class="eyebrow"><span class="min" style="--accent:var(--m1)">Conceptualización · {MIN} min</span>'
         f'<span class="kicker">El mapa de la misión · toca una tarjeta para abrirla</span></div>'
         f'<h2>{E(D["titulo"])}</h2>'
         f'<div class="cv-mapa" id="{g}">{lineas}{"".join(nodos)}</div>{"".join(dets)}')
    return dict(m=0, min=MIN, html=h, guia=_guia(
        "Ponerle nombre a lo que el grupo acaba de descubrir en la activación: una idea central y una "
        "por estrategia.",
        D["decir"], list(D["apoyo"]) + _chequeos(D)))


def _chequeos(D):
    """Para la guía del profe: la pregunta con la que comprueba que cada idea quedó (respuesta entre paréntesis)."""
    out = []
    if D.get("centro_chequeo"):
        out.append(f"Para comprobar la idea central: {D['centro_chequeo']}")
    for k, i in enumerate(D["ideas"], 1):
        if i.get("chequeo"):
            out.append(f"Estrategia {k} · {i['t']}: {i['chequeo']}")
    return out


def _detalle(ident, g, c, t, d, f, ej, ojo, svg):
    der = f'<h3>{E(t)}</h3><p>{E(d)}</p>'
    if f:
        der += f'<span class="cv-f">{E(f)}</span>'
    if ej:
        der += f'<p class="cv-ej"><b>Ejemplo:</b> {E(ej)}</p>'
    if ojo:
        der += f'<p class="cv-ojo"><b>Ojo:</b> {E(ojo)}</p>'
    der += (f'<div class="ctl"><button class="btn" data-cvback="{ident}" data-cvg="{g}">'
            f'← Volver al mapa</button></div>')
    return (f'<div class="cv-det" id="{ident}" hidden style="--acc:{c}">'
            f'<div>{svg}</div><div>{der}</div></div>')


def escenas(A, mis, D, colores):
    return [esc_vocabulario(A, mis, D, colores), esc_mapa(A, mis, D, colores)]


# ═══════════════════════ la hoja del planeador ═══════════════════════
# Una hoja por clase de contenido: «Clase N · conceptualización». Mismo motor que el planeador
# (SVG 2000 × 2588). La usa plan_mate.py; las otras áreas la llaman igual cuando tengan sus datos.
def _fig(svg, x, y, w):
    """Inserta la figura (viewBox 420 × 300) en el SVG de la hoja, al ancho w."""
    import re
    vb = re.search(r'viewBox="0 0 (\d+) (\d+)"', svg)
    vw, vh = int(vb.group(1)), int(vb.group(2))
    h = w * vh / vw
    return svg.replace("<svg ", f'<svg x="{x}" y="{y}" width="{w}" height="{h:.0f}" ', 1), h


def _bloque_idea(b, x, y, w, i, color, rotulo, L, medir=False):
    """Tarjeta de una idea. Devuelve el alto. Con medir=True no dibuja nada."""
    T, rect, parrafo_j, wrap_px, tw, INK, GRAY = L["T"], L["rect"], L["parrafo_j"], L["wrap_px"], L["tw"], L["INK"], L["GRAY"]
    pad, fw = 26, 240
    tx, tw_ = x + pad + fw + 26, w - pad * 2 - fw - 26
    sink = [] if medir else b
    # cabecera de la tarjeta, al lado de la figura
    yy = y + pad
    sink.append(T(tx, yy + 18, [rotulo.upper()], 17, color, weight="700", ls=1.3))
    yy += 30
    yy = parrafo_j(sink, tx, yy, i["t"], tw_, 27, INK, weight="700") + 4
    yy = parrafo_j(sink, tx, yy, i["d"], tw_, 21, INK, lh=29)
    fig, fh = _fig(i["svg"], x + pad, y + pad, fw)
    yy = max(yy, y + pad + fh) + 12
    # fórmula en recuadro punteado
    if i.get("f"):
        fl = wrap_px(i["f"], 22, w - pad * 2 - 30, weight="700")
        fh2 = 18 + len(fl) * 30
        sink.append(rect(x + pad, yy, min(w - pad * 2, max(tw(" ".join(l), 22, "700") for l in fl) + 34), fh2,
                         "white", r=10, stroke=color, sw=2, dash="7,6"))
        sink.append(T(x + pad + 16, yy + 32, [" ".join(l) for l in fl], 22, INK, weight="700", lh=30))
        yy += fh2 + 12
    for rot, txt, c in (("Ejemplo", i["ej"], GRAY), ("Ojo", i["ojo"], INK), ("Comprueba", i["chequeo"], INK)):
        sink.append(T(x + pad, yy + 20, [rot.upper()], 16, color if rot != "Ojo" else "#C9821B", weight="700", ls=1.2))
        yy = parrafo_j(sink, x + pad, yy + 24, txt, w - pad * 2, 20, c, lh=26) + 4
    h = yy - y + pad - 6
    if not medir:
        b.append(fig)
    return h


def hoja_planeador(b, y, D, colores, L, seccion, nota, area_color, area_bg, area_ln):
    """Dibuja la hoja de conceptualización desde y. L: primitivas de lib (dict). Devuelve el y final."""
    T, rect, parrafo_j, wrap_px, tw, INK, GRAY, M, CW = (L[k] for k in
        ("T", "rect", "parrafo_j", "wrap_px", "tw", "INK", "GRAY", "M", "CW"))
    y = nota(b, M, y,
             CW, "Al cierre de la Activación (3 min), antes de la dinámica de la estrategia 1: primero descubren, después "
             "se nombra, después se entrena. En pantalla: «las palabras de hoy» y «el mapa de la misión». Abres el centro "
             "y la estrategia 1; las demás, cuando llegue su pregunta en el taller. Una frase por tarjeta y la pregunta "
             "de «comprueba».",
             "#C9821B", "#FDF5E7", "#E8CFA3", "Cuándo y cómo", 22) + 26
    y = seccion(b, y, f"El mapa de la misión · {D['titulo']}")
    # la idea central, a todo el ancho
    ct, cd, csvg = D["centro"]
    centro = dict(t=ct, d=cd, f="", ej=D.get("centro_ej", ""), ojo=D.get("centro_ojo", ""),
                  chequeo=D.get("centro_chequeo", ""), svg=csvg)
    h = _bloque_idea(None, M, y, CW, centro, area_color, "La idea central", L, medir=True)
    b.append(rect(M, y, CW, h, area_bg, r=18, stroke=area_ln, sw=2))
    b.append(rect(M + 12, y + 14, 5, h - 28, area_color, r=3))
    _bloque_idea(b, M, y, CW, centro, area_color, "La idea central", L)
    y += h + 18
    # las cuatro estrategias, de a dos
    an = (CW - 18) / 2
    for fila in range(2):
        par = D["ideas"][fila * 2: fila * 2 + 2]
        hs = [_bloque_idea(None, 0, 0, an, i, colores[fila * 2 + k], f"Estrategia {fila*2+k+1}", L, medir=True)
              for k, i in enumerate(par)]
        hh = max(hs)
        for k, i in enumerate(par):
            x = M + k * (an + 18)
            c = colores[fila * 2 + k]
            b.append(rect(x, y, an, hh, "white", r=18, stroke=area_ln, sw=2))
            b.append(rect(x + 12, y + 14, 5, hh - 28, c, r=3))
            _bloque_idea(b, x, y, an, i, c, f"Estrategia {fila*2+k+1}", L)
        y += hh + 18
    # el vocabulario
    y = seccion(b, y + 6, "Las palabras de hoy",
                "Se leen una vez en voz alta al empezar; después se juega: dices la definición y el grupo dice la palabra.")
    col = 3
    aw = (CW - 2 * 14) / col
    filas = [D["vocab"][k:k + col] for k in range(0, len(D["vocab"]), col)]
    for fila in filas:
        hh = max(50 + len(wrap_px(d, 19, aw - 44)) * 25 + 8 for p, d in fila)
        for k, (p, d) in enumerate(fila):
            x = M + k * (aw + 14)
            b.append(rect(x, y, aw, hh, "white", r=12, stroke=area_ln, sw=1.8))
            b.append(rect(x + 10, y + 10, 4, hh - 20, colores[(filas.index(fila) * col + k) % len(colores)], r=2))
            b.append(T(x + 26, y + 34, [p], 22, INK, weight="700"))
            parrafo_j(b, x + 26, y + 42, d, aw - 44, 19, GRAY, lh=25)
        y += hh + 10
    return y


# ═══════════════════════ uso general (las siete áreas) ═══════════════════════
DECIR = ["«Lo que acaban de descubrir tiene nombre». Toca la tarjeta del centro y dila en una frase.",
         "Abre solo la tarjeta de la estrategia 1: es la que se entrena ya en la dinámica. Las demás se "
         "abren cuando aparezcan en el taller: vuelve a esta diapositiva con ← cuando haga falta.",
         "Una frase por tarjeta, nada más. Si alguien pregunta algo largo: «lo vemos en la pregunta que toca»."]
APOYO = ["Lo de las tarjetas está para reconocerlo en el taller, no para memorizarlo hoy.",
         "Los ejemplos son propios de la guía: no son los del libro, para que no resuelvan el taller por "
         "adelantado.",
         "La conceptualización se toma 3 de los 15 minutos de la Activación. Si la activación se alargó, pasa "
         "directo a la dinámica: el mapa sigue disponible para el cierre."]
COLOR_CENTRO = "#242478"


def armar(datos_mision, orden, color_de):
    """Datos de un módulo conceptos_<área>.py → lo que dibujan escenas() y hoja_planeador().
    orden: nombres de las estrategias en el orden del cuaderno. color_de(nombre) → color de la estrategia.
    Las figuras son funciones que reciben el color."""
    D = datos_mision
    ct, cd, cfig = D["centro"]
    faltan = [n for n in orden if n not in D["ideas"]]
    sobran = [n for n in D["ideas"] if n not in orden]
    assert not faltan and not sobran, f"estrategias que no cuadran · faltan {faltan} · sobran {sobran}"
    ideas = []
    for nombre in orden:
        i = dict(D["ideas"][nombre], t=nombre)
        i["svg"] = i["svg"](color_de(nombre))
        i.setdefault("f", "")
        ideas.append(i)
    out = dict(D, centro=(ct, cd, cfig(COLOR_CENTRO)), ideas=ideas,
               decir=D.get("decir", DECIR), apoyo=D.get("apoyo", APOYO))
    for i in ideas:
        falta = [k for k in ("t", "corto", "d", "ej", "ojo", "chequeo", "svg") if not i.get(k)]
        assert not falta, (i["t"], falta)
    for k in ("titulo", "centro_ej", "centro_ojo", "centro_chequeo", "vocab"):
        assert out.get(k), f"falta {k}"
    assert 6 <= len(out["vocab"]) <= 9, "el vocabulario lleva de 6 a 9 palabras"
    return out


def insertar_guia(sc, A, mis, D, colores):
    """Mete las dos diapositivas después de la activación (la primera escena del momento 0 que no es
    dinámica). Devuelve sc."""
    for k, e in enumerate(sc):
        if e.get("m") == 0 and ">Activación<" in e["html"][:600]:
            sc[k + 1:k + 1] = escenas(A, mis, D, colores)
            return sc
    raise ValueError("no encontré la activación")


def para_guia(A, mis, sc):
    """Gancho de las guías de las seis áreas (Matemáticas mete la suya en clase_viva_mate.py): si el área
    tiene conceptualización para la misión, la inserta después de la activación."""
    import motivos, conceptos_area
    clave = motivos.CLAVE.get(getattr(A, "nombre", ""))
    if not clave or clave == "mate":
        return sc
    D, cols = conceptos_area.de(clave, mis)
    if D:
        insertar_guia(sc, A, mis, D, cols)
    return sc


def motivo_cabecera(b, area, x=None, y=58, lado=184):
    """El toque del área en la banda oscura de la cabecera del planeador: trazo blanco, muy tenue."""
    import motivos
    from lib import W, M
    x = W - M - 470 if x is None else x
    svg = motivos.motivo(area, "#FFFFFF").replace(
        "<svg ", f'<svg x="{x}" y="{y}" width="{lado}" height="{lado}" opacity="0.28" ', 1)
    b.append(svg)
