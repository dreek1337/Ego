from abc import ABC

from src_posts.application.common import UnitOfWork
from src_posts.application.posts.interfaces import (
    PostReader,
    PostRepo,
)


class PostUoW(UnitOfWork, ABC):
    def __init__(self, *, post_repo: PostRepo, post_reader: PostReader) -> None:
        self.post_repo = post_repo
        self.post_reader = post_reader
