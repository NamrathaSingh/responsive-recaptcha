import re

TARGET_DOMAINS = ["cloud", "security", "platform", "dbaas", "ai", "developer tools", "enterprise"]
TARGET_ROLES = ["director", "staff", "engineering operations", "tpm", "chief of staff", "release"]


def _keyword_hits(text: str, keywords: list[str]) -> int:
    text = text.lower()
    return sum(1 for kw in keywords if kw in text)


def score_company(profile: dict) -> dict:
    text = " ".join(str(v) for v in profile.values() if v)
    domain = min(100, _keyword_hits(text, TARGET_DOMAINS) * 24)
    india = 100 if re.search(r"india|bangalore|remote", text, re.I) else 40
    investor = 90 if re.search(r"sequoia|accel|lightspeed|bessemer|insight|index|greylock|battery|peak xv|a16z", text, re.I) else 45
    hiring = 85 if re.search(r"hiring|open role|growing|scale", text, re.I) else 50
    fit = round((domain * 0.3) + (india * 0.2) + (investor * 0.3) + (hiring * 0.2), 2)
    return {
        "company_fit": fit,
        "domain_fit": domain,
        "india_bangalore_fit": india,
    }


def score_role(jd_text: str, title: str) -> dict:
    text = f"{title} {jd_text}".lower()
    role_fit = min(100, _keyword_hits(text, TARGET_ROLES) * 26)
    seniority = 95 if re.search(r"director|staff|principal|head", text) else 55
    domain = min(100, _keyword_hits(text, TARGET_DOMAINS) * 20)
    priority = round(role_fit * 0.35 + seniority * 0.25 + domain * 0.2 + 20, 2)
    return {
        "role_fit": round(role_fit, 2),
        "seniority_fit": seniority,
        "domain_fit": round(domain, 2),
        "outreach_priority": min(priority, 100),
    }
