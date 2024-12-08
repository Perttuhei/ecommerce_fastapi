from typing import Annotated

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import Request

import models
from custom_exceptions.forbidden_exception import ForbiddenException
from custom_exceptions.unauthorized_exception import UnauthorizedException
from services.service_factory import UserService
from tools.token_factory import AppToken


oauth_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/api_login', auto_error=False)

def get_logged_in_user(service: UserService, token: AppToken, authorization: Annotated[str, Depends(oauth_scheme)] = None) -> models.Users:
    # oauth2pass... tarkistaa käyttäjän tokenin, jos authorization true ja tokenin validointi onnistuu niin haetaan käyttäjä
    if authorization is None:
        raise UnauthorizedException()
    validated = token.validate_token(authorization)
    if validated is None:
        raise UnauthorizedException()
    user = service.get_by_id(validated['sub'])
    if user is None:
        raise UnauthorizedException()
    return user

def get_moderator_user(service: UserService, token: AppToken, authorization: Annotated[str, Depends(oauth_scheme)] = None) -> models.Users:
    loggedInUser = get_logged_in_user(service, token, authorization)
    role = loggedInUser.Role
    if role != 'moderator':
        raise ForbiddenException("required moderator role")
    return loggedInUser

def get_admin_user(service: UserService, token: AppToken, authorization: Annotated[str, Depends(oauth_scheme)] = None) -> models.Users:
    loggedInUser = get_logged_in_user(service, token, authorization)
    role = loggedInUser.Role
    if role != 'admin':
        raise ForbiddenException("required admin role")
    return loggedInUser

ModeratorUser = Annotated[models.Users, Depends(get_moderator_user)]
AdminUser = Annotated[models.Users, Depends(get_admin_user)]
LoggedInUser = Annotated[models.Users, Depends(get_logged_in_user)]