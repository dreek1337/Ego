from abc import (
    ABC,
    abstractmethod
)


from enum import Enum

from pydantic import BaseModel

from src.domain.common.constants import Empty
from src.application.user.dto import SubscriptionDTO


class GetSubscriptionsOrder(str, Enum):
    ASC = "asc"
    DESC = "desc"


class GetSubscriptionsFilters(BaseModel):
    offset: int | Empty = Empty.UNSET
    limit: int | Empty = Empty.UNSET
    order: GetSubscriptionsOrder = GetSubscriptionsOrder.ASC


class SubscriptionReader(ABC):
    """
    Ридер для работы с бд
    """
    @abstractmethod
    async def get_subscriptions_by_id(
            self,
            *,
            subscriber_id: int,
            filters: GetSubscriptionsFilters
    ) -> list[SubscriptionDTO]:
        """Получение списка всех подписок пользователя"""

    @abstractmethod
    async def get_subscribers_by_id(
            self,
            *,
            subscription_id: int,
            filters: GetSubscriptionsFilters
    ) -> list[SubscriptionDTO]:
        """Получения списка всех подписчиков пользователя"""

    @abstractmethod
    async def get_count_subscriptions(self, subscriber_id: int) -> int:
        """Получить кол-во подписок пользователя"""

    @abstractmethod
    async def get_count_subscribers(self, subscription_id: int) -> int:
        """Получить кол-во подписчиков пользователя"""
