import models
from custom_exceptions.not_found_exception import NotFoundException
from dtos.orders import OrderResDto
from services.order_service_base import OrderServiceBase


class OrderSaService(OrderServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def order_products(self, user_id) -> OrderResDto:
        order = self.context.query(models.Orders).filter(models.Orders.CustomerId == user_id).first()
        if order is None:
            raise NotFoundException("order not found")
        order.State = "ordered-state"
        self.context.commit()
        return order