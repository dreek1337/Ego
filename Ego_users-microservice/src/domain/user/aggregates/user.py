from dataclasses import (
    field,
    dataclass
)


from src.domain.common import Empty, Aggregate
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
class UserAggregate(Aggregate):
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
    count_of_subscribers: int = field(default=0)
    count_of_subscriptions: int = field(default=0)
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
    ) -> 'UserAggregate':
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

    def set_count_of_subscribers(self) -> None:
        """
        Подсчет кол-ва подписчиков у пользователя
        """
        if self.subscribers:
            self.count_of_subscribers = len(self.subscribers)

        self.count_of_subscribers = 0

    def set_count_of_subscriptions(self) -> None:
        """
        Подсчет кол-ва подписок у пользователя
        """
        if self.subscriptions:
            self.count_of_subscriptions = len(self.subscriptions)

        self.count_of_subscriptions = 0

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
            raise UserIsDeleted(user_id=self.user_id.to_int)
