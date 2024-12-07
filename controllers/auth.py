from typing import List
from fastapi import APIRouter
from fastapi_pagination import Page, paginate
from dtos.users import AddUserReqDto, UserDto, UpdateUserDto
from mapper.mapper import ResponseMapper
from services.service_factory import UserService

router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

# fastapi pagination hoitaa sivutuksen, Page class määrittelee palautettavan mallin
# paginate funktion avulla palautetaan mapattu users data
@router.get('/', response_model=Page[UserDto])
def get_all_users(service: UserService, mapper: ResponseMapper) -> List[UserDto]:
    users = service.get_all()
    return paginate(mapper.map("user_dto", users))

@router.get('/{user_id}')
def get_user_by_id(user_id: int, service: UserService, mapper: ResponseMapper) -> UserDto:
    user = service.get_by_id(user_id)
    return mapper.map("user_dto", user)

@router.post('/')
def create_user(service: UserService, req: AddUserReqDto, mapper: ResponseMapper) -> UserDto:
    user = service.create(req)
    return mapper.map("user_dto", user)

@router.put('/{user_id}')
def update_user(user_id: int, service: UserService, mapper: ResponseMapper, req_data: UpdateUserDto) -> UserDto:
    user = service.update_user(user_id, req_data)
    return mapper.map("user_dto", user)