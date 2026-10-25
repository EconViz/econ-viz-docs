---
seo_title: "Uncertainty and information"
---

# Uncertainty and information

<span id="sec-uncertainty"></span>

Risk, auctions and asymmetric information.

Each section is one example script and the figures it writes. The scripts are in `examples/scripts/` of the repository; `--help` lists their arguments.

## Choice under uncertainty

```bash
uv run python examples/scripts/uncertainty.py --output-dir out
```

### Utility of income

Setting: concave, convex, linear.

![Utility of income](../../assets/micro-viz/en/uncertainty/utility_of_income.svg){ .ev-figure-lg }

### Risk premium

Setting: concave utility.

![Risk premium](../../assets/micro-viz/en/uncertainty/risk_premium.svg){ .ev-figure-sm }

### Risk attitude

Setting: steep and flat.

![Risk attitude](../../assets/micro-viz/en/uncertainty/risk_attitude.svg){ .ev-figure-lg }

### Risk-return choice

Setting: one investor.

![Risk-return choice](../../assets/micro-viz/en/uncertainty/risk_return_choice.svg){ .ev-figure-sm }

### Two investors

Setting: different tangencies.

![Two investors](../../assets/micro-viz/en/uncertainty/risk_return_two_investors.svg){ .ev-figure-sm }

### State claims, fair premium

Setting: full insurance.

![State claims, fair premium](../../assets/micro-viz/en/uncertainty/state_claims_fair.svg){ .ev-figure-sm }

### State claims, unfair premium

Setting: partial insurance.

![State claims, unfair premium](../../assets/micro-viz/en/uncertainty/state_claims_unfair.svg){ .ev-figure-sm }

### First-order dominance

Setting: CDF comparison.

![First-order dominance](../../assets/micro-viz/en/uncertainty/first_order_dominance.svg){ .ev-figure-sm }

### Second-order dominance

Setting: integrated CDF.

![Second-order dominance](../../assets/micro-viz/en/uncertainty/second_order_dominance.svg){ .ev-figure-sm }

### Mean-variance frontier

Setting: two assets.

![Mean-variance frontier](../../assets/micro-viz/en/uncertainty/mean_variance_frontier.svg){ .ev-figure-sm }

### Borrowing

Setting: beyond the market portfolio.

![Borrowing](../../assets/micro-viz/en/uncertainty/risk_return_borrowing.svg){ .ev-figure-sm }

## Auctions

```bash
uv run python examples/scripts/auctions.py --output-dir out
```

### Bid functions

Setting: first and second price.

![Bid functions](../../assets/micro-viz/en/auctions/bid_functions.svg){ .ev-figure-sm }

### Bid shading

Setting: by number of bidders.

![Bid shading](../../assets/micro-viz/en/auctions/bid_functions_by_bidders.svg){ .ev-figure-sm }

### Revenue equivalence

Setting: expected revenue.

![Revenue equivalence](../../assets/micro-viz/en/auctions/revenue_equivalence.svg){ .ev-figure-sm }

## Information

```bash
uv run python examples/scripts/information.py --output-dir out
```

### Pooling signal

Setting: cheap signal.

![Pooling signal](../../assets/micro-viz/en/information/pooling.svg){ .ev-figure-lg }

### Lemons market

Setting: two shares.

![Lemons market](../../assets/micro-viz/en/information/lemons.svg){ .ev-figure-lg }

### Signaling

Setting: separating signal.

![Signaling](../../assets/micro-viz/en/information/signaling.svg){ .ev-figure-lg }

### Moral hazard

Setting: insurance.

![Moral hazard](../../assets/micro-viz/en/information/moral_hazard.svg){ .ev-figure-sm }

### Bonus schedule

Setting: truthful report.

![Bonus schedule](../../assets/micro-viz/en/information/bonus_schedule.svg){ .ev-figure-sm }

### Efficiency wage

Setting: no-shirking constraint.

![Efficiency wage](../../assets/micro-viz/en/information/efficiency_wage.svg){ .ev-figure-sm }
