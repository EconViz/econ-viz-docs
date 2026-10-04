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
  <tr id="v1120">
    <td class="ev-changelog__version"><strong>v1.12.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li><code>highlight_level</code> 可强调一条主要无差异曲线，其余效用水平会使用淡化的次要样式</li>
        <li><code>secondary_stroke</code> 与主题字段可控制次要曲线的颜色、线宽与不透明度</li>
        <li>支持数值与序数标签（<i>u</i><sub>1</sub>、<i>u</i><sub>2</sub>……）；标签会跟随曲线角度并避开图形边界</li>
      </ul>
      <p class="ev-changelog__type">变更</p>
      <ul>
        <li>主要与次要曲线标签共用主题的无差异曲线标签样式；平滑、线性、折点与饱和偏好仍完整支持</li>
      </ul>
    </td>
  </tr>
  <tr id="v1110">
    <td class="ev-changelog__version"><strong>v1.11.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>补齐图形背景、标签、线条、标记点与辅助经济线条的主题控制</li>
        <li>新增 <code>paper</code>、<code>monochrome</code>、<code>presentation</code> 与 <code>dark</code> 四个内置主题</li>
        <li>新增主题层级的 <code>background_color</code> 与 <code>label_scale</code> 控制</li>
      </ul>
    </td>
  </tr>
  <tr id="v1101">
    <td class="ev-changelog__version"><strong>v1.10.1</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">维护</p>
      <ul>
        <li>在开发工具与 CI 中加入 Ruff 代码检查、格式验证及 Mypy 类型检查</li>
        <li>加入 <code>py.typed</code>，将 <code>econ-viz</code> 发布为 PEP 561 类型包</li>
        <li>将公开异常信息统一为英文</li>
      </ul>
      <p class="ev-changelog__type">错误修复</p>
      <ul>
        <li>补上等高线层级类型注解缺少的 NumPy import</li>
        <li>让 Edgeworth Pareto 搜索的每个 closure 绑定各自的权重</li>
      </ul>
    </td>
  </tr>
  <tr id="v1100">
    <td class="ev-changelog__version"><strong>v1.10.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增 <code>Config</code>，从 <code>econ-viz.toml</code> 配置文件加载图形设置；<code>Config.load(...).use()</code> 会把它设为默认</li>
        <li>新增 <code>econ-viz init</code> 生成带注释的配置文件模板，<code>econ-viz plot --config</code> 可读取配置文件</li>
      </ul>
      <p class="ev-changelog__type">变更</p>
      <ul>
        <li>没有指定 theme 或字体时，图形改用当前生效的 <code>Config</code>；没有配置文件时输出不变</li>
        <li>Python 3.10 需要安装 <code>tomli</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v190">
    <td class="ev-changelog__version"><strong>v1.9.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>价格效应分解默认画出无差异曲线：通过 A 的 U<sub>0</sub>、通过 C 的 U<sub>1</sub>，Slutsky 分解还有通过 B 的曲线</li>
        <li>新增 <code>Haagsma</code> 效用模型，其商品 x 一定是劣等品，收入足够高时成为吉芬商品</li>
        <li>新增 <code>Legend</code>，自动放在最不遮挡图形的位置，也可指定角落或图外的上下左右</li>
        <li>所有文字都能用 <code>Label</code> 调整：坐标轴标签、原点、标题、效应标签、Edgeworth 盒状图文字</li>
        <li><code>Stroke</code>、<code>Marker</code>、<code>Label</code>、<code>Legend</code>、<code>Effect</code>、<code>Fill</code> 都支持 <code>opacity</code></li>
      </ul>
      <p class="ev-changelog__type">变更</p>
      <ul>
        <li>已有的效应分解图会多出无差异曲线；传入 <code>show_curves=False</code> 即可回到原来的图</li>
        <li>效应范围箭头改为单向，从 A 指向 B、从 B 指向 C</li>
      </ul>
      <p class="ev-changelog__type">错误修复</p>
      <ul>
        <li>提高最优化的精度，比较静态与 Slutsky 矩阵更准确</li>
        <li>效用为负值的无差异曲线改画实线</li>
      </ul>
    </td>
  </tr>
  <tr id="v180">
    <td class="ev-changelog__version"><strong>v1.8.0</strong><br><span>2026-09-26</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li><code>Effect</code> 可设置价格效应分解中每个效应的颜色、范围箭头高度与标签</li>
        <li><code>Marker</code> 可设置画布、需求图与 Edgeworth 盒状图中点的颜色、大小与形状</li>
        <li><code>Label</code> 可设置点标签的文字、位置（上下左右与四个角落）、偏移、颜色、大小与是否显示，也能隐藏效应分解的 A/B/C 标签</li>
        <li><code>Fill</code> 让预算集的阴影可以有自己的颜色与透明度</li>
        <li><code>Axis</code> 用一个对象设置单个坐标轴的标签、标签位置与线条</li>
        <li>新增标记点、标签与阴影的主题默认值，例如 <code>theme.eq_marker</code>、<code>theme.point_label</code> 与 <code>theme.budget_fill</code></li>
      </ul>
      <p class="ev-changelog__type">变更</p>
      <ul>
        <li>均衡点的默认大小从 6 缩小为 4</li>
        <li>建议用 <code>Stroke</code> 设置线条样式，另外的颜色、粗细与线型参数保留为简写</li>
      </ul>
      <p class="ev-changelog__type">错误修复</p>
      <ul>
        <li>楔形箭头在画面上保持固定大小，不再沿整条线拉长</li>
        <li>Edgeworth 盒状图均衡点的无差异曲线会应用 <code>stroke_a</code> / <code>stroke_b</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v170">
    <td class="ev-changelog__version"><strong>v1.7.0</strong><br><span>2026-09-25</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li><code>Canvas</code> 与 <code>Figure</code> 可分别设置坐标轴标签位置、线条样式与箭头样式</li>
        <li>可为单张图设置文字与数学字体，不会改动 Matplotlib 的全局设置</li>
        <li><code>Stroke</code> 统一控制画布、多面板图、需求图与 Edgeworth 盒状图中的线条粗细、线条样式、颜色与箭头样式</li>
        <li><code>econ-viz --version</code> 可显示已安装的包版本</li>
      </ul>
      <p class="ev-changelog__type">错误修复</p>
      <ul>
        <li>修正效用模型的参数定义域、非对称 CES 扩展路径、Cobb-Douglas 极限，以及收入未用尽时的饱和偏好最优解</li>
        <li>等高线水平可正确处理零与负效用值</li>
        <li>比较静态在价格、收入或最低消费约束附近改用边界安全的有限差分</li>
        <li>所有示例脚本均可从全新 checkout 直接运行</li>
      </ul>
      <p class="ev-changelog__type">维护</p>
      <ul>
        <li>包管理与构建流程迁移至 <code>uv</code></li>
        <li>CI 测试 Python 3.10–3.13、检查分支覆盖率，并运行所有可执行示例</li>
        <li>版本标签触发的发布流程仅在测试通过后才会上传包</li>
      </ul>
    </td>
  </tr>
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
