import pytest
from pydantic import ValidationError
from backend.schemas import (
    Resume, ContactInfo, JobPosting, GapReport, CompareBulletPoint,
    RewriteResult, RewrittenBullet, CritiqueReport, CritiqueIssue,
)


# Resume
def test_resume_valid_minimal():
    r = Resume(name="X", contact_info=ContactInfo())
    assert r.experience == [] and r.summary is None


def test_resume_invalid_missing_name():
    with pytest.raises(ValidationError):
        Resume(contact_info=ContactInfo())


# JobPosting
def test_job_valid_minimal():
    j = JobPosting(title="T", company="C")
    assert j.must_have_skills == []


def test_job_invalid_missing_title():
    with pytest.raises(ValidationError):
        JobPosting(company="C")


# GapReport
@pytest.mark.parametrize("score", [0, 50, 100])
def test_gap_report_valid_scores(score):
    assert GapReport(match_score=score).match_score == score


@pytest.mark.parametrize("score", [-1, 101])
def test_gap_report_invalid_scores(score):
    with pytest.raises(ValidationError):
        GapReport(match_score=score)


def test_gap_report_with_items():
    g = GapReport(
        match_score=70,
        matched_bullet_points=[CompareBulletPoint(
            candidate_bullet_point_id="exp0-b0",
            requirement_id="must0",
            evidence="Uses the same tool.",
        )],
        missing_requirement_ids=["must1"],
    )
    assert g.missing_requirement_ids == ["must1"]


# RewriteResult
def test_rewrite_valid():
    rb = RewrittenBullet(source_bullet_ids=["exp0-b0"], new_text="x")
    assert RewriteResult(rewritten_bullets=[rb]).rewritten_bullets[0].targets == []


def test_rewrite_requires_source():
    with pytest.raises(ValidationError):
        RewrittenBullet(source_bullet_ids=[], new_text="x")


def test_rewrite_missing_source_field():
    with pytest.raises(ValidationError):
        RewrittenBullet(new_text="x")


# CritiqueReport
def test_critique_valid():
    c = CritiqueReport(verdict="revise", issues=[CritiqueIssue(
        type="fabrication", rewrite_id="rw0",
        reason="Adds a metric not in the source.", suggested_fix="Remove 40%.",
    )])
    assert c.issues[0].rewrite_id == "rw0"


def test_critique_invalid_verdict():
    with pytest.raises(ValidationError):
        CritiqueReport(verdict="maybe")


def test_critique_invalid_issue_type():
    with pytest.raises(ValidationError):
        CritiqueIssue(type="spelling", rewrite_id="rw0",
                      reason="r", suggested_fix="f")