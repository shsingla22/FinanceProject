/* Company Analyst v2 — precomputed client.
   Everything renders from the STORED Markdown reports (served instantly by
   server.py); this file parses plain-English intent, renders the reports,
   draws the financial charts, and runs the report-grounded Q&A. */

"use strict";

const state = { data: null, names: [], ready: false, ai: false, pendingQ: null };

init();

function setStatus(html) {
  const el = document.getElementById("bootline");
  if (el) el.innerHTML = html;
}

async function init() {
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
  window.addEventListener("error", e => showError(e.message));
  window.addEventListener("unhandledrejection", e =>
    showError(e.reason && e.reason.message ? e.reason.message : String(e.reason)));

  let h = null;
  try { h = await fetch("api/health").then(r => r.ok ? r.json() : null); } catch (_) {}
  if (!h || h.mode !== "precomputed") {
    setStatus("❌ Backend not reachable. Start it with: " +
      "<code>cd UserInterfaceV2 && uvicorn server:app --host 0.0.0.0 --port 8001</code> then reload.");
    return;
  }
  state.ai = !!h.ai_qa;
  try {
    state.data = await fetch("api/companies").then(r => r.json());
  } catch (e) {
    setStatus(`❌ Failed to load the company list: ${esc(e.message)}.`);
    return;
  }
  state.names = Object.entries(state.data.companies).map(([sym, c]) => ({
    sym, name: c.name || sym, analysed: c.analysed,
    hay: (sym + " " + (c.name || "")).toUpperCase(),
  }));
  state.ready = true;
  setStatus(`<strong>${state.data.n_analysed}</strong> of ${state.data.n} companies have
    stored reports — every view is instant.` + (state.ai ? "" :
    " <em>(Q&amp;A runs in extract-from-report mode — AI is off.)</em>"));
  if (state.pendingQ) { const q = state.pendingQ; state.pendingQ = null; safeHandle(q); }
}

function showError(msg) {
  const out = document.getElementById("out");
  if (out) out.insertAdjacentHTML("beforeend",
    `<div class="card"><h2>Something went wrong</h2><p class="note">${esc(msg)}</p></div>`);
}

function safeHandle(q) {
  if (!state.ready) { state.pendingQ = q; return; }
  Promise.resolve(handle(q)).catch(e => showError(e.message || String(e)));
}

/* ---------------- intent parsing (same grammar as v1) ---------------- */

function findCompanies(q) {
  const up = q.toUpperCase();
  const hits = [];
  const tokens = up.split(/[^A-Z0-9&\-]+/).filter(t => t.length >= 2);
  for (const n of state.names) {
    if (tokens.includes(n.sym)) { hits.push({ ...n, w: 100 }); continue; }
    const words = n.name.toUpperCase().split(/\s+/);
    let w = 0;
    for (const t of tokens)
      if (t.length >= 4 && words.some(wd => wd.startsWith(t))) w += t.length;
    if (w > 0) hits.push({ ...n, w });
  }
  hits.sort((a, b) => b.w - a.w);
  const seen = new Set(); const out = [];
  for (const h of hits) if (!seen.has(h.sym)) { seen.add(h.sym); out.push(h); }
  return out;
}

function handle(q) {
  const low = q.toLowerCase();
  const out = document.getElementById("out");
  out.innerHTML = "";
  echo(q);

  if (/\b(help|how (do|to)|what can)\b/.test(low)) return renderHelp();

  const cos = findCompanies(q);
  const compareMode = /\b(compare|vs\.?|versus)\b/.test(low) && cos.length >= 2;
  const rankMode = /\b(best|top|rank|select|pick|screen|worst|bottom)\b/.test(low) &&
                   !compareMode && cos.length === 0;

  if (compareMode) return renderCompare(cos[0].sym, cos[1].sym);
  if (rankMode) {
    const nMatch = low.match(/\b(top|best|worst|bottom)\s*(\d{1,3})?/);
    const n = nMatch && nMatch[2] ? Math.min(200, +nMatch[2]) : 10;
    const asc = /\b(worst|bottom)\b/.test(low);
    const inds = [...new Set(Object.values(state.data.companies)
      .map(c => c.industry).filter(Boolean))];
    const ind = inds.find(i => low.includes(i.toLowerCase()));
    return renderRanking(n, asc ? "worst" : "best", ind || null);
  }
  if (cos.length >= 1) return renderCompany(cos[0].sym);

  card(`<h2>Didn't catch that</h2>
    <p>I couldn't find a company or intent in “${esc(q)}”. Try “analyse COLPAL”,
    “top 20 companies”, “worst 10”, or “compare DMART and APOLLOHOSP”.</p>`);
}

/* ---------------- small helpers ---------------- */

const $out = () => document.getElementById("out");
function echo(q) { $out().insertAdjacentHTML("beforeend", `<div class="you">You asked: “${esc(q)}”</div>`); }
function card(html) { $out().insertAdjacentHTML("beforeend", `<div class="card">${html}</div>`); }
function cardIn(el, html) { el.insertAdjacentHTML("beforeend", `<div class="card">${html}</div>`); }
function esc(s) { return String(s).replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c])); }
const fmtCr = v => v == null ? "—" : v >= 1e5 ? (v / 1e5).toFixed(1) + " L Cr" : Math.round(v).toLocaleString("en-IN") + " Cr";
const fmtNum = v => Math.abs(v) >= 1000 ? Math.round(v).toLocaleString("en-IN") : (Math.round(v * 10) / 10);
const fmtElapsed = s => s < 60 ? `${Math.round(s)}s`
  : `${Math.floor(s / 60)}m ${String(Math.round(s % 60)).padStart(2, "0")}s`;

const GRADE_CLS = { Outstanding: "pos", Strong: "pos", Decent: "mid",
                    Mixed: "mid", Weak: "neg" };
const DIR_META = {
  "improved": { icon: "📈", cls: "pos" }, "declined": { icon: "📉", cls: "neg" },
  "held steady": { icon: "➡️", cls: "mid" },
  "not comparable": { icon: "⬜", cls: "mid" },
};

async function jget(url) {
  const r = await fetch(url);
  if (!r.ok) {
    let d = ""; try { d = (await r.json()).detail || ""; } catch (_) {}
    throw new Error(d || `HTTP ${r.status}`);
  }
  return r.json();
}

/* ---------------- Markdown rendering (self-contained) ----------------
   The stored reports use headings, bold/italic, bullet lists, tables,
   blockquotes and horizontal rules — render exactly those, safely
   (everything is escaped first, then markup is layered back). */

function inlineMd(s) {
  return esc(s)
    .replace(/\*\*(.+?)\*\*/g, "<strong>$1</strong>")
    .replace(/(^|[^*])\*([^*\n]+)\*(?!\*)/g, "$1<em>$2</em>")
    .replace(/`([^`]+)`/g, "<code>$1</code>");
}

function mdToHtml(md, collapseFrom) {
  const lines = md.split("\n");
  const out = [];
  let list = null, table = null, quote = null, para = [];
  const flushPara = () => {
    if (para.length) { out.push(`<p>${inlineMd(para.join(" "))}</p>`); para = []; }
  };
  const flushList = () => { if (list) { out.push(`<ul>${list.join("")}</ul>`); list = null; } };
  const flushTable = () => {
    if (!table) return;
    const [head, ...body] = table;
    out.push(`<div class="tblwrap"><table class="rank"><thead><tr>` +
      head.map(c => `<th>${inlineMd(c)}</th>`).join("") + `</tr></thead><tbody>` +
      body.map(r => `<tr>` + r.map(c => `<td>${inlineMd(c)}</td>`).join("") + `</tr>`).join("") +
      `</tbody></table></div>`);
    table = null;
  };
  const flushQuote = () => {
    if (quote) { out.push(`<blockquote>${inlineMd(quote.join(" "))}</blockquote>`); quote = null; }
  };
  const flushAll = () => { flushPara(); flushList(); flushTable(); flushQuote(); };
  for (const raw of lines) {
    const line = raw.replace(/\s+$/, "");
    const h = line.match(/^(#{1,4})\s+(.*)$/);
    if (h) {
      flushAll();
      const lvl = h[1].length;
      out.push({ heading: true, lvl, html: inlineMd(h[2]) });
      continue;
    }
    if (/^(\s*)[-*]\s+/.test(line)) {
      flushPara(); flushTable(); flushQuote();
      list = list || [];
      list.push(`<li>${inlineMd(line.replace(/^(\s*)[-*]\s+/, ""))}</li>`);
      continue;
    }
    if (/^\|.*\|\s*$/.test(line)) {
      flushPara(); flushList(); flushQuote();
      const cells = line.slice(1, -1).split("|").map(c => c.trim());
      if (cells.every(c => /^:?-{2,}:?$/.test(c))) continue;   // separator row
      table = table || [];
      table.push(cells);
      continue;
    }
    if (/^>\s?/.test(line)) {
      flushPara(); flushList(); flushTable();
      quote = quote || [];
      quote.push(line.replace(/^>\s?/, ""));
      continue;
    }
    if (/^(---+|\*\*\*+)\s*$/.test(line)) { flushAll(); out.push("<hr>"); continue; }
    if (line.trim() === "") { flushAll(); continue; }
    flushTable(); flushList(); flushQuote();
    para.push(line.trim());
  }
  flushAll();
  // Fold the document into sections: heading levels >= collapseFrom become
  // collapsible <details> so a long report reads as an outline.
  return foldSections(out, collapseFrom || 2);
}

function foldSections(nodes, collapseFrom) {
  let html = "", open = 0;
  for (const n of nodes) {
    if (n && n.heading) {
      if (n.lvl >= collapseFrom) {
        while (open > 0 && open >= n.lvl - collapseFrom + 1) { html += "</details>"; open--; }
        html += `<details class="mdsec lvl${n.lvl}" open><summary>${n.html}</summary>`;
        open++;
      } else {
        while (open > 0) { html += "</details>"; open--; }
        html += `<h${n.lvl + 1} class="mdh">${n.html}</h${n.lvl + 1}>`;
      }
    } else {
      html += n;
    }
  }
  while (open > 0) { html += "</details>"; open--; }
  return html;
}

/* ---------------- charts (inline SVG, no libraries) ---------------- */

function chartSvg(meta, years, values) {
  const W = 340, H = 150, PL = 46, PR = 8, PT = 14, PB = 30;
  const pts = values.map((v, i) => ({ v, i })).filter(p => p.v != null);
  if (pts.length < 3) return "";
  const vs = pts.map(p => p.v);
  let min = Math.min(0, ...vs), max = Math.max(0, ...vs);
  if (min === max) { max = min + 1; }
  const pad = (max - min) * 0.08;
  max += pad; if (min < 0) min -= pad;
  const n = years.length;
  const x = i => PL + (n === 1 ? 0 : i * (W - PL - PR) / (n - 1));
  const bw = Math.max(4, (W - PL - PR) / Math.max(1, n) * 0.55);
  const y = v => PT + (max - v) / (max - min) * (H - PT - PB);
  let body = "";
  // gridlines + y labels (3 ticks)
  for (const tv of [min, (min + max) / 2, max]) {
    const ty = y(tv);
    body += `<line x1="${PL}" y1="${ty}" x2="${W - PR}" y2="${ty}" class="grid"/>` +
      `<text x="${PL - 4}" y="${ty + 3}" class="ax" text-anchor="end">${fmtNum(tv)}</text>`;
  }
  if (min < 0) body += `<line x1="${PL}" y1="${y(0)}" x2="${W - PR}" y2="${y(0)}" class="zero"/>`;
  // x labels: first, middle, last
  for (const i of [0, Math.floor((n - 1) / 2), n - 1]) {
    if (i >= 0 && years[i] != null)
      body += `<text x="${x(i)}" y="${H - 8}" class="ax" text-anchor="middle">${esc(String(years[i]).replace("Mar ", "FY"))}</text>`;
  }
  if (meta.kind === "bar") {
    for (const p of pts) {
      const yy = y(Math.max(0, p.v)), hh = Math.abs(y(p.v) - y(0));
      body += `<rect x="${x(p.i) - bw / 2}" y="${yy}" width="${bw}" height="${Math.max(1, hh)}"
        class="bar ${p.v < 0 ? "neg" : ""}"><title>${esc(String(years[p.i]))}: ${fmtNum(p.v)} ${esc(meta.unit)}</title></rect>`;
    }
  } else {
    let d = "", started = false;
    values.forEach((v, i) => {
      if (v == null) { started = false; return; }
      d += (started ? "L" : "M") + x(i).toFixed(1) + " " + y(v).toFixed(1) + " ";
      started = true;
    });
    body += `<path d="${d.trim()}" class="lineseries"/>`;
    for (const p of pts)
      body += `<circle cx="${x(p.i)}" cy="${y(p.v)}" r="2.6" class="dot">
        <title>${esc(String(years[p.i]))}: ${fmtNum(p.v)} ${esc(meta.unit)}</title></circle>`;
  }
  const last = pts[pts.length - 1].v;
  return `<figure class="chart">
    <figcaption>${esc(meta.title)} <span class="cur">${fmtNum(last)} ${esc(meta.unit)}</span></figcaption>
    <svg viewBox="0 0 ${W} ${H}" role="img" aria-label="${esc(meta.title)} by year">${body}</svg>
  </figure>`;
}

function chartsCard(data) {
  const figs = (data.charts || [])
    .map(m => chartSvg(m, data.years, data.series[m.key] || []))
    .filter(Boolean);
  if (!figs.length) return `<h2>The numbers as charts</h2>
    <p class="note">Not enough stored yearly figures to chart for this company.</p>`;
  return `<h2>The numbers as charts</h2>
    <p class="note">Yearly figures from the same screener.in-derived statements the stored
    analyses judged (₹ figures in crores) — hover any bar or point for the exact value.</p>
    <div class="charts">${figs.join("")}</div>`;
}

/* ---------------- company view: stored reports + charts + Q&A ---------------- */

async function renderCompany(sym) {
  const co = state.data.companies[sym];
  if (co && !co.analysed) {
    return card(`<h2>${esc(co.name)} <span class="sym">${sym}</span></h2>
      <p>This company is in the universe but has <strong>no stored analysis yet</strong> —
      ${state.data.n_analysed} of ${state.data.n} companies are covered so far.
      Run the batch analysis for it, or pick an analysed one (try “top 20 companies”).</p>`);
  }
  const ph = document.createElement("div");
  ph.className = "card";
  ph.innerHTML = `<p>⚡ Loading the stored reports for <strong>${esc(sym)}</strong>…</p>`;
  $out().appendChild(ph);
  let a, c, ch;
  try {
    [a, c, ch] = await Promise.all([
      jget(`api/analysis/${sym}`),
      jget(`api/comparison/${sym}`),
      jget(`api/charts/${sym}`).catch(() => null),
    ]);
  } catch (e) {
    ph.remove();
    return card(`<p>Could not load the stored reports for ${esc(sym)}: ${esc(e.message || e)}.</p>`);
  }
  ph.remove();

  $out().insertAdjacentHTML("beforeend",
    `<div class="duo" data-sym="${sym}"><div class="col-main"></div>
     <aside class="col-cmp"></aside></div>`);
  const duo = $out().querySelector(`.duo[data-sym="${sym}"]`);
  const main = duo.querySelector(".col-main");
  const aside = duo.querySelector(".col-cmp");

  const dir = DIR_META[c.direction] || DIR_META["not comparable"];
  cardIn(main, `
    <div class="co-head"><span class="nm">${esc(a.name)}</span>
      <span class="sym">${sym}</span>
      ${a.industry ? `<span class="tag">${esc(a.industry)}</span>` : ""}
      ${co && co.rank ? `<span class="tag">🏅 rank ${co.rank} of ${state.data.n_analysed}</span>` : ""}</div>
    <div class="facts">
      <div class="fact"><div class="v ${GRADE_CLS[a.grade] || "mid"}">${esc(a.grade || "—")}${a.score != null ? ` · ${a.score}/100` : ""}</div><div class="k">Stored rating</div></div>
      <div class="fact"><div class="v">${dir.icon} ${esc(c.direction || "—")}</div><div class="k">Last one year</div></div>
      <div class="fact"><div class="v">₹${fmtCr(a.market.mcap)}</div><div class="k">Market cap</div></div>
      <div class="fact"><div class="v">${a.market.pe ?? "—"}</div><div class="k">P/E</div></div>
    </div>
    <p class="note">Served instantly from the stored, validated reports — no recomputation.
    <a class="chip" id="dl-${sym}" href="api/report/${sym}" download="${sym}_analysis.md">📄 Download the analysis (Markdown)</a></p>`);

  if (ch) cardIn(main, chartsCard(ch));

  cardIn(main, `<h2>The analyst's report</h2>
    <p class="note">The complete stored workup — every check, pattern and risk with its why.
    Click any section heading to fold or unfold it.</p>
    <div class="mdreport">${mdToHtml(a.md, 2)}</div>`);

  cardIn(aside, `<h2>Then vs now — the last one year</h2>
    <div class="scoreline"><span class="big-score ${dir.cls}" style="font-size:20px">${dir.icon} ${esc((c.direction || "not comparable").toUpperCase())} in the last year</span></div>
    <p class="note"><a class="chip" id="dlc-${sym}" href="api/comparison_report/${sym}" download="${sym}_comparison.md">📄 Download the comparison (Markdown)</a></p>
    <div class="mdreport">${mdToHtml(c.md, 2)}</div>`);

  cardIn(aside, `<h3>Ask about this analysis</h3>
    <form class="qa-form" data-sym="${sym}">
      <input type="text" placeholder="e.g. Why this rating? What regressed last year? Which risk worries you most?" aria-label="Ask about this analysis">
      <button type="submit">Ask</button>
    </form>
    <div class="qa-out"></div>
    <p class="note">${state.ai
      ? "Answers come strictly from the two stored reports above — never thin air."
      : "AI is off — answers quote the most relevant passages of the stored reports, verbatim."}</p>`);
  const qaForm = duo.querySelector(`.qa-form[data-sym="${sym}"]`);
  qaForm.addEventListener("submit", e => {
    e.preventDefault();
    const inp = qaForm.querySelector("input");
    if (inp.value.trim()) askReports(sym, inp.value.trim(), qaForm.nextElementSibling);
  });
  wireDownload(`dl-${sym}`, a.md);
  wireDownload(`dlc-${sym}`, c.md);
}

function wireDownload(id, md) {
  const el = document.getElementById(id);
  if (el && md) el.href = URL.createObjectURL(new Blob([md], { type: "text/markdown" }));
}

/* ---------------- Q&A: job + poll (proxy-proof), grounded in the MDs -------- */

async function pollJob(id, onTick) {
  let misses = 0;
  for (;;) {
    await new Promise(r => setTimeout(r, 2500));
    let j = null;
    try {
      const r = await fetch(`api/jobs/ask/${id}`);
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      j = await r.json();
      misses = 0;
    } catch (e) {
      if (++misses >= 8) throw new Error("lost contact with the server: " + (e.message || e));
      continue;
    }
    if (j.state === "done") return j.result;
    if (j.state === "error") throw new Error(j.error || "failed on the server");
    if (onTick) onTick(j.elapsed || 0);
  }
}

async function askReports(sym, question, outEl) {
  outEl.insertAdjacentHTML("beforeend",
    `<div class="qa-q">Q: ${esc(question)}</div>
     <div class="qa-a note">Answering from the stored reports…</div>`);
  const slot = outEl.lastElementChild;
  try {
    const res = await fetch(`api/jobs/ask/${sym}`, {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question }),
    });
    if (!res.ok) throw new Error((await res.json()).detail || res.status);
    const { job } = await res.json();
    const data = await pollJob(job.split(":")[1],
      t => { slot.textContent = `Answering from the stored reports — ${fmtElapsed(t)}…`; });
    slot.className = "qa-a";
    slot.textContent = data.answer;
  } catch (e) {
    slot.textContent = "Failed: " + (e.message || e);
  }
}

/* ---------------- rankings with drill-down ---------------- */

async function renderRanking(n, order, industry) {
  let data;
  try {
    data = await jget(`api/ranking?n=${n}&order=${order}` +
      (industry ? `&industry=${encodeURIComponent(industry)}` : ""));
  } catch (e) {
    return card(`<p>Could not load the ranking: ${esc(e.message || e)}.</p>`);
  }
  const title = `${order === "worst" ? "Worst" : "Top"} ${data.n} companies` +
    (industry ? ` in ${industry}` : "") + " — by the stored analysis";
  const trs = data.rows.map(r => `<tr class="rowlink" data-co="${r.symbol}">
      <td>${r.rank}</td>
      <td><span class="co-link">${esc(r.name)}</span> <span class="sym">${r.symbol}</span></td>
      <td>${esc(r.industry || "—")}</td>
      <td><strong class="${GRADE_CLS[r.grade] || "mid"}">${esc(r.grade)}</strong>
          <span class="note">${r.score}/100</span></td>
      <td>${(DIR_META[r.direction] || {}).icon || ""} ${esc(r.direction || "—")}</td>
      <td>₹${fmtCr(r.mcap)}</td><td>${r.pe ?? "—"}</td></tr>`).join("");
  card(`<h2>${esc(title)}</h2>
    <p class="note">Ranked by the stored 0–100 rating (quality 45% + multibagger fit 30% +
    risk safety 25%) over the ${state.data.n_analysed} analysed companies.
    <strong>Click any row to drill down</strong> into that company's full stored reports.</p>
    <div class="tblwrap"><table class="rank"><thead><tr><th>#</th><th>Company</th><th>Industry</th>
      <th>Rating</th><th>Last 1 yr</th><th>Mcap</th><th>P/E</th></tr></thead>
    <tbody>${trs}</tbody></table></div>`);
}

/* ---------------- compare: two stored verdicts side by side ---------------- */

function extractSection(md, headingRe) {
  const lines = md.split("\n");
  let start = -1, lvl = 0;
  for (let i = 0; i < lines.length; i++) {
    const h = lines[i].match(/^(#{1,4})\s+(.*)$/);
    if (h && headingRe.test(h[2])) { start = i; lvl = h[1].length; break; }
  }
  if (start < 0) return "";
  const out = [];
  for (let i = start; i < lines.length; i++) {
    if (i > start) {
      const h = lines[i].match(/^(#{1,4})\s+/);
      if (h && h[1].length <= lvl) break;
    }
    out.push(lines[i]);
  }
  return out.join("\n");
}

async function renderCompare(s1, s2) {
  const missing = [s1, s2].filter(s => {
    const c = state.data.companies[s];
    return c && !c.analysed;
  });
  if (missing.length) {
    return card(`<h2>Compare: ${esc(s1)} vs ${esc(s2)}</h2>
      <p><strong>${missing.map(esc).join(" and ")}</strong> ${missing.length > 1 ? "have" : "has"}
      no stored analysis yet — ${state.data.n_analysed} of ${state.data.n} companies are covered
      so far, and comparing needs both. Try “top 20 companies” for analysed picks.</p>`);
  }
  let a1, a2, c1, c2;
  try {
    [a1, a2, c1, c2] = await Promise.all([
      jget(`api/analysis/${s1}`), jget(`api/analysis/${s2}`),
      jget(`api/comparison/${s1}`).catch(() => null),
      jget(`api/comparison/${s2}`).catch(() => null),
    ]);
  } catch (e) {
    return card(`<p>Could not compare: ${esc(e.message || e)} — both companies need stored reports.</p>`);
  }
  const half = (a, c) => {
    const dir = DIR_META[(c || {}).direction] || DIR_META["not comparable"];
    const verdict = extractSection(a.md, /^The verdict/);
    return `<div>
      <div class="co-head"><span class="nm">${esc(a.name)}</span> <span class="sym">${a.symbol}</span></div>
      <div class="scoreline"><span class="big-score ${GRADE_CLS[a.grade] || "mid"}" style="font-size:22px">
        ${esc(a.grade || "—")}${a.score != null ? ` · ${a.score}/100` : ""}</span>
        <span class="cov">${dir.icon} ${esc((c || {}).direction || "—")} in the last year</span></div>
      <div class="mdreport small">${mdToHtml(verdict, 3)}</div>
      <p class="note"><span class="co-link" data-co="${a.symbol}">full ${a.symbol} reports →</span></p>
    </div>`;
  };
  card(`<h2>Compare: ${esc(a1.name)} vs ${esc(a2.name)}</h2>
    <p class="note">Both stored verdicts, side by side — click through for the full reports.</p>
    <div class="grid2">${half(a1, c1)}${half(a2, c2)}</div>`);
}

function renderHelp() {
  card(`<h2>What you can ask</h2><ul>
    <li>“analyse COLPAL” / “tell me about Apollo Hospitals” — the full stored reports + charts</li>
    <li>“top 20 companies” / “worst 10” / “best 15 in PHARMA” — ranked lists you can click into</li>
    <li>“compare DMART and APOLLOHOSP” — stored verdicts side by side</li>
    <li>On any company page: ask the Q&amp;A box — answers are grounded in the stored reports</li></ul>`);
}
