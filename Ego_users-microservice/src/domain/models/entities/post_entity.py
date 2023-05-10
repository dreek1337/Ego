from dataclasses import dataclass

from src.domain.models.value_objects import (
    PostId,
    PostText,
    PostLike,
    DateOfCreate
)


@dataclass
class Post:
    """
    Модель поста
    """
    post_id: PostId
    post_text: PostText
    date_of_create: DateOfCreate
    like: PostLike
