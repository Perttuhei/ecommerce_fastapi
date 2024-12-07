import os
from typing import Any

import jwt

from tools.token_tool_base import TokenToolBase


class SymmetricToken(TokenToolBase):
    def create_token(self, payload: [str, Any]) -> str:
        token = jwt.encode(payload, key=os.getenv("SECRET_KEY"), algorithm='HS512')
        return token

    def validate_token(self, token_str) -> dict[str, Any]:
        return jwt.decode(token_str, key=os.getenv("SECRET_KEY"), algorithms=['HS512'])
