# Quick Start

## Minimal example

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

cvs = Canvas(x_max=20, y_max=15, x_label="x", y_label="y",
             title=r"Cobb-Douglas $x^{0.5} y^{0.5}$")
cvs.add_utility(model, levels=lvls)
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq, show_ray=True)
cvs.save("cobb_douglas.png")
```

## Step by step

### 1. Choose a model

Pick a utility function from `econ_viz.models`. See the [Model catalogue](models/index.md) for the full list.

```python
from econ_viz.models import CobbDouglas
model = CobbDouglas(alpha=0.5, beta=0.5)
```

### 2. Solve for the equilibrium

`solve()` returns an `Equilibrium` named tuple with fields `x`, `y`, `utility`, and `bundle_type`.

```python
from econ_viz import solve
eq = solve(model, px=2.0, py=3.0, income=30.0)
print(eq.x, eq.y, eq.utility)   # e.g. 7.5  5.0  5.303
```

### 3. Choose indifference-curve levels

```python
from econ_viz import levels
lvls = levels.around(eq.utility, n=5)   # 5 curves centred on the optimum
```

### 4. Build the canvas

```python
from econ_viz import Canvas
cvs = Canvas(x_max=20, y_max=15)
```

### 5. Add layers

`Canvas` methods return `self`, so calls can be chained:

```python
cvs.add_utility(model, levels=lvls)
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq, show_ray=True)
```

### 6. Export

```python
cvs.save("figure.png")    # raster
cvs.save("figure.tikz")   # TikZ source for LaTeX
```

Call `cvs.show()` instead to open an interactive window.

## Using the LaTeX parser

```python
from econ_viz import parse_latex, Canvas, levels, solve

model = parse_latex(r"x^{0.4} y^{0.6}")
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

Canvas(x_max=20, y_max=15) \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0) \
    .add_equilibrium(eq) \
    .save("figure.png")
```
