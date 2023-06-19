from dataclasses import dataclass

from src.domain.common import ValueObject, GenderValue
from src.domain.user.exceptions import InvalidGender


@dataclass(frozen=True)
class UserGender(ValueObject[GenderValue]):
    value: str

    @property
    def get_value(self) -> str:
        """
        Получение значения
        """
        if self.value == 'male':
            return GenderValue.MALE

        return self.value

    def _validate(self) -> None:
        """
        Проверка на тип пола
        """
        if not (self.value == GenderValue.MALE or self.value == GenderValue.FEMALE):
            raise InvalidGender(gender_type=self.value)
