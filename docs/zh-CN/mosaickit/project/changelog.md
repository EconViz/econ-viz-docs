---
seo_title: "更新记录"
---

<span id="sec-changelog"></span>

# 更新记录

本章列出影响软件包使用的版本变更，不列仅修改文档的版本。按照 l3doc 惯例，每个条目都标注在它所描述的功能旁，因此所列页码就是该功能的实际页码。

## 1.0.0rc6

- 各软件包声明 `econ_toml.Schema`，由 mosaickit 解析 `econ-viz.toml`；新增共用主题（`mosaickit.themes`）与标签微调（`Nudge`） [简介](../guides/introduction.md)
- `Nudge` — 新增 [区域标签与点标签](../guides/labels.md)
- `Schema` — 新增；软件包声明自己的键，由 mosaickit 解析文件 [主题与配置](../guides/themes.md)
- `get_tokens` — 新增 [主题与配置](../guides/themes.md)

## 1.0.0rc5

- 新增 `mosaickit.econ_toml`，读取每个 EconViz 软件包共用的 `econ-viz.toml` 区段 [简介](../guides/introduction.md)

## 1.0.0rc4

- 已解析的字体可跨符号链接共用；设置字体后的标题基线与 Matplotlib 的标题一致 [简介](../guides/introduction.md)

## 1.0.0rc3

- 标题与夹有 `$...$` 数学式的文字改用设置的文字字体排版，中文不再显示为方框 [简介](../guides/introduction.md)

## 1.0.0rc2

- 绘制更快，输出不变：标签布置、点的检查与 Matplotlib 的 mathtext 解析改用数组，并使用只在单次绘制或保存期间有效的缓存 [简介](../guides/introduction.md)

## 1.0.0rc1

- 移除已弃用的 `Animation` 与 `TextStyle.family`（详见参数与样式两章） [简介](../guides/introduction.md)
- `TextStyle` — 移除 `family`；改以 `font` 选择字体，并用 `TextFonts` 换成自己的字体文件。字段请以名称传入；含 `"family": null` 的场景文档仍可加载，指定字体家族名称的则会被拒绝 [样式与颜色](../guides/styles.md)
- `Animation` — 移除 0.6.0 起弃用的 `Animation`、`Animation.sweep()` 与 Matplotlib 播放辅助函数；动画改由 `kinetickit` 负责，`CanvasGrid.sweep()` 与 `canvas.bind()` 仍为每个值画一格 [参数与网格](../guides/parameters.md)

## 0.9.2

- `TikZ` — `font` 对应到 TeX 字体家族 [样式与颜色](../guides/styles.md)

## 0.9.1

- `TextStyle` — 新增 `font` 字段；`family` 弃用 [样式与颜色](../guides/styles.md)
- `TextFonts` — 新增 `serif` 与 `mono`；默认为 DejaVu [样式与颜色](../guides/styles.md)

## 0.9.0

- `TextStyle` — `weight` 不再弃用 [样式与颜色](../guides/styles.md)
- `TextFonts` — 新增；sans 接一个文件列表 [样式与颜色](../guides/styles.md)
- `Config` — 新增 `Config.math_font` 与 `Config.fonts` [主题与配置](../guides/themes.md)

## 0.8.0

- `DashStyle` — `DashStyle` 与 `ArrowStyle` 接受简写，让其他包可直接当作自己的线型与箭头枚举 [样式与颜色](../guides/styles.md)

## 0.5.1

- 绘图区边缘的标记完整画出；中心在绘图区外的标记略过 [图层与坐标轴](../guides/layers.md)

## 0.5.0

- 虚线、点线或点划线应用在箭身；箭头维持实线 [图层与坐标轴](../guides/layers.md)
- `CanvasGrid` — 新增 `links` [参数与网格](../guides/parameters.md)

## 0.4.0

- 内侧大括号的标签在尖端外没有空位时改以引线拉出（先前会重叠并发出警告） [坐标轴注释](../guides/annotations.md)

## 0.3.2

- 只有点严格位于区域内部时，该区域才算是点自己的区域；位于区域边上的点，标签仍放在区域外 [区域标签与点标签](../guides/labels.md)

## 0.3.1

- 点标签可以位于包含其点的填色区域内 [区域标签与点标签](../guides/labels.md)

## 0.3.0

- 坐标轴标题改放在箭头尖端之外，不再置中于尖端 [图层与坐标轴](../guides/layers.md)
- `mosaickit` — 坐标轴外的文字按栏排列：标记、外侧大括号（每条轨道一栏）、注释；标记与注释会沿轴分散，互不重叠 [坐标轴注释](../guides/annotations.md)
- 默认主题新增 `axes.note` 角色 [坐标轴注释](../guides/annotations.md)
- `mosaickit` — 点标签先于区域标签放置，区域的引线标注因此会避开它们；标签文字按旋转角度测量 [区域标签与点标签](../guides/labels.md)
- `Placement.leader` 可以是 `None` [区域标签与点标签](../guides/labels.md)
- 新增 `place_point_label` 与 `place_beside` [区域标签与点标签](../guides/labels.md)
- `Palette` — 主题与样式以调色板名称引用颜色，在创建渲染计划时按 `Config.palette` 解析；未知名称引发指明角色、字段与调色板的 `ConfigurationError` [样式与颜色](../guides/styles.md)
- 新增 `Config.palette`，默认为 `DEFAULT_PALETTE` [主题与配置](../guides/themes.md)
- `Config.load` — TOML 接受 `[palette]` 表，样式颜色可以是调色板名称，并在加载文件时检查 [主题与配置](../guides/themes.md)
- 新增 `expand`（默认 `True`） [绘制](../guides/rendering.md)

## 0.2.0

- `mosaickit` — 内置渲染器在第一次使用时按名称加载；核心不再导入 Matplotlib 后端 [安装](../installation.md)
- `LayoutWarning` — 新增，在没有任何引线标注位置能避开所有障碍物时发出 [画布与场景](../guides/canvas.md)
- 新增 `clip`（默认 `True`）；箭头不再于路径末端重画实线，虚线箭头因此保持虚线 [图层与坐标轴](../guides/layers.md)
- `anchor` 接受四个角 `top-left`、`top-right`、`bottom-left`、`bottom-right` [图层与坐标轴](../guides/layers.md)
- 箭头不再被坐标轴裁切 [图层与坐标轴](../guides/layers.md)
- 坐标轴默认改画实心三角箭头；轴线不受裁切，在绘图区边缘保持完整宽度 [图层与坐标轴](../guides/layers.md)
- `mosaickit.layout` — 新增：标签布局背后的纯几何模块 [布局几何](../guides/geometry.md)
- `DEFAULT_PALETTE` — 新增：灰阶、`white`、`blue`、`red` 与 `teal`；默认主题的颜色取自此调色板，`primary`、`secondary` 与 `accent` 改为蓝、红、青绿 [样式与颜色](../guides/styles.md)
- `resolve` — `themes.resolve` 接受 `overrides`，在主题之后依次应用 [主题与配置](../guides/themes.md)
- `Layer` — 图层声明 `style_slots`；Matplotlib 绘制改由各类型的注册表驱动 [绘制](../guides/rendering.md)

## 0.1.1

- PyPI 上的软件包信息链接首页、仓库、问题追踪、更新记录与发布说明 [简介](../guides/introduction.md)

## 0.1.0

- 首次发布：不可变的场景与图层、稀疏样式、具命名空间的主题、画布、可跨格的网格、参数表达式、动画、以任务为范围缓存的 Matplotlib 绘制，以及严格的 TOML 配置 [简介](../guides/introduction.md)

