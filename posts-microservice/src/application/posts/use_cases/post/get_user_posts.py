from src.application.common import UseCase, UseCaseData
from src.application.posts.dto import PostsDTO
from src.application.posts.interfaces import GetPostsFilters, GetPostsOrder
from src.application.posts.uow import PostUoW
from src.domain import Empty


class GetPostsData(UseCaseData):
    """
    Данные для получения постов
    """
    creator_id: int
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetPostsOrder = GetPostsOrder.ASC

    class Config:
        frozen = True


class GetPostsUseCase(UseCase):
    """
    UseCase для создания поста
    """
    def __init__(
            self,
            *,
            uow: PostUoW,
    ) -> None:
        self._uow = uow

    async def __call__(self, data: GetPostsData) -> PostsDTO:
        posts_data = await self._uow.post_reader.get_posts_by_creator_id(
            creator_id=data.creator_id,
            filters=GetPostsFilters(
                offset=data.offset,
                limit=data.limit,
                order=data.order
            )
        )

        return PostsDTO(
            posts=posts_data,
            offset=data.offset,
            limit=data.limit
        )
