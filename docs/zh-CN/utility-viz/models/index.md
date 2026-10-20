---
seo_title: "核心模型"
---

# 核心模型

<span id="sec-models"></span>

内置模型位于 `utility_viz.models`，可传入 `solve()` 与 `Canvas.add_utility()`。本章按偏好特性分组，列出各模型的效用函数、参数、特有行为与图形。

## 平滑偏好

Cobb-Douglas、CES 与 Translog 的无差异曲线为平滑曲线；最优解取决于模型参数、价格与收入。

### Cobb-Douglas

<!-- api: agora.utility_viz.models_index_1 -->

Cobb-Douglas 效用函数 [Cobb (1928)](../project/references.md#cobb1928)：

$$
u(x, y) = x^\alpha y^\beta
$$

正指数决定两种商品的相对权重，无差异曲线以坐标轴为渐近线。

### CES

<!-- api: agora.utility_viz.models_index_2 -->

CES [Arrow (1961)](../project/references.md#arrow1961) 通过 `rho` 调整商品间的替代弹性：

$$
u(x, y) = (\alpha x^\rho + \beta y^\rho)^{1 / \rho}.
$$

替代弹性为 $\sigma = 1 / (1 - \rho)$。极限形式分别为 Cobb-Douglas（$\rho \to 0$）、完全互补（$\rho \to -infinity$）与完全替代（$\rho \to 1$）。

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import CES

Config.load("manual.toml").use()  # 图形设置

model = CES(alpha=0.5, beta=0.5, rho=-0.5)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("ces.png")
```

<figure class="ev-fig" markdown>

![CES 曲线](../../../assets/utility-viz/agora/models/ces.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/ces.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>CES 曲线</figcaption>

</figure>

### Translog

<!-- api: agora.utility_viz.models_index_3 -->

Translog [Christensen (1975)](../project/references.md#christensen1975) 以对数的一次项、二次项与交叉项表示效用：

$$
\begin{aligned}ln u(x, y) = & \alpha_0 + \alpha_x ln x + \alpha_y ln y \\ & + 1/2 \beta_{x x} (ln x)^2 + 1/2 \beta_{y y} (ln y)^2 + \beta_{x y} ln x ln y.\end{aligned}
$$

二次项与交叉项控制曲率。所有 $\beta$ 系数为零时，退化为 Cobb-Douglas 型的对数线性形式。

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import Translog

Config.load("manual.toml").use()  # 图形设置

model = Translog(alpha_x=0.6, alpha_y=0.4, beta_xy=0.12)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=18, y_max=12, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=4))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("translog.png")
```

<figure class="ev-fig" markdown>

![Translog 示例](../../../assets/utility-viz/agora/models/translog.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/translog.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>Translog 示例</figcaption>

</figure>

## 折点与角解

无差异曲线有折点或为直线时，最优解可能位于折点或坐标轴，不能仅以相切条件判定。

### 完全互补

<!-- api: agora.utility_viz.models_index_4 -->

完全互补效用函数：

$$
u(x, y) = \min\lbrace a x, b y\rbrace
$$

无差异曲线呈 L 型。权重与价格为正时，最优点满足固定比例 $a x = b y$。

转角在图片与 TikZ 输出中都画成精确的直角；以 `CustomUtility` 创建的分段 `min`/`max` 函数亦同。

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import Leontief

Config.load("manual.toml").use()  # 图形设置

model = Leontief(a=1.0, b=1.0)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(
    model,
    levels=levels.around(eq.utility, n=5),
    show_rays=True,
    show_kinks=True,  # 每个折点画射线与标记
)
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("leontief.png")
```

<figure class="ev-fig" markdown>

![完全互补射线](../../../assets/utility-viz/agora/models/leontief.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/leontief.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>完全互补射线</figcaption>

</figure>

### 完全替代

<!-- api: agora.utility_viz.models_index_5 -->

完全替代效用函数：

$$
u(x, y) = a x + b y.
$$

无差异曲线为直线。每元边际效用不同时，最优解为仅购买较高者的角解；两者相等时，预算线上的消费组合皆为最优解。

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import PerfectSubstitutes

Config.load("manual.toml").use()  # 图形设置

model = PerfectSubstitutes(a=1.0, b=2.0)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("perfect_substitutes.png")
```

<figure class="ev-fig" markdown>

![完全替代角解](../../../assets/utility-viz/agora/models/perfect_substitutes.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/perfect_substitutes.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>完全替代角解</figcaption>

</figure>

### 最大值效用

<!-- api: agora.utility_viz.models_index_6 -->

以两个加权数量的最大值定义效用：

$$
u(x, y) = \max\lbrace a x, b y\rbrace
$$

此偏好不具凸性。在正权重与正价格下，最优解位于效用更高的预算线轴截距。此模型以 `CustomUtility` 创建（详见[进阶模型](advanced.md#sec-advanced)）。

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import CustomUtility

Config.load("manual.toml").use()  # 图形设置

model = CustomUtility(func=lambda x, y: np.maximum(x, y), name="maximum")
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=25, y_max=20, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0)
cvs.add_equilibrium(eq)
cvs.save("maximum.png")
```

<figure class="ev-fig" markdown>

![最大值效用](../../../assets/utility-viz/agora/models/maximum.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/maximum.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>最大值效用</figcaption>

</figure>

## 收入与参考点

以下模型分别描述准线性偏好、最低消费需求与具有饱和点的饱和偏好。

### 准线性

<!-- api: agora.utility_viz.models_index_7 -->

准线性效用中，一种商品以线性项表示：

$$
u(x, y) = f(x) + y.
$$

在内部解范围内，非线性商品的需求不受收入影响。`linear_in` 指定线性项对应的商品。

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import QuasiLinear

Config.load("manual.toml").use()  # 图形设置

model = QuasiLinear(v_func=np.log, linear_in="y")
eq = solve(model, px=1.0, py=2.0, income=20.0)

cvs = Canvas(x_max=15, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(1.0, 2.0, 20.0)
cvs.add_equilibrium(eq)
cvs.save("quasi_linear.png")
```

<figure class="ev-fig" markdown>

![准线性偏好](../../../assets/utility-viz/agora/models/quasi_linear.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/quasi_linear.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>准线性偏好</figcaption>

</figure>

### Haagsma

<!-- api: agora.utility_viz.models_index_8 -->

[Haagsma (2012)](../project/references.md#haagsma2012) 效用函数为

$$
u(x, y) = \alpha_x ln(x - \gamma_x) - \alpha_y ln(\gamma_y - y).
$$

定义域为 $x > \gamma_x$ 且 $0 \le y < \gamma_y$，并要求 $0 < \alpha_x < \alpha_y$。商品 $x$ 的 Marshall 需求随收入下降；当 $\gamma_y p_y < I < \gamma_y p_y + \gamma_x p_x$ 时，商品 $x$ 为季芬财。

收入达到 $\gamma_y p_y + \gamma_x p_x$ 时，效用在预算线上没有有限最大值，模型会抛出 `InvalidParameterError`。

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import Haagsma

Config.load("manual.toml").use()  # 图形设置

model = Haagsma(gamma_y=10.0)
eq = solve(model, px=1.0, py=1.0, income=11.0)

cvs = Canvas(x_max=9, y_max=12, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=4))
cvs.add_budget(1.0, 1.0, 11.0)
cvs.add_equilibrium(eq)
cvs.save("haagsma.png")
```

<figure class="ev-fig" markdown>

![$\gamma_y = 10$ 的 Haagsma](../../../assets/utility-viz/agora/models/haagsma.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/haagsma.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>$\gamma_y = 10$ 的 Haagsma</figcaption>

</figure>

### Stone-Geary

<!-- api: agora.utility_viz.models_index_9 -->

Stone-Geary [Stone (1954)](../project/references.md#stone1954)[Geary (1950)](../project/references.md#geary1950) 在 Cobb-Douglas 中添加最低消费量：

$$
u(x, y) = (x - \overline{x})^\alpha (y - \overline{y})^\beta.
$$

满足基本需求量 $\overline{x}$ 与 $\overline{y}$ 后，剩余收入依权重分配。

```python
from utility_viz import Canvas, Config, levels, solve
from utility_viz.models import StoneGeary

Config.load("manual.toml").use()  # 图形设置

model = StoneGeary(alpha=0.5, beta=0.5, bar_x=2.0, bar_y=2.0)
eq = solve(model, px=2.0, py=3.0, income=30.0)

cvs = Canvas(x_max=20, y_max=15, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.around(eq.utility, n=5))
cvs.add_budget(2.0, 3.0, 30.0, fill=True)
cvs.add_equilibrium(eq)
cvs.save("stone_geary.png")
```

<figure class="ev-fig" markdown>

![Stone-Geary](../../../assets/utility-viz/agora/models/stone_geary.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/stone_geary.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>Stone-Geary</figcaption>

</figure>

### 饱和偏好

<!-- api: agora.utility_viz.models_index_10 -->

饱和偏好以 $(x^*, y^*)$ 为效用最高的饱和点：

$$
u(x, y) = -a (x - x^*)^2 - b (y - y^*)^2.
$$

当 $a, b > 0$，偏离饱和点会使效用下降，无差异曲线为封闭椭圆，偏好不具单调性。

```python
import numpy as np

from utility_viz import Canvas, Config, levels
from utility_viz.models import Satiation

Config.load("manual.toml").use()  # 图形设置

model = Satiation(bliss_x=6.0, bliss_y=4.0)

# 曲线取自效用值网格
X, Y = np.meshgrid(np.linspace(0.1, 12.0, 300), np.linspace(0.1, 10.0, 300))

cvs = Canvas(x_max=12, y_max=10, x_label="$x$", y_label="$y$")
cvs.add_utility(model, levels=levels.percentile(model(X, Y), n=5))  # u 的五个百分位数
cvs.save("satiation.png")
```

<figure class="ev-fig" markdown>

![饱和偏好](../../../assets/utility-viz/agora/models/satiation.svg){ .ev-figure-sm }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/models/satiation.zh-CN.py" download aria-label="下载生图源文件"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下载生图源文件</span></a></div>

<figcaption markdown>饱和偏好</figcaption>

</figure>
