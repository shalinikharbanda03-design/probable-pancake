import streamlit as st
import pandas as pd
from extraction import parse_email_text
from mock_data import get_member_by_name
from rules_engine import check_member

st.set_page_config(page_title="Day 55: Rule Engine Integration", layout="wide")

st.title("⚡ AI-Powered Email Query Assistant - Rule Engine")
st.caption("Demo data only — no real PHI, no real email integration.")

st.sidebar.header("Input Panel")
email_input = st.sidebar.text_area(
    "Paste Email Query Here:",
    value="Member: Alice Smith\nLocation: NY\nDate: 2026-07-27"
)

if st.sidebar.button("Run Processing Pipeline"):
    st.subheader("1. Extraction Output")
    extracted_data = parse_email_text(email_input)
    st.json(extracted_data)

    st.subheader("2. Eligibility & Location Check (Rule-Based)")
    check_result = check_member(extracted_data)
    matched_record = check_result["matched_record"]
    flags = check_result["flags"]

    if not flags:
        st.success("No issues found. Member is eligible and details match.")
    else:
        for flag in flags:
            if flag in ("Member Not Found", "Member Name Missing"):
                st.error(f"🚫 {flag}")
            else:
                st.warning(f"⚠️ {flag}")

    if matched_record:
        st.subheader("3. Matched Member Record")
        st.json(matched_record)
    else:
        st.info("No matching member record to display.")

    st.subheader("4. Real-Time Execution Log")
    log_df = pd.DataFrame([
        {"Step": "Parsing", "Status": "Complete"},
        {"Step": "Database Match", "Status": "Complete" if matched_record else "Not Found"},
        {"Step": "Rule Checks", "Status": f"{len(flags)} flag(s) raised" if flags else "No flags"},
    ])
    st.dataframe(log_df)
