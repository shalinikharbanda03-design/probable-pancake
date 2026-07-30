# 30-Day Growth Plan — AI Email & Benefits Query Assistant

Turning this MVP into a significantly more complete product, one milestone per day.

## Week 1 — Real Extraction & Data Layer
- **Day 1:** Wire up real Claude-powered extraction (`call_claude_extract`) into `app.py`, replacing the hardcoded "John Doe" demo data.
- **Day 2:** Add a manual-paste + `.eml`/`.txt` file upload option in the UI (per the original Day 2 blueprint spec).
- **Day 3:** Move `mock_data.py` into a local SQLite database; rewrite `mock_data.get_member_by_name` to query it.
- **Day 4:** Add 5+ new test members to the database covering more edge cases (similar names, multiple locations).
- **Day 5:** Add fuzzy name matching (e.g. `difflib`) to `rules_engine.py` so small typos in names still match.
- **Day 6:** Add location normalization (state abbreviations ↔ full names) as a small lookup table.
- **Day 7:** Write 10 new unit tests covering the new extraction + fuzzy matching logic.

## Week 2 — Reliability & Observability
- **Day 8:** Add structured logging (Python `logging` module) alongside the existing `st.error` messages.
- **Day 9:** Add retry-with-backoff for Claude API calls (currently single retry only).
- **Day 10:** Add a "confidence score" field to extraction output, shown in the UI when extraction is uncertain.
- **Day 11:** Build a small analytics view: flag frequency chart from `audit_log.csv`, using `pandas` + `st.bar_chart`.
- **Day 12:** Add CSV export filtering (by date range, by flag type) to the audit log view.
- **Day 13:** Add input sanitization tests for malicious/malformed `.eml` files.
- **Day 14:** Mid-point review: re-run all tests, fix any regressions from Week 1–2 changes.

## Week 3 — Access Control & Multi-User
- **Day 15:** Add simple username/password login using `streamlit-authenticator`.
- **Day 16:** Add an Analyst vs Supervisor role distinction.
- **Day 17:** Require Supervisor approval for high-risk flags ("Member Not Found", "Outside Eligibility Window").
- **Day 18:** Add a per-user audit trail column (`approved_by`) to `audit_log.csv`.
- **Day 19:** Add a "pending supervisor review" queue view.
- **Day 20:** Add email notifications (mock/logged, not real SMTP) when a reply needs supervisor review.
- **Day 21:** Test the full multi-role flow end-to-end with 2 simulated users.

## Week 4 — Polish, Docs & Real-World Readiness
- **Day 22:** Move from CSV to SQLite/Postgres for the audit log itself (durability + concurrent writes).
- **Day 23:** Add a settings page (toggle demo mode, configure retry counts, etc.).
- **Day 24:** Add dark/light theme support and mobile-responsive layout tweaks.
- **Day 25:** Write API documentation for `rules_engine.check_member` and `drafting.call_claude_draft` (docstrings → a docs page).
- **Day 26:** Add a `CONTRIBUTING.md` and `LICENSE` file to the repo.
- **Day 27:** Load-test the app with 50 simulated sequential analyses; fix any performance issues found.
- **Day 28:** Record a 3-minute demo video showing the full multi-role, real-extraction flow.
- **Day 29:** Full regression test pass across all features built in the 30 days.
- **Day 30:** Tag and release **v2.0.0** with full release notes summarizing the 30-day transformation from MVP to multi-user, real-extraction product.
