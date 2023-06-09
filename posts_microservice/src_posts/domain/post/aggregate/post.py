from dataclasses import (
    dataclass,
    field,
)
from datetime import datetime

from src_posts.domain.common import Aggregate
from src_posts.domain.post.value_objects import (
    CreatorId,
    PostId,
)


@dataclass
class PostAggregate(Aggregate):
    creator_id: CreatorId
    text_content: str
    post_id: PostId | None = field(default=None)
    created_at: datetime = field(default=datetime.now())

    @classmethod
    def create_post(
        cls, *, creator_id: CreatorId, text_content: str
    ) -> "PostAggregate":
        """
        Создание поста
        """
        return PostAggregate(creator_id=creator_id, text_content=text_content)

    def update_post(self, text_content: str) -> None:
        """
        Обновление поста
        """
        self.text_content = text_content
