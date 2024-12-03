from typing import List
from fastapi import APIRouter
from dtos.users import UserDto
from mapper.mapper import ResponseMapper
from services.service_factory import UserService

router = APIRouter(
    prefix='/api/users',
    tags=['users']
)


@router.get('/')
def get_all_users(service: UserService, mapper: ResponseMapper) -> List[UserDto]:
    users = service.get_all()
    return mapper.map("user_dto", users)