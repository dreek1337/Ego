from typing import Union

from fastapi import (
    APIRouter,
    Depends,
    Header,
    status,
)
from src_users.application import (
    CreateUserData,
    DeleteUserData,
    GetUserData,
    UpdateUserData,
    UserIdIsAlreadyExist,
    UserIsNotExist,
)
from src_users.application.user.service.user_service import UserService
from src_users.domain.user import exceptions as exc
from src_users.domain.user.exceptions import UserIsDeleted
from src_users.presentation.api.controllers import (
    request as req,
    response as resp,
)
from src_users.presentation.api.di import get_service_stub

user_routers = APIRouter(tags=["users"], prefix="/users")


@user_routers.get(
    path="/info",
    responses={
        status.HTTP_200_OK: {"model": resp.UserDataResponse},
        status.HTTP_404_NOT_FOUND: {"model": resp.ErrorResult[UserIsNotExist]},
    },
    response_model=resp.UserDataResponse,
    status_code=status.HTTP_200_OK,
)
async def get_user(
    request_data: req.GetUserRequest = Depends(),
    service: UserService = Depends(get_service_stub),
):
    """
    Получение данных о пользователе с помощью его id
    """
    return await service.get_user(data=GetUserData(**request_data.dict()))


@user_routers.post(
    path="/create_user",
    responses={
        status.HTTP_201_CREATED: {"model": resp.UserDataResponse},
        status.HTTP_400_BAD_REQUEST: {
            "model": resp.ErrorResult[Union[exc.InvalidGender, exc.InvalidBirthdayDate]]
        },
        status.HTTP_409_CONFLICT: {"model": resp.ErrorResult[UserIdIsAlreadyExist]},
    },
    response_model=resp.UserDataResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_data: req.CreateUserRequest,
    service: UserService = Depends(get_service_stub),
    x_user_id: int = Header(None),
):
    """
    Создание пользователя
    """
    return await service.create_user(
        data=CreateUserData(user_id=x_user_id, **user_data.dict())
    )


@user_routers.patch(
    path="/update_user_info",
    responses={
        status.HTTP_200_OK: {"model": resp.UserDataResponse},
        status.HTTP_400_BAD_REQUEST: {
            "model": resp.ErrorResult[Union[exc.InvalidGender, exc.InvalidBirthdayDate]]
        },
        status.HTTP_409_CONFLICT: {"model": resp.ErrorResult[UserIsDeleted]},
    },
    status_code=status.HTTP_200_OK,
    response_model=resp.UserDataResponse,
)
async def update_user_info(
    update_data: req.UpdateUserRequest,
    service: UserService = Depends(get_service_stub),
    x_user_id: int = Header(None),
):
    """
    Обновление данных пользователя
    """
    return await service.update_user(
        data=UpdateUserData(user_id=x_user_id, **update_data.dict())
    )


@user_routers.delete(
    path="/delete_user",
    responses={
        status.HTTP_200_OK: {"model": resp.DeletedUserResponse},
        status.HTTP_404_NOT_FOUND: {"model": resp.ErrorResult[UserIsNotExist]},
        status.HTTP_409_CONFLICT: {"model": resp.ErrorResult[UserIsDeleted]},
    },
    status_code=status.HTTP_200_OK,
    response_model=resp.DeletedUserResponse,
)
async def delete_user(
    service: UserService = Depends(get_service_stub), x_user_id: int = Header(None)
):
    """
    Удаление пользователя
    """
    return await service.delete_user(data=DeleteUserData(user_id=x_user_id))
