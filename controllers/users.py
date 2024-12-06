from typing import List
from fastapi import APIRouter
from fastapi_pagination import Page, paginate

from dtos.users import UserDto
from mapper.mapper import ResponseMapper
from services.service_factory import UserService

router = APIRouter(
    prefix='/api/users',
    tags=['users']
)

# fastapi pagination hoitaa sivutuksen, Page class määrittelee palautettavan mallin
# paginate funktion avulla palautetaan mapattu users data
@router.get('/', response_model=Page[UserDto])
def get_all_users(service: UserService, mapper: ResponseMapper) -> List[UserDto]:
    users = service.get_all()
    return paginate(mapper.map("user_dto", users))