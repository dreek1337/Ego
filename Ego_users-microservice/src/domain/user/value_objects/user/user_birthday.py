from datetime import date
from dataclasses import dataclass

from src.domain.common import ValueObject
from src.domain.user.exceptions import InvalidBirthdayDate


@dataclass(frozen=True)
class UserBirthday(ValueObject[date]):
    value: date

    @property
    def get_value(self) -> date:
        """
        Получение значения
        """
        return self.value

    def _validate(self) -> None:
        """
        Проверка на то, что пользователь не может родится в будущем
        """
        if self.value > date.today():
            raise InvalidBirthdayDate(birthday_date=self.value)
