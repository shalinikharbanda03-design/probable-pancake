"""
Standalone tests for rules_engine.py — no Streamlit, no AI, no external dependencies.
Run with: python test_rules_engine.py
"""

from rules_engine import check_member

# A tiny in-memory dataset used only for these tests, so they don't depend on
# mock_data.py changing in the future.
TEST_MEMBERS = {
    "active member": {
        "member_id": "T1", "name": "Active Member", "eligible": True,
        "location": "NY", "plan_status": "Active",
        "eligibility_start": "2025-01-01", "eligibility_end": "2026-12-31"
    },
    "inactive member": {
        "member_id": "T2", "name": "Inactive Member", "eligible": False,
        "location": "CA", "plan_status": "Inactive",
        "eligibility_start": "2023-01-01", "eligibility_end": "2024-12-31"
    },
}


def fake_get_member(name):
    return TEST_MEMBERS.get(name.lower())


def run_test(description, extracted_fields, expected_flags):
    result = check_member(extracted_fields, get_member_fn=fake_get_member)
    actual_flags = result["flags"]
    passed = set(actual_flags) == set(expected_flags)
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {description}")
    if not passed:
        print(f"    Expected: {expected_flags}")
        print(f"    Actual:   {actual_flags}")
    return passed


def main():
    results = []

    results.append(run_test(
        "Member not found",
        {"member_name": "Nobody Here", "location": None, "date": None},
        ["Member Not Found"]
    ))

    results.append(run_test(
        "Member name missing entirely",
        {"member_name": None, "location": "NY", "date": None},
        ["Member Name Missing"]
    ))

    results.append(run_test(
        "Perfect match, no issues",
        {"member_name": "Active Member", "location": "NY", "date": "2025-06-01"},
        []
    ))

    results.append(run_test(
        "Location mismatch",
        {"member_name": "Active Member", "location": "TX", "date": None},
        ["Location Mismatch"]
    ))

    results.append(run_test(
        "Date outside eligibility window",
        {"member_name": "Active Member", "location": "NY", "date": "2027-01-01"},
        ["Outside Eligibility Window"]
    ))

    results.append(run_test(
        "Inactive plan flagged",
        {"member_name": "Inactive Member", "location": "CA", "date": None},
        ["Plan Inactive", "Marked Not Eligible"]
    ))

    total = len(results)
    passed = sum(results)
    print(f"\n{passed}/{total} tests passed.")


if __name__ == "__main__":
    main()
