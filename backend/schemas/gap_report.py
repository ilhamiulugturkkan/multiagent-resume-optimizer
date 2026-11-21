from pydantic import BaseModel, Field



class CompareBulletPoint(BaseModel):
    candidate_bullet_point_id: str
    requirement_id: str
    evidence: str  # Explanation of why this bullet point matches the requirement

'''
match_score (0 to 100), matched[], missing[], weak[], each with evidence (which bullet, which requirement).
'''
class GapReport(BaseModel):
    match_score: int = Field(ge=0, le=100)
    matched_bullet_points: list[CompareBulletPoint] = []
    missing_requirement_ids: list[str] = [] # ids of every must-have requirement that is not matched by any bullet point
    weak_bullet_points: list[CompareBulletPoint] = []
