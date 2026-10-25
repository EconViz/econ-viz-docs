---
seo_title: "快速开始"
---

# 快速开始

<span id="sec-quickstart"></span>

画一张图分两步：先创建模型，再把结果交给 `micro_viz` 的绘图函数。

```python
from micro_viz import CubicCost, analyze_costs, unit_cost_canvas

cost = CubicCost(fixed_cost=50, linear=36, quadratic=-8, cubic=0.6)
analysis = analyze_costs(cost, output_range=(1, 11))

unit_cost_canvas(analysis).save("unit_cost.svg")
```

![单位成本](../../assets/micro-viz/zh-CN/costs/unit_cost.svg){ .ev-figure-sm }

`save()` 依扩展名输出 PNG、SVG 或 PDF。模型不可变，不画图也能回答问题：

```python
analysis.minimum_average_total_cost    # 最低 ATC 与其产量
cost.marginal_cost(5.0)                # 某产量的 MC
```

## 标题、文本与设置

- `title=None` 不画标题，`title="..."` 设置标题。
- 内置文本（座标轴名称、曲线名称、点名称）是语系表的文本编号；`labels={"编号": "文本"}` 可以取代任何一句（见[文本与位置](guides/labels.md#sec-labels)）。
- 颜色、线宽、字体与大小来自主题和共用 `econ-viz.toml` 的 `[micro]` 表（见[设置](guides/settings.md#sec-settings)），绘图程序里**没有**这些值。
- 范围、产量标记与采样数等数字都是绘图函数的参数。
