---
seo_title: "比較靜態與 Slutsky 分析"
description: "用 econ-viz 的分析工具，以數值方法計算比較靜態、 Marshall 需求的導數與 Slutsky 分解。"
---

# 分析

`econ-viz` 除了繪圖與求解均衡，也提供分析工具。

## 比較靜態

用 `comparative_statics(...)` 以數值方法估計 Marshall 需求的六個導數：

```python
from econ_viz.models import CobbDouglas
from econ_viz.optimizer import comparative_statics

model = CobbDouglas(alpha=0.4, beta=0.6)
cs = comparative_statics(model, px=2.0, py=3.0, income=60.0)

print(round(cs.dx_dpx, 1), round(cs.dx_dpy, 1), round(cs.dx_dI, 1))
print(round(cs.dy_dpx, 1), round(cs.dy_dpy, 1), round(cs.dy_dI, 1))

# -6.0 0.0 0.2
# 0.0 -4.0 0.2
```

說明：

- 在 `solve(...)` 的結果附近使用**中央有限差分**
- 預設的相對步長是 `1e-3`
- 遇到經濟上不尋常的符號時會發出警告，例如**Giffen 財**式的自身價格反應，或**劣等財**的所得效果

## Slutsky 矩陣

用 `slutsky_matrix(...)` 計算 Slutsky 方程式所隱含的兩商品替代矩陣。

```python
from econ_viz import slutsky_matrix
from econ_viz.models import CobbDouglas

S = slutsky_matrix(
    CobbDouglas(alpha=0.4, beta=0.6),
    px=2.0, py=3.0, income=60.0,
)

print(round(S.s_xx, 1), round(S.s_xy, 1))
print(round(S.s_yx, 1), round(S.s_yy, 1))
print(S.as_array().round(1))

# -3.6 2.4
# 2.4 -1.6
# [[-3.6  2.4]
#  [ 2.4 -1.6]]
```

需要的是**補償性價格效果**，而不只是原始的 Marshall 導數時，就用這個工具。

## 齊次性分析

用 `HomogeneityAnalyzer` 檢查效用函數是否為齊次或位似。

### 可用的檢查

分析器提供以下四項檢查：

- `degree()` 估計齊次的次數
- `euler_check(x, y)` 計算某個消費組合上的 Euler 定理殘差
- `is_homothetic()` 檢查邊際替代率（MRS）在等比例縮放下是否不變
- `demand_degree_zero(px, py, income)` 驗證 Marshall 需求是否為**零次齊次**

### 程式碼範例

```python
from econ_viz.analysis import HomogeneityAnalyzer
from econ_viz.models import CobbDouglas

analyzer = HomogeneityAnalyzer(CobbDouglas(alpha=0.4, beta=0.6))
result = analyzer.degree()

print(round(result.degree, 6))
print(result.returns_to_scale)
print(round(analyzer.euler_check(3.0, 4.0), 6))
print(analyzer.is_homothetic())
print(analyzer.demand_degree_zero(px=2.0, py=3.0, income=60.0))

# 1.0
# ReturnsToScale.CONSTANT
# 0.0
# True
# True
```

## 規模報酬分類

`degree()` 會回傳 `HomogeneityResult`，其中包含估計的次數，以及 `ReturnsToScale` 分類：

Cobb–Douglas 效用函數的齊次次數是 $\alpha+\beta$：

$$
U(\lambda x, \lambda y)
= \lambda^{\alpha+\beta} U(x,y)
$$

- $\alpha+\beta>1$：`INCREASING`（規模報酬遞增）
- $\alpha+\beta=1$：`CONSTANT`（規模報酬固定）
- $\alpha+\beta<1$：`DECREASING`（規模報酬遞減）

無法得到一致齊次次數的函數會分類為 `NOT_HOMOGENEOUS`（非齊次）。

### 分類範例

```python
def shifted_utility(x, y):
    return x**0.4 * y**0.6 + 1.0


models = [
    CobbDouglas(alpha=0.7, beta=0.6),
    CobbDouglas(alpha=0.4, beta=0.6),
    CobbDouglas(alpha=0.2, beta=0.5),
    shifted_utility,
]

for model in models:
    result = HomogeneityAnalyzer(model).degree()
    degree = None if result.degree is None else round(result.degree, 1)
    print(degree, result.returns_to_scale.name)

# 1.3 INCREASING
# 1.0 CONSTANT
# 0.7 DECREASING
# None NOT_HOMOGENEOUS
```
