from fastapi import (
    status,
    FastAPI,
    Request
)
from fastapi.responses import ORJSONResponse

from src.domain.common import AbstractBaseException
from src.presentation.api.controllers.response import ErrorResult
from src.application import (
    UserIsNotExist,
    AvatarIsNotExist,
    SubscribeOnYourself,
    SubscribeIsNotExists,
    UserIdIsAlreadyExist,
    SubscribeIsAlreadyExists
)
from src.domain.user.exceptions import (
    InvalidGender,
    UserIsDeleted,
    InvalidAvatarType,
    InvalidBirthdayDate
)


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, unsupported_handler)
    app.add_exception_handler(InvalidGender, invalid_gender_handler)
    app.add_exception_handler(UserIsDeleted, user_is_deleted_handler)
    app.add_exception_handler(UserIsNotExist, user_is_not_exist_handler)
    app.add_exception_handler(SubscribeOnYourself, sub_on_yourself_handler)
    app.add_exception_handler(AvatarIsNotExist, avatar_is_not_exist_handler)
    app.add_exception_handler(SubscribeIsNotExists, sub_is_not_exist_handler)
    app.add_exception_handler(InvalidAvatarType, invalid_avatar_type_handler)
    app.add_exception_handler(InvalidBirthdayDate, invalid_birthday_date_handler)
    app.add_exception_handler(UserIdIsAlreadyExist, user_id_is_already_exist_handler)
    app.add_exception_handler(SubscribeIsAlreadyExists, sub_is_already_exist_handler)


async def invalid_gender_handler(
        request: Request,
        err: InvalidGender
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_400_BAD_REQUEST
    )


async def user_is_deleted_handler(
        request: Request,
        err: UserIsDeleted
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_409_CONFLICT
    )


async def user_is_not_exist_handler(
        request: Request,
        err: UserIsNotExist
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_404_NOT_FOUND
    )


async def avatar_is_not_exist_handler(
        request: Request,
        err: AvatarIsNotExist
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_404_NOT_FOUND
    )


async def invalid_avatar_type_handler(
        request: Request,
        err: InvalidAvatarType
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_409_CONFLICT
    )


async def invalid_birthday_date_handler(
        request: Request,
        err: InvalidBirthdayDate
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_409_CONFLICT
    )


async def sub_on_yourself_handler(
        request: Request,
        err: SubscribeOnYourself
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_400_BAD_REQUEST
    )


async def sub_is_not_exist_handler(
        request: Request,
        err: SubscribeIsNotExists
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_404_NOT_FOUND
    )


async def user_id_is_already_exist_handler(
        request: Request,
        err: UserIdIsAlreadyExist
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_409_CONFLICT
    )


async def sub_is_already_exist_handler(
        request: Request,
        err: SubscribeIsAlreadyExists
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_409_CONFLICT
    )


async def unsupported_handler(
        request: Request,
        err: Exception
) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(message="Unknown server error has occurred", data="Use Debug!"),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


async def handle_app_error(
        *,
        request: Request,
        status_code: int,
        err: AbstractBaseException
) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(
            data=err,
            message=err.message
        ),
        status_code=status_code,
    )
