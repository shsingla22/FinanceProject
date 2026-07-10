# The quality framework (full, in prose)

Faithful transcription of `Company_analysis.docx`, organised as 7 modules and 34
leaf parameters. The machine-readable version is `parameters.yaml`; this file is
for human understanding. IDs in brackets are the parameter ids.

---

## 1. Capital Allocation  `[CAP]`
Use the management-commentary / conference-call data to understand where
management allocates capital among these five uses, and how that allocation is
behaving over time.

1. **Capex for growth (not maintenance)** `[CAP.growth_capex]` — distinguish
   growth from maintenance capex; growth capex should be the maximum share, and
   the potential ROIC from new growth capex should be high (e.g. retailers opening
   new stores).
2. **Advertisement and promotion** `[CAP.advertising_promotion]` — marketing that
   creates brand and drives sales; not classified as capex but ideally *is* a
   capital expenditure.
3. **Research and development** `[CAP.research_development]` — helps new product
   creation and customer acquisition; assess long-term R&D efficiency.
4. **Merger and acquisition** `[CAP.mergers_acquisitions]` — acquisitions are a
   common source of value destruction; small bolt-ons succeed more often; the rare
   valuable skill is systematically improving the acquired business (OPM
   improvement post-deal); prefer buying already-strong, small, simple,
   complementary businesses. *Essilor* (bolt-ons, +3%/yr sales), *Luxottica* (buys
   winners like Oakley, leverages distribution), *Diageo* (complementary
   distribution), *Assa Abloy* (~120 deals, improves acquiree OPM).
5. **Distribution to shareholders** `[CAP.shareholder_distribution]` — dividends
   and buybacks; the best buy back advantageously (cheap), but most buybacks happen
   at elevated valuations.
6. **Cost of working capital** `[CAP.working_capital_cost]` — money stuck in
   working capital lowers return on capital; prefer low or negative working capital
   (rare).

## 2. Return on Capital  `[ROC]`
Depends on asset turns and profit margin. The better metric is **Cash Return on
Cash Capital Invested** = post-tax cash return / capital invested after adjusting
accounting conventions like goodwill.  `[ROC.headline]`

- **Asset turn** `[ROC.asset_turn]` — measure of asset intensity; asset-light
  industries are attractive but need additional competitive advantages (Domino's:
  high asset turns, low intensity, protected by a strong brand).
- **Profit margin** `[ROC.profit_margin]` — higher gross margins show pricing
  power; high operating margin + high gross margin indicates competitive
  advantage; big swings in OPM indicate major cost components not in management's
  control.

## 3. Multiple Sources of Growth  `[GRW]`
Future growth is the most expensive part to analyse; the best businesses are where
the end market is growing.

- **Gain in market share** `[GRW.market_share_gain]` — easier early; a company
  above ~50% share finds it tough.
- **Geographical expansion** `[GRW.geographic_expansion]` — challenging but
  powerful if executed well (Unilever ~60% revenue from emerging markets; premium
  brands like Nike transition easily).
- **Pricing, Mix and Volume** `[GRW.pricing_mix_volume]` — three revenue levers:
  pricing power (raise price without cost; price-insensitive luxury/status buyers)
  and mix optimisation (shift to value-added) are valuable; volume growth is least
  valuable (costs, incl. working capital, rise with volume).
- **Cyclical market growth** `[GRW.cyclical_growth]` — double-edged; invest at the
  bottom of the cycle (Marriott 2009→2015 ~6x); understand cycles to ride upside,
  avoid downside.
- **Structural end-market growth** `[GRW.structural_growth]` — permanent expansion
  (disease prevention, urbanisation, aging demographics); don't extrapolate
  cyclical uptrends as structural.
- **Persistence of growth** `[GRW.persistence]` — no relation between prior 5-yr
  and next 5-yr growth; find companies with consistent, predictable 10–15% growth;
  the link is return on capital (higher CFROI → higher future earnings growth).

## 4. Good Management  `[MGT]`
Strong management + well-positioned companies is a powerful combination.

- **Disciplined stewards** `[MGT.disciplined_stewards]` — patience/discipline for
  organic growth; prudent balance sheet; counter-cyclical investment; big inorganic
  bets absent.
- **Independent, long-term and tenacious** `[MGT.independent_longterm_tenacious]` —
  Handelsbanken (decentralised, profit-sharing, risk aversion); Rolls-Royce
  (long-term engine-then-servicing model); eradication of threats.
- **Out of limelight** `[MGT.out_of_limelight]` — award-winning CEOs underperform
  vs their prior record and peers.
- **People matter** `[MGT.people_talent]` — developing talent as top priority;
  Atlas Copco (execs rotate every ~3 years; four went on to lead other majors).
- **Candor** `[MGT.candor]` — effective communication to investors on what and why.
- **Halo effect** `[MGT.halo_effect_caution]` — a caution: much of our thinking is
  shaped by the halo effect.

## 5. Industry Structure  `[IND]`

- **Mini-monopolies** `[IND.mini_monopolies]` — an unregulated monopoly is
  strongest but gets targeted by governments; mini-monopolies exist in the
  customer's mind (tobacco brand loyalty) or in services (spare parts, software
  upgrades).
- **Partial monopoly** `[IND.partial_monopoly]` — broken competition (Ambev ~50%
  EBITDA in Brazil; logistics barriers) and switching costs (razor-blade/software;
  competitive upfront vs captive aftermarket; Atlas Copco has good service *and*
  upfront margins).
- **Oligopoly** `[IND.oligopoly]` — sometimes better than a duopoly (duopoly can
  become an obsession to beat the rival); prefer end customers without negotiating
  power and stable structures.
- **Barriers to entry and rationality** `[IND.barriers_entry_rationality]` —
  distinguish barriers to entry from barriers to success/scale; prefer few/no new
  entrants; family-owned big firms signal stability; avoid price wars (Coca-Cola's
  North America bulk-on-sale problem); favour non-discounters (LVMH didn't discount
  champagne in 2008).
- **Share donators** `[IND.share_donators]` — weak members (management
  incompetence, suboptimal products, ignored divisions, sub-scale companies).
- **Security by obscurity** `[IND.security_by_obscurity]` — humble niches (locks,
  lenses, bathroom fittings) that capital and competitors ignore.

## 6. Customer Benefits  `[CUS]`
Quality companies confer considerable benefits on their customers.

- **Intangible benefits** `[CUS.intangible_benefits]` — taste and image (high-end
  bags, cars, watches, jewelry); the smaller the ticket, the bigger the role;
  L'Oréal's ~$90 tub vs ~5x-cheaper Nivea, with consumers never testing the
  comparison; demand rises in expansions, steady in contractions.
- **Assurance benefits** `[CUS.assurance_benefits]` — where reliability is
  paramount and a small component's failure shuts a plant (industrial gases; baby
  food; SGS/Intertek testing — complex supply chains, high cost of deviation, few
  trusted testers).
- **Convenience benefits** `[CUS.convenience_benefits]` — readily accessible
  product; customer intimacy via a strong direct sales force.
- **Customer types** `[CUS.customer_types]` — retail customers splurge on
  intangibles; corporate clients are rational (TCO, reliability) but their high
  switching costs can be exploited.

## 7. Competitive Advantage  `[MOAT]`

- **Technology** `[MOAT.technology]` — must not be a single (copyable) product; the
  magnitude must be large; % R&D matters; deliver superior customer benefits;
  includes incremental innovation (jet engines post-1960s) and data advantage
  (Google). Syngenta: ~$300M and ~10 years per API, ~$4B R&D over 3 years, ~$3B
  peak sales; farmers keep buying seeds even in downturns.
- **Network effects** `[MOAT.network_effects]` — value grows with users (more
  sellers → more buyers); too-strong effects can backfire (UK agents formed a rival
  network); high innovation pace is a risk (Facebook killed MySpace, MSN chat).
- **Distribution** `[MOAT.distribution]` — a route to consumers more effective than
  rivals'; critical where the ability to service/fix the product is vital.
