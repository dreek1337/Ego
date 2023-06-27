from pydantic import Field

from src.application.common import DTO


class DeletePostDTO(DTO):
    post_id: str = Field(..., description='Айди поста')
