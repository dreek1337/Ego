from src_users.application import UserIsNotExist, UserRepo
from src_users.domain import UserAggregate
from src_users.domain.user.value_objects import UserId


class UserRepoMock(UserRepo):
    """
    Мок для работы с пользователем
    """

    def __init__(self) -> None:
        self.users: dict[UserId, UserAggregate] = dict()

    async def get_user_by_id(self, user_id: UserId) -> UserAggregate:
        """
        Получение пользователя с помощью id
        """
        for user in self.users.values():
            if user.user_id == user:
                return user
        raise UserIsNotExist(user_id=user_id.to_int)

    async def update_user(self, user: UserAggregate) -> None:
        """
        Обновление данных пользователя
        """
        self.users[user.user_id] = user

    async def create_user(self, user: UserAggregate) -> None:
        """
        Создание пользователя
        """
        self.users[user.user_id] = user
