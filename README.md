# Star Industrial Gases — website

Single-page website for Star Industrial Gases, Kota (oxygen, CO₂, nitrogen and argon cylinders).

- **Frontend:** HTML, CSS, JavaScript (`templates/`, `static/`)
- **Backend:** Python / Flask (`app.py`), served by Gunicorn
- **Hosting:** Render (`render.yaml`)

## Edit the content

All text, phone numbers, products, purity and cylinder sizes are in **`content.py`**.
Lines marked `# CONFIRM` are placeholders that should be checked before launch.
Commit and push the change; Render redeploys automatically.

## Run locally

```bash
pip install -r requirements.txt
python app.py
# open http://localhost:5000
```

## Project layout

```
app.py              Flask app (routes, WhatsApp links, map link)
content.py          All website content — edit this
templates/index.html  The page
static/css/style.css  Styles
static/js/main.js     Mobile menu
static/img/           Logo, favicon
static/fonts/         Archivo (self-hosted, SIL Open Font License)
render.yaml         Render settings
requirements.txt    Python packages
```

## Deploy on Render

1. Push this folder to a GitHub repository.
2. In Render: **New → Web Service** → connect the GitHub repo.
3. Render reads `render.yaml`. If you fill the fields by hand instead:
   - Runtime: **Python 3**
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn app:app`
   - Health check path: `/healthz`
4. Click **Deploy**. The site will be live at `https://<service-name>.onrender.com`.

Note: on Render's free plan the site sleeps after ~15 minutes without visitors, and the
first visit after that takes 30–60 seconds to load. The Starter plan keeps it always on.

## Connect your domain

1. In Render, open the service → **Settings → Custom Domains → Add**.
   Add both `yourdomain.com` and `www.yourdomain.com`.
2. At your domain registrar (GoDaddy, Hostinger, etc.), add the DNS records Render shows:
   - `www` → **CNAME** → `<service-name>.onrender.com`
   - root `@` → **A** record → the IP address Render shows (or ALIAS/ANAME if your registrar supports it)
3. Wait for DNS to update (minutes to a few hours). Render issues the HTTPS certificate automatically.
