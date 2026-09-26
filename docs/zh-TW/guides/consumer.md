---
seo_title: "多面板圖與需求圖"
description: "用 econ-viz 建立多面板圖、需求圖、價格效果分解與 Edgeworth 箱形圖。"
---

# 多面板圖與需求圖

`econ-viz` 在 `Canvas` 之上提供更高階的教學元件：

- `Figure`：多面板版面
- `PricePath` 與 `IncomePath`：讓預算與均衡隨參數移動
- `DemandDiagram`：連動的商品空間圖與 Marshall 需求圖
- `decompose_price_effect(...)`：Hicks 與 Slutsky 分解
- `EdgeworthBox`：兩人交換的 Edgeworth 箱形圖

## 多面板圖 {#multi-panel-figure data-toc-label="多面板圖"}

一個面板不夠用時就用 `Figure`，例如變動前後的比較、效果分解圖或課堂簡報。

```python
from econ_viz import Figure, Layout, levels, solve
from econ_viz.models import CobbDouglas

fig = Figure(
    Layout.SIDE_BY_SIDE,
    x_max=20,
    y_max=15,
    x_label="x",
    y_label="y",
    title="Before / After Price Change",
    shared_y=True,
)

cases = [
    (CobbDouglas(alpha=0.5, beta=0.5), 2.0, 3.0, 30.0, r"Before: $p_x=2$"),
    (CobbDouglas(alpha=0.3, beta=0.7), 4.0, 3.0, 30.0, r"After: $p_x=4$"),
]

for idx, (model, px, py, income, title) in enumerate(cases):
    eq = solve(model, px=px, py=py, income=income)
    panel = fig[idx]
    panel.ax.set_title(title)
    panel.add_utility(model, levels=levels.around(eq.utility, n=5), label="IC")
    panel.add_budget(px, py, income, fill=True, label="BC")
    panel.add_equilibrium(eq, show_ray=True)

fig[0].show_legend(loc="upper right")
fig.save("figure_side_by_side.png")
```

![多面板並排比較](../../assets/consumer/figure_side_by_side.png)

### 可用的版面

`Figure` 提供以下版面：

- `Layout.SINGLE`
- `Layout.STACKED`
- `Layout.SIDE_BY_SIDE`
- `Layout.TOP_TWO_BOTTOM_ONE`
- `Layout.TOP_ONE_BOTTOM_TWO`
- `Layout.GRID_2X2`
- `Layout.GRID_3X3`

`Figure[idx]` 會回傳一個面板 `Canvas`，所以版面建好之後，繪圖 API 完全相同。

## 路徑工具

路徑物件會讓某一個預算參數逐步變動，並在每一步重新求解消費者問題。

```python
from econ_viz import IncomePath, LinearBudget, PricePath
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
budget = LinearBudget(px=2.0, py=2.0, income=40.0)

price_path = PricePath(
    model,
    budget=budget,
    price="px",
    price_range=(0.8, 6.0),
    n=40,
)
income_path = IncomePath(
    model,
    budget=budget,
    income_range=(20.0, 80.0),
    n=30,
)
```

這些路徑可以用來：

- 用 `Canvas.add_path(...)` 畫出 PCC / ICC 形式的均衡軌跡
- 傳入 `DemandDiagram`
- 觀察價格或所得變動時，消費組合如何移動

## 需求圖 {#demanddiagram data-toc-label="需求圖"}

`DemandDiagram` 會建立上下兩個面板的圖：

- **上方面板**：無異曲線、預算線與均衡點
- **下方面板**：對應的 Marshall 需求曲線

```python
from econ_viz import DemandDiagram, LinearBudget, PricePath
from econ_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.5, beta=0.5)
budget = LinearBudget(px=2.0, py=2.0, income=40.0)
path = PricePath(
    model,
    budget=budget,
    price="px",
    price_range=(0.8, 6.0),
    n=40,
)

fig = DemandDiagram(path, title="Demand: Cobb-Douglas")
fig.add_marshallian_panel(
    price_markers=[1.5, 4.0],
    show_pcc=False,
    show_demand_guides=True,
)
fig.save("demand_cobb_douglas.png")
```

![連動的 Marshall 需求圖](../../assets/consumer/demand_cobb_douglas.png)

### 注意事項

建立需求圖時請注意以下限制：

- `DemandDiagram` 目前只接受 `PricePath`
- 平滑、拗折與角解的需求情況會分別處理，讓下方面板在經濟意義上保持正確
- `show_pcc=True` 會在商品空間面板上疊加價格消費曲線

## 價格效果分解

`decompose_price_effect(...)` 將價格變動分成替代效果與所得效果。`HICKS` 固定原本的效用水準；`SLUTSKY` 則讓原本的消費組合在新價格下仍買得起。

```python
from econ_viz import Canvas, DecompositionMethod, levels
from econ_viz.models import CobbDouglas
from econ_viz.optimizer import decompose_price_effect

model = CobbDouglas(alpha=0.5, beta=0.5)
result = decompose_price_effect(
    model,
    px=(2.0, 4.0),
    py=3.0,
    income=60.0,
    method=DecompositionMethod.HICKS,
)

utility_levels = sorted({result.A.utility, result.C.utility})

(
    Canvas(x_max=25, y_max=25, title="Hicks decomposition")
    .add_utility(model, levels=utility_levels)
    .add_decomposition(
        result,
        show_arrows=True,
        label_effects=True,
        show_x_projections=True,
    )
    .save("hicks.png")
)
```

`result.A`、`result.B` 與 `result.C` 分別是原始、補償後與最終消費組合。結果也包含 `substitution_effect`、`income_effect`、`total_effect` 與 `compensated_income`。

用 `Effect` 可設定每個效果的顏色、座標軸下方範圍箭頭的高度，以及旁邊的標籤。`point_label` 可移動或隱藏 A、B、C 標籤：

```python
from econ_viz import Effect, Label

canvas.add_decomposition(
    result,
    substitution=Effect(color="#E67E22", label="SE", label_position="top"),
    income=Effect(color="#27AE60", label="IE"),
    point_label=Label(visible=False),
)
```

![Hicks 價格效果分解](../../assets/consumer/cobb_douglas_hicks.png)

## Edgeworth 箱形圖

`EdgeworthBox` 用來畫兩人交換經濟。消費者 A 從左下角原點計量，消費者 B 則從右上角原點計量。

```python
from econ_viz import EdgeworthBox
from econ_viz.models import CobbDouglas

box = EdgeworthBox(
    CobbDouglas(alpha=0.8, beta=0.2),
    CobbDouglas(alpha=0.2, beta=0.8),
    total_x=12.0,
    total_y=10.0,
    title="Asymmetric Cobb-Douglas",
)

(
    box.add_endowment(5.0, 4.0)
    .add_contract_curve(n=100, method="mrs")
    .add_core()
    .add_price_line(px=1.2, py=1.0)
    .add_walrasian_equilibrium(px=1.2, py=1.0)
    .show_legend(loc="center left", bbox_to_anchor=(1.02, 0.5))
    .save("edgeworth.png")
)
```

平滑偏好可使用 `method="mrs"`。有折點、角解或自訂分段效用函數時，使用 `method="pareto"`。

![非對稱 Cobb-Douglas Edgeworth 箱形圖](../../assets/consumer/edgeworth_cobb_asymmetric.png)

## 繪製路徑 {#canvasadd_path data-toc-label="繪製路徑"}

不需要完整的需求圖時，也可以直接在 `Canvas` 上畫出路徑。

```python
from econ_viz import Canvas, levels

eq = price_path.equilibria[len(price_path.equilibria) // 2]
lvls = levels.around(eq.utility, n=5)

Canvas(x_max=25, y_max=20) \
    .add_utility(model, levels=lvls) \
    .add_path(price_path, label="PCC") \
    .save("price_path.png")
```
