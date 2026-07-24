:PROMPT:
System Design

Today is Day 2, continuing our chat from Day 1. Read the PRD, Implementation Blueprint, and Pitch Deck created yesterday. These are now the source of truth for the project. Do not redesign or rethink the project unless a critical issue is discovered.

Standing Rules

Whenever I need to perform a manual task outside this chat (creating a GitHub repository, installing software, using Git, configuring dashboards, etc.), stop and give me an exact numbered step-by-step guide using the real names of buttons, menus, fields, and commands.
Wait for my confirmation and a screenshot before moving on.
Do not assume I've completed any manual step.

Today's Goal

Today's objective is to transform the project plan into a complete technical blueprint that makes implementation straightforward.

Do not write production code today.

Follow the Day 2 section of the Implementation Blueprint, but improve it wherever necessary.

If any design decision conflicts with the approved PRD or Implementation Blueprint, explain why and ask for my approval before changing it.

Complete the following

0. Repository Setup

If I don't already have a GitHub repository for this project:

Walk me through creating one.
Clone it locally.
Create the initial project structure.
Explain every step before we continue.

1. Finalize the Tech Stack

Based on the project requirements:

Frontend
Backend
Database
Authentication
AI Model/API (if needed)
Hosting
Other tools or libraries

Explain why each choice is the best fit. Prefer free tools whenever possible.

2. System Architecture

Design the complete architecture. Include:

Component diagram
Data flow
Request lifecycle
AI interaction (if applicable)
External services

Show the architecture using diagrams (Mermaid preferred).

3. Database Design

If the project requires data storage: Design:

Tables / Collections
Fields
Relationships
Constraints

Validate the schema against every user story from the PRD.

4. API Design

List every endpoint required for the v1.0 product. For each endpoint include:

Purpose
Request
Response
Validation
Authentication
Error cases

No implementation yet.

5. UI & User Flow

Design the complete user journey. Include:

User Flow Diagram
Screen Flow
Wireframes (low fidelity is enough)
Navigation

Every screen should exist for a reason.

6. Project Structure

Design the complete folder structure. Explain:

What every major folder is responsible for.
Where future code will live.
Why the structure was chosen.

7. Day 3 Readiness Check

Review the remaining Implementation Blueprint. Confirm that:

The project can realistically be completed within the remaining days.
No unnecessary scope has crept in.
Tomorrow can begin implementation immediately.

If anything should be simplified, recommend it now.

Deliverables

Generate downloadable versions of:

ARCHITECTURE.md
SCHEMA.md
API.md
UI-WIREFRAMES.md
PROJECT-STRUCTURE.md

Also update the Implementation Blueprint if today's design decisions require any changes.

End of Day

Help me:

Commit today's work.
Push it to GitHub.
Update the project log.
Write a LinkedIn post summarizing today's progress.

Tomorrow should begin building immediately, with no additional planning required.


1.:ARCHITECTURE.md:

# System Architecture

## Overview
The AI-Powered Email & Benefits Query Assistant is a single-process Streamlit application built with Python. It parses client/broker email queries (.txt/.eml), extracts key details, checks member eligibility against a local mock CSV database using rule-based logic, and drafts professional, HIPAA-conscious responses using the Anthropic Claude API.

## Architecture Diagram (Mermaid)

```mermaid
graph TD
    A[User / Healthcare Analyst] -->|Uploads .txt/.eml File| B[Streamlit UI - app.py]
    B -->|Raw Text| C[Text Extraction & Parsing - extraction.py]
    C -->|Extracted Fields: Name, Dates, Location| D[Rule-Based Compliance Check - compliance_check.py]
    D -->|Match Query| E[(Mock Dataset - data/mock_members.csv)]
    E -->|Member Data & Discrepancies| D
    D -->|Flags & Extracted Data| F[AI Draft Generation - ai_drafting.py]
    F -->|Prompt + Context| G[Anthropic Claude API]
    G -->|Drafted Response| F
    F -->|Draft & Insights| B
    B -->|Analyst Reviews & Approves| H[Audit Logger - data/audit_log.csv]

 --- 2. `SCHEMA.md`

```

:markdown:
# Database & Data Schema

The system uses local CSV files managed via `pandas` to maintain a lightweight, zero-database setup consistent with v1.0 requirements.

## 1. Mock Member Dataset (`data/mock_members.csv`)

Stores static fake member eligibility and location data.

| Field Name | Data Type | Description | Example / Notes |
| :--- | :--- | :--- | :--- |
| `member_id` | String | Unique identifier for member | `"MEM-1001"` |
| `member_name` | String | Full name of the member | `"Jane Doe"` |
| `dob` | String (YYYY-MM-DD) | Date of birth | `"1985-06-12"` |
| `eligibility_status` | String | Current coverage status | `"Active"`, `"Terminated"`, `"Pending"` |
| `plan_type` | String | Assigned health plan | `"PPO Gold"`, `"HMO Silver"` |
| `state_location` | String | Primary registered state | `"CA"`, `"NY"`, `"TX"` |
| `effective_date` | String (YYYY-MM-DD) | Plan start date | `"2024-01-01"` |

---
2. Audit Log Dataset (`data/audit_log.csv`)

Appends historical records when the analyst clicks "Approve".

| Field Name | Data Type | Description | Example / Notes |
| :--- | :--- | :--- | :--- |
| `log_id` | String | Unique log identifier | `"LOG-20260724-001"` |
| `timestamp` | String (ISO 8601) | Time of approval | `"2026-07-24T18:30:00Z"` |
| `member_name` | String | Extracted member name | `"Jane Doe"` |
| `discrepancy_flag` | Boolean | `True` if discrepancy detected | `True` / `False` |
| `flag_details` | String | Human-readable discrepancy note | `"Location mismatch: Requested TX, Recorded CA"` |
| `final_response` | String | Approved response draft | `"Dear Broker, Regarding Jane Doe..."` |
| `analyst_action` | String | Status of action | `"APPROVED"` |

---

## PRD User Story Mapping

- **Extraction (FR1-FR3)**: Maps to `member_name`, `dob`, and `state_location` lookups.
- **Compliance Logic (FR4-FR6)**: Compares extracted state/eligibility against `eligibility_status` and `state_location` in `mock_members.csv`.
- **Audit History (FR10)**: Every approved action appends a row to `audit_log.csv`.


#3. API.md

:markdown:

# API & Function Specifications

> **Note**: This application operates as a single-process Streamlit app. There are no external REST HTTP endpoints exposed in v1.0. All operations are direct, internal Python function calls.

## Internal Functions Breakdown

### 1. File & Text Parsing
- **Function**: `parse_email_file(uploaded_file)`
- **Module**: `extraction.py`
- **Purpose**: Extracts raw text content from uploaded `.txt` or `.eml` files.
- **Input**: Streamlit `UploadedFile` object.
- **Output**: `dict` containing `{"raw_text": str, "sender": str, "subject": str}`
- **Error Handling**: Returns clean error string if file format is unsupported or corrupted.

---

### 2. Field Extraction
- **Function**: `extract_entities(text)`
- **Module**: `extraction.py`
- **Purpose**: Uses regular expressions and text parsing to extract key entity fields.
- **Input**: `text` (String)
- **Output**: `dict` containing `{"member_name": str, "dob": str, "location": str, "query_type": str}`
- **Validation**: Fallback to `None` or `"Not Found"` if entity extraction fails.

---

### 3. Compliance Check
- **Function**: `check_eligibility(member_name, location)`
- **Module**: `compliance_check.py`
- **Purpose**: Checks extracted entities against `data/mock_members.csv`.
- **Input**: `member_name` (str), `location` (str)
- **Output**: `dict` containing `{"is_found": bool, "status": str, "has_discrepancy": bool, "flag_reason": str}`

---

### 4. AI Response Generation
- **Function**: `generate_draft_response(email_text, member_info, flags)`
- **Module**: `ai_drafting.py`
- **Purpose**: Calls Anthropic Claude API (`claude-3-5-sonnet` / `claude-3-haiku`) to draft empathetic, HIPAA-conscious replies.
- **Input**: Extracted fields, compliance status, and original email context.
- **Output**: `str` (Markdown response draft)
- **Error Handling**: Catches `anthropic.AuthenticationError` or API connection timeouts gracefully.

---

### 5. Audit Logging
- **Function**: `log_approval(log_data)`
- **Module**: `compliance_check.py` / `app.py`
- **Purpose**: Appends approval record to `data/audit_log.csv`.
- **Input**: `dict` matching `SCHEMA.md` audit log fields.
- **Output**: `bool` (`True` if successfully written).



4.# UI-WIREFRAMES.md

# UI & User Flow Design
## Interface Layout (Single Screen Streamlit App)
```text
+-----------------------------------------------------------------------------------+
|  🏥 AI-Powered Email & Benefits Query Assistant                                   |
+-----------------------------------------------------------------------------------+
|  [Sidebar]                                |  [Main Content Area]                  |
|  - App Status & Instructions              |                                       |
|  - EXPANDER: 📁 View Audit Logs          |  1. 📄 Email File Upload              |

| (Displays CSV table + Download button) | [ Browse Files (.txt/.eml) ] |
| :--- | :--- |
|  | 2. 🔍 Extracted Information |
|  | - Member Name: [ Jane Doe      ] |
|  | - Date of Birth: [ 1985-06-12  ] |
|  | - Location:    [ CA            ] |
| :--- | :--- |
|  | 3. ⚠️ Compliance & Eligibility Check |
|  | [ Alert Box: Active | Location  ] |
|  | [ Mismatch Flagged!            ] |
| :--- | :--- |
|  | 4. 📝 AI Drafted Reply |
|  | +-------------------------------+ |
|  |  | Editable Text Area |  |
|  |  | "Dear Broker, Regarding..." |  |
|  | +-------------------------------+ |
| :--- | :--- |
|  | [ ✅ Approve & Log Action Button ] |

+-----------------------------------------------------------------------------------+


#5. PROJECT-STRUCTURE.md

:markdown:

# Project Folder Structure

Below is the repository structure for the Streamlit application:

```text
benefits-email-assistant/
│
├── .streamlit/
│   └── secrets.toml          # Local storage for ANTHROPIC_API_KEY (git ignored)
│
├── data/
│   ├── mock_members.csv      # Mock member database (10-15 rows)
│   └── audit_log.csv         # Audit trail log (append-only)
│
├── docs/                     # System Design Deliverables
│   ├── ARCHITECTURE.md
│   ├── SCHEMA.md
│   ├── API.md
│   ├── UI-WIREFRAMES.md
│   └── PROJECT-STRUCTURE.md
│
├── app.py                    # Main Streamlit UI application
├── extraction.py             # Email parsing & entity extraction logic
├── compliance_check.py       # Rule-based eligibility matching & logger
├── ai_drafting.py            # Anthropic Claude API integration
│
├── requirements.txt          # Project dependencies (streamlit, anthropic, pandas)
├── .gitignore                # Ignores secrets, cache, and env files
└── README.md                 # Project overview and run instructions.
