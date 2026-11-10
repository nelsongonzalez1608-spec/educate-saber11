// VERIFICADOR DE LAS GUÍAS DE CLASE («clase viva»), para cualquier área.
//
//   node verifica_guias.js <carpeta con las .html> [carpeta para capturas]
//
// Recorre cada guía diapositiva por diapositiva (tecla →) a 1600 × 900 y comprueba:
//   · cero errores de JavaScript;
//   · ninguna clave visible antes de revelarla (lo que se pinta, no solo el atributo hidden):
//     .clave, .aviso y la pista ocultos, ninguna
//     opción ICFES marcada (.op.ok) al llegar a la diapositiva;
//   · nada se sale de ancho (la página no tiene scroll horizontal y ningún elemento de la
//     diapositiva pasa el borde derecho del escenario);
//   · al presionar «Revelar la clave», queda marcada exactamente la opción de data-k, y al
//     presionar «Revelar las claves» aparecen las del bloque;
//   · la tecla G abre la guía del profe y trae «Si … no es tu fuerte» donde hay apoyo.
//   · clases 7 y 8 (simulacro de EDUCATE y socialización, decisión de Nelson del 10 nov): ninguna
//     pregunta ni clave proyectada (ni opciones .op, ni botón «Revelar la clave», ni .keychip);
//     la clase 7 trae el cronómetro grande de la prueba, que arranca, corre y NO se reinicia al
//     cambiar de diapositiva; la clase 8 trae las casillas donde el profe escribe las más falladas
//     y lo escrito reaparece en las diapositivas siguientes.
// Si se da la carpeta de capturas, guarda la portada, un bloque y una ICFES de cada guía, y todas
// las diapositivas de las clases 7 y 8.
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
    const sim = /Clase[78]_/.test(f), c7 = /Clase7_/.test(f), c8 = /Clase8_/.test(f);
    let vioReloj = false, vioCampos = false;
    for (let i = 0; i < n; i++) {
      const r = await page.evaluate(() => {
        const w = document.getElementById("wrap"), st = document.getElementById("stage");
        // visible = lo que de verdad se pinta: el atributo hidden no basta si el CSS le da display
        const vis = el => el.offsetParent !== null && getComputedStyle(el).visibility !== "hidden";
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
      if (sim) {
        const x = await page.evaluate(() => {
          const w = document.getElementById("wrap");
          return { proyecta: w.querySelectorAll(".op,[data-clave],.keychip,.enun").length,
                   reloj: !!w.querySelector("[data-examen]"), campos: w.querySelectorAll("[data-campo]").length };
        });
        if (x.proyecta) prob.push(`diap. ${d}: la clase ${c7 ? 7 : 8} proyecta preguntas o claves (${x.proyecta} elementos)`);
        if (x.reloj && c7 && !vioReloj) {
          vioReloj = true;
          const t0 = await page.evaluate(() => document.querySelector("#wrap [data-exnum]").textContent);
          await page.click('#wrap [data-ex="play"]');
          await page.waitForTimeout(2300);
          const t1 = await page.evaluate(() => document.querySelector("#wrap [data-exnum]").textContent);
          await page.keyboard.press("ArrowRight"); await page.waitForTimeout(1200);
          await page.keyboard.press("ArrowLeft");
          const t2 = await page.evaluate(() => document.querySelector("#wrap [data-exnum]").textContent);
          const seg = t => { const m = t.replace("+", "").split(":"); return +m[0] * 60 + +m[1]; };
          if (!(seg(t1) < seg(t0))) prob.push(`diap. ${d}: el cronómetro de la prueba no corre (${t0} → ${t1})`);
          if (!(seg(t2) < seg(t1))) prob.push(`diap. ${d}: el cronómetro de la prueba se reinició al cambiar de diapositiva (${t1} → ${t2})`);
          await page.click('#wrap [data-ex="play"]');      // en pausa para las capturas
        }
        if (x.campos && c8 && !vioCampos) {
          vioCampos = true;
          await page.fill('#wrap [data-campo="asig1"]', "17");
          await page.keyboard.press("Escape");
          await page.evaluate(() => document.activeElement.blur());
          await page.keyboard.press("ArrowRight");
          const eco = await page.evaluate(() => [...document.querySelectorAll('#wrap [data-eco="asig1"]')].map(e => e.textContent));
          await page.keyboard.press("ArrowLeft");
          const val = await page.evaluate(() => document.querySelector('#wrap [data-campo="asig1"]').value);
          if (!eco.length || eco.some(t => t !== "17")) prob.push(`diap. ${d + 1}: lo escrito en la asignada 1 no reaparece (${eco})`);
          if (val !== "17") prob.push(`diap. ${d}: la casilla no conserva lo escrito al volver (${val})`);
        }
        if (shots) { await page.waitForTimeout(400); await page.screenshot({ path: path.join(shots, f.replace(".html", `_${String(d).padStart(2, "0")}.png`)) }); }
      }
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
          return g.filter(x => x.offsetParent !== null).map(x => x.textContent.trim()[0]);
        });
        if (k.length !== 2 || k.some(x => !/[A-H]/.test(x))) prob.push(`diap. ${d}: el bloque revela [${k}]`);
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
    if (c7 && !vioReloj) prob.push("la clase 7 no trae el cronómetro de la prueba");
    if (c8 && !vioCampos) prob.push("la clase 8 no trae las casillas de las preguntas más falladas");
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
