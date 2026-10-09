---
seo_title: "线性市场"
---

# 线性市场

<span id="sec-markets"></span>

## 直线

需求或供给曲线以反函数形式表示为直线：

$$
p = a + b Q
$$

其中 $a$ 为价格截距，$b$ 为斜率（需求 $b < 0$，供给 $b > 0$）。价格一律在纵轴、数量在横轴，沿用 [Marshall (1890)](../project/references.md#marshall1890) 的画法。离散的逐单位表（详见[离散市场](discrete.md#sec-discrete)）与由个人曲线加总而成的分段线性市场曲线（详见[由个人加总市场曲线](aggregation.md#sec-aggregation)）不是单一直线。

<!-- api: agora.principle_viz.guides_markets_1 -->

价格—数量平面上的直线，内部保存为 $A p + B Q + C = 0$，因此也能表示水平线与垂直线。`from_inverse(a, b)` 创建 $p = a + b Q$；`from_standard(A, B, C)` 创建 $A p + B Q + C = 0$。软件包根目录另以 `line_from_inverse()` 与 `line_from_standard()` 提供这两个构造函数。

```python
from principle_viz import line_from_inverse, line_from_standard

demand = line_from_inverse(10.0, -1.0)
# 6.0 7.0
print(demand.q_at(4), demand.p_at(3))
# 10.0 10.0
print(demand.p_intercept(), demand.q_intercept())
# (10.0, -1.0)
print(line_from_standard(1, 1, -10).to_inverse())
```

$(A, B, C) = (1, 1, -10)$ 与 $p = 10 - Q$ 等价。

水平线没有 $Q(p)$，垂直线没有 $p(Q)$；调用对应的方法会抛出 `NonInvertibleLineError`。

## 均衡

<!-- api: agora.principle_viz.guides_markets_2 -->

两条直线的交点，返回 `EquilibriumResult`（详见[快速开始](../quickstart.md#sec-quickstart)）。两线平行时抛出 `ParallelLinesError`，重合时抛出 `CoincidentLinesError`。

```python
from principle_viz import solve_equilibrium

eq = solve_equilibrium(demand, line_from_inverse(2.0, 1.0))
print(eq)
# EquilibriumResult(q_star=4.0, p_star=6.0,
#                   is_valid_market=True, notes=())
```

由 $10 - Q = 2 + Q$ 得均衡数量 4、均衡价格 6，`is_valid_market` 为 `True`，`notes` 为空。

## 比较静态

<span id="sec-shifts"></span>

<!-- api: agora.principle_viz.guides_markets_3 -->

以反函数形式描述一条曲线的移动：`delta_intercept` 为正时向上平移、为负时向下，`delta_slope` 旋转曲线。情景可同时移动需求、供给或两者。两者都位于 `principle_viz.core.shifts`。

需求增加使需求截距上升；供给增加则使供给截距*下降*，因为卖方在每个数量下都愿意接受较低的价格。

<!-- api: agora.principle_viz.guides_markets_4 -->

求解移动前后的市场，结果包含下列字段：

```python
from principle_viz import comparative_statics
from principle_viz.core.shifts import ShiftScenario, ShiftSpec

up = ShiftScenario(demand_shift=ShiftSpec(delta_intercept=3.0))
result = comparative_statics(demand, supply, up)
new = result.shifted_equilibrium
# 5.5 7.5
print(new.q_star, new.p_star)
# right up
print(result.direction_q, result.direction_p)
```

<!-- api: agora.principle_viz.guides_markets_5 -->

画出移动的曲线、两个均衡点，以及由旧均衡指向新均衡的虚线箭头。在 `add_curves()` 中将原曲线命名为 $D_0$ 与 $S_0$。需求增加的结果如[需求增加。](markets.md#fig-shifts)，供给减少的结果如[供给减少。](markets.md#fig-shift-supply)。

```python
fig = MarketFigure(
    x_max=12, y_max=14, title="Increase in Demand"
)
fig.add_curves(
    demand,
    supply,
    q_max=10,
    demand_label="$D_0$",
    supply_label="$S_0$",
)
fig.add_comparative_statics(result, q_max=10)
fig.finalize()
```

<span id="fig-shifts"></span>

![需求增加。](../../../assets/principle-viz/agora/markets/shift_demand_increase.svg){ .ev-figure-sm }

<span id="fig-shift-supply"></span>

![供给减少。](../../../assets/principle-viz/agora/markets/shift_supply_decrease.svg){ .ev-figure-sm }

## 异常

<span id="sec-errors"></span>

软件包抛出的所有异常都继承自 `principle_viz.exceptions` 中的 `PrincipleVizError`，捕获它即可一并处理。0.10.0 版以前的名称 `PrincipleEconError` 是同一个类别。各异常的抛出时机如[异常类别](markets.md#tab-errors)。

<span id="tab-errors"></span>

| 异常 | 抛出时机 |
| --- | --- |
| `LineError` | 无法创建或转换直线 |
| `NonInvertibleLineError` | 对水平线求 $Q(p)$，或对垂直线求 $p(Q)$ |
| `ParallelLinesError` | 需求与供给没有交点 |
| `CoincidentLinesError` | 需求与供给是同一条直线 |
| `PolicyError` | 税收、补贴、价格管制或贸易情景无效 |
| `DiscreteMarketError` | 离散逐单位表无效（详见[离散市场](discrete.md#sec-discrete)） |
| `AggregationError`、`PiecewiseLinearError` | 个人曲线无法加总，或价格超出分段曲线范围（详见[由个人加总市场曲线](aggregation.md#sec-aggregation)） |
| `PPFError` | 生产可能性曲线无效（详见[生产可能性曲线](ppf.md#sec-ppf)） |
