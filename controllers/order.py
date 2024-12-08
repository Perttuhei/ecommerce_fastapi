from fastapi import APIRouter

from dependencies import LoggedInUser
from dtos.orders import OrderResDto
from mapper.mapper import ResponseMapper
from services.service_factory import OrderService

router = APIRouter(
    prefix='/api/orders',
    tags=['orders']
)

@router.post('/')
def order_products(service: OrderService, account: LoggedInUser, mapper: ResponseMapper) -> OrderResDto:
    user_id = account.Id
    order = service.order_products(user_id)
    return mapper.map("order_dto", order)