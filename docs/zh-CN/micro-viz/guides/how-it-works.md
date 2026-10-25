---
seo_title: "运作方式"
---

# 运作方式

<span id="sec-how"></span>

## 先模型，后图形

每个主题分两层。

- **模型**是冻结的 dataclass：输入会检查，方法回答问题，例如 `CubicCost.marginal_cost`、`Monopolist.solve`、`IndustrySupply.quantity`。模型**不引入**任何绘图套件，输入不合法时丢出自己的错误（`CostError`、`CompetitionError`、`UncertaintyError`）。
- `micro_viz.visuals` 里的**绘图函数**把模型结果变成 `mosaickit` 的 `Canvas`，例如 `unit_cost_canvas(analysis)`、`monopoly_canvas(outcome, analysis)`。绘图函数里没有方程序，只负责摆放模型算出来的东西。

```python
from micro_viz import CubicCost, LinearDemand, Monopolist, analyze_costs, monopoly_canvas

demand = LinearDemand(intercept=30, slope=2)
cost = CubicCost(20, 6, -1.5, 0.15)
outcome = Monopolist(demand, cost).solve()
analysis = analyze_costs(cost, output_range=(1, 10))

monopoly_canvas(outcome, analysis, profit=True).save("monopoly.svg")
```

## 套件结构

| 位置 | 内容 |
| --- | --- |
| `micro_viz/<主题>.py`、`micro_viz/<主题>/` | 模型与求解器，不含绘图 |
| `micro_viz/visuals/` | 回传 `Canvas` 的绘图函数；`plane.py` 是平面图的小工具（`Plane`） |
| `micro_viz/locale/labels.json` | 所有内置文本，依编号与语言存放 |
| `micro_viz/theme.py`、`config.py` | 主题与 `[micro]` 设置的结构 |
| `micro_viz/animation/` | 选用的参数动画 |
| `examples/scripts/` | 每个主题一支脚本，也是本文档的图 |

## 多面板图形

多个面板的图（市场与厂商、多厂独占、产业供给）使用 `mosaickit` 的 `CanvasGrid`。横跨面板间隙的虚线是 `GridLink`，从一格的某点连到下一格的某点，所以价格或边际成本的水准线是**连续**的一条。

## 与其他套件的关系

- **mosaickit** 负责所有绘制：场景、图层、主题、标签位置、网格与输出。`micro-viz` 运行时只依赖它。
- **bezierkit** 提供曲线几何。`micro-viz` 目前不直接引入；当图形需要它的公开几何 API（由角度决定的旋转连接线）时才加入依赖。
- **kinetickit** 让图形动起来，只随 `animation` 选用依赖安装（见[动画](animation.md#sec-animation)）。
- **glyphkit** 负责动画 SVG 的文本，经由 mosaickit 引入。
- **utility-viz** 与 **principle-viz** 负责消费者理论与入门市场图，这里可以使用它们的对象，但 `micro-viz` 不重写。
