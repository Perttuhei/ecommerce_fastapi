from typing import Annotated

from fastapi import Depends

import models
from services.user_sa_service import UserSaService
from services.user_service_base import UserServiceBase


def init_user_service(context: models.Db):
    return UserSaService(context)


UserService = Annotated[UserServiceBase, Depends(init_user_service)]