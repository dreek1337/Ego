from src_users import application as app
from tests_users.mocks.avatar_repo import AvatarRepoMock
from tests_users.mocks.subscription_reader import SubscriptionReaderMock
from tests_users.mocks.subscription_repo import SubscriptionRepoMock
from tests_users.mocks.user_repo import UserRepoMock


class UserUoWMock(app.UserUoW):
    """
    Мок для работы с uow
    """

    def __init__(
        self,
        *,
        user_repo: UserRepoMock,
        avatar_repo: AvatarRepoMock,
        subscription_repo: SubscriptionRepoMock,
        subscription_reader: SubscriptionReaderMock,
    ) -> None:
        self.user_repo = user_repo
        self.avatar_repo = avatar_repo
        self.subscription_repo = subscription_repo
        self.subscription_reader = subscription_reader
        self.commit_status = False
        self.rollback_status = False

        super().__init__(
            user_repo=user_repo,
            avatar_repo=avatar_repo,
            subscription_repo=subscription_repo,
            subscription_reader=subscription_reader,
        )

    async def commit(self) -> None:
        if self.rollback_status:
            raise ValueError("You can't commit after rollback!")
        self.commit_status = True

    async def rollback(self) -> None:
        if self.commit_status:
            raise ValueError("You can't rollback after commit!")
        self.rollback_status = True
