---
name: job-application-tracker
description: Log and track job applications and their status, follow-ups, and outcomes. Use when a user wants to record an application they submitted, check what needs a follow-up, see their pipeline, or set up a tracker. Supports a Notion database or a local CSV/spreadsheet.
---

# Job Application Tracker

Keep one row per application so nothing falls through the cracks and follow-ups
happen on time.

## Schema (fields per application)
- **Company**
- **Role** (title as posted)
- **Location / Remote**
- **Source** (LinkedIn, referral, company site, ...)
- **Date applied** (YYYY-MM-DD)
- **Status** — one of: `Wishlist`, `Applied`, `Phone screen`, `Interview`,
  `Offer`, `Rejected`, `Ghosted`, `Withdrawn`
- **Next action** + **Next action date** (e.g. "follow up" on applied+7 days)
- **Resume version** used (which tailored file)
- **Cover letter** (path under `cover-letters/`, if any)
- **Contact** (recruiter/manager name + link)
- **Job posting URL**
- **Salary range** (if listed)
- **Notes** (interview feedback, questions asked, etc.)

## Backends

### Notion (preferred for this repo)
Use the Notion tools to create/update a database. On first setup, create a
database with the fields above (Status and Source as select fields, dates as
date fields). To log an application, add a page; to update, patch the Status and
Next action. When asked "what needs a follow-up", query for rows where
`Next action date <= today` and status is not terminal
(Rejected/Ghosted/Withdrawn/Offer).

### Local CSV (no external service)
Maintain `applications.csv` in the repo (gitignore it if it contains contacts).
Columns = the schema fields. For edits, read the CSV, modify the row, write it
back. For a quick view, render a table sorted by Next action date.

## Common operations
- **Log**: capture company/role/source/date, set Status=Applied, set Next action
  = "follow up" at applied + 7 days.
- **Advance**: move Status forward, update Next action + date.
- **Follow-ups due**: filter to Next action date <= today, non-terminal status.
- **Pipeline view**: count by Status; show active applications grouped by stage.

## Related
- Resume version comes from `honest-resume-builder`; letters from
  `cover-letter-writer` (stored in `cover-letters/`).
