from backend.schemas import RewriteResult, RewrittenBullet
from backend.schemas.assign_ids import (
    assign_resume_ids, assign_job_ids, assign_rewrite_ids,
    collect_all_resume_ids, collect_all_resume_ids_list,
    collect_requirement_ids,
)


def test_all_resume_ids_nonempty_and_unique(sample_resume):
    assign_resume_ids(sample_resume)
    ids = collect_all_resume_ids_list(sample_resume)
    assert all(ids)
    assert len(ids) == len(set(ids))


def test_resume_id_values(sample_resume):
    r = assign_resume_ids(sample_resume)
    assert r.summary.id == "summary"
    assert r.experience[0].bullet_points[1].id == "exp0-b1"
    assert r.experience[1].bullet_points[0].id == "exp1-b0"
    assert r.education[0].bullet_points[0].id == "edu0-b0"
    assert r.projects[0].bullet_points[0].id == "proj0-b0"
    assert [s.id for s in r.skills] == ["skill0", "skill1"]
    assert r.awards[0].id == "award0"


def test_assign_resume_ids_without_summary(sample_resume):
    sample_resume.summary = None
    assign_resume_ids(sample_resume)
    assert "summary" not in collect_all_resume_ids(sample_resume)


def test_assign_resume_ids_overwrites_llm_ids(sample_resume):
    sample_resume.experience[0].bullet_points[0].id = "made-up"
    assign_resume_ids(sample_resume)
    assert sample_resume.experience[0].bullet_points[0].id == "exp0-b0"


def test_assign_resume_ids_is_idempotent(sample_resume):
    first = collect_all_resume_ids_list(assign_resume_ids(sample_resume))
    second = collect_all_resume_ids_list(assign_resume_ids(sample_resume))
    assert first == second


def test_unassigned_ids_are_empty(sample_resume):
    assert "" in collect_all_resume_ids(sample_resume)


def test_job_ids(sample_job):
    j = assign_job_ids(sample_job)
    assert [r.id for r in j.must_have_skills] == ["must0", "must1"]
    assert [r.id for r in j.nice_to_have_skills] == ["nice0"]
    assert collect_requirement_ids(j) == {"must0", "must1", "nice0"}


def test_rewrite_ids():
    result = RewriteResult(rewritten_bullets=[
        RewrittenBullet(source_bullet_ids=["exp0-b0"], new_text="a"),
        RewrittenBullet(source_bullet_ids=["exp0-b1"], new_text="b"),
    ])
    assign_rewrite_ids(result)
    assert [rb.id for rb in result.rewritten_bullets] == ["rw0", "rw1"]