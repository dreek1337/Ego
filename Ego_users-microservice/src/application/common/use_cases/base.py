from abc import (
    ABC,
    abstractmethod
)
from pydantic import BaseModel


class UseCaseData(BaseModel, ABC):
    """Модель данных для UseCase"""


class BaseUseCase(ABC):
    @abstractmethod
    async def __call__(self, data: UseCaseData):
        """Вызов логики"""
