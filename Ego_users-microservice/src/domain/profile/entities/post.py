from typing import Self
from datetime import datetime
from dataclasses import dataclass


@dataclass
class Post:
    """
    Модель поста
    """
    post_text: str
    date_of_create: datetime
    like: int

    @classmethod
    def create_post(
            cls,
            *,
            post_text: str,
            date_of_create: datetime,
            like: int
    ) -> Self:
        """
        Создание поста
        """
        post = Post(
            post_text=post_text,
            date_of_create=date_of_create,
            like=like
        )

        return post
