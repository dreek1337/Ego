from abc import (
    ABC,
    abstractmethod
)
from pydantic import BaseModel


class UseCaseData(ABC, BaseModel):
    """Модель данных для UseCase"""

    class Config(ABC):
        """Конфигурации модели"""


class BaseUseCase(ABC):
    @abstractmethod
    async def __call__(self, data: UseCaseData):
        """Вызов логики"""
