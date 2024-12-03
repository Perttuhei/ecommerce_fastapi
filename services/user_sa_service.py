import models
from services.user_service_base import UserServiceBase


class UserSaService(UserServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def get_all(self):
        users = self.context.query(models.Users).all()
        return users
