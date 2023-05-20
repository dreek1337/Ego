from typing import Self
from dataclasses import (
    dataclass,
    field
)

from src.domain.common import Empty
from src.domain.profile.exceptions import UserIsDeleted
from src.domain.profile.value_objects import (
    UserGender,
    UserBirthday,
    ProfileId
)
from src.domain.profile.entities import (
    FileEntity,
    PostEntity,
    SubscriptionEntity,
    SubscriberEntity
)


@dataclass
class ProfileAggregator:
    """
    Полная модель пользователя
    """
    profile_id: ProfileId
    first_name: str
    last_name: str
    gender: UserGender
    birthday: UserBirthday
    photo: FileEntity | None
    posts: list[PostEntity] | None
    subscriptions: list[SubscriptionEntity] | None
    subscribers: list[SubscriberEntity] | None
    deleted: bool = field(default=False)

    @classmethod
    def create_profile(
            cls,
            *,
            profile_id: ProfileId,
            first_name: str,
            last_name: str,
            gender: UserGender,
            birthday: UserBirthday,
            photo: FileEntity | None = None,
            posts: list[PostEntity] | None = None,
            subscriptions: list[SubscriptionEntity] | None = None,
            subscribers: list[SubscriberEntity] | None = None
    ) -> Self:
        """
        Создание модели пользователя
        """
        user = ProfileAggregator(
            profile_id=profile_id,
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
            photo: FileEntity | None | Empty = Empty.UNSET,
            posts: list[PostEntity] | None | Empty = Empty.UNSET,
            subscriptions: list[SubscriptionEntity] | None | Empty = Empty.UNSET,
            subscribers: list[SubscriberEntity] | None | Empty = Empty.UNSET
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

    def delete_profile(self) -> None:
        self.deleted = True

    def _check_on_delete(self) -> None:
        if self.deleted:
            raise UserIsDeleted(self.profile_id.to_int)
