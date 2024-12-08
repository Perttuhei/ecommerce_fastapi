import datetime

import models
from custom_exceptions.not_found_exception import NotFoundException
from dtos.orders import OrderResDto
from services.order_service_base import OrderServiceBase


class OrderSaService(OrderServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def order_products(self, user_id) -> models.Orders:
        order = self.context.query(models.Orders).filter(models.Orders.CustomerId == user_id).first()
        if order is None:
            raise NotFoundException("order not found")
        order.State = "ordered-state"
        order.ConfirmedDate = str(order.ConfirmedDate)
        order.RemovedDate = str(order.RemovedDate)
        order.HandlerId = int(0)
        self.context.commit()
        return order

    def order_confirm(self, user_id: int, order_id: int) -> models.Orders:
        order = self.context.query(models.Orders).filter(models.Orders.Id == order_id).first()
        if order is None:
            raise NotFoundException("order not found")
        print(datetime.datetime.now())
        order.ConfirmedDate = str(datetime.datetime.now())
        order.State = "confirmed-state"
        order.HandlerId = user_id
        self.context.commit()
        return order