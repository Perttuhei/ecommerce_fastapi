from pydantic import BaseModel


class UserDto(BaseModel):
    id: int
    username: str
    role: str
