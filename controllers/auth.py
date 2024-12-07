from fastapi import APIRouter

from dtos.users import AddUserReqDto, UserDto
from mapper.mapper import ResponseMapper
from services.service_factory import UserService

router = APIRouter(
    prefix='/api/auth',
    tags=['auth']
)

@router.post('/')
def create_user(user_service: UserService, req: AddUserReqDto, mapper: ResponseMapper) -> UserDto:
    user = user_service.create(req)
    return mapper.map("user_dto", user)