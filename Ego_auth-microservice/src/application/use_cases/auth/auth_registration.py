from src.application.uow import AuthUoW
from src.common import BaseUseCase
from src.config import CreateUserData


class RegistrationUserUseCase(BaseUseCase):
    def __init__(self, uow: AuthUoW):
        self._uow = uow

    async def __call__(self, data: CreateUserData) -> None:
        await self._uow.user_repo.create_user(data=data)

        await self._uow.commit()
