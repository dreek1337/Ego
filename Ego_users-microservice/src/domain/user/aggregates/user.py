from typing import Self

from dataclasses import (
    dataclass,
    field
)


from src.domain.common import Empty
from src.domain.user.exceptions import UserIsDeleted
from src.domain.user.value_objects import (
    UserGender,
    UserBirthday,
    UserId
)
from src.domain.user.entities import (
    FileEntity,
    SubscriptionEntity,
    SubscriberEntity
)


@dataclass
class UserAggregate:
    """
    Полная модель пользователя
    """
    user_id: UserId
    first_name: str
    last_name: str
    gender: UserGender
    birthday: UserBirthday
    photo: FileEntity | None = field(default=None)
    subscriptions: list[SubscriptionEntity] | None = field(default=None)
    subscribers: list[SubscriberEntity] | None = field(default=None)
    deleted: bool = field(default=False)

    @classmethod
    def create_user(
            cls,
            *,
            user_id: UserId,
            first_name: str,
            last_name: str,
            gender: UserGender,
            birthday: UserBirthday,
    ) -> Self:
        """
        Создание модели пользователя
        """
        user = UserAggregate(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birthday=birthday
        )

        return user

    @property
    def full_name(self) -> str:
        """
        Отображение полного имени
        """
        return f"{self.first_name} {self.last_name}"

    @property
    def count_of_subscriptions(self) -> int:
        """
        Колличество подписок
        """
        if self.subscriptions:
            return len(self.subscriptions)

        return 0

    @property
    def count_of_subscribers(self) -> int:
        """
        Колличество подписчиков
        """
        if self.subscribers:
            return len(self.subscribers)

        return 0

    def update(
            self,
            *,
            first_name: str | Empty = Empty.UNSET,
            last_name: str | Empty = Empty.UNSET,
            gender: UserGender | Empty = Empty.UNSET,
            birthday: UserBirthday | Empty = Empty.UNSET,
    ) -> None:
        """
        Обнавление информации, пользователя
        """
        self._check_on_delete()

        if first_name is not Empty.UNSET:
            self.first_name = first_name
        if last_name is not Empty.UNSET:
            self.last_name = last_name
        if gender is not Empty.UNSET:
            self.gender = gender
        if birthday is not Empty.UNSET:
            self.birthday = birthday

    def delete_user(self) -> None:
        self.deleted = True

    def _check_on_delete(self) -> None:
        if self.deleted:
            raise UserIsDeleted(self.user_id.to_int)
