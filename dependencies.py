from typing import Annotated

from fastapi import Depends
from starlette.requests import Request

import models
from custom_exceptions.unauthorized_exception import UnauthorizedException
from services.service_factory import UserService
from tools.token_factory import AppToken


def get_logged_in_user(service: UserService, token: AppToken, req: Request) -> models.Users:
    token_from_header = req.headers.get('Authorization')
    if token_from_header is None:
        raise UnauthorizedException()
    header_parts = token_from_header.split(' ')
    if len(header_parts) != 2:
        raise UnauthorizedException()
    if header_parts[0] != 'Bearer':
        raise UnauthorizedException()
    claims = token.validate_token(header_parts[1])
    user = service.get_by_id(claims['sub'])
    if user is None:
        raise UnauthorizedException()
    return user

def get_moderator_user(service: UserService, token: AppToken, req: Request) -> models.Users:
    loggedInUser = get_logged_in_user(service, token, req)
    role = loggedInUser.Role
    if role != 'moderator':
        raise UnauthorizedException('moderator role required')
    return loggedInUser

def get_admin_user(service: UserService, token: AppToken, req: Request) -> models.Users:
    loggedInUser = get_logged_in_user(service, token, req)
    role = loggedInUser.Role
    if role != 'admin':
        raise UnauthorizedException('admin role required')
    return loggedInUser

ModeratorUser = Annotated[models.Users, Depends(get_moderator_user)]
AdminUser = Annotated[models.Users, Depends(get_admin_user)]
LoggedInUser = Annotated[models.Users, Depends(get_logged_in_user)]