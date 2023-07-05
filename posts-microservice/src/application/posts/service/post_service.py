from src.application.common import Mapper, Service
from src.application.posts import dto
from src.application.posts import use_cases as uc
from src.application.posts.uow import PostUoW


class PostService(Service):
    """
    Сервис который отвечает за работу с Постами
    """
    def __init__(
            self,
            *,
            uow: PostUoW,
            mapper: Mapper,
    ) -> None:
        self._uow = uow
        self._mapper = mapper

    async def get_user_posts(
            self,
            data: uc.GetPostsData
    ) -> dto.PostsDTO:
        """
        Получение постов пользователя
        """
        return await uc.GetPostsUseCase(
            uow=self._uow
        )(data=data)

    async def full_text_posts_search(
            self,
            data: uc.FullTextSearchPostsData
    ) -> dto.PostsDTO:
        """
        Получение постов по ключевым словам
        """
        return await uc.FullTextSearchPostsUseCase(
            uow=self._uow
        )(data=data)

    async def create_post(
            self,
            data: uc.CreatePostData
    ) -> dto.PostDTO:
        """
        Создание поста
        """
        return await uc.CreatePostUseCase(
            uow=self._uow, mapper=self._mapper
        )(data=data)

    async def update_post(
            self,
            data: uc.UpdatePostData
    ) -> dto.PostDTO:
        """
        Обновление поста
        """
        return await uc.UpdatePostUseCase(
            uow=self._uow, mapper=self._mapper
        )(data=data)

    async def delete_post(
            self,
            data: uc.DeletePostData
    ) -> dto.DeletePostDTO:
        """
        Создание поста
        """
        return await uc.DeletePostUseCase(
            uow=self._uow
        )(data=data)
