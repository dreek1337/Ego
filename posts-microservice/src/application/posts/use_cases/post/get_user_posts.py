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


class CreatePostUseCase(UseCase):
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

    async def __call__(self, data: GetPostsData) -> list[PostDTO]:
        posts_data = await self._uow.post_reader.get_posts_by_creator_id(
            creator_id=data.creator_id,
            filters=GetPostsFilters(
                offset=data.offset,
                limit=data.limit,
                order=data.order
            )
        )

        post_dto = self._mapper.load(from_model=posts_data, to_model=list[PostDTO])

        return post_dto
