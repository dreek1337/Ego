import sqlalchemy as sa
from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from src.infrastructure.database.models.base import Base


class Subscriptions(Base):
    """
    Таблица, которая хранит данные о подписчках пользователей
    """
    __tablename__ = 'subscriptions'
    subscription_subscriber_id: Mapped[int] = mapped_column(
        sa.BigInteger,
        primary_key=True
    )
    subscription_id: Mapped[int] = mapped_column(
        sa.BigInteger,
        sa.ForeignKey('users.user_id')
    )
    subscriber_id: Mapped[int] = mapped_column(
        sa.BigInteger,
        sa.ForeignKey('users.user_id')
    )
