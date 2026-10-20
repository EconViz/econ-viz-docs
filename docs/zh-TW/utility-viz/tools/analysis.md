---
seo_title: "分析"
---

# 分析

<span id="sec-analysis"></span>

分析 API 提供 Marshall 需求的比較靜態、Slutsky 矩陣，以及效用函數的齊次性與位似性檢查。

## 比較靜態

<!-- api: agora.utility_viz.tools_analysis_1 -->

以有限差分估計兩商品 Marshall 需求對 $p_x$、$p_y$ 與所得的六個偏導數，回傳 `ComparativeStatics`。

- 在 `solve(...)` 的結果附近使用中央有限差分，預設的相對步長是 `1e-3`。
- 偵測到自身價格導數為正或所得導數為負時會發出警告，分別對應季芬財與劣等財的需求特性。

```python
from utility_viz import comparative_statics
from utility_viz.models import CobbDouglas

model = CobbDouglas(alpha=0.4, beta=0.6)
cs = comparative_statics(model, px=2.0, py=3.0, income=60.0)

print(
    round(cs.dx_dpx, 1), round(cs.dx_dpy, 1), round(cs.dx_dI, 1)
)
print(
    round(cs.dy_dpx, 1), round(cs.dy_dpy, 1), round(cs.dy_dI, 1)
)

# -6.0 0.0 0.2
# 0.0 -4.0 0.2
```

## Slutsky 矩陣

<!-- api: agora.utility_viz.tools_analysis_2 -->

以 Marshall 需求導數與所得效果計算兩商品的 Slutsky 替代矩陣，並檢查對稱性、負半定性與齊次性；檢查未通過時發出警告。使用 `as_array()` 可轉為 `NumPy` 陣列。

```python
from utility_viz import slutsky_matrix
from utility_viz.models import CobbDouglas

S = slutsky_matrix(
    CobbDouglas(alpha=0.4, beta=0.6),
    px=2.0,
    py=3.0,
    income=60.0,
)

print(round(S.s_xx, 1), round(S.s_xy, 1))
print(round(S.s_yx, 1), round(S.s_yy, 1))
print(S.as_array().round(1))

# -3.6 2.4
# 2.4 -1.6
# [[-3.6  2.4]
#  [ 2.4 -1.6]]
```

## 齊次性

<!-- api: agora.utility_viz.tools_analysis_3 -->

檢查效用函數的齊次性、位似性與需求的零次齊次性。

```python
from utility_viz.models import CobbDouglas, HomogeneityAnalyzer

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

## 規模報酬

<span id="sec-rts"></span>

`degree()` 回傳 `HomogeneityResult`，包含下列欄位：

Cobb-Douglas 的齊次次數為 $\alpha + \beta$：

$$
u(\lambda x, \lambda y) = \lambda^{\alpha + \beta} u(x, y).
$$

<!-- api: agora.utility_viz.tools_analysis_4 -->

函數的規模報酬分類。

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
    degree = (
        None
        if result.degree is None
        else round(result.degree, 1)
    )
    print(degree, result.returns_to_scale.name)

# 1.3 INCREASING
# 1.0 CONSTANT
# 0.7 DECREASING
# None NOT_HOMOGENEOUS
```
