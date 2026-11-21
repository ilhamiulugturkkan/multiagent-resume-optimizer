from pydantic import BaseModel
from .resume import BulletPoint


class JobPosting(BaseModel):
    title: str
    company: str
    location: str | None = None
    seniority_level: str | None = None
    must_have_skills: list[BulletPoint] = [] # includes experience, education, and skills requirements
    nice_to_have_skills: list[BulletPoint] = []
    keywords: list[str] = []