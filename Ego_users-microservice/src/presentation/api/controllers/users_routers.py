from typing import Union

from fastapi import (
    status,
    Depends,
    APIRouter
)

from src.domain.user import exceptions as exc
from src.domain.user.exceptions import UserIsDeleted
from src.presentation.api.di import get_service_stub
from src.presentation.api.controllers import request as req
from src.presentation.api.controllers import response as resp
from src.application.user.service.user_service import UserService
from src.application import (
    UserIsNotExist,
    UserIdIsAlreadyExist
)


user_routers = APIRouter(
    tags=['users'],
    prefix='/users'
)


@user_routers.get(
    path='/info/{user_id}',
    responses={
        status.HTTP_200_OK: {'model': resp.UserDataResponse},
        status.HTTP_404_NOT_FOUND: {'model': resp.ErrorResult[UserIsNotExist]}
    },
    response_model=resp.UserDataResponse,
    status_code=status.HTTP_200_OK
)
async def get_user(
        request_data: req.GetUserRequest = Depends(),
        service: UserService = Depends(get_service_stub)
):
    """
    Получение данных о пользователе с помощью его id
    """
    return await service.get_user(data=request_data)


@user_routers.post(
    path='/create_user',
    responses={
        status.HTTP_201_CREATED: {'model': resp.UserDataResponse},
        status.HTTP_400_BAD_REQUEST: {
            'model': resp.ErrorResult[
                Union[
                    exc.InvalidGender,
                    exc.InvalidBirthdayDate
                ]
            ]
        },
        status.HTTP_409_CONFLICT: {
            'model': resp.ErrorResult[UserIdIsAlreadyExist]
        }
    },
    response_model=resp.UserDataResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
        user_data: req.CreateUserRequest,
        service: UserService = Depends(get_service_stub)
):
    """
    Создание пользователя
    """
    return await service.create_user(data=user_data)


@user_routers.patch(
    path='/update_user_info',
    responses={
        status.HTTP_200_OK: {'model': resp.UserDataResponse},
        status.HTTP_400_BAD_REQUEST: {
            'model': resp.ErrorResult[
                Union[
                    exc.InvalidGender,
                    exc.InvalidBirthdayDate
                ]
            ]
        },
        status.HTTP_409_CONFLICT: {
            "model": resp.ErrorResult[UserIsDeleted]
        }
    },
    status_code=status.HTTP_200_OK,
    response_model=resp.UserDataResponse
)
async def update_user_info(
        update_data: req.UpdateUserRequest,
        service: UserService = Depends(get_service_stub)
):
    """
    Обновление данных пользователя
    """
    return await service.update_user(data=update_data)


@user_routers.delete(
    path='/delete_user',
    responses={
        status.HTTP_200_OK: {'model': resp.DeletedUserResponse},
        status.HTTP_404_NOT_FOUND: {"model": resp.ErrorResult[UserIsNotExist]},
        status.HTTP_409_CONFLICT: {
            "model": resp.ErrorResult[UserIsDeleted]
        }
    },
    status_code=status.HTTP_200_OK,
    response_model=resp.DeletedUserResponse
)
async def delete_user(
        request_data: req.DeleteUserRequest,
        service: UserService = Depends(get_service_stub)
):
    """
    Удаление пользователя
    """
    return await service.delete_user(data=request_data)
