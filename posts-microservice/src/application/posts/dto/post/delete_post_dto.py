from uuid import UUID

from pydantic import Field

from src.application.common import DTO


class DeletePostDTO(DTO):
    post_id: UUID = Field(..., description='Айди поста')
