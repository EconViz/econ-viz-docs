---
seo_title: "在 Jupyter 中操作互動式經濟學圖形"
description: "在 Jupyter 筆記本中用 econ-viz 的 WidgetViewer 滑桿與數字輸入框，互動探索效用函數與預算限制。"
---

# 互動元件

`WidgetViewer` 會在筆記本儲存格中繪製 `econ-viz` 圖形，只要控制項一變動就重新繪製。從 `v1.4.0` 起，每個參數都同時有**滑桿**和**數字輸入框**，使用者可以拖曳培養直覺，也可以輸入精確數值，方便教學與示範。

## 安裝

```bash
uv add "econ-viz[interactive]"
```

如果也要匯出 GIF：

```bash
uv add "econ-viz[all]"
```

## 基本用法

```python
from econ_viz import Canvas, levels, solve
from econ_viz.interactive import WidgetViewer
from econ_viz.models import CobbDouglas

def draw(alpha: float, px: float) -> Canvas:
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    eq = solve(model, px=px, py=2.0, income=20.0)

    return (
        Canvas(x_max=14, y_max=12, x_label="X_1", y_label="X_2", title="Interactive equilibrium")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(px=px, py=2.0, income=20.0, fill=True)
        .add_equilibrium(eq, show_ray=True, drop_dashes=True)
    )

WidgetViewer(
    draw,
    alpha=(0.2, 0.8, 0.05),
    px=(1.0, 6.0, 0.25),
).show()
```

## 互動元件做了什麼

- 為每個參數建立一個 `FloatSlider`。
- 為每個參數建立一個連動的 `FloatText` 輸入框。
- 讓滑桿與輸入的數值保持同步。
- 重新繪製前會先清掉舊圖，筆記本儲存格裡不會堆積一堆過時的圖。

## Colab 與 Jupyter 注意事項

在全新的筆記本執行環境中，尤其是 Colab：

1. 先執行一次安裝儲存格。
2. 如果 `ipywidgets`、`traitlets` 或 `IPython` 被升級了，**重新啟動一次執行環境**。
3. 重新啟動後跳過安裝儲存格，從 import 儲存格繼續執行。

隨套件附上的 Playground 筆記本已經照這個流程設計，若環境中已經有 `econ-viz 1.4.0`，就不會重新安裝。

## 什麼時候用互動元件，什麼時候用 GIF

- 學生需要輸入或拖曳參數、一次檢查一個狀態時，用 `WidgetViewer`。
- 想在簡報、文件或專案網站中呈現固定、可重複播放的變動過程時，用 `Animator`。
