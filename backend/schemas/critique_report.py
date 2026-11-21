from pydantic import BaseModel, PositiveInt
from typing import Literal

# - CritiqueReport: verdict (pass or revise)
# , issues[] with type (fabrication, ats_format, keyword_stuffing, clarity), the bullet it refers to, and a suggested fix.


class CritiqueIssue(BaseModel):
    type: Literal["fabrication", "ats_format", "keyword_stuffing", "clarity"]
    rewrite_id: str        # id of a RewrittenBullet
    reason: str            # what is wrong
    suggested_fix: str
    
class CritiqueReport(BaseModel):
    verdict: Literal["pass", "revise"]
    issues: list[CritiqueIssue] = []