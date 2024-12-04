from typing import List
from fastapi import APIRouter

from dtos.products import ProductDto
from mapper.mapper import ResponseMapper
from services.service_factory import ProductService

router = APIRouter(
    prefix='/api/products',
    tags=['products']
)


@router.get('/')
def get_all_products(service: ProductService, mapper: ResponseMapper) -> List[ProductDto]:
    products = service.get_all()
    return mapper.map("product_dto", products)