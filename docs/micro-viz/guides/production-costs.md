---
seo_title: "Production and costs"
---

# Production and costs

<span id="sec-production-costs"></span>

Short-run production and the cost curves that follow from it.

Each section is one example script and the figures it writes. The scripts are in `examples/scripts/` of the repository; `--help` lists their arguments.

## Short-run production

```bash
uv run python examples/scripts/production.py --output-dir out
```

### Total product

Setting: cubic.

![Total product](../../assets/micro-viz/en/production/total_product.svg){ .ev-figure-sm }

### Average and marginal product

Setting: cubic.

![Average and marginal product](../../assets/micro-viz/en/production/average_marginal_product.svg){ .ev-figure-sm }

### Total product, shade under the curve

Setting: cubic.

![Total product, shade under the curve](../../assets/micro-viz/en/production/total_product_under_curve.svg){ .ev-figure-sm }

### Average and marginal product, shade under the curve

Setting: cubic.

![Average and marginal product, shade under the curve](../../assets/micro-viz/en/production/average_marginal_product_under_curve.svg){ .ev-figure-sm }

## Short-run costs

```bash
uv run python examples/scripts/costs.py --output-dir out
```

### Total, variable and fixed cost

Setting: cubic.

![Total, variable and fixed cost](../../assets/micro-viz/en/costs/total_cost.svg){ .ev-figure-sm }

### Unit costs

Setting: cubic.

![Unit costs](../../assets/micro-viz/en/costs/unit_cost.svg){ .ev-figure-sm }

### AVC and MC of a cubic cost

Setting: cubic.

![AVC and MC of a cubic cost](../../assets/micro-viz/en/costs/cubic_avc_mc.svg){ .ev-figure-sm }

### Cost curves

Setting: cubic, two panels.

![Cost curves](../../assets/micro-viz/en/costs/cost_curves.svg){ .ev-figure-sm }

### Total cost panel

Setting: cubic.

![Total cost panel](../../assets/micro-viz/en/costs/cost_curves_total.svg){ .ev-figure-sm }

### Unit cost panel

Setting: cubic.

![Unit cost panel](../../assets/micro-viz/en/costs/cost_curves_unit.svg){ .ev-figure-sm }

## Stepped and kinked cost

```bash
uv run python examples/scripts/piecewise_costs.py --output-dir out
```

### Stepped marginal cost

Setting: two plants.

![Stepped marginal cost](../../assets/micro-viz/en/piecewise_costs/stepped_cost.svg){ .ev-figure-sm }

### Stepped cost and output

Setting: two prices.

![Stepped cost and output](../../assets/micro-viz/en/piecewise_costs/stepped_cost_prices.svg){ .ev-figure-sm }

### Kinked marginal cost

Setting: capacity.

![Kinked marginal cost](../../assets/micro-viz/en/piecewise_costs/kinked_marginal_cost.svg){ .ev-figure-sm }
