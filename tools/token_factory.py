from typing import Annotated

from fastapi import Depends

from tools.symmetric_token import SymmetricToken
from tools.token_tool_base import TokenToolBase


def create_token():
    return SymmetricToken()

AppToken = Annotated[TokenToolBase, Depends(create_token)]