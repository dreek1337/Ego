from abc import ABC
from pydantic import BaseModel


class UseCaseData(ABC, BaseModel):
    """Модель данных для UseCase"""

    class Config(ABC):
        """Конфигурации модели"""


class BaseUseCase(ABC):
    """Базовй класс Юзкейса"""
