import http.server, json, socketserver, subprocess, time
from pathlib import Path
from datetime import datetime

BASE = Path.home()/ "Documents" / "TraceHQ"
SANDBOX = BASE / "sandbox"
PROJECTS = SANDBOX / "projects"
EXPORTS  = SANDBOX / "exports"
RUNNER   = BASE / "runner"
LOGS     = BASE / "logs"

for p in (SANDBOX, PROJECTS, EXPORTS, LOGS): p.mkdir(parents=True, exist_ok=True)

ALLOW = json.loads((RUNNER/"allowlist.json").read_text())

def log(msg: str):
    (LOGS/"trace_actions.log").open("a").write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}\n")

def within_sandbox(p: Path) -> bool:
    try:
        rp = p.resolve()
        return rp == SANDBOX or SANDBOX in rp.parents
    except Exception:
        return False

def ts(): return datetime.now().strftime("%Y%m%d-%H%M%S")

PREVIEW_PROC = None

def op_make_site(args):
    name = args.get("name","site")
    out = PROJECTS / f"{name}-{ts()}"
    out.mkdir(parents=True, exist_ok=True)
    assets = out / "assets"; assets.mkdir(exist_ok=True)
    (assets/"style.css").write_text(args.get("css","body{font-family:system-ui}"), encoding="utf-8")
    for fname, html in args.get("html", {}).items():
        (out/fname).write_text(html, encoding="utf-8")
    log(f"make_site -> {out}")
    return {"ok": True, "path": str(out)}

def op_preview_start(args):
    global PREVIEW_PROC
    folder = Path(args.get("folder","")).expanduser()
    if not within_sandbox(folder): return {"ok": False, "error": "outside sandbox"}

    # already running? keep it
    if PREVIEW_PROC and PREVIEW_PROC.poll() is None:
        return {"ok": True, "note": "already running", "url": "http://localhost:5500/"}

    PREVIEW_PROC = subprocess.Popen(
        ["python3","-m","http.server","5500"], cwd=str(folder),
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    log(f"preview_start -> {folder}")
    return {"ok": True, "url": "http://localhost:5500/"}

def op_preview_stop(args):
    global PREVIEW_PROC
    if PREVIEW_PROC and PREVIEW_PROC.poll() is None:
        PREVIEW_PROC.terminate()
        try: PREVIEW_PROC.wait(timeout=3)
        except Exception: PREVIEW_PROC.kill()
        log("preview_stop")
        return {"ok": True}
    return {"ok": True, "note": "not running"}

def op_zip_export(args):
    folder = Path(args.get("folder","")).expanduser()
    if not within_sandbox(folder): return {"ok": False, "error": "outside sandbox"}
    out = EXPORTS / f"{folder.name}.zip"
    subprocess.run(["/usr/bin/zip","-r",str(out),folder.name], cwd=str(folder.parent), check=True)
    log(f"zip_export -> {out}")
    return {"ok": True, "zip": str(out)}

OPS = {
  "make_site": op_make_site,
  "preview_start": op_preview_start,
  "preview_stop": op_preview_stop,
  "zip_export": op_zip_export
}

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length","0"))
        raw = self.rfile.read(length) if length else b"{}"
        try: data = json.loads(raw)
        except Exception: return self._send(400, {"ok": False, "error": "bad json"})
        op = data.get("op")
        if not ALLOW.get(op): return self._send(403, {"ok": False, "error": "op not allowed"})
        try:
            res = OPS[op](data.get("args",{}))
            return self._send(200, res)
        except Exception as e:
            log(f"ERROR {op}: {e}")
            return self._send(500, {"ok": False, "error": str(e)})

    def _send(self, code, obj):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type","application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    with socketserver.TCPServer(("127.0.0.1", 8765), Handler) as httpd:
        log("runner listening on 127.0.0.1:8765")
        httpd.serve_forever()

