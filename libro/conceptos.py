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


def _guia(obj, decir, apoyo):
    return dict(obj=obj, decir=list(decir), como="", apoyo=list(apoyo))


def esc_vocabulario(A, mis, D, colores):
    tarjetas = "".join(
        f'<div style="--acc:{colores[k % len(colores)]}"><b>{E(p)}</b><span>{E(d)}</span></div>'
        for k, (p, d) in enumerate(D["vocab"]))
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m1)">Conceptualización · {MIN} min</span>'
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
    h = (f'<div class="eyebrow"><span class="min" style="--accent:var(--m1)">Conceptualización · {MIN} min</span>'
         f'<span class="kicker">El mapa de la misión · toca una tarjeta para abrirla</span></div>'
         f'<h2>{E(D["titulo"])}</h2>'
         f'<div class="cv-mapa" id="{g}">{lineas}{"".join(nodos)}</div>{"".join(dets)}')
    return dict(m=0, min=MIN, html=h, guia=_guia(
        "Ponerle nombre a lo que el grupo acaba de descubrir en la activación: una idea central y una "
        "por estrategia.",
        D["decir"], D["apoyo"]))


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
