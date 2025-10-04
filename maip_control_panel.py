cd ~/Documents/webbySites/c-d-lawn-service
mkdir -p assets gallery mp4 video

cat > assets/style.css <<'CSS'
:root{--brand:#136d2a;--accent:#0fb86b;--ink:#0f172a;--muted:#475569;--bg:#f6f7fb;--btn:#b31818}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;font-family:system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--ink)}
a{text-decoration:none;color:inherit}
.container{max-width:1200px;margin:0 auto;padding:0 24px}
.page{min-height:100vh;display:flex;flex-direction:column}
.nav{background:#fff;border-bottom:1px solid #e5e7eb;position:sticky;top:0;z-index:40}
.nav .wrap{height:88px;display:flex;align-items:center;justify-content:space-between}
.logo{display:flex;align-items:center;gap:14px}
.logo img{height:54px}
.logo strong{font-size:20px;letter-spacing:.02em}
.nav a{margin:0 14px;font-weight:700;letter-spacing:.06em}
.nav a:hover{color:var(--brand)}
.hero{position:relative;color:#fff;background:
 linear-gradient(180deg,rgba(0,0,0,.45),rgba(0,0,0,.25) 45%,rgba(0,0,0,.35)),
 url('../gallery/hero.jpg') center/cover no-repeat, linear-gradient(135deg,var(--brand),var(--accent))}
.hero .inner{min-height:520px;display:flex;align-items:center}
.hero .title{font-size:76px;line-height:1;letter-spacing:.02em;text-shadow:0 12px 42px rgba(0,0,0,.55)}
.hero .subtitle{font-size:22px;margin-top:10px;opacity:.95}
.cta{margin-top:24px;background:var(--btn);color:#fff;padding:14px 26px;border-radius:12px;font-weight:800;display:inline-block}
main{flex:1;padding:48px 0}
.grid{display:grid;grid-template-columns:repeat(12,1fr);gap:28px}
.col-7{grid-column:span 7}.col-5{grid-column:span 5}
.card{background:#fff;border:1px solid #e5e7eb;border-radius:18px;box-shadow:0 10px 36px rgba(2,8,23,.06);padding:22px}
.lead{color:var(--muted);font-size:18px}
.section-title{font-size:34px;margin:0 0 12px}
.services{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}
.service{background:#fff;border:1px solid #e5e7eb;border-radius:16px;overflow:hidden;box-shadow:0 8px 28px rgba(2,8,23,.06)}
.service img{width:100%;height:170px;object-fit:cover}
.service .body{padding:16px}
.service h3{margin:0 0 6px}
.strip{background:#0b1220;color:#cbd5e1}
.strip .wrap{padding:20px 0;display:flex;gap:24px;justify-content:center;flex-wrap:wrap;font-weight:600}
.gallery-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}
.gallery-grid img{width:100%;height:180px;object-fit:cover;border-radius:12px}
.video-card{background:#fff;border:1px solid #e5e7eb;border-radius:14px;overflow:hidden}
.video-card h4{margin:10px 12px}
.footer{background:#0f172a;color:#cbd5e1;margin-top:48px}
.footer .wrap{height:76px;display:flex;align-items:center;justify-content:space-between;gap:16px}
@media(max-width:980px){
 .col-7,.col-5{grid-column:span 12}
 .services{grid-template-columns:1fr}
 .hero .title{font-size:48px}
 .hero .inner{min-height:420px}
}
CSS

cat > index.html <<'HTML'
<!doctype html><html><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>C&D Lawn Service — Lexington, SC</title>
<link rel="stylesheet" href="assets/style.css">
</head><body><div class="page">
<div class="nav"><div class="container wrap">
  <div class="logo"><img src="assets/logo.svg" alt=""><strong>C&D Lawn Service</strong></div>
  <div><a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="services.html">SERVICES</a><a href="work.html">RECENT WORK</a><a href="videos.html">VIDEOS</a><a href="contact.html">CONTACT</a></div>
</div></div>
<header class="hero"><div class="container inner">
  <div>
    <div class="title">C&amp;D</div>
    <div class="title">LAWN SERVICE</div>
    <div class="subtitle">Mowing • Edging • Cleanup — Lexington, South Carolina</div>
    <a class="cta" href="contact.html">Get a Quote</a>
  </div>
</div></header>
<main><div class="container">
  <div class="grid">
    <div class="col-7">
      <h2 class="section-title">About Us</h2>
      <div class="card lead">
        Howdy! I’m Chris Hall, owner of C&amp;D Lawn Service. Born and raised right here in Lexington, South Carolina, I grew up with a passion for turning an ordinary yard into something special. After years of mowing for family and friends I decided to make it official—and C&amp;D Lawn Service was born. Today we’re proud to be a local, family-run business built on honest work, southern hospitality and a genuine love for a well-cut lawn.<br><br>
        Every yard we maintain is treated as if it were our own. Whether you’re a busy homeowner who just needs a reliable mow every week, or a property manager looking for full-service maintenance, we’ve got you covered. We believe in showing up on time, doing the job right the first time and leaving your yard looking clean, green and welcoming. When you hire us you’re getting personal service directly from me and my team—not a faceless corporation. Give us a call and see why your neighbors trust C&amp;D Lawn Service for all their lawn care needs.
      </div>
    </div>
    <div class="col-5">
      <h2 class="section-title">Services</h2>
      <div class="services">
        <div class="service"><img src="assets/service1.jpg" alt=""><div class="body"><h3>Mowing & Trimming</h3><p>Crisp edges, clean lines, and a healthy, even cut.</p></div></div>
        <div class="service"><img src="assets/service2.jpg" alt=""><div class="body"><h3>Seasonal Cleanup</h3><p>Leaves, limbs, and debris hauled away—no hassle.</p></div></div>
        <div class="service"><img src="assets/service3.jpg" alt=""><div class="body"><h3>Mulch & Pine Straw</h3><p>Fresh beds that make the whole property pop.</p></div></div>
      </div>
    </div>
  </div>
</div></main>
<div class="strip"><div class="container wrap">
  <div>Licensed & Insured</div><div>Local, Family-Run</div><div>On-Time, Every Time</div><div>Serving Lexington, SC</div>
</div></div>
<div class="footer"><div class="container wrap"><div>© 2025 C&D Lawn Service</div><div><a href="tel:+18033610657">(803) 361-0657</a> • <a href="mailto:arkanstar2@gmail.com">arkanstar2@gmail.com</a></div></div></div>
</div></body></html>
HTML

cat > about.html <<'HTML'
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>About — C&D Lawn Service</title><link rel="stylesheet" href="assets/style.css"></head>
<body><div class="page">
<div class="nav"><div class="container wrap"><div class="logo"><img src="assets/logo.svg"><strong>C&D Lawn Service</strong></div><div><a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="services.html">SERVICES</a><a href="work.html">RECENT WORK</a><a href="videos.html">VIDEOS</a><a href="contact.html">CONTACT</a></div></div></div>
<main><div class="container">
  <h1 class="section-title">Our Story</h1>
  <div class="card lead">Howdy! I’m Chris Hall, owner of C&amp;D Lawn Service… (same copy as Home)</div>
</div></main>
<div class="footer"><div class="container wrap">© 2025 C&D Lawn Service</div></div>
</div></body></html>
HTML

cat > services.html <<'HTML'
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Services — C&D Lawn Service</title><link rel="stylesheet" href="assets/style.css"></head>
<body><div class="page">
<div class="nav"><div class="container wrap"><div class="logo"><img src="assets/logo.svg"><strong>C&D Lawn Service</strong></div><div><a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="services.html">SERVICES</a><a href="work.html">RECENT WORK</a><a href="videos.html">VIDEOS</a><a href="contact.html">CONTACT</a></div></div></div>
<main><div class="container">
  <h1 class="section-title">What We Do</h1>
  <div class="services">
    <div class="service"><img src="assets/service1.jpg"><div class="body"><h3>Mowing & Trimming</h3><p>Weekly/bi-weekly programs, precision edging, bed touch-ups.</p></div></div>
    <div class="service"><img src="assets/service2.jpg"><div class="body"><h3>Seasonal Cleanup</h3><p>Fall leaf removal, spring refresh, storm debris.</p></div></div>
    <div class="service"><img src="assets/service3.jpg"><div class="body"><h3>Mulch & Pine Straw</h3><p>Delivery and install; crisp borders and fresh color.</p></div></div>
  </div>
</div></main>
<div class="footer"><div class="container wrap">© 2025 C&D Lawn Service</div></div>
</div></body></html>
HTML

cat > work.html <<'HTML'
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Recent Work — C&D Lawn Service</title><link rel="stylesheet" href="assets/style.css"></head>
<body><div class="page">
<div class="nav"><div class="container wrap"><div class="logo"><img src="assets/logo.svg"><strong>C&D Lawn Service</strong></div><div><a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="services.html">SERVICES</a><a href="work.html">RECENT WORK</a><a href="videos.html">VIDEOS</a><a href="contact.html">CONTACT</a></div></div></div>
<main><div class="container">
  <h1 class="section-title">Recent Work</h1>
  <div class="gallery-grid">
    <!-- images auto-populated by copying your gallery/ pics here -->
  </div>
</div></main>
<div class="footer"><div class="container wrap">© 2025 C&D Lawn Service</div></div>
</div></body></html>
HTML

cat > videos.html <<'HTML'
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Videos — C&D Lawn Service</title><link rel="stylesheet" href="assets/style.css"></head>
<body><div class="page">
<div class="nav"><div class="container wrap"><div class="logo"><img src="assets/logo.svg"><strong>C&D Lawn Service</strong></div><div><a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="services.html">SERVICES</a><a href="work.html">RECENT WORK</a><a href="videos.html">VIDEOS</a><a href="contact.html">CONTACT</a></div></div></div>
<main><div class="container">
  <h1 class="section-title">Videos</h1>
  <div id="videos"></div>
</div></main>
<div class="footer"><div class="container wrap">© 2025 C&D Lawn Service</div></div>
<script>
const holder=document.getElementById('videos');
const files=[].concat(
  Array.from([]) // placeholder; list populated by build step if needed
);
</script>
</div></body></html>
HTML

cat > contact.html <<'HTML'
<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Contact — C&D Lawn Service</title><link rel="stylesheet" href="assets/style.css"></head>
<body><div class="page">
<div class="nav"><div class="container wrap"><div class="logo"><img src="assets/logo.svg"><strong>C&D Lawn Service</strong></div><div><a href="index.html">HOME</a><a href="about.html">ABOUT</a><a href="services.html">SERVICES</a><a href="work.html">RECENT WORK</a><a href="videos.html">VIDEOS</a><a href="contact.html">CONTACT</a></div></div></div>
<main><div class="container">
  <h1 class="section-title">Contact</h1>
  <div class="card">
    <form action="https://formsubmit.co/arkanstar2@gmail.com" method="POST">
      <input type="hidden" name="_subject" value="Lead — C&D Lawn Service">
      <input type="hidden" name="_captcha" value="false">
      <div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px">
        <div><label>Name<br><input name="name" required style="width:100%;padding:12px;border:1px solid #e5e7eb;border-radius:10px"></label></div>
        <div><label>Phone<br><input name="phone" style="width:100%;padding:12px;border:1px solid #e5e7eb;border-radius:10px"></label></div>
      </div>
      <div style="margin-top:12px"><label>Email<br><input type="email" name="email" required style="width:100%;padding:12px;border:1px solid #e5e7eb;border-radius:10px"></label></div>
      <div style="margin-top:12px"><label>Message<br><textarea name="message" rows="6" required style="width:100%;padding:12px;border:1px solid #e5e7eb;border-radius:10px"></textarea></label></div>
      <div style="margin-top:16px"><button class="cta" type="submit">Send Message</button></div>
    </form>
  </div>
  <p style="margin-top:18px">Or call/text <a href="tel:+18033610657">(803) 361-0657</a> • <a href="mailto:arkanstar2@gmail.com">arkanstar2@gmail.com</a></p>
</div></main>
<div class="footer"><div class="container wrap">© 2025 C&D Lawn Service</div></div>
</div></body></html>
HTML

i=0; for f in gallery/*.{jpg,jpeg,png,webp,JPG,JPEG,PNG,WEBP}; do cp "$f" "assets/service$((++i)).jpg"; [ $i -ge 3 ] && break; done 2>/dev/null || true
python3 - <<'PY'
from pathlib import Path, PurePosixPath
base=Path.home()/ "Documents" / "webbySites" / "c-d-lawn-service"
g=base/"gallery"; w=base/"work.html"
imgs=[f"<img src='gallery/{PurePosixPath(p).name}' alt=''>" for p in g.iterdir() if p.suffix.lower() in {'.jpg','.jpeg','.png','.webp','.svg'}]
if imgs:
    txt=w.read_text(encoding='utf-8')
    txt=txt.replace("<!-- images auto-populated by copying your gallery/ pics here -->","\n".join(imgs))
    w.write_text(txt,encoding='utf-8')
vlist=[]
for folder in ["mp4","video"]:
    d=base/folder
    if d.exists():
        for p in d.iterdir():
            if p.suffix.lower() in {'.mp4','.mov','.webm'}:
                title=p.stem.replace('_',' ').title()
                vlist.append((folder+'/'+p.name,title))
vs=base/"videos.html"
if vlist:
    items=[]
    for path,title in vlist:
        items.append(f"<div class='video-card'><video src='{path}' controls style='width:100%;height:320px;display:block;background:#000'></video><h4>{title}</h4></div>")
    block="<div class='grid' style='grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:18px'>"+ "".join(items)+"</div>"
    s=vs.read_text(encoding='utf-8').replace("<div id=\"videos\"></div>",block)
    vs.write_text(s,encoding='utf-8')
PY

