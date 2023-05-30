from sqlalchemy import Result

from src.domain import SubscriptionEntity
from src.application.user.dto import (
    SubscriptionDTO,
    SubscribeActionDTO
)
from src.infrastructure.database.models import Subscriptions


def convert_subscription_entity_to_dto(
        subscription: SubscriptionEntity
) -> SubscribeActionDTO:
    """
    Преобразование из Энтити в ДТО
    """
    subscribe_action = SubscribeActionDTO(
        subscription_id=subscription.subscription_user_id.to_int,
        subscriber_id=subscription.subscriber_user_id.to_int
    )

    return subscribe_action


def convert_subscriptions_db_model_to_subscription_dto(
        subscriptions: Result
) -> list[SubscriptionDTO]:
    """
    Преобразования ORM моделей в ДТО
    """
    subscription_dto = [
        SubscriptionDTO(
            subscription_id=subscription.subscriber_id,
            first_name=subscription.first_name,
            last_name=subscription.first_name,
            avatar=subscription.avatar_content if subscription.avatar_content else None
        )
        for subscription in subscriptions
    ]

    return subscription_dto


def convert_subscription_db_model_to_subscription_entity(
        subscription: Subscriptions
) -> SubscriptionEntity:
    """
    Преобразования ORM модели в Энтити
    """
    subscription_entity = SubscriptionEntity(
        subscription_user_id=subscription.subscription_id,
        subscriber_user_id=subscription.subscriber_id
    )

    return subscription_entity
