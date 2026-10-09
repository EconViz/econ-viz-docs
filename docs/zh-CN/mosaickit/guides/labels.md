---
seo_title: "区域标签与点标签"
---

# 区域标签与点标签

<span id="sec-labels"></span>

标签用于命名已绘制的填色区域或点。标签图层会在所有其他图层之后，由延后处理程序绘制，因此能判断必须避开哪些对象。点标签先于区域标签放置；每个已放置的标签，都会成为后续标签的障碍物。

## 区域标签

<!-- api: agora.mosaickit.guides_labels_1 -->

为填色区域命名；区域可以是 `FillLayer` 的 id，也可以是至少由三点组成的多边形。`stroke` 设置引线标注的引线样式。

“文字放得下”是指：文字矩形置中于极点、每边留白 2 pt 后，仍位于区域内（参见[多边形内的矩形](geometry.md#thm-rect-inside)），且不碰到任何线条、标记、文字或其他区域。[区域内标签与引线标注。](labels.md#fig-regions)同时呈现这两种结果。

<span id="fig-regions"></span>

![区域内标签与引线标注。](../../../assets/mosaickit/agora/labels/regions.svg){ .ev-figure-sm }

## 点标签

<!-- api: agora.mosaickit.guides_labels_2 -->

在点的旁边加上文字为它命名，不使用引线。点的*足迹*是该处画有标记时的标记，否则就是点本身。

标签在足迹周围尝试 16 个方向，距足迹边缘 4、7、11、16 pt，由近而远。同一距离内根据[候选顺序](labels.md#def-candidate-order)的顺序尝试方向（参见[方向的尝试顺序。](labels.md#fig-candidates)），第一个不遮盖任何对象的位置胜出；若都不行，选违规数最少者（相同时取较早者），并发出指出该图层的 `LayoutWarning`。点严格位于其内部（距边缘超过 1.5 px）的区域是标签应在之处，不算障碍物。

<span id="def-candidate-order"></span>

!!! abstract "定义 · 候选顺序"

    将方向自 $+x$ 起逆时针编号为 $k = 0, \ldots, 15$，角度为 $2 \pi k / 16$。点标签按键值 $(\min(s, 16 - s), [s > 8])$（$s = (k - 2) \mod 16$）递增的顺序尝试：按与右上方向 $k = 2$ 的角距离，角距离相同的两个方向则逆时针者优先。

<span id="fig-candidates"></span>

![方向的尝试顺序。](../../../assets/mosaickit/agora/geometry/candidates.svg){ .ev-figure-sm }

<span id="fig-points"></span>

![点旁的点标签。](../../../assets/mosaickit/agora/labels/points.svg){ .ev-figure-sm }

## 硬性限制

两种标签都遵守同一条规则：不遮盖任何对象。障碍物包括坐标轴上已绘制的内容：路径的线段、标记与文字的矩形，以及填色区域的多边形。以下搜索函数位于 `mosaickit.layout.placement`；除 `place_beside` 外，也都由 `mosaickit.layout` 导出。它们与几何模块一样，以显示像素为单位运算；`scale` 则将以点为单位的间距换算为像素。

<!-- api: agora.mosaickit.guides_labels_3 -->

`Obstacles` 表示标签必须避开的障碍物；`Placement` 表示标签的放置结果，包括矩形、引线线段（不画引线的标签为 `None`）及违反的限制数。`Obstacles.extended(segments=..., rects=...)` 加入刚放置的标签。

<span id="def-violations"></span>

!!! abstract "定义 · 违规数"

    对候选矩形 $R$、障碍物 $O$、绘图区界线 $B$ 与多边形集合 $\mathcal{P}$，*违规数*为

    $$
    V(R) = [R \nsubseteq B] + \#\lbrace s \in O_\text{seg} : R \cap s \ne \emptyset\rbrace + \#\lbrace Q \in O_\text{rect} : R \cap Q \ne \emptyset\rbrace + \#\lbrace P \in \mathcal{P} : R \cap \overline{P} \ne \emptyset\rbrace ,
    $$

    其中 $[\cdot]$ 在条件成立时为 1，否则为 0。$V(R) = 0$ 时称候选位置*不遮盖任何对象*。

各项分别由[线段与矩形](geometry.md#lem-rect-segment)、`Rect.intersects` 与[与多边形重叠的矩形](geometry.md#cor-rect-overlap)精确计算。

## 引线标注

<!-- api: agora.mosaickit.guides_labels_4 -->

在区域周围为给定大小的引线标注搜索位置。从极点 $o$ 沿 16 个方向 $r$，把候选矩形放在距离 `ray_exit(o, r, P)` 再加 12、24 或 40 pt（近环）之处，并以面向极点的边或角对齐，使矩形朝远离区域的方向延伸。引线从极点拉向矩形上的最近点（参见[矩形上的最近点](geometry.md#lem-nearest)），并在距该点 2 pt 处停止。候选位置的代价为 $V(R)$（区域本身也列入多边形），中心不在开阔空间时加一，引线离开自身区域后每穿过一条线、一段文字或一个其他区域加一，每位于一个交叉点之外（参见[开阔空间与交叉点](labels.md#def-beyond)）再加一。

<span id="def-beyond"></span>

!!! abstract "定义 · 开阔空间与交叉点"

    *开阔空间*是在绘图区 4 pt 网格上、面积至少占十分之一的连通空白区域的联集；较小的空白区域称为*口袋*，例如两个阴影区域间未填色的窄带，文字放在那里看起来像在为口袋命名。区域的*交叉点*是两条障碍线段真正交叉（各自严格穿过对方）之处，且位于区域边界上或距边界 1.5 px 以内。从极点 $o$ 看，若 $(p - x) \cdot (x - o) > 0$，则称点 $p$ 位于 $x$ *之外*。

越过交叉点后，线条朝远离区域的方向分开；若把标签放在那里，看起来会贴近线条的延伸方向，而不是所命名的区域。交叉点本身由方向测试求得。

<span id="lem-crossing"></span>

!!! abstract "引理 · 交叉点"

    若 $[a, b]$ 与 $[c, d]$ 真正交叉，则它们恰交于一点 $a + t (b - a)$，其中

    $$
    t = ((c - a) \times (d - c)) / ((b - a) \times (d - c)) \in (0, 1),
    $$

    而 $u \times v = u_x v_y - u_y v_x$。

<span id="prop-callout"></span>

!!! abstract "命题 · 引线标注的选择"

    以键值（代价, 引线长度）按字典序排列候选位置，并逐方向、由近到远的距离枚举。若近环中有代价为 0 的候选，`place_callout` 返回其中引线最短的第一个；否则再尝试远环（60 与 90 pt），返回两环中键值最小的第一个候选。结果只取决于参数。

返回的代价不为零时，渲染器仍会在该处画出引线标注，并发出指出该图层的 `LayoutWarning`；放大画布或缩短文字通常就能消除。

<!-- api: agora.mosaickit.guides_labels_5 -->

其他搜索：置中于极点的矩形，若放得下且除自身区域外不碰到任何对象就返回它；前述的点标签搜索；以及大括号尖端旁的搜索，在尖端外 3 到 45 pt 尝试，并沿跨距以 3 pt 为步长最多滑动 `reach`，位移小者优先。`place_beside` 返回矩形与其违规数。大括号标签在该处没有空位时，渲染器改从尖端尝试引线标注，保留违规较少者。
