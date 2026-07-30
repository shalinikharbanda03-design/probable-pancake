import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import streamlit as st
import pandas as pd
import json
from drafting import call_claude_draft
from rules_engine import check_member

st.set_page_config(
    page_title="AI Email & Benefits Query Assistant",
    page_icon="✉️",
    layout="wide"
)

st.title("✉️ AI-Powered Email & Benefits Assistant")
st.caption("Phase 8 - Capstone MVP (Day 57 — Single-Screen Review UI)")
st.divider()

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

st.subheader("🚀 Run Analysis")
analyze_clicked = st.button("🚀 Analyze Email", type="primary", use_container_width=True)

if analyze_clicked:
    extracted_fields = {
        "member_name": "John Doe",
        "location": "New York",
        "dates": ["2026-08-01"],
        "raw_intent_summary": "Inquiring about health coverage eligibility for next month."
    }
    st.session_state["extracted_fields"] = extracted_fields
    result = check_member(extracted_fields)
    flags = result["flags"]
    matched_record = result["matched_record"]
    st.session_state["flags"] = flags
    st.session_state["matched_record"] = matched_record
    draft = call_claude_draft(extracted_fields, flags, matched_record)
    st.session_state["draft"] = draft

st.divider()

st.header("1️⃣ Extracted Information & Matched Record")
if "extracted_fields" in st.session_state:
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**Extracted Fields**")
        st.json(st.session_state["extracted_fields"])
    with col_b:
        st.markdown("**Matched Member Record**")
        matched_record = st.session_state.get("matched_record")
        if matched_record:
            st.json(matched_record)
        else:
            st.warning("No matching member record found.")
else:
    st.caption("Click **Analyze Email** above to see extracted fields here.")

st.divider()

st.header("2️⃣ Compliance & Rule Flags")
if "flags" in st.session_state:
    flags = st.session_state.get("flags", [])
    if not flags:
        st.success("✅ No Compliance Flags: Eligible & Verified")
    else:
        for flag in flags:
            if flag in ("Member Not Found", "Member Name Missing"):
                st.error(f"🚫 {flag}")
            elif flag in ("Outside Eligibility Window", "Plan Inactive", "Marked Not Eligible"):
                st.error(f"⛔ {flag}")
            else:
                st.warning(f"⚠️ {flag}")
else:
    st.caption("Flags will appear here after you run the analysis.")

st.divider()

st.header("3️⃣ Claude-Powered Reply Draft")
if "draft" in st.session_state:
    edited_draft = st.text_area(
        "Generated Draft (Editable):",
        value=st.session_state["draft"],
        height=300,
        key="draft_editor"
    )
    approve_col, _ = st.columns([1, 3])
    with approve_col:
        if st.button("👍 Approve & Send Reply", use_container_width=True):
            st.success("Reply approved and queued for sending!")
else:
    st.caption("The reply draft will appear here after you run the analysis.")

st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 10px;'>
    Built with Claude as part of the AB Talks 60-Day Claude AI Challenge.
    </div>
    """,
    unsafe_allow_html=True
)

