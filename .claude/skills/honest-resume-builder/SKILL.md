---
name: honest-resume-builder
description: Build or rewrite a resume that is truthful, defensible in an interview, and ATS-safe. Use when a user wants to create a resume from scratch, fix an inflated/keyword-stuffed one, derive honest metrics from real project scope, or produce .docx + PDF outputs. Enforces a source-of-truth rule, no invented numbers, no cross-role contamination, a plain human voice, and single-column ATS formatting.
---

# Honest Resume Builder

A resume you cannot defend in an interview is a liability, not an asset. This
skill builds resumes that are true, specific, and pass automated screeners.

## The five rules (non-negotiable)

1. **One source of truth.** Pick a trusted record of the person's history
   (usually their LinkedIn export or a verified profile). Nothing on the resume
   may contradict it or be indefensible when asked "walk me through this."
2. **No invented numbers.** Never fabricate metrics (events/day, TB, "improved X
   by 30%"). Use only real scope. Where a number is defensible, *derive it from
   architecture* and round down: e.g. "4 source domains → 4 pipelines",
   "~20 bronze tables", "~40 dbt models". Manager-confirmed volumes are fair
   ("over 20 GB/day"). Payoff magnitudes that are IP or unmeasured stay off the
   page and become interview talking points.
3. **No cross-role contamination.** Tools and stories belong to the role where
   they actually happened. A bank role does not borrow a factory role's IoT
   content to hit keywords. Project-only tools (side-project Kafka, dbt Cloud,
   public APIs) live in the Projects/Skills sections, never in job bullets.
4. **100% human voice.** No em dashes as sentence breaks (ordinary compound
   hyphens like end-to-end are fine). Ban: leverage, spanning, robust, seamless,
   delve, elevate. No three-part dashed lists. Read every bullet aloud; if it
   sounds like a model wrote it, rewrite it.
5. **ATS-safe format.** Single column. No tables, text boxes, images, icons, or
   sidebars for content (a sidebar is the #1 ATS killer). Standard section
   headings. Contact details in the body, not the header/footer. Standard font,
   black text, • bullets. Spell out each acronym once (AQE, RLS, SCD Type 2).

## Process

1. **Collect the truth first.** Build a client-agnostic inventory of everything
   real: timeline, confirmed tools per role, real scope/entities, portfolio.
   Keep a separate "NOT real — never claim" list of tools they don't actually
   know. Assign facts to roles only after the pool is complete.
2. **Derive defensible numbers** from architecture (see rule 2). Write them down
   with the reasoning so they survive interview questions.
3. **Draft bullets**: strong verb + what was built + real scope + honest
   outcome. Mirror a target posting's wording only where it is genuinely true.
4. **Structure (locked default):** Header → Professional Summary → Technical
   Skills → Experience → Projects → Education. Drop certifications unless
   proctored/validated.
5. **Separate content from layout.** Put all content and PII in one data module
   (see `references/data-driven-pattern.md`). Generators read from it, so a fix
   flows to every output and no PII is hardcoded in committed code.
6. **Produce two outputs**: an ATS-safe `.docx` for uploads and a PDF for humans
   (clickable links). Build both from the *same* data source so they never drift.

## Building the files (no Node/LibreOffice/pandoc needed)

- **.docx**: `python-docx`, single column, tab stops for right-aligned dates.
  Install with `pip install --user python-docx` if missing.
- **.pdf**: render an HTML version with headless Chrome:
  `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --no-pdf-header-footer --print-to-pdf=out.pdf file://<abs>/resume.html`
- Reference implementations (`build_resume.py`, `build_html.py`,
  `resume_data.example.py`) live in this repo root and are the canonical example
  of the data-driven pattern.

## Related
- Audit an existing resume before rewriting: `resume-ats-check` skill.
- Write the matching letter: `cover-letter-writer` skill.
