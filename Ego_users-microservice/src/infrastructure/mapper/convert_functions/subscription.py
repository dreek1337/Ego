from sqlalchemy import Result

from src.domain import SubscriptionEntity
from src.domain.user import value_objects as vo
from src.application.user.constant import AvatarCloudEnum
from src.infrastructure.database.models.subscriptions_model import Subscriptions
from src.application.user.dto import (
    SubscriptionDTO,
    SubscribeActionDTO
)


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
    Преобразование ORM моделей в ДТО
    """
    print()
    subscription_dto = [
        SubscriptionDTO(
            subscription_id=subscription.subscriber_id,
            first_name=subscription.first_name,
            last_name=subscription.first_name,
            avatar=f'{AvatarCloudEnum.FOLDER.value}/{subscription.avatar_user_id}.{subscription.avatar_type}'
            if subscription.avatar_user_id and subscription.avatar_type
            else None
        )
        for subscription in subscriptions
    ]

    return subscription_dto


def convert_subscription_db_model_to_subscription_entity(
        subscription: Subscriptions
) -> SubscriptionEntity:
    """
    Преобразование ORM модели в Энтити
    """
    subscription_entity = SubscriptionEntity(
        subscription_user_id=vo.SubscriptionId(value=subscription.subscription_id),
        subscriber_user_id=vo.SubscriberId(value=subscription.subscriber_id)
    )

    return subscription_entity


def convert_subscription_entity_to_db_model(
        subscription: SubscriptionEntity
) -> Subscriptions:
    """
    Преобразование энтити модель орм
    """
    subscription_orm_model = Subscriptions(
        subscription_id=subscription.subscription_user_id.to_int,
        subscriber_id=subscription.subscriber_user_id.to_int
    )

    return subscription_orm_model
