# CES (Constant Elasticity of Substitution)

$$U(x, y) = \left(\alpha x^\rho + \beta y^\rho\right)^{1/\rho}$$

The elasticity of substitution is $\sigma = 1 / (1 - \rho)$. CES nests several special cases:

| $\rho$ | Limit | Equivalent to |
|--------|-------|---------------|
| $\rho \to 0$ | $x^\alpha y^\beta$ | Cobb-Douglas |
| $\rho \to -\infty$ | $\min(\alpha x, \beta y)$ | Leontief |
| $\rho = 1$ | $\alpha x + \beta y$ | Perfect Substitutes |

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `alpha` | float | 0.5 | Share parameter for good x |
| `beta` | float | 0.5 | Share parameter for good y |
| `rho` | float | 0.5 | Substitution parameter (must not equal 1) |

## Usage

```python
from econ_viz.models import CES

model = CES(rho=-0.5, alpha=0.5, beta=0.5)   # elasticity σ = 1/(1+0.5) = 0.667
```

## Full example

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import CES

model = CES(rho=-0.5, alpha=0.5)
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

Canvas(x_max=20, y_max=15, title=r"CES $\rho = -0.5$") \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0) \
    .add_equilibrium(eq) \
    .save("ces.png")
```

## CLI

```bash
econ-viz plot --model ces --rho -0.5 --alpha 0.5 \
              --px 2 --py 3 --income 30 --output ces.png
```
