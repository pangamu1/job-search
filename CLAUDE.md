# CLAUDE.md

Guidance for Claude working in this repo. Personal status and verified facts live
in `CLAUDE.local.md` (gitignored) — read it if present.

## What this repo is

A toolkit for building an honest, ATS-safe resume and running a job search. It is
**intended to be published publicly on GitHub**, so committed code must never
contain personal data.

## Golden rules

1. **No PII in committed files.** Real content and contact details live only in
   `resume_data.py`, which is gitignored. Builders and templates stay PII-free.
   Before any `git push`, verify nothing leaked: grep the staged tree for your own
   email, phone, and handles, e.g.
   `git grep --cached -iE "<email-prefix>|<phone-digits>|<github-handle>"` — must
   return nothing. (The real search terms live in `CLAUDE.local.md`, gitignored.)
2. **`.gitignore` patterns take no inline `#` comments** — git treats the whole
   line literally. Put comments on their own lines. (This once leaked
   `resume_data.py`; the pre-commit grep caught it.)
3. **Honest resume rules** (see the `honest-resume-builder` skill for the full
   version): one source of truth, no invented numbers (derive scope from
   architecture and round down), no cross-role contamination, plain human voice
   (no em dashes as sentence breaks; ban leverage/spanning/robust/seamless/delve),
   single-column ATS-safe format.

## Layout

```
resume_data.py            # REAL content + PII. Single source of truth. GITIGNORED.
resume_data.example.py    # committed placeholder template
build_resume.py           # imports resume_data -> ATS-safe .docx
build_html.py             # imports resume_data -> resume.html (-> Chrome PDF)
templates/cover-letter.md # committed cover-letter template
cover-letters/            # personalized letters (gitignored except .gitkeep)
.claude/skills/           # reusable skills (committed)
CLAUDE.local.md           # private status + verified facts (gitignored)
```

## Building the resume

Environment has no node/npm, no LibreOffice/pandoc; macOS AppleScript conversion
is blocked. Use the Python builders:

```bash
python3 build_resume.py "Name_Resume.docx"          # .docx (needs python-docx)
python3 build_html.py resume.html                   # HTML
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --no-pdf-header-footer \
  --print-to-pdf="Name_Resume.pdf" "file://$(pwd)/resume.html"
```

Both builders read `resume_data.py`, so edit content once and rebuild both.

### PDF gotchas (learned the hard way)

- **Export the PDF from the `build_html.py` -> headless-Chrome pipeline above, not
  by opening the `.docx` in Pages or another app.** Pages substitutes a font
  (Calibri is not on macOS) whose ligature glyphs carry a broken ToUnicode map, so
  the PDF *looks* perfect but its text layer extracts as garbage
  (`Functions` -> `FuncMons`, `Kafka` -> `KaIa`) and fails ATS keyword matching.
- **`build_html.py` sets `font-variant-ligatures: none`** so Chrome does not emit
  fi/fl ligatures (`Airflow` -> `Airﬂow`) into the PDF text layer. Keep it.
- **Bullets are the standard `•`.** A decorative glyph (e.g. the U+27A2 arrowhead)
  has no font in headless Chrome and renders as a tofu box in the PDF, even though
  it looks fine in Word. Standard bullets render in every engine.
- **Verify both ways:** extract the PDF text (keywords must read as plain ASCII)
  *and* look at a rendered page. Text extraction alone will not catch a marker that
  renders as a box; a visual check alone will not catch garbled ligature text.

## Skills in this repo

- `honest-resume-builder` — build/rewrite a truthful, ATS-safe resume.
- `cover-letter-writer` — short tailored cover letter from resume + posting.
- `resume-ats-check` — audit a resume for ATS killers and AI-tell/fabrication.
- `job-application-tracker` — log applications, status, follow-ups (Notion/CSV).
