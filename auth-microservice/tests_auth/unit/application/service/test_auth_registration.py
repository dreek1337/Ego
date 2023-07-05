import pytest
from pydantic import EmailStr
from src_auth.application import AuthService
from src_auth.application.exceptions import UsernameIsAlreadyExist
from src_auth.config.schemas.token_models import TokensData
from src_auth.config.schemas.user_models import CreateUserData, UserModel
from tests_auth import mocks as m


@pytest.mark.asyncio
async def test_correct_registration_user(
    uow: m.UnitOfWorkMock,
    auth_jwt: m.AuthJWTMock,
    user_repo: m.UserRepoMock,
    token_manager: m.AccessTokenManagerMock,
    password_manager: m.PasswordManagerMock,
) -> None:
    auth_service = AuthService(
        uow=uow, token_manager=token_manager, password_manager=password_manager
    )

    data = CreateUserData(
        username="test_user",
        password="qwerty1337",
        user_email=EmailStr("qwerty@mail.ru"),
    )

    complete_registration_data = await auth_service.registration_user(
        authorize=auth_jwt, data=data
    )

    assert complete_registration_data == TokensData(
        access_token="some.0", refresh_token="some_refresh", access_token_expires=2
    )
    assert uow.commit_status is True
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_incorrect_registration_user(
    uow: m.UnitOfWorkMock,
    auth_jwt: m.AuthJWTMock,
    user_repo: m.UserRepoMock,
    token_manager: m.AccessTokenManagerMock,
    password_manager: m.PasswordManagerMock,
) -> None:
    auth_service = AuthService(
        uow=uow, token_manager=token_manager, password_manager=password_manager
    )

    user = UserModel(
        user_id=123,
        salt="my_salt",
        username="test_user",
        password="qwerty1337my_salthashed_hashed",
        user_email=EmailStr("qwerty@mail.ru"),
    )

    uow.user_repo.add_user(user=user)  # type: ignore

    data = CreateUserData(
        username="test_user",
        password="qwerty1337",
        user_email=EmailStr("qwerty@mail.ru"),
    )

    with pytest.raises(UsernameIsAlreadyExist):
        await auth_service.registration_user(authorize=auth_jwt, data=data)
    assert uow.commit_status is False
    assert uow.rollback_status is False
