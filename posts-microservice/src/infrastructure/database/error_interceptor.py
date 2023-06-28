from functools import wraps
from typing import (
    Any,
    Callable
)

from elasticsearch.exceptions import ElasticsearchException

from src.application.common.exceptions import RepoError


def error_interceptor(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        try:
            return await func(*args, **kwargs)
        except ElasticsearchException as err:
            raise RepoError() from err

    return wrapper
