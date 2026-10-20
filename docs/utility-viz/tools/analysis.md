---
seo_title: "Analysis"
---

# Analysis

<span id="sec-analysis"></span>

The analysis API provides comparative statics of Marshallian demand, the
Slutsky matrix, and checks for homogeneity and homotheticity of utility
functions.

## Comparative statics

<!-- api: agora.utility_viz.tools_analysis_1 -->

Estimate the six partial derivatives of two-good Marshallian demand with
respect to $p_x$, $p_y$ and income by finite differences, returned as a
`ComparativeStatics`.

- Central finite differences around `solve(...)`, with a default
  relative step of `1e-3`.
- Warns when the own-price derivative is positive or the income
  derivative negative, the signatures of Giffen and inferior goods.

```python
from utility_viz import comparative_statics
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.4, beta=0.6)
cs = comparative_statics(model, px=2.0, py=3.0, income=60.0)

print(round(cs.dx_dpx, 1), round(cs.dx_dpy, 1), round(cs.dx_dI, 1))
print(round(cs.dy_dpx, 1), round(cs.dy_dpy, 1), round(cs.dy_dI, 1))

# -6.0 0.0 0.2
# 0.0 -4.0 0.2
```

## Slutsky matrix

<!-- api: agora.utility_viz.tools_analysis_2 -->

The two-good Slutsky substitution matrix, computed from Marshallian
demand derivatives and income effects. The result checks
symmetry, negative semidefiniteness and homogeneity, and warns when a
condition fails. `as_array()` returns it as a `NumPy` array.

```python
from utility_viz import slutsky_matrix
from utility_viz.models import CobbDouglas

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

## Homogeneity

<!-- api: agora.utility_viz.tools_analysis_3 -->

Check homogeneity and homotheticity of a utility function, and
degree-zero homogeneity of demand.

```python
from utility_viz.models import CobbDouglas, HomogeneityAnalyzer

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

<span id="sec-rts"></span>

`degree()` returns a `HomogeneityResult` with these fields:

For Cobb-Douglas utility the degree is $\alpha + \beta$:

$$
u(\lambda x, \lambda y) = \lambda^{\alpha + \beta} u(x, y).
$$

<!-- api: agora.utility_viz.tools_analysis_4 -->

The returns-to-scale class of a function.

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
