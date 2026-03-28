# Advanced Models

## Custom Utility

Wrap any vectorised Python callable as a first-class utility model.

```python
import numpy as np
from econ_viz.models import CustomUtility

model = CustomUtility(
    func=lambda x, y: np.log(x) + np.log(y),
    name="log+log",
)
```

The callable is validated at construction time against a random NumPy meshgrid. It must accept two array arguments and return an array of the same shape.

### Full example

```python
import numpy as np
from econ_viz import Canvas, levels, solve
from econ_viz.models import CustomUtility

model = CustomUtility(func=lambda x, y: np.log(x) + np.log(y), name="log+log")
eq    = solve(model, px=2.0, py=3.0, income=30.0)
lvls  = levels.around(eq.utility, n=5)

Canvas(x_max=20, y_max=15, title="Custom: $\\ln x + \\ln y$") \
    .add_utility(model, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0) \
    .add_equilibrium(eq) \
    .save("custom.png")
```

---

## Multi-Good Cobb-Douglas

Model preferences over $N$ goods and project to a 2-D canvas by freezing all goods except x and y.

```python
from econ_viz.models import MultiGoodCD

m3   = MultiGoodCD({'x': 0.3, 'y': 0.3, 'z': 0.4})
flat = m3.freeze(z=10.0)   # returns a CustomUtility ready for Canvas
```

`freeze()` takes keyword arguments for each good not named `x` or `y`, fixes them at the supplied values, and returns a `CustomUtility` over x and y.

### Full example

```python
from econ_viz import Canvas, levels, solve
from econ_viz.models import MultiGoodCD

m3   = MultiGoodCD({'x': 0.3, 'y': 0.3, 'z': 0.4})
flat = m3.freeze(z=10.0)

eq   = solve(flat, px=2.0, py=3.0, income=30.0)
lvls = levels.around(eq.utility, n=5)

Canvas(x_max=20, y_max=15, title=r"MultiGoodCD $z=10$") \
    .add_utility(flat, levels=lvls) \
    .add_budget(2.0, 3.0, 30.0, fill=True) \
    .add_equilibrium(eq) \
    .save("multigood.png")
```
