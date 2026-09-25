---
seo_title: "Comparative Statics and Slutsky Analysis"
description: "Compute comparative statics, Marshallian demand derivatives, and Slutsky decompositions numerically with econ-viz analysis helpers."
---

# Analysis

`econ-viz` now includes analysis helpers beyond plotting and equilibrium solving.

## Comparative statics

Use `comparative_statics(...)` to estimate the six Marshallian demand derivatives numerically:

```python
from econ_viz.models import CobbDouglas
from econ_viz.optimizer import comparative_statics

model = CobbDouglas(alpha=0.4, beta=0.6)
cs = comparative_statics(model, px=2.0, py=3.0, income=60.0)

print(round(cs.dx_dpx, 1), round(cs.dx_dpy, 1), round(cs.dx_dI, 1))
print(round(cs.dy_dpx, 1), round(cs.dy_dpy, 1), round(cs.dy_dI, 1))

# -6.0 0.0 0.2
# 0.0 -4.0 0.2
```

Notes:

- Uses central finite differences around `solve(...)`
- Default relative step size is `1e-3`
- Emits warnings for economically unusual sign patterns such as Giffen-style own-price responses or inferior-good income effects

## Slutsky matrix

Use `slutsky_matrix(...)` to compute the two-good substitution matrix implied by the Slutsky equation.

```python
from econ_viz import slutsky_matrix
from econ_viz.models import CobbDouglas

S = slutsky_matrix(
    CobbDouglas(alpha=0.4, beta=0.6),
    px=2.0, py=3.0, income=60.0,
)

print(round(S.s_xx, 1), round(S.s_xy, 1))
print(round(S.s_yx, 1), round(S.s_yy, 1))
print(S.as_array().round(1))

# -3.6 2.4
# 2.4 -1.6
# [[-3.6  2.4]
#  [ 2.4 -1.6]]
```

Use this when you want compensated price effects rather than just the raw Marshallian derivatives.

## Homogeneity analysis

Use `HomogeneityAnalyzer` to study whether a utility function is homogeneous or homothetic.

### Available checks

The analyzer provides four checks:

- `degree()` estimates the homogeneity degree
- `euler_check(x, y)` evaluates the Euler-theorem residual at a bundle
- `is_homothetic()` checks whether MRS is invariant to proportional scaling
- `demand_degree_zero(px, py, income)` verifies Marshallian demand homogeneity of degree 0

### Example

```python
from econ_viz.analysis import HomogeneityAnalyzer
from econ_viz.models import CobbDouglas

analyzer = HomogeneityAnalyzer(CobbDouglas(alpha=0.4, beta=0.6))
result = analyzer.degree()

print(round(result.degree, 6))
print(result.returns_to_scale)
print(round(analyzer.euler_check(3.0, 4.0), 6))
print(analyzer.is_homothetic())
print(analyzer.demand_degree_zero(px=2.0, py=3.0, income=60.0))

# 1.0
# ReturnsToScale.CONSTANT
# 0.0
# True
# True
```

## Returns to scale

`degree()` returns a `HomogeneityResult` carrying both the estimated degree and a `ReturnsToScale` classification:

For a Cobb–Douglas utility, the degree is $\alpha+\beta$:

$$
U(\lambda x, \lambda y)
= \lambda^{\alpha+\beta} U(x,y)
$$

- $\alpha+\beta>1$: `INCREASING`
- $\alpha+\beta=1$: `CONSTANT`
- $\alpha+\beta<1$: `DECREASING`

Functions without a consistent homogeneity degree are classified as
`NOT_HOMOGENEOUS`.

### Classification example

```python
def shifted_utility(x, y):
    return x**0.4 * y**0.6 + 1.0


models = [
    CobbDouglas(alpha=0.7, beta=0.6),
    CobbDouglas(alpha=0.4, beta=0.6),
    CobbDouglas(alpha=0.2, beta=0.5),
    shifted_utility,
]

for model in models:
    result = HomogeneityAnalyzer(model).degree()
    degree = None if result.degree is None else round(result.degree, 1)
    print(degree, result.returns_to_scale.name)

# 1.3 INCREASING
# 1.0 CONSTANT
# 0.7 DECREASING
# None NOT_HOMOGENEOUS
```
