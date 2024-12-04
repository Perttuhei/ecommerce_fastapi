import models
from services.product_service_base import ProductServiceBase


class ProductSaService(ProductServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def get_all(self):
        products = self.context.query(models.Products).all()
        return products