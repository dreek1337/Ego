from dataclasses import dataclass

from src.domain.common import ValueObject


@dataclass(frozen=True)
class CreatorId(ValueObject[int]):
    value: int

    def get_value(self) -> int:
        """
        Получение значения
        """
        return self.value
