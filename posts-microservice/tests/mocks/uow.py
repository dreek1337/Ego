from src.application import PostUoW
from tests.mocks.post_repo import PostRepoMock
from tests.mocks.post_reader import PostReaderMock


class PostUoWMock(PostUoW):
    def __init__(
            self,
            *,
            post_repo: PostRepoMock,
            post_reader: PostReaderMock
    ) -> None:
        super().__init__(post_repo=post_repo, post_reader=post_reader)
        self.post_repo = post_repo
        self.post_reader = post_reader
