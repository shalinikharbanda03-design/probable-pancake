# Day 54-55: Core Feature Implementation + Rule Engine

## Overview
Implemented core email extraction and a deterministic rule-based eligibility/location engine for the AI-Powered Email & Benefits Query Assistant.

## Features
- **Extraction (`extraction.py`)**: Regex-based parsing of member name, location, and date from raw email text.
- **Mock Data (`mock_data.py`)**: 4 fictional member records with eligibility dates, plan status, and location.
- **Rule Engine (`rules_engine.py`)**: Pure Python, deterministic logic — NO AI/LLM calls. Flags:
  - Member Not Found / Member Name Missing
  - Location Mismatch
  - Outside Eligibility Window
  - Plan Inactive / Plan Pending
- **UI (`app.py`)**: Streamlit app showing extraction output, rule check flags, and matched record.

## Testing
Run `python test_rules_engine.py` — all 6 rule engine tests pass independent of the UI or any AI call.

## File Structure
- `app.py` — Streamlit UI pipeline
- `extraction.py` — regex-based entity extraction
- `mock_data.py` — mock member dataset
- `rules_engine.py` — deterministic eligibility/location rule engine
- `test_rules_engine.py` — standalone rule engine tests
- `requirements.txt` — dependencies
