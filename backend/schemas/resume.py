from pydantic import BaseModel

class BulletPoint(BaseModel):
    id: str = ""
    text: str

class ContactInfo(BaseModel):
    email: str | None = None
    phone: str | None = None
    linkedin_url: str | None = None
    github_url: str | None = None
    portfolio_url: str | None = None

class Summary(BaseModel):
    id: str = "summary"
    text: str

class EducationEntry(BaseModel):
    institution: str
    degree: str
    field_of_study: str | None = None
    gpa: float | None = None
    start_date: str | None = None 
    end_date: str | None = None
    bullet_points: list[BulletPoint] = [] # course work etc.

class ExperienceEntry(BaseModel):
    company: str
    title: str
    start_date: str | None = None  # Optional start date for ongoing experience
    end_date: str | None = None  # Optional end date for ongoing experience
    bullet_points: list[BulletPoint] = [] # Skills, tech used etc.

class ProjectEntry(BaseModel):
    name: str
    description: str = ""
    bullet_points: list[BulletPoint] = [] # Skills, tech used etc.

class Resume(BaseModel):
    name: str
    contact_info: ContactInfo
    summary: Summary | None = None
    experience: list[ExperienceEntry] = []
    education: list[EducationEntry] = []
    skills: list[BulletPoint] = []
    certifications: list[BulletPoint] = []
    languages: list[BulletPoint] = []
    projects: list[ProjectEntry] = []
    awards: list[BulletPoint] = []
    publications: list[BulletPoint] = []