# AI Email & Benefits Query Assistant

An AI-powered assistant that reads member benefit/eligibility emails, checks them against deterministic compliance rules, and drafts a ready-to-review reply — built as the capstone project for the AB Talks 60-Day Claude AI Challenge.

## What It Does
1. Takes a raw email (demo mode: uses a fixed sample member).
2. Extracts key fields (name, location, dates, intent).
3. Runs the extracted data through a **pure Python rule engine** (no AI) to check eligibility, location match, and plan status.
4. Uses **Claude** to draft a professional, empathetic reply — treating the rule engine's flags as ground truth.
5. Lets a human reviewer edit and approve the reply before it's logged.
6. Logs every approved reply to a CSV audit trail.

## Why Deterministic + AI (not just AI)
Compliance decisions (eligibility, location match, plan status) are made by plain Python logic in `rules_engine.py` — completely separate from any AI call. This makes every flag explainable and reproducible, with no risk of the AI silently overriding a compliance rule. Claude is only used for the human-facing tone of the reply, never for the decision itself.

## Current Scope (Important)
This is an MVP demo:
- Extraction is **simulated** — the app always analyzes one fixed sample member ("John Doe"), regardless of what's typed in the sample box. Live extraction from arbitrary email text is a planned next step (see `future-scope.md`).
- No real member data or real email integration — demo dataset only.

## Tech Stack
- **Frontend/App:** Streamlit
- **AI:** Anthropic Claude API (with a deterministic local fallback if no API key is set)
- **Rule Engine:** Pure Python, fully unit-tested (`test_rules_engine.py`)
- **Audit Log:** CSV-based, append-only

## Project Structure
