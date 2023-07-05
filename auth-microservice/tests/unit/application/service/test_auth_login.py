import pytest
from pydantic import EmailStr
from src.application import AuthService
from src.application.exceptions import UserDataIsNotCorrect
from src.config.schemas.token_models import TokensData
from src.config.schemas.user_models import LoginSchema, UserModel
from tests import mocks as m


@pytest.mark.asyncio
async def test_correct_login(
        uow: m.UnitOfWorkMock,
        auth_jwt: m.AuthJWTMock,
        user_repo: m.UserRepoMock,
        token_manager: m.AccessTokenManagerMock,
        password_manager: m.PasswordManagerMock
) -> None:
    auth_service = AuthService(
        uow=uow,
        token_manager=token_manager,
        password_manager=password_manager
    )

    user = UserModel(
        user_id=0,
        salt='my_salt',
        username='test_user',
        password='qwerty1337my_salthashed_hashed',
        user_email=EmailStr('qwerty@mail.ru')
    )

    uow.user_repo.add_user(user=user)  # type: ignore

    data = LoginSchema(
        username='test_user',
        password='qwerty1337'
    )

    login_data = await auth_service.login_user(data=data, authorize=auth_jwt)

    assert login_data == TokensData(
        access_token='some.0',
        refresh_token='some_refresh',
        access_token_expires=2
    )
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_incorrect_login_with_bad_password(
        uow: m.UnitOfWorkMock,
        auth_jwt: m.AuthJWTMock,
        user_repo: m.UserRepoMock,
        token_manager: m.AccessTokenManagerMock,
        password_manager: m.PasswordManagerMock
) -> None:
    auth_service = AuthService(
        uow=uow,
        token_manager=token_manager,
        password_manager=password_manager
    )

    user = UserModel(
        user_id=0,
        salt='my_salt',
        username='test_user',
        password='qwerty1337my_salthashed_hashed',
        user_email=EmailStr('qwerty@mail.ru')
    )

    uow.user_repo.add_user(user=user)  # type: ignore

    data = LoginSchema(
        username='test_user',
        password='incorrect_password'
    )

    with pytest.raises(UserDataIsNotCorrect):
        await auth_service.login_user(
            data=data,
            authorize=auth_jwt
        )
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_incorrect_login_with_bad_login(
        uow: m.UnitOfWorkMock,
        auth_jwt: m.AuthJWTMock,
        user_repo: m.UserRepoMock,
        token_manager: m.AccessTokenManagerMock,
        password_manager: m.PasswordManagerMock
) -> None:
    auth_service = AuthService(
        uow=uow,
        token_manager=token_manager,
        password_manager=password_manager
    )

    user = UserModel(
        user_id=0,
        salt='my_salt',
        username='test_user',
        password='qwerty1337my_salthashed_hashed',
        user_email=EmailStr('qwerty@mail.ru')
    )

    uow.user_repo.add_user(user=user)  # type: ignore

    data = LoginSchema(
        username='incorrect_username',
        password='qwerty1337'
    )

    with pytest.raises(UserDataIsNotCorrect):
        await auth_service.login_user(
            data=data,
            authorize=auth_jwt
        )
    assert uow.commit_status is False
    assert uow.rollback_status is False
