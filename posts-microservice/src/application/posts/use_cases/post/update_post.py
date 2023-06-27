from src.domain import PostId
from src.application.posts.dto import PostDTO
from src.application.posts.uow import PostUoW
from src.application.common import (
    Mapper,
    UseCase,
    UseCaseData
)


class UpdatePostData(UseCaseData):
    """
    Данные для изменение поста
    """
    post_id: str
    text_content: str

    class Config:
        frozen = True


class UpdatePostUseCase(UseCase):
    """
    UseCase для изменение поста
    """
    def __init__(
            self,
            *,
            uow: PostUoW,
            mapper: Mapper
    ) -> None:
        self._uow = uow
        self._mapper = mapper

    async def __call__(self, data: UpdatePostData) -> PostDTO:
        post = await self._uow.post_repo.get_post_by_id(
            post_id=PostId(value=data.post_id)
        )

        post.update_post(text_content=data.text_content)

        updated_post = await self._uow.post_repo.update_post(post=post)

        post_dto = self._mapper.load(from_model=updated_post, to_model=PostDTO)

        return post_dto
