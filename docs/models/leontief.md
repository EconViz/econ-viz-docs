# Leontief (Perfect Complements)

$$U(x, y) = \min(ax, by)$$

Goods are consumed in fixed proportions. Indifference curves are L-shaped with a kink along the ray $y = \tfrac{a}{b} x$.

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `a` | float | 1.0 | Coefficient on good x |
| `b` | float | 1.0 | Coefficient on good y |

## Usage

```python
from econ_viz.models import Leontief

model = Leontief(a=1.0, b=2.0)   # U = min(x, 2y)
```

## Equilibrium

The optimum always sits at the kink vertex where $ax = by$, intersected with the budget line:

$$x^* = \frac{I}{p_x + p_y \cdot \tfrac{a}{b}}, \quad y^* = \frac{a}{b} \cdot x^*$$

```python
from econ_viz import solve

eq = solve(Leontief(a=1.0, b=2.0), px=2.0, py=3.0, income=30.0)
```

## Full example

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import Leontief

model = Leontief(a=1.0, b=1.0)
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

Canvas(x_max=20, y_max=15, title=r"Leontief $\min(x, y)$") \
    .add_utility(model, levels=lvls, show_rays=True, show_kinks=True) \
    .add_budget(2.0, 3.0, 30.0) \
    .add_equilibrium(eq) \
    .save("leontief.png")
```

## CLI

```bash
econ-viz plot --model leontief --a 1 --b 1 \
              --px 2 --py 3 --income 30 --output leontief.png
```
