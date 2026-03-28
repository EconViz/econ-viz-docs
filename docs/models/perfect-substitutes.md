# Perfect Substitutes

$$U(x, y) = ax + by$$

Goods are perfect substitutes with a constant MRS of $a/b$. Indifference curves are straight lines with slope $-a/b$.

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `a` | float | 1.0 | Marginal utility of good x |
| `b` | float | 1.0 | Marginal utility of good y |

## Usage

```python
from econ_viz.models import PerfectSubstitutes

model = PerfectSubstitutes(a=1.0, b=2.0)   # U = x + 2y
```

## Equilibrium

The solution is always a corner — the consumer spends everything on whichever good offers higher utility per dollar:

- If $a / p_x > b / p_y$: buy only x → $x^* = I / p_x,\; y^* = 0$
- If $a / p_x < b / p_y$: buy only y → $x^* = 0,\; y^* = I / p_y$

```python
from econ_viz import solve

eq = solve(PerfectSubstitutes(a=1.0, b=2.0), px=2.0, py=3.0, income=30.0)
print(eq.bundle_type)   # "corner"
```

## Full example

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import PerfectSubstitutes

model = PerfectSubstitutes(a=1.0, b=2.0)
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

Canvas(x_max=20, y_max=15, title=r"Perfect Substitutes $x + 2y$") \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0) \
    .add_equilibrium(eq) \
    .save("perfect_substitutes.png")
```

## CLI

```bash
econ-viz plot --model perfect-substitutes --a 1 --b 2 \
              --px 2 --py 3 --income 30 --output ps.png
```
