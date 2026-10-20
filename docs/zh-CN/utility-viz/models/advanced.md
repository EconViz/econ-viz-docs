---
seo_title: "进阶模型"
---

# 进阶模型

<span id="sec-advanced"></span>

`CustomUtility` 定义二元效用函数。`MultiGoodCD` 表示多商品 Cobb-Douglas；固定其他商品的数量后，可将模型投影为二维图。

### 自定义效用函数

<!-- api: agora.utility_viz.models_advanced_1 -->

接受向量化的 Python 函数，返回的模型可用于 `solve()` 与 `Canvas`。函数须接受两个 `NumPy` 数组，并返回相同形状的效用数组。以下以对数效用为例：

$$
u(x, y) = ln x + ln y.
$$

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import CustomUtility

# 图形设置
Config.load("manual.toml").use()

# 任何数组函数都可作效用
model = CustomUtility(
    func=lambda x, y: np.log(x) + np.log(y), name="log+log"
)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("custom.png")
```

<figure class="ev-fig" markdown>

![对数自定义模型](../../../assets/utility-viz/agora/models/custom.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/custom.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>对数自定义模型</figcaption>

</figure>

### 多商品 Cobb-Douglas

<!-- api: agora.utility_viz.models_advanced_2 -->

`MultiGoodCD` 表示 $N$ 种商品的 Cobb-Douglas：

$$
u(x_1, ..., x_N) = product_{i=1}^N x_i^{\alpha_i}.
$$

使用 `freeze()` 固定 $x$、$y$ 以外的商品数量，返回可用于二维 `Canvas` 的 `CustomUtility`。

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import MultiGoodCD

# 图形设置
Config.load("manual.toml").use()

# 三种商品 固定 z = 10
model = MultiGoodCD({"x": 0.3, "y": 0.3, "z": 0.4})
two_good_model = model.freeze(z=10.0)
eq = solve(two_good_model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(
    two_good_model, levels=levels.around(eq.utility, n=5)
)
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("multigood.png")
```

<figure class="ev-fig" markdown>

![三商品固定 $z=10$](../../../assets/utility-viz/agora/models/multigood.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/multigood.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>三商品固定 $z=10$</figcaption>

</figure>

### 与后端无关的场景

<span id="sec-scenes"></span>

`utility_viz.core.scenes` 生成与 `Canvas` 相同的经济元素，但输出为不可变的 `mosaickit` 图层，而非直接绘制在 `matplotlib` 坐标轴上。每个图层都有固定的 id（`budget`、`budget.fill`、`equilibrium.drop`、`ic.2` 等）与以点分隔的主题角色（`utility.budget`、`utility.indifference.secondary` 等），因此场景可供检查、修改，并交由任何 `mosaickit` 后端渲染。这是额外添加的高级 API，`Canvas` 与其他图形不受影响。

<!-- api: agora.utility_viz.models_advanced_3 -->

分别返回预算线 $p_x x + p_y y = I$、均衡消费组合，以及模型在 $[0, x_{\max}] \times [0, y_{\max}]$ 范围内无差异曲线的图层 tuple。样式来自主题角色，也可传入部分字段的 `Stroke`、`Marker` 与 `Fill` 覆盖。`indifference_layers` 返回 `(layers, levels)`，并以 `bezierkit` 将曲线描成 Bézier 路径，因此也能处理非单调与有折角的效用函数。

<!-- api: agora.utility_viz.models_advanced_4 -->

`UTILITY_THEME` 是含 `utility.*` 角色的 `mosaickit` 主题，配色与默认主题相同。`canvas_to_tikz(canvas)` 将场景导出为 TikZ，曲线使用原生的 `.. controls ..` 语法。

```python
from mosaickit import Canvas, CanvasSpec, quadrant_axes

from utility_viz.core.scenes import (
    UTILITY_THEME,
    budget_layers,
    canvas_to_tikz,
    equilibrium_layers,
    indifference_layers,
)
from utility_viz.models import CobbDouglas, solve

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)
u = eq.utility
ic, _ = indifference_layers(
    model, [0.6 * u, u, 1.4 * u], 18, 12
)

spec = CanvasSpec(x_range=(0, 18), y_range=(0, 12))
canvas = (
    Canvas(spec, theme=UTILITY_THEME)
    .extend(quadrant_axes(18, 12))
    .extend(ic)
    .extend(budget_layers(2.0, 3.0, 30.0, fill=True))
    .extend(equilibrium_layers(eq))
)
canvas.save("scene.png")
tex = canvas_to_tikz(canvas)
```

TikZ 导出支持路径、填充、标记与文本图层。描绘的效用函数在绘图范围内必须为有限值。
