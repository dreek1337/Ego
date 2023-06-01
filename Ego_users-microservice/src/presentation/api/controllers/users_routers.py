from fastapi import (
    # status,
    Depends,
    APIRouter
)

from src.application.user.service.user_service import UserService
from src.presentation.api.controllers.request import GetUserRequest
from src.presentation.api.controllers.request.user_requests import CreateUserRequest
from src.presentation.api.di import get_service_stub

users_router = APIRouter(
    tags=['health_check'],
    prefix="/users"
)


@users_router.get(
    path='/info/{user_id}'
)
async def get_user(
        user_id: GetUserRequest = Depends(),
        user_service: UserService = Depends(get_service_stub)
):
    user = await user_service.get_user(data=user_id)

    return user


@users_router.post(
    path='/create_user'
)
async def create_user(
        user_data: CreateUserRequest,
        user_service: UserService = Depends(get_service_stub)
):
    """
    Создание пользователя
    """
    user = await user_service.create_user(data=user_data)

    return user
