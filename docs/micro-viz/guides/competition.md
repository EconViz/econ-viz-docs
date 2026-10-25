---
seo_title: "Competition and the long run"
---

# Competition and the long run

<span id="sec-competition"></span>

Price-taking firms, industry supply, long-run costs and entry.

Each section is one example script and the figures it writes. The scripts are in `examples/scripts/` of the repository; `--help` lists their arguments.

## Perfect competition

```bash
uv run python examples/scripts/competition.py --output-dir out
```

### Revenue, cost and profit

Setting: p = 18.

![Revenue, cost and profit](../../assets/micro-viz/en/competition/revenue_cost_profit.svg){ .ev-figure-sm }

### Market and firm

Setting: p = 4.

![Market and firm](../../assets/micro-viz/en/competition/market_and_firm.svg){ .ev-figure-lg }

### Firm earning a profit

Setting: p = 18.

![Firm earning a profit](../../assets/micro-viz/en/competition/firm_profit.svg){ .ev-figure-sm }

### Profit lost off the optimum

Setting: q1 and q2.

![Profit lost off the optimum](../../assets/micro-viz/en/competition/firm_lost_profit.svg){ .ev-figure-sm }

### Firm with a loss

Setting: p = 11.

![Firm with a loss](../../assets/micro-viz/en/competition/firm_loss.svg){ .ev-figure-sm }

### Shutdown

Setting: p = 8.

![Shutdown](../../assets/micro-viz/en/competition/firm_shutdown.svg){ .ev-figure-sm }

### Firm supply curve

Setting: two prices.

![Firm supply curve](../../assets/micro-viz/en/competition/firm_supply.svg){ .ev-figure-sm }

### Cost shift

Setting: MC up.

![Cost shift](../../assets/micro-viz/en/competition/cost_shift.svg){ .ev-figure-sm }

### Per-unit tax

Setting: T = 4.

![Per-unit tax](../../assets/micro-viz/en/competition/unit_tax.svg){ .ev-figure-sm }

### Industry supply

Setting: three firms.

![Industry supply](../../assets/micro-viz/en/competition/industry_supply.svg){ .ev-figure-lg }

### Industry supply alone

Setting: three firms.

![Industry supply alone](../../assets/micro-viz/en/competition/industry_supply_total.svg){ .ev-figure-sm }

### Producer surplus

Setting: p = 18.

![Producer surplus](../../assets/micro-viz/en/competition/producer_surplus.svg){ .ev-figure-sm }

## Long-run costs

```bash
uv run python examples/scripts/long_run_costs.py --output-dir out
```

### LAC and LMC

Setting: U-shaped.

![LAC and LMC](../../assets/micro-viz/en/long_run_costs/lac_lmc.svg){ .ev-figure-sm }

### Short-run envelope

Setting: three plants.

![Short-run envelope](../../assets/micro-viz/en/long_run_costs/short_run_envelope.svg){ .ev-figure-lg }

### Plant family

Setting: three plants.

![Plant family](../../assets/micro-viz/en/long_run_costs/plant_family.svg){ .ev-figure-sm }

## Long-run competition

```bash
uv run python examples/scripts/long_run_competition.py --output-dir out
```

### Firm in the long run

Setting: p above LAC.

![Firm in the long run](../../assets/micro-viz/en/long_run_competition/long_run_firm.svg){ .ev-figure-sm }

### Entry

Setting: profit draws firms.

![Entry](../../assets/micro-viz/en/long_run_competition/entry.svg){ .ev-figure-lg }

### Economic rent

Setting: low-cost firm.

![Economic rent](../../assets/micro-viz/en/long_run_competition/economic_rent.svg){ .ev-figure-lg }

### Constant-cost industry

Setting: demand up.

![Constant-cost industry](../../assets/micro-viz/en/long_run_competition/constant_cost.svg){ .ev-figure-lg }

### Increasing-cost industry

Setting: demand up.

![Increasing-cost industry](../../assets/micro-viz/en/long_run_competition/increasing_cost.svg){ .ev-figure-lg }
