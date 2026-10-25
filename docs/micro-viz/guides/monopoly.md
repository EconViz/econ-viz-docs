---
seo_title: "Monopoly and pricing"
---

# Monopoly and pricing

<span id="sec-monopoly"></span>

Market power: the single-price monopoly, its regulation, and pricing beyond one price.

Each section is one example script and the figures it writes. The scripts are in `examples/scripts/` of the repository; `--help` lists their arguments.

## Monopoly

```bash
uv run python examples/scripts/monopoly.py --output-dir out
```

### Monopoly: MR = MC

Setting: linear demand.

![Monopoly: MR = MC](../../assets/micro-viz/en/monopoly/monopoly.svg){ .ev-figure-sm }

### Monopoly: profit lost off the optimum

Setting: Q1 and Q2.

![Monopoly: profit lost off the optimum](../../assets/micro-viz/en/monopoly/monopoly_lost_profit.svg){ .ev-figure-sm }

### Monopoly profit

Setting: linear demand.

![Monopoly profit](../../assets/micro-viz/en/monopoly/monopoly_profit.svg){ .ev-figure-sm }

### Revenue, cost and profit

Setting: linear demand.

![Revenue, cost and profit](../../assets/micro-viz/en/monopoly/monopoly_totals.svg){ .ev-figure-sm }

### Totals and unit curves

Setting: two panels.

![Totals and unit curves](../../assets/micro-viz/en/monopoly/monopoly_totals_grid.svg){ .ev-figure-sm }

### Deadweight loss of monopoly

Setting: linear demand.

![Deadweight loss of monopoly](../../assets/micro-viz/en/monopoly/monopoly_dwl.svg){ .ev-figure-sm }

### Per-unit tax on a monopolist

Setting: T = 4.

![Per-unit tax on a monopolist](../../assets/micro-viz/en/monopoly/monopoly_tax.svg){ .ev-figure-sm }

### Demand shift

Setting: intercept 30 to 36.

![Demand shift](../../assets/micro-viz/en/monopoly/monopoly_demand_shift.svg){ .ev-figure-sm }

### Demand rotation

Setting: slope 2 to 1.5.

![Demand rotation](../../assets/micro-viz/en/monopoly/monopoly_demand_rotate.svg){ .ev-figure-sm }

### Multiplant monopoly

Setting: two plants.

![Multiplant monopoly](../../assets/micro-viz/en/monopoly/multiplant.svg){ .ev-figure-lg }

### Lerner markup

Setting: elastic and inelastic.

![Lerner markup](../../assets/micro-viz/en/monopoly/lerner_markup.svg){ .ev-figure-lg }

## Monopolistic competition

```bash
uv run python examples/scripts/monopolistic_competition.py --output-dir out
```

### Short run

Setting: profit before entry.

![Short run](../../assets/micro-viz/en/monopolistic_competition/short_run.svg){ .ev-figure-sm }

### Long-run tangency

Setting: profit zero.

![Long-run tangency](../../assets/micro-viz/en/monopolistic_competition/long_run.svg){ .ev-figure-sm }

### Excess capacity

Setting: versus perfect competition.

![Excess capacity](../../assets/micro-viz/en/monopolistic_competition/excess_capacity.svg){ .ev-figure-lg }

## Regulation

```bash
uv run python examples/scripts/regulation.py --output-dir out
```

### Price ceiling on a monopolist

Setting: ceiling 12.

![Price ceiling on a monopolist](../../assets/micro-viz/en/regulation/price_ceiling.svg){ .ev-figure-sm }

### Natural monopoly pricing

Setting: falling ATC.

![Natural monopoly pricing](../../assets/micro-viz/en/regulation/natural_monopoly.svg){ .ev-figure-sm }

## Price discrimination

```bash
uv run python examples/scripts/price_discrimination.py --output-dir out
```

### One monopoly price

Setting: MR = MC.

![One monopoly price](../../assets/micro-viz/en/price_discrimination/single_price.svg){ .ev-figure-sm }

### Perfect discrimination

Setting: price follows demand.

![Perfect discrimination](../../assets/micro-viz/en/price_discrimination/first_degree.svg){ .ev-figure-sm }

### Block pricing

Setting: three blocks.

![Block pricing](../../assets/micro-viz/en/price_discrimination/block_pricing_three.svg){ .ev-figure-sm }

### Block pricing with falling ATC

Setting: six blocks.

![Block pricing with falling ATC](../../assets/micro-viz/en/price_discrimination/block_pricing.svg){ .ev-figure-sm }

### Third-degree discrimination

Setting: two markets.

![Third-degree discrimination](../../assets/micro-viz/en/price_discrimination/third_degree.svg){ .ev-figure-lg }

### Third degree, corner

Setting: rising MC.

![Third degree, corner](../../assets/micro-viz/en/price_discrimination/third_degree_corner.svg){ .ev-figure-lg }

## Two-part tariffs

```bash
uv run python examples/scripts/two_part_tariff.py --output-dir out
```

### Two-part tariff, one buyer

Setting: usage fee = MC.

![Two-part tariff, one buyer](../../assets/micro-viz/en/two_part_tariff/single_buyer.svg){ .ev-figure-sm }

### Two-part tariff, two buyer types

Setting: usage fee above MC.

![Two-part tariff, two buyer types](../../assets/micro-viz/en/two_part_tariff/two_buyers.svg){ .ev-figure-sm }

### Profit against the entry fee

Setting: usage fee fixed.

![Profit against the entry fee](../../assets/micro-viz/en/two_part_tariff/tariff_profit.svg){ .ev-figure-sm }

## Bundling

```bash
uv run python examples/scripts/bundling.py --output-dir out
```

### Valuation space

Setting: three consumers.

![Valuation space](../../assets/micro-viz/en/bundling/valuation_points.svg){ .ev-figure-sm }

### Separate selling

Setting: P1, P2.

![Separate selling](../../assets/micro-viz/en/bundling/separate_regions.svg){ .ev-figure-sm }

### Pure bundling

Setting: r1 + r2 = PB.

![Pure bundling](../../assets/micro-viz/en/bundling/pure_bundling.svg){ .ev-figure-sm }

### Mixed bundling

Setting: negative correlation.

![Mixed bundling](../../assets/micro-viz/en/bundling/mixed_bundling.svg){ .ev-figure-sm }

### Mixed bundling with costs

Setting: C1, C2 > 0.

![Mixed bundling with costs](../../assets/micro-viz/en/bundling/mixed_with_costs.svg){ .ev-figure-sm }

### Regions I to IV

Setting: positive correlation.

![Regions I to IV](../../assets/micro-viz/en/bundling/regions_numbered.svg){ .ev-figure-sm }

## Intertemporal and peak-load pricing

```bash
uv run python examples/scripts/time_pricing.py --output-dir out
```

### Intertemporal pricing

Setting: high price first.

![Intertemporal pricing](../../assets/micro-viz/en/time_pricing/intertemporal.svg){ .ev-figure-sm }

### Peak-load pricing

Setting: capacity cost on the peak.

![Peak-load pricing](../../assets/micro-viz/en/time_pricing/peak_load.svg){ .ev-figure-sm }

## Advertising

```bash
uv run python examples/scripts/advertising.py --output-dir out
```

### Advertising

Setting: AR out, AC up.

![Advertising](../../assets/micro-viz/en/advertising/advertising.svg){ .ev-figure-sm }

## Exhaustible resources

```bash
uv run python examples/scripts/exhaustible_resource.py --output-dir out
```

### Exhaustible resource

Setting: Hotelling path.

![Exhaustible resource](../../assets/micro-viz/en/exhaustible_resource/resource_price_path.svg){ .ev-figure-lg }
