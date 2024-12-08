import abc

from dtos.orders import OrderResDto


class OrderServiceBase(abc.ABC):

    @abc.abstractmethod
    def order_products(self, user_id) -> OrderResDto:
        raise NotImplementedError()