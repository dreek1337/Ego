from fastapi import (
    FastAPI,
    Request,
    status,
)
from fastapi.responses import ORJSONResponse
from fastapi_jwt_auth.exceptions import AuthJWTException  # type: ignore
from src_auth.application.exceptions import (
    UserDataIsNotCorrect,
    UserIsNotExists,
    UsernameIsAlreadyExist,
)
from src_auth.common import BaseAppException
from src_auth.common.exceptions import BaseJWTException

from .responses.exception_responses import ErrorResult


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AuthJWTException, handle_jwt_error)
    app.add_exception_handler(UserIsNotExists, user_id_is_not_exists_handler)
    app.add_exception_handler(UsernameIsAlreadyExist, username_already_exist_handler)
    app.add_exception_handler(UserDataIsNotCorrect, user_data_is_not_correct_handler)
    app.add_exception_handler(Exception, unsupported_handler)


async def user_data_is_not_correct_handler(
    request: Request, err: UserDataIsNotCorrect
) -> ORJSONResponse:
    return await handle_app_error(
        err=err, request=request, status_code=status.HTTP_404_NOT_FOUND
    )


async def username_already_exist_handler(
    request: Request, err: UsernameIsAlreadyExist
) -> ORJSONResponse:
    return await handle_app_error(
        err=err, request=request, status_code=status.HTTP_409_CONFLICT
    )


async def user_id_is_not_exists_handler(
    request: Request, err: UserIsNotExists
) -> ORJSONResponse:
    return await handle_app_error(
        err=err, request=request, status_code=status.HTTP_404_NOT_FOUND
    )


async def unsupported_handler(request: Request, err: Exception) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(message="Unknown server error has occurred", data="Use Debug!"),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


async def handle_app_error(
    *, request: Request, status_code: int, err: BaseAppException
) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(data=err, message=err.message),
        status_code=status_code,
    )


async def handle_jwt_error(
    request: Request, err: BaseJWTException, *args, **kwargs
) -> ORJSONResponse:
    print()
    return ORJSONResponse(
        ErrorResult(message=err.message, data="JWTException"),
        status_code=err.status_code,
    )
