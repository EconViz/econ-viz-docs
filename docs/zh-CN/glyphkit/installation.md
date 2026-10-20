---
seo_title: "安装"
---

# 安装

<span id="sec-install"></span>

`glyphkit` 支持 Python 3.10 到 3.13。

```bash
uv add --prerelease allow glyphkit
uv add --prerelease allow "glyphkit[portable]"  # 加入 WOFF2 子集数据
uv add "glyphkit==1.0.0b2"                       # 本手册使用的版本
```

基本安装包含 FontTools、HarfBuzz 绑定、Unicode 分段与双向文本支持。`portable` 额外安装 Brotli，供 WOFF2 输出使用；两种安装都不包含渲染器。

开发环境的设置方式如下：

```bash
git clone https://github.com/EconViz/glyphkit.git
cd glyphkit
uv sync --all-extras
uv run pytest
uv run ruff check .
uv run mypy
uv run lint-imports
```
