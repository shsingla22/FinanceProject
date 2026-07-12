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
      ? "; qualitative concall analysis runs automatically via " +
        (h.ai_backend === "claude_code_cli" ? "your Claude subscription" : "the Claude API") +
        " (first analysis of a company takes ~30–60s, then it's cached)."
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
function echo(q) { $out().insertAdjacentHTML("beforeend", `<div class="you">You asked: “${esc(q)}”</div>`); }
function card(html) { $out().insertAdjacentHTML("beforeend", `<div class="card">${html}</div>`); attachSparkHover(); }
function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }
const fmtScore = s => s == null ? "n/a" : (s > 0 ? "+" : "") + (Math.round(s * 100) / 100);
const scoreCls = s => s == null ? "mid" : s > 0.25 ? "pos" : s < -0.25 ? "neg" : "mid";
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

function paramRows(co, moduleId) {
  const params = state.fw.parameters.filter(p => !moduleId || p.module === moduleId);
  let assessed = "", qual = [];
  for (const p of params) {
    const got = co.params[p.id];
    if (got && got.score != null) {
      const srcTag = got.source === "ai_concall" ? `<span class="tag">🤖 concall</span>`
                   : got.source === "fused" ? `<span class="tag">◐ quant + concall</span>` : "";
      assessed += `<div class="prow">
        <div class="pscore ${scoreCls(got.score)}">${fmtScore(got.score)}</div>
        <div class="pbody"><div class="pn">${esc(p.name)} <span class="tag">${p.nature}</span> ${srcTag}</div>
        <div class="pr">${esc(got.rationale)}${got.quote ? ` — <em>“${esc(got.quote)}”</em>` : ""}</div></div></div>`;
    } else {
      qual.push(`<li><strong>${esc(p.name)}</strong> — ${esc(p.signal)}</li>`);
    }
  }
  let html = "";
  if (assessed) html += `<h3>Assessed (financials${co.qualitative_included ? " + concall" : ""})</h3><div class="params">${assessed}</div>`;
  if (qual.length) html += `<h3>${co.qualitative_included
      ? "Not assessed — the concall was silent on these (never guessed)"
      : "Needs qualitative judgement (concalls / annual reports)"}</h3>
    <ul class="qual-list">${qual.join("")}</ul>`;
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
  let co = state.data.companies[sym];
  let excerpt = "";
  // Immediate feedback: the server runs BOTH modules live — quantitative
  // signals now, then the qualitative playbook over the latest concall
  // (first time per company; cached afterwards).
  const firstTime = !(co && co.qualitative_included);
  const ph = document.createElement("div");
  ph.className = "card";
  ph.innerHTML = `<p>⚙️ Running the complete analysis for <strong>${esc(sym)}</strong> —
    quantitative signals now${state.ai ? ", then the qualitative playbook over the latest concall" +
    (firstTime ? " <em>(first run for this company: ~30–60s via Claude)</em>" : " (cached)") : ""}…</p>`;
  $out().appendChild(ph);
  try {
    const live = await fetch(`api/company/${sym}`).then(r => r.ok ? r.json() : null);
    if (live) { co = live.record; state.data.companies[sym] = co; excerpt = co.concall_excerpt || ""; }
  } catch (_) { /* fall back to cached quant-only record */ }
  ph.remove();
  if (!co) return card(`<p>No data for ${esc(sym)}.</p>`);
  const sparkHtml = [
    sparkline("Sales (₹ Cr, FY series)", co.series.sales, ""),
    sparkline("Operating margin", co.series.opm, "%"),
    sparkline("Cash conversion cycle", co.series.ccc, " d"),
  ].join("");
  const mgmt = co.mgmt?.length
    ? `<h3>Current management (from annual reports)</h3><ul class="mgmt">` +
      co.mgmt.map(m => `<li><strong>${esc(m.role)}:</strong> ${esc(m.name)}</li>`).join("") + `</ul>`
    : "";
  card(`${companyHeader(sym, co)}
    <div class="scoreline">
      <span class="big-score ${scoreCls(co.overall)}">${fmtScore(co.overall)}</span>
      <span class="cov">overall quality score (−2…+2) ·
        coverage ${Math.round(co.coverage * 100)}% of 34 parameters —
        the rest need qualitative judgement</span>
    </div>
    <h3>Module scorecard</h3>${moduleBars(co)}
    ${sparkHtml ? `<h3>Key trends</h3><div class="sparks">${sparkHtml}</div>` : ""}
    ${paramRows(co, null)}
    ${mgmt}
    ${qualNote(co)}
    ${excerpt ? `<h3>Latest concall (live extract)</h3>
      <p class="note" style="white-space:pre-wrap">…${esc(excerpt.slice(-1200))}</p>` : ""}`);
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
      <td><strong class="${scoreCls(r.s)}" style="color:${r.s > 0 ? "var(--series-1)" : r.s < 0 ? "var(--neg)" : "var(--mid)"}">${fmtScore(r.s)}</strong></td>
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
      <div class="scoreline"><span class="big-score ${scoreCls(co.overall)}">${fmtScore(co.overall)}</span>
      <span class="cov">coverage ${Math.round(co.coverage * 100)}%</span></div>
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
