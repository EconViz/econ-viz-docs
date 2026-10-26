---
seo_title: "更新记录"
---

<span id="sec-changelog"></span>

# 更新记录

本章列出影响软件包使用的版本变更，不含仅修改文件的版本；各条目按 l3doc 惯例标注于它所描述的功能旁，页码即该功能的实际页码。

## 2.0.0b8

- `Label` — 添加 `top`、`bottom`、`left` 与 `right`，可微调已定位的单个标签 [Canvas 画布](../guides/canvas.md)
- `themes` — 内置主题改为 EconViz 共享主题，同一名称在各 EconViz 软件包中外观一致；添加 `manual` 主题 [主题与设置](../guides/themes.md)
- `themes` — 移除 `dark` 主题：`themes.dark` 与 `base = "dark"` 会发出警告并改用 `default` [主题与设置](../guides/themes.md)
- `Config` — utility-viz 自身的配置移至 `[utility]` 下；改由 `mosaickit` 读取并检查文件；旧格式仍可读取，但会发出警告 [主题与设置](../guides/themes.md)
- `utility-viz init` — 改为写出新格式，utility-viz 的表位于 `[utility]` 下；`--migrate` 会把表移到该处 [命令行工具](../getting-started/cli.md)
- `utility-viz plot` — `--theme` 接受所有内置主题，包括 `colorblind` 与 `manual`；`dark` 会发出警告并改用 `default` [命令行工具](../getting-started/cli.md)

## 2.0.0b7

- `Config` — 配置文件恢复为 `econ-viz.toml`，由所有 EconViz 软件包共享；`utility-viz.toml` 仍可读取，但会发出警告 [主题与设置](../guides/themes.md)
- `utility-viz plot` — 未指定 `--config` 时，读取当前目录的 `econ-viz.toml`（或 `utility-viz.toml`，并发出警告） [命令行工具](../getting-started/cli.md)

## 2.0.0b1

- 由 `econ-viz` 更名为 `utility-viz`：发行包、导入名称、命令与配置文件一并更名 [简介](../guides/introduction.md)
- 内部结构重整为 `core` 与 `models`；公开 API 为软件包根目录与 `utility_viz.models` [简介](../guides/introduction.md)
- 添加依赖 `mosaickit` 与 `bezierkit` [简介](../guides/introduction.md)
- 整个仓库通过 `mypy` 检查；Ruff 限制行长、复杂度与语句数量 [简介](../guides/introduction.md)
- `utility-viz` — 添加依赖 `mosaickit>=0.5.1,<0.6.0` 与 `bezierkit>=0.5.0rc1,<0.6.0` [安装](../getting-started/installation.md)
- `utility-viz` — 仓库改为 `uv` workspace，`utility-viz` 与 `econ-viz` 同步发布 [安装](../getting-started/installation.md)
- `econ-viz` — 更名为 `utility-viz`；`econ_viz` 包、`econ-viz` 命令与 `econ-viz.toml` 查找保留为已弃用的兼容层，于 3.0.0 移除 [安装](../getting-started/installation.md)
- `econ-viz` — 兼容层改由独立的 `econ-viz` 发行包提供，升级 1.x 安装时不再删除与 `utility-viz` 共用的文件 [安装](../getting-started/installation.md)
- `UtilityVizError` — `UtilityVizError` 成为基础异常类；`EconVizError` 保留为同一个类的别名 [快速开始](../getting-started/quickstart.md)
- `Leontief` — 折角效用函数的无差异曲线在 Matplotlib 与 TikZ 输出中保留精确直角 [核心模型](../models/index.md)
- `core.scenes` — 添加与后端无关的 `mosaickit` 图层工厂，涵盖预算线、均衡与无差异曲线，并可导出原生 Bézier TikZ [进阶模型](../models/advanced.md)
- `Config` — 默认配置文件更名为 `utility-viz.toml`；旧的 `econ-viz.toml` 仍可读取，但会发出警告 [主题与设置](../guides/themes.md)
- `Config.discover` — 添加 `Config.discover()`，找不到文件时改用内置默认值 [主题与设置](../guides/themes.md)
- `utility-viz` — 命令改为 `utility-viz`；`econ-viz` 会打印弃用警告并转交给新命令 [命令行工具](../getting-started/cli.md)
- `utility-viz plot` — 未指定 `--config` 时，读取当前目录的 `utility-viz.toml`（或旧的 `econ-viz.toml`） [命令行工具](../getting-started/cli.md)
- `utility-viz init` — 添加 `--migrate` 选项 [命令行工具](../getting-started/cli.md)
- `Animator` — 移至 `utility_viz.core.animation` [动画](../guides/animation.md)
- `WidgetViewer` — 移至 `utility_viz.core.interactive` [交互组件](../guides/interactive.md)

## 1.12.0

- 添加无差异曲线主次层级、焦点曲线及数值或序数标签 [简介](../guides/introduction.md)
- `Canvas.add_utility` — 添加焦点效用层级、次要曲线样式及序数标签 [Canvas 画布](../guides/canvas.md)
- `Theme` — 添加次要无差异曲线的颜色、线宽与不透明度设置 [主题与设置](../guides/themes.md)

## 1.11.0

- 完成主题系统，统一画布、多面板图、需求图、效应分解与 Edgeworth 箱形图的视觉设置 [简介](../guides/introduction.md)
- `Canvas` — 背景、标签、线条与标记均由主题提供默认值 [Canvas 画布](../guides/canvas.md)
- `Figure` — 面板背景、标签、线条与标记完整应用主题 [多面板图与需求图](../guides/consumer.md)
- `EdgeworthBox` — 箱框、契约曲线、核、禀赋、价格线与 Walras 均衡完整应用主题 [多面板图与需求图](../guides/consumer.md)
- `Theme` — 完成主题系统，添加背景色、标签比例及所有经济图层的默认样式 [主题与设置](../guides/themes.md)
- `themes` — 添加 `paper`、`monochrome`、`presentation` 与 `dark` [主题与设置](../guides/themes.md)
- `Config` — 配置文件可选择所有内置主题，并在各种图形间保留相同的视觉语义 [主题与设置](../guides/themes.md)
- `econ-viz plot` — `--theme` 支持所有命令行内置主题 [命令行工具](../getting-started/cli.md)

## 1.10.1

- 软件包添加 `py.typed`，并在 CI 运行 Ruff 与 Mypy 检查 [简介](../guides/introduction.md)

## 1.10.0

- `econ-viz` — Python 3.10 使用 `tomli` 读取 TOML 配置文件 [安装](../getting-started/installation.md)
- `Figure` — 未指定主题与字体时，使用当前的 `Config` [多面板图与需求图](../guides/consumer.md)
- `EdgeworthBox` — 未指定主题与字体时，使用当前的 `Config` [多面板图与需求图](../guides/consumer.md)
- `Config` — 添加 `Config`、`econ-viz.toml`、`econ-viz init` 与 `plot --config` [主题与设置](../guides/themes.md)
- `econ-viz init` — 添加配置文件模板命令与 `plot --config` [命令行工具](../getting-started/cli.md)

## 1.9.0

- `Canvas` — 坐标轴、原点、标题与其他文字元素接受 `Label` [Canvas 画布](../guides/canvas.md)
- `Stroke` — 添加 `opacity` 透明度 [Canvas 画布](../guides/canvas.md)
- `DemandDiagram` — 支持 `Legend`、`Marker`、`Label` 与各图层的 `Stroke` [多面板图与需求图](../guides/consumer.md)
- `Canvas.add_decomposition` — 默认绘制 A、B、C 所在的无差异曲线，并支持曲线标签与 `Legend` [多面板图与需求图](../guides/consumer.md)
- `Canvas.add_decomposition` — 横轴下方的效应箭头依 A→B、B→C 方向绘制；效应为零时不绘制箭头 [多面板图与需求图](../guides/consumer.md)
- `Haagsma` — 添加具有闭式解的 Haagsma 效用模型，用于劣等财与季芬财分析 [核心模型](../models/index.md)

## 1.8.0

- `Canvas` — 添加 `Axis`、`Marker`、`Label` 与 `Fill` 样式对象 [Canvas 画布](../guides/canvas.md)
- `Stroke` — 线条样式统一由 `Stroke` 表示；个别样式参数保留为简写 [Canvas 画布](../guides/canvas.md)
- `Canvas.add_decomposition` — 添加 `Effect`、`Marker` 与 `Label` 样式对象 [多面板图与需求图](../guides/consumer.md)
- `EdgeworthBox` — 标记点、文字与坐标轴接受 `Marker`、`Label` 与 `Axis` [多面板图与需求图](../guides/consumer.md)

## 1.7.0

- CI 测试 Python 3.10–3.13，强制分支覆盖率，并对可运行的示例做冒烟测试 [简介](../guides/introduction.md)
- 版本标签须通过测试后才会触发发布 [简介](../guides/introduction.md)
- `econ-viz` — 软件包管理与构建改用 `uv` [安装](../getting-started/installation.md)
- `econ-viz` — 修正示例脚本，使其可在新检出的源代码目录中直接运行 [安装](../getting-started/installation.md)
- `Canvas` — 支持为每幅图单独设置的文字与数学字体，不影响 `matplotlib` 的全局设置 [Canvas 画布](../guides/canvas.md)
- `Canvas` — `Canvas` 与 `Figure` 支持分别设置坐标轴标签位置、线条样式与箭头样式 [Canvas 画布](../guides/canvas.md)
- `Stroke` — 统一控制画布、多面板图、需求图与 Edgeworth 箱形图中线条的粗细、样式、颜色与箭头 [Canvas 画布](../guides/canvas.md)
- `CobbDouglas` — 修正效用模型的定义域、非对称 CES 的扩张路径、Cobb-Douglas 的极限情况，以及收入未花完时的饱和最优解 [核心模型](../models/index.md)
- `CobbDouglas` — 修正效用值接近零或为负时的等高线水平计算 [核心模型](../models/index.md)
- `comparative_statics` — 修正价格、收入接近零或基本需求限制时，比较静态计算超出定义域的问题 [分析](../tools/analysis.md)
- `econ-viz` — 添加 `econ-viz --version`，显示已安装的软件包版本 [命令行工具](../getting-started/cli.md)

## 1.6.0

- `examples/output/` 的输出文件不再纳入版本控制 [简介](../guides/introduction.md)
- `Canvas` — 无差异曲线的默认线宽从 `2.0` 降为 `1.8` [Canvas 画布](../guides/canvas.md)
- `themes.default` — 默认配色改为色盲友好方案，并提供 `COLORBLIND_CYCLE_RGB` 与 `COLORBLIND_CYCLE_HEX` [主题与设置](../guides/themes.md)
- `Canvas.save` — TikZ 坐标轴的回归测试不再依赖颜色索引 [导出](../guides/export.md)
- `Animator` — 动画示例移到 `examples/scripts/animation.py` [动画](../guides/animation.md)

## 1.5.0

- 添加效应分解、需求图、PCC/ICC 路径、多面板版面与 TikZ 导出的示例脚本 [简介](../guides/introduction.md)
- 添加 TikZ 导出与价格效应分解的回归测试 [简介](../guides/introduction.md)
- `econ-viz` — Colab 上的笔记本安装流程在重新启动后也能正常运作 [安装](../getting-started/installation.md)
- `Figure` — 改善共享面板版面中坐标轴标签的位置与可见度 [多面板图与需求图](../guides/consumer.md)
- `decompose_price_effect` — 价格效应分解：`decompose_price_effect()`、`PriceEffectDecomposition` 与 `Canvas.add_decomposition()`，可画出 A/B/C 消费组合以及替代与收入效应 [多面板图与需求图](../guides/consumer.md)
- `decompose_price_effect` — 效应分解的 API 可以直接从软件包根目录导入 [多面板图与需求图](../guides/consumer.md)
- `Canvas.save` — 纯 TikZ 导出后端；`Canvas.save()` 与 `Figure.save()` 接受 `.tex` [导出](../guides/export.md)

## 1.4.0

- 添加 `Animator` 与 `WidgetViewer` 的测试 [简介](../guides/introduction.md)
- `econ-viz[extras]` — 添加可选依赖 `animation`、`interactive` 与 `all` [安装](../getting-started/installation.md)
- `Animator.save` — 导出前将帧合成至不透明背景，改善 GIF 导出稳定性 [导出](../guides/export.md)
- `Animator` — `Animator` 以 `Pillow` 生成 GIF 参数变动动画，不需要 `ffmpeg` [动画](../guides/animation.md)
- `Animator` — 添加效用参数、价格、收入与仅显示预算线的 GIF 示例 [动画](../guides/animation.md)
- `WidgetViewer` — `WidgetViewer` 在 Jupyter 笔记本中提供滑块控制 [交互组件](../guides/interactive.md)
- `WidgetViewer` — 笔记本交互组件添加数值输入字段 [交互组件](../guides/interactive.md)

## 1.3.2

- 发布流程跳过 PyPI 上已有的版本 [简介](../guides/introduction.md)
- `EdgeworthBox` — Edgeworth 契约曲线与价格线默认为黑色虚线 [多面板图与需求图](../guides/consumer.md)

## 1.3.1

- 软件包根目录的导出改为延迟加载，公开 API 不变 [简介](../guides/introduction.md)
- `Canvas` — Canvas 的绘制拆成 `canvas.renderers` 与 `canvas.primitives` [Canvas 画布](../guides/canvas.md)
- `EdgeworthBox` — Edgeworth 的内部实现拆成 compute、state 与 plotter 三个模块 [多面板图与需求图](../guides/consumer.md)
- `models.registry` — 添加模型注册表（`models.registry`），供命令行工具创建模型 [核心模型](../models/index.md)
- `CobbDouglas` — 等高线水平的规则集中在 `contours.level_policies` [核心模型](../models/index.md)
- `Canvas.save` — `Canvas`、`Figure` 与 `EdgeworthBox` 共享同一个图形导出器（`io.exporter`） [导出](../guides/export.md)
- `econ-viz` — 命令行错误改为抛出 `CliConfigError`，结束处理集中在 `cli.main` [命令行工具](../getting-started/cli.md)

## 1.3.0

- `examples/edgeworth_box.py` 涵盖常见的效用函数组合 [简介](../guides/introduction.md)
- 添加 Edgeworth 测试 [简介](../guides/introduction.md)
- `EdgeworthBox` — 添加 `EdgeworthBox` 与 `EquilibriumFocusConfig`，支持两人交换经济绘图 [多面板图与需求图](../guides/consumer.md)
- `EdgeworthBox` — 契约曲线、核、Walras 均衡叠图，以及聚焦于均衡的无差异曲线 [多面板图与需求图](../guides/consumer.md)

## 1.2.3

- `slutsky_matrix` — `SlutskyMatrix` 会检查对称性、负半定性与齐次性，条件不成立时发出警告 [分析](../tools/analysis.md)
- `econ-viz models` — 命令行工具支持 `QuasiLinear`、`StoneGeary` 与 `Translog` [命令行工具](../getting-started/cli.md)

## 1.2.2

- 添加 PCC/ICC 示例生成器与测试 [简介](../guides/introduction.md)
- `PricePath` — PCC/ICC 路径默认经过平滑处理，端点略微延长，除非指定否则不显示标记 [多面板图与需求图](../guides/consumer.md)
- `PricePath` — PCC/ICC 路径改用独立配色，并增加需求图商品空间的留白 [多面板图与需求图](../guides/consumer.md)

## 1.2.0

- `Layout` — 多面板 `Figure` 版面与 `Layout` 枚举 [多面板图与需求图](../guides/consumer.md)
- `PricePath` — 添加 `PricePath`、`IncomePath` 与 `Canvas.add_path()`，支持 PCC/ICC 绘图 [多面板图与需求图](../guides/consumer.md)
- `DemandDiagram` — 添加 `DemandDiagram`，联动显示商品空间与 Marshall 需求 [多面板图与需求图](../guides/consumer.md)

## 1.1.0

- `Translog` — `Translog` 模型，以及图例与无差异曲线标签 [核心模型](../models/index.md)
- `comparative_statics` — `comparative_statics` 辅助函数 [分析](../tools/analysis.md)
- `HomogeneityAnalyzer` — 分析模块中的 `HomogeneityAnalyzer` 与 `ReturnsToScale` [分析](../tools/analysis.md)

## 1.0.2

- `econ-viz` — 删除 NumPy 的版本上限，避免在 Colab 上发生冲突 [安装](../getting-started/installation.md)
- `Canvas` — 数学式的坐标轴标签不再被重复包装 [Canvas 画布](../guides/canvas.md)

## 1.0.1

- `econ-viz` — 固定 `numpy<2`，避免 Colab 与本机安装时 ABI 不兼容 [安装](../getting-started/installation.md)
- `econ-viz` — 放宽 Python 与 NumPy 的版本限制；`pytest` 固定在 8.x [安装](../getting-started/installation.md)

## 1.0.0

- 首次发布 [更新记录](changelog.md)

