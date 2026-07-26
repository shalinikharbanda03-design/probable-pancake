---

### 📄 File 2: `SCHEMA.md`

```markdown
# Database & Data Schema

The system uses local CSV files managed via `pandas` to maintain a lightweight, zero-database setup consistent with rapid prototyping goals.

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

## 2. Audit Log Dataset (`data/audit_log.csv`)
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
* **Extraction (FR1-FR3):** Maps to `member_name`, `dob`, and `state_location` lookups.
* **Compliance Logic (FR4-FR6):** Compares extracted state/eligibility against `eligibility_status` and `state_location`.
* **Audit History (FR10):** Every approved action appends a row to `audit_log.csv`.
