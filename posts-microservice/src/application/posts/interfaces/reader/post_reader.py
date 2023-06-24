from abc import (
    ABC,
    abstractmethod
)


from enum import Enum

from pydantic import BaseModel

from src.domain.common.constants import Empty
from src.application.posts.dto import PostDTO


class GetPostsOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"


class GetPostsFilters(BaseModel):
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetPostsOrder = GetPostsOrder.ASC


class PostReader(ABC):
    """
    Ридер для работы с бд
    """
    @abstractmethod
    async def get_posts_by_creator_id(
            self,
            *,
            creator_id: int,
            filters: GetPostsFilters
    ) -> list[PostDTO] | None:
        """Получения списка всех постов пользователя"""

    @abstractmethod
    async def full_text_posts_search(
            self,
            query_string: str,
            filters: GetPostsFilters
    ) -> list[PostDTO]:
        """Полнотекстовый поиск постов"""
