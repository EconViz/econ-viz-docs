---
seo_title: "效用函数模型"
description: "econ-viz 支持的效用函数一览：Cobb-Douglas、Leontief、完全替代、CES、Translog、饱和、拟线性与 Stone-Geary。"
---

# 模型目录

所有模型都放在 `econ_viz.models`，并遵循 `UtilityFunction` 协议：它们都是**可调用的 dataclass**，能对 NumPy 数组逐元素计算 `U(x, y)`。

![模型目录总览](../../assets/models/cobb_douglas.png)

## 参数化模型

| 模型 | 函数形式 | 类 |
|-------|-----------|-------|
| [Cobb-Douglas](cobb-douglas.md) | $x^\alpha y^\beta$ | `CobbDouglas` |
| [Leontief](leontief.md) | $\min(ax, by)$ | `Leontief` |
| [完全替代](perfect-substitutes.md) | $ax + by$ | `PerfectSubstitutes` |
| [CES](ces.md) | $(\alpha x^\rho + \beta y^\rho)^{1/\rho}$ | `CES` |
| [Translog](translog.md) | 弹性的对数二次效用 | `Translog` |
| [饱和](satiation.md) | $-a(x-x^*)^2 - b(y-y^*)^2$ | `Satiation` |
| [拟线性](quasi-linear.md) | $f(x) + y$ 或 $x + f(y)$ | `QuasiLinear` |
| [Stone-Geary](stone-geary.md) | $(x-\bar{x})^\alpha(y-\bar{y})^\beta$ | `StoneGeary` |

## 高级模型

| 模型 | 说明 | 类 |
|-------|-------------|-------|
| [自定义效用函数](advanced.md#custom-utility) | 包装任何向量化的可调用函数 | `CustomUtility` |
| [多商品 Cobb-Douglas](advanced.md#multi-good-cobb-douglas) | N 种商品，投影到 2 维 | `MultiGoodCD` |

## 共同接口

每个模型都提供：

```python
model(x, y)            # evaluate U(x, y) — accepts scalars or NumPy arrays
model.utility_type     # UtilityType.SMOOTH | KINKED | LINEAR
model.ray_slopes()     # list of expansion-path slopes
model.kink_points(lvls)# kink coordinates for Leontief-type preferences
```
