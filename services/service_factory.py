from typing import Annotated
from fastapi import Depends
import models
from services.product_sa_service import ProductSaService
from services.product_service_base import ProductServiceBase
from services.user_sa_service import UserSaService
from services.user_service_base import UserServiceBase


def init_user_service(context: models.Db):
    return UserSaService(context)

def init_product_service(context: models.Db):
    return ProductSaService(context)

ProductService = Annotated[ProductServiceBase, Depends(init_product_service)]
UserService = Annotated[UserServiceBase, Depends(init_user_service)]