from src.common import UseCase, PasswordManager
from src.application.auth_uow import AuthUoW
from src.config.schemas.user_models import (
    UsernameData,
    CreateUserData,
    UserSaveDataInDB
)


class RegistrationUserUseCase(UseCase):
    """
    Регистрация пользователя
    """
    def __init__(
            self,
            *,
            uow: AuthUoW,
            password_manager: PasswordManager
    ) -> None:
        self._uow = uow
        self._password_manager = password_manager

    async def __call__(self, data: CreateUserData) -> UsernameData:
        salt = self._password_manager.generate_salt()
        hashed_password = self._password_manager.get_password_hash(
            password=data.password + salt
        )

        create_user_data = UserSaveDataInDB(
            username=data.username,
            password=hashed_password,
            salt=salt,
            user_email=data.user_email
        )

        await self._uow.user_repo.create_user(data=create_user_data)
        await self._uow.commit()

        return UsernameData(username=data.username)
