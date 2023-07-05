from src.application.exceptions import (UserDataIsNotCorrect, UserIsNotExists,
                                        UsernameIsAlreadyExist)
from src.common import UserRepo
from src.config.schemas.user_models import UserModel, UserSaveDataInDB


class UserRepoMock(UserRepo):
    """
    Мок для репозитория
    """
    def __init__(self) -> None:
        self.users: dict[int, UserModel] = dict()

    async def get_user_by_id(self, user_id: int) -> UserModel:
        """
        Получение пользователя по айли
        """
        user = self.users.get(user_id)

        if not user:
            raise UserIsNotExists(user_id=user_id)

        return user

    async def get_user_by_username(self, username: str) -> UserModel:
        """
        Получение пользователя по никнейму
        """
        for user in self.users.values():
            if user.username == username:
                return user
        raise UserDataIsNotCorrect()

    async def create_user(self, data: UserSaveDataInDB) -> None:
        """
        Создание пользователя
        """
        for user in self.users.values():
            if user.username == data.username:
                raise UsernameIsAlreadyExist(username=data.username)

        self.users[0] = UserModel(user_id=0, **data.dict())

    async def update_user(self, data: UserModel) -> None:
        """
        Обнавление данных пользователя
        """
        self.users[data.user_id] = data

    def add_user(self, user: UserModel) -> None:
        """
        Добавление пользователя для тестирования
        """
        self.users[user.user_id] = user
