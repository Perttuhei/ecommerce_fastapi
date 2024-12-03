from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
from services.service_factory import UserService

router = APIRouter(
    prefix='/api/users',
    tags=['users']
)


@router.get('/')
def get_all_users(service: UserService):
    users = service.get_all()
    return users