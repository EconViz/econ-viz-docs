---
seo_title: "比较静态与 Slutsky 分析"
description: "用 econ-viz 的分析工具，以数值方法计算比较静态、马歇尔需求的导数与 Slutsky 分解。"
---

# 分析

`econ-viz` 除了绘图与求解均衡，也提供分析工具。

![分析工具很适合搭配需求教学图](../assets/consumer/demand_cobb_douglas.png)

## 比较静态

用 `comparative_statics(...)` 以数值方法估计马歇尔需求的六个导数：

```python
from econ_viz.models import CobbDouglas
from econ_viz.optimizer import comparative_statics

model = CobbDouglas(alpha=0.4, beta=0.6)
cs = comparative_statics(model, px=2.0, py=3.0, income=60.0)

print(cs.dx_dpx, cs.dx_dpy, cs.dx_dI)
print(cs.dy_dpx, cs.dy_dpy, cs.dy_dI)
```

返回的对象：

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

说明：

- 在 `solve(...)` 的结果附近使用**中央有限差分**
- 缺省的相对步长是 `1e-3`
- 遇到经济上不寻常的符号时会发出警告，例如**Giffen 财**式的自身价格反应，或**劣等财**的收入效应

## Slutsky 矩阵

用 `slutsky_matrix(...)` 计算 Slutsky 方程序所隐含的两商品替代矩阵。

```python
from econ_viz import slutsky_matrix
from econ_viz.models import CobbDouglas

S = slutsky_matrix(CobbDouglas(alpha=0.4, beta=0.6), px=2.0, py=3.0, income=60.0)

print(S.s_xx, S.s_xy)
print(S.s_yx, S.s_yy)
print(S.as_array())
```

返回的对象：

```python
SlutskyMatrix(
    s_xx=...,
    s_xy=...,
    s_yx=...,
    s_yy=...,
)
```

需要的是**补偿价格效应**，而不只是原始的马歇尔导数时，就用这个工具。

## 齐次性分析

用 `HomogeneityAnalyzer` 检查效用函数是否为齐次或位似。

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

### 可用的检查

- `degree()` 估计齐次的次数
- `euler_check(x, y)` 计算某个消费束上的 Euler 定理残差
- `is_homothetic()` 检查边际替代率（MRS）在等比例缩放下是否不变
- `demand_degree_zero(px, py, income)` 验证马歇尔需求是否为**零次齐次**

## 规模报酬分类

`degree()` 会返回 `HomogeneityResult`，其中包含估计的次数，以及 `ReturnsToScale` 分类：

- `INCREASING`（规模报酬递增）
- `CONSTANT`（规模报酬固定）
- `DECREASING`（规模报酬递减）
- `NOT_HOMOGENEOUS`（非齐次）
