from datetime import datetime

from pydantic import Field

from src.application.common import DTO


class Post(DTO):
    """
    Модель поста
    """
    post_text: str = Field(..., description='Текст поста')
    date_of_create: datetime = Field(..., description='Дата создания поста')
    like: int = Field(..., description='Колличество лайков поста')

    class Config:
        frozen = True
