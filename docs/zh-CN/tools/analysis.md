---
seo_title: "比较静态与 Slutsky 分析"
description: "用 econ-viz 的分析工具，以数值方法计算比较静态、马歇尔需求的导数与 Slutsky 分解。"
---

# 分析

`econ-viz` 除了绘图与求解均衡，也提供分析工具。

## 比较静态

用 `comparative_statics(...)` 以数值方法估计马歇尔需求的六个导数：

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

说明：

- 在 `solve(...)` 的结果附近使用**中央有限差分**
- 缺省的相对步长是 `1e-3`
- 遇到经济上不寻常的符号时会发出警告，例如**Giffen 财**式的自身价格反应，或**劣等财**的收入效应

## Slutsky 矩阵

用 `slutsky_matrix(...)` 计算 Slutsky 方程序所隐含的两商品替代矩阵。

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

需要的是**补偿价格效应**，而不只是原始的马歇尔导数时，就用这个工具。

## 齐次性分析

用 `HomogeneityAnalyzer` 检查效用函数是否为齐次或位似。

### 可用的检查

分析器提供以下四项检查：

- `degree()` 估计齐次的次数
- `euler_check(x, y)` 计算某个消费束上的 Euler 定理残差
- `is_homothetic()` 检查边际替代率（MRS）在等比例缩放下是否不变
- `demand_degree_zero(px, py, income)` 验证马歇尔需求是否为**零次齐次**

### 代码示例

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

## 规模报酬分类

`degree()` 会返回 `HomogeneityResult`，其中包含估计的次数，以及 `ReturnsToScale` 分类：

Cobb–Douglas 效用函数的齐次次数是 $\alpha+\beta$：

$$
U(\lambda x, \lambda y)
= \lambda^{\alpha+\beta} U(x,y)
$$

- $\alpha+\beta>1$：`INCREASING`（规模报酬递增）
- $\alpha+\beta=1$：`CONSTANT`（规模报酬固定）
- $\alpha+\beta<1$：`DECREASING`（规模报酬递减）

无法得到一致齐次次数的函数会分类为 `NOT_HOMOGENEOUS`（非齐次）。

### 分类示例

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
