from functools import wraps
from typing import (
    Any,
    Callable,
)

from sqlalchemy.exc import SQLAlchemyError
from src_users.application.common.exceptions import RepoError


def error_interceptor(file_name: str) -> Callable:
    def inner(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(*args, **kwargs) -> Any:
            try:
                return await func(*args, **kwargs)
            except SQLAlchemyError as err:
                raise RepoError(file_name=file_name) from err

        return wrapper

    return inner
