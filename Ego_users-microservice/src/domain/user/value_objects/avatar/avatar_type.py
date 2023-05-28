from dataclasses import dataclass

from src.domain.common import (
    ValueObject,
    ValidAvatarType
)
from src.domain.user.exceptions import InvalidAvatarType


@dataclass(frozen=True)
class AvatarType(ValueObject[ValidAvatarType]):
    value: ValidAvatarType

    @property
    def get_value(self) -> ValidAvatarType:
        """
        Возвращает значение
        """
        return self.value

    def _validate(self) -> None:
        """
        Проверка на валидные типы файла
        """
        if self.value not in ValidAvatarType:
            raise InvalidAvatarType(file_type=self.value)
