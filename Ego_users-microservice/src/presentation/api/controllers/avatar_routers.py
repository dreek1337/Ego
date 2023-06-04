import imghdr

from fastapi import (
    status,
    Depends,
    APIRouter,
    UploadFile
)

from src.presentation.api.di import get_service_stub
from src.presentation.api.controllers import response as resp
from src.application.user.service.user_service import UserService
from src.presentation.api.controllers.request.avatar_requests import DeleteAvatarRequest
from src.application import (
    SetAvatarData,
    UserIsNotExist,
    AvatarIsNotExist,
)
from src.presentation.api.controllers.response import (
    SetAvatarResponse,
    DeletedAvatarResponse
)

avatar_routers = APIRouter(
    tags=['avatars'],
    prefix='/avatars'
)


@avatar_routers.post(
    path='/set_avatar',
    responses={
        status.HTTP_200_OK: {'model': SetAvatarResponse},
        status.HTTP_404_NOT_FOUND: {"model": resp.ErrorResult[UserIsNotExist]}
    },
    response_model=SetAvatarResponse
)
async def set_avatar(
        avatar_data: UploadFile,
        avatar_user_id: int,
        service: UserService = Depends(get_service_stub)
):
    """
    Установка аватарки у пользователя
    """
    # Сделать так, что бы все это происходило в юзкейсе
    file = avatar_data.file.read()

    data = SetAvatarData(
        avatar_content=file,
        avatar_user_id=avatar_user_id,
        avatar_type=imghdr.what(None, file)  # type: ignore
    )  # type: ignore

    return await service.set_avatar(data=data)


@avatar_routers.delete(
    path='/delete_avatar',
    responses={
        status.HTTP_200_OK: {'model': DeletedAvatarResponse},
        status.HTTP_404_NOT_FOUND: {'model': AvatarIsNotExist}
    },
    response_model=DeletedAvatarResponse
)
async def delete_avatar(
        avatar_user_id: DeleteAvatarRequest,
        service: UserService = Depends(get_service_stub)
):
    """
    Удаление аватарки у пользователя
    """
    return await service.delete_avatar(data=avatar_user_id)
