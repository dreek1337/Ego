from src.domain import Empty
from src.application.posts.dto import PostDTO
from src.application.posts.uow import PostUoW
from src.application.posts.interfaces import (
    GetPostsOrder,
    GetPostsFilters
)
from src.application.common import (
    Mapper,
    UseCase,
    UseCaseData
)


class FullTextSearchPostsData(UseCaseData):
    """
    Данные для получения постов
    """
    query_string: str
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetPostsOrder = GetPostsOrder.ASC

    class Config:
        frozen = True


class FullTextSearchPostsUseCase(UseCase):
    """
    UseCase для создания поста
    """
    def __init__(
            self,
            *,
            uow: PostUoW,
            mapper: Mapper
    ) -> None:
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, data: FullTextSearchPostsData) -> list[PostDTO]:
        posts_data = await self._uow.post_reader.full_text_posts_search(
            query_string=data.query_string,
            filters=GetPostsFilters(
                offset=data.offset,
                limit=data.limit,
                order=data.order
            )
        )

        post_dto = self._mapper.load(from_model=posts_data, to_model=list[PostDTO])

        return post_dto
