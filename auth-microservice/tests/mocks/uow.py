from src.application.auth_uow import AuthUoW
from tests.mocks.user_repo import UserRepoMock


class UnitOfWorkMock(AuthUoW):
    def __init__(self, user_repo: UserRepoMock) -> None:
        self.user_repo = user_repo
        self.commit_status = False
        self.rollback_status = False

        super().__init__(user_repo)

    async def commit(self) -> None:
        if self.rollback_status:
            raise ValueError("You can't commit after rollback!")
        self.commit_status = True

    async def rollback(self) -> None:
        if self.commit_status:
            raise ValueError("You can't rollback after commit!")
        self.rollback_status = True
