from fastapi import APIRouter, Depends

from dependencies import LoggedInUser, ModeratorUser
from dtos.orders import OrderResDto, OrderDto
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

@router.post('/{order_id}/confirm')
def order_confirm(service: OrderService, account: ModeratorUser, order_id: int, mapper: ResponseMapper) -> OrderDto:
    user_id = account.Id
    order = service.order_confirm(user_id, order_id)
    return mapper.map("order_dto", order)