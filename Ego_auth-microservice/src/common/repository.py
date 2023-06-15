from abc import (
    ABC,
    abstractmethod
)

from src.config.schemas.user_models import (
    UserModel,
    UserSaveDataInDB
)


class RepositoryBase(ABC):
    """Базовый класс для репозитория"""
    @abstractmethod
    async def get_user_by_id(self, user_id: int) -> UserModel:
        """Получение пользователя по айли"""

    @abstractmethod
    async def get_user_by_username(self, username: str) -> UserModel:
        """Получение пользователя по никнейму"""

    @abstractmethod
    async def create_user(self, data: UserSaveDataInDB) -> None:
        """Создание пользователя"""

    @abstractmethod
    async def update_user(self, data: UserModel) -> None:
        """Обнавление данных пользователя"""
