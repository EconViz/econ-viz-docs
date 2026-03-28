# Cobb-Douglas

$$U(x, y) = x^\alpha \cdot y^\beta$$

The most common textbook utility function. Indifference curves are smooth, strictly convex, and asymptotic to both axes.

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `alpha` | float | 0.5 | Output elasticity of good x |
| `beta` | float | 0.5 | Output elasticity of good y |

## Usage

```python
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.3, beta=0.7)
```

## Equilibrium

The interior optimum satisfies the tangency condition MRS = price ratio. With a budget $p_x x + p_y y = I$:

$$x^* = \frac{\alpha}{\alpha + \beta} \cdot \frac{I}{p_x}, \quad y^* = \frac{\beta}{\alpha + \beta} \cdot \frac{I}{p_y}$$

```python
from econ_viz import solve

eq = solve(CobbDouglas(alpha=0.3, beta=0.7), px=2.0, py=3.0, income=30.0)
```

## Full example

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

Canvas(x_max=20, y_max=15, title=r"Cobb-Douglas $x^{0.5} y^{0.5}$") \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq, show_ray=True) \
    .save("cobb_douglas.png")
```

## CLI

```bash
econ-viz plot --model cobb-douglas --alpha 0.5 --beta 0.5 \
              --px 2 --py 3 --income 30 --output cobb_douglas.png
```
