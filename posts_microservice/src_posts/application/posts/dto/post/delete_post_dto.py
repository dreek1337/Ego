from pydantic import Field
from src_posts.application.common import DTO


class DeletePostDTO(DTO):
    post_id: str = Field(..., description="Айди поста")
