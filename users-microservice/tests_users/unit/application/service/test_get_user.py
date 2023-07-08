import datetime

import pytest  # type: ignore
from src_users.application import (
    GetUserData,
    SubscriptionDTO,
    UserDTO,
    UserIsNotExist,
    UserService,
)
from src_users.domain import UserAggregate
from src_users.domain.user.value_objects import (
    UserBirthday,
    UserGender,
    UserId,
)
from src_users.infrastructure import MapperImpl
from tests_users.mocks import (
    UserCloudStorageMock,
    UserUoWMock,
)


@pytest.mark.asyncio
async def test_get_user_correct(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    user = UserAggregate(
        user_id=UserId(value=0),
        first_name="Danila",
        last_name="Safonov",
        gender=UserGender(value="male"),
        birthday=UserBirthday(value=datetime.date.today()),
    )

    await uow.user_repo.create_user(user=user)

    get_data = GetUserData(user_id=0)

    user = await user_service.get_user(data=get_data)  # type: ignore

    assert user == UserDTO(
        user_id=0,
        first_name="Danila",
        last_name="Safonov",
        gender="male",
        birthday=datetime.date.today(),
        avatar_path=None,
        count_of_subscriptions=0,
        count_of_subscribers=0,
        deleted=False,
    )
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_get_user_correct_with_subs_and_sups(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)
    user_subscriptions = [
        SubscriptionDTO(
            user_id=1,
            first_name="Евгений",
            last_name="Лучший",
            avatar=None,
            deleted=False,
        )
    ]
    user_subscribes = [
        SubscriptionDTO(
            user_id=0,
            first_name="Danila",
            last_name="Safonov",
            avatar=None,
            deleted=False,
        )
    ]

    uow.subscription_reader.add_subscriptions(  # type: ignore
        user_id=0, subscriptions=user_subscriptions
    )

    for user_id in range(1, 4):
        uow.subscription_reader.add_subscriptions(  # type: ignore
            user_id=user_id, subscriptions=user_subscribes
        )

    user = UserAggregate(
        user_id=UserId(value=0),
        first_name="Danila",
        last_name="Safonov",
        gender=UserGender(value="male"),
        birthday=UserBirthday(value=datetime.date.today()),
    )

    await uow.user_repo.create_user(user=user)

    get_data = GetUserData(user_id=0)

    user = await user_service.get_user(data=get_data)  # type: ignore

    assert user == UserDTO(
        user_id=0,
        first_name="Danila",
        last_name="Safonov",
        gender="male",
        birthday=datetime.date.today(),
        avatar_path=None,
        count_of_subscriptions=3,
        count_of_subscribers=1,
        deleted=False,
    )
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_get_not_exist_user(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    get_data = GetUserData(user_id=0)

    with pytest.raises(UserIsNotExist):
        await user_service.get_user(data=get_data)
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_get__deleted_user_correct(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    user = UserAggregate(
        user_id=UserId(value=0),
        first_name="Danila",
        last_name="Safonov",
        gender=UserGender(value="male"),
        birthday=UserBirthday(value=datetime.date.today()),
        deleted=True,
    )

    await uow.user_repo.create_user(user=user)

    get_data = GetUserData(user_id=0)

    user = await user_service.get_user(data=get_data)  # type: ignore

    assert user == UserDTO(
        user_id=0,
        first_name="Danila",
        last_name="Safonov",
        gender="male",
        birthday=datetime.date.today(),
        avatar_path=None,
        count_of_subscriptions=0,
        count_of_subscribers=0,
        deleted=True,
    )
    assert uow.commit_status is False
    assert uow.rollback_status is False
