from typing import List
from fastapi import APIRouter

from dtos.products import ProductDto
from mapper.mapper import ResponseMapper
from services.service_factory import ProductService

router = APIRouter(
    prefix='/api/categories',
    tags=['categories']
)


@router.get('/')
def get_all_categories(service: CategoryService, mapper: ResponseMapper) -> List[CategoryDto]:
    categories = service.get_all()
    return mapper.map("category_dto", categories)