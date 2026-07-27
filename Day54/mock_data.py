# Mock Dataset for Member Eligibility and Location Verification

MOCK_MEMBERS = [
    {
        "member_id": "MEM101",
        "name": "Alice Smith",
        "eligible": True,
        "location": "NY",
        "plan_type": "Gold"
    },
    {
        "member_id": "MEM102",
        "name": "Bob Jones",
        "eligible": False,
        "location": "CA",
        "plan_type": "Silver"
    },
    {
        "member_id": "MEM103",
        "name": "Charlie Brown",
        "eligible": True,
        "location": "TX",
        "plan_type": "Platinum"
    },
    {
        "member_id": "MEM104",
        "name": "Diana Prince",
        "eligible": True,
        "location": "FL",
        "plan_type": "Gold"
    }
]

def get_member_by_name(name):
    """Fetch member details by name (case-insensitive search)."""
    for member in MOCK_MEMBERS:
        if member["name"].lower() == name.lower():
            return member
    return None
