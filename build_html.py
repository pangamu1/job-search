#!/usr/bin/env python3
"""Build resume.html from resume_data.py, ready for headless-Chrome PDF export.

Usage: python3 build_html.py <out.html>
Content lives in resume_data.py (gitignored). This file is layout only, no PII.
Then render to PDF, e.g.:
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new \
    --no-pdf-header-footer --print-to-pdf=<out.pdf> file://<abs path to out.html>
"""
import re
import sys
from html import escape

import resume_data as data

CSS = """
  @page { size: A4; margin: 13mm 15mm; }
  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    font-family: Calibri, "Helvetica Neue", Arial, sans-serif;
    color: #111;
    font-size: 10.5pt;
    line-height: 1.28;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
    /* Disable fi/fl ligatures so PDF text extracts as plain "Airflow", not the
       "Airﬂow" ligature glyph, which can break ATS keyword matching. */
    font-variant-ligatures: none;
  }
  .name { text-align: center; font-size: 20pt; font-weight: 700; color: #1F3864; letter-spacing: .3px; }
  .title { text-align: center; font-size: 12pt; margin-top: 1px; }
  .contact { text-align: center; margin-top: 3px; font-size: 10.5pt; }
  .contact a { color: #0563C1; text-decoration: underline; }
  h2 {
    font-size: 12pt; color: #1F3864; text-transform: uppercase;
    border-bottom: 1px solid #1F3864; padding-bottom: 2px; margin: 13px 0 5px;
    letter-spacing: .3px;
  }
  p { margin: 0 0 3px; }
  .summary { text-align: justify; }
  .skill { margin: 0 0 1.5px; }
  .skill b { color: #111; }
  .jobrow { display: flex; justify-content: space-between; margin-top: 6px; }
  .jobrow .role { font-weight: 700; font-size: 11pt; }
  .jobrow .dates { font-size: 10.5pt; white-space: nowrap; }
  .company { font-style: italic; margin: 0 0 3px; }
  ul { margin: 0 0 2px; padding-left: 16px; }
  li { margin: 0 0 2.5px; text-align: justify; }
  .pname { font-weight: 700; font-size: 11pt; margin: 6px 0 0; }
  .plink { margin: 1px 0 0; }
  .plink a { color: #0563C1; text-decoration: underline; font-size: 10.5pt; }
  .stack { font-style: italic; font-size: 10pt; margin: 1px 0 3px; }
  .edu { display: flex; justify-content: space-between; margin-top: 4px; }
  .edu .deg { font-weight: 700; }
  .school { font-style: italic; margin: 0; }
"""


def e(s):
    return escape(s, quote=True)


def md(s):
    """Escape s, then render **double-asterisk** spans as bold."""
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", e(s))


def sep(text):
    return text.replace("|", "&nbsp;&nbsp;|&nbsp;&nbsp;")


def build():
    c = data.CONTACT
    out = []
    out.append("<!doctype html>")
    out.append('<html lang="en">')
    out.append("<head>")
    out.append('<meta charset="utf-8">')
    out.append(f"<title>{e(c['name'].title())} - {e(c['title'])}</title>")
    out.append(f"<style>{CSS}</style>")
    out.append("</head>")
    out.append("<body>")

    out.append(f'  <div class="name">{e(c["name"])}</div>')
    out.append(f'  <div class="title">{e(c["title"])}</div>')
    out.append(
        f'  <div class="contact">{e(c["location"])}&nbsp;&nbsp;|&nbsp;&nbsp;'
        f'{e(c["email"])}&nbsp;&nbsp;|&nbsp;&nbsp;{e(c["phone"])}</div>'
    )
    out.append(
        f'  <div class="contact"><a href="{e(c["linkedin_url"])}">{e(c["linkedin_text"])}</a>'
        f'&nbsp;&nbsp;|&nbsp;&nbsp;<a href="{e(c["github_url"])}">{e(c["github_text"])}</a></div>'
    )

    out.append("  <h2>Professional Summary</h2>")
    out.append(f'  <p class="summary">{e(data.SUMMARY)}</p>')

    out.append("  <h2>Technical Skills</h2>")
    for k, v in data.SKILLS:
        out.append(f'  <p class="skill"><b>{e(k)}:</b> {e(v)}</p>')

    out.append("  <h2>Experience</h2>")
    for job in data.EXPERIENCE:
        out.append(
            f'  <div class="jobrow"><span class="role">{e(job["role"])}</span>'
            f'<span class="dates">{e(job["dates"])}</span></div>'
        )
        out.append(f'  <p class="company">{e(job["company"])}</p>')
        out.append("  <ul>")
        for b in job["bullets"]:
            out.append(f"    <li>{md(b)}</li>")
        out.append("  </ul>")

    out.append("  <h2>Projects</h2>")
    for proj in data.PROJECTS:
        out.append(
            f'  <div class="jobrow"><span class="role">{e(proj["name"])}</span>'
            f'<span class="dates">{e(proj["dates"])}</span></div>'
        )
        out.append(f'  <p class="plink"><a href="{e(proj["url"])}">{e(proj["url_text"])}</a></p>')
        out.append("  <ul>")
        for b in proj["bullets"]:
            out.append(f"    <li>{md(b)}</li>")
        out.append("  </ul>")

    out.append("  <h2>Education</h2>")
    for ed in data.EDUCATION:
        out.append(
            f'  <div class="edu"><span class="deg">{e(ed["degree"])}</span>'
            f'<span>{e(ed["dates"])}</span></div>'
        )
        out.append(f'  <p class="school">{e(ed["school"])}</p>')

    out.append("</body>")
    out.append("</html>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    dest = sys.argv[1] if len(sys.argv) > 1 else "resume.html"
    with open(dest, "w", encoding="utf-8") as f:
        f.write(build())
    print("written", dest)
