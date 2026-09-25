---
seo_title: "效用函數模型"
description: "econ-viz 支援的效用函數一覽：Cobb-Douglas、Leontief、完全替代、CES、Translog、飽和、準線性與 Stone-Geary。"
---

# 模型目錄

所有模型都放在 `econ_viz.models`，並遵循 `UtilityFunction` 協定：它們都是**可呼叫的 dataclass**，能對 NumPy 陣列逐元素計算 `U(x, y)`。

![模型目錄總覽](../../assets/models/cobb_douglas.png)

## 參數化模型

| 模型 | 函數形式 | 類別 |
|-------|-----------|-------|
| [Cobb-Douglas](cobb-douglas.md) | $x^\alpha y^\beta$ | `CobbDouglas` |
| [Leontief](leontief.md) | $\min(ax, by)$ | `Leontief` |
| [完全替代](perfect-substitutes.md) | $ax + by$ | `PerfectSubstitutes` |
| [CES](ces.md) | $(\alpha x^\rho + \beta y^\rho)^{1/\rho}$ | `CES` |
| [Translog](translog.md) | 彈性的對數二次效用 | `Translog` |
| [飽和](satiation.md) | $-a(x-x^*)^2 - b(y-y^*)^2$ | `Satiation` |
| [準線性](quasi-linear.md) | $f(x) + y$ 或 $x + f(y)$ | `QuasiLinear` |
| [Stone-Geary](stone-geary.md) | $(x-\bar{x})^\alpha(y-\bar{y})^\beta$ | `StoneGeary` |

## 進階模型

| 模型 | 說明 | 類別 |
|-------|-------------|-------|
| [自訂效用函數](advanced.md#custom-utility) | 包裝任何向量化的可呼叫函數 | `CustomUtility` |
| [多商品 Cobb-Douglas](advanced.md#multi-good-cobb-douglas) | N 種商品，投影到 2 維 | `MultiGoodCD` |

## 共同介面

每個模型都提供：

```python
model(x, y)            # evaluate U(x, y) — accepts scalars or NumPy arrays
model.utility_type     # UtilityType.SMOOTH | KINKED | LINEAR
model.ray_slopes()     # list of expansion-path slopes
model.kink_points(lvls)# kink coordinates for Leontief-type preferences
```
