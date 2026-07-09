---
name: cover-letter-writer
description: Write a short, honest, tailored cover letter from a resume plus a specific job posting. Use when a user wants a cover letter for an application, or wants to tailor an existing one to a new role. Keeps the same no-fabrication and plain-voice rules as the resume, mirrors the posting's real requirements, and stays to half a page.
---

# Cover Letter Writer

A cover letter earns its place only if it says something the resume cannot: why
*this* company, and how the person's real experience maps to *this* posting's
top requirements. Otherwise it is filler.

## Inputs to gather first
1. The **job posting** (paste or URL). Extract the role title, the 3–4 hardest
   requirements, the company, and anything specific about their product/domain.
2. The candidate's **resume or `resume_data.py`** for real achievements to cite.
3. The **hiring manager's name** if known (else "Hiring Team").

## Rules (inherited from honest-resume-builder)
- Real claims only. Every achievement you cite must exist on the resume and be
  defensible in an interview. No new invented metrics.
- Plain human voice. No em dashes as sentence breaks. Ban: leverage, spanning,
  robust, seamless, delve, elevate. No three-part dashed lists.
- Mirror the posting's wording *only where it is genuinely true* for the person.

## Structure (half a page, 3–4 paragraphs)
1. **Opening**: name the role and one specific, genuine reason for this company.
   Reference something concrete about them so it does not read as a form letter.
2. **Fit**: pick the 2–3 requirements the person matches best; back each with one
   real achievement from the resume.
3. **Differentiator** (optional): one project or strength that a bullet list
   would not convey (a portfolio build, a tuning/cost win, a domain crossover).
4. **Close**: thank them, state interest/availability, invite the next step.

## Process
1. Read the posting; list its top requirements in priority order.
2. For each, find the strongest matching evidence in the resume. If there is no
   honest match for a "must-have", tell the user rather than inventing one.
3. Fill `templates/cover-letter.md` (in this repo). Delete the guidance notes.
4. Save the personalized letter under `cover-letters/` (gitignored) as
   `cover-letters/<company>-<role>.md`.
5. Read it aloud. Cut anything that sounds generated or that you could not defend.

## Related
- Source of the achievements: `honest-resume-builder` skill and `resume_data.py`.
