import abc

import models
from dtos.items import AddItemReqDto, CartDto, DeleteItemResDto, UpdateItemReqDto


class CartServiceBase(abc.ABC):

    @abc.abstractmethod
    def add_item(self, req: AddItemReqDto, user_id) -> models.OrdersProducts:
        raise NotImplementedError()

    def delete_item(self, item_id: int, user_id) -> models.OrdersProducts:
        raise NotImplementedError()
    def update_item(self, item_id: int, user_id, req: UpdateItemReqDto) -> models.OrdersProducts:
        raise NotImplementedError()

    def get_cart_item_by_id(self, item_id: int, user_id) -> models.OrdersProducts:
        raise NotImplementedError()