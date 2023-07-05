from src.application import SetAvatarData
from src.application.user.s3 import UserCloudStorage
from src.domain import AvatarEntity


class UserCloudStorageMock(UserCloudStorage):
    """
    Мок для работы с s3
    """

    async def put(self, avatar: SetAvatarData) -> None:
        """
        Сохранение объекта
        """

    async def delete(self, avatar: AvatarEntity) -> None:
        """
        Удаление объекта
        """
