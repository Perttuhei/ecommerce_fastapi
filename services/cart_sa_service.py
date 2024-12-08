import datetime
from typing import List

import models
from custom_exceptions.not_found_exception import NotFoundException
from dtos.items import AddItemReqDto, DeleteItemResDto, UpdateItemReqDto, CartDto
from services.cart_service_base import CartServiceBase


class CartSaService(CartServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def add_item(self, req: AddItemReqDto, user_id) -> models.OrdersProducts:
        product = self.context.query(models.Products).filter(models.Products.Id == req.ProductId).first()
        if product is None:
            raise NotFoundException('product not found')
        # jos käyttäjällä ei ole aktiivista ostoskoria niin luodaan sellainen
        order = self.context.query(models.Orders).filter(models.Orders.CustomerId == user_id).first()
        if order is None:
            NewOrder = models.Orders(
                CreatedDate=datetime.datetime.now(),
                State='cart-state',
                CustomerId=user_id,
                ConfirmedDate=None,
                RemovedDate=None,
                HandlerId=None
            )
            self.context.add(NewOrder)
            self.context.commit()
            order = self.context.query(models.Orders).filter(models.Orders.CustomerId == user_id).first()
        order_id = order.Id
        # jos lisättävä item löytyy jo ostoskorista niin unitcount + 1
        # else: lisätään tuote ostoskoriin
        item = self.context.query(
            models.OrdersProducts) \
            .filter(models.OrdersProducts.OrderId == order_id,
                    models.OrdersProducts.ProductId == req.ProductId).first()
        if item:
            item.UnitCount = item.UnitCount + 1
            self.context.commit()
            return item
        else:
            newitem = models.OrdersProducts(
                OrderId=order_id,
                ProductId=req.ProductId,
                UnitCount=1,
                UnitPrice=product.UnitPrice
            )
            self.context.add(newitem)
            self.context.commit()
            return newitem

    def get_cart_item_by_id(self, item_id: int, user_id) -> CartDto:
        order = self.context.query(models.Orders).filter(models.Orders.CustomerId == user_id).first()
        order_id = order.Id
        item = self.context.query(
            models.OrdersProducts) \
            .filter(models.OrdersProducts.OrderId == order_id,
                    models.OrdersProducts.ProductId == item_id).first()
        if item is None:
            raise NotFoundException("item not found")
        return item
    def update_item(self, item_id: int, user_id, req: UpdateItemReqDto) -> CartDto:
        item = self.get_cart_item_by_id(item_id, user_id)
        if item is None:
            raise NotFoundException("item not found")
        item.UnitCount = req.unitcount
        self.context.commit()
        return item

    def delete_item(self, item_id: int, user_id) -> DeleteItemResDto:
        # poisteaan item jos ostoskori ja poistettava tuote löytyy
        order = self.context.query(models.Orders).filter(models.Orders.CustomerId == user_id).first()
        order_id = order.Id
        if order is None:
            raise NotFoundException("order not found")

        product = self.context.query(
            models.OrdersProducts).filter(
            models.OrdersProducts.ProductId == item_id,
            models.OrdersProducts.OrderId == order_id).first()
        if product is None:
            raise NotFoundException("item not found")

        self.context.delete(product)
        self.context.commit()
        return DeleteItemResDto(response="item deleted successfully")


