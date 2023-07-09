from src_posts.application import PostUoW
from src_posts.infrastructure.database import repositories as repo
from src_posts.infrastructure.database.uow.base import ElasticsearchUoWBase


class ElasticsearchUoW(PostUoW, ElasticsearchUoWBase):
    def __init__(
        self, *, post_repo: repo.PostRepoImpl, post_reader: repo.PostReaderImpl
    ) -> None:
        self.post_repo = post_repo
        self.post_reader = post_reader

        super().__init__(post_repo=post_repo, post_reader=post_reader)
