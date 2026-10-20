---
seo_title: "动画"
---

# 动画

<span id="sec-animation"></span>

`Animator` 根据指定的参数序列调用绘图函数，将返回的 `Canvas` 或 `Figure` 导出为 GIF。使用前需安装 `animation` 可选依赖（详见[可选依赖](../getting-started/installation.md#sec-extras)）。从 `utility_viz.core.animation` 导入；1.x 为 `econ_viz.animation`。

<!-- api: agora.utility_viz.guides_animation_1 -->

依次将 `frames` 的值传入 `draw`，每次返回的图形对应一个帧。

- `save()` 使用 `Pillow`，不需要 `ffmpeg`。
- 导出前将帧合成至白色背景，避免残影。
- `fps`、`dpi` 与 `loop` 分别设置帧率、分辨率与循环次数。

```python
import numpy as np

from utility_viz import Canvas, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas


def draw(px: float) -> Canvas:
    model = CobbDouglas(alpha=0.5, beta=0.5)
    eq = solve(model, px=px, py=2.0, income=20.0)
    lvls = levels.around(eq.utility, n=5)

    return (
        Canvas(
            x_max=14,
            y_max=12,
            x_label="X_1",
            y_label="X_2",
            title="Price sweep",
        )
        .add_utility(model, levels=lvls)
        .add_budget(px=px, py=2.0, income=20.0, fill=True)
        .add_equilibrium(eq, show_ray=True, drop_dashes=True)
    )


Animator(draw, frames=np.linspace(1.0, 6.0, 45)).save(
    "price_sweep.gif",
    fps=12,
    dpi=120,
)
```

`examples/scripts/animation.py` 提供四种示例 (各示例均包含 Cobb-Douglas、CES、完全替代与完全互补模型。)：

- 参数变动：固定价格与收入，调整效用函数参数。
- 价格变动：固定效用函数与 $p_y$，调整 $p_x$，呈现预算线旋转，写法见上例。
- 收入变动：固定效用函数与价格，调整收入，呈现预算线平移。
- 预算线变动：仅显示预算线，省略效用图层。

四种示例的差异只在于 `draw()` 每次固定哪些值、调整哪个值。以参数变动为例，将上例的 `draw()` 改为接收 `alpha`，价格固定为 $p_x = 2$：

```python
def draw(alpha: float) -> Canvas:
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    eq = solve(model, px=2.0, py=2.0, income=20.0)
    ...


Animator(draw, frames=np.linspace(0.1, 0.9, 45)).save(
    "parameter_sweep.gif"
)
```

收入变动将 `draw()` 的参数改为 `income`，并把该值传入 `add_budget()` 与 `solve()`。只呈现预算线时，省略 `add_utility()` 与 `add_equilibrium()`。

[参数变动](animation.md#fig-sweep-param)至[收入变动](animation.md#fig-sweep-income)各节录四个帧。

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

# 图形设置
Config.load("manual.toml").use()


def draw(alpha: float) -> Canvas:
    """一格影格：x 的权重是 alpha，y 的权重是 1 - alpha。"""
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    eq = solve(model, px=2.0, py=2.0, income=20.0)
    cvs = Canvas(
        x_max=14, y_max=12, x_label="$x_1$", y_label="$x_2$"
    )
    cvs.add_utility(
        model, levels=levels.around(eq.utility, n=5)
    )
    cvs.add_budget(2.0, 2.0, 20.0, fill=True)
    cvs.add_equilibrium(eq, show_ray=True)
    return cvs


Animator(draw, frames=np.linspace(0.1, 0.9, 45)).save(
    "parameter_sweep.gif", fps=12, dpi=120
)
```

<span id="fig-sweep-param"></span>

<figure class="ev-fig" markdown>

![参数变动](../../../assets/utility-viz/agora/animation/parameter_sweep.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/animation/parameter_sweep.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a><a class="ev-download" href="../../../assets/utility-viz/agora/animation/parameter_sweep.svg" download aria-label="下载图片"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v14H4zM4 16l5-5 4 4 3-3 4 4M15 9.5h.01" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载图片</span></a></div>

<figcaption markdown>参数变动</figcaption>

</figure>

下面每张图取 GIF 的四个帧，GIF 共 45 帧。

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

# 图形设置
Config.load("manual.toml").use()

model = CobbDouglas(alpha=0.5, beta=0.5)
# 每帧用同一组曲线
fixed = levels.around(
    solve(model, px=2.0, py=2.0, income=20.0).utility, n=5
)


def draw(px: float) -> Canvas:
    """一格影格：x 的价格是 px。"""
    eq = solve(model, px=px, py=2.0, income=20.0)
    cvs = Canvas(
        x_max=14, y_max=12, x_label="$x_1$", y_label="$x_2$"
    )
    cvs.add_utility(model, levels=fixed)
    cvs.add_budget(px, 2.0, 20.0, fill=True)
    cvs.add_equilibrium(eq, show_ray=True)
    return cvs


Animator(draw, frames=np.linspace(1.0, 6.0, 45)).save(
    "price_sweep.gif", fps=12, dpi=120
)
```

<span id="fig-sweep-price"></span>

<figure class="ev-fig" markdown>

![价格变动](../../../assets/utility-viz/agora/animation/price_sweep.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/animation/price_sweep.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a><a class="ev-download" href="../../../assets/utility-viz/agora/animation/price_sweep.svg" download aria-label="下载图片"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v14H4zM4 16l5-5 4 4 3-3 4 4M15 9.5h.01" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载图片</span></a></div>

<figcaption markdown>价格变动</figcaption>

</figure>

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

# 图形设置
Config.load("manual.toml").use()

model = CobbDouglas(alpha=0.5, beta=0.5)
# 每帧用同一组曲线
fixed = levels.around(
    solve(model, px=2.0, py=2.0, income=20.0).utility, n=5
)


def draw(income: float) -> Canvas:
    """一格影格：所得是 income。"""
    eq = solve(model, px=2.0, py=2.0, income=income)
    cvs = Canvas(
        x_max=14, y_max=12, x_label="$x_1$", y_label="$x_2$"
    )
    cvs.add_utility(model, levels=fixed)
    cvs.add_budget(2.0, 2.0, income, fill=True)
    cvs.add_equilibrium(eq, show_ray=True)
    return cvs


Animator(draw, frames=np.linspace(8.0, 36.0, 45)).save(
    "income_sweep.gif", fps=12, dpi=120
)
```

<span id="fig-sweep-income"></span>

<figure class="ev-fig" markdown>

![收入变动](../../../assets/utility-viz/agora/animation/income_sweep.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/animation/income_sweep.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a><a class="ev-download" href="../../../assets/utility-viz/agora/animation/income_sweep.svg" download aria-label="下载图片"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5h16v14H4zM4 16l5-5 4 4 3-3 4 4M15 9.5h.01" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载图片</span></a></div>

<figcaption markdown>收入变动</figcaption>

</figure>

## 动画图库

以下 GIF 由文档仓库的 `scripts/animation_figures.py` 依 `manual.toml` 的设置画成，涵盖同样四种动画：参数、价格、收入与只有预算线。

### 参数变动

改变效用函数的参数，观察偏好图的形状如何随之改变。

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../../../assets/animation/parameter_sweeps/cobb_douglas_parameter_sweep.gif" alt="Cobb-Douglas 参数变动 GIF">
    <figcaption>改变 \(\alpha\)，并令 \(\beta = 1 - \alpha\)</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../../../assets/animation/parameter_sweeps/ces_parameter_sweep.gif" alt="CES 参数变动 GIF">
    <figcaption>改变 \(\rho\)，调整曲率与替代程度</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全替代</span>
    <img src="../../../../assets/animation/parameter_sweeps/perfect_substitutes_parameter_sweep.gif" alt="完全替代参数变动 GIF">
    <figcaption>固定 \(b\)，改变 \(a\)</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全互补</span>
    <img src="../../../../assets/animation/parameter_sweeps/leontief_parameter_sweep.gif" alt="完全互补参数变动 GIF">
    <figcaption>固定 \(b\)，改变 \(a\)，让折点的路径移动</figcaption>
  </figure>
      </td>
    </tr>
  </tbody>
</table>

### 价格变动

固定效用函数与背景无差异曲线的效用水平，只改变一种商品的价格，呈现预算线旋转时的均衡路径。

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../../../assets/animation/price_sweeps/cobb_douglas_price_sweep.gif" alt="Cobb-Douglas 价格变动 GIF">
    <figcaption>价格变动，\(p_y\) 固定</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../../../assets/animation/price_sweeps/ces_price_sweep.gif" alt="CES 价格变动 GIF">
    <figcaption>价格变动，效用曲面固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全替代</span>
    <img src="../../../../assets/animation/price_sweeps/perfect_substitutes_price_sweep.gif" alt="完全替代价格变动 GIF">
    <figcaption>预算线旋转</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全互补</span>
    <img src="../../../../assets/animation/price_sweeps/leontief_price_sweep.gif" alt="完全互补价格变动 GIF">
    <figcaption>价格变动，直角无差异曲线固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">只有预算线</span>
    <img src="../../../../assets/animation/price_sweeps/budget_only_price_sweep.gif" alt="只有预算线的价格变动 GIF">
    <figcaption>价格变动，单独呈现限制式的旋转</figcaption>
  </figure>
      </td>
      <td class="gif-table__empty" aria-hidden="true"></td>
    </tr>
  </tbody>
</table>

### 收入变动

固定效用函数与价格，只改变收入，呈现预算线平行移动时的均衡路径。

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../../../assets/animation/income_sweeps/cobb_douglas_income_sweep.gif" alt="Cobb-Douglas 收入变动 GIF">
    <figcaption>收入变动，价格固定</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../../../assets/animation/income_sweeps/ces_income_sweep.gif" alt="CES 收入变动 GIF">
    <figcaption>收入变动，价格与效用函数固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全替代</span>
    <img src="../../../../assets/animation/income_sweeps/perfect_substitutes_income_sweep.gif" alt="完全替代收入变动 GIF">
    <figcaption>收入变动</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全互补</span>
    <img src="../../../../assets/animation/income_sweeps/leontief_income_sweep.gif" alt="完全互补收入变动 GIF">
    <figcaption>收入变动，价格固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">只有预算线</span>
    <img src="../../../../assets/animation/income_sweeps/budget_only_income_sweep.gif" alt="只有预算线的收入变动 GIF">
    <figcaption>收入变动，单独呈现限制式的平行移动</figcaption>
  </figure>
      </td>
      <td class="gif-table__empty" aria-hidden="true"></td>
    </tr>
  </tbody>
</table>
