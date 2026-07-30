import os

def call_claude_draft(extracted_fields: dict, flags: list, matched_record: dict = None) -> str:
    """
    Generates an empathetic, professional email reply draft based on extracted facts
    and deterministic rule engine flags.
    """
    member_name = extracted_fields.get("member_name") or "Valued Member"
    location = extracted_fields.get("location") or "Unknown Location"
    raw_intent = extracted_fields.get("raw_intent_summary") or "Inquiry regarding benefits"

    flags_text = ", ".join(flags) if flags else "No issues identified. Fully eligible."
    
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if api_key:
        try:
            import anthropic
            client = anthropic.Anthropic(api_key=api_key)
            
            prompt = f"""You are an expert customer benefits support specialist.
Draft a concise, professional, and empathetic email response based strictly on these details:

- Member Name: {member_name}
- Extracted Intent: {raw_intent}
- Compliance Flags Identified (Ground Truth): {flags_text}
- Database Record Matched: {matched_record if matched_record else 'None'}

Instructions:
1. Treat the compliance flags as absolute ground truth. Do not override or question them.
2. Maintain a HIPAA-conscious, polite, and reassuring tone.
3. Keep the email concise and clear.
4. Include a courteous closing offering further support.
"""

            response = client.messages.create(
                model="claude-3-haiku-20240307",
                max_tokens=500,
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()
        except Exception as e:
            pass

    # Deterministic Local Fallback Generator (Ensures 100% working MVP without API reliance)
    if "Member Not Found" in flags:
        status_msg = "we were unable to locate your active profile in our immediate system records."
    elif "Location Mismatch" in flags:
        status_msg = f"our records indicate a location mismatch regarding {location}."
    elif "Outside Eligibility Window" in flags:
        status_msg = "your current coverage window appears to be outside active eligibility dates."
    elif "Plan Inactive/Pending" in flags:
        status_msg = "your plan status is currently flagged as Inactive or Pending."
    else:
        status_msg = "your benefits and eligibility status are active and verified."

    fallback_draft = f"""Dear {member_name},

Thank you for reaching out to us regarding your inquiry ({raw_intent}).

Upon reviewing your account details, {status_msg} 

If you believe this is an error or if you have updated documentation to provide, please reply directly to this message so our team can assist you further.

Best regards,
Benefits Support Team
    """.strip()

    return fallback_draft
    
