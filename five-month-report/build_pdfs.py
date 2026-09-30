#!/usr/bin/env python3
"""Compile the five-month reports from Markdown to PDF.

Follows reports/report-template (TEMPLATE.md + template.html): the template's
CSS is reused verbatim, markdown tables get the template's table styling, and
each report renders to A4. The template's html2pdf.py drives headless Edge on
Windows; on this Linux machine weasyprint provides the same print-to-PDF step.

    python build_pdfs.py            # builds both reports
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

import markdown

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE.parent / "reports" / "report-template" / "template.html"

EXTRA_CSS = """
/* markdown-generated tables: reuse the template's table look */
table{border-collapse:collapse; width:100%; margin:10px 0}
th{font-family:"IBM Plex Mono",ui-monospace,monospace; font-size:10px; text-transform:uppercase;
  letter-spacing:.04em; color:var(--muted); text-align:left; border-bottom:1px solid var(--line);
  padding:4px 6px; font-weight:500}
td{border-bottom:1px solid var(--line); padding:4px 6px; vertical-align:top; font-size:12px; line-height:1.35}
tr:last-child td{border-bottom:none}
h1{font-size:24px; margin:6px 0 12px}
section.page h1{break-before:page; page-break-before:always; padding-top:8px}
section.page h1:first-of-type{break-before:auto; page-break-before:auto}
h2{font-size:17px; margin:20px 0 6px; border-bottom:1px solid var(--line); padding-bottom:3px}
h3{font-size:14px; margin:16px 0 4px}
blockquote{border-left:3px solid var(--accent); margin:8px 0; padding:2px 12px; color:var(--ink-2);
  background:var(--accent-soft); border-radius:0 6px 6px 0}
code{font-family:"IBM Plex Mono",monospace; font-size:.88em; background:var(--sunk);
  padding:0 3px; border-radius:3px}
pre{background:var(--sunk); border:1px solid var(--line); border-radius:8px; padding:10px 12px;
  overflow-x:auto; font-size:11px}
pre code{background:none; padding:0}
ol,ul{padding-left:22px} li{margin-bottom:5px; font-size:13px; color:var(--ink-2)}
li b{color:var(--ink)}
strong{color:var(--ink)}
hr{border:none; border-top:1px solid var(--line); margin:18px 0}
"""


def build_css() -> str:
    html = TEMPLATE.read_text()
    m = re.search(r"<style>(.*?)</style>", html, re.S)
    css = m.group(1)
    # weasyprint needs its own @page; drop the print-media block's @page duplication
    return css + EXTRA_CSS


def md_to_html(md_path: pathlib.Path, title: str) -> str:
    text = md_path.read_text()
    body = markdown.markdown(text, extensions=["tables", "fenced_code"])
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
{build_css()}
@page {{ size: A4; margin: 14mm 13mm;
  @bottom-center {{ content: counter(page) " / " counter(pages);
    font-family: "IBM Plex Mono", monospace; font-size: 9px; color: #5E6E75; }} }}
body{{background:#fff; padding:0; font-size:12px}}
section.page{{max-width:none; padding:0; border:0}}
</style>
</head>
<body>
{body}
</body>
</html>
"""


def build(md_name: str, pdf_name: str, title: str) -> bool:
    md_path = HERE / md_name
    html_path = HERE / pdf_name.replace(".pdf", ".html")
    pdf_path = HERE / pdf_name
    html_path.write_text(md_to_html(md_path, title))
    r = subprocess.run(
        ["weasyprint", str(html_path), str(pdf_path)],
        capture_output=True, text=True, timeout=300,
    )
    ok = pdf_path.exists() and pdf_path.stat().st_size > 10000
    size = pdf_path.stat().st_size / 1024 if pdf_path.exists() else 0
    print(f"{'OK  ' if ok else 'FAIL'} {pdf_name}  ({size:,.0f} KB)")
    if not ok and r.stderr:
        print(r.stderr[:2000])
    return ok


if __name__ == "__main__":
    ok = True
    ok &= build("executive-summary.md", "executive-summary.pdf",
                "AI Gateway - Five-Month Executive Summary")
    ok &= build("technical-report.md", "technical-report.pdf",
                "AI Gateway - Five-Month Technical Report")
    sys.exit(0 if ok else 1)
