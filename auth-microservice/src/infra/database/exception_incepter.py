from functools import wraps
from typing import (
    Any,
    Callable
)

from sqlalchemy.exc import SQLAlchemyError

from src.application.exceptions import RepoError


def error_interceptor(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        try:
            return await func(*args, **kwargs)
        except SQLAlchemyError as err:
            raise RepoError() from err
    return wrapper
