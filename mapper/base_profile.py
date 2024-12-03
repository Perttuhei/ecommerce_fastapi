import abc
from typing import List

from pydantic import BaseModel


class BaseProfile(abc.ABC):
    @abc.abstractmethod
    def map(self, item) -> BaseModel:
        raise NotImplementedError()

    @abc.abstractmethod
    def map_list(self, data: list) -> List[BaseModel]:
        raise NotImplementedError()