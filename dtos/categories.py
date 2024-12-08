from pydantic import BaseModel


class CategoryDto(BaseModel):
    id: int
    name: str
    userid: int
    description: str

class AddCategoryReqDto(BaseModel):
    name: str
    description: str

class UpdateCategoryDto(BaseModel):
    name: str
    description: str
