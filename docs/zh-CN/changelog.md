---
seo_title: "更新日志"
description: "econ-viz Python 包的版本历史：每个版本的新功能、修正与变更。"
---

# 更新日志

本页同步自项目的 `CHANGELOG.md`。

## v1.4.0 (2026-04-10)

### 新功能

- 添加 `Animator` GIF 导出范例，涵盖四种标准效用函数的参数、价格与收入变动
- 添加只有预算线的变动范例，让教学页面能单独呈现预算约束的移动
- `WidgetViewer` 在滑块旁边添加数字输入框，方便在笔记本中使用

### 修正

- 导出前先把每一格叠在白色背景上，避免 GIF 帧残影堆叠
- 让安装保存格可以安全地重新启动，改善 Playground 笔记本在 Colab 上的安装流程

<div class="media-grid" markdown>
  <figure class="gif-card">
    <img src="../../assets/animation/price_sweeps/cobb_douglas_price_sweep.gif" alt="Cobb-Douglas 价格变动 GIF">
    <figcaption>Cobb-Douglas 价格变动：效用函数固定，预算线移动。</figcaption>
  </figure>
  <figure class="gif-card">
    <img src="../../assets/animation/income_sweeps/budget_only_income_sweep.gif" alt="只有预算线的收入变动 GIF">
    <figcaption>只有预算线的收入变动，用来单独呈现预算线的移动。</figcaption>
  </figure>
</div>

## v1.2.0 (2026-03-30)

### 新功能

- 添加多面板 `Figure` 布局与 `Layout` 枚举（closes #7）
- 添加联动的 `DemandDiagram`，用于马歇尔需求教学图（closes #31）
- 添加 `PricePath` / `IncomePath` 工具与 `Canvas.add_path()`，用来画 PCC / ICC（closes #5）

![v1.2.0 需求图功能](../assets/consumer/demand_cobb_douglas.png)

## v1.1.0 (2026-03-30)

### 新功能

- 添加 `comparative_statics` 工具（closes #12）
- 在分析子模块添加 `HomogeneityAnalyzer` 与 `ReturnsToScale`（closes #14）
- 添加 `Translog` 模型（#9），并支持图例与无差异曲线标签（#11）

## v1.0.2 (2026-03-29)

### 错误修正

- 避免数学座标轴标签被重复包装（closes #2）
- 移除 NumPy 的版本上限，避免在 Colab 环境中发生冲突

## v1.0.1 (2026-03-29)

### 错误修正

- 锁定 `numpy<2`，避免在 Colab 与本机安装时发生 ABI 不兼容

### 杂项

- 放宽 Python / NumPy 版本限制，并把 `pytest` 锁定在 8.x

### 文文件

- 在 README 加入 Stone-Geary，并更新测试数量徽章

## v1.0.0 (2026-03-28)

- 首次发布
