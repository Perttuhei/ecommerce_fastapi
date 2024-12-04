from pydantic import BaseModel


class ProductDto(BaseModel):
    id: int
    name: str
    categoryid: int
    unitprice: float
    description: str

class UpdateProductDto(BaseModel):
    name: str
    unitprice: float
    description: str
