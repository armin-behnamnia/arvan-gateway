"""Render the results dashboard to PDF with headless Edge.

Mirrors the invocation in tools/md2pdf.py, which is the one known to work on
this machine -- `--headless=new` and no invented flags. Web fonts need a moment
to load before printing, hence the virtual time budget.

    python html2pdf.py report.html report.pdf
"""
from __future__ import annotations

import os
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent

EDGE_CANDIDATES = (
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
)


def find_edge() -> str:
    for path in EDGE_CANDIDATES:
        if os.path.exists(path):
            return path
    raise SystemExit("Edge not found; edit EDGE_CANDIDATES")


def convert(html_path: pathlib.Path, pdf_path: pathlib.Path) -> bool:
    if pdf_path.exists():
        pdf_path.unlink()

    subprocess.run(
        [
            find_edge(),
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--virtual-time-budget=30000",
            f"--print-to-pdf={pdf_path}",
            "file:///" + str(html_path).replace("\\", "/"),
        ],
        capture_output=True,
        text=True,
        timeout=180,
    )

    ok = pdf_path.exists() and pdf_path.stat().st_size > 10000
    size = pdf_path.stat().st_size / 1024 if pdf_path.exists() else 0
    print(f"{'OK  ' if ok else 'FAIL'} {pdf_path}  ({size:,.0f} KB)")
    return ok


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("usage: python html2pdf.py report.html report.pdf")
    source, target = (pathlib.Path(a).resolve() for a in sys.argv[1:])
    sys.exit(0 if convert(source, target) else 1)
