from src.application.common import Mapper, UseCase, UseCaseData
from src.application.posts.dto import PostDTO
from src.application.posts.uow import PostUoW
from src.domain import CreatorId, PostAggregate


class CreatePostData(UseCaseData):
    """
    Данные для создания поста
    """
    creator_id: int
    text_content: str

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

    async def __call__(self, data: CreatePostData) -> PostDTO:
        post_data = PostAggregate.create_post(
            creator_id=CreatorId(value=data.creator_id),
            text_content=data.text_content
        )

        post = await self._uow.post_repo.create_post(data=post_data)

        post_dto = self._mapper.load(from_model=post, to_model=PostDTO)

        return post_dto
