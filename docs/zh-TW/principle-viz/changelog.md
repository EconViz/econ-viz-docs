---
seo_title: "更新紀錄"
---

<span id="sec-changelog"></span>

# 更新紀錄

本章列出影響套件使用的版本變更，包含以 `principle-econ` 名稱發布的版本，不含僅修改文件的版本；各條目依 l3doc 慣例標註於它所描述的功能旁，頁碼即該功能的實際頁碼。

## 0.10.1

- CI 測試 Python 3.10–3.13 [簡介](guides/introduction.md)
- `demand_aggregation_figure` — 市場曲線在折點處標出當時有效的需求 [由個人加總市場曲線](guides/aggregation.md)
- `Label` — 每個內建標籤都可改名、隱藏或移動：新增 `Label`、`labels=`、`configure_label()` 與 `label_ids` [圖形](guides/figures.md)
- `MarketFigure.configure_layer` — 每個圖層都可隱藏或顯示：新增 `visibility=`、`configure_layer()`、`hide()`、`show()` 與 `layer_ids` [圖形](guides/figures.md)

## 0.10.0

- 由 `principle-econ` 更名為 `principle-viz`，加入 EconViz 系列；Python 套件名稱改為 `principle_viz` [簡介](guides/introduction.md)
- 圖形改以 `mosaickit` 繪製（`mosaickit>=0.5.1,<0.6.0`） [簡介](guides/introduction.md)
- 專案工具由 Poetry 改為 `uv` [簡介](guides/introduction.md)
- `principle-viz` — 唯一的執行期依賴為 `mosaickit` [安裝](installation.md)
- `add_comparative_statics` — 只重畫移動的曲線；移動後的曲線命名為 $D_1$ / $S_1$（`demand_label` / `supply_label`） [線性市場](guides/markets.md)
- `add_comparative_statics` — 移動箭頭改為黑色細虛線 [線性市場](guides/markets.md)
- `MarketFigure.add_discrete_curves` — 可只傳入需求表、只傳入供給表，或兩者都傳入 [離散市場](guides/discrete.md)
- `MarketFigure.add_discrete_curves` — 空心端點改為不透明的白色填色，並以細虛線連到下一階 [離散市場](guides/discrete.md)
- `market_demand` — 個人線性曲線水平加總為市場需求與供給，並新增 `PiecewiseLinear`、`solve_piecewise_equilibrium()` 與 `piecewise_surplus()` [由個人加總市場曲線](guides/aggregation.md)
- `DiscreteDemand.combine` — 離散表新增 `combine()` 與 `quantity_at()` [由個人加總市場曲線](guides/aggregation.md)
- `demand_aggregation_figure` — 需求與供給（線性與離散）的*個人 | 個人 | 市場*圖，回傳 `AggregationFigure` [由個人加總市場曲線](guides/aggregation.md)
- `demand_aggregation_figure` — `link_price=True` 讓價格線橫跨所有面板 [由個人加總市場曲線](guides/aggregation.md)
- `MarketFigure.add_welfare` — 以文字命名各區塊（"Consumer surplus"、"CS" 等），寫在區塊內、改用縮寫或以引線標示；`labels=False` 只填色 [福利](guides/welfare.md)
- `MarketFigure.add_welfare` — 消費者剩餘與生產者剩餘沿用需求與供給的色相；稅收只標示文字、不填色 [福利](guides/welfare.md)
- `MarketFigure.add_tax_transform` — 課稅後的曲線命名為 $S + t$ / $D - t$；旋轉標籤移到箭頭尾端 [租稅與補貼](guides/taxes.md)
- `MarketFigure.add_tax_comparison` — 在價格軸上標出 $p_d$、$p_0$ 與 $p_s$，並加上 "Tax" 括號；新增 `brace_side` 與 `notes` [租稅與補貼](guides/taxes.md)
- `MarketFigure.add_subsidy_comparison` — 補貼楔差加上 "Subsidy" 括號，並標示補貼成本 [租稅與補貼](guides/taxes.md)
- `MarketFigure.add_price_control` — 有效的管制直接命名管制線，標出 $p_c$、$Q_d$ 與 $Q_s$，並在管制線上以括號標示 "Shortage" 或 "Surplus"；`gap_brace="axis"` 改在數量軸下方標示 [價格管制](guides/controls.md)
- `MarketFigure.add_trade` — 標出 $Q_s$ / $Q_d$，並在數量軸下方以括號標示 "Imports" / "Exports"；政策價格標為 $p_w + t$ 或 $p_q$ [國際貿易](guides/trade.md)
- `MarketFigure.add_externality` — 社會曲線命名為 $M S C$ / $M S B$；$Q_m$ 與 $Q^*$ 標在數量軸上；矯正稅與補貼改為橫跨 $Q^*$ 處的差距 [市場失靈](guides/failures.md)
- `MarketFigure.add_minimum_wage` — 以價格下限的方式繪製："Minimum wage" 線、$w_{\min}$、$L_d$ / $L_s$ 與 "Unemployment" 括號 [勞動與可貸資金](guides/factor-markets.md)
- `MarketFigure` — 圖形改為正方形（150 dpi 下 6 × 6 英吋），背景為不透明白色；直線曲線止於價格軸的 92% [圖形](guides/figures.md)
- `MarketFigure` — 曲線名稱標在可見端點旁，不再放進圖例 [圖形](guides/figures.md)
- `MarketFigure` — 座標軸名稱預設為 $p$ 與 $Q$，以斜體數學字放在箭頭外側；標題不再使用粗體 [圖形](guides/figures.md)
- `MarketFigure` — 均衡與政策標籤由 `mosaickit` 放在點旁；擁擠處的數量改標在數量軸上 [圖形](guides/figures.md)
- `MarketFigure.finalize` — 預設不加圖例；`finalize(legend=True)` 才會加入 [圖形](guides/figures.md)
- `ColorModel` — `default` 配色改用 `mosaickit` 的色相：需求藍、供給紅、無謂損失青 [圖形](guides/figures.md)
- `PlotTheme` — 供需曲線寬 3.5 pt、座標軸 1.0 pt、均衡點直徑 6.5 pt [圖形](guides/figures.md)

## 0.1.0

- 以 `principle-econ` 名稱首次發布：線性市場、租稅、福利、繪圖與命令列介面 [簡介](guides/introduction.md)
- `TaxScenario` — `fixed`、`per_unit` 與 `ad_valorem` 三種租稅，法定納稅人可為買方或賣方 [租稅與補貼](guides/taxes.md)
- `ColorModel` — `default`、`colorblind`、`nord` 與 `monochrome` 四種配色 [圖形](guides/figures.md)
- `principle-viz` — 命令列介面，輸出 JSON [命令列介面](cli.md)

