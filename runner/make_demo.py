import os, pathlib

base = os.path.expanduser("~/Documents/TraceHQ/sandbox/projects")
pathlib.Path(base).mkdir(parents=True, exist_ok=True)

demo = os.path.join(base, "trace-demo")
pathlib.Path(demo).mkdir(parents=True, exist_ok=True)

with open(os.path.join(demo, "index.html"), "w") as f:
    f.write("<h1>Hello from Trace Sandbox</h1><p>Sandbox OK.</p>")

with open(os.path.join(demo, "about.html"), "w") as f:
    f.write("<p>About Trace: safe & sandboxed.</p>")

with open(os.path.join(demo, "contact.html"), "w") as f:
    f.write("<p>(803) 361-0657</p>")

print("Demo site created at:", demo)

