import abc

import models
from dtos.users import UpdateUserDto, AddUserReqDto, LoginReqDto, LoginResDto
from tools.token_tool_base import TokenToolBase


class UserServiceBase(abc.ABC):

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_by_id(self, user_id: int):
        raise NotImplementedError()

    @abc.abstractmethod
    def update_user(self, user_id: int, req_data: UpdateUserDto):
        raise NotImplementedError()

    @abc.abstractmethod
    def create(self, req: AddUserReqDto):
        raise NotImplementedError()

    @abc.abstractmethod
    def login(self, req: LoginReqDto, _token: TokenToolBase) -> models.Users:
        raise NotImplementedError()