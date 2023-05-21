from src.application.profile import dto
from src.application.profile.uow import ProfileUoW
from src.domain.profile.value_objects import ProfileId
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class DeleteProfileData(UseCaseData):
    profile_id: int

    class Config:
        frozen = True


class DeleteProfile(BaseUseCase):
    def __init__(
            self,
            *,
            uow: ProfileUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: DeleteProfileData) -> dto.DeletedProfile:
        """
        Создание профиля
        """
        profile = await self._uow.profile_repo.get_profile_by_id(profile_id=ProfileId(data.profile_id))

        profile.delete_profile()
        await self._uow.profile_repo.update_profile(profile)
        await self._uow.commit()

        profile_dto = self._mapper.load(profile, dto.DeletedProfile)

        return profile_dto
