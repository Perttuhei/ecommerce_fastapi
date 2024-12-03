from typing import Annotated
from fastapi.params import Depends
from dtos.users import UserDto
from mapper.base_profile import BaseProfile
from mapper.profile_factory import create_user_profile


class Mapper:
    def __init__(self, profiles: dict[str: BaseProfile]) -> None:
        self.profiles = profiles

    def map(self, _type, data):
        if _type not in self.profiles.keys():
            raise Exception('Profile missing')

        if isinstance(data, list):
            return self.profiles[_type].map_list(data)
        else:
            return self.profiles[_type].map(data)



def create_mapper() -> Mapper:
    profiles = {
        'user_dto': create_user_profile(UserDto)
    }
    return Mapper(profiles)

ResponseMapper = Annotated[Mapper, Depends(create_mapper)]