import datetime

import pytest  # type: ignore
from elasticsearch import NotFoundError  # type: ignore
from src_posts.application import DeletePostData, PostService, UserIsNotPostCreator
from src_posts.application.posts import dto
from src_posts.domain import CreatorId, PostAggregate, PostId
from src_posts.infrastructure import MapperImpl
from tests_posts.mocks import PostUoWMock


@pytest.mark.asyncio
async def test_correct_delete_post(uow: PostUoWMock, mapper: MapperImpl) -> None:
    post_service = PostService(uow=uow, mapper=mapper)

    post_id = PostId(value="gl5MJXMBMk1dGnErnBW8")
    post = PostAggregate(
        post_id=post_id,
        creator_id=CreatorId(value=0),
        text_content="My test post!",
        created_at=datetime.datetime(year=2023, month=6, day=25, hour=11, minute=15),
    )

    uow.post_repo.add_post(post=post)  # type: ignore

    data = DeletePostData(post_id="gl5MJXMBMk1dGnErnBW8", creator_id=0)

    deleted_post_data = await post_service.delete_post(data=data)

    assert deleted_post_data == dto.DeletePostDTO(post_id="gl5MJXMBMk1dGnErnBW8")


@pytest.mark.asyncio
async def test_deleted_post_not_found(uow: PostUoWMock, mapper: MapperImpl) -> None:
    post_service = PostService(uow=uow, mapper=mapper)

    data = DeletePostData(post_id="gl5MJXMBMk1dGnErnBW81", creator_id=0)

    with pytest.raises(NotFoundError):
        await post_service.delete_post(data=data)


@pytest.mark.asyncio
async def test_user_is_not_post_creator_to_delete(
    uow: PostUoWMock, mapper: MapperImpl
) -> None:
    post_service = PostService(uow=uow, mapper=mapper)

    post_id = PostId(value="gl5MJXMBMk1dGnErnBW8")
    post = PostAggregate(
        post_id=post_id,
        creator_id=CreatorId(value=0),
        text_content="My test post!",
        created_at=datetime.datetime(year=2023, month=6, day=25, hour=11, minute=15),
    )

    uow.post_repo.add_post(post=post)  # type: ignore

    data = DeletePostData(post_id="gl5MJXMBMk1dGnErnBW8", creator_id=1)

    with pytest.raises(UserIsNotPostCreator):
        await post_service.delete_post(data=data)
