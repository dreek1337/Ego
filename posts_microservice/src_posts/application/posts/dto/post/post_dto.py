from datetime import datetime

from pydantic import Field
from src_posts.application.common import DTO


class PostDTO(DTO):
    post_id: str = Field(..., description="Айди поста")
    creator_id: int = Field(..., description="Айди создателя поста")
    text_content: str = Field(..., description="Текст поста")
    created_at: datetime = Field(..., description="Время создания поста")
