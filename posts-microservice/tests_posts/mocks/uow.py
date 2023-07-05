from src_posts.application import PostUoW
from tests_posts.mocks.post_reader import PostReaderMock
from tests_posts.mocks.post_repo import PostRepoMock


class PostUoWMock(PostUoW):
    def __init__(self, *, post_repo: PostRepoMock, post_reader: PostReaderMock) -> None:
        self.post_repo = post_repo
        self.post_reader = post_reader

        super().__init__(post_repo=post_repo, post_reader=post_reader)
