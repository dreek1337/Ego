from src.domain import PostId
from src.application.posts.uow import PostUoW
from src.application.posts.dto import DeletePostDTO
from src.application.common import (
    UseCase,
    UseCaseData
)


class DeletePostData(UseCaseData):
    """
    Данные для удаления поста
    """
    post_id: str

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
        await self._uow.post_repo.delete_post(
            post_id=PostId(value=data.post_id)
        )

        delete_post_dto = DeletePostDTO(post_id=data.post_id)

        return delete_post_dto
