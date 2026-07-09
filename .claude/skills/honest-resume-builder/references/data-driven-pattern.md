# Data-driven resume pattern

Keep content and PII in one module; keep generators PII-free. This fixes two
problems at once: outputs never drift, and the repo is safe to publish.

```
resume_data.py            # REAL content + contact details. GITIGNORED.
resume_data.example.py    # committed placeholder with the same structure
build_resume.py           # imports resume_data, emits ATS-safe .docx
build_html.py             # imports resume_data, emits resume.html (-> Chrome PDF)
```

`resume_data.py` exposes plain Python data:

```python
CONTACT = {"name": ..., "title": ..., "location": ..., "email": ...,
           "phone": ..., "linkedin_url": ..., "linkedin_text": ...,
           "github_url": ..., "github_text": ...}
SUMMARY = "..."                       # one paragraph
SKILLS = [("Category", "a, b, c"), ...]
EXPERIENCE = [{"role", "dates", "company", "bullets": [...]}, ...]
PROJECTS = [{"name", "url", "url_text", "stack", "bullets": [...]}, ...]
EDUCATION = [{"degree", "dates", "school"}, ...]
```

Both builders `import resume_data as data` and walk these structures. A content
edit is made once, in `resume_data.py`, and both the .docx and PDF pick it up on
the next build.

**.gitignore must cover**: `resume_data.py`, built `*.docx`/`*.pdf`/`resume.html`,
any source PDFs, and personalized cover letters. Commit only the builders and the
`.example` template.

**Hyperlinks**: show the full URL as visible text *and* hyperlink it. ATS readers
parse the plain URL; humans click the link. Never hide a link behind words only.
