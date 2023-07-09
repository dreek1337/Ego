import datetime

import pytest  # type: ignore
from src_users.application import (
    UpdateUserData,
    UserDTO,
    UserService,
)
from src_users.domain import UserAggregate
from src_users.domain.common import (
    Empty,
    GenderValue,
)
from src_users.domain.user.exceptions import UserIsDeleted
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
async def test_correct_full_update_user(
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

    update_data = UpdateUserData(
        user_id=0,
        first_name="Новое_имя",
        last_name="Новая_фамилия",
        gender=GenderValue.FEMALE,
        birthday=datetime.date(year=2001, month=6, day=25),
    )

    updated_user = await user_service.update_user(data=update_data)

    assert updated_user == UserDTO(
        user_id=0,
        first_name="Новое_имя",
        last_name="Новая_фамилия",
        gender="female",
        birthday=datetime.date(year=2001, month=6, day=25),
        avatar_path=None,
        count_of_subscriptions=0,
        count_of_subscribers=0,
        deleted=False,
    )
    assert uow.commit_status is True
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_correct_only_name_update_user(
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

    update_data = UpdateUserData(
        user_id=0,
        first_name="Новое_имя",
        last_name=Empty.UNSET,
        gender=Empty.UNSET,
        birthday=Empty.UNSET,
    )

    updated_user = await user_service.update_user(data=update_data)

    assert updated_user == UserDTO(
        user_id=0,
        first_name="Новое_имя",
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
async def test_update_deleted_user(
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

    update_data = UpdateUserData(user_id=0, first_name="Новое_имя")

    with pytest.raises(UserIsDeleted):
        await user_service.update_user(data=update_data)
    assert uow.commit_status is False
    assert uow.rollback_status is False
