from typing import Any

from asyncpg import UniqueViolationError, ForeignKeyViolationError  # type: ignore
from sqlalchemy.exc import IntegrityError, DBAPIError
from sqlalchemy import (
    func,
    delete,
    select
)

from src import application as app
from src.application.user import dto
from src.domain.common import Empty
from src.domain import SubscriptionEntity
from src.infrastructure.database.repositories.base import SQLAlchemyRepo
from src.infrastructure.database.error_interceptor import error_interceptor
from src.domain.user.value_objects import (
    SubscriberId,
    SubscriptionId,
)
from src.infrastructure.database.models import (
    Users,
    Avatars,
    Subscriptions
)


class SubscriptionReaderImpl(SQLAlchemyRepo, app.SubscriptionReader):
    """
    Реализация ридера для подписок
    """
    @error_interceptor(file_name=__name__)
    async def get_subscriptions_by_id(
            self,
            *,
            subscriber_id: int,
            filters: app.GetSubscriptionsFilters
    ) -> list[dto.SubscriptionDTO]:
        """
        Получение списка всех подписок пользователя
        """
        cte_query = (
            select(Subscriptions.subscription_id)
            .where(Subscriptions.subscriber_id == subscriber_id)
            .order_by(
                Subscriptions.subscription_id.desc()
                if filters.order == app.GetSubscriptionsOrder.DESC
                else Subscriptions.subscription_id.asc()
            )
        ).cte()

        subscriptions_dto = await self._create_subscription_request(
            cte_query=cte_query,
            filters=filters
        )

        return subscriptions_dto

    @error_interceptor(file_name=__name__)
    async def get_subscribers_by_id(
            self,
            *,
            subscription_id: int,
            filters: app.GetSubscriptionsFilters
    ) -> list[dto.SubscriptionDTO]:
        """
        Получения списка всех подписчиков пользователя
        """
        cte_query = (
            select(Subscriptions.subscriber_id)
            .where(Subscriptions.subscription_id == subscription_id)
            .order_by(
                Subscriptions.subscription_id.desc()
                if filters.order == app.GetSubscriptionsOrder.DESC
                else Subscriptions.subscription_id.asc()
            )
        ).cte()

        subscriptions_dto = await self._create_subscription_request(
            cte_query=cte_query,
            filters=filters
        )

        return subscriptions_dto

    @error_interceptor(file_name=__name__)
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

    @error_interceptor(file_name=__name__)
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

    @error_interceptor(file_name=__name__)
    async def _create_subscription_request(
            self,
            *,
            cte_query: Any,
            filters: app.GetSubscriptionsFilters
    ):
        """
        Основной запрос для подтягивания подписчиков и подписок
        """
        query = (
            select(
                cte_query,
                Users.first_name,
                Users.last_name,
                Avatars.avatar_type,
                Users.deleted
            )
            .select_from(cte_query)
            .join(Users)
            .join(Users.avatar, isouter=True)
        )

        if filters.limit is not Empty.UNSET:
            query = query.limit(filters.limit)
        if filters.offset is not Empty.UNSET:
            query = query.offset(filters.offset)

        subscriptions = await self._session.execute(query)

        return self._mapper.load(
            from_model=subscriptions,
            to_model=list[dto.SubscriptionDTO]
        )


class SubscriptionRepoImpl(SQLAlchemyRepo, app.SubscriptionRepo):
    """
    Реализация репозитория для подписок
    """
    @error_interceptor(file_name=__name__)
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

        result = subscription.scalar()

        if not result:
            raise app.SubscribeIsNotExists()

        subscription_entity = self._mapper.load(
            from_model=result,
            to_model=SubscriptionEntity
        )

        return subscription_entity

    @error_interceptor(file_name=__name__)
    async def subscribe(self, subscription: SubscriptionEntity) -> None:
        """
        Подписаться на пользователя
        """
        subscription_model = self._mapper.load(
            from_model=subscription,
            to_model=Subscriptions
        )

        if subscription_model.subscription_id == subscription_model.subscriber_id:
            raise app.SubscribeOnYourself()

        self._session.add(subscription_model)

        try:
            await self._session.flush((subscription_model,))
        except IntegrityError as err:
            self._parse_error(err=err, data=subscription)

    @error_interceptor(file_name=__name__)
    async def unsubscribe(self, subscription: SubscriptionEntity) -> None:
        """
        Отписаться от пользователя
        """
        query = (
            delete(Subscriptions)
            .where(
                Subscriptions.subscription_id == (
                    subscription.subscription_user_id.to_int
                ),
                Subscriptions.subscriber_id == (
                    subscription.subscriber_user_id.to_int
                )
            )
        )

        await self._session.execute(query)

    @staticmethod
    def _parse_error(
            err: DBAPIError,
            data: SubscriptionEntity
    ) -> None:
        """
        Определение ошибки
        """
        error = err.__cause__.__cause__.__class__  # type: ignore

        if error == UniqueViolationError:
            raise app.SubscribeIsAlreadyExists()
        elif error == ForeignKeyViolationError:
            raise app.UserIsNotExist(user_id=data.subscription_user_id.to_int)
        else:
            raise app.RepoError() from err
