import pytest
from backend.schemas import (
    Resume, ContactInfo, Summary, ExperienceEntry, EducationEntry,
    ProjectEntry, BulletPoint, JobPosting,
)


@pytest.fixture
def sample_resume() -> Resume:
    return Resume(
        name="Test User",
        contact_info=ContactInfo(email="t@example.com"),
        summary=Summary(text="Data science student."),
        experience=[
            ExperienceEntry(company="A", title="Intern", bullet_points=[
                BulletPoint(text="Built a churn model"),
                BulletPoint(text="Cut cost 10%"),
            ]),
            ExperienceEntry(company="B", title="Analyst", bullet_points=[
                BulletPoint(text="Wrote SQL reports"),
            ]),
        ],
        education=[
            EducationEntry(institution="UMD", degree="BS", bullet_points=[
                BulletPoint(text="Machine Learning coursework"),
            ]),
        ],
        projects=[
            ProjectEntry(name="Optimizer", bullet_points=[
                BulletPoint(text="Built a FastAPI service"),
            ]),
        ],
        skills=[BulletPoint(text="Python"), BulletPoint(text="SQL")],
        awards=[BulletPoint(text="Dean's List")],
    )


@pytest.fixture
def sample_job() -> JobPosting:
    return JobPosting(
        title="ML Engineer",
        company="Acme",
        must_have_skills=[BulletPoint(text="PyTorch"), BulletPoint(text="SQL")],
        nice_to_have_skills=[BulletPoint(text="Docker")],
        keywords=["pytorch", "sql"],
    )