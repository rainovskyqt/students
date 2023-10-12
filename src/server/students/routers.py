from typing import List

from fastapi import APIRouter
from .models import Student, StudentGroup
from .resolvers import get_students

router = APIRouter()


# @router.get('/')
# def get_group() -> List[OutputGroup]:
#     return get_groups()


@router.get('/{group_id}')
def get_students_by_group(group_id: int) -> List[Student]:
    return get_students(group_id)

#
# @router.post('/')
# def add_group(new_group: ImputGroup) -> NewId:
#     return add_new_group(new_group)
#
#
# @router.put('/{group_id}')
# def add_group(group_id: int, new_group: ImputGroup) -> NewId:
#     return update_group(group_id, new_group)
#
#
# @router.delete("/{group_id}")
# def delete_group(group_id: int) -> NewId:
#     return delete_current_group(group_id)