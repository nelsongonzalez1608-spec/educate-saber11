#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el visor del cuaderno: un HTML para navegar área por área, misión por misión,
   hoja por hoja, con los hallazgos del libro y el cruce con la revisión externa.

   Es un extra: no reemplaza los PDF, que siguen siendo el entregable.
   Las imágenes van como archivos aparte en img/, no incrustadas.
"""
import csv, json, os
import revision_externa as RX

TAB = "/home/claude/tablero/"
VIS = "/home/claude/visor/"


def leer(n):
    with open(TAB + n, encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


MAN = json.load(open(VIS + "manifiesto.json"))
HALL = leer("hallazgos.csv")
ICFES = leer("icfes.csv")
PEND = leer("pendientes.csv")
AVA = leer("avance.csv")

INSTR = []
try:
    from extrae_instrumentos import filas
    INSTR = [list(f) for f in filas()]
except Exception:
    pass

DATOS = {
    "areas": MAN["areas"],
    "hojas": MAN["hojas"],
    "hallazgos": HALL,
    "icfes": ICFES,
    "pendientes": PEND,
    "avance": AVA,
    "instrumentos": INSTR,
    "revisores": [{"area": a, "grado": g, "docente": d, "fecha": f,
                   "paginas": p, "n": n} for a, g, d, f, p, n in RX.REVISORES],
    "externos": [{"area": f[0], "grado": f[1], "pag": f[2], "item": f[3],
                  "que": f[4], "tipo": f[5], "cruce": f[6]} for f in RX.FILAS],
    "tipos": RX.NOMBRE_TIPO,
    "cruce": [{"tipo": t, "nombre": RX.NOMBRE_TIPO[t], "mios": m,
               "revisores": sum(1 for f in RX.FILAS if f[5] == t), "lectura": lec}
              for t, (m, lec) in RX.CRUCE.items()],
    "solo": [{"titulo": a, "reg": b, "por": c} for a, b, c in RX.SOLO_NOSOTROS],
}

HTML = r"""<title>Visor del cuaderno</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<style>
:root{
  --bg:#F7F8FA; --panel:#FFFFFF; --fg:#1B1F27; --fg2:#5C6472; --fg3:#8A919E;
  --linea:#DFE4EB; --track:#E9EDF2; --sombra:0 1px 2px rgba(27,31,39,.05), 0 8px 24px -16px rgba(27,31,39,.18);
  --azul:#242478; --rojo:#A82424; --verde:#2E7A39; --oro:#B0711A; --morado:#5B3E96; --teal:#157F86;
  --azul-soft:#EEF0FA; --rojo-soft:#FBEEEE; --verde-soft:#EBF4EC; --oro-soft:#FBF3E6; --morado-soft:#F1EDF8;
  --sobre-azul:#FFFFFF;
  --serif:"Source Serif 4",Georgia,"Times New Roman",serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
}
@media (prefers-color-scheme:dark){ :root:not([data-theme="light"]){
  --bg:#13161C; --panel:#1B1F27; --fg:#E8EBF0; --fg2:#A6AEBC; --fg3:#7A818E;
  --linea:#2B313C; --track:#242A34; --sombra:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -18px rgba(0,0,0,.7);
  --azul:#A3B4EC; --rojo:#E89393; --verde:#86C993; --oro:#E3B566; --morado:#B9A6E4; --teal:#6FC8CE;
  --azul-soft:#1C2132; --rojo-soft:#2C1D1D; --verde-soft:#1A2820; --oro-soft:#2B2317; --morado-soft:#241E33;
  --sobre-azul:#13161C;
  color-scheme:dark;
}}
:root[data-theme="dark"]{
  --bg:#13161C; --panel:#1B1F27; --fg:#E8EBF0; --fg2:#A6AEBC; --fg3:#7A818E;
  --linea:#2B313C; --track:#242A34; --sombra:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -18px rgba(0,0,0,.7);
  --azul:#A3B4EC; --rojo:#E89393; --verde:#86C993; --oro:#E3B566; --morado:#B9A6E4; --teal:#6FC8CE;
  --azul-soft:#1C2132; --rojo-soft:#2C1D1D; --verde-soft:#1A2820; --oro-soft:#2B2317; --morado-soft:#241E33;
  --sobre-azul:#13161C;
  color-scheme:dark;
}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--fg);font-family:var(--sans);font-size:15px;line-height:1.6;
  -webkit-text-size-adjust:100%}
.wrap{max-width:1180px;margin:0 auto;padding-inline:16px;padding-block:0 64px}

/* ── cabecera y pestañas ───────────────────────────────────────── */
header.top{position:sticky;top:env(safe-area-inset-top,0px);z-index:40;background:var(--bg);
  padding-block:16px 0;margin-bottom:4px}
.marca{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline}
.marca b{font-size:11.5px;letter-spacing:.15em;text-transform:uppercase;color:var(--azul);font-weight:700}
.marca span{font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--fg3)}
h1{font-family:var(--serif);font-size:clamp(25px,5.2vw,36px);font-weight:600;line-height:1.14;
  margin:8px 0 3px;text-wrap:balance;letter-spacing:-.012em}
.lede{color:var(--fg2);font-size:14.5px;max-width:66ch;margin:0 0 16px}
nav.tabs{display:flex;gap:2px;overflow-x:auto;scrollbar-width:none;border-bottom:1px solid var(--linea);
  margin:0 -16px;padding:0 16px}
nav.tabs::-webkit-scrollbar{display:none}
nav.tabs button{appearance:none;background:none;border:0;border-bottom:2px solid transparent;
  color:var(--fg2);font:inherit;font-size:14px;font-weight:600;padding:9px 13px;cursor:pointer;
  white-space:nowrap;margin-bottom:-1px;border-radius:7px 7px 0 0}
nav.tabs button:hover{color:var(--fg);background:var(--panel)}
nav.tabs button[aria-selected="true"]{color:var(--azul);border-bottom-color:var(--azul)}
nav.tabs button .c{font-variant-numeric:tabular-nums;color:var(--fg3);font-weight:500;margin-left:5px;font-size:12.5px}

/* ── piezas comunes ────────────────────────────────────────────── */
h2{font-family:var(--serif);font-size:21px;font-weight:600;margin:34px 0 2px;letter-spacing:-.008em}
h2:first-child{margin-top:26px}
h3{font-size:14.5px;font-weight:700;margin:0}
.nota{color:var(--fg2);font-size:13.5px;margin:0 0 14px;max-width:76ch}
.cifras{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:11px;margin:18px 0}
.cifra{background:var(--panel);border:1px solid var(--linea);border-radius:13px;padding:15px 17px;min-width:0}
.cifra .v{font-family:var(--serif);font-size:33px;line-height:1.02;color:var(--azul);
  font-variant-numeric:tabular-nums;font-weight:600}
.cifra .v small{font-size:15px;color:var(--fg3);font-family:var(--sans);font-weight:400}
.cifra .l{font-size:12.5px;color:var(--fg2);margin-top:6px;line-height:1.42}

.barra{display:grid;grid-template-columns:minmax(118px,1.3fr) 3fr minmax(66px,auto);gap:12px;
  align-items:center;font-size:13.5px;padding:3px 0}
.barra .n{min-width:0;overflow-wrap:anywhere}
.track{height:9px;border-radius:6px;background:var(--track);overflow:hidden;min-width:0}
.track i{display:block;height:100%;border-radius:6px}
.barra .q{text-align:right;color:var(--fg3);font-variant-numeric:tabular-nums;font-size:12.5px}

.pill{display:inline-block;padding:2px 9px;border-radius:99px;font-size:11px;font-weight:700;
  white-space:nowrap;letter-spacing:.01em}
.p-alta{background:var(--rojo-soft);color:var(--rojo)}
.p-media{background:var(--oro-soft);color:var(--oro)}
.p-baja{background:var(--azul-soft);color:var(--azul)}
.p-at{background:var(--verde-soft);color:var(--verde)}
.p-ok{background:var(--verde-soft);color:var(--verde)}
.p-mor{background:var(--morado-soft);color:var(--morado)}

.tw{overflow-x:auto;border:1px solid var(--linea);border-radius:13px;background:var(--panel);margin-top:12px}
table{border-collapse:collapse;width:100%;font-size:13px;min-width:620px}
th{text-align:left;font-size:10.5px;letter-spacing:.07em;text-transform:uppercase;color:var(--fg2);
  font-weight:700;padding:10px 13px;background:var(--azul-soft);white-space:nowrap;position:sticky;top:0}
td{padding:10px 13px;border-top:1px solid var(--linea);vertical-align:top;line-height:1.5}
td.num{font-variant-numeric:tabular-nums;white-space:nowrap;color:var(--fg2)}
tr.s-alta td:first-child{box-shadow:inset 3px 0 0 var(--rojo)}
tr.s-media td:first-child{box-shadow:inset 3px 0 0 var(--oro)}
tr.s-baja td:first-child{box-shadow:inset 3px 0 0 var(--azul)}
tr.s-at td:first-child{box-shadow:inset 3px 0 0 var(--verde)}

.filtros{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 2px;align-items:center}
.filtros .et{font-size:11px;letter-spacing:.07em;text-transform:uppercase;color:var(--fg3);
  font-weight:700;margin-right:3px}
.chip{appearance:none;background:var(--panel);border:1px solid var(--linea);color:var(--fg2);
  font:inherit;font-size:12.5px;padding:4px 11px;border-radius:99px;cursor:pointer}
.chip:hover{color:var(--fg);border-color:var(--fg3)}
.chip[aria-pressed="true"]{background:var(--azul);border-color:var(--azul);
  color:var(--sobre-azul);font-weight:600}

/* ── áreas ─────────────────────────────────────────────────────── */
.areas{display:grid;grid-template-columns:repeat(auto-fit,minmax(265px,1fr));gap:13px;margin-top:18px}
.area{position:relative;text-align:left;background:var(--panel);border:1px solid var(--linea);
  border-radius:14px;padding:17px 19px 16px;cursor:pointer;font:inherit;color:inherit;
  box-shadow:var(--sombra);min-width:0;transition:transform .12s ease}
.area:hover{transform:translateY(-2px)}
.area[disabled]{cursor:default;opacity:.62;box-shadow:none}
.area[disabled]:hover{transform:none}
.area .acc{position:absolute;left:0;top:17px;bottom:17px;width:3px;border-radius:0 3px 3px 0}
.area .nom{font-family:var(--serif);font-size:20px;font-weight:600;line-height:1.2;padding-left:13px}
.area .rg{font-size:12.5px;color:var(--fg3);padding-left:13px;margin-top:2px;font-variant-numeric:tabular-nums}
.area .bar{margin-top:13px}
.area .pie{display:flex;justify-content:space-between;gap:10px;font-size:12.5px;color:var(--fg2);margin-top:9px}

.volver{appearance:none;background:none;border:0;color:var(--azul);font:inherit;font-size:13.5px;
  font-weight:600;padding:8px 0;cursor:pointer}
.volver:hover{text-decoration:underline}
.cab-area{display:flex;flex-wrap:wrap;gap:6px 16px;align-items:baseline;margin:6px 0 2px}
.cab-area h2{margin:0}

.mision{background:var(--panel);border:1px solid var(--linea);border-radius:14px;padding:16px 18px;
  margin-top:13px;box-shadow:var(--sombra)}
.mision > .enc{display:flex;flex-wrap:wrap;gap:4px 14px;align-items:baseline;margin-bottom:3px}
.mision .mn{font-family:var(--serif);font-size:17px;font-weight:600}
.mision .meta{font-size:12.5px;color:var(--fg2)}
.mision .estr{font-size:12.5px;color:var(--fg2);margin:7px 0 0;line-height:1.5}
.mision .estr b{color:var(--fg);font-weight:600}
.hojas{display:grid;grid-template-columns:repeat(auto-fill,minmax(104px,1fr));gap:10px;margin-top:13px}
.hoja{appearance:none;background:none;border:0;padding:0;cursor:pointer;font:inherit;color:inherit;
  text-align:center;min-width:0}
.hoja img{display:block;width:100%;max-width:100%;aspect-ratio:2000/2588;object-fit:cover;object-position:top;
  border:1px solid var(--linea);border-radius:7px;background:var(--panel)}
.hoja:hover img{border-color:var(--azul)}
.hoja .et{font-size:11px;color:var(--fg2);margin-top:5px;line-height:1.3}
.hoja .et b{font-variant-numeric:tabular-nums;color:var(--fg)}
.vacia{border:1px dashed var(--linea);border-radius:14px;padding:19px;margin-top:13px;
  color:var(--fg2);font-size:13.5px;background:none}

/* ── lupa ──────────────────────────────────────────────────────── */
.lupa{position:fixed;inset:0;z-index:90;background:rgba(9,11,15,.96);display:flex;
  flex-direction:column;padding:env(safe-area-inset-top,0px) 0 env(safe-area-inset-bottom,0px)}
.lupa .bar{display:flex;gap:8px;align-items:center;padding:10px 14px;color:#EDEFF4;font-size:13px;
  flex-wrap:wrap;background:#0B0E13;border-bottom:1px solid rgba(255,255,255,.1)}
.lupa .bar .tt{flex:1;min-width:0;overflow-wrap:anywhere;font-weight:600}
.lupa .bar .pg{font-variant-numeric:tabular-nums;color:#AEB6C4}
.lupa .bar button{appearance:none;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.18);
  color:#EDEFF4;font:inherit;font-size:13px;font-weight:600;border-radius:8px;padding:5px 12px;cursor:pointer}
.lupa .bar button:hover{background:rgba(255,255,255,.2)}
.lupa .vis{flex:1;min-height:0;overflow:auto;display:flex;align-items:flex-start;justify-content:center;
  padding:0 14px 14px}
.lupa .vis img{max-width:100%;height:auto;border-radius:5px;background:#fff;box-shadow:0 18px 50px rgba(0,0,0,.5)}
body.quieto{overflow:hidden}

.aviso{border:1px solid var(--linea);border-left:3px solid var(--azul);border-radius:11px;
  padding:14px 17px;margin-top:16px;background:var(--panel);font-size:13.5px;max-width:88ch}
.aviso b{color:var(--azul)}
.aviso.rojo{border-left-color:var(--rojo)} .aviso.rojo b{color:var(--rojo)}
.fichas{display:grid;grid-template-columns:repeat(auto-fit,minmax(285px,1fr));gap:11px;margin-top:13px}
.ficha{background:var(--panel);border:1px solid var(--linea);border-left:3px solid var(--morado);
  border-radius:11px;padding:14px 16px;min-width:0}
.ficha .t{font-size:14px;font-weight:700;line-height:1.35}
.ficha .r{font-size:11.5px;color:var(--morado);font-weight:700;margin-top:3px;letter-spacing:.02em}
.ficha .d{font-size:12.5px;color:var(--fg2);margin-top:7px;line-height:1.5}
.cruz{background:var(--panel);border:1px solid var(--linea);border-radius:13px;padding:15px 18px;margin-top:11px}
.cruz .enc{display:flex;flex-wrap:wrap;gap:4px 12px;align-items:baseline}
.cruz .ti{font-size:11px;letter-spacing:.08em;font-weight:700;color:var(--morado);text-transform:uppercase}
.cruz .nb{font-size:14.5px;font-weight:700;flex:1;min-width:0}
.cruz .cu{font-size:12.5px;color:var(--fg2);font-variant-numeric:tabular-nums;white-space:nowrap}
.cruz .cu b{font-family:var(--serif);font-size:17px;font-weight:600}
.cruz .le{font-size:13px;color:var(--fg2);margin-top:8px;line-height:1.56;max-width:92ch}
footer{color:var(--fg3);font-size:12.5px;margin-top:44px;padding-top:16px;border-top:1px solid var(--linea)}
@media (max-width:560px){
  .barra{grid-template-columns:1fr auto}
  .barra .track{grid-column:1/-1}
  .hojas{grid-template-columns:repeat(auto-fill,minmax(88px,1fr))}
}
</style>

<div class="wrap">
<header class="top">
  <div class="marca"><b>EDUCATE · Para el Saber</b><span>Cuaderno Saber 11</span></div>
  <h1 id="h1">Visor del cuaderno</h1>
  <p class="lede" id="lede">Las hojas construidas, área por área y misión por misión, con lo que encontramos
  en el libro fuente y lo que encontraron los seis docentes que lo revisaron.</p>
  <nav class="tabs" id="tabs"></nav>
</header>
<main id="main"></main>
<footer>Los PDF siguen siendo el entregable para imprenta; este visor es para revisar y mostrar.
Las imágenes son las hojas reales renderizadas, no maquetas.</footer>
</div>
<div id="lupa" hidden></div>

<script id="datos" type="application/json">__DATOS__</script>
<script>
(function(){
  var D = JSON.parse(document.getElementById('datos').textContent);
  var INC = window.__IMG__ || null;   // archivo suelto: las hojas vienen incrustadas
  function fuente(sv){ return INC ? INC[sv] : ('img/' + sv + '.jpg'); }
  var main = document.getElementById('main'), tabsEl = document.getElementById('tabs');
  var HOJA = {}; D.hojas.forEach(function(h){ HOJA[h.svg] = h; });

  function el(t, cls, txt){ var e=document.createElement(t); if(cls) e.className=cls;
    if(txt!=null) e.textContent=txt; return e; }
  function N(x){ var v=Number(String(x==null?'':x).replace(/[^0-9.-]/g,'')); return isFinite(v)?v:0; }

  var listas = D.avance.reduce(function(s,r){ return s+N(r.listas); },0);
  var total  = D.avance.reduce(function(s,r){ return s+N(r.total); },0);

  /* ───── pestañas ───── */
  var TABS = [
    {id:'areas',  et:'Las seis áreas', c:listas},
    {id:'hall',   et:'Hallazgos del libro', c:D.hallazgos.length},
    {id:'ext',    et:'Revisión externa', c:D.externos.length},
    {id:'cruce',  et:'El cruce', c:null},
    {id:'icfes',  et:'Banco ICFES', c:D.icfes.length},
    {id:'inst',   et:'Instrumentos', c:D.instrumentos.length}
  ];
  var vista = 'areas', areaAbierta = null;

  TABS.forEach(function(t){
    var b = el('button', null, t.et);
    b.type='button'; b.setAttribute('aria-selected', t.id===vista);
    if(t.c!=null){ var s=el('span','c',String(t.c)); b.appendChild(s); }
    b.addEventListener('click', function(){ areaAbierta=null; ir(t.id); });
    b.dataset.id = t.id; tabsEl.appendChild(b);
  });
  function marcarTabs(){
    [].forEach.call(tabsEl.children, function(b){
      b.setAttribute('aria-selected', b.dataset.id===vista);
    });
  }

  function ir(id){ vista=id; marcarTabs(); pinta(); window.scrollTo({top:0,behavior:'smooth'}); }

  /* ───── cifras y barras ───── */
  function cifra(v, suf, l){
    var d=el('div','cifra'), a=el('div','v');
    a.textContent=String(v); if(suf){ var s=el('small',null,suf); a.appendChild(s); }
    d.appendChild(a); d.appendChild(el('div','l',l)); return d;
  }
  function barra(nom, l, t, color, suf){
    var f=el('div','barra');
    f.appendChild(el('div','n',nom));
    var tr=el('div','track'), i=el('i');
    var pc = t>0 ? Math.round(l/t*100) : 0;
    i.style.width = pc+'%'; i.style.background = pc>=100 ? 'var(--verde)' : (color||'var(--azul)');
    tr.appendChild(i); f.appendChild(tr);
    f.appendChild(el('div','q', l+' / '+t+(suf?' '+suf:'')));
    return f;
  }

  /* ───── vista: las seis áreas ───── */
  function vistaAreas(){
    var f = document.createDocumentFragment();
    var c = el('div','cifras');
    c.appendChild(cifra(listas, ' / '+total, 'páginas construidas · son 270 páginas, 135 hojas a doble cara'));
    var compl = D.areas.reduce(function(s,a){
      return s + a.misiones.filter(function(m){ return m.estado==='listo'; }).length; },0);
    c.appendChild(cifra(compl, ' / 36', 'misiones completas en las seis áreas'));
    c.appendChild(cifra(D.icfes.filter(function(r){return r.estado==='Usada';}).length, null,
      'preguntas Saber 11 montadas, todas verificadas'));
    c.appendChild(cifra(D.hallazgos.length + D.externos.length, null,
      'hallazgos registrados: ' + D.hallazgos.length + ' nuestros y ' + D.externos.length + ' de los revisores'));
    f.appendChild(c);

    var h=el('h2',null,'Entra por el área'); f.appendChild(h);
    f.appendChild(el('p','nota','Cada área son 43 páginas: una portada y seis misiones de siete páginas. '
      + 'Dentro de cada misión, cinco hojas de taller con las diez preguntas del libro y dos de '
      + 'entrenamiento con cuatro preguntas tipo Saber 11. Las misiones listas se abren hoja por hoja.'));

    var g = el('div','areas');
    D.areas.forEach(function(a){
      var listasA = a.misiones.reduce(function(s,m){ return s + m.hojas.length; },0)
                  + (D.hojas.some(function(h){ return h.area===a.clave && h.mision===null; }) ? 1 : 0);
      var totalA = 43;  // una portada y seis misiones de siete páginas
      var b = el('button','area'); b.type='button';
      var ac = el('div','acc'); ac.style.background = a.color; b.appendChild(ac);
      b.appendChild(el('div','nom', a.nombre));
      b.appendChild(el('div','rg', 'páginas ' + a.rango));
      var bar = el('div','bar'); bar.appendChild(barra('', listasA, totalA, a.color, 'pág.'));
      bar.querySelector('.barra').style.gridTemplateColumns = '1fr minmax(66px,auto)';
      bar.querySelector('.barra .n').remove();
      b.appendChild(bar);
      var pie = el('div','pie');
      var hechas = a.misiones.filter(function(m){ return m.estado==='listo'; }).length;
      pie.appendChild(el('span', null, hechas + ' de 6 misiones'));
      pie.appendChild(el('span', null, listasA ? 'Abrir →' : 'Sin empezar'));
      b.appendChild(pie);
      if(!listasA){ b.disabled = true; }
      else b.addEventListener('click', function(){ areaAbierta = a.clave; ir('areas'); });
      g.appendChild(b);
    });
    f.appendChild(g);

    f.appendChild(el('h2',null,'Avance por sección'));
    var bs = el('div');
    D.avance.forEach(function(r){
      var col = (D.areas.filter(function(a){ return a.nombre===r.seccion; })[0]||{}).color;
      bs.appendChild(barra(r.seccion, N(r.listas), N(r.total), col, 'pág.'));
    });
    f.appendChild(bs);
    return f;
  }

  /* ───── vista: un área por dentro ───── */
  function vistaArea(clave){
    var a = D.areas.filter(function(x){ return x.clave===clave; })[0];
    var f = document.createDocumentFragment();
    var v = el('button','volver','← Las seis áreas'); v.type='button';
    v.addEventListener('click', function(){ areaAbierta=null; ir('areas'); });
    f.appendChild(v);

    var cab = el('div','cab-area');
    var h = el('h2',null,a.nombre); h.style.color = a.color; cab.appendChild(h);
    cab.appendChild(el('span','nota','páginas ' + a.rango + ' · ' + a.misiones.filter(function(m){
      return m.estado==='listo'; }).length + ' de 6 misiones'));
    f.appendChild(cab);

    var todas = D.hojas.filter(function(h){ return h.area===clave; });
    var port = D.hojas.filter(function(h){ return h.area===clave && h.mision===null; })[0];
    if(port){
      var pm = el('div','mision');
      pm.style.borderLeft = '3px solid ' + a.color;
      var pe = el('div','enc');
      pe.appendChild(el('span','mn','Portada del área'));
      pe.appendChild(el('span','meta','página ' + port.pagina));
      pm.appendChild(pe);
      var ph = el('div','hojas'); ph.appendChild(miniatura(port, todas));
      ph.style.gridTemplateColumns = 'repeat(auto-fill,minmax(104px,1fr))';
      pm.appendChild(ph); f.appendChild(pm);
    }

    a.misiones.forEach(function(m){
      if(m.estado!=='listo'){
        var vz = el('div','vacia');
        vz.appendChild(el('b', null, 'Misión ' + m.n));
        vz.appendChild(document.createTextNode(' · todavía no construida. Siete páginas: '
          + 'cinco de taller con las diez preguntas del libro y dos de entrenamiento con cuatro preguntas tipo Saber 11.'));
        f.appendChild(vz); return;
      }
      var d = el('div','mision');
      d.style.borderLeft = '3px solid ' + a.color;
      var enc = el('div','enc');
      enc.appendChild(el('span','mn','Misión ' + m.n));
      enc.appendChild(el('span','meta','páginas ' + m.paginas));
      if(m.componente) enc.appendChild(el('span','meta','· ' + m.componente));
      if(m.icfes){ var p=el('span','pill p-ok','ICFES ' + m.icfes); enc.appendChild(p); }
      d.appendChild(enc);
      if(m.estrategias){
        var es = el('p','estr');
        es.appendChild(el('b',null,'Las cuatro estrategias: '));
        es.appendChild(document.createTextNode(m.estrategias));
        d.appendChild(es);
      }
      var g = el('div','hojas');
      m.hojas.forEach(function(sv){ g.appendChild(miniatura(HOJA[sv], todas)); });
      d.appendChild(g);
      f.appendChild(d);
    });
    return f;
  }

  function miniatura(h, grupo){
    var b = el('button','hoja'); b.type='button';
    var im = el('img'); im.src = fuente(h.svg); im.loading='lazy';
    im.alt = h.titulo + ', página ' + h.pagina;
    b.appendChild(im);
    var et = el('div','et');
    et.appendChild(el('b', null, 'pág. ' + h.pagina));
    et.appendChild(document.createElement('br'));
    et.appendChild(document.createTextNode(h.rol === 'Entrenamiento ICFES' ? 'ICFES' : h.rol));
    b.appendChild(et);
    b.addEventListener('click', function(){ abrir(h, grupo); });
    return b;
  }

  /* ───── lupa ───── */
  var lupaEl = document.getElementById('lupa'), lupaGrupo = [], lupaI = 0;
  function abrir(h, grupo){
    lupaGrupo = grupo.slice().sort(function(a,b){ return a.pagina-b.pagina; });
    lupaI = Math.max(0, lupaGrupo.map(function(x){return x.svg;}).indexOf(h.svg));
    lupaEl.hidden = false; document.body.classList.add('quieto'); pintaLupa();
  }
  function cerrar(){ lupaEl.hidden = true; document.body.classList.remove('quieto'); lupaEl.textContent=''; }
  function mover(d){ lupaI = (lupaI + d + lupaGrupo.length) % lupaGrupo.length; pintaLupa(); }
  function pintaLupa(){
    var h = lupaGrupo[lupaI];
    lupaEl.textContent='';
    var box = el('div','lupa');
    var bar = el('div','bar');
    var tt = el('div','tt', h.titulo); bar.appendChild(tt);
    bar.appendChild(el('div','pg','página ' + h.pagina + ' · ' + (lupaI+1) + ' de ' + lupaGrupo.length));
    var ba = el('button',null,'← Anterior'); ba.type='button';
    ba.addEventListener('click', function(){ mover(-1); });
    var bs = el('button',null,'Siguiente →'); bs.type='button';
    bs.addEventListener('click', function(){ mover(1); });
    var bc = el('button',null,'Cerrar'); bc.type='button';
    bc.addEventListener('click', cerrar);
    bar.appendChild(ba); bar.appendChild(bs); bar.appendChild(bc);
    box.appendChild(bar);
    var vis = el('div','vis');
    var im = el('img'); im.src = fuente(h.svg); im.alt = h.titulo;
    vis.appendChild(im); box.appendChild(vis);
    box.addEventListener('click', function(e){ if(e.target===box||e.target===vis) cerrar(); });
    lupaEl.appendChild(box);
  }
  document.addEventListener('keydown', function(e){
    if(lupaEl.hidden) return;
    if(e.key==='Escape') cerrar();
    else if(e.key==='ArrowLeft') mover(-1);
    else if(e.key==='ArrowRight') mover(1);
  });

  /* ───── tabla genérica con filtros ───── */
  function tabla(cols, filas, opts){
    opts = opts||{};
    var tw = el('div','tw'), t = el('table');
    var th = el('thead'), tr = el('tr');
    cols.forEach(function(c){ tr.appendChild(el('th',null,c.et)); });
    th.appendChild(tr); t.appendChild(th);
    var tb = el('tbody');
    filas.forEach(function(r){
      var f = el('tr');
      if(opts.sev){ var s=String(r[opts.sev]||'').toLowerCase();
        f.className = 's-' + (s.indexOf('alta')>=0?'alta':s.indexOf('media')>=0?'media':
                              s.indexOf('atenc')>=0?'at':'baja'); }
      cols.forEach(function(c){
        var td = el('td');
        if(c.pill){ td.appendChild(pill(r[c.k], c.pill)); }
        else { td.textContent = r[c.k]==null?'':String(r[c.k]); if(c.num) td.className='num'; }
        f.appendChild(td);
      });
      tb.appendChild(f);
    });
    t.appendChild(tb); tw.appendChild(t);
    if(!filas.length){ tw.textContent=''; var p=el('p','nota','Nada con ese filtro.');
      p.style.padding='14px'; tw.appendChild(p); }
    return tw;
  }
  function pill(v, modo){
    var s = String(v||''), c='p-baja';
    if(modo==='sev') c = /Alta/i.test(s)?'p-alta' : /Media/i.test(s)?'p-media' :
                          /Atenci/i.test(s)?'p-at' : 'p-baja';
    else if(modo==='estado') c = /Completa|Usada|Corregido/i.test(s)?'p-ok' :
      /Reportado|Registrado|Consultado|curso/i.test(s)?'p-media' : 'p-baja';
    else if(modo==='tipo') c='p-mor';
    var e = el('span','pill '+c, s); return e;
  }
  function filtros(et, valores, actual, cb){
    var d = el('div','filtros');
    d.appendChild(el('span','et', et));
    valores.forEach(function(v){
      var b = el('button','chip', v.et); b.type='button';
      b.setAttribute('aria-pressed', v.id===actual);
      b.addEventListener('click', function(){ cb(v.id); });
      d.appendChild(b);
    });
    return d;
  }

  /* ───── vista: hallazgos del libro ───── */
  var fSev = 'todas';
  function vistaHall(){
    var f = document.createDocumentFragment();
    f.appendChild(el('h2',null,'Lo que encontramos nosotros'));
    f.appendChild(el('p','nota','Salió de resolver una por una las preguntas ya montadas. Todo queda anotado, '
      + 'incluso lo que no es un error de fondo: eso va marcado como «Atención». Los que dicen «Nuestro» son '
      + 'defectos de nuestras propias hojas, ya corregidos y verificados.'));
    var cuenta = {};
    D.hallazgos.forEach(function(r){ var s=r.severidad||'—'; cuenta[s]=(cuenta[s]||0)+1; });
    var vals = [{id:'todas', et:'Todas ('+D.hallazgos.length+')'}];
    ['Alta','Media','Baja','Atención'].forEach(function(s){
      if(cuenta[s]) vals.push({id:s, et:s+' ('+cuenta[s]+')'}); });
    f.appendChild(filtros('Severidad', vals, fSev, function(v){ fSev=v; pinta(); }));
    var filas = D.hallazgos.filter(function(r){ return fSev==='todas' || r.severidad===fSev; });
    f.appendChild(tabla([
      {k:'n', et:'N.º', num:true}, {k:'ubicacion', et:'Dónde'},
      {k:'que_pasa', et:'Qué pasa'}, {k:'efecto', et:'Efecto'},
      {k:'severidad', et:'Severidad', pill:'sev'}, {k:'estado', et:'Estado', pill:'estado'}
    ], filas, {sev:'severidad'}));
    var av = el('div','aviso');
    av.appendChild(el('b',null,'El cuaderno no los esconde. '));
    av.appendChild(document.createTextNode('En los casos de fondo el instrumento hace que el estudiante '
      + 'cuente o calcule por su cuenta y le deja un renglón para escribir qué no le cuadró.'));
    f.appendChild(av);

    f.appendChild(el('h2',null,'Pendientes de nuestro lado'));
    f.appendChild(el('p','nota','No son problemas del libro: son tareas abiertas del proyecto.'));
    f.appendChild(tabla([
      {k:'n', et:'N.º', num:true}, {k:'que_falta', et:'Qué falta'},
      {k:'por_que_importa', et:'Por qué importa'}, {k:'quien', et:'Quién lo destraba'},
      {k:'estado', et:'Estado', pill:'estado'}
    ], D.pendientes));
    return f;
  }

  /* ───── vista: revisión externa ───── */
  var fArea='todas', fTipo='todos';
  function vistaExt(){
    var f = document.createDocumentFragment();
    f.appendChild(el('h2',null,'Los seis docentes que revisaron el libro'));
    f.appendChild(el('p','nota','Seis matrices recibidas. Las páginas son las del libro que cada uno revisó, '
      + 'no las del cuaderno: por eso no coinciden con nuestra numeración.'));
    f.appendChild(tabla([
      {k:'area', et:'Área'}, {k:'grado', et:'Grado', num:true},
      {k:'docente', et:'Docente a cargo'}, {k:'fecha', et:'Fecha'},
      {k:'paginas', et:'Páginas'}, {k:'n', et:'Hallazgos', num:true}
    ], D.revisores));

    f.appendChild(el('h2',null,'Los 120 hallazgos, uno por uno'));
    f.appendChild(el('p','nota','«Tipo» usa la misma taxonomía que nuestro registro, para poder cruzar. '
      + '«Cruce» dice si ya lo teníamos anotado o si es nuevo.'));

    var ca = {}; D.externos.forEach(function(r){ ca[r.area]=(ca[r.area]||0)+1; });
    var va = [{id:'todas', et:'Todas ('+D.externos.length+')'}];
    Object.keys(ca).forEach(function(k){ va.push({id:k, et:k+' ('+ca[k]+')'}); });
    f.appendChild(filtros('Área', va, fArea, function(v){ fArea=v; pinta(); }));

    var ct = {}; D.externos.forEach(function(r){ ct[r.tipo]=(ct[r.tipo]||0)+1; });
    var vt = [{id:'todos', et:'Todos'}];
    Object.keys(ct).sort(function(a,b){ return ct[b]-ct[a]; }).forEach(function(k){
      vt.push({id:k, et:k.charAt(0)+k.slice(1).toLowerCase()+' ('+ct[k]+')'}); });
    f.appendChild(filtros('Tipo', vt, fTipo, function(v){ fTipo=v; pinta(); }));

    var filas = D.externos.filter(function(r){
      return (fArea==='todas'||r.area===fArea) && (fTipo==='todos'||r.tipo===fTipo); });
    if(fTipo!=='todos'){
      var ex = el('p','nota'); ex.style.marginTop='10px';
      ex.appendChild(el('b',null, fTipo + ' · '));
      ex.appendChild(document.createTextNode(D.tipos[fTipo]||''));
      f.appendChild(ex);
    }
    f.appendChild(tabla([
      {k:'area', et:'Área'}, {k:'grado', et:'Gr.', num:true},
      {k:'pag', et:'Pág.', num:true}, {k:'item', et:'Ítem', num:true},
      {k:'que', et:'Qué reporta el docente'},
      {k:'tipo', et:'Tipo', pill:'tipo'}, {k:'cruce', et:'Cruce con nuestro registro'}
    ], filas));
    return f;
  }

  /* ───── vista: el cruce ───── */
  function vistaCruce(){
    var f = document.createDocumentFragment();
    var mios = D.cruce.reduce(function(s,c){ return s+c.mios.length; },0);
    var coinc = D.externos.filter(function(r){ return r.cruce.indexOf('Reg.')===0
      || r.cruce.indexOf('Coincide')===0 || r.cruce.indexOf('Es nuestra')===0; }).length;
    var c = el('div','cifras');
    c.appendChild(cifra(D.hallazgos.length, null, 'registros nuestros'));
    c.appendChild(cifra(D.externos.length, null, 'hallazgos de los seis docentes'));
    c.appendChild(cifra(coinc, null, 'de ellos ya estaban en nuestro registro'));
    c.appendChild(cifra(D.externos.length - coinc, null, 'aporte nuevo de los revisores'));
    f.appendChild(c);

    f.appendChild(el('h2',null,'Tipo por tipo'));
    f.appendChild(el('p','nota','Donde «nuestros» va en cero, el hallazgo es aporte limpio de los docentes. '
      + 'Donde los dos lados coinciden sin habernos hablado, el defecto es del libro, no de quien lo leyó.'));
    D.cruce.slice().sort(function(a,b){
      return (b.mios.length+b.revisores) - (a.mios.length+a.revisores); }).forEach(function(x){
      var d = el('div','cruz');
      var enc = el('div','enc');
      enc.appendChild(el('span','ti', x.tipo));
      enc.appendChild(el('span','nb', x.nombre));
      var cu = el('div','cu');
      cu.appendChild(el('b', null, String(x.mios.length)));
      cu.appendChild(document.createTextNode(' nuestros · '));
      cu.appendChild(el('b', null, String(x.revisores)));
      cu.appendChild(document.createTextNode(' de los revisores'));
      enc.appendChild(cu);
      d.appendChild(enc);
      if(x.mios.length){
        var r = el('div','le'); r.style.marginTop='5px'; r.style.color='var(--fg3)';
        r.textContent = 'Nuestros registros n.º ' + x.mios.join(', ');
        d.appendChild(r);
      }
      d.appendChild(el('div','le', x.lectura));
      f.appendChild(d);
    });

    f.appendChild(el('h2',null,'Lo que vimos nosotros y nadie más mencionó'));
    f.appendChild(el('p','nota','No es un mérito: es la lista de riesgos que nadie más está vigilando.'));
    var g = el('div','fichas');
    D.solo.forEach(function(s){
      var d = el('div','ficha');
      d.appendChild(el('div','t', s.titulo));
      d.appendChild(el('div','r', s.reg));
      d.appendChild(el('div','d', s.por));
      g.appendChild(d);
    });
    f.appendChild(g);
    return f;
  }

  /* ───── banco ICFES e instrumentos ───── */
  function vistaIcfes(){
    var f = document.createDocumentFragment();
    f.appendChild(el('h2',null,'Banco de preguntas ICFES'));
    f.appendChild(el('p','nota','El membrete es siempre «Pregunta Saber 11», sin año ni «oficial» (regla 7, 10 nov). '
      + 'La procedencia verificada de cada pregunta queda en la columna fuente.'));
    f.appendChild(tabla([
      {k:'membrete', et:'Membrete'}, {k:'contexto', et:'Contexto'},
      {k:'mision', et:'Misión'}, {k:'clave', et:'Clave'}, {k:'estado', et:'Estado', pill:'estado'}
    ], D.icfes));
    return f;
  }
  function vistaInst(){
    var f = document.createDocumentFragment();
    f.appendChild(el('h2',null,'Instrumentos de pensamiento'));
    f.appendChild(el('p','nota','Uno por pregunta. Esta lista existe para comprobar la regla: si dos '
      + 'instrumentos se parecen, está mal hecho. Hoy no hay ningún título repetido.'));
    var cols = ['Área','Misión','Pregunta','Estrategia','Instrumento','Contexto'];
    var filas = D.instrumentos.map(function(r){
      var o = {}; cols.forEach(function(c,i){ o['c'+i] = r[i]; }); return o; });
    f.appendChild(tabla(cols.map(function(c,i){ return {k:'c'+i, et:c, num:(i===1||i===2)}; }), filas));
    return f;
  }

  /* ───── pintar ───── */
  function pinta(){
    main.textContent='';
    if(vista==='areas') main.appendChild(areaAbierta ? vistaArea(areaAbierta) : vistaAreas());
    else if(vista==='hall') main.appendChild(vistaHall());
    else if(vista==='ext')  main.appendChild(vistaExt());
    else if(vista==='cruce')main.appendChild(vistaCruce());
    else if(vista==='icfes')main.appendChild(vistaIcfes());
    else if(vista==='inst') main.appendChild(vistaInst());
  }
  pinta();
})();
</script>
"""

if __name__ == "__main__":
    os.makedirs(VIS, exist_ok=True)
    html = HTML.replace("__DATOS__", json.dumps(DATOS, ensure_ascii=False))
    open(VIS + "index.html", "w", encoding="utf-8").write(html)
    print(f"visor escrito: {VIS}index.html · {len(html)/1024:.0f} KB")
    print("  hojas:", len(DATOS["hojas"]), "· hallazgos:", len(DATOS["hallazgos"]),
          "· externos:", len(DATOS["externos"]), "· instrumentos:", len(DATOS["instrumentos"]))
