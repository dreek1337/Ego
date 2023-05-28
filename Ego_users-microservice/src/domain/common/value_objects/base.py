from abc import ABC
from dataclasses import dataclass
from typing import (
    Any,
    TypeVar,
    Generic
)

V = TypeVar("V", bound=Any)


@dataclass(frozen=True)
class BaseValueObject(ABC):
    """
    Базовый класс для во
    """
    def __post_init__(self) -> None:
        """
        Пост обработка, проверка на валидность данных
        """
        self._validate()

    def _validate(self) -> None:
        """Валидация данных"""


@dataclass(frozen=True)
class ValueObject(BaseValueObject, ABC, Generic[V]):
    """Абстрактный класс для во"""
