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

    def delete_order(self, order_id: int, user_id: int) -> str:
        order = self.context.query(models.Orders).filter(models.Orders.Id == order_id, models.Orders.CustomerId == user_id).first()
        if order is None:
            raise NotFoundException("order not found")
        state = str(order.State)
        if state == "confirmed-state":
            return "order already confirmed, order cannot be deleted"
        self.context.query(models.OrdersProducts).where(models.OrdersProducts.OrderId == order_id).delete()
        self.context.delete(order)
        self.context.commit()
        return "delete ok"
