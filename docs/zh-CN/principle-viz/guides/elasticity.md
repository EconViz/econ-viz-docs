---
seo_title: "弹性与总收益"
---

# 弹性与总收益

<span id="sec-elasticity"></span>

## 价格弹性

<!-- api: agora.principle_viz.guides_elasticity_1 -->

直线在某数量下的点价格弹性

$$
\epsilon = (\mathrm{d} Q) / (\mathrm{d} p) \cdot p / Q,
$$

以及两点之间的弧弹性（中点法）

$$
\epsilon = (\Delta Q / \overline{Q}) / (\Delta p / \overline{p}),
$$

其中 $\overline{Q}$ 与 $\overline{p}$ 为两点的平均值。负斜率需求的弹性皆为负值。

```python
from principle_viz import (
    compute_arc_elasticity,
    compute_point_elasticity,
    line_from_inverse,
)

demand = line_from_inverse(10.0, -1.0)
# -1.5
print(compute_point_elasticity(demand, 4))
# -1.0 (unit elastic)
print(compute_point_elasticity(demand, 5))
# -1.0
print(compute_arc_elasticity(4, 6, 6, 4))
```

$Q = 4$ 处弹性为 $-1.5$，绝对值大于 1，需求有弹性；$Q = 5$ 为单位弹性，也是 $p = 10 - Q$ 的中点。弧弹性以两点的平均值计算，因此由 $(4, 6)$ 到 $(6, 4)$ 与反方向的结果相同。
`principle_viz.core.elasticity` 中的 `classify_elasticity(value)` 依绝对值分类：大于 1 为 `"elastic"`，等于 1 为 `"unit_elastic"`，小于 1 为 `"inelastic"`。

## 总收益

<!-- api: agora.principle_viz.guides_elasticity_2 -->

在线性需求上由 $Q = 0$ 采样到阻绝数量，返回每一点的价格、总收益 $p Q$、弹性与其分类。总收益在单位弹性处（直线的中点）最大。

$p = 12 - Q$ 的总收益最大值为 36，位于 $Q = 6$、$p = 6$。

<!-- api: agora.principle_viz.guides_elasticity_3 -->

返回两张 `mosaickit` 画布，位于 `principle_viz.visuals.revenue`：一张是需求曲线，沿线标出 "Elastic"、"Unit elastic" 与 "Inelastic"，并标记单位弹性点；另一张是总收益对数量的曲线，标记最大值。两张画布各有标题。以 `mosaickit.CanvasGrid` 左右并排（参见[需求曲线上的弹性与总收益。](elasticity.md#fig-revenue)）。

```python
from mosaickit import CanvasGrid
from principle_viz import PlotTheme, elasticity_revenue_schedule
from principle_viz.visuals.revenue import (
    elasticity_revenue_canvases,
)

demand = line_from_inverse(12.0, -1.0)
schedule = elasticity_revenue_schedule(demand)
canvases = elasticity_revenue_canvases(
    demand,
    schedule,
    theme=PlotTheme(),
)
CanvasGrid(canvases, rows=1).save(
    "elasticity_total_revenue.png"
)
```

输出参见[需求曲线上的弹性与总收益。](elasticity.md#fig-revenue)。

<span id="fig-revenue"></span>

![需求曲线上的弹性与总收益。](../../../assets/principle-viz/agora/elasticity/revenue.svg){ .ev-figure-sm }
