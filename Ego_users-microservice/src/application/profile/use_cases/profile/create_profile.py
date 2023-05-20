from datetime import datetime

from src.application.common.interfaces.mapper import Mapper
from src.application.common.interfaces.uow import UnitOfWork
from src.application.profile.dto import Profile
from src.application.profile.interfaces.repository.profile_repository import ProfileRepo
from src.domain import ProfileAggregator
from src.domain.profile.value_objects import (
    UserBirthday,
    UserGender,
    ProfileId
)


class CreateProfileUseCase:
    def __init__(
            self,
            *,
            profile_repo: ProfileRepo,
            uow: UnitOfWork,
            mapper: Mapper
    ) -> None:
        self._profile_repo = profile_repo
        self._mapper = mapper
        self._uow = uow

    async def __call__(
            self,
            *,
            profile_id: int,
            first_name: str,
            last_name: str,
            gender: str,
            birthday: datetime
    ) -> Profile:
        """
        Создание профиля
        """
        profile = ProfileAggregator.create_profile(
            profile_id=ProfileId(profile_id),
            first_name=first_name,
            last_name=last_name,
            gender=UserGender(gender),
            birthday=UserBirthday(birthday)
        )

        await self._profile_repo.create_profile(profile)
        await self._uow.commit()

        profile_dto = self._mapper.load(profile, Profile)

        return profile_dto
