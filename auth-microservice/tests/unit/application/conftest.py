import pytest

from tests import mocks as m


@pytest.fixture
def user_repo() -> m.UserRepoMock:
    return m.UserRepoMock()


@pytest.fixture
def uow(user_repo: m.UserRepoMock) -> m.UnitOfWorkMock:
    return m.UnitOfWorkMock(user_repo=user_repo)


@pytest.fixture
def auth_jwt() -> m.AuthJWTMock:
    return m.AuthJWTMock()


@pytest.fixture
def token_manager() -> m.AccessTokenManagerMock:
    return m.AccessTokenManagerMock()


@pytest.fixture
def password_manager() -> m.PasswordManagerMock:
    return m.PasswordManagerMock()
