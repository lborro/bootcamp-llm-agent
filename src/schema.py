from pydantic import BaseModel
from typing import List


class BotAction(BaseModel):
    action: str
    observation: str


class BotResponse(BaseModel):
    query: str
    response: str
    reasoning: List[BotAction]
