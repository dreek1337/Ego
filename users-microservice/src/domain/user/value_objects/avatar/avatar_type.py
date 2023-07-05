from dataclasses import dataclass

from src.domain.common import ValidAvatarType, ValueObject
from src.domain.user.exceptions import InvalidAvatarType


@dataclass(frozen=True)
class AvatarType(ValueObject[str]):
    value: str

    @property
    def get_value(self) -> str:
        """
        Возвращает значение
        """
        return self.value

    def _validate(self) -> None:
        """
        Проверка на валидные типы файла
        """
        if self.value not in ValidAvatarType.__members__.values():
            raise InvalidAvatarType(file_type=self.value)
