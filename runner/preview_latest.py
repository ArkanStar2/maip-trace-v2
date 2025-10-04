import os, glob, requests

base = os.path.expanduser("~/Documents/TraceHQ/sandbox/projects")
paths = sorted(glob.glob(base + "/*"))
if not paths:
    print("No projects found in", base)
    raise SystemExit(1)

latest = paths[-1]
print("Previewing:", latest)
res = requests.post(
    "http://127.0.0.1:8765",
    json={"op": "preview_start", "args": {"folder": latest}}
)
print(res.json())

