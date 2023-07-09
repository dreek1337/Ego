import datetime

import pytest
from src_users.application import (
    GetSubscriptionsOrder,
    SubscriptionDTO,
    SubscriptionsDTO,
    UserService,
)
from src_users.application.user.use_cases import GetSubscriptionsData
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
async def test_get_subscriptions_correct_with_sup(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    users_for_sup = [
        SubscriptionDTO(
            user_id=1,
            first_name="Евгений",
            last_name="Пригожин",
            avatar=None,
            deleted=True,
        ),
        SubscriptionDTO(
            user_id=2,
            first_name="Владимир",
            last_name="Царский",
            avatar=None,
            deleted=False,
        ),
    ]

    uow.subscription_reader.add_users(users=users_for_sup)  # type: ignore

    user = UserAggregate(
        user_id=UserId(value=0),
        first_name="Danila",
        last_name="Safonov",
        gender=UserGender(value="male"),
        birthday=UserBirthday(value=datetime.date.today()),
        deleted=True,
    )

    await uow.user_repo.create_user(user=user)

    subscriptions = [
        SubscriptionDTO(
            user_id=0,
            first_name="Danila",
            last_name="Safonov",
            avatar=None,
            deleted=False,
        )
    ]

    for user_id in range(1, 3):
        uow.subscription_reader.add_subscriptions(  # type: ignore
            user_id=user_id, subscriptions=subscriptions
        )

    get_sup_data = GetSubscriptionsData(
        user_id=0, offset=0, limit=20, order=GetSubscriptionsOrder.ASC
    )

    subscriptions_result = await user_service.get_subscriptions(data=get_sup_data)

    assert subscriptions_result == SubscriptionsDTO(
        subscriptions=[
            SubscriptionDTO(
                user_id=1,
                first_name="Евгений",
                last_name="Пригожин",
                avatar=None,
                deleted=True,
            ),
            SubscriptionDTO(
                user_id=2,
                first_name="Владимир",
                last_name="Царский",
                avatar=None,
                deleted=False,
            ),
        ],
        offset=0,
        limit=20,
    )
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_get_subscriptions_correct_without_sup(
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

    get_sup_data = GetSubscriptionsData(
        user_id=0, offset=0, limit=20, order=GetSubscriptionsOrder.ASC
    )

    subscriptions_result = await user_service.get_subscriptions(data=get_sup_data)

    assert subscriptions_result == SubscriptionsDTO(
        subscriptions=None, offset=0, limit=20
    )
    assert uow.commit_status is False
    assert uow.rollback_status is False
