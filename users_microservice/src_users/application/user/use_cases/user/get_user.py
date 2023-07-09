from src_users.application.common import (
    BaseUseCase,
    Mapper,
    UseCaseData,
)
from src_users.application.user import dto
from src_users.application.user.constant import AvatarCloudEnum
from src_users.application.user.uow import UserUoW
from src_users.domain.user.value_objects import (
    AvatarUserId,
    UserId,
)


class GetUserData(UseCaseData):
    user_id: int

    class Config:
        frozen = True


class GetUser(BaseUseCase):
    """
    Получение пользователя
    """

    def __init__(self, *, uow: UserUoW, mapper: Mapper) -> None:
        self._mapper = mapper
        self._uow = uow

    async def __call__(self, data: GetUserData) -> dto.UserDTO:
        user = await self._uow.user_repo.get_user_by_id(
            user_id=UserId(value=data.user_id)
        )
        avatar = await self._uow.avatar_repo.get_avatar_by_user_id(
            avatar_user_id=AvatarUserId(value=user.user_id.to_int)
        )
        subscribers_cnt = await self._uow.subscription_reader.get_count_subscribers(
            subscription_id=user.user_id.to_int
        )
        subscriptions_cnt = await self._uow.subscription_reader.get_count_subscriptions(
            subscriber_id=user.user_id.to_int
        )

        avatar_path = (
            f"{AvatarCloudEnum.FOLDER.value}/{avatar.get_full_avatar_name()}"
            if avatar
            else None
        )
        user.set_avatar(avatar_path=avatar_path)
        user.set_count_of_subscribers(count_of_subscribers=subscribers_cnt)
        user.set_count_of_subscriptions(count_of_subscriptions=subscriptions_cnt)

        user_dto = self._mapper.load(from_model=user, to_model=dto.UserDTO)

        return user_dto
