from src.application.profile import dto
from src.domain.common.constants import Empty
from src.application.profile.uow import ProfileUoW
from src.domain.profile.value_objects import ProfileId
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class UpdateProfileData(UseCaseData):
    profile_id: int
    first_name: str | Empty = Empty.UNSET
    last_name: str | Empty = Empty.UNSET
    gender: str | Empty = Empty.UNSET
    birthday: str | Empty = Empty.UNSET

    class Config:
        frozen = True


class UpdateProfile(BaseUseCase):
    def __init__(
            self,
            *,
            uow: ProfileUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: UpdateProfileData) -> dto.UpdatedProfile:
        """
        Создание профиля
        """
        profile = await self._uow.profile_repo.get_profile_by_id(profile_id=ProfileId(data.profile_id))

        profile.update(
            first_name=data.first_name,
            last_name=data.last_name,
            gender=data.gender,
            birthday=data.birthday
        )
        await self._uow.profile_repo.update_profile(profile)
        await self._uow.commit()

        profile_dto = self._mapper.load(profile, dto.UpdatedProfile)

        return profile_dto
