from abc import (
    ABC,
    abstractmethod
)
from typing import (
    Any,
    TypeVar,
    Generic
)

DataToUse = TypeVar('DataToUse', bound=Any)
ResultData = TypeVar('ResultData', bound=Any)


class RepositoryBase(ABC, Generic[ResultData]):
    """Базовый класс для репозитория"""
    @abstractmethod
    async def get_user_by_id(self, data: DataToUse) -> ResultData:
        """Получение пользователя по айли"""

    @abstractmethod
    async def create_user(self, data: DataToUse) -> int:
        """Создание пользователя"""

    @abstractmethod
    async def update_user(self, data: DataToUse) -> None:
        """Обнавление данных пользователя"""
