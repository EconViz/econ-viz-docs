---
seo_title: "自定义与高级效用模型"
description: "在 econ-viz 中把任何 Python 函数包装成自定义效用模型，并画出它的无差异曲线、预算约束与均衡点。"
---

# 高级模型

![自定义效用函数范例](../../assets/advanced/advanced_custom.png)

## 自定义效用函数 {#custom-utility}

把任何向量化的 Python 可调用函数，包装成完整的效用模型。

```python
import numpy as np
from econ_viz.models import CustomUtility

model = CustomUtility(
    func=lambda x, y: np.log(x) + np.log(y),
    name="log+log",
)
```

创建模型时，会用一组随机的 NumPy 网格检查这个函数。它必须接受两个数组参数，并返回形状相同的数组。

### 完整范例

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

## 多商品 Cobb-Douglas {#multi-good-cobb-douglas}

描述 $N$ 种商品的偏好，并把 x 与 y 以外的商品全部固定，投影到 2 维画布上。

```python
from econ_viz.models import MultiGoodCD

m3   = MultiGoodCD({'x': 0.3, 'y': 0.3, 'z': 0.4})
flat = m3.freeze(z=10.0)   # returns a CustomUtility ready for Canvas
```

`freeze()` 接受 `x`、`y` 以外每种商品的关键字参数，把它们固定在给定的数值，并返回一个以 x 和 y 为变量的 `CustomUtility`。

![多商品 Cobb-Douglas 投影范例](../../assets/advanced/advanced_multigd.png)

### 完整范例

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
