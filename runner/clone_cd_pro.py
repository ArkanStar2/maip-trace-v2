# Clone your full cd-lawn-pro folder into Trace sandbox and keep a timestamped copy
import os, shutil, time
from pathlib import Path

SRC = Path.home() / "Documents" / "webbySites" / "cd-lawn-pro"
DEST_BASE = Path.home() / "Documents" / "TraceHQ" / "sandbox" / "projects"
DEST = DEST_BASE / f"cd-lawn-pro-{time.strftime('%Y%m%d-%H%M%S')}"

if not SRC.exists():
    raise SystemExit(f"Source not found: {SRC}")

DEST_BASE.mkdir(parents=True, exist_ok=True)

def ignore_junk(path, names):
    junk = {".DS_Store", "Thumbs.db", "__pycache__"}
    return [n for n in names if n in junk]

shutil.copytree(SRC, DEST, ignore=ignore_junk)
print("Cloned to:", DEST)

