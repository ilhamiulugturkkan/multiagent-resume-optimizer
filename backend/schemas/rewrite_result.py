from pydantic import BaseModel, Field

class RewrittenBullet(BaseModel):
    id: str = ""
    source_bullet_ids: list[str] = Field(min_length=1) # New text is based on these source bullet points
    new_text: str
    targets: list[str] = []  # To address target requirement

class RewriteResult(BaseModel):
    rewritten_bullets: list[RewrittenBullet]