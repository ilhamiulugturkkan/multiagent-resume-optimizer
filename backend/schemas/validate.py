# check if the ids are valid so that we can use them to match rewritten bullets to source bullets

from .assign_ids import collect_all_resume_ids, collect_all_resume_ids_list, collect_requirement_ids
from .job_posting import JobPosting
from .resume import Resume
from .rewrite_result import RewriteResult

def check_resume_unique_ids(resume: Resume) -> list[str]:
    ids = collect_all_resume_ids_list(resume)
    problems = []
    if any(not i for i in ids):
        problems.append("empty resume ids (assign_resume_ids not run?)")
    if len(ids) != len(set(ids)):
        problems.append("duplicate resume ids")
    return problems

def check_rewrite(result: RewriteResult, resume: Resume, job: JobPosting) -> list[str]:
    """Return a list of problems. Empty list means the rewrite is valid."""

    # Start by checking the resume ids are unique and valid
    problems = check_resume_unique_ids(resume)
    if problems:
        return problems 

    
    valid_sources = collect_all_resume_ids(resume) # All the bullets from the resume. Returns empty if no bullet exists
    if not valid_sources:
        problems.append("no source bullets in resume")
    valid_targets = collect_requirement_ids(job) # all the bullets from the job posting

    for rb in result.rewritten_bullets:
        bad_src = set(rb.source_bullet_ids) - valid_sources
        if bad_src:
            problems.append(f"{rb.id}: unknown source ids {sorted(bad_src)}")
        bad_tgt = set(rb.targets) - valid_targets
        if bad_tgt:
            problems.append(f"{rb.id}: unknown target ids {sorted(bad_tgt)}")

    ids = [rb.id for rb in result.rewritten_bullets]
    if len(ids) != len(set(ids)):
        problems.append("duplicate rewrite ids")
    return problems