from typing import Type
from pydantic import BaseModel

from mapper.product_profile import ProductProfile
from mapper.user_profile import UserProfile


def create_user_profile(_type: Type[BaseModel]):
    return UserProfile(_type)

def create_product_profile(_type: Type[BaseModel]):
    return ProductProfile(_type)