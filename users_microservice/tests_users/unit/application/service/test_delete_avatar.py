import datetime
from uuid import UUID

import pytest  # type: ignore
from src_users.application import (
    AvatarIsNotExist,
    DeleteAvatarData,
    DeletedAvatarDTO,
    SetAvatarData,
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
async def test_delete_avatar_correct(
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

    await user_service.set_avatar(data=set_avatar_data)

    delete_avatar_data = DeleteAvatarData(avatar_user_id=0)

    delete_avatar_result = await user_service.delete_avatar(data=delete_avatar_data)

    assert delete_avatar_result == DeletedAvatarDTO(
        avatar_id=UUID("b17ce188-b222-435b-a161-8c114b23b37b")
    )
    assert uow.commit_status is True
    assert uow.rollback_status is False


@pytest.mark.asyncio
async def test_delete_avatar_without_avatar(
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

    delete_avatar_data = DeleteAvatarData(avatar_user_id=0)

    with pytest.raises(AvatarIsNotExist):
        await user_service.delete_avatar(data=delete_avatar_data)
    assert uow.commit_status is False
    assert uow.rollback_status is False
