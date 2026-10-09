---
seo_title: "图形"
---

# 图形

<span id="sec-figures"></span>

本手册的每张图都是 `MarketFigure`，或由 `ppf_canvas()` 等函数创建的 `mosaickit` 画布。两者的绘图区为正方形，坐标轴带箭头、无刻度与格线；曲线名称标在末端，面积名称写在区块内，数值标在坐标轴上，文字不遮住线、点、区块或其他文字。

## MarketFigure

<!-- api: agora.principle_viz.guides_figures_1 -->

`mosaickit` 画布上的市场图，坐标轴由 0 延伸到 `x_max` 与 `y_max`。坐标轴名称除非是文字，否则以 LaTeX 数学排版；`title` 为空字符串时不画标题。

<!-- api: agora.principle_viz.guides_figures_2 -->

由 $Q = 0$ 到 `q_max` 画出需求与供给并在末端命名；以实心点与标签标出均衡。

各主题另有专属方法，说明见对应章节（参见[`MarketFigure` 的主题方法](figures.md#tab-figure-methods)）。

<span id="tab-figure-methods"></span>

| 方法 | 章节 |
| --- | --- |
| `add_comparative_statics` | [比较静态](markets.md#sec-shifts) |
| `add_discrete_curves`、`add_discrete_equilibrium` | [离散市场](discrete.md#sec-discrete) |
| `add_welfare`、`add_welfare_transition` | [福利](welfare.md#sec-welfare) |
| `add_tax_transform`、`add_tax_comparison`、`add_subsidy_comparison` | [税收与补贴](taxes.md#sec-taxes) |
| `add_price_control` | [价格管制](controls.md#sec-controls) |
| `add_trade` | [国际贸易](trade.md#sec-trade) |
| `add_externality`、`add_common_resource` | [市场失灵](failures.md#sec-failures) |
| `add_minimum_wage`、`add_loanable_funds` | [劳动与可贷资金](factor-markets.md#sec-factor) |

<!-- api: agora.principle_viz.guides_figures_3 -->

`finalize()` 隐藏会把福利区块切成两半的辅助线（数值仍标在坐标轴上），只有在 `legend=True` 时才加入图例。`save()` 依扩展名写出 PNG、SVG 或 PDF，并创建不存在的目录。`close()` 不做任何事，仅为兼容而保留。

<!-- api: agora.principle_viz.guides_figures_4 -->

加入任意 `mosaickit` 图层，用于主题方法未提供的注记。同一数值的坐标轴标记会取代先前的标记。完成的场景可由 `fig.scene` 获得。

<!-- api: agora.principle_viz.guides_figures_5 -->

以名称与数值组成的文字框，供笔记本与调试使用。教学用图不放此框，数值应写在正文中。

## 标签与图层

<span id="sec-labels"></span>

图中的每条线、每个点、每个区块与每段文字都是一个图层，各有固定的 id，例如 `market.demand`、`market.demand.label` 或 `market.welfare.dwl`。id 依图形结构命名：坐标轴为 `axes.*`，各元素为 `market.<部分>`，命名该元素的文字再加上 `.label` 后缀。`fig.layer_ids` 列出所有图层；`fig.label_ids` 列出可设置的文字（标签、坐标轴标记与括号）。

<!-- api: agora.principle_viz.guides_figures_6 -->

覆盖一个内建标签。值为 `None` 的字段保留软件包的默认值。指定 `offset`（单位为点）时，标签不再自动放置，改为精确移动该距离。

<!-- api: agora.principle_viz.guides_figures_7 -->

改名、隐藏或移动一个标签（id 可省略结尾的 `.label`），或显示、隐藏任一图层。`hide(*ids)` 与 `show(*ids)` 一次切换多个图层。每个方法都返回图形本身。

同样的覆盖也可在创建图形时以 `labels=` 与 `visibility=` 对应表传入，之后加入的图层也会套用。加总图与各画布函数（`ppf_canvas()`、`public_good_canvas()` 等）接受同样的两个参数。

参见[改名的曲线与均衡点。](figures.md#fig-labels)：

```python
from principle_viz import Label, MarketFigure

fig = MarketFigure(
    x_max=12,
    y_max=12,
    labels={
        "market.demand.label": Label(text="Demand"),
        "market.supply.label": Label(text="Supply"),
    },
)
fig.add_curves(demand, supply, q_max=10)
fig.add_equilibrium(eq)
fig.configure_label("market.equilibrium", text="$E$")
fig.hide("axes.origin.label")
fig.finalize()
```

<span id="fig-labels"></span>

![改名的曲线与均衡点。](../../../assets/principle-viz/agora/figures/labels.svg){ .ev-figure-sm }

## 配色与主题

<span id="sec-palettes"></span>

`ColorModel` 为每个经济角色指定颜色；`PlotTheme` 再加上线宽与坐标轴选项，并将两者编译为 `mosaickit` 主题。内建的四种配色如[内建配色](figures.md#tab-palettes)。

<!-- api: agora.principle_viz.guides_figures_8 -->

具名的颜色角色：`axis_color`、`label_color`、`demand_color`、`supply_color`、`baseline_color`、`shifted_color`、`tax_color`、`control_color`、`cs_color`、`ps_color`、`tax_revenue_color`、`dwl_color` 与 `arrow_color`。每个值可为 `"#hex"` 或 `"blue"` 等 `mosaickit` 调色板名称。

<span id="tab-palettes"></span>

| 名称 | 特色 |
| --- | --- |
| `default` | `mosaickit` 色相：需求蓝、供给红、无谓损失青；剩余沿用曲线色相，透明度 15% |
| `colorblind` | 色盲友善的质性配色 |
| `nord` | Nord 配色 |
| `monochrome` | 黑、白与灰阶，供印刷使用 |

`list_color_models()` 返回所有名称，`get_color_model(name)` 返回对应的配色；四种配色也以 `DEFAULT_COLOR_MODEL`、`COLORBLIND_COLOR_MODEL`、`NORD_COLOR_MODEL` 与 `MONOCHROME_COLOR_MODEL` 导出。

<!-- api: agora.principle_viz.guides_figures_9 -->

配色加上线宽（`demand_linewidth`、`supply_linewidth`、`shifted_linewidth`、`tax_linewidth`、`arrow_linewidth`、`dashed_linewidth`）、`equilibrium_marker_size`，以及开关 `show_grid`、`show_ticks`、`show_axis_arrows` 与 `show_origin_label`。`from_palette()` 以内建配色为起点，并可设置上述任一字段。

以 `palette` 参数选用配色（参见[`monochrome` 配色。](figures.md#fig-monochrome)）：

```python
fig = MarketFigure(x_max=12, y_max=12, palette="monochrome")
```

<span id="fig-monochrome"></span>

![`monochrome` 配色。](../../../assets/principle-viz/agora/figures/monochrome.svg){ .ev-figure-sm }

## 画布

<!-- api: agora.principle_viz.guides_figures_10 -->

`mosaickit` 的 `Canvas`，并具备与 `MarketFigure` 相同的 `labels=`、`visibility=`、`configure_label()`、`configure_layer()`、`hide()`、`show()`、`layer_ids` 与 `label_ids`。生产可能性曲线、公共物品与总收益各章的画布函数都返回此类别；以 `save()` 保存，或以 `mosaickit.CanvasGrid` 组合多张画布。
