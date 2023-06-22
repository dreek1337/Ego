from datetime import datetime
from dataclasses import dataclass, field

from src.domain.common import Aggregate
from src.domain.post.value_objects import (
    PostId,
    CreatorId
)


@dataclass
class PostAggregate(Aggregate):
    post_id: PostId
    creator_id: CreatorId
    text_content: str
    created_at: datetime = field(default=datetime.now())

    @classmethod
    def create_post(
            cls,
            *,
            post_id: PostId,
            creator_id: CreatorId,
            text_content: str
    ) -> 'PostAggregate':
        """
        Создание поста
        """
        return PostAggregate(
            post_id=post_id,
            creator_id=creator_id,
            text_content=text_content
        )

    def update_post(self, text_content: str) -> None:
        """
        Обновление поста
        """
        self.text_content = text_content
