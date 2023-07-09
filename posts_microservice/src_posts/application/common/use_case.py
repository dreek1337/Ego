from abc import ABC

from pydantic import BaseModel


class UseCaseData(ABC, BaseModel):
    """Базовый класс для данных использующихся в юз кейсах"""


class UseCase(ABC):
    """Базовый класс UseCase"""
