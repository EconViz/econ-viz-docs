---
seo_title: "效用函数模型"
description: "比较 econ-viz 支持的核心效用模型，包含公式、参数、Python 示例与无差异曲线图。"
---

# 核心模型

核心模型涵盖平滑偏好、折点与线性偏好，以及具有收入或参考点效应的偏好。
先选择模型分组，再用选项卡切换并比较模型。

## 平滑偏好

这组模型会产生平滑的无差异曲线；价格与收入为正时，通常会得到内点解。

=== "Cobb-Douglas"

    Cobb-Douglas 是描述平滑、严格凸偏好的标准模型。

    $$
    U(x,y)=x^\alpha y^\beta
    $$

    指数决定两种商品在效用中的相对权重。无差异曲线会接近两轴，但不会接触两轴。

    **参数**

    | 参数 | 默认值 | 含义 |
    |------|--------|------|
    | `alpha` | `0.5` | 商品 $x$ 的权重 |
    | `beta` | `0.5` | 商品 $y$ 的权重 |

    **代码**

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import CobbDouglas

    model = CobbDouglas(alpha=0.5, beta=0.5)
    eq = solve(model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=20, y_max=15, title="Cobb-Douglas")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(2.0, 3.0, 30.0, fill=True)
        .add_equilibrium(eq, show_ray=True)
        .save("cobb_douglas.png")
    )
    ```

    ![Cobb-Douglas 无差异曲线图](../../assets/models/cobb_douglas.png)

=== "CES"

    CES 能在保持平滑偏好的同时，调整两种商品的替代难易度。

    $$
    U(x,y)=\left(\alpha x^\rho+\beta y^\rho\right)^{1/\rho}
    $$

    替代弹性是 $\sigma=1/(1-\rho)$。改变 $\rho$ 时，CES 会接近
    Cobb-Douglas、完全互补或完全替代。

    **参数**

    | 参数 | 默认值 | 含义 |
    |------|--------|------|
    | `alpha` | `0.5` | 商品 $x$ 的权重 |
    | `beta` | `0.5` | 商品 $y$ 的权重 |
    | `rho` | `0.5` | 替代参数，且 $\rho\ne1$ |

    **代码**

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import CES

    model = CES(alpha=0.5, beta=0.5, rho=-0.5)
    eq = solve(model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=20, y_max=15, title="CES")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(2.0, 3.0, 30.0)
        .add_equilibrium(eq)
        .save("ces.png")
    )
    ```

    ![CES 无差异曲线图](../../assets/models/ces.png)

=== "Translog"

    Translog 是描述平滑偏好的灵活对数二次模型。

    $$
    \begin{aligned}
    \ln U(x,y)={}&\alpha_0+\alpha_x\ln x+\alpha_y\ln y\\
    &+\tfrac12\beta_{xx}(\ln x)^2
    +\tfrac12\beta_{yy}(\ln y)^2
    +\beta_{xy}\ln x\ln y
    \end{aligned}
    $$

    二次项与交叉项让曲率能随消费束改变。所有 $\beta$ 系数都设为零时，
    会得到类似 Cobb-Douglas 的对数线性形式。

    **参数**

    | 参数 | 默认值 | 含义 |
    |------|--------|------|
    | `alpha_0` | `0.0` | 对数效用截距 |
    | `alpha_x` | `0.5` | $\ln x$ 的一次项权重 |
    | `alpha_y` | `0.5` | $\ln y$ 的一次项权重 |
    | `beta_xx` | `0.0` | $x$ 方向的曲率 |
    | `beta_yy` | `0.0` | $y$ 方向的曲率 |
    | `beta_xy` | `0.0` | $x$ 与 $y$ 的交叉效应 |

    **代码**

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import Translog

    model = Translog(alpha_x=0.6, alpha_y=0.4, beta_xy=0.12)
    eq = solve(model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=18, y_max=12, title="Translog")
        .add_utility(model, levels=levels.around(eq.utility, n=4))
        .add_budget(2.0, 3.0, 30.0)
        .add_equilibrium(eq)
        .save("translog.png")
    )
    ```

    ![Translog 无差异曲线图](../../assets/models/translog.png)

## 折点与角点

这组模型体现非光滑或线性偏好如何改变最优点的位置。

=== "完全互补"

    完全互补偏好描述以固定比例搭配消费的商品。

    $$
    U(x,y)=\min(ax,by)
    $$

    无差异曲线呈 L 型。最优点位于两个加权数量相等的折点。

    **参数**

    | 参数 | 默认值 | 含义 |
    |------|--------|------|
    | `a` | `1.0` | 商品 $x$ 的权重 |
    | `b` | `1.0` | 商品 $y$ 的权重 |

    **代码**

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import Leontief

    model = Leontief(a=1.0, b=1.0)
    eq = solve(model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=20, y_max=15, title="完全互补")
        .add_utility(
            model,
            levels=levels.around(eq.utility, n=5),
            show_rays=True,
            show_kinks=True,
        )
        .add_budget(2.0, 3.0, 30.0)
        .add_equilibrium(eq)
        .save("leontief.png")
    )
    ```

    ![完全互补无差异曲线图](../../assets/models/leontief.png)

=== "完全替代"

    完全替代偏好让两种商品之间的效用交换比例保持固定。

    $$
    U(x,y)=ax+by
    $$

    无差异曲线是直线。消费者通常只选择每元边际效用较高的商品，因此形成角点解。

    **参数**

    | 参数 | 默认值 | 含义 |
    |------|--------|------|
    | `a` | `1.0` | 商品 $x$ 的边际效用 |
    | `b` | `1.0` | 商品 $y$ 的边际效用 |

    **代码**

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import PerfectSubstitutes

    model = PerfectSubstitutes(a=1.0, b=2.0)
    eq = solve(model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=20, y_max=15, title="Perfect Substitutes")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(2.0, 3.0, 30.0)
        .add_equilibrium(eq)
        .save("perfect_substitutes.png")
    )
    ```

    ![完全替代无差异曲线图](../../assets/models/perfect_substitutes.png)

=== "最大值效用"

    最大值效用只取每个消费组合中较大的加权数量。

    $$
    U(x,y)=\max(ax,by)
    $$

    每条无差异曲线有两条朝坐标轴延伸的直角线段，因此偏好不是凸的。在
    线性预算约束下，最优选择通常落在加权效用较高的轴截距。

    **参数**

    | 参数 | 默认值 | 含义 |
    |------|--------|------|
    | `a` | `1.0` | 商品 $x$ 的权重 |
    | `b` | `1.0` | 商品 $y$ 的权重 |

    **代码**

    ```python
    import numpy as np
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import CustomUtility

    a, b = 1.0, 1.0
    model = CustomUtility(
        func=lambda x, y: np.maximum(a * x, b * y),
        name="maximum",
    )
    eq = solve(model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=25, y_max=20, title="最大值效用")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(2.0, 3.0, 30.0)
        .add_equilibrium(eq)
        .save("maximum.png")
    )
    ```

    ![最大值效用无差异曲线图](../../assets/models/maximum.png)

## 收入与参考点

这组模型加入特殊收入效应、最低消费量或偏好的消费参考点。

=== "拟线性"

    拟线性偏好让其中一种商品以线性方式进入效用。

    $$
    U(x,y)=f(x)+y
    $$

    得到内点解后，非线性商品没有收入效应。`linear_in` 可以对调 $x$ 与 $y$
    的角色。

    **参数**

    | 参数 | 默认值 | 含义 |
    |------|--------|------|
    | `v_func` | `numpy.log` | 递增且凹的函数 $f$ |
    | `linear_in` | `"y"` | 线性进入的商品 |

    **代码**

    ```python
    import numpy as np
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import QuasiLinear

    model = QuasiLinear(v_func=np.log, linear_in="y")
    eq = solve(model, px=2.0, py=1.0, income=20.0)

    (
        Canvas(x_max=15, y_max=15, title="Quasi-Linear")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(2.0, 1.0, 20.0)
        .add_equilibrium(eq)
        .save("quasi_linear.png")
    )
    ```

    ![拟线性无差异曲线图](../../assets/models/quasi_linear.png)

=== "Stone-Geary"

    Stone-Geary 在 Cobb-Douglas 中加入最低消费需求。

    $$
    U(x,y)=(x-\bar{x})^\alpha(y-\bar{y})^\beta
    $$

    消费者先满足最低消费量 $\bar{x}$ 与 $\bar{y}$，再像 Cobb-Douglas 消费者
    一样分配剩余收入。

    **参数**

    | 参数 | 默认值 | 含义 |
    |------|--------|------|
    | `alpha` | `0.5` | 超额 $x$ 的权重 |
    | `beta` | `0.5` | 超额 $y$ 的权重 |
    | `bar_x` | `1.0` | 最低消费量 $\bar{x}$ |
    | `bar_y` | `1.0` | 最低消费量 $\bar{y}$ |

    **代码**

    ```python
    from econ_viz import Canvas, levels, solve
    from econ_viz.models import StoneGeary

    model = StoneGeary(alpha=0.5, beta=0.5, bar_x=2.0, bar_y=2.0)
    eq = solve(model, px=2.0, py=3.0, income=30.0)

    (
        Canvas(x_max=20, y_max=15, title="Stone-Geary")
        .add_utility(model, levels=levels.around(eq.utility, n=5))
        .add_budget(2.0, 3.0, 30.0, fill=True)
        .add_equilibrium(eq)
        .save("stone_geary.png")
    )
    ```

    ![Stone-Geary 无差异曲线图](../../assets/models/stone_geary.png)

=== "饱和"

    饱和偏好有一个使效用达到最高的极乐点。

    $$
    U(x,y)=-a(x-x^*)^2-b(y-y^*)^2
    $$

    离开 $(x^*,y^*)$ 后，效用往任何方向都会下降，因此无差异曲线是封闭椭圆，
    且偏好不具单调性。

    **参数**

    | 参数 | 默认值 | 含义 |
    |------|--------|------|
    | `bliss_x` | `5.0` | 极乐点坐标 $x^*$ |
    | `bliss_y` | `5.0` | 极乐点坐标 $y^*$ |
    | `a` | `1.0` | $x$ 轴方向的曲率 |
    | `b` | `1.0` | $y$ 轴方向的曲率 |

    **代码**

    ```python
    import numpy as np
    from econ_viz import Canvas, levels
    from econ_viz.models import Satiation

    model = Satiation(bliss_x=6.0, bliss_y=4.0)
    x = np.linspace(0.1, 12.0, 300)
    y = np.linspace(0.1, 10.0, 300)
    X, Y = np.meshgrid(x, y)

    (
        Canvas(x_max=12, y_max=10, title="Satiation")
        .add_utility(model, levels=levels.percentile(model(X, Y), n=5))
        .save("satiation.png")
    )
    ```

    ![饱和无差异曲线图](../../assets/models/satiation.png)

自定义函数与多商品 Cobb-Douglas 模型请参阅[高级模型](advanced.md)。
