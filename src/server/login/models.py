from pydantic import BaseModel
from typing import Optional


class Login(BaseModel):
    login: str
    password: str

