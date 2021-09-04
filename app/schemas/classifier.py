from typing import Literal
from pydantic import BaseModel


P = dict[str, float]


class GetPerceptionRequest(BaseModel):
    input: str


class GetPerceptionResponse(BaseModel):
    perception: Literal['pos', 'neg']
    detail: P
