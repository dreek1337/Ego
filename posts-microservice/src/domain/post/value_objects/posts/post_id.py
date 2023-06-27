from dataclasses import dataclass

from src.domain.common import ValueObject


@dataclass(frozen=True)
class PostId(ValueObject[str]):
    value: str

    @property
    def get_value(self) -> str:
        """
        Получение значения
        """
        return self.value
