from fastapi import APIRouter
from dependencies import LoggedInUser
from dtos.items import CartDto, AddItemReqDto, DeleteItemResDto
from mapper.mapper import ResponseMapper
from services.service_factory import CartService

router = APIRouter(
    prefix='/api/cart',
    tags=['cart']
)

@router.post('/items')
def add_item(service: CartService, mapper: ResponseMapper, req: AddItemReqDto, account: LoggedInUser) -> CartDto:
    user_id = account.Id
    item = service.add_item(req, user_id)
    return mapper.map("cart_dto", item)

@router.delete('/items/{item_id}')
def delete_item(service: CartService, item_id: int, account: LoggedInUser) -> DeleteItemResDto:
    user_id = account.Id
    item = service.delete_item(item_id, user_id)
    return DeleteItemResDto(response=item.response)