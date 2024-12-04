from typing import List
from fastapi import APIRouter
from mapper.mapper import ResponseMapper

router = APIRouter(
    prefix='/api/products',
    tags=['products']
)


@router.get('/')
def get_all_products(service: ProductService, mapper: ResponseMapper) -> List[ProductDto]:
    products = service.get_all()
    return mapper.map("product_dto", products)