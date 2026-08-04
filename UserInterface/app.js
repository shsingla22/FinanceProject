/* Business Quality Analyst — client app.
   All analysis is precomputed by the BusinessAnalysis skill (build_data.py);
   this file only parses natural-language intent and renders explainable views. */

"use strict";

const state = { fw: null, data: null, names: [], dynamic: false, ai: false,
                ready: false, pendingQ: null };

const MODULE_TOPICS = {
  CAP: ["capital allocation", "capex", "buyback", "dividend", "acquisition", "m&a", "working capital", "wc"],
  ROC: ["return on capital", "roce", "roic", "croci", "returns", "margin", "margins", "profitability", "asset turn"],
  GRW: ["growth", "sales growth", "revenue growth", "persistence", "expansion"],
  MGT: ["management", "promoter", "ceo", "cfo", "chairman", "md", "leadership"],
  IND: ["industry", "competition", "oligopoly", "monopoly", "barriers", "pricing war"],
  CUS: ["customer", "brand", "intangible", "assurance", "convenience"],
  MOAT: ["moat", "competitive advantage", "network effect", "distribution", "technology"],
};
const PARAM_TOPICS = {
  "CAP.working_capital_cost": ["working capital", "cash conversion", "ccc", "debtor days", "inventory days", "payable"],
  "ROC.profit_margin": ["margin", "margins", "opm", "gross margin", "profitability"],
  "ROC.headline": ["return on capital", "roce", "roic", "croci"],
  "ROC.asset_turn": ["asset turn", "asset light", "asset intensity"],
  "GRW.persistence": ["growth consistency", "consistent growth", "persistence"],
};

init();

function setStatus(html) {
  let el = document.getElementById("bootStatus");
  if (!el) {
    el = document.createElement("p");
    el.id = "bootStatus";
    el.className = "note";
    const sub = document.querySelector(".app-header .sub");
    (sub || document.body).insertAdjacentElement("afterend", el);
  }
  el.innerHTML = html;
}

async function init() {
  // 1. Wire up ALL interaction FIRST, so a click during warm-up is never
  //    silently lost (the original cause of "analyse DIXON does nothing").
  document.getElementById("askForm").addEventListener("submit", e => {
    e.preventDefault();
    const q = document.getElementById("q").value.trim();
    if (q) safeHandle(q);
  });
  document.getElementById("chips").addEventListener("click", e => {
    const b = e.target.closest(".chip");
    if (b) { document.getElementById("q").value = b.dataset.q; safeHandle(b.dataset.q); }
  });
  document.getElementById("out").addEventListener("click", e => {
    const l = e.target.closest("[data-co]");
    if (l) safeHandle("analyse " + l.dataset.co);
  });
  // Never fail silently again: surface any uncaught error as a card.
  window.addEventListener("error", e => showError(e.message));
  window.addEventListener("unhandledrejection", e =>
    showError(e.reason && e.reason.message ? e.reason.message : String(e.reason)));

  // 2. This app is dynamic-only: the FastAPI server must be running.
  let h = null;
  try {
    h = await fetch("api/health").then(r => r.ok ? r.json() : null);
  } catch (_) { /* handled below */ }
  if (!h || h.mode !== "dynamic") {
    setStatus("❌ Backend not reachable. Start it with: " +
      "<code>cd UserInterface && uvicorn server:app --host 0.0.0.0 --port 8000</code> then reload.");
    return;
  }
  state.dynamic = true;
  state.ai = !!h.ai_qualitative;

  // 3. Load framework (fast) then companies (can take ~30-60s on a cold
  //    server while it computes 742 companies).
  setStatus("⏳ Warming up — the server is computing all 742 companies live (first load can take ~30–60s)…");
  try {
    state.fw = await fetch("api/framework").then(r => r.json());
    state.data = await fetch("api/companies").then(r => r.json());
  } catch (e) {
    setStatus(`❌ Failed to load data: ${esc(e.message)}. Is the server still running? Try reloading.`);
    return;
  }
  state.names = Object.entries(state.data.companies).map(([sym, c]) => ({
    sym, name: c.name || sym,
    hay: (sym + " " + (c.name || "")).toUpperCase(),
  }));
  state.ready = true;
  setStatus("⚡ <strong>Live analysis</strong> — quantitative signals recomputed per request" +
    (state.ai
      ? "; qualitative analysis runs automatically on <strong>" + esc(h.analysis_model || "opus") +
        "</strong> via " + (h.ai_backend === "claude_code_cli" ? "your Claude subscription" : "the Claude API") +
        " — multi-pass over the whole concall timeline, so the FIRST analysis of a company can take several minutes; cached afterwards."
      : ". ⚠️ Qualitative analysis is OFF — log in the Claude Code CLI (run <code>claude</code> once) or set ANTHROPIC_API_KEY, then restart the server."));

  // 4. If the user asked something while we were warming up, run it now.
  if (state.pendingQ) { const q = state.pendingQ; state.pendingQ = null; safeHandle(q); }
}

function showError(msg) {
  const out = document.getElementById("out");
  if (out) out.insertAdjacentHTML("beforeend",
    `<div class="card"><h2>Something went wrong</h2><p class="note">${esc(msg)}</p></div>`);
}

function safeHandle(q) {
  if (!state.ready) {
    state.pendingQ = q;
    const out = document.getElementById("out");
    out.insertAdjacentHTML("beforeend",
      `<div class="card"><p>⏳ Got it — <strong>“${esc(q)}”</strong> will run as soon as the
       server finishes warming up (computing 742 companies live)…</p></div>`);
    return;
  }
  Promise.resolve(handle(q)).catch(e => showError(e.message || String(e)));
}

/* ---------------- natural-language intent parsing ---------------- */

function findCompanies(q) {
  const up = q.toUpperCase();
  const hits = [];
  // exact symbol tokens first
  const tokens = up.split(/[^A-Z0-9&\-]+/).filter(t => t.length >= 2);
  for (const n of state.names) {
    if (tokens.includes(n.sym)) { hits.push({ ...n, w: 100 }); continue; }
    // name word-prefix match: SUM the lengths of all matching tokens so
    // "asian paints" (ASIAN+PAINTS = 11) outranks "Berger Paints" (PAINTS = 6)
    const words = n.name.toUpperCase().split(/\s+/);
    let w = 0;
    for (const t of tokens) {
      if (t.length >= 4 && words.some(wd => wd.startsWith(t))) w += t.length;
    }
    if (w > 0) hits.push({ ...n, w });
  }
  hits.sort((a, b) => b.w - a.w);
  const seen = new Set(); const out = [];
  for (const h of hits) if (!seen.has(h.sym)) { seen.add(h.sym); out.push(h); }
  return out;
}

function detectModule(q) {
  const low = q.toLowerCase();
  for (const [pid, keys] of Object.entries(PARAM_TOPICS))
    for (const k of keys)
      if (low.includes(k)) return { param: pid, module: pid.split(".")[0], phrase: k };
  for (const [m, keys] of Object.entries(MODULE_TOPICS))
    for (const k of keys)
      if (low.includes(k)) return { module: m, phrase: k };
  return null;
}

function handle(q) {
  const low = q.toLowerCase();
  const out = document.getElementById("out");
  out.innerHTML = "";
  echo(q);

  if (/\b(help|how (do|to)|what can)\b/.test(low)) return renderHelp();
  if (/\b(framework|methodology|method|parameters?)\b/.test(low) && /\b(explain|what|describe|show)\b/.test(low))
    return renderFramework();

  const topic = detectModule(q);
  // Strip the topic phrase before company matching, so words inside it
  // ("capital", "growth"…) can't fuzzy-match company names.
  const qForCos = topic
    ? q.replace(new RegExp(topic.phrase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "i"), " ")
    : q;
  const cos = findCompanies(qForCos);
  const compareMode = /\b(compare|vs\.?|versus)\b/.test(low) && cos.length >= 2;
  const rankMode = /\b(best|top|rank|select|pick|screen|good businesses|worst|bottom)\b/.test(low) && !compareMode && cos.length === 0;

  if (compareMode) return renderCompare(cos[0].sym, cos[1].sym);
  if (rankMode) {
    const nMatch = low.match(/\b(top|best|worst|bottom)\s*(\d{1,3})?/);
    const n = nMatch && nMatch[2] ? Math.min(50, +nMatch[2]) : 10;
    const asc = /\b(worst|bottom)\b/.test(low);
    // optional industry filter
    const inds = [...new Set(Object.values(state.data.companies).map(c => c.industry).filter(Boolean))];
    const ind = inds.find(i => low.includes(i.toLowerCase()));
    return renderRanking(n, topic ? topic.module : null, ind || null, asc);
  }
  if (cos.length >= 1 && topic) return renderTopic(cos[0].sym, topic);
  if (cos.length >= 1) return renderCompany(cos[0].sym);
  if (topic) return renderFramework(topic.module);

  card(`<h2>Didn't catch that</h2>
    <p>I couldn't find a company or intent in “${esc(q)}”. Try “analyse DIXON”,
    “best 10 companies”, “compare TITAN and DMART”, or “working capital of IXIGO”.</p>`);
}

/* ---------------- rendering ---------------- */

const $out = () => document.getElementById("out");

/* ---- proxy-proof long work: start a server job, poll with short GETs ----
   One long fetch dies at intermediary proxies (GitHub Codespaces port
   forwarding kills requests after ~100s -> "Analysis failed" even though
   the server was still working). Every request here returns in
   milliseconds, so NOTHING can time out no matter how long the analysis
   takes; transient poll failures are retried, never fatal. */
const fmtElapsed = s => s < 60 ? `${Math.round(s)}s`
  : `${Math.floor(s / 60)}m ${String(Math.round(s % 60)).padStart(2, "0")}s`;

async function pollJob(kind, id, onTick) {
  let misses = 0;
  for (;;) {
    await new Promise(r => setTimeout(r, 3500));
    let j = null;
    try {
      const r = await fetch(`api/jobs/${kind}/${id}`);
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      j = await r.json();
      misses = 0;
    } catch (e) {
      if (++misses >= 8) throw new Error("lost contact with the server — " +
        "check it is still running, then re-ask (finished work is cached): " + (e.message || e));
      continue;               // transient blip (proxy hiccup, laptop sleep) — keep polling
    }
    if (j.state === "done") return j.result;
    if (j.state === "error") throw new Error(j.error || "failed on the server");
    if (onTick) onTick(j.elapsed || 0);
  }
}

async function jobFetch(kind, sym, onTick) {
  const r = await fetch(`api/jobs/${kind}/${sym}`, { method: "POST" });
  if (!r.ok) {
    let d = ""; try { d = (await r.json()).detail || ""; } catch (_) { /* keep status */ }
    throw new Error(d || `HTTP ${r.status}`);
  }
  return pollJob(kind, sym, onTick);
}
function echo(q) { $out().insertAdjacentHTML("beforeend", `<div class="you">You asked: “${esc(q)}”</div>`); }
function card(html) { $out().insertAdjacentHTML("beforeend", `<div class="card">${html}</div>`); attachSparkHover(); }
function cardIn(el, html) { el.insertAdjacentHTML("beforeend", `<div class="card">${html}</div>`); attachSparkHover(); }
function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }
const fmtScore = s => s == null ? "n/a" : (s > 0 ? "+" : "") + (Math.round(s * 100) / 100);
const scoreCls = s => s == null ? "mid" : s > 0.25 ? "pos" : s < -0.25 ? "neg" : "mid";
// Intuitive labels: users read words, the -2..+2 number stays as fine print.
const PARAM_WORD = { "2": "Excellent", "1": "Good", "0": "Neutral", "-1": "Weak", "-2": "Poor" };
const paramWord = s => PARAM_WORD[String(Math.round(s))] || "n/a";
function verdictWord(s) {
  if (s == null) return "Not assessed";
  if (s >= 1.25) return "Excellent business";
  if (s >= 0.5) return "Good business";
  if (s >= -0.25) return "Mixed / average";
  if (s >= -1.25) return "Weak business";
  return "Poor business";
}
const scoreDots = s => {                       // ●●●●○ five-level meter
  const lvl = Math.round(s) + 3;               // -2..+2 -> 1..5
  return "●".repeat(lvl) + "○".repeat(5 - lvl);
};
const fmtCr = v => v == null ? "—" : v >= 1e5 ? (v / 1e5).toFixed(1) + " L Cr" : Math.round(v).toLocaleString("en-IN") + " Cr";
const modName = id => state.fw.modules.find(m => m.id === id)?.name || id;

function divergingBar(score) {
  if (score == null) return `<div class="barwrap"><div class="axis"></div></div>`;
  const pct = Math.min(50, Math.abs(score) / 2 * 50);
  const seg = Math.abs(score) < 0.05
    ? `<div class="bar zero"></div>`
    : `<div class="bar ${score > 0 ? "pos" : "neg"}" style="width:${pct}%"></div>`;
  return `<div class="barwrap"><div class="axis"></div>${seg}</div>`;
}

function moduleBars(co) {
  let rows = "";
  for (const m of state.fw.modules) {
    const md = co.modules[m.id];
    rows += `<div class="lbl">${m.name} <small>(${md.assessed}/${md.total})</small></div>
             ${divergingBar(md.score)}
             <div class="val">${md.score == null ? "n/a" : fmtScore(md.score)}</div>`;
  }
  return `<div class="bars">${rows}</div>`;
}

function sparkline(title, values, unit) {
  const pts = (values || []).filter(v => v != null);
  if (pts.length < 3) return "";
  const vals = values.map(v => v == null ? null : +v);
  const min = Math.min(...pts), max = Math.max(...pts);
  const range = (max - min) || 1;
  const W = 240, H = 52, P = 4;
  const n = vals.length;
  const x = i => P + i * (W - 2 * P) / (n - 1);
  const y = v => H - P - (v - min) / range * (H - 2 * P);
  let d = "", started = false;
  vals.forEach((v, i) => {
    if (v == null) { started = false; return; }
    d += (started ? "L" : "M") + x(i).toFixed(1) + " " + y(v).toFixed(1) + " ";
    started = true;
  });
  const last = pts[pts.length - 1];
  const dataAttr = esc(JSON.stringify(vals));
  return `<div class="spark" data-vals='${dataAttr}' data-unit="${esc(unit)}">
    <div class="t">${esc(title)}</div>
    <div class="cur">${fmtNum(last)}${esc(unit)}</div>
    <svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" role="img" aria-label="${esc(title)} trend">
      <path d="${d.trim()}" fill="none" stroke="var(--series-1)" stroke-width="2"
            stroke-linecap="round" stroke-linejoin="round"/>
      <circle class="hover-dot" r="3.5" fill="var(--series-1)" style="display:none"/>
    </svg>
    <div class="tip"></div>
  </div>`;
}
const fmtNum = v => Math.abs(v) >= 1000 ? Math.round(v).toLocaleString("en-IN") : (Math.round(v * 10) / 10);

function attachSparkHover() {
  document.querySelectorAll(".spark:not([data-hover])").forEach(sp => {
    sp.dataset.hover = "1";
    const vals = JSON.parse(sp.dataset.vals);
    const unit = sp.dataset.unit || "";
    const svg = sp.querySelector("svg"), tip = sp.querySelector(".tip"), dot = sp.querySelector(".hover-dot");
    const pts = vals.filter(v => v != null);
    const min = Math.min(...pts), max = Math.max(...pts), range = (max - min) || 1;
    const W = 240, H = 52, P = 4, n = vals.length;
    svg.addEventListener("mousemove", e => {
      const r = svg.getBoundingClientRect();
      const i = Math.max(0, Math.min(n - 1, Math.round((e.clientX - r.left) / r.width * (n - 1))));
      const v = vals[i];
      if (v == null) { tip.style.display = "none"; dot.style.display = "none"; return; }
      const cx = P + i * (W - 2 * P) / (n - 1), cy = H - P - (v - min) / range * (H - 2 * P);
      dot.setAttribute("cx", cx); dot.setAttribute("cy", cy); dot.style.display = "";
      tip.textContent = `yr ${i + 1}/${n}: ${fmtNum(v)}${unit}`;
      tip.style.left = (cx / W * r.width) + "px";
      tip.style.top = (cy / H * r.height) + "px";
      tip.style.display = "block";
    });
    svg.addEventListener("mouseleave", () => { tip.style.display = "none"; dot.style.display = "none"; });
  });
}

function paramRow(p, got) {
  const srcTag = (got.source === "ai_concall" || got.source === "calls")
               ? `<span class="tag">🎙 from the concalls</span>`
               : got.source === "fused" ? `<span class="tag">◐ numbers + concalls</span>`
               : `<span class="tag">🔢 from the numbers</span>`;
  return `<div class="prow">
    <div class="pscore ${scoreCls(got.score)}" title="score ${fmtScore(got.score)} on a -2..+2 scale">
      ${paramWord(got.score)}<span class="dots">${scoreDots(got.score)}</span></div>
    <div class="pbody"><div class="pn">${esc(p.name)} ${srcTag}</div>
    <div class="pr">${esc(got.rationale)}${got.quote ? ` — <em>“${esc(got.quote)}”</em>` : ""}</div></div></div>`;
}

function moduleBreakdown(co) {
  // Per-module expandable panels: the module's word + number, the exact
  // averaging arithmetic, then every stored per-parameter judgement.
  let html = "";
  for (const m of state.fw.modules) {
    const md = co.modules[m.id];
    const params = state.fw.parameters.filter(p => p.module === m.id);
    const assessed = params.filter(p => co.params[p.id] && co.params[p.id].score != null);
    const silent = params.filter(p => !co.params[p.id] || co.params[p.id].score == null);
    const scores = assessed.map(p => co.params[p.id].score);
    const mathLine = assessed.length
      ? `Module score = average of its assessed parameters: (${scores.map(fmtScore).join(" + ")}) / ${scores.length} = <strong>${fmtScore(md.score)}</strong> (weight ×${md.weight} in the overall)`
      : "No parameters assessed in this module — it does not count toward the overall score.";
    html += `<details class="mod" ${assessed.length ? "open" : ""}>
      <summary><span class="mod-word ${scoreCls(md.score)}">${md.score == null ? "—" : paramWord(Math.max(-2, Math.min(2, Math.round(md.score))))}</span>
        <strong>${esc(m.name)}</strong>
        <span class="note">${md.assessed}/${md.total} assessed · score ${md.score == null ? "n/a" : fmtScore(md.score)}</span></summary>
      <p class="note calc">${mathLine}</p>
      <div class="params">${assessed.map(p => paramRow(p, co.params[p.id])).join("")}</div>
      ${silent.length ? `<p class="note">Not assessed (${co.qualitative_included ? "the calls & records were silent — never guessed" : "needs qualitative evidence"}): ${silent.map(p => esc(p.name)).join(" · ")}</p>` : ""}
    </details>`;
  }
  return html;
}

function companyHeader(sym, co) {
  return `<div class="co-head"><span class="nm">${esc(co.name)}</span>
      <span class="sym">${sym}</span>
      ${co.industry ? `<span class="tag">${esc(co.industry)}</span>` : ""}
      ${co.concalls ? `<span class="tag">🎙 ${co.concalls} concalls on file</span>` : ""}</div>
    <div class="facts">
      <div class="fact"><div class="v">₹${fmtCr(co.mcap)}</div><div class="k">Market cap</div></div>
      <div class="fact"><div class="v">${co.pe ?? "—"}</div><div class="k">P/E</div></div>
      <div class="fact"><div class="v">₹${co.price ? co.price.toLocaleString("en-IN") : "—"}</div><div class="k">Price</div></div>
    </div>`;
}

async function renderCompany(sym) {
  // THE analyst experience: one server call runs all three skills via the
  // AnalystSkill and returns the records AND the Markdown report together.
  // In PARALLEL, the ComparisonSkill builds the then-vs-now view (full
  // history vs last one year) for the right-hand panel.
  const cached = state.data.companies[sym];
  const firstTime = !(cached && cached.qualitative_included);
  const ph = document.createElement("div");
  ph.className = "card";
  const phBase = `<p>⚙️ Running the complete analysis for <strong>${esc(sym)}</strong> —
    business overview, quality framework, multibagger patterns, risk check and the written report${state.ai ?
    (firstTime ? " <em>(first run: several deep reads of ALL its concalls — this can take several minutes; everything is cached afterwards)</em>" : " (served from cache)") : " (numbers only — AI is off)"}…</p>`;
  ph.innerHTML = phBase;
  $out().appendChild(ph);
  const cmpTick = { el: null };
  const cmpPromise = jobFetch("comparison", sym, t => {
    if (cmpTick.el && cmpTick.el.isConnected) cmpTick.el.textContent =
      `⏱ computing both views for ${fmtElapsed(t)} — long first runs are normal, nothing has timed out.`;
  });
  cmpPromise.catch(() => { /* handled when the panel attaches */ });
  let out = null, failWhy = "";
  try {
    out = await jobFetch("analysis", sym, t => {
      if (ph.isConnected) ph.innerHTML = phBase +
        `<p class="note">⏱ running for ${fmtElapsed(t)} — long first runs are normal, nothing has timed out.</p>`;
    });
  } catch (e) { failWhy = e.message || String(e); }
  ph.remove();
  if (!out) return card(`<p>Analysis failed for ${esc(sym)}: ${esc(failWhy || "unknown error")}.</p>
    <p class="note">Finished work is cached on the server — re-asking usually resumes where it left off.</p>`);
  const ba = out.business, mb = out.patterns, qr = out.risks, rt = out.rating;

  // Two columns: the full analyst workup on the left, the one-year
  // comparison on the right (stacks below on narrow screens).
  $out().insertAdjacentHTML("beforeend",
    `<div class="duo" data-sym="${sym}"><div class="col-main"></div>
     <aside class="col-cmp"><div class="card cmp-wait">
       <h2>Then vs now — the last one year</h2>
       <p class="note">⏳ Building the one-year comparison: the same three engines re-run on
       just the last year's evidence, then compared verdict-by-verdict with the long view${
         state.ai ? " <em>(first run of a company computes both views — this is the slowest step; cached afterwards)</em>" : ""}…</p>
       <p class="note cmp-tick"></p>
     </div></aside></div>`);
  const duo = $out().querySelector(`.duo[data-sym="${sym}"]`);
  const main = duo.querySelector(".col-main");
  const aside = duo.querySelector(".col-cmp");
  cmpTick.el = duo.querySelector(".cmp-tick");

  // 1. About the business
  cardIn(main, aboutCard(sym, out));
  // 2. The verdict (+ download of the SAME report)
  cardIn(main, verdictCard(sym, out));
  // 3. The three skill sections, every dimension
  cardIn(main, `<h2>Section 1 — How good is the business?</h2>
    <p class="note">The 34-check quality framework: <strong>${verdictWord(ba.overall)}</strong>
    (score ${fmtScore(ba.overall)} on a −2…+2 scale) ·
    ${Math.round((ba.coverage || 0) * 100)}% of checks had evidence — unanswerable checks are marked, never guessed.</p>
    <h3>Area scorecard</h3>${moduleBars({ modules: ba.modules })}
    ${trendSparks(out.trends)}
    <h3>Every check, area by area — with its why</h3>
    ${moduleBreakdown({ modules: ba.modules, params: ba.params, qualitative_included: ba.qualitative_included })}`);
  cardIn(main, `<h2>Section 2 — Does it look like a long-term winner?</h2>
    ${patternsSection(mb)}`);
  cardIn(main, `<h2>Section 3 — What could break it?</h2>
    ${risksSection(qr)}
    ${(out.extensions || []).filter(e => e.section_md).map(e =>
       `<h3>${esc(e.name)}</h3><p class="note">Additional analysis from the ${esc(e.skill)} skill (${esc(e.status)}).</p>`).join("")}
    ${state.ai ? `
      <h3>Ask about this analysis</h3>
      <form class="qa-form" data-sym="${sym}">
        <input type="text" placeholder="e.g. Why this rating? What changed in the last year? Which risk worries you most?" aria-label="Ask about this analysis">
        <button type="submit">Ask</button>
      </form>
      <div class="qa-out"></div>
      <p class="note">Answers come strictly from the records on this page — including the
      one-year comparison — and the call transcripts; never thin air.</p>` : ""}`);
  const qaForm = $out().querySelector(`.qa-form[data-sym="${sym}"]`);
  if (qaForm) qaForm.addEventListener("submit", e => {
    e.preventDefault();
    const inp = qaForm.querySelector("input");
    if (inp.value.trim()) askVerdict(sym, inp.value.trim(), qaForm.nextElementSibling);
  });
  wireDownload(sym, out.md);

  // the right panel lands whenever the ComparisonSkill finishes
  cmpPromise.then(c => {
    aside.innerHTML = "";
    cardIn(aside, comparisonPanel(sym, c));
    wireCmpDownload(sym, c.md);
  }).catch(e => {
    aside.innerHTML = "";
    cardIn(aside, `<h2>Then vs now — the last one year</h2>
      <p class="note">The one-year comparison could not be built: ${esc(e.message || e)}.
      The full analysis on the left is unaffected — try again with the ↻ button or re-ask.</p>`);
  });
}

function aboutCard(sym, out) {
  const ov = out.overview;
  const mk = out.market || {};
  const parts = (ov && ov.parts) || [];
  return `${companyHeader(sym, { name: out.name, industry: out.industry,
      mcap: mk.mcap, pe: mk.pe, price: mk.price, concalls: 0 })}
    <h3>About the business</h3>
    ${ov ? `<p>${esc(ov.what_it_does || "")}</p>` +
      (parts.length ? `<h3>The parts of the business</h3><ul class="parts">` +
        parts.map(pt => `<li><strong>${esc(pt.name || "?")}</strong> — ${esc(pt.what || "")}</li>`).join("") + `</ul>
        <p class="note">Described strictly from management's own words on the earnings calls.</p>` : "")
      : `<p class="note">No conference-call transcripts were available to describe the business in
         management's own words — the analysis below rests on the financial statements.</p>`}`;
}

function verdictCard(sym, out) {
  const rt = out.rating;
  const story = out.summary && out.summary.summary ? out.summary.summary : null;
  const watch = out.summary && out.summary.watch_items ? out.summary.watch_items : null;
  return `<h2>The verdict</h2>
    ${ratingCard(rt)}
    <p>${esc(out.verdict_plain || "")}</p>
    ${story ? `<details class="mod"><summary><strong>The story in depth</strong>
        <span class="note">the grounded narrative connecting all three analyses</span></summary>
        ${story.map(pa => `<p>${esc(pa)}</p>`).join("")}
        <p class="note">Written strictly from the analyses below — names it could not ground were grounds to reject it.</p>
      </details>` : ""}
    ${watch ? `<h3>What to watch</h3><ul>` + watch.map(w => `<li>${esc(w)}</li>`).join("") + `</ul>` : ""}
    <p><a class="chip" id="dl-${sym}" href="api/report/${sym}" download="${sym}_analysis.md">📄 Download this analysis (Markdown)</a>
      <span class="note">— generated together with this page from the same records; page and file can never disagree.</span></p>`;
}

function wireDownload(sym, md) {
  // The MD arrived WITH the analysis — offer it instantly from memory
  // (the href fallback still works if the blob is unavailable).
  const a = document.getElementById(`dl-${sym}`);
  if (a && md) {
    const url = URL.createObjectURL(new Blob([md], { type: "text/markdown" }));
    a.href = url;
  }
}

function wireCmpDownload(sym, md) {
  const a = document.getElementById(`dlc-${sym}`);
  if (a && md) {
    const url = URL.createObjectURL(new Blob([md], { type: "text/markdown" }));
    a.href = url;
  }
}

/* ------------- the then-vs-now panel (ComparisonSkill, right column) ------------- */

const DIR_META = {
  "improved": { word: "IMPROVED in the last year", icon: "📈", cls: "pos" },
  "declined": { word: "DECLINED in the last year", icon: "📉", cls: "neg" },
  "held steady": { word: "HELD STEADY in the last year", icon: "➡️", cls: "mid" },
  "not comparable": { word: "could not be compared", icon: "⬜", cls: "mid" },
};
const fmtPts = v => v == null ? "—" : String(v);
const fmtDelta = v => v == null ? "—" : (v > 0 ? "+" : "") + v;

function cmpMoveRows(items, kind) {
  // one movement line = verdict shift + BOTH sides' evidence (the why)
  return (items || []).map(i => {
    const from = i.from ?? i.full_word, to = i.to ?? i.recent_word;
    const why = i.now || i.explanation || i.why_now || "";
    const then = (i.then && i.then !== i.now) ? i.then : null;
    return `<details class="mod">
      <summary><span class="mod-word ${kind}">${esc(from)} → ${esc(to)}</span>
        <strong>${esc(i.name || i.check)}</strong>${i.area ? ` <span class="note">${esc(i.area)}</span>` : ""}</summary>
      ${why ? `<p class="note calc">${esc(why)}</p>` : ""}
      ${then ? `<p class="note">The long view had said: ${esc(then)}</p>` : ""}
      ${i.note ? `<p class="note">${esc(i.note)}</p>` : ""}
    </details>`;
  }).join("");
}

function cmpBucket(title, t, verbs, extraTop) {
  const nImp = (t.improved || []).length, nReg = (t.regressed || []).length;
  return `<details class="mod" ${nImp + nReg ? "open" : ""}>
    <summary><span class="mod-word ${nReg > nImp ? "neg" : nImp > nReg ? "pos" : "mid"}">${nImp}▲ ${nReg}▼</span>
      <strong>${esc(title)}</strong></summary>
    <p class="note calc">${esc(t.overall || "")}</p>
    ${extraTop || ""}
    ${nImp ? `<h4>That ${esc(verbs[0])}</h4>${cmpMoveRows(t.improved, "pos")}` : ""}
    ${nReg ? `<h4>That ${esc(verbs[1])}</h4>${cmpMoveRows(t.regressed, "neg")}` : ""}
    ${(t.unchanged || []).length ? `<p class="note">Unchanged: ${t.unchanged.map(i =>
        esc((i.name || i.check) + (i.from ? ` (${i.from})` : ""))).join(" · ")}</p>` : ""}
    ${(t.carried || []).length ? `<p class="note">Carried forward from the long view unchanged
      (the window could not re-test these): ${t.carried.map(i =>
        esc((i.name || i.check) + ` (${i.verdict || i.word})`)).join(" · ")}</p>` : ""}
    ${(t.window_excluded || []).length ? `<p class="note">Needs longer history than the one-year
      lens allows — listed, never counted as regressions: ${t.window_excluded.map(i =>
        esc(`${i.check} (long view: ${i.full_word})`)).join(" · ")}</p>` : ""}
    ${(t.not_comparable || []).length ? `<p class="note">Not comparable: ${t.not_comparable.map(i =>
        esc(`${i.name} (${i.from} → ${i.to})`)).join(" · ")}</p>` : ""}
    ${(t.newly_visible || []).length ? `<h4>Newly assessable in the recent view</h4>
      ${t.newly_visible.map(i => `<p class="note">✳️ <strong>${esc(i.check)}</strong> —
        ${esc(i.recent_word)}: ${esc(i.explanation || "")}</p>`).join("")}` : ""}
  </details>`;
}

function comparisonPanel(sym, c) {
  const rec = c.record, rd = rec.rating;
  const dir = DIR_META[rd.direction] || DIR_META["not comparable"];
  const scores = rd.delta == null ? "" :
    `<span class="cov">${rd.full.grade} ${rd.full.score}/100 → ${rd.recent.grade} ${rd.recent.score}/100
     (${fmtDelta(rd.delta)} points)</span>`;
  const pillarTbl = rd.delta == null ? "" : `
    <table class="rank cmp-tbl"><thead><tr><th>Pillar</th><th>Long view</th>
      <th>Last one year</th><th>Change</th></tr></thead><tbody>
    ${rec.pillars.map(p => `<tr><td>${esc(p.pillar)}</td><td>${fmtPts(p.full)}</td>
      <td>${fmtPts(p.recent)}</td><td>${fmtDelta(p.delta)}</td></tr>`).join("")}
    </tbody></table>
    <p class="note">A pillar move can be partly lens-driven — the one-year view cannot test
    multi-year fingerprints, which lowers its multibagger pillar mechanically. The buckets
    below separate genuine movement from window effects.</p>
    <details class="mod"><summary><strong>How each side built its number</strong></summary>
      ${rec.pillars.map(p => `<p class="note"><strong>${esc(p.pillar)}, long view:</strong> ${esc(p.full_why)}</p>
        <p class="note"><strong>${esc(p.pillar)}, last one year:</strong> ${esc(p.recent_why)}</p>`).join("")}
    </details>`;
  const numbers = (rec.numbers || []).length ? `
    <h3>The numbers behind the comparison</h3>
    <table class="rank cmp-tbl"><thead><tr><th>Measure</th><th>Long-view avg</th>
      <th>Year before last</th><th>Latest year</th><th>Change</th></tr></thead><tbody>
    ${rec.numbers.map(n => `<tr><td>${esc(n.measure)}</td>
      <td>${esc(n.long_avg)} <span class="note">(${n.n_years} yrs)</span></td>
      <td>${esc(n.prior)}</td><td>${esc(n.latest)}</td><td>${esc(n.change)}</td></tr>`).join("")}
    </tbody></table>` : "";
  const fr = rec.risks.fragility || {};
  const frBlock = fr.full ? `<p class="note"><strong>Financial resilience:</strong>
    ${esc((fr.full || "").toLowerCase())} on the long view vs
    ${esc((fr.recent || "").toLowerCase())} on the one-year view.</p>` : "";
  const gates = `<p class="note">Foundation test: ${esc(rec.patterns.gate_full || "?")} on the
    long view, ${esc(rec.patterns.gate_recent || "?")} on the one-year view.</p>`;
  return `<h2>Then vs now — the last one year</h2>
    <p class="note">The full-history view vs the same analysis run on just the last year's
    evidence. Only items assessed on BOTH views are compared; checks the one-year lens
    silences are listed separately — never counted as regressions.</p>
    <h3>Step 1 — The overall rating</h3>
    <div class="scoreline">
      <span class="big-score ${dir.cls}" style="font-size:22px">${dir.icon} ${esc(dir.word)}</span>
      ${scores}
    </div>
    <p class="note calc">${esc(rd.derivation)}</p>
    ${pillarTbl}
    ${numbers}
    <h3>Step 2 — Where it improved, where it regressed</h3>
    ${cmpBucket("Business quality (34 checks)", rec.business, ["improved", "regressed"])}
    ${cmpBucket("Multibagger patterns (11 patterns)", rec.patterns, ["strengthened", "weakened"], gates)}
    ${cmpBucket("Risks (8 channels)", rec.risks, ["eased", "worsened"], frBlock)}
    <p><a class="chip" id="dlc-${sym}" href="api/comparison_report/${sym}" download="${sym}_comparison.md">📄 Download the comparison (Markdown)</a>
      <span class="note">— generated together with this panel from the same comparison; panel and file can never disagree.</span></p>`;
}

function trendSparks(trends) {
  if (!trends) return "";
  const s = [];
  const add = (title, tr, unit) => {
    if (tr && tr.values && tr.values.filter(v => v != null).length >= 3)
      s.push(sparkline(title, tr.values, unit));
  };
  add("Sales (₹ Cr, yearly)", trends.sales, "");
  add("Operating margin", trends.opm, "%");
  add("Return on capital", trends.roce, "%");
  add("Cash conversion cycle", trends.ccc, " d");
  return s.length ? `<h3>The numbers over time</h3><div class="sparks">${s.join("")}</div>
    <p class="note">The same yearly figures the checks below judged — hover for each year's value.</p>` : "";
}

/* ---------------- unified rating + patterns + risks rendering ---------------- */

function ratingCard(rt) {
  if (rt.score == null) return `<p class="note">${esc(rt.derivation)}</p>`;
  const stars = "★".repeat(rt.stars) + "☆".repeat(5 - rt.stars);
  const cls = rt.score >= 65 ? "pos" : rt.score < 40 ? "neg" : "mid";
  const pillarRow = key => {
    const p = rt.pillars[key];
    const pts = p.points == null ? "—" : p.points;
    const w = p.points == null ? 0 : p.points;
    return `<div class="pillar">
      <div class="pl-head"><strong>${esc(p.name)}</strong>
        <span class="pl-pts">${pts}${p.points == null ? "" : " / 100"}</span></div>
      <div class="pl-bar"><div class="pl-fill" style="width:${w}%"></div></div>
      <div class="note">${esc(p.derivation)}</div>
    </div>`;
  };
  return `<div class="rating">
    <div class="scoreline">
      <span class="big-score ${cls}">${esc(rt.grade)}</span>
      <span class="stars">${stars}</span>
      <span class="cov">${rt.score} out of 100, combining all three analyses below</span>
    </div>
    <details class="mod" open>
      <summary><strong>How this rating was built</strong>
        <span class="note">every point earned or lost is listed — nothing hidden</span></summary>
      <p class="note calc">${esc(rt.derivation)}</p>
      ${pillarRow("quality")}${pillarRow("patterns")}${pillarRow("safety")}
    </details>
  </div>`;
}

const MB_VERDICT_CLS = { "STRONG FIT": "pos", "LIKELY FIT": "pos",
  "QUANT SIGNAL": "mid", "PARTIAL": "mid", "NO FIT": "neg", "NOT ASSESSED": "mid" };
const QR_VERDICT_CLS = { "HIGH RISK": "neg", "ELEVATED": "neg", "WATCH": "mid",
  "QUANT FLAG": "mid", "LOW": "pos", "NO SIGNAL": "pos", "NOT ASSESSED": "mid" };

function evidenceRows(list, iconMap) {
  return (list || []).map(e =>
    `<div class="ev">${iconMap[e.status] || "•"} ${esc(e.explanation)}</div>`).join("");
}

function patternsSection(mb) {
  const matched = mb.verdicts.filter(v =>
    ["STRONG FIT", "LIKELY FIT", "QUANT SIGNAL"].includes(v.verdict));
  const gate = mb.core_gate || {};
  const gateWord = { PASS: "passed in full", PARTIAL: "partly passed",
    FAIL: "did not pass", UNKNOWN: "could not be tested" }[gate.status] || "—";
  const rows = mb.verdicts.map(v => {
    const open = ["STRONG FIT", "LIKELY FIT"].includes(v.verdict) ? "open" : "";
    return `<details class="mod" ${open}>
      <summary><span class="mod-word ${MB_VERDICT_CLS[v.verdict] || "mid"}">${esc(v.verdict)}</span>
        <strong>${esc(v.name)}</strong> <span class="note">${esc(v.friendly)}</span></summary>
      <p class="note calc">Why: ${esc(v.derivation || v.verdict_friendly)}</p>
      ${v.qual && v.qual.fit ? `<p>${esc(v.qual.rationale || "")}</p>
        ${v.qual.quote ? `<p class="note">🎙 “${esc(v.qual.quote)}” — management, on an earnings call</p>` : ""}` : ""}
      ${evidenceRows(v.quant?.evidence, { supports: "✅", against: "❌", "no data": "⬜" })}
    </details>`;
  }).join("");
  return `<h3>Multibagger patterns — does it look like the long-term winners?</h3>
    <p class="note">${matched.length
      ? "Patterns it fits: <strong>" + matched.map(v => esc(v.name)).join(" · ") + "</strong>."
      : "No pattern is confirmed by the evidence."}
      The foundation test (steady cash + high returns on capital + growth) ${gateWord}
      (${gate.passed ?? "?"} of ${gate.of ?? "?"} checks).</p>
    ${rows}`;
}

function risksSection(qr) {
  const material = qr.verdicts.filter(v =>
    ["HIGH RISK", "ELEVATED", "QUANT FLAG"].includes(v.verdict));
  const fr = qr.fragility || {};
  const frWord = { SOUND: "no financial stress signals", STRAINED: "one financial stress signal",
    STRESSED: "multiple financial stress signals", UNKNOWN: "not enough data to stress-test" }[fr.status] || "—";
  const frRows = (fr.checks || []).map(c =>
    `<div class="ev">${c.flagged ? "⚠️" : c.flagged == null ? "⬜" : "✅"} ${esc(c.explanation)}</div>`).join("");
  const rows = qr.verdicts.map(v => {
    const open = ["HIGH RISK", "ELEVATED"].includes(v.verdict) ? "open" : "";
    return `<details class="mod" ${open}>
      <summary><span class="mod-word ${QR_VERDICT_CLS[v.verdict] || "mid"}">${esc(v.verdict)}</span>
        <strong>${esc(v.name)}</strong> <span class="note">${esc(v.friendly)}</span></summary>
      <p class="note calc">Why: ${esc(v.derivation || v.verdict_friendly)}</p>
      ${v.qual && v.qual.exposure ? `<p>${esc(v.qual.rationale || "")}</p>
        ${v.qual.quote ? `<p class="note">🎙 “${esc(v.qual.quote)}” — management, on an earnings call</p>` : ""}
        ${v.qual.mitigant ? `<p class="note">🌤 Silver lining: ${esc(v.qual.mitigant)}</p>` : ""}` : ""}
      ${evidenceRows(v.quant?.evidence, { "flags the risk": "⚠️", "no fingerprint": "✅", "no data": "⬜" })}
    </details>`;
  }).join("");
  return `<h3>Risk check — what could go wrong?</h3>
    <p class="note">${material.length
      ? "Risks worth your attention: <strong>" + material.map(v => esc(v.name)).join(" · ") + "</strong>."
      : "No risk channel shows both meaningful evidence and severity today."}
      The balance sheet shows ${frWord}.</p>
    ${frRows ? `<details class="mod"><summary><strong>Financial resilience checks</strong></summary>${frRows}</details>` : ""}
    ${rows}`;
}

async function askVerdict(sym, question, outEl) {
  outEl.insertAdjacentHTML("beforeend",
    `<div class="qa-q">Q: ${esc(question)}</div><div class="qa-a note">Thinking — answering from the stored analysis and the concalls…</div>`);
  const slot = outEl.lastElementChild;
  try {
    // job + poll, so a slow answer can't hit proxy timeouts (Codespaces)
    const res = await fetch(`api/jobs/ask/${sym}`, {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question }),
    });
    if (!res.ok) throw new Error((await res.json()).detail || res.status);
    const { job } = await res.json();
    const data = await pollJob("ask", job.split(":")[1],
      t => { slot.textContent = `Thinking for ${fmtElapsed(t)} — answering from the stored analysis and the concalls…`; });
    slot.className = "qa-a";
    slot.textContent = data.answer;
  } catch (e) {
    slot.textContent = "Failed: " + (e.message || e);
  }
}

function qualNote(co) {
  const st = co.qualitative_status;
  if (co.qualitative_included) return "";
  const why = {
    no_concalls: "this company has no concall transcripts on file",
    ai_unavailable: "AI is off — log in the Claude Code CLI (run <code>claude</code> once) or set ANTHROPIC_API_KEY, then restart the server",
    no_extractable_text: "the transcript PDF has no extractable text (scanned images)",
    skipped_quick: "quick mode skipped it",
  }[st] || "it could not run";
  return `<p class="note">ℹ️ Qualitative concall analysis not included: ${why}.
    Scores above are quantitative-only.</p>`;
}

function renderTopic(sym, topic) {
  const co = state.data.companies[sym];
  if (!co) return card(`<p>No data for ${esc(sym)}.</p>`);
  const m = topic.module;
  const md = co.modules[m];
  let spark = "";
  if (m === "CAP" || (topic.param || "").includes("working_capital"))
    spark = sparkline("Cash conversion cycle", co.series.ccc, " d");
  if (m === "ROC") spark = sparkline("Operating margin", co.series.opm, "%");
  if (m === "GRW") spark = sparkline("Sales (₹ Cr)", co.series.sales, "");
  const fwm = state.fw.modules.find(x => x.id === m);
  card(`${companyHeader(sym, co)}
    <div class="scoreline">
      <span class="big-score ${scoreCls(md.score)}">${fmtScore(md.score)}</span>
      <span class="cov">${esc(modName(m))} module score · ${md.assessed}/${md.total} parameters assessed</span>
    </div>
    ${fwm?.guidance ? `<p class="note">${esc(fwm.guidance)}</p>` : ""}
    ${spark ? `<div class="sparks">${spark}</div>` : ""}
    ${paramRows(co, m)}
    <p class="note">Full picture: <span class="co-link" data-co="${sym}">open the complete ${sym} scorecard</span>.</p>`);
}

function renderRanking(n, moduleId, industry, asc) {
  // Require >= 5 of the 34 parameters assessed (coverage >= ~15%): a single
  // inflated signal (e.g. CFO-based CROCI for lenders) must not top a
  // quality ranking. Honest-coverage discipline from the skill's rubric.
  const MIN_COV = 0.14;
  const rows = Object.entries(state.data.companies)
    .map(([sym, c]) => ({
      sym, c,
      s: moduleId ? c.modules[moduleId]?.score : c.overall,
      cov: c.coverage,
    }))
    .filter(r => r.s != null && r.cov >= MIN_COV &&
                 (!industry || r.c.industry === industry));
  rows.sort((a, b) => asc ? (a.s - b.s || a.cov - b.cov) : (b.s - a.s || b.cov - a.cov));
  const top = rows.slice(0, n);
  const title = `${asc ? "Weakest" : "Best"} ${top.length} companies` +
    (moduleId ? ` by ${modName(moduleId)}` : " by overall quality") +
    (industry ? ` in ${industry}` : "");
  const trs = top.map((r, i) => `<tr class="rowlink" data-co="${r.sym}">
      <td>${i + 1}</td><td><span class="co-link">${esc(r.c.name)}</span> <span class="sym">${r.sym}</span></td>
      <td>${esc(r.c.industry || "—")}</td>
      <td><strong style="color:${r.s > 0 ? "var(--series-1)" : r.s < 0 ? "var(--neg)" : "var(--mid)"}">${paramWord(Math.max(-2, Math.min(2, Math.round(r.s))))}</strong>
          <span class="note">(${fmtScore(r.s)})</span></td>
      <td>${Math.round(r.cov * 100)}%</td>
      <td>₹${fmtCr(r.c.mcap)}</td><td>${r.c.pe ?? "—"}</td></tr>`).join("");
  card(`<h2>${esc(title)}</h2>
    <p class="note">Ranked by score then coverage — a better-evidenced company outranks a
    thinly-evidenced one, and companies with fewer than 5 of 34 parameters assessed are
    excluded so one inflated signal can't top the list. Scores are quantitative-only;
    click a row for the full explainable scorecard.</p>
    <table class="rank"><thead><tr><th>#</th><th>Company</th><th>Industry</th>
      <th>Score</th><th>Coverage</th><th>Mcap</th><th>P/E</th></tr></thead>
    <tbody>${trs}</tbody></table>`);
}

function renderCompare(a, b) {
  const A = state.data.companies[a], B = state.data.companies[b];
  if (!A || !B) return card(`<p>Missing data for comparison.</p>`);
  const half = (sym, co) => `<div>
      <div class="co-head"><span class="nm">${esc(co.name)}</span> <span class="sym">${sym}</span></div>
      <div class="scoreline"><span class="big-score ${scoreCls(co.overall)}" style="font-size:22px">${verdictWord(co.overall)}</span>
      <span class="cov">${fmtScore(co.overall)} · coverage ${Math.round(co.coverage * 100)}%</span></div>
      ${moduleBars(co)}
      <p class="note"><span class="co-link" data-co="${sym}">full ${sym} scorecard →</span></p>
    </div>`;
  card(`<h2>Compare: ${esc(A.name)} vs ${esc(B.name)}</h2>
    <div class="grid2">${half(a, A)}${half(b, B)}</div>`);
}

function renderFramework(moduleId) {
  const mods = moduleId ? state.fw.modules.filter(m => m.id === moduleId) : state.fw.modules;
  let html = `<h2>The quality framework (${state.fw.parameters.length} parameters, v${state.fw.version})</h2>
    <p class="note">Transcribed in full from the source document — the skill enforces that
    none is missed. Each company is scored −2…+2 per parameter; quantitative ones from the
    financial statements, qualitative ones from concalls / annual reports.</p>`;
  for (const m of mods) {
    const ps = state.fw.parameters.filter(p => p.module === m.id);
    html += `<h3>${m.name}</h3><div class="params">` + ps.map(p =>
      `<div class="prow"><div class="pscore mid">${p.nature === "quantitative" ? "𝟙" : p.nature === "hybrid" ? "◐" : "✎"}</div>
       <div class="pbody"><div class="pn">${esc(p.name)} <span class="tag">${p.nature}</span></div>
       <div class="pr">${esc(p.description)}</div></div></div>`).join("") + `</div>`;
  }
  html += `<p class="note">𝟙 quantitative · ◐ hybrid · ✎ qualitative</p>`;
  card(html);
}

function renderHelp() {
  card(`<h2>What you can ask</h2><ul>
    <li>“analyse DIXON” / “tell me about Asian Paints” — full scorecard</li>
    <li>“best 10 companies” / “top 5 by growth” / “worst 10 by working capital” — rankings</li>
    <li>“select good businesses in PHARMA” — industry-filtered picks</li>
    <li>“compare TITAN and DMART” — side by side</li>
    <li>“working capital of IXIGO” / “margins of INFY” — topic deep-dive</li>
    <li>“explain the framework” / “explain return on capital” — methodology</li></ul>`);
}
