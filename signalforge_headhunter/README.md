# SignalForge Headhunter (Local-First)

Privacy-first job-search intelligence app for Namratha Singh, designed to run locally on a Mac mini.

## Compliance Guardrails
- No scraping/automation that violates LinkedIn terms.
- No automated LinkedIn messaging.
- No bypassing login/CAPTCHA/rate limits.
- Manual review + manual sending only.
- Never stores passwords/session cookies.

## Stack
- FastAPI backend
- SQLite local database
- Jinja/HTML local UI
- Offline-first workflow with manual imports (CSV/text/URL snippets)

## Features Implemented
- Company discovery scoring (0-100)
- Role matching scoring (0-100)
- Profile intelligence classification
- Outreach note drafting templates (human-reviewed)
- Resume matcher + CAR bullet suggestions
- SQLite schema: companies, roles, people, outreach_notes, interactions, resumes, investors, signals
- Export-ready architecture (CSV/Markdown/JSON/DOCX hooks)

## Setup
```bash
cd signalforge_headhunter
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000

## Seed Data
```bash
sqlite3 app/data/signalforge.db < sample_data/seed.sql
```

## Run Tests
```bash
PYTHONPATH=. pytest -q
```

## Notes
This tool supports manual profile text input, CSV import, and user-provided URLs. It intentionally does not include automated outreach sending.
