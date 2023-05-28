from dataclasses import dataclass

from src.domain.common import ValueObject, GenderValue
from src.domain.user.exceptions import InvalidGender


@dataclass(frozen=True)
class UserGender(ValueObject[GenderValue]):
    value: GenderValue

    @property
    def get_value(self) -> GenderValue:
        """
        Получение значения
        """
        return self.value

    def _validate(self) -> None:
        """
        Проверка на тип пола
        """
        if self.value != GenderValue.MALE or self.value != GenderValue.FEMALE:
            raise InvalidGender(gender_type=self.value)
