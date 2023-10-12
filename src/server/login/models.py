from pydantic import BaseModel
from typing import Optional, List


class Login(BaseModel):
    login: str
    password: str
