// VERIFICADOR DE LAS GUÍAS DE CLASE («clase viva»), para cualquier área.
//
//   node verifica_guias.js <carpeta con las .html> [carpeta para capturas]
//
// Recorre cada guía diapositiva por diapositiva (tecla →) a 1600 × 900 y comprueba:
//   · cero errores de JavaScript;
//   · ninguna clave visible antes de revelarla: .clave, .aviso y la pista ocultos, ninguna
//     opción ICFES marcada (.op.ok) al llegar a la diapositiva;
//   · nada se sale de ancho (la página no tiene scroll horizontal y ningún elemento de la
//     diapositiva pasa el borde derecho del escenario);
//   · al presionar «Revelar la clave», queda marcada exactamente la opción de data-k, y al
//     presionar «Revelar las claves» aparecen las del bloque;
//   · la tecla G abre la guía del profe y trae «Si … no es tu fuerte» donde hay apoyo.
// Si se da la carpeta de capturas, guarda la portada, un bloque y una ICFES de cada guía.
const { chromium } = require("playwright");
const fs = require("fs"), path = require("path");

(async () => {
  const dir = process.argv[2], shots = process.argv[3];
  if (!dir) { console.log("uso: node verifica_guias.js <carpeta> [capturas]"); process.exit(2); }
  if (shots) fs.mkdirSync(shots, { recursive: true });
  const files = fs.readdirSync(dir).filter(f => f.endsWith(".html")).sort();
  const browser = await chromium.launch();
  let fallas = 0;
  for (const f of files) {
    const page = await browser.newPage({ viewport: { width: 1600, height: 900 } });
    const errs = [];
    page.on("pageerror", e => errs.push(String(e)));
    page.on("console", m => { if (m.type() === "error" && !/fonts\.g/.test(m.text())) errs.push(m.text()); });
    await page.goto("file://" + path.resolve(dir, f));
    const n = await page.evaluate(() => +document.getElementById("count").textContent.split("/")[1]);
    const prob = [];
    let shotBloque = false, shotIcfes = false;
    for (let i = 0; i < n; i++) {
      const r = await page.evaluate(() => {
        const w = document.getElementById("wrap"), st = document.getElementById("stage");
        const vis = el => !el.hidden && el.offsetParent !== null;
        const out = {};
        out.claveVisible = [...w.querySelectorAll(".clave,.aviso,.note[id^=pista]")].filter(vis).length;
        out.opOk = w.querySelectorAll(".op.ok").length;
        out.hscroll = document.documentElement.scrollWidth > document.documentElement.clientWidth;
        const lim = st.getBoundingClientRect().right + 1;
        out.desborde = [...w.querySelectorAll("*")].filter(e => e.getBoundingClientRect().right > lim)
          .map(e => e.tagName + "." + e.className).slice(0, 3);
        out.esBloque = !!w.querySelector("[data-showgrupo]");
        out.esIcfes = !!w.querySelector("[data-clave]");
        out.portada = !!w.querySelector(".logo-xl");
        return out;
      });
      const d = i + 1;
      if (r.claveVisible) prob.push(`diap. ${d}: ${r.claveVisible} clave(s) o pista(s) visibles antes de revelar`);
      if (r.opOk) prob.push(`diap. ${d}: opción ICFES marcada antes de revelar`);
      if (r.hscroll) prob.push(`diap. ${d}: la página tiene scroll horizontal`);
      if (r.desborde.length) prob.push(`diap. ${d}: se sale de ancho: ${r.desborde.join(", ")}`);
      if (shots) await page.waitForTimeout(400);   // la diapositiva entra con una animación de 0,28 s
      if (shots && r.portada && i === 0) await page.screenshot({ path: path.join(shots, f.replace(".html", "_01.png")) });
      if (r.esIcfes) {
        const k = await page.evaluate(() => {
          const b = document.querySelector("#wrap [data-clave]"); b.click();
          const box = document.getElementById(b.dataset.clave);
          const ok = [...box.querySelectorAll(".op.ok")].map(o => o.dataset.op);
          return { esperada: b.dataset.k, marcadas: ok };
        });
        if (k.marcadas.length !== 1 || k.marcadas[0] !== k.esperada)
          prob.push(`diap. ${d}: al revelar se marca [${k.marcadas}] y la clave es ${k.esperada}`);
        if (shots && !shotIcfes) { await page.screenshot({ path: path.join(shots, f.replace(".html", `_${d}_icfes.png`)) }); shotIcfes = true; }
        await page.evaluate(() => document.querySelector("#wrap [data-clave]").click());
      }
      if (r.esBloque) {
        const k = await page.evaluate(() => {
          const b = document.querySelector("#wrap [data-showgrupo]"); b.click();
          const g = [...document.querySelectorAll(`#wrap [data-grupo="${b.dataset.showgrupo}"].clave`)];
          return g.filter(x => !x.hidden).map(x => x.textContent.trim()[0]);
        });
        if (k.length !== 2 || k.some(x => !/[A-D]/.test(x))) prob.push(`diap. ${d}: el bloque revela [${k}]`);
        if (shots && !shotBloque) { await page.screenshot({ path: path.join(shots, f.replace(".html", `_${d}_bloque.png`)) }); shotBloque = true; }
        await page.evaluate(() => document.querySelector("#wrap [data-showgrupo]").click());
      }
      if (i === 0) {
        await page.keyboard.press("g");
        const g = await page.evaluate(() => ({ abierta: document.getElementById("guia").classList.contains("open"),
                                               txt: document.getElementById("guiabody").textContent }));
        if (!g.abierta) prob.push("la tecla G no abre la guía del profe");
        if (!/no es tu fuerte/.test(g.txt)) prob.push("la portada no trae «… no es tu fuerte»");
        await page.keyboard.press("Escape");
      }
      await page.keyboard.press("ArrowRight");
    }
    if (errs.length) prob.push("errores de JavaScript: " + errs.join(" | "));
    fallas += prob.length;
    console.log(`${f.padEnd(32)} ${String(n).padStart(2)} diapositivas · ${prob.length ? prob.length + " problemas" : "bien"}`);
    prob.forEach(p => console.log("   · " + p));
    await page.close();
  }
  await browser.close();
  console.log(fallas ? `\n${fallas} problemas.` : "\nTodo en orden.");
  process.exit(fallas ? 1 : 0);
})();
