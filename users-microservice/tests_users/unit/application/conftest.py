import pytest  # type: ignore
from src_users.infrastructure import (
    MapperImpl,
    create_mapper,
)
from tests_users.mocks import (
    AvatarRepoMock,
    SubscriptionReaderMock,
    SubscriptionRepoMock,
    UserCloudStorageMock,
    UserRepoMock,
    UserUoWMock,
)


@pytest.fixture
def mapper() -> MapperImpl:
    return create_mapper()


@pytest.fixture
def user_repo() -> UserRepoMock:
    return UserRepoMock()


@pytest.fixture
def avatar_repo() -> AvatarRepoMock:
    return AvatarRepoMock()


@pytest.fixture
def cloud_storage_repo() -> UserCloudStorageMock:
    return UserCloudStorageMock()


@pytest.fixture
def subscription_repo() -> SubscriptionRepoMock:
    return SubscriptionRepoMock()


@pytest.fixture
def subscription_reader() -> SubscriptionReaderMock:
    return SubscriptionReaderMock()


@pytest.fixture
def uow(
    user_repo: UserRepoMock,
    avatar_repo: AvatarRepoMock,
    subscription_repo: SubscriptionRepoMock,
    subscription_reader: SubscriptionReaderMock,
) -> UserUoWMock:
    return UserUoWMock(
        user_repo=user_repo,
        subscription_repo=subscription_repo,
        subscription_reader=subscription_reader,
        avatar_repo=avatar_repo,
    )
