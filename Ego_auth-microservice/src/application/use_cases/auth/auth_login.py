from typing import Any

from fastapi_jwt_auth import AuthJWT  # type: ignore

from src.infra import creat_tokens
from src.common import BaseUseCase
from src.config import LoginSchema, UserIdData
from src.application.uow import AuthUoW


class UserLoginUseCase(BaseUseCase):
    def __init__(self, uow: AuthUoW, auth_settings: AuthJWT):
        self._uow = uow
        self._auth_settings = auth_settings

    async def __call__(self, data: LoginSchema):
        user = await self._uow.user_repo.get_user_by_username(
            username=data.username
        )

        check_on_correct_password = None  # Сделать проверку пароля

        if not check_on_correct_password:
            raise Exception

        tokens = creat_tokens(
            subject=UserIdData(user_id=user.user_id),
            authorize=Any
        )

        return tokens
