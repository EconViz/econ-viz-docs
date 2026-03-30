# Translog

`Translog` adds a flexible log-quadratic utility specification that can approximate a wide range of smooth preferences.

```python
from econ_viz.models import Translog

model = Translog(
    alpha_x=0.5,
    alpha_y=0.5,
    beta_xx=0.1,
    beta_yy=-0.05,
    beta_xy=0.08,
)
```

## Functional form

```text
ln U(x, y) = alpha_0
           + alpha_x ln x + alpha_y ln y
           + 0.5 beta_xx (ln x)^2
           + 0.5 beta_yy (ln y)^2
           + beta_xy ln x ln y
```

The implementation returns:

```text
U(x, y) = exp(ln U(x, y))
```

Setting `beta_xx = beta_yy = beta_xy = 0` collapses the model to a Cobb-Douglas-style log-linear form.

## Parameters

| Parameter | Default | Meaning |
|-----------|---------|---------|
| `alpha_x` | `0.5` | First-order coefficient on `ln x` |
| `alpha_y` | `0.5` | First-order coefficient on `ln y` |
| `beta_xx` | `0.0` | Second-order own effect for `ln x` |
| `beta_yy` | `0.0` | Second-order own effect for `ln y` |
| `beta_xy` | `0.0` | Cross term `ln x ln y` |
| `alpha_0` | `0.0` | Log-utility intercept |

`alpha_x` and `alpha_y` must be strictly positive.

## Properties

- `utility_type` is `UtilityType.SMOOTH`
- works with `Canvas.add_utility(...)`
- works with `solve(...)` through the library's numerical optimisation path

## Example

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import Translog

model = Translog(alpha_x=0.6, alpha_y=0.4, beta_xy=0.12)
eq = solve(model, px=2.0, py=3.0, income=30.0)
lvls = levels.around(eq.utility, n=4)

Canvas(x_max=18, y_max=12, title="Translog utility") \
    .add_utility(model, levels=lvls, label="$U$") \
    .add_budget(2.0, 3.0, 30.0, label="$B$") \
    .add_equilibrium(eq) \
    .show_legend()
```
