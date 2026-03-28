# Satiation (Bliss Point)

$$U(x, y) = -a(x - x^*)^2 - b(y - y^*)^2$$

Utility rises toward the bliss point $(x^*, y^*)$ and falls away in all directions. Indifference curves are closed ellipses centred on the bliss point. This violates the standard monotonicity axiom — a consumer can have "too much" of a good.

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `bliss_x` | float | 5.0 | x-coordinate of the bliss point $x^*$ |
| `bliss_y` | float | 5.0 | y-coordinate of the bliss point $y^*$ |
| `a` | float | 1.0 | Curvature along the x-axis (must be positive) |
| `b` | float | 1.0 | Curvature along the y-axis (must be positive) |

## Usage

```python
from econ_viz.models import Satiation

model = Satiation(bliss_x=6.0, bliss_y=4.0, a=1.0, b=1.0)
```

## Full example

```python
from econ_viz import Canvas, levels
from econ_viz.models import Satiation
import numpy as np

model = Satiation(bliss_x=6.0, bliss_y=4.0)

x_pts = np.linspace(0.1, 12, 300)
y_pts = np.linspace(0.1, 10, 300)
X, Y  = np.meshgrid(x_pts, y_pts)
lvls  = levels.percentile(model(X, Y), n=5)

Canvas(x_max=12, y_max=10, title="Satiation — bliss at $(6, 4)$") \
    .add_utility(model, levels=lvls) \
    .save("satiation.png")
```

## CLI

```bash
econ-viz plot --model satiation --bliss-x 6 --bliss-y 4 \
              --x-max 12 --y-max 10 \
              --no-budget --no-equilibrium \
              --output satiation.png
```

!!! note
    `Satiation` is not compatible with `solve()` because the standard budget-tangency optimum may lie outside the bliss ellipse. Use `--no-budget --no-equilibrium` in the CLI, or omit `add_budget` / `add_equilibrium` in Python.
