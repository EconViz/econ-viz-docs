---
seo_title: "新增圖形"
---

# 新增圖形

<span id="sec-adding"></span>

要畫哪些圖由儲存庫的議題與里程碑決定。統計圖與會計方塊不繪製。新增一張圖有五個步驟。

+ *模型。*把方程式放進 `macro_viz/<topic>/models.py` 的凍結 dataclass。檢查輸入並引發 `ValidationError`。不匯入繪圖器。
+ *比較。*在 `analysis.py` 加一個 `analyze_*` 函式，回傳兩個模型與各項變動的方向。
+ *繪圖函式。*用 `_theory.py` 的工具寫 `macro_viz/visuals/<topic>.py`。裡面不寫任何顯示文字。
+ *文字。*把每個詞以穩定的編號（`islm.curve.is`）加入 `locale/labels.json` 的三種語言。
+ *匯出、範例與測試。*把名稱加進 `visuals/__init__.py`，寫一個從 `examples/examples.toml` 讀數字的 `examples/scripts/<topic>/<script>.py`，並測試模型、參數改變會讓圖形改變、`title=None` 不畫標題，以及沒有標籤蓋到線。

```python
from macro_viz.i18n import Labels
from macro_viz.visuals._theory import (
    curve,
    drop_lines,
    marked_point,
    point_name,
    theory_canvas,
    trim,
)


def demand_canvas(intercept, slope, x_max, *, title=None):
    text = Labels()
    y_max = intercept
    canvas = theory_canvas(
        x_max,
        y_max,
        labels=text,
        x_label_id="keynesian.axis.income",
        y_label_id="keynesian.axis.demand",
        title=title,
    )
    line = [(0.0, intercept), (x_max, intercept - slope * x_max)]
    canvas.extend(
        curve(
            trim(line, x_max, y_max),
            layer_id="macro.demo.demand",
            role="macro.curve.primary",
            label=text("keynesian.curve.demand"),
        )
    )
    return canvas
```

## 理論圖工具

<span id="sec-kit"></span>

`macro_viz.visuals._theory` 的工具負責各圖共用的部分，每個都有穩定的編號與主題角色。

<!-- api: macro_viz.guides_adding_figure_1 -->

由原點出發、帶箭頭座標軸與符號軸標題的畫布，可加標題。`x_max` 與 `y_max` 是軸長。

<!-- api: macro_viz.guides_adding_figure_2 -->

通過 `points` 的曲線，名稱放在右端。角色說明它是什麼：`macro.curve.primary` 或 `secondary` 是粗曲線，加上 `.shifted` 後綴就是變動後的細實線。畫布會把名稱放在末端第一個空的斜角位置：右下、左上、左下、右上。

<!-- api: macro_viz.guides_adding_figure_3 -->

表示平行移動的細實線直線箭頭。它從舊均衡出發、結束於新曲線，所以橫向移動是水平的，上下移動是垂直的。

<!-- api: macro_viz.guides_adding_figure_4 -->

唯一彎曲的箭頭，用於斜率改變：曲率平緩，凹面朝下。彎曲的程度是參數 `BULGE`，以箭頭長度的比例表示。

## 慣例

- 變動後的曲線是細實線，不用虛線；平行移動用直線箭頭；彎曲箭頭只代表轉動。
- 點狀輔助線把點接到座標軸，軸上的記號標示它的值。
- 只有價格 `p` 用小寫；其他變數用大寫斜體。縮寫與點名保持原有的大小寫。
- 沒有任何寫死的數值：文字來自語系表，數字來自參數，顏色、線寬與字型來自主題。
- 主題一律是白底。範例使用 `manual`。

## 檢查

```bash
uv run ruff check . && uv run ruff format --check .
uv run mypy
uv run pytest
```
