---
seo_title: "更新紀錄"
description: "econ-viz Python 套件的版本歷史：每個版本的新功能、修正與變更。"
---

# 更新紀錄

`econ-viz` 的版本歷史，不列出只有文件更新的項目。

<table class="ev-changelog">
  <thead>
  <tr><th>版本</th><th>更新內容</th></tr>
  </thead>
  <tbody>
  <tr id="v160">
    <td class="ev-changelog__version"><strong>v1.6.0</strong><br><span>2026-04-24</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>預設配色改為色盲友善配色，並提供可重複使用的 <code>themes.COLORBLIND_CYCLE_RGB</code> 與 <code>themes.COLORBLIND_CYCLE_HEX</code></li>
        <li>無異曲線的預設線寬從 <code>2.0</code> 調整為 <code>1.8</code></li>
      </ul>
      <p class="ev-changelog__type">維護</p>
      <ul>
        <li>動畫範例移至 <code>examples/scripts/animation.py</code></li>
        <li>不再追蹤 <code>examples/output/</code> 底下產生的檔案</li>
      </ul>
      <p class="ev-changelog__type">測試</p>
      <ul>
        <li>TikZ 座標軸回歸測試不再依賴顏色索引</li>
      </ul>
    </td>
  </tr>
  <tr id="v150">
    <td class="ev-changelog__version"><strong>v1.5.0</strong><br><span>2026-04-21</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增純 TikZ 匯出後端，<code>Canvas.save()</code> 與 <code>Figure.save()</code> 支援 <code>.tex</code></li>
        <li>新增價格效果分解：<code>decompose_price_effect()</code>、<code>PriceEffectDecomposition</code>，以及繪製 A/B/C 消費組合與替代／所得效果的 <code>Canvas.add_decomposition()</code></li>
        <li>分解相關 API 可直接從套件根目錄匯入</li>
        <li>新增分解、需求圖、PCC/ICC 路徑、多面板版面與 TikZ 匯出的範例腳本</li>
      </ul>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>筆記本在 Colab 上的安裝流程可安全重新啟動</li>
      </ul>
      <p class="ev-changelog__type">重構</p>
      <ul>
        <li>改善共用面板版面中座標軸標籤的位置與顯示控制</li>
      </ul>
      <p class="ev-changelog__type">測試</p>
      <ul>
        <li>新增 TikZ 匯出與價格效果分解的回歸測試</li>
      </ul>
    </td>
  </tr>
  <tr id="v140">
    <td class="ev-changelog__version"><strong>v1.4.0</strong><br><span>2026-04-09</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增 <code>Animator</code>，透過 Pillow 匯出參數變動的 GIF，不需要 ffmpeg</li>
        <li>新增 <code>WidgetViewer</code>，在 Jupyter 筆記本中用滑桿調整參數</li>
        <li>新增選用依賴 <code>animation</code>、<code>interactive</code> 與 <code>all</code></li>
        <li>新增常見效用函數的參數、價格、所得與只有預算線的 GIF 範例</li>
        <li>影格先疊在純色背景上再匯出，GIF 更穩定</li>
        <li>筆記本互動元件除了滑桿，也能直接輸入數值</li>
      </ul>
      <p class="ev-changelog__type">測試</p>
      <ul>
        <li>新增 <code>Animator</code> 與 <code>WidgetViewer</code> 的測試</li>
      </ul>
    </td>
  </tr>
  <tr id="v132">
    <td class="ev-changelog__version"><strong>v1.3.2</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>Edgeworth 契約線與價格線預設為黑色虛線</li>
      </ul>
      <p class="ev-changelog__type">維護</p>
      <ul>
        <li>發佈流程會略過 PyPI 上已存在的版本</li>
      </ul>
    </td>
  </tr>
  <tr id="v131">
    <td class="ev-changelog__version"><strong>v1.3.1</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>Edgeworth 內部拆分為計算、狀態與繪圖三個模組</li>
        <li>新增模型登錄表（<code>models.registry</code>），命令列工具改由它建立模型</li>
      </ul>
      <p class="ev-changelog__type">重構</p>
      <ul>
        <li>命令列工具的錯誤改為拋出 <code>CliConfigError</code>，並統一在 <code>cli.main</code> 處理結束流程</li>
        <li>等高線水準的共用規則集中到 <code>contours.level_policies</code></li>
        <li><code>Canvas</code>、<code>Figure</code> 與 <code>EdgeworthBox</code> 共用同一個匯出器（<code>io.exporter</code>）</li>
        <li>Canvas 的繪製邏輯拆分到 <code>canvas.renderers</code> 與 <code>canvas.primitives</code></li>
        <li>套件根目錄的匯出改為延遲載入，公開 API 不變</li>
      </ul>
    </td>
  </tr>
  <tr id="v130">
    <td class="ev-changelog__version"><strong>v1.3.0</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增 <code>EdgeworthBox</code> 與 <code>EquilibriumFocusConfig</code>，繪製兩人交換的 Edgeworth 箱形圖</li>
        <li>新增契約線、核、Walras 均衡疊圖，以及聚焦於均衡的無異曲線</li>
        <li>新增涵蓋常見效用函數組合的 <code>examples/edgeworth_box.py</code></li>
        <li>新增 Edgeworth 專屬測試</li>
      </ul>
    </td>
  </tr>
  <tr id="v123">
    <td class="ev-changelog__version"><strong>v1.2.3</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li><code>SlutskyMatrix</code> 新增對稱性、半負定性與齊次性檢查，條件不成立時會發出警告</li>
        <li>命令列工具支援 <code>QuasiLinear</code>、<code>StoneGeary</code> 與 <code>Translog</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v122">
    <td class="ev-changelog__version"><strong>v1.2.2</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>PCC/ICC 路徑預設平滑化，端點稍微延伸，標記點預設不顯示</li>
        <li>PCC/ICC 路徑改用獨立顏色，需求圖的商品空間邊距加大</li>
        <li>新增 PCC/ICC 範例產生器與測試</li>
      </ul>
    </td>
  </tr>
  <tr id="v120">
    <td class="ev-changelog__version"><strong>v1.2.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增多面板 <code>Figure</code> 版面與 <code>Layout</code> 列舉</li>
        <li>新增連動的 <code>DemandDiagram</code>，繪製 Marshall 需求</li>
        <li>新增 <code>PricePath</code>、<code>IncomePath</code> 與 <code>Canvas.add_path()</code>，繪製 PCC/ICC</li>
      </ul>
    </td>
  </tr>
  <tr id="v110">
    <td class="ev-changelog__version"><strong>v1.1.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">新功能</p>
      <ul>
        <li>新增比較靜態工具 <code>comparative_statics</code></li>
        <li>分析模組新增 <code>HomogeneityAnalyzer</code> 與 <code>ReturnsToScale</code></li>
        <li>新增 <code>Translog</code> 模型，並支援圖例與無異曲線標籤</li>
      </ul>
    </td>
  </tr>
  <tr id="v102">
    <td class="ev-changelog__version"><strong>v1.0.2</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>數學式座標軸標籤不再被重複包裝</li>
        <li>移除 NumPy 版本上限，避免在 Colab 上發生衝突</li>
      </ul>
    </td>
  </tr>
  <tr id="v101">
    <td class="ev-changelog__version"><strong>v1.0.1</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">錯誤修正</p>
      <ul>
        <li>鎖定 <code>numpy&lt;2</code>，避免在 Colab 與本機安裝時 ABI 不相容</li>
      </ul>
      <p class="ev-changelog__type">維護</p>
      <ul>
        <li>放寬 Python 與 NumPy 版本限制，<code>pytest</code> 鎖定在 8.x</li>
      </ul>
    </td>
  </tr>
  <tr id="v100">
    <td class="ev-changelog__version"><strong>v1.0.0</strong><br><span>2026-03-28</span></td>
    <td>
      <ul>
        <li>首次發布</li>
      </ul>
    </td>
  </tr>
  </tbody>
</table>
