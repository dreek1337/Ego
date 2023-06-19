from src.domain.common import Empty
from src.application.common import DTO
from src.application.user.dto.subscription.subscriptiondto import SubscriptionDTO


class SubscriptionsDTO(DTO):
    """
    Модель подписок
    """
    subscriptions: list[SubscriptionDTO]
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET

    class Config:
        frozen = True
        arbitrary_types_allowed = True
