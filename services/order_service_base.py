import abc

import models
from dtos.orders import OrderResDto


class OrderServiceBase(abc.ABC):

    @abc.abstractmethod
    def order_products(self, user_id) -> models.Orders:
        raise NotImplementedError()

    @abc.abstractmethod
    def order_confirm(self, user_id: int, order_id: int) -> models.Orders:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_order(self, order_id: int, user_id: int) -> str:
        raise NotImplementedError()