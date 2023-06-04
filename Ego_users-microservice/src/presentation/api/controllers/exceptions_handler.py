from fastapi import (
    status,
    FastAPI
)
from starlette.requests import Request
from fastapi.responses import ORJSONResponse
from pydantic.error_wrappers import ValidationError

from src.presentation.api.controllers.response import ErrorResult
from src.application import (
    UserIsNotExist,
    UserIdIsAlreadyExist, AvatarIsNotExist
)
from src.domain.user.exceptions import (
    InvalidGender,
    UserIsDeleted,
    InvalidBirthdayDate,
)


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, exception_handler)


async def exception_handler(request: Request, err: Exception) -> ORJSONResponse:
    if isinstance(
            err,
            (UserIsNotExist,
             AvatarIsNotExist)
    ):
        return ORJSONResponse(
            ErrorResult(message=err.message, data=err),
            status_code=status.HTTP_404_NOT_FOUND
        )
    elif isinstance(
            err,
            (InvalidGender,
             InvalidBirthdayDate)
    ):
        return ORJSONResponse(
            ErrorResult(message=err.message, data=err),
            status_code=status.HTTP_400_BAD_REQUEST
        )
    elif isinstance(
            err,
            (UserIsDeleted,
             UserIdIsAlreadyExist)
    ):
        return ORJSONResponse(
            ErrorResult(message=err.message, data=err),
            status_code=status.HTTP_409_CONFLICT
        )
    else:
        err = parse_error(err=err)
        try:
            return ORJSONResponse(
                ErrorResult(
                    message="Unknown server error has occurred",
                    data=err
                ),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as err:
            return ORJSONResponse(
                ErrorResult(
                    message="Unknown server error, didn't parsed",
                    data=f"Use debug, to check what happened! {err}"
                ),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


def parse_error(err: Exception | ValidationError):
    if err.__class__.__context__.__objclass__ == BaseException:  # type: ignore
        err = err.args  # type: ignore
    try:
        err = err.json()  # type: ignore
    except AttributeError:
        pass

    return err
