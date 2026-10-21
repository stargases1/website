# Star Industrial Gases — website

Single-page website for Star Industrial Gases, Kota (oxygen, CO₂, nitrogen and argon cylinders).

- **Frontend:** HTML, CSS, JavaScript (`templates/`, `static/`)
- **Backend / build:** Python + Flask templates (`app.py`, `build.py`) render the page to static HTML
- **Hosting:** Render Static Site (`render.yaml`)

## Edit the content

All text, phone numbers, products, purity and cylinder sizes are in **`content.py`**.
Lines marked `# CONFIRM` are placeholders that should be checked before launch.
Commit and push the change; Render redeploys automatically.

## Run locally

```bash
pip install -r requirements.txt
python app.py        # live preview at http://localhost:5000
python build.py      # builds the final static site into build/
```

## Hero photo

Save a landscape photo (at least 1920px wide, under ~400 KB) as `static/img/hero.jpg`.
It appears behind the hero text automatically; without it the hero is plain navy.

## Project layout

```
app.py              Flask app (page template, WhatsApp links, map link)
build.py            Renders the site to static HTML in build/
content.py          All website content — edit this
templates/index.html  The page
static/css/style.css  Styles
static/js/main.js     Mobile menu
static/img/           Logo, favicon
static/fonts/         Archivo (self-hosted, SIL Open Font License)
render.yaml         Render settings
requirements.txt    Python packages
```

## Deploy on Render (Static Site — free, never sleeps)

1. Push this folder to GitHub (`stargases1/website`).
2. In Render: **New → Static Site** → connect the repo.
3. Settings:
   - Branch: `main`
   - Build command: `pip install -r requirements.txt && python build.py`
   - Publish directory: `build`
4. Optional, under **Headers**: path `/static/*`, name `Cache-Control`, value `public, max-age=604800`.
   (Or use **New → Blueprint**, which reads all of this from `render.yaml`.)
5. Every push to `main` rebuilds and redeploys the site.

## Connect your domain

1. In Render, open the service → **Settings → Custom Domains → Add**.
   Add both `yourdomain.com` and `www.yourdomain.com`.
2. At your domain registrar (GoDaddy, Hostinger, etc.), add the DNS records Render shows:
   - `www` → **CNAME** → `<static-site-name>.onrender.com`
   - root `@` → **A** record → `216.24.57.1`
   - delete any **AAAA** records and turn off GoDaddy domain forwarding
3. Wait for DNS to update (minutes to a few hours). Render issues the HTTPS certificate automatically.
