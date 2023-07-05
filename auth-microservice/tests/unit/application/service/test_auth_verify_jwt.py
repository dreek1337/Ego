import pytest
from fastapi_jwt_auth.exceptions import JWTDecodeError  # type: ignore
from src.application import AuthService
from src.config.schemas.user_models import UserIdData
from tests import mocks as m


@pytest.mark.asyncio
async def test_correct_verify_jwt(
        uow: m.UnitOfWorkMock,
        auth_jwt: m.AuthJWTMock,
        user_repo: m.UserRepoMock,
        token_manager: m.AccessTokenManagerMock,
        password_manager: m.PasswordManagerMock
) -> None:
    user_id = 0
    tokens = token_manager.create_tokens(
        authorize=auth_jwt,
        subject=UserIdData(user_id=user_id)
    )
    auth_jwt.set_access_token(acc_token=tokens.access_token)

    token_manager.add_jwt_data(token_data=tokens)

    auth_service = AuthService(
        uow=uow,
        token_manager=token_manager,
        password_manager=password_manager
    )

    verify_token_data = await auth_service.verify_token(authorize=auth_jwt)

    assert verify_token_data == user_id
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_incorrect_verify_with_bad_acc_token(
        uow: m.UnitOfWorkMock,
        auth_jwt: m.AuthJWTMock,
        user_repo: m.UserRepoMock,
        token_manager: m.AccessTokenManagerMock,
        password_manager: m.PasswordManagerMock
) -> None:
    user_id = 0
    tokens = token_manager.create_tokens(
        authorize=auth_jwt,
        subject=UserIdData(user_id=user_id)
    )
    bab_acc_token = 'bad_token'
    auth_jwt.set_access_token(acc_token=bab_acc_token)

    token_manager.add_jwt_data(token_data=tokens)

    auth_service = AuthService(
        uow=uow,
        token_manager=token_manager,
        password_manager=password_manager
    )

    with pytest.raises(JWTDecodeError):
        await auth_service.verify_token(authorize=auth_jwt)

    assert uow.commit_status is False
    assert uow.rollback_status is False
