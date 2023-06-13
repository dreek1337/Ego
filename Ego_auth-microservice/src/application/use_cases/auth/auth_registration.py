from src.common import BaseUseCase
from src.application.uow import AuthUoW
from src.config import (
    UsernameData,
    CreateUserData
)


class RegistrationUserUseCase(BaseUseCase):
    def __init__(self, uow: AuthUoW):
        self._uow = uow

    async def __call__(self, data: CreateUserData) -> UsernameData:
        await self._uow.user_repo.create_user(data=data)
        await self._uow.commit()

        return UsernameData(username=data.username)
