---
seo_title: "把经济学图形做成 GIF 动画"
description: "用 econ-viz 的 Animator，把价格、收入或效用参数变动时的无差异曲线与预算约束导出成 GIF 动画。"
---

# 动画

`econ-viz` 提供以 `Animator` 为核心的轻量 GIF 流程。API 跟一般绘图差不多：写一个**frame factory**，每次返回一个新的 `Canvas` 或 `Figure`，再扫过一串数值帧，最后保存为 GIF。

## 安装

```bash
uv add "econ-viz[animation]"
```

如果也要笔记本交互组件，就安装：

```bash
uv add "econ-viz[all]"
```

## 最简范例

```python
import numpy as np

from econ_viz import Canvas, levels, solve
from econ_viz.animation import Animator
from econ_viz.models import CobbDouglas

def draw(px: float) -> Canvas:
    model = CobbDouglas(alpha=0.5, beta=0.5)
    eq = solve(model, px=px, py=2.0, income=20.0)
    lvls = levels.around(eq.utility, n=5)

    return (
        Canvas(
            x_max=14, y_max=12,
            x_label="X_1", y_label="X_2",
            title="Price sweep"
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

## 教学用动画

范例脚本 `examples/animation.py` 会产生以下几类动画：

- **参数变动**：价格与收入固定，只改变效用函数的某个参数。
- **价格变动**：效用函数与 `p_y` 固定，只改变 `p_x`。
- **收入变动**：效用函数与价格固定，只改变收入。
- **只有预算线**：完全拿掉效用图层，让学生专心观察预算线怎么移动。

文文件网站直接嵌入同一批 GIF，所以这里看到的就是本机产生的结果。

## 参数变动

改变效用函数的参数，观察偏好图的形状如何随之改变。

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../assets/animation/parameter_sweeps/cobb_douglas_parameter_sweep.gif" alt="Cobb-Douglas 参数变动 GIF">
    <figcaption>改变 \(\alpha\)，并令 \(\beta = 1 - \alpha\)</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../assets/animation/parameter_sweeps/ces_parameter_sweep.gif" alt="CES 参数变动 GIF">
    <figcaption>改变 \(\rho\)，调整曲率与替代程度</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全替代</span>
    <img src="../../assets/animation/parameter_sweeps/perfect_substitutes_parameter_sweep.gif" alt="完全替代参数变动 GIF">
    <figcaption>固定 \(b\)，改变 \(a\)</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全互补</span>
    <img src="../../assets/animation/parameter_sweeps/leontief_parameter_sweep.gif" alt="完全互补参数变动 GIF">
    <figcaption>固定 \(b\)，改变 \(a\)，让折点的路径移动</figcaption>
  </figure>
      </td>
    </tr>
  </tbody>
</table>

## 价格变动

固定效用函数与背景无差异曲线的效用水平，只改变一种商品的价格，呈现预算线旋转时的均衡路径。

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../assets/animation/price_sweeps/cobb_douglas_price_sweep.gif" alt="Cobb-Douglas 价格变动 GIF">
    <figcaption>价格变动，\(p_y\) 固定</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../assets/animation/price_sweeps/ces_price_sweep.gif" alt="CES 价格变动 GIF">
    <figcaption>价格变动，效用曲面固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全替代</span>
    <img src="../../assets/animation/price_sweeps/perfect_substitutes_price_sweep.gif" alt="完全替代价格变动 GIF">
    <figcaption>预算线旋转</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全互补</span>
    <img src="../../assets/animation/price_sweeps/leontief_price_sweep.gif" alt="完全互补价格变动 GIF">
    <figcaption>价格变动，直角无差异曲线固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">只有预算线</span>
    <img src="../../assets/animation/price_sweeps/budget_only_price_sweep.gif" alt="只有预算线的价格变动 GIF">
    <figcaption>价格变动，单独呈现限制式的旋转</figcaption>
  </figure>
      </td>
      <td class="gif-table__empty" aria-hidden="true"></td>
    </tr>
  </tbody>
</table>

## 收入变动

固定效用函数与价格，只改变收入，呈现预算线平行移动时的均衡路径。

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../assets/animation/income_sweeps/cobb_douglas_income_sweep.gif" alt="Cobb-Douglas 收入变动 GIF">
    <figcaption>收入变动，价格固定</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../assets/animation/income_sweeps/ces_income_sweep.gif" alt="CES 收入变动 GIF">
    <figcaption>收入变动，价格与效用函数固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全替代</span>
    <img src="../../assets/animation/income_sweeps/perfect_substitutes_income_sweep.gif" alt="完全替代收入变动 GIF">
    <figcaption>收入变动</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全互补</span>
    <img src="../../assets/animation/income_sweeps/leontief_income_sweep.gif" alt="完全互补收入变动 GIF">
    <figcaption>收入变动，价格固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">只有预算线</span>
    <img src="../../assets/animation/income_sweeps/budget_only_income_sweep.gif" alt="只有预算线的收入变动 GIF">
    <figcaption>收入变动，单独呈现限制式的平行移动</figcaption>
  </figure>
      </td>
      <td class="gif-table__empty" aria-hidden="true"></td>
    </tr>
  </tbody>
</table>

## 导出说明

GIF 导出有以下特性：

- `Animator.save()` 使用 Pillow，**不需要** `ffmpeg`。
- 导出前，每一格都会先叠在白色背景上，避免帧残影堆叠。
- 每个动画都可以分别设置 `fps`、`dpi` 与 `loop`。
