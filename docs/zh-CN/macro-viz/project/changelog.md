---
seo_title: "更新纪录"
---

# 更新纪录

`macro-viz` 版本为 `0.2.0.dev0`。保存库的 [CHANGELOG](https://github.com/EconViz/macro-viz/blob/main/CHANGELOG.md) 列出每一项变更。

## 尚未发布

### 添加

- 模型家族 `keynesian`、`money`、`adas`、`islm`、`growth`、`labor`、`open_economy` 与 `panels`，各有类型化模型、比较与绘图函数。
- 已注册的 `[macro.*]` 设置结构，以及英文、繁体中文与简体中文的语系表。
- `macro_viz.animation` 与 `macro-viz[animation]` 选项：任何绘图函数都能输出 GIF 与动画 SVG。
- 带类型化曲线移动的连动四面板与五面板图。

### 变更

- 图形遵循 manual 风格：黑白、只有价格 `p` 用小写、细的 45 度线。
- 变动后的曲线是细实线；平行移动是从旧均衡指向新曲线的直线箭头；弯曲箭头只代表转动；曲线名称放在线的末端。

### 移除

- 数据串行、国民所得帐与景气循环系列：统计图不在范围内。
