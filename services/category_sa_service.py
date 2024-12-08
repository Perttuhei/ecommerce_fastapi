import models
from custom_exceptions.category_exist_exception import CategoryExistsException
from dtos.categories import AddCategoryReqDto, CategoryDto
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

