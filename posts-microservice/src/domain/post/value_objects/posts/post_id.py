from uuid import UUID
from dataclasses import dataclass

from src.domain.common import ValueObject


@dataclass(frozen=True)
class PostId(ValueObject[UUID]):
    value: UUID

    def get_value(self) -> UUID:
        """
        Получение значения
        """
        return self.value
