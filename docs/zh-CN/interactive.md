---
seo_title: "在 Jupyter 中操作交互式经济学图形"
description: "在 Jupyter 笔记本中用 econ-viz 的 WidgetViewer 滑块与数字输入框，交互探索效用函数与预算约束。"
---

# 交互组件

`WidgetViewer` 会在笔记本保存格中绘制 `econ-viz` 图形，只要控制项一变动就重新绘制。每个参数都同时有**滑块**和**数字输入框**，用户可以拖动培养直觉，也可以输入精确数值，方便教学与演示。

## 安装

```bash
uv add "econ-viz[interactive]"
```

如果也要导出 GIF：

```bash
uv add "econ-viz[all]"
```

## 基本用法

```python
from econ_viz import Canvas, levels, solve
from econ_viz.interactive import WidgetViewer
from econ_viz.models import CobbDouglas

def draw(alpha: float, px: float) -> Canvas:
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    eq = solve(model, px=px, py=2.0, income=20.0)

    return (
        Canvas(x_max=14, y_max=12, x_label="X_1", y_label="X_2", title="Interactive equilibrium")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(px=px, py=2.0, income=20.0, fill=True)
        .add_equilibrium(eq, show_ray=True, drop_dashes=True)
    )

WidgetViewer(
    draw,
    alpha=(0.2, 0.8, 0.05),
    px=(1.0, 6.0, 0.25),
).show()
```

## 交互组件做了什么

- 为每个参数创建一个 `FloatSlider`。
- 为每个参数创建一个联动的 `FloatText` 输入框。
- 让滑块与输入的数值保持同步。
- 重新绘制前会先清掉旧图，笔记本保存格里不会堆积一堆过时的图。

## Colab 与 Jupyter 注意事项

在全新的笔记本运行环境中，尤其是 Colab：

1. 先运行一次安装保存格。
2. 如果 `ipywidgets`、`traitlets` 或 `IPython` 被升级了，**重新启动一次运行环境**。
3. 重新启动后跳过安装保存格，从 import 保存格继续运行。

随包附带的 Playground 笔记本已经照这个流程设计，若环境中已经装好 `econ-viz`，就不会重新安装。

## 什么时候用交互组件，什么时候用 GIF

- 学生需要输入或拖动参数、一次检查一个状态时，用 `WidgetViewer`。
- 想在演示文稿、文文件或项目网站中呈现固定、可重复播放的变动过程时，用 `Animator`。
