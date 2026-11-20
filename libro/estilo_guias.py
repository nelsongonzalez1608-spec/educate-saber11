"""Estética de las guías de clase («clase viva») con el look de las diapositivas de conceptualización
(Nelson, 20 nov: «mismo look, sin internet»).

Las letras van incrustadas en el HTML (woff2 recortados a latín, libro/fuentes_web/, licencia OFL), así que la
guía se ve igual con doble clic y sin internet:
  · títulos en Shantell Sans (la letra de la bitácora del cuaderno);
  · rótulos, minutos y membretes en Space Mono;
  · tarjetas blancas con borde de tinta y sombra corrida del color del acento: el «3D» liviano;
  · papel claro, sin fondos sólidos detrás del texto y sin líneas horizontales de adorno.
Se aplica en clase_viva.pagina(): vale para las 56 guías.
"""
import base64
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
_FUENTES = [("Shantell Sans", "700", "shantell-sans-700"), ("Shantell Sans", "800", "shantell-sans-800"),
            ("Space Mono", "400", "space-mono-400"), ("Space Mono", "700", "space-mono-700")]


def _font_face():
    out = []
    for fam, w, f in _FUENTES:
        b64 = base64.b64encode(open(os.path.join(AQUI, "fuentes_web", f + ".woff2"), "rb").read()).decode()
        out.append(f'@font-face{{font-family:"{fam}";font-weight:{w};font-style:normal;font-display:block;'
                   f'src:url(data:font/woff2;base64,{b64}) format("woff2")}}')
    return "\n".join(out)


CSS = """
:root{--display:"Shantell Sans","Segoe UI",system-ui,sans-serif;--mono:"Space Mono",ui-monospace,Consolas,monospace;
  --ink:#1E2230;--bg:#FBF9F4;--sombra:6px 6px 0}
body{background:var(--bg)}
h1{font-weight:800;letter-spacing:-.005em}
h2{font-weight:800}
h3{font-weight:700}
.kicker{font-family:var(--mono);font-weight:700;letter-spacing:.12em;font-size:.78em;color:var(--muted)}
.tag,.min,.membrete{font-family:var(--mono);font-weight:700;letter-spacing:.04em;border-radius:8px}
.membrete{border:2px solid var(--ink);color:var(--ink);background:#fff}
#momnom,#tnum,.nbig,.relojxl{font-family:var(--display)}
/* tarjetas: borde de tinta y sombra corrida del acento */
.card{background:#fff;border:2.5px solid var(--ink);border-radius:18px;box-shadow:var(--sombra) var(--accent,var(--area))}
.card.edge{border-left:2.5px solid var(--ink)}
.card.big{box-shadow:8px 8px 0 var(--accent,var(--area))}
.step{background:#fff;border:2px solid var(--ink);border-left:2px solid var(--ink);box-shadow:4px 4px 0 var(--accent)}
.note{background:#fff;border:2px solid var(--ink);border-left:7px solid var(--accent,var(--area));box-shadow:4px 4px 0 rgba(30,34,48,.12)}
.cita{background:#fff;border:2.5px solid var(--ink);border-left:8px solid var(--area);box-shadow:var(--sombra) rgba(30,34,48,.10)}
.op{background:#fff;border:2px solid var(--ink);border-radius:14px}
.op .L{font-family:var(--mono);background:var(--bg);border:2px solid var(--ink)}
.op.ok{box-shadow:4px 4px 0 var(--verde)}
.icfes .texto{background:#fff;border:2px solid var(--ink)}
.sello{background:#FFFBEF;border:2.5px dashed var(--oro)}
.aviso{background:#fff;border:2px solid var(--ink);border-left:7px solid var(--area)}
.aviso.sev-aten{background:#fff;border-left-color:var(--verde)}
.aviso.sev-medi{background:#fff;border-left-color:var(--oro)}
.btn{border:2px solid var(--ink);border-radius:10px;font-weight:700;box-shadow:3px 3px 0 rgba(30,34,48,.15)}
.btn:hover{transform:translate(-1px,-1px);box-shadow:4px 4px 0 rgba(30,34,48,.2)}
.btn:active{transform:translate(2px,2px);box-shadow:1px 1px 0 rgba(30,34,48,.2)}
.tally .n{font-family:var(--mono)}
.keychip{border:2px solid var(--ink)}
.herr{background:#fff;border:2px solid var(--ink);border-left:7px solid var(--area);box-shadow:4px 4px 0 rgba(30,34,48,.10)}
.examen{background:#fff;border:2.5px solid var(--ink);border-left:10px solid var(--area);box-shadow:8px 8px 0 rgba(30,34,48,.10)}
.cv-voc div,.cv-det{border:2.5px solid var(--ink)}
.cv-voc div{border-top:7px solid var(--acc,var(--area))}
.cv-det{border-left:8px solid var(--acc)}
.gbox{border:2px solid var(--ink)}
.gbox h4{font-family:var(--mono);letter-spacing:.1em}
"""


def estilo():
    """Bloque <style> para pegar al final de los estilos de la página."""
    return _font_face() + CSS
