---
seo_title: "安装"
---

# 安装

<span id="sec-install"></span>

`kinetickit` 支持 Python 3.10 到 3.13。每种安装都会包含 NumPy 与 GlyphKit。它目前以预发行版本放在 PyPI，所以 uv 要加上 `--prerelease allow`。

```bash
uv add --prerelease allow kinetickit               # 动态 SVG
uv add --prerelease allow "kinetickit[raster]"     # SVG 与 GIF
uv add --prerelease allow "kinetickit[interactive]"# SVG 與 HTML
uv add --prerelease allow "kinetickit[studio]"     # 全部内置格式
uv add "kinetickit[studio]==1.0.0b2"               # 固定在某个版本
```

| 额外安装项 | 加入的软件包 | 输出 |
| --- | --- | --- |
| 无 | NumPy、GlyphKit | 动态 SVG（`vector`） |
| `raster` | Matplotlib、Pillow | GIF（`raster`） |
| `interactive` | Plotly | 交互 HTML（`interactive`） |
| `studio` | 以上全部 | 三种都有 |

这些第三方软件包只出现在私有适配器后面，不会进入公开的场景或绘图端接口，之后也可能在不造成破坏性变更的情况下换掉。

要存成的格式缺少对应的额外安装项时，会抛出 `CapabilityError` 并指出该装哪一项，同时不会写出任何文件。`available_formats()` 列出的是已登录的格式，所以即使缺少额外安装项，也会列出三种。

开发环境的设置方式如下：

```bash
git clone https://github.com/EconViz/kinetickit.git
cd kinetickit
uv sync --all-extras
uv run pytest
uv run ruff check .
uv run mypy
uv run lint-imports
uv run python -m kinetickit.conformance
```
