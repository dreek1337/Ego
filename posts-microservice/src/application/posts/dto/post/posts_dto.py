from src.domain.common import Empty
from src.application.common import DTO
from src.application.posts.dto.post.post_dto import PostDTO


class PostsDTO(DTO):
    """
    Модель подписок
    """
    posts: list[PostDTO]
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET

    class Config:
        frozen = True
        arbitrary_types_allowed = True
