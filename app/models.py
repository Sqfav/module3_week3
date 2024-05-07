from pydantic import BaseModel
from typing import Optional
from datetime import date


class User(BaseModel):
    id: Optional[int] = None
    username: str
    wallet: float
    birthdate: date


class UserUpdate(BaseModel):
    username: Optional[str] = None
    wallet: Optional[float] = None
    birthdate: Optional[date] = None
