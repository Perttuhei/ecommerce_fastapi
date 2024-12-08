from typing import Annotated
from fastapi.params import Depends

from dtos.categories import CategoryDto
from dtos.items import CartDto
from dtos.orders import OrderDto
from dtos.products import ProductDto, AddProductReqDto
from dtos.users import UserDto
from mapper.base_profile import BaseProfile
from mapper.profile_factory import create_user_profile, create_product_profile, create_category_profile, \
    create_cart_profile, create_order_profile


class Mapper:
    def __init__(self, profiles: dict[str: BaseProfile]) -> None:
        self.profiles = profiles

    def map(self, _type, data):
        if _type not in self.profiles.keys():
            raise Exception('Profile missing')

        if isinstance(data, list):
            return self.profiles[_type].map_list(data)
        else:
            return self.profiles[_type].map(data)



def create_mapper() -> Mapper:
    profiles = {
        'user_dto': create_user_profile(UserDto),
        'product_dto': create_product_profile(ProductDto),
        'category_dto': create_category_profile(CategoryDto),
        'product_req_dto': create_product_profile(AddProductReqDto),
        'cart_dto': create_cart_profile(CartDto),
        'order_dto': create_order_profile(OrderDto)
    }
    return Mapper(profiles)

ResponseMapper = Annotated[Mapper, Depends(create_mapper)]