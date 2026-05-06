from pydantic import BaseModel


class CompanyIn(BaseModel):
    name: str
    domain: str | None = None
    sector: str | None = None
    funding_stage: str | None = None
    investors: str | None = None
    india_presence: str | None = None


class RoleMatchRequest(BaseModel):
    title: str
    jd_text: str


class ProfileIntelligenceRequest(BaseModel):
    name: str
    company: str | None = None
    title: str | None = None
    profile_text: str


class OutreachRequest(BaseModel):
    note_type: str
    recipient_name: str
    company: str
    context: str


class ResumeMatchRequest(BaseModel):
    jd_text: str
