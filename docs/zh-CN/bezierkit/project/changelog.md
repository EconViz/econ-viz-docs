---
seo_title: "更新纪录"
---

<span id="sec-changelog"></span>

# 更新纪录

本章列出影响软件包使用的版本变更，不含仅修改文档的版本；各条目按 l3doc 惯例标注于它所描述的功能旁，页码即该功能的实际页码。

## 1.0.0

- 第一个正式版；公开 API 按语义化版本管理 [简介](../guides/introduction.md)
- `bezierkit` — 持续整合测试 Python 3.10、3.11、3.12 与 3.13 [安装](../installation.md)
- `PiecewiseBezier.segment` — `t0` 落在线段内部时回传正确的区间；先前会先在 `t0` 分割再对后半段重新参数化，导致终点错误 [三次线段与路径](../guides/paths.md)

## 0.5.0rc1

- 首次发布到 PyPI：任意次数的 Bézier 曲线、三次线段与路径、构造、Hermite 插值、拟合、等值线描绘、采样、导出器与命令行界面 [简介](../guides/introduction.md)

