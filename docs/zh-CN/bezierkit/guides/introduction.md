---
seo_title: "简介"
---

# 简介

<span id="sec-intro"></span>

`bezierkit` 是处理 Bézier 曲线的小型数学工具软件包。它可由控制点或端点条件构造曲线，计算曲线值与导数，分割与截取曲线，将曲线拟合到函数、采样点与等值线，并输出为 JSON、SVG 路径数据或 TikZ。软件包本身不绘图，绘图交给 Matplotlib、`mosaickit` 或 LaTeX 文档等绘图端，它们收到的是精确的三次控制点。

## 符号

点或向量位于某个维度 $d \ge 1$ 的 $\mathbb{R}^d$ 中；多数图使用 $d = 2$。$x \in \mathbb{R}^d$ 的欧氏范数为

$$
\left\lVert x \right\rVert = \sqrt{x_1^2 + \ldots + x_d^2},
$$

$\left\lVert x \right\rVert_\infty = \max_k |x_k|$ 为最大范数。集合 $S \subseteq \mathbb{R}^d$ 若对所有 $p, q \in S$ 与 $\lambda \in [0, 1]$ 都有 $\lambda p + (1 - \lambda) q \in S$，称为凸集；有限个点的凸包是它们所有凸组合 $\sum_i \lambda_i P_i$（$\lambda_i \ge 0$ 且 $\sum_i \lambda_i = 1$）的集合。映射 $A: \mathbb{R}^d \to \mathbb{R}^e$ 若可写成 $A(x) = M x + v$（$M$ 为矩阵，$v$ 为向量），称为仿射映射。函数若有直到 $k$ 阶的连续导数，称为 $C^k$。

$n$ 次 Bézier 曲线有 $n + 1$ 个控制点 $P_0, \ldots, P_n$，定义为映射

$$
B(t) = \sum_{i=0}^n b_{i,n}(t) P_i, \quad t \in [0, 1],
$$

其中

$$
b_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}
$$

为 Bernstein 多项式（详见[Bézier 曲线](curves.md#sec-curves)）。依次连接控制点即为控制多边形。软件包中每条曲线的参数范围都是 $[0, 1]$；超出范围的参数会抛出 `ParameterOutOfDomain`。符号 $d$ 一律表示维度，容差写作 $\epsilon$。

## 数学与证明

各章先回顾所用的标准定义并附出处，再以编号的引理、命题、定理与推论陈述算法所依据的性质：Bernstein 基底的保证、de Casteljau 算法为何能计算并分割曲线、Hermite 插值最多偏离多少、导出器因四舍五入损失多少精度。证明集中在[证明](../project/proofs.md#app-proofs)，只想了解 API 时可略过。属于本软件包而不见于文献的约定，称为软件包约定。标准参考书为 [Farin (2002)](../project/references.md#farin2002) 与 [Prautzsch (2002)](../project/references.md#prautzsch2002)；Bernstein 基底另见 [Farouki (2012)](../project/references.md#farouki2012)。

## 阅读指引

<span id="tab-guide"></span>

| 主题 | 内容 | 章节 |
| --- | --- | --- |
| 点、向量、参数、异常 | [几何数值对象](geometry.md#sec-geometry) | Bernstein 基底、曲线、求值 |
| [Bézier 曲线](curves.md#sec-curves) | 导数、反转、分割 | [导数、反转与分割](operations.md#sec-operations) |
| 三次线段与分段路径 | [三次线段与路径](paths.md#sec-paths) | 构造与 Hermite 插值 |
| [建构与 Hermite 插值](construction.md#sec-construction) | 拟合函数与折线 | [拟合](fitting.md#sec-fitting) |
| 描绘等值线 | [等值线](implicit.md#sec-implicit) | 采样、JSON、SVG、TikZ、Matplotlib |
| [采样与导出](export.md#sec-export) | 命令行 | [命令行界面](../cli.md#sec-cli) |

初次使用时，先读[快速开始](../quickstart.md#sec-quickstart)与[Bézier 曲线](curves.md#sec-curves)。本手册的图本身就是 `bezierkit` 的输出：每条曲线都由[采样与导出](export.md#sec-export)的 TikZ 导出器写出，再以 LaTeX 编译。
