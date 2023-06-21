from abc import (
    ABC,
    abstractmethod
)


from enum import Enum

from pydantic import BaseModel

from src.domain.common.constants import Empty
from src.application.posts.dto import PostsDTO


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
            subscription_id: int,
            filters: GetPostsFilters
    ) -> list[PostsDTO]:
        """Получения списка всех подписчиков пользователя"""

    @abstractmethod
    async def get_count_posts(self, subscriber_id: int) -> int:
        """Получить кол-во подписок пользователя"""
