import pytest  # type: ignore
from src_users.application import (
    SubscribeActionDTO,
    SubscribeOnYourself,
    UserIsNotExist,
    UserService,
)
from src_users.application.user.use_cases import SubscribeData
from src_users.infrastructure import MapperImpl
from tests_users.mocks import (
    UserCloudStorageMock,
    UserUoWMock,
)


@pytest.mark.asyncio
async def test_subscribe_correct(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    uow.subscription_repo.add_users(users_id=[0, 1])  # type: ignore

    subscribe_data = SubscribeData(subscription_id=0, subscriber_id=1)

    subscribe_result = await user_service.subscribe(data=subscribe_data)

    assert subscribe_result == SubscribeActionDTO(subscription_id=0, subscriber_id=1)
    assert uow.commit_status is True
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_subscribe_on_yourself(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    subscribe_data = SubscribeData(subscription_id=0, subscriber_id=0)
    with pytest.raises(SubscribeOnYourself):
        await user_service.subscribe(data=subscribe_data)
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_subscribe_with_not_exist_user(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    uow.subscription_repo.add_users(users_id=[0])  # type: ignore

    subscribe_data = SubscribeData(subscription_id=0, subscriber_id=1)

    with pytest.raises(UserIsNotExist):
        await user_service.subscribe(data=subscribe_data)
    assert uow.commit_status is False
    assert uow.rollback_status is False
