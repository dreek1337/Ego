from src.application.profile import dto
from src.application.common import Mapper
from src.application.profile.uow import ProfileUoW
from src.application.profile.use_cases import (
    CreateProfileData,
    CreateProfile,
    DeleteProfileData,
    DeleteProfile,
    UpdateProfileData,
    UpdateProfile
)


class ProfileService:
    """
    Сервис который отвечает за работу с Профилем
    """
    def __init__(
            self,
            *,
            uow: ProfileUoW,
            mapper: Mapper
    ) -> None:
        self._uow = uow
        self._mapper = mapper

    async def create_profile(self, data: CreateProfileData) -> dto.CreatedProfile:
        return await CreateProfile(uow=self._uow, mapper=self._mapper)(data=data)

    async def delete_profile(self, data: DeleteProfileData) -> dto.DeletedProfile:
        return await DeleteProfile(uow=self._uow, mapper=self._mapper)(data=data)

    async def update_profile(self, data: UpdateProfileData) -> dto.UpdatedProfile:
        return await UpdateProfile(uow=self._uow, mapper=self._mapper)(data=data)
