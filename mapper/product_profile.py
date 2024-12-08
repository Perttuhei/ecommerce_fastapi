import inspect
from typing import Type, List
from pydantic import BaseModel
import models
from mapper.base_profile import BaseProfile


class ProductProfile(BaseProfile):
    exclude = ['metadata']

    def __init__(self, dst_type: Type[BaseModel]):
        self.dst_type = dst_type

    def map(self, data: models.Products):
        significant_vars = self._get_significant_vars(data)
        product_dto = self.dst_type(**significant_vars)

        return product_dto

    def map_list(self, data: List[models.Products]):
        items = []

        for row in data:
            significant_vars = self._get_significant_vars(row)
            items.append(self.dst_type(**significant_vars))
        return items


    def _get_significant_vars(self, data):
        fields = {}

        for key, value in inspect.getmembers(data):
            if not key.startswith('__') and not key.startswith('_') and not callable(
                    value) and key not in self.exclude:

                fields[key.lower()] = type(value)


        v = vars(data)
        significant_vars = {}
        for key, value in v.items():
            if key.lower() not in fields:
                continue
            significant_vars[key.lower()] = value
        return significant_vars