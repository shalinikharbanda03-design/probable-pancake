---

### 📄 File 5: `PROJECT-STRUCTURE.md`

```markdown
# Project Folder Structure

Below is the repository structure for the Streamlit application:

```text
benefits-email-assistant/
├── .streamlit/
│   └── secrets.toml          # Local storage for ANTHROPIC_API_KEY (git ignored)
├── data/
│   ├── mock_members.csv      # Mock member database (10-15 rows)
│   └── audit_log.csv         # Audit trail log (append-only)
├── docs/
│   ├── ARCHITECTURE.md       # System Design Deliverables
│   ├── SCHEMA.md
│   ├── API.md
│   ├── UI-WIREFRAMES.md
│   └── PROJECT-STRUCTURE.md
├── app.py                    # Main Streamlit UI application
├── extraction.py             # Email parsing & entity extraction logic
├── compliance_check.py       # Rule-based eligibility matching & logger
├── ai_drafting.py            # Anthropic Claude API integration
├── requirements.txt          # Project dependencies (streamlit, anthropic, pandas)
├── .gitignore                # Ignores secrets, cache, and env files
└── README.md                 # Project overview and run instructions.
