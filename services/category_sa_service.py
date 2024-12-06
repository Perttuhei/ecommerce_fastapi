import models
from services.category_service_base import CategoryServiceBase


class CategorySaService(CategoryServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def get_all(self):
        categories = self.context.query(models.Categories).all()
        return categories