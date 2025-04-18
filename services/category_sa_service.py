import models
from custom_exceptions.category_exist_exception import CategoryExistsException
from custom_exceptions.not_found_exception import NotFoundException
from dtos.categories import AddCategoryReqDto, CategoryDto, UpdateCategoryReqDto
from services.category_service_base import CategoryServiceBase


class CategorySaService(CategoryServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def get_all(self):
        categories = self.context.query(models.Categories).all()
        return categories

    def add_category(self, req: AddCategoryReqDto, user_id) -> models.Categories:
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

    def update_category(self, req: UpdateCategoryReqDto, category_id) -> models.Categories:
        category_exists = self.context.query(models.Categories).filter(models.Categories.Name == req.name).first()
        if category_exists is not None:
            raise CategoryExistsException(f"category {req.name} already exists")
        category = self.context.query(models.Categories).filter(models.Categories.Id == category_id).first()
        category.Name = req.name
        category.Description = req.description
        self.context.commit()
        return category

    def delete_category(self, category_id: int) -> str:
        # id perusteella haetaan kategoria ja tuotteet, jos löytyy niin poistetaan
        category = self.context.query(models.Categories).filter(models.Categories.Id == category_id).first()
        if category is None:
            raise NotFoundException(f"category ID: {category_id} not found")
        self.context.query(models.Products).where(models.Products.CategoryId == category_id).delete()
        self.context.delete(category)
        self.context.commit()
        return "delete ok"

