"""Star Industrial Gases website.

The page is a Flask/Jinja template filled from content.py.
- `python app.py`   -> preview locally at http://localhost:5000
- `python build.py` -> render it to plain HTML in build/ (what Render publishes)
"""

import hashlib
from datetime import date
from pathlib import Path
from urllib.parse import quote

from flask import Flask, Response, redirect, render_template, url_for
from markupsafe import Markup, escape

import content

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 60 * 60 * 24 * 7  # cache static files for a week


def whatsapp_link(message: str) -> str:
    return f"https://wa.me/{content.BUSINESS['whatsapp']}?text={quote(message)}"


STATIC_DIR = Path(__file__).parent / "static"


def asset(filename: str) -> str:
    """URL for a file in static/, with a version tag so browsers fetch the new copy after a change."""
    path = STATIC_DIR / filename
    if not path.is_file():
        return url_for("static", filename=filename)
    version = hashlib.md5(path.read_bytes()).hexdigest()[:8]
    return url_for("static", filename=filename, v=version)


@app.template_filter("chem")
def chem(text: str) -> Markup:
    """Show chemical subscripts (CO₂, O₂, N₂) as <sub>2</sub> so they match the site font."""
    return Markup(str(escape(text)).replace("₂", "<sub>2</sub>"))


@app.context_processor
def inject_globals():
    return {
        "biz": content.BUSINESS,
        "year": date.today().year,
        "whatsapp_link": whatsapp_link,
        "asset": asset,
        "has_asset": lambda filename: (STATIC_DIR / filename).is_file(),
        "map_embed": "https://www.google.com/maps?output=embed&q=" + quote(content.BUSINESS["map_query"]),
        "map_link": "https://www.google.com/maps/search/?api=1&query=" + quote(content.BUSINESS["map_query"]),
    }


@app.route("/")
def home():
    return render_template(
        "index.html",
        products=content.PRODUCTS,
        industries=content.INDUSTRIES,
        reasons=content.REASONS,
        steps=content.ORDER_STEPS,
    )


@app.route("/robots.txt")
def robots():
    return Response("User-agent: *\nAllow: /\n", mimetype="text/plain")


@app.route("/healthz")
def health():
    return {"status": "ok"}


@app.errorhandler(404)
def not_found(_error):
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
