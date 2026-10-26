---
seo_title: "安装"
---

# 安装

<span id="sec-install"></span>

`glyphkit` 支持 Python 3.10 到 3.13。它目前以预发行版本放在 PyPI，所以 uv 要加上 `--prerelease allow`。

```bash
uv add --prerelease allow glyphkit
uv add --prerelease allow "glyphkit[portable]"  # 加入 WOFF2 子集数据
uv add "glyphkit==1.0.0b4"                       # 固定在某个版本
```

基本安装包含 FontTools、HarfBuzz 绑定（`uharfbuzz`）、Unicode 分段（`uniseg`）与双向文本支持（`python-bidi`）。`portable` 额外安装 Brotli，WOFF2 输出需要它；没有它也能输出 SFNT 子集。两种安装都不包含绘图端。

字体也不会一起安装。GlyphKit 只读取你传进去的字体，所以示例假设脚本旁边有一个 `fonts/` 文件夹。示例使用开源字体 Source Sans 3 与 Noto Sans TC，数学式则使用 STIX Two Math。

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
