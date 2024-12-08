import datetime
from typing import List
import bcrypt
import models
from custom_exceptions.not_found_exception import NotFoundException
from custom_exceptions.username_taken_exception import UsernameTakenException
from dtos.users import UpdateUserDto, AddUserReqDto, LoginReqDto
from services.user_service_base import UserServiceBase
from tools.token_tool_base import TokenToolBase


class UserSaService(UserServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def get_all(self) -> List[models.Users]:
        users = self.context.query(models.Users).all()
        return users

    def get_by_id(self, user_id: int) -> models.Users:
        user = self.context.query(models.Users).filter(models.Users.Id == int(user_id)).first()
        return user

    def update_user(self, user_id: int, req_data: UpdateUserDto) -> models.Users:
        user = self.context.query(models.Users).filter(models.Users.Id == user_id).first()
        if user is None:
            return None

        user.UserName = req_data.username
        self.context.commit()
        return user

    def create(self, req: AddUserReqDto) -> models.Users:
        user_exists = self.context.query(models.Users).filter(models.Users.UserName == req.UserName).first()
        if user_exists is not None:
            raise UsernameTakenException('username already taken')
        user = models.Users(
            UserName=req.UserName,
            HashedPassword=bcrypt.hashpw(req.Password.encode('utf-8'), bcrypt.gensalt()),
            Role=req.Role
        )
        user.PasswordSalt = ''.encode('utf-8')
        self.context.add(user)
        self.context.commit()
        return user

    def login(self, req: LoginReqDto, _token: TokenToolBase):
        user = self.context.query(models.Users).filter(models.Users.UserName == req.username).first()
        if user is None:
            raise NotFoundException('user not found')

        if bcrypt.checkpw(req.password.encode('utf-8'), user.HashedPassword):
            return _token.create_token(
                {'sub': str(user.Id), 'username': user.UserName, 'iat': datetime.datetime.now().timestamp(),
                 'exp': datetime.datetime.now().timestamp() + (3600 * 24 * 7)}), user
        raise NotFoundException('user not found')
