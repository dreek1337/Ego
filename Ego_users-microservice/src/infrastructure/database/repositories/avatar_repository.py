from src.application import AvatarRepo
from src.domain import AvatarEntity
from src.domain.user.value_objects import UserId
from src.infrastructure.database.repositories.base import SQLAlchemyRepo


class AvatarRepoImpl(SQLAlchemyRepo, AvatarRepo):
    async def get_avatar_by_id(self, user_id: UserId) -> AvatarEntity:
        return None  # type: ignore

    async def set_avatar(
            self,
            *,
            user_id: UserId,
            avatar: AvatarEntity
    ) -> None:
        pass

    async def update_avatar(self, avatar: AvatarEntity) -> None:
        pass
