---
seo_title: "更新日志"
description: "econ-viz Python 包的版本历史：每个版本的新功能、修复与变更。"
---

# 更新日志

`econ-viz` 的版本历史，不列出仅有文档更新的条目。

<table class="ev-changelog">
  <thead>
  <tr><th>版本</th><th>更新内容</th></tr>
  </thead>
  <tbody>
  <tr id="v160">
    <td class="ev-changelog__version"><strong>v1.6.0</strong><br><span>2026-04-24</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>默认配色改为色盲友好配色，并提供可复用的 <code>themes.COLORBLIND_CYCLE_RGB</code> 与 <code>themes.COLORBLIND_CYCLE_HEX</code></li>
        <li>无差异曲线的默认线宽从 <code>2.0</code> 调整为 <code>1.8</code></li>
      </ul>
      <p class="ev-changelog__type">维护</p>
      <ul>
        <li>动画示例移至 <code>examples/scripts/animation.py</code></li>
        <li>不再跟踪 <code>examples/output/</code> 下生成的文件</li>
      </ul>
      <p class="ev-changelog__type">测试</p>
      <ul>
        <li>TikZ 坐标轴回归测试不再依赖颜色索引</li>
      </ul>
    </td>
  </tr>
  <tr id="v150">
    <td class="ev-changelog__version"><strong>v1.5.0</strong><br><span>2026-04-21</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增纯 TikZ 导出后端，<code>Canvas.save()</code> 与 <code>Figure.save()</code> 支持 <code>.tex</code></li>
        <li>新增价格效应分解：<code>decompose_price_effect()</code>、<code>PriceEffectDecomposition</code>，以及绘制 A/B/C 消费组合与替代／收入效应的 <code>Canvas.add_decomposition()</code></li>
        <li>分解相关 API 可直接从包根目录导入</li>
        <li>新增分解、需求图、PCC/ICC 路径、多面板布局与 TikZ 导出的示例脚本</li>
      </ul>
      <p class="ev-changelog__type">错误修复</p>
      <ul>
        <li>笔记本在 Colab 上的安装流程可安全重启</li>
      </ul>
      <p class="ev-changelog__type">重构</p>
      <ul>
        <li>改进共享面板布局中坐标轴标签的位置与显示控制</li>
      </ul>
      <p class="ev-changelog__type">测试</p>
      <ul>
        <li>新增 TikZ 导出与价格效应分解的回归测试</li>
      </ul>
    </td>
  </tr>
  <tr id="v140">
    <td class="ev-changelog__version"><strong>v1.4.0</strong><br><span>2026-04-09</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增 <code>Animator</code>，通过 Pillow 导出参数变动的 GIF，无需 ffmpeg</li>
        <li>新增 <code>WidgetViewer</code>，在 Jupyter 笔记本中用滑块调整参数</li>
        <li>新增可选依赖 <code>animation</code>、<code>interactive</code> 与 <code>all</code></li>
        <li>新增常见效用函数的参数、价格、收入与仅预算线的 GIF 示例</li>
        <li>帧先叠加在纯色背景上再导出，GIF 更稳定</li>
        <li>笔记本交互组件除了滑块，也能直接输入数值</li>
      </ul>
      <p class="ev-changelog__type">测试</p>
      <ul>
        <li>新增 <code>Animator</code> 与 <code>WidgetViewer</code> 的测试</li>
      </ul>
    </td>
  </tr>
  <tr id="v132">
    <td class="ev-changelog__version"><strong>v1.3.2</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">错误修复</p>
      <ul>
        <li>Edgeworth 契约线与价格线默认为黑色虚线</li>
      </ul>
      <p class="ev-changelog__type">维护</p>
      <ul>
        <li>发布流程会跳过 PyPI 上已存在的版本</li>
      </ul>
    </td>
  </tr>
  <tr id="v131">
    <td class="ev-changelog__version"><strong>v1.3.1</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>Edgeworth 内部拆分为计算、状态与绘图三个模块</li>
        <li>新增模型注册表（<code>models.registry</code>），命令行工具改由它创建模型</li>
      </ul>
      <p class="ev-changelog__type">重构</p>
      <ul>
        <li>命令行工具的错误改为抛出 <code>CliConfigError</code>，并统一在 <code>cli.main</code> 处理退出流程</li>
        <li>等高线水平的共用规则集中到 <code>contours.level_policies</code></li>
        <li><code>Canvas</code>、<code>Figure</code> 与 <code>EdgeworthBox</code> 共用同一个导出器（<code>io.exporter</code>）</li>
        <li>Canvas 的绘制逻辑拆分到 <code>canvas.renderers</code> 与 <code>canvas.primitives</code></li>
        <li>包根目录的导出改为延迟加载，公开 API 不变</li>
      </ul>
    </td>
  </tr>
  <tr id="v130">
    <td class="ev-changelog__version"><strong>v1.3.0</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增 <code>EdgeworthBox</code> 与 <code>EquilibriumFocusConfig</code>，绘制两人交换的 Edgeworth 盒状图</li>
        <li>新增契约线、核、Walras 均衡叠加图，以及聚焦于均衡的无差异曲线</li>
        <li>新增涵盖常见效用函数组合的 <code>examples/edgeworth_box.py</code></li>
        <li>新增 Edgeworth 专属测试</li>
      </ul>
    </td>
  </tr>
  <tr id="v123">
    <td class="ev-changelog__version"><strong>v1.2.3</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li><code>SlutskyMatrix</code> 新增对称性、半负定性与齐次性检查，条件不成立时会发出警告</li>
        <li>命令行工具支持 <code>QuasiLinear</code>、<code>StoneGeary</code> 与 <code>Translog</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v122">
    <td class="ev-changelog__version"><strong>v1.2.2</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">错误修复</p>
      <ul>
        <li>PCC/ICC 路径默认平滑化，端点稍微延伸，标记点默认不显示</li>
        <li>PCC/ICC 路径改用独立颜色，需求图的商品空间边距加大</li>
        <li>新增 PCC/ICC 示例生成器与测试</li>
      </ul>
    </td>
  </tr>
  <tr id="v120">
    <td class="ev-changelog__version"><strong>v1.2.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增多面板 <code>Figure</code> 布局与 <code>Layout</code> 枚举</li>
        <li>新增联动的 <code>DemandDiagram</code>，绘制马歇尔需求</li>
        <li>新增 <code>PricePath</code>、<code>IncomePath</code> 与 <code>Canvas.add_path()</code>，绘制 PCC/ICC</li>
      </ul>
    </td>
  </tr>
  <tr id="v110">
    <td class="ev-changelog__version"><strong>v1.1.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增比较静态工具 <code>comparative_statics</code></li>
        <li>分析模块新增 <code>HomogeneityAnalyzer</code> 与 <code>ReturnsToScale</code></li>
        <li>新增 <code>Translog</code> 模型，并支持图例与无差异曲线标签</li>
      </ul>
    </td>
  </tr>
  <tr id="v102">
    <td class="ev-changelog__version"><strong>v1.0.2</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">错误修复</p>
      <ul>
        <li>数学式坐标轴标签不再被重复包装</li>
        <li>移除 NumPy 版本上限，避免在 Colab 上发生冲突</li>
      </ul>
    </td>
  </tr>
  <tr id="v101">
    <td class="ev-changelog__version"><strong>v1.0.1</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">错误修复</p>
      <ul>
        <li>锁定 <code>numpy&lt;2</code>，避免在 Colab 与本地安装时 ABI 不兼容</li>
      </ul>
      <p class="ev-changelog__type">维护</p>
      <ul>
        <li>放宽 Python 与 NumPy 版本限制，<code>pytest</code> 锁定在 8.x</li>
      </ul>
    </td>
  </tr>
  <tr id="v100">
    <td class="ev-changelog__version"><strong>v1.0.0</strong><br><span>2026-03-28</span></td>
    <td>
      <ul>
        <li>首次发布</li>
      </ul>
    </td>
  </tr>
  </tbody>
</table>
