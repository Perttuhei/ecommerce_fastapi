from pydantic import BaseModel


class UserDto(BaseModel):
    id: int
    username: str
    role: str

class UpdateUserDto(BaseModel):
    username: str

class AddUserReqDto(BaseModel):
    UserName: str
    Password: str
    Role: str

class LoginReqDto(BaseModel):
    username: str
    password: str

class LoginResDto(BaseModel):
    token: str
    user: UserDto

class ApiLoginResDto(BaseModel):
    token: str
    user: UserDto
