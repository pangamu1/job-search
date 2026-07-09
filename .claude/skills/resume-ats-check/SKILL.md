---
name: resume-ats-check
description: Audit an existing resume for ATS (applicant tracking system) parsing killers and AI-tell / fabrication red flags before it is submitted. Use when a user wants their resume reviewed, checked for ATS-safety, screened for buzzwords or an inflated/keyword-stuffed feel, or compared against a job posting. Reports issues; does not silently rewrite.
---

# Resume ATS Check

A linter for resumes. It flags what breaks automated parsers and what makes a
resume read as dishonest or machine-written. It reports findings for the user to
fix (or hands off to `honest-resume-builder` for a rewrite); it does not quietly
rewrite content.

## What to check

### A. ATS parsing killers (structure)
- **Sidebars / multi-column layouts** — the #1 killer. Two-column PDFs get read
  in the wrong order or scrambled. Flag any non-single-column content.
- **Tables, text boxes, images, icons, charts** carrying real content — many
  parsers drop them entirely.
- **Contact details in the header/footer** — often ignored by parsers. They
  belong in the document body.
- **Non-standard section headings** — use Summary, Technical Skills, Experience,
  Projects, Education, Certifications so the parser can classify sections.
- **Unusual fonts, colored body text, graphics-only bullets.**
- **Links hidden behind words only** — show the full URL as text *and* hyperlink
  it, so the parser reads the plain URL.
- **Acronyms never spelled out** — expand each once (AQE, RLS, SCD Type 2).

### B. Honesty / voice red flags (content)
- **Invented-looking metrics** — suspiciously round or unverifiable numbers
  (1M events/day, 20 TB, "improved X by 30%"). Ask what the real, defensible
  figure is; if none, cut it.
- **Cross-role contamination** — tools or stories that don't fit the employer
  (a bank role listing factory IoT). Flag mismatches to the role's real domain.
- **Keyword stuffing** — long tool lists with no evidence of use, or the same
  buzzwords repeated. Tools should trace to a real bullet or project.
- **AI tells** — em dashes as sentence breaks; the words leverage, spanning,
  robust, seamless, delve, elevate; three-part dashed lists; uniform bullet
  rhythm that reads as generated.
- **Title inflation** — summary headline may aim higher (e.g. "Senior ..."), but
  past *job-entry* titles must stay factual.

### C. Posting fit (only if a job posting is provided)
- List the posting's must-have requirements and whether the resume evidences each
  *honestly*. Note gaps; never suggest inventing evidence to close one.

## Output
Report as a checklist grouped A / B / C, each item marked pass / fix, with a one
line why and a concrete suggestion. Offer to hand off to `honest-resume-builder`
for the rewrite. Do not fabricate replacements for flagged numbers.
