import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import streamlit as st
import time
import csv
from datetime import datetime, timezone
from drafting import call_claude_draft
from rules_engine import check_member

st.set_page_config(
    page_title="AI Email & Benefits Query Assistant",
    page_icon="✉️",
    layout="wide"
)

# ---------- CSV AUDIT LOG SETUP ----------
LOG_DIR = os.path.abspath(os.path.dirname(__file__))
LOG_PATH = os.path.join(LOG_DIR, "audit_log.csv")
LOG_FIELDS = [
    "timestamp_utc",
    "member_name",
    "member_id",
    "email_location",
    "matched_location",
    "plan_type",
    "plan_status",
    "flags",
    "final_draft",
]


def ensure_log_file_exists():
    """Create the CSV log file with headers if it doesn't exist yet."""
    try:
        if not os.path.exists(LOG_PATH):
            with open(LOG_PATH, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=LOG_FIELDS)
                writer.writeheader()
        return True
    except OSError as e:
        st.error(f"⚠️ Could not create audit log file: {e}")
        return False


def append_log_row(extracted_fields, matched_record, flags, final_draft):
    """Append one approved-reply row to the CSV audit log. Returns True on success."""
    if not ensure_log_file_exists():
        return False
    try:
        matched_record = matched_record or {}
        row = {
            "timestamp_utc": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "member_name": extracted_fields.get("member_name", ""),
            "member_id": matched_record.get("member_id", ""),
            "email_location": extracted_fields.get("location", ""),
            "matched_location": matched_record.get("location", ""),
            "plan_type": matched_record.get("plan_type", ""),
            "plan_status": matched_record.get("plan_status", ""),
            "flags": "; ".join(flags) if flags else "None",
            "final_draft": (final_draft or "").replace("\n", " ").strip(),
        }
        with open(LOG_PATH, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=LOG_FIELDS)
            writer.writerow(row)
        return True
    except OSError as e:
        st.error(f"⚠️ Could not write to audit log: {e}")
        return False


def read_recent_log_rows(limit=5):
    """Read the last N rows from the audit log, most recent first. Returns [] on any issue."""
    if not os.path.exists(LOG_PATH):
        return []
    try:
        with open(LOG_PATH, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        return list(reversed(rows))[:limit]
    except OSError:
        return []


def safe_call_claude_draft(extracted_fields, flags, matched_record):
    """
    Wraps the Claude drafting call so a failure (API error, timeout, etc.)
    never crashes the app — instead we fall back to a clear, honest message
    that a human reviewer must handle manually.
    """
    try:
        draft = call_claude_draft(extracted_fields, flags, matched_record)
        if not draft or not isinstance(draft, str) or not draft.strip():
            raise ValueError("Empty draft returned")
        return draft, None
    except Exception as e:
        fallback = (
            "⚠️ Draft generation failed. Please write a manual reply.\n\n"
            f"(Reason: {type(e).__name__} — see logs for details.)"
        )
        return fallback, str(e)


def reset_analysis_state():
    """Clears all analysis-related session state so the user can start fresh."""
    for key in ["extracted_fields", "flags", "matched_record", "draft",
                "reply_approved", "draft_editor"]:
        st.session_state.pop(key, None)


st.title("✉️ AI-Powered Email & Benefits Assistant")
st.caption("Phase 8 - Capstone MVP (Day 59 — Error Handling, Polish & Edge Cases)")
st.divider()

with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("System operating in Free-Tier Mode with deterministic fallbacks.")
    st.warning(
        "🧪 **Demo mode:** extraction is simulated for this MVP. The text below "
        "is for reference only — the analysis always uses a fixed sample "
        "member (John Doe) regardless of what's typed here. Live extraction "
        "from real email text is planned for a future iteration."
    )
    st.markdown("---")
    st.markdown("### 📋 Sample Input Data")
    sample_email = st.text_area(
        "Paste Raw Email Text:",
        height=200,
        value="Hi, my name is John Doe from New York. I want to check my health coverage eligibility for next month."
    )
    if not sample_email or not sample_email.strip():
        st.caption("⚠️ Email text is empty — analysis will still run using the simulated sample member.")

col_run, col_reset = st.columns([3, 1])
with col_run:
    st.subheader("🚀 Run Analysis")
with col_reset:
    st.write("")
    if st.button("🔄 Start New Analysis", use_container_width=True):
        reset_analysis_state()
        st.rerun()

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

        try:
            result = check_member(extracted_fields)
            flags = result.get("flags", [])
            matched_record = result.get("matched_record")
        except Exception as e:
            flags = ["System Error During Eligibility Check"]
            matched_record = None
            st.error(f"⚠️ The rule engine encountered an unexpected error: {e}")

        st.session_state["flags"] = flags
        st.session_state["matched_record"] = matched_record

        draft, draft_error = safe_call_claude_draft(extracted_fields, flags, matched_record)
        st.session_state["draft"] = draft
        st.session_state["reply_approved"] = False
        if draft_error:
            st.error("⚠️ Reply drafting failed — a fallback message has been inserted below. "
                      "Please review Section 3 and write the reply manually.")
        time.sleep(0.3)
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
            st.warning("⚠️ No matching member record found for this email. "
                       "A human reviewer should verify member identity manually before responding.")
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
    "System Error During Eligibility Check": ("🛑", "error"),
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
    draft_text = st.session_state["draft"]
    edited_draft = st.text_area(
        "Generated Draft (Editable):",
        value=draft_text,
        height=300,
        key="draft_editor",
        max_chars=5000,
    )
    char_count = len(st.session_state.get("draft_editor", draft_text) or "")
    st.caption(f"📝 {char_count} / 5000 characters")

    is_fallback_draft = draft_text.startswith("⚠️ Draft generation failed")

    approve_col, status_col = st.columns([1, 3])
    with approve_col:
        approved = st.session_state.get("reply_approved", False)
        if not approved:
            approve_disabled = is_fallback_draft and not (
                st.session_state.get("draft_editor", "") or ""
            ).strip()
            if st.button(
                "👍 Approve & Send Reply",
                use_container_width=True,
                type="primary",
                disabled=approve_disabled,
            ):
                final_draft_text = st.session_state.get("draft_editor", draft_text)
                if not final_draft_text or not final_draft_text.strip():
                    st.error("⚠️ Cannot approve an empty reply. Please write or edit the draft first.")
                else:
                    with st.spinner("Recording approval in the audit log..."):
                        success = append_log_row(
                            extracted_fields=st.session_state.get("extracted_fields", {}),
                            matched_record=st.session_state.get("matched_record"),
                            flags=st.session_state.get("flags", []),
                            final_draft=final_draft_text,
                        )
                    if success:
                        st.session_state["reply_approved"] = True
                        st.rerun()
            if is_fallback_draft:
                st.caption("✏️ Please replace the fallback text above before approving.")
        else:
            st.button("✅ Reply Sent & Logged", use_container_width=True, disabled=True)

    with status_col:
        if st.session_state.get("reply_approved", False):
            st.success("Reply approved, queued for sending, and recorded in the audit log!")
else:
    st.info("The reply draft will appear here — editable before you approve it — after you run the analysis.")

st.divider()

# ---------- SECTION 4: Recent Approvals (Audit Log) ----------
st.header("4️⃣ Recent Approvals (Audit Log)")
st.caption("Last 5 approved replies, read from the CSV audit trail — for compliance review.")

recent_rows = read_recent_log_rows(limit=5)
if recent_rows:
    display_rows = []
    for r in recent_rows:
        display_rows.append({
            "Time (UTC)": r.get("timestamp_utc", ""),
            "Member": r.get("member_name", ""),
            "Member ID": r.get("member_id", ""),
            "Plan": f"{r.get('plan_type', '')} ({r.get('plan_status', '')})",
            "Flags": r.get("flags", ""),
        })
    st.dataframe(display_rows, use_container_width=True, hide_index=True)
    if os.path.exists(LOG_PATH):
        try:
            with open(LOG_PATH, "rb") as f:
                csv_bytes = f.read()
            st.download_button(
                "⬇️ Download Full Audit Log (CSV)",
                data=csv_bytes,
                file_name="audit_log.csv",
                mime="text/csv",
            )
        except OSError:
            st.caption("⚠️ Audit log file could not be read for download right now.")
else:
    st.info("No approvals logged yet. Once you approve a reply above, it will appear here.")

st.divider()
st.markdown(
    """
    <div style='text-align: center; color: gray; padding: 10px; font-size: 0.85em;'>
    Built with Claude as part of the AB Talks 60-Day Claude AI Challenge.
    </div>
    """,
    unsafe_allow_html=True
)
