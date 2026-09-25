---
seo_title: "把圖形匯出成 PNG、PDF、SVG 與 GIF"
description: "把 econ-viz 經濟學圖形存成 PNG、PDF 或 SVG 用於論文與簡報，也可以匯出 GIF 動畫，或開啟互動式 matplotlib 視窗。"
---

# 匯出

![匯出的多面板圖](../assets/consumer/figure_side_by_side.png)

## 點陣與向量格式

呼叫 `cvs.save()`，副檔名用 `.png`、`.pdf` 或 `.svg`：

```python
cvs.save("figure.png")   # PNG at the canvas DPI (default 300)
cvs.save("figure.pdf")   # PDF (vector, DPI ignored)
cvs.save("figure.svg")   # SVG (vector, DPI ignored)
```

`Canvas` 的 `dpi` 參數控制點陣圖的解析度：

```python
cvs = Canvas(x_max=20, y_max=15, dpi=150)   # lower DPI for faster preview
```

DPI 會限制在 1–1200 之間。

## 匯出 GIF 動畫

要輸出多個影格時，改用 `Animator`，不要用 `Canvas.save()`：

```python
from econ_viz.animation import Animator

Animator(draw_frame, frames=frames).save("animation.gif", fps=12, dpi=120)
```

參數、價格、所得與只有預算線的變動範例，請見[動畫](animation.md)頁面。

## 互動視窗

呼叫 `cvs.show()` 會開啟即時的 matplotlib 視窗，而不是存檔：

```python
cvs.show()
```

在命令列工具中，省略 `--output` 就會有同樣的效果：

```bash
econ-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```
