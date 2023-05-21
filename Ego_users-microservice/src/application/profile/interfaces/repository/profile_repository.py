from abc import (
    ABC,
    abstractmethod
)

from src.domain import ProfileAggregat
from src.domain.profile.value_objects import ProfileId


class ProfileRepo(ABC):
    """
    Репозиторий профиля
    """
    @abstractmethod
    async def get_profile_by_id(self, profile_id: ProfileId) -> ProfileAggregat:
        """Получение профиля с помощью id"""

    @abstractmethod
    async def update_profile(self, profile: ProfileAggregat) -> None:
        """Обновление данных профиля"""

    @abstractmethod
    async def create_profile(self, profile: ProfileAggregat) -> None:
        """Создание профиля"""
