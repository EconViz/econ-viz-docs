---
seo_title: "模型与图形"
---

# 模型与图形

<span id="sec-model-figure"></span>

## 先模型，后图形

每个主题分成两层。

- *模型*是冻结的数据类别（frozen dataclass），检查输入，并以方法回答问题：`CubicCost.marginal_cost`、`Monopolist.solve`、`IndustrySupply.quantity`。模型从不引入绘图器，输入不当时抛出自己的例外（`CostError`、`CompetitionError`、`UncertaintyError`）。
- `micro_viz.visuals` 中的*绘图函数*把模型结果转成 `mosaickit` 的 `Canvas`：`unit_cost_canvas(analysis)`、`monopoly_canvas(outcome, analysis)`。绘图函数不含方程序，只安置模型算出的内容。

```python
from micro_viz import (
    CubicCost,
    LinearDemand,
    Monopolist,
    analyze_costs,
    monopoly_canvas,
)

demand = LinearDemand(intercept=30, slope=2)
cost = CubicCost(20, 6, -1.5, 0.15)
outcome = Monopolist(demand, cost).solve()
analysis = analyze_costs(cost, output_range=(1, 10))

monopoly_canvas(outcome, analysis, profit=True).save(
    "monopoly.svg"
)
```

## 共同选项

<span id="sec-options"></span>

每个绘图函数都返回 `Canvas`，并接受相同的关键字选项。本页的函数签名以 `**options` 表示它们。

<!-- api: micro_viz.guides_model_figure_1 -->

画多栏的绘图函数以 `titles`（每栏一个）取代 `title`。

## 软件包结构

<span id="tab-layout"></span>

| 位置 | 内容 |
| --- | --- |
| `micro_viz/<topic>.py`、`micro_viz/<topic>/` | 模型与求解器，不含绘图 |
| `micro_viz/visuals/` | 返回 `Canvas` 的绘图函数；`plane.py` 是平面图的小工具组（`Plane`） |
| `micro_viz/locale/labels.json` | 所有内置文本，依编号与语言整理 |
| `micro_viz/theme.py`、`config.py` | 主题与 `[micro]` 设置结构 |
| `micro_viz/animation/` | 选用的参数动画 |
| `examples/scripts/` | 每个主题一支脚本；本页的图形 |

## 图层 ID

绘图函数替每个图层指定稳定的编号，格式为 `micro.<prefix>.<kind>.<n>`，例如 `micro.cost.avc.label`。设置档的逐图标签表以这些编号为对象（参见 [标签与位置](labels.md#sec-labels)），动画也以它们在帧之间配对图层（参见 [动画](animation.md#sec-animation)）。

## 多栏图

有数栏的图（市场与厂商、多厂房独占、产业供给）使用 `mosaickit` 的 `CanvasGrid`。横跨栏间空隙的虚线是从一格中的点连到下一格中的点的 `GridLink`，所以价格或边际成本的水准线保持连续。

## 与其他软件包的关系

- `mosaickit` 负责绘制一切：场景、图层、主题、标签位置、格状排版与输出。`micro-viz` 运行时只依赖它。
- `bezierkit` 提供曲线几何。`micro-viz` 不直接引入它；图形需要其公开的几何 API 时才加入依赖。
- `kinetickit` 让图形成为动画，只随 `animation` 选用依赖安装（参见 [动画](animation.md#sec-animation)）。
- `utility-viz` 与 `principle-viz` 负责消费者理论与入门的市场图。它们的对象可以搭配使用，`micro-viz` 不重写它们。
