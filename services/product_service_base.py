import abc


class ProductServiceBase(abc.ABC):

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_all_by_category_id(self, category_id):
        raise NotImplementedError()