import abc
from typing import Any

import models


class TokenToolBase(abc.ABC):
    @abc.abstractmethod
    def create_token(self, data: dict[str, Any]) -> str:
        raise NotImplementedError()