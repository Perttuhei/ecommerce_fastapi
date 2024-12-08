from typing import List
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate

from dependencies import get_moderator_user
from dtos.products import ProductDto, AddProductReqDto
from mapper.mapper import ResponseMapper
from services.service_factory import ProductService

router = APIRouter(
    prefix='/api/products',
    tags=['products']
)


@router.get('/', response_model=Page[ProductDto])
def get_all_products(service: ProductService, mapper: ResponseMapper) -> List[ProductDto]:
    products = service.get_all()
    return paginate(mapper.map("product_dto", products))

@router.post('/', dependencies=[Depends(get_moderator_user)])
def add_product(service: ProductService, mapper: ResponseMapper, req: AddProductReqDto) -> ProductDto:
    newproduct = service.add_product(req)
    return mapper.map("product_dto", newproduct)