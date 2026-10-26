---
seo_title: "输出格式"
---

# 输出格式

<span id="sec-outputs"></span>

同一个场景与同一段动作可以驱动所有输出，由目的档的扩展名决定格式。

| 格式 | 能力 | 2D | 3D | 交互 | 保留矢量 |
| --- | --- | :-: | :-: | :-: | :-: |
| 动态 SVG | `vector` | 是 | 投影（采样） | 否 | 是（2D） |
| GIF | `raster` | 是 | 投影 | 否 | 否 |
| HTML | `interactive` | 是（原生 SVG 与播放器） | 是（原生 3D，可旋转与缩放） | 是 | 2D 是 |

<!-- api: kinetickit.guides_outputs_1 -->

不可变的导出报告，记录格式、绘图端、输出目标、尺寸、长度、保留或降级的功能、警告与网络依赖。

<!-- api: kinetickit.guides_outputs_2 -->

返回已登录的输出格式 `('gif', 'html', 'svg')`。它不检查选用依赖：没有 `kinetickit[raster]` 时存成 GIF，会抛出附有安装提示的 `CapabilityError`。

<!-- api: kinetickit.guides_outputs_3 -->

导出器登录表的底层入口。一般用户通常调用 `Animation.save()`。

<!-- api: kinetickit.guides_outputs_4 -->

声明绘图端支持哪些场景维度、几何、功能、输出与交互。

<!-- api: kinetickit.guides_outputs_5 -->

KineticKit 由场景、动作、交互与无障碍数据推算出的动画所需能力。

<!-- api: kinetickit.guides_outputs_6 -->

在写入任何文件之前，先算出动画的 `Requirements`。每次导出都会先拿它和绘图端的能力比对：不支持的组合会抛出 `CapabilityError`，指出缺少的能力并附上提示，导出失败时也不会留下任何文件。

动态 SVG 采用 SVG 的矢量场景模型 [{W3C} (2018)](../project/references.md#svg2) 与声明式 SMIL 时序 [{W3C} (2008)](../project/references.md#smil3)。KineticKit 会写入明确的数值与时间，播放时不需要 Python。

## 选项
<span id="sec-options"></span>

`save()` 会把关键字选项交给所选的输出。

| 输出 | 选项 |
| --- | --- |
| SVG | `width`、`height`、`loop`（缺省 `False`）、`title`、`description`、`samples`、`embed_fonts`、`reduced_motion`、`degradation` |
| GIF | `width`、`height`、`fps`、`dpi`、`loop`、`colors`、`dither`、`palette`、`disposal`、`accessibility`、`description` |
| HTML | `width`、`height`、`packaging`、`autoplay`、`loop`、`speed`、`controls`、`fps`、`max_frames`、`title`、`description`、`lang` |

`loop=True` 让 SVG 无限重播。GIF 缺省无限重播，除非设成 `loop=None`。不认得的选项名称会抛出错误。

## GIF 设置

<!-- api: kinetickit.guides_outputs_7 -->

选项中属于 GIF 的部分：帧率、调色板、递色、循环、处置方式与无障碍文本。

<!-- api: kinetickit.guides_outputs_8 -->

把已编码的 PNG 帧串流写入 GIF，不必把所有解码后的帧留在内存。

点阵输出一次只画一张帧，所以内存不会随长度成长。DPI 最高到 1200。GIF 不接受短于 10 毫秒的帧间隔。时间会分配到整数百分之一秒，并把误差往后带，所以总长度维持正确。点阵工作量过大时会发出 `RenderCostWarning`，不会偷偷降低尺寸或 DPI。

## HTML 封装

`packaging="offline"` 会内嵌运行环境，不需要网络；`packaging="compact"` 会引用固定版本的 CDN 资源，并把网址写进 `ExportManifest.network_dependencies`。2D 场景是内嵌的动态 SVG，由一个没有外部依赖的小型播放器驱动：播放、暂停、跳转、逐格、速度、循环与标记，可用键盘操作，也能平移与缩放。3D 场景会依 `fps`（缺省 30，最多 `max_frames` 张）预先采样，由私有的绘图运行环境显示，并支持原生的旋转与缩放。

## 能力说明

- **矢量 3D** 是随时间变化的 2D 投影，着色是平面烘焙的，绘制顺序（画家算法）在 $t = 0$ 固定。如果有图元进入或离开视野，它会失败，而不是乱猜。
- **1.0.0b2 不支持：**视频编码、音频、物理、多面板版面、隐函数曲面、3D 文本、拖曳交互，以及 3D 场景上的动态叠层。

## 没有 JavaScript 或动态时的替代方案

| 情况 | 行为 |
| --- | --- |
| 没有 JavaScript 的 2D HTML | 内嵌的 SVG 以原生方式（SMIL）播放一次；控制项无作用 |
| 没有 JavaScript 的 3D HTML | `<noscript>` 区块显示最后状态的静态 SVG |
| 当作 `<img>` 使用的 SVG | 动画会播放；脚本（包括减少动态的处理）会被忽略 |
| GIF | 没有运行时的语意；使用输出清单的说明与代表性 PNG |
| `prefers-reduced-motion` | 不自动播放；显示代表性状态（缺省是最后一格）；仍可按播放 |

## 各格式保留什么

每次导出的 `ExportManifest.preserved` 与 `.degraded` 都会列出这份信息。

| 语意 | SVG | HTML | GIF |
| --- | --- | --- | --- |
| 标题、说明 | 有 | 有 | 只在输出清单 |
| 角色、标签、说明文本 | 有（`role`、`aria-label`、`<title>`、`<desc>`） | 有 | 无 |
| 阅读顺序 | `data-kk-order`（DOM 顺序是叠放顺序） | 有（依序的文本清单） | 无 |
| 可用键盘操作的控制项 | 不适用 | 有（原生按钮、滑杆、菜单） | 不适用 |
| 交互 | 依政策舍弃，标为 `required` 时报错 | 有 | 依政策舍弃，或报错 |
| 字体 | 以 `@font-face` 嵌入子集 | 通过内嵌的 SVG | 画进像素 |
| 稳定的对象编号 | `data-kk-id` | `data-kk-id` 与 `objects` 对照表 | 不适用 |

投影后的 3D 输出只保留可绘制节点的编号，群组与光源没有自己的元素。
