from app.services.scoring import score_company, score_role


def test_company_scoring_prioritizes_target_signals():
    result = score_company({
        "sector": "cloud security platform",
        "india_presence": "Bangalore remote",
        "investors": "Sequoia and Accel",
        "hiring_signal": "growing and hiring"
    })
    assert result["company_fit"] >= 80


def test_role_scoring_matches_director_tpm():
    result = score_role("Director of TPM for cloud platform AI infrastructure", "Director TPM")
    assert result["role_fit"] >= 50
    assert result["seniority_fit"] >= 90
