from typing import Any

from src.application.posts.dto import PostDTO
from src.domain import (
    PostId,
    PostAggregate
)


def convert_from_entity_to_dto(
        post: PostAggregate
) -> PostDTO:
    """
    Конвертация из энтити в дто
    """
    post_dto = PostDTO(
        post_id=post.post_id.get_value,  # type: ignore
        creator_id=post.creator_id.get_value,
        text_content=post.text_content,
        created_at=post.created_at
    )

    return post_dto


def convert_from_elastic_model_to_entity(
        elastic_data: dict[str, Any]
) -> PostAggregate:
    """
    Конвертация из модели эластика в энтити
    """
    post_aggregate = PostAggregate(
        post_id=PostId(value=elastic_data.get('_id')),  # type: ignore
        creator_id=elastic_data.get('creator_id'),  # type: ignore
        text_content=elastic_data.get('text_content'),  # type: ignore
        created_at=elastic_data.get('created_at')  # type: ignore
    )

    return post_aggregate


def convert_from_elastic_models_to_dto(
        elastic_posts: list[dict[str, Any]]
) -> list[PostDTO]:
    """
    Конвертация из моделей эластика в дто
    """
    posts_dto = [
        PostDTO(
            post_id=post.get('_id'),    # type: ignore
            creator_id=post.get('creator_id'),    # type: ignore
            text_content=post.get('text_content'),    # type: ignore
            created_at=post.get('created_at')    # type: ignore
        )
        for post in elastic_posts
    ]

    return posts_dto
