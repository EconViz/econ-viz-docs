---
seo_title: "更新纪录"
---

<span id="sec-changelog"></span>

# 更新纪录

本章列出影响软件包使用的版本变更，包含以 `principle-econ` 名称发布的版本，不含仅修改文档的版本；各条目依 l3doc 惯例标注于它所描述的功能旁，页码即该功能的实际页码。

## 0.10.1

- CI 测试 Python 3.10–3.13 [简介](guides/introduction.md)
- `demand_aggregation_figure` — 市场曲线在折点处标出当时有效的需求 [由个人加总市场曲线](guides/aggregation.md)
- `Label` — 每个内建标签都可改名、隐藏或移动：新增 `Label`、`labels=`、`configure_label()` 与 `label_ids` [图形](guides/figures.md)
- `MarketFigure.configure_layer` — 每个图层都可隐藏或显示：新增 `visibility=`、`configure_layer()`、`hide()`、`show()` 与 `layer_ids` [图形](guides/figures.md)

## 0.10.0

- 由 `principle-econ` 更名为 `principle-viz`，加入 EconViz 系列；Python 软件包名称改为 `principle_viz` [简介](guides/introduction.md)
- 图形改以 `mosaickit` 绘制（`mosaickit>=0.5.1,<0.6.0`） [简介](guides/introduction.md)
- 项目工具由 Poetry 改为 `uv` [简介](guides/introduction.md)
- `principle-viz` — 唯一的运行时依赖为 `mosaickit` [安装](installation.md)
- `add_comparative_statics` — 只重画移动的曲线；移动后的曲线命名为 $D_1$ / $S_1$（`demand_label` / `supply_label`） [线性市场](guides/markets.md)
- `add_comparative_statics` — 移动箭头改为黑色细虚线 [线性市场](guides/markets.md)
- `MarketFigure.add_discrete_curves` — 可只传入需求表、只传入供给表，或两者都传入 [离散市场](guides/discrete.md)
- `MarketFigure.add_discrete_curves` — 空心端点改为不透明的白色填色，并以细虚线连到下一阶 [离散市场](guides/discrete.md)
- `market_demand` — 个人线性曲线水平加总为市场需求与供给，并新增 `PiecewiseLinear`、`solve_piecewise_equilibrium()` 与 `piecewise_surplus()` [由个人加总市场曲线](guides/aggregation.md)
- `DiscreteDemand.combine` — 离散表新增 `combine()` 与 `quantity_at()` [由个人加总市场曲线](guides/aggregation.md)
- `demand_aggregation_figure` — 需求与供给（线性与离散）的*个人 | 个人 | 市场*图，返回 `AggregationFigure` [由个人加总市场曲线](guides/aggregation.md)
- `demand_aggregation_figure` — `link_price=True` 让价格线横跨所有面板 [由个人加总市场曲线](guides/aggregation.md)
- `MarketFigure.add_welfare` — 以文字命名各区块（"Consumer surplus"、"CS" 等），写在区块内、改用缩写或以引线标示；`labels=False` 只填色 [福利](guides/welfare.md)
- `MarketFigure.add_welfare` — 消费者剩余与生产者剩余沿用需求与供给的色相；税收只标示文字、不填色 [福利](guides/welfare.md)
- `MarketFigure.add_tax_transform` — 征税后的曲线命名为 $S + t$ / $D - t$；旋转标签移到箭头尾端 [税收与补贴](guides/taxes.md)
- `MarketFigure.add_tax_comparison` — 在价格轴上标出 $p_d$、$p_0$ 与 $p_s$，并加上 "Tax" 括号；新增 `brace_side` 与 `notes` [税收与补贴](guides/taxes.md)
- `MarketFigure.add_subsidy_comparison` — 补贴楔子加上 "Subsidy" 括号，并标示补贴成本 [税收与补贴](guides/taxes.md)
- `MarketFigure.add_price_control` — 有效的管制直接命名管制线，标出 $p_c$、$Q_d$ 与 $Q_s$，并在管制线上以括号标示 "Shortage" 或 "Surplus"；`gap_brace="axis"` 改在数量轴下方标示 [价格管制](guides/controls.md)
- `MarketFigure.add_trade` — 标出 $Q_s$ / $Q_d$，并在数量轴下方以括号标示 "Imports" / "Exports"；政策价格标为 $p_w + t$ 或 $p_q$ [国际贸易](guides/trade.md)
- `MarketFigure.add_externality` — 社会曲线命名为 $M S C$ / $M S B$；$Q_m$ 与 $Q^*$ 标在数量轴上；矫正税与补贴改为横跨 $Q^*$ 处的差距 [市场失灵](guides/failures.md)
- `MarketFigure.add_minimum_wage` — 以价格下限的方式绘制："Minimum wage" 线、$w_{\min}$、$L_d$ / $L_s$ 与 "Unemployment" 括号 [劳动与可贷资金](guides/factor-markets.md)
- `MarketFigure` — 图形改为正方形（150 dpi 下 6 × 6 英吋），背景为不透明白色；直线曲线止于价格轴的 92% [图形](guides/figures.md)
- `MarketFigure` — 曲线名称标在可见端点旁，不再放进图例 [图形](guides/figures.md)
- `MarketFigure` — 坐标轴名称默认为 $p$ 与 $Q$，以斜体数学字体放在箭头外侧；标题不再使用粗体 [图形](guides/figures.md)
- `MarketFigure` — 均衡与政策标签由 `mosaickit` 放在点旁；拥挤处的数量改标在数量轴上 [图形](guides/figures.md)
- `MarketFigure.finalize` — 默认不加图例；`finalize(legend=True)` 才会加入 [图形](guides/figures.md)
- `ColorModel` — `default` 配色改用 `mosaickit` 的色相：需求蓝、供给红、无谓损失青 [图形](guides/figures.md)
- `PlotTheme` — 供需曲线宽 3.5 pt、坐标轴 1.0 pt、均衡点直径 6.5 pt [图形](guides/figures.md)

## 0.1.0

- 以 `principle-econ` 名称首次发布：线性市场、税收、福利、绘图与命令行界面 [简介](guides/introduction.md)
- `TaxScenario` — `fixed`、`per_unit` 与 `ad_valorem` 三种税，法定纳税人可为买方或卖方 [税收与补贴](guides/taxes.md)
- `ColorModel` — `default`、`colorblind`、`nord` 与 `monochrome` 四种配色 [图形](guides/figures.md)
- `principle-viz` — 命令行界面，输出 JSON [命令行界面](cli.md)

