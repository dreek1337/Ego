from dataclasses import dataclass

from src.domain.common import (
    ValueObject,
    ValidAvatarType
)
from src.domain.user.exceptions import InvalidAvatarType


@dataclass(frozen=True)
class AvatarType(ValueObject[str]):
    value: str

    def _validate(self) -> None:
        """
        Проверка на валидные типы файла
        """
        valid_types = [file_type for file_type in ValidAvatarType]

        if self.value not in valid_types:
            raise InvalidAvatarType(file_type=self.value)
