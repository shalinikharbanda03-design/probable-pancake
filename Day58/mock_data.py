"""
Mock Dataset for Member Eligibility and Location Verification
"""

MOCK_MEMBERS = [
    {
        "member_id": "MEM101",
        "name": "Alice Smith",
        "eligible": True,
        "location": "NY",
        "plan_type": "Gold",
        "plan_status": "Active",
        "eligibility_start": "2025-01-01",
        "eligibility_end": "2026-12-31"
    },
    {
        "member_id": "MEM102",
        "name": "Bob Jones",
        "eligible": False,
        "location": "CA",
        "plan_type": "Silver",
        "plan_status": "Inactive",
        "eligibility_start": "2023-01-01",
        "eligibility_end": "2024-12-31"
    },
    {
        "member_id": "MEM103",
        "name": "Charlie Brown",
        "eligible": True,
        "location": "TX",
        "plan_type": "Platinum",
        "plan_status": "Active",
        "eligibility_start": "2025-06-01",
        "eligibility_end": "2026-06-01"
    },
    {
        "member_id": "MEM104",
        "name": "Diana Prince",
        "eligible": True,
        "location": "FL",
        "plan_type": "Gold",
        "plan_status": "Pending",
        "eligibility_start": "2026-08-01",
        "eligibility_end": "2027-08-01"
    },
    {
        "member_id": "MEM105",
        "name": "John Doe",
        "eligible": True,
        "location": "New York",
        "plan_type": "Gold",
        "plan_status": "Active",
        "eligibility_start": "2026-01-01",
        "eligibility_end": "2026-12-31"
    }
]

def get_member_by_name(name):
    """Fetch member details by name (case-insensitive search)."""
    for member in MOCK_MEMBERS:
        if member["name"].lower() == name.lower():
            return member
    return None
  
