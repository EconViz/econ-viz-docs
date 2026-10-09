# API references

Place a standalone directive in a Markdown page:

```markdown
<!-- api: canvas.add_budget -->
```

`hooks/api_reference.py` renders the shared grayscale signature and parameter
details at build time. `docs/stylesheets/api-reference.css` controls presentation.
Examples, diagrams, and explanatory prose remain in the original Markdown pages.

JSON files contain a symbol mapping. Each entry has `name`, `anchor`, `returns`,
and ordered `parameters`. A parameter has `name`, `types` (union alternatives),
and `description` with `en`, `zh-TW`, and `zh-CN` Markdown strings. Omit `default`
for required parameters; use the **string** `"None"` for a Python None default.
Set `keyword_only: true` for keyword-only parameters. Keep names and defaults
as Python syntax, even in translated pages.

Function links use `#api-{anchor}`; parameter links use `#{anchor}-{name}`
(without leading asterisks). Existing page headings keep their original anchors.
Do not change anchors when changing prose or a translated heading. Place each
symbol only once per page to keep IDs unique.

The current definitions were checked against the local utility-viz and bezierkit
source signatures. They are versioned snapshots, not build-time imports. When
updating a package, update its shared signature and all three descriptions here.
The Canvas constructor retains the documented selection of public options.
Use a standalone API reference for signatures; executable tutorials stay in
ordinary Python code fences.

Validate with `uv run --frozen python -m unittest discover -s tests` and
`uv run --frozen mkdocs build`.
