---
seo_title: "福利"
---

# 福利

<span id="sec-welfare"></span>

福利分析比較某個市場結果與其他可能結果：消費者剩餘、生產者剩餘、政府收入，以及無謂損失。

## 市場結果

<!-- api: agora.principle_viz.guides_welfare_1 -->

一個數量，加上買方支付與賣方收到的價格。課稅或補貼時兩個價格不同，價差乘以數量就是政府收入（補貼為負）。此類別位於 `principle_viz.welfare.surplus`，同模組也提供由各種結果建立市場結果的函式：

## 剩餘

<!-- api: agora.principle_viz.guides_welfare_2 -->

`outcome` 下的福利分解。傳入 `baseline_outcome` 時，以其為基準衡量無謂損失。回傳的 `SurplusResult` 包含下列欄位：

```python
from principle_viz import compute_surplus, solve_equilibrium
from principle_viz.welfare.surplus import (
    outcome_from_equilibrium,
)

eq = solve_equilibrium(demand, supply)
outcome = outcome_from_equilibrium(eq)
surplus = compute_surplus(demand, supply, outcome)
# 8.0 8.0
print(surplus.consumer_surplus, surplus.producer_surplus)
```

$(10 - 6) \times 4 / 2 = (6 - 2) \times 4 / 2 = 8$；自由市場的無謂損失為 0。

<!-- api: agora.principle_viz.guides_welfare_3 -->

兩個福利分解及其差異：`baseline`、`policy`、`delta_consumer_surplus`、`delta_producer_surplus`、`delta_tax_revenue`、`delta_total_surplus` 與 `deadweight_loss`。[租稅與補貼](taxes.md#sec-taxes)以租稅為例使用此函式。

## 圖形

<!-- api: agora.principle_viz.guides_welfare_4 -->

為消費者剩餘、生產者剩餘、稅收與無謂損失填色並命名：名稱放得下時寫在區塊內，只放得下縮寫時寫 CS、PS、Tax、DWL，否則以引線標示，且不遮住任何線、點或其他文字。

```python
fig = MarketFigure(x_max=12, y_max=12)
fig.add_curves(demand, supply, q_max=10)
fig.add_welfare(surplus)
fig.add_equilibrium(eq)
fig.finalize()
```

輸出參見[均衡下的消費者與生產者剩餘。](welfare.md#fig-welfare)。

<span id="fig-welfare"></span>

![均衡下的消費者與生產者剩餘。](../../../assets/principle-viz/agora/welfare/equilibrium.svg){ .ev-figure-sm }

<!-- api: agora.principle_viz.guides_welfare_5 -->

同樣的區塊，再加上基準與政策下數量及價格的輔助線，用於比較前後差異。

## 無謂損失報表

<!-- api: agora.principle_viz.guides_welfare_6 -->

將 `(名稱, 基準, 政策)` 三元組（皆為 `SurplusResult`）轉為報表列（`DWLScenarioRow`），包含數量變動、各項剩餘變動與無謂損失。`principle_viz.welfare.report` 中的 `save_dwl_report_csv()` 與 `save_dwl_report_json()` 可將報表寫成檔案。
