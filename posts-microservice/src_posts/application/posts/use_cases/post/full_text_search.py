from src_posts.application.common import UseCase, UseCaseData
from src_posts.application.posts.dto import PostsDTO
from src_posts.application.posts.interfaces import GetPostsFilters, GetPostsOrder
from src_posts.application.posts.uow import PostUoW
from src_posts.domain import Empty


class FullTextSearchPostsData(UseCaseData):
    """
    Данные для получения постов по ключевым словам
    """

    query_string: str
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetPostsOrder = GetPostsOrder.ASC

    class Config:
        frozen = True


class FullTextSearchPostsUseCase(UseCase):
    """
    UseCase для получения постов по ключевым словам
    """

    def __init__(
        self,
        *,
        uow: PostUoW,
    ) -> None:
        self._uow = uow

    async def __call__(self, data: FullTextSearchPostsData) -> PostsDTO:
        posts_data = await self._uow.post_reader.full_text_posts_search(
            query_string=data.query_string,
            filters=GetPostsFilters(
                offset=data.offset, limit=data.limit, order=data.order
            ),
        )

        return PostsDTO(posts=posts_data, offset=data.offset, limit=data.limit)
