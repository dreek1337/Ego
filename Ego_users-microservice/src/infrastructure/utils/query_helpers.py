from sqlalchemy import Select, Column

from src.domain.common import Empty
from src.application import (
    GetSubscriptionsOrder,
    GetSubscriptionsFilters
)


def add_filters(
        *,
        query: Select,
        column_for_order: Column,
        filters: GetSubscriptionsFilters
) -> Select:
    """
    Добавление фильтров и сортировка
    """
    if filters.order == GetSubscriptionsOrder.DESC:
        query = query.order_by(column_for_order.desc())
    if filters.order == GetSubscriptionsOrder.ASC:
        query = query.order_by(column_for_order.asc())

    if filters.limit is not Empty.UNSET:
        query = query.limit(filters.limit)
    if filters.offset is not Empty.UNSET:
        query = query.offset(filters.offset)

    return query
