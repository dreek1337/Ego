import datetime

import pytest  # type: ignore
from src_users.application import (
    CreateUserData,
    UserService,
)
from src_users.application.user import dto
from src_users.domain.user.exceptions import (
    InvalidBirthdayDate,
    InvalidGender,
)
from src_users.infrastructure import MapperImpl
from tests_users.mocks import (
    UserCloudStorageMock,
    UserUoWMock,
)


@pytest.mark.asyncio
async def test_create_user_correct(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    user_data = CreateUserData(
        user_id=0,
        first_name="Danila",
        last_name="Safonov",
        gender="male",
        birthday=datetime.date.today(),
    )

    created_user = await user_service.create_user(data=user_data)

    assert created_user == dto.UserDTO(
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
    assert uow.commit_status is True
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_create_user_incorrect_birthday(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    incorrect_date = {
        "year": datetime.date.today().year + 1,
        "month": datetime.date.today().month,
        "day": datetime.date.today().day,
    }

    user_data = CreateUserData(
        user_id=0,
        first_name="Danila",
        last_name="Safonov",
        gender="male",
        birthday=datetime.date(**incorrect_date),
    )

    with pytest.raises(InvalidBirthdayDate):
        await user_service.create_user(data=user_data)
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_create_user_incorrect_gender(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    user_data = CreateUserData(
        user_id=0,
        first_name="Danila",
        last_name="Safonov",
        gender="kurwa",
        birthday=datetime.date.today(),
    )

    with pytest.raises(InvalidGender):
        await user_service.create_user(data=user_data)
    assert uow.commit_status is False
    assert uow.rollback_status is False
