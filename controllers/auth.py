from typing import List
from fastapi import APIRouter
from fastapi_pagination import Page, paginate
from dtos.users import AddUserReqDto, UserDto, UpdateUserDto, LoginReqDto, LoginResDto
from mapper.mapper import ResponseMapper
from services.service_factory import UserService
from tools.token_factory import AppToken

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

@router.post('/register')
def create_user(service: UserService, req: AddUserReqDto, mapper: ResponseMapper) -> UserDto:
    user = service.create(req)
    return mapper.map("user_dto", user)

@router.put('/{user_id}')
def update_user(user_id: int, service: UserService, mapper: ResponseMapper, req_data: UpdateUserDto) -> UserDto:
    user = service.update_user(user_id, req_data)
    return mapper.map("user_dto", user)

@router.post('/login')
async def login(service: UserService, req: LoginReqDto, _token: AppToken) -> LoginResDto:
    token = service.login(req, _token)
    return LoginResDto(token=token)
