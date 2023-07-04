from src.application import UnitOfWork
from tests.mocks.post_repo import PostRepoMock
from tests.mocks.post_reader import PostReaderMock


class PostUoWMock(UnitOfWork):
    def __init__(
            self,
            *,
            post_repo: PostRepoMock,
            post_reader: PostReaderMock
    ) -> None:
        self.post_repo = post_repo
        self.post_reader = post_reader
