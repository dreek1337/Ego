from datetime import date

from src_users.application.common import BaseUseCase, Mapper, UseCaseData
from src_users.application.user import dto
from src_users.application.user.uow import UserUoW
from src_users.domain import UserAggregate
from src_users.domain.user.value_objects import UserBirthday, UserGender, UserId


class CreateUserData(UseCaseData):
    user_id: int
    first_name: str
    last_name: str
    gender: str
    birthday: date

    class Config:
        frozen = True


class CreateUser(BaseUseCase):
    """
    Создание пользователя
    """

    def __init__(self, *, uow: UserUoW, mapper: Mapper) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: CreateUserData) -> dto.UserDTO:
        user = UserAggregate.create_user(
            user_id=UserId(value=data.user_id),
            first_name=data.first_name,
            last_name=data.last_name,
            gender=UserGender(data.gender),
            birthday=UserBirthday(data.birthday),
        )

        await self._uow.user_repo.create_user(user=user)
        await self._uow.commit()

        created_user_dto = self._mapper.load(from_model=user, to_model=dto.UserDTO)

        return created_user_dto
