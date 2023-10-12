from pydantic import BaseModel
from typing import Optional, List


class Student(BaseModel):
    id: Optional[int]
    surname: str
    name: str
    group_id: Optional[int]


class StudentGroup(BaseModel):
    group_id: int
    students: List[Student]


class NewId(BaseModel):
    code: int
    id: int