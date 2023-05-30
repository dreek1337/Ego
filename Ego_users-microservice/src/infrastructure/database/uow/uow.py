from sqlalchemy.ext.asyncio import AsyncSession

from src.application import UserUoW
from src.infrastructure.database import repositories as repo
from src.infrastructure.database.uow.base import SQLAlchemyBaseUoW


class SQLAlchemyUoW(SQLAlchemyBaseUoW, UserUoW):
    def __init__(
            self,
            *,
            session: AsyncSession,
            user_repo: repo.UserRepoImpl,
            avatar_repo: repo.AvatarRepoImpl,
            subscription_repo: repo.SubscriptionRepoImpl
    ) -> None:
        self.user_repo = user_repo
        self.avatar_repo = avatar_repo
        self.subscription_repo = subscription_repo

        super().__init__(session=session)
