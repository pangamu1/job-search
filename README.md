# Job Search Toolkit

A small, honest toolkit for building a resume and running a job search, plus
reusable [Claude Code](https://docs.claude.com/en/docs/claude-code) skills that
encode the method. Personal data is kept out of version control.

## What's here

| Path | Purpose |
|------|---------|
| `resume_data.example.py` | Placeholder template for your resume content. Copy to `resume_data.py` (gitignored) and fill in. |
| `build_resume.py` | Renders an ATS-safe `.docx` from `resume_data.py` (uses `python-docx`). |
| `build_html.py` | Renders `resume.html` from `resume_data.py`; print it to PDF with headless Chrome. |
| `templates/cover-letter.md` | Reusable cover-letter template (fill the `{{placeholders}}`). |
| `.claude/skills/` | The reusable skills (below). |

## The skills

- **honest-resume-builder** — build or rewrite a truthful, interview-defensible,
  ATS-safe resume. Source-of-truth rule, no invented numbers, no cross-role
  contamination, plain human voice, single-column format.
- **cover-letter-writer** — a short, tailored, honest cover letter from a resume
  plus a specific posting.
- **resume-ats-check** — audit an existing resume for ATS parsing killers and
  AI-tell / fabrication red flags before submitting.
- **job-application-tracker** — log applications, statuses, and follow-ups
  (Notion or a local CSV).

## Quick start

```bash
# 1. Fill in your details (this file is gitignored)
cp resume_data.example.py resume_data.py
$EDITOR resume_data.py

# 2. Build the ATS-safe .docx (install python-docx if needed)
pip install --user python-docx
python3 build_resume.py "Your_Name_Resume.docx"

# 3. Build the HTML, then print to PDF with headless Chrome
python3 build_html.py resume.html
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --no-pdf-header-footer \
  --print-to-pdf="Your_Name_Resume.pdf" "file://$(pwd)/resume.html"
```

Both outputs are built from the same `resume_data.py`, so a content edit flows to
both and they never drift apart.

## Privacy

`resume_data.py`, all built `.docx`/`.pdf`/`resume.html`, source PDFs, and
personalized cover letters are gitignored. Only PII-free code and templates are
committed. Review `.gitignore` before pushing anywhere public.
