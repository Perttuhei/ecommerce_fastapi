from fastapi import APIRouter

from dependencies import LoggedInUser
from dtos.orders import DeleteOrderResDto
from services.service_factory import OrderService

router = APIRouter(
    prefix='/api/account',
    tags=['account']
)

@router.delete('/orders/{order_id}')
def delete_order(service: OrderService, order_id: int, account: LoggedInUser) -> DeleteOrderResDto:
    user_id = account.Id
    response = service.delete_order(order_id, user_id)
    return DeleteOrderResDto(response=response)
