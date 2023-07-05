from typing import Any

from sqlalchemy import ChunkedIteratorResult
from src.application.user.constant import AvatarCloudEnum
from src.application.user.dto import SubscribeActionDTO, SubscriptionDTO
from src.domain import SubscriptionEntity
from src.domain.user import value_objects as vo
from src.infrastructure.database.models.subscriptions_model import Subscriptions


def convert_subscription_entity_to_dto(
    subscription: SubscriptionEntity,
) -> SubscribeActionDTO:
    """
    Преобразование из Энтити в ДТО
    """
    subscribe_action = SubscribeActionDTO(
        subscription_id=subscription.subscription_user_id.to_int,
        subscriber_id=subscription.subscriber_user_id.to_int,
    )

    return subscribe_action


def convert_subscriptions_db_model_to_subscription_dto(
    subscriptions: ChunkedIteratorResult[tuple[Any, Subscriptions]]
) -> list[SubscriptionDTO]:
    """
    Преобразование ORM моделей в ДТО
    """
    subscription_dto = [
        SubscriptionDTO(
            user_id=subscription[0],
            first_name=subscription[1],
            last_name=subscription[2],
            avatar=f"{AvatarCloudEnum.FOLDER.value}/{subscription[0]}.{subscription[3]}"
            if subscription[3]
            else None,
            deleted=subscription[4],
        )
        for subscription in subscriptions
    ]

    return subscription_dto


def convert_subscription_db_model_to_subscription_entity(
    subscription: Subscriptions,
) -> SubscriptionEntity:
    """
    Преобразование ORM модели в Энтити
    """
    subscription_entity = SubscriptionEntity(
        subscription_user_id=vo.SubscriptionId(value=subscription.subscription_id),
        subscriber_user_id=vo.SubscriberId(value=subscription.subscriber_id),
    )

    return subscription_entity


def convert_subscription_entity_to_db_model(
    subscription: SubscriptionEntity,
) -> Subscriptions:
    """
    Преобразование энтити модель орм
    """
    subscription_orm_model = Subscriptions(
        subscription_id=subscription.subscription_user_id.to_int,
        subscriber_id=subscription.subscriber_user_id.to_int,
    )

    return subscription_orm_model
