TEMPLATES = {
    "referral": "Hi {name}, I’m looking at {company} because the work maps to my background in engineering operations and release governance. If this seems relevant, would you be open to pointing me to the right hiring team?",
    "hiring_manager": "Hi {name}, I noticed {company} is scaling in this area. I build engineering operating systems across release governance, execution visibility, and AI-assisted workflows. Would you be open to a short guidance conversation?",
    "recruiter": "Hi {name}, I’m targeting Sr. Staff / Director roles in Engineering Operations, TPM, and AI-enabled execution. My background spans Nutanix, Google Cloud, Walmart, and security/cloud platforms. Useful if I share a concise profile?",
    "warm_reconnect": "Hi {name}, great to reconnect. I’m focusing on senior engineering operations and TPM leadership roles where execution structure matters. If helpful, I can share a crisp update and get your directional advice.",
    "investor_operator": "Hi {name}, not asking for a job—asking for direction. Based on your operator/investor lens, which teams need stronger engineering execution systems right now?",
    "follow_up": "Hi {name}, quick follow-up in case this got buried. Happy to share a concise profile if useful, and no worries if timing is off.",
    "direction": "Hi {name}, not asking for a role directly. I’d value your perspective on where a leader with deep release governance and AI-enabled operating cadence can create the most leverage."
}


def generate_note(note_type: str, recipient_name: str, company: str, context: str = "") -> dict:
    base = TEMPLATES.get(note_type, TEMPLATES["direction"])
    note = base.format(name=recipient_name, company=company)
    if context:
        note = f"{note} Context: {context[:120]}"
    return {
        "note": note[:600],
        "channel": "linkedin" if len(note.split()) < 115 else "email"
    }
