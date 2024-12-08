import abc
from dtos.categories import AddCategoryReqDto, CategoryDto


class CategoryServiceBase(abc.ABC):

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def add_category(self, req: AddCategoryReqDto, user_id) -> CategoryDto:
        raise NotImplementedError()