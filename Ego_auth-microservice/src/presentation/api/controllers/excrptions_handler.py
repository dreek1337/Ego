from fastapi import (
    status,
    Request,
    FastAPI
)
from fastapi.responses import ORJSONResponse

from src.application.exceptions import UsernameIsAlreadyExists, UserIdIsNotExists
from src.common import BaseAppException
from src.common.exceptions import BaseJWTException
from .responses.exception_responses import ErrorResult


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(UserIdIsNotExists, user_id_is_not_exists_handler)
    app.add_exception_handler(UsernameIsAlreadyExists, username_already_exists_handler)


async def username_already_exists_handler(
        request: Request,
        err: UsernameIsAlreadyExists
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_409_CONFLICT
    )


async def user_id_is_not_exists_handler(
        request: Request,
        err: UserIdIsNotExists
) -> ORJSONResponse:
    return await handle_app_error(
        err=err,
        request=request,
        status_code=status.HTTP_404_NOT_FOUND
    )


async def handle_app_error(
        *,
        request: Request,
        status_code: int,
        err: BaseAppException
) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(
            data=err,
            message=err.message
        ),
        status_code=status_code,
    )


async def handle_jwt_error(
        *,
        request: Request,
        status_code: int,
        err: BaseJWTException
) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=status_code,
        content={"detail": err.message}
    )
