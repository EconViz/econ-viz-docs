---
seo_title: "配置文件"
description: "把 utility-viz 图形的样式保存为 utility-viz.toml 配置文件，用 Config 一次加载。"
---

# 配置文件

把颜色、线条、标签与图例的设置保存为 `utility-viz.toml`，加载一次即可，不用每个方法都传相同的参数。

## 格式

段落名称对应 Theme 的属性，字段名称与样式对象的参数相同。没写到的设置沿用内置默认值。

```toml
# utility-viz.toml
base = "default"                 # default or nord

[font]
text = "TeX Gyre Pagella"
math = "stix"

[color]
ic = "#2E86AB"
budget = "#6C3483"
equilibrium = "#C0392B"

[stroke.budget]                  # theme.budget_stroke
width = 1.5
style = "solid"

[stroke.ic]                      # theme.ic_stroke
width = 1.8
opacity = 0.9

[marker.equilibrium]             # theme.eq_marker
size = 5

[label.point]                    # theme.point_label
fontsize = 12
position = "top-right"

[label.origin]
visible = false

[fill.budget]                    # theme.budget_fill
color = "lightgrey"
opacity = 0.3

[legend]                         # theme.legend
position = "auto"
fontsize = 10
```

| 段落 | 设置的对象 | 字段 |
|------|------------|------|
| `base` | 作为基础的内置主题 | `"default"`、`"nord"` |
| `[font]` | 正文与数学字体 | `text`、`math` |
| `[color]` | Theme 的颜色，例如 `ic` → `ic_color` | 颜色字符串 |
| `[stroke.<name>]` | `theme.<name>_stroke` | `width`、`style`、`color`、`arrow`、`opacity` |
| `[marker.<name>]` | `theme.<name>_marker` | `color`、`size`、`shape`、`opacity` |
| `[label.<name>]` | `theme.<name>_label` | `position`、`offset`、`color`、`fontsize`、`visible`、`opacity` |
| `[fill.<name>]` | `theme.<name>_fill` | `color`、`opacity` |
| `[legend]` | `theme.legend` | `position`、`fontsize`、`frame`、`columns`、`visible`、`opacity` |

`eq` 也可以写成 `equilibrium`（`[marker.equilibrium]`、`[color] equilibrium`）。段落、名称或字段写错时，错误信息会列出可用的选项。

## 加载

`Config` 把主题与字体选项放在一起。从文件读进来后，可以让它成为之后所有图的默认值，也可以只把它的 `theme` 交给单独一张 `Canvas`。

### 读取配置文件 {#config_load data-toc-label="读取配置文件"}

把一个 TOML 文件读成 `Config`。

<!-- api: config.load -->

??? example "查看示例"

    ```python
    from utility_viz import Config

    config = Config.load("utility-viz.toml")
    theme = config.theme
    ```

### 自动查找 {#config_discover data-toc-label="自动查找"}

依次查找：指定的路径、`utility-viz.toml`、内置默认值。和 `Config.load` 不同的是，找不到文件时不会出错。

<!-- api: config.discover -->

??? example "查看示例"

    ```python
    from utility_viz import Config

    # 找不到文件时回到内置默认值
    config = Config.discover()
    ```

### 应用 {#config_use data-toc-label="应用"}

让这份 `Config` 成为之后创建的图的默认值，并返回它自己。只想影响单独一张图时，把它的 `theme` 传给 `Canvas(theme=...)`。

<!-- api: config.use -->

??? example "查看示例"

    ```python
    from utility_viz import Canvas, Config

    # 之后创建的图
    Config.load("utility-viz.toml").use()
    # 应用配置文件
    Canvas(x_max=20, y_max=15)

    theme = Config.load("utility-viz.toml").theme
    # 或只应用于这张图
    Canvas(theme=theme)
    ```

### 还原 {#config_reset data-toc-label="还原"}

回到内置默认值。`Config.active()` 可以查看当前使用的是哪一份 `Config`。

<!-- api: config.reset -->

<!-- api: config.active -->

??? example "查看示例"

    ```python
    from utility_viz import Config

    # 回到内置默认值
    Config.reset()
    ```

方法显式传入的参数仍然优先于配置文件：以上面的设置为例，`add_budget(..., stroke=Stroke(width=1))` 会画出 1 pt 粗、其余沿用配置文件样式的线。

## 命令行

`utility-viz init` 会生成一份带注释的模板，列出所有可以设置的名称；`utility-viz plot` 则通过 `--config` 读取同一份配置文件：

```bash
uv run utility-viz init                       # 生成 utility-viz.toml
uv run utility-viz plot --model cobb-douglas --px 2 --py 3 --income 30 \
    --config utility-viz.toml --output cd.png
```
