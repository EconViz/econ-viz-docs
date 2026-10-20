---
seo_title: "快速開始"
---

# 快速開始

<span id="sec-quickstart"></span>

## 基本範例

本章以 Cobb-Douglas 消費者問題說明完整流程：

$$
\begin{aligned}\max_{x, y} & u(x, y) = x^{1/2} y^{1/2} \\ \text{s.t.} & 2x + 3y = 30\end{aligned}
$$

程式先求解最適消費組合，再繪製無異曲線、預算集合與均衡點（參見[消費者均衡。](quickstart.md#fig-quickstart)）。

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import CobbDouglas

# 本手冊圖形所用的設定
Config.load("manual.toml").use()

model = CobbDouglas(alpha=0.5, beta=0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

# 斜體的 x 與 y
cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
# 五條曲線 一條過最適點
lvls = levels.around(eq.utility, n=5)
cvs.add_utility(model, levels=lvls)
# 預算線與可行集合
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
# 附擴張路徑
cvs.add_equilibrium(eq, show_ray=True)
cvs.save("cobb_douglas.png")
```

<span id="fig-quickstart"></span>

![消費者均衡。](../../../assets/utility-viz/agora/models/cobb_douglas.svg){ .ev-figure-sm }

消費者均衡。 [下載繪製腳本](../../../assets/utility-viz/agora/models/cobb_douglas.py){ .ev-download download="" }
{ .ev-caption }

執行主程式 `main.py` 後，會在目前工作目錄建立 `cobb_douglas.png`。本例的最適消費量為 $x^* = 7.5$、$y^* = 5$，支出為 $2 \times 7.5 + 3 \times 5 = 30$，恰好等於所得。預算線的兩個軸截距則為 $I / p_x = 15$ 與 $I / p_y = 10$。

## 逐步說明

繪圖流程依序為：建立模型、求解均衡、選取效用水準、建立畫布、加入圖層與匯出。

<!-- api: agora.utility_viz.getting_started_quickstart_1 -->

建立效用模型。內建模型詳見[核心模型](../models/index.md#sec-models)；自訂函數使用 `CustomUtility`，詳見[進階模型](../models/advanced.md#sec-advanced)。

<!-- api: agora.utility_viz.getting_started_quickstart_2 -->

依價格與所得求解，回傳不可變的 `Equilibrium` 物件。

```python
from utility_viz import solve

eq = solve(model, px=2.0, py=3.0, income=30.0)
print(eq.x, eq.y, round(eq.utility, 3))

# 7.5 5.0 6.124
```

<!-- api: agora.utility_viz.getting_started_quickstart_3 -->

以指定效用值為中心，產生 $n$ 個效用水準。[消費者均衡。](quickstart.md#fig-quickstart) 使用 `n=5`，因此繪製五條無異曲線。

`levels.around()` 會保留指定的效用值，均衡點會落在其中一條無異曲線上。若直接傳入 `levels=5`，畫布會依取樣到的效用範圍選取水準，不保證包含均衡效用。要比較多張圖上的同一組偏好，可先計算一次 `lvls`，再讓各張圖使用相同水準。

<!-- api: agora.utility_viz.getting_started_quickstart_4 -->

建立畫布並設定座標範圍，其餘參數詳見[Canvas 畫布](../guides/canvas.md#sec-canvas)。

座標範圍只控制顯示區域，不參與 `solve()` 的計算。均衡點未出現在圖中時，檢查 `eq.x` 與 `eq.y` 是否超出範圍，再調整座標上限。

<!-- api: agora.utility_viz.getting_started_quickstart_5 -->

在同一張畫布上加入無異曲線、預算線或均衡點。這些方法可以串接呼叫（詳見[串接呼叫](../guides/canvas.md#sec-chaining)）。`add_equilibrium()` 使用既有的求解結果，不會重新求解；若之後修改價格、所得或模型，需重新呼叫 `solve()`，並建立對應的新圖。

<!-- api: agora.utility_viz.getting_started_quickstart_6 -->

`save()` 依副檔名匯出檔案（詳見[匯出](../guides/export.md#sec-export)）；`show()` 開啟 `matplotlib` 互動視窗。輸出路徑以執行程式時的工作目錄為準，若需指定子目錄，請事先建立目錄。

### 檢查輸入與求解失敗

價格與所得必須為正；輸入不符合條件時，`solve()` 拋出 `InvalidParameterError` (一般平滑模型使用序列最小平方法（sequential least squares programming, SLSQP） 求解。)。

求解未收斂時，`solve()` 拋出 `OptimizationError`，不會回傳無效的均衡點。

```python
from utility_viz import (
    InvalidParameterError,
    OptimizationError,
    solve,
)

try:
    eq = solve(model, px=2.0, py=3.0, income=30.0)
except (InvalidParameterError, OptimizationError) as error:
    print(error)
else:
    print(round(eq.x, 3), round(eq.y, 3), eq.bundle_type)
```

套件拋出的所有例外都繼承自 `UtilityVizError`，捕捉它即可一併處理。1.x 的名稱 `EconVizError` 是同一個類別。

數值解可能有微小誤差，例如結果接近但不恰好等於 `7.5`。驗證時應使用適當容許誤差；顯示結果時再用 `round()` 格式化，避免過早四捨五入影響後續計算。
