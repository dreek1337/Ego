from typing import Self

from dataclasses import (
    field,
    dataclass
)


from src.domain.common import Empty
from src.domain.user.exceptions import UserIsDeleted
from src.domain.user.value_objects import (
    UserId,
    UserGender,
    UserBirthday
)
from src.domain.user.entities import (
    AvatarEntity,
    SubscriberEntity,
    SubscriptionEntity
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
    subscribers: list[SubscriberEntity] | None = field(default=None)
    subscriptions: list[SubscriptionEntity] | None = field(default=None)
    avatar: AvatarEntity | None = field(default=None)
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

    def count_of_subscribers(self) -> int:
        """
        Подсчет кол-ва подписчиков у пользователя
        """
        if self.subscribers:
            return len(self.subscribers)

        return 0

    def count_of_subscriptions(self) -> int:
        """
        Подсчет кол-ва подписок у пользователя
        """
        if self.subscriptions:
            return len(self.subscriptions)

        return 0

    def set_avatar(self, avatar: AvatarEntity | None) -> None:
        """
        Установка аватара
        """
        if avatar:
            self.avatar = avatar

    def set_subscribers(self, subscribers: list[SubscriberEntity] | None) -> None:
        """
        Установка подпичсиков
        """
        if subscribers:
            self.subscribers = subscribers

    def set_subscriptions(self, subscriptions: list[SubscriptionEntity] | None) -> None:
        """
        Установка подписок
        """
        if subscriptions:
            self.subscriptions = subscriptions

    def delete_user(self) -> None:
        """
        Удаление пользователя
        """
        self.deleted = True

    def _check_on_delete(self) -> None:
        """
        Проверка на удаленного пользователя
        """
        if self.deleted:
            raise UserIsDeleted(self.user_id.to_int)
