---
seo_title: "比較靜態與 Slutsky 分析"
description: "用 econ-viz 的分析工具，以數值方法計算比較靜態、 Marshall 需求的導數與 Slutsky 分解。"
---

# 分析

`econ-viz` 除了繪圖與求解均衡，也提供分析工具。

![分析工具很適合搭配需求教學圖](../assets/consumer/demand_cobb_douglas.png)

## 比較靜態

用 `comparative_statics(...)` 以數值方法估計 Marshall 需求的六個導數：

```python
from econ_viz.models import CobbDouglas
from econ_viz.optimizer import comparative_statics

model = CobbDouglas(alpha=0.4, beta=0.6)
cs = comparative_statics(model, px=2.0, py=3.0, income=60.0)

print(cs.dx_dpx, cs.dx_dpy, cs.dx_dI)
print(cs.dy_dpx, cs.dy_dpy, cs.dy_dI)
```

回傳的物件：

```python
ComparativeStatics(
    dx_dpx=...,
    dx_dpy=...,
    dx_dI=...,
    dy_dpx=...,
    dy_dpy=...,
    dy_dI=...,
)
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

S = slutsky_matrix(CobbDouglas(alpha=0.4, beta=0.6), px=2.0, py=3.0, income=60.0)

print(S.s_xx, S.s_xy)
print(S.s_yx, S.s_yy)
print(S.as_array())
```

回傳的物件：

```python
SlutskyMatrix(
    s_xx=...,
    s_xy=...,
    s_yx=...,
    s_yy=...,
)
```

需要的是**補償性價格效果**，而不只是原始的 Marshall 導數時，就用這個工具。

## 齊次性分析

用 `HomogeneityAnalyzer` 檢查效用函數是否為齊次或位似。

```python
from econ_viz.analysis import HomogeneityAnalyzer
from econ_viz.models import CobbDouglas

analyzer = HomogeneityAnalyzer(CobbDouglas(alpha=0.4, beta=0.6))

result = analyzer.degree()
print(result.degree)
print(result.returns_to_scale)
print(analyzer.euler_check(3.0, 4.0))
print(analyzer.is_homothetic())
print(analyzer.demand_degree_zero(px=2.0, py=3.0, income=60.0))
```

### 可用的檢查

- `degree()` 估計齊次的次數
- `euler_check(x, y)` 計算某個消費組合上的 Euler 定理殘差
- `is_homothetic()` 檢查邊際替代率（MRS）在等比例縮放下是否不變
- `demand_degree_zero(px, py, income)` 驗證 Marshall 需求是否為**零次齊次**

## 規模報酬分類

`degree()` 會回傳 `HomogeneityResult`，其中包含估計的次數，以及 `ReturnsToScale` 分類：

- `INCREASING`（規模報酬遞增）
- `CONSTANT`（規模報酬固定）
- `DECREASING`（規模報酬遞減）
- `NOT_HOMOGENEOUS`（非齊次）
