from src.application.uow import AuthUoW
from src.application.exceptions import UserDataIsNotCorrect
from src.common import (
    TokenMaker,
    BaseUseCase
)
from src.config import (
    TokensData,
    UserIdData,
    LoginSchema
)
from src.infra import verify_password


class UserLoginUseCase(BaseUseCase):
    def __init__(self, uow: AuthUoW, token_maker: TokenMaker):
        self._uow = uow
        self._token_maker = token_maker

    async def __call__(self, data: LoginSchema) -> TokensData:
        user = await self._uow.user_repo.get_user_by_username(
            username=data.username
        )

        check_on_correct_password = verify_password(
            plain_password=data.password + user.salt,
            hashed_password=user.password
        )

        if not check_on_correct_password:
            raise UserDataIsNotCorrect()

        tokens = self._token_maker.create_tokens(
            subject=UserIdData(user_id=user.user_id)
        )

        return tokens
