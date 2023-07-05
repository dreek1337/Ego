import datetime

import pytest  # type: ignore
from src.application import CreatePostData, PostService
from src.application.posts import dto
from src.infrastructure import MapperImpl
from tests.mocks import PostUoWMock


@pytest.mark.asyncio
async def test_create_post(
        uow: PostUoWMock,
        mapper: MapperImpl
) -> None:
    post_service = PostService(uow=uow, mapper=mapper)

    post_data = CreatePostData(
        creator_id=0,
        text_content='My test post!'
    )

    created_post = await post_service.create_post(data=post_data)

    assert created_post == dto.PostDTO(
        post_id="gl5MJXMBMk1dGnErnBW8",
        creator_id=0,
        text_content="My test post!",
        created_at=datetime.datetime(
            year=2023,
            month=6,
            day=25,
            hour=11,
            minute=15
        )
    )
