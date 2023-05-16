from abc import (
    ABC,
    abstractmethod
)

from src.domain import ProfileAggregator


class ProfileRepo(ABC):
    """
    Репозиторий профиля
    """
    @abstractmethod
    async def get_profile_by_id(self, profile_id: int) -> ProfileAggregator:
        """Получение профиля с помощью id"""

    @abstractmethod
    async def update_profile(self, profile: ProfileAggregator) -> None:
        """Обновление данных профиля"""

    @abstractmethod
    async def create_profile(self, profile: ProfileAggregator) -> None:
        """Создание профиля"""
