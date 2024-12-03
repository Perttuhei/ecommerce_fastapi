import abc


class UserServiceBase(abc.ABC):

    @abc.abstractmethod
    def get_all(self):
        raise NotImplementedError()