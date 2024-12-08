from pydantic import BaseModel


class ProductDto(BaseModel):
    id: int
    name: str
    categoryid: int
    unitprice: int
    description: str

class UpdateProductDto(BaseModel):
    name: str
    unitprice: int
    description: str

class AddProductReqDto(BaseModel):
    Name: str
    CategoryId: int
    UnitPrice: int
    Description: str

