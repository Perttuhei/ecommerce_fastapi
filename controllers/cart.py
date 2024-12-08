from fastapi import APIRouter
from dependencies import LoggedInUser
from dtos.items import CartDto, AddItemReqDto, DeleteItemResDto, UpdateItemReqDto
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

@router.put('/items/{item_id}')
def update_item(service: CartService, item_id: int, req: UpdateItemReqDto, mapper: ResponseMapper, account: LoggedInUser) -> CartDto:
    user_id = account.Id
    item = service.update_item(item_id, user_id, req)
    return mapper.map("cart_dto", item)

@router.get('/items/{item_id}')
def get_cart_item_by_id(service: CartService, item_id: int, mapper: ResponseMapper, account: LoggedInUser) -> CartDto:
    user_id = account.Id
    item = service.get_cart_item_by_id(item_id, user_id)
    return mapper.map("cart_dto", item)