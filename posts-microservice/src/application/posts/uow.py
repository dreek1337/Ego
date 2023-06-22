from abc import ABC

from src.application.posts.interfaces import (
    PostRepo,
    PostReader
)

from src.application.common import UnitOfWork


class PostUoW(UnitOfWork, ABC):
    def __init__(
            self,
            *,
            post_repo: PostRepo,
            post_reader: PostReader
    ) -> None:
        self.post_repo = post_repo
        self.post_reader = post_reader
