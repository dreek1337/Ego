import datetime
from uuid import UUID

import pytest  # type: ignore
from src_users.application import (
    AvatarDTO,
    SetAvatarData,
    UserIsNotExist,
    UserService,
)
from src_users.domain import UserAggregate
from src_users.domain.user.exceptions import InvalidAvatarType
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
async def test_set_avatar_correct(
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

    set_avatar_data = SetAvatarData(
        avatar_type="png",
        avatar_user_id=0,
        avatar_content=b"0",
        avatar_id=UUID("b17ce188-b222-435b-a161-8c114b23b37b"),
    )

    set_avatar_result = await user_service.set_avatar(data=set_avatar_data)

    assert set_avatar_result == AvatarDTO(
        avatar_id=UUID("b17ce188-b222-435b-a161-8c114b23b37b"),
        avatar_type="png",
        avatar_user_id=0,
    )
    assert uow.commit_status is True
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_set_avatar_with_unsupported_type(
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

    set_avatar_data = SetAvatarData(
        avatar_type="gif",
        avatar_user_id=0,
        avatar_content=b"0",
        avatar_id=UUID("b17ce188-b222-435b-a161-8c114b23b37b"),
    )

    with pytest.raises(InvalidAvatarType):
        await user_service.set_avatar(data=set_avatar_data)
    assert uow.commit_status is False
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_set_avatar_with_not_exist_user(
    uow: UserUoWMock, mapper: MapperImpl, cloud_storage_repo: UserCloudStorageMock
) -> None:
    user_service = UserService(uow=uow, mapper=mapper, cloud_storage=cloud_storage_repo)

    set_avatar_data = SetAvatarData(
        avatar_type="png",
        avatar_user_id=0,
        avatar_content=b"0",
        avatar_id=UUID("b17ce188-b222-435b-a161-8c114b23b37b"),
    )

    with pytest.raises(UserIsNotExist):
        await user_service.set_avatar(data=set_avatar_data)
    assert uow.commit_status is False
    assert uow.rollback_status is False
