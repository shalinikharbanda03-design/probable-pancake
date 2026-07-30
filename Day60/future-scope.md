# Future Scope — AI Email & Benefits Query Assistant

## Next 3 Months
- Replace simulated extraction with real Claude-powered extraction from arbitrary email text (the `call_claude_extract` function outlined in the original blueprint but not yet wired into the live app).
- Expand `mock_data.py` into a small SQLite database so multiple members can be tested without code changes.
- Add proper location normalization (e.g. "NY" vs "New York") using a lookup table instead of exact string match.
- Add basic authentication so only authorized analysts can access the review screen.

## Next 6 Months
- Connect to a real (sandboxed) email inbox via IMAP so emails can be pulled automatically instead of pasted manually.
- Add a simple analytics dashboard on top of `audit_log.csv` (flag frequency, approval turnaround time).
- Introduce multi-language extraction support for non-English member emails.
- Add role-based access (Analyst vs Supervisor) with a supervisor approval step for high-risk flags (e.g. "Member Not Found").

## Next 12 Months
- Move from CSV audit logging to a proper database (Postgres) with full query/reporting support.
- Add a feedback loop: let analysts mark AI-drafted replies as "edited heavily" vs "approved as-is" to track drafting quality over time.
- Explore fine-tuning or prompt-optimization based on 12 months of real (anonymized) analyst edits.
- Package the rule engine as a standalone, independently-testable compliance microservice usable by other internal tools.
