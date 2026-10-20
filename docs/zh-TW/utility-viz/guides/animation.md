---
seo_title: "動畫"
---

# 動畫

<span id="sec-animation"></span>

`Animator` 依指定的參數序列呼叫繪圖函數，將回傳的 `Canvas` 或 `Figure` 匯出為 GIF。使用前需安裝 `animation` 選用依賴（詳見[選用依賴](../getting-started/installation.md#sec-extras)）。從 `utility_viz.core.animation` 匯入；1.x 為 `econ_viz.animation`。

<!-- api: agora.utility_viz.guides_animation_1 -->

依序將 `frames` 的值傳入 `draw`，每次回傳的圖形對應一個影格。

- `save()` 使用 `Pillow`，不需要 `ffmpeg`。
- 匯出前將影格合成至白色背景，避免殘影。
- `fps`、`dpi` 與 `loop` 分別設定影格率、解析度與循環次數。

```python
import numpy as np

from utility_viz import Canvas, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas


def draw(px: float) -> Canvas:
    model = CobbDouglas(alpha=0.5, beta=0.5)
    eq = solve(model, px=px, py=2.0, income=20.0)
    lvls = levels.around(eq.utility, n=5)

    return (
        Canvas(
            x_max=14,
            y_max=12,
            x_label="X_1",
            y_label="X_2",
            title="Price sweep",
        )
        .add_utility(model, levels=lvls)
        .add_budget(px=px, py=2.0, income=20.0, fill=True)
        .add_equilibrium(eq, show_ray=True, drop_dashes=True)
    )


Animator(draw, frames=np.linspace(1.0, 6.0, 45)).save(
    "price_sweep.gif",
    fps=12,
    dpi=120,
)
```

`examples/scripts/animation.py` 提供四種範例 (各範例均包含 Cobb-Douglas、CES、完全替代與完全互補模型。)：

- 參數變動：固定價格與所得，調整效用函數參數。
- 價格變動：固定效用函數與 $p_y$，調整 $p_x$，呈現預算線旋轉，寫法見上例。
- 所得變動：固定效用函數與價格，調整所得，呈現預算線平移。
- 預算線變動：僅顯示預算線，省略效用圖層。

四種範例的差異只在於 `draw()` 每次固定哪些值、調整哪個值。以參數變動為例，將上例的 `draw()` 改為接收 `alpha`，價格固定為 $p_x = 2$：

```python
def draw(alpha: float) -> Canvas:
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    eq = solve(model, px=2.0, py=2.0, income=20.0)
    ...


Animator(draw, frames=np.linspace(0.1, 0.9, 45)).save(
    "parameter_sweep.gif"
)
```

所得變動將 `draw()` 的引數改為 `income`，並把該值傳入 `add_budget()` 與 `solve()`。只呈現預算線時，省略 `add_utility()` 與 `add_equilibrium()`。

[參數變動](animation.md#fig-sweep-param)至[所得變動](animation.md#fig-sweep-income)各節錄四個影格。

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

# 圖形設定
Config.load("manual.toml").use()


def draw(alpha: float) -> Canvas:
    """一格影格：x 的權重是 alpha，y 的權重是 1 - alpha。"""
    model = CobbDouglas(alpha=alpha, beta=1.0 - alpha)
    eq = solve(model, px=2.0, py=2.0, income=20.0)
    cvs = Canvas(
        x_max=14, y_max=12, x_label="$x_1$", y_label="$x_2$"
    )
    cvs.add_utility(
        model, levels=levels.around(eq.utility, n=5)
    )
    cvs.add_budget(2.0, 2.0, 20.0, fill=True)
    cvs.add_equilibrium(eq, show_ray=True)
    return cvs


Animator(draw, frames=np.linspace(0.1, 0.9, 45)).save(
    "parameter_sweep.gif", fps=12, dpi=120
)
```

<span id="fig-sweep-param"></span>

<figure class="ev-fig" markdown>

![參數變動](../../../assets/utility-viz/agora/animation/parameter_sweep.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/animation/parameter_sweep.zh-TW.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>參數變動</figcaption>

</figure>

下面每張圖取 GIF 的四個影格，GIF 共 45 格。

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

# 圖形設定
Config.load("manual.toml").use()

model = CobbDouglas(alpha=0.5, beta=0.5)
# 每格用同一組曲線
fixed = levels.around(
    solve(model, px=2.0, py=2.0, income=20.0).utility, n=5
)


def draw(px: float) -> Canvas:
    """一格影格：x 的價格是 px。"""
    eq = solve(model, px=px, py=2.0, income=20.0)
    cvs = Canvas(
        x_max=14, y_max=12, x_label="$x_1$", y_label="$x_2$"
    )
    cvs.add_utility(model, levels=fixed)
    cvs.add_budget(px, 2.0, 20.0, fill=True)
    cvs.add_equilibrium(eq, show_ray=True)
    return cvs


Animator(draw, frames=np.linspace(1.0, 6.0, 45)).save(
    "price_sweep.gif", fps=12, dpi=120
)
```

<span id="fig-sweep-price"></span>

<figure class="ev-fig" markdown>

![價格變動](../../../assets/utility-viz/agora/animation/price_sweep.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/animation/price_sweep.zh-TW.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>價格變動</figcaption>

</figure>

```python
import numpy as np

from utility_viz import Canvas, Config, levels, solve
from utility_viz.core.animation import Animator
from utility_viz.models import CobbDouglas

# 圖形設定
Config.load("manual.toml").use()

model = CobbDouglas(alpha=0.5, beta=0.5)
# 每格用同一組曲線
fixed = levels.around(
    solve(model, px=2.0, py=2.0, income=20.0).utility, n=5
)


def draw(income: float) -> Canvas:
    """一格影格：所得是 income。"""
    eq = solve(model, px=2.0, py=2.0, income=income)
    cvs = Canvas(
        x_max=14, y_max=12, x_label="$x_1$", y_label="$x_2$"
    )
    cvs.add_utility(model, levels=fixed)
    cvs.add_budget(2.0, 2.0, income, fill=True)
    cvs.add_equilibrium(eq, show_ray=True)
    return cvs


Animator(draw, frames=np.linspace(8.0, 36.0, 45)).save(
    "income_sweep.gif", fps=12, dpi=120
)
```

<span id="fig-sweep-income"></span>

<figure class="ev-fig" markdown>

![所得變動](../../../assets/utility-viz/agora/animation/income_sweep.svg){ .ev-figure-lg }

<div class="ev-downloads"><a class="ev-download" href="../../../assets/utility-viz/agora/animation/income_sweep.zh-TW.py" download aria-label="下載生圖原始檔"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11m0 0-4.5-4.5M12 15l4.5-4.5M5 20h14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg><span>下載生圖原始檔</span></a></div>

<figcaption markdown>所得變動</figcaption>

</figure>

## 動畫圖庫

以下 GIF 由文件儲存庫的 `scripts/animation_figures.py` 依 `manual.toml` 的設定畫成，涵蓋同樣四種動畫：參數、價格、所得與只有預算線。

### 參數變動

改變效用函數的參數，觀察偏好圖的形狀如何隨之改變。

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../../../assets/animation/parameter_sweeps/cobb_douglas_parameter_sweep.gif" alt="Cobb-Douglas 參數變動 GIF">
    <figcaption>改變 \(\alpha\)，並令 \(\beta = 1 - \alpha\)</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../../../assets/animation/parameter_sweeps/ces_parameter_sweep.gif" alt="CES 參數變動 GIF">
    <figcaption>改變 \(\rho\)，調整曲率與替代程度</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全替代</span>
    <img src="../../../../assets/animation/parameter_sweeps/perfect_substitutes_parameter_sweep.gif" alt="完全替代參數變動 GIF">
    <figcaption>固定 \(b\)，改變 \(a\)</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全互補</span>
    <img src="../../../../assets/animation/parameter_sweeps/leontief_parameter_sweep.gif" alt="完全互補參數變動 GIF">
    <figcaption>固定 \(b\)，改變 \(a\)，讓拗折點的路徑移動</figcaption>
  </figure>
      </td>
    </tr>
  </tbody>
</table>

### 價格變動

固定效用函數與背景無異曲線的效用水準，只改變一項商品的價格，呈現預算線旋轉時的均衡路徑。

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../../../assets/animation/price_sweeps/cobb_douglas_price_sweep.gif" alt="Cobb-Douglas 價格變動 GIF">
    <figcaption>價格變動，\(p_y\) 固定</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../../../assets/animation/price_sweeps/ces_price_sweep.gif" alt="CES 價格變動 GIF">
    <figcaption>價格變動，效用曲面固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全替代</span>
    <img src="../../../../assets/animation/price_sweeps/perfect_substitutes_price_sweep.gif" alt="完全替代價格變動 GIF">
    <figcaption>預算線旋轉</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全互補</span>
    <img src="../../../../assets/animation/price_sweeps/leontief_price_sweep.gif" alt="完全互補價格變動 GIF">
    <figcaption>價格變動，直角無異曲線固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">只有預算線</span>
    <img src="../../../../assets/animation/price_sweeps/budget_only_price_sweep.gif" alt="只有預算線的價格變動 GIF">
    <figcaption>價格變動，單獨呈現限制式的旋轉</figcaption>
  </figure>
      </td>
      <td class="gif-table__empty" aria-hidden="true"></td>
    </tr>
  </tbody>
</table>

### 所得變動

固定效用函數與價格，只改變所得，呈現預算線平行移動時的均衡路徑。

<table class="gif-table">
  <tbody>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">Cobb-Douglas</span>
    <img src="../../../../assets/animation/income_sweeps/cobb_douglas_income_sweep.gif" alt="Cobb-Douglas 所得變動 GIF">
    <figcaption>所得變動，價格固定</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">CES</span>
    <img src="../../../../assets/animation/income_sweeps/ces_income_sweep.gif" alt="CES 所得變動 GIF">
    <figcaption>所得變動，價格與效用函數固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全替代</span>
    <img src="../../../../assets/animation/income_sweeps/perfect_substitutes_income_sweep.gif" alt="完全替代所得變動 GIF">
    <figcaption>所得變動</figcaption>
  </figure>
      </td>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">完全互補</span>
    <img src="../../../../assets/animation/income_sweeps/leontief_income_sweep.gif" alt="完全互補所得變動 GIF">
    <figcaption>所得變動，價格固定</figcaption>
  </figure>
      </td>
    </tr>
    <tr>
      <td>
  <figure class="gif-card">
    <span class="gif-card__title">只有預算線</span>
    <img src="../../../../assets/animation/income_sweeps/budget_only_income_sweep.gif" alt="只有預算線的所得變動 GIF">
    <figcaption>所得變動，單獨呈現限制式的平行移動</figcaption>
  </figure>
      </td>
      <td class="gif-table__empty" aria-hidden="true"></td>
    </tr>
  </tbody>
</table>
