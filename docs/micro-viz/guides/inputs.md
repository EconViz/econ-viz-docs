---
seo_title: "Inputs and technology"
---

# Inputs and technology

<span id="sec-inputs"></span>

Long-run technology, the choice of inputs, and factor markets.

Each section is one example script and the figures it writes. The scripts are in `examples/scripts/` of the repository; `--help` lists their arguments.

## Isoquants

```bash
uv run python examples/scripts/isoquants.py --output-dir out
```

### Isoquant map

Setting: Cobb-Douglas.

![Isoquant map](../../assets/micro-viz/en/isoquants/isoquant_map.svg){ .ev-figure-sm }

### Diminishing MRTS

Setting: four points.

![Diminishing MRTS](../../assets/micro-viz/en/isoquants/mrts_steps.svg){ .ev-figure-sm }

### MRTS triangle

Setting: ΔK and ΔL.

![MRTS triangle](../../assets/micro-viz/en/isoquants/mrts_triangle.svg){ .ev-figure-sm }

### Perfect substitutes

Setting: straight isoquants.

![Perfect substitutes](../../assets/micro-viz/en/isoquants/perfect_substitutes.svg){ .ev-figure-sm }

### Fixed proportions

Setting: L-shaped isoquants.

![Fixed proportions](../../assets/micro-viz/en/isoquants/fixed_proportions.svg){ .ev-figure-sm }

### Returns to scale

Setting: constant and increasing.

![Returns to scale](../../assets/micro-viz/en/isoquants/returns_to_scale.svg){ .ev-figure-lg }

## Cost minimization

```bash
uv run python examples/scripts/cost_minimization.py --output-dir out
```

### Cost minimization

Setting: tangency.

![Cost minimization](../../assets/micro-viz/en/cost_minimization/cost_minimization.svg){ .ev-figure-sm }

### Dearer labor

Setting: wage up.

![Dearer labor](../../assets/micro-viz/en/cost_minimization/input_price_change.svg){ .ev-figure-sm }

### Technical change

Setting: isoquant inward.

![Technical change](../../assets/micro-viz/en/cost_minimization/technical_change.svg){ .ev-figure-sm }

### Expansion path

Setting: three outputs.

![Expansion path](../../assets/micro-viz/en/cost_minimization/expansion_path.svg){ .ev-figure-sm }

### Fixed capital

Setting: K0.

![Fixed capital](../../assets/micro-viz/en/cost_minimization/fixed_capital.svg){ .ev-figure-sm }

## Learning, scope and frontier

```bash
uv run python examples/scripts/production_extensions.py --output-dir out
```

### Learning curve

Setting: A + B N^-beta.

![Learning curve](../../assets/micro-viz/en/production_extensions/learning_curve.svg){ .ev-figure-sm }

### Scale versus learning

Setting: A to B to C.

![Scale versus learning](../../assets/micro-viz/en/production_extensions/scale_vs_learning.svg){ .ev-figure-sm }

### Product transformation curve

Setting: bow 2.

![Product transformation curve](../../assets/micro-viz/en/production_extensions/product_transformation.svg){ .ev-figure-sm }

### Technical progress

Setting: three technologies.

![Technical progress](../../assets/micro-viz/en/production_extensions/technology_shift.svg){ .ev-figure-sm }

### Production frontier

Setting: two inefficient points.

![Production frontier](../../assets/micro-viz/en/production_extensions/production_frontier.svg){ .ev-figure-sm }

## Factor markets

```bash
uv run python examples/scripts/factor_markets.py --output-dir out
```

### VMP and MRP

Setting: monopoly output market.

![VMP and MRP](../../assets/micro-viz/en/factor_markets/derived_demand.svg){ .ev-figure-sm }

### Firm hiring

Setting: flat supply.

![Firm hiring](../../assets/micro-viz/en/factor_markets/firm_hiring.svg){ .ev-figure-sm }

### A lower market wage

Setting: supply shifts down.

![A lower market wage](../../assets/micro-viz/en/factor_markets/wage_decline.svg){ .ev-figure-sm }

### MRP as capital adjusts

Setting: three capital levels.

![MRP as capital adjusts](../../assets/micro-viz/en/factor_markets/capital_adjustment.svg){ .ev-figure-sm }

### Firm and industry demand

Setting: price effect.

![Firm and industry demand](../../assets/micro-viz/en/factor_markets/industry_demand.svg){ .ev-figure-lg }

### Short- and long-run input demand

Setting: one anchor.

![Short- and long-run input demand](../../assets/micro-viz/en/factor_markets/short_long_run.svg){ .ev-figure-sm }

### Market and firm supply

Setting: two panels.

![Market and firm supply](../../assets/micro-viz/en/factor_markets/market_supply.svg){ .ev-figure-lg }

### Factor-market equilibrium

Setting: competitive and monopoly output.

![Factor-market equilibrium](../../assets/micro-viz/en/factor_markets/factor_equilibrium.svg){ .ev-figure-lg }

### Economic rent of labor

Setting: supply curve.

![Economic rent of labor](../../assets/micro-viz/en/factor_markets/economic_rent.svg){ .ev-figure-sm }

### Land rent

Setting: vertical supply.

![Land rent](../../assets/micro-viz/en/factor_markets/land_rent.svg){ .ev-figure-sm }

## Monopsony and unions

```bash
uv run python examples/scripts/monopsony.py --output-dir out
```

### Competitive buyer and seller

Setting: p = 12.

![Competitive buyer and seller](../../assets/micro-viz/en/monopsony/competitive_pair.svg){ .ev-figure-lg }

### Monopsony

Setting: linear.

![Monopsony](../../assets/micro-viz/en/monopsony/monopsony.svg){ .ev-figure-sm }

### Monopoly and monopsony

Setting: side by side.

![Monopoly and monopsony](../../assets/micro-viz/en/monopsony/monopoly_monopsony.svg){ .ev-figure-lg }

### Supply elasticity

Setting: elastic and inelastic.

![Supply elasticity](../../assets/micro-viz/en/monopsony/supply_elasticity.svg){ .ev-figure-lg }

### Monopsony deadweight loss

Setting: A, B, C.

![Monopsony deadweight loss](../../assets/micro-viz/en/monopsony/monopsony_dwl.svg){ .ev-figure-sm }

### Labor monopsony

Setting: MRP, ME, S.

![Labor monopsony](../../assets/micro-viz/en/monopsony/labor_monopsony.svg){ .ev-figure-sm }

### Union wage setting

Setting: wage bill maximising.

![Union wage setting](../../assets/micro-viz/en/monopsony/union.svg){ .ev-figure-sm }

### Two-sector labor market

Setting: union wage in sector 1.

![Two-sector labor market](../../assets/micro-viz/en/monopsony/two_sector.svg){ .ev-figure-lg }
