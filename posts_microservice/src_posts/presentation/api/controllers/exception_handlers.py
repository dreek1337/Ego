from elasticsearch.exceptions import ElasticsearchException  # type: ignore
from elasticsearch.exceptions import TransportError  # type: ignore
from fastapi import (
    FastAPI,
    Request,
    status,
)
from fastapi.responses import ORJSONResponse
from src_posts.application import UserIsNotPostCreator
from src_posts.domain import AbstractBaseException
from src_posts.presentation.api.controllers.responses import ErrorResult


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(Exception, unsupported_handler)
    app.add_exception_handler(ElasticsearchException, handle_elastic_error)
    app.add_exception_handler(UserIsNotPostCreator, user_is_not_post_creator)


async def user_is_not_post_creator(
    request: Request, err: UserIsNotPostCreator
) -> ORJSONResponse:
    return await handle_app_error(
        err=err, request=request, status_code=status.HTTP_409_CONFLICT
    )


async def unsupported_handler(request: Request, err: Exception) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(message="Unknown server error has occurred", data="Use Debug!"),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


async def handle_app_error(
    *, request: Request, status_code: int, err: AbstractBaseException
) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(data=err, message=err.message),
        status_code=status_code,
    )


async def handle_elastic_error(
    request: Request,
    err: TransportError,
) -> ORJSONResponse:
    return ORJSONResponse(
        status_code=err.status_code, content={"detail": err.info}  # type: ignore
    )
