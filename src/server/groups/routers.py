from fastapi import APIRouter

from .resolvers import get_groups, add_group

router = APIRouter()

@router.get('/')
def get_group():
    return get_groups()


@router.post('/')
def new_group(name: str):
    return add_group(name)
