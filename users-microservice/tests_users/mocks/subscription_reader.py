from src_users.application import (
    GetSubscriptionsFilters,
    GetSubscriptionsOrder,
    SubscriptionDTO,
    SubscriptionReader,
)
from src_users.domain.common import Empty


class SubscriptionReaderMock(SubscriptionReader):
    """
    Ридер для работы с бд
    """

    def __init__(self) -> None:
        self.users: dict[int, SubscriptionDTO] = dict()
        self.subscriptions: dict[int, list[SubscriptionDTO]] = dict()
        # В list[SubscriptionDTO] лежат все подписчики пользователя

    async def get_subscriptions_by_id(
        self, *, subscriber_id: int, filters: GetSubscriptionsFilters
    ) -> list[SubscriptionDTO] | None:
        """
        Получения списка всех подписок пользователя
        """
        subscriptions_list = list()

        for subscription_id, subscription_list in self.subscriptions.items():
            for subscriber in subscription_list:
                if subscriber.user_id == subscriber_id:
                    subscriptions_list.append(self.users[subscription_id])

        subscribers = subscriptions_list if subscriptions_list else None

        if subscribers:
            subscribers = self._add_filters(filters=filters, subscription=subscribers)

        return subscribers

    async def get_subscribers_by_id(
        self, *, subscription_id: int, filters: GetSubscriptionsFilters
    ) -> list[SubscriptionDTO] | None:
        """
        Получение списка всех подписчиков пользователя
        """
        subscribers = self.subscriptions.get(subscription_id)

        if subscribers:
            subscribers = self._add_filters(filters=filters, subscription=subscribers)

        return subscribers

    async def get_count_subscriptions(self, subscriber_id: int) -> int:
        """
        Получить кол-во подписок пользователя
        """
        subscriptions_list = list()

        for subscription_id, subscription_list in self.subscriptions.items():
            for subscriber in subscription_list:
                if subscriber.user_id == subscriber_id:
                    subscriptions_list.append(self.users[subscription_id])

        return len(subscriptions_list) if subscriptions_list else 0

    async def get_count_subscribers(self, subscription_id: int) -> int:
        """
        Получить кол-во подписчиков пользователя
        """
        subscriptions = self.subscriptions.get(subscription_id)

        return len(subscriptions) if subscriptions else 0

    @staticmethod
    def _add_filters(
        subscription: list[SubscriptionDTO], filters: GetSubscriptionsFilters
    ) -> list[SubscriptionDTO] | None:
        """
        Добавление фильтров
        """
        if filters.order == GetSubscriptionsOrder.ASC:
            subscription.sort(key=lambda sup: sup.user_id)
        else:
            subscription.sort(key=lambda sup: sup.user_id, reverse=True)

        limit = filters.limit if filters.limit is not Empty.UNSET else 0
        offset = (
            filters.offset if filters.offset is not Empty.UNSET else len(subscription)
        )
        last_index = limit + offset

        subscriptions = subscription[offset:last_index]

        result = subscriptions if subscriptions else None

        return result

    def add_subscriptions(
        self, user_id: int, subscriptions: list[SubscriptionDTO]
    ) -> None:
        """
        Добавление подписок для тестов
        """
        self.subscriptions[user_id] = subscriptions

    def _add_user(self, user: SubscriptionDTO) -> None:
        """
        Добавление пользовтаеля для тестов
        """
        self.users[user.user_id] = user

    def add_users(self, users: list[SubscriptionDTO]) -> None:
        """
        Добавление пользовтаелей для тестов
        """
        for user in users:
            self._add_user(user=user)
