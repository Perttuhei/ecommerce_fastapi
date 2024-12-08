from pydantic import BaseModel


class OrderResDto(BaseModel):
    id: int
    createddate: str
    customerid: int
    handlerid: int
    state: str

class OrderDto(BaseModel):
    id: int
    createddate: str
    customerid: int
    confirmeddate: str
    removeddate: str
    handlerid: int
    state: str

