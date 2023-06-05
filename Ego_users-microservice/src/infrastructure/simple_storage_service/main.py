from aiobotocore.session import get_session, ClientCreatorContext  # type: ignore

from src.infrastructure.simple_storage_service.config import MinioConfig


def sss_session_factory(config: MinioConfig) -> ClientCreatorContext:
    """
    Создает подключение к хранилищу
    """
    session = get_session()
    # Возможно нужно будет прокинуть регион
    client_context = session.create_client(
        's3',
        **config.dict()
    )

    return client_context
