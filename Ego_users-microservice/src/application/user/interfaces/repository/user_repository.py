from abc import (
    ABC,
    abstractmethod
)

from src.domain import UserAggregate
from src.domain.user.value_objects import UserId


class UserRepo(ABC):
    """
    Репозиторий пользователя
    """
    @abstractmethod
    async def get_user_by_id(self, user_id: UserId) -> UserAggregate:
        """Получение пользователя с помощью id"""

    @abstractmethod
    async def update_user(self, user: UserAggregate) -> None:
        """Обновление данных пользователя"""

    @abstractmethod
    async def create_user(self, user: UserAggregate) -> None:
        """Создание пользователя"""
