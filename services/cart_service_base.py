import abc

from dtos.items import AddItemReqDto, CartDto, DeleteItemResDto, UpdateItemReqDto


class CartServiceBase(abc.ABC):

    @abc.abstractmethod
    def add_item(self, req: AddItemReqDto, user_id) -> CartDto:
        raise NotImplementedError()

    def delete_item(self, item_id: int, user_id) -> DeleteItemResDto:
        raise NotImplementedError()
    def update_item(self, item_id: int, user_id, req: UpdateItemReqDto) -> CartDto:
        raise NotImplementedError()

    def get_cart_item_by_id(self, item_id: int, user_id) -> CartDto:
        raise NotImplementedError()