from pydantic import BaseModel


class UserDto(BaseModel):
    id: int
    username: str
    role: str

class UpdateUserDto(BaseModel):
    username: str
