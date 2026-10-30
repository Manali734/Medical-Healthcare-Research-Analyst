from pydantic import BaseModel, Field, field_validator
from typing import List

class AskRequest(BaseModel):
    question: str = Field(..., min_length=5, max_length=2000, description="Healthcare or medical research question")

    @field_validator("question")
    @classmethod
    def question_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Question must not be blank.")
        return value.strip()

class AskResponse(BaseModel):
    status: str
    question: str
    answer: str
    sources: List[str]
    disclaimer: str
