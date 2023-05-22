from datetime import datetime

from pydantic import BaseModel

from src.domain import UserAggregate
from src.application.user import dto
from src.application.user.uow import UserUoW
from src.application.common import (
    Mapper,
    BaseUseCase,
    UseCaseData
)
from src.domain.user.value_objects import (
    UserId,
    UserGender,
    UserBirthday
)


class CreateUserData(UseCaseData):
    user_id: int
    first_name: str
    last_name: str
    gender: str
    birthday: datetime

    class Config:
        frozen = True


class CreateUser(BaseUseCase):
    """
    Создание пользователя
    """
    def __init__(
            self,
            *,
            uow: UserUoW,
            mapper: Mapper
    ) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: CreateUserData) -> dto.CreatedUserDTO:
        user = UserAggregate.create_user(
            user_id=UserId(value=data.user_id),
            first_name=data.first_name,
            last_name=data.last_name,
            gender=UserGender(data.gender),
            birthday=UserBirthday(data.birthday)
        )

        await self._uow.user_repo.create_user(user=user)
        await self._uow.commit()

        user_dto = self._mapper.load(data=user, model=dto.CreatedUserDTO)

        return user_dto
