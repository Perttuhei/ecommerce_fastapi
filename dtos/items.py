from pydantic import BaseModel


class AddItemReqDto(BaseModel):
    ProductId: int

class DeleteItemResDto(BaseModel):
    response: str

class CartDto(BaseModel):
    orderid: int
    productid: int
    unitcount: int
    unitprice: int