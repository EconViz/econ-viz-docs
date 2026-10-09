---
seo_title: "Change history"
---

<span id="sec-changelog"></span>

# Change history

Release history of `principle-viz`, including its releases as
`principle-econ`. Documentation-only changes are not listed; each entry is
tagged where the feature it describes is documented, following l3doc
convention, so the page number is the real page.

## 0.10.1

- CI tests Python 3.10--3.13 [Introduction](guides/introduction.md)
- `demand_aggregation_figure` — The market curve names the demand that is active at a kink [Market curves from individuals](guides/aggregation.md)
- `Label` — Every built-in label can be renamed, hidden or moved: `Label`, `labels=`, `configure_label()` and `label_ids` [Figures](guides/figures.md)
- `MarketFigure.configure_layer` — Every layer can be hidden or shown: `visibility=`, `configure_layer()`, `hide()`, `show()` and `layer_ids` [Figures](guides/figures.md)

## 0.10.0

- Renamed from `principle-econ` to `principle-viz`, joining the EconViz family; the Python package is `principle_viz` [Introduction](guides/introduction.md)
- Figures are built on `mosaickit` (`mosaickit>=0.5.1,<0.6.0`) [Introduction](guides/introduction.md)
- Project tooling moved from Poetry to `uv` [Introduction](guides/introduction.md)
- `principle-viz` — The only runtime dependency is `mosaickit` [Installation](installation.md)
- `add_comparative_statics` — Redraws only the curve that moved; shifted curves are named $D_1$ / $S_1$ (`demand_label` / `supply_label`) [Linear markets](guides/markets.md)
- `add_comparative_statics` — Movement arrows are thin, black and dashed [Linear markets](guides/markets.md)
- `MarketFigure.add_discrete_curves` — Accepts a demand schedule, a supply schedule, or both [Discrete markets](guides/discrete.md)
- `MarketFigure.add_discrete_curves` — Open endpoints are drawn with an opaque white face, joined to the next step by a thin dashed riser [Discrete markets](guides/discrete.md)
- `market_demand` — Market demand and supply as the horizontal sum of individual linear curves, with `PiecewiseLinear`, `solve_piecewise_equilibrium()` and `piecewise_surplus()` [Market curves from individuals](guides/aggregation.md)
- `DiscreteDemand.combine` — `combine()` and `quantity_at()` for discrete schedules [Market curves from individuals](guides/aggregation.md)
- `demand_aggregation_figure` — Individual | individual | market figures for demand and supply, linear and discrete, returning an `AggregationFigure` [Market curves from individuals](guides/aggregation.md)
- `demand_aggregation_figure` — `link_price=True` runs the price line across every panel [Market curves from individuals](guides/aggregation.md)
- `MarketFigure.add_welfare` — Regions are named in words ("Consumer surplus", "CS", ...) inside, by short name or by callout; `labels=False` shades only [Welfare](guides/welfare.md)
- `MarketFigure.add_welfare` — Consumer and producer surplus reuse the demand and supply hues; tax revenue is labelled rather than shaded [Welfare](guides/welfare.md)
- `MarketFigure.add_tax_transform` — Taxed curves are named $S + t$ / $D - t$; the rotation label sits at the arrow's tail [Taxes and subsidies](guides/taxes.md)
- `MarketFigure.add_tax_comparison` — Marks $p_d$, $p_0$ and $p_s$ on the price axis with a "Tax" brace; `brace_side` and `notes` [Taxes and subsidies](guides/taxes.md)
- `MarketFigure.add_subsidy_comparison` — Subsidy wedge with a "Subsidy" brace, and the subsidy's cost named [Taxes and subsidies](guides/taxes.md)
- `MarketFigure.add_price_control` — Binding controls name the control line, mark $p_c$, $Q_d$ and $Q_s$, and brace "Shortage" or "Surplus" on the control line; `gap_brace="axis"` braces it under the quantity axis [Price controls](guides/controls.md)
- `MarketFigure.add_trade` — Marks $Q_s$ / $Q_d$ and braces "Imports" / "Exports" under the quantity axis; the policy price is marked $p_w + t$ or $p_q$ [International trade](guides/trade.md)
- `MarketFigure.add_externality` — Social curves are named $M S C$ / $M S B$; $Q_m$ and $Q^*$ are marked on the quantity axis; corrective taxes and subsidies span the gap at $Q^*$ [Market failures](guides/failures.md)
- `MarketFigure.add_minimum_wage` — Drawn like a price floor: the "Minimum wage" line, $w_{\min}$, $L_d$ / $L_s$ and an "Unemployment" brace [Labor and loanable funds](guides/factor-markets.md)
- `MarketFigure` — Figures are square (6 × 6 in at 150 dpi) on an opaque white background; straight curves stop at 92% of the price axis [Figures](guides/figures.md)
- `MarketFigure` — Curves are named beside their visible end instead of in a legend [Figures](guides/figures.md)
- `MarketFigure` — Axis titles default to $p$ and $Q$, set in italic math past the arrow tips; titles use normal weight [Figures](guides/figures.md)
- `MarketFigure` — Equilibrium and policy labels are placed by `mosaickit` beside their point; crowded quantities are marked on the quantity axis [Figures](guides/figures.md)
- `MarketFigure.finalize` — No legend by default; `finalize(legend=True)` adds one [Figures](guides/figures.md)
- `ColorModel` — The `default` palette takes its hues from `mosaickit`: demand blue, supply red, deadweight loss teal [Figures](guides/figures.md)
- `PlotTheme` — Supply and demand curves are 3.5 pt wide, axes 1.0 pt, equilibrium points 6.5 pt across [Figures](guides/figures.md)

## 0.1.0

- Initial release as `principle-econ`: linear markets, taxes, welfare, plotting and a command-line interface [Introduction](guides/introduction.md)
- `TaxScenario` — Fixed, per-unit and ad valorem taxes, with legal incidence on buyers or sellers [Taxes and subsidies](guides/taxes.md)
- `ColorModel` — `default`, `colorblind`, `nord` and `monochrome` colour models [Figures](guides/figures.md)
- `principle-viz` — Command-line interface with JSON output [Command-line interface](cli.md)

