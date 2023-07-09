from src_posts.application.common import (
    Mapper,
    UseCase,
    UseCaseData,
)
from src_posts.application.posts.dto import PostDTO
from src_posts.application.posts.exceptions import UserIsNotPostCreator
from src_posts.application.posts.uow import PostUoW
from src_posts.domain import PostId


class UpdatePostData(UseCaseData):
    """
    Данные для изменение поста
    """

    post_id: str
    creator_id: int
    text_content: str

    class Config:
        frozen = True


class UpdatePostUseCase(UseCase):
    """
    UseCase для изменение поста
    """

    def __init__(self, *, uow: PostUoW, mapper: Mapper) -> None:
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, data: UpdatePostData) -> PostDTO:
        post = await self._uow.post_repo.get_post_by_id(
            post_id=PostId(value=data.post_id)
        )

        if post.creator_id.get_value != data.creator_id:
            raise UserIsNotPostCreator()

        post.update_post(text_content=data.text_content)

        await self._uow.post_repo.update_post(post=post)

        post_dto = self._mapper.load(from_model=post, to_model=PostDTO)

        return post_dto
