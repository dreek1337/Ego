import pytest
from fastapi_jwt_auth.exceptions import RefreshTokenRequired  # type: ignore
from src.application import AuthService
from src.config.schemas.token_models import AccessToken
from src.config.schemas.user_models import UserIdData
from tests import mocks as m


@pytest.mark.asyncio
async def test_correct_refresh_jwt(
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
    auth_jwt.set_refresh_token(ref_token=tokens.refresh_token)

    token_manager.add_jwt_data(token_data=tokens)

    auth_service = AuthService(
        uow=uow,
        token_manager=token_manager,
        password_manager=password_manager
    )

    new_access_token = await auth_service.refresh_token(authorize=auth_jwt)

    assert new_access_token == AccessToken(access_token='new_token')
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_incorrect_refresh_jwt_with_bad_refresh(
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
    bad_refresh_token = 'bad_token'
    auth_jwt.set_refresh_token(ref_token=bad_refresh_token)

    token_manager.add_jwt_data(token_data=tokens)

    auth_service = AuthService(
        uow=uow,
        token_manager=token_manager,
        password_manager=password_manager
    )

    with pytest.raises(RefreshTokenRequired):
        await auth_service.refresh_token(authorize=auth_jwt)

    assert uow.commit_status is False
    assert uow.rollback_status is False
