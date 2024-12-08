import abc

from dtos.items import AddItemReqDto, CartDto, DeleteItemResDto


class CartServiceBase(abc.ABC):

    @abc.abstractmethod
    def add_item(self, req: AddItemReqDto, user_id) -> CartDto:
        raise NotImplementedError()

    def delete_item(self, item_id: int, user_id) -> DeleteItemResDto:
        raise NotImplementedError()