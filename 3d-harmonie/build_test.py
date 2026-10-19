import base64, os
D = 'site'
def uri(f):
    mime = 'image/png' if f.endswith('.png') else 'image/jpeg'
    return f"data:{mime};base64," + base64.b64encode(open(os.path.join(D, f), 'rb').read()).decode()
tex = {k: uri(f) for k, f in [('pine','pine.jpg'),('pineNor','pineNor.jpg'),('pineRough','pineRough.jpg'),('slat','slat.jpg'),('slatNor','slatNor.jpg'),('envRgb','envRgb.png'),('envM','envM.png')]}
weo = {k: {'d': uri(k + '_d.jpg'), 'n': uri(k + '_n.jpg')} for k in ['teak','cedar','ipe','darkgrey']}
import json
engine = open(os.path.join(D, 'harmonie.js'), encoding='utf-8').read().replace('</script', '<\\/script')
html = '''<title>Harmonie en 3D</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500;600&family=Instrument+Serif:ital@1&display=swap" rel="stylesheet">
<style>
:root{--bg:#f4f6f3;--card:#fff;--ink:#0b1a12;--ink2:#4c5a52;--line:#dfe5df;--green:#2d6a4f;--green2:#52b788;--dark:#0b1a12;color-scheme:light}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg);color:var(--ink);font-family:"Instrument Sans",system-ui,-apple-system,"Segoe UI",sans-serif}
.top{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;flex-wrap:wrap;padding:20px 24px 14px;max-width:1360px;margin:0 auto}
.top h1{margin:0;font-size:clamp(26px,3vw,36px);font-weight:600;letter-spacing:-.02em}
.top h1 em{font-family:"Instrument Serif",Georgia,serif;font-weight:400;color:var(--green)}
.top p{margin:4px 0 0;color:var(--ink2);font-size:15px;max-width:640px}
.tag{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border-radius:999px;background:#fff7e6;color:#7a5200;font-size:13px;font-weight:600;border:1px solid #f0dcae}
.wrap{max-width:1360px;margin:0 auto;padding:0 24px 28px;display:grid;grid-template-columns:minmax(0,1fr) 300px;gap:18px}
.stage{position:relative;border-radius:24px;overflow:hidden;background:#fff;box-shadow:0 30px 80px -50px rgba(14,42,31,.45);min-height:560px;height:calc(100svh - 150px);max-height:820px}
.stage canvas{position:absolute;inset:0;width:100%;height:100%;display:block;cursor:grab;touch-action:pan-y}
.ld{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;background:#fff;color:var(--ink2);font-size:14px;z-index:2;transition:opacity .6s}
.ld i{display:block;width:180px;height:2px;background:var(--line);position:relative;overflow:hidden}.ld i b{position:absolute;left:0;top:0;height:100%;width:0;background:var(--green);transition:width .3s}
.ld.done{opacity:0;pointer-events:none}
.tools{position:absolute;left:50%;bottom:16px;transform:translateX(-50%);z-index:3;display:flex;gap:4px;padding:5px;border-radius:999px;background:rgba(255,255,255,.95);box-shadow:inset 0 0 0 1px var(--line),0 10px 30px -12px rgba(14,42,31,.3);max-width:calc(100% - 24px);overflow-x:auto}
.tools button,.views button{border:0;background:none;font:inherit;font-size:14px;color:var(--ink);padding:9px 14px;border-radius:999px;cursor:pointer;white-space:nowrap}
.tools button[aria-pressed=true]{background:var(--dark);color:#fff}
.views{position:absolute;left:16px;top:16px;z-index:3;display:flex;gap:4px;flex-wrap:wrap;padding:4px;border-radius:999px;background:rgba(255,255,255,.92);box-shadow:inset 0 0 0 1px var(--line)}
.views button{font-size:13px;padding:7px 12px}.views button:hover,.tools button:hover{background:#eef2ee}.tools button[aria-pressed=true]:hover{background:var(--dark)}
.panel{display:flex;flex-direction:column;gap:14px}
.box{background:var(--card);border-radius:20px;padding:18px;box-shadow:inset 0 0 0 1px var(--line)}
.box h2{margin:0 0 4px;font-size:12px;letter-spacing:.16em;text-transform:uppercase;color:var(--green);font-weight:600}
.box p{margin:0 0 12px;color:var(--ink2);font-size:13px}
.opt{display:flex;align-items:center;justify-content:space-between;gap:10px;width:100%;padding:11px 0;border:0;border-top:1px solid var(--line);background:none;font:inherit;font-size:15px;color:var(--ink);cursor:pointer;text-align:left}
.opt:first-of-type{border-top:0}
.opt small{display:block;color:var(--ink2);font-size:12px}
.sw{width:42px;height:24px;border-radius:999px;background:#d5dcd6;position:relative;flex:none;transition:background .25s}
.sw::after{content:"";position:absolute;left:3px;top:3px;width:18px;height:18px;border-radius:50%;background:#fff;box-shadow:0 1px 3px rgba(0,0,0,.2);transition:transform .25s}
.opt[aria-checked=true] .sw{background:var(--green)}.opt[aria-checked=true] .sw::after{transform:translateX(18px)}
.clads{display:flex;gap:8px;flex-wrap:wrap}
.clads button{width:38px;height:38px;border-radius:50%;border:0;padding:0;cursor:pointer;background-size:cover;background-position:center;box-shadow:inset 0 0 0 1px rgba(0,0,0,.12)}
.clads button[aria-pressed=true]{box-shadow:0 0 0 2px #fff,0 0 0 4px var(--green)}
.cname{margin-top:10px;font-size:14px;font-weight:600}
.note{font-size:13px;color:var(--ink2);line-height:1.5}
button:focus-visible{outline:2px solid var(--green);outline-offset:2px}
@media (max-width:900px){.wrap{grid-template-columns:minmax(0,1fr)}.stage{height:62svh;min-height:420px}.views{right:16px}}
@media (max-width:640px){.top{padding:16px 16px 10px}.wrap{padding:0 16px 20px}.tools button{padding:9px 11px;font-size:13px}.views button{padding:6px 10px;font-size:12px}}
</style>
<header class="top"><div><h1>Harmonie <em>en 3D</em></h1><p>3 m de façade, hotte inox centrée, façades anthracite. Faites tourner la cuisine, ouvrez portes et tiroirs, allumez ou éteignez les équipements.</p></div><span class="tag">Version d’essai · à valider</span></header>
<main class="wrap">
  <section class="stage" aria-label="Vue 3D d’Harmonie">
    <div class="ld" id="ld"><span>Chargement de la vue 3D</span><i><b id="bar"></b></i></div>
    <canvas id="c" aria-label="Cuisine Harmonie en 3D : faites glisser pour la faire pivoter"></canvas>
    <div class="views" role="group" aria-label="Points de vue">
      <button type="button" data-v="trois">3/4</button><button type="button" data-v="face">Face</button><button type="button" data-v="cote">Côté</button><button type="button" data-v="detail">Cuisson</button><button type="button" data-v="evier">Évier</button><button type="button" data-v="frigo">Froid</button>
    </div>
    <div class="tools" role="toolbar" aria-label="Animer la cuisine">
      <button type="button" data-t="auto" aria-pressed="true">Rotation</button><button type="button" data-t="doors" aria-pressed="false">Portes</button><button type="button" data-t="drawers" aria-pressed="false">Tiroirs</button><button type="button" data-t="lid" aria-pressed="false">Couvercles</button><button type="button" data-t="blind" aria-pressed="false">Fermer</button>
    </div>
  </section>
  <aside class="panel">
    <div class="box"><h2>Équipements</h2><p>Allumez ou éteignez chaque élément.</p>
      <button type="button" class="opt" data-o="plancha" aria-checked="true" role="switch"><span>Plancha<small>Planet Oasi 55, au centre</small></span><i class="sw"></i></button>
      <button type="button" class="opt" data-o="friteuse" aria-checked="true" role="switch"><span>Friteuse<small>À gauche de la plancha</small></span><i class="sw"></i></button>
      <button type="button" class="opt" data-o="gaz" aria-checked="true" role="switch"><span>Plaque gaz<small>À droite de la plancha</small></span><i class="sw"></i></button>
      <button type="button" class="opt" data-o="evier" aria-checked="true" role="switch"><span>Évier<small>À droite</small></span><i class="sw"></i></button>
      <button type="button" class="opt" data-o="frigo" aria-checked="true" role="switch"><span>Réfrigérateur<small>Porte de gauche</small></span><i class="sw"></i></button>
    </div>
    <div class="box"><h2>Côtés et arrière</h2><div class="clads" id="clads"></div><div class="cname" id="cname">Teak</div></div>
    <div class="box note">À venir dans les prochaines versions : barbecue Napoléon, cave à vin, robinet Quooker, enceintes, plan Dekton, store banne et îlot sur roulettes.</div>
  </aside>
</main>
<script>window.__TEX = %%TEX%%; window.__WEO = %%WEO%%;</script>
<script>%%ENGINE%%</script>
<script>
(function () {
  var NAMES = { fundermax: "Fundermax anthracite", teak: "Teak", cedar: "Cedar", ipe: "Ipé", darkgrey: "Dark grey" };
  var SW = { fundermax: "background:#33353a", teak: "", cedar: "", ipe: "", darkgrey: "" };
  var clads = document.getElementById("clads"), cname = document.getElementById("cname");
  ["fundermax", "teak", "cedar", "ipe", "darkgrey"].forEach(function (k) {
    var b = document.createElement("button"); b.type = "button"; b.dataset.c = k; b.setAttribute("aria-label", NAMES[k]); b.title = NAMES[k];
    b.setAttribute("aria-pressed", String(k === "teak"));
    b.style.cssText = k === "fundermax" ? SW.fundermax : "background-image:url(" + window.__WEO[k].d + ")";
    clads.appendChild(b);
  });
  var canvas = document.getElementById("c"), ld = document.getElementById("ld"), bar = document.getElementById("bar");
  var api;
  try { api = window.DMG3D.mount(canvas, Object.assign({}, window.__TEX, { weo: window.__WEO })); }
  catch (e) { ld.querySelector("span").textContent = "La vue 3D n’a pas pu démarrer sur cet appareil."; return; }
  var st = { auto: true, doors: false, drawers: false, lid: false, blind: false };
  api.onProgress = function (p) { bar.style.width = Math.round(p * 100) + "%"; };
  api.onReady = function () { ld.classList.add("done"); };
  setTimeout(function () { ld.classList.add("done"); }, 7000);
  api.setCladding("teak");
  var sync = function () { document.querySelectorAll("[data-t]").forEach(function (b) { b.setAttribute("aria-pressed", String(!!st[b.dataset.t])); }); };
  api.onInteract = function () { if (st.auto) { st.auto = false; api.setAuto(false); sync(); } };
  document.querySelectorAll("[data-t]").forEach(function (b) {
    b.addEventListener("click", function () {
      var t = b.dataset.t; st[t] = !st[t];
      if (t === "auto") api.setAuto(st.auto);
      else { if (st.auto) { st.auto = false; api.setAuto(false); }
        if (t === "doors") api.setDoors(st.doors); if (t === "drawers") api.setDrawers(st.drawers); if (t === "lid") api.setLid(!st.lid); if (t === "blind") api.setBlind(st.blind); }
      sync();
    });
  });
  document.querySelectorAll("[data-v]").forEach(function (b) { b.addEventListener("click", function () { st.auto = false; api.setAuto(false); sync(); api.view(b.dataset.v); }); });
  document.querySelectorAll("[data-o]").forEach(function (b) {
    b.addEventListener("click", function () {
      var on = b.getAttribute("aria-checked") !== "true"; b.setAttribute("aria-checked", String(on)); api.setOption(b.dataset.o, on);
      if (on) { st.auto = false; api.setAuto(false); sync(); var v = { plancha: "detail", friteuse: "detail", gaz: "detail", evier: "evier", frigo: "frigo" }[b.dataset.o]; if (b.dataset.o === "frigo") { st.doors = true; api.setDoors(true); sync(); } api.view(v); }
    });
  });
  clads.addEventListener("click", function (e) {
    var b = e.target.closest("[data-c]"); if (!b) return;
    clads.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
    cname.textContent = (b.dataset.c === "fundermax" ? "" : "Lames WEO®35 · ") + NAMES[b.dataset.c];
    api.setCladding(b.dataset.c); st.auto = false; api.setAuto(false); sync(); api.view("trois");
  });
  cname.textContent = "Lames WEO®35 · Teak";
  window.__api = api;
})();
</script>
'''
html = html.replace('%%TEX%%', json.dumps(tex)).replace('%%WEO%%', json.dumps(weo)).replace('%%ENGINE%%', engine)
open('harmonie-essai.html', 'w', encoding='utf-8').write(html)
print(round(len(html) / 1e6, 2), 'Mo')
