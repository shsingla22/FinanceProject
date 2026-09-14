/* Company Analyst v2 — precomputed client.
   Everything renders from the STORED Markdown reports (served instantly by
   server.py); this file parses plain-English intent, renders the reports,
   draws the financial charts, and runs the report-grounded Q&A. */

"use strict";

const state = { data: null, names: [], ready: false, ai: false, pendingQ: null };
// Static mode (GitHub Pages build) is flagged by its index.html BEFORE this
// script loads — must be read before init() runs.
const STATIC = (typeof window !== "undefined") && window.STATIC_MODE === true;

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

  if (STATIC) {
    try {
      state.data = await jget("data/companies.json");
    } catch (e) {
      setStatus(`❌ Failed to load the site data: ${esc(e.message)}.`);
      return;
    }
    state.ai = false;
  } else {
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
  }
  state.names = Object.entries(state.data.companies).map(([sym, c]) => ({
    sym, name: c.name || sym, analysed: c.analysed,
    hay: (sym + " " + (c.name || "")).toUpperCase(),
  }));
  state.ready = true;
  setStatus("");
  const cov = document.getElementById("coverage");
  if (cov) cov.textContent =
    `Covering ${state.data.n_analysed} of ${state.data.n} NSE-listed companies today.` +
    (!STATIC && state.ai ? " AI assistance is on — ask anything in plain English." : "");
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

// Words that appear in hundreds of company names must never count as a
// match ("worst company" is a ranking request, not Cholamandalam ... Company Ltd).
const GENERIC_NAME_WORDS = new Set(["COMPANY", "COMPANIES", "LIMITED", "LTD",
  "INDIA", "INDIAN", "CORPORATION", "CORP", "GROUP", "THE", "AND", "OF"]);

function findCompanies(q) {
  const up = q.toUpperCase();
  const hits = [];
  const tokens = up.split(/[^A-Z0-9&\-]+/).filter(t => t.length >= 2);
  const nameTokens = tokens.filter(t => !GENERIC_NAME_WORDS.has(t));
  for (const n of state.names) {
    if (tokens.includes(n.sym)) { hits.push({ ...n, w: 100 }); continue; }
    const words = n.name.toUpperCase().split(/\s+/)
      .filter(wd => !GENERIC_NAME_WORDS.has(wd));
    let w = 0;
    for (const t of nameTokens)
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
  if (/\b(darvas|box screen|weekly screen|breakout screen|box method)\b/.test(low)) return renderDarvas();

  const cos = findCompanies(q);
  const compareMode = /\b(compare|vs\.?|versus)\b/.test(low) && cos.length >= 2;
  const rankMode = /\b(best|top|rank|select|pick|screen|worst|bottom)\b/.test(low) &&
                   !compareMode && cos.length === 0;

  // Anything shaped like a question is for the assistant (Opus): it
  // resolves the company AND answers, instead of just opening a page.
  const questiony = /\?|^(why|what|how|which|who|when|should|would|is|are|does|do|can|tell me|explain)\b/;
  if (!STATIC && state.ai && questiony.test(low) && !compareMode) return aiRoute(q);

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

  if (!STATIC && state.ai) return aiRoute(q);
  didntCatch(q);
}

function didntCatch(q) {
  card(`<h2>Didn't catch that</h2>
    <p>I couldn't find a company or intent in “${esc(q)}”. Try “analyse COLPAL”,
    “top 20 companies”, “worst 10”, or “compare DMART and APOLLOHOSP”.</p>`);
}

/* AI request routing (server mode): anything the plain patterns can't
   read goes to the assistant, which maps it onto the app's real actions —
   open a company, rank, compare, or answer a question about a company. */
async function aiRoute(q) {
  const ph = document.createElement("div");
  ph.className = "card";
  ph.innerHTML = `<p>🤔 Reading your request…</p>`;
  $out().appendChild(ph);
  let it = null;
  try {
    const res = await fetch("api/jobs/interpret", {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ query: q }),
    });
    if (!res.ok) throw new Error((await res.json()).detail || res.status);
    const { job } = await res.json();
    it = await pollJob("interpret", job.split(":")[1],
      t => { if (ph.isConnected) ph.innerHTML = `<p>🤔 Reading your request… ${fmtElapsed(t)}</p>`; });
  } catch (e) {
    ph.remove();
    return didntCatch(q);
  }
  ph.remove();
  if (!it || it.intent === "unknown") return didntCatch(q);
  if (it.intent === "rank")
    return renderRanking(it.n || 10, it.order || "best", it.industry || null);
  if (it.intent === "compare" && it.symbols.length >= 2)
    return renderCompare(it.symbols[0], it.symbols[1]);
  if (it.intent === "question" && it.symbols.length >= 1)
    return renderCompanyWithQuestion(it.symbols[0], it.question || it.query);
  if (it.symbols.length >= 1) return renderCompany(it.symbols[0]);
  return didntCatch(q);
}

async function renderCompanyWithQuestion(sym, question) {
  await renderCompany(sym);
  const form = $out().querySelector(`.qa-form[data-sym="${sym}"]`);
  if (!form || !question) return;
  form.querySelector("input").value = question;
  askReports(sym, question, form.nextElementSibling);
}

/* ---------------- small helpers ---------------- */

const $out = () => document.getElementById("out");
function echo(q) { $out().insertAdjacentHTML("beforeend", `<div class="you">You asked: “${esc(q)}”</div>`); }
function card(html) { $out().insertAdjacentHTML("beforeend", `<div class="card">${html}</div>`); }
function cardIn(el, html, cls) { el.insertAdjacentHTML("beforeend", `<div class="card${cls ? " " + cls : ""}">${html}</div>`); }
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

/* ---------------- data layer: one UI, two backends ----------------
   Server mode talks to /api. Static mode (GitHub Pages) reads the SAME
   data as prebuilt files (StaticWebsite/build_static.py). The static
   build's index.html sets window.STATIC_MODE; everything above and below
   this layer is identical in both, so UI improvements flow to both. */

async function jtext(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`HTTP ${r.status}`);
  return r.text();
}

const VERDICT_MD_RE = /^## The verdict: (.+?) — (\d+) out of 100/m;
const DIRECTION_MD_RE = /^## Step \d+ — The overall rating: (.+?) in the last year/m;

const _mdCache = {};
async function loadReports(sym) {
  if (!_mdCache[sym]) {
    const [a, c] = await Promise.all([
      jtext(`reports/${sym}_analysis.md`),
      jtext(`reports/${sym}_comparison.md`)]);
    _mdCache[sym] = { a, c };
  }
  return _mdCache[sym];
}

async function fetchAnalysis(sym) {
  if (!STATIC) return jget(`api/analysis/${sym}`);
  const co = state.data.companies[sym];
  if (!co || !co.analysed) throw new Error(`${sym} is not covered yet`);
  const { a } = await loadReports(sym);
  const m = a.match(VERDICT_MD_RE);
  return { symbol: sym, name: co.name, industry: co.industry,
           grade: m ? m[1] : co.grade, score: m ? +m[2] : co.score,
           market: { mcap: co.mcap, pe: co.pe, price: co.price }, md: a };
}

async function fetchComparison(sym) {
  if (!STATIC) return jget(`api/comparison/${sym}`);
  const { c } = await loadReports(sym);
  const m = c.match(DIRECTION_MD_RE);
  return { symbol: sym,
           direction: m ? m[1].toLowerCase()
                        : (state.data.companies[sym] || {}).direction,
           md: c };
}

async function fetchCharts(sym) {
  return jget(STATIC ? `data/charts/${sym}.json` : `api/charts/${sym}`);
}

let _rankingAll = null;
async function fetchRanking(n, order, industry) {
  if (!STATIC) return jget(`api/ranking?n=${n}&order=${order}` +
    (industry ? `&industry=${encodeURIComponent(industry)}` : ""));
  if (!_rankingAll) _rankingAll = await jget("data/ranking.json");
  let rows = _rankingAll.filter(r => r.score != null);
  if (industry) rows = rows.filter(r =>
    (r.industry || "").toLowerCase() === industry.toLowerCase());
  rows = [...rows].sort((x, y) => x.rank - y.rank);
  if (order === "worst") rows.reverse();
  rows = rows.slice(0, Math.max(1, Math.min(200, n)));
  return { order, n: rows.length, industry, rows };
}

async function fetchRelative(sym) {
  return jget(STATIC ? `data/relative/${sym}.json` : `api/relative/${sym}`);
}

const REPORT_API = { analysis: "api/report", comparison: "api/comparison_report",
                     stock_to_index: "api/relative_report" };
const reportHref = (sym, kind) => STATIC
  ? `reports/${sym}_${kind}.md`
  : `${REPORT_API[kind]}/${sym}`;

// Static-mode Q&A: quote the most relevant report passages, verbatim —
// the same behaviour as the server's no-AI mode, entirely client-side.
function extractiveAnswer(question, aMd, cMd) {
  const stop = new Set(["the", "and", "for", "what", "why", "how", "does",
    "this", "that", "with", "about", "are", "was", "has", "have", "its",
    "can", "you", "tell"]);
  const words = [...new Set((question.toLowerCase().match(/[a-z]{3,}/g) || [])
    .filter(w => !stop.has(w)))];
  const scored = [];
  for (const [src, md] of [["research", aMd], ["momentum", cMd]]) {
    const parts = md.split(/^#{1,4}\s+(.*)$/m);
    for (let i = 1; i < parts.length - 1; i += 2) {
      const title = parts[i].trim(), body = (parts[i + 1] || "").trim();
      if (HIDDEN_SECTION_RE.test(title)) continue;
      const hay = (title + " " + body).toLowerCase();
      let s = 0;
      for (const w of words) s += hay.split(w).length - 1;
      if (s > 0 && body) scored.push([s, src, title, body]);
    }
  }
  scored.sort((x, y) => y[0] - x[0]);
  if (!scored.length) return "No stored passage matches that question — " +
    "try asking about a check, pattern, risk or number the report mentions.";
  return "The most relevant passages from the research, verbatim:\n\n" +
    scored.slice(0, 2).map(([, src, t, b]) =>
      `[from the ${src} report — “${renameHeading(t)}”]\n${b.slice(0, 1500)}`)
    .join("\n\n");
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
  let list = null, table = null, quote = null, para = [], fence = null;
  const flushPara = () => {
    if (!para.length) return;
    const txt = para.join(" ");
    // the reports' legend for their ASCII bars — we draw real charts
    // instead, so swap the stale legend for one that matches the page
    out.push(/[█▒]/.test(txt)
      ? `<p><em>The same yearly figures the checks below judged — hover any bar for the exact value.</em></p>`
      : `<p>${inlineMd(txt)}</p>`);
    para = [];
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
    if (fence !== null) {                       // inside a ``` code fence
      if (/^```\s*$/.test(line)) { out.push(fencedBlock(fence, out)); fence = null; }
      else fence.push(raw);
      continue;
    }
    if (/^```/.test(line)) { flushAll(); fence = []; continue; }
    const h = line.match(/^(#{1,4})\s+(.*)$/);
    if (h) {
      flushAll();
      const lvl = h[1].length;
      out.push({ heading: true, lvl, text: h[2], html: inlineMd(h[2]) });
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
  if (fence !== null) out.push(fencedBlock(fence, out));   // unterminated fence
  // Fold the document into sections: heading levels >= collapseFrom become
  // collapsible <details>, CLOSED by default, each carrying its verdict in
  // the headline so the folded page still tells the story at a glance.
  return foldSections(out, collapseFrom || 2);
}

/* ---- fenced blocks: the reports draw yearly figures as ASCII bar charts
   (FY2006  █████  1,129). Rebuild those as REAL SVG charts; anything else
   stays a <pre> so nothing ever renders as mushed-together glyphs. ---- */

const ASCII_ROW_RE = /^FY(\d{4})\s+[█▒\s]*?(-?[\d,]+(?:\.\d+)?)\s*(%|days?|)(?:\s|$)/;

function fencedBlock(lines, out) {
  const rows = lines.filter(l => l.trim() !== "");
  const parsed = rows.map(l => l.match(ASCII_ROW_RE));
  if (rows.length >= 3 && parsed.every(Boolean)) {
    const labels = parsed.map(m => "FY" + m[1]);
    const values = parsed.map(m => parseFloat(m[2].replace(/,/g, "")));
    let unit = parsed[0][3] ? (parsed[0][3].startsWith("day") ? "days" : parsed[0][3]) : "";
    // caption = the bold intro line the report puts just above the block
    let title = "Yearly figures";
    const prev = out[out.length - 1];
    if (typeof prev === "string") {
      const m = prev.match(/^<p><strong>(.+?)<\/strong>\s*<\/p>$/);
      if (m) { title = m[1].replace(/<[^>]+>/g, ""); out.pop(); }
    }
    if (!unit && /₹|crore|\bcr\b/i.test(title)) unit = "₹ Cr";
    return chartSvg({ title, unit, kind: "bar" }, labels, values);
  }
  return `<pre class="mdcode">${esc(lines.join("\n"))}</pre>`;
}

/* ---- verdicts surfaced into the section headlines ---- */

const VERDICT_VOCAB = [
  ["STRONG FIT", "pos"], ["LIKELY FIT", "pos"], ["QUANT SIGNAL", "mid"],
  ["PARTIAL", "mid"], ["NO FIT", "neg"], ["NOT ASSESSED", "mid"],
  ["HIGH RISK", "neg"], ["ELEVATED", "neg"], ["QUANT FLAG", "mid"],
  ["WATCH", "warn"], ["NO SIGNAL", "pos"], ["LOW", "pos"],
  ["Excellent", "pos"], ["Outstanding", "pos"], ["Strong", "pos"],
  ["Good", "pos"], ["Decent", "mid"], ["Mixed", "mid"],
  ["Weak", "neg"], ["Poor", "neg"], ["Not rated", "mid"],
  ["IMPROVED", "pos"], ["DECLINED", "neg"], ["HELD STEADY", "mid"],
  // the index comparison — longest phrases first, so "LAGGED the index
  // badly" is never matched as the milder "LAGGED the index"
  ["GAINED STRONGLY on the index", "pos"], ["GAINED on the index", "pos"],
  ["MOVED WITH the index", "mid"],
  ["LAGGED the index badly", "neg"], ["LAGGED the index", "neg"],
];

function verdictBadge(fragment) {
  const t = fragment.trim().replace(/[★☆➡️📈📉⬜]/gu, "").trim();
  for (const [word, cls] of VERDICT_VOCAB) {
    if (t === word || t.startsWith(word + " ") || t.startsWith(word + ",")
        || t.endsWith(" " + word)) return { word, cls };
  }
  return null;
}

function classifyText(text) {
  for (const [word, cls] of VERDICT_VOCAB)
    if (text.includes(word)) return cls;
  return "mid";
}

const stripTags = s => String(s).replace(/<[^>]+>/g, "");

// "Section 1 — How good…", "Step 2 — Where…", "Bucket 3 — Risks…" →
// call each part by what it actually does, not by a number.
const renameHeading = t => t.replace(/^(Section|Step|Bucket)\s+\d+\s+—\s+/, "");

// Sections that describe internal machinery — never rendered on the site.
const HIDDEN_SECTION_RE = /^How this (report|comparison) was built/i;

const badgeHtml = (word, cls) => `<span class="vbadge ${cls}">${esc(word)}</span>`;

function childVerdictTally(nodes, i) {
  // Tally the verdicts of a section's own subsections ("Brand Strength —
  // STRONG FIT", "New Entrants — WATCH"…) so the folded headline says
  // what's well and what's not at a glance: "4 STRONG FIT · 1 NO FIT".
  const lvl = nodes[i].lvl;
  const counts = new Map();
  for (let j = i + 1; j < nodes.length; j++) {
    const n = nodes[j];
    if (!n || !n.heading) continue;
    if (n.lvl <= lvl) break;
    const parts = n.text.split(" — ");
    if (parts.length < 2) continue;
    const b = verdictBadge(parts[parts.length - 1]);
    if (b) counts.set(b.word, { cls: b.cls, n: (counts.get(b.word) || { n: 0 }).n + 1 });
  }
  if (!counts.size) return "";
  const sev = { neg: 0, warn: 1, mid: 2, pos: 3 };
  return [...counts.entries()]
    .sort((a, b) => sev[a[1].cls] - sev[b[1].cls])
    .map(([word, v]) => badgeHtml(`${v.n} ${word}`, v.cls)).join("");
}

function firstParagraph(nodes, i) {
  const lvl = nodes[i].lvl;
  for (let j = i + 1; j < nodes.length; j++) {
    const n = nodes[j];
    if (n && n.heading) { if (n.lvl <= lvl) break; continue; }
    if (typeof n === "string" && n.startsWith("<p>")) return stripTags(n).trim();
  }
  return "";
}

function summaryFor(nodes, i, titleText) {
  // Every folded headline must carry its verdict. In order of strength:
  // 1. verdict after a colon    "The overall rating: HELD STEADY …"
  // 2. verdict after " — "      "Brand Strength — STRONG FIT"
  // 3. tally of child verdicts  "4 STRONG FIT · 3 LIKELY FIT · 1 NO FIT"
  // 4. explicit counts / the section's own "Overall…" line, badged
  const colon = titleText.match(/^([^:]{3,60}):\s+(.+)$/);
  if (colon) {
    const b = verdictBadge(colon[2]);
    if (b) return { title: colon[1],
                    badge: badgeHtml(colon[2].replace(/[★☆➡️📈📉⬜]/gu, "").trim(), b.cls),
                    snippet: "" };
  }
  const parts = titleText.split(" — ");
  if (parts.length >= 2) {
    const b = verdictBadge(parts[parts.length - 1]);
    if (b) return { title: parts.slice(0, -1).join(" — "),
                    badge: badgeHtml(parts[parts.length - 1].trim(), b.cls),
                    snippet: "" };
  }
  const para = firstParagraph(nodes, i);
  let badge = childVerdictTally(nodes, i);
  let text = para.replace(/^Overall:?\s*/i, "").trim();
  if (text && !badge) {
    // pull the count claims forward ("fits 8 of the 11 patterns",
    // "2 improved, 3 regressed") so the verdict is explicit, not prose
    const fits = text.match(/fits (\d+) of the (\d+) patterns/);
    const moves = text.match(/(\d+) (improved|strengthened|eased), (\d+) (regressed|weakened|worsened)/);
    if (fits) badge = badgeHtml(`fits ${fits[1]} of ${fits[2]} patterns`,
                                +fits[1] > 0 ? "pos" : "neg");
    else if (moves) badge = badgeHtml(`▲ ${moves[1]} ${moves[2]}`, +moves[1] ? "pos" : "mid") +
                            badgeHtml(`▼ ${moves[3]} ${moves[4]}`, +moves[3] ? "neg" : "mid");
    else {
      // the index section states its verdict mid-sentence — "the company
      // has MOVED WITH the index — 54 out of 100" — so it never anchors to
      // the start or end of the paragraph the way the other verdicts do
      const rel = text.match(
        /the company has ([A-Z][A-Za-z ]+?) — (\d+) out of 100/);
      const b = verdictBadge(rel ? rel[1] : text);
      if (b) badge = badgeHtml(rel ? `${rel[1]} · ${rel[2]}/100` : b.word,
                               b.cls);
    }
  }
  if (text) {
    const cut = text.indexOf(". ");
    if (cut > 40) text = text.slice(0, cut + 1);
    if (text.length > 150) text = text.slice(0, 147) + "…";
  }
  return { title: titleText, badge,
           snippet: text ? `<span class="sum-note ${classifyText(text)}-t">${esc(text)}</span>` : "" };
}

function foldSections(nodes, collapseFrom) {
  let html = "", open = 0, hiddenBelow = null;
  for (let i = 0; i < nodes.length; i++) {
    const n = nodes[i];
    if (n && n.heading) {
      if (hiddenBelow !== null && n.lvl > hiddenBelow) continue;
      hiddenBelow = null;
      if (HIDDEN_SECTION_RE.test(n.text)) { hiddenBelow = n.lvl; continue; }
      const title = renameHeading(n.text);
      if (n.lvl >= collapseFrom) {
        while (open > 0 && open >= n.lvl - collapseFrom + 1) { html += "</details>"; open--; }
        const s = summaryFor(nodes, i, title);
        html += `<details class="mdsec lvl${n.lvl}"><summary><span class="sum-title">${inlineMd(s.title)}</span>${s.badge}${s.snippet}</summary>`;
        open++;
      } else {
        while (open > 0) { html += "</details>"; open--; }
        html += `<h${n.lvl + 1} class="mdh">${inlineMd(title)}</h${n.lvl + 1}>`;
      }
    } else {
      if (hiddenBelow !== null) continue;
      html += n;
    }
  }
  while (open > 0) { html += "</details>"; open--; }
  return html;
}

/* Reorder the report for display: the company verdict comes FIRST, before
   anything else; the leading H1 title is dropped (the hero already names
   the company). Pure string work on the stored MD — downloads untouched. */
function reorderReportMd(md) {
  const body = dropPreamble(md);
  const verdict = extractSection(body, /^The verdict/);
  if (!verdict) return body;
  return verdict + "\n\n" + body.replace(verdict, "");
}

// Everything before the first section heading (the H1 + any preamble that
// narrates how the report was produced) stays out of the page.
function dropPreamble(md) {
  const i = md.search(/^## /m);
  return i > 0 ? md.slice(i) : md.replace(/^#\s.*\n/, "");
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
    <p class="note">Yearly figures from the company's financial statements (₹ in crores) —
    hover any bar or point for the exact value.</p>
    <div class="charts">${figs.join("")}</div>`;
}

/* ---------------- company view: stored reports + charts + Q&A ---------------- */

/* ---------- the index comparison, from the stored reports ----------
   Everything here is parsed out of the same Markdown the download buttons
   hand over, so the page and the file can never disagree. */

const REL_COLORS = ["#2a78d6", "#1a9e5c", "#e07b00"];
const relCls = pct => pct == null ? "mid" : pct >= 10 ? "pos"
  : pct <= -10 ? "neg" : "mid";
const relVerdictCls = v => {
  const s = (v || "").toLowerCase();
  return s.includes("gained") ? "pos" : s.includes("lagged") ? "neg" : "mid";
};
const relPct = p => `${p >= 0 ? "+" : ""}${p}%`;

function relYoyChart(ratios) {
  const series = ratios.map((r, i) => ({
    label: r.label, color: REL_COLORS[i % REL_COLORS.length],
    pts: (r.levels || []).filter(l => l.yoy != null)
      .map(l => ({ fy: l.fy, v: l.yoy })),
  })).filter(s => s.pts.length > 1);
  if (!series.length) return "";
  const years = [...new Set(series.flatMap(s => s.pts.map(p => p.fy)))].sort();
  const vals = series.flatMap(s => s.pts.map(p => p.v)).concat([0]);
  let lo = Math.min(...vals), hi = Math.max(...vals);
  const pad = (hi - lo) * 0.12 || 1; lo -= pad; hi += pad;
  const W = 740, H = 300, L = 54, R = 14, T = 16, B = 40;
  const x = fy => years.length < 2 ? L + (W - L - R) / 2
    : L + years.indexOf(fy) * (W - L - R) / (years.length - 1);
  const y = v => T + (hi - v) * (H - T - B) / (hi - lo);
  const grid = [0, 1, 2, 3, 4].map(i => {
    const v = hi - (hi - lo) * i / 4;
    return `<line x1="${L}" y1="${y(v).toFixed(1)}" x2="${W - R}" y2="${y(v).toFixed(1)}"
      stroke="currentColor" stroke-opacity=".12"/>
      <text x="${L - 8}" y="${(y(v) + 4).toFixed(1)}" text-anchor="end" font-size="11"
        fill="currentColor" fill-opacity=".6">${v >= 0 ? "+" : ""}${v.toFixed(0)}%</text>`;
  }).join("");
  const zero = (lo < 0 && hi > 0)
    ? `<line x1="${L}" y1="${y(0).toFixed(1)}" x2="${W - R}" y2="${y(0).toFixed(1)}"
        stroke="currentColor" stroke-opacity=".45" stroke-dasharray="5 4"/>` : "";
  const xlab = years.map((fy, i) => (years.length > 9 && i % 2) ? "" :
    `<text x="${x(fy).toFixed(1)}" y="${H - B + 17}" text-anchor="middle" font-size="11"
       fill="currentColor" fill-opacity=".6">FY${String(fy).slice(2)}</text>`).join("");
  const lines = series.map(s =>
    `<polyline points="${s.pts.map(p => `${x(p.fy).toFixed(1)},${y(p.v).toFixed(1)}`).join(" ")}"
       fill="none" stroke="${s.color}" stroke-width="2.2"
       stroke-linejoin="round" stroke-linecap="round"/>` +
    s.pts.map(p => `<circle cx="${x(p.fy).toFixed(1)}" cy="${y(p.v).toFixed(1)}" r="3.4"
        fill="var(--surface-1,#fff)" stroke="${s.color}" stroke-width="2"><title>${esc(s.label)} · FY${p.fy} · ${p.v >= 0 ? "+" : ""}${p.v.toFixed(1)}%</title></circle>`).join("")
  ).join("");
  return `<figure class="rel-chart">
    <svg viewBox="0 0 ${W} ${H}" role="img" aria-label="Yearly change of each ratio against the index">
      ${grid}${zero}<line x1="${L}" y1="${H - B}" x2="${W - R}" y2="${H - B}"
        stroke="currentColor" stroke-opacity=".35"/>${xlab}${lines}</svg>
    <figcaption class="rel-legend">
      ${series.map(s => `<span class="rel-key"><i style="background:${s.color}"></i>${esc(s.label)}</span>`).join("")}
      <span class="note">above the dashed 0% line the company gained on the index that year</span>
    </figcaption></figure>`;
}

function relWindowTable(measures, rows) {
  if (!measures.length || !rows.length) return "";
  return `<div class="tblwrap"><table class="rel-table">
    <thead><tr><th>Window</th>${measures.map(m => `<th>${esc(m)}</th>`).join("")}</tr></thead>
    <tbody>${rows.map(r => `<tr>
      <th scope="row">last ${r.window} year${r.window > 1 ? "s" : ""}</th>
      ${measures.map(m => {
        const c = r.cells[m];
        if (!c || c.pct == null)
          return `<td class="note">${esc((c && c.word) || "not comparable")}</td>`;
        return `<td class="${relCls(c.pct)}">${relPct(c.pct)}<span class="note">${esc(c.word)}</span></td>`;
      }).join("")}</tr>`).join("")}</tbody></table></div>`;
}

function relRawTable(raw) {
  if (!raw || !raw.columns.length || !raw.rows.length) return "";
  return `<div class="tblwrap"><table class="rel-table raw">
    <thead><tr><th>Fiscal year</th>${raw.columns.map(c => `<th>${esc(c)}</th>`).join("")}</tr></thead>
    <tbody>${raw.rows.map(r => `<tr><th scope="row">FY${r.fy}</th>${
      r.values.map(v => `<td>${v == null ? "—" : esc(v)}</td>`).join("")}</tr>`).join("")}
    </tbody></table></div>`;
}

function relativeCard(rel) {
  const s = rel.section;
  if (!s) return "";
  // "Nifty 50" needs its article in prose; a generic fallback already has one
  const raw = rel.index || "index";
  const idx = /^the /i.test(raw) ? raw : `the ${raw}`;
  const head = `<h2>Against ${esc(idx)} — price and earnings</h2>`;
  if (!s.scored) {
    return `${head}<p class="note">The stored history is too short to compare
      this company with ${esc(idx)} over any window, so this pillar was left
      out of the rating rather than guessed.</p>`;
  }
  const cmp = rel.comparison || {};
  const w = rel.workup || {};
  const cov = s.coverage;
  return `${head}
    <p class="rel-verdict"><span class="vbadge ${relVerdictCls(s.verdict)}">${esc(s.verdict)}</span>
      <strong>${s.points} / 100</strong>
      ${cmp.recent_points != null ? `<span class="note">latest year on its own:
        ${esc(cmp.recent_verdict)} (${cmp.recent_points}/100)</span>` : ""}</p>
    <p class="note">${esc(s.note)} This is 10% of the overall rating.</p>
    <h3>The verdict over each window</h3>
    ${relWindowTable(s.measures, s.windows)}
    ${(w.ratios || []).length ? `<h3>How the three ratios moved, year by year</h3>
      ${relYoyChart(w.ratios)}` : ""}
    <details class="mod">
      <summary><strong>How this pillar was scored</strong>
        <span class="note">every window, and what it was worth</span></summary>
      ${cov ? `<p class="note calc">Across ${cov.answered} of ${cov.possible}
        measure-and-window pairs the stored data could answer, the company scored
        ${cov.mean >= 0 ? "+" : ""}${cov.mean} on the −2 (lagged badly) to +2
        (gained strongly) scale; mapped onto 0–100 that is ${s.points} points.</p>` : ""}
      <p class="note">A ratio change of +25% or more scores +2, +10% to +25% scores
        +1, inside ±10% scores 0, −10% to −25% scores −1, and −25% or worse scores −2.
        A window whose ratio crosses zero has no honest percentage, so it is left out
        rather than guessed.</p>
    </details>
    ${(w.ratios || []).length ? `<details class="mod">
      <summary><strong>Each ratio in full</strong>
        <span class="note">its level every year and the change over every window</span></summary>
      ${w.ratios.map(r => `<h4>${esc(r.label)}</h4>
        <p class="note">${esc(r.description)}${r.verdict
          ? ` — <strong>${esc(r.verdict)}</strong>, ${r.change_pct >= 0 ? "+" : ""}${r.change_pct}%
              from FY${r.from_fy} to FY${r.to_fy}.` : "."}</p>
        ${r.unavailable
          ? `<p class="note">${esc(r.unavailable)} — this measure was left out
             of the score rather than guessed.</p>`
          : `<div class="tblwrap"><table class="rel-table"><thead><tr>
          <th>Window</th><th>From</th><th>To</th><th>Change</th></tr></thead>
          <tbody>${r.windows.map(x => `<tr><th scope="row">last ${x.window} year${x.window > 1 ? "s" : ""}</th>
            <td>${esc(x.from)}</td><td>${esc(x.to)}</td>
            <td class="${relCls(x.pct)}">${esc(x.text)}</td></tr>`).join("")}</tbody>
        </table></div>`}`).join("")}
    </details>` : ""}
    ${relRawTable(w.raw) ? `<details class="mod">
      <summary><strong>The raw numbers behind every ratio</strong>
        <span class="note">company and index, side by side, year by year</span></summary>
      ${relRawTable(w.raw)}
    </details>` : ""}`;
}

async function renderCompany(sym) {
  const co = state.data.companies[sym];
  if (co && !co.analysed) {
    return card(`<h2>${esc(co.name)} <span class="sym">${sym}</span></h2>
      <p>This company is <strong>not covered yet</strong> —
      ${state.data.n_analysed} of ${state.data.n} companies are covered today.
      Try “top 20 companies” for covered picks.</p>`);
  }
  const ph = document.createElement("div");
  ph.className = "card";
  ph.innerHTML = `<p>⚡ Opening <strong>${esc(sym)}</strong>…</p>`;
  $out().appendChild(ph);
  let a, c, ch, rel;
  try {
    [a, c, ch, rel] = await Promise.all([
      fetchAnalysis(sym),
      fetchComparison(sym),
      fetchCharts(sym).catch(() => null),
      fetchRelative(sym).catch(() => null),
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
  // THE VERDICT FIRST: hero card leads with the rating before anything else.
  const breath = (a.md.match(/In one breath:\s*([^\n]+)/) || [])[1] || "";
  const gradeCls = { pos: "", neg: "neg", mid: "mid" }[GRADE_CLS[a.grade] || "mid"];
  cardIn(main, `
    <div class="hero-inner">
    <div class="co-head"><span class="nm">${esc(a.name)}</span>
      <span class="sym">${sym}</span>
      ${a.industry ? `<span class="tag">${esc(a.industry)}</span>` : ""}
      ${co && co.rank ? `<span class="tag">🏅 rank ${co.rank} of ${state.data.n_analysed}</span>` : ""}</div>
    <div class="verdict-line">
      <span class="grade-pill ${gradeCls}">${esc(a.grade || "Not rated")}
        ${a.score != null ? `<span class="score">${a.score} / 100</span>` : ""}</span>
      <span class="dir-chip ${dir.cls}">${dir.icon} ${esc((c.direction || "not comparable"))} over the last year</span>
    </div>
    ${breath ? `<p class="one-breath">${esc(breath)}</p>` : ""}
    <div class="facts">
      <div class="fact"><div class="v">₹${fmtCr(a.market.mcap)}</div><div class="k">Market cap</div></div>
      <div class="fact"><div class="v">${a.market.pe ?? "—"}</div><div class="k">P/E</div></div>
      <div class="fact"><div class="v">₹${a.market.price ? a.market.price.toLocaleString("en-IN") : "—"}</div><div class="k">Price</div></div>
    </div>
    <p class="note"><a class="chip" id="dl-${sym}" href="${reportHref(sym, "analysis")}" download="${sym}_analysis.md">📄 Full report (Markdown)</a>
      <a class="chip" id="dlc-${sym}" href="${reportHref(sym, "comparison")}" download="${sym}_comparison.md">📄 One-year comparison (Markdown)</a>
      ${rel && rel.has_workup ? `<a class="chip" id="dlr-${sym}" href="${reportHref(sym, "stock_to_index")}" download="${sym}_stock_to_index.md">📄 Index comparison (Markdown)</a>` : ""}</p>
    </div>`, "hero");

  if (ch) cardIn(main, chartsCard(ch));
  if (rel) { const rc = relativeCard(rel); if (rc) cardIn(main, rc); }

  cardIn(main, `<h2>The research</h2>
    <p class="note">Every check, pattern and risk with its why — folded, verdicts in the
    headlines. Click any headline to open it.</p>
    <div class="mdreport">${mdToHtml(reorderReportMd(a.md), 2)}</div>`);

  cardIn(aside, `<h2>Momentum — the last one year</h2>
    <div class="scoreline"><span class="big-score ${dir.cls}" style="font-size:20px">${dir.icon} ${esc((c.direction || "not comparable").toUpperCase())}</span>
      <span class="cov">vs the long-term picture</span></div>
    <div class="mdreport">${mdToHtml(dropPreamble(c.md), 2)}</div>`);

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

async function pollJob(kind, id, onTick) {
  let misses = 0;
  for (;;) {
    await new Promise(r => setTimeout(r, 2500));
    let j = null;
    try {
      const r = await fetch(`api/jobs/${kind}/${id}`);
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

// Answers arrive as light markdown at worst — render them clean:
// escaped, bold converted, bullets kept, never a raw asterisk on screen.
function qaHtml(answer) {
  const lines = String(answer).split(/\n/);
  const out = [];
  let list = null;
  for (const raw of lines) {
    const line = raw.trim();
    if (/^[-*•]\s+/.test(line)) {
      list = list || [];
      list.push(`<li>${inlineMd(line.replace(/^[-*•]\s+/, ""))}</li>`);
      continue;
    }
    if (list) { out.push(`<ul>${list.join("")}</ul>`); list = null; }
    if (line === "") continue;
    out.push(`<p>${inlineMd(line.replace(/^#+\s*/, ""))}</p>`);
  }
  if (list) out.push(`<ul>${list.join("")}</ul>`);
  return out.join("").replace(/\*\*/g, "");
}

async function askReports(sym, question, outEl) {
  outEl.insertAdjacentHTML("beforeend",
    `<div class="qa-q">Q: ${esc(question)}</div>
     <div class="qa-a note">Answering from the stored reports…</div>`);
  const slot = outEl.lastElementChild;
  if (STATIC) {
    try {
      const { a, c } = await loadReports(sym);
      slot.className = "qa-a";
      slot.innerHTML = qaHtml(extractiveAnswer(question, a, c));
    } catch (e) {
      slot.textContent = "Failed: " + (e.message || e);
    }
    return;
  }
  try {
    const res = await fetch(`api/jobs/ask/${sym}`, {
      method: "POST", headers: { "content-type": "application/json" },
      body: JSON.stringify({ question }),
    });
    if (!res.ok) throw new Error((await res.json()).detail || res.status);
    const { job } = await res.json();
    const data = await pollJob("ask", job.split(":")[1],
      t => { slot.textContent = `Answering from the stored reports — ${fmtElapsed(t)}…`; });
    slot.className = "qa-a";
    slot.innerHTML = qaHtml(data.answer);
  } catch (e) {
    slot.textContent = "Failed: " + (e.message || e);
  }
}

/* ---------------- rankings with drill-down ---------------- */

async function renderRanking(n, order, industry) {
  let data;
  try {
    data = await fetchRanking(n, order, industry);
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
    <p class="note">Ranked by the stored 0–100 rating (business quality 40.5% +
    multibagger fit 27% + risk safety 22.5% + how it has done against the Nifty 50 10%;
    a company the index comparison cannot reach keeps the original 45/30/25 split)
    over the ${state.data.n_analysed} analysed companies.
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
      <p><strong>${missing.map(esc).join(" and ")}</strong> ${missing.length > 1 ? "are" : "is"}
      not covered yet — ${state.data.n_analysed} of ${state.data.n} companies are covered today,
      and comparing needs both. Try “top 20 companies” for covered picks.</p>`);
  }
  let a1, a2, c1, c2;
  try {
    [a1, a2, c1, c2] = await Promise.all([
      fetchAnalysis(s1), fetchAnalysis(s2),
      fetchComparison(s1).catch(() => null),
      fetchComparison(s2).catch(() => null),
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


/* ---------------- Darvas weekly screen (the box method) ----------------
   Rendered from api/darvas/latest — the SAME machine-readable record the
   Markdown report was written from, so this page and the downloadable
   report can never disagree. The trace comes from the archived runs; the
   "run" button starts the real engine on the server and polls a status
   endpoint (every request returns in milliseconds, so a long fetch can
   never time out at a proxy). */
const DARVAS_QUICK = 1;   // this UI's run mode (1 = no AI call-read)
const inrFmt = v => (v === null || v === undefined || v === "")
  ? "—" : "₹" + Number(v).toLocaleString("en-IN", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const verbTag = (v) => {
  const cls = { BUY: "buy", ACCUMULATE: "buy", SELL: "sell", "RAISE STOP": "raise", WATCH: "watch" }[v] || "watch";
  return `<span class="verb ${cls}">${esc(v)}</span>`;
};

async function renderDarvas() {
  const holder = document.createElement("div");
  $out().appendChild(holder);
  cardIn(holder, `<h2>📦 Darvas weekly screen</h2><p class="note">Loading the latest run…</p>`);
  let rec = null, tr = null, st = null;
  try {
    const r = await fetch("api/darvas/latest");
    rec = r.ok ? await r.json() : null;
    tr = await fetch("api/darvas/trace?days=31").then(x => x.json());
    st = await fetch("api/darvas/run/status").then(x => x.json());
  } catch (e) {
    holder.innerHTML = "";
    cardIn(holder, `<h2>📦 Darvas weekly screen</h2><p class="note">Could not load the screen: ${esc(e.message)}</p>`);
    return;
  }
  holder.innerHTML = "";
  darvasRender(holder, rec, tr, st);
}

function darvasRender(holder, rec, tr, st) {
  // ---- header + the run button
  const running = st && st.state === "running";
  cardIn(holder, `
    <h2>📦 Darvas weekly screen</h2>
    <p>The box method, run mechanically over the NiftyTotalMarket universe: a weekly
    volume surge with the price rising is the trigger, the stock's own boxes give the
    entry and the stop, and every held stop only ever moves up. The universe is
    checked against the official constituent list every month.</p>
    ${rec ? `<p class="note">Latest run <b>${esc(rec.run_date)}</b> on data fetched ${esc(rec.fetched_at)} ·
      ${rec.scanned} stocks scanned (${rec.fetch_ok} fetched, ${rec.fetch_failed} unavailable) ·
      ${rec.weekly_qualifiers ?? "—"} weekly qualifiers → ${rec.fully_qualified ?? "—"} through all three gates
      ${rec.ai_used ? "· conference-call read by the judge model" : "· no AI call in this run"}</p>`
      : `<p class="note">No run stored yet — press the button to run the screen.</p>`}
    <p><button class="chip" id="darvas-run" ${running ? "disabled" : ""}>▶ Run this week's screen now</button>
       <a class="chip" href="api/darvas/report" download="DARVAS_REPORT.md">📄 Download the full report (Markdown)</a></p>
    <p class="note darvas-status" id="darvas-status">${running ? "A run is in progress…" : ""}</p>`);
  const btn = holder.querySelector("#darvas-run");
  btn.addEventListener("click", () => darvasStartRun(holder));
  if (running) darvasPoll(holder);
  if (!rec) return;

  // ---- the week in four verbs
  const a = rec.actions || {};
  const buyRows = (a.buys || []).map(b => `<tr><td>${verbTag(b.action || "BUY")} <b>${esc(b.symbol)}</b></td>
      <td>${esc(b.entry)}</td><td>${inrFmt(b.stop_loss)}</td>
      <td>${b.risk_pct == null ? "—" : (b.risk_pct.toFixed(1) + "%")}${b.wide ? ' <span class="verb sell">WIDE — half slice or wait for the next box</span>' : ""}</td></tr>`).join("");
  cardIn(holder, `
    <h2>Today's actions — plain and simple</h2>
    <h3>BUY <span class="note">(stop as a GTT order right after the fill; one equal slice — a tenth of capital)</span></h3>
    ${buyRows ? `<div class="tblwrap tablewrap"><table class="rank"><thead><tr><th>Stock</th><th>Entry</th><th>Stop loss</th><th>Risk from last close</th></tr></thead><tbody>${buyRows}</tbody></table></div>`
              : `<p class="note">Nothing to buy today.</p>`}
    <h3>RAISE STOP LOSS <span class="note">(replace the standing GTT — stops only move up)</span></h3>
    ${(a.raises || []).length ? `<ul>${a.raises.map(r => `<li>${verbTag("RAISE STOP")} <b>${esc(r.symbol)}</b>: ${inrFmt(r.old)} → <b>${inrFmt(r.new)}</b></li>`).join("")}</ul>` : `<p class="note">None this run.</p>`}
    <h3>SELL <span class="note">(closed below its box bottom — the red flag; only if you hold it)</span></h3>
    ${(a.sells || []).length ? `<ul>${a.sells.map(s => `<li>${verbTag("SELL")} <b>${esc(s.symbol)}</b></li>`).join("")}</ul>` : `<p class="note">Nothing flagged.</p>`}
    <h3>NOTHING TO DO — the radar <span class="note">(converts to BUY by itself in a coming week if the break comes; unbought old signals expire)</span></h3>
    <ul>${(a.radar || []).map(w => `<li>${verbTag("WATCH")} <b>${esc(w.symbol)}</b>${w.buy_above ? ` — turns into BUY on a daily close above ${inrFmt(w.buy_above)}` : ""}</li>`).join("")}
        ${(a.downgraded || []).map(d => `<li>${verbTag("WATCH")} <b>${esc(d.symbol)}</b> — ${esc(d.why)}</li>`).join("")}
        ${!(a.radar || []).length && !(a.downgraded || []).length ? "<li>(empty)</li>" : ""}</ul>`);

  // ---- the recommendations table (mirrors the report's)
  const recRows = (rec.recommendations || []).map(r => `<tr>
      <td><b>${esc(r.symbol)}</b></td><td>${verbTag(r.action)}${r.downgraded ? ' <span class="note">downgraded</span>' : ""}</td>
      <td>${r.box_top ? `${inrFmt(r.box_bottom)} – ${inrFmt(r.box_top)}` : "forming"}</td>
      <td>${r.box_range_pct != null ? r.box_range_pct.toFixed(1) + "%" : "—"}</td>
      <td>${r.action === "SELL" ? "exit" : inrFmt(r.stop_loss)}</td>
      <td>${esc(r.volume_trend || "—")}</td><td>${esc(r.earnings_power || "—")}</td><td>${esc(r.new_age || "—")}</td></tr>`).join("");
  cardIn(holder, `<h2>The recommendations</h2>
    <div class="tblwrap tablewrap"><table class="rank"><thead><tr><th>Stock</th><th>Action</th><th>Box (₹)</th><th>Own box height</th><th>Stop loss</th><th>Volume trend</th><th>Earnings power</th><th>New-age</th></tr></thead>
    <tbody>${recRows}</tbody></table></div>
    <p class="note">Every row has its full deep dive — price-and-volume chart, the complete box ladder, earnings power, the monthly volume trend — in the downloadable report.</p>`);

  // ---- the trace: every run's verbs, and every symbol's timeline
  const ev = (tr && tr.timeline) || [];
  const runs = (tr && tr.runs) || [];
  const evRows = ev.slice().reverse().map(e => `<tr><td>${esc(e.date)}</td><td><b>${esc(e.symbol)}</b></td><td>${verbTag(e.event)}</td><td>${esc(e.detail)}</td></tr>`).join("");
  cardIn(holder, `<h2>The trace — the last ${tr ? tr.days : 31} days, run by run</h2>
    <p class="note">${runs.length} run${runs.length === 1 ? "" : "s"} archived: ${runs.map(r => esc(r.run_date) + (r.source === "backfill" ? " (reconstructed)" : "")).join(" · ") || "none yet"}.
      Every BUY with its stop, every RAISE STOP with the old and new level, every SELL, and each symbol's first appearance on the radar — newest first.</p>
    ${evRows ? `<div class="tblwrap tablewrap"><table class="rank"><thead><tr><th>Date</th><th>Stock</th><th>Event</th><th>Detail</th></tr></thead><tbody>${evRows}</tbody></table></div>` : `<p class="note">No events yet.</p>`}`);
}

async function darvasStartRun(holder) {
  const status = holder.querySelector("#darvas-status");
  const btn = holder.querySelector("#darvas-run");
  btn.disabled = true;
  status.textContent = "Starting the weekly engine…";
  try {
    const r = await fetch(`api/darvas/run?quick=${DARVAS_QUICK}`, { method: "POST" });
    const j = await r.json();
    if (!j.started && j.state !== "running") { status.textContent = j.note || "Could not start"; btn.disabled = false; return; }
  } catch (e) { status.textContent = "Could not start: " + e.message; btn.disabled = false; return; }
  darvasPoll(holder);
}

async function darvasPoll(holder) {
  const status = holder.querySelector("#darvas-status");
  const t0 = Date.now();
  const tick = async () => {
    let st;
    try { st = await fetch("api/darvas/run/status").then(r => r.json()); }
    catch (_) { setTimeout(tick, 5000); return; }
    const secs = Math.round((Date.now() - t0) / 1000);
    if (st.state === "running") {
      const tail = (st.log_tail || "").split("\n").filter(Boolean).slice(-1)[0] || "";
      status.textContent = `Running the full engine — fresh universe check, price fetch, three gates, boxes, stops… ${fmtElapsedD(secs)} elapsed. ${tail}`;
      setTimeout(tick, 5000);
      return;
    }
    if (st.state === "done") {
      status.textContent = "Done — reloading the new recommendations…";
      holder.innerHTML = "";
      const rec = await fetch("api/darvas/latest").then(r => r.ok ? r.json() : null);
      const tr = await fetch("api/darvas/trace?days=31").then(r => r.json());
      darvasRender(holder, rec, tr, st);
      return;
    }
    status.textContent = "The run failed: " + (st.error || "unknown") + (st.log_tail ? " — " + st.log_tail.split("\n").slice(-1)[0] : "");
    const btn = holder.querySelector("#darvas-run"); if (btn) btn.disabled = false;
  };
  tick();
}
const fmtElapsedD = s => s < 60 ? `${s}s` : `${Math.floor(s / 60)}m ${String(s % 60).padStart(2, "0")}s`;
