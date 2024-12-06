import models
from dtos.products import AddProductReqDto
from services.product_service_base import ProductServiceBase


class ProductSaService(ProductServiceBase):

    def __init__(self, context: models.Db):
        self.context = context


    def get_all(self):
        products = self.context.query(models.Products).all()
        return products
    def get_all_by_category_id(self, category_id):
        products = self.context.query(models.Products).where(category_id == models.Products.CategoryId).all()
        return products
    def add_product(self, req: AddProductReqDto):
        product = models.Products(**req.model_dump())
        self.context.add(product)
        self.context.commit()
        return product
