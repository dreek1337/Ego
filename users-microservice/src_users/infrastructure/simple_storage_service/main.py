from typing import AsyncContextManager, Callable

from aiobotocore.session import ClientCreatorContext  # type: ignore
from aiobotocore.session import get_session
from src_users.infrastructure import MinioConfig


def s3_factory(cloud_config: MinioConfig) -> Callable[..., AsyncContextManager]:
    """
    Создание клинта для minio
    """

    def create_client() -> ClientCreatorContext:
        """
        Создает подключение к хранилищу
        """
        session = get_session()

        client_context = session.create_client("s3", **cloud_config.dict())

        return client_context

    return create_client
