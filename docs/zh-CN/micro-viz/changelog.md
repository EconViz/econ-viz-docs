---
seo_title: "更新记录"
---

<span id="sec-changelog"></span>

# 更新记录

`micro-viz` 的发行记录。软件包目前为 0.2.0.dev0 版，尚未发布到 PyPI；保存库的 [CHANGELOG](https://github.com/EconViz/micro-viz/blob/main/CHANGELOG.md) 列出每一项变更。纯文档的变更不列入；每一条记录都链接到说明该功能的页面。

## 0.2.0.dev0

- 开发版的第一版文档：生产者理论、市场结构、要素市场、不确定性与信息 [简介](guides/introduction.md)
- 图形以 `mosaickit` 绘制（`mosaickit>=1.0.0rc9,<2.0.0`） [简介](guides/introduction.md)
- `Config` — 设置读自共用的 `econ-viz.toml`；`micro-viz` 在 `[micro]` 下声明自己的表 [设置](guides/settings.md)
- `Config` — `[micro.region]` 决定是否为边际报酬区间上色，以及底色填到图顶或只填到曲线 [设置](guides/settings.md)
- `save_svg` — 以画出静态图的同一个绘图函数制作动画 SVG 与 GIF；需要 `animation` 选用依赖 [动画](guides/animation.md)

