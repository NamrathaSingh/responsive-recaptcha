from app.services.outreach import generate_note


def test_generate_note_length_and_channel():
    result = generate_note("hiring_manager", "Asha", "Acme", "cloud platform scaling")
    assert len(result["note"]) <= 600
    assert result["channel"] in {"linkedin", "email"}
