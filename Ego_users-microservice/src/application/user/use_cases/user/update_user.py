from src.application.user import dto
from src.domain.common.constants import Empty
from src.application.user.uow import UserUoW
from src.domain.user.value_objects import UserId
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)


class UpdateUserData(UseCaseData):
    user_id: int
    first_name: str | Empty = Empty.UNSET
    last_name: str | Empty = Empty.UNSET
    gender: str | Empty = Empty.UNSET
    birthday: str | Empty = Empty.UNSET

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
        user = await self._uow.user_repo.get_user_by_id(user_id=UserId(value=data.user_id))

        user.update(
            first_name=data.first_name,
            last_name=data.last_name,
            gender=data.gender,
            birthday=data.birthday
        )
        await self._uow.user_repo.update_user(user=user)
        await self._uow.commit()

        updated_user_dto = self._mapper.load(data=user, model=dto.UpdatedUserDTO)

        return updated_user_dto
