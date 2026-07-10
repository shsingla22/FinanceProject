# Data sources — how each parameter is fed

The skill consumes the data layer produced elsewhere in this repo. Each logical
data source below maps to a physical location, discovered at runtime (never
hard-coded into judgements — see the skill's maintainability design).

| Logical source (`data_sources` in parameters.yaml) | Physical location (per universe `U`, per symbol `S`) | Kind |
|---|---|---|
| `balance_sheet`   | `../../BalanceSheet/U/S.csv` and `_all_balance_sheets_long.csv` | quantitative |
| `profit_loss`     | `../../ProfitStatement/U/S.csv` and `_all_profit_loss_long.csv` | quantitative |
| `cash_flow`       | `../../CashFlow/U/S.csv` and `_all_cash_flow_long.csv` | quantitative |
| `working_capital` | `../../WorkingCapital/U/S.csv` and `_all_working_capital_long.csv` | quantitative |
| `stock_info`      | `../../StockInfo/U/S.csv`, `_all_stock_info_long.csv`, `live_market_data.csv` | quantitative |
| `concalls`        | `../../ConferenceCalls/U/S.pdf` (merged transcript text, oldest-first) | qualitative |
| `annual_reports`  | AR PDFs (listed via screener.in; cached during ingestion) | qualitative |
| `management_info` | `../../ManagementInfo/U/S.csv` (Chairman/MD/CEO/CFO history) | qualitative |

`U` defaults to `NiftyTotalMarket` (742 cos) but the skill works for any
universe folder that follows the same layout (e.g. `Nifty500`).

## Line items the quantitative engine relies on

**Balance sheet:** Fixed Assets, CWIP, Total Assets, Reserves, Equity Capital,
Borrowings, Investments, Inventories, Trade receivables, Trade Payables,
Cash Equivalents.

**Profit & loss:** Sales, Operating Profit, OPM %, Net Profit, Material Cost %
(for gross-margin proxy), Interest, Depreciation, EPS.

**Cash flow:** Cash from Operating Activity, Fixed assets purchased (capex),
Investments purchased/sold (M&A proxy), Proceeds from/Repayment of borrowings,
Dividends paid, Proceeds from shares (buyback proxy when negative).

**Working capital:** Debtor Days, Inventory Days, Days Payable,
Cash Conversion Cycle, Working Capital Days, ROCE %.

**Stock info:** Stock Price, Market Cap, P/E ratio (for the valuation-discipline
overlays under capital allocation and cyclical growth).

## Data availability caveats (must be surfaced in every analysis)

- Some line items (**R&D**, **Advertising & Promotion**) are NOT separable in the
  standard screener.in P&L. These parameters therefore fall back to
  qualitative extraction from annual reports / concalls, and the quantitative
  engine marks them `data_available: false`.
- **Gross margin** is approximated as `100 - Material Cost %` when a direct COGS
  line is unavailable.
- **Growth vs maintenance capex** is not separable from reported capex; the split
  is inferred qualitatively from management commentary, with total capex intensity
  as the quantitative anchor.
- Non-March fiscal-year reporters and recent IPOs have shorter histories; trend
  and persistence signals require >= 4 years and are flagged `insufficient_history`
  otherwise.
