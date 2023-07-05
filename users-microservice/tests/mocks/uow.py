from src import application as app


class UserUoWMock(app.UserUoW):
    """
    Мок для работы с uow
    """

    def __init__(
        self,
        *,
        user_repo: app.UserRepo,
        avatar_repo: app.AvatarRepo,
        subscription_repo: app.SubscriptionRepo,
        subscription_reader: app.SubscriptionReader,
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
