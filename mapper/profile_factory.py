from typing import Type
from pydantic import BaseModel

from mapper.category_profile import CategoryProfile
from mapper.cart_profile import CartProfile
from mapper.product_profile import ProductProfile
from mapper.user_profile import UserProfile


def create_user_profile(_type: Type[BaseModel]):
    return UserProfile(_type)

def create_product_profile(_type: Type[BaseModel]):
    return ProductProfile(_type)

def create_category_profile(_type: Type[BaseModel]):
    return CategoryProfile(_type)

def create_cart_profile(_type: Type[BaseModel]):
    return CartProfile(_type)