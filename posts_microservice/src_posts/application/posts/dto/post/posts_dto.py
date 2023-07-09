from src_posts.application.common import DTO
from src_posts.application.posts.dto.post.post_dto import PostDTO
from src_posts.domain.common import Empty


class PostsDTO(DTO):
    """
    Модель подписок
    """

    posts: list[PostDTO] | None
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET

    class Config:
        frozen = True
        arbitrary_types_allowed = True
