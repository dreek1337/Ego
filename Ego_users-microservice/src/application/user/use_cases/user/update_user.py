from datetime import date

from src.application.user import dto
from src.application.user.uow import UserUoW
from src.domain.common.constants import (
    Empty,
    GenderValue
)
from src.domain.user.value_objects import (
    UserId,
    UserGender,
    UserBirthday
)
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class UpdateUserData(UseCaseData):
    user_id: int
    first_name: str | Empty
    last_name: str | Empty
    gender: GenderValue | Empty
    birthday: date | Empty

    class Config:
        frozen = True


class UpdateUser(BaseUseCase):
    """
    Обнавление пользователя
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: UpdateUserData) -> dto.UpdatedUserDTO:
        user = await self._uow.user_repo.get_user_by_id(
            user_id=UserId(value=data.user_id)
        )
        user_gender: UserGender | Empty = (
            UserGender(value=data.gender)
            if data.gender is not Empty.UNSET
            else Empty.UNSET
        )
        user_birthday: UserBirthday | Empty = (
            UserBirthday(value=data.birthday)
            if data.birthday is not Empty.UNSET
            else Empty.UNSET
        )

        user.update(
            first_name=data.first_name,
            last_name=data.last_name,
            gender=user_gender,
            birthday=user_birthday
        )
        await self._uow.user_repo.update_user(user=user)
        await self._uow.commit()

        updated_user_dto = self._mapper.load(
            from_model=user,
            to_model=dto.UpdatedUserDTO
        )

        return updated_user_dto
