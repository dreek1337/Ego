from src_posts.application.common import (
    UseCase,
    UseCaseData,
)
from src_posts.application.posts.dto import DeletePostDTO
from src_posts.application.posts.exceptions import UserIsNotPostCreator
from src_posts.application.posts.uow import PostUoW
from src_posts.domain import PostId


class DeletePostData(UseCaseData):
    """
    Данные для удаления поста
    """

    post_id: str
    creator_id: int

    class Config:
        frozen = True


class DeletePostUseCase(UseCase):
    """
    UseCase для удаления поста
    """

    def __init__(
        self,
        *,
        uow: PostUoW,
    ) -> None:
        self._uow = uow

    async def __call__(self, data: DeletePostData) -> DeletePostDTO:
        post = await self._uow.post_repo.get_post_by_id(
            post_id=PostId(value=data.post_id)
        )

        if post.creator_id.get_value != data.creator_id:
            raise UserIsNotPostCreator()

        await self._uow.post_repo.delete_post(post_id=PostId(value=data.post_id))

        delete_post_dto = DeletePostDTO(post_id=data.post_id)

        return delete_post_dto
