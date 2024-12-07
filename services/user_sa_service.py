import bcrypt

import models
from custom_exceptions.username_taken_exception import UsernameTakenException
from dtos.users import UpdateUserDto, AddUserReqDto
from services.user_service_base import UserServiceBase


class UserSaService(UserServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def get_all(self):
        users = self.context.query(models.Users).all()
        return users

    def get_by_id(self, user_id: int):
        user = self.context.query(models.Users).filter(models.Users.Id == user_id).first()
        return user

    def update_user(self, user_id: int, req_data: UpdateUserDto):
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
