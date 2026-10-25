---
seo_title: "Oligopoly and vertical chains"
---

# Oligopoly and vertical chains

<span id="sec-oligopoly"></span>

A few firms, and firms at different stages of one chain.

Each section is one example script and the figures it writes. The scripts are in `examples/scripts/` of the repository; `--help` lists their arguments.

## Duopoly

```bash
uv run python examples/scripts/oligopoly.py --output-dir out
```

### Residual demand

Setting: rival output guesses.

![Residual demand](../../assets/micro-viz/en/oligopoly/residual_demand.svg){ .ev-figure-sm }

### Reaction curves

Setting: Cournot.

![Reaction curves](../../assets/micro-viz/en/oligopoly/cournot.svg){ .ev-figure-sm }

### Competitive, Cournot and collusive

Setting: symmetric.

![Competitive, Cournot and collusive](../../assets/micro-viz/en/oligopoly/cournot_points.svg){ .ev-figure-sm }

### Stackelberg

Setting: firm 1 leads.

![Stackelberg](../../assets/micro-viz/en/oligopoly/stackelberg.svg){ .ev-figure-sm }

### Price reaction curves

Setting: differentiated.

![Price reaction curves](../../assets/micro-viz/en/oligopoly/price_reaction.svg){ .ev-figure-sm }

## Kinked demand, dominant firm and cartel

```bash
uv run python examples/scripts/dominant_firm.py --output-dir out
```

### Kinked demand

Setting: two cost levels.

![Kinked demand](../../assets/micro-viz/en/dominant_firm/kinked_demand.svg){ .ev-figure-sm }

### Dominant firm

Setting: fringe supply.

![Dominant firm](../../assets/micro-viz/en/dominant_firm/dominant_firm.svg){ .ev-figure-sm }

### Cartel with a competitive fringe

Setting: same model.

![Cartel with a competitive fringe](../../assets/micro-viz/en/dominant_firm/cartel_fringe.svg){ .ev-figure-sm }

### Cartel, inelastic and elastic demand

Setting: two panels.

![Cartel, inelastic and elastic demand](../../assets/micro-viz/en/dominant_firm/cartel_elasticity.svg){ .ev-figure-lg }

## Vertical chains

```bash
uv run python examples/scripts/vertical.py --output-dir out
```

### Double marginalization

Setting: stacked monopolies.

![Double marginalization](../../assets/micro-viz/en/vertical/double_marginalization.svg){ .ev-figure-sm }

### Integrated firm

Setting: NMR = MC.

![Integrated firm](../../assets/micro-viz/en/vertical/integrated_firm.svg){ .ev-figure-sm }

### Transfer price, kinked MC

Setting: outside market.

![Transfer price, kinked MC](../../assets/micro-viz/en/vertical/transfer_kinked.svg){ .ev-figure-sm }

### Optimal transfer price

Setting: equals market price.

![Optimal transfer price](../../assets/micro-viz/en/vertical/transfer_price.svg){ .ev-figure-sm }
