import re

def parse_email_text(email_text: str) -> dict:
    """
    Extracts key information like Member Name, Date, and Location from raw email query.
    """
    extracted_data = {
        "member_name": None,
        "date": None,
        "location": None,
        "raw_text": email_text
    }

    # Regex pattern for Name extraction (stops at end of line, not across lines)
    name_match = re.search(r'(?:Name|Member):\s*([A-Za-z\s]+?)(?:\n|$)', email_text, re.IGNORECASE)
    if name_match:
        extracted_data["member_name"] = name_match.group(1).strip()

    # Regex pattern for Location extraction
    location_match = re.search(r'(?:Location|State):\s*([A-Za-z]{2,})', email_text, re.IGNORECASE)
    if location_match:
        extracted_data["location"] = location_match.group(1).strip()

    # Regex pattern for Date extraction
    date_match = re.search(r'\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2}/\d{1,2}/\d{4}\b', email_text)
    if date_match:
        extracted_data["date"] = date_match.group(0)

    return extracted_data
