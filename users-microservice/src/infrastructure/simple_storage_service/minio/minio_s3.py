from src.application import SetAvatarData
from src.application.user.constant import AvatarCloudEnum
from src.application.user.s3 import UserCloudStorage
from src.domain import AvatarEntity

from ..error_interceptor import error_interceptor
from ..minio.base import MinioCloudStorageImpl


class UserCloudStorageImpl(UserCloudStorage, MinioCloudStorageImpl):
    """
    Реализация работы с с3
    """

    @error_interceptor(file_name=__name__)
    async def put(self, avatar: SetAvatarData) -> None:
        """
        Сохранение файла в с3
        """
        bucket = AvatarCloudEnum.BUCKET.value
        key = (
            f"{AvatarCloudEnum.FOLDER.value}/"
            f"{avatar.avatar_user_id}."
            f"{avatar.avatar_type}"
        )

        async with self._connection() as client:
            await client.delete_object(Bucket=bucket, Key=key)
            await client.put_object(Bucket=bucket, Key=key, Body=avatar.avatar_content)

    @error_interceptor(file_name=__name__)
    async def delete(self, avatar: AvatarEntity) -> None:
        """
        Удаление файла с с3
        """
        bucket = AvatarCloudEnum.BUCKET.value
        key = (
            f"{AvatarCloudEnum.FOLDER.value}/"
            f"{avatar.avatar_user_id.to_int}."
            f"{avatar.avatar_type}"
        )

        async with self._connection() as client:
            await client.delete_object(Bucket=bucket, Key=key)
