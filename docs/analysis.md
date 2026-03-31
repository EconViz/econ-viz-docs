# Analysis

`econ-viz` now includes analysis helpers beyond plotting and equilibrium solving.

![Analysis helpers pair naturally with demand teaching diagrams](assets/consumer/demand_cobb_douglas.png)

## Comparative statics

Use `comparative_statics(...)` to estimate the six Marshallian demand derivatives numerically:

```python
from econ_viz.models import CobbDouglas
from econ_viz.optimizer import comparative_statics

model = CobbDouglas(alpha=0.4, beta=0.6)
cs = comparative_statics(model, px=2.0, py=3.0, income=60.0)

print(cs.dx_dpx, cs.dx_dpy, cs.dx_dI)
print(cs.dy_dpx, cs.dy_dpy, cs.dy_dI)
```

Returned object:

```python
ComparativeStatics(
    dx_dpx=...,
    dx_dpy=...,
    dx_dI=...,
    dy_dpx=...,
    dy_dpy=...,
    dy_dI=...,
)
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

S = slutsky_matrix(CobbDouglas(alpha=0.4, beta=0.6), px=2.0, py=3.0, income=60.0)

print(S.s_xx, S.s_xy)
print(S.s_yx, S.s_yy)
print(S.as_array())
```

Returned object:

```python
SlutskyMatrix(
    s_xx=...,
    s_xy=...,
    s_yx=...,
    s_yy=...,
)
```

Use this when you want compensated price effects rather than just the raw Marshallian derivatives.

## Homogeneity analysis

Use `HomogeneityAnalyzer` to study whether a utility function is homogeneous or homothetic.

```python
from econ_viz.analysis import HomogeneityAnalyzer
from econ_viz.models import CobbDouglas

analyzer = HomogeneityAnalyzer(CobbDouglas(alpha=0.4, beta=0.6))

result = analyzer.degree()
print(result.degree)
print(result.returns_to_scale)
print(analyzer.euler_check(3.0, 4.0))
print(analyzer.is_homothetic())
print(analyzer.demand_degree_zero(px=2.0, py=3.0, income=60.0))
```

### Available checks

- `degree()` estimates the homogeneity degree
- `euler_check(x, y)` evaluates the Euler-theorem residual at a bundle
- `is_homothetic()` checks whether MRS is invariant to proportional scaling
- `demand_degree_zero(px, py, income)` verifies Marshallian demand homogeneity of degree 0

## Returns to scale classification

`degree()` returns a `HomogeneityResult` carrying both the estimated degree and a `ReturnsToScale` classification:

- `INCREASING`
- `CONSTANT`
- `DECREASING`
- `NOT_HOMOGENEOUS`
