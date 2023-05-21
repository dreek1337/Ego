from datetime import datetime

from src.domain import ProfileAggregat
from src.application.profile.dto import Profile
from src.application.profile.uow import ProfileUoW
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)
from src.domain.profile.value_objects import (
    ProfileId,
    UserGender,
    UserBirthday
)


class CreateProfileData(UseCaseData):
    profile_id: int
    first_name: str
    last_name: str
    gender: str
    birthday: datetime

    class Config:
        frozen = True


class CreateProfile(BaseUseCase):
    def __init__(
            self,
            *,
            uow: ProfileUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: CreateProfileData) -> Profile:
        """
        Создание профиля
        """
        profile = ProfileAggregat.create_profile(
            profile_id=ProfileId(data.profile_id),
            first_name=data.first_name,
            last_name=data.last_name,
            gender=UserGender(data.gender),
            birthday=UserBirthday(data.birthday)
        )

        await self._uow.profile_repo.create_profile(profile)
        await self._uow.commit()

        profile_dto = self._mapper.load(profile, Profile)

        return profile_dto
