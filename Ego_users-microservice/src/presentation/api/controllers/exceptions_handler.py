from fastapi import status
from fastapi import FastAPI
from starlette.requests import Request
from fastapi.responses import ORJSONResponse

from src.presentation.api.controllers.response import ErrorResult
from src.application import (
    UserIsNotExist,
    UserIdIsAlreadyExist
)
from src.domain.user.exceptions import (
    InvalidGender,
    UserIsDeleted,
    InvalidBirthdayDate,
)


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, exception_handler)


async def exception_handler(request: Request, err: Exception) -> ORJSONResponse:
    if isinstance(err, (UserIsNotExist,)):
        return ORJSONResponse(
            ErrorResult(message=err.message, data=err).dict(),
            status_code=status.HTTP_404_NOT_FOUND
        )
    elif isinstance(
            err,
            (InvalidGender,
             InvalidBirthdayDate)
    ):
        return ORJSONResponse(
            ErrorResult(message=err.message, data=err).dict(),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    elif isinstance(err, (UserIdIsAlreadyExist, UserIsDeleted)):
        return ORJSONResponse(
            ErrorResult(message=err.message, data=err).dict(),
            status_code=status.HTTP_409_CONFLICT
        )
    else:
        return ORJSONResponse(
            ErrorResult(
                message="Unknown server error has occurred",
                data=err
            ).dict(),
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
