"""Build the website as plain static files in build/.

Render runs this on every push:  pip install -r requirements.txt && python build.py
Publish directory: build
"""

import shutil
from pathlib import Path

from app import app

ROOT = Path(__file__).parent
OUT = ROOT / "build"

NOT_FOUND_PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found | Star Industrial Gases</title>
<meta http-equiv="refresh" content="0; url=/">
</head><body><p>This page doesn't exist. <a href="/">Go to the Star Industrial Gases home page</a>.</p></body></html>
"""


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()

    client = app.test_client()
    for route, filename in [("/", "index.html"), ("/robots.txt", "robots.txt")]:
        response = client.get(route)
        if response.status_code != 200:
            raise SystemExit(f"Build failed: {route} returned {response.status_code}")
        (OUT / filename).write_bytes(response.data)

    (OUT / "404.html").write_text(NOT_FOUND_PAGE, encoding="utf-8")
    shutil.copytree(ROOT / "static", OUT / "static")

    files = sum(1 for p in OUT.rglob("*") if p.is_file())
    print(f"Built {files} files into {OUT}")


if __name__ == "__main__":
    main()
