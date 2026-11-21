from .resume import Resume
from .job_posting import JobPosting
from .rewrite_result import RewriteResult

def assign_resume_ids(resume: Resume) -> Resume:
    if resume.summary:
        resume.summary.id = "summary"

    for field, prefix in [("experience", "exp"), ("education", "edu"), ("projects", "proj")]:
        for i, entry in enumerate(getattr(resume, field)):
            for j, b in enumerate(entry.bullet_points):
                b.id = f"{prefix}{i}-b{j}"

    for field, prefix in [("skills", "skill"), ("certifications", "cert"),
                          ("languages", "lang"), ("awards", "award"),
                          ("publications", "pub")]:
        for i, b in enumerate(getattr(resume, field)):
            b.id = f"{prefix}{i}"

    return resume


def assign_job_ids(job: JobPosting) -> JobPosting:
    for i, r in enumerate(job.must_have_skills):
        r.id = f"must{i}"
    for i, r in enumerate(job.nice_to_have_skills):
        r.id = f"nice{i}"
    return job

def assign_rewrite_ids(result: RewriteResult) -> RewriteResult:
    for i, rb in enumerate(result.rewritten_bullets):
        rb.id = f"rw{i}"
    return result

# Get all ids from the resume
def collect_all_resume_ids(resume: Resume) -> set[str]:
    ids = set()
    if resume.summary:
        ids.add(resume.summary.id)
    for section in (resume.experience, resume.education, resume.projects):
        for entry in section:
            ids.update(b.id for b in entry.bullet_points)
    for section in (resume.skills, resume.certifications, resume.languages,
                    resume.awards, resume.publications):
        ids.update(b.id for b in section)
    return ids

# Get all ids from the resume as list
def collect_all_resume_ids_list(resume: Resume) -> list[str]:
    ids = list()
    if resume.summary:
        ids.append(resume.summary.id)
    for section in (resume.experience, resume.education, resume.projects):
        for entry in section:
            ids.extend(b.id for b in entry.bullet_points)
    for section in (resume.skills, resume.certifications, resume.languages,
                    resume.awards, resume.publications):
        ids.extend(b.id for b in section)
    return ids

# Return all ids from the job posting
def collect_requirement_ids(job: JobPosting) -> set[str]:
    return {r.id for r in job.must_have_skills + job.nice_to_have_skills}