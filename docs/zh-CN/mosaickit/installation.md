---
seo_title: "安装"
---

# 安装

<span id="sec-install"></span>

## 系统需求

`mosaickit` 需要 Python 3.10 以上、`NumPy` 1.24 以上、`Matplotlib` 3.6 以上（4 以下）与负责排版文字的 `glyphkit` 1.0.0b3 以上（2 以下）；在 Python 3.10 上还会安装 `tomli` 来读取 TOML。

## 安装软件包

```bash
uv add mosaickit                 # the library
uv add "mosaickit==1.0.0rc6"     # the version this manual describes
```

1.0.0rc6 是预览版。在 1.0 正式版发布之前，直接运行 `uv add mosaickit` 或 `pip install mosaickit` 安装的是 0.9.2；需以 `uv add --prerelease allow mosaickit` 或 `pip install --pre mosaickit` 才能安装预览版。

如果使用 `pip`，请运行 `python -m pip install mosaickit`。导入 `mosaickit` 时不会一并导入 Matplotlib：内置渲染器要到画布第一次绘制时，才会按名称加载（详见[绘制](guides/rendering.md#sec-rendering)）。

## 开发环境

```bash
git clone https://github.com/EconViz/mosaickit.git
cd mosaickit
uv sync --locked
uv run pre-commit install
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run mypy
uv run lint-imports
uv build
```

锁文件固定了所有开发依赖包的版本。持续集成流程会在 Python 3.10、3.11、3.12 与 3.13 上运行相同命令，再将构建完成的 wheel 安装到干净环境，确认其中不含 `bezierkit`，最后以该 wheel 运行测试。导入规则维持分层：场景、样式、主题与参数模块不会导入绘制与画布模块，核心也不会导入任何领域软件包。
