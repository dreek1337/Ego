from src.application import CloudStorageBase, SetAvatarData
from src.infrastructure.simple_storage_service.constant import AvatarCloudEnum
from src.infrastructure.simple_storage_service.error_inteceptor import error_interceptor
from src.infrastructure.simple_storage_service.minio.base import MinioBase


class CloudStorageImpl(MinioBase, CloudStorageBase):
    """
    Реализация работы с с3
    """
    @error_interceptor(file_name=__name__)
    async def put(self, data: SetAvatarData) -> None:
        """
        Сохранение файла в с3
        """
        bucket = AvatarCloudEnum.BUCKET.value
        key = f'{AvatarCloudEnum.FOLDER}/{data.avatar_name}.{data.avatar_type}'

        await self._session.put_object(
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
        key = f'{AvatarCloudEnum.FOLDER}/{data.avatar_name}.{data.avatar_type}'

        await self._session.delete_object(
            Bucket=bucket,
            Key=key
        )
