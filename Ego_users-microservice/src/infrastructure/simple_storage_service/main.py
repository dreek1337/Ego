from aiobotocore.session import get_session, ClientCreatorContext  # type: ignore

from src.application.user.constant import AvatarCloudEnum
from src.infrastructure.simple_storage_service.config import MinioConfig
from src.infrastructure.simple_storage_service.error_inteceptor import error_interceptor
from src.application import (
    SetAvatarData,
    CloudStorageBase
)


class CloudStorageImpl(CloudStorageBase):
    """
    Реализация работы с с3
    """
    def __init__(self, cloud_config: MinioConfig) -> None:
        self._cloud_config = cloud_config

    @error_interceptor(file_name=__name__)
    async def put(self, data: SetAvatarData) -> None:
        """
        Сохранение файла в с3
        """
        bucket = AvatarCloudEnum.BUCKET.value
        key = f'{AvatarCloudEnum.FOLDER.value}/{data.avatar_user_id}.{data.avatar_type}'

        async with self._create_client() as client:
            await client.delete_object(
                Bucket=bucket,
                Key=key
            )
            await client.put_object(
                Bucket=bucket,
                Key=key,
                Body=data.avatar_content
            )

    @error_interceptor(file_name=__name__)
    async def delete(self, data) -> None:
        """
        Удаление файла с с3
        """
        bucket = AvatarCloudEnum.BUCKET.value
        key = f'{AvatarCloudEnum.FOLDER.value}/{data.avatar_user_id}.{data.avatar_type}'

        async with self._create_client() as client:
            await client.delete_object(
                Bucket=bucket,
                Key=key
            )

    def _create_client(self) -> ClientCreatorContext:
        """
        Создает подключение к хранилищу
        """
        session = get_session()

        client_context = session.create_client(
            's3',
            **self._cloud_config.dict()
        )

        return client_context
