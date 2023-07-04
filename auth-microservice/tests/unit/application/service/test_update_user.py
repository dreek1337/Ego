import pytest
from pydantic import EmailStr

from tests import mocks as m
from src.application import AuthService
from src.application.exceptions import UserIsNotExists
from src.config.schemas.user_models import (
    UserModel,
    UserIdData,
    UsernameData,
    UpdateUserData
)


@pytest.mark.asyncio
async def test_correct_update_user_password(
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

    user = UserModel(
        user_id=0,
        salt='my_salt',
        username='test_user',
        password='qwerty1337my_salthashed_hashed',
        user_email=EmailStr('qwerty@mail.ru')
    )

    uow.user_repo.add_user(user=user)  # type: ignore

    data = UpdateUserData(
        password='new_password'
    )  # type: ignore

    update_data = await auth_service.update_user_data(data=data, authorize=auth_jwt)

    assert update_data == UsernameData(username='test_user')
    assert uow.commit_status is True
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_correct_update_user_email(
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

    user = UserModel(
        user_id=0,
        salt='my_salt',
        username='test_user',
        password='qwerty1337my_salthashed_hashed',
        user_email=EmailStr('qwerty@mail.ru')
    )

    uow.user_repo.add_user(user=user)  # type: ignore

    data = UpdateUserData(
        user_email=EmailStr('qwerty@gmail.com')
    )  # type: ignore

    update_data = await auth_service.update_user_data(data=data, authorize=auth_jwt)

    assert update_data == UsernameData(username='test_user')
    assert uow.commit_status is True
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_correct_update_user_email_and_password(
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

    user = UserModel(
        user_id=0,
        salt='my_salt',
        username='test_user',
        password='qwerty1337my_salthashed_hashed',
        user_email=EmailStr('qwerty@mail.ru')
    )

    uow.user_repo.add_user(user=user)  # type: ignore

    data = UpdateUserData(
        password='qwerty1337qwerty',
        user_email=EmailStr('qwerty@gmail.com')
    )

    update_data = await auth_service.update_user_data(data=data, authorize=auth_jwt)

    assert update_data == UsernameData(username='test_user')
    assert uow.commit_status is True
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_not_found_user_for_update(
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

    data = UpdateUserData(
        password='qwerty1337qwerty',
        user_email=EmailStr('qwerty@gmail.com')
    )

    with pytest.raises(UserIsNotExists):
        await auth_service.update_user_data(data=data, authorize=auth_jwt)

    assert uow.commit_status is False
    assert uow.rollback_status is False
