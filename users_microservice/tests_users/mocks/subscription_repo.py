from src_users.application import (
    SubscribeIsNotExists,
    SubscribeOnYourself,
    SubscriptionRepo,
    UserIsNotExist,
)
from src_users.domain.user import SubscriptionEntity
from src_users.domain.user.value_objects import (
    SubscriberId,
    SubscriptionId,
)


class SubscriptionRepoMock(SubscriptionRepo):
    """
    Репозиторий подпичок
    """

    def __init__(self) -> None:
        self.users: list[int] = list()
        self.subscriptions: dict[SubscriptionId, SubscriptionEntity] = dict()

    async def get_subscription_by_id(
        self, *, subscription_id: SubscriptionId, subscriber_id: SubscriberId
    ) -> SubscriptionEntity:
        """
        Получение подписки
        """
        for subscription in self.subscriptions.values():
            sup_id_correct = subscription.subscription_user_id == subscription_id
            sub_id_correct = subscription.subscriber_user_id == subscriber_id
            if sup_id_correct and sub_id_correct:
                return subscription
        raise SubscribeIsNotExists()

    async def subscribe(self, subscription: SubscriptionEntity) -> None:
        """
        Подписаться на пользователя
        """
        sup_id_correct = subscription.subscription_user_id
        sub_id_correct = subscription.subscriber_user_id
        if sup_id_correct.to_int not in self.users:
            raise UserIsNotExist(user_id=sup_id_correct.to_int)
        if sub_id_correct.to_int not in self.users:
            raise UserIsNotExist(user_id=sub_id_correct.to_int)
        if sup_id_correct == sub_id_correct:
            raise SubscribeOnYourself()

        self.subscriptions[subscription.subscription_user_id] = subscription

    async def unsubscribe(self, subscription: SubscriptionEntity) -> None:
        """
        Отписаться от пользователя
        """
        del self.subscriptions[subscription.subscription_user_id]

    def add_users(self, users_id: list[int]) -> None:
        self.users.extend(users_id)
