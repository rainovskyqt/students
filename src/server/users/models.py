from datetime import datetime

from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    id: int
    login: Optional[str] = None
    reg_date: Optional[datetime] = None
    post_id: int
    post: Optional[str] = None


class InputUser(BaseModel):
    login: str
    password: str
    post_id: Optional[int] = None


class Post(BaseModel):
    id: Optional[int] = None
    name: str

class NewId(BaseModel):
    code: int
    id: int