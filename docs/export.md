# Export

## Raster formats

Call `cvs.save()` with a `.png`, `.pdf`, or `.svg` extension:

```python
cvs.save("figure.png")   # PNG at the canvas DPI (default 300)
cvs.save("figure.pdf")   # PDF (vector, DPI ignored)
cvs.save("figure.svg")   # SVG (vector, DPI ignored)
```

The `dpi` parameter on `Canvas` controls raster resolution:

```python
cvs = Canvas(x_max=20, y_max=15, dpi=150)   # lower DPI for faster preview
```

DPI is clamped to the range 1–1200.

## Interactive window

Call `cvs.show()` to open a live matplotlib window instead of saving:

```python
cvs.show()
```

In the CLI, omit `--output` to get the same behaviour:

```bash
econ-viz plot --model cobb-douglas --px 2 --py 3 --income 30
```
