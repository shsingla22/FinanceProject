# Qualitative analysis playbook

16 of the 34 parameters are purely qualitative and 14 are hybrid — the human /
commentary side is the majority of this framework. This playbook tells an agent
**how to judge each qualitative and hybrid parameter from the concall transcripts,
annual reports, and management-history data**, and how to emit a `-2..+2` score
with a rationale and source pointers (so `scoring.py` can aggregate it).

## How to run it

For each company:
1. Load the merged **conference-call transcript** (oldest → newest) and, where
   needed, the **annual report** text and the **management-info** CSV.
2. For each parameter below, answer its **judgement questions** using ONLY the
   text. Quote the specific sentence(s) you rely on.
3. Emit a `ParamScore`: `score` (-2..+2), `rationale` (1–3 sentences),
   `evidence` (the quotes/numbers), `sources` (file + FY/quarter).
4. If the text does not address a parameter, score `None` (not assessed) — do
   **not** guess. Coverage is reported honestly.

Scoring convention: `+2` strong evidence for the quality trait, `0`
mixed/neutral, `-2` strong evidence against. Anchor every score to a quote.

---

## CAP — Capital Allocation (read management commentary first)

- **CAP.growth_capex** — Does management describe capex as *growth* (new
  capacity/stores/plants) vs just *maintenance*? Is there a stated ROIC/payback
  on new projects? Quote the capex rationale. Pair with `capex_intensity` from the
  quant engine. `+2` = large, high-return growth capex clearly articulated.
- **CAP.advertising_promotion** — Is A&P framed as brand-building investment with
  a sales response, or unfocused spend? Look for brand-equity language and
  discipline. (Quant cannot separate A&P — this is text-only.)
- **CAP.research_development** — Evidence of R&D → new products / customers, and
  of long-run R&D efficiency (output per R&D rupee). `+2` = a track record of
  R&D translating into revenue.
- **CAP.mergers_acquisitions** — Are deals small, bolt-on, complementary, and is
  the acquiree already strong? Does management show margin (OPM) improvement of
  acquired units? `-2` = large transformational M&A; `+2` = disciplined bolt-ons
  with post-deal OPM gains (cf. Assa Abloy, Essilor).
- **CAP.shareholder_distribution** — Is there a coherent dividend/buyback policy,
  and are buybacks done when the stock is CHEAP (check P/E context)? `-2` =
  buybacks at peak valuations.
- **CAP.working_capital_cost** — hybrid; quant supplies CCC/WC-days. Confirm with
  commentary whether low/negative working capital is structural or a one-off.

## GRW — Growth (quality of the growth, not just the rate)

- **GRW.market_share_gain** — Is there runway (not already >50% share)? Evidence of
  actually taking share? 
- **GRW.geographic_expansion** — Credible new-geography strategy, well executed;
  premium brand that travels. `-2` = flailing overseas forays.
- **GRW.pricing_mix_volume** — Classify the growth: **pricing** (raise price w/o
  cost) and **mix** (shift to value-added) are valuable; **volume** is least
  valuable. Pair with the quant hint (rising OPM alongside growth ⇒ price/mix).
- **GRW.cyclical_growth** — Is the end-market cyclical, and where in the cycle are
  we? Reward positioning near a trough. Flag any extrapolation of a cyclical
  upturn as structural.
- **GRW.structural_growth** — Is the end market in permanent secular expansion
  (demographics, urbanisation, prevention)? `+2` = clear structural tailwind.
- **GRW.persistence** — hybrid; quant supplies growth consistency. Confirm whether
  ~10–15% consistent growth is durable and ROC-funded.

## MGT — Good Management (concalls + management-info CSV)

- **MGT.disciplined_stewards** — Patience for organic growth, prudent balance
  sheet, counter-cyclical investment, big inorganic bets absent.
- **MGT.independent_longterm_tenacious** — Long-term vision executed with
  independence and tenacity; threat eradication (cf. Handelsbanken, Rolls-Royce).
- **MGT.out_of_limelight** — Prefer low-profile operators; be wary of celebrity /
  award-winning CEOs (they tend to underperform).
- **MGT.people_talent** — Talent development as a stated priority; strong internal
  pipeline / executive rotation (cf. Atlas Copco). The management-info CSV's
  tenure/stability history is direct evidence here.
- **MGT.candor** — Candid communication of what matters and why; owning mistakes
  in transcripts is a strong positive signal.
- **MGT.halo_effect_caution** — A meta-check: is your management view driven by
  recent results (halo) rather than durable behaviour? Score how robust your read
  is to the halo effect; downgrade confidence if it isn't.

## IND — Industry Structure

- **IND.mini_monopolies** — A monopoly in the customer's mind (brand) or in
  aftermarket/services (spares, upgrades). `+2` = clear mini-monopoly.
- **IND.partial_monopoly** — Regional monopoly / broken competition, or captive
  aftermarket via switching costs (razor-blade, software).
- **IND.oligopoly** — Stable oligopoly with end customers lacking negotiating
  power; wary of destructive duopoly dynamics.
- **IND.barriers_entry_rationality** — hybrid; quant supplies margin stability.
  Few/no new entrants, rational pricing (no discount wars), stable/family
  ownership. `-2` = habitual discounting / price wars.
- **IND.share_donators** — Are there weak competitors (incompetent management,
  poor products, ignored divisions, sub-scale) to take share from?
- **IND.security_by_obscurity** — A humble niche that capital and competitors
  ignore (locks/lenses/fittings).

## CUS — Customer Benefits

- **CUS.intangible_benefits** — hybrid; quant supplies gross-margin power. Does the
  product sell on taste/image with price-insensitive demand (steady in downturns)?
- **CUS.assurance_benefits** — Is reliability paramount (failure is catastrophic),
  so customers pay for certainty (industrial gases, testing, baby food)?
- **CUS.convenience_benefits** — Superior accessibility and direct customer
  intimacy / strong sales force.
- **CUS.customer_types** — Identify retail vs corporate mix and whether the
  benefit type matches (intangibles→retail; TCO/reliability + switching-cost
  lock-in→corporate).

## MOAT — Competitive Advantage

- **MOAT.technology** — hybrid; quant would use R&D intensity (not separable here,
  so rely on text). A deep, MULTI-product tech edge of large magnitude delivering
  superior customer benefit. `-2` = single, copyable product / slight edge.
- **MOAT.network_effects** — Self-reinforcing two-sided network. Note the
  cautions: too-strong effects can breed rival networks; high innovation pace is
  a disruption risk.
- **MOAT.distribution** — A route-to-customer / service reach rivals cannot match,
  especially where servicing the product is vital.

---

### Output contract

Every qualitative/hybrid judgement returns the same `ParamScore` shape as the
quant path, so both feed one aggregation and one explainability trace. A hybrid
parameter's final score should reconcile the quant signal and the text: if they
disagree, say so in the rationale and let the text arbitrate intent (e.g. quant
shows high capex, text reveals it is maintenance → do not credit as growth capex).
