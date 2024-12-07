import os
from typing import Any

import jwt

from tools.token_tool_base import TokenToolBase


class SymmetricToken(TokenToolBase):
    def create_token(self, payload: [str, Any]) -> str:
        token = jwt.encode(payload, key=os.getenv("SECRET_KEY"), algorithm='HS512')

        return token