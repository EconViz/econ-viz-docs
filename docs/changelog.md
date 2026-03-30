# Changelog

This page mirrors the project's release history from `CHANGELOG.md`.

## v1.1.0 (2026-03-30)

### Features

- Add `comparative_statics` helper (closes #12)
- Add `HomogeneityAnalyzer` and `ReturnsToScale` to the analysis submodule (closes #14)
- Add `Translog` model (#9) and legend / indifference-curve label support (#11)

## v1.0.2 (2026-03-29)

### Bug fixes

- Prevent double-wrap of math axis labels (closes #2)
- Remove NumPy upper bound to prevent Colab environment conflicts

## v1.0.1 (2026-03-29)

### Bug fixes

- Pin `numpy<2` to prevent ABI mismatch on Colab and local installs

### Chores

- Relax Python / NumPy bounds and pin `pytest` to 8.x

### Documentation

- Add Stone-Geary to README and update the test-count badge

## v1.0.0 (2026-03-28)

- Initial release
