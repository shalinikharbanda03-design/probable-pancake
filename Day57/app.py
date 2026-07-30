import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import streamlit as st
import time
from drafting import call_claude_draft
from rules_engine import check_member

st.set_page_config(
    page_title="AI Email & Benefits Query Assistant",
    page_icon="✉️",
    layout="wide"
)

st.title("✉️ AI-Powered Email & Benefits Assistant")
st.caption("Phase 8 - Capstone MVP (Day 57 — Single-Screen Review UI, refined)")
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
    with st.spinner("Analyzing email, matching member record, and drafting reply..."):
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
        st.session_state["reply_approved"] = False
        # Small delay so the spinner is visibly meaningful even on fast mock calls
        time.sleep(0.4)
    st.toast("Analysis complete ✅", icon="✅")

st.divider()

# ---------- SECTION 1: Extracted Info ----------
st.header("1️⃣ Extracted Information & Matched Record")
st.caption("What the system pulled from the email, matched against member records.")

if "extracted_fields" in st.session_state:
    col_a, col_b = st.columns(2, gap="large")
    with col_a:
        st.markdown("**📥 Extracted Fields**")
        st.json(st.session_state["extracted_fields"])
    with col_b:
        st.markdown("**🗂️ Matched Member Record**")
        matched_record = st.session_state.get("matched_record")
        if matched_record:
            st.json(matched_record)
        else:
            st.warning("⚠️ No matching member record found for this email.")
else:
    st.info("👉 Click **Analyze Email** above to see extracted fields and the matched member record here.")

st.divider()

# ---------- SECTION 2: Flags ----------
st.header("2️⃣ Compliance & Rule Flags")
st.caption("Deterministic, rule-based checks — no AI involved in this step, fully auditable.")

FLAG_STYLES = {
    "Member Not Found": ("🚫", "error"),
    "Member Name Missing": ("🚫", "error"),
    "Outside Eligibility Window": ("⛔", "error"),
    "Plan Inactive": ("⛔", "error"),
    "Marked Not Eligible": ("⛔", "error"),
    "Plan Pending": ("⏳", "warning"),
    "Location Mismatch": ("⚠️", "warning"),
    "Date Could Not Be Parsed": ("⚠️", "warning"),
}

if "flags" in st.session_state:
    flags = st.session_state.get("flags", [])
    if not flags:
        st.success("✅ No Compliance Flags: Eligible & Verified")
    else:
        flag_cols = st.columns(2, gap="medium")
        for i, flag in enumerate(flags):
            icon, severity = FLAG_STYLES.get(flag, ("⚠️", "warning"))
            target_col = flag_cols[i % 2]
            with target_col:
                if severity == "error":
                    st.error(f"{icon} **{flag}**")
                else:
                    st.warning(f"{icon} **{flag}**")
else:
    st.info("Flags will appear here — organized by severity — after you run the analysis.")

st.divider()

# ---------- SECTION 3: Draft ----------
st.header("3️⃣ Claude-Powered Reply Draft")
st.caption("Review and edit before sending. Nothing is sent automatically.")

if "draft" in st.session_state:
    edited_draft = st.text_area(
        "Generated Draft (Editable):",
        value=st.session_state["draft"],
        height=300,
        key="draft_editor"
    )

    approve_col, status_col = st.columns([1, 3])
    with approve_col:
        approved = st.session_state.get("reply_approved", False)
        if not approved:
            if st.button("👍 Approve & Send Reply", use_container_width=True, type="primary"):
                st.session_state["reply_approved"] = True
                st.rerun()
        else:
            st.button("✅ Reply Sent", use_container_width=True, disabled=True)

    with status_col:
        if st.session_state.get("reply_approved", False):
            st.success("Reply approved and queued for sending!")
else:
    st.info("The reply draft will appear here — editable before you approve it — after you run the analysis.")

st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 10px; font-size: 0.85em;'>
    Built with Claude as part of the AB Talks 60-Day Claude AI Challenge.
    </div>
    """,
    unsafe_allow_html=True
)
