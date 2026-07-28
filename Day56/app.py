import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import pandas as pd
import json


from rules_engine import check_member_eligibility
from drafting import call_claude_draft


st.set_page_config(
    page_title="AI Email & Benefits Query Assistant",
    page_icon="✉️",
    layout="wide"
)

st.title("✉️ AI-Powered Email & Benefits Assistant")
st.caption("Phase 8 - Capstone MVP (Day 56)")

st.divider()

# Sidebar Setup
with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("System operating in Free-Tier Mode with deterministic fallbacks.")
    
    st.markdown("---")
    st.markdown("### 📋 Sample Input Data")
    sample_email = st.text_area(
        "Paste Raw Email Text:",
        height=200,
        value="Hi, my name is John Doe from New York. I want to check my health coverage eligibility for next month."
    )

# Create Mock Data DataFrame for testing
mock_df = pd.DataFrame([
    {
        "member_name": "John Doe",
        "location": "New York",
        "eligibility_start": "2026-01-01",
        "eligibility_end": "2026-12-31",
        "plan_status": "Active"
    },
    {
        "member_name": "Jane Smith",
        "location": "California",
        "eligibility_start": "2025-01-01",
        "eligibility_end": "2025-12-31",
        "plan_status": "Inactive"
    }
])

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Extracted Information & Analysis")
    if st.button("🚀 Process & Analyze Email", type="primary"):
        # Simulated/Extracted fields
        extracted_fields = {
            "member_name": "John Doe",
            "location": "New York",
            "dates": ["2026-08-01"],
            "raw_intent_summary": "Inquiring about health coverage eligibility for next month."
        }
        
        st.session_state["extracted_fields"] = extracted_fields
        
        # Run Rule Engine
        flags, matched_record = check_member_eligibility(extracted_fields, mock_df)
        st.session_state["flags"] = flags
        st.session_state["matched_record"] = matched_record
        
        # Generate Reply Draft
        draft = call_claude_draft(extracted_fields, flags, matched_record)
        st.session_state["draft"] = draft

    if "extracted_fields" in st.session_state:
        st.json(st.session_state["extracted_fields"])
        
        st.subheader("2. Compliance & Rule Flags")
        flags = st.session_state.get("flags", [])
        if not flags:
            st.success("✅ No Compliance Flags: Eligible & Verified")
        else:
            for flag in flags:
                st.warning(f"⚠️ Flag: {flag}")

with col2:
    st.subheader("3. Claude-Powered Reply Draft")
    if "draft" in st.session_state:
        edited_draft = st.text_area("Generated Draft (Editable):", value=st.session_state["draft"], height=300)
        
        if st.button("👍 Approve & Send Reply"):
            st.success("Reply approved and queued for sending!")

# MANDATORY FOOTER (As required by Day 56 prompt)
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray; padding: 10px;'>"
    "Built with Claude as part of the AB Talks 60-Day Claude AI Challenge."
    "</div>", 
    unsafe_allow_html=True
)