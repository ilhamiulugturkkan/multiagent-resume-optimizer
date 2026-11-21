import pytest
from backend.schemas import RewriteResult, RewrittenBullet
from backend.schemas.assign_ids import (
    assign_resume_ids, assign_job_ids, assign_rewrite_ids,
)
from backend.schemas.validate import check_resume_unique_ids, check_rewrite


@pytest.fixture
def ready(sample_resume, sample_job):
    """Resume and job with ids assigned."""
    return assign_resume_ids(sample_resume), assign_job_ids(sample_job)


def make_rewrite(*bullets: RewrittenBullet) -> RewriteResult:
    return assign_rewrite_ids(RewriteResult(rewritten_bullets=list(bullets)))


# check_resume_unique_ids
def test_valid_resume_has_no_problems(sample_resume):
    assert check_resume_unique_ids(assign_resume_ids(sample_resume)) == []


def test_unassigned_ids_are_flagged(sample_resume):
    assert check_resume_unique_ids(sample_resume) != []


def test_duplicate_ids_are_flagged(sample_resume):
    assign_resume_ids(sample_resume)
    sample_resume.skills[1].id = sample_resume.skills[0].id
    assert "duplicate resume ids" in check_resume_unique_ids(sample_resume)


# check_rewrite
def test_valid_rewrite_passes(ready):
    resume, job = ready
    rewrite = make_rewrite(RewrittenBullet(
        source_bullet_ids=["exp0-b0"], new_text="x", targets=["must0"]))
    assert check_rewrite(rewrite, resume, job) == []


def test_check_rewrite_catches_fake_source(ready):
    resume, job = ready
    rewrite = make_rewrite(RewrittenBullet(
        source_bullet_ids=["exp9-b4"], new_text="x"))
    problems = check_rewrite(rewrite, resume, job)
    assert any("exp9-b4" in p for p in problems)


def test_check_rewrite_catches_fake_target(ready):
    resume, job = ready
    rewrite = make_rewrite(RewrittenBullet(
        source_bullet_ids=["exp0-b0"], new_text="x", targets=["must9"]))
    problems = check_rewrite(rewrite, resume, job)
    assert any("must9" in p for p in problems)


def test_check_rewrite_catches_duplicate_rewrite_ids(ready):
    resume, job = ready
    rewrite = make_rewrite(
        RewrittenBullet(source_bullet_ids=["exp0-b0"], new_text="a"),
        RewrittenBullet(source_bullet_ids=["exp0-b1"], new_text="b"),
    )
    rewrite.rewritten_bullets[1].id = rewrite.rewritten_bullets[0].id
    assert "duplicate rewrite ids" in check_rewrite(rewrite, resume, job)


def test_check_rewrite_flags_unassigned_ids(sample_resume, sample_job):
    # assign_resume_ids deliberately not called, so every id is ""
    rewrite = make_rewrite(RewrittenBullet(source_bullet_ids=[""], new_text="x"))
    assert check_rewrite(rewrite, sample_resume, sample_job) != []


def test_check_rewrite_reports_each_bad_bullet(ready):
    resume, job = ready
    rewrite = make_rewrite(
        RewrittenBullet(source_bullet_ids=["nope1"], new_text="a"),
        RewrittenBullet(source_bullet_ids=["nope2"], new_text="b"),
    )
    assert len(check_rewrite(rewrite, resume, job)) == 2