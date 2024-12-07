from typing import List
from fastapi import APIRouter
from fastapi_pagination import Page, paginate
from dtos.users import AddUserReqDto, UserDto
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

@router.post('/')
def create_user(user_service: UserService, req: AddUserReqDto, mapper: ResponseMapper) -> UserDto:
    user = user_service.create(req)
    return mapper.map("user_dto", user)