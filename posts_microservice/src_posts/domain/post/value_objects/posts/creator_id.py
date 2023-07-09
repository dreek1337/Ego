from dataclasses import dataclass

from src_posts.domain.common import ValueObject


@dataclass(frozen=True)
class CreatorId(ValueObject[int]):
    value: int

    @property
    def get_value(self) -> int:
        """
        Получение значения
        """
        return self.value
