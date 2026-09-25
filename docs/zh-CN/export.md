---
seo_title: "把图形导出成 PNG、PDF、SVG 与 GIF"
description: "把 econ-viz 经济学图形保存为 PNG、PDF 或 SVG 用于论文与演示文稿，也可以导出 GIF 动画，或打开交互式 matplotlib 窗口。"
---

# 导出

## 位图与矢量格式

调用 `cvs.save()`，扩展名用 `.png`、`.pdf` 或 `.svg`：

```python
cvs.save("figure.png")   # PNG at the canvas DPI (default 300)
cvs.save("figure.pdf")   # PDF (vector, DPI ignored)
cvs.save("figure.svg")   # SVG (vector, DPI ignored)
```

`Canvas` 的 `dpi` 参数控制位图的分辨率：

```python
cvs = Canvas(x_max=20, y_max=15, dpi=150)   # lower DPI for faster preview
```

DPI 会限制在 1–1200 之间。

## 导出 GIF 动画

要输出多个帧时，改用 `Animator`，不要用 `Canvas.save()`：

```python
from econ_viz.animation import Animator

Animator(draw_frame, frames=frames).save("animation.gif", fps=12, dpi=120)
```

参数、价格、收入与只有预算线的变动范例，请见[动画](animation.md)页面。

## 交互窗口

调用 `cvs.show()` 会打开即时的 matplotlib 窗口，而不是存盘：

```python
cvs.show()
```

在命令行工具中，省略 `--output` 就会有同样的效果：

```bash
econ-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```
