---
seo_title: "Changelog"
description: "Release history of the econ-viz Python package: new features, fixes, and changes in each version."
---

# Changelog

Release history of `econ-viz`. Documentation-only changes are not listed.

<table class="ev-changelog">
  <thead>
  <tr><th>Version</th><th>Changes</th></tr>
  </thead>
  <tbody>
  <tr id="v170">
    <td class="ev-changelog__version"><strong>v1.7.0</strong><br><span>2026-09-25</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Independent axis-label positions, line styles, and arrowhead styles for <code>Canvas</code> and <code>Figure</code></li>
        <li>Per-figure text and math fonts without changing Matplotlib's global configuration</li>
        <li><code>Stroke</code> controls line width, style, colour, and arrowheads across canvases, figures, demand diagrams, and Edgeworth boxes</li>
        <li><code>econ-viz --version</code> prints the installed package version</li>
      </ul>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Correct utility-model domains, asymmetric CES expansion paths, Cobb-Douglas limits, and satiation optima with unspent income</li>
        <li>Robust contour levels around zero and negative utility values</li>
        <li>Boundary-safe comparative statics near zero prices, income, and subsistence constraints</li>
        <li>All example scripts run from a clean checkout</li>
      </ul>
      <p class="ev-changelog__type">Maintenance</p>
      <ul>
        <li>Package management and builds migrated to <code>uv</code></li>
        <li>CI tests Python 3.10–3.13, enforces branch coverage, and smoke-tests runnable examples</li>
        <li>Tagged releases publish only after tests pass</li>
      </ul>
    </td>
  </tr>
  <tr id="v160">
    <td class="ev-changelog__version"><strong>v1.6.0</strong><br><span>2026-04-24</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Colour-blind-friendly default palette, with reusable <code>themes.COLORBLIND_CYCLE_RGB</code> and <code>themes.COLORBLIND_CYCLE_HEX</code></li>
        <li>Default indifference-curve line width reduced from <code>2.0</code> to <code>1.8</code></li>
      </ul>
      <p class="ev-changelog__type">Maintenance</p>
      <ul>
        <li>Animation example moved to <code>examples/scripts/animation.py</code></li>
        <li>Generated files under <code>examples/output/</code> are no longer tracked</li>
      </ul>
      <p class="ev-changelog__type">Tests</p>
      <ul>
        <li>TikZ axis regression test no longer depends on colour indices</li>
      </ul>
    </td>
  </tr>
  <tr id="v150">
    <td class="ev-changelog__version"><strong>v1.5.0</strong><br><span>2026-04-21</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Pure TikZ export backend; <code>Canvas.save()</code> and <code>Figure.save()</code> accept <code>.tex</code></li>
        <li>Price-effect decomposition: <code>decompose_price_effect()</code>, <code>PriceEffectDecomposition</code>, and <code>Canvas.add_decomposition()</code> for A/B/C bundles and substitution/income overlays</li>
        <li>Decomposition APIs importable from the package root</li>
        <li>New example scripts for decomposition, demand diagrams, PCC/ICC paths, multi-panel layouts, and TikZ export</li>
      </ul>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Notebook install flow on Colab is restart-safe</li>
      </ul>
      <p class="ev-changelog__type">Refactoring</p>
      <ul>
        <li>Better axis-label placement and visibility in shared-panel layouts</li>
      </ul>
      <p class="ev-changelog__type">Tests</p>
      <ul>
        <li>Regression tests for TikZ export and price-effect decomposition</li>
      </ul>
    </td>
  </tr>
  <tr id="v140">
    <td class="ev-changelog__version"><strong>v1.4.0</strong><br><span>2026-04-09</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>Animator</code> for GIF parameter sweeps via Pillow, no ffmpeg required</li>
        <li><code>WidgetViewer</code> for slider controls in Jupyter notebooks</li>
        <li>Optional extras <code>animation</code>, <code>interactive</code>, and <code>all</code></li>
        <li>Parameter, price, income, and budget-only GIF examples for common utility functions</li>
        <li>More reliable GIF export by compositing frames onto a solid background</li>
        <li>Notebook widgets accept typed values alongside sliders</li>
      </ul>
      <p class="ev-changelog__type">Tests</p>
      <ul>
        <li>Tests for <code>Animator</code> and <code>WidgetViewer</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v132">
    <td class="ev-changelog__version"><strong>v1.3.2</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Edgeworth contract curves and price lines default to dashed black</li>
      </ul>
      <p class="ev-changelog__type">Maintenance</p>
      <ul>
        <li>Publish workflow skips versions already on PyPI</li>
      </ul>
    </td>
  </tr>
  <tr id="v131">
    <td class="ev-changelog__version"><strong>v1.3.1</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Edgeworth internals split into compute, state, and plotter modules</li>
        <li>Model registry (<code>models.registry</code>), used by the CLI to build models</li>
      </ul>
      <p class="ev-changelog__type">Refactoring</p>
      <ul>
        <li>CLI errors raise <code>CliConfigError</code>, with exit handling centralized in <code>cli.main</code></li>
        <li>Shared contour-level policies in <code>contours.level_policies</code></li>
        <li>One figure exporter (<code>io.exporter</code>) shared by <code>Canvas</code>, <code>Figure</code>, and <code>EdgeworthBox</code></li>
        <li>Canvas rendering split into <code>canvas.renderers</code> and <code>canvas.primitives</code></li>
        <li>Package-root exports load lazily, with the public API unchanged</li>
      </ul>
    </td>
  </tr>
  <tr id="v130">
    <td class="ev-changelog__version"><strong>v1.3.0</strong><br><span>2026-04-03</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>EdgeworthBox</code> and <code>EquilibriumFocusConfig</code> for two-consumer exchange diagrams</li>
        <li>Contract curve, core, Walrasian equilibrium overlay, and equilibrium-focused indifference curves</li>
        <li><code>examples/edgeworth_box.py</code> covering common utility-function combinations</li>
        <li>Dedicated Edgeworth tests</li>
      </ul>
    </td>
  </tr>
  <tr id="v123">
    <td class="ev-changelog__version"><strong>v1.2.3</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>SlutskyMatrix</code> checks symmetry, negative semidefiniteness, and homogeneity, and warns when a condition fails</li>
        <li>CLI supports <code>QuasiLinear</code>, <code>StoneGeary</code>, and <code>Translog</code></li>
      </ul>
    </td>
  </tr>
  <tr id="v122">
    <td class="ev-changelog__version"><strong>v1.2.2</strong><br><span>2026-03-31</span></td>
    <td>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>PCC/ICC paths are smoothed by default, with slightly extended endpoints and markers hidden unless requested</li>
        <li>PCC/ICC paths use their own colours, and demand diagrams have more goods-space padding</li>
        <li>Dedicated PCC/ICC example generator and tests</li>
      </ul>
    </td>
  </tr>
  <tr id="v120">
    <td class="ev-changelog__version"><strong>v1.2.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li>Multi-panel <code>Figure</code> layouts and the <code>Layout</code> enum</li>
        <li>Linked <code>DemandDiagram</code> for Marshallian demand</li>
        <li><code>PricePath</code>, <code>IncomePath</code>, and <code>Canvas.add_path()</code> for PCC/ICC plots</li>
      </ul>
    </td>
  </tr>
  <tr id="v110">
    <td class="ev-changelog__version"><strong>v1.1.0</strong><br><span>2026-03-30</span></td>
    <td>
      <p class="ev-changelog__type">Features</p>
      <ul>
        <li><code>comparative_statics</code> helper</li>
        <li><code>HomogeneityAnalyzer</code> and <code>ReturnsToScale</code> in the analysis module</li>
        <li><code>Translog</code> model, plus legend and indifference-curve labels</li>
      </ul>
    </td>
  </tr>
  <tr id="v102">
    <td class="ev-changelog__version"><strong>v1.0.2</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Math axis labels are no longer double-wrapped</li>
        <li>NumPy upper bound removed to avoid conflicts on Colab</li>
      </ul>
    </td>
  </tr>
  <tr id="v101">
    <td class="ev-changelog__version"><strong>v1.0.1</strong><br><span>2026-03-29</span></td>
    <td>
      <p class="ev-changelog__type">Bug fixes</p>
      <ul>
        <li>Pin <code>numpy&lt;2</code> to avoid ABI mismatches on Colab and local installs</li>
      </ul>
      <p class="ev-changelog__type">Maintenance</p>
      <ul>
        <li>Relaxed Python and NumPy bounds; <code>pytest</code> pinned to 8.x</li>
      </ul>
    </td>
  </tr>
  <tr id="v100">
    <td class="ev-changelog__version"><strong>v1.0.0</strong><br><span>2026-03-28</span></td>
    <td>
      <ul>
        <li>Initial release</li>
      </ul>
    </td>
  </tr>
  </tbody>
</table>
