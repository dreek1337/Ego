from dataclasses import (
    field,
    dataclass
)


from src.domain.user.entities import AvatarEntity
from src.domain.user.exceptions import UserIsDeleted
from src.domain.common import (
    Empty,
    Aggregate
)
from src.domain.user.value_objects import (
    UserId,
    UserGender,
    UserBirthday
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

    def set_count_of_subscribers(self, count_of_subscribers: int) -> None:
        """
        Подсчет кол-ва подписчиков у пользователя
        """
        self.count_of_subscribers = count_of_subscribers

    def set_count_of_subscriptions(self, count_of_subscriptions: int) -> None:
        """
        Подсчет кол-ва подписок у пользователя
        """
        self.count_of_subscriptions = count_of_subscriptions

    def set_avatar(self, avatar: AvatarEntity | None) -> None:
        """
        Установка аватара
        """
        if avatar:
            self.avatar = avatar

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
