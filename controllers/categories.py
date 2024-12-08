from typing import List
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate

from dependencies import ModeratorUser
from dtos.categories import CategoryDto, AddCategoryReqDto
from dtos.products import ProductDto
from mapper.mapper import ResponseMapper
from services.service_factory import CategoryService, ProductService

router = APIRouter(
    prefix='/api/categories',
    tags=['categories']
)


@router.get('/')
def get_all_categories(service: CategoryService, mapper: ResponseMapper) -> List[CategoryDto]:
    categories = service.get_all()
    return mapper.map("category_dto", categories)

@router.post('/')
def add_category(service: CategoryService, req: AddCategoryReqDto, account: ModeratorUser, mapper: ResponseMapper) -> CategoryDto:
    user_id = account.Id
    category = service.add_category(req, user_id)
    return mapper.map("category_dto", category)

@router.get('/{category_id}/products', response_model=Page[ProductDto])
def get_products_by_category(category_id: int, service: ProductService, mapper: ResponseMapper) -> List[ProductDto]:
    products = service.get_all_by_category_id(category_id)
    return paginate(mapper.map("product_dto", products))