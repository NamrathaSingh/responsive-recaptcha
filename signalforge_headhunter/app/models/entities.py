from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String, Text

from app.core.db import Base


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Company(Base, TimestampMixin):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    domain = Column(String)
    sector = Column(String)
    funding_stage = Column(String)
    funding_signal = Column(String)
    india_presence = Column(String)
    hiring_signal = Column(Text)
    investors = Column(Text)
    company_fit = Column(Float, default=0)


class Role(Base, TimestampMixin):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    company_name = Column(String, nullable=False)
    title = Column(String, nullable=False)
    location = Column(String)
    source_url = Column(String)
    jd_text = Column(Text)
    role_fit = Column(Float, default=0)
    seniority_fit = Column(Float, default=0)
    domain_fit = Column(Float, default=0)


class Person(Base, TimestampMixin):
    __tablename__ = "people"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    company = Column(String)
    title = Column(String)
    profile_url = Column(String)
    profile_text = Column(Text)
    classification = Column(String)
    shared_context = Column(Text)
    referral_likelihood = Column(Float, default=0)


class OutreachNote(Base, TimestampMixin):
    __tablename__ = "outreach_notes"
    id = Column(Integer, primary_key=True)
    person_name = Column(String)
    company_name = Column(String)
    note_type = Column(String)
    channel = Column(String)
    note_text = Column(Text)


class Interaction(Base, TimestampMixin):
    __tablename__ = "interactions"
    id = Column(Integer, primary_key=True)
    person_name = Column(String, nullable=False)
    channel = Column(String)
    status = Column(String)
    summary = Column(Text)
    next_step = Column(String)


class Resume(Base, TimestampMixin):
    __tablename__ = "resumes"
    id = Column(Integer, primary_key=True)
    version_name = Column(String, nullable=False)
    focus_area = Column(String)
    resume_text = Column(Text)


class Investor(Base, TimestampMixin):
    __tablename__ = "investors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    thesis = Column(Text)
    stability_score = Column(Float, default=0)


class Signal(Base, TimestampMixin):
    __tablename__ = "signals"
    id = Column(Integer, primary_key=True)
    entity_type = Column(String, nullable=False)
    entity_name = Column(String, nullable=False)
    signal_type = Column(String)
    signal_text = Column(Text)
    score = Column(Float, default=0)
