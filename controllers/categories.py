from typing import List
from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate

from dependencies import AdminUser, get_admin_user
from dtos.categories import CategoryDto, AddCategoryReqDto, UpdateCategoryReqDto
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
def add_category(service: CategoryService, req: AddCategoryReqDto, account: AdminUser, mapper: ResponseMapper) -> CategoryDto:
    user_id = account.Id
    category = service.add_category(req, user_id)
    return mapper.map("category_dto", category)

@router.get('/{category_id}/products', response_model=Page[ProductDto])
def get_products_by_category(category_id: int, service: ProductService, mapper: ResponseMapper) -> List[ProductDto]:
    products = service.get_all_by_category_id(category_id)
    return paginate(mapper.map("product_dto", products))

@router.put('/{category_id}', dependencies=[Depends(get_admin_user)])
def update_category(service: CategoryService, req: UpdateCategoryReqDto, category_id: int, mapper: ResponseMapper) -> CategoryDto:
    print("kontrolleri")
    category = service.update_category(req, category_id)
    return mapper.map("category_dto", category)