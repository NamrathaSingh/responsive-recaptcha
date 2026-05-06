from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.db import get_db
from app.models.entities import Company, Person, Resume, Role
from app.models.schemas import CompanyIn, OutreachRequest, ProfileIntelligenceRequest, ResumeMatchRequest, RoleMatchRequest
from app.services.outreach import generate_note
from app.services.scoring import score_company, score_role

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/companies")
def add_company(payload: CompanyIn, db: Session = Depends(get_db)):
    scores = score_company(payload.model_dump())
    company = Company(**payload.model_dump(), company_fit=scores["company_fit"])
    db.add(company)
    db.commit()
    db.refresh(company)
    return {"id": company.id, "scores": scores}


@router.post("/roles/match")
def match_role(payload: RoleMatchRequest):
    return score_role(payload.jd_text, payload.title)


@router.post("/people/intel")
def profile_intel(payload: ProfileIntelligenceRequest, db: Session = Depends(get_db)):
    text = payload.profile_text.lower()
    classification = "peer / weak signal"
    if "recruit" in text:
        classification = "recruiter"
    elif "hiring manager" in text or "vp engineering" in text or "director" in text:
        classification = "hiring manager"
    elif "investor" in text or "partner" in text:
        classification = "investor/operator"
    elif "referr" in text or "employee at" in text:
        classification = "possible referrer"

    person = Person(**payload.model_dump(), classification=classification)
    db.add(person)
    db.commit()
    db.refresh(person)
    return {"id": person.id, "classification": classification}


@router.post("/outreach/generate")
def outreach(payload: OutreachRequest):
    return generate_note(payload.note_type, payload.recipient_name, payload.company, payload.context)


@router.post("/resumes/match")
def resume_match(payload: ResumeMatchRequest, db: Session = Depends(get_db)):
    resumes = db.query(Resume).all()
    if not resumes:
        return {"error": "No resumes found"}

    def score(resume_text: str):
        terms = ["release governance", "engineering operations", "tpm", "ai", "platform"]
        text = f"{resume_text} {payload.jd_text}".lower()
        return sum(1 for t in terms if t in text)

    ranked = sorted(resumes, key=lambda r: score(r.resume_text), reverse=True)
    best = ranked[0]
    return {
        "best_resume": best.version_name,
        "top_strengths": ["Release governance", "AI-assisted workflows", "Cross-org execution"],
        "missing_keywords": ["finops", "sre"] if "sre" not in payload.jd_text.lower() else ["finops"],
        "custom_summary": "Strategic EngOps leader who scales execution systems for distributed engineering.",
        "car_bullets": [
            "Built release governance cadence reducing delays across multi-team programs.",
            "Designed Jira transformation and Definition of Done enforcement for reliability.",
            "Implemented AI-assisted reporting workflows for executive visibility.",
            "Created capacity modeling and KPI frameworks for quarterly planning.",
            "Enabled cross-functional delivery excellence for cloud and platform teams.",
        ],
        "outreach_angle": "Position as execution systems leader for scaling engineering velocity."
    }
