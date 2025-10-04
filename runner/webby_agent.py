# Webby Agent — writes a full static site into Trace sandbox
import os, shutil, time
from pathlib import Path
from datetime import datetime

BASE = Path.home() / "Documents" / "TraceHQ"
SANDBOX = BASE / "sandbox"
PROJECTS = SANDBOX / "projects"

def ts():
    return datetime.now().strftime("%Y%m%d-%H%M%S")

def safe_copy(src, dst):
    try:
        if src and Path(src).exists():
            shutil.copy2(src, dst)
            return True
    except Exception:
        pass
    return False

def build_site(cfg: dict):
    name = cfg.get("name","site")
    images_src = Path(cfg.get("images_src","")).expanduser()
    out = PROJECTS / f"{name}-{ts()}"
    assets = out / "assets"
    gallery = out / "gallery"
    out.mkdir(parents=True, exist_ok=True); assets.mkdir(exist_ok=True); gallery.mkdir(exist_ok=True)

    # Try to bring over logo/hero if present
    logo_ok = safe_copy(images_src/"logo.svg", assets/"logo.svg") or \
              safe_copy(images_src/"logo.png", assets/"logo.png")
    hero_ok = safe_copy(images_src/"hero.jpg", out/"hero.jpg") or \
              safe_copy(images_src/"hero.png", out/"hero.png") or \
              safe_copy(images_src/"hero.jpeg", out/"hero.jpeg")

    # Basic CSS (clean, readable)
    (assets/"style.css").write_text(f"""
:root {{
  --brand:#0a7f3f; --dark:#0c1220; --txt:#222; --muted:#6b7280; --card:#fff; --bg:#f7f8fb;
}}
*{{box-sizing:border-box}}
html,body{{margin:0;padding:0;font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Inter, system-ui; color:var(--txt); background:var(--bg)}}
a{{color:inherit;text-decoration:none}}
.container{{max-width:1100px;margin:0 auto;padding:24px}}
.nav{{position:sticky;top:0;background:#fff;border-bottom:1px solid #e5e7eb;z-index:10}}
.nav-inner{{display:flex;align-items:center;gap:24px}}
.brand{{display:flex;align-items:center;gap:12px;font-weight:800}}
.brand img{{height:32px}}
nav a{{margin-right:18px;color:#374151;font-weight:600}}
nav a:hover{{color:var(--brand)}}
.hero{{position:relative;min-height:70vh;display:flex;align-items:center;justify-content:center;overflow:hidden;background:linear-gradient(135deg,#0aa34f,#12b76a)}}
.hero img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:brightness(0.65)}}
.hero .overlay{{position:relative;color:#fff;text-align:center;padding:32px}}
.hero h1{{font-size: clamp(36px,6vw,56px);margin:0 0 8px 0;letter-spacing:.5px}}
.hero p.tag{{opacity:.9;font-weight:600;margin:0 0 20px 0}}
.btn{{display:inline-block;background:#b91c1c;color:#fff;padding:14px 22px;border-radius:10px;font-weight:800}}
.section{{padding:48px 0}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:18px}}
.card{{background:var(--card);border-radius:14px;padding:22px;box-shadow:0 6px 20px rgba(16,24,40,.06)}}
.card h3{{margin:0 0 8px}}
.footer{{background:var(--dark);color:#ccd3ea;padding:22px 0;font-size:14px}}
.small{{color:var(--muted)}}
    """.strip(), encoding="utf-8")

    # Common header/footer
    brand_img = '<img src="assets/logo.svg" alt="logo">' if logo_ok else ''
    nav = f"""
<div class="nav"><div class="container nav-inner">
  <div class="brand">{brand_img}<span>{cfg['name']}</span></div>
  <nav>
    <a href="index.html">Home</a>
    <a href="about.html">About</a>
    <a href="services.html">Services</a>
    <a href="work.html">Recent Work</a>
    <a href="videos.html">Videos</a>
    <a href="contact.html">Contact</a>
  </nav>
</div></div>
"""
    footer = f"""
<div class="footer"><div class="container">
  © {time.strftime('%Y')} {cfg['name']}. All rights reserved.
</div></div>
"""

    # Hero image element if available
    hero_img_tag = ""
    for fn in ("hero.jpg","hero.png","hero.jpeg"):
        if (out/fn).exists():
            hero_img_tag = f'<img src="{fn}" alt="hero">'
            break

    # Pages
    index_html = f"""<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="assets/style.css"><title>{cfg['name']}</title></head><body>
{nav}
<header class="hero">{hero_img_tag}
  <div class="overlay">
    <h1>{cfg['headline']}</h1>
    <p class="tag">{cfg['tagline']}</p>
    <a class="btn" href="contact.html">Get a Quote</a>
  </div>
</header>
<section class="section"><div class="container">
  <div class="grid">
    <div class="card"><h3>Mowing & Edging</h3><p>Clean cuts, sharp edges, tidy beds.</p></div>
    <div class="card"><h3>Hedge Shaping</h3><p>Pruning for healthy, neat growth.</p></div>
    <div class="card"><h3>Mulch & Bed Refresh</h3><p>Weeds out, beds fresh, plants pop.</p></div>
  </div>
</div></section>
{footer}
</body></html>"""

    about_html = f"""<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="assets/style.css"><title>About — {cfg['name']}</title></head><body>
{nav}
<section class="section"><div class="container">
  <h1>About Us</h1>
  <p class="small">{cfg['about']}</p>
</div></section>
{footer}
</body></html>"""

    services_cards = "".join(
        f'<div class="card"><h3>{s["title"]}</h3><p>{s["desc"]}</p></div>'
        for s in cfg["services"]
    )
    services_html = f"""<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="assets/style.css"><title>Services — {cfg['name']}</title></head><body>
{nav}
<section class="section"><div class="container"><h1>Services</h1>
  <div class="grid">{services_cards}</div>
</div></section>
{footer}
</body></html>"""

    work_html = f"""<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="assets/style.css"><title>Recent Work — {cfg['name']}</title></head><body>
{nav}
<section class="section"><div class="container"><h1>Recent Work</h1>
  <p class="small">Add photos to the <code>gallery/</code> folder. They’ll show here in the next version.</p>
</div></section>
{footer}
</body></html>"""

    videos_html = f"""<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="assets/style.css"><title>Videos — {cfg['name']}</title></head><body>
{nav}
<section class="section"><div class="container"><h1>Videos</h1>
  <p class="small">Drop processed MP4s beside this page; we’ll auto-embed in the next version.</p>
</div></section>
{footer}
</body></html>"""

    contact_html = f"""<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="assets/style.css"><title>Contact — {cfg['name']}</title></head><body>
{nav}
<section class="section"><div class="container"><h1>Contact</h1>
  <div class="grid">
    <div class="card"><h3>Phone</h3><p><a href="tel:{cfg['phone']}">{cfg['phone']}</a></p></div>
    <div class="card"><h3>Email</h3><p><a href="mailto:{cfg['email']}">{cfg['email']}</a></p></div>
    <div class="card"><h3>Service Area</h3><p>{cfg['city']}, {cfg['state']}</p></div>
  </div>
</div></section>
{footer}
</body></html>"""

    (out/"index.html").write_text(index_html, encoding="utf-8")
    (out/"about.html").write_text(about_html, encoding="utf-8")
    (out/"services.html").write_text(services_html, encoding="utf-8")
    (out/"work.html").write_text(work_html, encoding="utf-8")
    (out/"videos.html").write_text(videos_html, encoding="utf-8")
    (out/"contact.html").write_text(contact_html, encoding="utf-8")

    return str(out)

if __name__ == "__main__":
    # Manual test (not used when called by Trace runner)
    demo_cfg = dict(
        name="Demo Site",
        images_src="",
        headline="Demo Headline",
        tagline="Tagline goes here",
        phone="(803) 361-0657",
        email="info@example.com",
        city="Lexington",
        state="SC",
        about="We care for every yard like it’s our own.",
        services=[
          {"title":"Mowing & Edging","desc":"Clean cuts, sharp edges, tidy beds."},
          {"title":"Hedge Shaping","desc":"Pruning for healthy, neat growth."},
          {"title":"Mulch & Bed Refresh","desc":"Weeds out, beds fresh, plants pop."},
          {"title":"Tree Limb Trim (Low)","desc":"Low limbs removed, debris hauled."},
          {"title":"Leaf & Debris Cleanup","desc":"Seasonal cleanups; spotless yards."},
          {"title":"Commercial Maintenance","desc":"Storefronts clean and welcoming."}
        ]
    )
    path = build_site(demo_cfg)
    print("Built:", path)

