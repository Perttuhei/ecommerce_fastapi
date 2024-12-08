from typing import List, Annotated
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_pagination import Page, paginate

from dependencies import LoggedInUser, get_moderator_user
from dtos.users import AddUserReqDto, UserDto, UpdateUserDto, LoginReqDto, LoginResDto, ApiLoginResDto
from mapper.mapper import ResponseMapper
from services.service_factory import UserService
from tools.token_factory import AppToken

router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

LoginReq = Annotated[OAuth2PasswordRequestForm, Depends()]

# fastapi pagination hoitaa sivutuksen, Page class määrittelee palautettavan mallin
# paginate funktion avulla palautetaan mapattu users data
@router.get('/', response_model=Page[UserDto])
def get_all_users(service: UserService, mapper: ResponseMapper) -> List[UserDto]:
    users = service.get_all()
    return paginate(mapper.map("user_dto", users))

@router.get('/account')
async def get_account(account: LoggedInUser, mapper: ResponseMapper) -> UserDto:
    return mapper.map("user_dto", account)

@router.post('/register')
def create_user(service: UserService, req: AddUserReqDto, mapper: ResponseMapper) -> UserDto:
    user = service.create(req)
    return mapper.map("user_dto", user)

@router.post('/api_login')
async def api_login(service: UserService, req: LoginReq, _token: AppToken) -> ApiLoginResDto:
    # loginista saadaan token ja user objekti, parsitaan user vastaamaan userDto joka palautetaan
    token, user = service.login(req, _token)
    userdto = {"id": user.Id, "username": user.UserName, "role": user.Role}
    return LoginResDto(token=token, user=userdto)
@router.post('/login')
async def login(service: UserService, req: LoginReqDto, _token: AppToken) -> LoginResDto:
    token, user = service.login(req, _token)
    userdto = {"id": user.Id, "username": user.UserName, "role": user.Role}
    return LoginResDto(token=token, user=userdto)

@router.get('/{user_id}')
def get_user_by_id(user_id: int, service: UserService, mapper: ResponseMapper) -> UserDto:
    user = service.get_by_id(user_id)
    return mapper.map("user_dto", user)

@router.put('/{user_id}')
def update_user(user_id: int, service: UserService, mapper: ResponseMapper, req_data: UpdateUserDto) -> UserDto:
    user = service.update_user(user_id, req_data)
    return mapper.map("user_dto", user)



