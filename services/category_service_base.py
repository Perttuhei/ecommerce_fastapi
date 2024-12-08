import abc
from dtos.categories import AddCategoryReqDto, CategoryDto, UpdateCategoryReqDto


class CategoryServiceBase(abc.ABC):

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def add_category(self, req: AddCategoryReqDto, user_id) -> CategoryDto:
        raise NotImplementedError()

    @abc.abstractmethod
    def update_category(self, req: UpdateCategoryReqDto, category_id: int) -> CategoryDto:
        raise NotImplementedError()