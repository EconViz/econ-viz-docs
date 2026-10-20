---
seo_title: "交互组件"
---

# 交互组件

<span id="sec-widgets"></span>

`WidgetViewer` 在 Jupyter 中提供滑块与数值输入字段，调整参数后会更新图形。使用前需安装 `interactive` 可选依赖（详见[可选依赖](../getting-started/installation.md#sec-extras)）。从 `utility_viz.core.interactive` 导入；1.x 为 `econ_viz.interactive`。

<!-- api: agora.utility_viz.guides_interactive_1 -->

传入绘图函数 `draw`，并以 `(最小值, 最大值, 步长)` 指定各参数范围。每个参数会生成同步的 `FloatSlider` 与 `FloatText`；数值变更后重新调用 `draw`，并替换单元格中的旧图。

`draw` 的写法与 `Animator` 相同（详见[动画](animation.md#sec-animation)），只是可同时接收多个参数。以[动画](animation.md#sec-animation)的价格变动示例为基础，让 `draw()` 另外接收 `alpha`：

```python
from utility_viz.core.interactive import WidgetViewer

def draw(alpha: float, px: float) -> Canvas:
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    ...  # 其余与动画示例相同

WidgetViewer(
    draw,
    alpha=(0.2, 0.8, 0.05),
    px=(1.0, 6.0, 0.25),
).show()
```

## 笔记本设置

在新的 Jupyter 或 Colab 环境中，按下列顺序运行 (utility-viz 仓库中的 `notebook/econ-viz Playground.ipynb`（沿用旧文件名）已采用此流程，可在 Jupyter、VS Code 或 Colab 打开；环境中已有 `utility-viz` 时，会自动跳过安装。)：

+ 运行安装单元格。
+ 若安装过程升级 `ipywidgets`、`traitlets` 或 `IPython`，重新启动运行环境。
+ 重新启动后，从导入软件包的单元格继续运行，无须再次安装。

## 选择交互组件或 GIF

需要由用户调整参数时，使用 `WidgetViewer`；需要在演示文稿或网页中播放固定的变动过程时，使用 `Animator` 导出 GIF（详见[动画](animation.md#sec-animation)）。
