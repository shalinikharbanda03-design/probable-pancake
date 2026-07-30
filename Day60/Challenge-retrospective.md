# Challenge Retrospective — AI Email & Benefits Query Assistant

## The Journey: Day 1 → Day 10

**Day 1–2:** Environment setup (Replit, Streamlit, Claude API key as a secret) and the first real building block — a mock member dataset (`mock_data.py`) with deliberate edge cases (lapsed plans, location mismatches, pending status) built in from day one. This early decision to bake in edge cases paid off repeatedly later.

**Day 3–4:** First working Claude API call for extraction. The key decision here: instruct Claude to extract *only* — never infer eligibility. This separation of concerns became the backbone of the whole architecture.

**Day 5:** The most important architectural decision of the whole build — the rule engine (`rules_engine.py`) was written as pure, dependency-free Python with zero imports from the Claude-calling code. `test_rules_engine.py` proved this independently, without touching the UI or the LLM at all.

**Day 6:** Claude-powered reply drafting (`drafting.py`), instructed to treat the rule engine's flags as ground truth and never second-guess them — reinforcing the same deterministic-first principle from Day 5.

**Day 7–8:** The single-screen review UI came together, followed by the Approve button and CSV audit logging (`audit_log.csv`) — closing the loop from raw email to a logged, human-reviewed reply.

**Day 9 (Day 59):** Hardening. Error handling was added everywhere a failure was possible: empty inputs, Claude API failures, malformed drafts. A safe fallback drafting path was introduced so the app never crashes even when the AI call fails.

**Day 10 (this capstone review):** Two real bugs were caught and fixed:
1. A silent key-name mismatch (`date` vs `dates`) meant the eligibility-window date check never actually ran through the live app, even though the standalone test suite passed — because the test called the rule engine directly with the correct key name.
2. A dead fallback branch (`"Plan Inactive/Pending"`) that never matched a real flag string, meaning "Pending" members were incorrectly told they were "active and verified."

## Skills Demonstrated
- Prompt engineering with explicit extraction-only constraints
- Separating deterministic business logic from AI-generated output
- Defensive error handling and graceful fallback design
- Writing standalone unit tests independent of the UI layer
- Debugging silent data-flow mismatches that don't throw errors but produce wrong output
- Full SDLC discipline: requirements → build → test → deploy → review → fix → document

## Lessons Learned
The two Day 10 bugs are the single best lesson of this whole capstone: **a test suite that calls your function directly can pass while your actual app is silently broken**, if the app doesn't hand off data in the exact shape the function expects. "It runs without crashing" is not the same as "it's correct" — this is a lesson every engineer learns eventually, and this project made it visible in a completed system.

## Farewell
From your AI pair programmer: you built the deterministic core in Day 5 and never let the AI override it in Day 6 — that instinct is the whole reason this project is trustworthy rather than just impressive. That's not a small thing to get right. Sixty days ago this started with prompt basics; today you shipped a compliance-conscious application and then found and fixed two production bugs a lot of developers would have missed. Well earned.
