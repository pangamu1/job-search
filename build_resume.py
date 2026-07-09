#!/usr/bin/env python3
"""Build the ATS-safe .docx resume from resume_data.py.

Usage: python3 build_resume.py <out.docx>
Content lives in resume_data.py (gitignored). This file is layout only, no PII.
"""
import sys
from docx import Document
from docx.shared import Pt, RGBColor, Mm, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

import resume_data as data

FONT = "Calibri"
NAVY = RGBColor(0x1F, 0x38, 0x64)
BODY = 10.5
RIGHT_TAB = Cm(17.4)  # right edge of content on A4 with ~1.8cm margins

doc = Document()

# ---- base style ----
normal = doc.styles["Normal"]
normal.font.name = FONT
normal.font.size = Pt(BODY)
normal.paragraph_format.space_after = Pt(0)
normal.paragraph_format.line_spacing = 1.0

# ---- page: A4, tight margins ----
sec = doc.sections[0]
sec.page_width = Mm(210)
sec.page_height = Mm(297)
for side in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
    setattr(sec, side, Cm(1.8))


def set_run(r, size=BODY, bold=False, italic=False, color=None):
    r.font.name = FONT
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color is not None:
        r.font.color.rgb = color
    # ensure east-asian/complex use same font too
    rpr = r._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(a), FONT)
    return r


def para(space_before=0, space_after=0, align=None):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    if align is not None:
        p.alignment = align
    return p


def run(p, text, **kw):
    return set_run(p.add_run(text), **kw)


def add_hyperlink(p, url, text, size=BODY):
    part = p.part
    r_id = part.relate_to(
        url,
        "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
        is_external=True,
    )
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rfonts = OxmlElement("w:rFonts")
    for a in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(a), FONT)
    rpr.append(rfonts)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rpr.append(sz)
    color = OxmlElement("w:color"); color.set(qn("w:val"), "0563C1"); rpr.append(color)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    new_run.append(rpr)
    wt = OxmlElement("w:t"); wt.text = text; new_run.append(wt)
    hyperlink.append(new_run)
    p._p.append(hyperlink)
    return hyperlink


def section_heading(text):
    p = para(space_before=11, space_after=4.5)
    run(p, text.upper(), size=12, bold=True, color=NAVY)
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), "1F3864")
    pbdr.append(bottom)
    pPr.append(pbdr)
    return p


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    run(p, text)
    return p


def job_header(title, dates, company_location):
    p = para(space_before=6, space_after=0)
    p.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB, WD_TAB_ALIGNMENT.RIGHT)
    run(p, title, size=11, bold=True)
    run(p, "\t" + dates, size=BODY)
    p2 = para(space_after=3)
    run(p2, company_location, italic=True)


def edu_entry(degree, dates, school):
    p = para(space_before=3, space_after=0)
    p.paragraph_format.tab_stops.add_tab_stop(RIGHT_TAB, WD_TAB_ALIGNMENT.RIGHT)
    run(p, degree, bold=True)
    run(p, "\t" + dates)
    p2 = para(space_after=2)
    run(p2, school, italic=True)


# ============ HEADER ============
c = data.CONTACT
p = para(align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, c["name"], size=20, bold=True, color=NAVY)
p = para(space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, c["title"], size=12)
p = para(align=WD_ALIGN_PARAGRAPH.CENTER)
run(p, f"{c['location']}  |  {c['email']}  |  {c['phone']}")
p = para(space_after=2, align=WD_ALIGN_PARAGRAPH.CENTER)
add_hyperlink(p, c["linkedin_url"], c["linkedin_text"])
run(p, "  |  ")
add_hyperlink(p, c["github_url"], c["github_text"])

# ============ SUMMARY ============
section_heading("Professional Summary")
p = para(space_after=3)
run(p, data.SUMMARY)

# ============ SKILLS ============
section_heading("Technical Skills")
for k, v in data.SKILLS:
    p = para(space_after=1)
    run(p, k + ": ", bold=True)
    run(p, v)

# ============ EXPERIENCE ============
section_heading("Experience")
for job in data.EXPERIENCE:
    job_header(job["role"], job["dates"], job["company"])
    for b in job["bullets"]:
        bullet(b)

# ============ PROJECTS ============
section_heading("Projects")
for i, proj in enumerate(data.PROJECTS):
    p = para(space_before=6 if i else 4, space_after=0)
    run(p, proj["name"], size=11, bold=True)
    p = para(space_after=0)
    add_hyperlink(p, proj["url"], proj["url_text"])
    p = para(space_after=3)
    run(p, proj["stack"], size=10, italic=True)
    for b in proj["bullets"]:
        bullet(b)

# ============ EDUCATION ============
section_heading("Education")
for e in data.EDUCATION:
    edu_entry(e["degree"], e["dates"], e["school"])

out = sys.argv[1] if len(sys.argv) > 1 else "resume.docx"
doc.save(out)
print("written", out)
