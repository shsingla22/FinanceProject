"""Interactive HTML versions of Charts 1-4, built with Chart.js.

Why Chart.js (not Plotly):
- ~200 KB embedded vs ~4.7 MB for Plotly inline.
- Renders reliably from `file://` in Safari, Chrome and Firefox without
  network access or strict-mode blocking.
- The two requested controls — line enable/disable and a custom year
  window — are wired up explicitly with native HTML controls (checkboxes,
  buttons, range sliders) so they work even if a JS framework feature
  silently regresses.

Each `*_interactive.html` is fully self-contained:
  - Chart.js library is inlined.
  - Data is inlined as a JSON literal.
  - Controls are plain `<input>` and `<button>` elements wired with a
    small inline `<script>`.
"""

from __future__ import annotations
import json
import os

import pandas as pd

from plot_inr_usd  import build_dataset as build_inr
from plot_indices  import build_dataset as build_indices
from plot_medians  import build_dataset as build_medians
from plot_combined import build_dataset as build_combined

HERE = os.path.dirname(os.path.abspath(__file__))
VENDOR_JS = os.path.join(HERE, ".cache", "vendor", "chart.umd.min.js")
YEARS_BACK = 25

# Standard colour scheme reused from the matplotlib charts
C_INR = "#d62728"
C_50  = "#1f77b4"
C_MID = "#2ca02c"
C_SM  = "#ff7f0e"
C_FII = "#8c564b"


def _chartjs_source() -> str:
    if not os.path.exists(VENDOR_JS):
        raise FileNotFoundError(
            f"Chart.js bundle missing at {VENDOR_JS}. Run "
            "`curl -sL https://cdn.jsdelivr.net/npm/chart.js@4.4.4/dist/"
            "chart.umd.min.js -o .cache/vendor/chart.umd.min.js`."
        )
    with open(VENDOR_JS) as f:
        return f.read()


def _series_to_xy(values: pd.Series) -> list[dict]:
    """Convert a year-indexed Series to [{x:int, y:float|null}, ...]."""
    out = []
    for yr, v in values.items():
        out.append({"x": int(yr),
                    "y": None if pd.isna(v) else float(v)})
    return out


_HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>__TITLE__</title>
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  *,*::before,*::after { box-sizing: border-box; }
  html,body { margin:0; padding:0; font-family: -apple-system,BlinkMacSystemFont,
      "Segoe UI",Roboto,Helvetica,Arial,sans-serif; color:#222; background:#fff; }
  body { padding: 16px 22px; }
  h1 { font-size: 18px; margin: 0 0 12px 0; font-weight: 600; }

  .controls { display:flex; flex-wrap:wrap; gap:18px; align-items:flex-start;
    margin-bottom: 14px; padding: 12px 14px; background:#f6f8fa;
    border:1px solid #e5e7eb; border-radius:6px; }
  .control-block { display:flex; flex-direction:column; gap:6px;
    min-width:200px; }
  .control-block > label { font-size:12px; font-weight:600;
    text-transform:uppercase; color:#555; letter-spacing:.05em; }
  .toggle-list { display:flex; flex-direction:column; gap:4px; }
  .toggle-list label { font-size:13px; cursor:pointer; user-select:none;
    display:flex; align-items:center; gap:8px; }
  .toggle-list input[type="checkbox"] { width:14px; height:14px; cursor:pointer; }
  .swatch { display:inline-block; width:14px; height:14px; border-radius:3px;
    border:1px solid #ccc; }

  .preset-row, .range-row { display:flex; gap:6px; flex-wrap:wrap;
    align-items:center; }
  .preset-row button, #resetBtn { font-size:12px; padding:5px 10px;
    border:1px solid #c2c8d0; background:#fff; border-radius:4px;
    cursor:pointer; color:#222; }
  .preset-row button:hover, #resetBtn:hover { background:#eef1f5; }
  .preset-row button.active { background:#1f77b4; color:#fff;
    border-color:#1f77b4; }

  .range-row { gap:10px; }
  .range-row label { font-size:12px; min-width:36px; }
  .range-row input[type="number"] { width:70px; padding:3px 5px;
    font-size:13px; }
  .range-row input[type="range"] { flex:1; min-width:140px; }

  .chart-wrap { width:100%; height:640px; min-height:520px;
    background:#fff; border:1px solid #e5e7eb; border-radius:6px;
    padding:8px; }
  @media (min-width:1100px) { .chart-wrap { height:720px; } }

  .footnote { font-size:11px; color:#666; margin-top:10px; }
</style>
</head>
<body>
<h1>__TITLE__</h1>
<div class="controls">
  <div class="control-block">
    <label>Lines (click to toggle)</label>
    <div class="toggle-list" id="lineToggles"></div>
  </div>
  <div class="control-block">
    <label>Quick year window</label>
    <div class="preset-row" id="presetRow">
      <button data-years="5">Last 5y</button>
      <button data-years="10">Last 10y</button>
      <button data-years="15">Last 15y</button>
      <button data-years="25">Last 25y</button>
      <button data-years="all" class="active">All</button>
    </div>
  </div>
  <div class="control-block" style="flex:1; min-width:280px;">
    <label>Custom year range</label>
    <div class="range-row">
      <label>From</label>
      <input type="number" id="fromYear">
      <input type="range"  id="fromSlider">
    </div>
    <div class="range-row">
      <label>To</label>
      <input type="number" id="toYear">
      <input type="range"  id="toSlider">
    </div>
    <div class="range-row" style="justify-content:flex-end;">
      <button id="resetBtn">Reset</button>
    </div>
  </div>
</div>

<div class="chart-wrap"><canvas id="chart"></canvas></div>
<div class="footnote">__FOOTNOTE__</div>

<script>__CHARTJS__</script>
<script>
(function () {
  const PAYLOAD = __PAYLOAD__;
  const yearsAll = PAYLOAD.years;
  const yMin = Math.min(...yearsAll);
  const yMax = Math.max(...yearsAll);

  // Build Chart.js datasets
  const datasets = PAYLOAD.series.map(function (s) {
    const data = yearsAll.map(function (yr) {
      const pt = s.points.find(function (p) { return p.x === yr; });
      return pt ? pt.y : null;
    });
    const ds = {
      label: s.label,
      data: data,
      borderColor: s.color,
      backgroundColor: s.color,
      borderWidth: s.width || 2,
      borderDash: s.dash || [],
      pointRadius: 4,
      pointHoverRadius: 6,
      tension: 0.0,
      spanGaps: true,
      yAxisID: s.yAxis || 'y',
    };
    return ds;
  });

  // Build scales
  const scales = {
    x: {
      type: 'linear',
      title: { display: true, text: 'Year' },
      ticks: { stepSize: 1, callback: function (v) { return Math.round(v); } },
      min: yMin,
      max: yMax,
    },
  };
  PAYLOAD.axes.forEach(function (ax) {
    scales[ax.id] = {
      type: 'linear',
      position: ax.position || 'left',
      title: { display: true, text: ax.title, color: ax.color || '#444' },
      ticks: { color: ax.color || '#444' },
      grid: { drawOnChartArea: ax.id === 'y' },
    };
  });

  const ctx = document.getElementById('chart').getContext('2d');
  const chart = new Chart(ctx, {
    type: 'line',
    data: { labels: yearsAll, datasets: datasets },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      interaction: { mode: 'index', intersect: false },
      plugins: {
        legend: {
          display: true,
          position: 'top',
          align: 'start',
          labels: { boxWidth: 14, font: { size: 11 } },
          onClick: function (e, legendItem, legend) {
            // Default behaviour + sync our checkboxes
            const idx = legendItem.datasetIndex;
            const visible = legend.chart.isDatasetVisible(idx);
            legend.chart.setDatasetVisibility(idx, !visible);
            legend.chart.update();
            const cb = document.querySelector(
              'input[data-idx="' + idx + '"]');
            if (cb) cb.checked = !visible;
          },
        },
        tooltip: { mode: 'index', intersect: false },
      },
      scales: scales,
    },
  });

  // ---------- line toggle checkboxes ----------
  const togglesEl = document.getElementById('lineToggles');
  datasets.forEach(function (ds, idx) {
    const wrap = document.createElement('label');
    const cb = document.createElement('input');
    cb.type = 'checkbox';
    cb.checked = true;
    cb.dataset.idx = idx;
    cb.addEventListener('change', function () {
      chart.setDatasetVisibility(idx, cb.checked);
      chart.update();
    });
    const sw = document.createElement('span');
    sw.className = 'swatch';
    sw.style.background = ds.borderColor;
    const txt = document.createElement('span');
    txt.textContent = ds.label;
    wrap.appendChild(cb); wrap.appendChild(sw); wrap.appendChild(txt);
    togglesEl.appendChild(wrap);
  });

  // ---------- year window controls ----------
  const fromInput = document.getElementById('fromYear');
  const toInput   = document.getElementById('toYear');
  const fromSlider = document.getElementById('fromSlider');
  const toSlider   = document.getElementById('toSlider');

  [fromInput, fromSlider, toInput, toSlider].forEach(function (el) {
    el.min = yMin; el.max = yMax;
  });
  fromInput.value = fromSlider.value = yMin;
  toInput.value   = toSlider.value   = yMax;

  function setWindow(lo, hi) {
    lo = Math.max(yMin, Math.min(yMax, parseInt(lo, 10)));
    hi = Math.max(yMin, Math.min(yMax, parseInt(hi, 10)));
    if (lo > hi) { const t = lo; lo = hi; hi = t; }
    fromInput.value = fromSlider.value = lo;
    toInput.value   = toSlider.value   = hi;
    chart.options.scales.x.min = lo;
    chart.options.scales.x.max = hi;
    chart.update('none');
  }

  fromInput.addEventListener('change', function () {
    setWindow(fromInput.value, toInput.value); clearActivePreset();
  });
  toInput.addEventListener('change', function () {
    setWindow(fromInput.value, toInput.value); clearActivePreset();
  });
  fromSlider.addEventListener('input', function () {
    setWindow(fromSlider.value, toInput.value); clearActivePreset();
  });
  toSlider.addEventListener('input', function () {
    setWindow(fromInput.value, toSlider.value); clearActivePreset();
  });

  // ---------- preset buttons ----------
  const presetRow = document.getElementById('presetRow');
  function clearActivePreset() {
    presetRow.querySelectorAll('button').forEach(function (b) {
      b.classList.remove('active');
    });
  }
  presetRow.addEventListener('click', function (e) {
    const btn = e.target.closest('button');
    if (!btn) return;
    clearActivePreset();
    btn.classList.add('active');
    const yearsAttr = btn.dataset.years;
    if (yearsAttr === 'all') {
      setWindow(yMin, yMax);
      clearActivePreset(); btn.classList.add('active');
    } else {
      const n = parseInt(yearsAttr, 10);
      const lo = Math.max(yMin, yMax - n + 1);
      setWindow(lo, yMax);
      clearActivePreset(); btn.classList.add('active');
    }
  });

  // ---------- reset ----------
  document.getElementById('resetBtn').addEventListener('click', function () {
    setWindow(yMin, yMax);
    clearActivePreset();
    presetRow.querySelector('button[data-years="all"]').classList.add('active');
    datasets.forEach(function (_, idx) {
      chart.setDatasetVisibility(idx, true);
    });
    document.querySelectorAll('#lineToggles input').forEach(function (cb) {
      cb.checked = true;
    });
    chart.update();
  });
})();
</script>
</body>
</html>
"""


def _render(out_path: str, title: str, years: list[int],
            series: list[dict], axes: list[dict],
            footnote: str = "") -> str:
    payload = {
        "years":  years,
        "series": series,
        "axes":   axes,
    }
    html = (_HTML_TEMPLATE
            .replace("__TITLE__", title)
            .replace("__FOOTNOTE__", footnote)
            .replace("__CHARTJS__", _chartjs_source())
            .replace("__PAYLOAD__", json.dumps(payload)))
    with open(out_path, "w") as f:
        f.write(html)
    print(f"Saved: {out_path}  ({os.path.getsize(out_path) // 1024} KB)")
    return out_path


# -- Chart 1 --------------------------------------------------------------
def render_inr_usd(out: str | None = None) -> str:
    out = out or os.path.join(HERE, "inr_vs_usd_interactive.html")
    df = build_inr(YEARS_BACK)
    years = [int(y) for y in df.index]
    series = [{
        "label": "INR per 1 USD (year-end)",
        "color": C_INR, "width": 2.6,
        "yAxis": "y",
        "points": _series_to_xy(df["inr_per_usd"]),
    }]
    axes = [{"id": "y", "title": "INR per 1 USD",
             "color": C_INR, "position": "left"}]
    return _render(
        out, "Indian Rupee vs US Dollar (last 25 years, year-end close)",
        years, series, axes,
    )


# -- Chart 2 --------------------------------------------------------------
def render_indices(out: str | None = None) -> str:
    out = out or os.path.join(HERE, "nifty_indices_interactive.html")
    df = build_indices(YEARS_BACK)
    years = [int(y) for y in df.index]
    series = [
        {"label": "Nifty 50",
         "color": C_50, "width": 2.4,
         "points": _series_to_xy(df["nifty50"])},
        {"label": "Nifty Midcap 100",
         "color": C_MID, "width": 2.4,
         "points": _series_to_xy(df["nifty_midcap"])},
        {"label": "Nifty/BSE Smallcap",
         "color": C_SM, "width": 2.4,
         "points": _series_to_xy(df["nifty_smallcap"])},
    ]
    axes = [{"id": "y", "title": "Index level (year-end close)",
             "color": "#222", "position": "left"}]
    return _render(
        out, "Nifty 50 / Midcap 100 / Smallcap Yearly Close (last 25 years)",
        years, series, axes,
    )


# -- Chart 3 --------------------------------------------------------------
def render_medians(out: str | None = None) -> str:
    out = out or os.path.join(HERE, "constituent_medians_interactive.html")
    df = build_medians(YEARS_BACK)
    years = [int(y) for y in df.index]
    series = [
        {"label": "Nifty 50 — median constituent close",
         "color": C_50, "width": 2.0,
         "points": _series_to_xy(df["nifty50_median"])},
        {"label": "Nifty Midcap 100 — median constituent close",
         "color": C_MID, "width": 2.0,
         "points": _series_to_xy(df["midcap_median"])},
        {"label": "Nifty Smallcap 100 — median constituent close",
         "color": C_SM, "width": 2.0,
         "points": _series_to_xy(df["smallcap_median"])},
    ]
    axes = [{"id": "y", "title": "Median constituent close (INR)",
             "color": "#444", "position": "left"}]
    return _render(
        out, "Median Year-End Constituent Price: Nifty 50 / Midcap / "
             "Smallcap (last 25 years)",
        years, series, axes,
    )


# -- Chart 4: combined, multi-axis ---------------------------------------
def render_combined(out: str | None = None) -> str:
    out = out or os.path.join(HERE, "combined_all_interactive.html")
    df = build_combined(YEARS_BACK)
    years = [int(y) for y in df.index]
    series = [
        # left axis (yINR)
        {"label": "INR per 1 USD",
         "color": C_INR, "width": 2.8, "yAxis": "yINR",
         "points": _series_to_xy(df["inr_per_usd"])},
        # right #1 (yMed) — dashed
        {"label": "Nifty 50 — median constituent close",
         "color": C_50,  "width": 1.8, "yAxis": "yMed",
         "dash": [6, 4],
         "points": _series_to_xy(df["nifty50_median"])},
        {"label": "Nifty Midcap 100 — median constituent close",
         "color": C_MID, "width": 1.8, "yAxis": "yMed",
         "dash": [6, 4],
         "points": _series_to_xy(df["midcap_median"])},
        {"label": "Nifty Smallcap 100 — median constituent close",
         "color": C_SM,  "width": 1.8, "yAxis": "yMed",
         "dash": [6, 4],
         "points": _series_to_xy(df["smallcap_median"])},
        # right #2 (yIdx) — solid
        {"label": "Nifty 50 — year-end close",
         "color": C_50,  "width": 2.4, "yAxis": "yIdx",
         "points": _series_to_xy(df["nifty50"])},
        {"label": "Nifty Midcap 100 — year-end close",
         "color": C_MID, "width": 2.4, "yAxis": "yIdx",
         "points": _series_to_xy(df["nifty_midcap"])},
        {"label": "Nifty/BSE Smallcap — year-end close",
         "color": C_SM,  "width": 2.4, "yAxis": "yIdx",
         "points": _series_to_xy(df["nifty_smallcap"])},
        # right #3 (yFII) — dotted
        {"label": "Net FII inflow — total Indian equity (USD mn, CDSL)",
         "color": C_FII, "width": 2.4, "yAxis": "yFII",
         "dash": [2, 4],
         "points": _series_to_xy(df["fii_total_usd_mn"])},
    ]
    axes = [
        {"id": "yINR", "title": "INR per 1 USD",
         "color": C_INR, "position": "left"},
        {"id": "yMed", "title": "Median constituent close (INR, dashed)",
         "color": "#444", "position": "right"},
        {"id": "yIdx", "title": "Index level (year-end close, solid)",
         "color": "#222", "position": "right"},
        {"id": "yFII", "title": "Net FII inflow (USD mn, dotted)",
         "color": C_FII, "position": "right"},
    ]
    return _render(
        out, "INR/USD · Nifty 50 / Midcap / Smallcap index levels · median "
             "constituent prices · net FII equity inflow — last 25 years",
        years, series, axes,
        footnote="Tip: click the legend OR the checkboxes above to "
                 "show/hide a line. Use the preset buttons or the "
                 "From/To inputs/sliders to change the year window.",
    )


def render_all() -> None:
    render_inr_usd()
    render_indices()
    render_medians()
    render_combined()


if __name__ == "__main__":
    render_all()
