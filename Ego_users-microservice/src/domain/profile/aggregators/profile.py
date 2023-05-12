from typing import Self
from dataclasses import (
    dataclass,
    field
)

from src.domain.common import Empty
from src.domain.profile.exceptions import UserIsDeleted
from src.domain.profile.value_objects import (
    UserGender,
    UserBirthday
)
from src.domain.profile.entities import (
    File,
    Post,
    Subscription,
    Subscriber
)


@dataclass
class ProfileAggregator:
    """
    Полная модель пользователя
    """
    user_id: int
    first_name: str
    last_name: str
    gender: UserGender
    birthday: UserBirthday
    photo: File | None
    posts: list[Post] | None
    subscriptions: list[Subscription] | None
    subscribers: list[Subscriber] | None
    deleted: bool = field(default=False)

    @classmethod
    def create_user(
            cls,
            *,
            user_id: int,
            first_name: str,
            last_name: str,
            gender: UserGender,
            birthday: UserBirthday,
            photo: File | None = None,
            posts: list[Post] | None = None,
            subscriptions: list[Subscription] | None = None,
            subscribers: list[Subscriber] | None = None
    ) -> Self:
        """
        Создание модели пользователя
        """
        user = ProfileAggregator(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            gender=gender,
            birthday=birthday,
            photo=photo,
            posts=posts,
            subscriptions=subscriptions,
            subscribers=subscribers
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
        try:
            return len(self.subscriptions)
        except TypeError:
            return 0

    @property
    def count_of_subscribers(self) -> int:
        """
        Колличество подписчиков
        """
        try:
            return len(self.subscribers)
        except TypeError:
            return 0

    def update(
            self,
            *,
            first_name: str | Empty = Empty.UNSET,
            last_name: str | Empty = Empty.UNSET,
            gender: UserGender | Empty = Empty.UNSET,
            birthday: UserBirthday | Empty = Empty.UNSET,
            photo: File | None | Empty = Empty.UNSET,
            posts: list[Post] | None | Empty = Empty.UNSET,
            subscriptions: list[Subscription] | None | Empty = Empty.UNSET,
            subscribers: list[Subscriber] | None | Empty = Empty.UNSET
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
        if photo is not Empty.UNSET:
            self.photo = photo
        if posts is not Empty.UNSET:
            self.posts = posts
        if subscriptions is not Empty.UNSET:
            self.subscriptions = subscriptions
        if subscribers is not Empty.UNSET:
            self.subscribers = subscribers

    def delete_user(self) -> None:
        self.deleted = True

    def _check_on_delete(self) -> None:
        if self.deleted:
            raise UserIsDeleted(self.user_id)
