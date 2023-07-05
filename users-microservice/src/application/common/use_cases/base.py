from abc import ABC

from pydantic import BaseModel


class UseCaseData(ABC, BaseModel):
    """Модель данных для UseCase"""


class BaseUseCase(ABC):
    """Базовй класс Юзкейса"""
