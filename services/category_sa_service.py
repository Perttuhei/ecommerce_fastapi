import models
from custom_exceptions.category_exist_exception import CategoryExistsException
from dtos.categories import AddCategoryReqDto, CategoryDto, UpdateCategoryReqDto
from services.category_service_base import CategoryServiceBase


class CategorySaService(CategoryServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def get_all(self):
        categories = self.context.query(models.Categories).all()
        return categories

    def add_category(self, req: AddCategoryReqDto, user_id) -> CategoryDto:
        category_exists = self.context.query(models.Categories).filter(models.Categories.Name == req.name).first()
        if category_exists is not None:
            raise CategoryExistsException()
        category = models.Categories(
            Name=req.name,
            UserId=user_id,
            Description=req.description
        )
        self.context.add(category)
        self.context.commit()
        return category

    def update_category(self, req: UpdateCategoryReqDto, category_id) -> CategoryDto:
        category_exists = self.context.query(models.Categories).filter(models.Categories.Name == req.name).first()
        if category_exists is not None:
            raise CategoryExistsException(f"category {req.name} already exists")
        category = self.context.query(models.Categories).filter(models.Categories.Id == category_id).first()
        category.Name = req.name
        category.Description = req.description
        self.context.commit()
        return category

