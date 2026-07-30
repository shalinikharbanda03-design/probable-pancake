import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
"""
Rule-Based Eligibility & Location Engine
------------------------------------------
Pure deterministic Python logic. NO AI/LLM calls happen anywhere in this file.
This is what makes eligibility/location decisions auditable and compliance-safe.
"""

from datetime import datetime
from mock_data import get_member_by_name


def _parse_date(date_str):
    """Convert a YYYY-MM-DD string to a date object. Returns None if invalid/missing."""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return None


def check_member(extracted_fields: dict, get_member_fn=get_member_by_name) -> dict:
    """
    Takes extracted email fields (member_name, location, date) and checks them
    against the mock member dataset using deterministic rules only.

    Returns a dict:
    {
        "matched_record": <member dict or None>,
        "flags": [<list of flag strings>]
    }
    """
    flags = []
    member_name = extracted_fields.get("member_name")
    email_location = extracted_fields.get("location")
    email_date_str = extracted_fields.get("date")

    # Rule 1: Member not found
    if not member_name:
        flags.append("Member Name Missing")
        return {"matched_record": None, "flags": flags}

    matched_record = get_member_fn(member_name)

    if matched_record is None:
        flags.append("Member Not Found")
        return {"matched_record": None, "flags": flags}

    # Rule 2: Location mismatch (only checked if email provided a location)
    if email_location:
        if email_location.strip().upper() != matched_record.get("location", "").strip().upper():
            flags.append("Location Mismatch")

    # Rule 3: Date outside eligibility window (only checked if email provided a date)
    if email_date_str:
        email_date = _parse_date(_normalize_date_str(email_date_str))
        start_date = _parse_date(matched_record.get("eligibility_start"))
        end_date = _parse_date(matched_record.get("eligibility_end"))

        if email_date and start_date and end_date:
            if email_date < start_date or email_date > end_date:
                flags.append("Outside Eligibility Window")
        elif email_date is None:
            flags.append("Date Could Not Be Parsed")

    # Rule 4: Plan status check
    plan_status = matched_record.get("plan_status", "").strip().lower()
    if plan_status == "inactive":
        flags.append("Plan Inactive")
    elif plan_status == "pending":
        flags.append("Plan Pending")

    # Also honor the existing simple `eligible` boolean flag as a safety net
    if matched_record.get("eligible") is False and "Plan Inactive" not in flags:
        flags.append("Marked Not Eligible")

    return {"matched_record": matched_record, "flags": flags}


def _normalize_date_str(date_str: str) -> str:
    """
    Converts common date formats (e.g., MM/DD/YYYY) into YYYY-MM-DD.
    Returns the original string if it's already in YYYY-MM-DD format or unrecognized.
    """
    if not date_str:
        return date_str

    # Already in YYYY-MM-DD format
    if len(date_str) == 10 and date_str[4] == "-" and date_str[7] == "-":
        return date_str

    # Try MM/DD/YYYY format
    if "/" in date_str:
        parts = date_str.split("/")
        if len(parts) == 3:
            month, day, year = parts
            try:
                return f"{int(year):04d}-{int(month):02d}-{int(day):02d}"
            except ValueError:
                return date_str

    return date_str
