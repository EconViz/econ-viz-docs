---
seo_title: "Custom and Advanced Utility Models"
description: "Build custom utility functions and multi-good Cobb-Douglas models with econ-viz."
---

# Advanced Models

Advanced models extend the built-in utility families with user-defined
functions or more than two goods.

## Extensible models

Use these models when a predefined two-good utility class is not enough.

=== "Custom Utility"

    `CustomUtility` wraps any vectorised Python callable as an econ-viz model.

    $$
    U(x,y)=\ln x+\ln y
    $$

    The equation above is one example. The callable must accept two NumPy
    arrays and return an array with the same shape.

    **Parameters**

    | Parameter | Meaning |
    |-----------|---------|
    | `func` | Vectorised utility function of $x$ and $y$ |
    | `name` | Display name for the custom model |

    **Example**

    ```python
    import numpy as np
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import CustomUtility

    model = CustomUtility(
        func=lambda x, y: np.log(x) + np.log(y),
        name="log+log",
    )
    eq = solve(model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=20, y_max=15, title="Custom Utility")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(2.0, 3.0, 30.0)
        .add_equilibrium(eq)
        .save("custom.png")
    )
    ```

    ![Custom utility indifference map](../assets/advanced/advanced_custom.png)

=== "Multi-Good Cobb-Douglas"

    `MultiGoodCD` represents Cobb-Douglas preferences over $N$ goods.

    $$
    U(x_1,\ldots,x_N)=\prod_{i=1}^{N}x_i^{\alpha_i}
    $$

    `freeze()` fixes every good except $x$ and $y$, then returns a
    `CustomUtility` that can be drawn on a two-dimensional canvas.

    **Parameters**

    | Parameter | Meaning |
    |-----------|---------|
    | `shares` | Mapping from each good name to its exponent $\alpha_i$ |
    | `freeze(...)` | Fixed quantities for goods other than $x$ and $y$ |

    **Example**

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import MultiGoodCD

    model = MultiGoodCD({"x": 0.3, "y": 0.3, "z": 0.4})
    two_good_model = model.freeze(z=10.0)
    eq = solve(two_good_model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=20, y_max=15, title="Multi-Good Cobb-Douglas")
        .add_utility(
            two_good_model,
            levels=levels.around(eq.utility, n=5),
        )
        .add_budget(2.0, 3.0, 30.0, fill=True)
        .add_equilibrium(eq)
        .save("multigood.png")
    )
    ```

    ![Multi-good Cobb-Douglas projection](../assets/advanced/advanced_multigd.png)
