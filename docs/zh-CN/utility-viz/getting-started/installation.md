---
seo_title: "安装"
---

# 安装

<span id="sec-install"></span>

## 系统需求

`utility-viz` 需要 Python 3.10 以上版本 (Python 官方网站提供各操作系统的安装程序：[https://www.python.org/downloads/](https://www.python.org/downloads/)。)。本章以 `uv` (`uv` 是 Astral 开发的 Python 软件包与项目管理工具，速度快且可一并管理 Python 版本；安装方式与完整说明见官方文档：[https://docs.astral.sh/uv/](https://docs.astral.sh/uv/)。) 管理软件包与项目，并附上对应的 `pip` 命令。

安装软件包时会一并安装 `NumPy`、`SciPy`、`matplotlib` 与 `SymPy`，分别用于数组运算、数值求解、绘图与符号运算，以及用于与后端无关的场景与 Bézier 曲线的 `mosaickit` 与 `bezierkit` (一般 Python 绘图不需要另外安装 LaTeX；只有要编译导出的 TikZ 源代码时，才需要 LaTeX 环境。)。

## 安装 `uv`

本手册的命令以 `uv` 为准。现有项目仍可使用 `pip`、`pipx` 或 `Poetry`；软件包 API 不受管理工具影响。

依操作系统运行下列安装命令。

### macOS、Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
### Windows

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 安装 `utility-viz`

创建项目并添加 `utility-viz`：

```bash
uv init my-diagrams
cd my-diagrams
uv add utility-viz
```

使用 `uv run` 在项目环境中运行程序：

```bash
uv run python main.py
```

将[快速开始](quickstart.md#sec-quickstart)的基本示例存为项目目录下的 `main.py`，再运行上述命令。`uv add` 记录项目依赖，`uv run` 使用该项目的 Python 环境。安装与运行必须使用同一个环境。

若要固定本手册使用的版本，可在添加依赖时指定版本号：

```bash
uv add "utility-viz==2.0.0b1"
```

2.0.0b1 是预览版。在没有 2.x 正式版之前，`uv add utility-viz` 与 `pip install utility-viz` 会直接安装此版本；正式版发布后，需以 `uv add --prerelease allow utility-viz` 或 `pip install --pre utility-viz` 才能安装预览版。

若使用现有的 Python 虚拟环境，可通过 `pip` 安装：

```bash
python -m pip install -U utility-viz
```

软件包名称是 `utility-viz`，Python 导入名称是 `utility_viz`：

```python
from utility_viz import Canvas, solve
```

`import` 语句不得使用连字符。若发生 `ModuleNotFoundError`，检查运行程序的解释器是否与安装软件包时使用的环境相同。

## 可选依赖

<span id="sec-extras"></span>

动画与 Jupyter 交互组件需要可选依赖。按用途安装其中一组：

<!-- api: agora.utility_viz.getting_started_installation_1 -->

```bash
uv add "utility-viz[animation]"    # GIF 导出（Pillow）
uv add "utility-viz[interactive]"  # 笔记本交互组件
uv add "utility-viz[all]"          # 全部可选依赖
```

安装可选依赖不会自动运行动画或打开笔记本，仍需按各章示例调用对应的 API。

## 安装命令行工具

<span id="sec-install-cli"></span>

仅使用命令行接口时，可将 `utility-viz` 安装为独立工具（详见[命令行工具](cli.md#sec-cli)）：

```bash
uv tool install utility-viz
```

此方式将命令行工具安装在独立环境。需要在 Python 程序中导入软件包时，仍须在该项目运行 `uv add utility-viz`。在项目内以 `uv run utility-viz` 调用工具，可让命令行与 Python 程序使用同一版本。

## 开发环境设置

```bash
git clone https://github.com/EconViz/utility-viz.git
cd utility-viz
uv sync --all-packages --all-extras
```

此仓库是 `uv` workspace，包含两个同步发布的软件包：根目录的 `utility-viz`，以及 `packages/econ-viz/` 中的 `econ-viz`，即[从 `econ-viz` 迁移](installation.md#sec-migrate)所述的兼容包。`uv sync --all-packages --all-extras` 会以可编辑模式安装两者，并安装开发依赖与所有可选依赖。完成后运行完整的质量检查：

```bash
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy .
```

## 验证安装

```bash
uv run utility-viz --version   # utility-viz 2.0.0b1
uv run utility-viz help
```

注释中的版本号仅为示例，实际输出取决于安装版本。也可用以下命令确认 Python 能导入绘图与求解接口：

```bash
uv run python -c "from utility_viz import Canvas, solve; print('OK')"
```

在服务器或其他没有图形界面的环境中，请以 `save()` 或命令行的 `--output` 输出文件。`show()` 需要可用的交互式绘图后端，窗口打不开不代表安装失败。

## 从 `econ-viz` 迁移

<span id="sec-migrate"></span>

`econ-viz` 于 2.0.0 更名为 `utility-viz`（参见[1.x 与 2.x 的名称](installation.md#tab-migrate)）。

<span id="tab-migrate"></span>

|  | 1.x | 2.x |
| --- | --- | --- |
| 发行包 | `pip install econ-viz` | `pip install utility-viz` |
| 导入 | `import econ_viz` | `import utility_viz` |
| 命令 | `econ-viz` | `utility-viz` |
| 配置文件 | `econ-viz.toml` | `utility-viz.toml` |

### 应安装哪个软件包

`utility-viz` 只提供 `utility_viz` 包与 `utility-viz` 命令。版本号相同的 `econ-viz` 2.x 是精简的兼容包：它依赖同版本的 `utility-viz`，并另外提供 `econ_viz` 包与 `econ-viz` 命令。因此以 `pip install --upgrade econ-viz` 升级 1.x 安装（预览版需加 `--pre`）会改用 2.x，旧代码仍可运行。代码不再导入 `econ_viz` 后，再改为 `pip install utility-viz`。

### 兼容层

在整个 2.x 期间，按文档编写的 1.x 代码仍可运行：

- `import econ_viz` 在每个进程中发出一次弃用警告。
- `from econ_viz import ...` 与文档记载的子模块（`econ_viz.models`、`econ_viz.optimizer`、`econ_viz.themes` 等）会对应到 `utility_viz` 的同名对象；名称未变更者是同一个对象。
- 创建 `econ_viz.Canvas`、`econ_viz.Figure` 或 `econ_viz.animation.Animator`，或访问 `econ_viz.Layout` 时，会发出指明替代名称的 `UtilityVizDeprecationWarning`。
- `econ-viz` 命令会打印弃用警告，再以相同参数运行 `utility-viz`。
- 旧的 `econ-viz.toml` 仍可读取，但会发出警告（详见[配置文件查找顺序](../guides/themes.md#sec-config-lookup)）；`utility-viz init --migrate` 可将其复制为 `utility-viz.toml`（详见[创建配置文件](cli.md#sec-cli-init)）。

<!-- api: agora.utility_viz.getting_started_installation_2 -->

`FutureWarning` 的子类，默认会显示。消息列出弃用版本、移除版本与替代方式，例如：

```text
econ_viz.Canvas is deprecated since 2.0.0 and will be removed in 3.0.0;
use utility_viz.Canvas instead.
```

### 更新代码

多数代码只需更改导入名称。1.x 中可单独导入的模块已移至别处（参见[已迁移的模块](installation.md#tab-migrate-modules)），其中的名称也可从软件包根目录导入。

<span id="tab-migrate-modules"></span>

| 1.x | 2.x |
| --- | --- |
| `econ_viz.optimizer` | `utility_viz`（根目录）或 `utility_viz.models` |
| `econ_viz.analysis` | `utility_viz.models` |
| `econ_viz.exceptions` | `utility_viz`（根目录） |
| `econ_viz.animation` | `utility_viz.core.animation` |
| `econ_viz.interactive` | `utility_viz.core.interactive` |

公开 API 为软件包根目录（`from utility_viz import Canvas, ...`）与 `utility_viz.models`。其他 `utility_viz.core.*` 模块属高级 API，可能在次要版本间迁移。

### 3.0.0 的移除范围

`econ_viz` 包、`econ-viz` 命令与 `econ-viz.toml` 查找于 3.0.0 移除，而非 2.0.0。兼容层只涵盖文档记载的 1.x API；未记载的深层路径（例如 `econ_viz.canvas.renderers`）仅尽力对应，随时可能移除。
