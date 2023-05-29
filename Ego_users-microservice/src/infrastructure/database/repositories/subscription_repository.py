from sqlalchemy.exc import IntegrityError
from sqlalchemy import (
    func,
    delete,
    select
)

from src.application.user import dto
from src.domain import SubscriptionEntity
from src.infrastructure.utils import add_filters
from src.infrastructure.database.repositories.base import SQLAlchemyRepo
from src.domain.user.value_objects import (
    SubscriberId,
    SubscriptionId,
)
from src.infrastructure.database.models import (
    Users,
    Avatars,
    Subscriptions
)
from src.application import (
    SubscriptionRepo,
    SubscriptionReader,
    GetSubscriptionsFilters
)


class SubscriptionReaderImpl(SQLAlchemyRepo, SubscriptionReader):
    """
    Реализация ридера для подписок
    """
    async def get_subscriptions_by_id(
            self,
            *,
            subscriber_id: int,
            filters: GetSubscriptionsFilters
    ) -> list[dto.SubscriptionDTO]:
        """
        Получение списка всех подписок пользователя
        """
        cte_query = (
            select(Subscriptions.subscription_id).label('subscription_id')
            .where(Subscriptions.subscriber_id == subscriber_id)
        )
        cte_query = add_filters(
            query=cte_query,
            filters=filters,
            column_for_order=cte_query.subscription_id
        ).cte()

        query = (
            select(
                cte_query.subscription_id,
                Users.first_name,
                Users.last_name,
                Avatars.avatar_content
            )
            .join(Users)
            .join(Users.avatar, isouter=True)
        )

        subscriptions = await self._session.execute(query)

        subscriptions_dto = self._mapper.load(
            from_model=subscriptions,
            to_model=list[dto.SubscriptionDTO]
        )

        return subscriptions_dto

    async def get_subscribers_by_id(
            self,
            *,
            subscription_id: int,
            filters: GetSubscriptionsFilters
    ) -> list[dto.SubscriptionDTO]:
        """
        Получения списка всех подписчиков пользователя
        """
        cte_query = (
            select(Subscriptions.subscriber_id).label('subscriber_id')
            .where(Subscriptions.subscription_id == subscription_id)
        )
        cte_query = add_filters(
            query=cte_query,
            filters=filters,
            column_for_order=cte_query.subscriber_id
        ).cte()

        query = (
            select(
                cte_query.subscriber_id,
                Users.first_name,
                Users.last_name,
                Avatars.avatar_content
            )
            .join(Users)
            .join(Users.avatar, isouter=True)
        )

        subscribers = await self._session.execute(query)

        subscriptions_dto = self._mapper.load(
            from_model=subscribers,
            to_model=list[dto.SubscriptionDTO]
        )

        return subscriptions_dto

    async def get_count_subscriptions(self, subscriber_id: int) -> int:
        """
        Получить кол-во подписок пользователя
        """
        query = (
            select(func.count(Subscriptions.subscription_id))
            .where(Subscriptions.subscriber_id == subscriber_id)
        )

        count_of_subscriptions = await self._session.scalar(query)

        return count_of_subscriptions or 0

    async def get_count_subscribers(self, subscription_id: int) -> int:
        """
        Получить кол-во подписчиков пользователя
        """
        query = (
            select(func.count(Subscriptions.subscriber_id))
            .where(Subscriptions.subscription_id == subscription_id)
        )

        count_of_subscribers = await self._session.scalar(query)

        return count_of_subscribers or 0


class SubscriptionRepoImpl(SQLAlchemyRepo, SubscriptionRepo):
    """
    Реализация репозитория для подписок
    """
    async def get_subscription_by_id(
            self,
            *,
            subscription_id: SubscriptionId,
            subscriber_id: SubscriberId
    ) -> SubscriptionEntity:
        """
        Получение подписки
        """
        query = (
            select(Subscriptions)
            .where(
                Subscriptions.subscription_id == subscription_id.to_int,
                Subscriptions.subscriber_id == subscriber_id.to_int
            )
        )

        subscription = await self._session.execute(query)

        if not subscription:
            # raise SubscriptionIsNotExist(subscription_id.to_int, subscriber_id.to_int)
            pass

        result = subscription.all()

        subscription_entity = self._mapper.load(
            from_model=result,
            to_model=SubscriptionEntity
        )

        return subscription_entity

    async def subscribe(self, subscription: SubscriptionEntity) -> None:
        """
        Подписаться на пользователя
        """
        subscription_model = self._mapper.load(
            from_model=subscription,
            to_model=Subscriptions
        )

        self._session.add(subscription_model)

        try:
            await self._session.flush((subscription_model,))
        except IntegrityError:
            pass  # Добавить обрабокту ошибок

    async def unsubscribe(self, subscription: SubscriptionEntity) -> None:
        """
        Отписаться от пользователя
        """
        query = (
            delete(Subscriptions)
            .where(
                Subscriptions.subscription_id == (
                    subscription
                    .subscription_user_id
                    .to_int
                ),
                Subscriptions.subscriber_id == (
                    subscription
                    .subscriber_user_id
                    .to_int
                )
            )
        )

        await self._session.execute(query)
