from src.common import BaseUseCase
from src.application.uow import AuthUoW
from src.infra import (
    generate_salt,
    get_password_hash
)
from src.config import (
    UsernameData,
    CreateUserData,
    UserSaveDataInDB
)


class RegistrationUserUseCase(BaseUseCase):
    def __init__(self, uow: AuthUoW):
        self._uow = uow

    async def __call__(self, data: CreateUserData) -> UsernameData:
        salt = generate_salt()
        hashed_password = get_password_hash(
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
