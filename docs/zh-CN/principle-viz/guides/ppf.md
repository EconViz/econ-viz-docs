---
seo_title: "生产可能性曲线"
---

# 生产可能性曲线

<span id="sec-ppf"></span>

<!-- api: agora.principle_viz.guides_ppf_1 -->

通过截距 $X$ 与 $Y$ 的生产可能性曲线

$$
y = Y (1 - (x / X)^c).
$$

曲率 $c = 1$ 为直线（机会成本固定）；$c > 1$ 时曲线向外凸出（机会成本递增）。截距与曲率必须为正且 $c \ge 1$，否则抛出 `PPFError`。

```python
from principle_viz import ProductionPossibilitiesFrontier

ppf = ProductionPossibilitiesFrontier(
    10,
    8,
    curvature=2,
    x_good="Consumer goods",
    y_good="Capital goods",
)
# 5.12 0.96
print(ppf.y_at(6), ppf.opportunity_cost_x(6))
print(ppf.assess(4, 3), ppf.assess(7, 6))
# PointStatus.INEFFICIENT PointStatus.UNATTAINABLE
```

<!-- api: agora.principle_viz.guides_ppf_2 -->

在曲线上采样，并评估以 `(x, y, label)` 三元组给定的点；`principle_viz.visuals.ppf` 中的 `ppf_canvas()` 画出曲线、为可达成的区域填色并标出各点（参见[有效率、无效率与无法达成的点。](ppf.md#fig-ppf)）。

```python
from principle_viz import analyze_ppf
from principle_viz.visuals.ppf import ppf_canvas

points = ((6, ppf.y_at(6), "A"), (4, 3, "B"), (7, 6, "C"))
result = analyze_ppf(ppf, points=points)
ppf_canvas(result).save("ppf_points.png")
```

<span id="fig-ppf"></span>

![有效率、无效率与无法达成的点。](../../../assets/principle-viz/agora/ppf/points.svg){ .ev-figure-sm }

<!-- api: agora.principle_viz.guides_ppf_3 -->

经济成长使各截距乘以一加上对应的成长率；结果包含 `baseline` 与 `shifted` 两条曲线及其采样点。`ppf_growth_canvas()` 画出两条曲线并命名为 $P P F_0$ 与 $P P F_1$（参见[消费财成长 20%、资本财成长 10%。](ppf.md#fig-ppf-growth)）。

<span id="fig-ppf-growth"></span>

![消费财成长 20%、资本财成长 10%。](../../../assets/principle-viz/agora/ppf/growth.svg){ .ev-figure-sm }

## 比较优势

<span id="sec-comparative-advantage"></span>

<!-- api: agora.principle_viz.guides_ppf_4 -->

比较两条直线型生产可能性曲线：各生产者生产 $x$ 的机会成本，以及各商品的比较优势归属（成本相同时为 `"tie"`）。曲线型的生产可能性曲线会抛出 `PPFError`。

```python
from principle_viz import compare_linear_ppfs

# x costs 0.5 y
ann = ProductionPossibilitiesFrontier(10, 5)
# x costs 1 y
bob = ProductionPossibilitiesFrontier(6, 6)
result = compare_linear_ppfs("Ann", ann, "Bob", bob)
print(
    result.comparative_advantage_x,
    result.comparative_advantage_y,
)
# Ann Bob
```

$x$ 的比较优势属于 Ann（0.5 对 1），$y$ 属于 Bob（1 对 2）。
