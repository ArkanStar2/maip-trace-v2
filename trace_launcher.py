# trace_launcher.py — Step 1: start Trace HQ + minimal Control Panel
import sys, subprocess, time, webbrowser, os
from pathlib import Path

BASE = Path.home() / "Documents" / "TraceHQ"
PANEL = BASE / "maip_control_panel.py"
TRACE = BASE / "trace.csv"

PANEL_CODE = r"""
import csv, time, subprocess, sys
from pathlib import Path
import streamlit as st

BASE = Path.home() / "Documents" / "TraceHQ"
TRACE = BASE / "trace.csv"
BASE.mkdir(parents=True, exist_ok=True)

def log(event:str, status:str, extra:str=""):
    new = not TRACE.exists()
    with open(TRACE, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if new: w.writerow(["ts","event","status","extra"])
        w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), event, status, extra])

st.set_page_config(page_title="MAIP Control Panel — Minimal", page_icon="🚦", layout="centered")
st.title("🚦 MAIP Control Panel — Minimal")

tab1, tab2, tab3, tab4 = st.tabs(["Projects", "Build", "Trace Log", "Settings"])

with tab1:
    st.subheader("Project (no editing needed)")
    project_name = st.text_input("Business / Project Name", value="C&D Lawn Service")
    images_folder = st.text_input("Images folder (with hero.jpg, logo.svg, etc.)",
                                  value=str(Path.home()/ "Documents" / "webbySites" / "c-d-lawn-service" / "images"))
    output_folder = st.text_input("Output folder",
                                  value=str(Path.home()/ "Documents" / "webbySites" / "c-d-lawn-service"))
    if st.button("Record Project"):
        log("project_recorded", "ok", f"name={project_name} images={images_folder} out={output_folder}")
        st.success("Saved to Trace log. (Build button will arrive next step.)")

with tab2:
    st.subheader("Preview (serve a folder locally)")
    site_dir = st.text_input("Folder to preview", value=str(Path.home()/ "Documents" / "webbySites" / "c-d-lawn-service"))
    if st.button("Open Preview at http://localhost:5500/"):
        p = Path(site_dir)
        if p.exists():
            subprocess.Popen([sys.executable, "-m", "http.server", "5500"], cwd=str(p))
            time.sleep(0.7)
            import webbrowser; webbrowser.open("http://localhost:5500/")
            log("preview_opened", "ok", f"dir={site_dir}")
            st.info("Preview opened. If a tab didn’t pop up, open http://localhost:5500/ manually.")
        else:
            log("preview_opened", "error", f"missing={site_dir}")
            st.error("That folder doesn’t exist. Update the path and try again.")

with tab3:
    st.subheader("Trace Log")
    if TRACE.exists():
        st.code(TRACE.read_text(encoding="utf-8"))
    else:
        st.info("No runs logged yet.")

with tab4:
    st.subheader("Settings")
    st.write(f"Trace base folder: {BASE}")
    st.write(f"Trace log file: {TRACE}")
    st.caption("Next steps will add Build buttons (Webby), Twilio, and one-click Publish.")
"""

def ensure_panel():
    BASE.mkdir(parents=True, exist_ok=True)
    if not PANEL.exists():
        PANEL.write_text(PANEL_CODE, encoding="utf-8")
        print(f"[Trace] Wrote minimal Control Panel → {PANEL}")

def ensure_streamlit():
    try:
        import streamlit  # noqa: F401
        return
    except Exception:
        print("[Trace] Installing Streamlit (first run)…")
        subprocess.run([sys.executable, "-m", "pip", "install", "streamlit"], check=True)

def run_panel():
    print("[Trace] Launching Control Panel…")
    proc = subprocess.Popen([sys.executable, "-m", "streamlit", "run", str(PANEL)], cwd=str(BASE))
    time.sleep(1.0)
    try:
        webbrowser.open("http://localhost:8501/")
    except Exception:
        pass
    print("[Trace] Panel should be at http://localhost:8501/")
    return proc

if __name__ == "__main__":
    ensure_panel()
    ensure_streamlit()
    run_panel()
    print("[Trace] Running. Close this window or Ctrl+C to stop.")

