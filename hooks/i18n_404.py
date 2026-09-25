"""Keep the site-wide 404 page in English.

mkdocs-static-i18n builds each language into the same site directory, so the
root 404.html is overwritten by whichever language is built last. GitHub Pages
serves that single file for every missing URL, so keep the English version.
"""

import shutil
from pathlib import Path

_BACKUP_NAME = ".404.en.html"


def on_post_build(config, **kwargs):
    site_dir = Path(config.site_dir)
    page = site_dir / "404.html"
    backup = site_dir / _BACKUP_NAME
    if config.theme["language"] == "en":
        if page.exists():
            shutil.copyfile(page, backup)
    elif backup.exists():
        shutil.copyfile(backup, page)
