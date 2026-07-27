import streamlit as st
import pandas as pd
from extraction import parse_email_text
from mock_data import get_member_by_name
from rules_engine import check_member

st.set_page_config(page_title="Rule Engine", layout="wide")
st.title("Email Query Assistant - Rule Engine")

email_input = st.sidebar.text_area("Paste Email:", value="Member: Alice Smith\nLocation: NY\nDate: 2026-07-27")

if st.sidebar.button("Run Pipeline"):
    st.subheader("1. Extraction")
    extracted_data = parse_email_text(email_input)
    st.json(extracted_data)

    st.subheader("2. Rule Checks")
    result = check_member(extracted_data)
    flags = result["flags"]
    matched = result["matched_record"]

    if not flags:
        st.success("No issues found.")
    else:
        for f in flags:
            st.warning(f)

    if matched:
        st.subheader("3. Matched Record")
        st.json(matched)
        